import uuid
import time
from fastapi import FastAPI, HTTPException, Request

from api.errors import general_exception_handler
from config.logging import logger
from config.settings import settings
from api.schemas import AnalysisRequest, AnalysisResponse
from services.analysis import graph
from graph.state import create_initial_state

# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
)

# Global exception handler
app.add_exception_handler(
    Exception,
    general_exception_handler
)


# ============================================================
# Health Check
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ============================================================
# Analyze Company
# ============================================================

@app.post(
    "/analyze",
    response_model=AnalysisResponse
)
def analyze(
    request: Request,
    analysis_request: AnalysisRequest
):

    request_id = request.state.request_id

    # Validate company name
    if not analysis_request.company.strip():

        logger.warning(
            f"[{request_id}] Empty company name received."
        )

        raise HTTPException(
            status_code=400,
            detail="Company name cannot be empty."
        )

    logger.info(
        f"[{request_id}] Starting financial analysis "
        f"for {analysis_request.company}"
    )

    # ========================================================
    # Initial LangGraph State
    # ========================================================

    state = create_initial_state(
        analysis_request.company
    )

    # ========================================================
    # Run LangGraph
    # ========================================================

    try:

        result = graph.invoke(
    state,
    config={
        "configurable": {
            "thread_id": request_id
        }
    }
)

    except Exception:

        logger.exception(
            f"[{request_id}] Financial analysis failed."
        )

        raise HTTPException(
            status_code=500,
            detail="Financial analysis failed."
        )

    # ========================================================
    # Return Response
    # ========================================================

    logger.info(
        f"[{request_id}] Financial analysis completed."
    )

    return AnalysisResponse(
        request_id=request_id,
        company=result["company"],
        research=result["research"],
        finance=result["finance"],
        risk=result["risk"],
        report=result["report"],
    )

@app.middleware("http")
async def log_requests(request: Request, call_next):

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