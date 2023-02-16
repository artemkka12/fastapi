from fastapi import HTTPException

__all__ = ["ItemNotFoundException"]


class ItemNotFoundException(HTTPException):
    def __init__(self, item_id: int):
        super().__init__(status_code=404, detail=f"Item with id {item_id} does not exist.")
