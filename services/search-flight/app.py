from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Search Flight Service")

class Flight(BaseModel):
    provider: str
    origin: str
    destination: str
    travel_date: str
    price: int

@app.get("/flights", response_model=List[Flight])
def search_flights(
    origin: str = Query(..., description="IATA code of departure"),
    destination: str = Query(..., description="IATA code of arrival"),
    travel_date: str = Query(..., description="Date in YYYY-MM-DD")
):
    return [
        Flight(provider="ProviderA", origin=origin, destination=destination, travel_date=travel_date, price=120),
        Flight(provider="ProviderB", origin=origin, destination=destination, travel_date=travel_date, price=150),
    ]
