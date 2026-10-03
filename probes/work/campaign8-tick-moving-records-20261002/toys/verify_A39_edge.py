#!/usr/bin/env python3
"""Coordinator's check of A39 loophole (b): the light-carrying (antiferromagnetic, J>0) chain next to a record is FULL RANK
on the edge star (sites 1,2 beside the recorded site 0), while the aligned (ferromagnetic) vacuum is rank-deficient (quiet).
Open chain sites 1..N, record at site 0 with content |up>, compressed coupling J sz_0 . s_1 -> J * s^z_1 (field)."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.sparse import kron, identity, csr_matrix
from scipy.sparse.linalg import eigsh
X = csr_matrix(np.array([[0, 1], [1, 0]], complex)); Y = csr_matrix(np.array([[0, -1j], [1j, 0]])); Z = csr_matrix(np.diag([1.0 + 0j, -1.0]))
def op(o, i, N):
    out = identity(1, format="csr", dtype=complex)
    for k in range(N):
        out = kron(out, o if k == i else identity(2, format="csr"), format="csr")
    return out
def ground(N, J, wall):
    H = csr_matrix((2 ** N, 2 ** N), dtype=complex)
    for i in range(N - 1):
        for P in (X, Y, Z):
            H = H + J * op(P, i, N) @ op(P, i + 1, N)
    H = H + wall * J * op(Z, 0, N)        # record (content up) at the left: field on site 1 (index 0)
    w, v = eigsh(H, k=1, which="SA")
    return v[:, 0]
def star_min_eig(psi, N):
    psi = psi.reshape([2] * N)
    m = psi.reshape(4, -1)                # sites (1,2) = indices 0,1
    rho = m @ m.conj().T
    return np.linalg.eigvalsh(rho).min()
for N in (10, 12):
    for wall in (1.0, 3.0, 10.0):
        e_afm = star_min_eig(ground(N, +1.0, wall), N)
        print("N=%d AFM (J>0) wall x%.0f: edge-star smallest eigenvalue %.3e" % (N, wall, e_afm))
    psi_f = ground(N, -1.0, 1.0)
    print("N=%d aligned (J<0, ferro) with the record field: edge-star smallest eigenvalue %.3e" % (N, star_min_eig(psi_f, N)))
