# DailyBlog

created github repo with readme
cloned repo
pipenv install django
pipenv shell
django-admin startproject dailyblog .
-> python interpreter for dailyblog
pip install djangorestframework
pip install markdown
pip install django-filter

pipenv install mysqlclient
database created in mysql
-> database in settings updated
python manage.py migrate

django-admin startapp bloguser
-> add to installed apps
-> class User(AbstractUser)

django-admin startapp blogpost
-> add to installed apps

django-admin startapp commentapp
-> add to installed apps

django-admin startapp likeapp
-> add to installed apps

-> Deleted database to recreate (bcoz of abstractuser)
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
-> admin
-> mhnpta@gmail.com
-> dribblecode

Extended UserAdmin class

create new user
-> rahul
-> wordp88@gmail.com
-> newyear2022

Will Edit It later

---------------------

First Commit

----------------------