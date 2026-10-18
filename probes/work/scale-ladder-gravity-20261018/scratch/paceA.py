"""A: formation pace on a cubic grid. Empty sites: average of 6 neighbours (linear NN rule). Records: fixed lower
pace. Far boundary: p_inf = 1. Jacobi/CG relaxation of the stationary field; test 1/r and sign."""
import numpy as np, scipy.sparse.linalg as spl
def solve(L, rec, p_rec):
    fixed = rec.copy(); fixed[[0, -1], :, :] = fixed[:, [0, -1], :] = fixed[:, :, [0, -1]] = True
    val = np.where(rec, p_rec, 1.0)
    free = ~fixed; nf = int(free.sum()); fi = np.full(rec.shape, -1); fi[free] = np.arange(nf)
    def lap(v):
        u = np.zeros(rec.shape); u[free] = v
        out = 6*u - (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) + np.roll(u, 1, 2) + np.roll(u, -1, 2))
        return out[free]
    g = np.where(fixed, val, 0.0)
    rhs = (np.roll(g, 1, 0) + np.roll(g, -1, 0) + np.roll(g, 1, 1) + np.roll(g, -1, 1) + np.roll(g, 1, 2) + np.roll(g, -1, 2))[free]
    A = spl.LinearOperator((nf, nf), matvec=lap)
    x, info = spl.cg(A, rhs, rtol=1e-11, maxiter=5000)
    p = val.copy(); p[free] = x; return p, info
L = 61; c = L//2
X, Y, Z = np.meshgrid(*[np.arange(L) - c]*3, indexing='ij'); R = np.sqrt(X**2 + Y**2 + Z**2)
Rb = c  # box half-size: grounded-sphere-like correction 1/r - 1/Rb approx
for rad, p_rec in ((0.5, 0.5), (2.2, 0.5), (2.2, 0.8)):
    rec = R <= rad; p, info = solve(L, rec, p_rec)
    print(f"records: ball radius {rad} ({int(rec.sum())} sites), record pace {p_rec} (cg info {info}):")
    for nm, d in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
        d = np.array(d); out = []
        for r in (5, 8, 11, 14):
            n = max(1, int(round(r/np.linalg.norm(d)))); q = c + n*d; rr = n*np.linalg.norm(d)
            out.append(f"r={rr:5.2f}: (1-p)/(1/r-1/{Rb}) = {(1-p[tuple(q)])/(1/rr - 1/Rb):.4f}")
        print("   ", nm, "; ".join(out))
