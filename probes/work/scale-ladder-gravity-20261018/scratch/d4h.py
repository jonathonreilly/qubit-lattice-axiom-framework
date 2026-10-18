import sys, numpy as np
sys.path.insert(0, '.')
from d4e import C
from d4f import golden
def info(k):
    _, s, vh = np.linalg.svd(C.Q(k)); s = s[::-1]/s[0]
    return s
def roots(ks, km, lo=0.97, hi=1.02, npt=500):
    oms = km*np.linspace(lo, hi, npt); f = np.array([info(np.array([*ks, 1j*o]))[32:36] for o in oms])
    out = []
    for j in range(4):
        for i in range(1, npt-1):
            if f[i, j] < f[i-1, j] and f[i, j] < f[i+1, j] and f[i, j] < 1e-6:
                w = golden(lambda o: info(np.array([*ks, 1j*o]))[32+j], oms[i-1], oms[i+1]); out.append(w)
    ws = sorted(set(np.round(np.array(out)/km, 9)))
    res = []
    for w in ws:
        k = np.array([*ks, 1j*w*km]); _, s, vh = np.linalg.svd(C.Q(k)); s = s[::-1]/s[0]
        nul = int((s < 1e-9).sum()); N = vh[-nul:].conj().T; G = C.gauge(k)
        X = N - G @ np.linalg.pinv(G, rcond=1e-9) @ N; X = np.linalg.svd(X)[0][:, :nul-32]
        A = np.hstack([C.line_map(k), G]); sh = np.linalg.svd(A @ np.linalg.pinv(A, rcond=1e-10) @ X, compute_uv=False)
        res.append((w, nul, sh))
    return res
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.1, 0.05):
        r = roots(km*n, km)
        print(f"{name} |k|={km}: " + "; ".join(f"w/k={w:.7f} nullity {nu} metric shares {np.round(sh,3)} alpha {(w*w-1)/km**2:+.4f}" for w, nu, sh in r))
