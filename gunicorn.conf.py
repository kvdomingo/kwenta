# config
wsgi_app = "kwenta.wsgi"

# logging
errorlog = "-"
accesslog = "-"
loglevel = "debug"
capture_output = True

# worker processes
worker_class = "gevent"
workers = 1
timeout = 30
graceful_timeout = 10
