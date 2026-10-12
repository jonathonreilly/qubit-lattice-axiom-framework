"""R6-2 check 4: on finite-dimensional sites, weak gauge invariance of a local Hamiltonian adds nothing.

Lemma A (elementary): if H = sum_x h_x (uniformly local) commutes with every local Gauss operator G_y,
and the G_y generate a compact group (always true for finite-dimensional sites), then
H = sum_x avg(h_x), where avg is the Haar average over the local gauge group; each avg(h_x) is local and
individually gauge invariant.  So the non-invariant parts of a weakly invariant density sum to zero
identically: they do not contribute to H.

Check: Z2 gauge theory with matter on a ring of L sites (qubits ordered s0,l0,s1,l1,...),
G_x = X(l_{x-1}) Z(s_x) X(l_x).  Translation-invariant density h on (s_x, l_x, s_{x+1}, l_{x+1}).
Solve for all h with [sum_x T^x h, G_y] = 0 (weak), compare with strongly invariant h, and verify
sum_x T^x avg(h) == sum_x T^x h for every weak solution.
"""
import itertools
import numpy as np
from scipy.linalg import null_space as _ns

def null_space(A):
    Gm = A.T @ A
    w, V = np.linalg.eigh(Gm)
    return V[:, w < 1e-9 * max(1.0, w.max())]


L = 4
n = 2 * L
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.])
P1 = {"I": I2, "X": X, "Y": Y, "Z": Z}

def op(ops):  # ops: dict qubit -> 2x2
    M = np.array([[1.0 + 0j]])
    for q in range(n):
        M = np.kron(M, ops.get(q, I2))
    return M

def G(x):
    return op({(2 * x - 1) % n: X, (2 * x) % n: Z, (2 * x + 1) % n: X})

Gs = [G(x) for x in range(L)]
assert all(np.allclose(a @ b, b @ a) for a in Gs for b in Gs)
supp = [0, 1, 2, 3]  # s0, l0, s1, l1
paulis = list(itertools.product("IXYZ", repeat=len(supp)))[1:]  # drop identity

def density(word, x):
    return op({(supp[i] + 2 * x) % n: P1[c] for i, c in enumerate(word) if c != "I"})

def H_of(word):
    return sum(density(word, x) for x in range(L))

# weak: [H(c), G_0] = 0 for all y (translation invariance -> y=0 suffices, check all anyway)
cols_weak, cols_strong = [], []
for w in paulis:
    Hw = H_of(w)
    cols_weak.append(np.concatenate([(Hw @ g - g @ Hw).ravel() for g in Gs]))
    hw = density(w, 0)
    cols_strong.append(np.concatenate([(hw @ g - g @ hw).ravel() for g in Gs]))
Aw = np.array(cols_weak).T; As = np.array(cols_strong).T
Nw = null_space(np.vstack([Aw.real, Aw.imag])); Ns = null_space(np.vstack([As.real, As.imag]))
# densities whose translation sum vanishes identically
Az = np.array([H_of(w).ravel() for w in paulis]).T
Nz = null_space(np.vstack([Az.real, Az.imag]))
print(f"L={L}: Pauli densities on 4 consecutive qubits: {len(paulis)}")
print(f"  weakly invariant (sum commutes with all G): dim {Nw.shape[1]}")
print(f"  strongly invariant (density commutes with all G): dim {Ns.shape[1]}")
print(f"  densities whose translation sum is identically zero: dim {Nz.shape[1]}")
span = np.hstack([Ns, Nz])
print(f"  dim(strong + zero-sum) = {np.linalg.matrix_rank(span, tol=1e-9)}  (equals weak dim => weak adds nothing)")

def avg(M, x):
    # Haar average over the Z2^L gauge group restricted to generators overlapping the support
    gens = [Gs[y % L] for y in (x - 1, x, x + 1, x + 2)]
    gens = [g for i, g in enumerate(gens) if not any(np.allclose(g, h) for h in gens[:i])]
    out = np.zeros_like(M)
    for bits in itertools.product([0, 1], repeat=len(gens)):
        U = np.eye(2 ** n)
        for b, g in zip(bits, gens):
            if b: U = U @ g
        out += U @ M @ U
    return out / 2 ** len(gens)

worst = 0.0
for j in range(Nw.shape[1]):
    c = Nw[:, j]
    H = sum(ci * H_of(w) for ci, w in zip(c, paulis) if abs(ci) > 1e-12)
    Havg = sum(avg(sum(ci * density(w, x) for ci, w in zip(c, paulis) if abs(ci) > 1e-12), x) for x in range(L))
    worst = max(worst, np.abs(H - Havg).max())
    local_inv = max(np.abs(avg(sum(ci * density(w, 0) for ci, w in zip(c, paulis) if abs(ci) > 1e-12), 0) @ g
                           - g @ avg(sum(ci * density(w, 0) for ci, w in zip(c, paulis) if abs(ci) > 1e-12), 0)).max() for g in Gs)
print(f"  max |sum_x h_x - sum_x avg(h_x)| over all weak solutions = {worst:.2e}")
print(f"  averaged density commutes with every G (last solution): residual {local_inv:.2e}")
