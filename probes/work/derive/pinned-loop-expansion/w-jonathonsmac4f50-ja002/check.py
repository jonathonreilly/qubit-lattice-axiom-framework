"""pinned-loop-expansion, attempt a4 (w-jonathonsmac4f50-ja002): part (c) at the pinned scale - what 'large l_1' can supply.  Exact.

Six-axis menu at c0 = 6/S (S = p + q + 4r): W = c0 omega = 6 K1, W_eq = 6p/S.  A configuration (occupied set A, contents s) weighs
z^|A| prod_{E(A)} W(s_e).  The balance point z_t = W_eq^-3 gives the empty and the fully occupied aligned configurations weight 1 per
site.  A: the balance-point energy, the l_1 -> 1 limit, FKG.  B: the chessboard route (site-only bond-plane reflections).  D: heuristics.
"""
import itertools
import os
import random
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from loopexp import AX, Kmat, grid, phi_brute

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


def Wm(p, q, r):
    S = p + q + 4 * r
    return [[F(6 * (p if a == b else q if a[1] == b[1] else r), S) for b in AX] for a in AX]


def torus(L):
    V = list(itertools.product(range(L), repeat=3))
    E = []
    for v in V:
        for j in range(3):
            w = list(v); w[j] = (w[j] + 1) % L; E.append((v, tuple(w)))
    return V, E


def ncomp(A, EA):
    par = {x: x for x in A}
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for u, v in EA: par[f(u)] = f(v)
    return len({f(x) for x in A})


def induced(E, A):
    S = set(A)
    return [e for e in E if e[0] in S and e[1] in S]


def boundary(E, A):
    S = set(A)
    return sum(1 for u, v in E if (u in S) != (v in S))


random.seed(20260922)
TRIPLES = [(3, 1, 2), (16, 1, 2), (100, 1, 2), (5, 1, 1), (7, 2, 1), (1000, 1, 1)]

# ------------------------------------------------------------------ A1: the cap
ok = True
for (p, q, r) in TRIPLES:
    W = Wm(p, q, r); Weq = W[0][0]; S = p + q + 4 * r; l1 = F(p - q, S)
    ok = ok and all(sum(row) == 6 for row in W) and max(max(row) for row in W) == Weq and 6 * l1 <= Weq < 6 and Weq >= 1
want("A1 at c0 every row of W sums to 6 (W = 6 K1, K1 a probability kernel), so no record-record weight exceeds 6; W_eq = 6p/S is the "
     "largest entry and 6 l1 <= W_eq < 6 at (3,1,2), (16,1,2), (100,1,2), (5,1,1), (7,2,1), (1000,1,1)", ok)

# ------------------------------------------------------------------ A2: the balance-point energy on the 3^3 torus
Vt, Et = torus(3)
ok = True; nconf = 0
for (p, q, r) in ((16, 1, 2), (5, 1, 1), (3, 1, 2)):
    W = Wm(p, q, r); Weq = W[0][0]; zt = 1 / Weq ** 3
    for trial in range(40):
        mode = trial % 4
        if mode == 0:
            cfg = {v: (None if random.random() < 0.5 else random.randrange(6)) for v in Vt}
        elif mode == 1:                                                     # dense aligned with defects
            cfg = {v: (None if random.random() < 0.15 else (0 if random.random() < 0.8 else random.randrange(6))) for v in Vt}
        elif mode == 2:                                                     # dilute
            cfg = {v: (random.randrange(6) if random.random() < 0.15 else None) for v in Vt}
        else:
            cfg = {v: (None if trial % 8 == 3 else 2) for v in Vt}           # the two ground states
        A = [v for v in Vt if cfg[v] is not None]
        EA = induced(Et, A)
        wt = zt ** len(A)
        for u, v in EA: wt *= W[cfg[u]][cfg[v]]
        rhs = Weq ** (-boundary(Et, A))
        for u, v in EA: rhs *= (W[cfg[u]][cfg[v]] / Weq) ** 2
        ground = (len(A) == 0) or (len(A) == len(Vt) and len({cfg[v] for v in Vt}) == 1)
        ok = ok and wt ** 2 == rhs and wt <= 1 and ((wt == 1) == ground)
        nconf += 1
want("A2 at z_t = W_eq^-3 every configuration weighs W_eq^{-|dA|/2} prod_{E(A)} (W/W_eq) (|dA| = record-vacancy bonds; 6|A| = 2|E(A)| + "
     "|dA|): a sum of non-negative bond energies, (log W_eq)/2 per record-vacancy bond and log(W_eq/W) per record-record bond, zero exactly "
     "for the empty and the fully occupied aligned configurations - checked exactly (squared) on the 3^3 torus", ok, f"{nconf} configurations")

# ------------------------------------------------------------------ A3: the l1 -> 1 limit model
ok = True; nsets = 0
for dims in ((2, 2, 2), (3, 3, 1)):
    V, E = grid(dims)
    Kinf = Kmat(1, 0, 0)                                                   # W = 6 * identity
    for k in range(len(V) + 1):
        for A in itertools.combinations(V, k):
            EA = induced(E, A)
            beta1 = len(EA) - len(A) + (ncomp(A, EA) if A else 0)
            ok = ok and phi_brute(list(A), EA, Kinf) == F(6) ** beta1
            nsets += 1
for trial in range(60):
    A = [v for v in Vt if random.random() < (0.2 + 0.6 * (trial % 3) / 2)]
    EA = induced(Et, A); dA = boundary(Et, A)
    sig = {v: (1 if v in set(A) else -1) for v in Vt}
    ok = ok and (F(1, 216) ** len(A) * F(6) ** len(EA)) ** 2 == F(6) ** (-dA) and 2 * dA == 3 * len(Vt) - sum(sig[u] * sig[v] for u, v in Et)
want("A3 as l1 -> 1 (W -> 6 I) the occupied set's law is (6z)^|A| 6^{beta1(A)} = z^|A| 6^{|E(A)| + c(A)} (beta1 the cycle rank; checked "
     "on all subsets of the 2x2x2 and 3x3x1 windows), and at z_t = 1/216 it is 6^{c(A) - |dA|/2} with |dA| = (3N - sum_bonds sigma sigma)/2: "
     "the 3D Ising lattice gas at J = (log 6)/4, h = 0, times six contents per occupied cluster (checked on the 3^3 torus)", ok, f"{nsets} window sets")

# ------------------------------------------------------------------ A4: no small parameter from l1 -> 1
p = sp.Symbol("p", positive=True)
Weq_s = 6 * p / (p + 9)                                                    # the line (p,1,2)
lims = {
    "record-vacancy bond W_eq^-1/2": (Weq_s ** sp.Rational(-1, 2), 1 / sp.sqrt(6)),
    "single record, empty phase 6 z_t": (6 / Weq_s ** 3, sp.Rational(1, 36)),
    "single vacancy, dense phase W_eq^-3": (1 / Weq_s ** 3, sp.Rational(1, 216)),
    "domino, empty phase 36 z_t^2": (36 / Weq_s ** 6, sp.Rational(1, 1296)),
    "opposite neighbour W_opp/W_eq": (1 / p, 0),
    "orthogonal neighbour W_perp/W_eq": (2 / p, 0),
}
ok = all(sp.simplify(sp.limit(e, p, sp.oo) - v) == 0 for e, v in lims.values())
Pq, Qq, Rq = sp.symbols("P Q R", positive=True)
ok = ok and sp.simplify(6 - 6 * Pq / (Pq + Qq + 4 * Rq) - 6 * (Qq + 4 * Rq) / (Pq + Qq + 4 * Rq)) == 0     # W_eq = 6 - 6(q+4r)/S < 6
Vc, Ec = grid((2, 2, 2))
cube_inf = F(1, 216) ** 8 * F(6) ** 8 * phi_brute(Vc, Ec, Kmat(1, 0, 0))
Wbig = Wm(10 ** 6, 1, 2); Weqb = Wbig[0][0]
cube_big = (1 / Weqb ** 3) ** 8 * F(6) ** 8 * phi_brute(Vc, Ec, Kmat(10 ** 6, 1, 2))
ok = ok and cube_inf == F(1, 6 ** 11) and abs(cube_big / cube_inf - 1) < F(1, 10 ** 3)
want("A4 NO SMALL PARAMETER: for every weight triple each record-vacancy bond at z_t weighs W_eq^{-1/2} > 6^{-1/2} = 0.408 (W_eq = 6 - "
     "6(q+4r)/S), and as l1 -> 1 the density excitations tend to fixed positive weights (single record 1/36, vacancy 1/216, domino "
     "1/1296, unit-cube cluster 6^-11, checked at p = 10^6 against the exact limit); only misaligned record-record bonds become costly",
     ok, "; ".join(f"{k} -> {v}" for k, (e, v) in lims.items()))

# ------------------------------------------------------------------ A5: FKG in the limit (cycle rank supermodular)
def beta1_table(V, E):
    idx = {v: i for i, v in enumerate(V)}; N = len(V); tab = {}
    for mask in range(1 << N):
        A = [V[i] for i in range(N) if mask >> i & 1]
        EA = induced(E, A)
        tab[mask] = len(EA) - len(A) + (ncomp(A, EA) if A else 0)
    return tab, N


def local_super(tab, N, logf):
    bad = 0
    for mask in range(1 << N):
        for i in range(N):
            if mask >> i & 1: continue
            for j in range(i + 1, N):
                if mask >> j & 1: continue
                if not logf(tab[mask | 1 << i | 1 << j], tab[mask], tab[mask | 1 << i], tab[mask | 1 << j]): bad += 1
    return bad


ok = True; rows = []
for dims in ((2, 2, 2), (3, 3, 1), (2, 2, 3), (4, 3, 1)):
    V, E = grid(dims); tab, N = beta1_table(V, E)
    bad = local_super(tab, N, lambda a, b, c, d: a + b >= c + d)
    ok = ok and bad == 0; rows.append(f"{dims}: {bad}")
want("A5 FKG IN THE LIMIT: beta1(A + v) - beta1(A) = (neighbours of v in A) - (components of A they lie in) never decreases as A grows, so "
     "beta1 is supermodular and the limit law (6z)^|A| 6^beta1(A) satisfies the FKG lattice condition for every z (proof in ATTEMPT.md); "
     "every mixed second difference checked on four windows", ok, "violations " + "; ".join(rows))

# ------------------------------------------------------------------ A6: FKG at finite p on windows (checked, not proved)
ok = True; rows = []
cases = [((2, 2, 2), t) for t in ((3, 1, 2), (16, 1, 2), (5, 1, 1), (7, 2, 1), (2, 1, 2))]
cases += [((3, 3, 1), t) for t in ((3, 1, 2), (16, 1, 2), (5, 1, 1))] + [((4, 3, 1), (3, 1, 2)), ((2, 2, 3), (3, 1, 2))]
for dims, trip in cases:
    V, E = grid(dims); N = len(V); K = Kmat(*trip); tab = {}
    for mask in range(1 << N):
        A = [V[i] for i in range(N) if mask >> i & 1]
        tab[mask] = phi_brute(A, induced(E, A), K)
    bad = local_super(tab, N, lambda a, b, c, d: a * b >= c * d)
    ok = ok and bad == 0; rows.append(f"{dims}{trip}: {bad}")
want("A6 CHECKED, NOT PROVED at finite p: Phi(A) = E_s[prod_{E(A)} 6K1] is log-supermodular (every mixed second difference of log Phi "
     "non-negative) on the 2x2x2, 3x3x1, 4x3x1 and 2x2x3 windows at the listed triples, (2,1,2) outside the positive semidefinite rule included",
     ok, "violations " + "; ".join(rows))

# ------------------------------------------------------------------ B0: reflection positivity at c0
def psd_by_minors(M):
    n = M.shape[0]
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            if M.extract(list(S), list(S)).det() < 0: return False
    return True


ok = True
for (pp, qq, rr) in ((3, 1, 2), (16, 1, 2), (5, 1, 1)):
    W = Wm(pp, qq, rr)
    B = sp.Matrix(7, 7, lambda i, j: 1 if (i == 0 or j == 0) else sp.Rational(W[i - 1][j - 1].numerator, W[i - 1][j - 1].denominator))
    ok = ok and psd_by_minors(B) and B.det() == 0
want("B0 at c0 the 7-state bond kernel (empty + six contents; 1 with an empty end, W between records) is positive semidefinite (all 127 "
     "principal minors >= 0) and singular, at (3,1,2), (16,1,2), (5,1,1): site-only bond-plane reflections are reflection positive "
     "(block 39 T5), so chessboard estimates hold for 2x2x2 blocks on L^3 tori with 4 | L", ok)

# ------------------------------------------------------------------ B1: the disseminated weight of a block configuration
def disseminate_weight(b, W, z, L=4):
    cfg = {}
    for x in itertools.product(range(L), repeat=3):
        src = tuple((xi % 4) if (xi % 4) < 2 else 3 - (xi % 4) for xi in x)
        cfg[x] = b[src]
    val = F(1)
    for x, s in cfg.items():
        if s is not None: val *= z
        for j in range(3):
            y = list(x); y[j] = (y[j] + 1) % L; t = cfg[tuple(y)]
            if s is not None and t is not None: val *= W[s][t]
    return val


V8, E8 = grid((2, 2, 2))
ok = True
for (pp, qq, rr), z in (((16, 1, 2), F(1, 50)), ((16, 1, 2), None), ((5, 1, 1), None)):
    W = Wm(pp, qq, rr); Weq = W[0][0]
    if z is None: z = 1 / Weq ** 3
    for trial in range(8):
        b = {v: (None if random.random() < 0.4 else random.randrange(6)) for v in V8}
        A = [v for v in V8 if b[v] is not None]; EA = induced(E8, A)
        inner = F(1)
        for u, v in EA: inner *= W[b[u]][b[v]]
        w2 = (z ** len(A) * inner) ** 2 * Weq ** (3 * len(A))                # w(b)^2
        ok = ok and disseminate_weight(b, W, z) ** 2 == w2 ** 8
        if z == 1 / Weq ** 3:
            e2 = Weq ** (-boundary(E8, A))
            for u, v in EA: e2 *= (W[b[u]][b[v]] / Weq) ** 2
            ok = ok and w2 == e2
want("B1 the site-only disseminated configuration of a 2x2x2 block b weighs w(b) per block, w(b) = prod (z W_eq^{3/2})^{n} prod_{12 internal "
     "bonds} W (each crossing bond joins a site to its own mirror copy), checked against the whole 4^3 torus; at z_t, w(b) = exp(-E_int(b)), "
     "the block's internal balance-point energy, the crossing bonds never excited", ok)

# ------------------------------------------------------------------ B2: the single-configuration chessboard sum at z_t
def zcube(p_, q_, r_):
    S = p_ + q_ + 4 * r_; Weq = F(6 * p_, S); K = Kmat(p_, q_, r_)
    even, odd = F(0), F(0)
    for k in range(9):
        for A in itertools.combinations(V8, k):
            EA = induced(E8, A)
            term = F(6) ** k * phi_brute(list(A), EA, K) / Weq ** (3 * (k // 2))
            if k % 2 == 0: even += term
            else: odd += term
    return Weq, sp.Rational(even.numerator, even.denominator) + sp.Rational(odd.numerator, odd.denominator) / sp.sqrt(sp.Rational(Weq.numerator, Weq.denominator)) ** 3


rows = []; ok = True; ZC = {}
for (pp, qq, rr) in ((3, 1, 2), (16, 1, 2), (100, 1, 2), (1000, 1, 1)):
    Weq, Zc = zcube(pp, qq, rr); ZC[(pp, qq, rr)] = (Weq, Zc)
    ok = ok and Zc - 7 > 1 and Zc - 7 >= 48 / sp.sqrt(sp.Rational(Weq.numerator, Weq.denominator)) ** 3
    rows.append(f"({pp},{qq},{rr}): bad sum {float(Zc - 7):.4f}")
lim = sp.Integer(0)
for k in range(9):
    for A in itertools.combinations(V8, k):
        EA = induced(E8, A)
        lim += sp.Integer(6) ** (len(EA) + (ncomp(A, EA) if A else 0)) * sp.sqrt(6) ** (-3 * k)
lim = sp.radsimp(sp.expand(lim))
ok = ok and sp.simplify(lim - (sp.Rational(152, 9) + 136 * sp.sqrt(6) / 27)) == 0 and 48 / sp.sqrt(6) ** 3 > 1
want("B2 at z_t the good blocks (empty; six aligned dense) have w = 1 and the bad blocks' single-configuration weights sum to Z_cube - 7 >= "
     "48 W_eq^{-3/2} > 8/sqrt6 = 3.27 for EVERY triple (the 48 single-record blocks alone), tending to 152/9 + 136 sqrt6/27 - 7 = 22.227 as "
     "l1 -> 1: the bound P(bad) <= sum_bad w(b) / Z^{1/n} is vacuous unless Z^{1/n} > 3.27, while both ground states give 1", ok,
     "; ".join(rows) + f"; limit block sum {sp.N(lim, 8)}")

# ------------------------------------------------------------------ B3: the event-form chessboard parameter stays away from 0
T4, E4 = torus(4)
even_ok = all((sum(u) + sum(v)) % 2 == 1 for u, v in E4)                    # even sites are pairwise non-adjacent
blocks_ok = all(sum(1 for d in itertools.product(range(2), repeat=3) if sum(2 * bx + dx for bx, dx in zip(bl, d)) % 2 == 0) == 4
                for bl in itertools.product(range(2), repeat=3))
rows = []; ok = even_ok and blocks_ok
for key, (Weq, Zc) in ZC.items():
    zt = 1 / sp.Rational(Weq.numerator, Weq.denominator) ** 3
    lb = ((1 + 6 * zt) ** 4 - 1) / Zc
    ok = ok and lb > 0; rows.append(f"{key}: eps >= {float(lb):.5f}")
lb_inf = ((1 + sp.Rational(6, 216)) ** 4 - 1) / lim
ok = ok and sp.N(lb_inf, 10) > sp.Rational(39, 10000)
want("B3 the event-form parameter eps = (Z(all blocks bad)/Z)^{1/n} is at least ((1 + 6 z_t)^4 - 1)/Z_cube: records only on even sites "
     "(four per block, never adjacent), at least one per block, give Z(all bad) >= ((1+6z_t)^4 - 1)^n, and the chessboard gives Z <= "
     "Z_cube^n; as l1 -> 1 the bound tends to ((37/36)^4 - 1)/(152/9 + 136 sqrt6/27) = 0.00396 > 0: the chessboard's small parameter "
     "does not vanish either", ok, "; ".join(rows) + f"; limit {sp.N(lb_inf, 6)}")

# ------------------------------------------------------------------ D: heuristics (labelled, not claimed)
J = sp.log(6) / 4
want("D1 HEURISTIC (not claimed): the limit model is the Ising lattice gas at J = (log 6)/4 = 0.448 (bond weight 6 between aligned records) "
     "plus a factor 6 per occupied cluster; block 39's calibration puts the content-less onset at bond weight e^{4K_c} = 2.427 (K_c = "
     "0.2216544, literature, cited not used), so the binding alone is deep in the condensed range and the six-fold cluster entropy is what a "
     "proof must beat; the low-temperature variable is u = e^{-4J} = 1/6",
     sp.simplify(sp.exp(-4 * J) - sp.Rational(1, 6)) == 0, f"J = {sp.N(J, 6)}")
rows = []
for rho in (sp.Rational(1, 10), sp.Rational(3, 10), sp.Rational(1, 2), sp.Rational(7, 10)):
    z = rho / (6 * (1 - rho)); Wb = z ** sp.Rational(-1, 3); pb = 9 * Wb / (6 - Wb)
    rows.append(f"density {rho}: p = {sp.N(pb, 3)}")
want("D2 HEURISTIC (not claimed) on the line (p,1,2): the balance line z W_eq^3 = 1 with the dilute density 6z/(1 + 6z) reaches densities "
     "0.1, 0.3, 0.5, 0.7 at p = 15.3, 6.0, 3.9, 2.7; the executed onsets are above 16, 8-12, 6-8, below 6. At z_t the dilute side leads by "
     "about 5 z_t per site (single records 6 z_t, vacancies z_t), which moves coexistence above the balance line, the direction of the gap; "
     "its size is not derived", True, "; ".join(rows))

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: ROUTE FAILS AT (c)'s small parameter: at the pinned scale large l1 makes no density excitation costly - at the balance "
          "point every record-vacancy bond weighs W_eq^{-1/2} > 6^{-1/2} for every weight triple (W = 6K1 caps the binding at 6) and as "
          "l1 -> 1 the law tends to one fixed model, the 3D Ising lattice gas at J = (log 6)/4, h = 0, with hard alignment and six contents "
          "per occupied cluster; that model's occupied set is FKG (cycle rank supermodular); the 2x2x2 chessboard (reflection positive at "
          "c0) has single-configuration bad sum >= 8/sqrt6 > 1 at every p and event-form parameter >= 0.00396 in the limit. An explicit "
          "region needs a contour estimate for the fixed limit model at 6^{-1/2} per plaquette, not supplied")
    print("HIT: at the pinned scale 'large l1' supplies no small parameter for dense/dilute coexistence: at z_t = W_eq^-3 every "
          "configuration weighs W_eq^{-|dA|/2} prod (W/W_eq) with W_eq = 6p/S in [6 l1, 6), so each record-vacancy bond weighs more than "
          "6^{-1/2} for every triple, and as l1 -> 1 the law tends to mu(A) ~ 6^{c(A) - |dA|/2} (Ising lattice gas at J = (log 6)/4, h = 0, "
          "six contents per cluster), whose occupied set is FKG since the cycle rank is supermodular; the 2x2x2 chessboard's parameter "
          "stays >= ((1+6z_t)^4 - 1)/Z_cube -> 0.00396")
