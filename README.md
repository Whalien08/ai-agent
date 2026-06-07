# AI Coding Agent 

An autonomous, terminal-based AI Coding Agent engineered for the **Elite Coders Open Source Hackathon 2026**. This intelligent system is designed to inspect local multi-directory codebases, structurally parse logical files, execute scripts to analyze error streams, and automatically deploy functional patches using a closed-loop agentic workflow.

---

## 🛠️ Tech Stack & Architecture

- **Language:** Python 3.14
- **Environment & Dependency Manager:** [uv](https://github.com/astral-sh/uv) (Fast, strictly isolated virtual sandboxing)
- **LLM Core Engine:** Google Gemini 2.5 Flash via the modern `google-genai` SDK
- **Telemetry System:** Live contextual token metric monitoring per agent iteration

---

## ⚡ Core Features & Capabilities

### 1. Autonomous Agentic Loop
The system orchestrates a multi-turn reasoning loop (capped at 15 iterations for structural safety) where the LLM evaluates terminal/test outputs, decides on sequential file system actions, and repeats until the user's requirements are satisfied or all test suites pass.

### 2. High-Fidelity File System Tools ("The Hands")
The agent is armed with four native Python execution tools mapped via explicit SDK schemas:
* `get_files_info`: Lists folder directories, sizes, and item categories recursively.
* `get_file_content`: Reads full file texts with an embedded 10,000-character circuit breaker to optimize token limits.
* `write_file`: Overwrites or initializes files to apply precise debugging patches.
* `run_python_file`: Executes scripts inside a separate runtime subprocess with a 30-second timeout, feeding raw `stdout` and `stderr` directly back into the AI's short-term context.

### 3. Absolute Security Sandboxing
To avoid unpredictable file modification behavior, the system implements a strict path-resolution validation check. Using deterministic string comparisons (`startswith`), the agent's actions are permanently restricted to the specified project directory (e.g., `calculator/`). Any attempt to pass absolute system parameters or directory traversals (such as `../../`) results in an instant hard stop and an automated access denial.

---

## 🚀 Completed Milestones (Final Status)

- [x] **Phase 1 (The Foundations):** Configured isolated package environments using `uv`, structured secure `.env` variable mapping, and established real-time token telemetry streams.
- [x] **Phase 2 (The Toolkit):** Programmed four decoupled file manipulation tools featuring strict defensive sandboxing logic against arbitrary system crawling.
- [x] **Phase 3 (The Scheme Mappings):** Translated low-level tools into official `FunctionDeclaration` structures allowing Gemini to cleanly evaluate complex system calls.
- [x] **Phase 4 (The Agentic System):** Orchestrated the complete autonomous problem-solving feedback loop, successfully testing it against an algorithmic bug within a multi-directory modular calculator application.

---

## 📦 Getting Started & Verification

### 1. Setup Instructions
Ensure your Google AI Studio credentials are securely configured inside a local environment file. 
Create a file named .env and add this line:
GEMINI_API_KEY=your_actual_api_key_here

### 2. Installation & Launch
Activate your sandbox workspace and execute a project query directly via the terminal:

python main.py "Fix the bug in the calculator. Run test.py to see what fails, identify the bug, overwrite the broken file to patch it, and confirm the fix runs successfully." --verbose

---

## 📜 Project Showcase: Sample Execution Log

Agent engine initialized. Executing task loop...

[Iteration 1 Metrics] Total Tokens Used: 453
 -> AI requesting tool execution: run_python_file({'file_path': 'test.py'})

[Iteration 2 Metrics] Total Tokens Used: 648
 -> AI requesting tool execution: get_files_info({})

[Iteration 3 Metrics] Total Tokens Used: 689
 -> AI requesting tool execution: get_file_content({'file_path': 'main.py'})

[Iteration 4 Metrics] Total Tokens Used: 888
 -> AI requesting tool execution: get_file_content({'file_path': 'pkg/calculator.py'})

[Iteration 5 Metrics] Total Tokens Used: 2026
 -> AI requesting tool execution: write_file({'file_path': 'pkg/calculator.py', 'content': '...'})
    Success: Successfully wrote 1845 characters to 'pkg/calculator.py'.

[Iteration 6 Metrics] Total Tokens Used: 1848
 -> AI requesting tool execution: run_python_file({'file_path': 'test.py'})
 
🚀 [Agent Final Response]:
The operator precedence error in 'pkg/calculator.py' was successfully located. I corrected the addition operator priority back to 1, ran the unit tests via test.py, and verified that all 5 verification suites are now passing with clean execution states.


## 🤝 Credits & Inspiration
The foundational architecture for this agent was inspired by Lane Wagner's freeCodeCamp tutorial. However, this repository represents a significantly upgraded, custom implementation:
- Migrated from the deprecated `google-generativeai` library to the modern `google-genai` SDK.
- Re-engineered tool function declarations to match the new SDK's schema requirements.
- Implemented API rate-limit mitigation (429/503 error handling) using custom interval logic.
- Hardened cross-platform absolute path resolution for strict Windows/PowerShell sandboxing.