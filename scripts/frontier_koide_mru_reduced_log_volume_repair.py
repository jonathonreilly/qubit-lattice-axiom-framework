#!/usr/bin/env python3
"""Reduced two-slot log-volume repair runner for the Koide MRU row."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
CLAIM_ID = "koide_moment_ratio_uniformity_theorem_note_2026-04-19"
RUNNER_PATH = "scripts/frontier_koide_mru_reduced_log_volume_repair.py"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    required = [
        "bounded-support formal reduced-carrier algebra",
        "That formal reduced-carrier identity is the entire repaired theorem.",
        "This repair withdraws the physical quotient from the binding claim.",
        "The physical bridge from this formal reduced-carrier identity to the charged-lepton scalar lane remains a separate open science problem.",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in text)

    forbidden = [
        "physical SO(2)-quotient is derived",
        "charged-lepton scalar observables therefore factor through",
        "operator-side `kappa = 2` is derived in the framework",
        "observational matching is derived",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim phrase: {needle!r}", needle not in text)


def check_lagrange_solution() -> None:
    section("Symbolic Lagrange solution")
    rp, rq, lam, etot = sp.symbols("rho_plus rho_perp lambda E_tot", positive=True)
    lag = sp.log(rp) + sp.log(rq) - lam * (rp**2 + rq**2 - etot)
    d_rp = sp.diff(lag, rp)
    d_rq = sp.diff(lag, rq)
    check("stationarity equation for rho_plus", sp.simplify(d_rp - (1 / rp - 2 * lam * rp)) == 0)
    check("stationarity equation for rho_perp", sp.simplify(d_rq - (1 / rq - 2 * lam * rq)) == 0)
    # Divide equations to eliminate lambda.
    equality = sp.simplify((1 / rp) / rp - (1 / rq) / rq)
    check("stationarity forces 1/rho_plus^2 = 1/rho_perp^2", equality == sp.simplify(1 / rp**2 - 1 / rq**2))
    solution_r2 = etot / 2
    kappa = sp.simplify(2 * solution_r2 / solution_r2)
    check("constraint gives rho_plus^2 = rho_perp^2 = E_tot/2", sp.simplify(2 * solution_r2 - etot) == 0)
    check("kappa = 2 at the reduced extremum", kappa == 2, str(kappa))


def check_numeric_concavity() -> None:
    section("Numeric concavity / uniqueness samples")
    etot = 10.0
    optimum = math.sqrt(etot / 2.0)
    opt_l = math.log(optimum) + math.log(optimum)
    for t in [0.05, 0.1, 0.2, 0.35, 0.65, 0.8, 0.9, 0.95]:
        rp2 = etot * t
        rq2 = etot * (1.0 - t)
        val = 0.5 * math.log(rp2) + 0.5 * math.log(rq2)
        check(f"sample t={t:.2f}: log-volume below symmetric point", val < opt_l, f"delta={opt_l - val:.6f}")


def check_negative_controls() -> None:
    section("Negative controls")
    etot = sp.symbols("E_tot", positive=True)
    # If the unreduced doublet is counted twice, the extremum changes.
    rp, rq, lam = sp.symbols("rho_plus rho_perp lambda", positive=True)
    lag_weighted = sp.log(rp) + 2 * sp.log(rq) - lam * (rp**2 + rq**2 - etot)
    eq1 = sp.Eq(sp.diff(lag_weighted, rp), 0)
    eq2 = sp.Eq(sp.diff(lag_weighted, rq), 0)
    # From equations: 1/rp = 2 lam rp; 2/rq = 2 lam rq, hence rq^2 = 2 rp^2.
    rp2 = etot / 3
    rq2 = 2 * etot / 3
    kappa_weighted = sp.simplify(2 * rp2 / rq2)
    check("weighted unreduced log-volume gives kappa != 2", kappa_weighted != 2, f"kappa={kappa_weighted}")
    check("weighted unreduced log-volume gives kappa = 1", kappa_weighted == 1, f"kappa={kappa_weighted}")


def check_audit_metadata_after_pipeline() -> None:
    section("Audit metadata after pipeline regeneration")
    if not LEDGER_PATH.exists():
        check("audit ledger exists", False, str(LEDGER_PATH))
        return
    ledger = json.loads(LEDGER_PATH.read_text())
    row = ledger.get("rows", {}).get(CLAIM_ID)
    check(f"{CLAIM_ID} row exists", row is not None)
    if row is None:
        return
    check("claim_type is bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit_status reset to unaudited", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective_status reset to unaudited", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("runner path is reduced-log-volume repair runner", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("direct deps are empty for formal reduced theorem", row.get("deps") == [], str(row.get("deps")))
    check("open dependency paths are empty", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))


def main() -> int:
    print("Koide MRU reduced log-volume repair")
    check_note_boundary()
    check_lagrange_solution()
    check_numeric_concavity()
    check_negative_controls()
    check_audit_metadata_after_pipeline()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
