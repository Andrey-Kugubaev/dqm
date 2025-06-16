from pydantic import BaseModel, ConfigDict


class TagBase(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)
