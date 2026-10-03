"""Check 8: one possibility per site (d=1), ring N>=5: every strictly range-1 tick is
either pair-mixing on disjoint adjacent pairs (plus phases) or a phase-weighted shift.
Sample range-1 unitaries by alternating projections from Haar starts and classify them."""
import numpy as np
from common import haar_unitary, ring_allowed
rng = np.random.default_rng(8)

def project(N, iters=6000):
    mask = ~ring_allowed(N)
    U = haar_unitary(N, rng)
    for _ in range(iters):
        V = U.copy(); V[mask] = 0
        W, s, Vh = np.linalg.svd(V); U = W @ Vh
        if np.abs(U[mask]).max() < 1e-13: break
    return U, float(np.abs(U[mask]).max())

def classify(U, tol=1e-6):
    N = U.shape[0]
    right = all(abs(abs(U[(x+1) % N, x]) - 1) < tol for x in range(N))
    left = all(abs(abs(U[(x-1) % N, x]) - 1) < tol for x in range(N))
    if right: return 'shift-right'
    if left: return 'shift-left'
    # pair structure: each site's off-diagonal partners
    for x in range(N):
        partners = [y for y in ((x-1) % N, (x+1) % N) if abs(U[y, x]) > tol or abs(U[x, y]) > tol]
        if len(partners) > 1: return 'OTHER'
        if partners:
            y = partners[0]
            # block {x,y} must be closed
            for z in range(N):
                if z not in (x, y) and (abs(U[z, x]) > tol or abs(U[x, z]) > tol): return 'OTHER'
    return 'pairs'

for N in (5, 6, 7, 8):
    counts = {}
    for k in range(40):
        U, err = project(N)
        lab = classify(U) if err < 1e-10 else 'not-converged'
        counts[lab] = counts.get(lab, 0) + 1
    print(f"N={N}: {counts}")
