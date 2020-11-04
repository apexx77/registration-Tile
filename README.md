# Registration-Tile 

* A simple registration application written in Django 3.0.7 that allows users to register their details for the website.

<p align="center">
  <img src="https://github.com/apexx77/Registration-Tile/blob/master/reg1.jpg" width="60%" title="Welcome User">
</p>

## Connecting to the database

* Start the server and connect it with the project through appropriate connector.
* Create a database with the desired name and the enter the name of the database name in this [file](https://github.com/apexx77/Registration-Tile/blob/master/django_project/settings.py) in 'DATABASES'.
* And then, enter the username `root`, host `localhost`, port `3306` and password. These are the default values when connected to MySQL database.

## Running the application

To run the application:
* Open the terminal and navigate to the project directory and make migrations by executing the command `python manage.py makemigrations`
* Then, execute `python manage.py migrate`
* Then run the server by executing `python manage.py runserver`

## Specifications

* When connected to a MySQL database and run, it saves the input data in it and the data can be accessed through SQL commands.
* If you want to connect with a database other than MySQL, go to this [file](https://github.com/apexx77/Registration-Tile/blob/master/django_project/settings.py) and make changes in Default Engine in 'DATABASES'.

 ## Check these before running the application
 
* [x] Server Connection
* [x] Database Connection
* [x] Migrations are made
 
<p align="center">&copy; <a href="https://github.com/apexx77">Asif Ahmad</a></p>

