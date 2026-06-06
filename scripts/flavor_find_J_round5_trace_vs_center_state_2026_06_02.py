#!/usr/bin/env python3
"""Repaired J-hunt round 5 central-state certificate.

The previous packet used E(A)=e0 A e0 + e1 A e1 as if it were a
center-valued conditional expectation. It is not: for a general 3x3 operator
the e1 block may still fail to commute with C. This runner keeps the useful
finite algebra and makes the status boundary explicit:

* the C3 central idempotents have ranks 1 and 2;
* trace and equal-central-block states are both positive C3-invariant states;
* the equal-block state is C3-compatible and is not a continuous U(1)_b
  rephasing move;
* the finite C3 packet alone does not force either central-block weighting.

The Q(r) arithmetic is checked only as the local displayed readout convention.
This runner does not derive the physical Q readout or select p0=1/2.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "outputs" / "flavor_find_J_round5_trace_vs_center_state_2026_06_02.json"
TOL = 1e-10


def check(name: str, cond: bool, detail: str = "", results: list[dict] | None = None) -> bool:
    passed = bool(cond)
    print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    if results is not None:
        results.append({"name": name, "pass": passed, "detail": detail})
    return passed


def is_close(a: np.ndarray | float, b: np.ndarray | float, tol: float = TOL) -> bool:
    return bool(np.allclose(a, b, atol=tol, rtol=0.0))


def min_eigenvalue(a: np.ndarray) -> float:
    return float(np.min(np.linalg.eigvalsh((a + a.T) / 2.0)))


C = np.array(
    [
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]
)
I3 = np.eye(3)
C2 = C @ C
E0 = (I3 + C + C2) / 3.0
E1 = I3 - E0


def block_compression(a: np.ndarray) -> np.ndarray:
    return E0 @ a @ E0 + E1 @ a @ E1


def c3_average(a: np.ndarray) -> np.ndarray:
    return (a + C @ a @ C.T + C2 @ a @ C2.T) / 3.0


def block_trace(a: np.ndarray, p: np.ndarray) -> float:
    return float(np.trace(p @ a @ p) / np.trace(p))


def center_valued_average(a: np.ndarray) -> np.ndarray:
    return block_trace(a, E0) * E0 + block_trace(a, E1) * E1


def central_state_density(p0: float) -> np.ndarray:
    p1 = 1.0 - p0
    return p0 * E0 / np.trace(E0) + p1 * E1 / np.trace(E1)


def state_value(a: np.ndarray, p0: float) -> float:
    rho = central_state_density(p0)
    return float(np.trace(rho @ a))


def q_of_r(r: float) -> float:
    return 1.0 / 3.0 + 2.0 * r / 3.0


def main() -> int:
    results: list[dict] = []

    check(
        "R5-1 central idempotents close with ranks 1 and 2",
        is_close(E0 @ E0, E0)
        and is_close(E1 @ E1, E1)
        and is_close(E0 @ E1, np.zeros((3, 3)))
        and is_close(E0 + E1, I3)
        and is_close(np.trace(E0), 1.0)
        and is_close(np.trace(E1), 2.0)
        and is_close(E0 @ C, C @ E0)
        and is_close(E1 @ C, C @ E1),
        f"Tr(e0)={np.trace(E0):.0f}, Tr(e1)={np.trace(E1):.0f}",
        results,
    )

    witness = np.array(
        [
            [0.0, 2.0, -1.0],
            [1.0, 0.5, 3.0],
            [4.0, -2.0, 1.0],
        ]
    )
    compressed = block_compression(witness)
    comm_norm = float(np.linalg.norm(compressed @ C - C @ compressed))
    check(
        "R5-2 old E(A)=e0Ae0+e1Ae1 is only block compression, not center-valued",
        comm_norm > 1e-3,
        f"counterexample commutator norm ||E_old(A)C-C E_old(A)||={comm_norm:.6f}",
        results,
    )

    h_group = 1.2 * I3 + 0.4 * C - 0.15 * C2
    check(
        "R5-3 on R[C3] the old block compression is just the identity",
        is_close(block_compression(h_group), h_group),
        "so it cannot by itself create an equal-central-block state from a group-algebra operator",
        results,
    )

    z_witness = center_valued_average(witness)
    check(
        "R5-4 corrected center-valued average lands in span{e0,e1}",
        is_close(z_witness, block_trace(witness, E0) * E0 + block_trace(witness, E1) * E1)
        and is_close(z_witness @ C, C @ z_witness)
        and is_close(center_valued_average(z_witness), z_witness),
        (
            f"block averages=({block_trace(witness, E0):+.6f}, "
            f"{block_trace(witness, E1):+.6f})"
        ),
        results,
    )

    avg_witness = c3_average(witness)
    check(
        "R5-5 C3 conjugation average gives the C3-commutant but does not select state weights",
        is_close(avg_witness @ C, C @ avg_witness)
        and not is_close(avg_witness, z_witness),
        "operator averaging and state-weight selection are distinct finite operations",
        results,
    )

    rho_trace = central_state_density(1.0 / 3.0)
    rho_equal = central_state_density(1.0 / 2.0)
    masses_trace = (float(np.trace(rho_trace @ E0)), float(np.trace(rho_trace @ E1)))
    masses_equal = (float(np.trace(rho_equal @ E0)), float(np.trace(rho_equal @ E1)))
    check(
        "R5-6 tracial state has central block masses 1:2",
        is_close(rho_trace, I3 / 3.0)
        and is_close(masses_trace[0], 1.0 / 3.0)
        and is_close(masses_trace[1], 2.0 / 3.0),
        f"trace masses=({masses_trace[0]:.6f}, {masses_trace[1]:.6f})",
        results,
    )
    check(
        "R5-7 equal-block state is positive, normalized, C3-invariant, and non-tracial",
        min_eigenvalue(rho_equal) >= -TOL
        and is_close(np.trace(rho_equal), 1.0)
        and is_close(rho_equal @ C, C @ rho_equal)
        and is_close(masses_equal[0], 0.5)
        and is_close(masses_equal[1], 0.5)
        and not is_close(rho_equal, rho_trace),
        f"equal masses=({masses_equal[0]:.6f}, {masses_equal[1]:.6f}), eigmin={min_eigenvalue(rho_equal):+.3e}",
        results,
    )

    ps = [0.0, 0.25, 1.0 / 3.0, 0.5, 0.75, 1.0]
    simplex_ok = True
    for p0 in ps:
        rho = central_state_density(p0)
        simplex_ok = (
            simplex_ok
            and min_eigenvalue(rho) >= -TOL
            and is_close(np.trace(rho), 1.0)
            and is_close(rho @ C, C @ rho)
        )
    check(
        "R5-8 finite C3 central-state simplex leaves the block weight unforced",
        simplex_ok,
        "sampled p0 values 0, 1/4, 1/3, 1/2, 3/4, 1 are all admissible C3-invariant states",
        results,
    )

    check(
        "R5-9 equal-block route is not the continuous U(1)_b rephasing obstruction",
        is_close(C @ C @ C, I3) and is_close(rho_equal @ C, C @ rho_equal),
        "changing central state weights leaves the discrete C3 operator relation C^3=I untouched",
        results,
    )

    check(
        "R5-10 local displayed Q(r) arithmetic is separated from state selection",
        abs(q_of_r(1.0) - 1.0) < TOL and abs(q_of_r(0.5) - 2.0 / 3.0) < TOL,
        "this verifies the displayed convention only; it does not derive the physical Q readout",
        results,
    )

    payload = {
        "claim_id": "flavor_find_j_round5_trace_vs_center_state_final_2026-06-02",
        "repair": "replace false block-compression-as-center-expectation step with corrected central-state algebra",
        "status_boundary": (
            "bounded-support finite algebra; no physical Q selector, trace-default "
            "authority, or Frobenius beta-family authority is derived here"
        ),
        "trace_block_masses": masses_trace,
        "equal_block_masses": masses_equal,
        "old_block_compression_counterexample_commutator_norm": comm_norm,
        "pass_count": sum(1 for item in results if item["pass"]),
        "fail_count": sum(1 for item in results if not item["pass"]),
        "results": results,
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    passed = payload["pass_count"]
    failed = payload["fail_count"]
    print()
    print("FLAVOR J-HUNT ROUND 5 REPAIRED CENTRAL-STATE CERTIFICATE")
    print(f"trace block masses       = ({masses_trace[0]:.6f}, {masses_trace[1]:.6f})")
    print(f"equal-block masses       = ({masses_equal[0]:.6f}, {masses_equal[1]:.6f})")
    print(f"old-E commutator norm    = {comm_norm:.6f}")
    print(f"OUTPUT_JSON={OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"SCORECARD PASS={passed} FAIL={failed}")
    print("VERDICT: bounded finite algebra repaired. The equal-block state is C3-compatible")
    print("and not the U(1)_b obstruction, but the finite packet does not force that state")
    print("or derive the physical Q=2/3 selector.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
