import yaml
import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.table import Table
from typing import Optional
from dataclasses import dataclass

from version_checker import VersionChecker, RestAPIJSONVersionChecker, GitHubReleaseVersionChecker


@dataclass
class SoftwareVersion:
    name: str
    running_version: str
    desired_version: str

    def is_up_to_date(self) -> bool:
        if self.running_version is None or self.desired_version is None:
            return False
        return self.running_version == self.desired_version


def retrieve_software_version(name: str, configuration: dict) -> Optional[str]:
    """ Method to retrieve a specific current version """
    logger = logging.getLogger(f'CurrentVersion_{name}')
    logger.info(f'Checking current software version for "{name}"')

    # Object for the checker
    cv: Optional[VersionChecker] = None

    # Define checkers
    checkers = {
        'rest-api-json': RestAPIJSONVersionChecker,
        'github-release': GitHubReleaseVersionChecker,
    }

    # Start the correct 'check type'
    if configuration['type'] in checkers.keys():
        cv = checkers[configuration['type']](**configuration['configuration'])

    if cv:
        return cv.retrieve_version()

    logger.warning(f'Checker "{configuration["type"]}" is not defined')
    return None


def process_application(name: str, configuration: dict) -> SoftwareVersion:
    """ Method to process a application """

    # Logger for this process
    logger = logging.getLogger(f'Process_{name}')
    logger.info(f'Processing "{name}"')

    # Retrieve the current version
    logger.info('Retrieving running software version')
    running_version = retrieve_software_version(
        name,
        configuration['current_version'])
    logger.info('Retrieving desired software version')
    latest_version = retrieve_software_version(
        name,
        configuration['desired_version'])

    # Create a SoftwareVersion object and return it
    return SoftwareVersion(
        name=name,
        running_version=running_version,
        desired_version=latest_version
    )


if __name__ == '__main__':
    # Basic logging configuration
    # TODO: Configurable logging-level
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s -> %(message)s',
        datefmt="[%X]",
        handlers=[RichHandler()]
    )

    # Create a Rich Console
    console = Console()

    # Logger for the main thread
    logger = logging.getLogger('Main')

    # Load the configuration file
    # TODO: Configurable location
    # TODO: Exception handling (invalid JSON, file not exists, etc.)
    logger.info('Loading configuration')
    with open('../testdata/checks.yml') as configuration_file:
        configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)
    logger.info('Configuration loaded')

    # Create a Rich Table
    table = Table()
    table.add_column('Name')
    table.add_column('Running version')
    table.add_column('Desired version')
    table.add_column('Status')

    # Loop through the configured applications and handle them
    for name, config in configuration['checks'].items():
        version = process_application(config['name'], config)
        table.add_row(
            version.name,
            version.running_version,
            version.desired_version,
            "[green]Up-to-date[/green]" if version.is_up_to_date(
            ) else "[yellow]Needs to be updated[/yellow]"
        )

    # Print the table
    console.print(table)
