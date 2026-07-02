#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""frontier_species_bridge_ratification_class_2026_07_02.py

Bounded runner for the note
  docs/SPECIES_BRIDGE_RESIDUAL_IS_RATIFICATION_CLASS_GRADE_SCOPED_BOUNDED_NOTE_2026-07-02.md

Purpose (class-membership exhibit + governance map, NOT a verdict):
  - guard that the three read source notes still carry the sentences this note
    quotes (the parent's minimum-form residual; the C3 canonical note's
    ratification + Does-NOT sentences; the two axiom distinction clauses);
  - encode the T2 term-for-term mapping (C3 Does-NOT item <-> parent witness)
    as an exact *mapping-completeness* checklist -- this checks that both
    columns are grounded as substrings in their own source files and that no
    Does-NOT bullet is dropped; it does NOT assert semantic equivalence;
  - recompute the small exact T3 witnesses of the two vacuities
    (single C3 orbit; the unitary intertwiner identity EH(dagger)EH = I with
    the intertwining relation EH*C1 = C2*EH; the equivariant corner-weight
    contrast: a generic rational diagonal separates, the C3 orbit-average
    equalizes it, spread 0);
  - grep the note itself for the T4 grade-scope sentences and the T5 boundary
    tokens (owner decision / morning / nothing adopted / grade / does not
    retire).

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
C_DN_SUPPLY = (
    "Does not supply a weighting, normalization, probability rule, occupancy "
    "rule, dictionary selection, or any value of `r` or `Q`"
)
C_DN_SCORE = "Does not select among scoring rules and does not close any wall"
C_DN_AXIOM = "Does not modify any axiom or primitive"
C_DN_AUDIT = "Does not set audit status"

# axioms note (distinction clauses)
AX_QUBIT = (
    "No possibility is privileged. Possibilities are distinguished by the "
    "supplied algebraic structure alone."
)
AX_LATTICE = (
    "No site is privileged. Sites are distinguished by the supplied lattice "
    "structure alone."
)

# this note (T4 grade-scope sentences; T5 boundary tokens)
N_BRACKET = "taste/Dirac/chirality"
N_UNTOUCHED = "sub-admissions (i) and (ii)"
N_OWNER = "owner decision"
N_MORNING = "morning"
N_NOTHING = "nothing adopted"
N_GRADE = "grade"
N_RETIRE = "does not retire"


# ----------------------------------------------------------------------------
# T2 mapping table: each C3 Does-NOT bullet (and the two-namings header) paired
# with a parent-side witness substring. Honestly a *mapping-completeness*
# table: it certifies both columns occur in their own source note and that
# every enumerated Does-NOT key is covered; it does not assert equivalence.
# ----------------------------------------------------------------------------
MAPPING = [
    # key                c3-side (Does-NOT / header)   parent-side witness
    ("namings", C_TWONAME, P_RESIDUAL),
    ("supply", C_DN_SUPPLY, P_MINFORM),
    ("scoring_wall", C_DN_SCORE, P_CONTENTLESS),
    ("axiom_primitive", C_DN_AXIOM, P_REGISTRY),
    ("audit_status", C_DN_AUDIT, P_AUDIT),
]
MAPPING_EXPECTED_KEYS = {
    "namings",
    "supply",
    "scoring_wall",
    "axiom_primitive",
    "audit_status",
}


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
# sentence guards on the three read source files
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
    "C3 canonical note carries the ratification framing (naming ratification on already-landed surfaces; import-retirement path)",
    C_RATIFY in C3,
)
check(
    "C3 canonical note carries the two-namings sentence and both cell namings (outcome naming; channel naming)",
    has_all(C3, [C_TWONAME, C_OUTCOME, C_CHANNEL]),
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
    "axioms note carries both distinction clauses (Qubit possibility twin; Lattice site twin)",
    has_all(AX, [AX_QUBIT, AX_LATTICE]),
)

# ----------------------------------------------------------------------------
# T2 mapping-completeness (data-structure completeness, not equivalence)
# ----------------------------------------------------------------------------
check(
    "T2 mapping: every parent-side witness in the table occurs as a substring of the parent note",
    all(par in PARENT for (_k, _c3, par) in MAPPING),
)
check(
    "T2 mapping: every C3-side Does-NOT/header item in the table occurs as a substring of the C3 note",
    all(c3s in C3 for (_k, c3s, _par) in MAPPING),
)
check(
    "T2 mapping-completeness: every enumerated Does-NOT key (and the two-namings header) is paired -- no bullet dropped",
    set(k for (k, _c3, _par) in MAPPING) == MAPPING_EXPECTED_KEYS
    and len(MAPPING) == len(MAPPING_EXPECTED_KEYS),
)

# ----------------------------------------------------------------------------
# T3 exact witness 1 -- within-triplet naming vacuity: single C3 orbit
# ----------------------------------------------------------------------------
p = (1, 2, 0)  # C3 as a 3-cycle on the three corner labels {0,1,2}
p2 = compose(p, p)
p3 = compose(p2, p)
orbit0 = set()
x = 0
for _ in range(3):
    orbit0.add(x)
    x = p[x]
check(
    "T3 within-triplet: C3 acts as an order-3 3-cycle with a single transitive orbit {0,1,2} on the three corner labels",
    orbit0 == {0, 1, 2}
    and p3 == (0, 1, 2)
    and p != (0, 1, 2)
    and p2 != (0, 1, 2),
)

# ----------------------------------------------------------------------------
# T3 exact witness 2 -- carrier-triplet vacuity: unitary intertwiner identity
#   EH(dagger) EH = I, with the intertwining relation EH*C1 = C2*EH.
# hw=1 and hw=2 carry the same shared-orientation cyclic generator C1=C2=C3M;
# EH is a nontrivial (order-3) equivariant permutation between the carriers.
# ----------------------------------------------------------------------------
C1 = C3M
C2 = C3M
EH = C3M  # orientation-preserving equivariant permutation (a power of the shift)
EH_dag = dagger(EH)
identity_ok = matmul(EH_dag, EH) == I3
intertwine_ok = matmul(EH, C1) == matmul(C2, EH)
order3_ok = matmul(matmul(EH, EH), EH) == I3
nontrivial_ok = EH != I3
check(
    "T3 carrier: EH(dagger)EH = I (unitary), EH*C1 = C2*EH (intertwining), EH^3 = I, EH nontrivial -- exact integer arithmetic",
    identity_ok and intertwine_ok and order3_ok and nontrivial_ok,
)

# ----------------------------------------------------------------------------
# T3 exact witness 3 -- equivariant corner-weight equality (all exact Fractions):
#   a generic rational diagonal separates the corners (spread > 0), the C3
#   orbit-average forces them equal (spread = 0), yielding a scalar operator.
# ----------------------------------------------------------------------------
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
    "T3 corner-weight: generic rational diagonal separates (spread = 6 > 0); C3 orbit-average equalizes (spread = 0), Havg = 3*I, commutes with C3 -- exact",
    spread_generic == Fraction(6)
    and spread_generic > 0
    and spread_avg == Fraction(0)
    and Havg_is_scalar
    and equivariant_ok,
)

# ----------------------------------------------------------------------------
# T4 grade-scope greps on this note
# ----------------------------------------------------------------------------
check(
    "T4 scope: note states the bracketed above-grade content (taste/Dirac/chirality) and that sub-admissions (i) and (ii) are untouched",
    has_all(NOTE, [N_BRACKET, N_UNTOUCHED]),
)

# ----------------------------------------------------------------------------
# T5 governance-boundary greps on this note
# ----------------------------------------------------------------------------
check(
    "T5 boundary: note carries the boundary tokens (owner decision; morning; nothing adopted; grade; does not retire)",
    has_all(NOTE, [N_OWNER, N_MORNING, N_NOTHING, N_GRADE, N_RETIRE]),
)


# ----------------------------------------------------------------------------
# declared-open residue (informational; not counted as checks)
# ----------------------------------------------------------------------------
print("")
print("DECLARED-OPEN RESIDUE (conserved; owner surface, nothing adopted here):")
for line in (
    "the AC_phi_lambda(iii) identification -- pending the owner ratify/decline decision",
    "the bracketed above-C3-grade content (taste/Dirac/chirality; hw=1 vs hw=2 beyond C3)",
    "sub-admission (i) (occupancy/reading selection) -- untouched",
    "sub-admission (ii) (R-eta identification) -- untouched",
    "adjacent review-pending K-arc PRs #4831/#4835/#4837/#4840/#4845 (non-overlapping)",
    "adjacent note-level two-cell family PR #4853 (context only)",
    "audit statuses of all cited notes -- owned by the independent audit lane",
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
