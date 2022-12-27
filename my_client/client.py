from logging import getLogger

import requests
from requests import Response

logger = getLogger(__name__)


class MyClient(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.state = self.init_app(app)

    def get_status(self) -> Response:
        path = "https://yandex.ru/search/?text=waitress+ini&lr=10262&search_source=yaru_desktop_common&src=suggest_Pers"
        logger.info("Loading image for path %s", path)
        resp = self.connection.get(path)
        return resp

    def init_app(self, app):
        """Initializes your mail settings from the application settings.
        You can use this if you want to set up your Mail instance
        at configuration time.
        :param app: Flask application instance
        """
        state = self.init_client()

        # register extension with app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['my_in_client'] = state
        return state

    def init_client(self):
        self.url = "https://ya.ru"
        session = requests.session()

        r = session.get(self.url, verify=False)

        try:
            if r.status_code != 200:
                msg = 'Login failed. Please verify credentials!'
                logger.warning(msg)
                raise Exception(msg)

            self.connection = session
        except Exception as e:  # pylint:disable=broad-except
            logger.exception('Error during session creation: %s', e)
        return self
