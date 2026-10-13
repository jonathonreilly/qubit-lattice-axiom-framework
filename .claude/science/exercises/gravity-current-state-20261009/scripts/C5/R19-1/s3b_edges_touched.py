"""R19-1 s3b (correction to s3's last line): edges touched by a move = edges with a nonzero G entry in ANY column of the
pattern (s3 counted |G p| > 0 for the all-ones lift, which misses edges where that lift cancels). Also the max |Delta sum gamma^2|
over random configurations, and the exact bound |Delta| <= #touched edges (gamma^2 in {0,1})."""
import numpy as np, sys
sys.path.insert(0, '.')
from common import *
from mc import move_tables, charges
L = 6; V = L**3; G = G_matrix(L); P = pattern_vectors(L)
for a, name in enumerate(["cube", "mu8a", "mu8b", "mu8c"]):
    p = P[a*V]; cols = np.nonzero(p)[0]
    touched = np.nonzero(np.abs(G[:, cols]).sum(1))[0]
    print("%s: slots %d, edges touched (any column) %d, edges with nonzero all-ones lift %d" % (name, len(cols), len(touched), int((np.abs(G @ p) > 0).sum())))
# empirical max |Delta E| over random coset configurations (uniform, bU = 0) for each move type
from mc import sweeps
S, GE, GN = move_tables(L); rng = np.random.default_rng(1)
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); mx = np.zeros(4)
for it in range(200):
    sweeps(n, g, L, 0.0, S, GE, GN, 2, 10 + it, it % 2)
    flat = n.reshape(-1)          # slot index t*V + site with site=(x*L+y)*L+z matches pattern_vectors ordering
    E0 = ((G @ flat)**2).sum()/4
    for a in range(4):
        for b in rng.integers(0, V, 5):
            q = P[a*V + b]; E1 = ((G @ (flat ^ q))**2).sum()/4; mx[a] = max(mx[a], abs(E1 - E0))
print("empirical max |Delta sum gamma^2| per move type over 200 uniform configs x 5 translates:", mx)
