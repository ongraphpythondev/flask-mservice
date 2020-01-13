from flaskr import app
# import pytest
import json

client = app.test_client()


def test_hello():
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_ctime():
    response = client.get('/ctime')
    assert response.status_code == 200
    assert b"The UTC time with format 'mm/dd/YYYY HH:MM:SS' is" in response.data


def test_invalid_zone():
    response = client.get('/ctime/some_invalid_tzone')
    assert response.status_code == 200
    assert b'Unknown time zone please provide valid timezone' in response.data
