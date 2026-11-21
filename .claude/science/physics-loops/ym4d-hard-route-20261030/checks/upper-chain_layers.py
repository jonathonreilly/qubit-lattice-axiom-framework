#!/usr/bin/env python3
"""(MD*_j) in the free theory, with data frozen at two levels. Text 20 of parts/upper-chain.md.

The question it decides: does freezing regular data at a finer level open a slower channel across the shell
than the coarse one? If it did, (MD*_j) would be false with the rate c_t, at Gaussian order.

Model: 2D free scalar on a strip, periodic in y. Level-1 cells are L x L block averages, level-2 cells L^2 x L^2.
Each side has a frozen site column d0 and frozen level-1 averages d1 on the (L-1)/2 cell columns next to it, as in
a layer family: the site layer is one cell column thick, inside a level-1 layer one coarse block thick. Between the
two sides, D coarse blocks with level-2 averages fixed at W = 0, and level-1 averages free. E(d) is the minimum
energy. K is its off-diagonal block between inner and outer data, split into K00, K01, K10, K11 by level.

Criteria, written before the run.
L1: for L = 3 and L = 5, at each D, every block has rate log(||K(D)|| / ||K(D+1)||) >= 1 per coarse block.
L2: at the largest D reached, ||K00|| <= 10 ||K11||, in units where d0, d1 are site values: the finer data do not
    carry a larger coupling than the coarser data.
"""
import resource

import numpy as np

RSS_LIMIT_GB = 2.0


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


def schur_blocks(L, D, width_blocks):
    ny = width_blocks * L * L
    nc = (L - 1) // 2
    ncols_side = nc * L
    ncols = 2 * ncols_side + D * L * L
    nfree = ncols * ny
    idx = lambda x, y: x * ny + (y % ny)
    A = np.zeros((nfree, nfree))
    for x in range(ncols):
        for y in range(ny):
            i = idx(x, y)
            A[i, i] += 2.0
            A[i, idx(x, y + 1)] -= 1.0
            A[idx(x, y + 1), i] -= 1.0
            if x + 1 < ncols:
                A[i, i] += 1.0
                A[idx(x + 1, y), idx(x + 1, y)] += 1.0
                A[i, idx(x + 1, y)] -= 1.0
                A[idx(x + 1, y), i] -= 1.0
    rows_side = nc * (ny // L)
    nd = 2 * ny + 2 * rows_side  # d0I, d1I, d1O, d0O
    i0I = np.arange(ny)
    i1I = ny + np.arange(rows_side)
    i1O = ny + rows_side + np.arange(rows_side)
    i0O = ny + 2 * rows_side + np.arange(ny)
    P = np.zeros((nfree, nd))
    Q = np.zeros((nd, nd))
    for y in range(ny):
        A[idx(0, y), idx(0, y)] += 1.0
        A[idx(ncols - 1, y), idx(ncols - 1, y)] += 1.0
        P[idx(0, y), i0I[y]] = 1.0
        P[idx(ncols - 1, y), i0O[y]] = 1.0
        Q[i0I[y], i0I[y]] = 1.0
        Q[i0O[y], i0O[y]] = 1.0
    constraints = []
    # level-1 averages on the two sides
    for side, base, data in ((0, 0, i1I), (1, ncols - ncols_side, i1O)):
        k = 0
        for cx in range(nc):
            for cy in range(ny // L):
                row = np.zeros(nfree)
                for x in range(base + cx * L, base + (cx + 1) * L):
                    for y in range(cy * L, (cy + 1) * L):
                        row[idx(x, y)] = 1.0 / L**2
                constraints.append((row, data[k], 1.0))
                k += 1
    # level-2 averages, W = 0, between the sides
    for b in range(D):
        for cy in range(ny // L**2):
            row = np.zeros(nfree)
            for x in range(ncols_side + b * L**2, ncols_side + (b + 1) * L**2):
                for y in range(cy * L**2, (cy + 1) * L**2):
                    row[idx(x, y)] = 1.0 / L**4
            constraints.append((row, None, 0.0))
    m = len(constraints)
    C = np.zeros((m, nfree))
    G = np.zeros((m, nd))
    for i, (row, d, val) in enumerate(constraints):
        C[i] = row
        if d is not None:
            G[i, d] = val
    M = np.block([[A, C.T], [C, np.zeros((m, m))]])
    R = np.vstack([P, G])
    rss_guard()
    W = np.linalg.solve(M, R)
    S = Q - R.T @ W
    rss_guard()
    op = lambda X: float(np.linalg.norm(X, 2))
    return {"K00": op(S[np.ix_(i0I, i0O)]), "K01": op(S[np.ix_(i0I, i1O)]),
            "K10": op(S[np.ix_(i1I, i0O)]), "K11": op(S[np.ix_(i1I, i1O)])}


def main():
    ok1 = True
    ok2 = True
    for L, width, Ds in ((3, 2, (1, 2, 3, 4)), (5, 1, (1, 2, 3))):
        rows = [schur_blocks(L, D, width) for D in Ds]
        for key in ("K00", "K01", "K10", "K11"):
            vals = [r[key] for r in rows]
            rates = [float(np.log(vals[i] / vals[i + 1])) for i in range(len(vals) - 1)]
            print(f"L={L} {key}: " + ", ".join(f"{v:.3e}" for v in vals) + "; rates " + ", ".join(f"{r:.2f}" for r in rates))
            ok1 = ok1 and all(r >= 1 for r in rates)
        ratio = rows[-1]["K00"] / rows[-1]["K11"]
        print(f"L={L}: ||K00||/||K11|| at largest D = {ratio:.3f}")
        ok2 = ok2 and ratio <= 10
    print("L1", "PASS" if ok1 else "FAIL")
    print("L2", "PASS" if ok2 else "FAIL")


if __name__ == "__main__":
    main()
