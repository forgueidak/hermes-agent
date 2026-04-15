# Hermes Agent

A fork of [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — an AI agent framework powered by Hermes models with tool-calling and structured output capabilities.

> **Personal fork** — I'm using this to experiment with local LLM agents via Ollama. My default config targets `hermes3` running locally.

## Features

- 🤖 **Hermes Model Integration** — Optimized for NousResearch Hermes series models
- 🔧 **Tool Calling** — Native function/tool calling support via structured XML and JSON schemas
- 💬 **Multi-turn Conversations** — Stateful conversation management
- 🧠 **Structured Outputs** — Enforce response schemas using Hermes prompt format
- 🐳 **Docker Support** — Containerized deployment ready
- 🔌 **OpenAI-Compatible API** — Drop-in replacement for OpenAI-based workflows

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- Access to a Hermes-compatible model endpoint (local via Ollama/llama.cpp or remote)

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-org/hermes-agent.git
cd hermes-agent
```

### 2. Set up environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Install dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

### 4. Run the agent

```bash
uv run python -m hermes_agent
```

## Configuration

All configuration is handled via environment variables. See [`.env.example`](.env.example) for a full list of options.

### Key Variables

| Variable | Description | Default |
|---|---|---|
| `MODEL_NAME` | Hermes model identifier | `NousResearch/Hermes-3-Llama-3.1-8B` |
| `API_BASE_URL` | Model API endpoint | `http://localhost:11434/v1` |
| `API_KEY` | API authentication key | `ollama` |
| `MAX_TOKENS` | Maximum tokens per response | `4096` |
| `TEMPERATURE` | Sampling temperature | `0.2` |
| `MAX_TOOL_ROUNDS` | Max consecutive tool-call iterations before stopping | `5` |
| `SYSTEM_PROMPT_PATH` | Path to a custom system prompt file | `prompts/default.txt` |
| `VERBOSE_TOOL_CALLS` | Print tool call inputs/outputs to stdout for debugging | `false` |

> **Note:** I lowered `TEMPERATURE` to `0.2` (from `0.7`) for more deterministic tool-calling behavior.

> **Note:** `MAX_TOOL_ROUNDS` defaults to `5` in my setup — I found the agent would occasionally loop indefinitely on ambiguous queries without a hard cap.

> **Note:** `SYSTEM_PROMPT_PATH` lets you swap in a custom system prompt without touching the code — handy for testing different personas or task-specific instructions.

> **Note:** `VERBOSE_TOOL_CALLS=true` is useful when debugging tool chains locally — it logs each tool invocation and its result so you can trace exactly what the agent is doing.

> **Note:** When running against Ollama, make sure the model is already pulled before starting the agent (`ollama pull hermes3`), otherwise the first request will time out while Ollama downloads it in the background.

## Docker

```bash
docker build -t hermes-agent .
docker run --env-file .env hermes-agent
```

## Project Structure

```
hermes-agent/
├── hermes_agent/          # Main package
│   ├── __init__.p
```
