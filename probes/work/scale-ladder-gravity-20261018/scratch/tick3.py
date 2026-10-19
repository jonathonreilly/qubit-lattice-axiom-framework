"""T3: probabilistic time. Each influence sub-step, each site updates only with probability rho (its own random clock);
a site that updates does u <- 2u - u_prev + s*lap(u), u_prev <- old u; a site that waits keeps both. s = 1/4 per sub-step."""
import numpy as np
rng = np.random.default_rng(3)
L = 128; c = L//2
X, Y, Z = np.meshgrid(*[np.arange(L) - c]*3, indexing='ij'); R = np.sqrt(X**2 + Y**2 + Z**2)
def lap3(u): return np.roll(u,1,0)+np.roll(u,-1,0)+np.roll(u,1,1)+np.roll(u,-1,1)+np.roll(u,1,2)+np.roll(u,-1,2)-6*u
def shell_radius(u, d):
    d = np.array(d, float); d /= np.linalg.norm(d); rs = np.arange(5, c - 4, 0.5)
    pts = np.round(c + np.outer(rs, d)).astype(int); prof = np.abs(u[pts[:, 0], pts[:, 1], pts[:, 2]]); return rs[int(np.argmax(prof))]
s = 0.25
for rho in (1.0, 0.7, 0.4):
    u = np.exp(-R**2/18.0); up = u.copy(); snaps = {}; ok = True
    T = int(round(110/max(rho, 0.4)))
    for t in range(1, T + 1):
        m = rng.random(u.shape) < rho
        new = 2*u - up + s*lap3(u)
        up = np.where(m, u, up); u = np.where(m, new, u)
        if np.abs(u).max() > 1e6: ok = False; break
        if t in (int(T*0.45), T): snaps[t] = u.copy()
    if not ok: print(f"rho={rho}: UNSTABLE at step {t}"); continue
    t1, t2 = sorted(snaps); sp = {nm: (shell_radius(snaps[t2], d) - shell_radius(snaps[t1], d))/(t2 - t1) for nm, d in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items()}
    amp = np.abs(snaps[t2]).max()
    print(f"rho={rho}: speed per sub-step axis {sp['axis']:.3f}, face {sp['face']:.3f}, body {sp['body']:.3f} (synchronous sqrt(s) = 0.5; expect ~rho*0.5 = {0.5*rho:.3f}); peak amplitude {amp:.2e}")
