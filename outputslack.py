import json

import requests # type: ignore


def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))
