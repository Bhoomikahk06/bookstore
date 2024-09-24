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

# Getting All the Book Details
@pytest.mark.run(order=1)
@pytest.mark.asyncio
async def test_get_allbooks(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"] = f"Bearer {login}"
        response = await client.get("/books/",headers=header)
        assert response.status_code == 200,logger.error("Failed to Get Book Details")
        logger.info("Fetched all the Book details Successfully!!")
        logger.info("Books Details are: %s",response.json())


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
            "book_summary": "The main focus of War and Peace is the invasion of Russia by Napoleon in 1812"
        }
        response =await client.post("/books/", json=data,headers=header)
        assert response.status_code == 200,logger.error("Failed to Create Book")
        logger.info("Created the Book Successfully!!")
        response_data=response.json()
        logger.info("Created Book details: %s", response_data)
        await test_get_allbooks(login)

# Getting the created book details
@pytest.mark.run(order=3)
@pytest.mark.asyncio
async def test_get_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"] = f"Bearer {login}"
        response = await client.get("/books/1",headers=header)
        logger.info("Book %s:",response.json())
        assert response.status_code == 200,logger.error("Failed to Get Book Details")
        logger.info("Fetched  the Book detail Successfully!!")
        response_data=response.json()
        logger.info("Book Details: %s",response_data)
        assert response_data["id"]==1

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
            "book_summary": "The main focus of War and Peace is the invasion of Russia by Napoleon in 1812"
        }
        response =await client.put("/books/1", json=data,headers=header)
        assert response.status_code == 200,logger.error("Failed to Update the Book ")
        response_data=response.json()
        assert response_data["published_year"]==1888
        logger.info("Updated the Book Successfully!!")
        logger.info("Updated Book Details: %s", response_data)
        assert response_data["published_year"] == 1888

# Deleting the Book
@pytest.mark.run(order=5)
@pytest.mark.asyncio
async def test_delete_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"] = f"Bearer {login}"
        response_data = await client.delete("/books/1",headers=header)
        logger.info("Book %s:",response.json())
        assert response.status_code == 200,logger.error("Failed to Delete Book Details")
        response_data=response.json()
        assert response_data["message"]=="Book deleted successfully"
        logger.info("Deleted the Book Successfully!!")
        logger.info("Deleted Book info: %s", response_data)
        await test_get_allbooks(login)


#Negative Testing

# Getting Book details that doesn't exist
@pytest.mark.run(order=6)
@pytest.mark.asyncio
async def test_get_nonexist_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"] = f"Bearer {login}"
        response = await client.get("/books/10",headers=header)
        response_data=response.json()
        assert response.status_code == 404,logger.error("Failed to get the expected error condition")
        assert response_data["detail"]=="Book not found"
        logger.info("Failed to Fetched the Book detail Since book doesn't exist")
        logger.info("Info after Fetching the Book detail which doesn't exist: %s",response_data)

# Updating the Book which doesn't exist
@pytest.mark.run(order=7)
@pytest.mark.asyncio
async def test_update_nonexist_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"]=f"Bearer {login}"
        data={"id": 10,
            "name": "Treasure Island ",
            "author": "Leo Tolstoy",
            "published_year": 1888,
            "book_summary": "The main focus of War and Peace is the invasion of Russia by Napoleon in 1812"
        }
        response =await client.put("/books/10", json=data,headers=header)
        response_data = response.json()
        assert response.status_code == 404,logger.error("Failed to get the expected error condition")
        assert response_data["detail"] == "Book not found"
        logger.info("Failed to Update the Book detail Since book doesn't exist")
        logger.info("Info after trying to update the Book detail which doesn't exist: %s",response_data)

# Deleting the Book which doesn't exist
@pytest.mark.run(order=8)
@pytest.mark.asyncio
async def test_delete_nonexist_book(login):
    async with httpx.AsyncClient(base_url=url) as client:
        header["Authorization"] = f"Bearer {login}"
        response = await client.delete("/books/10",headers=header)
        response_data = response.json()
        logger.info("Book %s:", response_data)
        assert response.status_code == 404,logger.error("Failed to get the expected error condition")
        assert response_data["detail"] == "Book not found"
        logger.info("Failed to Delete the Book detail Since book doesn't exist")
        logger.info("Info after trying to Delete the Book detail which doesn't exist: %s",response_data)

# Failed to Login the Due to  invalid Email Id
@pytest.mark.run(order=9)
@pytest.mark.asyncio
async def test_invalid_login_emailid():
    # async with httpx.AsyncClient(base_url=url) as client:
        data = {"email": "testusr@example.com", "password": "password123"}
        # response = await client.post("/login/", json=data)
        response = requests.post(url=f"{url}/login/", json=data)
        response_data = response.json()
        assert response.status_code == 400,logger.error("Failed to get the expected error condition")
        assert response_data["detail"] == "Incorrect email or password"
        logger.info("Failed to Login the Due to  invalid Email Id")

# Failed to Login the Due to  invalid Password Id
@pytest.mark.run(order=10)
@pytest.mark.asyncio
async def test_invalid_login_password():
        data = {"email": "testuser@example.com", "password": "password1123"}
        # response = await client.post("/login/", json=data)
        response = requests.post(url=f"{url}/login/", json=data)
        response_data = response.json()
        assert response.status_code == 400,logger.error("Failed to get the expected error condition")
        assert response_data["detail"] == "Incorrect email or password"
        logger.info("Failed to Login the Due to invalid Password")
