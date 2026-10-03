"""Covariance tests of single-excitation 'content-set' walks on Z^3.

Conventions: T_v <-> exp(-i k.v); walk W(k) = sum_v A_v exp(-i k.v).
Soldered rotation R (24 proper cubic rotations) acts on the coin by the
spin-1/2 lift U_R:  U_R (r.sigma) U_R^dag = (R r).sigma.
Covariance  <=>  W(R k) = U_R W(k) U_R^dag  for all k.
"""
import itertools
import numpy as np

rng = np.random.default_rng(7)
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
SIG = [sx, sy, sz]


def rotations():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3), int)
            for i, p in enumerate(perm):
                R[i, p] = signs[i]
            if round(np.linalg.det(R)) == 1:
                Rs.append(R)
    return Rs


def su2_lift(R):
    R = R.astype(float)
    c = (np.trace(R) - 1) / 2
    th = np.arccos(np.clip(c, -1, 1))
    if abs(th) < 1e-12:
        return I2.copy()
    if abs(th - np.pi) < 1e-9:
        M = R + np.eye(3)
        j = np.argmax(np.linalg.norm(M, axis=0))
        n = M[:, j] / np.linalg.norm(M[:, j])
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
    U = np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * sum(n[a] * SIG[a] for a in range(3))
    # verify adjoint action
    for b in range(3):
        lhs = U @ SIG[b] @ U.conj().T
        rhs = sum(R[a, b] * SIG[a] for a in range(3))
        assert np.allclose(lhs, rhs, atol=1e-12)
    return U


RS = rotations()
US = [su2_lift(R) for R in RS]
assert len(RS) == 24


def P(a, s):
    return (I2 + s * SIG[a]) / 2


def W_sum(k):
    return sum(P(a, +1) * np.exp(-1j * k[a]) + P(a, -1) * np.exp(1j * k[a]) for a in range(3))


def Wa(a, ka):
    return np.cos(ka) * I2 - 1j * np.sin(ka) * SIG[a]


def W_prod(k, order=(2, 1, 0)):
    M = I2
    for a in order:  # leftmost factor first in the product
        M = M @ Wa(a, k[a])
    return M


def H_weyl(k):
    return sum(np.sin(k[a]) * SIG[a] for a in range(3))


def cov_defect(Wf, R, U, ks):
    return max(np.linalg.norm(Wf(R @ k) - U @ Wf(k) @ U.conj().T) for k in ks)


def unitarity_defect(Wf, ks):
    return max(np.linalg.norm(Wf(k).conj().T @ Wf(k) - I2) for k in ks)


def describe(R):
    # rotation angle and axis label
    c = (np.trace(R) - 1) / 2
    th = int(round(np.degrees(np.arccos(np.clip(c, -1, 1)))))
    w, v = np.linalg.eig(R.astype(float))
    ax = np.real(v[:, np.argmin(abs(w - 1))])
    ax = ax / np.max(abs(ax))
    return th, tuple(int(round(x)) for x in ax)


if __name__ == "__main__":
    ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(40)]
    tol = 1e-10
    # 1) sum candidate S
    cs = [cov_defect(W_sum, R, U, ks) for R, U in zip(RS, US)]
    print("S = sum_a (P_a^+ T_a + P_a^- T_a^-1): covariant under", sum(c < tol for c in cs),
          "/24 rotations; max unitarity defect ||S^dag S - 1|| =", round(unitarity_defect(W_sum, ks), 3))
    # S^dag S at special points
    for kk in [(0, 0, 0), (np.pi / 2,) * 3]:
        M = W_sum(np.array(kk))
        print("   S^dag S at k =", tuple(round(x, 3) for x in kk), "=", np.round(np.real(np.diag(M.conj().T @ M)), 6))
    # 2) ordered products, all 6 orders
    for order in itertools.permutations(range(3)):
        f = lambda k, o=order: W_prod(k, o)
        cs = [cov_defect(f, R, U, ks) for R, U in zip(RS, US)]
        good = [describe(R) for R, c in zip(RS, cs) if c < tol]
        print("product order", "".join("xyz"[a] for a in order), ": unitary defect",
              f"{unitarity_defect(f, ks):.1e}", "; symmetric under", len(good), "rotations:", good)
    # 3) lattice Weyl Hamiltonian (continuous-time generator)
    cs = [max(np.linalg.norm(H_weyl(R @ k) - U @ H_weyl(k) @ U.conj().T) for k in ks) for R, U in zip(RS, US)]
    print("H = sum_a sin(k_a) sigma_a: covariant under", sum(c < tol for c in cs), "/24")
    chis = []
    for K in itertools.product([0, np.pi], repeat=3):
        J = np.diag([np.cos(K[a]) for a in range(3)])  # H ~ sum_a J_aa q_a sigma_a
        chis.append(int(np.sign(np.linalg.det(J))))
    print("   Weyl nodes at the 8 TRIM, chiralities:", chis, " sum =", sum(chis))
    # inversion: k -> -k, coin untouched (automorphism convention, forced by Schur)
    print("   inversion maps H to -H (opposite hand):",
          np.allclose(H_weyl(-ks[0]), -H_weyl(ks[0])))
