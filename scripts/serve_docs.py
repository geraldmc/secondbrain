#!/usr/bin/env python3
"""Serve MkDocs with output captured to mkdocs.log."""

import subprocess
import sys


def main():
    proc = subprocess.Popen(
        [sys.executable, "-m", "mkdocs", "serve"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    try:
        with open("mkdocs.log", "w") as log:
            for line in proc.stdout:
                print(line, end="", flush=True)
                log.write(line)
                log.flush()
    except KeyboardInterrupt:
        proc.terminate()


if __name__ == "__main__":
    main()
