"""
WSGI config for ezadmin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/opt/ezadmin')
sys.path.append('/opt/ezadmin/env/lib/python2.7/site-packages')
sys.path.append('/usr/lib64/python27.zip')
sys.path.append('/usr/lib64/python2.7')
sys.path.append('/usr/lib64/python2.7/plat-linux2')
sys.path.append('/usr/lib64/python2.7/lib-tk')
sys.path.append('/usr/lib64/python2.7/lib-old')
sys.path.append('/usr/lib64/python2.7/lib-dynload')
sys.path.append('/usr/lib64/python2.7/site-packages')
sys.path.append('/usr/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ezadmin.settings")

application = get_wsgi_application()
