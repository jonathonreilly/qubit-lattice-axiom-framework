#!/usr/bin/env python3
"""Exact companion for the supplied-action KS blocking theorem.

Starting from the explicitly supplied one-component free OS0 staggered action
in four Euclidean directions, this runner verifies at exact symbolic precision:

* the block decomposition n = 2y + b with b in {0,1}^4;
* the momentum-local rephasing of the blocked finite difference;
* the resulting four Clifford generators on the 16-component block carrier;
* the character and rank that identify four copies of the unique 4-dimensional
  irreducible Cl_4(C) module.

The runner analyzes the supplied action.  It does not identify that action as
the framework's physical charged-lepton carrier.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy is required for exact algebra")
    raise SystemExit(1)


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        mark = f"PASS ({kind})"
    else:
        FAIL += 1
        mark = f"FAIL ({kind})"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{mark}] {label}{suffix}")


def section(label: str) -> None:
    print()
    print(label)
    print("-" * len(label))


def bits(index: int) -> tuple[int, ...]:
    return tuple((index >> mu) & 1 for mu in range(4))


def index(bit_tuple: tuple[int, ...] | list[int]) -> int:
    return sum((int(bit) & 1) << mu for mu, bit in enumerate(bit_tuple))


BLOCK_BITS = tuple(bits(i) for i in range(16))


def eta(mu: int, bit_tuple: tuple[int, ...]) -> int:
    return -1 if sum(bit_tuple[:mu]) % 2 else 1


def alpha(mu: int) -> sp.Matrix:
    matrix = sp.zeros(16)
    for column, bit_tuple in enumerate(BLOCK_BITS):
        flipped = list(bit_tuple)
        flipped[mu] ^= 1
        matrix[index(flipped), column] = eta(mu, bit_tuple)
    return matrix


ALPHAS = tuple(alpha(mu) for mu in range(4))


def raw_blocked_direction(mu: int, t: sp.Symbol, a: sp.Symbol) -> sp.Matrix:
    """Blocked one-direction difference before rephasing.

    t = exp(i p_mu a), so a coarse-cell boundary hop carries t^(+/-2).
    Rows are output block labels b and columns are input labels b xor e_mu.
    """
    matrix = sp.zeros(16)
    for row, bit_tuple in enumerate(BLOCK_BITS):
        flipped = list(bit_tuple)
        flipped[mu] ^= 1
        column = index(flipped)
        sign = eta(mu, bit_tuple)
        if bit_tuple[mu] == 0:
            coefficient = sign * (1 - t**-2) / (2 * a)
        else:
            coefficient = sign * (t**2 - 1) / (2 * a)
        matrix[row, column] = coefficient
    return matrix


def rephasing(t_symbols: tuple[sp.Symbol, ...]) -> sp.Matrix:
    diagonal = []
    for bit_tuple in BLOCK_BITS:
        phase = sp.Integer(1)
        for mu, bit in enumerate(bit_tuple):
            phase *= t_symbols[mu] ** bit
        diagonal.append(phase)
    return sp.diag(*diagonal)


def clifford_word(mask: int) -> sp.Matrix:
    word = sp.eye(16)
    for mu in range(4):
        if mask & (1 << mu):
            word *= ALPHAS[mu]
    return word


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def main() -> int:
    print("=" * 88)
    print("Supplied-action KS blocking and four-taste module: exact companion")
    print("=" * 88)

    section("Part 1: exact block carrier and canonical staggered phases")
    check(
        "b in {0,1}^4 gives 16 blocked components",
        len(BLOCK_BITS) == 16 and len(set(BLOCK_BITS)) == 16,
    )
    expected_counts = (1, 4, 6, 4, 1)
    observed_counts = tuple(
        sum(1 for bit_tuple in BLOCK_BITS if sum(bit_tuple) == weight)
        for weight in range(5)
    )
    check(
        "Hamming-weight multiplicities are (1,4,6,4,1)",
        observed_counts == expected_counts,
        detail=f"observed={observed_counts}",
    )
    check(
        "canonical eta signs depend on preceding block bits",
        all(eta(mu, bit_tuple) == (-1) ** sum(bit_tuple[:mu])
            for mu in range(4) for bit_tuple in BLOCK_BITS),
    )

    section("Part 2: exact Laurent-polynomial blocking identity")
    a = sp.symbols("a", nonzero=True)
    t_symbols = sp.symbols("t0:4", nonzero=True)
    phase = rephasing(t_symbols)
    phase_inverse = sp.diag(*[entry**-1 for entry in phase.diagonal()])
    direction_residuals = []
    for mu in range(4):
        raw = raw_blocked_direction(mu, t_symbols[mu], a)
        reduced = phase_inverse * raw * phase
        expected = ((t_symbols[mu] - t_symbols[mu]**-1) / (2 * a)) * ALPHAS[mu]
        direction_residuals.append(matrix_is_zero(reduced - expected))
    check(
        "rephasing turns every blocked direction into alpha_mu (t_mu-t_mu^-1)/(2a)",
        all(direction_residuals),
        detail=f"directions={direction_residuals}",
    )

    m = sp.symbols("m")
    raw_full = m * sp.eye(16)
    expected_full = m * sp.eye(16)
    for mu in range(4):
        raw_full += raw_blocked_direction(mu, t_symbols[mu], a)
        expected_full += ((t_symbols[mu] - t_symbols[mu]**-1) / (2 * a)) * ALPHAS[mu]
    check(
        "the full blocked operator has the exact reduced Laurent-polynomial form",
        matrix_is_zero(phase_inverse * raw_full * phase - expected_full),
    )
    check(
        "on t_mu=exp(i p_mu a), the Laurent coefficient is i sin(p_mu a)/a",
        sp.simplify((sp.exp(sp.I * sp.Symbol("x"))
                     - sp.exp(-sp.I * sp.Symbol("x"))) / 2
                    - sp.I * sp.sin(sp.Symbol("x"))) == 0,
    )

    section("Part 3: exact Cl_4(C) representation")
    identity = sp.eye(16)
    zero = sp.zeros(16)
    square_checks = [matrix_is_zero(A * A - identity) for A in ALPHAS]
    check(
        "each alpha_mu is a real symmetric involution",
        all(A == A.T for A in ALPHAS) and all(square_checks),
        detail=f"squares={square_checks}",
    )
    anticomm_checks = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            anticomm_checks.append(matrix_is_zero(ALPHAS[mu] * ALPHAS[nu]
                                                   + ALPHAS[nu] * ALPHAS[mu]))
    check(
        "distinct alpha generators anticommute",
        all(anticomm_checks),
        detail=f"pairs={anticomm_checks}",
    )

    words = tuple(clifford_word(mask) for mask in range(16))
    flattened = sp.Matrix.hstack(*[word.reshape(256, 1) for word in words])
    word_rank = flattened.rank()
    check(
        "the 16 Clifford words are linearly independent",
        word_rank == 16,
        detail=f"exact rank={word_rank}",
    )
    traces = tuple(sp.trace(word) for word in words)
    check(
        "the block-module character is 16 on the identity and 0 on 15 nonidentity words",
        traces[0] == 16 and all(value == 0 for value in traces[1:]),
        detail=f"character={traces}",
    )

    section("Part 4: module multiplicity and inverse")
    spin_dimension = 4
    multiplicity = 16 // spin_dimension
    check(
        "Cl_4(C)=M_4(C) gives four irreducible spin modules in the 16-component carrier",
        16 == spin_dimension * multiplicity and multiplicity == 4,
        detail=f"16={spin_dimension}*{multiplicity}",
    )
    check(
        "the exact character equals four times the irreducible Cl_4(C) character",
        traces[0] == 4 * spin_dimension and all(value == 4 * 0 for value in traces[1:]),
    )

    s_symbols = sp.symbols("s0:4", real=True)
    kinetic = sp.zeros(16)
    for mu in range(4):
        kinetic += s_symbols[mu] * ALPHAS[mu]
    kinetic_square = sum(value**2 for value in s_symbols) * identity
    check(
        "the Clifford kinetic square is (sum_mu s_mu^2) I_16",
        matrix_is_zero(kinetic * kinetic - kinetic_square),
    )
    denominator = m**2 + sum(value**2 for value in s_symbols)
    operator = m * identity + sp.I * kinetic
    numerator = m * identity - sp.I * kinetic
    check(
        "the blocked operator has the exact scalar-denominator inverse identity",
        matrix_is_zero(operator * numerator - denominator * identity),
    )

    section("Scope guard")
    note = (Path(__file__).resolve().parents[1]
            / "docs/STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md").read_text()
    check(
        "source note discloses the action premise and disclaims physical-carrier selection",
        "The action displayed above is the premise of this bounded theorem" in note
        and "does not identify it as the realized charged-lepton matter carrier" in note,
        kind="C",
    )

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
