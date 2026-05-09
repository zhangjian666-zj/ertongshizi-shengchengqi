import asyncio
import json
import os
import time
import logging

import httpx
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class KIEClient:
    """KIE API 客户端，封装 Nano Banana Pro 生图调用"""

    def __init__(self):
        self.api_key = os.getenv("KIE_API_KEY", "")
        self.base_url = os.getenv("KIE_API_BASE", "https://api.kie.ai")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    @property
    def is_configured(self) -> bool:
        return bool(self.api_key) and self.api_key != "your_api_key_here"

    async def create_task(self, prompt: str, aspect_ratio: str = "3:4") -> dict:
        """提交生图任务到 KIE API

        Args:
            prompt: 完整的绘图提示词
            aspect_ratio: 图片比例，默认 3:4（A4竖版）

        Returns:
            {"task_id": "task_xxx"} 或错误信息
        """
        if not self.is_configured:
            return {"error": "KIE_API_KEY 未配置，请在 .env 文件中设置"}

        payload = {
            "model": "nano-banana-pro",
            "callBackUrl": "",
            "input": {
                "prompt": prompt,
                "image_input": [],
                "aspect_ratio": aspect_ratio,
                "resolution": "2K",
                "output_format": "png",
            },
        }

        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                f"{self.base_url}/api/v1/jobs/createTask",
                headers=self.headers,
                json=payload,
            )
            data = resp.json()
            logger.info("KIE createTask response: %s", data)

            if resp.status_code != 200 or data.get("code") != 200:
                return {"error": data.get("msg", f"HTTP {resp.status_code}")}

            return {"task_id": data["data"]["taskId"]}

    async def query_task(self, task_id: str) -> dict:
        """查询任务状态和结果

        Returns:
            {"state": "success", "image_urls": [...], ...}
            或 {"state": "fail", "error": "..."}
        """
        async with httpx.AsyncClient(timeout=15) as client:
            resp = await client.get(
                f"{self.base_url}/api/v1/jobs/recordInfo",
                headers=self.headers,
                params={"taskId": task_id},
            )
            data = resp.json()
            logger.info("KIE recordInfo response: %s", data)

            if resp.status_code != 200 or data.get("code") != 200:
                return {"state": "fail", "error": data.get("msg", "查询失败")}

            task_data = data["data"]
            state = task_data.get("state", "unknown")
            result = {
                "task_id": task_data.get("taskId"),
                "state": state,
            }

            if state == "success":
                try:
                    result_json = json.loads(task_data.get("resultJson", "{}"))
                    result["image_urls"] = result_json.get("resultUrls", [])
                except json.JSONDecodeError:
                    result["image_urls"] = []
            elif state == "fail":
                result["error"] = task_data.get("failMsg", "生成失败")

            return result

    async def wait_for_result(
        self, task_id: str, poll_interval: float = 3.0, max_wait: float = 120.0
    ) -> dict:
        """轮询等待任务完成

        Args:
            task_id: 任务ID
            poll_interval: 轮询间隔（秒）
            max_wait: 最大等待时间（秒）

        Returns:
            最终任务结果
        """
        start = time.time()
        while True:
            result = await self.query_task(task_id)
            state = result.get("state")

            if state in ("success", "fail"):
                return result

            if time.time() - start > max_wait:
                return {"state": "timeout", "error": f"等待超时（{max_wait}s）"}

            await asyncio.sleep(poll_interval)

    async def generate(self, prompt: str, aspect_ratio: str = "3:4") -> dict:
        """完整生图流程：提交 → 轮询 → 返回结果"""
        create_result = await self.create_task(prompt, aspect_ratio)
        if "error" in create_result:
            return create_result

        task_id = create_result["task_id"]
        return await self.wait_for_result(task_id)


