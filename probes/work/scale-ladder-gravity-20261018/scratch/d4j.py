import sys, numpy as np
sys.path.insert(0, '.')
from d4e import C, on_shell, stress
import regge_generic as RG
rng = np.random.default_rng(2)
print("Ward: |G(q)^dag J| on/off shell vs scale")
n1, n2, xi = rng.standard_normal(3), rng.standard_normal(3), None
prev = None
for s in (0.1, 0.05, 0.025):
    k1s, k2s = s*n1/np.linalg.norm(n1), 0.7*s*n2/np.linalg.norm(n2)
    k1, p1, _ = on_shell(k1s, 1j*s); k2, p2, _ = on_shell(k2s, 0.7j*s)
    J = stress(k1, p1, k2, p2); q = k1 - k2; G = C.gauge(q)
    w_on = np.linalg.norm(G.T @ J)       # bilinear pairing with displacement directions (holomorphic)
    k2o = np.array([*k2s, 1.2*k2[3]]); Jo = stress(k1, p1, k2o, p2); w_off = np.linalg.norm(C.gauge(k1-k2o).T @ Jo)
    print(f"  s={s}: on {w_on:.3e}  off {w_off:.3e}" + (f"  ratios on {prev[0]/w_on:.2f} off {prev[1]/w_off:.2f}" if prev else ""))
    prev = (w_on, w_off)
# Newtonian rung through the full edge form: source = line-map image of static T_tt
itt = 3
print("Newtonian: metric h_tt * k^2 from full edge solve")
for n in [(1,0,0), (1,1,1), (3,1,2)]:
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.02, 0.5):
        k = np.array([*(km*n), 0.0]); Q = C.Q(k); M = C.line_map(k)
        T = np.zeros(10); T[itt] = 1.0; J = np.conj(M) @ T
        x = np.linalg.pinv(Q, rcond=1e-10) @ J
        h = np.linalg.lstsq(M, x, rcond=None)[0]
        ph = np.sum(4*np.sin(km*n/2)**2)
        print(f"  n={np.round(n,2)} |k|={km}: h_tt k^2 = {h[itt].real*km**2:+.5f}; h_tt * phat^2 = {h[itt].real*ph:+.5f}; residual of metric fit {np.linalg.norm(M@h - x)/np.linalg.norm(x):.1e}")
