"""C5 R17-2: real-space form of R16-12's forced boost kernel X_T = -(q.Delta_b)/(|q|^2 (q.v)) (PV), d = 3.
Claim (analytic): FT^-1[PV 1/(q.v)] is a signed line distribution along v; convolved with the dipole-Coulomb factor
(q.Delta)/|q|^2 = FT[-i Delta.grad (1/(4 pi r))] it gives X(x) proportional to Delta.grad G(x)/|v|, with
G(x) = int ds sgn(s) / (4 pi |x - s vhat|) = asinh(x_par/rho)/(2 pi)  (rho = distance from the world-line).
So |X| ~ 1/r times an angular factor ~ cot(theta) near the line: homogeneous of degree -1 in x (= degree -2 in q),
unbounded angular factor -- the R16-12 referee's correction. Check G numerically (truncated line, L -> large)."""
import numpy as np
out = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
def G_num(z, rho, L=1e7, n=400001):
    # integrate sgn(s)/sqrt(rho^2+(z-s)^2) on [-L, L] with substitution s = z + rho*sinh(u) (exact measure)
    u_hi = np.arcsinh((L - z) / rho); u_lo = np.arcsinh((-L - z) / rho); u0 = np.arcsinh(-z / rho)
    # integral of du over u in (u0, u_hi) minus over (u_lo, u0)
    return ((u_hi - u0) - (u0 - u_lo)) / (4 * np.pi)
pr("z, rho, numeric G, asinh(z/rho)/(2 pi), rel diff  (L = 1e7)")
for z, rho in [(0.0, 1.0), (1.0, 1.0), (10.0, 1.0), (-3.0, 0.1), (100.0, 0.01), (5.0, 20.0)]:
    g = G_num(z, rho); a = np.arcsinh(z / rho) / (2 * np.pi)
    pr(f"  {z:7.2f} {rho:6.2f}  {g:+.10f}  {a:+.10f}  {abs(g-a)/max(abs(a),1e-12):.1e}")
pr("gradient magnitude r*|grad G| along rays at angle theta from the world-line (r = 100): grows like cot(theta)")
for th in (1.0, 0.3, 0.1, 0.03, 0.01):
    r = 100.0; z = r * np.cos(th); rho = r * np.sin(th)
    dz = 1 / np.sqrt(rho ** 2 + z ** 2) / (2 * np.pi); drho = -z / (rho * np.sqrt(rho ** 2 + z ** 2)) / (2 * np.pi)
    pr(f"  theta = {th:5.2f}: r|grad G| = {r*np.hypot(dz, drho):.4e}; cot(theta)/(2 pi) = {1/np.tan(th)/(2*np.pi):.4e}")
import os
with open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w") as f:
    f.write("\n".join(out) + "\n")
