in the cmd line use command -> pipenv shell to create a virtual environment
alternatively you can also you venv -> follow below commands
    mkdir env
    virtualenv env/django_task
    source env/django_task/bin/activate

NOTE: for this project purposes I will be using pipenv

once you are in virtual env install the required files
Use the requirements.txt file to install all the necessary files. run command -> pipenv install -r requirements.txt 

Database -> I have used default django sqlite database for this app. Instead of using AWS database or heroku database

The default user model has been changed to add email & address field by overrding AbstractBaseUser, PermissionsMixin, BaseUserManager

In order to access the delete and edit functionality you need to login via an admin account.

You can use the edit form to make changes to the form. If you don't want to change your password just type your old password.
