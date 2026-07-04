from fastapi import FastAPI, Request, UploadFile, Form, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import re
from app.logic import transcribe_audio, extract_fields, save_record

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"record": None},
        request=request
    )


@app.post("/", response_class=HTMLResponse)
async def process_form(
    request: Request,
    session_number: str = Form(...),
    patient_name: str = Form(...),
    audiofile: UploadFile = File(...)
):
    os.makedirs("uploads", exist_ok=True)

    # Derive safe filename with correct extension from content-type
    # (browser-recorded blobs arrive with a generic name like 'blob')
    content_type = audiofile.content_type or ''
    if 'mp4' in content_type:
        ext = '.mp4'
    elif 'ogg' in content_type:
        ext = '.ogg'
    else:
        ext = '.webm'

    raw_base = os.path.splitext(audiofile.filename or 'recording')[0]
    safe_base = re.sub(r'[^a-zA-Z0-9_-]', '_', raw_base)[:64] or 'recording'
    file_path = os.path.join("uploads", safe_base + ext)

    with open(file_path, "wb") as f:
        f.write(await audiofile.read())

    transcript = transcribe_audio(file_path)
    extracted = extract_fields(transcript)
    record = save_record(extracted, patient_name, session_number)

    return templates.TemplateResponse(
        name="index.html",
        context={"record": record},
        request=request
    )
