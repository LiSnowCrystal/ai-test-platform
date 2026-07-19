from fastapi import APIRouter
from ..services.workflow import run_generation_workflow

router = APIRouter()

@router.post("/projects/{project_id}/generate")
async def generate_cases(project_id: int, requirement: str):
    """生成测试用例（同步返回结果）"""
    result = await run_generation_workflow(project_id, requirement)
    return result  # 直接返回生成的用例列表