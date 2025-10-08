# jupyter_ai_litellm

[![Github Actions Status](https://github.com/jupyter-ai-contrib/jupyter-ai-litellm/workflows/Build/badge.svg)](https://github.com/jupyter-ai-contrib/jupyter-ai-litellm/actions/workflows/build.yml)

A JupyterLab extension that provides LiteLLM model abstraction

This extension is composed of a Python package named `jupyter_ai_litellm`.

## Requirements

- JupyterLab >= 4.0.0

## Install

To install the extension, execute:

```bash
pip install jupyter_ai_litellm
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyter_ai_litellm
```

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

## Contributing

### Development install

```bash
# Clone the repo to your local environment
# Change directory to the jupyter_ai_litellm directory
# Install package in development mode
pip install -e ".[test]"

# Server extension must be manually installed in develop mode
jupyter server extension enable jupyter_ai_litellm
```

### Development uninstall

```bash
# Server extension must be manually disabled in develop mode
jupyter server extension disable jupyter_ai_litellm
pip uninstall jupyter_ai_litellm
```

### Testing the extension

#### Server tests

This extension is using [Pytest](https://docs.pytest.org/) for Python code testing.

Install test dependencies (needed only once):

```sh
pip install -e ".[test]"
```

To execute them, run:

```sh
pytest -vv -r ap --cov jupyter_ai_litellm
```

### Packaging the extension

See [RELEASE](RELEASE.md)
