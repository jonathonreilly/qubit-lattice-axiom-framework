#!/usr/bin/env python3
"""Gate theorem-z-repaired, N2: is (O1) true with Y_i containing the blocks of affected parents? Written before running.

Claim read: `library/quiet-boundary-rarity.md`, (O1): G_i >= -delta T^2 |R_i|, delta small for L large, by a line fraction f <= C (r/L)^3 of a parent. The same text puts "the blocks of affected parents" in Y_i, and (O2) needs them there, since the bump moves level-j data on the whole block.

Model: U(1), one level, Wilson quadratic energy ||D a||^2, block constraint Q of `checks/hard-core--mapped_face_constant.py`, torus of n blocks. Parent data p: one parent bond with value 1, all others 0, so parent flux 1 =: T on its plaquettes. a_0 := the minimal lift. Modes:
 block: Y := bonds with both ends in the two blocks of that parent bond; free on Y, Q not imposed. This is the step from 𝒜_i to 𝒜_{i-1} if Y_i holds those blocks.
 block-Q: the same with Q imposed. Control: energy change at most 1e-6 of E(a_0), as a_0 is the global constrained minimiser.
 hull: Y := bonds with both ends in a cube of radius 1 about the block centre; Q not imposed. Control for the fraction count.
Read out: rho := (E(a_0) - E_min) / E(a_0), and s := largest |Q(a_min) - p|.
PRE-STATED reading.
 C0 controls: block-Q within 1e-6; constraint residual of a_0 at most 1e-7.
 C1 if rho(block) >= 0.1 and s >= 0.1 at every L: (O1) with these Y_i fails in this model, as delta is the fraction of parent energy that is released and it does not fall with L.
 C2 if rho(block) falls below half its value at L = 3 by the largest L: (O1) may survive in this model; report so.
 Reported: rho(hull), expected to fall with L.
Limits: abelian, one level, one parent, torus; d = 3 at L = 3, 5, 7, d = 4 at L = 3. It tests the mechanism, not the size in SU(2). RSS guard 2 GB by a parent process that polls ps.
"""
import importlib.util, itertools, os, subprocess, sys, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = os.path.dirname(os.path.abspath(__file__))

def load():
    spec = importlib.util.spec_from_file_location("fc", os.path.join(HERE, "..", "hard-core--mapped_face_constant.py"))
    fc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fc)
    return fc

def solve_free(D, a0, Y, Qy=None, reg=1e-10):
    r = D @ a0
    Dy = D[:, Y].tocsc()
    n = len(Y)
    H = (Dy.T @ Dy).tocsc() + reg * sp.identity(n, format="csc")
    g = -(Dy.T @ r)
    if Qy is None:
        w = spla.splu(H, permc_spec="COLAMD").solve(g)
    else:
        keep = np.asarray(np.abs(Qy).sum(axis=1)).ravel() > 1e-14
        Qk = Qy[keep]
        K = sp.bmat([[H, Qk.T], [Qk, -reg * sp.identity(Qk.shape[0])]], format="csc")
        rhs = np.concatenate([g, np.zeros(Qk.shape[0])])
        w = spla.splu(K, permc_spec="COLAMD").solve(rhs)[:n]
    return w

def job(d, L, n):
    fc = load()
    M = fc.Model(d, L, n, n)
    D, _ = M.plaquettes()
    D = D.tocsr()
    Q = M.constraints().tocsr()
    nl, nc = D.shape[1], Q.shape[0]
    reg = 1e-9
    K = sp.bmat([[D.T @ D + reg * sp.identity(nl), Q.T], [Q, -reg * sp.identity(nc)]], format="csc")
    lu = spla.splu(K, permc_spec="COLAMD")
    # parent bond: first constraint row of direction 0 at block centre c = (h, ..., h) + L (n // 2) e
    h = M.h
    c = tuple(L * (n // 2) + h for _ in range(d))
    cidx = 0
    centres = list(itertools.product(*[[L * q + h for q in range(s // L)] for s in M.shape]))
    k0 = centres.index(c) * d
    p = np.zeros(nc); p[k0] = 1.0
    sol = lu.solve(np.concatenate([np.zeros(nl), p]))
    a0 = sol[:nl]
    res = np.abs(Q @ a0 - p).max()
    E0 = float(np.sum((D @ a0) ** 2))
    def bonds(inside):
        out = []
        for x in itertools.product(*[range(s) for s in M.shape]):
            for m in range(d):
                y = list(x); y[m] = (y[m] + 1) % M.shape[m]
                if inside(x) and inside(tuple(y)):
                    out.append(M.link(x, m))
        return np.array(sorted(out))
    cp = list(c); cp[0] += L
    inblocks = lambda x: all(abs(x[i] - c[i]) <= h for i in range(d)) or all(abs(x[i] - cp[i]) <= h for i in range(d))
    incube = lambda x: all(abs(x[i] - c[i]) <= 1 for i in range(d))
    Yb, Yh = bonds(inblocks), bonds(incube)
    out = {}
    for name, Y, withQ in (("block", Yb, False), ("block-Q", Yb, True), ("hull", Yh, False)):
        Qy = Q[:, Y].tocsr() if withQ else None
        w = solve_free(D, a0, Y, Qy)
        a = a0.copy(); a[Y] += w
        E = float(np.sum((D @ a) ** 2))
        out[name] = ((E0 - E) / E0, float(np.abs(Q @ a - p).max()))
    print(f"d {d} L {L} n {n} bonds {nl} E0 {E0:.5f} residual {res:.1e} |Yb| {len(Yb)} |Yh| {len(Yh)}", flush=True)
    for k, v in out.items():
        print(f"   {k:8s} rho {v[0]:.5f}  s {v[1]:.4f}", flush=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        job(*map(int, sys.argv[1:4]))
        sys.exit(0)
    for d, L, n in ((3, 3, 3), (3, 5, 3), (3, 7, 3), (4, 3, 3)):
        p = subprocess.Popen([sys.executable, __file__, str(d), str(L), str(n)])
        while p.poll() is None:
            time.sleep(1)
            try:
                rss = int(subprocess.check_output(["ps", "-o", "rss=", "-p", str(p.pid)]).split()[0])
            except Exception:
                continue
            if rss > 2 * 1024 * 1024:
                p.kill(); print("RSS guard stopped", d, L, n, flush=True); break
