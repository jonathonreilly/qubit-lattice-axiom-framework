"""E2: lean with spatial neighbours, away from your own previous tick:
     u(t+1) = 2 u(t) - u(t-1) + s * (sum of 6 neighbours - 6 u(t))      [s = w_space / w_time]
The stationary 4D rule with + weights to space and - weights to time; s = 1 is 'tick on the same footing'."""
import numpy as np
L = 128; c = L//2
def lap(u): return (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) + np.roll(u, 1, 2) + np.roll(u, -1, 2) - 6*u)
for s in (1/3, 0.25, 0.1, 1.0, 0.34):
    u0 = np.zeros((L, L, L)); u0[c, c, c] = 1.0; u1 = u0.copy()
    T = 50; blew = None; reach = {}
    for t in range(1, T + 1):
        u2 = 2*u1 - u0 + s*lap(u1); u0, u1 = u1, u2
        m = np.abs(u1).max()
        if m > 1e6 and blew is None: blew = t; break
    if blew:
        print(f"s={s:.3f}: UNSTABLE (amplitude > 1e6 at tick {blew})"); continue
    a = np.abs(u1); thr = 1e-6*a.max()
    for nm, d in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
        d = np.array(d); n = 0
        while np.all(c + (n+1)*d < L) and a[tuple(c + (n+1)*d)] > thr: n += 1
        reach[nm] = n*np.linalg.norm(d)
    print(f"s={s:.3f}: after {T} ticks front reach axis {reach['axis']:.1f}, face {reach['face']:.1f}, body {reach['body']:.1f}; "
          f"continuum speed sqrt(s) = {np.sqrt(s):.3f} -> {np.sqrt(s)*T:.1f}; strict cone max 1 site/tick on each axis")
