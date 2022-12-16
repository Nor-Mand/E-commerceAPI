from fastapi import APIRouter, HTTPException
from schemas.clients.schema_countries import Countries
from uuid import uuid4 as uuid

countries = APIRouter()

countryData = []


# Get all countries
@countries.get('/countries', tags=["Clients: Get methods"])
def get_countries():
    return countryData

# Get country by id
@countries.get('/countries/{country_id}', tags=["Clients: Get methods"])
def get_countries_id(country_id: str):
    for country in countryData:
        if country["id"] == country_id:
            return country
    raise HTTPException(status_code=404, detail="Not Found")


# Create country
@countries.post('/countries/', tags=["Clients: Post methods"])
def create_countries(country: Countries):
    country.id = str(uuid())
    countryData.append(country.dict())
    return countryData[-1]


# Delete country
@countries.delete('/countries/{country_id}', tags=["Clients: Delete methods"])
def delete_countries(country_id: str):
    for index, country in enumerate(countryData):
        if country["id"] == country_id:
            countryData.pop(index)
        return {"message": f"Country {country['name']} was delete successfully"}
    raise HTTPException(status_code=404, detail="Not Found")


# Update country
@countries.put('/countries/{country_id}', tags=["Clients: Put methods"])
def update_countries(country_id: str, update: Countries):
    for index, country in enumerate(countryData):
        if country["id"] == country_id:
            countryData[index]["name"] = update.name
            countryData[index]["write_at"] = update.write_at
            return{"message": f"Country with id: {country_id}, was delete successfully"}
    raise HTTPException(status_code=404, detail="Not Found")
