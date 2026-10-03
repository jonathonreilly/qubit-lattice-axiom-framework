"""E2: 12x12 star-local covariant CHIRAL walk (content = direction (6) x spin-1/2 (2)).
      U(k) = S(k) C,  S = sum_v |v><v| e^{i k.v} (x) 1   (each content hops one site along its own direction v)
      C = G exp(-i beta Hel),  G = (2|s><s| - 1)(x)1 (Grover mixing of directions),
      Hel = sum_v |v><v| (x) (v.sigma)   (helicity: proper-rotation invariant, inversion odd).
      Two-layer variant U2 = S C S C' also checked.
E4: M = i d4 + d.sigma : strictly local, invertible on the torus, NOT unitary (inverse not strictly local).
"""
import time
import numpy as np
from scipy.linalg import expm
from wlib import grid, w3_from, proper_rotations, spin_half, SIG
from models import E4

t0 = time.time()
V = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], dtype=float)
sv = np.ones(6) / np.sqrt(6)
G = np.kron(2 * np.outer(sv, sv) - np.eye(6), np.eye(2))
Hel = sum(np.kron(np.diag(np.eye(6)[i]), np.einsum("a,aij->ij", V[i], SIG)) for i in range(6))


def coin(beta, alpha=0.0):
    return G @ expm(-1j * beta * Hel) @ expm(-1j * alpha * np.kron(np.eye(6), np.eye(2)))


def S_and_dS(K):
    ph = np.exp(1j * K @ V.T)  # (M,6)
    S = np.zeros((len(K), 12, 12), complex)
    dS = np.zeros((3, len(K), 12, 12), complex)
    for i in range(6):
        for s in range(2):
            S[:, 2 * i + s, 2 * i + s] = ph[:, i]
            for j in range(3):
                dS[j, :, 2 * i + s, 2 * i + s] = 1j * V[i, j] * ph[:, i]
    return S, dS


def walk1(K, beta=0.7):
    S, dS = S_and_dS(K)
    C = coin(beta)
    return S @ C, np.stack([dS[j] @ C for j in range(3)])


def walk2(K, b1=0.7, b2=-1.9):
    S, dS = S_and_dS(K)
    C1, C2 = coin(b1), coin(b2)
    U = S @ C1 @ S @ C2
    dU = np.stack([dS[j] @ C1 @ S @ C2 + S @ C1 @ dS[j] @ C2 for j in range(3)])
    return U, dU


def perm(R):
    P = np.zeros((6, 6))
    for i in range(6):
        j = np.argmin(np.linalg.norm(V - R @ V[i], axis=1))
        P[j, i] = 1
    return P


print("E2: 12x12 star-local covariant chiral walk")
rng = np.random.default_rng(3)
Kr = rng.uniform(0, 2 * np.pi, (30, 3))
for name, f in (("U=S C", walk1), ("U=S C S C'", walk2)):
    U, _ = f(Kr)
    ncov = nimp = 0
    for R in proper_rotations():
        D = np.kron(perm(R), spin_half(R))
        UR, _ = f(Kr @ R.T)
        ncov += np.abs(UR - D @ U @ D.conj().T).max() < 1e-10
        Di = np.kron(perm(-R), spin_half(R))  # improper -R, spin axial
        UI, _ = f(Kr @ (-R).T)
        nimp += np.abs(UI - Di @ U @ Di.conj().T).max() < 1e-10
    print(f"  {name}: proper covariant {ncov}/24, improper covariant {nimp}/24")
    for N in (8, 14):
        K = grid(N)
        U, dU = f(K)
        w, wi = w3_from(U, dU, U.conj().transpose(0, 2, 1))
        print(f"    N={N:2d}  max|UU^+-1|={np.abs(U@U.conj().transpose(0,2,1)-np.eye(12)).max():.1e}  W3={w:+.2e}")

# Hel is O-invariant but inversion-odd:
P_I = np.kron(perm(-np.eye(3)), np.eye(2))
print(f"  ||P_I Hel P_I^+ + Hel|| = {np.abs(P_I@Hel@P_I.T + Hel).max():.1e} (inversion flips helicity)")

print("E4: M = i d4 + d.sigma (strictly local, non-unitary), W3 via GL formula")
for N in (16, 24, 32, 40):
    K = grid(N)
    M, dM = E4(K)
    smin = np.linalg.svd(M, compute_uv=False).min()
    w, wi = w3_from(M, dM)
    print(f"  N={N:2d}  min singular value {smin:.3f}  W3={w:+.8f} (imag {wi:+.1e})")
print(f"time {time.time()-t0:.1f}s")
