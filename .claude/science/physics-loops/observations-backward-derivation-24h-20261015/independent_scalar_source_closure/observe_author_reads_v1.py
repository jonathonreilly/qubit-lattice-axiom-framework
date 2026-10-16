"""Additional observed execution, separate from exact uninstrumented replay.

Observe Python open events within this repository. This is process-level read
evidence, not a general operating-system sandbox or proof about third-party code.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/check_scalar_source_closure_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_PLAN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/SCALAR_SOURCE_CLOSURE_v1.md",
]
import json
import os
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[5]
allowed = {str(ROOT / p) for p in AUDIT_INPUT_PATHS}
events = []

def observe(event, args):
    if event != "open" or not isinstance(args[0], (str, bytes, os.PathLike)):
        return
    path = os.path.abspath(os.fsdecode(args[0]))
    if path == str(ROOT) or path.startswith(str(ROOT) + os.sep):
        mode, flags = args[1], args[2]
        writes = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        row = {"path": os.path.relpath(path, ROOT), "mode": mode, "flags": flags, "write": writes}
        events.append(row)
        if writes or path not in allowed:
            raise RuntimeError("Unexpected repository file access: " + repr(row))

sys.addaudithook(observe)
try:
    runpy.run_path(str(ROOT / AUDIT_INPUT_PATHS[0]), run_name="__main__")
finally:
    print(json.dumps({"observed_repository_open_events": events,
                      "allowed_reads": AUDIT_INPUT_PATHS,
                      "dont_write_bytecode": sys.dont_write_bytecode}, indent=2), file=sys.stderr)
