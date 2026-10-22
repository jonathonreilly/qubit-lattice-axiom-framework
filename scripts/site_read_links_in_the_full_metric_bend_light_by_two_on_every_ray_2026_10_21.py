#!/usr/bin/env python3
"""links-metric: the CL-3 link reading of the full metric (lapse, inverse spatial metric, shift, shear) on the
centre-bond (Yee) placement, and light bending, Shapiro delay and frame dragging of photon packets in weak static fields
under the fixed-4-volume clause.  Supplied models; exact identities and finite diagnostics; no physical identification.

Link reading (lattice units: cube = 1, tick = 1).  Links A on the bonds between neighbouring even-cube centres; their
spatial plaquettes B = curl A are the faces pierced by odd-centre bonds.  Each site s pairs its even centre w with its
odd cube P: it carries the three bonds of P's centre cell that meet at w and the three faces of that cell that contain w.
The plaquette phase per tick is a sum over sites, each read from the metric (N, beta, gamma_ij) of its two cubes:
   L_s = (1/8)[ 1/2 Et_s . (sqrt(gamma)/N) gamma^ij Et_s  -  1/2 B_s . (N/sqrt(gamma)) gamma_ij B_s ],
   Et_s = (A(t+1) - A(t)) + beta x B = F_0i - beta^k F_ki  (electric plaquette along the slice normal, B at mid-tick).
 A  exact: 3+1 identity; gauge invariance and Gauss law; the cone is the null cone of the edges; diagonal cells equal
    the CL-1 fermion band at every K
 B  the placement: one-to-one (Yee) pairing cannot read shear; the site pairing is the minimal change
 C  photon packets in metric gradients follow the eikonal of the lattice dispersion (lapse, gamma, shear, shift)
 D  weak static fields (radial and second trace-fixed gauge): bending, Shapiro delay, frame dragging, photon = fermion cone
 E  estimates against measurement
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/SITE_READ_LINKS_IN_THE_FULL_METRIC_BEND_LIGHT_BY_TWO_ON_EVERY_RAY_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp
import scipy.sparse as sps
from scipy.sparse.linalg import splu
from scipy.linalg import expm
from scipy.optimize import brentq

T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022); r3 = np.sqrt(3.0)
E0 = 0.3; TAU0 = np.sin(E0) / r3                       # flat cell: proper tick per tick (cube edge = 1)

# ------------------------------------------------------------------ photon: site-read plaquette phase, Fourier
SIG = np.array(list(itertools.product((1, -1), repeat=3)), float)
EPS3 = np.zeros((3, 3, 3))
for a_, b_, c_ in itertools.permutations(range(3)): EPS3[a_, b_, c_] = np.linalg.det(np.eye(3)[[a_, b_, c_]])
def curlK(K):
    d = 2j * np.sin(np.asarray(K, float) / 2)
    return np.array([[0, -d[2], d[1]], [d[2], 0, -d[0]], [-d[1], d[0], 0]])
def site_weights(Nl, beta, gl, onetoone=False):
    gu = np.linalg.inv(gl); sq = np.sqrt(np.linalg.det(gl)); wE = sq / Nl * gu; wB = Nl / sq * gl
    if onetoone: wE, wB = np.diag(np.diag(wE)), np.diag(np.diag(wB))
    return wE, wB, np.einsum('kil,k->il', EPS3, beta)
def parts(K, Nl, beta, gl, onetoone=False):
    K = np.asarray(K, float); wE, wB, X = site_weights(Nl, beta, gl, onetoone)
    WE = np.zeros((3, 3), complex); WB = WE.copy(); Y = WE.copy(); Z = WE.copy()
    for s in SIG:
        P = np.diag(np.exp(1j * s * K / 2)); Q = np.diag([np.exp(1j * (s @ K - s[l] * K[l]) / 2) for l in range(3)])
        WE += P.conj().T @ wE @ P; WB += Q.conj().T @ wB @ Q; Y += P.conj().T @ wE @ X @ Q; Z += Q.conj().T @ X.T @ wE @ X @ Q
    C = curlK(K); Ch = C.conj().T; Y /= 8
    return WE / 8, Y @ C - Ch @ Y.conj().T, Ch @ Z @ C / 8, Ch @ WB @ C / 8, WB / 8
def Mst(w, pr):                          # plane-wave symbol of the action, cancellation-free form
    WE, Yp, CZC, CBC = pr[:4]
    return 0.5 * (4 * np.sin(w / 2) ** 2 * WE - 1j * np.sin(w) * Yp + np.cos(w / 2) ** 2 * CZC - CBC)
def wcone(K, Nl, beta, gl): return Nl * np.sqrt(K @ np.linalg.inv(gl) @ K) - beta @ K
def freqs(K, Nl, beta, gl, onetoone=False, wt=None, span=0.4):
    """the two positive-frequency roots (polarisations) of det' M(w) = 0 near wt"""
    K = np.asarray(K, float); pr = parts(K, Nl, beta, gl, onetoone); wt = wcone(K, Nl, beta, gl) if wt is None else wt
    f = lambda w, j: np.linalg.eigvalsh(Mst(w, pr))[j]
    return np.array([brentq(f, (1 - span) * wt, (1 + span) * wt, args=(j,), xtol=1e-300, rtol=1e-15, maxiter=200) for j in (1, 0)])
def companion(K, Nl, beta, gl):
    WE, Yp, CZC, CBC, _ = parts(K, Nl, beta, gl)
    A0 = 0.5 * (2 * WE + 0.5 * CZC - CBC); A1 = 0.5 * (-WE - 0.5 * Yp + 0.25 * CZC); A1i = np.linalg.inv(A1)
    return np.linalg.eigvals(np.block([[np.zeros((3, 3)), np.eye(3)], [-A1i @ A1.conj().T, -A1i @ A0]]))
def rd_photon(h00, hij, h0i, box=False):
    g = np.diag([-1.0, 1, 1, 1]); g[0, 0] += h00; g[1:, 1:] += hij; g[0, 1:] = g[1:, 0] = h0i
    if box: return TAU0 * np.sqrt(-g[0, 0]), np.zeros(3), np.diag(np.diag(g[1:, 1:]))
    gi = np.linalg.inv(g); N = 1 / np.sqrt(-gi[0, 0]); beta = -gi[0, 1:] / gi[0, 0]
    return TAU0 * N, TAU0 * beta, g[1:, 1:].copy()
DIRS = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1], [0, 1, 1], [0, 1, -1], [1, 1, 1], [1, -1, 1], [-1, 1, 1]], float)
DIRS /= np.linalg.norm(DIRS, axis=1)[:, None]
AFIT = np.array([[n[0]**2, n[1]**2, n[2]**2, 2*n[0]*n[1], 2*n[0]*n[2], 2*n[1]*n[2]] for n in DIRS])
def sym6(s_): return np.array([[s_[0], s_[3], s_[4]], [s_[3], s_[1], s_[5]], [s_[4], s_[5], s_[2]]])
def photon_fit(Nl, beta, gl, k=1e-3, onetoone=False):
    wf = lambda K: freqs(K, Nl, beta, gl, onetoone).mean()
    b = np.array([-(wf(k * e) - wf(-k * e)) / (2 * k) for e in np.eye(3)])
    y = np.array([(wf(k * n) + k * b @ n) ** 2 / k ** 2 for n in DIRS]); return b, sym6(np.linalg.lstsq(AFIT, y, rcond=None)[0])

# ------------------------------------------------------------------ CL-1 fermion (inlined from shift-shear)
C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8, dtype=complex)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); NV = (2 * C8 - 1.0) / r3; XI = []
for i in range(8):
    _, v_ = np.linalg.eigh(sum(NV[i, k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
WAX = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(a + 1, 8):
        if np.sum(abs(C8[a] - C8[b])) == 1:
            g_ = XI[a].conj() @ XI[b]; x = -g_ / abs(g_) / r3; ax = int(np.argmax(abs(C8[a] - C8[b]))); WAX[ax][a, b] = x; WAX[ax][b, a] = np.conj(x)
NN = [np.diag(C8[:, i]).astype(complex) for i in range(3)]
VOL = (r3 ** 3) * WAX[0] @ WAX[1] @ WAX[2]
def DK(K): return np.diag(np.exp(1j * (C8 @ np.asarray(K, float))))
def Rf(f): f = np.asarray(f, float); return sum(f[i] * WAX[i] for i in range(3)) / np.sqrt(f @ f / 3)
def s3f(f): return 1j * VOL @ Rf(f)
PL3 = None
def halves(f, eps, mu, M):
    R = Rf(f); P = (I8 - s3f(f)) / 2; F = expm(1j * (M / 2) * P @ R)
    return F @ expm(-1j * (eps - mu / 2) * R) @ F, expm(1j * (eps + mu / 2) * R)
def fineU(K, f, eps, mu, M):
    Ue, Uo = halves(f, eps, mu, M); Dm = DK(K); return Dm @ Uo @ Dm.conj().T @ Ue
def lightpos(U, Pl):
    ev, V = np.linalg.eig(U); w = -np.angle(ev); lw = np.linalg.norm(Pl @ V, axis=0); return np.sort(w[(lw > 0.7) & (w > 0)])
PL3 = (I8 + s3f([1, 1, 1])) / 2
NC = C8.copy(); SY = np.array([[0, -1j], [1j, 0]]); I2 = np.eye(2)
JC = [np.kron(np.kron(*(SY if q == i else I2 for q in (0, 1))), SY if i == 2 else I2) for i in range(3)]
IDX = lambda n, c: 8 * int(n @ [4, 2, 1]) + int(c @ [4, 2, 1])
ODDS = [([IDX((n0 + 1 - c) % 2, c) for c in C8], ((n0 == 1) & (C8 == 0)).astype(float)) for n0 in NC]
DCM = np.repeat((NC == 0).astype(float), 8, axis=0)
def coarseU(Q, Ue, Uo, X):
    SA = expm(-1j * X); d = np.exp(1j * DCM @ np.asarray(Q, float)); U = np.zeros((64, 64), complex)
    for ids, mask in ODDS:
        ph = np.exp(1j * mask @ Q); U[np.ix_(ids, ids)] = ph.conj()[:, None] * Uo * ph[None, :]
    return U @ (d.conj()[:, None] * SA.conj().T * d[None, :]) @ SA @ np.kron(np.eye(8), Ue)
def Xins(b, sig, f, eps):
    E = expm(-1j * eps * Rf(f)); V = [NN[j] - E @ NN[j] @ E.conj().T for j in range(3)]; f = np.asarray(f, float); th = np.arcsin(np.asarray(b, float)) / 2
    return sum(np.kron(JC[i], -th[i] * I8 + 0.25 * sum(sig[i, j] * f[i] / f[j] * V[j] for j in range(3) if j != i)) for i in range(3))
def wpos(K, Ue, Uo, X, ref):
    w = -np.angle(np.linalg.eigvals(coarseU(2 * K, Ue, Uo, X))); return np.mean(np.sort(w[np.argsort(np.abs(np.angle(np.exp(1j * (w - ref)))))[:2]]))
def fermion_fit(f, eps, b, sig, k=1e-3, M=0.5):
    Ue, Uo = halves(f, eps, 0.0, M); Pl = (I8 + s3f(f)) / 2; X = Xins(b, sig, f, eps)
    wf = lambda K: wpos(K, Ue, Uo, X, lightpos(DK(K) @ Uo @ DK(K).conj().T @ Ue, Pl).mean())
    bt = np.array([-(wf(k * e) - wf(-k * e)) / (2 * k) for e in np.eye(3)])
    y = np.array([(wf(k * n) + k * bt @ n) ** 2 / k ** 2 for n in DIRS]); return bt, sym6(np.linalg.lstsq(AFIT, y, rcond=None)[0]), wf

print('== A. the link reading (exact)')
# A1 3+1 identity, exact rationals
import random; random.seed(7); Rq = lambda: sp.Rational(random.randint(-9, 9), random.randint(10, 30))
Nq = 1 + Rq(); bq = sp.Matrix([Rq() for _ in range(3)]); Hq = sp.zeros(3, 3)
for i in range(3):
    for j in range(i, 3): Hq[i, j] = Hq[j, i] = Rq() / 3
gq = sp.eye(3) + Hq; G4 = sp.zeros(4, 4); G4[0, 0] = -Nq ** 2 + (bq.T * gq * bq)[0]
for i in range(3):
    G4[0, i + 1] = G4[i + 1, 0] = (gq * bq)[i]
    for j in range(3): G4[i + 1, j + 1] = gq[i, j]
G4i = G4.inv(); Fq = sp.zeros(4, 4)
for a in range(4):
    for b in range(a + 1, 4): Fq[a, b] = Rq(); Fq[b, a] = -Fq[a, b]
lhs = -sp.Rational(1, 4) * Nq * sp.sqrt(gq.det()) * sum(G4i[m, a] * G4i[n, b] * Fq[m, n] * Fq[a, b] for m in range(4) for n in range(4) for a in range(4) for b in range(4))
Etq = sp.Matrix([Fq[0, i + 1] - sum(bq[k] * Fq[k + 1, i + 1] for k in range(3)) for i in range(3)]); Bq = sp.Matrix([Fq[2, 3], Fq[3, 1], Fq[1, 2]])
rhs = sp.Rational(1, 2) * sp.sqrt(gq.det()) / Nq * (Etq.T * gq.inv() * Etq)[0] - sp.Rational(1, 2) * Nq / sp.sqrt(gq.det()) * (Bq.T * gq * Bq)[0]
check('A1 theorem (3+1 identity, exact rationals): -1/4 sqrt(-g) F.F = 1/2 (sqrt(gamma)/N) gamma^ij Et_i Et_j - 1/2 (N/sqrt(gamma)) gamma_ij B^i B^j, Et_i = F_0i - beta^k F_ki: lapse, shift, inverse metric and shear all sit in two site weights',
      sp.simplify(lhs - rhs) == 0, 'difference = 0')

# ------------------------------------------------------------------ the same action on a z line (Bloch Kx, Ky), sparse
def line_ops(Nz, Kb, fields, onetoone=False):
    """A index 3p + c (A_x, A_y at (1/2,0,p), (0,1/2,p); A_z at (0,0,p+1/2)); faces B_x, B_y at p+1/2, B_z at p.
    fields(zs) -> (Nl, beta, gl) at the site position zs (between its even centre p and odd centre p +- 1/2)."""
    Kx, Ky = Kb; n = 3 * Nz; trip = {k: ([], [], []) for k in 'EBYZ'}
    for p in range(Nz):
        for s in SIG:
            zl = p if s[2] > 0 else (p - 1) % Nz
            P = [(3 * p, np.exp(1j * s[0] * Kx / 2)), (3 * p + 1, np.exp(1j * s[1] * Ky / 2)), (3 * zl + 2, 1.0)]
            Q = [(3 * zl, np.exp(1j * s[1] * Ky / 2)), (3 * zl + 1, np.exp(1j * s[0] * Kx / 2)), (3 * p + 2, np.exp(1j * (s[0] * Kx + s[1] * Ky) / 2))]
            wE, wB, X = site_weights(*fields(p + s[2] / 4), onetoone)
            for key, Ls, Mid, Rs in (('E', P, wE, P), ('B', Q, wB, Q), ('Y', P, wE @ X, Q), ('Z', Q, X.T @ wE @ X, Q)):
                for a in range(3):
                    for b in range(3):
                        if Mid[a, b] != 0:
                            trip[key][0].append(Ls[a][0]); trip[key][1].append(Rs[b][0]); trip[key][2].append(np.conj(Ls[a][1]) * Mid[a, b] * Rs[b][1] / 8)
    M = {k: sps.csr_matrix((v[2], (v[0], v[1])), shape=(n, n)) for k, v in trip.items()}
    r, c, v = [], [], []; sx, sy = 2j * np.sin(Kx / 2), 2j * np.sin(Ky / 2)
    for p in range(Nz):
        q = (p + 1) % Nz
        r += [3*p]*3 + [3*p+1]*3 + [3*p+2]*2; c += [3*p+2, 3*q+1, 3*p+1, 3*q, 3*p, 3*p+2, 3*p+1, 3*p]; v += [sy, -1, 1, 1, -1, -sx, sx, -sy]
    C = sps.csr_matrix((v, (r, c)), shape=(n, n)); Ch = C.conj().T
    r, c, v = [], [], []
    for p in range(Nz): r += [3*p, 3*p+1, 3*p+2, 3*p+2]; c += [p, p, (p+1) % Nz, p]; v += [sx, sy, 1, -1]
    G = sps.csr_matrix((v, (r, c)), shape=(n, Nz))
    Yp = M['Y'] @ C - Ch @ M['Y'].conj().T
    A0 = 0.5 * (2 * M['E'] + 0.5 * Ch @ M['Z'] @ C - Ch @ M['B'] @ C); A1 = 0.5 * (-M['E'] - 0.5 * Yp + 0.25 * Ch @ M['Z'] @ C)
    return dict(A0=A0.tocsc(), A1=A1.tocsc(), C=C, G=G, WE=M['E'], WB=M['B'], Y=M['Y'])
class Line:
    """stationarity of the summed plaquette phase: A1 A(n-1) + A0 A(n) + A1^dag A(n+1) = 0"""
    def __init__(self, Nz, Kb, fields, onetoone=False):
        self.o = line_ops(Nz, Kb, fields, onetoone); self.lu = splu(self.o['A1'].conj().T.tocsc()); self.N = Nz
    def step(self, Am, A): return A, -self.lu.solve(self.o['A0'] @ A + self.o['A1'] @ Am)
    def gauss(self, Am, A):
        o = self.o; return o['G'].conj().T @ (o['WE'] @ (A - Am) - o['Y'] @ (o['C'] @ ((A + Am) / 2)))
    def gauss_fix(self, Am, A):
        o = self.o; Lg = (o['G'].conj().T @ o['WE'] @ o['G']).tocsc() + 1e-14 * sps.eye(self.N, format='csc')
        return Am, A + o['G'] @ splu(Lg).solve(-self.gauss(Am, A))
    def energy(self, Am, A):
        o = self.o; dA = A - Am; B = o['C'] @ ((A + Am) / 2)
        return (np.real(dA.conj() * (o['WE'] @ dA)) + np.real(B.conj() * (o['WB'] @ B))).reshape(self.N, 3).sum(1)
    def pos(self, Am, A): e = self.energy(Am, A); return (e * np.arange(self.N)).sum() / e.sum()

print('   (A2 on a z line of 16 cells, random strong lapse, shift, shear per site; Bloch K = (0.7, -1.1))')
Hr = [rng.normal(size=(3, 3)) * 0.2 for _ in range(64)]
rf = lambda z: (TAU0 * (1 + 0.2 * np.sin(z)), TAU0 * 0.2 * np.array([np.cos(z), np.sin(2 * z), 0.5]), np.eye(3) + (Hr[int(4 * z) % 64] + Hr[int(4 * z) % 64].T) / 2)
ln = Line(16, (0.7, -1.1), rf); o = ln.o
cg = abs(o['C'] @ o['G']).max(); mg = abs((o['A0'] + o['A1'] + o['A1'].conj().T) @ o['G']).max()
Am = rng.normal(size=48) + 1j * rng.normal(size=48); A = rng.normal(size=48) + 1j * rng.normal(size=48); q0 = ln.gauss(Am, A); dq = 0
for _ in range(200): Am, A = ln.step(Am, A); dq = max(dq, np.abs(ln.gauss(Am, A) - q0).max())
check('A2 theorem: the action depends on links only through B = curl A and the normal-taken electric plaquettes, so static pure gauge solves the field equation and the Gauss charge div D is conserved by every tick, for any lapse, shift and shear',
      cg == 0 and mg < 1e-13 and dq < 1e-11 * np.abs(q0).max(), f'|curl grad| = {cg:.0e}; |M(0) grad| = {mg:.0e}; Gauss drift over 200 ticks {dq / np.abs(q0).max():.0e}')
# A3 cone = null cone of the edges, strong fields
dev = {1e-3: 0, 2e-3: 0}; split = {1e-3: 0, 2e-3: 0}
for _ in range(4):
    H = rng.normal(size=(3, 3)) * 0.15; gl = np.eye(3) + (H + H.T) / 2; be = TAU0 * rng.normal(size=3) * 0.1; Nl = TAU0 * (1 + 0.2 * rng.normal())
    for n in DIRS[[3, 9, 10]] @ np.linalg.qr(rng.normal(size=(3, 3)))[0]:
        for k in dev:
            w = freqs(k * n, Nl, be, gl); t = wcone(k * n, Nl, be, gl); dev[k] = max(dev[k], np.abs(w / t - 1).max()); split[k] = max(split[k], abs(w[1] - w[0]) / t)
check('A3 theorem (continuum limit = covariant Maxwell): for strong lapse, shift (0.1 c) and shear (0.15) both polarisations obey (w + beta.K)^2 = N^2 gamma^ij K_i K_j up to the lattice O(K^2); no birefringence at leading order',
      dev[1e-3] < 1e-6 and 3.5 < dev[2e-3] / dev[1e-3] < 4.5 and split[1e-3] < 1e-7,
      f'max rel. deviation {dev[1e-3]:.1e} at |K| 1e-3, x{dev[2e-3] / dev[1e-3]:.2f} at 2e-3; polarisation split {split[1e-3]:.0e}')
# A4 diagonal cells: photon band = CL-1 fermion band at every K
mx = 0
for f in (np.array([1.0, 0.9, 1.15]), np.array([0.8, 1.1, 1.0])):
    for N_ in (1.0, 1.07):
        eps = np.arcsin(r3 * TAU0 * N_ * np.sqrt(np.mean(f ** 2))); gl = np.diag(1 / f ** 2)
        for K in rng.uniform(-np.pi, np.pi, (40, 3)):
            wf0 = np.sort(np.abs(np.angle(np.linalg.eigvals(fineU(K, f, eps, 0.0, 0.0)))))[-1]
            mx = max(mx, np.abs(freqs(K, TAU0 * N_, np.zeros(3), gl, wt=wf0, span=1e-6) - wf0).max())
c6 = {}
for nm, n in (('axis', np.array([1.0, 0, 0])), ('generic', np.array([0.267, 0.535, 0.802])), ('body', np.ones(3) / r3)):
    out = []
    for k in (0.02, 0.04):
        K = k * n; wl = lightpos(fineU(K, np.ones(3), E0, 0.0, 0.5), PL3).mean(); out.append((wl / freqs(K, TAU0, np.zeros(3), np.eye(3)).mean() - 1) / k ** 2)
    c6[nm] = out
check('A4 theorem: in a diagonal cell (lapse N, gamma^ii = f_i^2) the link band (2 sin w/2)^2 = N^2 tau^2 sum f_i^2 (2 sin K_i/2)^2 is the CL-1 band sin^2(w/2) = sin^2(eps) sum f_i^2 sin^2(K_i/2)/sum f_i^2 at EVERY K, since sin eps = sqrt3 N tau rms f. The copy mass moves the light fermion band by a dimension-six term dv/c = c6 K^2',
      mx < 1e-12 and all(abs(v[1] / v[0] - 1) < 0.01 for k_, v in c6.items() if k_ != 'body') and abs(c6['body'][0]) < 1e-9,
      f'160 K, no copy mass: {mx:.0e}; copy mass M .5, eps .3: c6 axis {c6["axis"][0]:+.4f}, generic {c6["generic"][0]:+.4f}, body {c6["body"][0]:+.0e}')

print('== B. the centre-bond (Yee) placement and the shear')
gT = np.array([[1.0, -.15, .1], [-.15, .92, -.08], [.1, -.08, 1.07]])           # strong target spatial metric
refl = 0
for K in rng.uniform(-np.pi, np.pi, (30, 3)):
    for ax in range(3):
        Kr = K.copy(); Kr[ax] *= -1; refl = max(refl, np.abs(freqs(K, TAU0, np.zeros(3), gT, True) - freqs(Kr, TAU0, np.zeros(3), gT, True)).max())
_, G1 = photon_fit(TAU0, np.zeros(3), gT, onetoone=True); _, Gs = photon_fit(TAU0, np.zeros(3), gT)
tg = TAU0 ** 2 * np.linalg.inv(gT); off = lambda M_: np.abs(M_[np.triu_indices(3, 1)]).max() / TAU0 ** 2
check('B1 theorem: pairing each link only with its own dual face (the one-to-one Yee Hodge) makes every weight diagonal, so the band is even in each K_i separately and the cone has no K_i K_j term: the plain placement cannot read shear',
      refl < 1e-13 and off(G1) < 1e-5 and off(tg) > 0.05, f'max |w(K) - w(reflected K)| {refl:.0e}; cone off-diagonal one-to-one {off(G1):.0e}, target {off(tg):.3f}')
Kg = np.array(list(itertools.product(np.linspace(-np.pi, np.pi, 9), repeat=3))) + 1e-3
pdm = min(min(np.linalg.eigvalsh(parts(K, TAU0, TAU0 * np.array([0, -.15, .1]), gT)[0]).min(), np.linalg.eigvalsh(parts(K, TAU0, TAU0 * np.array([0, -.15, .1]), gT)[4]).min()) for K in Kg[::7])
def physz(K):
    z = companion(K, TAU0, TAU0 * np.array([0, -.15, .1]), gT); return z[np.argsort(np.abs(z - 1))[2:]]      # drop the static gauge/Gauss pair
zabs = max(np.abs(np.abs(physz(K)) - 1).max() for K in Kg[::7])
same = max(np.abs(parts(K, TAU0, np.zeros(3), np.diag([1.0, 0.9, 1.2]))[0] - parts(K, TAU0, np.zeros(3), np.diag([1.0, 0.9, 1.2]), True)[0]).max() for K in Kg[::50])
check('B2 minimal change: let each site pair the three links that meet at its even centre (shear couples links sharing a centre, range one cell). Same carriers, same gauge group, weights positive for any positive gamma, equal to Yee when gamma is diagonal, stable: every tick eigenvalue on |z| = 1',
      np.abs(Gs - tg).max() / TAU0 ** 2 < 1e-6 and pdm > 0 and zabs < 1e-12 and same < 1e-15,
      f'site cone - target {np.abs(Gs - tg).max() / TAU0 ** 2:.0e}; min weight eigenvalue {pdm:.3f}; max ||z| - 1| of the 4 radiating roots {zabs:.0e} (shear .15, shift .15 c, 105 K); diagonal = Yee {same:.0e}')
bS = TAU0 * np.array([0.0, -0.15, 0.1]); dr = []
for k in (1e-3, 2e-3):
    for e in np.eye(3)[1:]:
        for j in range(2): dr.append(-(freqs(k * e, TAU0, bS, np.eye(3))[j] - freqs(-k * e, TAU0, bS, np.eye(3))[j]) / (2 * k) / (bS @ e) - 1)
check('B3 the shift drags both photon polarisations by exactly b at every order in b (0.15 c tested); the error is the lattice O(K^2)', max(np.abs(dr)) < 1e-6,
      f'drift/b - 1 up to {max(np.abs(dr)):.0e}')

print('== C. photon packets in metric gradients (z line, 2048 cells; Bloch along x, y; energy centroid)')
NZ, ZC, GS, X0 = 2048, 1024.0, 2e-5, 900
pol0 = rng.normal(size=3) + 1j * rng.normal(size=3)
def saw(x):
    x = (x + NZ / 2) % NZ - NZ / 2; return np.where(np.abs(x) <= X0, x, np.sign(x) * X0 - (x - np.sign(x) * X0) * 2 * X0 / (NZ - 2 * X0))
def packet(Kb, sg, dwdl, oto=False):
    Kx, Ky = Kb; A0 = np.zeros(3 * NZ, complex); A1 = A0.copy(); m = np.arange(NZ)
    for j in range(NZ):
        Kz = (2 * np.pi * j / NZ + np.pi) % (2 * np.pi) - np.pi; gw = np.exp(-(Kz * sg) ** 2 / 2)
        if gw < 1e-13: continue
        K = np.array([Kx, Ky, Kz]); w = freqs(K, TAU0, np.zeros(3), np.eye(3), span=0.3)[0]
        ev, V = np.linalg.eigh(Mst(w, parts(K, TAU0, np.zeros(3), np.eye(3)))); Vn = V[:, np.argsort(np.abs(ev))[:2]]
        a = Vn @ (Vn.conj().T @ pol0); a /= np.linalg.norm(a)
        ph = (np.exp(1j * Kz * (m - ZC))[:, None] * np.array([1, 1, np.exp(1j * Kz / 2)])[None, :] * a[None, :]).reshape(-1)
        A0 += gw * ph; A1 += gw * np.exp(-1j * w) * ph
    lam = GS * np.stack([saw(m - ZC), saw(m - ZC), saw(m + 0.5 - ZC)], 1).reshape(-1)
    return A0, A1 * np.exp(-1j * dwdl * lam)                # start at the local frequency (no negative-frequency admixture)
def predict(F, Kb, oto=False, d=1e-4):
    K = np.array([Kb[0], Kb[1], 0.0]); dwdl = (freqs(K, *F(d), oto).mean() - freqs(K, *F(-d), oto).mean()) / (2 * d); h = 1e-3
    wz = lambda q: freqs(K + [0, 0, q], TAU0, np.zeros(3), np.eye(3)).mean()
    return -(wz(h) - 2 * wz(0) + wz(-h)) / h ** 2 * dwdl * GS, dwdl
def packet_accel(F, Kb, oto=False, T=400):
    pred, dwdl = predict(F, Kb, oto); ln_ = Line(NZ, Kb, lambda z: F(GS * float(saw(z - ZC))), oto); aa = []
    for sg in (100.0, 200.0):
        Am, A = ln_.gauss_fix(*packet(Kb, sg, dwdl, oto)); xs = [ln_.pos(Am, A)]
        for _ in range(T): Am, A = ln_.step(Am, A); xs.append(ln_.pos(Am, A))
        aa.append(2 * np.polyfit(np.arange(T + 1), np.array(xs) - xs[0], 2)[0])
    return (4 * aa[1] - aa[0]) / 3, pred
flat3 = np.eye(3); Exy = np.array([[0, 1.0, 0], [1, 0, 0], [0, 0, 0]])
cases = [('lapse', lambda l: (TAU0 * (1 + l), np.zeros(3), flat3), (0.12, -0.09), False),
         ('gamma_ii', lambda l: (TAU0, np.zeros(3), flat3 + l * np.diag([1.0, -0.5, 0.3])), (0.12, -0.09), False),
         ('shear xy, K ~ (1,1)', lambda l: (TAU0, np.zeros(3), flat3 + l * Exy), (0.106, 0.106), False),
         ('shear xy, K ~ (1,-1)', lambda l: (TAU0, np.zeros(3), flat3 + l * Exy), (0.106, -0.106), False),
         ('curl shift b_x(z)', lambda l: (TAU0, TAU0 * l * np.array([1.0, 0, 0]), flat3), (0.15, 0.0), False)]
def hrad_grad(x0, d=1e-6):
    def h(x): r = np.linalg.norm(x); n = x / r; return 2 / r, 2 * np.outer(n, n) / r
    hp, hm = h(x0 + [0, 0, d]), h(x0 - [0, 0, d]); return (hp[0] - hm[0]) / (2 * d), (hp[1] - hm[1]) / (2 * d)
for nm, x0, Kb in (('radial gauge, axis ray at s = b', np.array([1.0, 0, 1.0]), (0.15, 0.0)), ('radial gauge, face ray at s = b', np.array([0.7071, 0.7071, 1.0]), (0.106, 0.106))):
    d00, dij = hrad_grad(x0); cases.append((nm, (lambda d00, dij: lambda l: rd_photon(l * d00, l * dij, np.zeros(3)))(d00, dij), Kb, False))
res = {}
for nm, F, Kb, oto in cases: res[nm] = packet_accel(F, Kb, oto)
zero_sh = packet_accel(cases[2][1], cases[2][2], True)[0]; zero_cf = packet_accel(lambda l: (TAU0, TAU0 * l * np.array([0, 0, 1.0]), flat3), (0.15, 0.0))[0]
rat = {k: v[0] / v[1] for k, v in res.items()}
check('C1 lattice photon packets follow the eikonal of the lattice dispersion (transverse push = -w_KzKz dw/dz) for lapse, gamma_ii, shear, shift and the radial-gauge gradient on rays',
      all(abs(r - 1) < 5e-3 for r in rat.values()), '; '.join(f'{k} {v:.4f}' for k, v in rat.items()))
sc = abs(res['shear xy, K ~ (1,1)'][0]); scs = abs(res['curl shift b_x(z)'][0])
check('C2 shear pushes the (1,1) and (1,-1) packets oppositely; the one-to-one placement does not push (second order only); a curl-free shift b_z(z) pushes nothing (gravitomagnetism is the curl)',
      res['shear xy, K ~ (1,1)'][0] * res['shear xy, K ~ (1,-1)'][0] < 0 and abs(zero_sh) < 1e-3 * sc and abs(zero_cf) < 1e-2 * scs,
      f'one-to-one/site {zero_sh / sc:.0e}; curl-free/curl {zero_cf / scs:+.0e}')
print(f'   elapsed {time.time() - T0:.0f} s')

print('== D. weak static fields under the fixed-4-volume clause (lattice-measured local photon dispersion along rays)')
GMs = 1e-6
def h_rad(x, gm):
    r = np.linalg.norm(x); n = x / r; return 2 * gm / r, 2 * gm * np.outer(n, n) / r, np.zeros(3)
def eta2(x):
    r = np.linalg.norm(x); X, Y, Z = x; return np.array([X / r - X * Y * Y / r ** 3, -Y / r + X * X * Y / r ** 3, 0.0])
def h_two(x, gm, c=0.7, d=1e-6):
    h00, hij, h0 = h_rad(x, gm); r = np.linalg.norm(x); Jx = np.zeros((3, 3))
    for i in range(3):
        e = np.zeros(3); e[i] = d * r; Jx[i] = (eta2(x + e) - eta2(x - e)) / (2 * d * r)
    return h00, hij + c * gm * (Jx + Jx.T), h0
def h_iso(x, gm): r = np.linalg.norm(x); return 2 * gm / r, 2 * gm / r * np.eye(3), np.zeros(3)
JV = {'eq': np.array([0, 0, 1.0]), 'gen': np.array([0.3, -0.5, 0.8]) / np.linalg.norm([0.3, -0.5, 0.8])}
def h_lt(J): return lambda x, gm: (0.0, np.zeros((3, 3)), -2 * gm * np.cross(J, x) / np.linalg.norm(x) ** 3)
REF = {}
def deficit(hf, x, k, box, group, ks=1e-3):
    h0 = hf(x, GMs); amp = GMs * 1e-5 / max(abs(h0[0]), np.abs(h0[1]).max(), np.abs(h0[2]).max())
    out = []
    for sgn in (1, -1):                  # symmetric in the field amplitude: removes the second-order response
        rd = rd_photon(*hf(x, sgn * amp), box=box); w = lambda K: freqs(K, *rd).mean()
        key = (tuple(k), group)
        if key not in REF:
            wr = lambda K: freqs(K, TAU0, np.zeros(3), np.eye(3)).mean()
            REF[key] = (wr(ks * k * 1.01) - wr(ks * k * 0.99)) / 0.02 if group else wr(ks * k)
        val = (w(ks * k * 1.01) - w(ks * k * 0.99)) / 0.02 if group else w(ks * k)
        out.append(sgn * (1 - val / REF[key]))
    return (out[0] + out[1]) / 2 * GMs / amp
ug, wg = np.polynomial.legendre.leggauss(24)
def delay(hf, k, e, b, box=False, group=False, L=1e4, off=None):
    U = np.arcsinh(L / b); tot = 0; off = np.zeros(3) if off is None else off
    for lo, hi in ((-U, -3), (-3, 3), (3, U)):
        for uu, ww in zip((hi - lo) / 2 * ug + (hi + lo) / 2, (hi - lo) / 2 * wg):
            tot += ww * deficit(hf, b * e + off + b * np.sinh(uu) * k, k, box, group) * b * np.cosh(uu)
    return tot
def bend(hf, k, e, box=False): return -(delay(hf, k, e, 2.0, box) - delay(hf, k, e, 1.0, box)) / np.log(2) / 2 / GMs
rays = {'axis': [1, 0, 0], 'face': [1, 1, 0], 'face xz': [1, 0, 1], 'body': [1, 1, 1], 'generic': [0.8, 0.5, 0.33]}
RK = {}
for nm, kk in rays.items():
    k = np.array(kk, float); k /= np.linalg.norm(k); t = np.array([0, 0, 1.0]) if abs(k[2]) < 0.9 else np.array([1.0, 0, 0])
    e = t - (t @ k) * k; RK[nm] = (k, e / np.linalg.norm(e))
tab = {nm: (bend(h_rad, k, e), bend(h_rad, k, e, True), 1 + np.sum(k ** 4)) for nm, (k, e) in RK.items()}
two = [bend(h_two, *RK[nm]) for nm in ('face xz', 'body', 'generic')]; iso = [bend(h_iso, *RK[nm]) for nm in ('body', 'generic')]
kg, eg = RK['generic']; e2 = np.cross(kg, eg)
outp = [-(delay(h_rad, kg, eg, 1.0, bx_, off=1e-3 * e2) - delay(h_rad, kg, eg, 1.0, bx_, off=-1e-3 * e2)) / 2e-3 / GMs for bx_ in (False, True)]
full = [v[0] for v in tab.values()] + two + iso
check('D1 photon bending 1 + gamma = 2 on every ray, in the radial and the second trace-fixed gauge (and the isotropic one: the site reading is covariant); no out-of-plane bending. One-to-one placement: 1 + sum k^4 (4/3 on the body diagonal)',
      max(abs(np.array(full) - 2)) < 2e-6 and all(abs(v[1] - v[2]) < 5e-5 for v in tab.values()) and abs(outp[0]) < 1e-4 and abs(outp[1] - 0.2318) < 2e-3,
      ' '.join(f'{nm} {v[0]:.6f}/{v[1]:.4f}' for nm, v in tab.items()) + f' (site/one-to-one); 2nd gauge, iso: max |dev| {max(abs(np.array(two + iso) - 2)):.0e}; generic out-of-plane {outp[0]:+.0e}/{outp[1]:+.4f} GM/b')
shp = {nm: (delay(h_rad, *RK[nm], 1.0, group=True) - delay(h_rad, *RK[nm], 10.0, group=True)) / np.log(10) / 4 / GMs for nm in ('axis', 'body', 'generic')}
check('D2 Shapiro delay (packet group delay along the ray): coefficient of -4 GM ln b is (1 + gamma)/2 = 1 on every ray',
      all(abs(v - 1) < 2e-6 for v in shp.values()), ' '.join(f'{k} {v:.6f}' for k, v in shp.items()))
lt = {}
for nm, J in (('axis', np.cross(*RK['axis'][::-1])), ('generic', JV['gen']), ('body', JV['gen'])):
    k, e = RK[nm]; ex = -4 * GMs * J @ np.cross(e, k)
    lt[nm] = [delay(h_lt(J), k, e, b) * b / ex for b in (1.0, 2.0)]
check('D3 photon frame dragging: the Lense-Thirring shift g_0i = -2G (J x r)_i / r^3 delays the photon by -4 G J.(e x k)/b, the GR value (8GJ/b between prograde and retrograde), as for every species (B3: drag coefficient 1)',
      all(abs(v - 1) < 2e-6 for vs in lt.values() for v in vs), ' '.join(f'{k} {v[0]:.6f}' for k, v in lt.items()) + f' (b = 1); at b = 2: max dev {max(abs(v[1] - 1) for v in lt.values()):.0e}')
print(f'   elapsed {time.time() - T0:.0f} s')
# D4 photon and fermion cones in the same cell
Gt = TAU0 ** 2 * gT; bP, GP_ = photon_fit(TAU0, np.zeros(3), np.linalg.inv(gT))
_, Gref, _ = fermion_fit(np.ones(3), E0, np.zeros(3), np.zeros((3, 3))); cor = Gref - TAU0 ** 2 * np.eye(3)
fc = np.sqrt(np.diag(gT)); sc_ = gT / np.outer(fc, fc); np.fill_diagonal(sc_, 0); cal = []
for it in range(6):
    ec = np.arcsin(r3 * TAU0 * np.sqrt(np.mean(fc ** 2))); _, G, _ = fermion_fit(fc, ec, np.zeros(3), sc_); E = (G - cor) - Gt; cal.append(np.abs(E).max() / TAU0 ** 2)
    fc = fc * np.sqrt(np.diag(Gt) / np.diag(G - cor)); offE = E / np.outer(np.sqrt(np.diag(Gt)), np.sqrt(np.diag(Gt))); np.fill_diagonal(offE, 0); sc_ = sc_ - offE
pf = np.abs((G - cor) - GP_).max() / TAU0 ** 2
bF, _, _ = fermion_fit(np.ones(3), E0, bS, np.zeros((3, 3))); bPh, _ = photon_fit(TAU0, bS, np.eye(3))
check('D4 photon = fermion cone in every direction, at every order in the field: shear .15 (fermion hop weights and shear parts fixed by CL-1\'s null-cone clause; the site-read link needs no calibration) and shift .15 c (both drift by b)',
      pf < 2e-5 and cal[0] > 1e-3 and np.abs(bF - bS)[1:].max() / np.abs(bS).max() < 1e-5 and np.abs(bPh - bS).max() / np.abs(bS).max() < 1e-5,
      f'|G_fermion - G_link|/tau^2 {pf:.0e} (fermion before calibration {cal[0]:.0e}); drift - b: fermion {np.abs(bF - bS).max() / np.abs(bS).max():.0e}, link {np.abs(bPh - bS).max() / np.abs(bS).max():.0e}')
# O(K^2) mismatch per unit shear (dimension-six), weak cell; the K -> 0 part (fermion O(sigma^2) before calibration) removed
sw = 1e-4; Sm = np.array([[0, sw, 0], [sw, 0, -sw], [0, -sw, 0]]); gu = np.eye(3) + Sm
_, _, wf_s = fermion_fit(np.ones(3), E0, np.zeros(3), Sm); _, _, wf_0 = fermion_fit(np.ones(3), E0, np.zeros(3), 0 * Sm)
dmm = lambda kk, n: (freqs(kk * n, TAU0, np.zeros(3), np.linalg.inv(gu)).mean() / wf_s(kk * n) - 1) - (freqs(kk * n, TAU0, np.zeros(3), np.eye(3)).mean() / wf_0(kk * n) - 1)
mm = [max(abs(dmm(kk, n) - dmm(0.01, n)) for n in DIRS) / (sw * (kk ** 2 - 1e-4)) for kk in (0.05, 0.1)]
C6H = max(mm)
print(f'   O(K^2) link-fermion mismatch from shear: |dv/c| <= {C6H:.2f} sigma K^2 (|K| .05, .1: {mm[0]:.2f}, {mm[1]:.2f}); flat: copy-mass c6 (A4)')
print(f'   elapsed {time.time() - T0:.0f} s')

print('== E. ESTIMATES against measurement (not theorems)')
aL = 2 * np.sqrt(8 * np.pi); EP = 1.22089e28; Kof = lambda E: E / EP * aL              # wavenumber per cube at energy E (eV)
c6ax = abs(c6['axis'][0]); Ugal = 1e-6
for lab, E, bound in (('LHAASO 1.4 PeV photon decay', 1.4e15, 3e-19), ('LEP 104.5 GeV electrons', 104.5e9, 1e-11)):
    print(f'   {lab}: link - fermion speed: copy mass c6 K^2 = {c6ax * Kof(E) ** 2:.0e}, shear {C6H:.2f} sigma K^2 (sigma ~ 1e-6) = {C6H * Ugal * Kof(E) ** 2:.0e} vs {bound:.0e}')
print(f'   VLBI (gamma - 1 = 1e-4) and Cassini (2.3e-5): tree-level 1 + gamma = 2 exactly at leading order; lattice part ~ K^2 = {Kof(3.5e-5) ** 2:.0e} at 8.4 GHz')
kSM, Ainv = 8 / (6 * np.pi ** 2), 137.036 / (4 * np.pi)
print(f'   SPECULATION (not computed): the sea\'s link term is cut off at the proper cell; a cell anisotropic at order U (no static gauge is diagonal')
print(f'   and trace-fixed) would give the dressed cone an anisotropy (b/A) c U = {kSM / Ainv:.1e} c U, i.e. gamma - 1 ~ {kSM / Ainv:.0e} c vs Cassini 2.3e-5,')
print('   unless the dressed cone is held to the edges\' null cone in every cell (proposed CL-3 clause); the shape coefficient c is open')
print('supplied: the covariant Maxwell form of the plaquette phase (proper area extended to shift and shear), the site pairing, the normal-taken')
print('  electric plaquette with mid-tick B, temporal gauge, CL-1 fermion code, fields, gauges, packets, rescaled local response, measured numbers.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
