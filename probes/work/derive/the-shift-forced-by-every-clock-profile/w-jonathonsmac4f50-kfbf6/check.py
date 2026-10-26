#!/usr/bin/env python3
"""
check.py -- attempt J:derive:the-shift-forced-by-every-clock-profile:a1

Exact checks (Fractions / integers / sympy DomainMatrix over QQ / sympy symbolic).
Setting (block 112 as landed on main, flat strain, term linear in canonical
momentum): C[N] = sum_x N_x * (kinetic density) + K sum_x N_x R1(h)(x);
{C[N], C[M]} = G[xi(N,M)],  xi_j(x->x+e_j) = (K/(4 alpha)) (N_{x+e_j} M_x - N_x M_{x+e_j}).

Prints one line per check starting PASS/FAIL, then TOTAL, SUMMARY, and (only for new
scoped exact results) a HIT line.
"""
import itertools
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ

T0 = time.time()
RESULTS = []


def rec(ok, msg):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + msg, flush=True)


# ----------------------------------------------------------------------------
# lattice machinery (torus Z_L^3, L >= 3)
# ----------------------------------------------------------------------------
class Lat:
    def __init__(self, L):
        self.L = L
        self.ns = L ** 3
        self.pairs = [(0, 1), (0, 2), (1, 2)]

    def s(self, x):
        L = self.L
        return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)

    def xs(self):
        return itertools.product(range(self.L), repeat=3)

    def sh(self, x, d, k=1):
        y = list(x)
        y[d] += k
        return tuple(y)

    def bond(self, j, x):  # bond index (j, x -> x+e_j)
        return j * self.ns + self.s(x)

    def diag(self, j, x):
        return j * self.ns + self.s(x)

    def face(self, p, x):
        return 3 * self.ns + p * self.ns + self.s(x)

    @property
    def nvar(self):
        return 6 * self.ns

    @property
    def nbond(self):
        return 3 * self.ns


def lapse_delta(lat, N, j, x):
    """second difference Delta_j N at site x"""
    return N[lat.s(lat.sh(x, j))] - 2 * N[lat.s(x)] + N[lat.s(lat.sh(x, j, -1))]


def dface(lat, N, p, x):
    i, j = lat.pairs[p]
    xi = lat.sh(x, i)
    xj = lat.sh(x, j)
    xij = lat.sh(xi, j)
    return N[lat.s(x)] - N[lat.s(xi)] - N[lat.s(xj)] + N[lat.s(xij)]


def fmean(lat, N, p, x):
    i, j = lat.pairs[p]
    xi = lat.sh(x, i)
    xj = lat.sh(x, j)
    xij = lat.sh(xi, j)
    return (N[lat.s(x)] + N[lat.s(xi)] + N[lat.s(xj)] + N[lat.s(xij)]) / 4


def bracket_coeffs(lat, N, M, K, alpha, c):
    """P-coefficient vector of {C[N], C[M]} (linear in P), face timing = 4-corner mean.
    {A,B} = sum dA/dh dB/dP - dA/dP dB/dh.
    dC[N]/dh_jj(x) = K (Delta_j N - sum_i Delta_i N)(x); dC[N]/dh_f = 2K dN_f;
    dC[M]/dP_jj = M_x (P_jj - c sum P)/(2 alpha); dC[M]/dP_f = Mbar_f P_f/(4 alpha)."""
    n = lat.nvar
    out = [Fr(0)] * n
    for x in lat.xs():
        # diagonal
        SN = sum(lapse_delta(lat, N, i, x) for i in range(3))
        SM = sum(lapse_delta(lat, M, i, x) for i in range(3))
        a = []
        for j in range(3):
            aj = (K / (2 * alpha)) * ((lapse_delta(lat, N, j, x) - SN) * M[lat.s(x)]
                                      - (lapse_delta(lat, M, j, x) - SM) * N[lat.s(x)])
            a.append(aj)
        sa = sum(a)
        for k in range(3):
            out[lat.diag(k, x)] += a[k] - c * sa
        for p in range(3):
            out[lat.face(p, x)] += (K / (2 * alpha)) * (dface(lat, N, p, x) * fmean(lat, M, p, x)
                                                        - dface(lat, M, p, x) * fmean(lat, N, p, x))
    return out


def xi_field(lat, N, M, K, alpha):
    xi = [Fr(0)] * lat.nbond
    for x in lat.xs():
        for j in range(3):
            xi[lat.bond(j, x)] = (K / (4 * alpha)) * (N[lat.s(lat.sh(x, j))] * M[lat.s(x)]
                                                      - N[lat.s(x)] * M[lat.s(lat.sh(x, j))])
    return xi


def build_D(lat):
    """integer matrix D (nvar x nbond):  (D xi) = delta_xi h  (block 112 definition)."""
    D = [[0] * lat.nbond for _ in range(lat.nvar)]
    for x in lat.xs():
        for j in range(3):
            D[lat.diag(j, x)][lat.bond(j, x)] += 2
            D[lat.diag(j, x)][lat.bond(j, lat.sh(x, j, -1))] -= 2
        for p, (i, j) in enumerate(lat.pairs):
            f = lat.face(p, x)
            # nabla_i xi_j + nabla_j xi_i with forward differences at the face base x
            D[f][lat.bond(j, lat.sh(x, i))] += 1
            D[f][lat.bond(j, x)] -= 1
            D[f][lat.bond(i, lat.sh(x, j))] += 1
            D[f][lat.bond(i, x)] -= 1
    return D


def matvec(Mx, v):
    return [sum(Fr(a) * b for a, b in zip(row, v) if a != 0) for row in Mx]


def matTvec(Mx, v):
    ncol = len(Mx[0])
    out = [Fr(0)] * ncol
    for r, row in enumerate(Mx):
        vr = v[r]
        if vr == 0:
            continue
        for cidx, a in enumerate(row):
            if a != 0:
                out[cidx] += a * vr
    return out


def Amatrix(lat, G):
    """antisymmetric site matrix:  M^T A N = sum_{j,x} G_j(x) (N_{x+e_j} M_x - N_x M_{x+e_j})."""
    ns = lat.ns
    A = [[Fr(0)] * ns for _ in range(ns)]
    for x in lat.xs():
        for j in range(3):
            g = G[lat.bond(j, x)]
            y = lat.sh(x, j)
            A[lat.s(x)][lat.s(y)] += g
            A[lat.s(y)][lat.s(x)] -= g
    return A


def dm(rows):
    return DomainMatrix([[QQ(r.numerator, r.denominator) if isinstance(r, Fr) else QQ(r) for r in row]
                         for row in rows], (len(rows), len(rows[0])), QQ)


def rank(rows):
    return dm(rows).rank()


def nullspace(rows):
    ns = dm(rows).nullspace()
    return ns


def legendre_c_half(lat, hdot, alpha):
    """P = dL/dhdot at c = 1/2 (beta=-alpha): P_jj = 2 alpha (hd_jj - tr hd), P_f = 4 alpha hd_f."""
    P = [Fr(0)] * lat.nvar
    for x in lat.xs():
        t = sum(hdot[lat.diag(k, x)] for k in range(3))
        for j in range(3):
            P[lat.diag(j, x)] = 2 * alpha * (hdot[lat.diag(j, x)] - t)
        for p in range(3):
            P[lat.face(p, x)] = 4 * alpha * hdot[lat.face(p, x)]
    return P


def divergence(lat, G):
    """backward divergence  sum_j (G_j(y) - G_j(y - e_j))"""
    out = []
    for y in lat.xs():
        out.append(sum(G[lat.bond(j, y)] - G[lat.bond(j, lat.sh(y, j, -1))] for j in range(3)))
    return out


def rnd_vec(rng, n, lo=-3, hi=3):
    return [Fr(rng.randint(lo, hi)) for _ in range(n)]


K = Fr(2, 5)
ALPHA = Fr(1, 3)
rng = random.Random(20261025)

# ----------------------------------------------------------------------------
# A. retrieval: block 112 T1 bracket recomputed on the torus
# ----------------------------------------------------------------------------
print("# A. block 112 T1 recomputed (retrieval, not new)")
for L in (3, 4):
    lat = Lat(L)
    D = build_D(lat)
    ok = True
    for trial in range(3):
        N = rnd_vec(rng, lat.ns)
        M = rnd_vec(rng, lat.ns)
        b = bracket_coeffs(lat, N, M, K, ALPHA, Fr(1, 2))
        g = matvec(D, xi_field(lat, N, M, K, ALPHA))
        ok = ok and (b == g)
    rec(ok, f"A1 L={L}: {{C[N],C[M]}} P-coefficients == G[xi(N,M)] exactly at c=1/2 (3 random integer lapse pairs)")
    N = rnd_vec(rng, lat.ns)
    M = rnd_vec(rng, lat.ns)
    b = bracket_coeffs(lat, N, M, K, ALPHA, Fr(1, 3))
    g = matvec(D, xi_field(lat, N, M, K, ALPHA))
    rec(b != g, f"A2 L={L}: at c=1/3 the bracket differs from G[xi(N,M)] (the landed 'iff c=1/2' direction)")

# ----------------------------------------------------------------------------
# B. span of xi(N,M): every clock profile vs the uniform profile (retrieval of T1(a),(b))
# ----------------------------------------------------------------------------
print("# B. span of the relabellings xi(N,M)  (T1(a),(b) recomputed, plus the new minimal-profile table)")


def span_rank(lat, Nlist):
    rows = []
    for Nv in Nlist:
        for z in lat.xs():
            M = [Fr(0)] * lat.ns
            M[lat.s(z)] = Fr(1)
            rows.append(xi_field(lat, Nv, M, Fr(1), Fr(1)))
    return rank(rows)


for L in (3, 4):
    lat = Lat(L)
    ones = [Fr(1)] * lat.ns
    deltas = []
    for z in lat.xs():
        d = [Fr(0)] * lat.ns
        d[lat.s(z)] = Fr(1)
        deltas.append(d)
    rk_all = span_rank(lat, deltas)
    rk_one = span_rank(lat, [ones])
    rec(rk_all == lat.nbond, f"B1 L={L}: span of xi(N,M) over ALL lapses has rank {rk_all} == #bonds {lat.nbond}")
    rec(rk_one == lat.ns - 1, f"B2 L={L}: span of xi(M,1) (uniform evolution lapse) has rank {rk_one} == #sites-1 = {lat.ns-1} (gradients only)")

print("# B3. NEW (finite check): torus rank when the evolution-lapse family is {1} plus sawtooth lapses f(x_a)=x_a (one site defect at the wrap)")
for L in (3, 4, 5):
    lat = Lat(L)
    ones = [Fr(1)] * lat.ns
    saw = []
    for a in range(3):
        saw.append([Fr(x[a]) for x in lat.xs()])
    ranks = []
    for r in range(4):
        fam = [ones] + saw[:r]
        ranks.append(span_rank(lat, fam))
    print(f"   L={L}: bond dof={lat.nbond}; rank of span for families {{1}}, +1 axis lapse, +2, +3: {ranks}")
    rec(ranks[0] == lat.ns - 1 and ranks == sorted(ranks), f"B3 L={L}: ranks nondecreasing, start at #sites-1 (data above)")
    # record the full-rank statement as data
    if L in (3, 4, 5):
        FULL_TABLE = globals().setdefault("FULL_TABLE", {})
        FULL_TABLE[L] = (ranks, lat.nbond)

# ----------------------------------------------------------------------------
# C. the consistency operator A_G is antisymmetric and carries the bracket
# ----------------------------------------------------------------------------
print("# C. NEW: the preservation condition as an antisymmetric operator A_G on lapses")
for L in (3, 4):
    lat = Lat(L)
    D = build_D(lat)
    P = rnd_vec(rng, lat.nvar)
    G = matTvec(D, P)  # momentum-constraint density, one value per bond
    A = Amatrix(lat, G)
    antisym = all(A[i][j] == -A[j][i] for i in range(lat.ns) for j in range(lat.ns))
    rec(antisym, f"C1 L={L}: A_G is antisymmetric (G = D^T P for a random integer P)")
    N = rnd_vec(rng, lat.ns)
    M = rnd_vec(rng, lat.ns)
    lhs = sum(p * b for p, b in zip(P, bracket_coeffs(lat, N, M, K, ALPHA, Fr(1, 2))))
    AN = [sum(A[i][j] * N[j] for j in range(lat.ns)) for i in range(lat.ns)]
    rhs = (K / (4 * ALPHA)) * sum(M[i] * AN[i] for i in range(lat.ns))
    rec(lhs == rhs, f"C2 L={L}: P . {{C[N],C[M]}} == (K/4alpha) M^T A_G N exactly (random P, N, M)")

# ----------------------------------------------------------------------------
# D. kernel structure of A_G on states with G != 0
# ----------------------------------------------------------------------------
print("# D. NEW: which evolution lapses are consistent at a state with nonzero momentum constraint")
for L in (3, 4):
    lat = Lat(L)
    D = build_D(lat)
    ranks = []
    for trial in range(3):
        P = rnd_vec(rng, lat.nvar)
        G = matTvec(D, P)
        ranks.append(rank(Amatrix(lat, G)))
    exp = lat.ns - (lat.ns % 2)
    rec(all(r == exp for r in ranks), f"D1 L={L}: rank A_G = {ranks} for 3 random states (full antisymmetric rank {exp} of {lat.ns} sites => kernel dim {lat.ns-exp})")
    ones = [Fr(1)] * lat.ns
    P = rnd_vec(rng, lat.nvar)
    G = matTvec(D, P)
    A = Amatrix(lat, G)
    A1 = [sum(row) for row in A]
    div = divergence(lat, G)
    # (A 1)_y = sum_j (G_j(y) - G_j(y-e_j)) ... relation to divergence
    rec(A1 == div, f"D2 L={L}: A_G applied to the uniform lapse equals the backward divergence of G (so uniform lapse consistent iff div G = 0)")
    rec(any(v != 0 for v in A1), f"D3 L={L}: a random state has div G != 0, so the uniform clock is NOT a consistent profile there")

# odd torus always has a kernel: exact determinant of A_G is 0 for a random state on 3^3 (parity argument in ATTEMPT.md)
lat3 = Lat(3)
D3 = build_D(lat3)
G3 = matTvec(D3, rnd_vec(rng, lat3.nvar))
det3 = dm(Amatrix(lat3, G3)).det()
rec(det3 == 0 and lat3.ns % 2 == 1, "D4 L=3: det A_G = 0 exactly (27 sites, odd antisymmetric matrix), so EVERY state on the 3^3 torus has a nonzero consistent lapse; on 4^3 (64 sites) D1 shows a trivial kernel for the sampled states")

# G = 0 iff A_G = 0 (side >= 3): entries A[x, x+e_j] = G_j(x) are distinct for L>=3
lat = Lat(3)
G = [Fr(0)] * lat.nbond
b0 = lat.bond(1, (1, 2, 0))
G[b0] = Fr(7)
A = Amatrix(lat, G)
nz = [(i, j) for i in range(lat.ns) for j in range(lat.ns) if A[i][j] != 0]
rec(len(nz) == 2, "D5 L=3: a single nonzero bond value of G puts exactly one antisymmetric pair of entries in A_G, so A_G = 0 iff G = 0 (side>=3)")

# ----------------------------------------------------------------------------
# E. the lattice drifting twist: G != 0, div G = 0
# ----------------------------------------------------------------------------
print("# E. NEW: lattice version of the drifting transverse relabelling")
for L in (3, 4):
    lat = Lat(L)
    D = build_D(lat)
    ok0 = True
    for trial in range(3):
        Nv = rnd_vec(rng, lat.ns)
        xi = rnd_vec(rng, lat.nbond)
        dCdh = [Fr(0)] * lat.nvar  # dC[N]/dh : K (Delta_j N - sum_i Delta_i N) on sites, 2K dN on faces
        for x in lat.xs():
            SN = sum(lapse_delta(lat, Nv, i, x) for i in range(3))
            for j in range(3):
                dCdh[lat.diag(j, x)] = K * (lapse_delta(lat, Nv, j, x) - SN)
            for p in range(3):
                dCdh[lat.face(p, x)] = 2 * K * dface(lat, Nv, p, x)
        Dxi = matvec(D, xi)
        if sum(a * b for a, b in zip(dCdh, Dxi)) != 0:
            ok0 = False
    rec(ok0, f"E0 L={L}: the linear curvature term K sum_x N_x R1(h) is invariant under h -> h + D xi for every lapse N and bond field xi (so h = t D xi, u = 0 stays on the energy-constraint surface at this order)")
for L in (3, 4):
    lat = Lat(L)
    D = build_D(lat)
    okb = True
    for trial in range(3):
        Mv = rnd_vec(rng, lat.ns)
        gradM = [Fr(0)] * lat.nbond
        for x in lat.xs():
            for j in range(3):
                gradM[lat.bond(j, x)] = Mv[lat.s(lat.sh(x, j))] - Mv[lat.s(x)]
        Pg = legendre_c_half(lat, matvec(D, gradM), ALPHA)
        dCdh = [Fr(0)] * lat.nvar
        for x in lat.xs():
            SM = sum(lapse_delta(lat, Mv, i, x) for i in range(3))
            for j in range(3):
                dCdh[lat.diag(j, x)] = K * (lapse_delta(lat, Mv, j, x) - SM)
            for p in range(3):
                dCdh[lat.face(p, x)] = 2 * K * dface(lat, Mv, p, x)
        if Pg != [(4 * ALPHA / K) * v for v in dCdh]:
            okb = False
    rec(okb, f"E0b L={L}: Lambda D(grad M) == (4 alpha/K) dC[M]/dh exactly (the DeWitt momentum of a pure-gradient relabelling is the curvature-constraint gradient); with E0 and symmetry of Lambda these together imply div G = 0 for every drifting relabelling (ATTEMPT.md step 6)")
for L in (3, 4):
    lat = Lat(L)
    D = build_D(lat)
    ok_div = True
    ok_nonzero = False
    for trial in range(3):
        xi = rnd_vec(rng, lat.nbond)
        hdot = matvec(D, xi)
        P = legendre_c_half(lat, hdot, ALPHA)
        G = matTvec(D, P)
        if any(v != 0 for v in divergence(lat, G)):
            ok_div = False
        if any(v != 0 for v in G):
            ok_nonzero = True
    rec(ok_div, f"E1 L={L}: for random relabelling velocities hdot = D xi at c=1/2, the lattice momentum constraint G = D^T P has div G = 0 EXACTLY (so the uniform clock is consistent on drifting relabellings)")
    rec(ok_nonzero, f"E2 L={L}: and G is nonzero for them (so a uniform clock does not force G = 0)")

# ----------------------------------------------------------------------------
# F. infinite-lattice (padded box) forcing by polynomial lapses
# ----------------------------------------------------------------------------
print("# F. NEW: minimal evolution-lapse families on a padded box (finite support G, the Z^3 statement)")
BOX = 6  # sites 0..5 ; G supported on bonds starting in 1..4 (so both ends are in the box)
sup = [x for x in itertools.product(range(1, BOX - 1), repeat=3)]
var_index = {}
for x in sup:
    for j in range(3):
        var_index[(j, x)] = len(var_index)
nvars = len(var_index)


def eq_rows_for_lapse(Nfun):
    """equations (A_G N)_y = 0 for all y in the box, linear in the unknown bond values G."""
    rows = []
    for y in itertools.product(range(BOX), repeat=3):
        row = [0] * nvars
        for j in range(3):
            # + G_j(y) N_{y+e_j}
            yj = (y[0] + (j == 0), y[1] + (j == 1), y[2] + (j == 2))
            if (j, y) in var_index:
                row[var_index[(j, y)]] += Nfun(yj)
            # - G_j(y-e_j) N_{y-e_j}
            ym = (y[0] - (j == 0), y[1] - (j == 1), y[2] - (j == 2))
            if (j, ym) in var_index:
                row[var_index[(j, ym)]] -= Nfun(ym)
        if any(row):
            rows.append(row)
    return rows


fam = {
    "{1}": [lambda y: 1],
    "{1,x1}": [lambda y: 1, lambda y: y[0]],
    "{1,x1,x2}": [lambda y: 1, lambda y: y[0], lambda y: y[1]],
    "{1,x1,x2,x3}": [lambda y: 1, lambda y: y[0], lambda y: y[1], lambda y: y[2]],
    "{x1,x2,x3} (no uniform)": [lambda y: y[0], lambda y: y[1], lambda y: y[2]],
}
nullity = {}
for name, funs in fam.items():
    rows = []
    for f in funs:
        rows += eq_rows_for_lapse(f)
    rk = rank(rows)
    nullity[name] = nvars - rk
    print(f"   family {name}: unknown finite-support bond fields G: {nvars}; rank {rk}; surviving dimension {nvars - rk}")
rec(nullity["{1}"] > nullity["{1,x1}"] > nullity["{1,x1,x2}"] == 0 and nullity["{1,x1,x2,x3}"] == 0,
    f"F1 finite-support G on Z^3 (padded 6^3 box, support in the interior): surviving dims {nullity['{1}']} > {nullity['{1,x1}']} > 0 = {nullity['{1,x1,x2}']} for {{1}},{{1,x1}},{{1,x1,x2}}: the uniform lapse plus linear lapses in two independent directions force G = 0")
# the analytic equations used in the proof: with N=1 and N=x_a  -> div G=0 and G_a(y)+G_a(y-e_a)=0
rows = eq_rows_for_lapse(lambda y: 1)
G_try = {}
# independent verification of the analytic reduction: (A x_a)_y = y_a (div G)(y) + G_a(y) + G_a(y-e_a)
ok = True
rng2 = random.Random(5)
Gv = {k: rng2.randint(-3, 3) for k in var_index}
for a in range(3):
    for y in itertools.product(range(BOX), repeat=3):
        lhs = 0
        for j in range(3):
            yj = tuple(y[i] + (i == j) for i in range(3))
            ym = tuple(y[i] - (i == j) for i in range(3))
            lhs += Gv.get((j, y), 0) * yj[a] - Gv.get((j, ym), 0) * ym[a]
        div = sum(Gv.get((j, y), 0) - Gv.get((j, tuple(y[i] - (i == j) for i in range(3))), 0) for j in range(3))
        ya = y[a]
        ea = tuple(y[i] - (i == a) for i in range(3))
        rhs = ya * div + Gv.get((a, y), 0) + Gv.get((a, ea), 0)
        ok = ok and (lhs == rhs)
rec(ok, "F2 identity used in the proof: (A_G x_a)(y) = y_a (div G)(y) + G_a(y) + G_a(y-e_a), checked at every site of the box for random integer G")
# {1, x1}: surviving G has G_1 = 0  (all x1-bond values vanish)
rows = eq_rows_for_lapse(lambda y: 1) + eq_rows_for_lapse(lambda y: y[0])
for (j, x), idx in list(var_index.items()):
    pass
ker = nullspace(rows)  # rows of DomainMatrix nullspace: each row a basis vector
kerl = ker.to_Matrix()
g1_idx = [idx for (j, x), idx in var_index.items() if j == 0]
g1_zero = all(kerl[r, i] == 0 for r in range(kerl.rows) for i in g1_idx)
rec(g1_zero, "F3 with {1, x1}: every surviving finite-support G has G_1 = 0 (the lapse gradient along axis a forces the a-component)")

# ----------------------------------------------------------------------------
# G. the plane-wave drifting twist: which lapses stay consistent
# ----------------------------------------------------------------------------
print("# G. NEW: lapses consistent with a plane-wave drifting twist on the 4^3 torus")
lat = Lat(4)
D = build_D(lat)
xi = [Fr(0)] * lat.nbond
pat = {0: 1, 1: 0, 2: -1, 3: 0}  # cos(pi x/2), period 4
for x in lat.xs():
    xi[lat.bond(1, x)] = Fr(pat[x[0]])  # transverse: xi along e_2, varying in x_1
hdot = matvec(D, xi)
P = legendre_c_half(lat, hdot, ALPHA)
G = matTvec(D, P)
support = sorted({j for j in range(3) for x in lat.xs() if G[lat.bond(j, x)] != 0})
rec(support == [1] and all(v == 0 for v in divergence(lat, G)),
    "G1 4^3: the twist xi = e_2 cos(pi x_1/2) has G supported on the e_2 component only, and div G = 0")
A = Amatrix(lat, G)
ker = nullspace(A)
kdim = ker.shape[0]
g_vals = {x[0]: G[lat.bond(1, x)] for x in lat.xs()}
nonzero_x1 = sorted({x[0] for x in lat.xs() if G[lat.bond(1, x)] != 0})
# lapses independent of x_2 (arbitrary in x_1, x_3) are consistent
ok_free = True
rng3 = random.Random(11)
for trial in range(3):
    prof = {(a, b): Fr(rng3.randint(-4, 4)) for a in range(4) for b in range(4)}
    Nv = [prof[(x[0], x[2])] for x in lat.xs()]
    ok_free = ok_free and all(sum(A[i][j] * Nv[j] for j in range(lat.ns)) == 0 for i in range(lat.ns))
rec(ok_free, "G2 any lapse N(x_1, x_3) independent of the twist direction x_2 is consistent with the twist state (3 random profiles)")
# a lapse varying along x_2 is not
Nv = [Fr(1) if x == (0, 0, 0) else Fr(0) for x in lat.xs()]
AN = [sum(A[i][j] * Nv[j] for j in range(lat.ns)) for i in range(lat.ns)]
rec(any(v != 0 for v in AN), "G3 a lapse localized on one site is NOT consistent with the twist state")
Nv = [Fr(x[1]) for x in lat.xs()]  # sawtooth along x_2
AN = [sum(A[i][j] * Nv[j] for j in range(lat.ns)) for i in range(lat.ns)]
rec(any(v != 0 for v in AN), "G4 a lapse with a gradient along the twist direction (sawtooth in x_2) is NOT consistent with the twist state")
print(f"   kernel dimension of A_G for this twist on 4^3: {kdim}; G_2 nonzero on x_1 in {nonzero_x1}")
# kernel count: slices x1 where G!=0 : N_{y+e2}=N_{y-e2} -> 2 free values per (x1,x3) line of length 4 ; else 4 free
expected = sum((2 if x1 in nonzero_x1 else 4) * 4 for x1 in range(4))
rec(kdim == expected, f"G5 kernel dimension {kdim} == {expected} = sum over x_1-slices of (2 if G!=0 else 4) free values per x_3 line (lapse must be 2-site periodic along the twist direction where the twist is present)")

# ----------------------------------------------------------------------------
# H. sign of the consistent lapse
# ----------------------------------------------------------------------------
print("# H. NEW (data): on the 3^3 torus the unique consistent lapse of a random state is not sign-definite")
lat = Lat(3)
D = build_D(lat)
mixed = 0
trials = 12
rngH = random.Random(77)
for t in range(trials):
    P = rnd_vec(rngH, lat.nvar)
    G = matTvec(D, P)
    A = Amatrix(lat, G)
    ker = nullspace(A)
    assert ker.shape[0] == 1
    v = [ker.to_Matrix()[0, i] for i in range(lat.ns)]
    if min(v) < 0 < max(v):
        mixed += 1
rec(mixed >= trials // 2, f"H1 {mixed} of {trials} random states have a consistent lapse with entries of both signs (positivity of the clock is not automatic); this is data, not a theorem")

# ----------------------------------------------------------------------------
# I. finite-lapse Lagrangian: kinetic + K N R1 sector of block 112's T2, symbolic
# ----------------------------------------------------------------------------
print("# I. NEW (symbolic, continuum comparator form): block 112 T2 at finite, space-and-time-dependent lapse N")
t, x1, x2, x3 = sp.symbols("t x1 x2 x3")
X = (x1, x2, x3)
al, Ksym = sp.symbols("alpha K", positive=True)
Nf = sp.Function("N")(t, *X)
zeta = sp.Function("zeta")(t, *X)
hf = {}
for i in range(3):
    for j in range(i, 3):
        hf[(i, j)] = sp.Function(f"h{i}{j}")(t, *X)
        hf[(j, i)] = hf[(i, j)]
Hd = lambda f: sp.diff(f, t)
tr = lambda dct: sum(dct[(k, k)] for k in range(3))


def R1(hh):
    """R1^L = -(d_i d_j h_ij - lap tr h)  (landed symbol sign p^2 tr h - p h p)"""
    return -(sum(sp.diff(hh[(i, j)], X[i], X[j]) for i in range(3) for j in range(3))
             - sum(sp.diff(tr(hh), X[k], 2) for k in range(3)))


def Lag(hh, Nn):
    kin = (al / Nn) * (sum(sp.diff(hh[(i, j)], t) ** 2 for i in range(3) for j in range(3))
                       - sp.diff(tr(hh), t) ** 2)  # beta = -alpha
    return kin + Ksym * Nn * R1(hh)


eps, lam = sp.symbols("epsilon lambda", positive=True)
# gradient relabelling h_ij -> lam*h_ij + eps d_i d_j zeta ; lapse N -> N + eps dN.
# lam counts the order in the strain field h: T2 is the QUADRATIC action, so only the part of the first
# variation linear in h is kept (the dN * kinetic term is quadratic in h and belongs to the cubic order).
dN = -(2 * al / Ksym) * sp.diff(sp.diff(zeta, t) / Nf, t)
zz = {(i, j): sp.diff(zeta, X[i], X[j]) for i in range(3) for j in range(3)}
rec(sp.simplify(R1(zz)) == 0, "I1 R1(d_i d_j zeta) == 0 identically (gradient relabellings do not change the linear curvature, any zeta(t,x))")
hh2 = {(i, j): lam * hf[(i, j)] + eps * zz[(i, j)] for i in range(3) for j in range(3)}
L2 = Lag(hh2, Nf + eps * dN)
dL = sp.expand(sp.diff(L2, eps).subs(eps, 0)).coeff(lam, 1)
Pi = {(i, j): sp.diff(hf[(i, j)], t) - (sp.diff(tr(hf), t) if i == j else 0) for i in range(3) for j in range(3)}
Gc = [sum(sp.diff(Pi[(i, j)], X[j]) for j in range(3)) for i in range(3)]  # momentum-constraint density d_j Pi_ij
# REM = 2 alpha zeta_t [ 2 d_i(1/N) d_j Pi_ij + Pi_ij d_i d_j (1/N) ]
REM = 2 * al * sp.diff(zeta, t) * (2 * sum(sp.diff(1 / Nf, X[i]) * Gc[i] for i in range(3))
                                   + sum(Pi[(i, j)] * sp.diff(1 / Nf, X[i], X[j]) for i in range(3) for j in range(3)))
diff_expr = sp.expand(dL - REM)


def euler_all(expr, fields):
    """Euler-Lagrange operator of expr wrt each field; expression is a total divergence iff all vanish"""
    from sympy.calculus.euler import euler_equations
    eqs = euler_equations(expr, fields, [t, *X])
    return [sp.simplify(e.lhs - e.rhs) for e in eqs]


fields = [zeta, Nf] + [hf[(i, j)] for i in range(3) for j in range(i, 3)]
ee = euler_all(diff_expr, fields)
rec(all(e == 0 for e in ee), "I2 first variation (linear in h) of kinetic + K N R1 under h -> h + d d zeta, N -> N - (2 alpha/K) d_t(zeta_t/N) equals REM up to a TOTAL DIVERGENCE (all 8 Euler operators vanish); REM = 2 alpha zeta_t [2 d_i(1/N) d_j Pi_ij + Pi_ij d_i d_j (1/N)]")
# the wrong sign of the compensator does not work (control)
dN_bad = +(2 * al / Ksym) * sp.diff(sp.diff(zeta, t) / Nf, t)
L2b = Lag(hh2, Nf + eps * dN_bad)
dLb = sp.expand(sp.diff(L2b, eps).subs(eps, 0)).coeff(lam, 1)
eeb = euler_all(sp.expand(dLb - REM), fields)
rec(any(e != 0 for e in eeb), "I2c control: with the opposite sign of the compensator the same statement FAILS (the check is sensitive)")
nt = sp.Function("n")(t)
REMu = REM.subs(Nf, nt).doit()
rec(sp.simplify(REMu) == 0, "I3 for a lapse depending on t only (any finite N(t)), REM == 0: T2 extends exactly to a finite uniform-in-space, time-dependent lapse in this sector")
a1 = sp.symbols("a1")
Nlin = 1 + a1 * x1
REM_lin = REM.subs(Nf, Nlin).doit()
expected_lin = 2 * al * sp.diff(zeta, t) * (-2 * a1 / Nlin ** 2 * Gc[0] + 2 * a1 ** 2 / Nlin ** 3 * Pi[(0, 0)])
rec(sp.simplify(REM_lin - expected_lin) == 0, "I4 for N = 1 + a x_1: REM = 2 alpha zeta_t [ -2a/N^2 (d_j Pi_1j) + 2a^2/N^3 Pi_11 ]: first order in the lapse gradient it is the lapse gradient times the momentum constraint, second order in a Pi_11 term appears")
rec(sp.simplify(REM_lin) != 0, "I5 REM is not identically zero for a lapse with a gradient: this completion of T2 does not extend to spatially varying lapse")

# ----------------------------------------------------------------------------
elapsed = time.time() - T0
npass = sum(RESULTS)
nfail = len(RESULTS) - npass
if nfail == 0:
    print("HIT: at flat strain and linear order in the momenta (block 112 stencil), (i) preservation of the clock constraints under lapse N at a state with momentum constraint G is M^T A_G N = 0 for all M with A_G antisymmetric, so the consistent evolution lapses are exactly ker A_G (all lapses iff G = 0; the uniform lapse iff div G = 0, which holds exactly for lattice drifting relabellings; nonzero kernel on odd tori, trivial for sampled states on 4^3); (ii) for finitely supported G on Z^3 the evolution lapses {1, x_1, x_2} force G = 0 and {1, x_a} force G_a = 0 given div G = 0 (exact padded-box rank check), while {1} leaves only div G = 0; (iii) in the continuum-comparator kinetic + K N R1 sector, block 112's T2 compensator extends exactly to finite N(t), and for spatially varying N leaves REM = 2 alpha zeta_t [2 d_i(1/N) d_j Pi_ij + Pi_ij d_i d_j (1/N)] at linear order in h")
print(f"# runtime {elapsed:.1f} s")
print(f"TOTAL: PASS={npass} FAIL={nfail}")
print("SUMMARY: PARTIAL The landed T1 reading is re-confirmed on 3^3/4^3 tori; new exact results: the lapse-preservation condition is M^T A_G N with A_G antisymmetric, so at a state with G != 0 the consistent clocks are ker A_G (the algebra restricts the lapse, and forces G = 0 only if every profile must stay allowed); on Z^3 the lapses {1, x_1, x_2} already force G = 0 for finite-support G, while {1} leaves the divergence-free sector that the lattice drifting relabellings occupy exactly; T2's compensator extends exactly to finite N(t) and leaves, for spatially varying N, a remainder first order in grad N times the momentum constraint.")

sys.exit(0 if nfail == 0 else 1)
