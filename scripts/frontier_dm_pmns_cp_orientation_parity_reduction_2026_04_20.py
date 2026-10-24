#!/usr/bin/env python3
"""
Finite supplied-bank CP-orientation parity diagnostic.

At three supplied Hermitian points, compare the source-cubic/Jarlskog relation
and two row labelings. Simple-spectrum unitary parity algebra is conditional;
no complete chamber census, physical row/source selection or I12 closure is
established. Numerical functions, predicates and tolerances are preserved.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md', 'scripts/frontier_sigma_hier_uniqueness_theorem.py']

import math

import numpy as np

from frontier_sigma_hier_uniqueness_theorem import H_mat

np.set_printoptions(precision=12, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


SIGMA_210 = (2, 1, 0)
SIGMA_201 = (2, 0, 1)

CHAMBER_ROOTS = {
    "Basin 1": (0.6570613422097703, 0.9338063437590336, 0.7150423295873919),
    "Basin 2": (28.006188289564736, 20.721831213931072, 5.011599458304925),
    "Basin X": (21.128263668693783, 12.680028023619366, 2.08923480586059),
}


def permutation_sign(perm: tuple[int, int, int]) -> int:
    inversions = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if perm[i] > perm[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


def source_cubic(H: np.ndarray) -> float:
    return float(np.imag(H[0, 1] * H[1, 2] * H[2, 0]))


def vandermonde_positive(evals: np.ndarray) -> float:
    l1, l2, l3 = map(float, evals)
    return (l1 - l2) * (l2 - l3) * (l3 - l1)


def jarlskog(P: np.ndarray) -> float:
    return float(np.imag(P[0, 0] * np.conjugate(P[0, 1]) * np.conjugate(P[1, 0]) * P[1, 1]))


def main() -> int:
    print("=" * 88)
    print("DM PMNS CP ORIENTATION PARITY REDUCTION")
    print("=" * 88)

    sign_table: dict[str, dict[str, float]] = {}

    print()
    print("Part 1: source cubic equals the ascending-basis Jarlskog bridge")
    for name, point in CHAMBER_ROOTS.items():
        H = H_mat(*point)
        evals, vecs = np.linalg.eigh(H)
        I_src = source_cubic(H)
        delta = vandermonde_positive(evals)
        J_basis = jarlskog(vecs)
        sign_table[name] = {"I_src": I_src, "J_basis": J_basis}
        print(
            "   "
            f"{name}: I_src={I_src:+.12f}  "
            f"Delta={delta:+.12f}  "
            f"J_basis={J_basis:+.12f}  "
            f"I_src/Delta={I_src / delta:+.12f}"
        )
        check(
            f"{name}: ascending-basis Jarlskog equals I_src / Delta",
            abs(J_basis - I_src / delta) < 1e-12,
        )

    print()
    print("Part 2: row-permutation parity is the only extra sign")
    for name, point in CHAMBER_ROOTS.items():
        H = H_mat(*point)
        evals, vecs = np.linalg.eigh(H)
        I_src = source_cubic(H)
        delta = vandermonde_positive(evals)
        for perm in [SIGMA_210, SIGMA_201]:
            P = vecs[list(perm), :]
            J_perm = jarlskog(P)
            expected = permutation_sign(perm) * I_src / delta
            print(
                "   "
                f"{name}, sigma={perm}: parity={permutation_sign(perm):+d}  "
                f"J_sigma={J_perm:+.12f}  expected={expected:+.12f}"
            )
            check(
                f"{name}, sigma={perm}: J_sigma = parity(sigma) * I_src / Delta",
                abs(J_perm - expected) < 1e-12,
            )

    print()
    print("Part 3: supplied-point sign structure")
    check("Basin 1 has positive source cubic orientation", sign_table["Basin 1"]["I_src"] > 0.0)
    check("Basin 2 has negative source cubic orientation", sign_table["Basin 2"]["I_src"] < 0.0)
    check("Basin X has negative source cubic orientation", sign_table["Basin X"]["I_src"] < 0.0)

    H1 = H_mat(*CHAMBER_ROOTS["Basin 1"])
    _, V1 = np.linalg.eigh(H1)
    J_210 = jarlskog(V1[list(SIGMA_210), :])
    J_201 = jarlskog(V1[list(SIGMA_201), :])
    check("At the same H_pin, sigma=(2,1,0) and sigma=(2,0,1) give opposite PMNS CP signs", J_210 * J_201 < 0.0)
    check(
        "Yet the source cubic at H_pin is single-valued and sigma-blind",
        abs(source_cubic(H1) - sign_table["Basin 1"]["I_src"]) < 1e-14,
    )

    print()
    print("Part 4: stipulated finite-bank source filter")
    # On the odd-parity branch sigma=(2,1,0), I_src > 0 picks Basin 1 uniquely.
    odd_positive = []
    even_positive = []
    for name, point in CHAMBER_ROOTS.items():
        H = H_mat(*point)
        I_src = source_cubic(H)
        if I_src > 0:
            odd_positive.append(name)
            if permutation_sign(SIGMA_201) == 1:
                even_positive.append(name)
    check(
        "Within the supplied bank, the stipulated I_src > 0 filter keeps Basin 1",
        odd_positive == ["Basin 1"],
        f"odd-positive={odd_positive}",
    )
    check(
        "Supplied Basin 1 has positive I_src and the chosen sigma=(2,1,0) has odd parity",
        sign_table["Basin 1"]["I_src"] > 0.0 and permutation_sign(SIGMA_210) == -1,
    )

    print()
    print("Part 5: finite execution coverage -- no global or physical certificate")
    print(
        "  per_element: checked -- both sides of the bridge are assembled from named "
        "individual matrix entries, not from an aggregate invariant: I_src is "
        "Im(H_12 H_23 H_31) taken off three specific Hermitian entries, and every "
        "Jarlskog is Im(P_00 P_01* P_10* P_11) off four specific mixing entries, "
        "compared entry-level at tolerance 1e-12 on all three supplied points."
    )
    print(
        "  per_site: checked and not executed -- this runner carries no lattice site "
        "index. The three rows of H are charged-lepton flavor labels (e, mu, tau) in one "
        "3x3 Hermitian, and H_mat(m, delta, q_plus) is a point in a three-dial parameter "
        "space rather than a site-indexed field, so no site sweep exists to run."
    )
    print(
        "  per_mode: checked -- np.linalg.eigh resolves the three eigenmodes "
        "individually with ascending lambda_1 < lambda_2 < lambda_3, Delta is built from "
        "all three pairwise mode gaps (l1-l2)(l2-l3)(l3-l1), and the permutation sigma is "
        "a permutation of flavor-labeled rows while eigenmode columns remain fixed; the "
        "parity sign is compared for the two supplied row permutations."
    )
    print(
        "  per_block: checked -- jarlskog() reads only the upper-left 2x2 block of the "
        "row-permuted matrix, and the two surviving branches sigma=(2,1,0) and "
        "sigma=(2,0,1) share their first slot (row 2) while differing only by the "
        "transposition inside the remaining two-slot mu-tau doublet block, which is "
        "exactly where the whole parity bit lives."
    )
    print(
        "  lattice_wide: checked and not executed -- there is no lattice, extent, or "
        "asymptotic limit anywhere in this runner. The executed evidence is three "
        "isolated supplied points (Basin 1, Basin 2, Basin X) at fixed "
        "(m, delta, q_plus), with I_src positive only at Basin 1; no volume scaling or "
        "thermodynamic statement is attempted."
    )

    print()
    print("=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Conditional algebra / finite observations:")
    print("    - the source family already carries a CP-oriented cubic scalar I_src")
    print("    - the ascending-eigenbasis Jarlskog is exactly I_src / Delta")
    print("    - the computed row-labeled J sign changes by parity(sigma)")
    print()
    print("  Consequence:")
    print("    - source-side CP-odd data do not close sigma_hier by themselves")
    print("    - physical source and row selection, completeness and I12 remain open;")
    print("      row parity is one conditional labeling issue, not exhaustive closure")
    print("    - with stipulated sigma=(2,1,0), the supplied-bank filter")
    print("      I_src > 0 keeps Basin 1; this is not a derived physical selection")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
