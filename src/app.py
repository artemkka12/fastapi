import time

from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles

from src.router import main_router

app = FastAPI()

app.include_router(main_router)

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
