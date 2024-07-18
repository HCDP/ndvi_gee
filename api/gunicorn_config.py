import os

certfile = os.environ.get('GUNICORN_CERTFILE', None)
keyfile = os.environ.get('GUNICORN_KEYFILE', None)
workers = int(os.environ.get('GUNICORN_PROCESSES', '2'))
threads = int(os.environ.get('GUNICORN_THREADS', '4'))
# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:443')

forwarded_allow_ips = '*'