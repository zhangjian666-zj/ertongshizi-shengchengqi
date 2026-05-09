document.addEventListener("DOMContentLoaded", async () => {
    // ===== 配置区 =====
    // GitHub Pages 部署时如果另有后端 API，在这里设置地址
    // 例如: const API_BASE = "https://your-api.onrender.com";
    const API_BASE = window.API_BASE || "";
    // =================

    function api(path) {
        return API_BASE + path;
    }

    const themeSelect = document.getElementById("theme");
    const themeCustom = document.getElementById("themeCustom");
    const titleInput = document.getElementById("title");
    const form = document.getElementById("generateForm");
    const generateBtn = document.getElementById("generateBtn");
    const btnText = document.getElementById("btnText");
    const btnSpinner = document.getElementById("btnSpinner");
    const resultArea = document.getElementById("resultArea");
    const imageContainer = document.getElementById("imageContainer");
    const resultImage = document.getElementById("resultImage");
    const downloadLink = document.getElementById("downloadLink");
    const errorMessage = document.getElementById("errorMessage");
    const loadingDots = document.getElementById("loadingDots");
    const taskStatus = document.getElementById("taskStatus");
    const promptPreview = document.getElementById("promptPreview");
    const promptText = document.getElementById("promptText");

    // 加载本地主题列表（vocabulary.js 内置数据，无需后端）
    loadLocalThemes();

    // 检查后端 API 状态（如果有）
    checkStatus();

    themeSelect.addEventListener("change", () => {
        if (themeSelect.value) {
            themeCustom.value = "";
        }
    });

    themeCustom.addEventListener("input", () => {
        if (themeCustom.value) {
            themeSelect.value = "";
        }
    });

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const theme = themeSelect.value || themeCustom.value.trim();
        const title = titleInput.value.trim();

        if (!theme) {
            alert("请选择或输入主题");
            return;
        }
        if (!title) {
            alert("请输入小报标题");
            return;
        }

        await generatePoster(theme, title);
    });

    // ----- 本地主题加载（vocabulary.js） -----
    function loadLocalThemes() {
        const vocab = window.VOCABULARY || {};
        const themes = Object.keys(vocab);
        if (themes.length === 0) return;

        themes.forEach((t) => {
            const opt = document.createElement("option");
            opt.value = t;
            opt.textContent = t;
            themeSelect.appendChild(opt);
        });
    }

    // ----- 本地 prompt 生成 -----
    function buildPrompt(theme, title) {
        const vocab = window.VOCABULARY?.[theme];
        const core = vocab?.core || [];
        const items = vocab?.items || [];
        const env = vocab?.environment || [];

        function fmt(list) {
            return list.map(([p, c]) => `${p} ${c}`).join("\n");
        }

        return `请生成一张儿童识字小报《${theme}》，竖版 A4，学习小报版式，适合 5–9 岁孩子 认字与看图识物。

# 一、小报标题区（顶部）

**顶部居中大标题**：《${title}》
* **风格**：十字小报 / 儿童学习报感
* **文本要求**：大字、醒目、卡通手写体、彩色描边
* **装饰**：周围添加与 ${theme} 相关的贴纸风装饰，颜色鲜艳

# 二、小报主体（中间主画面）

画面中心是一幅 **卡通插画风的「${theme}」场景**：
* **整体气氛**：明亮、温暖、积极
* **构图**：物体边界清晰，方便对应文字，不要过于拥挤。

**场景分区与核心内容**
1.  **核心区域 A（主要对象）**：表现 ${theme} 的核心活动。
2.  **核心区域 B（配套设施）**：展示相关的工具或物品。
3.  **核心区域 C（环境背景）**：体现环境特征（如墙面、指示牌等）。

**主题人物**
* **角色**：1 位可爱卡通人物（职业/身份：与 ${theme} 匹配）。
* **动作**：正在进行与场景相关的自然互动。

# 三、必画物体与识字清单（Generated Content）

**请务必在画面中清晰绘制以下物体，并为其预留贴标签的位置：**

**1. 核心角色与设施：**
${fmt(core)}

**2. 常见物品/工具：**
${fmt(items)}

**3. 环境与装饰：**
${fmt(env)}

*(注意：画面中的物体数量不限于此，但以上列表必须作为重点描绘对象)*

# 四、识字标注规则

对上述清单中的物体，贴上中文识字标签：
* **格式**：两行制（第一行拼音带声调，第二行简体汉字）。
* **样式**：彩色小贴纸风格，白底黑字或深色字，清晰可读。
* **排版**：标签靠近对应的物体，不遮挡主体。

# 五、画风参数
* **风格**：儿童绘本风 + 识字小报风
* **色彩**：高饱和、明快、温暖 (High Saturation, Warm Tone)
* **质量**：8k resolution, high detail, vector illustration style, clean lines.`;
    }

    // ----- 生成主逻辑 -----
    async function generatePoster(theme, title) {
        resultArea.classList.remove("hidden");
        imageContainer.classList.add("hidden");
        errorMessage.classList.add("hidden");
        promptPreview.classList.add("hidden");
        loadingDots.classList.remove("hidden");
        taskStatus.textContent = "⏳ 处理中...";
        taskStatus.className = "status-badge";
        setButtonsDisabled(true);

        // 先生成本地 prompt
        const prompt = buildPrompt(theme, title);

        // 如果有后端 API，尝试调用
        if (API_BASE) {
            try {
                const resp = await fetch(api("/api/generate"), {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ theme, title }),
                });
                const data = await resp.json();

                if (data.success && data.image_url) {
                    taskStatus.textContent = "✅ 生成成功";
                    taskStatus.className = "status-badge success";
                    loadingDots.classList.add("hidden");
                    imageContainer.classList.remove("hidden");
                    resultImage.src = data.image_url;
                    resultImage.onload = () => {
                        const proxyUrl = api(`/api/proxy-image?url=${encodeURIComponent(data.image_url)}`);
                        downloadLink.href = proxyUrl;
                    };
                    return;
                }

                taskStatus.textContent = "❌ 生成失败";
                taskStatus.className = "status-badge fail";
                errorMessage.classList.remove("hidden");
                errorMessage.textContent = data.message || "未知错误";
            } catch (err) {
                taskStatus.textContent = "❌ 请求失败";
                taskStatus.className = "status-badge fail";
                errorMessage.classList.remove("hidden");
                errorMessage.textContent = "无法连接后端: " + err.message;
            }
        }

        // 没有后端 或 后端调用失败 → 显示 prompt 文本供复制使用
        loadingDots.classList.add("hidden");
        promptPreview.classList.remove("hidden");
        promptText.textContent = prompt;

        if (!API_BASE) {
            taskStatus.textContent = "📝 提示词已生成";
            taskStatus.className = "status-badge";
        }
    }

    function setButtonsDisabled(disabled) {
        generateBtn.disabled = disabled;
        if (disabled) {
            btnText.classList.add("hidden");
            btnSpinner.classList.remove("hidden");
        } else {
            btnText.classList.remove("hidden");
            btnSpinner.classList.add("hidden");
        }
    }

    // ----- 后端状态检查（仅在有 API_BASE 时） -----
    async function checkStatus() {
        const configDot = document.getElementById("configDot");
        const configText = document.getElementById("configText");

        if (!API_BASE) {
            configDot.className = "config-dot ok";
            configText.textContent = "纯前端模式 · 生图需自行复制提示词到 AI 绘图工具";
            return;
        }

        try {
            const resp = await fetch(api("/api/status"));
            const data = await resp.json();
            if (data.kie_configured) {
                configDot.className = "config-dot ok";
                configText.textContent = `API 已就绪 · 支持 ${data.supported_themes.length} 个主题`;
            } else {
                configDot.className = "config-dot err";
                configText.textContent = "⚠️ 后端 API Key 未配置";
            }
        } catch {
            configDot.className = "config-dot err";
            configText.textContent = "⚠️ 无法连接后端服务";
        }
    }
});
