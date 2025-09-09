# FastAPI RESTful API

A RESTful API built with FastAPI that provides basic endpoints for item management and serves as a foundation for building scalable web services with authentication and database integration capabilities.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Pip (usually comes with Python)

## Setup and Installation

Follow these steps to set up the development environment.

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create and Activate a Python Virtual Environment:

A virtual environment is a self-contained directory that contains a specific Python installation and any additional packages. This is a crucial best practice for managing project dependencies.

**On macOS and Linux:**

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

After activation, your terminal prompt will change to show `(venv)`, indicating you are now working inside the virtual environment.

**On Windows (Command Prompt / PowerShell):**

```cmd
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
```

Similarly, your command prompt will be prefixed with `(venv)`.

### 3. Install Dependencies:

With your virtual environment activated, install the required packages from the requirements.txt file.

```bash
pip install -r requirements.txt
```

### 4. Run the Application:

Start the development server using Uvicorn. The `--reload` flag will automatically restart the server whenever you make changes to the code.

```bash
uvicorn main:app --reload
```

The application will be running and available at http://127.0.0.1:8000.

## API Documentation

Once the server is running, you can access the interactive API documentation (provided automatically by FastAPI) at the following endpoints:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Available Endpoints

- `GET /` - Returns a welcome message
- `GET /items/{item_id}` - Retrieves an item by ID with optional query parameter

## Dependencies

This project uses the following key dependencies:

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library
- **Pydantic**: Data validation using Python type annotations
- **python-jose**: JWT token handling for authentication
- **passlib**: Password hashing library
- **bcrypt**: Password hashing algorithm

## Deactivating the Virtual Environment

When you are finished working on the project, you can exit the virtual environment by simply running:

```bash
deactivate
```

## Development

This project is set up with common dependencies for building a production-ready API with authentication capabilities. The current implementation provides basic endpoints that can be extended with additional functionality as needed.
