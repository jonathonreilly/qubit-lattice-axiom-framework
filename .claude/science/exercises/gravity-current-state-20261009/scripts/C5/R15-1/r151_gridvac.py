"""R15-1 (d): the grid zero-point (uniform constants rho_v, p_v, any w, at rest in the site = CMC frame) in the R14-5 model.
Spherical metric ds^2 = -N(t,r)^2 dt^2 + A^2 dr^2 + B^2 dOmega^2 (as r145_bianchi.py). kappa = 1.
G is conserved identically and matter is separately conserved, so div(E + T_grid) = 0 where E := G - T_matter - T_grid.
Imposed equations (H-imp) fix E = lam(t) n n + p_E h. Claim D1: div(E + T_grid) = 0 iff
   p_E = g1(t)/N - lam - (rho_v + p_v)   and   lam' + g1 theta_n = 0,
i.e. E' := E + T_grid is a Lemma-C fluid with rho' = lam + rho_v =: Lt (uniform) and g' = g1.
Claim D2 (FRW): g1 = -2H' - (rho+p)_matter: the vacuum's (rho+p)_v does NOT enter (contrast R14-5 K5).
Claim D3 (Lemma G' branch): if instead T_grid must be conserved by itself (no momentum exchange with E), its Euler
   equation is (rho_v + p_v) d_r ln N = 0, so N(t, r) is uniform on each slice unless rho_v + p_v = 0.
"""
import sympy as sp
t, r, th, ph = sp.symbols('t r theta phi', real=True)
N = sp.Function('N')(t, r); A = sp.Function('A')(t, r); B = sp.Function('B')(t, r)
x = [t, r, th, ph]
g = sp.diag(-N**2, A**2, B**2, B**2*sp.sin(th)**2); gi = g.inv()
def Gam(a, b, c):
    return sp.Rational(1, 2)*sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(4))
G = [[[sp.simplify(Gam(a, b, c)) for c in range(4)] for b in range(4)] for a in range(4)]
n_up = sp.Matrix([1/N, 0, 0, 0]); h_up = gi + n_up*n_up.T
def div(T, nu):
    s = 0
    for mu in range(4):
        s += sp.diff(T[mu, nu], x[mu])
        for l in range(4):
            s += G[mu][mu][l]*T[l, nu] + G[nu][mu][l]*T[mu, l]
    return sp.simplify(s)
lam = sp.Function('lam')(t); g1 = sp.Function('g1')(t)
rv, pv = sp.symbols('rho_v p_v', real=True)
pE = g1/N - lam - (rv + pv)
E = lam*n_up*n_up.T + pE*h_up
Tg = rv*n_up*n_up.T + pv*h_up
tot = E + Tg
dr = div(tot, 1); dt_ = div(tot, 0)
theta_n = sp.diff(sp.log(A*B**2), t)/N
print("D1 r-component of div(E + T_grid):", sp.simplify(dr))
print("D1 N^2 * t-component - (lam' + g1 theta_n):", sp.simplify(dt_*N**2 - (sp.diff(lam, t) + g1*theta_n)))
# D3: grid vacuum alone
print("D3 r-component of div(T_grid) alone:", sp.factor(div(Tg, 1)), " (vanishes only if d_r N = 0 or rho_v + p_v = 0)")
print("D3 t-component of div(T_grid) alone * N^2:", sp.factor(sp.simplify(div(Tg, 0)*N**2)), " (energy injected by creation)")
# D2 FRW bookkeeping
tt = sp.symbols('t'); a = sp.Function('a')(tt); H = sp.diff(a, tt)/a
rm = sp.Function('rho_m')(tt); pm = sp.Function('p_m')(tt)
lamH = 3*H**2 - rm - rv                       # E_nn
pEH = -(2*sp.diff(H, tt) + 3*H**2) - pm - pv  # trace equation
g1H = sp.simplify(lamH + pEH + (rv + pv))
print("D2 g' =", g1H, " -> minus(-2H' - (rho+p)_m):", sp.simplify(g1H - (-2*sp.diff(H, tt) - rm - pm)))
cons = {sp.diff(rm, tt): -3*H*(rm + pm)}
print("D2 (lam + rho_v)' + 3H g' (should vanish for any a(t)):", sp.simplify((sp.diff(lamH + rv, tt) + 3*H*g1H).subs(cons)))
print("D2 worker's E-alone g = N(lam + p_E) = g' - (rho_v + p_v): Planckian and N-dependent off-FRW; not the observable combination.")
