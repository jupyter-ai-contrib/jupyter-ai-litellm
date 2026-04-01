# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a JupyterLab extension that provides LiteLLM model abstraction for Jupyter AI. It exposes LiteLLM's extensive catalog of language models (OpenAI, Anthropic, Google, Cohere, Azure, AWS, etc.) through a standardized REST API.

## Development Commands

### Setup and Installation
```bash
# Development install
pip install -e ".[test]"
jupyter server extension enable jupyter_ai_litellm

# Development uninstall
jupyter server extension disable jupyter_ai_litellm
pip uninstall jupyter_ai_litellm
```

### Testing
```bash
# Install test dependencies
pip install -e ".[test]"

# Run all tests with coverage
pytest -vv -r ap --cov jupyter_ai_litellm

# Run specific test file
pytest jupyter_ai_litellm/tests/test_handlers.py -v
```

### Package Building
```bash
# Build package (uses hatchling)
python -m build

# Version management
hatch version
```

## Architecture

### Core Components

- **`jupyter_ai_litellm/__init__.py`**: Extension entry point and Jupyter server integration
- **`jupyter_ai_litellm/handlers.py`**: Request routing and handler setup
- **`jupyter_ai_litellm/chat_models_rest_api.py`**: REST API handler for chat models endpoint
- **`jupyter_ai_litellm/model_list.py`**: LiteLLM model discovery and categorization

### API Endpoints

The extension provides REST endpoints under `/api/ai/`:
- `GET /api/ai/models/chat` - Returns list of available chat models in LiteLLM format

### Model Discovery

Models are automatically discovered from LiteLLM's `models_by_provider` and categorized into:
- Chat models (stored in `CHAT_MODELS`)
- Embedding models (stored in `EMBEDDING_MODELS`)

Model IDs follow LiteLLM format: `provider/model-name` (e.g., `openai/gpt-4`, `anthropic/claude-3-sonnet`)

### Jupyter Server Integration

The extension registers as a Jupyter server extension through:
- `_jupyter_server_extension_points()` - Declares extension module
- `_load_jupyter_server_extension()` - Sets up handlers and logging
- Server configuration in `jupyter-config/server-config/jupyter_ai_litellm.json`

### Testing Framework

Uses pytest with:
- `pytest-jupyter` for Jupyter server testing
- `jp_fetch` fixture for API endpoint testing
- Configuration via `conftest.py`

## Key Dependencies

- `jupyter_server>=2.4.0,<3` - Jupyter server framework
- `litellm>=1.73,<2` - Model abstraction library
- `tornado` - Web framework (via jupyter_server)
- `pydantic` - Data validation for API responses