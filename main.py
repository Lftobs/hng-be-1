from fastapi import FastAPI, Query, Request, status 
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime
from .api.stage_two import stage_two_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {
        "email": "tobbytobs1@gmail.com",
        "current_datetime": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Lftobs/hng-be-1"
    }

app.include_router(stage_two_router, prefix="/api")

