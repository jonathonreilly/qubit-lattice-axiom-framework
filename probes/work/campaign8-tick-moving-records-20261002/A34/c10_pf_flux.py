"""A34 c10: Choi information flux of A37's fill-behind step PF (erase y's content, refill x fresh) vs the swap.
Window {x, y, a, b}: input sites (y, a, b) -> output sites (x, a, b); split W1 = {x, a}, W2 = {y, b}."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
def S(r):
    w = np.linalg.eigvalsh(r); w = w[w > 1e-13]; return float(-(w * np.log2(w)).sum())
def ptr(rho, keep, n=6):
    r = rho.reshape([2] * (2 * n)); tr = [i for i in range(n) if i not in keep]
    for k, i in enumerate(sorted(tr, reverse=True)):
        r = np.trace(r, axis1=i, axis2=i + r.ndim // 2)
    d = 2 ** len(keep); return r.reshape(d, d)
def choi(kraus):   # outputs (x, a, b) = 0,1,2 ; references (Ry, Ra, Rb) = 3,4,5
    rho = np.zeros((64, 64), complex)
    for K in kraus:
        v = np.zeros(64, complex)
        for i in range(8):
            v += np.kron(K[:, i], np.eye(8)[i])
        rho += np.outer(v, v.conj()) / 8
    return rho
def flux(rho):
    I = lambda A, B: S(ptr(rho, A)) + S(ptr(rho, B)) - S(ptr(rho, sorted(A + B)))
    return 0.5 * (I([0, 1], [3, 5]) - I([2], [4]))
# swap: y's content -> x (input order y,a,b ; output order x,a,b): identity matrix on 3 qubits
print("swap flux:", round(flux(choi([np.eye(8)])), 6))
# PF: trace out y, prepare x in |0>: Kraus K_j = |0>_x <j|_y (x) I_ab
kr = []
for j in range(2):
    K = np.zeros((8, 8))
    for ab in range(4):
        K[0 * 4 + ab, j * 4 + ab] = 1.0
    kr.append(K)
print("fill-behind (PF) flux:", round(flux(choi(kr)), 6))
