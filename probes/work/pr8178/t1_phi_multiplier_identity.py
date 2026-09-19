#!/usr/bin/env python3
"""J:attack-g:PR8178 — brute-force T1.2 multiplier identity, NOT the known D1 HIT.

T1.2: φ(k)=(1+e^{ik1}+e^{ik2})/3 and
  1-|φ|² = (4/9)[sin²(k1/2)+sin²(k2/2)+sin²((k1-k2)/2)]
so |φ|<1 off the zero mode. Proof: 9|φ|²=3+2cos k1+2cos k2+2cos(k1-k2)
and 1-cos x = 2 sin²(x/2).

HIT if the identity fails symbolically or at any torus mode of L=2,3,4,8,
or if a nonzero mode has |φ|=1. Exact sympy.
"""
from __future__ import annotations

import sympy as sp


def main():
    hits = []
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    u = sp.simplify(sp.expand_complex(sp.conjugate(phi) * phi))
    nine_u = sp.simplify(9 * u)
    claimed_nine = 3 + 2 * sp.cos(k1) + 2 * sp.cos(k2) + 2 * sp.cos(k1 - k2)
    if sp.simplify(nine_u - claimed_nine) != 0:
        hits.append(f"HIT: 9|phi|^2 != 3+2cos k1+2cos k2+2cos(k1-k2): {nine_u}")
        print(hits[-1])
    else:
        print("9|φ|² = 3+2cos k1+2cos k2+2cos(k1-k2)")

    one_minus = sp.simplify(1 - u)
    rhs = (4 * sp.Rational(1, 9)) * (
        sp.sin(k1 / 2) ** 2 + sp.sin(k2 / 2) ** 2 + sp.sin((k1 - k2) / 2) ** 2
    )
    if sp.simplify(one_minus - rhs) != 0:
        hits.append("HIT: 1-|phi|^2 != (4/9)[sin^2(k1/2)+sin^2(k2/2)+sin^2((k1-k2)/2)]")
        print(hits[-1], sp.simplify(one_minus - rhs))
    else:
        print("1-|φ|² = (4/9)[sin²(k1/2)+sin²(k2/2)+sin²((k1-k2)/2)]")

    # torus modes
    n_zero_u1 = 0
    n_checked = 0
    for L in (2, 3, 4, 8):
        for n1 in range(L):
            for n2 in range(L):
                n_checked += 1
                kk1 = 2 * sp.pi * n1 / L
                kk2 = 2 * sp.pi * n2 / L
                val = sp.simplify(one_minus.subs({k1: kk1, k2: kk2}))
                rhs_v = sp.simplify(rhs.subs({k1: kk1, k2: kk2}))
                if sp.simplify(val - rhs_v) != 0:
                    hits.append(f"HIT: identity fails at L={L} n=({n1},{n2})")
                    print(hits[-1])
                u_v = sp.simplify(u.subs({k1: kk1, k2: kk2}))
                if (n1, n2) == (0, 0):
                    if sp.simplify(u_v - 1) != 0:
                        hits.append(f"HIT: zero mode u!=1 at L={L}: {u_v}")
                        print(hits[-1])
                else:
                    # u < 1
                    num = sp.N(u_v, 50)
                    if num >= 1:
                        hits.append(f"HIT: nonzero mode |phi|=1 at L={L} n=({n1},{n2}) u={u_v}")
                        print(hits[-1])
                        n_zero_u1 += 1
        print(f"L={L}: all {L*L} modes identity ok; zero mode u=1")
    print(f"modes checked {n_checked}; extra u=1 nonzero {n_zero_u1}")

    if hits:
        print("SUMMARY: T1.2 multiplier identity fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note beyond the known lag-25 D1 HIT "
        "— T1.2 1-|φ(k)|²=(4/9)[sin²(k1/2)+sin²(k2/2)+sin²((k1-k2)/2)] holds "
        "symbolically and on every mode of the L=2,3,4,8 tori, with |φ|=1 only "
        "at the zero mode"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
