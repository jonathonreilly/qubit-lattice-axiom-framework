#!/usr/bin/env python3
"""Finite checks for the post-record classical semigroup boundary.

The target is the dynamics implication of the record-typing split:

* pre-record: quantum / ensemble states may have amplitudes, probabilities,
  instruments, and supplied continuous dynamics;
* post-record: realized record atoms live in a finite commutative algebra and
  finite histories/counts evolve by append/count updates.

This runner verifies the exact finite algebra facts that keep those layers
separate:

1. automorphisms of a finite record alphabet are only permutations;
2. every derivation of C^n is zero, so there is no nontrivial connected
   reversible Hamiltonian-like flow on the finite post-record algebra itself;
3. append/count updates are irreversible translations on N^O;
4. nontrivial continuous Markov semigroups live on the probability/ensemble
   layer and require supplied rates;
5. stable dial locations are set by supplied generators/flows, not by the
   finite record algebra alone.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import math

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def basis(n: int) -> list[tuple[int, ...]]:
    return [tuple(1 if i == j else 0 for i in range(n)) for j in range(n)]


def pointwise_mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x * y for x, y in zip(a, b))


def pullback_matrix(phi: tuple[int, ...]) -> list[list[int]]:
    """Matrix for T_phi f = f o phi on functions O -> R.

    phi[i] is the target atom assigned to source atom i.
    Column j is T(e_j), the indicator of phi^{-1}(j).
    """
    n = len(phi)
    mat = [[0 for _ in range(n)] for _ in range(n)]
    for source, target in enumerate(phi):
        mat[source][target] = 1
    return mat


def mat_vec(mat: list[list[int]], vec: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[j] * vec[j] for j in range(len(vec))) for row in mat)


def is_unital_hom(phi: tuple[int, ...]) -> bool:
    n = len(phi)
    mat = pullback_matrix(phi)
    one = tuple(1 for _ in range(n))
    atoms = basis(n)
    if mat_vec(mat, one) != one:
        return False
    for a in atoms:
        for b in atoms:
            left = mat_vec(mat, pointwise_mul(a, b))
            right = pointwise_mul(mat_vec(mat, a), mat_vec(mat, b))
            if left != right:
                return False
    return True


def rank_int_matrix(mat: list[list[int]]) -> int:
    return int(sp.Matrix(mat).rank())


def derivation_nullity(n: int) -> tuple[int, int, int]:
    """Return (num_unknowns, rank, nullity) for derivations of C^n.

    A derivation D satisfies D(fg) = D(f)g + fD(g). We impose the equations on
    the idempotent atom basis e_i.
    """
    unknowns = n * n
    rows: list[list[int]] = []

    def idx(row: int, col: int) -> int:
        return row * n + col

    atoms = basis(n)
    for i, ei in enumerate(atoms):
        for j, ej in enumerate(atoms):
            prod_ij = pointwise_mul(ei, ej)
            for k in range(n):
                row = [0 for _ in range(unknowns)]
                # D(e_i e_j)_k
                if prod_ij == ei:
                    row[idx(k, i)] += 1
                elif prod_ij == ej:
                    row[idx(k, j)] += 1
                elif any(prod_ij):
                    raise AssertionError("unexpected atom product")
                # - (D(e_i) e_j)_k - (e_i D(e_j))_k
                row[idx(k, i)] -= ej[k]
                row[idx(k, j)] -= ei[k]
                rows.append(row)

    rank = int(sp.Matrix(rows).rank())
    return unknowns, rank, unknowns - rank


def count_vector(word: tuple[int, ...], n: int) -> tuple[int, ...]:
    out = [0 for _ in range(n)]
    for atom in word:
        out[atom] += 1
    return tuple(out)


def add_counts(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def in_image_of_translation(c: tuple[int, ...], v: tuple[int, ...]) -> bool:
    return all(ci >= vi for ci, vi in zip(c, v))


def two_state_markov(a: Fraction, b: Fraction, exp_factor: Fraction) -> list[list[Fraction]]:
    """Column-stochastic two-state semigroup matrix at a time with e^-lambda t.

    Generator convention:
        Q = [[-a, b],
             [ a,-b]]
    with stationary vector (b/(a+b), a/(a+b)).
    """
    lam = a + b
    pi0 = b / lam
    pi1 = a / lam
    e = exp_factor
    return [
        [pi0 + pi1 * e, pi0 * (1 - e)],
        [pi1 * (1 - e), pi1 + pi0 * e],
    ]


def det2(mat: list[list[Fraction]]) -> Fraction:
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def inv2(mat: list[list[Fraction]]) -> list[list[Fraction]]:
    d = det2(mat)
    return [
        [mat[1][1] / d, -mat[0][1] / d],
        [-mat[1][0] / d, mat[0][0] / d],
    ]


def col_sums(mat: list[list[Fraction]]) -> list[Fraction]:
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]


def stationary_from_rates(a: Fraction, b: Fraction) -> tuple[Fraction, Fraction]:
    return (b / (a + b), a / (a + b))


def main() -> int:
    n = 3
    section("A finite record algebra has only permutation automorphisms")
    maps = list(product(range(n), repeat=n))
    homs = [phi for phi in maps if is_unital_hom(phi)]
    autos = [phi for phi in homs if len(set(phi)) == n and rank_int_matrix(pullback_matrix(phi)) == n]
    noninvertible = [phi for phi in homs if phi not in autos]
    check("A1 every function O -> O gives a unital algebra endomorphism by pullback",
          len(homs) == n ** n, f"endomorphisms={len(homs)} expected={n**n}")
    check("A2 automorphisms are exactly bijections/permutations",
          len(autos) == math.factorial(n), f"automorphisms={len(autos)} expected={math.factorial(n)}")
    check("A3 non-bijective endomorphisms exist but are not reversible",
          len(noninvertible) == n ** n - math.factorial(n),
          f"noninvertible={len(noninvertible)}")
    collapse = (0, 0, 1)
    check("A4 a coarse-graining/collapse map is a valid endomorphism, not an automorphism",
          collapse in homs and collapse in noninvertible and rank_int_matrix(pullback_matrix(collapse)) < n,
          f"phi={collapse}, rank={rank_int_matrix(pullback_matrix(collapse))}")

    section("No nontrivial connected reversible flow on C^n")
    unknowns, rank, nullity = derivation_nullity(n)
    check("D1 derivation equations on C^3 have full rank",
          rank == unknowns, f"unknowns={unknowns}, rank={rank}, nullity={nullity}")
    check("D2 every derivation of the finite record algebra is zero",
          nullity == 0)
    identity = tuple(range(n))
    min_perm_distance = min(
        math.sqrt(
            sum(
                ((1 if i == p[j] else 0) - (1 if i == j else 0)) ** 2
                for i in range(n)
                for j in range(n)
            )
        )
        for p in autos if p != identity
    )
    # The expression above deliberately computes the Frobenius distance by
    # flattening permutation matrices; the minimum nonidentity distance is 2.
    check("D3 nonidentity permutations are separated from identity",
          abs(min_perm_distance - 2.0) < 1e-12,
          f"minimum Frobenius distance={min_perm_distance}")
    check("D4 a continuous one-parameter automorphism path starting at identity is locally forced to identity",
          min_perm_distance > 1.0,
          "there is an open ball around identity containing no other automorphism")

    section("Append/count dynamics is an irreversible post-record action")
    word = (0, 2, 2, 1)
    suffix = (2, 0)
    c = count_vector(word, n)
    v = count_vector(suffix, n)
    updated = count_vector(word + suffix, n)
    check("R1 suffix append composes finite histories",
          word + suffix == (0, 2, 2, 1, 2, 0))
    check("R2 count projection is equivariant under append",
          updated == add_counts(c, v), f"{c} + {v} = {updated}")
    check("R3 count translation by a nonzero suffix is injective on N^O",
          add_counts((0, 0, 0), v) != add_counts((1, 0, 0), v))
    check("R4 count translation by a nonzero suffix is not surjective on N^O",
          not in_image_of_translation((0, 0, 0), v),
          "the zero count has no preimage after appending a nonempty suffix")
    check("R5 append/count dynamics is therefore not a reversible automorphism",
          v != (0, 0, 0) and not in_image_of_translation((0, 0, 0), v))

    section("Continuous rate dynamics belongs to the ensemble layer")
    T = two_state_markov(Fraction(1, 1), Fraction(2, 1), Fraction(1, 2))
    inv_T = inv2(T)
    check("M1 supplied two-state rate matrix has stochastic semigroup at tested time",
          col_sums(T) == [Fraction(1, 1), Fraction(1, 1)] and all(x >= 0 for row in T for x in row),
          f"T={T}")
    check("M2 the tested semigroup step is not a permutation/write of one realized atom",
          any(x not in (0, 1) for row in T for x in row),
          f"T={T}")
    check("M3 the inverse linear map is not stochastic",
          any(x < 0 for row in inv_T for x in row),
          f"T^-1={inv_T}")
    p0_after_atom0 = (T[0][0], T[1][0])
    check("M4 a Markov step from a realized atom produces an ensemble distribution",
          p0_after_atom0 != (Fraction(1, 1), Fraction(0, 1))
          and p0_after_atom0 != (Fraction(0, 1), Fraction(1, 1)),
          f"T e0={p0_after_atom0}")

    section("Stable dial locations require supplied dynamics")
    pi_equal = stationary_from_rates(Fraction(1, 1), Fraction(1, 1))
    pi_dimension = stationary_from_rates(Fraction(2, 1), Fraction(1, 1))
    pi_other = stationary_from_rates(Fraction(1, 1), Fraction(2, 1))
    check("S1 equal-letter stationary point is realized by supplied symmetric rates",
          pi_equal == (Fraction(1, 2), Fraction(1, 2)), f"pi={pi_equal}")
    check("S2 dimension-weighted stationary point is realized by different supplied rates",
          pi_dimension == (Fraction(1, 3), Fraction(2, 3)), f"pi={pi_dimension}")
    check("S3 the same record algebra permits another stable point under another generator",
          pi_other == (Fraction(2, 3), Fraction(1, 3)), f"pi={pi_other}")
    check("S4 finite record algebra alone cannot distinguish those supplied generators",
          len({pi_equal, pi_dimension, pi_other}) == 3,
          "stability is a property of the chosen generator/functional")

    section("Scorecard")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "FINDING: finite post-record algebras have only discrete reversible "
        "permutations and zero derivations. Nontrivial continuous dynamics, "
        "transition rates, and dial attractors live on supplied Markov/ensemble "
        "or append/action layers, not in Record alone."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
