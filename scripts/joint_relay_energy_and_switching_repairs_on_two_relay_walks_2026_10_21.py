#!/usr/bin/env python3
"""Supplied lossless 1D walks with two relays: tests of the proposed joint repairs CL-5' (conditional
relay energy) and CL-6' (joint switching plus fresh redraws from the conditional odds of a direction
given the other relays' blocks and directions). Checks, in supplied two-walker rings and few-qubit
pointer couplings: (A) whether the conditional energy is well defined (other relays' phase, arg(0),
range); (B) exact equivariance of the joint odds with fresh redraws, by update order; (C, D) reader
agreement and CHSH with redraws exercised; (E) the record source for product and entangled states;
(F) a toy with burns and finite block capacity. Supplied models; no physical identification.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/JOINT_RELAY_ENERGY_AND_SWITCHING_REPAIRS_ON_TWO_RELAY_WALKS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
def _timeout(*args):
    raise TimeoutError('Owning 300-second aggregate cap exceeded; streamed diagnostics retained')
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


# ---------------- single-walker tick U = S C on (x, d), flattened x*2+d; d=0 steps +1, d=1 steps -1
def mats(N, th):
    c, s = np.cos(th), np.sin(th)
    C = np.zeros((2 * N, 2 * N), complex); S = np.zeros((2 * N, 2 * N))
    for x in range(N):
        C[2 * x:2 * x + 2, 2 * x:2 * x + 2] = [[c, -1j * s], [-1j * s, c]]
        S[2 * ((x + 1) % N), 2 * x] = 1; S[2 * ((x - 1) % N) + 1, 2 * x + 1] = 1
    return C, S


def mode(N, th, k):
    """upper-band plane wave: returns (psi, frequency w, group velocity v = P(+) - P(-))."""
    Cc = np.array([[np.cos(th), -1j * np.sin(th)], [-1j * np.sin(th), np.cos(th)]])
    w, V = np.linalg.eig(np.diag([np.exp(-1j * k), np.exp(1j * k)]) @ Cc)
    j = int(np.argmax(-np.angle(w))); v = V[:, j] / np.linalg.norm(V[:, j])
    return np.outer(np.exp(1j * k * np.arange(N)), v).ravel() / np.sqrt(N), -np.angle(w[j]), abs(v[0]) ** 2 - abs(v[1]) ** 2


def band_packet(N, th, k0, x0, sig):
    ks = 2 * np.pi * np.fft.fftfreq(N); amp = np.zeros((N, 2), complex)
    for i, k in enumerate(ks):
        v = mode(N, th, k)[0].reshape(N, 2)[0] * np.sqrt(N); v = v * np.exp(-1j * np.angle(v[0]))
        dk = (k - k0 + np.pi) % (2 * np.pi) - np.pi
        amp[i] = v * np.exp(-dk ** 2 * sig ** 2 / 2 - 1j * k * x0)
    psi = np.fft.ifft(amp, axis=0) * N
    return (psi / np.linalg.norm(psi)).ravel()


class Ring:
    """two distinguishable walkers on an N-ring; joint amplitude Psi[(x1,d1),(x2,d2)]; tick Psi -> U Psi U^T."""
    def __init__(self, N, th=TH):
        self.N = N; self.C, self.S = mats(N, th); self.U = self.S @ self.C
        ev, V = np.linalg.eig(self.U); self.H = V @ np.diag(-np.angle(ev)) @ np.linalg.inv(V)

    def odds(self, Psi):
        return (abs(Psi) ** 2).reshape(self.N, 2, self.N, 2)

    def cond(self, num, wt, r):
        """odds-weighted conditional mean over relay r's own directions: r=1 -> (x1,x2,d2), r=2 -> (x1,d1,x2)."""
        N = self.N; ax = 1 if r == 1 else 3
        W = wt.reshape(N, 2, N, 2).sum(ax); X = (wt * num).reshape(N, 2, N, 2).sum(ax)
        return np.where(W > 0, X / np.where(W > 0, W, 1), np.nan), W

    def energy(self, old, new, kind, r=1):
        """CL-5' readings of relay r's energy for the tick old -> new."""
        if kind == 'literal':      # phase advance of the joint amplitude, weighted by odds after
            return self.cond(-np.angle(new * old.conj()), abs(new) ** 2, r)
        if kind == 'own':          # phase advance relative to old with the OTHER relays' part of the tick applied
            ref = old @ self.U.T if r == 1 else self.U @ old
            return self.cond(-np.angle(new * ref.conj()), abs(new) * abs(ref), r)
        Hn = self.H @ new if r == 1 else new @ self.H.T   # generator local energy, H = i log U (principal branch)
        return self.cond((new.conj() * Hn).real / np.maximum(abs(new) ** 2, 1e-300), abs(new) ** 2, r)


# ---------------- relay machinery on joint odds Q[x1,d1,x2,d2] (exact occupation) and samples
def flow(Q, P, Pn):
    """CL-6 minimal joint switching flow (exact image) + relay-1 and relay-2 turn masses."""
    N1, N2 = P.shape[0], P.shape[2]
    t = lambda A: A.transpose(0, 2, 1, 3).reshape(N1 * N2, 4)
    q, p, pn = t(Q), t(P), t(Pn)
    ex = np.clip(p - pn, 0, None); sh = np.clip(pn - p, 0, None); Ssh = sh.sum(1, keepdims=True)
    go = np.where(p > 0, ex / np.where(p > 0, p, 1), 0.0); out = q * go
    to = np.where(Ssh > 0, sh / np.where(Ssh > 0, Ssh, 1), 0)
    turns = [sum((out[:, a] * to[:, b]).sum() for a in range(4) for b in range(4) if (a >> s) & 1 != (b >> s) & 1) for s in (1, 0)]
    qn = q - out + out.sum(1, keepdims=True) * to
    return qn.reshape(N1, N2, 2, 2).transpose(0, 2, 1, 3), turns


def flow_sample(P, Pn, x1, d1, x2, d2):
    N2 = P.shape[2]
    t = lambda A: A.transpose(0, 2, 1, 3).reshape(-1, 4)
    p, pn = t(P), t(Pn); ex = np.clip(p - pn, 0, None); sh = np.clip(pn - p, 0, None)
    blk = x1 * N2 + x2; d = 2 * d1 + d2; pr = p[blk, d]
    sw = (rng.random(len(d)) < np.where(pr > 0, ex[blk, d] / np.where(pr > 0, pr, 1), 0)) & (sh[blk].sum(1) > 0)
    if sw.any():
        cs = np.cumsum(sh[blk[sw]], 1); cs /= cs[:, -1:]
        d = d.copy(); d[sw] = np.minimum((rng.random(sw.sum())[:, None] > cs).sum(1), 3)
    return d // 2, d % 2


def shiftQ(Q):
    Q = Q.copy()
    Q[:, 0] = np.roll(Q[:, 0], 1, 0); Q[:, 1] = np.roll(Q[:, 1], -1, 0)
    Q[:, :, :, 0] = np.roll(Q[:, :, :, 0], 1, 2); Q[:, :, :, 1] = np.roll(Q[:, :, :, 1], -1, 2)
    return Q


def conds(Pn):
    W1 = Pn.sum(1); W2 = Pn.sum(3)
    c1 = Pn / np.where(W1 > 0, W1, 1)[:, None]; c2 = Pn / np.where(W2 > 0, W2, 1)[..., None]
    m1 = Pn.sum((2, 3)); m1 = m1 / np.where(m1.sum(1, keepdims=True) > 0, m1.sum(1, keepdims=True), 1)
    m2 = Pn.sum((0, 1)); m2 = m2 / np.where(m2.sum(1, keepdims=True) > 0, m2.sum(1, keepdims=True), 1)
    return c1, c2, m1, m2


def redraw(Q, Pn, r1, r2, order):
    """fresh redraws on the exact occupation. r1[x1,x2,d2], r2[x1,d1,x2] in [0,1] (independent of own direction).
    order: 'seq' (relay 1 then 2), 'sim' (both from the pre-redraw configuration), 'marg' (own block's odds)."""
    c1, c2, m1, m2 = conds(Pn); R1 = r1[:, None]; R2 = r2[..., None]
    if order == 'seq':
        Q = (1 - R1) * Q + R1 * Q.sum(1, keepdims=True) * c1
        return (1 - R2) * Q + R2 * Q.sum(3, keepdims=True) * c2
    if order == 'marg':
        Q = (1 - R1) * Q + R1 * Q.sum(1, keepdims=True) * m1[:, :, None, None]
        return (1 - R2) * Q + R2 * Q.sum(3, keepdims=True) * m2[None, None]
    I = np.eye(2)
    K1 = (1 - r1)[..., None, None] * I + r1[..., None, None] * c1.transpose(0, 2, 3, 1)[:, :, :, None, :]
    K2 = (1 - r2)[..., None, None] * I + r2[..., None, None] * c2[:, :, :, None, :]
    return np.einsum('adbc,abcde,adbcf->aebf', Q, K1, K2)


def redraw_sample(Pn, r1, r2, x1, d1, x2, d2):
    c1, c2, _, _ = conds(Pn)
    h = rng.random(len(x1)) < r1[x1, x2, d2]
    d1 = np.where(h, (rng.random(len(x1)) > c1[x1, 0, x2, d2]).astype(int), d1)
    h = rng.random(len(x1)) < r2[x1, d1, x2]
    d2 = np.where(h, (rng.random(len(x1)) > c2[x1, d1, x2, 0]).astype(int), d2)
    return d1, d2


def sample(P, M):
    N2 = P.shape[2]; idx = rng.choice(P.size, M, p=(P / P.sum()).ravel())
    x1, rem = np.divmod(idx, 2 * N2 * 2); d1, rem = np.divmod(rem, N2 * 2); x2, d2 = np.divmod(rem, 2)
    return x1, d1, x2, d2


def chi2(P, x1, d1, x2, d2):
    M = len(x1); h = np.bincount(((x1 * 2 + d1) * P.shape[2] + x2) * 2 + d2, minlength=P.size)
    e = M * P.ravel(); k = e >= 5
    return ((h[k] - e[k]) ** 2 / e[k]).sum() / max(k.sum() - 1, 1), k.sum()


def rates(R, old, new, kind='own'):
    e1, _ = R.energy(old, new, kind, 1); e2, _ = R.energy(old, new, kind, 2)
    return np.clip(2 * np.nan_to_num(e1), 0, 1), np.clip(2 * np.nan_to_num(e2), 0, 1), e1, e2


# ---------------- A. is the conditional energy well defined?
def section_energy():
    print("A. CL-5' conditional energy: other relays' phase, arg(0), range")
    R = Ring(32); k = 2 * np.pi / 32
    (a, wa, va), (b, wb, vb) = mode(32, TH, 0.0), mode(32, TH, 2 * k)
    Psi = np.outer(a, b); new = R.U @ Psi @ R.U.T
    el, _ = R.energy(Psi, new, 'literal'); eo, _ = R.energy(Psi, new, 'own')
    check("A1 FAILURE of literal CL-5': for a product of modes, relay 1's energy is w1 + w2 (counts relay 2's phase)",
          abs(np.nanmax(abs(el - (wa + wb)))) < 1e-12, f'w1={wa:.4f}, w2={wb:.4f}, literal={np.nanmean(el):.4f}')
    check("A2 repair 'own part of the tick' gives w1 exactly", np.nanmax(abs(eo - wa)) < 1e-12, f'{np.nanmean(eo):.6f}')
    # arg(0): localized start; the coin-shift walk alternates sublattices, so same-block overlap is zero
    N = 40; C, S = mats(N, TH); U = S @ C; p = np.zeros(2 * N, complex); p[40] = 1 / np.sqrt(2); p[41] = 1j / np.sqrt(2)
    und = []
    for t in range(20):
        q = U @ p; und.append((abs(q) ** 2)[abs(p) < 1e-14].sum()); p = q
    check('A3 FAILURE: from a one-site start, the odds weight with zero same-block amplitude before the tick is 1 at every tick',
          min(und) > 1 - 1e-12, f'min over 20 ticks {min(und):.15f}; np.angle(0)=0 then gives energy 0 and no redraws')
    p0 = np.zeros(2 * N, complex); p0[40] = 1 / np.sqrt(2); p0[41] = 1j / np.sqrt(2); ev, V = np.linalg.eig(U)
    Hs = V @ np.diag(-np.angle(ev)) @ np.linalg.inv(V); p = p0
    for _ in range(9): p = U @ p
    g = (p.conj() * (Hs @ p)).real.reshape(N, 2).sum(1)
    check('A4 generator local energy (H = i log U) is defined wherever odds > 0; here it is 0 to rounding', abs(g).max() < 1e-12, f'max |local energy| {abs(g).max():.1e}')
    pk = band_packet(N, TH, 0.3, 20, 3.0); q = U @ pk; Pn = abs(q) ** 2
    e = (Pn * -np.angle(q * pk.conj())).reshape(N, 2).sum(1) / Pn.reshape(N, 2).sum(1); pb = Pn.reshape(N, 2).sum(1)
    check('A5 FAILURE: an upper-band packet has negative same-block energy in its tails (probability 2*eps < 0)', pb[e < 0].sum() > 1e-3,
          f'weight with eps<0: {pb[e < 0].sum():.4f}, min eps {e.min():.3f}')
    # entangled stationary state with branch energies 0.2 and 0.438: conditional energy spreads past 1/2
    Ent = (np.outer(a, b) + np.outer(b, a)) / np.sqrt(2); new = R.U @ Ent @ R.U.T; eo, W = R.energy(Ent, new, 'own')
    eg, _ = R.energy(Ent, new, 'gen'); over = W[eo > 0.5].sum()
    check("A6 FAILURE of CL-6's domain: entangled state, repaired conditional energy exceeds 1/2 on some configurations",
          over > 0, f'own: range [{np.nanmin(eo):.4f},{np.nanmax(eo):.4f}], weight>1/2 {over:.4f}; generator [{np.nanmin(eg):.4f},{np.nanmax(eg):.4f}]')


# ---------------- B. equivariance with fresh redraws
def run_ring(R, Psi, T, order, M=0, kind='own'):
    P = R.odds(Psi); Q = P.copy(); smp = sample(P, M) if M else None; dev = 0.0
    for _ in range(T):
        P0 = R.odds(Psi); Pc_ = R.C @ Psi @ R.C.T; Pc = R.odds(Pc_); Q, _ = flow(Q, P0, Pc)
        new = R.S @ Pc_ @ R.S.T; Pn = R.odds(new); Q = shiftQ(Q)
        r1, r2, _, _ = rates(R, Psi, new, kind); Q = redraw(Q, Pn, r1, r2, order)
        if M:
            x1, d1, x2, d2 = smp; d1, d2 = flow_sample(P0, Pc, x1, d1, x2, d2)
            x1 = (x1 + 1 - 2 * d1) % R.N; x2 = (x2 + 1 - 2 * d2) % R.N
            d1, d2 = redraw_sample(Pn, r1, r2, x1, d1, x2, d2); smp = (x1, d1, x2, d2)
        Psi = new; dev = max(dev, 0.5 * abs(Q - Pn).sum())
    return Psi, Q, smp, dev


def section_equivariance():
    print('B. CL-6 with fresh redraws: is the relay distribution kept exactly at the joint odds?')
    R = Ring(16); k0 = 2 * np.pi / 16
    Psi = (np.outer(band_packet(16, TH, k0, 4, 1.5), band_packet(16, TH, -k0, 12, 1.5)) +
           np.outer(band_packet(16, TH, -k0, 4, 1.5), band_packet(16, TH, k0, 12, 1.5))); Psi /= np.linalg.norm(Psi)
    out = {o: run_ring(R, Psi.copy(), 20, o) for o in ('seq', 'sim', 'marg')}
    rmax = rates(R, Psi, R.U @ Psi @ R.U.T)[0].max()
    check('B1 sequential redraws (each a draw from the conditional odds): joint occupation = joint odds for 20 ticks',
          out['seq'][3] < 1e-12, f'max TV {out["seq"][3]:.1e}; redraw rate up to {rmax:.2f}/tick')
    check('B2 FAILURE of simultaneous redraws (both relays from the pre-redraw configuration)', out['sim'][3] > 1e-4, f'max TV {out["sim"][3]:.2e}')
    check("B3 FAILURE of own-block-marginal redraws (CL-6 as written): joint odds lost", out['marg'][3] > 1e-3, f'max TV {out["marg"][3]:.2e}')
    Rb = Ring(32); k = 2 * np.pi / 32; a, b = mode(32, TH, 0.0)[0], mode(32, TH, 2 * k)[0]
    Ent = (np.outer(a, b) + np.outer(b, a)) / np.sqrt(2)
    dv = {o: run_ring(Rb, Ent.copy(), 10, o)[3] for o in ('seq', 'sim', 'marg')}
    check('B4 stationary entangled state (branch energies 0.200, 0.438): seq exact, sim and marg not',
          dv['seq'] < 1e-12 and dv['sim'] > 1e-4 and dv['marg'] > 1e-3, f"TV seq {dv['seq']:.1e}, sim {dv['sim']:.2e}, marg {dv['marg']:.2e}")
    Pf, Q, smp, _ = run_ring(R, Psi.copy(), 20, 'seq', M=20000)
    c, nb = chi2(R.odds(Pf), *smp)
    check('B5 sampled relay pairs match the joint odds after 20 ticks (chi2/dof)', c < 1.3, f'chi2/dof={c:.3f} over {nb} bins')


# ---------------- C, D. pointers with a coin after coupling, so redraws act; forced rate 0.4 (any direction-independent rate)
def ptr_engine(psi, nsp, ops, M, order, rate=0.4):
    oddsf = lambda p: (abs(p) ** 2).sum(tuple(range(nsp)))
    P = oddsf(psi); Q = P.copy(); x1, d1, x2, d2 = sample(P, M)
    for op in ops:
        P0 = oddsf(psi); pc = op(psi); Pc = oddsf(pc); Q, _ = flow(Q, P0, Pc); d1, d2 = flow_sample(P0, Pc, x1, d1, x2, d2)
        new = pc.copy(); ax1, ax2 = nsp, nsp + 2
        sl = lambda ax, dv: tuple([slice(None)] * (ax + 1) + [dv])
        tmp = new.copy()
        tmp[sl(ax1, 0)] = np.roll(new[sl(ax1, 0)], 1, ax1); tmp[sl(ax1, 1)] = np.roll(new[sl(ax1, 1)], -1, ax1)
        new = tmp.copy(); new[..., 0] = np.roll(tmp[..., 0], 1, -1); new[..., 1] = np.roll(tmp[..., 1], -1, -1)
        N = P.shape[0]; x1 = (x1 + 1 - 2 * d1) % N; x2 = (x2 + 1 - 2 * d2) % N; Q = shiftQ(Q)
        Pn = oddsf(new); r1 = np.full((N, N, 2), rate); r2 = np.full((N, 2, N), rate)
        Q = redraw(Q, Pn, r1, r2, order)
        if order == 'seq': d1, d2 = redraw_sample(Pn, r1, r2, x1, d1, x2, d2)
        else:
            _, _, m1, m2 = conds(Pn)
            h = rng.random(M) < rate; d1 = np.where(h, (rng.random(M) > m1[x1, 0]).astype(int), d1)
            h = rng.random(M) < rate; d2 = np.where(h, (rng.random(M) > m2[x2, 0]).astype(int), d2)
        psi = new
    return psi, Q, (x1, d1, x2, d2), oddsf(psi)


def pcoin(p, th, nsp):
    c, s = np.cos(th), np.sin(th); Cc = np.array([[c, -1j * s], [-1j * s, c]])
    p = np.moveaxis(np.tensordot(Cc, p, axes=([1], [nsp + 1])), 0, nsp + 1)
    return np.moveaxis(np.tensordot(Cc, p, axes=([1], [nsp + 3])), 0, nsp + 3)


def section_readers():
    print('C. two pointers read one spin; pointers carry a coin (theta 0.15) so redraws change directions')
    N, al2, M = 24, 0.3, 20000
    psi = np.zeros((2, N, 2, N, 2), complex); psi[0, 8, 0, 8, 0] = np.sqrt(al2); psi[1, 8, 0, 8, 0] = np.sqrt(1 - al2)
    def couple(p): q = p.copy(); q[1] = p[1][:, ::-1][:, :, :, ::-1]; return q
    ops = [couple] + [lambda p: pcoin(p, 0.15, 1)] * 6
    for order in ('seq', 'marg'):
        _, Q, (x1, d1, x2, d2), P = ptr_engine(psi.copy(), 1, ops, M, order)
        u1, u2 = x1 > 8, x2 > 8; X = np.arange(N) > 8
        dis_ex = P[X][:, :, ~X].sum() + P[~X][:, :, X].sum(); tv = 0.5 * abs(Q - P).sum()
        if order == 'seq':
            check('C1 seq redraws: exact occupation = odds through coupling + 6 coined ticks', tv < 1e-12, f'TV {tv:.1e}')
            check('C2 reader disagreement equals that of the odds (coin only)', abs((u1 != u2).mean() - dis_ex) < 4 * np.sqrt(dis_ex / M) + 2e-4,
                  f'relays {(u1 != u2).mean():.4f}, odds {dis_ex:.4f}, Born up {u1.mean():.4f} vs odds {P[X].sum():.4f}')
        else:
            check('C3 FAILURE of own-block-marginal redraws: reader disagreement and occupation leave the odds',
                  abs((u1 != u2).mean() - dis_ex) > 8 * np.sqrt(dis_ex / M) and tv > 1e-3, f'relays {(u1 != u2).mean():.4f} vs odds {dis_ex:.4f}, TV {tv:.2e}')


def Ry(t):
    return np.array([[np.cos(t / 2), -np.sin(t / 2)], [np.sin(t / 2), np.cos(t / 2)]])


def section_chsh():
    print('D. singlet with coined pointers and redraws: CHSH')
    N, M = 26, 20000; Es, Er = {}, {}
    for a in (0.0, np.pi / 2):
        for b in (np.pi / 4, -np.pi / 4):
            psi = np.zeros((2, 2, N, 2, N, 2), complex); psi[0, 1, 12, 0, 12, 0] = 1 / np.sqrt(2); psi[1, 0, 12, 0, 12, 0] = -1 / np.sqrt(2)
            def meas(p, a=a, b=b):
                q = np.einsum('ij,jk...->ik...', Ry(a), p); q = np.einsum('ij,kj...->ki...', Ry(b), q)
                q[1] = q[1][:, :, ::-1].copy(); q[:, 1] = q[:, 1][:, :, :, :, ::-1].copy(); return q
            _, Q, (x1, d1, x2, d2), P = ptr_engine(psi, 2, [meas] + [lambda p: pcoin(p, 0.1, 2)] * 5, M, 'seq')
            sg = np.where(np.arange(N) > 12, 1, -1); Es[a, b] = np.einsum('adbc,a,b->', P, sg, sg)
            Er[a, b] = (np.where(x1 > 12, 1, -1) * np.where(x2 > 12, 1, -1)).mean()
    f = lambda E: abs(E[0, np.pi / 4] + E[0, -np.pi / 4] + E[np.pi / 2, np.pi / 4] - E[np.pi / 2, -np.pi / 4])
    check('D1 odds of the pointer readings violate CHSH', f(Es) > 2.5, f'S_odds={f(Es):.4f}')
    check('D2 relay readings with redraws reproduce it', abs(f(Er) - f(Es)) < 0.06 and f(Er) > 2.5, f'S_relays={f(Er):.3f}')


# ---------------- E. record source: eps (1,d)(1,d) per tick, turn d->d' deposits -1 (1D chord, -1/4 * 4)
def source(R, Psi, kind):
    P = R.odds(Psi); new = R.U @ Psi @ R.U.T; Pn = R.odds(new); e1, W = R.energy(Psi, new, kind, 1)
    r1, r2, _, _ = rates(R, Psi, new, kind); c1 = conds(Pn)[0]
    Tt = np.nansum(e1 * Pn.sum(1)); Tx = np.nansum(e1[:, None] * Pn * np.array([1, -1])[None, :, None, None])
    _, (tsw, _) = flow(P, P, R.odds(R.C @ Psi @ R.C.T)); trd = (r1 * Pn.sum(1) * 2 * c1[:, 0] * c1[:, 1]).sum()
    return np.array([Tt, Tx, Tt - tsw - trd]), tsw, trd


def section_source():
    print('E. record source per relay per tick (tt, tx, xx) versus eps u u')
    R = Ring(32); k = 2 * np.pi / 32; M0, M2 = mode(32, TH, 0.0), mode(32, TH, 2 * k); Mk = mode(32, TH, k)
    for lab, A, B in (('k (x) 2k', Mk, M2), ('0 (x) 2k', M0, M2)):
        T, tsw, trd = source(R, np.outer(A[0], B[0]), 'own'); tgt = A[1] * np.array([1, A[2], A[2] ** 2])
        check(f'E1 product {lab}: repaired rules give eps u u for relay 1', abs(T - tgt).max() < 1e-12, f'T={np.round(T, 5)}, target {np.round(tgt, 5)}, switch turns {tsw:.1e}')
    Tl, _, _ = source(R, np.outer(Mk[0], M2[0]), 'literal')
    check("E2 FAILURE of literal CL-5' for a product: T_tt = w1 + w2", abs(Tl[0] - Mk[1] - M2[1]) < 1e-12, f'T={np.round(Tl, 5)}')
    Ent = (np.outer(M0[0], M2[0]) + np.outer(M2[0], M0[0])) / np.sqrt(2)
    mix = 0.5 * sum(m[1] * np.array([1, m[2], m[2] ** 2]) for m in (M0, M2))
    To, tsw, trd = source(R, Ent, 'own'); Tg, _, _ = source(R, Ent, 'gen')
    check('E3 entangled (0,2k)+(2k,0): T_tt is the mean energy (generator reading exact; own-part reading close)', abs(Tg[0] - mix[0]) < 1e-12,
          f'gen {Tg[0]:.5f}, own {To[0]:.5f}, reduced-state value {mix[0]:.5f}')
    check('E4 entangled: T_tx and T_xx are NOT the reduced-state (branch-mixture) values', abs(To[1] - mix[1]) > 0.02 and abs(To[2] - mix[2]) > 0.05,
          f'own T={np.round(To, 4)}, gen T={np.round(Tg, 4)}, mixture {np.round(mix, 4)}; turns switch {tsw:.4f} redraw {trd:.4f}')
    # remote operation on walker 2 during one tick: walker 1's reduced odds unchanged, relay-1 turn mass changes
    out = []
    for th2 in (TH, TH + 0.6):
        C2, _ = mats(32, th2); Pc = R.odds(R.C @ Ent @ C2.T); _, (t1, _) = flow(R.odds(Ent), R.odds(Ent), Pc)
        out.append((t1, Pc.sum((2, 3))))
    check('E5 FAILURE (signalling of the turn source): relay-1 switching turns depend on walker 2\'s coin, its own odds do not',
          abs(out[0][0] - out[1][0]) > 1e-3 and abs(out[0][1] - out[1][1]).max() < 1e-12,
          f'turns {out[0][0]:.4f} vs {out[1][0]:.4f}; own-odds diff {abs(out[0][1] - out[1][1]).max():.1e}')


def burn_ring(n, L, T, M, two=False):
    """stationary odds on an L-ring of blocks; each relay's step burns one site of the block it enters;
    a used-up target makes the relay take the other direction (1D: the only one left); none left = stuck."""
    R = Ring(L); k = 2 * np.pi / L; a, wa, va = mode(L, TH, k); b = mode(L, TH, -k)[0]
    Psi = (np.outer(a, b) + np.outer(b, a)) / np.sqrt(2) if two else np.outer(a, a)
    P = R.odds(Psi); Pc = R.odds(R.C @ Psi @ R.C.T); new = R.U @ Psi @ R.U.T; r1, r2, _, _ = rates(R, Psi, new, 'own')
    x1, d1, x2, d2 = sample(P, M); vis = np.zeros((M, L), int); ar = np.arange(M)
    np.add.at(vis, (ar, x1), 1)
    if two: np.add.at(vis, (ar, x2), 1)
    first = np.full(M, -1); stuck = np.zeros(M, bool); chis = {}
    for t in range(T):
        d1, d2 = flow_sample(P, Pc, x1, d1, x2, d2)
        for r in ((1, 2) if two else (1,)):
            x, d = (x1, d1) if r == 1 else (x2, d2)
            tgt = (x + 1 - 2 * d) % L; full = vis[ar, tgt] >= n
            alt = (x - 1 + 2 * d) % L; can = full & (vis[ar, alt] < n); st = full & ~can
            d = np.where(can, 1 - d, d); tgt = np.where(st, x, (x + 1 - 2 * d) % L)
            first = np.where((full) & (first < 0), t, first); stuck |= st
            np.add.at(vis, (ar[~st], tgt[~st]), 1)
            if r == 1: x1, d1 = tgt, d
            else: x2, d2 = tgt, d
        if not two: x2, d2 = x1, d1  # placeholder; single relay uses its marginal below
        d1, d2 = redraw_sample(P, r1, r2, x1, d1, x2, d2) if two else (redraw_sample(P, r1, r2, x1, d1, x1, d1)[0], d1)
        if t + 1 in (T // 2, T):
            if two: chis[t + 1] = chi2(P, x1, d1, x2, d2)[0]
            else:
                P1 = P.sum((2, 3)); h = np.bincount(x1 * 2 + d1, minlength=2 * L); e = M * P1.ravel()
                chis[t + 1] = ((h - e) ** 2 / e).sum() / (2 * L - 1)
    return first, stuck, chis



def burn_single(psi, C, S, n, T, M, ring=True):
    """one relay; odds evolve unconditioned; switching + CL-4 capacity + redraws at 2*eps (same-block CL-5,
    clipped to [0,1]). A used-up target block makes the relay take the other direction (1D: the only one
    left); none left = stuck (stays; CL-4 gives no rule). Returns per-tick realised mean step / odds current."""
    L = len(psi) // 2; U = S @ C; P = (abs(psi) ** 2).reshape(L, 2)
    idx = rng.choice(2 * L, M, p=P.ravel() / P.sum()); x, d = idx // 2, idx % 2
    vis = np.zeros((M, L), np.int32); ar = np.arange(M); vis[ar, x] = 1
    first = np.full(M, -1); stuck = np.zeros(M, bool); ratio = []
    for t in range(T):
        P = (abs(psi) ** 2).reshape(L, 2); pc = C @ psi; Pc = (abs(pc) ** 2).reshape(L, 2)
        ex = np.clip(P - Pc, 0, None); sh = np.clip(Pc - P, 0, None); Ssh = sh.sum(1)
        pr = P[x, d]; sw = (rng.random(M) < np.where(pr > 0, ex[x, d] / np.where(pr > 0, pr, 1), 0)) & (Ssh[x] > 0)
        d = np.where(sw, (rng.random(M) > sh[x, 0] / np.where(Ssh[x] > 0, Ssh[x], 1)).astype(int), d)
        tgt = x + 1 - 2 * d; alt = x - 1 + 2 * d
        if ring: tgt, alt = tgt % L, alt % L
        else: tgt, alt = np.clip(tgt, 0, L - 1), np.clip(alt, 0, L - 1)
        full = vis[ar, tgt] >= n; can = full & (vis[ar, alt] < n); st = full & ~can
        first = np.where(full & (first < 0), t, first); stuck |= st
        d = np.where(can, 1 - d, d); nx = np.where(st, x, x + 1 - 2 * d); nx = nx % L if ring else nx
        step = nx - x; step = (step + 1) % L - 1 if ring else step
        vis[ar[~st], nx[~st]] += 1; x = nx
        J = (Pc[:, 0] - Pc[:, 1]).sum(); ratio.append(step.mean() / J if abs(J) > 1e-9 else np.nan)
        new = S @ pc; Pn = (abs(new) ** 2).reshape(L, 2); W = Pn.sum(1)
        e = (Pn * -np.angle(new * psi.conj()).reshape(L, 2)).sum(1) / np.where(W > 0, W, 1)
        r = np.clip(2 * e, 0, 1); h = rng.random(M) < r[x]
        d = np.where(h, (rng.random(M) > Pn[x, 0] / np.where(W[x] > 0, W[x], 1)).astype(int), d); psi = new
    return first, stuck, np.array(ratio)


def section_burns():
    print('F. burns (a site records once) + block capacity n (CL-4); odds never conditioned')
    L, M = 16, 4000; C, S = mats(L, TH); a, w, v = mode(L, TH, 2 * np.pi / L)
    for n in (4, 16, 64):
        T = int(1.25 * n * L); first, stuck, rat = burn_single(a.copy(), C, S, n, T, M); f = first[first >= 0]
        pre = np.nanmean(rat[:max(int(f.min()), 1)]); post = np.nanmean(rat[-10:])
        check(f'F1 FAILURE at exhaustion, ring L=16, n={n}: exact current until a block is used up, then all relays stuck (CL-4 has no rule)',
              abs(pre - 1) < 0.05 and stuck.mean() > 0.99 and abs(post) < 0.05,
              f'first hit min {f.min()} median {int(np.median(f))} (nL={n * L}); current/odds before {pre:.3f}, last 10 ticks {post:.3f}; stuck {stuck.mean():.3f}')
    # entangled pair sharing blocks: capacity used twice as fast
    n = 16; first, stuck, _ = burn_ring(n, L, int(0.75 * n * L), 3000, two=True); f = first[first >= 0]
    check(f'F2 entangled pair sharing blocks, n={n}: hits and stuck relays at about nL/2={n * L // 2}', stuck.mean() > 0.9,
          f'first hit min {f.min()} median {int(np.median(f))}; stuck by {int(0.75 * n * L)}: {stuck.mean():.3f}')
    # drifting packet on an open line: fresh blocks ahead; capacity hits come from the relay's own zigzags
    N = 300; C, S = mats(N, TH); pk = band_packet(N, TH, 2 * np.pi / 16, 60, 6.0); res = []
    for n in (1, 2, 4, 8):
        first, stuck, rat = burn_single(pk.copy(), C, S, n, 150, 4000, ring=False)
        res.append((n, (first >= 0).mean(), np.nanmean(rat)))
    check('F3 drifting packet (v~0.88), 150 ticks: n=1 breaks for most relays; n>=8 gives no hit at this scale',
          res[0][1] > 0.5 and res[-1][1] < 0.01, '; '.join(f'n={n}: hit {h:.3f}, current/odds {r:.3f}' for n, h, r in res))


# ---------------- G. standing waves: CL-7 stress versus the conserved stress of the walk
def relay_stress_single(psi, C, S, U):
    """CL-5 same-block energy, CL-6 switching + redraws at 2 eps from block odds, CL-7 deposits (1D turn = -1)."""
    L = len(psi) // 2; P = (abs(psi) ** 2).reshape(L, 2); Pc = (abs(C @ psi) ** 2).reshape(L, 2)
    new = U @ psi; Pn = (abs(new) ** 2).reshape(L, 2); W = Pn.sum(1)
    e = (Pn * -np.angle(new * psi.conj()).reshape(L, 2)).sum(1) / W
    tsw = np.clip(P - Pc, 0, None).sum(); trd = (np.clip(2 * e, 0, 1) * 2 * Pn[:, 0] * Pn[:, 1] / W).sum()
    return np.array([(e * W).sum(), (e[:, None] * Pn * [1, -1]).sum(), (e * W).sum() - tsw - trd]), tsw, trd


def section_standing():
    print('G. standing wave (theta 0.1, k = 2 pi 5/154 = 0.2040): burns+turns stress versus the conserved stress')
    th, N, m = 0.1, 154, 5; C, S = mats(N, th); U = S @ C; k = 2 * np.pi * m / N
    ev, V = np.linalg.eig(U); Hm = V @ np.diag(-np.angle(ev)) @ np.linalg.inv(V)
    sx = np.kron(np.eye(N), np.array([[0, 1], [1, 0]]))
    lin = lambda p: np.array([(p.conj() @ Hm @ p).real, th * (p.conj() @ sx @ p).real])   # <H>, theta <sigma_x> = theta dw/dtheta
    def dirac_xx(p):  # continuum-form canonical stress Re psi^dag sigma_z (-i d_x) psi, centred difference
        q = p.reshape(N, 2); dq = (np.roll(q, -1, 0) - np.roll(q, 1, 0)) / 2
        return (q.conj() * (-1j) * dq * np.array([1, -1])).sum().real
    (a, w, v), b = mode(N, th, k), mode(N, th, -k)[0]; sw = (a + b) / np.sqrt(2)
    Tp, _, _ = relay_stress_single(a, C, S, U); Ts, tsw, trd = relay_stress_single(sw, C, S, U)
    check('G1 plane wave: burns+turns give eps v^2', abs(Tp[2] - w * v * v) < 1e-9, f'T_xx={Tp[2]:.4f}, eps v^2={w * v * v:.4f}')
    check('G2 FAILURE of CL-7 for a standing wave (same modes, same energy): burns+turns stress has the wrong sign',
          Ts[2] < 0, f'T_xx={Ts[2]:.4f} (turns: switching {tsw:.4f}, redraw {trd:.4f}; plane-wave turns {w * (1 - v * v):.4f})')
    dp, ds = dirac_xx(a), dirac_xx(sw); Lp, Ls = lin(a), lin(sw)
    check('G3 conserved (linear) stress readings give the standing wave the plane-wave value',
          abs(dp - ds) < 1e-12 and abs((Lp - Ls)).max() < 1e-12,
          f'eps v^2={w * v * v:.4f}, k v={k * v:.4f}, Dirac-form {ds:.4f}, <H>-theta<sx> {Ls[0] - Ls[1]:.4f} (plane wave {Lp[0] - Lp[1]:.4f})')
    # random superposition of upper-band modes
    ks = 2 * np.pi * np.array([1, 3, 5, -4, -6, 8]) / N; c = rng.normal(size=6) + 1j * rng.normal(size=6); c /= np.linalg.norm(c)
    ms = [mode(N, th, q) for q in ks]; p = sum(ci * mi[0] for ci, mi in zip(c, ms))
    tgt = sum(abs(ci) ** 2 * mi[1] * mi[2] ** 2 for ci, mi in zip(c, ms)); Tr_, _, _ = relay_stress_single(p, C, S, U); Lr = lin(p)
    tgt2 = sum(abs(ci) ** 2 * (mi[1] - th * (mi[0].conj() @ sx @ mi[0]).real) for ci, mi in zip(c, ms))
    check('G4 repair: T_xx = <H> - theta <sigma_x> (mass-term reading) is linear, so any superposition gets its modes\' weighted stress',
          abs(Lr[0] - Lr[1] - tgt2) < 1e-12 and abs(Lr[0] - Lr[1] - tgt) / tgt < 0.02,
          f'6-mode packet: CL-7 burns+turns {Tr_[2]:.4f}; repaired {Lr[0] - Lr[1]:.4f}; mode-weighted eps v^2 {tgt:.4f}')


if __name__ == '__main__':
    section_energy()
    section_equivariance()
    section_readers()
    section_chsh()
    section_source()
    section_burns()
    section_standing()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
