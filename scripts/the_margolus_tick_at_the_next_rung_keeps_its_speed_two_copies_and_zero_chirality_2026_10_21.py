#!/usr/bin/env python3
"""The supplied spin-3/2 Margolus tick (CL-3) read at the next rung: 4^3 cells of 64 one-mode sites.
Zoom = x2 in space and x2 in time (keeps the Margolus causal cone: one block per tick).  Sections:
 1  exact folding: the 64-band rung-1 tick is the direct sum of the 8 fine bands at K = (Q + 2 pi n)/2;
    at Q = 0 the momentum stars split 1+1+3+3 (Gamma, R, X, M); rotation content of the cell;
 2  the composite tick is NOT a rung-1 two-partition Margolus circuit (one tick or two, any alignment);
 3  light-sector flow (Wilsonian: project on the light states, then compose): c invariant, mass doubles,
    cubic anisotropy / 4 per rung; the CL-3 family can follow the flow iff 3c^2 <= (mu_n/2) cot(mu_n/2);
 4  the pi-cone under the exact (stroboscopic) zoom: aliased onto the coarse zone centre; band aliasing;
 5  chirality: zero Berry flux at the rung-1 nodes (the 3-winding vanishes at every rung, proof in note);
 6  copies: fourfold levels persist at every rung; rung 0 cannot hold a single Dirac copy (no E1/2);
 7  a SUPPLIED rung-1 covariant block unitary with exactly one Dirac copy (existence, not a law).
Supplied model, finite diagnostic; no physical identification.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/THE_MARGOLUS_TICK_AT_THE_NEXT_RUNG_KEEPS_ITS_SPEED_TWO_COPIES_AND_ZERO_CHIRALITY_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq, minimize

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

rng = np.random.default_rng(20261021)
C = np.array(list(itertools.product((0, 1), repeat=3)))
ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): ROTS.append(R)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
LIFT = [axang(R) for R in ROTS]
def Dj(j, n, a): J = Jm(j); return expm(-1j * a * sum(n[k] * J[k] for k in range(3)))
XI = []
for i in range(8):
    n = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n[k] * Jm(1.5)[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3)
def Wm(a): return np.cos(a) * W + 1j * np.sin(a) * np.eye(8)
def res(x): return int((np.asarray(x) % 2) @ [4, 2, 1])
def qe(U): return -np.angle(np.linalg.eigvals(U))
def AB(mu, b): return (np.cos(2 * b) + np.cos(mu)) / 2, (np.cos(2 * b) - np.cos(mu)) / 2
def cosw(K, mu, b): A, B = AB(mu, b); return A * np.mean(np.cos(K), axis=-1) - B
def c2_of(mu, b): A, _ = AB(mu, b); return A / 3 * (mu / np.sin(mu) if mu else 1.0)

class Cell:
    """L^3 supercell, Bloch twist Q per period L; fine Margolus tick (2^3 blocks, offsets 0 and 1)."""
    def __init__(self, L):
        self.L = L; self.sites = np.array(list(itertools.product(range(L), repeat=3))); self.N = L ** 3
        self.idx = {tuple(s): i for i, s in enumerate(self.sites)}; self.blocks = {}
        for off in (0, 1):
            bl = []
            for b0 in itertools.product(range(0, L, 2), repeat=3):
                X = np.array(b0) + off + C
                bl.append(([self.idx[tuple(v)] for v in X % L], [res(v) for v in X], np.floor_divide(X, L)))
            self.blocks[off] = bl
    def half(self, off, Wb, Q=np.zeros(3)):
        M = np.zeros((self.N, self.N), complex)
        for ids, rs, wrap in self.blocks[off]:
            ph = np.exp(1j * wrap @ Q); M[np.ix_(ids, ids)] += Wb[np.ix_(rs, rs)] * np.outer(ph.conj(), ph)
        return M
    def tick(self, Q=np.zeros(3), mu=0.0, b=0.0):
        return self.half(1, Wm(mu / 2 - b), Q) @ self.half(0, Wm(mu / 2 + b), Q)
    def rotation(self, R, cen):
        G = np.zeros((self.N, self.N), complex); S = Dj(1.5, *axang(R))
        for i, x in enumerate(self.sites):
            y = np.rint(R @ (x - cen) + cen).astype(int) % self.L
            G[self.idx[tuple(y)], i] = XI[res(y)].conj() @ S @ XI[res(x)]
        return G
c2c, c4c = Cell(2), Cell(4)
CEN = np.full(3, 1.5); L4 = [c4c.rotation(R, CEN) for R in ROTS]
chi = {'E1/2': np.array([np.trace(Dj(.5, n, a)) for n, a in LIFT]), 'G3/2': np.array([np.trace(Dj(1.5, n, a)) for n, a in LIFT])}
chi['E5/2'] = np.array([np.trace(Dj(2.5, n, a)) for n, a in LIFT]) - chi['G3/2']
def content(Ls): cl = np.array([np.trace(L) for L in Ls]); return tuple(int(round((np.conj(chi[k]) @ cl).real / 24)) for k in ('E1/2', 'E5/2', 'G3/2'))

print('== 1. exact folding at the next rung (4^3 cells, 64 modes)')
err = 0
for mu, b in ((0.13, 0.21), (0.0, 0.0), (0.4, 1.1)):
    for Q in rng.uniform(-np.pi, np.pi, (4, 3)):
        big = np.sort(np.angle(np.linalg.eigvals(c4c.tick(Q, mu, b))))
        sm = np.sort(np.concatenate([np.angle(np.linalg.eigvals(c2c.tick((Q + 2 * np.pi * n) / 2, mu, b))) for n in C]))
        cw = np.sort(np.repeat([cosw((Q + 2 * np.pi * n) / 2, mu, b) for n in C], 8))
        err = max(err, abs(big - sm).max(), abs(np.sort(np.cos(big)) - cw).max())
check('64-band rung-1 tick = direct sum of the 8 fine bands at K=(Q+2pi n)/2; all obey cos w = A S(K) - B', err < 1e-12, f'{err:.1e}')
mu, b = 0.13, 0.21; A, B = AB(mu, b)
U0 = c4c.tick(np.zeros(3), mu, b); ev, EV = np.linalg.eig(U0); o = np.abs(-np.angle(ev))
pred = {'Gamma': np.arccos(A - B), 'X(3)': np.arccos(A / 3 - B), 'M(3)': np.arccos(-A / 3 - B), 'R': np.arccos(-A - B)}
dims = {k: int(np.sum(np.isclose(o, v, atol=1e-9))) for k, v in pred.items()}
cont = {}
for k, v in pred.items():
    P = np.linalg.qr(EV[:, np.isclose(o, v, atol=1e-9)])[0]; cont[k] = content([P.conj().T @ L @ P for L in L4])
print('   Q=0 levels |w|:', {k: round(v, 6) for k, v in pred.items()}, 'dims', dims)
check('Q=0 splits 1+1+3+3 stars: Gamma (|w|=mu) 8, X 24, M 24, R (|w|=pi-2b) 8', list(dims.values()) == [8, 24, 24, 8] and np.isclose(pred['R'], np.pi - 2 * b) and np.isclose(pred['Gamma'], mu))
print('   rotation content (E1/2, E5/2, G3/2):', cont, ' whole cell', content(L4), ' rung-0 cube', content([c2c.rotation(R, np.full(3, .5)) for R in ROTS]))
check('cell = 4E1/2+4E5/2+12G3/2; Gamma and R = 2G3/2; X and M = 2E1/2+2E5/2+4G3/2; rung-0 cube = 2G3/2 only',
      content(L4) == (4, 4, 12) and cont['Gamma'] == cont['R'] == (0, 0, 2) and cont['X(3)'] == cont['M(3)'] == (2, 2, 4))
check('the fine tick commutes with the 24 spin-3/2 rotations about the rung-1 cell centre (a fine odd-block centre)', max(np.abs(L @ U0 - U0 @ L).max() for L in L4) < 1e-12)

print('== 2. is the composite a rung-1 Margolus circuit? (8^3 torus, blocks 4^3, partitions offset (2,2,2))')
c8 = Cell(8); U8 = c8.tick(np.zeros(3), 0.13, 0.21); S8 = c8.sites
blk = {}
def inblock(o):
    k = tuple(np.asarray(o) % 8)
    if k not in blk: blk[k] = np.where(np.all(((S8 - np.asarray(o)) % 8) < 4, 1))[0]
    return blk[k]
def split_dims(Uop, oe):
    """U = V_o V_e  <=>  for every even block B, U H_B = sum over the 8 odd blocks B' of (U H_B cap H_B'), dims 8 each."""
    oe = np.array(oe); tot = []
    for B0 in itertools.product((0, 4), repeat=3):
        Sb = np.linalg.qr(Uop[:, inblock(oe + np.array(B0))])[0]; d = 0
        for Bp in itertools.product((-4, 0), repeat=3):
            out = np.setdiff1d(np.arange(c8.N), inblock(oe + 2 + np.array(B0) + np.array(Bp)))
            d += int(np.sum(np.linalg.svd(Sb[out], compute_uv=False) < 1e-9))
        tot.append(d)
    return max(tot)
for name, Uop in (('one fine tick', U8), ('two fine ticks', U8 @ U8)):
    best = max(split_dims(Uop, oe) for oe in itertools.product(range(4), repeat=3))
    check(f'{name}: no alignment of the rung-1 partitions factorises it as V_odd V_even (needs 64 per block)', best < 64, f'best {best}/64')

print('== 3. light-sector flow under the x2 zoom (Wilsonian: light states only, two ticks per rung tick)')
dirs = rng.normal(size=(30, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
for mu, b in ((0.1, 0.3), (0.05, (np.pi - .5) / 2)):
    q = 2e-3; cw2 = []
    for d in dirs[:6]:
        w2 = np.sort(np.abs(qe(np.linalg.matrix_power(c4c.tick(q * d, mu, b), 2))))[:8]
        cw2.append((np.mean(w2) ** 2 - (2 * mu) ** 2) / q ** 2)
    w1 = [(np.sort(np.abs(qe(c2c.tick(q * d, mu, b))))[:8].mean() ** 2 - mu ** 2) / q ** 2 for d in dirs[:6]]
    check(f'mu={mu}, b={b:.3f}: rung-1 light mass = 2 mu and c^2 unchanged = A mu/(3 sin mu) = {c2_of(mu, b):.6f}',
          abs(np.mean(cw2) / c2_of(mu, b) - 1) < 2e-3 and abs(np.mean(w1) / c2_of(mu, b) - 1) < 2e-3, f'rung0 {np.mean(w1):.6f}, rung1 {np.mean(cw2):.6f}')
mu, b = 0.05, 0.4; c2v = c2_of(mu, b)
def aniso(rung, q):
    def w2(d):
        K = q * d / 2 ** rung; w = np.arccos(np.clip(cosw(K, mu, b), -1, 1)); return (2 ** rung * w) ** 2
    return (w2(np.array([1., 0, 0])) - w2(np.ones(3) / np.sqrt(3))) / (-c2v * q ** 4 / 18)
an = [aniso(n, 0.05) for n in range(4)]
check('cubic anisotropy w^2(q x) - w^2(q n111) = -c^2 q^4/(18 * 4^n) at rung n (irrelevant: isotropy emerges)',
      all(abs(a * 1.0 - 4.0 ** -n) < 0.02 * 4.0 ** -n for n, a in enumerate(an)), 'ratios ' + ' '.join(f'{a:.4f}' for a in an))
# family closure
def bnext(mu, b):  # CL-3 member with mass 2mu and the same c
    x = np.cos(2 * b) * np.cos(mu) + np.sin(mu) ** 2; return None if x > 1 + 1e-15 else 0.5 * np.arccos(min(x, 1.0))
ok = True
for mu, b in ((0.1, 0.0), (0.1, 0.049), (0.1, 0.051), (0.1, 0.3), (0.3, 0.9)):
    bn = bnext(mu, b); ok &= (bn is not None) == (2 * b >= mu)
    if bn is not None: ok &= abs(c2_of(2 * mu, bn) / c2_of(mu, b) - 1) < 1e-12
check('a CL-3 member (2mu, b\') with the same c exists iff 2b >= mu; cos 2b\' = cos2b cos mu + sin^2 mu', ok)
c2cl6 = c2_of(1e-9, (np.pi - .5) / 2); mstar = brentq(lambda m: (m / 2) / np.tan(m / 2) - 3 * c2cl6, 0.1, 3.1)
check('rung-n matching needs 3c^2 <= (mu_n/2)cot(mu_n/2): fails at the first rung for b=0; for the CL-6 b it holds up to mu_n = %.4f > pi - 1/2' % mstar,
      bnext(0.01, 0.0) is None and mstar > np.pi - .5)

print('== 4. the pi-cone under the exact (stroboscopic) zoom')
for mu, b in ((0.3, 0.05), (0.05, (np.pi - .5) / 2)):
    o2 = np.abs(qe(np.linalg.matrix_power(c4c.tick(np.zeros(3), mu, b), 2)))
    al = abs(np.angle(np.exp(2j * (np.pi - 2 * b))))
    check(f'mu={mu}, b={b:.3f}: two-tick rung-1 tick at Q=0 has 8 states at |w|={al:.4f} = |2(pi-2b)| mod 2pi (fine R states aliased to the coarse centre)',
          int(np.sum(np.isclose(o2, al, atol=1e-9))) >= 8)
mu, b = 0.3, 0.05; A, B = AB(mu, b); q = 2e-3
dw = [np.sort(np.abs(qe(np.linalg.matrix_power(c4c.tick(q * d, mu, b), 2))))[:8].mean() for d in dirs[:4]]
cD2 = np.mean([(x ** 2 - (4 * b) ** 2) / q ** 2 for x in dw]); pD = A / 3 * (2 * b / np.sin(2 * b))
check('aliased doubler: mass 4b per rung-1 tick, c_D^2 = (A/3)(2b/sin2b) = %.5f vs light c^2 = %.5f (equal only if 2b = mu)' % (pD, c2_of(mu, b)), abs(cD2 / pD - 1) < 2e-3, f'fit {cD2:.5f}')
b = (np.pi - .5) / 2; mu = 0.05; width = np.pi - 2 * b - mu; nstar = int(np.ceil(np.log2(2 * np.pi / width)))
tt = np.linspace(0.5, np.pi * np.sqrt(3), 40001); KK = tt[:, None] * np.ones(3) / np.sqrt(3)
wK = np.arccos(np.clip(cosw(KK, mu, b), -1, 1)); m0 = wK.min(); mn = np.abs(np.angle(np.exp(1j * 2 ** nstar * wK))).min()
check(f'band aliasing: CL-6 b, band [mu, 1/2]; at rung n*={nstar} (U^{2**nstar}) states with |K| >= 0.5 alias to quasi-energy 0', m0 >= mu and mn < 1e-3, f'rung0 min {m0:.3f}, rung {nstar} min {mn:.1e}')

print('== 5. chirality at rung 1')
def flux(Ufun, sel, r=0.02, nt=16, nph=32):
    th_ = np.linspace(0, np.pi, nt + 1); ph_ = np.linspace(0, 2 * np.pi, nph + 1)[:-1]; V = {}
    for i, t in enumerate(th_):
        for k_, p in enumerate(ph_):
            Q = r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)]); w_, v = np.linalg.eig(Ufun(Q)); o_ = -np.angle(w_)
            V[i, k_] = np.linalg.qr(v[:, sel(o_)])[0]
    F = 0
    for i in range(nt):
        for k_ in range(nph):
            a, b2, c2_, d2 = V[i, k_], V[i + 1, k_], V[i + 1, (k_ + 1) % nph], V[i, (k_ + 1) % nph]
            F += np.angle(np.linalg.det(a.conj().T @ b2) * np.linalg.det(b2.conj().T @ c2_) * np.linalg.det(c2_.conj().T @ d2) * np.linalg.det(d2.conj().T @ a))
    return F / (2 * np.pi)
fl = flux(lambda Q: np.linalg.matrix_power(c4c.tick(Q, 0.0, 0.3), 2), lambda o_: (o_ > 0) & (o_ < 0.3))
fd = flux(lambda Q: np.linalg.matrix_power(c4c.tick(Q, 0.4, 0.0), 2), lambda o_: (o_ > 0) & (o_ < 0.3))
check('rung-1 massless light node and aliased massless doubler node: zero Berry flux (not net-chiral)', abs(fl) < 1e-6 and abs(fd) < 1e-6, f'{fl:+.1e}, {fd:+.1e}')

print('== 6. copies')
deg = 0
for Q in rng.uniform(-np.pi, np.pi, (5, 3)):
    o_ = np.sort(qe(np.linalg.matrix_power(c4c.tick(Q, 0.13, 0.21), 2))); deg = max(deg, np.abs(o_.reshape(16, 4) - o_.reshape(16, 4)[:, :1]).max())
check('every rung-1 (two-tick) level is fourfold at generic Q: the two light copies persist at every rung', deg < 1e-9, f'{deg:.1e}')
check('rung 0: the 8-mode cube has no E1/2 or E5/2, so no covariant rung-0 tick has a 2-dim rest level (single Dirac impossible)',
      content([c2c.rotation(R, np.full(3, .5)) for R in ROTS]) == (0, 0, 2))

print('== 7. SUPPLIED rung-1 block unitary with one Dirac copy (existence check, not a law)')
P4 = np.array(list(itertools.product(range(4), repeat=3))); WR = (P4 < 2).astype(float)
def U1many(Qs, W1):
    ph = np.exp(1j * np.atleast_2d(Qs) @ WR.T); return (ph.conj()[:, :, None] * W1[None] * ph[:, None, :]) @ W1[None]
iso = 2 / 24 * sum(np.conj(x) * L for x, L in zip(chi['E1/2'], L4)); e_, V_ = np.linalg.eigh(iso); B8 = V_[:, e_ > .5]
Lr = [B8.conj().T @ L @ B8 for L in L4]; D12 = [Dj(.5, n, a) for n, a in LIFT]
Aint = np.vstack([np.kron(l, np.eye(2)) - np.kron(np.eye(8), d.T) for l, d in zip(Lr, D12)]); _, s_, Vh = np.linalg.svd(Aint)
Xs = [v.conj().reshape(8, 2) for v in Vh[-4:]]; G = np.array([[np.trace(x.conj().T @ y) / 2 for y in Xs] for x in Xs]); gw, gv = np.linalg.eigh(G)
Xs = [B8 @ sum(gv[i, k] * Xs[i] for i in range(4)) / np.sqrt(gw[k]) for k in range(4)]
xz = np.diag((c4c.sites[:, 2] - 1.5) / 4).astype(complex)
lam, E = np.linalg.eigh(np.array([[x[:, 0].conj() @ xz @ y[:, 0] for y in Xs] for x in Xs]))
def copyP(m): q_, _ = np.linalg.qr(sum(m[k] * Xs[k] for k in range(4))); return q_ @ q_.conj().T
Pa, Pb = copyP((E[:, 3] + E[:, 0]) / np.sqrt(2)), copyP((E[:, 3] - E[:, 0]) / np.sqrt(2))
h = np.zeros((64, 64), complex)                      # pi-flux edge hop inside the cell (spin-3/2 overlap phases)
for i, x in enumerate(c4c.sites):
    for j, y in enumerate(c4c.sites):
        if np.sum(abs(x - y)) == 1: g_ = XI[res(x)].conj() @ XI[res(y)]; h[i, j] = -g_ / abs(g_)
Rp = np.eye(64) - Pa - Pb; ALPHA = 0.3
def W1of(m, al=ALPHA): return np.exp(1j * m / 2) * Pa - np.exp(-1j * m / 2) * Pb + Rp @ (1j * expm(1j * al * Rp @ h @ Rp)) @ Rp
W1 = W1of(0.0)
print('   W1 = P_a - P_b + i exp(i 0.3 h_rest) on the rest; P_a, P_b = E1/2 copies (e_max +- e_min)/sqrt2 of the reduced z-position (eigenvalues',
      np.round(lam, 5), '); h = in-cell pi-flux edge hop')
check('W1 unitary and commutes with the 24 rotations about the cell centre', np.allclose(W1 @ W1.conj().T, np.eye(64)) and max(np.abs(L @ W1 - W1 @ L).max() for L in L4) < 1e-12)
ev0, EV0 = np.linalg.eig(U1many(np.zeros(3), W1)[0]); o0 = -np.angle(ev0); P0 = np.linalg.qr(EV0[:, np.abs(o0) < 1e-9])[0]
check('Q=0: exactly 4 states at w=0, carrying E1/2 + E1/2; the other 60 at |w| >= %.3f' % np.sort(np.abs(o0))[4], P0.shape[1] == 4 and np.sort(np.abs(o0))[4] > 1.0
      and content([P0.conj().T @ L @ P0 for L in L4]) == (2, 0, 0))
k = 1e-3; ok = qe(U1many(k * dirs, W1)); ok = np.take_along_axis(ok, np.argsort(np.abs(ok), 1), 1)[:, :4]; c1 = np.abs(ok).mean() / k
check('one isotropic Dirac cone: +-c1|Q|, each twofold, c1 = %.4f rung-1 blocks per tick' % c1, np.ptp(np.abs(ok)) / k < 1e-6 and np.all(np.sum(ok > 0, 1) == 2))
g = np.linspace(-np.pi, np.pi, 9)[:-1]; QG = np.vstack([np.array(list(itertools.product(g, g, g))), np.array(list(itertools.product(g, g, g))) + np.pi / 8])
QG = QG[np.linalg.norm(QG, axis=1) > .5]; oz = np.abs(qe(U1many(QG, W1))).min(1)
f = lambda Q: np.abs(qe(U1many(Q, W1)[0])).min() if np.linalg.norm(np.angle(np.exp(1j * Q))) > 0.3 else 9.0
mn = min(minimize(f, s0, method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-10, maxiter=500)).fun for s0 in QG[np.argsort(oz)[:5]])
c03 = np.abs(qe(U1many(0.3 * dirs, W1))).min(1).min()
check('no other light states: min |w| over |Q| >= 0.3 is the cone itself at |Q| = 0.3', mn >= c03 - 2e-3, f'min {mn:.4f}, cone at 0.3 {c03:.4f}')
QR = rng.uniform(-np.pi, np.pi, (600, 3)); oR = np.sort(np.abs(qe(U1many(QR, W1))), 1); npi = np.mean(np.sum(oR > np.pi - 0.2, 1))
n0 = np.mean(np.sum(np.sort(np.abs(qe(U1many(QR, W1of(0.0, 0.0)))), 1) > np.pi - 0.2, 1))
check('the light band is isolated (5th level >= 1 over the zone) and the in-cell hop removes the flat pile-up at pi (mean states within 0.2 of pi: %.1f, vs %.1f without it)' % (npi, n0),
      oR[:, 4].min() > 1.0 and npi < 3 and n0 > 50)
m = 0.1; q = 0.02; om = np.sort(np.abs(qe(U1many(q * dirs, W1of(m)))), 1)[:, :4]
check('mass: W1(m) = e^{im/2}P_a - e^{-im/2}P_b + i(rest) gives |w| = sqrt(m^2 + c1^2 Q^2) (|Q| = 0.02)', abs(om.mean() / np.sqrt(m ** 2 + c1 ** 2 * q ** 2) - 1) < 1e-3, f'{om.mean():.6f}')
fw = flux(lambda Q: U1many(Q, W1)[0], lambda o_: (o_ > 0) & (o_ < 0.3))
check('zero Berry flux through the upper cone (Dirac, not Weyl)', abs(fw) < 1e-6, f'{fw:+.1e}')
idx8 = {tuple(s): i for i, s in enumerate(S8)}; lab = np.array([int((s % 4) @ [16, 4, 1]) for s in S8])
def layer(off):
    M = np.zeros((512, 512), complex)
    for o_ in itertools.product((0, 4), repeat=3):
        ids = inblock(np.array(o_) + off); M[np.ix_(ids, ids)] = W1[np.ix_(lab[ids], lab[ids])]
    return M
UL = layer(2) @ layer(0)
cv = max(np.abs(Gr @ UL - UL @ Gr).max() for R in ROTS for cn in (np.full(3, 1.5), np.full(3, 3.5)) for Gr in [c8.rotation(R, cn)])
check('8^3 lattice: the rung-1 tick commutes with the 24 rotations about both partitions\' block centres', cv < 1e-12, f'{cv:.1e}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
