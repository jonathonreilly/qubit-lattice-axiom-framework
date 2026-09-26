#!/usr/bin/env python3
"""Round-five synthesis: one exact identity from each block of the third campaign, recomputed in one runner.

Setting (all supplied, none adopted): the composite-site network of the landed network note in the six-Majorana representation
(open PRs 9255, 9264), and the link-qubit ring clause -g (U + U^dag) at V = 0, g = 1 with the exact vertex Gauss law, with and
without the single-link term -t sigma^x and the charge mass M Q^2 (open PRs 9258, 9263 and the energy-only photon bound of open
PR 9236 that the 20^3 block extends). Every check here is exact linear algebra on small clusters; no Monte Carlo.

Checks: (1) the projection rule of open PR 9255 gives the exact ground energy of the 16-qubit spin model on 8 sites; (2) the
matching bound of open PR 9264 at J_z = 2.5, kappa = 0 on the 256-site cluster: the z-bond part has every singular value 5, the
x- and y-bond parts norm 2, and every level of every winding class is at least 1; (3) the section flux of open PR 9258 on 2^3:
equal on every plane for every ice state and conserved by every plaquette flip, with the exact sector ground energies for one flux
quantum and none; (4) the averaged f-sum of open PR 9236 on the exact 2^3 component, f = 2 u s^2; (5) the averaged f-sum with
the single-link term of open PR 9263 on 2^3 (the term on the six links at one vertex), f = 2 u s^2 + (2t / 3N) sum <sigma^x>,
and the central differences used for <sigma^x> against the exact expectation. Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
from scipy.linalg import schur
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


# ------------------------------------------------------------------------------------------------ the composite-site network
import itertools
import numpy as np
from collections import deque

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


# ------------------------------------------------------------------------------------------------ the ring model
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

def exact_L2(ice, canon):
    B = np.zeros((ice.nv, ice.nl), dtype=np.int64)
    for v in range(ice.nv):
        for (l, s) in ice.inc[v]:
            B[v, l] += s
    bits = np.arange(ice.nl)
    codes = []
    n = 1 << ice.nl
    step = 1 << 18
    for start in range(0, n, step):
        ids = np.arange(start, min(n, start + step), dtype=np.int64)
        sig = (((ids[:, None] >> bits) & 1) * 2 - 1).astype(np.int64)
        ok = np.all(sig @ B.T == 0, axis=1)
        codes.append(ids[ok])
    codes = np.concatenate(codes)
    masks = np.array([sum(1 << int(l) for l in links) for links in ice.plaq], dtype=np.int64)

    def sig_of(code):
        return ((code >> bits) & 1) * 2 - 1

    def flippable(code):
        s = sig_of(code)
        return np.flatnonzero(np.abs((s[ice.plaq] * ice.sign).sum(axis=1)) == 4)

    def code_of(s):
        return int(((s + 1) // 2 * (1 << bits)).sum())

    c0 = code_of(canon)
    comp = {c0: 0}
    order = [c0]
    q = 0
    while q < len(order):
        c = order[q]
        q += 1
        for p in flippable(c):
            c2 = int(c ^ masks[p])
            if c2 not in comp:
                comp[c2] = len(order)
                order.append(c2)
    n_c = len(order)
    rows, cols = [], []
    for c in order:
        for p in flippable(c):
            rows.append(comp[int(c ^ masks[p])])
            cols.append(comp[c])
    H = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n_c, n_c)).tocsr()
    return codes, order, H, sig_of



def triple(ice, k):
    """The cyclic triple of transverse modes: a-links modulated along axis (a + 1) mod 3, so the three modes cover each plaquette
    orientation once. Returns the field pattern sum over the triple of cos(k x_b) and the three mode vectors O = N^-1/2 sum e^{ikx_b} sigma."""
    tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
    b = (ice.axis + 1) % 3
    xb = tail[np.arange(ice.nl), b]
    hv = np.cos(k * xb)
    PH = np.array([np.exp(1j * k * xb) * (ice.axis == a) / np.sqrt(ice.nv) for a in range(3)])
    return hv, PH



# ------------------------------------------------------------------------------------------------ main
# ---------------------------------------------------------------- 1. the projection rule gives the exact ground energy
sites8, idx8, Aset8, bonds8 = cluster((2, 2, 4))
n8 = len(sites8)
psign8 = parity_sign(n8, bonds8)
nq = 2 * n8
dim = 1 << nq
st = np.arange(dim, dtype=np.int64)


def pauli_term(ops):
    xm = zm = 0; ny = 0
    for q, pp in ops:
        if pp in "xy":
            xm |= 1 << q
        if pp in "yz":
            zm |= 1 << q
        if pp == "y":
            ny += 1
    par = np.zeros(dim, dtype=np.int64); t = st & zm
    while np.any(t):
        par ^= t & 1; t = t >> 1
    return st ^ xm, (1j ** ny) * (1 - 2 * par)


tree8 = spanning_tree(n8, bonds8)
cot8 = [k for k in bonds8 if k not in tree8]
rows1, ok1 = [], True
for J in ((1.0, 1.0, 2.5), (0.4, 1.0, 1.6)):
    rr, cc, vv = [], [], []
    for (a, b, R), lam in bonds8.items():
        for al in ("x", "y", "z"):
            r_, v_ = pauli_term([(2 * a, lam), (2 * b, lam), (2 * a + 1, al), (2 * b + 1, al)])
            rr.append(r_); cc.append(st); vv.append(J[AX[lam]] * v_)
    H = coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))), shape=(dim, dim)).tocsr()
    Ex = float(eigsh(H, k=1, which="SA", return_eigenvectors=False)[0])
    phys = []
    for bitsv in range(1 << len(cot8)):
        u = {k: 1 for k in bonds8}
        for i, k in enumerate(cot8):
            if (bitsv >> i) & 1:
                u[k] = -1
        phys.append(physical_energy(matrix(n8, Aset8, bonds8, u, J, 0.0, sites8, (2, 2, 4), idx8), n8, bonds8, u, psign8)[0])
    ok1 &= abs(min(phys) - Ex) < 1e-8
    rows1.append(f"J = {J}: lowest physical energy over the {len(phys)} sectors {min(phys):.8f}, exact ground {Ex:.8f} (difference {abs(min(phys) - Ex):.1e})")
check("open PR 9255, the projection rule: the lowest physical energy it assigns over every sector of the 8-site cluster equals the exact ground "
      "energy of the full 16-qubit spin model", ok1, "; ".join(rows1) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2. the matching bound on the 256-site cluster
Ls = (8, 8, 8)
sites, idx, Aset, bonds = cluster(Ls)
n = len(sites)
J2 = (1.0, 1.0, 2.5)
cuts = [[k for k in bonds if k[2][d] != 0] for d in range(3)]
parts, minlev = {}, []
for w in range(8):
    u = {k: 1 for k in bonds}
    for d in range(3):
        if (w >> d) & 1:
            for k in cuts[d]:
                u[k] = -u[k]
    M = matrix(n, Aset, bonds, u, J2, 0.0, sites, Ls, idx)
    minlev.append(float(np.linalg.svd(M, compute_uv=False).min()))
    for lam in ("x", "y", "z"):
        Jl = tuple(J2[i] if i == AX[lam] else 0.0 for i in range(3))
        sv = np.linalg.svd(matrix(n, Aset, bonds, u, Jl, 0.0, sites, Ls, idx), compute_uv=False)
        parts.setdefault(lam, []).append((float(sv.min()), float(sv.max())))
zmin = min(p[0] for p in parts["z"]); zmax = max(p[1] for p in parts["z"])
xn = max(p[1] for p in parts["x"]); yn = max(p[1] for p in parts["y"])
ok2 = abs(zmin - 5) < 1e-12 and abs(zmax - 5) < 1e-12 and abs(xn - 2) < 1e-12 and abs(yn - 2) < 1e-12 and min(minlev) >= 1 - 1e-12
check("open PR 9264, the matching bound at J_z = 2.5, kappa = 0 on the 256-site cluster: in every winding class of the flux-free sector the "
      "z-bond part has every singular value 5 and the x- and y-bond parts norm 2, so Weyl's inequality puts every level at 1 or above",
      ok2, f"{n} sites; z-part singular values {zmin:.12f} to {zmax:.12f}; x-part norm {xn:.12f}; y-part norm {yn:.12f}; lowest level over the "
      f"eight classes {min(minlev):.12f}; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 3. the section flux on 2^3
ice2 = Ice(2)
canon2 = ice2.sector_state(0)
codes, order, H2, sig_of = exact_L2(ice2, canon2)
bits = np.arange(ice2.nl)
sig_all = ((codes[:, None] >> bits) & 1) * 2 - 1
planes = np.stack([np.stack([sig_all[:, (ice2.axis == a) & (ice2.coord == c)].sum(axis=1) for c in range(ice2.L)], axis=1)
                   for a in range(3)], axis=1)                                     # (state, axis, plane)
equal_planes = bool(np.all(planes == planes[:, :, :1]))
masks2 = np.array([sum(1 << int(l) for l in links) for links in ice2.plaq], dtype=np.int64)
W_of = {int(c): tuple(planes[i, :, 0]) for i, c in enumerate(codes)}
conserved, n_flips = True, 0
for i, c in enumerate(codes):
    s = sig_all[i]
    for p in np.flatnonzero(np.abs((s[ice2.plaq] * ice2.sign).sum(axis=1)) == 4):
        conserved &= W_of[int(c) ^ int(masks2[p])] == W_of[int(c)]
        n_flips += 1


def sector_ground(W):
    sec = codes[[W_of[int(c)] == W for c in codes]]
    pos = {int(c): m for m, c in enumerate(sec)}
    Hs = np.zeros((len(sec), len(sec)))
    for m, c in enumerate(sec):
        sg = ((int(c) >> bits) & 1) * 2 - 1
        for p_ in np.flatnonzero(np.abs((sg[ice2.plaq] * ice2.sign).sum(axis=1)) == 4):
            Hs[pos[int(c) ^ int(masks2[p_])], m] -= 1.0
    return float(np.linalg.eigvalsh(Hs)[0]), len(sec)


E0s, n0 = sector_ground((0, 0, 0))
E1s, n1 = sector_ground((2, 0, 0))
ok3 = equal_planes and conserved and E1s > E0s
check("open PR 9258, the section flux on the 2^3 torus: for every ice state the flux through every plane of an axis is the same, every plaquette "
      "flip conserves it, and the sector with one flux quantum lies above the sector with none",
      ok3, f"{len(codes)} ice states; every plane equal: {equal_planes}; {n_flips} flips, flux conserved: {conserved}; exact sector grounds "
      f"{E0s:.6f} ({n0} states) and {E1s:.6f} ({n1} states); comparator reading L [E(1) - E(0)] / 2 = {ice2.L * (E1s - E0s) / 2:.5f}; "
      f"{time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 4. the averaged f-sum at the pure-ring point on 2^3
Sg = np.array([sig_of(c) for c in order]).astype(float)
hv2, PH2 = triple(ice2, np.pi)
v, V = eigsh(H2, k=1, which="SA")
E0x = float(v[0]); psi = V[:, 0] * np.sign(V[:, 0].sum())
fs = []
for a in range(3):
    rhs = np.real(Sg @ PH2[a]) * psi
    rhs -= psi * (psi @ rhs)
    fs.append(float(rhs @ (H2 @ rhs)) - E0x * float(rhs @ rhs))
f_ex = float(np.mean(fs)); u_ex = -E0x / ice2.np_
ok4 = abs(f_ex - 2 * u_ex * 4.0) < 1e-9
check("open PR 9236 (the bound the 20^3 block extends), the averaged f-sum: on the exact 2^3 component at k = pi the cyclic-triple first moment "
      "equals 2 u s^2 without any symmetry of the state", ok4,
      f"{len(order)} states; E0 {E0x:.6f}; per-mode first moments {', '.join(f'{x:.6f}' for x in fs)}; average {f_ex:.9f}; 2 u s^2 {2 * u_ex * 4:.9f}; "
      f"{time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 5. the f-sum with the single-link term, and the central differences
S2 = [l for (l, sg) in ice2.inc[0]]
masks2l = [int(m) for m in masks2]


def reach(ice, masks, seed, S):
    bits_ = np.arange(ice.nl)
    c0 = int(((seed + 1) // 2 * (1 << bits_)).sum())
    idx_ = {c0: 0}; order_ = [c0]; q = 0
    out = []
    while q < len(order_):
        c = order_[q]; q += 1
        s = ((c >> bits_) & 1) * 2 - 1
        fl = np.flatnonzero(np.abs((s[ice.plaq] * ice.sign).sum(axis=1)) == 4)
        Qv = np.zeros(ice.nv, dtype=int)
        for vv_ in range(ice.nv):
            for (l, sg) in ice.inc[vv_]:
                Qv[vv_] += sg * s[l]
        out.append((fl, int(((Qv // 2) ** 2).sum()), s))
        for p in fl:
            c2 = c ^ masks[p]
            if c2 not in idx_:
                idx_[c2] = len(order_); order_.append(c2)
        for l in S:
            c2 = c ^ (1 << int(l))
            if c2 not in idx_:
                idx_[c2] = len(order_); order_.append(c2)
    return order_, idx_, out


ordq, idxq, propsq = reach(ice2, masks2l, canon2, S2)
nqs = len(ordq)
Sgq = np.array([pp[2] for pp in propsq], dtype=float)
Q2q = np.array([pp[1] for pp in propsq], dtype=float)
rr_, cr_, rt_, ct_ = [], [], [], []
for a_, (fl, q2, s) in enumerate(propsq):
    c = ordq[a_]
    for p in fl:
        rr_.append(idxq[c ^ masks2l[p]]); cr_.append(a_)
    for l in S2:
        rt_.append(idxq[c ^ (1 << int(l))]); ct_.append(a_)
Hring = coo_matrix((-np.ones(len(rr_)), (rr_, cr_)), shape=(nqs, nqs)).tocsr()
Hlink = coo_matrix((-np.ones(len(rt_)), (rt_, ct_)), shape=(nqs, nqs)).tocsr()


def ground(t, Mq):
    Hq = (Hring + t * Hlink + diags(Mq * Q2q)).tocsr()
    w, vec = eigsh(Hq, k=1, which="SA")
    ps = vec[:, 0] * np.sign(vec[:, 0].sum())
    return float(w[0]), ps, Hq


rows5, ok5 = [], True
for (t, Mq) in ((0.8, 1.5), (0.4, 2.0)):
    E0q, ps, Hq = ground(t, Mq)
    uq = -float(ps @ (Hring @ ps)) / ice2.np_
    sxs = -float(ps @ (Hlink @ ps))                       # sum of <sigma^x> over the six links
    fq = []
    for a in range(3):
        rhs = np.real(Sgq @ PH2[a]) * ps
        rhs -= ps * (ps @ rhs)
        fq.append(float(rhs @ (Hq @ rhs)) - E0q * float(rhs @ rhs))
    fpred = 2 * uq * 4.0 + 2 * t * sxs / (3 * ice2.nv)
    dev = abs(float(np.mean(fq)) - fpred)
    ok5 &= dev < 1e-9
    fd = {}
    for d in (0.05, 0.1):
        fd[d] = -(ground(t + d, Mq)[0] - ground(t - d, Mq)[0]) / (2 * d)
    ok5 &= abs(fd[0.05] - sxs) < 0.01 * sxs
    rows5.append(f"t {t}, M {Mq}: averaged first moment {np.mean(fq):.9f}, 2 u s^2 + (2t/3N) sum <sigma^x> {fpred:.9f} (difference {dev:.1e}); "
                 f"sum <sigma^x> {sxs:.6f}, central differences of step 0.05 and 0.1 give {fd[0.05]:.6f} and {fd[0.1]:.6f}")
check(f"open PR 9263, the f-sum with the single-link term on the 2^3 torus ({nqs} states, the term on the six links at one vertex): the "
      "averaged first moment equals 2 u s^2 + (2t / 3N) sum <sigma^x> exactly, and the central differences of the energy that estimate <sigma^x> "
      "agree with its exact value within 1 per cent", ok5, "; ".join(rows5) + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
