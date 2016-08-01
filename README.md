############################
 CREATED BY DENIS VIEIRA
############################

- Python Version 2.7
- uWSGI version 2.0.13.1
- With the FMQBetAppConf nginx configuration, app address is: 127.0.0.1:8000

#Important steps on setup:
- Database:
	- Change the ./BetApp/BetApp/settings.py file with the credentials of the server and the database;
	- Delete folders:
		- ./BetApp/BetApp/Migrations
		- ./BetApp/BetApp/Migrations
	- Make migrations for each app
		./BetApp/manage.py makemigrations <app_name>   [BetApp and cauth]
		./BetApp/manage.py migrate

- Server
	- Put the nginx config file running:
		- sudo ln -s ./BetApp/FMQBetAppConf /etc/nginx/sites-enabled/
		- sudo service nginx restart
	- Use the uwsgi .ini file to set up our server:
		- uwsgi --ini ./BetApp/BetApp_uwsgi.ini
