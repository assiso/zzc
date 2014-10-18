"""
WSGI config for zzc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
#Calculate the path based on the location of the WSGI script.  
apache_configuration= os.path.dirname(__file__)  
project = os.path.dirname(apache_configuration)  
workspace = os.path.dirname(project)  
sys.path.append(workspace)

sys.path.append('C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\zzc\zzc\zzc')
sys.path.append('C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\zzc\zzc')
sys.path.append('C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs')
sys.path.append('C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\zzc')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zzc.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# import django.core.handlers.wsgi

# application = django.core.handlers.wsgi.WSGIHandler()
