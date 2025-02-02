# FastAPI Recipe Suggester

This project is a FastAPI application that generates recipe suggestions using OpenAI's GPT models. It provides an API endpoint to interact with the OpenAI service and fetch personalized recipe ideas based on user input.

## Project Structure

```
fastapi-recipe-suggester
├── app
│   ├── api
│   │   ├── endpoints
│   │   │   └── recipes.py  # API endpoints for generating recipe suggestions
│   │   └── __init__.py      # Initializes the API module
│   ├── core
│   │   ├── config.py        # Configuration settings (API keys, etc.)
│   │   └── __init__.py      # Initializes the core module
│   ├── models
│   │   └── __init__.py      # Data models for request and response validation
│   ├── services
│   │   ├── openai_service.py # Logic for interacting with OpenAI's GPT models
│   │   └── __init__.py      # Initializes the services module
│   ├── main.py               # Entry point of the FastAPI application
│   └── __init__.py          # Initializes the app module
├── requirements.txt          # Lists project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-recipe-suggester
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key in the `app/core/config.py` file.

4. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

## Usage

Once the application is running, you can access the API at `http://localhost:8000`. Use the `/recipes` endpoint to get recipe suggestions by sending a request with the necessary parameters.

## License

This project is licensed under the MIT License.