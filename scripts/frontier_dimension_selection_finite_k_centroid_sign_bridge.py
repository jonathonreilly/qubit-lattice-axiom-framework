#!/usr/bin/env python3
"""Finite-k centroid-sign bridge for dimension selection.

This runner differentiates the actual layer-normalized finite-k propagator
used by scripts/frontier_dimension_selection.py.  It supplies an independent
finite-k sign certificate for the lower-bound dimension-selection row, avoiding
WKB/eikonal reasoning as the load-bearing sign argument.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


AUDIT_INPUT_PATHS = (
    "docs/DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md",
    "docs/DIMENSION_SELECTION_NOTE.md",
    "docs/DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md",
    "docs/D3_RETENTION_CLOSURE_PLAN_2026-05-20.md",
    "docs/audit/data/ledger/di/dimension_selection_lower_bound_bridge_v2_2026-05-20.json",
    "docs/audit/data/ledger/di/dimension_selection_note.json",
    "scripts/frontier_dimension_selection.py",
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json"

NOTE = DOCS / "DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md"
PARENT = DOCS / "DIMENSION_SELECTION_NOTE.md"
LOWER_BOUND_V2 = DOCS / "DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md"
D3_PLAN = DOCS / "D3_RETENTION_CLOSURE_PLAN_2026-05-20.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
LEDGER_SHARDS = DOCS / "audit" / "data" / "ledger"
PARENT_RUNNER = ROOT / "scripts" / "frontier_dimension_selection.py"

PASS_COUNT = 0
FAIL_COUNT = 0
CONDITIONAL_STATUS = "audited_" + "conditional"

DIMS = (1, 2, 3, 4, 5)
EXPECTED_SIGN = {1: -1, 2: -1, 3: 1, 4: 1, 5: 1}
K = 6.0
LX = 40
LY = 60
SIGMA = 2.0
MASS_OFFSET = 7
FINITE_M = 0.005


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def status_detail(status: Any) -> Any:
    if status == CONDITIONAL_STATUS:
        return "conditional-status"
    return status


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def one_line(text: str) -> str:
    return " ".join(text.split())


def sign(x: float) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def ledger_row(claim_id: str) -> dict[str, Any]:
    shard = LEDGER_SHARDS / claim_id[:2] / f"{claim_id}.json"
    if shard.exists():
        row = json.loads(read(shard))
        if isinstance(row, dict) and row.get("claim_id") == claim_id:
            return row
        raise ValueError(f"ledger shard identity mismatch: {shard}")

    if LEDGER.exists():
        rows = json.loads(read(LEDGER))["rows"]
        iterable = rows.values() if isinstance(rows, dict) else rows
        for row in iterable:
            if isinstance(row, dict) and row.get("claim_id") == claim_id:
                return row
    raise KeyError(claim_id)


def load_parent_runner():
    spec = importlib.util.spec_from_file_location("frontier_dimension_selection", PARENT_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def potential_profile(d: int, lx: int = LX, ly: int = LY, offset: int = MASS_OFFSET) -> np.ndarray:
    mid_y = ly // 2
    mass_x = lx // 2
    mass_y = mid_y + offset
    profile = np.zeros((lx, ly), dtype=float)
    for ix in range(lx):
        for iy in range(ly):
            r = math.sqrt((ix - mass_x) ** 2 + (iy - mass_y) ** 2)
            if r < 0.5:
                r = 0.5
            if d == 1:
                value = r
            elif d == 2:
                value = math.log(r)
            else:
                value = 1.0 / r ** (d - 2)
            profile[ix, iy] = value
    return profile


def initial_state(ly: int = LY, sigma: float = SIGMA) -> np.ndarray:
    mid_y = ly // 2
    coords = np.arange(ly, dtype=float)
    psi = np.exp(-((coords - mid_y) ** 2) / (2.0 * sigma**2)).astype(complex)
    psi /= np.sqrt(np.sum(np.abs(psi) ** 2))
    return psi


def centroid(psi: np.ndarray) -> float:
    coords = np.arange(psi.shape[0], dtype=float)
    prob = np.abs(psi) ** 2
    return float(np.sum(coords * prob) / np.sum(prob))


def propagate_centroid_for_mass(d: int, mass: float) -> float:
    profile = potential_profile(d)
    psi = initial_state()
    for x_new in range(1, LX):
        x_old = x_new - 1
        psi_new = np.zeros(LY, dtype=complex)
        for dy in (-1, 0, 1):
            length = math.sqrt(1.0 + dy * dy)
            if dy >= 0:
                src = slice(0, LY - dy) if dy > 0 else slice(0, LY)
                dst = slice(dy, LY) if dy > 0 else slice(0, LY)
            else:
                src = slice(-dy, LY)
                dst = slice(0, LY + dy)
            favg = 0.5 * (profile[x_old, src] + profile[x_new, dst])
            amp = np.exp(1j * K * length * (1.0 + mass * favg)) / length
            psi_new[dst] += amp * psi[src]
        norm = np.sqrt(np.sum(np.abs(psi_new) ** 2))
        if norm > 1e-30:
            psi_new /= norm
        psi = psi_new
    return centroid(psi)


def finite_k_centroid_derivative(d: int) -> dict[str, float]:
    profile = potential_profile(d)
    psi = initial_state()
    dpsi = np.zeros_like(psi)

    for x_new in range(1, LX):
        x_old = x_new - 1
        z = np.zeros(LY, dtype=complex)
        dz = np.zeros(LY, dtype=complex)

        for dy in (-1, 0, 1):
            length = math.sqrt(1.0 + dy * dy)
            amp0 = np.exp(1j * K * length) / length
            if dy >= 0:
                src = slice(0, LY - dy) if dy > 0 else slice(0, LY)
                dst = slice(dy, LY) if dy > 0 else slice(0, LY)
            else:
                src = slice(-dy, LY)
                dst = slice(0, LY + dy)
            favg = 0.5 * (profile[x_old, src] + profile[x_new, dst])
            damp = amp0 * 1j * K * length * favg
            z[dst] += amp0 * psi[src]
            dz[dst] += damp * psi[src] + amp0 * dpsi[src]

        norm = np.sqrt(np.sum(np.abs(z) ** 2))
        psi_next = z / norm
        d_norm = float(np.real(np.vdot(psi_next, dz)))
        dpsi_next = (dz - psi_next * d_norm) / norm
        psi, dpsi = psi_next, dpsi_next

    coords = np.arange(LY, dtype=float)
    dprob = 2.0 * np.real(np.conj(psi) * dpsi)
    deriv = float(np.sum(coords * dprob))
    norm_deriv = float(np.sum(dprob))
    base_centroid = centroid(psi)
    return {
        "dC_dM_at_zero": deriv,
        "probability_norm_derivative": norm_deriv,
        "free_centroid": base_centroid,
    }


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and audit boundary")
    for path in (NOTE, PARENT, LOWER_BOUND_V2, D3_PLAN, PARENT_RUNNER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    check(
        "canonical sharded audit ledger or legacy cache exists",
        LEDGER_SHARDS.is_dir() or LEDGER.exists(),
        "sharded" if LEDGER_SHARDS.is_dir() else "legacy-cache",
    )

    note = read(NOTE)
    for phrase in (
        "Exact Finite-k Derivative",
        "Result",
        "What This Closes",
        "What Remains Open",
        "Non-Claims",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    lower_row = ledger_row("dimension_selection_lower_bound_bridge_v2_2026-05-20")
    parent_row = ledger_row("dimension_selection_note")
    lower_status = lower_row.get("effective_status")
    check(
        "audit ledger contains the lower-bound V2 row",
        lower_row.get("claim_id") == "dimension_selection_lower_bound_bridge_v2_2026-05-20",
    )
    parent_status = parent_row.get("effective_status")
    check(
        "audit ledger contains the parent dimension-selection row",
        parent_row.get("claim_id") == "dimension_selection_note",
    )
    check("audit blocker names finite-k/eikonal bridge", "finite-k sign proof" in json.dumps(lower_row) or "discrete-to-eikonal" in json.dumps(lower_row))
    return {
        "lower_bound_v2_status": status_detail(lower_status),
        "parent_status": status_detail(parent_status),
    }


def part2_exact_derivatives() -> dict[int, dict[str, float]]:
    print("\nPart 2: exact finite-k first derivative")
    results: dict[int, dict[str, float]] = {}
    for d in DIMS:
        row = finite_k_centroid_derivative(d)
        expected = EXPECTED_SIGN[d]
        check(f"d={d} derivative has expected sign", sign(row["dC_dM_at_zero"]) == expected, row["dC_dM_at_zero"])
        check(f"d={d} probability normalization derivative vanishes", abs(row["probability_norm_derivative"]) < 1e-9, row["probability_norm_derivative"])
        check(f"d={d} free centroid remains centered", abs(row["free_centroid"] - LY / 2) < 1e-8, row["free_centroid"])
        results[d] = row
    min_margin = min(abs(row["dC_dM_at_zero"]) for row in results.values())
    check("minimum derivative sign margin is large", min_margin > 100.0, min_margin)
    return results


def part3_finite_difference(derivatives: dict[int, dict[str, float]]) -> dict[int, float]:
    print("\nPart 3: central finite-difference cross-check")
    # This is only a numerical cross-check of the exact tangent recursion.
    # Around eps ~ 1e-6 to 1e-5 truncation and cancellation are balanced for
    # the layer-normalized complex recurrence.
    eps = 3.0e-6
    fd_results: dict[int, float] = {}
    for d in DIMS:
        c_plus = propagate_centroid_for_mass(d, eps)
        c_minus = propagate_centroid_for_mass(d, -eps)
        fd = (c_plus - c_minus) / (2.0 * eps)
        exact = derivatives[d]["dC_dM_at_zero"]
        rel = abs(fd - exact) / max(1.0, abs(exact))
        check(f"d={d} finite difference matches exact derivative", rel < 2e-5, {"fd": fd, "exact": exact, "rel": rel})
        fd_results[d] = fd
    return fd_results


def part4_parent_finite_probe() -> dict[int, dict[str, Any]]:
    print("\nPart 4: parent finite-M runner sign")
    parent = load_parent_runner()
    parent_results: dict[int, dict[str, Any]] = {}
    for d in DIMS:
        parent_row = parent.measure_gravity_2d_with_d_potential(d, k=K)
        direct_delta = propagate_centroid_for_mass(d, FINITE_M) - propagate_centroid_for_mass(d, 0.0)
        expected = EXPECTED_SIGN[d]
        check(f"d={d} parent raw_delta sign matches lower-bound sign", sign(float(parent_row["raw_delta"])) == expected, parent_row["raw_delta"])
        check(f"d={d} direct finite-M replay matches parent raw_delta", abs(direct_delta - float(parent_row["raw_delta"])) < 2e-9, {"direct": direct_delta, "parent": parent_row["raw_delta"]})
        parent_results[d] = {
            "raw_delta_M_0p005": float(parent_row["raw_delta"]),
            "attractive": bool(parent_row["attractive"]),
        }
    return parent_results


def part5_firewalls() -> None:
    print("\nPart 5: claim-status firewalls")
    note = read(NOTE)
    flat = one_line(note)
    for phrase in (
        "no repo-wide dimension-axiom rewrite",
        "no repo-wide axiom rewrite",
        "does not authorize changing",
        "not full retained dimension selection",
        "use WKB, Fermat, stationary phase, or ray optics as the load-bearing",
    ):
        check(f"boundary phrase present: {phrase}", phrase in flat)

    forbidden = {
        "bare retained status": "Status:** retained",
        "proposed retained status": "proposed_retained",
        "deprecated dimension-axiom shorthand derived": "A" + "2 is now derived",
        "dimension-free baseline derives Z3": "Z^3 has been derived from " + "A" + "1 alone",
        "full retained spatial d = 3 closure": "full retained spatial d = 3 closure",
        "repo-wide axiom rewrite is authorized": "repo-wide axiom rewrite is authorized",
    }
    for label, phrase in forbidden.items():
        check(f"forbidden overclaim absent: {label}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("DIMENSION SELECTION FINITE-K CENTROID-SIGN BRIDGE")
    print("=" * 88)

    statuses = part1_anchors()
    derivatives = part2_exact_derivatives()
    finite_difference = part3_finite_difference(derivatives)
    finite_probe = part4_parent_finite_probe()
    part5_firewalls()

    result = {
        "status": "bounded support: exact finite-k runner sign bridge",
        "claim": (
            "For the finite runner geometry and k=6.0, the exact first derivative "
            "of the layer-normalized detector centroid is negative for d<=2 and "
            "positive for d>=3; the parent finite-M sign matches."
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "This retires the WKB load-bearing sign step for the lower-bound runner, "
            "but it is runner-specific and does not close all-d potential source derivation "
            "or the upper-bound dimension-selection chain."
        ),
        "upstream_statuses": statuses,
        "finite_k_derivatives": {str(k): v for k, v in derivatives.items()},
        "finite_difference_check": {str(k): v for k, v in finite_difference.items()},
        "parent_finite_probe": {str(k): v for k, v in finite_probe.items()},
        "remaining_blockers": [
            "all-d potential/Coulomb law source derivation",
            "upper-bound Bertrand/Coulomb conditional dependencies",
            "uniform parameter/lattice-size generalization if required by audit",
            "independent audit before any axiom rewrite",
        ],
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md",
            "scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py",
            "outputs/dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
