import logging
import requests
import httpx
import pytest

logger = logging.getLogger(__name__)
url="http://127.0.0.1:8000"
header = {
    "Authorization":"",
    'Content-Type': 'application/json'
}


# Test Login the with Created user
@pytest.mark.run(order=9)
@pytest.mark.asyncio
async def test_valid_login(signup):
        data = {"email": signup, "password": "password123"}
        response = requests.post(url=f"{url}/login/", json=data)
        assert response.status_code == 200

# Getting All the Book Details
@pytest.mark.run(order=1)
@pytest.mark.asyncio
async def test_get_allbooks(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"] = f"Bearer {login}"
        response = await client.get("/books/",headers=header)
        assert response.status_code == 200

# Creating the book
@pytest.mark.run(order=2)
@pytest.mark.asyncio
async def test_create_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"]=f"Bearer {login}"
        data={"id": 1,
            "name": "Treasure Island ",
            "author": "Leo Tolstoy",
            "published_year": 1869,
            "book_summary": "The main focus of War and Peace is the invasion of Russia by Napoleon in 1812" }
        response =await client.post("/books/", json=data,headers=header)
        assert response.status_code == 200


# Getting the created book details
@pytest.mark.run(order=3)
@pytest.mark.asyncio
async def test_get_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"] = f"Bearer {login}"
        response = await client.get("/books/1",headers=header)
        assert response.status_code == 200


# Updating the Book
@pytest.mark.run(order=4)
@pytest.mark.asyncio
async def test_update_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"]=f"Bearer {login}"
        data={"id": 1,
            "name": "Treasure Island ",
            "author": "Leo Tolstoy",
            "published_year": 1888,
            "book_summary": "The main focus of War and Peace is the invasion of Russia by Napoleon in 1812"}
        response =await client.put("/books/1", json=data,headers=header)
        assert response.status_code == 200


# Deleting the Book
@pytest.mark.run(order=5)
@pytest.mark.asyncio
async def test_delete_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"] = f"Bearer {login}"
        response = await client.delete("/books/1",headers=header)
        assert response.status_code == 200





