from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
import os
import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()

def get_real_ip(request: Request):
    headers = request.headers
    if 'x-forwarded-for' in headers:
        return headers['x-forwarded-for'].split(',')[0].strip()
    elif 'x-real-ip' in headers:
        return headers['x-real-ip']
    else:
        return request.client.host

@app.get("/api/hello")
async def greeting(request: Request, visitor_name: str):
    ip_add = get_real_ip(request)
    name = visitor_name.replace('"', '')
    url  = f'https://api.weatherapi.com/v1/current.json?q={ip_add}&key={os.getenv("KEY")}'
    res = requests.get(url)
    data = res.json()
    location = data["location"].get('region', 'Delhi')
    text = f'Hello, {name}!, the temperature is {data["current"]["temp_c"]} degrees Celsius in {location}'
    
    return JSONResponse(content={
        "client_ip": ip_add,
        "location": location,
        "greeting": text,
    })

@app.get('/api/products')
async def get_products(request: Request):
    url = f'https://api.timbu.cloud/products?{request.query_params}'
    print(url)
    res = requests.get(url)
    data = res.json()
    return JSONResponse(content=data)

@app.get('/api/products/{product_id}')
async def get_products(product_id: str, request: Request):
    url = f'https://api.timbu.cloud/products/{product_id}?{request.query_params}'
    res = requests.get(url)
    data = res.json()
    return JSONResponse(content=data)