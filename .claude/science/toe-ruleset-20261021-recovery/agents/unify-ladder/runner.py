#!/usr/bin/env python3
"""The rung ladder read as a fifth lattice direction (deconstruction test). Supplied models; finite diagnostics.
 A  the exact corner-preserving split S as the rung operator: isometry, Wold shift, tower spectrum, rung profile, ends
 B  a domain wall along the rung with S as the hop: zero-mode count and the overlap ladder
 C  chirality: product window vs octree (cone) ladder; exact swap circuits; bounded-range index theorem; static
    Wilson-Chern (ring x rung) spectral flow by rung and energy; 3D Wilson-Dirac on the octree over an 8^3 torus
 D  generations: the boundary count is the bulk invariant, not the window; the one integer 3 of the CL-2 phases
 E  against measurement (estimates)
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from math import comb
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

C8 = np.array(list(itertools.product((0, 1), repeat=3)))
def sidx(x, L):
    x = np.asarray(x) % L; return int((x[0] * L + x[1]) * L + x[2])

# ============================================================ A. the exact split as the rung operator
print('== A. corner-preserving split S (coarse 4^3 -> fine 8^3 sites; then 2^3 -> 4^3)')
def split(Lc):
    """coarse site 2n+a -> (1/sqrt8) sum_c fine site 2(2n+c)+a  (each corner mode shared evenly by that corner of the 8 children)"""
    Lf = 2 * Lc; S = np.zeros((Lf ** 3, Lc ** 3))
    for n in itertools.product(range(Lc // 2), repeat=3):
        for a in C8:
            i = sidx(2 * np.array(n) + a, Lc)
            for c in C8: S[sidx(2 * (2 * np.array(n) + c) + a, Lf), i] = 1 / np.sqrt(8)
    return S
def transl(L, d, ax):
    T = np.zeros((L ** 3, L ** 3))
    for x in itertools.product(range(L), repeat=3):
        y = np.array(x); y[ax] += d; T[sidx(y, L), sidx(x, L)] = 1
    return T
S0, S1 = split(4), split(2)
corner = lambda L: np.array([sidx(np.array(x) % 2, 2) for x in itertools.product(range(L), repeat=3)])
cf, cc = corner(8), corner(4)
iso = np.abs(S0.T @ S0 - np.eye(64)).max(); itw = max(np.abs(S0 @ transl(4, 2, ax) - transl(8, 4, ax) @ S0).max() for ax in range(3))
keep = all(np.all(cf[np.nonzero(S0[:, i])[0]] == cc[i]) for i in range(64))
wand = 512 - np.linalg.matrix_rank(S0.T)
check('THEOREM S^T S = 1, S T_coarse(2 sites) = T_fine(4 sites) S, corner label kept: S = (3D Haar refinement of the cell '
      'lattice) x 1_corner', iso < 1e-14 and itw == 0 and keep, f'|S^TS-1| {iso:.0e}; intertwining {itw:.0f}; corners kept {keep}')
N3 = 512 + 64 + 8; T = np.zeros((N3, N3))
T[:512, 512:576] = S0; T[512:576, :512] = S0.T; T[512:576, 576:] = S1; T[576:, 512:576] = S1.T
ev = np.linalg.eigvalsh(T); pred = np.sort(np.concatenate([np.repeat([np.sqrt(2), 0, -np.sqrt(2)], 8), np.repeat([1., -1.], 56), np.zeros(448)]))
check('THEOREM (Wold) S is a pure isometric shift with wandering space ker S^T = 7/8 of the modes (56 per coarse cell); the rung '
      'hop S + S^T on 3 rungs (512+64+8) is a sum of path graphs: {+-sqrt2, 0} x8, {+-1} x56, 0 x448, no level outside (-2, 2)',
      wand == 448 and np.abs(np.sort(ev) - pred).max() < 1e-12 and np.abs(ev).max() < 2,
      f'ker S^T {wand}; max dev {np.abs(np.sort(ev) - pred).max():.0e}; max|eig| {np.abs(ev).max():.4f}')
def pw(L, K, a):
    v = np.zeros(L ** 3, complex)
    for x in itertools.product(range(L // 2), repeat=3): v[sidx(2 * np.array(x) + a, L)] = np.exp(1j * np.dot(K, x))
    return v / np.linalg.norm(v)
P1 = S0 @ S0.T; S01 = S0 @ S1; P2 = S01 @ S01.T; err = 0.0; dc = 0.0
prof = lambda K, n: np.prod([1.0 if abs(np.sin(k / 2)) < 1e-12 else (np.sin(2 ** (n - 1) * k) / (2 ** n * np.sin(k / 2))) ** 2 for k in K])
for m in itertools.product(range(4), repeat=3):
    K = 2 * np.pi * np.array(m) / 4; vs = [pw(8, K, C8[a]) for a in (0, 5)]
    for n, P in ((1, P1), (2, P2)):
        q = [np.vdot(v, P @ v).real for v in vs]; err = max(err, abs(q[0] - prof(K, n))); dc = max(dc, abs(q[0] - q[1]))
check('THEOREM rung profile of a plane wave: |P_{V_n} K|^2 = prod_i [sin(2^(n-1) K_i)/(2^n sin(K_i/2))]^2, the same for every '
      'corner; the partner cone K = pi(1,1,1) has zero weight above rung 0, light states fill the coarse rungs',
      err < 1e-12 and dc < 1e-12 and prof(np.full(3, np.pi), 1) < 1e-30, f'max err {err:.0e}; corner dependence {dc:.0e}')
print('   rung = log2(wavelength): partner cone at the UV end, light states at the IR end; family and mirror copy share a profile')
jm = [next(n for n in range(1, 40) if prof(np.array([np.pi / 2 ** m, 0, 0]), n) < 1e-30) - 1 for m in (1, 3, 6)]
check('THEOREM natural ends: UV = rung 0 (S^T kills the finest details, every Wold chain starts there); IR for momentum K = the rung '
      'where 2^j K_i = pi (the link amplitude prod|cos(2^(j-1) K_i)| vanishes): j_max = log2(pi/|K|)', jm == [1, 3, 6], f'j_max at pi/2, pi/8, pi/64: {jm}')

# ============================================================ B. domain wall along the rung, hop = S
print('== B. domain wall along the rung with the split as the hop (D = A - lam, A = S^T up the tower)')
lam = 0.5; A = np.zeros((N3, N3)); A[512:576, :512] = S0.T; A[576:, 512:576] = S1.T
sv = np.linalg.svd(A - lam * np.eye(N3), compute_uv=False)
chain = lambda l: np.linalg.svd(np.diag(np.ones(l - 1), -1) - lam * np.eye(l), compute_uv=False).min()
lv = [(round(chain(l), 9), sum(np.isclose(sv, chain(l), atol=1e-9))) for l in (3, 2, 1)]
check('THEOREM one near-zero mode per Wold chain (one per rung-0 mode), levels sigma_min(J_l - lam) with multiplicities 8 (chains from '
      'the top cell), 56, 448: the wall binds the wandering space, not one generation (8) or three (24)',
      [c for _, c in lv] == [8, 56, 448], f'lam = {lam}: ' + ', '.join(f'{s} x{c}' for s, c in lv))
rat = [chain(l) / chain(l + 1) for l in range(1, 13)]
check('THEOREM chain masses fall geometrically: sigma(l)/sigma(l+1) -> 1/lam, one ratio for every step', abs(rat[-1] - 1 / lam) < 1e-3,
      'ratios ' + ' '.join(f'{r:.3f}' for r in rat[::3]))

# ============================================================ C. chirality
print('== C. chirality with a rung bulk')
def perm(N, pairs):
    P = np.eye(N); used = set()
    for a, b in pairs:
        assert not ({a, b} & used); used |= {a, b}; P[[a, b]] = P[[b, a]]
    return P
def flow(V, idx, n):
    x0 = n // 2; pos = np.arange(n); d = (pos - x0) % n; near = (d < n // 4) | (d >= n - n // 4)
    R_ = idx[(d < n // 2) & near]; L_ = idx[(d >= n // 2) & near]; P = np.abs(V) ** 2
    return P[np.ix_(R_, L_)].sum() - P[np.ix_(L_, R_)].sum()
L = 32; N2 = 2 * L
U2 = perm(N2, [(L + x, (x + 1) % L) for x in range(L)]) @ perm(N2, [(x, L + x) for x in range(L)])
check('EXACT product window (a full lattice copy per rung): a 2-layer swap circuit gives flow +1 on rung 0 and -1 on rung 1 (the mirror at the far end)',
      abs(flow(U2, np.arange(L), L) - 1) < 1e-12 and abs(flow(U2, np.arange(L, 2 * L), L) + 1) < 1e-12)
def tree(L, top=None):
    sizes = []; n = L
    while n >= 1 and (top is None or len(sizes) <= top): sizes.append(n); n //= 2
    return list(np.cumsum([0] + sizes[:-1])), sizes
def Q(j, off, sizes):
    n1, n0, o0, o1 = sizes[j + 1], sizes[j], off[j], off[j + 1]
    return [[(o1 + p, o0 + 2 * p) for p in range(n1)], [(o1 + p, o0 + 2 * p + 1) for p in range(n1)], [(o1 + p, o0 + (2 * p + 2) % n0) for p in range(n1)]]
def tree_circuit(L, top=None):
    off, sizes = tree(L, top); N = sum(sizes); U = np.eye(N); rngs = {}
    for par in (0, 1):
        lays = [[], [], []]
        for j in range(par, len(sizes) - 1, 2):
            for k, l in enumerate(Q(j, off, sizes)): lays[k] += l
        for l in lays: U = perm(N, l) @ U
    pos = lambda j, p: (p + 0.5) * 2 ** j - 0.5
    for j in range(len(sizes) - 1):
        r = 0
        for l in Q(j, off, sizes):
            for u, v in l:
                d = abs(pos(j + 1, u - off[j + 1]) - pos(j, v - off[j])) % L; r = max(r, min(d, L - d))
        rngs[j] = r
    return U, off, sizes, rngs
U, off, sizes, rngs = tree_circuit(L)
E_ = np.eye(len(U)); E_[:L, :L] = np.roll(np.eye(L), 1, axis=0)
fl = [flow(U, np.arange(off[j], off[j] + s), s) for j, s in enumerate(sizes) if s >= 4]
check('EXACT octree ladder (binary cone over the ring): a depth-6 swap circuit of cell-child gates gives U = Shift on rung 0 x 1 on every '
      'coarser rung: lattice flow +1, no mirror; the 1-site top absorbs it',
      np.array_equal(U, E_) and abs(fl[0] - 1) < 1e-12 and max(abs(f) for f in fl[1:]) < 1e-12,
      f'L = {L}, {len(sizes)} rungs, {len(U)} sites; flows {[int(round(f)) for f in fl]}; gate range by rung {[float(rngs[j]) for j in rngs]} sites (3 2^(j-1), then wraps)')
Ut, offt, szt, _ = tree_circuit(L, top=2)
ft = [flow(Ut, np.arange(offt[j], offt[j] + s), s) for j, s in enumerate(szt)]
check('THEOREM (GNVW on supersites) gates of physical range <= r on any bounded density of ladder modes give total flow 0, so the '
      'mirror stays on an extensive set; e.g. the same circuit stopped at rung 2 (range <= 3 sites): flows +1, 0, -1 on 32, 16, 8 sites',
      [round(f) for f in ft] == [1, 0, -1] and abs(sum(ft)) < 1e-12, f'flows {[int(round(f)) for f in ft]}, total {abs(sum(ft)):.0e}')

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
def chern(L, tree_=True, nr=1, rate=lambda j: 1.0, m0=-1.0, phi=0.0, orient=1.0):
    sizes = [L >> j for j in range(int(np.log2(L)) + 1)] if tree_ else [L] * nr
    off = np.cumsum([0] + sizes[:-1]); H = np.zeros((2 * sum(sizes), 2 * sum(sizes)), complex)
    def blk(i, j, M): H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += M
    for j, n in enumerate(sizes):
        g = rate(j)
        for p in range(n):
            i = off[j] + p; blk(i, i, g * (m0 + 2.0) * sz)
            hop = g * (-0.5j * sx - 0.5 * sz) * (np.exp(1j * phi) if p == n - 1 else 1.0)   # branch-cut gauge: flux at the centre
            blk(i, off[j] + (p + 1) % n, hop); blk(off[j] + (p + 1) % n, i, hop.conj().T)
        if j + 1 < len(sizes):
            h = np.sqrt(rate(j) * rate(j + 1))
            for P in range(sizes[j + 1]):
                kids = [off[j] + 2 * P, off[j] + 2 * P + 1] if tree_ else [off[j] + P]
                for k in kids:
                    M = h / np.sqrt(len(kids)) * (-0.5j * orient * sy - 0.5 * sz); blk(k, off[j + 1] + P, M); blk(off[j + 1] + P, k, M.conj().T)
    return H, sizes, off
def sflow(L, tree_, nr, rate, m0=-1.0, Erefs=(1e-3,), nphi=96, orient=1.0):
    sizes, off = chern(L, tree_, nr, rate, m0, 0.0, orient)[1:]; out = {e: np.zeros(len(sizes), int) for e in Erefs}; prev = None
    for k in range(nphi + 1):
        E, V = np.linalg.eigh(chern(L, tree_, nr, rate, m0, 2 * np.pi * k / nphi, orient)[0])
        if prev is not None:
            E0, V0 = prev; mt = np.argmax(np.abs(V0.conj().T @ V) ** 2, axis=1)
            for e in Erefs:
                for a in np.where(np.abs(E0 - e) < 0.5)[0]:
                    up, dn = E0[a] < e <= E[mt[a]], E[mt[a]] < e <= E0[a]
                    if up or dn:
                        w = [np.sum(np.abs(V[2 * o:2 * (o + s), mt[a]]) ** 2) for o, s in zip(off, sizes)]; out[e][int(np.argmax(w))] += 1 if up else -1
        prev = (E, V)
    return out
fs = sflow(32, False, 3, lambda j: 1.0)[1e-3]; fu = sflow(64, True, 1, lambda j: 1.0, Erefs=(1e-3, 0.1, 0.2))
fz = sflow(64, True, 1, lambda j: 2.0 ** -j, Erefs=(0.05, 0.1, 0.2))
loc = lambda f: [(j, int(v)) for j, v in enumerate(f) if v]
check('DIAGNOSTIC static Wilson-Chern model (ring x rung, Haar split as rung hop): flux-threading spectral flow by rung: strip +1 on rung 0, -1 '
      'on the far rung; octree at the fine rate: -1 always on the 1-site top cell', loc(fs) == [(0, 1), (2, -1)] and all(loc(f) == [(0, 1), (6, -1)] for f in fu.values()),
      f'strip {loc(fs)}; octree uniform {[loc(f) for f in fu.values()]} (E_ref 0.001, 0.1, 0.2)')
check('DIAGNOSTIC octree at zoom-consistent rates (rung j at 2^-j: every rung keeps the fine light speed): the -1 sits on rung log2(E0/E): the mirror is light and '
      'propagating, spread across scales', [loc(f)[-1][0] for f in fz.values()] == [4, 3, 2] and all(loc(f)[0] == (0, 1) for f in fz.values()),
      f'E_ref 0.05, 0.1, 0.2 -> mirror on rungs {[loc(f)[-1][0] for f in fz.values()]}')

s0 = np.eye(2); AL = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, s0)]; BE = np.kron(sz, s0)
def oct3(L0=8, rate=lambda j: 1.0, m0=-1.0):
    sizes = [L0 >> j for j in range(int(np.log2(L0)) + 1)]; off = np.cumsum([0] + [n ** 3 for n in sizes[:-1]])
    R, Cc, Vv = [], [], []
    def add(i, j, M):
        r, c = np.nonzero(M); R.extend(4 * i + r); Cc.extend(4 * j + c); Vv.extend(M[r, c])
    ix = lambda j, x: off[j] + sidx(x, sizes[j])
    for j, n in enumerate(sizes):
        g = rate(j)
        for x in itertools.product(range(n), repeat=3):
            i = ix(j, x); add(i, i, g * (m0 + 4.0) * BE)
            for mu in range(3):
                y = list(x); y[mu] += 1; hop = g * (-0.5j * AL[mu] - 0.5 * BE); add(i, ix(j, y), hop); add(ix(j, y), i, hop.conj().T)
        if j + 1 < len(sizes):
            h = np.sqrt(rate(j) * rate(j + 1))
            for X in itertools.product(range(sizes[j + 1]), repeat=3):
                for c in C8:
                    M = h / np.sqrt(8) * (-0.5j * AL[3] - 0.5 * BE); k = ix(j, 2 * np.array(X) + c); add(k, ix(j + 1, X), M); add(ix(j + 1, X), k, M.conj().T)
    H = sp.csr_matrix((Vv, (R, Cc)), shape=(4 * (off[-1] + 1), 4 * (off[-1] + 1))); H.sum_duplicates(); return H, sizes, off
GB = 1j * AL[3] @ BE
def census(H, sizes, off, k=60):
    """eigsh returns non-orthonormal vectors inside degenerate clusters: orthonormalise each window before taking traces.
    chirality = trace of Gb = i alpha_4 beta (the boundary chirality) on rung 0 and on the top cell"""
    E, V = eigsh(H, k=k, sigma=1e-5, which='LM'); n0 = 4 * sizes[0] ** 3; nt = 4 * off[-1]
    def win(lo, hi):
        s = (np.abs(E) >= lo) & (np.abs(E) < hi)
        if not s.any(): return 0, 0.0, 0.0, 0.0, 0.0
        Q_ = np.linalg.qr(V[:, s])[0]
        g = lambda a, b: float(np.real(np.einsum('sic,ij,sjc->', Q_[a:b].reshape(-1, 4, Q_.shape[1]).conj(), GB, Q_[a:b].reshape(-1, 4, Q_.shape[1]))))
        return int(s.sum()), np.sum(np.abs(Q_[:n0]) ** 2), np.sum(np.abs(Q_[nt:]) ** 2), g(0, n0), g(nt, H.shape[0])
    z, z0, zt, gz0, gzt = win(0, 0.05); sh, sh0, _, gs0, _ = win(0.05, 0.8); lt, lt0, _, _, _ = win(0.05, 0.7)
    return dict(zero=z, z0=z0, ztop=zt, gz0=gz0, gzt=gzt, shell=sh, sh0=sh0, gs0=gs0, light=lt, light0=lt0,
                e1=float(np.round(np.sort(np.abs(E[np.abs(E) > 0.05]))[0], 3)))
cu = census(*oct3()); cz = census(*oct3(rate=lambda j: 2.0 ** -j))
def slab_count(nr=3, L0=8, m0=-1.0):
    z = sh = 0
    for m in itertools.product(range(L0), repeat=3):
        p = 2 * np.pi * np.array(m) / L0; Hk = np.zeros((4 * nr, 4 * nr), complex)
        for j in range(nr):
            Hk[4 * j:4 * j + 4, 4 * j:4 * j + 4] = (m0 + 4.0) * BE + sum(np.sin(p[i]) * AL[i] - np.cos(p[i]) * BE for i in range(3))
            if j + 1 < nr:
                M = -0.5j * AL[3] - 0.5 * BE; Hk[4 * j:4 * j + 4, 4 * j + 4:4 * j + 8] = M; Hk[4 * j + 4:4 * j + 8, 4 * j:4 * j + 4] = M.conj().T
        e = np.abs(np.linalg.eigvalsh(Hk)); z += np.sum(e < 0.05); sh += np.sum((e > 0.05) & (e < 0.8))
    return int(z), int(sh)
sz_, ss_ = slab_count()
check('DIAGNOSTIC 3D Wilson-Dirac (3 space + rung) on the octree over 8^3 (rungs 8^3, 4^3, 2^3, 1; 2340 modes), fine rate: below the bulk gap only '
      'ONE Weyl cone, on rung 0 (2 zero modes + 12 first-shell states, all of boundary chirality -1), plus 2 zero modes of chirality +1 in '
      'the top cell; the 3-rung slab has 4 + 24 (a cone on each wall)',
      cu['zero'] == 4 and abs(cu['z0'] - 2) < 0.05 and abs(cu['ztop'] - 2) < 0.05 and abs(cu['gz0'] + 2) < 0.05 and abs(cu['gzt'] - 2) < 0.05
      and cu['shell'] == 12 and cu['sh0'] > 11 and cu['gs0'] < -11 and (sz_, ss_) == (4, 24),
      f"zero: rung 0 {cu['z0']:.2f} (chirality {cu['gz0']:+.2f}), top {cu['ztop']:.2f} ({cu['gzt']:+.2f}); shell {cu['shell']} at |E| {cu['e1']} "
      f"(rung 0 {cu['sh0']:.2f}, chirality {cu['gs0']:+.2f}); slab {sz_} + {ss_}")
check('DIAGNOSTIC the same octree at zoom-consistent rates: light coarse-rung states fill the gap below the first shell (none at the fine rate)',
      cu['light'] == 0 and cz['light'] - cz['light0'] > 10 and cz['e1'] < 0.3,
      f"states with 0.05 < |E| < 0.7: fine rate {cu['light']}, zoom rate {cz['light']} (rung-0 weight {cz['light0']:.1f}); lowest {cz['e1']}")

# ============================================================ D. generations
print('== D. generations')
cm = {lab: loc(sflow(32, True, 1, lambda j: 1.0, m0=m0, nphi=64, orient=o)[1e-3]) for lab, m0, o in (('m0=-1', -1.0, 1.0), ('m0=-1 reversed', -1.0, -1.0), ('m0=+1', 1.0, 1.0))}
cw = {L_: loc(sflow(L_, True, 1, lambda j: 1.0, nphi=64)[1e-3])[0] for L_ in (16, 32, 64)}
check('DIAGNOSTIC the lattice carries the bulk invariant (+1; -1 with the rung hop reversed; 0 when trivial) for 5, 6, 7 rungs: rungs '
      'never multiply species; three families need a bulk invariant 3',
      [c[0] if c else None for c in cm.values()] == [(0, 1), (0, -1), None] and all(v == (0, 1) for v in cw.values()),
      f'{cm}; rung-0 flow for L = 16, 32, 64: {list(cw.values())}')
def slab_cones(m0, nr=3, L0=8):
    out = []
    for m in itertools.product(range(L0), repeat=3):
        p = 2 * np.pi * np.array(m) / L0; Hk = np.zeros((4 * nr, 4 * nr), complex)
        for j in range(nr):
            Hk[4 * j:4 * j + 4, 4 * j:4 * j + 4] = (m0 + 4.0) * BE + sum(np.sin(p[i]) * AL[i] - np.cos(p[i]) * BE for i in range(3))
            if j + 1 < nr:
                M = -0.5j * AL[3] - 0.5 * BE; Hk[4 * j:4 * j + 4, 4 * j + 4:4 * j + 8] = M; Hk[4 * j + 4:4 * j + 8, 4 * j:4 * j + 4] = M.conj().T
        if np.min(np.abs(np.linalg.eigvalsh(Hk))) < 0.05: out.append(tuple(int(v) for v in m))
    return out
c3 = slab_cones(-3.0)
check('DIAGNOSTIC the window-free 3: the slab\'s C2 = -3 phase (m0 = -3) puts one cone per wall at each of the three X points, a '
      'rotation triplet (the three axes), which covariant masses keep degenerate: colour-type, not three families',
      sorted(c3) == [(0, 0, 4), (0, 4, 0), (4, 0, 0)], f'zero-mode momenta (units 2pi/8) {sorted(c3)}')
def Jm(j):
    d = int(round(2 * j + 1)); mm = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - mm[a] * (mm[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(mm).astype(complex)]
def coh(j, n):
    J = Jm(j); w, v = np.linalg.eigh(sum(n[k] * J[k] for k in range(3))); return v[:, -1]
face = [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
ph = {}
for j in (0.5, 1.5, 2.5, 4.5):
    xi = [coh(j, (2 * np.array(c) - 1) / np.sqrt(3)) for c in face]
    ph[j] = np.angle(np.prod([np.vdot(xi[k], xi[(k + 1) % 4]) for k in range(4)]))
sg = np.sign(ph[0.5]); okp = all(abs(np.exp(1j * ph[j]) - np.exp(1j * sg * j * 2 * np.pi / 3)) < 1e-9 for j in ph) and [j for j in ph if abs(abs(ph[j]) - np.pi) < 1e-9] == [1.5, 4.5]
check('THEOREM spin-j corner phases have face holonomy exp(+-i j 2pi/3); -1 on every face (W a reflection) iff j = 3/2 mod 3, so each cube '
      'encloses Berry charge 2j = 3 mod 6 (whether it can serve as a bulk invariant is open)', okp, 'face phase/pi: ' + ', '.join(f'j={j}: {ph[j] / np.pi:+.3f}' for j in ph))

# ============================================================ E. against measurement
print('== E. against measurement (estimates; inputs: PDG masses, M_P = 1.22089e19 GeV, a = sqrt(8 pi) l_P)')
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
r = np.log(mmu / me) / np.log(mtau / mmu); ru = np.log(1273 / 2.16) / np.log(172570 / 1273); rd = np.log(93.5 / 4.70) / np.log(4183 / 93.5)
check('ESTIMATE one overlap ratio per rung and equally spaced generations force equal log-steps (ratio 1); measured '
      'ln(m_mu/m_e)/ln(m_tau/m_mu) = %.4f, up %.2f, down %.2f (free rung positions fit any ratio by rationals, e.g. 17/9: no rule)' % (r, ru, rd), abs(r - 1) > 0.5 and abs(ru - 1) > 0.2 and abs(rd - 1) > 0.2,
      f'steps {np.log(mmu / me):.4f}, {np.log(mtau / mmu):.4f} = {np.log2(mmu / me):.3f}, {np.log2(mtau / mmu):.3f} rungs of 2')
kmin = 2 * np.pi / 64; sl = np.prod(np.cos(np.array([kmin, 0, 0]) / 2) ** 2)
check('THEOREM the exact split passes light modes unsuppressed (|s|^2 = prod cos^2(K/2) >= 1 - |K|^2/4): it supplies no hierarchy',
      sl > 1 - kmin ** 2 / 4 - 1e-15, f'|s|^2 at the smallest K of a 64-cell torus {sl:.6f}')
mP = 1.22089e19; rung = lambda m: np.log2(1 / (m * 1e-3 / mP * np.sqrt(8 * np.pi)))
check('ESTIMATE windows (rungs from the cell): Compton e %.1f, mu %.1f, tau %.1f; formation horizon >= 15.7, CMB pivot 192.3, Hubble 200.1 '
      '(zoom-tilt); none is 3' % (rung(me), rung(mmu), rung(mtau)), rung(me) > 70 and rung(mtau) > 59)
print('supplied: the split and tower sizes, lam, swap circuits, Wilson-Chern/Dirac models (m0, rates, Haar rung hop, branch-cut flux),')
print('  the rung timing choice, spin-j corner states, measured masses and the cited window numbers.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
