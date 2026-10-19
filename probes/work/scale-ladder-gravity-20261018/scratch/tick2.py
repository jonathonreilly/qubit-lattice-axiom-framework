import numpy as np
L = 160; c = L//2
X, Y, Z = np.meshgrid(*[np.arange(L) - c]*3, indexing='ij'); R = np.sqrt(X**2 + Y**2 + Z**2)
def lap3(u): return np.roll(u,1,0)+np.roll(u,-1,0)+np.roll(u,1,1)+np.roll(u,-1,1)+np.roll(u,1,2)+np.roll(u,-1,2)-6*u
def shell_radius(u, d):
    d = np.array(d, float); d /= np.linalg.norm(d); rs = np.arange(5, c - 4, 0.5)
    vals = [abs(np.interp(0, [0], [0]))]  # placeholder
    pts = np.round(c + np.outer(rs, d)).astype(int); prof = np.abs(u[pts[:, 0], pts[:, 1], pts[:, 2]])
    return rs[int(np.argmax(prof))]
sigma = 3.0
for n in (2, 3, 4):
    u0 = np.exp(-R**2/(2*sigma**2)); u1 = u0.copy()           # smooth pulse at rest
    speeds = {}
    snaps = {}
    for t in range(1, 50*n + 1):
        u2 = 2*u1 - u0 + lap3(u1)/n**2; u0, u1 = u1, u2
        if t in (30*n, 50*n): snaps[t//n] = u1.copy()
    for nm, d in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
        speeds[nm] = (shell_radius(snaps[50], d) - shell_radius(snaps[30], d))/20
    print(f"n={n} influence sub-steps per record tick: light speed per record tick axis {speeds['axis']:.3f}, face {speeds['face']:.3f}, body {speeds['body']:.3f} (target 1)")
