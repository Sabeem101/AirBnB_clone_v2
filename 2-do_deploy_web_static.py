#!/usr/bin/python3
"""
A Fabric script that distributes an archive to web servers.
"""
from fabric.api import env, put, run
from os.path import exists


env.hosts = ['100.25.16.129', '52.91.136.56']


def do_deploy(archive_path):
    """
    Deploys the packed web static file.
    """
    if not exists(archibe_path):
        return False
    try:
        fname = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}"
            .format(fname))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(fname, fname))
        run('rm -rf /tmp/{}.tgz'.format(fname))
        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(fname, fname))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(fname))
        run('rm -rf /data/web_static/current')
        run(('ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(fname))
        return True
    except Exception:
        return False
