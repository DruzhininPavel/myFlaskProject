from flask import Flask
from flask_bootstrap import Bootstrap

from my_client import client
import routes


def register_routes(app: Flask):
    Bootstrap(app)
    app.register_blueprint(routes.bp)


def initialize_extensions(app):
    client.MyClient(app)


def create_app():
    app = Flask(__name__,
                template_folder=str('templates'),
                static_folder=str('static'),
                )
    register_routes(app)
    initialize_extensions(app)
    return app


def main():
    return create_app()


if __name__ == '__main__':
    main_app = main()
    main_app.run()
