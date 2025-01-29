from fastapi import FastAPI, Request, status 
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime

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

@app.get("/")
async def main():
    return {
        "email": "tobbytobs1@gmail.com",
        "current_datetime": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "github_url": "https://github.com/Lftobs/hng-be-1"
    }

