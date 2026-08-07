# secondbrain

## Installation

Clone the repo, then install dependencies:

```bash
uv sync
```

## Usage

Via the CLI entrypoint:

```bash
uv run secondbrain
```

With dev environment settings:

```bash
uv run --env-file .env secondbrain
```

Via the Python module:

```bash
uv run python -m secondbrain
```

## Environment Variables

`.env.example` is the template — copy it to `.env` for development:

```bash
cp .env.example .env
```

| Variable    | Default    | Description                                    |
|-------------|------------|-------------------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level. Set to `DEBUG` in `.env` for verbose output. |
| `LOG_FILE`  | `app.log`  | Path to the log file.                          |

`uv run --env-file .env` loads the dev environment explicitly — it is not auto-loaded.

## Testing

Run tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov
```

## Documentation

Preview docs locally:

```bash
uv run python scripts/serve_docs.py
```

Build static docs:

```bash
uv run mkdocs build
```
