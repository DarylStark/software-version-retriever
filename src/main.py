import yaml
import logging
from rich.logging import RichHandler
from typing import Optional

from version_checker import RestAPIJSONVersionChecker


def retrieve_current_version(name: str, configuration: dict) -> Optional[str]:
    """ Method to retrieve a specific current version """
    logger = logging.getLogger(f'CurrentVersion_{name}')
    logger.info(f'Checking current software version for "{name}"')

    # Start the correct 'check type'
    if configuration['type'] == 'rest-api-json':
        logger.info('Handing check off to RestAPIJSON checker')
        cv = RestAPIJSONVersionChecker(**configuration['configuration'])
        return cv.retrieve_version()

    return


def process_application(name: str, configuration: dict) -> None:
    """ Method to process a application """

    # Logger for this process
    logger = logging.getLogger(f'Process_{name}')
    logger.info(f'Processing "{name}"')

    # Retrieve the current version
    current_version = retrieve_current_version(
        name,
        configuration['current_version'])
    print()


if __name__ == '__main__':
    # Basic logging configuration
    # TODO: Configurable logging-level
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s -> %(message)s',
        datefmt="[%X]",
        handlers=[RichHandler()]
    )

    # Logger for the main thread
    logger = logging.getLogger('Main')

    # Load the configuration file
    # TODO: Configurable location
    # TODO: Exception handling (invalid JSON, file not exists, etc.)
    logger.info('Loading configuration')
    with open('../testdata/checks.yml') as configuration_file:
        configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)
    logger.info('Configuration loaded')

    # Loop through the configured applications and handle them
    for name, config in configuration['checks'].items():
        process_application(name, config)
