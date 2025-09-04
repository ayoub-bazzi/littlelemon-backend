🍋 Little Lemon Web Application

A Django REST API for a restaurant with menu and booking functionality.
Includes user registration, token authentication, and a static homepage.

🚀 How to Run Locally

Clone the repository

git clone https://github.com/ayoub-bazzi/littlelemon-backend.git
cd littlelemon-backend


Set up environment

Copy .env.example to .env

Fill in your database credentials

Create virtual environment & activate it

python -m venv .venv
.venv\Scripts\activate   # (Windows)
source .venv/bin/activate  # (Linux/Mac)


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Create superuser (optional)

python manage.py createsuperuser


Run the server

python manage.py runserver

⚙️ Environment Variables

Example .env.example file:

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=3306

🔑 Authentication
Register a new user
POST /api/registration/register/
Body: {
  "username": "testuser",
  "password": "TestPass123!",
  "email": "test@example.com"
}


👉 Returns: {"token": "<your_token>"}

Get token (login)
POST /api/api-token-auth/
Body: {
  "username": "testuser",
  "password": "TestPass123!"
}


👉 Returns: {"token": "<your_token>"}

Use token in requests
Authorization: Token <your_token>

📌 Key Endpoints
Endpoint	Method(s)	Notes
/	GET	Static homepage
/api/menu-items/	GET	List all menu items
/api/menu-items/<id>/	GET	Retrieve menu item by ID
/api/bookings/	GET, POST, PUT, DELETE	Requires auth
/api/registration/register/	POST	User registration
/api/api-token-auth/	POST	Get auth token
🧪 Running Tests

Run all tests:

python manage.py test

📝 Submission Info

GitHub Repository: https://github.com/ayoub-bazzi/littlelemon-backend

Static homepage: /

API ready with Menu, Bookings, and Auth

Tested endpoints included above