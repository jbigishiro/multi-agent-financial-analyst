# Multi-Agent Financial Analyst

A production-oriented multi-agent financial analysis system built with **Python, FastAPI, LangGraph, LangChain, RAG, Docker, and LLMs**.

The system coordinates multiple specialized agents to research a company, analyze financial information, identify risks, and generate a final financial report.

## Architecture

```text
                         ┌──────────────────┐
                         │      Client      │
                         │   Swagger / API  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     FastAPI      │
                         │   POST /analyze  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    LangGraph     │
                         │    Supervisor    │
                         └────────┬─────────┘
                                  │
               ┌──────────────────┼──────────────────┐
               ▼                  ▼                  ▼
        ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
        │  Research   │    │   Finance   │    │    Risk     │
        │    Agent    │    │    Agent    │    │    Agent    │
        └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
               │                  │                  │
               ▼                  ▼                  ▼
          Web Search            RAG              Web Search
                              / Financial
                              Documents
               │                  │                  │
               └──────────────────┼──────────────────┘
                                  ▼
                         ┌──────────────────┐
                         │   Writer Agent   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  Financial       │
                         │     Report       │
                         └──────────────────┘
```

## Features

* Multi-agent architecture using LangGraph
* Supervisor-based agent routing
* Research agent for company research
* Finance agent for financial analysis
* Risk agent for risk identification
* Writer agent for final report generation
* RAG pipeline for financial documents
* Vector database for document retrieval
* Web search integration
* Persistent workflow memory/checkpointing
* Retry handling for LLM operations
* Structured API responses
* Request ID tracking
* Centralized logging
* FastAPI REST API
* Swagger/OpenAPI documentation
* Automated pytest test suite
* Docker containerization

## Technology Stack

| Category            | Technology               |
| ------------------- | ------------------------ |
| Language            | Python 3.12              |
| API                 | FastAPI                  |
| LLM Framework       | LangChain                |
| Agent Orchestration | LangGraph                |
| LLM                 | OpenAI                   |
| Web Search          | Tavily                   |
| RAG                 | LangChain + Vector Store |
| Embeddings          | OpenAI Embeddings        |
| PDF Processing      | PyPDF                    |
| Validation          | Pydantic                 |
| Testing             | Pytest                   |
| Containerization    | Docker                   |
| API Server          | Uvicorn                  |

## Project Structure

```text
multi-agent-financial-analyst/
│
├── app.py
├── Dockerfile
├── README.md
├── requirements.txt
├── .env
├── .gitignore
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── llm.py
│
├── agents/
│   ├── research.py
│   ├── finance.py
│   ├── risk.py
│   ├── writer.py
│   └── supervisor.py
│
├── graph/
│   ├── __init__.py
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
│
├── services/
│   └── analysis.py
│
├── schemas/
│   └── schemas.py
│
├── tools/
│   ├── search.py
│   ├── finance.py
│   └── financial_rag.py
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── retriever.py
│
├── tests/
│   ├── test_api.py
│   ├── test_workflow.py
│   ├── test_finance_agent.py
│   ├── test_risk.py
│   ├── test_search.py
│   ├── test_vectorstore.py
│   └── ...
│
└── documents/
    └── financial documents
```

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd multi-agent-financial-analyst
```

Create a virtual environment:

```bash
python3.12 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Never commit `.env` or API keys to GitHub.

## Run Locally

Start the FastAPI application:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## API

### Health Check

```http
GET /health
```

Example:

```bash
curl http://127.0.0.1:8000/health
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

Example:

```bash
curl -X POST \
  http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"company":"NVIDIA"}'
```

Response:

```json
{
  "request_id": "42bd1e84-6de8-4f97-94d0-181785a79bd4",
  "company": "NVIDIA",
  "report": "Financial analysis report..."
}
```

## Docker

Build the image:

```bash
docker build -t multi-agent-financial-analyst .
```

Run the container:

```bash
docker run --env-file .env -p 8000:8000 multi-agent-financial-analyst
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Testing

Run the complete test suite:

```bash
pytest -v
```

The project contains tests covering:

* API endpoints
* Analysis service
* Financial calculations
* Embeddings
* Finance tools
* Finance agent
* Financial RAG
* PDF loading
* Workflow memory
* Retriever
* Risk agent
* Web search
* Document splitting
* Supervisor
* Vector store
* Full LangGraph workflow
* Writer agent

## Example Workflow

For a request such as:

```json
{
  "company": "NVIDIA"
}
```

the system approximately follows:

```text
User Request
     │
     ▼
FastAPI
     │
     ▼
Supervisor
     │
     ├──► Research Agent ──► Web Search
     │
     ├──► Finance Agent ──► RAG / Financial Documents
     │
     └──► Risk Agent ─────► Web Search
                             
              │
              ▼
        Writer Agent
              │
              ▼
       Final Financial Report
```

## Engineering Practices

This project demonstrates several production-oriented engineering concepts:

* Modular project structure
* Separation of API, services, agents, tools, and RAG components
* Environment-based configuration
* Dependency isolation
* Structured request/response schemas
* Error handling
* Logging
* Request tracing with request IDs
* Automated testing
* Workflow state management
* LangGraph checkpointing
* Docker deployment

## Testing Result

The project currently has a comprehensive automated test suite covering the major application components.

Run:

```bash
pytest -v
```

Expected result:

```text
29 passed
```

## Future Improvements

Potential improvements include:

* Add a frontend dashboard
* Add authentication and authorization
* Add PostgreSQL for persistent application data
* Replace development checkpoint storage with production persistence
* Add Redis for distributed caching
* Add CI/CD with GitHub Actions
* Add cloud deployment
* Add monitoring and observability
* Add automated evaluation of LLM responses
* Add streaming responses
* Add asynchronous agent execution
* Improve financial data extraction
* Add more financial data sources
* Add model evaluation and cost tracking

## Disclaimer

This project is for educational and engineering demonstration purposes.

It does not provide financial advice or investment recommendations.

## Author

Justin
