import os

from fabric.api import env, run, local
from fabric.context_managers import cd
from fabric.operations import sudo, get

env.hosts = ['mkaufmann.com.ar']
# use "ssh-copy-id" command
# env.password = ''

REMOTE_CIENSONRISAS_SRC = '~/apps/ciensonrisas.com.ar/ciensonrisas'
REMOTE_CIENSONRISAS_APP = os.path.join(REMOTE_CIENSONRISAS_SRC,
                                    'ciensonrisas')


def remote_virtualenv(command):
    run('source ~/.virtualenvs/ciensonrisas.com.ar/bin/activate && %s' % command)


def local_virtualenv(command):
    local('source %s && %s' % ('~/.virtualenvs/ciensonrisas/bin/activate', command))


def deploy():
    with cd(REMOTE_CIENSONRISAS_SRC):
        run('git pull')
        remote_virtualenv('pip install -r requirements.txt')

    with cd(REMOTE_CIENSONRISAS_APP):
        remote_virtualenv('./manage.py collectstatic --noinput')
        remote_virtualenv('./manage.py migrate')

    restart_uwsgi()


def restart_uwsgi():
    sudo('/etc/init.d/uwsgi restart')


# def restart_webservers():
#     sudo('/etc/init.d/apache2 restart')
#     sudo('/etc/init.d/nginx restart')


# def pull_source():
#     with cd(REMOTE_CIENSONRISAS_SRC):
#         run('git pull')


# def sync_local_db():
#     with cd(REMOTE_CIENSONRISAS_APP):
#         remote_virtualenv('./manage.py dumpdata --indent=4 --format=json '
#                           '--exclude=contenttypes '
#                           '> dump.json')

#     with cd(LOCAL_CIENSONRISAS_APP):
#         local('rm -f profiles/fixtures/initial_data.json')
#         local('./manage.py reset_db --router=default --noinput')
#         local('./manage.py syncdb --noinput')
#         local('./manage.py migrate')
#         get('~/apps/lookremix/src/application/lookremix/dump.json', '/tmp')
#         local_virtualenv('./manage.py loaddata /tmp/dump.json')
#         local('rsync --compress --progress --verbose '
#               '--human-readable --recursive '
#               'stageuser@178.79.156.225:~/apps/lookremix/src/application/lookremix/user-media .')
#         local('git checkout -- profiles/fixtures/initial_data.json')

#         # FIXME: I don't know why the "load" command duplicates some
#         # User's profiles
#         local('./manage.py runjob delete_duplicated_profiles')


# def restart_memcached():
#     sudo('/etc/init.d/memcached restart')
