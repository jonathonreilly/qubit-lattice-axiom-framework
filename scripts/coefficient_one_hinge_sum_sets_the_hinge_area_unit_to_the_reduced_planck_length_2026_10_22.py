AUDIT_INPUT_PATHS = ('docs/COEFFICIENT_ONE_HINGE_SUM_SETS_THE_HINGE_AREA_UNIT_TO_THE_REDUCED_PLANCK_LENGTH_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""unit-map: which length is sqrt(8 pi G hbar / c^3) in the rules, and what the factor-2 changes.

CL-3's total phase carries "minus the sum over hinges of area times deficit ... in fixed proper units"
with coefficient one.  This runner (i) checks the hinge-curvature identity int sqrt(g) R = 2 sum A delta
that turns that coefficient into 8 pi G hbar = u^2 (u = the unit the hinge areas are counted in),
(ii) shows the rest of the rule text (lapse clause, block scaling) does not fix u, and
(iii) recomputes every register number that moves when u is the cell rung L (reading B) instead of
half of it (reading A: u = site spacing, cell = 2 sites), against the measured bound each faces.
Tags: [T] theorem (exact, checked), [D] finite diagnostic, [E] estimate vs measurement, [B] bookkeeping.
Self-contained: numpy, scipy, sympy.
"""
import math, time, signal
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

AUDIT_TIMEOUT_SEC = 60
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(AUDIT_TIMEOUT_SEC)
T0 = time.time()
NP = NF = 0


def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))


rng = np.random.default_rng(7)
print('== A. the coefficient of the hinge sum')
# A1: int sqrt(g) R over a piecewise-flat surface = 2 x (sum of vertex deficits): Gauss-Bonnet (R = 2K) on
# random convex polyhedra.  The hinge is a codimension-2 cone; its transverse integral is 2 delta, times the
# hinge's (d-2)-volume A in any dimension, so int sqrt(g) R = 2 sum_h A_h delta_h.
errs = []
for trial in range(20):
    P = rng.normal(size=(40 + trial, 3)); P /= np.linalg.norm(P, axis=1)[:, None]
    P *= rng.uniform(0.7, 1.3, size=(len(P), 1))
    hull = ConvexHull(P); ang = np.zeros(len(P))
    for s in hull.simplices:
        for k in range(3):
            o, p, q = P[s[k]], P[s[(k + 1) % 3]], P[s[(k + 2) % 3]]
            u, v = p - o, q - o
            ang[s[k]] += math.acos(np.clip(u @ v / np.linalg.norm(u) / np.linalg.norm(v), -1, 1))
    used = np.unique(hull.simplices)
    errs.append(abs((2 * np.pi - ang[used]).sum() - 4 * np.pi))
check('A1 [T] hinge identity: on 20 random convex polyhedra the vertex deficits sum to 4 pi = (1/2) int sqrt(g) R, '
      'so int sqrt(g) R = 2 sum_h A_h delta_h (the codim-2 cone; coupling-G (PR #9856) found the same 1/2 per cell on '
      'Kuhn and coned-D4 4D carriers)', max(errs) < 1e-10, f'max |sum delta - 4 pi| = {max(errs):.1e}')
# A2: phase = -(1/u^2) sum A delta must equal S_EH/hbar = (1/(16 pi G hbar)) int sqrt(-g) R
u, G, hb, SAd = sp.symbols('u G hbar SAd', positive=True)
sol = sp.solve(sp.Eq(SAd / u ** 2, 2 * SAd / (16 * sp.pi * G * hb)), u)
check('A2 [T] coefficient one in the total phase <=> u^2 = 8 pi G hbar / c^3: the hinge area unit u is the reduced '
      'Planck length sqrt(8 pi) l_P = 5.013 l_P, whatever lattice length u is', sp.simplify(sol[0] - sp.sqrt(8 * sp.pi * G * hb)) == 0,
      f'u = {sol[0]}')
# A3: block triangulation scaled by b: areas x b^2, dihedrals fixed -> Lambda_b = b^2 Lambda_cell, G unchanged
X = rng.normal(size=(4, 3))
def tet_data(Y):
    fa, dih = [], []
    for i in range(4):
        f = [j for j in range(4) if j != i]; a, b_, c = Y[f]; fa.append(0.5 * np.linalg.norm(np.cross(b_ - a, c - a)))
    for i in range(4):
        for j in range(i + 1, 4):
            k, l = [m for m in range(4) if m not in (i, j)]
            e = Y[j] - Y[i]; e /= np.linalg.norm(e)
            n1 = (Y[k] - Y[i]) - ((Y[k] - Y[i]) @ e) * e; n2 = (Y[l] - Y[i]) - ((Y[l] - Y[i]) @ e) * e
            dih.append(math.acos(n1 @ n2 / np.linalg.norm(n1) / np.linalg.norm(n2)))
    return np.array(fa), np.array(dih)
fa1, d1 = tet_data(X); fa7, d7 = tet_data(7 * X)
check('A3 [T] scaling: areas go as b^2 and dihedral angles (deficits) are scale-free, so block edges of b_e cells have '
      'stiffness Lambda_b = b_e^2 Lambda_cell with the same G: G fixes u, not the block (edge-block C1)',
      np.allclose(fa7 / fa1, 49) and np.allclose(d7, d1), f'area ratio {np.mean(fa7 / fa1):.6f}, dihedral change {abs(d7 - d1).max():.1e}')
# A4: the lapse clause sqrt3 N rms(sqrt(gamma^ii)) = sin eps0 is invariant under a change of length unit
lam, N, g = sp.symbols('lambda N g', positive=True)
expr = sp.sqrt(3) * N * sp.sqrt(g); expr2 = sp.sqrt(3) * (N / lam) * sp.sqrt(g * lam ** 2)
check('A4 [T] the lapse clause and the dressed-cone clauses are unit-free (N -> N/lambda, gamma^ii -> lambda^2 gamma^ii): '
      'nothing in CL-1 fixes u; only CL-3\'s "fixed proper units" does, and the text never names the unit',
      sp.simplify(expr - expr2) == 0)

print('== B. the two readings (l_P = 1.616e-35 m, M_P = 1.2209e19 GeV)')
lP, MP, s8 = 1.616255e-35, 1.220890e19, math.sqrt(8 * math.pi)
R = {'A': dict(site=s8, L=2 * s8), 'B': dict(site=s8 / 2, L=s8)}   # lengths in l_P; L = cell rung (cube period)
for k, r in R.items():
    r['Lam'] = r['L'] ** 2 / (8 * math.pi); r['EL'] = MP / r['L']
    print(f"   {k}: u = {'site spacing' if k == 'A' else 'cell rung L'}; site {r['site']:.3f} l_P, rung L {r['L']:.3f} l_P "
          f"({r['L'] * lP:.2e} m), Lambda_cell = L^2/(8 pi G hbar) = {r['Lam']:.0f}, hbar c/L = {r['EL']:.3e} GeV")
check('B1 [B] reading A (u = site, register "Lambda ~ 4", volume-mode, tick-law, predictions) and reading B (u = rung, '
      'the brief\'s l_rung = sqrt(8 pi) l_P) differ by exactly 2 in L and 4 in Lambda_cell; hbar c/L under B is the reduced '
      'Planck mass the particle probes already call the cell scale', abs(R['A']['Lam'] - 4) < 1e-12 and abs(R['B']['Lam'] - 1) < 1e-12
      and abs(R['B']['EL'] - 2.435e18) / 2.435e18 < 1e-3)

print('== C. register numbers that move (A -> B) against measurement')
# C1 edge-block bottom-wall margins: b_min = 22 sigma x s1(Lambda)/(distance), s1 = 0.2 sqrt(4/Lambda)
s1 = {k: 0.2 * math.sqrt(4 / r['Lam']) for k, r in R.items()}
bm = {k: {nm: 21.97 * s1[k] / d for nm, d in (('weak', 0.875), ('J0740', 0.45 - 0.125), ('causal', 0.24 - 0.125))} for k in R}
for k in R:
    print(f"   {k}: one-cell spread {s1[k]:.2f} L; b_e min weak {bm[k]['weak']:.1f}, J0740 core {bm[k]['J0740']:.1f}, causal max {bm[k]['causal']:.1f}")
check('C1 [E] graviton-mass margin (22 zero-point spreads to the floor): b_e >= 5.0 / 13.5 / 38 under A becomes 10.0 / 27 / 76 '
      'under B; the register\'s "10 to 16 cells" is right only for weak fields under B', abs(bm['A']['weak'] - 5.02) < 0.02
      and abs(bm['B']['weak'] / bm['A']['weak'] - 2) < 1e-12 and abs(bm['A']['J0740'] - 13.5) < 0.1)
def sites_per_cell(k, b, eps0):
    sl = s1[k] / b; Dl = math.log2(1 + 22 * sl / 2); s = max(0.85 / math.sin(eps0), 26.3 * b * 0.2 / s1[k])
    return 12 * (4 + Dl) * s / b ** 3, s
pa, sa = sites_per_cell('A', 6, 0.0075); pb, sb = sites_per_cell('B', 10, 0.0075); pbj, _ = sites_per_cell('B', 27, 0.0075)
check('C2 [E] register sites per cell at the weak-field minimum: A b_e 6 (s 158) 39/cell; B b_e 10 (s 132) 7/cell, '
      'b_e 27 (J0740) 0.9/cell: the larger block under B is cheaper per cell (cost ~ 1/b_e^2), so B costs no fit',
      abs(pa - 39.1) < 0.2 and pb < pa and pbj < 1, f'A {pa:.1f}, B {pb:.1f}, B(J0740) {pbj:.2f} sites/cell')
# C3 photon decay threshold k_th = (8/c6)^(1/4) sqrt(m_e M_P/L)
me = 0.51099895e-3
th = {k: [(8 / c) ** 0.25 * math.sqrt(me * MP / r['L']) / 1e6 for c in (0.0833, 0.0208)] for k, r in R.items()}
check('C3 [E] photon decay to e+e- (copy-mass c6 K^2, K per cell): threshold 78 / 110 PeV under A becomes 110 / 156 PeV '
      'under B (x sqrt 2); LHAASO\'s 1.4 PeV tests neither', abs(th['A'][0] - 78) < 1 and min(th['B']) > 1.4,
      f"A {th['A'][0]:.0f}/{th['A'][1]:.0f}, B {th['B'][0]:.0f}/{th['B'][1]:.0f} PeV")
# C4 neutrino v^2 / (cell scale)
v = 246.21965; nu = {k: v ** 2 / r['EL'] * 1e9 for k, r in R.items()}
check('C4 [E] v^2 over the cell scale: 2.5e-5 eV (register) is the B value (A would give 5.0e-5); vs m3 = 0.05 eV '
      'the seesaw shortfall stays > 100 either way', abs(nu['B'] - 2.49e-5) < 1e-7 and 0.05 / nu['A'] > 100,
      f"A {nu['A']:.2e} eV, B {nu['B']:.2e} eV")
# C5 nucleon decay ~ M_cell^4
tp = {k: 5.3e42 * (r['EL'] / 2.435e18) ** 4 for k, r in R.items()}
check('C5 [E] nucleon decay at the cell scale: register 5e42 yr is the B value (proton-theta used M_P/sqrt(8 pi)); '
      'A\'s cell would give 3e41 yr; Super-K 2.4e34 yr is passed by > 1e7 either way', min(tp.values()) / 2.4e34 > 1e7,
      f"A {tp['A']:.1e}, B {tp['B']:.1e} yr")
# C6 graviton cone 0.1 (k L)^2 at 100 Hz
kg = 2 * math.pi * 100 / 2.998e8; cg = {k: 0.1 * (kg * r['L'] * lP) ** 2 for k, r in R.items()}
check('C6 [E] |c_g - 1| ~ 0.1 (k L)^2 at 100 Hz: A 1.2e-80, B 2.9e-81 (register 4e-81); GW170817 allows 1e-15',
      max(cg.values()) < 1e-15, f"A {cg['A']:.1e}, B {cg['B']:.1e}")
# C7 universality of free fall (mu/eps)^2/4 ~ L^2
mic = {'A': 2e-33, 'B': 2e-33 / 4}
check('C7 [E] free-fall spread (mu/eps)^2/4, mu = m x tick ~ L: 2e-33 (A) -> 5e-34 (B) vs MICROSCOPE 3e-15', mic['A'] < 3e-15)
# C8 volume-mode single-cell spread ~ Lambda^-1/2, Hubble-patch spread at recombination
r1 = {k: 0.1794 * math.sqrt(4 / r['Lam']) for k, r in R.items()}
Ncell = {k: (5.7e21 / (r['L'] * lP)) ** 3 for k, r in R.items()}
ind = {k: r1[k] / math.sqrt(Ncell[k]) for k in R}; cor = {k: r['L'] * lP / 5.7e21 for k, r in R.items()}
check('C8 [E] single-cell classical spread 0.18 (A) -> 0.36 (B): edges are classical only on blocks either way; Hubble '
      'patch at recombination (independent/correlated) 9e-85/3e-56 (A) -> 6e-85/1e-56 (B) vs CMB 1e-5', r1['B'] > 0.3 and max(ind['A'], cor['A']) < 1e-5,
      f"A {r1['A']:.2f}: {ind['A']:.0e}/{cor['A']:.0e}; B {r1['B']:.2f}: {ind['B']:.0e}/{cor['B']:.0e}")
# C9 split keep-up H N < 0.22 per tick, tick T = L sin(eps0)/(sqrt3 c): H_max ~ 1/L, vs the r < 0.036 inflation H
Hmax = {k: 0.22 * math.sqrt(3) / (math.sin(0.0375) * r['L']) for k, r in R.items()}   # in Planck units (1/t_P)
Hinf = 2.4e-5 / s8                     # H/M_P at the r < 0.036 bound (as odds-ramp)
check('C9 [E] splits keep up for H below 0.22/tick: H_max 1.0 (A) -> 2.0 (B) inverse Planck times at eps0 0.0375, '
      '>1e4 above the r < 0.036 inflation scale either way', min(Hmax.values()) / Hinf > 1e4,
      f"A {Hmax['A']:.2f}, B {Hmax['B']:.2f} t_P^-1")

print('== D. probe census (lengths read from runners, in units of sqrt(8 pi) l_P)')
census = {  # cell/cube length used, /sqrt(8 pi) l_P (1 = B-cell or A-site; 2 = A-cube; 4 = A coarse cell)
    'volume-mode lc': 2, 'tick-law Lc': 2, 'predictions aL': 2, 'links-metric aL': 2, 'photon-placement Lb': 2,
    'kasner-crush l0c': 2, 'crush-bounce l0': 2, 'inhomog-volume lc': 2, 'momentum-constraint lr': 2, 'hop-recheck lr': 2,
    'sea-split lf': 2, 'one-cell-start lf': 2, 'induced-response blk': 2, 'matter-sees-geometry blk': 2, 'proper-couplings': 2,
    'one-principle': 2, 'odds-ramp lcP (coarse)': 4, 'one-cell-start lc (coarse)': 4,
    'qcrush Lr': 1, 'hanging-nodes L': 1, 'skew-light l': 1, 'edge-source aL': 1, 'self-gravity aL': 1, 'octree-field a': 1,
    'proton-theta 1/a': 1, 'neutrino/ew M_c': 1, 'coupling-blocks MBAR': 1, 'running-tilt acell': 1, 'act-tilt acell': 1,
    'source-reading a': 1, 'lambda-split a_P (site)': 1, 'cosmology aS (site, tick 2a)': 1, 'dark-matter unit (site)': 1}
n2 = sum(v == 2 for v in census.values()); n1 = sum(v == 1 for v in census.values()); n4 = sum(v == 4 for v in census.values())
print(f"   cube = 2 sqrt(8 pi) l_P (A): {n2}; length sqrt(8 pi) l_P as cell or site (B-cell / A-site, ambiguous): {n1}; coarse 4: {n4}")
check('D1 [B] the probes split, and the sqrt(8 pi) l_P length is called a site in some runners (cosmology, lambda-split, '
      'dark-matter: tick 2a/sqrt3) and a cell in others (qcrush, edge-source, proton-theta): no single convention is in use',
      n2 > 0 and n1 > 0)
print('supplied: the radian (phase = deficit in radians), the codim-2 cone identity in 4D (cited from coupling-G), '
      's1 = 0.2 at Lambda 4 and the 22-sigma margin (edge-block), c6 (links-metric), 5.3e42 yr (proton-theta).')
print(f'elapsed {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
