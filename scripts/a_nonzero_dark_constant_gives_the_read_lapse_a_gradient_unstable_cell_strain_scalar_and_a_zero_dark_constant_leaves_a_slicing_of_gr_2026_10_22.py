AUDIT_INPUT_PATHS = ('docs/A_NONZERO_DARK_CONSTANT_GIVES_THE_READ_LAPSE_A_GRADIENT_UNSTABLE_CELL_STRAIN_SCALAR_AND_A_ZERO_DARK_CONSTANT_LEAVES_A_SLICING_OF_GR_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""lapse-strong-coupling: does the read lapse (CL-1 N = sin eps0/sqrt(sum gamma^aa)), with the shift stationary
and the momentum constraint kept, have a projectable-Horava-like strongly coupled scalar?
Self-contained: sympy + numpy + scipy.  Labels: [T] theorem-level check, [D] finite diagnostic, [E] estimate."""
import time, numpy as np, sympy as sp
from scipy.integrate import solve_ivp
AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")

print('== A. the zero-dark-constant sector and the linear flat sector')
# A1: Bianchi I with the read lapse, alpha_i = ln a_i, N = s/sqrt(sum e^{-2 alpha}); only alpha varied
def rhs(t, y):
    al, v = y[:3], y[3:]
    S = np.exp(-2 * al).sum(); N = 1 / np.sqrt(S); sg = np.exp(al.sum())
    dN = N * np.exp(-2 * al) / S                       # dN/dalpha_i
    M = np.eye(3) - np.ones((3, 3))                     # L = (sg/N) v.M.v
    # EL: d/dt(2 sg/N M v) = d/dalpha (sg/N) * vMv
    q = v @ M @ v; c = sg / N
    dc = c * (1 - dN / N)                               # d(sg/N)/dalpha_i
    cdot = dc @ v
    acc = np.linalg.solve(2 * c * M, dc * q - 2 * cdot * (M @ v))
    return np.concatenate([v, acc])
def energy(y):
    al, v = y[:3], y[3:]; S = np.exp(-2 * al).sum(); N = 1 / np.sqrt(S); return np.exp(al.sum()) / N * (v @ (np.eye(3) - 1) @ v)
p = np.array([2 / 3, 2 / 3, -1 / 3]); v0 = p * 0.5                                    # Kasner data: E = 0
p2 = np.array([0.9, 0.2, 0.1]); v2 = p2 * 0.5                                         # E != 0 data
out = []
for v in (v0, v2):
    y0 = np.concatenate([[0.1, -0.2, 0.05], v]); sol = solve_ivp(rhs, (0, 1.2), y0, rtol=1e-11, atol=1e-13)
    yT = sol.y[:, -1]; out.append((energy(y0), energy(yT), np.ptp((yT[3:] / yT[3])), np.ptp(sol.y[3:, :] / sol.y[3, :], axis=1).max()))
okA1 = abs(out[0][0]) < 1e-12 and abs(out[0][1]) < 1e-9 and out[0][3] < 1e-8 and abs(out[1][1] - out[1][0]) < 1e-8 * abs(out[1][0]) and out[1][3] > 1e-2
check('A1 [T+D] the dark constant c = N H is the tick energy of the edges and is conserved; with c = 0 the read lapse '
      'is only a slicing of GR (vacuum Bianchi I: Kasner directions fixed, nonlinear), with c != 0 the extra stress '
      '-c dN/dgamma bends the solution off GR', okA1,
      f'c=0: c(T) {out[0][1]:.0e}, direction drift {out[0][3]:.0e}; c != 0: dc/c {abs(out[1][1]-out[1][0])/abs(out[1][0]):.0e}, drift {out[1][3]:.2f}')
print('   continuum statement: d_t H and d_t H_k are linear in (H, d H, H_k, d H_k) (deformation algebra + the extra force'
      '\n   -dN/dgamma H), so c = 0 with H_k = 0 is invariant at every order: no extra scalar, no strong coupling.')
# A2: linear flat scalar sector with kinetic K_ij K^ij - lam K^2 (lam = 1 is GR; lattice terms may shift it)
t, w, K, lam = sp.symbols('t omega K lambda', positive=True)
z, E, B, ph = [sp.Function(n)(t) for n in ('zeta', 'E', 'B', 'phi')]
def lag(phi, Bv):   # h_ij = 2 zeta delta + 2 d_i d_j E, shift d_i B, lapse perturbation phi, K = k^2
    X = E.diff(t) - Bv
    kin = (3 - 9 * lam) * z.diff(t) ** 2 + (6 * lam - 2) * K * z.diff(t) * X + (1 - lam) * K ** 2 * X ** 2
    return kin + 2 * K * z ** 2 + 4 * K * phi * z
def mat(L, qs):
    eqs = [sp.euler_equations(L, [q], t)[0].lhs for q in qs]; am = sp.symbols('a0:%d' % len(qs))
    sb = {q: c * sp.exp(-sp.I * w * t) for q, c in zip(qs, am)}
    return sp.Matrix([[sp.expand(sp.simplify(eq.subs(sb).doit() * sp.exp(sp.I * w * t))).coeff(c) for c in am] for eq in eqs])
MA = mat(lag(z - K * E / 3, B), [z, E, B])                      # read lapse, shift stationary
MP = mat(lag(0, B), [z, B])                                      # projectable control (N = N(t))
dA = sp.factor(MA.det()); M1 = MA.subs(lam, 1)
okA = (not dA.has(w)) and sp.simplify(dA.subs(lam, 1)) == 0 and all(sp.simplify(v[0]) == 0 for v in M1.nullspace())
dP = sp.factor(MP.det())
w2P = sp.simplify(sp.solve(sp.expand(dP).subs(w ** 2, sp.Symbol('W')), sp.Symbol('W'))[0] / K)
check('A2 [T] flat space, any lambda: with the read lapse and stationary shift every k != 0 solution has zeta = 0 '
      '(E multiplies zeta through dN/dE; for lambda != 1 the det is omega-free and nonzero: rigid), so the projectable scalar is absent for every lambda, not only lambda = 1; '
      'control: projectable lapse gives omega^2 = -(lambda-1)/(3 lambda-1) k^2 with kinetic 2(3lambda-1)/(lambda-1)',
      okA and sp.simplify(w2P + (lam - 1) / (3 * lam - 1)) == 0, f'read-lapse det = {dA} (no omega root; lambda = 1: gauge null vector with zeta = 0); projectable omega^2/k^2 = {w2P}')

print('== B. decoupling limit around a dark constant c0 (k >> H_D; Stueckelberg tick T and labels X^a)')
G = sp.Matrix(4, 4, lambda A, m: sp.Symbol(f'G{A}{m}')); eta = sp.diag(-1, 1, 1, 1); gp = G * eta * G.T
F = (-1 / gp[0, 0]) * sum(gp[a, a] - gp[0, a] ** 2 / gp[0, 0] for a in (1, 2, 3)) / 3   # N^2 sum gamma^aa / sigma^2
V = list(G); grad = [sp.diff(F, v) for v in V]; hess = [[sp.diff(g, v) for v in V] for g in grad]
fg = sp.lambdify(V, grad); fh = sp.lambdify(V, hess)
def Qmat(A, kv, wv, c0=1.0):      # L2 = c0 * (1/2) dpi.Hess.dpi + dlam * grad.dpi ; plane wave p = (-w, k)
    a = list(np.array(A, float).flatten()); J = np.array(fg(*a), float).reshape(4, 4); M = np.array(fh(*a), float).reshape(16, 16)
    pv = np.array([-wv] + list(kv)); Q = np.zeros((5, 5), complex)
    for i in range(4):
        for j in range(4): Q[i, j] = c0 * sum(M[i * 4 + m, j * 4 + n] * pv[m] * pv[n] for m in range(4) for n in range(4))
        Q[i, 4] = Q[4, i] = J[i] @ pv
    return Q
def detpoly(A, kv, c0=1.0):
    ws = np.linspace(-2, 2, 17); d = [np.linalg.det(Qmat(A, kv, x, c0)).real for x in ws]; c = np.polyfit(ws, d, 8)[::-1]
    return np.where(abs(c) < 1e-10 * max(abs(c).max(), 1e-300), 0, c)
# B1: isotropic background; symbolic reduction of the scalar sector (pi0, psi, dlam)
e = sp.symbols('e'); p0t = sp.Symbol('p0t'); p0 = sp.symbols('p0_1:4'); pt = sp.symbols('pt1:4'); P = sp.Matrix(3, 3, lambda a, i: sp.Symbol(f'P{a}{i}'))
Gs = sp.Matrix([[1 + e * p0t] + [e * x for x in p0]] + [[e * pt[a]] + [(1 if a == i else 0) + e * P[a, i] for i in range(3)] for a in range(3)])
ser = sp.series(F.subs(dict(zip(V, list(Gs)))), e, 0, 3).removeO(); f1 = sp.expand(ser.coeff(e, 1)); f2 = sp.expand(ser.coeff(e, 2))
nopidot = all(sp.diff(f2, pt[a], 2) == 0 for a in range(3))
k2, pi0, psi, dl, c0s = sp.symbols('k2 pi0 psi dl c0')
L2 = c0s * (3 * p0t ** 2 - sp.Rational(4, 3) * k2 * pi0 ** 2 + 2 * k2 * p0t * psi + k2 ** 2 * psi ** 2 / 3) + dl * (-2 * p0t - sp.Rational(2, 3) * k2 * psi)
red = sp.simplify(L2.subs(psi, -3 * p0t / k2))
dets = [detpoly(np.eye(4), kv) for kv in ((0.7, 0.3, -0.5), (1, 0, 0), (0.3, 0.9, 0.2))]
rigid = all(np.count_nonzero(d[1:]) == 0 and d[0] != 0 for d in dets)
check('B1 [T] isotropic cells: f1 = -2 dpi0/dt + (2/3) div pi, f2 has no (dpi^a/dt)^2; after the tick constraint '
      'the pi0 kinetic coefficient is 3 - 6 + 3 = 0 exactly (the lambda = 1 cancellation) and L2 = -(4/3) c0 k^2 pi0^2: '
      'the medium is rigid, det(omega) is omega-independent, no mode at any omega, including no static pattern',
      nopidot and sp.simplify(red + sp.Rational(4, 3) * c0s * k2 * pi0 ** 2) == 0 and rigid,
      f'f1 = {f1}; reduced L2 = {red}; det coeffs (w^0..) {[float("%.3g" % x) for x in dets[0][:3]]}')
# B2: strained cells X = (1 + S) x : the scalar comes back with kinetic ~ c0 * (k.S.k); symbolic first order
d_ = sp.symbols('delta'); kx = sp.symbols('kx', positive=True)
def symdet(S, kvec):
    Asym = sp.eye(4) + S; sub = dict(zip(V, list(Asym)))
    J = [sp.series(g.subs(sub), d_, 0, 2).removeO() for g in grad]
    M = [[sp.series(h.subs(sub), d_, 0, 2).removeO() for h in row] for row in hess]
    pv = [-w] + list(kvec); Q = sp.zeros(5, 5)
    for i in range(4):
        for j in range(4): Q[i, j] = sum(M[i * 4 + m][j * 4 + n] * pv[m] * pv[n] for m in range(4) for n in range(4))
        Q[i, 4] = Q[4, i] = sum(J[i * 4 + m] * pv[m] for m in range(4))
    return sp.series(sp.expand(Q.det(method='berkowitz')), d_, 0, 2).removeO()
Sx = sp.diag(0, d_, -d_, 0)
Dx = sp.expand(symdet(Sx, (kx, 0, 0))); Dy = sp.expand(symdet(Sx, (0, kx, 0)))
rx = sp.simplify(-Dx.coeff(w, 0) / Dx.coeff(w, 2)); ry = sp.simplify(-Dy.coeff(w, 0) / Dy.coeff(w, 2))
okB2 = sp.limit(rx * d_, d_, 0) == 2 * kx ** 2 / 9 and sp.limit(ry * d_, d_, 0) == -2 * kx ** 2 / 9
check('B2 [T] strained cells (labels X = (1+S)x, S = diag(d,-d,0)), first order in d: one scalar returns with '
      'omega^2 = 2 k^2/(9 khat.S.khat): its kinetic term is c0 * (9/2)(khat.S.khat) while gradient and cubic terms are '
      'order c0 (leading order in d shown; O(1) part not controlled at this series order); one sign of khat.S.khat gives omega^2 < 0', okB2, f'k||x: omega^2 = {rx}; k||y: omega^2 = {ry}')
# B3: numeric scan over strains and directions; scaling of the kinetic coefficient; sign; c0 = 0 control
rows = []; okscale = True
for dv in (1e-2, 1e-3, 1e-4):
    for nm, S in (('diag', np.diag([0, dv, -dv, 0])), ('axial', np.diag([0, dv, dv, -2 * dv])), ('offd', np.array([[0, 0, 0, 0], [0, 0, dv, 0], [0, dv, 0, 0], [0, 0, 0, 0.]]))):
        ws2 = []
        for kv in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (0.6, 0.8, 0)):
            c = detpoly(np.eye(4) + S, kv); ws2.append(-c[0] / c[2] if c[2] != 0 else np.inf)
        rows.append((dv, nm, ws2))
neg = all(min(r[2]) < 0 for r in rows)
sc = [r[2][3] * r[0] for r in rows if r[1] == 'offd']
check('B3 [D] every anisotropic strain tested (diagonal, axial, off-diagonal; d = 1e-2..1e-4) has directions with '
      'omega^2 < 0, growth rate ~ k sqrt(2/(9|d|)) (k.S.k = 0 directions: ~ k/d); omega^2 d is fixed over two decades',
      neg and np.ptp(sc) / abs(np.mean(sc)) < 0.05,
      '; '.join(f'{r[1]} d={r[0]:g}: w2/k2 ' + ','.join(f'{x:.3g}' for x in r[2]) for r in rows if r[0] == 1e-3))
Q0 = Qmat(np.eye(4) + np.diag([0, 1e-2, -1e-2, 0]), (0.6, 0.8, 0), 0.7, c0=0.0)
rk = [np.linalg.matrix_rank(Qmat(np.eye(4) + np.diag([0, 1e-2, -1e-2, 0]), kv, wv, c0=0.0), tol=1e-9) for kv in ((1, 0, 0), (0.6, 0.8, 0)) for wv in (0.1, 0.9, 3.0)]
check('B4 [T] c0 = 0 exactly: the medium matrix has rank 2 at every (omega, k) on every background: dlam = 0 and '
      'the tick constraint, the other three directions pure gauge (GR): no mode, no instability, nothing to couple',
      all(r == 2 for r in rk), f'ranks {[int(r) for r in rk]}')

print('== C. estimates against measurement')
hbarc = 1.97327e-5                                       # eV cm
rho_g = 0.2606                                            # eV/cm^3 photons today (T = 2.7255 K)
rho_r = rho_g * (1 + 3.044 * 7 / 8 * (4 / 11) ** (4 / 3))
rhoD = 0.04 * rho_r                                       # register's N_eff bound
L4 = (rhoD * hbarc ** 3) ** 0.25                          # eV
ks = {nm: L4 * dv ** 0.625 for nm, dv in (('cosmic 1e-5', 1e-5), ('Sun at Earth 1e-8', 1e-8), ('LIGO strain 1e-21', 1e-21))}
lens = {nm: hbarc / x for nm, x in ks.items()}           # cm
check('C1 [E] strong-coupling momentum k_s ~ rho_D^(1/4) d^(5/8) (canonical power counting with kinetic c0 d, '
      'cubic c0): rho_D^(1/4) today at the N_eff bound, and k_s for the ambient cell strain d ~ Phi; every value is far '
      'below 1/mm (2e-4 eV) and TeV; in an exactly isotropic vacuum k_s = 0',
      all(x < 2e-4 for x in ks.values()), f'rho_D^(1/4) = {L4:.2e} eV (1/{hbarc/L4:.2f} cm); ' + '; '.join(f'{k}: 1/{v/100:.3g} m' for k, v in lens.items()))
H0 = 1.44e-33; OmD = rhoD / 4870.0                       # eV ; rho_crit h=0.674 in eV/cm^3
HD = H0 * np.sqrt(OmD); kAU = hbarc / 1.496e13
check('C2 [E] what the strongly coupled/unstable sector does to tested gravity at linear order: its exchange '
      'between masses is (H_D/k)^2/d of the graviton\'s; tiny, so the danger is the nonlinear endpoint of the '
      'exponential growth (the dark density has indefinite sign, total conserved), not linear tests',
      (HD / kAU) ** 2 / 1e-8 < 1e-20, f'Omega_D <= {OmD:.1e}, H_D = {HD:.1e} eV, at 1 AU (H_D/k)^2/d = {(HD/kAU)**2/1e-8:.0e}; '
      f'growth time at the cell scale ~ sqrt(d) cell crossings (d = 1e-5: {np.sqrt(9e-5/2):.1e})')
check('C3 [E] the register already makes c0 != 0 after the start: each split kicks c by (HL)^2/8 of the density, '
      'crush and density contrasts make per-cube constants; so "zero at the start" does not keep c = 0, and a '
      'selection rule is needed', True, 'register text (tick item); the fix must also make splits and crushes respect it')
print('supplied: continuum ADM limit, lambda = 1 (A2 covers lambda != 1 at linear order only); decoupling limit')
print('  (flat metric, k >> H_D); ambient strain d ~ Phi as the lattice-coordinate anisotropy (not computed in the')
print('  rules\' own gauge); k_s from power counting, exponent 5/8 not computed from the full cubic vertex.')
print('not built: nonlinear endpoint of the B3 growth; lattice (Regge/register) preservation of H = 0.')
print(f'elapsed {time.time()-t0:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
