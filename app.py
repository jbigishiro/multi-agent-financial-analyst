from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from graph.workflow import graph
from config.logging import logger


app = FastAPI(
    title="Multi-Agent Financial Analyst",
    version="1.0.0",
)


class AnalysisRequest(BaseModel):
    company: str


class AnalysisResponse(BaseModel):
    company: str
    report: str


@app.get("/")
def root():
    return {
        "message": "Multi-Agent Financial Analyst API"
    }


@app.post(
    "/analyze",
    response_model=AnalysisResponse
)
def analyze(request: AnalysisRequest):

    if not request.company.strip():
        logger.warning("Empty company name received.")

        raise HTTPException(
            status_code=400,
            detail="Company name cannot be empty."
        )

    logger.info(
        f"Starting financial analysis for {request.company}"
    )

    state = {
        "company": request.company,
        "research": "",
        "finance": "",
        "risk": "",
        "report": "",
        "next": "",
    }

    config = {
        "configurable": {
            "thread_id": f"analysis-{request.company}"
        }
    }

    try:

        result = graph.invoke(
            state,
            config=config
        )

        if not result.get("report"):
            logger.error(
                f"Empty report generated for {request.company}"
            )

            raise HTTPException(
                status_code=500,
                detail="Report generation failed."
            )

        logger.info(
            f"Financial analysis completed for {request.company}"
        )

        return {
            "company": request.company,
            "report": result["report"]
        }

    except HTTPException:
        raise

    except Exception:
        logger.exception(
            f"Analysis failed for {request.company}"
        )

        raise HTTPException(
            status_code=500,
            detail="Financial analysis failed."
        )