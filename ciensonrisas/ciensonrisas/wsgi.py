"""
WSGI config for ciensonrisas project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

import site
envpath = '/home/humitos/.virtualenvs/ciensonrisas.com.ar/lib/python2.6/site-packages'
site.addsitedir(envpath)

# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
import os
os.environ['PYTHON_EGG_CACHE'] = '/home/humitos/apps/ciensonrisas.com.ar/mod_wsgi/egg-cache'

#If your project is not on your PYTHONPATH by default you can add the following
sys.path.append('/home/humitos/apps/ciensonrisas.com.ar/ciensonrisas/ciensonrisas')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ciensonrisas.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
