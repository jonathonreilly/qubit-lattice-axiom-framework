"""K1: full Lorentz-violating mass matrix of a metric coupled to a medium of
spatial labels phi^I (I=1..3), unitary gauge phi^I = x^I, around Minkowski.

L = sqrt(-g) [ F(B) - Lam ],  B^{IJ} = g^{mu nu} d_mu phi^I d_nu phi^J.
Fluid: F = F(b), b = sqrt(det B).  Solid: F = F(tr B, tr B^2, det B).
Signature (-,+,+,+).  Bookkeeping parameter eps; expand to eps^2.

Outputs:
 (1) tadpole (first order) -> conditions for Minkowski to be a solution;
 (2) quadratic mass terms: coefficients of h00^2, h0i h0i, hij hij, (hii)^2, h00 hii;
 (3) Stueckelberg check on Minkowski (h=0): phi^I = x^I + pi^I, quadratic
     action in pi; kinetic coefficient vs enthalpy w = rho + p.
"""
import sympy as sp

eps = sp.symbols('eps')
h = sp.Matrix(4, 4, lambda i, j: sp.Symbol('h%d%d' % (min(i, j), max(i, j))))
eta = sp.diag(-1, 1, 1, 1)
etai = eta.inv()
H = etai * h  # eta^{-1} h
# inverse metric to second order: g^{-1} = eta^-1 - eta^-1 h eta^-1 + eta^-1 h eta^-1 h eta^-1
ginv = etai - eps * etai * h * etai + eps**2 * etai * h * etai * h * etai
trH = H.trace()
trH2 = (H * H).trace()
sqrtg = 1 + eps * trH / 2 + eps**2 * (trH**2 / 8 - trH2 / 4)

B = ginv[1:, 1:]  # unitary gauge: d_mu phi^I = delta_mu^I
X = B - sp.eye(3)
trX = X.trace()
trX2 = (X * X).trace()
detB = 1 + trX + (trX**2 - trX2) / 2  # exact to eps^2 since X = O(eps)
trB = B.trace()
trB2 = (B * B).trace()


def series2(expr):
    return sp.series(sp.expand(expr), eps, 0, 3).removeO()


def read_masses(L2, label):
    """L2 = eps^2 coefficient. Read coefficients in the isotropic basis."""
    L2 = sp.expand(L2)
    c = {}
    c['h00^2'] = L2.coeff(sp.Symbol('h00'), 2).subs({s: 0 for s in L2.free_symbols if str(s).startswith('h')})
    c['h01^2 (x2 for h0i h0i convention)'] = sp.expand(L2).coeff(sp.Symbol('h01'), 2).subs({s: 0 for s in L2.free_symbols if str(s).startswith('h')})
    # h_ij h_ij coefficient: from off-diagonal h12 (appears twice in hij hij)
    c12 = L2.coeff(sp.Symbol('h12'), 2).subs({s: 0 for s in L2.free_symbols if str(s).startswith('h')})
    # diag: h11^2 coefficient = A + D (A: hij hij, D: (hii)^2) ; h11 h22 coeff = 2D
    c11 = L2.coeff(sp.Symbol('h11'), 2).subs({s: 0 for s in L2.free_symbols if str(s).startswith('h')})
    c1122 = sp.expand(L2.coeff(sp.Symbol('h11'), 1).coeff(sp.Symbol('h22'), 1)).subs({s: 0 for s in L2.free_symbols if str(s).startswith('h')})
    c0011 = sp.expand(L2.coeff(sp.Symbol('h00'), 1).coeff(sp.Symbol('h11'), 1)).subs({s: 0 for s in L2.free_symbols if str(s).startswith('h')})
    A = sp.simplify(c12 / 2)       # coefficient of h_ij h_ij  (h12^2 appears as 2 A h12^2)
    D = sp.simplify(c1122 / 2)     # coefficient of (h_ii)^2
    print(f'--- {label}: quadratic terms  L2 = a h00^2 + b h0i h0i + A hij hij + D (hii)^2 + E h00 hii')
    print('  a (h00^2)      =', sp.simplify(c['h00^2']))
    print('  b (h0i h0i)    =', sp.simplify(c['h01^2 (x2 for h0i h0i convention)'] / 2))
    print('  A (hij hij)    =', A, '   [m2^2 ~ -A ; TT mass]')
    print('  check: h11^2 coeff - (A+D) =', sp.simplify(c11 - A - D))
    print('  D ((hii)^2)    =', D, '   [m3^2 ~ D]')
    print('  E (h00 hii)    =', sp.simplify(c0011))
    return A, D


def tadpole(L1):
    L1 = sp.expand(L1)
    out = {}
    for s in ['h00', 'h11', 'h01', 'h12']:
        out[s] = sp.simplify(L1.coeff(sp.Symbol(s), 1))
    return out


Lam = sp.symbols('Lam')
# ---------------- fluid ----------------
F0, F1, F2 = sp.symbols('F0 F1 F2')  # F(b) = F0 + F1 (b-1) + F2/2 (b-1)^2 at b0 = 1
b = sp.sqrt(detB)
db = series2(b - 1)
Ffl = F0 + F1 * db + F2 / 2 * db**2
L = series2(sqrtg * (Ffl - Lam))
L1 = L.coeff(eps, 1)
L2 = L.coeff(eps, 2)
print('=== FLUID F(b)')
tp = tadpole(L1)
print('tadpole coefficients (must vanish for Minkowski):', tp)
# rho = Lam - F0 (coefficient of h00 with sign), p from h11
sol = sp.solve([tp['h00'], tp['h11']], [Lam, F1], dict=True)
print('Minkowski conditions:', sol)
print('  => enthalpy w = rho + p = -F1 must vanish (F1 = dF/db at b0)')
read_masses(L2, 'fluid, general background (not a solution unless F1 = 0)')
L2m = sp.expand(L2.subs(sol[0]))
A, D = read_masses(L2m, 'fluid on Minkowski (F1 = 0, Lam = F0)')

# ---------------- solid ----------------
S0, S1, S2, S3, S11, S22, S33, S12, S13, S23 = sp.symbols('S0 S1 S2 S3 S11 S22 S33 S12 S13 S23')
t1 = series2(trB - 3)
t2 = series2(trB2 - 3)
t3 = series2(detB - 1)
Fs = (S0 + S1 * t1 + S2 * t2 + S3 * t3
      + S11 / 2 * t1**2 + S22 / 2 * t2**2 + S33 / 2 * t3**2
      + S12 * t1 * t2 + S13 * t1 * t3 + S23 * t2 * t3)
L = series2(sqrtg * (Fs - Lam))
L1 = L.coeff(eps, 1)
L2 = L.coeff(eps, 2)
print('\n=== SOLID F(trB, trB^2, detB)')
tp = tadpole(L1)
print('tadpole:', tp)
sol = sp.solve([tp['h00'], tp['h11']], [Lam, S3], dict=True)
print('Minkowski conditions:', sol)
L2m = sp.expand(L2.subs(sol[0]))
read_masses(L2m, 'solid on Minkowski')

# ---------------- Stueckelberg on Minkowski ----------------
print('\n=== Stueckelberg modes of the fluid on fixed Minkowski (h = 0)')
t, x, y, z = sp.symbols('t x y z')
# constant-gradient bookkeeping: d_mu pi^I = P[mu, I] symbols
P = sp.Matrix(4, 3, lambda m, I: sp.Symbol('P%d%d' % (m, I + 1)))
J = sp.Matrix(4, 3, lambda m, I: (1 if m == I + 1 else 0)) + eps * P  # d_mu phi^I
Bst = J.T * etai * J
Xs = Bst - sp.eye(3)
detBs = sp.expand(Bst.det())
db_s = series2(sp.sqrt(series2(detBs)) - 1)
Lst = series2(F0 + F1 * db_s + F2 / 2 * db_s**2 - Lam)
L2s = sp.expand(Lst.coeff(eps, 2))
print('quadratic pi action (P0I = d_t pi^I, PjI = d_j pi^I):')
print('  coefficient of (d_t pi^1)^2 :', sp.simplify(L2s.coeff(sp.Symbol('P01'), 2)))
print('  coefficient of (d_1 pi^1)^2 :', sp.simplify(L2s.coeff(sp.Symbol('P11'), 2)))
print('  coefficient of (d_2 pi^1)^2 (transverse gradient):', sp.simplify(L2s.coeff(sp.Symbol('P21'), 2)))
print('  coefficient of d_1pi^2 d_2pi^1 :', sp.simplify(L2s.coeff(sp.Symbol('P12'), 1).coeff(sp.Symbol('P21'), 1)))
print('  => kinetic term = (-F1/2) (d_t pi)^2 = (w/2) (d_t pi)^2 ; on Minkowski (F1 = 0) it vanishes.')
L2s_m = sp.expand(L2s.subs({F1: 0}))
print('  quadratic pi action at F1 = 0:', sp.factor(L2s_m))
