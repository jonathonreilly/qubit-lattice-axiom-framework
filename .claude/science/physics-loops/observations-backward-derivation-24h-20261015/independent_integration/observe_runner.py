#!/usr/bin/env python3
"""Observe an exact-byte isolated copy of the current author runner.

This writes only inside independent_integration. The snapshot is reproduction
provenance, not another author source, current canonical cache, or audit verdict.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_integration/reproduction_repaired/scripts/scalar_observation_inverse.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_integration/reproduction_repaired/scripts/scalar_observation_inverse_math.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_integration/reproduction_repaired/docs/SCALAR_OBSERVATION_INVERSE_AND_INPUT_BOUNDS_NOTE_2026-10-16.md",
)

import json
import os
from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SNAPSHOT = HERE / "reproduction_repaired"
events = []
runtime_open_count = 0
calls = {}
observing = True


def observe(event, args):
    global runtime_open_count
    if not observing or event != "open" or not isinstance(args[0], (str, bytes, os.PathLike)):
        return
    path = Path(os.fsdecode(args[0])).absolute()
    if path.is_relative_to(ROOT):
        events.append({"path": str(path.relative_to(ROOT)), "mode": args[1], "flags": args[2]})
    else:
        runtime_open_count += 1


def profile(frame, event, arg):
    if event == "call" and frame.f_code.co_filename == str(SNAPSHOT / "scripts/scalar_observation_inverse_math.py"):
        name = frame.f_code.co_name
        calls[name] = calls.get(name, 0) + 1


sys.dont_write_bytecode = True
sys.path.insert(0, str(SNAPSHOT / "scripts"))
sys.addaudithook(observe)
sys.setprofile(profile)
code = 0
try:
    runpy.run_path(str(SNAPSHOT / "scripts/scalar_observation_inverse.py"), run_name="__main__")
except SystemExit as exc:
    code = exc.code if isinstance(exc.code, int) else 1
finally:
    sys.setprofile(None)
    observing = False
    (HERE / "observed_read_closure.json").write_text(json.dumps({
        "scope": "isolated byte-identical author reproduction, not an audit",
        "repository_open_events": events,
        "runtime_open_events_outside_repository": runtime_open_count,
        "helper_function_call_counts": calls,
        "exit_code": code,
        "caveat": "Open audit events include attempted opens; non-repository Python/runtime reads are counted, not scientific inputs.",
    }, indent=2) + "\n")
sys.exit(code)
