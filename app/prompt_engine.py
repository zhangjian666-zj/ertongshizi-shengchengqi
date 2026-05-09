"""提示词模板引擎 — 从 prompt.md 加载模板并填充词汇"""

from app.vocabulary import get_vocabulary


# 自定义主题的通用词汇占位
FALLBACK_VOCAB = {
    "core": [
        ("rén wù", "人物"),
        ("jiàn zhù", "建筑"),
        ("shè shī", "设施"),
        ("gōng jù", "工具"),
        ("zhuāng shì", "装饰"),
    ],
    "items": [
        ("wù pǐn 1", "物品1"),
        ("wù pǐn 2", "物品2"),
        ("wù pǐn 3", "物品3"),
        ("wù pǐn 4", "物品4"),
        ("wù pǐn 5", "物品5"),
        ("wù pǐn 6", "物品6"),
    ],
    "environment": [
        ("huán jìng 1", "环境1"),
        ("huán jìng 2", "环境2"),
        ("huán jìng 3", "环境3"),
    ],
}


def fill_prompt(theme: str, title: str) -> str:
    """根据主题和标题，填充 prompt.md 模板

    返回完整的绘图提示词，自定义主题会使用占位词汇
    """
    vocab = get_vocabulary(theme) or FALLBACK_VOCAB

    # 格式化词汇列表：拼音 汉字
    def fmt(words, prefix=""):
        return "\n".join(f"{prefix}{p} {c}" for p, c in words)

    core_text = fmt(vocab["core"])
    items_text = fmt(vocab["items"])
    env_text = fmt(vocab["environment"])

    # 构建提示词
    prompt = f"""请生成一张儿童识字小报《{theme}》，竖版 A4，学习小报版式，适合 5–9 岁孩子 认字与看图识物。

# 一、小报标题区（顶部）

**顶部居中大标题**：《{title}》
* **风格**：十字小报 / 儿童学习报感
* **文本要求**：大字、醒目、卡通手写体、彩色描边
* **装饰**：周围添加与 {theme} 相关的贴纸风装饰，颜色鲜艳

# 二、小报主体（中间主画面）

画面中心是一幅 **卡通插画风的「{theme}」场景**：
* **整体气氛**：明亮、温暖、积极
* **构图**：物体边界清晰，方便对应文字，不要过于拥挤。

**场景分区与核心内容**
1.  **核心区域 A（主要对象）**：表现 {theme} 的核心活动。
2.  **核心区域 B（配套设施）**：展示相关的工具或物品。
3.  **核心区域 C（环境背景）**：体现环境特征（如墙面、指示牌等）。

**主题人物**
* **角色**：1 位可爱卡通人物（职业/身份：与 {theme} 匹配）。
* **动作**：正在进行与场景相关的自然互动。

# 三、必画物体与识字清单（Generated Content）

**请务必在画面中清晰绘制以下物体，并为其预留贴标签的位置：**

**1. 核心角色与设施：**
{core_text}

**2. 常见物品/工具：**
{items_text}

**3. 环境与装饰：**
{env_text}

*(注意：画面中的物体数量不限于此，但以上列表必须作为重点描绘对象)*

# 四、识字标注规则

对上述清单中的物体，贴上中文识字标签：
* **格式**：两行制（第一行拼音带声调，第二行简体汉字）。
* **样式**：彩色小贴纸风格，白底黑字或深色字，清晰可读。
* **排版**：标签靠近对应的物体，不遮挡主体。

# 五、画风参数
* **风格**：儿童绘本风 + 识字小报风
* **色彩**：高饱和、明快、温暖 (High Saturation, Warm Tone)
* **质量**：8k resolution, high detail, vector illustration style, clean lines."""

    return prompt
