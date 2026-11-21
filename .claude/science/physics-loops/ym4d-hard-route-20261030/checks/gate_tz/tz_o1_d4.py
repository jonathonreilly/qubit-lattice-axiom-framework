#!/usr/bin/env python3
"""Gate theorem-z-repaired, N2b: N2 of tz_o1_blocks.py in d = 4, with no factorisation. Written before running.

The direct run at d = 4, L = 3 was stopped by the RSS guard during LU. Same model, parent datum and modes block and hull. a_0: MINRES on the KKT system. Free steps: LSMR on D restricted to Y.
Control replacing block-Q, same content: a_0 stationary with the constraint, max |D^T D a_0 + Q^T lam| at most 1e-5, and constraint residual at most 1e-6. If not reached in the iteration limit, the size is reported as NOT CONVERGED and not read.
Reading unchanged: rho(block) >= 0.1 and s >= 0.1 at L = 3, 5: (O1) with these Y_i fails in this model. Reported: rho(hull).
Limits as N2. d = 4, 3 blocks across, L = 3, 5 only. RSS guard 2 GB by the parent process; wall limit 20 min per size.
"""
import importlib.util, itertools, os, subprocess, sys, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = os.path.dirname(os.path.abspath(__file__))

def job(d, L, n):
    spec = importlib.util.spec_from_file_location("fc", os.path.join(HERE, "..", "hard-core--mapped_face_constant.py"))
    fc = importlib.util.module_from_spec(spec); spec.loader.exec_module(fc)
    M = fc.Model(d, L, n, n)
    D, _ = M.plaquettes(); D = D.tocsr()
    Q = M.constraints().tocsr()
    nl, nc = D.shape[1], Q.shape[0]
    h = M.h
    c = tuple(L * (n // 2) + h for _ in range(d))
    centres = list(itertools.product(*[[L * q + h for q in range(s // L)] for s in M.shape]))
    k0 = centres.index(c) * d
    p = np.zeros(nc); p[k0] = 1.0
    Dt = D.T.tocsr(); Qt = Q.T.tocsr()
    diagH = np.maximum(np.asarray(D.multiply(D).sum(axis=0)).ravel(), 1.0)
    S = np.maximum(np.asarray(Q.multiply(Q).multiply(1 / diagH[None, :]).sum(axis=1)).ravel(), 1e-12)
    def mv(z):
        a, lam = z[:nl], z[nl:]
        return np.concatenate([Dt @ (D @ a) + Qt @ lam, Q @ a])
    K = spla.LinearOperator((nl + nc, nl + nc), matvec=mv, dtype=float)
    P = spla.LinearOperator((nl + nc, nl + nc), matvec=lambda z: np.concatenate([z[:nl] / diagH, z[nl:] / S]), dtype=float)
    t0 = time.time()
    sol, info = spla.minres(K, np.concatenate([np.zeros(nl), p]), M=P, rtol=1e-10, maxiter=60000)
    a0, lam = sol[:nl], sol[nl:]
    stat = float(np.abs(Dt @ (D @ a0) + Qt @ lam).max()); res = float(np.abs(Q @ a0 - p).max())
    E0 = float(np.sum((D @ a0) ** 2))
    print(f"d {d} L {L} n {n} bonds {nl} minres info {info} {time.time()-t0:.0f}s E0 {E0:.6f} stationarity {stat:.1e} residual {res:.1e}", flush=True)
    conv = stat <= 1e-5 and res <= 1e-6
    def bonds(inside):
        out = []
        for x in itertools.product(*[range(s) for s in M.shape]):
            if not inside(x):
                continue
            for m in range(d):
                y = list(x); y[m] = (y[m] + 1) % M.shape[m]
                if inside(tuple(y)):
                    out.append(M.link(x, m))
        return np.array(sorted(out))
    cp = list(c); cp[0] += L
    inblocks = lambda x: all(abs(x[i] - c[i]) <= h for i in range(d)) or all(abs(x[i] - cp[i]) <= h for i in range(d))
    incube = lambda x: all(abs(x[i] - c[i]) <= 1 for i in range(d))
    r = D @ a0
    for name, Y in (("block", bonds(inblocks)), ("hull", bonds(incube))):
        w = spla.lsmr(D[:, Y].tocsc(), -r, atol=1e-11, btol=1e-11, maxiter=40000)[0]
        a = a0.copy(); a[Y] += w
        E = float(np.sum((D @ a) ** 2))
        print(f"   {name:6s} |Y| {len(Y)} rho {(E0-E)/E0:.5f} s {float(np.abs(Q @ a - p).max()):.4f}" + ("" if conv else "  NOT CONVERGED, not read"), flush=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        job(*map(int, sys.argv[1:4])); sys.exit(0)
    for d, L, n in ((4, 3, 3), (4, 5, 3)):
        p = subprocess.Popen([sys.executable, __file__, str(d), str(L), str(n)])
        t0 = time.time()
        while p.poll() is None:
            time.sleep(1)
            try:
                rss = int(subprocess.check_output(["ps", "-o", "rss=", "-p", str(p.pid)]).split()[0])
            except Exception:
                continue
            if rss > 2 * 1024 * 1024 or time.time() - t0 > 1200:
                p.kill(); print("guard stopped", d, L, n, "rss kB", rss, flush=True); break
