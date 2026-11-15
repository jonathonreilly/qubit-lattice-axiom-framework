#!/usr/bin/env python3
"""r55n_w1 -- is NORMS Definition N^F-2's vertex norm finite on the nonabelian Wilson vertex at the trivial point?
REVIEW55_NORMS reviewer (claude-opus-5-5). Criteria: checks/r55n_w1_criteria.md (written before this file).
SU(2) Wilson action, exponential chart U_b = e^{A_b}, planar configurations; su(2) = (Q^3, cross product), dot product.
Exact Fraction arithmetic only."""
from fractions import Fraction as Fr
import itertools

out = []
def say(s):
    out.append(s); print(s, flush=True)

Z3 = (0, 0, 0)
def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
def vsub(a, b): return tuple(x - y for x, y in zip(a, b))
def vneg(a): return tuple(-x for x in a)
def vsc(c, a): return tuple(c * x for x in a)
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])

E = [(1, 0), (0, 1)]
def sadd(s, t, per=None):
    r = (s[0] + t[0], s[1] + t[1])
    return (r[0] % per, r[1] % per) if per else r

def plaq_links(s, per=None):
    return [(s, 0), (sadd(s, E[0], per), 1), (sadd(s, E[1], per), 0), (s, 1)]   # b1,b2,b3,b4

def get(F, lk): return F.get(lk, Z3)

def cubic(F, plaqs, per=None, bch=Fr(1, 2), bracket=cross):
    tot = Fr(0)
    for s in plaqs:
        b1, b2, b3, b4 = plaq_links(s, per)
        a = [get(F, b1), get(F, b2), vneg(get(F, b3)), vneg(get(F, b4))]
        X1 = Z3
        for v in a: X1 = vadd(X1, v)
        X2 = Z3
        for i in range(4):
            for j in range(i + 1, 4):
                X2 = vadd(X2, vsc(bch, bracket(a[i], a[j])))
        tot += dot(X1, X2)
    return tot

def fadd(*Fs):
    r = {}
    for F in Fs:
        for k, v in F.items(): r[k] = vadd(r.get(k, Z3), v)
    return r

def T3(X, Y, W, plaqs, per=None, bch=Fr(1, 2), bracket=cross):
    C = lambda F: cubic(F, plaqs, per, bch, bracket)
    return (C(fadd(X, Y, W)) - C(fadd(X, Y)) - C(fadd(X, W)) - C(fadd(Y, W)) + C(X) + C(Y) + C(W))

def curv(F, s, per=None):
    b1, b2, b3, b4 = plaq_links(s, per)
    return vsub(vsub(vadd(get(F, b1), get(F, b2)), get(F, b3)), get(F, b4))

def H(Y, W, plaqs, per=None):
    return sum(dot(curv(Y, s, per), curv(W, s, per)) for s in plaqs)

def dgrad(lam, links, per=None):
    return {(s, nu): vsub(lam.get(sadd(s, E[nu], per), Z3), lam.get(s, Z3)) for (s, nu) in links}

def lbar_br(lam, F, per=None, bracket=cross):
    return {(s, nu): bracket(vadd(lam.get(s, Z3), lam.get(sadd(s, E[nu], per), Z3)), v) for (s, nu), v in F.items()}

# ---- deterministic candidate generator (fixed before any run) ----
class LCG:
    def __init__(self, seed): self.x = seed
    def nxt(self):
        self.x = (1103515245 * self.x + 12345) % (2 ** 31); return self.x
    def vec(self): return tuple((self.nxt() >> 8) % 5 - 2 for _ in range(3))

SITES = [(x, y) for x in range(-1, 4) for y in range(-1, 4)]
BOX_LINKS = [((x, y), nu) for x in range(0, 3) for y in range(0, 3) for nu in (0, 1)]
LAM_SITES = [(0, 0), (1, 0), (0, 1), (1, 1)]
PLAQS = [(x, y) for x in range(-2, 4) for y in range(-2, 4)]    # covers every plaquette touching the supports
ALL_LINKS = [((x, y), nu) for x in range(-2, 5) for y in range(-2, 5) for nu in (0, 1)]

cands = []
for seed in range(1, 21):
    g = LCG(seed)
    lam = {s: g.vec() for s in LAM_SITES}
    Y = {lk: g.vec() for lk in BOX_LINKS}
    W = {lk: g.vec() for lk in BOX_LINKS}
    cands.append((lam, Y, W))

ok0 = ok1 = True; fire1p = 0; nwit = 0; abel_zero = True; first = None
for idx, (lam, Y, W) in enumerate(cands):
    dl = {k: v for k, v in dgrad(lam, ALL_LINKS).items() if v != Z3}
    ok0 &= (H(dl, Y, PLAQS) == 0 and H(dl, W, PLAQS) == 0)
    t = T3(dl, Y, W, PLAQS)
    rhs = Fr(1, 2) * (H(Y, lbar_br(lam, W), PLAQS) + H(W, lbar_br(lam, Y), PLAQS))
    ok1 &= (t == rhs)
    tbad = T3(dl, Y, W, PLAQS, bch=Fr(1))
    if tbad != rhs: fire1p += 1
    if t != 0:
        nwit += 1
        if first is None: first = (idx + 1, t)
    tab = T3(dl, Y, W, PLAQS, bracket=lambda a, b: Z3)
    abel_zero &= (tab == 0)
    say("cand %2d : T(d lam, Y, W) = %s ; Ward RHS = %s ; BCH-1 control T' = %s ; abelian T = %s"
        % (idx + 1, t, rhs, tbad, tab))
say("w1-0 H(d lam, .) == 0 for all candidates: %s" % ok0)
say("w1-1 Ward identity exact for all %d candidates: %s ; control w1-1' (BCH coefficient 1) fired in %d of %d"
    % (len(cands), ok1, fire1p, len(cands)))
say("w1-2 witnesses with T(d lam, Y, W) != 0: %d of %d (first: candidate %s) ; abelian control all zero: %s"
    % (nwit, len(cands), first[0] if first else None, abel_zero))

# ---- w1-3 positive witness ----
lam = {(0, 0): (1, 0, 0), (1, 0): (0, 2, 0), (0, 1): (0, 0, 1), (1, 1): (1, 1, 0)}
mu = {(0, 0): (0, 1, 0), (1, 0): (1, 0, 0), (0, 1): (0, 0, 2), (1, 1): (0, 1, 1), (2, 1): (1, 0, 1)}
dl = {k: v for k, v in dgrad(lam, ALL_LINKS).items() if v != Z3}
dm = {k: v for k, v in dgrad(mu, ALL_LINKS).items() if v != Z3}
Zf = {k: v for k, v in lbar_br(lam, dm).items() if v != Z3}
dZ2 = sum(dot(curv(Zf, s), curv(Zf, s)) for s in PLAQS)
t3 = T3(dl, dm, Zf, PLAQS)
say("w1-3 Z = [lam-bar, d mu]: sum_p |dZ_p|^2 = %s ; T(d lam, d mu, Z) = %s ; (1/2)sum|dZ|^2 = %s"
    % (dZ2, t3, Fr(dZ2, 2)))
ok3 = (dZ2 != 0 and t3 == Fr(dZ2, 2) and t3 > 0)

# ---- w1-4 harmonic modes on a periodic 3x3 torus (informational) ----
P = 3
TPLAQ = [(x, y) for x in range(P) for y in range(P)]
TL = [((x, y), nu) for x in range(P) for y in range(P) for nu in (0, 1)]
hits = 0
for seed in range(1, 11):
    g = LCG(1000 + seed)
    h0, h1 = g.vec(), g.vec()
    hf = {((x, y), nu): (h0 if nu == 0 else h1) for ((x, y), nu) in TL}
    Yt = {lk: g.vec() for lk in TL}
    Wt = {lk: g.vec() for lk in TL}
    dh = [curv(hf, s, P) for s in TPLAQ]
    assert all(v == Z3 for v in dh)
    th = T3(hf, Yt, Wt, TPLAQ, per=P)
    if th != 0: hits += 1
    say("w1-4 torus seed %d: constant h = (%s, %s), dh = 0, T(h, Y, W) = %s" % (seed, h0, h1, th))
say("w1-4 constant (harmonic) modes with T(h,Y,W) != 0: %d of 10 (informational)" % hits)

res = {'w1-0': ok0, 'w1-1': ok1 and fire1p > 0, 'w1-2': nwit > 0 and abel_zero, 'w1-3': ok3}
say("SUMMARY " + " ".join("%s=%s" % (k, "PASS" if v else "FAIL") for k, v in sorted(res.items())))
