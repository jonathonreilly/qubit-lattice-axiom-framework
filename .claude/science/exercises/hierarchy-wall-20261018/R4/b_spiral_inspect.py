"""Re-run b2b with the same seed; inspect every T >= L* trajectory that has no
slow point (min|beta| > 0.05): fixed points, Jacobian eigenvalues, radial rate."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
rng = np.random.default_rng(1018)
LSTAR, U_END = 38.4, 3.0
# replay the b2a RNG consumption exactly
for trial in range(40000):
    a = rng.uniform(-1, 1, 5); u0 = rng.uniform(-1, 1)
def runaway(t, z): return np.hypot(z[0], z[1]) - U_END
runaway.terminal = True
stats = {"gapped": 0, "long": 0, "long_fast": 0}
for trial in range(3000):
    A = rng.uniform(-1, 1, (2, 6))
    def f(t, z, A=A):
        x, y = z
        return A @ np.array([1.0, x, y, x*x, x*y, y*y])
    z0 = rng.uniform(-1, 1, 2)
    sol = solve_ivp(f, (0, 400), z0, events=runaway, max_step=0.05, rtol=1e-8, atol=1e-10)
    if sol.status != 1: continue
    stats["gapped"] += 1
    T = sol.t_events[0][0]
    if T < LSTAR: continue
    stats["long"] += 1
    sp = np.array([np.hypot(*f(0, sol.y[:, i])) for i in range(sol.y.shape[1])])
    if sp.min() <= 0.05: continue
    stats["long_fast"] += 1
    print(f"trial {trial}: T={T:.2f}, min speed {sp.min():.3f}")
    # fixed points from many seeds
    fps = []
    for s in rng.uniform(-4, 4, (60, 2)):
        zf, info, ier, msg = fsolve(lambda z: f(0, z), s, full_output=True)
        if ier == 1 and np.linalg.norm(f(0, zf)) < 1e-10 and not any(np.linalg.norm(zf - p) < 1e-6 for p in fps):
            fps.append(zf)
    for p in fps:
        h = 1e-6
        Jm = np.column_stack([(f(0, p + h*e) - f(0, p - h*e)) / (2*h) for e in np.eye(2)])
        ev = np.linalg.eigvals(Jm)
        print(f"   fixed point {np.round(p,4)}  eigenvalues {np.round(ev,4)}"
              + (f"  Re/|Im| = {abs(ev[0].real)/abs(ev[0].imag):.4f}" if abs(ev[0].imag) > 1e-9 else ""))
    # radial growth about the trajectory's centroid of the first half
    c = sol.y[:, : sol.y.shape[1]//2].mean(axis=1)
    r = np.hypot(sol.y[0]-c[0], sol.y[1]-c[1]); th = np.unwrap(np.arctan2(sol.y[1]-c[1], sol.y[0]-c[0]))
    n_wind = abs(th[-1]-th[0])/(2*np.pi)
    omega = abs(th[-1]-th[0])/T
    k = len(r)//10
    print(f"   windings {n_wind:.1f}, mean angular rate {omega:.3f}, r start {r[:k].mean():.3f}, "
          f"r at 90% time {r[-k:].mean():.3f}")
    # per-winding radial growth in the middle 80%
    mid = slice(k, len(r)-k)
    eps = np.polyfit(sol.t[mid], np.log(r[mid]), 1)[0]
    print(f"   effective radial rate eps_eff = {eps:.4f}; eps_eff/omega = {eps/omega:.4f}")
print(stats)
