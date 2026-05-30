#!/usr/bin/env python3
"""Scale-free chiral U(1) cubic trace surface for the ABJ route.

The 3+1 anomaly-forces-time proof does not need physical hypercharge
normalization, GMN, electron charge, or quark/lepton naming.  It only needs a
nonzero cubic chiral U(1) trace on the retained graph-first selected-axis
surface.  This runner verifies that statement exactly.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
NOTE = ROOT / "docs" / "ABJ_SCALE_FREE_CHIRAL_U1_TRACE_SURFACE_THEOREM_NOTE_2026-05-30.md"
OUTPUT = ROOT / "outputs" / "abj_scale_free_chiral_u1_trace_surface_2026-05-30.json"

PASS = 0
FAIL = 0
CHECKS: list[dict[str, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    CHECKS.append({"name": name, "status": status, "detail": detail})
    print(f"[{status}] {name}" + (f"  {detail}" if detail else ""))


def state_index(bits: tuple[int, int, int]) -> int:
    x, y, z = bits
    return 4 * x + 2 * y + z


def cube_basis() -> list[tuple[int, int, int]]:
    return [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]


def residual_swap(axis: int) -> sp.Matrix:
    basis = cube_basis()
    index = {bits: state_index(bits) for bits in basis}
    others = [i for i in range(3) if i != axis]
    a, b = others
    mat = sp.zeros(8, 8)
    for bits in basis:
        swapped = list(bits)
        swapped[a], swapped[b] = swapped[b], swapped[a]
        mat[index[tuple(swapped)], index[bits]] = 1
    return mat


def verify_dependencies() -> None:
    rows = json.loads(LEDGER.read_text())["rows"]
    required = {
        "graph_first_selector_derivation_note": "scripts/frontier_graph_first_selector_derivation.py",
        "graph_first_su3_integration_note": "scripts/frontier_graph_first_su3_integration.py",
    }
    for claim_id, runner in required.items():
        row = rows[claim_id]
        check(f"{claim_id} is positive_theorem", row.get("claim_type") == "positive_theorem", str(row.get("claim_type")))
        check(f"{claim_id} is audited_clean", row.get("audit_status") == "audited_clean", str(row.get("audit_status")))
        check(f"{claim_id} is retained effective status", row.get("effective_status") == "retained", str(row.get("effective_status")))
        check(f"{claim_id} runner registered", row.get("runner_path") == runner, str(row.get("runner_path")))
        check(f"{claim_id} runner exists", (ROOT / runner).exists())


def verify_source_firewall() -> None:
    text = NOTE.read_text()
    required = [
        "**Claim type:** positive_theorem",
        "scale-free",
        "Y0 = P_+ - 3 P_-",
        "Tr[Y0^3] = -48",
        "No `alpha = 1/3`",
        "No GMN",
        "No electron-charge",
        "No physical-SM hypercharge",
    ]
    forbidden = [
        "**Claim type:** bounded_theorem",
        "Q(e_L) = -1",
        "T_3(e_L)",
        "Gell-Mann-Nishijima convention",
        "PDG",
        "observed target",
        "Monte Carlo measurement input",
    ]
    for phrase in required:
        check(f"source contains required firewall phrase: {phrase}", phrase in text)
    for phrase in forbidden:
        check(f"source excludes forbidden bounded/observed phrase: {phrase}", phrase not in text)


def matrix_equal(a: sp.Matrix, b: sp.Matrix) -> bool:
    return all(sp.simplify((a - b)[i, j]) == 0 for i in range(a.rows) for j in range(a.cols))


def verify_axis(axis: int) -> dict[str, str]:
    tau = residual_swap(axis)
    ident = sp.eye(8)
    zero = sp.zeros(8, 8)
    p_plus = (ident + tau) / 2
    p_minus = (ident - tau) / 2
    y0 = p_plus - 3 * p_minus
    lam = sp.symbols("lambda")

    check(f"axis {axis}: tau^2 = I", matrix_equal(tau * tau, ident))
    check(f"axis {axis}: P_+ projector", matrix_equal(p_plus * p_plus, p_plus))
    check(f"axis {axis}: P_- projector", matrix_equal(p_minus * p_minus, p_minus))
    check(f"axis {axis}: P_+ P_- = 0", matrix_equal(p_plus * p_minus, zero))
    check(f"axis {axis}: rank/trace P_+ = 6", sp.simplify(p_plus.trace()) == 6, str(p_plus.trace()))
    check(f"axis {axis}: rank/trace P_- = 2", sp.simplify(p_minus.trace()) == 2, str(p_minus.trace()))
    check(f"axis {axis}: Y0 Hermitian/symmetric", matrix_equal(y0.T, y0))
    check(f"axis {axis}: Tr[Y0] = 0", sp.simplify(y0.trace()) == 0, str(y0.trace()))
    check(f"axis {axis}: Y0 P_+ = +P_+", matrix_equal(y0 * p_plus, p_plus))
    check(f"axis {axis}: Y0 P_- = -3 P_-", matrix_equal(y0 * p_minus, -3 * p_minus))

    eigs = y0.eigenvals()
    check(f"axis {axis}: eigenvalue +1 multiplicity 6", eigs.get(sp.Integer(1)) == 6, str(eigs))
    check(f"axis {axis}: eigenvalue -3 multiplicity 2", eigs.get(sp.Integer(-3)) == 2, str(eigs))
    tr_y0_2 = sp.simplify((y0 * y0).trace())
    tr_y0_3 = sp.simplify((y0 * y0 * y0).trace())
    check(f"axis {axis}: Tr[Y0^2] = 24", tr_y0_2 == 24, str(tr_y0_2))
    check(f"axis {axis}: Tr[Y0^3] = -48", tr_y0_3 == -48, str(tr_y0_3))
    scaled_cubic = sp.simplify(((lam * y0) ** 3).trace())
    check(f"axis {axis}: Tr[(lambda Y0)^3] = -48 lambda^3", scaled_cubic == -48 * lam**3, str(scaled_cubic))
    check(f"axis {axis}: nonzero cubic trace for nonzero scale", sp.factor(scaled_cubic) == -48 * lam**3)
    y_sm_scale = y0 / 3
    tr_scaled = sp.simplify((y_sm_scale**3).trace())
    check(f"axis {axis}: optional 1/3 rescale gives -16/9", tr_scaled == sp.Rational(-16, 9), str(tr_scaled))
    return {
        "axis": str(axis),
        "trace_y0": str(y0.trace()),
        "trace_y0_squared": str(tr_y0_2),
        "trace_y0_cubed": str(tr_y0_3),
        "trace_lambda_y0_cubed": str(scaled_cubic),
        "eigenvalues": {str(k): str(v) for k, v in eigs.items()},
    }


def main() -> int:
    print("ABJ SCALE-FREE CHIRAL U(1) TRACE SURFACE")
    verify_source_firewall()
    verify_dependencies()
    axis_results = [verify_axis(axis) for axis in range(3)]
    out = {
        "claim": "scale-free chiral U(1) cubic trace surface",
        "pass": PASS,
        "fail": FAIL,
        "checks": CHECKS,
        "axis_results": axis_results,
        "verdict": "nonzero cubic trace follows from retained selected-axis 6+2 surface without alpha=1/3 or physical hypercharge naming",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("VERDICT:", out["verdict"])
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
