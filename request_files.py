from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(..., description="Afile read as bytes")):
    return {"file_size": len(file)}


@app.post("/upload_file/")
async def upload_file(uploaded_file: UploadFile = File(...)):
    return {
        "filename": uploaded_file.filename,
        "content_type": uploaded_file.content_type,
    }


@app.post("/upload_files/")
async def upload_files(uploaded_files: list[UploadFile] = File(...)):
    return {
        "filenames": [uploaded_file.filename for uploaded_file in uploaded_files],
        "content_types": [
            uploaded_file.content_type for uploaded_file in uploaded_files
        ],
    }
