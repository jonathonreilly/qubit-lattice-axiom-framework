#!/usr/bin/env python3
"""skew-light: photon-gravity results on CL-3's skew-loop plaquettes (registers on site bonds, even -> odd centre).
Gaussian / large-S model of the registers. Supplied model, finite diagnostics; numpy + sympy; no Fock space.

Model. Centres = body-centred lattice (primitive: one centre, four bonds d in D4); register A_t on bond t; the six skew loops
through each bond (diagonals along two axes) with area vector A_p = (1/2) d02 x d13 = +-2 e_c. Lagrangian per primitive cell
  L = 1/2 Et^T Me Et - 1/2 A^T K A,  Et = dA/dt - X A,  (X A)_t = (beta x s_t) . B_t,  B_t = (1/2) sum_{p ∋ t} A_p Phi_p / |A_p|^2
(the electric plaquette taken along the slice normal, B_t read by the site from its six loops).
LITERAL reading of CL-3 ("each loop read in proper area", Wilson weight = 4-volume share / proper area^2):
  Me = diag u_t, u_t = (sqrt(g)/N)/(s^T g s)    [time-space plaquette: area N dt |s|_g]
  K  = sum_p w_p Phi_p^* Phi_p, w_p = (1/6)(N/sqrt(g))/(Ahat^T g^-1 Ahat)   [proper area^2 = det g * A^T g^-1 A]
SITE-HODGE reading (proposal): add to Me, at each centre (half at each end), the block S D_E S^T/16 with D_E = eps_t - S^T Me S,
  and to K the site term (1/4) sum_t B_t^dag D_B B_t with D_B = nu_t - sum_p w_p A_p A_p^T, where the covariant targets are
  eps_t = (4/3)(sqrt(g)/N) g^-1, nu_t = (4/3)(N/sqrt(g)) g  (3+1 split of -1/4 sqrt(-g) F.F). Flat cell: no change.
Target cone (null cone of the cell): (w + beta.k)^2 = N^2 k^T g^-1 k.
"""
import itertools, math, os, signal, time
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import sympy as sp

T0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022)

# ---------------- geometry (inlined from the site-register layout) ----------------
SG = [np.array(s) for s in itertools.product((-1, 1), repeat=3)]; SIDX = {tuple(s): i for i, s in enumerate(SG)}
D4 = [np.array(d) for d in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1))]; DIDX = {tuple(d): i for i, d in enumerate(D4)}
S = np.array(D4, float)                                            # 4 x 3, S^T S = 4 I
def is_even(v): return all(c % 2 == 0 for c in v)
def skew_loops_prim():
    out = {}
    for start in (np.zeros(3, int), np.ones(3, int)):
        for ss in itertools.product(range(8), repeat=3):
            st = [SG[i] for i in ss]; s4 = -(st[0] + st[1] + st[2])
            if tuple(s4) not in SIDX: continue
            st.append(s4); vs = [start.copy()]
            for s in st: vs.append(vs[-1] + s)
            if len({tuple(v) for v in vs[:4]}) < 4: continue
            d02 = vs[2] - vs[0]; d13 = vs[3] - vs[1]
            if not (np.count_nonzero(d02) == 1 and np.count_nonzero(d13) == 1): continue
            mn = np.array(min(map(tuple, vs[:4]))); vt = [v - mn for v in vs]
            key = frozenset(frozenset((tuple(vt[j]), tuple(vt[j + 1]))) for j in range(4))
            out.setdefault(key, vt)
    return list(out.values())
LOOPS = skew_loops_prim()
def step_bond(v, s):
    if s[0] == 1: return v, DIDX[tuple(s)], 1
    return v + s, DIDX[tuple(-s)], -1
LOOPINFO = []                                                       # (area vector, [(cell x, type t, sign)])
for vt in LOOPS:
    Ap = 0.5 * np.cross(vt[2] - vt[0], vt[3] - vt[1]).astype(float)
    LOOPINFO.append((Ap, [step_bond(vt[j], vt[j + 1] - vt[j]) for j in range(4)]))
def loop_rows(q):
    C = np.zeros((len(LOOPINFO), 4), complex)
    for i, (Ap, st) in enumerate(LOOPINFO):
        for x, t, sg in st: C[i, t] += sg * np.exp(1j * q @ x)
    return C
def site_B(q):
    """B_t(q): 3 x 4 block per site type t -> stacked (4,3,4): B estimate at the site of bond t from its six loops"""
    C = loop_rows(q); B = np.zeros((4, 3, 4), complex)
    for i, (Ap, st) in enumerate(LOOPINFO):
        for x, t, sg in st: B[t] += 0.5 * np.outer(Ap / (Ap @ Ap), C[i]) * np.exp(-1j * q @ x)
    return B
def gauge(q): return np.array([np.exp(1j * q @ d) - 1 for d in D4])[:, None]

def targets(N, g):
    sg = math.sqrt(np.linalg.det(g)); gi = np.linalg.inv(g)
    return (4 / 3) * (sg / N) * gi, (4 / 3) * (N / sg) * g
def literal_weights(N, g):
    sg = math.sqrt(np.linalg.det(g)); gi = np.linalg.inv(g)
    u = np.array([(sg / N) / (s @ g @ s) for s in S])
    w = np.array([(1 / 6) * (N / sg) / ((Ap / np.linalg.norm(Ap)) @ gi @ (Ap / np.linalg.norm(Ap))) for Ap, _ in LOOPINFO])
    return u, w
def medium(N, g, reading):
    """continuum-limit (q -> 0) electric and magnetic tensors of a reading"""
    u, w = literal_weights(N, g)
    eps = S.T @ np.diag(u) @ S; nu = sum(wi * np.outer(Ap, Ap) for wi, (Ap, _) in zip(w, LOOPINFO))
    if reading == 'site': return targets(N, g)
    return eps, nu
def matrices(q, N, g, beta, reading):
    u, w = literal_weights(N, g); C = loop_rows(q); B = site_B(q)
    Me = np.diag(u).astype(complex); K = C.conj().T @ np.diag(w) @ C
    if reading == 'site':
        et, nt = targets(N, g); DE = et - S.T @ np.diag(u) @ S
        DB = nt - sum(wi * np.outer(Ap, Ap) for wi, (Ap, _) in zip(w, LOOPINFO))
        blk = S @ DE @ S.T / 16; P = np.diag([np.exp(-1j * q @ d) for d in D4])
        Me = Me + 0.5 * blk + 0.5 * P.conj().T @ blk @ P
        K = K + 0.25 * sum(B[t].conj().T @ DB @ B[t] for t in range(4))
    X = np.array([np.cross(beta, S[t]) @ B[t] for t in range(4)])
    return Me, K, X
def omegas(q, N, g, beta, reading):
    Me, K, X = matrices(q, N, g, beta, reading)
    G = np.block([[X, np.linalg.inv(Me)], [-K, -X.conj().T]])
    lam = np.linalg.eigvals(G); w = (1j * lam)
    return w
def photon(q, N, g, beta, reading):
    w = omegas(q, N, g, beta, reading); wr = np.real(w); qn = np.linalg.norm(q)
    sel = np.abs(w) > 1e-4 * qn; phys = wr[sel]                     # drop the gauge pair (a Jordan block at w = 0)
    pos = np.sort(phys[phys > 0])[:2]; neg = np.sort(phys[phys < 0])[::-1][:2]
    return pos, neg, np.max(np.abs(np.imag(w[sel])))
def cone_err(N, g, beta, reading, qm=1e-3, ndir=12, seed=1):
    r = np.random.default_rng(seed); dirs = [np.array([1., 0, 0]), np.array([1., 1, 0]) / 2**.5, np.ones(3) / 3**.5]
    dirs += [v / np.linalg.norm(v) for v in r.normal(size=(ndir, 3))]
    e = 0.0; spl = 0.0; im = 0.0; gi = np.linalg.inv(g)
    for n in dirs:
        q = qm * n; Om = N * math.sqrt(q @ gi @ q); d = -beta @ q
        pos, neg, ii = photon(q, N, g, beta, reading); im = max(im, ii)
        e = max(e, np.max(np.abs(pos - (d + Om))) / Om, np.max(np.abs(neg - (d - Om))) / Om)
        spl = max(spl, abs(pos[1] - pos[0]) / Om)
    return e, spl, im

# ---------------- A. what a per-element reading can represent (exact) ----------------
print('== A. per-element (literal) proper-area reading: representable tensors (exact)')
us = sp.symbols('u0:4', positive=True); Ssym = sp.Matrix([[int(c) for c in d] for d in D4])
EPS = sp.simplify(Ssym.T * sp.diag(*us) * Ssym)
check('A1 [T] every per-bond electric weighting gives eps = sum_s u_s s s^T with EQUAL diagonal entries (the four bonds are body '
      'diagonals): no choice of electric coefficients represents a metric with unequal g^ii', EPS[0, 0] == EPS[1, 1] == EPS[2, 2],
      f'eps_xx = eps_yy = eps_zz = {EPS[0, 0]}; off-diagonals free (u0+u1-u2-u3 etc.)')
ws = sp.symbols('w0:6', positive=True)
NU = sp.zeros(3, 3)
for wi, (Ap, _) in zip(ws, LOOPINFO): NU += wi * sp.Matrix(Ap.astype(int)) * sp.Matrix(Ap.astype(int)).T
check('A2 [T] every per-loop magnetic weighting gives a DIAGONAL nu (each skew loop measures exactly A_p.B with A_p = +-2 e_c): '
      'no choice of magnetic coefficients reads shear g_ij (i != j)', all(NU[i, j] == 0 for i in range(3) for j in range(3) if i != j),
      f'nu = diag({NU[0,0]}, {NU[1,1]}, {NU[2,2]})')
def fresnel(eps, nu, k):
    kx = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    import scipy.linalg as sl
    w2 = np.sort(np.real(sl.eigh(-kx @ nu @ kx, eps, eigvals_only=True)))[1:]
    return np.sqrt(np.abs(w2))
ok3 = True; bad = 0.0
for _ in range(20):
    M = rng.normal(size=(3, 3)); gR = np.eye(3) + 0.3 * (M + M.T) / 2; et, nt = targets(1.2, gR)
    for _k in range(5):
        k = rng.normal(size=3); w = fresnel(et, nt, k); ok3 &= abs(w[1] - w[0]) < 1e-9 * w[0]
    M2 = rng.normal(size=(3, 3)); w = fresnel(et, nt + 0.1 * (M2 + M2.T), rng.normal(size=3)); bad = max(bad, abs(w[1] - w[0]) / w[0])
check('A3 [T] (standard optics) a Maxwell medium is birefringence-free in all directions iff eps is proportional to nu^-1; with A1 and '
      'A2 the literal reading is on the null cone in every direction iff the cell metric is CONFORMALLY FLAT (g = a^2 1), any N, any shift',
      ok3 and bad > 1e-3, f'eps ~ nu^-1: split < 1e-9 (100 random); perturbed nu: split up to {bad:.2f}')
gc = 0.81 * np.eye(3); el, nl = medium(1.3, gc, 'lit'); et, nt = targets(1.3, gc)
check('A4 [T] in a conformal cell the literal weights equal the covariant 3+1 tensors exactly (Wilson V4/area^2 = Hodge)',
      np.allclose(el, et) and np.allclose(nl, nt), f'|eps-eps_t| {np.abs(el-et).max():.0e}, |nu-nu_t| {np.abs(nl-nt).max():.0e}')

# ---------------- B. lattice photon cones (Bloch, q = 1e-3 site units) ----------------
print('== B. lattice photon cone vs the cell null cone; rel. error at |q| = 1e-3 (lattice O(q^2) ~ 1e-7)')
I3 = np.eye(3); cases = {
    'flat': (1.0, I3, np.zeros(3)),
    'conformal+lapse (N 1.3, a .85)': (1.3, 0.85**2 * I3, np.zeros(3)),
    'conformal+shift (.15c)': (1.1, 0.9 * I3, np.array([0.1, -0.08, 0.07])),
    'diag aniso (1.1,.95,1)': (1.0, np.diag([1.1, 0.95, 1.0]), np.zeros(3)),
    'shear g_xy .1': (1.0, I3 + 0.1 * (np.outer([1, 0, 0], [0, 1, 0]) + np.outer([0, 1, 0], [1, 0, 0])), np.zeros(3)),
}
M = rng.normal(size=(3, 3)); cases['generic g+N+shift'] = (1.2, I3 + 0.12 * (M + M.T) / 2, np.array([0.08, 0.05, -0.1]))
R = {}
for name, (N, g, b) in cases.items():
    R[name] = {rd: cone_err(N, g, b, rd) for rd in ('lit', 'site')}
    R[name + '@2q'] = {rd: cone_err(N, g, b, rd, qm=2e-3) for rd in ('lit', 'site')}
okc = all(R[n]['lit'][0] < 1e-6 and R[n + '@2q']['lit'][0] / R[n]['lit'][0] > 3 for n in list(cases)[:3])
check('B1 [T/D] literal reading, conformal cells (strong lapse, shift .15 c): both photon polarisations on the null cone '
      '(w + beta.k)^2 = N^2 k g^-1 k, error O(q^2) only; the shift drags light by exactly -beta (frame dragging at the GR value)',
      okc, '; '.join(f"{n}: {R[n]['lit'][0]:.1e} (x{R[n+'@2q']['lit'][0]/R[n]['lit'][0]:.1f} at 2q)" for n in list(cases)[:3]))
okd = all(R[n]['lit'][0] > 1e-3 for n in list(cases)[3:])
check('B2 [T/D] literal reading, non-conformal cells: the photon leaves the null cone at FIRST order in the anisotropy and is '
      'birefringent (A1-A3), on the lattice as in the medium limit', okd,
      '; '.join(f"{n}: err {R[n]['lit'][0]:.2e}, pol split {R[n]['lit'][1]:.2e}" for n in list(cases)[3:]))
oks = all(R[n]['site'][0] < 1e-6 and R[n]['site'][1] < 1e-6 and R[n]['site'][2] < 1e-9 for n in cases)
check('B3 [T/D] site-Hodge reading: every cell (anisotropic, sheared, strong lapse, shift .15 c) puts both polarisations on the '
      'null cone to lattice O(q^2), degenerate, all frequencies real (stable)', oks,
      'max err ' + f"{max(R[n]['site'][0] for n in cases):.1e}, split {max(R[n]['site'][1] for n in cases):.1e}, "
      f"Im w {max(R[n]['site'][2] for n in cases):.0e}")
gap = 1e9; immax = 0.0
for name, (N, g, b) in cases.items():
    for _ in range(25):
        q = rng.uniform(-np.pi, np.pi, 3); w = omegas(q, N, g, b, 'site'); w = w[np.abs(w) > 1e-5]
        immax = max(immax, np.max(np.abs(np.imag(w))))
        wr = np.sort(np.abs(np.real(w)))
    q0 = np.array([1e-4, 0, 0]); wr = np.sort(np.abs(np.real(omegas(q0, N, g, b, 'site')))); gap = min(gap, wr[-1])
check('B4 [D] site-Hodge reading keeps the extra (copy-sign) branch gapped at q -> 0 and every Bloch frequency real over the zone',
      gap > 1 and immax < 1e-8, f'min extra frequency at q -> 0 over cells {gap:.2f}; max |Im w| over 150 zone points {immax:.0e}')
# lattice = medium check (literal, diag aniso)
N, g, b = cases['diag aniso (1.1,.95,1)']; el, nl = medium(N, g, 'lit'); dev = 0.0
for n in (np.array([0, 0, 1.]), np.array([1, 2, 3.]) / 14**.5):
    pos, _, _ = photon(1e-3 * n, N, g, b, 'lit'); dev = max(dev, np.max(np.abs(np.sort(pos) / 1e-3 - fresnel(el, nl, n))))
check('B5 [D] the lattice cones equal the continuum medium (eps, nu of A1-A2) to O(q^2), so C and D may use the medium',
      dev < 1e-5, f'max |w_lattice - w_medium|/q = {dev:.1e}')

# ---------------- C. weak fields: bending, Shapiro, GWs ----------------
print('== C. weak fields (medium limit, linear in the field)')
def w_pol(eps, nu, k):
    import scipy.linalg as sl
    kx = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    w2, V = sl.eigh(-kx @ nu @ kx, eps); idx = np.argsort(w2)[1:]
    return np.sqrt(np.abs(w2[idx])), V[:, idx]
def ray_factor(gauge_kind, reading, m=1e-7, b=1.0):
    """deflection of a ray along x at z = b past mass m at the origin, in units of the Newtonian 2m/b, per polarisation (y, xz)"""
    def metric(x, z):
        r = math.hypot(x, z); n = np.array([x, 0, z]) / r; Phi = -m / r
        if gauge_kind == 'iso': return 1 + Phi, (1 - 2 * Phi) * I3
        return 1 + Phi, I3 - 2 * Phi * np.outer(n, n)                 # linearised Schwarzschild (radial) gauge
    def wy_wxz(x, z):
        N, g = metric(x, z); e, nu = medium(N, g, reading); w, V = w_pol(e, nu, np.array([1., 0, 0]))
        iy = int(np.argmax(np.abs(V[1]))); return w[iy], w[1 - iy]
    us = np.linspace(-9, 9, 1201); xs = b * np.sinh(us); jac = b * np.cosh(us); dz = 1e-4 * b; out = []
    for p in (0, 1):
        f = np.array([(wy_wxz(x, b + dz)[p] - wy_wxz(x, b - dz)[p]) / (2 * dz) for x in xs])
        out.append(np.trapezoid(f * jac, us) / (2 * m / b))
    return out
rf = {(gk, rd): ray_factor(gk, rd) for gk in ('iso', 'rad') for rd in ('lit', 'site')}
check('C1 [T/D] isotropic gauge, literal reading: light bends by 1 + gamma = 2 for both polarisations; Shapiro coefficient '
      '(1 + gamma)/2 = 1 (local speed N/a = 1 + 2U: same integrand)', all(abs(v - 2) < 1e-3 for v in rf[('iso', 'lit')]),
      f"bending/(2m/b) y-pol {rf[('iso','lit')][0]:.4f}, xz-pol {rf[('iso','lit')][1]:.4f}")
check('C2 [T/D] the SAME field in the radial gauge: literal reading gives gauge-dependent, polarisation-split bending; site-Hodge '
      'gives 2 for both in both gauges', all(abs(v - 2) < 1e-3 for v in rf[('rad', 'site')] + rf[('iso', 'site')])
      and max(abs(v - 2) for v in rf[('rad', 'lit')]) > 0.05,
      f"radial literal y/xz {rf[('rad','lit')][0]:.4f}/{rf[('rad','lit')][1]:.4f}; site y/xz {rf[('rad','site')][0]:.4f}/{rf[('rad','site')][1]:.4f}")
# GW: TT h_+ and h_x, light along z (wave direction) and along x
def gw_coeff(kind, k, reading, h=1e-6):
    g = I3.copy()
    if kind == '+': g[0, 0] += h; g[1, 1] -= h
    else: g[0, 1] = g[1, 0] = h
    e, nu = medium(1.0, g, reading); w, _ = w_pol(e, nu, k); target = math.sqrt(k @ np.linalg.inv(g) @ k)
    return (w - target) / (h * target)
gwl = {(kd, ax): gw_coeff(kd, kv, 'lit') for kd in '+x' for ax, kv in (('z', np.array([0, 0, 1.])), ('x', np.array([1., 0, 0])))}
gws = max(np.max(np.abs(gw_coeff(kd, kv, 'site'))) for kd in '+x' for kv in (np.array([0, 0, 1.]), np.array([1., 0, 0])))
check('C3 [T/D] in a TT gravitational wave the literal reading makes light birefringent at first order in h (dv/c per unit h shown); '
      'site-Hodge: zero', max(np.max(np.abs(v)) for v in gwl.values()) > 0.2 and gws < 1e-5,
      '; '.join(f"h{kd} k||{ax}: {v[0]:+.2f},{v[1]:+.2f}" for (kd, ax), v in gwl.items()) + f'; site {gws:.0e}')

# ---------------- D. alpha in a cell ----------------
print('== D. Coulomb strength in a cell (proper energy x proper distance), Gauss law, least electric energy')
def alpha_dir(N, g, reading, n):
    e, _ = medium(N, g, reading); r_c = 1.0; x = n * r_c
    phi = 1 / (4 * math.pi * math.sqrt(np.linalg.det(e)) * math.sqrt(x @ np.linalg.inv(e) @ x))
    return phi / N * math.sqrt(x @ g @ x)
a0 = alpha_dir(1.0, I3, 'lit', np.array([1., 0, 0]))
dirsD = [np.array(v) / np.linalg.norm(v) for v in ((1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1), (1, -2, 3))]
conf = max(abs(alpha_dir(N, a * I3, 'lit', n) / a0 - 1) for N, a in ((1.3, .7), (0.8, 1.2)) for n in dirsD)
an_l = [alpha_dir(1.0, np.diag([1 + 1e-4, 1 - 1e-4, 1]), 'lit', n) / a0 - 1 for n in dirsD]
an_s = [alpha_dir(1.0, np.diag([1 + 1e-4, 1 - 1e-4, 1]), 'site', n) / a0 - 1 for n in dirsD]
check('D1 [T] tree level: in every conformal cell (any lapse, any scale) the literal reading gives the flat Coulomb strength in '
      'proper units exactly, in every direction (no per-cell tuning needed); in an anisotropic cell (sigma = 1e-4) it varies with '
      'direction at O(sigma), site-Hodge does not', conf < 1e-12 and np.ptp(an_l) > 0.5e-4 and np.ptp(an_s) < 1e-12,
      f'conformal dev {conf:.0e}; aniso literal spread/sigma {np.ptp(an_l)/1e-4:.2f}, site {np.ptp(an_s):.0e}')
k_alpha_noclause = (2 / (3 * math.pi)) * 8 / 137.036
print(f'   sea running: proper cell size ~ (1 - U), so a FIXED bare coupling per cell gives d ln alpha/dU = (2 alpha/3 pi) sum Q^2 Nc '
      f'= {k_alpha_noclause:.1e} (charged fermions, sum = 8) vs clock bound 1.4e-8: the clause is needed and sets it to 0 (residual (E l)^2)')

# ---------------- E. estimates against measurement ----------------
print('== E. ESTIMATES (not theorems); site spacing l = sqrt(8 pi) l_P = 8.1e-35 m (x2 for a cube)')
hbarc = 1.9733e-16; lP = 1.616e-35; l = math.sqrt(8 * math.pi) * lP
# dimension-six birefringence from the flat lattice (face diagonal)
qf = 0.02 * np.array([1., 1, 0]) / 2**.5; pos, _, _ = photon(qf, 1.0, I3, np.zeros(3), 'lit'); bface = (pos[1] - pos[0]) / np.mean(pos) / 0.02**2
c6 = bface * (l / hbarc)**2
E = 1e-4; k = E / hbarc; Lgrb = 3e25; dphi = bface * (k * l)**2 * k * Lgrb
check('E1 [D] flat skew loops: dimension-six birefringence on face diagonals dv/c = b (q l)^2 (zero on axes/body diagonals)',
      abs(bface - 1 / 12) < 2e-3, f'b = {bface:.4f}; dv/c = {c6:.1e} (E/GeV)^2 vs quoted bound ~1e-16 (E/GeV)^2; '
      f'100 keV GRB at 1 Gpc: rotation {dphi:.0e} rad (polarisation kept)')
h_pta = 2e-15; lam = 3e16; Nseg = Lgrb / lam
rot_lit = math.sqrt(Nseg) * k * lam / 2 * 0.5 * h_pta
print(f'   literal reading in the measured nHz GW background (h ~ {h_pta:.0e}): dv/c ~ h/2 per coherence length {lam:.0e} m -> 100 keV '
      f'GRB rotation ~{rot_lit:.0e} rad (random walk), 1 GHz radio ~{rot_lit*(2*math.pi*1e9/3e8)/k:.0e} rad: polarised GRBs/quasars exclude it; '
      f'any tensor residual c_b h needs c_b < {math.pi/2/rot_lit*0.5:.0e}')
print('   static field, conformal cells: 1 + gamma = 2, Shapiro 1, GP-B drag = GR at tree level; lattice part (k l)^2 = '
      f'{(2*math.pi*8.4e9/3e8*l)**2:.0e} at 8.4 GHz vs Cassini 2.3e-5; non-conformal part of the edges must be < ~1e-18 (cavity) '
      'for the literal reading')
print(f'   GW170817: photon (100 keV) dim-6 {bface*(k*l)**2:.0e}, GW (100 Hz) {(2*math.pi*100/3e8*l)**2:.0e}; |c_g - c_gamma| << 1e-15 '
      'IF the edge waves sit on the edge null cone (edge-modes probe: no result yet)')
print('supplied: Gaussian registers, Wilson V4/area^2 meaning of "proper area", site B from its loops, temporal gauge, metrics/gauges,')
print('  site-Hodge companion pairing (proposal), measured numbers. Not computed: sea (dressed) tensor response in non-conformal cells.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
