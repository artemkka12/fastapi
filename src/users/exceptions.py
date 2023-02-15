from fastapi import HTTPException


class UserAlreadyExistsException(HTTPException):
    def __init__(self, email: str):
        super().__init__(status_code=400, detail=f"User with email {email} already exists.")


class UserNotFoundException(HTTPException):
    def __init__(self, user_id: int):
        super().__init__(status_code=404, detail=f"User with id {user_id} does not exist.")
