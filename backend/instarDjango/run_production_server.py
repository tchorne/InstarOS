from gevent import monkey; monkey.patch_all()
from gevent.pywsgi import WSGIServer
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instarDjango.settings")
django.setup()

PORT = os.environ['PORT']

from django.core.handlers.wsgi import WSGIHandler as DjangoWSGIApp
application = DjangoWSGIApp()
server = WSGIServer(("0.0.0.0", int(PORT)), application)

print("Starting server on http://0.0.0.0:" + PORT)
server.serve_forever()