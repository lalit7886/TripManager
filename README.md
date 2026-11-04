<div align="center">

# ✈️ TripManager AI

### Your AI-powered travel planning copilot

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.162-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-FF6B35)](https://langchain-ai.github.io/langgraph)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Persisted-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**TripManager AI plans flights, finds hotel leads, builds day-by-day itineraries, and returns an organized travel response through a modern web interface.**

</div>

---

## 🌟 Highlights

<table>
<tr>
<td width="50%">

### 🧠 Multi-Agent Planning
A LangGraph workflow coordinates specialized agents for flights, hotels, itinerary creation, and the final response.

</td>
<td width="50%">

### 🏨 Smart Hotel Discovery
Uses Tavily search to discover relevant accommodation options for the requested destination.

</td>
</tr>
<tr>
<td>

### ✈️ Live Flight Context
AviationStack plus airport and country data help resolve routes and identify relevant flight information.

</td>
<td>

### 💾 Conversation Memory
PostgreSQL-backed LangGraph checkpoints preserve plans by thread ID across follow-up requests.

</td>
</tr>
<tr>
<td>

### 📄 PDF Export
Generate a polished PDF directly from the browser using the built-in download action.

</td>
<td>

### 🎨 Responsive Interface
A clean, mobile-friendly UI supports quick prompts, loading feedback, copy, and PDF export.

</td>
</tr>
</table>

## 🏗️ How It Works

```mermaid
flowchart LR
    U[🧑 User Request] --> API[⚡ FastAPI /api/travel]
    API --> F[✈️ Flight Agent]
    F --> H[🏨 Hotel Agent]
    H --> I[🗓️ Itinerary Agent]
    I --> R[📝 Final Response Agent]
    R --> UI[🌐 TripManager Web UI]

    F -. AviationStack .-> F
    H -. Tavily Search .-> H
    I -. Groq LLM .-> I
    R -. Groq LLM .-> R
    API <--> DB[(🐘 PostgreSQL Checkpoints)]
```

## 🧰 Technology Stack

| Layer | Technology |
|---|---|
| Web framework | FastAPI, Uvicorn |
| AI orchestration | LangGraph, LangChain |
| Language model | Groq via `langchain-groq` |
| Hotel search | Tavily |
| Flight data | AviationStack, `airportsdata`, `pycountry` |
| Memory | PostgreSQL with LangGraph Postgres checkpointer |
| Frontend | HTML, CSS, JavaScript, Marked, html2pdf |
| Deployment | Docker |

## 📁 Project Structure

```text
TripManager/
├── app.py                 # FastAPI routes and web entry point
├── backend.py             # LangGraph travel-planning workflow
├── requirements.txt       # Python dependencies
├── dockerfile             # Container build configuration
├── static/
│   ├── script.js          # Frontend API, copy, and PDF behavior
│   └── style.css          # Interface styles
├── templates/
│   └── index.html         # Main web page
└── tools/
    ├── flight.py          # Aviation and airport resolution tools
    └── tavily.py          # Hotel and destination web search
```

## 🚀 Getting Started

### Prerequisites

- Python **3.13** recommended
- A PostgreSQL database
- API access for:
  - [Groq](https://console.groq.com)
  - [Tavily](https://tavily.com)
  - [AviationStack](https://aviationstack.com)

### 1. Clone and enter the project

```bash
git clone <your-repository-url>
cd TripManager
```

### 2. Create a virtual environment

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Configure environment variables

Create `.env` in the project directory:

```dotenv
# Required
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
DATABASE_URL=postgresql://username:password@host:5432/database

# Optional
DEFAULT_ORIGIN_IATA=DAC
LANGSMITH_TRACING=false
LANGSMITH_PROJECT=tripmanager
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
```

> **Note:** `DATABASE_URL` should point to a reachable PostgreSQL instance. The application adds `sslmode=require` when it is absent.

### 4. Run the application

```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Open **http://127.0.0.1:8000** in your browser.

## 🐳 Docker

Build the image:

```bash
docker build -t tripmanager-ai .
```

Run it with your environment file:

```bash
docker run --rm -p 8000:8000 --env-file .env tripmanager-ai
```

Then open **http://localhost:8000**.

## 🔌 API

### Create a travel plan

```http
POST /api/travel
Content-Type: application/json
```

```json
{
  "message": "Plan a 7-day Japan trip from Kathmandu under 2 lakhs, including flights, hotels, and sightseeing.",
  "thread_id": null
}
```

### Example request

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Plan a 5-day Dubai trip from Kathmandu",
    "thread_id": null
  }'
```

### Example response fields

```json
{
  "success": true,
  "thread_id": "user_...",
  "answer": "# Trip Summary...",
  "flight_results": "...",
  "hotel_results": "...",
  "itinerary": "...",
  "llm_calls": 2
}
```

Pass the returned `thread_id` in a later request to keep the same LangGraph conversation thread.

## 💡 Example Prompts

- `Plan a complete 7-day Japan trip from Nepal under 2 lakhs.`
- `Plan a 5-day Dubai trip from Kathmandu with hotels and sightseeing.`
- `Plan a budget Thailand trip for two people, with a relaxed itinerary.`
- `Show flight information for Singapore from Dhaka.`

## 🔒 Configuration Notes

- Never commit `.env`, API keys, database credentials, or production secrets.
- Use a dedicated, least-privileged database account for PostgreSQL.
- Live flight availability and prices depend on the AviationStack plan and response data.
- Hotel results are research suggestions from web search and should be verified before booking.

## 🧪 Development

Run the FastAPI app with automatic reload:

```bash
uvicorn app:app --reload
```

Interactive API documentation is available at:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

## 🗺️ Roadmap Ideas

- [ ] Streaming agent progress responses
- [ ] Budget and date-specific search controls
- [ ] User accounts and saved trip history
- [ ] Direct booking-provider integrations
- [ ] Map and route visualization
- [ ] Automated tests and CI workflow

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make focused changes with clear commit messages.
4. Test the API and UI locally.
5. Open a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

<div align="center">

Built with FastAPI, LangGraph, Groq, PostgreSQL, Tavily, and AviationStack.

</div>
