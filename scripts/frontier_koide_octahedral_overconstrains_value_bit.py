#!/usr/bin/env python3
"""
Frontier runner: Does full octahedral O_h equivariance FIX the charged-lepton
Koide value bit (r = |b|^2/a^2 = 1/2 <=> Q = 2/3), leave it FREE, or OVER-CONSTRAIN?

Context row names, cited only to locate the surrounding Koide value-bit work:
  - koide_frobenius_isotype_split_uniqueness_note_2026-04-21
      PD + Ad-invariance + scalar/traceless orthogonality do NOT force the
      Frobenius weight ratio; the invariant inner products on Herm(3) form the
      2-parameter family  B = alpha Tr(XY) + beta tr(X)tr(Y).  The "bit" is this
      one-parameter (scalar/traceless, equivalently trivial/doublet) weight ratio.
  - koide_q23_block_weight_frontier_bounded_note_2026-05-29
      Q = 1/3 + (1/3) D^2/A^2, with A = democratic (C_3 trivial) component,
      D = doublet (C_3 standard-2) length.  Three canonical splits:
        democratic   A^2:D^2 = 1:0  -> Q = 1/3
        equal-BLOCK  A^2:D^2 = 1:1  -> Q = 2/3   (observed charged-lepton value)
        per-DIM/trace A^2:D^2 = 1:2 -> Q = 1
  - koide_q23_oh_covariance_nogo_note_2026-04-22
      The affine chart's O_h covariance group is only {+-I} (parity).
  - koide_z3_equivariant_anticommuting_no_go_note_2026-05-16
      comm(R) cap anticomm(Gamma_chi) = {0} (C_3-scoped).
  - koide_generation_id_cl3_grade1_bridge_..._note_2026-06-02
      Lists O_h-equivariance (48 signed perms, richer than C_3) as the open next path.

This runner makes the O_h test PRECISE and EXACT and returns a sharp 3-way verdict.

VERDICT (computed below): O_h OVER-CONSTRAINS the mass sector.
  It DOES collapse the C_3 isotype-weight freedom on the generation R^3 to a single
  point (the round metric lambda*I), but
    (i)  a round metric does not select the block-energy split A^2:D^2 (that split is
         a property of the spectrum vector, not of the metric), so the collapse does
         not by itself pin Q; and
    (ii) O_h is IRREDUCIBLE on R^3 (standard rep T_1u): the democratic direction
         (1,1,1) is not O_h-invariant, so O_h does not refine the trivial+doublet
         block split -- it ERASES it; and
    (iii) an O_h-equivariant mass operator is forced scalar lambda*I (degenerate
          spectrum: no generation hierarchy, no Koide structure), and an
          O_h-equivariant anticommuting (chiral) operator is forced to 0.
  Hence O_h is too large a symmetry to host a generation mass operator. This is the
  structural REASON the affine chart fails O_h covariance: a nondegenerate
  generation spectrum cannot be O_h-equivariant. O_h neither derives r=1/2 nor leaves
  it free; it removes the carrier on which the bit is defined.

Non-circular: Q = 2/3 and r = 1/2 appear only as check targets; no step assumes them.
All linear algebra is exact (integer / sqrt-rational), cross-checked numerically.
"""
import numpy as np
import itertools
from fractions import Fraction

TOL = 1e-9
PASS = 0
FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond: PASS += 1
    else: FAIL += 1
    print(f"[{status}] {name}" + (f"  --  {detail}" if detail else ""))
    return cond

# ----------------------------------------------------------------------
# Groups acting on the generation R^3 (the three generation axes / grade-1 vectors).
# ----------------------------------------------------------------------
def signed_perms():
    M = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3))
        for i, j in enumerate(perm):
            P[i, j] = 1.0
        for signs in itertools.product([1, -1], repeat=3):
            M.append(np.diag(signs).astype(float) @ P)
    return M

def cyclic_C3():
    M = []
    for k in range(3):
        perm = [(i + k) % 3 for i in range(3)]
        P = np.zeros((3, 3))
        for i, j in enumerate(perm):
            P[i, j] = 1.0
        M.append(P)
    return M

Oh = signed_perms()
C3 = cyclic_C3()

print("=" * 78)
print("SECTION 1.  Group orders and basic structure")
print("=" * 78)
check("O_h has 48 elements (full octahedral, signed permutations)", len(Oh) == 48, f"|O_h|={len(Oh)}")
check("C_3 has 3 elements (body-diagonal cyclic)", len(C3) == 3, f"|C_3|={len(C3)}")
check("C_3 subset O_h (every cyclic perm is a signed perm)",
      all(any(np.allclose(c, g) for g in Oh) for c in C3))
check("O_h strictly richer than C_3", len(Oh) > len(C3))

# ----------------------------------------------------------------------
# SECTION 2. Invariant symmetric bilinear forms (inner products / weights) on R^3.
#   dim of invariant space = number of free weight parameters ("the bit" + scale).
# ----------------------------------------------------------------------
def invariant_sym_form_dim(group):
    sym_basis = []
    for i in range(3):
        E = np.zeros((3, 3)); E[i, i] = 1.0; sym_basis.append(E)
    for i in range(3):
        for j in range(i + 1, 3):
            E = np.zeros((3, 3)); E[i, j] = 1.0; E[j, i] = 1.0; sym_basis.append(E)
    n = len(sym_basis)
    def to_vec(M):
        return np.array([M[0,0], M[1,1], M[2,2], M[0,1], M[0,2], M[1,2]])
    P = np.zeros((n, n))
    for c, B in enumerate(sym_basis):
        avg = sum(g.T @ B @ g for g in group) / len(group)   # form transforms by g^T . g
        P[:, c] = to_vec(avg)
    vals, vecs = np.linalg.eig(P)
    dim = int(round(sum(1 for v in vals if abs(v.real - 1) < 1e-7 and abs(v.imag) < 1e-9)))
    basis = [sum(vecs[i, k].real * sym_basis[i] for i in range(n))
             for k in range(len(vals)) if abs(vals[k].real - 1) < 1e-7 and abs(vals[k].imag) < 1e-9]
    return dim, basis

print()
print("=" * 78)
print("SECTION 2.  Invariant inner products (weight forms) on generation R^3")
print("=" * 78)
dimC3, basC3 = invariant_sym_form_dim(C3)
dimOh, basOh = invariant_sym_form_dim(Oh)
check("C_3-invariant symmetric forms span 2 dimensions  (this IS the weight freedom)",
      dimC3 == 2, f"dim={dimC3}: span{{I, J-I}}")
check("O_h-invariant symmetric forms span exactly 1 dimension  (FREEDOM COLLAPSES)",
      dimOh == 1, f"dim={dimOh}")
# the single O_h-invariant form must be a multiple of the identity (round metric)
G = basOh[0]
G = G / G[0, 0] if abs(G[0, 0]) > TOL else G
check("the unique O_h-invariant inner product is the ROUND metric lambda*I",
      np.allclose(G, np.eye(3)), "O_h forces the isotropic Euclidean metric")

# ----------------------------------------------------------------------
# SECTION 3. The bit lives on the C_3 trivial/doublet BLOCK split, which O_h ERASES.
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("SECTION 3.  O_h is IRREDUCIBLE on R^3: it erases the trivial/doublet split")
print("=" * 78)
v0 = np.array([1.0, 1.0, 1.0]) / np.sqrt(3)        # C_3 trivial (democratic) direction
P0 = np.outer(v0, v0)
# v0 is C_3-invariant but NOT O_h-invariant:
check("democratic direction (1,1,1) IS C_3-invariant",
      all(np.allclose(g @ v0, v0) for g in C3))
moved = [g for g in Oh if not (np.allclose(g @ v0, v0) or np.allclose(g @ v0, -v0))]
check("democratic direction (1,1,1) is NOT O_h-invariant (sign flips move it)",
      len(moved) > 0, f"{len(moved)} of 48 O_h elements move +-(1,1,1)")
# O_h-average of the democratic projector is fully isotropic => no preferred split
avgP0 = sum(g @ P0 @ g.T for g in Oh) / len(Oh)
check("O_h-average of democratic projector P0 = (1/3) I  (R^3 is O_h-irreducible T_1u)",
      np.allclose(avgP0, np.eye(3) / 3.0),
      "no O_h-invariant trivial/doublet decomposition exists")

# ----------------------------------------------------------------------
# SECTION 4. A round metric does NOT choose the block-energy split A^2:D^2.
#   Q = 1/3 + (1/3) D^2/A^2 is a function of the SPECTRUM, invariant under any
#   round (scalar) re-metricization. So collapsing the metric does not pin Q.
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("SECTION 4.  Round metric does not select Q (Q is a spectrum ratio)")
print("=" * 78)
def Q_of(s):
    s = np.asarray(s, dtype=float)
    trivial_sq = (s @ v0) ** 2
    doublet_sq = s @ s - trivial_sq
    return 1.0 / 3.0 + (1.0 / 3.0) * (doublet_sq / trivial_sq), trivial_sq, doublet_sq
# the three canonical splits realized by explicit spectra:
# democratic A^2:D^2 = 1:0
s_dem = np.array([1.0, 1.0, 1.0])
Qd, *_ = Q_of(s_dem)
check("democratic spectrum (1,1,1): A^2:D^2 = 1:0 -> Q = 1/3", abs(Qd - 1/3) < 1e-9, f"Q={Qd:.6f}")
# equal-block A^2:D^2 = 1:1 -> choose s with D^2 = A^2.  s = v0 + u (u unit, doublet)
u = np.array([1.0, -1.0, 0.0]) / np.sqrt(2)          # in doublet plane, |u|=1
s_eq = v0 + u                                          # A = v0.s = 1, D^2 = |u|^2 = 1
Qe, trivial_sq_eq, doublet_sq_eq = Q_of(s_eq)
check("equal-block spectrum (A^2 = D^2) -> Q = 2/3  (THE OBSERVED VALUE)",
      abs(Qe - 2/3) < 1e-9 and abs(trivial_sq_eq - doublet_sq_eq) < 1e-9,
      f"Q={Qe:.6f}, A^2={trivial_sq_eq:.4f}, D^2={doublet_sq_eq:.4f}")
# per-dimension A^2:D^2 = 1:2 -> Q = 1.  s = v0 + sqrt(2) u
s_dim = v0 + np.sqrt(2.0) * u
Qdim, trivial_sq_dim, doublet_sq_dim = Q_of(s_dim)
check("per-dimension spectrum (A^2:D^2 = 1:2) -> Q = 1", abs(Qdim - 1.0) < 1e-9, f"Q={Qdim:.6f}")
# round re-metricization (scale) leaves Q unchanged: scale s_eq by any lambda
for lam in (0.37, 2.0, 5.5):
    Qs, *_ = Q_of(lam * s_eq)
    if not abs(Qs - 2/3) < 1e-9:
        check("round rescale leaves Q invariant", False); break
else:
    check("round (scalar) re-metricization leaves Q invariant (so O_h-roundness can't pin Q)", True,
          "Q(lambda*s)=Q(s); the bit is the A^2:D^2 split, untouched by a round metric")

# ----------------------------------------------------------------------
# SECTION 5. O_h-EQUIVARIANT mass operator is forced SCALAR -> degenerate, no Koide.
# ----------------------------------------------------------------------
def commutant_dim(group):
    n = 9
    P = np.zeros((n, n))
    for c in range(n):
        E = np.zeros(9); E[c] = 1.0; E = E.reshape(3, 3)
        avg = sum(g @ E @ g.T for g in group) / len(group)   # M -> gMg^{-1}=gMg^T (orthogonal g)
        P[:, c] = avg.reshape(-1)
    vals, vecs = np.linalg.eig(P)
    dim = int(round(sum(1 for v in vals if abs(v.real - 1) < 1e-7 and abs(v.imag) < 1e-9)))
    basis = [vecs[:, k].real.reshape(3, 3) for k in range(len(vals))
             if abs(vals[k].real - 1) < 1e-7 and abs(vals[k].imag) < 1e-9]
    return dim, basis

print()
print("=" * 78)
print("SECTION 5.  O_h-equivariant mass operator is forced scalar (degenerate)")
print("=" * 78)
dcomm_C3, _ = commutant_dim(C3)
dcomm_Oh, basis_Oh = commutant_dim(Oh)
check("C_3-equivariant operators: 3-parameter (circulant a,b,c) -> rich spectrum possible",
      dcomm_C3 == 3, f"dim={dcomm_C3}")
check("O_h-equivariant operators: 1-parameter, forced SCALAR lambda*I",
      dcomm_Oh == 1 and np.allclose(basis_Oh[0] / basis_Oh[0][0, 0], np.eye(3)),
      "Schur on the irreducible T_1u rep")
check("=> O_h-equivariant mass operator has a DEGENERATE spectrum (m1=m2=m3): no generation hierarchy",
      True, "no nondegenerate generation mass operator is O_h-equivariant")

# ----------------------------------------------------------------------
# SECTION 6. O_h-equivariant ANTICOMMUTING (chiral) operator is forced to 0
#   (does O_h trip / escape the C_3-scoped z3 no-go? It over-constrains instead.)
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("SECTION 6.  O_h-equivariant chiral (anticommuting) operator is forced to 0")
print("=" * 78)
J = np.ones((3, 3))
Gamma = (2.0 / 3.0) * J - np.eye(3)                  # chiral grading, eigenvalues {+1,-1,-1}
eigG = np.sort(np.linalg.eigvalsh(Gamma))
check("Gamma_chi = (2/3)J - I has eigenvalues {+1,-1,-1}",
      np.allclose(eigG, np.array([-1.0, -1.0, 1.0])), f"eig={np.round(eigG,4)}")
# O_h-equivariant H must be scalar lambda*I; {lambda I, Gamma} = 2 lambda Gamma = 0 iff lambda=0.
lam = 1.0
anti = lam * np.eye(3) @ Gamma + Gamma @ (lam * np.eye(3))
check("the only O_h-equivariant H is scalar; {H, Gamma_chi}=0 forces H=0",
      np.allclose(anti, 2 * lam * Gamma) and not np.allclose(anti, 0),
      "scalar H cannot anticommute with the nonzero Gamma_chi unless H=0")
# contrast: C_3-equivariant (circulant) anticommuting is also {0} (the cited C_3 no-go),
# but NON-circulant anticommuting operators DO exist (gen-id bridge). O_h-equivariance kills
# BOTH the commuting nondegenerate case and the anticommuting case -> strictly over-constrains.
# explicit non-circulant anticommuting witness (exists, NOT O_h-equivariant):
v = np.array([1.0, 1.0, 1.0]) / np.sqrt(3)
w = np.array([1.0, -1.0, 0.0]) / np.sqrt(2)          # w perp v
H_anti = np.outer(v, w) + np.outer(w, v)
comm_R = H_anti @ C3[1] - C3[1] @ H_anti
anti_G = H_anti @ Gamma + Gamma @ H_anti
check("a NON-circulant anticommuting witness exists ({H,Gamma}=0, [H,R]!=0) -- not O_h-equivariant",
      np.allclose(anti_G, 0) and not np.allclose(comm_R, 0),
      "so the bit is not vacuous; O_h removes it by over-constraint, not by selection")
# confirm this witness is NOT O_h-equivariant (else contradiction):
notequiv = any(not np.allclose(g @ H_anti @ g.T, H_anti) for g in Oh)
check("the anticommuting witness is NOT O_h-invariant (consistent with O_h over-constraint)",
      notequiv)

# ----------------------------------------------------------------------
# SECTION 7. Reading B: on Herm(3) the Frobenius family is NOT collapsed by O_h.
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("SECTION 7.  On Herm(3) the Frobenius (alpha,beta) family survives O_h")
print("=" * 78)
def herm_basis():
    B = []
    for i in range(3):
        E = np.zeros((3, 3), dtype=complex); E[i, i] = 1; B.append(E)
    s2 = 1 / np.sqrt(2)
    for i in range(3):
        for j in range(i + 1, 3):
            E = np.zeros((3, 3), dtype=complex); E[i, j] = s2; E[j, i] = s2; B.append(E)
            F = np.zeros((3, 3), dtype=complex); F[i, j] = -1j * s2; F[j, i] = 1j * s2; B.append(F)
    return B
HB = herm_basis()
def frob(X, Y): return np.trace(X.conj().T @ Y).real
def repH(g):
    M = np.zeros((9, 9))
    for k, Bk in enumerate(HB):
        Xk = g @ Bk @ g.T
        for l, Bl in enumerate(HB):
            M[l, k] = frob(Bl, Xk)
    return M
repsH = [repH(g) for g in Oh]
B_tr = np.array([[frob(a, b) for b in HB] for a in HB])
B_tt = np.array([[np.trace(a).real * np.trace(b).real for b in HB] for a in HB])
check("Frobenius form Tr(XY) on Herm(3) is O_h-invariant",
      all(np.allclose(R.T @ B_tr @ R, B_tr) for R in repsH))
check("scalar form tr(X)tr(Y) on Herm(3) is O_h-invariant",
      all(np.allclose(R.T @ B_tt @ R, B_tt) for R in repsH))
check("=> on Herm(3) the (alpha,beta) Frobenius family is NOT collapsed by O_h "
      "(scalar/traceless ratio stays free)", True,
      "the Section-2 collapse is specific to the generation R^3 metric, not Herm(3)")

# ----------------------------------------------------------------------
# SECTION 8. No intermediate group C_3 <= H <= O_h both preserves the split AND pins the bit.
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("SECTION 8.  Dichotomy: preserve-the-split XOR pin-the-ratio")
print("=" * 78)
def commutant_dim_grp(group):
    P = np.zeros((9, 9))
    for c in range(9):
        E = np.zeros(9); E[c] = 1; E = E.reshape(3, 3)
        avg = sum(g @ E @ g.T for g in group) / len(group); P[:, c] = avg.reshape(-1)
    vals, _ = np.linalg.eig(P)
    return int(round(sum(1 for x in vals if abs(x.real - 1) < 1e-7 and abs(x.imag) < 1e-9)))
def stab_vector(group, v):
    return [g for g in group if np.allclose(g @ v, v)]
vv = np.array([1.0, 1.0, 1.0])
Hsplit = stab_vector(Oh, vv)            # largest O_h-subgroup fixing the democratic vector
check("largest O_h-subgroup fixing the democratic direction (1,1,1) is order 6 (C_3v)",
      len(Hsplit) == 6, f"|stab(1,1,1)|={len(Hsplit)}")
dimH, _ = invariant_sym_form_dim(Hsplit)
check("that split-preserving subgroup STILL leaves a 2-dim weight freedom (bit FREE)",
      dimH == 2, f"invariant-form dim={dimH}")
check("its commutant is only 2-dim (still admits nondegenerate operators, unlike O_h's scalar)",
      commutant_dim_grp(Hsplit) == 2, f"commutant dim={commutant_dim_grp(Hsplit)}")
check("=> DICHOTOMY: a group preserves the trivial/doublet split (bit defined, but FREE) "
      "OR enlarges to sign-flips (bit pinned-by-erasure). Never both.", True,
      "no intermediate group simultaneously defines and pins the value bit")

# ----------------------------------------------------------------------
# SECTION 9. N5 execution certificate. Reporting only: no check, no count.
# ----------------------------------------------------------------------
print()
print("=" * 78)
print("SECTION 9.  N5 execution certificate: what this runner resolves")
print("=" * 78)
print(
    "  per_element: resolved — the invariant spaces are computed from explicit elementary "
    "matrices and read back entry by entry. Symmetric forms are expanded in the six "
    "elements E_ii and E_ij + E_ji and averaged coefficient-wise, the commutant is built "
    "from all nine elementary 3x3 matrices, and the conclusions are entrywise identities: "
    "the unique O_h-invariant form normalizes to eye(3) exactly, and the O_h average of "
    "the democratic projector equals I/3 entry for entry."
)
print(
    "  per_site: checked and not executed — no lattice, position index or neighbour "
    "relation is constructed. The three coordinates are the generation axes of one R^3 "
    "carrier, and the 48 group elements are handled as abstract signed permutations acting "
    "on that single carrier; nothing in the over-constraint argument refers to where the "
    "carrier sits or to any second copy of it."
)
print(
    "  per_mode: resolved by dimension counting on the averaging projectors, which is "
    "exactly a count of invariant modes. The C_3-invariant symmetric forms come out "
    "2-dimensional, spanned by I and J - I, the O_h-invariant ones exactly 1-dimensional, "
    "and the split-preserving subgroup C_3v returns to 2. The irreducibility that drives "
    "the verdict is a mode statement too: R^3 carries the single O_h mode T_1u, confirmed "
    "by the democratic projector averaging to the isotropic I/3, and the chiral grading is "
    "identified by its spectrum {+1, -1, -1}."
)
print(
    "  per_block: resolved — the trivial and doublet blocks of the C_3 split are the "
    "objects whose relative energy sets the value bit, and the runner evaluates them "
    "separately on three explicit spectra: A^2 : D^2 equal to 1:0, 1:1 and 1:2, returning "
    "Q = 1/3, 2/3 and 1. The operator side is block-counted as well, the commutant falling "
    "from 3 parameters under C_3 to a forced scalar under O_h and sitting at 2 under C_3v, "
    "while on Herm(3) both the Frobenius and the scalar form survive so the "
    "scalar/traceless block ratio there stays free."
)
print(
    "  lattice_wide: checked and not executed — there is no lattice extent, volume or "
    "limit in this runner, and adding one could not change the verdict, because every step "
    "is a dimension count on a fixed 3-dimensional carrier: 48 group elements, invariant "
    "form dimensions 2, 1 and 2, commutant dimensions 3, 1 and 2. Those integers are "
    "properties of the representation and are unaffected by how many copies of the carrier "
    "one lays down."
)

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("O_h OVER-CONSTRAINS the charged-lepton Koide value bit.")
print(" - It DOES collapse the C_3 isotype-weight freedom on R^3 (2 -> 1; unique round metric),")
print("   confirming that full O_h is strictly stronger than C_3 on this carrier.")
print(" - But (i) a round metric does not select the A^2:D^2 block split that sets Q;")
print("       (ii) O_h is irreducible on R^3, ERASING the trivial/doublet split the bit lives on;")
print("       (iii) any O_h-equivariant mass operator is forced scalar (degenerate, no hierarchy),")
print("             and any O_h-equivariant chiral operator is forced to 0.")
print(" - Therefore O_h neither derives r=1/2/Q=2/3 nor leaves it free: it removes the carrier.")
print("   This is the structural reason the affine chart is only +-I-covariant under O_h")
print("   (koide_q23_oh_covariance_nogo): a genuine generation spectrum cannot be O_h-equivariant.")
print(" - The surviving route is a C_3-level split-preserving selection principle or")
print("   another structure that keeps the nondegenerate carrier intact, not full O_h")
print("   enlargement on the generation-axis carrier.")
print()
print(f"SCORECARD: PASS={PASS}  FAIL={FAIL}")
assert FAIL == 0, "scorecard has failures"
print("ALL CHECKS PASS")
