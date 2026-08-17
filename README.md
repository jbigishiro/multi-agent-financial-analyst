# Multi-Agent Financial Analys

A production-oriented multi-agent AI system for financial company analysis, built with **LangGraph, LangChain, OpenAI, RAG, FastAPI, and Docker**.
The system accepts a company name such as NVIDIA and orchestrates specialized AI agents for:

* Company and industry research
* Financial analysis using retrieved financial documents
* Risk identification
* Final report generation

The project demonstrates how to build, test, containerize, and expose a multi-agent AI application through a REST API.


## Architecture

```text
                         User
                           │
                           ▼
                      FastAPI API
                           │
                           ▼
                    Analysis Service
                           │
                           ▼
                      LangGraph
                           │
                           ▼
                      Supervisor
                    /      |       \
                   ▼       ▼        ▼
              Research  Finance    Risk
                 │         │         │
                 ▼         ▼         ▼
               Tavily      RAG      Tavily
                 │         │         │
                 └─────────┼─────────┘
                           ▼
                      Writer Agent
                           │
                           ▼
                      Final Report
                           │
                           ▼
                     API Response
```

### Workflow

1. The client submits a company name to `POST /analyze`.
2. FastAPI validates the request.
3. The analysis service initializes the LangGraph state.
4. The supervisor determines which agent should execute.
5. The research agent gathers company and industry information.
6. The finance agent retrieves relevant financial information through RAG.
7. The risk agent identifies relevant risks.
8. The writer agent combines the available information into a final report.
9. FastAPI returns the completed analysis.



## Tech Stack

| Technology   | Purpose                                  |
| ------------ | ---------------------------------------- |
| Python       | Application development                  |
| LangGraph    | Multi-agent workflow orchestration       |
| LangChain    | LLM and tool integration                 |
| OpenAI       | Language model and embeddings            |
| RAG          | Financial document retrieval             |
| Vector Store | Semantic search over financial documents |
| Tavily       | Web research                             |
| FastAPI      | REST API                                 |
| Pydantic     | Request/response validation              |
| Pytest       | Automated testing                        |
| Docker       | Containerization                         |
| Git          | Version control                          |
| GitHub       | Source control and collaboration         |


## API

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

### Financial Analysis

```http
POST /analyze
```

Request:

```json
{
  "company": "NVIDIA"
}
```

Response:

```json
{
  "request_id": "42bd1e84-6de8-4f97-94d0-181785a79bd4",
  "company": "NVIDIA",
  "report": "..."
}
```

Interactive API documentation is available through FastAPI's Swagger UI:

`http://127.0.0.1:8000/docs`

## Running with Docker

Build the Docker image:

```bash
docker build -t multi-agent-financial-analyst .
```

Run the container:

```bash
docker run --env-file .env -p 8000:8000 multi-agent-financial-analyst
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Testing

The project includes automated tests covering the API, agents, RAG pipeline, workflow, financial calculations, document processing, retrieval, search, and supporting services.

Run the complete test suite:

```bash
pytest -v
```

Expected result:

```text
29 passed
```
The tests are designed to verify individual components as well as the complete analysis workflow.


## Limitations

This project is a production-oriented prototype rather than a production financial advisory platform.

Current limitations include:

* Financial data coverage depends on the available documents and external tools.
* LLM-generated reports require validation before being used for financial decisions.
* The current deployment is designed primarily for demonstration and portfolio purposes.
* Production deployment would require authentication, persistent infrastructure, monitoring, and stronger evaluation.
* Financial analysis should not be interpreted as investment advice.


## Future Improvements

Potential improvements include:

* Persistent production checkpoint storage
* Authentication and authorization
* CI/CD pipeline
* Cloud deployment
* Improved observability and monitoring
* LLM evaluation and quality metrics
* Token and API cost tracking
* Streaming responses
* More robust financial-data extraction
* Additional financial data sources
* Automated agent evaluation
* Improved caching and performance
