#!/usr/bin/env python3
"""Exact Fraction checks for Block11 C2 rational normal form."""

from fractions import Fraction


PASS = 0
FAIL = 0


def check(name, condition):
    global PASS, FAIL
    if condition:
        PASS += 1
    else:
        FAIL += 1


def add(r, s):
    return (r[0] + s[0], r[1] + s[1])


def scale(n, r):
    return (n * r[0], n * r[1])


def refine(r, k):
    return (r[0] / k, r[1] / k)


def readout(u, v):
    return lambda r: u * r[0] + v * r[1]


def reachable_pair(p, q, r, s):
    a_piece = refine((Fraction(1), Fraction(0)), q)
    b_piece = refine((Fraction(0), Fraction(1)), s)
    return add(scale(p, a_piece), scale(r, b_piece))


def run_reachability_checks():
    samples = [
        (2, 3, 5, 7),
        (0, 5, 4, 9),
        (11, 6, 0, 8),
    ]
    for p, q, r, s in samples:
        got = reachable_pair(p, q, r, s)
        expected = (Fraction(p, q), Fraction(r, s))
        check(f"reachability {expected}", got == expected)


def run_cauchy_checks():
    I = readout(Fraction(5, 3), Fraction(7, 4))
    u = I((Fraction(1), Fraction(0)))
    v = I((Fraction(0), Fraction(1)))
    check("u coefficient witness", u == Fraction(5, 3))
    check("v coefficient witness", v == Fraction(7, 4))
    check(
        "integer union on A",
        I(scale(4, (Fraction(1), Fraction(0)))) == 4 * u,
    )
    check(
        "integer union on B",
        I(scale(6, (Fraction(0), Fraction(1)))) == 6 * v,
    )
    check(
        "refinement on A",
        I(refine((Fraction(1), Fraction(0)), 9)) == u / 9,
    )
    check(
        "refinement on B",
        I(refine((Fraction(0), Fraction(1)), 10)) == v / 10,
    )
    parent = (Fraction(7, 5), Fraction(11, 13))
    k = 8
    check("equal-subrecord refinement", k * I(refine(parent, k)) == I(parent))


def run_reconstruction_checks():
    grid = [
        (Fraction(0), Fraction(0)),
        (Fraction(1, 2), Fraction(2, 3)),
        (Fraction(5, 4), Fraction(7, 6)),
        (Fraction(9, 10), Fraction(11, 12)),
    ]
    examples = [
        readout(Fraction(1), Fraction(2)),
        readout(Fraction(3, 2), Fraction(5, 3)),
    ]
    for idx, I in enumerate(examples, start=1):
        u = I((Fraction(1), Fraction(0)))
        v = I((Fraction(0), Fraction(1)))
        for record in grid:
            check(
                f"normal form example {idx} {record}",
                I(record) == u * record[0] + v * record[1],
            )


def run_non_content_determined_counterexample():
    record_a = ("alpha", (Fraction(1, 2), Fraction(3, 4)))
    record_b = ("beta", (Fraction(1, 2), Fraction(3, 4)))
    assigned = {"alpha": Fraction(5), "beta": Fraction(6)}
    same_content = record_a[1] == record_b[1]
    different_values = assigned[record_a[0]] != assigned[record_b[0]]
    check("same content pair", same_content)
    check("identity-dependent values differ", different_values)
    check("counterexample outside class", same_content and different_values)


def run_degenerate_checks():
    ignores_a = readout(Fraction(0), Fraction(5))
    ignores_b = readout(Fraction(7), Fraction(0))
    zero = readout(Fraction(0), Fraction(0))
    r = (Fraction(2, 3), Fraction(4, 5))
    check("degenerate ignores A", ignores_a(r) == Fraction(5) * r[1])
    check("degenerate ignores B", ignores_b(r) == Fraction(7) * r[0])
    check("zero readout", zero(r) == 0)


def main():
    run_reachability_checks()
    run_cauchy_checks()
    run_reconstruction_checks()
    run_non_content_determined_counterexample()
    run_degenerate_checks()
    print("Block11 C2 weighting normal form uniqueness")
    print("checks: reachability, finite Cauchy, reconstruction, counterexample, degenerates")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
