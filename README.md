in the cmd line use command -> pipenv shell to create a virtual environment
alternatively you can also you venv -> follow below commands
    mkdir env
    virtualenv env/django_task
    source env/django_task/bin/activate

NOTE: for this project purposes I will be using pipenv 

once you are in virtual env install the required files

install Django -> pipenv install Django
You can find all the required dependencies in requirements.txt file

Database -> I have used default django sqlite database for this app. Instead of using AWS database or heroku database