#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the content of web_static.
"""
from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """
    Packs the content of the web_static directory.
    """
    form_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(form_dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None
