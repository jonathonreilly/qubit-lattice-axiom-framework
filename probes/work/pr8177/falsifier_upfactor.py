#!/usr/bin/env python3
"""J:falsifier:PR8177 — independent symbolic check of T3.1 up-factor (D1).

For n successor positions each empty / processed (x_P U) / amplified (x_A U),
the generating function with at most one processed child is
  (1 + x_A U)^n + n x_P U (1 + x_A U)^{n-1}.
HIT if this identity fails for n=2 or n=3.
"""
import sympy as sp

xP, xA, U = sp.symbols("x_P x_A U", positive=True)


def full_factor(n: int):
    """Sum over configs with k processed children in {0,1}."""
    # empty weight 1, processed xP*U, amplified xA*U, mutually exclusive per slot
    # generating function per slot if unrestricted: 1 + xP U + xA U
    # restricted: expand and drop terms with two or more processed.
    slot = 1 + xP * U + xA * U
    unrestricted = sp.expand(slot**n)
    # subtract configs with >=2 processed: choose k>=2 slots processed, rest empty or amp
    rest = 1 + xA * U
    extra = 0
    for k in range(2, n + 1):
        extra += sp.binomial(n, k) * (xP * U) ** k * sp.expand(rest ** (n - k))
    return sp.expand(unrestricted - extra)


def claimed(n: int):
    return sp.expand((1 + xA * U) ** n + n * xP * U * (1 + xA * U) ** (n - 1))


def main() -> None:
    hits = []
    for n in (2, 3, 4):
        a, b = full_factor(n), claimed(n)
        ok = sp.simplify(a - b) == 0
        print(f"n={n} identity holds: {ok}")
        print(f"  claimed: {b}")
        if not ok:
            hits.append(f"n={n} claimed {b} != derived {a}")
    if hits:
        for h in hits:
            print("HIT:", h)
        print("SUMMARY: up-factor falsifier FIRED:", "; ".join(hits))
    else:
        print(
            "SUMMARY: up-factor falsifier did not fire: "
            "(1+x_A U)^n + n x_P U (1+x_A U)^{n-1} matches the "
            "at-most-one-processed-child generating function for n=2,3,4"
        )


if __name__ == "__main__":
    main()
