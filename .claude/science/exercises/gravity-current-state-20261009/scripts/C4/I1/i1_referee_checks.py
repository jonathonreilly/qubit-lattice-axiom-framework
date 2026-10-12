"""Independent checks for Campaign C4 / lane RI / probe I1.

This deliberately does not import the worker scripts.  It checks the algebraic
formula with a separately assembled random Bloch Hamiltonian, tests the
unfixed diagonal improvement, verifies the finite-difference telescoping sum,
and computes the determinant windings used in Theorem 3.
"""

import numpy as np


rng = np.random.default_rng(20261011)
N = 3
R = 2
raw = {
    r: rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    for r in range(0, R + 1)
}
raw[0] = raw[0] + raw[0].conj().T + np.diag([-9.0, 0.0, 9.0])
coeff = {0: raw[0]}
for r in range(1, R + 1):
    coeff[r] = raw[r]
    coeff[-r] = raw[r].conj().T
S = np.diag([0.13, 0.41, 0.82])


def h(k):
    return sum(m * np.exp(1j * r * k) for r, m in coeff.items())


def dh(k):
    return sum(1j * r * m * np.exp(1j * r * k) for r, m in coeff.items())


def covariant(a, da):
    return da - 1j * (S @ a - a @ S)


def improved(k, diagonal=False, wrong_sign=False):
    H = h(k)
    E, V = np.linalg.eigh(H)
    DH = covariant(H, dh(k))
    DHb = V.conj().T @ DH @ V
    ab = np.zeros((N, N), dtype=complex)
    sign = -1 if wrong_sign else 1
    for i in range(N):
        for j in range(N):
            if i != j:
                ab[i, j] = sign * 1j * (E[i] + E[j]) * DHb[i, j] / (
                    2 * (E[i] - E[j])
                )
    if diagonal:
        ab += np.diag([0.2 * np.sin(k), -0.3 * np.cos(2 * k), 0.1 * np.sin(3 * k)])
    a = V @ ab @ V.conj().T
    P = 0.5 * (DH @ H + H @ DH) + 1j * (H @ a - a @ H)
    return H, E, V, a, P


grid = np.linspace(-np.pi, np.pi, 65, endpoint=False)
comm_correct = 0.0
comm_wrong = 0.0
diag_p_change = 0.0
q_change = 0.0
q_offdiag = 0.0
q_diag_rel = 0.0
eps = 2e-5
eig_eps = 2e-4
for k in grid:
    H, E, V, a, P = improved(k)
    _, _, _, a_diag, P_diag = improved(k, diagonal=True)
    _, _, _, _, P_wrong = improved(k, wrong_sign=True)
    comm_correct = max(comm_correct, np.max(np.abs(H @ P - P @ H)))
    comm_wrong = max(comm_wrong, np.max(np.abs(H @ P_wrong - P_wrong @ H)))
    diag_p_change = max(diag_p_change, np.max(np.abs(P_diag - P)))

    P_plus = improved(k + eps)[4]
    P_minus = improved(k - eps)[4]
    DP = covariant(P, (P_plus - P_minus) / (2 * eps))
    Q = 0.5 * (DP @ H + H @ DP) - 1j * (a @ P - P @ a)

    P_plus_diag = improved(k + eps, diagonal=True)[4]
    P_minus_diag = improved(k - eps, diagonal=True)[4]
    DP_diag = covariant(P_diag, (P_plus_diag - P_minus_diag) / (2 * eps))
    Q_diag_improvement = 0.5 * (DP_diag @ H + H @ DP_diag) - 1j * (
        a_diag @ P_diag - P_diag @ a_diag
    )
    q_change = max(q_change, np.max(np.abs(Q_diag_improvement - Q)))

    Qb = V.conj().T @ Q @ V
    q_offdiag = max(q_offdiag, np.max(np.abs(Qb - np.diag(np.diag(Qb)))))
    Ep = np.linalg.eigvalsh(h(k + eig_eps))
    Em = np.linalg.eigvalsh(h(k - eig_eps))
    u_second = (Ep**2 - 2 * E**2 + Em**2) / (2 * eig_eps**2)
    denom = max(1.0, np.max(np.abs(E * u_second)))
    q_diag_rel = max(
        q_diag_rel,
        np.max(np.abs(np.real(np.diag(Qb)) - E * u_second)) / denom,
    )

print("independent multiband algebra")
print(f"  max commutator, correct off-diagonal improvement: {comm_correct:.3e}")
print(f"  max commutator, sign-mutated improvement:         {comm_wrong:.3e}")
print(f"  max change in P from arbitrary diagonal a:        {diag_p_change:.3e}")
print(f"  max change in Q from arbitrary diagonal a:        {q_change:.3e}")
print(f"  max off-diagonal Q in band frame:                 {q_offdiag:.3e}")
print(f"  max relative diagonal error Q vs E u'':           {q_diag_rel:.3e}")

# A cyclic second-difference has exactly zero total (up to roundoff), even if
# individual sorted bands have cusps at crossings.
L = 4096
k = np.linspace(-np.pi, np.pi, L, endpoint=False)
crossing_energies = np.stack([2 + np.sin(k), 2 - np.sin(k)], axis=1)
crossing_energies.sort(axis=1)
u = crossing_energies**2 / 2
d2u = np.roll(u, -1, axis=0) - 2 * u + np.roll(u, 1, axis=0)
print("crossing-band cyclic Hessian sums:", d2u.sum(axis=0))
print("trace cyclic Hessian sum:", d2u.sum())

# Determinant winding: a continuous periodic Hermitian logarithm gives zero,
# while lattice translation contributes -N.  Thus V=U^{-1}T must carry -N.
Nw = 4
k_closed = np.linspace(-np.pi, np.pi, 20001)
det_t = np.exp(-1j * Nw * k_closed)
tr_pi = 0.7 * np.sin(k_closed) + 0.2 * np.cos(2 * k_closed)
det_u = np.exp(-1j * tr_pi)
det_v = np.conj(det_u) * det_t


def winding(z):
    return (np.unwrap(np.angle(z))[-1] - np.unwrap(np.angle(z))[0]) / (2 * np.pi)


print("determinant windings")
print(f"  wind(det T) = {winding(det_t):.9f}")
print(f"  wind(det U) = {winding(det_u):.9f}")
print(f"  wind(det V) = {winding(det_v):.9f}")

# At a degenerate point h=E I, conservation cannot fix any within-block a.
E0 = 2.0
H0 = E0 * np.eye(2)
a0 = np.array([[0.2, 0.3 + 0.4j], [0.3 - 0.4j, -0.1]])
P0 = 1j * (H0 @ a0 - a0 @ H0)
print("degenerate-block nonuniqueness |[h, i[h,a]]|:", np.max(np.abs(H0 @ P0 - P0 @ H0)))
