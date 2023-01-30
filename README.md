# Shortly

A File Generation application built with `python` `django` `Celery` `Redis`. 

A simple, reponsive  website. Built with:

- Python 🐍
- Django 🎸
- Bootstrap 4 🌈
- Sqlite3
- Celery
- Redis
- HTML
- CSS

## Features

- Generates csv files according to user input filename and no of rows
- Inserts status of Celery Task to Database
- sends email when new user registers to the application


## How to run this project (Ubuntu 18.04)

1. **Clone the project**

```sh
git clone https://github.com/Aby-Sebastian/Shortly.git
```

2.  **Make sure you are in *Shortly* folder**

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



**Backend**


Note: Please change those gmail credentials from real_estate folder you will get settings.py inside that file you will see username and password mentioned as place your Username and Password. Also do that same thing from Contacts folder views.py you will see YourEmail mentioned on line number 33.
