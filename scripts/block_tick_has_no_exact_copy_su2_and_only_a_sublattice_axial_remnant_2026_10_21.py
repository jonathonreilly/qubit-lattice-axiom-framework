#!/usr/bin/env python3
"""Internal symmetry of the supplied spin-3/2 Margolus Dirac tick (one fermion mode per site, block unitary
W(mu) = cos(mu/2) W + i sin(mu/2) on even then odd 2^3 blocks).  Checks: (1) the six Clifford generators
Gamma_1..6 hidden in the Bloch tick, and the block-local (K-independent) commutant of U(K): scalars for
mu != 0, span{1, eps} with eps = (-1)^(x+y+z) for mu = 0; (2) the continuum Dirac algebra (beta, alpha_a)
read from the tick, its copy algebra M_2, the emergent copy symmetry U(2) (massive) or U(2)_L x U(2)_R
(massless), the lattice remnant eps = gamma5 x sigma3 and the order at which the lattice breaks the rest;
(3) the mass as a breaker; (4) how the 24 rotations act on the copy doublet, inversion, particle-hole, and
the species count.  Supplied model, finite diagnostic; no physical identification.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm, logm

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------- the supplied tick (same construction as the covariant-tick runner) ----------
C = np.array(list(itertools.product((0, 1), repeat=3))); c = C - 0.5
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def img(R, i): return int(np.argmin(np.sum(abs(c - R @ c[i]), 1)))
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
J3 = Jm(1.5)
def D3(n, a): return expm(-1j * a * sum(n[k] * J3[k] for k in range(3)))
xi = []
for i in range(8):
    n = (2 * C[i] - 1.0) / np.sqrt(3); w, v = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); xi.append(v[:, -1])
def Lrot(R):
    n, a = axang(R); Dm = D3(n, a); L = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); L[k, i] = xi[k].conj() @ Dm @ xi[i]
    return L
Ls = [Lrot(R) for R in rots]
Gm = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
Wa = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1:
            ax = int(np.argmax(abs(C[a] - C[b]))); Wa[ax][a, b] = -Gm[a, b] / abs(Gm[a, b]) / np.sqrt(3)
W3 = sum(Wa); I8 = np.eye(8)
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def Wm(mu): return np.cos(mu / 2) * W3 + 1j * np.sin(mu / 2) * I8
def U(K, mu): Wq = Wm(mu); d = Dg(K); return d.conj().T @ Wq @ d @ Wq
eps = np.diag((-1.0) ** C.sum(1)).astype(complex)
def comm_dim(Ms, tol=1e-9):
    A = np.vstack([np.kron(M, I8) - np.kron(I8, M.T) for M in Ms])
    _, s2, Vh = np.linalg.svd(A); nd = int(np.sum(s2 < tol)); return nd, [v.reshape(8, 8) for v in Vh[len(s2) - nd:].conj()], s2
def nrm(X): return np.abs(X).max()
rng = np.random.default_rng(11); KR = rng.uniform(-np.pi, np.pi, size=(40, 3))
dirs = rng.normal(size=(60, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]

# lattice cross-check of the Bloch form (6^3 sites)
N = 6; sites = np.array(list(itertools.product(range(N), repeat=3))); idx = {tuple(s): i for i, s in enumerate(sites)}
def half(Wq, off):
    M = np.zeros((N**3, N**3), complex)
    for b in itertools.product(range(0, N, 2), repeat=3):
        xs = [(np.array(b) + off + s) % N for s in C]; ids = [idx[tuple(x)] for x in xs]; rs = [int((x % 2) @ [4, 2, 1]) for x in xs]
        for p in range(8):
            for q in range(8): M[ids[p], ids[q]] = Wq[rs[p], rs[q]]
    return M
mu0 = 0.3; Ufull = half(Wm(mu0), np.ones(3, int)) @ half(Wm(mu0), np.zeros(3, int))
Kg = [2 * np.pi * np.array(k) / (N // 2) for k in itertools.product(range(N // 2), repeat=3)]
bl = np.sort(np.concatenate([np.angle(np.linalg.eigvals(U(K, mu0))) for K in Kg])); la = np.sort(np.angle(np.linalg.eigvals(Ufull)))
print('== 0. supplied tick')
check('Bloch form U(K) = D^dag W D W reproduces the 6^3 lattice spectrum (mu = 0.3)', np.abs(bl - la).max() < 1e-10, f'{np.abs(bl-la).max():.1e}')

print('== 1. Clifford structure and the block-local commutant')
gam = [np.sqrt(3) * Wa[a] for a in range(3)]
tau = [np.diag(2.0 * C[:, a] - 1).astype(complex) for a in range(3)]
G = gam + [1j * gam[a] @ tau[a] for a in range(3)]
ac = max(nrm(G[p] @ G[q] + G[q] @ G[p] - 2 * (p == q) * I8) for p in range(6) for q in range(6))
herm = max(nrm(g - g.conj().T) for g in G)
check('Gamma_1..6 = (gamma_a, i gamma_a tau_a), gamma_a = sqrt3 W_a: six anticommuting Hermitian involutions on C^8', ac < 1e-12 and herm < 1e-12, f'{ac:.1e}')
dev = max(nrm(Dg(K).conj().T @ gam[a] @ Dg(K) - np.cos(K[a]) * G[a] - np.sin(K[a]) * G[a + 3]) for K in KR for a in range(3))
check('D(K)^dag gamma_a D(K) = cos K_a Gamma_a + sin K_a Gamma_(a+3): the tick is a product of two unit 6-vectors', dev < 1e-12, f'{dev:.1e}')
P6 = G[0] @ G[1] @ G[2] @ G[3] @ G[4] @ G[5]; sgn = np.round((P6 @ eps).trace().imag / 8)
check('Gamma_1...Gamma_6 = i s eps, eps = (-1)^(x+y+z) sublattice parity, s = +-1', nrm(P6 - 1j * sgn * eps) < 1e-12, f's = {sgn:+.0f}')
nd0, B0, _ = comm_dim([U(K, 0.0) for K in KR])
span_ok = nd0 == 2 and all(nrm(b - (b.trace() / 8) * I8 - ((eps @ b).trace() / 8) * eps) < 1e-9 for b in B0)
check('mu = 0: K-independent commutant of {U(K)} has dim 2, = span{1, eps}  -> U(1)_V x U(1)_eps', span_ok, f'dim {nd0}')
dims = [comm_dim([U(K, mu) for K in KR])[0] for mu in (0.05, 0.3, 1.0)]
check('mu = 0.05, 0.3, 1.0: K-independent commutant = scalars  -> U(1)_V only', dims == [1, 1, 1], f'dims {dims}')
check('eps anticommutes with W and with the mass-free hop; eps W(mu) eps = -W(-mu)', nrm(eps @ Wm(0.3) @ eps + Wm(-0.3)) < 1e-12)
dimL = comm_dim(Ls + [U(K, 0.0) for K in KR[:10]])[0]
epsg = [np.trace(L @ eps @ L.conj().T @ eps).real / 8 for L in Ls]
odd = [round(np.linalg.det(abs(R))) * 0 + (1 if round(np.trace(R)) in (3, 0) or np.allclose(abs(np.diag(R)), 1) else -1) for R in rots]
check('rotations: L eps L^dag = +eps for E, C2face, C3 and -eps for C4, C2edge, so the commutant with rotations is scalars only',
      dimL == 1 and np.allclose(epsg, odd), f'dim {dimL}')
dp = comm_dim([U(KR[0], 0.3)])[0]
check('pointwise commutant at one generic K is 32 = 16 + 16 (U(4) x U(4) on the two fourfold bands)', dp == 32, f'{dp}')
# finite-range commutant is not a group: X_Y = sin^2 w Y - (1/4)(U - U^dag) Y (U - U^dag) commutes for ANY Y
Y = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)); fr = 0
for K in KR[:10]:
    u = U(K, 0.3); cw = np.trace(u).real / 8; X = (1 - cw**2) * Y - 0.25 * (u - u.conj().T) @ Y @ (u - u.conj().T); fr = max(fr, nrm(X @ u - u @ X))
check('finite range: X_Y = sin^2(w) Y - (U - U^+) Y (U - U^+)/4 commutes for any block-local Y (range-1 conserved bilinears, no group)', fr < 1e-12, f'{fr:.1e}')

print('== 2. continuum Dirac algebra read from the tick')
mu = 0.3; beta = -1j * logm(U(np.zeros(3), mu)) / mu      # U(0) = exp(i mu beta)
check('U(0) = exp(i mu beta) with beta = (Gamma_1+Gamma_2+Gamma_3)/sqrt3 = W', nrm(beta - W3) < 1e-10 and nrm(beta - (G[0] + G[1] + G[2]) / np.sqrt(3)) < 1e-10)
h = 1e-5; H = lambda K: 1j * logm(U(K, 0.0) + 0j)            # U = exp(-iH)
al = [np.sqrt(3) * (H(h * np.eye(3)[a]) - H(-h * np.eye(3)[a])) / (2 * h) for a in range(3)]
alA = [1j * G[a + 3] @ W3 for a in range(3)]
check('alpha_a = sqrt3 dH/dK_a = i Gamma_(a+3) beta (speed 1/sqrt3)', max(nrm(al[a] - alA[a]) for a in range(3)) < 1e-6, f'{max(nrm(al[a]-alA[a]) for a in range(3)):.1e}')
al = alA
cl = max(nrm(x @ y + y @ x - 2 * (p == q) * I8) for p, x in enumerate(al + [beta]) for q, y in enumerate(al + [beta]))
check('{alpha_a, alpha_b} = 2 delta, {alpha_a, beta} = 0: Dirac Clifford algebra Cl_4 = M_4', cl < 1e-12)
g5 = 1j * al[0] @ al[1] @ al[2]
check('gamma5 = i alpha_1 alpha_2 alpha_3: Hermitian involution, commutes with alpha, anticommutes with beta',
      nrm(g5 @ g5 - I8) < 1e-12 and max(nrm(g5 @ a - a @ g5) for a in al) < 1e-12 and nrm(g5 @ beta + beta @ g5) < 1e-12)
ndc, Bc, _ = comm_dim(al + [beta])
check('copy algebra = commutant of {beta, alpha}: dim 4 (= M_2)  -> C^8 = Dirac(4) x copy(2), emergent U(2)', ndc == 4, f'dim {ndc}')
s3 = eps @ g5
check('sigma3 := eps gamma5 lies in the copy algebra, s3^2 = 1, traceless', nrm(s3 @ s3 - I8) < 1e-12 and abs(np.trace(s3)) < 1e-12 and max(nrm(s3 @ x - x @ s3) for x in al + [beta]) < 1e-12)
Hs = [(b + b.conj().T) / 2 for b in Bc] + [(b - b.conj().T) / 2j for b in Bc]
Hs = [x - np.trace(x) / 8 * I8 for x in Hs]; Hs = [x - np.trace(x @ s3).real / 8 * s3 for x in Hs]
s1 = max(Hs, key=lambda x: np.linalg.norm(x)); s1 = s1 / np.sqrt(np.trace(s1 @ s1).real / 8); s2 = -1j * s3 @ s1
sig = [s1, s2, s3]
pa = max(nrm(sig[p] @ sig[q] - (p == q) * I8 - 1j * sum(np.sign(np.linalg.det(np.eye(3)[[p, q, r]])) * sig[r] for r in range(3) if r not in (p, q)))
         for p in range(3) for q in range(3))
check('sigma1, sigma2, sigma3 obey the Pauli algebra and commute with beta, alpha', pa < 1e-10 and max(nrm(s @ x - x @ s) for s in sig for x in al + [beta]) < 1e-10, f'{pa:.1e}')
ndm = comm_dim(al)[0]
check('massless continuum: commutant of {alpha} has dim 8 (= M_2 + M_2)  -> U(2)_L x U(2)_R on the copies', ndm == 8, f'dim {ndm}')
PL = (I8 + g5) / 2
check('lattice remnant eps = gamma5 sigma3: +1 on (L,copy+) and (R,copy-), -1 on (L,copy-) and (R,copy+): copy-nonsinglet axial', nrm(eps - g5 @ s3) < 1e-12)

print('== 3. how the lattice breaks the emergent copy symmetry')
def brk(X, mu, ks=(0.01, 0.02, 0.04)):
    v = [max(nrm(X @ U(k * d, mu) - U(k * d, mu) @ X) for d in dirs[:30]) for k in ks]; return v, np.log2(v[2] / v[1])
rows = {}
for name, X, m_ in [('sigma1', s1, 0.3), ('sigma2', s2, 0.3), ('sigma3', s3, 0.3), ('sigma3', s3, 0.0),
                    ('P_L sigma1', PL @ s1, 0.0), ('P_L sigma3', PL @ s3, 0.0), ('P_L sigma1', PL @ s1, 0.3)]:
    v, e = brk(X, m_); rows[(name, m_)] = (v, e); print(f'   [{name}, U(k)] mu={m_}: |k|=.02 {v[1]:.2e}, slope {e:.2f}')
check('massive: copy generators sigma_1,2,3 are broken at O(k^2) (block-local; not exact)', all(abs(rows[(n, 0.3)][1] - 2) < 0.15 for n in ('sigma1', 'sigma2', 'sigma3')))
check('massless: sigma3 is broken at O(k^2), while eps = gamma5 sigma3 is exact', abs(rows[('sigma3', 0.0)][1] - 2) < 0.15)
check('massless: chiral generators P_L sigma_i are broken at O(k^2); massive: P_L sigma1 is broken at O(mu) (k -> 0 limit finite)',
      abs(rows[('P_L sigma1', 0.0)][1] - 2) < 0.15 and rows[('P_L sigma1', 0.3)][0][0] > 0.05, f"{rows[('P_L sigma1', 0.3)][0][0]:.3f}")
mb = np.linalg.norm(PL @ s1 @ U(np.zeros(3), 0.3) - U(np.zeros(3), 0.3) @ PL @ s1, 2)
check('||[P_L sigma1, U(0)]|| = sin(mu): the Dirac mass breaks SU(2)_L x SU(2)_R to SU(2)_V and breaks U(1)_eps', abs(mb - np.sin(0.3)) < 1e-10 and nrm(eps @ U(np.zeros(3), 0.3) - U(np.zeros(3), 0.3) @ eps) > 0.1, f'{mb:.3f}')

print('== 4. rotations, inversion, particle-hole, species')
cov = max(min(nrm(L @ U(K, 0.3) @ L.conj().T - U(R @ K, 0.3)), nrm(L @ U(K, 0.3) @ L.conj().T - U(R.T @ K, 0.3))) for L, R in zip(Ls, rots) for K in KR[:5])
check('L(R) U(K) L(R)^dag = U(RK) for the 24 spin-3/2 corner actions', cov < 1e-12, f'{cov:.1e}')
Sig = [-1j * al[1] @ al[2], -1j * al[2] @ al[0], -1j * al[0] @ al[1]]
chis = []; rhos = []; ok = True
for L, R in zip(Ls, rots):
    M = np.array([[np.trace(L @ al[a] @ L.conj().T @ al[b]).real / 8 for b in range(3)] for a in range(3)])
    Mr = np.round(M); assert nrm(M - Mr) < 1e-10; n, a = axang(Mr.T); best = None
    for sgn_ in (1, -1):
        S = expm(-1j * sgn_ * a / 2 * sum(n[k] * Sig[k] for k in range(3)))
        e_ = max(nrm(S @ al[q] @ S.conj().T - L @ al[q] @ L.conj().T) for q in range(3))
        if best is None or e_ < best[0]: best = (e_, S)
    rho = best[1].conj().T @ L; ok &= best[0] < 1e-10 and max(nrm(rho @ x - x @ rho) for x in al + [beta]) < 1e-10
    r2 = np.trace(rho).real / 8 * np.eye(2) + sum(np.trace(rho @ sig[i]) / 8 * np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]][i]) for i in range(3))
    rhos.append(r2); chis.append(abs(np.trace(r2)))
check('each rotation factorises as L(R) = S_spin1/2(R) rho(R), rho(R) in the copy U(2)', ok)
cls = {}
for R, ch in zip(rots, chis):
    t = int(round(np.trace(R))); key = {3: 'E', -1: 'C2', 1: 'C4', 0: 'C3'}[t]
    if key == 'C2' and np.count_nonzero(R) == 3 and np.allclose(abs(np.diag(R)), 1): key = 'C2face'
    elif key == 'C2': key = 'C2edge'
    cls.setdefault(key, set()).add(round(ch, 6))
print('   |tr rho| by class:', {k: sorted(v) for k, v in cls.items()})
check("copy doublet carries |chi| = (2, 2, 0, 1, 0) on (E, C2face, C4, C3, C2edge): the E irrep of O (factor S3 = axis permutations)",
      cls == {'E': {2.0}, 'C2face': {2.0}, 'C4': {0.0}, 'C3': {1.0}, 'C2edge': {0.0}})
def comm2(Ms):
    A = np.vstack([np.kron(M, np.eye(2)) - np.kron(np.eye(2), M.T) for M in Ms]); return int(np.sum(np.linalg.svd(A, compute_uv=False) < 1e-9))
check('rho is irreducible: only scalars in the copy U(2) commute with all 24 rotations', comm2(rhos) == 1, f'dim {comm2(rhos)}')
def sol(lhs, rhs, Ks):   # dim of {P : P lhs(K) = rhs(K) P for all K}
    A = np.vstack([np.kron(I8, lhs(K).T) - np.kron(rhs(K), I8) for K in Ks]); _, sv, Vh = np.linalg.svd(A)
    nd = int(np.sum(sv < 1e-9)); return nd, [v.conj().reshape(8, 8) for v in Vh[len(sv) - nd:]]
npar, Bp = sol(lambda K: U(K, 0.3), lambda K: U(-K, 0.3), KR[:20])
if npar:
    P = Bp[0] / np.sqrt(np.trace(Bp[0].conj().T @ Bp[0]).real / 8)
    check('inversion: P U(K) = U(-K) P has a 1-dim block-local solution, |P| = corner inversion s -> 1-s',
          npar == 1 and nrm(abs(P) - np.eye(8)[::-1]) < 1e-9, f'dim {npar}')
    check('P flips chirality (P gamma5 P^-1 = -gamma5) and eps: the matter content is L-R symmetric (vector-like)',
          nrm(P @ g5 @ P.conj().T + g5) < 1e-9 and nrm(P @ eps @ P.conj().T + eps) < 1e-9)
else:
    check('inversion: P U(K) = U(-K) P has a block-local solution', False, 'dim 0')
nph0 = sol(lambda K: U(K, 0.0), lambda K: U(-K, 0.0).conj(), KR[:20])[0]
nph3 = sol(lambda K: U(K, 0.3), lambda K: U(-K, 0.3).conj(), KR[:20])[0]
print(f'   particle-hole M U(K) = U(-K)^* M: solution dims mu=0: {nph0}, mu=0.3: {nph3}')
check('particle-hole (Fock-space unitary c -> M c^dag): block-local M exists at mu = 0 and mu = 0.3', nph0 >= 1 and nph3 >= 1, f'{nph0}, {nph3}')
KZ = rng.uniform(-np.pi, np.pi, size=(3000, 3)); w = np.abs(np.angle(np.linalg.eigvals(np.array([U(K, 0.3) for K in KZ]))))
d0 = np.min(w, 1); dpi = np.min(np.pi - w, 1)
wpi = np.abs(np.angle(np.linalg.eigvals(U(np.full(3, np.pi) + 0.02 * dirs[0], 0.3))))
check('species: w = 0 sector gapped by mu at K = 0 (2 Dirac copies); w = pi sector massless at K = pi(1,1,1), speed cos(mu/2)/sqrt3',
      d0.min() >= 0.3 - 1e-12 and np.allclose(np.pi - wpi, 0.02 * np.cos(0.15) / np.sqrt(3), rtol=2e-3), f'{(np.pi - wpi).mean()/0.02:.4f}')
check('every band is exactly fourfold (no threefold degeneracy anywhere sampled)', np.ptp(np.sort(w, 1)[:, :4], 1).max() < 1e-8 and np.ptp(np.sort(w, 1)[:, 4:], 1).max() < 1e-8)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
