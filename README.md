# AI Coding Agent 🚀

An autonomous, terminal-based AI Coding Agent built for the Elite Coders Open Source Hackathon 2026. This agent is designed to inspect local project files, analyze code logic, and automatically detect and patch bugs using an advanced agentic loop.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **Environment & Package Manager:** [uv](https://github.com/astral-sh/uv) (Strictly isolated virtual environment)
- **LLM Core:** Google Gemini 2.5 Flash (`google-genai` SDK)

## ⚡ Current Progress (Day 1)
- [x] Initialized cross-platform isolated sandbox configuration using `uv`.
- [x] Integrated secure runtime environment variable mapping for API credentials.
- [x] Established live client connection to `gemini-2.5-flash` with precise real-time token telemetry tracking.
- [ ] Implement local file system execution tools (Phase 2)
- [ ] Orchestrate the autonomous feedback execution loop (Phase 3)

## 🚀 Getting Started

Ensure you have your `GEMINI_API_KEY` configured in a local `.env` file, then initialize the pipeline:

```bash
# Install dependencies securely within the project vault
C:\Users\Nyx\AppData\Roaming\Python\Python314\Scripts\uv add google-genai python-dotenv

# Run a query through the foundational terminal pipeline
python main.py "Your prompt here" --verbose