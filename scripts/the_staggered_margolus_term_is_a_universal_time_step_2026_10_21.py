AUDIT_INPUT_PATHS = ('docs/THE_STAGGERED_MARGOLUS_TERM_IS_A_UNIVERSAL_TIME_STEP_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""b-compaction: what the staggered term b is for, and a bare-metal pass over CL-1..CL-6.

Supplied model: the CL-3 Margolus tick on Z^3 (one fermion mode per site, spin-3/2 edge hop W on 2x2x2 cubes,
two partitions offset by (1,1,1)), species half-ticks V(a) = cos(a) W + i sin(a), a = mu/2 +- b; the block-lattice
Yee leapfrog for links (E on even-block links, B on odd, Courant C).  Finite diagnostics; no physical reading.

Sections
 1. the speed claim: cos w = A S - (cos2b - cos mu)/2, c^2 = (A/3)(mu/sin mu), so c = cos(b)/sqrt3 as mu -> 0
 2. exact rewrite: V(mu/2+b) = i exp(-i(eps-mu/2)W), V(mu/2-b) = -i exp(+i(eps+mu/2)W), eps = pi/2 - b
 3. links: Yee band sin^2(w/2) = C^2 sum sin^2(K/2) equals the b-band at every K iff C = cos(b)/sqrt3;
    C = 1/sqrt3 (b = 0) is a Jordan block at K = R; universal b closes photon decay, per-species b opens it
 4. the symmetric-stress clause: per-species b has no common metric; universal b leaves only O(mu^2)
 5. quasi-energy arcs: excitation range [2mu, 2pi - 4b]; pi-cone pair at R is -4b mod 2pi; two-pair wrap open iff b <= pi/4
 6. CL-1 and CL-3 clauses that are theorems (bond partition, symmetry group, face flux)
 7. arithmetic with measured numbers (ESTIMATES, separated)
"""
import itertools, time, sys
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 90
T0 = time.time()
NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

rng = np.random.default_rng(20261021)
r3 = np.sqrt(3.0)
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
I8 = np.eye(8)
def V(a): return np.cos(a) * W + 1j * np.sin(a) * I8
def tick(K, Ve, Vo):
    D = np.exp(1j * (np.atleast_2d(K) @ C8.T)); return (D.conj()[:, :, None] * Vo[None] * D[:, None, :]) @ Ve[None]
def qe(U): return -np.angle(np.linalg.eigvals(U))          # quasi-energies in (-pi, pi]
def wband(K, mu, b): return np.abs(qe(tick(K, V(mu / 2 + b), V(mu / 2 - b))))
def Sof(K): return np.cos(np.atleast_2d(K)).sum(1) / 3
def w_f(K, mu, b):                                           # analytic fermion band (checked in 1a)
    A = (np.cos(2 * b) + np.cos(mu)) / 2
    return np.arccos(np.clip(A * Sof(K) - (np.cos(2 * b) - np.cos(mu)) / 2, -1, 1))
def w_g(K, Cn):                                              # analytic Yee band (checked in 3a)
    return 2 * np.arcsin(np.clip(Cn * np.sqrt((np.sin(np.atleast_2d(K) / 2) ** 2).sum(1)), 0, 1))

print('== 1. the limiting-speed claim')
KR = rng.uniform(-np.pi, np.pi, (1500, 3)); worst = 0
for mu, b in ((0.0, 0.0), (0.05, 0.6), (0.3, 0.1), (0.2, 1.2), (0.01, 7.3e-3)):
    wn = np.sort(wband(KR, mu, b), 1); worst = max(worst, np.abs(wn - w_f(KR, mu, b)[:, None]).max())
check('1a all 8 bands obey cos w = A S - (cos2b - cos mu)/2, A = (cos2b + cos mu)/2 (rederived: two-reflection 2x2 blocks, det = 1)', worst < 1e-9, f'{worst:.1e}')
devs = []
for mu, b in ((0.0, 0.0), (0.0, 0.3), (0.0, 1.0), (0.1, 0.6), (0.4, 0.2)):
    for n in (np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.ones(3) / r3):
        h = 1e-3; w2 = [np.sort(wband(k * n, mu, b))[0, -1] ** 2 for k in (h, 2 * h)]
        slope = (4 * (w2[0] - mu**2) / h**2 - (w2[1] - mu**2) / (4 * h**2)) / 3
        A = (np.cos(2 * b) + np.cos(mu)) / 2; pred = A / 3 * (mu / np.sin(mu) if mu else 1.0)
        devs.append(abs(slope - pred) / pred)
check('1b c^2 = d(w^2)/d(K^2) at K = 0 equals (A/3)(mu/sin mu) on axis/face/body; mu -> 0 gives c = cos(b)/sqrt3 (precision-qed claim confirmed)', max(devs) < 1e-5,
      f'max rel dev {max(devs):.1e}; c(b=0.3)/c(0) = {np.cos(0.3):.6f}')

print('== 2. exact rewrite of the staggered half-ticks as one step eps = pi/2 - b')
err = 0
for mu, b in ((0.0, 0.0), (0.05, 0.6), (0.3, 1.4), (0.2, -0.4)):
    e = np.pi / 2 - b
    err = max(err, np.abs(V(mu / 2 + b) - 1j * expm(-1j * (e - mu / 2) * W)).max(), np.abs(V(mu / 2 - b) + 1j * expm(1j * (e + mu / 2) * W)).max())
check('2a V(mu/2+b) = i exp(-i(eps-mu/2)W) and V(mu/2-b) = -i exp(+i(eps+mu/2)W): the tick is exactly exp(+i delta_o W_o) exp(-i delta_e W_e)', err < 1e-12, f'{err:.1e}')
Ks = rng.uniform(-0.05, 0.05, (200, 3)); e = 1e-3; mu = 4e-4
D = np.exp(1j * (Ks @ C8.T)); Wo = D.conj()[:, :, None] * W[None] * D[:, None, :]
Heff = e * (W[None] - Wo) - (mu / 2) * (W[None] + Wo)
dev = max(np.abs(np.sort(np.linalg.eigvalsh(Heff[i])) - np.sort(qe(tick(Ks[i], V(mu / 2 + np.pi / 2 - e), V(mu / 2 - np.pi / 2 + e)))[0])).max() for i in range(200))
check('2b b -> pi/2 is the continuous-time limit: quasi-energies -> eigenvalues of eps(W_e - W_o) - (mu/2)(W_e + W_o) (error O(eps^2))', dev < 5 * e**2, f'max dev {dev:.1e} at eps = {e}')
wmax = max(wband(np.full(3, np.pi), 0.0, b).max() - (np.pi - 2 * b) for b in (0.1, 0.6, 1.3))
check('2c band top at R is pi - 2b = 2 eps for every b: the step eps sets the bandwidth', abs(wmax) < 1e-12, f'{wmax:.1e}')

print('== 3. links: can the link update carry b?')
def curl(K):
    d = 2j * np.sin(K / 2); return np.array([[0, -d[2], d[1]], [d[2], 0, -d[0]], [-d[1], d[0], 0]])
def yee(K, Cn):
    X = curl(K); I = np.eye(3); return np.block([[I, Cn * X], [0 * I, I]]) @ np.block([[I, 0 * I], [-Cn * X, I]])
dv = 0; dvb = 0
for K in KR[:800]:
    for b in (0.0, 0.4, 1.1):
        ph = np.sort(np.abs(np.angle(np.linalg.eigvals(yee(K, np.cos(b) / r3)))))[2:]
        dv = max(dv, np.abs(ph - w_g(K, np.cos(b) / r3)[0]).max()); dvb = max(dvb, np.abs(ph - w_f(K, 0.0, b)[0]).max())
check('3a Yee leapfrog bands: sin^2(w/2) = C^2 sum sin^2(K_i/2) = (3C^2/2)(1 - S) (both transverse polarisations)', dv < 1e-9, f'{dv:.1e}')
check('3b with C = cos(b)/sqrt3 the photon has EXACTLY the (mu = 0, b) fermion band at every K: one universal b is carried by the Courant number', dvb < 1e-9,
      f'{dvb:.1e} over 800 K x 3 b')
I6 = np.eye(6); Mc = yee(np.full(3, np.pi), 1 / r3); Mb = yee(np.full(3, np.pi), np.cos(0.3) / r3)
jord = np.linalg.norm((Mc + I6) @ (Mc - I6)); diag_ok = np.linalg.matrix_rank(np.linalg.eig(Mb)[1], tol=1e-8) == 6
gc = np.linalg.norm(np.linalg.matrix_power(Mc, 1000)) / np.linalg.norm(np.linalg.matrix_power(Mc, 100))
gb = max(np.linalg.norm(np.linalg.matrix_power(Mb, n)) for n in (100, 300, 1000)) / np.linalg.norm(Mb)
check('3c b = 0 photon (C = 1/sqrt3) is a Jordan block at R (norm grows linearly in ticks); any b > 0 makes it diagonalisable and bounded', jord > 1 and diag_ok and gc > 5 and gb < 3,
      f'|M^1000|/|M^100| = {gc:.2f} (b=0); max_n |M^n|/|M| = {gb:.3f} (b=0.3)')
lhs = 1 - np.cos(w_f(KR, 0.05, 0.6)); rhs = 1 - np.cos(w_g(KR, np.cos(0.6) / r3)) + (1 - np.cos(0.05)) * (1 + Sof(KR)) / 2
check('3d identity at the same K: 1 - cos w_e = (1 - cos w_gamma) + (1 - cos mu)(1 + S)/2 (mass is the only difference)', np.abs(lhs - rhs).max() < 1e-12, f'{np.abs(lhs - rhs).max():.1e}')
def decay_margin(mu, be, bg, n=60000, kmax=0.6):
    d = rng.normal(size=(n, 3)); d /= np.linalg.norm(d, axis=1)[:, None]; d[: n // 6] = np.ones(3) / r3
    K = d * rng.uniform(0.01, kmax, n)[:, None]; x = rng.uniform(0.02, 0.98, n)[:, None]
    perp = rng.normal(size=(n, 3)) * rng.choice([0.0, 1e-3, 1e-2], n)[:, None] * np.linalg.norm(K, axis=1)[:, None]
    K1 = x * K + perp; Cg = np.cos(bg) / r3
    return (w_f(K1, mu, be) + w_f(K - K1, mu, be) - w_g(K, Cg)) / w_g(K, Cg)
mins = {b: decay_margin(1e-3, b, b).min() for b in (0.3, 0.9, 1.3)}
check('3e universal b: gamma -> f fbar is closed (min over 60k K, splits; margin > 0) for b = 0.3, 0.9, 1.3', min(mins.values()) > 0,
      'min rel margin ' + ', '.join(f'{v:.1e}' for v in mins.values()))
mo = decay_margin(1e-3, 0.3, 0.0).min()
check('3f per-species b (fermion b = 0.3, photon b = 0): gamma -> f fbar opens (negative margin)', mo < 0, f'min rel margin {mo:.3f}')

print('== 4. the symmetric-stress clause of CL-6')
def alpha(mu, b): A = (np.cos(2 * b) + np.cos(mu)) / 2; return A / 3 * (mu / np.sin(mu) if mu else 1.0)
spread = alpha(0, 0.0) - alpha(0, 0.3)
check('4a species with b = 0 and b = 0.3: massless stresses are symmetric in metrics alpha = 1/3 and cos^2(0.3)/3: no common metric', spread > 1e-2, f'alpha spread {spread:.4f}')
mu = 0.05; b = 0.6; ex = alpha(mu, b) / (np.cos(b) ** 2 / 3) - 1; ap = mu**2 * (1 / 6 - 1 / (4 * np.cos(b) ** 2))
check('4b universal b: the only spread is (alpha_s/alpha_gamma - 1) = mu^2 (1/6 - 1/(4cos^2 b)) + O(mu^4): the clause is exact only for massless sources', abs(ex - ap) < 2e-6,
      f'{ex:.3e} vs {ap:.3e}')

print('== 5. quasi-energy arcs and the pi-cone')
check('5a b = 0: all 8 states at R sit at quasi-energy pi for every mu (massless pi-cone; charge = species number, so it is charged)',
      max(np.abs(np.abs(qe(tick(np.full(3, np.pi), V(m / 2), V(m / 2)))) - np.pi).max() for m in (0.0, 0.1, 0.5)) < 1e-9)
grid = np.stack(np.meshgrid(*[np.linspace(-np.pi, np.pi, 15)] * 3), -1).reshape(-1, 3)
ok = True; info = []
for mu, b in ((0.05, 0.3), (0.05, 1.0), (0.02, 7.3e-3)):
    wb = w_f(grid, mu, b); top = w_f(np.full(3, np.pi), mu, b)[0]
    ok &= abs(wb.min() - mu) < 1e-12 and abs(wb.max() - (np.pi - 2 * b)) < 1e-12 and abs(top - (np.pi - 2 * b)) < 1e-12
    pair = 2 * top - 2 * np.pi
    ok &= abs(pair + 4 * b) < 1e-12; info.append(f'b={b}: pi-pair {pair:+.4f} = -4b')
    near = w_f(np.full(3, np.pi) + rng.normal(size=(500, 3)) * 0.05, mu, b); ok &= near.max() <= top + 1e-12
check('5b upper band fills [mu, pi - 2b] with its global TOP at R; a particle-hole pair at R has quasi-energy 2(pi-2b) = -4b mod 2pi', ok, '; '.join(info))
print('   theorem: one gap at 0 and one at pi bound the same two arcs; filling either arc leaves filled states BELOW the 0-gap and ABOVE')
print('   the pi-gap (or the reverse). Excitations: [2mu, 2pi - 4b] mod 2pi, i.e. the 0-cone at +2mu.. and the pi-cone at -4b.. sit on')
print('   opposite sides of 0. Quasi-energy is conserved only mod 2pi, so a light excitation of 4b + kin and a pi-pair balance.')
tbl = []
for b in (0.0, 7.3e-10, np.pi / 8, np.pi / 4 - 1e-9, np.pi / 4 + 1e-3, 1.0, (np.pi - 0.5) / 2, 1.534):
    tbl.append((b, int(np.ceil(np.pi / (np.pi - 2 * b) - 1e-12))))
check('5c m band-top pairs at R (total momentum 0) wrap to 2pi iff 2m(pi - 2b) >= 2pi: two pairs suffice iff b <= pi/4', tbl[3][1] == 2 and tbl[4][1] == 3,
      'm_min ' + ', '.join(f'b={b:.3g}:{m}' for b, m in tbl))

print('== 6. clauses of CL-1 and CL-3 that are theorems')
L = 6; ok = True
for x in itertools.product(range(L), repeat=3):
    for i in range(3):
        y = list(x); y[i] = (y[i] + 1) % L
        cnt = 0
        for off in (0, 1):
            cube = tuple(((x[k] - off) // 2) % (L // 2) for k in range(3)); cube2 = tuple(((y[k] - off) // 2) % (L // 2) for k in range(3))
            cnt += cube == cube2
        ok &= cnt == 1
check('6a every nearest-neighbour bond lies in exactly one cube of exactly one partition (6^3 torus): CL-1 sentence 2 is a theorem', ok)
cent_e = np.array(list(itertools.product(range(-2, 4, 2), repeat=3))) + 0.5; cent_o = cent_e + 1
def preserves(f):
    ce = {tuple(np.round(f(p), 6)) for p in cent_e}; co = {tuple(np.round(f(p), 6)) for p in cent_o}
    E = {tuple(np.round(p, 6)) for p in np.array(list(itertools.product(range(-8, 9, 2), repeat=3))) + 0.5}
    O = {tuple(np.round(p, 6)) for p in np.array(list(itertools.product(range(-7, 10, 2), repeat=3))) + 0.5}
    return (ce <= E and co <= O) or (ce <= O and co <= E)
trans = [t for t in itertools.product((0, 1), repeat=3) if preserves(lambda p, t=t: p + np.array(t))]
Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1.]])
check('6b translations preserving the pair: 2Z^3 and (1,1,1)+2Z^3 only; a 90 deg turn about a cube centre preserves it, about a site does not',
      trans == [(0, 0, 0), (1, 1, 1)] and preserves(lambda p: Rz @ (p - 0.5) + 0.5) and not preserves(lambda p: Rz @ p), f'translations mod 2: {trans}')
fl = []; ok = True
faces = [[a, b, c, d] for (a, b, c, d) in [(0, 1, 3, 2), (4, 5, 7, 6), (0, 1, 5, 4), (2, 3, 7, 6), (0, 2, 6, 4), (1, 3, 7, 5)]]
def flux(Wm, f): return np.angle(Wm[f[0], f[1]] * Wm[f[1], f[2]] * Wm[f[2], f[3]] * Wm[f[3], f[0]])
fl = [abs(abs(flux(W, f)) - np.pi) for f in faces]
for t in range(300):
    Wr = np.zeros((8, 8), complex)
    for a, b in EDGES:
        if a < b: ph = np.exp(1j * rng.uniform(-np.pi, np.pi)); Wr[a, b] = ph / r3; Wr[b, a] = np.conj(ph) / r3
    if t % 3 == 0:
        g = np.exp(1j * rng.uniform(-np.pi, np.pi, 8)); Wr = np.diag(g) @ W @ np.diag(g.conj())
    allpi = all(abs(abs(flux(Wr, f)) - np.pi) < 1e-9 for f in faces); inv = np.abs(Wr @ Wr - I8).max() < 1e-9
    ok &= allpi == inv
check('6c an equal-edge Hermitian hop squares to 1 iff every face carries phase -1; the spin-3/2 W has it (so the CL-3 phase follows from unitarity, up to gauge)',
      ok and max(fl) < 1e-9, f'W face |flux| - pi: {max(fl):.1e}; 300 random hops consistent')

print('== 7. arithmetic with measured numbers (ESTIMATES, not theorems)')
GeV_tick = 2.109e18      # hbar/tau at b = 0, block = 2a = 10.03 l_P, a = sqrt(8 pi) l_P (precision-qed unit map)
me, Eg = 0.51099895e-3, 1.4e6
dlt = 2 * me**2 / Eg**2; bmax = np.sqrt(2 * dlt)
print(f'   per-species b, photon at 1/sqrt3: LHAASO 1.4 PeV gamma survives => 1 - cos b_e < {dlt:.2e} => b_e < {bmax:.2e}; pi-reading partner 2b hbar/tau < {2 * bmax * GeV_tick:.2e} GeV')
print(f'   same for muon (gamma -> mu mu): b_mu < {np.sqrt(4 * 0.1056584**2 / Eg**2):.1e}; proton: b_p < {np.sqrt(4 * 0.938272**2 / Eg**2):.1e}')
print(f'   universal b: the bound is gone (3b,3e); residual speed offset ~ mu^2/24 = {(2.424e-22)**2 / 24:.1e} (electron)')
M4b = 4 * bmax * GeV_tick
sig = (1 / 137.036) ** 3 / M4b**2 * 0.3894e-27; rate = (1e26) ** 2 * sig * 1e9 * 2.2e31
print(f'   per-species small b (0-reading): e e -> e e + pi-pair + {M4b:.1e} GeV of light quanta is open at any energy; sigma ~ alpha^3/M^2 ~ {sig:.1e} cm^2;')
print(f'   solar core (n_e 1e26/cc, v 1e9 cm/s, 2.2e31 cc): ~{rate:.0e}/s x {M4b:.0e} GeV = {rate * M4b * 1.602e-3:.0e} erg/s vs L_sun 3.8e33 (needs quantised links)')
blk = 1.62e-32; tau = 3.12e-43; t0 = 4.35e17; rho_c = 4.8e-6
rmax = rho_c / (2 * np.pi * GeV_tick * (t0 / tau) / blk**3)
print(f'   wrap events inject 2pi hbar/tau = {2 * np.pi * GeV_tick:.2e} GeV each; keeping the injected density below rho_crit over the age needs')
print(f'   a rate < {rmax:.0e} per cell-tick; at ~alpha per quantum and unit phase space that asks pi/eps >~ {np.log10(1 / rmax) / np.log10(137):.0f} quanta, eps <~ {np.pi / (np.log10(1 / rmax) / np.log10(137)):.3f}')
e25 = 0.25; print(f'   b = (pi - 1/2)/2 (eps = 0.25, the |w| <= 1/2 setting): pi/eps = {np.pi / e25:.1f} -> rate ~ alpha^13 ~ {(1 / 137) ** 13:.0e} per cell-tick: fails the crude bound')
Mpi = 2 * 0.04 / np.sin(0.04) * GeV_tick
print(f'   universal small eps: band-top (pi-cone) states at 2 eps hbar/tau = {Mpi:.2e} GeV (eps-independent); Boltzmann at T = 1.6e16 GeV (r < 0.036 inflation scale): exp(-{Mpi / 1.6e16:.0f})')
sv = np.pi * (1 / 137.036) ** 2 / (2 * bmax * GeV_tick) ** 2 * 1.17e-17
print(f'   normal-orientation thermal relic at M = {2 * bmax * GeV_tick:.1e} GeV: sigma v ~ pi alpha^2/M^2 = {sv:.1e} cm^3/s -> Omega h^2 ~ {0.1 * 3e-26 / sv:.0e} if T_RH > M/25')
print('supplied: CL-3 tick and its b, mu; Yee placement of links; Fock filling of one arc (0-reading); quasi-energy = energy x tau; unit map')
print('          a = sqrt(8 pi) l_P; quantised links for the rate estimates; all measured numbers. Rates in section 7 are order-of-magnitude only.')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'TOTAL: PASS={NP} FAIL={NF}')
