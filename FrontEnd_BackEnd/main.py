from fastapi import FastAPI, File, UploadFile
from ml_obj_detection import detect
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile=File(...)):
    out_reponse = detect(file.file)    
    return {
        "objects":out_reponse
    }