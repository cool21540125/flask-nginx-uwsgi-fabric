import os
from fabric.api import *
from fabric.contrib.files import exists


env.user = 'ubuntu'
env.hosts = ['ubuntu@<ip or dns>']
REMOTE_DIR = '/home/ubuntu/data/app'

def prepare():
    sudo('apt-get -y update && apt-get -y upgrade')

    # python dev
    sudo('apt-get install python-pip python-dev build-essential python-virtualenv -y')
    sudo('pip install --upgrade pip')

    # nginx
    sudo('apt-get install nginx -y')

    # uwsgi
    sudo('apt-get install uwsgi -y')
    sudo('apt-get install python3-dev -y')
    sudo('apt-get install uwsgi-plugin-python3 -y')

def deploy():
    run('whoami')

    local('source venv/bin/activate && pip freeze > requirements.txt')

    for host in env.hosts:
        if not exists(REMOTE_DIR):
            run('mkdir /home/ubuntu/data /home/ubuntu/data/app')

        local('rsync -avz . {}:{} --delete --exclude-from \'rsync_exclude.txt\''.format(host, REMOTE_DIR))

    with cd(REMOTE_DIR):
        if not exists('venv'):
            run('virtualenv -p python3 venv')
        run('source venv/bin/activate && pip install -r requirements.txt')

        sudo('cp config/nginx/default /etc/nginx/sites-available/')
        sudo('cp config/uwsgi/uwsgi.ini /etc/uwsgi/apps-available/')
        if not exists('/etc/uwsgi/apps-enabled/uwsgi.ini'):
            sudo('ln -s /etc/uwsgi/apps-available/uwsgi.ini /etc/uwsgi/apps-enabled/uwsgi.ini')

    restart()

def restart():
    sudo('service nginx restart')
    sudo('service uwsgi restart')

def go():
    prepare()
    deploy()
