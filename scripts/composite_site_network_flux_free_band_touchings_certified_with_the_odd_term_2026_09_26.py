#!/usr/bin/env python3
"""Flux-free Majorana bands of the supplied composite-site network with the odd term: a certified search of the whole zone.

Setting (all supplied, none adopted): the colored periodic network of composite sites of the landed note
docs/THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md
(its explicit site and colour rules, reproduced below), bonds J_lam and the three-site odd term kappa in the sign convention of
open PR 9255, in the sector with every bond variable u = +1 (the locally flux-free sector of open PR 9255). In that sector the
model is three identical copies of one free-Majorana hopping problem. The site and colour rules are invariant under the
translations (2,0,0), (0,2,0), (1,1,2), which leave four sites per cell, so the hopping problem reduces to a 4x4 Bloch matrix
H(f) = i M(f) of the fractional momentum f in [0,1)^3. Weyl's inequality bounds every level's change by
lip * |f - f'|_inf with lip = sum over hopping terms of |t| 2 pi |n|_1 (twice that for a term on one site). A cube of half-width h
around f is cleared when the gap between the middle two levels at f exceeds 2 lip h (they cannot meet inside) and, separately,
when every level at f exceeds lip h in size (no level reaches zero inside); uncleared cubes are halved, level after level.

Checks: (1) the Bloch reduction reproduces the real-space levels of the u = +1 hopping matrices of 32-, 64- and 256-site tori;
(2) isotropic J, kappa = 0.3: after the finest level every uncleared cube lies in two groups of small diameter at f and -f,
both certificates leave the same cubes, and spheres around the groups carry Chern numbers -1 and +1 (lowest two bands);
(3) Chern numbers of two-dimensional slices of the zone jump by the enclosed charges; (4) isotropic J: two groups at
kappa = 0.1 and 0.35, six at 0.4, 0.45, 0.6 and 0.7, charges +-1, total 0, the f1 < f2 side always -1; (5) at f = (1/4, 3/4, 1/2) the
characteristic polynomial is (l^2 - 48(1/2 - kappa)^2)(l^2 - 48(1/2 + kappa)^2) exactly; at kappa = 0.5 the off-plane groups
meet there and at its partner with charges -2 and +2; J = (1, 0.8, 0.6), kappa = 0.35: six groups;
(6) kappa = 0: the uncleared count doubles at every halving (as a line of touchings would); J = (1, 1, 2.5), kappa = 0.3: every
cube is cleared (a certified gap); (7) with J_x = J_y = 1, J_z = J, exactly: on the line (x, 1 - x, 0)
the determinant is 16 (J^2 + 4 c^2 kappa^2 - 2c - 4 kappa^2 - 2)^2 with c = cos 2 pi x, and the touching's f3 velocity vanishes at
kappa^2 = J (J + 2) / (4 (4 + 2J - J^2)), c = (J - 2)(J + 1)/(J + 2) (3/20 and -2/3 at J = 1, the 50-digit root of the
velocity determinant); the certificate switches from two groups to six across the predicted point at J_z = 0.5 and 1.5.
Finite certified statements about the supplied bands in one sector; no ground-sector, phase or physical identification.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
import mpmath as mp
import sympy as sp

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
LEV = 8 if DRY else 14


# ---------------------------------------------------------------- 1. the Bloch reduction against real-space levels
def cluster_levels(Ls, J, kappa):
    """Levels of i M for the u = +1 hopping matrix of the torus Ls, built site by site from the network rules."""
    sites = [p for p in itertools.product(range(Ls[0]), range(Ls[1]), range(Ls[2])) if is_site(p)]
    idx = {p: n for n, p in enumerate(sites)}
    M = np.zeros((len(sites), len(sites)))
    for p in sites:
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b = idx[tuple(q[k] % Ls[k] for k in range(3))]
                M[idx[p], b] += 2 * J[AX[flavour(p, q)]]
                M[b, idx[p]] -= 2 * J[AX[flavour(p, q)]]
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                a1 = idx[tuple(nb[l][k] % Ls[k] for k in range(3))]; a2 = idx[tuple(nb[m][k] % Ls[k] for k in range(3))]
                M[a1, a2] += 2 * kappa; M[a2, a1] -= 2 * kappa
    return np.linalg.eigvalsh(1j * M)


def torus_momenta(Ls):
    """Fractional momenta allowed by the torus translations (Lx,0,0) = (Lx/2) a1, (0,Ly,0) = (Ly/2) a2,
    (0,0,Lz) = (Lz/2) a3 - (Lz/4)(a1 + a2)."""
    Lx, Ly, Lz = Ls
    out = []
    for i in range(Lx // 2):
        for j in range(Ly // 2):
            f1, f2 = i / (Lx // 2), j / (Ly // 2)
            for k in range(Lz // 2):
                out.append((f1, f2, (k + (f1 + f2) * Lz / 4) / (Lz / 2)))
    return np.array(out)


SETS = [((1.0, 1.0, 1.0), 0.0), ((1.0, 1.0, 1.0), 0.3), ((1.0, 0.8, 0.6), 0.35)]
rows1, dmax = [], 0.0
for Ls in [(4, 4, 4), (8, 4, 4), (8, 8, 8)]:
    for J, kap in SETS:
        er = np.sort(cluster_levels(Ls, J, kap))
        eb = np.sort(Bloch(J, kap).levels(torus_momenta(Ls)).ravel())
        d = float(np.abs(er - eb).max()) if len(er) == len(eb) else np.inf
        dmax = max(dmax, d)
    rows1.append(f"{Ls[0] * Ls[1] * Ls[2] // 2} sites")
check("the four-site Bloch matrix reproduces the real-space levels of the u = +1 hopping matrices (32-, 64- and 256-site tori; "
      "kappa = 0, 0.3 and anisotropic J = (1, 0.8, 0.6), kappa = 0.35)", dmax < 1e-12,
      f"{', '.join(rows1)}; max level deviation {dmax:.1e}; Lipschitz constants " +
      ", ".join(f"{Bloch(J, k).lip:.1f}" for J, k in SETS) + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 2. the certified search at isotropic J, kappa = 0.3
def analyse(J, kap, levels):
    B = Bloch(J, kap)
    C, h, counts = certify(B, levels=levels)
    Cz, hz, cz = certify_zero(B, levels=levels)
    same = len(C) == len(Cz) and set(map(tuple, np.floor(C / (2 * h)).astype(np.int64))) == set(map(tuple, np.floor(Cz / (2 * hz)).astype(np.int64)))
    info = []
    if 0 < len(C) < 400000:
        for g in clusters(C, h):
            P = C[g]
            d0 = P - P[0]; d0 -= np.rint(d0)
            c = (P[0] + d0.mean(axis=0)) % 1.0
            d = d0 - d0.mean(axis=0)
            diam = float((d.max(axis=0) - d.min(axis=0)).max()) + 2 * h
            ev = B.levels(c[None])[0]
            sph = [sphere_chern(B, c, s, m) for s in (0.01, 0.03) for m in (32, 64)]
            info.append(dict(c=c, n=len(g), diam=diam, ev=ev, ch=[x[0] for x in sph], gmin=min(x[1] for x in sph)))
    return B, h, counts, cz, same, info


def groups_ok(info, dmax):
    if len(info) != 2:
        return False
    ok = all(i["diam"] < dmax for i in info)
    ok &= all(max(abs(x - round(x)) for x in i["ch"]) < 1e-6 and len({round(x) for x in i["ch"]}) == 1 for i in info)
    ok &= {round(info[0]["ch"][0]), round(info[1]["ch"][0])} == {-1, 1}
    s = (info[0]["c"] + info[1]["c"]) % 1.0
    ok &= bool(np.all(np.minimum(s, 1 - s) < 1e-3))                     # the two groups sit at f and -f
    ok &= all(i["gmin"] > 1e-3 for i in info)
    return ok


def fmt(info):
    return "; ".join(f"group at f = ({i['c'][0]:.5f}, {i['c'][1]:.5f}, {i['c'][2]:.5f}) ({i['n']} cubes, diameter {i['diam']:.1e}): "
                     f"middle levels there {i['ev'][1]:+.1e}, {i['ev'][2]:+.1e}; sphere Chern numbers "
                     + "/".join(f"{x:+.0f}" for x in i["ch"]) + f"; smallest middle gap on the spheres {i['gmin']:.3f}" for i in info)


B3, h3, cnt3, cz3, same3, inf3 = analyse((1.0, 1.0, 1.0), 0.3, LEV)
ok2 = groups_ok(inf3, 1e-3 if not DRY else 5e-2) and same3 and max(cnt3[-4:]) < 1.2 * min(cnt3[-4:])
check("isotropic J, kappa = 0.3: after the finest level every uncleared cube lies in two groups of small diameter at f and -f, "
      "the no-zero-level certificate leaves the same cubes, and spheres around the groups carry Chern numbers -1 and +1 "
      "(radii 0.01 and 0.03, meshes 32 and 64)", ok2,
      f"finest cube half-width {h3:.1e}; uncleared counts per level {cnt3}; same cubes under both certificates: {same3}; " + fmt(inf3)
      + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 3. slice Chern numbers jump by the enclosed charges
rows3, ok3 = [], True
fs = (np.arange(24) + 0.5) / 24
for ax in range(3):
    cs = []
    for f in fs:
        c, gmin = slice_chern(B3, f, m=48, axis=ax)
        ok3 &= abs(c - round(c)) < 1e-6 and gmin > 1e-3
        cs.append(int(round(c)))
    for i in range(len(fs)):
        lo, hi = fs[i], fs[(i + 1) % len(fs)] + (1.0 if i + 1 == len(fs) else 0.0)
        enc = sum(round(g["ch"][0]) for g in inf3 if lo < g["c"][ax] < hi or lo < g["c"][ax] + 1.0 < hi)
        ok3 &= cs[(i + 1) % len(fs)] - cs[i] == enc
    rows3.append(f"along f{ax + 1}: " + "".join("+" if c > 0 else ("-" if c < 0 else "0") for c in cs))
check("isotropic J, kappa = 0.3: Chern numbers of the lowest two bands on 24 slices along each fractional axis are integers "
      "and jump between neighbouring slices by the charge of the groups between them", ok3,
      "; ".join(rows3) + " (slices at (i + 1/2)/24; + = +1, - = -1)" + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 4. the touchings as kappa grows (isotropic J)
def groups_at(J, kap, levels, radius):
    """Uncleared groups after `levels` halvings, with centre, cube count, diameter and sphere Chern number (mesh 32)."""
    B = Bloch(J, kap)
    C, h, counts = certify(B, levels=levels)
    out = []
    for g in clusters(C, h):
        P = C[g]
        d0 = P - P[0]; d0 -= np.rint(d0)
        c = (P[0] + d0.mean(axis=0)) % 1.0
        d = d0 - d0.mean(axis=0)
        q, gmin = sphere_chern(B, c, radius, 32)
        out.append(dict(c=c, n=len(g), diam=float((d.max(axis=0) - d.min(axis=0)).max()) + 2 * h, q=q, gmin=gmin))
    return counts, sorted(out, key=lambda x: tuple(np.round(x["c"], 6)))


def side_charge(out):
    """Total charge of the groups with f1 < f2 (the side of the kappa = 0.3 group at (0.355, 0.645, 0))."""
    return sum(round(o["q"]) for o in out if o["c"][0] < o["c"][1])


rows4, ok4 = [], True
KAPS = [(0.1, 2), (0.35, 2), (0.4, 6), (0.45, 6), (0.6, 6), (0.7, 6)]
for kap, nexp in (KAPS[:2] + KAPS[2:3] if DRY else KAPS):
    cnt, out = groups_at((1.0, 1.0, 1.0), kap, LEV - 3, 0.01)
    good = len(out) == nexp and all(abs(o["q"] - round(o["q"])) < 1e-6 and abs(round(o["q"])) == 1 and o["gmin"] > 1e-3 for o in out)
    good &= sum(round(o["q"]) for o in out) == 0 and side_charge(out) == -1
    ok4 &= good
    rows4.append(f"kappa {kap}: {len(out)} groups " + " ".join(f"({o['c'][0]:.3f},{o['c'][1]:.3f},{o['c'][2]:.3f}){round(o['q']):+d}" for o in out))
check("isotropic J: at kappa = 0.1 and 0.35 the certificate leaves two groups; at kappa = 0.4, 0.45, 0.6 and 0.7 it leaves six "
      "(two on the plane f3 = 0, four off it), each of charge +1 or -1 on spheres of radius 0.01; the total charge is 0 and the groups "
      "with f1 < f2 carry -1 in every case", ok4, "; ".join(rows4) + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 5. the meeting point kappa = 0.5 and an anisotropic case
ks, lam = sp.symbols("kappa lambda")
f0 = [sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(1, 2)]
Ms = sp.zeros(4, 4)
for kind, lst in (("bond", terms((1.0, 1.0, 1.0), 0.0)), ("odd", [x for x in terms((0.0, 0.0, 0.0), 1.0) if x[3] != 0])):
    for (a, b, n, t) in lst:
        ph = sp.exp(2 * sp.pi * sp.I * sum(f0[i] * int(n[i]) for i in range(3)))
        amp = sp.Integer(2) if kind == "bond" else 2 * ks
        Ms[a, b] += amp * ph
        Ms[b, a] -= amp * sp.conjugate(ph)
charpoly = sp.expand((sp.I * Ms - lam * sp.eye(4)).det())
target = sp.expand((lam ** 2 - 48 * (sp.Rational(1, 2) - ks) ** 2) * (lam ** 2 - 48 * (sp.Rational(1, 2) + ks) ** 2))
exact5 = sp.simplify(charpoly - target) == 0
cnt5, out5 = groups_at((1.0, 1.0, 1.0), 0.5, 7 if not DRY else 5, 0.02)
q5 = sorted(round(o["q"]) for o in out5)
dbl = [o for o in out5 if abs(round(o["q"])) == 2]
ok5 = exact5 and q5 == [-2, -1, 1, 2] and all(abs(o["q"] - round(o["q"])) < 1e-6 and o["gmin"] > 1e-4 for o in out5)
ok5 &= all(np.allclose(sorted([o["c"][0] % 1, o["c"][1] % 1]), [0.25, 0.75], atol=2e-3) and abs(o["c"][2] - 0.5) < 2e-3 for o in dbl)
cntA6, outA6 = groups_at((1.0, 0.8, 0.6), 0.35, LEV - 3, 0.01)
ok5 &= len(outA6) == 6 and sum(round(o["q"]) for o in outA6) == 0 and all(abs(round(o["q"])) == 1 for o in outA6)
check("isotropic J: at f = (1/4, 3/4, 1/2) the characteristic polynomial is (l^2 - 48 (1/2 - kappa)^2)(l^2 - 48 (1/2 + kappa)^2) "
      "exactly, so the middle levels meet there at kappa = 1/2; at kappa = 0.5 the four off-plane groups meet in pairs at that point and "
      "its partner, with charges -2 and +2 (spheres of radius 0.02) beside the +1, -1 pair on the plane; J = (1, 0.8, 0.6), kappa = 0.35: "
      "six groups of charge +1 or -1, total 0", ok5,
      f"symbolic identity at (1/4, 3/4, 1/2): {exact5}; kappa 0.5 (7 halvings, counts {cnt5[-3:]}): " + " ".join(f"({o['c'][0]:.4f},{o['c'][1]:.4f},{o['c'][2]:.4f}){o['q']:+.3f} diam {o['diam']:.1e}" for o in out5)
      + f"; J = (1, 0.8, 0.6): " + " ".join(f"({o['c'][0]:.3f},{o['c'][1]:.3f},{o['c'][2]:.3f}){round(o['q']):+d}" for o in outA6)
      + f"; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 6. kappa = 0 and the anisotropic gap
B0 = Bloch((1.0, 1.0, 1.0), 0.0)
C0, h0, cnt0 = certify(B0, levels=9 if not DRY else 6)
ratios = [cnt0[i + 1] / cnt0[i] for i in range(len(cnt0) - 4, len(cnt0) - 1)]
BA = Bloch((1.0, 1.0, 2.5), 0.3)
CA, hA, cntA = certify(BA, levels=LEV)
CzA, hzA, czA = certify_zero(BA, levels=LEV)
grid = (np.arange(48) + 0.5) / 48
minlev = float(np.abs(BA.levels(np.array(list(itertools.product(grid, grid, grid))))).min())
ok5 = all(1.8 < r < 2.2 for r in ratios) and len(CA) == 0 and len(CzA) == 0
check("kappa = 0 (isotropic): the uncleared count doubles at every halving of the cube size, as a line of touchings would "
      "require; J = (1, 1, 2.5), kappa = 0.3: every cube is cleared by both certificates (no touching and no zero level anywhere)",
      ok5, f"kappa = 0 counts {cnt0}, last ratios " + ", ".join(f"{r:.3f}" for r in ratios)
      + f"; J_z = 2.5 counts {cntA} and {czA}; smallest |level| on a 48^3 grid {minlev:.3f}; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 7. where two become six: exact on the line f = (x, 1 - x, 0)
zs, ws, Js, cs, qs = sp.symbols("z w J c q")
Ml = sp.zeros(4, 4)
for p in REPS:
    a, _ = reduce(p)
    if sum(p) % 2 == 0:
        for qn in neighbours(p):
            b, n = reduce(qn)
            amp = Js if flavour(p, qn) == "z" else sp.Integer(1)
            mono = zs ** (n[0] - n[1]) * ws ** n[2]            # f = (x, 1 - x, f3): e^{2 pi i f.n} = z^(n1 - n2) w^n3
            Ml[a, b] += 2 * amp * mono
            Ml[b, a] -= 2 * amp / mono
for (a, b, n, t) in [x for x in terms((0.0, 0.0, 0.0), 1.0) if x[3] != 0]:
    mono = zs ** (int(n[0]) - int(n[1])) * ws ** int(n[2])
    Ml[a, b] += 2 * ks * mono
    Ml[b, a] -= 2 * ks / mono
Dl = sp.expand((sp.I * Ml).det())
D0l = sp.expand(Dl.subs(ws, 1))
D2l = sp.expand((ws * sp.diff(sp.expand(ws * sp.diff(Dl, ws)), ws)).subs(ws, 1))   # -(d/df3)^2 D / (2 pi)^2 at f3 = 0


def cheb(expr):
    """A Laurent polynomial in z that is symmetric under z -> 1/z, written in c = (z + 1/z) / 2."""
    P = sp.Poly(sp.expand(expr * zs ** 8), zs)
    co = {m[0] - 8: v for m, v in zip(P.monoms(), P.coeffs())}
    assert all(sp.expand(co.get(j, 0) - co.get(-j, 0)) == 0 for j in range(1, 9))
    return sp.expand(co.get(0, 0) + sum(co.get(j, 0) * 2 * sp.chebyshevt(j, cs) for j in range(1, 9)))


node = Js ** 2 + 4 * cs ** 2 * ks ** 2 - 2 * cs - 4 * ks ** 2 - 2
P0l, P2l = cheb(D0l), cheb(D2l)
ok_node = sp.expand(P0l - 16 * node ** 2) == 0
qsol = sp.solve(sp.Eq(node.subs(ks, sp.sqrt(qs)), 0), qs)[0]
curv = sp.factor(sp.simplify(P2l.subs(ks, sp.sqrt(qs)).subs(qs, qsol)))
ok_curv = sp.simplify(curv + 64 * ((1 + cs) * (Js + 2) - Js ** 2) ** 2 / (1 + cs)) == 0
c_split = (Js - 2) * (Js + 1) / (Js + 2)
q_split = Js * (Js + 2) / (4 * (4 + 2 * Js - Js ** 2))
ok_split = sp.simplify(node.subs({cs: c_split, ks: sp.sqrt(q_split)})) == 0
ok_iso = q_split.subs(Js, 1) == sp.Rational(3, 20) and c_split.subs(Js, 1) == sp.Rational(-2, 3)

mp.mp.dps = 50
BOND_T = terms((1.0, 1.0, 1.0), 0.0)
ODD_T = [x for x in terms((0.0, 0.0, 0.0), 1.0) if x[3] != 0]


def H_mp(f, kap, deriv=None):
    Mm = mp.zeros(4, 4)
    for lst, amp in ((BOND_T, mp.mpf(2)), (ODD_T, 2 * kap)):
        for (a, b, n, t) in lst:
            ph = mp.expj(2 * mp.pi * sum(f[i] * int(n[i]) for i in range(3)))
            c = (2j * mp.pi * int(n[deriv])) if deriv is not None else 1
            Mm[a, b] += amp * c * ph
            Mm[b, a] -= amp * mp.conj(c * ph)
    return 1j * Mm


def velocity_det(kap, x0=mp.mpf("0.3661")):
    """Determinant of the 3x3 velocity matrix of the touching on the line (projected derivatives on its two zero modes)."""
    x = mp.findroot(lambda x: mp.diff(lambda y: mp.re(mp.det(H_mp([y, 1 - y, 0], kap))), x), x0)
    f = [x, 1 - x, mp.mpf(0)]
    E, U = mp.eigh(H_mp(f, kap))
    order = sorted(range(4), key=lambda i: E[i])
    Uc = mp.matrix(4, 2)
    for r in range(4):
        for ci, cc in enumerate(order[1:3]):
            Uc[r, ci] = U[r, cc]
    pauli = [mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, -1j], [1j, 0]]), mp.matrix([[1, 0], [0, -1]])]
    v = mp.matrix(3, 3)
    for i in range(3):
        P = Uc.H * H_mp(f, kap, deriv=i) * Uc
        for a in range(3):
            v[i, a] = mp.re(sum((P * pauli[a])[j, j] for j in range(2))) / 2
    return mp.det(v), x


d_lo, _ = velocity_det(mp.mpf("0.35"))
d_hi, _ = velocity_det(mp.mpf("0.40"))
kc = mp.findroot(lambda k: velocity_det(k)[0], mp.mpf("0.3873"))
err_k = abs(kc - mp.sqrt(mp.mpf(3) / 20))
rows7 = []
ok_cert = True
for jz in ((1.5,) if DRY else (0.5, 1.5)):
    kcz = float(sp.sqrt(q_split.subs(Js, sp.nsimplify(jz))))
    for kap, nexp in ((round(kcz - 0.02, 3), 2), (round(kcz + 0.03, 3), 6)):
        cnt, out = groups_at((1.0, 1.0, jz), kap, LEV - 4, 0.005)
        ok_cert &= len(out) == nexp and sum(round(o["q"]) for o in out) == 0
        rows7.append(f"J_z {jz}, kappa {kap}: {len(out)} groups")
    rows7[-2] = f"(predicted kappa_c {kcz:.4f}) " + rows7[-2]
ok7 = ok_node and ok_curv and ok_split and ok_iso and d_lo * d_hi < 0 and err_k < mp.mpf(10) ** -40 and ok_cert
check("J_x = J_y = 1, J_z = J: on the line f = (x, 1 - x, 0) the determinant of H is exactly 16 (J^2 + 4 c^2 kappa^2 - 2c - 4 kappa^2 - 2)^2 "
      "(c = cos 2 pi x); on that touching curve its f3 curvature is exactly -64 ((1 + c)(J + 2) - J^2)^2 / (1 + c), so the touching's f3 "
      "velocity vanishes at c = (J - 2)(J + 1)/(J + 2), kappa^2 = J (J + 2) / (4 (4 + 2J - J^2)): 3/20 and -2/3 at J = 1, the 50-digit root "
      "of the velocity determinant; the certificate gives two groups just below and six just above the predicted kappa_c", ok7,
      f"symbolic: determinant {ok_node}, curvature {ok_curv}, split point on the curve {ok_split}, J = 1 values {ok_iso}; det v at 0.35 "
      f"{mp.nstr(d_lo, 5)}, at 0.40 {mp.nstr(d_hi, 5)}, root {mp.nstr(kc, 22)} (|root - sqrt(3/20)| = {mp.nstr(err_k, 2)}); " + "; ".join(rows7)
      + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
