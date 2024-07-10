#!/usr/bin/python3
"""
A Fabric script that distributes an archive to web servers.
"""
from fabric.api import task, local, env, put, run
from datetime import datetime
import os


env.hosts = ['100.25.16.129', '52.91.136.56']


@task
def do_pack():
    """
    Packs the files from the web_static directory.
    """
    form_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(form_dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None

@task
def do_deploy(archive_path):
    """
    Deploys the packed web static file.
    """
    try:
        if not os.path.exists(archive_path):
            return False
        w_exit = os.path.basename(archive_path)
        no_exit = os.path.splitext(w_exit)
        dpath = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, no_exit))
        run("mkdir -p {}{}/".format(dpath, no_exit))
        run("tar -xzf /tmp/{} -C {}{}/".format(w_exit, dpath, no_exit))
        run("rm /tmp/{}".format(w_exit))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, no_exit))
        run("rm -rf {}{}/web_static".format(dpath, no_exit))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, no_exit))
        print("New version deployed!")
        return True
    except Exception:
        return False
