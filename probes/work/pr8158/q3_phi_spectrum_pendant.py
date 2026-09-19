#!/usr/bin/env python3
"""J:attack-g:PR8158 — brute-force Q3 spectrum and Q2 pendant constancy.

Do NOT re-find the known Q4(a) triangle-not-a-Z^3-window HIT.

Q3: 6×6 φ has eigenvalues Z1 (constants), p−q (odd sector, 3), p+q−2r
(even zero-sum, 2); φ² = Z1² P0 + (p−q)² P_odd + (p+q−2r)² P_even;
φ² is a multiple of P0 iff p=q=r.
Q2: F of a pendant path of 2 or 3 unrecorded sites is independent of the
attachment value (same polynomial for all six v_b).
Q3(e): z cosh z − sinh z = Σ_{n≥1} 2n z^{2n+1}/(2n+1)! (truncation identity).

HIT if a spectral identity, pendant constancy, or the series fails.
Exact sympy / Fraction.
"""
from __future__ import annotations

from collections import defaultdict

import sympy as sp


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
p, q, r = sp.symbols("p q r", positive=True)


def phi_entry(s, t):
    if s == t:
        return p
    if s == (-t[0], -t[1], -t[2]):
        return q
    return r


def main():
    hits = []
    Phi = sp.zeros(6)
    for i, a in enumerate(AXES):
        for j, b in enumerate(AXES):
            Phi[i, j] = phi_entry(a, b)
    Z1 = p + q + 4 * r
    ev = Phi.eigenvals()
    got = {sp.simplify(lam): int(m) for lam, m in ev.items()}
    want_keys = {Z1: 1, p - q: 3, p + q - 2 * r: 2}
    # match by substituting a point
    pt = {p: 5, q: 2, r: 4}
    got_n = {int(sp.simplify(lam.subs(pt))): m for lam, m in got.items()}
    want_n = {int(sp.simplify(lam.subs(pt))): m for lam, m in want_keys.items()}
    print("φ eigenvalues at (5,2,4):", got_n)
    if got_n != want_n:
        hits.append(f"HIT: φ spectrum {got_n} != {want_n}")
        print(hits[-1])
    else:
        print("Q3: φ spectrum Z1, p-q (×3), p+q-2r (×2)")

    # odd sector: f(a)=-f(-a), four orthogonals cancel
    # even zero-sum: f(a)=f(-a), sum=0
    Phi2 = sp.expand(Phi * Phi)
    # P0 projector onto constants: all-ones / 6
    ones = sp.ones(6, 1)
    P0 = ones * ones.T / 6
    # check Phi * 1 = Z1 * 1
    if sp.simplify(Phi * ones - Z1 * ones) != sp.zeros(6, 1):
        hits.append("HIT: constants are not Z1-eigenvectors")
        print(hits[-1])

    # reconstruct Phi2 via spectral mapping on a generic point and as a matrix identity
    # Phi2 1 = Z1^2 1
    if sp.simplify(Phi2 * ones - Z1 ** 2 * ones) != sp.zeros(6, 1):
        hits.append("HIT: Phi2 constants not Z1^2")
        print(hits[-1])

    # odd vector e.g. f(+x)=1, f(-x)=-1, else 0
    odd = sp.Matrix([1, -1, 0, 0, 0, 0])
    if sp.simplify(Phi * odd - (p - q) * odd) != sp.zeros(6, 1):
        hits.append("HIT: odd vector not (p-q)-eigenvector")
        print(hits[-1])
    if sp.simplify(Phi2 * odd - (p - q) ** 2 * odd) != sp.zeros(6, 1):
        hits.append("HIT: Phi2 odd not (p-q)^2")
        print(hits[-1])

    even = sp.Matrix([1, 1, -1, -1, 0, 0])  # even, sum 0
    if sp.simplify(Phi * even - (p + q - 2 * r) * even) != sp.zeros(6, 1):
        hits.append("HIT: even zero-sum vector not (p+q-2r)-eigenvector")
        print(hits[-1])
    if sp.simplify(Phi2 * even - (p + q - 2 * r) ** 2 * even) != sp.zeros(6, 1):
        hits.append("HIT: Phi2 even not (p+q-2r)^2")
        print(hits[-1])

    # Phi2 is a multiple of P0 (all entries equal) iff p=q=r
    diffs = set()
    for i in range(6):
        for j in range(6):
            diffs.add(sp.expand(Phi2[i, j] - Phi2[0, 0]))
    # all entries equal iff every diff vanishes
    # at p=q=r they should
    if any(sp.simplify(d.subs({p: r, q: r})) != 0 for d in diffs):
        hits.append("HIT: Phi2 not constant on p=q=r")
        print(hits[-1])
    # at (3,1,2) not constant
    if all(sp.simplify(d.subs({p: 3, q: 1, r: 2})) == 0 for d in diffs):
        hits.append("HIT: Phi2 constant at (3,1,2) (should not be)")
        print(hits[-1])
    print("Q3: Phi2 constant iff p=q=r (checked p=q=r and (3,1,2))")

    # Q2 pendant path of length 2 and 3: F(vb) independent of vb
    def F_path(k, vb):
        """k internal unrecorded sites in a path attached at one end to vb."""
        # sites u0-u1-...-u_{k-1}, u0 attached to vb
        tot = 0
        for us in _product_axes(k):
            w = phi_entry(vb, us[0])
            for i in range(k - 1):
                w *= phi_entry(us[i], us[i + 1])
            tot += w
        return sp.expand(tot)

    def _product_axes(k):
        if k == 0:
            yield ()
            return
        for rest in _product_axes(k - 1):
            for a in AXES:
                yield (a,) + rest

    for k in (2, 3):
        polys = [F_path(k, vb) for vb in AXES]
        if not all(sp.expand(polys[i] - polys[0]) == 0 for i in range(6)):
            hits.append(f"HIT: pendant path k={k} factor depends on vb")
            print(hits[-1])
        else:
            print(f"Q2: pendant path k={k} factor independent of vb: {polys[0]}")

    # Q3(e) series: z cosh z - sinh z vs sum 2n z^{2n+1}/(2n+1)!
    z = sp.symbols("z")
    lhs = z * sp.cosh(z) - sp.sinh(z)
    N = 12
    rhs = sum(2 * n * z ** (2 * n + 1) / sp.factorial(2 * n + 1) for n in range(1, N + 1))
    ser = lhs.series(z, 0, 2 * N + 3).removeO()
    if sp.expand(ser - rhs.expand()) != 0:
        hits.append("HIT: z cosh z - sinh z series mismatch")
        print(hits[-1], sp.expand(ser - rhs.expand()))
    else:
        print(f"Q3(e): series identity holds through z^{2*N+1}")

    if hits:
        print("SUMMARY: Q3 spectrum / Q2 pendant / series identities fail")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known Q4(a) "
        "triangle HIT — Q3 φ-spectrum Z1 / p-q (×3) / p+q-2r (×2) and φ² "
        "isotypic squares, constancy iff p=q=r, Q2 pendant-path factors of "
        "length 2 and 3 independent of the attachment value, and the Q3(e) "
        "series z cosh z − sinh z = Σ 2n z^{2n+1}/(2n+1)! all hold literally"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
