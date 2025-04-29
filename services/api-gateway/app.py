from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

SEARCH_URL = "http://search-flight:4000"

@app.get("/flights")
async def proxy_flights(
    origin: str = Query(...),
    destination: str = Query(...),
    travel_date: str = Query(...)
):
    params = {"origin": origin, "destination": destination, "travel_date": travel_date}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{SEARCH_URL}/flights", params=params)
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPError:
            raise HTTPException(status_code=502, detail="Error contacting search-flight")
