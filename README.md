# 智能测试用例生成平台

> 一款输入需求描述即可自动生成结构化测试用例的 AI 提效工具

## ✨ 项目背景

在软件测试流程中，编写测试用例是一项重复性高、耗时长的劳动。本项目通过集成大语言模型 API，将"需求描述 → 测试用例"的转换过程自动化，帮助测试人员快速生成用例草稿，大幅提升工作效率。

## 🚀 功能特性

- 📁 项目管理：创建项目、查看项目列表
- 🤖 智能生成：输入需求描述，AI 自动生成结构化测试用例（含标题、前置条件、测试步骤、预期结果）
- 📊 表格展示：生成的用例以清晰表格呈现，一目了然
- 🔄 降级保障：AI 服务不可用时自动切换为模拟模式，确保演示永不中断

## 🛠️ 技术栈

| 分类 | 技术 |
|------|------|
| 前端 | Vue 3 + Vite + Element Plus |
| 后端 | FastAPI + SQLAlchemy |
| 数据库 | SQLite |
| AI 服务 | 硅基流动 API（Qwen3.5-9B） |
| 测试 | Pytest + FastAPI TestClient |

## 🏃 快速启动

### 1. 后端启动

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
uvicorn app.main:app --reload
```

后端访问地址：`http://localhost:8000`

### 2. 前端启动

```bash
cd frontend
npm install
npm run dev
```

前端访问地址：`http://localhost:5173`

## 📸 效果预览

（建议放两张项目截图：一张项目列表页，一张用例生成结果页）

## 📁 项目结构

```
├── backend/          # 后端代码（FastAPI）
│   ├── app/
│   │   ├── routers/  # API 路由
│   │   ├── services/ # AI 服务 & 工作流
│   │   ├── models.py # 数据模型
│   │   └── main.py   # 应用入口
│   └── test_api.py   # 自动化测试
├── frontend/         # 前端代码（Vue 3）
│   └── src/
│       ├── api/      # API 请求封装
│       └── App.vue   # 主页面
└── .gitignore
```

## 📝 后续规划

- [ ] 接入真实 AI API（当前为模拟模式）
- [ ] 支持用例导出为 Excel / Markdown
- [ ] 支持用例编辑和版本管理
- [ ] 支持批量生成

## 👩‍💻 作者

**李雪晶** | 河北农业大学 · 计算机科学与技术（2027届）
- GitHub：[@LiSnowCrystal](https://github.com/LiSnowCrystal)

## 📄 许可证

MIT License
