import random

import httpx
import pytest
import logging

import requests

logger = logging.getLogger(__name__)
url="http://127.0.0.1:8000"

#
# @pytest.fixture(scope="module")
# async def signup():
#     async with httpx.AsyncClient(base_url=url) as client:
#         number=random.randint(1, 999)
#         data = {"email": "testuser"+str(number)+"@example.com", "password": "password123"}
#         response = await client.post(url=f"{url}/signup/", json=data)
#         logger.info(response)
#         assert response.status_code == 200
#         data=data["email"]
#         return data
#
#
# @pytest.fixture(scope="module")
# async def login(signup):
#     async with httpx.AsyncClient(base_url=url) as client:
#         global token
#         data = {"email": signup,"password":"password123"}
#         response = await client.post(url=f"{url}/login/", json=data)
#         assert response.status_code == 200
#         response=response.json()
#         token=response["access_token"]
#         yield token


@pytest.fixture(scope="module")
def signup():
    # async with httpx.AsyncClient(base_url=url) as client:
        number=random.randint(1, 999)
        data = {"email": "testuser"+str(number)+"@example.com", "password": "password123"}
        response = requests.post(url=f"{url}/signup/", json=data)
        logger.info(response)
        assert response.status_code == 200
        data=data["email"]
        return data


@pytest.fixture(scope="module")
def login(signup):
    global token
    # async with httpx.AsyncClient(base_url=url) as client:
    data = {"email": signup,"password":"password123"}
    # response = await client.post("/login/", json=data)
    response = requests.post(url=f"{url}/login/", json=data)
    assert response.status_code == 200
    response=response.json()
    token=response["access_token"]
    yield token

