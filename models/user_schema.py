from pydantic import BaseModel

class UserSchemaBase(BaseModel):
    telegram_id: int


class UserShema(UserSchemaBase):
    user_id: int
