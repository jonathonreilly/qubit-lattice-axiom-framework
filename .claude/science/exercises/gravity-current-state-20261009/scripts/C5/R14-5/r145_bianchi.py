"""R14-5 Lemma C check (sympy): divergence of E^{mu nu} = rho_E n n + p_E h for a general
spherically symmetric metric with lapse N(t,r), zero shift:
   ds^2 = -N(t,r)^2 dt^2 + A(t,r)^2 dr^2 + B(t,r)^2 dOmega^2 .
Claims checked:
 C1. nabla_mu E^{mu r} = h^{rr} [ (rho_E+p_E) d_r ln N + d_r p_E ]            (Euler form)
     nabla_mu E^{mu t} = (1/N) [ (1/N) d_t rho_E + (rho_E+p_E) theta_n ]         (energy form)
     with theta_n = (1/N) d_t ln(A B^2) (expansion of the slice normals).
 C2. With rho_E = lam(t) (zero-mode lapse: E_nn uniform) the r-equation integrates to
     (lam + p_E) N = g(t); substituting p_E = g/N - lam, the r-equation vanishes identically and
     the t-equation becomes  lam' + g(t) theta_n(t,r) = 0  ->  either g=0 (lam const: unimodular)
     or theta_n uniform (CMC slicing).
 C3. Homogeneous bookkeeping (FRW, N=1, kappa=1): E_nn = 3H^2 - rho_tot =: lam,
     p_E = -(2H'+3H^2) - p_tot, g = lam + p_E = -2H' - (rho+p)_nc  (w=-1 vacuum drops out);
     and lam' = -3 H g holds identically given total conservation (any a(t)): L-hom.
 C4. Linearised N-multiplied Raychaudhuri/CMC lapse equation: the g-term (3g/2) is N-independent,
     so g drops out of the perturbation equation (only the background value Qbar = -theta' - 3g/2 changes).
"""
import sympy as sp
t, r, th, ph = sp.symbols('t r theta phi', real=True)
N = sp.Function('N')(t, r); A = sp.Function('A')(t, r); B = sp.Function('B')(t, r)
x = [t, r, th, ph]
g = sp.diag(-N**2, A**2, B**2, B**2*sp.sin(th)**2)
gi = g.inv()
def Gam(a, b, c):
    return sp.Rational(1, 2)*sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(4))
G = [[[sp.simplify(Gam(a, b, c)) for c in range(4)] for b in range(4)] for a in range(4)]
rhoE = sp.Function('rho_E')(t, r); pE = sp.Function('p_E')(t, r)
n_up = sp.Matrix([1/N, 0, 0, 0])
h_up = gi + n_up*n_up.T
E = rhoE*n_up*n_up.T + pE*h_up
def divE(nu):
    s = 0
    for mu in range(4):
        s += sp.diff(E[mu, nu], x[mu])
        for lam_ in range(4):
            s += G[mu][mu][lam_]*E[lam_, nu] + G[nu][mu][lam_]*E[mu, lam_]
    return sp.simplify(s)
dt_, dr_ = divE(0), divE(1)
theta_n = sp.diff(sp.log(A*B**2), t)/N
euler = (1/A**2)*((rhoE + pE)*sp.diff(sp.log(N), r) + sp.diff(pE, r))
energy = (1/N)*((1/N)*sp.diff(rhoE, t) + (rhoE + pE)*theta_n)
print("C1 r-component - Euler form  =", sp.simplify(dr_ - euler))
print("C1 t-component - energy form =", sp.simplify(dt_ - energy))
lam = sp.Function('lam')(t); gg = sp.Function('g')(t)
sub = {rhoE: lam, pE: gg/N - lam}
print("C2 r-component with rho_E=lam, p_E=g/N-lam :", sp.simplify(dr_.subs(sub).doit()))
t_sub = sp.simplify((dt_.subs(sub).doit())*N**2)
print("C2 N^2 * t-component =", t_sub)
print("C2 check: equals lam' + g*theta_n*N^... ->", sp.simplify(t_sub - (sp.diff(lam, t) + gg*theta_n)))
# C3 homogeneous
tt = sp.symbols('t'); a = sp.Function('a')(tt)
rn = sp.Function('rho_nc')(tt); pn = sp.Function('p_nc')(tt); rv = sp.Function('rho_v')(tt)
H = sp.diff(a, tt)/a
lamH = 3*H**2 - (rn + rv)
pEH = -(2*sp.diff(H, tt) + 3*H**2) - (pn - rv)
gH = sp.simplify(lamH + pEH)
print("C3 g =", gH, "   [expect -2H' - (rho_nc + p_nc)]:", sp.simplify(gH - (-2*sp.diff(H, tt) - rn - pn)))
# total conservation: rho_nc' + rho_v' = -3H(rho_nc + p_nc)
cons = {sp.diff(rn, tt): -3*H*(rn + pn) - sp.diff(rv, tt)}
print("C3 lam' + 3H g (should vanish for any a(t)) =", sp.simplify((sp.diff(lamH, tt) + 3*H*gH).subs(cons)))
# C4
Nn, dN, Qt, Sx, g0 = sp.symbols('N dN Qtilde S g0')
# N*R_nn contribution of E: N*(1/2)(rho_E + 3 p_E) with rho_E=lam, p_E=g0/N-lam
l0 = sp.symbols('lam0')
contrib = sp.expand(Nn*sp.Rational(1, 2)*(l0 + 3*(g0/Nn - l0)))
print("C4 N*R_nn(E) =", contrib, "-> d/dN =", sp.diff(contrib, Nn), "(g-independent)")
