systemctl start mysql

systemctl status mysql.service

systemctl stop mysql

env/bin/python3.8 api/manage.py makemigrations

env/bin/python3.8 api/manage.py migrate

python3 api/manage.py runserver

