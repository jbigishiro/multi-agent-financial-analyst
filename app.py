import uuid
import time
from pathlib import Path

from fastapi import (
    FastAPI,
    HTTPException,
    Request,
    UploadFile,
    File,
    Form,
)

from api.errors import general_exception_handler
from config.logging import logger
from config.settings import settings
from api.schemas import AnalysisResponse
from services.analysis import run_analysis

# FastAPI Application

app = FastAPI(title=settings.api_title,version=settings.api_version,)

# Global Exception Handler

app.add_exception_handler(Exception, general_exception_handler)

# Health Check

@app.get("/health")
def health():return {"status": "healthy"}

# Analyze Company

@app.post( "/analyze", response_model=AnalysisResponse)
def analyze(request: Request, company: str = Form(...),file: UploadFile = File(...),):
    request_id = request.state.request_id

    # Validate Company
    if not company.strip():
        logger.warning(f"[{request_id}] Empty company name received.")
        raise HTTPException(status_code=400, detail="Company name cannot be empty.")

    # Validate File
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided.")

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    # Save Uploaded PDF
    upload_dir = Path("data/uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = upload_dir /(f"{request_id}_{file.filename}")

    try:
        with file_path.open("wb") as buffer:
            buffer.write(file.file.read())

    except Exception:
        logger.exception(f"[{request_id}] Failed to save uploaded document.")
        raise HTTPException(status_code=500, detail="Failed to save uploaded document.")

    logger.info( f"[{request_id}] Uploaded document: {file.filename}")

    # Start Financial Analysis
    logger.info(
        f"[{request_id}] Starting financial analysis "
        f"for {company}"
    )

    # Run Analysis Service
    try:
        result = run_analysis(company=company,request_id=request_id,document_path=str(file_path),)

    except Exception:
        logger.exception(f"[{request_id}] Financial analysis failed.")

        raise HTTPException(
            status_code=500,
            detail="Financial analysis failed."
        )

    # Return Response
    logger.info(f"[{request_id}] Financial analysis completed.")

    return AnalysisResponse(request_id=request_id,company=result["company"],report=result["report"],)

# Request Logging Middleware

@app.middleware("http")
async def log_requests(request: Request,call_next,):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(
        f"[{request_id}] "
        f"{request.method} "
        f"{request.url.path} "
        f"status={response.status_code} "
        f"duration={duration:.2f}s"
    )
    response.headers["X-Request-ID"] = request_id
    return response