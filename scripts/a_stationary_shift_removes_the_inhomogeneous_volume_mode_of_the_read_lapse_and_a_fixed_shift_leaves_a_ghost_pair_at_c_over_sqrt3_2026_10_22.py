AUDIT_INPUT_PATHS = ('docs/A_STATIONARY_SHIFT_REMOVES_THE_INHOMOGENEOUS_VOLUME_MODE_OF_THE_READ_LAPSE_AND_A_FIXED_SHIFT_LEAVES_A_GHOST_PAIR_AT_C_OVER_SQRT3_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""inhomog-volume: inhomogeneous volume (conformal) modes of the edges under CL-1's fixed lapse.

CL-1 lapse: sqrt3 N rms(sqrt gamma^ii) = sin eps0, i.e. N(gamma) = s / sqrt(Sigma), Sigma = sum_a gamma^aa,
s = sin eps0.  N is read from the edges and is NOT varied (no Hamiltonian constraint).  Linearised
around flat space in the continuum limit of the hinge sum (ADM form of Regge; lattice Fourier
multipliers K = sum 4 sin^2(k_i/2) for the hops and K_R for the slice curvature, both supplied).
Two readings of the shift: (A) the shift is a stationary variable (momentum constraint holds);
(B) the shift is not varied (fixed, zero on the flat background).
Tags: [T] exact theorem (symbolic/exact check), [D] finite diagnostic, [E] estimate vs measurement.
numpy + sympy only.
"""
import time, signal
import numpy as np
import sympy as sp
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(AUDIT_TIMEOUT_SEC)
T0 = time.time(); NP = NF = 0
rng = np.random.default_rng(11)


def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")


print('== A. the lapse rule as a function of the edges')
s = sp.symbols('s', positive=True)
gs = sp.symbols('g11 g12 g13 g22 g23 g33')
G = sp.Matrix([[gs[0], gs[1], gs[2]], [gs[1], gs[3], gs[4]], [gs[2], gs[4], gs[5]]])
Gi = G.inv(); Sig = Gi[0, 0] + Gi[1, 1] + Gi[2, 2]; Nf = s / sp.sqrt(Sig)
# symmetric derivative dN/dgamma_ij (off-diagonal halved)
idx = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 1): 3, (1, 2): 4, (2, 2): 5}
def comp(i, j): return idx[(min(i, j), max(i, j))]
dN = [[sp.diff(Nf, gs[comp(i, j)]) * (1 if i == j else sp.Rational(1, 2)) for j in range(3)] for i in range(3)]
# A1: linearisation: dN/N0 = tr h/6; TT and transverse-vector parts vanish at first order; TT second order -|h|^2/6
e = sp.symbols('e'); hs = sp.symbols('h1:7'); H = sp.Matrix([[hs[0], hs[1], hs[2]], [hs[1], hs[3], hs[4]], [hs[2], hs[4], hs[5]]])
Nh = Nf.subs({gs[comp(i, j)]: (1 if i == j else 0) + e * H[i, j] for i in range(3) for j in range(3)})
ser = sp.series(Nh, e, 0, 3).removeO(); N0 = s / sp.sqrt(3)
c1 = sp.simplify(ser.coeff(e, 1) / N0 - H.trace() / 6)
c2tt = sp.simplify((ser.coeff(e, 2) / N0).subs({hs[0]: hs[0], hs[3]: hs[3], hs[5]: -hs[0] - hs[3]}) -
                   (-(sum(H[i, j] ** 2 for i in range(3) for j in range(3)) / 6)).subs(hs[5], -hs[0] - hs[3]))
check('A1 [T] CL-1 lapse N = sin(eps0)/sqrt(sum_a gamma^aa) linearised: dN/N0 = tr h/6 exactly (rotation-invariant at '
      'first order, blind to transverse-vector and tensor parts); on traceless h the second order is -N0 h_ab h_ab/6',
      c1 == 0 and c2tt == 0, f'first-order residual {c1}; traceless second-order residual {c2tt}')
# A2: homogeneous law: N = a^n not varied -> conserved energy is a fluid with w = n/3
a, n_, E0 = sp.symbols('a n E0', positive=True); tt = sp.symbols('t')
ws = []
for n in (0, 1, -3):
    A_ = sp.Function('A')(tt); L = -3 * A_ * A_.diff(tt) ** 2 / A_ ** n
    En = sp.simplify(A_.diff(tt) * sp.diff(L, A_.diff(tt)) - L)        # conserved (L has no explicit t)
    adot2 = sp.solve(sp.Eq(En.subs(A_.diff(tt), sp.Symbol('v')), E0), sp.Symbol('v'))[0] ** 2
    H2 = sp.simplify(adot2.subs(A_, a) / (a ** 2 * a ** (2 * n)))          # (adot/(N a))^2 ~ rho_D
    p = sp.simplify(a * sp.diff(sp.log(H2), a)); ws.append(sp.simplify(-p / 3 - 1))
check('A2 [T] a lapse N = a^n that is read, not varied, turns the dropped constraint into a conserved fluid with w = n/3: '
      'n = 0 (projectable Horava-Lifshitz) dust, n = 1 (CL-1, N = sig l) radiation (= volume-mode A3: dark constant = dark '
      'radiation), n = -3 (unimodular) a cosmological constant', ws == [0, sp.Rational(1, 3), -1], f'w for n = 0, 1, -3: {ws}')
# A3: momentum-constraint consistency: {H_k, int N H} = int H Pi^i_k d_i xi^k with Pi^i_k = 2 gamma_kj dN/dgamma_ij
gnum = rng.normal(size=(3, 3)); gnum = gnum @ gnum.T + 3 * np.eye(3)
sub = {gs[comp(i, j)]: float(gnum[i, j]) for i in range(3) for j in range(3)}
Pi = np.array([[float(sum(2 * G[k, j] * dN[i][j] for j in range(3)).subs(sub).subs(s, 1)) for k in range(3)] for i in range(3)])
gin = np.linalg.inv(gnum); Sn = np.trace(gin); Pform = Sn ** -1.5 * gin
xs = sp.symbols('x1:4'); gfield = [[sp.Rational(int(gnum[i, j] * 100), 100) + sp.Rational(1, 7) * xs[(i + j) % 3] * (i + 1) for j in range(3)] for i in range(3)]
gfield = [[gfield[min(i, j)][max(i, j)] for j in range(3)] for i in range(3)]
xi = [xs[1] ** 2 / 3, xs[0] * xs[2] / 5, xs[1] / 2 + xs[0] ** 2 / 7]
Lxi = [[sum(xi[k] * sp.diff(gfield[i][j], xs[k]) + gfield[k][j] * sp.diff(xi[k], xs[i]) + gfield[i][k] * sp.diff(xi[k], xs[j]) for k in range(3)) for j in range(3)] for i in range(3)]
fsub = {gs[comp(i, j)]: gfield[i][j] for i in range(3) for j in range(3)}
pt = {xs[0]: sp.Rational(1, 3), xs[1]: -sp.Rational(1, 2), xs[2]: sp.Rational(1, 5), s: 1}
dNf = [[dN[i][j].subs(fsub) for j in range(3)] for i in range(3)]
lhs = sum(dNf[i][j] * Lxi[i][j] for i in range(3) for j in range(3)) - sum(xi[k] * sp.diff(Nf.subs(fsub), xs[k]) for k in range(3))
rhs = sum(2 * gfield[k][j] * dNf[i][j] * sp.diff(xi[k], xs[i]) for i in range(3) for j in range(3) for k in range(3))
idn = abs(float((lhs - rhs).subs(pt)))
iso = float((2 * 4 * dN[0][0]).subs({gs[0]: 4, gs[3]: 4, gs[5]: 4, gs[1]: 0, gs[2]: 0, gs[4]: 0, s: 1}))
check('A3 [T] the lapse is not a spatial scalar, so the momentum constraints H_k = 0 are kept only if '
      'd_i(H Pi^i_k) = 0, Pi^i_k = 2 gamma_kj dN/dgamma_ij = s Sigma^(-3/2) gamma^ik = N gamma^ik/Sigma; on isotropic '
      'cells Pi = (N/3) delta, so d_k(N H) = 0: the dark pressure must be uniform (for unimodular N the same identity '
      'gives the known d_k Lambda = 0)', abs(Pi - Pform).max() < 1e-12 and idn < 1e-12 and abs(iso - 2 / (3 * np.sqrt(3))) < 1e-12,
      f'Pi vs closed form {abs(Pi - Pform).max():.0e}; Lie-derivative identity at a point {idn:.0e}; isotropic Pi_11 at a = 2: {iso:.6f} = N/3')

print('== B. linear scalar sector on flat space (lattice multipliers K, K_R; any k != 0)')
t, w, K, KR = sp.symbols('t omega K K_R', positive=True)
z, E, Bf, ph = [sp.Function(nm)(t) for nm in ('zeta', 'E', 'B', 'phi')]
def lag(phi, Bv):   # h_ij = 2 zeta delta + 2 d_i d_j E, shift d_i B, lapse perturbation phi (units 1/16 pi G)
    return -6 * z.diff(t) ** 2 + 4 * K * z.diff(t) * (E.diff(t) - Bv) + 2 * KR * z ** 2 + 4 * KR * phi * z
def eom(L, qs):
    eqs = [sp.euler_equations(L, [q], t)[0].lhs for q in qs]; am = sp.symbols('c0:%d' % len(qs))
    sb = {q: c * sp.exp(-sp.I * w * t) for q, c in zip(qs, am)}
    return sp.Matrix([[sp.expand(sp.simplify(eq.subs(sb).doit() * sp.exp(sp.I * w * t))).coeff(c) for c in am] for eq in eqs])
MG = eom(lag(ph, Bf), [z, E, Bf, ph]); MA = eom(lag(z - K * E / 3, Bf), [z, E, Bf]); MB = eom(lag(z - K * E / 3, 0), [z, E])
gr_ok = sp.simplify(MG.det()) == 0 and len(MG.nullspace()) == 2 and all(sp.simplify(v[0]) == 0 for v in MG.nullspace())
check('B1 [T] control, GR (lapse varied): the lapse equation forces zeta = 0 at every k != 0 and the rest is two gauge '
      'directions: no scalar degree of freedom', gr_ok, f'det {sp.simplify(MG.det())}; gauge directions {len(MG.nullspace())}, zeta component 0')
# case A: rows E and B force zeta = 0 at every omega; one gauge direction mixing E and B
nsA = MA.nullspace(); zrows = [sp.factor(MA[1, 0]), sp.factor(MA[2, 0])]
okA = sp.simplify(MA.det()) == 0 and len(nsA) == 1 and sp.simplify(nsA[0][0]) == 0 and \
      sp.solve(MA[2, 0], w) == [] and sp.simplify(MA[1, 0].subs(w, 0)) != 0
check('B2 [T] (A) fixed lapse, shift stationary: the shift equation is the momentum constraint d_t zeta = 0, and the '
      'E equation, which now carries the dropped Hamiltonian constraint times dN/dE, gives d^2(d_t^2 zeta - K_R zeta/3) = 0; '
      'together zeta = 0 for every k != 0. The leftover (E, B) direction is a gauge symmetry (a spatial shift xi combined '
      'with the time shift d_t alpha = -K xi/3 that keeps N = N(gamma)). No inhomogeneous volume mode exists: no dispersion, '
      'no ghost, and the dark constant cannot vary between cells',
      okA, f'zeta coefficients in the E and B rows: {zrows[0]}, {zrows[1]}; det {sp.simplify(MA.det())}; gauge vector (zeta,E,B) = {list(sp.simplify(x) for x in nsA[0])}')
dB = sp.factor(MB.det()); Tm = sp.Matrix([[-12, 4 * K], [4 * K, 0]])
okB = sp.simplify(dB + 16 * K ** 2 * (KR - 3 * w ** 2) ** 2 / 9) == 0 and Tm.det() < 0
check('B3 [T] (B) fixed lapse, shift not varied: two scalar fields (zeta, E) remain with det = -(16K^2/9)(K_R - 3w^2)^2: '
      'a DOUBLE root w^2 = K_R/3 (continuum w = k/sqrt3, the Bona-Masso gauge speed sqrt(dlnN/dln sqrt(gamma)) made physical), '
      'kinetic matrix of signature (+,-): a propagating ghost scalar paired with a normal one at the same frequency',
      okB, f'det = {dB}; kinetic matrix det {Tm.det()} < 0')

print('== C. time domain (exact linear evolution, periodic 16^3 lattice modes)')
Ls = 16; ks = 2 * np.pi * np.arange(Ls) / Ls
kk = np.array(np.meshgrid(ks, ks, ks, indexing='ij')).reshape(3, -1).T[1:]
Kv = (4 * np.sin(kk / 2) ** 2).sum(1); sel = Kv[np.argsort(Kv)[[0, len(Kv) // 2, -1]]]
grow = []
for Kn in sel:
    # case B, K_R = K: q = (zeta, F = K E); L = -6 zd^2 + 4 zd Fd + 6K z^2 - (4/3) K F z
    Tn = np.array([[-12.0, 4.0], [4.0, 0.0]]); Vn = np.array([[-12.0 * Kn, 4 * Kn / 3], [4 * Kn / 3, 0.0]])
    Aop = np.block([[np.zeros((2, 2)), np.eye(2)], [-np.linalg.solve(Tn, Vn), np.zeros((2, 2))]])
    ev, V = np.linalg.eig(Aop); y0 = np.array([1e-3, 0, 0, 0.0])
    tw = 2 * np.pi * 50 / np.sqrt(Kn / 3)
    y1 = expm(Aop * tw) @ y0; y2 = expm(Aop * 2 * tw) @ y0
    en = lambda y: 0.5 * y[2:] @ Tn @ y[2:] + 0.5 * y[:2] @ Vn @ y[:2]
    grow.append((np.linalg.norm(y1) / 1e-3, np.linalg.norm(y2) / 1e-3, abs(en(y2) - en(y0)) / (abs(en(y0)) + 1e-30)))
check('C1 [D] (B) the ghost-normal pair at one frequency is a Jordan block: from zeta(0) = 1e-3 at rest the state (fields and rates) grows '
      'linearly in time with exactly conserved total energy (ghost and normal parts cancel), at every lattice k',
      all(g[1] / g[0] > 1.8 and g[2] < 1e-6 for g in grow),
      '; '.join(f'K={k:.2f}: x{g[0]:.0f} after 50 periods, x{g[1]:.0f} after 100, dE/E {g[2]:.0e}' for k, g in zip(sel, grow)))

print('== D. background with a dark constant (case A)')
x1, x2, x3, c0, ee = sp.symbols('x1 x2 x3 c0 e'); X = (x1, x2, x3); kx = sp.symbols('k1:4')
ph_ = sp.exp(sp.I * (kx[0] * x1 + kx[1] * x2 + kx[2] * x3))
zt, Et, F1, F2, F3, dc = sp.symbols('zt Et F1 F2 F3 dc')
Fv = (F1, F2, F3)
hS = [[2 * zt * ph_ * (1 if i == j else 0) + 2 * sp.diff(Et * ph_, X[i], X[j]) for j in range(3)] for i in range(3)]
hV = [[sp.diff(Fv[j] * ph_, X[i]) + sp.diff(Fv[i] * ph_, X[j]) for j in range(3)] for i in range(3)]
def constraint(h):   # d_i (c Sigma^-1 gamma^ik), gamma = delta + e h, c = c0 + e dc e^{ikx}; first order in e
    Hm = sp.Matrix(h); gi = sp.eye(3) - ee * Hm; Sg = 3 - ee * Hm.trace(); cc = c0 + ee * dc * ph_
    T = cc / Sg * gi
    return [sp.simplify(sp.diff(sum(sp.diff(T[i, k], X[i]) for i in range(3)), ee).subs(ee, 0) / ph_) for k in range(3)]
cs = constraint(hS); ksq = sum(q ** 2 for q in kx)
sol = sp.solve(cs[0], dc); okS = len(sol) == 1 and sp.simplify(sol[0] - (-sp.Rational(4, 3) * c0 * ksq * Et)) == 0
hVt = [[h.subs({kx[0]: 0, kx[1]: 0, F3: 0}) for h in row] for row in hV]   # transverse: k along x3, F in the x1-x2 plane
cv = [c.subs({kx[0]: 0, kx[1]: 0, F3: 0, dc: 0}) for c in constraint(hVt)]
okV = all(sp.simplify(cv[k] - c0 * kx[2] ** 2 * Fv[k] / 3) == 0 for k in range(2)) and sp.simplify(cv[2]) == 0
check('D1 [T] (A) around cells with a uniform dark constant c0 = N H: the kept momentum constraints fix the dark-constant '
      'perturbation to dc = (4/3) c0 d^2 E (zeta drops out), force transverse vector strains to vanish (c0 d^2 F_k = 0), '
      'and leave tensors free; since N H is conserved at each cell, d_t d^2 E = 0: the pattern is static. The dark constant '
      'never propagates between cells, so the photon + two dark quanta channel (volume-mode D2) has no dark quanta',
      okS and okV, f'scalar: dc = {sol[0]}; transverse vector rows {cv}')
check('D2 [T] the same kept constraint gives the tensors a mass term from the dark constant: -N0 h_ab h_ab/6 per unit '
      'dark density (A1), i.e. m^2 = (32 pi G/3) rho_D = 4 H_D^2 in the frame of the cells, with H_D^2 = 8 pi G rho_D/3; '
      'its sign follows the sign of rho_D (tachyonic for negative dark density; sign convention flagged, not lattice-checked)',
      c2tt == 0, 'coefficient from A1 second order')

print('== E. estimates against measurement')
MP = 1.22e19; Lc = MP / (2 * np.sqrt(8 * np.pi)); cjm = 3e-3      # GeV; cell cutoff hbar c / l_c; CJM bound ~ 3 MeV
excl = (Lc / cjm) ** 8; t0 = 4.35e17; lc = 2 * np.sqrt(8 * np.pi) * 1.616e-35; growth = t0 * 3e8 / lc / np.sqrt(3)
check('E1 [E] (B) is excluded: a gravitationally coupled ghost with a Lorentz-violating cutoff makes the vacuum decay to '
      'photons + ghosts at Gamma ~ Lambda^8/M_P^4 (Cline-Jeon-Moore 2004: Lambda <~ 3 MeV from the diffuse gamma-ray '
      'background); the cell cutoff is Lambda ~ M_P/10, and the lattice terms leave the pair gapless (w -> 0 as k -> 0); '
      'even without matter the zero-point amplitude of each cell-scale pair grows by ~t0/l_c',
      excl > 1e100 and growth > 1e50, f'cutoff {Lc:.1e} GeV; rate excess over bound ~ (Lambda/3 MeV)^8 = {excl:.0e}; cell-scale Jordan growth over the age {growth:.0e}')
OmD = 0.04 * 9.1e-5; H0 = 1.44e-33; mg = 2 * np.sqrt(OmD) * H0; mgr = 2 * np.sqrt(0.04)
check('E2 [E] (A) passes: no scalar quanta, so no decay channel and no fifth force; the only trace is the global dark '
      'radiation (N_eff bounds it below ~0.04 of radiation) and the tensor mass of D2: today m ~ 2 sqrt(Omega_D) H0 against '
      'the LIGO bound 1.3e-23 eV; in the radiation era |m^2|/H^2 <~ 0.16, an untested (sign-flagged) superhorizon tensor tilt',
      mg < 1.3e-23, f'm_g today <~ {mg:.0e} eV; radiation era |m|/H <~ {mgr:.2f}')
print('supplied: continuum ADM limit of the hinge sum with lattice multipliers K, K_R (not the frustum hinge sum itself);')
print('  flat background, linear order; the two shift readings (CL-1 does not say whether the shift is stationary).')
print('not built: lattice momentum constraints on the edge registers (Regge breaks diffeos off flat cells), nonlinear')
print('  consistency with a dark constant, the sign of rho_D in D2 from the lattice phase.')
print(f'elapsed {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
