from logging import getLogger

from flask import Blueprint, render_template
from flask import current_app
# from app import my_in_client

logger = getLogger(__name__)

bp = Blueprint(
    'api',
    __name__,
    url_prefix='/',
)


@bp.route('/', methods=['POST', 'GET'])
def index():
    app = current_app._get_current_object()

    # client = my_client.client.MyClient()

    resp = app.extensions['my_in_client'].get_status()
    headers = dict(resp.raw.headers)
    out = resp.content
    return out


@bp.route('/about')
def hello_world():  # put application's code here
    return 'Hello World!'
