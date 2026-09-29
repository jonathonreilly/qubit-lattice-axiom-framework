"""Kill-round check for F7: what 'a GR lapse' is in the broken-branch coordinates.

Schwarzschild in isotropic coordinates: g_00 = -((1-M/2r)/(1+M/2r))^2, g_ij = (1+M/2r)^4 delta_ij.
Agent 4's static profile h_ij = Phi (delta + xhat xhat) equals the isotropic 2 Phi delta in
coordinates r' = r_iso + (M/2) (gauge xi = -(M/2) xhat at linear order; checked below).
Question: what is GR's own g_00 in those coordinates to O(M^2)?  PPN reads beta from
g_00 = -1 + 2Phi - 2 beta Phi^2 in *isotropic* coordinates.  A lapse with a Phi^2 coefficient
of -2 (beta_coord = 1) in the r' coordinates is NOT GR's lapse there.
"""
import sympy as sp

M, r, lam = sp.symbols('M r lambda', positive=True)
# isotropic radius r_iso in terms of r' = r_iso + lam*M
rp = sp.symbols('rp', positive=True)
r_iso = rp - lam * M
g00_iso = -((1 - M / (2 * r_iso)) / (1 + M / (2 * r_iso))) ** 2
Phi_p = M / rp
series = sp.series(g00_iso.subs(rp, M / Phi_p), M, 0, 3).removeO()
series = sp.simplify(sp.expand(series))
# express in Phi' = M/r' ; series in M at fixed rp is a series in Phi'
Phi = sp.symbols('Phi')
expr = sp.expand(series.subs(M, Phi * rp))
print("GR's g_00 in coordinates r' = r_iso + lambda*M, as a series in Phi' = M/r':")
print("   ", sp.collect(expr, Phi))
beta_coord = sp.simplify(-expr.coeff(Phi, 2) / 2)
print("   coefficient read as -2*beta_coord*Phi'^2  ->  beta_coord =", beta_coord)
print("   lambda = 1/2 (agent 4's profile):", beta_coord.subs(lam, sp.Rational(1, 2)))
print("   lambda = 1   (Schwarzschild r):   ", beta_coord.subs(lam, 1))

# Linear-order gauge check: 2 Phi delta_ij + d_i xi_j + d_j xi_i with xi = c*M*xhat
x, y, z = sp.symbols('x y z', real=True)
X = sp.Matrix([x, y, z]); R = sp.sqrt(x**2 + y**2 + z**2)
c = sp.symbols('c')
xi = c * M * X / R
h_iso = 2 * (M / R) * sp.eye(3)
dxi = sp.Matrix(3, 3, lambda i, j: sp.diff(xi[j], X[i]) + sp.diff(xi[i], X[j]))
target = (M / R) * (sp.eye(3) + X * X.T / R**2)
sol = sp.solve(sp.simplify((h_iso + dxi - target)[0, 0]), c)
print("gauge parameter c with 2Phi delta + 2 d(i xi j) = Phi(delta + xhat xhat):", sol)
print("full-matrix residual at c:", sp.simplify((h_iso + dxi - target).subs(c, sol[0])))

# PPN perihelion factor for agent 4's mixed-gauge number and for GR's own lapse in the same coordinates
for gam, bet, label in [(1, sp.Rational(3, 2), "gamma=1, beta_eff=3/2 (agent 4: isotropic-gauge lapse pasted into lambda=1/2 coordinates)"),
                        (1, 1, "gamma=1, beta=1 (GR's own lapse in the same coordinates, transformed back)")]:
    print(f"(2+2gamma-beta)/3 = {sp.nsimplify((2 + 2*gam - bet)/3)} = {float((2 + 2*gam - bet)/3):.4f}   <- {label}")
