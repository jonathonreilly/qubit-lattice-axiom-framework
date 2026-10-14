"""F3 shared Dirac-algebra helpers (Hamiltonian form H = gamma0 D; F1/validate2 conventions).
Euclidean hermitian gammas (f1_validate2.py:19-20): g0 = s1 x 1, g_j = s2 x s_j.  F1's D = i g.c + M  ->  H = g0 D = alpha.c + beta M,
alpha_j = i g0 g_j, beta = g0.  Spin Sigma_j = -(i/2) eps_jkl alpha_k alpha_l.
Symmetries of the undressed root law H(k) (checked numerically in f3_sym.py):
  cubic  : H(Rk) = S_R H(k) S_R^dag ;   P : H(-k) = beta H(k) beta ;
  T      : U_T H(k)^* U_T^dag = H(-k) ;  C : U_C H(k)^* U_C^dag = -H(-k).
A dressing H -> V H V^dag, V = exp(i eps G) is symmetric iff (proved in the report, sec. 2):
  cubic: G(Rk) = S_R G(k) S_R^dag ;  P: beta G(-k) beta = G(k) ;  T: -U_T G(-k)^* U_T^dag = G(k) ;  C: -U_C G(-k)^* U_C^dag = G(k).
"""
import numpy as np
from scipy.linalg import expm

s0 = np.eye(2, dtype=complex); s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
g0 = np.kron(s1, s0); gs = [np.kron(s2, s1), np.kron(s2, s2), np.kron(s2, s3)]
I4 = np.eye(4, dtype=complex)
beta = g0
alpha = [1j*g0 @ g for g in gs]
eps3 = np.zeros((3, 3, 3))
for (a, b, c) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
    eps3[a, b, c] = 1; eps3[a, c, b] = -1
Sigma = [sum(-0.5j*eps3[j, k, l]*alpha[k] @ alpha[l] for k in range(3) for l in range(3)) for j in range(3)]
g5 = g0 @ gs[0] @ gs[1] @ gs[2]


def herm_basis():
    """16 hermitian 4x4 basis matrices with names (Hamiltonian-form hermitian)."""
    B = [('1', I4), ('beta', beta), ('g5', g5), ('i beta g5', 1j*beta @ g5)]
    for j, n in enumerate('xyz'):
        B += [('alpha_' + n, alpha[j]), ('Sigma_' + n, Sigma[j]), ('beta Sigma_' + n, beta @ Sigma[j]),
              ('i beta alpha_' + n, 1j*beta @ alpha[j])]
    for nm, m in B:
        assert np.allclose(m, m.conj().T), nm
    return B


def rot90(axis):
    """3x3 rotation by +90 deg about axis (k -> R k)."""
    R = np.eye(3); i, j = [(1, 2), (2, 0), (0, 1)][axis]
    R[i, i] = 0; R[j, j] = 0; R[j, i] = 1; R[i, j] = -1
    return R


def spin90(axis):
    """spinor S_R with S alpha_j S^dag = sum_l R_lj alpha_l for R = rot90(axis) (sign fixed by test)."""
    R = rot90(axis)
    for sg in (+1, -1):
        S = expm(-1j*sg*(np.pi/4)*Sigma[axis])
        if all(np.allclose(S @ alpha[j] @ S.conj().T, sum(R[l, j]*alpha[l] for l in range(3))) for j in range(3)):
            return S
    raise RuntimeError('no spin rep')


def find_antiunitary(sign_alpha, sign_beta):
    """unitary U with U alpha_j^* U^dag = sign_alpha alpha_j, U beta^* U^dag = sign_beta beta (search over Pauli products)."""
    paulis = [s0, s1, s2, s3]
    for a in range(4):
        for b in range(4):
            U = np.kron(paulis[a], paulis[b])
            if all(np.allclose(U @ alpha[j].conj() @ U.conj().T, sign_alpha*alpha[j]) for j in range(3)) and \
                    np.allclose(U @ beta.conj() @ U.conj().T, sign_beta*beta):
                return U
    raise RuntimeError('none')


U_T = find_antiunitary(-1, +1)     # T: alpha odd, beta even (k -> -k)
U_C = find_antiunitary(+1, -1)     # C: U H^* U^dag = -H(-k): alpha_j^* -> +alpha_j, beta^* -> -beta


def H_of(c, M):
    """H = alpha.c + beta M for arrays c (3, ...), M (...) -> (..., 4, 4)."""
    out = np.multiply.outer(M, beta)
    for j in range(3):
        out = out + np.multiply.outer(c[j], alpha[j])
    return out


def comps(H):
    """(c_x, c_y, c_z, M) of a Dirac-form H (..., 4, 4): c_j = tr(alpha_j H)/4, M = tr(beta H)/4; plus the norm of the remainder."""
    c = [np.real(np.einsum('ab,...ba->...', alpha[j], H))/4 for j in range(3)]
    M = np.real(np.einsum('ab,...ba->...', beta, H))/4
    rem = H - H_of(c, M)
    return c, M, np.sqrt(np.sum(np.abs(rem)**2, axis=(-2, -1)))
