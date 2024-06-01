
from src.controllers.tag_creator_controller import TagCreatorController

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

class MockTagCreatorController:
    def create(self, product_code: str) -> dict:
        return {"product_code": product_code, "message": "Tag created"}

def test_tag_creator_view(monkeypatch):
    def mock_create(self, product_code: str) -> dict:
        return {"product_code": product_code, "message": "Tag created"}

    monkeypatch.setattr(TagCreatorController, "create", mock_create)
