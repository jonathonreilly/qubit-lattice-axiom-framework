#!/usr/bin/env python3
"""Finite-cluster occupation distributions for two ladder constructions.

This runner checks a declared hopping-plus-density matrix subfamily on four
finite open graphs.  Its probability object is the occupation-basis diagonal
of a normalized ground-space projector.  A physical record reading additionally
requires state-selection/Born and occupation-to-record bridges outside this
mathematical runner's input set.

Declared objects:

  * clusters with open boundaries and nearest-neighbour bonds -- chain6 (6 sites
    on a line, 5 bonds), grid2x3 (2 rows by 3 columns, 7 bonds), cube (2x2x2,
    12 bonds), grid3x3 (9 sites, 12 bonds);
  * site operators: ungraded ladders b_i = a at site i and the identity
    elsewhere; graded ladders c_i = Jordan-Wigner, the s3 string on the sites
    before i; n_i = b_i^dag b_i = c_i^dag c_i is the same operator;
  * one declared homogeneous hopping-plus-density expression on both
    constructions,
        H(t, V) = -t sum_bonds (x_i^dag x_j + x_j^dag x_i) + V sum_bonds n_i n_j,
    with x = b (ungraded) or x = c (graded); nonzero hopping is normalized to
    t = 1 and g = V/abs(t), while t = 0 is outside this slice;
  * occupation distribution P(g): the occupation-basis diagonal of the matrix's
    lowest-energy state in a fixed occupation-number sector, the normalized
    ground-space projector diagonal if degenerate.

Check families:

  * local operator span, global boundary-degree term, zero-hopping boundary,
    and the nonzero-hopping sign gauge;
  * exact one-dimensional matrix identity and a numerical control;
  * exact ungraded sign/connectivity hypotheses and numerical positivity sample;
  * exact graded free-point spectra, probabilities, and comparator support;
  * bounded finite-window distance scans;
  * exact symmetry representations and free-point forced-zero sets, plus a
    numerical nine-coupling persistence sample.

Exact checks use sympy only (Rational, sqrt(2), integer matrices, Sturm root
counts). Numerical witnesses use numpy and scipy and are labelled as such.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

import itertools
import sys

import numpy as np
import sympy as sp
from scipy.linalg import eigh
from scipy.optimize import minimize_scalar
from sympy import I, Matrix, Rational, eye, sqrt, symbols, zeros

AUDIT_TIMEOUT_SEC = 300

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ---------------------------------------------------------------- clusters

def grid_cluster(nr, nc):
    """Open nr x nc grid: site (r, c) has index nc*r + c."""
    idx = {(r, c): nc * r + c for r in range(nr) for c in range(nc)}
    bonds = []
    for r in range(nr):
        for c in range(nc):
            if c + 1 < nc:
                bonds.append((idx[(r, c)], idx[(r, c + 1)]))
            if r + 1 < nr:
                bonds.append((idx[(r, c)], idx[(r + 1, c)]))
    return nr * nc, sorted((min(u, v), max(u, v)) for u, v in bonds)


def chain_cluster(n):
    return n, [(i, i + 1) for i in range(n - 1)]


def cube_cluster():
    """2x2x2 cube: site (x, y, z) has index 4x + 2y + z."""
    bonds = [(s, s ^ bit) for s in range(8) for bit in (4, 2, 1) if s ^ bit > s]
    return 8, sorted(bonds)


CHAIN6 = chain_cluster(6)
GRID23 = grid_cluster(2, 3)
CUBE = cube_cluster()
GRID33 = grid_cluster(3, 3)
CASES = [("grid2x3", GRID23, 2), ("grid2x3", GRID23, 3),
         ("cube", CUBE, 4), ("grid3x3", GRID33, 3)]


def adjacency(L, B):
    A = zeros(L, L)
    for (u, v) in B:
        A[u, v] = 1
        A[v, u] = 1
    return A


def configs_of(L, N):
    return [frozenset(s) for s in itertools.combinations(range(L), N)]


def jw_sign(S, src, dst):
    """Jordan-Wigner sign of the hop src -> dst in the occupation pattern S."""
    lo, hi = min(src, dst), max(src, dst)
    return (-1) ** sum(1 for k in range(lo + 1, hi) if k in S)


def sector(L, B, N, graded, t, V):
    """Exact sector matrix of H(t, V) in the occupation basis."""
    cfg = configs_of(L, N)
    idx = {c: i for i, c in enumerate(cfg)}
    M = zeros(len(cfg), len(cfg))
    for S in cfg:
        i = idx[S]
        M[i, i] = V * sum(1 for (u, v) in B if u in S and v in S)
        for (u, v) in B:
            for (src, dst) in ((u, v), (v, u)):
                if src in S and dst not in S:
                    T = frozenset((S - {src}) | {dst})
                    sgn = jw_sign(S, src, dst) if graded else 1
                    M[idx[T], i] += -t * sgn
    return cfg, idx, M


def slater(cfg, idx, Phi, N):
    """Slater-determinant amplitudes of the N orbitals in Phi, exact."""
    v = zeros(len(cfg), 1)
    for S in cfg:
        rows = sorted(S)
        v[idx[S]] = sp.expand(sp.radsimp(
            Matrix(N, N, lambda a, b: Phi[rows[a], b]).det()))
    return v


LAM = sp.Symbol("lam")


def count_below(M, tau):
    """Exact count of eigenvalues of the symmetric integer matrix M below tau."""
    p = sp.Poly(M.charpoly(LAM).as_expr(), LAM)
    return p.count_roots(sp.S.NegativeInfinity, tau)


def ground_certificate(M, v, E, lo, hi):
    """Exact: M v = E v, v nonzero, and E is the simple lowest eigenvalue."""
    n = M.shape[0]
    return (sp.simplify(M * v - E * v) == zeros(n, 1)
            and sp.simplify((v.T * v)[0]) == 1
            and lo < E < hi
            and count_below(M, lo) == 0
            and count_below(M, hi) == 1)


# ======================= local operator span, boundaries, and hopping sign gauge

# The two-qubit covariant span is exactly 4-dimensional.

def kron(A, B):
    return Matrix(sp.kronecker_product(A, B))


one2 = eye(2)
n1s = Matrix([[0, 0], [0, 1]])
a1s = Matrix([[0, 1], [0, 0]])
nA, nB = kron(n1s, one2), kron(one2, n1s)
HOP2 = sp.expand(kron(a1s.T, a1s) + kron(a1s, a1s.T))
EXCH = Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
NTOT = nA + nB

hp = list(symbols("hd0:4", real=True)) + list(symbols("hx0:6", real=True)) \
     + list(symbols("hy0:6", real=True))
HG = zeros(4, 4)
_k = 0
for _i in range(4):
    HG[_i, _i] = hp[_i]
for _i in range(4):
    for _j in range(_i + 1, 4):
        HG[_i, _j] = hp[4 + _k] + I * hp[10 + _k]
        HG[_j, _i] = hp[4 + _k] - I * hp[10 + _k]
        _k += 1
f1_sol = sp.solve(list(HG * NTOT - NTOT * HG) + list(EXCH * HG * EXCH - HG),
                  hp, dict=True)
HF = HG.subs(f1_sol[0])
f1_free = sorted(HF.free_symbols, key=sp.default_sort_key)
BASIS4 = [eye(4), NTOT, sp.expand(nA * nB), HOP2]
rows4 = Matrix([[e for e in M] for M in BASIS4])
cc = symbols("cc0:4", real=True)
f1_lin = sp.solve(list(sp.expand(cc[0] * BASIS4[0] + cc[1] * BASIS4[1]
                                 + cc[2] * BASIS4[2] + cc[3] * BASIS4[3] - HF)),
                  list(cc), dict=True)
SEC1 = [1, 2]  # the one-particle sector of the two-qubit space
f1_const = all(Matrix(2, 2, lambda p, q: M[SEC1[p], SEC1[q]]) == M[SEC1[0], SEC1[0]] * eye(2)
               for M in (eye(4), NTOT))
check("local-operator-span [exact]: number conservation and factor exchange give the "
      "4-dimensional span {1,n_A+n_B,n_A n_B,exchange hopping}; the first two are local "
      "one-particle-block constants",
      len(f1_sol) == 1 and len(f1_free) == 4 and rows4.rank() == 4
      and len(f1_lin) == 1 and len(f1_lin[0]) == 4 and f1_const
      and sp.expand(HOP2 * NTOT - NTOT * HOP2) == zeros(4, 4)
      and sp.expand(EXCH * HOP2 * EXCH - HOP2) == zeros(4, 4))

# The summed local linear term is degree-weighted and generally nonconstant.

def summed_linear_values(L, B):
    degrees = [sum(i in edge for edge in B) for i in range(L)]
    return degrees, [sum(degrees[i] for i in S) for S in configs_of(L, 1)]


boundary_expected = {
    "chain6": [1, 2, 2, 2, 2, 1],
    "grid2x3": [2, 3, 2, 2, 3, 2],
    "cube": [3, 3, 3, 3, 3, 3, 3, 3],
    "grid3x3": [2, 3, 2, 3, 4, 3, 2, 3, 2],
}
boundary_actual = {}
for boundary_name, boundary_cluster in (
        ("chain6", CHAIN6), ("grid2x3", GRID23),
        ("cube", CUBE), ("grid3x3", GRID33)):
    degrees, values = summed_linear_values(*boundary_cluster)
    boundary_actual[boundary_name] = values
    assert degrees == values
check("boundary-degree-term [exact]: summed one-particle diagonals are "
      "[1,2,2,2,2,1], [2,3,2,2,3,2], 3 x 8, and [2,3,2,3,4,3,2,3,2]; three open graphs "
      "are nonconstant",
      boundary_actual == boundary_expected
      and all(len(set(boundary_actual[name])) > 1
              for name in ("chain6", "grid2x3", "grid3x3"))
      and len(set(boundary_actual["cube"])) == 1)

# The diagonal t=0 limit has sparse ground-projector support.

zero_hopping_zero_counts = []
for _, (zero_L, zero_B), zero_N in CASES:
    zero_cfg, _, zero_H = sector(zero_L, zero_B, zero_N, False, 0, 1)
    zero_diagonal = [zero_H[i, i] for i in range(len(zero_cfg))]
    zero_ground = min(zero_diagonal)
    zero_hopping_zero_counts.append(sum(value != zero_ground for value in zero_diagonal))
check("zero-hopping-boundary [exact]: at t=0,V=1 the four normalized ground-projector "
      "distributions have 7,18,68,62 zero entries; positivity is scoped to t!=0",
      zero_hopping_zero_counts == [7, 18, 68, 62])

# The sign of nonzero t is a diagonal gauge on a bipartite cluster.

Vs = sp.Symbol("Vs", real=True)
SUBA = frozenset(s for s in range(6) if ((s // 3) + (s % 3)) % 2 == 0)
f2 = True
for f2_graded in (False, True):
    for f2_N in (2, 3):
        cfg, idx, Hp = sector(GRID23[0], GRID23[1], f2_N, f2_graded, 1, Vs)
        _, _, Hm = sector(GRID23[0], GRID23[1], f2_N, f2_graded, -1, Vs)
        U = sp.diag(*[(-1) ** len(S & SUBA) for S in cfg])
        f2 = (f2 and all(U[i, i] ** 2 == 1 for i in range(len(cfg)))
              and sp.expand(U * Hp * U - Hm) == zeros(len(cfg), len(cfg)))
check("hopping-sign-gauge [exact]: on grid2x3 the operator "
      "U = (-1)^{N_A} for the sublattice {0,2,4} has entries +-1 and satisfies "
      "U H(1,V) U = H(-1,V) for symbolic V, both constructions, N=2 and 3; with positive "
      "rescaling the nonzero-hopping parameter is g=V/abs(t)",
      f2)

# =============================================== exact one-dimensional identity

# The two constructions give the same chain6 sector matrix.

a1 = True
a1_dims = []
for a1_N in (2, 3):
    _, _, Hg = sector(CHAIN6[0], CHAIN6[1], a1_N, True, 1, Vs)
    ca, _, Hu = sector(CHAIN6[0], CHAIN6[1], a1_N, False, 1, Vs)
    a1_dims.append(len(ca))
    a1 = a1 and Hg == Hu
    a1 = a1 and all(sp.expand(e.coeff(Vs, 0)) in (0, -1) for e in Hg)
check("chain-matrix-identity [exact]: chain6 N=2 (dim %d) and N=3 (dim %d) graded and ungraded "
      "sector matrices at t = 1 with symbolic V agree entrywise, hopping and interaction "
      "alike, every bond of a line carrying an empty Jordan-Wigner string; hence "
      "their occupation distributions agree at every real g"
      % (a1_dims[0], a1_dims[1]),
      a1)

# ------------------------------------------------- numerical witness machinery

def np_parts(L, B, N, graded):
    """Float hopping matrix T (t = 1) and interaction diagonal D of a sector."""
    cfg = configs_of(L, N)
    idx = {c: i for i, c in enumerate(cfg)}
    T = np.zeros((len(cfg), len(cfg)))
    D = np.zeros(len(cfg))
    for S in cfg:
        i = idx[S]
        D[i] = sum(1 for (u, v) in B if u in S and v in S)
        for (u, v) in B:
            for (src, dst) in ((u, v), (v, u)):
                if src in S and dst not in S:
                    sgn = jw_sign(S, src, dst) if graded else 1
                    T[idx[frozenset((S - {src}) | {dst})], i] += -sgn
    return T, D


DEG_TOL = 1e-9


def rstat(T, D, g):
    """Record statistics: normalized ground-space projector diagonal (float)."""
    w, Vm = eigh(T + g * np.diag(D))
    m = int(np.sum(w < w[0] + DEG_TOL))
    return (Vm[:, :m] ** 2).sum(axis=1) / m


GRID_G = np.linspace(-6.0, 6.0, 241)


def best_match(Tu, Du, Ptarget):
    """Scan then refine: min_g L1(P_ungraded(g), Ptarget) and its argument."""
    f = lambda g: float(np.abs(rstat(Tu, Du, g) - Ptarget).sum())
    ds = [f(g) for g in GRID_G]
    k = int(np.argmin(ds))
    lo = GRID_G[max(k - 1, 0)]
    hi = GRID_G[min(k + 1, len(GRID_G) - 1)]
    r = minimize_scalar(f, bounds=(lo, hi), method="bounded",
                        options={"xatol": 1e-10})
    if float(r.fun) < ds[k]:
        return float(r.fun), float(r.x)
    return ds[k], float(GRID_G[k])


# Numerical witness for the one-dimensional identity.

Tc_u, Dc_u = np_parts(CHAIN6[0], CHAIN6[1], 2, False)
Tc_g, Dc_g = np_parts(CHAIN6[0], CHAIN6[1], 2, True)
a2_d = [float(np.abs(rstat(Tc_u, Dc_u, g) - rstat(Tc_g, Dc_g, g)).sum())
        for g in (0.0, 1.0)]
check("chain-distance-control [numerical]: chain6 N=2 L1 distance between occupation "
      "distributions is "
      "%.2e at g = 0 and %.2e at g = 1, both below 1e-12 (float, scipy eigh)"
      % (a2_d[0], a2_d[1]),
      max(a2_d) < 1e-12)

# ========================================= ungraded normalized-slice positivity

# Nonpositive off-diagonal and an irreducible configuration graph.

b1 = True
b1_dims = []
for (nm, (L, B), N) in CASES:
    cfg, idx, H0 = sector(L, B, N, False, 1, 0)
    n = len(cfg)
    b1_dims.append(n)
    b1 = b1 and all(H0[i, i] == 0 for i in range(n))
    b1 = b1 and all(H0[i, j] in (0, -1) for i in range(n) for j in range(n) if i != j)
    b1 = b1 and H0 == H0.T
    nbr = {i: [j for j in range(n) if j != i and H0[i, j] == -1] for i in range(n)}
    seen, stack = {0}, [0]
    while stack:
        u = stack.pop()
        for w_ in nbr[u]:
            if w_ not in seen:
                seen.add(w_)
                stack.append(w_)
    b1 = b1 and len(seen) == n
check("ungraded-connectivity [exact]: on grid2x3 N=2/3 (dim %d,%d), cube N=4 (%d), "
      "grid3x3 N=3 (%d), the "
      "ungraded off-diagonal at t = 1 is minus the 0/1 configuration adjacency, entries in "
      "{0,-1}, symmetric, that graph connected by exact BFS; Perron-Frobenius then gives a "
      "simple strictly positive ground vector at every real g on this normalized slice"
      % tuple(b1_dims),
      b1)

# Numerical witness of strict positivity.

b2_min = 1.0
for (nm, (L, B), N) in CASES:
    Tu, Du = np_parts(L, B, N, False)
    for g in (-2.0, 0.0, 1.0, 3.0):
        b2_min = min(b2_min, float(rstat(Tu, Du, g).min()))
check("ungraded-positivity-sample [numerical]: the smallest ungraded ground occupation "
      "probability over the "
      "sixteen cluster-sector-g cases, g in {-2, 0, 1, 3}, is %.2e, above the 1e-06 "
      "threshold (float)" % b2_min,
      b2_min > 1e-6)

# ========================================== graded free-point exact distributions

W1 = Matrix([1, sqrt(2), 1]) / 2          # path-of-3 orbital, eigenvalue  sqrt2
W2 = Matrix([1, 0, -1]) / sqrt(2)         # path-of-3 orbital, eigenvalue  0
U2 = Matrix([1, 1]) / sqrt(2)             # path-of-2 orbital, eigenvalue  1


def product_orbital(fs, dims):
    """Product orbital on a product cluster, sites ordered as nested indices."""
    out = []
    for t in itertools.product(*[range(d) for d in dims]):
        e = 1
        for f, k in zip(fs, t):
            e = e * f[k]
        out.append(sp.expand(e))
    return Matrix(out)


# Exact grid2x3 free-point distribution.

A23 = adjacency(*GRID23)
c1_spec = A23.eigenvals()
phi1 = product_orbital([U2, W1], [2, 3])
phi2 = product_orbital([U2, W2], [2, 3])
c1_orb = (sp.simplify(A23 * phi1 - (1 + sqrt(2)) * phi1) == zeros(6, 1)
          and sp.simplify(A23 * phi2 - phi2) == zeros(6, 1))
c1_cfg, c1_idx, H23 = sector(GRID23[0], GRID23[1], 2, True, 1, 0)
c1_v = slater(c1_cfg, c1_idx, Matrix.hstack(phi1, phi2), 2)
c1_E = -(2 + sqrt(2))
c1_ok = ground_certificate(H23, c1_v, c1_E,
                           Rational(-3415, 1000), Rational(-3413, 1000))
C1P = {tuple(sorted(S)): sp.nsimplify(sp.expand(c1_v[c1_idx[S]] ** 2)) for S in c1_cfg}
c1_expect = {}
for S in c1_cfg:
    i, j = sorted(S)
    d = abs((i % 3) - (j % 3))
    c1_expect[(i, j)] = (0 if d == 0 else Rational(1, 16) if d == 1 else Rational(1, 8))
c1_counts = [sum(1 for p in C1P.values() if p == q) for q in (0, Rational(1, 16), Rational(1, 8))]
check("grid2x3-free-point [exact]: N=2,g=0 spectrum {+-1}+{sqrt2,0,-sqrt2}; the two lowest "
      "orbitals of -A are (1,1)/sqrt2 (x) (1,sqrt2,1)/2 at -(1+sqrt2) and (1,1)/sqrt2 (x) "
      "(1,0,-1)/sqrt2 at -1; ground energy -(2+sqrt2), simple; the 15 pair values: 0 on %d "
      "vertical pairs, 1/16 on %d, 1/8 on %d, sum 1"
      % tuple(c1_counts),
      c1_orb and c1_ok and C1P == c1_expect and sum(C1P.values()) == 1
      and c1_spec == {1 + sqrt(2): 1, 1: 1, 1 - sqrt(2): 1,
                      -1 + sqrt(2): 1, -1: 1, -1 - sqrt(2): 1}
      and c1_counts == [3, 8, 4])

# Exact cube free-point distribution.

A8 = adjacency(*CUBE)
c2_spec = A8.eigenvals()
o2, w2v = Matrix([1, 1]), Matrix([1, -1])
c2_orbs = [product_orbital([o2, o2, o2], [2, 2, 2]) / sqrt(8),
           product_orbital([w2v, o2, o2], [2, 2, 2]) / sqrt(8),
           product_orbital([o2, w2v, o2], [2, 2, 2]) / sqrt(8),
           product_orbital([o2, o2, w2v], [2, 2, 2]) / sqrt(8)]
c2_orb = all(sp.simplify(A8 * v - e * v) == zeros(8, 1)
             for v, e in zip(c2_orbs, [3, 1, 1, 1]))
c2_cfg, c2_idx, H8 = sector(CUBE[0], CUBE[1], 4, True, 1, 0)
c2_v = slater(c2_cfg, c2_idx, Matrix.hstack(*c2_orbs), 4)
c2_ok = ground_certificate(H8, c2_v, sp.Integer(-6), Rational(-13, 2), Rational(-11, 2))
C2P = {tuple(sorted(S)): sp.nsimplify(sp.expand(c2_v[c2_idx[S]] ** 2)) for S in c2_cfg}
c2_counts = [sum(1 for p in C2P.values() if p == q)
             for q in (0, Rational(1, 64), Rational(1, 16))]
c2_zero = sorted(k for k in C2P if C2P[k] == 0)
c2_faces, c2_edgepairs = [], []
for k in c2_zero:
    trip = [(s >> 2 & 1, s >> 1 & 1, s & 1) for s in k]
    ed = [(u, v) for u, v in itertools.combinations(k, 2) if bin(u ^ v).count("1") == 1]
    if any(len({t[ax] for t in trip}) == 1 for ax in range(3)):
        c2_faces.append(k)
    elif len(ed) == 2 and len(set(ed[0]) | set(ed[1])) == 4:
        c2_edgepairs.append(k)
check("cube-free-point [exact]: N=4,g=0 four lowest orbitals of -A are products at -3 "
      "((1,1)^(x)3/sqrt8) and -1 (three, one factor (1,-1)), fifth level +1; ground energy "
      "-6, simple; the 70 patterns take {0, 1/64, 1/16} with counts %d, %d, %d, sum 1, the %d "
      "zeros being %d occupied faces and %d two-disjoint-adjacent-pair patterns"
      % (c2_counts[0], c2_counts[1], c2_counts[2], len(c2_zero),
         len(c2_faces), len(c2_edgepairs)),
      c2_orb and c2_ok and sum(C2P.values()) == 1
      and c2_spec == {3: 1, 1: 3, -1: 3, -3: 1}
      and set(C2P.values()) == {0, Rational(1, 64), Rational(1, 16)}
      and c2_counts == [12, 56, 2] and len(c2_faces) == 6 and len(c2_edgepairs) == 6)

# Exact grid3x3 free-point distribution.

A9 = adjacency(*GRID33)
c3_spec = A9.eigenvals()
c3_orbs = [product_orbital([W1, W1], [3, 3]),
           product_orbital([W1, W2], [3, 3]),
           product_orbital([W2, W1], [3, 3])]
c3_orb = all(sp.simplify(A9 * v - e * v) == zeros(9, 1)
             for v, e in zip(c3_orbs, [2 * sqrt(2), sqrt(2), sqrt(2)]))
c3_gram = Matrix(3, 3, lambda i, j: sp.simplify((c3_orbs[i].T * c3_orbs[j])[0]))
c3_cfg, c3_idx, H9 = sector(GRID33[0], GRID33[1], 3, True, 1, 0)
c3_v = slater(c3_cfg, c3_idx, Matrix.hstack(*c3_orbs), 3)
c3_ok = ground_certificate(H9, c3_v, -4 * sqrt(2),
                           Rational(-566, 100), Rational(-565, 100))
C3P = {tuple(sorted(S)): sp.nsimplify(sp.expand(sp.radsimp(c3_v[c3_idx[S]] ** 2)))
       for S in c3_cfg}
c3_vals = [Rational(0), Rational(1, 256), Rational(1, 128), Rational(1, 64),
           Rational(1, 32), Rational(9, 256)]
c3_counts = [sum(1 for p in C3P.values() if p == q) for q in c3_vals]
c3_zero = sorted(k for k in C3P if C3P[k] == 0)
c3_lines = set()
for r in range(3):
    c3_lines.add(tuple(3 * r + c for c in range(3)))
    c3_lines.add(tuple(3 * c + r for c in range(3)))
c3_lines.add((0, 4, 8))
c3_lines.add((2, 4, 6))
check("grid3x3-free-point [exact]: N=3,g=0 orbitals of -A are w1(x)w1 at -2sqrt2 and "
      "w1(x)w2, w2(x)w1 at -sqrt2, orthonormal, next level 0; ground energy -4sqrt2, simple; "
      "the 84 patterns take {0, 1/256, 1/128, 1/64, 1/32, 9/256} with counts %d, %d, %d, %d, "
      "%d, %d, sum 1, the %d zeros being the 3 rows, 3 columns and 2 diagonals"
      % tuple(c3_counts + [len(c3_zero)]),
      c3_orb and c3_ok and c3_gram == eye(3) and sum(C3P.values()) == 1
      and c3_spec == {2 * sqrt(2): 1, sqrt(2): 2, 0: 3, -sqrt(2): 2, -2 * sqrt(2): 1}
      and set(C3P.values()) == set(c3_vals) and c3_counts == [8, 12, 32, 20, 8, 4]
      and set(c3_zero) == c3_lines)

# Exact support property of the declared bond-product comparator.

def bond_types(S, B):
    """Counts (n00, n01, n11) of bond types of a pattern."""
    n00 = n01 = n11 = 0
    for (u, v) in B:
        k = (u in S) + (v in S)
        if k == 0:
            n00 += 1
        elif k == 1:
            n01 += 1
        else:
            n11 += 1
    return (n00, n01, n11)


c4_vert = [(c, c + 3) for c in range(3)]
c4_horz = [(0, 1), (1, 2), (3, 4), (4, 5)]
c4_support = [bond_types(frozenset(k), GRID23[1]) for k in c4_vert + c4_horz]
check("bond-product-support [exact]: grid2x3 N=2 declared weights give each pattern "
      "w00^n00 w01^n01 w11^n11; all %d vertical and %d horizontal adjacent pairs carry all "
      "three bond types (n00,n01,n11 >= 1), hence share support status, while the graded "
      "distribution has vertical probability 0 and horizontal probability 1/16"
      % (len(c4_vert), len(c4_horz)),
      all(min(t) >= 1 for t in c4_support)
      and all(C1P[k] == 0 for k in c4_vert)
      and all(C1P[k] == Rational(1, 16) for k in c4_horz)
      and sorted(k for k in C1P if C1P[k] == 0) == sorted(c4_vert))

# ========================================== bounded finite-window distance scan

d1_all = []
for (nm, (L, B), N) in CASES:
    Tu, Du = np_parts(L, B, N, False)
    Tg, Dg = np_parts(L, B, N, True)
    res = [best_match(Tu, Du, rstat(Tg, Dg, gt)) for gt in (0.0, 1.0)]
    d1_all.extend(r[0] for r in res)
    check("finite-window-distance [numerical]: %s N=%d min L1(P_ungraded(g),P_graded(g_t)) "
          "over the "
          "241-point [-6,6] scan, bounded refinement, is %.3f at g = %.3f (g_t = 0) and %.3f "
          "at g = %.3f (g_t = 1), both at or above 0.15 (float)"
          % (nm, N, res[0][0], res[0][1], res[1][0], res[1][1]),
          min(res[0][0], res[1][0]) >= 0.15)

d2 = [best_match(Tc_u, Dc_u, rstat(Tc_g, Dc_g, gt)) for gt in (0.0, 1.0)]
check("finite-window-chain-control [numerical]: chain6 N=2 returns %.2e at g=%.3f "
      "(g_t = 0) and %.2e at g = %.3f (g_t = 1), both below 1e-09 and attained at g = g_t, so "
      "the scan finds an exact match when one exists"
      % (d2[0][0], d2[0][1], d2[1][0], d2[1][1]),
      max(d2[0][0], d2[1][0]) < 1e-9 and abs(d2[0][1]) < 1e-6 and abs(d2[1][1] - 1) < 1e-6)

# ====================================== symmetry identity and sampled persistence

def automorphisms(L, B):
    """Every site permutation preserving the bond set, by exact backtracking."""
    adj = [set() for _ in range(L)]
    for (u, v) in B:
        adj[u].add(v)
        adj[v].add(u)
    out, perm, used = [], [-1] * L, [False] * L

    def rec(i):
        if i == L:
            out.append(tuple(perm))
            return
        for j in range(L):
            if used[j] or len(adj[j]) != len(adj[i]):
                continue
            if all((k in adj[i]) == (perm[k] in adj[j]) for k in range(i)):
                perm[i], used[j] = j, True
                rec(i + 1)
                used[j] = False
        perm[i] = -1

    rec(0)
    return out


def perm_sign(seq):
    """Sign of the permutation sorting seq, by exact inversion count."""
    s = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def u_sigma(cfg, idx, sg, graded):
    """U_sigma as (image, sign) per pattern: U |S> = sgn_S(sigma) |sigma S>."""
    p, s = [0] * len(cfg), [0] * len(cfg)
    for S in cfg:
        img = [sg[k] for k in sorted(S)]
        p[idx[S]] = idx[frozenset(img)]
        s[idx[S]] = perm_sign(img) if graded else 1
    return p, s


def int_parts(M, n):
    """Exact integer pair (coeff of V^0, of V^1) per entry, reconstruction checked."""
    C = [[(int(sp.expand(M[i, j]).coeff(Vs, 0)), int(sp.expand(M[i, j]).coeff(Vs, 1)))
          for j in range(n)] for i in range(n)]
    ok = all(sp.expand(M[i, j] - C[i][j][0] - C[i][j][1] * Vs) == 0
             for i in range(n) for j in range(n))
    return C, ok


def predicted_zeros(cfg, autos, chi, graded):
    """{S : some sigma fixes S with chi(sigma) sgn_S(sigma) = -1}."""
    out = set()
    for S in cfg:
        for sg in autos:
            if frozenset(sg[k] for k in S) != S:
                continue
            sgn = perm_sign([sg[k] for k in sorted(S)]) if graded else 1
            if chi[sg] * sgn == -1:
                out.add(tuple(sorted(S)))
                break
    return out


ECASES = [("grid2x3", GRID23, 2, c1_cfg, c1_idx, c1_v, C1P),
          ("cube", CUBE, 4, c2_cfg, c2_idx, c2_v, C2P),
          ("grid3x3", GRID33, 3, c3_cfg, c3_idx, c3_v, C3P)]
EAUT = {nm: automorphisms(L, B) for (nm, (L, B), N, cfg, idx, cv, P) in ECASES}

# Signed permutation representations commute with the matrix.

e1 = True
e1_na, e1_img = [], []
for (nm, (L, B), N, cfg, idx, cv, P) in ECASES:
    autos = EAUT[nm]
    n = len(cfg)
    e1_na.append(len(autos))
    for graded in (True, False):
        _, _, Hsym = sector(L, B, N, graded, 1, Vs)
        C, dec = int_parts(Hsym, n)
        e1 = e1 and dec
        reps = {}
        for sg in autos:
            p, s = u_sigma(cfg, idx, sg, graded)
            reps[sg] = (p, s)
            e1 = e1 and sorted(p) == list(range(n)) and all(x in (1, -1) for x in s)
            e1 = e1 and all(C[p[i]][p[j]] == (s[i] * s[j] * C[i][j][0],
                                              s[i] * s[j] * C[i][j][1])
                            for i in range(n) for j in range(n))
        for sa in autos:
            pa, ssa = reps[sa]
            for sb in autos:
                pb, ssb = reps[sb]
                pc, ssc = reps[tuple(sa[sb[k]] for k in range(L))]
                e1 = e1 and all(pa[pb[i]] == pc[i] and ssb[i] * ssa[pb[i]] == ssc[i]
                                for i in range(n))
        if graded:
            e1_img.append(len({(tuple(p), tuple(s)) for (p, s) in reps.values()}))
check("symmetry-representation [exact]: the %d,%d,%d bond-preserving site permutations of "
      "grid2x3 "
      "N=2, cube N=4, grid3x3 N=3 act by U_sigma|S> = sgn_S(sigma)|sigma S>, a signed "
      "permutation commuting with H(1,V) for symbolic V in both compositions; "
      "sigma -> U_sigma a homomorphism of image order %d, %d, %d" % tuple(e1_na + e1_img),
      e1)

# Exact character and forced-zero sets at the free point.

e2 = True
e2_sz, ECHI, EPRED = [], {}, {}
for (nm, (L, B), N, cfg, idx, cv, P) in ECASES:
    autos, n, chi = EAUT[nm], len(cfg), {}
    j0 = next(i for i in range(n) if cv[i] != 0)
    for sg in autos:
        p, s = u_sigma(cfg, idx, sg, True)
        ch = 1 if sp.expand(s[j0] * cv[j0] - cv[p[j0]]) == 0 else -1
        e2 = e2 and all(sp.expand(s[i] * cv[i] - ch * cv[p[i]]) == 0 for i in range(n))
        chi[sg] = ch
    ECHI[nm] = chi
    pred = predicted_zeros(cfg, autos, chi, True)
    EPRED[nm] = pred
    exact = {k for k in P if P[k] == 0}
    e2 = e2 and pred <= exact
    e2_sz.extend([len(pred), len(exact)])
e2 = (e2 and EPRED["grid2x3"] == set(c4_vert)
      and EPRED["cube"] == set(c2_faces) | set(c2_edgepairs)
      and EPRED["grid3x3"] == {ln for ln in c3_lines if 4 in ln})
check("free-point-symmetry-zeros [exact]: each U_sigma acts on the exact graded ground vector "
      "as a scalar chi in {+1,-1}, verified on every pattern; the predicted set "
      "{S : sigma S = S, chi sgn_S = -1} lies inside the exact zero set, %d of %d (vertical "
      "pairs), %d of %d (faces, disjoint adjacent pairs), %d of %d (lines through the centre)"
      % tuple(e2_sz),
      e2)

# Ungraded free-point contrast; structural sign plus numerical eigenvector checks.

e3 = True
e3_min = 1.0
for (nm, (L, B), N, cfg, idx, cv, P) in ECASES:
    autos, n = EAUT[nm], len(cfg)
    Tu, Du = np_parts(L, B, N, False)
    wu, Vu = eigh(Tu)
    vu = Vu[:, 0] if Vu[0, 0] > 0 else -Vu[:, 0]
    e3 = e3 and wu[1] - wu[0] > DEG_TOL
    e3_min = min(e3_min, float(vu.min()))
    chiu = {}
    for sg in autos:
        p, s = u_sigma(cfg, idx, sg, False)
        e3 = e3 and all(x == 1 for x in s)
        e3 = e3 and max(abs(vu[i] - vu[p[i]]) for i in range(n)) < 1e-9
        chiu[sg] = 1
    e3 = e3 and predicted_zeros(cfg, autos, chiu, False) == set()
check("ungraded-symmetry-contrast [exact/numerical]: U_sigma is unsigned; the computed "
      "strictly positive ground vector (smallest entry %.2e, float) is invariant under all "
      "%d,%d,%d automorphisms, giving chi=+1 and an empty forced-zero set"
      % tuple([e3_min] + e1_na),
      e3)

# Numerical persistence sample away from the free point.

E_GS = (0.25, -0.25, 0.4, -0.4, 0.5, 0.75, 1.0, 2.0)
e4 = True
e4_sz, e4_gap = [], 1e9
for (nm, (L, B), N, cfg, idx, cv, P) in ECASES:
    pi = {idx[frozenset(k)] for k in EPRED[nm]}
    Tg, Dg = np_parts(L, B, N, True)
    inter = None
    for g in (0.0,) + E_GS:
        wg, Vg = eigh(Tg + g * np.diag(Dg))
        e4_gap = min(e4_gap, float(wg[1] - wg[0]))
        e4 = e4 and wg[1] - wg[0] > DEG_TOL
        z = {i for i in range(len(cfg)) if abs(Vg[i, 0]) < 1e-12}
        e4 = e4 and pi <= z
        inter = z if inter is None else inter & z
    e4 = e4 and inter == pi
    e4_sz.append(len(inter))
check("sampled-symmetry-persistence [numerical]: at g in {0,+-0.25,+-0.4,0.5,0.75,1,2} the "
      "graded ground state stays simple (smallest gap %.3f) and its zero set below 1e-12 "
      "contains the predicted set, whose intersection over the nine couplings it equals: "
      "%d, %d, %d (float)" % tuple([e4_gap] + e4_sz),
      e4)

print("SUMMARY: the declared nonzero-hopping subfamily has identical chain matrices; on the "
      "named two- and three-dimensional cases its ungraded ground vectors are strictly "
      "positive, while exact graded g=0 distributions contain 3, 12, and 8 zeros, of which "
      "3, 12, and 4 are symmetry-forced at g=0; nine-coupling persistence and finite-window "
      "L1 separation >= %.3f are numerical observations."
      % min(d1_all))
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
