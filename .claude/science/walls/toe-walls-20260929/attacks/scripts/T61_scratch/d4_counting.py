#!/usr/bin/env python3
"""T61 D4: how many independent mass-type (and two-derivative) quadratic terms does each symmetry allow?

Count = dim of the space of symmetric bilinear forms Q on a field multiplet V that are invariant under the
symmetry group (finite: by its generators; continuous: by its Lie algebra generators).
Multiplets:  scalar (n=1),  vector A_mu,  symmetric tensor h_mu nu,  and d_lambda h_mu nu (two-derivative terms).
Groups: Z^3 -> O (24 proper cubic rotations, the axiom's group), O_h (with reflections); continuum SO(3), O(3).
        Z^4 -> hyperoctahedral B4 (384, with reflections); continuum O(4).
"""
import numpy as np, itertools

def sym_basis(n):
    B = []
    for i in range(n):
        for j in range(i, n):
            E = np.zeros((n, n)); E[i, j] = E[j, i] = 1.0 if i == j else 1 / np.sqrt(2)
            B.append(E)
    return B  # orthonormal basis of symmetric matrices

def rep_scalar(R): return np.eye(1)
def rep_vector(R): return R
def rep_sym2(R, n):
    B = sym_basis(n)
    M = np.zeros((len(B), len(B)))
    for b, E in enumerate(B):
        Rt = R @ E @ R.T
        for a, F in enumerate(B):
            M[a, b] = np.sum(F * Rt)
    return M
def rep_dh(R, n):
    return np.kron(R, rep_sym2(R, n))

def rep_dgen_sym2(X, n):
    """Lie-algebra action of X on sym2 (X antisymmetric)."""
    B = sym_basis(n)
    M = np.zeros((len(B), len(B)))
    for b, E in enumerate(B):
        Rt = X @ E + E @ X.T
        for a, F in enumerate(B):
            M[a, b] = np.sum(F * Rt)
    return M

def count_invariant_forms(rho_list, dim, algebra_list=()):
    # Q symmetric dim x dim, parametrised by upper triangle
    idx = [(i, j) for i in range(dim) for j in range(i, dim)]
    P = len(idx)
    rows = []
    def vec_from_Q(Q): return np.array([Q[i, j] for (i, j) in idx])
    basisQ = []
    for (i, j) in idx:
        Q = np.zeros((dim, dim)); Q[i, j] = Q[j, i] = 1.0
        basisQ.append(Q)
    blocks = []
    for R in rho_list:
        blocks.append(np.stack([vec_from_Q(R.T @ Q @ R - Q) for Q in basisQ], 1))
    for X in algebra_list:  # rho(X)^T Q + Q rho(X) = 0
        blocks.append(np.stack([vec_from_Q(X.T @ Q + Q @ X) for Q in basisQ], 1))
    A = np.concatenate(blocks, 0)
    s = np.linalg.svd(A, compute_uv=False)
    tol = 1e-9 * max(1.0, s[0])
    return P - int((s > tol).sum())

def cubic_generators(n, proper_only):
    gens = []
    # 90 degree rotation in plane (0,1); cyclic permutation; (for improper) sign flip
    R01 = np.eye(n); R01[[0, 1], [0, 1]] = 0; R01[0, 1] = -1; R01[1, 0] = 1
    gens.append(R01)
    if n >= 3:
        # 120 degree rotation about (1,1,1) in first 3 coordinates: cyclic permutation of axes (proper)
        C = np.eye(n); C[:3, :3] = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        gens.append(C)
    if n == 4:
        # proper hyperoctahedral: also a 4-cycle composed with a sign (det +1): use permutation (0 1 2 3) with det -1 -> combine with sign flip
        P4 = np.zeros((4, 4));
        for i in range(4): P4[(i + 1) % 4, i] = 1
        if np.linalg.det(P4) < 0: P4[:, 0] *= -1
        gens.append(P4)
    if not proper_only:
        F = np.eye(n); F[0, 0] = -1; gens.append(F)
        if n == 4:
            P4 = np.zeros((4, 4))
            for i in range(4): P4[(i + 1) % 4, i] = 1
            gens.append(P4)
    return gens

def so_generators(n):
    Xs = []
    for i in range(n):
        for j in range(i + 1, n):
            X = np.zeros((n, n)); X[i, j] = -1; X[j, i] = 1; Xs.append(X)
    return Xs

def run(n, label, groups):
    out = {}
    for name, (gens, algebra) in groups.items():
        row = []
        for mult, rep, gen_rep in (("scalar", rep_scalar, None), ("vector", rep_vector, None),
                                    ("h_ij", lambda R: rep_sym2(R, n), lambda X: rep_dgen_sym2(X, n)),
                                    ("d h", lambda R: rep_dh(R, n), None)):
            dimV = {"scalar": 1, "vector": n, "h_ij": n * (n + 1) // 2, "d h": n * n * (n + 1) // 2}[mult]
            rho = [rep(g) for g in gens]
            alg = []
            for X in algebra:
                if mult == "scalar": alg.append(np.zeros((1, 1)))
                elif mult == "vector": alg.append(X)
                elif mult == "h_ij": alg.append(rep_dgen_sym2(X, n))
                else: alg.append(np.kron(X, np.eye(n * (n + 1) // 2)) + np.kron(np.eye(n), rep_dgen_sym2(X, n)))
            row.append((mult, count_invariant_forms(rho, dimV, alg)))
        out[name] = row
        print(f"{label:6s} {name:34s} " + "  ".join(f"{m}={c}" for m, c in row))
    return out

if __name__ == "__main__":
    print("Number of independent invariant quadratic forms (mass-type terms; 'd h' = two-derivative kinetic-type terms):")
    n = 3
    run(3, "Z^3", {
        "O (24 proper cubic rotations)": (cubic_generators(3, True), []),
        "O_h (48, with reflections)": (cubic_generators(3, False), []),
        "SO(3) continuum": ([], so_generators(3)),
        "O(3) continuum": ([np.diag([-1.0, 1, 1])], so_generators(3)),
    })
    run(4, "Z^4", {
        "B4 proper (192)": (cubic_generators(4, True), []),
        "B4 full (384)": (cubic_generators(4, False), []),
        "SO(4) continuum": ([], so_generators(4)),
        "O(4) continuum": ([np.diag([-1.0, 1, 1, 1])], so_generators(4)),
    })

def closure_size(gens, cap=2000):
    key = lambda M: tuple(np.round(M).astype(int).flatten())
    I = np.eye(gens[0].shape[0]); seen = {key(I): I}; frontier = [I]
    while frontier and len(seen) < cap:
        new = []
        for A in frontier:
            for g in gens:
                B = g @ A
                k = key(B)
                if k not in seen:
                    seen[k] = B; new.append(B)
        frontier = new
    return len(seen)

if __name__ == "__main__":
    print("group orders from generators: O:", closure_size(cubic_generators(3, True)), " O_h:", closure_size(cubic_generators(3, False)),
          " B4 proper:", closure_size(cubic_generators(4, True)), " B4 full:", closure_size(cubic_generators(4, False)))
