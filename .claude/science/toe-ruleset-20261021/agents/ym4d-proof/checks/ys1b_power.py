"""ys1b_power.py -- YSUP session 25, RE-RUN under a new id of the two ys1 clauses that FAILED
(A2 (c) -> B1;  A4 -> B2/B3), with the exact profile (1+s)^-3 and i up to 6.
checks/ys1_criteria.md is untouched; checks/ys1b_criteria.md was written before this file.

Exact arithmetic throughout: all profile sums are integer sums over the common denominator
M = lcm(1..Smax+1)^3, converted to a single Fraction at the end.  Plain python, no numpy, no BLAS.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import gcd, log

L, D = 3, 4
OFF = (L - 1) // 2


def off(l):
    return (L ** l - 1) // 2


def avatar(k, i):
    return (off(k) - off(i)) // L ** i


# ---------- rebuilt operators (same definitions as ys1_funnel.py, re-typed, not imported) ----------
def build_HT(half=OFF):
    W1 = F(1, 24 * L ** D)
    HT = {}
    for sig in permutations(range(D)):
        for o in product(range(-half, half + 1), repeat=D):
            z = [0] * D
            for c in sig:
                while z[c] != o[c]:
                    if o[c] > z[c]:
                        k = (tuple(z), c); HT[k] = HT.get(k, F(0)) + W1; z[c] += 1
                    else:
                        z[c] -= 1
                        k = (tuple(z), c); HT[k] = HT.get(k, F(0)) - W1
    return {k: v for k, v in HT.items() if v != 0}


HT = build_HT()


def hfun(w, Y):
    tot = F(0)
    for (z, c), wt in HT.items():
        v = w.get((tuple(L * Y[n] + OFF + z[n] for n in range(D)), c))
        if v:
            tot += wt * v
    return tot


def qstr(v):
    out, cand = {}, set()
    for (s, _) in v:
        for Y in product(*[range(s[n] // L - 1, s[n] // L + 1) for n in range(D)]):
            cand.add(Y)
    for Y in cand:
        for m in range(D):
            tot = F(0)
            for r in product(range(L), repeat=D):
                base = [L * Y[n] + r[n] for n in range(D)]
                for j in range(L):
                    z = list(base); z[m] += j
                    tot += v.get((tuple(z), m), F(0))
            if tot:
                out[(Y, m)] = tot / L ** D
    return out


def plaq(s, m, n):
    s = tuple(s)
    sm = list(s); sm[m] += 1
    sn = list(s); sn[n] += 1
    return {(tuple(sm), n): F(1), (s, n): F(-1), (tuple(sn), m): F(-1), (s, m): F(1)}


def hT(k, i):
    Y = (avatar(k, i + 1),) * D
    return {(tuple(L * Y[n] + OFF + z[n] for n in range(D)), c): wt for (z, c), wt in HT.items()}


def qstrT(psi):
    out = {}
    for (Y, m), val in psi.items():
        w = val / L ** D
        for r in product(range(L), repeat=D):
            base = [L * Y[n] + r[n] for n in range(D)]
            for j in range(L):
                z = list(base); z[m] += j
                kk = (tuple(z), m)
                out[kk] = out.get(kk, F(0)) + w
    return {k: v for k, v in out.items() if v != 0}


def mult_long(i):
    cur = {0: 1}
    for _ in range(i):
        nxt = {}
        for w, c in cur.items():
            for r in range(L):
                for j in range(L):
                    nxt[L * w + r + j] = nxt.get(L * w + r + j, 0) + c
        cur = nxt
    return cur


print("=" * 104)
print("ys1b -- re-run of the two FAILED ys1 clauses, exact profile (1+s)^-3, i up to 6.  d=%d L=%d" % (D, L))
print("=" * 104)

# ================================================================ B1 (repaired A2 (c))
print("\n--- B1  ||K_i||_1 <= L^i * L^-D sum_{y in B}|y - c_X|_1   and   sup|K_i| <= L^{i(1-D)} ---")
closed_tv = F(sum(sum(abs(o[n]) for n in range(D)) for o in product(range(-OFF, OFF + 1), repeat=D)), L ** D)
B1 = True
for i in (0, 1, 2, 3, 4):
    g = hT(i + 1, i)
    ml = mult_long(i)
    cl = {}
    for (Y, m), wt in g.items():
        Yp = tuple(Y[n] for n in range(D) if n != m)
        for w, mu in ml.items():
            kk = (m, Yp, L ** i * Y[m] + w)
            cl[kk] = cl.get(kk, F(0)) + F(mu, L ** (D * i)) * wt
    cl = {k: v for k, v in cl.items() if v != 0}
    sup = max(abs(v) for v in cl.values())
    l1 = sum(abs(v) for v in cl.values()) * L ** (i * (D - 1))
    bnd_sup = F(1, L ** (i * (D - 1)))
    bnd_l1 = F(L ** i) * closed_tv
    ok = (sup <= bnd_sup) and (l1 <= bnd_l1)
    B1 = B1 and ok
    print("  i=%d: sup=%-18s <= %-12s %-5s | l1=%-14s <= %-8s %-5s | l1/L^i = %.5f"
          % (i, sup, bnd_sup, sup <= bnd_sup, l1, bnd_l1, l1 <= bnd_l1, float(l1) / L ** i))
print("  B1 VERDICT: %s" % ("PASS" if B1 else "FAIL"))

# ================================================================ B2 / B3  exact profile, i = 0..6
IMAX = 6
KB = IMAX + 1
SMAX = 4 * L ** IMAX + 8
print("\n--- B2/B3  exact profile v(b) = (1+|b-p|_inf)^-3 ; i = 0..%d ; SMAX = %d ---" % (IMAX, SMAX))
lc = 1
for t in range(1, SMAX + 2):
    lc = lc * t // gcd(lc, t)
M = lc ** 3
INV = [M // (1 + s) ** 3 for s in range(SMAX + 1)]
print("  common denominator M = lcm(1..%d)^3 has %d decimal digits" % (SMAX + 1, len(str(M))))

cXb = [off(KB)] * D
pb = [cXb[0] + 1, cXb[1], cXb[2], cXb[3]]


def li_at(i, Y, m):
    """exact (Q_str^{(0->i)} v)(Y, m) as a Fraction, via radius classes."""
    ni = L ** i
    base = [ni * Y[n] for n in range(D)]
    ml = mult_long(i)
    # transverse cumulative counts
    tmax = 0
    for n in range(D):
        if n != m:
            tmax = max(tmax, abs(base[n] - pb[n]), abs(base[n] + ni - 1 - pb[n]))
    amax = 0
    for w in ml:
        amax = max(amax, abs(base[m] + w - pb[m]))
    smax = max(tmax, amax)
    P = [0] * (smax + 1)
    for T in range(smax + 1):
        pr = 1
        for n in range(D):
            if n != m:
                hi = min(base[n] + ni - 1, pb[n] + T)
                lo = max(base[n], pb[n] - T)
                pr *= max(0, hi - lo + 1)
        P[T] = pr
    A = [0] * (smax + 1)
    for w, mu in ml.items():
        A[abs(base[m] + w - pb[m])] += mu
    Bp = [0] * (smax + 1)
    run = 0
    for s in range(smax + 1):
        Bp[s] = run
        run += A[s]
    tot = 0
    chk = 0
    for s in range(smax + 1):
        cnt = P[s] - (P[s - 1] if s else 0)
        c = P[s] * A[s] + cnt * Bp[s]
        if c:
            tot += c * INV[s]
            chk += c
    assert chk == L ** (i * (D + 1)), (i, Y, m, chk, L ** (i * (D + 1)))
    return F(tot, M * L ** (D * i))


LI, LIMAX, BA = {}, {}, {}
for i in range(IMAX + 1):
    ni = L ** i
    Yc = avatar(KB, i)
    LI[i] = li_at(i, [Yc] * D, 0)
    best = F(0)
    for z in product(range(-1, 2), repeat=D):
        Y = [Yc + z[n] for n in range(D)]
        for m in range(D):
            val = abs(li_at(i, Y, m))
            if val > best:
                best = val
    LIMAX[i] = best
    h = (ni - 1) // 2
    tot = 0
    for s in range(h + 1):
        N = 1 if s == 0 else (2 * s + 1) ** D - (2 * s - 1) ** D
        tot += N * INV[s]
    BA[i] = F(tot, M * ni ** D)
    print("  i=%d (n_i=%-4d): LI=%.9e  LImax=%.9e  BA=%.9e   | LI*n^2=%.6f  LImax*n^2=%.6f  BA*n^3=%.6f"
          % (i, ni, float(LI[i]), float(LIMAX[i]), float(BA[i]),
             float(LI[i]) * ni ** 2, float(LIMAX[i]) * ni ** 2, float(BA[i]) * ni ** 3))


def bands(fam, name):
    rho = []
    for i in range(len(fam) - 1):
        r = fam[i + 1] / fam[i]
        rho.append((i, r, -log(float(r)) / log(L)))
    print("  %s:  " % name + "  ".join("rho_%d=%.4f" % (i, q) for i, _, q in rho))
    sub = [q for i, _, q in rho if i in (3, 4, 5)]
    v2 = all(1.5 <= q < 2.5 for q in sub)
    v3 = all(2.5 <= q < 3.5 for q in sub)
    verd = "(V-2)" if v2 else ("(V-3)" if v3 else "(V-other)")
    print("     band test on i = 3,4,5 -> %s   [%s]" % (verd, ", ".join("%.4f" % q for q in sub)))
    return verd


print("\n  pre-registered band test (i = 3,4,5 only; i <= 2 reported but excluded):")
vLI = bands([LI[i] for i in range(IMAX + 1)], "LI   ")
vLM = bands([LIMAX[i] for i in range(IMAX + 1)], "LImax")
vBA = bands([BA[i] for i in range(IMAX + 1)], "BA   ")
B2 = all(v in ("(V-2)", "(V-3)") for v in (vLI, vLM, vBA))
print("  B2 VERDICT: LI=%s LImax=%s BA=%s -> %s" % (vLI, vLM, vBA, "usable" if B2 else "criteria INADEQUATE"))
print("  B2' (the two objects land in DIFFERENT bands): %s" % (vLI != vBA))

print("\n--- B3  scaled constants, monotone convergence over i = 3..6, 15%% between i = 5 and 6 ---")
sLI = [float(LI[i]) * L ** (2 * i) for i in range(IMAX + 1)]
sLM = [float(LIMAX[i]) * L ** (2 * i) for i in range(IMAX + 1)]
sBA = [float(BA[i]) * L ** (3 * i) for i in range(IMAX + 1)]
for nm, a in (("LI*n^2 ", sLI), ("LImx*n^2", sLM), ("BA*n^3 ", sBA)):
    print("  %s: " % nm + "  ".join("i=%d:%.5f" % (i, a[i]) for i in range(IMAX + 1)))


def conv(a):
    seg = a[3:IMAX + 1]
    mono = all(seg[j] <= seg[j + 1] for j in range(len(seg) - 1)) or \
           all(seg[j] >= seg[j + 1] for j in range(len(seg) - 1))
    close = abs(a[IMAX] - a[IMAX - 1]) <= 0.15 * abs(a[IMAX - 1])
    return mono, close


B3 = True
for nm, a in (("LI*n^2", sLI), ("LImax*n^2", sLM), ("BA*n^3", sBA)):
    mo, cl = conv(a)
    print("  %-10s monotone on i=3..6: %-5s   |delta(5->6)|/|v5| = %.4f  (<=0.15: %s)"
          % (nm, mo, abs(a[IMAX] - a[IMAX - 1]) / abs(a[IMAX - 1]), cl))
    B3 = B3 and mo and cl
print("  B3 VERDICT: %s" % ("PASS" if B3 else "FAIL"))

# ================================================================ B4
print("\n--- B4  the funnel terms of u = (1/8) d* delta_p at k = 5 ---")
k5 = 5
cX5 = (off(k5),) * D
p5 = tuple(cX5[n] + (1, 0, 0, 0)[n] for n in range(D))
u5 = {b: v / 8 for b, v in plaq(p5, 0, 1).items()}
cur, terms = dict(u5), []
for i in range(k5):
    terms.append(hfun(cur, (avatar(k5, i + 1),) * D))
    if i + 1 < k5:
        cur = qstr(cur)
cov = (terms[0] == F(-1, 432) and terms[1] == F(-17, 104976))
B4 = cov
for i, t in enumerate(terms):
    print("  phi_%d = %-26s = %+.10e" % (i + 1, t, float(t)))
print("  Phi_5 = %s = %+.10e" % (sum(terms, F(0)), float(sum(terms, F(0)))))
print("  (covariance: phi_1 = -1/432 and phi_2 = -17/104976 at k = 5 as at k = 2) : %s" % cov)
print("  B4 VERDICT: %s" % ("PASS" if B4 else "FAIL"))

# ================================================================ B5 designed-FAIL control
print("\n--- B5  DESIGNED-FAIL CONTROL: longitudinal multiplicity replaced by 1 ---")
_real_ml = mult_long


def _flat_ml(i):
    return {w: 1 for w in _real_ml(i)}


mult_long = _flat_ml
ctrl = li_at(1, [avatar(KB, 1)] * D, 0)
mult_long = _real_ml
B5 = (ctrl != LI[1])
print("  control LI_1 = %.9e   true LI_1 = %.9e   differ: %s" % (float(ctrl), float(LI[1]), B5))
print("  B5 VERDICT: %s" % ("PASS" if B5 else "FAIL -- the pipeline cannot see the feature it tests"))

print("\n" + "=" * 104)
print("SUMMARY  B1 %s | B2 %s | B3 %s | B4 %s | B5 %s"
      % tuple("PASS" if x else "FAIL" for x in [B1, B2, B3, B4, B5]))
print("=" * 104)
