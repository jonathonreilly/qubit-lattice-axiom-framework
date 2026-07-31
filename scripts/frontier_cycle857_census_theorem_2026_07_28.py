#!/usr/bin/env python3
"""Cycle 857: census theorem and exact initial-selection bit accounting.

The Cycle-719 core is a SHA-pinned text/AST-only primary.  This runner never
imports or executes it.  Instead it independently rebuilds the two-bank
geometry, proves the circular-gap counting law, enumerates every admissible
setup, and audits the information needed to select one setup.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

from hashlib import sha1, sha256
import ast
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockF22-20260729"
EXPECTED_PARENT_HEAD = "db6bb28220ec173bc85de540022a9ef3f58e2375"
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited source primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def run() -> int:
    started = monotonic()
    report = {
        "cycle": 857,
        "status": "INCREMENTAL_SCAFFOLD",
        "runtime_seconds": round(monotonic() - started, 6),
        "pass": False,
    }
    sys.stdout.write("FAIL D_CONTROLS :: " + compact(report) + "\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(run())
