#!/usr/bin/python3
''' generates a .tgz archive from contents of web_static folder '''
from fabric.api import local
from datetime import datetime


def do_pack():
    ''' generates .tgz archive '''
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("sudo mkdir -p versions")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("sudo tar -cvzf {} web_static".format(file_name))
    return file_name
