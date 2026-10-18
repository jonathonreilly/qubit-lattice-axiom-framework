import sys, numpy as np
sys.path.insert(0, '.')
from d4e import C
def svn(k):
    s = np.sort(np.linalg.svd(C.Q(k), compute_uv=False)); return s/s[-1]
for name, n in {'axis': (1,0,0), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n); km = 0.1; ks = km*n
    oms = np.linspace(0.2*km, 3*km, 600); f = np.array([svn(np.array([*ks, 1j*o]))[32:36] for o in oms])
    mins = [(oms[i]/km, f[i]) for i in range(1, 599) if f[i, 0] < f[i-1, 0] and f[i, 0] < f[i+1, 0]]
    mins1 = [(oms[i]/km) for i in range(1, 599) if f[i, 2] < f[i-1, 2] and f[i, 2] < f[i+1, 2]]
    print(name, "local minima of sv33 at w/k:", [f"{m[0]:.3f}" for m in mins], " of sv35:", [f"{m:.3f}" for m in mins1])
    # metric content of the null space at w/k ~ 1
    w = km*min(mins, key=lambda m: abs(m[0]-1))[0]; k = np.array([*ks, 1j*w])
    _, s, vh = np.linalg.svd(C.Q(k)); N = vh[-34:].conj().T; G = C.gauge(k)
    X = N - G @ np.linalg.pinv(G, rcond=1e-9) @ N; X = np.linalg.svd(X)[0][:, :2]
    M = C.line_map(k); A = np.hstack([M, G]); share = np.linalg.svd(A @ np.linalg.pinv(A, rcond=1e-10) @ X, compute_uv=False)
    print(f"   at w/k={w/km:.4f}: the 2 extra null directions' share in im M + im G: {share.round(4)}")
