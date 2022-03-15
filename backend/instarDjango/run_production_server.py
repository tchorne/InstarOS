from gevent import monkey; monkey.patch_all()
from gevent.pywsgi import WSGIServer
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instarDjango.settings")
django.setup()


from django.core.handlers.wsgi import WSGIHandler as DjangoWSGIApp
application = DjangoWSGIApp()
server = WSGIServer(("127.0.0.1", 1234), application)
print("Starting server on http://127.0.0.1:1234")
server.serve_forever()