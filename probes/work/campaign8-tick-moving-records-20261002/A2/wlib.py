"""Small library: 3D winding W3, Weyl-node finder, cubic rotations + spin-1/2 lifts.

Conventions
  U(k) = sum_v A_v exp(i k.v)            (step operator in momentum space)
  W3   = (1/24 pi^2) Int_{T^3} Tr[(U^-1 dU)^3] = (1/8 pi^2) Int d^3k Tr(A_x [A_y, A_z]),
         A_j = U^-1 d_j U.  On an N^3 uniform grid: W3 = pi * mean(Tr(A_x[A_y,A_z])).
         For a strictly local unitary the integrand is a trig polynomial, so the grid
         mean is the exact constant Fourier coefficient once N > (max frequency).
  Node chirality (2x2, SU(2)-valued): U = u0 - i b.sigma, b_a = (i/2) Tr(sigma_a U).
         Near a node U(k0) = u0 * 1 (u0 = +-1), U ~ e^{-i eps} e^{-i h.sigma}; chi := sign det(dh/dk).
         => chi = u0 * sign det(db/dk).
"""
import itertools
import numpy as np

s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = np.array([sx, sy, sz])


def grid(N):
    k1 = 2 * np.pi * np.arange(N) / N
    K = np.stack(np.meshgrid(k1, k1, k1, indexing="ij"), -1).reshape(-1, 3)
    return K


def w3_from(U, dU, Uinv=None):
    """U: (M,n,n); dU: (3,M,n,n). Returns (W3 real part, imag part)."""
    if Uinv is None:
        Uinv = np.linalg.inv(U)
    A = [Uinv @ dU[j] for j in range(3)]
    comm = A[1] @ A[2] - A[2] @ A[1]
    f = np.einsum("mij,mji->m", A[0], comm)
    val = np.pi * f.mean()
    return val.real, val.imag


def proper_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for i, p in enumerate(perm):
                R[i, p] = signs[i]
            if round(np.linalg.det(R)) == 1:
                out.append(R)
    return out  # 24 matrices


def spin_half(R):
    """SU(2) lift D with D sigma_a D^dag = sum_b R[b,a] sigma_b (proper R)."""
    # quaternion from rotation matrix (Shepperd)
    m = R
    tr = np.trace(m)
    if tr > 0:
        S = np.sqrt(tr + 1.0) * 2
        w = 0.25 * S
        x = (m[2, 1] - m[1, 2]) / S
        y = (m[0, 2] - m[2, 0]) / S
        z = (m[1, 0] - m[0, 1]) / S
    elif m[0, 0] > m[1, 1] and m[0, 0] > m[2, 2]:
        S = np.sqrt(1.0 + m[0, 0] - m[1, 1] - m[2, 2]) * 2
        w = (m[2, 1] - m[1, 2]) / S
        x = 0.25 * S
        y = (m[0, 1] + m[1, 0]) / S
        z = (m[0, 2] + m[2, 0]) / S
    elif m[1, 1] > m[2, 2]:
        S = np.sqrt(1.0 + m[1, 1] - m[0, 0] - m[2, 2]) * 2
        w = (m[0, 2] - m[2, 0]) / S
        x = (m[0, 1] + m[1, 0]) / S
        y = 0.25 * S
        z = (m[1, 2] + m[2, 1]) / S
    else:
        S = np.sqrt(1.0 + m[2, 2] - m[0, 0] - m[1, 1]) * 2
        w = (m[1, 0] - m[0, 1]) / S
        x = (m[0, 2] + m[2, 0]) / S
        y = (m[1, 2] + m[2, 1]) / S
        z = 0.25 * S
    D = w * s0 - 1j * (x * sx + y * sy + z * sz)
    # verify; if convention flipped, use conjugate quaternion
    ok = all(np.allclose(D @ SIG[a] @ D.conj().T, sum(R[b, a] * SIG[b] for b in range(3))) for a in range(3))
    if not ok:
        D = w * s0 + 1j * (x * sx + y * sy + z * sz)
        ok = all(np.allclose(D @ SIG[a] @ D.conj().T, sum(R[b, a] * SIG[b] for b in range(3))) for a in range(3))
    assert ok
    return D


def find_nodes_su2(Ufun, N=24, tol=1e-11, thresh=0.6):
    """Zeros of b(k) for SU(2)-valued U; returns list of (k0, u0, chi)."""
    K = grid(N) + 1e-3  # small offset avoids exact symmetric starting points
    U, dU = Ufun(K)
    b = np.einsum("aij,mji->ma", SIG, U).imag * (-1) * 0.5  # (i/2)Tr = -0.5*Im? fixed below
    # (i/2) Tr(s_a U): Tr is purely imaginary for SU(2): Tr = -2i b  => b = (i/2) Tr
    tr = np.einsum("aij,mji->ma", SIG, U)
    b = (0.5j * tr).real
    sel = np.linalg.norm(b, axis=1) < thresh
    k = K[sel].copy()
    for _ in range(60):
        U, dU = Ufun(k)
        tr = np.einsum("aij,mji->ma", SIG, U)
        b = (0.5j * tr).real
        J = np.stack([(0.5j * np.einsum("aij,mji->ma", SIG, dU[j])).real for j in range(3)], -1)  # (m,a,j)
        try:
            step = np.linalg.solve(J, b[..., None])[..., 0]
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(J.reshape(-1, 3), b.reshape(-1), rcond=None)[0]
        step = np.clip(step, -0.3, 0.3)
        k = k - step
    U, dU = Ufun(k)
    tr = np.einsum("aij,mji->ma", SIG, U)
    b = (0.5j * tr).real
    good = np.linalg.norm(b, axis=1) < tol
    k = np.mod(k[good], 2 * np.pi)
    # dedupe
    roots = []
    for kk in k:
        if not any(np.linalg.norm(np.angle(np.exp(1j * (kk - r))) ) < 1e-6 for r in roots):
            roots.append(kk)
    out = []
    for r in roots:
        U, dU = Ufun(r[None, :])
        u0 = np.trace(U[0]).real / 2
        J = np.stack([(0.5j * np.einsum("aij,mji->ma", SIG, dU[j])).real for j in range(3)], -1)[0]
        chi = int(np.sign(u0) * np.sign(np.linalg.det(J)))
        out.append((r, int(np.sign(u0)), chi, np.linalg.det(J)))
    return out
