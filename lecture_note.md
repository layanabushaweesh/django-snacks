## to build django project
1. poetry init -n
2. poetry add django
3. poetry add --dev black # this as eslint for syntax error
4. poetry shell
5. django -admin startproject snacks_project . #ls we have manage.py
6. python manage.py runserver # we will have error
7. python manage.py migrate # to solve error
8. python manage.py startapp snacks

## inside the profiles
1. in setting the brain of project we add in insialled app our app
2. add path in url in project
3. create urls.py in app
4. connect app url to project url
5. in veiws we create class that we use
6. in setting import os .. for tamplets
7. creat tamplets directory
