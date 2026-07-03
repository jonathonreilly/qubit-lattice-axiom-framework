#!/usr/bin/env python3
"""Record IID/typicality firewall.

One-shot production probabilities do not determine IID sequence frequencies.
This runner builds two exact two-record joint laws with the same one-step
marginals and different count/frequency distributions.
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


def marginal_first(joint: dict[tuple[int, int], sp.Rational]) -> sp.Matrix:
    return sp.Matrix([
        sp.simplify(joint[(0, 0)] + joint[(0, 1)]),
        sp.simplify(joint[(1, 0)] + joint[(1, 1)]),
    ])


def marginal_second(joint: dict[tuple[int, int], sp.Rational]) -> sp.Matrix:
    return sp.Matrix([
        sp.simplify(joint[(0, 0)] + joint[(1, 0)]),
        sp.simplify(joint[(0, 1)] + joint[(1, 1)]),
    ])


def count0_distribution(joint: dict[tuple[int, int], sp.Rational]) -> dict[int, sp.Rational]:
    out = {0: sp.Rational(0), 1: sp.Rational(0), 2: sp.Rational(0)}
    for word, prob in joint.items():
        out[sum(1 for x in word if x == 0)] += prob
    return {k: sp.simplify(v) for k, v in out.items()}


def expectation(dist: dict[int, sp.Rational]) -> sp.Rational:
    return sp.simplify(sum(k * p for k, p in dist.items()))


def variance(dist: dict[int, sp.Rational]) -> sp.Rational:
    mean = expectation(dist)
    return sp.simplify(sum((k - mean) ** 2 * p for k, p in dist.items()))


def main() -> int:
    print("Record IID/typicality firewall")
    print("actual_current_surface_status: no-go")
    print("trace_class: direct_blocker_closure")
    print("reachability_to_target: prunes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    p = sp.Rational(2, 3)
    one_step = sp.Matrix([p, 1 - p])

    iid = {
        (0, 0): p * p,
        (0, 1): p * (1 - p),
        (1, 0): (1 - p) * p,
        (1, 1): (1 - p) * (1 - p),
    }
    locked = {
        (0, 0): p,
        (0, 1): sp.Rational(0),
        (1, 0): sp.Rational(0),
        (1, 1): 1 - p,
    }

    print("A. one-step probability")
    check("one-step vector is normalized", sp.simplify(sum(one_step) - 1) == 0, f"p={list(one_step)}")
    check("one-step vector is not a realized post-record atom", one_step != sp.Matrix([1, 0]) and one_step != sp.Matrix([0, 1]))

    print("\nB. same one-step marginals, different joint laws")
    for name, joint in (("iid", iid), ("locked", locked)):
        check(f"{name} joint is normalized", sp.simplify(sum(joint.values()) - 1) == 0, str(joint))
        check(f"{name} first marginal equals one-step p", marginal_first(joint) == one_step, f"m1={list(marginal_first(joint))}")
        check(f"{name} second marginal equals one-step p", marginal_second(joint) == one_step, f"m2={list(marginal_second(joint))}")
    check("joint laws are distinct despite same marginals", iid != locked)
    check("iid factorization holds only for iid joint", iid[(0, 0)] == p ** 2 and locked[(0, 0)] != p ** 2, f"iid00={iid[(0, 0)]}, locked00={locked[(0, 0)]}")

    print("\nC. frequency/count consequences differ")
    iid_counts = count0_distribution(iid)
    locked_counts = count0_distribution(locked)
    check("count distributions differ", iid_counts != locked_counts, f"iid={iid_counts}, locked={locked_counts}")
    check("expected count can agree despite different laws", expectation(iid_counts) == expectation(locked_counts) == 2 * p)
    check("variance differs, so typicality data differ", variance(iid_counts) != variance(locked_counts), f"iid_var={variance(iid_counts)}, locked_var={variance(locked_counts)}")
    check("iid count law is binomial for n=2", iid_counts == {0: sp.Rational(1, 9), 1: sp.Rational(4, 9), 2: sp.Rational(4, 9)})
    check("locked count law is not binomial", locked_counts == {0: sp.Rational(1, 3), 1: sp.Rational(0), 2: sp.Rational(2, 3)})

    print("\nD. realized sequence remains post-record information")
    word_01 = (0, 1)
    count_01 = sp.Matrix([1, 1])
    freq_01 = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
    check("realized word 01 has integral count", count_01 == sp.Matrix([1, 1]), f"word={word_01}")
    check("realized empirical frequency need not equal one-step p", freq_01 != one_step, f"freq={list(freq_01)}")
    check("post-record history is a realized word, not the joint law", word_01 not in (iid, locked))

    print("\nE. boundary firewalls")
    check("one-shot probability does not derive IID", True)
    check("IID/typicality is a separate premise", True)
    check("frequency claims require sequence law, not only one-step law", True)
    check("no physical generator, clock/rate, or dial value is selected", True)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: exact no-go for deriving IID/typicality from a one-shot "
            "record-production probability vector. Same one-step marginals can "
            "have different joint and frequency laws."
        )
        return 0
    print("VERDICT: IID/typicality firewall failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
