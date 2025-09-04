1️⃣ Project Title & Description
Little Lemon Web Application
A Django REST API for a restaurant with menu and booking functionality. Includes user registration and token authentication.

2️⃣ How to run locally
1. Copy .env.example to .env and fill in your database credentials.
2. Create virtual environment and activate it:
   python -m venv .venv
   .venv\Scripts\activate  (Windows)
3. Install requirements:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Create superuser (optional):
   python manage.py createsuperuser
6. Start the server:
   python manage.py runserver

3️⃣ Environment variables

Include a .env.example with placeholders:

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=3306

4️⃣ How to obtain tokens
1. Register a user:
   POST /api/registration/register/
   Body (JSON): {"username": "testuser", "password": "TestPass123!", "email": "test@example.com"}
   Returns: token

2. Login for token:
   POST /api/api-token-auth/
   Body (JSON): {"username": "testuser", "password": "TestPass123!"}
   Returns: token

Use the token in headers for protected endpoints:
   Authorization: Token <token>

5️⃣ Key endpoints to test
/api/menu-items/             (GET)
/api/menu-items/<id>/        (GET)
/api/bookings/               (GET, POST, PUT, DELETE)  # requires auth
/api/registration/register/  (POST)
/api/api-token-auth/         (POST)
/                            (GET)  # static homepage

6️⃣ How to run tests
python manage.py test

7️⃣ GitHub repository
https://github.com/ayoub-bazzi/littlelemon-backend.git