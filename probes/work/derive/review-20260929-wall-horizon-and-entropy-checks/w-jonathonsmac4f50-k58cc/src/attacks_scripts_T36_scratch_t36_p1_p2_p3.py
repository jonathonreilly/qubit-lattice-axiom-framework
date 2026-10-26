#!/usr/bin/env python3
"""T36 tests P1 (law-level commutant), P2 (subgroup lattice, no-protection lemma), P3 (locking).
Run: python3 t36_p1_p2_p3.py     Pre-registration: PREREGISTRATION.md (written before this ran).
"""
from __future__ import annotations
import itertools
import numpy as np
from t36_corner_model import ROTS, ROT_K, SHIFT_K, HW

rng = np.random.default_rng(20260929)
np.set_printoptions(precision=6, suppress=True, linewidth=140)

# -------------------------------------------------------------------- helpers
def commutant_dim(mats, complex_dim=True):
    """dimension of {X : M X = X M for all M in mats} (complex matrices)."""
    n = mats[0].shape[0]
    I = np.eye(n)
    rows = [np.kron(M, I) - np.kron(I, M.T) for M in mats]      # vec(MX - XM), column-major vec
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < 1e-9))


def distinct_levels(mats, trials=3):
    """generic number of distinct eigenvalues of a Hermitian operator invariant under the group `mats`."""
    n = mats[0].shape[0]
    best = 0
    for _ in range(trials):
        X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        X = X + X.conj().T
        Y = sum(M @ X @ np.linalg.inv(M) for M in mats) / len(mats)
        ev = np.sort(np.linalg.eigvalsh((Y + Y.conj().T) / 2))
        levels = 1 + int(np.sum(np.diff(ev) > 1e-7))
        best = max(best, levels)
    return best


idx1 = [i for i in range(8) if HW[i] == 1]        # hw=1 basis states (bit patterns 100, 010, 001 in s-order)
R1 = [M[np.ix_(idx1, idx1)] for M in ROT_K]        # 3x3 restriction of each rotation lift to hw=1
V = [M.astype(float) for M in ROTS]                # the 3x3 rotation matrices (vector rep)

print("=" * 78)
print("P1  law level: commutant of the 24 rotation lifts")
print("=" * 78)
# closure / invariance of the hw=1 subspace under rotations
leak = max(np.abs(M[np.ix_([i for i in range(8) if HW[i] != 1], idx1)]).max() for M in ROT_K)
print("hw=1 invariant under all 24 rotation lifts (max leakage out):", leak)
chi_R1 = [round(float(np.trace(M))) for M in R1]
chi_V = [round(float(np.trace(M))) for M in V]
print("characters of hw=1 restriction == characters of the 3x3 rotation matrices (T1 = vector rep):",
      sorted(chi_R1) == sorted(chi_V))
print("commutant dim of O on hw=1 (complex 3x3):", commutant_dim(R1), " -> generic levels:", distinct_levels(R1))
print("commutant dim of O on the full 8-dim kernel:", commutant_dim(ROT_K), "(2A1+2T1 predicts 8)")
# unsigned S_3 permutation representation (the older notes' premise)
perm3 = [np.eye(3)[list(p)] for p in itertools.permutations(range(3))]
print("older premise: S_3 permutation rep on 3 corners: commutant dim", commutant_dim(perm3),
      "levels", distinct_levels(perm3), "(A1+E: 2)")
# shift lifts: what do they do to the hw grading
print("\nKS one-site shift lifts on the 8-dim kernel:")
for c, S in enumerate(SHIFT_K):
    leak_out = np.abs(S[np.ix_([i for i in range(8) if HW[i] != 1], idx1)]).max()
    print(f"  shift {c}: sends hw=1 states out of hw=1 with weight {leak_out:.3f}  (1.0 = fully out)")
allmats = ROT_K + SHIFT_K
print("commutant dim of <rotations, shifts> on the full kernel:", commutant_dim(allmats),
      "(1 = irreducible: hw grading is not preserved by the exact one-site translations)")
# does the hw-grading operator Z1+Z2+Z3 commute with them?
Zs = np.diag(3 - 2 * HW.astype(float))
comm_rot = max(np.abs(M @ Zs - Zs @ M).max() for M in ROT_K)
comm_sh = [np.abs(S @ Zs - Zs @ S).max() for S in SHIFT_K]
print("hw-grading operator Z1+Z2+Z3 commutes with rotations (max |[R,Z]|):", comm_rot,
      "  with shifts:", comm_sh)

print()
print("=" * 78)
print("P2  subgroup lattice of the 24 rotations: which residual symmetries split hw=1?")
print("=" * 78)
key = {tuple(M.flatten()): i for i, M in enumerate(ROTS)}
mul = [[key[tuple((A @ B).flatten())] for B in ROTS] for A in ROTS]
def closure(gens):
    S = {0} | set(gens)   # identity index?
    ident = key[tuple(np.eye(3, dtype=int).flatten())]
    S = {ident} | set(gens)
    changed = True
    while changed:
        changed = False
        for a in list(S):
            for b in list(S):
                c = mul[a][b]
                if c not in S:
                    S.add(c)
                    changed = True
    return frozenset(S)
subgroups = set()
n = len(ROTS)
for a in range(n):
    subgroups.add(closure([a]))
    for b in range(a, n):
        subgroups.add(closure([a, b]))
subgroups = sorted(subgroups, key=lambda s: (len(s), sorted(s)))
print("number of subgroups found:", len(subgroups), "(S_4 has 30)")
def order_class(H):
    return len(H)
rows = []
violations = 0
for H in subgroups:
    mats = [R1[i] for i in H]
    d = commutant_dim(mats)
    s = distinct_levels(mats)
    # H-invariant real tensors on the vector rep V: symmetric traceless, antisymmetric (axial vector)
    A_sym, A_asym = [], []
    basis_sym = []
    for i in range(3):
        for j in range(i, 3):
            E = np.zeros((3, 3)); E[i, j] = 1; E[j, i] = 1
            basis_sym.append(E)
    basis_asym = []
    for i in range(3):
        for j in range(i + 1, 3):
            E = np.zeros((3, 3)); E[i, j] = 1; E[j, i] = -1
            basis_asym.append(E)
    def inv_dim(basis, traceless=False):
        # invariant subspace of span(basis) under X -> R X R^T for R in H; return dim (excluding trace part if asked)
        Bm = np.array([b.flatten() for b in basis]).T           # 9 x k
        cons = []
        for i in H:
            R = V[i]
            T = np.kron(R, R)                                     # acts on flattened X
            cons.append((T - np.eye(9)) @ Bm)
        C = np.vstack(cons)
        sv = np.linalg.svd(C, compute_uv=False)
        rank = int(np.sum(sv > 1e-9))
        dim = len(basis) - rank
        return dim
    n_sym = inv_dim(basis_sym) - 1        # remove the identity (trace) part, always invariant
    n_asym = inv_dim(basis_asym)
    nH = n_sym + n_asym
    ok = (s >= 2) == (nH >= 1)
    if not ok:
        violations += 1
    rows.append((len(H), d, s, n_sym, n_asym, ok))
from collections import Counter
cnt = Counter(rows)
print(" |H|  commutant_dim  levels  inv_traceless_sym  inv_axial  equivalence_holds   #subgroups")
for k in sorted(cnt):
    print(f" {k[0]:>3}  {k[1]:>13}  {k[2]:>6}  {k[3]:>17}  {k[4]:>9}  {str(k[5]):>17}   {cnt[k]}")
print("violations of  (levels>=2) <=> (spatial quadrupole or axial vector allowed):", violations)
irreducible = [len(H) for H, r in zip(subgroups, rows) if r[2] == 1]
print("residual groups that keep the triplet degenerate (irreducible):", sorted(irreducible),
      "(orders 12 = tetrahedral T and 24 = O)")
# min parameters for 3 levels
print("smallest commutant dimension among subgroups giving 3 distinct levels:",
      min(r[1] for r in rows if r[2] == 3))

print()
print("=" * 78)
print("P3  locking in the corner model: staircase masses r_a per axis and the hw=0 branch")
print("=" * 78)
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.diag([1, -1]).astype(complex)
def kr(*ms):
    o = np.array([[1.0 + 0j]])
    for m in ms:
        o = np.kron(o, m)
    return o
XI = [kr(SX, I2, I2), kr(SZ, SX, I2), kr(SZ, SZ, SX)]
GAM = [kr(SY, I2, I2), kr(SZ, SY, I2), kr(SZ, SZ, SY)]
ZA = [kr(SZ, I2, I2), kr(I2, SZ, I2), kr(I2, I2, SZ)]
def Hbloch(q):
    H = np.zeros((8, 8), dtype=complex)
    for a in range(3):
        H += (1 + np.cos(q[a])) * XI[a] + np.sin(q[a]) * GAM[a]
    return H
axis_state = [4, 2, 1]   # basis index with only bit a set (a=0 is the most significant bit)
def branch_energy(p, D, target=0):
    w, U = np.linalg.eigh(Hbloch(np.pi + p) + D)
    k = int(np.argmax(np.abs(U[target, :]) ** 2))
    return w[k]
def stiffness_tensor(D, eps=2e-3):
    """quadratic coefficient tensor K_ab of the hw=0 branch, E0(p) = -p^T K p (fit from exact eigenvalues)."""
    pts, vals = [], []
    for _ in range(40):
        p = rng.normal(size=3) * eps
        pts.append(p); vals.append(branch_energy(p, D))
    P = np.array(pts); y = np.array(vals)
    feats = np.array([[p[0]**2, p[1]**2, p[2]**2, 2*p[0]*p[1], 2*p[0]*p[2], 2*p[1]*p[2]] for p in P])
    coef, *_ = np.linalg.lstsq(feats, y, rcond=None)
    K = -np.array([[coef[0], coef[3], coef[4]], [coef[3], coef[1], coef[5]], [coef[4], coef[5], coef[2]]])
    return K
def staircase(r):
    return sum(r[a] * (np.eye(8) - ZA[a]) for a in range(3))   # eigenvalue 2 r_a on the state with only bit a set
cases = {
    "isotropic r=(1,1,1)": (1.0, 1.0, 1.0),
    "r=(1,0.1,0.01)": (1.0, 0.1, 0.01),
    "r=(1,0.007,1e-5)": (1.0, 0.007, 1e-5),
}
print("staircase masses 2r_a on the triplet; predicted stiffness 1/(2 r_a) (E0 = -sum p_a^2/(2 r_a))")
for name, r in cases.items():
    D = staircase(r)
    K = stiffness_tensor(D, eps=(1e-3 if min(r) > 1e-3 else 2e-5 * max(r)))
    pred = np.diag([1 / (2 * x) for x in r])
    # relative comparison of diagonal entries
    diag_fit = np.diag(K)
    print(f"  {name:22s} fitted diag(K) = {diag_fit}  predicted = {np.diag(pred)}  rel.err = {np.max(np.abs(diag_fit/np.diag(pred)-1)):.2e}")
# general Hermitian source S on the triplet: prediction K = c^dagger M1^{-1} c
print("\ngeneral Hermitian source S on the triplet (masses M1 = 2 r I + S); prediction E0 = -v^dag M1^-1 v, v_a = <e_a| p.Gamma |0>")
r0 = 1.0
S3 = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
S3 = 0.25 * (S3 + S3.conj().T)
S8 = np.zeros((8, 8), dtype=complex)
for i, a in enumerate(axis_state):
    for j, b in enumerate(axis_state):
        S8[a, b] = S3[i, j]
D = staircase((r0, r0, r0)) + S8
M1 = np.array([[D[a, b] for b in axis_state] for a in axis_state])
worst = 0.0
for _ in range(6):
    p = rng.normal(size=3) * 1e-3
    E_exact = branch_energy(p, D)
    Hp = -sum(p[a] * GAM[a] for a in range(3))                    # = H(pi+p) to first order
    v = np.array([Hp[axis_state[a], 0] for a in range(3)])
    E_pred = -(v.conj() @ np.linalg.inv(M1) @ v).real
    worst = max(worst, abs(E_exact / E_pred - 1))
print(f"  worst relative deviation exact vs perturbative prediction over 6 random p: {worst:.2e}")
print("  eigenvalues of triplet mass matrix M1:", np.linalg.eigvalsh(M1))
print("  eigenvalues of inverse (light-state stiffness tensor):", np.linalg.eigvalsh(np.linalg.inv(M1)))
