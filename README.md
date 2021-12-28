# Based on Requirements

user can register using api
user can login using api

----------------

author can create new post, delete post, update post using api
author authorized to delete/create/modify using api
author can commment using api

user can read or search other posts using api, but can't modify
user can comment using api
user can like using api

filter posts using api
search posts using api

-----------------





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

#### Models

First model: blogpost -> BlogPost

- title
- content
- last_update

bloguser -> BlogUser  


-------------------

Deleted -> likedapp, commentapp
Created -> useractivity


--------------

- A customer can comment many times, on same post, if customer or post gets deleted, comment also get deleted
- A customer can like a post one time, if customer or post get deleted the like disappears
