from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_project():
    response = client.post("/projects", json={"name": "测试项目", "description": "描述"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "测试项目"
    assert "id" in data


def test_get_projects():
    response = client.get("/projects")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_generate_cases():
    # 先确保有一个项目存在（如果数据库是空的，先创建）
    create_resp = client.post("/projects", json={"name": "测试项目", "description": "描述"})
    project_id = create_resp.json()["id"]

    response = client.post(f"/projects/{project_id}/generate?requirement=用户登录功能")
    assert response.status_code == 200
    result = response.json()
    # 验证返回的是列表（模拟模式返回3条用例）
    assert isinstance(result, list)
    if len(result) > 0:
        assert "title" in result[0]
        assert "steps" in result[0]


def test_generate_cases_empty():
    # 先确保有一个项目存在
    create_resp = client.post("/projects", json={"name": "测试项目", "description": "描述"})
    project_id = create_resp.json()["id"]

    response = client.post(f"/projects/{project_id}/generate?requirement=")
    # 模拟模式会生成3条用例，即使需求为空
    assert response.status_code == 200


def test_generate_cases_long():
    create_resp = client.post("/projects", json={"name": "测试项目", "description": "描述"})
    project_id = create_resp.json()["id"]

    long_text = "用户登录功能" * 50
    response = client.post(f"/projects/{project_id}/generate?requirement={long_text}")
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)