#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """  return the archive path if the archive has been correctly generated """
    try:
        archive = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir versions")
        val = local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(archive))
        res = "versions/web_static_{:s}.tgz".format(archive)
        return res
    except:
        return None
