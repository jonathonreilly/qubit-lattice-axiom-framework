#!/usr/bin/env python3
"""Proposal test: the gravitational source of each relay is the canonical conserved stress of its
CONDITIONAL odds (the joint odds with every other relay fixed at its actual block and direction);
relays follow the joint odds by minimal switching only (no redraws; CL-5 energy and CL-7 deposits dropped).
Supplied lossless 1D coin-shift walks and few-relay toys; no physical identification.
A. Page-Geilker toy: ball conditioned on a pointer of n imperfect relays (or on its own other relays).
B. Single relay: canonical stress (eps, k, eps v, k v per mode) for plane, standing and packet states.
C. Entangled pair: conditional source per configuration, its Born mean, per-tick jumps under minimal
   switching, and the interaction (binding) energy a per-subsystem free stress leaves out.
D. Remote setting: B's conditional source distribution under A's z / x setting; means; sizes in SI.
E. Minimal switching only: joint Born, reader agreement, CHSH.
F. Single elementary relay versus a bound pair in a two-arm superposition; back-reaction estimates.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/CONDITIONAL_ODDS_CANONICAL_STRESS_AS_THE_RELAY_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import os, sys, signal
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
def _timeout(*a):
    raise TimeoutError('120-second cap exceeded')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

PASS = FAIL = 0
rng = np.random.default_rng(20261021)
TH = 0.2


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------- walk: (x, d) flattened x*2+d; d=0 steps +1, d=1 steps -1; tick U = S C
def mats(N, th):
    c, s = np.cos(th), np.sin(th)
    C = np.zeros((2 * N, 2 * N), complex); S = np.zeros((2 * N, 2 * N))
    for x in range(N):
        C[2 * x:2 * x + 2, 2 * x:2 * x + 2] = [[c, -1j * s], [-1j * s, c]]
        S[2 * ((x + 1) % N), 2 * x] = 1; S[2 * ((x - 1) % N) + 1, 2 * x + 1] = 1
    return C, S


class Bands:
    """band data per lattice momentum k = 2 pi fftfreq(N): eps_n(k) = -arg(eigenvalue), v_n = <sigma_z>."""
    def __init__(self, N, th):
        self.N = N; self.k = 2 * np.pi * np.fft.fftfreq(N); c, s = np.cos(th), np.sin(th)
        Cc = np.array([[c, -1j * s], [-1j * s, c]]); self.E = np.zeros((N, 2)); self.V = np.zeros((N, 2, 2), complex)
        for i, k in enumerate(self.k):
            w, X = np.linalg.eig(np.diag([np.exp(-1j * k), np.exp(1j * k)]) @ Cc)
            o = np.argsort(np.angle(w)); self.E[i] = -np.angle(w[o]); self.V[i] = X[:, o]
        self.v = (abs(self.V[:, 0]) ** 2 - abs(self.V[:, 1]) ** 2)   # (k, n)
        kk = np.repeat(self.k[:, None], 2, 1)
        # canonical per-mode stress: T00 = eps, Tx0 = k (momentum), T0x = eps v (energy flux), Txx = k v
        self.f = np.stack([self.E, kk, self.E * self.v, kk * self.v])

    def mode(self, k, n=0):
        i = int(np.argmin(abs((self.k - k + np.pi) % (2 * np.pi) - np.pi)))
        return np.outer(np.exp(1j * self.k[i] * np.arange(self.N)), self.V[i][:, n]).ravel() / np.sqrt(self.N), i

    def canon(self, psi):
        """psi shape (N, 2, ...) -> (T[4, ...], weight); quadratic in psi, normalised by weight."""
        ph = np.fft.fft(psi, axis=0) / np.sqrt(self.N)
        c = np.einsum('kdn,kd...->kn...', self.V.conj(), ph); w = abs(c) ** 2; W = w.sum((0, 1))
        return np.einsum('fkn,kn...->f...', self.f, w) / np.where(W > 0, W, 1), W


def band_packet(B, th, k0, x0, sig):
    N = B.N; amp = np.zeros((N, 2), complex)
    for i, k in enumerate(B.k):
        v = B.V[i][:, 0] * np.exp(-1j * np.angle(B.V[i][0, 0])); dk = (k - k0 + np.pi) % (2 * np.pi) - np.pi
        amp[i] = v * np.exp(-dk ** 2 * sig ** 2 / 2 - 1j * k * x0)
    psi = np.fft.ifft(amp, axis=0) * np.sqrt(N); return (psi / np.linalg.norm(psi)).ravel()


# ---------------- relay machinery (minimal joint switching, no redraws)
def flow(Q, P, Pn):
    N1, N2 = P.shape[0], P.shape[2]; t = lambda A: A.transpose(0, 2, 1, 3).reshape(N1 * N2, 4)
    q, p, pn = t(Q), t(P), t(Pn); ex = np.clip(p - pn, 0, None); sh = np.clip(pn - p, 0, None); Ssh = sh.sum(1, keepdims=True)
    out = q * np.where(p > 0, ex / np.where(p > 0, p, 1), 0.0); to = np.where(Ssh > 0, sh / np.where(Ssh > 0, Ssh, 1), 0)
    return (q - out + out.sum(1, keepdims=True) * to).reshape(N1, N2, 2, 2).transpose(0, 2, 1, 3), out.sum()


def flow_sample(P, Pn, x1, d1, x2, d2):
    N2 = P.shape[2]; t = lambda A: A.transpose(0, 2, 1, 3).reshape(-1, 4)
    p, pn = t(P), t(Pn); ex = np.clip(p - pn, 0, None); sh = np.clip(pn - p, 0, None)
    blk = x1 * N2 + x2; d = 2 * d1 + d2; pr = p[blk, d]
    sw = (rng.random(len(d)) < np.where(pr > 0, ex[blk, d] / np.where(pr > 0, pr, 1), 0)) & (sh[blk].sum(1) > 0)
    if sw.any():
        cs = np.cumsum(sh[blk[sw]], 1); cs /= cs[:, -1:]; d = d.copy(); d[sw] = np.minimum((rng.random(sw.sum())[:, None] > cs).sum(1), 3)
    return d // 2, d % 2


def shiftQ(Q):
    Q = Q.copy(); Q[:, 0] = np.roll(Q[:, 0], 1, 0); Q[:, 1] = np.roll(Q[:, 1], -1, 0)
    Q[:, :, :, 0] = np.roll(Q[:, :, :, 0], 1, 2); Q[:, :, :, 1] = np.roll(Q[:, :, :, 1], -1, 2); return Q


def sample(P, M):
    N2 = P.shape[2]; idx = rng.choice(P.size, M, p=(P / P.sum()).ravel())
    x1, rem = np.divmod(idx, 2 * N2 * 2); d1, rem = np.divmod(rem, N2 * 2); x2, d2 = np.divmod(rem, 2); return x1, d1, x2, d2


def chi2(P, x1, d1, x2, d2):
    h = np.bincount(((x1 * 2 + d1) * P.shape[2] + x2) * 2 + d2, minlength=P.size); e = len(x1) * P.ravel(); k = e >= 5
    return ((h[k] - e[k]) ** 2 / e[k]).sum() / max(k.sum() - 1, 1), k.sum()


odds = lambda Psi, N: (abs(Psi) ** 2).reshape(N, 2, N, 2)


# ---------------- A. Page-Geilker
def torque(n, s, sig, M=16000, L=61):
    """ball at L/R (orthogonal), pointer of n relays with Gaussian block amplitudes centred s apart.
    torque (classical-ball units) = E[P(actual | pointer) - P(other | pointer)]; exact conditional odds."""
    x = np.arange(L); gL = np.exp(-(x - (L // 2 - s / 2)) ** 2 / (2 * sig ** 2)); gR = np.exp(-(x - (L // 2 + s / 2)) ** 2 / (2 * sig ** 2))
    gL /= gL.sum(); gR /= gR.sum(); bc = np.sqrt(gL * gR).sum(); lr = np.log(gL) - np.log(gR)
    if n == 1:   # exact sum: branch L by symmetry
        pl = 1 / (1 + np.exp(-lr)); return (gL * (2 * pl - 1)).sum(), bc
    ell = np.zeros(M)
    for j in range(0, n, 16): ell += lr[rng.choice(L, (M, min(16, n - j)), p=gL)].sum(1)
    return (2 / (1 + np.exp(-ell)) - 1).mean(), bc


def section_pg():
    print('A. Page-Geilker toy: ball (L or R, weight 1/2) conditioned on n pointer relays')
    res = {n: torque(n, 2.0, 1.5) for n in (1, 4, 16, 64, 256)}; bc = res[1][1]
    check('A1 full odds (no conditioning): torque 0; conditional odds: torque rises to 1 with n', res[256][0] > 0.999 and res[1][0] < 0.5,
          f'per-relay overlap {bc:.3f}; ' + ', '.join(f'n={n}: {t:.4f}' for n, (t, _) in res.items()))
    check('A2 bound 1 - torque <= overlap^n (Bhattacharyya; rederived by AM-GM)', all(1 - t <= bc ** n + 0.02 for n, (t, _) in res.items()),
          ', '.join(f'n={n}: {1 - t:.1e} <= {bc ** n:.1e}' for n, (t, _) in res.items() if n > 1))
    t_ideal = torque(1, 40.0, 1.5)[0]
    check('A3 one ideal pointer relay (disjoint supports): torque 1', abs(t_ideal - 1) < 1e-12, f'{t_ideal:.15f}')
    print('   a ball of N relays is its own pointer (n = N-1 others): N=1 torque 0; a kg ball (N~1e25) torque 1 - O(overlap^1e25)')


# ---------------- B. single relay stress
def section_single():
    print('B. single relay (theta 0.1, N 154): canonical stress (T00, Tx0, T0x, Txx), CL-7 standing T_xx was -0.0563')
    th, N = 0.1, 154; B = Bands(N, th); C, S = mats(N, th); U = S @ C; k = 2 * np.pi * 5 / N
    a, ia = B.mode(k); b, ib = B.mode(-k); fa = B.f[:, ia, 0]
    Tp, _ = B.canon(a.reshape(N, 2)); Ts, _ = B.canon(((a + b) / np.sqrt(2)).reshape(N, 2))
    check('B1 plane wave: (eps, k, eps v, k v)', abs(Tp - fa).max() < 1e-12, f'T={np.round(Tp, 4)}')
    check('B2 standing wave: T00 = eps, momentum 0, energy flux 0, Txx = k v (same sign and size as the plane wave)',
          abs(Ts - np.array([fa[0], 0, 0, fa[3]])).max() < 1e-12, f'T={np.round(Ts, 4)}')
    ks = 2 * np.pi * np.array([1, 3, 5, -4, -6, 8]) / N; c = rng.normal(size=6) + 1j * rng.normal(size=6); c /= np.linalg.norm(c)
    ms = [B.mode(q) for q in ks]; p = sum(ci * m[0] for ci, m in zip(c, ms)); tgt = sum(abs(ci) ** 2 * B.f[:, m[1], 0] for ci, m in zip(c, ms))
    T6, _ = B.canon(p.reshape(N, 2))
    check('B3 linear: 6-mode packet stress = odds-weighted mode stresses', abs(T6 - tgt).max() < 1e-12, f'Txx {T6[3]:.4f} (target {tgt[3]:.4f})')
    q = band_packet(B, th, 0.3, 40, 4.0); T0, _ = B.canon(q.reshape(N, 2)); dev = 0
    for _ in range(60): q = U @ q; dev = max(dev, abs(B.canon(q.reshape(N, 2))[0] - T0).max())
    check('B4 conserved: a moving packet keeps its integrated stress for 60 ticks', dev < 1e-12, f'max dev {dev:.1e}, T={np.round(T0, 4)}')
    r = [B.f[2, B.mode(q)[1], 0] / B.f[1, B.mode(q)[1], 0] for q in (k, k / 5)]
    check('B5 lattice asymmetry: energy flux / momentum density = eps v / k -> theta/tan(theta) at k -> 0 (the low-k c_eff^2), 1 only as theta -> 0',
          r[0] < r[1] < 1 and abs(r[1] - th / np.tan(th)) < 2e-5, f'k={k:.3f}: {r[0]:.5f}; k={k / 5:.4f}: {r[1]:.6f}; theta/tan theta {th / np.tan(th):.6f}')
    ev, V = np.linalg.eig(U); H = V @ np.diag(-np.angle(ev)) @ np.linalg.inv(V)
    hr = [abs(H[2 * 77:2 * 77 + 2, 2 * (77 + d):2 * (77 + d) + 2]).max() for d in (0, 10, 20, 40)]
    rate = np.log(hr[1] / hr[3]) / 30
    check('B6 the generator H = i log U is quasi-local: |H(x, x+r)| decays exponentially (range ~ 1/theta blocks)', rate > 0.05,
          f'|H| at r=0,10,20,40: {", ".join(f"{h:.1e}" for h in hr)}; decay {rate:.3f}/block')


# ---------------- C. entangled pair: conditional source, conservation, binding energy
def section_pair():
    print('C. entangled pair (0, 2k)+(2k, 0), N 32, theta 0.2: conditional source of relay 1')
    N = 32; B = Bands(N, TH); C, S = mats(N, TH); U = S @ C; CC = lambda A: C @ A @ C.T
    a, ia = B.mode(0.0); b, ib = B.mode(2 * 2 * np.pi / N); Psi = (np.outer(a, b) + np.outer(b, a)) / np.sqrt(2)
    T, W = B.canon(Psi.reshape(N, 2, N, 2)); mix = 0.5 * (B.f[:, ia, 0] + B.f[:, ib, 0]); mean = (T * W).sum((1, 2))
    check('C1 Born mean of the conditional source = reduced-state (branch mixture) value, all four components', abs(mean - mix).max() < 1e-12,
          f'mean {np.round(mean, 4)}; CL-7 gave Txx 0.0512 vs eps v^2 mixture 0.1711')
    check('C2 per configuration the conditional source spreads between the branch values', T[0].min() >= B.E[ia, 0] - 1e-12 and T[0].max() <= B.E[ib, 0] + 1e-12 and np.ptp(T[0]) > 0.05,
          f'T00 range [{T[0].min():.4f}, {T[0].max():.4f}], branches {B.E[ia, 0]:.4f}, {B.E[ib, 0]:.4f}')
    M, Tt = 4000, 150; x1, d1, x2, d2 = sample(odds(Psi, N), M); E1 = np.zeros((Tt + 1, M)); P1 = np.zeros((Tt + 1, M)); exdev = 0
    for t in range(Tt + 1):
        T, W = B.canon(Psi.reshape(N, 2, N, 2)); E1[t] = T[0][x2, d2]; P1[t] = T[1][x2, d2]
        exdev = max(exdev, abs((T * W).sum((1, 2)) - mix).max())
        if t == Tt: break
        P0 = odds(Psi, N); Pc = odds(CC(Psi), N); d1, d2 = flow_sample(P0, Pc, x1, d1, x2, d2)
        x1 = (x1 + 1 - 2 * d1) % N; x2 = (x2 + 1 - 2 * d2) % N; Psi = U @ Psi @ U.T
    dE = np.diff(E1, axis=0); dP = np.diff(P1, axis=0); jump = abs(dE) > 1e-9; se = E1.std() / np.sqrt(M)
    check('C3 per tick the conditional energy is NOT conserved: it jumps when the other relay switches direction',
          jump.mean() > 0.01, f'jump fraction {jump.mean():.3f}/tick, rms jump {np.sqrt((dE[jump] ** 2).mean()):.4f}, max {abs(dE).max():.4f}; momentum rms {np.sqrt((dP ** 2).mean()):.4f}')
    check('C4 the jumps average to zero: exact Born mean constant every tick; sampled mean within error',
          exdev < 1e-12 and abs(E1.mean(1) - mix[0]).max() < 5 * se and abs(dE.mean()) < 5 * dE.std() / np.sqrt(dE.size),
          f'exact dev {exdev:.1e}; sampled max dev {abs(E1.mean(1) - mix[0]).max():.4f} (5 se {5 * se:.4f}); mean jump {dE.mean():.1e}')
    v = [((E1[t] - E1[0]) ** 2).mean() for t in (10, 50, 150)]
    check('C5 no secular drift: variance of E1(t)-E1(0) saturates below (branch gap)^2', max(v) < (B.E[ib, 0] - B.E[ia, 0]) ** 2,
          f'var at t=10,50,150: {v[0]:.4f}, {v[1]:.4f}, {v[2]:.4f}; gap^2 {(B.E[ib, 0] - B.E[ia, 0]) ** 2:.4f}')
    # binding energy: continuous-time two-particle ring, hopping 1, contact U0 = -3
    n, U0 = 24, -3.0; h = -(np.eye(n, k=1) + np.eye(n, k=-1)); h[0, -1] = h[-1, 0] = -1
    I = np.eye(n); Vd = U0 * np.eye(n).ravel(); Ht = np.kron(h, I) + np.kron(I, h) + np.diag(Vd); w, X = np.linalg.eigh(Ht)
    g = X[:, 0]; Ekin = g @ (np.kron(h, I) + np.kron(I, h)) @ g; Vm = g @ (Vd * g)
    check('C6 a free per-subsystem stress misses the binding energy: bound pair E = <H1>+<H2>+<V>', abs(w[0] - Ekin - Vm) < 1e-10 and abs(Vm / w[0]) > 0.3,
          f'E {w[0]:.4f}, free parts {Ekin:.4f}, <V> {Vm:.4f} ({100 * Vm / w[0]:.0f}% of E)')
    xg = np.arange(n); pk = lambda x0, k0: np.exp(-(xg - x0) ** 2 / 8 + 1j * k0 * xg)
    psi0 = np.kron(pk(6, np.pi / 2), pk(18, -np.pi / 2)); psi0 /= np.linalg.norm(psi0); cf = X.conj().T @ psi0; fr, sp = [], []
    for tt in np.linspace(0, 12, 25):
        ps = (X @ (np.exp(-1j * w * tt) * cf)).reshape(n, n); fr.append(np.vdot(ps, h @ ps).real + np.vdot(ps, ps @ h.T).real)
        p2 = abs(ps) ** 2
        e1 = np.einsum('ab,ac,cb->b', ps.conj(), h, ps).real + 0.5 * U0 * np.diag(p2)   # relay 1 given x2 = b (weight sum_a |ps|^2)
        e2 = np.einsum('ab,bc,ac->a', ps.conj(), h, ps).real + 0.5 * U0 * np.diag(p2)
        sp.append(e1.sum() + e2.sum())
    E0 = np.vdot(psi0, Ht @ psi0).real
    check('C7 scattering: free subsystem energies change; with V split half to each relay the Born-mean source is conserved',
          np.ptp(fr) > 0.1 and abs(np.array(sp) - E0).max() < 1e-10, f'free sum range {np.ptp(fr):.3f}; split mean dev {abs(np.array(sp) - E0).max():.1e}')


# ---------------- D. remote setting
def section_signal():
    print("D. A (two blocks) entangled with B; A's setting z (none) or x (Hadamard); B's conditional source")
    N = 32; B = Bands(N, TH); k = 2 * 2 * np.pi / N; Hd = np.array([[1, 1], [1, -1]]) / np.sqrt(2); out = {}
    for lab in ('mom', 'pos'):
        p, q = B.mode(k)[0], B.mode(-k)[0]
        if lab == 'pos':
            Bp = Bands(64, TH); p, q = band_packet(Bp, TH, 0.0, 16, 3.0), band_packet(Bp, TH, 0.0, 48, 3.0); BB, NN = Bp, 64
        else: BB, NN = B, N
        Psi = np.stack([p, q]) / np.sqrt(2)
        for s, Op in (('z', np.eye(2)), ('x', Hd)):
            Ps = Op @ Psi; pa = (abs(Ps) ** 2).sum(1); T, _ = BB.canon(Ps.T.reshape(NN, 2, 2))
            Pb = (abs(Ps) ** 2).reshape(2, NN, 2).sum(2) / pa[:, None]; dip = (Pb * (np.arange(NN) - NN / 2)).sum(1)
            out[lab, s] = (pa, T, dip, (abs(Ps) ** 2).sum(0))
    for lab, comp, name in (('mom', 1, 'momentum Tx0'), ('pos', None, 'mass dipole')):
        st = {}
        for s in 'zx':
            pa, T, dip, mg = out[lab, s]; val = T[comp] if comp is not None else dip; st[s] = ((pa * val).sum(), (pa * val ** 2).sum() - (pa * val).sum() ** 2)
        same = abs(out[lab, 'z'][3] - out[lab, 'x'][3]).max() < 1e-15
        check(f'D{1 if lab == "mom" else 2} {name}: Born mean independent of A setting, distribution not (B marginal odds identical)',
              same and abs(st['z'][0] - st['x'][0]) < 1e-12 and st['z'][1] - st['x'][1] > 0.01,
              f"mean z {st['z'][0]:.2e} x {st['x'][0]:.2e}; variance z {st['z'][1]:.4f} x {st['x'][1]:.1e}")
    G, hb, c, mRb = 6.674e-11, 1.0546e-34, 2.998e8, 1.443e-25
    p = mRb * 0.01; dg = G * mRb * 0.54 / 1.0 ** 3
    print(f'   SI: Rb at 1 cm/s, momentum source per run +-{p:.1e} kg m/s vs 0 (mass-equivalent p/c {p / c:.1e} kg)')
    print(f'   Rb split 0.54 m, field at 1 m per run differs by G m d/r^3 = {dg:.1e} m/s^2 (gravimeters ~1e-9; 1e6 pairs x1e3)')
    print(f'   smallest measured gravitating source 9e-5 kg = {9e-5 / mRb:.0e} Rb masses')
    check('D3 the setting-dependent part is >= 20 orders below any measured gravitational source', p / c / 9e-5 < 1e-20 and dg * 1e3 / 1e-9 < 1e-20)


# ---------------- E. minimal switching only
def pcoin(p, th, nsp):
    c, s = np.cos(th), np.sin(th); Cc = np.array([[c, -1j * s], [-1j * s, c]])
    p = np.moveaxis(np.tensordot(Cc, p, axes=([1], [nsp + 1])), 0, nsp + 1)
    return np.moveaxis(np.tensordot(Cc, p, axes=([1], [nsp + 3])), 0, nsp + 3)


def ptr_engine(psi, nsp, ops, M):
    oddsf = lambda p: (abs(p) ** 2).sum(tuple(range(nsp))); P = oddsf(psi); Q = P.copy(); x1, d1, x2, d2 = sample(P, M); sw = 0
    for op in ops:
        P0 = oddsf(psi); pc = op(psi); Pc = oddsf(pc); Q, m = flow(Q, P0, Pc); sw += m; d1, d2 = flow_sample(P0, Pc, x1, d1, x2, d2)
        ax = nsp; sl = lambda dv: tuple([slice(None)] * (ax + 1) + [dv]); tmp = pc.copy()
        tmp[sl(0)] = np.roll(pc[sl(0)], 1, ax); tmp[sl(1)] = np.roll(pc[sl(1)], -1, ax)
        new = tmp.copy(); new[..., 0] = np.roll(tmp[..., 0], 1, -1); new[..., 1] = np.roll(tmp[..., 1], -1, -1)
        N = P.shape[0]; x1 = (x1 + 1 - 2 * d1) % N; x2 = (x2 + 1 - 2 * d2) % N; Q = shiftQ(Q); psi = new
    return Q, (x1, d1, x2, d2), oddsf(psi), sw


def Ry(t):
    return np.array([[np.cos(t / 2), -np.sin(t / 2)], [np.sin(t / 2), np.cos(t / 2)]])


def section_minimal():
    print('E. minimal switching only (no redraws)')
    N = 16; B = Bands(N, TH); C, S = mats(N, TH); U = S @ C; k0 = 2 * np.pi / N
    pk = lambda kk, x: band_packet(B, TH, kk, x, 1.5)
    Psi = np.outer(pk(k0, 4), pk(-k0, 12)) + np.outer(pk(-k0, 4), pk(k0, 12)); Psi /= np.linalg.norm(Psi)
    Q = odds(Psi, N).copy(); smp = sample(Q, 20000); dev = 0
    for _ in range(20):
        P0 = odds(Psi, N); Pc = odds(C @ Psi @ C.T, N); Q, _ = flow(Q, P0, Pc); x1, x2 = smp[0], smp[2]; d1, d2 = flow_sample(P0, Pc, *smp)
        smp = ((x1 + 1 - 2 * d1) % N, d1, (x2 + 1 - 2 * d2) % N, d2); Q = shiftQ(Q); Psi = U @ Psi @ U.T; dev = max(dev, 0.5 * abs(Q - odds(Psi, N)).sum())
    c2, nb = chi2(odds(Psi, N), *smp)
    check('E1 joint Born kept exactly (20 ticks, entangled packets); samples agree', dev < 1e-12 and c2 < 1.3, f'max TV {dev:.1e}; chi2/dof {c2:.3f} over {nb} bins')
    N, al2, M = 24, 0.3, 20000; psi = np.zeros((2, N, 2, N, 2), complex); psi[0, 8, 0, 8, 0] = np.sqrt(al2); psi[1, 8, 0, 8, 0] = np.sqrt(1 - al2)
    def couple(p): q = p.copy(); q[1] = p[1][:, ::-1][:, :, :, ::-1]; return q
    Q, (x1, d1, x2, d2), P, sw = ptr_engine(psi, 1, [couple] + [lambda p: pcoin(p, 0.15, 1)] * 6, M)
    u1, u2 = x1 > 8, x2 > 8; X = np.arange(N) > 8; dis = P[X][:, :, ~X].sum() + P[~X][:, :, X].sum()
    check('E2 two coined pointers: exact Born, reader disagreement = that of the odds, Born frequency',
          0.5 * abs(Q - P).sum() < 1e-12 and abs((u1 != u2).mean() - dis) < 4 * np.sqrt(dis / M) + 2e-4 and abs(u1.mean() - P[X].sum()) < 0.015,
          f'disagree relays {(u1 != u2).mean():.4f} odds {dis:.4f}; up {u1.mean():.4f} vs {P[X].sum():.4f}; switched mass {sw:.3f}')
    N, M = 26, 20000; Es, Er = {}, {}
    for a in (0.0, np.pi / 2):
        for b in (np.pi / 4, -np.pi / 4):
            psi = np.zeros((2, 2, N, 2, N, 2), complex); psi[0, 1, 12, 0, 12, 0] = 1 / np.sqrt(2); psi[1, 0, 12, 0, 12, 0] = -1 / np.sqrt(2)
            def meas(p, a=a, b=b):
                q = np.einsum('ij,jk...->ik...', Ry(a), p); q = np.einsum('ij,kj...->ki...', Ry(b), q)
                q[1] = q[1][:, :, ::-1].copy(); q[:, 1] = q[:, 1][:, :, :, :, ::-1].copy(); return q
            _, (x1, d1, x2, d2), P, _ = ptr_engine(psi, 2, [meas] + [lambda p: pcoin(p, 0.1, 2)] * 5, M)
            sg = np.where(np.arange(N) > 12, 1, -1); Es[a, b] = np.einsum('adbc,a,b->', P, sg, sg)
            Er[a, b] = (np.where(x1 > 12, 1, -1) * np.where(x2 > 12, 1, -1)).mean()
    f = lambda E: abs(E[0, np.pi / 4] + E[0, -np.pi / 4] + E[np.pi / 2, np.pi / 4] - E[np.pi / 2, -np.pi / 4])
    check('E3 singlet + coined pointers: relay readings violate CHSH like the odds', f(Er) > 2.5 and abs(f(Er) - f(Es)) < 0.06, f'S_odds {f(Es):.4f}, S_relays {f(Er):.3f}')
    N = 32; B = Bands(N, TH); C, S = mats(N, TH); a = B.mode(2 * np.pi / N)[0]; b = B.mode(-2 * np.pi / N)[0]
    sp = lambda p: np.clip((abs(p) ** 2 - abs(C @ p) ** 2), 0, None).sum()
    check('E4 a plane-wave relay never switches (straight null path); a standing wave switches', sp(a) < 1e-15 and sp((a + b) / np.sqrt(2)) > 1e-3,
          f'switch mass/tick plane {sp(a):.1e}, standing {sp((a + b) / np.sqrt(2)):.4f}')


# ---------------- F. single relay versus bound pair
def section_isolated():
    print('F. two-arm superposition (arms 20 blocks apart): one relay versus a bound pair (relative width 1)')
    L = 81; x = np.arange(L); arm = lambda c: np.exp(-(x - c) ** 2 / 8.0)
    one = arm(30) + arm(50); one /= np.linalg.norm(one); p1 = one ** 2
    check('F1 single elementary relay: conditional = full odds, source half in each arm (torque 0)', abs(p1[x < 40].sum() + p1[40] / 2 - 0.5) < 1e-12, f'left weight {p1[x < 40].sum():.6f}')
    X1, X2 = np.meshgrid(x, x, indexing='ij'); rel = np.exp(-(X1 - X2) ** 2 / 2.0); cm = (X1 + X2) / 2
    Psi = (np.exp(-(cm - 30) ** 2 / 8.0) + np.exp(-(cm - 50) ** 2 / 8.0)) * rel; P = Psi ** 2 / (Psi ** 2).sum()
    cond = P / P.sum(0, keepdims=True); left = (cond * (X1 < 40)).sum(0); act = np.where(x < 40, 1.0, 0.0)
    tq = (P.sum(0) * (2 * np.where(x < 40, left, 1 - left) - 1)).sum()
    check('F2 bound pair: relay 1 conditioned on relay 2 sits in relay 2\'s actual arm (torque ~1)', tq > 0.999, f'torque {tq:.6f}')
    G, hb = 6.674e-11, 1.0546e-34
    for lab, m, R in (('molecule 4e-23 kg, R 1 nm', 4.2e-23, 1e-9), ('BMV crystal 1e-14 kg, R 0.9 um', 1e-14, 9e-7)):
        print(f'   if the response acts back on the odds: arm-phase rate G m^2/(hbar R), {lab}: {G * m * m / (hb * R):.1e} rad/s')


if __name__ == '__main__':
    section_pg(); section_single(); section_pair(); section_signal(); section_minimal(); section_isolated()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
