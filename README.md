# Test Assignment for the Position of Python Engineer (GenAI) at 4Create
![Python](https://img.shields.io/badge/Python-3.13.2-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.14-green)
![Pydantic](https://img.shields.io/badge/Pydantic-2.11.5-green)<br>
![Docker](https://img.shields.io/badge/Docker-gray)
![Pytest](https://img.shields.io/badge/Pytest-gray)
<br>
## Table of Contents:

- [Introduction](#introduction)
- [Database Schema](#database-schema)
- [Setup Instructions](#setup-instructions)
----
### <anchor>Introduction</anchor>
This project implements a flexible and efficient data retrieval mechanism 
using modern technologies such as **FastAPI**, **Pydantic**, and **SQLAlchemy**. 
Special attention has been given to designing an architecture focused 
on component reusability and scalability, ensuring ease of maintenance 
and the possibility of straightforward functionality expansion.

The project includes data models for the main entities: **Posts**, **Comments**, **Tags**, and **Users**. 
REST API endpoints are provided for interacting with the data. 

The primary available endpoints are:<br>
* **GET** _**/api/posts?status=draft&include=tags,user**_<br>
— retrieves a list of posts with the ability to filter by status and include related tags and user information;<br>
<br>
* **GET** _**/api/posts/1?include=tags,user,comments**_<br> 
— retrieves a single post by ID, including related tags, author, and comments;<br>
<br>
* **GET** _**/api/users/1?include=posts,comments**_<br> 
— retrieves a user by ID, including their posts and comments.
The project also includes code testing and code style checks using the ruff linter.

### <anchor>Database Schema</anchor>
The table relationship schema in the database is presented as an ERD diagram and is available via URL: <br>
[https://drawsql.app/teams/singleplayer-2/diagrams/dataquerym](https://drawsql.app/teams/singleplayer-2/diagrams/dataquerym)

### <anchor>Setup Instructions</anchor>

1. Clone the repository:<br>
`git clone git@github.com:Andrey-Kugubaev/dqm.git`<br>
`cd dpm`<br>
<br>
2. Create a .env file in the root of the project and add the following parameters:<br>

`nano .env`
<br>
<br>
`APP_TITLE=Data Query Project`<br>
`DESCRIPTION = Test assignment for the position of Python Engineer (GenAI)`<br>
`DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres`<br>
<br>
4. Build and run the Docker containers<br>
`docker-compose up -d --build`<br>
_During the build, the database will be automatically populated with test data_<br>
<br>
5. Open the documentation in your browser:<br>
[http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs) (Swagger UI)<br>
<br>
6. To stop and remove the containers:<br>
`docker-compose down -v`<br>
<br>


Author: [https://github.com/Andrey-Kugubaev](https://github.com/Andrey-Kugubaev)