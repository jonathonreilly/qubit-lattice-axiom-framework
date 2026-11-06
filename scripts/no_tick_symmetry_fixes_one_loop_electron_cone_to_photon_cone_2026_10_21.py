#!/usr/bin/env python3
"""fermion-cones: the one-loop limiting speed of the CL-1 light copy against the photon's dressed cone.

Supplied model: the CL-1 cube tick (spin-3/2 edge hop W, even then odd 2^3 cubes, copy mass M on the copy the
three-fold turns rotate by e^(2 pi i/3), wrapped around the even half-tick), its filled negative-quasi-energy sea,
CL-3 site-phase links in Coulomb gauge: two transverse modes with the partition-lattice (Yee) band, which is the
massless fermion band at every momentum, lifted to site phases by the straight-bond integral and projected off the
gauge orbit; instantaneous Coulomb exchange between frame block charges with the partition Gauss law; one loop.
Under CL-3 the photon's dressed cone is the edge cone (one-principle B2), so delta c/c = kappa alpha is the electron's
speed against the photon.  Finite diagnostics; no physical identification.
 A  exact/finite: tick checks, step-set stabiliser, signature, 1+1 vs 3+1 permutation ticks, mass-cone decoupling
 B  engine validation: toy many-body, static field on a torus, Coulomb in real space, Ward identity
 C  one-loop kappa: reference point, logs, continuous-time limit, photon-law variants, speed-difference flow
 D  fix options;  E  estimates with measured numbers
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/NO_TICK_SYMMETRY_FIXES_ONE_LOOP_ELECTRON_CONE_TO_PHOTON_CONE_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm, schur
np.seterr(all='ignore')
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ CL-1 cube tick (block Bloch form)
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
VOL = (r3 ** 3) * WAX[0] @ WAX[1] @ WAX[2]; S3 = 1j * VOL @ W; PL = (I8 + S3) / 2; PH = (I8 - S3) / 2
D_R = C8 - 0.5; XS = C8 / 2.0
def dag(A): return np.conj(np.swapaxes(A, -1, -2))
def DK(K): return np.exp(1j * (np.atleast_2d(K) @ C8.T))
class Tick:
    def __init__(s, eps, mu, M):
        s.eps, s.mu, s.M = eps, mu, M; F = expm(1j * (M / 2) * PH @ W)
        s.Ue = F @ expm(-1j * (eps - mu / 2) * W) @ F; s.Eo = expm(1j * (eps + mu / 2) * W)
    def U(s, K): D = DK(K); return (D[:, :, None] * s.Eo[None] * D.conj()[:, None, :]) @ s.Ue
    def spec(s, K): UK = s.U(K); z, V = np.linalg.eig(UK); return UK, z, V, np.linalg.inv(V)
def pair(tk, p, sign=1):
    """orthonormal light-copy pair at p with sign of quasi-energy; lowest |w|"""
    T, Z = schur(tk.U(p)[0], output='complex'); z = np.diag(T); w = -np.angle(z); lw = np.linalg.norm(PL @ Z, axis=0)
    sel = np.where((sign * w > 0) & (lw > 0.5))[0]; sel = sel[np.argsort(np.abs(w[sel]))][:2]; return Z[:, sel], w[sel], z[sel]
def kern(x, l0): return x ** l0 / (1 - x)
def shift_batch(tk, p, B, zk, qs, dab, om, taus=(0.5, 1.0), sig=(1, -1)):
    """Floquet second order (s-tick-dressing formula): particle at p - q, hole at p + q, seagull; insertions after the
    even half-tick (+chi) and after the odd half-tick (-chi)"""
    F0 = [tk.Ue, tk.U(p)[0]]
    Um, zm, Vm, Vmi = tk.spec(p - qs); Up, zp, Vp, Vpi = tk.spec(p + qs)
    Fm = [np.broadcast_to(tk.Ue, Um.shape), Um]; Fq = [np.broadcast_to(tk.Ue, Up.shape), Up]
    seam, seap = -np.angle(zm) < 0, -np.angle(zp) < 0; dem = np.conj(dab); Bd = B.conj().T
    VR = [Vmi @ (dag(Fm[i]) @ (dem[:, :, None] * (F0[i] @ B)[None])) for i in range(2)]
    LV = [(((Bd @ F0[i].conj().T)[None] * dab[:, None, :]) @ Fm[i]) @ Vm for i in range(2)]
    VRp = [Vpi @ (dag(Fq[i]) @ (dab[:, :, None] * (F0[i] @ B)[None])) for i in range(2)]
    LVp = [(((Bd @ F0[i].conj().T)[None] * dem[:, None, :]) @ Fq[i]) @ Vp for i in range(2)]
    X = 0
    for i2 in range(2):
        for i1 in range(2):
            l0 = 0 if i1 < i2 else 1; pre = sig[i1] * sig[i2] * np.exp(-1j * om * (taus[i2] - taus[i1]))
            fm = np.where(~seam, kern((zm / zk) * np.exp(-1j * om)[:, None], l0), 0)
            fp = np.where(seap, kern((zk / zp) * np.exp(-1j * om)[:, None], l0), 0)
            X = X - pre[:, None, None] * (LV[i2] @ (fm[:, :, None] * VR[i1]) - LVp[i1] @ (fp[:, :, None] * VRp[i2]))
    for i in range(2):
        X = X - 0.5 * (LV[i] @ ((~seam)[:, :, None] * VR[i]) - LVp[i] @ (seap[:, :, None] * VRp[i]))
    return 1j * X
def tvecs(qs, proj=True):
    qn = np.linalg.norm(qs, axis=1); qh = qs / qn[:, None]
    ref = np.where(np.abs(qh[:, [0]]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
    e1 = np.cross(qh, ref); e1 /= np.linalg.norm(e1, axis=1)[:, None]; e2 = np.cross(qh, e1); qd = qs @ D_R.T
    L = np.stack([(e @ D_R.T) * np.sinc(qd / 2 / np.pi) for e in (e1, e2)], 1).astype(complex)
    if proj:
        G = np.stack([-np.exp(-0.5j * qd), np.exp(0.5j * qd)], 2); L = L - np.einsum('nab,nbc,ncd,nld->nla', G, np.linalg.inv(dag(G) @ G), dag(G), L)
    return L
def band(qs, eps): return 2 * np.arcsin(np.sin(eps) / r3 * np.sqrt(np.sum(np.sin(np.atleast_2d(qs) / 2) ** 2, 1)))
def G_sc(qs): return 1.0 / (4 * np.sum(np.sin(qs / 2) ** 2, 1))
def G_bcc(qs): c = np.prod(np.cos(qs / 2), 1); return 1.0 / (4 * (1 - c * c))
def grid(n, levels):
    pts, wts = [], []
    for l in range(levels + 1):
        side = 2 * np.pi / 2 ** l; h = side / n; g = -side / 2 + h * (np.arange(n) + 0.5)
        Q = np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
        if l < levels: Q = Q[np.max(np.abs(Q), 1) > side / 4]
        pts.append(Q); wts.append(np.full(len(Q), (h / (2 * np.pi)) ** 3))
    return np.concatenate(pts), np.concatenate(wts)
def selfE(tk, p, Q, Wq, phot='band', vf=1.0, coul='sc', proj=True, sign=1, batch=2000):
    """(transverse 2x2, Coulomb 2x2) in units e^2 = 4 pi alpha c0, quasi-energy per tick"""
    B, w0, z0 = pair(tk, p, sign); zk = np.mean(z0); T = 0; Cm = 0; Gf = G_sc if coul == 'sc' else G_bcc
    for s in range(0, len(Q), batch):
        qs, wq = Q[s:s + batch], Wq[s:s + batch]
        om = vf * (band(qs, tk.eps) if phot == 'band' else np.sin(tk.eps) / r3 * np.linalg.norm(qs, axis=1))
        Lv = tvecs(qs, proj); ph = np.exp(1j * qs @ XS.T)
        for lam in range(2):
            T = T + shift_batch(tk, p, B, zk, qs, np.sqrt(wq / (2 * om))[:, None] * Lv[:, lam] * ph, om).sum(0)
        Up, zp, Vp, Vpi = tk.spec(p + qs); Ps = Vp @ ((-np.angle(zp) < 0).astype(float)[:, :, None] * Vpi)
        ev = np.einsum('ai,nab,bj->nij', B.conj(), Ps, B); Bo = tk.Ue @ B; Dq = DK(qs)
        od = np.einsum('ai,na,nab,nb,bj->nij', Bo.conj(), Dq.conj(), tk.Ue[None] @ Ps @ tk.Ue.conj().T[None], Dq, Bo)
        Cm = Cm + 0.25 * np.einsum('n,nij->ij', Gf(qs) * wq, 2 * np.eye(2)[None] - 2 * ev - 2 * od)
    return T, Cm, w0
def kap(tk, p, Q, Wq, **kw):
    T, Cm, w0 = selfE(tk, p, Q, Wq, **kw); pm = np.linalg.norm(p)
    return 4 * np.pi * np.trace(T).real / 2 / pm, 4 * np.pi * np.trace(Cm).real / 2 / pm, T + Cm

# ------------------------------------------------------------------ A. exact and finite
print('== A. tick, step set and symmetry (exact / finite)')
def realspace(tk, Ls, chi=None):
    S = np.array(list(itertools.product(*[range(n) for n in Ls]))); IDX = {tuple(x): i for i, x in enumerate(S)}; N = len(S)
    Ue_R, Uo_R = np.zeros((N, N), complex), np.zeros((N, N), complex); perm = [7 - int(t @ [4, 2, 1]) for t in C8]
    for R in itertools.product(*[range(0, n, 2) for n in Ls]):
        ids = [IDX[tuple((np.array(R) + c) % Ls)] for c in C8]; Ue_R[np.ix_(ids, ids)] = tk.Ue
        ido = [IDX[tuple((np.array(R) + 1 + t) % Ls)] for t in C8]; Uo_R[np.ix_(ido, ido)] = tk.Eo[np.ix_(perm, perm)]
    if chi is not None: Uo_R = np.exp(-1j * chi)[:, None] * Uo_R * np.exp(1j * chi)[None, :]
    return S, Uo_R, Ue_R
dev = 0; sp = []
for M in (0.0, 0.5, 1.0):
    tk = Tick(0.3, 0.05, M); S8, Uo8, Ue8 = realspace(tk, np.array([8, 8, 8]))
    Kg = np.array(list(itertools.product(2 * np.pi * np.arange(4) / 4, repeat=3)))
    dev = max(dev, np.abs(np.sort(np.angle(np.linalg.eigvals(Uo8 @ Ue8))) - np.sort(np.angle(np.linalg.eigvals(tk.U(Kg))).ravel())).max())
    tk0 = Tick(0.3, 0.0, M)
    for d in (np.array([1.0, 0, 0]), np.array([1, 1, 1]) / r3):
        w2 = [pair(tk0, k * d)[1][0] ** 2 for k in (0.01, 0.02)]; c2 = np.linalg.solve([[1e-4, 1e-8], [4e-4, 16e-8]], w2)[0]
        sp.append(np.sqrt(c2) / (np.sin(0.3) / r3))
rng = np.random.default_rng(20261021); KR = rng.uniform(-np.pi, np.pi, (200, 3)); tkm = Tick(0.3, 0.0, 0.0)
fb = np.sort(np.abs(np.angle(np.linalg.eigvals(tkm.U(KR)))), 1)[:, 0]
check('A1 real-space 8^3 tick = Bloch tick (M = 0, .5, 1); the copy mass leaves the light speed exactly sin(eps)/sqrt3; the '
      'partition (Yee) photon band equals the massless fermion band at every K', dev < 1e-12 and max(abs(x - 1) for x in sp) < 1e-7
      and np.abs(fb - band(KR, 0.3)).max() < 1e-12, f'{dev:.0e}; speed/c0 - 1 <= {max(abs(x - 1) for x in sp):.0e}; band {np.abs(fb - band(KR, 0.3)).max():.0e}')
S8, Uo8, Ue8 = realspace(Tick(0.3, 0.05, 0.5), np.array([8, 8, 8])); U8 = Uo8 @ Ue8; Dset = set()
for j in range(8):
    x0 = np.array([2, 2, 2]) + C8[j]; i0 = int(np.where((S8 == x0).all(1))[0][0])
    for t in np.where(np.abs(U8[:, i0]) > 1e-12)[0]: Dset.add(tuple(int(v) for v in ((S8[t] - x0 + 4) % 8 - 4)))
Dl = np.array(sorted(Dset)); Sst = np.concatenate([np.c_[np.ones(len(Dl)), Dl], -np.c_[np.ones(len(Dl)), Dl]])
def stabiliser(c):
    eta = np.diag([c * c, -0.25, -0.25, -0.25]); Qv = np.einsum('ni,ij,nj->n', Sst, eta, Sst); key = {tuple(np.round(s, 9)) for s in Sst}
    basis = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1.]]); out = []
    cand = [Sst[np.abs(Qv - b @ eta @ b) < 1e-12] for b in basis]
    for im in itertools.product(*cand):
        L = np.array(im).T @ np.linalg.inv(basis.T)
        if np.abs(L.T @ eta @ L - eta).max() < 1e-9 and all(tuple(np.round(L @ s, 9)) in key for s in Sst): out.append(L)
    return out
stb = {c: stabiliser(c) for c in (np.sin(0.3) / r3, 0.5, 0.9)}
ok_t = all(np.abs(L[0, 1:]).max() < 1e-12 and np.abs(L[1:, 0]).max() < 1e-12 for v in stb.values() for L in v)
check(f'A2 THEOREM: the one-tick step set ({len(Dl)} displacements, both time senses) is kept by exactly 96 cone-preserving '
      'linear maps for every trial cone speed, all of them cubic rotations/reflections with or without time reversal: '
      'no symmetry maps a time step into a space step, and none distinguishes one cone speed from another; every step '
      'advances one tick, so the Euclidean hypercubic turn t -> x (the B4 route) is not a symmetry of any tick',
      all(len(v) == 96 for v in stb.values()) and ok_t and np.all(np.abs(Sst[:, 0]) == 1), f'counts {[len(v) for v in stb.values()]}')
inert = lambda d: (int(np.sum(np.array(d) > 0)), int(np.sum(np.array(d) < 0)))
chi1 = rng.uniform(-np.pi, np.pi, 16); chi2 = rng.uniform(-np.pi, np.pi, 16); Se = np.zeros((16, 16)); So = np.zeros((16, 16))
for k in range(8): Se[2 * k, 2 * k + 1] = Se[2 * k + 1, 2 * k] = 1; So[(2 * k + 1) % 16, (2 * k + 2) % 16] = So[(2 * k + 2) % 16, (2 * k + 1) % 16] = 1
U1 = np.diag(np.exp(-1j * chi2)) @ So @ np.diag(np.exp(1j * chi1)) @ Se
mono = np.all(np.sum(np.abs(U1) > 1e-12, 0) == 1); disp = {int(((np.argmax(np.abs(U1[:, i])) - i + 8) % 16) - 8) for i in range(16)}
perm8 = rng.permutation(8); dsp = rng.integers(-1, 2, (8, 3)); phs = rng.uniform(-np.pi, np.pi, 8)
def mono3(K): Mx = np.zeros((8, 8), complex); Mx[perm8, np.arange(8)] = np.exp(1j * (phs + dsp @ K)); return Mx
cyc = []; seen = set()
for s0_ in range(8):
    if s0_ in seen: continue
    l_, t_ = 0, s0_
    while True:
        seen.add(t_); t_ = perm8[t_]; l_ += 1
        if t_ == s0_: break
    cyc.append(l_)
npow = int(np.lcm.reduce(cyc)); K0, hk = rng.uniform(-1, 1, 3), 0.3
Mp = lambda K: np.linalg.matrix_power(mono3(K), npow); offd = max(np.abs(Mp(K) - np.diag(np.diag(Mp(K)))).max() for K in (K0, K0 + hk))
hess = max(np.abs(np.angle(np.diag(Mp(K0 + hk * e)) * np.diag(Mp(K0 - hk * e)) / np.diag(Mp(K0)) ** 2)).max() for e in np.eye(3)) + offd
check('A3 THEOREM: an isometry flipping the metric sign needs equal inertia: (1,1) in 1+1 has it (the null-lattice x <-> t '
      'exchange), (1,3) vs (3,1) in 3+1 does not; the 1+1 step-pi/2 tick dressed by any site phases is a permutation times '
      'phases with displacements +-2 per tick, so link dressing cannot change its speed; a power of any translation-'
      'invariant permutation tick on Z^3 is diagonal with phases affine in K (bands are planes, no cone), while W has 3 entries per row',
      inert([1, -1]) == inert([-1, 1]) and inert([1, -1, -1, -1]) != inert([-1, 1, 1, 1]) and mono and disp == {-2, 2}
      and hess < 1e-6 and set(np.sum(np.abs(W) > 1e-12, 1)) == {3}, f'1+1 displacements {sorted(disp)}; 3D: power {npow}, curvature + off-diagonal {hess:.0e}')
dws = {}
for M in (0.0, 0.5):
    tkp, tkm_ = Tick(0.3, 1e-5, M), Tick(0.3, -1e-5, M)
    dws[M] = [(pair(tkp, k * np.array([1.0, 0, 0]))[1][0] - pair(tkm_, k * np.array([1.0, 0, 0]))[1][0]) / 2e-5 / (np.sin(0.3) / r3 * k) for k in (0.02, 0.04, 0.08)]
check('A4 bare-mass sensitivity of the light cone at mu = 0: zero without the copy mass (bands even in mu), O(K^2) relative '
      'with it, so the additive mass does not feed the limiting speed at O(alpha): mass and cone conditions are independent',
      max(abs(x) for x in dws[0.0]) < 1e-6 and 3.5 < dws[0.5][1] / dws[0.5][0] < 4.5 and 3.5 < dws[0.5][2] / dws[0.5][1] < 4.5,
      'M = .5: ' + ', '.join(f'{x:.1e}' for x in dws[0.5]) + ' at K = .02, .04, .08')

# ------------------------------------------------------------------ B. engine validation
print('== B. engine validation')
tr = np.random.default_rng(53); Mt = 4
def herm(n): X = tr.normal(size=(n, n)) + 1j * tr.normal(size=(n, n)); return (X + X.conj().T) / 2
hA, hB, hC = herm(Mt), herm(Mt), herm(Mt); A_, B_, C_ = expm(-1j * hA), expm(-1j * hB), expm(-1j * hC)
w_, V_ = np.linalg.eig(C_ @ B_ @ A_); o_ = np.argsort(-np.angle(w_)); V_, _ = np.linalg.qr(V_[:, o_]); zt = w_[o_]; seat = -np.angle(zt) < 0
cubes = [[0, 1], [2, 3]]; phi_t = np.array([0.7 + 0.2j, -0.4 + 0.5j])
def Pc(c): P = np.zeros((Mt, Mt)); P[c, c] = 1; return P
def f_at(i, amp): Ui = A_ if i == 0 else B_ @ A_; return V_.conj().T @ Ui.conj().T @ sum(amp[j] * Pc(c) for j, c in enumerate(cubes)) @ Ui @ V_
def toy_formula(k, om):
    Ab = [f_at(i, phi_t) for i in range(2)]; Em = [f_at(i, phi_t.conj()) for i in range(2)]; P = seat; X = 0
    hart = {(i1, i2): Ab[i2][k, k] * np.trace(Em[i1][np.ix_(P, P)]) + np.trace(Ab[i2][np.ix_(P, P)]) * Em[i1][k, k] for i1 in range(2) for i2 in range(2)}
    for i2 in range(2):
        for i1 in range(2):
            l0 = 0 if i1 < i2 else 1; pre = (1, -1)[i1] * (1, -1)[i2] * np.exp(-1j * om * ((0.25, 0.75)[i2] - (0.25, 0.75)[i1]))
            fm = np.where(~seat, kern(zt / zt[k] * np.exp(-1j * om), l0), 0); fp = np.where(seat, kern(zt[k] / zt * np.exp(-1j * om), l0), 0)
            X += -pre * (Ab[i2][k] @ (fm * Em[i1][:, k]) - Em[i1][k] @ (fp * Ab[i2][:, k])) - pre * hart[(i1, i2)] * kern(np.exp(-1j * om), l0)
    for i in range(2): X += -0.5 * (Ab[i][k] @ ((~seat) * Em[i][:, k]) - Em[i][k] @ (seat * Ab[i][:, k])) - 0.5 * hart[(i, i)]
    return (1j * X).real
dimF = 2 ** Mt
def cop(j):
    m = np.zeros((dimF, dimF))
    for s in range(dimF):
        if (s >> j) & 1: m[s ^ (1 << j), s] = (-1) ** bin(s & ((1 << j) - 1)).count('1')
    return m
cs = [cop(j) for j in range(Mt)]
def sq(h): return sum(h[i, j] * cs[i].T @ cs[j] for i in range(Mt) for j in range(Mt))
aop = np.diag(np.sqrt(np.arange(1, 4)), 1); nph = aop.T @ aop
def U_tot(gc, om):
    pe = lambda t: expm(-1j * om * t * nph)
    cpl = lambda i: expm(1j * (1, -1)[i] * sum(np.kron(sq(Pc(c)), gc * phi_t[j] * aop + np.conj(gc * phi_t[j]) * aop.T) for j, c in enumerate(cubes)))
    return np.kron(expm(-1j * sq(hC)), pe(0.25)) @ cpl(1) @ np.kron(expm(-1j * sq(hB)), pe(0.5)) @ cpl(0) @ np.kron(expm(-1j * sq(hA)), pe(0.25))
def mb(occ, gc, om):
    st = np.zeros(dimF, complex); st[0] = 1
    for p_ in occ: st = sum(V_[j, p_] * cs[j].T for j in range(Mt)) @ st
    psi = np.kron(st, np.eye(4)[0]); l0 = psi.conj() @ U_tot(0.0, om) @ psi; ev, EV = np.linalg.eig(U_tot(gc, om))
    return -np.angle(ev[np.argmax(np.abs(EV.conj().T @ psi))] / l0)
dv = 0; seaocc = list(np.nonzero(seat)[0])
for om in (0.9, 2.2):
    base = mb(seaocc, 5e-4, om)
    for k in range(Mt):
        occ = seaocc + [k] if not seat[k] else [x for x in seaocc if x != k]; sg = 1 if not seat[k] else -1
        fo_ = toy_formula(k, om); dv = max(dv, abs(sg * (mb(occ, 5e-4, om) - base) / 2.5e-7 - fo_) / max(abs(fo_), 1e-3))
check('B1 second-order Floquet formula = exact many-body shift (toy: 4 modes, 3 kicks, 2 insertions, quantised mode)', dv < 1e-4, f'{dv:.1e}')
tk = Tick(0.4, 0.12, 0.5); qx = np.array([2 * np.pi / 8, 0, 0]); u = tvecs(qx[None])[0, 0]; B0, w00, z00 = pair(tk, np.zeros(3))
Fs = sum(shift_batch(tk, np.zeros(3), B0, np.mean(z00), sq_[None], (am * np.exp(1j * sq_ @ XS.T))[None], np.zeros(1))[0]
         for sq_, am in ((qx, u), (-qx, np.conj(u))))
fe = np.linalg.eigvalsh((Fs + Fs.conj().T) / 2).mean(); Lt = np.array([16, 2, 2]); ex = []
St, Uot, Uet = realspace(tk, Lt); e0 = -np.angle(np.linalg.eigvals(Uot @ Uet)); s0 = np.sort(e0[np.abs(e0 - w00[0]) < 1e-6]).mean()
for a in (0.01, 0.005):
    chi = 2 * np.real(a * u[(St % 2) @ [4, 2, 1]] * np.exp(1j * (St / 2.0) @ qx)); _, Uoc, Uec = realspace(tk, Lt, chi)
    e1 = -np.angle(np.linalg.eigvals(Uoc @ Uec)); ex.append((np.sort(e1[np.abs(e1 - w00[0]) < 0.01]).mean() - s0) / a ** 2)
check('B2 static transverse site-phase field on a 16x2x2 torus: exact light-level shift -> formula as amplitude^2',
      abs(ex[1] - fe) < abs(ex[0] - fe) / 3 and abs(ex[1] - fe) < 1e-3 * abs(fe), f'exact {ex[0]:.6f}, {ex[1]:.6f}; formula {fe:.6f}')
tk = Tick(0.4, 0.12, 0.5); S4, Uo4, Ue4 = realspace(tk, np.array([8, 8, 8])); U4 = Uo4 @ Ue4
z4, V4 = np.linalg.eig(U4); Ps4 = V4 @ np.diag((np.angle(z4) > 0).astype(float)) @ np.linalg.inv(V4)
Kst, _ = np.linalg.qr(V4[:, np.abs(-np.angle(z4) - w00[0]) < 1e-6])
Rb = np.array(list(itertools.product(range(4), repeat=3)), float)
qg = (np.array([np.array(m) * np.pi / 2 for m in itertools.product(range(4), repeat=3) if any(m)]) + np.pi) % (2 * np.pi) - np.pi
cdev = 0
for coul, Gf in (('sc', G_sc), ('bcc', G_bcc)):
    Gbb = np.cos((Rb[:, None, :] - Rb[None]) @ qg.T) @ Gf(qg) / 64; tot = 0
    for st, P, blk in ((Kst, Ps4, ((S4 // 2) % 4) @ [16, 4, 1]), (Ue4 @ Kst, Ue4 @ Ps4 @ Ue4.conj().T, (((S4 - 1) // 2) % 4) @ [16, 4, 1])):
        PiK = np.stack([st * (blk == b)[:, None] for b in range(64)]); PPiK = np.einsum('ij,bjk->bik', P, PiK)
        tot = tot + 0.5 * sum(0.5 * Gbb[b, b] * PiK[b].conj().T @ PiK[b] - np.einsum('c,ik,cil->kl', Gbb[b], PiK[b].conj(), PPiK) for b in range(64))
    _, Cb, _ = selfE(tk, np.zeros(3), qg, np.full(len(qg), 1 / 64), coul=coul)
    cdev = max(cdev, abs(np.trace(tot).real - np.trace(Cb).real) / abs(np.trace(Cb).real))
check('B3 Coulomb exchange with the sea, frame block charges: real-space 8^3 sum = Bloch sum (partition and bcc Gauss laws)', cdev < 1e-10, f'{cdev:.0e}')
wd = 0
for q in (np.array([0.3, -0.1, 0.2]), qx):
    qd = q @ D_R.T
    for g in (np.exp(0.5j * qd), -np.exp(-0.5j * qd)):
        ph = 0.1 * g / np.linalg.norm(g) * np.exp(1j * q @ XS.T)
        wd = max(wd, np.abs(sum(shift_batch(tk, np.zeros(3), B0, np.mean(z00), s_ * q[None], a_[None], np.zeros(1))[0] for s_, a_ in ((1, ph), (-1, np.conj(ph))))).max())
check('B4 Ward identity: static pure-gauge centre phases give zero shift', wd < 1e-14, f'{wd:.0e}')
print(f'   [{time.time() - T0:.0f} s]')

# ------------------------------------------------------------------ C. one-loop speed shift
print('== C. one loop: delta c/c = kappa alpha, kappa = 4 pi (dw/e^2)/p at small p, e^2 = 4 pi alpha c0; external light positive pair')
Q16, W16 = grid(16, 9); Q12, W12 = grid(12, 9); ex_ = np.array([1.0, 0, 0]); dg = np.ones(3) / r3
tk = Tick(0.3, 0.0, 0.5); R = {}
for nm, p in (('x3', 0.03 * ex_), ('x15', 0.015 * ex_), ('d3', 0.03 * dg)): R[nm] = kap(tk, p, Q16, W16)
kx, kx2, kd = [sum(R[n][:2]) for n in ('x3', 'x15', 'd3')]; split = np.abs(R['x15'][2] - np.trace(R['x15'][2]) / 2 * np.eye(2)).max()
check('C1 reference point eps = .3, M = .5: kappa is nonzero, O(1) and negative (electron slower than the photon), '
      'isotropic, p-independent, with no helicity splitting (no CPT-odd term)', -0.87 < kx < -0.82 and abs(kx - kd) < 4e-3
      and abs(kx - kx2) < 3e-3 and split < 1e-12, f'kappa x(.03) {kx:+.4f}, x(.015) {kx2:+.4f}, diag(.03) {kd:+.4f}; split {split:.0e}')
sC = (R['x15'][1] - R['x3'][1]) / np.log(2); sT = (R['x15'][0] - R['x3'][0]) / np.log(2)
check('C2 the Coulomb part runs with the continuum velocity log 2/(3 pi) per ln(1/p), the transverse part with the opposite '
      'log: equal tree cones cancel the logs and kappa is a finite lattice constant', abs(sC - 2 / (3 * np.pi)) < 0.01
      and abs(sC + sT) < 3e-3, f'slopes C {sC:+.4f} (2/3pi = {2 / (3 * np.pi):.4f}), T {sT:+.4f}')
ct = {}
for r in (0.1, 1.0, 3.0, 10.0): ct[r] = sum(kap(Tick(0.05, 0.0, r * 0.05), 0.03 * ex_, Q12, W12)[:2])
ct['pi/2'] = sum(kap(Tick(0.05, 0.0, np.pi / 2), 0.03 * ex_, Q12, W12)[:2]); k25 = sum(kap(Tick(0.025, 0.0, 0.25), 0.03 * ex_, Q12, W12)[:2])
check('C3 continuous-time limit (eps = .05; r = M/eps): kappa(r) stays negative and O(1) for every copy mass, -0.17 when '
      'the copies are near-degenerate to -1.0 near r = 3; eps .05 -> .025 at r = 10 moves it by < 3e-3',
      all(-1.05 < v < -0.15 for v in ct.values()) and abs(k25 - ct[10.0]) < 3e-3,
      ', '.join(f'r {k}: {v:+.3f}' for k, v in ct.items()) + f'; r 10 at eps .025: {k25:+.3f}')
tk10, tk01 = Tick(0.05, 0.0, 0.5), Tick(0.05, 0.0, 0.005)
kl = {'bcc Gauss': sum(kap(tk10, 0.03 * ex_, Q12, W12, coul='bcc')[:2]), 'linear photon': sum(kap(tk10, 0.03 * ex_, Q12, W12, phot='lin')[:2]),
      'no projection': sum(kap(tk10, 0.03 * ex_, Q12, W12, proj=False)[:2])}
kz = sum(kap(tk01, 0.03 * ex_, Q12, W12, coul='bcc', phot='lin')[:2])
check('C4 photon-law variants (eps = .05): at r = 10 every variant stays negative and O(1); at near-degenerate copies '
      '(r = .1) bcc Gauss law plus linear photon crosses zero: a one-loop zero can be tuned from supplied choices, not '
      'protected', all(-0.95 < v < -0.6 for v in kl.values()) and 0 < kz < 0.1 < -ct[0.1],
      ', '.join(f'{k} {v:+.3f}' for k, v in kl.items()) + f'; r .1: register law {ct[0.1]:+.3f}, bcc + linear {kz:+.3f}')
tkf = Tick(0.05, 0.0, 0.5); f0 = [sum(kap(tkf, pm * ex_, Q12, W12)[:2]) for pm in (0.03, 0.015)]
f1 = [sum(kap(tkf, pm * ex_, Q12, W12, vf=1.1)[:2]) for pm in (0.03, 0.015)]; Aflow = ((f1[1] - f1[0]) - (f0[1] - f0[0])) / np.log(2) / 0.1
check('C5 with the photon faster by delta = .1 the electron speed runs towards it, d kappa/d ln(1/p) = A delta: the '
      'speed-difference anomalous dimension is A alpha', 0.3 < Aflow < 0.4, f'A = {Aflow:.3f}')
print(f'   [{time.time() - T0:.0f} s]')

# ------------------------------------------------------------------ D. fix options
print('== D. fix options')
Kg20 = np.array(np.meshgrid(*[2 * np.pi * (np.arange(20) + 0.5) / 20 - np.pi] * 3, indexing='ij')).reshape(3, -1).T
es = np.linspace(0.02, 1.5, 40); Phi = np.array([-4 * np.mean(band(Kg20, e)) for e in es])
dmu = []
for fm in (0.04, 0.02, 0.01):
    tkm2 = Tick(0.05, fm * 0.05, 0.5); T_, C_, w_ = selfE(tkm2, np.zeros(3), Q12, W12); dmu.append((np.trace(T_).real + np.trace(C_).real) / 2)
mus = np.array([0.04, 0.02, 0.01]) * 0.05; bLI = 3 / (8 * np.pi ** 2 * np.sin(0.05) / r3)
afit = np.linalg.lstsq(np.c_[np.ones(3), mus], np.array(dmu) - bLI * mus * np.log(1 / mus), rcond=None)[0][0]
dmL = afit * 4 * np.pi * np.sin(0.05) / r3 * r3 / 0.05
check('D1 a step is not a response variable: the vacuum phase falls monotonically with the step, so no stationarity of '
      'the total phase selects it; and the additive mass is unprotected, delta m L = O(alpha) (r = 10, after removing '
      'the Lorentz-invariant 3 alpha/4pi m ln term)', np.all(np.diff(Phi) < 0) and abs(dmL) > 0.1, f'delta m L = {dmL:+.3f} alpha')

# ------------------------------------------------------------------ E. estimates
print('== E. ESTIMATES (measured numbers supplied; not theorems)')
al = 1 / 137.035999084; me = 0.51099895e6; ks = [min(ct.values()), max(ct.values())]
dc = [abs(k_) * al for k_ in ks]; Eth = [2 * me / np.sqrt(2 * d_) / 1e6 for d_ in dc]
print(f'   no fix: delta c_e/c = kappa alpha = {-dc[0]:.1e} .. {-dc[1]:.1e} (photon faster): vacuum photon decay above '
      f'{Eth[0]:.0f}-{Eth[1]:.0f} MeV; LHAASO 1.4 PeV (3e-19) exceeded {dc[1] / 3e-19:.0e}-{dc[0] / 3e-19:.0e}x, LEP (1e-11) {dc[1] / 1e-11:.0e}-{dc[0] / 1e-11:.0e}x')
gfl = Aflow * al * np.log(2.4e27 / me)
print(f'   speed-difference flow cell -> m_e: suppression exp(-A alpha ln) = {np.exp(-gfl):.2f} (electron part; needs < 1e-8)')
print(f'   a tuned one-loop zero leaves O(alpha^2) ~ {al ** 2:.0e} (x O(1)): still {al ** 2 / 1e-11:.0e}x LEP, {al ** 2 / 3e-19:.0e}x LHAASO')
print(f'   dressed-cone step (CL-1 option): sin eps_s = sin eps_edge/(1 + kappa_s alpha_s): electron step up by '
      f'{dc[1] * 100:.2f}-{dc[0] * 100:.2f} %; dimension-4 offset 0 by construction; residual dimension-6 ~ (E L)^2 ~ 3e-25 at 1.4 PeV')
dmo = abs(dmL) * al * 2.4e27 / me
print(f'   additive mass with a fixed bare mu = mN: delta m/m_e ~ {dmo:.0e}; a potential changes L by ~Phi, so m_e moves by '
      f'~{dmo:.0e} Phi (Sun, annual 1.6e-10: {dmo * 1.6e-10:.0e}): mu must also be read as a dressed value, or protected')
check('E1 arithmetic: every kappa excluded by > 1e8 (LEP) and > 1e15 (LHAASO); flow suppression > 0.5',
      dc[1] / 1e-11 > 1e8 and dc[1] / 3e-19 > 1e15 and np.exp(-gfl) > 0.5)
print('supplied: tick, copy mass and step (scanned), sea branch, photon law (band, lift, gauge projection, Gauss law,')
print('  continuous-time modes at the half-tick boundaries), Coulomb gauge, one loop, e^2 = 4 pi alpha c0, CL-3 photon cone,')
print('  cell = 5 l_P in E, measured bounds.  Forced: no symmetry fixes the cone (A2, A3), logs cancel, isotropy, no')
print('  helicity split, mass-cone independence; kappa != 0 in the register law at every copy mass.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
