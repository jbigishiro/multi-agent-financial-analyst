# Multi-Agent Financial Analyst

An AI-powered financial analysis system that uses multiple specialized agents to analyze a company's financial information from an uploaded PDF document and current web information.

The system combines:

- Multi-agent orchestration with LangGraph
- Retrieval-Augmented Generation (RAG)
- PDF document processing
- Vector search with Chroma
- OpenAI embeddings and LLMs
- Web search with Tavily
- FastAPI for the REST API

The goal of the project is to simulate a financial analyst team where different AI agents specialize in research, financial analysis, risk analysis, and report generation.

---

## Features

### Multi-Agent Financial Analysis

The system uses specialized agents for different parts of the analysis:

1. **Supervisor Agent**
   - Controls the workflow.
   - Determines which stage should run next.

2. **Research Agent**
   - Researches the company using current web information.
   - Looks for:
     - Recent developments
     - Company announcements
     - Industry trends
     - Competitors
     - Market developments

3. **Finance Agent**
   - Analyzes the uploaded financial document.
   - Uses RAG to retrieve relevant financial information.
   - Focuses on:
     - Revenue
     - Profitability
     - Cash flow
     - Financial trends
     - Financial risks

4. **Risk Agent**
   - Uses current web information to identify important risks.
   - Focuses on:
     - Business risks
     - Competitive risks
     - Regulatory risks
     - Technology risks
     - Market risks
     - Recent developments

5. **Writer Agent**
   - Combines the outputs from the Research, Finance, and Risk agents.
   - Produces the final financial analysis report.

---

# Architecture

The high-level workflow is:

```text
                         ┌──────────────────┐
                         │     FastAPI      │
                         │    /analyze      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Supervisor    │
                         │      Agent       │
                         └────────┬─────────┘
                                  │
                                  ▼
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
      ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
      │   Research   │    │   Finance    │    │     Risk     │
      │    Agent     │    │    Agent     │    │    Agent     │
      └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
             │                   │                   │
             ▼                   ▼                   ▼
          Tavily             PDF + RAG             Tavily
          Search             Chroma                 Search
                                  │
                                  ▼
                         ┌──────────────────┐
                         │      Writer      │
                         │      Agent       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  Final Report    │
                         └──────────────────┘


---

# RAG Pipeline

Uploaded PDF
     │
     ▼
PyPDFLoader
     │
     ▼
Document Pages
     │
     ▼
RecursiveCharacterTextSplitter
     │
     ▼
Document Chunks
     │
     ▼
OpenAI Embeddings
     │
     ▼
Chroma Vector Store
     │
     ▼
Similarity Search
     │
     ▼
Relevant Financial Context
     │
     ▼
Finance Agent


# Project Structure

multi-agent-financial-analyst/
│
├── agents/
│   ├── finance.py
│   ├── research.py
│   ├── risk.py
│   ├── supervisor.py
│   └── writer.py
│
├── config/
│   ├── llm.py
│   ├── logging.py
│   └── settings.py
│
├── graph/
│   ├── nodes.py
│   ├── router.py
│   ├── state.py
│   └── workflow.py
│
├── rag/
│   ├── embeddings.py
│   ├── loader.py
│   ├── pipeline.py
│   ├── retriever.py
│   ├── splitter.py
│   └── vectorstore.py
│
├── services/
│   └── analysis.py
│
├── tools/
│   ├── agent_tools.py
│   ├── calculator.py
│   ├── financial_rag.py
│   └── search.py
│
├── data/
│   ├── uploads/
│   └── chroma/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .env

---
# Technology Stack

| Technology    | Purpose                            |
| ------------- | ---------------------------------- |
| Python        | Primary programming language       |
| FastAPI       | REST API                           |
| Uvicorn       | ASGI server                        |
| LangGraph     | Multi-agent workflow orchestration |
| LangChain     | LLM and tool integration           |
| OpenAI        | LLM and embeddings                 |
| Chroma        | Vector database                    |
| Tavily        | Web search                         |
| PyPDFLoader   | PDF document loading               |
| Pydantic      | Data validation                    |
| python-dotenv | Environment configuration          |
| Git/GitHub    | Version control                    |


