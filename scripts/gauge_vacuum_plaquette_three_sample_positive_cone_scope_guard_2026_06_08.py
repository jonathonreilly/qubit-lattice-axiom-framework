#!/usr/bin/env python3
"""
Scope guard for the first symmetric three-sample positive-cone theorem.

This runner checks the bounded cone theorem without modifying the already
retained local-Wilson parent runner.  It imports that runner only for the
shared exact matrix and beta=6 local-sample utilities.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import frontier_gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_2026_04_17 as base_runner


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}
FAILED_AUDIT_STATUSES = {"audited_failed", "failed", "rejected"}

POSITIVE_CONE_CLAIM = (
    "gauge_vacuum_plaquette_first_symmetric_three_sample_positive_cone_order_witness_note_2026-04-17"
)
RADICAL_MAP_CLAIM = (
    "gauge_vacuum_plaquette_first_symmetric_three_sample_exact_radical_reconstruction_map_note_2026-04-17"
)
CHARACTER_MEASURE_CLAIM = "gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note"
LOCAL_WILSON_CLAIM = (
    "gauge_vacuum_plaquette_first_three_sample_local_wilson_partial_evaluation_note_2026-04-17"
)


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text()


def load_ledger_rows() -> dict[str, dict]:
    ledger = json.loads((ROOT / "docs/audit/data/audit_ledger.json").read_text())
    return ledger["rows"]


def retained_grade(row: dict | None) -> bool:
    return bool(row) and row.get("effective_status") in RETAINED_GRADES


def not_failed(row: dict | None) -> bool:
    return bool(row) and (row.get("audit_status") or "") not in FAILED_AUDIT_STATUSES


def main() -> int:
    cone_note = read(
        "docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SYMMETRIC_THREE_SAMPLE_POSITIVE_CONE_ORDER_WITNESS_NOTE_2026-04-17.md"
    )
    radical_note = read(
        "docs/GAUGE_VACUUM_PLAQUETTE_FIRST_SYMMETRIC_THREE_SAMPLE_EXACT_RADICAL_RECONSTRUCTION_MAP_NOTE_2026-04-17.md"
    )
    character_note = read(
        "docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md"
    )
    local_note = read(
        "docs/GAUGE_VACUUM_PLAQUETTE_FIRST_THREE_SAMPLE_LOCAL_WILSON_PARTIAL_EVALUATION_NOTE_2026-04-17.md"
    )
    rim_note = read(
        "docs/GAUGE_VACUUM_PLAQUETTE_FULL_SLICE_RIM_LIFT_INTEGRAL_BOUNDARY_SCIENCE_ONLY_NOTE_2026-04-17.md"
    )
    rows = load_ledger_rows()

    entries = base_runner.radical_entries()
    f_mat = base_runner.sample_matrix(entries)
    f_inv = sp.simplify(f_mat.inv())
    det_abs = abs(float(sp.N(f_mat.det(), 50)))
    inverse_gap = base_runner.max_abs_complex(sp.N(f_inv * f_mat - sp.eye(3), 100))

    sign_pattern_ok = (
        float(sp.N(entries["a"], 50)) < 0.0
        and float(sp.N(entries["b"], 50)) > 0.0
        and float(sp.N(entries["c"], 50)) > 0.0
        and float(sp.N(entries["d"], 50)) > 0.0
        and float(sp.N(entries["e"], 50)) < 0.0
    )
    order_coeff_ba = float(sp.N(entries["b"] - entries["a"], 50))
    order_coeff_c = float(sp.N(entries["c"], 50))

    z_1plaq, max_mode = base_runner.su3_partition_sum(base_runner.BETA)
    z_loc = sp.Matrix(
        [
            sp.N(sp.exp(entries["a"] / 3) / z_1plaq, 80),
            sp.N(sp.exp(entries["b"] / 3) / z_1plaq, 80),
            sp.N(sp.exp(entries["d"] / 3) / z_1plaq, 80),
        ]
    )
    coeff = sp.N(f_inv * z_loc, 80)
    rec_gap = base_runner.max_abs_complex(sp.N(f_mat * coeff - z_loc, 80))
    coeff_vals = [float(sp.N(val, 50)) for val in coeff]
    sample_vals = [float(sp.N(val, 50)) for val in z_loc]
    order_gap = sample_vals[1] - sample_vals[0]
    repair = -coeff_vals[2]

    dep_rows = {
        RADICAL_MAP_CLAIM: rows.get(RADICAL_MAP_CLAIM),
        CHARACTER_MEASURE_CLAIM: rows.get(CHARACTER_MEASURE_CLAIM),
        LOCAL_WILSON_CLAIM: rows.get(LOCAL_WILSON_CLAIM),
    }

    print("=" * 112)
    print("GAUGE-VACUUM PLAQUETTE THREE-SAMPLE POSITIVE-CONE SCOPE GUARD")
    print("=" * 112)
    print()
    print("Exact first-symmetric radical sample matrix F")
    print(f_mat)
    print()
    print("Inverse half-space map F^(-1), numerical display")
    print(sp.N(f_inv, 12))
    print()
    print("Exact normalized local Wilson one-plaquette sample triple")
    print(f"  Z_loc(W_A)                            = {sample_vals[0]:.15f}")
    print(f"  Z_loc(W_B)                            = {sample_vals[1]:.15f}")
    print(f"  Z_loc(W_C)                            = {sample_vals[2]:.15f}")
    print(f"  Z_(1plaq)(6)                          = {z_1plaq:.15f}   (mode cutoff m = {max_mode})")
    print()
    print("Reconstructed local coordinates a_loc = F^(-1) Z_loc")
    print(f"  a_loc_(0,0)                           = {coeff_vals[0]:.15f}")
    print(f"  a_loc_(1,0)                           = {coeff_vals[1]:.15f}")
    print(f"  a_loc_(1,1)                           = {coeff_vals[2]:.15f}")
    print(f"  reconstruction gap                    = {rec_gap:.3e}")
    print(f"  |det(F)|                              = {det_abs:.12f}")
    print(f"  local order gap Z_loc(W_B)-Z_loc(W_A) = {order_gap:.15f}")
    print(f"  minimal adjoint-channel repair        = {repair:.15f}")
    print()

    check(
        "Source note is narrowed to a bounded finite-packet cone theorem, not a full Wilson identification",
        "bounded finite-packet positive-cone theorem" in cone_note
        and "does **not** identify the supplied triple" in cone_note
        and "not an identification" in cone_note
        and "actual full Wilson spatial-environment" in cone_note,
        bucket="SUPPORT",
    )
    check(
        "Source note records the local Wilson obstruction without promoting it to an actual-environment identification",
        "negative reconstructed" in cone_note
        and "adjoint coordinate" in cone_note
        and "finite-packet positive cone" in cone_note
        and "actual Wilson environment" in cone_note
        and "positive adjoint-channel correction" in cone_note
        and "cone theorem" in cone_note,
        bucket="SUPPORT",
    )
    check(
        "Source note does not carry stale retained-cone overclaim language",
        "positivity of the retained character data already forces the first symmetric retained sample triple"
        not in cone_note
        and "already forces the first symmetric retained sample triple" not in cone_note
        and "retained profile obeys" not in cone_note
        and "retained positive cone" not in cone_note
        and "sole-axiom PF selector" not in cone_note,
        bucket="SUPPORT",
    )
    check(
        "Support notes fix the exact radical map, finite character packet, local samples, and open full-slice beta=6 problem",
        "exact radical-form sample matrix" in radical_note
        and "exact algebraic inverse map" in radical_note
        and "positive finite coefficients" in character_note
        and "w_6(W_A) / Z_(1plaq)(6) = 0.1351652795620484" in local_note
        and "w_6(W_B) / Z_(1plaq)(6) = 0.3170224955005416" in local_note
        and "w_6(W_C) / Z_(1plaq)(6) = 0.5812139466746343" in local_note
        and "What remains open is the explicit `beta = 6` evaluation problem." in rim_note,
        bucket="SUPPORT",
    )
    check(
        "Load-bearing parents are retained-grade without requiring stale exact audit-status labels",
        all(retained_grade(row) and not_failed(row) for row in dep_rows.values()),
        detail=", ".join(
            f"{claim_id}: effective={row.get('effective_status') if row else None}, "
            f"audit={row.get('audit_status') if row else None}"
            for claim_id, row in dep_rows.items()
        ),
        bucket="SUPPORT",
    )

    check(
        "The radical sample matrix is exactly invertible and the displayed inverse is internally consistent",
        det_abs > 1.0 and inverse_gap < 1.0e-75,
        detail=f"|det(F)|={det_abs:.12f}, max |F^(-1)F-I|={inverse_gap:.3e}",
    )
    check(
        "The radical entries have the sign pattern needed for cone and order statements",
        sign_pattern_ok and order_coeff_ba > 0.0 and order_coeff_c > 0.0,
        detail=(
            f"b-a={order_coeff_ba:.15f}, c={order_coeff_c:.15f}; "
            "a<0, b>0, c>0, d>0, e<0"
        ),
    )
    check(
        "Nonnegative supplied first-sector coefficients are equivalent to the half-space test F^(-1)Z >= 0",
        det_abs > 1.0 and inverse_gap < 1.0e-75,
        detail="Z=F a_vec with det(F)!=0, so componentwise a_vec>=0 iff componentwise F^(-1)Z>=0",
    )
    check(
        "The exact order witness Z_B-Z_A=(b-a)a_(1,0)+c a_(1,1) is nonnegative on the supplied positive cone",
        order_coeff_ba > 0.0 and order_coeff_c > 0.0,
        detail=f"b-a={order_coeff_ba:.15f}, c={order_coeff_c:.15f}",
    )
    check(
        "The exact local Wilson sample triple reconstructs uniquely but lies outside the supplied positive cone",
        rec_gap < 1.0e-75
        and coeff_vals[0] > 1.0e-12
        and coeff_vals[1] > 1.0e-12
        and coeff_vals[2] < -1.0e-12,
        detail=(
            f"a_loc=( {coeff_vals[0]:.15f}, {coeff_vals[1]:.15f}, {coeff_vals[2]:.15f} ); "
            f"max |F a_loc-Z_loc|={rec_gap:.3e}"
        ),
    )
    check(
        "The local obstruction is sharper than the coarse order witness and requires a positive adjoint-channel correction",
        order_gap > 1.0e-12 and repair > 1.0e-12,
        detail=f"order gap={order_gap:.15f}, minimal adjoint-channel repair={repair:.15f}",
    )

    print()
    print(f"THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
