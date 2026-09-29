#!/usr/bin/env python3
"""J:falsifier:PR9300 -- the composite-site comparator's flux-free bands: does the slice Chern profile follow the node positions and charges exactly?

Target claims (PR #9300; supplied u = +1 quadratic Majorana comparator, J_x = J_y = 1, J_z = J, odd term kappa; fractional momenta f in units of the primitive
translations t1 = (2,0,0), t2 = (0,2,0), t3 = (1,1,2) of the network in p-coordinates):
 (E) on f = (x, 1 - x, 0): det H = 16 (J^2 + 4 c^2 kappa^2 - 2 c - 4 kappa^2 - 2)^2, c = cos 2 pi x, so the middle levels vanish on J^2 = 2 (1 + c)(1 + 2 kappa^2 (1 - c));
 (S) the slice fluxes of the lowest two bands averaged over 96 slices per axis are (arccos c / pi, -arccos c / pi, 0) at J = 1, kappa = 0.1, 0.3 ("if the continuum slice
     Chern numbers were +1 outside the interval between the two zeros on the line and 0 inside, mirrored along f_2"), reversing at kappa = -0.3;
 (N) at kappa = 0.6 (six numerical groups) the averages equal minus the flux-weighted sum of the group positions modulo one.
The PR checks the averages to two slice spacings (0.021). This script tests the structure behind them: the slice Chern number is a step function of the slice position,
C_a(f) = C_a(0+) + sum over nodes n with f_n^a < f of q_n, so its exact average is C_a(0+) + sum_n q_n (1 - f_n^a), with no resolution slack.

Machinery disjoint from the PR's runner: (1) the network and its Hamiltonian are built here from the landed construction's stated rules (kept sites, axial neighbours, flavour
alternating along chains and shifted in layers 2,3, z on interlayer bonds), assembled first as a real-space matrix on a periodic p-torus with no reference to the four-site
reduction, then as the Bloch matrix, and the two are compared level by level on 54 momenta; (2) the determinant identity is checked symbolically on the script's own Bloch matrix;
(3) Chern numbers come from the Kubo/TKNN Berry-curvature formula (gauge invariant, no link overlaps, no Fukui plaquettes), cross-checked against a Fukui link count on sample slices
so the sign convention is the PR's; (4) nodes come from a grid of local minima of the middle gap refined by minimisation, not from the PR's certified adaptive cubes.
Floating point is labelled. Prints SUMMARY: and, only if a falsifier fires, HIT:.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
import sympy as sp
from scipy.optimize import minimize

RESULTS = []
FIRED = []
T0 = time.time()
DRY = "--dry" in sys.argv


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def fire(msg):
    FIRED.append(msg)


# ------------------------------------------------------------------------------------------------ 1. the network (own construction)
def kept(p):
    i, j, z = p
    m = z % 4
    return (m == 0 and j % 2 == 0) or (m == 1 and i % 2 == 1) or (m == 2 and j % 2 == 1) or (m == 3 and i % 2 == 0)


AXIAL = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def nbrs(p):
    """Kept axial neighbours of a kept site, as unwrapped coordinates."""
    return [tuple(a + b for a, b in zip(p, d)) for d in AXIAL if kept(tuple(a + b for a, b in zip(p, d)))]


def flavour(p, q):
    """z on interlayer bonds; on a chain, x/y alternate with the position of the lower endpoint along the chain, shifted by one in layers z = 2, 3 (mod 4)."""
    d = [b - a for a, b in zip(p, q)]
    if d[2] != 0:
        return "z"
    lo = min(p, q)                                           # lexicographic: the endpoint with the smaller coordinate along the chain
    along = 0 if d[0] != 0 else 1
    idx = lo[along] + (1 if p[2] % 4 in (2, 3) else 0)
    return "x" if idx % 2 == 0 else "y"


def bond_entries(p, J):
    """(q, value) entries A[p, q] of the comparator's antisymmetric matrix: +2 J_flavour from the even-sum end of every bond to the odd-sum end (the antisymmetric partner is added by the caller)."""
    return [(q, 2.0 * J[flavour(p, q)]) for q in nbrs(p)] if sum(p) % 2 == 0 else []


def odd_entries(p, kappa):
    """Odd paths through the middle site p: A[q_l, q_m] = +2 kappa for the cyclic colour pairs (l, m) in (x,y), (y,z), (z,x), q_c the neighbour of p in colour c."""
    nb = {flavour(p, q): q for q in nbrs(p)}
    assert len(nb) == 3
    return [(nb[l], nb[m], 2.0 * kappa) for (l, m) in (("x", "y"), ("y", "z"), ("z", "x"))]


def torus_matrix(L, J, kappa):
    """Real-space antisymmetric matrix A on the periodic p-torus of size L = (Lx, Ly, Lz) (all even, Lz a multiple of 4), H = i A."""
    sites = [p for p in itertools.product(range(L[0]), range(L[1]), range(L[2])) if kept(p)]
    idx = {p: n for n, p in enumerate(sites)}
    w = lambda q: (q[0] % L[0], q[1] % L[1], q[2] % L[2])
    A = np.zeros((len(sites), len(sites)))
    for p in sites:
        for q, v in bond_entries(p, J):
            A[idx[p], idx[w(q)]] += v; A[idx[w(q)], idx[p]] -= v
        for q1, q2, v in odd_entries(p, kappa):
            A[idx[w(q1)], idx[w(q2)]] += v; A[idx[w(q2)], idx[w(q1)]] -= v
    return sites, A


TRANS = np.array([[2, 0, 0], [0, 2, 0], [1, 1, 2]])          # rows: t1, t2, t3
REPS = [p for p in itertools.product(range(2), range(2), range(2)) if kept(p)]


def reduce(p):
    """p = REPS[a] + n1 t1 + n2 t2 + n3 t3: solve for the integer cell index n."""
    for a, r in enumerate(REPS):
        d = np.array(p) - np.array(r)
        n = np.linalg.solve(TRANS.T.astype(float), d.astype(float))
        if np.allclose(n, np.rint(n), atol=1e-9):
            return a, tuple(int(x) for x in np.rint(n))
    raise ValueError(p)


def bloch_entries(J, kappa):
    """Entries (a, b, dn, value) with M(f)[a, b] += value e^(2 pi i f.dn), H(f) = i M(f); dn = cell(col) - cell(row), row site translated to cell 0."""
    out = []
    for a, p in enumerate(REPS):
        for q, v in bond_entries(p, J):
            b, n = reduce(q)
            out.append((a, b, n, v)); out.append((b, a, tuple(-x for x in n), -v))
        for q1, q2, v in odd_entries(p, kappa):
            r1, n1 = reduce(q1); r2, n2 = reduce(q2)
            dn = tuple(y - x for x, y in zip(n1, n2))
            out.append((r1, r2, dn, v)); out.append((r2, r1, tuple(-x for x in dn), -v))
    return out


class Bloch:
    def __init__(self, J, kappa):
        if not isinstance(J, dict):
            J = {"x": J[0], "y": J[1], "z": J[2]}
        self.J, self.kappa = J, kappa
        E = bloch_entries(J, kappa)
        self.a = np.array([e[0] for e in E]); self.b = np.array([e[1] for e in E])
        self.n = np.array([e[2] for e in E], dtype=float); self.v = np.array([e[3] for e in E])

    def M(self, F, deriv=None):
        F = np.atleast_2d(F)
        ph = self.v * np.exp(2j * np.pi * (F @ self.n.T))
        if deriv is not None:
            ph = ph * (2j * np.pi * self.n[:, deriv])
        out = np.zeros((len(F), 4, 4), dtype=complex)
        for j in range(len(self.v)):
            out[:, self.a[j], self.b[j]] += ph[:, j]
        return out

    def H(self, F):
        return 1j * self.M(F)

    def dH(self, F, ax):
        return 1j * self.M(F, ax)

    def levels(self, F):
        return np.linalg.eigvalsh(self.H(F))


def torus_vs_bloch(J, kappa, N, M):
    """The p-torus (2N, 2N, 4M) with M a multiple of N is the quotient by N t1, N t2, 2M t3, so its momenta are f = (a/N, b/N, c/(2M)); compare every level."""
    assert M % N == 0
    sites, A = torus_matrix((2 * N, 2 * N, 4 * M), J, kappa)
    ev_real = np.sort(np.linalg.eigvalsh(1j * A))
    fs = np.array([(a / N, b / N, c / (2 * M)) for a in range(N) for b in range(N) for c in range(2 * M)])
    ev_bloch = np.sort(Bloch(J, kappa).levels(fs).ravel())
    return len(sites), len(fs), float(np.abs(ev_real - ev_bloch).max()) if len(ev_real) == len(ev_bloch) else np.inf


# ---------------------------------------------------------------- 2. (E) exact, symbolic on the script's own Bloch matrix
w_, J_, k_ = sp.symbols("w J kappa")


def sym_det_on_line():
    Js = {"x": sp.Integer(1), "y": sp.Integer(1), "z": J_}
    Mx = sp.zeros(4, 4)
    for a, p in enumerate(REPS):
        ents = [(q, 2 * Js[flavour(p, q)]) for q in nbrs(p)] if sum(p) % 2 == 0 else []
        for q, v in ents:
            b, n = reduce(q)
            ph = w_ ** n[0] * w_ ** (-n[1])                   # f = (x, 1 - x, 0): e^(2 pi i f.n) = w^n0 w^(-n1)
            Mx[a, b] += v * ph; Mx[b, a] -= v / ph
        nb = {flavour(p, q): q for q in nbrs(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
            dn = (n2[0] - n1[0], n2[1] - n1[1])
            ph = w_ ** dn[0] * w_ ** (-dn[1])
            Mx[r1, r2] += 2 * k_ * ph; Mx[r2, r1] -= 2 * k_ / ph
    return sp.expand((sp.I * Mx).det(method="berkowitz"))


# ---------------------------------------------------------------- 3. Berry curvature (Kubo/TKNN) of the two lowest bands
def curvature(B, P, a_ax, b_ax):
    """F_ab = -2 Im sum_{n occ, m unocc} <n|d_a H|m><m|d_b H|n> / (E_n - E_m)^2 for the two lowest bands, at the points P (N, 3); A = i <u|d u>, F = d_a A_b - d_b A_a
    (derivatives in the fractional momenta)."""
    E, V = np.linalg.eigh(B.H(P))
    Da = np.einsum("nia,nij,njb->nab", V.conj(), B.dH(P, a_ax), V)
    Db = np.einsum("nia,nij,njb->nab", V.conj(), B.dH(P, b_ax), V)
    X = np.zeros(len(P), dtype=complex)
    for n in (0, 1):
        for m in (2, 3):
            X += Da[:, n, m] * Db[:, m, n] / (E[:, n] - E[:, m]) ** 2
    return -2.0 * X.imag, E[:, 2] - E[:, 1]


def vec_curvature(B, P):
    """The Berry curvature vector (F_23, F_31, F_12) at the points P."""
    return np.stack([curvature(B, P, 1, 2)[0], curvature(B, P, 2, 0)[0], curvature(B, P, 0, 1)[0]], axis=1)


SIGN = -1.0        # C_link = -(1/2 pi) int F_std: the Fukui-Hatsugai-Suzuki link count (the PR's convention) has this sign relative to A = i <u|d u> (verified below on sample slices)


def slice_chern(B, f, axis, m=64):
    """Chern number of the two lowest bands on the slice f_axis = f, in the PR's (link) sign convention, oriented by the cyclic order (axis+1, axis+2)."""
    o0, o1 = (axis + 1) % 3, (axis + 2) % 3
    u = (np.arange(m) + 0.5) / m
    P = np.zeros((m, m, 3)); P[:, :, o0] = u[:, None]; P[:, :, o1] = u[None, :]; P[:, :, axis] = f
    F, gap = curvature(B, P.reshape(-1, 3), o0, o1)
    return SIGN * F.sum() / m ** 2 * 1.0 / (2 * np.pi) * 1.0 * 1.0 * (1.0), float(gap.min())


def link_chern(B, f, axis, m=48):
    """Fukui-Hatsugai-Suzuki link count (own implementation) of the two lowest bands on the same slice, for the sign cross-check."""
    o0, o1 = (axis + 1) % 3, (axis + 2) % 3
    u = np.arange(m) / m
    P = np.zeros((m, m, 3)); P[:, :, o0] = u[:, None]; P[:, :, o1] = u[None, :]; P[:, :, axis] = f
    E, V = np.linalg.eigh(B.H(P.reshape(-1, 3)))
    V = V[:, :, :2].reshape(m, m, 4, 2)
    lnk = lambda X, Y: np.linalg.det(np.einsum("...ia,...ib->...ab", X.conj(), Y))
    Vx, Vy, Vxy = np.roll(V, -1, axis=0), np.roll(V, -1, axis=1), np.roll(np.roll(V, -1, axis=0), -1, axis=1)
    return float(np.angle(lnk(V, Vx) * lnk(Vx, Vxy) * lnk(Vxy, Vy) * lnk(Vy, V)).sum() / (2 * np.pi))


def sphere_charge(B, c, s=0.01, nth=32, nph=64):
    """Sphere charge (outward orientation, PR sign convention) of the two lowest bands on |f - c| = s: SIGN/(2 pi) * flux of the curvature vector, Gauss-Legendre in cos(theta)."""
    x, wx = np.polynomial.legendre.leggauss(nth)
    ph = (np.arange(nph) + 0.5) * 2 * np.pi / nph
    ct = x[:, None] * np.ones(nph)[None, :]; st = np.sqrt(1 - ct ** 2)
    nx, ny, nz = st * np.cos(ph)[None, :], st * np.sin(ph)[None, :], ct
    P = (np.stack([nx, ny, nz], axis=-1) * s + np.asarray(c)).reshape(-1, 3)
    Bv = vec_curvature(B, P)
    integrand = (Bv * np.stack([nx, ny, nz], axis=-1).reshape(-1, 3)).sum(axis=1).reshape(nth, nph)
    flux = (integrand * wx[:, None]).sum() * (2 * np.pi / nph) * s ** 2
    return SIGN * flux / (2 * np.pi)


# ---------------------------------------------------------------- 4. nodes
def refine_node(B, c0):
    g = lambda f: (lambda e: e[2] - e[1])(B.levels(np.array([f]))[0])
    x = np.asarray(c0, dtype=float)
    for tol in (1e-4, 1e-8, 1e-12):
        r = minimize(g, x, method="Nelder-Mead", options={"xatol": tol * 0.1, "fatol": tol * 1e-3, "maxiter": 4000})
        x = r.x
    return x % 1.0, float(r.fun)


def find_nodes(B, n=24):
    """Local minima of the middle gap eps3 - eps2 on an n^3 periodic grid, each refined by minimisation; those with gap < 1e-8 are nodes (periodic duplicates merged)."""
    g1 = (np.arange(n) + 0.25) / n                       # offset grid: generic positions
    P = np.array(list(itertools.product(g1, g1, g1)))
    E = B.levels(P)
    G = (E[:, 2] - E[:, 1]).reshape(n, n, n)
    loc = np.ones_like(G, dtype=bool)
    for d in itertools.product((-1, 0, 1), repeat=3):
        if d != (0, 0, 0):
            loc &= G <= np.roll(G, d, axis=(0, 1, 2))
    cands = P.reshape(n, n, n, 3)[loc]
    nodes = []
    for c0 in cands:
        x, gap = refine_node(B, c0)
        if gap < 1e-8 and all(np.abs(((x - y[0]) + 0.5) % 1.0 - 0.5).max() > 1e-4 for y in nodes):
            nodes.append((x, gap))
    return nodes, len(cands)


def step_pred(nodes, charges, axis, C0):
    pts = sorted((n[0][axis], q) for n, q in zip(nodes, charges))
    return lambda f: C0 + sum(q for pos, q in pts if pos < f)


def profile_test(B, nodes, charges, ns, guard=0.03):
    """Slice Chern number on ns slices per axis (skipping slices within `guard` of a node along that axis) against the step function fixed by node positions and charges
    (C(0+) read from the first unguarded slice). Returns per axis: max deviation from an integer, C(0+), mismatches, slices used, smallest middle gap."""
    res = {}
    for ax in range(3):
        pos = [n[0][ax] for n in nodes]
        fs = [(i + 0.5) / ns for i in range(ns)]
        fs = [f for f in fs if all(min(abs(f - p), 1 - abs(f - p)) > guard for p in pos)]
        vals = []
        for f in fs:
            near = min(min(abs(f - p), 1 - abs(f - p)) for p in pos) if pos else 1.0
            c, g = slice_chern(B, f, ax, m=256 if near < 0.05 else (128 if near < 0.1 else 64))
            vals.append((f, c, g))
        dev = max(abs(c - round(c)) for _, c, _ in vals)
        C = [round(c) for _, c, _ in vals]
        C0 = C[0] - step_pred(nodes, charges, ax, 0)(vals[0][0])
        pf = step_pred(nodes, charges, ax, C0)
        mism = [(f, c, pf(f)) for (f, _, _), c in zip(vals, C) if c != pf(f)]
        res[ax] = (dev, C0, mism, len(vals), min(g for _, _, g in vals))
    return res


def exact_average(nodes, charges, ax, C0):
    return C0 + sum(q * (1 - n[0][ax]) for n, q in zip(nodes, charges))


def c_closed(J, kap):
    roots = np.roots([-4 * kap ** 2, 2.0, 2 + 4 * kap ** 2 - J ** 2])
    return float(min((r.real for r in roots if abs(r.imag) < 1e-12 and -1 - 1e-12 <= r.real <= 1 + 1e-12), key=lambda r: abs(r + 0.5)))


def run():
    NS = 40 if DRY else 120
    # ---- 0. the Bloch matrix is the Fourier transform of the real-space matrix
    Jd = {"x": 1.0, "y": 1.0, "z": 1.7}
    tests = [((1.0, 1.0, 1.7), 0.31, 2, 2), ((1.0, 1.0, 1.0), 0.6, 3, 3)] if not DRY else [((1.0, 1.0, 1.7), 0.31, 2, 2)]
    parts, okb = [], True
    for J3, kap, N, M in tests:
        ns, nf, d = torus_vs_bloch({"x": J3[0], "y": J3[1], "z": J3[2]}, kap, N, M)
        okb &= d < 1e-10 and ns == 4 * nf
        parts.append(f"J {J3}, kappa {kap}, torus ({2 * N}, {2 * N}, {4 * M}): {ns} sites = 4 x {nf} momenta, max level difference {d:.1e}")
    check("(B) the script's Bloch matrix reproduces, level by level, the spectrum of its own real-space matrix on periodic p-tori built with no four-site reduction "
          "(FLOATING POINT diagonalisation)", okb, "; ".join(parts) + f"; {time.time() - T0:.0f} s")
    if not okb:
        fire("own Bloch matrix disagrees with own real-space matrix")
    # ---- 1. (E)
    dH = sym_det_on_line()
    c_ = (w_ + 1 / w_) / 2
    target = 16 * (J_ ** 2 + 4 * c_ ** 2 * k_ ** 2 - 2 * c_ - 4 * k_ ** 2 - 2) ** 2
    diff = sp.simplify(sp.expand(dH - target))
    curve = J_ ** 2 - 2 * (1 + c_) * (1 + 2 * k_ ** 2 * (1 - c_))
    diff2 = sp.simplify(sp.expand(J_ ** 2 + 4 * c_ ** 2 * k_ ** 2 - 2 * c_ - 4 * k_ ** 2 - 2 - curve))
    check("(E) exact (sympy): on f = (x, 1 - x, 0) the four-band determinant of the script's own Bloch matrix is 16 (J^2 + 4 c^2 kappa^2 - 2 c - 4 kappa^2 - 2)^2 identically in "
          "J, kappa and w = e^(2 pi i x) (c = (w + 1/w)/2), and the bracket equals J^2 - 2 (1 + c)(1 + 2 kappa^2 (1 - c))", diff == 0 and diff2 == 0,
          f"det - target simplifies to {diff}; bracket - curve simplifies to {diff2}; {time.time() - T0:.0f} s")
    if diff != 0 or diff2 != 0:
        fire("(E) determinant identity on the line fails for the script's own Bloch matrix")
    # ---- sign cross-check: Kubo against the Fukui link count on sample slices
    B3 = Bloch((1.0, 1.0, 1.0), 0.3)
    pairs = []
    for ax, f in ((0, 0.1), (0, 0.5), (1, 0.9), (2, 0.4), (2, 0.83)):
        pairs.append((slice_chern(B3, f, ax, m=96)[0], link_chern(B3, f, ax, m=48)))
    okl = all(abs(a - round(a)) < 1e-4 and round(a) == round(b) for a, b in pairs)
    check("(L) the Kubo slice Chern numbers (with the sign fixed as -F/(2 pi)) are integers and equal a Fukui link count (own implementation) on five sample slices, so they carry the PR's sign convention",
          okl, "; ".join(f"{a:+.6f}/{b:+.3f}" for a, b in pairs) + f"; {time.time() - T0:.0f} s")
    if not okl:
        fire("Kubo and link slice Chern numbers disagree")
    # ---- kappa = 0.1, 0.3
    for kap in (0.1, 0.3):
        B = Bloch((1.0, 1.0, 1.0), kap)
        nodes, ncand = find_nodes(B, 16 if DRY else 24)
        charges = [round(sphere_charge(B, n[0])) for n in nodes]
        rawq = [sphere_charge(B, n[0]) for n in nodes]
        c = c_closed(1.0, kap); x0 = np.arccos(c) / (2 * np.pi)
        order = sorted(range(len(nodes)), key=lambda i: tuple(nodes[i][0]))
        print(f"   kappa = {kap}: {ncand} local minima of the gap on the grid, {len(nodes)} nodes: " +
              "; ".join(f"({nodes[i][0][0]:.7f}, {nodes[i][0][1]:.7f}, {nodes[i][0][2]:.7f}) q = {rawq[i]:+.5f}" for i in order) + f"; x0 (closed form) = {x0:.7f}", flush=True)
        okn = len(nodes) == 2 and all(abs(r - q) < 1e-3 for r, q in zip(rawq, charges)) and sorted(charges) == [-1, 1]
        xs = sorted(n[0][0] for n in nodes)
        okpos = okn and all(abs(n[0][0] + n[0][1] - 1) < 1e-6 and min(n[0][2], 1 - n[0][2]) < 1e-6 for n in nodes) and abs(xs[0] - x0) < 1e-6 and abs(xs[1] - (1 - x0)) < 1e-6
        check(f"(N1) kappa = {kap}: two nodes, on f = (x, 1 - x, 0) at x = x0 and 1 - x0 with x0 = arccos(c)/(2 pi) from the closed-form root (to 1e-6), sphere charges (Kubo, own) equal to +-1 and opposite",
              okn and okpos, f"{len(nodes)} nodes, charges {charges}, positions {'match' if okpos else 'DIFFER'}; {time.time() - T0:.0f} s")
        if not (okn and okpos):
            fire(f"kappa = {kap}: node set differs from the two on-line nodes of the closed form")
        res = profile_test(B, nodes, charges, NS)
        allok, parts = True, []
        for ax in range(3):
            dev, C0, mism, nsl, gmin = res[ax]
            ex = exact_average(nodes, charges, ax, C0)
            target = (np.arccos(c) / np.pi, -np.arccos(c) / np.pi, 0.0)[ax]
            good = dev < 1e-3 and not mism and abs(ex - target) < 1e-5
            allok &= good
            parts.append(f"axis {ax}: C(0+) = {C0:+d}, {nsl} slices, max distance to an integer {dev:.1e}, mismatches {len(mism)}, exact average {ex:+.7f} vs closed form {target:+.7f}, min gap {gmin:.3f}")
        check(f"(S1) kappa = {kap}: on {NS} slices per axis (at least 0.03 from a node) the Kubo slice Chern number is an integer and equals the step function fixed by the node positions and charges; "
              "its exact average is (arccos c/pi, -arccos c/pi, 0) to 1e-5, not merely to two slice spacings", allok, "; ".join(parts) + f"; {time.time() - T0:.0f} s")
        if not allok:
            fire(f"kappa = {kap}: slice Chern profile is not the step function of the nodes, or its exact average differs from the closed form")
        if kap == 0.3:
            Bm = Bloch((1.0, 1.0, 1.0), -0.3)
            nm, _ = find_nodes(Bm, 16 if DRY else 24)
            qm = [round(sphere_charge(Bm, n[0])) for n in nm]
            resm = profile_test(Bm, nm, qm, max(NS // 4, 12))
            posm = sorted((tuple(np.round(n[0], 6)), q) for n, q in zip(nm, qm))
            posp = sorted((tuple(np.round(n[0], 6)), q) for n, q in zip(nodes, charges))
            flip = len(nm) == 2 and [p for p, _ in posm] == [p for p, _ in posp] and [q for _, q in posm] == [-q for _, q in posp]
            avgm = [exact_average(nm, qm, ax, resm[ax][1]) for ax in range(3)]
            okm = flip and all(resm[ax][0] < 1e-3 and not resm[ax][2] for ax in range(3)) and abs(avgm[0] + np.arccos(c) / np.pi) < 1e-5 and abs(avgm[1] - np.arccos(c) / np.pi) < 1e-5 and abs(avgm[2]) < 1e-5
            check("(K) kappa = -0.3: the nodes sit at the same positions with every charge reversed, the slice profile is the negated step function, and the averages are (-arccos c/pi, +arccos c/pi, 0) with c the kappa = 0.3 root",
                  okm, f"nodes {len(nm)}, charges reversed {flip}, averages ({avgm[0]:+.6f}, {avgm[1]:+.6f}, {avgm[2]:+.6f}); {time.time() - T0:.0f} s")
            if not okm:
                fire("kappa = -0.3: the reversal of the slice fluxes fails")
    # ---- kappa = 0.6
    B6 = Bloch((1.0, 1.0, 1.0), 0.6)
    n6, nc6 = find_nodes(B6, 16 if DRY else 24)
    rq6 = [sphere_charge(B6, n[0]) for n in n6]
    q6 = [round(x) for x in rq6]
    print(f"   kappa = 0.6: {nc6} local minima, {len(n6)} nodes: " + "; ".join(f"({n[0][0]:.6f}, {n[0][1]:.6f}, {n[0][2]:.6f}) q = {r:+.5f}" for n, r in sorted(zip(n6, rq6), key=lambda t: tuple(t[0][0]))), flush=True)
    res6 = profile_test(B6, n6, q6, NS)
    ok6 = len(n6) == 6 and sum(q6) == 0 and all(abs(r - q) < 1e-3 for r, q in zip(rq6, q6))
    parts = []
    for ax in range(3):
        dev, C0, mism, nsl, gmin = res6[ax]
        ex = exact_average(n6, q6, ax, C0)
        dip = -sum(q * n[0][ax] for n, q in zip(n6, q6))
        dd = abs(((ex - dip) + 0.5) % 1.0 - 0.5)
        ok6 &= dev < 1e-3 and not mism and dd < 1e-9
        parts.append(f"axis {ax}: C(0+) = {C0:+d}, {nsl} slices, max distance to an integer {dev:.1e}, mismatches {len(mism)}, exact average {ex:+.6f}, -sum q f {dip:+.6f} (mod 1 difference {dd:.1e})")
    check(f"(N2) kappa = 0.6: six nodes of total charge 0 with integer Kubo charges; on {NS} slices per axis the slice Chern number is the integer step function of the node positions and charges; "
          "its exact average equals minus the flux-weighted sum of the node positions modulo one to 1e-9", ok6, "; ".join(parts) + f"; {time.time() - T0:.0f} s")
    if not ok6:
        fire("kappa = 0.6: node set, slice profile or the -sum q f identity fails")
    avg6 = [exact_average(n6, q6, ax, res6[ax][1]) for ax in range(3)]
    print(f"   kappa = 0.6 exact averages of the step functions: ({avg6[0]:+.4f}, {avg6[1]:+.4f}, {avg6[2]:+.4f}); the PR quotes (0.104, -0.104, 0) from 96 midpoint slices and (0.093, -0.093, 0) for -sum q f mod 1")
    # ---- control: the profile test must be able to fail
    def with_change(nodes, charges, i, flip=False, shift=None):
        nn = [((n[0] + np.array([shift if (j == i and shift) else 0.0, 0, 0])) % 1.0, n[1]) for j, n in enumerate(nodes)]
        qq = [(-q if (j == i and flip) else q) for j, q in enumerate(charges)]
        return nn, qq
    cok, ctxt = True, []
    for name, (nn, qq) in (("one charge flipped", with_change(n6, q6, 0, flip=True)), ("one node moved by 0.1 along f_1", with_change(n6, q6, 0, shift=0.1))):
        r = profile_test(B6, nn, qq, 36)
        nm_ = sum(len(r[ax][2]) for ax in range(3))
        cok &= nm_ > 0
        ctxt.append(f"{name}: {nm_} mismatching slices")
    check("(S2) control: the same step-function test fails when one node's charge is flipped or one node is moved by 0.1 (the test discriminates)", cok, "; ".join(ctxt) + f"; {time.time() - T0:.0f} s")
    if not cok:
        fire("the profile test does not discriminate (control did not fail)")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0])
        print("HIT: PR #9300 claim fails: " + "; ".join(FIRED))
        sys.exit(1)
    print("SUMMARY: no falsifier fired: with an independently built network (real-space and Bloch matrices agree level by level), the determinant identity on the line holds exactly; at kappa = 0.1 and 0.3 the two "
          "nodes sit on the line at the closed-form x0 and 1 - x0 with charges +-1 and reverse with kappa; at kappa = 0.6 the six nodes have total charge 0; on " + str(NS) + " slices per axis the Kubo slice Chern number "
          "equals the integer step function fixed by node positions and charges, so the exact averages equal arccos(c)/pi (kappa = 0.1, 0.3) and -sum q f mod 1 (kappa = 0.6) with no two-slice-spacing slack")


if __name__ == "__main__":
    run()
