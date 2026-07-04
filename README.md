# Symptom Tracker

Records patient session notes from spoken audio using OpenAI Whisper (transcription) and Groq LLaMA (structured extraction).

Audio can be recorded directly in the browser or uploaded as a file.

---

## Setup

### 1. Create a virtual environment

**Windows:**
```
py -3.12 -m venv venv
```

**macOS / Linux:**
```
python3.12 -m venv venv
```

### 2. Activate the virtual environment

**Windows:**
```
venv\Scripts\activate
```

**macOS / Linux:**
```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set environment variables and run

**Windows (PowerShell):**
```
$env:OPENAI_API_KEY="your_key_here"; $env:GROQ_API_KEY="your_key_here"; python -m uvicorn api.index:app --reload
```

**Windows (Command Prompt):**
```
set OPENAI_API_KEY=your_key_here && set GROQ_API_KEY=your_key_here && python -m uvicorn api.index:app --reload
```

**macOS / Linux:**
```
OPENAI_API_KEY="your_key_here" GROQ_API_KEY="your_key_here" python -m uvicorn api.index:app --reload
```

### 5. Open in browser

- App: http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs

> **Note:** In-browser recording requires a secure context. `http://127.0.0.1` works locally,
> but any other HTTP origin will block microphone access — use HTTPS in production.

---

## Deployments

- Vercel: https://symptom-tracker-njp6xnbsc-safwans-team.vercel.app/
- Render: https://symptom-tracker-jx8r.onrender.com/



