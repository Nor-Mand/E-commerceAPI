from fastapi import FastAPI
from routes.clients.users import users
from routes.clients.countries import countries

tags_metadata = [
    {"name": "Clients: Get methods", "description": "Get all information user, countries, customers"},
    {"name": "Clients: Post methods", "description": "Create users, countries, customers "},
    {"name": "Clients: Delete methods", "description": "Delete users, countries, customers"},
    {"name": "Clients: Put methods", "description": "Update users, countries, customers"},
]

app = FastAPI(openapi_tags=tags_metadata)


app.include_router(users)
app.include_router(countries)

