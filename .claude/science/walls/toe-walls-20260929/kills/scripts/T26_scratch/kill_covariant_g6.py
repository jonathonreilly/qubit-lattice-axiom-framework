"""Kill check for T26: is there a translation-covariant (and cubic-covariant) copy of
su(3)+su(2)+u(1) (dim 12, tensor-product action on C^3 x C^2) inside End(C^8) on the taste cube?
Uses the attacker's helper definitions (read only copy of test_T26.py prefix)."""
import itertools, math, json
import numpy as np
exec(open('test_T26.py').read().split("# ------------- TEST A")[0])

# character basis psi_k(n) = (-1)^{k.n}/sqrt(8); T_mu psi_k = (-1)^{k_mu} psi_k  (repo: FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION, T_mu|n>=|n+e_mu mod 2>)
keys = list(itertools.product((0, 1), repeat=3))
def psi(k):
    return np.array([(-1) ** (sum(a * b for a, b in zip(k, n))) for n in keys], dtype=complex) / math.sqrt(8)
# sanity: X_mu psi_k = (-1)^{k_mu} psi_k
for k in keys:
    for m in range(3):
        assert np.allclose(X[m] @ psi(k), (-1) ** k[m] * psi(k))

A_set = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]     # V3 = hw=1 characters
B_set = [(0, 0, 0), (1, 1, 1)]                # C^2
xor = lambda a, b: tuple((x + y) % 2 for x, y in zip(a, b))
cols = [psi(xor(a, b)) for a in A_set for b in B_set]   # ordering: a major, b minor => C^3 (x) C^2
W6 = np.column_stack(cols)                    # 8x6 isometry
assert np.allclose(W6.conj().T @ W6, np.eye(6))

def gm(n):
    ms = []
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), dtype=complex); m[i, j] = m[j, i] = 1; ms.append(m)
            m = np.zeros((n, n), dtype=complex); m[i, j] = -1j; m[j, i] = 1j; ms.append(m)
    for k in range(1, n):
        m = np.zeros((n, n), dtype=complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k
        ms.append(m / math.sqrt(k * (k + 1) / 2))
    return ms
G3, G2 = gm(3), gm(2)
emb = lambda M6: W6 @ M6 @ W6.conj().T
g_su3_c = [1j * emb(np.kron(m / 2, np.eye(2))) for m in G3]
g_su2_c = [1j * emb(np.kron(np.eye(3), m / 2)) for m in G2]
g_u1_c = [1j * emb(np.eye(6))]
g12c = g_su3_c + g_su2_c + g_u1_c
print("dim of covariant candidate g6' (abstract su(3)+su(2)+u(1), tensor action on hw=1 (x) {000,111}):", close(g12c).dim)

Perm = list(map(swap_axes, (0, 0, 1), (1, 2, 2)))
def rot_generators():
    def perm_from_map(f):
        op = np.zeros((8, 8), dtype=complex)
        for x, i in idx.items():
            y = f(x); op[idx[tuple(y)], i] = 1
        return op
    return [perm_from_map(lambda x: (x[0], x[2], 1 - x[1])),
            perm_from_map(lambda x: (1 - x[2], x[1], x[0])),
            perm_from_map(lambda x: (x[1], 1 - x[0], x[2]))]
Rg = rot_generators()
res = {}
for name, gens in {"X_i translations": X, "X_i + all axis perms (B3)": X + Perm,
                   "X_i + proper cube rotations": X + Rg, "X_i + rotations + perms": X + Rg + Perm,
                   "Pauli <X_i,Z_i> (control: should break)": X + Z}.items():
    d = close(g12c, gens).dim
    print(f"  closure(g6', {name}) = {d}")
    res[name] = d

# attacker's graph-first g8 under the same groups, for the side-by-side
for name, gens in {"X_i translations": X, "X_i + rotations + perms": X + Rg + Perm}.items():
    print(f"  (attacker's graph-first g8) closure(g8, {name}) = {close(g8, gens).dim}")

# Z-reading: Hadamard-rotate everything so translations are diagonal Z_i in the basis where the cube corners are momentum corners
H1 = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
H3 = np.kron(np.kron(H1, H1), H1)
g12z = [H3 @ g @ H3.conj().T for g in g12c]
print("\nZ-reading (translations diagonal Z_i): Hadamard-rotated copy")
assert all(np.allclose(H3 @ X[m] @ H3.conj().T, Z[m]) for m in range(3))
res_z = {}
for name, gens in {"Z_i translations": Z, "Z_i + all axis perms": Z + Perm}.items():
    d = close(g12z, gens).dim
    print(f"  closure(g6'_Z, {name}) = {d}")
    res_z[name] = d

# is g6' irreducible on its C^6, and is the (8,3) still the only complement (same abstract structure)?
S = close(g12c)
print("\nabstract check: commutant of g6' restricted to C^6 = scalars? ->", end=" ")
ops6 = [W6.conj().T @ (-1j * g) @ W6 for g in g12c]
d6, _ = commutant_dim(ops6, n=6)
print(d6)

# what this does NOT do: is it selected? closure with ONE more covariant cross generator (a translation-normalised element of (8,3))
# choose a cross generator that is diagonal in the character basis (so all translations commute with it)
cross = 1j * emb(np.kron(np.diag([1, -1, 0]).astype(complex), np.diag([1, -1]).astype(complex)))
Sx = close(g12c + [cross], X + Perm)
print("g6' + one translation-invariant cross generator (diag lambda3 (x) sigma3), closed under X_i + perms: dim", Sx.dim, "(u(6) restricted = 36 would mean covariance does not separate g6' from u(6))")
res["cross_closure"] = Sx.dim
json.dump(dict(X_reading=res, Z_reading=res_z), open('kill_covariant_g6_results.json', 'w'), indent=1)
