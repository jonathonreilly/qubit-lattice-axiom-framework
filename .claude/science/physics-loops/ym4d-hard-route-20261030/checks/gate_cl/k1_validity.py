#!/usr/bin/env python3
"""V1, V2 of K1: dense constrained minimiser at N' = 2, L = 3 against the Fourier lift, in plaquette angles. Torus 6^4, abelian."""
import numpy as np, sys
sys.path.insert(0, ".")
import k1_kernel as k
L, Np, d = 3, 2, 4
n = L * Np
idx = lambda x, mu: (np.ravel_multi_index(tuple(c % n for c in x), (n,) * d)) * d + mu
nv = n**d * d
# curl operator on fine bonds
rows = []
for x in np.ndindex(*(n,) * d):
    for mu in range(d):
        for nu in range(mu + 1, d):
            xm = list(x); xm[mu] += 1
            xn = list(x); xn[nu] += 1
            rows.append({idx(x, mu): 1.0, idx(xm, nu): 1.0, idx(xn, mu): -1.0, idx(x, nu): -1.0})
def dense(rows, ncol):
    A = np.zeros((len(rows), ncol))
    for i, r in enumerate(rows):
        for j, v in r.items():
            A[i, j] += v
    return A
Cf = dense(rows, nv)
# Q_path: y in L Z^4, avg over block offsets of the line of L bonds
r = (L - 1) // 2
qrows = []
for y in np.ndindex(*(Np,) * d):
    for mu in range(d):
        e = {}
        for o in np.ndindex(*(L,) * d):
            base = [L * y[i] + o[i] - r for i in range(d)]
            for t in range(L):
                b = list(base); b[mu] += t
                j = idx(b, mu)
                e[j] = e.get(j, 0.0) + 1.0 / L**d
        qrows.append(e)
Q = dense(qrows, nv)
nc = Np**d * d
cidx = lambda y, mu: np.ravel_multi_index(tuple(c % Np for c in y), (Np,) * d) * d + mu
crows = []
for y in np.ndindex(*(Np,) * d):
    for mu in range(d):
        for nu in range(mu + 1, d):
            ym = list(y); ym[mu] += 1
            yn = list(y); yn[nu] += 1
            crows.append({cidx(y, mu): 1.0, cidx(ym, nu): 1.0, cidx(yn, mu): -1.0, cidx(y, nu): -1.0})
Cc = dense(crows, nc)
# minimise |Cf H|^2 subject to Cc Q H = Cc Y, Y unit bond at origin along 0 minus the mean
Y = np.zeros(nc); Y[cidx((0,0,0,0), 0)] = 1.0
Y[::d] -= 1.0 / Np**d
B = Cc @ Q
A = Cf.T @ Cf
b = Cc @ Y
# nullspace method through pinv on the KKT system
KKT = np.block([[A, B.T], [B, np.zeros((B.shape[0], B.shape[0]))]])
rhs = np.concatenate([np.zeros(nv), b])
sol = np.linalg.lstsq(KKT, rhs, rcond=1e-11)[0]
H = sol[:nv]
print("dense: constraint residual", np.abs(B @ H - b).max(), "stationarity", np.abs(A @ H + B.T @ sol[nv:]).max())
Fd = Cf @ H
# Fourier
gen = k.fourier_lift(L, Np, 1, np.float64)
mup, Ht, q1, nn, ell, s, gi, flat = next(gen)
Hx = np.stack([k.to_position(Ht[mu], q1, mu, n) for mu in range(d)], -1)
Hv = np.zeros(nv)
for x in np.ndindex(*(n,) * d):
    for mu in range(d):
        Hv[idx(x, mu)] = Hx[x + (mu,)]
Ff = Cf @ Hv
print("Fourier: curl constraint residual", np.abs(Cc @ Q @ Hv - b).max())
print("plaquette angles, dense vs Fourier: max diff", np.abs(Fd - Ff).max(), "max", np.abs(Fd).max())
print("energies", (Fd**2).sum(), (Ff**2).sum())
