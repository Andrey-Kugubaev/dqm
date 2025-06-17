from pydantic import BaseModel, ConfigDict


class CommentBase(BaseModel):
    text: str

    model_config = ConfigDict(from_attributes=True)
