"""Exploratory: small O12 witnesses (lines through 0 in direction (1,c), and small grids)."""
import numpy as np, sys
sys.argv = ['o12.py', 'grid', '2']
exec(open('o12.py').read().split("t0 = time.time()")[0])
def lmin(P):
    K = np.array([[h_exact(*(p - q)) for q in P] for p in P]); ev = np.linalg.eigvalsh(K); return ev[0] / ev[-1], ev
m = 0.55
for dirn in [(1, 0), (1, 1), (1, -1), (1, -0.5), (1, 0.5)]:
    for npts in (5, 9, 17):
        t = np.linspace(-m, m, npts); D = np.array(dirn) / max(abs(dirn[0]), abs(dirn[1]))
        r, _ = lmin(t[:, None] * D[None, :]); print(f"line {dirn} npts {npts}: rel {r:+.3e}")
for n in (3, 4, 5):
    ax = np.linspace(-m, m, n); P = np.array([(x, y) for x in ax for y in ax]); r, ev = lmin(P)
    print(f"grid {n}x{n}: rel {r:+.3e}  lam_min {ev[0]:+.3e}")
