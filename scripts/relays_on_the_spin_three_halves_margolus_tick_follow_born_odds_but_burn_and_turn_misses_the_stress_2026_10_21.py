#!/usr/bin/env python3
"""Relay rules on the spin-3/2 Margolus tick (supplied model; finite diagnostic; no physical identification).

Sites of Z^3 carry one mode each. Even blocks {0,1}^3 + 2Z^3, odd blocks shifted by (1,1,1). Each half-tick every block of
one partition applies W(mu) = cos(mu/2) W + i sin(mu/2) 1, with W the edge hop of amplitude 1/sqrt3 carrying the phase of
the two sites' spin-3/2 coherent-state overlap (polarisation n = 2 (x mod 2) - 1). Sections:
 A  independent check of the tick: unitarity, 24/24 covariance, bands, copies (own construction, own Bloch derivation);
 B  relay geometry (block-centre steps n/2 per half-tick), Born following by minimal switching, single and joint odds;
 C  the record source: burn-and-turn deposits versus the canonical (state-bilinear) stress, plane and standing waves;
 D  the pi-cone at K = pi(1,1,1).
Units: K per block (block = 2 sites), w per tick (tick = two half-ticks), velocities in blocks per tick.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/RELAYS_ON_THE_SPIN_THREE_HALVES_MARGOLUS_TICK_FOLLOW_BORN_ODDS_BUT_BURN_AND_TURN_MISSES_THE_STRESS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120


import itertools, os, signal, sys
from math import comb
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

PASS = FAIL = 0
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ------------------------------------------------------------------ the tick, built from scratch
CORN = np.array(list(itertools.product((0, 1), repeat=3)))   # corner / site parity c, index 4cx+2cy+cz
NV = (2 * CORN - 1).astype(float)                              # polarisation n(c); also the step label d
OPP = 7 - np.arange(8)                                         # opposite corner (c -> 1-c)


def coherent(j, n):
    th, ph, d = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])


XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]
WA = np.zeros((3, 8, 8), complex)
for s, t in itertools.product(range(8), repeat=2):
    if abs(CORN[s] - CORN[t]).sum() == 1:
        g = XI[s].conj() @ XI[t]; WA[int(np.argmax(abs(CORN[s] - CORN[t])))][s, t] = -g / abs(g) / np.sqrt(3)
W0 = WA.sum(0)
def Wmu(mu): return np.cos(mu / 2) * W0 + 1j * np.sin(mu / 2) * np.eye(8)


def Jm(j):
    m = j - np.arange(int(round(2 * j)) + 1); Jp = np.diag(np.sqrt(j * (j + 1) - m[1:] * (m[1:] + 1)), 1)
    return [(Jp + Jp.T) / 2, (Jp - Jp.T) / 2j, np.diag(m).astype(complex)]


def spin_rot(R, j=1.5, ang=None):
    w, V = np.linalg.eig(R); a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)) if ang is None else ang
    ax = np.real(V[:, np.argmin(abs(w - 1))]); ax /= np.linalg.norm(ax)
    if 1e-9 < a < np.pi - 1e-9 and np.dot(ax, [R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) < 0: ax = -ax
    e, Q = np.linalg.eigh(sum(ax[k] * Jm(j)[k] for k in range(3)))
    return Q @ np.diag(np.exp(-1j * a * e)) @ Q.conj().T


ROTS = [R for R in (np.array(p) * np.array(s)[:, None] for p in itertools.permutations(np.eye(3)) for s in itertools.product((1, -1), repeat=3)) if np.isclose(np.linalg.det(R), 1)]
def cidx(v): return int(np.argmin(abs(NV - v).sum(1)))


def corner_action(R):
    S = spin_rot(R); L = np.zeros((8, 8), complex)
    for i in range(8):
        k = cidx(R @ NV[i]); L[k, i] = XI[k].conj() @ S @ XI[i]
    return L


def half(psi, Wm, odd):
    """block unitary on even or odd blocks of an (X,Y,Z) site array; the matrix is indexed by site parity."""
    X, Y, Z = psi.shape; p = np.roll(psi, -1, (0, 1, 2)) if odd else psi
    b = p.reshape(X // 2, 2, Y // 2, 2, Z // 2, 2).transpose(0, 2, 4, 1, 3, 5).reshape(-1, 8)
    b = b @ (Wm[np.ix_(OPP, OPP)] if odd else Wm).T            # odd block: corner c' (from its origin) has parity 1-c'
    p = b.reshape(X // 2, Y // 2, Z // 2, 2, 2, 2).transpose(0, 3, 1, 4, 2, 5).reshape(X, Y, Z)
    return np.roll(p, 1, (0, 1, 2)) if odd else p


def blocks(p, odd):
    q = np.roll(p, -1, (0, 1, 2)) if odd else p; X, Y, Z = p.shape
    return q.reshape(X // 2, 2, Y // 2, 2, Z // 2, 2).transpose(0, 2, 4, 1, 3, 5).reshape(-1, 8)


def bloch_U(K, We, Wo=None):
    """derived: psi(2n+c) = e^{iK.n} phi(c) gives even half We, odd half D Wo D^dag, D = diag e^{iK.c}."""
    Wo = We if Wo is None else Wo; D = np.exp(1j * (CORN @ K)); return (D[:, None] * Wo * D.conj()[None, :]) @ We


def bloch_state(L, K, phi):
    n = np.arange(L // 2); ph = np.exp(1j * (K[0] * n[:, None, None] + K[1] * n[None, :, None] + K[2] * n[None, None, :]))
    out = np.zeros((L, L, L), complex)
    for ci, c in enumerate(CORN): out[c[0]::2, c[1]::2, c[2]::2] = ph * phi[ci]
    return out


def omega_formula(K, m1, m2=None):
    m2 = m1 if m2 is None else m2
    return np.arccos(np.clip(np.cos(m1 / 2) * np.cos(m2 / 2) * np.cos(K).sum(-1) / 3 - np.sin(m1 / 2) * np.sin(m2 / 2), -1, 1))


def grad_w(K, mu, h=1e-6): return np.array([(omega_formula(K + h * e, mu) - omega_formula(K - h * e, mu)) / 2 / h for e in np.eye(3)])


def upper_mode(K, mu, vec=None):
    """a +w eigenvector (positive quasi-energy band; fourfold) and the three leg amplitudes a0 -> a1 -> a2."""
    Wm = Wmu(mu); w, V = np.linalg.eig(bloch_U(K, Wm)); om = -np.angle(w); sel = np.where(om > 1e-12)[0]
    Q, _ = np.linalg.qr(V[:, sel]); phi = Q[:, 0] if vec is None else Q @ vec; phi = phi / np.linalg.norm(phi)
    a1 = Wm @ phi; D = np.exp(1j * (CORN @ K)); a2 = (D[:, None] * Wm * D.conj()[None, :]) @ a1
    return om[sel[0]], phi, a1, a2


def commutant_dim(Ms):
    A = np.vstack([np.kron(M, np.eye(8)) - np.kron(np.eye(8), M.T) for M in Ms]); return int((np.linalg.svd(A, compute_uv=False) < 1e-9).sum())


# ------------------------------------------------------------------ A. independent verification
def section_A():
    print('A. independent check of the tick (own coherent states, own J matrices, own Bloch form)')
    ac = max(abs(WA[a] @ WA[b] + WA[b] @ WA[a] - (2 / 3) * (a == b) * np.eye(8)).max() for a in range(3) for b in range(3))
    check('A1 {Wa,Wb} = (2/3) delta_ab, so W is Hermitian with W^2 = 1', ac < 1e-12 and abs(W0 - W0.conj().T).max() < 1e-14 and abs(W0 @ W0 - np.eye(8)).max() < 1e-12, f'{ac:.1e}')
    cyc = [0, 1, 3, 2]; hol = np.prod([XI[cyc[(i + 1) % 4]].conj() @ XI[cyc[i]] for i in range(4)])
    two_pi = spin_rot(np.eye(3), ang=2 * np.pi)
    check('A2 face holonomy of the spin-3/2 overlaps is -1 (pi flux); the 2pi rotation acts as -1', abs(hol / abs(hol) + 1) < 1e-12 and abs(two_pi + np.eye(4)).max() < 1e-12)
    Ls = [corner_action(R) for R in ROTS]
    check('A3 24 corner actions are monomial unitaries commuting with W', len(Ls) == 24 and max(abs(L @ L.conj().T - np.eye(8)).max() for L in Ls) < 1e-12 and max(abs(L @ W0 - W0 @ L).max() for L in Ls) < 1e-12)
    L = 4; sites = np.array(list(itertools.product(range(L), repeat=3))); Wm = Wmu(0.3)
    def mat(f):
        M = np.zeros((L**3, L**3), complex)
        for i in range(L**3):
            e = np.zeros(L**3, complex); e[i] = 1; M[:, i] = f(e.reshape(L, L, L)).ravel()
        return M
    Ue, Uo = mat(lambda p: half(p, Wm, False)), mat(lambda p: half(p, Wm, True))
    err = 0
    for R in ROTS:
        S = spin_rot(R)
        for cen in (np.full(3, .5), np.full(3, 1.5)):
            G = np.zeros((L**3, L**3), complex)
            for i, x in enumerate(sites):
                y = np.rint(R @ (x - cen) + cen).astype(int) % L
                G[(y[0] * L + y[1]) * L + y[2], i] = XI[cidx(2 * (y % 2) - 1)].conj() @ S @ XI[cidx(2 * (x % 2) - 1)]
            err = max(err, abs(G @ Ue - Ue @ G).max(), abs(G @ Uo - Uo @ G).max())
    check('A4 both half-ticks (4^3 sites) commute with all 24 rotations about an even and an odd block centre', err < 1e-12, f'{err:.1e}')
    inv = np.array([((-x[0]) % L * L + (-x[1]) % L) * L + (-x[2]) % L for x in sites]); I = np.eye(L**3)[inv]
    check('A5 site inversion x -> -x maps the even half-tick onto the odd one: U = (I U_e)^2', abs(I @ Ue @ I - Uo).max() < 1e-12)
    L8 = 8; dev = 0
    for K in [np.array(k) * np.pi / 2 for k in itertools.product(range(4), repeat=3)][::5]:
        w, V = np.linalg.eig(bloch_U(K, Wm))
        for a in range(8):
            p = bloch_state(L8, K, V[:, a]); dev = max(dev, abs(half(half(p, Wm, False), Wm, True) - w[a] * p).max())
    check('A6 the derived Bloch form reproduces the 8^3 lattice tick', dev < 1e-12, f'{dev:.1e}')
    KR = rng.uniform(-np.pi, np.pi, (1500, 3)); em = deg = 0
    for mu in (0.0, 0.1, 0.3, 1.0):
        for K in KR[:400]:
            w = np.sort(np.abs(np.angle(np.linalg.eigvals(bloch_U(K, Wmu(mu))))))
            em = max(em, abs(w - omega_formula(K, mu)).max()); deg = max(deg, np.ptp(w))
    check('A7 bands: cos w = cos^2(mu/2)(cos Kx+cos Ky+cos Kz)/3 - sin^2(mu/2), each of +-w fourfold (1600 K, 4 mu)', em < 1e-7 and deg < 1e-7, f'{em:.1e}')
    KG = np.array(list(itertools.product(np.linspace(-np.pi, np.pi, 41)[:-1], repeat=3))); wz = omega_formula(KG, 0.0)
    near = KG[wz < 0.3]
    check('A8 mu=0: w is small only near K=0 (no spatial doublers); mu>0: global gap = mu at K=0',
          np.abs(near).max() < 0.6 and abs(omega_formula(KG, 0.2).min() - 0.2) < 1e-12, f'{len(near)} grid points with w<0.3, max |K_a| {np.abs(near).max():.2f}')
    h = 1e-4
    def Heff(K, mu):
        w, V = np.linalg.eig(bloch_U(K, Wmu(mu))); return V @ np.diag(-np.angle(w)) @ np.linalg.inv(V)
    G = [Heff(h * np.eye(3)[a], 0.0) / h * np.sqrt(3) for a in range(3)]; B = Heff(np.zeros(3), 0.01) / 0.01
    cl = max([abs(G[a] @ G[b] + G[b] @ G[a] - 2 * (a == b) * np.eye(8)).max() for a in range(3) for b in range(3)] + [abs(B @ g + g @ B).max() for g in G] + [abs(B @ B - np.eye(8)).max()])
    cd = commutant_dim(G + [B])
    check('A9 low energy: H = (1/sqrt3) k.Gamma + mu beta, an 8x8 Clifford set whose commutant is 4-dim: exactly two Dirac copies, c = 1/sqrt3', cl < 1e-6 and cd == 4, f'Clifford err {cl:.1e}, commutant {cd}')
    c0, c1 = commutant_dim([bloch_U(K, Wmu(0.0)) for K in KR[:6]]), commutant_dim([bloch_U(K, Wmu(0.3)) for K in KR[:6]])
    check('A10 NEW: no taste symmetry acting within blocks: the common commutant of U(K) over K is 2-dim (mu=0) and 1-dim (mu>0)', c0 == 2 and c1 == 1, f'{c0}, {c1}')
    P = (np.eye(8) - W0) / 2      # W = -1: the w = +mu rest states (U(0) = W(mu)^2 = e^{-i mu} there)
    cls = {'C3 (120 deg)': ROTS[[i for i, R in enumerate(ROTS) if np.isclose(np.trace(R), 0)][0]],
           'C4 (90 deg)': ROTS[[i for i, R in enumerate(ROTS) if np.isclose(np.trace(R), 1)][0]],
           'C2 face': ROTS[[i for i, R in enumerate(ROTS) if np.isclose(np.trace(R), -1) and np.allclose(abs(R), np.eye(3))][0]],
           'C2 edge': ROTS[[i for i, R in enumerate(ROTS) if np.isclose(np.trace(R), -1) and not np.allclose(abs(R), np.eye(3))][0]]}
    ch = {k: np.trace(P @ corner_action(R) @ P).real for k, R in cls.items()}
    check('A11 NEW: the four w=+mu rest states carry G3/2 = E1/2 x E (characters 4,-1,0,0,0): a 90 deg rotation mixes the two copies',
          abs(np.trace(P).real - 4) < 1e-9 and abs(ch['C3 (120 deg)'] + 1) < 1e-9 and all(abs(ch[k]) < 1e-9 for k in ('C4 (90 deg)', 'C2 face', 'C2 edge')),
          ', '.join(f'{k} {v:+.2f}' for k, v in ch.items()))


# ------------------------------------------------------------------ B. relays
def flow(pin, pout):
    """CL-6 minimal switching on paired labels: keep min(pin,pout); excess goes to shortfalls in proportion."""
    keep = np.minimum(pin, pout); ex, sh = pin - keep, pout - keep
    return np.diag(keep) + (np.outer(ex, sh / sh.sum()) if sh.sum() > 1e-300 else 0)


def section_B():
    print('B. relay geometry and Born following (straight pairing: in-direction d -> out-direction d = opposite corner)')
    L = 8; X = np.array(list(itertools.product(range(L), repeat=3))); par = X % 2; n = 2 * par - 1
    ec = (X - par) + 0.5; oc = (X - (1 - par)) + 0.5     # centre of the even and of the odd block containing the site
    check('B1 each site is the shared corner of one even block and one odd block whose centre is (even centre) + n(x), n in {+-1}^3: a half-step of n/2 block',
          np.allclose(oc - ec, n))
    worst = 0
    for _ in range(40):
        K = rng.uniform(-np.pi, np.pi, 3) * rng.choice([0.1, 1.0]); mu = rng.choice([0.0, 0.2, 0.7])
        eps, a0, a1, a2 = upper_mode(K, mu, rng.normal(size=4) + 1j * rng.normal(size=4))
        v = 0.5 * (abs(a1)**2 @ NV - abs(a2)**2 @ NV); worst = max(worst, abs(v - grad_w(K, mu)).max())
    check('B2 group velocity = odds-weighted mean block step over the two legs (exact Hellmann-Feynman; 40 modes)', worst < 1e-7, f'{worst:.1e}')
    KG = rng.uniform(-np.pi, np.pi, (100000, 3)); cw = np.cos(KG).sum(1) / 3; vmax = np.linalg.norm(np.sin(KG) / 3 / np.sqrt(1 - cw**2)[:, None], axis=1).max()
    t = np.linspace(0.05, 3.1, 30); wd = omega_formula(t[:, None] * np.ones(3), 0.0)
    check('B3 light speed c = 1/sqrt3 block per tick is the zone maximum of |v| (mu=0), held exactly along every body diagonal (w = |K|/sqrt3 up to pi)',
          vmax < 1 / np.sqrt(3) + 1e-9 and vmax > 0.577 and abs(wd - t).max() < 1e-12, f'max |v| {vmax:.6f}; steps sqrt3/2 block per half-tick = sqrt3 per tick = 3c')
    ok = True
    for s, t_ in itertools.product(range(8), repeat=2):
        if abs(W0[t_, s]) > 1e-12:   # amplitude path: arrive at s (in-direction -n(s)), leave from t (out-direction n(t))
            din, dout = -NV[s], NV[t_]; ok &= np.isclose(din @ dout, -1) and np.isclose(abs(din + dout).sum(), 2)
    check('B4 amplitude paths: every edge hop turns the step by arccos(-1/3) = 109.47 deg (d -> -F_a d) and two hop half-steps net one block along an axis; the mass term reverses (d -> -d)', ok)
    perms = np.array(list(itertools.permutations(range(8)))); gens = [np.array([cidx(R @ NV[i]) for i in range(8)]) for R in ROTS]
    cen = np.all([np.all(perms[:, g] == g[perms], 1) for g in gens], 0); found = sorted(tuple(p) for p in perms[cen])
    check('B5 the only rotation-covariant pairings of in- and out-directions are straight (d->d) and reversal (d->-d)', found == sorted([tuple(range(8)), tuple(OPP)]), f'{len(found)} pairings')
    # B6 single relay: exact occupation and samples follow the odds through 12 half-ticks of a localised packet
    mu = 0.2; Wm = Wmu(mu); psi = np.zeros((L, L, L), complex); psi[2:6, 2:6, 2:6] = rng.normal(size=(4, 4, 4)) + 1j * rng.normal(size=(4, 4, 4))
    psi /= np.linalg.norm(psi); q = abs(psi)**2; M = 40000; samp = rng.choice(L**3, M, p=q.ravel()); tvq = 0
    idx = np.arange(L**3).reshape(L, L, L)
    for hstep in range(12):
        odd = hstep % 2 == 1; new = half(psi, Wm, odd)
        bi, bo, bq, bid = abs(blocks(psi, odd))**2, abs(blocks(new, odd))**2, blocks(q, odd), blocks(idx, odd)
        qn = np.zeros_like(bq); where = np.empty(L**3, int); slot = np.empty(L**3, int)
        where[bid.ravel()] = np.repeat(np.arange(len(bid)), 8); slot[bid.ravel()] = np.tile(np.arange(8), len(bid))
        Fs = []
        for b in range(len(bi)):
            F = flow(bi[b], bo[b][OPP]); Fs.append(F)                  # paired label j <-> out site OPP[j]
            T = np.where(bi[b][:, None] > 0, F / np.where(bi[b] > 0, bi[b], 1)[:, None], 0)
            qn[b][OPP] = bq[b] @ T
        bb, ss = where[samp], slot[samp]; u = rng.random(M); out = np.empty(M, int)
        for b in np.unique(bb):
            m = bb == b; T = Fs[b] / np.maximum(bi[b][:, None], 1e-300); cs = np.cumsum(T[ss[m]], 1); cs /= cs[:, -1:]
            out[m] = bid[b][OPP[np.minimum((u[m][:, None] > cs).sum(1), 7)]]
        samp = out; psi = new
        q = np.zeros(L**3); q[bid.ravel()] = qn.ravel(); q = q.reshape(L, L, L); tvq = max(tvq, 0.5 * abs(q - abs(psi)**2).sum())
    h_ = np.bincount(samp, minlength=L**3); e = M * abs(psi.ravel())**2; k = e >= 5; chi = ((h_[k] - e[k])**2 / e[k]).sum() / (k.sum() - 1)
    check('B6 single relay: exact occupation equals the odds at every half-tick, and 40000 sampled relays match them (chi2/dof)', tvq < 1e-12 and chi < 1.3, f'TV {tvq:.1e}, chi2/dof {chi:.2f} over {k.sum()} sites')
    # B7 two relays (two fermions, entangled: sum of two Slater determinants) on 4^3 sites; joint vs own-block-marginal switching
    L4 = 4; N = L4**3; f = [rng.normal(size=N) + 1j * rng.normal(size=N) for _ in range(4)]
    Psi = np.outer(f[0], f[1]) - np.outer(f[1], f[0]) + 0.8 * (np.outer(f[2], f[3]) - np.outer(f[3], f[2])); Psi /= np.linalg.norm(Psi)
    idx4 = np.arange(N).reshape(L4, L4, L4); Qj = abs(Psi)**2; Qm = Qj.copy(); tvj = tvm = 0
    def h4(P, odd): return np.stack([half(c.reshape(L4, L4, L4), Wm, odd).ravel() for c in P.T], 1)
    for hstep in range(8):
        odd = hstep % 2 == 1; U1 = h4(Psi, odd); New = h4(U1.T, odd).T
        bid = blocks(idx4, odd); Pi, Po = abs(Psi)**2, abs(New)**2; Qjn = np.zeros_like(Qj); Qmn = np.zeros_like(Qj)
        marg_i, marg_o = Pi.sum(1), Po.sum(1); Ts = {}
        for b in range(len(bid)):
            s = bid[b]; F = flow(marg_i[s], marg_o[s][OPP]); Ts[b] = np.where(marg_i[s][:, None] > 0, F / np.where(marg_i[s] > 0, marg_i[s], 1)[:, None], 0)
        for b1, b2 in itertools.product(range(len(bid)), repeat=2):
            s1, s2 = bid[b1], bid[b2]; pin = Pi[np.ix_(s1, s2)].ravel(); pout = Po[np.ix_(s1[OPP], s2[OPP])].ravel()
            F = flow(pin, pout); T = np.where(pin[:, None] > 0, F / np.where(pin > 0, pin, 1)[:, None], 0)
            Qjn[np.ix_(s1[OPP], s2[OPP])] = (Qj[np.ix_(s1, s2)].ravel() @ T).reshape(8, 8)
            Qmn[np.ix_(s1[OPP], s2[OPP])] = Ts[b1].T @ Qm[np.ix_(s1, s2)] @ Ts[b2]
        Qj, Qm, Psi = Qjn, Qmn, New; tvj = max(tvj, 0.5 * abs(Qj - Po).sum()); tvm = max(tvm, 0.5 * abs(Qm - Po).sum())
    check('B7 two entangled fermion relays: joint minimal switching keeps the joint odds exactly; own-block marginal switching does not', tvj < 1e-12 and tvm > 1e-2, f'TV joint {tvj:.1e}, marginal {tvm:.3f}')
    tvs = []
    for K, mu in ((np.array([0.1, 0, 0]), 0.0), (np.array([0.05, 0.08, 0.03]), 0.0), (np.array([0.1, 0, 0]), 0.2), (np.array([0.3, 0.2, -0.1]), 0.2)):
        eps, a0, a1, a2 = upper_mode(K, mu); qA, qB = abs(a1)**2, abs(a2[OPP])**2
        tvs.append((0.5 * abs(qA - qB).sum(), 0.5 * abs(abs(a0)**2 - abs(a1)**2).sum()))
    check('B8 plane waves: Born-following relays switch at most half-ticks (straight TV >= 0.78; reversal pairing TV = 1 at mu=0)',
          min(t[0] for t in tvs) > 0.78 and abs(tvs[0][1] - 1) < 1e-12, 'straight ' + ', '.join(f'{t[0]:.3f}' for t in tvs) + '; reversal ' + ', '.join(f'{t[1]:.3f}' for t in tvs))
    okz, txt = True, []
    for _ in range(6):
        eps, a0, a1, a2 = upper_mode(np.array([1e-3, 0, 0]), 0.0, rng.normal(size=4) + 1j * rng.normal(size=4)); mA, mB = abs(a1)**2 @ NV, -abs(a2)**2 @ NV
        okz &= abs(mA[0] - 1 / np.sqrt(3)) < 1e-5 and abs(mB[0] - 1 / np.sqrt(3)) < 1e-5 and np.allclose(mA[1:], -mB[1:], atol=1e-5); txt.append(np.linalg.norm(mA[1:]))
    eps, a0, a1, a2 = upper_mode(np.array([1, 1, 1]) * 1e-3, 0.0, rng.normal(size=4) + 1j * rng.normal(size=4)); kh = np.ones(3) / np.sqrt(3)
    check('B9 zigzag (massless, K along x, 6 states of the band): forward odds (1+1/sqrt3)/2 = 0.789 on both legs; transverse leg means cancel; net/path = 1/3',
          okz, f'|transverse leg mean| {min(txt):.2f}..{max(txt):.2f}; K along (1,1,1): legs split the forward step {abs(a1)**2 @ NV @ kh:.3f} + {-abs(a2)**2 @ NV @ kh:.3f}')


# ------------------------------------------------------------------ C. the record source
def relay_source(states, mu, eps, L):
    """CL-7 on half-steps: steps eps*dt*(1,d)(1,d) [d = n or -n, |d| = sqrt3]; redraws with probability eps per half-tick
    from the block's out-odds, each turn depositing -1/4 (d'-d)(d'-d); and the straight-pairing switching chords (unweighted)."""
    Wm = Wmu(mu); a0 = states; a1 = half(a0, Wm, False); a2 = half(a1, Wm, True)
    st = np.zeros((3, 3)); rd = np.zeros((3, 3)); sw = np.zeros((3, 3)); dd = NV[None, :, :] - NV[:, None, :]
    for pin, pout in ((abs(blocks(a0, False))[:, OPP]**2, abs(blocks(a1, False))**2), (abs(blocks(a1, True))[:, OPP]**2, abs(blocks(a2, True))**2)):
        st += eps * 0.5 * np.einsum('ba,ai,aj->ij', pout, NV, NV)
        for i in range(len(pin)):
            P = pout[i].sum()
            if P < 1e-15: continue
            qq = pout[i] / P; m = qq @ NV; rd -= (eps / 2) * P * (np.einsum('a,ai,aj->ij', qq, NV, NV) - np.outer(m, m))
            sw += np.einsum('ab,abi,abj->ij', flow(pin[i], pout[i]), dd, dd)
    return st, rd, sw


def canonical(psi, mu, c2=1 / 3):
    """c^2 * sym( step d^i  x  Re psi^* (-i)(psi(x+2e_j) - psi(x-2e_j))/2 ), averaged over the two legs: bilinear in the state."""
    Wm = Wmu(mu); a1 = half(psi, Wm, False); a2 = half(a1, Wm, True)
    n = 2 * np.array(np.meshgrid(*[np.arange(s) % 2 for s in psi.shape], indexing='ij')) - 1; T = np.zeros((3, 3))
    for a, sg in ((a1, 1), (a2, -1)):
        for j in range(3):
            pj = (a.conj() * (-1j) * (np.roll(a, -2, j) - np.roll(a, 2, j)) / 2).real
            for i in range(3): T[i, j] += 0.5 * sg * (n[i] * pj).sum()
    return c2 * (T + T.T) / 2


def glob_rot(psi, R, cen):
    L = psi.shape[0]; S = spin_rot(R); out = np.zeros_like(psi)
    for x in itertools.product(range(L), repeat=3):
        x = np.array(x); y = np.rint(R @ (x - cen) + cen).astype(int) % L
        out[tuple(y)] += XI[cidx(2 * (y % 2) - 1)].conj() @ S @ XI[cidx(2 * (x % 2) - 1)] * psi[tuple(x)]
    return out


def section_C():
    print('C. record source: target eps v v (per relay per tick) for plane waves; standing waves have the same modes and energy')
    rows = []
    for K, mu in ((np.array([0.1, 0, 0]), 0.0), (np.array([0.05, 0.08, 0.03]), 0.0), (np.array([0.1, 0, 0]), 0.2), (np.array([0.3, 0.2, -0.1]), 0.2), (np.array([0.6, 0.1, 0.4]), 0.5)):
        eps, a0, a1, a2 = upper_mode(K, mu); qA, qB = abs(a1)**2, abs(a2[OPP])**2; mA, mB = qA @ NV, qB @ NV; v = (mA + mB) / 2
        tgt = eps * np.outer(v, v); strd = eps * (np.outer(mA, mA) + np.outer(mB, mB)) / 2
        dd = NV[None, :, :] - NV[:, None, :]; sw = sum(np.einsum('ab,abi,abj->ij', flow(x, y), dd, dd) for x, y in ((qB, qA), (qA, qB)))
        rows.append((tgt, strd, sw, eps, K, mu, v))
    e1 = max(abs(r[1] - r[0]).max() / abs(r[0]).max() for r in rows)
    check('C1 FAILURE: steps + redraws (2 eps per tick) give eps (mA mA + mB mB)/2, not eps v v: the leg-to-leg zigzag stays in the stress', e1 > 1, f'max relative error {e1:.1f}')
    A = np.array([(r[3] * r[2]).ravel() for r in rows]).ravel(); b = np.array([(r[0] - r[1]).ravel() for r in rows]).ravel()
    al = (A @ b) / (A @ A); res = np.linalg.norm(b - al * A) / np.linalg.norm(b)
    check('C2 FAILURE: the best single coefficient on energy-weighted switching chords still misses eps v v by >10% (5 plane waves)', res > 0.1, f'best alpha {al:.4f}, residual {res:.2f}')
    feats, targs = [], []
    for _ in range(300):
        mu = rng.choice([0.0, 0.1, 0.3]); K = rng.normal(size=3) * rng.choice([0.05, 0.2, 0.5])
        eps, a0, a1, a2 = upper_mode(K, mu, rng.normal(size=4) + 1j * rng.normal(size=4)); qA, qB = abs(a1)**2, abs(a2[OPP])**2
        feats.append(np.concatenate([eps * qA, eps * qB, qA, qB])); targs.append(eps * np.outer(*[grad_w(K, mu)] * 2)[np.triu_indices(3)])
    F_, T_ = np.array(feats), np.array(targs); coef, *_ = np.linalg.lstsq(F_, T_, rcond=None); rr = np.linalg.norm(F_ @ coef - T_) / np.linalg.norm(T_)
    check('C3 no stress linear in the direction odds (with or without the CL-5 energy weight) fits eps v v over 300 plane waves', rr > 0.2, f'best linear residual {rr:.2f}')
    L = 24; mu = 0.2
    for m, R in (((1, 0, 0), np.diag([-1., 1, -1])), ((1, 1, 0), np.diag([-1., -1, 1]))):
        K = 2 * np.pi * np.array(m) / (L // 2); eps, phi, _, _ = upper_mode(K, mu); pw = bloch_state(L, K, phi); pw /= np.linalg.norm(pw)
        sw_ = pw + glob_rot(pw, R, np.full(3, .5)); sw_ /= np.linalg.norm(sw_)
        Wm = Wmu(mu); eig = abs(half(half(sw_, Wm, False), Wm, True) - np.exp(-1j * eps) * sw_).max()
        Sp, Ss = relay_source(pw, mu, eps, L), relay_source(sw_, mu, eps, L); Cp, Cs = canonical(pw, mu), canonical(sw_, mu)
        tg = eps * np.outer(*[grad_w(K, mu)] * 2)
        check(f'C4 K = 2pi{m}/12: standing wave (eigenstate, err {eig:.0e}) changes the relay source; the canonical stress is unchanged',
              abs((Sp[0] + Sp[1]) - (Ss[0] + Ss[1])).max() > 0.05 * abs(tg).max() and abs(Cp - Cs).max() < 1e-12,
              f'relay xx/yy/xy plane {np.round([(Sp[0]+Sp[1])[0,0], (Sp[0]+Sp[1])[1,1], (Sp[0]+Sp[1])[0,1]], 3)}, standing {np.round([(Ss[0]+Ss[1])[0,0], (Ss[0]+Ss[1])[1,1], (Ss[0]+Ss[1])[0,1]], 3)}; canon {np.round([Cs[0,0], Cs[1,1], Cs[0,1]], 4)}, target {np.round([tg[0,0], tg[1,1], tg[0,1]], 4)}')
    ks = [np.array(k) * 2 * np.pi / (L // 2) for k in ((1, 0, 0), (0, 1, 1), (-1, 2, 0), (2, 0, -1), (0, 0, -1), (1, 1, 1))]
    cs = rng.normal(size=6) + 1j * rng.normal(size=6); cs /= np.linalg.norm(cs); modes = []
    for K in ks:
        eps, phi, _, _ = upper_mode(K, mu, rng.normal(size=4) + 1j * rng.normal(size=4)); p = bloch_state(L, K, phi); modes.append(p / np.linalg.norm(p))
    tot = canonical(sum(c * p for c, p in zip(cs, modes)), mu); wsum = sum(abs(c)**2 * canonical(p, mu) for c, p in zip(cs, modes))
    check('C5 the canonical stress of a 6-mode superposition is the odds-weighted sum of its modes (exactly linear)', abs(tot - wsum).max() < 1e-12, f'{abs(tot - wsum).max():.1e}')
    dev = []
    for mu in (0.0, 0.1):
        for kk in (0.05, 0.1, 0.2):
            for _ in range(10):
                u = rng.normal(size=3); K = kk * u / np.linalg.norm(u); eps, a0, a1, a2 = upper_mode(K, mu)
                v = 0.5 * (abs(a1)**2 @ NV - abs(a2)**2 @ NV); can = np.outer(v, np.sin(K)) / 3; can = (can + can.T) / 2
                tg = eps * np.outer(v, v); dev.append((mu, kk, abs(can - tg).max() / abs(tg).max()))
    d = {(m, k): max(x[2] for x in dev if x[0] == m and x[1] == k) for m, k, _ in dev}
    check('C6 plane waves: canonical stress (c^2 = 1/3) -> eps v v as K, mu -> 0 (lattice error O(K^2, mu^2))',
          d[(0.0, 0.05)] < 1e-3 and d[(0.0, 0.2)] < 2e-2 and d[(0.1, 0.05)] < 1e-2, ', '.join(f'mu {m} |K| {k}: {x:.1e}' for (m, k), x in d.items()))


# ------------------------------------------------------------------ D. the pi-cone
def section_D():
    print('D. the cone at K = pi(1,1,1), quasi-energy pi')
    Kp = np.full(3, np.pi); ok = True; sp = []
    for mu in (0.0, 0.3, 1.0):
        ok &= np.allclose(np.abs(np.angle(np.linalg.eigvals(bloch_U(Kp, Wmu(mu))))), np.pi)
        u = rng.normal(size=(50, 3)); u /= np.linalg.norm(u, axis=1)[:, None]; q = 1e-3
        w = np.abs(np.angle(np.linalg.eigvals(np.array([bloch_U(Kp + q * x, Wmu(mu)) for x in u]))))
        sp.append((np.pi - w).mean() / q / (np.cos(mu / 2) / np.sqrt(3)))
    check('D1 all 8 states sit at w = pi for every mu; the cone is massless with speed c cos(mu/2), isotropic', ok and max(abs(np.array(sp) - 1)) < 1e-3, 'speed/(c cos(mu/2)) ' + ', '.join(f'{s:.5f}' for s in sp))
    KR = rng.uniform(-np.pi, np.pi, (300, 3)); em = 0; m1, m2 = 0.9, -0.5
    for K in KR:
        w = np.sort(np.abs(np.angle(np.linalg.eigvals(bloch_U(K, Wmu(m1), Wmu(m2))))))
        em = max(em, abs(w - omega_formula(K, m1, m2)).max())
    g0, gp = omega_formula(np.zeros(3), m1, m2), np.pi - omega_formula(Kp, m1, m2)
    check('D2 NEW: different masses on the two half-ticks: cos w = cos(m1/2)cos(m2/2) S - sin(m1/2)sin(m2/2); K=0 mass (m1+m2)/2, pi-cone gap |m1-m2|/2',
          em < 1e-7 and abs(g0 - abs(m1 + m2) / 2) < 1e-12 and abs(gp - abs(m1 - m2) / 2) < 1e-12, f'formula err {em:.1e}; K=0 gap {g0:.3f}, pi gap {gp:.3f}')
    check('D3 each W(m) commutes with the 24 corner actions, so the staggered-mass tick keeps 24/24 covariance; it breaks U = (I U_e)^2',
          max(abs(corner_action(R) @ Wmu(m1) - Wmu(m1) @ corner_action(R)).max() for R in ROTS) < 1e-12)
    eps = -np.angle(np.linalg.eigvals(bloch_U(Kp + 0.05 * np.array([1, 0, 0]), Wmu(0.1))))
    t = np.linspace(1e-3, np.pi - 1e-3, 20001); vd = []
    for mu in (0.1, 0.3, 1.0):
        c2, s2 = np.cos(mu / 2)**2, np.sin(mu / 2)**2; vdiag = c2 * np.sin(t) / (np.sqrt(3) * np.sqrt(1 - (c2 * np.cos(t) - s2)**2))
        KG = rng.uniform(-np.pi, np.pi, (60000, 3)); cw = c2 * np.cos(KG).sum(1) / 3 - s2
        vz = np.linalg.norm(c2 * np.sin(KG) / 3 / np.sqrt(1 - cw**2)[:, None], axis=1).max(); vd.append((vdiag.max() / (np.cos(mu / 2) / np.sqrt(3)), vz <= vdiag.max() + 1e-9))
    check('D5 NEW: a massive band\'s top group speed is c cos(mu/2) (on the body diagonals): species-dependent top speed, 1 - cos(mu/2) ~ mu^2/8 below c',
          all(abs(a - 1) < 1e-6 and b for a, b in vd), 'max|v|/(c cos(mu/2)) ' + ', '.join(f'{a:.6f}' for a, _ in vd))
    check('D4 CL-5 reads a pi-cone mode as energy |w| ~ pi rad per tick, outside CL-6 domain (<= 1/2)', np.abs(eps).min() > 3.0, f'|w| {np.abs(eps).min():.4f}')


if __name__ == '__main__':
    section_A(); section_B(); section_C(); section_D()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
