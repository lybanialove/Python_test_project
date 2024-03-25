import pytest

from conftest import client

def test_register():
    response = client.post("/user/register", json={
        "email": "string123111",
        "password": "string",
        "name": "sadas"
    })

    print(response.text)

def test_select():
    response = client.get("/user/select", params={
        "email": "string123111",
    })

    print(response.text)

def test_auth():
    response = client.get("/user/auth", params={
        "email": "string123111",
        "password": "string",
    })

    print(response.text)

def test_con():
    response = client.post("/user/connectevent", params={
        "uniq_code": "sadas",
        "user_id": "1",
    })

    print(response.text)