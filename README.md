# Hermes Agent

A fork of [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — an AI agent framework powered by Hermes models with tool-calling and structured output capabilities.

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
| `TEMPERATURE` | Sampling temperature | `0.7` |

## Docker

```bash
docker build -t hermes-agent .
docker run --env-file .env hermes-agent
```

## Project Structure

```
hermes-agent/
├── hermes_agent/          # Main package
│   ├── __init__.py
│   ├── __main__.py        # Entry point
│   ├── agent.py           # Core agent logic
│   ├── tools/             # Tool definitions
│   ├── prompts/           # System prompts
│   └── utils/             # Utilities
├── tests/                 # Test suite
├── .env.example           # Environment template
├── Dockerfile
└── pyproject.toml
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Commit your changes
4. Open a Pull Request

Please use the [issue templates](.github/ISSUE_TEMPLATE/) for bug reports and feature requests.

## License

MIT License — see [LICENSE](LICENSE) for details.

## Acknowledgements

- [NousResearch](https://nousresearch.com/) for the original hermes-agent and Hermes model series
- The open-source LLM community
