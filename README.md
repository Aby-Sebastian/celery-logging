# Celery-Logging-File-Generator

A File Generation application built with `python` `django` `Celery` `Redis`. When user inputs filename and number of rows, django views calles a celery task named generate_file and passes user inputs as arguments. The celery Task creates a csv file with the specified number of rows and in the given filename. The task_id, task_status and the arguments are then inserted into the database.

A simple, reponsive  website. Built with:

- Python 🐍
- Django 🎸
- Bootstrap 4 🌈
- Sqlite3
- Celery
- Redis (Broker)
- HTML
- CSS

## Features

- Generates csv files according to user input filename and no of rows
- Inserts status of Celery Task to Database
- sends email when new user registers to the application


## How to run this project (Ubuntu 18.04)

1. **Clone the project**

```sh
git clone https://github.com/Aby-Sebastian/celery-logging.git
```

2.  **Make sure you are in *celery-logging* folder**

   1. Install all dependencies

      ```sh
      pip install -r requirements.txt
      ```
   
3. **Run Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
```

4. **Create SuperUser**

```sh
python manage.py createsuperuser
```

5. **Run Server**

```sh
python manage.py runserver 
```

And you are good to go. 

