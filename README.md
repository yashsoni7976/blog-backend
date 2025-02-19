# FastAPI Blog Backend

This is a backend API built with FastAPI to handle user authentication, user management, and blog posts. It uses JWT-based authentication, CRUD operations for users, and supports role-based access for different routes.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup & Installation](#setup-installation)
- [Configuration](#configuration)
- [Endpoints](#endpoints)
- [Testing](#testing)
- [Code Quality and Optimization](#code-quality-and-optimization)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project provides an API for managing users and blog posts. The core functionalities include:

- **User Authentication**: Users can register, log in, and access protected resources using JWT tokens.
- **User Management**: Admin can perform CRUD operations on user data.

## Technologies Used

- **Python 3.x**
- **FastAPI**: Fast API framework for building APIs
- **SQLAlchemy**: ORM for database interaction
- **JWT**: For user authentication using JSON Web Tokens
- **PostgresSQL**: Database for development (you can easily swap it with PostgreSQL, MySQL, etc.)
- **Pydantic**: For request validation
- **Alembic**: For database migrations
- **Pylint**: For code linting and style checks
