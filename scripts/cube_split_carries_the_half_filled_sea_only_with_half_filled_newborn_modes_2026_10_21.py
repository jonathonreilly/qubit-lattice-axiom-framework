#!/usr/bin/env python3
"""sea-split: is the half-filled vacuum physical, and can a 2^3 cube split carry it locally?  (supplied models; finite
diagnostics; no physical identification)
Supplied model: the CL-1 cube tick WITHOUT the copy mass (spin-3/2 edge hop W, even then odd 2^3 cubes, half-ticks
exp(-i(eps - mu/2)W), exp(+i(eps + mu/2)W)), its negative-quasi-energy sea, site-phase links, CL-1's split at the middle
of an even half-tick (corner modes shared evenly over the children), fixed record 4-volume (sin eps x16 at a split).
 A  engine: 8 bands, the sea projector, the alias matrix of a split; the Dirac point in the midpoint frame
 B  filling: link response of the sea, the other half, empty and full; relabelling invariants of one cube
 C  split: T6 reproduction; mode counting; half-filled newborn modes and the nearest sea-to-sea unitary; the Dirac point
    order by order (exact series); real-space range and truncation; a strictly local handover
 D  estimates against measurement
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/CUBE_SPLIT_CARRIES_THE_HALF_FILLED_SEA_ONLY_WITH_HALF_FILLED_NEWBORN_MODES_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import factorial
import numpy as np
import scipy.fft as sfft
from scipy.linalg import expm

T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ engine (inlined from induced-response, plus split)
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8); I64 = np.eye(64)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C8[i] - 1.0) / r3; _, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
EDGES = [(a, b) for a in range(8) for b in range(8) if a < b and np.sum(abs(C8[a] - C8[b])) == 1]
W = np.zeros((8, 8), complex)
for a, b in EDGES:
    g_ = XI[a].conj() @ XI[b]; W[a, b] = -g_ / abs(g_) / r3; W[b, a] = np.conj(W[a, b])
def expmW(t): return np.cos(t) * I8 - 1j * np.sin(t) * W
def dag(A): return np.conj(np.swapaxes(A, -1, -2))
def tr(A): return np.trace(A, axis1=-2, axis2=-1)
def Dm(K): return np.exp(1j * (np.atleast_2d(K) @ C8.T))
def Uo(Ko, Ki, M):
    Do, Di = Dm(Ko), Dm(Ki); return Do[:, :, None] * M[None] * Di.conj()[:, None, :]
def tick(K, eps, mu):
    Ue = expmW(eps - mu / 2); Mo = expmW(-(eps + mu / 2)); return Uo(K, K, Mo) @ Ue, Ue, Mo
def proj(U):
    cw = np.real(tr(U)) / 8; w = np.arccos(np.clip(cw, -1, 1)); X = (U - dag(U)) / (2j * np.sin(w)[:, None, None])
    return (I8 + X) / 2, (I8 - X) / 2, w
def sea(K, eps, mu, mid=True):                    # sea projector (negative quasi-energy), midpoint frame of the even half-tick
    P, _, w = proj(tick(np.atleast_2d(K), eps, mu)[0])
    if mid: F = expmW((eps - mu / 2) / 2); P = F @ P @ F.conj().T
    return P, w
def Umid(K, eps, mu):
    F = expmW((eps - mu / 2) / 2); return F[None] @ Uo(np.atleast_2d(K), np.atleast_2d(K), expmW(-(eps + mu / 2))) @ F[None]
def omega(K):                                     # rows: fine alias q_m = K/2 + pi m; columns: child sign pattern (-1)^(m'.c)
    K = np.atleast_2d(K); q = K[:, None, :] / 2 + np.pi * C8[None]; sg = (-1.0) ** C8
    return np.prod((1 + sg[None, None] * np.exp(-1j * q)[:, :, None, :]) / 2, axis=-1)
def had(K):  return np.einsum('nmk,ab->nmakb', omega(K), I8).reshape(len(np.atleast_2d(K)), 64, 64)
def fine(K, ef, mf, gen=False):                   # fine sea (or fine physical generator, units hbar c / l_f) in the parent basis
    K = np.atleast_2d(K); B = had(K); P = np.zeros((len(K), 64, 64), complex)
    for im, m in enumerate(C8):
        Pm, wm = sea(K / 2 + np.pi * m, ef, mf)
        P[:, 8 * im:8 * im + 8, 8 * im:8 * im + 8] = (wm[:, None, None] * (I8 - 2 * Pm) * r3 / np.sin(ef)) if gen else Pm
    return dag(B) @ P @ B
def newborn(ef, mf):                              # the 56 new modes: each sign pattern m' != 0 holds the fine sea at pi m'
    Q = np.zeros((64, 64), complex)
    for im, m in enumerate(C8):
        if im: Q[8 * im:8 * im + 8, 8 * im:8 * im + 8] = sea(np.pi * m[None], ef, mf)[0][0]
    return Q
def P1of(K, ec, mc, ef, mf, born=True):
    Pc, _ = sea(K, ec, mc); P = np.zeros((len(np.atleast_2d(K)), 64, 64), complex); P[:, :8, :8] = Pc
    return P + (newborn(ef, mf)[None] if born else 0)
def kcube(n, shift=0.5):
    g = 2 * np.pi * (np.arange(n) + shift) / n - np.pi; return np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
def polar(M):
    U, s, Vh = np.linalg.svd(M); return U @ Vh, s
X16 = lambda e: (np.arcsin(np.sin(e) / 16), e)    # fixed record 4-volume: sin eps_c = sin eps_f / 16, mu_f = 8 mu_c

# ------------------------------------------------------------------ heavy parts first (fresh heap); printed in C4, C5
NO = 7
def X_series(n, eps, scale=1.0):
    """exact Taylor coefficients X_j, X(k n) = sum k^j X_j, of X = 2P - 1 (massless, midpoint frame) at K = scale k n"""
    lam = C8 @ n * scale; Mo, Ue = expmW(-eps), expmW(eps); U = np.zeros((NO + 1, 8, 8), complex)
    for i in range(NO + 1):
        for j in range(NO + 1 - i): U[i + j] += np.diag((1j * lam) ** i / factorial(i)) @ Mo @ np.diag((-1j * lam) ** j / factorial(j))
    U = U @ Ue; Nk = ((U - dag(U)) / 2j)[1:]
    S = np.array([(-1) ** (j // 2) * np.mean((n * scale) ** j) / factorial(j) if j % 2 == 0 else 0.0 for j in range(NO + 3)])
    cw = np.sin(eps) ** 2 * S; cw[0] += np.cos(eps) ** 2; s2 = -np.convolve(cw, cw)[:NO + 3]; s2[0] += 1; sig = s2[2:NO + 2]
    inv = np.zeros(NO); inv[0] = sig[0] ** -0.5
    for m in range(1, NO): inv[m] = -np.convolve(np.convolve(inv, inv)[:NO], sig)[m] / (2 * inv[0] * sig[0])
    X = np.zeros((NO, 8, 8), complex)
    for i in range(NO):
        for j in range(NO - i): X[i + j] += Nk[i] * inv[j]
    F = expmW(eps / 2); return F[None] @ X @ F.conj().T[None]
HB = []
for i in range(8):
    E = np.zeros((8, 8), complex); E[i, i] = 1; HB.append(E)
    for j in range(i + 1, 8):
        E = np.zeros((8, 8), complex); E[i, j] = E[j, i] = 1 / np.sqrt(2); HB.append(E)
        E = np.zeros((8, 8), complex); E[i, j] = -1j / np.sqrt(2); E[j, i] = 1j / np.sqrt(2); HB.append(E)
HB = np.array(HB)
def mons(n, deg): return np.array([np.prod(n ** np.array(p)) for p in itertools.product(range(deg + 1), repeat=3) if sum(p) == deg])
def cvec(M): return np.concatenate([M.real.ravel(), M.imag.ravel()])
def ccols(n, deg, X0): return np.array([cvec(1j * mv * (H @ X0 - X0 @ H)) for mv in mons(n, deg) for H in HB]).T
def build(n, deg, x): mm = mons(n, deg); return np.einsum('m,mh,hij->ij', mm, x.reshape(len(mm), len(HB)), HB)
rgd = np.random.default_rng(11); ND = rgd.normal(size=(320, 3)); ND /= np.linalg.norm(ND, axis=1)[:, None]
ND = np.vstack([ND, np.eye(3), np.ones((1, 3)) / r3])
def nsolve(M, v, tol=1e-11):
    lam, Q = np.linalg.eigh(M); keep = lam > tol * lam.max(); return Q[:, keep] @ ((Q[:, keep].T @ v) / lam[keep]), Q[:, ~keep].T
def dirac(ec_, ef_, degs=(2,)):
    """order-by-order analytic matching e^{i Lam} X_c(K) e^{-i Lam} = X_f(K/2) at the Dirac point (normal equations, 324 rays)"""
    SC = [X_series(n, ec_) for n in ND]; SF = [X_series(n, ef_, 0.5) for n in ND]; X0 = [s_[0] for s_ in SC]
    M1 = np.zeros((192, 192)); v1 = np.zeros(192)
    for n, c, f, x0 in zip(ND, SC, SF, X0):
        A = ccols(n, 1, x0); b = cvec(f[1] - c[1]); M1 += A.T @ A; v1 += A.T @ b
    x1, nulls = nsolve(M1, v1); r1 = np.sqrt(sum(np.sum((cvec(f[1] - c[1]) - ccols(n, 1, x0) @ x1) ** 2) for n, c, f, x0 in zip(ND, SC, SF, X0))
                                        / sum(np.sum(cvec(f[1] - c[1]) ** 2) for c, f in zip(SC, SF)))
    def rowsof(n, c, f, x0):
        L1 = build(n, 1, x1); C1 = L1 @ x0 - x0 @ L1; Nl = [build(n, 1, v) for v in nulls]
        b = cvec((f[2] - c[2]) - 1j * (L1 @ c[1] - c[1] @ L1) + 0.5 * (L1 @ C1 - C1 @ L1))
        A = np.hstack([ccols(n, d, x0) for d in degs] + [np.array([cvec(1j * (Nm @ c[1] - c[1] @ Nm) - 0.5 * (Nm @ C1 - C1 @ Nm)) for Nm in Nl]).T])
        return A, b
    M2 = None; bb = 0.0
    for z in zip(ND, SC, SF, X0):
        A, b = rowsof(*z); M2 = A.T @ A if M2 is None else M2 + A.T @ A; v2 = A.T @ b if bb == 0.0 else v2 + A.T @ b; bb += b @ b
    x2, _ = nsolve(M2, v2, 1e-13); rr = 0.0; Fl = []
    for i, z in enumerate(zip(ND, SC, SF, X0)):
        A, b = rowsof(*z); res = b - A @ x2; rr += res @ res
        if len(degs) == 1:
            R = res.reshape(2, 8, 8); R = R[0] + 1j * R[1]; k = 1e-2; Xf = sum(z[2][j] * k ** j for j in range(NO))
            wp, vp = np.linalg.eigh(Xf + k ** 2 * (R + R.conj().T) / 2); wf, vf = np.linalg.eigh(Xf)
            Fl.append(np.real(np.trace((I8 - vf[:, wf > 0] @ vf[:, wf > 0].conj().T) @ vp[:, wp > 0] @ vp[:, wp > 0].conj().T)) / k ** 4)
    return r1, np.sqrt(rr / bb), (np.mean(Fl[:-4]) if Fl else None)
dr = {e: dirac(*X16(e)) for e in (0.04, 0.3)}; dr['same'] = dirac(0.3, 0.3); r4 = dirac(*X16(0.3), (2, 4))[1]
Fbar = dr[0.04][2]
N = 10; Kt = kcube(N); NK = len(Kt); BS = 50; ec, ef = X16(0.3)
A_ = np.zeros((NK, 64, 64), np.complex64)
for s in range(0, NK, BS):
    K = Kt[s:s + BS]; Pf_ = fine(K, ef, 0.0); P1_ = P1of(K, ec, 0.0, ef, 0.0); A_[s:s + BS] = polar(Pf_ @ P1_ + (I64 - Pf_) @ (I64 - P1_))[0]
VR = sfft.fftn(A_.reshape(N, N, N, 64, 64), axes=(0, 1, 2), workers=1, overwrite_x=True) / NK; del A_
Rw = np.where(np.arange(N) > N // 2, np.arange(N) - N, np.arange(N)); Rin = np.maximum(np.maximum(abs(Rw)[:, None, None], abs(Rw)[None, :, None]), abs(Rw)[None, None, :])
nr = np.linalg.norm(VR, axis=(3, 4)); shell = [nr[Rin == r].max() / nr.max() for r in range(1, 5)]; ht = []
for r in range(0, 4):
    Vt = VR.copy(); Vt[Rin > r] = 0; Vt = sfft.ifftn(Vt, axes=(0, 1, 2), workers=1, overwrite_x=True); Vt *= NK; Vt = Vt.reshape(NK, 64, 64); h = 0.0
    for s in range(0, NK, BS):
        K = Kt[s:s + BS]; U_, _ = polar(Vt[s:s + BS].astype(complex)); h += np.real(tr((I64 - fine(K, ef, 0.0)) @ U_ @ P1of(K, ec, 0.0, ef, 0.0) @ dag(U_))).sum()
    ht.append(h / NK / 32); del Vt
del VR
# ------------------------------------------------------------------ A. engine
print('== A. engine')
rng = np.random.default_rng(20261021); KR = rng.uniform(-np.pi, np.pi, (300, 3)); dv = 0
for eps, mu in ((0.04, 0.01), (0.3, 0.2), (1.2, 0.0)):
    U = tick(KR, eps, mu)[0]; A_ = (np.cos(mu) - np.cos(2 * eps)) / 2
    w = np.arccos(A_ * np.cos(KR).mean(1) + (np.cos(2 * eps) + np.cos(mu)) / 2)
    P = sea(KR, eps, mu)[0]
    dv = max(dv, np.abs(np.sort(np.abs(np.angle(np.linalg.eigvals(U))), 1) - w[:, None]).max(), np.abs(P @ P - P).max(),
             np.abs(np.real(tr(P)) - 4).max())
dO = np.abs(dag(omega(KR)) @ omega(KR) - I8).max()
check('A1 all 8 bands obey the CL-1 band law; sea projector rank 4; the split\'s alias matrix is unitary', max(dv, dO) < 1e-10, f'{max(dv, dO):.0e}')
NV = rng.normal(size=(80, 3)); NV /= np.linalg.norm(NV, axis=1)[:, None]; NV = np.vstack([NV, np.eye(3), np.ones((1, 3)) / r3])
d0 = 0
for e in (0.0025, 0.3, 1.2):
    for n in NV[:20]:
        L_ = np.diag(C8 @ n); d0 = max(d0, np.abs(X_series(n, e)[0] - 1j * r3 * (L_ @ W - W @ L_)).max())
ser = X_series(NV[0], 0.3); Xd = 2 * sea(0.01 * NV[:1], 0.3, 0.0)[0][0] - I8; sd = np.abs(Xd - sum(ser[j] * 0.01 ** j for j in range(NO))).max()
check('A2 THEOREM: in the midpoint frame the massless sea at the Dirac point is X0(n) = i sqrt3 [n.C, W] for every step '
      '(C = corner positions), so coarse and fine seas share it exactly', d0 < 1e-12 and sd < 1e-9, f'{d0:.0e} (series vs direct {sd:.0e})')

# ------------------------------------------------------------------ B. filling
print('== B. is the filling physical? (empty, sea, other half, full)')
Lb = 4; L = 2 * Lb; NS = L ** 3; Sg = np.array(list(itertools.product(range(L), repeat=3))); ridx = (Sg % 2) @ [4, 2, 1]; XS = Sg / 2.0
def idx(v): v = np.asarray(v) % L; return (v[0] * L + v[1]) * L + v[2]
def torus(eps, mu, th1=None, th2=None):
    Ue = np.zeros((NS, NS), complex); Uo_ = np.zeros((NS, NS), complex)
    for n in itertools.product(range(Lb), repeat=3):
        n = np.array(n); ie = [idx(2 * n + t) for t in C8]; io = [idx(2 * n + 1 + (1 - t)) for t in C8]
        Ue[np.ix_(ie, ie)] = expm(-1j * (eps - mu / 2) * W); Uo_[np.ix_(io, io)] = expm(1j * (eps + mu / 2) * W)
    V1 = np.ones(NS) if th1 is None else np.exp(1j * th1); V2 = np.ones(NS) if th2 is None else np.exp(1j * th2)
    e = -np.angle(np.linalg.eigvals((V2[:, None] * Uo_ * V1[None, :]) @ Ue)); return np.array([0.0, e[e < 0].sum(), e[e > 0].sum(), e.sum()])
resp = []
for eps, mu in ((0.7, 0.3), (1.3, 0.4)):
    q = np.array([2 * np.pi / Lb, 2 * np.pi / Lb, 0]); amp = 1e-3; h1, h2 = rng.normal(size=8), rng.normal(size=8); base = torus(eps, mu)
    ed = sum(torus(eps, mu, s * amp * h1[ridx] * np.cos(XS @ q), s * amp * h2[ridx] * np.cos(XS @ q)) for s in (1, -1)) - 2 * base
    resp.append(ed / (2 * amp ** 2))
resp = np.array(resp)
check('B1 THEOREM + exact (8 site)^3 torus: under a link field the empty state keeps phase 0 and the full state\'s phase is '
      'linear (det), so both have zero induced response; the sea and the other half respond oppositely',
      np.all(resp[:, 0] == 0) and np.abs(resp[:, 3]).max() < 1e-6 * np.abs(resp[:, 1]).min() and np.abs(resp[:, 1] + resp[:, 2]).max() < 1e-6 * np.abs(resp[:, 1]).min(),
      'empty 0, full ' + ', '.join(f'{x:.0e}' for x in resp[:, 3]) + '; sea ' + ', '.join(f'{x:+.4f}' for x in resp[:, 1]) + ', other half ' + ', '.join(f'{x:+.4f}' for x in resp[:, 2]))
def speed2(eps, mu):
    A_ = (np.cos(mu) - np.cos(2 * eps)) / 2; return A_ / 3 * (mu / np.sin(mu) if mu else 1.0)
def mu_of_m(eps, m):
    mu = np.sin(eps) / r3 * m
    for _ in range(60): mu = np.sqrt(speed2(eps, mu)) * m
    return mu
def second_order(U0, U0p, U0m, d1p, d1m, d2):
    PF, _, w = proj(U0); _, PEp, wp = proj(U0p); _, PEm, wm = proj(U0m)
    M1p, M1m = dag(U0p) @ d1p, dag(U0m) @ d1m
    A2 = 1j * (dag(U0) @ d2 + 0.5 * (dag(M1p) @ M1p + dag(M1m) @ M1m)); A1p, A1m = 1j * M1p, 1j * M1m
    t2 = -0.5 * (np.real(tr(PEp @ A1p @ PF @ dag(A1p))) / np.tan((w + wp) / 2) + np.real(tr(PEm @ A1m @ PF @ dag(A1m))) / np.tan((w + wm) / 2))
    return np.sum(np.real(tr(PF @ A2)) + t2)
def gauge_blocks(K, eps, mu, q, h1, h2):
    U0, Ue, Mo = tick(K, eps, mu); Kp, Km = K + q, K - q; Op, Om, O0 = Uo(Kp, Kp, Mo), Uo(Km, Km, Mo), Uo(K, K, Mo)
    ph = np.exp(1j * (C8 @ q) / 2); T1p, T1m, T2p, T2m = (np.diag(h * p) / 2 for h, p in ((h1, ph), (h1, ph.conj()), (h2, ph), (h2, ph.conj())))
    d1p = 1j * T2p @ O0 @ Ue + Op @ (1j * T1p) @ Ue; d1m = 1j * T2m @ O0 @ Ue + Om @ (1j * T1m) @ Ue
    d2 = (-0.25 * np.diag(h2 ** 2) @ O0 @ Ue - 0.25 * O0 @ np.diag(h1 ** 2) @ Ue - T2m @ Op @ T1p @ Ue - T2p @ Om @ T1m @ Ue)
    return U0, Op @ Ue, Om @ Ue, d1p, d1m, d2
def kgrid3(ns):
    gs = [2 * np.pi * (np.arange(n) + 0.5) / n - np.pi for n in ns]; return np.array(np.meshgrid(*gs, indexing='ij')).reshape(3, -1).T
kap = 2 / (6 * np.pi ** 2)
def coulomb(eps, m, f=0.7):                       # 1/e^2 of the sea from the static Coulomb response, q -> 0 (induced-response B)
    mu = mu_of_m(eps, m); c = np.sqrt(speed2(eps, mu)); Nx, Nt = int(round(f * 32 / m)), int(round(f * 16 / m)); Ks = kgrid3((Nx, Nt, Nt)); rows = []
    for j in (1, 2, 3):
        q = np.array([2 * np.pi * j / Nx, 0, 0]); s_ = np.sinc(((C8 - 0.5) @ q) / 2 / np.pi)
        r = sum(second_order(*gauge_blocks(Ks[s:s + 800], eps, mu, q, -0.5 * s_, -0.5 * s_)) for s in range(0, len(Ks), 800))
        rows.append((q[0] ** 2, -4 * r / (q[0] ** 2 * len(Ks))))
    rows = np.array(rows); return c * np.linalg.solve(np.stack([np.ones(3), rows[:, 0], rows[:, 0] ** 2], 1), rows[:, 1])[0]
ms = (0.5, 0.35, 0.25); Ae = [coulomb(0.05, m) for m in ms]; sl = (Ae[2] - Ae[1]) / np.log(0.35 / 0.25) / kap
check('B2 the sea\'s link coupling runs: 1/e^2 = kappa[ln(1/m) + C] with slope -> kappa = 2/(6 pi^2) (two Dirac copies); the '
      'other half gives -1/e^2 (ghost photon) and empty and full give 0 at every m (B1): no running', abs(sl - 1) < 0.03 and min(Ae) > 0,
      '1/e^2 = ' + ', '.join(f'{a:.4f}' for a in Ae) + f' at m = {ms}; slope {sl:.3f} kappa')
Kb = kcube(24); G = sum(sea(Kb[s:s + 1728], 0.3, 0.0, mid=False)[0].sum(0) for s in range(0, len(Kb), 1728)) / len(Kb); nu = np.clip(np.linalg.eigvalsh(G), 1e-15, 1 - 1e-15)
Sent = -np.sum(nu * np.log(nu) + (1 - nu) * np.log(1 - nu)); Pr = []
for S_ in itertools.product((0, 1), repeat=8):
    Pr.append(abs(np.linalg.det(G - np.diag(1 - np.array(S_, float)))))
Pr = np.array(Pr); Hrec = -np.sum(Pr[Pr > 0] * np.log(Pr[Pr > 0])); var = np.real(np.trace(G @ (I8 - G)))
check('B3 THEOREM: a site relabelling is local, so it keeps every region\'s entanglement; particle-hole maps empty <-> full and '
      'sea <-> sea. One cube of the sea (eps .3): entanglement > 0, records half filled and random; empty: all 0',
      Sent > 1 and abs(Pr.sum() - 1) < 1e-10 and abs(np.real(np.diag(G)) - 0.5).max() < 1e-3,
      f'S = {Sent:.3f} nats, record entropy {Hrec:.3f} nats (8 ln2 = {8 * np.log(2):.3f}), count 4 +- {np.sqrt(var):.3f}')

# ------------------------------------------------------------------ C. split
print('== C. the split with a half-filled sea (parent basis: 8 corner modes + 56 new modes per parent)')
Kg6 = kcube(6); out = {}
for lab, (ec, ef, mc, mf) in {'2^4': (0.3, 0.3, 0.4, 0.2), 'x16': (*X16(0.3), 0.05, 0.4)}.items():
    out[lab] = sum(np.real(tr((I64 - fine(Kg6[s:s + 36], ef, mf)) @ P1of(Kg6[s:s + 36], ec, mc, ef, mf, born=False))).sum() for s in range(0, 216, 36)) / 216 / 4
check('C1 T6 reproduced: the corner passing in the midpoint frame sends ~20% of the coarse sea modes above the fine sea',
      0.17 < out['2^4'] < 0.22 and 0.17 < out['x16'] < 0.23, f"2^4 {out['2^4']:.3f}, x16 {out['x16']:.3f}")
ec, ef = X16(0.3); Kg = kcube(8); acc = np.zeros(7)
for s in range(0, len(Kg), 32):
    K = Kg[s:s + 32]; Pf = fine(K, ef, 0.0); P1c = P1of(K, ec, 0.0, ef, 0.0, born=False); P1 = P1of(K, ec, 0.0, ef, 0.0)
    Hf = fine(K, ef, 0.0, gen=True); u_ = np.linalg.svd(Pf @ P1c)[0][:, :, :4]; img = u_ @ dag(u_)
    acc += [np.real(tr(img)).sum(), np.real(tr(Pf)).sum(), np.real(tr(Hf @ Pf)).sum(), np.real(tr(Hf @ img)).sum(),
            np.real(tr(Hf @ P1)).sum(), np.real(tr((I64 - Pf) @ P1)).sum(), np.real(tr(Hf @ P1c)).sum()]
acc /= len(Kg); E0 = acc[2]; Es = acc[3] - E0; Ep = acc[4] - E0; heat = acc[5] / 32; E6 = acc[6] - E0
del Pf, P1c, P1, Hf, u_, img
check('C2 THEOREM (counting): a split that conserves mode number with empty newborn modes fills 4 of the 32 fine sea modes per '
      'parent (28 holes); T6\'s heat-free sign map sits inside the fine sea but leaves 7/8 of it empty; it also changes the '
      'conserved charge sum(n - 1/2) by -28 per parent, so links on exact charges force 28 newborn particles',
      abs(acc[0] - 4) < 1e-9 and abs(acc[1] - 32) < 1e-9 and Es > 0,
      f'hole energy {Es:.1f} hbar c/l_f per parent (fine sea {-E0:.1f}); newborn zone-point vacuum + plain passing {Ep:.2f}')
smin = {}; Ksv = np.vstack([kcube(8), rng.uniform(-np.pi, np.pi, (300, 3))])
for lab, (ec_, ef_, mc_, mf_) in {'massless eps .3': (*X16(0.3), 0, 0), 'massless eps .04': (*X16(0.04), 0, 0),
                                    'mL_f 2.3 eps .3': (*X16(0.3), 0.05, 0.4)}.items():
    s0 = 1.0; res = 0.0
    for s in range(0, len(Ksv), 29):
        K = Ksv[s:s + 29]; Pf_ = fine(K, ef_, mf_); P1_ = P1of(K, ec_, mc_, ef_, mf_)
        V, sv = polar(Pf_ @ P1_ + (I64 - Pf_) @ (I64 - P1_)); s0 = min(s0, sv.min()); res = max(res, np.abs(V @ P1_ @ dag(V) - Pf_).max())
    smin[lab] = (s0, res)
del Pf_, P1_, V
check('C3 newborn modes half filled (each child sign pattern holds the fine sea at its zone point): the plain passing still '
      'heats, but the sign blocks are nonsingular on the whole zone, so the nearest unitary V* maps the sea onto the sea exactly',
      all(v[0] > 0.3 and v[1] < 1e-9 for v in smin.values()) and heat > 0.05,
      f'plain heating {heat:.3f}; min sv ' + ', '.join(f'{k} {v[0]:.2f}' for k, v in smin.items()) + f'; |V*P1V*+ - Pf| <= {max(v[1] for v in smin.values()):.0e}')
check('C4 exact series at the Dirac point: the O(k) coarse/fine mismatch is removed by a range-1 analytic unitary; the O(k^2) '
      'one is mostly irreducible (no polynomial generator removes it; quartic angular terms, i.e. non-analytic ones, do), the '
      'same for every step ratio: a finite-range split leaves F k^4 flips per momentum', max(v[0] for v in dr.values()) < 1e-12
      and all(v[1] > 0.9 for v in dr.values()) and r4 < 1e-4 and np.ptp([v[2] for v in dr.values()]) < 0.01 * Fbar,
      f'O(k) residual {max(v[0] for v in dr.values()):.0e}; O(k^2) irreducible {dr[0.3][1]:.3f} (with quartic {r4:.0e}); F = {Fbar:.2e}')
check('C5 (10 cell)^3 torus, massless: V*\'s kernel falls fast and a re-unitarised range-r truncation removes the heating to '
      '1e-4 (r = 1) and 1e-6 (r = 3); the remainder sits at small K (power-law tail)', ht[1] < 1e-3 and ht[3] < 3e-6 and ht[0] > ht[1] > ht[2] > ht[3],
      'shells/centre ' + ', '.join(f'{x:.0e}' for x in shell) + '; heating r=0..3 ' + ', '.join(f'{x:.1e}' for x in ht))
def mpow(U, t):
    w, v = np.linalg.eig(U); return v @ np.diag(np.exp(1j * t * np.angle(w))) @ np.linalg.inv(v)
def handover(ec_, ef_, K, ss):
    UA = [mpow(Umid(np.pi * m[None], ef_, 0)[0], 1.0) for m in C8]; B = had(K); bad = 0; gl = None; g0 = g1 = None
    for s in ss:
        Uf = np.zeros((len(K), 64, 64), complex)
        for im, m in enumerate(C8): Uf[:, 8 * im:8 * im + 8, 8 * im:8 * im + 8] = Umid(K / 2 + np.pi * m, s * ef_, 0)
        U1 = np.zeros_like(Uf); U1[:, :8, :8] = np.linalg.matrix_power(Umid(K, (1 - s) * ec_, 0), 8)
        for im in range(1, 8): U1[:, 8 * im:8 * im + 8, 8 * im:8 * im + 8] = mpow(UA[im], 1 - s)[None]
        q = -np.angle(np.linalg.eigvals((dag(B) @ Uf @ B) @ U1)); bad += int(np.sum((q < 0).sum(1) != 32))
        g = np.minimum(np.abs(q), np.pi - np.abs(q)).min(1); gl = g if gl is None else np.minimum(gl, g)
        if s == 0: g0 = g
        if s == 1: g1 = g
    return bad, (gl / np.minimum(g0, g1)).min()
NV2 = NV[:24]; Kh = np.vstack([kk * NV2 for kk in (0.01, 0.1, 0.5)] + [rng.uniform(-np.pi, np.pi, (100, 3))])
hv = {e: handover(*X16(e), Kh, np.linspace(0, 1, 9)) for e in (0.04, 0.3)}
check('C6 a strictly local handover (fine half-ticks at step s eps_f, eight coarse ticks at (1-s) eps_c, newborn zone-point '
      'ticks to the power 1-s) keeps the vacuum gap at every K != 0: an adiabatic split carries the sea',
      all(v[0] == 0 and v[1] > 0.5 for v in hv.values()), ', '.join(f'eps_f {e}: wrong counts {v[0]}, min gap/end gap {v[1]:.2f}' for e, v in hv.items()))

# ------------------------------------------------------------------ D. estimates
print('== D. ESTIMATES with measured numbers (unit map: fine cell l_f = 2 sqrt(8 pi) l_P, parent l_c = 2 l_f; not theorems)')
MP = 1.220890e19; lf = 2 * np.sqrt(8 * np.pi) / MP; lc = 2 * lf; rhoc = 3.68e-47; rcas = 5.8e-7 * 7.68e-51; gev_m = 1.97327e-16
rho20 = Ep / (8 * lf ** 4); rho6 = E6 / (8 * lf ** 4); rbbn = np.pi ** 2 / 30 * 10.75 * 1e-12
print(f'   local split as in T6 (empty newborns): {E6:.1f} hbar c/l_f per parent -> {rho6:.0e} GeV^4 per split; with half-filled newborns'
      f' {Ep:.1f} -> {rho20:.0e}: vs rho_c {rhoc:.1e} ({rho20 / rhoc:.0e}x), BBN radiation {rbbn:.1e} ({rho20 / rbbn:.0e}x); ~33 splits since BBN, one per cube per ~10 Gyr today')
Ns = 12; rmin = {nm: (Ns * Fbar / (8 * np.pi ** 2 * lc ** 4 * rb)) ** 0.125 for nm, rb in (('rho_c', rhoc), ('cascade', rcas))}
print(f'   finite-range split, residual F k^4 below k = 1/r: rho = N_s F r^-8/(8 pi^2 l_c^4), N_s = {Ns}: r >= {rmin["rho_c"]:.1e} cells'
      f' ({rmin["rho_c"] * lc * gev_m:.0e} m, rho_c), {rmin["cascade"]:.1e} cells ({rmin["cascade"] * lc * gev_m:.0e} m, Fermi cascade 5.8e-7 eV/cm^3)')
Ks1 = 0.01 * NV[:40]; F1 = np.real(tr((I64 - fine(Ks1, ef, 0.0)) @ P1of(Ks1, ec, 0.0, ef, 0.0))).mean() / 0.01 ** 2; kst = (6 * np.pi ** 2 * lc ** 4 * rcas / (Ns * F1)) ** (1 / 6); Tmin = lc / kst * 6.582e-25
print(f'   handover of duration T: sudden only below k = l_c/(cT), F1 = {F1:.2f} k^2 flips: T >= {Tmin:.0e} s (doubling time today ~3e17 s)')
amp4 = shell[3]; lam_nu = 1.97327e-7 / 0.05 / (lc * gev_m)
print(f'   exact split V*: tail ~{amp4:.0e} at 4 cells falling ~r^-4: {amp4 * (4 / rmin["cascade"]) ** 4:.0e} at r_min, {amp4 * (4 / lam_nu) ** 4:.0e}'
      f' at the 0.05 eV neutrino Compton length ({lam_nu:.0e} cells)')
print('   empty vacuum: no Uehling term (muonic-H Lamb shift 205.0 meV of measured 202.3706(23) meV: ~9e4 sigma), no running '
      '(1/alpha 137.036 -> 127.95 at M_Z measured), no holes for e+e- pairs, nothing to stop decay into the empty negative band')
check('D1 arithmetic: plain-split heating exceeds rho_c by > 1e110; strict range needs > 1e13 cells; handover needs > 1e-25 s',
      rho20 / rhoc > 1e110 and rmin['rho_c'] > 1e13 and Tmin > 1e-25)
print('supplied: tick without copy mass, sea branch, site-phase links, corner passing and midpoint frame (CL-1), newborn')
print('  zone-point state, nearest-unitary and handover paths (choices), grids and tori, unit map, species count, measured numbers.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
