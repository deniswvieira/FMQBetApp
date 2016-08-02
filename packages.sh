pip install virtualenv;
source bin/activate;
sudo apt-get install libmysqlclient-dev;
pip install mysql-python;
pip install django;
pip install uwsgi;
sudo apt-get install nginx;
sudo ln -s ./BetApp/FMQBetAppConf /etc/nginx/sites-enabled/
sudo service nginx restart