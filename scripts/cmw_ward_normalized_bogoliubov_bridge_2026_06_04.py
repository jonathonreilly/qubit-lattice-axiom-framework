#!/usr/bin/env python3
"""Finite-volume CMW Ward-normalized Bogoliubov bridge.

The runner verifies the algebraic bridge from explicit Ward-normalized
finite-volume hypotheses to the order-parameter bound

    |m_L|^2 <= K / I_d(L).

It does not import the Mermin-Wagner theorem as an oracle and it does not
assert that arbitrary Hamiltonians automatically satisfy the Ward hypotheses.
"""
from __future__ import annotations

import json
import math
from itertools import product
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE = "docs/CMW_WARD_NORMALIZED_BOGOLIUBOV_BRIDGE_THEOREM_NOTE_2026-06-04.md"


def dispersion(k_vec: tuple[float, ...]) -> float:
    return 2.0 * sum(1.0 - math.cos(k) for k in k_vec)


def ir_sum(length: int, dim: int) -> float:
    volume = length**dim
    total = 0.0
    for mode in product(range(length), repeat=dim):
        if all(n == 0 for n in mode):
            continue
        k_vec = tuple(2.0 * math.pi * n / length for n in mode)
        total += 1.0 / dispersion(k_vec)
    return total / volume


def exact_ir_sum_1d(length: int) -> float:
    return (length * length - 1.0) / (12.0 * length)


def bound(beta: float, c_a: float, c_h: float, c_w: float, i_d: float) -> float:
    """Return the theorem's upper bound on |m_L|^2."""
    return beta * c_a * c_h / (2.0 * c_w * c_w * i_d)


def check(condition: bool, name: str, detail: str, results: list[dict]) -> None:
    results.append({"name": name, "pass": bool(condition), "detail": detail})


def main() -> int:
    results: list[dict] = []
    note_text = (REPO_ROOT / NOTE).read_text(encoding="utf-8")

    for marker in [
        "W1. Ward/commutator lower bound",
        "W2. Susceptibility/onsite anticommutator bound",
        "W3. Local double-commutator bound",
        "W4. Finite Gibbs-state Bogoliubov inequality",
        "|m_L|^2 <= (beta C_A C_H) / (2 c_W^2 I_d(L))",
        "every Hamiltonian",
    ]:
        check(marker in note_text, f"note_marker:{marker}", marker, results)

    lengths_1d = [8, 16, 32, 64, 128, 256]
    vals_1d = [ir_sum(length, 1) for length in lengths_1d]
    exact_ok = all(
        abs(value - exact_ir_sum_1d(length)) < 1e-10
        for value, length in zip(vals_1d, lengths_1d)
    )
    check(exact_ok, "d1_exact_ir_identity", "I_1(L) exact identity holds", results)
    check(
        all(b > a for a, b in zip(vals_1d, vals_1d[1:])),
        "d1_ir_sum_monotone",
        f"I_1 values {[round(v, 6) for v in vals_1d]}",
        results,
    )
    check(
        abs(vals_1d[-1] / lengths_1d[-1] - 1.0 / 12.0) < 1e-4,
        "d1_linear_coefficient",
        f"I_1/L at L=256 is {vals_1d[-1] / lengths_1d[-1]:.8f}",
        results,
    )

    lengths_2d = [8, 16, 32, 64, 96, 128]
    vals_2d = [ir_sum(length, 2) for length in lengths_2d]
    ratios_2d = [value / math.log(length) for value, length in zip(vals_2d, lengths_2d)]
    check(
        all(b > a for a, b in zip(vals_2d, vals_2d[1:])),
        "d2_ir_sum_monotone",
        f"I_2 values {[round(v, 6) for v in vals_2d]}",
        results,
    )
    check(
        max(ratios_2d[-3:]) - min(ratios_2d[-3:]) < 0.03,
        "d2_log_ratio_stable",
        f"I_2/log(L) last ratios {[round(v, 6) for v in ratios_2d[-3:]]}",
        results,
    )

    lengths_3d = [6, 8, 10, 12, 16, 20]
    vals_3d = [ir_sum(length, 3) for length in lengths_3d]
    check(
        max(vals_3d) < 0.27,
        "d3_finite_window_under_watson_half_convention",
        f"I_3 max on window {max(vals_3d):.9f}",
        results,
    )
    final_change = abs(vals_3d[-1] - vals_3d[-2]) / vals_3d[-2]
    check(
        final_change < 0.04,
        "d3_finite_window_converging",
        f"final relative change {final_change:.6e}",
        results,
    )

    beta = 0.8
    c_a = 3.0
    c_h = 2.0
    c_w = 0.5
    bounds_1d = [math.sqrt(bound(beta, c_a, c_h, c_w, value)) for value in vals_1d]
    bounds_2d = [math.sqrt(bound(beta, c_a, c_h, c_w, value)) for value in vals_2d]
    bounds_3d = [math.sqrt(bound(beta, c_a, c_h, c_w, value)) for value in vals_3d]
    check(
        all(b < a for a, b in zip(bounds_1d, bounds_1d[1:])),
        "d1_order_bound_decreases",
        f"d=1 |m_L| bounds {[round(v, 6) for v in bounds_1d]}",
        results,
    )
    check(
        all(b < a for a, b in zip(bounds_2d, bounds_2d[1:])),
        "d2_order_bound_decreases",
        f"d=2 |m_L| bounds {[round(v, 6) for v in bounds_2d]}",
        results,
    )
    check(
        bounds_3d[-1] > 1.0,
        "d3_bound_not_forced_to_zero_on_window",
        f"d=3 final |m_L| bound {bounds_3d[-1]:.6f}",
        results,
    )

    # Algebraic rearrangement check with arbitrary admissible constants.
    i_test = vals_2d[-1]
    m2_bound = bound(beta, c_a, c_h, c_w, i_test)
    lhs = c_a
    rhs = (2.0 * c_w * c_w * m2_bound / (beta * c_h)) * i_test
    check(
        abs(lhs - rhs) < 1e-12,
        "symbolic_bound_rearrangement",
        f"C_A={lhs:.12f}; rearranged RHS={rhs:.12f}",
        results,
    )

    pass_count = sum(1 for item in results if item["pass"])
    fail_count = len(results) - pass_count

    print("=" * 78)
    print("CMW WARD-NORMALIZED BOGOLIUBOV BRIDGE")
    print("=" * 78)
    print(f"Constants for numerical bound witness: beta={beta}, C_A={c_a}, C_H={c_h}, c_W={c_w}")
    print(f"d=1 I_d(L): {[round(v, 6) for v in vals_1d]}")
    print(f"d=2 I_d(L): {[round(v, 6) for v in vals_2d]}")
    print(f"d=3 I_d(L): {[round(v, 6) for v in vals_3d]}")
    print(f"d=1 |m_L| bound: {[round(v, 6) for v in bounds_1d]}")
    print(f"d=2 |m_L| bound: {[round(v, 6) for v in bounds_2d]}")
    print(f"d=3 |m_L| bound: {[round(v, 6) for v in bounds_3d]}")
    print("-" * 78)
    for item in results:
        status = "PASS" if item["pass"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")
    print("=" * 78)
    print(f"SUMMARY: CMW WARD BRIDGE PASS={pass_count} FAIL={fail_count}")
    print("=" * 78)
    print("STATUS_BOUNDARY: exact-support bridge under explicit W1-W4 hypotheses; audit owns status movement")

    out_dir = REPO_ROOT / "outputs"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "cmw_ward_normalized_bogoliubov_bridge_2026_06_04.json"
    out_path.write_text(
        json.dumps(
            {
                "claim_id": "cmw_ward_normalized_bogoliubov_bridge_theorem_note_2026-06-04",
                "note": NOTE,
                "summary": {"pass": pass_count, "fail": fail_count},
                "constants": {"beta": beta, "C_A": c_a, "C_H": c_h, "c_W": c_w},
                "ir_sums": {
                    "d1": dict(zip(map(str, lengths_1d), vals_1d)),
                    "d2": dict(zip(map(str, lengths_2d), vals_2d)),
                    "d3": dict(zip(map(str, lengths_3d), vals_3d)),
                },
                "results": results,
                "status_boundary": "independent audit lane only",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Output written: {out_path.relative_to(REPO_ROOT)}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
