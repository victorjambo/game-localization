"""Flask entry point"""

from os import getenv

from flask import jsonify

from main import create_app
from config import config


config_name = getenv('FLASK_ENV', default='production')

# create application from config
app = create_app(config[config_name])


@app.route('/healthcheck')
def healthcheck():
    """Used to check health status of the app"""
    return jsonify(dict(status='OK'))


if __name__ == '__main__':
    app.run()
