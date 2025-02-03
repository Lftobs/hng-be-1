from fastapi import FastAPI, Query, Request, status 
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime
import math
import httpx

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def get_real_ip(request: Request):
#     headers = request.headers
#     if 'x-forwarded-for' in headers:
#         return headers['x-forwarded-for'].split(',')[0].strip()
#     elif 'x-real-ip' in headers:
#         return headers['x-real-ip']
#     else:
#         return request.client.host

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    divisors_sum = 0
    sqrt_n = math.isqrt(n)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i == n:
                continue
            divisors_sum += i
            counterpart = n // i
            if counterpart != i and counterpart != n:
                divisors_sum += counterpart
    return divisors_sum == n

def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = list(map(int, str(n)))
    num_digits = len(digits)
    total = sum(d ** num_digits for d in digits)
    return total == n

def digit_sum(n: int) -> int:
    return sum(map(int, str(abs(n))))

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
    
    fun_fact = ""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"http://numbersapi.com/{num}/math?json",
                timeout=5.0
            )
            if response.status_code == 200:
                data = response.json()
                print(data)
                if data.get("found", False):
                    fun_fact = data.get("text", "")
        except (httpx.RequestError, KeyError, ValueError):
            pass
    
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

