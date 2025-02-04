from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime

import httpx
from .utils import is_armstrong, is_prime, is_perfect, digit_sum

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/classify-number")
async def classify_number(number: str = Query(...)):
    try:
        num = int(number)
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True}
        )
    
    parity = "even" if num % 2 == 0 else "odd"
    armstrong = is_armstrong(num)
    properties = ["armstrong", parity] if armstrong else [parity]
    
    prime = is_prime(num)
    perfect = is_perfect(num)
    digit_sum_val = digit_sum(num)
    async def get_fun_fact(num: int) -> str:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"http://numbersapi.com/{num}/math?json",
                    timeout=5.0
                )
                if response.status_code == 200:
                    data = response.json()
                    if data.get("found", False):
                        return data.get("text", "")
            except (httpx.RequestError, KeyError, ValueError):
                pass
        return ""

    fun_fact = await get_fun_fact(num)
    
    return {
        "number": num,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": digit_sum_val,
        "fun_fact": fun_fact
    }


@app.get("/")
async def main():
    return {
        "email": "tobbytobs1@gmail.com",
        "current_datetime": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Lftobs/hng-be-1"
    }


