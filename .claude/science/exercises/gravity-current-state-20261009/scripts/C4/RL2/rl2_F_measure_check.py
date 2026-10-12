"""RL2 (F): consistency check of the curved measure factor used in rl2_A: the interval volume computed from the plane-wave
measure d^4z = (2 pi/Lam) g du dsigma1 dsigma2 is V = (pi/24) tau^4 <g>_w (w = 6u(Lam-u)/Lam^3, affine u), so <g>_w must equal
nu computed independently from G-L's conformal formula nu = <Om^4>_w/<Om^2>^2 (flat parameter).  Also checks the Van Vleck
chain-rule identity g(u;Lam) Delta^{1/2}(0,u) = Delta^{1/2}(0,Lam)/Delta^{1/2}(u,Lam) used in the kappa-substitution."""
import numpy as np
from rl2_A_planewave_mean import Ray, Rr
for A, c in [(3.0, 50.0), (3.0, 25.0), (1.0, 50.0)]:
    r = Ray(A, c); uobs = r.u_of_t(Rr)
    x, w = np.polynomial.legendre.leggauss(400); u = 0.5*uobs*(x+1); wu = 0.5*uobs*w
    t = r.t_of_u(u)
    _, D0u = r.nu_Delta(np.zeros_like(t), t); _, Dux = r.nu_Delta(t, np.full_like(t, Rr))
    nuL, DL = r.nu_Delta(0.0, Rr)
    g = np.sqrt(DL/(D0u*Dux)); gw = np.sum(wu*6*u*(uobs-u)/uobs**3*g)
    print("A=%g c=%g: <g>_w (affine) = %.6f   nu (G-L conformal formula) = %.6f   rel.diff %.1e" % (A, c, gw, nuL, gw/nuL-1))
