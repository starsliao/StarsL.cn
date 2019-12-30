workers = 2
bind = 'unix:/etc/nginx/starsl.sock'
daemon = True
worker_class = 'gevent'
chdir = '/data/venv/StarsL.cn'
pidfile = '/var/run/gunicorn.pid'

errorlog = '/var/log/gunicorn_error.log'
loglevel = 'info'
accesslog = '/var/log/gunicorn_access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
