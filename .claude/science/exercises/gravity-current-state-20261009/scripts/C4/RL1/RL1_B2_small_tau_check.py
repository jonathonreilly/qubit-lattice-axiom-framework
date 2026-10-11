"""RL1 (B2): independent check of the Volterra mean Hbar at small tau (T = 1, 1.5): Neumann terms by direct Monte Carlo
integration over the diamond (k = 1, 2, 3 hops), rho = 1."""
import numpy as np
rng = np.random.default_rng(5)
def fc(t2):
    m = np.pi*np.maximum(t2, 0)**2/24; return np.exp(-m)*(1 - 9*m + 8*m**2 - (4/3)*m**3)
def diamond(T, n):
    out = []; got = 0
    while got < n:
        t = rng.uniform(0, T, 4*n); xyz = rng.uniform(-T/2, T/2, (4*n, 3))
        ok = np.sqrt((xyz**2).sum(1)) < np.minimum(t, T-t); out.append(np.column_stack([t[ok], xyz[ok]])); got += ok.sum()
    return np.vstack(out)[:n]
def tau2(a, b):
    d = b - a; return d[..., 0]**2 - (d[..., 1:]**2).sum(-1)
for T in [1.0, 1.5, 2.0]:
    V = np.pi/24*T**4; y = np.zeros(4); x = np.array([T, 0, 0, 0.])
    n = 2_000_000; Z = diamond(T, n)
    h1 = fc(T*T)
    g = fc(tau2(y, Z))*fc(tau2(Z, x)); h2 = V*g.mean(); e2 = V*g.std()/np.sqrt(n)
    # 3 hops: z1 < z2 both in diamond
    n3 = 2_000_000; Z1 = diamond(T, n3); Z2 = diamond(T, n3)
    ordered = (Z2[:, 0] > Z1[:, 0]) & (tau2(Z1, Z2) > 0)
    g3 = np.where(ordered, fc(tau2(y, Z1))*fc(np.where(ordered, tau2(Z1, Z2), 0))*fc(tau2(Z2, x)), 0.0)
    h3 = V*V*g3.mean(); e3 = V*V*g3.std()/np.sqrt(n3)
    print("T=%.1f: f(T)=%+.5f  2-hop=%+.5f+-%.5f  3-hop=%+.5f+-%.5f  sum(1..3)=%+.5f" % (T, h1, h2, e2, h3, e3, h1+h2+h3))
d = np.load("RL1_B_Hbar_h0.02.npz"); print("Volterra Hbar(1, 1.5, 2) =", np.interp([1, 1.5, 2], d["taus"], d["H"]))
