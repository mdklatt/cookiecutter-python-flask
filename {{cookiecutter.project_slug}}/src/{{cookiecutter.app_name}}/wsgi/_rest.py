""" Implementation of the REST API.

"""
from flask import Blueprint
from flask import jsonify

from .. import api


rest = Blueprint("rest", __name__)


@rest.route("hello")
@rest.route("hello/<name>")
def hello(name="World"):
    """ Return a greeting.

    """
    return jsonify({"message": api.hello(name)})
