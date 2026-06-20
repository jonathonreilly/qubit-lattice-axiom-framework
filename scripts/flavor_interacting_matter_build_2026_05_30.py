#!/usr/bin/env python3
"""Executable split for the interacting-flavor build note.

Source-boundary split (scope_too_broad, 2026-06-20): the runner now SEGREGATES the
verified epsilon/Q algebra from the broader C3-wall and interacting-dynamics
claims. The original build reported an external/interpreter summary of three
nonperturbative matter-action builds; this runner does not certify those
branches, critical couplings, or r(g) curves.

VERIFIED CORE (load-bearing finite algebra):
* epsilon is constant on the hw=1 generation orbit and maps hw=1 to hw=2 as a
  (pi, pi, pi) shift (checks E1, E2);
* the Koide-style Q formula for F=aI+b(J-I) is Q=1/3+(2/3)r (Q checks).

CONDITIONAL / DIAGNOSTIC (NOT part of the verified core):
* the C3-wall obstruction — a C3-invariant diagonal generation operator is
  scalar, so diagonal orbit-splitting requires C3 breaking (checks C3-1..C3-3,
  formerly E3-E5). These are exact finite-algebra facts about the tested
  diagonal/epsilon escape, but the note does NOT assert them as a retained
  framework no-go; they support the broader (conditional) C3-wall narrative.
* the supplied off-self-dual r values are contextual inputs, not derivations.

Both groups pass deterministically; segregation is by label/section only, and no
derived value is changed.
"""

from __future__ import annotations

import itertools

import numpy as np

PASS = 0
FAIL = 0
TOL = 1.0e-10


CORE_PASS = 0
CORE_FAIL = 0
COND_PASS = 0
COND_FAIL = 0


def check(name: str, condition: bool, detail: str = "", group: str = "core") -> bool:
    """Record a check. group='core' = verified epsilon/Q algebra (load-bearing);
    group='conditional' = C3-wall / diagnostic checks (NOT part of the verified
    core). Both feed the global scorecard, but subtotals keep the boundary
    split explicit."""
    global PASS, FAIL, CORE_PASS, CORE_FAIL, COND_PASS, COND_FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    if group == "conditional":
        COND_PASS += int(ok)
        COND_FAIL += int(not ok)
    else:
        CORE_PASS += int(ok)
        CORE_FAIL += int(not ok)
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
    print("FLAVOR INTERACTING MATTER BUILD: SOURCE-BOUNDARY SPLIT (verified epsilon/Q core | conditional C3-wall)")
    print("scope: verified core = exact epsilon/Q finite algebra; C3-wall + interacting branches are conditional/diagnostic")

    # ------------------------------------------------------------------
    # VERIFIED CORE: epsilon generation-orbit algebra + Q(r) trace identity.
    # These are the only load-bearing runner-verified claims.
    # ------------------------------------------------------------------
    print("\n--- VERIFIED CORE: epsilon/Q finite algebra (load-bearing) ---")
    corners = list(itertools.product([0, 1], repeat=3))
    hw1 = [c for c in corners if sum(c) == 1]
    eps_hw1 = [(-1) ** sum(c) for c in hw1]
    shifted_hw = [sum(1 - x for x in c) for c in hw1]

    check(
        "E1 epsilon is constant on the hw=1 generation orbit",
        eps_hw1 == [-1, -1, -1],
        f"eps(hw1)={eps_hw1}",
        group="core",
    )
    check(
        "E2 epsilon as the (pi,pi,pi) shift maps hw=1 out of the triplet to hw=2",
        shifted_hw == [2, 2, 2],
        f"shifted Hamming weights={shifted_hw}",
        group="core",
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
            group="core",
        )

    # ------------------------------------------------------------------
    # CONDITIONAL / DIAGNOSTIC: the C3-wall obstruction. Exact finite-algebra
    # facts about the tested diagonal/epsilon escape, but NOT asserted as a
    # retained framework no-go and NOT part of the verified core.
    # ------------------------------------------------------------------
    print("\n--- CONDITIONAL / DIAGNOSTIC: C3-wall obstruction (NOT load-bearing) ---")
    c = c3_cycle()
    i3 = np.eye(3, dtype=complex)
    check(
        "C3-1 C3 cycle has order 3",
        np.allclose(c @ c @ c, i3, atol=TOL),
        group="conditional",
    )

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
        "C3-2 C3-invariant diagonal generation operators are scalar",
        invariant_kernel_dim == 1,
        f"diagonal invariant dimension={invariant_kernel_dim}",
        group="conditional",
    )

    splitting = np.diag([1.0, -1.0, 0.0])
    split_breaks_c3 = np.linalg.norm(c @ splitting @ c.conj().T - splitting) > 0.1
    check(
        "C3-3 non-scalar diagonal orbit splitting requires C3 breaking",
        split_breaks_c3,
        f"commutator norm={np.linalg.norm(c @ splitting @ c.conj().T - splitting):.3f}",
        group="conditional",
    )

    contextual_rs = {
        "natural C3-symmetric/self-dual input": 0.0,
        "reported SD/Fierz off-self-dual input": 2.0 / 5.0,
        "reported two-channel onset input": 0.535,
        "Koide target comparison": 0.5,
    }
    print("\nContextual r values converted through the checked Q formula (context only):")
    for label, r in contextual_rs.items():
        print(f"  {label}: r={r:.6f}, Q={q_formula(r):.6f}")

    print("\nCONTEXT ONLY: this runner does not derive the three interacting builds,")
    print("critical coupling, continuous r(g) curve, or b!=0 branch. Those remain")
    print("external build summaries until a first-principles matter-action runner lands.")
    print(f"\nVERIFIED-CORE SUBTOTAL  PASS={CORE_PASS} FAIL={CORE_FAIL}")
    print(f"CONDITIONAL SUBTOTAL    PASS={COND_PASS} FAIL={COND_FAIL}")
    print(f"\nTOTAL SUMMARY PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
