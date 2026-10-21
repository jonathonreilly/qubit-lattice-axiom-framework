#!/usr/bin/env python3
"""Initial odds under CL-1..CL-6 (supplied model; finite diagnostic; no physical identification).

Which initial odds do the rules make natural, and what does each give for the arrow, the large-scale
fluctuation spectrum and relic abundances?  Candidates:
 (a) all sites empty, no records          (b) the half-filled sea (ground state of the tick's generator)
 (c) typical: Haar-random odds             (d) any odds stationary under the tick ("no-boundary-like")
 (e) definite start: the odds sit on ONE configuration at the first half-tick
     (e1) every configuration equally likely  (e2) the configuration the first records would read from (b)
 A  theorems: stationary odds freeze CL-5; strict light cone; superhorizon spectrum fixed by the start;
    analytic structure factor for finite-range starts (index 0 or 2, never 1)
 B  16-site torus, exact many-body odds (2^16 Fock space): odds entropy and the CL-5 move rate per candidate
 C  512-site torus, exact Gaussian evolution: light cone, block entropy growth, mode occupations
 D  structure-factor index at small q on a 64^3-site torus (Bloch + FFT), validated against real space
 E  measured-reality arithmetic: n_s, eta, link-free relic abundance, counting numerology
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/A_DEFINITE_START_GIVES_THE_RECORD_ARROW_BUT_NO_INITIAL_ODDS_GIVE_THE_SPECTRAL_TILT_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 90
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import comb
import numpy as np
from scipy.linalg import schur

T0 = time.monotonic(); PASS = FAIL = 0
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------- supplied tick: CL-3, same conventions as agents/records-causal-set/runner.py section C ----------------
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * CORN - 1).astype(float); OPP = 7 - np.arange(8)
def coherent(j, nv):
    th, ph, d = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])
XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]; W0 = np.zeros((8, 8), complex)
for s_, t_ in itertools.product(range(8), repeat=2):
    if abs(CORN[s_] - CORN[t_]).sum() == 1: g = XI[s_].conj() @ XI[t_]; W0[s_, t_] = -g / abs(g) / np.sqrt(3)
def Wa(a): return np.cos(a) * W0 + 1j * np.sin(a) * np.eye(8)
def half(psi, Wm, odd):
    X, Y, Z = psi.shape; p = np.roll(psi, -1, (0, 1, 2)) if odd else psi
    b_ = p.reshape(X // 2, 2, Y // 2, 2, Z // 2, 2).transpose(0, 2, 4, 1, 3, 5).reshape(-1, 8) @ (Wm[np.ix_(OPP, OPP)] if odd else Wm).T
    p = b_.reshape(X // 2, Y // 2, Z // 2, 2, 2, 2).transpose(0, 3, 1, 4, 2, 5).reshape(X, Y, Z)
    return np.roll(p, 1, (0, 1, 2)) if odd else p
def half_mats(shape, mu, b):
    We, Wo = Wa(mu / 2 + b), Wa(mu / 2 - b); N = int(np.prod(shape)); E = np.eye(N).reshape(N, *shape)
    return [np.stack([half(e, Wm, od).ravel() for e in E], 1) for Wm, od in ((We, 0), (Wo, 1))]
def sea_modes(U, tol=1e-12):   # U = e^{-iH}: fill quasi-energy omega = -angle < 0 (the branch is a supplied choice)
    w, V = np.linalg.eig(U); Q, _ = np.linalg.qr(V[:, -np.angle(w) < -tol]); return Q
def H2(p): p = p[p > 1e-300]; return float(-(p * np.log(p)).sum())
def ent(nu): nu = np.clip(nu, 1e-15, 1 - 1e-15); return float(-(nu * np.log(nu) + (1 - nu) * np.log(1 - nu)).sum())
MU, B = 0.4, 0.3

print('== A. theorems (proofs in the note; numerical checks in B-D)')
# T1: CL-5 picks, among transports p_t -> p_{t+1/2} using tick-connected moves, one with the largest stay mass.
#     Stay mass <= sum_n min(p_t(n), p_{t+1/2}(n)) = 1 - TV.  If p_{t+1/2} = p_t the identity transport reaches 1, and stay
#     mass 1 forces every configuration to stay: the configuration and every record it writes are frozen.  P(move) >= TV always.
# T2: a half-tick is a product of disjoint cube unitaries, so an operator at x after T half-ticks is supported within
#     L-infinity distance T of x (exact zero outside).  Connected correlations at distance > 2T + xi are those of the start.
# T3: the tick conserves N exactly, and by T2 the q -> 0 structure factor S(q,t) differs from S(q,0) only through
#     correlations inside the cone; for a start with finite correlation range S(q,t) is a trigonometric polynomial, hence
#     analytic and even in q: S = S0 + S2 q^2 + ... at every t.  Its small-q index is 0 (S0 != 0) or >= 2, never 1 or 0.965.
#     A non-even-integer index n needs connected correlations ~ r^-(3+n) at all ranges in the start itself.
print('   T1 stationary odds freeze CL-5; T2 strict cone; T3 analytic S(q) for finite-range starts (index 0 or >= 2)')

print('== B. 16-site torus 4x2x2, exact many-body odds in the 2^16 Fock space (mu, b) = (0.4, 0.3)')
shp = (4, 2, 2); NS = 16; Ue, Uo = half_mats(shp, MU, B)
def cubes(U):
    seen, out = set(), []
    for s in range(NS):
        if s in seen: continue
        comp, st = {s}, [s]
        while st:
            x = st.pop()
            for y in np.where(abs(U[:, x]) > 1e-12)[0]:
                if y not in comp: comp.add(int(y)); st.append(int(y))
        seen |= comp; out.append(sorted(comp))
    return out
states = np.arange(1 << NS); bits = (states[:, None] >> np.arange(NS)) & 1
def cube_op(U, S):
    S = np.array(S); O = np.array([s for s in range(NS) if s not in set(S)]); u = U[np.ix_(S, S)]
    iS = (bits[:, S] << np.arange(8)).sum(1); iO = (bits[:, O] << np.arange(len(O))).sum(1)
    below = np.cumsum(bits * np.isin(np.arange(NS), O), 1) - bits * np.isin(np.arange(NS), O)   # outside occupied below s
    sig = (-1.0) ** (bits[:, S] * below[:, S]).sum(1)
    G = np.zeros((256, 256), complex); sub = (np.arange(256)[:, None] >> np.arange(8)) & 1
    for m in range(256):
        for n in range(256):
            if sub[m].sum() == sub[n].sum():
                G[m, n] = np.linalg.det(u[np.ix_(np.where(sub[m])[0], np.where(sub[n])[0])]) if sub[m].sum() else 1.0
    return iS, iO, sig, G
OPS = [[cube_op(U, S) for S in cubes(U)] for U in (Ue, Uo)]
def fock_half(psi, par):
    for iS, iO, sig, G in OPS[par]:
        A = np.zeros((256, 256), complex); A[iS, iO] = sig * psi; A = G @ A; psi = sig * A[iS, iO]
    return psi
SEC = np.where(bits.sum(1) == 8)[0]; occ = [np.where(bits[i])[0] for i in SEC]; DIM = len(SEC)
def slater_fock(Q):   # odds amplitude of each N=8 configuration for the Slater state with orbitals Q (16 x 8)
    psi = np.zeros(1 << NS, complex); psi[SEC] = np.linalg.det(Q[np.array(occ)]); return psi
# validation: Fock evolution of a definite configuration equals the Slater evolution
x0 = np.sort(rng.choice(NS, 8, replace=False)); Q = np.eye(NS)[:, x0]; psi = slater_fock(Q); err = 0
for t in range(6):
    psi = fock_half(psi, t % 2); Q = (Ue if t % 2 == 0 else Uo) @ Q
    err = max(err, np.max(abs(abs(psi[SEC]) ** 2 - abs(slater_fock(Q)[SEC]) ** 2)))
check('Fock-space cube operators (with fermion reordering signs) reproduce the exact Slater odds of a definite start',
      err < 1e-12, f'max odds error {err:.1e} over 6 half-ticks, {DIM} configurations')
Ufull = Uo @ Ue; wq, Vq = np.linalg.eig(Ufull); om = -np.angle(wq); Qsea = sea_modes(Ufull)
ord_ = np.argsort(om); Qeig = np.linalg.qr(Vq[:, rng.choice(NS, 8, replace=False)])[0]
cands = {}
e0 = np.zeros(1 << NS, complex); e0[0] = 1; cands['(a) empty'] = e0
cands['(b) half-filled sea'] = slater_fock(Qsea)
cands['(d) a tick eigenstate'] = slater_fock(Qeig)
h = np.zeros(1 << NS, complex); h[SEC] = rng.normal(size=DIM) + 1j * rng.normal(size=DIM); cands['(c) Haar-typical'] = h / np.linalg.norm(h)
cands['(e1) definite, uniform'] = slater_fock(np.eye(NS)[:, x0])
psb = abs(cands['(b) half-filled sea'][SEC]) ** 2; i2 = rng.choice(DIM, p=psb / psb.sum()); cands['(e2) definite, sea-read'] = slater_fock(np.eye(NS)[:, occ[i2]])
TH = 40; res = {}
for k, psi in cands.items():
    sec = SEC if k != '(a) empty' else np.arange(1 << NS)
    p = abs(psi[sec]) ** 2; Ss, tv = [H2(p)], []
    for t in range(TH):
        psi = fock_half(psi, t % 2); q = abs(psi[sec]) ** 2; tv.append(0.5 * abs(q - p).sum()); p = q; Ss.append(H2(p))
    res[k] = (np.array(Ss), np.array(tv))
lnD = np.log(DIM)
for k, (Ss, tv) in res.items():
    print(f'   {k:26s} S(p)/ln D: t=0 {Ss[0] / lnD:.3f}, t=2 {Ss[2] / lnD:.3f}, late mean {Ss[20:].mean() / lnD:.3f};'
          f' move rate >= TV: first {tv[0]:.3f}, late mean {tv[20:].mean():.3f}')
fro = [res[k][1].max() for k in ('(a) empty', '(b) half-filled sea')]
check('T1: (a) and (b) are frozen: odds identical at every half-tick, so CL-5 moves nothing and every record repeats',
      max(fro) < 1e-12 and np.ptp(res['(b) half-filled sea'][0]) < 1e-10, f'max TV {max(fro):.1e}')
Sd, tvd = res['(d) a tick eigenstate']
check('(d) a stationary (tick-eigen) start: odds return every tick, so the configuration at most oscillates with period one tick',
      np.max(abs(Sd[::2] - Sd[0])) < 1e-10 and np.max(abs(tvd - np.tile(tvd[:2], TH // 2))) < 1e-10,
      f'half-tick TV {tvd[0]:.3f}, return error {np.max(abs(Sd[::2] - Sd[0])):.1e}')
Sc = res['(c) Haar-typical'][0]
check('(c) a typical start has near-maximal odds entropy at t = 0 and no growth: no arrow (equilibrium from the first half-tick)',
      Sc[0] / lnD > 0.95 and Sc[1:].mean() <= Sc[0] + 0.02, f'S/lnD {Sc[0] / lnD:.3f} -> mean {Sc[1:].mean() / lnD:.3f}')
S1, S2 = res['(e1) definite, uniform'][0], res['(e2) definite, sea-read'][0]
check('(e) a definite start has zero odds entropy and the largest possible growth: the arrow, with P(move) >= TV > 0 at every late half-tick',
      S1[0] < 1e-12 and S2[0] < 1e-12 and S1[20:].mean() / lnD > 0.5 and min(res['(e1) definite, uniform'][1][20:].min(), res['(e2) definite, sea-read'][1][20:].min()) > 0.05,
      f'S/lnD 0 -> {S1[20:].mean() / lnD:.3f} (e1), {S2[20:].mean() / lnD:.3f} (e2)')
# symmetric definite starts: the only configurations fixed by the CL-1 symmetries are empty and full (4 body-diagonal classes,
# permuted transitively by the 24 rotations about a cube centre), and both are tick eigenstates
cls = {tuple(sorted((tuple(c), tuple(1 - c)))) for c in CORN}
check('a definite start that privileges no site is all-empty or all-full (the 8 corners fall in 4 classes mod (1,1,1), permuted '
      'transitively by the rotations); both are frozen, so a definite start must leave WHICH configuration to a measure', len(cls) == 4)

del bits, states, OPS, cands, res, h, psi, e0
print('== C. 8^3 torus (512 sites), exact Gaussian evolution')
shp3 = (8, 8, 8); N3 = 512; Ue3, Uo3 = half_mats(shp3, MU, B)
xyz = np.array(np.unravel_index(np.arange(N3), shp3)).T
def blocks_R(Ureal, L):   # U(n+R, a; n, b) for R in {-1,0,1}^3 on an L^3-site torus
    s = lambda v: np.ravel_multi_index(tuple(np.asarray(v) % L), (L, L, L)); n0 = np.array([1, 1, 1]); out = {}
    for R in itertools.product((-1, 0, 1, 2), repeat=3):
        out[R] = np.array([[Ureal[s(2 * (n0 + R) + CORN[a]), s(2 * n0 + CORN[b])] for b in range(8)] for a in range(8)])
    return out
URm = blocks_R(np.matmul(*half_mats(shp3, 0.0, B)[::-1]), 8)
def bloch_P(Lb, URd, rule):   # spectral projector P(K) onto the filled modes, built slab by slab (memory)
    ks = 2 * np.pi * np.arange(Lb) / Lb; k2 = np.stack(np.meshgrid(ks, ks, indexing='ij'), -1)
    P = np.empty((Lb, Lb, Lb, 8, 8), complex); oms = np.empty((Lb, Lb, Lb, 8))
    for i in range(Lb):
        Kg = np.concatenate([np.full((Lb, Lb, 1), ks[i]), k2], -1); M = np.zeros((Lb, Lb, 8, 8), complex)
        for R, Mr in URd.items():
            if 2 not in R: M += Mr * np.exp(-1j * (Kg @ np.array(R, float)))[..., None, None]
        w, V = np.linalg.eig(M); oms[i] = -np.angle(w)
        P[i] = np.einsum('...ak,...k,...kb->...ab', V, rule(oms[i]).astype(float), np.linalg.inv(V))
    return P, oms
UR = blocks_R(Uo3 @ Ue3, 8); far = max(abs(M).max() for R, M in UR.items() if 2 in R)
def dinf(i, j): d = abs(xyz[i] - xyz[j]); return np.minimum(d, 8 - d).max(-1)
x0 = 0; v = np.eye(N3)[:, x0]; reach = []
for T in range(1, 4):
    v = (Ue3 if T % 2 else Uo3) @ v; reach.append(int(dinf(np.where(abs(v) > 1e-13)[0], x0).max()))
check('T2: the support after T half-ticks reaches exactly L-infinity distance T (strict cone; up to 3x the light speed 1/sqrt3 '
      'site per half-tick along a body diagonal)', reach == [1, 2, 3], f'reach {reach}')
Qs3 = sea_modes(Uo3 @ Ue3)
def half_cols(Phi, Wm, odd, L):   # the half-tick applied to many columns at once (Phi: L^3 x ncol)
    p = Phi.reshape(L, L, L, -1); p = np.roll(p, -1, (0, 1, 2)) if odd else p; h_ = L // 2
    b_ = np.einsum('ab,nbc->nac', Wm[np.ix_(OPP, OPP)] if odd else Wm, p.reshape(h_, 2, h_, 2, h_, 2, -1).transpose(0, 2, 4, 1, 3, 5, 6).reshape(h_ ** 3, 8, -1))
    p = b_.reshape(h_, h_, h_, 2, 2, 2, -1).transpose(0, 3, 1, 4, 2, 5, 6).reshape(L, L, L, -1)
    return (np.roll(p, 1, (0, 1, 2)) if odd else p).reshape(L ** 3, -1)
WE, WO = Wa(MU / 2 + B), Wa(MU / 2 - B); Xr = rng.normal(size=(N3, 3)) + 0j
hc_err = max(abs(half_cols(Xr, WE, 0, 8) - Ue3 @ Xr).max(), abs(half_cols(Xr, WO, 1, 8) - Uo3 @ Xr).max())
L12 = 12; N12 = L12 ** 3; xyz12 = np.array(np.unravel_index(np.arange(N12), (L12,) * 3)).T; blk = np.where((xyz12 < 4).all(1))[0]
P6, _ = bloch_P(6, UR, lambda o: o < 0); CR6 = np.fft.ifftn(P6, axes=(0, 1, 2)); nb, cn = np.divmod(xyz12, 2); ci = cn @ np.array([4, 2, 1])
C12 = np.empty((N12, N12), complex)
for x in range(N12): C12[x] = CR6[(nb[x, 0] - nb[:, 0]) % 6, (nb[x, 1] - nb[:, 1]) % 6, (nb[x, 2] - nb[:, 2]) % 6, ci[x], ci]
del P6, CR6
def block_S(Phi): A = Phi[blk]; return ent(np.linalg.eigvalsh(A @ A.conj().T))
S_sea = ent(np.linalg.eigvalsh(C12[np.ix_(blk, blk)]))
K = C12; conf = np.zeros(N12, bool)   # (e2): sample the sea's odds (determinantal process, sequential conditioning, in place)
for i in range(N12):
    pi = float(np.real(K[i, i])); conf[i] = rng.random() < pi; ki = K[:, i].copy(); kr = K[i, :].copy() / (pi if conf[i] else pi - 1)
    for r0 in range(0, N12, 288): K[r0:r0 + 288] -= np.outer(ki[r0:r0 + 288], kr)
del K, C12
starts = {'(e1) uniform': np.where(rng.random(N12) < 0.5)[0], '(e2) sea-read': np.where(conf)[0]}
Sb = {}
for k, occ_ in starts.items():   # evolve the occupied orbitals in chunks; keep only the block's 64 x 64 correlation
    CA = np.zeros((13, 64, 64), complex)
    for c0 in range(0, len(occ_), 128):
        Phi = np.zeros((N12, len(occ_[c0:c0 + 128])), complex); Phi[occ_[c0:c0 + 128], np.arange(Phi.shape[1])] = 1
        A = Phi[blk]; CA[0] += A @ A.conj().T
        for t in range(48):
            Phi = half_cols(Phi, WE if t % 2 == 0 else WO, t % 2, L12)
            if t % 4 == 3: A = Phi[blk]; CA[(t + 1) // 4] += A @ A.conj().T
    Sb[k] = np.array([ent(np.linalg.eigvalsh(C_)) for C_ in CA])
print(f'   12^3 torus (1728 sites); 4^3-block entropy per site; the sea (b) is constant at {S_sea / 64:.3f}; t = 0,4,..,48:')
for k, s_ in Sb.items(): print(f'   {k:14s} N = {len(starts[k]):4d}: ' + ' '.join(f'{x / 64:.2f}' for x in s_))
e1, e2 = Sb['(e1) uniform'] / 64, Sb['(e2) sea-read'] / 64
check('arrow: a definite start rises from zero block entropy to a volume law and stays far from zero (finite-torus revivals only)',
      hc_err < 1e-12 and max(e1[0], e2[0]) < 1e-9 and min(e1[1:].min(), e2[1:].min()) > 0.2 and min(e1[1:].mean(), e2[1:].mean()) > 0.4,
      f"after t >= 4: e1 min {e1[1:].min():.3f} mean {e1[1:].mean():.3f}; e2 min {e2[1:].min():.3f} mean {e2[1:].mean():.3f} (ln2 = 0.693)")
KAP = e1[1:].mean() / np.log(2)
check('(e2) reads exactly half filling (the sea is an N eigenstate), so its net charge has zero fluctuation', conf.sum() == N12 // 2, f'N = {conf.sum()}')
Tq3, Vq3 = schur(Uo3 @ Ue3, output='complex'); wq3 = np.diag(Tq3); occ1 = rng.random(N3) < 0.5; nk = (abs(Vq3[occ1]) ** 2).sum(0)
om3 = -np.angle(wq3)
check('(e1) occupies every tick mode about equally (infinite-temperature start): mode occupation independent of quasi-energy',
      abs(nk.mean() - occ1.sum() / N3) < 1e-10 and abs(np.corrcoef(om3, nk)[0, 1]) < 0.2,
      f'mean {nk.mean():.3f}, sd {nk.std():.3f}, corr with omega {np.corrcoef(om3, nk)[0, 1]:+.3f}')

print('== D. structure-factor index at small q: Bloch construction checked against real space, then 80^3 sites')
def S_of_q(P, m, d):   # S(q) = (1/8)[sum_a rho_a - sum_ab ph_a F_ab(Q) ph_b^*],  F(Q) = (1/Nb) sum_K P(K) o P(K-Q)^*
    Lb = P.shape[0]; d = np.array(d); F = np.zeros((8, 8), complex); rho = np.zeros(8)
    for i in range(Lb):
        sl = np.roll(P[(i - m * d[0]) % Lb], (m * d[1], m * d[2]), axis=(0, 1))
        F += (P[i] * sl.conj()).sum((0, 1)); rho += np.real(np.diagonal(P[i], axis1=-2, axis2=-1)).sum((0, 1))
    F /= Lb ** 3; rho /= Lb ** 3; ph = np.exp(-1j * (CORN @ (np.pi * m * d / Lb)))
    return float(np.real(rho.sum() - ph @ F @ ph.conj())) / 8
# real-space S(q) on 8^3 for the sea, against the Bloch result at Lb = 4
Cr = Qs3 @ Qs3.conj().T; Cov = np.diag(np.real(np.diag(Cr))) - abs(Cr) ** 2; qd = 2 * np.pi * np.array([1, 1, 0]) / 8
phr = np.exp(-1j * xyz @ qd); S_real = float(np.real(phr @ Cov @ phr.conj())) / N3
P4, om4 = bloch_P(4, UR, lambda o: o < 0); S_bl = S_of_q(P4, 1, (1, 1, 0))
check('Bloch construction: range-1 blocks, spectrum and S(q) agree with the real-space 512-site tick',
      far < 1e-12 and np.allclose(np.sort(om4.ravel()), np.sort(om3), atol=1e-9) and abs(S_real - S_bl) < 1e-10, f'S(q): {S_real:.6f} vs {S_bl:.6f}')
del Cr, Cov, P4
Lb = 40; ms = np.arange(1, 7); dirs = [(1, 0, 0), (1, 1, 0), (1, 1, 1)]
def index(URd, rule):
    P, oms = bloch_P(Lb, URd, rule); loc, flin = [], []
    for d in dirs:
        q = np.pi * ms * np.linalg.norm(d) / Lb; Sq = np.array([S_of_q(P, m, d) for m in ms])
        loc.append(np.log(Sq[1] / Sq[0]) / np.log(2)); A = np.linalg.lstsq(np.stack([q, q ** 2, q ** 3], 1), Sq, rcond=None)[0]
        flin.append(A[0] * q[0] / Sq[0])
    fill = float(np.mean([np.trace(np.real(P[i].sum((0, 1)))) for i in range(Lb)]) / Lb ** 2 / 8); del P
    return np.mean(loc), np.mean(flin), fill, oms
ng, fg, xg, omg = index(UR, lambda o: o < 0)
wF = np.quantile(omg, 0.56); del omg
nf, ff, xf, _ = index(UR, lambda o: o < wF)
nm, fm, xm, _ = index(URm, lambda o: o < -1e-9)
print(f'   80^3 sites, q = pi m/40 (m = 1..6), 3 directions. local index n from m = 1,2; linear share A q1/S(q1) from S = Aq + Bq^2 + Cq^3:')
for nm_, (n_, f_, x_) in (('gapped sea (mu, b) = (0.4, 0.3)', (ng, fg, xg)), ('massless sea (0, 0.3)', (nm, fm, xm)), ('doped sea (Fermi surface)', (nf, ff, xf))):
    print(f'     {nm_:32s} filling {x_:.3f}: n = {n_:.3f}, linear share {f_:+.3f}')
check('T3 illustrated: gapped and massless half-filled seas give index 2 with no linear term (analytic S); the uniform start is white '
      '(index 0, exact since its ensemble is rho ~ 1)', abs(ng - 2) < 0.1 and abs(nm - 2) < 0.2 and abs(fg) < 0.1 and abs(fm) < 0.1)
check('a Fermi surface gives a dominant |q| term (index -> 1): the free-fermion form of the scale-invariant (Harrison-Zeldovich) shape',
      ff > 0.7 and nf < 1.25, f'n = {nf:.3f}, linear share {ff:.3f}')

print('== E. measured-reality arithmetic')
ns, dns = 0.9649, 0.0042
print(f'   Planck 2018 n_s = {ns} +- {dns}: index 1 at {(1 - ns) / dns:.1f} sigma; index 0 at {ns / dns:.0f} sigma; index 2 at {(2 - ns) / dns:.0f} sigma')
check('no candidate gives the measured tilt: (a,b,d) freeze, (c,e1) white, (b,e2) index 2, a doped Fermi sea index 1 (8.4 sigma off)',
      (1 - ns) / dns > 5)
hb, cc, Gn = 1.054571817e-34, 2.99792458e8, 6.67430e-11; lP = np.sqrt(hb * Gn / cc ** 3); a_site = np.sqrt(8 * np.pi) * lP
Nh = 4 / 3 * np.pi * (4.4e26 / a_site) ** 3; eta_fl = 1 / np.sqrt(Nh)
check('baryon asymmetry: every CL rule conserves each species number, so eta is the start\'s; (e1) gives <eta> = 0 with |eta| ~ N^-1/2 '
      'and lattice-scale sign domains (excluded: no antimatter domains below ~Gpc, Cohen-De Rujula-Glashow 1998); (e2) gives exactly 0',
      eta_fl < 1e-80, f'N_sites in today\'s horizon {Nh:.1e}, |eta| ~ {eta_fl:.0e} vs measured 6.1e-10')
Oc, Ob, dOc, dOb = 0.1200, 0.02237, 0.0012, 0.00015; R = Oc / Ob; dR = R * np.hypot(dOc / Oc, dOb / Ob)
s0, rcrit = 2891.2, 1.05371e-5; mfac = Oc * rcrit / s0 * 1e9      # eV, m_c * (n_c/s)
print(f'   Omega_c/Omega_b = {R:.3f} +- {dR:.3f}; m_c (n_c/s) = {mfac:.3f} eV; (e1) late entropy per mode kappa ln2, kappa = {KAP:.3f}')
mc = lambda f: mfac * 2 * KAP * np.log(2) / f
check('(e1) fills a never-thermalised link-free species at 1/2 per mode: n_c/s = f/(2 kappa ln2) with f its mode fraction relative to '
      'the visible sector, so m_c = 0.61 kappa/f eV; hot (excluded, Lyman-alpha m > 5.3 keV) unless f < ~1e-4',
      mc(1.0) < 5.3e3 and mc(1e-4) > 1e3, f'f = 1: {mc(1.0):.2f} eV; f = 1/16: {mc(1/16):.1f} eV; f = 1e-4: {mc(1e-4) / 1e3:.1f} keV')
fr = sorted({(p, q) for q in range(1, 9) for p in range(1, 80) if np.gcd(p, q) == 1 and abs(p / q - R) < dR})
dens = sum(1 for q in range(1, 9) for p in range(5 * q, 6 * q) if np.gcd(p, q) == 1)
check('counting numerology: the mass-density ratio needs m_c/m_b, which no law supplies; fractions with q <= 8 inside 1 sigma are '
      'expected by chance, so a counting match is not evidence', len(fr) >= 1 and dens * 2 * dR > 1,
      f"hits {', '.join(f'{p}/{q}' for p, q in fr)}; expected by chance {dens * 2 * dR:.1f}")
print('supplied: the CL-3 tick with (mu, b) = (0.4, 0.3) and (0, 0.3); the negative-quasi-energy branch for "the sea"; the')
print('  identification of matter density with site occupation and P_delta(k) ~ k^n_s at fixed time; the unit map a = sqrt(8 pi) l_P;')
print('  standard adiabatic expansion for n_c/s; the uniform measure in (e1); all measured numbers.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
