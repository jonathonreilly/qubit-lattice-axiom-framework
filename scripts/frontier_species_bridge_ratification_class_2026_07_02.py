#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""frontier_species_bridge_ratification_class_2026_07_02.py

Bounded runner for the note
  docs/SPECIES_BRIDGE_RESIDUAL_IS_RATIFICATION_CLASS_GRADE_SCOPED_BOUNDED_NOTE_2026-07-02.md

Purpose (profile-match exhibit + two-part governance map, NOT a verdict):
  - guard that the three read source notes still carry the sentences this note
    quotes -- the parent's minimum-form residual AND its own scorecard
    (argued/strongly-supported, not exhaustively proven; the uncomputed
    invariant functional ring), its class assignment (the universal
    abstract->physical bridge, abstract su(3) -> physical color, not derived
    away), and its ker-D-only U_R scope; the C3 canonical note's Does-NOT
    profile plus the FULL third bullet (axiom/primitive clause AND the
    already-landed-surfaces positive condition) and the two-landed-surfaces
    sentence; the axioms' distinction clauses PLUS the Qualification supply
    sentence and the Open-Gates placement that keep the derived surface outside
    axiom content;
  - encode the Ratification Profile Boundary comparison as (i) a Does-NOT *profile* map (C3 negative-profile
    item <-> parent witness), every row MATCHES and source-grounded, no bullet
    dropped; and (ii) the path's defining POSITIVE condition (co-reference on
    already-landed surfaces), which the residual fails -- its second relatum is
    external nature, not a landed repo surface. The internal FAILS verdict is the
    EXPECTED result: the check passes when the mapping correctly records the
    failure. This is data-structure completeness + source-groundedness, NOT an
    assertion of semantic equivalence or term-for-term shape-identity;
  - recompute the small exact Distinction-Clause Analogy witnesses of the two vacuities: the single C3
    orbit; a FALSIFIABLE unitary intertwiner E*C1 = C2*E between two genuinely
    distinct integer carriers C1 != C2, with a broken shift E' as a negative
    control (E'*C1 != C2*E'); and the equivariant corner-weight contrast (a
    generic rational diagonal separates, the C3 orbit-average equalizes,
    spread 0);
  - grep the note itself for the Grade Scope + owner-class wording and the
    Governance Map boundary tokens (owner decision / owner review list / nothing adopted / grade /
    does not retire / fails / path-extension / argued / not exhaustively proven
    / separate residual) and the two-part decision + extended residue markers.

Nothing here sets, predicts, or edits any audit status. Python3 stdlib only;
exact arithmetic (int / Fraction; permutation matrices as integer tuples); no
floats anywhere. Per-check line is "CHECK NN: PASS/FAIL -- <desc>"; the run
prints "TOTAL: PASS=N FAIL=0" and exits nonzero if any check FAILs.
"""

import os
import sys
import unicodedata
from fractions import Fraction


# ----------------------------------------------------------------------------
# text loading + canonicalization
# ----------------------------------------------------------------------------
def canon(s):
    """NFKC-normalize (subscripts/letterlike -> ASCII) then collapse whitespace.

    This turns 'C_3'-subscript into 'C3', 'M_3(double-struck C)' into 'M3(C)',
    superscript two into '2', and folds line-wraps to single spaces so that a
    quoted sentence matches regardless of where the source note wrapped it.
    """
    return " ".join(unicodedata.normalize("NFKC", s).split())


def read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")

PARENT_MD = os.path.join(
    DOCS, "SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md"
)
C3_MD = os.path.join(
    DOCS, "C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md"
)
AXIOMS_MD = os.path.join(DOCS, "MINIMAL_AXIOMS_2026-06-29.md")
NOTE_MD = os.path.join(
    DOCS,
    "SPECIES_BRIDGE_RESIDUAL_IS_RATIFICATION_CLASS_GRADE_SCOPED_BOUNDED_NOTE_2026-07-02.md",
)

PARENT = canon(read(PARENT_MD))
C3 = canon(read(C3_MD))
AX = canon(read(AXIOMS_MD))
NOTE = canon(read(NOTE_MD))


# ----------------------------------------------------------------------------
# quoted-sentence targets (already in NFKC/whitespace-collapsed form)
# ----------------------------------------------------------------------------
# parent note (SPECIES_BRIDGE_MINIMUM_DECOMPOSITION ... 2026-06-13)
P_RESIDUAL = (
    "derived 3-state irreducible C3-structure is what physics calls fermion "
    "generations at the C3-structural grade"
)
P_MINFORM = "carrying no tested C3-grade number, selector, ordering, or weight"
P_TWO_VAC = "two provably-vacuous"
P_VAC1 = "within-triplet naming"
P_VAC2 = "carrier-triplet choice"
P_CAVEAT = (
    "two candidate carriers exist; their selection is vacuous only at the C3 "
    "grade, the full taste/Dirac content being bracketed"
)
P_W_EQUIP = "single-orbit equipartition"
P_W_INTERT = "intertwiner"
P_W_SPREAD = "spread = 0"
P_W_RIGID = "rigid regular C3-rep"
P_CONTENTLESS = "contentless at the tested C3-structural grade"
P_REGISTRY = "the registry is untouched"
P_AUDIT = "does not set or predict an audit outcome"
# Landed Residual Restatement imports: the parent's own scorecard, class assignment, and U_R scope
P_ARGUED = "argued/strongly-supported, not exhaustively proven"
P_INVRING = (
    "invariant functional ring of the carrier and showing it has no "
    "orbit-separating generator"
)
P_SU3COLOR = "abstract su(3) → physical color"
P_UNIVBRIDGE = "universal abstract→physical bridge"
P_NOTDERIVED = "it is not derived away"
P_INTERPBRIDGE = "It remains an interpretive bridge"
P_URSCOPE = "not of D globally"
P_CKM = "across-fermion-type alignment (the CKM/PMNS mixing structure)"
P_CKM_SEP = "a separate residual, not addressed here"

# C3 canonical note (labeling-convention ratification exemplar)
C_RATIFY = (
    "this is a naming ratification on already-landed surfaces (the "
    "import-retirement path for labeling conventions)"
)
C_TWONAME = (
    "two namings of the same two cells of this one context, not two "
    "independent structures"
)
C_OUTCOME = "outcome naming"
C_CHANNEL = "channel naming"
C_BOTHLANDED = (
    "two landed surfaces named above, cited for their existing cell namings"
)
C_DN_SUPPLY = (
    "Does not supply a weighting, normalization, probability rule, occupancy "
    "rule, dictionary selection, or any value of `r` or `Q`"
)
C_DN_SCORE = "Does not select among scoring rules and does not close any wall"
C_DN_AXIOM = "Does not modify any axiom or primitive"
C_DN_AUDIT = "Does not set audit status"
C_LANDED = "already-landed surfaces"
# the FULL third bullet: the Does-NOT (axiom/primitive) clause AND the positive
# condition (co-reference on already-landed surfaces) -- both halves, intact.
C_DN_AXIOM_FULL = C_DN_AXIOM + "; " + C_RATIFY

# axioms note (distinction clauses + Qualification + Open-Gates placement)
AX_QUBIT = (
    "No possibility is privileged. Possibilities are distinguished by the "
    "supplied algebraic structure alone."
)
AX_LATTICE = (
    "No site is privileged. Sites are distinguished by the supplied lattice "
    "structure alone."
)
AX_QUALIF = (
    "Further physical structure requires a retained derivation or bridge, or "
    "explicit approved- primitive registration, before use as a premise"
)
AX_OUTSIDE = "remain outside axiom content"
AX_OPENGATE = "staggered-Dirac/finite-Grassmann realization and"
AX_ONESITE = "full one-site possibility domain has algebraic presentation"

# this note (Grade Scope + owner-class wording; Governance Map boundary tokens; the
# external-referent disanalogy; the two-part decision + extended residue)
N_BRACKET = "taste/Dirac/chirality"
N_UNTOUCHED = "sub-admissions (i) and (ii)"
N_OWNER = "owner decision"
N_OWNER_REVIEW = "owner review list"
N_NOTHING = "nothing adopted"
N_GRADE = "grade"
N_RETIRE = "does not retire"
N_OWNERCLASS = "carried by whatever class the owner rules"
N_FAILS = "fails"
N_PATHEXT = "path-extension"
N_ARGUED = "argued"
N_NOTPROVEN = "not exhaustively proven"
N_SEPRESID = "separate residual"
N_EXTERNAL = "second relatum is external nature"
N_TWOPART = "two-part owner decision"
N_INTERNALONLY = "internal-only precedent"
N_CKM = "CKM/PMNS"
N_INVRING = "invariant functional ring"


# ----------------------------------------------------------------------------
# Ratification Profile Boundary Does-NOT PROFILE map: each C3 negative-profile bullet paired with a
# parent-side witness. Honestly a *profile-completeness* table -- it certifies
# both columns occur in their own source note, that every enumerated Does-NOT
# key is covered, and that every row is a MATCHES; it does NOT assert semantic
# equivalence.
# ----------------------------------------------------------------------------
MAPPING = [
    # key                c3-side (Does-NOT profile)    parent-side witness   verdict
    ("supply", C_DN_SUPPLY, P_MINFORM, "MATCHES"),
    ("scoring_wall", C_DN_SCORE, P_CONTENTLESS, "MATCHES"),
    ("axiom_primitive", C_DN_AXIOM, P_REGISTRY, "MATCHES"),
    ("audit_status", C_DN_AUDIT, P_AUDIT, "MATCHES"),
]
MAPPING_EXPECTED_KEYS = {
    "supply",
    "scoring_wall",
    "axiom_primitive",
    "audit_status",
}

# The path's defining POSITIVE condition -- the SECOND clause of the exemplar's
# third bullet, the clause the earlier draft carved off. For the residual it
# fails: the second relatum is external nature, not a landed repo surface.
# Fields: (key, c3-side positive condition, note-side disanalogy, verdict).
# FAILS is the EXPECTED result; the check passes when the failure is recorded.
POSITIVE_CONDITION = ("landed_surfaces", C_LANDED, N_EXTERNAL, "FAILS")


# ----------------------------------------------------------------------------
# exact 3x3 integer/Fraction matrix helpers (no floats)
# ----------------------------------------------------------------------------
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
# cyclic 3-cycle permutation matrix: e0 -> e1 -> e2 -> e0
C3M = ((0, 0, 1), (1, 0, 0), (0, 1, 0))


def matmul(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def transpose(A):
    return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))


def dagger(A):
    # real integer/Fraction matrices: conjugate-transpose == transpose
    return transpose(A)


def scal(c, A):
    return tuple(tuple(c * A[i][j] for j in range(3)) for i in range(3))


def add(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(3)) for i in range(3))


def diagm(a, b, c):
    return ((a, 0, 0), (0, b, 0), (0, 0, c))


def diag_of(A):
    return [A[i][i] for i in range(3)]


def is_diagonal(A):
    return all(A[i][j] == 0 for i in range(3) for j in range(3) if i != j)


def compose(p, q):
    # permutation composition (p after q): (p o q)[i] = p[q[i]]
    return tuple(p[q[i]] for i in range(3))


# ----------------------------------------------------------------------------
# check harness
# ----------------------------------------------------------------------------
_RESULTS = []


def check(desc, cond):
    cond = bool(cond)
    _RESULTS.append(cond)
    print("CHECK %02d: %s -- %s" % (len(_RESULTS), "PASS" if cond else "FAIL", desc))


def has_all(hay, needles):
    return all(n in hay for n in needles)


# ----------------------------------------------------------------------------
# Landed Residual Restatement -- the landed residual restated, WITH the parent's own scorecard, class
# assignment, and U_R scope imported verbatim (checks 1-8)
# ----------------------------------------------------------------------------
check(
    "parent note carries the minimum-form residual identification sentence",
    P_RESIDUAL in PARENT,
)
check(
    "parent note carries the no-number/no-selector/no-ordering/no-weight sentence",
    P_MINFORM in PARENT,
)
check(
    "parent note names both vacuities (two provably-vacuous; within-triplet naming; carrier-triplet choice)",
    has_all(PARENT, [P_TWO_VAC, P_VAC1, P_VAC2]),
)
check(
    "parent note carries the carrier-choice caveat (two candidate carriers; vacuous only at C3 grade; taste/Dirac bracketed)",
    P_CAVEAT in PARENT,
)
check(
    "parent note carries its computed witnesses (single-orbit equipartition; intertwiner; spread = 0; rigid regular C3-rep)",
    has_all(PARENT, [P_W_EQUIP, P_W_INTERT, P_W_SPREAD, P_W_RIGID]),
)
check(
    "Landed Residual Restatement scorecard: parent states contentlessness is argued/strongly-supported, not exhaustively proven, pending the uncomputed invariant functional ring",
    has_all(PARENT, [P_ARGUED, P_INVRING]),
)
check(
    "Landed Residual Restatement class assignment: parent classes the residual as the universal abstract->physical bridge (abstract su(3) -> physical color), not derived away -- it remains an interpretive bridge",
    has_all(PARENT, [P_SU3COLOR, P_UNIVBRIDGE, P_NOTDERIVED, P_INTERPBRIDGE]),
)
check(
    "Landed Residual Restatement scope: parent scopes U_R as a symmetry of ker D only (not of D globally)",
    P_URSCOPE in PARENT,
)

# ----------------------------------------------------------------------------
# Ratification Profile Boundary -- Does-NOT profile MATCHES; the positive landed-surfaces condition fails
# (checks 9-16)
# ----------------------------------------------------------------------------
check(
    "C3 canonical note carries the ratification framing (naming ratification on already-landed surfaces; import-retirement path)",
    C_RATIFY in C3,
)
check(
    "C3 canonical note carries the two-namings sentence, both cell namings, and that BOTH namings are landed internal surfaces",
    has_all(C3, [C_TWONAME, C_OUTCOME, C_CHANNEL, C_BOTHLANDED]),
)
check(
    "C3 canonical note carries the Does-NOT supply-nothing sentence (weighting/normalization/probability/occupancy/dictionary/value)",
    C_DN_SUPPLY in C3,
)
check(
    "C3 canonical note carries the Does-NOT scoring/wall, axiom/primitive, and audit-status sentences",
    has_all(C3, [C_DN_SCORE, C_DN_AXIOM, C_DN_AUDIT]),
)
check(
    "C3 canonical note carries the FULL third bullet intact -- axiom/primitive Does-NOT clause AND the already-landed-surfaces positive condition, mapped in full (not carved)",
    C_DN_AXIOM_FULL in C3
    and C_DN_AXIOM in C_DN_AXIOM_FULL
    and C_LANDED in C_DN_AXIOM_FULL,
)
check(
    "Ratification Profile Boundary profile: every Does-NOT row's C3-side occurs in the C3 note and every parent-side witness occurs in the parent note; all four rows are MATCHES",
    all(c3s in C3 for (_k, c3s, _p, _v) in MAPPING)
    and all(p in PARENT for (_k, _c3, p, _v) in MAPPING)
    and all(v == "MATCHES" for (_k, _c3, _p, v) in MAPPING),
)
check(
    "Ratification Profile Boundary completeness: every enumerated Does-NOT profile key is paired -- no negative-profile bullet dropped",
    set(k for (k, _c3, _p, _v) in MAPPING) == MAPPING_EXPECTED_KEYS
    and len(MAPPING) == len(MAPPING_EXPECTED_KEYS),
)
# positive-condition failure -- the EXPECTED result
_pk, _pc3, _pnote, _pver = POSITIVE_CONDITION
check(
    "Ratification Profile Boundary positive condition: the landed-surfaces clause is grounded in C3; the mapping records the residual fails it (second relatum is external nature, not a landed surface) and the note owns the disanalogy -- failure is the expected result",
    _pc3 in C3
    and _pver == "FAILS"
    and _pnote in NOTE,
)

# ----------------------------------------------------------------------------
# Distinction-Clause Analogy -- the vacuities' computations instantiate, on the derived surface, the
# axioms' non-privilege discipline (analogy, not axiom grounding) (checks 17-21)
# ----------------------------------------------------------------------------
check(
    "axioms note carries both distinction clauses (Qubit possibility twin; Lattice site twin)",
    has_all(AX, [AX_QUBIT, AX_LATTICE]),
)
check(
    "axioms note keeps the derived surface OUTSIDE axiom content: Qualification supply sentence; Open-Gates staggered realization + AC_phi_lambda outside; Qubit possibilities are the one-site domain",
    has_all(AX, [AX_QUALIF, AX_OUTSIDE, AX_OPENGATE, AX_ONESITE]),
)

# Distinction-Clause Analogy witness 1 -- within-triplet naming vacuity: single C3 orbit
p = (1, 2, 0)  # C3 as a 3-cycle on the three corner labels {0,1,2}
p2 = compose(p, p)
p3 = compose(p2, p)
orbit0 = set()
x = 0
for _ in range(3):
    orbit0.add(x)
    x = p[x]
check(
    "Distinction-Clause Analogy within-triplet witness: C3 acts as an order-3 3-cycle with a single transitive orbit {0,1,2} on the three corner labels",
    orbit0 == {0, 1, 2}
    and p3 == (0, 1, 2)
    and p != (0, 1, 2)
    and p2 != (0, 1, 2),
)

# Distinction-Clause Analogy witness 2 -- carrier-triplet vacuity via a FALSIFIABLE unitary intertwiner
#   between two GENUINELY DISTINCT integer carriers.
#     C1 = forward 3-cycle 0->1->2->0;  C2 = C1^2 = C1^{-1}, the reverse cycle,
#       so C1 != C2 (two distinct integer-matrix presentations of the regular
#       C3-rep carried by the two Hamming triplets).
#     E  = the transposition (1 2): the equivariant intertwiner. E^T E = I,
#          E != I, and E*C1 = C2*E.
#     E' = a shift (the wrong conjugator): E'*C1 != C2*E' -- negative control.
#   The intertwining relation is thus a real, falsifiable constraint, NOT the
#   unfalsifiable identity of the earlier draft (which set C1 = C2 = E).
C1 = ((0, 0, 1), (1, 0, 0), (0, 1, 0))  # forward 3-cycle
C2 = matmul(C1, C1)  # = C1^{-1}, the reverse 3-cycle (distinct from C1)
E = ((1, 0, 0), (0, 0, 1), (0, 1, 0))  # transposition (1 2): the intertwiner
E_broken = C1  # a shift: the wrong conjugator (negative control)

carriers_distinct = C1 != C2
E_unitary = matmul(dagger(E), E) == I3
E_nontrivial = E != I3
intertwine_ok = matmul(E, C1) == matmul(C2, E)
neg_control_fails = matmul(E_broken, C1) != matmul(C2, E_broken)
check(
    "Distinction-Clause Analogy carrier witness: distinct integer carriers C1 != C2 with a unitary intertwiner E (E^T E = I, E != I) satisfying E*C1 = C2*E, and a broken shift E' with E'*C1 != C2*E' -- the intertwining is falsifiable, exact integer arithmetic",
    carriers_distinct
    and E_unitary
    and E_nontrivial
    and intertwine_ok
    and neg_control_fails,
)

# Distinction-Clause Analogy witness 3 -- equivariant corner-weight equality (all exact Fractions):
#   a generic rational diagonal separates the corners (spread > 0), the C3
#   orbit-average forces them equal (spread = 0), yielding a scalar operator.
H = diagm(Fraction(0), Fraction(3), Fraction(6))  # distinct rational corner weights
dH = diag_of(H)
spread_generic = max(dH) - min(dH)  # exact Fraction

Cpows = [I3, C3M, matmul(C3M, C3M)]  # C^0, C^1, C^2
conjs = [matmul(matmul(Cp, H), dagger(Cp)) for Cp in Cpows]  # Cp H Cp^{-1}
Havg = scal(Fraction(1, 3), conjs[0])
Havg = add(Havg, scal(Fraction(1, 3), conjs[1]))
Havg = add(Havg, scal(Fraction(1, 3), conjs[2]))
dAvg = diag_of(Havg)
spread_avg = max(dAvg) - min(dAvg)  # exact Fraction

scalar_val = Fraction(0 + 3 + 6, 3)  # = 3
Havg_is_scalar = (
    is_diagonal(Havg)
    and all(v == scalar_val for v in dAvg)
    and Havg == scal(scalar_val, I3)
)
equivariant_ok = matmul(Havg, C3M) == matmul(C3M, Havg)
check(
    "Distinction-Clause Analogy corner-weight witness: generic rational diagonal separates (spread = 6 > 0); C3 orbit-average equalizes (spread = 0), Havg = 3*I, commutes with C3 -- exact",
    spread_generic == Fraction(6)
    and spread_generic > 0
    and spread_avg == Fraction(0)
    and Havg_is_scalar
    and equivariant_ok,
)

# ----------------------------------------------------------------------------
# Grade Scope -- grade-scope + owner-class wording grep on this note (check 22)
# ----------------------------------------------------------------------------
check(
    "Grade Scope: note states the bracketed above-grade content (taste/Dirac/chirality), that sub-admissions (i) and (ii) are untouched, and the owner-class wording (carried by whatever class the owner rules)",
    has_all(NOTE, [N_BRACKET, N_UNTOUCHED, N_OWNERCLASS]),
)

# ----------------------------------------------------------------------------
# Governance Map -- governance-boundary greps + two-part decision + extended residue (checks 23-24)
# ----------------------------------------------------------------------------
check(
    "Governance Map boundary: note carries the boundary tokens (owner decision; owner review list; nothing adopted; grade; does not retire) and the repair tokens (fails; path-extension; argued; not exhaustively proven; separate residual)",
    has_all(
        NOTE,
        [
            N_OWNER,
            N_OWNER_REVIEW,
            N_NOTHING,
            N_GRADE,
            N_RETIRE,
            N_FAILS,
            N_PATHEXT,
            N_ARGUED,
            N_NOTPROVEN,
            N_SEPRESID,
        ],
    ),
)
check(
    "Governance Map: note states the two-part owner decision with internal-only precedent, and the extended residue carries item 8 (CKM/PMNS separate residual) and item 9 (the invariant-ring proof-strength gap)",
    has_all(NOTE, [N_TWOPART, N_INTERNALONLY, N_CKM, N_INVRING]),
)


# ----------------------------------------------------------------------------
# declared-open residue (informational; not counted as checks)
# ----------------------------------------------------------------------------
print("")
print("DECLARED-OPEN RESIDUE (conserved; owner surface, nothing adopted here):")
for line in (
    "the AC_phi_lambda(iii) identification -- pending the owner two-part (path-extension, then ratify/decline) decision",
    "the bracketed above-C3-grade content (taste/Dirac/chirality; hw=1 vs hw=2 beyond C3)",
    "sub-admission (i) (occupancy/reading selection) -- untouched",
    "sub-admission (ii) (R-eta identification) -- untouched",
    "adjacent review-pending K-arc PRs #4831/#4835/#4837/#4840/#4845 (non-overlapping)",
    "adjacent note-level two-cell family PR #4853 (context only)",
    "audit statuses of all cited notes -- owned by the independent audit lane",
    "the parent's separate CKM/PMNS across-fermion-type alignment residual -- not addressed here",
    "the parent's proof-strength gap: contentlessness argued/strongly-supported, not exhaustively proven (uncomputed C3/epsilon invariant functional ring)",
):
    print("  RESIDUE: " + line)
print("")

# ----------------------------------------------------------------------------
# totals + exit code
# ----------------------------------------------------------------------------
_npass = sum(1 for r in _RESULTS if r)
_nfail = len(_RESULTS) - _npass
print("TOTAL: PASS=%d FAIL=%d" % (_npass, _nfail))
sys.exit(0 if _nfail == 0 else 1)
