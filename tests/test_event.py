import pytest

from datetime import datetime

from conftest import client



def test_register():
    response = client.post("/event/addevent", json={
        "name": "string123111",
        "description": "string",
        "uniq_code": "sadas",
        "start_at" : "2024-03-23T09:53:21.150"
    })

    print(response.text)

def test_datetime():
    response = client.post("/event/datetime", params={
        "uniq_code": "sadas",
        "date_time" : "2024-05-22T15:25:40.018541"
    })

    print(response.text)

def test_optimal_datetime():
    response = client.get("/event/optimaldatetime", params={
        "id_event": "1"
    })

    print(response.text)
