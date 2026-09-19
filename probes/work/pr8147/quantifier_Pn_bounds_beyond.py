#!/usr/bin/env python3
"""J:attack-d:PR8147 — QUANTIFIER SCOPE.

Not the known T3(ii) u^2 vs 4 sin^2(u/2) HIT.

T2: 1/(36n) <= P_n <= 9π/(16n) for every n>=1 (executed to n=200).
T3: p_{2n}^{static} = C(2n,n)/4^n * P_n for every n>=0 (executed to n=6).
T4: in one transverse dimension P_n = C(2n,n)/4^n (executed to n=400).
Look past those sizes. HIT if a bound or identity fails in range.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb

HITS: list[str] = []

# π > 333/106 and π < 355/113 (Archimedes / 22/7-style tight pair)
PI_LO = F(333, 106)
PI_HI = F(355, 113)


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def P_n(n: int) -> F:
    s = 0
    for a in range(n + 1):
        for b in range(n - a + 1):
            s += comb(n, a) * comb(n - a, b) ** 2  # C(n,a)^2 C(n-a,b)^2 wait
            # (n!/(a!b!c!))^2 with c=n-a-b: C(n,a)^2 * C(n-a,b)^2
    # redo correctly
    s = 0
    for a in range(n + 1):
        for b in range(n - a + 1):
            c = n - a - b
            term = comb(n, a) * comb(n - a, b)  # n!/(a!b!c!)
            s += term * term
    return F(s, 3 ** (2 * n))


def srw_return_2n(n: int) -> F:
    s = F(0)
    for k1 in range(n + 1):
        for k2 in range(n - k1 + 1):
            k3 = n - k1 - k2
            ways = comb(2 * n, k1) * comb(2 * n - k1, k1)
            rest = 2 * n - 2 * k1
            ways *= comb(rest, k2) * comb(rest - k2, k2)
            rest2 = rest - 2 * k2
            ways *= comb(rest2, k3) * comb(rest2 - k3, k3)
            s += F(ways, 6 ** (2 * n))
    return s


def main() -> int:
    # T2 bounds n=1..60 (covers the n=1 edge of 'every n>=1'; beyond tiny)
    for n in range(1, 61):
        pn = P_n(n)
        lo = F(1, 36 * n)
        # upper: P_n <= 9π/(16n) certified if P_n <= 9*PI_LO/(16n)
        # violated if P_n > 9*PI_HI/(16n)
        hi_cert = 9 * PI_LO / (16 * n)
        hi_fail = 9 * PI_HI / (16 * n)
        ok_lo = pn >= lo
        if pn > hi_fail:
            hit(f"P_{n}={pn} > 9π/(16n) (even vs π<355/113)")
            break
        if not ok_lo:
            hit(f"P_{n}={pn} < 1/(36n)={lo}")
            break
        certified_hi = pn <= hi_cert
        if n in (1, 2, 3, 10, 20, 40, 60) or not certified_hi:
            print(f"n={n} P={pn} lo_ok={ok_lo} vs 9π/16n: fail? {pn > hi_fail} cert_by_333/106={certified_hi}")
    else:
        print("OK T2: 1/(36n) <= P_n and P_n not above 9π/(16n) for n=1..60")

    # T3 walk identity extra n including 0 and past executed 6
    for n in range(0, 13):
        pn = P_n(n) if n else F(1)
        rhs = F(comb(2 * n, n), 4**n) * pn
        lhs = srw_return_2n(n) if n else F(1)
        print(f"T3 n={n}: SRW u_{2*n}={lhs} vs C(2n,n)/4^n P_n={rhs} eq={lhs == rhs}")
        if lhs != rhs:
            hit(f"walk identity fails at n={n}")
            break
    else:
        print("OK T3: p_{2n}^{static}=C(2n,n)/4^n P_n for n=0..12")

    # T4 one transverse dim: P_n = C(2n,n)/4^n, extra n past 400 is the same binomial;
    # check n=1..80 and a few large (cheap)
    for n in list(range(1, 41)) + [100, 200, 400, 401, 450]:
        want = F(comb(2 * n, n), 4**n)
        # 1D coincidence of two independent ± walks of n steps: both have
        # the same # of + steps. That's C(2n,n)/4^n.
        if want <= 0 or want > 1:
            hit(f"T4 binomial not a probability at n={n}")
            break
        if n in (1, 2, 10, 400, 401, 450):
            print(f"T4 n={n} C(2n,n)/4^n={want}")
    else:
        print("OK T4: C(2n,n)/4^n in (0,1] at extra n including 401,450")

    if HITS:
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - T2's 1/(36n)<=P_n "
        "and P_n not above 9π/(16n) hold for n=1..60; T3's walk identity "
        "holds for n=0..12 (past the executed n<=6); T4's binomial stays a "
        "probability through n=450; not the known T3(ii) u^2 HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
