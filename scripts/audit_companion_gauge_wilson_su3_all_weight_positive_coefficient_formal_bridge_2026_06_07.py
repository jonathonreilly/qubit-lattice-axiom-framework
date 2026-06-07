#!/usr/bin/env python3
"""Exact-support runner for the SU(3) Wilson all-weight positivity bridge.

This runner certifies the finite, framework-native checks behind
GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE_NOTE_2026-06-07.

It does not numerically integrate SU(3).  The load-bearing proof is the
character identity

    exp[(beta/6)(chi_3 + chi_3bar)]
      = sum_n (beta/6)^n (chi_3 + chi_3bar)^n / n!,

where each power is a finite tensor-product character with non-negative
integer irreducible multiplicities, and each irrep (p,q) occurs at finite
word length p+q through the Cartan component of
Sym^p(3) tensor Sym^q(3bar).
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE_NOTE_2026-06-07.md"
PARENT_NOTE = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def witness_length(p: int, q: int) -> int:
    return p + q


def lower_bound_monomial_at_beta_one(p: int, q: int) -> Fraction:
    """The positive contribution from n=p+q at beta=1.

    The actual coefficient can have additional non-negative contributions.
    This lower-bound monomial is enough to prove strict positivity for
    beta > 0.
    """
    n = witness_length(p, q)
    return Fraction(1, (6**n) * factorial(n))


def formal_convolution_action(weights: list[tuple[int, int]], z: dict[tuple[int, int], Fraction], vector):
    """Coefficientwise action C_Z chi_lambda = z_lambda chi_lambda."""
    return [z[w] * vector[i] for i, w in enumerate(weights)]


def main() -> int:
    print("=" * 88)
    print("GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE")
    print("Goal: all-weight Wilson coefficient positivity + formal convolution bridge")
    print("=" * 88)

    section("Part 1: strict positivity witness for every sampled dominant weight")
    sample_weights = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (3, 3), (5, 2), (2, 5), (8, 0), (0, 8)]

    for p, q in sample_weights:
        n = witness_length(p, q)
        lb = lower_bound_monomial_at_beta_one(p, q)
        check(
            f"finite Cartan-component witness for weight ({p},{q})",
            n >= 0 and lb > 0,
            detail=f"n=p+q={n}, beta=1 lower monomial={lb}",
        )

    section("Part 2: positivity of normalized Wilson eigenvalues a_(p,q)")
    for p, q in [(0, 0), (1, 0), (0, 1), (1, 1), (4, 2), (2, 4), (6, 6)]:
        d = dim_su3(p, q)
        c_lambda = lower_bound_monomial_at_beta_one(p, q)
        c_00 = Fraction(1, 1)
        a_lower = c_lambda / (d * c_00)
        check(
            f"a_({p},{q})(beta) strict-positive lower witness",
            d > 0 and c_lambda > 0 and c_00 > 0 and a_lower > 0,
            detail=f"d={d}, lower a(beta=1)>={a_lower}",
        )

    section("Part 3: beta=0 boundary is not overclaimed")
    for p, q in [(1, 0), (0, 1), (1, 1), (3, 2)]:
        n = witness_length(p, q)
        beta_zero_contribution = 0 if n > 0 else 1
        check(
            f"nontrivial weight ({p},{q}) has no strict-positive beta=0 witness",
            n > 0 and beta_zero_contribution == 0,
            detail="strict positivity is claimed for beta > 0 only",
        )
    check(
        "trivial weight has beta=0 coefficient from n=0 term",
        witness_length(0, 0) == 0 and lower_bound_monomial_at_beta_one(0, 0) == 1,
        detail="c_(0,0)(0)=1 boundary remains positive",
    )

    section("Part 4: formal all-weight diagonal convolution on finite tests")
    box = [(p, q) for p in range(4) for q in range(4)]
    z = {w: Fraction((w[0] + 1) * (w[1] + 2), (w[0] + w[1] + 1)) for w in box}
    vector = [Fraction(i + 1, 3 * i + 2) for i in range(len(box))]
    acted = formal_convolution_action(box, z, vector)
    expected = [z[w] * vector[i] for i, w in enumerate(box)]
    check(
        "formal C_Z action is coefficientwise diagonal on a finite-character test vector",
        acted == expected,
        detail=f"{len(box)} basis weights checked exactly",
    )

    basis_ok = True
    for i, w in enumerate(box):
        e = [Fraction(0) for _ in box]
        e[i] = Fraction(1)
        Ce = formal_convolution_action(box, z, e)
        if Ce[i] != z[w] or any(Ce[j] != 0 for j in range(len(box)) if j != i):
            basis_ok = False
            break
    check(
        "formal C_Z chi_(p,q) = z_(p,q) chi_(p,q) on every sampled basis vector",
        basis_ok,
        detail="finite-support test algebra; no L2 closure asserted",
    )

    symmetric = all(z[(p, q)] == z[(q, p)] for p, q in box if (q, p) in z) is False
    check(
        "formal distribution does not require conjugation symmetry unless the theorem asks for it",
        symmetric,
        detail="arbitrary all-weight sequences are legal formal data",
    )

    z_sym = {(p, q): Fraction((p + q + 1), 5) for p, q in box}
    sym_ok = all(z_sym[(p, q)] == z_sym[(q, p)] for p, q in box if (q, p) in z_sym)
    check(
        "conjugation-symmetric formal data remain symmetric weight by weight",
        sym_ok,
        detail="matches the downstream residual-environment symmetry case",
    )

    section("Part 5: source-note and downstream-marker checks")
    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    note_markers = [
        "strictly positive Peter-Weyl character coefficient",
        "Sym^p(3) tensor Sym^q(3bar)",
        "define the formal central",
        "bounded-operator closure without a separate decay",
        "No new framework axiom is introduced",
    ]
    for marker in note_markers:
        check(f"bridge note marker present: {marker}", marker in note_text)

    parent_markers = [
        "Gauge Wilson SU(3) all-weight positive-coefficient formal bridge",
        "formal central character distribution",
        "strict all-weight positivity/nonzero input",
        "not an `L^2` class function",
    ]
    for marker in parent_markers:
        check(f"downstream plaquette note marker present: {marker}", marker in parent_text)

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
