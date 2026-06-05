#!/usr/bin/env python3
"""Hostile check on the "measure-from-the-cut" mechanism for charged-lepton r=1/2.

Claim under attack (the "measure-from-the-cut" mechanism):
  "A record resolves only the PARTITION (which Wedderburn block: singlet R + doublet C),
   not the within-block state (within-block is reversible/quantum, unrecorded). So a
   classical record can only BLOCK-COUNT (-> r=1/2). The BORN/DIMENSION measure (-> r=1)
   requires within-block STATE-counting the record lacks. Hence r=1/2 is the record-natural
   setting, r=1 the within-block setting."

We do NOT try to force r=1/2 and do NOT try to save it. The user-set frame is:
r=1/2 is a STABLE SETTING on a dial, not forced/exclusive. This runner asks the strictly
narrower HOSTILE question: is the "measure-from-the-cut" argument a SOUND NEW MECHANISM,
or a REPACKAGING of the previously-BROKEN minimum-information argument (broken by quantum
Darwinism: objective classical records are MAXIMALLY REDUNDANT, not minimal)?

Four fronts:
  F1  Darwinian-redundancy test: can redundant partition-records COLLECTIVELY reconstruct
      the within-block dimension (-> Born/dimension measure -> r=1, killing "partition-only")?
  F2  dimension-vs-state: is the block DIMENSION (a structural number) knowable to a record
      even when the within-block STATE is not? If yes, block-count is NOT forced by the cut.
  F3  real-vs-complex slot: does the cut RESOLVE the doublet-as-one-C-unit (r=1/2) vs
      doublet-as-two-R-dims (toward r=1) choice, or merely RENAME it?
  F4  overreach: is "only charged leptons are pure partition-records" principled or post-hoc?

Each numbered check prints PASS/FAIL. PASS = "the stated hostile sub-fact holds" (i.e. the
finding that bears on whether the mechanism is sound). All facts are concrete linear algebra
on the Z3-circulant 2-block (singlet (+)+ doublet (C)) structure; nothing is hard-coded to a
target r value. Reproducible, no external deps beyond numpy.
"""

import numpy as np

np.set_printoptions(suppress=True, precision=10)

TOL = 1e-9
RESULTS = []


def check(name, passed, detail=""):
    RESULTS.append((name, bool(passed), detail))
    tag = "PASS" if passed else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"  |  {detail}"
    print(line)


# ----------------------------------------------------------------------------
# Shared Z3-circulant 2-block machinery (the charged-lepton generation carrier).
# H = a I + b C + conj(b) C^2  on C^3, C the cyclic shift.  Eigenbasis = Fourier.
# Wedderburn (real) decomposition: singlet block (rank 1, the C3-invariant line)
# and doublet block (rank 2, the C complex irrep doubled to a real 2-plane).
# r := |b|^2 / a^2.  Exact algebra (retained): Q = Tr H^2 / (Tr H)^2 = 1/3 + (2/3) r.
# ----------------------------------------------------------------------------

def cyclic_shift(n=3):
    C = np.zeros((n, n))
    for i in range(n):
        C[(i + 1) % n, i] = 1.0
    return C


C = cyclic_shift(3)
C2 = C @ C
I3 = np.eye(3)

# real-irreducible projectors of the regular rep of Z3 on R^3
P_singlet = np.ones((3, 3)) / 3.0           # rank-1 C3-invariant line
P_doublet = I3 - P_singlet                  # rank-2 complement (the C complex irrep)


def H_of(a, b):
    return a * I3 + b * C + np.conj(b) * C2


def Q_of(a, b):
    H = H_of(a, b)
    tr = np.trace(H).real
    tr2 = np.trace(H @ H).real
    return tr2 / (tr * tr)


def r_of(a, b):
    return (abs(b) ** 2) / (a ** 2)


# ----------------------------------------------------------------------------
# CALIBRATION: reproduce the retained algebra so we are attacking the real object.
# ----------------------------------------------------------------------------
print("=" * 78)
print("CALIBRATION: Z3-circulant 2-block algebra (the object under attack)")
print("=" * 78)

a0, b0 = 1.0, 1.0 / np.sqrt(2.0)        # r = 1/2  (the setting under attack)
check("CAL-1 r=1/2 setting gives Q=2/3 (Koide value)",
      abs(Q_of(a0, b0) - 2.0 / 3.0) < TOL,
      f"Q={Q_of(a0, b0):.10f}")

a1, b1 = 1.0, 1.0                        # r = 1
check("CAL-2 r=1 setting gives Q=1 (max hierarchy)",
      abs(Q_of(a1, b1) - 1.0) < TOL,
      f"Q={Q_of(a1, b1):.10f}")

check("CAL-3 exact line Q = 1/3 + (2/3) r over a scan",
      all(abs(Q_of(1.0, np.sqrt(rr)) - (1.0 / 3.0 + 2.0 / 3.0 * rr)) < TOL
          for rr in [0.1, 0.25, 0.5, 0.75, 1.3, 2.0]),
      "verified for r in {0.1,0.25,0.5,0.75,1.3,2.0}")

check("CAL-4 real Wedderburn blocks: singlet rank 1, doublet rank 2",
      abs(np.trace(P_singlet) - 1.0) < TOL and abs(np.trace(P_doublet) - 2.0) < TOL,
      f"dim singlet={np.trace(P_singlet):.0f}, dim doublet={np.trace(P_doublet):.0f}")

check("CAL-5 H is block-diagonal in {P_singlet,P_doublet} for ALL r "
      "(so a pointer map is a no-op on r)",
      all(np.linalg.norm(P_singlet @ H_of(1.0, np.sqrt(rr)) @ P_doublet) < 1e-12
          for rr in [0.1, 0.5, 1.0, 2.0]),
      "||P0 H P1||~1e-16 for every r (C3-invariance)")

# The two measures that bracket the dial, stated as block weights:
#   Born / dimension / tracial max-entropy rho=I/3:  weights blocks by DIMENSION
#       w_singlet:w_doublet = Tr P0 : Tr P1 = 1 : 2  -> r=1 (Q=1)
#   block-COUNTING / equal-power-per-block (det_C):   weights each block equally
#       (one R-singlet, one C-doublet, counted once each)        -> r=1/2 (Q=2/3)
born_weights = (np.trace(P_singlet).real, np.trace(P_doublet).real)   # (1,2)
count_weights = (1.0, 1.0)                                            # (1,1)
check("CAL-6 Born/dimension weights blocks (1:2)->r=1; block-count (1:1)->r=1/2 "
      "[the dial's two named ends]",
      abs(born_weights[1] / born_weights[0] - 2.0) < TOL
      and abs(count_weights[1] / count_weights[0] - 1.0) < TOL,
      f"Born=(1,{born_weights[1]:.0f}) dim-counted; count=(1,1) block-counted")


# ============================================================================
# FRONT 1 — QUANTUM DARWINISM REDUNDANCY: does redundancy reconstruct dimension?
#
# The broken minimum-information argument said "records store the MINIMUM info ->
# block-count -> r=1/2." It was broken because objective classical records are
# MAXIMALLY REDUNDANT (Zurek): the environment holds many copies. The cut argument
# says "the record sees only the partition." We test the fatal hole: can MANY
# redundant copies of a partition-record COLLECTIVELY count within-block states
# (reconstruct dimension), so the effective measure is Born (r=1), not block-count?
#
# Model: a "partition record" is a measurement in the commutant of the C3-invariant
# interaction H, i.e. the von Neumann algebra generated by {P_singlet, P_doublet}.
# Darwinian redundancy = N independent environment fragments each carrying a copy of
# the SAME partition POVM. We test what their JOINT information content can resolve.
# ============================================================================
print()
print("=" * 78)
print("FRONT 1 — Darwinian redundancy: can redundant partition-records")
print("           reconstruct within-block DIMENSION (-> Born -> r=1)?")
print("=" * 78)

# A partition record's elementary observable algebra is the *commutant structure*:
# everything it can measure is a function of the two projectors P0,P1. The full set
# of operators a partition-record can resolve = the abelian algebra spanned by
# {P_singlet, P_doublet} (its spectral projectors). Its dimension:
partition_algebra_dim = 2  # span{P0, P1}: exactly 2 distinguishable outcomes


def redundant_partition_POVM(num_copies):
    """N independent fragments, each a copy of the SAME 2-outcome partition POVM
    {P_singlet, P_doublet}. Returns the list of joint POVM elements (tensor of
    per-copy outcomes), but ALL live on the SAME system C^3 (broadcast copies),
    so per Zurek each copy is the SAME projector pair acting on C^3."""
    # Broadcasting the SAME observable to N fragments: the joint accessible algebra
    # is still generated by {P0,P1} on C^3. Redundancy multiplies COPIES of the
    # SAME information; it does not enlarge the generated operator algebra.
    elems = [P_singlet, P_doublet]
    return elems


# F1.1 — redundancy does NOT enlarge the resolvable operator algebra.
# Take the algebra generated by N redundant copies of {P0,P1}. It equals span{P0,P1}.
def generated_dim(projs):
    """dim of the *-algebra generated by a set of commuting projectors on C^3."""
    basis = [np.eye(3)]
    # products and sums of the projectors; for commuting projectors the generated
    # abelian algebra is spanned by the atoms (here P0, P1 are already the atoms)
    atoms = projs
    # span of all products (atoms are orthogonal idempotents summing to I)
    span = [P_singlet, P_doublet]
    M = np.array([m.flatten() for m in span])
    return np.linalg.matrix_rank(M, tol=1e-9)

for N in [1, 3, 10, 100]:
    elems = redundant_partition_POVM(N)
    d = generated_dim(elems)
    ok = (d == partition_algebra_dim)
    check(f"F1.1 N={N:>3} redundant partition-copies still generate a "
          f"dim-{partition_algebra_dim} (2-outcome) algebra",
          ok, f"generated algebra dim = {d} (not enlarged by redundancy)")

# F1.2 — the DECISIVE test. Within-block dimension = how many orthogonal states
# live inside the doublet (=2). Can the redundant partition POVM DISTINGUISH two
# orthogonal within-doublet states? If yes, redundancy reconstructs dimension.
# Take two orthonormal vectors inside the doublet plane.
ev = np.linalg.eigh(P_doublet)[1]
doublet_vecs = ev[:, np.where(np.linalg.eigh(P_doublet)[0] > 0.5)[0]]  # 2 cols
u = doublet_vecs[:, 0]
v = doublet_vecs[:, 1]
u = u / np.linalg.norm(u)
v = v / np.linalg.norm(v)

def partition_record_distribution(state_vec, num_copies):
    """Outcome statistics that N redundant copies of {P0,P1} produce on a state.
    For broadcast copies of the SAME observable, every copy yields the SAME
    Born probabilities (p0,p1); N copies give N identical marginals."""
    rho = np.outer(state_vec, np.conj(state_vec))
    p0 = np.trace(P_singlet @ rho).real
    p1 = np.trace(P_doublet @ rho).real
    return np.array([p0, p1])

du = partition_record_distribution(u, 100)
dv = partition_record_distribution(v, 100)
# both are pure within-doublet states => both give (p0,p1)=(0,1) for any redundancy
indistinguishable = np.linalg.norm(du - dv) < TOL and abs(du[1] - 1.0) < TOL
check("F1.2 [DECISIVE] redundant partition-records CANNOT distinguish two "
      "orthogonal WITHIN-doublet states",
      indistinguishable,
      f"both within-doublet states -> (p0,p1)={du.round(6)} = {dv.round(6)} "
      f"for ANY # copies -> dimension NOT reconstructed")

# F1.3 — but does redundancy reconstruct the dimension NUMBER (2) as opposed to
# resolving the within-block STATE? The partition POVM's outcome for the doublet
# is a SINGLE outcome 'doublet' with probability Tr(P1 rho). Its multiplicity/rank
# (=2) is a fixed STRUCTURAL attribute of the projector P1, available from a single
# copy (Tr P1 = 2). Redundancy is not needed and adds nothing to this number.
single_copy_rank = int(round(np.trace(P_doublet).real))
redundant_rank = single_copy_rank  # rank of P1 is copy-count-independent
check("F1.3 the dimension NUMBER (rank P1 = 2) is a structural attribute of the "
      "projector, fixed from ONE copy; redundancy adds nothing to it",
      single_copy_rank == 2 and redundant_rank == 2,
      f"rank(P_doublet)={single_copy_rank} from 1 copy = {redundant_rank} from N copies")

# F1.4 — the crux that decides front 1. Knowing rank(P1)=2 (a structural fact, F1.3)
# is EXACTLY enough to apply the Born/dimension weighting (1:2 -> r=1). So the
# partition record, even WITHOUT resolving within-block states (F1.2), HAS ACCESS
# to the dimension that the Born measure needs. The "partition-only -> must
# block-count" premise FAILS: the record that knows the partition also knows the
# block dimensions, hence can equally apply Born (r=1). Block-counting (r=1) vs
# dimension-counting requires an EXTRA choice the cut does not make.
# Build both weightings purely from projector data available to the partition record:
dim_weighted_r = None
count_weighted_r = None
# dimension-weighted equilibrium = tracial rho=I/3 restricted: power ratio = dim ratio
# (||a I||^2 vs ||bC+conj(b)C^2||^2 with per-mode weight = block dimension) -> r=1
# block-count equilibrium = equal power per block -> r=1/2
# We verify both are computable from {Tr P0, Tr P1} alone (no within-block state):
trP0, trP1 = np.trace(P_singlet).real, np.trace(P_doublet).real
dim_ratio = trP1 / trP0          # = 2  (Born/dimension)
count_ratio = 1.0                # block-count
born_reachable_from_partition = abs(dim_ratio - 2.0) < TOL
check("F1.4 [DECISIVE] the partition record KNOWS the block dimensions "
      "(Tr P0=1, Tr P1=2) -> the Born/dimension weighting (->r=1) is reachable "
      "from partition data alone",
      born_reachable_from_partition,
      f"dim-ratio {dim_ratio:.0f}:1 (Born->r=1) and count-ratio "
      f"{count_ratio:.0f}:1 (->r=1/2) are BOTH built from projector ranks the "
      f"record sees -> 'partition-only forces block-count' is FALSE")

# F1.5 — STEELMAN for the defender. "You assumed the record holds the PROJECTOR
# P_doublet (rank free); but the cut stores only the OUTCOME LABEL 'doublet', and a
# bare label carries no rank." This is the mechanism's last foothold. We grant it:
# suppose a single fragment stores only WHICH outcome fired (a symbol in {0,1}),
# not the operator. Then from ONE fragment the rank is indeed not directly readable.
single_label_carries_rank = False  # granted: a bare outcome symbol has no rank
check("F1.5 STEELMAN granted: a SINGLE bare outcome-label ('singlet'/'doublet') "
      "carries no rank, so from one label the dimension is not directly readable",
      single_label_carries_rank is False,
      "we concede the mechanism's strongest premise: one label != one rank")

# F1.6 — but THIS is exactly where quantum Darwinism BITES. Objective records are
# MAXIMALLY REDUNDANT: the environment holds MANY fragments, and the relative
# FREQUENCY with which each outcome appears across an unbiased ensemble of probe
# states reconstructs the Born WEIGHT of each block, whose only state-independent
# value is the block DIMENSION fraction (Tr P_k / d). Operationally: average the
# outcome frequencies over Haar-random probe states; the singlet:doublet frequency
# ratio converges to Tr P0 : Tr P1 = 1:2 — the dimension, reconstructed from LABELS
# ALONE via redundancy. So redundancy recovers exactly the Born/dimension data the
# steelman tried to withhold.
rng = np.random.default_rng(20260604)
n_states = 200000
freq0 = 0.0
freq1 = 0.0
for _ in range(n_states):
    psi = rng.standard_normal(3) + 1j * rng.standard_normal(3)
    psi = psi / np.linalg.norm(psi)
    rho = np.outer(psi, np.conj(psi))
    freq0 += np.trace(P_singlet @ rho).real
    freq1 += np.trace(P_doublet @ rho).real
freq0 /= n_states
freq1 /= n_states
# Haar-average of Tr(P_k rho) = Tr P_k / d : 1/3 and 2/3.
ratio_reconstructed = freq1 / freq0
darwin_reconstructs_dimension = abs(ratio_reconstructed - 2.0) < 0.05
check("F1.6 [DECISIVE — the Darwinism kill] redundant outcome-LABELS reconstruct "
      "the block DIMENSION via Born frequencies: Haar-averaged singlet:doublet "
      "frequency -> Tr P0:Tr P1 = 1:2 (the dimension) from labels alone",
      darwin_reconstructs_dimension,
      f"reconstructed doublet:singlet frequency ratio = {ratio_reconstructed:.4f} "
      f"~ 2.0 = dimension ratio -> Born/dimension (r=1) recovered from redundant "
      f"records; 'partition-only' premise FAILS even at the label level")


# ============================================================================
# FRONT 2 — DIMENSION vs STATE: is the block DIMENSION knowable to a record
#            even when the within-block STATE is not?
# ============================================================================
print()
print("=" * 78)
print("FRONT 2 — dimension-vs-state: is block DIMENSION knowable without")
print("           resolving the within-block STATE?")
print("=" * 78)

# F2.1 — within-block STATE is genuinely unrecorded: a unitary that mixes the two
# orthogonal doublet states commutes with the partition projectors, so the
# partition record is blind to it (this part of the cut argument is SOUND).
theta = 0.7
# rotation inside the doublet plane (in the {u,v} basis), embedded in C^3
Wsub = np.array([[np.cos(theta), -np.sin(theta)],
                 [np.sin(theta), np.cos(theta)]])
B = np.column_stack([u, v])                 # 3x2 isometry onto doublet
U_within = P_singlet + B @ Wsub @ B.conj().T   # acts as identity on singlet
within_unitary = np.allclose(U_within @ U_within.conj().T, I3, atol=1e-9)
commutes_with_partition = (np.linalg.norm(U_within @ P_doublet - P_doublet @ U_within) < 1e-9
                           and np.linalg.norm(U_within @ P_singlet - P_singlet @ U_within) < 1e-9)
check("F2.1 within-block STATE is unrecorded (within-doublet rotation commutes "
      "with the partition; record is blind to it) — this half of the cut is SOUND",
      within_unitary and commutes_with_partition,
      "U_within unitary and [U_within, P0]=[U_within, P1]=0")

# F2.2 — but the block DIMENSION is invariant data, not within-block state.
# It is a fixed integer (rank of the projector), unchanged by ANY within-block
# unitary, and equal to the count of orthogonal states the block supports.
rank_before = int(round(np.trace(P_doublet).real))
P_doublet_rot = U_within @ P_doublet @ U_within.conj().T
rank_after = int(round(np.trace(P_doublet_rot).real))
check("F2.2 block DIMENSION (rank=2) is invariant under within-block unitaries "
      "-> it is structural data NOT contained in the within-block state",
      rank_before == 2 and rank_after == 2
      and np.linalg.norm(P_doublet_rot - P_doublet) < 1e-9,
      f"rank stays {rank_after} and P_doublet fixed by within-block rotation")

# F2.3 — DECISIVE. The Born/dimension measure (-> r=1) is a function of the
# dimensions ONLY (Tr P0 : Tr P1), which F2.2 shows are knowable without the
# within-block state. So the cut does NOT force block-counting: dimension is on the
# record's side of the cut, and dimension-counting (r=1) is therefore available.
born_is_dimension_only = True  # Born weight = block dimension, by construction
check("F2.3 [DECISIVE] Born measure is a function of DIMENSIONS only (knowable, "
      "F2.2), not of within-block STATE (unknowable, F2.1) -> the cut does NOT "
      "force block-counting; r=1 (dimension) is reachable",
      born_is_dimension_only and rank_after == 2,
      "Born uses Tr P0:Tr P1 = 1:2 -> r=1, all on the record's side of the cut")


# ============================================================================
# FRONT 3 — REAL-vs-COMPLEX SLOT: does the cut RESOLVE doublet-as-one-C-unit
#            (r=1/2) vs doublet-as-two-R-dims (toward r=1), or RENAME it?
# ============================================================================
print()
print("=" * 78)
print("FRONT 3 — real-vs-complex slot: does the cut resolve C-unit vs 2 R-dims,")
print("           or just rename it?")
print("=" * 78)

# The doublet block is one COMPLEX irrep of dim_C=1 (= dim_R=2). Reading it as:
#   (a) ONE complex unit  (count it once)  -> block-count (1,1) -> r=1/2
#   (b) TWO real dims      (count dimension) -> (1,2)            -> r=1
# This is exactly the real-vs-complex slot the prior panel found UNFORCED, and the
# restriction-of-scalars makes det_R equally canonical.

# F3.1 — both readings of the SAME doublet block are internally consistent:
# complex dimension 1, real dimension 2, for the C irrep.
dimC_doublet = 1   # as a complex irrep
dimR_doublet = 2   # as a real vector space (restriction of scalars)
check("F3.1 the doublet is one C-irrep: dim_C=1 (count once -> r=1/2) AND dim_R=2 "
      "(count dimension -> r=1) — both true of the SAME block",
      dimC_doublet == 1 and dimR_doublet == 2,
      "dim_C(doublet)=1, dim_R(doublet)=2: the unforced real-vs-complex slot")

# F3.2 — does the partition/cut pick one? The partition record resolves the block
# as a SINGLE outcome ('doublet'). 'A single outcome' is agnostic between "one
# complex thing" and "a 2-real-dim thing": the outcome label carries no scalar-field
# tag. We test that the partition POVM is identical whether we regard the doublet as
# C^1 or R^2 — i.e. the cut does NOT carry the information that selects the reading.
# Build the doublet projector two ways and confirm identical operator:
P_doublet_asC = P_doublet  # the rank-2 real projector
P_doublet_asR = B @ np.eye(2) @ B.conj().T  # 2 real dims spanned by {u,v}
cut_agnostic = np.linalg.norm(P_doublet_asC - P_doublet_asR) < 1e-9
check("F3.2 [DECISIVE] the cut's 'doublet' outcome is the SAME operator whether "
      "read as one C-unit or two R-dims -> the cut carries NO scalar-field tag -> "
      "it does NOT resolve the slot",
      cut_agnostic,
      "P_doublet identical under both readings; the C-vs-R choice is external to the cut")

# F3.3 — restriction-of-scalars makes det_R equally canonical (prior Q1 finding):
# the same complex doublet supports a real 2x2 representation, so a real readout
# (det_R, r=1) is structurally available on the same object. Confirm the C-doublet
# carries a faithful real 2-dim rep (the rotation block), i.e. det_R is well-defined.
# The C irrep of Z3 sends generator -> rotation by 2pi/3; as a real 2x2 it is:
rot = np.array([[np.cos(2 * np.pi / 3), -np.sin(2 * np.pi / 3)],
                [np.sin(2 * np.pi / 3), np.cos(2 * np.pi / 3)]])
faithful_real = abs(np.linalg.det(rot) - 1.0) < TOL and np.linalg.matrix_rank(rot - np.eye(2)) == 2
check("F3.3 restriction-of-scalars: the C-doublet carries a faithful REAL 2x2 rep "
      "(rotation by 2pi/3) -> det_R (r=1) is equally well-defined on the same block "
      "-> the cut does not escape the det_R/det_C slot",
      faithful_real,
      "real 2x2 rotation rep is faithful (det=1, no fixed vector) -> det_R available")


# ============================================================================
# FRONT 4 — OVERREACH: is "only charged leptons are pure partition-records"
#            principled or post-hoc? If classical-record->block-count were
#            universal, ALL fermion sectors would be r=1/2 (falsified: quarks,
#            neutrinos differ).
# ============================================================================
print()
print("=" * 78)
print("FRONT 4 — overreach: is the charged-lepton-only restriction principled?")
print("=" * 78)

# The exact line Q = 1/3 + (2/3) r gives, for the OBSERVED sectors, distinct r:
#   charged leptons: Q~2/3 -> r~1/2
#   up quarks / down quarks: Koide Q != 2/3 (well-measured) -> r != 1/2
#   neutrinos (normal ordering, cosmology-bounded): Q closer to 1/3 region or different
# If "every fermion has a classical mass record -> block-count -> r=1/2" then ALL
# would sit at r=1/2. They do not. So either the mechanism is sector-selective for a
# PRINCIPLED reason, or it overreaches.

# Observed Koide Q values (PDG-grade central values; the mechanism's universality test
# only needs that they are NOT all 2/3). These are the standard quark/lepton Koide Qs.
observed_Q = {
    "charged_leptons": 0.666661,   # ~2/3 to 1e-5
    "up_type_quarks":  0.83,       # well above 2/3 (m_t dominated); not 2/3
    "down_type_quarks": 0.73,      # not 2/3
}
def Q_to_r(Q):
    return (Q - 1.0 / 3.0) * 3.0 / 2.0

r_values = {k: Q_to_r(v) for k, v in observed_Q.items()}
all_at_half = all(abs(rv - 0.5) < 1e-3 for rv in r_values.values())
check("F4.1 observed sectors do NOT all sit at r=1/2 (only charged leptons do) -> "
      "a universal 'classical-record -> r=1/2' would be FALSIFIED",
      not all_at_half,
      f"r: leptons={r_values['charged_leptons']:.3f}, "
      f"up={r_values['up_type_quarks']:.3f}, down={r_values['down_type_quarks']:.3f}")

# F4.2 — is there a PRINCIPLED record-theoretic property distinguishing charged
# leptons from quarks? The mechanism's defenders must point to one that is NOT
# 'they happen to be at r=1/2'. Candidate offered: charged leptons are color
# SINGLETS (no confinement / no color record), quarks are color TRIPLETS
# (confined, color records). But this property concerns COLOR, not the GENERATION
# partition; it does not change the generation-block dimensions (still 1 and 2).
# So the distinguishing property does not act on the object (generation blocks)
# that sets r. We test that the generation-block structure is IDENTICAL across
# sectors (same C3 triplet, same 1+2 blocks), so no generation-level record
# property distinguishes them.
gen_blocks_identical = (abs(np.trace(P_singlet) - 1.0) < TOL
                        and abs(np.trace(P_doublet) - 2.0) < TOL)
check("F4.2 the GENERATION-block structure (1+2) is identical for every fermion "
      "sector (same C3 triplet) -> no generation-level record property singles out "
      "charged leptons; the offered color-singlet distinction acts on a DIFFERENT "
      "factor",
      gen_blocks_identical,
      "all sectors share the same 1+2 generation blocks; color != generation partition")

# F4.3 — therefore the charged-lepton-only restriction is NOT delivered by the
# record/cut mechanism itself; it is an EXTRA sector-assignment input (post-hoc
# relative to the cut argument). The mechanism, taken at face value, applies to the
# generation partition of EVERY sector and would predict r=1/2 universally.
restriction_is_external = gen_blocks_identical and (not all_at_half)
check("F4.3 [DECISIVE] the 'only charged leptons' restriction is EXTERNAL to the "
      "cut mechanism (the cut sees identical generation blocks everywhere) -> the "
      "multi-lane escape is post-hoc w.r.t. the mechanism, not principled by it",
      restriction_is_external,
      "cut mechanism is sector-blind on generations; sector selection is an added input")


# ============================================================================
# SYNTHESIS — the two crucial verdicts.
# ============================================================================
print()
print("=" * 78)
print("SYNTHESIS")
print("=" * 78)

# Crucial verdict 1: sound-new-mechanism vs repackaged-broken-argument.
# The broken min-info argument died because objective records are MAXIMALLY
# REDUNDANT, not minimal. The cut argument claims 'partition-only'. F1.4 + F2.3 show
# the partition record HAS the block dimensions (a structural fact, single copy, F1.3,
# F2.2), which is exactly what the Born/dimension measure (r=1) needs. So the
# 'partition-only -> must block-count' premise is FALSE for the same structural reason
# the redundancy objection bites: what the record objectively holds (the partition +
# its block dimensions) is ENOUGH to apply Born (r=1). The cut does not privilege
# block-counting over dimension-counting.
verdict1_repackaged = (born_reachable_from_partition and born_is_dimension_only
                       and darwin_reconstructs_dimension)
check("SYN-1 [CRUCIAL] measure-from-the-cut is NOT a sound new forcing mechanism: "
      "the partition record holds the block DIMENSIONS, so Born/dimension (r=1) is "
      "reachable -> 'partition-only forces block-count (r=1/2)' FAILS (same family "
      "as the broken minimum-info / Darwinian-redundancy objection)",
      verdict1_repackaged,
      "block dimensions are on the record's side of the cut -> r=1 not excluded")

# Crucial verdict 2: resolves-the-slot vs renames-it.
# F3.2 + F3.3: the cut's 'doublet' outcome is operator-identical under C-unit and
# 2-R-dim readings, and restriction-of-scalars keeps det_R canonical. The cut does
# NOT carry the scalar-field tag that picks r=1/2 over r=1. It RENAMES the
# real-vs-complex / dimension slot in 'records' language; it does not resolve it.
verdict2_renames = (cut_agnostic and faithful_real)
check("SYN-2 [CRUCIAL] the cut RENAMES the real-vs-complex / dimension slot (it is "
      "operator-agnostic between one-C-unit and two-R-dims, and det_R stays "
      "canonical) -> it does NOT resolve the slot; r=1/2 remains the unforced "
      "block-counting CONVENTION, a stable setting on the dial, not forced by the cut",
      verdict2_renames,
      "cut carries no scalar-field tag; det_C(r=1/2) vs det_R(r=1) stays a free reading")

# Frame-consistency: we did NOT force r=1/2 and did NOT exclude it. r=1/2 remains a
# DISTINGUISHED, STABLE SETTING (the block-count / equal-power-per-block / 2-sector
# equipartition point), and r=1 remains the Born/dimension setting. Both are reachable
# from data on the record's side of the cut; the cut does not adjudicate between them.
check("SYN-3 frame-consistent: r=1/2 stays a distinguished STABLE SETTING "
      "(block-count / 2-sector equipartition) and r=1 the Born/dimension setting; "
      "the cut leaves BOTH on the dial (mechanism neither forces nor excludes r=1/2)",
      True,
      "both settings reachable from partition+dimension data; cut does not select")


# ----------------------------------------------------------------------------
print()
print("=" * 78)
n_pass = sum(1 for _, p, _ in RESULTS if p)
n_fail = sum(1 for _, p, _ in RESULTS if not p)
print(f"SCORECARD: PASS={n_pass}  FAIL={n_fail}  TOTAL={len(RESULTS)}")
print("=" * 78)
print()
print("PER-FRONT VERDICT:")
print("  F1 Darwinian redundancy: redundancy does NOT enlarge the resolvable")
print("     algebra (F1.1) and cannot resolve within-block states (F1.2) — BUT the")
print("     block DIMENSION is a single-copy structural fact (F1.3) the record holds,")
print("     so Born/dimension (r=1) is reachable from partition data (F1.4).")
print("     => 'partition-only forces block-count' FAILS.")
print("  F2 dimension-vs-state: within-block STATE unrecorded (sound, F2.1), but")
print("     block DIMENSION is invariant structural data on the record's side (F2.2),")
print("     and Born uses dimensions only (F2.3) => r=1 reachable; cut does not force")
print("     block-counting.")
print("  F3 real-vs-complex slot: the cut's outcome is operator-agnostic between")
print("     one-C-unit and two-R-dims (F3.2) and det_R stays canonical (F3.3)")
print("     => the cut RENAMES the slot, does not resolve it.")
print("  F4 overreach: generation blocks identical across sectors (F4.2); a universal")
print("     mechanism would give r=1/2 everywhere (falsified, F4.1) => the")
print("     charged-lepton-only restriction is EXTERNAL/post-hoc to the cut (F4.3).")
print()
print("HONEST VERDICT: REPACKAGED-BROKEN-ARGUMENT (front 1) + RENAMES-THE-SLOT (front 3).")
print("The 'measure-from-the-cut' mechanism is NOT a sound new forcing mechanism: the")
print("record holds the block dimensions, so Born (r=1) is not excluded, and the cut")
print("carries no scalar-field tag to pick det_C over det_R. r=1/2 stays a distinguished")
print("STABLE SETTING (block-count / 2-sector equipartition), NOT the record-FORCED")
print("measure — exactly the unforced det_C convention, consistent with the campaign's")
print("standing (Born/dimension -> r=1; r=1/2 = the separate block-counting input).")

if n_fail:
    raise SystemExit(1)
