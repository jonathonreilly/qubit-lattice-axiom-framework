"""R15-4 (b): the lumpy universe in the R14-5 CMC model.

Part A (sympy, algebra of the model; R14-5 H-imp: E_ni = 0, E^TL = 0, E_nn(x) = lambda(t); CMC theta(t) uniform;
        Lemma C: lambda' = -g theta; clock law -D^2 N + Qt N = S(t), <N> = 1, g = -(2/3)(theta' + S);
        Qt = K_ij K^ij + (kappa/2)(rho+3p)_nc - Lt, Lt = lambda + kappa rho_v (R14-5 report:165-168, referee sec. 3)).
  A1  calE(x) := kappa T_nn^tot - R/2 + sigma2/2 = theta^2/3 - lambda : uniform on each slice (so readable at any site).
  A2  Lt = theta^2/3 - calE_nc, calE_nc := calE - kappa rho_v = kappa rho_nc - R/2 + sigma2/2 (pointwise, uniform).
  A3  Qt = calE_nc + sigma2 + (kappa/2)(rho+3p)_nc   (exact; no dropped terms) = (3kappa/2)(rho+p)_nc - R/2 + (3/2) sigma2.
  A4  d calE/dt = -(2/3) theta S, i.e. d calE/du = -2S (u: theta = 3 du/dt); S = <Qt N> > 0 when N > 0.
  A5  homogeneous: S = (3kappa/2)(rho+p)_nc, g = -2H' - kappa(rho+p)_nc (R14-5 r145_homog.py:7).
Part B (numerics): <R>_vol = 2 int e^{-Psi}|grad Psi|^2 / int e^{-3Psi} for h = e^{-2Psi} delta on T^3 (identity, checked
        on a random periodic field), and the conformal scalar-curvature formula (sympy, Psi(x,y)).
Part C (magnitude; comparator inputs RECALLED: BBKS transfer, Omega_m=0.31, h=0.677, n_s=0.965, sigma_8=0.81; linear
        theory): <R>/H0^2 and <sigma^2>/H0^2 today; Lt for (i) R14-5's <rho>-reader, Lt = <R>/2 - <sigma^2>/2, and
        (ii) the calE-reader, Lt = R[B] - B with B = -<R>/2 + <sigma^2>/2 (linear-theory history B ~ (D/a)^2 a^-2).
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r154_reader import DESIGNS

print('# Part A (sympy)')
th, lam, kap, rnc, rv, p, R, s2, g, S, thd = sp.symbols('theta lambda kappa rho_nc rho_v p R sigma2 g S thetadot', real=True)
Gnn = R / 2 + th ** 2 / 3 - s2 / 2
lam_sol = Gnn - kap * (rnc + rv)                          # E_nn = lambda
calE = kap * (rnc + rv) - R / 2 + s2 / 2
calEnc = calE - kap * rv
Lt = lam_sol + kap * rv
print('A1 calE - (theta^2/3 - lambda) =', sp.simplify(calE - (th ** 2 / 3 - lam_sol)))
print('A2 Lt - (theta^2/3 - calE_nc) =', sp.simplify(Lt - (th ** 2 / 3 - calEnc)))
Qt = th ** 2 / 3 + s2 + kap / 2 * (rnc + 3 * p) - Lt
print('A3 Qt - (calE_nc + sigma2 + kappa/2 (rho+3p)) =', sp.simplify(Qt - (calEnc + s2 + kap / 2 * (rnc + 3 * p))),
      '; Qt - [(3k/2)(rho+p) - R/2 + 3 sigma2/2] =', sp.simplify(Qt - (sp.Rational(3, 2) * kap * (rnc + p) - R / 2 + sp.Rational(3, 2) * s2)))
lamdot = -g * th
calEdot = sp.Rational(2, 3) * th * thd - lamdot
print('A4 dcalE/dt + (2/3) theta S with g = -(2/3)(thetadot+S):', sp.simplify(calEdot.subs(g, -sp.Rational(2, 3) * (thd + S)) + sp.Rational(2, 3) * th * S))
Shom = Qt.subs({R: 0, s2: 0})
print('A5 homogeneous S = Qt(N=1) =', sp.factor(sp.simplify(Shom.subs(th, sp.sqrt(3 * kap * rnc)))), '(exact reader, theta^2/3 = kappa rho_nc)')
H = sp.symbols('H', positive=True); Hd = sp.symbols('Hdot', real=True)
print('    g(theta=3H) =', sp.expand((-sp.Rational(2, 3) * (3 * Hd + Shom.subs(th, sp.sqrt(3 * kap * rnc))))))

print('\n# Part B: conformal curvature formula and the volume average')
x, y, z = sp.symbols('x y z', real=True)
Psi = sp.Function('Psi')(x, y)
hmat = sp.diag(sp.exp(-2 * Psi), sp.exp(-2 * Psi), sp.exp(-2 * Psi))
X = [x, y, z]; hinv = hmat.inv()
Gam = [[[sum(hinv[a, d] * (sp.diff(hmat[d, b], X[c]) + sp.diff(hmat[d, c], X[b]) - sp.diff(hmat[b, c], X[d])) for d in range(3)) / 2
         for c in range(3)] for b in range(3)] for a in range(3)]
def Ric(b, c):
    return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                           + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(3)) for a in range(3)))
Rs = sp.simplify(sum(hinv[b, c] * Ric(b, c) for b in range(3) for c in range(3)))
lap = sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2); gr2 = sp.diff(Psi, x) ** 2 + sp.diff(Psi, y) ** 2
print('   R - e^{2Psi}(4 lap Psi - 2|grad Psi|^2) =', sp.simplify(Rs - sp.exp(2 * Psi) * (4 * lap - 2 * gr2)))
n = 64; Lb = 2 * np.pi
rng = np.random.default_rng(3)
kv = np.fft.fftfreq(n, d=Lb / n) * 2 * np.pi
KX, KY, KZ = np.meshgrid(kv, kv, kv, indexing='ij'); K2 = KX ** 2 + KY ** 2 + KZ ** 2
ph = np.fft.fftn(rng.standard_normal((n, n, n))) * np.exp(-K2 / 8.0)
Ps = np.real(np.fft.ifftn(ph)); Ps *= 0.3 / Ps.std()
Pk = np.fft.fftn(Ps)
gx, gy, gz = [np.real(np.fft.ifftn(1j * Kc * Pk)) for Kc in (KX, KY, KZ)]
lapP = np.real(np.fft.ifftn(-K2 * Pk)); g2 = gx ** 2 + gy ** 2 + gz ** 2
Rfield = np.exp(2 * Ps) * (4 * lapP - 2 * g2)
vol = np.exp(-3 * Ps)
lhs = np.sum(vol * Rfield) / np.sum(vol); rhs = 2 * np.sum(np.exp(-Ps) * g2) / np.sum(vol)
print(f'   T^3 random Psi (rms 0.3): <R>_vol = {lhs:.8f}, 2<e^(-Psi)|grad Psi|^2>/<e^(-3Psi)> = {rhs:.8f}; <R> > 0; min R = {Rfield.min():.3f} (R not >= 0 pointwise)')

print('\n# Part C: magnitude (linear theory; inputs RECALLED)')
Om, h, ns, s8 = 0.31, 0.677, 0.965, 0.81
H0 = 1 / 2997.92                                           # h/Mpc, c = 1
def T_bbks(k):
    q = k / (Om * h)
    return np.log(1 + 2.34 * q) / (2.34 * q) * (1 + 3.89 * q + (16.1 * q) ** 2 + (5.46 * q) ** 3 + (6.71 * q) ** 4) ** -0.25
P0 = lambda k: k ** ns * T_bbks(k) ** 2
W = lambda x: 3 * (np.sin(x) - x * np.cos(x)) / x ** 3
s8raw = quad(lambda lk: np.exp(lk) ** 3 * P0(np.exp(lk)) * W(8 * np.exp(lk)) ** 2 / (2 * np.pi ** 2), np.log(1e-5), np.log(50), limit=400)[0]
A = s8 ** 2 / s8raw
P = lambda k: A * P0(k)
I1 = quad(lambda lk: np.exp(lk) * P(np.exp(lk)) / (2 * np.pi ** 2), np.log(1e-5), np.log(20), limit=400)[0]
I2 = quad(lambda lk: np.exp(lk) ** -1 * P(np.exp(lk)) / (2 * np.pi ** 2), np.log(1e-4), np.log(20), limit=400)[0]
f = Om ** 0.55
R_H2 = 4.5 * Om ** 2 * H0 ** 2 * I1
s2_H2 = 13.5 * Om ** 2 * f ** 2 * H0 ** 4 * I2
Lobs = 3 * (1 - Om)
print(f'   int P dk/2pi^2 = {I1:.2f} (Mpc/h)^2 [3D displacement variance], int P/k^2 dk/2pi^2 = {I2:.3e} (Mpc/h)^4')
print(f'   <R>/H0^2 = {R_H2:.3e};  <sigma^2>/H0^2 = {s2_H2:.3e} (suggested normalisation)')
Lt_rho = 0.5 * R_H2 - 0.5 * s2_H2
print(f'   (i) R14-5 <rho>-reader: Lt/H0^2 = {Lt_rho:+.3e}; Lt/Lambda_obs = {Lt_rho/Lobs:+.3e} (Lambda_obs = 3 Omega_L H0^2)')
# growth D(a) in flat LCDM, B(a) = -<R>/2 * (D/a)^2/a^2 normalised at a=1 (sigma^2 negligible)
def Dgrowth(a):
    E = lambda aa: np.sqrt(Om / aa ** 3 + 1 - Om)
    return 2.5 * Om * E(a) * quad(lambda aa: 1 / (aa * E(aa)) ** 3, 0, a)[0]
D1 = Dgrowth(1.0)
us = np.linspace(np.log(1e-3), 0, 3001)
Bv = np.array([-(Dgrowth(np.exp(u)) / D1 / np.exp(u)) ** 2 * np.exp(-2 * u) for u in us]) * 0.5 * R_H2  # units H0^2/kappa*... (kappa=1)
EB = -np.gradient(Bv, us)
for name in ('D1 minimal (2 regs)', 'R* fast (2 regs, beta 20,24)'):
    b, k = DESIGNS[name]
    y0 = (2 * Bv[0]) / (b - 2)          # equilibrium for an x=2 component (B ~ a^-2 in the matter era)
    sol = solve_ivp(lambda u, yv: np.interp(u, us, EB) - b * yv, (us[0], 0), y0, t_eval=us, rtol=1e-10, atol=1e-30, method='DOP853', max_step=0.01)
    RB = k @ sol.y
    Lt_E = RB[-1] - Bv[-1]
    print(f'   (ii) calE-reader {name}: R[B]/B (a=1) = {RB[-1]/Bv[-1]:.4f}; Lt/H0^2 = {Lt_E:+.3e}; Lt/Lambda_obs = {Lt_E/Lobs:+.3e}')
