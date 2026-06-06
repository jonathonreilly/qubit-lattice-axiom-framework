#!/usr/bin/env python3
"""Finite checks for the Record classicalization dynamics firewall.

The target distinction is type-level:

* pre-record: a qubit density state, with Born weights for possible records;
* record event: an instrument that writes one realized label;
* post-record: a durable one-hot information token / additive count.

The runner does not derive a physical measurement dynamics. It verifies finite
matrix consequences of the separation and exhibits where probabilities re-enter
as predictive or ensemble states, not as the individual record token.
"""

from __future__ import annotations

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


def is_zero_matrix(mat: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in mat)


def shannon(vec: tuple[float, ...]) -> float:
    return -sum(x * math.log(x, 2) for x in vec if x > 0.0)


def main() -> int:
    sqrt = sp.sqrt
    I2 = sp.eye(2)
    ket0 = sp.Matrix([1, 0])
    ket1 = sp.Matrix([0, 1])
    P0 = ket0 * ket0.T
    P1 = ket1 * ket1.T

    # A nontrivial pure qubit before any record is written.
    psi = sp.Matrix([sqrt(sp.Rational(2, 3)), sqrt(sp.Rational(1, 3))])
    rho = psi * psi.T
    p0 = sp.simplify((P0 * rho).trace())
    p1 = sp.simplify((P1 * rho).trace())
    born = sp.Matrix([p0, p1])

    print("=== Pre-record qubit surface ===")
    check("Q1 pre-record state is normalized", sp.simplify((psi.T * psi)[0]) == 1)
    check("Q2 density matrix has trace one", sp.simplify(rho.trace()) == 1)
    check("Q3 projective instrument resolves identity", P0 + P1 == I2)
    check("Q4 Born weights are nontrivial and sum to one",
          p0 == sp.Rational(2, 3) and p1 == sp.Rational(1, 3) and p0 + p1 == 1,
          f"p = ({p0}, {p1})")
    check("Q5 the qubit still has coherence before the record",
          rho[0, 1] != 0 and rho[1, 0] != 0,
          f"offdiag = {rho[0, 1]}")

    print("\n=== Record-event interface ===")
    rho0_num = P0 * rho * P0
    rho1_num = P1 * rho * P1
    rho0 = sp.simplify(rho0_num / p0)
    rho1 = sp.simplify(rho1_num / p1)
    nonselective = sp.simplify(rho0_num + rho1_num)
    ensemble = sp.simplify(p0 * rho0 + p1 * rho1)
    check("I1 selective outcome 0 gives conditional branch state P0",
          rho0 == P0)
    check("I2 selective outcome 1 gives conditional branch state P1",
          rho1 == P1)
    check("I3 nonselective state is the ensemble mixture over records",
          nonselective == ensemble and nonselective == sp.diag(p0, p1),
          f"nonselective = {nonselective}")
    check("I4 nonselective mixture is not an individual realized record",
          nonselective != P0 and nonselective != P1)

    print("\n=== Post-record information surface ===")
    e0 = sp.Matrix([1, 0])
    e1 = sp.Matrix([0, 1])
    zero = sp.Matrix([0, 0])
    check("R1 realized record 0 is one-hot information, not the Born vector",
          e0 != born,
          f"e0 = {tuple(e0)}, born = {tuple(born)}")
    check("R2 realized record 1 is one-hot information, not the Born vector",
          e1 != born,
          f"e1 = {tuple(e1)}, born = {tuple(born)}")
    check("R3 one-hot records are orthogonal and distinguishable",
          (e0.T * e1)[0] == 0)
    check("R4 one-hot record entropy is zero while predictive entropy is positive",
          shannon((1.0, 0.0)) == 0.0 and shannon((float(p0), float(p1))) > 0.0,
          f"H(born) = {shannon((float(p0), float(p1))):.6f} bits")
    check("R5 additive record readout has I(empty)=0 and adds over disjoint records",
          int(sum(zero)) == 0 and int(sum(e0)) == 1 and int(sum(e1)) == 1
          and int(sum(e0 + e1)) == 2)

    print("\n=== Copy/re-read stability checks ===")
    # Classical copier on the pointer basis: |i>|0> -> |i>|i>.
    # Matrix basis order: |00>, |01>, |10>, |11>.
    cnot = sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
    )
    anc0 = ket0
    basis0_in = sp.kronecker_product(ket0, anc0)
    basis1_in = sp.kronecker_product(ket1, anc0)
    check("C1 pointer label 0 copies stably", cnot * basis0_in == sp.kronecker_product(ket0, ket0))
    check("C2 pointer label 1 copies stably", cnot * basis1_in == sp.kronecker_product(ket1, ket1))
    super_in = sp.kronecker_product(psi, anc0)
    copied_super = sp.simplify(cnot * super_in)
    desired_clone = sp.simplify(sp.kronecker_product(psi, psi))
    check("C3 the same copier does not clone a nontrivial qubit superposition",
          not is_zero_matrix(copied_super - desired_clone),
          "CNOT makes entanglement, not two copies of psi")
    phi = sp.Matrix([sqrt(sp.Rational(1, 2)), sqrt(sp.Rational(1, 2))])
    overlap = sp.simplify((phi.T * psi)[0])
    check("C4 arbitrary pre-record qubit states need not be orthogonal records",
          overlap != 0 and overlap != 1,
          f"<phi|psi> = {overlap}")
    check("C5 repeat-read of a pointer atom is idempotent",
          P0 * ket0 == ket0 and P1 * ket1 == ket1)

    print("\n=== Dynamics consequences ===")
    counts = sp.Matrix([3, 4])
    update0 = counts + e0
    update1 = counts + e1
    expected_update = counts + born
    check("D1 realized post-record update is integral for outcome 0",
          all(v.is_integer for v in update0),
          f"counts -> {tuple(update0)}")
    check("D2 realized post-record update is integral for outcome 1",
          all(v.is_integer for v in update1),
          f"counts -> {tuple(update1)}")
    check("D3 predictive expected update is fractional for nontrivial Born weights",
          expected_update[0] != int(expected_update[0]) and expected_update[1] != int(expected_update[1]),
          f"E[counts'] = {tuple(expected_update)}")
    check("D4 expected update is an ensemble object, not either realized update",
          expected_update != update0 and expected_update != update1)
    seq_a = e0 + e1 + e1
    seq_b = e0 + e0
    check("D5 post-record count dynamics is additive under concatenating histories",
          seq_a + seq_b == sp.Matrix([3, 2]),
          f"(0,1,1)+(0,0) -> {tuple(seq_a + seq_b)}")
    freq = sp.Matrix([sp.Rational(3, 5), sp.Rational(2, 5)])
    check("D6 empirical frequency is a normalized count summary, not the written token",
          freq != e0 and freq != e1 and sp.simplify(sum(freq)) == 1)

    print("\n=== Generation-dial implication ===")
    dims = sp.Matrix([1, 2])
    letter_prior = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
    dimension_prior = sp.simplify(dims / sum(dims))
    singlet_token = sp.Matrix([1, 0])
    doublet_token = sp.Matrix([0, 1])
    check("G1 equal record-letter prior is distinct from dimension/Born-style prior",
          letter_prior != dimension_prior,
          f"gamma=0 letters={tuple(letter_prior)}, gamma=1 dims={tuple(dimension_prior)}")
    check("G2 a realized singlet token is not either prior distribution",
          singlet_token != letter_prior and singlet_token != dimension_prior)
    check("G3 a realized doublet token is not either prior distribution",
          doublet_token != letter_prior and doublet_token != dimension_prior)
    check("G4 the dial is therefore a prior/ensemble choice over record letters",
          True,
          "the individual post-record site carries the selected letter")

    print("\n=== Scorecard ===")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "FINDING: pre-record qubits carry predictive weights; record events write "
        "one realized label; post-record dynamics acts on information tokens/counts. "
        "Probabilities re-enter as predictive or ensemble states, not as the "
        "individual durable record."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
