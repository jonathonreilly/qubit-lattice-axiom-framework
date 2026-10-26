#!/usr/bin/env python3
"""J:derive:review-20261004-physical-tick-edge-bridge:a1  (same-family, unrefereed)

Self-contained.  numpy, scipy, sympy only.  Every finite claim uses Fractions /
sympy except the two lines explicitly marked [float sample].

What is checked (see ATTEMPT.md for the numbered steps):
  A. units: a_tau/t_P = a_s/l_P = r exactly; r = G_lat^(-1/2); ruler-convention table;
     the repo's own a/l_P = 2 sqrt(pi) (G_kernel = 1/(4 pi)) falls out of the same identity.
  B. support geometry: reach of the one-tick influence set N after n ticks, and the
     inscribed Euclidean radius rho(N) of conv(N) for cubic-symmetric N in the 26-neighbourhood.
  C. the pincer 1 <= c*a_tau/a_s <= rho(N): empty for N = six neighbours, pinned to equality
     exactly when rho(N) = 1.
  D. the Planck packet's own A4 dispersion model sits outside the 6-NN octahedron (l1 norm).
  E. premise-independence counter-models (saturation, record index vs tick, universality,
     tau-relative generator).
"""
from fractions import Fraction as F
from itertools import product, combinations
import math
import sympy as sp
import numpy as np
from scipy.spatial import ConvexHull

PASS = 0
FAIL = 0


def chk(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + (("  | " + detail) if detail else ""))
    return ok


# ------------------------------------------------------------------ A. units
hbar, G, c, a, l, kap = sp.symbols("hbar G c a l kappa", positive=True)
lP = sp.sqrt(hbar * G / c**3)
tP = sp.sqrt(hbar * G / c**5)
chk("A1 t_P = l_P/c (symbolic)", sp.simplify(tP - lP / c) == 0)
a_tau = a / c                               # supplied tie + physical-c bridge (ASSUMED in the packet)
r = a / lP
chk("A2 a_tau / t_P = a_s / l_P = r for every c, hbar, G (symbolic)", sp.simplify(a_tau / tP - r) == 0)

# dimension analysis in (M, L, T) exponents: G ~ M^-1 L^3 T^-2, hbar ~ M L^2 T^-1, c ~ L T^-1, a ~ L
dims = {"G": (-1, 3, -2), "hbar": (1, 2, -1), "c": (0, 1, -1), "a": (0, 1, 0)}
al, be, ga, de = sp.symbols("al be ga de")
eqs = [sum(e * dims[k][i] for e, k in zip((al, be, ga, de), ("G", "hbar", "c", "a"))) for i in range(3)]
sol = sp.solve(eqs, (al, be, ga), dict=True)[0]
chk("A3 the only dimensionless combination of (G,hbar,c,a) is (G hbar c^-3 a^-2)^k",
    sp.simplify(sol[al] / sol[be]) == 1 and sp.simplify(sol[ga] / sol[al]) == -3 and sp.simplify(de / sol[al]) == -2,
    f"solution {sol}")
Glat = G * hbar / (c**3 * a**2)             # Newton coupling in lattice units (hbar = c = a = 1)
chk("A4 r = G_lat^(-1/2)  (so 'r = 1' is the statement G_lat = 1)", sp.simplify(r**-2 - Glat) == 0)

# ruler convention table: a^{-1} = kappa * M_Pl,  M_Pl = sqrt(hbar c / G)
MPl = sp.sqrt(hbar * c / G)
a_ruler = hbar / (kap * MPl * c)
r_ruler = sp.simplify(a_ruler / lP)
chk("A5 ruler a^-1 = kappa M_Pl  gives r = 1/kappa", sp.simplify(r_ruler - 1 / kap) == 0)
tbl = {
    "M_Pl (hbar)": sp.Integer(1),
    "reduced M_Pl/sqrt(8 pi)": 1 / sp.sqrt(8 * sp.pi),
    "h-based sqrt(2 pi) M_Pl": sp.sqrt(2 * sp.pi),
}
vals = {k: sp.simplify(1 / v) for k, v in tbl.items()}
chk("A6 the 'r = 1' fixture holds only for the hbar-Planck mass; reduced mass gives sqrt(8 pi), h-based gives 1/sqrt(2 pi)",
    vals["M_Pl (hbar)"] == 1 and sp.simplify(vals["reduced M_Pl/sqrt(8 pi)"] - sp.sqrt(8 * sp.pi)) == 0
    and sp.simplify(vals["h-based sqrt(2 pi) M_Pl"] - 1 / sp.sqrt(2 * sp.pi)) == 0,
    str(vals))
# cross-check against the repo's own bare-source mismatch (PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md:60-62)
chk("A7 G_lat = 1/(4 pi) (graph-Green coefficient) gives r = 2 sqrt(pi), the repo's old mismatch value",
    sp.simplify(1 / sp.sqrt(sp.Rational(1, 4) / sp.pi) - 2 * sp.sqrt(sp.pi)) == 0)
ccell = sp.symbols("c_cell", positive=True)
r_bp = sp.solve(sp.Eq(ccell / a**2, 1 / (4 * lP**2)), a)[0] / lP
chk("A8 the 06-05 BP same-surface density c_cell/a^2 = 1/(4 l_P^2) gives r = 2 sqrt(c_cell): r = 1 iff c_cell = 1/4 (the premise BP supplies it, the axioms do not)",
    sp.simplify(r_bp - 2 * sp.sqrt(ccell)) == 0 and sp.simplify(r_bp.subs(ccell, sp.Rational(1, 4)) - 1) == 0)

# ---------------------------------------------------------- B. support geometry
def sumset(S, T):
    return {tuple(x + y for x, y in zip(s, t)) for s in S for t in T}


A_ax = {v for v in product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 1}            # 6 axis steps
B_fd = {v for v in product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 2}            # 12 face diagonals
C_bd = {v for v in product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 3}            # 8 body diagonals
chk("B0 orbit sizes 6, 12, 8", (len(A_ax), len(B_fd), len(C_bd)) == (6, 12, 8))


def reach(Nset, n):
    """exact support after n applications of a one-tick influence set (identity allowed)."""
    cur = {(0, 0, 0)}
    step = set(Nset) | {(0, 0, 0)}
    for _ in range(n):
        cur = sumset(cur, step)
    return cur


for n in range(1, 6):
    ok = reach(A_ax, n) == {v for v in product(range(-n, n + 1), repeat=3) if sum(map(abs, v)) <= n}
    if not ok:
        break
chk("B1 six-neighbour reach after n ticks is exactly the l1 octahedron |x|+|y|+|z| <= n (n<=5)", ok)

# three sequential axis layers per tick (x-layer, y-layer, z-layer)
def layered_tick(n):
    cur = {(0, 0, 0)}
    for _ in range(n):
        for ax in range(3):
            e = tuple(1 if i == ax else 0 for i in range(3))
            em = tuple(-x for x in e)
            cur = sumset(cur, {(0, 0, 0), e, em})
    return cur


ok = all(layered_tick(n) == {v for v in product(range(-n, n + 1), repeat=3)} for n in range(1, 5))
chk("B2 three axis layers per tick reach exactly the cube |x|,|y|,|z| <= n (n<=4)", ok)

# strict-locality support lemma with random integer weights (exact): support of W^n is inside the n-step reach
rng = np.random.default_rng(7)
def poly_mul(P, Q):
    out = {}
    for (p, w), (q, u) in product(P.items(), Q.items()):
        k = tuple(x + y for x, y in zip(p, q))
        out[k] = out.get(k, 0) + w * u
    return {k: v for k, v in out.items() if v != 0}
W = {(0, 0, 0): 2}
for v in A_ax:
    W[v] = int(rng.integers(1, 5))
P = {(0, 0, 0): 1}
ok = True
for n in range(1, 6):
    P = poly_mul(P, W)
    ok &= all(sum(map(abs, k)) <= n for k in P)
    ok &= len(P) == len(reach(A_ax, n))      # positive weights: the whole octahedron is realised (no cancellation)
chk("B3 exact integer-weight 6-NN update: support of W^n equals the l1 octahedron (n<=5) -- containment, and realisation for positive weights", ok)


def inradius_sq(Nset):
    """exact squared inradius of conv(N) (origin interior) from integer facet normals."""
    pts = np.array(sorted(Nset), dtype=float)
    hull = ConvexHull(pts)
    best = None
    for simp in hull.simplices:
        p0, p1, p2 = [tuple(int(round(x)) for x in pts[i]) for i in simp]
        u = [p1[i] - p0[i] for i in range(3)]
        w = [p2[i] - p0[i] for i in range(3)]
        nrm = (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])
        d = sum(nrm[i] * p0[i] for i in range(3))
        d2 = F(d * d, sum(x * x for x in nrm))
        best = d2 if best is None or d2 < best else best
    return best


cases = {
    "N = 6 axis steps": A_ax,
    "N = 6 + 12 face diagonals": A_ax | B_fd,
    "N = 6 + 8 body diagonals": A_ax | C_bd,
    "N = all 26": A_ax | B_fd | C_bd,
    "N = three axis layers (cube)": layered_tick(1) - {(0, 0, 0)},
    "N = two six-neighbour layers": sumset(A_ax | {(0, 0, 0)}, A_ax | {(0, 0, 0)}) - {(0, 0, 0)},
}
rho2 = {k: inradius_sq(v) for k, v in cases.items()}
chk("B4 rho^2 (inscribed radius squared of conv N): 6 axis steps -> 1/3", rho2["N = 6 axis steps"] == F(1, 3))
chk("B5 rho^2 = 1 for 6+12, 6+8, all 26, and the three-axis-layer cube",
    all(rho2[k] == 1 for k in ("N = 6 + 12 face diagonals", "N = 6 + 8 body diagonals", "N = all 26",
                               "N = three axis layers (cube)")))
chk("B6 rho^2 = 4/3 for two six-neighbour layers (the hull is the octahedron of radius 2)",
    rho2["N = two six-neighbour layers"] == F(4, 3))
a_, b_, c_ = sp.symbols("a b c", nonnegative=True)
chk("B7 Cauchy-Schwarz identity 3(a^2+b^2+c^2) - (a+b+c)^2 = (a-b)^2+(b-c)^2+(c-a)^2, hence |v|_1 <= sqrt3 |v|_2 with equality on (1,1,1)",
    sp.expand(3 * (a_**2 + b_**2 + c_**2) - (a_ + b_ + c_)**2 - ((a_ - b_)**2 + (b_ - c_)**2 + (c_ - a_)**2)) == 0)

# ------------------------------------------------------------------ C. pincer
# premises: (U_N) strict locality with displacement set N; (S) an axis signal moves one edge per tick;
# (R) all signal speeds <= c and a round cone of speed c exists; (P) physical-c bridge.
# S + (speeds <= c):   a_s/a_tau <= c          i.e.  x := c a_tau / a_s >= 1
# U_N + R (centroid):  c a_tau / a_s <= rho(N)  i.e.  x <= rho(N)
# => x in [1, rho(N)]
interval = {k: (F(1), v) for k, v in rho2.items()}    # [1, rho]; compare squares since both >= 0
empty = [k for k, (lo, hi2) in interval.items() if hi2 < lo * lo]
pinned = [k for k, (lo, hi2) in interval.items() if hi2 == lo * lo]
wide = [k for k, (lo, hi2) in interval.items() if hi2 > lo * lo]
chk("C1 six-neighbour single layer: interval [1, 1/sqrt3] is empty -> (U_6, S, R) inconsistent", empty == ["N = 6 axis steps"], str(empty))
chk("C2 interval is the single point x = 1 (a_tau = a_s/c forced) for 6+12, 6+8, 26, and the cube",
    set(pinned) == {"N = 6 + 12 face diagonals", "N = 6 + 8 body diagonals", "N = all 26", "N = three axis layers (cube)"},
    str(sorted(pinned)))
chk("C3 two six-neighbour layers: x in [1, 2/sqrt3]; a_tau = a_s/c is NOT forced (a_tau only pinned within a factor 1.155)",
    wide == ["N = two six-neighbour layers"])
# minimal number m of six-neighbour sub-steps per tick that leaves room for the round cone: m^2/3 >= 1
m_min = next(m for m in range(1, 10) if F(m * m, 3) >= 1)
chk("C4 smallest m of six-neighbour sub-steps per record tick compatible with a round cone and axis saturation is m = 2; "
    "the sub-step duration is then a_sigma = a_tau/m with a_tau <= (2/sqrt3) a_s/c",
    m_min == 2)
chk("C5 if the six-neighbour update is itself the clock, U_6 + R gives c a_sigma/a_s <= rho = 1/sqrt3, i.e. a_sigma <= r t_P/sqrt3 "
    "(symbolic, using a_s/c = r t_P): a 'minimum step' at r t_P would be a factor sqrt3 too long for a round cone",
    rho2["N = 6 axis steps"] == F(1, 3) and sp.simplify((a / c) / tP - r) == 0)

# ----------------------------------------------- D. the packet's own A4 dispersion model
p1, p2, p3, eps = sp.symbols("p1 p2 p3 epsilon", real=True)
S = sp.sin(p1)**2 + sp.sin(p2)**2 + sp.sin(p3)**2
E = sp.asinh(sp.sqrt(S))
dE = [sp.diff(E, q) for q in (p1, p2, p3)]
pt = {p1: sp.pi / 6, p2: sp.pi / 6, p3: sp.pi / 6}
l1_pt = sp.nsimplify(sum(sp.simplify(g.subs(pt)) for g in dE))
l2_pt = sp.sqrt(sum(sp.simplify(g.subs(pt))**2 for g in dE))
chk("D1 exact point p=(pi/6)(1,1,1): |grad E|_1 = 3/sqrt7 > 1 while |grad E|_2 = sqrt(3/7) < 1",
    sp.simplify(l1_pt - 3 / sp.sqrt(7)) == 0 and sp.simplify(l2_pt - sp.sqrt(3) / sp.sqrt(7)) == 0 and 3 / math.sqrt(7) > 1 > math.sqrt(3 / 7),
    f"l1={l1_pt}, l2={sp.simplify(l2_pt)}")
t = sp.symbols("t", positive=True)
Ed = E.subs({p1: t, p2: t, p3: t})
# gradient component along the diagonal: dE/dp1 at (t,t,t)
comp = sp.simplify(dE[0].subs({p1: t, p2: t, p3: t}))
lim = sp.limit(comp, t, 0, "+")
chk("D2 infrared limit along the body diagonal: each component of grad E -> 1/sqrt3, so |grad E|_1 -> sqrt3 > 1 and |grad E|_2 -> 1",
    sp.simplify(lim - 1 / sp.sqrt(3)) == 0)
gf = sp.lambdify((p1, p2, p3), dE, "numpy")
g = np.linspace(-np.pi, np.pi, 41) + 0.0123
X, Y, Z = np.meshgrid(g, g, g, indexing="ij")
with np.errstate(all="ignore"):
    comps = np.array(gf(X, Y, Z))
l2 = np.sqrt((comps**2).sum(0))
l1 = np.abs(comps).sum(0)
chk("D3 [float sample] on a 41^3 BZ grid, sup |grad E|_2 <= 1 (what the packet's runner tests) but sup |grad E|_1 > 1",
    np.nanmax(l2) <= 1 + 1e-9 and np.nanmax(l1) > 1.2, f"sup l2={np.nanmax(l2):.4f}, sup l1={np.nanmax(l1):.4f}")
chk("D4 hence the sinh model cannot be the (strictly 6-NN-local) one-tick map whose octahedral reach the BFS computes: "
    "centroid lemma needs |v|_1 <= 1 per tick (proved in ATTEMPT.md step 7)", np.nanmax(l1) > 1)

# -------------------------------------------------- E. premise independence
# E1 saturation not implied by locality: a one-tick map of support N = 6 steps that moves content one edge only on odd ticks
def gated_front(n):
    pos = {0}
    for t_ in range(1, n + 1):
        if t_ % 2 == 1:
            pos = {x + d for x in pos for d in (-1, 1)}
    return max(abs(x) for x in pos)
speeds = [F(gated_front(n), n) for n in (2, 4, 6, 8, 10, 12)]
ok_reach = all(gated_front(n) <= n for n in range(1, 13))
chk("E1 gated 6-NN update (shift only on odd ticks): reach bound |x|<=n holds, realised speed = 1/2 edge/tick, so c*a_tau/a_s = 1/2 "
    "and a_tau = a_s/(2c) -- locality alone does not give the tie",
    ok_reach and all(s == F(1, 2) for s in speeds))

# E2 record index vs tick: same record word, many integer tick embeddings
word = ("o1", "o2", "o3", "o4")
embeds = [(0, 1, 2, 3), (0, 2, 4, 6), (0, 1, 3, 6), (5, 9, 10, 40)]
spans = [e[-1] - e[0] for e in embeds]
chk("E2 one record word embeds in the tick lattice with total elapsed ticks 3, 6, 6, 35 (strictly increasing integer maps): "
    "record index is not tick number without a synchrony premise; the 06-06 no-go holds in tick units",
    all(all(e[i] < e[i + 1] for i in range(3)) for e in embeds) and spans == [3, 6, 6, 35])

# E3 tau-relative generator: same transfer, different declared a_tau -> rescaled H (G-SCOPE)
mu, MT, lam, a_t = sp.symbols("mu M_T lambda a_tau", positive=True)
H = lambda at: -sp.log(mu / MT) / (2 * at)
chk("E3 H = -(1/(2 a_tau)) log(T^2/M_T): same T^2, a_tau -> lambda a_tau gives H/lambda (one-clock theorem is tau-relative)",
    sp.simplify(H(lam * a_t) - H(a_t) / lam) == 0)

# E4 universality: two species with speeds 1 and 1/3 edge/tick; which one is 'light' changes a_tau
speeds_sp = [F(1), F(1, 3)]
ratios = [1 / s for s in speeds_sp]          # c*a_tau/a_s when that species is identified with light
chk("E4 two species (speeds 1 and 1/3 edge/tick) both allowed by locality: identifying either one with light gives a_tau = a_s/c or a_s/(3c)",
    ratios == [F(1), F(3)])

# E5 anisotropic regulator: IR slope scales with the temporal hopping coefficient gamma while the reach set does not
gam = sp.symbols("gamma", positive=True)
q = sp.symbols("q", positive=True)
Eg = sp.asinh(gam * sp.sin(q))                               # one-axis slice of sinh E = gamma |sin p|
slope = sp.limit(sp.diff(Eg, q), q, 0, "+")
chk("E5 sinh E = gamma |sin p|: IR speed = gamma edge/tick while the 6-NN reach set is gamma-independent; "
    "a_tau = a_s/c needs gamma = 1 (the kinetic-form clause, matter sector only)", sp.simplify(slope - gam) == 0)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("SUMMARY: with all premises explicit, a tick=edge identification a_tau=a_s/c follows exactly when the one-tick influence set "
      "has inscribed radius 1 (cube-type reach), is empty for a single six-neighbour layer (rho=1/sqrt3), and a_tau=r*t_P still needs the "
      "separate supplier G_lat=1/r^2, none of which is supplied by the axioms or registered primitives.")
raise SystemExit(1 if FAIL else 0)
