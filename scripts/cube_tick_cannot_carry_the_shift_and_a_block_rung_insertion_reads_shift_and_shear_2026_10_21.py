#!/usr/bin/env python3
"""shift-shear: reading the full 4D cube metric (lapse, shift g_0i, spatial metric with g_ij off-diagonal) into the
CL-1 update tick (old CL-2).  Supplied models; exact identities and finite diagnostics; no physical identification.
 A  cube rung (2^3): flow, reflection, shear-sign and shift-helicity-lock theorems; copy-mass placement
 B  block rung (2x2x2 cubes): the frame insertion; exact at rest; shift and shear of the light cone; covariance
 C  dynamics: gravitomagnetic force on packets (curl vs gradient shift); light bent by a shear gradient
 D  coordinator checks: (a) bending under the fixed-4-volume clause, (b) GP-B, (c) PPN alpha1, alpha2 from the rule
 E  earlier results; estimates against measurement
Conventions: tick U = exp(-iH), quasi-energy w = -arg(eig); K per cube; shift b in cubes per tick (normals move at -b);
coarse Bloch Q = 2K on blocks of 2x2x2 cubes (site-attached labels; second block tiling offset by one cube).
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/CUBE_TICK_CANNOT_CARRY_THE_SHIFT_AND_A_BLOCK_RUNG_INSERTION_READS_SHIFT_AND_SHEAR_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm
from scipy.spatial.transform import Rotation

T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
rng = np.random.default_rng(20261021)

# ------------------------------------------------------------------ cube algebra (CL-1 hop with spin-3/2 phases)
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8, dtype=complex)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); NV = (2 * C8 - 1.0) / r3; XI = []
for i in range(8):
    _, v_ = np.linalg.eigh(sum(NV[i, k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex); WAX = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(a + 1, 8):
        if np.sum(abs(C8[a] - C8[b])) == 1:
            g_ = XI[a].conj() @ XI[b]; x = -g_ / abs(g_) / r3; ax = int(np.argmax(abs(C8[a] - C8[b])))
            for Mx in (W, WAX[ax]): Mx[a, b] = x; Mx[b, a] = np.conj(x)
NN = [np.diag(C8[:, i]).astype(complex) for i in range(3)]
def dK(i, X): return 1j * (NN[i] @ X - X @ NN[i])                     # K_i-derivative of D X D^dag at K = 0
GA = [r3 * X for X in WAX]; GP = [dK(i, GA[i]) for i in range(3)]; VOL = GA[0] @ GA[1] @ GA[2]
def DK(K): return np.diag(np.exp(1j * (C8 @ np.asarray(K, float))))
def Rf(f): f = np.asarray(f, float); return sum(f[i] * WAX[i] for i in range(3)) / np.sqrt(f @ f / 3)
def s3f(f): return 1j * VOL @ Rf(f)                                    # copy sign; light copy s3 = +1
S3 = s3f([1, 1, 1]); PL = (I8 + S3) / 2; PH = (I8 - S3) / 2
ROTS, LROT = [], []
for g in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        Gm = np.zeros((3, 3)); Gm[range(3), g] = s
        if np.linalg.det(Gm) < 0: continue
        rv = Rotation.from_matrix(Gm).as_rotvec(); Dm = expm(-1j * sum(rv[i] * J3[i] for i in range(3)))
        sig = [int(np.argmin(np.abs(NV - Gm @ NV[a]).sum(1))) for a in range(8)]; V = np.zeros((8, 8), complex)
        for a in range(8): V[sig[a], a] = XI[sig[a]].conj() @ Dm @ XI[a]
        ROTS.append(Gm); LROT.append(V)
ODD = [int(round(np.trace(Rm))) == 1 or (int(round(np.trace(Rm))) == -1 and not np.allclose(abs(np.diag(Rm)), 1)) for Rm in ROTS]
def halves(f, eps, mu, M, mode='even'):
    """CL-1 half-ticks; copy mass M on the s3 = -1 copy: 'even' = wrapped around the even half-tick (both halves),
    'every' = applied by every cube in every half-tick (the literal old text)."""
    R = Rf(f); P = (I8 - s3f(f)) / 2; F = expm(1j * (M / 2) * P @ R)
    Ee, Eo = expm(-1j * (eps - mu / 2) * R), expm(1j * (eps + mu / 2) * R)
    return (F @ Ee @ F, Eo) if mode == 'even' else (Ee @ F, Eo @ F)
def fineU(K, f, eps, mu, M, mode='even'):
    Ue, Uo = halves(f, eps, mu, M, mode); Dm = DK(K); return Dm @ Uo @ Dm.conj().T @ Ue
def lightpos(U, Pl=PL):
    ev, V = np.linalg.eig(U); w = -np.angle(ev); lw = np.linalg.norm(Pl @ V, axis=0)
    return np.sort(w[(lw > 0.7) & (w > 0)])

# ------------------------------------------------------------------ A. cube rung
print('== A. cube rung (2^3)')
V6 = GA + GP
cl = max(nrm(V6[a] @ V6[b] + V6[b] @ V6[a] - 2 * (a == b) * I8) for a in range(6) for b in range(6))
s3sum = 1j * r3 * (WAX[1] @ WAX[2] + WAX[2] @ WAX[0] + WAX[0] @ WAX[1])
keep = max(nrm(L @ S3 @ L.conj().T - (-S3 if o else S3)) for L, o in zip(LROT, ODD))
comm = max(nrm(S3 @ X - X @ S3) for X in GP + [W])
iC3 = [i for i, Rm in enumerate(ROTS) if np.allclose(Rm @ [1., 0, 0], [0, 1., 0]) and np.allclose(Rm @ [1., 1, 1], [1., 1, 1])][0]
Sg = [-1j * GP[1] @ GP[2], -1j * GP[2] @ GP[0], -1j * GP[0] @ GP[1]]
Mr = np.array([[np.trace(LROT[iC3] @ GP[a] @ LROT[iC3].conj().T @ GP[b]).real / 8 for b in range(3)] for a in range(3)])
rv = Rotation.from_matrix(np.round(Mr).T).as_rotvec(); best = None
for sg in (1, -1):
    Sl = expm(-1j * sg * np.linalg.norm(rv) / 2 * sum(rv[k] / np.linalg.norm(rv) * Sg[k] for k in range(3)))
    e_ = max(nrm(Sl @ X @ Sl.conj().T - LROT[iC3] @ X @ LROT[iC3].conj().T) for X in GP + [W])
    if best is None or e_ < best[0]: best = (e_, Sl)
rho = best[1].conj().T @ LROT[iC3]; om = np.exp(2j * np.pi / 3)
light_is_w2 = abs(np.trace(PL @ rho) - 4 * om ** 2) < 1e-9 and abs(np.trace(PH @ rho) - 4 * om) < 1e-9
check('A1 sqrt3 W_i and i[N_i, sqrt3 W_i]: six anticommuting generators; copy sign s3 = i sqrt3 sum W_jW_k commutes with the light Dirac algebra, kept by the 12 tetrahedral turns, flipped by the 12 odd; light copy = e^(4 pi i/3) copy', cl < 1e-13 and nrm(s3sum - S3) < 1e-13 and keep < 1e-13 and comm < 1e-13 and light_is_w2,
      f'{max(cl, keep, comm):.0e}')
# A2 flow theorem: det U(K) is K-independent for ANY pair of cube unitaries
def randU(n=8): Z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); Q, R_ = np.linalg.qr(Z); return Q * (np.diag(R_) / abs(np.diag(R_)))
fl = 0
for _ in range(4):
    Ue, Uo = randU(), randU(); ws = [np.sum(np.angle(np.linalg.eigvals(DK(K) @ Uo @ DK(K).conj().T @ Ue))) % (2 * np.pi) for K in rng.uniform(-np.pi, np.pi, (6, 3))]
    fl = max(fl, np.ptp(np.angle(np.exp(1j * np.array(ws)))))
check('A2 theorem (flow): det U(K) = det U_o det U_e for every reading, so the 8 quasi-energies sum to a constant at each K: a -b drag needs +b on 4 other bands; no copy-blind cube reading tilts the cone',
      fl < 1e-12, f'random cube unitaries: spread of sum w {fl:.0e}')
# A3 reflection theorem: with reflection half-ticks the first-order Hamiltonian anticommutes with R
ac = 0
for _ in range(4):
    Z = randU(); R = Z @ np.diag([1.] * 4 + [-1.] * 4) @ Z.conj().T; e_ = 0.4; Ue, Uo = expm(-1j * e_ * R), expm(1j * e_ * R)
    Hs = [-(NN[i] - Uo.conj().T @ NN[i] @ Uo) for i in range(3)]; Hs = [Ue.conj().T @ H @ Ue for H in Hs]
    ac = max(ac, max(nrm(H @ R + R @ H) for H in Hs))
check('A3 theorem: with reflection half-ticks and the light content exact at rest, first-order velocities anticommute with R: +- symmetric spectrum, no shift', ac < 1e-12, f'random reflections: max |{{H_i, R}}| {ac:.0e}')
# A4 shear-sign theorem: diagonal of {H_1, H_2} is >= 0 on main-diagonal corners, <= 0 on anti-diagonal corners
sgn_ok = True; mx = 0
for _ in range(6):
    V = randU(); Hs = [V.conj().T @ NN[i] @ V - NN[i] for i in range(3)]; d12 = np.real(np.diag(Hs[0] @ Hs[1] + Hs[1] @ Hs[0]))
    main = C8[:, 0] == C8[:, 1]; sgn_ok &= bool(np.all(d12[main] > -1e-13) and np.all(d12[~main] < 1e-13)); mx = max(mx, abs(d12).max())
check('A4 theorem (shear sign), any copy-blind massless reading, any step: diag {H1,H2} >= 0 on face-main-diagonal corners, <= 0 on the rest, so no scalar K1K2 term: two degenerate copies cannot be sheared',
      sgn_ok and mx > 1e-3, f'6 random readings, |diag| up to {mx:.2f}')
# A5 exact-at-rest insertions at the cube rung: image of X -> (P_L d_i X P_L)_i in Dirac coordinates
u_, _, _ = np.linalg.svd(PL); BL = u_[:, :4]; L4 = lambda X: BL.conj().T @ X @ BL
al = [L4(g) for g in GP]; be = L4(W); Om = al[0] @ al[1] @ al[2] @ be; Sgl = [L4(s) for s in Sg]
names = ['1'] + [f'a{i}' for i in range(3)] + ['b'] + [f'iba{i}' for i in range(3)] + [f'S{i}' for i in range(3)] + [f'bS{i}' for i in range(3)] + ['Om', 'iOmb']
basis = [np.eye(4)] + al + [be] + [1j * be @ a for a in al] + Sgl + [be @ s for s in Sgl] + [Om, 1j * Om @ be]
coords = lambda Mx: np.array([np.trace(B.conj().T @ Mx).real / 4 for B in basis])
HB = []
for a in range(8):
    for b in range(a, 8):
        E = np.zeros((8, 8), complex)
        if a == b: E[a, a] = 1; HB.append(E); continue
        E[a, b] = E[b, a] = 1; HB.append(E.copy()); E = np.zeros((8, 8), complex); E[a, b] = -1j; E[b, a] = 1j; HB.append(E)
Am = np.array([np.concatenate([coords(L4(dK(i, E))) for i in range(3)]) for E in HB]).T
rk = np.linalg.matrix_rank(Am, 1e-9); Uu, ss, _ = np.linalg.svd(Am); Img = Uu[:, :rk]
def tv(spec):
    v = np.zeros(48)
    for i, nm, c in spec: v[16 * i + names.index(nm)] += c
    return v
res = lambda t: np.linalg.norm(t - Img @ (Img.T @ t)) / np.linalg.norm(t)
shear_ok = max(res(tv([(0, 'a1', 1), (1, 'a0', 1)])), res(tv([(0, 'a0', 1)])), res(tv([(0, 'a1', 1), (1, 'a0', -1)])))
base = tv([(0, '1', 1)]); oth = [tv([(i, nm, 1)]) for i in range(3) for nm in names if not (i == 0 and nm == '1')]
Mo = np.stack([o - Img @ (Img.T @ o) for o in oth], 1); cf = np.linalg.lstsq(Mo, -(base - Img @ (Img.T @ base)), rcond=None)[0]
lab = [(i, nm) for i in range(3) for nm in names if not (i == 0 and nm == '1')]; acc_ = {lab[k]: cf[k] for k in range(len(cf)) if abs(cf[k]) > 1e-8}
lock = set(acc_) == {(1, 'S2'), (2, 'S1')} and all(abs(abs(v) - r3 / 2) < 1e-9 for v in acc_.values())
check('A5 theorem (cube rung): exact-at-rest readings are insertions S, S^-1 across the two tilings; light image rank 40/48 holds every stretch, shear, rotation, but the shift only with (sqrt3/2)(K2 S3 + K3 S2) per unit K1 shift', rk == 40 and shear_ok < 1e-12 and abs(res(base) - np.sqrt(0.6)) < 1e-9 and lock,
      f'rank {rk}; pure-shift residual {res(base):.4f} = sqrt(3/5); partner coefficients ' + ', '.join(f'{v:+.4f}' for v in acc_.values()))
# A6 copy-mass placement
spl = {}
for mode in ('every', 'even'):
    out = []
    for k in (0.04, 0.08):
        p = lightpos(fineU(k * np.array([0.267, 0.535, 0.802]), [1, 1, 1], 0.3, 0.0, 0.5, mode)); out.append(p[1] - p[0])
    spl[mode] = out
rest = [np.sort(np.abs(np.angle(np.linalg.eigvals(fineU(np.zeros(3), [1, 1, 1], 0.3, 0.1, 0.5, m))))) for m in ('every', 'even')]
check("A6 copy mass in every half-tick (old text) splits light helicities as K^2 off the axes; wrapped around the even half-tick (the copy-mass probe's form) no splitting, same rest phases", np.log2(spl['every'][1] / spl['every'][0]) > 1.95 and max(spl['even']) < 1e-13 and nrm(rest[0] - rest[1]) < 1e-12,
      f"every: {spl['every'][1]:.2e} at |K| .08 (slope {np.log2(spl['every'][1]/spl['every'][0]):.2f}); even: {max(spl['even']):.0e}")

# ------------------------------------------------------------------ B. block rung: the frame insertion
print('== B. block rung: 2x2x2 blocks of cubes, two block tilings offset by one cube')
NC = C8.copy(); I2 = np.eye(2); SY = np.array([[0, -1j], [1j, 0]])
JC = [np.kron(np.kron(*(SY if q == i else I2 for q in (0, 1))), SY if i == 2 else I2) for i in range(3)]   # sigma_y on cube index n_i
IDX = lambda n, c: 8 * int(n @ [4, 2, 1]) + int(c @ [4, 2, 1])
ODDS = [([IDX((n0 + 1 - c) % 2, c) for c in C8], ((n0 == 1) & (C8 == 0)).astype(float)) for n0 in NC]
DCM = np.repeat((NC == 0).astype(float), 8, axis=0)
def oddcoarse(Q, Uo):
    U = np.zeros((64, 64), complex)
    for ids, mask in ODDS:
        ph = np.exp(1j * mask @ Q); U[np.ix_(ids, ids)] = ph.conj()[:, None] * Uo * ph[None, :]
    return U
def coarseU(Q, Ue, Uo, X):
    SA = expm(-1j * X); d = np.exp(1j * DCM @ np.asarray(Q, float))
    return oddcoarse(Q, Uo) @ (d.conj()[:, None] * SA.conj().T * d[None, :]) @ SA @ np.kron(np.eye(8), Ue)
def Vops(f, eps):
    E = expm(-1j * eps * Rf(f)); return [NN[j] - E @ NN[j] @ E.conj().T for j in range(3)]
def Xins(b, sig, f, eps):
    """frame insertion: X = sum_i J_i (x) [ -theta_i + (1/4) sum_j sig_ij (f_i/f_j) V_j ], sin 2 theta_i = b_i (exact drift),
    V_j = N_j - e^{-i eps R} N_j e^{i eps R} (the odd half-tick's displacement along j)"""
    V = Vops(f, eps); f = np.asarray(f, float); th = np.arcsin(np.asarray(b, float)) / 2
    return sum(np.kron(JC[i], -th[i] * I8 + 0.25 * sum(sig[i, j] * f[i] / f[j] * V[j] for j in range(3) if j != i)) for i in range(3))
EMB = lambda K: np.exp(1j * NC @ K) / np.sqrt(8)
def tracked(K, f, eps, mu, M, X):
    Ue, Uo = halves(f, eps, mu, M); Dm = DK(K); ev, vf = np.linalg.eig(Dm @ Uo @ Dm.conj().T @ Ue); wf = -np.angle(ev)
    lw = np.linalg.norm((I8 + s3f(f)) / 2 @ vf, axis=0); evc, vc = np.linalg.eig(coarseU(2 * K, Ue, Uo, X)); wc = -np.angle(evc)
    jj = [int(np.argmax(np.abs(vc.conj().T @ np.kron(EMB(K), vf[:, j])))) for j in range(8)]
    return wf, wc[jj], lw
# B1 zoom: the block-rung image is complete
u64 = np.zeros((64, 8)); u64[np.arange(64), np.arange(64) % 8] = 1 / np.sqrt(8); BL64 = u64 @ BL
rows = []; BB = np.array(basis)
for i in range(3):
    dl = DCM[:, i]; Dd = dl[:, None] - dl[None, :]
    blk = np.einsum('ak,bl->abkl', BL64.conj(), BL64)            # (P_L E_ab P_L)_{kl}
    Ms = (-1j * Dd[:, :, None, None] * blk).reshape(-1, 4, 4); Mh = Ms.conj().transpose(0, 2, 1)
    re = np.concatenate([np.einsum('kij,nij->nk', BB.conj(), Ms + Mh).real, np.einsum('kij,nij->nk', BB.conj(), 1j * (Ms - Mh)).real], 0) / 4
    rows.append(re)
A64 = np.concatenate(rows, 1).T; rk64 = np.linalg.matrix_rank(A64, 1e-8)
check("B1 zoom: insertions on blocks of 2x2x2 cubes (2nd block tiling offset by one cube) reach all 48 light terms, the pure shift included: moving whole cubes keeps each site's overlap state", rk64 == 48, f'rank {rk64}')
# B2 explicit insertion: exact at rest, uniform tilt -b.K for every species and both copies
f1 = np.array([1.0, 0.93, 1.08]); e1 = 0.3; b1 = np.array([0.013, -0.007, 0.021]); M1 = 0.5
sg1 = np.array([[0, .012, -.008], [.012, 0, .005], [-.008, .005, 0]])
X1 = Xins(b1, sg1, f1, e1); ex0 = 0
for mu in (0.0, 0.1):
    Ue, Uo = halves(f1, e1, mu, M1); ex0 = max(ex0, nrm(coarseU(np.zeros(3), Ue, Uo, X1) - coarseU(np.zeros(3), Ue, Uo, 0 * X1)))
rat = {'light': [], 'heavy': []}; hel = 0
for mu in (0.0, 0.1):
    for _ in range(4):
        n = rng.normal(size=3); n /= np.linalg.norm(n); K = 2e-3 * n
        wf, wc, lw = tracked(K, f1, e1, mu, M1, Xins(b1, 0 * sg1, f1, e1))
        for j in range(8): rat['light' if lw[j] > 0.9 else 'heavy'].append((wc[j] - wf[j]) / (-b1 @ K))
        p = np.sort(wc[(lw > 0.9) & (wc > 0)]); hel = max(hel, abs(p[1] - p[0]) if mu == 0 else 0)
dets = [np.sum(np.angle(np.linalg.eigvals(coarseU(Q, *halves(f1, e1, 0.1, M1), X1)))) for Q in rng.uniform(-np.pi, np.pi, (3, 3))]
check('B2 X = sum_i J_i (x) (-theta_i + shear), sin 2theta_i = b_i, J_i the cube-pair current, on block tiling 1 after the even half-tick, undone on tiling 2: rest phases exact; all species, both copies drift by -b; det constant',
      ex0 < 1e-13 and max(abs(np.array(rat['light']) - 1)) < 3e-4 and max(abs(np.array(rat['heavy']) - 1)) < 3e-4 and hel < 1e-10 and np.ptp(np.angle(np.exp(1j * np.array(dets)))) < 1e-10,
      f"rest {ex0:.0e}; tilt/(-b.K): light {min(rat['light']):.5f}..{max(rat['light']):.5f}, heavy {min(rat['heavy']):.5f}..{max(rat['heavy']):.5f}; helicity split {hel:.0e}")
# B3 shear (with shift, anisotropic box): fitted light cone vs target; a massive species
DIRS = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1], [0, 1, 1], [0, 1, -1], [1, 1, 1], [1, -1, 1], [-1, 1, 1]], float)
DIRS /= np.linalg.norm(DIRS, axis=1)[:, None]
def wpos(K, Ue, Uo, X, ref):
    w = -np.angle(np.linalg.eigvals(coarseU(2 * K, Ue, Uo, X))); return np.mean(np.sort(w[np.argsort(np.abs(np.angle(np.exp(1j * (w - ref)))))[:2]]))
def fit_metric(f, eps, mu, M, X, k=1e-3):
    """lattice-measured tilt b and cone G from the positive light pair: (w + b.K)^2 - w0^2 = G_ij K_i K_j"""
    Ue, Uo = halves(f, eps, mu, M); Pl = (I8 + s3f(f)) / 2
    ref = lambda K: lightpos(DK(K) @ Uo @ DK(K).conj().T @ Ue, Pl).mean()
    b = np.array([-(wpos(k * e, Ue, Uo, X, ref(k * e)) - wpos(-k * e, Ue, Uo, X, ref(-k * e))) / (2 * k) for e in np.eye(3)])
    w0 = wpos(np.zeros(3), Ue, Uo, X, mu) if mu else 0.0
    A = np.array([[n[0]**2, n[1]**2, n[2]**2, 2*n[0]*n[1], 2*n[0]*n[2], 2*n[1]*n[2]] for n in DIRS])
    y = np.array([((wpos(k * n, Ue, Uo, X, ref(k * n)) + k * b @ n) ** 2 - w0 ** 2) / k ** 2 for n in DIRS])
    s_ = np.linalg.lstsq(A, y, rcond=None)[0]; return b, np.array([[s_[0], s_[3], s_[4]], [s_[3], s_[1], s_[5]], [s_[4], s_[5], s_[2]]])
v1 = np.sin(e1) / r3 * f1 / np.sqrt(np.mean(f1 ** 2)); errs = []
for sc in (1.0, 0.1):
    Xs = Xins(sc * b1, sc * sg1, f1, e1); _, G0 = fit_metric(f1, e1, 0.0, M1, 0 * X1); bF, GF = fit_metric(f1, e1, 0.0, M1, Xs)
    tgt = np.outer(v1, v1) * sc * sg1; errs.append((np.abs(bF - sc * b1).max() / np.abs(sc * b1).max(), np.abs(GF - G0 - tgt).max() / np.abs(tgt).max()))
mu_m = 0.05; _, G0m = fit_metric(f1, e1, mu_m, M1, 0 * X1); _, GFm = fit_metric(f1, e1, mu_m, M1, Xins(0 * b1, 0.1 * sg1, f1, e1))
ratm = ((GFm - G0m) / np.sqrt(np.outer(np.diag(G0m), np.diag(G0m))))[np.triu_indices(3, 1)] / (0.1 * sg1[np.triu_indices(3, 1)])
cm2 = (np.cos(mu_m) - np.cos(2 * e1)) / 6 * mu_m / np.sin(mu_m) / (np.sin(e1) ** 2 / 3)
pr = np.sin(e1 + mu_m / 2) / (np.sin(e1) * np.cos(mu_m / 2)) / cm2
check('B3 anisotropic box + shift + shear: (w + b.K)^2 = v_i v_j (1 + sigma)_ij K_i K_j, errors second order; massive shear weight sin(eps+mu/2)/(sin eps cos(mu/2))/(c_m/c)^2 = 1 + O(mu/eps)', errs[1][0] < 2e-4 and errs[1][1] < 1e-3 and errs[0][1] / errs[1][1] > 5 and np.all(np.abs(ratm / pr - 1) < 2e-3),
      f'(tilt, shear) err at 1x {errs[0][0]:.0e},{errs[0][1]:.0e}; at 0.1x {errs[1][0]:.0e},{errs[1][1]:.0e}; mu/eps 1/6: {ratm.mean():.4f} vs {pr:.4f}')
# B4 covariance: 24 rotations about the block centre act as P_g (x) L_g
def Pcube(Rm):
    P = np.zeros((8, 8))
    for a, n in enumerate(NC):
        n2 = np.rint((Rm @ (2 * n - 1) + 1) / 2).astype(int); P[int(n2 @ [4, 2, 1]), a] = 1
    return P
cvX = cvT = 0; cvO = []
f_iso = np.ones(3); Xb = Xins(b1, sg1, f_iso, e1); Qr = rng.uniform(-1, 1, 3)
for Rm, L, o in zip(ROTS, LROT, ODD):
    Gg = np.kron(Pcube(Rm), L); cvX = max(cvX, nrm(Gg @ Xb @ Gg.conj().T - Xins(Rm @ b1, Rm @ sg1 @ Rm.T, f_iso, e1)))
    for M_ in (0.0, 0.5):
        Ue, Uo = halves(f_iso, e1, 0.1, M_)
        d_ = nrm(Gg @ coarseU(Qr, Ue, Uo, Xb) @ Gg.conj().T - coarseU(Rm @ Qr, Ue, Uo, Xins(Rm @ b1, Rm @ sg1 @ Rm.T, f_iso, e1)))
        if M_ == 0 or not o: cvT = max(cvT, d_)
        else: cvO.append(d_)
Pinv = Pcube(-np.eye(3)); jodd = max(nrm(Pinv @ J @ Pinv.T + J) for J in JC)
check('B4 covariance: insertion is a vector/tensor under the 24 block rotations; tick with copy mass keeps the 12 tetrahedral (24 at M = 0); J_i is odd under inversion: the inversion-odd piece', cvX < 1e-12 and cvT < 1e-11 and min(cvO) > 1e-3 and jodd < 1e-15,
      f'insertion {cvX:.0e}, tick {cvT:.0e}, odd turns with M: >= {min(cvO):.2f}')

# ------------------------------------------------------------------ C. dynamics on lattice lines
print('== C. packets (one real axis, Bloch along the others)')
class Line:
    def __init__(self, Nr, ra, coarse, Kb, eps, mu, M, Xfun=None, breal=None):
        """ra: real axis; coarse: tuple of coarse axes (Bloch Q = 2K, cube pairs); remaining axis fine Bloch K.
        Xfun(p) -> insertion on (cube index of coarse axes) x corners at real-axis cube p; breal: shift along ra per pair."""
        self.N, self.ra, self.co = Nr, ra, tuple(coarse); self.fi = [a for a in range(3) if a != ra and a not in coarse]
        self.Ue, self.Uo = halves([1, 1, 1], eps, mu, M); nc = len(coarse); self.nd = 2 ** nc; self.Kb = np.asarray(Kb, float)
        ncs = np.array(list(itertools.product((0, 1), repeat=nc))) if nc else np.zeros((1, 0), int)
        self.ncs = ncs; Q = 2 * self.Kb
        mr = np.arange(Nr)[:, None, None]; cr = C8[:, ra][None, None, :]
        self.pr = np.broadcast_to((mr + 1 - cr) % Nr, (Nr, self.nd, 8))
        nidx = np.zeros((self.nd, 8), int); ph = np.ones((self.nd, 8), complex)
        for q, n0 in enumerate(ncs):
            for c in range(8):
                nn = [(n0[k] + 1 - C8[c, a]) % 2 for k, a in enumerate(coarse)]
                nidx[q, c] = int(sum(v << (nc - 1 - k) for k, v in enumerate(nn)))
                ph[q, c] = np.exp(1j * sum(Q[a] * (n0[k] == 1) * (C8[c, a] == 0) for k, a in enumerate(coarse)) - 1j * sum(self.Kb[a] * C8[c, a] for a in self.fi))
        self.ni = np.broadcast_to(nidx[None], (Nr, self.nd, 8)); self.ph = np.broadcast_to(ph[None], (Nr, self.nd, 8)); self.cc = np.broadcast_to(np.arange(8)[None, None], (Nr, self.nd, 8))
        self.dB = np.repeat(np.exp(1j * sum(Q[a] * (ncs[:, k] == 0) for k, a in enumerate(coarse))) if nc else np.ones(1), 8)
        self.SA = None if Xfun is None else np.array([expm(-1j * Xfun(p)) for p in range(Nr)])
        self.Rr = None if breal is None else np.array([[[np.cos(b / 2), np.sin(b / 2)], [-np.sin(b / 2), np.cos(b / 2)]] for b in breal])
    def tick(self, a):
        N, nd = self.N, self.nd
        a = np.einsum('ij,xnj->xni', self.Ue, a)
        if self.SA is not None:
            v = a.reshape(N, nd * 8); v = np.einsum('xij,xj->xi', self.SA, v)
            v = v * self.dB[None]; v = np.einsum('xji,xj->xi', self.SA.conj(), v); v = v * self.dB.conj()[None]; a = v.reshape(N, nd, 8)
        if self.Rr is not None:
            for st in (0, 1):
                lo = np.arange(st, N, 2); hi = (lo + 1) % N; Rm = self.Rr[lo]; al_, ah = a[lo].copy(), a[hi].copy()
                a[lo] = Rm[:, 0, 0, None, None] * al_ + Rm[:, 0, 1, None, None] * ah; a[hi] = Rm[:, 1, 0, None, None] * al_ + Rm[:, 1, 1, None, None] * ah
        g = a[self.pr, self.ni, self.cc] * self.ph; g = np.einsum('ij,xnj->xni', self.Uo, g) * self.ph.conj()
        b = np.empty_like(a); b[self.pr, self.ni, self.cc] = g; return b
    def pos(self, a):
        p = np.abs(a) ** 2; x = np.arange(self.N)[:, None, None] + C8[:, self.ra][None, None, :] / 2.0; return (p * x).sum() / p.sum()
def Xsub(b, sig, co, eps):
    """the frame insertion restricted to the coarse axes co (isotropic box), on (cube index of co) x corners"""
    V = Vops([1, 1, 1], eps); nc = len(co); X = 0
    for k, i in enumerate(co):
        J = np.kron(np.kron(np.eye(2 ** k), SY), np.eye(2 ** (nc - 1 - k)))
        X = X + np.kron(J, -np.arcsin(b[i]) / 2 * I8 + 0.25 * sum(sig[i, j] * V[j] for j in range(3) if j != i))
    return X
def packet(ln, x0, sg, eps, mu, M, chi):
    a = np.zeros((ln.N, ln.nd, 8), complex); m = np.arange(ln.N)
    namp = np.exp(1j * ln.ncs @ ln.Kb[list(ln.co)]) if ln.co else np.ones(1)
    for j in range(ln.N):
        Kr = (2 * np.pi * j / ln.N + np.pi) % (2 * np.pi) - np.pi; gw = np.exp(-(Kr * sg) ** 2 / 2)
        if gw < 1e-13: continue
        K = ln.Kb.copy(); K[ln.ra] = Kr; ev, V = np.linalg.eig(fineU(K, [1, 1, 1], eps, mu, M)); w = -np.angle(ev)
        sel = (np.linalg.norm(PL @ V, axis=0) > 0.9) & (w > 0); Qb, _ = np.linalg.qr(V[:, sel]); c = Qb @ (Qb.conj().T @ chi)
        a += gw * np.exp(1j * Kr * (m - x0))[:, None, None] * namp[None, :, None] * (c / np.linalg.norm(c))[None, None, :]
    return a / np.linalg.norm(a)
def accel(ln, a, T):
    xs = [ln.pos(a)]
    for _ in range(T): a = ln.tick(a); xs.append(ln.pos(a))
    return 2 * np.polyfit(np.arange(T + 1), np.array(xs) - xs[0], 2)[0]
def wband(K, mu, M, eps=0.3):
    return lightpos(fineU(np.asarray(K, float), [1, 1, 1], eps, mu, M)).mean()
chi0 = rng.normal(size=8) + 1j * rng.normal(size=8); Nl, e0, gs = 1024, 0.3, 2e-5; xc = Nl / 2
def saw(x, X0=420):
    x = (x + Nl / 2) % Nl - Nl / 2; return np.where(np.abs(x) <= X0, x, np.sign(x) * X0 - (x - np.sign(x) * X0) * 2 * X0 / (Nl - 2 * X0))
# C1 gravitomagnetic: b_y(x) (B_z = db_y/dx) vs curl-free b_x(x); packet moving along y
gm = []
for mu, Ky in ((0.0, 0.15), (0.06, 0.15)):
    h = 2e-3; wxx = (wband([h, Ky, 0], mu, M1) - 2 * wband([0, Ky, 0], mu, M1) + wband([-h, Ky, 0], mu, M1)) / h ** 2
    vy = (wband([0, Ky + 1e-5, 0], mu, M1) - wband([0, Ky - 1e-5, 0], mu, M1)) / 2e-5
    pred = gs * Ky * wxx; aa = []
    for sg in (50.0, 100.0):
        by = gs * saw(np.arange(Nl) - xc)
        ln = Line(Nl, 0, (1,), [0, Ky, 0], e0, mu, M1, Xfun=lambda p, by=by: Xsub([0, by[p], 0], np.zeros((3, 3)), (1,), e0))
        aa.append(accel(ln, packet(ln, xc, sg, e0, mu, M1, chi0), 300))
    ext = (4 * aa[1] - aa[0]) / 3
    lg = Line(Nl, 0, (1,), [0, Ky, 0], e0, mu, M1, breal=gs * saw(np.arange(Nl) + 0.5 - xc)); ag = accel(lg, packet(lg, xc, 100.0, e0, mu, M1, chi0), 300)
    gm.append((ext / pred, ag / pred, vy * Ky * wxx / (vy ** 2) if mu == 0 else 0, gs * vy / pred))
check('C1 gravitomagnetism: a packet moving along y in b_y(x) is pushed along x at g K_y w_xx (eikonal of w - b.K; v x curl b as K -> 0); curl-free b_x(x) pushes nothing',
      all(abs(r[0] - 1) < 0.01 and abs(r[1]) < 1e-3 for r in gm),
      'massless, massive: lattice/eikonal ' + ', '.join(f'{r[0]:.4f}' for r in gm) + '; curl-free/curl ' + ', '.join(f'{r[1]:.0e}' for r in gm)
      + '; eikonal/(g v_y) ' + ', '.join(f'{1/r[3]:.4f}' for r in gm))
# C2 light bent by a shear gradient: h_xy(z) = g saw(z) (sigma_xy = -h_xy); massless packet along (1, +-1, 0)
cs = []
for sgn in (1, -1):
    k0 = 0.15; Kb = np.array([k0, sgn * k0, 0]) / np.sqrt(2); Ue, Uo = halves([1, 1, 1], e0, 0.0, M1); s_ = 1e-5
    S1 = np.zeros((3, 3)); S1[0, 1] = S1[1, 0] = s_
    dw = (wpos(Kb, Ue, Uo, Xins(np.zeros(3), S1, [1, 1, 1], e0), wband(Kb, 0, M1)) - wpos(Kb, Ue, Uo, 0 * X1, wband(Kb, 0, M1))) / s_
    h = 2e-3; wzz = (wband(Kb + [0, 0, h], 0, M1) - 2 * wband(Kb, 0, M1) + wband(Kb - [0, 0, h], 0, M1)) / h ** 2
    pred = wzz * dw * gs; aa = {}
    for lab, on in (('full', True), ('box', False)):
        acc_s = []
        for sg in ((50.0, 100.0) if on else (100.0,)):
            sig_p = lambda p: (lambda v: np.array([[0, v, 0], [v, 0, 0], [0, 0, 0]]))(-gs * saw(np.array(p) - xc))
            ln = Line(Nl, 2, (0, 1), Kb, e0, 0.0, M1, Xfun=(lambda p: Xsub(np.zeros(3), sig_p(p), (0, 1), e0)) if on else None)
            acc_s.append(accel(ln, packet(ln, xc, sg, e0, 0.0, M1, chi0), 300))
        aa[lab] = (4 * acc_s[1] - acc_s[0]) / 3 if on else acc_s[0]
    cs.append((aa['full'] / pred, aa['box'] / pred, dw / (np.sin(e0) / r3 * k0 / 2)))
check('C2 light in h_xy(z): packets along (1,+-1,0) bend along z at the eikonal rate with opposite signs; the box reading does not bend them',
      all(abs(c[0] - 1) < 0.01 and abs(c[1]) < 1e-6 for c in cs) and cs[0][2] * cs[1][2] < 0,
      'lattice/eikonal ' + ', '.join(f'{c[0]:.4f}' for c in cs) + '; box ' + ', '.join(f'{c[1]:.0e}' for c in cs)
      + '; dw/dsigma over continuum v k/2: ' + ', '.join(f'{c[2]:+.4f}' for c in cs))

# ------------------------------------------------------------------ D. coordinator checks
print('== D. coordinator checks')
TAU0 = np.sin(e0) / r3; GMs = 1e-6
def h_rad(x, gm=GMs):
    r = np.linalg.norm(x); n = x / r; return 2 * gm / r, 2 * gm * np.outer(n, n) / r, np.zeros(3)
def eta2(x):
    r = np.linalg.norm(x); X, Y, Z = x; return np.array([X / r - X * Y * Y / r ** 3, -Y / r + X * X * Y / r ** 3, 0.0])
def h_two(x, gm=GMs, c=0.7, d=1e-6):
    h00, hij, h0 = h_rad(x, gm); r = np.linalg.norm(x); Jx = np.zeros((3, 3))
    for i in range(3):
        e = np.zeros(3); e[i] = d * r; Jx[i] = (eta2(x + e) - eta2(x - e)) / (2 * d * r)
    return h00, hij + c * gm * (Jx + Jx.T), h0
def reading(h00, hij, h0i, box=False):
    """cube reading of a weak metric g = eta + h (signature -+++, lattice time in flat proper ticks): lapse, shift, inverse
    spatial metric -> box (f, eps), shift b (cubes per tick), shear sigma"""
    g = np.diag([-1.0, 1, 1, 1]); g[0, 0] += h00; g[1:, 1:] += hij; g[0, 1:] = g[1:, 0] = h0i; gi = np.linalg.inv(g)
    N = 1 / np.sqrt(-gi[0, 0]); beta = -gi[0, 1:] / gi[0, 0]; gup = gi[1:, 1:] + np.outer(beta, beta) / N ** 2
    if box: f = 1 / np.sqrt(np.diag(g[1:, 1:])); N = np.sqrt(-g[0, 0])
    else: f = np.sqrt(np.diag(gup))
    eps = np.arcsin(r3 * TAU0 * N * np.sqrt(np.mean(f ** 2))); sig = gup / np.outer(f, f); np.fill_diagonal(sig, 0)
    return f, eps, (np.zeros(3) if box else TAU0 * beta), (0 * sig if box else sig)
def speed_deficit(hf, x, k, box, ks=1e-3):
    """local linear response, measured on the lattice with the field rescaled to h00 = 1e-5 at x (the reading is local)"""
    gl = 5e-6 * np.linalg.norm(x); f, eps, b, sig = reading(*hf(x, gl), box=box); Ue, Uo = halves(f, eps, 0.0, M1); K = ks * k
    ref = wband(K, 0.0, M1, e0)
    w = (wpos(K, Ue, Uo, Xins(b, sig, f, eps), ref) if not box else lightpos(DK(K) @ Uo @ DK(K).conj().T @ Ue, (I8 + s3f(f)) / 2).mean())
    return (1 - w / ref) * GMs / gl
ug, wg = np.polynomial.legendre.leggauss(40)
def shapiro(hf, k, e, b, box, lat=True, L=1e4, off=None):
    U = np.arcsinh(L / b); tot = 0; off = np.zeros(3) if off is None else off
    for lo, hi in ((-U, -3), (-3, 3), (3, U)):
        u = (hi - lo) / 2 * ug + (hi + lo) / 2; wq = (hi - lo) / 2 * wg
        for uu, ww in zip(u, wq):
            x = b * e + off + b * np.sinh(uu) * k
            if lat: dlt = speed_deficit(hf, x, k, box)
            else:
                h00, hij, _ = hf(x); hb = np.diag(np.diag(hij)) if box else hij; dlt = (h00 + k @ hb @ k) / 2
            tot += ww * dlt * b * np.cosh(uu)
    return tot
def opg(hf, k, e, box, lat=True): return -(shapiro(hf, k, e, 2.0, box, lat) - shapiro(hf, k, e, 1.0, box, lat)) / np.log(2) / 2 / GMs
rays = {'axis': [1, 0, 0], 'face': [1, 1, 0], 'face xz': [1, 0, 1], 'body': [1, 1, 1], 'generic': [0.8, 0.5, 0.33]}
tab = {}
for nm, kk in rays.items():
    k = np.array(kk, float); k /= np.linalg.norm(k); t = np.array([0, 0, 1.0]) if abs(k[2]) < 0.9 else np.array([1.0, 0, 0])
    e = t - (t @ k) * k; e /= np.linalg.norm(e)
    tab[nm] = (opg(h_rad, k, e, False), opg(h_rad, k, e, True), opg(h_rad, k, e, True, lat=False), 1 + np.sum(k ** 4),
               opg(h_two, k, e, False) if nm in ('face xz', 'generic') else np.nan)
full = [v[0] for v in tab.values()] + [v[4] for v in tab.values() if not np.isnan(v[4])]
kg = np.array(rays['generic'], float); kg /= np.linalg.norm(kg); eg = np.array([0, 0, 1.0]) - kg[2] * kg; eg /= np.linalg.norm(eg); e2g = np.cross(kg, eg)
outp = {bx_: -(shapiro(h_rad, kg, eg, 1.0, bx_, off=1e-3 * e2g) - shapiro(h_rad, kg, eg, 1.0, bx_, off=-1e-3 * e2g)) / 2e-3 / GMs for bx_ in (False, True)}
check('D1 (a) fixed-4-volume (unimodular) gauges: lattice-measured light speeds give 1 + gamma = 2.0000 on every ray and no out-of-plane bending; the box gives 1 + sum k^4',
      max(abs(np.array(full) - 2)) < 2e-4 and all(abs(v[1] - v[3]) < 2e-4 and abs(v[2] - v[3]) < 1e-6 for v in tab.values()) and abs(outp[False]) < 1e-4 and abs(outp[True] - 0.2318) < 2e-3,
      ' '.join(f'{nm} {v[0]:.4f}/{v[1]:.4f}' for nm, v in tab.items()) + f' (full/box); max |full - 2| {max(abs(np.array(full) - 2)):.0e} incl. 2nd gauge; generic out-of-plane {outp[False]:+.0e}/{outp[True]:+.4f} GM/b')
# D2 GP-B and LAGEOS: the rule's gravitomagnetic coefficient is exactly 1 (B2, C1); a rotor's parts feel v x B, so it precesses at -B/2
ph_ = np.linspace(0, 2 * np.pi, 400, endpoint=False); Bv = np.array([0.3, -0.5, 0.8]); rr = np.stack([np.cos(ph_), np.sin(ph_), 0 * ph_], 1)
vv = np.cross([0, 0, 1.0], rr); tq = np.mean(np.cross(rr, np.cross(vv, Bv)), 0); Lr = np.array([0, 0, 1.0])
Gn, cl_, J_E, a_gpb, dec = 6.6743e-11, 2.99792458e8, 8.034e37 * 7.2921159e-5, 7.0274e6, np.radians(16.841)
yr, mas = 3.15576e7, np.degrees(1) * 3.6e6
om_gpb = Gn * J_E / (2 * cl_ ** 2 * a_gpb ** 3) * np.cos(dec) * yr * mas
a_lg, e_lg = 1.2270e7, 0.0045; om_lg = 2 * Gn * J_E / (cl_ ** 2 * a_lg ** 3 * (1 - e_lg ** 2) ** 1.5) * yr * mas
check('D2 (b) parts feel v x B, so a rotor precesses at -B/2; coefficient 1 gives GP-B frame dragging G J cos(dec)/(2 c^2 a^3) = GR and LAGEOS 2GJ/(c^2 a^3)',
      nrm(tq - np.cross(-Bv / 2, Lr)) < 1e-12 and abs(om_gpb - 39.2) < 0.4 and abs(om_lg - 30.7) < 0.3,
      f'{om_gpb:.1f} mas/yr (GR papers 39.2); measured/this {37.2/om_gpb:.2f} +- {7.2/om_gpb:.2f}; LAGEOS {om_lg:.1f} mas/yr, measured 0.99 +- 0.10 of GR')
# D3 PPN alpha1, alpha2 from the rule: lattice-measured effective metric around a source moving at w through the lattice
def boost(w):
    w = np.asarray(w, float); g = 1 / np.sqrt(1 - w @ w); L = np.eye(4); L[0, 0] = g; L[0, 1:] = L[1:, 0] = g * w
    L[1:, 1:] += (g - 1) * np.outer(w, w) / (w @ w); return L
KDIR = DIRS
Gflat = {}
def lat_quantities(f, eps, b, sig, box, k=1e-3, mu_t=0.05):
    tau = np.sin(eps) / (r3 * np.sqrt(np.mean(np.asarray(f) ** 2))); Ue, Uo = halves(f, eps, mu_t * tau / TAU0, M1)   # mu = m tau
    rest = np.sort(np.abs(np.angle(np.linalg.eigvals(DK(np.zeros(3)) @ Uo @ Ue))))[0]
    Ue, Uo = halves(f, eps, 0.0, M1); X = 0 * X1 if box else Xins(b, sig, f, eps); Pl = (I8 + s3f(f)) / 2
    if box: wfun = lambda K: lightpos(DK(K) @ Uo @ DK(K).conj().T @ Ue, Pl).mean()
    else: wfun = lambda K: wpos(K, Ue, Uo, X, wband(K, 0.0, M1, e0))
    bt = np.array([-(wfun(k * e) - wfun(-k * e)) / (2 * k) for e in np.eye(3)])
    A = np.array([[n[0]**2, n[1]**2, n[2]**2, 2*n[0]*n[1], 2*n[0]*n[2], 2*n[1]*n[2]] for n in KDIR])
    s_ = np.linalg.lstsq(A, np.array([((wfun(k * n) + k * bt @ n) ** 2) / k ** 2 for n in KDIR]), rcond=None)[0]
    return rest, bt, np.array([[s_[0], s_[3], s_[4]], [s_[3], s_[1], s_[5]], [s_[4], s_[5], s_[2]]])
for box in (False, True):
    f, eps, b, sig = reading(0.0, np.zeros((3, 3)), np.zeros(3), box); Gflat[box] = lat_quantities(f, eps, b, sig, box)
def g_eff(hL, box):
    """inverse effective metric read off the lattice: lapse from the rest phase, shift from the tilt, gamma^ij from the cone"""
    g = np.diag([-1.0, 1, 1, 1]) + hL; f, eps, b, sig = reading(hL[0, 0], hL[1:, 1:], hL[0, 1:], box)
    rest, bt, G = lat_quantities(f, eps, b, sig, box); r0, b0, G0 = Gflat[box]
    N = rest / r0; beta = (bt - b0) / TAU0; gup = (TAU0 ** 2 * np.eye(3) + G - G0) / (N * TAU0) ** 2
    gi = np.zeros((4, 4)); gi[0, 0] = -1 / N ** 2; gi[0, 1:] = gi[1:, 0] = beta / N ** 2; gi[1:, 1:] = gup - np.outer(beta, beta) / N ** 2
    return gi - np.linalg.inv(g)
def delta_rest(xr, w, box, sc=1e-5):
    """first-order (Richardson in the field strength) deviation of the rule's metric from the true one, in the source frame, per unit GM"""
    L = boost(w) if np.any(w) else np.eye(4); Li = np.linalg.inv(L); out = []
    for s_ in (sc, 2 * sc):
        gm = s_ * np.linalg.norm(xr) / 2; h00, hij, _ = h_rad(xr, gm); h = np.zeros((4, 4)); h[0, 0] = h00; h[1:, 1:] = hij
        hL = Li.T @ h @ Li; dU = g_eff(hL, box); eta = np.diag([-1.0, 1, 1, 1]); dL = -eta @ dU @ eta
        out.append(L.T @ dL @ L / gm)
    return 2 * out[0] - out[1]
pts = rng.normal(size=(6, 3)); pts /= np.linalg.norm(pts, axis=1)[:, None]; wv = np.array([0.12, -0.09, 0.07])
alph = {}
for box in (False, True):
    rowsA, rhsA, rowsB, rhsB = [], [], [], []
    for xr in pts:
        Dp, Dm, D0 = delta_rest(xr, wv, box), delta_rest(xr, -wv, box), delta_rest(xr, np.zeros(3), box)
        odd = (Dp - Dm) / 2; even = (Dp + Dm) / 2 - D0; U = 1.0 / np.linalg.norm(xr); Uij = np.outer(xr, xr) / np.linalg.norm(xr) ** 3
        for i in range(3): rowsA.append([wv[i] * U, (Uij @ wv)[i]]); rhsA.append(odd[0, 1 + i])
        rowsB.append([wv @ wv * U, wv @ Uij @ wv]); rhsB.append(even[0, 0])
    A1, A2 = np.linalg.lstsq(np.array(rowsA), np.array(rhsA), rcond=None)[0]; B1, B2 = np.linalg.lstsq(np.array(rowsB), np.array(rhsB), rcond=None)[0]
    a2 = -A2; a1 = -2 * A1 - 2 * A2; alph[box] = (a1, a2, -B2, np.abs(np.array(rhsA)).max(), np.abs(np.array(rhsB)).max())
fu, bx = alph[False], alph[True]
check('D3 (c) source moving at w = (.12,-.09,.07) through the lattice: lattice-read lapse, shift and cone equal the boosted metric; preferred-frame terms vanish, alpha1 = alpha2 = 0; box: order one', max(abs(fu[0]), abs(fu[1]), abs(fu[2])) < 1e-4 and max(abs(bx[0]), abs(bx[1])) > 0.3,
      f'full: alpha1 {fu[0]:+.1e}, alpha2 {fu[1]:+.1e} (from g00: {fu[2]:+.1e}); box (boosted radial gauge): alpha1 {bx[0]:+.2f}, alpha2 {bx[1]:+.2f} (g00: {bx[2]:+.2f})')

# ------------------------------------------------------------------ E. earlier results; estimates
print('== E. earlier results; ESTIMATES (not theorems)')
tiltE = []
for ee in (0.05, 0.3, 1.0):
    for mu in (0.0, 0.2):
        K = 2e-3 * np.array([0.6, -0.48, 0.64]); wf, wc, lw = tracked(K, [1, 1, 1], ee, mu, M1, Xins(b1, 0 * sg1, [1, 1, 1], ee))
        tiltE.append(np.max(np.abs((wc - wf) / (-b1 @ K) - 1)))
Xsh = Xins(np.zeros(3), sg1, [1, 1, 1], e0); Ue, Uo = halves([1, 1, 1], e0, 0.0, M1); hs = 0
for n in DIRS:
    w = -np.angle(np.linalg.eigvals(coarseU(2e-3 * n, Ue, Uo, Xsh))); ref = wband(2e-3 * n, 0, M1)
    p = np.sort(w[np.argsort(np.abs(w - ref))[:2]]); hs = max(hs, p[1] - p[0])
spinblind = max(nrm(np.kron(np.eye(8), Op) @ Xins(b1, 0 * sg1, [1, 1, 1], e0) - Xins(b1, 0 * sg1, [1, 1, 1], e0) @ np.kron(np.eye(8), Op)) for Op in GA + GP + [S3])
check('E1 no shift or shear: insertion = 1, static results unchanged; drift -b for every step and mass; shift part spin-blind (g = 2 kept); sheared cone helicity-degenerate; step from lapse and lengths',
      nrm(Xins(np.zeros(3), np.zeros((3, 3)), f1, e1)) == 0 and max(tiltE) < 5e-4 and spinblind < 1e-15 and hs < 1e-11,
      f'drag dev over eps .05/.3/1, mu 0/.2: {max(tiltE):.0e}; spin commutator {spinblind:.0e}; sheared helicity split {hs:.0e}')
# E2 exact reading: shift angle law, and a strong shear calibrated so that the cone is the null cone of the edges
bS = np.array([0.0, -0.15, 0.1]); bmeas, _ = fit_metric(np.ones(3), e1, 0.0, M1, Xins(bS, 0 * sg1, np.ones(3), e1))
gT = np.array([[1.0, -.15, .1], [-.15, .92, -.08], [.1, -.08, 1.07]]); Gt = TAU0 ** 2 * gT
fc = np.sqrt(np.diag(gT)); sc_ = gT / np.outer(fc, fc); np.fill_diagonal(sc_, 0); ecal = []
_, Gref = fit_metric(np.ones(3), e0, 0.0, M1, 0 * X1); cor = Gref - TAU0 ** 2 * np.eye(3)
for it in range(6):
    ec = np.arcsin(r3 * TAU0 * np.sqrt(np.mean(fc ** 2))); _, G = fit_metric(fc, ec, 0.0, M1, Xins(np.zeros(3), sc_, fc, ec))
    E = (G - cor) - Gt; ecal.append(np.abs(E).max() / TAU0 ** 2)
    fc = fc * np.sqrt(np.diag(Gt) / np.diag(G - cor)); offE = E / np.outer(np.sqrt(np.diag(Gt)), np.sqrt(np.diag(Gt))); np.fill_diagonal(offE, 0); sc_ = sc_ - offE
check('E2 exact reading: sin 2theta = b gives the drift to all orders (below the light speed); for a strong shear (0.15) the hop weights '
      'and shear amplitudes fixed by "the light cone is the null cone of the edges" converge: the implicit rule is well posed',
      np.abs(bmeas[1:] / bS[1:] - 1).max() < 1e-5 and ecal[-1] < 1e-5 and ecal[0] > 1e-3,
      f'drift/b - 1 {np.abs(bmeas[1:] / bS[1:] - 1).max():.0e} at |b| .15; calibration error ' + ' '.join(f'{x:.0e}' for x in ecal[::2]))
# estimates
Ugal, wl_ = 5e-7, 2e-3; bet = 4 * Ugal * wl_
print(f'   shift in the lattice frame ~ 4 U w: galaxy {bet:.0e} (U ~ 5e-7, w ~ 2e-3), Sun at 1 AU {4*1e-8*1.2e-3:.0e}, Earth {4*7e-10*1.2e-3:.0e}')
print(f'   cube-rung shift reading (A5) would add (sqrt3/2) b d_ijk K_j S_k: a 3.1 GeV muon gets {r3/2*bet*3.1e9:.0f} eV of spin energy '
      f'against a g-2 precession of 1e-9 eV measured to 2e-7: excluded, hence the block rung')
spl04 = []
for k in (0.01, 0.02):
    p = lightpos(fineU(k * np.array([0.267, 0.535, 0.802]), [1, 1, 1], 0.04, 0.0, 0.5, 'every')); spl04.append(p[1] - p[0])
c5 = spl04[1] / 0.02 ** 2; v04 = np.sin(0.04) / r3; aP = 2 * np.sqrt(8 * np.pi)
pe = lightpos(fineU(0.02 * np.array([0.267, 0.535, 0.802]), [1, 1, 1], 0.04, 0.0, 0.5, 'even')); sev = pe[1] - pe[0]
print(f'   copy mass in every half-tick: helicity split {c5:.2e} K^2 at eps .04 -> eta = (c5/v)(a/l_P) ~ {c5/v04*aP:.1e} '
      f'(a = {aP:.1f} l_P per cube) vs Crab electrons |eta| < ~1e-7: excluded; wrapped around the even half-tick: {sev:.0e}')
print('   block rung: GP-B, LAGEOS = GR; alpha1 = alpha2 = 0 (LLR 1e-4, pulsars 1.6e-9); residual drift O((E a)^2) ~ 1e-36 at 1 GeV;')
print('   massive shear weight 1 + O(mu/eps) < 1e-16 off; h_xy is read, so both GW polarisations act with GR antenna patterns')
print('supplied: CL-1 hop, copy projector, steps, masses, packets, fields, metric gauges, measured numbers; the block tiling one rung up')
print('  (insertion range: one cube) is a proposal, not derived from the axioms.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
