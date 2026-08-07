import os
import re

from secondbrain.app import main

ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")

COMPACT_LOG_LINE_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \| "
    r"INF \| "
    r"secondbrain\.app \| main \| \d+ \| "
    r"Hello from secondbrain!$"
)


def test_main_logs_greeting(capfd):
    main()
    captured = capfd.readouterr()
    assert "Hello from secondbrain!" in captured.err


def test_console_log_format_is_compact_and_pipe_delimited(capfd):
    main()
    captured = capfd.readouterr()
    line = ANSI_ESCAPE_RE.sub("", captured.err).strip()
    assert COMPACT_LOG_LINE_RE.match(line), line


def test_file_log_format_matches_console_format(capfd):
    main()
    capfd.readouterr()
    line = ANSI_ESCAPE_RE.sub("", _read_log_file()).strip()
    assert COMPACT_LOG_LINE_RE.match(line), line


def _read_log_file():
    with open(os.environ["LOG_FILE"], encoding="utf-8") as f:
        return f.read()
