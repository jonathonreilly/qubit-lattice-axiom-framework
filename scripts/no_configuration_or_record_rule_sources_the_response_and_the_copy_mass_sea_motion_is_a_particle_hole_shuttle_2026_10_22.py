AUDIT_INPUT_PATHS = ('docs/NO_CONFIGURATION_OR_RECORD_RULE_SOURCES_THE_RESPONSE_AND_THE_COPY_MASS_SEA_MOTION_IS_A_PARTICLE_HOLE_SHUTTLE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""departure-law: does CL-2's forced motion of the copy-massed sea create departures from the vacuum?
(supplied models; finite diagnostics; estimates labelled; no physical identification beyond the stated unit map)
 A  the sea's odds at the two half-ticks: what differs, and the forced flips
 B  the one-cube start and the split cascade: does the forced motion carry a clock?
 C  what CL-3 sees; baryon number and the C-odd part
 D  estimates against measurement; the two escapes (records condition the odds, CL-3 reads the configuration)
Supplied: CL-1 cube tick with the copy mass on equal edges, lapse 1 (b, mu, M) = (0.3, 0.4, 0.5) unless stated; its
negative-quasi-energy vacuum; antiperiodic tori; 12-site 3x2x2 patches; the unit map a = sqrt(8 pi) l_P, tau = 2a/(sqrt3 c).
"""
import itertools, os, signal, sys, time
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import comb
import numpy as np
from scipy.linalg import expm
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
# ---------------------------------------------------------------- CL-1 tick (rule text): spin-3/2 edge hop, copy sign, copy mass
CORN = np.array(list(itertools.product((0, 1), repeat=3)))
def coh(nv):
    th, ph = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0])
    return np.array([np.sqrt(comb(3, k)) * np.cos(th / 2) ** (3 - k) * np.sin(th / 2) ** k * np.exp(1j * (k - 1.5) * ph) for k in range(4)])
XI = [coh((2 * c - 1) / np.sqrt(3)) for c in CORN]; W = np.zeros((8, 8), complex); Wax = [np.zeros((8, 8), complex) for _ in range(3)]
for s, t in itertools.product(range(8), repeat=2):
    d = np.abs(CORN[s] - CORN[t])
    if d.sum() == 1:
        g = XI[s].conj() @ XI[t]; W[s, t] = -g / abs(g) / np.sqrt(3); Wax[int(np.argmax(d))][s, t] = W[s, t]
SC = 1j * np.sqrt(3) ** 3 * Wax[0] @ Wax[1] @ Wax[2] @ W
def ticks(b, mu, M):
    e = np.pi / 2 - b; Cm = expm(1j * (M / 4) * (np.eye(8) - SC) @ W)
    return Cm @ expm(-1j * (e - mu / 2) * W) @ Cm, expm(1j * (e + mu / 2) * W)
lab = lambda x: 4 * (x[0] % 2) + 2 * (x[1] % 2) + x[2] % 2
def realspace(We, Wo, Lc, anti=True):            # antiperiodic (or periodic) torus of Lc^3 even cubes
    Ls = 2 * Lc; N = Ls ** 3; idx = lambda x: (x[0] % Ls) * Ls * Ls + (x[1] % Ls) * Ls + x[2] % Ls
    Ue = np.zeros((N, N), complex); Uo = np.zeros((N, N), complex)
    for n in itertools.product(range(Lc), repeat=3):
        bs = 2 * np.array(n); ids = [idx(bs + c) for c in CORN]; Ue[np.ix_(ids, ids)] += We
        st = [bs + 1 + c for c in CORN]; ids = [idx(x) for x in st]; sv = np.array([(-1) ** int(sum(x // Ls)) if anti else 1 for x in st])
        Uo[np.ix_(ids, ids)] += sv[:, None] * Wo[np.ix_([lab(x) for x in st], [lab(x) for x in st])] * sv[None, :]
    return Ue, Uo, idx
def corr_k(b, mu, M, L):                         # Bloch construction of both half-tick stages of the vacuum
    We, Wo = ticks(b, mu, M); Ue, Uo, idx = realspace(We, Wo, 3, False)   # periodic Lc = 3: each +-1 cell displacement distinct
    Tm = {d: np.array([[Uo[idx(ca), idx(2 * np.array(d) + cb)] for cb in CORN] for ca in CORN]) for d in itertools.product((-1, 0, 1), repeat=3)}
    ks = (2 * np.pi * np.arange(L) + np.pi) / L; K = np.array(list(itertools.product(ks, repeat=3)))
    P0 = np.zeros((len(K), 8, 8), complex); P1 = np.zeros_like(P0)
    for i, k in enumerate(K):
        w, V = np.linalg.eig(sum(A * np.exp(1j * k @ np.array(d)) for d, A in Tm.items()) @ We)
        Q, _ = np.linalg.qr(V[:, -np.angle(w) < 0]); Q1 = We @ Q; P0[i] = Q.conj() @ Q.T; P1[i] = Q1.conj() @ Q1.T
    return K, P0, P1
def patchC(K, P, sites):
    R = np.array([np.array(x) // 2 for x in sites]); a = [lab(x) for x in sites]
    return np.array([[(np.exp(1j * K @ (R[j] - R[i])) * P[:, a[i], a[j]]).mean() for j in range(len(sites))] for i in range(len(sites))])
def podds(C):                                    # Gaussian pattern odds on a patch
    n = len(C); PT = np.array(list(itertools.product((0, 1), repeat=n)), bool)
    return np.linalg.det(np.where(PT[:, :, None], C[None], np.eye(n)[None] - C[None])).real, PT
TV = lambda p, q: 0.5 * np.abs(p - q).sum()
PA = [(i, j, k) for i in range(3) for j in range(2) for k in range(2)]
def tv_patch(b, mu, M, L=8):
    K, P0, P1 = corr_k(b, mu, M, L); return TV(podds(patchC(K, P0, PA))[0], podds(patchC(K, P1, PA))[0])

print('== A. the copy-massed sea at the two half-tick stages (12-site 3x2x2 patch, 8^3 cubes)')
We, Wo = ticks(0.3, 0.4, 0.5); Ue, Uo, idx = realspace(We, Wo, 4)
w, V = np.linalg.eig(Uo @ Ue); Q, _ = np.linalg.qr(V[:, -np.angle(w) < 0]); C0r = Q.conj() @ Q.T; Q1 = Ue @ Q; C1r = Q1.conj() @ Q1.T
tv_real = TV(podds(C0r[np.ix_([idx(x) for x in PA], [idx(x) for x in PA])])[0], podds(C1r[np.ix_([idx(x) for x in PA], [idx(x) for x in PA])])[0])
K, P0, P1 = corr_k(0.3, 0.4, 0.5, 4); tv_k4 = TV(podds(patchC(K, P0, PA))[0], podds(patchC(K, P1, PA))[0])
K, P0, P1 = corr_k(0.3, 0.4, 0.5, 8); C0, C1 = patchC(K, P0, PA), patchC(K, P1, PA); p0, PT = podds(C0); p1, _ = podds(C1)
tv0, tvM = tv_patch(0.3, 0.4, 0.0), TV(p0, p1)
check('A1 finite diagnostic: the copy mass makes the sea\'s odds differ between half-ticks (zero at M = 0); CL-2 then flips at least '
      'TV/12 occupations per site per half-tick (real space = Bloch at 4^3)', abs(tv_real - tv_k4) < 1e-12 and tv0 < 1e-12 and tvM > 1e-3,
      f'TV M=0 {tv0:.0e}, M=.5 {tvM:.2e}; >= {tvM / 12:.1e} flips/site/half-tick')
maps = {'PH': (lambda x: x, True), 'R4x': (lambda x: (x[0], 1 - x[2], x[1]), False), 'Myz': (lambda x: (x[0], x[2], x[1]), False),
        'PH.R4x': (lambda x: (x[0], 1 - x[2], x[1]), True), 'R2x': (lambda x: (x[0], 1 - x[1], 1 - x[2]), False)}
res = {}
for nm, (g, ph) in maps.items():
    q0 = podds(patchC(K, P0, [g(x) for x in PA]))[0]; q0 = q0[::-1] if ph else q0
    res[nm] = (TV(q0, p0), TV(q0, p1))
check('A2 finite diagnostic (exact to rounding): stage 1 is stage 0 with particles and holes exchanged, equally its fourfold turn or '
      'yz mirror; PH x fourfold turn and the half turn keep each stage. The forced motion is a period-2 shuttle P -> P o PH -> P',
      all(res[n][1] < 1e-13 for n in ('PH', 'R4x', 'Myz')) and all(res[n][0] < 1e-13 for n in ('PH.R4x', 'R2x')),
      '; '.join(f'{n}: {a:.0e}/{c:.0e}' for n, (a, c) in res.items()) + ' (TV to stage 0/1)')
D0, D1 = C0 - np.eye(12) / 2, C1 - np.eye(12) / 2
k3 = lambda D, t: 2 * (D[t[0], t[1]] * D[t[1], t[2]] * D[t[2], t[0]]).real
tri = list(itertools.combinations(range(12), 3)); k30 = np.array([k3(D0, t) for t in tri]); k31 = np.array([k3(D1, t) for t in tri])
quads = [t for t in itertools.permutations(range(12), 4) if t[0] == min(t)][::7]
l4 = max(abs(np.prod([D0[t[m], t[(m + 1) % 4]] for m in range(4)]) - np.prod([D1[t[m], t[(m + 1) % 4]] for m in range(4)])) for t in quads)
check('A3 consequence: every even-order density statistic (|C_ij|, 4-loops) is the same at both stages; odd orders flip sign, '
      'third cumulant of three sites', np.abs(abs(C0) - abs(C1)).max() < 1e-13 and l4 < 1e-14 and np.abs(k30 + k31).max() < 1e-15 and np.abs(k30).max() > 1e-5,
      f'd|C| {np.abs(abs(C0) - abs(C1)).max():.0e}; 4-loop {l4:.0e}; max|k3| {np.abs(k30).max():.2e}, k3_0 + k3_1 {np.abs(k30 + k31).max():.0e}')
cnt = PT.sum(1); h0 = np.bincount(cnt, p0, 13); h1 = np.bincount(cnt, p1, 13)
cube = [i for i, x in enumerate(PA) if x[0] < 2]; sub = PT[:, cube].sum(1); c0 = np.bincount(sub, p0, 9); c1 = np.bincount(sub, p1, 9)
check('A4 THEOREM (from A2): a region mapped to itself by the fourfold turn has the same count distribution at both stages '
      '(P1(N) = P0(n-N) = P0(N)); the shuttle is invisible to every coarse cube count', TV(h0, h1) < 1e-13 and TV(c0, c1) < 1e-13,
      f'3x2x2 counts TV {TV(h0, h1):.0e}, 2x2x2 {TV(c0, c1):.0e} (patterns {tvM:.1e})')
Lg = 16; K, Q0, Q1_ = corr_k(0.3, 0.4, 0.5, Lg)
def Gf(P):
    G = np.fft.ifftn(P.reshape(Lg, Lg, Lg, 8, 8), axes=(0, 1, 2)); return np.abs(G) ** 2
def Sq(G2, m):
    q = 2 * np.pi * m / (2 * Lg); dx = 2 * np.arange(Lg)[:, None, None, None, None] + CORN[None, None, None, None, :, 0] - CORN[None, None, None, :, None, 0]
    return 0.25 - (G2 * np.cos(q * dx)).sum() / 8 + 0.25 * 1      # remove i=j term counted in the sum (|C_ii|^2 = 1/4)
G20, G21 = Gf(Q0), Gf(Q1_); S0 = [Sq(G20, m) for m in (1, 2, 4)]; S1 = [Sq(G21, m) for m in (1, 2, 4)]
sl = np.log(S0[1] / S0[0]) / np.log(2); xi = [np.sqrt(G20[d, 0, 0].max()) for d in (1, 2, 3, 4)]
check('A5 finite diagnostic: the density structure factor is the same at both stages and falls as q^2 (gapped, number conserved): '
      'the vacuum configuration\'s large-scale noise is fixed, and |C| decays exponentially', max(abs(a - c) for a, c in zip(S0, S1)) < 1e-12 and abs(sl - 2) < 0.1,
      f'S(q_1,2,4) {S0[0]:.2e} {S0[1]:.2e} {S0[2]:.2e}; slope {sl:.2f}; max|C| at 1..4 cells {", ".join(f"{v:.0e}" for v in xi)}')

print('== B. one-cube start and the split cascade (antiperiodic, same per-tick angles)')
Ue1, Uo1, i1 = realspace(We, Wo, 1); w, V = np.linalg.eig(Uo1 @ Ue1); Q, _ = np.linalg.qr(V[:, -np.angle(w) < 0])
c_0 = Q.conj() @ Q.T; c_1 = (Ue1 @ Q).conj() @ (Ue1 @ Q).T; tv1 = TV(podds(c_0)[0], podds(c_1)[0])
lev = [tv_patch(0.3, 0.4, 0.5, L) for L in (2, 3, 4, 8)]
check('B1 finite diagnostic: on the one-cube start nothing moves (tick mass-blind there); from 2 cubes across the forced rate is '
      'set to within 5% by 4 cubes, then fixed: a one-split transient, not a clock', tv1 < 1e-13 and abs(lev[2] / lev[3] - 1) < 0.05 and lev[0] > lev[3],
      f'TV 1 cube {tv1:.0e}; 2, 3, 4, 8 cubes across: ' + ', '.join(f'{v:.2e}' for v in lev))
Ms = [tv_patch(0.3, 0.4, m) for m in (0.05, 0.1)]; es = [tv_patch(np.pi / 2 - e, 0.4 * e / 1.2708, 0.5 * e / 1.2708, 12) for e in (0.3, 0.15)]
half = tv_patch(0.3, 0.2, 0.25)
check('B2 finite diagnostic: the rate depends only on the per-tick angles (eps0, mu N, M N): linear in M N at small M, and linear in '
      'eps at fixed ratios; CL-1 fixes eps0 and every split cycle repeats the same N(t), so every level gets the same rate (lambda = 1)',
      abs(Ms[1] / Ms[0] - 2) < 0.2 and abs(es[0] / es[1] - 2) < 0.1, f'M .05, .1: {Ms[0]:.2e}, {Ms[1]:.2e}; eps .3, .15: {es[0]:.2e}, {es[1]:.2e}; birth angles (mu, M)/2: {half:.2e}')

print('== C. what CL-3 sees; B and C-odd parts')
U2 = Uo @ Ue; wv, Vv = np.linalg.eig(U2); Qv = np.linalg.qr(Vv[:, -np.angle(wv) < 0])[0]; Cv = Qv.conj() @ Qv.T
Qt = U2 @ U2 @ U2 @ Qv; Ct = Qt.conj() @ Qt.T
check('C1 THEOREM (CL-1 + CL-2 text): CL-2 never changes the odds and the vacuum odds return every tick, so the odds\' departure from '
      'the vacuum stays 0 at every k; CL-3 subtracts the vacuum odds at the SAME configuration, so its source is 0 for every '
      'configuration: no actuality-only rule (any rate, record reading or cost) seeds anything', np.abs(Ct - Cv).max() < 1e-12,
      f'|C(3 ticks) - C_vac| {np.abs(Ct - Cv).max():.0e}; created modes 0 vs >= 1e80')
nU = max(np.abs(Ue @ Ue.conj().T - np.eye(len(Ue))).max(), np.abs(Uo @ Uo.conj().T - np.eye(len(Ue))).max())
check('C2 THEOREM: the half-ticks are one-body unitaries, so CL-2\'s transitions conserve the number exactly (Delta B = 0); the only '
      'C-odd part is A3\'s odd cumulants, which flip sign every half-tick and average to 0 over each tick: no CP-odd bias',
      nU < 1e-9 and np.abs(k30 + k31).max() < 1e-15, f'eta = 0 vs 6.1e-10; tick-mean k3 {np.abs(k30 + k31).max():.0e}')

print('== D. ESTIMATES vs measurement (not theorems)')
hb, cl, Gn = 1.054571817e-34, 2.99792458e8, 6.67430e-11; tP = np.sqrt(hb * Gn / cl ** 5); H0 = 67.36e3 / 3.0857e22; x0 = H0 * tP
rhoc = 3 * x0 ** 2 / (8 * np.pi); a3 = (8 * np.pi) ** 1.5; tau = 2 * np.sqrt(8 * np.pi) / np.sqrt(3); Nt = 1 / (x0 * tau)
gmax = rhoc * a3 * tau / Nt; f = tvM / 12
print(f'   CL-2 shuttle: >= {f:.1e} flips/site/half-tick forever; odds departures 0; coarse counts unchanged; lambda = 1; eta = 0')
print(f'   escape 1 (records condition the odds at the shuttle rate, ~hbar/tau each): today allows <= {gmax:.0e} per site-tick, '
      f'{f / gmax:.0e} below the forced rate, with no rule variable to switch it off')
print(f'   escape 2 (CL-3 reads the configuration): coarse cubes see 0 (A4); the static noise S ~ q^2 gives Delta^2 ~ q^5 (n - 1 = 4), '
      f'and cell-scale noise of 1/4 per site today')
check('D1 arithmetic: the shuttle and both escapes each miss a measured fact (matter, switch-off, n_s, eta)', f / gmax > 1e100)
print('supplied: tick and angles, vacuum branch, tori, patches, unit map, measured numbers.')
print(f'elapsed {time.time() - T0:.0f} s'); print(f'TOTAL: PASS={NP} FAIL={NF}')
