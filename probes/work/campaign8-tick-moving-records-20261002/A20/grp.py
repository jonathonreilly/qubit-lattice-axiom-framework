"""Soldered proper cubic group O acting on Z^3 sites and on one-qubit Paulis.

Conventions
- A rotation R is a 3x3 signed permutation matrix with det +1 (24 of them).
- Site action: v -> R v.
- Label action (soldered, adjoint of spin-1/2): sigma^a -> sum_b R[b,a] sigma^b,
  i.e. sigma^a -> eps * sigma^{pi(a)} with R e_a = eps e_{pi(a)}.
- Mod-2 Pauli labels as symplectic bit pairs (bx, bz): X=(1,0), Y=(1,1), Z=(0,1).
"""
import itertools
import numpy as np

AX = {0: (1, 0), 1: (1, 1), 2: (0, 1)}   # sigma^x, sigma^y, sigma^z -> (bx, bz)
BITS2AX = {v: k for k, v in AX.items()}


def rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for i in range(3):
                M[perm[i], i] = signs[i]          # column i = image of e_i
            if round(np.linalg.det(M)) == 1:
                mats.append(M)
    assert len(mats) == 24
    return mats


def label_map(R):
    """Return (pi, eps): sigma^a -> eps[a] sigma^{pi[a]}."""
    pi, eps = {}, {}
    for a in range(3):
        col = R[:, a]
        b = int(np.nonzero(col)[0][0])
        pi[a], eps[a] = b, int(col[b])
    return pi, eps


def label_bits_matrix(R):
    """2x2 F2 matrix acting on (bx,bz) column vectors, induced mod 2 by R."""
    pi, _ = label_map(R)
    g = np.zeros((2, 2), dtype=int)
    # image of X=(1,0) is AX[pi[0]]; image of Z=(0,1) is AX[pi[2]]
    g[:, 0] = AX[pi[0]]
    g[:, 1] = AX[pi[2]]
    # consistency: Y=(1,1) -> AX[pi[1]]
    assert tuple((g @ np.array([1, 1])) % 2) == AX[pi[1]]
    return g


def find(mats, pred):
    return [M for M in mats if pred(M)]


def named():
    mats = rotations()
    e = np.eye(3, dtype=int)
    def is_(M, cols):
        return np.array_equal(M, np.array(cols).T)
    C4x = [M for M in mats if is_(M, [e[0], e[2], -e[1]])][0]
    C4z = [M for M in mats if is_(M, [e[1], -e[0], e[2]])][0]
    C2y = [M for M in mats if is_(M, [-e[0], e[1], -e[2]])][0]
    C3 = [M for M in mats if is_(M, [e[1], e[2], e[0]])][0]   # x->y->z->x
    return dict(C4x=C4x, C4z=C4z, C2y=C2y, C3=C3, all=mats)


if __name__ == "__main__":
    N = named()
    for k in ["C4x", "C4z", "C2y", "C3"]:
        print(k, label_map(N[k]), label_bits_matrix(N[k]).tolist())
    # stabilizer of the x-axis line (D4_x)
    D4x = [M for M in N["all"] if abs(M[0, 0]) == 1]
    print("|D4_x| =", len(D4x))
    # GL(2,F2) image size
    imgs = {tuple(label_bits_matrix(M).flatten()) for M in N["all"]}
    print("label image size", len(imgs))
