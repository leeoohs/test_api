import pytest


@pytest.fixture()
def context():
    return  {
        "host": "117.72.115.136",
        "port": "8003"
    }