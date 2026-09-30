"""Shared objects for the T20 attack: the proper cubic group O, the four soldering actions
(THE_SOLDERING_MENU_..._2026-09-22), SU(2) lifts. Pure numpy."""
import itertools
import numpy as np

SIG = [np.array([[0, 1], [1, 0]], complex),
       np.array([[0, -1j], [1j, 0]], complex),
       np.array([[1, 0], [0, -1]], complex)]
I2 = np.eye(2, dtype=complex)


def cubic_rotations():
    """24 signed permutation matrices of determinant +1 (integer 3x3)."""
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3):
                M[i, p[i]] = s[i]
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    assert len(out) == 24
    return out


O = cubic_rotations()


def perm_sign(M):
    """sign of the axis permutation underlying a signed permutation matrix."""
    A = np.abs(M)
    return int(round(np.linalg.det(A)))


def rho(kind, g):
    """Bloch-vector rotation (3x3 in SO(3)) of lattice rotation g under the given action."""
    if kind == "trivial":
        return np.eye(3)
    if kind == "sign":
        s = perm_sign(g)
        return np.diag([1.0, s, s])
    if kind == "axis":
        s = perm_sign(g)
        return s * np.abs(g).astype(float)
    if kind == "full":
        return g.astype(float)
    raise ValueError(kind)


KINDS = ["trivial", "sign", "axis", "full"]


def su2_of_rotation(R):
    """A unitary U in SU(2) with U (b.sigma) U^dag = (R b).sigma (one of the two lifts)."""
    R = np.asarray(R, float)
    assert abs(np.linalg.det(R) - 1) < 1e-9
    # rotation angle and axis
    tr = np.trace(R)
    c = np.clip((tr - 1) / 2, -1, 1)
    th = np.arccos(c)
    if th < 1e-9:
        return I2.copy()
    if abs(th - np.pi) < 1e-7:
        # axis from symmetric part: R = 2 n n^T - I
        S = (R + np.eye(3)) / 2
        i = np.argmax(np.diag(S))
        n = S[:, i] / np.sqrt(S[i, i])
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
    ns = sum(n[i] * SIG[i] for i in range(3))
    U = np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * ns
    # verify conjugation convention
    for b in np.eye(3):
        lhs = U @ sum(b[i] * SIG[i] for i in range(3)) @ U.conj().T
        rhs = sum((R @ b)[i] * SIG[i] for i in range(3))
        assert np.allclose(lhs, rhs, atol=1e-9), "lift convention"
    return U


def check_homs():
    """Each rho(kind, .) is a homomorphism O -> SO(3): all 576 pairs."""
    idx = {tuple(g.flatten()): i for i, g in enumerate(O)}
    for kind in KINDS:
        for a in O:
            for b in O:
                ab = a @ b
                assert idx[tuple(ab.flatten())] >= 0
                assert np.allclose(rho(kind, a) @ rho(kind, b), rho(kind, ab)), kind
                assert abs(np.linalg.det(rho(kind, a)) - 1) < 1e-12
    return True


if __name__ == "__main__":
    print("homs ok:", check_homs())
