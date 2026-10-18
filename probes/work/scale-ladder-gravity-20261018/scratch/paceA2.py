"""A, source version: every site's pace = average of its 6 neighbours, minus q at record sites (each record drains q).
Far boundary p_inf = 1. Mass should then be additive: (1-p) r -> N q / (4 pi) * 6 ... check scaling with N."""
import numpy as np, scipy.sparse.linalg as spl
L = 61; c = L//2
X, Y, Z = np.meshgrid(*[np.arange(L) - c]*3, indexing='ij'); R = np.sqrt(X**2 + Y**2 + Z**2)
bd = np.zeros((L, L, L), bool); bd[[0, -1], :, :] = bd[:, [0, -1], :] = bd[:, :, [0, -1]] = True
free = ~bd; nf = int(free.sum())
def lap(v):
    u = np.zeros((L, L, L)); u[free] = v
    return (6*u - (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) + np.roll(u, 1, 2) + np.roll(u, -1, 2)))[free]
A = spl.LinearOperator((nf, nf), matvec=lap)
for rad in (0.5, 1.5, 2.2):
    rec = R <= rad; q = 0.01
    rhs = (-6*q*rec)[free]                 # 6 p - sum(nb) = -6 q at records  ->  deficit d = 1 - p obeys lap d = 6 q rec
    d, info = spl.cg(A, -rhs, rtol=1e-12, maxiter=5000)
    D = np.zeros((L, L, L)); D[free] = d
    vals = [D[c+n, c, c]*(1/(1/n - 1/c)) for n in (8, 12)] + [D[c+n, c+n, c+n]*(1/(1/(n*np.sqrt(3)) - 1/c)) for n in (5, 7)]
    print(f"N = {int(rec.sum()):3d} records: (1-p)/(1/r - 1/R) along axis r=8,12 and body r=8.7,12.1: " + ", ".join(f"{v:.4f}" for v in vals) + f"   per record: {np.mean(vals)/rec.sum():.5f}")
