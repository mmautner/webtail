webtail
=======

tail your logs from your web browser

install requirements:

    # platform-dependent redis, nginx server installationb
    pip install -r requirements.txt

Run the server:

    python server.py

Run redis:

    redis-server

Run celery:

    celery -A 'app.celery' worker

