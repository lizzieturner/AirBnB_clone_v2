#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""
from fabric.api import *
import os.path
from fabric.operations import run, put, sudo
env.hosts = ['35.196.149.169', '35.185.80.112']


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    tmp_path = "/tmp/" + file_name
    dest = "/data/web_static/releases/" + "os.path.splitext(file_name)"
    curr = "/data/web_static/current"
    try:
        put(archive_path, tmp_path)
        run ("sudo mkdir -p {}".format(dest))
        run("sudo tar -xzf {} -C {}".format(tmp_path, dest))
        run("sudo rm {}".format(tmp_path))
        run("sudo mv {}/web_static/* {}/".format(dest, dest))
        run("sudo rm -rf {}/web_static".format(dest))
        run("sudo rm -rf {}".format(curr))
        run("sudo ln -s {} {}".format(dest, curr))
        return True
    except:
        return False
