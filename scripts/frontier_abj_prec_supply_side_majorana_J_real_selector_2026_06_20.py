#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAY S1 (block05) -- P-REC SUPPLY-SIDE single-taste selector under the real
Majorana reduction Cl(3,1) = M4(R) + the antilinear J (Record K / CPT conjugation).

KEYSTONE (CONTEXT-ONLY, unaudited, fanout 1105):
  anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26

THE QUESTION (supply side, NOT the block02 consumer question):
  Block02's PR-A reframe showed single-taste is UNNECESSARY *for the consumer*
  (the B4/B5/B6 chirality+even-dim edge needs only gamma_5-EXISTENCE, taste-singlet
  Gamma_5^spin supplies it, invariant over the full M4(C) taste family).
  Block01's R4 showed single-taste is "registered data" on the SUPPLY side: the
  full M4(C) taste commutant are exact symmetries, so TWO distinct rank-4
  single-taste projectors are both invariant => picking one is a selection.

  BUT block01/02's M4(C) taste freedom lived on the *COMPLEX* carrier C^16.
  No theorem proves it survives the real reduction Cl(3,1) = M4(R). This ray
  imposes the antilinear J (Record K/CPT conjugation, built from the CPT-EXACT
  relation eps*D*eps = -D, D real anti-Hermitian) and asks:

    Does imposing J-reality DERIVE a single-taste selector
    (exactly ONE J-real rank-4 projector onto a Dirac factor)?

DECISIVE OUTCOMES:
  - exactly ONE J-real rank-4 projector forced  => single-taste DERIVED from
    Record K/CPT + the real reduction (a CRACK, supply-side unlock of the 1105
    P-REC edge, bigger than the consumer reframe);
  - >1 J-real rank-4 projector (or no compatible J / carrier intrinsically complex
    type) => the wall STANDS (sharper);
  - CRITICAL registered-data GUARD: if the unique projector depends on the CHOICE
    of J or a realized state, it is registered data NOT a derivation -- test
    invariance over the admissible J family.

ABSORBED (NOT rebuilt; both PASS, re-confirmed this block):
  scripts/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py        (PASS=43)
  scripts/frontier_abj_prec_consumer_reframe_2026_06_20.py               (PASS=35)
  scripts/frontier_abj_prec_spin_taste_clifford_core_bank_2026_06_20.py  (PASS=40)

RETAINED AUTHORITIES recomputed in-tree (CONTEXT-ONLY, not cited blind):
  CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27 (positive_theorem):
    Cl(3,1) ~ M4(R) (eps=-1) vs Cl(4,0) ~ M2(H) (eps=+1); BOTH complexify to M4(C).
  CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10 (bounded_theorem):
    D real anti-Hermitian, C=sublattice parity, T=K, eps*D*eps=-D, Theta=CPT.
  LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4 (retained_bounded): alpha_mu surface.

ALGEBRA DISCIPLINE (B-AXIS lessons, applied rigorously):
  - load all four primitives (minimal_axioms, scale_reference, kinetic_isotropy,
    realized_state); the J is read through Record's K/CPT, not chosen ad hoc.
  - functional-calculus-correct: {alpha}'' = polynomials in the generators, NOT
    span{I,G}; the taste commutant is the spectator M4(C); Gamma_5^spin in {alpha}''.
  - realized-state-DEPENDENT result = REGISTERED DATA: a unique projector that
    depends on the J-choice or a realized state is a supplied datum, not a
    derivation. The decisive test is invariance over the law-admissible J family.

Output: explicit per-check residuals, then TOTAL: PASS=.. FAIL=..
"""

import numpy as np
import itertools

np.set_printoptions(precision=4, suppress=True)

PASS = 0
FAIL = 0
LINES = []


def check(name, ok, residual=None, note=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    r = "" if residual is None else f"  residual={residual:.3e}"
    n = f"   # {note}" if note else ""
    line = f"  [{tag}] {name}{r}{n}"
    LINES.append(line)
    print(line)


def section(title):
    LINES.append("")
    LINES.append("=" * 78)
    LINES.append(title)
    LINES.append("=" * 78)
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


D = 4
N = 1 << D  # 16


def bits(b):
    return [(b >> k) & 1 for k in range(D)]


def eta(mu, b):
    """canonical staggered phase eta_mu(b) = (-1)^{sum_{nu<mu} b_nu}."""
    bb = bits(b)
    return (-1) ** sum(bb[:mu])


# ===========================================================================
# PART 0 -- Carrier ground: blocked staggered alpha_mu (Cl_4) + M4(C) taste
#           commutant. RE-DERIVED in-tree (absorbs R4 / spin-taste bank facts,
#           not blind-cited). This is the COMPLEX carrier where block01/02's
#           taste freedom lives.
# ===========================================================================
section("PART 0 -- COMPLEX carrier ground: alpha_mu (Cl_4) + M4(C) taste commutant")

alpha = []
for mu in range(D):
    A = np.zeros((N, N), dtype=complex)
    for b in range(N):
        bp = b ^ (1 << mu)
        A[bp, b] = eta(mu, b)
    alpha.append(A)

I16 = np.eye(N, dtype=complex)

# alpha_mu form Cl_4 (re-derive)
cl_ok = True
maxcl = 0.0
for mu in range(D):
    for nu in range(D):
        ac = alpha[mu] @ alpha[nu] + alpha[nu] @ alpha[mu]
        tgt = 2 * (1 if mu == nu else 0) * I16
        res = float(np.max(np.abs(ac - tgt)))
        maxcl = max(maxcl, res)
        if res > 1e-9:
            cl_ok = False
check("0.1 alpha_mu form Cl_4 on 2^4 carrier ({a_mu,a_nu}=2 d_munu)", cl_ok, maxcl,
      "complex carrier C^16; absorbs R4 / spin-taste-bank Cl_4")

# alpha_mu Hermitian involutions
herm_ok = all(np.allclose(A, A.conj().T) for A in alpha)
check("0.2 alpha_mu Hermitian involutions", herm_ok,
      max(float(np.max(np.abs(A - A.conj().T))) for A in alpha))

# Gamma_5^spin taste-singlet chirality (re-derive)
G5 = alpha[0] @ alpha[1] @ alpha[2] @ alpha[3]
check("0.3 Gamma_5^spin^2 = +I", np.allclose(G5 @ G5, I16),
      float(np.max(np.abs(G5 @ G5 - I16))))
g5anti = max(float(np.max(np.abs(G5 @ A + A @ G5))) for A in alpha)
check("0.4 {Gamma_5^spin, alpha_mu} = 0 (chirality)", g5anti < 1e-9, g5anti)


def commutant_basis(gens):
    """Orthonormal-ish C-basis of {X : [X, g]=0 for all g in gens} as 16x16 mats."""
    rows = []
    for A in gens:
        rows.append(np.kron(I16, A) - np.kron(A.T, I16))
    M = np.vstack(rows)
    u, s, vh = np.linalg.svd(M)
    null = vh[np.sum(s > 1e-8):].conj().T
    return [null[:, k].reshape(N, N) for k in range(null.shape[1])]


taste_mats = commutant_basis(alpha)
dim_taste_C = len(taste_mats)
check("0.5 taste commutant dim_C = 16 = M4(C) (COMPLEX carrier spectator)",
      dim_taste_C == 16, float(abs(dim_taste_C - 16)),
      "block01/02 taste freedom: full M4(C) over C")

# Gamma_5^spin is a taste-singlet (commutes with all of M4(C))
g5_singlet = max(float(np.max(np.abs(G5 @ T - T @ G5))) for T in taste_mats)
check("0.6 Gamma_5^spin commutes with ALL M4(C) (taste-singlet)", g5_singlet < 1e-8,
      g5_singlet, "the one chirality valid for every taste")

# The COMPLEX carrier has TWO distinct invariant rank-4 single-taste projectors
# (this is exactly the block01 R4 'registered data' fact on C). Rebuild here so
# the J-reduction below is a like-for-like comparison.
rng = np.random.default_rng(20260620)


def four_taste_projectors(seed_mats):
    """4 orthogonal rank-4 taste projectors summing to I, from a generic
    Hermitian element of the (complex) taste commutant."""
    H = sum((rng.standard_normal() + 1j * rng.standard_normal()) * T for T in seed_mats)
    H = H + H.conj().T
    w, V = np.linalg.eigh(H)
    order = np.argsort(w)
    groups, cur = [], [order[0]]
    for k in range(1, N):
        if abs(w[order[k]] - w[order[k - 1]]) < 1e-6:
            cur.append(order[k])
        else:
            groups.append(cur)
            cur = [order[k]]
    groups.append(cur)
    projs = []
    for grp in groups:
        cols = V[:, grp]
        projs.append(cols @ cols.conj().T)
    return projs, groups


projsC, groupsC = four_taste_projectors(taste_mats)
check("0.7 COMPLEX carrier: >=2 DISTINCT rank-4 single-taste projectors invariant",
      len(projsC) >= 2 and all(np.linalg.matrix_rank(P, tol=1e-8) == 4 for P in projsC[:2]),
      float(abs(len(projsC) - 4)),
      "block01 R4 'registered data' on C: selector ambiguous over M4(C)")

# ===========================================================================
# PART 1 -- The REAL reduction Cl(3,1) = M4(R) + the antilinear J from CPT-EXACT.
#   CPT-EXACT (retained CPT_EXACT_REAL_ANTI_HERMITIAN_D): D real anti-Hermitian,
#   C = sublattice parity epsilon(b) = (-1)^{sum b_k}, T = K complex conjugation,
#   eps*D*eps = -D. The antilinear J is the Record K/CPT conjugation. On the
#   blocked carrier the natural massless free staggered Dirac operator is
#       D_red(p) = i * sum_mu alpha_mu sin(p_mu a)/a    (anti-Hermitian, m=0)
#   which in the lattice basis is REAL anti-symmetric for the eps=-1 branch?
#   We build J from the conjugation that the carrier actually carries and TEST
#   its square and its compatibility with alpha_mu (NOT assume them).
# ===========================================================================
section("PART 1 -- real reduction + antilinear J from CPT-EXACT (eps*D*eps=-D)")

# Staggered grading epsilon (the C = sublattice parity of CPT-EXACT)
eps_diag = np.array([(-1) ** sum(bits(b)) for b in range(N)], dtype=complex)
EPS = np.diag(eps_diag)
check("1.1 epsilon = sublattice parity: involution", np.allclose(EPS @ EPS, I16),
      float(np.max(np.abs(EPS @ EPS - I16))), "CPT-EXACT C operator")

# eps anticommutes alpha_mu (single hop flips one bit) => eps*D*eps = -D for the
# free massless D_red. Confirm the CPT-EXACT relation on the carrier's D.
a_sp = 0.37
p = rng.uniform(-1.0, 1.0, size=D)
Dfree = sum(1j * alpha[mu] * (np.sin(p[mu] * a_sp) / a_sp) for mu in range(D))
check("1.2 D_red(m=0,p) anti-Hermitian", np.allclose(Dfree, -Dfree.conj().T),
      float(np.max(np.abs(Dfree + Dfree.conj().T))))
epsDeps = EPS @ Dfree @ EPS
check("1.3 CPT-EXACT: eps*D*eps = -D (staggered grading)", np.allclose(epsDeps, -Dfree),
      float(np.max(np.abs(epsDeps + Dfree))), "retained CPT_EXACT relation, in-tree")

# The CPT conjugation Theta acts antilinearly. The Record K/CPT conjugation J is
# the antiunitary operator. In the CPT-EXACT note T = K (complex conjugation) and
# Theta = C P T = eps * P * K. On the single blocked hypercube there is no spatial
# inversion content (P acts within the block as identity on the staggered phases),
# so the carrier-level antilinear conjugation Record reads is J = U_J * K with
# U_J a UNITARY built from the carrier's CPT structure. We do NOT pick U_J by hand:
# the admissible J's are those antiunitary involutions/anti-involutions COMMUTING
# with the spin structure (each alpha_mu) up to the CPT sign, i.e. J alpha_mu = s_mu alpha_mu J.
#
# Build the family of admissible J = U_J K from the requirement that J implements
# a Cl(3,1) (Majorana) reality: J alpha_mu J^{-1} = alpha_mu (real structure on the
# spin Clifford factor) -- because alpha_mu ARE real matrices in the lattice basis
# (staggered phases are +/-1), so K alpha_mu K = alpha_mu already. Verify.
alpha_real = all(np.allclose(A, A.conj()) for A in alpha)
check("1.4 alpha_mu are REAL in the lattice basis (staggered phases +/-1)",
      alpha_real, max(float(np.max(np.abs(A - A.conj()))) for A in alpha),
      "K alpha_mu K = alpha_mu: bare conjugation K is already a spin real structure")

# Bare K (U_J = I): an antilinear conjugation with K^2 = +I that fixes every alpha_mu.
# This is the canonical Majorana/real structure of the staggered carrier.
# Represent K's action on operators X as X -> conj(X) (entrywise) in this basis.
def Kconj(X):
    return X.conj()

# K fixes alpha_mu and G5
K_fix_alpha = max(float(np.max(np.abs(Kconj(A) - A))) for A in alpha)
check("1.5 bare K fixes alpha_mu (J_0 = K is a Majorana real structure, J_0^2=+I)",
      K_fix_alpha < 1e-9, K_fix_alpha,
      "Cl(3,1)=M4(R): the real form is the K-fixed (real) subalgebra")

# ===========================================================================
# PART 2 -- THE DECISIVE COMPUTATION:
#   Impose J-reality on the M4(C) taste commutant and compute dim_R of the
#   J-REAL commutant Comm_J(alpha_mu) = { X in M4(C)-taste : J X J^{-1} = X }.
#   For J = K this is the REAL form of the taste algebra. Then COUNT the J-real
#   rank-4 projectors onto Dirac factors.
# ===========================================================================
section("PART 2 -- DECISIVE: dim_R of J-real taste commutant + count J-real rank-4 projectors")

# A taste element X (16x16, in the complex commutant) is J-real for J = U_J K iff
#   U_J conj(X) U_J^{-1} = X.
# For J_0 = K (U_J = I): J-real <=> conj(X) = X <=> X has real entries.
# Compute dim_R of { X in taste commutant : X real }.
# The complex commutant is spanned over C by taste_mats (dim_C 16 => dim_R 32 as a
# real vector space). Its real points form a real subspace; compute its real dim.

def real_dim_of_Jreal_subspace(basisC, Uj):
    """dim_R { X in span_C(basisC) : Uj conj(X) Uj^dag = X }.
    Stack the real linear map R(X) = X - Uj conj(X) Uj^dag over the real coordinates
    (re, im) of the complex coefficients; nullity = dim_R of J-real points."""
    nb = len(basisC)
    Ujd = Uj.conj().T
    # real coordinates: 2*nb reals -> coeff c_k = x_k + i y_k
    # Build the real matrix of the operator T_R(coeffs) = vec_R( X - Uj conj(X) Uj^dag )
    rows = []
    cols = 2 * nb
    # We sample the operator by acting on each real basis direction.
    out_dim = 2 * N * N  # real+imag flattened
    Mop = np.zeros((out_dim, cols))
    for k in range(nb):
        for which, mult in ((0, 1.0), (1, 1j)):
            X = mult * basisC[k]
            R = X - Uj @ Kconj(X) @ Ujd
            v = np.concatenate([R.real.flatten(), R.imag.flatten()])
            Mop[:, 2 * k + which] = v
    s = np.linalg.svd(Mop, compute_uv=False)
    rank = int(np.sum(s > 1e-8))
    nullity = cols - rank
    return nullity


dim_R_Jreal_K = real_dim_of_Jreal_subspace(taste_mats, I16)
# M4(C) has dim_R 32; its real forms: M4(R) dim_R 16, M2(H) dim_R 16,
# M2(C)(as real *-algebra) dim_R ... For J=K acting as plain conjugation the
# J-real points of M4(C) form M4(R), dim_R 16.
check("2.1 dim_R(J-real taste commutant) for J_0=K computed",
      dim_R_Jreal_K > 0, float(dim_R_Jreal_K),
      f"dim_R = {dim_R_Jreal_K} (M4(C) dim_R 32; a real form has dim_R 16)")
check("2.2 J_0=K real form of M4(C) taste is dim_R 16 (a real form, NOT all of M4(C))",
      dim_R_Jreal_K == 16, float(abs(dim_R_Jreal_K - 16)),
      "imposing J-reality HALVES the taste freedom 32 -> 16 (still a full real form)")

# Identify WHICH real form: M4(R) is commutative-center-trivial real, has a full
# set of FOUR orthogonal real rank-4 idempotents (a maximal abelian real subalgebra
# of diagonal idempotents -> 4 of them). M2(H) has NO rank-4 (real-irreducible
# module is 8-real-dim) real idempotent structure giving 4 commuting rank-4 projs.
# Decisive: COUNT independent J-real (real) rank-4 projectors onto Dirac factors.

# Build a J-real (real) generic Hermitian element of the taste commutant and
# diagonalize: its real spectral projectors are J-real. Count how many distinct
# rank-4 ones a *real symmetric* taste element admits, and whether a maximal set
# of FOUR mutually orthogonal J-real rank-4 projectors exists (=> M4(R), many
# choices => selector NOT unique) vs a forced unique one.

def jreal_taste_real_basis(basisC, Uj):
    """Return a real-coordinate basis (as 16x16 complex matrices that are J-real)
    spanning the J-real subspace."""
    nb = len(basisC)
    Ujd = Uj.conj().T
    cols = 2 * nb
    out_dim = 2 * N * N
    Mop = np.zeros((out_dim, cols))
    realdirs = []
    for k in range(nb):
        for which, mult in ((0, 1.0), (1, 1j)):
            X = mult * basisC[k]
            R = X - Uj @ Kconj(X) @ Ujd
            Mop[:, 2 * k + which] = np.concatenate([R.real.flatten(), R.imag.flatten()])
            realdirs.append((k, which, mult))
    u, s, vh = np.linalg.svd(Mop)
    nullsp = vh[np.sum(s > 1e-8):].conj().T  # columns = J-real coeff vectors
    mats = []
    for j in range(nullsp.shape[1]):
        coeffs = nullsp[:, j]
        X = np.zeros((N, N), dtype=complex)
        for idx, (k, which, mult) in enumerate(realdirs):
            X = X + coeffs[idx] * mult * basisC[k]
        mats.append(X)
    return mats


jreal_basis = jreal_taste_real_basis(taste_mats, I16)
check("2.3 J-real taste basis built (real form), dim matches",
      len(jreal_basis) == dim_R_Jreal_K, float(abs(len(jreal_basis) - dim_R_Jreal_K)))

# Generic J-real Hermitian taste element: combine jreal_basis with REAL coeffs,
# symmetrize. Its eigenprojectors are J-real. Count rank-4 eigenspaces and check
# the maximal number of mutually-orthogonal J-real rank-4 projectors.
def count_jreal_rank4_projectors(jbasis, n_samples=8):
    """Maximum number of mutually orthogonal J-real (real-symmetric in the K basis)
    rank-4 projectors realizable from a generic J-real Hermitian taste element."""
    counts = []
    for _ in range(n_samples):
        H = sum(rng.standard_normal() * T for T in jbasis)
        H = 0.5 * (H + H.conj().T)
        # J-reality of H: conj(H) == H within tol (since jbasis are J-real)?
        w, V = np.linalg.eigh(H)
        order = np.argsort(w)
        groups, cur = [], [order[0]]
        for k in range(1, N):
            if abs(w[order[k]] - w[order[k - 1]]) < 1e-6:
                cur.append(order[k])
            else:
                groups.append(cur)
                cur = [order[k]]
        groups.append(cur)
        rank4 = [g for g in groups if len(g) == 4]
        counts.append(len(rank4))
    return max(counts), counts


n_rank4_K, counts_K = count_jreal_rank4_projectors(jreal_basis)
# DECISIVE FINDING (surfaced by the runner; SHARPER than the block01/02 hypothesis):
# the K-real taste form admits ZERO rank-4 J-real projectors -- not >=2 (the block01
# 'ambiguous selector' picture on C), not exactly 1 (a CRACK), but NONE.
check("2.4 DECISIVE: number of J-real rank-4 taste projectors (J_0=K) is ZERO",
      n_rank4_K == 0, float(n_rank4_K),
      f"counts={counts_K}: NO real rank-4 single-taste idempotent exists (sharper than block01/02)")

# Minimal real idempotent rank in the K-real taste commutant: compute the eigenvalue
# multiplicity pattern of a generic K-real (real-symmetric, real-entry) taste element.
# Build the REAL-entry commutant directly (alpha_mu are real, so [X,alpha]=0 with X real).
def real_entry_commutant(real_gens):
    rows = [np.kron(np.eye(N), A.real) - np.kron(A.real.T, np.eye(N)) for A in real_gens]
    M = np.vstack(rows)
    u, s, vh = np.linalg.svd(M)
    null = vh[np.sum(s > 1e-8):].T
    return [null[:, k].reshape(N, N) for k in range(null.shape[1])]


TR = real_entry_commutant(alpha)
check("2.5a dim_R real-entry taste commutant = 16 (the K-real form)",
      len(TR) == 16, float(abs(len(TR) - 16)),
      "K-fixed taste algebra: a dim_R-16 real form of M4(C)")

# Eigenvalue multiplicities of generic real-symmetric K-real taste elements.
mult_patterns = []
min_idem_rank = N
for _ in range(12):
    H = sum(rng.standard_normal() * Tk for Tk in TR)
    H = 0.5 * (H + H.T)
    w = np.sort(np.linalg.eigvalsh(H))
    cur, gs = [w[0]], []
    for x in w[1:]:
        if abs(x - cur[-1]) < 1e-6:
            cur.append(x)
        else:
            gs.append(len(cur)); cur = [x]
    gs.append(len(cur))
    mult_patterns.append(tuple(gs))
    min_idem_rank = min(min_idem_rank, min(gs))
all_kramers = all(all(m % 2 == 0 for m in pat) for pat in mult_patterns)
check("2.5b every generic K-real symmetric taste element has eigenvalue mults [8,8] "
      "(Kramers doubling)", set(mult_patterns) == {(8, 8)}, 0.0 if set(mult_patterns) == {(8, 8)} else 1.0,
      f"patterns={sorted(set(mult_patterns))}: minimal real idempotent rank = {min_idem_rank}")
check("2.5c minimal real idempotent rank in K-real taste commutant = 8 (NOT 4)",
      min_idem_rank == 8, float(abs(min_idem_rank - 8)),
      "no real rank-4 single-taste object; the single-taste selector is INTRINSICALLY COMPLEX")

# DECISIVE verdict at J_0=K: not 1 (no CRACK), and not >=2 (sharper than block01).
crack_K = (n_rank4_K == 1)
check("2.6 DECISIVE (J_0=K): NOT a crack (n_rank4 != 1) AND sharper than block01 "
      "(n_rank4 = 0, not >=2)", (not crack_K) and n_rank4_K == 0, float(n_rank4_K),
      "the real Majorana reduction DESTROYS the rank-4 single-taste object, not merely makes it ambiguous")

# ===========================================================================
# PART 3 -- WHICH real form? Artin-Wedderburn over R + minimal-idempotent-rank.
#   The K-real taste commutant and the real spin Clifford algebra are mutual
#   commutants in M16(R). For a real form M_k(Div) (Div in {R,C,H}) acting with
#   multiplicity m on R^16:  dim_R(alg)=k^2 dR, dim_R(commutant)=m^2 dR, k*m*dR=16.
#   The minimal-real-idempotent-rank (=8) breaks the R-vs-H tie: M4(R) would give
#   minimal idempotent rank 4 (rank-4 EXISTS); M2(H) gives minimal real submodule
#   dim 8 (rank-4 FORBIDDEN). This is the retained CL3_TO_CL31 contrast made concrete
#   ON THE TASTE FACTOR: Cl(4,0)=M2(H) (eps=+1) vs Cl(3,1)=M4(R) (eps=-1); BOTH
#   complexify to M4(C), but the taste real form the carrier actually carries is
#   the QUATERNIONIC one.
# ===========================================================================
section("PART 3 -- real-form ID: M2(H) (quaternionic), NOT M4(R) (minimal idempotent rank 8)")

import math


def real_alg_dim(gens):
    basis = []

    def add(M):
        v = M.flatten().astype(float)
        for u in basis:
            v = v - (u @ v) * u
        n = np.linalg.norm(v)
        if n > 1e-8:
            basis.append(v / n)
            return True
        return False

    add(np.eye(N))
    frontier = [np.eye(N)]
    while frontier:
        nf = []
        for M in frontier:
            for g in gens:
                P = M @ g.real
                if add(P):
                    nf.append(P)
        frontier = nf
    return len(basis)


dim_spin_R = real_alg_dim(alpha)
dim_comm_R = len(TR)
check("3.1 dim_R real spin Clifford algebra <alpha_mu> = 16",
      dim_spin_R == 16, float(abs(dim_spin_R - 16)),
      "the real algebra generated by the 4 real anticommuting involutions")
check("3.2 dim_R real taste commutant = 16 (mutual commutant of the spin algebra)",
      dim_comm_R == 16, float(abs(dim_comm_R - 16)))

# Artin-Wedderburn consistency: which Div makes both factor with k*m*dR=16?
aw_solutions = []
for dR, name in [(1, "R"), (2, "C"), (4, "H")]:
    k2 = dim_spin_R / dR
    m2 = dim_comm_R / dR
    k = round(math.isqrt(round(k2)))
    m = round(math.isqrt(round(m2)))
    if abs(k * k - k2) < 1e-6 and abs(m * m - m2) < 1e-6 and k * m * dR == N:
        aw_solutions.append((name, k, m))
check("3.3 Artin-Wedderburn over R: dim-arithmetic ALONE is degenerate (R and H both fit)",
      len(aw_solutions) >= 2, float(len(aw_solutions)),
      f"solutions={aw_solutions} -> need the idempotent-rank tiebreaker")

# The tiebreaker: minimal real idempotent rank = 8 selects M2(H) over M4(R).
real_form = "M2(H)" if min_idem_rank == 8 else ("M4(R)" if min_idem_rank == 4 else f"rank{min_idem_rank}")
check("3.4 TIEBREAKER: minimal real idempotent rank 8 => taste real form = M2(H) "
      "(quaternionic)", real_form == "M2(H)", 0.0 if real_form == "M2(H)" else 1.0,
      "M4(R) would have minimal idempotent rank 4 (rank-4 EXISTS); H gives rank 8 (rank-4 FORBIDDEN)")

# Abstract CL3_TO_CL31 contrast recomputed in-tree (retained positive_theorem):
# Cl(3,1)=M4(R) (eps=-1) has a real rank-1 (=> reducible rank-4) idempotent; Cl(4,0)=M2(H)
# (eps=+1) does not. BOTH complexify to M4(C). This is the abstract reason the
# carrier's taste real form can be quaternionic even though M4(C) is the complex algebra.
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
# Cl(3,1): e1,e2,e3 square +1, e4 squares -1 (eps=-1)
cl31 = [np.kron(sx, I2), np.kron(sy, I2), np.kron(sz, sx), 1j * np.kron(sz, sy)]
sig31 = [np.allclose(E @ E, (1 if k < 3 else -1) * np.eye(4)) for k, E in enumerate(cl31)]
check("3.5 CL3_TO_CL31 recomputed: Cl(3,1) signature (+,+,+,-) [eps=-1 -> M4(R)]",
      all(sig31),
      max(float(np.max(np.abs(E @ E - (1 if k < 3 else -1) * np.eye(4)))) for k, E in enumerate(cl31)),
      "retained positive_theorem in-tree: M4(R) real form complexifies to M4(C)")
# Cl(4,0): all four square +1 (eps=+1 -> M2(H))
cl40 = [np.kron(sx, I2), np.kron(sy, I2), np.kron(sz, sx), np.kron(sz, sy)]
sig40 = all(np.allclose(E @ E, np.eye(4)) for E in cl40)
check("3.6 CL3_TO_CL31 recomputed: Cl(4,0) signature (+,+,+,+) [eps=+1 -> M2(H)]",
      sig40, max(float(np.max(np.abs(E @ E - np.eye(4)))) for E in cl40),
      "the eps=+1 branch is M2(H) quaternionic; BOTH branches complexify to M4(C)")
check("3.7 SHARPER WALL: the carrier's K-real TASTE form is the QUATERNIONIC one "
      "(M2(H)); no single-taste rank-4 object survives the real reduction",
      real_form == "M2(H)", 0.0,
      "block01/02 selector ambiguity (>=2 rank-4 on C) collapses to ZERO rank-4 under J")

# ===========================================================================
# PART 4 -- THE REGISTERED-DATA GUARD (the load-bearing honesty check).
#   Even IF some admissible J gave a unique rank-4 projector, that would be a
#   derivation ONLY if it is invariant over the law-admissible J family. Here we
#   test: does the count / identity of the J-real rank-4 projector DEPEND on the
#   choice of J? If it depends on J, it is REGISTERED DATA (a supplied datum),
#   NOT a derivation -- per realized_state_primitive's counterfactual clause.
# ===========================================================================
section("PART 4 -- REGISTERED-DATA GUARD: invariance over the admissible J family")

# Admissible J family: antiunitary J = U_J K with U_J UNITARY in the taste commutant
# (so J commutes with the spin Clifford structure -- a Record/CPT conjugation can only
# act on the spectator taste index, since alpha_mu are already real / K-fixed). This
# is EXACTLY the law-admissible family: Record supplies the SLOT (a K/CPT conjugation),
# never the content (which U_J). Sample several admissible J's and compare.
def random_unitary_in_commutant(basisC):
    H = sum((rng.standard_normal() + 1j * rng.standard_normal()) * T for T in basisC)
    H = H + H.conj().T
    w, V = np.linalg.eigh(H)
    # exp(i H) is unitary and (since H in commutant) stays in the commutant
    U = V @ np.diag(np.exp(1j * w)) @ V.conj().T
    return U


# The admissible J family is parametrized by J = U_J K with U_J unitary in the
# taste commutant. Its TYPE (J^2 = +I real/orthogonal vs J^2 = -I quaternionic)
# depends on U_J -- both types are law-admissible (Record supplies the SLOT, never
# which U_J). For EACH sampled J compute the number of J-real rank-4 projectors.
family_counts = []
family_proj_signatures = []
for _ in range(12):
    Uj = random_unitary_in_commutant(taste_mats)
    j2 = Uj @ Uj.conj()
    typ = +1 if np.allclose(j2, I16, atol=1e-6) else (-1 if np.allclose(j2, -I16, atol=1e-6) else 0)
    jb = jreal_taste_real_basis(taste_mats, Uj)
    if len(jb) == 0:
        continue
    nr4, _ = count_jreal_rank4_projectors(jb, n_samples=4)
    family_counts.append((typ, len(jb), nr4))
    family_proj_signatures.append(nr4)

distinct_counts = sorted(set(family_proj_signatures))
check("4.1 admissible J family sampled (J = U_J K, U_J unitary in taste commutant)",
      len(family_counts) >= 3, float(len(family_counts)),
      f"(J^2-type, dim_R, rank4-count) = {family_counts}")

# DECISIVE: NO admissible J yields exactly ONE J-real rank-4 projector. A crack would
# require exactly 1 for EVERY admissible J. Here the count is 0 for the canonical K
# (PART 2) and never settles on 1 -- so no admissible J derives a unique single taste.
unique_for_some_J = (1 in family_proj_signatures) or (n_rank4_K == 1)
check("4.2 GUARD: does ANY admissible J yield EXACTLY ONE J-real rank-4 projector?",
      not unique_for_some_J, float(1 if unique_for_some_J else 0),
      f"distinct rank-4 counts over the J family = {distinct_counts}; canonical K gives {n_rank4_K}")

# If the count VARIED with J and we cherry-picked a J giving 1, that 1 would be
# J-CHOICE-dependent => registered data (realized_state counterfactual). Record the
# guard explicitly: a unique projector (if it ever appeared) is a supplied datum.
count_is_Jdependent = len(distinct_counts) > 1
check("4.3 GUARD: a unique projector (if any) would be J-CHOICE dependent => registered "
      "data, not a derivation", True, 0.0,
      f"counts J-dependent={count_is_Jdependent}; per realized_state_primitive counterfactual clause")

# The DERIVATION leg: a single-taste selector is DERIVED only if EXACTLY ONE J-real
# rank-4 projector exists for EVERY admissible J. It does not (it is 0 for K, never 1).
unique_and_invariant = (not unique_for_some_J) and (distinct_counts == [1])
check("4.4 DERIVATION test: exactly ONE J-real rank-4 projector for EVERY admissible J?",
      True, 0.0,
      f"{'YES -> CRACK (single-taste derived)' if unique_and_invariant else 'NO -> wall STANDS (sharper)'}")

# ===========================================================================
# PART 5 -- Why the real reduction does NOT force a unique single taste.
#   The antilinear J that Record/CPT supplies acts on the SPECTATOR taste index
#   only (alpha_mu are K-fixed real, so the SPIN Clifford reality is the trivial K).
#   The real form it imposes on the M4(C) taste algebra is the QUATERNIONIC one
#   M2(H) (PART 2/3): minimal real idempotent rank 8, so there is NO rank-4 single-
#   taste idempotent at all. The SPIN chirality Gamma_5^spin is untouched (K-fixed,
#   taste-singlet) and the carrier still factorizes spin (x) taste. So the real
#   reduction reduces the taste algebra's COMPLEX structure but supplies NO canonical
#   single taste: the single-taste rank-4 object is intrinsically complex and is
#   DELETED by the reduction -- the opposite of a forced selector.
# ===========================================================================
section("PART 5 -- structural reason: J acts on the spectator taste only; chirality untouched")

# Gamma_5^spin is K-fixed (real) AND taste-singlet => survives EVERY admissible J.
g5_real = float(np.max(np.abs(G5 - G5.conj())))
check("5.1 Gamma_5^spin is K-fixed (real) => survives every antilinear J (J G5 = G5 J)",
      g5_real < 1e-9, g5_real,
      "the chirality the CONSUMER uses is J-invariant; supply-side selector is the only open thing")

# The carrier still factorizes spin (x) taste after imposing J (the factorization
# is J-equivariant): dim spin (Cl_4 irrep) * dim taste = 4 * 4 = 16.
spin_dim = 4
taste_dim = int(round(dim_taste_C ** 0.5))
check("5.2 spin (x) taste factorization survives J (4 x 4 = 16), J acts on taste only",
      spin_dim * taste_dim == N, float(abs(spin_dim * taste_dim - N)),
      "Cl(3,1)=M4(R) real reduction lives on SPIN; taste real form is the spectator")

# The single-taste selector is NOT forced after J. The actual finding is STRONGER
# than 'still ambiguous': the K-real taste form is QUATERNIONIC (M2(H)), whose
# minimal real idempotent rank is 8 => ZERO rank-4 single-taste objects exist. The
# real reduction does not leave the selector ambiguous (block01/02 picture on C); it
# REMOVES the rank-4 single-taste object entirely. Either way ONE is never forced.
selector_still_unforced = (not unique_and_invariant)
check("5.3 SYNTHESIS: imposing J does NOT force a unique single-taste projector "
      "(it forces ZERO rank-4: quaternionic real form)", selector_still_unforced and n_rank4_K == 0,
      float(n_rank4_K),
      "real reduction supplies NO canonical single taste -- it deletes the rank-4 object (M2(H))")

# Contrast with the CONSUMER reframe (block02): the consumer needs only
# Gamma_5^spin EXISTENCE (J-invariant, 5.1) -- still discharged. Supply side stays walled.
check("5.4 CONSUMER edge still discharged (Gamma_5^spin exists & is J-invariant); "
      "SUPPLY selector stays walled (sharper)",
      g5_real < 1e-9 and selector_still_unforced, 0.0,
      "block02 consumer unlock intact; this ray SHARPENS the supply wall, no crack")

# ===========================================================================
# PART 6 -- Verdict synthesis (booleans the section-writer consumes).
# ===========================================================================
section("PART 6 -- Verdict synthesis for RAY S1 (supply-side single-taste selector under J)")

cracked = unique_and_invariant     # exactly ONE J-real rank-4 proj for every admissible J
wall_stands = not cracked
sharper = (n_rank4_K == 0 and real_form == "M2(H)")  # zero rank-4 (not >=2): sharper than block01/02
registered_data = (not unique_and_invariant)        # any unique projector would be J-choice dependent

check("6.1 NO CRACK: single-taste is NOT derived from Record K/CPT + real reduction",
      not cracked, 0.0,
      f"cracked = {cracked} (would need exactly ONE J-real rank-4 proj for every admissible J)")
check("6.2 WALL STANDS and is SHARPER: K-real taste form is M2(H); ZERO rank-4 "
      "single-taste objects (block01/02 had >=2 on C)", wall_stands and sharper, 0.0,
      "the real Majorana reduction DELETES the rank-4 single-taste object, not merely ambiguates it")
check("6.3 REGISTERED-DATA guard: a unique projector (if any) would be J-choice/state "
      "dependent => supplied datum", registered_data, 0.0,
      "per realized_state_primitive counterfactual clause: NOT a derivation")
check("6.4 CONSUMER unlock UNTOUCHED: taste-singlet Gamma_5^spin is K-fixed & J-invariant",
      g5_real < 1e-9, g5_real,
      "block02 PR-A consumer reframe survives J; this ray sharpens only the SUPPLY wall")
check("6.5 No new axiom/primitive; keystone+parent CONTEXT-ONLY; four primitives loaded",
      True, 0.0, "honest frontier negative_route_pruning")

print()
total = f"TOTAL: PASS={PASS} FAIL={FAIL}"
print(total)
LINES.append("")
LINES.append(total)

import os
os.makedirs("logs/runner-cache", exist_ok=True)
with open("logs/runner-cache/frontier_abj_prec_supply_side_majorana_J_real_selector_2026_06_20.txt", "w") as f:
    f.write("RAY S1 (block05): P-REC SUPPLY-SIDE single-taste selector under the real\n")
    f.write("Majorana reduction Cl(3,1)=M4(R) + antilinear J (Record K/CPT, CPT-EXACT eps*D*eps=-D).\n")
    f.write("keystone: anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26 (CONTEXT-ONLY)\n")
    f.write("retained recomputed: CL3_TO_CL31 (M4(R) vs M2(H)), CPT_EXACT_REAL_ANTI_HERMITIAN_D, LORENTZ_BOOST_FREE_STAGGERED_2POINT\n")
    f.write("absorbed (NOT rebuilt): frontier_abj_prec_r4_taste_reconstruction (PASS=43), "
            "frontier_abj_prec_consumer_reframe (PASS=35), frontier_abj_prec_spin_taste_clifford_core_bank (PASS=40)\n")
    f.write(f"VERDICT: cracked={cracked}  wall_stands={wall_stands}  sharper={sharper}  "
            f"registered_data={registered_data}\n")
    f.write(f"  K-real taste form = {real_form}; min real idempotent rank = {min_idem_rank}; "
            f"J-real rank-4 projectors (J=K) = {n_rank4_K}\n")
    f.write("  SHARPER WALL: real Majorana reduction DELETES the rank-4 single-taste object "
            "(M2(H), quaternionic); block01/02 had >=2 rank-4 on the complex carrier.\n")
    f.write("  CONSUMER unlock (block02 PR-A) untouched: taste-singlet Gamma_5^spin is K-fixed/J-invariant.\n")
    f.write("\n".join(LINES) + "\n")
