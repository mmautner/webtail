
DEBUG = True
SECRET_KEY = 'something secret'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

BROKER_URL = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)

SOCKETIO_CHANNEL = 'tail-message'
MESSAGES_KEY = 'tail'
CHANNEL_NAME = 'tail-channel'
