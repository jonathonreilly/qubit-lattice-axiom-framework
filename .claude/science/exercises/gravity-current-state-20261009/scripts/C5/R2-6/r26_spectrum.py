"""R2-6 (a): Snyder coordinate spectra, covariance, and joint eigenvectors.

Snyder 1947: momentum space = de Sitter dS_4 = SO(4,1)/SO(3,1).
x_mu = a * J_{mu 4} (coset generators), Lorentz M_{mu nu} = J_{mu nu}.
Spatial x_i generate rotations in the compact (i,4) planes; t = x_0 generates
a boost in the (0,4) plane.

Checks:
 1. so(4) = su(2)+su(2): x_i/a = A_i - B_i, L_i = A_i + B_i satisfy
    [x_1/a, x_2/a] = i L_3 and [L_i, x_j] = i eps_ijk x_k.  Spectrum of x_1/a in
    (jA,jB) irreps: integers if jA+jB integer, half-integers otherwise.
 2. Joint eigenvectors of (x_1,x_2,x_3): only in the SO(4)-trivial (0,0)
    component (eigenvalue 0): the observer's origin.
 3. 5D defining rep of so(4,1): generator n^mu J_{mu4} is elliptic
    (exp(2 pi X) = 1) for every spacelike unit n, including boosted ones,
    hyperbolic for timelike n.  So every inertial observer's spatial
    coordinate has spectrum in a*Z (single-valued reps) or a*(Z+1/2).
"""
import numpy as np
from scipy.linalg import expm, null_space

np.set_printoptions(precision=6, suppress=True)


def spin(j):
    d = int(round(2 * j + 1))
    m = np.array([j - k for k in range(d)])
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((d, d), complex)
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    Jm = Jp.conj().T
    Jx = (Jp + Jm) / 2
    Jy = (Jp - Jm) / (2j)
    return [Jx, Jy, Jz]


def comm(A, B):
    return A @ B - B @ A


print("== 1. so(4) realisation x_i/a = A_i - B_i, L_i = A_i + B_i ==")
for (jA, jB) in [(0, 0), (0.5, 0.5), (1, 1), (2, 2), (0.5, 0), (1, 0.5), (1.5, 1), (2, 1)]:
    A = spin(jA)
    B = spin(jB)
    IA = np.eye(len(A[0]))
    IB = np.eye(len(B[0]))
    Af = [np.kron(Ai, IB) for Ai in A]
    Bf = [np.kron(IA, Bi) for Bi in B]
    X = [Af[i] - Bf[i] for i in range(3)]
    L = [Af[i] + Bf[i] for i in range(3)]
    r1 = np.linalg.norm(comm(X[0], X[1]) - 1j * L[2])
    r2 = np.linalg.norm(comm(L[0], X[1]) - 1j * X[2])
    ev = np.sort(np.linalg.eigvalsh(X[0]))
    frac = np.unique(np.round(np.mod(ev, 1.0), 9))
    # joint eigenvectors: need [x_i,x_j] psi = 0 -> L psi = 0; then x psi = lambda psi
    Lstack = np.vstack(L)
    K = null_space(Lstack)
    joint = []
    if K.shape[1] > 0:
        for i in range(3):
            joint.append(np.linalg.norm(X[i] @ K))
    print(f"(jA,jB)=({jA},{jB}) dim={X[0].shape[0]:2d}  [x1,x2]-iL3={r1:.1e} [L1,x2]-ix3={r2:.1e} "
          f"spec(x1/a)={np.round(ev, 6)}  frac parts={frac}  "
          f"dim ker(L)={K.shape[1]}  |x_i on ker L|={np.round(joint, 6) if joint else '-'}")

print()
print("== 2. 5D defining rep of so(4,1), metric G = diag(-1,1,1,1,1) ==")
G = np.diag([-1.0, 1, 1, 1, 1])


def J(A, B):
    """(J_AB)^C_D = delta^C_A G_BD - delta^C_B G_AD (preserves G)."""
    M = np.zeros((5, 5))
    for C in range(5):
        for D in range(5):
            M[C, D] = (C == A) * G[B, D] - (C == B) * G[A, D]
    return M


Jmu4 = [J(mu, 4) for mu in range(4)]
for M in Jmu4:
    assert np.allclose(M.T @ G + G @ M, 0)


def coord_gen(n):
    return sum(n[mu] * Jmu4[mu] for mu in range(4))


for eta in [0.0, 0.7, 2.5, 6.0]:
    n_sp = np.array([np.sinh(eta), np.cosh(eta), 0, 0])  # boosted x_1 direction (spacelike unit)
    n_tm = np.array([np.cosh(eta), np.sinh(eta), 0, 0])  # boosted time direction (timelike unit)
    Xs = coord_gen(n_sp)
    Xt = coord_gen(n_tm)
    evs = np.linalg.eigvals(Xs)
    evt = np.linalg.eigvals(Xt)
    per = np.linalg.norm(expm(2 * np.pi * Xs) - np.eye(5))
    pert = np.linalg.norm(expm(2 * np.pi * Xt) - np.eye(5))
    print(f"eta={eta:4.1f}: spacelike n: eig={np.round(np.sort_complex(evs), 6)} |exp(2pi X)-1|={per:.1e} | "
          f"timelike n: eig={np.round(np.sort_complex(evt), 6)} |exp(2pi X)-1|={pert:.3e}")

# conjugacy: boosted x_1 generator = Lambda J_14 Lambda^-1 with Lambda in SO(3,1)
eta = 1.3
Lam = expm(eta * J(0, 1))
assert np.allclose(Lam.T @ G @ Lam, G) and np.allclose(Lam[:, 4], [0, 0, 0, 0, 1])
lhs = Lam @ Jmu4[1] @ np.linalg.inv(Lam)
n = Lam[:4, 1].copy()  # image of e_1 (contravariant components)
rhs = coord_gen(n)
print(f"Lambda J_14 Lambda^-1 == (Lambda e_1)^mu J_mu4 : residual {np.linalg.norm(lhs - rhs):.1e}; "
      f"n = {np.round(n, 6)}, n.n = {n @ G[:4, :4] @ n:.6f}")

# high-precision recheck of exp(2 pi X) for the strongly boosted spacelike direction
import mpmath as mp
mp.mp.dps = 60
for eta in [2.5, 6.0]:
    n_sp = [mp.sinh(eta), mp.cosh(eta), 0, 0]
    Xs = mp.matrix(5, 5)
    for mu in range(4):
        for C in range(5):
            for D in range(5):
                Xs[C, D] += n_sp[mu] * float(Jmu4[mu][C, D])
    E = mp.expm(2 * mp.pi * Xs)
    res = mp.mnorm(E - mp.eye(5), 1)
    print(f"[mpmath dps=60] eta={eta}: |exp(2 pi X_spacelike) - 1| = {mp.nstr(res, 5)} (float64 residual above is round-off)")
