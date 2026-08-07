import sys

from loguru import logger

LEVEL_SHORT = {
    "TRACE": "TRC",
    "DEBUG": "DBG",
    "INFO": "INF",
    "SUCCESS": "SUC",
    "WARNING": "WRN",
    "ERROR": "ERR",
    "CRITICAL": "CRI",
}


def _compact_formatter(record):
    """Build a compact, pipe-delimited log line: seconds-precision time,
    3-letter level code, no separate dash before the message.
    """
    record["extra"]["level_short"] = LEVEL_SHORT.get(
        record["level"].name, record["level"].name[:3]
    )
    return (
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "<level>{extra[level_short]}</level> | "
        "{name} | {function} | {line} | "
        "<level>{message}</level>\n{exception}"
    )


def configure_logging():
    """Configure loguru for console and file logging.

    Removes the default handler and sets up:
    - stderr handler at LOG_LEVEL (default: INFO, configurable via env var)
    - File handler at DEBUG level writing to LOG_FILE (default: app.log)

    Both handlers share a compact format (see _compact_formatter).
    """
    import os

    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_file = os.environ.get("LOG_FILE", "app.log")
    logger.remove()
    logger.add(sys.stderr, level=log_level, format=_compact_formatter)
    logger.add(
        log_file,
        level="DEBUG",
        rotation="50 KB",
        retention=1,
        format=_compact_formatter,
    )


@logger.catch
def main():
    """Run the application.

    Configures logging and prints a greeting to verify the setup works.
    """
    configure_logging()
    logger.info("Hello from secondbrain!")
