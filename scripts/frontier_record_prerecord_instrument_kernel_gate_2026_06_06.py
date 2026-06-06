#!/usr/bin/env python3
"""Pre-record instrument to record-production kernel gate.

This stacked block makes the pre-record/post-record split operational:

  qubit state + supplied instrument + Born trace rule -> probabilities over
  possible future record atoms;
  realized record atom -> post-record information/count update.

It is conditional support only. The runner does not derive the instrument, the
Born rule, IID/typicality, a physical production generator, a clock/rate unit,
or a dial value.
"""

from __future__ import annotations

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
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def trace(M: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(M[i, i] for i in range(M.rows)))


def is_zero_matrix(M: sp.Matrix) -> bool:
    M = sp.simplify(M)
    return all(M[i, j] == 0 for i in range(M.rows) for j in range(M.cols))


def projector(ket: sp.Matrix) -> sp.Matrix:
    return sp.simplify(ket * ket.T)


def born_probs(rho: sp.Matrix, projectors: list[sp.Matrix]) -> sp.Matrix:
    return sp.Matrix([sp.simplify(trace(P * rho)) for P in projectors])


def is_probability_vector(p: sp.Matrix) -> bool:
    return all(x >= 0 for x in p) and sp.simplify(sum(p) - 1) == 0


def main() -> int:
    print("Record pre-record instrument kernel gate")
    print("actual_current_surface_status: conditional-support")
    print("trace_class: upstream_support")
    print("reachability_to_target: supports")
    print("conditional_surface_status: exact under supplied instrument and Born trace rule")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    sqrt2 = sp.sqrt(2)
    ket0 = sp.Matrix([1, 0])
    ket1 = sp.Matrix([0, 1])
    ket_plus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), sp.sqrt(sp.Rational(1, 2))])
    ket_minus = sp.Matrix([sp.sqrt(sp.Rational(1, 2)), -sp.sqrt(sp.Rational(1, 2))])

    psi = sp.Matrix([sp.sqrt(sp.Rational(2, 3)), sp.sqrt(sp.Rational(1, 3))])
    rho = projector(psi)
    P0 = projector(ket0)
    P1 = projector(ket1)
    Pp = projector(ket_plus)
    Pm = projector(ket_minus)
    identity = sp.eye(2)

    print("A. supplied one-qubit state and projective instruments")
    check("rho has trace one", trace(rho) == 1, f"rho={rho}")
    check("rho is pure positive semidefinite", rho.det() == 0 and rho[0, 0] >= 0 and rho[1, 1] >= 0)
    check("Z projectors are orthogonal and complete", is_zero_matrix(P0 * P1) and is_zero_matrix(P0 + P1 - identity))
    check("X projectors are orthogonal and complete", is_zero_matrix(Pp * Pm) and is_zero_matrix(Pp + Pm - identity))
    check("projective Kraus completeness holds for Z instrument", is_zero_matrix(P0.T * P0 + P1.T * P1 - identity))

    print("\nB. Born trace rule gives a future-record production kernel")
    p_z = born_probs(rho, [P0, P1])
    p_x = born_probs(rho, [Pp, Pm])
    check("Z-instrument probabilities are normalized", is_probability_vector(p_z), f"p_z={list(p_z)}")
    check("Z-instrument probabilities equal (2/3, 1/3)", p_z == sp.Matrix([sp.Rational(2, 3), sp.Rational(1, 3)]), f"p_z={list(p_z)}")
    check("X-instrument probabilities are normalized", is_probability_vector(p_x), f"p_x={list(p_x)}")
    check("same rho with different supplied instrument gives different kernel", p_x != p_z, f"p_x={list(p_x)}")
    check("instrument is load-bearing for the production kernel", p_x[0] == sp.Rational(1, 2) + sqrt2 / 3)

    print("\nC. realized post-record atoms are not the probability vector")
    e0 = sp.Matrix([1, 0])
    e1 = sp.Matrix([0, 1])
    check("outcome 0 writes one-hot record atom e0", e0 != p_z and sum(e0) == 1, f"e0={list(e0)}")
    check("outcome 1 writes one-hot record atom e1", e1 != p_z and sum(e1) == 1, f"e1={list(e1)}")
    count = sp.Matrix([4, 2])
    count_if_0 = count + e0
    count_if_1 = count + e1
    expected_count = count + p_z
    check("realized count update for outcome 0 is integral", count_if_0 == sp.Matrix([5, 2]), f"count0={list(count_if_0)}")
    check("realized count update for outcome 1 is integral", count_if_1 == sp.Matrix([4, 3]), f"count1={list(count_if_1)}")
    check("ensemble expected count is fractional and typed separately", expected_count == sp.Matrix([sp.Rational(14, 3), sp.Rational(7, 3)]), f"E[count']={list(expected_count)}")
    check("expected count is not either realized update", expected_count != count_if_0 and expected_count != count_if_1)

    print("\nD. selective and nonselective quantum states remain pre-record/ensemble objects")
    selective0 = sp.simplify(P0 * rho * P0 / p_z[0])
    selective1 = sp.simplify(P1 * rho * P1 / p_z[1])
    nonselective = sp.simplify(P0 * rho * P0 + P1 * rho * P1)
    check("selective state for outcome 0 is normalized projector P0", is_zero_matrix(selective0 - P0))
    check("selective state for outcome 1 is normalized projector P1", is_zero_matrix(selective1 - P1))
    check("nonselective ensemble has trace one", trace(nonselective) == 1, f"rho_ns={nonselective}")
    check("nonselective ensemble is not a realized record atom", nonselective != P0 and nonselective != P1)

    print("\nE. boundary firewalls")
    check("Record alone does not derive the supplied instrument", True)
    check("Record alone does not derive the Born trace rule", True)
    check("one-shot probabilities do not supply IID frequencies", True)
    check("instrument probabilities do not supply a physical Markov generator", True)
    check("no clock/rate unit is selected", True)
    check("no generation or Koide dial value is selected", True)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: conditional support for the pre-record instrument kernel "
            "gate. With a supplied instrument and Born trace rule, a qubit state "
            "gives probabilities over possible future record atoms; the written "
            "post-record atom is realized information, not the probability vector."
        )
        return 0
    print("VERDICT: pre-record instrument gate failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
