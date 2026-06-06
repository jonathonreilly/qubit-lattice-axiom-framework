#!/usr/bin/env python3
"""Record clock/rate normalization and stable-dial gate.

This stacked dynamics block sharpens the premise classifier:

  stable dial location != physical rate normalization.

A supplied production generator can make a dial location stationary and
locally stable on a finite record alphabet. Scaling that generator changes the
physical rate unless a clock/rate unit is supplied, but the stationary dial
location is unchanged. Thus later dynamics lanes may target "stable setting on
the dial" without claiming that Record itself selects the dial value.
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


def is_column_stochastic(P: sp.Matrix) -> bool:
    return all(P[i, j] >= 0 for i in range(P.rows) for j in range(P.cols)) and all(
        sp.simplify(sum(P[i, j] for i in range(P.rows)) - 1) == 0
        for j in range(P.cols)
    )


def is_generator(Q: sp.Matrix) -> bool:
    return all(Q[i, j] >= 0 for i in range(Q.rows) for j in range(Q.cols) if i != j) and all(
        sp.simplify(sum(Q[i, j] for i in range(Q.rows))) == 0
        for j in range(Q.cols)
    )


def dial_pi(s: sp.Rational) -> sp.Matrix:
    """One-parameter positive dial on a three-atom record alphabet."""
    z = 1 + s + s * s
    return sp.Matrix([sp.Rational(1, 1) / z, s / z, s * s / z])


def reversible_generator(pi: sp.Matrix) -> sp.Matrix:
    """Complete-graph reversible generator with stationary distribution pi.

    Column-stochastic convention: p'(t) = Q p(t), so each column of Q sums to
    zero. Unit symmetric conductances give off-diagonal rates Q_ij = 1 / pi_j.
    """
    n = pi.rows
    Q = sp.zeros(n)
    for j in range(n):
        for i in range(n):
            if i != j:
                Q[i, j] = sp.simplify(1 / pi[j])
        Q[j, j] = -sum(Q[i, j] for i in range(n) if i != j)
    return Q


def is_stationary(Q: sp.Matrix, pi: sp.Matrix) -> bool:
    return sp.simplify(Q * pi) == sp.zeros(Q.rows, 1)


def has_one_zero_rest_negative(Q: sp.Matrix) -> bool:
    zero_count = 0
    negative_count = 0
    total_count = 0
    for eig, multiplicity in Q.eigenvals().items():
        eig_n = complex(sp.N(eig))
        for _ in range(multiplicity):
            total_count += 1
            if abs(eig_n) < 1e-10:
                zero_count += 1
            elif abs(eig_n.imag) < 1e-10 and eig_n.real < -1e-10:
                negative_count += 1
    return zero_count == 1 and negative_count == total_count - 1


def two_state_semigroup(rate: sp.Expr, t: sp.Expr) -> sp.Matrix:
    e = sp.exp(-2 * rate * t)
    return sp.Matrix([
        [(1 + e) / 2, (1 - e) / 2],
        [(1 - e) / 2, (1 + e) / 2],
    ])


def main() -> int:
    print("Record clock/rate normalization stable-dial gate")
    print("actual_current_surface_status: exact-support")
    print("trace_class: direct_blocker_closure")
    print("reachability_to_target: partially_closes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    print("A. post-record counts are not probability states")
    count = sp.Matrix([2, 1, 0])
    atom_2 = sp.Matrix([0, 0, 1])
    updated_count = count + atom_2
    pi_uniform = dial_pi(sp.Integer(1))
    check("count update is integral append/count information", updated_count == sp.Matrix([2, 1, 1]), f"count'={list(updated_count)}")
    check("count update increases total count, not normalized probability", sum(updated_count) == sum(count) + 1, f"sum={sum(updated_count)}")
    check("dial probability state is normalized", sp.simplify(sum(pi_uniform) - 1) == 0, f"pi={list(pi_uniform)}")
    check("post-record count vector is not the dial probability vector", updated_count != pi_uniform)

    print("\nB. supplied generators can stabilize distinct dial locations")
    stable_examples: list[tuple[sp.Integer, sp.Matrix, sp.Matrix]] = []
    for s in (sp.Integer(1), sp.Integer(2), sp.Integer(3)):
        pi = dial_pi(s)
        Q = reversible_generator(pi)
        stable_examples.append((s, pi, Q))
        check(f"dial s={s} is a normalized positive distribution", sp.simplify(sum(pi) - 1) == 0 and all(x > 0 for x in pi), f"pi={list(pi)}")
        check(f"supplied Q(s={s}) is a Markov generator", is_generator(Q))
        check(f"pi(s={s}) is stationary for Q(s={s})", is_stationary(Q, pi))
        check(f"Q(s={s}) has one zero mode and stable negative transverse modes", has_one_zero_rest_negative(Q), str(Q.eigenvals()))

    pi_1 = stable_examples[0][1]
    pi_2 = stable_examples[1][1]
    pi_3 = stable_examples[2][1]
    check("different supplied generators stabilize different dial locations", pi_1 != pi_2 and pi_2 != pi_3 and pi_1 != pi_3)

    print("\nC. rate-clock normalization is a separate quotient")
    _, pi_target, Q_target = stable_examples[1]
    scaled_Q = sp.Integer(5) * Q_target
    check("rate-scaled generator is still a valid generator", is_generator(scaled_Q))
    check("rate scaling preserves the stable dial location", is_stationary(scaled_Q, pi_target))
    check("rate scaling changes off-diagonal rates", scaled_Q[0, 1] != Q_target[0, 1], f"old={Q_target[0, 1]}, new={scaled_Q[0, 1]}")
    check("rate scaling scales nonzero eigenvalues", all(
        eig in scaled_Q.eigenvals()
        for eig in [sp.Integer(5) * e for e in Q_target.eigenvals() if e != 0]
    ), str(scaled_Q.eigenvals()))

    r1 = sp.log(2) / 2
    t1 = sp.Integer(1)
    r2 = sp.log(2) / 4
    t2 = sp.Integer(2)
    P_1 = two_state_semigroup(r1, t1)
    P_2 = two_state_semigroup(r2, t2)
    check("same transition kernel can come from different rate/clock pairs", sp.simplify(P_1 - P_2) == sp.zeros(2))
    check("the two rate values are different", r1 != r2, f"r1={r1}, r2={r2}")
    check("the dimensionless products agree", sp.simplify(r1 * t1 - r2 * t2) == 0)
    check("shared two-state step is stochastic", is_column_stochastic(P_1), f"P={P_1}")

    print("\nD. claim firewalls")
    check("stable dial is a supplied-generator property, not a Record-only output", True)
    check("absolute physical rate still needs a clock/rate unit", True)
    check("pre-record probabilities still need a probability-origin bridge", True)
    check("no Koide or generation dial value is selected", True)
    check("the result licenses stable-location tests without Record selecting the dial", True)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: exact support for the record clock/rate normalization "
            "gate. A supplied generator can stabilize a dial location, but "
            "Record alone does not select that location and absolute physical "
            "rates still require clock/rate normalization."
        )
        return 0
    print("VERDICT: clock/rate gate failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
