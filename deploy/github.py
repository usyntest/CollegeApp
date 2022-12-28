import os
from pathlib import Path

from .api import GithubApp
from dotenv import load_dotenv

load_dotenv((Path(__file__).parent.parent / ".env").resolve())
print((Path(__file__).parent.parent / ".env").resolve())

OWNER = os.environ.get("OWNER")
REPOSITORY = os.environ.get("REPOSITORY")

api = GithubApp(
    os.path.expanduser(os.environ.get("KEY_FILE_PATH")),
    os.environ.get("APP_ID")
)


def create_deployment():
    # printing it so that bash script can store the output
    print(api.create_deployment(OWNER, REPOSITORY, branch="master")["id"])


def update_status(deployment_id, state):
    api.update_deployment_status(OWNER, REPOSITORY, branch="master", deployment_id, state=state)
