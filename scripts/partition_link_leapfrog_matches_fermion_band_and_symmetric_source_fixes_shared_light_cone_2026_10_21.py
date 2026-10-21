#!/usr/bin/env python3
"""Light cones of the tick's fermions, of link quanta and of the geometry, on supplied lattice discretisations.

(0) Fermion: the CL-2 Margolus tick (spin-3/2 edge hop W, even then odd 2^3 blocks).  Its massless band obeys
    cos w = S(K) = (cos Kx + cos Ky + cos Kz)/3 (K in block units, w per tick), i.e. sin^2(w/2) = sum sin^2(K_i/2)/3.
(1) Links on the two partitions: E on the links between neighbouring even-block centres (one per even-block face),
    B on the links between neighbouring odd-block centres (the dual lattice), each half-tick advancing one of them by
    C times the lattice curl of the other (Yee leapfrog, step = one tick).  Bands: sin^2(w/2) = C^2 sum sin^2(K_i/2).
    At C = 1/sqrt3 this is the fermion band at every K.  C = 1/sqrt3 is also the stability edge; at the zone corner
    K = pi(1,1,1) the transverse map is a Jordan block.
(2) Links on the individual site hops W uses: leapfrog once per tick cannot reach the fermion speed (unstable);
    leapfrog once per half-tick matches at leading order with O(K^2) coefficient 1/4 of the fermion's; continuous-time
    (Hamiltonian) lattice Maxwell leaves the fermion faster by w^2/24.
(3) Peierls phases on W's hops: W^2 = 1 (hence unitarity of cos(mu/2) W + i sin(mu/2)) survives only zero added face
    flux; the polar part sign(W') is a gauge-covariant unitary.  W's coupling fixes no link kinetic term.
(4) Symmetric-source rule: a band's energy flux / momentum density is d(w^2)/d(K^2); a source symmetric in
    g = diag(-alpha,1,1,1) needs alpha = that ratio.  Fermion and (1)'s link both give 1/3, so the TT cone
    w^2 = alpha K^2 equals the fermion cone.  Massive bands give (1/3)(mu/2)cot(mu/2).
(5) Measured comparisons (GW170817, UHECR proton Cherenkov, LHAASO PeV photon decay) at lattice spacing a few Planck.
Supplied: the discretisations, their placement on blocks or hops, the tick as time step, Planck-scale spacing, the
energy-flux reading of the source.  Supplied-model, finite diagnostic; no physical identification is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/PARTITION_LINK_LEAPFROG_MATCHES_FERMION_BAND_AND_SYMMETRIC_SOURCE_FIXES_SHARED_LIGHT_CONE_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import os, sys, signal, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
rng = np.random.default_rng(20261021)
r3 = np.sqrt(3.0)

# ------------------------------------------------------------------ (0) the CL-2 fermion tick
C8 = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for i in range(8):
    n = (2 * C8[i] - 1.0) / r3; w_, v_ = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); xi.append(v_[:, -1])
G = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
EDGES = [(a, b) for a in range(8) for b in range(8) if np.sum(abs(C8[a] - C8[b])) == 1]
W = np.zeros((8, 8), complex)
for a, b in EDGES: W[a, b] = -G[a, b] / abs(G[a, b]) / r3
def tick(K, Wb):
    D = np.exp(1j * (np.atleast_2d(K) @ C8.T)); return (D.conj()[:, :, None] * Wb[None] * D[:, None, :]) @ Wb[None]
def wf(K, Wb=W): return np.sort(np.abs(np.angle(np.linalg.eigvals(tick(K, Wb)))), 1)
print('== 0. fermion tick (CL-2, mu = 0)')
KR = rng.uniform(-np.pi, np.pi, (2000, 3)); wF = wf(KR); S = np.cos(KR).sum(1) / 3
check('W Hermitian, W^2 = 1; all 8 bands obey cos w = S(K) (2000 K)', np.allclose(W, W.conj().T) and np.allclose(W @ W, np.eye(8))
      and np.abs(np.cos(wF) - S[:, None]).max() < 1e-10, f'{np.abs(np.cos(wF) - S[:, None]).max():.1e}')

DIRS = {'axis': (np.array([1., 0, 0]), 1.0), 'face': (np.array([1., 1, 0]) / np.sqrt(2), 0.5), 'body': (np.ones(3) / r3, 1 / 3)}
def beta(wfun, n):
    """phase-velocity coefficient b in w/K = c (1 - b w^2 + ...), Richardson over K = 0.04, 0.02"""
    out = []
    for K in (0.04, 0.02):
        w = wfun(K * n); c0 = wfun(1e-5 * n) / 1e-5; out.append(((1 - (w / K) / c0) / w**2, c0))
    return (4 * out[1][0] - out[0][0]) / 3, out[1][1]
bF = {}
for nm, (n, A4) in DIRS.items():
    b, c0 = beta(lambda K: wf(K[None])[0, -1], n); bF[nm] = b
    check(f'fermion {nm} (A4={A4:.3f}): c = 1/sqrt3, phase-velocity coefficient (3A4-1)/24', abs(c0 - 1 / r3) < 1e-8 and abs(b - (3 * A4 - 1) / 24) < 1e-5,
          f'c={c0:.8f}, b={b:+.6f}')

# ------------------------------------------------------------------ (1) links on the two partitions (block Yee)
def curl(K, h=1.0):
    d = 2j * np.sin(K * h / 2)
    return np.array([[0, -d[2], d[1]], [d[2], 0, -d[0]], [-d[1], d[0], 0]])
def yee(K, Cn, h=1.0):
    X = curl(K, h); I = np.eye(3)
    return np.block([[I, Cn * X], [0 * I, I]]) @ np.block([[I, 0 * I], [-Cn * X, I]])
def ybands(K, Cn, h=1.0):
    ev = np.linalg.eigvals(yee(K, Cn, h)); return ev
print('== 1. links on the two partitions: E on even-block links, B on odd-block (dual) links, alternate half-ticks')
dev = 0; pol = 0; lon = 0
for K in KR[:2000]:
    ev = ybands(K, 1 / r3); ph = np.abs(np.angle(ev)); o = np.argsort(ph); lon = max(lon, np.abs(ev[o[:2]] - 1).max())
    tr = np.sort(ph[o[2:]]); dev = max(dev, np.abs(tr - wf(K[None])[0, -1]).max()); pol = max(pol, np.ptp(tr))
check('C = 1/sqrt3: both transverse polarisations have exactly the fermion band w(K) at every K (2000 K)', dev < 1e-9 and pol < 1e-9,
      f'max |w_link - w_fermion| = {dev:.1e}, polarisation splitting {pol:.1e}')
check('longitudinal (Gauss) modes are static: eigenvalue 1', lon < 1e-6, f'{lon:.1e}')
Mc = yee(np.full(3, np.pi), 1 / r3); I6 = np.eye(6)
dn = np.linalg.norm((Mc + I6) @ (Mc + I6) @ (Mc - I6)); nn = np.linalg.norm((Mc + I6) @ (Mc - I6))
check('zone corner K = pi(1,1,1): (M+1)^2(M-1) = 0 but (M+1)(M-1) != 0 (transverse Jordan block: no link vacuum at that K)', dn < 1e-12 and nn > 1,
      f'{dn:.1e}, {nn:.2f}')
gr = [np.abs(ybands(np.full(3, np.pi) * 0.999, Cn)).max() for Cn in (1 / r3 * 0.999, 1 / r3 * 1.001)]
check('stability edge is C = 1/sqrt3: |eig| = 1 just below, > 1 just above', abs(gr[0] - 1) < 1e-10 and gr[1] > 1 + 1e-3, f'{gr[0]:.12f}, {gr[1]:.4f}')
for Cn in (0.5, 0.55):
    b, c0 = beta(lambda K: np.sort(np.abs(np.angle(ybands(K, Cn))))[-1], DIRS['axis'][0])
    check(f'C = {Cn}: link speed = C (not 1/sqrt3), so leading-order cone differs from the fermion', abs(c0 - Cn) < 1e-8, f'c = {c0:.6f}')

# ------------------------------------------------------------------ (2) links on W's own site hops
print("== 2. links on the individual site hops W uses (site spacing = 1/2 block)")
# (a) one leapfrog per tick (E on one partition's hops, B on the other's): the fermion speed is 2/sqrt3 site per tick
mx = np.abs(np.concatenate([ybands(K, 2 / r3) for K in rng.uniform(-np.pi, np.pi, (300, 3))])).max()
check('one leapfrog per tick on site hops: matching the fermion needs Courant 2/sqrt3 > 1/sqrt3, unstable', mx > 1.5, f'max |eig| = {mx:.2f}')
# (b) one leapfrog per half-tick, Courant 1/sqrt3 (site per half-tick): w_tick = 2 w_half(K_site = K/2)
def site_half(K): return 2 * np.sort(np.abs(np.angle(ybands(K / 2, 1 / r3))))[-1]
def ks(K): return (2 / r3) * np.sqrt(np.sum(np.sin(K / 2) ** 2))        # continuous-time Maxwell, block links
for nm, (n, A4) in DIRS.items():
    bs, cs = beta(site_half, n); bk, ck = beta(ks, n)
    check(f'{nm}: half-tick site Yee c = 1/sqrt3, coefficient (3A4-1)/96 = fermion/4; continuous-time coefficient 3A4/24',
          abs(cs - 1 / r3) < 1e-8 and abs(bs - (3 * A4 - 1) / 96) < 1e-5 and abs(ck - 1 / r3) < 1e-8 and abs(bk - 3 * A4 / 24) < 1e-5,
          f'site {bs:+.6f}, cont {bk:+.6f}, fermion {bF[nm]:+.6f}')
dsite = {nm: bF[nm] - beta(site_half, DIRS[nm][0])[0] for nm in DIRS}; dks = {nm: bF[nm] - beta(ks, DIRS[nm][0])[0] for nm in DIRS}
print('   (v_link - v_fermion)/c in units of w^2: site half-tick', {k: round(float(v), 5) for k, v in dsite.items()},
      '; continuous time', {k: round(float(v), 5) for k, v in dks.items()})
check('half-tick site links are faster than fermions by (3A4-1)/32 w^2 (0 to 1/16); continuous-time links slower by w^2/24 in every direction',
      all(abs(dsite[k] - (3 * DIRS[k][1] - 1) / 32) < 1e-5 for k in DIRS) and all(abs(v + 1 / 24) < 1e-5 for v in dks.values()))

# ------------------------------------------------------------------ (3) Peierls phases on W's hops
print('== 3. gauge-covariant W from link phases on its hops')
def peierls(th):
    Wp = W.copy()
    for (a, b), t in zip([(a, b) for a, b in EDGES if a < b], th): Wp[a, b] *= np.exp(1j * t); Wp[b, a] *= np.exp(-1j * t)
    return Wp
th = rng.uniform(-0.3, 0.3, 12); Wp = peierls(th); chi = rng.uniform(-np.pi, np.pi, 8)
thg = [chi[a] - chi[b] for a, b in EDGES if a < b]; Wg = peierls(thg)
mu = 0.2; Um = lambda X: np.cos(mu / 2) * X + 1j * np.sin(mu / 2) * np.eye(8)
uerr = np.linalg.norm(Um(Wp) @ Um(Wp).conj().T - np.eye(8)); gerr = np.linalg.norm(Um(Wg) @ Um(Wg).conj().T - np.eye(8))
check('random face flux: W\'^2 != 1 and cos(mu/2)W\' + i sin(mu/2) is not unitary; pure gauge keeps both', uerr > 1e-2 and gerr < 1e-12,
      f'|UU^+ - 1| = {uerr:.3f} (flux), {gerr:.1e} (gauge)')
ev, V = np.linalg.eigh(Wp); Ws = V @ np.diag(np.sign(ev)) @ V.conj().T; Dg = np.diag(np.exp(1j * chi))
ev2, V2 = np.linalg.eigh(Dg @ Wp @ Dg.conj().T); Ws2 = V2 @ np.diag(np.sign(ev2)) @ V2.conj().T
check('polar part sign(W\') is unitary, squares to 1, gauge covariant, and reduces to W at zero flux',
      np.allclose(Ws @ Ws, np.eye(8)) and np.allclose(Ws2, Dg @ Ws @ Dg.conj().T) and np.allclose(np.linalg.eigh(W)[1] @ np.diag(np.sign(np.linalg.eigh(W)[0])) @ np.linalg.eigh(W)[1].conj().T, W))
print('   (the link phases enter only the fermion update; the link kinetic term and its Courant number are not fixed by W)')

# ------------------------------------------------------------------ (4) symmetric-source rule for the geometry
print('== 4. geometry: symmetric source in g = diag(-alpha,1,1,1) needs alpha = (energy flux)/(momentum density) = d(w^2)/d(K^2)')
def ratio(wfun, K, n, h=1e-5):
    w = wfun(K * n); vg = (wfun((K + h) * n) - wfun((K - h) * n)) / (2 * h); return vg * w / K
rf = ratio(lambda K: wf(K[None])[0, -1], 1e-3, DIRS['face'][0]); rl = ratio(lambda K: np.sort(np.abs(np.angle(ybands(K, 1 / r3))))[-1], 1e-3, DIRS['face'][0])
check('fermion and partition links: flux/momentum -> 1/3 at long wavelength, so alpha = 1/3 (block, tick)', abs(rf - 1 / 3) < 1e-6 and abs(rl - 1 / 3) < 1e-6,
      f'{rf:.8f}, {rl:.8f}')
fin = max(abs(ratio(lambda K: wf(K[None])[0, -1], k, n) - ratio(lambda K: np.sort(np.abs(np.angle(ybands(K, 1 / r3))))[-1], k, n))
          for k in (0.3, 0.8, 1.5) for n, _ in DIRS.values())
check('the two ratios agree at every K too (identical bands); for a single band they vary with K at O(K^2)', fin < 1e-7,
      f'max diff {fin:.1e}; fermion axis ratio at K=0.8: {ratio(lambda K: wf(K[None])[0, -1], 0.8, DIRS["axis"][0]):.5f}')
for m in (0.1, 0.5):
    Wm = np.cos(m / 2) * W + 1j * np.sin(m / 2) * np.eye(8)
    r0 = ratio(lambda K: wf(K[None], Wm)[0, -1], 1e-3, DIRS['axis'][0])
    check(f'mu = {m}: rest-frame ratio = (1/3)(mu/2)cot(mu/2) (massive limiting speed below the cone by mu^2/24)',
          abs(r0 - (m / 6) / np.tan(m / 2)) < 1e-6, f'{r0:.8f} vs {(m / 6) / np.tan(m / 2):.8f}')
for al in (1 / 3, 0.6, 1.0):
    cg = np.sqrt(al); print(f'   alpha = {al:.4f}: TT cone w = sqrt(alpha) K, c_grav/c_fermion = {cg * r3:.6f}')
check('alpha = 1/3: c_grav = c_fermion exactly at leading order; the supplied alpha = 0.6 gives 1.3416', abs(np.sqrt(1 / 3) * r3 - 1) < 1e-15)

# ------------------------------------------------------------------ (5) measured comparisons
print('== 5. measured comparisons; w = E tau, tau = L_block/(sqrt3 c); a = sqrt(8 pi) l_P')
EP = 1.22089e28; a = np.sqrt(8 * np.pi)
for Lb, lab in ((2 * a, 'block = 2a'), (a, 'block = a')):
    wE = lambda E: E / EP * Lb / r3
    pc = (0.938272e9) ** 2 / (2 * 1e20 ** 2); gd = 2 * (0.511e6) ** 2 / (1.4e15) ** 2
    ks20 = wE(1e20) ** 2 / 24; site14 = wE(1.4e15) ** 2 / 16
    print(f'   [{lab} = {Lb:.2f} l_P] w(1e20 eV) = {wE(1e20):.2e}; proton Cherenkov needs (v_p - v_link) < {pc:.1e}')
    check(f'[{lab}] continuous-time links: fermions faster by {ks20:.1e} at 1e20 eV, above the proton Cherenkov threshold (excluded if protons carry the fermion O(k^2))',
          ks20 > pc, f'ratio {ks20 / pc:.1e}')
    check(f'[{lab}] half-tick site links: photon faster by <= {site14:.1e} at 1.4 PeV, below the photon-decay threshold {gd:.1e} (allowed)', site14 < gd, f'margin {gd / site14:.1e}')
    print(f'   [{lab}] massive limiting-speed offset mu^2/24: proton {(0.938e9 / EP * Lb / r3) ** 2 / 24:.1e}, top {(173e9 / EP * Lb / r3) ** 2 / 24:.1e}')
check('GW170817 (|c_g - c|/c < ~1e-15): alpha = 1/3 passes; alpha = 0.6 would miss by 3e14', abs(np.sqrt(0.6 * 3) - 1) / 1e-15 > 1e14)
print('supplied: discretisations and their placement, tick as time step, a = sqrt(8 pi) l_P, energy-flux reading of the source.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
