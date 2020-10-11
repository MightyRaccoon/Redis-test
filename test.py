import logging

import redis

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')

def main():
    client = redis.Redis(host='localhost', port=6379)

    logger.info('Add value to redis')
    client.set('Hello', 'World')

    logger.info('Get value')
    logger.info('Value: %s', client.get('Hello'))

    logger.info('Delete value')
    client.delete('Hello')

    logger.warning('Get deleted value')
    try:
        value = client.get('Hello')
        logger.info('Deleted value: %s', value)
    except Exception as e:
        logger.info(str(e))


if __name__ == '__main__':
    main()