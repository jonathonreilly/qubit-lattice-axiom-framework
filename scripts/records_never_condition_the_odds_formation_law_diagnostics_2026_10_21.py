#!/usr/bin/env python3
"""Supplied lossless walks with relays: candidate formation law 'records never condition the odds'.
Relays follow the odds by the CL-6 minimal switching flow on the joint configuration of all relays;
the odds are never conditioned on a record. Checks, in supplied 1D walks and few-qubit couplings:
exact equivariance and sampled Born statistics; ballistic drift kept (versus conditioning every tick and
conditioning at a rate twice the energy); definite agreeing outcomes for an ideal pointer coupling
(versus marginal-only switching); no signalling of outcome marginals and CHSH above 2 for a singlet;
interference kept (versus conditioning when branches have disjoint support); free crossing undisturbed
(versus conditioning when two relays meet); and a failure: the expected turn count, hence the CL-7 turn
deposit, of a distant relay depends on a remote measurement basis. No physical identification.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/RECORDS_NEVER_CONDITION_THE_ODDS_FORMATION_LAW_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time
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


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------- CL-6 minimal switching flow (rederived equivariant: see note)
def switch(P, Pn, blk, d):
    """relays at (blk, d) switch from directions over their new odds to directions under them,
    in proportion to the shortfalls. P, Pn: (B, D) odds before/after. Returns new d."""
    ex = np.clip(P - Pn, 0, None); sh = np.clip(Pn - P, 0, None); S = sh.sum(1)
    Pr = P[blk, d]; p = np.where(Pr > 0, ex[blk, d] / np.where(Pr > 0, Pr, 1), 0.0)
    sw = rng.random(len(d)) < p
    if sw.any():
        b = blk[sw]; cs = np.cumsum(sh[b], 1) / S[b][:, None]
        d = d.copy(); d[sw] = np.minimum((rng.random(sw.sum())[:, None] > cs).sum(1), P.shape[1] - 1)
    return d


def flow_occupation(Q, P, Pn):
    """exact image of an occupation Q under the flow built from P -> Pn (Markov kernel)."""
    ex = np.clip(P - Pn, 0, None); sh = np.clip(Pn - P, 0, None); S = sh.sum(1, keepdims=True)
    stay = np.where(P > 0, 1 - ex / np.where(P > 0, P, 1), 1.0)
    out = (Q * (1 - stay)).sum(1, keepdims=True)
    return Q * stay + out * np.where(S > 0, sh / np.where(S > 0, S, 1), 0)


# ---------------- 1D two-direction walk: d=0 steps +1, d=1 steps -1
def coin(psi, th):
    c, s = np.cos(th), np.sin(th)
    a, b = psi[..., 0], psi[..., 1]
    return np.stack([c * a - 1j * s * b, -1j * s * a + c * b], -1)


def shift(psi):
    return np.stack([np.roll(psi[..., 0], 1, -1), np.roll(psi[..., 1], -1, -1)], -1)


def band_packet(N, th, k0, x0, sig):
    """upper-band packet of U(k) = diag(e^-ik, e^ik) C(th)."""
    ks = 2 * np.pi * np.fft.fftfreq(N); amp = np.zeros((N, 2), complex)
    C = np.array([[np.cos(th), -1j * np.sin(th)], [-1j * np.sin(th), np.cos(th)]])
    for i, k in enumerate(ks):
        w, V = np.linalg.eig(np.diag([np.exp(-1j * k), np.exp(1j * k)]) @ C)
        j = int(np.argmax(-np.angle(w))); v = V[:, j] * np.exp(-1j * np.angle(V[0, j]))
        dk = (k - k0 + np.pi) % (2 * np.pi) - np.pi
        amp[i] = v * np.exp(-dk ** 2 * sig ** 2 / 2 - 1j * k * x0)
    psi = np.fft.ifft(amp, axis=0) * N
    return psi / np.linalg.norm(psi)


def energy(psi_old, psi_new):
    """CL-5 per block: odds-weighted phase advance at the same block."""
    adv = -np.angle(psi_new * psi_old.conj()); Pn = abs(psi_new) ** 2
    return (Pn * adv).sum(-1) / np.maximum(Pn.sum(-1), 1e-300)


def relay_walk(psi, th, T, M, fresh=True):
    """odds evolve unconditioned; M relays follow by CL-6 switching (+ fresh draws w.p. 2 eps)."""
    N = psi.shape[0]; P = abs(psi) ** 2
    idx = rng.choice(2 * N, M, p=(P / P.sum()).ravel()); x, d = idx // 2, idx % 2
    Q = P.copy(); xs = [x.mean()]
    for _ in range(T):
        P = abs(psi) ** 2; pc = coin(psi, th); Pc = abs(pc) ** 2
        d = switch(P, Pc, x, d); Q = flow_occupation(Q, P, Pc)
        new = shift(pc); x = (x + 1 - 2 * d) % N; Q = shift(Q)
        if fresh:
            Pn = abs(new) ** 2; r = np.clip(2 * abs(energy(psi, new)), 0, 1)
            red = rng.random(M) < r[x]; cond = Pn / np.maximum(Pn.sum(1, keepdims=True), 1e-300)
            d[red] = (rng.random(red.sum()) > cond[x[red], 0]).astype(int)
            Q = (1 - r[:, None]) * Q + r[:, None] * Q.sum(1, keepdims=True) * cond
        psi = new; xs.append(x.mean())
    return psi, x, d, Q, np.array(xs)


def section_born_and_drift():
    print('A. single walker: Born statistics and free drift')
    N, T, M = 241, 100, 20000
    psi = np.zeros((N, 2), complex); psi[120] = [1 / np.sqrt(2), 1j / np.sqrt(2)]
    psi, x, d, Q, _ = relay_walk(psi, np.pi / 4, T, M)
    P = abs(psi) ** 2
    check('A1 exact equivariance: flow image of the odds is the odds after 100 ticks', abs(Q - P).max() < 1e-12, f'max|Q-P|={abs(Q-P).max():.1e}')
    px = P.sum(1); h = np.bincount(x, minlength=N); e = M * px; keep = e >= 5
    chi = ((h[keep] - e[keep]) ** 2 / e[keep]).sum() / (keep.sum() - 1)
    sq = np.sqrt((px * (np.arange(N) - 120) ** 2).sum())
    check('A2 sampled relays match the Born histogram (chi2/dof)', chi < 1.6, f'chi2/dof={chi:.3f} over {keep.sum()} bins; Born spread {sq:.1f} sites (ballistic, classical walk ~{np.sqrt(T):.0f})')
    # drift of a massive packet
    N, T, M, th, k0 = 800, 400, 5000, 0.1, 0.2
    psi0 = band_packet(N, th, k0, 150, 15.0); xx = np.arange(N)
    om = np.arccos(np.cos(th) * np.cos(k0)); v0 = np.cos(th) * np.sin(k0) / np.sin(om)
    psi, x, d, _, xs = relay_walk(psi0.copy(), th, T, M)
    disp_exact = ((abs(psi) ** 2).sum(1) * xx).sum() - ((abs(psi0) ** 2).sum(1) * xx).sum()
    disp_rel = xs[-1] - xs[0]; se = x.std() / np.sqrt(M)
    check('A3 unconditioned odds keep the drift: exact <x> shift / (v T)', abs(disp_exact / (v0 * T) - 1) < 0.02, f'v={v0:.4f}, ratio={disp_exact/(v0*T):.4f}')
    check('A4 relays carry the same drift', abs(disp_rel - disp_exact) < 4 * se + 0.5, f'relay {disp_rel:.2f} vs odds {disp_exact:.2f} sites')
    # (i) records condition the odds every tick: each relay's odds collapse to its block -> persistent walk
    P0 = abs(psi0) ** 2; idx = rng.choice(2 * N, M, p=P0.ravel()); xc, dc = idx // 2, idx % 2; x0m = xc.mean()
    for _ in range(T):
        dc = np.where(rng.random(M) < np.sin(th) ** 2, 1 - dc, dc); xc = xc + 1 - 2 * dc
    ri = (xc.mean() - x0m) / (v0 * T)
    # (iii) conditioning with probability 2*eps per tick (eps of the packet)
    Mr = 200; idx = rng.choice(2 * N, Mr, p=P0.ravel()); xg, dg = idx // 2, idx % 2; x0g = xg.mean()
    ps = np.repeat(psi0[None], Mr, 0); r = min(1.0, 2 * om); ar = np.arange(Mr)
    for _ in range(T):
        P = abs(ps) ** 2; pc = coin(ps, th); Pc = abs(pc) ** 2
        dg = switch(P.reshape(-1, 2), Pc.reshape(-1, 2), ar * N + xg, dg)
        ps = shift(pc); xg = (xg + 1 - 2 * dg) % N
        hit = np.where(rng.random(Mr) < r)[0]
        if len(hit):
            kv = ps[hit, xg[hit]].copy(); ps[hit] = 0; ps[hit, xg[hit]] = kv / np.linalg.norm(kv, axis=1, keepdims=True)
    riii = (xg.mean() - x0g) / (v0 * T)
    check('A5 conditioning every tick (i) loses the drift', ri < 0.2, f'drift ratio {ri:.3f}')
    check('A6 conditioning at rate 2*eps (iii) loses about half the drift by T=400', riii < 0.6, f'rate {r:.3f}/tick, drift ratio {riii:.3f}')


# ---------------- joint configuration of several pointers (spins have no relays)
def joint_P(psi, nspin):
    P = (abs(psi) ** 2).sum(tuple(range(nspin)))           # (N1, 2, N2, 2)
    N1, N2 = P.shape[0], P.shape[2]
    return P.transpose(0, 2, 1, 3).reshape(N1 * N2, 4), N1, N2


def joint_step(psi, op, nspin, x1, x2, d, rule='joint'):
    """apply on-block op to psi, switch relays (joint dirs d = 2*d1 + d2), then shift both pointers."""
    P, N1, N2 = joint_P(psi, nspin); new = op(psi); Pn, _, _ = joint_P(new, nspin); blk = x1 * N2 + x2
    ex = np.clip(P - Pn, 0, None); sh = np.clip(Pn - P, 0, None); S = sh.sum(1)
    flowB = 0.0
    for a in range(4):
        for b in range(4):
            if a != b and (a % 2) != (b % 2):
                flowB += (ex[:, a] * np.where(S > 0, sh[:, b] / np.where(S > 0, S, 1), 0)).sum()
    if rule == 'joint':
        d = switch(P, Pn, blk, d)
    else:  # marginal-only: each pointer switches by its own marginal odds
        R = P.reshape(N1, N2, 2, 2); Rn = Pn.reshape(N1, N2, 2, 2)
        d1, d2 = d // 2, d % 2
        d1 = switch(R.sum((1, 3)), Rn.sum((1, 3)), x1, d1); d2 = switch(R.sum((0, 2)), Rn.sum((0, 2)), x2, d2)
        d = 2 * d1 + d2
    sh_ = [slice(None)] * nspin
    out = new.copy()
    out[(*sh_, slice(None), 0)] = np.roll(new[(*sh_, slice(None), 0)], 1, nspin)
    out[(*sh_, slice(None), 1)] = np.roll(new[(*sh_, slice(None), 1)], -1, nspin)
    sp = out.copy()
    sp[..., 0] = np.roll(out[..., 0], 1, -1); sp[..., 1] = np.roll(out[..., 1], -1, -1)
    x1 = (x1 + 1 - 2 * (d // 2)) % N1; x2 = (x2 + 1 - 2 * (d % 2)) % N2
    return sp, x1, x2, d, flowB


def sample_joint(psi, nspin, M):
    P, N1, N2 = joint_P(psi, nspin); idx = rng.choice(P.size, M, p=(P / P.sum()).ravel())
    blk, d = idx // 4, idx % 4
    return blk // N2, blk % N2, d


def Ry(t):
    return np.array([[np.cos(t / 2), -np.sin(t / 2)], [np.sin(t / 2), np.cos(t / 2)]])


def section_pointers():
    print('B. ideal pointer coupling: definite, agreeing outcomes')
    N = 24; al2 = 0.3
    psi = np.zeros((2, N, 2, N, 2), complex)
    psi[0, 8, 0, 8, 0] = np.sqrt(al2); psi[1, 8, 0, 8, 0] = np.sqrt(1 - al2)
    def couple(p):  # both pointers flip direction iff spin is down
        q = p.copy(); q[1] = p[1][:, ::-1][:, :, :, ::-1]; return q
    for rule in ('joint', 'marginal'):
        x1, x2, d = sample_joint(psi, 1, 20000); ps = psi.copy()
        ps, x1, x2, d, _ = joint_step(ps, couple, 1, x1, x2, d, rule)
        for _ in range(6):
            ps, x1, x2, d, _ = joint_step(ps, lambda p: p, 1, x1, x2, d, rule)
        up1, up2 = x1 > 8, x2 > 8; f = up1.mean(); dis = (up1 != up2).mean()
        if rule == 'joint':
            check('B1 pointer reading frequency is the Born weight', abs(f - al2) < 4 * np.sqrt(al2 * (1 - al2) / 20000), f'{f:.4f} vs {al2}')
            check('B2 joint switching: two readers never disagree', dis == 0, f'disagreement {dis:.4f}')
        else:
            check('B3 marginal-only switching: readers disagree at 2p(1-p)', abs(dis - 2 * al2 * (1 - al2)) < 0.02, f'disagreement {dis:.4f} vs {2*al2*(1-al2):.2f}')


def singlet_run(a, b, M, betaB=None, phiB=None, tB=0):
    """singlet spins; A: Ry(a) then flip dA iff sA down (tick 0). B: either the same at tick 0 with b,
    or (betaB, phiB) pointer prepared in cos/sin superposition, rotated by +-phiB at tick tB."""
    N = 26; psi = np.zeros((2, 2, N, 2, N, 2), complex)
    if betaB is None:
        psi[0, 1, 12, 0, 12, 0] = 1 / np.sqrt(2); psi[1, 0, 12, 0, 12, 0] = -1 / np.sqrt(2)
    else:  # B amplitudes converge on block 12 at tick 1 with both directions
        for xb, db, c in ((11, 0, np.cos(betaB)), (13, 1, np.sin(betaB))):
            psi[0, 1, 12, 0, xb, db] = c / np.sqrt(2); psi[1, 0, 12, 0, xb, db] = -c / np.sqrt(2)
    x1, x2, d = sample_joint(psi, 2, M); turnsB = []; margB = []
    def opA(p):
        q = np.einsum('ij,jk...->ik...', Ry(a), p) if a is not None else p.copy()
        if a is not None: q[1] = q[1][:, :, ::-1]
        return q
    def opB(p):
        q = np.einsum('ij,kj...->ki...', Ry(b), p); q[:, 1] = q[:, 1][:, :, :, :, ::-1]; return q
    def opBrot(p):
        q = p.copy()
        for s, sg in ((0, 1), (1, -1)):
            c, sn = np.cos(sg * phiB), np.sin(sg * phiB)
            u, v = p[:, s, ..., 0], p[:, s, ..., 1]; q[:, s, ..., 0] = c * u - sn * v; q[:, s, ..., 1] = sn * u + c * v
        return q
    for t in range(6):
        op = (lambda p: opB(opA(p))) if (t == 0 and betaB is None) else (opA if t == 0 else (opBrot if (betaB is not None and t == tB) else (lambda p: p)))
        psi, x1, x2, d, fB = joint_step(psi, op, 2, x1, x2, d)
        turnsB.append(fB); margB.append((abs(psi) ** 2).sum((0, 1, 2, 3)))
    PA = (abs(psi) ** 2).sum((0, 1, 4, 5)).sum(0); PB = (abs(psi) ** 2).sum((0, 1, 2, 3)).sum(0)
    PAB = (abs(psi) ** 2).sum((0, 1)).sum((0, 2))   # (dA, dB)
    E_exact = PAB[0, 0] + PAB[1, 1] - PAB[0, 1] - PAB[1, 0]
    rA = np.where(x1 > 12, 1, -1); rB = np.where(x2 > 12, 1, -1)
    return dict(E=E_exact, Er=(rA * rB).mean(), PBup=PB[0], fBup=(rB > 0).mean(), turnsB=turnsB, margB=np.array(margB), d=d)


def section_bell():
    print('C. singlet: no signalling of outcomes, CHSH')
    M = 20000; a0, a1, b0, b1 = 0.0, np.pi / 2, np.pi / 4, -np.pi / 4
    R = {(a, b): singlet_run(a, b, M) for a in (a0, a1) for b in (b0, b1)}
    S_ex = abs(R[a0, b0]['E'] + R[a0, b1]['E'] + R[a1, b0]['E'] - R[a1, b1]['E'])
    S_rl = abs(R[a0, b0]['Er'] + R[a0, b1]['Er'] + R[a1, b0]['Er'] - R[a1, b1]['Er'])
    check('C1 exact odds give CHSH 2 sqrt 2', abs(S_ex - 2 * np.sqrt(2)) < 1e-12, f'S={S_ex:.6f}')
    check('C2 relay readings violate CHSH', S_rl > 2.6, f'S_relays={S_rl:.3f} (local bound 2)')
    PB = [singlet_run(a, b0, 2000)['PBup'] for a in (0.0, 0.7, np.pi / 2, None)]
    check('C3 B outcome odds independent of A setting (and of A doing nothing)', np.ptp(PB) < 1e-12, f'P_B(up) spread {np.ptp(PB):.1e}')
    fB = [R[a, b0]['fBup'] for a in (a0, a1)]
    check('C4 sampled B frequency independent of A setting', abs(fB[0] - fB[1]) < 4 * np.sqrt(0.5 / M), f'{fB[0]:.4f} vs {fB[1]:.4f}')


def section_turn_signal():
    print('D. turn source of a distant relay under a remote measurement basis')
    res = {}
    for name, a in (('none', None), ('z', 0.0), ('x', np.pi / 2)):
        res[name] = singlet_run(a, None, 20000, betaB=np.pi / 4, phiB=np.pi / 8, tB=1)
    mspread = max(abs(res[n]['margB'] - res['none']['margB']).max() for n in res)
    check('D1 B position-direction odds at every tick independent of A (burn density unchanged)', mspread < 1e-12, f'max diff {mspread:.1e}')
    tb = {n: res[n]['turnsB'][1] for n in res}
    check('D2 expected B turns at its coupling tick DEPEND on A basis (signalling via CL-7 turn deposits)',
          abs(tb['z'] - tb['x']) > 0.3, f"none {tb['none']:.4f}, z {tb['z']:.4f}, x {tb['x']:.4f}; deposit -1 per 1D turn")
    check('D3 z-basis value equals sum over A branches of |change of B odds| = sin(pi/4)/2', abs(tb['z'] - np.sin(np.pi / 4) / 2) < 1e-12, f'{tb["z"]:.6f}')


def section_interference():
    print('E. interferometer: candidate keeps fringes; disjoint-support conditioning (iv) erases them')
    N, x0, W, M = 64, 32, 10, 10000; H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    out = {}
    for phi in (0.0, np.pi):
        psi = np.zeros((N, 2), complex); psi[x0, 0] = 1
        x = np.full(M, x0); d = np.zeros(M, int)
        for t in range(2 * W + 1):
            P = abs(psi) ** 2; new = psi.copy()
            if t == 0 or t == 2 * W:
                new[x0] = H @ psi[x0]
            if t == 0:
                new[x0, 1] *= np.exp(1j * phi)
            for w in (x0 - W, x0 + W):
                new[w] = new[w][::-1]
            d = switch(P, abs(new) ** 2, x, d)
            if t < 2 * W: psi = shift(new); x = (x + 1 - 2 * d) % N
            else: psi = new
        pR_cand = abs(psi[x0, 0]) ** 2; fR = (d == 0).mean()
        out[phi] = (pR_cand, fR)
    vis = abs(out[0.0][0] - out[np.pi][0]) / (out[0.0][0] + out[np.pi][0])
    check('E1 candidate: exact fringe visibility 1', abs(vis - 1) < 1e-12, f'P_R(0)={out[0.0][0]:.3f}, P_R(pi)={out[np.pi][0]:.3f}')
    check('E2 candidate relays reproduce the fringe', abs(out[0.0][1] - out[0.0][0]) < 0.02 and abs(out[np.pi][1] - out[np.pi][0]) < 0.02, f'relays {out[0.0][1]:.3f}, {out[np.pi][1]:.3f}')
    # (iv): branches have disjoint support from tick 1, so the odds are conditioned on the relay's branch;
    # each branch alone gives P_R = 1/2 at the final beam splitter for every phase
    single = np.array([1, 0]); pR_iv = abs((H @ single)[0]) ** 2
    check('E3 (iv) conditioning on disjoint branches gives P_R = 1/2 at every phase (visibility 0)', abs(pR_iv - 0.5) < 1e-12, f'P_R={pR_iv:.3f}')


def section_meeting():
    print('F. two free walkers crossing: conditioning when relays meet (ii) disturbs them')
    N, th, T, Mr = 32, 0.3, 30, 120
    p1 = band_packet(N, th, 0.9, 8, 2.0); p2 = band_packet(N, th, -0.9, 24, 2.0)
    psi0 = np.einsum('ab,cd->abcd', p1, p2)
    def mom1(ps):
        return (abs(np.fft.fft(ps, axis=-4)) ** 2).sum((-1, -2, -3))
    m0 = mom1(psi0); m0 /= m0.sum()
    ps = np.repeat(psi0[None], Mr, 0); P = (abs(psi0) ** 2).transpose(0, 2, 1, 3).reshape(-1, 4)
    idx = rng.choice(P.size, Mr, p=P.ravel()); x1, x2, d = (idx // 4) // N, (idx // 4) % N, idx % 4
    met = np.zeros(Mr, bool); ar = np.arange(Mr)
    for _ in range(T):
        P = (abs(ps) ** 2).transpose(0, 1, 3, 2, 4).reshape(Mr, N * N, 4)
        new = coin(ps, th); new = coin(new.transpose(0, 3, 4, 1, 2), th).transpose(0, 3, 4, 1, 2)
        Pn = (abs(new) ** 2).transpose(0, 1, 3, 2, 4).reshape(Mr, N * N, 4)
        d = switch(P.reshape(-1, 4), Pn.reshape(-1, 4), ar * N * N + x1 * N + x2, d)
        new = shift(new.transpose(0, 3, 4, 1, 2)).transpose(0, 3, 4, 1, 2); new = shift(new)
        ps = new; x1 = (x1 + 1 - 2 * (d // 2)) % N; x2 = (x2 + 1 - 2 * (d % 2)) % N
        for i in np.where(x1 == x2)[0]:
            blk = ps[i, x1[i], :, x2[i], :].copy(); ps[i] = 0; ps[i, x1[i], :, x2[i], :] = blk / np.linalg.norm(blk); met[i] = True
    # candidate: no conditioning -> exact unitary, momentum distribution of walker 1 unchanged
    pc = psi0.copy()
    for _ in range(T):
        pc = coin(pc, th); pc = coin(pc.transpose(2, 3, 0, 1), th).transpose(2, 3, 0, 1)
        pc = shift(pc.transpose(2, 3, 0, 1)).transpose(2, 3, 0, 1); pc = shift(pc)
    mc = mom1(pc); mc /= mc.sum()
    mii = sum(mom1(ps[i]) / mom1(ps[i]).sum() for i in range(Mr)) / Mr
    tv_c = 0.5 * abs(mc - m0).sum(); tv_ii = 0.5 * abs(mii - m0).sum()
    check('F1 candidate: free crossing leaves walker-1 momentum odds unchanged', tv_c < 1e-12, f'TV={tv_c:.1e}')
    check('F2 (ii) meeting-conditioning disturbs non-interacting walkers', tv_ii > 0.05, f'met fraction {met.mean():.2f}, TV={tv_ii:.3f}')


if __name__ == '__main__':
    section_born_and_drift()
    section_pointers()
    section_bell()
    section_turn_signal()
    section_interference()
    section_meeting()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
