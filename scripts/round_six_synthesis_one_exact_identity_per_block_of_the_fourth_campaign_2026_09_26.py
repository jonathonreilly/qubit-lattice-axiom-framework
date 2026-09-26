#!/usr/bin/env python3
"""Round-six synthesis: one exact or reference identity per block of the fourth campaign, recomputed in about two minutes.

Blocks (supplied models, none adopted): the composite-site comparator's band note and flux-candidate note (landed), the slice-flux
note (open PR 9300), the charge-hopping projector note (landed). Checks: (1) the four-site Bloch matrix of the u = +1 comparator
reproduces the 32-site torus levels; (2) the characteristic polynomial at f = (1/4, 3/4, 1/2); (3) on the line f = (x, 1 - x, f3) the
identities D = 16 N^2 and C = (w d/dw)^2 D = -64 ((1 + c)(J + 2) - J^2)^2 / (1 + c) on N = 0, and their joint solution
kappa^2 = J (J + 2) / (4 (4 + 2J - J^2)); (4) the zero-determinant root at J = 1; (5) the 32-site flux-free and exception candidates'
projected-comparator energies and the exception repeated onto 64 sites; (6) the Lanczos Ritz reference of the full 2^3 charged torus.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time
from collections import deque

import numba as nb
import numpy as np
import sympy as sp
from scipy.linalg import schur

AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


# ---------------------------------------------------------------- the composite-site network (open PRs 9255, 9277)
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


def cluster(Ls):
    """Multigraph on the torus: bond keys (a, b, R) with a on sublattice A, R the wrap vector from p's image to q's."""
    sites = [p for p in itertools.product(range(Ls[0]), range(Ls[1]), range(Ls[2])) if is_site(p)]
    idx = {p: n for n, p in enumerate(sites)}
    Aset = {n for n, p in enumerate(sites) if sum(p) % 2 == 0}
    bonds = {}
    for p in sites:
        if sum(p) % 2:
            continue
        for q in neighbours(p):
            qf = tuple(q[b] % Ls[b] for b in range(3))
            R = tuple((q[b] - qf[b]) // Ls[b] for b in range(3))
            bonds[(idx[p], idx[qf], R)] = flavour(p, q)
    return sites, idx, Aset, bonds


def key_of(p, q, Ls, idx):
    """Bond key of the infinite-lattice bond p-q."""
    if sum(p) % 2:
        p, q = q, p
    pf = tuple(p[b] % Ls[b] for b in range(3))
    shift = tuple((p[b] - pf[b]) for b in range(3))
    q0 = tuple(q[b] - shift[b] for b in range(3))                 # translate so that p sits in the fundamental domain
    qf = tuple(q0[b] % Ls[b] for b in range(3))
    R = tuple((q0[b] - qf[b]) // Ls[b] for b in range(3))
    return (idx[pf], idx[qf], R)


def ten_loops(Ls, idx, sites):
    """Every 10-cycle of the infinite graph with a vertex in the fundamental domain, as a frozenset of bond keys (deduplicated)."""
    out = set()
    for p0 in sites:
        stack = [(p0, [p0])]
        while stack:
            v, path = stack.pop()
            if len(path) == 11:
                continue
            for w in neighbours(v):
                if w == p0 and len(path) == 10:
                    cyc = path + [p0]
                    out.add(frozenset(key_of(cyc[i], cyc[i + 1], Ls, idx) for i in range(10)))
                elif w not in path and len(path) < 10:
                    stack.append((w, path + [w]))
    return [l for l in out if len(l) == 10]


def spanning_tree(n, bonds):
    adj = {i: [] for i in range(n)}
    for k in bonds:
        a, b, R = k
        adj[a].append((b, k)); adj[b].append((a, k))
    seen, tree, q = {0}, set(), deque([0])
    while q:
        v = q.popleft()
        for w, k in adj[v]:
            if w not in seen:
                seen.add(w); q.append(w); tree.add(k)
    return tree


def matrix(n, Aset, bonds, u, J, kappa, sites, Ls, idx):
    M = np.zeros((n, n))
    for k, fl in bonds.items():
        a, b, R = k
        M[a, b] += 2 * J[AX[fl]] * u[k]
        M[b, a] -= 2 * J[AX[fl]] * u[k]
    if kappa:
        for p in sites:
            nb = {flavour(p, q): q for q in neighbours(p)}
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                q1, q2 = nb[l], nb[m]
                g = u[key_of(p, q1, Ls, idx)] * u[key_of(p, q2, Ls, idx)]
                a1 = idx[tuple(q1[b] % Ls[b] for b in range(3))]; a2 = idx[tuple(q2[b] % Ls[b] for b in range(3))]
                M[a1, a2] += 2 * kappa * g
                M[a2, a1] -= 2 * kappa * g
    return M


def energy(M):
    ev = np.linalg.eigvalsh(1j * M)
    return -1.5 * ev[ev > 0].sum()


def windings(n, bonds, tree, sites, Ls):
    """Fundamental cycles of the cotree bonds with nonzero total wrap: their bond lists and wrap vectors."""
    adj = {i: [] for i in range(n)}
    for k in tree:
        a, b, R = k
        adj[a].append((b, k, R)); adj[b].append((a, k, tuple(-r for r in R)))
    parent = {0: None}; wrap = {0: (0, 0, 0)}; q = deque([0])
    while q:
        v = q.popleft()
        for w, k, R in adj[v]:
            if w not in parent:
                parent[w] = (v, k); wrap[w] = tuple(wrap[v][i] + R[i] for i in range(3)); q.append(w)
    def path_to_root(v):
        ks = []
        while parent[v] is not None:
            v0, k = parent[v]; ks.append(k); v = v0
        return ks
    out = []
    for k in bonds:
        if k in tree:
            continue
        a, b, R = k
        tot = tuple(wrap[a][i] + R[i] - wrap[b][i] for i in range(3))
        if any(tot):
            ks = set(path_to_root(a)) ^ set(path_to_root(b))
            out.append((ks | {k}, tot))
    return out




def schur_det(M):
    """det of the orthogonal Q with Q^T M Q = blocks [[0, e],[-e, 0]], e > 0, and the smallest level e."""
    T, Z = schur(M, output="real")
    Z = Z.copy(); m = M.shape[0]; eps = []
    i = 0
    while i < m:
        if i + 1 < m and abs(T[i + 1, i]) > 1e-12:
            e = T[i, i + 1]
            if e < 0:
                Z[:, [i, i + 1]] = Z[:, [i + 1, i]]
                e = -e
            eps.append(e); i += 2
        else:
            eps.append(0.0); i += 1
    return float(np.linalg.det(Z)), float(min(eps))


def perm_sign(seq):
    seq = list(seq); sgn = 1
    for i in range(len(seq)):
        while seq[i] != i:
            j = seq[i]; seq[i], seq[j] = seq[j], seq[i]; sgn = -sgn
    return sgn


def parity_sign(n, bonds):
    """Reordering sign taking the site-ordered product of all 6N Majoranas (b^x b^y b^z c^x c^y c^z per site) to the bond-paired b's
    followed by the flavour-grouped c's."""
    target = []
    for (a, b, R), lam in bonds.items():
        target += [6 * a + AX[lam], 6 * b + AX[lam]]
    for al in range(3):
        target += [6 * i + 3 + al for i in range(n)]
    return perm_sign(target)


def physical_energy(M, n, bonds, u, psign):
    """Lowest energy of the sector's physical states: the free ground energy, plus the lowest level when the product of the local
    constraints is -1 on the free ground state (validated against exact diagonalization in check 2)."""
    ev = np.linalg.eigvalsh(1j * M)
    Ef = -1.5 * ev[ev > 1e-12].sum()
    detQ, emin = schur_det(M)
    if emin < 1e-9:
        return Ef, Ef, emin, 0
    prod_u = int(np.prod([u[k] for k in bonds]))
    v = ((-1j) ** n) * psign * ((-1j) ** len(bonds)) * prod_u * (detQ * (1j) ** (n // 2)) ** 3
    ok = abs(v - 1) < 1e-6
    return Ef + (0.0 if ok else emin), Ef, emin, (1 if ok else -1)


def fluxes(u, loops):
    return np.array([int(np.prod([u[k] for k in l])) for l in loops])


def winding_sectors(bonds, E):
    u0 = {k: 1 for k in bonds}
    cuts = [[k for k in bonds if k[2][d] != 0] for d in range(3)]
    out = []
    for w in range(8):
        u = dict(u0)
        for d in range(3):
            if (w >> d) & 1:
                for k in cuts[d]:
                    u[k] = -u[k]
        out.append((E(u), w, u))
    out.sort(key=lambda x: x[0])
    return out


def anneal(keys, E, u_start, steps, rng):
    u = dict(u_start); e = E(u); best = (e, dict(u))
    for s in range(steps):
        Tm = 0.5 * (0.002 / 0.5) ** (s / max(1, steps - 1))
        k = keys[rng.integers(len(keys))]
        u[k] = -u[k]
        e2 = E(u)
        if e2 <= e or rng.random() < np.exp(-(e2 - e) / Tm):
            e = e2
            if e < best[0]:
                best = (e, dict(u))
        else:
            u[k] = -u[k]
    return best




# ---------------------------------------------------------------- the four-site Bloch reduction (open PR 9273)
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce_site(p):
    """p = rep + n1 (2,0,0) + n2 (0,2,0) + n3 (1,1,2) with rep in the 2x2x2 box; returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    return REPS.index((x - 2 * n1, y - 2 * n2, z)), (n1, n2, n3)


def odd_hops():
    """(a, b, n): the odd-term hop between the two neighbours of a site, colours (x,y), (y,z), (z,x), gauge u = +1."""
    out = []
    for p in REPS:
        nb_ = {flavour(p, q): q for q in neighbours(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce_site(nb_[l]); r2, n2 = reduce_site(nb_[m])
            out.append((r1, r2, tuple(int(v) for v in np.subtract(n2, n1))))
    return out


def bloch_levels(J, kappa, F):
    """Levels of H(f) = i M(f) for the u = +1 sector at the fractional momenta F."""
    F = np.atleast_2d(F)
    Mk = np.zeros((len(F), 4, 4), dtype=complex)
    for p in REPS:
        a, _ = reduce_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce_site(q)
                ph = np.exp(2j * np.pi * F @ np.array(n, dtype=float))
                t = 2 * J[AX[flavour(p, q)]]
                Mk[:, a, b] += t * ph; Mk[:, b, a] -= t * np.conj(ph)
    for (a, b, n) in odd_hops():
        ph = np.exp(2j * np.pi * F @ np.array(n, dtype=float))
        Mk[:, a, b] += 2 * kappa * ph; Mk[:, b, a] -= 2 * kappa * np.conj(ph)
    return np.linalg.eigvalsh(1j * Mk)


# ---------------------------------------------------------------- the ring clause (open PR 9276)
class Ice:
    def __init__(self, L):
        self.L = L
        self.nv, self.nl = L ** 3, 3 * L ** 3
        self.verts = list(itertools.product(range(L), repeat=3))
        self.vid = {v: i for i, v in enumerate(self.verts)}
        self.tail = np.zeros(self.nl, dtype=int)
        self.head = np.zeros(self.nl, dtype=int)
        self.axis = np.zeros(self.nl, dtype=int)
        self.coord = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            for a in range(3):
                w = list(v)
                w[a] = (w[a] + 1) % L
                l = 3 * self.vid[v] + a
                self.tail[l], self.head[l], self.axis[l], self.coord[l] = self.vid[v], self.vid[tuple(w)], a, v[a]
        self.xc = np.array([self.verts[l // 3][0] for l in range(self.nl)])      # x-coordinate of the link's tail vertex
        self.inc = [[] for _ in range(self.nv)]
        for l in range(self.nl):
            self.inc[self.tail[l]].append((l, 1))
            self.inc[self.head[l]].append((l, -1))
        plaq = []
        for v in self.verts:
            for a, b in ((0, 1), (1, 2), (0, 2)):
                va, vb = list(v), list(v)
                va[a] = (va[a] + 1) % L
                vb[b] = (vb[b] + 1) % L
                plaq.append([3 * self.vid[v] + a, 3 * self.vid[tuple(va)] + b, 3 * self.vid[tuple(vb)] + a, 3 * self.vid[v] + b])
        self.plaq = np.array(plaq)
        self.sign = np.tile([1, 1, -1, -1], (len(plaq), 1))
        self.np_ = len(plaq)
        pol = [[] for _ in range(self.nl)]
        for p, links in enumerate(self.plaq):
            for l in links:
                pol[l].append(p)
        self.pol = pol
        width = max(len({q for l in links for q in pol[l]}) for links in self.plaq)
        self.A = np.full((self.np_, width), self.np_, dtype=int)
        self.M = np.zeros((self.np_, width, 4))
        for p, links in enumerate(self.plaq):
            aff = sorted({q for l in links for q in pol[l]})
            self.A[p, :len(aff)] = aff
            for j, q in enumerate(aff):
                for k, l in enumerate(links):
                    for h in np.flatnonzero(self.plaq[q] == l):
                        self.M[p, j, k] += self.sign[q, h]

    def circ(self, sigma):
        c = np.zeros(self.np_ + 1)
        c[:self.np_] = (sigma[self.plaq] * self.sign).sum(axis=1)
        return c

    def deltas(self, sigma, C, P):
        Ca = C[self.A[P]]
        Cn = Ca - 2 * np.einsum("pjk,pk->pj", self.M[P], sigma[self.plaq[P]])
        return Cn, (np.abs(Cn) == 4).sum(axis=1) - (np.abs(Ca) == 4).sum(axis=1)

    def winding_fast(self, sigma):
        return tuple(int(sigma[(self.axis == a) & (self.coord == 0)].sum()) for a in range(3))

    def sector_state(self, quanta=0):
        sigma = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            i = self.vid[v]
            sigma[3 * i] = (-1) ** v[1]
            sigma[3 * i + 1] = (-1) ** v[0]
            sigma[3 * i + 2] = (-1) ** v[0]
        for q in range(quanta):
            for x in range(self.L):
                sigma[3 * self.vid[(x, 1, q)]] *= -1
        return sigma

    def modes(self, ms):
        """Transverse field modes O_b(k e_a) = N^{-1/2} sum over b-links of e^{i k x_a} sigma, b != a, k = 2 pi m / L:
        for each m the six (axis, polarisation) modes."""
        PH = np.zeros((len(ms), 6, self.nl), dtype=complex)
        tail_coord = np.array([self.verts[l // 3] for l in range(self.nl)])       # (nl, 3)
        for j, m in enumerate(ms):
            q = 0
            for a in range(3):
                e = np.exp(1j * 2 * np.pi * m / self.L * tail_coord[:, a]) / np.sqrt(self.nv)
                for b in range(3):
                    if b != a:
                        PH[j, q] = e * (self.axis == b)
                        q += 1
        return PH



# ---------------------------------------------------------------- exact full 2^3 torus: matrix-free Lanczos
@nb.njit(cache=False)
def ex_tables(nl, inc6, incs6, pl, ps):
    n = 1 << nl
    q2 = np.zeros(n, dtype=np.int8)
    fm = np.zeros(n, dtype=np.int32)
    for s in range(n):
        tot = 0
        for v in range(inc6.shape[0]):
            d = 0
            for j in range(6):
                d += incs6[v, j] * (2 * ((s >> inc6[v, j]) & 1) - 1)
            q = d // 2
            tot += q * q
        q2[s] = tot
        m = 0
        for p in range(pl.shape[0]):
            c = 0
            for k in range(4):
                c += ps[p, k] * (2 * ((s >> pl[p, k]) & 1) - 1)
            if c == 4 or c == -4:
                m |= 1 << p
        fm[s] = m
    return q2, fm


@nb.njit(cache=False)
def ex_matvec(x, y, q2, fm, pm, nl, g, t, M):
    for s in range(x.shape[0]):
        acc = M * q2[s] * x[s]
        for l in range(nl):
            acc -= t * x[s ^ (1 << l)]
        m = fm[s]
        p = 0
        while m:
            if m & 1:
                acc -= g * x[s ^ pm[p]]
            m >>= 1
            p += 1
        y[s] = acc


@nb.njit(cache=False)
def ex_axpy(w, v, vprev, a, b):
    for i in range(w.shape[0]):
        w[i] -= a * v[i] + b * vprev[i]


def ex_lanczos(q2, fm, pm, nl, g, t, M, iters=240, seed=1):
    """Three-vector Lanczos from a random start; returns (iterations, lowest Ritz value, change over the last ten steps)."""
    n = 1 << nl
    v = np.random.default_rng(seed).standard_normal(n); v /= np.linalg.norm(v)
    w = np.empty(n); vprev = np.zeros(n)
    al, be = [], []
    b = 0.0
    last = None
    for it in range(iters):
        ex_matvec(v, w, q2, fm, pm, nl, g, t, M)
        a = float(v @ w); al.append(a)
        ex_axpy(w, v, vprev, a, b)
        b = float(np.linalg.norm(w)); be.append(b)
        w /= b
        vprev, v, w = v, w, vprev
        if it >= 10 and it % 10 == 0:
            e0 = float(np.linalg.eigvalsh(np.diag(al) + np.diag(be[:-1], 1) + np.diag(be[:-1], -1))[0])
            if last is not None and abs(e0 - last) < 1e-11:
                return it, e0, abs(e0 - last)
            last = e0
    return iters, last, np.inf




DRY = "--dry" in sys.argv


# ---------------------------------------------------------------- 1. the four-band Bloch reduction (open PR 9273)
def torus_momenta(Ls):
    Lx, Ly, Lz = Ls
    out = []
    for i in range(Lx // 2):
        for j in range(Ly // 2):
            f1, f2 = i / (Lx // 2), j / (Ly // 2)
            for k in range(Lz // 2):
                out.append((f1, f2, (k + (f1 + f2) * Lz / 4) / (Lz / 2)))
    return np.array(out)


sites32, idx32, Aset32, bonds32 = cluster((4, 4, 4))
u1 = {k: 1 for k in bonds32}
er = np.sort(np.linalg.eigvalsh(1j * matrix(len(sites32), Aset32, bonds32, u1, (1.0, 1.0, 1.0), 0.3, sites32, (4, 4, 4), idx32)))
eb = np.sort(bloch_levels((1.0, 1.0, 1.0), 0.3, torus_momenta((4, 4, 4))).ravel())
d1 = float(np.abs(er - eb).max())
check("the four-site Bloch matrix of the u = +1 comparator reproduces the 32-site torus levels at kappa = 0.3 (landed band note)", d1 < 1e-12,
      f"{len(er)} levels, max deviation {d1:.1e}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2./3. the exact identities of open PR 9273
ks, lam, zs, ws, Js, cs, qs = sp.symbols("kappa lambda z w J c q")


def bloch_symbolic(Jz, f=None):
    """i M as a symbolic 4x4 matrix: with f = None, on the line f = (x, 1 - x, f3) in z = e^{2 pi i x}, w = e^{2 pi i f3};
    otherwise at the rational momentum f."""
    Mm = sp.zeros(4, 4)
    for p in REPS:
        a, _ = reduce_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce_site(q)
                amp = Jz if flavour(p, q) == "z" else sp.Integer(1)
                mono = zs ** (n[0] - n[1]) * ws ** n[2] if f is None else sp.exp(2 * sp.pi * sp.I * sum(f[i] * n[i] for i in range(3)))
                Mm[a, b] += 2 * amp * mono; Mm[b, a] -= 2 * amp / mono
    for (a, b, n) in odd_hops():
        mono = zs ** (n[0] - n[1]) * ws ** n[2] if f is None else sp.exp(2 * sp.pi * sp.I * sum(f[i] * n[i] for i in range(3)))
        Mm[a, b] += 2 * ks * mono; Mm[b, a] -= 2 * ks / mono
    return sp.I * Mm


cp = sp.expand((bloch_symbolic(sp.Integer(1), [sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(1, 2)]) - lam * sp.eye(4)).det())
ok2 = sp.expand(cp - (lam ** 2 - 48 * (sp.Rational(1, 2) - ks) ** 2) * (lam ** 2 - 48 * (sp.Rational(1, 2) + ks) ** 2)) == 0
check("at f = (1/4, 3/4, 1/2), isotropic J = 1, the characteristic polynomial is (l^2 - 48 (1/2 - kappa)^2)(l^2 - 48 (1/2 + kappa)^2) "
      "(landed band note)", ok2, f"exact: {ok2}; {time.time() - T0:.0f} s")

Dl = sp.expand(bloch_symbolic(Js).det())
D0l = sp.expand(Dl.subs(ws, 1))
D2l = sp.expand((ws * sp.diff(sp.expand(ws * sp.diff(Dl, ws)), ws)).subs(ws, 1))


def cheb(expr):
    P = sp.Poly(sp.expand(expr * zs ** 8), zs)
    co = {m[0] - 8: v for m, v in zip(P.monoms(), P.coeffs())}
    return sp.expand(co.get(0, 0) + sum(co.get(j, 0) * 2 * sp.chebyshevt(j, cs) for j in range(1, 9)))


node = Js ** 2 + 4 * cs ** 2 * ks ** 2 - 2 * cs - 4 * ks ** 2 - 2
okA = sp.expand(cheb(D0l) - 16 * node ** 2) == 0
qsol = sp.solve(sp.Eq(node.subs(ks, sp.sqrt(qs)), 0), qs)[0]
okB = sp.simplify(sp.factor(sp.simplify(cheb(D2l).subs(ks, sp.sqrt(qs)).subs(qs, qsol))) + 64 * ((1 + cs) * (Js + 2) - Js ** 2) ** 2 / (1 + cs)) == 0
qsplit = Js * (Js + 2) / (4 * (4 + 2 * Js - Js ** 2))
okC = qsplit.subs(Js, 1) == sp.Rational(3, 20)
check("on the line f = (x, 1 - x, f3) with J_x = J_y = 1, J_z = J: at w = 1, D = det H = 16 N^2 with N = J^2 + 4 c^2 kappa^2 - 2c - 4 kappa^2 - 2; "
      "on N = 0, C = (w d/dw)^2 D at w = 1 = -64 ((1 + c)(J + 2) - J^2)^2 / (1 + c), and C = N = 0 gives kappa^2 = J (J + 2) / (4 (4 + 2J - J^2)), "
      "3/20 at J = 1 (landed composite-network band note)", okA and okB and okC, f"D identity {okA}, C identity {okB}, J = 1 value {okC}; {time.time() - T0:.0f} s")

c_root = -(1 + 4 * ks ** 2) / (1 + sp.sqrt(1 + 4 * ks ** 2 + 16 * ks ** 4))
ok4r = sp.simplify(node.subs({Js: 1, cs: c_root})) == 0 and sp.limit(c_root, ks, 0) == sp.Rational(-1, 2)
check("at J = 1 the root of N = 0 in (-1, 1) is c = -(1 + 4 kappa^2) / (1 + (1 + 4 kappa^2 + 16 kappa^4)^(1/2)), tending to -1/2 (open PR 9300)",
      ok4r, f"exact: {ok4r}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 5. the 32-site candidates and the repetition (landed flux-candidate note)
EXC_BITS = 28582                      # the exception candidate, found by a sweep of every cotree assignment
tree = spanning_tree(len(sites32), bonds32)
cotree = [k for k in bonds32 if k not in tree]
uex = {k: 1 for k in bonds32}
for i, k in enumerate(cotree):
    if (EXC_BITS >> i) & 1:
        uex[k] = -1
psg32 = parity_sign(len(sites32), bonds32)
Mff = matrix(len(sites32), Aset32, bonds32, u1, (1.0, 1.0, 1.0), 0.3, sites32, (4, 4, 4), idx32)
E_ff = min(physical_energy(matrix(len(sites32), Aset32, bonds32, uw, (1.0, 1.0, 1.0), 0.3, sites32, (4, 4, 4), idx32), len(sites32), bonds32, uw, psg32)[0]
           for _, _, uw in winding_sectors(bonds32, lambda u: energy(matrix(len(sites32), Aset32, bonds32, u, (1.0, 1.0, 1.0), 0.3, sites32, (4, 4, 4), idx32))))
E_ex = physical_energy(matrix(len(sites32), Aset32, bonds32, uex, (1.0, 1.0, 1.0), 0.3, sites32, (4, 4, 4), idx32), len(sites32), bonds32, uex, psg32)[0]
loops32 = ten_loops((4, 4, 4), idx32, sites32)
nfl = int((fluxes(uex, loops32) == -1).sum())
sites64, idx64, Aset64, bonds64 = cluster((8, 4, 4))
psg64 = parity_sign(len(sites64), bonds64)
E64 = lambda u: energy(matrix(len(sites64), Aset64, bonds64, u, (1.0, 1.0, 1.0), 0.3, sites64, (8, 4, 4), idx64))
ff64 = min(physical_energy(matrix(len(sites64), Aset64, bonds64, uw, (1.0, 1.0, 1.0), 0.3, sites64, (8, 4, 4), idx64), len(sites64), bonds64, uw, psg64)[0]
           for _, _, uw in winding_sectors(bonds64, E64))
ut = {}
for p in sites64:
    if sum(p) % 2 == 0:
        for q in neighbours(p):
            ut[key_of(p, q, (8, 4, 4), idx64)] = uex[key_of(p, q, (4, 4, 4), idx32)]
cuts = [[k for k in bonds64 if k[2][d] != 0] for d in range(3)]
rep = np.inf
for w in range(8):
    u2 = dict(ut)
    for d in range(3):
        if (w >> d) & 1:
            for k in cuts[d]:
                u2[k] = -u2[k]
    rep = min(rep, physical_energy(matrix(len(sites64), Aset64, bonds64, u2, (1.0, 1.0, 1.0), 0.3, sites64, (8, 4, 4), idx64), len(sites64), bonds64, u2, psg64)[0])
ok4 = abs(E_ff - (-84.81708)) < 1e-4 and abs(E_ex - (-85.64104)) < 1e-4 and nfl == 16 and rep > ff64
check("32 sites, kappa = 0.3: the flux-free and exception candidates' projected-comparator energies (-84.81708, -85.64104; 16 of 32 loops "
      "at -1), and the exception pattern repeated onto 64 sites lies above the flux-free energy there (landed flux-candidate note)", ok4,
      f"flux-free {E_ff:.5f}, exception {E_ex:.5f} ({nfl} loops at -1); 64 sites: repeated {rep:.4f} vs flux-free {ff64:.4f} ({rep - ff64:+.4f}); "
      f"{time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 6. the Lanczos Ritz reference of the full 2^3 charged torus (landed projector note)
ice2 = Ice(2)
pm2 = np.array([sum(1 << int(l) for l in ice2.plaq[p]) for p in range(ice2.np_)], dtype=np.int64)
inc6 = np.array([[l for (l, s) in ice2.inc[v]] for v in range(ice2.nv)], dtype=np.int64)
incs6 = np.array([[s for (l, s) in ice2.inc[v]] for v in range(ice2.nv)], dtype=np.int64)
q2tab, fmtab = ex_tables(ice2.nl, inc6, incs6, ice2.plaq.astype(np.int64), ice2.sign.astype(np.int64))
it, e0, de = ex_lanczos(q2tab, fmtab, pm2, ice2.nl, 1.0, 0.35, 2.0)
ok5 = abs(e0 - (-9.631658548)) < 1e-8 and de < 1e-10
check("the full 2^3 torus with the single-link term on all 24 links (2^24 states), t = 0.35, M = 2: Lanczos Ritz reference -9.631658548 "
      "(landed projector note)", ok5, f"E0 {e0:.10f} ({it} steps, last change {de:.1e}); {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
