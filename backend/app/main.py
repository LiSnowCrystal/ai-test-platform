from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import projects, tasks
from .database import engine, Base

# 创建数据库表（如果不存在的话）
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],   # 允许前端访问
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(projects.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "智能测试用例生成平台 API 已启动"}