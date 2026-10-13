"""R18-6, arena C-box-E (Z^3 x R with site creation, R14-5 E-sector), the combined bridge (S) + (d-i) + N.

kappa = 1 (G = 1/(8 pi) where a Newtonian U is needed).
E := G - kappa T_tot, T_tot = T_m + T_v, T_v = -V g + W h (site-frame vacuum; W = rho_v + p_v).
H-imp: E_ni = 0, E^TL = 0, E_nn = lam (uniform); spatial trace NOT imposed.
(S): lam = -kappa e0 (law constant).  (d-i): Q = div(W h) received by E.  H-m: div(T_m - V g) = 0.

Sections
 B1  Lemma C beyond spherical symmetry: div(lam n n + P h) for a non-symmetric metric (zero shift, diagonal h_ij
     depending on all four coordinates).  Claimed: spatial part = h^{ij} d_j[N (lam+P)]/N,  time part ~ lam' + N(lam+P) theta_n.
 B2  Static star with ARBITRARY W(r), V(r): E-sector + (S) + g=0 gives exactly TOV for (rho_m+V-e0, p_m-V+e0); W absent.
 B3  Exterior + isotropic coordinates: PPN beta = gamma = 1 at O(U^2) (Schwarzschild), and Lambda-tilde = V_out - e0.
 B4  Literal N ("total stress" incl. the vacuum's W h, all ten equations imposed): Bianchi needs Q = 0, i.e.
     W' + W Phi' = 0 in a static well and W theta = 0 in expansion  ->  W = 0 (pairing) for a fixed-proper-spacing vacuum.
 B5  g(t) is slice-global: a static region on an expanding slice inherits g = 0 (from N(lam+P) = g(t)).
 B6  If a whole slice were static (g0 != 0 allowed): extra pressure g0/N in the exterior; size of its O(U) piece.
"""
import sympy as sp

print("=== B1: Lemma C without spherical symmetry (zero shift, diagonal spatial metric, all functions of t,x,y,z) ===")
t, X, Y, Z = sp.symbols('t x y z', real=True)
xs = [t, X, Y, Z]
N = sp.Function('N')(t, X, Y, Z)
a1 = sp.Function('a1')(t, X, Y, Z); a2 = sp.Function('a2')(t, X, Y, Z); a3 = sp.Function('a3')(t, X, Y, Z)
g = sp.diag(-N**2, a1**2, a2**2, a3**2); gi = sp.diag(-1/N**2, 1/a1**2, 1/a2**2, 1/a3**2)
def Gam(a, b, c):
    return sp.Rational(1, 2)*sum(gi[a, d]*(sp.diff(g[d, b], xs[c]) + sp.diff(g[d, c], xs[b]) - sp.diff(g[b, c], xs[d])) for d in range(4))
GG = [[[Gam(a, b, c) for c in range(4)] for b in range(4)] for a in range(4)]
def div_up(T, nu):
    s = 0
    for mu in range(4):
        s += sp.diff(T[mu, nu], xs[mu])
        for l in range(4):
            s += GG[mu][mu][l]*T[l, nu] + GG[nu][mu][l]*T[mu, l]
    return s
lam = sp.Function('lam')(t); P = sp.Function('P')(t, X, Y, Z)
n_up = sp.Matrix([1/N, 0, 0, 0]); h_up = gi + n_up*n_up.T
Tf = lam*n_up*n_up.T + P*h_up
theta_n = sp.diff(sp.log(a1*a2*a3), t)/N
gp = N*(lam + P)
res_t = sp.simplify(div_up(Tf, 0)*N**2 - (sp.diff(lam, t) + gp*theta_n))
res_sp = [sp.simplify(div_up(Tf, i) - gi[i, i]*sp.diff(gp, xs[i])/N) for i in (1, 2, 3)]
print("B1 time:  N^2 div^t - (lam' + g theta_n), g := N(lam+P):", res_t)
print("B1 space: div^i - h^{ii} d_i[N(lam+P)]/N  (i = x,y,z):", res_sp)
print("   => D_i[N(lam+P)] = 0 so N(lam+P) = g(t) (slice-global); lam' = -g theta_n pointwise.")

print("\n=== B2: static star, arbitrary W(r), V(r), matter (rho_m, p_m) at rest; (S) + g = 0 ===")
r, th, ph = sp.symbols('r theta phi', positive=True)
xr = [t, r, th, ph]
Phi = sp.Function('Phi')(r); Lam = sp.Function('Lam')(r)
gs = sp.diag(-sp.exp(2*Phi), sp.exp(2*Lam), r**2, r**2*sp.sin(th)**2); gsi = gs.inv()
def Gam_s(a, b, c):
    return sp.Rational(1, 2)*sum(gsi[a, d]*(sp.diff(gs[d, b], xr[c]) + sp.diff(gs[d, c], xr[b]) - sp.diff(gs[b, c], xr[d])) for d in range(4))
Gs = [[[sp.simplify(Gam_s(a, b, c)) for c in range(4)] for b in range(4)] for a in range(4)]
def Ric(b, c):
    s = 0
    for a in range(4):
        s += sp.diff(Gs[a][b][c], xr[a]) - sp.diff(Gs[a][b][a], xr[c])
        for d in range(4):
            s += Gs[a][a][d]*Gs[d][b][c] - Gs[a][c][d]*Gs[d][b][a]
    return sp.simplify(s)
Rl = sp.Matrix(4, 4, lambda b, c: Ric(b, c))
Rs = sp.simplify(sum(gsi[a, b]*Rl[a, b] for a in range(4) for b in range(4)))
Gl = sp.simplify(Rl - Rs*gs/2)
Gmix = sp.simplify(gsi*Gl)          # G^mu_nu
rho_m = sp.Function('rho_m')(r); p_m = sp.Function('p_m')(r)
V = sp.Function('V')(r); W = sp.Function('W')(r)
e0 = sp.symbols('e_0', real=True); kap = 1
lam0 = -kap*e0
# mixed components of T_m, T_v (diag): T^t_t = -rho, T^i_i = p
Tm = sp.diag(-rho_m, p_m, p_m, p_m)
Tv = sp.diag(-V, W - V, W - V, W - V)     # -V delta + W h
# E-sector with g = 0: E = lam0 n n + pE h, pE = -lam0 - kap W  ->  E^t_t = -lam0, E^i_i = pE
pE = -lam0 - kap*W
Emix = sp.diag(-lam0, pE, pE, pE)
# field equations: G^mu_nu = kap T^mu_nu + E^mu_nu
FE = sp.simplify(Gmix - kap*(Tm + Tv) - Emix)
eff = sp.simplify(Gmix - kap*(Tm - (V - e0)*sp.eye(4)))
print("B2 [G - kappa(T_m+T_v) - E] - [G - kappa(T_m - (V-e0) g)] (mixed comps), should be 0:", sp.simplify(FE - eff) == sp.zeros(4, 4))
print("B2 W appears in the reduced equations:", any(eq.has(W) for eq in eff))
# matter conservation with H-m: div(T_m - V g) = 0  (static: r-component)
cons = sp.simplify(sp.diff(p_m, r) + (rho_m + p_m)*sp.diff(Phi, r) - sp.diff(V, r))
rho_eff = rho_m + V - e0; p_eff = p_m - V + e0
tov_eff = sp.simplify(sp.diff(p_eff, r) + (rho_eff + p_eff)*sp.diff(Phi, r))
print("B2 H-m static Euler  minus  effective-fluid TOV Euler:", sp.simplify(cons - tov_eff))
# Contracted Bianchi of the reduced system: div of G is identically zero; check r-component of div(T_eff) on shell
print("B2 => exact GR (TOV) with rho_eff = rho_m + V - e0, p_eff = p_m - V + e0; the enthalpy W never enters (proved, all orders).")

print("\n=== B3: exterior, isotropic coordinates, PPN beta and gamma (Lambda-tilde = V_out - e0 = 0 under P93) ===")
M, R = sp.symbols('M R', positive=True)   # isotropic radius R
# Schwarzschild in isotropic coordinates (G=c=1): exterior solution of the reduced equations when V_out = e0
A00 = -((1 - M/(2*R))/(1 + M/(2*R)))**2
Aij = (1 + M/(2*R))**4
U = M/R
ser00 = sp.series(A00, M, 0, 3).removeO()
serij = sp.series(Aij, M, 0, 2).removeO()
beta = sp.simplify(-(ser00 - (-1 + 2*U)).coeff(M, 2)*R**2/2)
gamma = sp.simplify((serij - 1).coeff(M, 1)*R/2)
print("B3 g00 to O(M^2):", sp.expand(ser00), " -> beta =", beta)
print("B3 gij to O(M):  ", sp.expand(serij), " -> gamma =", gamma)
# verify the isotropic Schwarzschild metric solves the reduced vacuum equations (V_out = e0, rho_m = p_m = 0)
Rv = sp.symbols('R_v', positive=True)
Phi_iso = sp.log((1 - M/(2*Rv))/(1 + M/(2*Rv)))
psi4 = (1 + M/(2*Rv))**4
# areal radius r = R psi^2; check G^mu_nu = 0 by direct computation in isotropic coords
xi = [t, Rv, th, ph]
gI = sp.diag(-sp.exp(2*Phi_iso), psi4, psi4*Rv**2, psi4*Rv**2*sp.sin(th)**2); gIi = gI.inv()
def GamI(a, b, c):
    return sp.Rational(1, 2)*sum(gIi[a, d]*(sp.diff(gI[d, b], xi[c]) + sp.diff(gI[d, c], xi[b]) - sp.diff(gI[b, c], xi[d])) for d in range(4))
GI = [[[sp.simplify(GamI(a, b, c)) for c in range(4)] for b in range(4)] for a in range(4)]
def RicI(b, c):
    s = 0
    for a in range(4):
        s += sp.diff(GI[a][b][c], xi[a]) - sp.diff(GI[a][b][a], xi[c])
        for d in range(4):
            s += GI[a][a][d]*GI[d][b][c] - GI[a][c][d]*GI[d][b][a]
    return sp.simplify(s)
RI = sp.Matrix(4, 4, lambda b, c: RicI(b, c))
print("B3 isotropic Schwarzschild Ricci = 0 (so it solves the reduced exterior equations with V_out = e0):", sp.simplify(RI) == sp.zeros(4, 4))

print("\n=== B4: literal N (all ten equations with T_m + T_v; the vacuum's W h gravitates) ===")
# static: div(T_m + T_v) = div(T_m - V g) + div(W h) ; with H-m the first vanishes, so Bianchi needs div(W h) = 0
Wh = sp.diag(0, W, W, W)
divWh_r = sp.simplify(sp.diff(W, r) + W*sp.diff(Phi, r))   # r-comp of div(W h) for static metric (from R17-11 G2: Q^r A^2 = W' + W N'/N)
print("B4 static Q_r = W' + W Phi' (R17-11 G2 at static N = e^Phi). Literal N needs Q_r = 0  =>  W e^Phi = const (Tolman-like).")
W0, Phi0 = sp.symbols('W_0 Phi_0', real=True)
print("B4 fixed proper spacing => local vacuum the same in proper units => W = W0 const => Q_r = W0 Phi'  != 0 in any well unless W0 = 0")
print("B4 expansion: energy leg -n.Q = W theta_n (R17-11 G2)  != 0 unless W = 0.  So literal N  AND  (d-i) with W != 0 cannot hold;")
print("   the joint bridge must read N on the gravitating stress T_m - (V - e0) g (N_red). [proved, elementary]")

print("\n=== B5/B6: inheritance of g = 0, and the size of the static-slice alternative ===")
print("B5 From B1: N(lam+P) = g(t) on each slice; (S) lam' = 0 => g(t) theta_n(x) = 0 for all x; theta_n != 0 somewhere => g(t) = 0 on the whole slice,")
print("   including static (theta_n = 0) regions on that slice. [proved]")
# B6: if g0 != 0 (whole slice static): pE = g0/N - lam0 - W => extra mixed pressure g0 e^{-Phi} ~ g0 (1 - U)
g0 = sp.symbols('g_0', real=True)
H0 = 2.27e-18; c = 2.998e8; AU = 1.496e11
for frac in (0.05, 1.0):
    gg = frac*H0**2
    print(f"B6 |g0| = {frac} H0^2: (g0/c^2) r^2 at 1 AU = {gg*AU**2/c**2:.2e} (relative metric term; beta-type piece ~ that x U ~ {gg*AU**2/c**2*1e-8:.1e})")
