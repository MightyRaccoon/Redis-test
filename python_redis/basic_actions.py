import logging

import redis
import click

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level='INFO'
)


@click.command()
@click.option('--numbers-count', default=0)
def main(numbers_count):
    logger.info('Connect to Redis')
    client = redis.Redis(host='redis', port=6379)

    logger.info('Is Redis available: %s', client.ping())

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

    logger.info('Put numbers to Redis')
    for number in range(numbers_count):
        logger.info('Set to key %i value %i', number, number)
        client.set(number, number)


if __name__ == '__main__':
    main()
