from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
from dotenv import load_dotenv
import os

app = FastAPI()
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
        "greating": text,
    })