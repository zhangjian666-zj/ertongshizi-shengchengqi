import logging
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import httpx

from app.kie_client import KIEClient
from app.prompt_engine import fill_prompt
from app.vocabulary import get_theme_list

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="儿童识字小报生成器")

# CORS — 允许前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# 挂载静态文件
static_dir = os.path.join(ROOT_DIR, "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

kie_client = KIEClient()


class GenerateRequest(BaseModel):
    theme: str
    title: str


class GenerateResponse(BaseModel):
    success: bool
    message: str
    task_id: str | None = None
    image_url: str | None = None


@app.get("/", response_class=HTMLResponse)
async def index():
    # 优先返回根目录 index.html（GitHub Pages 兼容）
    root_index = os.path.join(ROOT_DIR, "index.html")
    if os.path.exists(root_index):
        with open(root_index, encoding="utf-8") as f:
            return HTMLResponse(f.read())
    return HTMLResponse("<h1>儿童识字小报生成器</h1><p>根目录缺少 index.html</p>")


@app.get("/api/themes")
async def list_themes():
    """获取支持的主题列表"""
    return {"themes": get_theme_list()}


@app.get("/api/status")
async def api_status():
    """检查 API 配置状态"""
    return {
        "kie_configured": kie_client.is_configured,
        "supported_themes": get_theme_list(),
    }


@app.post("/api/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    """生成识字小报"""
    # 1. 填充提示词
    prompt = fill_prompt(req.theme, req.title)

    # 2. 检查 KIE 配置
    if not kie_client.is_configured:
        return GenerateResponse(
            success=False,
            message="KIE_API_KEY 未配置，请在 .env 文件中设置 API Key",
        )

    # 3. 调用 KIE API 生图
    result = await kie_client.generate(prompt)

    if "error" in result:
        logger.error("生成失败: %s", result["error"])
        return GenerateResponse(
            success=False,
            message=f"生成失败: {result['error']}",
        )

    image_urls = result.get("image_urls", [])
    return GenerateResponse(
        success=True,
        message="生成成功！",
        task_id=result.get("task_id"),
        image_url=image_urls[0] if image_urls else None,
    )


@app.get("/api/proxy-image")
async def proxy_image(url: str):
    """代理下载图片，避免前端跨域问题"""
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        content_type = resp.headers.get("content-type", "image/png")
        return Response(content=resp.content, media_type=content_type)
