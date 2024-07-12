from fastapi.testclient import TestClient
from app.main import app
# for eg
# def test_hello():
#     greet = "Hi"
#     assert greet == "Hi"

# test_hello()

client = TestClient(app=app)

def test_todo():
    response = client.get("/")
    assert response.json() == {}

