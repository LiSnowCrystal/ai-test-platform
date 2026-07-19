from pydantic import BaseModel
from typing import List, Optional

# 用于创建项目的请求体
class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

# 用于返回项目信息的响应体
class Project(ProjectCreate):
    id: int

    class Config:
        orm_mode = True

# 用于返回测试用例信息的响应体
class TestCase(BaseModel):
    id: int
    title: str
    precondition: str
    steps: str
    expected_result: str
    project_id: int

    class Config:
        orm_mode = True