"""T62 test G: is Lambda = 3/R^2 = lambda_1(S^3_R) a statement about the world or about a slice?
Exact (sympy) + arithmetic.  c = 1 units unless stated.  Pre-registered in PREREGISTRATION.md."""
import sympy as sp
import numpy as np

t, chi, th, ph = sp.symbols('t chi theta phi', real=True)
R, rho = sp.symbols('R rho', positive=True)

def ricci(g, X):
    n = len(X)
    ginv = g.inv()
    Gam = [[[sum(ginv[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for d in range(n):
                    s += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
            Ric[b, c] = sp.simplify(s)
    return Ric

X = [t, chi, th, ph]

# G1: closed de Sitter, a(t) = R cosh(t/R)
a = R*sp.cosh(t/R)
g = sp.diag(-1, a**2, a**2*sp.sin(chi)**2, a**2*sp.sin(chi)**2*sp.sin(th)**2)
Ric = ricci(g, X)
lam = sp.symbols('Lambda', positive=True)
resid = sp.simplify(Ric - (3/R**2)*g)
print("G1 closed dS: Ricci - (3/R^2) g =", resid.tolist() == sp.zeros(4, 4).tolist(), "-> Lambda_dS = 3/R^2")
H = sp.simplify(sp.diff(a, t)/a)
lam1_slice = 3/a**2
print("   H(t) =", H, "; lambda_1(slice) = 3/a(t)^2 =", sp.simplify(lam1_slice))
eq = sp.simplify(lam1_slice - 3/R**2)
print("   lambda_1(slice) - Lambda_dS =", eq, " (zero only at t=0)")
print("   solve lambda_1(slice)=Lambda for t:", sp.solve(sp.Eq(sp.cosh(t/R)**2, 1), t), "; H there =", sp.simplify(H.subs(t, 0)))

# G2: product R x S^3_rho, constant radius
g2 = sp.diag(-1, rho**2, rho**2*sp.sin(chi)**2, rho**2*sp.sin(chi)**2*sp.sin(th)**2)
Ric2 = ricci(g2, X)
print("G2 R x S^3_rho: Ricci_00 =", Ric2[0, 0], "; Ricci_11/g_11 =", sp.simplify(Ric2[1, 1]/g2[1, 1]))
print("   R_mu nu = Lambda g_mu nu needs R_00 = -Lambda (g_00 = -1) and R_ij = Lambda g_ij.")
print("   Here R_00 = 0 forces Lambda = 0, while R_ij = (2/rho^2) g_ij forces Lambda = 2/rho^2 > 0: no vacuum solution for any rho (constant-radius S^3 needs matter: the Einstein static universe).")

# G3: closed FRW with dust + radiation + Lambda: H^2 = 8piG rho/3 + Lambda/3 - 1/a^2   (c = 1)
# lambda_1(S^3_a) = 3/a^2 = Lambda  <=>  H^2 = 8 pi G rho / 3 <=> Omega_m + Omega_r = 1 (Omega_k = -Lambda/(3H^2) = -Omega_Lambda)
Om, OL, Orad = 0.315, 0.685, 9.2e-5
print("\nG3 closed FRW today (Planck-like Om=0.315, OL=0.685):")
print("   lane: curvature radius today = R_Lambda => Omega_k = -Omega_Lambda = %.3f; then Omega_m = 1-OL-Ok = %.3f (vs 0.315)" % (-OL, 1 - OL + OL))
for Ok in (0.002, 0.005, 0.01):
    Rc = 1/np.sqrt(Ok)         # in c/H0
    RL = 1/np.sqrt(OL)         # R_Lambda in c/H0
    print("   |Omega_k|<=%.3f -> R_curv >= %.1f c/H0 = %.1f R_Lambda" % (Ok, Rc, Rc/RL))
# with the observed matter content, the slice where lambda_1 = Lambda (a=R_Lambda) is a slice with H^2 = 8piG rho/3:
# closed dS + dust has no turnaround at a = R_Lambda unless rho_m = H^2*3/(8 pi G)
print("   => 'Lambda = lambda_1(S^3)' on today's slice needs Omega_m+Omega_r = 1 (an Einstein-de Sitter-like closure), inconsistent with the flat bridge Omega_m = 1 - Omega_Lambda.")
