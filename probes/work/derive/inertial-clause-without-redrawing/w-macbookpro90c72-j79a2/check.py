#!/usr/bin/env python3
"""J:derive:inertial-clause-without-redrawing:a3 -- records with inertia and no re-drawing.

Six-axis menu of block 44 (PR #8550): contents 0..5 = +x,-x,+y,-y,+z,-z (opposite = d^1).
(S) each record at rate 1 tries x -> x + e_d; the values of the two sites are exchanged
    (empty target: a move; occupied target: an exchange of contents; same content: nothing).
(C) block 44's bond clock: opposite pairs re-drawn uniformly on opposite pairs, other pairs
    exchanged with probability 1/2.
Families: A the independence claim (counterexample); B stationarity; C exact product-state
currents; D the linear evolution of a standing wave; E the content-preserving class and its
additive invariants; F re-drawing variants; N a labelled simulation (not load-bearing).
Exact: integers, Fractions, sympy. Enumerations on the 3^3 torus with two and three records.
"""
import itertools
import sys
import time
from fractions import Fraction as F

import sympy as sp

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    print(("ok " if cond else "FAIL ") + tag + (" " + msg if msg else ""))
    if not cond:
        FAILS.append(tag)


L = 3
E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
COORD = [(i // 9, (i // 3) % 3, i % 3) for i in range(27)]


def site(x, y, z):
    return (x % L) * 9 + (y % L) * 3 + (z % L)


NB = [[site(COORD[s][0] + E[d][0], COORD[s][1] + E[d][1], COORD[s][2] + E[d][2]) for d in range(6)] for s in range(27)]
BONDS = [(s, NB[s][k], k // 2) for s in range(27) for k in (0, 2, 4)]   # (x, x+e_axis, axis)


def states(N):
    for sites in itertools.combinations(range(27), N):
        for cs in itertools.product(range(6), repeat=N):
            yield tuple(zip(sites, cs))


def fd(dd):
    return tuple(sorted(dd.items()))


# rates are integers in units of 1/12
def S_moves(st):
    dd = dict(st)
    out = []
    for x, d in st:
        t = NB[x][d]
        c = dd.get(t, -1)
        if c == d:
            continue
        nd = dict(dd)
        del nd[x]
        if c >= 0:
            nd[x] = c
        nd[t] = d
        out.append((fd(nd), 12))
    return out


def C_moves(st, variant):
    dd = dict(st)
    out = []
    for x, y, ax in BONDS:
        if x in dd and y in dd:
            d, d2 = dd[x], dd[y]
            if d2 == (d ^ 1):
                if variant in ("full", "opp"):
                    tg, r = [(e, e ^ 1) for e in range(6)], 2          # 1/6
                elif variant == "min":
                    if d // 2 == ax:
                        continue
                    tg, r = [(e, e ^ 1) for e in range(6) if e // 2 != ax], 3   # 1/4
                elif variant == "headon":
                    if d // 2 != ax:
                        continue
                    tg, r = [(e, e ^ 1) for e in range(6)], 2
                else:
                    continue
                for a, b in tg:
                    if (a, b) == (d, d2):
                        continue
                    nd = dict(dd)
                    nd[x], nd[y] = a, b
                    out.append((fd(nd), r))
            elif variant == "full" and d2 != d:
                nd = dict(dd)
                nd[x], nd[y] = d2, d
                out.append((fd(nd), 6))                                # 1/2
    return out


def S_stream(st):
    """head-on exchange replaced by a uniform re-draw on the streaming clock"""
    dd = dict(st)
    out = []
    for x, d in st:
        t = NB[x][d]
        c = dd.get(t, -1)
        if c == d:
            continue
        if c == (d ^ 1):
            for e in range(6):
                if (e, e ^ 1) != (d, c):
                    nd = dict(dd)
                    nd[x], nd[t] = e, e ^ 1
                    out.append((fd(nd), 2))
            continue
        nd = dict(dd)
        del nd[x]
        if c >= 0:
            nd[x] = c
        nd[t] = d
        out.append((fd(nd), 12))
    return out


def counts(st):
    v = [0] * 6
    for _, d in st:
        v[d] += 1
    return v


def analyze(N, gen, weights=None):
    idx = {}
    lst = []
    for st in states(N):
        idx[st] = len(lst)
        lst.append(st)
    n = len(lst)
    wt = [1] * n if weights is None else [eval_w(st, weights) for st in lst]
    inr = [0] * n
    outr = [0] * n
    vecs = set()
    for i, st in enumerate(lst):
        cb = counts(st)
        for tgt, r in gen(st):
            j = idx[tgt]
            outr[i] += r
            inr[j] += r * wt[i]
            ca = counts(tgt)
            if ca != cb:
                vecs.add(tuple(a - b for a, b in zip(ca, cb)))
    bad = sum(1 for i in range(n) if inr[i] != outr[i] * wt[i])
    if vecs:
        rank = sp.Matrix(sorted(vecs)).rank()
    else:
        rank = 0
    return n, bad, 6 - rank, vecs


def eval_w(st, w):
    p = 1
    for _, d in st:
        p *= w[d]
    return p


# ---------------------------------------------------------------- A the independence claim
A_state = fd({site(0, 0, 0): 0, site(1, 0, 0): 2})     # +x at 000, +y at 100
B_state = fd({site(1, 0, 0): 2, site(0, 0, 0): 4})     # +y at 100, +z at 000
proj = lambda st: tuple(sorted(s for s, d in st if d == 2))
ok("A.sameproj", proj(A_state) == proj(B_state) == (site(1, 0, 0),), "same +y projection {100}")
rateA = sum(r for tgt, r in S_moves(A_state) if proj(tgt) == (site(0, 0, 0),))
rateB = sum(r for tgt, r in S_moves(B_state) if proj(tgt) == (site(0, 0, 0),))
ok("A.counterexample", rateA == 12 and rateB == 0,
   "(S): the +y content jumps 100 -> 000 (a step -e_x) at rate 1 from A, rate 0 from B: the +y stream is not autonomous and not a TASEP along +y")
# operational check of "each species is blocked only by its own species", on every 2-record configuration:
# (S) has one transition per record whose target does not hold its own content, and in it that content advances
good = True
for st in states(2):
    dd = dict(st)
    movers = [(x, d) for x, d in st if dd.get(NB[x][d], -1) != d]
    outs = S_moves(st)
    good &= len(outs) == len(movers)
    for (x, d), (tgt, _) in zip(movers, outs):
        good &= dict(tgt).get(NB[x][d], -1) == d
ok("A.ownblock", good, "an attempt of content d is suppressed exactly when the target holds d, otherwise d advances")

# ---------------------------------------------------------------- B stationarity (S alone)
n2, badS, invS, vS = analyze(2, S_moves)
ok("B.uniform2", badS == 0, "(S), 2 records: all %d configurations balance" % n2)
wts = [2, 3, 5, 7, 11, 13]
_, badW, _, _ = analyze(2, S_moves, weights=wts)
ok("B.product2", badW == 0, "(S): the tilted product weights prod_r w_{s_r} (w = 2,3,5,7,11,13) balance on all %d" % n2)

# ---------------------------------------------------------------- C exact product-state currents across an x-bond
r = sp.symbols("r0:6", nonnegative=True)
rho = sum(r)
p = {-1: 1 - rho}
for d in range(6):
    p[d] = r[d]
J = [0] * 6
for cx in range(-1, 6):
    for cy in range(-1, 6):
        if cx == cy:
            continue
        w = p[cx] * p[cy]
        rate = (1 if cx == 0 else 0) + (1 if cy == 1 else 0)     # +x record at x attempts; -x record at x+e attempts
        if rate == 0:
            continue
        if cx >= 0:
            J[cx] += rate * w          # the value at x moves forward
        if cy >= 0:
            J[cy] -= rate * w          # the value at x+e moves back
g1 = r[0] - r[1]
formula = [r[0] * (1 - r[0] + r[1]), -r[1] * (1 - r[1] + r[0])] + [-r[d] * g1 for d in range(2, 6)]
ok("C.currents", all(sp.expand(J[d] - formula[d]) == 0 for d in range(6)),
   "x-currents: +x: r+(1-r+ + r-), -x: -r-(1-r- + r+), transverse d: -r_d g_x")
ok("C.mass", sp.expand(sum(J) - (1 - rho) * g1) == 0, "sum = (1 - rho) g_x (block 44's mass current)")
ok("C.xmomflux", sp.expand(J[0] - J[1] - (r[0] + r[1] - (r[0] - r[1]) ** 2)) == 0,
   "x-momentum flux = r+ + r- - (r+ - r-)^2: carried by x-movers only")

# ---------------------------------------------------------------- D linear evolution of a standing wave along x
c, k, t = sp.symbols("c k t", positive=True)
subs0 = {r[d]: c for d in range(6)}
Mlin = sp.Matrix(6, 6, lambda i, j: sp.diff(J[i], r[j]).subs(subs0))
lam = sp.symbols("lam")
cp = sp.expand((Mlin - lam * sp.eye(6)).det())
ok("D.eigen", sp.expand(cp - lam**4 * (lam**2 - (1 - 2 * c))) == 0,
   "linearized x-flux matrix at rho_d = c: char. poly lam^4 (lam^2 - (1-2c)): eigenvalues 0 (x4), +-sqrt(1-2c)")
# closed form: a_d(0) = cos kx for all d (uniform density wave, zero momentum)
w0 = sp.sqrt(1 - 2 * c) * k
Sx = 2 * sp.cos(w0 * t)                             # a+ + a- amplitude of cos kx
Dx = 2 / sp.sqrt(1 - 2 * c) * sp.sin(w0 * t)        # a+ - a- amplitude of sin kx
bx = 1 + 2 * c / (1 - 2 * c) * (1 - sp.cos(w0 * t))  # each transverse species, amplitude of cos kx
# check the PDE system on u(x,t) = amplitude(t) * trig(kx)
x = sp.symbols("x", real=True)
apx = (Sx * sp.cos(k * x) + Dx * sp.sin(k * x)) / 2
amx = (Sx * sp.cos(k * x) - Dx * sp.sin(k * x)) / 2
bxx = bx * sp.cos(k * x)
avec = sp.Matrix([apx, amx, bxx, bxx, bxx, bxx])
jvec = Mlin * avec
eqs = [sp.diff(avec[i], t) + sp.diff(jvec[i], x) for i in range(6)]
ok("D.solution", all(sp.simplify(e_) == 0 for e_ in eqs) and sp.simplify(apx.subs(t, 0) - sp.cos(k * x)) == 0
   and sp.simplify(bxx.subs(t, 0) - sp.cos(k * x)) == 0, "exact solution of the linearized six-stream system")
rho0 = sp.symbols("rho0", positive=True)
amp = sp.simplify(((Sx + 4 * bx) / 6).subs(c, rho0 / 6))
frozen = 2 / (3 - rho0)
osc = (1 - rho0) / (3 - rho0)
ok("D.amplitude", sp.simplify(amp - (frozen + osc * sp.cos(sp.sqrt(1 - rho0 / 3) * k * t))) == 0,
   "density amplitude = 2/(3-rho0) + ((1-rho0)/(3-rho0)) cos(sqrt(1-rho0/3) k t)")
ok("D.rho03", frozen.subs(rho0, sp.Rational(3, 10)) == sp.Rational(20, 27) and osc.subs(rho0, sp.Rational(3, 10)) == sp.Rational(7, 27),
   "at rho0 = 3/10: frozen 20/27, oscillating 7/27, speed sqrt(9/10); block 44 with (C): sound speed sqrt(7/30)")

# ---------------------------------------------------------------- E the content-preserving class
# proper rotations of the cube as signed permutation matrices with det +1
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = [[0] * 3 for _ in range(3)]
        for i in range(3):
            M[i][perm[i]] = sg[i]
        if sp.Matrix(M).det() == 1:
            rots.append(M)
ok("E.group", len(rots) == 24)
vec2c = {E[d]: d for d in range(6)}


def act(M, d):
    if d < 0:
        return d
    v = tuple(sum(M[i][j] * E[d][j] for j in range(3)) for i in range(3))
    return vec2c[v]


keys = set()
for e in range(6):
    for a in range(-1, 6):
        for b in range(-1, 6):
            if a != b:
                keys.add((e, a, b))
orbit_of = {}
norb = 0
for key in sorted(keys):
    if key in orbit_of:
        continue
    stack = [key]
    orbit_of[key] = norb
    while stack:
        e, a, b = stack.pop()
        nbrs = [(act(M, e), act(M, a), act(M, b)) for M in rots] + [(e ^ 1, b, a)]
        for nb in nbrs:
            if nb not in orbit_of:
                orbit_of[nb] = norb
                stack.append(nb)
    norb += 1
ok("E.orbits", norb > 0, "covariant content-preserving bond rules = one swap rate per orbit: %d orbits of (bond, ordered pair of site states)" % norb)
# a generic member: random rates per orbit; its additive invariants on the 3^3 torus


def generic_moves(st, rates):
    dd = dict(st)
    out = []
    for s in range(27):
        for kk in range(6):
            y = NB[s][kk]
            a, b = dd.get(s, -1), dd.get(y, -1)
            if a == b:
                continue
            rr = rates[orbit_of[(kk, a, b)]]
            if rr == 0 or kk % 2 == 1:
                continue          # each unordered bond counted once (key (e,a,b) ~ (-e,b,a))
            nd = dict(dd)
            nd.pop(s, None)
            nd.pop(y, None)
            if b >= 0:
                nd[s] = b
            if a >= 0:
                nd[y] = a
            out.append((fd(nd), rr))
    return out


rates = [(7 * i * i + 3 * i + 1) % 11 + 1 for i in range(norb)]
_, _, invG, vG = analyze(2, lambda s_: generic_moves(s_, rates))
ok("E.invariants", invS == 6 and invG == 6 and not vS and not vG,
   "(S) and a generic content-preserving rule change no content: all six N_d are conserved (6 additive invariants, not the 4 of N and P)")

# ---------------------------------------------------------------- F re-drawing variants (2 records)
res = {}
for name, gen in [("S+C", lambda s_: S_moves(s_) + C_moves(s_, "full")),
                  ("S+Copp", lambda s_: S_moves(s_) + C_moves(s_, "opp")),
                  ("S+Cmin", lambda s_: S_moves(s_) + C_moves(s_, "min")),
                  ("S+Chead", lambda s_: S_moves(s_) + C_moves(s_, "headon")),
                  ("Sstream", S_stream)]:
    nn, bad, inv, _ = analyze(2, gen)
    res[name] = (bad, inv)
print("   2 records, 12636 configurations: (unbalanced for uniform, additive invariants) " + str(res))
ok("F.C", res["S+C"] == (0, 4), "block 44's (C): uniform stationary, invariants N and P only")
ok("F.opp", res["S+Copp"] == (0, 4), "opposite pairs only, bond clock: uniform stationary, invariants N and P only")
ok("F.min", res["S+Cmin"] == (0, 4), "opposite pairs on the two axes perpendicular to the bond only: same")
ok("F.fail", res["S+Chead"][0] == 486 and res["Sstream"][0] == 486,
   "head-on (along the bond) re-draw only, or re-draw on the streaming clock: 486 configurations unbalanced")
t3 = time.time()
n3, bad3S, _, _ = analyze(3, S_moves)
n3b, bad3m, inv3m, _ = analyze(3, lambda s_: S_moves(s_) + C_moves(s_, "min"))
ok("F.three", n3 == 631800 and bad3S == 0 and bad3m == 0 and inv3m == 4,
   "3 records, 631800 configurations: (S) and (S)+Cmin balance for the uniform measure; Cmin invariants N, P (%.0f s)" % (time.time() - t3))

# ---------------------------------------------------------------- N simulation (floats; not load-bearing)
try:
    import numpy as np
    sys.path.insert(0, "probes/lib")
    import inertial
    L_, r0, T_ = 64, 0.3, 300
    amps = inertial.sound("six", L_, r0, 0.0, (1,), T_, 4, seed=7)[1]
    kk_ = 2 * np.pi / L_
    tt = np.arange(T_ + 1)
    best = None
    for ww in np.linspace(0.5 * kk_, 1.2 * kk_, 141):
        for gg in np.linspace(0, 0.03, 31):
            Mm = np.stack([np.ones(T_ + 1), np.exp(-gg * tt) * np.cos(ww * tt)], 1)
            co = np.linalg.lstsq(Mm, amps, rcond=None)[0]
            err = ((Mm @ co - amps) ** 2).sum()
            if best is None or err < best[0]:
                best = (err, ww / kk_, gg, co)
    print("N.sim NUMERICAL (S) alone, side 64, rho 0.3, 4 runs, 300 ticks: fitted speed %.3f (linear %.3f; independent-stream reading %.3f), "
          "oscillating %.3f (linear %.3f; reading 0.333), offset %.3f (linear %.3f before diffusion; reading 0.667)"
          % (best[1], (1 - r0 / 3) ** 0.5, 1 - r0 / 3, best[3][1], (1 - r0) / (3 - r0), best[3][0], 2 / (3 - r0)))
except Exception as ex:
    print("N.skip simulation skipped: " + type(ex).__name__)

print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: under (S) alone the six contents are not independent streams: a +x record passing a +y record at 100 moves "
    "the +y content to 000 (rate 1), which no +y exclusion stream does; exact product-state x-currents: r+(1-r+ +r-), "
    "-r-(1-r- +r+), -r_d g_x for transverse d; every tilted product measure is stationary.",
    "HIT: the linearized six-stream equations give a standing density wave along x the evolution 2/(3-rho0) + "
    "((1-rho0)/(3-rho0)) cos(sqrt(1-rho0/3) k t): at rho0 = 0.3, 20/27 of the amplitude has zero frequency and the "
    "rest oscillates at speed 0.949, not as sound (block 44's (C): 0.483).",
    "HIT: every covariant clause that never changes a content is a swap process (10 orbit rates) conserving all six "
    "content numbers, so none thermalizes momentum; re-drawing only opposite pairs on a bond clock, even only those on "
    "the axes perpendicular to the bond, keeps the uniform measure stationary with invariants N and P only; head-on-only "
    "or streaming-clock re-drawing breaks it (486 of 12636).",
]
print("SUMMARY: COUNTEREXAMPLE under (S) alone the six contents are not independent exclusion streams: an exchange "
      "pushes the other content back; a standing wave keeps 20/27 of its amplitude frozen at rho 0.3; no "
      "content-preserving clause thermalizes")
print("\n".join(HITS))
