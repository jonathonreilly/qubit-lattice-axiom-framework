#!/usr/bin/env python3
"""Generation mass-degeneracy minimal-symmetry-breaking discriminator.

Substep-4 of the staggered-Dirac gate needs the three hw=1 generation sectors
to carry three DISTINCT masses. Two retained rows bracket the question:

  s3_mass_matrix_no_go_note           (retained_no_go)
        unbroken S_3-invariant Hermitian operators on V = span(X1,X2,X3)
        have at most TWO distinct eigenvalues (forced degeneracy).
  z2_hw1_mass_matrix_parametrization  (retained)
        a single preserved Z_2 (swap X1,X2; fix X3) gives a 5-real-param
        family that is GENERICALLY nondegenerate (three distinct).

This discriminator completes the lattice of S_3 subgroups and proves the exact
characterization: forced generation degeneracy holds for the FULL S_3 and for
NO proper subgroup. Hence the minimal symmetry-breaking input substep-4
requires is precisely S_3 -> (any proper subgroup); the framework's own
C_3[111] is one sufficient proper-subgroup route.

Method, for each subgroup G <= S_3 acting on C^3 by permutation:
  * commutant complex-dimension via the exact character formula
      dim Comm = (1/|G|) sum_g |Tr rho(g)|^2  (= real dim of G-invariant
      Hermitian operators, the mass-matrix parameter count);
  * generic distinct-eigenvalue count of a G-invariant Hermitian operator,
    built by Reynolds (group) averaging a fixed generic Hermitian seed.

Verdict: only the full S_3 forces a degeneracy (2 distinct eigenvalues, the
2-dim irrep E doubled); C_3, every Z_2, and the trivial group all give 3
distinct. The 2-dim irrep E stays irreducible only under the full S_3.

Pure finite-group representation theory on abstract C^3. No PDG / fitted /
scale / mass-value input. This script asserts no audit status.
"""

from __future__ import annotations

import itertools

import numpy as np

TOL = 1.0e-9
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def perm_matrix(p: tuple[int, int, int]) -> np.ndarray:
    """3x3 permutation matrix sending e_i -> e_{p[i]}."""
    m = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        m[p[i], i] = 1.0
    return m


# All six elements of S_3 as permutations of (0,1,2).
S3 = list(itertools.permutations((0, 1, 2)))


def subgroup(name: str) -> list[tuple[int, int, int]]:
    if name == "S3":
        return S3
    if name == "C3":   # {id, (012), (021)}
        return [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    if name == "Z2":   # {id, swap 0<->1}
        return [(0, 1, 2), (1, 0, 2)]
    if name == "triv":
        return [(0, 1, 2)]
    raise ValueError(name)


def commutant_dim(G: list[tuple[int, int, int]]) -> int:
    """Exact: dim_C Comm(rho) = (1/|G|) sum_g |Tr rho(g)|^2."""
    total = 0.0
    for p in G:
        tr = np.trace(perm_matrix(p))
        total += abs(tr) ** 2
    return round(total / len(G))


def reynolds_invariant(G: list[tuple[int, int, int]], seed: np.ndarray) -> np.ndarray:
    """Project a Hermitian seed onto the G-invariant subspace by averaging."""
    acc = np.zeros((3, 3), dtype=complex)
    for p in G:
        R = perm_matrix(p)
        acc += R @ seed @ R.conj().T
    return acc / len(G)


def distinct_eigs(H: np.ndarray) -> list[float]:
    ev = np.sort(np.linalg.eigvalsh((H + H.conj().T) / 2).real)
    out: list[float] = []
    for x in ev:
        if not out or abs(x - out[-1]) > 1e-6:
            out.append(float(x))
    return out


def main() -> int:
    print("=" * 76)
    print("GENERATION MASS-DEGENERACY MINIMAL-SYMMETRY-BREAKING DISCRIMINATOR")
    print("=" * 76)

    # A fixed generic Hermitian seed (deterministic; distinct entries).
    seed = np.array(
        [[5.0, 2.0 + 1.0j, -1.0 + 3.0j],
         [2.0 - 1.0j, 7.0, 0.5 - 2.0j],
         [-1.0 - 3.0j, 0.5 + 2.0j, 11.0]],
        dtype=complex,
    )

    expected = {  # (commutant dim, generic distinct eigenvalues, forces degeneracy?)
        "S3":   (2, 2, True),
        "C3":   (3, 3, False),
        "Z2":   (5, 3, False),
        "triv": (9, 3, False),
    }
    labels = {"S3": "full S_3 (all axis permutations)",
              "C3": "C_3[111] (3-cycle only)",
              "Z2": "single transposition Z_2",
              "triv": "no symmetry"}

    results = {}
    for g in ("S3", "C3", "Z2", "triv"):
        G = subgroup(g)
        cdim = commutant_dim(G)
        Minv = reynolds_invariant(G, seed)
        de = distinct_eigs(Minv)
        forces = len(de) < 3
        results[g] = (cdim, len(de), forces)
        exp_cdim, exp_ndist, exp_forces = expected[g]
        print("\n" + "-" * 76)
        print(f"G = {g}: {labels[g]}")
        print("-" * 76)
        check(f"commutant (mass-param) dim = {exp_cdim}", cdim == exp_cdim, detail=f"got {cdim}")
        check(f"generic invariant mass matrix has {exp_ndist} distinct eigenvalues",
              len(de) == exp_ndist, detail=f"eigs={[round(x,3) for x in de]}")
        check(f"forces degeneracy = {exp_forces}", forces == exp_forces)

    # The decisive structural fact: only S_3 forces degeneracy.
    print("\n" + "-" * 76)
    print("CHARACTERIZATION")
    print("-" * 76)
    forcing = [g for g, (_, _, f) in results.items() if f]
    check("forced generation degeneracy holds for the FULL S_3 only",
          forcing == ["S3"], detail=f"forcing set = {forcing}")
    check("every PROPER subgroup (C_3, Z_2, trivial) permits 3 distinct masses",
          all(not results[g][2] for g in ("C3", "Z2", "triv")))
    # reproduce retained anchors
    check("reproduces retained s3_mass_matrix_no_go: S_3 -> <=2 eigenvalues",
          results["S3"][1] <= 2)
    check("reproduces retained z2 parametrization: Z_2 commutant real-dim 5, nondegenerate",
          results["Z2"][0] == 5 and results["Z2"][1] == 3)

    # The 2-dim irrep E is the obstruction carrier: irreducible only under full S_3.
    # dim Comm = sum(mult^2). S_3: A1(1)+E(1) -> 1+1=2 ; under any proper subgroup E splits,
    # raising the commutant dim above 2 (3,5, or 9), i.e. E is no longer irreducible.
    print("\n" + "-" * 76)
    print("OBSTRUCTION CARRIER: the 2-dim irrep E")
    print("-" * 76)
    check("E (2-dim) irreducible under S_3 (commutant dim 2 = 1^2+1^2)",
          results["S3"][0] == 2)
    check("E reducible under every proper subgroup (commutant dim > 2)",
          all(results[g][0] > 2 for g in ("C3", "Z2", "triv")))

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  MINIMAL-BREAKING CHARACTERIZATION PROVEN.\n"
            "  The forced generation mass-degeneracy on the hw=1 triplet is carried\n"
            "  entirely by the 2-dim S_3 irrep E, which is irreducible under the FULL\n"
            "  S_3 and reducible under every proper subgroup. Therefore:\n\n"
            "   * unbroken S_3        -> at most 2 distinct masses (forced degeneracy);\n"
            "   * any proper subgroup -> 3 distinct masses permitted (C_3, Z_2, triv);\n\n"
            "  So substep-4's required external input is EXACTLY an S_3 -> proper-\n"
            "  subgroup breaking; the framework's own C_3[111] is one sufficient\n"
            "  proper-subgroup route. This characterizes the residual\n"
            "  precisely; it does NOT derive the breaking, the mass values, or the\n"
            "  generation labeling -- those remain the admitted external input.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
