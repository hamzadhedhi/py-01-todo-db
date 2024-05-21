# Todo CRUD FastAPI

This project is a simple Todo application built using FastAPI. It allows you to perform CRUD (Create, Read, Update, Delete) operations on todo items.

## Features

- Create a new todo item
- Read all todo items
- Update an existing todo item by ID
- Delete a todo item by ID

## Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/) for dependency management
- Supabase account for database

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hamzadhedhi/py-01-todo-db.git
   cd py-01-todo-db
   ```

2. **Install Poetry:**

   Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) to install Poetry.

3. **Install the dependencies:**

   ```bash
   poetry install
   ```

4. **Set up your environment variables:**

   Create a `.env` file in the root directory of your project and add your Supabase connection string. Make sure to replace the first `postgres` with `postgresql` in the URI so it works with SQLModel.

   ```plaintext
   URI=postgresql://yourusername:yourpassword@yourdbhost:5432/yourdbname
   ```

### Running the Application

1. **Run the FastAPI server:**

   ```bash
   poetry run dev
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the application running.

3. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Supabase](https://supabase.io/)
- [Poetry](https://python-poetry.org/)