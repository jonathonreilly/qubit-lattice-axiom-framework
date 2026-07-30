#!/usr/bin/env python3
"""Cycle 812: test a choice-free mixed-input extension of the W7 response.

This runner is deliberately self-contained.  The seven named historical
primaries are SHA-pinned text/AST evidence only: none is imported or executed.
All physics used below is reimplemented with stdlib exact arithmetic.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Iterable


PROCESS_STARTED = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
COPY_ROOT = ROOT.parent / "born-harness-worktree"
AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200_000
REFERENCE_COMMIT = "596edad4baf851c18cca1432e963655f2839729b"

# Literal, worktree-relative, seven-file packet.  These are tracked copies in
# ../born-harness-worktree and are never imported or executed.
AUDIT_INPUT_PATHS = (
    "../born-harness-worktree/scripts/frontier_cycle749_response_comparison_harness_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle768_response_law_candidate_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle771_prediction_verification_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle774_interference_sector_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle778_norefit_attachment_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle803_decoder_derivation_2026_07_28.py",
    "../born-harness-worktree/scripts/frontier_cycle803_decoder_independent_check_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "ab9b852236f73ec4aecad9287e07a4029309159d956a1cb3043f9238342d6807",
    AUDIT_INPUT_PATHS[1]:
        "7c8771e9494a8ed3eea6f6519b2e29d655123c96b98e0295b5300c1320570c32",
    AUDIT_INPUT_PATHS[2]:
        "6e668efc97a276ce9b0b442cbf7f9eda32c2aa6c722b6f562c5ca4046a4b7ba1",
    AUDIT_INPUT_PATHS[3]:
        "2f5214633abf7bcc715c88a646ded9bd25dc3fdfbfe09785ddd12a551dc18c25",
    AUDIT_INPUT_PATHS[4]:
        "033e6442c01eef32efe20e55b025459aa606b92d1a91a4e48e9f795bc3946181",
    AUDIT_INPUT_PATHS[5]:
        "df3287bd2aa0fdfc3361551894760f04d3ebb60ba6214fe83f005056e8aec0ab",
    AUDIT_INPUT_PATHS[6]:
        "33c3c26c4781efe7ab77eef83ed61a6e25cc72bfde271f52b534342f4d0ff5e8",
}
BLOCKLISTED_MODULES = (
    "frontier_cycle749_response_comparison_harness_2026_07_28",
    "frontier_cycle768_response_law_candidate_2026_07_28",
    "frontier_cycle771_prediction_verification_2026_07_28",
    "frontier_cycle774_interference_sector_2026_07_28",
    "frontier_cycle778_norefit_attachment_2026_07_28",
    "frontier_cycle803_decoder_derivation_2026_07_28",
    "frontier_cycle803_decoder_independent_check_2026_07_28",
)

# This is printed before the tableau is rebuilt or any response outcome is
# evaluated.  It is the conditional value obtained by applying W7's diagonal
# unit kernel to a direction-symmetric six-channel density.
PREREGISTERED_PREDICTION = {
    "conditional_assumption":
        "the 720 operator is canonically a density on W7's six-column space",
    "derived_kernel": "unit diagonal recoil kernel; zero fitted defaults",
    "instrument_response": (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    ),
    "interference_nonzero_cells": 0,
    "strict_package_prediction":
        "UNDEFINED unless the span/embedding gate passes",
}

PASS = 0
FAIL = 0
STDOUT_BYTES = 0


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        return fraction_text(value)
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def emit(line: str) -> None:
    global STDOUT_BYTES
    print(line)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))


def certificate(name: str, passed: bool, detail: object) -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
        prefix = "PASS"
    else:
        FAIL += 1
        prefix = "FAIL"
    emit(
        f"{prefix} {name} :: "
        + json.dumps(
            detail, sort_keys=True, separators=(",", ":"), default=jsonable
        )
    )


def sha256_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


def read_reference_copies() -> dict[str, bytes]:
    return {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}


def line_of_fragment(text: str, fragment: str) -> int:
    offset = text.find(fragment)
    if offset < 0:
        raise ValueError(f"defining fragment absent: {fragment!r}")
    return text.count("\n", 0, offset) + 1


def literal_paths_from_self() -> tuple[str, ...]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    if len(matches) != 1 or not isinstance(matches[0].value, ast.Tuple):
        return ()
    elements = matches[0].value.elts
    if not all(
        isinstance(element, ast.Constant)
        and isinstance(element.value, str)
        for element in elements
    ):
        return ()
    return tuple(element.value for element in elements)


def own_import_firewall() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    imports = tuple(
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    )
    forbidden = tuple(
        name
        for name in imports
        if any(
            name == blocked or name.startswith(blocked + ".")
            for blocked in BLOCKLISTED_MODULES
        )
    )
    loaded = {
        name: name in sys.modules for name in BLOCKLISTED_MODULES
    }
    return {
        "forbidden_static_imports": forbidden,
        "sys_modules": loaded,
        "passed": not forbidden and not any(loaded.values()),
    }


def tracked_copy_status() -> dict[str, object]:
    head = subprocess.run(
        ("git", "-C", str(COPY_ROOT), "rev-parse", "HEAD"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    tracked = {}
    prefix = "../born-harness-worktree/"
    for path in AUDIT_INPUT_PATHS:
        relative = path.removeprefix(prefix)
        result = subprocess.run(
            (
                "git", "-C", str(COPY_ROOT), "ls-files",
                "--error-unmatch", relative,
            ),
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        tracked[path] = result.returncode == 0
    actual_head = head.stdout.strip() if head.returncode == 0 else "ERROR"
    return {
        "actual_copy_commit": actual_head,
        "expected_copy_commit": REFERENCE_COMMIT,
        "commit_match": actual_head == REFERENCE_COMMIT,
        "tracked": tracked,
        "all_tracked": all(tracked.values()),
    }


def defining_code_audit(copies: dict[str, bytes]) -> dict[str, object]:
    texts = {
        path: data.decode("utf-8") for path, data in copies.items()
    }
    citations = (
        (
            AUDIT_INPUT_PATHS[2],
            "return Fraction.from_float(real * real + imaginary * imaginary)",
            "pure amplitude enters as |amplitude|^2",
        ),
        (
            AUDIT_INPUT_PATHS[2],
            "tuple(value / weight for value in matter)",
            "Cycle-771 conditions every column response by branch weight",
        ),
        (
            AUDIT_INPUT_PATHS[3],
            "raw[component][axis] / total",
            "Cycle-774 coherent response is explicitly branch-conditioned",
        ),
        (
            AUDIT_INPUT_PATHS[3],
            "cross_term = coherent_probability - mixture_probability",
            "Cycle-774 defines the interference tensor exactly",
        ),
        (
            AUDIT_INPUT_PATHS[3],
            "(matter,mediator,auxiliary)=(REVERSE[d],d,d)",
            "orthogonal source labels make the W7 interference sector empty",
        ),
        (
            AUDIT_INPUT_PATHS[4],
            "composition_row = add_response_rows(input_rows)",
            "Cycle-778's kernel prediction is additive over identity columns",
        ),
    )
    rows = []
    for path, fragment, meaning in citations:
        rows.append({
            "path": path,
            "line": line_of_fragment(texts[path], fragment),
            "defining_code": fragment,
            "meaning": meaning,
        })
    parsed = {
        path: isinstance(ast.parse(text, filename=path), ast.Module)
        for path, text in texts.items()
    }
    return {
        "citations": tuple(rows),
        "all_ast_parse": all(parsed.values()),
        "ast_parse": parsed,
    }


def source_control_certificate() -> dict[str, object]:
    before = read_reference_copies()
    shas_before = {
        path: sha256_bytes(data) for path, data in before.items()
    }
    defining = defining_code_audit(before)
    tracked = tracked_copy_status()
    firewall_before = own_import_firewall()
    after = read_reference_copies()
    shas_after = {
        path: sha256_bytes(data) for path, data in after.items()
    }
    firewall_after = own_import_firewall()
    literal_paths = literal_paths_from_self()
    passed = (
        len(AUDIT_INPUT_PATHS) == 7
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and shas_before == EXPECTED_SHA256
        and shas_after == EXPECTED_SHA256
        and shas_before == shas_after
        and tracked["commit_match"]
        and tracked["all_tracked"]
        and defining["all_ast_parse"]
        and firewall_before["passed"]
        and firewall_after["passed"]
    )
    return {
        "pass": passed,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "defining_code_audit": defining,
        "literal_paths": literal_paths,
        "reference_copy": tracked,
        "sha256": shas_after,
        "text_ast_only_before": firewall_before,
        "text_ast_only_after": firewall_after,
    }


def main() -> int:
    emit(
        "PREREGISTERED W7 PREDICTION :: "
        + json.dumps(
            PREREGISTERED_PREDICTION,
            sort_keys=True,
            separators=(",", ":"),
            default=jsonable,
        )
    )
    controls = source_control_certificate()
    certificate(
        "CERTIFICATE F source copies, SHA anchors, and BLOCKLIST",
        bool(controls["pass"]),
        controls,
    )
    elapsed = time.monotonic() - PROCESS_STARTED
    emit(f"SCAFFOLD_RUNTIME_SECONDS {elapsed:.6f}")
    return 0 if controls["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
