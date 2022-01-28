"""
Bot
"""
import requests
from PIL import Image


class Bot:
    """
    Class represents telegram bot
    """
    def __init__(self, token, server_url):
        """
        Initilization of bot
        :param token: bot'token from @BotFather
        :param server_url: utl to set webhook
        """
        self.token = token
        self.server_url = server_url
        self.set_webhook()

    def make_api_url(self, method):
        """
        Method to create API url to telegram
        :param method: bot's method
        :return: string url
        """
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def set_webhook(self):
        """
        Method to set webhook
        :return: response in JSON
        """
        method = "setWebhook"
        api_url = self.make_api_url(method)
        post_data = {
            "url": self.server_url,
        }
        req = requests.post(api_url, data=post_data, headers={'header': 'Content-Type: application/json'})
        return req.json()

    def send_message(self, chat_id, text):
        """
        Send message to tg user with text
        :param chat_id: user/group to send message
        :param text:  to send
        """
        method = "sendMessage"
        url = self.make_api_url(method)
        data = {"chat_id": chat_id, "text": text}
        requests.post(url, data=data)

    def get_photo_path(self, photo_id):
        """
        Method to get photo path by photo id
        :param photo_id: of user's photo
        :return: photo_path
        """
        method = "getFile"
        api_url = self.make_api_url(method)
        post_data = {
            'file_id': photo_id,
            "url": self.server_url
        }
        req = requests.post(api_url, data=post_data, headers={'header': 'Content-Type: application/json'})
        return req.json()['result']['file_path']

    def get_photo(self, photo_id):
        """
        Method to  get photo with telegram api
        :param photo_id:  of user's photo
        :return: opens requested image
        """
        photo_path = self.get_photo_path(photo_id)
        photo_url = self.make_api_url(photo_path)
        return Image.open(requests.get(photo_url, stream=True).raw)
