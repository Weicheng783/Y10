# Cultime development documentation

## API endpoint docs

To login a user POST call at http://localhost:8000/login/ needs to be sent with header elements:
{
    "username": "admin",
    "password": "admin"
}

User with this receives two tokens: session token(valid for about 5 minutes) and a refresh token (valid for about 24 hours). To refresh token API call to http://localhost:8000/refresh/ needs to be done.

To register a user POST call at http://localhost:8000/register/ needs to be sent with header elements:
{
    "username": "admin",
    "password": "admin",
    "first_name": "Name",
    "last_name": "Last Name"
}

## Problems that needs to be solved

1. Figuring out how to upload images on the backend, including posters of movies and profile pictures