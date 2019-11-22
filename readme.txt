Read Me
--------

Python Django Dev to Deployment
Brad Traversy
Udemy

Created:	18 oct 2019
Last:		21 nov 2019



django-admin startproject btre . 

Creates the the project and manage.py

python manage.py help

python manage.py runserver 

python manage.py collectstatic 

python manage.py startapp listings 

python manage.py startapp realtors 

python manage.py migrate


Pip
----
pip freeze
pip install psycopg2
pip install psycopg2-binary



Postgres
---------
Launch Postgres
pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start 

Connect
psql -p5432 -d "postgres"


Create
CREATE DATABASE btredb OWNER postgres;

\l
\q



