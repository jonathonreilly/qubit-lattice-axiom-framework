#!/usr/bin/env python3
"""BLOCK 189 -- THE SHIFT FAMILY, ITS EXACT STABILIZER, AND THE INVARIANT SECTOR.

THE RESULT, AND ITS EXACT SCOPE.  On BLOCK 188's OWN site-glued action Q_s --
Block 107's d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32,
at the fixture (m, c) = (9/20, 5/13) -- THE PER-SLICE SPATIAL SHIFT FAMILY IS
CLASSIFIED EXACTLY, ITS EXACT STABILIZER IS COMPUTED BY EXHAUSTIVE SWEEP, AND
THE INVARIANT SECTOR OF THE CORE PAIRING IS BUILT AND MEASURED POSITIVE
DEFINITE.  ALL OF IT IS FINITE SYMMETRY ALGEBRA.  NONE OF IT IS GRAVITY, AND
THE WORDS GAUGE, QUOTIENT AND LAPSE ARE FENCED AS INTERPRETATIONS THROUGHOUT.

  0. THE CONTROL COMES FIRST AND IT IS BLOCK 188'S OWN NUMBER (C).  The site
     route rebuilt here reproduces their landed core Gram digit-for-digit: the
     first leading minor
     250811603701251182926764176363850176714557920003089965221914456500 over
     666495028860293624372300921944800123265476111209829299156533225479 and the
     second one too, with rank(Q_s) = 32, the core Gram symmetric at zero
     residual, the reflected-transpose covariance Ps Q_s Ps = Q_s^T at zero and
     the plain symmetry defect at EXACTLY 144.  NOTHING BELOW IS ABOUT THEIR
     OBJECT IF THIS IS NOT EXACT.

  1. THE GRADING SELECTS THE EVEN SHIFTS, AND IT IS A MEASUREMENT AND NOT A
     PREFERENCE (C).  The odd per-slice shift U_x: e_(t,x) -> e_(t,x+1) does NOT
     commute with the grade-raising part: [U_x, d_K] has EXACTLY 64 nonzero
     entries, EXACT RANK 16, and its ordered time-pair support is the eight
     DIAGONAL pairs (0,0)...(7,7) -- ENTIRELY INTRA-SLICE.  The mechanism is
     measured one level down: the grade projectors themselves fail to commute
     with U_x, at 16, 32 and 16 entries for grades 0, 1 and 2, because the
     staggered eta_x = (-1)^t makes the degree of a site depend on x parity.
     The odd shift is therefore not a symmetry of the action either:
     [U_x, Q_s] has 64 nonzero entries at EXACT RANK 8.  THE GLOBAL EVEN SHIFT
     IS AN EXACT SYMMETRY: [V_glob, Q_s] = 0, V_glob Q_s V_glob^T - Q_s = 0, and
     V_glob commutes with d_K, with H_s, with D_s and with Ps, ALL AT ZERO.  AND
     THE SPLIT IS LOCATED: U_x commutes with H_s at ZERO and fails on D_s at 48,
     so the obstruction lives in the GLUE and not in the Hodge.

  2. THE SINGLE-SLICE TWISTS LOCALIZE, AND THE RANGE IS TWO AND NOT ONE (D).
     None of the eight single-slice even twists V_t is an exact symmetry: every
     defect V_t Q_s V_t^T - Q_s has EXACT RANK 4, with the exact census
     {0: 96, 1: 64, 2: 80, 3: 64, 4: 64, 5: 64, 6: 80, 7: 64}.  EVERY supported
     ordered time-pair CONTAINS the twisted slice t -- that is the localization,
     and it is exact.  BUT THE SUPPORT IS NOT NEAREST-BOND, AND THIS IS THE
     ADVERSARIAL CHECK'S CORRECTION CARRIED AS CONTENT: at t = 0, 2 and 6 the
     support contains SEPARATION-TWO pairs -- (0,2), (0,6) -- so the exact
     temporal RANGE of the defect is 2 at those three slices and 1 at the other
     five.  The word bond is too narrow and is not used.

  3. THE OS-COMPATIBLE SUBGROUP IS EXACTLY THE REFLECTION-EVEN ONE, AND
     COVARIANCE TRANSPORTS (E).  Of the 256 even-shift patterns, EXACTLY the 32
     reflection-even ones (xi_t = xi_(-t)) commute with Ps, and ALL 224 others
     FAIL to -- an exact iff on a finite sweep, not a sample.  For every one of
     the 32 the twisted action transports the covariance:
     Ps (V Q_s V^T) Ps = (V Q_s V^T)^T at zero residual, which is the two-line
     algebra P_s(VQV^T)P_s = V(P_sQP_s)V^T = VQ^TV^T = (VQV^T)^T made
     executable.  AND THE INSTANCE IS NONTRIVIAL: V = V_1 V_7 commutes with Ps,
     its twist differs from Q_s at EXACTLY 128 entries -- so it is NOT in the
     stabilizer -- and the transport still holds exactly.  OS COMPATIBILITY IS
     STRICTLY WEAKER THAN EXACT INVARIANCE.

  4. THE CORE ACTION, AND THE ONE EXACT INVARIANCE THEOREM (F).  On the {1,2}
     core in the t-major order ((1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3))
     the two core shifts satisfy W_1^2 = W_2^2 = I_8 and W_1 W_2 = W_2 W_1
     exactly.  NEITHER IS INDIVIDUALLY AN INVARIANCE: W_1^T K W_1 - K and
     W_2^T K W_2 - K each have EXACTLY 32 nonzero entries at EXACT RANK 4.  THE
     DIAGONAL ELEMENT IS: (W_1 W_2)^T K (W_1 W_2) - K = 0_8 EXACTLY.  That is
     the block's one genuine invariance theorem on the OS pairing.

  5. THE INVARIANT SECTOR IS EXPLICIT, AND ITS POSITIVITY IS AUTOMATIC (F).  The
     projector Pi = (I + W_1)(I + W_2)/4 is exactly symmetric, exactly
     idempotent and of EXACT RANK 4; its column-space basis B is exact, with
     B^T B = I_4/2 and det(B^T B) = 1/16; and the restricted Gram B^T K B is
     exact, with four exact leading minors, all positive, determinant
     2198952681327212186709224903107443847656250000000000 over
     2836414688995746959145683979271775764957689091340617249 and
     basis-independent density det(B^T K B)/det(B^T B).  AND THE SCOPE IS STATED
     IN THE SAME BREATH AS THE RESULT, WHICH IS THE CHECK'S C6.1: THE POSITIVITY
     OF THE RESTRICTION IS AUTOMATIC.  K is positive definite and B has full
     column rank, so y^T B^T K B y = (By)^T K (By) > 0 for every nonzero y.  IT
     IS NOT A NEW DYNAMICAL THEOREM AND IT IS NOT CLAIMED AS ONE.  What is NOT
     automatic is the explicit sector: the projector's rank, the exact basis and
     the exact restricted Gram are COMPUTED.  AND THE BASIS SIGN IS A
     CONVENTION, MEASURED TO BE ONE: all sixteen sign patterns of B give the
     SAME four minors, and the adversarial check's displayed representative is
     the diag(1,-1,-1,1) conjugate, reached from this block's own core Gram by
     the STAGGERED SITE SIGN (-1)^(t+x) -- a diagonal congruence, so the two
     rebuilds are the same object in two phase conventions.

  6. THE EXACT STABILIZER, BY EXHAUSTIVE SWEEP, AND IT IS THE CHECK'S OWN
     RESULT (G).  All 2^8 = 256 even-shift patterns are swept exactly.  The
     family acts FAITHFULLY -- 256 distinct site permutations -- and the
     stabilizer of Q_s is EXACTLY {00000000, 11111111}: ORDER 2, generated by
     the uniform global even shift.  ALL 32 reflection-even patterns are in the
     sweep and only the two uniform ones stabilize; NONE of the 8 adjacent
     two-slice patterns does.  THE MORAL IS THE CHECK'S: OS COMPATIBILITY OF A
     TWIST IS MUCH WEAKER THAN MEMBERSHIP IN THE EXACT STABILIZER -- 32 against
     2.  AND IT SURVIVES A SECOND FIXTURE: at (1, 5/13) the stabilizer is again
     of order 2, W_1 W_2 is again an exact core invariance, the projector is
     again rank 4 and the restricted Gram is again positive definite -- WHICH IS
     TWO POINTS AND NOT A WINDOW.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GAUGE
IDENTIFICATION: the shift family is a CHOSEN FINITE TRANSFORMATION FAMILY, and
that its elements are redundancies of physical states is NOT DERIVED anywhere.
NO GRAVITY CONSTRAINT QUOTIENT: no lapse function, no shift vector, no
Hamiltonian constraint, no momentum/diffeomorphism constraint, no first-class
algebra, no Dirac closure and no ADM phase space is supplied by this block.  NO
LAPSE DIRECTION: no volume dial is turned here at all, and the word lapse
appears only inside the interpretation fence.  NO GENERALITY: TWO fixtures on
ONE carrier, with no bracket, no ray and no edge.  BLOCK 188 IS NOT CORRECTED:
their core Gram is reproduced digit-for-digit and their positivity stands
exactly as landed.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 188 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the seven audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: the imposed objects,
     ZERO registered and ZERO adopted, with the gauge identification, the
     constraint quotient, the lapse direction and the generality all declared
     NOT CLAIMED as measured constants.
  C  THE CONTROL AND THE GRADING SELECTION: Block 188's own core minors
     digit-for-digit, the rank, the covariance and the asymmetry; the odd
     shift's exact intra-slice commutator with d_K and the grade projectors that
     explain it; the odd shift's rank-8 failure on Q_s; and the global even
     shift exact against d_K, H_s, D_s, Q_s and Ps.
  D  THE TWIST TABLE AND THE RANGE-TWO CORRECTION: eight exact defects, eight
     exact ranks, the exact nonzero census, the exact ordered supports, the
     exact locality statement (every pair contains t) AND the exact range vector
     (2 at t = 0, 2, 6 and 1 elsewhere), which is the check's wording
     correction carried as a measured number.
  E  THE OS-COMPATIBLE SUBGROUP: the reflection-even criterion measured as an
     EXACT IFF over all 256 patterns, the covariance transport verified for all
     32, and the V_1 V_7 instance that transports while differing from Q_s at
     128 entries.
  F  THE CORE ACTION AND THE INVARIANT SECTOR: the involutions, the commuting,
     the two individual failures at 32 and rank 4, the exact zero diagonal
     defect, the projector's symmetry, idempotence and rank, the exact basis and
     its Gram, the exact restricted Gram with its four exact minors and exact
     inertia, the automatic-positivity disclosure gated as a constant, and the
     basis-sign convention measured to be one.
  G  THE EXACT STABILIZER AND THE SECOND FIXTURE: the faithful 256-element
     family, the exhaustive sweep, the order-2 stabilizer with its two exact
     patterns, the 32-against-2 reflection-even count, the zero adjacent
     stabilizers, and the second fixture rebuilt whole.
  H  the note at its final path, the N5 fence byte-identical, and the nsimplify
     count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: twenty-nine declared mutations, each of which rewrites
  ONE CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_gauge_identification,
       claim_constraint_quotient, claim_lapse_direction, claim_generality
    C  break_control_minor, break_odd_shift_grading, break_grade_projectors,
       break_global_even_symmetry
    D  break_twist_census, break_twist_range_two, break_twist_locality
    E  break_reflection_even_criterion, break_os_transport,
       break_twist_nontrivial
    F  break_diagonal_invariance, break_singleton_invariance,
       break_projector_rank, break_quotient_positivity,
       break_basis_sign_invariance, break_automatic_disclosure
    G  break_stabilizer_order, break_stabilizer_reflection_even,
       break_stabilizer_adjacent, break_robustness
    H  drop_n5_fence, break_nsimplify_absence
  FOUR OF THE TWENTY-NINE GUARD THE CHECK'S OWN CORRECTIONS:
  break_twist_range_two asserts the nearest-bond wording the check refused;
  break_stabilizer_order asserts an order the exhaustive sweep forbids;
  break_automatic_disclosure asserts the restriction positivity is NOT
  automatic, which is exactly the overread the check named; and
  claim_gauge_identification asserts the identification the check ruled a
  reading.  ALL FOUR MUST FAIL.
  BEFORE LANDING GATE H ALREADY FAILS AT BASELINE, on note-at-final-path alone,
  so drop_n5_fence cannot flip it and THE SWEEP IS RUN AT LANDING, once the note
  sits at docs/ and the baseline is 8 of 8 by family.

RUNNING
  python3 scripts/admissibility_dirac_kahler_site_gauge_quotient_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation break_stabilizer_order

NOTES FOR THE LANDING AGENT
  1. NOTHING from any scratchpad is imported OR READ.  THE SITE CONSTRUCTION IS
     BUILT DIRECTLY HERE from Block 188's landed note and runner: the staggered
     kernel with its antiperiodic edge sign, the grade projectors, the raising
     part d_K, the site reflection, the offset permutation P_4, the site raising
     set A_s, the derived glue D_s and the glued action Q_s.  The LANDED Block
     128 runner is imported for EXACTLY TWO objects -- cover_embedding() and the
     Block 105 module's shear_hodge() -- and for nothing else.  Gate C's first
     check is the proof that the rebuild IS Block 188's object.
  2. EVERY CHECK IS EXACT.  sympy Rational and Integer only; no float enters any
     measured object and no tolerance is used anywhere.  Ranks, inverses and
     determinants go through sympy's DomainMatrix over the EXACT RATIONAL FIELD
     QQ, which is exact arithmetic and not a numerical method: it is used
     because the dense sympy fallbacks are slow on a 32x32 rational matrix, and
     it changes NO value.  Signatures are decided by exact leading principal
     minors and by an EXACT CONGRUENCE chain, never by an eigenvalue estimate.
  3. THE b186 nsimplify HAZARD CARRIES OVER AND THIS RUNNER NSIMPLIFIES NOTHING.
     That call carries a rational TOLERANCE and maps a small nonzero rational to
     EXACTLY ZERO, so a coefficient passed through it can silently lose its
     sign -- and this block is nothing but zeros, ranks and signs.  Every mass
     and shear here is ALREADY an exact sympy Rational, so nothing needs
     converting and NOTHING IS CONVERTED.  The absence is MEASURED, not
     promised: gate H counts the occurrences of the call in this file's own
     source and requires zero.
  4. The N5 fence appears byte-identically in the note; gate H checks it as a
     raw substring.
  5. PARENT_COMMIT is the Block 188 tip and PARENT_REF resolves to it; nothing
     needs sed, and CURRENT_MAIN was carried forward from the Block 188 runner
     and re-resolved at draft time.
  6. The stale pin is the Block 187 tip, a real ancestor of HEAD that predates
     Block 188 and carries NEITHER Block 188 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  7. THE ADVERSARIAL CHECK LANDED BEFORE THIS RUNNER WAS FINISHED, verdict
     CONFIRMED-WITH-CORRECTION, AND ITS VERDICTS ARE FOLDED RATHER THAN
     APPENDED.  NO SENTINEL REMAINS ANYWHERE IN THIS FILE.  It CONFIRMED every
     algebraic claim on an independent reconstruction; it SUPPLIED the exact
     stabilizer by exhaustive sweep, which is now family G; it CORRECTED the
     twist-support wording from nearest-bond to temporal range two, which is now
     a measured range vector in family D; and it INSISTED that the gauge, the
     quotient and the lapse identifications are INTERPRETATIONS -- which is why
     they are declared constants in family B, why the note carries a required
     interpretations fence, and why the automatic-positivity disclosure is
     itself a gate.
  8. Re-run at landing; gate H should then pass, the battery should be 8/8 by
     family, and the twenty-nine-mutation sweep should be run then.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORT, LANDED, AND DELIBERATELY THIN -- the same two objects
# Blocks 185, 187 and 188 imported and no others: cover_embedding(), whose
# corner order IS the form basis (1, dx, dt, dx^dt), and the Block 105 module it
# re-exports, from which shear_hodge() is read.  Everything else is built here.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_SITE_GAUGE_QUOTIENT_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 188 is the commit this block's branch
# is cut from, and its note and its runner are the pair that distinguishes the
# parent pin from the stale pin: both exist at PARENT_COMMIT and NEITHER exists
# at STALE_PARENT_COMMIT.  Block 188 is ALSO the construction authority: Q_s is
# their object, rebuilt here from their displayed equations.
BLOCK188_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK188_RUNNER = (
    "scripts/admissibility_dirac_kahler_site_os_positivity_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK188_NOTE, BLOCK188_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "84d3e97db95982860000a233af9513303c0497a6",   # Block 188 note
    "34f2c48545b99a9b401c654a262efab6548ec468",   # Block 188 runner
)
# THE LADDER AUTHORITY: Block 107's note, whose section-10 step 3 is the thing
# this block does NOT execute and whose sentence is pinned for that reason.
BLOCK107_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_"
    "THEOREM_NOTE_2026-08-15.md"
)
# THE DOWNSTREAM-QUOTIENT SENTENCE, read from Block 187's primary body.
BLOCK187_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
# THE CARRIER PARENT, imported for exactly two objects and read as an input.
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time -- this block's own note excepted,
# since it lands later and gate H is the gate that owns it.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_GAUGE_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_site_os_positivity_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
# THE BLOCK'S OWN NOTE is the one audit input gate A does NOT require readable,
# because it does not exist until landing and gate H is the gate that owns it.
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 188 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 188 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block188-"
              "site-os-positivity-20260824")
PARENT_COMMIT = "094200a75208b6c8d153c1b91df32a3913729ed0"
# The Block 187 tip: a real ancestor of HEAD that predates Block 188 and
# therefore carries NEITHER Block 188 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "22bc4f5406d1aff3b16d120d1e0a1951faf8b2b2"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gauge_identification",
    "claim_constraint_quotient",
    "claim_lapse_direction",
    "claim_generality",
    "break_control_minor",
    "break_odd_shift_grading",
    "break_grade_projectors",
    "break_global_even_symmetry",
    "break_twist_census",
    "break_twist_range_two",
    "break_twist_locality",
    "break_reflection_even_criterion",
    "break_os_transport",
    "break_twist_nontrivial",
    "break_diagonal_invariance",
    "break_singleton_invariance",
    "break_projector_rank",
    "break_quotient_positivity",
    "break_basis_sign_invariance",
    "break_automatic_disclosure",
    "break_stabilizer_order",
    "break_stabilizer_reflection_even",
    "break_stabilizer_adjacent",
    "break_robustness",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gauge_identification": "B",
    "claim_constraint_quotient": "B",
    "claim_lapse_direction": "B",
    "claim_generality": "B",
    "break_control_minor": "C",
    "break_odd_shift_grading": "C",
    "break_grade_projectors": "C",
    "break_global_even_symmetry": "C",
    "break_twist_census": "D",
    "break_twist_range_two": "D",
    "break_twist_locality": "D",
    "break_reflection_even_criterion": "E",
    "break_os_transport": "E",
    "break_twist_nontrivial": "E",
    "break_diagonal_invariance": "F",
    "break_singleton_invariance": "F",
    "break_projector_rank": "F",
    "break_quotient_positivity": "F",
    "break_basis_sign_invariance": "F",
    "break_automatic_disclosure": "F",
    "break_stabilizer_order": "G",
    "break_stabilizer_reflection_even": "G",
    "break_stabilizer_adjacent": "G",
    "break_robustness": "G",
    "drop_n5_fence": "H",
    "break_nsimplify_absence": "H",
}
# EVERY FAMILY CARRIES AT LEAST ONE MUTATION, INCLUDING G AND H.  Family G is
# the adversarial check's own leg -- the exhaustive stabilizer sweep -- and it
# carries four mutations of its own rather than being carried as prose.
MUTATED_FAMILIES = "ABCDEFGH"


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
        # THE STALE LEG.  At the Block 187 tip NEITHER Block 188 artifact
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
    "BLOCK 188's SITE-GLUED ACTION Q_s, REBUILT HERE from their landed note and runner rather than imported: Block 107's d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32 with eta_t = 1 and eta_x = (-1)^t, the antiperiodic kernel carrying the far-seam edge sign omega_-(3) = -1, the grade-raising part d_K, the SITE reflection theta_s(t) = -t with the fixed slices {0,4} and the anchor pairing thA_s(t) = -1-t, the site-adapted glued Hodge with the physical anchors {0..3} at the UNIFORM step c = 5/13 and the image anchors {4..7} the UNFLIPPED P_4-images of their thA_s partners, the site raising set A_s of the d_K entries in the CLOSED half {0..4} EXCLUDING the fixed-slice spatial edges, the derived glue D_s = A_s - Ps A_s Ps and the completion Q_s = m*H_s + H_s*D_s - D_s^T*H_s",
    "THE PER-SLICE SPATIAL SHIFT FAMILY U(xi): e_(t,x) -> e_(t, x + xi_t), WHICH IS THIS BLOCK'S OWN CHOSEN FINITE TRANSFORMATION FAMILY AND NOT A DERIVED REDUNDANCY -- the ODD member U_x at xi = (1,1,1,1,1,1,1,1), the EVEN subfamily at xi_t in {0,2} which is a faithful (Z_2)^8 of order 256, the single-slice even twists V_t, the global even shift V_glob and the composites V_a V_b",
    "THE CORE SHIFTS W_1 and W_2 on the {1,2}-core Gram K in the t-major order ((1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)), THE INVARIANT PROJECTOR Pi = (I + W_1)(I + W_2)/4, ITS EXACT COLUMN-SPACE BASIS B AND THE RESTRICTED GRAM B^T K B",
    "THE TWO FIXTURES (9/20, 5/13) and (1, 5/13) at unit volume -- the first is BLOCK 188's and BLOCK 107's and the second is BLOCK 188's own robustness point -- AND TWO POINTS ARE NOT A WINDOW: no bracket, no ray, no edge and no interior is established for anything in this block",
    "Block 128's LANDED cover_embedding(), whose corner order IS the form basis (1, dx, dt, dx^dt), and the LANDED Block 105 shear_hodge() block it re-exports: THE ONLY TWO OBJECTS IMPORTED BY THIS RUNNER",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS rather than prose, so
# the B mutations bite on an object.  ALL FOUR ARE FALSE AND STAY FALSE, AND
# THE FIRST THREE ARE THE ADVERSARIAL CHECK'S C6 BOUNDARY MADE EXECUTABLE.
GAUGE_IDENTIFICATION_CLAIMED = False
CONSTRAINT_QUOTIENT_CLAIMED = False
LAPSE_DIRECTION_CLAIMED = False
GENERALITY_CLAIMED = False
# AND THE FIFTH DECLARED CONSTANT IS A DISCLOSURE RATHER THAN A DENIAL: the
# positivity of the restricted Gram follows from K > 0 and full column rank
# alone, so it is NOT a new dynamical theorem.  Family F gates it as a claim so
# that break_automatic_disclosure has something to deny.
RESTRICTION_POSITIVITY_IS_AUTOMATIC = True
# THE LIST OF GRAVITY STRUCTURES THIS BLOCK DOES NOT SUPPLY, ENUMERATED SO THAT
# THE ABSENCE IS A COUNT AND NOT A MOOD.
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function",
    "shift vector",
    "Hamiltonian constraint",
    "momentum/diffeomorphism constraint",
    "first-class constraint algebra",
    "Dirac closure",
    "ADM phase space / history transporter",
    "proof that the selected transformations are redundancies of physical states",
)

# THE ADVERSARIAL CHECK LANDED BEFORE THIS RUNNER WAS FINISHED, verdict
# CONFIRMED-WITH-CORRECTION, and every slot that was a placeholder in draft is
# now a MEASURED GATE.  Nothing in this file is a sentinel.
CHECK_VERDICT = "CONFIRMED-WITH-CORRECTION"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
TIME_EXTENT = 8
SPACE_EXTENT = 4
COVER_SIZE = TIME_EXTENT * SPACE_EXTENT
FIXTURE_MASS = sp.Rational(9, 20)
FIXTURE_SHEAR = sp.Rational(5, 13)
UNIT_VOLUME = sp.Integer(1)

# --- C: THE CONTROL, WHICH IS BLOCK 188'S OWN OBJECT ------------------------
ACTION_RANK = 32
SITE_ASYMMETRY = 144
B188_CORE_MINOR_1 = sp.Rational(
    250811603701251182926764176363850176714557920003089965221914456500,
    666495028860293624372300921944800123265476111209829299156533225479)
B188_CORE_MINOR_2 = sp.Rational(
    9699265179160355495171233606378759680576921193642386633764164130236400111062250000,
    65542091681979044701359795584266761562795513633598145522262137753727157320281821073)
CORE_SIGNS = (1,) * 8
CORE_INERTIA = (8, 0, 0)

# --- C: THE GRADING SELECTION -----------------------------------------------
# THE ODD SHIFT xi = (1,...,1), which is the discrete spatial diffeomorphism the
# construction would have wanted and which the STAGGERING FORBIDS.
ODD_SHIFT = (1,) * TIME_EXTENT
EVEN_SHIFT = (2,) * TIME_EXTENT
ODD_DK_NONZEROS = 64
ODD_DK_RANK = 16
# THE SUPPORT IS THE EIGHT DIAGONAL TIME-PAIRS: the obstruction is INTRA-SLICE
# and does not propagate along the time direction at all.
ODD_DK_SUPPORT = tuple((t, t) for t in range(TIME_EXTENT))
ODD_ACTION_NONZEROS = 64
ODD_ACTION_RANK = 8
ODD_CONJUGATION_NONZEROS = 64
# THE MECHANISM, ONE LEVEL DOWN: the grade projectors themselves do not commute
# with the odd shift, because eta_x = (-1)^t makes the DEGREE of a site depend
# on x parity.  This is the exact reason the odd shift breaks the grading.
GRADE_PROJECTOR_DEFECTS = (16, 32, 16)
# THE ODD SHIFT SPLIT: it commutes with the Hodge and fails on the GLUE.
ODD_HODGE_NONZEROS = 0
ODD_GLUE_NONZEROS = 48
# THE GLOBAL EVEN SHIFT: exact against every object in the construction.
GLOBAL_EVEN_RESIDUALS = {
    "d_K": 0, "H_s": 0, "D_s": 0, "Q_s": 0, "Ps": 0, "conjugation": 0}

# --- D: THE SINGLE-SLICE TWIST TABLE ----------------------------------------
# EXACT NONZERO CENSUS of V_t Q_s V_t^T - Q_s, slice by slice.
TWIST_NONZEROS = (96, 64, 80, 64, 64, 64, 80, 64)
TWIST_RANKS = (4,) * TIME_EXTENT
# THE EXACT ORDERED TIME-PAIR SUPPORTS.  EVERY pair contains the twisted slice.
TWIST_SUPPORTS = (
    ((0, 1), (0, 2), (0, 6), (0, 7), (1, 0), (2, 0), (6, 0), (7, 0)),
    ((0, 1), (1, 0), (1, 2), (2, 1)),
    ((0, 2), (1, 2), (2, 0), (2, 1), (2, 3), (3, 2)),
    ((2, 3), (3, 2), (3, 4), (4, 3)),
    ((3, 4), (4, 3), (4, 5), (5, 4)),
    ((4, 5), (5, 4), (5, 6), (6, 5)),
    ((0, 6), (5, 6), (6, 0), (6, 5), (6, 7), (7, 6)),
    ((0, 7), (6, 7), (7, 0), (7, 6)),
)
# THE ADVERSARIAL CHECK'S WORDING CORRECTION, CARRIED AS A MEASURED NUMBER.  The
# solve said the twists localize on their touching TEMPORAL BONDS.  If bond
# means an ELEMENTARY NEAREST-SLICE bond that is too narrow: at t = 0, 2 and 6
# the support contains SEPARATION-TWO pairs, because the Hodge multiplication in
# the completion extends the support to temporal RANGE TWO.  The exact circular
# range max over the support is measured slice by slice and is this vector.
TWIST_RANGES = (2, 1, 2, 1, 1, 1, 2, 1)
TWIST_LOCALITY = (True,) * TIME_EXTENT      # every supported pair contains t

# --- E: THE OS-COMPATIBLE SUBGROUP ------------------------------------------
EVEN_PATTERN_COUNT = 256
REFLECTION_EVEN_COUNT = 32
NON_REFLECTION_EVEN_COUNT = EVEN_PATTERN_COUNT - REFLECTION_EVEN_COUNT
# THE EXACT IFF, over the WHOLE 256-element family: reflection-even <=> commutes
# with Ps.  Both halves are counted, so neither direction is a sample.
REFLECTION_EVEN_COMMUTING = REFLECTION_EVEN_COUNT
NON_REFLECTION_EVEN_FAILING = NON_REFLECTION_EVEN_COUNT
REFLECTION_EVEN_TRANSPORTING = REFLECTION_EVEN_COUNT
# THE NONTRIVIAL INSTANCE: V_1 V_7 commutes with Ps and transports covariance
# EXACTLY, while its twist differs from Q_s at 128 entries -- so it is NOT in
# the stabilizer, and OS compatibility is strictly weaker than invariance.
TRANSPORT_INSTANCE = (1, 7)
TRANSPORT_INSTANCE_DIFFERENCE = 128

# --- F: THE CORE ACTION AND THE INVARIANT SECTOR ----------------------------
CORE_SLICES = (1, 2)
CORE_ORDER = tuple((t, x) for t in CORE_SLICES for x in range(SPACE_EXTENT))
CORE_SIZE = len(CORE_ORDER)
SINGLETON_DEFECT_NONZEROS = (32, 32)
SINGLETON_DEFECT_RANKS = (4, 4)
DIAGONAL_DEFECT_NONZEROS = 0
PROJECTOR_RANK = 4
# THE EXACT COLUMN-SPACE BASIS, in the t-major core order.  Each basis vector
# is the HALF-SUM of an x-orbit of the core shift on one slice.
QUOTIENT_BASIS = (
    (sp.Rational(1, 2), 0, sp.Rational(1, 2), 0, 0, 0, 0, 0),
    (0, sp.Rational(1, 2), 0, sp.Rational(1, 2), 0, 0, 0, 0),
    (0, 0, 0, 0, sp.Rational(1, 2), 0, sp.Rational(1, 2), 0),
    (0, 0, 0, 0, 0, sp.Rational(1, 2), 0, sp.Rational(1, 2)),
)
BASIS_GRAM = sp.eye(4) / 2
BASIS_GRAM_DETERMINANT = sp.Rational(1, 16)
# THE EXACT RESTRICTED GRAM B^T K B, entrywise, in THIS block's own phase
# convention.  The adversarial check's displayed representative is the
# diag(1,-1,-1,1) conjugate of it; see BASIS_SIGN below.
QUOTIENT_GRAM = (
    (sp.Rational(21963305608532250, 98338455418123687),
     sp.Rational(1668901104000, 24167720672923),
     sp.Rational(6968252744640000, 98338455418123687),
     sp.Rational(943847791250, 24167720672923)),
    (sp.Rational(1668901104000, 24167720672923),
     sp.Rational(21963305608532250, 98338455418123687),
     sp.Rational(943847791250, 24167720672923),
     sp.Rational(6968252744640000, 98338455418123687)),
    (sp.Rational(6968252744640000, 98338455418123687),
     sp.Rational(943847791250, 24167720672923),
     sp.Rational(15357851117106250, 98338455418123687),
     sp.Integer(0)),
    (sp.Rational(943847791250, 24167720672923),
     sp.Rational(6968252744640000, 98338455418123687),
     sp.Integer(0),
     sp.Rational(15357851117106250, 98338455418123687)),
)
QUOTIENT_MINORS = (
    sp.Rational(21963305608532250, 98338455418123687),
    sp.Rational(436272390996572018995584314062500,
                9670451814022299931794587630473969),
    sp.Rational(988031356039629755460576499986328125000000,
                165618270654292302550203905627153987721012841),
    sp.Rational(2198952681327212186709224903107443847656250000000000,
                2836414688995746959145683979271775764957689091340617249),
)
QUOTIENT_SIGNS = (1, 1, 1, 1)
QUOTIENT_INERTIA = (4, 0, 0)
QUOTIENT_DENSITY = sp.Rational(
    35183242901235394987347598449719101562500000000000000,
    2836414688995746959145683979271775764957689091340617249)
# THE BASIS-SIGN CONVENTION, MEASURED TO BE ONE.  All 2^4 = 16 sign patterns of
# B give the SAME four leading minors, because a diag(+/-1) congruence scales
# each leading minor by a square.  The check's displayed matrix is the
# diag(1,-1,-1,1) representative, and it is reached from THIS block's core Gram
# by the STAGGERED SITE SIGN (-1)^(t+x) -- itself a diagonal congruence, which
# is why the two independent rebuilds share every minor and every inertia.
BASIS_SIGN_PATTERN_COUNT = 16
CHECK_BASIS_SIGN = (1, -1, -1, 1)
STAGGERED_SITE_SIGN = tuple((-1) ** (t + x) for t, x in CORE_ORDER)
# THE ADVERSARIAL CHECK'S OWN DISPLAYED MATRIX, TRANSCRIBED FROM ITS FINDINGS SO
# THAT THE RECONCILIATION IS A GATE AND NOT A REMARK.  It is EXACTLY the
# diag(1,-1,-1,1) conjugate of QUOTIENT_GRAM above, and reaching it from this
# block's core Gram takes the staggered site sign and nothing else.
CHECK_QUOTIENT_GRAM = (
    (sp.Rational(21963305608532250, 98338455418123687),
     sp.Rational(-1668901104000, 24167720672923),
     sp.Rational(-6968252744640000, 98338455418123687),
     sp.Rational(943847791250, 24167720672923)),
    (sp.Rational(-1668901104000, 24167720672923),
     sp.Rational(21963305608532250, 98338455418123687),
     sp.Rational(943847791250, 24167720672923),
     sp.Rational(-6968252744640000, 98338455418123687)),
    (sp.Rational(-6968252744640000, 98338455418123687),
     sp.Rational(943847791250, 24167720672923),
     sp.Rational(15357851117106250, 98338455418123687),
     sp.Integer(0)),
    (sp.Rational(943847791250, 24167720672923),
     sp.Rational(-6968252744640000, 98338455418123687),
     sp.Integer(0),
     sp.Rational(15357851117106250, 98338455418123687)),
)

# --- G: THE EXACT STABILIZER AND THE SECOND FIXTURE -------------------------
# THE EXHAUSTIVE SWEEP.  Patterns are written xi_0 xi_1 ... xi_7 with 1 meaning
# the +2 shift is applied on that slice.
STABILIZER_PATTERNS = ("00000000", "11111111")
STABILIZER_ORDER = 2
GROUP_ORDER = 256
REFLECTION_EVEN_STABILIZERS = 2
ADJACENT_PATTERN_COUNT = 8
ADJACENT_STABILIZERS = 0
ROBUSTNESS_POINT = (sp.Integer(1), sp.Rational(5, 13))
ROBUSTNESS_CORE_MINOR_1 = sp.Rational(
    55795661638694573774002196454830133285353706,
    478085441610996097228041845484841835649475045)
ROBUSTNESS_QUOTIENT_MINORS = (
    sp.Rational(1073507296788, 17191165688833),
    sp.Rational(840424992635542804441344, 295536177740908995380901889),
    sp.Rational(495303857775473953823625609216,
                13398201477813522937389110887955137),
    sp.Rational(284977712258371116586448359495041024,
                607410585777620392917379753768283029441921),
)

# THE CITATION PINS, read from the PRIMARY BODIES so that the ladder step this
# block does NOT execute, the firewall it inherits and the parent it rebuilds
# all have a measured referent rather than a paraphrase.
B107_STEP_THREE_PIN = ("only then form and test the physical gravity constraint "
                       "quotient")
B107_NOT_A_NOGO_PIN = "This is not a curved OS no-go."
B187_QUOTIENT_PIN = ("AND THE CONSTRAINT QUOTIENT STAYS DOWNSTREAM OF ALL "
                     "FIVE, in flight on its own thread and untouched by "
                     "anything in this note.")
B188_PREREQUISITE_PIN = "NOT EXECUTED, AND NOW WELL-POSED FOR THE FIRST TIME."
B188_NO_QUOTIENT_PIN = "NO GRAVITY CONSTRAINT QUOTIENT IS FORMED."

# THE H-FAMILY SCOPE KEYS.  The set is required WHOLE by gate H, which is what
# gives drop_n5_fence its teeth.
SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO, so a residual or a minor passed through it can silently lose its
# sign -- and this block is nothing but zeros, ranks and signs.  Here every mass
# and shear is ALREADY an exact sympy Rational, so nothing needs converting and
# nothing is converted.  Gate H counts the occurrences in this file's own source
# and requires ZERO.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def rational_matrix(matrix: sp.MatrixBase) -> DomainMatrix:
    """THE EXACT RATIONAL DOMAIN, AND IT IS NOT A NUMERICAL METHOD.  Every entry
    of every matrix in this runner is a sympy Rational, so the matrix lies in
    QQ^(n x n) exactly; DomainMatrix carries out rank, inverse and determinant
    by exact fraction-free arithmetic over that field.  No float is created at
    any point and no tolerance exists to be tuned.  It is used in place of the
    dense sympy fallbacks purely because those are slow at dimension 32, and it
    changes NO value."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ)


def exact_rank(matrix: sp.MatrixBase) -> int:
    return rational_matrix(matrix).rank()


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return rational_matrix(matrix).inv().to_Matrix()


def exact_determinant(matrix: sp.MatrixBase) -> object:
    """THE EXACT DETERMINANT, RETURNED AS A SYMPY RATIONAL.  DomainMatrix hands
    back a domain element, so it is converted back through QQ.to_sympy: the
    value is unchanged and every number this runner prints or compares is a
    sympy Rational, never a foreign numeric type."""
    return QQ.to_sympy(rational_matrix(matrix).det())


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is involved
    at any point."""
    return nonzero_entries(sp.Matrix(matrix).applyfunc(sp.expand))


def time_pair_support(matrix: sp.MatrixBase) -> tuple:
    """THE EXACT ORDERED TIME-PAIR SUPPORT of a cover-sized matrix."""
    return tuple(sorted({
        (row // SPACE_EXTENT, column // SPACE_EXTENT)
        for row in range(matrix.rows) for column in range(matrix.cols)
        if matrix[row, column] != 0}))


def circular_distance(first: int, second: int) -> int:
    """THE TEMPORAL RANGE OF A PAIR on the periodic time circle Z_8."""
    return min((first - second) % TIME_EXTENT, (second - first) % TIME_EXTENT)


def support_range(support: tuple) -> int:
    """THE EXACT TEMPORAL RANGE OF A SUPPORT: 1 is a nearest-slice bond and 2 is
    the range-two coupling the adversarial check insisted the wording admit."""
    return max(circular_distance(a, b) for a, b in support) if support else 0


def leading_minors(matrix: sp.Matrix) -> tuple:
    """THE LEADING PRINCIPAL MINORS, exact determinants over QQ: no eigenvalue
    estimate, no numerical factorization and no tolerance enters the
    decision."""
    return tuple(exact_determinant(matrix[:size, :size])
                 for size in range(1, matrix.rows + 1))


def minor_signs(minors: tuple) -> tuple:
    """THE SIGN VECTOR, in {+1, 0, -1}."""
    return tuple(int(sp.sign(value)) for value in minors)


def inertia(matrix: sp.MatrixBase) -> tuple:
    """THE EXACT INERTIA (n+, n-, n0) BY CONGRUENCE, and this is the honest
    instrument that leading minors are not.  Symmetric Gaussian elimination is a
    chain of congruences A -> E^T A E, so SYLVESTER'S LAW OF INERTIA makes the
    signs of the pivots the inertia itself.  Block 188 landed this routine's
    verdict as correction #16 and it is carried here unchanged."""
    active = sp.Matrix(matrix)
    positive = negative = null = 0
    while active.rows:
        size = active.rows
        pivot = next((i for i in range(size) if active[i, i] != 0), None)
        if pivot is None:
            pair = next(((i, j) for i in range(size) for j in range(i + 1, size)
                         if active[i, j] != 0), None)
            if pair is None:
                null += size
                break
            first, second = pair
            hyperbolic = sp.eye(size)
            hyperbolic[second, first] = 1
            active = sp.expand(hyperbolic.T * active * hyperbolic)
            pivot = first
        value = active[pivot, pivot]
        if value > 0:
            positive += 1
        else:
            negative += 1
        rest = [i for i in range(size) if i != pivot]
        reduced = sp.zeros(len(rest), len(rest))
        for a, i in enumerate(rest):
            for b, j in enumerate(rest):
                reduced[a, b] = sp.expand(
                    active[i, j] - active[i, pivot] * active[pivot, j] / value)
        active = reduced
    return positive, negative, null


def is_exact_rational(value: object) -> bool:
    """EXACT means a RATIONAL with no float anywhere in it.  Unlike Block 188,
    which needed quadratic surds for its sign operator, EVERY scalar in this
    block lies in Q."""
    expression = sp.sympify(value)
    return bool(not expression.atoms(sp.Float) and expression.is_rational)


# ---------------------------------------------------------------------------
# THE CARRIER AND BLOCK 188'S SITE CONSTRUCTION, BUILT DIRECTLY
# ---------------------------------------------------------------------------
# BLOCK 107 EQUATION (15): the offset permutation, an UNSIGNED corner swap.
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])
POSITIVE_TIMES = (0, 1, 2, 3)
# THE SITE ROUTE'S TWO FIXED SLICES: theta_s(0) = 0 and theta_s(4) = 4.
FIXED_SLICES = (0, 4)
CLOSED_HALF = (0, 1, 2, 3, 4)


def site_index(time_coordinate: int, space_coordinate: int) -> int:
    """idx(t,x) = (t mod 8)*4 + (x mod 4): time first, exactly Block 107's
    ordering, and identical to the LANDED Block 128 cover_index."""
    return ((time_coordinate % TIME_EXTENT) * SPACE_EXTENT
            + space_coordinate % SPACE_EXTENT)


def staggered_kernel(antiperiodic: bool = True) -> sp.Matrix:
    """BLOCK 107 EQUATION (3), BUILT DIRECTLY.  eta_t = 1 and eta_x = (-1)^t;
    the temporal edge sign is -1 at t = 3 -- the FAR reflection seam -- and +1
    everywhere else, and every bond is antisymmetrized.  THE eta_x = (-1)^t IS
    THE WHOLE OF THIS BLOCK'S FIRST RESULT: it is what makes the site degree
    depend on x parity, and therefore what forbids the odd spatial shift."""
    kernel = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            temporal_sign = -1 if (antiperiodic and time == 3) else 1
            here = site_index(time, space)
            ahead = site_index(time + 1, space)
            kernel[here, ahead] += sp.Rational(temporal_sign, 2)
            kernel[ahead, here] -= sp.Rational(temporal_sign, 2)
            spatial_sign = (-1) ** time
            right = site_index(time, space + 1)
            kernel[here, right] += sp.Rational(spatial_sign, 2)
            kernel[right, here] -= sp.Rational(spatial_sign, 2)
    return kernel


def site_degree(time_coordinate: int, space_coordinate: int) -> int:
    return time_coordinate % 2 + space_coordinate % 2


def grade_projector(grade: int) -> sp.Matrix:
    return sp.diag(*[1 if site_degree(t, x) == grade else 0
                     for t in range(TIME_EXTENT)
                     for x in range(SPACE_EXTENT)])


def raising_part(kernel: sp.Matrix) -> sp.Matrix:
    """BLOCK 107 EQUATION (4): d_K = P1 K P0 + P2 K P1, the grade-raising part."""
    p0, p1, p2 = (grade_projector(g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def reflection_permutation(theta) -> sp.Matrix:
    """P e_(t,x) = e_(theta(t),x)."""
    matrix = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            matrix[site_index(theta(time), space),
                   site_index(time, space)] = 1
    return matrix


def site_theta(time: int) -> int:
    """BLOCK 188's SITE reflection: theta_s(t) = -t, fixing slices {0, 4}."""
    return (-time) % TIME_EXTENT


def site_anchor_theta(time: int) -> int:
    """thA_s(t) = -1-t.  Under it EVERY cell pairs and NO anchor is fixed."""
    return (-1 - time) % TIME_EXTENT


def shear_block(shear: object, volume: object) -> sp.Matrix:
    """The LANDED Block 105 shear Hodge, read through Block 128, at an EXACT
    rational shear and an EXACT rational volume.  NO nsimplify: both arguments
    are already sympy Rationals or Integers."""
    return b128.block105.shear_hodge(shear, volume)


def anchor_block(local_shear: object) -> sp.Matrix:
    if local_shear == 0:
        return sp.eye(SPACE_EXTENT)
    return shear_block(local_shear, UNIT_VOLUME)


def assemble_hodge(blocks: tuple) -> sp.Matrix:
    """BLOCK 107 EQUATION (20): the per-cell blocks pushed onto the cover
    through the LANDED Block 128 cover_embedding()."""
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            embedding = b128.cover_embedding(time, space)
            result += embedding * blocks[time] * embedding.T / 4
    return sp.expand(result)


def site_image_hodge(shear: object) -> sp.Matrix:
    """BLOCK 188's SITE-ADAPTED GLUED HODGE.  The physical anchors {0..3} carry
    the UNIFORM step block B(c); the image anchors {4..7} carry the P_4-image of
    their thA_s partner's block, UNFLIPPED.  Rebuilt here, not imported."""
    physical = anchor_block(shear)
    blocks = []
    for time in range(TIME_EXTENT):
        if time in POSITIVE_TIMES:
            blocks.append(physical)
        else:
            assert site_anchor_theta(time) in POSITIVE_TIMES
            blocks.append(sp.expand(OFFSET_PERMUTATION * physical
                                    * OFFSET_PERMUTATION.T))
    return assemble_hodge(tuple(blocks))


def site_restricted_raising(raising: sp.Matrix) -> sp.Matrix:
    """BLOCK 188's A_s: the d_K entries with BOTH endpoint times in the CLOSED
    half {0..4}, EXCLUDING the spatial edges that live INSIDE a fixed slice --
    an exclusion their block measured to be an EXACT NO-OP."""
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            if row_time not in CLOSED_HALF or column_time not in CLOSED_HALF:
                continue
            if row_time == column_time and row_time in FIXED_SLICES:
                continue
            result[row, column] = raising[row, column]
    return result


def completion(hodge: sp.Matrix, glue: sp.Matrix, mass: object) -> sp.Matrix:
    """BLOCK 107 EQUATION (21): Q = m*H + H*D - D^T*H, used UNCHANGED."""
    return sp.expand(mass * hodge + hodge * glue - glue.T * hodge)


def slice_indices(slices: tuple) -> tuple:
    return tuple(site_index(t, x) for t in slices for x in range(SPACE_EXTENT))


def reflected_indices(slices: tuple, theta) -> tuple:
    return tuple(site_index(theta(t), x)
                 for t in slices for x in range(SPACE_EXTENT))


def paired_gram(inverse: sp.Matrix, slices: tuple, theta) -> sp.Matrix:
    """BLOCK 107 EQUATION (7)/(22): K_ab = conj(G(b, theta a)).  THE INDEX ORDER
    IS t-MAJOR, which is the core order the whole of family F is written in."""
    anchors = slice_indices(slices)
    partners = reflected_indices(slices, theta)
    gram = sp.zeros(len(anchors), len(anchors))
    for row in range(len(anchors)):
        for column in range(len(anchors)):
            gram[row, column] = sp.conjugate(inverse[anchors[column],
                                                     partners[row]])
    return sp.expand(gram)


# ---------------------------------------------------------------------------
# THE SHIFT FAMILY, AS INDEX PERMUTATIONS.  A permutation is applied by index
# lookup rather than by matrix multiplication: for V with V e_j = e_pi(j),
# (V M V^T)[i,j] = M[pi^-1(i), pi^-1(j)] and (V M - M V)[i,j] = M[pi^-1(i), j] -
# M[i, pi(j)].  This is an EXACT identity, not an approximation, and it is what
# makes the exhaustive 256-pattern sweep of family G affordable.
# ---------------------------------------------------------------------------
def shift_permutation(shifts: tuple) -> tuple:
    """U(xi): e_(t,x) -> e_(t, x + xi_t), as the index map pi."""
    return tuple(site_index(t, x + shifts[t])
                 for t in range(TIME_EXTENT) for x in range(SPACE_EXTENT))


def inverse_permutation(permutation: tuple) -> tuple:
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def permutation_matrix(permutation: tuple) -> sp.Matrix:
    matrix = sp.zeros(len(permutation), len(permutation))
    for source, target in enumerate(permutation):
        matrix[target, source] = 1
    return matrix


def conjugate_by(matrix: sp.MatrixBase, permutation: tuple) -> sp.Matrix:
    """V M V^T, by index lookup."""
    back = inverse_permutation(permutation)
    return sp.Matrix(matrix.rows, matrix.cols,
                     lambda i, j: matrix[back[i], back[j]])


def commutator_with(matrix: sp.MatrixBase, permutation: tuple) -> sp.Matrix:
    """V M - M V, by index lookup."""
    back = inverse_permutation(permutation)
    return sp.Matrix(matrix.rows, matrix.cols,
                     lambda i, j: matrix[back[i], j] - matrix[i, permutation[j]])


def single_slice_shift(slice_label: int) -> tuple:
    """V_t: the +2 shift on slice t alone, identity on every other slice."""
    return shift_permutation(
        tuple(2 if s == slice_label else 0 for s in range(TIME_EXTENT)))


def pattern_shift(pattern: tuple) -> tuple:
    """U(xi) for a pattern xi in {0,1}^8, with 1 meaning the +2 shift."""
    return shift_permutation(tuple(2 * bit for bit in pattern))


def compose(first: tuple, second: tuple) -> tuple:
    """second after first, as index maps."""
    return tuple(second[first[k]] for k in range(len(first)))


def pattern_name(pattern: tuple) -> str:
    return "".join(str(bit) for bit in pattern)


def is_reflection_even(pattern: tuple) -> bool:
    """xi_t = xi_(-t): the condition that makes U(xi) commute with Ps."""
    return all(pattern[t] == pattern[(-t) % TIME_EXTENT]
               for t in range(TIME_EXTENT))


def is_adjacent_pair(pattern: tuple) -> bool:
    """Exactly two slices shifted, and they are neighbours on the time circle."""
    return sum(pattern) == 2 and any(
        pattern[t] and pattern[(t + 1) % TIME_EXTENT]
        for t in range(TIME_EXTENT))


def core_shift(slice_label: int) -> sp.Matrix:
    """W_1 and W_2: the +2 spatial shift restricted to ONE core slice, written
    in the t-major core order ((1,0)...(1,3),(2,0)...(2,3))."""
    position = {cell: index for index, cell in enumerate(CORE_ORDER)}
    matrix = sp.zeros(CORE_SIZE, CORE_SIZE)
    for time, space in CORE_ORDER:
        target = ((time, (space + 2) % SPACE_EXTENT)
                  if time == slice_label else (time, space))
        matrix[position[target], position[(time, space)]] = 1
    return matrix


def sign_patterns(size: int) -> tuple:
    """Every diag(+/-1) of the given size, as sign tuples."""
    return tuple(
        tuple(1 if not (bits >> k) & 1 else -1 for k in range(size))
        for bits in range(2 ** size))


def note_text() -> tuple:
    """(text, at_final_path).  THE FINAL PATH IS THE ONLY PATH READ: there is no
    draft fallback anywhere in this runner, so before landing the text is empty
    and gate H fails on note-at-final-path alone."""
    try:
        return NOTE_PATH.read_text(encoding="utf-8"), True
    except OSError:
        return "", False


def landed_text(path: str) -> str:
    """A LANDED PRIMARY BODY, read at its own path in the worktree.  Every
    citation below is checked against the primary body and never against a
    summary of it -- the Block 182 process rule."""
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except OSError:
        return ""

# ---------------------------------------------------------------------------
# THE N5 FENCE.  Single-line literal with \n separators; it appears
# BYTE-IDENTICALLY in the note and gate H checks it as a raw substring.
# ---------------------------------------------------------------------------
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 188's SITE-GLUED ACTION Q_s, REBUILT HERE from their landed note and runner and imported from nothing (Block 107's d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32 with eta_t = 1 and eta_x = (-1)^t, the antiperiodic kernel carrying omega_-(3) = -1 on the FAR seam, the grade-raising d_K, the SITE reflection theta_s(t) = -t with fixed slices {0,4}, the anchor pairing thA_s(t) = -1-t, the site-adapted glued Hodge with the physical anchors {0..3} at the uniform step c = 5/13 and the image anchors {4..7} the UNFLIPPED P_4-images of their thA_s partners, the site raising set A_s of the d_K entries in the CLOSED half {0..4} EXCLUDING the fixed-slice spatial edges, the derived glue D_s = A_s - Ps A_s Ps and the completion Q_s = m*H_s + H_s*D_s - D_s^T*H_s at (m, c) = (9/20, 5/13)), THE PER-SLICE SPATIAL SHIFT FAMILY U(xi): e_(t,x) -> e_(t, x + xi_t) with its ODD member U_x, its EVEN subfamily which is a FAITHFUL (Z_2)^8 OF ORDER 256, its single-slice twists V_t, its global even shift V_glob and its composites, THE CORE SHIFTS W_1 AND W_2 on the {1,2}-core Gram K, THE INVARIANT PROJECTOR Pi = (I + W_1)(I + W_2)/4 with its exact column-space basis B and the restricted Gram B^T K B, THE TWO FIXTURES (9/20, 5/13) and (1, 5/13), and the LANDED Block 128 cover_embedding() and Block 105 shear_hodge() -- THE ONLY TWO OBJECTS IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. AND THE WORDS ARE FENCED BEFORE THE NUMBERS ARE READ. GAUGE IS AN INTERPRETATION: what is measured is a CHOSEN FINITE TRANSFORMATION FAMILY and its exact stabilizer, and that its elements are REDUNDANCIES OF PHYSICAL STATES IS NOT DERIVED ANYWHERE. QUOTIENT IS AN INTERPRETATION: an invariant subspace of a positive form is computed, and NO GRAVITY CONSTRAINT QUOTIENT IS FORMED -- no lapse function, no shift vector, no Hamiltonian constraint, no momentum or diffeomorphism constraint, no first-class algebra, no Dirac closure and no ADM phase space is supplied by this block. LAPSE IS AN INTERPRETATION AND NO VOLUME DIAL IS TURNED HERE AT ALL. NO GENERALITY IS CLAIMED: TWO points on ONE carrier, with no bracket, no ray and no edge. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE CONTROL COMES FIRST AND IT IS BLOCK 188'S OWN NUMBER. The site route rebuilt here reproduces THEIR LANDED CORE GRAM DIGIT-FOR-DIGIT -- first leading minor 250811603701251182926764176363850176714557920003089965221914456500/666495028860293624372300921944800123265476111209829299156533225479 and second leading minor 9699265179160355495171233606378759680576921193642386633764164130236400111062250000/65542091681979044701359795584266761562795513633598145522262137753727157320281821073 -- with rank(Q_s) = 32, the core Gram symmetric at ZERO residual and positive definite at inertia (8,0,0), the reflected-transpose covariance Ps Q_s Ps = Q_s^T at ZERO and the plain symmetry defect at EXACTLY 144, which is Block 188's own precision and is not weakened here. IF THAT MINOR MOVED BY A DIGIT the symmetry family classified below would be the symmetry family of some other object. AND THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's many zeros, ranks and signs could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate H.\nper_mode: THE GRADING SELECTS THE EVEN SHIFTS, AND IT IS A MEASUREMENT AND NOT A PREFERENCE. The ODD per-slice shift U_x fails to commute with the grade-raising part: [U_x, d_K] has EXACTLY 64 nonzero entries, EXACT RANK 16, and its ordered time-pair support is the EIGHT DIAGONAL PAIRS (0,0) through (7,7) -- ENTIRELY INTRA-SLICE, so the obstruction does not propagate along time at all. THE MECHANISM IS MEASURED ONE LEVEL DOWN: the grade projectors themselves fail to commute with U_x at 16, 32 and 16 entries for grades 0, 1 and 2, because the staggered eta_x = (-1)^t makes the DEGREE of a site depend on x parity. The odd shift is therefore not a symmetry of the action either: [U_x, Q_s] has 64 nonzero entries at EXACT RANK 8, and U_x Q_s U_x^T - Q_s has 64. AND THE SPLIT IS LOCATED: U_x commutes with the site Hodge H_s at ZERO and fails on the glue D_s at 48, so the obstruction lives in the GLUE. THE GLOBAL EVEN SHIFT IS AN EXACT SYMMETRY: [V_glob, Q_s] = 0 and V_glob Q_s V_glob^T = Q_s, with V_glob commuting at ZERO with d_K, with H_s, with D_s and with Ps as well. THAT EVENNESS IS FORCED IS TRUE RELATIVE TO THE STIPULATED PARITY GRADING AND THIS CONSTRUCTED ACTION, AND IS NOT A GENERAL LAW.\nper_block: THE SINGLE-SLICE TWISTS LOCALIZE, AND THE RANGE IS TWO AND NOT ONE. None of the eight single-slice even twists V_t is an exact symmetry: every defect V_t Q_s V_t^T - Q_s has EXACT RANK 4, with the exact nonzero census {0: 96, 1: 64, 2: 80, 3: 64, 4: 64, 5: 64, 6: 80, 7: 64}. EVERY supported ordered time-pair CONTAINS the twisted slice t, and that is the localization, measured exactly at all eight slices. BUT THE SUPPORT IS NOT A NEAREST-SLICE BOND, AND THIS IS THE ADVERSARIAL CHECK'S CORRECTION CARRIED AS CONTENT RATHER THAN AS AN ERRATUM: at t = 0, 2 and 6 the support contains SEPARATION-TWO pairs -- (0,2) and (0,6) -- because the Hodge multiplication in the completion extends the support to temporal RANGE TWO. The exact circular range vector is (2,1,2,1,1,1,2,1) and the word bond is not used.\nlattice_wide: THE OS-COMPATIBLE SUBGROUP IS EXACTLY THE REFLECTION-EVEN ONE, AND COVARIANCE TRANSPORTS. Of the 256 even-shift patterns EXACTLY the 32 REFLECTION-EVEN ones, xi_t = xi_(-t), commute with Ps, and ALL 224 others FAIL to -- an EXACT IFF measured on the whole finite family and not a sample. For every one of those 32 the twisted action transports the covariance: Ps (V Q_s V^T) Ps = (V Q_s V^T)^T at ZERO residual, which is the two-line algebra Ps(V Q_s V^T)Ps = V (Ps Q_s Ps) V^T = V Q_s^T V^T = (V Q_s V^T)^T made executable for real orthogonal V commuting with Ps. AND THE INSTANCE IS NONTRIVIAL, WHICH IS THE POINT: V = V_1 V_7 commutes with Ps, its twist differs from Q_s at EXACTLY 128 entries -- so it is NOT in the stabilizer -- and the transport identity still holds at ZERO. OS COMPATIBILITY OF A TWIST IS STRICTLY WEAKER THAN EXACT INVARIANCE, 32 against 2.\nper_scope: THE CORE INVARIANCE THEOREM, THE EXPLICIT INVARIANT SECTOR, AND THE EXACT STABILIZER. On the {1,2}-core in the t-major order the two core shifts satisfy W_1^2 = W_2^2 = I_8 and W_1 W_2 = W_2 W_1 exactly; NEITHER IS INDIVIDUALLY AN INVARIANCE, each defect carrying EXACTLY 32 nonzero entries at EXACT RANK 4; and THE DIAGONAL ELEMENT IS AN EXACT INVARIANCE, (W_1 W_2)^T K (W_1 W_2) - K = 0_8, which is this block's one genuine theorem on the OS pairing. The invariant projector Pi = (I + W_1)(I + W_2)/4 is exactly symmetric, exactly idempotent and of EXACT RANK 4; its column-space basis B is exact with B^T B = I_4/2 and det(B^T B) = 1/16; and the restricted Gram B^T K B is exact with four exact leading minors, all POSITIVE, inertia (4,0,0), determinant 2198952681327212186709224903107443847656250000000000/2836414688995746959145683979271775764957689091340617249 and basis-independent density 35183242901235394987347598449719101562500000000000000/2836414688995746959145683979271775764957689091340617249. AND THE SCOPE IS STATED IN THE SAME BREATH AS THE RESULT, WHICH IS THE ADVERSARIAL CHECK'S C6: THE POSITIVITY OF THE RESTRICTION IS AUTOMATIC -- K is positive definite and B has full column rank, so y^T B^T K B y = (By)^T K (By) > 0 for every nonzero y -- SO IT IS NOT A NEW DYNAMICAL OR GRAVITATIONAL THEOREM AND IS NOT CLAIMED AS ONE. What is NOT automatic is the EXPLICIT sector: the projector's rank, the exact basis and the exact restricted Gram are COMPUTED. THE BASIS SIGN IS A CONVENTION AND IS MEASURED TO BE ONE: all sixteen sign patterns of B give the SAME four minors, and the check's displayed representative is the diag(1,-1,-1,1) conjugate, reached from this block's own core Gram by the STAGGERED SITE SIGN (-1)^(t+x), itself a diagonal congruence -- so the two independent rebuilds are ONE OBJECT IN TWO PHASE CONVENTIONS. AND THE STABILIZER IS EXACT AND EXHAUSTIVE, WHICH IS THE CHECK'S OWN LEG: all 2^8 = 256 patterns are swept, the family acts FAITHFULLY at 256 distinct site permutations, and Stab(Q_s) = {00000000, 11111111} of ORDER EXACTLY 2, generated by the uniform global even shift; all 32 reflection-even patterns are in the sweep and only the two uniform ones stabilize; NONE of the 8 adjacent two-slice patterns does. IT SURVIVES A SECOND FIXTURE (1, 5/13) -- same order-2 stabilizer, same exact W_1 W_2 core invariance, same rank-4 projector, same four positive quotient minors -- WHICH IS TWO POINTS AND NOT A WINDOW.\nRESULT: A FINITE TRANSFORMATION FAMILY IS CLASSIFIED, ITS EXACT STABILIZER IS COMPUTED BY EXHAUSTIVE SWEEP, AND AN EXPLICIT FOUR-DIMENSIONAL INVARIANT SECTOR IS BUILT ON BLOCK 188'S POSITIVE CORE -- AND NOT ONE LINE OF IT IS GRAVITY. Block 188's core minors are reproduced digit-for-digit as the control; the odd shift breaks the grading at 64 entries, rank 16, entirely intra-slice, with the grade projectors measured to be the mechanism; the global even shift is exact against every object in the construction; the eight single-slice twists localize on supports that all contain their own slice, with the exact census (96,64,80,64,64,64,80,64) and the exact range vector (2,1,2,1,1,1,2,1) -- RANGE TWO AND NOT NEAREST-BOND; reflection-evenness is an EXACT IFF for commuting with Ps over all 256 patterns and all 32 transport the OS covariance, with V_1 V_7 transporting at zero while differing from Q_s at 128; W_1 and W_2 are commuting involutions that individually fail at 32 entries and rank 4 and whose PRODUCT preserves the core Gram EXACTLY; the invariant projector has rank 4 with an exact basis and an exact restricted Gram of four positive minors at inertia (4,0,0), WHOSE POSITIVITY IS AUTOMATIC AND IS DISCLOSED AS SUCH; the exact stabilizer is {identity, global} OF ORDER 2 BY EXHAUSTIVE 256-SWEEP; and every one of those facts survives a second fixture, WHICH IS TWO POINTS AND NOT A WINDOW. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-188 STAND EXACTLY AS LANDED; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. BLOCK 188 IS NEITHER CORRECTED NOR CONTRADICTED: their core Gram is reproduced here digit-for-digit, their full-span positivity stands exactly as landed, and their named open leg -- THE PROPER OS TRANSFER -- is untouched by anything here and is NOT supplied by this block. BLOCK 107's SECTION-10 STEP 3 IS NOT EXECUTED: this block forms NO gravity constraint quotient and licenses NO part of one. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: TWO FIXTURES AND NO WINDOW; THE RESTRICTION POSITIVITY IS AUTOMATIC and the derived content is the symmetry classification, the stabilizer and the explicit sector rather than the positivity; THE FORCED EVENNESS IS RELATIVE to the stipulated parity grading and this constructed action and is not a general law; and THE COMPARATIVE PHRASE FIRST EXECUTABLE INSTANCE IS NOT VERIFIABLE UNDER A BOUNDED READ FENCE AND IS NOT MADE. THREE ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the EXACT STABILIZER OF ORDER 2 from the exhaustive 256-sweep, which is now a claim family of its own; the RANGE-TWO support correction, which is now a measured range vector; and the INTERPRETATION FENCE on the words gauge, quotient and lapse, which is now a required note section and four declared constants. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE CONSTRAINT QUOTIENT -- FIRST EXECUTABLE INSTANCE and B188 + B189 CHECK VERDICTS anchors, as corrected and extended by the b189 adversarial check.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
        "gauge_identification_claimed": GAUGE_IDENTIFICATION_CLAIMED,
        "constraint_quotient_claimed": CONSTRAINT_QUOTIENT_CLAIMED,
        "lapse_direction_claimed": LAPSE_DIRECTION_CLAIMED,
        "generality_claimed": GENERALITY_CLAIMED,
        # C -- the control and the grading selection.
        "citation_pins": True,
        "action_rank": ACTION_RANK,
        "site_covariance_residual": ZERO_RESIDUAL,
        "site_asymmetry": SITE_ASYMMETRY,
        "core_symmetry_residual": ZERO_RESIDUAL,
        "core_minor_1": B188_CORE_MINOR_1,
        "core_minor_2": B188_CORE_MINOR_2,
        "core_signs": CORE_SIGNS,
        "core_inertia": CORE_INERTIA,
        "odd_dk_nonzeros": ODD_DK_NONZEROS,
        "odd_dk_rank": ODD_DK_RANK,
        "odd_dk_support": ODD_DK_SUPPORT,
        "odd_action_nonzeros": ODD_ACTION_NONZEROS,
        "odd_action_rank": ODD_ACTION_RANK,
        "odd_conjugation_nonzeros": ODD_CONJUGATION_NONZEROS,
        "grade_projector_defects": GRADE_PROJECTOR_DEFECTS,
        "odd_hodge_nonzeros": ODD_HODGE_NONZEROS,
        "odd_glue_nonzeros": ODD_GLUE_NONZEROS,
        "global_even_residuals": GLOBAL_EVEN_RESIDUALS,
        # D -- the single-slice twist table and the range-two correction.
        "twist_nonzeros": TWIST_NONZEROS,
        "twist_ranks": TWIST_RANKS,
        "twist_supports": TWIST_SUPPORTS,
        "twist_ranges": TWIST_RANGES,
        "twist_locality": TWIST_LOCALITY,
        # E -- the OS-compatible subgroup and the covariance transport.
        "reflection_even_commuting": REFLECTION_EVEN_COMMUTING,
        "non_reflection_even_failing": NON_REFLECTION_EVEN_FAILING,
        "reflection_even_transporting": REFLECTION_EVEN_TRANSPORTING,
        "instance_commutator": ZERO_RESIDUAL,
        "instance_difference": TRANSPORT_INSTANCE_DIFFERENCE,
        "instance_transport": ZERO_RESIDUAL,
        # F -- the core action and the invariant sector.
        "w_involutive": (ZERO_RESIDUAL, ZERO_RESIDUAL),
        "w_commuting": ZERO_RESIDUAL,
        "singleton_defect_nonzeros": SINGLETON_DEFECT_NONZEROS,
        "singleton_defect_ranks": SINGLETON_DEFECT_RANKS,
        "diagonal_defect_nonzeros": DIAGONAL_DEFECT_NONZEROS,
        "projector_rank": PROJECTOR_RANK,
        "projector_idempotent": ZERO_RESIDUAL,
        "projector_symmetric": ZERO_RESIDUAL,
        "quotient_basis": QUOTIENT_BASIS,
        "basis_gram": BASIS_GRAM,
        "basis_gram_determinant": BASIS_GRAM_DETERMINANT,
        "quotient_gram": QUOTIENT_GRAM,
        "quotient_minors": QUOTIENT_MINORS,
        "quotient_signs": QUOTIENT_SIGNS,
        "quotient_inertia": QUOTIENT_INERTIA,
        "quotient_density": QUOTIENT_DENSITY,
        "basis_sign_invariant": BASIS_SIGN_PATTERN_COUNT,
        "check_representative_matches": True,
        "restriction_positivity_is_automatic":
            RESTRICTION_POSITIVITY_IS_AUTOMATIC,
        # G -- the exact stabilizer and the second fixture.
        "group_order": GROUP_ORDER,
        "stabilizer_patterns": STABILIZER_PATTERNS,
        "stabilizer_order": STABILIZER_ORDER,
        "reflection_even_stabilizers": REFLECTION_EVEN_STABILIZERS,
        "adjacent_pattern_count": ADJACENT_PATTERN_COUNT,
        "adjacent_stabilizers": ADJACENT_STABILIZERS,
        "robustness_stabilizer_order": STABILIZER_ORDER,
        "robustness_diagonal_defect": DIAGONAL_DEFECT_NONZEROS,
        "robustness_projector_rank": PROJECTOR_RANK,
        "robustness_core_minor_1": ROBUSTNESS_CORE_MINOR_1,
        "robustness_quotient_minors": ROBUSTNESS_QUOTIENT_MINORS,
        "robustness_quotient_signs": QUOTIENT_SIGNS,
        # H -- the note, the fence and the nsimplify absence.
        "required_scope_keys": SCOPE_KEYS,
        "nsimplify_calls": 0,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_objects_registered":
        # THE BANNER DENIED: the imposed objects asserted REGISTERED, which zero
        # registered and zero adopted objects forbid.
        claims["objects_registered"] = True
    elif mutation == "claim_gauge_identification":
        # THE CHECK'S C6 BOUNDARY DENIED, AND IT IS THIS BLOCK'S SINGLE BIGGEST
        # OVERREAD RISK.  Calling the shift family a GAUGE group asserts that
        # its elements are redundancies of physical states.  Nothing here
        # derives that: what is measured is a chosen finite transformation
        # family, its grading compatibility and its exact stabilizer.
        claims["gauge_identification_claimed"] = True
    elif mutation == "claim_constraint_quotient":
        # BLOCK 107'S STEP 3 ASSERTED.  The invariant sector is an invariant
        # subspace of a positive bilinear form; a gravity constraint quotient
        # would need a constraint, an algebra and a closure, and this block
        # supplies none of the eight named structures.
        claims["constraint_quotient_claimed"] = True
    elif mutation == "claim_lapse_direction":
        # THE CHECK'S C8 CORRECTION DENIED IN ADVANCE.  No volume dial is turned
        # in this block at all; asserting a lapse direction would import a
        # bridge theorem that does not exist.
        claims["lapse_direction_claimed"] = True
    elif mutation == "claim_generality":
        # TWO FIXTURES OVERSOLD.  Every statement here is measured at (9/20,
        # 5/13) and re-measured at (1, 5/13) and NOWHERE ELSE; there is no
        # bracket, no ray and no edge.
        claims["generality_claimed"] = True
    elif mutation == "break_control_minor":
        # THE CONTROL DENIED AT ITS LAST DIGIT: if Block 188's core minor is not
        # reproduced exactly then the symmetry family classified below is the
        # symmetry family of a different object and nothing in this block
        # attaches to theirs.
        claims["core_minor_1"] = B188_CORE_MINOR_1 + 1
    elif mutation == "break_odd_shift_grading":
        # THE SELECTION ERASED: the odd shift asserted to commute with d_K,
        # which would make the even restriction an arbitrary preference rather
        # than a forced one.  It is measured to fail at 64 entries and rank 16.
        claims["odd_dk_nonzeros"] = ZERO_RESIDUAL
    elif mutation == "break_grade_projectors":
        # THE MECHANISM ERASED: the grade projectors asserted to commute with
        # the odd shift, which is exactly the statement the staggered
        # eta_x = (-1)^t forbids.  Without this the intra-slice commutator is a
        # number without a reason.
        claims["grade_projector_defects"] = (0, 0, 0)
    elif mutation == "break_global_even_symmetry":
        # THE ONE EXACT SYMMETRY DENIED: the global even shift asserted NOT to
        # commute with Q_s.  It is the generator of the entire stabilizer, so
        # if it moved the action there would be no stabilizer to compute.
        claims["global_even_residuals"] = dict(
            claims["global_even_residuals"], **{"Q_s": 64})
    elif mutation == "break_twist_census":
        # THE LOCALIZATION TABLE FLATTENED: the t = 0 twist asserted to carry
        # the same 64 entries as the generic slice, which would erase the
        # measured inhomogeneity of the seam-adjacent slices.
        claims["twist_nonzeros"] = (64,) + TWIST_NONZEROS[1:]
    elif mutation == "break_twist_range_two":
        # THE ADVERSARIAL CHECK'S CORRECTION DENIED, AND THIS IS THE MUTATION
        # THAT GUARDS IT.  The range vector asserted to be all ones -- the
        # NEAREST-BOND wording the check refused.  Three slices measure range
        # TWO, and the wording of the whole block depends on it.
        claims["twist_ranges"] = (1,) * TIME_EXTENT
    elif mutation == "break_twist_locality":
        # THE LOCALIZATION ITSELF DENIED: some supported pair asserted NOT to
        # contain the twisted slice, which would mean the twists are not
        # localized at all and the table describes nothing.
        claims["twist_locality"] = (False,) + TWIST_LOCALITY[1:]
    elif mutation == "break_reflection_even_criterion":
        # THE IFF DOWNGRADED TO ONE DIRECTION: the non-reflection-even patterns
        # asserted to commute with Ps too, which would make reflection-evenness
        # descriptive rather than the exact criterion it is measured to be.
        claims["non_reflection_even_failing"] = ZERO_RESIDUAL
    elif mutation == "break_os_transport":
        # THE TRANSPORT LEMMA DENIED AT ITS INSTANCE: the V_1 V_7 twist asserted
        # NOT to satisfy Ps (V Q V^T) Ps = (V Q V^T)^T.  If covariance did not
        # transport, the OS-compatible subgroup would be empty of content.
        claims["instance_transport"] = 128
    elif mutation == "break_twist_nontrivial":
        # THE INSTANCE MADE VACUOUS: the V_1 V_7 twist asserted EQUAL to Q_s,
        # which would make the transport statement a tautology about the
        # stabilizer instead of the strictly-weaker fact it is.
        claims["instance_difference"] = ZERO_RESIDUAL
    elif mutation == "break_diagonal_invariance":
        # THE BLOCK'S ONE INVARIANCE THEOREM DENIED: the simultaneous shift
        # asserted NOT to preserve the core Gram.  Without it the invariant
        # projector projects onto nothing the pairing respects.
        claims["diagonal_defect_nonzeros"] = 32
    elif mutation == "break_singleton_invariance":
        # THE THEOREM TRIVIALIZED FROM THE OTHER SIDE: W_1 alone asserted to
        # preserve K, which would make the DIAGONAL element's invariance an
        # uninteresting consequence rather than the measured fact that only the
        # product works.
        claims["singleton_defect_nonzeros"] = (ZERO_RESIDUAL,
                                               SINGLETON_DEFECT_NONZEROS[1])
    elif mutation == "break_projector_rank":
        # THE SECTOR INFLATED: the invariant projector asserted to have rank 8,
        # i.e. to be the identity, which would mean the whole core is invariant
        # and there is no sector to exhibit.
        claims["projector_rank"] = CORE_SIZE
    elif mutation == "break_quotient_positivity":
        # THE RESTRICTED GRAM DENIED AT ITS THIRD MINOR: asserted NEGATIVE,
        # which the exact determinants over QQ forbid and which congruence
        # forbids independently.
        claims["quotient_signs"] = (1, 1, -1, 1)
    elif mutation == "break_basis_sign_invariance":
        # THE CONVENTION PROMOTED TO A FACT: the basis sign asserted to change
        # the minors, which would mean the displayed quotient Gram carries
        # content that it does not, and would leave this block and the
        # adversarial check reporting genuinely different objects.
        claims["basis_sign_invariant"] = 1
    elif mutation == "break_automatic_disclosure":
        # THE CHECK'S C6.1 DENIED, AND THIS IS THE MUTATION THAT GUARDS IT: the
        # restriction positivity asserted NOT automatic, i.e. asserted to be a
        # new dynamical theorem.  It follows from K > 0 and full column rank
        # alone, and saying otherwise is precisely the overread the check named.
        claims["restriction_positivity_is_automatic"] = False
    elif mutation == "break_stabilizer_order":
        # THE ADVERSARIAL CHECK'S OWN LEG DENIED: the stabilizer asserted to
        # have order 4.  The exhaustive 256-sweep returns exactly two patterns,
        # and the whole 32-against-2 moral depends on that number.
        claims["stabilizer_order"] = 4
    elif mutation == "break_stabilizer_reflection_even":
        # OS COMPATIBILITY CONFLATED WITH INVARIANCE: all 32 reflection-even
        # patterns asserted to stabilize Q_s.  Exactly 2 do, and the gap between
        # 32 and 2 is the single most useful thing family G measures.
        claims["reflection_even_stabilizers"] = REFLECTION_EVEN_COUNT
    elif mutation == "break_stabilizer_adjacent":
        # A LOCAL SYMMETRY INVENTED: some adjacent two-slice pattern asserted to
        # be an exact symmetry, which would mean the stabilizer contains a
        # LOCAL element and the global generator is not the whole story.
        claims["adjacent_stabilizers"] = 1
    elif mutation == "break_robustness":
        # THE SECOND POINT DENIED: the (1, 5/13) fixture asserted to lose the
        # order-2 stabilizer.  It is the mutation that stops the second point
        # from being quietly dropped -- while the banner still refuses to call
        # two points a window.
        claims["robustness_stabilizer_order"] = 1
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim")
    elif mutation == "break_nsimplify_absence":
        # THE HAZARD DECLARED PRESENT: a nonzero nsimplify count asserted, which
        # the source-token census forbids.  Every zero in this block would be
        # suspect if the call appeared even once.
        claims["nsimplify_calls"] = 1
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
    # C -- the control and the grading selection
    action_rank: int
    site_covariance_residual: int
    site_asymmetry: int
    core_symmetry_residual: int
    core_minors: tuple
    core_signs: tuple
    core_inertia: tuple
    odd_dk_nonzeros: int
    odd_dk_rank: int
    odd_dk_support: tuple
    odd_action_nonzeros: int
    odd_action_rank: int
    odd_conjugation_nonzeros: int
    grade_projector_defects: tuple
    odd_hodge_nonzeros: int
    odd_glue_nonzeros: int
    global_even_residuals: dict
    # D -- the single-slice twist table
    twist_nonzeros: tuple
    twist_ranks: tuple
    twist_supports: tuple
    twist_ranges: tuple
    twist_locality: tuple
    # E -- the OS-compatible subgroup
    reflection_even_commuting: int
    non_reflection_even_failing: int
    reflection_even_transporting: int
    instance_commutator: int
    instance_difference: int
    instance_transport: int
    # F -- the core action and the invariant sector
    w_involutive: tuple
    w_commuting: int
    singleton_defect_nonzeros: tuple
    singleton_defect_ranks: tuple
    diagonal_defect_nonzeros: int
    projector_rank: int
    projector_idempotent: int
    projector_symmetric: int
    quotient_basis: tuple
    basis_gram: sp.Matrix
    basis_gram_determinant: object
    quotient_gram: tuple
    quotient_minors: tuple
    quotient_signs: tuple
    quotient_inertia: tuple
    quotient_density: object
    basis_sign_invariant: int
    check_representative_matches: bool
    staggered_congruence_matches: bool
    automatic_positivity_witness: bool
    # G -- the exact stabilizer and the second fixture
    group_order: int
    stabilizer_patterns: tuple
    stabilizer_order: int
    reflection_even_stabilizers: int
    adjacent_pattern_count: int
    adjacent_stabilizers: int
    robustness_point: tuple
    robustness_stabilizer_order: int
    robustness_diagonal_defect: int
    robustness_projector_rank: int
    robustness_core_minor_1: object
    robustness_quotient_minors: tuple
    robustness_quotient_signs: tuple
    # H
    nsimplify_calls: int
    exactness_holds: bool


def build_site_action(mass: object, shear: object) -> dict:
    """BLOCK 188's SITE CONSTRUCTION, REBUILT WHOLE at a given fixture.  Called
    twice: once at their fixture and once at the robustness point, so the second
    point is a full rebuild and not a re-dialled cache."""
    kernel = staggered_kernel()
    raising = raising_part(kernel)
    reflection = reflection_permutation(site_theta)
    restricted = site_restricted_raising(raising)
    glue = sp.expand(restricted - reflection * restricted * reflection)
    hodge = site_image_hodge(shear)
    action = completion(hodge, glue, mass)
    return {"kernel": kernel, "raising": raising, "reflection": reflection,
            "glue": glue, "hodge": hodge, "action": action}


def stabilizer_sweep(action: sp.Matrix) -> dict:
    """THE EXHAUSTIVE 2^8 SWEEP, EXACT AND BY INDEX LOOKUP.  A pattern xi
    stabilizes Q_s exactly when Q_s[pi^-1(i), pi^-1(j)] == Q_s[i,j] for every
    (i,j) -- a finite conjunction of exact rational equalities, with no
    tolerance and no residual threshold anywhere."""
    permutations = set()
    stabilizers: list[str] = []
    reflection_even_total = reflection_even_stabilizers = 0
    adjacent_total = adjacent_stabilizers = 0
    for bits in range(2 ** TIME_EXTENT):
        pattern = tuple((bits >> t) & 1 for t in range(TIME_EXTENT))
        permutation = pattern_shift(pattern)
        permutations.add(permutation)
        back = inverse_permutation(permutation)
        fixes = all(action[back[i], back[j]] == action[i, j]
                    for i in range(COVER_SIZE) for j in range(COVER_SIZE))
        if fixes:
            stabilizers.append(pattern_name(pattern))
        if is_reflection_even(pattern):
            reflection_even_total += 1
            reflection_even_stabilizers += int(fixes)
        if is_adjacent_pair(pattern):
            adjacent_total += 1
            adjacent_stabilizers += int(fixes)
    return {
        "group_order": len(permutations),
        "stabilizers": tuple(sorted(stabilizers)),
        "reflection_even_total": reflection_even_total,
        "reflection_even_stabilizers": reflection_even_stabilizers,
        "adjacent_total": adjacent_total,
        "adjacent_stabilizers": adjacent_stabilizers,
    }


def invariant_sector(core: sp.Matrix) -> dict:
    """THE Z2 x Z2 INVARIANT SECTOR of a core Gram: the two core shifts, their
    defects, the projector, its exact column-space basis and the restricted
    Gram, with the basis-sign convention measured rather than assumed."""
    identity = sp.eye(CORE_SIZE)
    first, second = core_shift(CORE_SLICES[0]), core_shift(CORE_SLICES[1])
    projector = sp.expand((identity + first) * (identity + second) / 4)
    basis = sp.Matrix.hstack(*projector.columnspace())
    restricted = sp.expand(basis.T * core * basis)
    minors = leading_minors(restricted)
    return {
        "first": first,
        "second": second,
        "involutive": (residual_count(first * first - identity),
                       residual_count(second * second - identity)),
        "commuting": residual_count(first * second - second * first),
        "singleton_defects": (sp.expand(first.T * core * first - core),
                              sp.expand(second.T * core * second - core)),
        "diagonal_defect": sp.expand(
            (first * second).T * core * (first * second) - core),
        "projector": projector,
        "basis": basis,
        "restricted": restricted,
        "minors": minors,
    }


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    built = build_site_action(FIXTURE_MASS, FIXTURE_SHEAR)
    action = built["action"]
    raising = built["raising"]
    hodge = built["hodge"]
    glue = built["glue"]
    reflection = built["reflection"]

    # --- C: THE CONTROL, WHICH IS BLOCK 188'S OWN OBJECT -------------------
    site_covariance = residual_count(
        reflection * action * reflection - action.T)
    site_asymmetry = residual_count(action - action.T)
    inverse = exact_inverse(action)
    core = paired_gram(inverse, CORE_SLICES, site_theta)
    core_minors = leading_minors(core)

    # --- C: THE GRADING SELECTION ------------------------------------------
    odd = shift_permutation(ODD_SHIFT)
    even = shift_permutation(EVEN_SHIFT)
    odd_dk = sp.expand(commutator_with(raising, odd))
    odd_action = sp.expand(commutator_with(action, odd))
    grade_defects = tuple(
        residual_count(commutator_with(grade_projector(g), odd))
        for g in (0, 1, 2))
    even_matrix = permutation_matrix(even)
    global_even = {
        "d_K": residual_count(commutator_with(raising, even)),
        "H_s": residual_count(commutator_with(hodge, even)),
        "D_s": residual_count(commutator_with(glue, even)),
        "Q_s": residual_count(commutator_with(action, even)),
        "Ps": residual_count(even_matrix * reflection
                             - reflection * even_matrix),
        "conjugation": residual_count(conjugate_by(action, even) - action),
    }

    # --- D: THE SINGLE-SLICE TWIST TABLE -----------------------------------
    twist_nonzeros: list[int] = []
    twist_ranks: list[int] = []
    twist_supports: list[tuple] = []
    twist_ranges: list[int] = []
    twist_locality: list[bool] = []
    for label in range(TIME_EXTENT):
        defect = sp.expand(
            conjugate_by(action, single_slice_shift(label)) - action)
        support = time_pair_support(defect)
        twist_nonzeros.append(nonzero_entries(defect))
        twist_ranks.append(exact_rank(defect))
        twist_supports.append(support)
        twist_ranges.append(support_range(support))
        twist_locality.append(all(label in pair for pair in support))

    # --- E: THE OS-COMPATIBLE SUBGROUP AND THE TRANSPORT --------------------
    reflection_even_commuting = 0
    non_reflection_even_failing = 0
    reflection_even_transporting = 0
    for bits in range(2 ** TIME_EXTENT):
        pattern = tuple((bits >> t) & 1 for t in range(TIME_EXTENT))
        permutation = pattern_shift(pattern)
        matrix = permutation_matrix(permutation)
        commutes = residual_count(
            matrix * reflection - reflection * matrix) == 0
        if is_reflection_even(pattern):
            reflection_even_commuting += int(commutes)
            twisted = conjugate_by(action, permutation)
            reflection_even_transporting += int(residual_count(
                reflection * twisted * reflection - twisted.T) == 0)
        else:
            non_reflection_even_failing += int(not commutes)
    instance = compose(single_slice_shift(TRANSPORT_INSTANCE[0]),
                       single_slice_shift(TRANSPORT_INSTANCE[1]))
    instance_matrix = permutation_matrix(instance)
    instance_twist = conjugate_by(action, instance)

    # --- F: THE CORE ACTION AND THE INVARIANT SECTOR ------------------------
    sector = invariant_sector(core)
    basis = sector["basis"]
    restricted = sector["restricted"]
    basis_gram = sp.expand(basis.T * basis)
    quotient_minors = sector["minors"]
    # THE BASIS-SIGN CONVENTION, MEASURED.  Every diag(+/-1) congruence of the
    # basis leaves the leading minors untouched, because each minor is scaled by
    # a square; the count of sign patterns that preserve them is the whole 16.
    invariant_sign_patterns = sum(
        1 for signs in sign_patterns(PROJECTOR_RANK)
        if leading_minors(
            sp.expand(sp.diag(*signs) * restricted * sp.diag(*signs)))
        == quotient_minors)
    # AND THE ADVERSARIAL CHECK'S DISPLAYED REPRESENTATIVE IS RECONCILED, not
    # waved at: it is the diag(1,-1,-1,1) conjugate of this block's restricted
    # Gram, and that conjugate is ALSO what this block's core Gram gives after
    # the STAGGERED SITE SIGN (-1)^(t+x) -- a diagonal congruence of the core.
    check_sign = sp.diag(*CHECK_BASIS_SIGN)
    check_representative = sp.expand(check_sign * restricted * check_sign)
    staggered = sp.diag(*STAGGERED_SITE_SIGN)
    staggered_core = sp.expand(staggered * core * staggered)
    staggered_representative = sp.expand(basis.T * staggered_core * basis)
    # THE AUTOMATIC-POSITIVITY WITNESS, MEASURED RATHER THAN ARGUED: the
    # restriction is a congruence of a positive-definite form by a full-column-
    # rank map, so positivity is inherited and is not a new theorem.
    automatic_witness = bool(
        exact_rank(basis) == PROJECTOR_RANK
        and inertia(core) == CORE_INERTIA
        and residual_count(restricted - basis.T * core * basis) == 0)

    # --- G: THE EXACT STABILIZER AND THE SECOND FIXTURE ---------------------
    sweep = stabilizer_sweep(action)
    robust_mass, robust_shear = ROBUSTNESS_POINT
    robust = build_site_action(robust_mass, robust_shear)
    robust_sweep = stabilizer_sweep(robust["action"])
    robust_core = paired_gram(
        exact_inverse(robust["action"]), CORE_SLICES, site_theta)
    robust_sector = invariant_sector(robust_core)

    citation_pins = {
        "b107_step_three": B107_STEP_THREE_PIN in landed_text(BLOCK107_NOTE),
        "b107_not_a_nogo": B107_NOT_A_NOGO_PIN in landed_text(BLOCK107_NOTE),
        "b187_quotient_downstream":
            B187_QUOTIENT_PIN in landed_text(BLOCK187_NOTE),
        "b188_prerequisite":
            B188_PREREQUISITE_PIN in landed_text(BLOCK188_NOTE),
        "b188_no_quotient":
            B188_NO_QUOTIENT_PIN in landed_text(BLOCK188_NOTE),
    }
    banners = {
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "objects_registered": bool(REGISTERED_OBJECTS or ADOPTED_OBJECTS),
        "gauge_identification_claimed": GAUGE_IDENTIFICATION_CLAIMED,
        "constraint_quotient_claimed": CONSTRAINT_QUOTIENT_CLAIMED,
        "lapse_direction_claimed": LAPSE_DIRECTION_CLAIMED,
        "generality_claimed": GENERALITY_CLAIMED,
        "unsupplied_structures": len(UNSUPPLIED_GRAVITY_STRUCTURES),
    }
    exact_scalars = (
        tuple(core_minors) + tuple(quotient_minors)
        + tuple(robust_sector["minors"])
        + (sp.expand(quotient_minors[-1] / exact_determinant(basis_gram)),))
    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        action_rank=exact_rank(action),
        site_covariance_residual=site_covariance,
        site_asymmetry=site_asymmetry,
        core_symmetry_residual=residual_count(core - core.T),
        core_minors=core_minors,
        core_signs=minor_signs(core_minors),
        core_inertia=inertia(core),
        odd_dk_nonzeros=nonzero_entries(odd_dk),
        odd_dk_rank=exact_rank(odd_dk),
        odd_dk_support=time_pair_support(odd_dk),
        odd_action_nonzeros=nonzero_entries(odd_action),
        odd_action_rank=exact_rank(odd_action),
        odd_conjugation_nonzeros=residual_count(
            conjugate_by(action, odd) - action),
        grade_projector_defects=grade_defects,
        odd_hodge_nonzeros=residual_count(commutator_with(hodge, odd)),
        odd_glue_nonzeros=residual_count(commutator_with(glue, odd)),
        global_even_residuals=global_even,
        twist_nonzeros=tuple(twist_nonzeros),
        twist_ranks=tuple(twist_ranks),
        twist_supports=tuple(twist_supports),
        twist_ranges=tuple(twist_ranges),
        twist_locality=tuple(twist_locality),
        reflection_even_commuting=reflection_even_commuting,
        non_reflection_even_failing=non_reflection_even_failing,
        reflection_even_transporting=reflection_even_transporting,
        instance_commutator=residual_count(
            instance_matrix * reflection - reflection * instance_matrix),
        instance_difference=residual_count(instance_twist - action),
        instance_transport=residual_count(
            reflection * instance_twist * reflection - instance_twist.T),
        w_involutive=sector["involutive"],
        w_commuting=sector["commuting"],
        singleton_defect_nonzeros=tuple(
            nonzero_entries(d) for d in sector["singleton_defects"]),
        singleton_defect_ranks=tuple(
            exact_rank(d) for d in sector["singleton_defects"]),
        diagonal_defect_nonzeros=nonzero_entries(sector["diagonal_defect"]),
        projector_rank=exact_rank(sector["projector"]),
        projector_idempotent=residual_count(
            sector["projector"] * sector["projector"] - sector["projector"]),
        projector_symmetric=residual_count(
            sector["projector"].T - sector["projector"]),
        quotient_basis=tuple(
            tuple(basis[row, column] for row in range(CORE_SIZE))
            for column in range(basis.cols)),
        basis_gram=basis_gram,
        basis_gram_determinant=exact_determinant(basis_gram),
        quotient_gram=tuple(
            tuple(restricted[r, c] for c in range(PROJECTOR_RANK))
            for r in range(PROJECTOR_RANK)),
        quotient_minors=quotient_minors,
        quotient_signs=minor_signs(quotient_minors),
        quotient_inertia=inertia(restricted),
        quotient_density=sp.expand(
            quotient_minors[-1] / exact_determinant(basis_gram)),
        basis_sign_invariant=invariant_sign_patterns,
        check_representative_matches=all(
            check_representative[r, c] == CHECK_QUOTIENT_GRAM[r][c]
            for r in range(PROJECTOR_RANK) for c in range(PROJECTOR_RANK)),
        staggered_congruence_matches=bool(
            residual_count(staggered_representative - check_representative) == 0
            and leading_minors(staggered_core) == core_minors),
        automatic_positivity_witness=automatic_witness,
        group_order=sweep["group_order"],
        stabilizer_patterns=sweep["stabilizers"],
        stabilizer_order=len(sweep["stabilizers"]),
        reflection_even_stabilizers=sweep["reflection_even_stabilizers"],
        adjacent_pattern_count=sweep["adjacent_total"],
        adjacent_stabilizers=sweep["adjacent_stabilizers"],
        robustness_point=(robust_mass, robust_shear),
        robustness_stabilizer_order=len(robust_sweep["stabilizers"]),
        robustness_diagonal_defect=nonzero_entries(
            robust_sector["diagonal_defect"]),
        robustness_projector_rank=exact_rank(robust_sector["projector"]),
        robustness_core_minor_1=leading_minors(robust_core)[0],
        robustness_quotient_minors=robust_sector["minors"],
        robustness_quotient_signs=minor_signs(robust_sector["minors"]),
        nsimplify_calls=nsimplify_occurrences(),
        exactness_holds=all(is_exact_rational(v) for v in exact_scalars),
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
        "registry blobs in the worktree. THE TWO BLOCK 188 ARTIFACTS ARE "
        "CONTENT-BOUND -- its note and its runner, the pair that identifies "
        "the commit this block's branch is cut from AND the construction this "
        "block rebuilds -- at PARENT_COMMIT, in the worktree and against their "
        "pinned blobs, and PARENT_COMMIT IS REAL and PARENT_REF resolves to "
        "it, so nothing needs sed at landing. THE STALE PIN IS THE BLOCK 187 "
        "TIP, a REAL ancestor of HEAD that PREDATES Block 188 and therefore "
        "carries NEITHER Block 188 artifact, which is exactly what makes the "
        "stale_parent_authority mutation bite: under it the gate looks for the "
        "artifact blobs at a commit where they do not exist. "
        "AUDIT_INPUT_PATHS IS LITERAL and every one of its SEVEN entries is "
        "required readable in the worktree EXCEPT this block's own note, which "
        "lands later and belongs to gate H -- and the seven include BOTH BLOCK "
        "188 ARTIFACTS, whose action Q_s is this block's entire object, the "
        "BLOCK 107 note whose section-10 STEP 3 this block does NOT execute, "
        "and the BLOCK 187 note whose downstream-quotient sentence is pinned. "
        "AND THE MACHINERY IMPORT IS GATED: the LANDED Block 128 runner must "
        "have imported, because the two helper objects this runner does not "
        "build itself -- cover_embedding() and the Block 105 shear_hodge() -- "
        "are read from it, and NOTHING from any scratchpad is imported or read",
        bool(
            AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
            and len(AUDIT_INPUT_PATHS) == 7
            and len(set(AUDIT_INPUT_PATHS)) == 7
            and BLOCK188_NOTE in AUDIT_INPUT_PATHS
            and BLOCK188_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK187_NOTE in AUDIT_INPUT_PATHS
            and BLOCK107_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_RUNNER in AUDIT_INPUT_PATHS
            and CAMPAIGN_NOTE in AUDIT_INPUT_PATHS
            and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
            and authority.inputs_missing == ()
            and PARENT_ARTIFACTS == (BLOCK188_NOTE, BLOCK188_RUNNER)
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
        "B-THE-IMPOSED-OBJECT-BANNER-and-THE-INTERPRETATION-FENCE",
        f"THE BANNER COMES BEFORE ANY NUMERAL AND IT IS MEASURED RATHER THAN "
        f"ASSERTED. {ban['imposed_objects']} objects are IMPOSED by this block "
        f"-- Block 188's site-glued action Q_s rebuilt from their landed pair, "
        f"the per-slice spatial shift family with its faithful even subgroup "
        f"of order 256, the core shifts with their projector and restricted "
        f"Gram, the TWO fixtures, and the two LANDED Block 128 helpers that "
        f"are the only imports -- and {ban['registered_objects']} are "
        f"REGISTERED and {ban['adopted_objects']} are ADOPTED. AND THE "
        f"BANNER'S SECOND HALF IS THE INTERPRETATION FENCE, gated as declared "
        f"constants because THIS BLOCK ENDS ON A POSITIVE RESULT WITH "
        f"GRAVITY-SHAPED VOCABULARY AND THAT IS THE EASIEST THING IN THE "
        f"CORPUS TO OVERREAD. GAUGE IS AN INTERPRETATION: a CHOSEN FINITE "
        f"TRANSFORMATION FAMILY is measured, and that its elements are "
        f"REDUNDANCIES OF PHYSICAL STATES is derived NOWHERE. QUOTIENT IS AN "
        f"INTERPRETATION: an invariant subspace of a positive form is "
        f"computed, and {ban['unsupplied_structures']} named gravity "
        f"structures are NOT SUPPLIED by this block -- "
        f"{', '.join(UNSUPPLIED_GRAVITY_STRUCTURES)}. LAPSE IS AN "
        f"INTERPRETATION and no volume dial is turned here at all. NO "
        f"GENERALITY: TWO fixtures on ONE carrier, with no bracket, no ray and "
        f"no edge. Asserting any of the four, or asserting that the imposed "
        f"objects are registered, fails HERE and nowhere else",
        bool(
            ban["imposed_objects"] == 5
            and ban["registered_objects"] == 0
            and ban["adopted_objects"] == 0
            and ban["unsupplied_structures"] == 8
            and ban["objects_registered"] == claims["objects_registered"]
            and ban["gauge_identification_claimed"]
            == claims["gauge_identification_claimed"]
            and ban["constraint_quotient_claimed"]
            == claims["constraint_quotient_claimed"]
            and ban["lapse_direction_claimed"]
            == claims["lapse_direction_claimed"]
            and ban["generality_claimed"] == claims["generality_claimed"]))

    # --- C: the control and the grading selection ---------------------------
    pins = facts.citation_pins
    checks.check(
        "C-THE-CONTROL-and-THE-GRADING-THAT-SELECTS-THE-EVEN-SHIFTS",
        f"THE CONTROL COMES FIRST AND IT IS SOMEBODY ELSE'S NUMBER. The site "
        f"action rebuilt here from Block 188's landed pair has rank "
        f"{facts.action_rank}, is reflected-transpose covariant at "
        f"{facts.site_covariance_residual} while its PLAIN symmetry defect is "
        f"{facts.site_asymmetry} -- Block 188's own precision, not weakened "
        f"here -- and its {CORE_SLICES} core Gram is symmetric at "
        f"{facts.core_symmetry_residual}, positive definite at inertia "
        f"{facts.core_inertia}, and reproduces THEIR LANDED FIRST TWO LEADING "
        f"MINORS DIGIT-FOR-DIGIT: {facts.core_minors[0]} and "
        f"{facts.core_minors[1]}. IF THOSE MOVED, EVERY SYMMETRY BELOW WOULD "
        f"BE A SYMMETRY OF SOME OTHER OBJECT. THEN THE SELECTION, AND IT IS A "
        f"MEASUREMENT AND NOT A PREFERENCE: the ODD per-slice shift fails to "
        f"commute with the grade-raising part at EXACTLY "
        f"{facts.odd_dk_nonzeros} entries, EXACT RANK {facts.odd_dk_rank}, on "
        f"the support {facts.odd_dk_support} -- the EIGHT DIAGONAL time-pairs, "
        f"so the obstruction is ENTIRELY INTRA-SLICE and does not propagate "
        f"along time at all. THE MECHANISM IS MEASURED ONE LEVEL DOWN: the "
        f"grade projectors themselves fail to commute with it at "
        f"{facts.grade_projector_defects} entries for grades 0, 1 and 2, "
        f"because the staggered eta_x = (-1)^t makes a site's DEGREE depend on "
        f"x parity. So the odd shift is no symmetry of the action either: "
        f"{facts.odd_action_nonzeros} entries at RANK {facts.odd_action_rank}, "
        f"and {facts.odd_conjugation_nonzeros} under conjugation. AND THE "
        f"SPLIT IS LOCATED: it commutes with the Hodge at "
        f"{facts.odd_hodge_nonzeros} and fails on the GLUE at "
        f"{facts.odd_glue_nonzeros}. THE GLOBAL EVEN SHIFT IS EXACT AGAINST "
        f"EVERYTHING: {facts.global_even_residuals}. THAT EVENNESS IS FORCED "
        f"IS TRUE RELATIVE TO THIS PARITY GRADING AND THIS ACTION AND IS NOT "
        f"A GENERAL LAW. EVERY CITATION IS SOMEBODY ELSE'S LANDED SENTENCE, "
        f"read from the PRIMARY BODY: Block 107's step 3 and their scope "
        f"firewall, Block 187's downstream-quotient sentence, and Block 188's "
        f"own prerequisite and no-quotient sentences, at {pins}",
        bool(
            all(pins.values()) == claims["citation_pins"]
            and facts.action_rank == claims["action_rank"]
            and facts.site_covariance_residual
            == claims["site_covariance_residual"]
            and facts.site_asymmetry == claims["site_asymmetry"]
            and facts.core_symmetry_residual == claims["core_symmetry_residual"]
            and facts.core_minors[0] == claims["core_minor_1"]
            and facts.core_minors[1] == claims["core_minor_2"]
            and facts.core_signs == claims["core_signs"]
            and facts.core_inertia == claims["core_inertia"]
            and facts.odd_dk_nonzeros == claims["odd_dk_nonzeros"]
            and facts.odd_dk_rank == claims["odd_dk_rank"]
            and facts.odd_dk_support == claims["odd_dk_support"]
            and facts.odd_action_nonzeros == claims["odd_action_nonzeros"]
            and facts.odd_action_rank == claims["odd_action_rank"]
            and facts.odd_conjugation_nonzeros
            == claims["odd_conjugation_nonzeros"]
            and facts.grade_projector_defects
            == claims["grade_projector_defects"]
            and facts.odd_hodge_nonzeros == claims["odd_hodge_nonzeros"]
            and facts.odd_glue_nonzeros == claims["odd_glue_nonzeros"]
            and facts.global_even_residuals == claims["global_even_residuals"]))

    # --- D: the twist table and the range-two correction --------------------
    checks.check(
        "D-THE-TWIST-TABLE-and-THE-RANGE-IS-TWO-AND-NOT-A-NEAREST-BOND",
        f"THE SINGLE-SLICE EVEN TWISTS LOCALIZE, AND NONE OF THEM IS A "
        f"SYMMETRY. Every defect V_t Q_s V_t^T - Q_s has EXACT RANK 4 "
        f"({facts.twist_ranks}) with the exact nonzero census "
        f"{facts.twist_nonzeros} -- inhomogeneous, and the three heavy slices "
        f"are the ones the seam touches. THE LOCALIZATION IS EXACT: every "
        f"supported ordered time-pair CONTAINS the twisted slice, at all eight "
        f"labels ({facts.twist_locality}), on the supports "
        f"{facts.twist_supports}. AND HERE IS THE ADVERSARIAL CHECK'S "
        f"CORRECTION, CARRIED AS A MEASURED NUMBER RATHER THAN AS AN ERRATUM: "
        f"THE SUPPORT IS NOT A NEAREST-SLICE BOND. The exact circular range "
        f"vector is {facts.twist_ranges} -- TWO at t = 0, 2 and 6, where the "
        f"support contains the separation-two pairs (0,2) and (0,6), and one "
        f"elsewhere -- because the Hodge multiplication in the completion "
        f"extends the support to temporal range two. The word bond is too "
        f"narrow and is not used anywhere in this block. Asserting the census "
        f"flat, the range all-ones, or the localization false fails HERE",
        bool(
            facts.twist_nonzeros == claims["twist_nonzeros"]
            and facts.twist_ranks == claims["twist_ranks"]
            and facts.twist_supports == claims["twist_supports"]
            and facts.twist_ranges == claims["twist_ranges"]
            and facts.twist_locality == claims["twist_locality"]))

    # --- E: the OS-compatible subgroup and the covariance transport ---------
    checks.check(
        "E-THE-OS-COMPATIBLE-SUBGROUP-IS-EXACTLY-THE-REFLECTION-EVEN-ONE",
        f"THE CRITERION IS AN EXACT IFF ON A FINITE FAMILY AND NOT A SAMPLE. "
        f"Of the {EVEN_PATTERN_COUNT} even-shift patterns, EXACTLY "
        f"{facts.reflection_even_commuting} of the {REFLECTION_EVEN_COUNT} "
        f"reflection-even ones (xi_t = xi_(-t)) commute with Ps, and ALL "
        f"{facts.non_reflection_even_failing} of the "
        f"{NON_REFLECTION_EVEN_COUNT} others FAIL to -- both directions "
        f"counted. AND COVARIANCE TRANSPORTS ACROSS THE WHOLE SUBGROUP: for "
        f"all {facts.reflection_even_transporting} of them "
        f"Ps (V Q_s V^T) Ps = (V Q_s V^T)^T at ZERO residual, which is the "
        f"two-line algebra Ps(V Q_s V^T)Ps = V (Ps Q_s Ps) V^T = V Q_s^T V^T = "
        f"(V Q_s V^T)^T made executable for real orthogonal V commuting with "
        f"Ps. AND THE INSTANCE IS NONTRIVIAL, WHICH IS THE ENTIRE POINT: "
        f"V = V_{TRANSPORT_INSTANCE[0]} V_{TRANSPORT_INSTANCE[1]} commutes "
        f"with Ps at {facts.instance_commutator}, its twist differs from Q_s "
        f"at EXACTLY {facts.instance_difference} entries -- so it is NOT in "
        f"the stabilizer -- and the transport identity STILL holds at "
        f"{facts.instance_transport}. OS COMPATIBILITY OF A TWIST IS STRICTLY "
        f"WEAKER THAN EXACT INVARIANCE",
        bool(
            facts.reflection_even_commuting
            == claims["reflection_even_commuting"]
            and facts.non_reflection_even_failing
            == claims["non_reflection_even_failing"]
            and facts.reflection_even_transporting
            == claims["reflection_even_transporting"]
            and facts.instance_commutator == claims["instance_commutator"]
            and facts.instance_difference == claims["instance_difference"]
            and facts.instance_transport == claims["instance_transport"]))

    # --- F: the core action and the invariant sector ------------------------
    checks.check(
        "F-THE-DIAGONAL-INVARIANCE-THEOREM-and-THE-EXPLICIT-INVARIANT-SECTOR",
        f"ONE INVARIANCE THEOREM, ONE EXPLICIT SECTOR, AND ONE DISCLOSURE THAT "
        f"IS AS LOAD-BEARING AS EITHER. In the t-major core order "
        f"{CORE_ORDER} the two core shifts are commuting involutions -- "
        f"W^2 - I at {facts.w_involutive} and [W_1, W_2] at "
        f"{facts.w_commuting}. NEITHER IS INDIVIDUALLY AN INVARIANCE: the two "
        f"defects carry {facts.singleton_defect_nonzeros} nonzero entries at "
        f"EXACT RANKS {facts.singleton_defect_ranks}. THE DIAGONAL ELEMENT IS: "
        f"(W_1 W_2)^T K (W_1 W_2) - K has {facts.diagonal_defect_nonzeros} "
        f"nonzero entries, EXACTLY ZERO, and that is this block's one genuine "
        f"theorem on the OS pairing. THE SECTOR IS THEN EXPLICIT AND EXACT: "
        f"Pi = (I + W_1)(I + W_2)/4 is symmetric at "
        f"{facts.projector_symmetric}, idempotent at "
        f"{facts.projector_idempotent} and of EXACT RANK "
        f"{facts.projector_rank}; its column-space basis is "
        f"{facts.quotient_basis} with B^T B = I_4/2 at determinant "
        f"{facts.basis_gram_determinant}; and the restricted Gram is "
        f"{facts.quotient_gram} with exact leading minors "
        f"{facts.quotient_minors}, sign vector {facts.quotient_signs}, EXACT "
        f"CONGRUENCE INERTIA {facts.quotient_inertia} and basis-independent "
        f"density {facts.quotient_density}. AND NOW THE DISCLOSURE, WHICH IS "
        f"THE ADVERSARIAL CHECK'S C6 AND IS GATED RATHER THAN CONFESSED IN "
        f"PROSE: THE POSITIVITY OF THIS RESTRICTION IS AUTOMATIC. K is "
        f"positive definite and B has full column rank, so "
        f"y^T B^T K B y = (By)^T K (By) > 0 for every nonzero y -- witnessed "
        f"here at {facts.automatic_positivity_witness}. IT IS NOT A NEW "
        f"DYNAMICAL THEOREM, IT IS NOT A GRAVITY THEOREM, AND IT IS NOT "
        f"CLAIMED AS EITHER. WHAT IS NOT AUTOMATIC is the EXPLICIT sector: the "
        f"rank, the basis and the restricted Gram are COMPUTED. AND THE BASIS "
        f"SIGN IS A CONVENTION, MEASURED TO BE ONE: all "
        f"{facts.basis_sign_invariant} of the {BASIS_SIGN_PATTERN_COUNT} sign "
        f"patterns give the SAME four minors, the check's displayed "
        f"representative is the {CHECK_BASIS_SIGN} conjugate "
        f"({facts.check_representative_matches}), and that same representative "
        f"is what this block's core Gram gives after the STAGGERED SITE SIGN "
        f"(-1)^(t+x) ({facts.staggered_congruence_matches}) -- a diagonal "
        f"congruence, so the two independent rebuilds are ONE OBJECT IN TWO "
        f"PHASE CONVENTIONS and neither corrects the other. AND EVERY SCALAR "
        f"ABOVE IS AN EXACT RATIONAL: {facts.exactness_holds}",
        bool(
            facts.w_involutive == claims["w_involutive"]
            and facts.w_commuting == claims["w_commuting"]
            and facts.singleton_defect_nonzeros
            == claims["singleton_defect_nonzeros"]
            and facts.singleton_defect_ranks == claims["singleton_defect_ranks"]
            and facts.diagonal_defect_nonzeros
            == claims["diagonal_defect_nonzeros"]
            and facts.projector_rank == claims["projector_rank"]
            and facts.projector_idempotent == claims["projector_idempotent"]
            and facts.projector_symmetric == claims["projector_symmetric"]
            and facts.quotient_basis == claims["quotient_basis"]
            and facts.basis_gram == claims["basis_gram"]
            and facts.basis_gram_determinant
            == claims["basis_gram_determinant"]
            and facts.quotient_gram == claims["quotient_gram"]
            and facts.quotient_minors == claims["quotient_minors"]
            and facts.quotient_signs == claims["quotient_signs"]
            and facts.quotient_inertia == claims["quotient_inertia"]
            and facts.quotient_density == claims["quotient_density"]
            and facts.basis_sign_invariant == claims["basis_sign_invariant"]
            and facts.check_representative_matches
            == claims["check_representative_matches"]
            and facts.staggered_congruence_matches
            and facts.automatic_positivity_witness
            == claims["restriction_positivity_is_automatic"]
            and facts.exactness_holds))

    # --- G: the exact stabilizer and the second fixture ---------------------
    checks.check(
        "G-THE-EXACT-STABILIZER-BY-EXHAUSTIVE-SWEEP-and-THE-SECOND-FIXTURE",
        f"THE STABILIZER IS COMPUTED AND NOT ESTIMATED, AND IT IS THE "
        f"ADVERSARIAL CHECK'S OWN LEG. All 2^8 = {EVEN_PATTERN_COUNT} even "
        f"patterns are swept exactly, by index lookup and exact rational "
        f"equality with no residual threshold anywhere; the family acts "
        f"FAITHFULLY at {facts.group_order} DISTINCT site permutations, so it "
        f"really is a (Z_2)^8 and not a quotient of one. AND THE STABILIZER OF "
        f"Q_s IS EXACTLY {facts.stabilizer_patterns} -- ORDER "
        f"{facts.stabilizer_order}, generated by the UNIFORM GLOBAL EVEN "
        f"SHIFT. ALL {REFLECTION_EVEN_COUNT} reflection-even patterns are in "
        f"the sweep and only {facts.reflection_even_stabilizers} of them "
        f"stabilize; of the {facts.adjacent_pattern_count} ADJACENT two-slice "
        f"patterns, {facts.adjacent_stabilizers} do. THE MORAL IS THE CHECK'S "
        f"AND IT IS A NUMBER: OS COMPATIBILITY OF A TWIST IS MUCH WEAKER THAN "
        f"MEMBERSHIP IN THE EXACT STABILIZER, {REFLECTION_EVEN_COUNT} against "
        f"{facts.stabilizer_order}, and there is NO LOCAL exact symmetry at "
        f"all. AND IT SURVIVES A SECOND FIXTURE, REBUILT WHOLE at "
        f"{facts.robustness_point}: stabilizer order "
        f"{facts.robustness_stabilizer_order}, W_1 W_2 core defect "
        f"{facts.robustness_diagonal_defect}, projector rank "
        f"{facts.robustness_projector_rank}, core first minor "
        f"{facts.robustness_core_minor_1}, quotient minors "
        f"{facts.robustness_quotient_minors} at signs "
        f"{facts.robustness_quotient_signs} -- WHICH IS TWO POINTS AND NOT A "
        f"WINDOW, and the banner says so",
        bool(
            facts.group_order == claims["group_order"]
            and facts.stabilizer_patterns == claims["stabilizer_patterns"]
            and facts.stabilizer_order == claims["stabilizer_order"]
            and facts.reflection_even_stabilizers
            == claims["reflection_even_stabilizers"]
            and facts.adjacent_pattern_count == claims["adjacent_pattern_count"]
            and facts.adjacent_stabilizers == claims["adjacent_stabilizers"]
            and facts.robustness_stabilizer_order
            == claims["robustness_stabilizer_order"]
            and facts.robustness_diagonal_defect
            == claims["robustness_diagonal_defect"]
            and facts.robustness_projector_rank
            == claims["robustness_projector_rank"]
            and facts.robustness_core_minor_1
            == claims["robustness_core_minor_1"]
            and facts.robustness_quotient_minors
            == claims["robustness_quotient_minors"]
            and facts.robustness_quotient_signs
            == claims["robustness_quotient_signs"]))

    # --- H: the note, the fence and the nsimplify absence -------------------
    scope = facts.scope
    required = claims["required_scope_keys"]
    checks.check(
        "H-THE-NOTE-AT-ITS-FINAL-PATH-THE-N5-FENCE-and-THE-nsimplify-ABSENCE",
        f"THE NOTE MUST EXIST AT ITS FINAL PATH docs/{FINAL_NOTE_NAME} -- "
        f"currently {facts.note_at_final_path} -- and the N5 fence must appear "
        f"in it BYTE-IDENTICALLY with this runner's single-line literal, "
        f"checked as a raw substring and not as a paraphrase: {scope}. THE "
        f"REQUIRED SCOPE-KEY SET IS THE FULL DECLARED SET AND NOT A SUBSET, "
        f"which is what gives drop_n5_fence its teeth. THERE IS NO DRAFT "
        f"FALLBACK PATH ANYWHERE IN THIS RUNNER, so before landing this gate "
        f"fails on note-at-final-path alone and the sweep is run AT LANDING. "
        f"THE FENCE IS AN N5-PREFIXED SINGLE-LINE LITERAL WITH NINE LABELLED "
        f"SECTIONS, and the mutation battery is {len(MUTATIONS)} members "
        f"mapped ONE-PER-FAMILY across {MUTATED_FAMILIES}, EVERY family "
        f"carrying at least one -- family G included, because the adversarial "
        f"check's exhaustive sweep is a claim family here and not a paragraph. "
        f"AND THE BLOCK 186 HAZARD IS HONOURED BY ABSENCE AND MEASURED RATHER "
        f"THAN PROMISED: the nsimplify call carries a rational TOLERANCE and "
        f"maps a small nonzero rational to EXACTLY ZERO, and this block is "
        f"nothing but zeros, ranks and signs -- every residual, every rank, "
        f"every stabilizer decision. This runner calls it "
        f"{facts.nsimplify_calls} times, counted in its own source",
        bool(
            facts.note_at_final_path
            and NOTE_PATH.name == FINAL_NOTE_NAME
            and set(facts.scope) == set(SCOPE_KEYS)
            and required == SCOPE_KEYS
            and all(facts.scope[key] for key in required)
            and facts.scope["n5_verbatim"]
            and facts.nsimplify_calls == claims["nsimplify_calls"]
            and len(MUTATIONS) == 29
            and len(set(MUTATIONS)) == 29
            and set(MUTATION_GATE) == set(MUTATIONS)
            and set(MUTATION_GATE.values()) == set(MUTATED_FAMILIES)
            and set(MUTATED_FAMILIES) == set("ABCDEFGH")
            and N5_FENCE.startswith("N5: ")
            and 9 <= N5_FENCE.count("\n") + 1 <= 12
            and all(N5_FENCE.count(f"\n{name}:") == 1
                    for name in ("per_site", "per_mode", "per_block",
                                 "lattice_wide", "per_scope", "RESULT",
                                 "DECISION_CUT", "TOE"))))
    return checks


# ---------------------------------------------------------------------------
# the measured report: every number the note quotes, printed once
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED -- BLOCK 189, THE SHIFT FAMILY AND THE INVARIANT SECTOR")
    print(f"  elapsed_measurement_ns: {elapsed_ns}")
    print(f"  main_head: {facts.main_head}")
    print(f"  parent_ref: {PARENT_REF}")
    print(f"  parent_commit: {PARENT_COMMIT}")
    print(f"  stale_parent_commit: {STALE_PARENT_COMMIT}")
    print(f"  audit_inputs_readable: {facts.authority.inputs_readable}"
          f" of {len(AUDIT_INPUT_PATHS) - 1} required"
          f" (missing {facts.authority.inputs_missing})")
    print(f"  check_verdict: {CHECK_VERDICT}")
    print()
    print("  THE CONTROL, WHICH IS BLOCK 188'S OWN OBJECT")
    print(f"    fixture (m, c): ({FIXTURE_MASS}, {FIXTURE_SHEAR})"
          f" at unit volume")
    print(f"    rank(Q_s): {facts.action_rank}")
    print(f"    Ps Q_s Ps - Q_s^T residual: {facts.site_covariance_residual}")
    print(f"    PLAIN symmetry defect of Q_s: {facts.site_asymmetry}")
    print(f"    core Gram symmetry residual: {facts.core_symmetry_residual}")
    print(f"    core Gram inertia by congruence: {facts.core_inertia}")
    print(f"    core leading-minor signs: {facts.core_signs}")
    for index, value in enumerate(facts.core_minors, 1):
        print(f"    core leading minor {index}: {value}")
    print()
    print("  THE GRADING SELECTION")
    print(f"    [U_x, d_K]: {facts.odd_dk_nonzeros} entries,"
          f" rank {facts.odd_dk_rank}")
    print(f"    [U_x, d_K] time-pair support: {facts.odd_dk_support}")
    print(f"    grade-projector defects (grades 0,1,2):"
          f" {facts.grade_projector_defects}")
    print(f"    [U_x, Q_s]: {facts.odd_action_nonzeros} entries,"
          f" rank {facts.odd_action_rank}")
    print(f"    U_x Q_s U_x^T - Q_s: {facts.odd_conjugation_nonzeros}")
    print(f"    [U_x, H_s]: {facts.odd_hodge_nonzeros}"
          f"   [U_x, D_s]: {facts.odd_glue_nonzeros}")
    print(f"    global even shift residuals: {facts.global_even_residuals}")
    print()
    print("  THE SINGLE-SLICE TWIST TABLE")
    for label in range(TIME_EXTENT):
        print(f"    t={label}: nnz={facts.twist_nonzeros[label]}"
              f" rank={facts.twist_ranks[label]}"
              f" range={facts.twist_ranges[label]}"
              f" contains_t={facts.twist_locality[label]}"
              f" support={facts.twist_supports[label]}")
    print(f"    exact circular range vector: {facts.twist_ranges}"
          f"  -- RANGE TWO AT t = 0, 2, 6; NOT A NEAREST-SLICE BOND")
    print()
    print("  THE OS-COMPATIBLE SUBGROUP")
    print(f"    reflection-even patterns commuting with Ps:"
          f" {facts.reflection_even_commuting} of {REFLECTION_EVEN_COUNT}")
    print(f"    others FAILING to commute:"
          f" {facts.non_reflection_even_failing}"
          f" of {NON_REFLECTION_EVEN_COUNT}")
    print(f"    reflection-even twists transporting covariance:"
          f" {facts.reflection_even_transporting} of {REFLECTION_EVEN_COUNT}")
    print(f"    instance V_{TRANSPORT_INSTANCE[0]} V_{TRANSPORT_INSTANCE[1]}:"
          f" [V, Ps]={facts.instance_commutator},"
          f" twist-vs-Q_s={facts.instance_difference},"
          f" transport={facts.instance_transport}")
    print()
    print("  THE CORE ACTION AND THE INVARIANT SECTOR")
    print(f"    core order: {CORE_ORDER}")
    print(f"    W^2 - I: {facts.w_involutive}   [W_1, W_2]:"
          f" {facts.w_commuting}")
    print(f"    singleton defects: {facts.singleton_defect_nonzeros} entries"
          f" at ranks {facts.singleton_defect_ranks}")
    print(f"    (W_1 W_2)^T K (W_1 W_2) - K: "
          f"{facts.diagonal_defect_nonzeros} entries")
    print(f"    projector rank {facts.projector_rank},"
          f" idempotent {facts.projector_idempotent},"
          f" symmetric {facts.projector_symmetric}")
    for index, column in enumerate(facts.quotient_basis, 1):
        print(f"    basis b_{index}: {column}")
    print(f"    B^T B determinant: {facts.basis_gram_determinant}")
    for index, row in enumerate(facts.quotient_gram):
        print(f"    B^T K B row {index}: {row}")
    for index, value in enumerate(facts.quotient_minors, 1):
        print(f"    quotient leading minor {index}: {value}")
    print(f"    quotient signs {facts.quotient_signs},"
          f" congruence inertia {facts.quotient_inertia}")
    print(f"    basis-independent density: {facts.quotient_density}")
    print(f"    sign patterns leaving the minors fixed:"
          f" {facts.basis_sign_invariant} of {BASIS_SIGN_PATTERN_COUNT}")
    print(f"    check representative reproduced: "
          f"{facts.check_representative_matches};"
          f" staggered-sign congruence: {facts.staggered_congruence_matches}")
    print(f"    RESTRICTION POSITIVITY IS AUTOMATIC:"
          f" {RESTRICTION_POSITIVITY_IS_AUTOMATIC}"
          f" (witness {facts.automatic_positivity_witness})")
    print()
    print("  THE EXACT STABILIZER, BY EXHAUSTIVE SWEEP")
    print(f"    distinct site permutations in the even family:"
          f" {facts.group_order}")
    print(f"    Stab(Q_s) = {facts.stabilizer_patterns},"
          f" order {facts.stabilizer_order}")
    print(f"    reflection-even patterns that stabilize:"
          f" {facts.reflection_even_stabilizers} of {REFLECTION_EVEN_COUNT}")
    print(f"    adjacent two-slice patterns that stabilize:"
          f" {facts.adjacent_stabilizers} of {facts.adjacent_pattern_count}")
    print(f"    second fixture {facts.robustness_point}:"
          f" stabilizer order {facts.robustness_stabilizer_order},"
          f" W_1W_2 defect {facts.robustness_diagonal_defect},"
          f" projector rank {facts.robustness_projector_rank}")
    print(f"    second fixture core first minor:"
          f" {facts.robustness_core_minor_1}")
    for index, value in enumerate(facts.robustness_quotient_minors, 1):
        print(f"    second fixture quotient minor {index}: {value}")
    print()
    print(f"  nsimplify calls in this runner's own source:"
          f" {facts.nsimplify_calls}")
    print(f"  every measured scalar is an exact rational:"
          f" {facts.exactness_holds}")
    print()
    print("  WHAT IS NOT SUPPLIED, ENUMERATED SO THE ABSENCE IS A COUNT:")
    for structure in UNSUPPLIED_GRAVITY_STRUCTURES:
        print(f"    NOT SUPPLIED: {structure}")
    print()
    print("  READING FENCE, CARRIED FROM THE ADVERSARIAL CHECK'S C6 AND NOT "
          "SOFTENED: the word GAUGE names a CHOSEN FINITE TRANSFORMATION "
          "FAMILY here and nothing more; the word QUOTIENT names an INVARIANT "
          "SUBSPACE of a positive bilinear form and nothing more; the word "
          "LAPSE appears in this block only as a name for something it does "
          "NOT compute. The derived content is the grading classification, the "
          "exact stabilizer, the exact transport criterion, the W_1 W_2 "
          "invariance theorem and the explicit four-dimensional sector. The "
          "positivity of that sector is AUTOMATIC and is disclosed as such. "
          "BLOCK 188 IS NEITHER CORRECTED NOR CONTRADICTED and BLOCK 107'S "
          "STEP 3 IS NOT EXECUTED.")
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
