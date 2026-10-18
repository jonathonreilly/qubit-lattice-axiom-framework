import numpy as np
from disp import maxwell_hol, kv, golden
def roots(ks, km):
    # det of the 15x15 form restricted off gauge: use product of 2 smallest non-gauge svs; find the two roots separately
    oms = np.linspace(0.97*km, 1.005*km, 400)
    s = np.array([np.sort(np.linalg.svd(maxwell_hol(kv(ks, o)), compute_uv=False)) for o in oms])
    out = []
    for idx in (1, 2):
        f = s[:, idx]/s[:, -1]; i = int(np.argmin(f))
        lo, hi = oms[max(i-2, 0)], oms[min(i+2, len(oms)-1)]
        om = golden(lambda o: (lambda t: t[idx]/t[-1])(np.sort(np.linalg.svd(maxwell_hol(kv(ks, o)), compute_uv=False))), lo, hi)
        out.append(om)
    return out
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'face-': (1,-1,0), 'body': (1,1,1), 'body-': (1,1,-1), 'gen': (3,1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n)
    al = []
    for km in (0.1, 0.05):
        r = roots(km*n, km); al.append([(o**2/km**2-1)/km**2 for o in r])
    a = (4*np.array(al[1]) - np.array(al[0]))/3
    print(f"{name:6s} Maxwell pol alphas {a[0]:+.6f} {a[1]:+.6f}   raw(k=.05) {al[1][0]:+.6f} {al[1][1]:+.6f}")
