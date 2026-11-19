#!/usr/bin/env python3
"""nononsite-chiral: exact quantised non-on-site charges of the CL-1 tick and of H' = (i/2)[W_o, W_e], and whether any can
carry a chiral link.
 A 1+1D template (staggered chain): Kitaev-pairing axial charge, Onsager growth, single-chirality combination, bookkeeping
 B CL-1 tick: pi-flux real gauge, staggered particle-hole map; translation, tick and glide charges; backgrounds; light action
 C all range-1 conserved one-body operators (exact on the 5^3 grid), with and without the copy mass
 D theorem T1 (compact one-body charges are vector-like) bookkeeping: H' over its four massless points; hypercharge multisets
 E measured checks: strict light cone, partner gap, V - A
Labels: [T] theorem / exact finite computation, [F] finite diagnostic, [M] against measurement. Supplied model, finite
diagnostic; no physical identification. Cited, not rederived: Nielsen-Ninomiya; Chatterjee-Pace-Shao 2024 (1+1D template);
Gioia-Thorngren 2025 arXiv:2503.07708 (3+1D single-Weyl charge non-compact; Weyl-doublet Onsager pair)."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import gc, itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from collections import deque
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import expm, eigh

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
def bdg(A, B): return np.block([[A, B], [B.conj().T, -A.T]])
def Ub(u): n = len(u); return np.block([[u, np.zeros((n, n))], [np.zeros((n, n)), u.conj()]])
def Qof(Y, S, sig=1):
    """quantised one-body charge from a conserved unitary Y with S Y^T S = sig Y^dag (T1 template)"""
    if sig > 0: return bdg((Y + Y.conj().T) / 2, (Y - Y.conj().T) @ S / 2)
    return bdg(1j * (Y - Y.conj().T) / 2, (Y + Y.conj().T) @ S / 2)
def majorana(Q):
    n = len(Q) // 2; Om = np.block([[np.eye(n), np.eye(n)], [-1j * np.eye(n), 1j * np.eye(n)]]) / np.sqrt(2); return Om @ Q @ Om.conj().T
def matching(Q):
    M = majorana(Q); rows = [np.nonzero(np.abs(M[i]) > 1e-9)[0] for i in range(len(M))]
    return nrm(M.real) < 1e-12 and all(len(r) == 1 for r in rows) and np.allclose(np.abs(M[np.abs(M) > 1e-9]), 1)
def lie_dim(gens, cap=300):
    basis, mats = [], []
    def add(X):
        v = np.concatenate([X.ravel().real, X.ravel().imag])
        for b in basis: v = v - (b @ v) * b
        if np.linalg.norm(v) > 1e-8: basis.append(v / np.linalg.norm(v)); mats.append(X); return True
        return False
    for g in gens: add(g)
    i = 0
    while i < len(mats) < cap:
        for j in range(i): add(mats[i] @ mats[j] - mats[j] @ mats[i])
        i += 1
    return len(mats)

# =============================================== A. 1+1D template =========================================================
print('== A. 1+1D staggered chain h = (i/2) sum (c_j^+ c_j+1 - h.c.): the template')
def chain(L):
    T = np.roll(np.eye(L), 1, axis=0); h = 0.5j * (T - T.T); QV = bdg(np.eye(L), np.zeros((L, L)))
    QA = bdg((T + T.T) / 2, (T - T.T) / 2); return T, h, QV, QA
L = 12; T, h, QV, QA = chain(L); hB = Ub(expm(-1j * h)); v0 = np.ones(L) / np.sqrt(L); vp = (-1.0) ** np.arange(L) / np.sqrt(L)
e0 = np.concatenate([v0, 0 * v0]); ep = np.concatenate([vp, 0 * vp]); vel = lambda v: float((v @ (0.5 * (T + T.T)) @ v))
check('A1 [T] Kitaev-pairing axial charge Q_A (BdG [[cos k, i sin k], [-i sin k, -cos k]]): conserved, Q_A^2 = 1 (integer '
      'spectrum), sum of commuting Majorana pairs (a_j, b_j+1); Q_A = +1 on the k = 0 node, -1 on the k = pi node (opposite movers)',
      nrm(QA @ hB - hB @ QA) < 1e-13 and nrm(QA @ QA - np.eye(2 * L)) < 1e-13 and matching(QA)
      and np.allclose(QA @ e0, e0) and np.allclose(QA @ ep, -ep) and vel(v0) * vel(vp) < 0, f'velocities {-vel(v0):+.0f}, {-vel(vp):+.0f}')
dims = [lie_dim([1j * chain(l)[2], 1j * chain(l)[3]]) for l in (4, 6, 8, 10, 12)]
check('A2 [T] [Q_V, Q_A] != 0 and the Lie algebra they generate grows linearly with L (Onsager): each charge alone is a U(1), '
      'the pair is not U(1) x U(1)', nrm(QV @ QA - QA @ QV) > 0.5 and all(np.diff(dims) > 0), f'dim at L = 4..12: {dims}')
QR = (QV - QA) / 2; evR = np.sort(np.abs(np.linalg.eigvalsh(QR))); ks = 2 * np.pi * np.arange(L) / L
qv = lambda j: bdg(np.diag(np.eye(L)[j]), np.zeros((L, L)))
def qa(j):
    A = np.zeros((L, L)); B = np.zeros((L, L)); k = (j + 1) % L; A[j, k] = A[k, j] = 0.25; B[j, k] = -0.25; B[k, j] = 0.25; return bdg(A, B)
dens = nrm(sum(qa(j) for j in range(L)) * 2 - QA)
cR = nrm((qv(0) - 2 * qa(0)) @ (qv(1) - 2 * qa(1)) - (qv(1) - 2 * qa(1)) @ (qv(0) - 2 * qa(0)))
check('A3 [T] the single-chirality charge (Q_V - Q_A)/2 is not quantised: its BdG levels |sin(k/2)| run from 0 to 1, so by T1\' '
      'no split into commuting local parts exists (the natural split fails) and it can carry no link', np.allclose(evR, np.sort(np.abs(np.concatenate([np.sin(ks / 2), np.sin(ks / 2)])))) and dens < 1e-13 and cR > 0.1,
      f'|[q_R(0), q_R(1)]| = {cR:.2f}')
def ok1d(R, Lm):
    qs = {abs(q) for q in R + Lm}
    return all(sum(abs(q) == a for q in R) == sum(abs(q) == a for q in Lm) for a in qs)
check('A4 [T] T1 in 1+1D (#R(+-q) = #L(+-q) for every |q|): the template (R: -1, L: +1) passes; the anomaly-free 3450 set '
      '(R: 5, 0; L: 3, 4; 25 + 0 = 9 + 16) fails, so no free chain carries it as an exact quantised one-body charge',
      ok1d([-1], [1]) and not ok1d([5, 0], [3, 4]) and 25 + 0 == 9 + 16)

# =============================================== B. CL-1 tick ==============================================================
print('== B. CL-1 cube tick (equal edges): staggered particle-hole map and exact quantised non-on-site charges')
Cc = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for c in Cc:
    n_ = (2 * c - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
def hop8(sel, sign):
    H = np.zeros((8, 8), complex)
    for a in range(8):
        for b in range(8):
            if sel(Cc[a] - Cc[b]): g = XI[a].conj() @ XI[b]; H[a, b] = sign * g / abs(g) / np.sqrt(3)
    return H
W8 = hop8(lambda d: np.abs(d).sum() == 1, -1.0); Wi8 = [hop8(lambda d, i=i: np.abs(d).sum() == 1 and d[i] != 0, -1.0) for i in range(3)]
F8 = hop8(lambda d: np.abs(d).sum() == 2, 1.0); S8 = np.diag((-1.0) ** Cc.sum(1)); s3 = -S8 @ F8; I8 = np.eye(8)
Ri = [np.sqrt(3) * w for w in Wi8]; sc8 = 1j * Ri[0] @ Ri[1] @ Ri[2] @ W8                        # cube copy sign
class Torus:
    def __init__(s, L):
        s.L = np.array(L); s.sites = np.array(list(itertools.product(*[range(l) for l in L]))); s.N = len(s.sites)
        s.idx = {tuple(x): i for i, x in enumerate(s.sites)}; s.lab = (s.sites % 2) @ [4, 2, 1]; s.S = np.diag((-1.0) ** s.sites.sum(1))
        s.cubes = {o: [[s.idx[tuple((np.array(b) + o + c) % s.L)] for c in Cc] for b in itertools.product(*[range(0, l, 2) for l in L])] for o in (0, 1)}
    def embed(s, o, m8s):
        M = np.zeros((s.N, s.N), complex)
        for k, ids in enumerate(s.cubes[o]):
            m8 = m8s[k] if isinstance(m8s, list) else m8s; lb = s.lab[ids]; M[np.ix_(ids, ids)] += m8[np.ix_(lb, lb)]
        return M
    def trans(s, d):
        T = np.zeros((s.N, s.N))
        for i, x in enumerate(s.sites): T[s.idx[tuple((x + d) % s.L)], i] = 1
        return T
    def gauge(s):
        A = [s.embed(0, W8), s.embed(1, W8)]; X = A[0] + A[1]; ph = np.full(s.N, np.nan); ph[0] = 0; q = deque([0])
        while q:
            i = q.popleft()
            for j in np.nonzero(np.abs(X[i]) > 1e-12)[0]:
                if np.isnan(ph[j]): ph[j] = ph[i] - np.angle(X[i, j]); q.append(j)
        s.D = np.diag(np.exp(1j * ph)); s.We, s.Wo = [s.D.conj().T @ a @ s.D for a in A]; return s
def R8(w): w = np.asarray(w, float); return sum(w[i] * Ri[i] for i in range(3)) / np.linalg.norm(w)
def tick(t, eps=np.pi / 3, mu=0.0, M=0.0, wts=None, ph=None):
    """CL-1 tick u = U_o C U_e C in the real gauge (C: copy mass on even cubes; wts: per-cube hop weights; ph: link phases)"""
    Rs = {o: [R8(np.ones(3) if wts is None else wts[o][k]) for k in range(len(t.cubes[o]))] for o in (0, 1)}
    Ge = t.embed(0, Rs[0]); Go = t.embed(1, Rs[1])
    if ph is not None: Ge = Ge * ph; Go = Go * ph
    Ue = expm(-1j * (eps - mu / 2) * Ge); Uo = expm(1j * (eps + mu / 2) * Go)
    if M:
        Cm = t.embed(0, [expm(1j * (M / 4) * (I8 - 1j * Ri[0] @ Ri[1] @ Ri[2] @ R) @ R) for R in Rs[0]]); Ue = Cm @ Ue @ Cm
    D = t.D; return D.conj().T @ Uo @ Ue @ D, D.conj().T @ Uo @ D
t4 = Torus((4, 4, 4)).gauge(); N4 = t4.N; S4 = t4.S
u4, Uo4 = tick(t4); rng = np.random.default_rng(20261022)
wts = {o: [1 + 0.3 * rng.random(3) for _ in t4.cubes[o]] for o in (0, 1)}
th = rng.uniform(-0.3, 0.3, (N4, N4)); lph = np.exp(1j * (th - th.T))
psk = lambda u: nrm(S4 @ u.conj() @ S4 - u)
vals = [psk(tick(t4, *a)[0]) for a in ((np.pi / 3, 0), (0.7, 0.2))] + [psk(tick(t4, wts=wts)[0])]
brk = [psk(tick(t4, M=0.3)[0]), psk(tick(t4, ph=lph)[0])]
check('B1 [T] every face carries pi flux, so a site gauge makes both tilings\' hops real; then the staggered particle-hole map '
      'S conj(u) S = u holds for every step, mass and real hop weights (curved edges); the copy mass and link phases break it',
      nrm(t4.We.imag) < 1e-13 and nrm(t4.Wo.imag) < 1e-13 and max(vals) < 1e-13 and min(brk) > 1e-2, f'copy mass {brk[0]:.3f}, links {brk[1]:.3f}')
# glide: V maps W_e <-> W_o; G = U_o S V commutes with the tick at mu = M = 0
T111 = t4.trans(np.array([1, 1, 1])); X1 = T111 @ t4.We @ T111.T; X2 = T111 @ t4.Wo @ T111.T
lam = np.full(N4, np.nan); lam[0] = 1; q = deque([0])
while q:
    i = q.popleft()
    for j in np.nonzero((np.abs(t4.Wo[i]) > 1e-12) | (np.abs(t4.We[i]) > 1e-12))[0]:
        if np.isnan(lam[j]): lam[j] = lam[i] * (t4.Wo[i, j] / X1[i, j] if abs(t4.Wo[i, j]) > 1e-12 else t4.We[i, j] / X2[i, j]).real; q.append(j)
V = np.diag(lam) @ T111; G = Uo4 @ S4 @ V
t8 = Torus((8, 4, 4)).gauge(); N8 = t8.N; u8 = tick(t8)[0]; Tx = t8.D.conj().T @ t8.trans(np.array([2, 0, 0])) @ t8.D
QT = Qof(Tx, t8.S); Qu = Qof(u4, S4); QG = Qof(G, S4, -1); QV4 = bdg(np.eye(N4), 0 * np.eye(N4)); QV8 = bdg(np.eye(N8), 0 * np.eye(N8))
def good(Q, u): n = len(u); tx = np.block([[0 * np.eye(n), np.eye(n)], [np.eye(n), 0 * np.eye(n)]]); U = Ub(u); return max(nrm(Q @ U - U @ Q), nrm(Q @ Q - np.eye(2 * n)), nrm(tx @ Q.conj() @ tx + Q))
errs = [good(QT, u8), good(Qu, u4), good(QG, u4)]; pair = [nrm(Q[:len(Q) // 2, len(Q) // 2:]) for Q in (QT, Qu, QG)]
ncom = [nrm(QV8 @ QT - QT @ QV8), nrm(QV4 @ Qu - Qu @ QV4), nrm(QV4 @ QG - QG @ QV4)]
check('B2 [T] three exact quantised non-on-site charges from conserved unitaries Y (translation by one block, the tick itself, the '
      'glide G = U_o S V): Q^2 = 1, particle-hole consistent, conserved; each has pairing and fails to commute with fermion number',
      max(errs) < 1e-12 and min(pair) > 0.1 and min(ncom) > 0.1 and nrm(G @ u4 - u4 @ G) < 1e-12, 'max err %.1e; pairing %.2f %.2f %.2f' % (max(errs), *pair))
dimsT = []
for n in (2, 3, 4, 5, 6):
    tn = Torus((2 * n, 2, 2)).gauge(); Tn = tn.D.conj().T @ tn.trans(np.array([2, 0, 0])) @ tn.D
    dimsT.append(lie_dim([1j * bdg(np.eye(tn.N), 0 * np.eye(tn.N)), 1j * Qof(Tn, tn.S)]))
check('B3 [T] the translation charge is a perfect Majorana matching (commuting local parts, so individually gaugeable) and with '
      'fermion number generates an algebra growing with length (Onsager type)', matching(QT) and all(np.diff(dimsT) > 0), f'dims at Lx = 4..12: {dimsT}')
uc = tick(t8, wts={o: [1 + 0.3 * rng.random(3) for _ in t8.cubes[o]] for o in (0, 1)})[0]; Quc = Qof(uc, t8.S)
b4 = [nrm(QT @ Ub(uc) - Ub(uc) @ QT), nrm(QG @ Ub(tick(t4, mu=0.1)[0]) - Ub(tick(t4, mu=0.1)[0]) @ QG), nrm(QG @ Ub(tick(t4, M=0.3)[0]) - Ub(tick(t4, M=0.3)[0]) @ QG)]
check('B4 [T] backgrounds: curved edges break the translation charge but not the tick charge; the mass and the copy mass break the '
      'glide charge; link phases break every pairing charge (B1: S o conj is charge conjugation)', good(Quc, uc) < 1e-12 and min(b4) > 1e-2,
      'curved %.3f, mass %.3f, copy mass %.3f' % tuple(b4))
# light states at Gamma and their chirality
w0, V0 = np.linalg.eig(u4); P = np.linalg.qr(V0[:, np.abs(np.angle(w0)) < 1e-8])[0]
dsp = [((t4.sites[:, j][:, None] - t4.sites[:, j][None, :] + 2) % 4 - 2).astype(float) for j in range(3)]
We0, Wo0 = t4.embed(0, W8), t4.embed(1, W8)
def uA(a):
    ph = np.exp(1j * sum(a[j] * dsp[j] for j in range(3))); return t4.D.conj().T @ expm(1j * np.pi / 3 * Wo0 * ph) @ expm(-1j * np.pi / 3 * We0 * ph) @ t4.D
Vj = [1j * P.conj().T @ (uA(1e-5 * np.eye(3)[j]) - uA(-1e-5 * np.eye(3)[j])) @ P / 2e-5 for j in range(3)]
c2 = np.trace(Vj[0] @ Vj[0]).real / P.shape[1]; g5 = -1j * Vj[0] @ Vj[1] @ Vj[2] / c2 ** 1.5
lt = lambda Q: (P.conj().T @ Q[:N4, :N4] @ P, P.conj().T @ Q[:N4, N4:] @ P.conj())
Al_u, Bl_u = lt(Qu); Al_G, Bl_G = lt(QG); Gl = P.conj().T @ G @ P
P8 = np.linalg.qr(np.linalg.eig(u8)[1][:, np.abs(np.angle(np.linalg.eig(u8)[0])) < 1e-8])[0]; AT = P8.conj().T @ QT[:N8, :N8] @ P8
check('B5 [T] on the 8 light states at Gamma (two Dirac copies, speed 1 site/tick): the translation and tick charges act as fermion '
      'number (+1, no pairing); the glide charge is pure pairing (a Pauli-Gursey flavour turn); the glide itself is -g5 (discrete)',
      P.shape[1] == 8 and abs(c2 - 1) < 1e-6 and nrm(g5 @ g5 - np.eye(8)) < 1e-8 and nrm(AT - np.eye(8)) < 1e-10 and nrm(Al_u - np.eye(8)) < 1e-10
      and nrm(Bl_u) < 1e-10 and nrm(Al_G) < 1e-10 and nrm(Bl_G) > 0.1 and nrm(Gl + g5) < 1e-8, f'tr(G g5)/8 = {np.trace(Gl @ g5).real / 8:+.3f}')
del t8, u8, Tx, QT, QV8, uc, Quc, P8, AT; gc.collect()

# =============================================== C. range-1 commutant ======================================================
print('== C. every range-1 conserved one-body operator (Bloch, exact on the 5^3 grid)')
NS = [np.array(n) for n in itertools.product(range(-1, 2), repeat=3)]; NSI = {tuple(n): k for k, n in enumerate(NS)}
def Dg(K): return np.diag(np.exp(1j * (Cc @ K)))
def uB(K, eps=np.pi / 3, mu=0.0, M=0.0):
    Cm = expm(1j * (M / 4) * (I8 - sc8) @ W8)
    return Dg(K).conj().T @ expm(1j * (eps + mu / 2) * W8) @ Dg(K) @ Cm @ expm(-1j * (eps - mu / 2) * W8) @ Cm
def gram_null(build, extra=None):
    nb = len(NS); G = np.zeros((nb, 64, nb, 64), complex)
    for k in itertools.product(range(5), repeat=3):
        K = 2 * np.pi * np.array(k) / 5; acc = build(K); ph = np.exp(1j * (np.array(NS) @ K))
        for i in range(nb): G[i] += ph[i].conj() * np.einsum('j,ab->ajb', ph, acc)
    G = G.reshape(nb * 64, nb * 64)
    if extra: extra(G)
    top = np.abs(G).max(); ev, Vv = eigh(G, subset_by_value=(-np.inf, 1e-7 * top), driver='evr'); del G; gc.collect(); return Vv
def comm_nc(uf):
    def b(K): U = uf(K); Mk = np.kron(U.T, I8) - np.kron(I8, U); return Mk.conj().T @ Mk
    return gram_null(b)
def comm_pair(uf):
    def b(K): Mk = np.kron(uf(-K).conj().T, I8) - np.kron(I8, uf(K)); return Mk.conj().T @ Mk
    Tp = np.zeros((64, 64))
    for a in range(8):
        for c in range(8): Tp[a + 8 * c, c + 8 * a] = 1
    def anti(G):
        for i, n in enumerate(NS):
            j = NSI[tuple(-n)]; G[64*i:64*i+64, 64*i:64*i+64] += 10 * np.eye(64); G[64*j:64*j+64, 64*j:64*j+64] += 10 * np.eye(64)
            G[64*i:64*i+64, 64*j:64*j+64] += 10 * Tp; G[64*j:64*j+64, 64*i:64*i+64] += 10 * Tp
    return gram_null(b, anti)
def Xof(z, K): return np.tensordot(np.exp(1j * (np.array(NS) @ K)), z.reshape(27, 8, 8).transpose(0, 2, 1), 1)
def light(uf):
    w0, V0 = np.linalg.eig(uf(np.zeros(3))); P = np.linalg.qr(V0[:, np.abs(np.angle(w0)) < 1e-8])[0]
    Vj = [1j * P.conj().T @ (uf(1e-5 * np.eye(3)[j]) - uf(-1e-5 * np.eye(3)[j])) @ P / 2e-5 for j in range(3)]
    c2 = np.trace(Vj[0] @ Vj[0]).real / P.shape[1]; return P, -1j * Vj[0] @ Vj[1] @ Vj[2] / c2 ** 1.5
res = {}
for M in (0.0, 0.3):
    uf = lambda K, M=M: uB(K, M=M); Z = comm_nc(uf); P, g5b = light(uf)
    ims = np.array([(P.conj().T @ Xof(Z[:, k], np.zeros(3)) @ P).ravel() for k in range(Z.shape[1])]).T
    co = np.linalg.lstsq(ims, g5b.ravel(), rcond=None)[0]; r5 = np.linalg.norm(ims @ co - g5b.ravel())
    res[M] = (Z.shape[1], np.linalg.matrix_rank(ims, tol=1e-8), r5)
    if M == 0.0:
        z = Z @ co; Ks = rng.uniform(-np.pi, np.pi, (300, 3))
        ev5 = np.array([np.linalg.eigvalsh((Xof(z, K) + Xof(z, K).conj().T) / 2) for K in Ks]); cm5 = max(nrm(Xof(z, K) @ uf(K) - uf(K) @ Xof(z, K)) for K in Ks[:20])
    del Z, ims; gc.collect()
check('C1 [T] without the copy mass the light image of the range-1 conserved one-body operators is all of {1, g5} x M2(copies): '
      'chiral conserved operators exist; [F] the minimal one equal to g5 at Gamma is dispersive, with levels falling from 1 to near 0',
      res[0.0][1] == 8 and res[0.0][2] < 1e-8 and cm5 < 1e-12 and np.abs(ev5).min() < 0.05, f'dim {res[0.0][0]}; levels |.| in [{np.abs(ev5).min():.4f}, {np.abs(ev5).max():.3f}]')
Zp = comm_pair(lambda K: uB(K, M=0.3)); Pm, _ = light(lambda K: uB(K, M=0.3))
Bl = max(nrm(Pm.conj().T @ Xof(Zp[:, k], np.zeros(3)) @ Pm.conj()) for k in range(Zp.shape[1]))
check('C2 [T] with the copy mass (M = 0.3) the light image of the number-conserving ones is fermion number alone and the '
      'pairing ones vanish on the light copy: no range-1 conserved one-body operator acts on it chirally, on-site or not',
      res[0.3][1] == 1 and res[0.3][2] > 1e-2 and Zp.shape[1] == 3 and Bl < 1e-10, f'dims {res[0.3][0]} + {Zp.shape[1]} pairing; g5 residual {res[0.3][2]:.3f}')
del Zp; gc.collect()

# =============================================== D. theorem T1 bookkeeping =================================================
print('== D. T1: a one-body charge with K-independent spectrum is vector-like on the massless content')
def Hp(K): Wo = Dg(K).conj().T @ W8 @ Dg(K); return 0.5j * (Wo @ W8 - W8 @ Wo)
ax = []
for K0 in (np.zeros(3), np.full(3, np.pi)):
    Vh = [(Hp(K0 + 1e-5 * np.eye(3)[j]) - Hp(K0 - 1e-5 * np.eye(3)[j])) / 2e-5 for j in range(3)]
    for sg in (-1, 1):
        w_, v_ = np.linalg.eigh(s3); Pc = v_[:, np.isclose(w_, sg)]; Vc = [Pc.conj().T @ v @ Pc for v in Vh]
        c2 = np.trace(Vc[0] @ Vc[0]).real / 4; g5c = -1j * Vc[0] @ Vc[1] @ Vc[2] / c2 ** 1.5; ax.append(np.trace(Pc.conj().T @ S8 @ Pc @ g5c).real / 4)
t8 = Torus((8, 4, 4)).gauge(); Hr = 0.5j * (t8.Wo @ t8.We - t8.We @ t8.Wo); Tx = t8.D.conj().T @ t8.trans(np.array([2, 0, 0])) @ t8.D
QK = bdg((Tx + Tx.T) / 2, (Tx - Tx.T) / 2); HB = np.block([[Hr, 0 * Hr], [0 * Hr, -Hr.conj()]])
check("D1 [T] H': purely imaginary in the real gauge (so c -> c^+ is a symmetry and Kitaev-type pairing charges are exact); its "
      "on-site sublattice charge S is quantised and chiral node by node, with axial charges summing to zero over the four massless "
      "Dirac points (light, mirror at Gamma; light, mirror at R), as T1 requires", nrm(Hr.real) < 1e-13 and nrm(QK @ HB - HB @ QK) < 1e-12
      and nrm(QK @ QK - np.eye(2 * t8.N)) < 1e-12 and np.allclose(ax, [-1, 1, 1, -1], atol=1e-6), 'S axial: ' + ' '.join(f'{a:+.0f}' for a in ax))
del t8, Hr, Tx, QK, HB; gc.collect()
fam = [Fr(1, 6)] * 6 + [Fr(-2, 3)] * 3 + [Fr(1, 3)] * 3 + [Fr(-1, 2)] * 2 + [Fr(1)] + [Fr(0)]
sym = lambda ms: all(ms.count(y) == ms.count(-y) for y in set(ms))
check('D2 [T] exact fractions: the 16 hypercharges (left-handed, with nu_R) are anomaly-free (sum y = sum y^3 = 0) but not '
      'symmetric under y -> -y for any family number (+1/6: 6N, -1/6: 0); 16 + 16bar is; the axial charge of one Dirac (-1, -1) is not',
      all(sum(fam) == 0 and sum(y ** 3 for y in fam) == 0 and not sym(fam * Nf) for Nf in (1, 2, 3)) and sym(fam + [-y for y in fam]) and not sym([-1, -1]),
      'so no free update with this light content conserves a quantised one-body hypercharge, on-site or not')

# =============================================== E. measured checks ========================================================
print('== E. measured checks')
t12 = Torus((12, 2, 2)).gauge(); u12 = tick(t12)[0]; reach = []
for n in (1, 2, 3):
    Un = np.linalg.matrix_power(u12, n); dx = np.abs((t12.sites[:, 0][:, None] - t12.sites[:, 0][None, :] + 6) % 12 - 6)
    reach.append(int(dx[np.abs(Un) > 1e-12].max()))
wR = np.sort(np.angle(np.linalg.eigvals(uB(np.full(3, np.pi)))))
check('E1 [T] the charges leave the update unchanged: strict cone of 2 sites per tick, light speed sin(eps)/sqrt3 = 1/2 block per '
      'tick, partner at R gapped at exactly +-2 eps (no doubler is released; the translation charge gives it -1)',
      reach == [2, 4, 6] and np.allclose(wR, [-2 * np.pi / 3] * 4 + [2 * np.pi / 3] * 4), f'reach {reach}')
print('   [M] V - A: by T1 and C2 every link CL-3 can attach couples vector-like; parity-violating weak observables then vanish,')
print('       against measured mu-decay P_mu xi = 1.0008 (TWIST) and the neutron beta asymmetry A = -0.1196: the route fails as a free update')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('theorems/exact: A1-A4, B1-B5, C1-C2 (C1 last clause finite), D1-D2, E1. Supplied: the CL-1 tick and H\', eps = pi/3, M = 0.3, mu = 0.1,')
print('  random edge weights and link phases, the SM 16 (for D2). Cited: Nielsen-Ninomiya, Chatterjee-Pace-Shao, Gioia-Thorngren, TWIST, PDG.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
