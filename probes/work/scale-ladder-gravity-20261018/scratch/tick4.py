"""T3b: coherent random time: all sites tick together, but each tick has a random length dt_n (variable-step leapfrog)
   u_{n+1} = u_n + (dt_n/dt_{n-1}) (u_n - u_{n-1}) + dt_n (dt_n + dt_{n-1})/2 * lap u_n.
Measure speed per unit elapsed time and roundness."""
import numpy as np
rng = np.random.default_rng(5)
L = 128; c = L//2
X, Y, Z = np.meshgrid(*[np.arange(L) - c]*3, indexing='ij'); R = np.sqrt(X**2 + Y**2 + Z**2)
def lap3(u): return np.roll(u,1,0)+np.roll(u,-1,0)+np.roll(u,1,1)+np.roll(u,-1,1)+np.roll(u,1,2)+np.roll(u,-1,2)-6*u
def shell_radius(u, d):
    d = np.array(d, float); d /= np.linalg.norm(d); rs = np.arange(5, c - 4, 0.5)
    pts = np.round(c + np.outer(rs, d)).astype(int); prof = np.abs(u[pts[:, 0], pts[:, 1], pts[:, 2]]); return rs[int(np.argmax(prof))]
for lo, hi in ((0.5, 0.5), (0.2, 0.55), (0.05, 0.57)):
    u = np.exp(-R**2/18.0); up = u.copy(); dtp = (lo + hi)/2; T = 0.0; snaps = {}; ok = True
    while T < 52:
        dt = rng.uniform(lo, hi)
        un = u + (dt/dtp)*(u - up) + dt*(dt + dtp)/2*lap3(u); up, u, dtp = u, un, dt; T += dt
        if np.abs(u).max() > 1e6: ok = False; break
        for mark in (25, 50):
            if mark not in snaps and T >= mark: snaps[mark] = (T, u.copy())
    if not ok: print(f"dt in [{lo},{hi}]: UNSTABLE"); continue
    (t1, a1), (t2, a2) = snaps[25], snaps[50]
    sp = {nm: (shell_radius(a2, d) - shell_radius(a1, d))/(t2 - t1) for nm, d in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items()}
    print(f"tick lengths random in [{lo}, {hi}]: speed per unit time axis {sp['axis']:.3f}, face {sp['face']:.3f}, body {sp['body']:.3f} (continuum 1); amplitude {np.abs(a2).max():.2e}")
