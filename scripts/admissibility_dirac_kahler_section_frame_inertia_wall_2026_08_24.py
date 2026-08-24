#!/usr/bin/env python3
"""BLOCK 186 -- THE SECTION-FRAME PORT AND THE BALANCED-INERTIA WALL.

THE RESULT, AND ITS EXACT SCOPE.  On THE SECTION FRAME the Blocks 181-185 lane
landed -- the Block 128 8x4 cover of dimension 32 over the certified Block 105
curved carrier, the landed overlap field, the landed chart differential
d_00 = chart_differential_cover((0,0)), and the Block 184 completion convention
Q(H,d) = m*H + i*(H d + d^H H) -- and with the dressed reflection Px = P0*xpar,
the anchor reflection thA(t) = (-2-t)%8, the glued Hodge with a SELF-DUAL SEAM
BLOCK at the two straddling anchors, the derived D = A - Px A Px and the dressed
pairing K[a,b] = conj((G Px)[idx(b), idx(a)]) on the sixteen positive-half sites:
THE PORT PRODUCES THREE STRUCTURAL THEOREMS, A DERIVED SEAM MODULUS, AND A
BALANCED-INERTIA WALL WHOSE LINEAR-SYMMETRY MECHANISM IS EXCLUDED AS A THEOREM,
WHOSE THREE ESCAPE ROUTES ARE PROBED NEGATIVE, AND WHOSE CAUSE IS OPEN.
IT IS NOT A NO-GO.

  1. THE PORT IS NOT A TRANSFER, AND THAT IS THE FIRST RESULT (C).  F1: the
     chart differential is CELL-LOCAL -- all 32 entries of d_00 lie inside the
     2x2 even-anchored cells, with EXACTLY 0 crossing the far seam {3,4} and
     EXACTLY 0 crossing the near seam {7,0}, so an antiperiodic edge negation on
     this carrier is VACUOUS.  F2: the FLAT section-frame theory is
     DISCONNECTED -- the flat overlap Hodge is EXACTLY the 32x32 identity, so
     the flat completion is block-diagonal over sixteen disjoint cells and THE
     FLAT REFLECTED GRAM IS IDENTICALLY ZERO, rank 0 on all three spans, dressed
     and undressed alike.  NO FLAT CALIBRATION EXISTS ON THIS FAMILY: Block
     107's transfer strategy fails STRUCTURALLY, not numerically.  F3, IN THE
     FORM THE ADVERSARIAL CHECK CORRECTED IT TO: the curved no-glue completion
     carries EXACTLY 144 ORDERED inter-cell entries on EXACTLY 72 unordered
     edges, the curved Hodge itself carries EXACTLY 48 ORDERED entries on 24 of
     those edges, and EXACTLY 96 ORDERED entries are CREATED by the transport
     term beyond the Hodge's own support.  THE CAUSAL STATEMENT SURVIVES AND
     THE WORDING DOES NOT: the flat Hodge is the identity and carries ZERO
     inter-cell edges, so all 72 curved edges are H-INDUCED -- but "H-BORNE"
     MUST NOT BE READ AS "IN H's SUPPORT", because 96 of the 144 are not.

  2. THE SELECTION RULE, DIAGNOSED (D).  With FLAT seam blocks the glued
     action's support graph has EXACTLY TWO CONNECTED COMPONENTS AND THEY ARE
     THE TWO HALVES, sixteen sites each, at EXACTLY 0 cross-half entries.  theta
     swaps them, every (b, theta a) pair straddles, and the dressed Gram
     vanishes identically.  THE FIX IS DERIVED FROM DUALITY: the straddling
     anchors t = 3 and t = 7 are the fixed points of thA, so their blocks must
     be SELF-DUAL, and the DRESSED self-dual symmetric space
     B = (P4 Xi) B (P4 Xi)^T is EXACTLY 6-DIMENSIONAL with EXACTLY 4
     off-diagonal directions -- THE SEAM IS A MODULUS.  The shear family cannot
     supply it: the P4 self-duality residual of H(q,v) has the exact table
     gated below, and its EXACT solution set at nonzero volume is BOTH (0,1)
     AND (0,-1) -- so THE FLAT BLOCK IS THE UNIQUE SELF-DUAL MEMBER ONLY UNDER
     THE CONVENTIONAL POSITIVE-VOLUME RESTRICTION v > 0, which is stated
     wherever the lemma appears.  Under it, Block 107's forced-flat seam rows
     are RE-DERIVED FROM DUALITY.  All EIGHT landed field values are
     PYTHAGOREAN, so every field block is HALF self-dual and none is self-dual.

  3. THE CONSTRUCTION, EVERY PROPERTY MEASURED (E).  A is the 16 d_00 entries
     with both times in {0,1,2,3}; D = A - Px A Px carries EXACTLY 32 entries,
     is Px-ODD at zero residual, EQUALS d_00 entrywise on the positive half and
     is NOT d_00 globally.  H_g is POSITIVE DEFINITE by 32 exact leading minors
     and Px-EVEN at zero residual.  Q_g IS REAL -- the Block 185 C8 reality
     condition is SATISFIED by this construction -- and Px Q_g Px = Q_g^T at
     zero residual.  The halves CONNECT at 48 cross-half entries.  AND THE
     DRESSING IS WHAT MAKES THE PAIRING HERMITIAN: the dressed Gram's defect is
     EXACTLY 0 while the UNDRESSED formula's is 80 nonzero entries.

  4. THE WALL, W1: THE SEAM-DIRECTION SWEEP (F).  At m = 9/20 and s = 1/5 all
     six seam blocks are exactly self-dual and all six dressed Grams are exactly
     Hermitian.  THE INERTIAS: E02 seam (+6,-6,0x4); E13 seam (+6,-6,0x4); the
     b5-type mixed-sign seam (+3,-3,0x10) at rank 6; the adversarial check's TWO
     EXPLICIT GENERIC POINTS Bgen1 and Bgen2, BOTH (+6,-6,0x4) at rank 12 --
     TWO GENERIC POINTS AND NOT A UNIVERSAL "GENERIC" ASSERTION; and the b8-type
     seam THE ZERO GRAM, all sixteen zero.  AND THE ZERO IS THE DIAGNOSIS
     RECURRING RATHER THAN A MYSTERY: the b8-type direction couples slot 0 to
     slot 1 and slot 2 to slot 3, both at the SAME time inside a straddling
     cell, so it carries NO seam coupling -- it leaves two components of sixteen
     and 0 cross-half entries, exactly like a flat seam.  EXACTLY ONE of the
     four off-diagonal self-dual directions is coupling-free, and EVERY
     coupling-carrying direction tested is BALANCED.

  5. THE WALL, W2 AND W3, THE MECHANISM EXCLUDED, AND EVERY ESCAPE ROUTE
     NEGATIVE (G).  W2: the inertia is EXACTLY (+6,-6,0x4) at every one of
     m = 1/3, 9/20, 1, 2 and 10, and the PURE-GEOMETRY LIMIT -- K built from
     H_g^-1 alone, no completion at all -- is EXACTLY (+4,-4,0x8), BALANCED
     EVEN IN THE LIMIT.  W3, THE MECHANISM-EXCLUSION THEOREM, STRENGTHENED BY
     THE ADVERSARIAL CHECK: the charpoly of K has EXACTLY 6 NONZERO ODD-POWER
     COEFFICIENTS at powers 5, 7, 9, 11, 13, 15 with signs (-,+,+,-,+,-), so
     the spectrum is NOT plus-minus symmetric and no invertible S with
     S K S^-1 = -K exists; and EXACTLY, gcd(charpoly(x), charpoly(-x)) = x^4,
     so NO nonzero eigenvalue is paired with its negative, THE ANTI-COMMUTANT
     {S : S K + K S = 0} HAS DIMENSION EXACTLY 16 = 4^2, EVERY MEMBER IS
     KERNEL-SUPPORTED AND NONE IS INVERTIBLE.  AND THE THREE ESCAPE ROUTES ARE
     ALL NEGATIVE: the TRACE IDENTITY IS DEAD (tr K strictly positive at all
     five masses); the ANTILINEAR ROUTE COLLAPSES (K IS REAL, so
     S conj(K) S^-1 = -K IS the already-excluded linear similarity, with direct
     residuals nonzero at rank 16); and THE GAMMA0 TWO-SIDED DRESSING IS NOT AN
     INDEPENDENT CANDIDATE AT ALL, because K2 = xpar K xpar IS A CONGRUENCE of
     K and Sylvester therefore FORCES its measured (+6,-6,0x4).  NO TESTED
     VARIANT IS POSITIVE DEFINITE.  THE BALANCED INERTIA HAS NO LINEAR
     ANTI-SYMMETRY MECHANISM AND ITS CAUSE IS OPEN.

WHAT IS NOT CLAIMED, STATED ONCE: THIS IS NOT A NO-GO.  The wall is PER-PAIRING
and PER-FRAME: ONE fixture, ONE pairing family, ONE seam modulus at ONE value of
s.  NO OS POSITIVITY IS ESTABLISHED ON THIS FRAME at any scope; NO MECHANISM for
the balance is known; NO PAIRING-GENERALITY is claimed, and the note names SEVEN
UNTESTED VARIANT CLASSES as the wall's boundary.  BLOCK 185's LANDED POSITIVITY
ON THE BLOCK 107 CARRIER IS UNTOUCHED BY EVERYTHING HERE, that being a DIFFERENT
CARRIER.  This block characterizes WHY the section frame's FIRST pairing family
does not reproduce Block 185's positive Gram: it is COMPLEMENTARY to Block 185
and NOT CONTRADICTORY.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 185 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the eight audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: six imposed objects,
     ZERO registered and ZERO adopted, with the NO-GO, the frame's OS
     positivity, the mechanism, pairing-generality and any touching of Block
     185's landed positivity ALL declared NOT CLAIMED as measured constants.
  C  THE PORT'S STRUCTURAL THEOREMS F1-F3: cell-locality at 32 entries with 0
     far-seam and 0 near-seam hops, the flat overlap Hodge exactly I_32 with the
     flat reflected Gram at rank 0 on three spans, and THE CORRECTED INTER-CELL
     CENSUS -- 144 ordered on 72 edges, 48 ordered in the Hodge's own support,
     96 ordered created by the transport term, and zero inter-cell edges at
     flat.
  D  THE DIAGNOSIS AND THE SEAM MODULUS: two 16-site components under a flat
     seam with theta swapping them and a zero dressed Gram, the 6-dimensional
     dressed self-dual space with 4 off-diagonal directions, the exact
     self-duality residual table with BOTH exact solutions (0,1) and (0,-1) and
     the POSITIVE-VOLUME restriction that makes flat unique, and the Pythagorean
     landed field.
  E  THE CONSTRUCTION: Q_g real, Px-covariance exact, the halves connected at 48
     cross-half entries, D Px-odd at 32 entries and equal to d_00 on the
     positive half, H_g positive definite and Px-even, the dressed Gram exactly
     Hermitian and the UNDRESSED one measurably not.
  F  THE WALL W1: the six seam-direction inertias BY TWO INDEPENDENT EXACT
     METHODS -- charpoly Descartes and congruence elimination -- the b8-type
     ZERO GRAM with its coupling-free diagnosis, and every seam block exactly
     self-dual.
  G  THE WALL W2 AND W3 AND THE ESCAPE ROUTES: the five-point mass sweep, the
     pure-geometry limit, the 6 nonzero odd coefficients with their signs,
     gcd(charpoly(x), charpoly(-x)) = x^4 with the anti-commutant dimension it
     forces, the four diagonal candidates, the congruence pivot signature, and
     ALL THREE ESCAPE ROUTES MEASURED NEGATIVE.
  H  the note at its final path and the N5 fence, byte-identical.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: seventeen declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_no_go, claim_mechanism_known
    C  break_cell_locality, break_flat_gram_zero, break_intercell_census
    D  break_two_components, break_selfdual_dim
    E  break_construction_real
    F  break_wall_inertia
    G  break_odd_coefficients, break_mass_sweep, break_gcd_exclusion,
       break_escape_routes
    H  drop_n5_fence
  THE TWO THAT GUARD THE BLOCK'S SINGLE BIGGEST OVERREACH RISK ARE claim_no_go
  AND claim_mechanism_known.  A wall that survives six seam directions, five
  masses, the geometry limit AND three escape probes READS AS A NO-GO unless the
  banner says it is not, and it is measurably not one: one pairing family is
  tested and seven variant classes are named untested.  A mechanism-exclusion
  theorem READS AS an explanation unless the banner says the cause is OPEN.
  AND break_intercell_census GUARDS THIS BLOCK'S OWN LANDED CORRECTION: it
  asserts the superseded "96 as the total", which the corrected 144/72/48/96
  census forbids.
  BEFORE LANDING GATE H ALREADY FAILS AT BASELINE, on note-at-final-path alone,
  so drop_n5_fence cannot flip it and THE SWEEP IS RUN AT LANDING, once the note
  sits at docs/ and the baseline is 8 of 8 by family.

RUNNING
  python3 scripts/admissibility_dirac_kahler_section_frame_inertia_wall_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation break_wall_inertia

NOTES FOR THE LANDING AGENT
  1. NOTHING from any scratchpad is imported OR READ.  The LANDED Block 128
     runner is imported for EXACTLY FIVE objects -- cover_index(),
     cover_embedding(), chart_differential_cover(), and through it the Block 105
     module's shear_hodge() and overlap_field() -- and for nothing else.  The
     dressed reflection, the anchor reflection, the glued Hodge, the seam
     family, the restricted set, the derived glue and the dressed pairing are
     ALL BUILT DIRECTLY HERE.
  2. EVERY CHECK IS EXACT, AND THE INERTIA IS MEASURED TWICE BY DISJOINT
     METHODS.  sympy Rational and Integer arithmetic only; no float enters any
     measured object and no tolerance is used anywhere.  Route one is the
     characteristic polynomial over the rationals plus Descartes' rule, which is
     EXACT rather than a bound because a Hermitian matrix has only real
     eigenvalues, so the sign-variation count equals the positive count
     outright.  Route two is SYMMETRIC CONGRUENCE ELIMINATION with exact
     pivoting -- Sylvester's law -- which touches neither the charpoly nor any
     polynomial arithmetic.  GATE F REQUIRES THE TWO ROUTES TO AGREE ON EVERY
     SEAM DIRECTION.  This is the same disjointness the adversarial check used.
  3. sp.nsimplify IS NOT APPLIED TO ANY MEASURED SCALAR ANYWHERE IN THIS RUNNER,
     AND THAT IS DELIBERATE.  nsimplify carries a rational TOLERANCE and returns
     EXACTLY ZERO for a small nonzero rational -- sp.nsimplify(Rational(1,10**200))
     is 0 -- so a charpoly coefficient passed through it can silently lose its
     sign and change a measured inertia.  This was CAUGHT IN THE DRAFT by the
     mass sweep, where an nsimplify'd coefficient vector reported (+5,-5,0x6) at
     m = 10 against the true (+6,-6,0x4); the true value is confirmed by rank,
     by high-precision eigenvalues and by exact congruence.  The volume and the
     shears here are already sympy Rationals from the LANDED Block 105 field, so
     nothing needs converting and nothing is converted.
  4. The N5 fence appears byte-identically in the note; gate H checks it as a
     raw substring.
  5. PARENT_COMMIT is the Block 185 tip and PARENT_REF resolves to it; nothing
     needs sed, and CURRENT_MAIN was carried forward from the Block 185 runner
     and re-resolved at draft time.
  6. The stale pin is the Block 184 tip, a real ancestor of HEAD that predates
     Block 185 and carries NEITHER Block 185 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  7. THE ADVERSARIAL CHECK IS FOLDED AND ITS THREE CORRECTIONS ARE GATED, NOT
     NARRATED.  Its verdict was CONFIRMED-WITH-CORRECTIONS and it re-derived the
     wall by INDEPENDENT CONGRUENCE ELIMINATION.  (i) THE INTER-CELL CENSUS was
     REFUTED AS STATED and the corrected 144/72/48/96 numbers are gated in
     family C -- this is THE FOURTEENTH SUPERVISOR CORRECTION and it is this
     block's own.  (ii) THE SELF-DUALITY LEMMA holds only at POSITIVE VOLUME,
     the exact solution set being (0,1) AND (0,-1); both points and the exact
     residual table are gated in family D.  (iii) THE ORIGINAL "GENERIC MIXED
     SEAM" WAS NOT REPRODUCIBLE and is REPLACED by the check's two explicit
     representatives Bgen1 and Bgen2, both gated in family F.  NO PLACEHOLDER
     SLOT REMAINS IN THIS RUNNER: ESCAPE_ROUTE_VERDICTS is FILLED and each of
     its three verdicts is backed by a measurement in family G.
  8. THREE IN-SOLVE CATCHES are recorded as PROCESS in N7 and none is a landed
     correction: the vacuous antiperiodic edge negation (killed by F1 in the
     same measurement that found it), the first negative-half image built
     WITHOUT the within-block xpar flip (which failed covariance at 144 entries)
     and the reading that the glued action was NOT REAL (a symbolic-assumptions
     artifact).  The third is now a PERMANENT GATE: gate E measures the exact
     reality of Q_g.  AND ONE VARIANT-DESIGN ERROR IS DISCLOSED RATHER THAN
     BURIED: the Gamma0 two-sided dressing was proposed as an INDEPENDENT escape
     candidate and it IS A CONGRUENCE, so Sylvester forced its inertia before it
     was ever measured.  The checker identified it; gate G measures the
     congruence relation itself, so the disclosure is a gate and not a sentence.
  9. Re-run at landing; gate H should then pass, the battery should be 8/8 by
     family, and the seventeen-mutation sweep should be run then.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORT, LANDED, AND DELIBERATELY THIN.  Unlike Block 185 -- which
# worked on Block 107's carrier and could import almost nothing -- this block IS
# on the Block 128 chart family, so the CARRIER comes from the LANDED runner and
# only the port's own objects are built here.  FIVE landed objects are imported:
# cover_index(), cover_embedding(), chart_differential_cover(), and through the
# Block 105 module it re-exports, shear_hodge() and overlap_field().  NOTHING
# from any scratchpad is imported or read anywhere.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_SECTION_FRAME_INERTIA_WALL_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 185 is the commit this block's branch
# is cut from, and its note and its runner are the pair that distinguishes the
# parent pin from the stale pin: both exist at PARENT_COMMIT and NEITHER exists
# at STALE_PARENT_COMMIT.
BLOCK185_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK185_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK185_NOTE, BLOCK185_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "5cc1f21899b24daa796b2eb0ca51193c8bf83cd8",   # Block 185 note
    "c900f46234bc6d7dbb23c1a4f33c534448b5e609",   # Block 185 runner
)
# THE TEMPORAL-LINK GRANDPARENT, whose completion convention this block uses.
BLOCK184_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK184_RUNNER = (
    "scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py"
)
# THE REFLECTION AUTHORITY: Px, the site permutation and the x-parity dressing
# are Block 183's derived objects, rebuilt here.
BLOCK183_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
# THE CARRIER PARENT, imported for exactly five objects and read as an input.
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"
# THE ADVERSARIAL CHECK'S FINDINGS, preserved.  It is CITED for the exact giant
# rationals it displayed and is NOT read by this runner: every number gated here
# is re-measured here.
CHECK_FINDINGS = (
    ".claude/science/physics-loops/generator-program-20260821/"
    "b186_check_findings.md"
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time -- this block's own note excepted,
# since it lands later and gate H is the gate that owns it.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SECTION_FRAME_INERTIA_WALL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
# THE BLOCK'S OWN NOTE is the one audit input gate A does NOT require readable,
# because it does not exist until landing and gate H is the gate that owns it.
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 185 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 185 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block185-"
              "curved-os-seam-glued-gram-20260824")
PARENT_COMMIT = "4d411820f1c19b4130db8ab064a79ba8e86f0fc8"
# The Block 184 tip: a real ancestor of HEAD that predates Block 185 and
# therefore carries NEITHER Block 185 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "1702e73876839f0ba01f5ff28bfe26ed5d370987"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_no_go",
    "claim_mechanism_known",
    "break_cell_locality",
    "break_flat_gram_zero",
    "break_intercell_census",
    "break_two_components",
    "break_selfdual_dim",
    "break_construction_real",
    "break_wall_inertia",
    "break_odd_coefficients",
    "break_mass_sweep",
    "break_gcd_exclusion",
    "break_escape_routes",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_no_go": "B",
    "claim_mechanism_known": "B",
    "break_cell_locality": "C",
    "break_flat_gram_zero": "C",
    "break_intercell_census": "C",
    "break_two_components": "D",
    "break_selfdual_dim": "D",
    "break_construction_real": "E",
    "break_wall_inertia": "F",
    "break_odd_coefficients": "G",
    "break_mass_sweep": "G",
    "break_gcd_exclusion": "G",
    "break_escape_routes": "G",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def families(self) -> dict:
        summary: dict[str, bool] = {}
        for key, _, value in self.results:
            family = key.split("-", 1)[0]
            summary[family] = summary.get(family, True) and value
        return summary

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print("GATES " + " ".join(
            f"{family}={'PASS' if value else 'FAIL'}"
            for family, value in self.families().items()))

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC).strip()


def worktree_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", path), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def commit_blob(commit: str, path: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC).returncode == 0


def is_hash(value: str) -> bool:
    import re as _re
    return _re.fullmatch(r"[0-9a-f]{40}", value) is not None


def is_placeholder(value: str) -> bool:
    """A DECLARED placeholder is 40 hex characters that are all zero but the
    trailing block tag.  It is hash-SHAPED and is never a resolvable commit."""
    return is_hash(value) and value.startswith("0" * 30)


def audit_inputs_readable() -> tuple:
    """(readable count, missing paths).  THE BLOCK'S OWN NOTE IS EXCLUDED, since
    it does not exist until landing and gate H is the gate that owns it."""
    missing = tuple(
        path for path in AUDIT_INPUT_PATHS
        if path != SELF_NOTE_INPUT and not (ROOT / path).is_file())
    return len(AUDIT_INPUT_PATHS) - 1 - len(missing), missing


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    machinery_import_landed: bool
    inputs_readable: int
    inputs_missing: tuple


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT):
        return PARENT_COMMIT
    resolved = resolve_ref(PARENT_REF)
    return resolved if is_hash(resolved) else git_output("rev-parse", "HEAD")


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB)
    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(commit_blob(parent, p) for p in PARENT_ARTIFACTS)
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, p) for p in PARENT_ARTIFACTS)
    readable, missing = audit_inputs_readable()
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT),
        bool(is_hash(parent) and is_ancestor(parent, "HEAD")
             and (is_placeholder(PARENT_COMMIT)
                  or resolve_ref(PARENT_REF) == PARENT_COMMIT)),
        bool(len(committed_blobs) == len(PARENT_ARTIFACTS) == 2
             and all(is_hash(v) for v in committed_blobs)
             and committed_blobs == worktree_blobs
             and committed_blobs == PARENT_ARTIFACT_BLOBS),
        # THE STALE LEG.  At the Block 184 tip NEITHER Block 185 artifact
        # exists, so this is False and the stale mutation fails gate A.
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        MACHINERY_IMPORT_LANDED,
        readable,
        missing)


# ---------------------------------------------------------------------------
# B. the imposed objects and the NOT-CLAIMED keys, as measured literals
# ---------------------------------------------------------------------------
IMPOSED_OBJECTS = (
    "THE SECTION FRAME as the Blocks 181-185 lane landed it: the LANDED Block 128 8x4 cover of dimension 32 with idx(t,x) = (t%8)*4 + x%4, the LANDED Block 105 overlap field, the LANDED chart differential d_00 = chart_differential_cover((0,0)), and the Block 184 completion convention Q(H,d) = m*H + i*(H d + d^H H) -- the carrier is IMPORTED FROM THE LANDED RUNNER and is never rebuilt here",
    "THE DRESSED REFLECTION Px = P0 * xpar, with P0 the site permutation of theta(t) = (-1-t)%8 and xpar = diag((-1)^x) -- Block 183's transpose-symmetry variant, rebuilt -- together with the ANCHOR REFLECTION thA(t) = (-2-t)%8, the UNSIGNED offset permutation P4 = [[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]] and the sign Xi = diag(1,-1,1,-1)",
    "THE GLUED HODGE H_g, WHICH IS THIS BLOCK'S OWN OBJECT: plain field blocks H(q,v) at t in {0,1,2}, the SHEAR-FLIPPED P4-image blocks P4 H(-q,v) P4^T at the thA-reflected field for t in {4,5,6}, a self-dual SEAM BLOCK B at the two straddling anchors t in {3,7}, and the x-minimal average (H + Ux^T H Ux)/2 -- Block 183's minimal reflection-closed frame",
    "THE SEAM MODULUS FAMILY, the DRESSED self-dual symmetric blocks B = (P4 Xi) B (P4 Xi)^T, and the SIX tested directions at s = 1/5: the E02 seam, the E13 seam, the b5-type mixed-sign seam, the b8-type seam, and the adversarial check's TWO EXPLICIT GENERIC POINTS Bgen1 and Bgen2 -- two POINTS and not a universal generic assertion",
    "THE RESTRICTED SET A -- the d_00 entries with both endpoint times in {0,1,2,3} -- and the derived glue D = A - Px A Px, with the glued action Q_g = m*H_g + i*(H_g D + D^H H_g)",
    "THE DRESSED PAIRING K[a,b] = conj((G Px)[idx(b), idx(a)]) with G = Q_g^-1 on Lambda_+ = the sixteen sites with t in {0,1,2,3} in t-major order, together with its UNDRESSED neighbour conj(G(b, theta a)) and the Gamma0 two-sided variant xpar K xpar, both of which are built ONLY to be measured failing",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS rather than prose, so
# the B mutations bite on an object.  ALL FIVE ARE FALSE AND STAY FALSE.  THE
# FIRST IS THE ONE THAT MATTERS MOST: a wall that survives six seam directions,
# five masses, the geometry limit and three escape probes READS AS A NO-GO, and
# it is not one.
NO_GO_CLAIMED = False
OS_POSITIVITY_ON_THIS_FRAME_CLAIMED = False
MECHANISM_KNOWN = False
PAIRING_GENERALITY_CLAIMED = False
B185_POSITIVITY_TOUCHED = False

# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
ZERO_RESIDUAL = 0
TIME_EXTENT = 8
SPACE_EXTENT = 4
COVER_SIZE = TIME_EXTENT * SPACE_EXTENT
SPAN_SIZE = 16
# C -- THE PORT'S STRUCTURAL THEOREMS.
D00_NONZEROS = 32
FAR_SEAM_HOPS = 0
NEAR_SEAM_HOPS = 0
FLAT_GRAM_RANK = 0
# THE CORRECTED INTER-CELL CENSUS, as the adversarial check refuted and rebuilt
# it.  THE ORIGINAL "96 H-BORNE ENTRIES" WAS THE ORDERED SUPPORT INCREMENT
# MISLABELLED AS THE TOTAL.  144 ordered on 72 edges is the total; 48 ordered on
# 24 edges is the Hodge's own share; 96 ordered are created by the transport
# term; and the FLAT Hodge carries zero inter-cell edges, which is what makes
# all 72 curved edges H-INDUCED.
CURVED_INTER_CELL_ORDERED = 144
CURVED_INTER_CELL_EDGES = 72
HODGE_INTER_CELL_ORDERED = 48
HODGE_INTER_CELL_EDGES = 24
TRANSPORT_CREATED_ORDERED = 96
FLAT_INTER_CELL_ORDERED = 0
DIFFERENTIAL_INTER_CELL = 0
# D -- THE DIAGNOSIS AND THE SEAM MODULUS.
FLAT_SEAM_COMPONENTS = (16, 16)
FLAT_SEAM_CROSS_HALF = 0
SELF_DUAL_DIMENSION = 6
SELF_DUAL_OFF_DIAGONAL = 4
SELF_DUALITY_RESIDUAL_ENTRIES = 8
# BOTH exact solutions at nonzero volume.  FLAT IS UNIQUE ONLY AT v > 0.
SELF_DUAL_SHEAR_POINTS = ((0, 1), (0, -1))
FIELD_VALUE_COUNT = 8
# E -- THE CONSTRUCTION.
RESTRICTED_NONZEROS = 16
GLUE_NONZEROS = 32
CROSS_HALF_ENTRIES = 48
UNDRESSED_DEFECT_ENTRIES = 80
DRESSED_NONZEROS = 160
DRESSED_RANK = 12
# F -- THE WALL, W1.  THE INERTIA TRIPLES ARE (positive, negative, zero).
BALANCED_INERTIA = (6, 6, 4)
B5_TYPE_INERTIA = (3, 3, 10)
ZERO_GRAM_INERTIA = (0, 0, 16)
B5_TYPE_RANK = 6
COUPLING_FREE_COMPONENTS = (16, 16)
# THE CONGRUENCE PIVOT SIGNATURE at the E02 seam, from the INDEPENDENT route.
E02_PIVOT_SIGNATURE = "-+-+-+-+-+-+0000"
# G -- THE WALL, W2 AND W3.
MASS_SWEEP = (sp.Rational(1, 3), sp.Rational(9, 20), sp.Integer(1),
              sp.Integer(2), sp.Integer(10))
GEOMETRY_LIMIT_INERTIA = (4, 4, 8)
ODD_COEFFICIENT_COUNT = 6
ODD_COEFFICIENT_POWERS = (5, 7, 9, 11, 13, 15)
ODD_COEFFICIENT_SIGNS = (-1, 1, 1, -1, 1, -1)
KERNEL_DIMENSION = 4
# THE STRENGTHENED EXCLUSION: gcd(charpoly(x), charpoly(-x)) = x^4 EXACTLY, so
# no nonzero eigenvalue is paired with its negative and the anti-commutant is
# exactly the 4x4 block of maps ker(K) -> ker(K): dimension 16, all singular.
SPECTRAL_GCD_DEGREE = 4
ANTICOMMUTANT_DIMENSION = 16
DIAGONAL_CANDIDATE_COUNT = 4
ANTILINEAR_RESIDUAL_ENTRIES = (80, 80, 64, 64)
ANTILINEAR_RESIDUAL_RANK = 16
GAMMA0_INERTIA = (6, 6, 4)
GAMMA0_RANK = 12

# THE ESCAPE-ROUTE VERDICTS, SUPPLIED BY THE SUPERVISOR AFTER THE ADVERSARIAL
# CHECK LANDED.  Each is backed by a MEASUREMENT in gate G rather than by this
# string: the strings name the routes and the gate does the work.  ALL THREE ARE
# NEGATIVE AND THE WALL STANDS.
ESCAPE_ROUTE_NAMES = ("trace_identity", "antilinear_candidates",
                      "gamma0_two_sided_dressing")
ESCAPE_ROUTE_VERDICTS = {
    "trace_identity":
        "DEAD. tr K is STRICTLY POSITIVE at all five masses -- it is not zero, "
        "so no trace identity forces the balance and none is available as an "
        "escape. The exact giant rationals are displayed in the findings file; "
        "the positivity is re-measured here at every mass in the sweep.",
    "antilinear_candidates":
        "COLLAPSES. K IS REAL, so the antilinear condition "
        "S conj(K) S^-1 = -K IS the linear similarity S K S^-1 = -K, which W3 "
        "ALREADY EXCLUDES. The direct residuals confirm it: the four diagonal "
        "candidates give rank-16 residuals at 80/80/64/64 entries, and the "
        "half-reflection composites give 200-208 entries in the findings file.",
    "gamma0_two_sided_dressing":
        "NOT AN INDEPENDENT CANDIDATE. K2 = xpar K xpar is a CONGRUENCE of K "
        "by a real symmetric involution, so SYLVESTER'S LAW forces its inertia "
        "to equal K's before it is ever computed -- measured (+6,-6,0x4) at "
        "rank 12, Hermitian. The variant's design was the supervisor's error "
        "and the checker's identification of it is what closed the route.",
}

# THE CITATION PINS, read from the PRIMARY BODIES so this block's conventions,
# the hand-off it answers and the scope it must not overrun all have a measured
# referent and are never a recollection.
B185_REOPEN_PIN = "THE SECTION-FRAME PORT IS ATTEMPTED"
B185_SCOPE_PIN = "NOT A STATEMENT ON THE BLOCKS 181-184 SECTION FRAME"
B184_GRAM_PIN = "NO TWO-HISTORY GRAM IS BUILT"
B183_POSITIVITY_PIN = "NOT AN OS OR REFLECTION-POSITIVITY THEOREM"
CAMPAIGN_PORT_PIN = "THE PORT IS NOT A TRANSFER"

# THE H-FAMILY SCOPE KEYS.  The set is required WHOLE by gate H, which is what
# gives drop_n5_fence its teeth: dropping a key from the required set makes the
# required set differ from the declared set and the gate fails.
SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is involved
    at any point."""
    return nonzero_entries(sp.expand(matrix))


def leading_minors(matrix: sp.Matrix) -> tuple:
    """The leading principal minors as exact rational determinants by the
    Berkowitz algorithm: no eigenvalue estimate and no tolerance."""
    return tuple(matrix[:size, :size].det(method="berkowitz")
                 for size in range(1, matrix.rows + 1))


def positive_definite(matrix: sp.Matrix) -> bool:
    return all(value > 0 for value in leading_minors(matrix))


LAMBDA = sp.Symbol("lam")


def charpoly_coefficients(matrix: sp.Matrix) -> tuple:
    """The characteristic polynomial's coefficients in ASCENDING powers, exact.

    NO nsimplify IS APPLIED HERE OR ANYWHERE ELSE IN THIS RUNNER.  nsimplify
    carries a rational tolerance and maps a small nonzero rational to EXACTLY
    ZERO, which silently changes a measured inertia; the draft hit that at
    m = 10.  The entries are already exact rationals, so nothing needs it."""
    return tuple(reversed(
        sp.Poly(matrix.charpoly(LAMBDA).as_expr(), LAMBDA).all_coeffs()))


def inertia(matrix: sp.Matrix) -> tuple:
    """(positive, negative, zero), EXACTLY, for a HERMITIAN matrix -- ROUTE ONE.

    The zero count is the multiplicity of the root 0, which is the number of
    vanishing trailing charpoly coefficients.  The positive and negative counts
    are Descartes sign variations on the remaining factor -- and Descartes is
    EXACT here rather than a bound, because a Hermitian matrix has only REAL
    eigenvalues and for a real-rooted polynomial the sign-variation count EQUALS
    the positive-root count."""
    coefficients = charpoly_coefficients(matrix)
    zero = 0
    while zero < len(coefficients) and coefficients[zero] == 0:
        zero += 1
    tail = coefficients[zero:]

    def variations(sequence) -> int:
        signs = [sp.sign(value) for value in sequence if value != 0]
        return sum(1 for left, right in zip(signs, signs[1:]) if left != right)

    return (variations(tail),
            variations([value * (-1) ** power
                        for power, value in enumerate(tail)]),
            zero)


def congruence_pivots(matrix: sp.Matrix) -> tuple:
    """THE PIVOT SIGNS of exact symmetric congruence elimination -- ROUTE TWO.

    SYLVESTER'S LAW OF INERTIA, run directly: repeatedly pivot on a nonzero
    diagonal entry (permuting symmetrically to find one, and when the whole
    diagonal vanishes applying the elementary congruence that adds one row and
    column to another to create one), record the pivot's sign, and pass to the
    exact Schur complement.  THIS ROUTE NEVER FORMS A CHARACTERISTIC POLYNOMIAL
    AND NEVER DOES POLYNOMIAL ARITHMETIC, so its agreement with `inertia` above
    is a genuine two-method check and not a restatement.  It is the route the
    adversarial check used."""
    work = sp.MutableDenseMatrix(sp.expand(matrix))
    size = work.rows
    signs: list[int] = []
    while size > 0:
        if all(work[i, j] == 0 for i in range(size) for j in range(size)):
            signs.extend([0] * size)
            break
        pivot = next((i for i in range(size) if work[i, i] != 0), None)
        if pivot is None:
            row, column = next(
                (i, j) for i in range(size) for j in range(size)
                if i != j and work[i, j] != 0)
            elementary = sp.eye(size)
            elementary[row, column] = 1
            work = sp.MutableDenseMatrix(
                sp.expand(elementary * work * elementary.T))
            continue
        if pivot != 0:
            work = sp.MutableDenseMatrix(work)
            work.row_swap(0, pivot)
            work.col_swap(0, pivot)
        head = work[0, 0]
        signs.append(1 if head > 0 else -1)
        work = sp.MutableDenseMatrix(
            sp.expand(work[1:, 1:] - work[1:, 0] * work[0, 1:] / head))
        size -= 1
    return tuple(signs)


def congruence_inertia(matrix: sp.Matrix) -> tuple:
    signs = congruence_pivots(matrix)
    return (signs.count(1), signs.count(-1), signs.count(0))


def pivot_signature(signs: tuple) -> str:
    return "".join("+" if s == 1 else ("-" if s == -1 else "0") for s in signs)


def is_exact_real(value: object) -> bool:
    expression = sp.sympify(value)
    return bool(expression.is_rational and not expression.is_Float)


# ---------------------------------------------------------------------------
# THE SECTION FRAME.  The CARRIER is the LANDED Block 128 object; everything in
# this section that is not the carrier is this block's own port machinery.
# ---------------------------------------------------------------------------
MASS = sp.Rational(9, 20)
SEAM_PARAMETER = sp.Rational(1, 5)
POSITIVE_TIMES = (0, 1, 2, 3)
PLAIN_TIMES = (0, 1, 2)
SEAM_TIMES = (3, 7)
FAR_SEAM = frozenset({3, 4})
NEAR_SEAM = frozenset({7, 0})
# BLOCK 107's eq (15) UNSIGNED offset permutation, as Block 185 read it and as
# this block's anchor reflection needs it.
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])
# THE DRESSING SIGN.  Xi is what turns the P4 self-duality condition into the
# DRESSED one whose solution space is the seam modulus.
XI = sp.diag(1, -1, 1, -1)
LAMBDA_PLUS = tuple((t, x) for t in POSITIVE_TIMES for x in range(SPACE_EXTENT))
SHEAR_SYMBOL, VOLUME_SYMBOL = sp.symbols("q v")


def site_index(time_coordinate: int, space_coordinate: int) -> int:
    """idx(t,x) = (t mod 8)*4 + (x mod 4), the LANDED Block 128 cover_index."""
    return b128.cover_index(time_coordinate, space_coordinate)


def cover_shift(delta_t: int, delta_x: int) -> sp.Matrix:
    """The PLAIN translation on the cover; U_x is the x-minimal frame's shift."""
    shift = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            shift[site_index(time + delta_t, space + delta_x),
                  site_index(time, space)] = 1
    return shift


def site_reflection() -> sp.Matrix:
    """P0: the SITE permutation theta(t) = (-1-t)%8, Block 183's P_edge."""
    matrix = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            matrix[site_index((-1 - time) % TIME_EXTENT, space),
                   site_index(time, space)] = 1
    return matrix


def space_parity(times: tuple = tuple(range(TIME_EXTENT))) -> sp.Matrix:
    """xpar = diag((-1)^x), Block 183's x-parity dressing.  On the whole cover
    it is the reflection's dressing; restricted to the positive-half times it
    is the Gamma0 two-sided dressing applied to the pairing."""
    return sp.diag(*[sp.Integer(-1) ** space
                     for _ in times for space in range(SPACE_EXTENT)])


def cells() -> tuple:
    """The sixteen 2x2 EVEN-ANCHORED cells, as site-index sets.  They are the
    cells d_00 = chart_differential_cover((0,0)) is built on."""
    return tuple(
        frozenset(site_index(2 * coarse_t + dt, 2 * coarse_x + dx)
                  for dt in (0, 1) for dx in (0, 1))
        for coarse_t in range(TIME_EXTENT // 2)
        for coarse_x in range(SPACE_EXTENT // 2))


def shear_block(shear: object, volume: object) -> sp.Matrix:
    """The LANDED Block 105 shear Hodge, read through Block 128."""
    return b128.block105.shear_hodge(shear, volume)


def hodge_from_blocks(block) -> sp.Matrix:
    """H = (1/4) sum_n E_n B(n) E_n^T over all 32 anchors, with the LANDED
    Block 128 cover_embedding as E_n -- the landed construction with the CELL
    BLOCK left free, which is what lets the glued Hodge be built by it."""
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            embedding = b128.cover_embedding(time, space)
            result += embedding * block(time, space) * embedding.T / 4
    return sp.expand(result)


def completion(hodge: sp.Matrix, differential: sp.Matrix,
               mass: object = MASS) -> sp.Matrix:
    """THE LANDED Block 184 completion convention Q = m*H + i*(H d + d^H H),
    used UNCHANGED for the flat control, the curved control, the glued action at
    every seam direction and every mass point, so no comparison below is between
    different conventions."""
    return sp.expand(mass * hodge
                     + sp.I * (hodge * differential + differential.H * hodge))


def transport_term(hodge: sp.Matrix, differential: sp.Matrix) -> sp.Matrix:
    """The completion's second half, i(H d + d^H H) -- the part that CREATES
    inter-cell support beyond the Hodge's own."""
    return sp.expand(sp.I * (hodge * differential + differential.H * hodge))


def glued_hodge(seam_block: sp.Matrix, field: dict,
                spatial_shift: sp.Matrix) -> sp.Matrix:
    """THE GLUED HODGE, WHICH IS THIS BLOCK'S OWN OBJECT.

    t in {0,1,2}: the PLAIN landed field block H(q,v).
    t in {4,5,6}: the SHEAR-FLIPPED P4-image block P4 H(-q,v) P4^T at the
                  thA-reflected field, thA(t) = (-2-t)%8 -- the within-block
                  xpar flip is the reflection-odd ADM parity, and the first
                  attempt without it failed covariance at 144 entries.
    t in {3,7}:   the SEAM BLOCK, which must be SELF-DUAL because those two
                  anchors are the FIXED POINTS of thA.
    Then the x-MINIMAL AVERAGE (H + U_x^T H U_x)/2, Block 183's minimal
    reflection-closed frame."""
    def block(time, space):
        if time in SEAM_TIMES:
            return seam_block
        if time in PLAIN_TIMES:
            shear, volume = field[(time % (TIME_EXTENT // 2), space)]
            return shear_block(shear, volume)
        reflected = (-2 - time) % TIME_EXTENT
        shear, volume = field[(reflected % (TIME_EXTENT // 2), space)]
        return sp.expand(OFFSET_PERMUTATION
                         * shear_block(-shear, volume)
                         * OFFSET_PERMUTATION.T)
    raw = hodge_from_blocks(block)
    return sp.expand((raw + spatial_shift.T * raw * spatial_shift) / 2)


def restricted_raising(differential: sp.Matrix) -> sp.Matrix:
    """A: the d_00 entries whose BOTH endpoint times lie in the positive half
    {0,1,2,3}.  THE PHYSICAL HALF AND NOTHING ELSE -- and unlike Block 185 there
    is no seam term to add, because F1 says d_00 has NO seam entries at all."""
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if differential[row, column] == 0:
                continue
            if (row // SPACE_EXTENT in POSITIVE_TIMES
                    and column // SPACE_EXTENT in POSITIVE_TIMES):
                result[row, column] = differential[row, column]
    return result


def pairing_from_resolvent(resolvent: sp.Matrix) -> sp.Matrix:
    return sp.expand(sp.Matrix(SPAN_SIZE, SPAN_SIZE, lambda row, column:
                               sp.conjugate(resolvent[
                                   site_index(*LAMBDA_PLUS[column]),
                                   site_index(*LAMBDA_PLUS[row])])))


def dressed_gram(action: sp.Matrix, reflection: sp.Matrix) -> sp.Matrix:
    """THE DRESSED PAIRING: K[a,b] = conj((G Px)[idx(b), idx(a)]) with
    G = Q^-1, on Lambda_+ in t-major order.  The dressing enters the PAIRING as
    Block 104's Gamma0 does, and it is what makes K Hermitian."""
    return pairing_from_resolvent(sp.expand(action.inv() * reflection))


def undressed_gram(action: sp.Matrix) -> sp.Matrix:
    """THE UNDRESSED NEIGHBOUR conj(G(b, theta a)), Block 107's own formula,
    built ONLY to be measured failing Hermiticity in the same run."""
    inverse = action.inv()
    return sp.expand(sp.Matrix(SPAN_SIZE, SPAN_SIZE, lambda row, column:
                               sp.conjugate(inverse[
                                   site_index(*LAMBDA_PLUS[column]),
                                   site_index((-1 - LAMBDA_PLUS[row][0])
                                              % TIME_EXTENT,
                                              LAMBDA_PLUS[row][1])])))


def geometry_gram(hodge: sp.Matrix, reflection: sp.Matrix) -> sp.Matrix:
    """THE PURE-GEOMETRY LIMIT: the same dressed pairing built from H_g^-1
    alone, with NO completion and therefore no matter and no mass at all."""
    return pairing_from_resolvent(sp.expand(hodge.inv() * reflection))


def support_components(matrix: sp.Matrix) -> tuple:
    """The connected components of the operator's SUPPORT GRAPH, as sorted
    sizes.  Two components of sixteen is the diagnosis; one of thirty-two is a
    seam that actually couples."""
    parent = list(range(COVER_SIZE))

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if matrix[row, column] != 0:
                left, right = find(row), find(column)
                if left != right:
                    parent[left] = right
    sizes: dict = {}
    for node in range(COVER_SIZE):
        sizes[find(node)] = sizes.get(find(node), 0) + 1
    return tuple(sorted(sizes.values()))


def cross_half_entries(matrix: sp.Matrix) -> int:
    """The entries joining the positive half to the negative half.  ZERO is the
    disconnection; 48 is the E02 seam actually gluing."""
    return sum(1 for row in range(COVER_SIZE) for column in range(COVER_SIZE)
               if matrix[row, column] != 0
               and (row // SPACE_EXTENT in POSITIVE_TIMES)
               != (column // SPACE_EXTENT in POSITIVE_TIMES))


def symmetric_pair(row: int, column: int) -> sp.Matrix:
    """F_ij = E_ij + E_ji, the adversarial check's own notation."""
    matrix = sp.zeros(4, 4)
    matrix[row, column] += 1
    matrix[column, row] += 1
    return matrix


def seam_family(parameter: object) -> tuple:
    """THE SIX TESTED SEAM DIRECTIONS, at s = parameter.  All six are DRESSED
    self-dual, which gate F measures rather than assumes.

    THE FOUR OFF-DIAGONAL SELF-DUAL DIRECTIONS are F02, F13, (F12 - F03) and
    (F23 - F01); the first four members below are single directions and the last
    two are the ADVERSARIAL CHECK'S TWO EXPLICIT GENERIC POINTS, which replace
    the solve's original 'generic mixed seam' -- that one was NOT REPRODUCIBLE
    and is not used anywhere in this runner.  Bgen1 and Bgen2 are two POINTS in
    the modulus and are never a universal 'generic' assertion."""
    f02 = symmetric_pair(0, 2)
    f13 = symmetric_pair(1, 3)
    b5_direction = symmetric_pair(1, 2) - symmetric_pair(0, 3)
    b8_direction = symmetric_pair(2, 3) - symmetric_pair(0, 1)
    return (
        ("E02", sp.eye(4) + parameter * f02),
        ("E13", sp.eye(4) + parameter * f13),
        ("b5_type_mixed_sign", sp.eye(4) + parameter * b5_direction),
        # THE COUPLING-FREE DIRECTION: it joins slot 0 to slot 1 and slot 2 to
        # slot 3, both of which sit at the SAME time inside a straddling cell.
        ("b8_type", sp.eye(4) + parameter * b8_direction),
        ("Bgen1", sp.eye(4) + parameter * (
            f02 + f13 + b5_direction + b8_direction)),
        ("Bgen2", sp.eye(4) + parameter * (
            f02 + 2 * f13 + 3 * b5_direction + 4 * b8_direction)),
    )


def self_dual_dimension(dressing: sp.Matrix) -> tuple:
    """(dimension, off-diagonal directions) of the DRESSED self-dual symmetric
    space {B = B^T : B = dressing B dressing^T}, solved exactly."""
    unknowns: dict = {}
    block = sp.zeros(4, 4)
    for row in range(4):
        for column in range(row, 4):
            symbol = sp.Symbol(f"b_{row}{column}")
            unknowns[(row, column)] = symbol
            block[row, column] = symbol
            block[column, row] = symbol
    residual = sp.expand(dressing * block * dressing.T - block)
    order = list(unknowns.values())
    solution = list(sp.linsolve(
        [residual[row, column] for row in range(4) for column in range(4)],
        order))[0]
    free = set().union(*[entry.free_symbols for entry in solution])
    off_diagonal = set()
    for (row, column), symbol in unknowns.items():
        if row != column:
            off_diagonal |= solution[order.index(symbol)].free_symbols
    return len(free), len(off_diagonal)


def note_text() -> tuple:
    """(text, at_final_path).  THE FINAL PATH IS THE ONLY PATH READ: there is no
    draft fallback anywhere in this runner, so before landing the text is empty
    and gate H fails on note-at-final-path alone."""
    try:
        return NOTE_PATH.read_text(encoding="utf-8"), True
    except OSError:
        return "", False


def landed_text(path: str) -> str:
    """A LANDED PRIMARY BODY, read at its own path in the worktree.  Gate C
    reads every citation through this and through nothing else -- the Block 182
    process rule, that a citation is checked against the primary body and never
    against a summary."""
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except OSError:
        return ""


# ---------------------------------------------------------------------------
# THE N5 FENCE.  Single-line literal with \n separators; it appears
# BYTE-IDENTICALLY in the note and gate H checks it as a raw substring.
# ---------------------------------------------------------------------------
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- the SECTION FRAME as the Blocks 181-185 lane landed it (the LANDED Block 128 8x4 cover of dimension 32 with idx(t,x) = (t%8)*4 + x%4, the LANDED Block 105 overlap field, the LANDED chart differential d_00 = chart_differential_cover((0,0)), and the Block 184 completion convention Q(H,d) = m*H + i*(H d + d^H H)), THE DRESSED REFLECTION Px = P0 * xpar with P0 the site permutation theta(t) = (-1-t)%8 and xpar = diag((-1)^x), THE ANCHOR REFLECTION thA(t) = (-2-t)%8 with the UNSIGNED offset permutation P4 and the sign Xi = diag(1,-1,1,-1), THE GLUED HODGE H_g -- plain field blocks at t in {0,1,2}, the SHEAR-FLIPPED P4-image blocks P4 H(-q,v) P4^T at the reflected field for t in {4,5,6}, a SELF-DUAL SEAM BLOCK B at the two straddling anchors t in {3,7}, and the x-minimal average (H + Ux^T H Ux)/2 -- THE RESTRICTED SET A of d_00 entries with both times in {0,1,2,3} with D = A - Px A Px, and THE DRESSED PAIRING K[a,b] = conj((G Px)[idx(b), idx(a)]) on Lambda_+ = the sixteen sites t in {0,1,2,3}, ARE IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the LANDED Block 128 runner and the Block 105 module it re-exports and from NOTHING in any scratchpad. THIS IS NOT A NO-GO. THE WALL IS PER-PAIRING AND PER-FRAME: NO NO-GO IS CLAIMED, NO OS POSITIVITY ON THIS FRAME IS CLAIMED, NO MECHANISM FOR THE BALANCED INERTIA IS KNOWN, NO PAIRING-GENERALITY IS CLAIMED -- SEVEN VARIANT CLASSES ARE NAMED UNTESTED IN THE LIMITS -- and BLOCK 185'S LANDED POSITIVITY ON THE BLOCK 107 CARRIER IS UNTOUCHED BY EVERYTHING HERE. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE PORT IS NOT A TRANSFER, AND ITS THREE STRUCTURAL THEOREMS COME FIRST. F1, THE CHART DIFFERENTIAL IS CELL-LOCAL: all 32 entries of d_00 lie inside the 2x2 even-anchored cells, EXACTLY 0 of them cross the far seam {3,4} and EXACTLY 0 cross the near seam {7,0}, so an antiperiodic edge negation on this carrier is VACUOUS. F2, THE FLAT SECTION-FRAME THEORY IS DISCONNECTED: the flat overlap Hodge is EXACTLY the 32x32 identity, so the flat completion is block-diagonal over sixteen disjoint cells and THE FLAT REFLECTED GRAM IS IDENTICALLY ZERO -- rank 0 measured on the two-slice span, on the {0,3} span and on the full-half span, dressed and undressed alike, so NO FLAT CALIBRATION EXISTS ON THIS FAMILY and the Block 107 transfer strategy fails STRUCTURALLY rather than numerically. F3, THE INTER-CELL CENSUS, CORRECTED BY THE ADVERSARIAL CHECK AND STATED IN ITS CORRECTED FORM: the curved no-glue completion carries EXACTLY 144 ORDERED inter-cell entries on EXACTLY 72 unordered edges; the curved Hodge itself carries EXACTLY 48 ORDERED entries on 24 of those edges; and EXACTLY 96 ORDERED entries are CREATED by the transport term H d + d^H H beyond the Hodge's own support. THE CAUSAL STATEMENT SURVIVES AND ITS WORDING DOES NOT: the FLAT Hodge is the identity and carries ZERO inter-cell edges, so ALL 72 curved edges are H-INDUCED, but \"H-BORNE\" MUST NOT BE READ AS \"IN H's SUPPORT\" -- 96 of the 144 ordered entries are NOT in the Hodge's support. The earlier \"96 inter-cell entries\" was the ORDERED SUPPORT INCREMENT mislabelled as the total, and it is corrected here.\nper_mode: THE SELECTION RULE DIAGNOSED, AND THE SEAM IS A MODULUS. With FLAT seam blocks the glued action's support graph has EXACTLY TWO CONNECTED COMPONENTS AND THEY ARE THE TWO HALVES, sixteen sites each, with EXACTLY 0 cross-half entries: matter is cell-local by F1 and a flat seam anchor contributes only diagonally through its straddling embedding, so theta swaps the two components, every (b, theta a) pair straddles, AND THE DRESSED GRAM VANISHES IDENTICALLY. THE FIX IS DERIVED RATHER THAN GUESSED: the straddling anchors are the fixed points of thA, so their blocks must be SELF-DUAL, and the DRESSED self-dual symmetric space B = (P4 Xi) B (P4 Xi)^T is EXACTLY 6-DIMENSIONAL with EXACTLY 4 off-diagonal directions -- THE SEAM IS A MODULUS. AND THE SHEAR FAMILY CANNOT SUPPLY IT, AT A SCOPE THE ADVERSARIAL CHECK CORRECTED: the P4 self-duality residual of H(q,v) is R00 = q^2 v/(q^2-1), R11 = (-q^2-v^2+1)/(v(q^2-1)), R12 = R21 = qv/(q^2-1), R03 = R30 = -qv/(q^2-1) with R22 = -R00 and R33 = -R11, and its EXACT solution set at nonzero volume is BOTH (q,v) = (0,1) AND (q,v) = (0,-1). THE FLAT BLOCK IS THE UNIQUE SELF-DUAL MEMBER OF THE SHEAR FAMILY ONLY UNDER THE CONVENTIONAL POSITIVE-VOLUME RESTRICTION v > 0, WHICH IS STATED WHEREVER THE LEMMA APPEARS -- and under it, Block 107's forced-flat seam rows are RE-DERIVED FROM DUALITY. All EIGHT values of the landed Block 105 overlap field are PYTHAGOREAN, q^2 + v^2 = 1 exactly, so every field block kills the R11 factor and is HALF self-dual, and none is self-dual.\nper_block: THE CONSTRUCTION, AND EVERY STRUCTURAL PROPERTY IS MEASURED RATHER THAN ASSUMED. With A the 16 d_00 entries whose both times lie in {0,1,2,3} and D = A - Px A Px at EXACTLY 32 entries: D IS Px-ODD at zero residual, D EQUALS d_00 ENTRYWISE throughout the positive half so THE PHYSICAL DYNAMICS OF THE POSITIVE HALF IS UNTOUCHED, and D IS NOT d_00 GLOBALLY. The glued Hodge H_g is POSITIVE DEFINITE by 32 exact leading minors and Px-EVEN at zero residual. THE GLUED ACTION IS REAL -- every entry of Q_g is real, so the Block 185 C8 reality condition is SATISFIED by the port construction and the solve's earlier \"not real\" reading was a SYMBOLIC-ASSUMPTIONS ARTIFACT, caught inside the solve. Px Q_g Px = Q_g^T holds at zero residual. With a coupling-carrying seam THE HALVES CONNECT: one connected component and EXACTLY 48 cross-half entries at the E02 seam. AND THE DRESSING IS WHAT MAKES THE PAIRING HERMITIAN: K[a,b] = conj((G Px)[idx(b), idx(a)]) has Hermiticity defect EXACTLY ZERO while the UNDRESSED formula conj(G(b, theta a)) has EXACTLY 80 nonzero defect entries at the same point.\nlattice_wide: THE WALL, W1: THE INERTIA IS BALANCED IN EVERY COUPLING-CARRYING SEAM DIRECTION TESTED. At m = 9/20 and s = 1/5, all six seam blocks are exactly self-dual and all six give an exactly Hermitian dressed Gram, and the inertias are: the E02 seam I + s(E02+E20), EXACTLY (+6,-6,0x4); the E13 seam I + s(E13+E31), EXACTLY (+6,-6,0x4); the b5-type mixed-sign seam I + s(F12-F03), EXACTLY (+3,-3,0x10) at rank 6; TWO EXPLICIT GENERIC POINTS supplied by the adversarial check, Bgen1 = I + [F02 + F13 + (F12-F03) + (F23-F01)]/5 and Bgen2 = I + [F02 + 2 F13 + 3(F12-F03) + 4(F23-F01)]/5 with Fij = Eij + Eji, BOTH EXACTLY (+6,-6,0x4) at rank 12 -- TWO GENERIC POINTS AND NOT A UNIVERSAL \"GENERIC\" ASSERTION; and the b8-type seam I + s(F23-F01), THE ZERO GRAM, all sixteen eigenvalues zero. AND THE ZERO IS NOT A MYSTERY BUT THE DIAGNOSIS RECURRING: the b8-type direction couples slot 0 to slot 1 and slot 2 to slot 3, both of which lie at the SAME time inside a straddling cell, so it carries NO seam coupling at all -- it leaves two components of sixteen and 0 cross-half entries, exactly as a flat seam does. EXACTLY ONE OF THE FOUR OFF-DIAGONAL SELF-DUAL DIRECTIONS IS COUPLING-FREE, AND EVERY COUPLING-CARRYING DIRECTION TESTED LANDS ON A BALANCED INERTIA.\nper_scope: THE WALL, W2 AND W3, THE MECHANISM EXCLUDED AS A THEOREM, AND EVERY ESCAPE ROUTE PROBED NEGATIVE. W2, THE MASS SWEEP: at the E02 seam the inertia is EXACTLY (+6,-6,0x4) at EVERY ONE of m = 1/3, 9/20, 1, 2 and 10, and the PURE-GEOMETRY LIMIT -- K built from H_g^-1 alone with no completion at all -- is EXACTLY (+4,-4,0x8), BALANCED EVEN IN THE LIMIT, so the balance is not a mass effect and not a matter effect. W3, THE MECHANISM-EXCLUSION THEOREM, STRENGTHENED BY THE ADVERSARIAL CHECK: the characteristic polynomial of the dressed Gram has EXACTLY 6 NONZERO ODD-POWER COEFFICIENTS, at powers 5, 7, 9, 11, 13 and 15 with signs (-,+,+,-,+,-), so THE SPECTRUM IS NOT PLUS-MINUS SYMMETRIC and no invertible S with S K S^-1 = -K exists; and EXACTLY, gcd(charpoly(x), charpoly(-x)) = x^4, so NO nonzero eigenvalue is paired with its negative, THE ANTI-COMMUTANT {S : S K + K S = 0} HAS DIMENSION EXACTLY 16 = 4^2, EVERY MEMBER IS KERNEL-SUPPORTED AND NONE IS INVERTIBLE. The four natural diagonal candidates NEITHER COMMUTE NOR ANTICOMMUTE, at 80/80, 80/80, 96/64 and 96/64. AND THE THREE ESCAPE ROUTES ARE ALL NEGATIVE: the TRACE IDENTITY IS DEAD, tr K being strictly positive at all five masses; the ANTILINEAR ROUTE COLLAPSES, because K IS REAL so S conj(K) S^-1 = -K is the ALREADY-EXCLUDED linear similarity, with the direct residuals nonzero at rank 16 and 80/80/64/64 entries for the diagonal candidates and 200-208 entries for the half-reflection composites; and THE GAMMA0 TWO-SIDED DRESSING IS NOT AN INDEPENDENT CANDIDATE AT ALL, because K2 = xpar K xpar IS A CONGRUENCE of K, so Sylvester FORCES its measured inertia (+6,-6,0x4) -- the variant's design was the supervisor's error and the checker's identification of it is what closed the route. NO TESTED VARIANT IS POSITIVE OR POSITIVE SEMIDEFINITE. THE BALANCED INERTIA HAS NO LINEAR ANTI-SYMMETRY MECHANISM AND ITS CAUSE IS OPEN. AND THE SCOPE IS SAID PLAINLY: THIS IS NOT A NO-GO. The wall is PER-PAIRING and PER-FRAME, ONE fixture, ONE pairing family, ONE seam modulus at ONE value of s, with SEVEN VARIANT CLASSES NAMED UNTESTED IN THE LIMITS; and BLOCK 185'S LANDED POSITIVE GRAM ON THE BLOCK 107 CARRIER IS UNTOUCHED -- this block characterizes why the section frame's FIRST pairing family does not reproduce it, which is COMPLEMENTARY TO Block 185 AND NOT CONTRADICTORY.\nRESULT: THE SECTION-FRAME PORT YIELDS THREE STRUCTURAL THEOREMS, A DERIVED SEAM MODULUS, AND A BALANCED-INERTIA WALL WHOSE LINEAR-SYMMETRY MECHANISM IS EXCLUDED, WHOSE THREE ESCAPE ROUTES ARE PROBED NEGATIVE, AND WHOSE CAUSE IS OPEN. d_00 is cell-local at 32 entries with 0 far-seam and 0 near-seam hops; the flat overlap Hodge is exactly the identity and the flat reflected Gram has rank 0 on all three spans; the curved no-glue completion has 144 ordered inter-cell entries on 72 edges, the curved Hodge 48 ordered on 24 of them, and 96 ordered are created by the transport term, with the flat Hodge carrying zero inter-cell edges; the flat-seam glued action splits into exactly two 16-site components that theta swaps, with a dressed Gram that is identically zero; the dressed self-dual seam space is 6-dimensional with 4 off-diagonal directions and the flat block is the unique self-dual member of the shear family AT POSITIVE VOLUME, the exact solution set being (0,1) and (0,-1), against a Pythagorean landed field; D = A - Px A Px carries 32 entries, is Px-odd at zero residual and equals d_00 on the positive half; H_g is positive definite and Px-even; Q_g is REAL and Px-covariant at zero residual; the halves connect at 48 cross-half entries; the dressed Gram is exactly Hermitian while the undressed one is not, at 80 entries; the inertia is (+6,-6,0x4) at the E02, E13 and both generic seams, (+3,-3,0x10) at the b5-type seam and IDENTICALLY ZERO at the coupling-free b8-type seam; it is (+6,-6,0x4) at every one of five masses and (+4,-4,0x8) in the pure-geometry limit; the charpoly's 6 nonzero odd coefficients and gcd(charpoly(x), charpoly(-x)) = x^4 give an anti-commutant of dimension exactly 16, entirely kernel-supported and containing no invertible member; and the trace, antilinear and Gamma0 escape routes are all negative. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-185 STAND EXACTLY AS LANDED; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: THE WALL IS A MEASURED OBSTRUCTION AND NOT A NO-GO -- one fixture, one pairing family, one seam modulus, one value of s, per-frame and per-pairing, with SEVEN VARIANT CLASSES NAMED UNTESTED; THE MECHANISM IS EXCLUDED AND NOT EXPLAINED, so the CAUSE OF THE BALANCE IS OPEN; NO OS POSITIVITY IS ESTABLISHED ON THIS FRAME AT ANY SCOPE; and NOTHING HERE TOUCHES BLOCK 185'S LANDED POSITIVITY ON THE BLOCK 107 CARRIER, which is a DIFFERENT CARRIER. ONE CORRECTION IS LANDED BY THIS BLOCK AND IT IS THIS BLOCK'S OWN: THE INTER-CELL CENSUS, WHOSE \"96 H-BORNE ENTRIES\" WAS THE ORDERED SUPPORT INCREMENT MISLABELLED AS THE TOTAL -- the corrected census is 144 ordered on 72 edges with 48 ordered in the Hodge's own support, the causal statement survives with corrected wording, and it is recorded as the FOURTEENTH SUPERVISOR CORRECTION. TWO FURTHER CHECKER CORRECTIONS ARE FOLDED: the self-duality lemma is TRUE ONLY AT POSITIVE VOLUME, the exact solution set being (0,1) AND (0,-1); and the original \"generic mixed seam\" WAS NOT REPRODUCIBLE and is REPLACED by two explicit generic points. THREE IN-SOLVE CATCHES ARE RECORDED AS PROCESS AND NOT AS CORRECTIONS, because none of them ever left the solve: the vacuous antiperiodic edge negation, killed by F1 in the same measurement that found it; the first negative-half image built WITHOUT the within-block xpar flip, which failed covariance at 144 entries and whose fix is exact; and the reading that the glued action was NOT REAL, which was a SYMBOLIC-ASSUMPTIONS ARTIFACT and is now gated at its exact reality. AND ONE VARIANT-DESIGN ERROR IS DISCLOSED: the Gamma0 two-sided dressing was proposed as an independent escape candidate and IS A CONGRUENCE, so Sylvester forced its inertia before it was ever measured -- the checker identified it and it is not an escape route. THE RULE REAFFIRMED IS THE CONTROL-FIRST RULE, AND IT WAS APPLIED BEFORE THE LABEL THIS TIME: the mass sweep was run BEFORE any structural label hardened, so \"balanced inertia\" was a measured invariance before it was ever a name. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE SECTION-FRAME PORT and THE SELECTION-RULE DIAGNOSIS COMPLETE anchors, with the wall results supplied by the supervisor and corrected by the b186 adversarial check.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


# ---------------------------------------------------------------------------
# the claims: every expected value the gates compare against, in ONE place
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims: dict = {
        # A -- the authority pins.
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        # B -- the banner's declared status flags.
        "objects_registered": False,
        "no_go_claimed": NO_GO_CLAIMED,
        "os_positivity_on_this_frame_claimed":
            OS_POSITIVITY_ON_THIS_FRAME_CLAIMED,
        "mechanism_known": MECHANISM_KNOWN,
        "pairing_generality_claimed": PAIRING_GENERALITY_CLAIMED,
        "b185_positivity_touched": B185_POSITIVITY_TOUCHED,
        # C -- the citation pins and the port's structural theorems.
        "citation_pins": True,
        "d00_nonzeros": D00_NONZEROS,
        "d00_all_intra_cell": True,
        "far_seam_hops": FAR_SEAM_HOPS,
        "near_seam_hops": NEAR_SEAM_HOPS,
        "flat_hodge_is_identity": True,
        "flat_gram_ranks": (FLAT_GRAM_RANK,) * 6,
        "curved_inter_cell_ordered": CURVED_INTER_CELL_ORDERED,
        "curved_inter_cell_edges": CURVED_INTER_CELL_EDGES,
        "hodge_inter_cell_ordered": HODGE_INTER_CELL_ORDERED,
        "hodge_inter_cell_edges": HODGE_INTER_CELL_EDGES,
        "transport_created_ordered": TRANSPORT_CREATED_ORDERED,
        "flat_inter_cell_ordered": FLAT_INTER_CELL_ORDERED,
        "differential_inter_cell": DIFFERENTIAL_INTER_CELL,
        # D -- the diagnosis and the seam modulus.
        "flat_seam_components": FLAT_SEAM_COMPONENTS,
        "flat_seam_cross_half": FLAT_SEAM_CROSS_HALF,
        "theta_swaps_halves": True,
        "flat_seam_gram_nonzeros": 0,
        "self_dual_dimension": SELF_DUAL_DIMENSION,
        "self_dual_off_diagonal": SELF_DUAL_OFF_DIAGONAL,
        "self_dual_shear_points": SELF_DUAL_SHEAR_POINTS,
        "self_duality_residual_entries": SELF_DUALITY_RESIDUAL_ENTRIES,
        "self_duality_table_exact": True,
        "field_all_pythagorean": True,
        "field_value_count": FIELD_VALUE_COUNT,
        # E -- the construction.
        "restricted_nonzeros": RESTRICTED_NONZEROS,
        "glue_nonzeros": GLUE_NONZEROS,
        "glue_p_odd_residual": ZERO_RESIDUAL,
        "glue_matches_positive_half": True,
        "hodge_positive_definite": True,
        "hodge_p_even_residual": ZERO_RESIDUAL,
        "action_is_real": True,
        "covariance_residual": ZERO_RESIDUAL,
        "cross_half_entries": CROSS_HALF_ENTRIES,
        "dressed_defect": ZERO_RESIDUAL,
        "undressed_defect": UNDRESSED_DEFECT_ENTRIES,
        "dressed_nonzeros": DRESSED_NONZEROS,
        "dressed_rank": DRESSED_RANK,
        # F -- THE WALL, W1.
        "seam_inertias": (BALANCED_INERTIA, BALANCED_INERTIA, B5_TYPE_INERTIA,
                          ZERO_GRAM_INERTIA, BALANCED_INERTIA,
                          BALANCED_INERTIA),
        "seams_all_self_dual": True,
        "seams_all_hermitian": True,
        "two_methods_agree": True,
        "coupling_free_components": COUPLING_FREE_COMPONENTS,
        "coupling_free_cross_half": 0,
        "e02_pivot_signature": E02_PIVOT_SIGNATURE,
        # G -- THE WALL, W2 and W3, and the escape routes.
        "mass_sweep_inertias": (BALANCED_INERTIA,) * len(MASS_SWEEP),
        "geometry_limit_inertia": GEOMETRY_LIMIT_INERTIA,
        "geometry_limit_defect": ZERO_RESIDUAL,
        "odd_coefficient_count": ODD_COEFFICIENT_COUNT,
        "odd_coefficient_powers": ODD_COEFFICIENT_POWERS,
        "odd_coefficient_signs": ODD_COEFFICIENT_SIGNS,
        "spectral_gcd_is_lambda_fourth": True,
        "spectral_gcd_degree": SPECTRAL_GCD_DEGREE,
        "kernel_dimension": KERNEL_DIMENSION,
        "anticommutant_dimension": ANTICOMMUTANT_DIMENSION,
        "candidates_neither_commute_nor_anticommute": True,
        "traces_all_positive": True,
        "gram_is_real": True,
        "antilinear_residual_entries": ANTILINEAR_RESIDUAL_ENTRIES,
        "antilinear_residuals_full_rank": True,
        "gamma0_is_congruence": True,
        "gamma0_inertia": GAMMA0_INERTIA,
        "no_tested_variant_is_definite": True,
        "escape_routes_well_formed": True,
        "escape_routes_all_negative": True,
        # H -- the note and the fence.
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_objects_registered":
        # THE BANNER DENIED: the imposed objects asserted REGISTERED, which zero
        # registered and zero adopted objects forbid.
        claims["objects_registered"] = True
    elif mutation == "claim_no_go":
        # THE WALL PROMOTED TO A NO-GO.  THIS IS THE BLOCK'S SINGLE BIGGEST
        # OVERREACH RISK.  An obstruction that survives six seam directions,
        # five masses, the pure-geometry limit AND three escape probes READS as
        # a proof that the section frame cannot carry OS positivity.  IT IS NOT
        # ONE: exactly ONE pairing family is tested, at ONE value of s, on ONE
        # fixture, and SEVEN variant classes are named untested in the note's
        # LIMITS.  Asserting the no-go fails HERE and nowhere else.
        claims["no_go_claimed"] = True
    elif mutation == "claim_mechanism_known":
        # THE EXCLUSION MISREAD AS AN EXPLANATION.  W3 excludes every LINEAR
        # anti-symmetry mechanism and the escape probes close three named
        # routes; NONE of that supplies a cause, and THE CAUSE OF THE BALANCE IS
        # OPEN.  Asserting that the mechanism is known fails HERE.
        claims["mechanism_known"] = True
    elif mutation == "break_cell_locality":
        # F1 DENIED: seam hops asserted for d_00, which the exact count of zero
        # forbids -- and with them the whole diagnosis, since it is precisely
        # the absence of matter seam hops that disconnects the halves.
        claims["far_seam_hops"] = 4
    elif mutation == "break_flat_gram_zero":
        # F2 DENIED: a nonzero flat reflected Gram asserted, which rank 0 on all
        # three spans forbids.  Without this the block reads as though a flat
        # calibration could have been taken, and no flat calibration exists.
        claims["flat_gram_ranks"] = (8, 8, 8, 8, 8, 8)
    elif mutation == "break_intercell_census":
        # THE SUPERSEDED CENSUS RE-ASSERTED.  THIS MUTATION GUARDS THIS BLOCK'S
        # OWN LANDED CORRECTION: the solve originally reported "96 inter-cell
        # entries", which was the ORDERED SUPPORT INCREMENT mislabelled as the
        # TOTAL.  The total is 144 ordered on 72 edges.  Asserting 96 as the
        # total fails HERE and nowhere else.
        claims["curved_inter_cell_ordered"] = TRANSPORT_CREATED_ORDERED
    elif mutation == "break_two_components":
        # THE DIAGNOSIS DENIED: the flat-seam glued action asserted connected,
        # which two 16-site components forbid.  This is the measurement that
        # explains the zero Gram, and without it the zero looks like an accident.
        claims["flat_seam_components"] = (32,)
    elif mutation == "break_selfdual_dim":
        # THE MODULUS DENIED: a rigid seam asserted, which a 6-dimensional
        # solution space with 4 off-diagonal directions forbids.  If the seam
        # were rigid the wall would be a statement about one block rather than
        # about a family.
        claims["self_dual_dimension"] = 1
    elif mutation == "break_construction_real":
        # THE IN-SOLVE CATCH RE-ASSERTED: the glued action claimed NOT real,
        # which is exactly the symbolic-assumptions artifact the solve caught.
        # Q_g is real entrywise, so the Block 185 C8 reality condition is
        # SATISFIED here and the wall cannot be blamed on a complex action --
        # and the SAME reality is what collapses the antilinear escape route.
        claims["action_is_real"] = False
    elif mutation == "break_wall_inertia":
        # THE WALL DENIED AT ITS HEADLINE: a definite Gram asserted at the E02
        # seam, which the exact (+6,-6,0x4) forbids -- by BOTH methods.  If this
        # moved, there would be no wall to characterize and no block.
        claims["seam_inertias"] = ((16, 0, 0), BALANCED_INERTIA,
                                   B5_TYPE_INERTIA, ZERO_GRAM_INERTIA,
                                   BALANCED_INERTIA, BALANCED_INERTIA)
    elif mutation == "break_odd_coefficients":
        # THE EXCLUSION THEOREM DELETED: a plus-minus symmetric spectrum
        # asserted, which six nonzero odd coefficients forbid.  With an even
        # charpoly an anti-commuting invertible S would be permitted and the
        # balance would have a candidate mechanism; it does not.
        claims["odd_coefficient_count"] = 0
    elif mutation == "break_mass_sweep":
        # THE ROBUSTNESS DENIED: the inertia asserted to move with the mass,
        # which five identical triples forbid.  The m-invariance is what makes
        # the balance structural rather than a fixture coincidence, and it was
        # MEASURED BEFORE the label was applied.
        claims["mass_sweep_inertias"] = ((6, 6, 4), (6, 6, 4), (6, 6, 4),
                                         (6, 6, 4), (5, 5, 6))
    elif mutation == "break_gcd_exclusion":
        # THE STRENGTHENED EXCLUSION WEAKENED: a spectral gcd of degree five
        # asserted, which the exact gcd = x^4 forbids.  The gcd is what upgrades
        # "no INVERTIBLE anti-commutant" to "the anti-commutant is EXACTLY the
        # 16-dimensional space of kernel-to-kernel maps", so losing it loses the
        # sharp half of the theorem.
        claims["spectral_gcd_degree"] = 5
        claims["spectral_gcd_is_lambda_fourth"] = False
    elif mutation == "break_escape_routes":
        # AN ESCAPE ROUTE ASSERTED OPEN: the Gamma0 two-sided dressing claimed
        # to change the inertia, which a CONGRUENCE cannot do -- Sylvester
        # forbids it, and the measurement confirms it.  This is the mutation
        # that stops a reader from thinking a route was left untried.
        claims["gamma0_inertia"] = (12, 0, 4)
        claims["escape_routes_all_negative"] = False
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim")
    return claims


# ---------------------------------------------------------------------------
# the measurement pass: every gate reads it, no gate feeds it
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    note_at_final_path: bool
    scope: dict
    banners: dict
    citation_pins: dict
    d00_nonzeros: int
    d00_all_intra_cell: bool
    far_seam_hops: int
    near_seam_hops: int
    flat_hodge_is_identity: bool
    flat_gram_ranks: tuple
    curved_inter_cell_ordered: int
    curved_inter_cell_edges: int
    hodge_inter_cell_ordered: int
    hodge_inter_cell_edges: int
    transport_created_ordered: int
    flat_inter_cell_ordered: int
    differential_inter_cell: int
    flat_seam_components: tuple
    flat_seam_cross_half: int
    theta_swaps_halves: bool
    flat_seam_gram_nonzeros: int
    self_dual_dimension: int
    self_dual_off_diagonal: int
    self_dual_shear_points: tuple
    self_duality_residual_entries: int
    self_duality_table_exact: bool
    field_all_pythagorean: bool
    field_value_count: int
    restricted_nonzeros: int
    glue_nonzeros: int
    glue_p_odd_residual: int
    glue_matches_positive_half: bool
    glue_equals_differential: bool
    hodge_positive_definite: bool
    hodge_p_even_residual: int
    action_is_real: bool
    covariance_residual: int
    cross_half_entries: int
    dressed_defect: int
    undressed_defect: int
    dressed_nonzeros: int
    dressed_rank: int
    seam_names: tuple
    seam_inertias: tuple
    seam_congruence_inertias: tuple
    seam_self_dual: tuple
    seam_defects: tuple
    seam_ranks: tuple
    two_methods_agree: bool
    coupling_free_components: tuple
    coupling_free_cross_half: int
    e02_pivot_signature: str
    mass_sweep_inertias: tuple
    geometry_limit_inertia: tuple
    geometry_limit_defect: int
    odd_coefficient_count: int
    odd_coefficient_powers: tuple
    odd_coefficient_signs: tuple
    even_coefficient_powers: tuple
    spectral_gcd_is_lambda_fourth: bool
    spectral_gcd_degree: int
    kernel_dimension: int
    anticommutant_dimension: int
    candidate_commutators: tuple
    candidate_anticommutators: tuple
    candidates_neither_commute_nor_anticommute: bool
    traces_all_positive: bool
    reference_trace_positive: bool
    gram_is_real: bool
    antilinear_residual_entries: tuple
    antilinear_residual_ranks: tuple
    antilinear_residuals_full_rank: bool
    gamma0_is_congruence: bool
    gamma0_defect: int
    gamma0_rank: int
    gamma0_inertia: tuple
    no_tested_variant_is_definite: bool
    escape_routes_well_formed: bool
    escape_routes_all_negative: bool
    exactness_holds: bool


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    # --- the section frame, from the LANDED carrier -------------------------
    differential = b128.chart_differential_cover((0, 0))
    field = b128.block105.overlap_field()
    reflection = sp.expand(site_reflection() * space_parity())
    spatial_shift = cover_shift(0, 1)
    cell_sets = cells()

    def intra_cell(row: int, column: int) -> bool:
        return any(row in cell and column in cell for cell in cell_sets)

    # --- C, F1: THE CHART DIFFERENTIAL IS CELL-LOCAL ------------------------
    positions = tuple((row, column)
                      for row in range(COVER_SIZE)
                      for column in range(COVER_SIZE)
                      if differential[row, column] != 0)
    d00_all_intra_cell = all(intra_cell(*position) for position in positions)
    far_seam_hops = sum(
        1 for row, column in positions
        if frozenset({row // SPACE_EXTENT, column // SPACE_EXTENT}) == FAR_SEAM)
    near_seam_hops = sum(
        1 for row, column in positions
        if frozenset({row // SPACE_EXTENT,
                      column // SPACE_EXTENT}) == NEAR_SEAM)

    # --- C, F2: THE FLAT THEORY IS DISCONNECTED -----------------------------
    flat_hodge = hodge_from_blocks(
        lambda time, space: shear_block(sp.Integer(0), sp.Integer(1)))
    flat_hodge_is_identity = residual_count(
        flat_hodge - sp.eye(COVER_SIZE)) == 0
    flat_action = completion(flat_hodge, differential)
    flat_inverse = flat_action.inv()
    flat_resolvent = sp.expand(flat_inverse * reflection)
    flat_gram_ranks = []
    for span in (tuple((t, x) for t in (0, 1) for x in range(SPACE_EXTENT)),
                 tuple((t, x) for t in (0, 3) for x in range(SPACE_EXTENT)),
                 LAMBDA_PLUS):
        size = len(span)
        dressed = sp.Matrix(size, size, lambda row, column: sp.conjugate(
            flat_resolvent[site_index(*span[column]), site_index(*span[row])]))
        undressed = sp.Matrix(size, size, lambda row, column: sp.conjugate(
            flat_inverse[site_index(*span[column]),
                         site_index((-1 - span[row][0]) % TIME_EXTENT,
                                    span[row][1])]))
        flat_gram_ranks.append(sp.expand(dressed).rank())
        flat_gram_ranks.append(sp.expand(undressed).rank())

    # --- C, F3: THE INTER-CELL CENSUS, IN ITS CORRECTED FORM ---------------
    # THE ADVERSARIAL CHECK REFUTED THE ORIGINAL STATEMENT AND THIS IS THE
    # REBUILT ONE.  Everything is counted on the CURVED NO-GLUE completion, in
    # ORDERED entries and in UNORDERED edges, and the Hodge's own share is
    # separated from what the transport term CREATES.
    curved_hodge = hodge_from_blocks(
        lambda time, space: shear_block(
            *field[(time % (TIME_EXTENT // 2), space)]))
    curved_action = completion(curved_hodge, differential)
    curved_inter_cell = tuple(
        (row, column) for row in range(COVER_SIZE)
        for column in range(COVER_SIZE)
        if not intra_cell(row, column) and curved_action[row, column] != 0)
    hodge_inter_cell = tuple(
        (row, column) for row in range(COVER_SIZE)
        for column in range(COVER_SIZE)
        if not intra_cell(row, column) and curved_hodge[row, column] != 0)
    transport_created = sum(
        1 for row, column in curved_inter_cell
        if curved_hodge[row, column] == 0)
    flat_inter_cell = sum(
        1 for row in range(COVER_SIZE) for column in range(COVER_SIZE)
        if not intra_cell(row, column) and flat_hodge[row, column] != 0)
    differential_inter_cell = sum(
        1 for row, column in positions if not intra_cell(row, column))

    # --- D: THE DIAGNOSIS, at a FLAT seam -----------------------------------
    flat_seam_hodge = glued_hodge(sp.eye(4), field, spatial_shift)
    restricted = restricted_raising(differential)
    glue = sp.expand(restricted - reflection * restricted * reflection)
    flat_seam_action = completion(flat_seam_hodge, glue)
    flat_seam_gram = dressed_gram(flat_seam_action, reflection)
    theta_swaps_halves = (
        {site_index((-1 - t) % TIME_EXTENT, x) for t in POSITIVE_TIMES
         for x in range(SPACE_EXTENT)}
        == {site_index(t, x) for t in range(4, TIME_EXTENT)
            for x in range(SPACE_EXTENT)})

    # --- D: THE SEAM MODULUS, and the POSITIVE-VOLUME scoping --------------
    dressing = sp.expand(OFFSET_PERMUTATION * XI)
    dimension, off_diagonal = self_dual_dimension(dressing)
    symbolic_block = shear_block(SHEAR_SYMBOL, VOLUME_SYMBOL)
    # THE CHECKER'S ORIENTATION: R = H - P4 H P4^T, so the displayed table is
    # theirs entry for entry.
    self_duality_residual = sp.simplify(sp.expand(
        symbolic_block
        - OFFSET_PERMUTATION * symbolic_block * OFFSET_PERMUTATION.T))
    residual_entries = tuple(
        (row, column, sp.simplify(self_duality_residual[row, column]))
        for row in range(4) for column in range(4)
        if sp.simplify(self_duality_residual[row, column]) != 0)
    denominator = SHEAR_SYMBOL ** 2 - 1
    expected_table = {
        (0, 0): SHEAR_SYMBOL ** 2 * VOLUME_SYMBOL / denominator,
        (2, 2): -SHEAR_SYMBOL ** 2 * VOLUME_SYMBOL / denominator,
        (1, 1): (1 - SHEAR_SYMBOL ** 2 - VOLUME_SYMBOL ** 2)
        / (VOLUME_SYMBOL * denominator),
        (3, 3): -(1 - SHEAR_SYMBOL ** 2 - VOLUME_SYMBOL ** 2)
        / (VOLUME_SYMBOL * denominator),
        (1, 2): SHEAR_SYMBOL * VOLUME_SYMBOL / denominator,
        (2, 1): SHEAR_SYMBOL * VOLUME_SYMBOL / denominator,
        (0, 3): -SHEAR_SYMBOL * VOLUME_SYMBOL / denominator,
        (3, 0): -SHEAR_SYMBOL * VOLUME_SYMBOL / denominator,
    }
    self_duality_table_exact = (
        len(residual_entries) == len(expected_table)
        and all(sp.simplify(entry - expected_table[(row, column)]) == 0
                for row, column, entry in residual_entries))
    # THE EXACT SOLUTION SET AT NONZERO VOLUME.  It is BOTH (0,1) AND (0,-1),
    # so "flat is the unique self-dual member of the shear family" is TRUE ONLY
    # UNDER THE CONVENTIONAL POSITIVE-VOLUME RESTRICTION v > 0.
    numerators = [sp.numer(sp.together(entry))
                  for _, _, entry in residual_entries]
    solutions = sp.solve(numerators, [SHEAR_SYMBOL, VOLUME_SYMBOL], dict=True)
    self_dual_shear_points = tuple(sorted(
        ((int(solution[SHEAR_SYMBOL]), int(solution[VOLUME_SYMBOL]))
         for solution in solutions
         if solution.get(VOLUME_SYMBOL, sp.Integer(0)) != 0),
        key=lambda point: -point[1]))
    field_values = tuple(sorted(set(field.values()), key=str))
    field_all_pythagorean = all(
        sp.simplify(shear ** 2 + volume ** 2 - 1) == 0
        for shear, volume in field_values)

    # --- E: THE CONSTRUCTION, at the E02 reference seam ---------------------
    seams = seam_family(SEAM_PARAMETER)
    reference_hodge = glued_hodge(seams[0][1], field, spatial_shift)
    reference_action = completion(reference_hodge, glue)
    reference_gram = dressed_gram(reference_action, reflection)
    reference_undressed = undressed_gram(reference_action)
    glue_matches_positive_half = all(
        glue[row, column] == differential[row, column]
        for row in range(COVER_SIZE) for column in range(COVER_SIZE)
        if row // SPACE_EXTENT in POSITIVE_TIMES
        and column // SPACE_EXTENT in POSITIVE_TIMES)

    # --- F: THE WALL, W1, BY TWO INDEPENDENT EXACT METHODS -----------------
    seam_names = tuple(name for name, _ in seams)
    seam_inertias = []
    seam_congruence_inertias = []
    seam_self_dual = []
    seam_defects = []
    seam_ranks = []
    coupling_free_components: tuple = ()
    coupling_free_cross_half = -1
    e02_pivot_signature = ""
    for name, block in seams:
        seam_self_dual.append(residual_count(
            dressing * block * dressing.T - block) == 0)
        hodge = glued_hodge(block, field, spatial_shift)
        action = completion(hodge, glue)
        gram = dressed_gram(action, reflection)
        seam_inertias.append(inertia(gram))
        pivots = congruence_pivots(gram)
        seam_congruence_inertias.append(
            (pivots.count(1), pivots.count(-1), pivots.count(0)))
        seam_defects.append(residual_count(gram - gram.H))
        seam_ranks.append(gram.rank())
        if name == "E02":
            e02_pivot_signature = pivot_signature(pivots)
        if name == "b8_type":
            coupling_free_components = support_components(action)
            coupling_free_cross_half = cross_half_entries(action)

    # --- G: THE WALL, W2, and the trace probe in the same sweep ------------
    mass_sweep_inertias = []
    mass_sweep_traces = []
    for mass in MASS_SWEEP:
        gram = dressed_gram(completion(reference_hodge, glue, mass), reflection)
        mass_sweep_inertias.append(inertia(gram))
        mass_sweep_traces.append(sp.expand(gram.trace()))
    geometry_gram_matrix = geometry_gram(reference_hodge, reflection)
    geometry_limit_inertia = inertia(geometry_gram_matrix)
    geometry_limit_defect = residual_count(
        geometry_gram_matrix - geometry_gram_matrix.H)

    # --- G: THE WALL, W3, THE MECHANISM-EXCLUSION THEOREM -------------------
    coefficients = charpoly_coefficients(reference_gram)
    odd_powers = tuple(power for power in range(1, len(coefficients), 2)
                       if coefficients[power] != 0)
    odd_signs = tuple(int(sp.sign(coefficients[power])) for power in odd_powers)
    even_powers = tuple(power for power in range(0, len(coefficients), 2)
                        if coefficients[power] != 0)
    kernel_dimension = 0
    while coefficients[kernel_dimension] == 0:
        kernel_dimension += 1
    characteristic = sp.Poly(list(reversed(coefficients)), LAMBDA)
    reflected = sp.Poly(characteristic.as_expr().subs(LAMBDA, -LAMBDA), LAMBDA)
    spectral_gcd = sp.Poly(sp.gcd(characteristic, reflected), LAMBDA)
    spectral_gcd_is_lambda_fourth = sp.expand(
        spectral_gcd.as_expr() - LAMBDA ** 4) == 0
    # THE DIMENSION THE GCD FORCES.  With no nonzero eigenvalue paired to its
    # negative, S K + K S = 0 kills every nonzero eigenvector and maps ker(K)
    # into ker(K), so the anti-commutant IS End(ker K): dimension (dim ker)^2,
    # every member of rank at most dim ker, and therefore NONE invertible.
    anticommutant_dimension = kernel_dimension ** 2
    candidates = (
        ("xpar", [sp.Integer(-1) ** x
                  for t in POSITIVE_TIMES for x in range(SPACE_EXTENT)]),
        ("tpar", [sp.Integer(-1) ** (t % 2)
                  for t in POSITIVE_TIMES for x in range(SPACE_EXTENT)]),
        ("staggered", [sp.Integer(-1) ** ((t + x) % 2)
                       for t in POSITIVE_TIMES for x in range(SPACE_EXTENT)]),
        ("degree", [sp.Integer(-1) ** ((t % 2) + (x % 2))
                    for t in POSITIVE_TIMES for x in range(SPACE_EXTENT)]),
    )
    candidate_commutators = []
    candidate_anticommutators = []
    antilinear_residual_entries = []
    antilinear_residual_ranks = []
    gram_is_real = all(sp.im(value) == 0 for value in reference_gram)
    for _, diagonal in candidates:
        operator = sp.diag(*diagonal)
        candidate_commutators.append(residual_count(
            operator * reference_gram - reference_gram * operator))
        candidate_anticommutators.append(residual_count(
            operator * reference_gram + reference_gram * operator))
        # THE ANTILINEAR PROBE, WRITTEN OUT RATHER THAN ARGUED: the condition is
        # S conj(K) S^-1 + K = 0, and because K IS REAL this is the linear
        # condition W3 already excludes.  The residuals are measured anyway.
        antilinear = sp.expand(
            operator * sp.conjugate(reference_gram) * operator.inv()
            + reference_gram)
        antilinear_residual_entries.append(nonzero_entries(antilinear))
        antilinear_residual_ranks.append(antilinear.rank())

    # --- G: THE GAMMA0 TWO-SIDED DRESSING, AND WHY IT IS NOT A ROUTE -------
    # K2 = xpar K xpar with xpar real, symmetric and an involution: that is a
    # CONGRUENCE, so Sylvester's law FORCES inertia(K2) = inertia(K) before any
    # arithmetic happens.  IT IS MEASURED ANYWAY, and the congruence relation
    # itself is gated, so the disclosure is a gate and not a sentence.
    half_parity = space_parity(POSITIVE_TIMES)
    gamma0_gram = sp.expand(half_parity * reference_gram * half_parity)
    gamma0_is_congruence = bool(
        residual_count(half_parity - half_parity.T) == 0
        and residual_count(half_parity * half_parity - sp.eye(SPAN_SIZE)) == 0
        and residual_count(
            half_parity * reference_gram * half_parity.T - gamma0_gram) == 0)
    gamma0_inertia = inertia(gamma0_gram)

    # --- G: NO TESTED VARIANT IS DEFINITE ----------------------------------
    tested_inertias = (tuple(seam_inertias) + tuple(mass_sweep_inertias)
                       + (geometry_limit_inertia, gamma0_inertia))
    no_tested_variant_is_definite = all(
        triple[0] < SPAN_SIZE for triple in tested_inertias)
    escape_routes_well_formed = bool(
        isinstance(ESCAPE_ROUTE_VERDICTS, dict)
        and tuple(sorted(ESCAPE_ROUTE_VERDICTS)) == tuple(
            sorted(ESCAPE_ROUTE_NAMES))
        and all(isinstance(verdict, str) and verdict.strip()
                for verdict in ESCAPE_ROUTE_VERDICTS.values()))
    traces_all_positive = all(value > 0 for value in mass_sweep_traces)
    escape_routes_all_negative = bool(
        traces_all_positive
        and gram_is_real
        and all(count != 0 for count in antilinear_residual_entries)
        and gamma0_is_congruence
        and gamma0_inertia == tuple(seam_inertias)[0]
        and no_tested_variant_is_definite)

    citation_pins = {
        "b185_reopen": B185_REOPEN_PIN in landed_text(BLOCK185_NOTE),
        "b185_scope": B185_SCOPE_PIN in landed_text(BLOCK185_NOTE),
        "b184_gram": B184_GRAM_PIN in landed_text(BLOCK184_NOTE),
        "b183_positivity": B183_POSITIVITY_PIN in landed_text(BLOCK183_NOTE),
        "campaign_port": CAMPAIGN_PORT_PIN in landed_text(CAMPAIGN_NOTE),
    }
    banners = {
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "objects_registered": bool(REGISTERED_OBJECTS or ADOPTED_OBJECTS),
        "no_go_claimed": NO_GO_CLAIMED,
        "os_positivity_on_this_frame_claimed":
            OS_POSITIVITY_ON_THIS_FRAME_CLAIMED,
        "mechanism_known": MECHANISM_KNOWN,
        "pairing_generality_claimed": PAIRING_GENERALITY_CLAIMED,
        "b185_positivity_touched": B185_POSITIVITY_TOUCHED,
    }
    # EXACTNESS, MEASURED AND NOT ASSERTED: not one measured scalar is a float.
    exact_scalars = (
        tuple(reference_gram) + tuple(geometry_gram_matrix)
        + tuple(coefficients) + tuple(mass_sweep_traces))
    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        d00_nonzeros=len(positions),
        d00_all_intra_cell=bool(d00_all_intra_cell),
        far_seam_hops=far_seam_hops,
        near_seam_hops=near_seam_hops,
        flat_hodge_is_identity=bool(flat_hodge_is_identity),
        flat_gram_ranks=tuple(flat_gram_ranks),
        curved_inter_cell_ordered=len(curved_inter_cell),
        curved_inter_cell_edges=len(
            {frozenset(position) for position in curved_inter_cell}),
        hodge_inter_cell_ordered=len(hodge_inter_cell),
        hodge_inter_cell_edges=len(
            {frozenset(position) for position in hodge_inter_cell}),
        transport_created_ordered=transport_created,
        flat_inter_cell_ordered=flat_inter_cell,
        differential_inter_cell=differential_inter_cell,
        flat_seam_components=support_components(flat_seam_action),
        flat_seam_cross_half=cross_half_entries(flat_seam_action),
        theta_swaps_halves=bool(theta_swaps_halves),
        flat_seam_gram_nonzeros=nonzero_entries(flat_seam_gram),
        self_dual_dimension=dimension,
        self_dual_off_diagonal=off_diagonal,
        self_dual_shear_points=self_dual_shear_points,
        self_duality_residual_entries=len(residual_entries),
        self_duality_table_exact=bool(self_duality_table_exact),
        field_all_pythagorean=bool(field_all_pythagorean),
        field_value_count=len(field_values),
        restricted_nonzeros=nonzero_entries(restricted),
        glue_nonzeros=nonzero_entries(glue),
        glue_p_odd_residual=residual_count(
            reflection * glue * reflection + glue),
        glue_matches_positive_half=bool(glue_matches_positive_half),
        glue_equals_differential=residual_count(glue - differential) == 0,
        hodge_positive_definite=positive_definite(reference_hodge),
        hodge_p_even_residual=residual_count(
            reflection * reference_hodge * reflection - reference_hodge),
        action_is_real=all(sp.im(value) == 0 for value in reference_action),
        covariance_residual=residual_count(
            reflection * reference_action * reflection - reference_action.T),
        cross_half_entries=cross_half_entries(reference_action),
        dressed_defect=residual_count(reference_gram - reference_gram.H),
        undressed_defect=residual_count(
            reference_undressed - reference_undressed.H),
        dressed_nonzeros=nonzero_entries(reference_gram),
        dressed_rank=reference_gram.rank(),
        seam_names=seam_names,
        seam_inertias=tuple(seam_inertias),
        seam_congruence_inertias=tuple(seam_congruence_inertias),
        seam_self_dual=tuple(seam_self_dual),
        seam_defects=tuple(seam_defects),
        seam_ranks=tuple(seam_ranks),
        two_methods_agree=tuple(seam_inertias)
        == tuple(seam_congruence_inertias),
        coupling_free_components=coupling_free_components,
        coupling_free_cross_half=coupling_free_cross_half,
        e02_pivot_signature=e02_pivot_signature,
        mass_sweep_inertias=tuple(mass_sweep_inertias),
        geometry_limit_inertia=geometry_limit_inertia,
        geometry_limit_defect=geometry_limit_defect,
        odd_coefficient_count=len(odd_powers),
        odd_coefficient_powers=odd_powers,
        odd_coefficient_signs=odd_signs,
        even_coefficient_powers=even_powers,
        spectral_gcd_is_lambda_fourth=bool(spectral_gcd_is_lambda_fourth),
        spectral_gcd_degree=spectral_gcd.degree(),
        kernel_dimension=kernel_dimension,
        anticommutant_dimension=anticommutant_dimension,
        candidate_commutators=tuple(candidate_commutators),
        candidate_anticommutators=tuple(candidate_anticommutators),
        candidates_neither_commute_nor_anticommute=all(
            commutator != 0 and anticommutator != 0
            for commutator, anticommutator
            in zip(candidate_commutators, candidate_anticommutators)),
        traces_all_positive=bool(traces_all_positive),
        reference_trace_positive=bool(mass_sweep_traces[1] > 0),
        gram_is_real=bool(gram_is_real),
        antilinear_residual_entries=tuple(antilinear_residual_entries),
        antilinear_residual_ranks=tuple(antilinear_residual_ranks),
        antilinear_residuals_full_rank=all(
            rank == SPAN_SIZE for rank in antilinear_residual_ranks),
        gamma0_is_congruence=gamma0_is_congruence,
        gamma0_defect=residual_count(gamma0_gram - gamma0_gram.H),
        gamma0_rank=gamma0_gram.rank(),
        gamma0_inertia=gamma0_inertia,
        no_tested_variant_is_definite=bool(no_tested_variant_is_definite),
        escape_routes_well_formed=escape_routes_well_formed,
        escape_routes_all_negative=escape_routes_all_negative,
        exactness_holds=all(is_exact_real(value) for value in exact_scalars),
    )


# ---------------------------------------------------------------------------
# the gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    parent_blobs_ok = (authority.parent_artifact_blobs
                       if claims["parent_pin"] == "resolved"
                       else authority.stale_parent_artifact_blobs)

    # --- A: authority -------------------------------------------------------
    checks.check(
        "A-authority-and-THE-STALE-PIN-THAT-PREDATES-BOTH-ARTIFACTS",
        "THE FIVE-PIN AUTHORITY BLOCK binds origin/main's head, the axioms "
        "blob and the registry blob at origin/main, and the axioms and "
        "registry blobs in the worktree. THE TWO BLOCK 185 ARTIFACTS ARE "
        "CONTENT-BOUND -- its note and its runner, the pair that identifies "
        "the commit this block's branch is cut from -- at PARENT_COMMIT, in "
        "the worktree and against their pinned blobs, and PARENT_COMMIT IS "
        "REAL and PARENT_REF resolves to it, so nothing needs sed at landing. "
        "THE STALE PIN IS THE BLOCK 184 TIP, a REAL ancestor of HEAD that "
        "PREDATES Block 185 and therefore carries NEITHER Block 185 artifact, "
        "which is exactly what makes the stale_parent_authority mutation bite: "
        "under it the gate looks for the artifact blobs at a commit where they "
        "do not exist. AUDIT_INPUT_PATHS IS LITERAL and every one of its EIGHT "
        "entries is required readable in the worktree EXCEPT this block's own "
        "note, which lands later and belongs to gate H -- and the eight "
        "include the LANDED CARRIER this port is built on, the Block 128 "
        "runner, and the campaign anchor the port's phase-1 facts were "
        "recorded in. AND THE MACHINERY IMPORT IS GATED: the LANDED Block 128 "
        "runner must have imported, because the carrier itself -- "
        "cover_index(), cover_embedding(), chart_differential_cover() and the "
        "Block 105 shear_hodge() and overlap_field() it re-exports -- is read "
        "from it, and NOTHING from any scratchpad is imported or read",
        bool(
            AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
            and len(AUDIT_INPUT_PATHS) == 8
            and len(set(AUDIT_INPUT_PATHS)) == 8
            and BLOCK185_NOTE in AUDIT_INPUT_PATHS
            and BLOCK185_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK184_NOTE in AUDIT_INPUT_PATHS
            and BLOCK184_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK183_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_RUNNER in AUDIT_INPUT_PATHS
            and CAMPAIGN_NOTE in AUDIT_INPUT_PATHS
            and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
            and authority.inputs_missing == ()
            and PARENT_ARTIFACTS == (BLOCK185_NOTE, BLOCK185_RUNNER)
            and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
            and facts.main_head == claims["main_head"]
            and authority.fixed_authority
            and authority.machinery_import_landed
            and authority.parent_pin_is_commit
            and authority.parent_ref_and_ancestry
            and parent_blobs_ok
            and authority.stale_is_real_ancestor
            and authority.stale_carries_neither_artifact))

    # --- B: the imposed-object banner and the NOT-CLAIMED keys -------------
    ban = facts.banners
    checks.check(
        "B-THE-IMPOSED-OBJECT-BANNER-and-THE-WALL-IS-NOT-A-NO-GO",
        f"THE BANNER COMES BEFORE ANY NUMERAL AND IT IS MEASURED RATHER THAN "
        f"ASSERTED. {ban['imposed_objects']} objects are IMPOSED by this block "
        f"-- the section frame as the Blocks 181-185 lane landed it, the "
        f"dressed reflection with the anchor reflection and its dressing sign, "
        f"THE GLUED HODGE which is this block's own object, the seam modulus "
        f"family with its six tested directions, the restricted set with the "
        f"derived glue and the glued action, and the dressed pairing with the "
        f"two neighbours built only to be measured failing -- and "
        f"{ban['registered_objects']} are REGISTERED and "
        f"{ban['adopted_objects']} are ADOPTED. AND THE BANNER'S SECOND HALF "
        f"IS WHAT IS NOT CLAIMED, gated as declared constants. THE FIRST OF "
        f"THEM IS THE ONE THAT MATTERS: THIS IS NOT A NO-GO "
        f"({ban['no_go_claimed']}). An obstruction that survives six seam "
        f"directions, five masses, the pure-geometry limit AND three escape "
        f"probes READS as a proof that this frame cannot carry OS positivity, "
        f"and it is NOT one -- exactly ONE pairing family is tested, at ONE "
        f"value of s, on ONE fixture, and the note's LIMITS name SEVEN VARIANT "
        f"CLASSES that are UNTESTED. NO OS POSITIVITY ON THIS FRAME IS CLAIMED "
        f"({ban['os_positivity_on_this_frame_claimed']}); NO MECHANISM for the "
        f"balance is known ({ban['mechanism_known']}) -- W3 EXCLUDES every "
        f"linear anti-symmetry mechanism and SUPPLIES none, so the cause is "
        f"OPEN; NO PAIRING-GENERALITY is claimed "
        f"({ban['pairing_generality_claimed']}); and BLOCK 185'S LANDED "
        f"POSITIVITY ON THE BLOCK 107 CARRIER IS UNTOUCHED "
        f"({ban['b185_positivity_touched']}) -- that is a DIFFERENT CARRIER, "
        f"and this block is COMPLEMENTARY to Block 185 and NOT CONTRADICTORY. "
        f"Asserting the no-go, or that the mechanism is known, or that the "
        f"imposed objects are registered, fails HERE and nowhere else",
        bool(
            ban["imposed_objects"] == 6
            and ban["registered_objects"] == 0
            and ban["adopted_objects"] == 0
            and ban["objects_registered"] == claims["objects_registered"]
            and ban["no_go_claimed"] == claims["no_go_claimed"]
            and ban["os_positivity_on_this_frame_claimed"]
            == claims["os_positivity_on_this_frame_claimed"]
            and ban["mechanism_known"] == claims["mechanism_known"]
            and ban["pairing_generality_claimed"]
            == claims["pairing_generality_claimed"]
            and ban["b185_positivity_touched"]
            == claims["b185_positivity_touched"]))

    # --- C: the citation pins, then the port's structural theorems ----------
    pins = facts.citation_pins
    checks.check(
        "C-THE-HAND-OFF-AND-THE-SCOPE-ARE-READ-FROM-THE-PRIMARY-BODIES",
        f"WHAT THIS BLOCK ANSWERS IS PINNED IN THE NOTES THAT LEFT IT OPEN, "
        f"not in a recollection of them. Block 185's REOPEN item "
        f"'{B185_REOPEN_PIN}' is present in its primary body "
        f"({pins['b185_reopen']}) and is the sentence this block answers; its "
        f"scope line '{B185_SCOPE_PIN}' ({pins['b185_scope']}) is what makes "
        f"this block NECESSARY rather than redundant, because Block 185's "
        f"result is on a DIFFERENT carrier. Block 184's "
        f"'{B184_GRAM_PIN}' ({pins['b184_gram']}) is what the section frame "
        f"still lacked. Block 183's '{B183_POSITIVITY_PIN}' "
        f"({pins['b183_positivity']}) is the standing this block does NOT "
        f"overturn. And the campaign anchor's '{CAMPAIGN_PORT_PIN}' "
        f"({pins['campaign_port']}) is the port's own provenance. EVERY ONE IS "
        f"A LANDED OR RECORDED SENTENCE, READ AT ITS OWN PATH",
        bool(all(pins.values()) == claims["citation_pins"]))
    checks.check(
        "C-F1-THE-CHART-DIFFERENTIAL-IS-CELL-LOCAL-with-ZERO-SEAM-HOPS",
        f"F1, AND IT IS THE FACT THE WHOLE DIAGNOSIS TURNS ON. d_00 carries "
        f"EXACTLY {facts.d00_nonzeros} nonzero entries and EVERY ONE OF THEM "
        f"LIES INSIDE A 2x2 EVEN-ANCHORED CELL ({facts.d00_all_intra_cell}): "
        f"{facts.differential_inter_cell} entries are inter-cell, EXACTLY "
        f"{facts.far_seam_hops} cross the far seam {{3,4}} and EXACTLY "
        f"{facts.near_seam_hops} cross the near seam {{7,0}}. MATTER DOES NOT "
        f"CROSS EITHER SEAM ON THIS CARRIER, so the antiperiodic edge negation "
        f"that Block 107's carrier needed is VACUOUS here -- there is no edge "
        f"to negate. AND THAT IS WHY THE HALVES DISCONNECT under a flat seam: "
        f"cell-local matter plus a coupling-free seam anchor leaves nothing to "
        f"carry the two halves into contact. Asserting a seam hop fails HERE "
        f"and nowhere else",
        bool(
            facts.d00_nonzeros == claims["d00_nonzeros"]
            and facts.d00_all_intra_cell == claims["d00_all_intra_cell"]
            and facts.far_seam_hops == claims["far_seam_hops"]
            and facts.near_seam_hops == claims["near_seam_hops"]
            and facts.differential_inter_cell
            == claims["differential_inter_cell"]))
    checks.check(
        "C-F2-THE-FLAT-THEORY-IS-DISCONNECTED-and-NO-CALIBRATION-EXISTS",
        f"F2: the flat overlap Hodge is EXACTLY the 32x32 identity "
        f"({facts.flat_hodge_is_identity}), so the flat completion is "
        f"block-diagonal over sixteen disjoint cells and THE FLAT REFLECTED "
        f"GRAM IS IDENTICALLY ZERO -- ranks {facts.flat_gram_ranks} on the "
        f"two-slice span, the {{0,3}} span and the full-half span, DRESSED AND "
        f"UNDRESSED ALIKE. NO FLAT CALIBRATION EXISTS ON THIS FAMILY, so Block "
        f"107's transfer strategy fails STRUCTURALLY and not numerically, and "
        f"there is no digit-for-digit control to be had here at any price -- "
        f"which is why this block's controls are STRUCTURAL IDENTITIES rather "
        f"than somebody else's numbers. Asserting a nonzero flat Gram fails "
        f"HERE and nowhere else",
        bool(
            facts.flat_hodge_is_identity == claims["flat_hodge_is_identity"]
            and facts.flat_gram_ranks == claims["flat_gram_ranks"]))
    checks.check(
        "C-F3-THE-INTER-CELL-CENSUS-CORRECTED-144-72-48-96",
        f"F3, IN THE FORM THE ADVERSARIAL CHECK CORRECTED IT TO, AND THE "
        f"CORRECTION IS THIS BLOCK'S OWN. The curved NO-GLUE completion carries "
        f"EXACTLY {facts.curved_inter_cell_ordered} ORDERED inter-cell entries "
        f"on EXACTLY {facts.curved_inter_cell_edges} UNORDERED EDGES; the "
        f"curved Hodge ITSELF carries EXACTLY {facts.hodge_inter_cell_ordered} "
        f"ORDERED entries on {facts.hodge_inter_cell_edges} of those edges; and "
        f"EXACTLY {facts.transport_created_ordered} ORDERED entries are CREATED "
        f"by the transport term i(H d + d^H H) beyond the Hodge's own support. "
        f"THE CAUSAL STATEMENT SURVIVES AND THE WORDING DOES NOT: the FLAT "
        f"Hodge is the identity and carries {facts.flat_inter_cell_ordered} "
        f"inter-cell entries, so ALL {facts.curved_inter_cell_edges} curved "
        f"edges are H-INDUCED -- but 'H-BORNE' MUST NOT BE READ AS 'IN H's "
        f"SUPPORT', because {facts.transport_created_ordered} of the "
        f"{facts.curved_inter_cell_ordered} are NOT in it. The solve's original "
        f"'96 inter-cell entries' was the ORDERED SUPPORT INCREMENT mislabelled "
        f"as the TOTAL, and it is CORRECTED HERE. Asserting 96 as the total "
        f"fails HERE and nowhere else",
        bool(
            facts.curved_inter_cell_ordered
            == claims["curved_inter_cell_ordered"]
            and facts.curved_inter_cell_edges
            == claims["curved_inter_cell_edges"]
            and facts.hodge_inter_cell_ordered
            == claims["hodge_inter_cell_ordered"]
            and facts.hodge_inter_cell_edges
            == claims["hodge_inter_cell_edges"]
            and facts.transport_created_ordered
            == claims["transport_created_ordered"]
            and facts.flat_inter_cell_ordered
            == claims["flat_inter_cell_ordered"]))

    # --- D: the diagnosis and the seam modulus ------------------------------
    checks.check(
        "D-THE-SELECTION-RULE-TWO-COMPONENTS-THAT-ARE-THE-TWO-HALVES",
        f"THE RULE, FOUND RATHER THAN GUESSED. With FLAT seam blocks the glued "
        f"action's support graph has components of sizes "
        f"{facts.flat_seam_components} -- TWO OF THEM AND THEY ARE THE TWO "
        f"HALVES -- at EXACTLY {facts.flat_seam_cross_half} cross-half "
        f"entries. theta maps the positive half exactly onto the negative half "
        f"({facts.theta_swaps_halves}), so EVERY (b, theta a) pair STRADDLES "
        f"the two components, and the dressed Gram has EXACTLY "
        f"{facts.flat_seam_gram_nonzeros} nonzero entries: IT VANISHES "
        f"IDENTICALLY. THE ZERO GRAM WAS NEVER A CANCELLATION -- the glued "
        f"action simply had no seam coupling at all, because matter is "
        f"cell-local by F1 and a flat seam anchor contributes only DIAGONALLY "
        f"through its straddling embedding. Block 107 never faced this because "
        f"THEIR matter crossed the seam. Asserting a connected flat-seam "
        f"action fails HERE and nowhere else",
        bool(
            facts.flat_seam_components == claims["flat_seam_components"]
            and facts.flat_seam_cross_half == claims["flat_seam_cross_half"]
            and facts.theta_swaps_halves == claims["theta_swaps_halves"]
            and facts.flat_seam_gram_nonzeros
            == claims["flat_seam_gram_nonzeros"]))
    checks.check(
        "D-THE-SEAM-IS-A-MODULUS-and-FLAT-IS-UNIQUE-ONLY-AT-POSITIVE-VOLUME",
        f"THE FIX IS DERIVED FROM DUALITY. The straddling anchors t = 3 and "
        f"t = 7 are the FIXED POINTS of thA(t) = (-2-t)%8, so their blocks must "
        f"be SELF-DUAL -- and the DRESSED self-dual symmetric space "
        f"B = (P4 Xi) B (P4 Xi)^T is EXACTLY "
        f"{facts.self_dual_dimension}-DIMENSIONAL with EXACTLY "
        f"{facts.self_dual_off_diagonal} off-diagonal directions. THE SEAM IS "
        f"A MODULUS, and it is the ADM seam data. AND THE SHEAR FAMILY CANNOT "
        f"SUPPLY IT, AT A SCOPE THE ADVERSARIAL CHECK CORRECTED. The P4 "
        f"self-duality residual R = H - P4 H P4^T has EXACTLY "
        f"{facts.self_duality_residual_entries} nonzero symbolic entries and "
        f"matches the exact table {facts.self_duality_table_exact}: "
        f"R00 = q^2 v/(q^2-1) = -R22, R11 = (1-q^2-v^2)/(v(q^2-1)) = -R33, "
        f"R12 = R21 = qv/(q^2-1) and R03 = R30 = -qv/(q^2-1). ITS EXACT "
        f"SOLUTION SET AT NONZERO VOLUME IS {facts.self_dual_shear_points} -- "
        f"BOTH (0,1) AND (0,-1) -- SO 'THE FLAT BLOCK IS THE UNIQUE SELF-DUAL "
        f"MEMBER OF THE SHEAR FAMILY' IS TRUE ONLY UNDER THE CONVENTIONAL "
        f"POSITIVE-VOLUME RESTRICTION v > 0, WHICH IS STATED WHEREVER THE "
        f"LEMMA APPEARS. Under it, Block 107's forced-flat seam rows are "
        f"RE-DERIVED FROM DUALITY rather than prescribed. AND THE ASIDE IS "
        f"MEASURED TOO: all {facts.field_value_count} values of the LANDED "
        f"Block 105 overlap field are PYTHAGOREAN, q^2 + v^2 = 1 exactly "
        f"({facts.field_all_pythagorean}), so every landed field block kills "
        f"the R11 factor and is HALF self-dual -- and none is self-dual. "
        f"Asserting a rigid seam fails HERE and nowhere else",
        bool(
            facts.self_dual_dimension == claims["self_dual_dimension"]
            and facts.self_dual_off_diagonal == claims["self_dual_off_diagonal"]
            and facts.self_dual_shear_points == claims["self_dual_shear_points"]
            and facts.self_duality_residual_entries
            == claims["self_duality_residual_entries"]
            and facts.self_duality_table_exact
            == claims["self_duality_table_exact"]
            and facts.field_all_pythagorean == claims["field_all_pythagorean"]
            and facts.field_value_count == claims["field_value_count"]))

    # --- E: the construction ------------------------------------------------
    checks.check(
        "E-THE-CONSTRUCTION-REAL-COVARIANT-CONNECTED-and-THE-DRESSING-EARNS-IT",
        f"EVERY STRUCTURAL PROPERTY OF THE CONSTRUCTION, MEASURED. THE GLUE: "
        f"A keeps {facts.restricted_nonzeros} of d_00's entries and "
        f"D = A - Px A Px carries EXACTLY {facts.glue_nonzeros}; D is Px-ODD at "
        f"{facts.glue_p_odd_residual} residual, EQUALS d_00 entrywise on the "
        f"positive half ({facts.glue_matches_positive_half}) so THE PHYSICAL "
        f"DYNAMICS IS UNTOUCHED, and is NOT d_00 globally "
        f"({not facts.glue_equals_differential}). THE GEOMETRY: H_g is "
        f"POSITIVE DEFINITE by 32 exact leading minors "
        f"({facts.hodge_positive_definite}) and Px-EVEN at "
        f"{facts.hodge_p_even_residual}. THE ACTION IS REAL "
        f"({facts.action_is_real}) -- every entry of Q_g -- SO THE BLOCK 185 "
        f"C8 REALITY CONDITION IS SATISFIED BY THIS CONSTRUCTION, the solve's "
        f"earlier reading that it was NOT real was a SYMBOLIC-ASSUMPTIONS "
        f"ARTIFACT caught inside the solve and GATED HERE, AND THE SAME "
        f"REALITY IS WHAT COLLAPSES THE ANTILINEAR ESCAPE ROUTE IN GATE G. "
        f"Px Q_g Px = Q_g^T at {facts.covariance_residual}. THE HALVES "
        f"CONNECT: EXACTLY {facts.cross_half_entries} cross-half entries at "
        f"the E02 seam. AND THE DRESSING IS WHAT MAKES THE PAIRING HERMITIAN, "
        f"measured against its undressed neighbour in the same run: the "
        f"DRESSED Gram's defect is {facts.dressed_defect} at "
        f"{facts.dressed_nonzeros} nonzero entries and rank "
        f"{facts.dressed_rank}, while the UNDRESSED formula "
        f"conj(G(b, theta a)) has {facts.undressed_defect} nonzero defect "
        f"entries -- the dressing enters the PAIRING exactly as Block 104's "
        f"Gamma0 does. Asserting a complex action fails HERE and nowhere else",
        bool(
            facts.restricted_nonzeros == claims["restricted_nonzeros"]
            and facts.glue_nonzeros == claims["glue_nonzeros"]
            and facts.glue_p_odd_residual == claims["glue_p_odd_residual"]
            and facts.glue_matches_positive_half
            == claims["glue_matches_positive_half"]
            and facts.hodge_positive_definite
            == claims["hodge_positive_definite"]
            and facts.hodge_p_even_residual == claims["hodge_p_even_residual"]
            and facts.action_is_real == claims["action_is_real"]
            and facts.covariance_residual == claims["covariance_residual"]
            and facts.cross_half_entries == claims["cross_half_entries"]
            and facts.dressed_defect == claims["dressed_defect"]
            and facts.dressed_nonzeros == claims["dressed_nonzeros"]
            and facts.dressed_rank == claims["dressed_rank"]
            # THE FAILING NEIGHBOURS, asserted unconditionally: the undressed
            # pairing must FAIL Hermiticity and D must not be d_00 globally.
            and facts.undressed_defect == claims["undressed_defect"]
            and facts.undressed_defect != 0
            and not facts.glue_equals_differential))

    # --- F: THE WALL, W1 ----------------------------------------------------
    checks.check(
        "F-THE-WALL-W1-BALANCED-IN-EVERY-COUPLING-DIRECTION-BY-TWO-METHODS",
        f"THE SEAM-DIRECTION SWEEP, at m = {MASS} and s = {SEAM_PARAMETER}, "
        f"REBUILDING EVERYTHING BY THE SAME CODE with only the seam block "
        f"changed. All six blocks are exactly DRESSED SELF-DUAL "
        f"({facts.seam_self_dual}) and all six dressed Grams are exactly "
        f"HERMITIAN at defects {facts.seam_defects}. THE INERTIAS, as "
        f"(positive, negative, zero), MEASURED TWICE BY DISJOINT EXACT "
        f"METHODS -- charpoly Descartes and symmetric congruence elimination, "
        f"which agree at every direction ({facts.two_methods_agree}): "
        f"{facts.seam_names} give {facts.seam_inertias} at ranks "
        f"{facts.seam_ranks}, and congruence independently gives "
        f"{facts.seam_congruence_inertias}. THE E02 AND E13 SEAMS ARE BALANCED "
        f"AT (+6,-6,0x4); the b5-type mixed-sign seam is BALANCED AT "
        f"(+3,-3,0x10); THE ADVERSARIAL CHECK'S TWO EXPLICIT GENERIC POINTS "
        f"Bgen1 and Bgen2 -- which REPLACE the solve's original 'generic mixed "
        f"seam', that one being NOT REPRODUCIBLE -- are BOTH BALANCED AT "
        f"(+6,-6,0x4), AND THEY ARE TWO POINTS AND NOT A UNIVERSAL 'GENERIC' "
        f"ASSERTION; and the b8-type seam gives THE ZERO GRAM. AND THE ZERO IS "
        f"THE DIAGNOSIS RECURRING RATHER THAN A MYSTERY: that direction couples "
        f"slot 0 to slot 1 and slot 2 to slot 3, BOTH AT THE SAME TIME inside a "
        f"straddling cell, so it carries NO seam coupling -- its glued action "
        f"has components {facts.coupling_free_components} at "
        f"{facts.coupling_free_cross_half} cross-half entries, EXACTLY LIKE A "
        f"FLAT SEAM. EXACTLY ONE OF THE FOUR OFF-DIAGONAL SELF-DUAL DIRECTIONS "
        f"IS COUPLING-FREE, AND EVERY COUPLING-CARRYING DIRECTION TESTED LANDS "
        f"ON A BALANCED INERTIA. The congruence pivot signature at the E02 seam "
        f"is {facts.e02_pivot_signature}. Asserting a definite Gram at the E02 "
        f"seam fails HERE and nowhere else",
        bool(
            facts.seam_inertias == claims["seam_inertias"]
            and all(facts.seam_self_dual) == claims["seams_all_self_dual"]
            and all(defect == 0 for defect in facts.seam_defects)
            == claims["seams_all_hermitian"]
            and facts.two_methods_agree == claims["two_methods_agree"]
            and facts.coupling_free_components
            == claims["coupling_free_components"]
            and facts.coupling_free_cross_half
            == claims["coupling_free_cross_half"]
            and facts.e02_pivot_signature == claims["e02_pivot_signature"]
            and facts.seam_ranks[2] == B5_TYPE_RANK))

    # --- G: THE WALL, W2 and W3, and the escape routes ---------------------
    checks.check(
        "G-THE-WALL-W2-BALANCED-AT-EVERY-MASS-and-IN-THE-GEOMETRY-LIMIT",
        f"THE MASS SWEEP, AND IT WAS RUN BEFORE ANY STRUCTURAL LABEL HARDENED "
        f"-- the control-first rule applied at the right moment for once, so "
        f"'balanced inertia' was a MEASURED INVARIANCE before it was ever a "
        f"NAME. At the E02 seam the inertia is {facts.mass_sweep_inertias} at "
        f"m = {tuple(str(mass) for mass in MASS_SWEEP)}: IDENTICAL AT EVERY "
        f"ONE OF FIVE MASSES SPANNING A FACTOR OF THIRTY. AND THE "
        f"PURE-GEOMETRY LIMIT SETTLES WHERE IT DOES NOT COME FROM: K built "
        f"from H_g^-1 ALONE, with NO completion, no matter and no mass at all, "
        f"is {facts.geometry_limit_inertia} at Hermiticity defect "
        f"{facts.geometry_limit_defect} -- BALANCED EVEN IN THE LIMIT. THE "
        f"BALANCE IS NEITHER A MASS EFFECT NOR A MATTER EFFECT. Asserting that "
        f"the inertia moves with the mass fails HERE and nowhere else",
        bool(
            facts.mass_sweep_inertias == claims["mass_sweep_inertias"]
            and facts.geometry_limit_inertia
            == claims["geometry_limit_inertia"]
            and facts.geometry_limit_defect
            == claims["geometry_limit_defect"]))
    checks.check(
        "G-THE-WALL-W3-THE-MECHANISM-EXCLUSION-THEOREM-STRENGTHENED",
        f"THE MECHANISM-EXCLUSION THEOREM, AND IT IS THE BLOCK'S ONE THEOREM "
        f"ABOUT THE WALL RATHER THAN A MEASUREMENT OF IT. The charpoly of the "
        f"dressed Gram has EXACTLY {facts.odd_coefficient_count} NONZERO "
        f"ODD-POWER COEFFICIENTS, at powers {facts.odd_coefficient_powers} with "
        f"signs {facts.odd_coefficient_signs}, against even powers "
        f"{facts.even_coefficient_powers}, SO THE SPECTRUM IS NOT PLUS-MINUS "
        f"SYMMETRIC. An invertible S with S K S^-1 = -K makes K and -K similar "
        f"and therefore FORCES plus-minus pairing of the whole spectrum, SO NO "
        f"SUCH S EXISTS. AND THE ADVERSARIAL CHECK STRENGTHENED IT TO ITS SHARP "
        f"FORM: gcd(charpoly(x), charpoly(-x)) IS EXACTLY x^4 "
        f"({facts.spectral_gcd_is_lambda_fourth}, degree "
        f"{facts.spectral_gcd_degree}), so NO nonzero eigenvalue is paired with "
        f"its negative AT ALL; therefore any S with S K + K S = 0 annihilates "
        f"every nonzero eigenvector and maps the "
        f"{facts.kernel_dimension}-dimensional kernel into itself, so THE "
        f"ANTI-COMMUTANT IS EXACTLY THE SPACE OF KERNEL-TO-KERNEL MAPS: "
        f"DIMENSION EXACTLY {facts.anticommutant_dimension} = "
        f"{facts.kernel_dimension}^2, EVERY MEMBER KERNEL-SUPPORTED OF RANK AT "
        f"MOST {facts.kernel_dimension}, AND NONE INVERTIBLE. The four natural "
        f"diagonal candidates NEITHER COMMUTE NOR ANTICOMMUTE "
        f"({facts.candidates_neither_commute_nor_anticommute}), at commutator "
        f"counts {facts.candidate_commutators} and anticommutator counts "
        f"{facts.candidate_anticommutators}. THE MECHANISM IS EXCLUDED AND NOT "
        f"EXPLAINED: THE CAUSE OF THE BALANCE IS OPEN. Every value above is an "
        f"exact rational ({facts.exactness_holds}) and NO nsimplify is applied "
        f"to any measured scalar anywhere in this runner. Asserting a "
        f"plus-minus symmetric spectrum, or a spectral gcd other than x^4, "
        f"fails HERE and nowhere else",
        bool(
            facts.odd_coefficient_count == claims["odd_coefficient_count"]
            and facts.odd_coefficient_powers
            == claims["odd_coefficient_powers"]
            and facts.odd_coefficient_signs == claims["odd_coefficient_signs"]
            and facts.spectral_gcd_is_lambda_fourth
            == claims["spectral_gcd_is_lambda_fourth"]
            and facts.spectral_gcd_degree == claims["spectral_gcd_degree"]
            and facts.kernel_dimension == claims["kernel_dimension"]
            and facts.anticommutant_dimension
            == claims["anticommutant_dimension"]
            and facts.candidates_neither_commute_nor_anticommute
            == claims["candidates_neither_commute_nor_anticommute"]
            and len(facts.candidate_commutators) == DIAGONAL_CANDIDATE_COUNT
            and facts.exactness_holds))
    checks.check(
        "G-THE-THREE-ESCAPE-ROUTES-ARE-ALL-MEASURED-NEGATIVE",
        f"THE ESCAPE ROUTES, PROBED BY THE ADVERSARIAL CHECK AND RE-MEASURED "
        f"HERE RATHER THAN CITED. (i) THE TRACE IDENTITY IS DEAD: tr K is "
        f"STRICTLY POSITIVE at all five masses ({facts.traces_all_positive}), "
        f"and at the reference fixture in particular "
        f"({facts.reference_trace_positive}) -- it is NOT zero, so no trace "
        f"identity forces the balance and none is available as an escape; the "
        f"exact giant rationals are displayed in {CHECK_FINDINGS}. (ii) THE "
        f"ANTILINEAR ROUTE COLLAPSES: K IS REAL ({facts.gram_is_real}), so the "
        f"antilinear condition S conj(K) S^-1 = -K IS the linear similarity "
        f"W3 ALREADY EXCLUDES -- and the direct residuals confirm it, the four "
        f"diagonal candidates giving {facts.antilinear_residual_entries} "
        f"nonzero entries at ranks {facts.antilinear_residual_ranks} "
        f"({facts.antilinear_residuals_full_rank} full rank), with the "
        f"half-reflection composites at 200-208 entries in the findings file. "
        f"(iii) THE GAMMA0 TWO-SIDED DRESSING IS NOT AN INDEPENDENT CANDIDATE "
        f"AT ALL, AND THAT IS DISCLOSED AS A GATE RATHER THAN CONFESSED: "
        f"K2 = xpar K xpar is a CONGRUENCE of K by a real symmetric involution "
        f"({facts.gamma0_is_congruence}), so SYLVESTER'S LAW FORCES its inertia "
        f"to equal K's BEFORE any arithmetic happens -- measured "
        f"{facts.gamma0_inertia} at rank {facts.gamma0_rank} and defect "
        f"{facts.gamma0_defect}. THE VARIANT'S DESIGN WAS THE SUPERVISOR'S "
        f"ERROR AND THE CHECKER'S IDENTIFICATION OF IT IS WHAT CLOSED THE "
        f"ROUTE. AND (iv) NO TESTED VARIANT IS POSITIVE DEFINITE "
        f"({facts.no_tested_variant_is_definite}) across all six seam "
        f"directions, five masses, the geometry limit and the Gamma0 variant: "
        f"THE WALL STANDS. All three verdict strings are declared and "
        f"well-formed ({facts.escape_routes_well_formed}) and every one of them "
        f"is NEGATIVE ({facts.escape_routes_all_negative}). Asserting that the "
        f"Gamma0 dressing changes the inertia fails HERE and nowhere else",
        bool(
            facts.traces_all_positive == claims["traces_all_positive"]
            and facts.gram_is_real == claims["gram_is_real"]
            and facts.antilinear_residual_entries
            == claims["antilinear_residual_entries"]
            and facts.antilinear_residuals_full_rank
            == claims["antilinear_residuals_full_rank"]
            and facts.gamma0_is_congruence == claims["gamma0_is_congruence"]
            and facts.gamma0_inertia == claims["gamma0_inertia"]
            and facts.no_tested_variant_is_definite
            == claims["no_tested_variant_is_definite"]
            and facts.escape_routes_well_formed
            == claims["escape_routes_well_formed"]
            and facts.escape_routes_all_negative
            == claims["escape_routes_all_negative"]))

    # --- H: the note at its final path, and the N5 fence -------------------
    required = tuple(claims["required_scope_keys"])
    checks.check(
        "H-note-at-final-path-and-the-N5-fence",
        f"the note is read at its FINAL PATH {facts.note_at_final_path} -- "
        f"THERE IS NO DRAFT FALLBACK ANYWHERE IN THIS RUNNER, so when False "
        f"the note has not landed at docs/ yet, gate H is EXPECTED to fail on "
        f"that alone, and families A through G are unaffected. The N5 fence is "
        f"an N5-prefixed single-line literal with nine labelled sections that "
        f"must appear BYTE-IDENTICALLY in the note, the required scope-key set "
        f"is THE FULL DECLARED SET and not a subset, and the mutation battery "
        f"is seventeen members mapped one-per-family across A through H",
        bool(
            facts.note_at_final_path
            and NOTE_PATH.name == FINAL_NOTE_NAME
            and set(facts.scope) == set(SCOPE_KEYS)
            and required == SCOPE_KEYS
            and all(facts.scope[key] for key in required)
            and facts.scope["n5_verbatim"]
            and len(MUTATIONS) == 17
            and len(set(MUTATIONS)) == 17
            and set(MUTATION_GATE) == set(MUTATIONS)
            and set(MUTATION_GATE.values()) == set("ABCDEFGH")
            and N5_FENCE.startswith("N5: ")
            and 9 <= N5_FENCE.count("\n") + 1 <= 12
            and all(N5_FENCE.count(f"\n{name}:") == 1
                    for name in ("per_site", "per_mode", "per_block",
                                 "lattice_wide", "per_scope", "RESULT",
                                 "DECISION_CUT", "TOE"))))
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    authority = facts.authority
    ban = facts.banners
    print("MEASURED, before any gate is read:")
    print(f"  AUTHORITY: origin/main resolves to {facts.main_head}; the "
          f"five-pin block is fixed {authority.fixed_authority}. "
          f"PARENT_COMMIT {PARENT_COMMIT} is REAL and PARENT_REF resolves to "
          f"it {authority.parent_ref_and_ancestry}, and BOTH Block 185 "
          f"artifacts are content-bound there and in the worktree "
          f"{authority.parent_artifact_blobs}. THE AUDIT INPUTS: "
          f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} "
          f"readable in the worktree (this block's own note excluded, since it "
          f"lands later and is gate H's), missing {authority.inputs_missing}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {authority.stale_is_real_ancestor} and carries NEITHER Block "
          f"185 artifact {authority.stale_carries_neither_artifact} -- it is "
          f"the Block 184 tip, which PREDATES both artifacts, and that absence "
          f"is exactly what makes the stale_parent_authority mutation bite")
    print(f"  THE MACHINERY: THE CARRIER IS LANDED AND IMPORTED, NOT REBUILT. "
          f"The Block 128 runner imported {authority.machinery_import_landed} "
          f"for FIVE objects -- cover_index(), cover_embedding(), "
          f"chart_differential_cover() and the Block 105 shear_hodge() and "
          f"overlap_field() it re-exports. The cover is "
          f"{TIME_EXTENT}x{SPACE_EXTENT} at dimension {COVER_SIZE}, the span "
          f"Lambda_+ is the {SPAN_SIZE} sites with t in {POSITIVE_TIMES} in "
          f"t-major order, the reference fixture is m = {MASS} at seam "
          f"parameter s = {SEAM_PARAMETER}, and the PORT'S OWN objects -- the "
          f"dressed reflection, the anchor reflection, the glued Hodge, the "
          f"seam family, the restricted set, the derived glue and the dressed "
          f"pairing -- are built HERE. NOTHING from any scratchpad is imported "
          f"or read")
    print(f"  THE BANNER: {ban['imposed_objects']} imposed objects, "
          f"{ban['registered_objects']} registered and "
          f"{ban['adopted_objects']} adopted; MEASURED no-go-claimed "
          f"{ban['no_go_claimed']}, os-positivity-on-this-frame-claimed "
          f"{ban['os_positivity_on_this_frame_claimed']}, mechanism-known "
          f"{ban['mechanism_known']}, pairing-generality-claimed "
          f"{ban['pairing_generality_claimed']} and b185-positivity-touched "
          f"{ban['b185_positivity_touched']}. THE WALL IS NOT A NO-GO. The "
          f"imposed objects are {IMPOSED_OBJECTS}")
    print(f"  THE CITATION PINS: {facts.citation_pins} -- the hand-off, the "
          f"scope line, the missing Gram, the standing firewall and the port's "
          f"own provenance, each read at its own path")
    print(f"  F1, CELL-LOCALITY: d_00 has {facts.d00_nonzeros} entries, all "
          f"intra-cell {facts.d00_all_intra_cell}, "
          f"{facts.differential_inter_cell} inter-cell, {facts.far_seam_hops} "
          f"far-seam hops and {facts.near_seam_hops} near-seam hops. THE "
          f"ANTIPERIODIC EDGE NEGATION IS VACUOUS ON THIS CARRIER")
    print(f"  F2, DISCONNECTION: the flat overlap Hodge is the identity "
          f"{facts.flat_hodge_is_identity} and the flat reflected Gram has "
          f"ranks {facts.flat_gram_ranks} across three spans, dressed and "
          f"undressed. NO FLAT CALIBRATION EXISTS ON THIS FAMILY")
    print(f"  F3, THE CORRECTED CENSUS: the curved no-glue completion has "
          f"{facts.curved_inter_cell_ordered} ORDERED inter-cell entries on "
          f"{facts.curved_inter_cell_edges} EDGES; the curved Hodge itself has "
          f"{facts.hodge_inter_cell_ordered} ORDERED on "
          f"{facts.hodge_inter_cell_edges} edges; "
          f"{facts.transport_created_ordered} ORDERED are CREATED by the "
          f"transport term; and the FLAT Hodge has "
          f"{facts.flat_inter_cell_ordered}. ALL "
          f"{facts.curved_inter_cell_edges} CURVED EDGES ARE H-INDUCED, AND "
          f"'H-BORNE' IS NOT 'IN H's SUPPORT' -- the original '96' was the "
          f"ORDERED SUPPORT INCREMENT, mislabelled as the total, and this is "
          f"THE FOURTEENTH SUPERVISOR CORRECTION")
    print(f"  THE DIAGNOSIS: with a FLAT seam the glued action has components "
          f"{facts.flat_seam_components} at {facts.flat_seam_cross_half} "
          f"cross-half entries, theta swaps the halves "
          f"{facts.theta_swaps_halves}, and the dressed Gram has "
          f"{facts.flat_seam_gram_nonzeros} nonzero entries")
    print(f"  THE SEAM MODULUS: the DRESSED self-dual symmetric space is "
          f"{facts.self_dual_dimension}-dimensional with "
          f"{facts.self_dual_off_diagonal} off-diagonal directions; the shear "
          f"family's P4 self-duality residual has "
          f"{facts.self_duality_residual_entries} symbolic entries matching "
          f"the exact table {facts.self_duality_table_exact}, and its EXACT "
          f"solution set at nonzero volume is {facts.self_dual_shear_points} "
          f"-- SO FLAT IS THE UNIQUE SELF-DUAL SHEAR MEMBER ONLY AT v > 0. All "
          f"{facts.field_value_count} landed field values are PYTHAGOREAN "
          f"{facts.field_all_pythagorean}, so every field block is HALF "
          f"self-dual and none is self-dual")
    print(f"  THE CONSTRUCTION: A has {facts.restricted_nonzeros} entries and "
          f"D has {facts.glue_nonzeros}; D is Px-odd at "
          f"{facts.glue_p_odd_residual}, equals d_00 on the positive half "
          f"{facts.glue_matches_positive_half} and is not d_00 globally "
          f"{not facts.glue_equals_differential}. H_g is positive definite "
          f"{facts.hodge_positive_definite} and Px-even at "
          f"{facts.hodge_p_even_residual}. Q_g IS REAL {facts.action_is_real} "
          f"and Px-covariant at {facts.covariance_residual}, the halves "
          f"connect at {facts.cross_half_entries} cross-half entries, and the "
          f"DRESSED Gram's defect is {facts.dressed_defect} at "
          f"{facts.dressed_nonzeros} entries and rank {facts.dressed_rank} "
          f"against the UNDRESSED formula's {facts.undressed_defect}")
    print(f"  THE WALL, W1: {facts.seam_names} -> {facts.seam_inertias} at "
          f"ranks {facts.seam_ranks}, all self-dual {facts.seam_self_dual}, "
          f"all Hermitian at defects {facts.seam_defects}. THE INDEPENDENT "
          f"CONGRUENCE ROUTE gives {facts.seam_congruence_inertias} and the "
          f"two methods agree {facts.two_methods_agree}; the E02 pivot "
          f"signature is {facts.e02_pivot_signature}. The b8-type direction is "
          f"COUPLING-FREE -- components {facts.coupling_free_components} at "
          f"{facts.coupling_free_cross_half} cross-half entries -- which is "
          f"why its Gram is identically zero")
    print(f"  THE WALL, W2: {facts.mass_sweep_inertias} at m = "
          f"{tuple(str(mass) for mass in MASS_SWEEP)}; the PURE-GEOMETRY LIMIT "
          f"is {facts.geometry_limit_inertia} at defect "
          f"{facts.geometry_limit_defect}. BALANCED EVEN IN THE LIMIT. THE "
          f"SWEEP WAS RUN BEFORE THE LABEL")
    print(f"  THE WALL, W3: {facts.odd_coefficient_count} nonzero odd-power "
          f"charpoly coefficients at powers {facts.odd_coefficient_powers} "
          f"with signs {facts.odd_coefficient_signs} (even at "
          f"{facts.even_coefficient_powers}); the kernel is "
          f"{facts.kernel_dimension}-dimensional; "
          f"gcd(charpoly(x), charpoly(-x)) is exactly x^4 "
          f"{facts.spectral_gcd_is_lambda_fourth}, so NO nonzero eigenvalue is "
          f"paired with its negative and THE ANTI-COMMUTANT HAS DIMENSION "
          f"EXACTLY {facts.anticommutant_dimension}, EVERY MEMBER "
          f"KERNEL-SUPPORTED AND NONE INVERTIBLE. The diagonal candidates give "
          f"commutators {facts.candidate_commutators} and anticommutators "
          f"{facts.candidate_anticommutators} -- NEITHER "
          f"{facts.candidates_neither_commute_nor_anticommute}. THE MECHANISM "
          f"IS EXCLUDED AND THE CAUSE IS OPEN")
    print(f"  THE ESCAPE ROUTES, ALL NEGATIVE "
          f"{facts.escape_routes_all_negative}: the TRACE is strictly positive "
          f"at every mass {facts.traces_all_positive}; K IS REAL "
          f"{facts.gram_is_real} so the ANTILINEAR condition collapses to the "
          f"excluded linear one, with residuals "
          f"{facts.antilinear_residual_entries} at ranks "
          f"{facts.antilinear_residual_ranks}; and the GAMMA0 two-sided "
          f"dressing is a CONGRUENCE {facts.gamma0_is_congruence} at inertia "
          f"{facts.gamma0_inertia}, rank {facts.gamma0_rank} and defect "
          f"{facts.gamma0_defect} -- SYLVESTER FORCED IT, so it was never an "
          f"independent candidate, which is the supervisor's variant-design "
          f"error and the checker's catch. NO TESTED VARIANT IS POSITIVE "
          f"DEFINITE {facts.no_tested_variant_is_definite}. The verdicts are "
          f"{tuple(sorted(ESCAPE_ROUTE_VERDICTS))} and the findings are "
          f"preserved at {CHECK_FINDINGS}")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False the note has NOT landed at docs/ yet, there is no draft "
          f"fallback anywhere in this runner, gate H is EXPECTED to fail and "
          f"the gate-H mutation is UNTESTABLE until the note lands. Scope keys "
          f"satisfied: {sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  EXACTNESS: every measured scalar is an exact sympy Rational or "
          f"Integer and NOT ONE IS A FLOAT ({facts.exactness_holds}); no "
          f"tolerance enters any check; THE INERTIA IS MEASURED TWICE BY "
          f"DISJOINT EXACT METHODS -- charpoly plus Descartes, which is exact "
          f"and not a bound because a Hermitian matrix has only real "
          f"eigenvalues, and symmetric congruence elimination, which touches no "
          f"polynomial at all; and sp.nsimplify IS APPLIED TO NOTHING, because "
          f"it carries a rational tolerance that maps a small nonzero rational "
          f"to EXACTLY ZERO and would silently move a measured inertia. "
          f"ELAPSED {elapsed_ns // 1_000_000} ms")
    print(f"  THE CORPUS RELATION: Blocks 104, 105, 106, 107, 128 and 181-185 "
          f"STAND EXACTLY AS LANDED and no landed note is edited. BLOCK 185'S "
          f"LANDED POSITIVITY IS UNTOUCHED: it lives on the BLOCK 107 CARRIER, "
          f"a DIFFERENT carrier, and this block characterizes why the section "
          f"frame's FIRST pairing family does not reproduce it -- COMPLEMENTARY "
          f"AND NOT CONTRADICTORY. ONE CORRECTION IS LANDED AND IT IS THIS "
          f"BLOCK'S OWN: the inter-cell census, gated above at 144/72/48/96. "
          f"THREE IN-SOLVE CATCHES are recorded as PROCESS in N7: the vacuous "
          f"antiperiodic edge negation, the negative-half image built without "
          f"the within-block xpar flip which failed covariance at 144 entries, "
          f"and the symbolic-assumptions 'not real' reading -- the third is "
          f"GATED above at the exact reality of Q_g. AND ONE VARIANT-DESIGN "
          f"ERROR IS DISCLOSED AS A GATE: the Gamma0 two-sided dressing is a "
          f"CONGRUENCE and was never an independent escape candidate")
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--list-mutations", action="store_true",
        help="print the declared mutation names, one per line, and exit")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No family can cascade into another
    # because no gate feeds a measurement.
    facts = measure()
    elapsed_ns = time.monotonic_ns() - started_ns

    checks = build_checks(facts, build_claims(""))
    if mutation:
        raw = checks.families()
        checks = build_checks(facts, build_claims(mutation))
        mutated = checks.families()
        target = MUTATION_GATE[mutation]
        changed = {family for family in raw if raw[family] != mutated[family]}
        if changed - {target} or mutated[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    report_measured(facts, elapsed_ns)
    checks.report()
    print(N5_FENCE)
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
