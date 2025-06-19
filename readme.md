Mood Journal – A Beginner Flask App
A simple web app built using Flask that lets users log their daily mood.
This project was created as a hands-on way to learn the basics of Flask and backend development.

Features
View homepage and multiple routes

Submit moods through a form

Display list of submitted moods

Use of HTML templates with Jinja2

Handling POST/GET requests

Linking static files (CSS/JS)

Clean, beginner-friendly code structure

What I Learned
Setting up a Flask project and routing

Using Jinja2 for HTML templating

Handling form data using GET/POST

Connecting Python (backend) with frontend files

Creating reusable templates and static files

Project structuring for scalability

Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

Templating Engine: Jinja2

Local Server: Flask Development Server

Getting Started
Clone the Repository
git clone https://github.com/your-username/mood-journal.git
cd mood-journal

Create Virtual Environment
python -m venv venv
source venv/bin/activate (On Windows: venv\Scripts\activate)

Install Flask
pip install Flask

Run the App
python app.py

The app will be available at http://127.0.0.1:5000/

Project Structure
mood-journal/
├── app.py
├── static/
│ ├── style.css
│ └── script.js
├── templates/
│ ├── index.html
│ ├── about.html
│ ├── add_mood.html
│ └── moods.html
└── README.txt

Future Plans
Add SQLite database for permanent mood storage

User authentication with Flask-Login

Responsive design with Bootstrap

Deploy the app to Render or Railway