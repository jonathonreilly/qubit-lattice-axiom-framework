#!/usr/bin/env python3
"""Trace-form rigidity check for the narrowed g_bare rigidity row.

This runner checks only finite-dimensional algebra on the retained structural
SU(3) carrier. It does not derive a lattice holonomy, does not assert
g_bare = 1, and does not apply an audit verdict.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    msg = f"[{tag}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return cond


def ledger_rows() -> dict:
    ledger = (
        Path(__file__).resolve().parent.parent
        / "docs"
        / "audit"
        / "data"
        / "audit_ledger.json"
    )
    return json.loads(ledger.read_text())["rows"]


def gellmann_generators() -> list[np.ndarray]:
    lambdas = [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex)
        / np.sqrt(3),
    ]
    return [lam / 2 for lam in lambdas]


def gram(gens: list[np.ndarray]) -> np.ndarray:
    n = len(gens)
    out = np.zeros((n, n), dtype=float)
    for i, a in enumerate(gens):
        for j, b in enumerate(gens):
            out[i, j] = np.trace(a @ b).real
    return out


def random_orthogonal(n: int, seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def main() -> int:
    rows = ledger_rows()
    deps = [
        "graph_first_su3_integration_note",
        "native_gauge_closure_note",
    ]
    target_id = "g_bare_rigidity_theorem_note"

    for dep in deps:
        check(
            f"dependency {dep} is retained",
            rows.get(dep, {}).get("effective_status") == "retained",
            f"effective_status = {rows.get(dep, {}).get('effective_status', 'missing')}",
        )

    gens = gellmann_generators()
    target = 0.5 * np.eye(8)
    base_gram = gram(gens)
    check(
        "canonical Gram is delta_ab / 2",
        np.linalg.norm(base_gram - target) < 1e-12,
        f"max deviation = {np.max(np.abs(base_gram - target)):.2e}",
    )

    q = random_orthogonal(8)
    rotated = [sum(q[i, j] * gens[j] for j in range(8)) for i in range(8)]
    rotated_gram = gram(rotated)
    check(
        "orthogonal basis rotation preserves Gram",
        np.linalg.norm(rotated_gram - target) < 1e-12,
        f"max deviation = {np.max(np.abs(rotated_gram - target)):.2e}",
    )

    for scale in [0.5, 1.2, 2.0]:
        scaled = [scale * gen for gen in gens]
        scaled_gram = gram(scaled)
        expected = (scale**2) * target
        check(
            f"scalar dilation {scale:g} gives lambda^2 Gram",
            np.linalg.norm(scaled_gram - expected) < 1e-12,
            f"lambda^2 = {scale**2:.6g}",
        )
        check(
            f"scalar dilation {scale:g} does not preserve canonical Gram",
            np.linalg.norm(scaled_gram - target) > 1e-6,
            "canonical Gram would require lambda^2 = 1",
        )

    target_row = rows.get(target_id, {})
    target_deps = set(target_row.get("deps", []))
    check(
        "target row declares both retained structural SU(3) dependencies",
        set(deps).issubset(target_deps),
        f"deps = {sorted(target_deps)}",
    )
    check(
        "target row has no holonomy/g_bare dependency edge",
        "g_bare_derivation_note" not in target_deps
        and "g_bare_rescaling_freedom_removal_theorem_note_2026-05-03" not in target_deps
        and "g_bare_constraint_vs_convention_theorem_note_2026-05-03" not in target_deps,
        f"deps = {sorted(target_deps)}",
    )

    print(
        "INFO target audit routing: "
        f"audit_status = {target_row.get('audit_status', 'missing')}; "
        f"effective_status = {target_row.get('effective_status', 'missing')}"
    )
    print(f"SUMMARY: PASS = {PASS}, FAIL = {FAIL}")
    if FAIL:
        print("Trace-form rigidity check failed.")
        return 1

    print("Trace-form rigidity check passed; no retained status is asserted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
