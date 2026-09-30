#!/usr/bin/env python3
"""T25 test A: can the ONE 8-state taste cube host both the SM gauge content and the generation triplet?

Operator definitions are copied from the repo (read only):
  scripts/audit_companion_cl3_taste_abstract_c8_orbit_scope_2026_06_12.py  (perm matrices, Y, T3)
  scripts/verify_cl3_sm_embedding.py  (fibre SU(2)_weak Jf_i, Gell-Mann SU(3) on the symmetric base)
Pre-registration: PREREGISTER.md (same folder).
"""
import json
from itertools import product as iproduct

import numpy as np

np.set_printoptions(precision=5, suppress=True, linewidth=150)
EPS = 1e-10
out = {}


def kron(*m):
    r = m[0]
    for x in m[1:]:
        r = np.kron(r, x)
    return r


def idx(b1, b2, b3):
    return 4 * b1 + 2 * b2 + b3


def perm8(perm):
    mat = np.zeros((8, 8), dtype=complex)
    for b in iproduct(range(2), repeat=3):
        nb = [b[perm[i]] for i in range(3)]
        mat[idx(*nb), idx(*b)] = 1.0
    return mat


I2, I4, I8 = np.eye(2, dtype=complex), np.eye(4, dtype=complex), np.eye(8, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)

# --- S3 on the cube (repo definitions) ---
T12 = perm8([1, 0, 2])
T23 = perm8([0, 2, 1])
T13 = perm8([2, 1, 0])
Z3 = perm8([2, 0, 1])
S3elems = {"e": I8, "T12": T12, "T23": T23, "T13": T13, "C3": Z3, "C3^2": Z3 @ Z3}

# --- Hamming weight ---
hw = np.array([sum(b) for b in iproduct(range(2), repeat=3)])
P_hw = {k: np.diag((hw == k).astype(float)).astype(complex) for k in range(4)}
HW = np.diag(hw.astype(float)).astype(complex)
hw1 = [idx(1, 0, 0), idx(0, 1, 0), idx(0, 0, 1)]

# --- gauge operators (repo definitions) ---
p_swap = np.zeros((8, 8), dtype=complex)
for b1, b2, b3 in iproduct(range(2), repeat=3):
    p_swap[idx(b1, b2, b3), idx(b2, b1, b3)] = 1.0
P_sym, P_anti = (I8 + p_swap) / 2, (I8 - p_swap) / 2
Y = (1 / 3) * P_sym - P_anti
Jf = [kron(I4, s1 / 2), kron(I4, s2 / 2), kron(I4, s3 / 2)]  # SU(2)_weak on the fibre b3
T3f = Jf[2]
Q = T3f + Y / 2

sq2 = np.sqrt(2)
U_base = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 1 / sq2, 1 / sq2, 0], [0, 1 / sq2, -1 / sq2, 0]], dtype=complex)
lam = np.zeros((8, 3, 3), dtype=complex)
lam[0] = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
lam[1] = [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]]
lam[2] = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
lam[3] = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
lam[4] = [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]]
lam[5] = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
lam[6] = [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
Tc = []
for a in range(8):
    M4 = np.zeros((4, 4), dtype=complex)
    M4[:3, :3] = lam[a] / 2
    Tc.append(kron(U_base.conj().T @ M4 @ U_base, I2))


def comm(a, b):
    return a @ b - b @ a


def nrm(a):
    return float(np.linalg.norm(a))


# ============ A1: charge table on the 8 states (sanity: this is the SM one-generation LH doublet content) ============
Qeig = np.round(np.linalg.eigvalsh(Q), 6)
Yeig = np.round(np.linalg.eigvalsh(Y), 6)
out["A1_Q_spectrum_C8"] = sorted(Qeig.tolist())
out["A1_Y_spectrum_C8"] = sorted(Yeig.tolist())
weak_cas = sum(J @ J for J in Jf)
out["A1_weak_Casimir_C8_is_3over4_everywhere"] = bool(np.allclose(weak_cas, 0.75 * I8, atol=EPS))
colour_cas = sum(T @ T for T in Tc)
out["A1_colour_Casimir_spectrum_C8"] = sorted(np.round(np.linalg.eigvalsh(colour_cas), 6).tolist())
print("A1 Q spectrum on C^8:", out["A1_Q_spectrum_C8"])
print("A1 weak Casimir = 3/4 on all C^8 (no SU(2)_weak singlet on the cube):", out["A1_weak_Casimir_C8_is_3over4_everywhere"])
print("A1 colour Casimir spectrum:", out["A1_colour_Casimir_spectrum_C8"])

# ============ A2: what are the three hw=1 states, gauge-wise ============
def restrict(op, ids):
    return op[np.ix_(ids, ids)]


Q1, Y1, T31 = restrict(Q, hw1), restrict(Y, hw1), restrict(T3f, hw1)
qe, qv = np.linalg.eigh(Q1.real)
out["A2_Q_on_hw1"] = np.round(qe, 6).tolist()
out["A2_Y_on_hw1"] = np.round(np.linalg.eigvalsh(Y1.real), 6).tolist()
out["A2_T3_on_hw1"] = np.round(np.linalg.eigvalsh(T31.real), 6).tolist()
distinct_Q = len(set(np.round(qe, 6).tolist()))
out["A2_distinct_Q_values_on_hw1"] = distinct_Q
print("A2 on hw=1: Q =", out["A2_Q_on_hw1"], " Y =", out["A2_Y_on_hw1"], " T3 =", out["A2_T3_on_hw1"])
print("A2 Q eigenvectors (columns, basis e1=100,e2=010,e3=001):\n", np.round(qv, 4))
# joint invariance: is hw=1 preserved by Q, Y, T3?
out["A2_Q_preserves_hw1"] = bool(nrm(comm(P_hw[1], Q)) < EPS)
# colour generators do not preserve hw
comm_col_hw = max(nrm(comm(P_hw[1], T)) for T in Tc)
comm_col_hw1_leak = max(nrm(P_hw[1] @ T @ (I8 - P_hw[1])) for T in Tc)
out["A2_max_norm_[P_hw1,T_colour]"] = comm_col_hw
out["A2_max_leak_of_hw1_under_colour"] = comm_col_hw1_leak
print("A2 [P_hw1, colour generators] max norm =", round(comm_col_hw, 4), " leak out of hw=1 =", round(comm_col_hw1_leak, 4))

# ============ A3: stabiliser in S3 of the gauge algebra ============
gauge_ops = [Y] + Jf + Tc
rows = {}
for name, g in S3elems.items():
    rows[name] = max(nrm(comm(g, o)) for o in gauge_ops)
out["A3_max_commutator_norm_of_S3_element_with_gauge_algebra"] = {k: round(v, 6) for k, v in rows.items()}
stab = [k for k, v in rows.items() if v < EPS]
out["A3_stabiliser_of_gauge_algebra_in_S3"] = stab
comps = {}
for lab, ops in [("Y", [Y]), ("T3_fibre", [T3f]), ("SU3", Tc), ("all_weak", Jf)]:
    comps[lab] = {k: round(max(nrm(comm(g, o)) for o in ops), 6) for k, g in S3elems.items()}
out["A3_commutators_by_operator"] = comps
print("A3 max ||[g, gauge algebra]||:", out["A3_max_commutator_norm_of_S3_element_with_gauge_algebra"])
print("A3 stabiliser of the SM gauge algebra in S3:", stab)

# ============ A4: hw=1 mass operators: charge-conserving and C3-covariant ============
# Hermitian 3x3 basis (9 real params)
def herm_basis(n):
    B = []
    for i in range(n):
        m = np.zeros((n, n), dtype=complex)
        m[i, i] = 1
        B.append(m)
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), dtype=complex)
            m[i, j] = m[j, i] = 1
            B.append(m)
            m = np.zeros((n, n), dtype=complex)
            m[i, j] = 1j
            m[j, i] = -1j
            B.append(m)
    return B


def commutant_dim(basis, constraints):
    """dimension of {sum c_k basis_k : [g, sum]=0 for g in constraints}"""
    if not constraints:
        return len(basis)
    rows = []
    for g in constraints:
        cols = [np.concatenate([comm(g, b).real.ravel(), comm(g, b).imag.ravel()]) for b in basis]
        rows.append(np.array(cols).T)
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    rank = int(np.sum(s > 1e-9))
    return len(basis) - rank


B3 = herm_basis(3)
C3_1 = restrict(Z3, hw1)
T12_1 = restrict(T12, hw1)
dims = {
    "no_constraint": commutant_dim(B3, []),
    "C3_only": commutant_dim(B3, [C3_1]),
    "S3_full": commutant_dim(B3, [C3_1, T12_1]),
    "Q_only": commutant_dim(B3, [Q1]),
    "Q_and_C3": commutant_dim(B3, [Q1, C3_1]),
    "Q_and_T12": commutant_dim(B3, [Q1, T12_1]),
    "Q_and_S3": commutant_dim(B3, [Q1, C3_1, T12_1]),
}
out["A4_dim_hermitian_hw1_operators"] = dims
print("A4 dims of Hermitian hw=1 operators under constraints:", dims)

# circulant mass operator with generic complex b: how much does it violate charge conservation?
J = np.roll(np.eye(3), 1, axis=0).astype(complex)  # e1->e2->e3->e1
rng = np.random.default_rng(1)
viol = []
for _ in range(5):
    a = rng.normal()
    b = rng.normal() + 1j * rng.normal()
    H = a * np.eye(3) + b * J + np.conj(b) * J.conj().T
    off = H - np.diag(np.diag(H))
    viol.append(nrm(comm(Q1, H)) / nrm(off))
out["A4_circulant_charge_violation_ratio_||[Q,H]||/||H_offdiag||"] = [round(v, 4) for v in viol]
# weight of each Fourier (C3) mode on the Q eigenstates
w = np.exp(2j * np.pi / 3)
F = np.array([[1, 1, 1], [1, w, w ** 2], [1, w ** 2, w]]).T / np.sqrt(3)  # columns = Fourier modes
weights = np.abs(qv.T @ F) ** 2
out["A4_Fourier_mode_weights_on_Q_eigenstates"] = np.round(weights, 4).tolist()
print("A4 circulant charge-violation ratios:", out["A4_circulant_charge_violation_ratio_||[Q,H]||/||H_offdiag||"])
print("A4 |<Q-eigenstate_i | Fourier mode_k>|^2:\n", np.round(weights, 4))

# ============ A5: zero-mode census of the supplied walker vs SM Weyl count ============
def walker_kernel(L=4):
    n = L ** 3
    S = []
    for a in range(3):
        M = np.zeros((n, n), dtype=complex)
        for x in iproduct(range(L), repeat=3):
            i = x[0] * L * L + x[1] * L + x[2]
            for sgn in (+1, -1):
                y = list(x)
                y[a] = (y[a] + sgn) % L
                j = y[0] * L * L + y[1] * L + y[2]
                M[i, j] += sgn / (2j)
        S.append(M)
    H = kron(S[0], s1) + kron(S[1], s2) + kron(S[2], s3)  # sum_a S_a (x) sigma_a
    ev = np.linalg.eigvalsh(H)
    return H, ev


Hw, ev = walker_kernel(4)
nzero = int(np.sum(np.abs(ev) < 1e-9))
# chirality at each corner n: sign det(diag((-1)^{n_a})) = (-1)^{|n|}
chir = {}
for nvec in iproduct(range(2), repeat=3):
    chir[nvec] = int((-1) ** sum(nvec))
nR = sum(1 for v in chir.values() if v > 0)
nL = sum(1 for v in chir.values() if v < 0)
out["A5_walker_zero_modes_4^3_torus"] = nzero
out["A5_weyl_points_chirality_split_+/-"] = [nR, nL]
sm_per_gen_with_nuR = 16
out["A5_SM_weyl_fields_3_generations_with_nuR"] = 3 * sm_per_gen_with_nuR
out["A5_SM_weyl_fields_3_generations_no_nuR"] = 3 * 15
out["A5_ratio_needed_over_supplied"] = (3 * sm_per_gen_with_nuR) / (nzero / 2)
print(f"A5 walker zero modes (4^3 torus) = {nzero} = {nzero//2} Weyl points, chirality split {nR}+/{nL}-;"
      f" SM needs {3*sm_per_gen_with_nuR} Weyl fields (3 gen with nu_R): ratio {out['A5_ratio_needed_over_supplied']}")

# ============ verdict against the pre-registration ============
cond_a = all(max(nrm(comm(Z3, o)) for o in gauge_ops) < EPS for _ in [0])
cond_b = distinct_Q == 1
cond_c = dims["Q_and_C3"] >= 3
passed = cond_a or cond_b or cond_c
failed = (distinct_Q >= 2) and ("C3" not in stab) and (dims["Q_and_C3"] == 1)
out["verdict_PASS_(cube_can_host_both)"] = bool(passed)
out["verdict_FAIL_(cube_cannot_host_both)"] = bool(failed)
print("\nVERDICT: PASS =", passed, "  FAIL =", failed)
json.dump(out, open("test_T25A_results.json", "w"), indent=1, default=str)
