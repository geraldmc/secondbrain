# Usage

## Installation

Clone the repository and install dependencies:

```bash
uv sync
```

## Running

Via the CLI entrypoint:

```bash
uv run secondbrain                          # production defaults
uv run --env-file .env secondbrain          # dev settings
```

Or as a Python module:

```bash
uv run python -m secondbrain
```

## Environment Variables

| Variable    | Default    | Description                          |
|-------------|------------|---------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level (DEBUG, INFO, …)   |
| `LOG_FILE`  | `app.log`  | Path to the log file                 |

Copy `.env.example` to `.env` for development defaults, then run with `uv run --env-file .env`.

## Log Format

Both the console handler and the file handler (`LOG_FILE`) share a compact, pipe-delimited
format: a seconds-precision timestamp, a 3-letter level code, and `name | function | line | message`.

```
2026-08-07 12:21:52 | INF | secondbrain.app | main | 62 | Hello from secondbrain!
```

Level codes: `TRC` (TRACE), `DBG` (DEBUG), `INF` (INFO), `SUC` (SUCCESS), `WRN` (WARNING),
`ERR` (ERROR), `CRI` (CRITICAL).
