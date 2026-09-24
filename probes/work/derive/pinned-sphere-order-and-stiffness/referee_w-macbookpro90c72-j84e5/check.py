#!/usr/bin/env python3
"""Referee for pinned-sphere-order-and-stiffness a4.

Author w-jonathonsmac4f50-j7c7a (claude-opus-5-5). Own ring enumeration and own rational bounds.
"""
import itertools
import math
from fractions import Fraction as Fr
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def c0_decreases():
    b = sp.symbols("beta", positive=True)
    # d/db (b/sinh b) has numerator sinh b - b cosh b, whose derivative is -b sinh b.
    num = sp.sinh(b) - b * sp.cosh(b)
    ok = sp.diff(num, b) == -b * sp.sinh(b) and sp.limit(num, b, 0) == 0
    # two-valued floor 1/cosh is the same story
    num2 = sp.sinh(b)  # d(1/cosh)/db = -sinh/cosh^2 < 0
    report(
        "pinned floor decreases",
        bool(ok and sp.simplify(sp.diff(1 / sp.cosh(b), b) + sp.sinh(b) / sp.cosh(b) ** 2) == 0),
        "beta/sinh beta and 1/cosh beta are strictly decreasing, so c0(beta) < c0(beta - beta') for beta' > 0",
    )


def kernel_floor():
    """Two-valued bond kernel on {empty, +1, -1} is singular at c0 and not PSD below it."""
    q = sp.symbols("q", positive=True)
    c0 = 2 * q / (q**2 + 1)  # 1/cosh when e^beta = q
    same = c0 * q
    opp = c0 / q
    M = sp.Matrix([[1, 1, 1], [1, same, opp], [1, opp, same]])
    # at c0 the Schur complement on the two spins has determinant 0
    schur = M[1:, 1:] - M[1:, 0] * M[0, 1:]
    ok_sing = sp.simplify(schur.det()) == 0
    # slightly below: c = c0 * 99/100, smallest eigenvalue of the numerical matrix at q=3 is negative
    qv = 3
    c_below = (2 * qv / (qv**2 + 1)) * 0.99
    Mb = sp.Matrix([[1, 1, 1], [1, c_below * qv, c_below / qv], [1, c_below / qv, c_below * qv]])
    ev = [complex(v).real for v in Mb.eigenvals()]
    report(
        "kernel floor",
        bool(ok_sing and min(ev) < 0),
        f"two-valued Schur determinant vanishes at c0=1/cosh; at 0.99 c0 the smallest eigenvalue is {min(ev):.4f}",
    )


def ring_two(q, z):
    c = Fr(2 * q, q * q + 1)
    Z = Fr(0)
    num = Fr(0)
    occ = Fr(0)
    n = 4
    for cfg in itertools.product((None, 1, -1), repeat=n):
        w = Fr(1)
        for x in range(n):
            if cfg[x] is not None:
                w *= z
            a, b = cfg[x], cfg[(x + 1) % n]
            if a is not None and b is not None:
                w *= c * (q if a == b else Fr(1, q))
        Z += w
        sig = [0 if s is None else s for s in cfg]
        m = sum(((-1) ** x) * sig[x] for x in range(n))
        num += w * m * m
        occ += w * sum(1 for s in cfg if s is not None)
    return num / (n * Z), occ / (n * Z), Z


def two_valued_witness():
    S, rho, Z = ring_two(20, Fr(1, 2))
    claimed = Fr(77831376023, 439056344017)
    u = Fr(19, 21)
    log_lo = 2 * sum(u ** (2 * k + 1) / (2 * k + 1) for k in range(80))
    lb = 4 * log_lo * S
    # sum rule: sum_k <|sigma hat|^2>/4 = 4 rho? S(pi) is one mode. Check total occupation identity rho in (0,1).
    report(
        "two-valued ring",
        S == claimed and lb > Fr(212, 100),
        f"S(pi)={S} matches the printed fraction; 4 log(20) S > {float(lb):.4f}; rho={float(rho):.4f}",
    )


def literal():
    q = 3
    c0 = Fr(3, 5)
    states = [(u, a) for a in (0, 2) for u in (None, 1, -1)]

    def entry(s1, s2):
        (u, a), (v, b) = s1, s2
        if u is None or v is None:
            return Fr(1)
        d = (u - v) - (a - b)
        return c0 * q * Fr(1, q ** ((d * d) // 2))

    K = [[entry(states[i], states[j]) for j in range(6)] for i in range(6)]
    x = [Fr(-1), Fr(1), Fr(1, 2), Fr(-1), Fr(1, 2), Fr(1)]
    form = sum(x[i] * K[i][j] * x[j] for i in range(6) for j in range(6))
    sig = [1, 1, 0, 1]
    psi = [1, 0, -1, 0]
    rec = 0
    for t in range(4):
        u, v = sig[t], sig[(t + 1) % 4]
        if u != 0 and v != 0:
            rec += (psi[t] - psi[(t + 1) % 4]) * (u - v)
    emb = 2 * sum(sig[t] * psi[t] for t in range(4))
    report(
        "literal twist",
        form == Fr(-6559, 3645) and rec == 0 and emb == 2,
        f"crossing form {form}; record-bond contraction {rec} against E sum sigma psi = {emb}",
    )


def dfact(n):
    out = 1
    while n > 0:
        out *= n
        n -= 2
    return out


def sphere_bound():
    """Rational lower bound for 4*beta*S(pi) on the sphere 4-ring at beta=8, z=1."""
    beta = 8
    K = 80
    series = sum(Fr(16) ** k / math.factorial(k) for k in range(K + 1))
    # e^16 > series, e^16 < series + next/(1 - 16/(K+1))
    rem = Fr(16) ** (K + 1) / math.factorial(K + 1)
    e_hi = series + rem * Fr(K + 1, K + 1 - 16)
    e_lo = series
    coth_lo = (e_hi + 1) / (e_hi - 1)  # coth decreases in e^16
    coth_hi = (e_lo + 1) / (e_lo - 1)
    # i_l = a sinh + b cosh, recurrence i_{l+1} = i_{l-1} - (2l+1) i_l / beta
    # i0 = sinh/beta => a0=1/beta, b0=0
    # i1 = cosh/beta - sinh/beta^2 => a1=-1/beta^2, b1=1/beta
    a = [Fr(1, beta), Fr(-1, beta ** 2)]
    b = [Fr(0), Fr(1, beta)]
    LC = 24
    for l in range(1, LC + 2):
        a.append(a[l - 1] - Fr(2 * l + 1, beta) * a[l])
        b.append(b[l - 1] - Fr(2 * l + 1, beta) * b[l])
    r_lo, r_hi = [], []
    for l in range(LC + 2):
        v1 = beta * a[l] + beta * b[l] * coth_lo
        v2 = beta * a[l] + beta * b[l] * coth_hi
        lo, hi = min(v1, v2), max(v1, v2)
        r_lo.append(max(lo, Fr(0)))
        r_hi.append(min(hi, Fr(1)))
    # tail r_l <= (beta^l / (2l+1)!!) * e^{beta^2/(4l+6)} * (beta/sinh beta)
    # e^{64/(4l+6)} <= e^{1/2} < 5/3 for l >= 24, and beta/sinh beta = 16/(e^16-e^{-16}) < 16/(e^16-1)
    e8_lo = sum(Fr(8) ** k / math.factorial(k) for k in range(40))
    e_half_hi = sum(Fr(1) / math.factorial(k) for k in range(20)) + Fr(1, math.factorial(19))
    ok_tail_const = e8_lo > 2980 and e_half_hi < Fr(25, 9)
    sinh8_lo = (e8_lo - Fr(1, 2980)) / 2  # e^{-8} < 1/2980
    # use the attempt's explicit 16/2979 only after checking e^8>2980 implies 8/sinh 8 < 16/(e^8 - e^{-8}) < 16/2979
    ratio_8 = Fr(16, 2979)

    def T(l):
        return Fr(8 ** l, dfact(2 * l + 1)) * Fr(5, 3) * ratio_8

    L0 = LC + 1
    tail = (2 * L0 + 2) * T(L0) ** 4 * 2
    LF_lo = sum((2 * l + 1) * r_lo[l] ** 4 for l in range(LC + 1))
    LF_hi = sum((2 * l + 1) * r_hi[l] ** 4 for l in range(LC + 1)) + tail
    A_hi = sum((l + 1) * (r_hi[l] ** 3 * r_hi[l + 1] + r_hi[l] * r_hi[l + 1] ** 3) for l in range(LC + 1)) + tail
    O_lo = sum(2 * (l + 1) * r_lo[l] ** 2 * r_lo[l + 1] ** 2 for l in range(LC + 1))
    # Z = 15 + LF: every occupancy except the full ring is a forest and weighs 1 at c0; the ring weighs LF.
    num_lo = 7 + LF_lo - 6 * r_hi[1] - 2 * A_hi + 2 * r_lo[1] ** 2 + O_lo
    V_lo = Fr(4 * beta, 3) * num_lo / (15 + LF_hi)
    report(
        "sphere ring",
        ok_tail_const and V_lo > Fr(19, 10) and r_lo[0] == Fr(1),
        f"4 beta S(pi) > {float(V_lo):.4f}; forest count gives Z=15+LF; coth bounds from the e^16 series",
    )


def main():
    c0_decreases()
    kernel_floor()
    two_valued_witness()
    literal()
    sphere_bound()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - at the pinned scale the Gaussian-domination route fails. "
        "On the two-valued 4-ring with e^beta=20 and z=1/2, S(pi)=77831376023/439056344017 and 4 beta S(pi)>2.12. "
        "On the sphere 4-ring at beta=8, z=1, 4 beta S(pi)>1.9. "
        "No twist beta'>0 fits inside c0, because c0 is strictly decreasing."
    )
    print(
        "SUMMARY: confirmed the floor, the exact two-valued fraction, the crossing form -6559/3645, "
        "and a rational lower bound above 1 for the sphere ring. "
        "The route therefore gives beta'=0 and no infrared constant at c0."
    )


if __name__ == "__main__":
    main()
