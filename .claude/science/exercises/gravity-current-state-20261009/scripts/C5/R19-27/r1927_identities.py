"""R19-27 (a): exact identities for an isotropic H-cov vacuum term  Gamma = -Int sqrt(-g) F(n, phi),
n = sqrt(det b), b^{IJ} = g^{mu nu} d_mu X^I d_nu X^J (R19-17's lattice-frame fields X^I).

E1 (stress identity):   T_{mu nu} = -F g_{mu nu} + n dF/dn h_{mu nu},  h = (b^-1)_{IJ} dX^I dX^J  (projector orthogonal to u),
                         so rho = F, p = n F_n - F, W = rho + p = n F_n.          [checked numerically at a random Lorentzian point]
E2 (frame energy leg):  u^mu d_mu X^I = 0, so the Noether force term E_I grad^nu X^I has no u-component:
                         the lattice frame can receive only momentum legs, never the energy leg W theta.   [checked]
E3 (homogeneous V1):    with n = n0 a^-3, rho_dot + 3H(rho+p) = F_phi phi_dot  (identity; the energy leg of W is the
                         vacuum term's own drift).                                                   [sympy]
E4 (force on lattice):  static 1D, X^1 = x + xi(x): E_1 = d/dx[F_n] -> at xi = 0, E_1 = F_{n phi} phi'  = (d/dx W)|_{explicit phi}.
                         LCP form F = F0(n) + DV(phi): E_1 = 0.  Lorentz-invariant counterterm form F = F0 + c1 n m(phi) + Vct(phi):
                         E_1 = c1 m'(phi) phi' = d/dx (state-dependent W).                            [sympy]
E5 (reading-A balance): F_I = 0 with the LI form forces F0'(n) + c1 m(phi) = const: delta n = -c1 delta m / F0''(n).  [sympy]
"""
import numpy as np, sympy as sp
rng = np.random.default_rng(27)
out = []
# ---------- E1, E2: numeric point check ----------
def lorentz_metric():
    A = rng.normal(size=(4, 4)); eta = np.diag([-1., 1, 1, 1])
    L = np.eye(4) + 0.3*A
    return L.T @ eta @ L                     # g_{mu nu}, Lorentzian (signature preserved for small perturbation)
g = lorentz_metric(); gi = np.linalg.inv(g)
assert np.sum(np.linalg.eigvalsh(g) < 0) == 1
dX = np.array([[0.2, 1.0, 0.1, -0.3], [-0.1, 0.2, 0.9, 0.2], [0.3, -0.2, 0.1, 1.1]])   # d_mu X^I, rows I
c43, c1 = 1.7, -0.69
def F(n): return c43*n**(4/3) + c1*n                # radiation-like sea piece + per-site (dust-like) piece
def Fn(n): return (4/3)*c43*n**(1/3) + c1
def L_of_ginv(Gi):
    G = np.linalg.inv(Gi); b = dX @ Gi @ dX.T; n = np.sqrt(np.linalg.det(b))
    return np.sqrt(-np.linalg.det(G))*F(n)
# T_{mu nu} = (2/sqrt-g) d(sqrt-g F)/d g^{mu nu}  (Gamma = -Int sqrt-g F; T = -(2/sqrt-g) dGamma/dg^{mu nu})
h = 1e-5; Tnum = np.zeros((4, 4))
for m in range(4):
    for v in range(m, 4):
        E = np.zeros((4, 4)); E[m, v] += 1; E[v, m] += 1
        if m == v: E[m, m] = 1
        d = (L_of_ginv(gi + h*E) - L_of_ginv(gi - h*E))/(2*h)
        val = d if m == v else d/2
        Tnum[m, v] = Tnum[v, m] = 2*val/np.sqrt(-np.linalg.det(g))
b = dX @ gi @ dX.T; n = np.sqrt(np.linalg.det(b)); hproj = dX.T @ np.linalg.inv(b) @ dX
Tform = -F(n)*g + n*Fn(n)*hproj
out.append('E1  max|T_num - (-F g + n F_n h)| = %.2e   (scale %.2e)' % (np.abs(Tnum - Tform).max(), np.abs(Tform).max()))
# u from epsilon contraction; check u.dX = 0, h u = 0, h projector
eps = np.zeros((4,)*4)
import itertools
for p in itertools.permutations(range(4)):
    eps[p] = np.linalg.det(np.eye(4)[list(p)])
u_up = np.einsum('mnrs,n,r,s->m', eps, dX[0], dX[1], dX[2])
u_up = u_up/np.sqrt(-u_up @ g @ u_up)
u_dn = g @ u_up
out.append('E2  |u^mu d_mu X^I| = %s ;  |h_{mu nu} u^nu| = %.1e ;  |h g^-1 h - h| = %.1e ;  h = g + u u: %.1e'
           % (np.array2string(np.abs(dX @ u_up), precision=1), np.abs(hproj @ u_up).max(),
              np.abs(hproj @ gi @ hproj - hproj).max(), np.abs(hproj - (g + np.outer(u_dn, u_dn))).max()))
rho = u_up @ Tform @ u_up; ptr = (np.einsum('mn,mn->', gi, Tform) + rho)/3
out.append('E1  rho = %.9f vs F = %.9f ;  p = %.9f vs nF_n - F = %.9f ;  W = %.9f vs nF_n = %.9f'
           % (rho, F(n), ptr, n*Fn(n) - F(n), rho + ptr, n*Fn(n)))
# ---------- E3: homogeneous V1 identity ----------
t = sp.symbols('t'); a = sp.Function('a')(t); ph = sp.Function('phi')(t); n0 = sp.symbols('n0', positive=True)
nn, pp = sp.symbols('n p_hi', positive=True)
Fs = sp.Function('F')(nn, pp)
ns = n0*a**-3
rho_t = Fs.subs({nn: ns, pp: ph}); W_t = (nn*sp.diff(Fs, nn)).subs({nn: ns, pp: ph})
H = sp.diff(a, t)/a
lhs = sp.diff(rho_t, t) + 3*H*W_t
rhs = sp.diff(Fs, pp).subs({nn: ns, pp: ph})*sp.diff(ph, t)
out.append('E3  rho_dot + 3H W - F_phi phi_dot = %s' % sp.simplify(lhs - rhs))
# ---------- E4, E5: force on the lattice (static, flat, 1D strain) ----------
x = sp.symbols('x'); xi = sp.Function('xi')(x); phx = sp.Function('phi')(x)
F0 = sp.Function('F0'); DV = sp.Function('DV'); m = sp.Function('m'); Vct = sp.Function('Vct'); c1s = sp.symbols('c1')
def E1_of(Fexpr_of_n_phi):
    nx = 1 + sp.diff(xi, x)                                    # n = |dX^1/dx| (flat metric, X^2 = y, X^3 = z)
    Lag = -Fexpr_of_n_phi(nx, phx)                             # static Lagrangian density (Gamma = -Int F)
    EL = sp.diff(sp.diff(Lag, sp.diff(xi, x)), x)*(-1)         # dGamma/dxi = -d/dx dL/dxi'  (L has no xi)
    return sp.simplify(EL.subs(xi, 0).doit())
E_lcp = E1_of(lambda n_, p_: F0(n_) + DV(p_))
E_li = E1_of(lambda n_, p_: F0(n_) + c1s*n_*m(p_) + Vct(p_))
out.append('E4  LCP form F0(n)+DV(phi):            E_1|xi=0 = %s' % E_lcp)
out.append('E4  LI-counterterm form F0+c1 n m+Vct: E_1|xi=0 = %s' % E_li)
Wli = (nn*sp.diff(F0(nn) + c1s*nn*m(pp) + Vct(pp), nn)).subs({nn: 1, pp: phx})
out.append('E4  d/dx[W_state] (LI form, n=1) = %s   -> E_1 = d/dx W_state: %s'
           % (sp.simplify(sp.diff(Wli - sp.diff(F0(nn), nn).subs(nn, 1), x)), sp.simplify(E_li - sp.diff(Wli, x).subs(sp.Derivative(F0(1), x), 0)) == 0))
# E5: reading-A constraint for general n(x): d/dx F_n(n(x), phi(x)) = 0
A43 = sp.symbols('A', positive=True); dn, dm = sp.symbols('delta_n delta_m'); nb, mb = sp.symbols('nbar mbar', positive=True)
Fn_li = lambda n_, M_: sp.diff(A43*nn**sp.Rational(4, 3) + c1s*nn*M_, nn).subs(nn, n_)   # F0 = A n^{4/3} (sea's m-independent piece)
lin = sp.series(Fn_li(nb + dn, mb + dm) - Fn_li(nb, mb), dn, 0, 2).removeO()
sol = sp.solve(sp.expand(lin), dn)
out.append('E5  reading A (F_1 = 0), F0 = A n^(4/3), LI form: delta n = %s  [first order in delta m]' % [sp.simplify(s_) for s_ in sol])
print('\n'.join(out))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
