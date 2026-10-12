"""Common tools for R15-3: proper cubic group O, its irreps, Sym^2 action, TT subspaces."""
import itertools
import numpy as np

def proper_cubic_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3))
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if round(np.linalg.det(M)) == 1:
                mats.append(M)
    assert len(mats) == 24
    return mats

# basis of Sym^2(R^3): orthonormal (Frobenius) basis
def sym2_basis():
    B = []
    for i in range(3):
        E = np.zeros((3, 3)); E[i, i] = 1; B.append(E)
    for (i, j) in [(1, 2), (2, 0), (0, 1)]:
        E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1 / np.sqrt(2); B.append(E)
    return B
SYM2 = sym2_basis()

def sym2_rep(R):
    """6x6 matrix of h -> R h R^T in the orthonormal SYM2 basis."""
    M = np.zeros((6, 6))
    for b, Eb in enumerate(SYM2):
        img = R @ Eb @ R.T
        for a, Ea in enumerate(SYM2):
            M[a, b] = np.sum(Ea * img)
    return M

def tt_projector(khat):
    k = np.asarray(khat, float); k = k / np.linalg.norm(k)
    P = np.eye(3) - np.outer(k, k)
    # TT projector on symmetric tensors: P_ia P_jb sym - 1/2 P_ij P_ab
    T = np.zeros((6, 6))
    for b, Eb in enumerate(SYM2):
        img = P @ Eb @ P - 0.5 * P * np.trace(P @ Eb)
        for a, Ea in enumerate(SYM2):
            T[a, b] = np.sum(Ea * img)
    return T

def stabilizer_element(G, axis, order):
    """Return a group element R with R axis = axis and R of the given order (rotation)."""
    ax = np.asarray(axis, float)
    for R in G:
        if np.allclose(R @ ax, ax):
            # order
            M = np.eye(3); n = 0
            for n in range(1, 7):
                M = M @ R
                if np.allclose(M, np.eye(3)):
                    break
            if n == order:
                return R
    raise ValueError("not found")

# Irreps of O as explicit real matrices, built from natural reps
def irreps(G):
    """Return dict name -> list of matrices (same order as G)."""
    T1 = [R.copy() for R in G]
    S2 = [sym2_rep(R) for R in G]
    # E: diagonal traceless part, T2: off-diagonal part, A1: trace
    diag_tl = np.array([[1, -1, 0], [1, 1, -2]], float)
    diag_tl[0] /= np.sqrt(2); diag_tl[1] /= np.sqrt(6)
    UE = np.zeros((2, 6)); UE[:, :3] = diag_tl
    UT2 = np.zeros((3, 6)); UT2[:, 3:] = np.eye(3)
    E = [UE @ M @ UE.T for M in S2]
    T2 = [UT2 @ M @ UT2.T for M in S2]
    A1 = [np.eye(1) for R in G]
    # A2: character -1 on C4 and C2', +1 on C3 and C2 (=C4^2): = det of the permutation part
    A2 = []
    for R in G:
        P = np.abs(R)
        # sign of permutation
        perm = [int(np.argmax(P[i])) for i in range(3)]
        s = np.linalg.det(P)
        A2.append(np.array([[round(s)]], float))
    return {"A1": A1, "A2": A2, "E": E, "T1": T1, "T2": T2}

def check_irreps(G, irr):
    """Check homomorphism and irreducibility (sum |chi|^2 = |G|)."""
    idx = {}
    for i, R in enumerate(G):
        idx[tuple(np.round(R).astype(int).ravel())] = i
    out = {}
    for name, mats in irr.items():
        hom = True
        for i, Ri in enumerate(G):
            for j, Rj in enumerate(G):
                k = idx[tuple(np.round(Ri @ Rj).astype(int).ravel())]
                if not np.allclose(mats[i] @ mats[j], mats[k]):
                    hom = False
        chi = np.array([np.trace(M) for M in mats])
        out[name] = (hom, round(float(np.sum(chi ** 2)) / len(G), 6))
    return out
