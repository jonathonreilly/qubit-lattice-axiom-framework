#!/usr/bin/env python3
"""Independent referee for moving-what-fixes-the-scale a2.

Six-axis stencil, exact. The author's script is not called.
"""
import itertools

import sympy as sp

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def kind(a, b):
    d = sum(x * y for x, y in zip(AX[a], AX[b]))
    return "eq" if d == 1 else ("opp" if d == -1 else "orth")


def main():
    p, q, r, c = sp.symbols("p q r c", positive=True)
    S = p + q + 4 * r

    def omega(a, s):
        k = kind(a, s)
        return p if k == "eq" else (q if k == "opp" else r)

    # degree 1: sum_s omega(a,s) = S for every a
    ok1 = all(sp.simplify(sum(omega(a, s) for s in range(6)) - S) == 0 for a in range(6))
    c0 = sp.solve(sp.Eq(c * S / 6, 1), c)
    check("degree 1: one neighbour gives c*S/6, equal to 1 only at c=6/S",
          ok1 and c0 == [6 / S])

    def pair_sum(a, b):
        return sp.simplify(sum(omega(a, s) * omega(b, s) for s in range(6)))

    # one representative of each class
    eq = pair_sum(0, 0)
    opp = pair_sum(0, 1)
    orth = pair_sum(0, 2)
    check("degree 2 sums are p^2+q^2+4r^2, 2pq+4r^2, 2r(p+q)+2r^2",
          sp.expand(eq - (p ** 2 + q ** 2 + 4 * r ** 2)) == 0
          and sp.expand(opp - (2 * p * q + 4 * r ** 2)) == 0
          and sp.expand(orth - (2 * r * (p + q) + 2 * r ** 2)) == 0)

    # every pair of the same class agrees, and the three classes meet only at p=q=r
    ok_class = True
    for a, b in itertools.product(range(6), repeat=2):
        got = pair_sum(a, b)
        ok_class &= got == {"eq": eq, "opp": opp, "orth": orth}[kind(a, b)]
    diff_eo = sp.factor(eq - opp)
    diff_er = sp.factor(eq - orth)
    check("the three branches agree for every pair of that class, and only when p=q=r",
          ok_class and diff_eo == (p - q) ** 2
          and sp.simplify(diff_er.subs({q: p}) - 2 * (p - r) ** 2) == 0,
          f"eq-opp {diff_eo}")

    ident = sp.factor(12 * r * (p + q + r) - S ** 2)
    check("at c0 the orthogonal weight is 1 iff p+q=2r",
          ident == -(p + q - 2 * r) ** 2)

    triples = {("3,1,2"): (3, 1, 2), ("7,3,5"): (7, 3, 5), ("5,2,4"): (5, 2, 4), ("5,1,1"): (5, 1, 1)}
    flags = {name: sp.Integer(pp + qq - 2 * rr) == 0 for name, (pp, qq, rr) in triples.items()}
    check("(3,1,2) and (7,3,5) lie on p+q=2r; (5,2,4) and (5,1,1) do not",
          flags == {"3,1,2": True, "7,3,5": True, "5,2,4": False, "5,1,1": False},
          str(flags))

    # fully averaged: each neighbour uniform, and the record uniform
    j = sp.symbols("j", integer=True, positive=True)
    # (c^j / 6^{j+1}) * sum_s (sum_a omega(a,s))^j = (c S / 6)^j
    row = sp.simplify(sum(omega(0, s) for s in range(6)))  # same for every content, already checked
    averaged = sp.simplify((c ** j / 6 ** (j + 1)) * 6 * row ** j)
    check("averaging the neighbours too gives [c S/6]^j, hence 1 at c0 for every j",
          averaged == (c * S / 6) ** j)

    print()
    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0])
        raise SystemExit(1)
    print("SUMMARY: confirmed - an empty site matches an averaged record at exactly c0 for one neighbour; the three degree-2 branches agree only if p=q=r; averaging the neighbours as well gives (c S/6)^j, which is 1 at c0 for every j.")
    print("HIT: confirmed - c0=6/(p+q+4r) is the unique one-bond scale; degree 2 takes the three values p^2+q^2+4r^2, 2pq+4r^2 and 2r(p+q)+2r^2; the orthogonal branch equals 1 at c0 iff p+q=2r, which holds for (3,1,2) and (7,3,5) but not (5,2,4).")


if __name__ == "__main__":
    main()
