from app.schemas.full.comments_full import CommentDB
from app.schemas.full.posts_full import PostDB
from app.schemas.full.tags_full import TagDB
from app.schemas.full.users_full import UserDB

UserDB.model_rebuild()
PostDB.model_rebuild()
CommentDB.model_rebuild()
TagDB.model_rebuild()
