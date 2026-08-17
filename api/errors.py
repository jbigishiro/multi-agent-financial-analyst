from fastapi import Request
from fastapi.responses import JSONResponse

from config.logging import logger


async def general_exception_handler(
    request: Request,
    exc: Exception
):
    request_id = getattr(
        request.state,
        "request_id",
        "unknown"
    )

    logger.exception(
        f"[{request_id}] "
        f"Unhandled error on "
        f"{request.method} {request.url.path}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "request_id": request_id,
            "detail": "Internal server error."
        }
    )