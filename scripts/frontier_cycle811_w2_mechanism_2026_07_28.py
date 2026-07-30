#!/usr/bin/env python3
"""Cycle 811: the rule-level W2 source-bootstrap mechanism theorem.

The four copied primaries are inert text/AST audit inputs.  The executable
experiment below is a stdlib-only reimplementation of the exact frozen
two-bank gate fixture used by the 752 lineage.  Its transition rules are
expanded into source-emission and clean-return predicates so the certificate
explains the boundary-0 obstruction rather than merely correlating it.
"""
from __future__ import annotations

import ast
import base64
from collections import defaultdict
from hashlib import sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import perf_counter
import zlib


# Literal, existing, worktree-relative, text/AST-only audit inputs.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle783_functional_order_w2_2026_07_28.py",
    "scripts/frontier_cycle806_w2_indistinguishability_2026_07_28.py",
    "scripts/frontier_cycle810_satisfiable_start_discriminator_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    AUDIT_INPUT_PATHS[1]:
        "d773f3ce86d7c7f6fba9d49cddb2e9839f4dce26a30310b7b2bb5568418c94c1",
    AUDIT_INPUT_PATHS[2]:
        "d9a8cb70f3c0a99c112b7ca3e962941f7524dc743c56979ef9d4f6b06fa58c5c",
    AUDIT_INPUT_PATHS[3]:
        "2f39e834f89be02bf40bbe9a0d9cac905dc8f4294096faaa7914cfc31fed26a7",
}
BLOCKED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
ROOT = Path(__file__).resolve().parents[1]
RING_STATIONS = 11
ASSIGNMENTS_PER_START = 1 << RING_STATIONS
EXPECTED_SUCCESS_COUNTS = (512,) + (0,) * 10
RUNTIME_LIMIT_SECONDS = 1200.0
STDOUT_LIMIT_BYTES = 200 * 1024
EXPECTED_FIXTURE_RAW_SHA256 = (
    "3b45537e75b8b1c3157073ff603604b56c9db107511a2d2ab43d4f54ad50ff0c"
)

# The exact frozen 752/719 two-bank fixture will be inserted in the next
# incremental commit.  It contains only integer wire constants and X/CNOT/TOF
# rows, never executable copied-module code.
FROZEN_FIXTURE_B85 = "__CYCLE811_FROZEN_FIXTURE__"


class _CopiedInputBlocker(importlib.abc.MetaPathFinder):
    """Fail closed on executable imports of every copied primary."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in BLOCKED_MODULES:
            raise ImportError(f"{fullname} is text/AST-only in Cycle 811")
        return None


_IMPORT_BLOCKER = _CopiedInputBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def assignment_value(tree: ast.Module, name: str) -> ast.expr:
    matches: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("assignment census", name, len(matches)))
    return matches[0]


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def command_output(arguments: tuple[str, ...]) -> str:
    return subprocess.run(
        arguments,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def decode_fixture() -> dict[str, object]:
    compressed = base64.b85decode(FROZEN_FIXTURE_B85.encode("ascii"))
    raw = zlib.decompress(compressed)
    if sha256(raw).hexdigest() != EXPECTED_FIXTURE_RAW_SHA256:
        raise AssertionError("frozen fixture digest mismatch")
    return json.loads(raw)


Gate = tuple[int, ...]
Word = tuple[Gate, ...]


def apply_gate(state: int, gate: Gate) -> int:
    """Exact Boolean gate update: 0=X, 1=CNOT, 2=TOF."""

    kind, *wires = gate
    if kind == 0:
        return state ^ (1 << wires[0])
    if kind == 1:
        return state ^ (((state >> wires[0]) & 1) << wires[1])
    if kind == 2:
        enabled = (
            ((state >> wires[0]) & 1)
            & ((state >> wires[1]) & 1)
        )
        return state ^ (enabled << wires[2])
    raise AssertionError(("unsupported frozen gate kind", kind))


def apply_word(state: int, word: Word) -> int:
    for gate in word:
        state = apply_gate(state, gate)
    return state


def apply_pair(
    state: int,
    words: tuple[Word, ...],
    first: int,
    second: int,
) -> int:
    return apply_word(apply_word(state, words[first]), words[second])


def bit_signature(state: int, wires: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in wires)


def main() -> int:
    raise SystemExit(
        "incremental scaffold only; frozen fixture and certificates pending"
    )


if __name__ == "__main__":
    raise SystemExit(main())
