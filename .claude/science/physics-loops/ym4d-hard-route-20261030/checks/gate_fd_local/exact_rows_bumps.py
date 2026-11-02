#!/usr/bin/env python3
"""Gate fd-local: exact rational checks of the row kernels and bumps of fd-local.md Section 4.

Criteria, written before the first run. PASS requires all of:
 R1  composite longitudinal row weight, built by iterating the one-level average at L = 32, 33
     through 2 and 3 levels, equals exactly (z+1)/L^k on the first block and 1 - (z+1)/L^k on the
     second, z = 0..L^k-1. So the moments against (1-t, t) are the actual rows.
 B1  at m in {32, 33, 40, 64, 1024} sites, with t = (z+1)/m and exact site averages:
     avg(b) >= 1/16; each of the two intervals has p-mass >= 1/128; v >= 2^-18.
 B2  avg(psi_- (1-t)) = 1, avg(psi_- t) = 0, avg(psi_+ (1-t)) = 0, avg(psi_+ t) = 1, exactly.
 B3  sup|psi| <= 2^22 and m * max first difference <= 2^25; supp psi inside the block interior.
 T1  the IMS absorption: with e = 1/(100(1+C0)), (4C0+1)e < 1/20 and
     (8C0 + 4C0 e)/(1-(4C0+1)e) <= 16 C0, at C0 in {1, 4, 100, 10^6}.
A FAIL refutes the displayed constant only. A PASS covers these sizes only and proves nothing
for other sizes: the hand arguments in the gate report carry the general case.
"""
import resource
from fractions import Fraction as Fr

def guard():
    """Stop above 2 GB RSS (ru_maxrss is in bytes on darwin)."""
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 2 << 30:
        raise SystemExit("stopped: RSS above 2 GB")


def one_level(L):
    """Weights of the one-level row on fine positions 0..2L-1 (last entry zero)."""
    w = [Fr(0)] * (2 * L)
    for y in range(L):
        for i in range(L):
            w[y + i] += Fr(1, L)
    return w


def compose(wc, w0, L):
    """Coarse row wc on L-cells, each coarse step read through the fine row w0."""
    n = len(wc) * L
    out = [Fr(0)] * (n + L)
    for m, c in enumerate(wc):
        if c:
            for j, v in enumerate(w0):
                out[m * L + j] += c * v
    return out[:n]


def check_rows():
    ok = True
    for L in (32, 33):
        w = one_level(L)
        cur = w
        for k in (2, 3):
            if L ** k > 40000:
                continue
            cur = compose(cur, w, L)
            B = L ** k
            a = all(cur[z] == Fr(z + 1, B) for z in range(B))
            bb = all(cur[B + z] == 1 - Fr(z + 1, B) for z in range(B))
            print(f"R1 L={L} k={k} rising={a} falling={bb}")
            ok &= a and bb
            guard()
    return ok


def check_bump(m):
    ts = [Fr(z + 1, m) for z in range(m)]
    b = [max(Fr(0), 1 - 4 * abs(t - Fr(1, 2))) for t in ts]
    av = sum(b) / m
    p = [x / av for x in b]
    a = sum(t * q for t, q in zip(ts, p)) / m
    v = sum((t - a) ** 2 * q for t, q in zip(ts, p)) / m
    pm = [q * (1 - a * (t - a) / v) for t, q in zip(ts, p)]
    pp = [q * (1 + (1 - a) * (t - a) / v) for t, q in zip(ts, p)]
    mass = lambda lo, hi: sum(q for t, q in zip(ts, p) if lo <= t <= hi) / m
    m1, m2 = mass(Fr(5, 16), Fr(3, 8)), mass(Fr(5, 8), Fr(11, 16))
    mom = lambda f, g: sum(f[i] * g(ts[i]) for i in range(m)) / m
    B2 = (mom(pm, lambda t: 1 - t) == 1 and mom(pm, lambda t: t) == 0
          and mom(pp, lambda t: 1 - t) == 0 and mom(pp, lambda t: t) == 1)
    sup = max(max(abs(x) for x in pm), max(abs(x) for x in pp))
    dif = max(max(abs(f[i + 1] - f[i]) for i in range(m - 1)) for f in (pm, pp)) * m
    B1 = av >= Fr(1, 16) and m1 >= Fr(1, 128) and m2 >= Fr(1, 128) and v >= Fr(1, 2 ** 18)
    B3 = sup <= 2 ** 22 and dif <= 2 ** 25 and pm[0] == 0 and pm[-1] == 0 and pp[0] == 0 and pp[-1] == 0
    guard()
    print(f"B m={m} avg_b={float(av):.4f} masses={float(m1):.4f},{float(m2):.4f} "
          f"v={float(v):.5f} sup={float(sup):.1f} Lip={float(dif):.1f} B1={B1} B2={B2} B3={B3}")
    return B1 and B2 and B3


def check_ims():
    ok = True
    for C0 in (1, 4, 100, 10 ** 6):
        e = Fr(1, 100 * (1 + C0))
        c1 = (4 * C0 + 1) * e
        ratio = (8 * C0 + 4 * C0 * e) / (1 - c1)
        good = c1 < Fr(1, 20) and ratio <= 16 * C0
        print(f"T1 C0={C0} coeff={float(c1):.4f} W/E<={float(ratio):.2f} ok={good}")
        ok &= good
    return ok


res = [check_rows()] + [check_bump(m) for m in (32, 33, 40, 64, 1024)] + [check_ims()]
print("PASS" if all(res) else "FAIL")
