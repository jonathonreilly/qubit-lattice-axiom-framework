"""ys1b2_control.py -- clause B5 of checks/ys1b_criteria.md ONLY, run separately.

`ys1b_power.py` aborted AT clause B5 with an AssertionError: the internal mass check
  sum_s c_s == L^{i(D+1)}
fired on the deliberately corrupted pipeline (135 against 243 at i = 1).  `ys1b_power.py`,
`ys1b_out.txt` and `ys1b_err.txt` are kept unaltered with that abort; B1-B4 had already printed their
verdicts and are unaffected.  This file re-runs clause B5 alone, with the mass assertion reported rather
than raised, so that the control's VALUE can be compared as the criterion asks.  `ys1b_criteria.md` is
untouched.  Exact arithmetic, plain python, no numpy/BLAS, no lock.
"""
from fractions import Fraction as F
from math import gcd

L, D = 3, 4


def off(l):
    return (L ** l - 1) // 2


def avatar(k, i):
    return (off(k) - off(i)) // L ** i


def mult_true(i):
    cur = {0: 1}
    for _ in range(i):
        nxt = {}
        for w, c in cur.items():
            for r in range(L):
                for j in range(L):
                    nxt[L * w + r + j] = nxt.get(L * w + r + j, 0) + c
        cur = nxt
    return cur


def mult_flat(i):
    return {w: 1 for w in mult_true(i)}


IMAX, KB = 6, 7
SMAX = 4 * L ** IMAX + 8
lc = 1
for t in range(1, SMAX + 2):
    lc = lc * t // gcd(lc, t)
M = lc ** 3
INV = [M // (1 + s) ** 3 for s in range(SMAX + 1)]
cXb = [off(KB)] * D
pb = [cXb[0] + 1, cXb[1], cXb[2], cXb[3]]


def li_at(i, Y, m, mlfun):
    ni = L ** i
    base = [ni * Y[n] for n in range(D)]
    ml = mlfun(i)
    smax = 0
    for n in range(D):
        if n != m:
            smax = max(smax, abs(base[n] - pb[n]), abs(base[n] + ni - 1 - pb[n]))
    for w in ml:
        smax = max(smax, abs(base[m] + w - pb[m]))
    P = [0] * (smax + 1)
    for T in range(smax + 1):
        pr = 1
        for n in range(D):
            if n != m:
                pr *= max(0, min(base[n] + ni - 1, pb[n] + T) - max(base[n], pb[n] - T) + 1)
        P[T] = pr
    A = [0] * (smax + 1)
    for w, mu in ml.items():
        A[abs(base[m] + w - pb[m])] += mu
    Bp, run = [0] * (smax + 1), 0
    for s in range(smax + 1):
        Bp[s] = run
        run += A[s]
    tot = chk = 0
    for s in range(smax + 1):
        c = P[s] * A[s] + (P[s] - (P[s - 1] if s else 0)) * Bp[s]
        if c:
            tot += c * INV[s]
            chk += c
    return F(tot, M * L ** (D * i)), chk


print("=" * 104)
print("ys1b2 -- clause B5 of ys1b_criteria.md, run alone (ys1b_power.py aborted at this clause).")
print("=" * 104)
ok = True
for i in (1, 2, 3):
    Y = [avatar(KB, i)] * D
    t, ct = li_at(i, Y, 0, mult_true)
    c, cc = li_at(i, Y, 0, mult_flat)
    diff = (t != c)
    ok = ok and diff
    print("  i=%d: true LI = %.9e (mass %d = L^{i(D+1)} %s) | control LI = %.9e (mass %d) | differ: %s"
          % (i, float(t), ct, ct == L ** (i * (D + 1)), float(c), cc, diff))
print("\n  B5 VERDICT (control must differ from the true pipeline at every i): %s"
      % ("PASS" if ok else "FAIL -- the pipeline cannot see the feature it tests"))
print("=" * 104)
