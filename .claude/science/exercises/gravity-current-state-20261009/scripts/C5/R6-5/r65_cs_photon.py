"""R6-5 (b): a bare (k_AF)_0 term in a NONCOMPACT lattice photon Hamiltonian on Z^3.

Midpoint convention: A_i lives at x + e_i/2, d_j(q) = 2i sin(q_j/2), curl K_ik(q) = eps_ijk d_j(q).
Cup-product CS term A u dA has a fixed link-to-plaquette offset s = (1/2)(1,1,1); averaging it over the 24 proper
rotations (s runs over the 8 vectors (+-1/2)^3) gives  M(q) = c3(q) K(q),  c3 = prod_l cos(q_l/2).
Checks: Hermitian; gauge invariant on both sides (M d = 0, d^+ M = 0); covariant under the 24 proper rotations;
odd under inversion; small-q form eps_ijk i q_j (continuum A.B).  Then the quadratic potential
    V(q) = (1/2) K^+ K - k M
has a negative eigenvalue for |q| < ~2|k| for every k != 0, i.e. the Hamiltonian (1/2)E^2 + V is unbounded below.
"""
import itertools
import numpy as np

eps = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    eps[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])


def d(q):
    return 2j * np.sin(np.asarray(q) / 2)


def K(q):
    return np.einsum('ijk,j->ik', eps, d(q))


def M(q):
    return np.prod(np.cos(np.asarray(q) / 2)) * K(q)


rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if np.isclose(np.linalg.det(R), 1):
            rots.append(R)

rng = np.random.default_rng(7)
herm = gauge = rot = par = 0.0
for _ in range(200):
    q = rng.uniform(-np.pi, np.pi, 3)
    Mq = M(q)
    herm = max(herm, np.abs(Mq - Mq.conj().T).max())
    gauge = max(gauge, np.abs(Mq @ d(q)).max(), np.abs(d(q).conj() @ Mq).max())
    for R in rots:   # A'(Rq) = R A(q)  =>  covariance: R^T M(Rq) R = M(q)
        rot = max(rot, np.abs(R.T @ M(R @ q) @ R - Mq).max())
    par = max(par, np.abs(M(-q) + Mq).max())   # inversion: A(q) -> -A(-q); form invariant iff M(-q) = M(q)
print("Hermitian err %.1e | gauge (M d, d^+ M) err %.1e | proper-rotation covariance err %.1e | M(-q)+M(q) = %.1e (odd: P-odd)"
      % (herm, gauge, rot, par))
q = np.array([1e-3, 2e-3, -1.5e-3])
print("small-q: M(q) / (i eps_ijk q_j) - 1 =", np.abs(M(q) / np.where(np.abs(np.einsum('ijk,j->ik', eps, 1j * q)) > 0, np.einsum('ijk,j->ik', eps, 1j * q), 1) - (np.abs(np.einsum('ijk,j->ik', eps, 1j * q)) > 0)).max())

print("lowest eigenvalue of V(q) = K^+K/2 - k M  along q = |q| n, n = (1,2,2)/3  (negative => H unbounded below)")
n = np.array([1, 2, 2]) / 3
for kk in (1e-3, 1e-2, 1e-1):
    row = []
    for Q in (0.25 * kk, kk, 1.9 * kk, 2.1 * kk, 4 * kk):
        V = 0.5 * K(Q * n).conj().T @ K(Q * n) - kk * M(Q * n)
        row.append(np.linalg.eigvalsh(V).min())
    print("  k=%.0e : |q|/k = 0.25,1,1.9,2.1,4 -> min eig %s ; continuum q(q-2k)/2 = %s"
          % (kk, np.array2string(np.array(row), precision=3), np.array2string(np.array([0.5 * Q * (Q - 2 * kk) for Q in (0.25 * kk, kk, 1.9 * kk, 2.1 * kk, 4 * kk)]), precision=3)))
