#!/usr/bin/env python3
"""Referee and sharpen: the depolarized commuting pointer cannot carry the routed record law through a positive evolution.
J:derive:deferred-20260926-quantum-record-codes-and-pointers:a1

Supplied model (Codex campaign 12h_third, DIMER_FIXED_ENCODING_QUANTUM_CONTRACTION.md + DEPOLARIZED_POINTER_RATE_BOUNDARY.md):
N=12 torus, even sublattice U (864 sites), 14 colours (6 A with e=+-e_i, 8 B with b in {+-1}^3), routes delta != +e1,
a = delta - e1, stencil (u-a, u, u+a, u+2a) = (l,c,d,r), swap (c,d) at rate k0/2 + h/4, k0=11/10, gamma=1,
S_delta(c,d) = (gamma/2) delta.(e_c x b_d + e_d x b_c), h = S(l,c)+S(c,r)-S(l,d)-S(d,r).
Pointer states rho_a = (1-eta)|a><a| + (eta/14) I; preparation matrix B = rI + q11^T (r=1-eta, q=eta/14).
Required generator on the pointer diagonal: G = B^K L B^-K; positivity needs G_{x,y} >= 0 for x != y.

R  referee of the author's witness (three consecutive route positions, colours (b,c,a) -> (a,b,c)):
   R1 model facts; R2 B^-1; R3 torus stencils; R4 closed form for every eta (symbolic pair identity);
   R5 exact torus-level values; R6 an independent tensor-propagation algorithm at eta = 1/2
N  new: a witness negative at FIRST order in eta, exact for every 0 < eta < 1
D  diagnostic (not proof): single-site entries in random contexts
"""
import hashlib, itertools, os, random, subprocess, sys, time
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time()
FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

SRC = "probes/work/deferred-science-20260926/mobile-record-formation-20260920/campaign12h_third"
for f in ("DEPOLARIZED_POINTER_RATE_BOUNDARY.md", "DIMER_FIXED_ENCODING_QUANTUM_CONTRACTION.md", "noisy_pointer_generator_check.py", "APPROACH_REGISTRY.md"):
    p = os.path.join(SRC, f)
    print(f"   source {f}: sha256 {hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else 'MISSING'}")

# ---------------- model ----------------
LAB = []
for i in range(3):
    for s in (1, -1):
        e = [0, 0, 0]; e[i] = s; LAB.append(('A', tuple(e), (0, 0, 0)))
for bb in itertools.product((1, -1), repeat=3): LAB.append(('B', (0, 0, 0), bb))
def cross(u, v): return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
def dot(u, v): return sum(x*y for x, y in zip(u, v))
def Smat(delta):
    return [[Fr(1, 2)*dot(delta, tuple(x+y for x, y in zip(cross(LAB[c][1], LAB[d][2]), cross(LAB[d][1], LAB[c][2])))) for d in range(14)] for c in range(14)]
ROUTES = [(-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SM = {dl: Smat(dl) for dl in ROUTES}
K0 = Fr(11, 10)
print("== R1 model facts")
okS = all(SM[d][i][j] == SM[d][j][i] and SM[d][i][i] == 0 for d in ROUTES for i in range(14) for j in range(14))
okZ = all(sum(SM[d][i]) == 0 for d in ROUTES for i in range(14))
check("R1a every S_delta is symmetric with zero diagonal", okS)
check("R1b every S_delta has zero row sums (sum of b over B labels and of e over A labels vanish)", okZ)
check("R1c |S| <= 1/2 so every rate k0/2 + h/4 >= 1/20 > 0", all(abs(SM[d][i][j]) <= Fr(1, 2) for d in ROUTES for i in range(14) for j in range(14)))
idx = lambda kind, e, b: LAB.index((kind, e, b))
a_ = idx('A', (0, 1, 0), (0, 0, 0)); b_ = idx('B', (0, 0, 0), (-1, -1, -1)); c_ = idx('B', (0, 0, 0), (1, -1, -1))
S1 = SM[(-1, 0, 0)]
check("R1d author's colours: S_-e1(a,b) = S_-e1(a,c) = 1/2", S1[a_][b_] == Fr(1, 2) and S1[a_][c_] == Fr(1, 2))

print("== R2 preparation matrix")
eta = sp.Symbol('eta', positive=True)
r_, q_ = 1 - eta, eta/14
Bs = sp.Matrix(14, 14, lambda i, j: (r_ if i == j else 0) + q_)
Bis = sp.Matrix(14, 14, lambda i, j: ((1 if i == j else 0) - q_)/r_)
check("R2 B^-1 = (I - q 11^T)/r exactly (r + 14 q = 1)", sp.simplify(Bs*Bis - sp.eye(14)) == sp.zeros(14))

def Bmats(e):
    r, q = 1 - e, e/14
    return ([[(r if i == j else 0) + q for j in range(14)] for i in range(14)], [[((1 if i == j else 0) - q)/r for j in range(14)] for i in range(14)])
def pair(B, Bi, S, i, j, k, l):
    wa = [B[i][s]*Bi[s][k] for s in range(14)]; wb = [B[j][t]*Bi[t][l] for t in range(14)]
    return sum(wa[s]*S[s][t]*wb[t] for s in range(14) for t in range(14) if S[s][t])
def stencil_entry(B, Bi, S, x, y):
    """[B^4 L_e B^-4]_{x,y}: constant part (k0/2)(P - I) and h/4 part (P - I) sum(+-K_pair), factorised."""
    xl, xc, xd, xr = x; yl, yc, yd, yr = y
    d = lambda p, q: 1 if p == q else 0
    tot = 0
    for (Xl, Xc, Xd, Xr), sg in (((xl, xd, xc, xr), 1), ((xl, xc, xd, xr), -1)):
        tot += sg*K0/2*d(Xl, yl)*d(Xc, yc)*d(Xd, yd)*d(Xr, yr)
        tot += sg*Fr(1, 4)*(pair(B, Bi, S, Xl, Xc, yl, yc)*d(Xd, yd)*d(Xr, yr) + pair(B, Bi, S, Xc, Xr, yc, yr)*d(Xl, yl)*d(Xd, yd)
                            - pair(B, Bi, S, Xl, Xd, yl, yd)*d(Xc, yc)*d(Xr, yr) - pair(B, Bi, S, Xd, Xr, yd, yr)*d(Xl, yl)*d(Xc, yc))
    return tot

print("== R3 torus stencils")
N = 12
U = [u for u in itertools.product(range(N), repeat=3) if sum(u) % 2 == 0]
def add(u, v, k=1): return tuple((x + k*y) % N for x, y in zip(u, v))
EDGES = []
for dl in ROUTES:
    a = tuple(x - y for x, y in zip(dl, (1, 0, 0)))
    for u in U: EDGES.append((dl, (add(u, a, -1), u, add(u, a), add(u, a, 2))))
check("R3a 864 sites x 5 routes = 4320 routed stencils, four distinct positions each", len(U) == 864 and len(EDGES) == 4320 and all(len(set(st)) == 4 for _, st in EDGES))
u0, u1, u2 = (0, 0, 0), (10, 0, 0), (8, 0, 0)
cont = [st for _, st in EDGES if {u0, u1, u2} <= set(st)]
check("R3b exactly two stencils contain the three consecutive delta=-e1 positions (0,0,0),(10,0,0),(8,0,0)",
      sorted(cont) == sorted([((2, 0, 0), u0, u1, u2), (u0, u1, u2, (6, 0, 0))]), str(cont))
def G_entry(e, cx, cy, default):
    B, Bi = Bmats(e)
    D = {p for p in set(cx) | set(cy) if cx.get(p, default) != cy.get(p, default)}
    tot = Fr(0)
    for dl, st in EDGES:
        if D <= set(st):
            tot += stencil_entry(B, Bi, SM[dl], tuple(cx.get(p, default) for p in st), tuple(cy.get(p, default) for p in st))
    return tot

print("== R4 closed form of the author's entry for every eta (symbolic pair identity)")
Bl = [[Bs[i, j] for j in range(14)] for i in range(14)]; Bil = [[Bis[i, j] for j in range(14)] for i in range(14)]
Ss = [[sp.Rational(v.numerator, v.denominator) for v in row] for row in S1]
okpair = True
for i, j in [(a_, b_), (a_, c_), (b_, c_), (0, 13), (3, 9)]:
    val = sp.simplify(pair(Bl, Bil, Ss, i, j, j, i) - q_**2*(1 + r_**2)*Ss[i][j]/r_**2)
    if val != 0: okpair = False
check("R4a (K_S)_{ij,ji} = q^2 (1 + r^2) S_ij / r^2 (symbolic eta, sampled colour pairs)", okpair)
auth = -eta**2*(1 + (1 - eta)**2)/(784*(1 - eta)**2)
e_auth = sp.simplify(stencil_entry(Bl, Bil, Ss, (5, a_, b_, c_), (5, b_, c_, a_)) + stencil_entry(Bl, Bil, Ss, (a_, b_, c_, 5), (b_, c_, a_, 5)))
check("R4b author's entry = -eta^2 [1 + (1-eta)^2] / [784 (1-eta)^2] for symbolic eta", sp.simplify(e_auth - auth) == 0, str(sp.factor(e_auth)))

print("== R5 torus-level exact values")
for ev in (Fr(1, 2), Fr(1, 5), Fr(9, 10)):
    v = G_entry(ev, {u0: a_, u1: b_, u2: c_}, {u0: b_, u1: c_, u2: a_}, 7)
    check(f"R5 eta={ev}: author's entry on the full torus", v == Fr(-1)*ev**2*(1 + (1 - ev)**2)/(784*(1 - ev)**2), str(v))

print("== R6 independent algorithm: tensor propagation on the 14^4 stencil space (eta = 1/2)")
def propagate(e, S, x, y):
    B, Bi = Bmats(e)
    n = 14
    # v = (B^-1)^{x4} e_y : v[z] = prod_p Bi[z_p][y_p]
    v = {}
    cols = [[Bi[z][y[p]] for z in range(n)] for p in range(4)]
    for z in itertools.product(range(n), repeat=4):
        val = cols[0][z[0]]*cols[1][z[1]]*cols[2][z[2]]*cols[3][z[3]]
        if val: v[z] = val
    # w = L_e v  (rate(z) moves weight from z to swap(z))
    wv = {}
    for z, val in v.items():
        if z[1] == z[2]: continue
        l, c, d, r = z
        h = S[l][c] + S[c][r] - S[l][d] - S[d][r]
        rate = K0/2 + h/4
        zs = (l, d, c, r)
        wv[zs] = wv.get(zs, 0) + rate*val
        wv[z] = wv.get(z, 0) - rate*val
    # entry = (B^{x4} w)_x
    return sum(B[x[0]][z[0]]*B[x[1]][z[1]]*B[x[2]][z[2]]*B[x[3]][z[3]]*val for z, val in wv.items())
p1 = propagate(Fr(1, 2), S1, (5, a_, b_, c_), (5, b_, c_, a_)); p2 = propagate(Fr(1, 2), S1, (a_, b_, c_, 5), (b_, c_, a_, 5))
check("R6 propagation gives the two stencil contributions -5/6272 each, total -5/3136", p1 == Fr(-5, 6272) and p2 == Fr(-5, 6272), f"{p1}, {p2}")

print("== N  a witness negative at first order in eta")
Ap = idx('A', (0, 1, 0), (0, 0, 0)); Am = idx('A', (0, -1, 0), (0, 0, 0))
Bp = idx('B', (0, 0, 0), (1, 1, 1)); Bm = idx('B', (0, 0, 0), (1, 1, -1))
# y = (A+e2, B(.,.,+1), B(.,.,-1)) at (u0,u1,u2); x = (A-e2, B(.,.,-1), B(.,.,+1)): swap at (u1,u2) plus a changed end colour at u0
new = eta*(eta - 2)*(eta**2 - 14*eta + 14)/(784*(eta - 1)**2)
e_new = sp.simplify(stencil_entry(Bl, Bil, Ss, (5, Am, Bm, Bp), (5, Ap, Bp, Bm)) + stencil_entry(Bl, Bil, Ss, (Am, Bm, Bp, 5), (Ap, Bp, Bm, 5)))
check("N1 exact entry = eta (eta - 2)(eta^2 - 14 eta + 14) / [784 (1 - eta)^2] for symbolic eta", sp.simplify(e_new - new) == 0, str(sp.factor(e_new)))
roots = sp.solve(eta**2 - 14*eta + 14, eta)
check("N2 negative for every 0 < eta < 1: eta > 0, eta - 2 < 0, roots 7 -+ sqrt 35 of the quadratic lie above 1",
      all(sp.N(rt) > 1 for rt in roots) and sp.sympify(14) > 0, str(roots))
ser = sp.series(new, eta, 0, 3).removeO()
check("N3 leading order: -eta/28 - eta^2/56 (the author's witness starts at -eta^2/392)", sp.simplify(ser - (-eta/28 - eta**2/56)) == 0 and sp.simplify(sp.series(auth, eta, 0, 3).removeO() + eta**2/392) == 0)
for ev in (Fr(1, 2), Fr(1, 5), Fr(1, 100)):
    v = G_entry(ev, {u0: Am, u1: Bm, u2: Bp}, {u0: Ap, u1: Bp, u2: Bm}, 7)
    check(f"N4 eta={ev}: new witness on the full torus", v == ev*(ev - 2)*(ev**2 - 14*ev + 14)/(784*(ev - 1)**2), str(v))
check("N5 at eta = 1/2 the new entry -87/3136 is 17.4 times the author's -5/3136", G_entry(Fr(1, 2), {u0: Am, u1: Bm, u2: Bp}, {u0: Ap, u1: Bp, u2: Bm}, 7) == Fr(-87, 3136))
pn = propagate(Fr(1, 2), S1, (5, Am, Bm, Bp), (5, Ap, Bp, Bm)) + propagate(Fr(1, 2), S1, (Am, Bm, Bp, 5), (Ap, Bp, Bm, 5))
check("N6 tensor propagation reproduces -87/3136", pn == Fr(-87, 3136), str(pn))

print("== D  diagnostic: single-site entries in random contexts (float-free exact values at eta = 1/1000; a search, not a bound)")
random.seed(20260926)
near = sorted({p for _, st in EDGES if u0 in st for p in st} - {u0})
worst = Fr(0)
for trial in range(150):
    ctx = {p: random.randrange(14) for p in near}
    yu = random.randrange(14); xu = random.choice([c for c in range(14) if c != yu])
    cx = dict(ctx); cx[u0] = xu; cy = dict(ctx); cy[u0] = yu
    worst = min(worst, G_entry(Fr(1, 1000), cx, cy, 0)*1000)
print(f"   most negative single-site entry / eta over 150 contexts: {float(worst):.5f} (compare -1/28 = {-1/28:.5f})")
check("D1 single-site entries are also negative at first order in some context", worst < 0)

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PROVED (referee + sharpening): the author's entry -eta^2[1+(1-eta)^2]/[784(1-eta)^2] is reproduced for every "
          "eta by a symbolic pair identity and two independent exact computations; NEW: an entry "
          "eta(eta-2)(eta^2-14eta+14)/[784(1-eta)^2] = -eta/28 + O(eta^2) < 0 for all 0<eta<1, so positivity already fails at "
          "first order in the noise and any positive implementation has generator error >= eta/28 - O(eta^2)")
    print("HIT depolarized pointer: required generator is negative at first order in eta (exact witness), author's O(eta^2) entry confirmed cross-model")
