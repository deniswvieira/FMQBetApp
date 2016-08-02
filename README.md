############################
 BET APP - CREATED BY DENIS VIEIRA
############################

- System Ubuntu 16.04 LTS
- Python Version 2.7
- Django Version 1.9.8
- uWSGI Version 2.0.13.1
- With the FMQBetAppConf nginx configuration, app address is: 127.0.0.1:8000

#Pre requesites
- Git
	- $ sudo apt-get install git

- MySQL
	- $ sudo apt-get install mysql-server

- Virtual Environment
	- $ sudo apt-get install virtualenv

- Nginx
	- $ sudo apt-get install nginx

#Instalation
- Set up Project and Virtual Environment
	- Create the virtual environment (project folder):
		- `$ virtualenv BetAppEnv`
		- `$ cd BetAppEnv`
		- `$ source bin/activate`
	- Install Django 1.9.8:
		- `$ pip install -I django==1.9.8`
	- Clone App into the project folder:
		- $ `git clone https://github.com/deniswvieira/FMQBetApp.git`

- Set up Server with Nginx and uWSGI
	- install uWSGI:
		- $ pip install uwsgi
	- Edit uwsgi configuration file (BetApp_uwsgi.ini) in order to path's match with your directories
	- Create nginx configuration file:
		- $ sudo nano /etc/nginx/sites-available/BetAppConf
		- Copy and paste the code on FMQBetAppConfig file and edit in order to path's match with your directories
		- press Ctrl + X, y, and enter to exit when the file is ready
		- $ sudo ln -s /etc/nginx/sites-available/BetAppConf /etc/nginx/sites-enabled
		- It will give error if you have an other file on sites-enabled folder with the same listen, use $ sudo rm /etc/nginx/sites-enabled/filename to remove it
	- Load configuration:
		- $ sudo service nginx reload
		- $ sudo service nginx restart

- Set up Database
	- Create Database
		- $ mysql -u root -p
		- insert root password
		- $ CREATE DATABASE BetAppDB
	- Edit DATABASE parameters on ./BetApp/settings.py file
	- Install components:
		- $ pip install mysql-python
		- $ sudo apt-get install libmysqlclient-dev
	- Do migations:
		- $ ./manage.py makemigrations BetApp
		- $ ./manage.py makemigrations cauth
		- $ ./manage.py migrate

- Run application
	- $ uwsgi --ini BetApp_uwsgi.ini
	- Visit the application on 127.0.0.1:8000
	

