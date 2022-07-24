# Library Reservation System

<img width="600" alt="resim" src="https://user-images.githubusercontent.com/60014138/180317482-4840c017-6606-410e-b605-eb0fceef6fc4.png">
<img width="600" alt="resim" src="https://user-images.githubusercontent.com/60014138/180317536-e950e116-6fb7-417c-94a8-751348745259.png">

## What is the purpose? / Working Principle

This system will be used for reservation in library. Filled tables and available ones will be shown on main page. Also user can add or extract table from database.

## Technologies

Django Web Framework, Python, HTML, CSS and JS.

## How to setup

`git clone https://github.com/canerucal/library.git`

`cd mainApp`

`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

`.env file must be created in main project folder. And SECRET_KEY, DB_NAME, DB_PASSWORD values must be defined. Otherwise it won't work`

`Another solution is you can modify settings.py file. But it is not recommended because of security issues.`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

And also you need to create a database. Table and column names can be found on models.py.
