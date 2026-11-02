#!/usr/bin/env python3
"""T3: flat D-coer constant in d = 2, in L and depth. See CRITERIA.md."""
import resource, sys
import numpy as np
import scipy.linalg as sl

P = 4  # torus of 4 parents; bricks of side 2 parents shifted by 1


def guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 2e9:
        sys.exit("RSS above 2 GB")


def brick(px, py):
    """index of the brick of parent (px, py): rows of height 2, shift 1 per row."""
    row = (py // 2) % 2
    col = ((px - row) // 2) % 2
    return row, col


def tri_row(mu, ybx, yby, n, S):
    """Q row at block side S (in eta units) for level bond (ybx, yby), mu. Bond index lattice n x n.
    Lower-corner blocks: starts in block, path of S steps along mu."""
    w = {}
    for i in range(S):
        for j in range(S):
            sx, sy = ybx * S + i, yby * S + j
            for t in range(S):
                bx, by = (sx + (t if mu == 0 else 0)) % n, (sy + (t if mu == 1 else 0)) % n
                w[(bx, by)] = w.get((bx, by), 0.0) + 1.0 / S ** 3
    return w


def run(L, M, omega_set):
    N = P * L * M
    S_h, S_p = M, L * M
    eta = 1.0 / (L * M)

    def bi(mu, x, y):
        return mu * N * N + (x % N) * N + (y % N)

    def si(x, y):
        return (x % N) * N + (y % N)

    nb = 2 * N * N
    ns = N * N
    Omega = np.zeros((P, P), bool)
    for px in range(P):
        for py in range(P):
            Omega[px, py] = brick(px, py) in omega_set

    def in_om(hx, hy):  # h site -> parent
        return Omega[(hx // L) % P, (hy // L) % P]

    # constraint rows
    rows = []
    for hx in range(P * L):
        for hy in range(P * L):
            for mu in range(2):
                ex, ey = (1, 0) if mu == 0 else (0, 1)
                if in_om(hx, hy) and in_om(hx + ex, hy + ey):
                    rows.append(tri_row(mu, hx, hy, N, S_h))
    for px in range(P):
        for py in range(P):
            for mu in range(2):
                ex, ey = (1, 0) if mu == 0 else (0, 1)
                if not (Omega[px, py] and Omega[(px + ex) % P, (py + ey) % P]):
                    rows.append(tri_row(mu, px, py, N, S_p))
    C = np.zeros((len(rows), nb))
    r = 0
    for hx in range(P * L):
        for hy in range(P * L):
            for mu in range(2):
                ex, ey = (1, 0) if mu == 0 else (0, 1)
                if in_om(hx, hy) and in_om(hx + ex, hy + ey):
                    for (bx, by), val in rows[r].items():
                        C[r, bi(mu, bx, by)] = val
                    r += 1
    for px in range(P):
        for py in range(P):
            for mu in range(2):
                ex, ey = (1, 0) if mu == 0 else (0, 1)
                if not (Omega[px, py] and Omega[(px + ex) % P, (py + ey) % P]):
                    for (bx, by), val in rows[r].items():
                        C[r, bi(mu, bx, by)] = val
                    r += 1
    guard()
    Qc, _ = sl.qr(C.T, mode="full", check_finite=False)
    rank = C.shape[0]  # rows are independent: Section 8 gives a right inverse
    Z = Qc[:, rank:]
    del Qc
    guard()
    # d, D*
    dm = np.zeros((ns, nb))
    Dst = np.zeros((ns, nb))
    for x in range(N):
        for y in range(N):
            p = si(x, y)
            dm[p, bi(0, x, y)] += 1
            dm[p, bi(1, x + 1, y)] += 1
            dm[p, bi(0, x, y + 1)] -= 1
            dm[p, bi(1, x, y)] -= 1
            Dst[p, bi(0, x - 1, y)] += 1
            Dst[p, bi(0, x, y)] -= 1
            Dst[p, bi(1, x, y - 1)] += 1
            Dst[p, bi(1, x, y)] -= 1
    dm /= eta
    Dst /= eta
    # leaves of P_N: subtract means
    leaf = {}
    for x in range(N):
        for y in range(N):
            hx, hy = x // M, y // M
            if in_om(hx, hy):
                key = ("h", hx, hy)
            else:
                key = ("p", hx // L, hy // L)
            leaf.setdefault(key, []).append(si(x, y))
    A = (dm @ Z)
    H1 = A.T @ A
    del A, dm
    B = Dst @ Z
    del Dst
    for ix in leaf.values():
        B[ix] -= B[ix].mean(0, keepdims=True)
    H1 += B.T @ B
    del B
    guard()
    ev = sl.eigvalsh(H1, subset_by_index=[0, 0], check_finite=False)
    return 1.0 / ev[0]


if __name__ == "__main__":
    res = {}
    for name, om in (("one", {(0, 0)}), ("two", {(0, 0), (1, 0)})):
        for L, M in ((4, 1), (8, 1), (16, 1), (4, 2), (4, 4), (8, 2)):
            c = run(L, M, om)
            res[(name, L, M)] = c
            print(name, "L", L, "M", M, "C_0 =", round(c, 4), flush=True)
    ok = True
    for name in ("one", "two"):
        r1 = res[(name, 16, 1)] / res[(name, 8, 1)]
        r2 = res[(name, 4, 4)] / res[(name, 4, 2)]
        print(name, "ratios", r1, r2)
        ok &= r1 <= 1.25 and r2 <= 1.25
    print("T3", "PASS" if ok else "FAIL")
