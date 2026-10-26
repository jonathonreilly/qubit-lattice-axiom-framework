#!/usr/bin/env python3
"""Selected 3+1 matrix diagnostics for the corrected Route-4 review note.
Companion: docs/A3_R4_REVIEW_CONFIRMED_NOTE_2026-05-08_r4hr.md.
SU(3) is supplied on a selected three-dimensional block of C^4. Its
stabilizer is S(U(3) x U(1)) = (SU(3) x U(1))/Z_3, not a direct product.
Full SU(3) invariance gives scalarity on the defining three; C3 invariance
only gives equal coordinate diagonals. H=C+C† is a non-scalar control.
Ordinary two-qubit tensoring does not yield Cl_6(C); Clifford factorization
uses the graded tensor product. No physical carrier selection, generation
identification, campaign exhaustion or no-escape theorem is established.
Computed finite matrix checks are numerical diagnostics, not exact proofs.
Historical documentary assertions are omitted from current PASS accounting.
Original recovery: d5a1f49aea605481b7d31c6b96534be3cb4d0be7.
Self-contained: numpy only."""
from __future__ import annotations

import sys
import numpy as np

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/A3_R4_REVIEW_CONFIRMED_NOTE_2026-05-08_r4hr.md', 'docs/A3_ROUTE4_SPIN6_CHAIN_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_r4.md')

np.set_printoptions(precision=6, linewidth=140, suppress=True)

PASS = 0
FAIL = 0
BPASS = 0
BFAIL = 0

def check(name, cond, detail="", kind="NUMERICAL"):
    global PASS, FAIL, BPASS, BFAIL
    tag = "PASS" if cond else "FAIL"
    if kind == "NUMERICAL":
        if cond:
            PASS += 1
        else:
            FAIL += 1
    else:
        if cond:
            BPASS += 1
        else:
            BFAIL += 1
    k = f" [{kind}]" if kind != "NUMERICAL" else ""
    msg = f"  [{tag}]{k} {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond

def is_close(A, B, tol=1e-9):
    return np.linalg.norm(np.asarray(A) - np.asarray(B)) < tol

def commutator(A, B):
    return A @ B - B @ A

def antic(A, B):
    return A @ B + B @ A

def is_anti_hermitian(A, tol=1e-9):
    return np.linalg.norm(A + A.conj().T) < tol

def is_hermitian(A, tol=1e-9):
    return np.linalg.norm(A - A.conj().T) < tol

def section(t):
    print("\n" + "=" * 88)
    print(t)
    print("=" * 88)

I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)
I4 = np.eye(4, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)

def gellmann():
    L = []
    L.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex))
    L.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex))
    L.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex))
    L.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex))
    L.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex))
    L.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex))
    L.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex))
    L.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3))
    return L

def embed3in4(M3):
    M4 = np.zeros((4, 4), dtype=complex)
    M4[:3, :3] = M3
    return M4

lambdas = gellmann()
T_su3_4 = [embed3in4(L) / 2 for L in lambdas]
T_15 = np.diag([1, 1, 1, -3]).astype(complex) / (2 * np.sqrt(6))
U_BL = T_15 * (2 * np.sqrt(6) / 3)

section("HR4.1  Are there OTHER maximal subgroups of SU(4) for the supplied SU(3) on V_3?")

Omega = np.array([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]],
                 dtype=complex)
ok_sp = abs(np.linalg.det(Omega) - 1) < 1e-12 and \
        np.allclose(Omega.T, -Omega)
check("HR4.1.1 Sp(2)~Sp(4) symplectic form Omega has det=1, antisym",
      ok_sp,
      "Sp(2) preserves a non-degenerate antisymmetric form on C^4")

def in_sp4(M):
    return np.allclose(M.T @ Omega + Omega @ M, np.zeros_like(M))

incompatible = 0
for i, t in enumerate(T_su3_4):
    if not in_sp4(t):
        incompatible += 1
check("HR4.1.2 At least one SU(3) generator is NOT in sp(4)",
      incompatible >= 1,
      f"{incompatible}/8 SU(3) generators violate Sp(4) condition")

T_2L_X = np.zeros((4, 4), dtype=complex)
T_2L_X[0, 1] = 1; T_2L_X[1, 0] = 1
T_2L_Y = np.zeros((4, 4), dtype=complex)
T_2L_Y[0, 1] = -1j; T_2L_Y[1, 0] = 1j
T_2L_Z = np.diag([1, -1, 0, 0]).astype(complex)

dim_su2_su2 = 6
dim_su2_su2_u1 = 7
dim_su3 = 8
check("HR4.1.4 SU(3) (dim 8) cannot be subgroup of SU(2)xSU(2)xU(1) (dim 7)",
      dim_su3 > dim_su2_su2_u1,
      f"{dim_su3} > {dim_su2_su2_u1}: dimensional impossibility")

check("HR4.1.5 SU(3) cannot be subgroup of SO(4)~SU(2)xSU(2) (dim 6)",
      dim_su3 > 6,
      "dimensional impossibility")

section("HR4.2  Could there be a DIFFERENT branching with non-uniform U(1) charge?")

def centralizer_in_su4(generators):
    """Find the centralizer of `generators` in su(4).  Returns the
    null space of the map M -> [generators, M] in the space of 4x4
    Hermitian traceless matrices."""

    basis = list(T_su3_4)
    for i in range(3):

        Ms = np.zeros((4, 4), dtype=complex)
        Ms[i, 3] = 1; Ms[3, i] = 1; Ms /= 2
        Ma = np.zeros((4, 4), dtype=complex)
        Ma[i, 3] = -1j; Ma[3, i] = 1j; Ma /= 2
        basis.append(Ms)
        basis.append(Ma)
    basis.append(T_15)
    assert len(basis) == 15

    rows = []
    for g in generators:
        for a in range(15):
            comm = commutator(g, basis[a])

            v = comm.flatten()
            rows.append(np.concatenate([v.real, v.imag]))

    n_gen = len(generators)
    C = np.zeros((n_gen * 32, 15))
    for gi, g in enumerate(generators):
        for ai, b in enumerate(basis):
            comm = commutator(g, b)
            v = np.concatenate([comm.flatten().real, comm.flatten().imag])
            C[gi * 32:(gi + 1) * 32, ai] = v

    _, s, vh = np.linalg.svd(C)
    null_dim = int(np.sum(s < 1e-7))
    null_basis = vh[-null_dim:] if null_dim > 0 else np.zeros((0, 15))
    return null_dim, null_basis, basis

null_dim_su3, null_basis_su3, basis15 = centralizer_in_su4(T_su3_4)
check("HR4.2.1 Centralizer of SU(3) in su(4) is 1-dimensional",
      null_dim_su3 == 1,
      f"dim = {null_dim_su3}: U(1) generator is unique up to scale")

if null_dim_su3 == 1:
    coefs = null_basis_su3[0]
    M_central = sum(coefs[i] * basis15[i] for i in range(15))

    diag_M = np.diag(M_central).real
    diag_T15 = np.diag(T_15).real

    if abs(diag_T15[0]) > 1e-9:
        ratio = diag_M[0] / diag_T15[0]
        is_prop = np.allclose(diag_M, ratio * diag_T15)
    else:
        is_prop = False
    check("HR4.2.2 Centralizer generator is proportional to T_15 (= U(1)_(B-L))",
          is_prop,
          "U(1)_(B-L) is the unique centralizer up to scale")

proj_quark = np.eye(4)[:, :3]
U_BL_on_quark = proj_quark.T @ U_BL @ proj_quark
diag_uBL = np.diag(U_BL_on_quark).real
check("HR4.2.3 U(1)_(B-L) acts as constant +1/3 on 3 corner subspace",
      np.allclose(diag_uBL, [1/3, 1/3, 1/3]) and \
      np.linalg.norm(U_BL_on_quark - (1/3) * I3) < 1e-12,
      f"diag = {diag_uBL} (Schur's lemma: scalar on irrep)")

section("HR4.3  Could Z_3 triality of Spin(8) be inherited at Spin(6) level?")

spin6_irreps_low = {"4": 4, "4-bar": 4, "6": 6, "10": 10, "10-bar": 10,
                    "15 (adjoint)": 15, "20'": 20}
spin8_irreps_low = {"8_v": 8, "8_s": 8, "8_c": 8, "28 (adjoint)": 28}

spin6_4dim = [k for k, v in spin6_irreps_low.items() if v == 4]
check("HR4.3.1 Spin(6) has only 2 distinct 4-dim irreps (4 and 4-bar)",
      len(spin6_4dim) == 2,
      f"4-dim irreps: {spin6_4dim} -- Z_2 symmetry, not Z_3")

spin8_8dim = [k for k, v in spin8_irreps_low.items() if v == 8]
check("HR4.3.2 Spin(8) has 3 distinct 8-dim irreps (8_v, 8_s, 8_c)",
      len(spin8_8dim) == 3,
      f"8-dim irreps: {spin8_8dim} -- S_3 triality")

section("HR4.4  C_3[111] as Weyl element of SU(3) — conjugacy class")

C_3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
det_C3 = np.linalg.det(C_3)
trace_C3 = np.trace(C_3)
check("HR4.4.1 C_3[111] is in SU(3): det = 1",
      abs(det_C3 - 1) < 1e-12,
      f"det = {det_C3}")
check("HR4.4.2 C_3[111] has trace 0 (sum of eigenvalues 1+omega+omega-bar)",
      abs(trace_C3) < 1e-12,
      f"trace = {trace_C3}")

eigs_C3 = np.sort(np.linalg.eigvals(C_3))
omega = np.exp(2j * np.pi / 3)
expected = np.sort([1, omega, omega.conj()])
check("HR4.4.3 C_3[111] eigenvalues = {1, omega, omega-bar}",
      np.allclose(eigs_C3, expected, atol=1e-9),
      "")

H_test = np.diag([1, 2, -3]).astype(complex)
H_conj = C_3 @ H_test @ C_3.conj().T
expected_conj = np.diag([-3, 1, 2]).astype(complex)
ok_weyl = is_close(H_conj, expected_conj)
check("HR4.4.4 C_3 acts on SU(3) Cartan as cyclic permutation (= S_3 Coxeter)",
      ok_weyl,
      "C_3 in (123)-conjugacy class of W(SU(3))=S_3")

omega_I = omega * I3

ok_center_C3 = all(is_close(commutator(omega_I, l/2), np.zeros((3, 3)))
                   for l in lambdas)
check("HR4.4.5 C_3 center element omega*I commutes with all SU(3); "
      "acts as scalar on corners; cannot distinguish",
      ok_center_C3,
      "Non-Weyl C_3 is in center of SU(3) -> uniform on corners")

section("HR4.5  Branching multiplicities — multi-irrep alternatives?")

np.random.seed(1234)
M_random = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)

vec_basis = []
for i in range(3):
    for j in range(3):
        E = np.zeros((3, 3), dtype=complex)
        E[i, j] = 1
        vec_basis.append(E)
n_basis = len(vec_basis)

constraint_rows = []
for L in lambdas:
    T = L / 2
    M_to_comm = np.zeros((9, 9), dtype=complex)
    for col, E in enumerate(vec_basis):
        comm = T @ E - E @ T
        M_to_comm[:, col] = comm.flatten()
    constraint_rows.append(M_to_comm)

C_full = np.vstack(constraint_rows)

_, s_full, vh_full = np.linalg.svd(C_full)
nullity = int(np.sum(s_full < 1e-9))
check("HR4.5.1 SU(3) action on V_3 (fundamental rep) has 1-dim centralizer",
      nullity == 1,
      f"nullity = {nullity}; centralizer = scalar multiples of I")

if nullity >= 1:
    null_vec = vh_full[-1]
    M_null = null_vec.reshape(3, 3)

    M_null_norm = M_null / M_null[0, 0] if abs(M_null[0, 0]) > 1e-9 else M_null
    is_scalar = is_close(M_null_norm, I3, tol=1e-7)
    check("HR4.5.2 Centralizer is span of identity matrix",
          is_scalar,
          "Confirms SU(3) on V_3 is the fundamental (irreducible)")

section("HR4.6  Could a different Cl(6) substructure give a different breaking?")

section("HR4.7  Higher reps of SU(3) x U(1) — corner-distinguishing matrix elements?")

c3_centralizer_dim = 0
gellmann_basis = lambdas
basis_gens = [L / 2 for L in gellmann_basis]
basis_gens.append(I3 / np.sqrt(3) / 2)

constraint = []
for E in basis_gens:
    comm = C_3 @ E - E @ C_3.conj().T
    constraint.append(comm.flatten())
C_mat = np.vstack(constraint)

_, s_c3, _ = np.linalg.svd(C_mat)

real_constraint = []
for E in basis_gens:
    comm = C_3 @ E - E @ C_3.conj().T
    real_constraint.append(np.concatenate([comm.flatten().real,
                                            comm.flatten().imag]))

eigvals_C3, eigvecs_C3 = np.linalg.eig(C_3)

proj_centralizer = []
for k in range(3):
    v = eigvecs_C3[:, k:k+1]
    P = v @ v.conj().T
    proj_centralizer.append(P)

ok_proj = all(is_close(commutator(C_3, P), np.zeros((3, 3)))
              for P in proj_centralizer)
check("HR4.7.1 Centralizer of C_3 in u(3) is 3-dim "
      "(eigenspace projectors)",
      ok_proj and len(proj_centralizer) == 3,
      "C_3 has 3 distinct eigenvalues -> 3 projectors")

expect_table = np.zeros((3, 3))
for n in range(3):
    corner = np.zeros((3, 1), dtype=complex)
    corner[n, 0] = 1
    for k in range(3):
        expect_table[n, k] = (corner.conj().T @ proj_centralizer[k] @ corner).real[0, 0]

all_uniform = np.allclose(expect_table, 1/3 * np.ones((3, 3)))
check("HR4.7.2 C_3-invariant projectors P_k have uniform expectation "
      "1/3 on each corner",
      all_uniform,
      f"expect[n,k] = 1/3 for all n, k (corners share C_3-invariant data)")

A_invariant = sum(proj_centralizer)
A_invariant2 = 1.5 * proj_centralizer[0] + 0.7 * proj_centralizer[1] + 0.7 * proj_centralizer[2]

A_test = 1.5 * proj_centralizer[0] + 0.7 * proj_centralizer[1] - 0.3 * proj_centralizer[2]
ok_a_inv = is_close(commutator(C_3, A_test), np.zeros((3, 3)))
check("HR4.7.3 Random linear combo of C_3-eigenspace projectors is "
      "C_3-invariant",
      ok_a_inv,
      "")

expect_A = np.zeros(3)
for n in range(3):
    corner = np.zeros((3, 1), dtype=complex)
    corner[n, 0] = 1
    expect_A[n] = (corner.conj().T @ A_test @ corner).real[0, 0]
all_eq_A = np.allclose(expect_A, expect_A[0])
check("HR4.7.4 C_3-invariant A_test has equal expectation on 3 corners",
      all_eq_A,
      f"expect = {expect_A}: equal as substep 4 AC narrowing predicts")

section("HR4.8  Embedding rigidity — does choice of SU(3) ↪ SU(4) matter?")

np.random.seed(42)
M_random = np.random.randn(4, 4) + 1j * np.random.randn(4, 4)
M_random = (M_random + M_random.conj().T) / 2

_, V_random = np.linalg.eigh(M_random)
W = V_random[:, :3]

SU3_on_W = []
for L in lambdas:
    T_4 = W @ (L / 2) @ W.conj().T
    SU3_on_W.append(T_4)

ok_rank = all(np.linalg.matrix_rank(t, tol=1e-9) <= 3 for t in SU3_on_W)
check("HR4.8.1 SU(3) on random 3-subspace W has rank<=3 in C^4",
      ok_rank,
      "SU(3) action restricts to W")

null_dim_W, null_basis_W, basis15_W = centralizer_in_su4(SU3_on_W)
check("HR4.8.2 Centralizer of random SU(3)_on_W in su(4) is 1-dim",
      null_dim_W == 1,
      f"dim = {null_dim_W}: U(1) generator unique")

if null_dim_W == 1:
    coefs_W = null_basis_W[0]
    M_central_W = sum(coefs_W[i] * basis15_W[i] for i in range(15))

    eigs_W = np.sort(np.linalg.eigvalsh(M_central_W))

    n_unique = len(set(np.round(eigs_W, 6)))
    check("HR4.8.3 Centralizer eigenvalues on random W: 3 equal + 1 different",
          n_unique == 2,
          f"eigenvalues sorted: {eigs_W}")

    proj_W = W.conj().T @ M_central_W @ W
    diag_W = np.diag(proj_W).real
    all_eq_W = np.allclose(diag_W, diag_W[0], atol=1e-6)
    check("HR4.8.4 U(1) charge is uniform on the 3-dim W subspace",
          all_eq_W,
          f"diag on W: {diag_W} (Schur on irrep)")

section("HR4.9  Selected Cartan and charge-square diagnostics")

T_3 = lambdas[2] / 2
ok_T3_not_inv = not is_close(commutator(C_3, T_3), np.zeros((3, 3)))
check("HR4.9.2 SU(3) Cartan T_3 is NOT C_3-invariant (as expected)",
      ok_T3_not_inv,
      "T_3 has unequal coordinate diagonals and does not commute with the supplied C_3")

U_BL_quark_sq = U_BL_on_quark @ U_BL_on_quark
diag_sq = np.diag(U_BL_quark_sq).real
check("HR4.9.3 U(1)_(B-L)^2 on corners: uniform 1/9",
      np.allclose(diag_sq, [1/9, 1/9, 1/9]),
      f"{diag_sq}")

# Decisive control: C3 invariance does not imply scalarity, even inside
# the Hermitian Gell-Mann span. Integer entries make the algebra exact here.
H_c3 = C_3 + C_3.conj().T
check("C3 control: H=C+C† is Hermitian and commutes with C",
      np.array_equal(H_c3, H_c3.conj().T)
      and np.array_equal(commutator(C_3, H_c3), np.zeros((3, 3))))
check("C3 control: H is traceless, non-scalar, and has equal coordinate diagonals",
      np.trace(H_c3) == 0 and np.array_equal(np.diag(H_c3), np.zeros(3))
      and not np.array_equal(H_c3, np.zeros((3, 3))))
check("C3 control: H=lambda_1+lambda_4+lambda_6",
      np.array_equal(H_c3, lambdas[0] + lambdas[3] + lambdas[5]))
check("C3 control: H^2=H+2I; spectrum {2,-1,-1}",
      np.array_equal(H_c3 @ H_c3, H_c3 + 2 * I3)
      and np.allclose(np.linalg.eigvalsh(H_c3), [-1, -1, 2]))

section("HR4.10  Summary of bounded matrix diagnostics")

print("Selected 3+1 result: full SU(3) centralizer is scalar on its defining three.")
print("Its u(4) centralizer has dimension two; its traceless part has dimension one.")
print("Group stabilizer: S(U(3) x U(1)) = (SU(3) x U(1))/Z_3.")
print("C3 invariance gives equal coordinate diagonals, not scalarity.")
print("Physical carrier selection and admissible-observable hypotheses remain open.")
print("Historical universal/no-escape and promotion assertions are withdrawn.")
print(f"=== TOTAL: PASS={PASS + BPASS}, FAIL={FAIL + BFAIL} ===")
sys.exit(1 if FAIL > 0 or BFAIL > 0 else 0)
