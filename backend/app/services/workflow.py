from .ai_service import generate_test_cases

async def run_generation_workflow(project_id: int, requirement: str):
    """执行完整的用例生成工作流"""
    print(f"开始为项目 {project_id} 生成测试用例...")
    # 调用 AI 服务生成用例
    result = await generate_test_cases(requirement)
    print("AI 生成结果:", result)
    # 这里我们只打印结果，之后我们会把它保存到数据库
    return result