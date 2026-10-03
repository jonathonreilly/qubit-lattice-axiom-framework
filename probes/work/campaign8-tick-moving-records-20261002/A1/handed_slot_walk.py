"""Spin (x) direction-slot walk (coin C^2 (x) C^6):
  W_theta(k) = D(k) . exp(i theta sum_v (sigma.v) (x) |v><v|) . (1 (x) G)
D(k) = sum_v exp(-i k.v) 1 (x) |v><v|  (slot v moves along v),
G = Grover coin on the 6 slots (commutes with all slot permutations).
Checks: unitarity; covariance under the 24 proper rotations acting as
U_R (x) Pi_R; behaviour under inversion (k -> -k, slot v -> -v, spin untouched,
the only automorphism choice by Schur)."""
import numpy as np
from walk_covariance import RS, US, SIG

rng = np.random.default_rng(11)
dirs = [np.array(d) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
key = {tuple(d): i for i, d in enumerate(dirs)}


def Pi(R):
    M = np.zeros((6, 6))
    for i, d in enumerate(dirs):
        M[key[tuple(R @ d)], i] = 1
    return M


s = np.ones(6) / np.sqrt(6)
G = 2 * np.outer(s, s) - np.eye(6)


def expm_herm(H, th):
    w, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(1j * th * w)) @ V.conj().T


def W(k, th):
    D = np.kron(np.eye(2), np.diag([np.exp(-1j * k @ d) for d in dirs]))
    K = sum(np.kron(sum(d[a] * SIG[a] for a in range(3)), np.diag(np.eye(6)[i])) for i, d in enumerate(dirs))
    return D @ expm_herm(K, th) @ np.kron(np.eye(2), G)


th = 0.7
ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(20)]
uni = max(np.linalg.norm(W(k, th).conj().T @ W(k, th) - np.eye(12)) for k in ks)
cov = max(np.linalg.norm(W(R @ k, th) - np.kron(U, Pi(R)) @ W(k, th) @ np.kron(U, Pi(R)).conj().T)
          for R, U in zip(RS, US) for k in ks)
PI = np.kron(np.eye(2), Pi(-np.eye(3, dtype=int)))
inv_self = max(np.linalg.norm(PI @ W(-k, th) @ PI.T - W(k, th)) for k in ks)
inv_mirror = max(np.linalg.norm(PI @ W(-k, th) @ PI.T - W(k, -th)) for k in ks)
print(f"unitarity defect {uni:.1e}; proper-rotation covariance defect (24 rotations) {cov:.1e}")
print(f"inversion image vs itself: {inv_self:.3f} (nonzero => not inversion covariant);"
      f" vs theta -> -theta walk: {inv_mirror:.1e}")
th0 = max(np.linalg.norm(PI @ W(-k, 0.0) @ PI.T - W(k, 0.0)) for k in ks)
print(f"theta = 0 (pure slot walk) inversion defect {th0:.1e} (achiral)")
