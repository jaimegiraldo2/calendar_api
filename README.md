# calendar_api
basic calendar api

Requirements

    Python 3.6+ (tested with Python 3.8).
    Django 2.2 and other dependencies declared in the requirements.txt file (use virtual environments!).
    
Install and Run

(Optional) Create a virtual environment and activate it with:

$ python3 -m venv .venv && source .venv/bin/activate

Install dependencies with:

$ pip install -r requirements.txt

Create the database with:

$ python3 manage.py makemigrations
$ python3 manage.py migrate

To create an admin user:

$ python3 manage.py createsuperuser

Then run in development mode with:

$ python3 manage.py runserver
