from pydantic import BaseModel


class CommentBase(BaseModel):
    text: str

    model_config = {"from_attributes": True}
