# sm55_1 -- exact symbolic checks of the W0 chart algebra (SEAM55 section 1).
# Criteria: checks/sm55_1_criteria.md (written before this script). sympy only; no floats in any verdict.
import sympy as sp

R, a, b0, b1, Binf, B1, B2, L = sp.symbols('R a b0 b1 Binf B1 B2 L', positive=True)
u, t, tt = sp.symbols('u t tt', positive=True)
x = sp.Matrix(sp.symbols('x1:5', real=True))
c = sp.Matrix(sp.symbols('c1:5', real=True))
T = sp.Function('T')

def dot(p, q):
    return (p.T * q)[0, 0]

r2 = dot(x, x)
Omega = 2 * R**2 / (R**2 + r2)
vc = R**2 * c + 2 * dot(c, x) * x - r2 * c          # boost field, south chart

def div(v):
    return sp.simplify(sum(sp.diff(v[i], x[i]) for i in range(4)))

def grad(f):
    return sp.Matrix([sp.diff(f, x[i]) for i in range(4)])

results = {}

# C1
divv = div(vc)
C1a = sp.simplify(divv - 8 * dot(c, x))
C1b = sp.simplify(dot(vc, grad(sp.log(Omega))) + divv / 4)
results['C1'] = (C1a == 0 and C1b == 0)

# C2: profile identity with undefined T
s_arg = sp.log(a * Omega)
uprof = T(s_arg)
C2expr = dot(vc, grad(uprof)) + (divv / 4) * sp.Subs(sp.Derivative(T(tt), tt), tt, s_arg).doit()
C2 = sp.simplify(C2expr)
results['C2'] = (C2 == 0)

# C3: north-chart representative: D phi(x) v_c(x) = -v_c(phi(x))
phi = R**2 * x / r2
Dphi = phi.jacobian(x)
vc_at_phi = vc.subs({x[i]: phi[i] for i in range(4)}, simultaneous=True)
C3a = sp.simplify(Dphi * vc + vc_at_phi)
C3b = sp.simplify(Dphi - ((R**2 / r2 - 1) * sp.eye(4) - 2 * (R**2 / r2**2 - 1 / R**2) * x * x.T)
                  - (sp.eye(4) - 2 * x * x.T / R**2))
results['C3'] = (C3a == sp.zeros(4, 1) and C3b == sp.zeros(4, 4))

# C4: Omega in the polar angle t from S; one-sided derivatives at t = pi/2
OmS_t = sp.simplify(Omega.subs(r2, (R * sp.tan(t / 2))**2))
OmN_t = sp.simplify(Omega.subs(r2, (R * sp.cot(t / 2))**2))     # north chart has the same Omega formula in y
C4a = sp.simplify(sp.trigsimp(OmS_t - (1 + sp.cos(t))))
C4b = sp.simplify(sp.trigsimp(OmN_t - (1 - sp.cos(t))))
dS = sp.diff(1 + sp.cos(t), t).subs(t, sp.pi / 2)
dN = sp.diff(1 - sp.cos(t), t).subs(t, sp.pi / 2)
results['C4'] = (C4a == 0 and C4b == 0 and dS == -1 and dN == 1)

# C5: conformal Killing in the chart: symmetric part of d_mu v_nu - (div v/4) delta vanishes
J = vc.jacobian(x)            # J[i, j] = d v_i / d x_j
symm = sp.simplify((J + J.T) / 2 - (divv / 4) * sp.eye(4))
results['C5'] = (symm == sp.zeros(4, 4))

# C6: P4 two-loop profile slope
logf = (b1 / (2 * b0**2)) * sp.log(u / b0) - u / (2 * b0)
slope = sp.simplify(1 / sp.diff(logf, u))
C6a = sp.simplify(slope - (-2 * b0 / (1 - b1 / (b0 * u))))
w = sp.symbols('w', positive=True)          # w = 1/u
ser = sp.series(slope.subs(u, 1 / w), w, 0, 3).removeO()
C6b = sp.simplify(sp.expand(ser - (-2 * b0 - 2 * b1 * w - 2 * b1**2 / b0 * w**2)))
results['C6'] = (C6a == 0 and C6b == 0)

# C7: value-problem dependence of the G-pert profile
Blat = Binf + B1 / u + B2 / u**2
Bpert = 2 * b0 + 2 * b1 / u + 2 * b1**2 / (b0 * u**2)
c4p = (Blat - Bpert) / Blat
lim = sp.limit(c4p, u, sp.oo)
C7a = sp.simplify(lim - (Binf - 2 * b0) / Binf)
c4p_val = sp.simplify(c4p.subs({Binf: 2 * b0, B1: 2 * b1}))
ser7 = sp.series(c4p_val.subs(u, 1 / w), w, 0, 2).removeO()   # orders w^0 and w^1 must vanish
C7b = sp.simplify(ser7)
results['C7'] = (C7a == 0 and C7b == 0)

# C8: interpolation error of the trajectory profile in the two-loop model B(u) = 2 b0 + 2 b1/u
lnL = sp.symbols('lnL', positive=True)
d0, d1, d2 = sp.symbols('d0 d1 d2')
Delta = d0 + d1 * w + d2 * w**2                 # step running, series in w = 1/u
B = lambda uu: 2 * b0 + 2 * b1 / uu
# integral_u^{u+Delta} du'/B(u') with B = 2 b0 + 2 b1/u' : exact antiderivative
up = sp.symbols('up', positive=True)
F = sp.integrate(up / (2 * b0 * up + 2 * b1), up)
integ = (F.subs(up, 1 / w + Delta) - F.subs(up, 1 / w))
eq = sp.series(integ - lnL, w, 0, 3).removeO()
sol = sp.solve([sp.expand(eq).coeff(w, k) for k in range(3)], [d0, d1, d2], dict=True)
ok8 = False
if sol:
    Dsol = Delta.subs(sol[0])
    diffexpr = Dsol / lnL - B(1 / w + tt * Dsol)
    ser8 = sp.series(diffexpr, w, 0, 2).removeO()
    ok8 = (sp.simplify(ser8) == 0)
results['C8'] = ok8

# C9: exponent arithmetic of the two-scale thresholds
from fractions import Fraction as Fr
E10 = {'seam': Fr(1) / Fr(7, 2), 'bulk': Fr(2) / Fr(4), 'dil': Fr(1) / Fr(2)}
cor = {'seam': Fr(1) / (Fr(7, 2) + 4), 'bulk': Fr(2) / (4 + 4), 'dil': Fr(1) / (2 + 4)}
results['C9'] = (E10 == {'seam': Fr(2, 7), 'bulk': Fr(1, 2), 'dil': Fr(1, 2)}
                 and cor == {'seam': Fr(2, 15), 'bulk': Fr(1, 4), 'dil': Fr(1, 6)})

# ---- controls (must FIRE) ----
controls = {}
uwrong = T(sp.log(a * Omega**2))
X1 = sp.simplify(dot(vc, grad(uwrong)) + (divv / 4) * sp.Subs(sp.Derivative(T(tt), tt), tt, sp.log(a * Omega**2)).doit())
controls['X1'] = (X1 != 0)
wtr = R**2 * c
X2 = sp.simplify(dot(wtr, grad(sp.log(Omega))) + div(wtr) / 4)
controls['X2'] = (X2 != 0)
X3 = sp.simplify(Dphi * vc - vc_at_phi)
controls['X3'] = (X3 != sp.zeros(4, 1))
limX4 = sp.limit(c4p.subs(Binf, sp.Rational(11, 10) * 2 * b0), u, sp.oo)
controls['X4'] = (sp.simplify(limX4 - sp.Rational(1, 11)) == 0 and limX4 != 0)
X5 = sp.simplify(sp.trigsimp(OmN_t - (1 + sp.cos(t))))
controls['X5'] = (X5 != 0)

for k in sorted(results):
    print(k, 'PASS' if results[k] else 'FAIL')
for k in sorted(controls):
    print(k, 'FIRED' if controls[k] else 'DID-NOT-FIRE')
print('C1 detail: div v - 8 c.x =', C1a, '; v.grad log Omega + div v/4 =', C1b)
print('C7 limit:', sp.simplify(lim))
print('X4 limit:', limX4)
verdict = all(results.values()) and all(controls.values())
print('VERDICT:', 'PASS' if verdict else 'FAIL')
