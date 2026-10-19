"""T5: light delay through a record 'pace well' Phi(x) < 0 in the lean-away wave rule  m(x) u_tt = d/dx( k(x) du/dx ).
 lapse-only (time runs slower, space untouched):   m = 1/N, k = N            (N = 1 + Phi)
 full GR (gamma = 1, space stretched too):         m = a^3/N, k = N a        (a = 1 - Phi)   [isotropic weak field]
Compare pulse arrival delays to the flat case: GR should be twice lapse-only (Shapiro)."""
import numpy as np
L = 4000; x = np.arange(L) - L/2
Phi = -0.02*np.exp(-x**2/(2*150.0**2))                       # a smooth well along the path
def arrival(m, k, dt=0.5):
    u = np.exp(-(x + 1500)**2/(2*15.0**2)); v = np.zeros(L)  # right-moving pulse: initial velocity = -u_x
    v = -np.gradient(u)
    kh = 0.5*(k + np.roll(k, -1)); t = 0.0; det = 1500
    while t < 4000:
        f = (kh*(np.roll(u, -1) - u) - np.roll(kh, 1)*(u - np.roll(u, 1)))/m
        v += dt*f; u += dt*v; t += dt
        if u[int(L/2 + det)] > 0.5*u.max() and t > 100: return t
for name in ('flat', 'lapse-only', 'GR'):
    N = 1 + Phi; a = 1 - Phi
    if name == 'flat': m = np.ones(L); k = np.ones(L)
    elif name == 'lapse-only': m = 1/N; k = N
    else: m = a**3/N; k = N*a
    t = arrival(m, k); print(f"{name:10s}: arrival tick {t:.1f}")
print("predicted delays: lapse-only = integral |Phi| dx =", round(float(np.sum(np.abs(Phi))), 2), "; GR = twice that")
