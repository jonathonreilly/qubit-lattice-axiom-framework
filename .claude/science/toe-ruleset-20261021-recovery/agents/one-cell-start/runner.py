#!/usr/bin/env python3
"""one-cell-start: a universe that starts as ONE cube in its own vacuum and is refined only by CL-1's vacuum-carrying
splits.  What does the split history produce?  (supplied models; finite diagnostics; estimates labelled; no physical
identification beyond the stated unit map)
 A  one cube: the 2^3 torus, its 8 spin structures, the copy mass, the start's configurational entropy
 B  the exact split cascade from one cube (1 -> 4096 parent cubes); Born-mean homogeneity; the newborn state; a
    finite-range split on the cascade; the irreducible Dirac-point residual F (exact series)
 C  the split history with a finite range: occupation per comoving mode, the steady state, the reset of density
    excesses by triggered splits, the cascade tilt, the tensor ratio of a shot-noise seed
 D  the weak tick-fixing: adiabatic flips per split cycle
 E  estimates against measurement
Supplied: CL-1 tick without the copy mass for B-D (copy mass only in A), its negative-quasi-energy vacuum, CL-1's split
(midpoint of an even half-tick, corner passing, zone-point newborns, nearest unitary), the tick law sin(eps) ~ l^-2
inside a cycle (cubic Regge carrier), finite ranges r, the unit map, N_s = 12, measured numbers.
"""
from __future__ import annotations
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import factorial, comb
import numpy as np
import scipy.fft as sfft
from scipy.linalg import expm

T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ engine (CL-1 cube tick; inlined)
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8); I64 = np.eye(64)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C8[i] - 1.0) / r3; _, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(a + 1, 8):
        d_ = C8[a] - C8[b]
        if np.sum(abs(d_)) == 1:
            g_ = XI[a].conj() @ XI[b]; ax = int(np.argmax(abs(d_))); Wi[ax][a, b] = -g_ / abs(g_) / r3; Wi[ax][b, a] = np.conj(Wi[ax][a, b])
W = sum(Wi); SCOPY = 1j * (r3 * Wi[0]) @ (r3 * Wi[1]) @ (r3 * Wi[2]) @ W          # copy sign s = i R1 R2 R3 R
def expmW(t): return np.cos(t) * I8 - 1j * np.sin(t) * W
def dag(A): return np.conj(np.swapaxes(A, -1, -2))
def tr(A): return np.trace(A, axis1=-2, axis2=-1)
def Dm(K): return np.exp(1j * (np.atleast_2d(K) @ C8.T))
def Uo(Ko, Ki, M):
    Do, Di = Dm(Ko), Dm(Ki); return Do[:, :, None] * M[None] * Di.conj()[:, None, :]
def tick(K, eps, mu, M=0.0):
    Ue = expmW(eps - mu / 2)
    if M: Cm = expm(1j * (M / 4) * (I8 - SCOPY) @ W); Ue = Cm @ Ue @ Cm
    return Uo(K, K, expmW(-(eps + mu / 2))) @ Ue
def proj(U):
    cw = np.real(tr(U)) / 8; w = np.arccos(np.clip(cw, -1, 1)); X = (U - dag(U)) / (2j * np.sin(w)[:, None, None])
    return (I8 + X) / 2, (I8 - X) / 2, w
def sea(K, eps, mu, mid=True):                    # negative-quasi-energy projector; midpoint frame of the even half-tick
    P, _, w = proj(tick(np.atleast_2d(K), eps, mu))
    if mid: F = expmW((eps - mu / 2) / 2); P = F @ P @ F.conj().T
    return P, w
def projH(U):                                     # negative-quasi-energy projector for any spectrum (copy mass)
    _, vv = np.linalg.eigh((U - dag(U)) / 2j); vp = vv[:, :, 4:]; return vp @ dag(vp)
def seaC(K, eps, M, mid=True):                    # massless species with copy mass M on the even cubes; midpoint frame
    P = projH(tick(np.atleast_2d(K), eps, 0.0, M))
    if mid: F = expm(1j * (M / 4) * (I8 - SCOPY) @ W) @ expmW(eps / 2); P = F @ P @ F.conj().T
    return P
def band(K, eps, mu):
    b = np.pi / 2 - eps; A = (np.cos(2 * b) + np.cos(mu)) / 2
    return np.arccos(np.clip(A * np.mean(np.cos(K)) - (np.cos(2 * b) - np.cos(mu)) / 2, -1, 1))
def omega(K):                                     # rows: fine alias K/2 + pi m; columns: child sign pattern (-1)^(m'.c)
    K = np.atleast_2d(K); q = K[:, None, :] / 2 + np.pi * C8[None]; sg = (-1.0) ** C8
    return np.prod((1 + sg[None, None] * np.exp(-1j * q)[:, :, None, :]) / 2, axis=-1)
def had(K):  return np.einsum('nmk,ab->nmakb', omega(K), I8).reshape(len(np.atleast_2d(K)), 64, 64)
def fine(K, ef, mf, gen=False):                   # fine sea (or fine generator, units hbar c / l_f) in the parent basis
    K = np.atleast_2d(K); B = had(K); P = np.zeros((len(K), 64, 64), complex)
    for im, m in enumerate(C8):
        Pm, wm = sea(K / 2 + np.pi * m, ef, mf)
        P[:, 8 * im:8 * im + 8, 8 * im:8 * im + 8] = (wm[:, None, None] * (I8 - 2 * Pm) * r3 / np.sin(ef)) if gen else Pm
    return dag(B) @ P @ B
def newborn(ef, mf):                              # the 56 new modes per parent start in the children's zone-point sea
    Q = np.zeros((64, 64), complex)
    for im, m in enumerate(C8):
        if im: Q[8 * im:8 * im + 8, 8 * im:8 * im + 8] = sea(np.pi * m[None], ef, mf)[0][0]
    return Q
def P1of(K, ec, mc, ef, mf, NB=None):
    Pc, _ = sea(K, ec, mc); P = np.zeros((len(np.atleast_2d(K)), 64, 64), complex); P[:, :8, :8] = Pc
    return P + (newborn(ef, mf) if NB is None else NB)[None]
def polar(M):
    U, s, Vh = np.linalg.svd(M); return U @ Vh, s
def Kanti(Lc):                                    # antiperiodic cube momenta pi(2m+1)/Lc, kept in m order (FFT-ready)
    g = (np.pi * (2 * np.arange(Lc) + 1) / Lc + np.pi) % (2 * np.pi) - np.pi; return np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
EF = 0.3; EC = np.arcsin(np.sin(EF) / 4)          # tick law: sin(eps) falls 4x per cycle (l^-2), reset at the split

# ------------------------------------------------------------------ heavy part first: exact Dirac series (sea-split C4 method)
NO = 7
def X_series(n, eps, scale=1.0):
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
def dirac(ec_, ef_):
    SC = [X_series(n, ec_) for n in ND]; SF = [X_series(n, ef_, 0.5) for n in ND]; X0 = [s_[0] for s_ in SC]
    M1 = np.zeros((192, 192)); v1 = np.zeros(192)
    for n, c, f, x0 in zip(ND, SC, SF, X0):
        A = ccols(n, 1, x0); b = cvec(f[1] - c[1]); M1 += A.T @ A; v1 += A.T @ b
    x1, nulls = nsolve(M1, v1); r1 = np.sqrt(sum(np.sum((cvec(f[1] - c[1]) - ccols(n, 1, x0) @ x1) ** 2) for n, c, f, x0 in zip(ND, SC, SF, X0))
                                        / sum(np.sum(cvec(f[1] - c[1]) ** 2) for c, f in zip(SC, SF)))
    def rowsof(n, c, f, x0):
        L1 = build(n, 1, x1); C1 = L1 @ x0 - x0 @ L1; Nl = [build(n, 1, v) for v in nulls]
        b = cvec((f[2] - c[2]) - 1j * (L1 @ c[1] - c[1] @ L1) + 0.5 * (L1 @ C1 - C1 @ L1))
        A = np.hstack([ccols(n, 2, x0)] + [np.array([cvec(1j * (Nm @ c[1] - c[1] @ Nm) - 0.5 * (Nm @ C1 - C1 @ Nm)) for Nm in Nl]).T])
        return A, b
    M2 = None; bb = 0.0
    for z in zip(ND, SC, SF, X0):
        A, b = rowsof(*z); M2 = A.T @ A if M2 is None else M2 + A.T @ A; v2 = A.T @ b if bb == 0.0 else v2 + A.T @ b; bb += b @ b
    x2, _ = nsolve(M2, v2, 1e-13); rr = 0.0; Fl = []
    for z in zip(ND, SC, SF, X0):
        A, b = rowsof(*z); res = b - A @ x2; rr += res @ res
        R = res.reshape(2, 8, 8); R = R[0] + 1j * R[1]; k = 1e-2; Xf = sum(z[2][j] * k ** j for j in range(NO))
        wp, vp = np.linalg.eigh(Xf + k ** 2 * (R + R.conj().T) / 2); wf, vf = np.linalg.eigh(Xf)
        Fl.append(np.real(np.trace((I8 - vf[:, wf > 0] @ vf[:, wf > 0].conj().T) @ vp[:, wp > 0] @ vp[:, wp > 0].conj().T)) / k ** 4)
    return r1, np.sqrt(rr / bb), np.mean(Fl[:-4])
DR = dirac(EC, EF); FBAR = DR[2]

# ------------------------------------------------------------------ A. one cube
print('== A. one cube: the 2^3 torus')
def torus(Lb, eps, mu, bc):
    L = 2 * Lb; NS = L ** 3
    def idx(v):
        v = np.asarray(v); ph = np.prod([bc[i] for i in range(3) if v[i] >= L or v[i] < 0]) if (np.any(v >= L) or np.any(v < 0)) else 1.0
        v = v % L; return (v[0] * L + v[1]) * L + v[2], ph
    Ue = np.zeros((NS, NS), complex); Uo_ = np.zeros((NS, NS), complex); Me = expm(-1j * (eps - mu / 2) * W); Mo = expm(1j * (eps + mu / 2) * W)
    for n in itertools.product(range(Lb), repeat=3):
        n = np.array(n); ie = [idx(2 * n + t) for t in C8]; io = [idx(2 * n + 1 + (1 - t)) for t in C8]
        for a in range(8):
            for b in range(8):
                Ue[ie[a][0], ie[b][0]] += Me[a, b] * ie[a][1] * ie[b][1]; Uo_[io[a][0], io[b][0]] += Mo[a, b] * io[a][1] * io[b][1]
    return Uo_ @ Ue
dev = 0; zm = {}
for bc in itertools.product((1, -1), repeat=3):
    K = np.pi * (1 - np.array(bc)) / 2
    for mu in (0.0, 0.2):
        q = np.sort(-np.angle(np.linalg.eigvals(torus(1, EF, mu, bc)))); qb = np.sort(-np.angle(np.linalg.eigvals(tick(K, EF, mu)[0])))
        dev = max(dev, np.abs(q - qb).max(), np.abs(np.abs(q) - band(K, EF, mu)).max())
        if mu == 0: zm[bc] = int(np.sum(np.abs(q) < 1e-9))
dper = np.abs(torus(1, EF, 0.2, (1, 1, 1)) - expm(1j * 0.2 * W)).max(); dap = np.abs(torus(1, EF, 0.2, (-1, -1, -1)) - expm(-2j * EF * W)).max()
check('A1 THEOREM: on one cube the odd cube is the even cube (same sites, labels, overlap states), so the tick is exp(i mu W) '
      '(periodic: no hop) or exp(-2i eps W) (antiperiodic, mass-blind); spin structures = K in {0,pi}^3, on the band law',
      max(dev, dper, dap) < 1e-12, f'{max(dev, dper, dap):.0e}')
orbits = {}
for bc in zm: orbits.setdefault(tuple(sorted(bc)), []).append(bc)
inv = [o[0] for o in orbits.values() if len(o) == 1]
qM = {M: np.sort(np.abs(np.angle(np.linalg.eigvals(tick(np.full(3, np.pi), EF, 0.0, M)[0]))))[0] for M in (0.2, 0.4)}
check('A2 THEOREM: massless, only the periodic structure is gapless (its "negative modes filled" vacuum is empty, charge -4); '
      'the 7 twisted ones are unique, half filled; of the 2 rotation-invariant ones only (-,-,-). Copy mass: s^2 = 1, [s,W] = 0, '
      'gap 2 eps - M (open iff M < 2 eps)',
      zm[(1, 1, 1)] == 8 and all(v == 0 for k, v in zm.items() if k != (1, 1, 1)) and sorted(inv) == [(-1, -1, -1), (1, 1, 1)]
      and np.abs(SCOPY @ SCOPY - I8).max() < 1e-12 and np.abs(SCOPY @ W - W @ SCOPY).max() < 1e-12 and all(abs(qM[M] - (2 * EF - M)) < 1e-9 for M in qM),
      f'zero modes 8 (periodic), 0 (rest); gap M .2, .4: {qM[0.2]:.3f}, {qM[0.4]:.3f}')
def conf_entropy(V):
    p = np.array([abs(np.linalg.det(V[list(S), :])) ** 2 for S in itertools.combinations(range(8), 4)]); p = p[p > 1e-15]
    return -np.sum(p * np.log(p)), p.sum()
wv, vv = np.linalg.eigh(W); S0, n0 = conf_entropy(vv[:, wv < 0]); Pm1 = vv[:, wv < 0] @ vv[:, wv < 0].conj().T
dW = max(np.abs(sea(np.full(3, np.pi), e, m)[0][0] - Pm1).max() for e, m in ((0.3, 0.2), (0.04, 0.0), (1.1, 0.5)))
dW = max(dW, np.abs(seaC(np.full(3, np.pi), EF, 0.4)[0] - Pm1).max())
check('A3 the (-,-,-) one-cube vacuum is the W = -1 eigenspace at every step, mass and copy mass M < 2 eps; its 70 '
      'configurations hold all the initial randomness', dW < 1e-12 and abs(n0 - 1) < 1e-10 and 0 < S0 < np.log(70),
      f'|P - P(W=-1)| {dW:.0e}; S0 = {S0:.3f} nats of ln 70 = {np.log(70):.3f}')

# ------------------------------------------------------------------ B. exact cascade
print('== B. the exact split cascade from one (-,-,-) cube (1 to 4096 parent cubes)')
def level(n, ec, mc, ef, mf, NB=None, BS=64):
    K = Kanti(2 ** n); smin = 9; res = 0; plain = 0; hv = 0; occ = []
    for s0 in range(0, len(K), BS):
        k = K[s0:s0 + BS]; Pf = fine(k, ef, mf); P1 = P1of(k, ec, mc, ef, mf, NB)
        V, sv = polar(Pf @ P1 + (I64 - Pf) @ (I64 - P1)); smin = min(smin, sv.min())
        res = max(res, np.abs(V @ P1 @ dag(V) - Pf).max()); plain += np.real(tr((I64 - Pf) @ P1)).sum()
        hv += np.real(tr((I64 - Pf) @ V @ P1 @ dag(V))).sum(); occ.append(np.real(np.einsum('kaa->ka', sea(k, ec, mc, mid=False)[0])))
    return smin, res, plain / len(K) / 32, hv / len(K) / 32, np.vstack(occ).mean(0), (np.linalg.norm(V[0] - I64, 2) if n == 0 else None)
cas = {}
for lab, (ef, mf) in {'massless': (EF, 0.0), 'mu .2': (EF, 0.2), 'eps .04': (0.04, 0.0)}.items():
    ec = np.arcsin(np.sin(ef) / 4); cas[lab] = [level(n, ec, mf / 2, ef, mf) for n in range(5)]
smin = min(l[0] for v in cas.values() for l in v); res = max(l[1] for v in cas.values() for l in v); heat = max(abs(l[3]) for v in cas.values() for l in v)
check('B1 at every level the sign blocks are nonsingular, so the nearest unitary V* exists and carries the vacuum onto the '
      'children\'s vacuum (no heating); the plain passing alone heats every level',
      smin > 0.3 and res < 1e-10 and heat < 1e-12, f'min sv {smin:.2f}; |V*P1V*+ - Pf| {res:.0e}; heat {heat:.0e}; plain, levels 0 and 4: '
      + f"{cas['massless'][0][2]:.3f}, {cas['massless'][4][2]:.3f} (mu 0), {cas['mu .2'][0][2]:.3f}, {cas['mu .2'][4][2]:.3f} (mu .2)")
def splitC(n, Mf):                                # copy mass angle ~ tick: M_c = M_f/2 at the parent
    K = Kanti(2 ** n); B = had(K); Pf = np.zeros((len(K), 64, 64), complex); NB = np.zeros((64, 64), complex)
    for im, m in enumerate(C8):
        Pf[:, 8 * im:8 * im + 8, 8 * im:8 * im + 8] = seaC(K / 2 + np.pi * m, EF, Mf)
        if im: NB[8 * im:8 * im + 8, 8 * im:8 * im + 8] = seaC(np.pi * m[None], EF, Mf)[0]
    Pf = dag(B) @ Pf @ B; P1 = np.zeros_like(Pf); P1[:, :8, :8] = seaC(K, EC, Mf / 2); P1 += NB[None]
    V, sv = polar(Pf @ P1 + (I64 - Pf) @ (I64 - P1)); return sv.min(), np.abs(V @ P1 @ dag(V) - Pf).max()
cm = {Mf: [splitC(n, Mf) for n in range(3)] for Mf in (0.28, 0.32)}
check('B1b with the copy mass the split exists iff the parent partner gap at K = pi(1,1,1) is open (M_c < 2 eps_c); the '
      'one-cube split sits on that momentum and fails first (tick law: M < ~eps at birth)',
      all(v[0] > 0.3 and v[1] < 1e-10 for v in cm[0.28]) and cm[0.32][0][0] < 1e-10 and all(v[0] > 0.2 and v[1] < 1e-10 for v in cm[0.32][1:]),
      f'2 eps_c = {2 * EC:.3f}; M_c .14: sv ' + ', '.join(f'{v[0]:.2f}' for v in cm[0.28]) + '; M_c .16: sv ' + ', '.join(f'{v[0]:.0e}' for v in cm[0.32]) + f' (levels 0-2)')
occd = max(np.abs(l[4] - 0.5).max() for v in cas.values() for l in v)
check('B2 THEOREM (symmetry): each level is invariant under its cube translations with every site half filled, so every Born '
      'mean is homogeneous above one cube and CL-3 sees no departure (empty de Sitter, H = sqrt(Lambda/3)); a seed must be '
      'a departure\'s actual configuration', occd < 1e-12, f'max |<n> - 1/2| {occd:.0e}')
rng = np.random.default_rng(1); sdef = []; K0 = np.full((1, 3), np.pi); Pf0 = fine(K0, EF, 0.0)
for trial in range(8):
    dg = np.zeros(64); dg[8 + rng.choice(56, 28, replace=False)] = 1; P1 = P1of(K0, EC, 0.0, EF, 0.0, np.diag(dg).astype(complex))
    M_ = Pf0 @ P1 + (I64 - Pf0) @ (I64 - P1); sv = np.linalg.svd(M_[0], compute_uv=False); V_ = polar(M_)[0]
    sdef.append((sv.min(), np.linalg.norm(V_[0] - I64, 2), np.real(tr((I64 - Pf0) @ V_ @ P1 @ dag(V_)))[0] / 32))
sing = sum(s < 1e-10 for s, _, _ in sdef); good = [x for x in sdef if x[0] > 1e-10]
check('B3 definite newborn modes instead of the zone-point sea: sign blocks singular in about half the draws (V* undefined), '
      'nearly singular otherwise; where V* exists it heats nothing: the newborn state conditions the split, never sources',
      0 < sing < 8 and max(x[0] for x in good) < 0.2 and max(abs(x[2]) for x in good) < 1e-12 and cas['massless'][0][0] > 0.5,
      f'singular {sing}/8; else min sv <= {max(x[0] for x in good):.2f}, |V*-1| {np.mean([x[1] for x in good]):.2f} (sea newborns: '
      f"{cas['massless'][0][0]:.2f}, {cas['massless'][0][5]:.2f})")
def trunc(Lc, rs, BS=64):
    K = Kanti(Lc); NK = len(K); V = np.empty((NK, 64, 64), complex)
    for s0 in range(0, NK, BS):
        k = K[s0:s0 + BS]; Pf = fine(k, EF, 0.0); P1 = P1of(k, EC, 0.0, EF, 0.0); V[s0:s0 + BS] = polar(Pf @ P1 + (I64 - Pf) @ (I64 - P1))[0]
    VR = sfft.ifftn(V.reshape(Lc, Lc, Lc, 64, 64), axes=(0, 1, 2), workers=1, overwrite_x=True); del V
    Rw = np.minimum(np.arange(Lc), Lc - np.arange(Lc)); Rin = np.maximum(np.maximum(Rw[:, None, None], Rw[None, :, None]), Rw[None, None, :])
    out = []
    for r in rs:
        Vt = VR.copy(); Vt[Rin > r] = 0; Vt = sfft.fftn(Vt, axes=(0, 1, 2), workers=1, overwrite_x=True).reshape(NK, 64, 64); h = e = 0.0
        for s0 in range(0, NK, BS):
            k = K[s0:s0 + BS]; Pf = fine(k, EF, 0.0); P1 = P1of(k, EC, 0.0, EF, 0.0); Hf = fine(k, EF, 0.0, gen=True)
            U_ = polar(Vt[s0:s0 + BS])[0]; img = U_ @ P1 @ dag(U_)
            h += np.real(tr((I64 - Pf) @ img)).sum(); e += np.real(tr(Hf @ img) - tr(Hf @ Pf)).sum()
        out.append((r, h / NK / 32, e / NK)); del Vt
    return out
tr2, tr4, tr8 = trunc(2, (0, 1)), trunc(4, (0, 1, 2)), trunc(8, (0, 1, 2, 3, 4))
EP = {r: e for r, h, e in tr8}
check('B4 a range-r split on the cascade is exact while the universe is at most 2r+1 parent cubes across (the first log2(2r) '
      'splits), and heats every split after that',
      tr2[1][1] < 1e-12 and tr4[2][1] < 1e-12 and tr8[4][1] < 1e-12 and min(tr4[1][1], tr8[3][1]) > 1e-8,
      '8^3, r = 0..3: heat ' + ', '.join(f'{h:.1e}' for r, h, e in tr8[:4]) + '; energy/parent ' + ', '.join(f'{e:.1e}' for r, h, e in tr8[:4]))
check('B5 exact Dirac series: the O(k) mismatch is removable by a range-1 unitary, the O(k^2) one is not (non-analytic), so the '
      'best finite-range split leaves F k^4 flips per momentum', DR[0] < 1e-12 and DR[1] > 0.9 and 1e-5 < FBAR < 1e-4,
      f'O(k) residual {DR[0]:.0e}; irreducible share {DR[1]:.3f}; F = {FBAR:.3e}')

# ------------------------------------------------------------------ C. finite-range history
print('== C. the split history with a finite range r (k per parent cell)')
lk = np.linspace(-6, 2, 4001); kk = 2.0 ** lk; js = np.arange(0, 60)
def occ_sum(f): return np.array([np.sum(f(k * 2.0 ** js)) for k in kk])   # a mode now at k had k 2^j j splits back
fs = lambda k: FBAR * k ** 4 * (k < 1.0); fm = lambda k: FBAR * k ** 4 / (1 + k ** 8)
ns, nm = occ_sum(fs), occ_sum(fm); sel = (lk > -5) & (lk < -4)
mod = lambda n: (n[sel].max() - n[sel].min()) / (n[sel].max() + n[sel].min())
check('C1 THEOREM (cascade sum): a comoving mode\'s lattice momentum halves each split, so its occupation is the sum of f(k 2^j) '
      'over past splits: constant on average, log-periodic ripple of period ln 2; energy per log k ~ p^4 n sits at the cutoff '
      '(blue)', abs(ns[sel].mean() / (FBAR / (4 * np.log(2))) - 1) < 0.02,
      f'mean n = {FBAR / (4 * np.log(2)):.2e} r^-4; ripple sharp {mod(ns):.2f}, smooth {mod(nm):.2f}; energy within 2x of cutoff {1 - 2 ** -8:.3f}')
def steady(p, n=400, H0=1.0):
    D = (15 / 16) * (3 / (8 * np.pi)) * H0 ** (2 - p); rho = 0.0; H = 1.3 * H0
    for _ in range(n):
        rho = rho / 16 + D * H ** p; H = np.sqrt(8 * np.pi / 3 * rho)
        if not 1e-6 < H < 1e6: break
    return H
st = {p: steady(p) for p in (0, 1, 1.9, 2.5)}
check('C2 THEOREM (steady state): Delta rho per split, radiation diluting 16x: rho -> (16/15) Delta rho, H a 4x sawtooth. '
      'For Delta rho ~ H^p: a stable, unending fixed point iff p < 2, injecting (15/16)(H*/H0)^(2-p) rho_c per split '
      'today; p > 2 cannot sustain itself',
      all(abs(st[p] - 1) < 1e-6 for p in (0, 1)) and abs(st[1.9] - 1) < 1e-3 and not (0.5 < st[2.5] < 2),
      'H/H*, 400 splits: ' + ', '.join(f'p={p}: {v:.3g}' for p, v in st.items()))
d0 = 1e-3; da = []; ra = rb = 1 / 15
for n in range(4):
    ra, rb = ra * (1 + (d0 if n == 0 else 0)) + 1.0, rb + 1.0; da.append(ra / rb - 1); ra, rb = ra / 16, rb / 16
check('C3 THEOREM (reset): a triggered split injects the same energy at the same local edge length, so a density excess at '
      'fixed local e-fold number falls by rho-/rho+ = 1/16 per split: super-Hubble zeta is erased unless another clock ends the phase',
      all(abs(da[i + 1] / da[i] - 1 / 16) < 1e-9 for i in range(3)), 'excess: ' + ', '.join(f'{x:.2e}' for x in da))
Lv = 40; hl = 2.0 ** -np.arange(Lv + 1); kq = 2.0 ** np.linspace(4, 30, 300)
def slope(q, lam, ka, kb):
    P = np.array([np.sum(q ** (2 * (Lv - np.arange(Lv + 1))) * lam ** np.arange(Lv + 1) * hl ** 3 * np.exp(-(k * hl) ** 2)) for k in kq])
    D2 = kq ** 3 * P; m = (kq > ka) & (kq < kb); return np.polyfit(np.log2(kq[m]), np.log2(D2[m]), 1)[0]
LP = 2 ** (0.9649 - 1); LA = 2 ** (0.974 - 1)
sl = {'lam 1': slope(1, 1, 2 ** 8, 2 ** 28), 'Planck': slope(1, LP, 2 ** 8, 2 ** 28), 'ACT': slope(1, LA, 2 ** 8, 2 ** 28), 'reset': slope(1 / 16, 1, 2 ** 5, 2 ** 25)}
check('C4 THEOREM (cascade): per-level variance lambda^l inherited by finer levels gives n_s - 1 = log2 lambda; a fixed-range '
      'split is self-similar (lambda = 1, n_s = 1); with the reset of C3 the frozen spectrum is white',
      abs(sl['lam 1']) < 2e-3 and abs(sl['Planck'] - np.log2(LP)) < 2e-3 and abs(sl['reset'] - 3) < 0.02,
      'index of Delta^2: ' + ', '.join(f'{k} {v:+.4f}' for k, v in sl.items()) + f' (log2 lambda {np.log2(LP):+.4f}, {np.log2(LA):+.4f})')
hN = h_ = 0.0; dN = np.log(2) / 4000; h1 = None          # super-Hubble h_NN + h_N = 6 pi(N) per cycle (radiation); h_N/4 at a split
for cyc in range(8):
    for _ in range(4000): hN += dN * (6 * 16.0 ** -cyc - hN); h_ += dN * hN
    if cyc == 0: h1 = h_
    hN /= 4
zcyc = (16 / 15) * np.log(2) / 2; rT = 2 * (h_ / np.sqrt(15) / zcyc) ** 2; h1x = 6 * (np.log(2) - 0.5)
check('C5 ESTIMATE (shot-noise seed): free-streaming quanta carry TT stress at 1/15 of their energy variance per polarisation; '
      'on the sawtooth h_+ = 1.69 pi, zeta = 0.37 delta (proper-time exit clock): r = O(1)',
      abs(h1 - h1x) < 1e-3 and rT > 0.5, f'h/pi cycle 1 {h1:.3f} (exact {h1x:.3f}), total {h_:.3f}; zeta/delta {zcyc:.3f}; r ~ {rT:.1f}')

# ------------------------------------------------------------------ D. tick fixing
print('== D. the weak tick-fixing: sin(eps) ~ l^-2 over a cycle of N ticks (mu ~ 1/l)')
def ramp(K, e0, m0, N, mid=False):                # step updated at half-tick boundaries (mid=False) or mid even half-tick
    K = np.atleast_2d(K); P0, _ = sea(K, e0, m0, mid=mid); Vv = np.linalg.svd(P0)[0][:, :, :4]
    for j in range(N):
        x = (j + 0.5) / N; e = np.arcsin(np.sin(e0) / (1 + x) ** 2); m = m0 / (1 + x)
        if mid: F = expmW((e - m / 2) / 2); Vv = F @ (Uo(K, K, expmW(-(e + m / 2))) @ (F @ Vv))
        else: Vv = tick(K, e, m) @ Vv
    P1, w1 = sea(K, np.arcsin(np.sin(e0) / 4), m0 / 2, mid=mid)
    return np.real(np.einsum('kai,kab,kbi->k', Vv.conj(), I8 - P1, Vv)), w1
KG = Kanti(8); cN = {}
for e0 in (0.3, 0.04):
    for N in (100, 300, 1000):
        f_, w_ = ramp(KG, e0, 0.0, N); cN[(e0, N)] = (f_.mean() * N ** 2, np.mean(f_ * w_) * N ** 2)
cmid = {e0: ramp(KG, e0, 0.0, 300, True)[0].mean() * 300 ** 2 for e0 in (0.3, 0.04)}
fsm = max(abs(ramp(k * np.eye(3), 0.3, 0.0, 100, True)[0]).max() for k in (0.01, 0.1))
check('D1 finite diagnostic (8^3 grid): a smooth tick ramp flips c/N^2 of the sea per cycle; c = O(1) with the step read per '
      'half-tick (oscillating in N: the two kinks interfere), far less if it changes mid even half-tick; long modes untouched',
      all(0.2 < v[0] < 1.5 for v in cN.values()) and max(cmid.values()) < 0.05 and fsm < 1e-5,
      'c = ' + ', '.join(f'{v[0]:.2f}' for v in cN.values()) + f' (eps .3, .04; N 100-1000); midpoint {cmid[0.3]:.3f}, {cmid[0.04]:.0e}; k <= .1: {fsm:.0e}')
def tick_fraction(e0, cE, H=1e-3, l0=1.0):         # energy per tile 2 cE/N^2 per tick T at the cycle end; 8 pi G = (l0/2)^2
    s0 = np.sin(e0); N = r3 / (H * l0 * s0); lend = 2 * l0; Tend = lend * (s0 / 4) / r3
    return (2 * cE / N ** 2 / Tend / lend ** 3) / (12 * H ** 2 / l0 ** 2)
fr = {e0: tick_fraction(e0, np.mean([cN[(e0, N)][1] for N in (100, 300, 1000)])) for e0 in (0.3, 0.04)}
check('D2 ESTIMATE: N = sqrt3/(H a sin eps0) ticks per cycle, so the ramp injects a fixed fraction of rho_crit per split '
      '(p = 2 in C2), zone-scale, far below the 15x a self-sustained phase needs',
      all(v < 1e-2 for v in fr.values()), 'per split: ' + ', '.join(f'eps0 {e0}: {v:.1e} rho_crit' for e0, v in fr.items()))

# ------------------------------------------------------------------ E. measurement
print('== E. ESTIMATES vs measurement (l_f = 2 sqrt(8 pi) l_P, l_c = 2 l_f; N_s = 12; not theorems)')
MP = 1.220890e19; lc = 4 * np.sqrt(8 * np.pi) / MP; lf = lc / 2; rhoc = 3.68e-47; H0 = 67.4e3 / 3.0857e22 * 6.582e-25; HL = H0 * np.sqrt(0.685)
Ns = 12; c8 = Ns * FBAR / (8 * np.pi ** 2 * lc ** 4); rho13 = (15 / 16) * 3 / (8 * np.pi) * (1e13 * MP) ** 2
r_today = (c8 / rhoc) ** 0.125; r_inf = (c8 / rho13) ** 0.125; tsplit = np.log(2) / HL * 6.582e-25 / 3.156e16
e3 = EP[3]; rt_inf = 3 * (Ns * e3 / (8 * lf ** 4) / rho13) ** 0.2; rt_today = 3 * (Ns * e3 / (8 * lf ** 4) / rhoc) ** 0.2
print(f'   exact cascade: 0 departures vs 3.4e80 occupied modes (F1); Lambda only: one split per {tsplit:.1f} Gyr')
print(f'   steady H = 1e13 GeV needs r = {r_inf:.1f} (best map, F k^4) to {rt_inf:.0f} (truncated V*, r^-5 from B4); today rho_c needs r >= {r_today:.1e} to {rt_today:.0e}')
print(f'   so a range allowed today injects <= rho_c0 per split at every epoch: H_ss <= {np.sqrt(16 / 15):.2f} H0 (inflation needs (H/H0)^2 = {(1e13 / H0) ** 2:.0e} more)')
sig = lambda ns_, m, s: (ns_ - m) / s
print(f'   lambda = 2^(n_s-1): Planck {LP:.5f}, ACT {LA:.5f}, DR2 {2 ** (0.9752 - 1):.5f}; n_s = 1 is {sig(1, .9649, .0042):.1f}, {sig(1, .974, .003):.1f}, {sig(1, .9752, .003):.1f} sigma; n_s = 4: {sig(4, .9649, .0042):.0f}')
print(f'   shot-noise r ~ {rT:.0f} vs < 0.036; Q = B = L = 0 at half filling: eta = 0 vs 6.1e-10; Omega_k = 0 vs 0.0007 +- 0.0019')
check('E1 arithmetic: every channel misses a measured fact (matter, n_s, r or today\'s injection bound)',
      r_today > 1e13 and r_inf < 10 and rt_inf < 1e3 and sig(1, .974, .003) > 5 and rT > 1 and tsplit > 1)
print('supplied: tick (copy mass only in A, B1b), vacuum branch, CL-1 split, (-,-,-) start, tick law, ranges r, ramp,')
print('  separate-universe/GR response (C3-C5), unit map, N_s, measured numbers.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
