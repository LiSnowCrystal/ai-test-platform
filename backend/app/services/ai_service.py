from openai import OpenAI
import json

API_KEY = "登录硅基流动找APIKEY"
BASE_URL = "https://api.siliconflow.cn/v1"
MODEL_ID = "Qwen/Qwen3.5-9B"  # 免费模型

async def generate_test_cases(requirement_text: str):
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    prompt = f"""
    你是一位资深的软件测试工程师。请根据以下需求，生成详细的测试用例。

    需求：{requirement_text}

    请直接以 JSON 数组格式返回，不要包含任何其他解释或标记。
    每个用例需要包含：title, precondition, steps, expected_result。
    """

    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        content = response.choices[0].message.content
        start = content.find('[')
        end = content.rfind(']') + 1
        if start != -1:
            return json.loads(content[start:end])
        return {"error": "未找到JSON数组"}
    except Exception as e:
        return {"error": f"API调用失败: {str(e)}"}