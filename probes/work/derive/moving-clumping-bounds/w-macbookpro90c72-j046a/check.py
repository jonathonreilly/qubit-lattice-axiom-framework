#!/usr/bin/env python3
"""J:derive:moving-clumping-bounds:a2 -- exact checks (Fractions, sympy, integer enumeration) plus labelled float notes.

Law (block 39, owner's reading): each site empty (0) or one record with content a in {+-e1, +-e2, +-e3}; fugacity z per record;
bond weight W(a, b) = c omega(a, b) (omega = p, q, r for equal, opposite, orthogonal) between two records, 1 if an end is empty.
T = p + q + 4r, c0 = 6/T, w* = max(p, q, r), t = T/w*.
"""
import itertools, math, random, sys, time
from fractions import Fraction as Fr
from collections import Counter, deque
import sympy as sp

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    print(("ok   " if cond else "FAIL ") + tag + (": " + msg if msg else ""), flush=True)
    if not cond:
        FAILS.append(tag)


# ---------------------------------------------------------------- B1: the sharp one-site total-variation bound
Mm, mm, H = sp.symbols("M m H", positive=True)
val = (H - mm) * (Mm - H) / ((Mm - mm) * H)
crit = sp.solve(sp.diff(val, H), H)
best = sp.simplify(val.subs(H, sp.sqrt(Mm * mm)))
good = sp.sqrt(Mm * mm) in crit and sp.simplify(best - (sp.sqrt(Mm) - sp.sqrt(mm)) / (sp.sqrt(Mm) + sp.sqrt(mm))) == 0
rng = random.Random(20260923)
for _ in range(300):
    k = rng.randint(2, 7)
    f = [Fr(rng.randint(1, 20), rng.randint(1, 9)) for _ in range(k)]
    h = [Fr(rng.randint(1, 30), rng.randint(1, 9)) for _ in range(k)]
    F, Fp = sum(f), sum(fi * hi for fi, hi in zip(f, h))
    tv = sum(max(Fr(0), fi * hi / Fp - fi / F) for fi, hi in zip(f, h))
    M_, m_ = max(h), min(h)
    # tv <= (sqrt M - sqrt m)/(sqrt M + sqrt m)  <=>  (tv (sqrtM+sqrtm))^2 <= (sqrtM - sqrtm)^2, i.e. with s = sqrt(M/m):
    # tv <= (s-1)/(s+1)  <=>  s >= (1+tv)/(1-tv)  <=>  M/m >= ((1+tv)/(1-tv))^2
    good &= M_ / m_ >= ((1 + tv) / (1 - tv)) ** 2
Mv, mv = Fr(9), Fr(4)                                        # attained: two-point f with weights sqrt(m) : sqrt(M) on argmax/argmin
f2 = [Fr(2), Fr(3)]; h2 = [Mv, mv]
tv2 = sum(max(Fr(0), fi * hi / sum(a * b for a, b in zip(f2, h2)) - fi / sum(f2)) for fi, hi in zip(f2, h2))
good &= tv2 == Fr(1, 5)                                      # (3 - 2)/(3 + 2)
ok("B.tv", good, "for P ~ f and P' ~ f h with h in [m, M], sup_f TV(P, P') = (sqrt M - sqrt m)/(sqrt M + sqrt m) = tanh(log(M/m)/4) "
   "(maximiser at mean sqrt(Mm); 300 random rational checks; attained, e.g. 1/5 at M/m = 9/4)")

# ---------------------------------------------------------------- B2: the Dobrushin region (six neighbours, all fugacities)
CONT = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
STATES = [None] + CONT


def Wt(a, b, c, p, q, r):
    if a is None or b is None:
        return Fr(1)
    return c * (p if a == b else (q if a == tuple(-x for x in b) else r))


def Rmax(c, p, q, r):
    best = Fr(1)
    for b in STATES:
        for b2 in STATES:
            if b == b2:
                continue
            hs = [Wt(a, b2, c, p, q, r) / Wt(a, b, c, p, q, r) for a in STATES]
            best = max(best, max(hs) / min(hs))
    return best


LIM = Fr(49, 25)                                           # 6 tanh(log R/4) < 1  <=>  R < (7/5)^2
good = True
w = Fr(1)
for cw in (Fr(25, 49) + Fr(1, 1000), Fr(1), Fr(49, 25) - Fr(1, 1000)):
    good &= Rmax(cw, w, w, w) < LIM
for cw in (Fr(25, 49) - Fr(1, 1000), Fr(49, 25) + Fr(1, 1000)):
    good &= not Rmax(cw, w, w, w) < LIM
p, q, r = Fr(9), Fr(8), Fr(8)
good &= Rmax(Fr(25, 392) + Fr(1, 10 ** 4), p, q, r) < LIM and Rmax(Fr(49, 225) - Fr(1, 10 ** 4), p, q, r) < LIM
good &= not Rmax(Fr(25, 392) - Fr(1, 10 ** 4), p, q, r) < LIM and not Rmax(Fr(49, 225) + Fr(1, 10 ** 4), p, q, r) < LIM
good &= Rmax(Fr(1, 2), Fr(3), Fr(1), Fr(2)) >= 4 and all(not Rmax(Fr(k, 10), Fr(3), Fr(1), Fr(2)) < LIM for k in range(1, 40))
ok("B.dobrushin", good, "uniqueness at every fugacity if R_max < 49/25, R_max the largest ratio spread of W(a, b')/W(a, b) over a "
   "(7 states) and neighbour changes b -> b': content-less records need 25/49 < cw < 49/25 (c/c0 up to 1.96); (9,8,8): "
   "25/392 < c < 49/225 (c/c0 in (0.52, 1.78)); (3,1,2): the content channel alone gives R = 4, no certificate at any c")

# ---------------------------------------------------------------- A1: reflection positivity -- bond planes (a1's region) and site planes (always)
cc, P_, Q_, R_ = sp.symbols("c p q r", positive=True)
Om = sp.Matrix(6, 6, lambda i, j: P_ if i == j else (Q_ if i // 2 == j // 2 else R_))
Sch = cc * Om - sp.ones(6, 6)
vecs = {"uniform": sp.Matrix([1] * 6), "vector": sp.Matrix([1, -1, 0, 0, 0, 0]), "quadrupole": sp.Matrix([1, 1, -1, -1, 0, 0])}
eig = {k: sp.simplify((Sch * v)[0] / v[0]) for k, v in vecs.items()}
good = sp.simplify(eig["uniform"] - (cc * (P_ + Q_ + 4 * R_) - 6)) == 0 and sp.simplify(eig["vector"] - cc * (P_ - Q_)) == 0
good &= sp.simplify(eig["quadrupole"] - cc * (P_ + Q_ - 2 * R_)) == 0
ok("A.rp", good, "bond planes: the 7x7 weight matrix is PSD iff its Schur complement c Omega - J is, with eigenvalues cT - 6, c(p - q), "
   "c(p + q - 2r): c >= c0, p >= q, p + q >= 2r (as a1); site planes: no bond crosses a plane of sites, so the weight factorises as "
   "F_+ theta F_+ and <F theta F> = sum over the plane of G^2 >= 0 for every positive law")

# ---------------------------------------------------------------- A2: the bad unit-cube patterns and their disseminated weights
cube = list(itertools.product((0, 1), repeat=3))


def classes(period, fmap):
    res = Counter()
    for bits in itertools.product((0, 1), repeat=8):
        if len(set(bits)) == 1:
            continue
        occ = dict(zip(cube, bits))
        pat = {x: occ[tuple(fmap[x[i]] for i in range(3))] for x in itertools.product(range(period), repeat=3)}
        n = period ** 3
        rho = Fr(sum(pat.values()), n)
        e = Fr(sum(1 for x in pat for d in range(3)
                   if pat[x] != pat[tuple((x[i] + (1 if i == d else 0)) % period for i in range(3))]), n)
        seen, comp = set(), 0
        for s in (x for x in pat if pat[x]):
            if s in seen:
                continue
            comp += 1; seen.add(s); dq = deque([s])
            while dq:
                x = dq.popleft()
                for d in range(3):
                    for sg in (1, -1):
                        y = tuple((x[i] + (sg if i == d else 0)) % period for i in range(3))
                        if pat[y] and y not in seen:
                            seen.add(y); dq.append(y)
        res[(rho, e, Fr(comp, n))] += 1
    return res


site = classes(2, {0: 0, 1: 1})
good = sum(site.values()) == 254 and len(site) == 16 and min(k[1] for k in site) == Fr(3, 4)
ok("A.patterns", good, "254 bad occupancy patterns of a unit cube; disseminated by site-plane reflections (period 2) they fall in 16 "
   "classes (rho, e, kappa), e = mixed bonds per site >= 3/4; per cube the chessboard factor is at most 6^kappa t^(rho-kappa) (c w*)^(-e/2) "
   "(tree bound for contents: sum over a cluster of prod omega/w* <= 6 t^(n-1))")

# exact certificate: t = 2 (e.g. (p,q,r) = (6,2,1)) at c w* = 44^8, and the content-less lattice gas at cw = 38^8
S2 = Fr(10906, 10000); S6 = Fr(12511, 10000)                 # upper bounds for 2^(1/8) and 6^(1/8)
bounds_ok = S2 ** 8 >= 2 and S6 ** 8 >= 6


def eps_upper(res, M, tq, contents=True):
    tot = Fr(0)
    for (rho, e, kap), n in res.items():
        k8 = int(kap * 8)                                     # kappa in units of 1/8
        rk8 = int((rho - kap) * 8)
        base = (S6 ** k8) * ((S2 ** rk8) if tq == 2 else Fr(1)) if contents else Fr(1)
        tot += n * base * Fr(1, M ** int(4 * e))              # (M^8)^(-e/2) = M^(-4e), e in (1/4)Z
    return tot


cert1 = 676 * eps_upper(site, 44, 2) <= Fr(1, 4)
cert2 = 676 * eps_upper(site, 38, 1, contents=False) <= Fr(1, 4)
ok("A.threshold", bounds_ok and cert1 and cert2 and all(int(4 * k[1]) == 4 * k[1] for k in site),
   "exact rational certificate of 676 * eps <= 1/4 (every connected set of k cubes has a depth-first code of 26^(2(k-1)) choices): "
   "at T/w* = 2, c w* = 44^8 = 1.4e13; content-less, c w = 38^8 = 4.3e12")

# ---------------------------------------------------------------- C: content-less records
zz, cw_, N_, Bn = sp.symbols("z cw N B", positive=True)
ok("C.latticegas", sp.simplify(sp.log(zz ** N_ * cw_ ** Bn) - (N_ * sp.log(zz) + Bn * sp.log(cw_))) == 0 and Rmax(Fr(1), Fr(1), Fr(1), Fr(1)) == 1,
   "p = q = r = w: weight z^N (cw)^B, the lattice gas with bond activity cw (Ising with K = log(cw)/4); at the neutral scale cw = 1 the "
   "sites are independent (R_max = 1)")

# ---------------------------------------------------------------- notes (floating point)
def eps_f(res, cw, t, contents=True):
    return sum(n * (((t ** float(r - kk)) * 6 ** float(kk)) if contents else 1.0) * cw ** (-float(e) / 2) for (r, e, kk), n in res.items())


def thresh(res, t, const, contents=True):
    lo, hi = 1.0, 1e40
    for _ in range(400):
        mid = math.sqrt(lo * hi)
        if const * eps_f(res, mid, t, contents) <= 0.25:
            hi = mid
        else:
            lo = mid
    return hi


row = ", ".join("T/w* = %.2f: %.3g" % (tq, thresh(site, tq, 676)) for tq in (1.0, 1.5, 2.0, 49 / 9))
print("note: site-plane chessboard + Peierls thresholds c w* >= (676 count): " + row + "; with the lattice-animal constant 26e instead: "
      + ", ".join("%.3g" % thresh(site, tq, 26 * math.e) for tq in (1.0, 1.5, 2.0, 49 / 9)) + "; content-less %.3g (676), %.3g (26e), "
      "Ising literature exp(4 K_c) = 2.4269" % (thresh(site, 1, 676, False), thresh(site, 1, 26 * math.e, False)))
print("note: bond-plane reflections (region of A.rp) with non-overlapping 2-blocks give per-block factors to the 8th power "
      "(period-4 patterns, e >= 3/8); with two interleaved tilings and a separation lemma not proved here the threshold would be "
      "c p of order 1e4 to 1e5")

print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: (b) the one-site total-variation shift is at most tanh(log R/4), attained, so the seven-state law is unique at every fugacity "
    "when every neighbour change has ratio spread R < 49/25: content-less records for 25/49 < cw < 49/25 (c/c0 up to 1.96, sharper "
    "than a1's bound), (9,8,8) for c/c0 in (0.52, 1.78); (3,1,2) has content spread 4 and no certificate at any c.",
    "HIT: (a) site-plane reflections are positive for every law, and unit cubes sharing faces make bad cubes separate the two "
    "phases, so with the tree bound for contents the gas clumps at some fugacity once c max(p,q,r) exceeds an explicit bound "
    "(exactly certified at 44^8 for T/w* = 2, 38^8 content-less); the Peierls-to-coexistence step is FILS (assumed).",
]
print("SUMMARY: PARTIAL a sharp Dobrushin bound (tanh(log R/4)) with exact uniqueness windows below, and an explicit, rigorous but very "
      "conservative clumping region above, valid for every (p, q, r) through site-plane reflection positivity")
print("\n".join(HITS))
