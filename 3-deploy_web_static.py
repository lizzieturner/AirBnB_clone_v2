#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""
from fabric.api import *
import os.path
from fabric.operations import run, put, sudo
do_pack = __import__('1-pack_web_static')
do_deploy = __import__('2-do_deploy_web_static')
env.hosts = ['35.196.149.169', '35.185.80.112']


def deploy():
    """ return value of do_deploy """
    path = do_pack.do_pack()
    try:
        return do_deploy(path)
    except:
        return False
