"""First-order test: project each covariant pairing Delta onto the 8 exact zero modes of the KS hopping.
M_ab = z_a^T Delta z_b (8x8, antisymmetric).  M != 0 would be a Majorana mass matrix for the light
sector; M = 0 means the light modes stay massless at first order and only the heavy modes see the pairing."""
import sys, numpy as np
src = open('verify_and_bdg.py').read().split('print("\\n== step 2')[0].replace('print(', '(lambda *a, **k: None)(')
sys.argv = ['x', '12']
exec(src)
exec(open('verify_and_bdg.py').read().split('print("\\n== step 2: build invariant Delta for the class of d=(3,1,0), verify invariance ==")')[1].split('nodes, val, ok = build_invariant')[0])
h = np.zeros((N, N))
for (i, j), e in hop.items(): h[i, j] = e
w, V = np.linalg.eigh(h)
Z = V[:, np.abs(w) < 1e-9]
print("zero modes of h:", Z.shape[1])
for d in [(3,1,0),(3,2,-1),(4,2,-1),(4,3,-1),(5,1,0),(4,3,-2),(5,2,-1),(5,3,0),(5,3,-1),(5,3,-2),(5,4,-1),(5,4,-2),(5,4,-3)]:
    nodes, val, ok = build_invariant(d, -1)
    rows = np.array([k[0] for k in val]); cols = np.array([k[1] for k in val]); vals = np.array([val[k] for k in val], dtype=float)
    # M = Z^T Delta Z with Delta_ij = x, Delta_ji = -x
    M = np.zeros((Z.shape[1], Z.shape[1]))
    for r, c, x in zip(rows, cols, vals):
        M += x * (np.outer(Z[r], Z[c]) - np.outer(Z[c], Z[r]))
    print(f"d={d}: max|M| on the 8 light modes = {np.abs(M).max():.2e}   (norm of Delta entries: 1)", flush=True)
