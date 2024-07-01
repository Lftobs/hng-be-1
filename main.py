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
async def greeting(request: Request, vistor_name: str):
    ip_add = get_real_ip(request)
    name = vistor_name.replace('"', '')
    url  = f'https://ipinfo.io/{ip_add}/json'
    res = requests.get(url)
    data = res.json()
    location = data.get('city', 'Delhi')
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv("KEY")}'
    weather_res = requests.get(weather_url)
    weather_data = weather_res.json()
    text = f'Hello, {name}!, the temperature is {weather_data["main"]["temp"]} degrees Celsius in {location}'
    
    return JSONResponse(content={
        "client_ip": ip_add,
        "location": location,
        "greating": text,
    })