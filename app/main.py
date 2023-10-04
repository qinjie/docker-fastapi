from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging
from fastapi import File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from routes.api import router as api_router
import uvicorn
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('main')

app = FastAPI()

# origins = ["http://localhost:8000"]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root(request: Request):
    logger.info(f'{str(request.url)}\t{request.headers}')
    return {"message": "Hello World", 'request.headers': request.headers}


@app.get("/users")
async def users(request: Request):
    logger.info(f'{str(request.url)}\t{request.headers}')
    users = [
        {
            "name": "Mars Kule",
            "age": 25,
            "city": "Lagos, Nigeria"
        },
        {
            "name": "Mercury Lume",
            "age": 23,
            "city": "Abuja, Nigeria"
        },
    ]

    return users


@app.post("/")
async def post_message(msg: Msg, request: Request):
    logger.info(f'{str(request.url)}\t{request.headers}')

    return {'message': msg, 'request.headers': request.headers}


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        with open(file.filename, 'wb') as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload = True)
    print("running")