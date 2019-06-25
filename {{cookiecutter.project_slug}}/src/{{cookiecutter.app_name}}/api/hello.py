""" Implement the hello command.

"""
from ..core.logger import logger


def main(name="World") -> str:
    """ Generate a greeting.
    
    :param name: name to use in greeting
    """
    logger.debug("executing hello command")
    return "Hello, {:s}!".format(name)   # TODO: f-string with Python 3.6+
