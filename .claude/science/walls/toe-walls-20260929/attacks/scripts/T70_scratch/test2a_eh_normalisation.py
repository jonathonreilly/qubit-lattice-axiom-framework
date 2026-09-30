"""Test 2a (T70): verify the continuum Einstein-Hilbert quadratic forms used to read G off a static
vacuum-energy response.  Static metric ds^2 = -N^2 dt^2 + g_ij dx^i dx^j, all fields depend on z only.
  E_EH = -(1/(16 pi G)) * Int N sqrt(g) R^(3)   (static, total derivatives dropped)
Sectors: TT  g = diag(1+eps f, 1-eps f, 1), N=1;   conformal-lapse  g = psi^4 delta, N = 1+nu f, psi = 1+pi f.
Expected: TT:  E2/V = k^2 eps^2 /(64 pi G) ;  (n,p): E2/V = -(k^2/(4 pi G)) (pi^2 + nu pi)  (f = cos kz).
"""
import sympy as sp
z, eps, nu, pi_, k = sp.symbols('z epsilon nu pi_ k', real=True)
G = sp.symbols('G', positive=True)

def scalar_curvature(g, coords):
    n = len(coords)
    ginv = g.inv()
    Gam = [[[sum(ginv[a, d]*(sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b]) - sp.diff(g[b, c], coords[d])) for d in range(n))/2
             for c in range(n)] for b in range(n)] for a in range(n)]
    def Ric(b, c):
        return sum(sp.diff(Gam[a][b][c], coords[a]) - sp.diff(Gam[a][b][a], coords[c])
                   + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(n)) for a in range(n))
    return sum(ginv[b, c]*Ric(b, c) for b in range(n) for c in range(n))

x, y = sp.symbols('x y', real=True)
coords = [x, y, z]
f = sp.cos(k*z)

def avg(expr):  # average over one period in z
    return sp.simplify(sp.integrate(sp.expand(expr), (z, 0, 2*sp.pi/k))*k/(2*sp.pi))

# TT
g = sp.diag(1+eps*f, 1-eps*f, 1)
sqrtg = sp.sqrt((1+eps*f)*(1-eps*f))
R = scalar_curvature(g, coords)
integrand = sp.series(sqrtg*R, eps, 0, 3).removeO()
quad = sp.expand(integrand).coeff(eps, 2)
E2 = avg(-quad/(16*sp.pi*G))
print("TT: E2/V (eps^2 coefficient, average over period) =", sp.simplify(E2), "  expected k^2/(64 pi G) =", k**2/(64*sp.pi*G))

# conformal + lapse
psi = 1 + pi_*f
N = 1 + nu*f
g = sp.diag(psi**4, psi**4, psi**4)
sqrtg = psi**6
R = scalar_curvature(g, coords)
integrand = sp.expand(sp.series(N*sqrtg*R, eps, 0, 3).removeO()) if False else N*sqrtg*R
t = sp.symbols('t')
integrand = integrand.subs({nu: t*nu, pi_: t*pi_})
ser = sp.series(sp.simplify(integrand), t, 0, 3).removeO()
quad = sp.expand(ser).coeff(t, 2)
E2 = avg(-quad/(16*sp.pi*G))
print("conformal/lapse: E2/V =", sp.simplify(E2), "  expected -(k^2/(4 pi G))(pi^2+nu pi) =", sp.expand(-(k**2/(4*sp.pi*G))*(pi_**2 + nu*pi_)))
