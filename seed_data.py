import asyncio
import logging
import os
import random

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.base import Base
from app.models.comments import Comments
from app.models.posts import Posts
from app.models.tags import Tags
from app.models.users import Users
from app.schemas.base.posts_base import PostStatus
from app.schemas.base.users_base import GenderValue, UserBase

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

male_names = [
    "Nikola", "Miloš", "Marko", "Stefan", "Luka",
    "Đorđe", "Vladimir", "Aleksandar", "Nenad", "Ivan"
]
female_names = [
    "Ana", "Jovana", "Marija", "Ivana", "Teodora",
    "Milica", "Jelena", "Sara", "Katarina", "Tamara"
]
serbian_surnames = [
    "Petrović", "Jovanović", "Nikolić", "Marković", "Đorđević",
    "Stojanović", "Ilić", "Pavlović", "Stefanović", "Milanković"
]

sample_titles = [
    "How to cook river crayfish", "Top Serbian dishes",
    "A short history of Belgrade", "A walk through Drvar",
    "10 places to visit in Montenegro", "Cat photography tips",
    "What is Kajmak?", "Best ćevapi in the Balkans", "Gusle and folk music",
    "Coffee with rakija: cultural etiquette"
]

sample_tags = [
    "food", "travel", "history", "culture", "Belgrade", "photography",
    "music", "tradition", "tips", "cats"
]

statuses = list(PostStatus)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_users():
    async with AsyncSessionLocal() as session:
        for _ in range(20):
            if random.choice([True, False]):
                name = random.choice(male_names)
                gender = GenderValue.MALE
            else:
                name = random.choice(female_names)
                gender = GenderValue.FEMALE

            surname = random.choice(serbian_surnames)
            age = random.randint(15, 99)
            base_email = f"{name.lower()}.{surname.lower()}@example.com"

            email = await generate_unique_email(session, base_email)

            user_data = {
                "name": name,
                "surname": surname,
                "age": age,
                "gender": gender,
                "email": email
            }

            validated = UserBase(**user_data)
            user_row = Users(**validated.model_dump())
            session.add(user_row)

        await session.commit()
    logging.info("20 users successfully added")


async def is_email_unique(session: AsyncSession, email: str) -> bool:
    result = await session.execute(select(Users).filter_by(email=email))
    return result.scalar_one_or_none() is None


async def generate_unique_email(session: AsyncSession, base_email: str) -> str:
    email = base_email
    attempt = 0
    while not await is_email_unique(session, email):
        attempt += 1
        if attempt > 100:
            raise Exception("Too many attempts to generate unique email")
        local_part, domain = base_email.split("@")
        email = f"{local_part}{attempt}@{domain}"
    return email


async def is_title_unique(session: AsyncSession, title: str) -> bool:
    result = await session.execute(select(Posts).filter_by(title=title))
    return result.scalar_one_or_none() is None


async def generate_unique_title(session: AsyncSession, base_title: str) -> str:
    title = base_title
    attempt = 0
    while not await is_title_unique(session, title):
        attempt += 1
        if attempt > 20:
            raise Exception("Too many attempts to generate unique title")
        title = f"{base_title} #{random.randint(1, 1000)}"
    return title


async def create_posts_and_tags():
    async with AsyncSessionLocal() as session:
        existing_tags = await session.execute(select(Tags.name))
        existing_tag_names = {row[0] for row in existing_tags.all()}
        new_tags = [
            Tags(name=tag) for tag in sample_tags
            if tag not in existing_tag_names
        ]
        session.add_all(new_tags)
        await session.flush()

        tags = (await session.execute(select(Tags))).scalars().all()

        for _ in range(20):
            user = (
                await session.execute(
                    select(Users).order_by(func.random()).limit(1)
                )
            ).scalar()
            if not user:
                logging.info("No users found, please add them first.")
                return

            base_title = random.choice(sample_titles)
            title = await generate_unique_title(session, base_title)

            post = Posts(
                title=title,
                text=(
                    "This is a sample blog post about "
                    "Balkan culture, cuisine, or lifestyle."
                ),
                status=random.choice(statuses),
                image=None if random.random() < 0.5 else "https://placekitten.com/300/200",
                user_id=user.id
            )
            post.tags = random.sample(tags, k=random.randint(1, 3))
            session.add(post)

        await session.commit()
    logging.info("Posts and tags successfully added")


async def add_comments_to_existing_posts():
    async with AsyncSessionLocal() as session:
        posts = (await session.execute(select(Posts))).scalars().all()
        users = (await session.execute(select(Users))).scalars().all()

        if not posts:
            logging.info("No posts found in the database")
            return
        if not users:
            logging.info("No users found in the database")
            return

        for post in posts:
            for _ in range(random.randint(1, 3)):
                comment = Comments(
                    text="This is a sample comment.",
                    user_id=random.choice(users).id,
                    post_id=post.id
                )
                session.add(comment)
        await session.commit()
    logging.info(f"Added 1-3 comments to each of {len(posts)} posts.")


async def main():
    await create_tables()
    await create_users()
    await create_posts_and_tags()
    await add_comments_to_existing_posts()


if __name__ == "__main__":
    asyncio.run(main())
