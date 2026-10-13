"""R17-11 (a)/(b), nonlinear: generalized Lemma V with a space- and time-dependent vacuum (sympy).

Setting (R14-5/R15-1 E-sector, kappa = 1):
  spherical metric ds^2 = -N(t,r)^2 dt^2 + A(t,r)^2 dr^2 + B(t,r)^2 dOmega^2 (as r145_bianchi.py / r151_gridvac.py);
  n = lattice-slice normal = site frame (sites ride the normals, R14-5 site rule);
  imposed: E_ni = 0, E^TL = 0, E_nn = lam(t) (uniform), trace NOT imposed  ->  E = lam n n + pE h, pE(t,r) unknown;
  grid vacuum at rest in the site frame, NOW with arbitrary local profiles:
      T_v = V(t,r) n n + (W(t,r) - V(t,r)) h  =  -V g + W h      (V = rho_v, W = rho_v + p_v, the enthalpy);
  matter T_m with the covariant vacuum-energy exchange only:  div(T_m - V g) = 0   (standard latent heat; no W leg).
Bianchi: div(E + T_v + T_m) = 0  <=>  div(E + T_v + V g) = 0  <=>  div(E + W h) = 0.

Claims checked here:
  G1 (generalized Lemma V): r-component of div(E + W h) = d_r[N (lam + pE + W)] / (A^2 N^2)   (so N(lam+pE+W) = g'(t)),
     t-component * N^2 = lam' + g' theta_n  with g' := N(lam + pE + W), theta_n = d_t ln(A B^2)/N.
     W(t,r) and V(t,r) are ARBITRARY: the enthalpy may vary in space and time (phase transitions, bubbles, media).
  G2 (exchange current): Q_nu := div(T_v)_nu + d_nu V = div(W h)_nu equals  D_nu W + W (a_nu + theta_n n_nu)  componentwise
     (a = D ln N, n_nu = (-N,0,0,0)).  Note: no n.dW (time-derivative) term -- W carries no site-frame energy density.
  G3 (S): lam = lam0 constant  ->  lam' = 0  ->  g' theta_n = 0  ->  g' = 0 wherever theta_n != 0  ->  pE = -lam0 - W,
     and then E + T_v = -(lam0 + V) g  identically (all components), whatever W(t,r), N, A, B.
  G4 control: with W -> 0 this is R14-5 Lemma C verbatim.
"""
import sympy as sp

t, r, th, ph = sp.symbols('t r theta phi', real=True)
N = sp.Function('N')(t, r); A = sp.Function('A')(t, r); B = sp.Function('B')(t, r)
x = [t, r, th, ph]
g = sp.diag(-N**2, A**2, B**2, B**2*sp.sin(th)**2); gi = g.inv()

def Gam(a, b, c):
    return sp.Rational(1, 2)*sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(4))
G = [[[sp.simplify(Gam(a, b, c)) for c in range(4)] for b in range(4)] for a in range(4)]

def div_up(T, nu):
    """(nabla_mu T^{mu nu}) for contravariant T."""
    s = 0
    for mu in range(4):
        s += sp.diff(T[mu, nu], x[mu])
        for l in range(4):
            s += G[mu][mu][l]*T[l, nu] + G[nu][mu][l]*T[mu, l]
    return sp.simplify(s)

n_up = sp.Matrix([1/N, 0, 0, 0]); h_up = gi + n_up*n_up.T
lam = sp.Function('lam')(t); pE = sp.Function('p_E')(t, r)
W = sp.Function('W')(t, r); V = sp.Function('V')(t, r)
theta_n = sp.diff(sp.log(A*B**2), t)/N

E = lam*n_up*n_up.T + pE*h_up
Wh = W*h_up
tot = E + Wh

# G1 ------------------------------------------------------------
gp = N*(lam + pE + W)
r_comp = div_up(tot, 1)
t_comp = div_up(tot, 0)
res_r = sp.simplify(r_comp - sp.diff(gp, r)/(A**2*N))
res_t = sp.simplify(t_comp*N**2 - (sp.diff(lam, t) + gp*theta_n))
print("G1 r-component of div(E + W h) - d_r[N(lam+pE+W)]/(A^2 N):", res_r)
print("G1 N^2 t-component - (lam' + g' theta_n), g' = N(lam+pE+W):", res_t)

# G2 ------------------------------------------------------------
Tv = V*n_up*n_up.T + (W - V)*h_up
# covariant components: lower nu with g; div_up returns upper-index divergence; compare upper-index forms
# claimed: Q^nu = h^{nu mu} d_mu W + W (a^nu + theta_n n^nu), a^nu = h^{nu mu} d_mu ln N
dV_up = [sum(gi[nu, mu]*sp.diff(V, x[mu]) for mu in range(4)) for nu in range(4)]
Q_up = [sp.simplify(div_up(Tv, nu) + dV_up[nu]) for nu in range(4)]
claim = [sp.simplify(sum(h_up[nu, mu]*sp.diff(W, x[mu]) for mu in range(4))
                     + W*(sum(h_up[nu, mu]*sp.diff(sp.log(N), x[mu]) for mu in range(4)) + theta_n*n_up[nu]))
         for nu in range(4)]
print("G2 Q^nu - [D^nu W + W(a^nu + theta_n n^nu)] for nu = t, r, theta, phi:",
      [sp.simplify(Q_up[nu] - claim[nu]) for nu in range(4)])
print("G2 energy leg  -n_nu Q^nu = N*Q^t:", sp.simplify(N*Q_up[0]), "  (= W theta_n: creation at fixed density pays W per unit new volume)")
print("G2 momentum leg Q^r:", sp.simplify(Q_up[1]), "  (= [d_r W + W d_r ln N]/A^2: gradient + holding the hovering vacuum up)")

# G3 ------------------------------------------------------------
lam0 = sp.symbols('lambda_0', real=True)
pE_S = -lam0 - W
E_S = lam0*n_up*n_up.T + pE_S*h_up
lhs = E_S + Tv
rhs = -(lam0 + V)*gi
print("G3 (S): E + T_v + (lam0 + V) g^{-1} (all 16 components) =", sp.simplify(lhs - rhs) == sp.zeros(4, 4))
print("G3 (S): g' = N(lam0 + pE + W) with pE = -lam0 - W:", sp.simplify(N*(lam0 + pE_S + W)))
print("G3 (S): div(E_S + W h) components:", [sp.simplify(sp.expand_trig(div_up(E_S + Wh, nu)).rewrite(sp.cos)) for nu in range(4)])

# G4 control ----------------------------------------------------
print("G4 control (W = 0, R14-5 Lemma C): r-comp - d_r[N(lam+pE)]/(A^2 N) =",
      sp.simplify(div_up(E, 1) - sp.diff(N*(lam + pE), r)/(A**2*N)))
