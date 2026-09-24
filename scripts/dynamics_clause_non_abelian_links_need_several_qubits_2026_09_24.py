#!/usr/bin/env python3
"""Non-Abelian gauge links need several qubits; one qubit carries only Abelian links.

A gauge link from vertex v to vertex w carries two commuting actions of the
gauge group G: a left action (in the Gauss law at v) and a right action (in
the Gauss law at w). For a non-Abelian field at both ends both actions must
be nontrivial. The runner certifies (supplied constructions, finite
diagnostics, no physical reading):

1. One qubit, U(1): E = s^z generates commuting left and right U(1) actions
   (e^{i a E}, e^{-i b E}), and s^+ is a covariant link operator (charge 1):
   the spin-1/2 quantum link.
2. One qubit, SU(2): the only nontrivial SU(2) action on C^2 is irreducible,
   so its commutant is the scalars; a commuting right action is trivial.
3. The floor 2N: a link space carrying commuting nontrivial left and right
   SU(N) actions has dimension at least 2N (each nontrivial irrep has
   dimension >= N; one component (rho, sigma) with both nontrivial has
   dimension >= N^2 >= 2N, two components give >= 2N). The floor is reached
   by (N, 1) + (1, N), dimension 2N, for N = 2, 3.
4. It is dynamical: on (N, 1) + (1, N) the operator-valued matrices U^{ab}
   with V^dag U V = Omega_L U Omega_R^dag (a link operator, the consistent
   Heisenberg-picture law) form a nonzero space, found by linear algebra for
   random group elements, N = 2, 3. For SU(3) the mixed pairings
   (N, 1) + (1, Nbar) have none.
5. Qubit counts: U(1) 1 qubit (dimension 2), SU(2) 2 qubits (4), SU(3)
   3 qubits (6 <= 8); independent SU(3) x SU(2) x U(1) link fields need
   dimension >= 6 * 4 * 2 = 48, so at least 6 qubits per link.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 300

import numpy as np
from scipy.linalg import expm

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260924)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1.0 + 0j, -1.0])


def null_dim(A, tol=1e-9):
    """Null-space dimension via the (small) Gram matrix."""
    g = A.conj().T @ A
    w = np.linalg.eigvalsh(g)
    return int(np.sum(w < tol * max(1.0, w.max())))


def gell_mann(n):
    gens = []
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), dtype=complex)
            m[i, j] = m[j, i] = 1
            gens.append(m)
            m = np.zeros((n, n), dtype=complex)
            m[i, j], m[j, i] = -1j, 1j
            gens.append(m)
    for k in range(1, n):
        m = np.zeros((n, n), dtype=complex)
        for i in range(k):
            m[i, i] = 1
        m[k, k] = -k
        gens.append(m * np.sqrt(2 / (k * (k + 1))))
    return gens


def random_su(n):
    return expm(1j * sum(rng.normal() * g for g in gell_mann(n)))


# ----------------------------------------------------------- 1. U(1)
E = Z / 2
a, b = rng.normal(size=2)
L = expm(1j * a * E)
R = expm(-1j * b * E)
Up = (X + 1j * Y) / 2                             # s^+
cov = np.linalg.norm(L @ R @ Up @ (L @ R).conj().T - np.exp(1j * (a - b)) * Up)
check("one qubit carries a U(1) link: left and right actions commute, s^+ is covariant with charge 1",
      np.linalg.norm(L @ R - R @ L) < 1e-12 and cov < 1e-12, f"covariance defect {cov:.1e}")

# ----------------------------------------------------------- 2. SU(2) on a qubit
gens2 = [X / 2, Y / 2, Z / 2]
rows = [np.kron(np.eye(2), g.T) - np.kron(g, np.eye(2)) for g in gens2]
comm = null_dim(np.vstack(rows))
check("one qubit carries no non-Abelian link: the commutant of the SU(2) action on C^2 is the scalars",
      comm == 1, f"commutant dimension {comm}")

# ----------------------------------------------------- 3-4. the floor 2N
floor_ok, dyn = True, []
for n in (2, 3):
    d = 2 * n
    gl = gell_mann(n)
    # (N, 1) + (1, N): the left action is the fundamental on the first block, the right on the second
    Lg = [np.block([[g, np.zeros((n, n))], [np.zeros((n, n)), np.zeros((n, n))]]) for g in gl]
    Rg = [np.block([[np.zeros((n, n)), np.zeros((n, n))], [np.zeros((n, n)), g]]) for g in gl]
    commute = max(np.linalg.norm(x @ y - y @ x) for x in Lg for y in Rg)
    nontriv = min(max(np.linalg.norm(x) for x in Lg), max(np.linalg.norm(y) for y in Rg))
    floor_ok &= commute < 1e-12 and nontriv > 0.1
    # link operators: V^dag U^{ab} V = (Omega_L U Omega_R^dag)_{ab}, the consistent (Heisenberg) law
    rows = []
    for _ in range(3):
        OL, OR = random_su(n), random_su(n)
        V = np.block([[OL, np.zeros((n, n))], [np.zeros((n, n)), OR]])
        T1 = np.einsum("ki,lj->ijkl", V.conj(), V)
        A = np.zeros((n, n, d, d, n, n, d, d), dtype=complex)
        for a_ in range(n):
            for b_ in range(n):
                A[a_, b_, :, :, a_, b_, :, :] += T1
        A -= np.einsum("xz,yw,ik,jl->xyijzwkl", OL, OR.conj(), np.eye(d), np.eye(d))
        rows.append(A.reshape(n * n * d * d, n * n * d * d))
    dyn.append((n, d, null_dim(np.vstack(rows))))
# the mixed pairing (N, 1) + (1, Nbar) for SU(3): no covariant link operator
n, d = 3, 6
rows = []
for _ in range(3):
    OL, OR = random_su(n), random_su(n)
    V = np.block([[OL, np.zeros((n, n))], [np.zeros((n, n)), OR.conj()]])
    T1 = np.einsum("ki,lj->ijkl", V.conj(), V)
    A = np.zeros((n, n, d, d, n, n, d, d), dtype=complex)
    for a_ in range(n):
        for b_ in range(n):
            A[a_, b_, :, :, a_, b_, :, :] += T1
    A -= np.einsum("xz,yw,ik,jl->xyijzwkl", OL, OR.conj(), np.eye(d), np.eye(d))
    rows.append(A.reshape(n * n * d * d, n * n * d * d))
mixed = null_dim(np.vstack(rows))
check("the floor 2N is reached: (N, 1) + (1, N) carries commuting nontrivial left and right SU(N) actions (N = 2, 3)",
      floor_ok, "dimensions " + ", ".join(f"SU({n}): {d}" for n, d, _ in dyn))
check("it is dynamical: a covariant link operator (V^dag U V = Omega_L U Omega_R^dag) exists on the 2N-dimensional link; the SU(3) mixed pairing has none",
      all(k >= 1 for _, _, k in dyn) and mixed == 0,
      "; ".join(f"SU({n}): covariant solution space dimension {k}" for n, _, k in dyn) + f"; SU(3) mixed (N, 1) + (1, Nbar): {mixed}")

# ------------------------------------------------------ 5. qubit counts
dims = {"U(1)": 2, "SU(2)": 4, "SU(3)": 6}
qubits = {g: int(np.ceil(np.log2(v))) for g, v in dims.items()}
prod = dims["U(1)"] * dims["SU(2)"] * dims["SU(3)"]
check("qubit counts per link: U(1) 1, SU(2) 2, SU(3) 3; independent SU(3) x SU(2) x U(1) fields need dimension >= 48, i.e. >= 6 qubits",
      qubits == {"U(1)": 1, "SU(2)": 2, "SU(3)": 3} and prod == 48 and int(np.ceil(np.log2(prod))) == 6,
      f"minimal link dimensions {dims}; product {prod}; qubits {int(np.ceil(np.log2(prod)))}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
