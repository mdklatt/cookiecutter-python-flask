""" Implementation of the WSGI interface.

"""
from flask import Flask

from ..core.config import config
from ..core.logger import logger
from ._rest import rest


app = Flask(__name__)
app.register_blueprint(rest, url_prefix="/{{ cookiecutter.app_url }}")


@app.before_first_request
def _setup():
    """ One-time application setup.

    """
    config.load(app.config.get("config_path", "etc/config.yml"))
    logger.start(config.wsgi.logging)
    logger.debug("application setup complete")
    return
