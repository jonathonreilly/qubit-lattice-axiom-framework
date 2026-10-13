"""R17-1 s8 (written before running). s3 (ii-b) gaps were taken over the full TFIM space (both Z2 sectors).
The face model is the Z2-EVEN sector only (n_f = tau_c xor tau_c'). Report the even-sector gap on 3x3x2."""
import numpy as np, itertools, scipy.sparse as sp, scipy.sparse.linalg as sla
E3 = np.eye(3, dtype=int); Ls = (3,3,2)
faces = [(x, t) for x in itertools.product(*[range(l) for l in Ls]) for t in range(3)]
fidx = {f: n for n, f in enumerate(faces)}
def fk(x, t): return fidx[(tuple(np.mod(x, Ls)), t)]
cubes = []
for x in itertools.product(*[range(l) for l in Ls]):
    x = np.array(x); cubes.append([fk(x, 0), fk(x + E3[2], 0), fk(x, 1), fk(x + E3[0], 1), fk(x, 2), fk(x + E3[1], 2)])
nc = len(cubes); fc = {}
for c, fs in enumerate(cubes):
    for f in fs: fc.setdefault(f, []).append(c)
dim = 2**nc; st = np.arange(dim, dtype=np.int64)
zz = np.zeros(dim)
for f in range(len(faces)): zz += 1 - 2*(((st >> fc[f][0]) & 1) ^ ((st >> fc[f][1]) & 1))
rows = np.concatenate([st ^ (1 << c) for c in range(nc)]); cols = np.tile(st, nc)
Hx = sp.csr_matrix((-np.ones(len(rows)), (rows, cols)), shape=(dim, dim))
for h in [0.0, 0.1, 0.2, 0.3]:
    H = Hx + sp.diags(-h*zz)
    w, v = sla.eigsh(H, k=6, which='SA', tol=1e-10, ncv=40); o = np.argsort(w); w = w[o]; v = v[:, o]
    par = [np.vdot(v[:, i], v[st ^ (dim - 1), i]).real for i in range(6)]
    ev = [w[i] for i in range(6) if par[i] > 0.5]
    print("h/K=%.1f lowest (E, parity): %s ; even-sector gap = %s" %
          (h, [(round(w[i], 5), int(np.sign(par[i]))) for i in range(6)], round(ev[1] - ev[0], 5) if len(ev) > 1 else ">= %.4f" % (w[5]-ev[0])))
