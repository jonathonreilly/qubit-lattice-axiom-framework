"""O1 check 2: (i) integer Lorentz group O(1,3;Z) has only eta as invariant symmetric 2-tensor and no invariant
vector, but (ii) its orbits of lattice vectors are infinite, so a translation-covariant kernel that is exactly
invariant under it is constant on infinite orbits and not summable. (iii) Lemma F check: any finite subgroup of
O(1,3) has a PSD invariant 2-tensor S != lambda*eta (numerical illustration on a conjugated finite group)."""
import itertools, numpy as np, sympy as sp
eta = np.diag([1, -1, -1, -1])
def signed_perms3():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1, -1], repeat=3):
            M = np.eye(4, dtype=int)
            M[1:, 1:] = 0
            for i in range(3): M[1 + p[i], 1 + i] = s[i]
            out.append(M)
    return out
r = np.array([1, 1, 1, 1])
def refl(r):
    rr = r @ eta @ r          # = -2
    return (np.eye(4, dtype=int) - (2 * np.outer(r, r @ eta)) // rr).astype(int)
s_r = refl(r)
gens = signed_perms3() + [s_r]
for g in gens: assert np.array_equal(g.T @ eta @ g, eta)
print("s_r =\n", s_r, "\n  preserves eta, integer:", np.array_equal(s_r.T @ eta @ s_r, eta))
# invariant vectors and symmetric 2-tensors (fixed by all generators)
A = sp.Matrix(np.vstack([g - np.eye(4, dtype=int) for g in gens]))
print("invariant vectors: dim =", 4 - A.rank())
rows = []
for g in gens:
    # action on symmetric matrices X -> g X g^T, vectorized
    M = np.kron(g, g) - np.eye(16, dtype=int)
    rows.append(M)
Asym = sp.Matrix(np.vstack(rows))
# restrict to symmetric X: add constraints X_ij - X_ji = 0
symc = []
for i in range(4):
    for j in range(i + 1, 4):
        v = np.zeros(16, dtype=int); v[4 * i + j] = 1; v[4 * j + i] = -1; symc.append(v)
Afull = sp.Matrix(np.vstack([np.vstack(rows), np.array(symc)]))
ns = Afull.nullspace()
print("invariant symmetric 2-tensors: dim =", len(ns), "; basis (as 4x4):", [list(np.array(n).reshape(4, 4).astype(int).tolist()) for n in ns])
# orbit growth of e0 (timelike) and e1 (spacelike) under words of length <= L
def orbit(v, L):
    seen = {tuple(v)}; frontier = [np.array(v)]
    for _ in range(L):
        new = []
        for x in frontier:
            for g in gens:
                y = g @ x
                if tuple(y) not in seen:
                    seen.add(tuple(y)); new.append(y)
        frontier = new
    return seen
for L in (2, 4, 6, 8):
    o0 = orbit([1, 0, 0, 0], L); o1 = orbit([0, 1, 0, 0], L)
    print(f"word length <= {L}: |orbit(e0)| = {len(o0):5d}  max t = {max(abs(x[0]) for x in o0):4d};  |orbit(e1)| = {len(o1):5d}")
print("e.g. points on t^2-x^2-y^2-z^2=1 reached:", sorted(orbit([1,0,0,0], 4), key=lambda x: x[0])[-3:])
# (iii) Lemma F illustration: a finite group F inside O(1,3): conjugate O_h x {+-1 time} by a boost B; S = sum g u u^T g^T
def boost(beta):
    gm = 1 / np.sqrt(1 - beta ** 2); B = np.eye(4); B[0, 0] = B[1, 1] = gm; B[0, 1] = B[1, 0] = gm * beta; return B
B = boost(0.6)
F = [B @ g @ np.linalg.inv(B) for g in signed_perms3() for g in (g, np.diag([-1,1,1,1]) @ g)]
for g in F: assert np.allclose(g.T @ eta @ g, eta)
u = np.array([1.0, 0.0, 0.0, 0.0])
S = sum(np.outer(g @ u, g @ u) for g in F) / len(F)
ev = np.linalg.eigvalsh(S)
print("Lemma F: S eigenvalues (PSD, rank>=1):", np.round(ev, 6))
lam = np.trace(S @ eta) / 4
print("  ||S - lam*eta|| =", round(float(np.linalg.norm(S - lam * eta)), 6), "(nonzero => invariant speed tensor besides eta)")
print("  invariance check max|gSg^T - S| =", max(np.abs(g @ S @ g.T - S).max() for g in F))
