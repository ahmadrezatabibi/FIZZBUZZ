
# Fizzbuzz API

## Overview

The Fizzbuzz API is a Django REST framework-based backend service that provides an API for managing Fizzbuzz items. This service allows clients to retrieve a list of Fizzbuzz items and create new ones.

## Features

- Retrieve a list of all Fizzbuzz items
- Retrieve detailed view of a Fizzbuzz item
- Create new Fizzbuzz items

## Requirements

- Python 3.8
- Django 3.2
- Django REST Framework

## Installation

Clone the repository and set up a local development environment:

```bash
git clone https://github.com/ahmadrezatabibi/fizzbuzz.git
cd fizzbuzz
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py makemigrations fizzbuzz
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/fizzbuzz` in your browser to view the browsable API.

## Configuration

For local development, set the following environment variables:

```bash
export DJANGO_SECRET_KEY='your_secret_key'
export DJANGO_DEBUG='True'
export DJANGO_ALLOWED_HOSTS='localhost,127.0.0.1'
```

For production environments, ensure `DJANGO_DEBUG` is set to `False` and configure `DJANGO_ALLOWED_HOSTS` with your actual domain names or IP addresses.

## API Endpoints

### List Fizzbuzz Items
- **Endpoint**: `GET /fizzbuzz/`
- **Response Body**:
    ```json
    [
        {
            "fizzbuzz_id": 1,
            "creation_date": "2024-02-11T01:09:41.679514Z",
            "message": "Example Fizzbuzz message",
            "user_agent": "Mozilla/5.0"
        }
    ]
    ```

### Retrieve a Fizzbuzz Item
- **Endpoint**: `GET /fizzbuzz/{id}/`
- **Response Body**:
    ```json
    {
        "fizzbuzz_id": 1,
        "creation_date": "2024-02-11T01:09:41.679514Z",
        "message": "Example Fizzbuzz message",
        "user_agent": "Mozilla/5.0"
    }
    ```

### Create a Fizzbuzz Item
- **Endpoint**: `POST /fizzbuzz/`
- **Request Body**:
    ```json
    {
        "message": "New Fizzbuzz message",
        "user_agent": "Mozilla/5.0"
    }
    ```
- **Response Body**:
    ```json
    {
        "fizzbuzz_id": 2,
        "creation_date": "2024-02-11T01:09:41.679514Z",
        "message": "New Fizzbuzz message",
        "user_agent": "Mozilla/5.0"
    }
    ```


## Testing

Run tests using the Django test framework:

```bash
python manage.py test
```
