#!/usr/bin/env python3
"""The composite-site comparator's flux-free bands with the odd term: slice fluxes of the lowest two bands averaged along each axis.

Setting (all supplied, none adopted): the colored periodic network of composite sites of the landed note
docs/THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md
(site and colour rules reproduced below), bonds J_x = J_y = 1, J_z = J and the three-site odd term kappa in the fixed hopping-sign
convention of the landed notes, in the supplied u = +1 quadratic Majorana comparator (one copy), through the landed four-band Bloch
reduction. Equality to the named spin Hamiltonian is not established.

Checks: (1) exact: on the line f = (x, 1 - x, 0) the middle levels vanish on the zero-determinant curve
J^2 = 2 (1 + c)(1 + 2 kappa^2 (1 - c)), c = cos 2 pi x; at J = 1 its root in (-1, 1) is c = [1 - (1 + 4 kappa^2 + 16 kappa^4)^(1/2)] /
(4 kappa^2), and the curve passes through c = 1 at J = 2 for every kappa; (2) the numerical zero on the line matches the root (J = 1
and J = 1.5); (3) discrete overlap fluxes of the lowest two bands on 96 slices per fractional axis are integers, and their averages are
(arccos c / pi, -arccos c / pi, 0) within two slice spacings at kappa = 0.1 and 0.3; (4) they reverse with kappa; (5) at kappa = 0.6
(six numerical groups) the averages equal minus the flux-weighted sum of the group positions modulo one. Finite diagnostics: no
certified continuum Chern number, node count, transport coefficient, phase or physical identification. Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


AX = {"x": 0, "y": 1, "z": 2}


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


A_VEC = np.array([[2, 0, 0], [0, 2, 0], [1, 1, 2]])       # rows: primitive translations of the site and colour rules
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce(p):
    """p = rep + n1 a1 + n2 a2 + n3 a3 with rep in the 2x2x2 box; returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1."""
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
                out.append((r1, r2, tuple(np.subtract(n2, n1)), 2.0 * kappa))
    return out


class Bloch:
    def __init__(self, J, kappa):
        self.T = terms(J, kappa)
        self.a = np.array([x[0] for x in self.T]); self.b = np.array([x[1] for x in self.T])
        self.n = np.array([x[2] for x in self.T], dtype=float); self.t = np.array([x[3] for x in self.T])
        # Lipschitz constant of every level in the sup-norm of the fractional momentum (Weyl's inequality, term by term)
        fac = np.where(self.a == self.b, 2.0, 1.0)
        self.lip = float(np.sum(fac * np.abs(self.t) * 2 * np.pi * np.abs(self.n).sum(axis=1)))

    def H(self, F):
        F = np.atleast_2d(F)
        ph = np.exp(2j * np.pi * F @ self.n.T)
        Mk = np.zeros((len(F), 4, 4), dtype=complex)
        for j in range(len(self.T)):
            Mk[:, self.a[j], self.b[j]] += self.t[j] * ph[:, j]
            Mk[:, self.b[j], self.a[j]] -= self.t[j] * np.conj(ph[:, j])
        return 1j * Mk

    def levels(self, F, vecs=False):
        return np.linalg.eigh(self.H(F)) if vecs else np.linalg.eigvalsh(self.H(F))


def certify(B, n0=40, levels=14, chunk=200000):
    """Adaptive cubes over the fractional zone [0,1)^3: a cube of half-width h at centre c is cleared when
    eps3(c) - eps2(c) > 2 lip h (the middle bands cannot meet inside). Returns the uncleared cubes at the finest level,
    the minimum cleared-gap ratio, and the number of evaluations."""
    h = 0.5 / n0
    g = (np.arange(n0) + 0.5) / n0
    C = np.array(list(itertools.product(g, g, g)))
    counts = []
    for lev in range(levels):
        keep = []
        for s in range(0, len(C), chunk):
            ev = B.levels(C[s:s + chunk])
            gap = ev[:, 2] - ev[:, 1]
            keep.append(C[s:s + chunk][gap <= 2 * B.lip * h])
        C = np.concatenate(keep) if keep else np.zeros((0, 3))
        counts.append(len(C))
        if lev == levels - 1 or len(C) == 0:
            break
        off = np.array(list(itertools.product((-0.5, 0.5), repeat=3))) * h
        C = (C[:, None, :] + off[None, :, :]).reshape(-1, 3)
        h /= 2
    return C, h, counts


def clusters(C, h):
    """Connected groups of uncleared cubes (touching or diagonal neighbours, periodic zone), by breadth-first search on the
    integer cube indices of the finest level."""
    n = int(round(0.5 / h))                          # cubes have full width 2h
    ids = np.floor(C / (2 * h)).astype(np.int64) % n
    where = {tuple(x): i for i, x in enumerate(ids)}
    seen = np.zeros(len(C), dtype=bool)
    out = []
    offs = [d for d in itertools.product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]
    for s0 in range(len(C)):
        if seen[s0]:
            continue
        seen[s0] = True
        grp = [s0]; q = [s0]
        while q:
            i = q.pop()
            x = ids[i]
            for d in offs:
                k = where.get(((x[0] + d[0]) % n, (x[1] + d[1]) % n, (x[2] + d[2]) % n))
                if k is not None and not seen[k]:
                    seen[k] = True; grp.append(k); q.append(k)
        out.append(np.array(grp))
    return out


def _link(A_, B_):
    return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))


def _plaquettes(V):
    return np.angle(_link(V[:-1, :-1], V[1:, :-1]) * _link(V[1:, :-1], V[1:, 1:]) * _link(V[1:, 1:], V[:-1, 1:]) * _link(V[:-1, 1:], V[:-1, :-1]))


def sphere_chern(B, c, s, m=48, nocc=2):
    """Chern number of the lowest nocc bands on the sphere |f - c| = s (fractional coordinates, outward orientation), Fukui
    link method on a latitude-longitude grid with shared poles and a periodic seam. Also returns the smallest middle gap met."""
    th = np.linspace(0, np.pi, m + 1)
    ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    P = np.stack([np.sin(th)[:, None] * np.cos(ph)[None, :], np.sin(th)[:, None] * np.sin(ph)[None, :],
                  np.cos(th)[:, None] * np.ones_like(ph)[None, :]], axis=-1) * s + c
    ev, V = B.levels(P.reshape(-1, 3), vecs=True)
    V = V[:, :, :nocc].reshape(m + 1, 2 * m + 1, 4, nocc).copy()
    V[0, :] = V[0, 0]; V[-1, :] = V[-1, 0]; V[:, -1] = V[:, 0]
    return _plaquettes(V).sum() / (2 * np.pi), float((ev[:, 2] - ev[:, 1]).min())


def slice_chern(B, f, m=60, nocc=2, axis=2):
    """Chern number of the lowest nocc bands on the slice (fractional coordinate `axis`) = f, oriented by the cyclic
    order of the two other coordinates; returns (Chern number, smallest middle gap on the slice)."""
    o = [(axis + 1) % 3, (axis + 2) % 3]
    u = np.arange(m + 1) / m
    P = np.zeros((m + 1, m + 1, 3)); P[:, :, o[0]] = u[:, None]; P[:, :, o[1]] = u[None, :]; P[:, :, axis] = f
    ev, V = B.levels(P.reshape(-1, 3), vecs=True)
    V = V[:, :, :nocc].reshape(m + 1, m + 1, 4, nocc).copy()
    V[-1, :] = V[0, :]; V[:, -1] = V[:, 0]
    return _plaquettes(V).sum() / (2 * np.pi), float((ev[:, 2] - ev[:, 1]).min())


def certify_zero(B, n0=40, levels=14, chunk=200000):
    """Adaptive cubes as in certify, clearing a cube when every level at its centre exceeds lip h in size (no level can reach
    zero inside). Returns the uncleared cubes at the finest level, the final half-width and per-level counts."""
    h = 0.5 / n0
    g = (np.arange(n0) + 0.5) / n0
    C = np.array(list(itertools.product(g, g, g)))
    counts = []
    for lev in range(levels):
        keep = []
        for s in range(0, len(C), chunk):
            ev = B.levels(C[s:s + chunk])
            keep.append(C[s:s + chunk][np.abs(ev).min(axis=1) <= B.lip * h])
        C = np.concatenate(keep) if keep else np.zeros((0, 3))
        counts.append(len(C))
        if lev == levels - 1 or len(C) == 0:
            break
        off = np.array(list(itertools.product((-0.5, 0.5), repeat=3))) * h
        C = (C[:, None, :] + off[None, :, :]).reshape(-1, 3)
        h /= 2
    return C, h, counts


DRY = "--dry" in sys.argv
NS = 32 if DRY else 96

# ---------------------------------------------------------------- 1. the closed forms on the zero-determinant line
Js, cs, ks = sp.symbols("J c kappa")
curve = 2 * (1 + cs) * (1 + 2 * ks ** 2 * (1 - cs)) - Js ** 2
c_iso = (1 - sp.sqrt(1 + 4 * ks ** 2 + 16 * ks ** 4)) / (4 * ks ** 2)
ok_iso = sp.simplify(curve.subs({Js: 1, cs: c_iso})) == 0
ok_zone = sp.simplify(curve.subs({Js: 2, cs: 1})) == 0
ok_lim = sp.limit(c_iso, ks, 0) == sp.Rational(-1, 2)
check("exact: at J = 1 the zero-determinant curve J^2 = 2 (1 + c)(1 + 2 kappa^2 (1 - c)) has the root c = [1 - (1 + 4 kappa^2 + 16 kappa^4)^(1/2)] / "
      "(4 kappa^2) (c -> -1/2 as kappa -> 0), and at J = 2 it passes through c = 1, the zone centre, for every kappa",
      ok_iso and ok_zone and ok_lim, f"root {ok_iso}, J = 2 through c = 1 {ok_zone}, kappa -> 0 limit -1/2 {ok_lim}; {time.time() - T0:.0f} s")


def c_closed(J, kap):
    """The root in [-1, 1] of the zero-determinant curve at given J, kappa (numerically, from the quadratic in c)."""
    # 4 kappa^2 c^2 - 2 c (1 - 2 kappa^2 ... ) : expand J^2 = 2 (1 + c) + 4 kappa^2 (1 - c^2)
    a, b, cc = -4 * kap ** 2, 2.0, 2 + 4 * kap ** 2 - J ** 2
    roots = np.roots([a, b, cc])
    return float(min((r.real for r in roots if abs(r.imag) < 1e-12 and -1 - 1e-12 <= r.real <= 1 + 1e-12), key=lambda r: abs(r + 0.5)))


def line_node(B, lo, hi):
    g = lambda x: (lambda e: e[2] - e[1])(B.levels(np.array([[x, 1 - x, 0.0]]))[0])
    return minimize_scalar(g, bounds=(lo, hi), method="bounded", options={"xatol": 1e-14}).x


# ---------------------------------------------------------------- 2. the numerical zero on the line
rows2, ok2, dmax = [], True, 0.0
for J, kap in [(1.0, 0.05), (1.0, 0.1), (1.0, 0.2), (1.0, 0.3), (1.0, 0.35), (1.5, 0.3), (1.5, 0.5)]:
    B = Bloch((1.0, 1.0, J), kap)
    xc = np.arccos(c_closed(J, kap)) / (2 * np.pi)
    xn = line_node(B, xc - 0.02, xc + 0.02)
    dmax = max(dmax, abs(xn - xc))
    rows2.append(f"J {J}, kappa {kap}: x {xn:.8f} (closed {xc:.8f})")
ok2 = dmax < 1e-6
check("the numerical zero of the middle levels on the line matches the closed-form root at J = 1 (kappa 0.05-0.35) and J = 1.5 (kappa 0.3, 0.5)", ok2,
      "; ".join(rows2) + f"; max difference {dmax:.1e}; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 3./4./5. slice-averaged discrete fluxes
def chern_vector(kap):
    B = Bloch((1.0, 1.0, 1.0), kap)
    out, allint, gmin = [], True, np.inf
    for ax in range(3):
        cvals = []
        for i in range(NS):
            c, g = slice_chern(B, (i + 0.5) / NS, m=48, axis=ax)
            allint &= abs(c - round(c)) < 1e-6
            gmin = min(gmin, g)
            cvals.append(round(c))
        out.append(float(np.mean(cvals)))
    return np.array(out), allint, gmin


cv = {}
for kap in (0.1, 0.3, -0.3, 0.6):
    cv[kap] = chern_vector(kap)
rows3, ok3 = [], True
for kap in (0.1, 0.3):
    v, allint, gmin = cv[kap]
    pred = np.arccos(c_closed(1.0, kap)) / np.pi
    good = allint and abs(v[0] - pred) <= 2.0 / NS and abs(v[1] + pred) <= 2.0 / NS and abs(v[2]) < 1e-12
    ok3 &= good
    rows3.append(f"kappa {kap}: ({v[0]:+.4f}, {v[1]:+.4f}, {v[2]:+.4f}) against (+{pred:.4f}, -{pred:.4f}, 0)")
check(f"kappa = 0.1 and 0.3: the discrete overlap fluxes of the lowest two bands on {NS} slices per fractional axis are integers, and their averages "
      "are (arccos(c)/pi, -arccos(c)/pi, 0) within two slice spacings", ok3, "; ".join(rows3) + f"; {time.time() - T0:.0f} s")
v3, v3m = cv[0.3][0], cv[-0.3][0]
ok4 = bool(np.allclose(v3, -v3m, atol=1e-12)) and cv[-0.3][1]
check("the slice-averaged fluxes change sign with kappa (kappa = 0.3 against -0.3)", ok4,
      f"kappa 0.3: ({v3[0]:+.4f}, {v3[1]:+.4f}, {v3[2]:+.4f}); kappa -0.3: ({v3m[0]:+.4f}, {v3m[1]:+.4f}, {v3m[2]:+.4f}); {time.time() - T0:.0f} s")
# six numerical groups: the slice averages against the flux-weighted group positions, -sum_n q_n f_n (mod 1)
B6 = Bloch((1.0, 1.0, 1.0), 0.6)
C6, h6, cnt6 = certify(B6, levels=6 if DRY else 10)
nodes6 = []
for g in clusters(C6, h6):
    P = C6[g]
    d0 = P - P[0]; d0 -= np.rint(d0)
    c = (P[0] + d0.mean(axis=0)) % 1.0
    nodes6.append((c, round(sphere_chern(B6, c, 0.01, 32)[0])))
dip = -sum(q * c for c, q in nodes6)
v6, allint6, g6 = cv[0.6]
dev = [abs(((v6[i] - dip[i]) + 0.5) % 1.0 - 0.5) for i in range(3)]
ok6 = allint6 and len(nodes6) == 6 and all(d <= 2.0 / NS for d in dev)
for kap in (0.1, 0.3):                          # the same rule below the split
    B = Bloch((1.0, 1.0, 1.0), kap)
    x = np.arccos(c_closed(1.0, kap)) / (2 * np.pi)
    dip2 = -(-1 * np.array([x, 1 - x, 0.0]) + 1 * np.array([1 - x, x, 0.0]))
    ok6 &= all(abs(((cv[kap][0][i] - dip2[i]) + 0.5) % 1.0 - 0.5) <= 2.0 / NS for i in range(3))
check("kappa = 0.6 (six numerical groups): the slice fluxes are integers on every slice, and their averages equal minus the flux-weighted sum "
      "of the six numerical group positions modulo one within two slice spacings (the same weighting at kappa = 0.1 and 0.3)", ok6,
      f"averages ({v6[0]:+.4f}, {v6[1]:+.4f}, {v6[2]:+.4f}); -sum q f = ({dip[0]:+.4f}, {dip[1]:+.4f}, {dip[2]:+.4f}) from "
      + ", ".join(f"({c[0]:.3f},{c[1]:.3f},{c[2]:.3f}){q:+d}" for c, q in nodes6) + f"; smallest middle gap on the slices {g6:.3f}; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
