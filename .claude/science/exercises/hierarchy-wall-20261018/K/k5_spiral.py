"""K5: passage time of a weak focus with O(1) quadratic terms, fixed-step RK4,
no trajectory storage.  dz/dt = (s + i w) z + b (0.7 z^2 + 0.4i |z|^2 - 0.5 zbar^2).
T = RG time from r0 = 0.3 to r1 = 3 (gap); compare with ln(10)/s."""
import numpy as np
def f(z, lam, b):
    return lam * z + b * (0.7 * z * z + 0.4j * z * np.conj(z) - 0.5 * np.conj(z) ** 2)
def passage(s, w, b=1.0, r0=0.3, r1=3.0, tmax=3000.0):
    lam = s + 1j * w
    dt = min(0.02, 0.05 / max(abs(w), 1e-9))
    z, t = r0 + 0j, 0.0
    while t < tmax:
        k1 = f(z, lam, b); k2 = f(z + dt/2*k1, lam, b); k3 = f(z + dt/2*k2, lam, b); k4 = f(z + dt*k3, lam, b)
        z += dt/6*(k1 + 2*k2 + 2*k3 + k4); t += dt
        if abs(z) >= r1: return t
        if not np.isfinite(z): return np.nan
    return np.inf
print("Re y    Im y    Re/|Im|   T(0.3->3)   ln(10)/Re y")
for s, w in [(0.03, 0.3), (0.03, 3.0), (0.03, 10.0), (0.03, 30.0),
             (0.06, 10.0), (0.01, 10.0), (0.5, 10.0), (0.5, 30.0), (1.0, 30.0)]:
    T = passage(s, w)
    print(f"{s:<7}{w:<8}{s/w:<10.4g}{T:<12.2f}{np.log(10)/s:.1f}")
