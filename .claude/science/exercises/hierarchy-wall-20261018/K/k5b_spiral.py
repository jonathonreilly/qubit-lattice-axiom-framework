"""K5b: weak focus + random O(1) complex quadratic terms (z^2, |z|^2, zbar^2).
For each draw: passage time r0 = 0.3 -> r1 = 3 at several (Re y, Im y).
inf = never gaps within tmax (captured by a limit cycle / other attractor)."""
import numpy as np
rng = np.random.default_rng(7)
def passage(s, w, c, r0=0.3, r1=3.0, tmax=1500.0):
    lam = s + 1j * w
    f = lambda z: lam * z + c[0] * z * z + c[1] * z * np.conj(z) + c[2] * np.conj(z) ** 2
    dt = min(0.02, 0.05 / abs(w)); z, t = r0 + 0j, 0.0
    while t < tmax:
        k1 = f(z); k2 = f(z + dt/2*k1); k3 = f(z + dt/2*k2); k4 = f(z + dt*k3)
        z += dt/6*(k1 + 2*k2 + 2*k3 + k4); t += dt
        if abs(z) >= r1: return t
    return np.inf
grid = [(0.03, 3.0), (0.03, 10.0), (0.5, 10.0), (0.5, 50.0)]
print("draw | " + " | ".join(f"Re={s},Im={w}" for s, w in grid))
for d in range(6):
    c = (rng.uniform(-1, 1, 3) + 1j * rng.uniform(-1, 1, 3)) / np.sqrt(2)
    print(f"{d:4d} | " + " | ".join(f"{passage(s, w, c):10.1f}" for s, w in grid))
print("reference ln(10)/Re: Re=0.03 -> 76.8 ; Re=0.5 -> 4.6")
