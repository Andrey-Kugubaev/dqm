import pytest

from app.models.comments import Comments
from app.models.posts import Posts
from app.models.tags import Tags


@pytest.fixture
def tags(mixer):
    return mixer.cycle(2).blend(Tags, name=(t for t in ["tech", "life"]))


@pytest.fixture
def post_with_relations(mixer, user, tags):
    post = mixer.blend(
        Posts,
        title="Test Post",
        text="Lorem ipsum",
        status="draft",
        user=user,
        tags=[]
    )

    for tag in tags:
        post.tags.append(tag)

    mixer.blend(Comments, text="Nice post!", user=user, post=post)

    return post
