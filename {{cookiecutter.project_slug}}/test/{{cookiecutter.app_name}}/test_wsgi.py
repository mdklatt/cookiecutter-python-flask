""" Test suite for the wsgi module.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the module is actually
being tested. If the library is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""
from yaml import dump

import pytest
from {{ cookiecutter.app_name }}.wsgi import app


@pytest.fixture
def config(tmp_path):
    """ Create a config file for testing.

    """
    path = tmp_path / "config.yml"
    path.write_text(dump({"wsgi": {"logging": "WARN"}}))
    return path


@pytest.fixture
def client(config):
    """ Return a Flask test client.

    """
    app.config["config_path"] = str(config)
    return app.test_client()


def test_hello(client):
    """ Test the hello/ end point.

    """
    response = client.get("{{ cookiecutter.app_url }}/hello/foo").get_json()
    assert response == {"message": "Hello, foo!"}
    return


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
