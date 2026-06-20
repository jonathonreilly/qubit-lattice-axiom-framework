#!/usr/bin/env python3
"""Executable core split for the interacting-flavor build note.

The original build reported an external/interpreter summary of three
nonperturbative matter-action builds. This runner does not certify those
branches, critical couplings, or r(g) curves. It verifies only the finite
algebraic core that is source-native:

* epsilon is constant on the hw=1 generation orbit and maps hw=1 to hw=2 as a
  (pi, pi, pi) shift;
* a C3-invariant diagonal generation operator is scalar, so diagonal
  orbit-splitting requires C3 breaking;
* the Koide-style Q formula for F=aI+b(J-I) is Q=1/3+(2/3)r;
* the supplied off-self-dual r values are contextual inputs, not derivations.
"""

from __future__ import annotations

import itertools

import numpy as np

PASS = 0
FAIL = 0
TOL = 1.0e-10


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f" -- {detail}"
    print(line)
    return ok


def c3_cycle() -> np.ndarray:
    return np.array(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ],
        dtype=complex,
    )


def q_from_matrix(a: float, b: float) -> float:
    i3 = np.eye(3)
    j = np.ones((3, 3))
    f = a * i3 + b * (j - i3)
    return float(np.trace(f @ f) / (np.trace(f) ** 2))


def q_formula(r: float) -> float:
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def main() -> int:
    print("FLAVOR INTERACTING MATTER BUILD: EXECUTABLE CORE SPLIT")
    print("scope: exact epsilon/Q/C3 finite algebra; external interacting branches are context only")

    corners = list(itertools.product([0, 1], repeat=3))
    hw1 = [c for c in corners if sum(c) == 1]
    eps_hw1 = [(-1) ** sum(c) for c in hw1]
    shifted_hw = [sum(1 - x for x in c) for c in hw1]

    check(
        "E1 epsilon is constant on the hw=1 generation orbit",
        eps_hw1 == [-1, -1, -1],
        f"eps(hw1)={eps_hw1}",
    )
    check(
        "E2 epsilon as the (pi,pi,pi) shift maps hw=1 out of the triplet to hw=2",
        shifted_hw == [2, 2, 2],
        f"shifted Hamming weights={shifted_hw}",
    )

    c = c3_cycle()
    i3 = np.eye(3, dtype=complex)
    check("E3 C3 cycle has order 3", np.allclose(c @ c @ c, i3, atol=TOL))

    diagonal_basis = [
        np.diag([1.0, 0.0, 0.0]),
        np.diag([0.0, 1.0, 0.0]),
        np.diag([0.0, 0.0, 1.0]),
    ]
    commutator_matrix = []
    for basis in diagonal_basis:
        commutator_matrix.append((c @ basis @ c.conj().T - basis).reshape(-1))
    commutator_matrix = np.vstack(commutator_matrix).T
    # C D C^{-1}=D imposes the two independent equalities d0=d1=d2.
    invariant_kernel_dim = 3 - np.linalg.matrix_rank(commutator_matrix, tol=TOL)
    check(
        "E4 C3-invariant diagonal generation operators are scalar",
        invariant_kernel_dim == 1,
        f"diagonal invariant dimension={invariant_kernel_dim}",
    )

    splitting = np.diag([1.0, -1.0, 0.0])
    split_breaks_c3 = np.linalg.norm(c @ splitting @ c.conj().T - splitting) > 0.1
    check(
        "E5 non-scalar diagonal orbit splitting requires C3 breaking",
        split_breaks_c3,
        f"commutator norm={np.linalg.norm(c @ splitting @ c.conj().T - splitting):.3f}",
    )

    for r in (0.0, 2.0 / 5.0, 0.5, 0.535):
        a = 1.0
        b = float(np.sqrt(r))
        matrix_q = q_from_matrix(a, b)
        formula_q = q_formula(r)
        check(
            f"Q formula holds for r={r:.3f}",
            abs(matrix_q - formula_q) < TOL,
            f"Q={matrix_q:.6f}",
        )

    contextual_rs = {
        "natural C3-symmetric/self-dual input": 0.0,
        "reported SD/Fierz off-self-dual input": 2.0 / 5.0,
        "reported two-channel onset input": 0.535,
        "Koide target comparison": 0.5,
    }
    print("\nContextual r values converted through the checked Q formula:")
    for label, r in contextual_rs.items():
        print(f"  {label}: r={r:.6f}, Q={q_formula(r):.6f}")

    print("\nCONTEXT ONLY: this runner does not derive the three interacting builds,")
    print("critical coupling, continuous r(g) curve, or b!=0 branch. Those remain")
    print("external build summaries until a first-principles matter-action runner lands.")
    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
