import os
import logging

import yaml
from dotenv import load_dotenv
from glom import assign

load_dotenv()

# Set Logger
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=logging.getLevelName(LOG_LEVEL), format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Set Arguments
GITHUB_URL = os.getenv('GITHUB_URL')
GITHUB_REPO = GITHUB_URL.split('/')[-1].split('.')[0]
GITHUB_BRANCH = os.getenv('GITHUB_BRANCH')
YAML_PATH = os.getenv('YAML_PATH')
TARGET_KEY = os.getenv('TARGET_KEY')
NEW_VALUE = os.getenv('NEW_VALUE')
COMMIT_MESSAGE = os.getenv('COMMIT_MESSAGE')
COMMIT_AUTHOR = os.getenv('COMMIT_AUTHOR')


def print_env():
    logger.debug("ENVIRONMENT VARIABLES")
    logger.info(f"LOG_LEVEL: {LOG_LEVEL}")
    logger.debug(f"GITHUB_URL: {GITHUB_URL}")
    logger.debug(f"GITHUB_BRANCH: {GITHUB_BRANCH}")
    logger.debug(f"YAML_PATH: {YAML_PATH}")
    logger.debug(f"TARGET_KEY: {TARGET_KEY}")
    logger.debug(f"NEW_VALUE: {NEW_VALUE}")
    logger.debug(f"COMMIT_MESSAGE: {COMMIT_MESSAGE}")
    logger.debug(f"COMMIT_AUTHOR: {COMMIT_AUTHOR}")


def clone_repo() -> None:
    logger.info("clone repo ...")
    command = f"git clone -b {GITHUB_BRANCH} {GITHUB_URL}"
    logger.debug(command)
    os.system(command)

    command = f"git config --global user.name '{COMMIT_AUTHOR.split('<')[0][:-1]}'"
    logger.debug(command)
    os.system(command)

    command = f"git config --global user.email '{COMMIT_AUTHOR}'"
    logger.debug(command)
    os.system(command)


def load_yaml() -> dict:
    logger.info("load yaml ...")
    with open(f"{GITHUB_REPO}/{YAML_PATH}") as f:
        loaded_yaml = yaml.safe_load(f)
        logger.debug(loaded_yaml)
        return loaded_yaml


def modify_yaml(loaded_yaml: dict) -> dict:
    logger.info("modify yaml ...")
    modified_yaml = assign(loaded_yaml, TARGET_KEY, NEW_VALUE)
    logger.debug(modified_yaml)
    return modified_yaml


def write_yaml(updated_yaml: dict) -> None:
    logger.info("write yaml ...")
    with open(f"{GITHUB_REPO}/{YAML_PATH}", 'w') as f:
        yaml.dump(updated_yaml, f, sort_keys=False)


def add_commit_push() -> None:
    logger.info("add, commit and push ...")

    command = f"cd {GITHUB_REPO} && git add '{YAML_PATH}'"
    logger.debug(command)
    os.system(command)

    command = f"cd {GITHUB_REPO} && git commit -m '{COMMIT_MESSAGE}'"
    logger.debug(command)
    os.system(command)

    command = f"cd {GITHUB_REPO} && git push origin {GITHUB_BRANCH}"
    logger.debug(command)
    os.system(command)


if __name__ == "__main__":
    print_env()  # only in 'DEBUG' logging level
    clone_repo()
    loaded_yaml = load_yaml()
    updated_yaml = modify_yaml(loaded_yaml)
    write_yaml(updated_yaml)
    add_commit_push()
    logger.info("finished.")
