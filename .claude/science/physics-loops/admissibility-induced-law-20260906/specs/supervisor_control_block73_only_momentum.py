#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 73 (floating point; numerical linear algebra; machinery disjoint from the exact runner's symbolic solve).

W1  THE COMMUTANT. All translation-invariant operators of reach <= R with the qubit as coin: M(k) = sum_{|m|_1 <= R} A_m exp(i m.k), A_m complex
    2 x 2. The condition [M(k), H(k)] = 0 at many random wave vectors is a linear system for the A_m; its null space is counted by singular values
    and compared with the count of a(k) + c(k) H(k): (monomials of reach <= R) + (monomials of reach <= R - 1).
W2  OWN WAVE NUMBER. The 32 conditions (value and gradient at the eight zeros) on the real monomials of reach <= 1 and <= 2, as a numerical
    matrix: least-squares residual (reach 1: not solvable), rank and nullity (reach 2), and the distance of (1/2) sin 2k_1 and of the six functions
    sin k_b sin k_c from the solution set.
W3  COVARIANCE. The solution set of W2 at reach two, averaged over the stabiliser of e_1 in the 24 proper rotations and antisymmetrised under
    the rotations that reverse e_1 (a projector onto symbols that turn as the first component of a vector): what is left.
"""
import itertools
import numpy as np

rng = np.random.default_rng(73)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def exps(reach):
    return [m for m in itertools.product(range(-reach, reach + 1), repeat=3) if sum(abs(v) for v in m) <= reach]


def w1():
    print("[W1] dimension of the space of translation-invariant operators of reach <= R commuting with the walk (complex dimension):")
    for reach in (1, 2, 3):
        ms = exps(reach); basis_mats = [np.eye(2, dtype=complex)] + sig
        rows = []
        for _ in range(200):                                   # 800 equations, more than the unknowns at every R used
            k = rng.uniform(-np.pi, np.pi, size=3); H = sum(np.sin(k[a])*sig[a] for a in range(3))
            cols = []
            for m in ms:
                ph = np.exp(1j*np.dot(m, k))
                for Bm in basis_mats:
                    cols.append((ph*(Bm@H - H@Bm)).ravel())
            rows.append(np.array(cols).T)
        A = np.vstack(rows); sv = np.linalg.svd(A, compute_uv=False)
        null = int((sv < 1e-9*sv[0]).sum()) + (A.shape[1] - len(sv))
        print(f"     R = {reach}: {A.shape[0]} equations, unknowns {A.shape[1]}, null space {null}; count of a + c H: {len(exps(reach))} + {len(exps(reach - 1))} = {len(exps(reach)) + len(exps(reach - 1))}; smallest kept / largest dropped singular value: {sv[len(sv) - null - 1]/sv[0]:.1e} / {sv[len(sv) - null]/sv[0] if null else 0:.1e}")


def real_basis(reach):
    out = [(None, None)]
    for m in exps(reach):
        if m > (0, 0, 0):
            out += [(m, "cos"), (m, "sin")]
    return out


def value_and_gradient(fn, k):
    m, kind = fn
    if m is None:
        return 1.0, np.zeros(3)
    arg = np.dot(m, k)
    return (np.cos(arg), -np.sin(arg)*np.array(m)) if kind == "cos" else (np.sin(arg), np.cos(arg)*np.array(m))


def conditions(reach):
    basis = real_basis(reach); A = []; b = []
    for n in itertools.product((0, 1), repeat=3):
        k = np.pi*np.array(n)
        vg = [value_and_gradient(fn, k) for fn in basis]
        A.append([v for v, g in vg]); b.append(0.0)
        for c in range(3):
            A.append([g[c] for v, g in vg]); b.append(1.0 if c == 0 else 0.0)
    return basis, np.array(A), np.array(b)


def coefficients(basis, terms):
    """terms: dict {(m, kind): coefficient}"""
    return np.array([terms.get(fn, 0.0) for fn in basis])


def w2_w3():
    print("\n[W2] the 32 conditions for 'own wave number along axis 1':")
    basis1, A1, b1 = conditions(1)
    x1, res1, rk1, _ = np.linalg.lstsq(A1, b1, rcond=None)
    print(f"     reach <= 1: {len(basis1)} monomials, rank {rk1}; least-squares residual |Ax - b| = {np.linalg.norm(A1@x1 - b1):.4f} (not solvable)")
    basis2, A2, b2 = conditions(2)
    x2, res2, rk2, _ = np.linalg.lstsq(A2, b2, rcond=None)
    print(f"     reach <= 2: {len(basis2)} monomials, rank {rk2}, nullity {len(basis2) - rk2}; residual {np.linalg.norm(A2@x2 - b2):.1e} (solvable)")
    two_step = coefficients(basis2, {((2, 0, 0), "sin"): 0.5})
    print(f"     (1/2) sin 2k_1 satisfies the conditions: |A x - b| = {np.linalg.norm(A2@two_step - b2):.1e}")
    # sin k_b sin k_c = (1/2)[cos(k_b - k_c) - cos(k_b + k_c)];  sin^2 k_b = (1/2)[1 - cos 2k_b]
    def prod(b, c):
        if b == c:
            m = [0, 0, 0]; m[b] = 2
            return coefficients(basis2, {(None, None): 0.5, (tuple(m), "cos"): -0.5})
        mp = [0, 0, 0]; mp[b] = 1; mp[c] = 1; mm = [0, 0, 0]; mm[b] = 1; mm[c] = -1
        return coefficients(basis2, {(tuple(mm), "cos"): 0.5, (tuple(mp), "cos"): -0.5})
    six = [prod(b, c) for b in range(3) for c in range(b, 3)]
    print(f"     the six functions sin k_b sin k_c satisfy the homogeneous conditions: largest |A x| = {max(np.linalg.norm(A2@v) for v in six):.1e}; their rank: {np.linalg.matrix_rank(np.array(six))}")

    print("\n[W3] covariance, by sampling: a symbol f(k) that is the first component of a vector obeys f(Rk) = sum_i R_1i f_i(k); using only rotations with R e_1 = +-e_1: f(Rk) = +-f(k)")
    rots = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for i in range(3): R[i, perm[i]] = signs[i]
            if np.isclose(np.linalg.det(R), 1): rots.append(R)
    keep = [(R, R[0, 0]) for R in rots if abs(R[0, 0]) == 1]
    print(f"     proper rotations: {len(rots)}; those with R e_1 = +-e_1: {len(keep)}")
    ks = rng.uniform(-np.pi, np.pi, size=(40, 3))
    def evaluate(vec, k):
        return sum(c*value_and_gradient(fn, k)[0] for c, fn in zip(vec, basis2))
    rows = []
    for v in six:
        rows.append([evaluate(v, R@k) - sgn*evaluate(v, k) for R, sgn in keep for k in ks])
    rows = np.array(rows)                                  # a combination sum e_i v_i is covariant iff e . rows = 0
    sv = np.linalg.svd(rows, compute_uv=False)
    print(f"     the six functions under these conditions: singular values {np.array2string(sv, precision=3)}: none vanishes, so no combination of them survives")
    print(f"     (1/2) sin 2k_1 under the same conditions: largest violation {max(abs(evaluate(two_step, R@k) - sgn*evaluate(two_step, k)) for R, sgn in keep for k in ks):.1e}")


if __name__ == "__main__":
    w1()
    w2_w3()
