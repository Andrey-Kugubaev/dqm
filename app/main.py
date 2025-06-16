from fastapi import FastAPI

from app.api.posts import router as post_router
from app.api.users import router as user_router
from app.core.config import settings

app = FastAPI(title=settings.app_title, description=settings.description)

app.include_router(post_router)
app.include_router(user_router)
