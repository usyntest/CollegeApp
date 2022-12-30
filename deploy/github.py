import os
import pickle
from pathlib import Path

from .api import GithubApp
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
load_dotenv(PROJECT_ROOT / ".env")

OWNER = os.environ.get("OWNER")
REPOSITORY = os.environ.get("REPOSITORY")


def save_api_cache():
    with open(API_CACHE_PATH, "wb") as cache_file:
        pickle.dump(api, cache_file)


API_CACHE_PATH = PROJECT_ROOT / "deploy/api.pickle"
if os.path.exists(API_CACHE_PATH):
    with open(API_CACHE_PATH, "rb") as file:
        api = pickle.load(file)
else:
    api = GithubApp(
        os.path.expanduser(os.environ.get("KEY_FILE_PATH")),
        os.environ.get("APP_ID")
    )
    save_api_cache()


def create_deployment():
    # printing it so that bash script can store the output
    print(api.create_deployment(OWNER, REPOSITORY, branch="master")["id"])
    save_api_cache()


def update_status(deployment_id, state):
    api.update_deployment_status(OWNER, REPOSITORY, deployment_id, state=state)
    save_api_cache()
