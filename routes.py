from logging import getLogger

from flask import Blueprint
from flask import current_app

logger = getLogger(__name__)

bp = Blueprint(
    'api',
    __name__,
    url_prefix='/',
)


@bp.route('/', methods=['POST', 'GET'])
def index():
    app = current_app._get_current_object()
    resp = app.extensions['my_in_client'].get_status()
    headers = dict(resp.raw.headers)
    out = resp.content
    return out


@bp.route('/about')
def hello_world():
    return 'Hello World!'
