"""T1/T2: how many influence sub-steps per record tick does a full-speed (c = 1 site per record tick) light cone need?
 (a) n synchronous 3D sub-steps per tick, each u+ = 2u - u- + (1/n^2) lap3 u          (CFL: needs n >= sqrt3)
 (b) 3 directional sub-steps per tick (x, then y, then z), each a 1D leapfrog at full speed: split-step wave rule.
     Implemented as the symmetric splitting of the second-order system (u, v = du/dt)."""
import numpy as np
L = 128; c = L//2
def lap3(u): return np.roll(u,1,0)+np.roll(u,-1,0)+np.roll(u,1,1)+np.roll(u,-1,1)+np.roll(u,1,2)+np.roll(u,-1,2)-6*u
def lap1(u, ax): return np.roll(u,1,ax)+np.roll(u,-1,ax)-2*u
def reach(u):
    a = np.abs(u); thr = 1e-3*a.max(); out = {}
    for nm, d in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
        d = np.array(d); n = 0
        while np.all(c + (n+1)*d < L) and a[tuple(c + (n+1)*d)] > thr: n += 1
        out[nm] = n*np.linalg.norm(d)
    return out
def peak_radius(u, d):
    d = np.array(d, float); n = int(L/2/np.linalg.norm(d)) - 1
    prof = [abs(u[tuple(c + (k*d).astype(int))]) for k in range(1, n)]
    return (1 + int(np.argmax(prof)))*np.linalg.norm(d)
T = 40
for n in (1, 2, 3):
    u0 = np.zeros((L, L, L)); u0[c, c, c] = 1.0; u1 = u0.copy(); ok = True
    for t in range(T*n):
        u2 = 2*u1 - u0 + lap3(u1)/n**2; u0, u1 = u1, u2
        if np.abs(u1).max() > 1e8: ok = False; break
    if not ok: print(f"(a) n={n} synchronous sub-steps: UNSTABLE"); continue
    print(f"(a) n={n} synchronous sub-steps per tick: wave peak after {T} ticks axis {peak_radius(u1,(1,0,0)):.1f}, face {peak_radius(u1,(1,1,0)):.1f}, body {peak_radius(u1,(1,1,1)):.1f} (light at c=1: {T})")
# (b) directional splitting: first-order form v_t = lap u, u_t = v ; per tick: for ax in x,y,z: Stoermer-Verlet in 1D at dt = 1
u = np.zeros((L, L, L)); u[c, c, c] = 1.0; v = np.zeros_like(u); ok = True
for t in range(T):
    for ax in (0, 1, 2):
        v = v + 0.5*lap1(u, ax); u = u + v; v = v + 0.5*lap1(u, ax)
    for ax in (2, 1, 0):
        pass
    if np.abs(u).max() > 1e8: ok = False; break
print("(b) three directional sub-steps per tick (x, y, z each at full speed):", "UNSTABLE" if not ok else
      f"peak after {T} ticks axis {peak_radius(u,(1,0,0)):.1f}, face {peak_radius(u,(1,1,0)):.1f}, body {peak_radius(u,(1,1,1)):.1f}")
