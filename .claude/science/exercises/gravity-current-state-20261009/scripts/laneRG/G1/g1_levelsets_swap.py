# G1 check 1b: robust swap test for 2-component level sets of Omega_K (KG, d=2):
# map every contour cell of component A by q -> K - q and read the label there.
import numpy as np
from scipy import ndimage
exec(open('g1_levelsets.py').read().split('def run(')[0])  # reuse helpers
rng = np.random.default_rng(7)
def robust(eps, d, N, K, E):
    g = np.linspace(-np.pi, np.pi, N, endpoint=False)
    Q = np.array(np.meshgrid(*([g]*d), indexing='ij'))
    W = eps(Q) + eps(K.reshape((d,)+(1,)*d) - Q) - E
    mn = W.copy(); mx = W.copy()
    for off in np.ndindex(*(2,)*d):
        Ws = W
        for ax, o in enumerate(off):
            if o: Ws = np.roll(Ws, -1, axis=ax)
        mn = np.minimum(mn, Ws); mx = np.maximum(mx, Ws)
    mask = (mn <= 0) & (mx >= 0)
    lab, n = periodic_label(mask)
    if n != 2: return n, None
    cells = np.argwhere(lab > 0); same = 0; other = 0
    h = 2*np.pi/N
    for c in cells[::7]:
        q = g[c] + h/2
        q1 = K - q
        j = np.floor((q1 + np.pi)/h).astype(int) % N
        labs = set()
        for off in np.ndindex(*(3,)*d):
            jj = tuple((j + np.array(off) - 1) % N)
            if lab[jj] > 0: labs.add(lab[jj])
        if lab[tuple(c)] in labs and len(labs) == 1: same += 1
        elif labs and lab[tuple(c)] not in labs: other += 1
    return n, (same, other)
for name, eps in (("KG m=1", eps_kg(1.0)), ("KG m=0.2", eps_kg(0.2)), ("KG m=0", eps_kg(0.0))):
    worst = 0; n2 = 0; hist = {}
    for _ in range(40):
        K = rng.uniform(-np.pi, np.pi, 2)
        g = np.linspace(-np.pi, np.pi, 64, endpoint=False)
        Q = np.array(np.meshgrid(g, g, indexing='ij'))
        Om = eps(Q) + eps(K.reshape(2,1,1) - Q); lo, hi = Om.min(), Om.max()
        for E in lo + (hi-lo)*rng.uniform(0.03, 0.97, 12):
            n, so = robust(eps, 2, 384, K, E)
            hist[n] = hist.get(n, 0) + 1
            if n == 2:
                n2 += 1
                if so[0] > 0: worst += 1; print(f"  {name} K={K} E={E:.4f} same/other={so}")
    print(f"{name}: histogram {hist}; 2-comp cases with any cell mapped into its own component: {worst} of {n2}")
