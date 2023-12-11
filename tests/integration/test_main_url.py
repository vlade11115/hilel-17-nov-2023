import os

import requests

HEROKU_PR_NUMBER = os.getenv("HEROKU_PR_NUMBER")


def get_main():
    r = requests.get(f"https://hilel-review-pr-{HEROKU_PR_NUMBER}.herokuapp.com")
    assert r.ok
