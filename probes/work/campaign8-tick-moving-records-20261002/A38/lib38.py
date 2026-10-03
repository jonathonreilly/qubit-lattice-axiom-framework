"""A38 library: period-2 product textures on Z^3 (one qubit per site), glued covariant laws,
exact flip amplitudes (calm test), one-flip (magnon) Bloch Hamiltonians, plaquette Wilson loops.

Conventions
  - Pauli index 0,1,2 = x,y,z.  Glued turn g (3x3 proper rotation R) acts by  site d -> R d  and
    sigma^a -> sum_b R[b,a] sigma^b  (vector operator).
  - A translation-invariant law is a 'template': dict key = tuple of integer sites (sorted, first site
    at the origin), value = real tensor C of shape (3,)*k; the law is sum_x sum_key C[a..] prod sigma^{a_i}_{x+s_i}.
  - Texture: dict r in {0,1}^3 -> unit vector m(r); m(x) = m(x mod 2).
  - Local frame per site: |m>, |mbar> (orthogonal), e = <mbar|sigma|m>.
"""
import itertools
import numpy as np

PA = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0]).astype(complex)]
CELL = [tuple(c) for c in itertools.product((0, 1), repeat=3)]


def turns():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3), int)
            for r in range(3):
                R[r, perm[r]] = sg[r]
            if round(np.linalg.det(R)) == 1:
                out.append(R)
    return out


TURNS = turns()


def spinors(m):
    m = np.asarray(m, float) / np.linalg.norm(m)
    th = np.arccos(np.clip(m[2], -1, 1)); ph = np.arctan2(m[1], m[0])
    up = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
    dn = np.array([-np.exp(-1j * ph) * np.sin(th / 2), np.cos(th / 2)])
    return up, dn


_BC = {}


def site_B(m):
    """B[a, fout, fin] = <b_fout| sigma^a |b_fin>, b_0 = |m>, b_1 = |mbar>  (memoised)."""
    key = tuple(np.round(np.asarray(m, float), 12))
    if key in _BC:
        return _BC[key]
    _BC[key] = _site_B(m)
    return _BC[key]


def _site_B(m):
    up, dn = spinors(m)
    b = [up, dn]
    B = np.zeros((3, 2, 2), complex)
    for a in range(3):
        for fo in range(2):
            for fi in range(2):
                B[a, fo, fi] = np.vdot(b[fo], PA[a] @ b[fi])
    return B


def canon(sites, C):
    """sort sites, permute tensor axes accordingly, translate first site to origin"""
    order = sorted(range(len(sites)), key=lambda i: tuple(sites[i]))
    s = [tuple(sites[i]) for i in order]
    o = np.array(s[0])
    s = tuple(tuple(int(v) for v in (np.array(x) - o)) for x in s)
    return s, np.transpose(C, order)


def add_term(tpl, sites, C, w=1.0):
    s, Cc = canon(sites, C)
    if s in tpl:
        tpl[s] = tpl[s] + w * Cc
    else:
        tpl[s] = w * Cc.copy()


def rotate_term(R, sites, C):
    k = len(sites)
    s2 = [tuple(R @ np.array(x)) for x in sites]
    C2 = C
    for ax in range(k):          # C'_{..b..} = sum_a R[b,a] C_{..a..}
        C2 = np.moveaxis(np.tensordot(R.astype(float), C2, axes=([1], [ax])), 0, ax)
    return s2, C2


def twirl(sites, C):
    tpl = {}
    for R in TURNS:
        s2, C2 = rotate_term(R, sites, C)
        add_term(tpl, s2, C2)
    return tpl


def tpl_vec(tpls):
    keys = sorted(set(k for t in tpls for k in t))
    rows = []
    for t in tpls:
        v = []
        for k in keys:
            if k in t:
                v.append(t[k].ravel())
            else:
                v.append(np.zeros(3 ** len(k)))
        rows.append(np.concatenate(v))
    return np.array(rows), keys


def covariant_basis(shape_sites, tol=1e-9):
    """basis of glued-covariant, translation-invariant k-body terms (no identities) on the orbit of a shape"""
    k = len(shape_sites)
    seeds = []
    for al in itertools.product(range(3), repeat=k):
        C = np.zeros((3,) * k); C[al] = 1.0
        seeds.append(twirl(shape_sites, C))
    M, keys = tpl_vec(seeds)
    U, S, Vt = np.linalg.svd(M, full_matrices=False)
    r = int(np.sum(S > tol * S[0]))
    basis = []
    for i in range(r):
        v = Vt[i]
        t = {}; pos = 0
        for key in keys:
            n = 3 ** len(key)
            blk = v[pos:pos + n].reshape((3,) * len(key)); pos += n
            if np.max(np.abs(blk)) > 1e-12:
                t[key] = blk
        basis.append(t)
    return basis


def pair_law(J, K, D):
    """J s.s + K s^a s^a + D (s_x cross s_{x+a})_a on every a-bond (x, x+e_a)"""
    t = {}
    for a in range(3):
        C = J * np.eye(3); C[a, a] += K
        b, c = (a + 1) % 3, (a + 2) % 3
        C[b, c] += D; C[c, b] -= D
        e = [0, 0, 0]; e[a] = 1
        add_term(t, [(0, 0, 0), tuple(e)], C)
    return t


def tex_m(tex, x):
    return tex[tuple(int(v) % 2 for v in x)]


def canon_pattern(sites):
    s = sorted(tuple(int(v) for v in x) for x in sites)
    sh = np.array([2 * (v // 2) for v in s[0]])
    return tuple(tuple(int(v) for v in (np.array(x) - sh)) for x in s)


def flip_amplitudes(tex, tpl, override=None, Bcache=None):
    """dict: canonical (mod 2Z^3) set of flipped sites -> amplitude in H|Omega>, nonempty patterns only.
    override: dict absolute site -> direction (e.g. a record's content); then no 2Z^3 canonicalisation."""
    amps = {}
    for x in CELL:
        for key, C in tpl.items():
            S = [tuple(np.array(x) + np.array(s)) for s in key]
            Bs = []
            for y in S:
                m = override[y] if (override is not None and y in override) else tex_m(tex, y)
                Bs.append(site_B(m))
            k = len(S)
            for f in itertools.product((0, 1), repeat=k):
                if sum(f) == 0:
                    continue
                T = C
                for i in range(k):
                    # contract axis 0 (current first remaining Pauli index) with B_i[:, f_i, 0]
                    T = np.tensordot(Bs[i][:, f[i], 0], T, axes=([0], [0]))
                amp = complex(T)
                if abs(amp) < 1e-15:
                    continue
                fl = [S[i] for i in range(k) if f[i]]
                key2 = tuple(sorted(fl)) if override is not None else canon_pattern(fl)
                amps[key2] = amps.get(key2, 0) + amp
    return amps


def calm_matrix(tex, tpls, override=None):
    """real matrix: rows = (pattern, re/im), cols = law templates"""
    dicts = [flip_amplitudes(tex, t, override) for t in tpls]
    keys = sorted(set(k for d in dicts for k in d))
    M = np.zeros((2 * len(keys), len(tpls)))
    for j, d in enumerate(dicts):
        for i, k in enumerate(keys):
            v = d.get(k, 0)
            M[2 * i, j] = v.real; M[2 * i + 1, j] = v.imag
    return M, keys


def null_space(M, tol=1e-10):
    if M.shape[0] == 0:
        return np.eye(M.shape[1])
    U, S, Vt = np.linalg.svd(M)
    Sfull = np.zeros(M.shape[1]); Sfull[:len(S)] = S
    return Vt[Sfull < tol * max(1.0, S[0])].T, Sfull


def combine(tpls, coeffs):
    out = {}
    for t, c in zip(tpls, coeffs):
        if abs(c) < 1e-14:
            continue
        for k, C in t.items():
            out[k] = out.get(k, 0) + c * C
    return out


def onefl_terms(tex, tpl):
    """list of (alpha, beta, dvec, amp): hop of one flip from cell site alpha to site alpha+dvec (sublattice beta);
    alpha==beta,dvec==0 is the diagonal cost (energy relative to the background)."""
    out = []
    cellidx = {c: i for i, c in enumerate(CELL)}
    for x in CELL:
        for key, C in tpl.items():
            S = [tuple(np.array(x) + np.array(s)) for s in key]
            Bs = [site_B(tex_m(tex, y)) for y in S]
            k = len(S)
            base = C
            for l in range(k):
                base = np.tensordot(Bs[l][:, 0, 0], base, axes=([0], [0]))
            E0 = complex(base)
            for i in range(k):
                for j in range(k):
                    T = C
                    for l in range(k):
                        fo = 1 if l == j else 0
                        fi = 1 if l == i else 0
                        T = np.tensordot(Bs[l][:, fo, fi], T, axes=([0], [0]))
                    amp = complex(T)
                    if i == j:
                        amp -= E0
                    if abs(amp) < 1e-15:
                        continue
                    a = cellidx[tuple(v % 2 for v in S[i])]
                    b = cellidx[tuple(v % 2 for v in S[j])]
                    out.append((a, b, np.array(S[j]) - np.array(S[i]), amp, S[i], S[j]))
    return out


def bloch(terms, k):
    H = np.zeros((8, 8), complex)
    for a, b, d, amp, _, _ in terms:
        H[b, a] += amp * np.exp(1j * np.dot(k, d))
    return H


def realspace_hop(terms):
    """dict (x_from, x_to) -> amplitude with x_from in the cell (absolute sites), for building Wilson loops"""
    hop = {}
    for a, b, d, amp, Si, Sj in terms:
        xi = np.array(Si); sh = 2 * (xi // 2)
        key = (tuple(int(v) for v in xi - sh), tuple(int(v) for v in np.array(Sj) - sh))
        hop[key] = hop.get(key, 0) + amp
    return hop


def H1(hop, x, y):
    x = np.array(x); sh = 2 * (x // 2)
    return hop.get((tuple(int(v) for v in x - sh), tuple(int(v) for v in np.array(y) - sh)), 0)


def plaquette_fluxes(hop):
    """Wilson loop phase / pi for every elementary plaquette with lower corner in the cell, orientation a->b"""
    res = []
    for x in CELL:
        for a, b in ((0, 1), (1, 2), (2, 0)):
            ea = np.eye(3, dtype=int)[a]; eb = np.eye(3, dtype=int)[b]
            p = [np.array(x), np.array(x) + ea, np.array(x) + ea + eb, np.array(x) + eb]
            W = 1.0 + 0j
            for i in range(4):
                W *= H1(hop, p[i], p[(i + 1) % 4])
            res.append((x, "xyz"[a] + "xyz"[b], abs(W), np.angle(W) / np.pi if abs(W) > 1e-12 else np.nan))
    return res


def bloch_batch(terms, ks):
    """H(k) for an array of k points (nk,3) -> (nk,8,8), vectorised"""
    agg = {}
    for a, b, d, amp, _, _ in terms:
        key = (a, b, tuple(int(v) for v in d))
        agg[key] = agg.get(key, 0) + amp
    keys = list(agg)
    A = np.array([agg[k] for k in keys]); D = np.array([k[2] for k in keys], float)
    ph = np.exp(1j * (np.asarray(ks) @ D.T)) * A          # nk x ne
    H = np.zeros((len(ks), 8, 8), complex)
    for e, (a, b, _) in enumerate(keys):
        H[:, b, a] += ph[:, e]
    return H
