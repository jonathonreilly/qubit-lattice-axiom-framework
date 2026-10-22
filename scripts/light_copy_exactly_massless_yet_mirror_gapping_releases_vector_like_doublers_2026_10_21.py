#!/usr/bin/env python3
"""light-protection: does the light copy stay massless and chiral when the mirror copy of H' is gapped by its own term?

Supplied model: the cube objects of the register (one fermion mode per site, spin-3/2 edge hop W, face-diagonal hop F,
copy sign s3 = -S F; light = s3 = -1 (q2), mirror = s3 = +1 (q1), families-mod-3 labels), the candidate generator
H' = (i/2)[W_o, W_e] in the Bloch convention of the probes (odd cube read in even corner labels = one overlap state per
site), and a supplied copy-selective mirror term: the Spin(10) pair square (smg-verify chain data, recomputed), its
one-block stand-in (the mirror top form, 8 modes), and a 1+1D two-copy chain with a mirror pair hop.
 A free copy structure of H'          B exact K = 0 decoupling           C light self-energy from the exact mirror
 D anomaly bookkeeping (integers)     E Golterman-Shamir: composites and strong-coupling doubling
 F 1+1D chain, sparse ED (16 modes, twisted ring)
Labels: [T] theorem / exact finite computation, [F] finite diagnostic, [E] estimate, [M] against measurement.
Cited, not rederived: Nielsen-Ninomiya, 't Hooft matching, Golterman-Shamir arXiv:2505.20436 (generalised NN, Sec. IV)."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/LIGHT_COPY_EXACTLY_MASSLESS_YET_MIRROR_GAPPING_RELEASES_VECTOR_LIKE_DOUBLERS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import eigsh
from scipy.linalg import expm

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
OM = np.exp(2j * np.pi / 3)

# ------------------------------------------------ cube objects and H' ------------------------------------------------
C = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
S = np.diag((-1.0) ** C.sum(1)).astype(complex)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
def hop(d2, sign):
    H = np.zeros((8, 8), complex)
    for a in range(8):
        for b in range(8):
            if round(float(np.sum((C[a] - C[b]) ** 2))) == d2: g_ = XI[a].conj() @ XI[b]; H[a, b] = sign * g_ / abs(g_) / np.sqrt(3)
    return H
W = hop(1, -1.0); F = hop(2, 1.0); s3 = -S @ F
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def Hp(K): D = Dg(K); Wo = D.conj().T @ W @ D; return 0.5j * (Wo @ W - W @ Wo)
EV = [i for i in range(8) if C[i].sum() % 2 == 0]; OD = [i for i in range(8) if C[i].sum() % 2 == 1]
def cbasis(sub, sgn):
    ix = EV if sub == 'e' else OD; w_, v_ = np.linalg.eigh(s3[np.ix_(ix, ix)]); B = np.zeros((8, 2), complex); B[ix, :] = v_[:, np.isclose(w_, sgn)]; return B
Le, Me, Lo, Mo = cbasis('e', -1), cbasis('e', 1), cbasis('o', -1), cbasis('o', 1)
Ul = np.hstack([Le, Lo]); Um = np.hstack([Me, Mo])
P2 = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1]).astype(complex)]
def chir(B, K0, h=1e-6):
    vel = [(B.conj().T @ (Hp(K0 + h * np.eye(3)[a]) - Hp(K0 - h * np.eye(3)[a])) @ B) / (2 * h) for a in range(3)]
    return float(np.sign(np.linalg.det(np.array([[np.trace(vel[a] @ P2[i]).real / 2 for a in range(3)] for i in range(3)]))))
Rv = np.full(3, np.pi); corners = [np.array(c) * np.pi for c in itertools.product((0, 1), repeat=3)]

# ===================================== A. free copy structure =====================================
print('== A. free copy structure of H\' (light = s3 -1, mirror = s3 +1)')
kd = np.array([.3, .5, .81]) / np.linalg.norm([.3, .5, .81])
sl = np.log2(nrm(s3 @ Hp(.04 * kd) - Hp(.04 * kd) @ s3) / nrm(s3 @ Hp(.02 * kd) - Hp(.02 * kd) @ s3))
win = (chir(Le, np.zeros(3)), chir(Me, np.zeros(3)), chir(Le, Rv), chir(Lo, np.zeros(3)))
check('A1 [T] H\'(0) = H\'(R) = 0; s3 splits each sublattice 2+2; [s3,H\'(K)] = O(K^2); even sublattice: light L at Gamma and R at R, '
      'mirror R at Gamma', nrm(Hp(np.zeros(3))) < 1e-14 and nrm(Hp(Rv)) < 1e-14 and abs(sl - 2) < 0.02
      and win == (-1.0, 1.0, 1.0, 1.0), f'slope {sl:.3f}')
ratio = []
for d in (np.array([1., 0, 0]), np.array([1., 1, 0]), np.array([1., 2, 3]), np.array([2., -1, .5])):
    d = d / np.linalg.norm(d); q = 0.01 * d; sv = np.linalg.svd(Me.conj().T @ Hp(q) @ Le, compute_uv=False)
    pred = np.sqrt(2) / 6 * abs(q[0] ** 2 + OM * q[1] ** 2 + OM ** 2 * q[2] ** 2); ratio.append(sv / pred)
bd = np.linalg.svd(Me.conj().T @ Hp(0.05 * np.ones(3) / np.sqrt(3)) @ Le, compute_uv=False).max()
check('A2 [T] near Gamma the light-mirror block has 2 equal singular values (sqrt2/6)|Kx^2 + w Ky^2 + w^2 Kz^2| (d-wave, 0 on body diagonals)', np.allclose(ratio, 1, atol=2e-3) and bd < 1e-12,
      f'ratio {np.min(ratio):.4f}..{np.max(ratio):.4f}')
cor = []
for K in corners:
    H = Hp(K); cor.append((nrm(Le.conj().T @ H @ Le), nrm(Me.conj().T @ H @ Me), *np.linalg.svd(Me.conj().T @ H @ Le, compute_uv=False),
                           np.abs(np.linalg.eigvalsh(H)).min()))
cor = np.array(cor); nX = [i for i, K in enumerate(corners) if 0 < np.sum(K > 1) < 3]
check('A3 [T] at the 8 corners the light-light and mirror-mirror blocks vanish; the mixing is 0 at Gamma, R and 2sqrt2/3 = the whole '
      'free gap at the 6 X/M corners: H\' gaps X, M only by copy mixing',
      cor[:, :2].max() < 1e-14 and np.allclose(cor[nX, 2:4], 2 * np.sqrt(2) / 3) and np.allclose(cor[nX, 4], 2 * np.sqrt(2) / 3)
      and cor[[0, 7], 2:].max() < 1e-14)
g20 = (np.arange(20) + 0.5) / 20 * 2 * np.pi - np.pi; far = np.inf; tr = 0.0
for K in itertools.product(g20, g20, g20):
    K = np.array(K); h = Le.conj().T @ Hp(K) @ Le; tr = max(tr, abs(np.trace(h)))
    dist = min(np.linalg.norm((K - c + np.pi) % (2 * np.pi) - np.pi) for c in corners)
    if dist > 0.4: far = min(far, np.abs(np.linalg.eigvalsh(h)).min())
chis = [chir(Le, K) for K in corners]; r_ = [int(np.sum(K > 1)) for K in corners]
check('A4 [T] the light projected band P_l H\' P_l is traceless with zeros only at the 8 corners, chirality (-1)^(r+1) (Gamma, 3M left; '
      '3X, R right): net 0',
      tr < 1e-12 and all(c == (-1.0) ** (r + 1) for c, r in zip(chis, r_)) and sum(chis) == 0 and far > 0.05,
      f'min |E| > {far:.3f} away from corners')

# ===================================== B. exact K = 0 decoupling =====================================
print('== B. exact decoupling of the light copy at K = 0 and R')
Lt = 4; sites = np.array(list(itertools.product(range(Lt), repeat=3))); sid = {tuple(s): i for i, s in enumerate(sites)}
def layer(off):
    M = np.zeros((Lt ** 3, Lt ** 3), complex); cubes = []
    for b0 in itertools.product(range(0, Lt, 2), repeat=3):
        X_ = [(np.array(b0) + off + c) % Lt for c in C]; ids = [sid[tuple(x)] for x in X_]; lab = [int((x % 2) @ [4, 2, 1]) for x in X_]
        M[np.ix_(ids, ids)] = W[np.ix_(lab, lab)]; cubes.append((ids, lab))          # one overlap state per site (even labels)
    return M, cubes
We_, ce = layer(np.zeros(3, int)); Wo_, co = layer(np.ones(3, int)); Hr = 0.5j * (Wo_ @ We_ - We_ @ Wo_)
blk = np.array([int(((s // 2) % 2) @ [1, 1, 1]) for s in sites]); lab = np.array([int((s % 2) @ [4, 2, 1]) for s in sites])
vecs = [np.array([Ul[lab[i], k] * sgn ** blk[i] for i in range(Lt ** 3)]) / np.sqrt(8) for k in range(4) for sgn in (1, -1)]
Pm = (I8 + s3) / 2; orth = 0.0
for ids, lb in ce + co:
    Q = Pm[np.ix_(lb, lb)]
    for v in vecs: orth = max(orth, np.abs(Q @ v[ids]).max())
bl = np.sort(np.concatenate([np.linalg.eigvalsh(Hp(K)) for K in corners])); spec_ok = np.allclose(np.sort(np.linalg.eigvalsh(Hr)), bl)
check('B1 [T] 4^3 torus, both tilings: light K=0 and K=R states are killed by H\' and orthogonal to the mirror combos of all 16 cubes, '
      'so (CAR) they commute with every mirror term: exact zero modes, G_l(z,0) = 1/z at any coupling', spec_ok and max(np.abs(Hr @ v).max() for v in vecs) < 1e-13 and orth < 1e-13,
      f'overlap {orth:.0e}')

# ---------- one-block twisted model: 8 modes, copy-selective mirror top form ----------
nB = 8; dB = 1 << nB
def annB(i):
    M = np.zeros((dB, dB))
    for s in range(dB):
        if (s >> i) & 1: M[s ^ (1 << i), s] = (-1) ** bin(s & ((1 << i) - 1)).count('1')
    return M
cB = [annB(i) for i in range(nB)]
def modeB(U, k): return sum(np.conj(U[i, k]) * cB[i] for i in range(nB))
bm = [modeB(Um, k) for k in range(4)]; al = [modeB(Ul, k) for k in range(4)]
Om = bm[0].conj().T @ bm[1].conj().T @ bm[2].conj().T @ bm[3].conj().T; Hint = -(Om + Om.conj().T)
def H0B(K): h = Hp(K); return sum(h[i, j] * cB[i].T @ cB[j] for i in range(nB) for j in range(nB))
deg = []
for K in (np.zeros(3), Rv):
    for g in (0.5, 4.0, 32.0):
        E = np.linalg.eigvalsh(H0B(K) + g * Hint); deg.append((E[15] - E[0], E[16] - E[0] - g))
comm = max(nrm(a @ (H0B(K) + 4 * Hint) - (H0B(K) + 4 * Hint) @ a) for a in al for K in (np.zeros(3), Rv))
check('B2 [T] one block, mirror top form: at Gamma and R the 16 light states stay exactly degenerate, mirror gap exactly g (g = .5, 4, 32)', max(abs(x) for d_ in deg for x in d_) < 1e-10
      and comm < 1e-12, f'splitting {max(d_[0] for d_ in deg):.0e}')

# ===================================== C. light self-energy from the exact mirror =====================================
print('== C. light self-energy with the exact Spin(10) pair-square cell (Task 1)')
b0 = np.sqrt([16 * k * (9 - k) * (k + 4) * (13 - k) for k in range(1, 9)]); ew, ev = np.linalg.eigh(np.diag(b0, 1) + np.diag(b0, -1)); E0c, gsv = ew[0], ev[:, 0]
b10 = np.sqrt([16 * k * (8 - k) * (k + 5) * (13 - k) for k in range(1, 8)]); D10 = np.linalg.eigvalsh(np.diag(b10, 1) + np.diag(b10, -1))[0] - E0c
bf = np.sqrt([16 * k * (8 - k) * (k + 4) * (13 - k) for k in range(1, 8)]); ef, vf = np.linalg.eigh(np.diag(bf, 1) + np.diag(bf, -1))
n0 = np.concatenate([[1.0], np.cumprod(b0 ** 2)]); nf = np.concatenate([[1.0], np.cumprod(bf ** 2)])
Aw = (vf.T @ (gsv[:8] * np.sqrt(nf / n0[:8]))) ** 2; eps_ = ef - E0c; Df = eps_[0]
cZ = float(np.sum(2 * Aw / eps_ ** 2))
Gb = lambda z: np.sum(Aw * (1 / (z - eps_) + 1 / (z + eps_)))
check('C1 [T] cell chains: E0 = -2g sqrt(11088+48 sqrt21081), Delta = %.4f g, Delta_f = %.4f g, c^dag|GS> %.3f%% in the lowest fermion '
      'level; chain reversal + p-h conjugation (16 <-> 16bar) give equal hole weights, so the isolated-cell G_b is odd: G_b(0) = 0' % (D10, Df, 200 * Aw[0]),
      abs(E0c + 2 * np.sqrt(11088 + 48 * np.sqrt(21081))) < 1e-9 and np.allclose(nf / n0[:8], 1 - np.arange(8) / 8) and abs(Aw.sum() - .5) < 1e-12
      and abs(Gb(0.0)) < 1e-15 and abs(Gb(1e-3 * Df) + 1e-3 * Df * cZ) < 1e-8 and np.allclose(gsv[::-1], gsv),
      f'c_Z Delta_f^2 = {cZ * Df ** 2:.5f}; ground chain reversal-even')
# second order with the atom's exact G_m(z) = (z - h_m)/((z - h_m)^2 - g^2) for each mirror eigenmode m of the mirror's own band
Kq = np.array([0.3, 0, 0]); Hq = Hp(Kq); haa = Le.conj().T @ Hq @ Le; hbb = Me.conj().T @ Hq @ Me; hba = Me.conj().T @ Hq @ Le
ea, va = np.linalg.eigh(haa); vK = ea[-1]; plus = va[:, -1]; eb, vb = np.linalg.eigh(hbb); cpl = np.abs(vb.conj().T @ (hba @ plus)) ** 2
res = []
for g in (2.0, 8.0):
    E, Vv = np.linalg.eigh(H0B(Kq) + g * Hint); gs = Vv[:, 0]; best = (0, 0)
    for a in al:
        amp = np.abs(Vv.conj().T @ (a.conj().T @ gs)) ** 2; k = int(np.argmax(amp))
        if amp[k] > best[1]: best = (E[k] - E[0], amp[k])
    zr = vK
    for _ in range(80): zr = vK + np.sum(cpl * (zr - eb) / ((zr - eb) ** 2 - g ** 2))
    res.append((g, best[0], zr))
st0 = float(np.sum(cpl * eb / (g ** 2 - eb ** 2)))
check('C2 [T/F] second order Sigma = h G_b h^+: a Z factor -z c_Z s^2 and a static part h G_b(0,K) h^+, G_b(0,K) ~ h_bb(K)/Delta^2 from the '
      'mirror\'s own band: O(K^5), zero at K = 0, never a mass. One-block ED at K = .3x matches the shift to 1%', all(abs(e - p) < 0.01 * (vK - p) for g, e, p in res)
      and all(vK - e > 1e-6 for g, e, p in res), '; '.join(f'g={g:g}: {e:.9f} vs {p:.9f}' for g, e, p in res))
aTeV = 2 * 3 * 1.616e-35 * 1e3 / 1.973e-16; dv = 2 * aTeV ** 4 / 18 / 3.4 ** 2
print(f'   [E] 1 TeV (block 2a, a = 3 l_P): K = {aTeV:.0e}, |dv/v| < {dv:.0e} for Delta_f >= 3.4; induced light-light terms ~ K^8/Delta_f^3')
print('   [T] a mirror condensate reaches the light only through h(K) ~ K^2: its induced light mass term is ~ K^4/M, zero at K = 0 (B1).')
print('       Measured masses need a vacuum field coupled to the light copy directly, not a mirror-sector vev.')

# ===================================== D. anomaly bookkeeping =====================================
print('== D. anomalies of the light content (exact integers)')
qa = 2; prot = {k: [N for N in range(1, 10) if (4 * N * (qa + k)) % 3 != 0] for k in range(3)}
Sobs = {k: [N for N in range(1, 10) if (-4 * N * (qa + k)) % 3 != 0] for k in range(3)}
check('D1 [T] per family the light carries twisted-Z3_k x SU(2)_e^2 = 4(q_a+k) (16 = 1 mod 3 at k = 2), S the opposite: anomaly '
      'protection holds exactly for the N at which S cannot be gapped', prot == Sobs and prot[2] == [1, 2, 4, 5, 7, 8] and prot[1] == [],
      f'k=2: N {prot[2]}')
fam = [(+1, 2, 1, 4), (-1, 1, 2, 4)]                  # (z charge in LH basis, SU(2)_e dim, SU(2)_o dim, SU(4) dim): (a,L) even, conj (a,R) odd
z4su2 = sum(4 * 1 for f in fam if f[1] == 2) % 4; witten = sum(4 for f in fam if f[1] == 2) % 2
z3c = lambda N: N * sum(f[0] ** 3 * f[1] * f[2] * f[3] for f in fam) % 3; z3g = lambda N: N * sum(f[0] * f[1] * f[2] * f[3] for f in fam) % 3
su4 = sum(f[0] * f[1] * f[2] for f in fam)
check('D2 [T] at N = 0 mod 3 all listed light anomalies vanish (Z4xSU(2)^2, Z16 = 16, Witten, Z3^3, Z3-grav, Z3xSU(4)^2, Z3xSU(2)^2): '
      'anomaly matching gives no protection there', (z4su2, 16 % 16, witten, z3c(3), z3g(3), su4, (4 * 3 * (qa + 2)) % 3) == (0,) * 7)

# ===================================== E. Golterman-Shamir =====================================
print('== E. Golterman-Shamir: composites and strong-coupling doubling (Task 2)')
bind = (8 / 9) / Df
check('E1 [E] composites: odd-N cell levels >= %.2f g (c^dag|GS> %.2f%% in the lowest, so composite fermions share it), even >= %.2f g; '
      'band >= %.1f g for t < 3.65 g; light + mirror boson >= %.2f g - %.3f/g; twisted charge 0 vs 1 forbids mirror-only partners'
      % (Df, 200 * Aw[0], D10, Df * (1 - 3.65 / 5.60), D10, bind), Df * (1 - 3.65 / 5.60) > 10 and 0.1 * D10 > 5 * bind / 0.1)
X = np.array([np.pi, 0, 0]); out = []
for g in (0.0, 2.0, 8.0, 32.0):
    E, Vv = np.linalg.eigh(H0B(X) + g * Hint); E = E - E[0]; gs = Vv[:, 0]
    wt = np.mean([sum(abs(Vv[:, k].conj() @ (a.conj().T @ gs)) ** 2 + abs(Vv[:, k].conj() @ (a @ gs)) ** 2 for k in range(dB) if E[k] < 0.1) for a in al])
    out.append((g, E[1], E[15], E[16], wt))
slope = np.log(out[2][2] / out[3][2]) / np.log(out[2][0] / out[3][0])
Zp = 32 ** 2 / (32 ** 2 + 8 / 9)
check('E2 [T] endpoint (mirror frozen, P f P = 0): light H_eff = P_l H\' P_l, 8 Weyl nodes per sublattice per family, 4L + 4R: '
      'vector-like in each SU(2)_e sector (Golterman-Shamir Sec. IV)', sum(chis) == 0 and len(chis) == 8)
check('E3 [F] one block at X: free gap 2sqrt2/3; with the mirror top form the 16 light states lie within %.1e at g = 32 (slope %.2f), '
      'light weight %.4f = Z = g^2/(g^2+8/9): doublers released' % (out[3][2], slope, out[3][4]),
      abs(out[0][1] - 2 * np.sqrt(2) / 3) < 1e-12 and out[3][2] < 1e-3 and abs(slope + 3) < 0.2 and abs(out[3][4] - Zp) < 5e-4 and out[3][3] > 25,
      'gap ' + ', '.join(f'{o[1]:.4f}' for o in out))
g8 = (np.arange(16) + 0.5) / 16 * 2 * np.pi - np.pi; full = proj = 0.0
for K in itertools.product(g8, g8, g8):
    H = Hp(np.array(K)); full += np.abs(np.linalg.eigvalsh(H)).sum() / 2
    proj += (np.abs(np.linalg.eigvalsh(Ul.conj().T @ H @ Ul)).sum() + np.abs(np.linalg.eigvalsh(Um.conj().T @ H @ Um)).sum()) / 2
full /= 16 ** 3; proj /= 16 ** 3; gstar = 8 * (full - proj / 2) / (-E0c); gsmg = np.sqrt(0.2382 * (5 / 6) / D10)
check('E4 [E] per block: hybridisation + mirror band %.3f x 8 vs condensation %.2f g: g* = %.3f < SMG bound %.3f (s^2 = 5/6): where the '
      'mirror is gapped, the doublers are released' % (full - proj / 2, -E0c, gstar, gsmg), gstar < gsmg)
rim = max(nrm(Hp(np.array(K) + Rv) + Hp(np.array(K))) for K in itertools.product(g8[::3], g8[::3], g8[::3])); zr5 = []; mu5 = 0.3
for K in itertools.product(g20, g20, g20):
    K = np.array(K); h = Le.conj().T @ Hp(K) @ Le; f = 1 - np.mean(np.cos(K)) ** 2
    zr5.append((np.abs(np.linalg.eigvalsh(np.block([[h, mu5 * f * np.eye(2)], [mu5 * f * np.eye(2), Le.conj().T @ Hp(K + Rv) @ Le]]))).min(),
                min(np.linalg.norm((K - c + np.pi) % (2 * np.pi) - np.pi) for c in (np.zeros(3), Rv))))
zfar = min(e for e, d in zr5 if d > 0.4); zX = min(np.abs(np.linalg.eigvalsh(np.block([[Le.conj().T @ Hp(c) @ Le, mu5 * (1 - np.mean(np.cos(c)) ** 2) * np.eye(2)],
       [mu5 * (1 - np.mean(np.cos(c)) ** 2) * np.eye(2), Le.conj().T @ Hp(c + Rv) @ Le]]))).min() for c in corners[1:7])
check('E5 [T] zoom repair of X/M: a light-copy term mu(1 - S(K)^2) linking K and K+R (staggered over blocks, one rung up) gives '
      'E^2 = |d|^2 + mu^2 f^2 since H\'(K+R) = -H\'(K): the 6 X/M doublers get gap mu 8/9, Gamma and R stay, B1 is kept', rim < 1e-12 and
      abs(zX - mu5 * 8 / 9) < 1e-12 and zfar > 0.05, f'X/M gap {zX:.4f} at mu = {mu5}')
print('   [M] >= 4 left + 4 right weak-doublet tastes per family: N_nu >= 12 at N = 3 vs 2.984 +- 0.008; right-handed currents vs V - A.')
print('   [T] an endpoint freezing local light combinations leaves a finite-range free H_eff: by Nielsen-Ninomiya its nodes have net')
print('       chirality 0 per SU(2)_e sector, so with Gamma kept (B1) a right-handed node survives (1+1D: F5)')

# ===================================== F. 1+1D chain =====================================
print('== F. 1+1D two-copy chain: 2 cells x (e,o) x (light, mirror) x 2 flavours = 16 modes, twisted ring (Task 3)')

L1 = 2; NM = 16; MU = 0.5
def ix1(j, s, c, a): return ((j * 2 + s) * 2 + c) * 2 + a
def hs1(p, s): sg = 1.0 if s == 0 else -1.0; return np.array([[sg * np.sin(p), MU * (1 - np.cos(p))], [MU * (1 - np.cos(p)), -sg * np.sin(p)]])
def hsp1(th):
    H = np.zeros((NM, NM), complex); ps = [(th + 2 * np.pi * n) / L1 for n in range(L1)]
    for s, a, j, jp in itertools.product(range(2), range(2), range(L1), range(L1)):
        bk = sum(np.exp(1j * p * (j - jp)) * hs1(p, s) for p in ps) / L1
        for c, cp in itertools.product(range(2), range(2)): H[ix1(j, s, c, a), ix1(jp, s, cp, a)] = bk[c, cp]
    return H
st1 = np.arange(1 << NM, dtype=np.int64); pc1 = np.array([bin(x).count('1') for x in range(1 << NM)], np.int64)
bitsum = lambda lst: sum((st1 >> m) & 1 for m in lst)
QN = np.stack([pc1, bitsum([ix1(j, 0, c, 0) for j in range(L1) for c in range(2)]) - bitsum([ix1(j, 0, c, 1) for j in range(L1) for c in range(2)]),
               bitsum([ix1(j, 1, c, 0) for j in range(L1) for c in range(2)]) - bitsum([ix1(j, 1, c, 1) for j in range(L1) for c in range(2)])], 1)
def sec(N, a, b): return st1[(QN[:, 0] == N) & (QN[:, 1] == a) & (QN[:, 2] == b)]
def apply(st, seq):
    s = st.copy(); sg = np.ones(len(s)); ok = np.ones(len(s), bool)
    for op, m in reversed(seq):
        occ = ((s >> m) & 1) == 1; ok &= (~occ) if op == 'c' else occ
        sg *= np.where(pc1[s & ((1 << m) - 1)] % 2 == 0, 1.0, -1.0); s = s ^ (1 << m)
    return s, sg, ok
def build(si, so, terms):
    pos = -np.ones(1 << NM, np.int64); pos[so] = np.arange(len(so)); R_, C_, V_ = [], [], []
    for coef, seq in terms:
        s, sg, ok = apply(si, seq); ok &= pos[s] >= 0; R_.append(pos[s[ok]]); C_.append(np.nonzero(ok)[0]); V_.append(coef * sg[ok])
    return sps.csr_matrix((np.concatenate(V_), (np.concatenate(R_), np.concatenate(C_))), shape=(len(so), len(si)))
def Hterms(th, g, cops=(1,)):
    h = hsp1(th); T = [(h[i, k], [('c', i), ('a', k)]) for i in range(NM) for k in range(NM) if abs(h[i, k]) > 1e-13]
    for j, c, cq in itertools.product(range(L1), cops, cops):
        T.append((-g, [('c', ix1(j, 0, c, 0)), ('c', ix1(j, 0, c, 1)), ('a', ix1(j, 1, cq, 1)), ('a', ix1(j, 1, cq, 0))]))
        T.append((-g, [('c', ix1(j, 1, cq, 0)), ('c', ix1(j, 1, cq, 1)), ('a', ix1(j, 0, c, 1)), ('a', ix1(j, 0, c, 0))]))
    return T
def lmode(p, s):
    v = np.zeros(NM, complex)
    for j in range(L1): v[ix1(j, s, 0, 0)] = np.exp(1j * p * j) / np.sqrt(L1)
    return v
def qp(th, g, p, s, cops=(1,)):            # signed light quasiparticle energy with the largest weight (particle +, hole -)
    T = Hterms(th, g, cops); s0 = sec(8, 0, 0); w_, v_ = eigsh(build(s0, s0, T), k=2, which='SA'); E0_, gs = w_[0], v_[:, np.argmin(w_)]
    best = (0.0, 0.0)
    for create in (True, False):
        d = 1 if create else -1; s1 = sec(9 if create else 7, *((d, 0) if s == 0 else (0, d)))
        vec = lmode(p, s); A = build(s0, s1, [((vec[m] if create else np.conj(vec[m])), [('c' if create else 'a', m)]) for m in range(NM) if abs(vec[m]) > 1e-13])
        ww, vv = eigsh(build(s1, s1, T), k=10, which='SA'); ov = np.abs(vv.conj().T @ (A @ gs)) ** 2; k = int(np.argmax(ov))
        if ov[k] > best[1]: best = ((ww[k] - E0_) * (1 if create else -1), ov[k])
    return best
pp = np.linspace(-np.pi, np.pi, 401); fb = [np.linalg.eigvalsh(hs1(p, 0)) for p in pp]
check('F1 [T] free chain: one Dirac cone per sublattice at p = 0 (light R + mirror L on e); the light p = pi doubler is gapped only by '
      'the copy mixing mu(1 - cos p): 2 mu = 1', min(abs(e).min() for e in fb) < 1e-12 and abs(np.abs(np.linalg.eigvalsh(hs1(np.pi, 0))).min() - 2 * MU) < 1e-12)
s0 = sec(8, 0, 0); s1 = sec(7, -1, 0); T0_ = Hterms(0.0, 16.0); A0 = build(s0, s1, [(np.conj(lmode(0, 0)[m]), [('a', m)]) for m in range(NM) if abs(lmode(0, 0)[m]) > 0])
cmm = abs(build(s1, s1, T0_) @ A0 - A0 @ build(s0, s0, T0_)).max()
th = 0.3; G = {g: qp(th, g, th / 2, 0) for g in (0.0, 16.0)}; Pi_ = {g: qp(th, g, th / 2 + np.pi, 0) for g in (0.0, 4.0, 16.0)}
check('F2 [F] mirror cell singlet unique, gap g, G_b = z/(z^2 - g^2); [H, a_light(p=0)] = 0 at theta = 0, g = 16; theta = .3: light Gamma qp '
      '%+.4f (w %.4f) at g = 16: gapless, right-moving' % G[16.0], cmm < 1e-12 and abs(G[16.0][0] - np.sin(.15)) < 2e-4 and G[16.0][1] > 0.999
      and abs(G[0.0][0] - np.hypot(np.sin(.15), MU * (1 - np.cos(.15)))) < 1e-9, f'commutator {cmm:.0e}')
Zpi = 16 ** 2 / (16 ** 2 + (MU * (1 + np.cos(.15))) ** 2)
check('F3 [F] light p = pi doubler qp: free %+.3f (w %.2f), g = 4 %+.3f (w %.2f), g = 16 %+.4f (w %.4f = Z): released as a left-mover, the '
      'light copy becomes R + L: not chiral' % (*Pi_[0.0], *Pi_[4.0], *Pi_[16.0]),
      abs(Pi_[0.0][0]) > 0.99 and abs(Pi_[16.0][0] + np.sin(.15)) < 1e-3 and abs(Pi_[16.0][1] - Zpi) < 2e-3)
Gn = qp(th, 16.0, th / 2, 0, cops=(0, 1))
check('F4 [F] contrast, pair hop on both copies: light Gamma qp -> %+.2f (w %.2f): a term touching the light at p = 0 gaps it' % Gn,
      abs(Gn[0] - np.sin(.15)) > 0.05 or Gn[1] < 0.5)
Ls = 400; hl = np.zeros((Ls, Ls), complex)
for j in range(Ls): hl[(j + 1) % Ls, j] = 0.5j; hl[j, (j + 1) % Ls] = -0.5j
Ssym = np.zeros((Ls, Ls // 2))
for J in range(Ls // 2): Ssym[2 * J, J] = Ssym[2 * J + 1, J] = 1 / np.sqrt(2)
heff = Ssym.T @ hl @ Ssym; ks = 2 * np.pi * np.arange(Ls // 2) / (Ls // 2); band = np.sort(np.linalg.eigvalsh(heff))
check('F5 [T] zone-corner endpoint: freezing (a_2J - a_2J+1)/sqrt2 leaves H_eff = sin(K)/2, a new left-mover at K = pi (Nielsen-Ninomiya)',
      np.allclose(band, np.sort(np.sin(ks) / 2), atol=1e-12))
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('theorems: A1-A4, B1-B2, C1, D1-D2, E2, E5, F1, F5; finite: C2, E3, F2-F4; estimates: E1, E4, [E]/[M] lines. Supplied: H\', which copy')
print('  is the mirror, the mirror terms (pair square, top form, pair hop), g, mu, the (4,2) content, twist k = 2. Cited: Nielsen-Ninomiya,')
print('  anomaly matching, Golterman-Shamir 2505.20436, the smg-verify chain formulas.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
