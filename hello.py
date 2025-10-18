#!/usr/bin/env python3
"""Simple CLI application that prints a greeting."""

import sys
from typing import Optional, Sequence


def build_greeting(name: Optional[str] = None) -> str:
    """Return a greeting, optionally addressing *name*."""
    if name:
        return f"Hello, {name}!"
    return "Hello, world!"


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Entry point for the greeting CLI."""
    if argv is None:
        argv = sys.argv[1:]

    name = argv[0] if argv else None
    print(build_greeting(name))


if __name__ == "__main__":
    main()
