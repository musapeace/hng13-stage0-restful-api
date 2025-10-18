from fastapi import FastAPI
import httpx
from datetime import datetime, timezone
from fastapi.responses import JSONResponse

app = FastAPI()

USER_INFO = {
    "email": "mubarakinda@gmail.com",
    "name": "Muhammad Mubarak Musa",
    "stack": "Python/FastAPI"
}

CAT_FACT_API = "https://catfact.ninja/fact"

@app.get("/me")
async def get_profile():
    # Fetch cat fact
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(CAT_FACT_API)
            data = response.json()
            cat_fact = data.get("fact", "Cats are mysterious creatures 🐱")
    except Exception:
        cat_fact = "Could not fetch cat fact at the moment."

    # Current UTC timestamp in ISO 8601 format
    timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    result = {
        "status": "success",
        "user": USER_INFO,
        "timestamp": timestamp,
        "fact": cat_fact
    }

    return JSONResponse(content=result)
