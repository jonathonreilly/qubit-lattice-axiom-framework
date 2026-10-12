"""R15-1 (b): quadratic scalar action of GR + canonical scalar chi + the R14-5 E-sector
on flat FRW, in the E-sector's own time (lattice/CMC time; time reparametrisation is broken).
E-sector action (kappa = 1):  S_E = int dt d^3x sqrt(h) [ g(t) - N lam(t) ].
  Varying N gives E_nn = lam; varying h_ij gives p_E = g/N - lam  (R14-5 Sec. 4.1 item 5).
  This is the cuscuton in unitary gauge with V(phi(t)) = lam, mu^2 phidot = g.
Perturbations: N = 1+alpha, N_i = d_i beta, h_ij = a^2 e^{2 zeta} delta_ij (spatial gauge E = 0), chi = chi0 + dchi.
Fields depend on (t, x); each perturbation ~ eps * f(t) cos(k x) (beta ~ eps*b(t) cos kx), averaged over x.
Outputs: background equations; after solving the alpha, beta constraints, the kinetic matrix of (zeta, dchi),
its rank, the sign of the surviving kinetic coefficient, and omega^2(k) (gradient / tachyon check).
"""
import sympy as sp
t, x, k, eps = sp.symbols('t x k epsilon', positive=True)
a = sp.Function('a')(t); chi0 = sp.Function('chi0')(t)
g = sp.Function('g')(t); lam = sp.Function('lam')(t)
Vf = sp.Function('V')
al, b, ze, dc = [sp.Function(n)(t) for n in ('alpha', 'b', 'zeta', 'dchi')]
c = sp.cos(k*x); s = sp.sin(k*x)
N = 1 + eps*al*c
beta = eps*b*c
om = sp.log(a) + eps*ze*c          # h_ij = e^{2 om} delta_ij
chi = chi0 + eps*dc*c
X = [x, sp.Symbol('y'), sp.Symbol('z')]
h = sp.exp(2*om)*sp.eye(3); hi = sp.exp(-2*om)*sp.eye(3)
Ni = sp.Matrix([sp.diff(beta, x), 0, 0])
d = lambda f, i: sp.diff(f, X[i])
Gam = [[[ (1 if kk == i else 0)*d(om, j) + (1 if kk == j else 0)*d(om, i) - (1 if i == j else 0)*d(om, kk)
          for j in range(3)] for i in range(3)] for kk in range(3)]
DN = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        DN[i, j] = d(Ni[j], i) - sum(Gam[kk][i][j]*Ni[kk] for kk in range(3))
K = (sp.diff(h, t) - DN - DN.T)/(2*N)
Kup = hi*K*hi
KK = sum(K[i, j]*Kup[i, j] for i in range(3) for j in range(3))
trK = sum(hi[i, j]*K[i, j] for i in range(3) for j in range(3))
R3 = -sp.exp(-2*om)*(4*sp.diff(om, x, 2) + 2*sp.diff(om, x)**2)
sqh = sp.exp(3*om)
Nup = hi*Ni
chidot = sp.diff(chi, t) - Nup[0]*sp.diff(chi, x)
L = sqh*(N/2*(R3 + KK - trK**2) + chidot**2/(2*N) - N*(hi[0, 0]*sp.diff(chi, x)**2/2 + Vf(chi)) + g - N*lam)
Ls = sp.series(L, eps, 0, 3).removeO()
L1 = sp.expand(Ls.coeff(eps, 1)); L2 = sp.expand(Ls.coeff(eps, 2)); L0 = Ls.coeff(eps, 0)
P = 2*sp.pi/k
avg = lambda e: sp.simplify(sp.integrate(sp.expand(e), (x, 0, P))/P)
# background equations: vary homogeneous N, a, chi in L0 with N0 -> use first-order coefficient of alpha's zero mode
N0, A0 = sp.symbols('N0 A0')
# homogeneous action with general N0(t): redo quickly
Nt = sp.Function('Nt')(t)
Lh = a**3*(Nt/2*(-6*sp.diff(a, t)**2/(a**2*Nt**2)) + sp.diff(chi0, t)**2/(2*Nt) - Nt*Vf(chi0) + g - Nt*lam)
EN = sp.simplify(sp.diff(Lh, Nt).subs(Nt, 1))
Ea = sp.simplify((sp.diff(Lh, a) - sp.diff(sp.diff(Lh, sp.diff(a, t)), t)).subs(Nt, 1).doit())
print("background N-eq (=0):", EN)
print("background a-eq (=0):", sp.simplify(Ea/a**2))
H, Hd, cd, V0, V2, gs, ls, gd = sp.symbols('H Hdot chidot V0 Vpp g lam gdot')
# solve background: EN=0 -> lam = 3H^2 - cd^2/2 - V0 ; Ea -> g = -2Hdot - cd^2
L2a = avg(L2)
print("L1 averaged (should vanish for cos modes):", avg(L1))
# replace background derivatives by symbols
rep = {}
L2s = L2a.subs({sp.Derivative(a, (t, 2)): a*(Hd + H**2)}).subs({sp.Derivative(a, t): a*H})
L2s = L2s.subs({sp.Derivative(chi0, (t, 2)): sp.Symbol('chiddot')}).subs({sp.Derivative(chi0, t): cd})
L2s = L2s.subs({sp.Subs(sp.Derivative(Vf(sp.Symbol('_xi_1')), sp.Symbol('_xi_1'), 2), sp.Symbol('_xi_1'), chi0): V2})
L2s = sp.expand(L2s)
# second derivative of V appears as Subs(...); map generically
V1 = sp.Symbol('Vp')
L2s = L2s.subs(sp.Derivative(Vf(chi0), (chi0, 2)), V2).subs(sp.Derivative(Vf(chi0), chi0), V1)
for e in list(L2s.atoms(sp.Subs)):
    n = e.expr.derivative_count if isinstance(e.expr, sp.Derivative) else 0
    L2s = L2s.subs(e, V2 if n == 2 else V1)
L2s = L2s.subs(sp.Symbol('chiddot'), -3*H*cd - V1)
L2s = L2s.subs({Vf(chi0): V0, g: gs, lam: ls})
L2s = sp.expand(L2s.subs(ls, 3*H**2 - cd**2/2 - V0).subs(gs, -2*Hd - cd**2))
# variables
A_, B_, Z_, D_, Zd, Dd = sp.symbols('A B Z D Zd Dd')
L2v = L2s.subs({sp.Derivative(ze, t): Zd, sp.Derivative(dc, t): Dd}).subs({al: A_, b: B_, ze: Z_, dc: D_})
L2v = sp.expand(L2v)
assert not L2v.has(sp.Derivative), L2v.atoms(sp.Derivative)
print("alpha^2 coefficient:", sp.factor(L2v.coeff(A_, 2)))
sol = sp.solve([sp.diff(L2v, A_), sp.diff(L2v, B_)], [A_, B_], dict=True)[0]
Lred = sp.simplify(sp.expand(L2v.subs(sol)))
Kmat = sp.Matrix(2, 2, lambda i, j: sp.diff(Lred, [Zd, Dd][i], [Zd, Dd][j]))
Kmat = sp.simplify(Kmat)
print("kinetic matrix (zeta, dchi):"); sp.pprint(Kmat)
print("det K =", sp.factor(Kmat.det()))
import pickle
pickle.dump({'Lred': Lred, 'Kmat': Kmat, 'sol': sol}, open(__file__.replace('.py', '.pkl'), 'wb'))
