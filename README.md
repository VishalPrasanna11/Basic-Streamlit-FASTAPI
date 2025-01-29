# Basic-Streamlit-FASTAPI

A full-stack application built with FastAPI backend and Streamlit frontend for managing an online bookshop.

## Project Structure

```
online-bookshop/
├── __pycache__/
├── .devcontainer/
├── .streamlit/
├── venv/
├── .gitignore
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── start.sh
└── streamlit_app.py
```

### .gitignore Configuration
```
# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual Environment
venv/
.env

# IDE and Development
.devcontainer/
.vscode/
*.swp
*.swo

# Streamlit
.streamlit/

# System Files
.DS_Store
```

## Backend Deployment (Render)

### Prerequisites
- A [Render](https://render.com) account
- Git repository with your code

### Backend Requirements
The project uses a single `requirements.txt` file for both the FastAPI backend and Streamlit frontend:

```
fastapi==0.68.0
uvicorn==0.15.0
pydantic==1.8.2
python-dotenv==0.19.0
streamlit==1.22.0
requests==2.28.2
pandas==1.5.3
```

### Deployment Steps for Backend

1. Log in to your Render account
2. Click on "New +" and select "Web Service"
3. Connect your Git repository
4. Configure the service:
   - Name: `bookshop-api` (or your preferred name)
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `./start.sh`
   - Add the following environment variables:
     - `PORT`: `10000`
5. Click "Create Web Service"

The backend will be available at: `https://your-service-name.onrender.com`

## Frontend Deployment (Streamlit)

### Deployment Steps for Frontend

1. Log in to your Render account
2. Click on "New +" and select "Web Service"
3. Connect your Git repository
4. Configure the service:
   - Name: `bookshop-frontend` (or your preferred name)
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run streamlit_app.py`
   - Add the following environment variables:
     - `PORT`: `8501`
     - `API_URL`: `https://your-backend-service.onrender.com`
5. Click "Create Web Service"

## Local Development

### Running the Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Running the Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Environment Variables

### Backend
- `PORT`: The port number for the FastAPI server (default: 10000)

### Frontend
- `API_URL`: The URL of your backend service
- `PORT`: The port number for the Streamlit server (default: 8501)

## API Endpoints

- `GET /books/`: Get all books
- `GET /books/{book_id}`: Get a specific book by ID
- `POST /books/`: Add a new book

## Security Considerations

1. Add CORS middleware in the backend to restrict access to your frontend domain
2. Implement rate limiting for API endpoints
3. Add authentication for sensitive operations
4. Use HTTPS for all communications

## Troubleshooting

1. **Backend Connection Issues**
   - Verify the `API_URL` environment variable is set correctly
   - Check if the backend service is running
   - Verify CORS settings

2. **Deployment Issues**
   - Check Render logs for error messages
   - Verify all requirements are properly listed in requirements.txt
   - Ensure start commands are correct
   - Check if environment variables are properly set

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.