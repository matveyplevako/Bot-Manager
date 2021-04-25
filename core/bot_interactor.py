from Bot_manager.settings import TELEGRAM_BOT_SERVER_URL, WEBHOOK_URL
import requests
import json
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def process_update(update, bot_token):
    data = json.loads(update)
    message = data["message"]
    chat_data = message["chat"]
    try:
        text = message["text"]
    except Exception as e:
        logger.error(e)
        return

    send_message(text, chat_data["id"], bot_token)


def send_message(message, chat_id, token):
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(
        f"{TELEGRAM_BOT_SERVER_URL}bot{token}/sendMessage", data=params
    )


def set_webhook(token):
    params = {'url': f'{WEBHOOK_URL}{token}'}
    url = f"{TELEGRAM_BOT_SERVER_URL}bot{token}/setWebhook"
    return json.loads(requests.get(url, params=params).content)


def remove_webhook(token):
    url = f"{TELEGRAM_BOT_SERVER_URL}bot{token}/deleteWebhook"
    return requests.get(url).content
