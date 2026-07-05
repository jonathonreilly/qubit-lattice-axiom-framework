#!/usr/bin/env python3
"""Compatibility wrapper for the renamed minimal-axioms companion runner."""

from __future__ import annotations

import runpy
from pathlib import Path


TARGET = Path(__file__).with_name("audit_companion_minimal_axioms_clean_base_exact.py")


if __name__ == "__main__":
    runpy.run_path(str(TARGET), run_name="__main__")
