import pytest

from app.models.users import Users


@pytest.fixture
def user(mixer):
    return mixer.blend(
        Users,
        name="Alice",
        surname="Smith",
        email="alice@example.com",
        gender="female",
        age=30
    )
