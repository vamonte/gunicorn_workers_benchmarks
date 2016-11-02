bind = ':8000'
workers = 4
worker_class = 'gevent'

try:
    from gevent import monkey
    from psycogreen.gevent import patch_psycopg

    def do_post_fork(server, worker):
        monkey.patch_all()
        patch_psycopg()

    post_fork = do_post_fork
except ImportError:
    pass
