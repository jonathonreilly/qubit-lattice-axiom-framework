#!/usr/bin/env python3
"""T3: flat D-coer constant in d = 2, in L and depth, by a sparse saddle solve. See CRITERIA.md."""
import os, subprocess, threading, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

P = 4  # torus of 4 parents; bricks of side 2 parents shifted by 1


def watchdog():
    def loop():
        while True:
            rss = int(subprocess.check_output(["ps", "-o", "rss=", "-p", str(os.getpid())]))
            if rss > 2_000_000:
                print("watchdog: RSS above 2 GB, stopping", flush=True)
                os._exit(3)
            time.sleep(1.0)

    threading.Thread(target=loop, daemon=True).start()


def brick(px, py):
    row = (py // 2) % 2
    col = ((px - row) // 2) % 2
    return row, col


def run(L, M, omega_set):
    N = P * L * M
    S_h, S_p = M, L * M
    eta = 1.0 / (L * M)
    bi = lambda mu, x, y: mu * N * N + (x % N) * N + (y % N)
    si = lambda x, y: (x % N) * N + (y % N)
    nb, ns = 2 * N * N, N * N
    Omega = np.array([[brick(px, py) in omega_set for py in range(P)] for px in range(P)])
    in_om = lambda hx, hy: Omega[(hx // L) % P, (hy // L) % P]

    ri, ci, va = [], [], []
    nrow = 0

    def add_row(mu, yx, yy, S):
        nonlocal nrow
        w = {}
        for i in range(S):
            for j in range(S):
                for t in range(S):
                    bx = yx * S + i + (t if mu == 0 else 0)
                    by = yy * S + j + (t if mu == 1 else 0)
                    k = bi(mu, bx, by)
                    w[k] = w.get(k, 0.0) + 1.0 / S ** 3
        for k, v in w.items():
            ri.append(nrow), ci.append(k), va.append(v)
        nrow += 1

    for hx in range(P * L):
        for hy in range(P * L):
            for mu, (ex, ey) in enumerate(((1, 0), (0, 1))):
                if in_om(hx, hy) and in_om(hx + ex, hy + ey):
                    add_row(mu, hx, hy, S_h)
    for px in range(P):
        for py in range(P):
            for mu, (ex, ey) in enumerate(((1, 0), (0, 1))):
                if not (Omega[px, py] and Omega[(px + ex) % P, (py + ey) % P]):
                    add_row(mu, px, py, S_p)
    C = sp.csc_matrix((va, (ri, ci)), shape=(nrow, nb))

    dr, dc, dv, sr, sc, sv = [], [], [], [], [], []
    for x in range(N):
        for y in range(N):
            p = si(x, y)
            for k, v in ((bi(0, x, y), 1), (bi(1, x + 1, y), 1), (bi(0, x, y + 1), -1), (bi(1, x, y), -1)):
                dr.append(p), dc.append(k), dv.append(v / eta)
            for k, v in ((bi(0, x - 1, y), 1), (bi(0, x, y), -1), (bi(1, x, y - 1), 1), (bi(1, x, y), -1)):
                sr.append(p), sc.append(k), sv.append(v / eta)
    dm = sp.csr_matrix((dv, (dr, dc)), shape=(ns, nb))
    Dst = sp.csr_matrix((sv, (sr, sc)), shape=(ns, nb))

    leaf = {}
    for x in range(N):
        for y in range(N):
            hx, hy = x // M, y // M
            key = ("h", hx, hy) if in_om(hx, hy) else ("p", hx // L, hy // L)
            leaf.setdefault(key, []).append(si(x, y))
    lr, lc, lv = [], [], []
    for b, ix in enumerate(leaf.values()):
        lr += ix
        lc += [b] * len(ix)
        lv += [1.0 / np.sqrt(len(ix))] * len(ix)
    Pi = sp.csr_matrix((lv, (lr, lc)), shape=(ns, len(leaf)))
    W = (Pi.T @ Dst).tocsr()  # supported on leaf boundaries
    K = (dm.T @ dm + Dst.T @ Dst - W.T @ W).tocsc()
    Sad = sp.bmat([[K, C.T], [C, None]], format="csc")
    lu = sla.splu(Sad)
    zero = np.zeros(nrow)
    Gop = sla.LinearOperator((nb, nb), matvec=lambda r: lu.solve(np.concatenate([np.ravel(r), zero]))[:nb], dtype=float)
    ev = sla.eigsh(Gop, k=1, which="LA", return_eigenvectors=False, tol=1e-6, ncv=40)
    return float(ev[0]), nrow, nb


if __name__ == "__main__":
    watchdog()
    res = {}
    sizes = ((4, 1), (8, 1), (16, 1), (4, 2), (4, 4), (8, 2), (32, 1), (4, 8), (8, 4), (16, 2))
    for name, om in (("one", {(0, 0)}), ("two", {(0, 0), (1, 0)})):
        for L, M in sizes:
            c, nr, nb = run(L, M, om)
            res[(name, L, M)] = c
            print(name, "L", L, "M", M, "C_0 =", round(c, 5), "rows", nr, "bonds", nb, flush=True)
    ok = True
    for name in ("one", "two"):
        r1 = res[(name, 16, 1)] / res[(name, 8, 1)]
        r2 = res[(name, 4, 4)] / res[(name, 4, 2)]
        print(name, "ratios", r1, r2)
        ok &= r1 <= 1.25 and r2 <= 1.25
    print("T3", "PASS" if ok else "FAIL")
