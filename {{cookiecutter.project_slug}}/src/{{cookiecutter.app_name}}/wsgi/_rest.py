""" Implementation of the REST API.

"""
from flask import Blueprint
from flask import jsonify
from flask import Response

from .. import api


__all__ = "rest",


rest = Blueprint("rest", __name__)


@rest.route("hello")
@rest.route("hello/<name>")
def hello(name="World") -> Response:
    """ Return a greeting.

    :param name: name to use for greeting
    :return: JSON content
    """
    return jsonify({"message": api.hello(name)})
