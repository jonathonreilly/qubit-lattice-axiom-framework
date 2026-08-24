#!/usr/bin/env python3
"""BLOCK 185 -- CURVED OS POSITIVITY VIA THE SEAM-GLUED ACTION.

THE RESULT, AND ITS EXACT SCOPE.  On BLOCK 107's OWN carrier -- the d=2
one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32, with eta_t = 1,
eta_x = (-1)^t, the antiperiodic far-seam edge sign omega_-(3) = -1, the
grade-raising part d_K of that kernel, the link-centered reflection
theta(t) = -1-t, the two-history span Lambda_+ = {0,1} x Z4 and the Block 104
dressing K_ab = conj(G(b, theta a)) -- and AT BLOCK 107'S OWN FIXTURE
m = 9/20, c = 5/13, volume 1 on the reflection-odd step history: THE TWO-HISTORY
GRAM OF A SEAM-GLUED ACTION IS EXACTLY HERMITIAN AND STRICTLY POSITIVE, AND THE
POSITIVITY HOLDS IN A MASS-AND-HISTORY WINDOW WHOSE BOUNDARY IS MEASURED AND
WHOSE CHARACTERIZATION IS OPEN.

  0. THE CONTROLS COME FIRST AND THEY ARE BLOCK 107'S OWN NUMBERS,
     DIGIT-FOR-DIGIT (C).  The flat calibration Q_0 = m I + K_eps reproduces
     Block 107 equation (8) exactly -- the flat two-history Gram is EXACTLY
     Hermitian, its first leading minor is 11457708200/26164592321 and its
     eighth is 25600000000000000000000000000000000 over
     468657842600056497856109298772694726695681, and all eight are strictly
     positive.  Their equation (23) delta_const AND delta_step are reproduced
     exactly on Q_hist = m*H_hist + H_hist*d_K - d_K^T*H_hist.  Their equation
     (29) delta_A02 is reproduced exactly.  NOTHING BELOW IS BELIEVABLE IF
     THESE ARE NOT EXACT, AND THEY ARE EXACT.

  1. THE MEASUREMENT THAT CRACKED IT (D).  The matter reflection defect
     P(-i d_K)P + (-i d_K)^H has EXACTLY 64 NONZERO ENTRIES AND EVERY ONE OF
     THEM IS INTRA-SLICE -- row time equals column time at all 64 -- with
     maximum magnitude 1/2, which is Block 107's equation (28) localized.
     THE TEMPORAL LINKS ARE REFLECTION-EXACT.  The obstruction is the GRADING
     SPLIT: theta flips time parity, so P maps a grade-raising entry into a
     mixture, and the whole defect sits in the spatial (intra-slice) direction.
     THIS IS THE CO-TRANSPORT LESSON A FOURTH TIME, after Block 106's W1,
     Block 182's T2 and Block 183's grading correction.

  2. THE CONSTRUCTION, AND IT IS DERIVED RATHER THAN DRESSED (E).  Let A be
     the d_K entries with BOTH endpoints' times in the positive half {0,1,2,3},
     PLUS every d_K entry on the two seam edge-time pairs {3,4} and {7,0} --
     the physical half plus its seams, and nothing else.  Put D = A - P A P,
     which carries EXACTLY 72 nonzero entries.  Three structural properties
     are measured, not assumed: D IS P-ODD (P D P + D = 0); D EQUALS d_K
     ENTRYWISE wherever both times lie in {0,1,2,3}, so the physical dynamics
     of the positive half is UNTOUCHED; and with the A02-image geometry
     H_image, which is P-EVEN (P H_image P = H_image, Block 107 equation (27)),
     the glued action Q_glued = m H_image + H_image D - D^T H_image satisfies
     P Q_glued P = Q_glued^T EXACTLY.

  3. THE RESULT, WITH ITS STRUCTURAL HALF SCOPED AS THE ADVERSARIAL CHECK
     SCOPED IT (F).  P Q_glued P = Q_glued^T, PLUS THE CONSTRUCTION'S EXACT
     REALITY -- every entry of Q_glued and of its inverse is real -- PLUS
     invertibility, gives an EXACTLY HERMITIAN two-history Gram, delta = 0.
     THE REALITY CLAUSE IS LOAD-BEARING AND IS NOT DECORATION: the bare
     implication is FALSE, and the one-dimensional counterexample P = [1],
     Q = [i] -- which satisfies P Q P = Q^T and whose Gram is [i], not
     Hermitian -- IS BUILT AND MEASURED IN THE SAME RUN.  AND THE GENUINELY
     NEW NUMERICAL CONTENT IS THE STRICT POSITIVITY: all eight leading
     principal minors are strictly positive, the first being
     4465961414671029642827787914210419072833144728317065801107200 over
     8932040001245962023277146780748464953706237777456506835365883, which is
     CALIBRATION rather than the claim.  Nothing about transpose covariance,
     reality or invertibility forces positivity, and positivity is what an OS
     statement needs.

  4. THE NECESSITY OF THE INGREDIENTS, WITHIN THE TESTED FAMILY (G).  Every
     ingredient is attacked by rebuilding everything by the same code with
     exactly one ingredient changed.  THE SEAMS: drop both and all eight
     minors are exactly ZERO; keep only the NEAR seam {7,0} and the sign
     vector is (+,+,+,+,-,+,-,+), INDEFINITE; keep only the FAR seam {3,4}
     and it is (+,+,+,+,0,0,0,0), DEGENERATE.  AND THE PRECISION MATTERS:
     the zero-, one- and two-seam A - P A P variants ALL have delta = 0, so
     HERMITICITY IS SEAM-INSENSITIVE and BOTH SEAMS ARE NECESSARY ONLY FOR
     STRICT POSITIVITY.  THE PARITY: the P-EVEN variant D' = A + P A P fails
     transpose covariance at maximum norm EXACTLY 313/288 and its Gram defect
     is nonzero.  THE GEOMETRY: the raw H(-c) negative half with the SAME D
     fails covariance at maximum norm EXACTLY 65/576 -- Block 107's own
     equation (17) channel residual, reappearing -- and its Gram defect is
     nonzero.  THESE ESTABLISH THE INGREDIENTS' NECESSITY WITHIN THE
     ENUMERATED VARIANTS AND NOT THAT D = A - P A P IS THE ONLY CONCEIVABLE
     CONSTRUCTION: it is FORCED WITHIN THE TESTED FAMILY, and the P-odd
     extension is what the structural proof forces once the independent-half
     data are fixed.

  5. THE WINDOW, WHICH THE ADVERSARIAL CHECK MEASURED AND WHICH NARROWS THE
     SCOPE (G).  POSITIVITY IS MASS-WINDOWED: at m = 1/3 all eight minors are
     positive, and at m = 2 the sign vector is (+,+,+,+,+,-,+,-) -- covariance
     and Hermiticity survive both, POSITIVITY DOES NOT.  POSITIVITY IS
     HISTORY-WINDOWED: the constant-in-x step at c = 3/5 is positive 8 of 8,
     and the x-alternating reflection-odd history c(t,x) = c_t (-1)^x at
     c = 3/5 is Hermitian at delta = 0 with sign vector (+,+,+,+,+,+,-,-).
     HERMITICITY IS ROBUST IN BOTH DIRECTIONS AND POSITIVITY IS NOT.  The
     window's characterization is OPEN and is named as a next leg; in the
     mass direction its boundary lies in (9/20, 2].

  6. AND BLOCK 107'S TWO OPEN ITEMS CLOSE AT THIS SCOPE WITH NO DRESSING AT
     ALL.  Their Section 7 dressing machinery -- the eight-element diagonal
     class D_8, the 32-parameter cell-local class with rank 24 and an
     eight-dimensional kernel, and the fixture-tuned coefficient vector whose
     admissibility and action-derived selection they left open -- IS
     SUPERSEDED AT THIS SCOPE.  D is canonical given A, and A is the physical
     half plus its seams.  NO DRESSING IS APPLIED ANYWHERE IN THIS RUNNER.

WHAT IS NOT CLAIMED, STATED ONCE: NO m-GENERALITY -- positivity is measured at
m = 9/20 and m = 1/3 and MEASURED TO FAIL at m = 2; NO HISTORY-GENERALITY --
positivity is measured on two constant-in-x steps and MEASURED TO FAIL on the
x-alternating one; NO CHARACTERIZATION OF THE WINDOW those four points bound;
NO SECTION-FRAME PORT -- this is BLOCK 107'S carrier, which is NOT the Block
128 chart family the Blocks 181-184 section frame lives on; NO GRAVITY
CONSTRAINT QUOTIENT; and THE READING THAT THE NEGATIVE HALF IS THE DUAL-FRAME
DYNAMICS IS A READING, gated as a declared constant and never a theorem.
BLOCK 107'S RAW DELTA STANDS UNTOUCHED: their nonzero defects are reproduced
here exactly, and what is Hermitian is the SEAM-GLUED action, a different
object from the one they measured.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 184 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the eight audit
     inputs readable, and the stale pin verified to be a REAL ancestor of HEAD
     that carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: six imposed objects,
     ZERO registered and ZERO adopted, with m-generality, history-generality,
     the section-frame port, the constraint quotient and the dual-frame
     reading all declared NOT CLAIMED as measured constants.
  C  THE CONTROLS: four citation pins read from the two primary bodies, then
     Block 107's flat calibration (Hermitian, first and eighth minors, all
     eight positive), their equation (23) delta_const and delta_step with
     their equation (24) ordering, and their equation (29) delta_A02.
  D  THE DEFECT LOCALIZATION: 64 nonzeros, ALL intra-slice, max magnitude 1/2.
  E  THE STRUCTURE: H_image P-even against the SIGNED-cell-map neighbour that
     fails in the same run, D P-odd at exactly 72 entries, D == d_K on the
     interior-positive entries, and P Q_glued P = Q_glued^T.
  F  THE RESULT: the exact reality certificate AND the one-dimensional
     counterexample that shows why it is needed, the Hermiticity defect at
     exactly 0, all eight leading minors strictly positive, and the first
     minor's exact rational as calibration.
  G  THE NECESSITY CONTROLS AND THE WINDOW: the three seam variants with
     their sign vectors and their common delta = 0, the P-even and raw-image
     canonicity attacks at 313/288 and 65/576, and the four window points
     m = 1/3, m = 2, the c = 3/5 step and the x-alternating history.
  H  the note at its final path and the N5 fence, byte-identical.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: sixteen declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_m_generality, claim_dual_frame_theorem
    C  break_flat_minor, break_delta_step
    D  break_defect_count
    E  break_p_odd, break_transpose_covariance
    F  break_gram_delta, break_first_minor
    G  break_no_seam_control, break_second_mass_window,
       break_x_alternating_window
    H  drop_n5_fence
  THREE OF THE SIXTEEN GUARD WHAT THE ADVERSARIAL CHECK SUPPLIED:
  break_second_mass_window asserts positivity at m = 2, break_x_alternating_
  window asserts it on the x-alternating history, and both must FAIL -- they
  are the mutations that stop a reader from taking one fixture's positivity
  for a general one.
  BEFORE LANDING GATE H ALREADY FAILS AT BASELINE, on note-at-final-path alone,
  so drop_n5_fence cannot flip it and THE SWEEP IS RUN AT LANDING, once the note
  sits at docs/ and the baseline is 8 of 8 by family.

RUNNING
  python3 scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation break_second_mass_window

NOTES FOR THE LANDING AGENT
  1. NOTHING from any scratchpad is imported OR READ.  THIS BLOCK'S MACHINERY
     IS NEW: Block 107's carrier is NOT the Block 128 chart family, so the
     staggered kernel with its antiperiodic edge sign, the grade projectors,
     the raising part d_K, the site reflection, the offset permutation P_4, the
     restricted raising set A, the derived D and the glued action are ALL BUILT
     DIRECTLY HERE from Block 107's displayed equations.  The LANDED Block 128
     runner is imported for EXACTLY TWO objects -- cover_embedding() and the
     Block 105 module's shear_hodge() -- and for nothing else.
  2. EVERY CHECK IS EXACT.  sympy Rational and Integer arithmetic only; no
     float enters any measured object and no tolerance is used anywhere.  The
     volume is sp.Integer(1) and every shear is passed through sp.nsimplify,
     because `1/volume` at a Python int would silently inject a float into the
     Hodge block and every number below would become a decimal.
  3. The N5 fence appears byte-identically in the note; gate H checks it as a
     raw substring.
  4. PARENT_COMMIT is the Block 184 tip and PARENT_REF resolves to it; nothing
     needs sed, and CURRENT_MAIN was carried forward from the Block 184 runner
     and re-resolved at draft time.
  5. The stale pin is the Block 183 tip, a real ancestor of HEAD that predates
     Block 184 and carries NEITHER Block 184 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  6. THE ADVERSARIAL CHECK IS FOLDED AND ITS TWO NARROWINGS ARE GATED, NOT
     NARRATED.  Its verdict was CONFIRMED-WITH-CORRECTION.  It confirmed C1-C4
     exactly, including all eight minors and the three curved controls; it ran
     the canonicity attacks; it supplied the FOUR WINDOW POINTS, which are the
     block's scope narrowing and which gate G now measures directly; and it
     supplied the REALITY scoping of the structural implication, which gate F
     now measures directly, counterexample included.  NO PLACEHOLDER SLOT
     REMAINS IN THIS RUNNER.
  7. TWO DEAD ENDS ARE RECORDED IN THE NOTE AS PROCESS AND NEITHER IS A LANDED
     CORRECTION: the naive interior-edge glue (broke nilpotency and left the
     defect unchanged) and the one-sided xpar Gram dressing (WORSENED the flat
     calibration, its defect-split assumption unmeasured).  Both were caught
     inside the solve by the control that was measured alongside them.  A third
     in-solve catch IS gated: the SIGNED cell-map guess for the negative-half
     image fails Block 107 equation (27) in the same run, and gate E measures
     that failure.
  8. Re-run at landing; gate H should then pass, the battery should be 8/8 by
     family, and the sixteen-mutation sweep should be run then.
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

# THE MACHINERY IMPORT, LANDED, AND DELIBERATELY THIN.  Block 107's carrier is
# NOT the Block 128 chart family, so almost nothing transfers: the LANDED Block
# 128 runner is imported for EXACTLY TWO objects -- cover_embedding(), whose
# corner order IS the form basis (1, dx, dt, dx^dt), and the Block 105 module it
# re-exports, from which shear_hodge() is read.  Everything else in this runner
# is built directly from Block 107's displayed equations.  NOTHING from any
# scratchpad is imported or read anywhere.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 184 is the commit this block's branch
# is cut from, and its note and its runner are the pair that distinguishes the
# parent pin from the stale pin: both exist at PARENT_COMMIT and NEITHER exists
# at STALE_PARENT_COMMIT.
BLOCK184_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK184_RUNNER = (
    "scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK184_NOTE, BLOCK184_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "d106984d47563488da3bfb339f86da86757d29ce",   # Block 184 note
    "3f6f1b4d3f509aa2f4b5bcd87594d65cf32184e7",   # Block 184 runner
)
# THE REFLECTION GRANDPARENT, whose two artifacts are the STALE pin's tell.
BLOCK183_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK183_RUNNER = (
    "scripts/admissibility_dirac_kahler_derived_reflection_seam_dual_2026_08_24.py"
)
# THE CONVENTION AUTHORITY.  Every convention, every control number and both
# open items this block closes at fixture scope are read from Block 107's
# PRIMARY BODY and never from a summary of it.
BLOCK107_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_"
    "THEOREM_NOTE_2026-08-15.md"
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_derived_reflection_seam_dual_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
# THE BLOCK'S OWN NOTE is the one audit input gate A does NOT require readable,
# because it does not exist until landing and gate H is the gate that owns it.
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 184 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 184 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block184-"
              "temporal-link-extraction-20260824")
PARENT_COMMIT = "1702e73876839f0ba01f5ff28bfe26ed5d370987"
# The Block 183 tip: a real ancestor of HEAD that predates Block 184 and
# therefore carries NEITHER Block 184 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "b1648d61971b7cc10bdf61749211bad8b97f9935"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_m_generality",
    "claim_dual_frame_theorem",
    "break_flat_minor",
    "break_delta_step",
    "break_defect_count",
    "break_p_odd",
    "break_transpose_covariance",
    "break_gram_delta",
    "break_first_minor",
    "break_no_seam_control",
    "break_second_mass_window",
    "break_x_alternating_window",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_m_generality": "B",
    "claim_dual_frame_theorem": "B",
    "break_flat_minor": "C",
    "break_delta_step": "C",
    "break_defect_count": "D",
    "break_p_odd": "E",
    "break_transpose_covariance": "E",
    "break_gram_delta": "F",
    "break_first_minor": "F",
    "break_no_seam_control": "G",
    "break_second_mass_window": "G",
    "break_x_alternating_window": "G",
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
        # THE STALE LEG.  At the Block 183 tip NEITHER Block 184 artifact
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
# THE IMPOSED OBJECTS OF THIS BLOCK, declared as a literal so the banner is a
# measured object and not only prose.  NONE of them is registered or adopted.
IMPOSED_OBJECTS = (
    "BLOCK 107's carrier and conventions, REBUILT HERE from its displayed equations and imported from nothing: the d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32 with eta_t = 1 and eta_x = (-1)^t, the antiperiodic kernel K_eps of its equation (3) carrying the far-seam edge sign omega_-(3) = -1, the grade-raising part d_K of its equation (4), the link-centered site reflection theta(t) = -1-t, the two-history span Lambda_+ = {0,1} x Z4 ordered ((0,0)..(0,3),(1,0)..(1,3)), and the Block 104 dressing K_ab = conj(G(b, theta a)) of its equation (7)",
    "THE FIXTURE, taken exactly as Block 107 displayed it: m = 9/20, c = 5/13, volume 1, and the reflection-odd step history (c_0..c_7) = (c, c, c, 0, -c, -c, -c, 0) of its equation (19), whose two straddling anchors are flat by antisymmetry -- together with the THREE FURTHER FIXTURE POINTS the adversarial check supplied, m = 1/3, m = 2 and the c = 3/5 step, and the x-alternating reflection-odd history c(t,x) = c_t (-1)^x at c = 3/5",
    "THE COMPLETION CONVENTION Q(H, d) = m*H + H*d - d^T*H, Block 107's equation (21), used unchanged for the flat calibration, for both history controls, for the A02-image control, for the glued action and for every necessity variant",
    "THE A02-IMAGE GEOMETRY H_image: Block 107's equation (15) UNSIGNED offset permutation P_4 applied to the negative-half blocks at the anchor reflection theta_A(t) = -2-t, which is their equation (27) construction and which is P-EVEN",
    "THE GLUED ACTION, WHICH IS THIS BLOCK'S OWN OBJECT: the restricted raising set A -- the d_K entries with both endpoint times in the positive half {0,1,2,3} PLUS every d_K entry on the two seam edge-time pairs {3,4} and {7,0} -- the derived D = A - P A P at 72 nonzero entries, and Q_glued = m*H_image + H_image*D - D^T*H_image",
    "Block 128's LANDED cover_embedding(), whose corner order IS the form basis (1, dx, dt, dx^dt), and the LANDED Block 105 shear_hodge() block it re-exports: THE ONLY TWO OBJECTS IMPORTED BY THIS RUNNER",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS rather than prose, so
# the B mutations bite on an object.  ALL FIVE ARE FALSE AND STAY FALSE.
# Positivity is measured at four points and MEASURED TO FAIL at two of them, the
# carrier is Block 107's and NOT the Blocks 181-184 section frame, no constraint
# quotient is formed, and THE NEGATIVE HALF BEING THE DUAL-FRAME DYNAMICS IS A
# READING.
M_GENERALITY_CLAIMED = False
HISTORY_GENERALITY_CLAIMED = False
SECTION_FRAME_PORT_CLAIMED = False
CONSTRAINT_QUOTIENT_CLAIMED = False
DUAL_FRAME_READING_CLAIMED = False

# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.  THE FIVE BLOCK
# 107 CONTROL NUMBERS ARE COPIED FROM THEIR PRIMARY BODY, equations (8), (23)
# and (29), and are reproduced here digit-for-digit by independent code.
ZERO_RESIDUAL = 0
TIME_EXTENT = 8
SPACE_EXTENT = 4
MINOR_COUNT = 8
FLAT_FIRST_MINOR = sp.Rational(11457708200, 26164592321)
FLAT_LAST_MINOR = sp.Rational(
    25600000000000000000000000000000000,
    468657842600056497856109298772694726695681)
DELTA_CONST = sp.Rational(
    14956538493029334947329841745598883128206218860908000,
    126263516440889155637290868049543261980212777042759973)
DELTA_STEP = sp.Rational(
    1968254788609376403972598115871411702171024000,
    61391349876435377016600254323619839508354485363)
DELTA_A02 = sp.Rational(
    4073726618187763151174731250983212188681424000,
    61391349876435377016600254323619839508354485363)
# THE DEFECT LOCALIZATION, which is the measurement that cracked the block.
DEFECT_NONZEROS = 64
DEFECT_MAX_MAGNITUDE = sp.Rational(1, 2)
# THE GLUE'S OWN CENSUS.
GLUE_NONZEROS = 72
# THE RESULT.  THE FIRST MINOR IS CALIBRATION, NOT THE CLAIM: the claim is the
# strict positivity of all eight, and this number pins which object produced it.
GLUED_FIRST_MINOR = sp.Rational(
    4465961414671029642827787914210419072833144728317065801107200,
    8932040001245962023277146780748464953706237777456506835365883)
POSITIVE_SIGNS = (1,) * MINOR_COUNT

# THE WINDOW, AS THE ADVERSARIAL CHECK MEASURED IT.  Hermiticity survives every
# point below; POSITIVITY DOES NOT, and these four points are what turns "the
# Gram is positive" into "the Gram is positive INSIDE A WINDOW".
SECOND_MASS = sp.Rational(1, 3)             # positive, 8 of 8
THIRD_MASS = sp.Integer(2)                  # NOT positive
THIRD_MASS_SIGNS = (1, 1, 1, 1, 1, -1, 1, -1)
SECOND_HISTORY_SHEAR = sp.Rational(3, 5)    # constant-in-x step: positive
X_ALTERNATING_SIGNS = (1, 1, 1, 1, 1, 1, -1, -1)
# The mass-direction window boundary is bracketed and NOT characterized.
MASS_WINDOW_BRACKET = "(9/20, 2]"

# THE CANONICITY ATTACKS, AS THE ADVERSARIAL CHECK RAN THEM.  Each rebuilds
# everything by the same code with EXACTLY ONE ingredient changed.
NEAR_SEAM_ONLY_SIGNS = (1, 1, 1, 1, -1, 1, -1, 1)     # {7,0} only: INDEFINITE
FAR_SEAM_ONLY_SIGNS = (1, 1, 1, 1, 0, 0, 0, 0)        # {3,4} only: DEGENERATE
NO_SEAM_SIGNS = (0,) * MINOR_COUNT                    # neither: DEAD
P_EVEN_COVARIANCE_MAXNORM = sp.Rational(313, 288)
# BLOCK 107 EQUATION (17), REAPPEARING: the raw H(-c) negative half fails the
# covariance at exactly the shear-channel residual they measured.
RAW_IMAGE_COVARIANCE_MAXNORM = sp.Rational(65, 576)

# THE CITATION PINS, read from the PRIMARY BODIES so this block's conventions,
# the open items it closes and the hand-off it answers all have a measured
# referent and are never a recollection.  Block 107's own not-claimed sentence
# for curved OS positivity is the gap this block closes at fixture scope; its
# dressing-selection sentence is the obligation this block supersedes by needing
# no dressing at all; its no-go firewall is the sentence that made the closure
# admissible to attempt.  Block 184's own hand-off names the Gram as the leg.
B107_CURVED_OS_PIN = (
    "curved OS positivity, the actual ADM/history transporter completion")
B107_DRESSING_PIN = "involution admissibility and action-derived selection."
B107_NOT_A_NOGO_PIN = "This is not a curved OS no-go."
B184_GRAM_PIN = "NO TWO-HISTORY GRAM IS BUILT.** It is the next leg."

# THE H-FAMILY SCOPE KEYS.  The set is required WHOLE by gate H, which is what
# gives drop_n5_fence its teeth: dropping a key from the required set makes the
# required set differ from the declared set and the gate fails.
SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float and no tolerance anywhere
# ---------------------------------------------------------------------------
def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is involved
    at any point."""
    return nonzero_entries(sp.expand(matrix))


def max_norm(matrix: sp.MatrixBase) -> object:
    """||.||_max, exactly: the largest entry magnitude, Block 107's own norm."""
    expanded = sp.expand(matrix)
    return max(sp.Abs(expanded[i, j])
               for i in range(expanded.rows) for j in range(expanded.cols))


def leading_minors(matrix: sp.Matrix) -> tuple:
    """THE EIGHT LEADING PRINCIPAL MINORS, exact rational determinants by the
    Berkowitz algorithm: no eigenvalue estimate, no numerical factorization and
    no tolerance enters the decision."""
    return tuple(matrix[:size, :size].det(method="berkowitz")
                 for size in range(1, matrix.rows + 1))


def minor_signs(minors: tuple) -> tuple:
    """THE SIGN VECTOR, in {+1, 0, -1}.  A vector of eight +1 is the strict
    positivity statement; anything else is exactly how it fails."""
    return tuple(int(sp.sign(value)) for value in minors)


def is_exact_real(value: object) -> bool:
    expression = sp.sympify(value)
    return bool(expression.is_rational and not expression.is_Float)


# ---------------------------------------------------------------------------
# BLOCK 107's CARRIER, BUILT DIRECTLY.  Nothing in this section comes from the
# Block 128 chart family; every object is Block 107's own displayed equation.
# ---------------------------------------------------------------------------
MASS = sp.Rational(9, 20)
SHEAR = sp.Rational(5, 13)
COVER_SIZE = TIME_EXTENT * SPACE_EXTENT
# BLOCK 107 EQUATION (15): the offset permutation, an UNSIGNED corner swap.  IT
# IS UNSIGNED, and gate E measures what the signed guess costs.
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])
# THE SIGNED NEIGHBOUR, built ONLY to be measured failing: the cell map whose
# square is -I.  It is not used to build anything this block claims.
SIGNED_CELL_MAP = sp.Matrix([[0, 0, -1, 0],
                             [0, 0, 0, -1],
                             [1, 0, 0, 0],
                             [0, 1, 0, 0]])
# THE TWO SEAM EDGE-TIME PAIRS.  {3,4} is the FAR seam, the one carrying
# omega_-(3) = -1; {7,0} is the NEAR seam, an ordinary action edge.
FAR_SEAM = frozenset({3, 4})
NEAR_SEAM = frozenset({7, 0})
BOTH_SEAMS = (FAR_SEAM, NEAR_SEAM)
POSITIVE_TIMES = (0, 1, 2, 3)
# BLOCK 107's displayed two-history span, in its displayed order.
LAMBDA_PLUS = tuple((t, x) for t in (0, 1) for x in range(SPACE_EXTENT))


def site_index(time_coordinate: int, space_coordinate: int) -> int:
    """idx(t,x) = (t mod 8)*4 + (x mod 4): time first, exactly Block 107's
    ordering, and identical to the LANDED Block 128 cover_index."""
    return ((time_coordinate % TIME_EXTENT) * SPACE_EXTENT
            + space_coordinate % SPACE_EXTENT)


def staggered_kernel(antiperiodic: bool = True) -> sp.Matrix:
    """BLOCK 107 EQUATION (3), BUILT DIRECTLY.  eta_t = 1 and eta_x = (-1)^t;
    the temporal edge sign omega is used ONLY on a forward temporal edge, and
    for antiperiodic closure it is -1 at t = 3 -- the FAR reflection seam
    3 <-> -4 -- and +1 everywhere else, which is their equation (2)."""
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
    """deg(t,x) = t%2 + x%2, the staggered form degree on the fine carrier."""
    return time_coordinate % 2 + space_coordinate % 2


def grade_projector(grade: int) -> sp.Matrix:
    return sp.diag(*[1 if site_degree(t, x) == grade else 0
                     for t in range(TIME_EXTENT)
                     for x in range(SPACE_EXTENT)])


def raising_part(kernel: sp.Matrix) -> sp.Matrix:
    """BLOCK 107 EQUATION (4): d_K = P1 K P0 + P2 K P1, the grade-raising part,
    for which K = d_K - d_K^T and d_K^2 = 0.  Both are gated in family C."""
    p0, p1, p2 = (grade_projector(g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def site_reflection() -> sp.Matrix:
    """P e_(t,x) = e_(theta(t),x) with theta(t) = -1-t mod 8: Block 107's
    link-centered time reflection, a pure site permutation."""
    matrix = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            matrix[site_index((-1 - time) % TIME_EXTENT, space),
                   site_index(time, space)] = 1
    return matrix


def shear_block(shear: object) -> sp.Matrix:
    """The LANDED Block 105 shear Hodge at VOLUME ONE, read through Block 128.
    The volume is sp.Integer(1) and the shear passes through nsimplify: a
    Python int would make `1/volume` a FLOAT and silently decimalize the block,
    the Hodge, the action, the Gram and every number in this runner."""
    return b128.block105.shear_hodge(sp.nsimplify(shear), sp.Integer(1))


def step_history(shear: object) -> tuple:
    """BLOCK 107 EQUATION (19): the reflection-odd step on time representatives
    -4..3 re-indexed to t = 0..7, with the two straddling anchors t = 3 and
    t = 7 FLAT by antisymmetry rather than by prescription."""
    shear = sp.nsimplify(shear)
    return (shear, shear, shear, sp.Integer(0),
            -shear, -shear, -shear, sp.Integer(0))


def constant_in_x(history: tuple):
    """The field of Block 107's Section 6: c depends on the anchor row only."""
    return lambda time, space: history[time % TIME_EXTENT]


def x_alternating(history: tuple):
    """THE ADVERSARIAL CHECK'S SECOND HISTORY: c(t,x) = c_t (-1)^x.  It is still
    reflection-odd in t -- the same step profile -- and it is the point at which
    positivity is MEASURED TO FAIL while Hermiticity survives."""
    return lambda time, space: (history[time % TIME_EXTENT]
                                * (-1) ** (space % SPACE_EXTENT))


def hodge_from_cells(cell_block) -> sp.Matrix:
    """BLOCK 107 EQUATION (20): H = (1/4) sum_n E_n B(n) E_n^dagger over all 32
    anchors, with the LANDED Block 128 cover_embedding as E_n and the overlap
    weight 1/4 they display.  The block is a function of the FULL anchor (t,x),
    which is what lets the x-alternating history be measured by the same code."""
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            embedding = b128.cover_embedding(time, space)
            result += embedding * cell_block(time, space) * embedding.T / 4
    return sp.expand(result)


def plain_cells(field):
    """The raw per-anchor blocks H(c(t,x), 1) -- the negative half keeps its
    shear in the (dx,dt) channel, which is the geometry Block 107 measured."""
    return lambda time, space: shear_block(field(time, space))


def image_cells(field, cell_map: sp.Matrix = OFFSET_PERMUTATION):
    """BLOCK 107's A02-IMAGE HALF, their equation (27) construction.  The
    POSITIVE half t = 0..3 carries its plain blocks; the NEGATIVE half t = 4..7
    carries the IMAGE block cell_map * H(c(theta_A(t), x), 1) * cell_map^T at
    the anchor reflection theta_A(t) = -2-t of their equation (14).  With the
    UNSIGNED equation (15) permutation this is P-EVEN; gate E measures both."""
    def block(time, space):
        if time in POSITIVE_TIMES:
            return shear_block(field(time, space))
        reflected = (-2 - time) % TIME_EXTENT
        return sp.expand(cell_map * shear_block(field(reflected, space))
                         * cell_map.T)
    return block


def completion(hodge: sp.Matrix, raising: sp.Matrix, mass: object) -> sp.Matrix:
    """BLOCK 107 EQUATION (21): Q = m*H + H*d - d^T*H.  Used UNCHANGED for the
    flat calibration, both history controls, the A02-image control, the glued
    action and every necessity variant, so no comparison below is between
    different conventions."""
    return sp.expand(mass * hodge + hodge * raising - raising.T * hodge)


REFLECTION_OF = {anchor: site_index((-1 - anchor[0]) % TIME_EXTENT, anchor[1])
                 for anchor in LAMBDA_PLUS}


def two_history_gram(action: sp.Matrix) -> sp.Matrix:
    """BLOCK 107 EQUATION (7)/(22): K_ab = conj(G(b, theta a)) on Lambda_+ with
    G = Q^-1, in their displayed span order."""
    inverse = action.inv()
    gram = sp.zeros(len(LAMBDA_PLUS), len(LAMBDA_PLUS))
    for row, anchor in enumerate(LAMBDA_PLUS):
        for column, partner in enumerate(LAMBDA_PLUS):
            gram[row, column] = sp.conjugate(
                inverse[site_index(*partner), REFLECTION_OF[anchor]])
    return sp.expand(gram)


def hermiticity_defect(gram: sp.Matrix) -> object:
    """BLOCK 107 EQUATION (22): delta = ||K - K^dagger||_max, the exact maximum
    entry magnitude.  Zero is the exact Hermiticity statement."""
    return max_norm(gram - gram.H)


def restricted_raising(raising: sp.Matrix, seams: tuple) -> sp.Matrix:
    """A: the d_K entries with BOTH endpoint times in the positive half
    {0,1,2,3}, PLUS every d_K entry on each supplied seam edge-time pair.  THE
    PHYSICAL HALF PLUS ITS SEAMS AND NOTHING ELSE.  The seam tuple is what the
    necessity controls vary: both, near only, far only, neither."""
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            keep = row_time in POSITIVE_TIMES and column_time in POSITIVE_TIMES
            if frozenset({row_time, column_time}) in seams:
                keep = True
            if keep:
                result[row, column] = raising[row, column]
    return result


@dataclass(frozen=True)
class Variant:
    """One rebuilt point: the covariance residual, the Hermiticity defect, the
    eight leading minors and their sign vector.  EVERY necessity control and
    EVERY window point below is one of these, produced by the SAME code."""
    covariance_max_norm: object
    covariance_residual: int
    delta: object
    minors: tuple
    signs: tuple
    invertible: bool


def build_variant(mass: object, cells, glue: sp.Matrix,
                  reflection: sp.Matrix) -> Variant:
    hodge = hodge_from_cells(cells)
    action = completion(hodge, glue, mass)
    covariance = sp.expand(reflection * action * reflection - action.T)
    invertible = action.det(method="berkowitz") != 0
    if not invertible:
        return Variant(max_norm(covariance), nonzero_entries(covariance),
                       None, (), (), False)
    gram = two_history_gram(action)
    minors = leading_minors(gram)
    return Variant(max_norm(covariance), nonzero_entries(covariance),
                   hermiticity_defect(gram), minors, minor_signs(minors), True)


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
    reads Block 107's and Block 184's notes through this and through nothing
    else -- the Block 182 process rule, that every citation is checked against
    the primary body and never against a summary."""
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except OSError:
        return ""


# ---------------------------------------------------------------------------
# THE N5 FENCE.  Single-line literal with \n separators; it appears
# BYTE-IDENTICALLY in the note and gate H checks it as a raw substring.
# ---------------------------------------------------------------------------
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 107's carrier and conventions rebuilt from their displayed equations (the d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32 with eta_t = 1 and eta_x = (-1)^t, the antiperiodic kernel K_eps of eq (3) carrying omega_-(3) = -1 on the FAR seam, the grade-raising d_K of eq (4), the link-centered site reflection theta(t) = -1-t, the span Lambda_+ = {0,1} x Z4 and the Block 104 dressing K_ab = conj(G(b, theta a)) of eq (7)), THE FIXTURE m = 9/20 and c = 5/13 at volume 1 on the reflection-odd step history (c,c,c,0,-c,-c,-c,0) of eq (19) TOGETHER WITH THE THREE FURTHER POINTS THE ADVERSARIAL CHECK SUPPLIED (m = 1/3, m = 2, the c = 3/5 step, and the x-alternating reflection-odd history c(t,x) = c_t (-1)^x), THE COMPLETION CONVENTION Q = m*H + H*d - d^T*H of eq (21), THE A02-IMAGE GEOMETRY built with the UNSIGNED offset permutation P_4 of eq (15) at the anchor reflection theta_A(t) = -2-t, THE GLUED ACTION Q_glued = m*H_image + H_image*D - D^T*H_image with A the positive-half raising entries plus the two seam edge-time pairs {3,4} and {7,0} and D = A - P A P at 72 nonzero entries, and the LANDED Block 128 cover_embedding() and Block 105 shear_hodge() -- THE ONLY TWO OBJECTS IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from Block 107's primary body and the two landed helpers and from NOTHING in any scratchpad. NO m-GENERALITY IS CLAIMED, positivity being MEASURED TO FAIL at m = 2; NO HISTORY-GENERALITY IS CLAIMED, positivity being MEASURED TO FAIL on the x-alternating history; NO CHARACTERIZATION OF THE WINDOW those points bound is claimed; NO PORT TO THE BLOCKS 181-184 SECTION FRAME IS CLAIMED, Block 107's carrier being a DIFFERENT carrier from the Block 128 chart family; NO GRAVITY CONSTRAINT QUOTIENT IS FORMED; AND THE STATEMENT THAT THE NEGATIVE HALF IS THE DUAL-FRAME DYNAMICS IS A READING AND NOT A THEOREM. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE CONTROLS COME FIRST AND THEY ARE BLOCK 107'S OWN NUMBERS, DIGIT-FOR-DIGIT. The flat calibration Q_0 = m I + K_eps gives a two-history Gram that is EXACTLY Hermitian with all EIGHT leading principal minors strictly positive, the first EXACTLY 11457708200/26164592321 and the eighth EXACTLY 25600000000000000000000000000000000/468657842600056497856109298772694726695681 -- Block 107 equation (8), reproduced by independent code. Their equation (23) is reproduced EXACTLY on both histories: delta_const = 14956538493029334947329841745598883128206218860908000/126263516440889155637290868049543261980212777042759973 and delta_step = 1968254788609376403972598115871411702171024000/61391349876435377016600254323619839508354485363, both NONZERO, both STANDING, and satisfying their equation (24) ordering 0 < 3*delta_step < delta_const as re-measured here. Their equation (29) is reproduced EXACTLY: delta_A02 = 4073726618187763151174731250983212188681424000/61391349876435377016600254323619839508354485363. AND ONE IN-SOLVE CATCH IS GATED RATHER THAN NARRATED: equation (29) comes out exactly only when P_4 is read as the UNSIGNED corner swap their equation (15) displays; the SIGNED cell-map guess fails their equation (27) in the same run at a measured nonzero residual, and that failure is gated.\nper_mode: THE MEASUREMENT THAT CRACKED IT, AND IT IS A LOCALIZATION. The matter reflection defect P(-i d_K)P + (-i d_K)^H has EXACTLY 64 NONZERO ENTRIES, EVERY ONE OF THEM INTRA-SLICE -- row time equals column time at all 64 -- with maximum magnitude EXACTLY 1/2, which is Block 107 equation (28) localized rather than merely bounded. THE TEMPORAL LINKS ARE REFLECTION-EXACT: not one entry of the defect connects different times. THE OBSTRUCTION IS THE GRADING SPLIT, because theta flips time parity and so P carries a grade-raising entry into a mixture of raising and lowering. THIS IS THE CO-TRANSPORT LESSON A FOURTH TIME, after Block 106's W1, Block 182's T2 and Block 183's grading correction: the object that must be co-transported with the map is the GRADING, and every time it has been ignored the defect has landed exactly where the grading was split.\nper_block: THE CONSTRUCTION, DERIVED AND NOT DRESSED, WITH THREE MEASURED STRUCTURAL PROPERTIES. Let A be the d_K entries whose BOTH endpoint times lie in the positive half {0,1,2,3}, PLUS every d_K entry on the two seam edge-time pairs {3,4} and {7,0} -- the physical half plus its two seams and nothing else -- and put D = A - P A P, which carries EXACTLY 72 nonzero entries. THEN: D IS P-ODD, P D P + D = 0 at zero residual; D EQUALS d_K ENTRYWISE at every entry whose two times both lie in {0,1,2,3}, so THE PHYSICAL DYNAMICS OF THE POSITIVE HALF IS UNTOUCHED and the negative half is the transported co-graded image; H_image IS P-EVEN, P H_image P = H_image at zero residual, which is Block 107 equation (27); and therefore P Q_glued P = Q_glued^T at zero residual for Q_glued = m*H_image + H_image*D - D^T*H_image. NO DRESSING IS APPLIED ANYWHERE: no diagonal phase, no cell-local intertwiner, no fixture-tuned coefficient vector, and no congruence of the positive-time span.\nlattice_wide: THE RESULT, AND THE HONEST SPLIT BETWEEN WHAT FOLLOWS AND WHAT IS NEW, AS THE ADVERSARIAL CHECK SCOPED IT. P Q_glued P = Q_glued^T is exactly the hypothesis of Block 107 equation (6), AND THE IMPLICATION TO GRAM HERMITICITY NEEDS THE CONSTRUCTION'S EXACT REALITY AS WELL: the bare implication is FALSE, and the one-dimensional counterexample P = [1], Q = [i] -- which satisfies P Q P = Q^T while its Gram [i] is not Hermitian -- is BUILT AND MEASURED IN THE SAME RUN. THE CHAIN IS: transpose covariance PLUS reality of every entry of Q and of its inverse PLUS invertibility IMPLIES delta = 0, structurally. SO delta = 0 FOLLOWS AND IS NOT THE NEW CONTENT; it is measured here at exactly zero and reported as a consequence. THE GENUINELY NEW NUMERICAL CONTENT IS THE STRICT POSITIVITY: all EIGHT leading principal minors of the glued Gram are STRICTLY POSITIVE as exact rationals, the first being 4465961414671029642827787914210419072833144728317065801107200/8932040001245962023277146780748464953706237777456506835365883, WHICH IS CALIBRATION AND NOT THE CLAIM. Nothing about covariance, reality or invertibility forces positivity, and positivity is what an OS statement needs. REFLECTION POSITIVITY HOLDS FOR THE SEAM-GLUED ACTION AT THIS FIXTURE, AND FOR NOTHING WIDER.\nper_scope: THE NECESSITY OF THE INGREDIENTS, THE WINDOW, AND WHOSE NUMBERS STAND. EVERY INGREDIENT IS ATTACKED BY REBUILDING EVERYTHING BY THE SAME CODE WITH EXACTLY ONE THING CHANGED. THE SEAMS: neither seam gives all eight minors EXACTLY ZERO; the NEAR seam {7,0} alone gives the sign vector (+,+,+,+,-,+,-,+), INDEFINITE; the FAR seam {3,4} alone gives (+,+,+,+,0,0,0,0), DEGENERATE -- and THE PRECISION MATTERS, because the zero-, one- and two-seam A - P A P variants ALL have delta = 0, so HERMITICITY IS SEAM-INSENSITIVE and BOTH SEAMS ARE NECESSARY ONLY FOR STRICT POSITIVITY. THE PARITY: the P-EVEN variant D' = A + P A P fails transpose covariance at maximum norm EXACTLY 313/288 with a nonzero Gram defect. THE GEOMETRY: the raw H(-c) negative half with the SAME D fails covariance at maximum norm EXACTLY 65/576, which is Block 107 equation (17)'s own shear-channel residual reappearing, again with a nonzero Gram defect. THESE ESTABLISH THE INGREDIENTS' NECESSITY WITHIN THE ENUMERATED VARIANTS AND NOT THAT D = A - P A P IS THE ONLY CONCEIVABLE CONSTRUCTION: IT IS FORCED WITHIN THE TESTED FAMILY, AND THE P-ODD EXTENSION IS WHAT THE STRUCTURAL PROOF FORCES ONCE THE INDEPENDENT-HALF DATA ARE FIXED. AND THE POSITIVITY IS WINDOWED IN BOTH DIRECTIONS: at m = 1/3 all eight minors are positive and at m = 2 the sign vector is (+,+,+,+,+,-,+,-); the constant-in-x step at c = 3/5 is positive 8 of 8 and the x-alternating reflection-odd history at c = 3/5 gives (+,+,+,+,+,+,-,-). COVARIANCE AND HERMITICITY SURVIVE ALL FOUR POINTS AND POSITIVITY DOES NOT. THE WINDOW'S CHARACTERIZATION IS OPEN AND IS NAMED AS A NEXT LEG; in the mass direction its boundary lies in (9/20, 2]. BLOCK 107'S TWO OPEN ITEMS CLOSE AT THIS SCOPE WITH NO DRESSING AT ALL -- their dressing-selection obligation is SUPERSEDED rather than discharged, because D is canonical given A -- AND BLOCK 107'S RAW DELTA STANDS UNTOUCHED, their nonzero delta_const, delta_step and delta_A02 being reproduced here EXACTLY and none of them corrected, because the Hermitian object here is the SEAM-GLUED action, a DIFFERENT operator from the one they measured.\nRESULT: THE TWO-HISTORY GRAM OF THE SEAM-GLUED ACTION IS EXACTLY HERMITIAN AND STRICTLY POSITIVE AT BLOCK 107'S OWN FIXTURE, AND THE POSITIVITY IS WINDOWED. Block 107's flat calibration is reproduced digit-for-digit (equation (8), first minor 11457708200/26164592321 and eighth minor 25600000000000000000000000000000000/468657842600056497856109298772694726695681), as are their equation (23) delta_const and delta_step and their equation (29) delta_A02; the matter reflection defect is 64 entries, ALL intra-slice, at maximum magnitude 1/2; the derived D = A - P A P carries 72 entries, is P-odd, agrees with d_K on the whole interior of the positive half, and against the P-even A02-image geometry gives P Q_glued P = Q_glued^T at zero residual; the glued Gram's Hermiticity defect is EXACTLY ZERO -- structurally, given covariance AND reality AND invertibility -- and all EIGHT leading minors are STRICTLY POSITIVE with first minor 4465961414671029642827787914210419072833144728317065801107200/8932040001245962023277146780748464953706237777456506835365883; the no-seam variant degenerates with all eight minors EXACTLY ZERO, the single-seam variants are indefinite and degenerate respectively, the P-even and raw-image variants fail covariance at 313/288 and 65/576; and POSITIVITY FAILS at m = 2 and on the x-alternating history while Hermiticity survives both. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-184 STAND EXACTLY AS LANDED; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: POSITIVITY HOLDS IN A MASS-AND-HISTORY WINDOW AND NOT GENERALLY, measured positive at (m = 9/20, m = 1/3) x (constant-in-x steps c = 5/13, c = 3/5) and MEASURED TO FAIL at m = 2 and on the x-alternating history, with the window's characterization OPEN and its mass-direction boundary only bracketed in (9/20, 2]; the TWO-SLICE span Lambda_+ and not the full positive-time span; BLOCK 107'S CARRIER and not the Blocks 181-184 section frame, so nothing here ports without being re-measured; the Hermiticity delta = 0 FOLLOWS STRUCTURALLY from covariance AND reality AND invertibility and only the strict positivity is new numerical content, the first minor being calibration; the necessity results hold WITHIN THE TESTED FAMILY of variants and do not show D = A - P A P is the only conceivable construction; the glue is NOT nilpotent and no nilpotency is claimed for it; and the dual-frame statement is a READING. NO CORRECTION IS LANDED BY THIS BLOCK, AND THE ADVERSARIAL CHECK NARROWED SCOPE RATHER THAN OVERTURNING A NUMBER. THREE IN-SOLVE CATCHES ARE RECORDED AS PROCESS AND NOT AS CORRECTIONS, because none of them ever left the solve: the naive interior-edge glue, which broke nilpotency and left the defect unchanged; the one-sided xpar Gram dressing, which WORSENED the flat calibration because its defect-split assumption was assumed rather than measured; and the SIGNED cell-map guess for the negative-half image, which failed Block 107 equation (27) and is GATED here at its failure. THE RULE REAFFIRMED IS THE CONTROL-FIRST RULE: each of the three was caught by a control measured alongside it, and the third is now a permanent gate. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE OS RESTRICTION SOLVE COMPLETE anchor, as narrowed by the b185 adversarial check.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
        "m_generality_claimed": M_GENERALITY_CLAIMED,
        "history_generality_claimed": HISTORY_GENERALITY_CLAIMED,
        "section_frame_port_claimed": SECTION_FRAME_PORT_CLAIMED,
        "constraint_quotient_claimed": CONSTRAINT_QUOTIENT_CLAIMED,
        "dual_frame_reading_claimed": DUAL_FRAME_READING_CLAIMED,
        # C -- the citation pins and Block 107's own control numbers.
        "citation_pins": True,
        "kernel_split_residual": ZERO_RESIDUAL,
        "raising_nilpotent_residual": ZERO_RESIDUAL,
        "flat_covariance_residual": ZERO_RESIDUAL,
        "flat_delta": sp.Integer(0),
        "flat_first_minor": FLAT_FIRST_MINOR,
        "flat_last_minor": FLAT_LAST_MINOR,
        "flat_signs": POSITIVE_SIGNS,
        "minor_count": MINOR_COUNT,
        "delta_const": DELTA_CONST,
        "delta_step": DELTA_STEP,
        "delta_a02": DELTA_A02,
        # D -- the defect localization.
        "defect_nonzeros": DEFECT_NONZEROS,
        "defect_all_intra_slice": True,
        "defect_max_magnitude": DEFECT_MAX_MAGNITUDE,
        # E -- the structure of the glue.
        "image_p_even_residual": ZERO_RESIDUAL,
        "d_p_odd_residual": ZERO_RESIDUAL,
        "d_matches_interior": True,
        "glue_nonzeros": GLUE_NONZEROS,
        "glued_transpose_residual": ZERO_RESIDUAL,
        # F -- the result, with its structural half scoped by reality.
        "glued_reality_holds": True,
        "counterexample_covariance_holds": True,
        "counterexample_gram_hermitian": False,
        "glued_delta": sp.Integer(0),
        "glued_signs": POSITIVE_SIGNS,
        "glued_first_minor": GLUED_FIRST_MINOR,
        # G -- the necessity controls and the window.
        "no_seam_signs": NO_SEAM_SIGNS,
        "near_seam_only_signs": NEAR_SEAM_ONLY_SIGNS,
        "far_seam_only_signs": FAR_SEAM_ONLY_SIGNS,
        "seam_variants_all_hermitian": True,
        "p_even_covariance_max_norm": P_EVEN_COVARIANCE_MAXNORM,
        "raw_image_covariance_max_norm": RAW_IMAGE_COVARIANCE_MAXNORM,
        "second_mass_signs": POSITIVE_SIGNS,
        "third_mass_signs": THIRD_MASS_SIGNS,
        "second_history_signs": POSITIVE_SIGNS,
        "x_alternating_signs": X_ALTERNATING_SIGNS,
        "window_points_all_hermitian": True,
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
    elif mutation == "claim_m_generality":
        # THE SCOPE OVERSOLD: positivity at the displayed masses asserted to
        # hold at every mass, which the measured failure at m = 2 forbids
        # outright.  This is the mutation that guards the block's single
        # biggest overreach risk -- a positivity result reads as general unless
        # the banner says it is not, and here it is measurably not.
        claims["m_generality_claimed"] = True
    elif mutation == "claim_dual_frame_theorem":
        # THE READING PROMOTED: the statement that the negative half of the
        # glued action IS the dual-frame dynamics asserted as a theorem, which
        # nothing here derives.  The construction transports the grading; that
        # the transported half is the dual frame is a recognition of its shape.
        claims["dual_frame_reading_claimed"] = True
    elif mutation == "break_flat_minor":
        # THE CALIBRATION MOVED: a different first flat minor asserted, which
        # Block 107 equation (8) forbids.  If this one moves, every number in
        # the block is measuring a different carrier from theirs.
        claims["flat_first_minor"] = FLAT_FIRST_MINOR + 1
    elif mutation == "break_delta_step":
        # THE STEP-HISTORY CONTROL DENIED: delta_step asserted equal to
        # delta_const, which their exact inequality 3*delta_step < delta_const
        # forbids -- and with it the claim that this runner is on their fixture.
        claims["delta_step"] = DELTA_CONST
    elif mutation == "break_defect_count":
        # THE LOCALIZATION ERASED: a defect wider than the measured 64 entries
        # asserted, which the exact count forbids.  The localization is the
        # measurement the whole construction was built from.
        claims["defect_nonzeros"] = 72
    elif mutation == "break_p_odd":
        # THE GLUE'S PARITY DENIED: a P-odd residual asserted allowed for
        # D = A - P A P, which is P-odd by construction AND by measurement.
        claims["d_p_odd_residual"] = 8
    elif mutation == "break_transpose_covariance":
        # THE HYPOTHESIS DELETED: a nonzero P Q P - Q^T residual asserted
        # allowed, which the exact identity forbids -- and without it Block
        # 107's equation (6) -> (7) argument does not run at all.
        claims["glued_transpose_residual"] = 4
    elif mutation == "break_gram_delta":
        # THE RESULT DENIED AT ITS HERMITICITY: the glued Gram asserted to carry
        # Block 107's step-history defect, which the exact zero forbids.
        claims["glued_delta"] = DELTA_STEP
    elif mutation == "break_first_minor":
        # THE CALIBRATION MOVED AT THE RESULT: a different first leading minor
        # asserted, which the exact rational forbids.  It is the calibration of
        # the positive verdict rather than the verdict itself, and it still has
        # to be right.
        claims["glued_first_minor"] = GLUED_FIRST_MINOR / 2
    elif mutation == "break_no_seam_control":
        # THE SEAM DEMOTED: the no-seam variant asserted to stay positive,
        # which eight exactly zero minors forbid.  Without this control the
        # seam edges look like decoration and the result looks like it would
        # survive without them.
        claims["no_seam_signs"] = POSITIVE_SIGNS
    elif mutation == "break_second_mass_window":
        # THE WINDOW DENIED IN THE MASS DIRECTION: positivity asserted at
        # m = 2, which the measured sign vector (+,+,+,+,+,-,+,-) forbids.  This
        # is the mutation that guards the adversarial check's scope narrowing:
        # without it, a reader takes one fixture's positivity for all masses.
        claims["third_mass_signs"] = POSITIVE_SIGNS
    elif mutation == "break_x_alternating_window":
        # THE WINDOW DENIED IN THE HISTORY DIRECTION: positivity asserted on the
        # x-alternating reflection-odd history, which the measured sign vector
        # (+,+,+,+,+,+,-,-) forbids.  Hermiticity DOES survive there, which is
        # exactly why this mutation is needed: the Hermitian half generalizes
        # and the positive half does not.
        claims["x_alternating_signs"] = POSITIVE_SIGNS
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
    kernel_split_residual: int
    raising_nilpotent_residual: int
    flat_covariance_residual: int
    flat_delta: object
    flat_minors: tuple
    flat_signs: tuple
    delta_const: object
    delta_step: object
    delta_a02: object
    delta_ordering_holds: bool
    signed_image_residual: int
    defect_nonzeros: int
    defect_all_intra_slice: bool
    defect_max_magnitude: object
    defect_inter_slice_entries: int
    image_p_even_residual: int
    d_p_odd_residual: int
    d_matches_interior: bool
    raising_nonzeros: int
    restricted_nonzeros: int
    glue_nonzeros: int
    glue_equals_raising: bool
    glue_nilpotent_residual: int
    glued_transpose_residual: int
    glued_inverse_covariance_residual: int
    glued_reality_holds: bool
    counterexample_covariance_holds: bool
    counterexample_gram_hermitian: bool
    counterexample_defect: object
    glued_delta: object
    glued_minors: tuple
    glued_signs: tuple
    no_seam_signs: tuple
    near_seam_only_signs: tuple
    far_seam_only_signs: tuple
    seam_variant_deltas: tuple
    seam_variants_all_hermitian: bool
    p_even_covariance_max_norm: object
    p_even_delta: object
    raw_image_covariance_max_norm: object
    raw_image_delta: object
    second_mass_signs: tuple
    third_mass_signs: tuple
    second_history_signs: tuple
    x_alternating_signs: tuple
    window_deltas: tuple
    window_points_all_hermitian: bool
    exactness_holds: bool


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    # --- Block 107's carrier, built directly from their equations -----------
    kernel = staggered_kernel()
    raising = raising_part(kernel)
    reflection = site_reflection()
    kernel_split_residual = residual_count(kernel - (raising - raising.T))
    raising_nilpotent_residual = residual_count(raising * raising)
    base_step = step_history(SHEAR)
    base_field = constant_in_x(base_step)

    # --- C: the flat calibration, Block 107 equations (5), (6) and (8) ------
    flat_action = MASS * sp.eye(COVER_SIZE) + kernel
    flat_covariance_residual = residual_count(
        reflection * flat_action * reflection - flat_action.T)
    flat_gram = two_history_gram(flat_action)
    flat_delta = hermiticity_defect(flat_gram)
    flat_minors = leading_minors(flat_gram)

    # --- C: their equation (23), both histories -----------------------------
    const_hodge = hodge_from_cells(
        plain_cells(constant_in_x((SHEAR,) * TIME_EXTENT)))
    step_hodge = hodge_from_cells(plain_cells(base_field))
    delta_const = hermiticity_defect(
        two_history_gram(completion(const_hodge, raising, MASS)))
    delta_step = hermiticity_defect(
        two_history_gram(completion(step_hodge, raising, MASS)))
    # Their equation (24), re-measured rather than recalled.
    delta_ordering_holds = bool(0 < 3 * delta_step < delta_const)

    # --- C/E: their equation (29), and the SIGNED neighbour that fails ------
    image_hodge = hodge_from_cells(image_cells(base_field))
    delta_a02 = hermiticity_defect(
        two_history_gram(completion(image_hodge, raising, MASS)))
    image_p_even_residual = residual_count(
        reflection * image_hodge * reflection - image_hodge)
    # THE IN-SOLVE CATCH, GATED.  The SIGNED cell map -- the one whose square is
    # -I -- is the natural guess and it FAILS Block 107 equation (27).  It is
    # built here only to be measured failing, in the same run as the identity.
    signed_hodge = hodge_from_cells(image_cells(base_field, SIGNED_CELL_MAP))
    signed_image_residual = residual_count(
        reflection * signed_hodge * reflection - signed_hodge)

    # --- D: THE DEFECT LOCALIZATION -----------------------------------------
    # Block 107 equation (4) puts d = -i d_K; their equation (28) bounds
    # ||P d P + d^dagger||_max at 1/2.  THIS MEASURES WHERE IT LIVES.
    matter = sp.expand(-sp.I * raising)
    defect = sp.expand(reflection * matter * reflection + matter.H)
    defect_positions = tuple(
        (row, column)
        for row in range(COVER_SIZE) for column in range(COVER_SIZE)
        if defect[row, column] != 0)
    defect_inter_slice_entries = sum(
        1 for row, column in defect_positions
        if row // SPACE_EXTENT != column // SPACE_EXTENT)
    defect_max_magnitude = max(
        sp.Abs(defect[position]) for position in defect_positions)

    # --- E: the glue --------------------------------------------------------
    restricted = restricted_raising(raising, BOTH_SEAMS)
    glue = sp.expand(restricted - reflection * restricted * reflection)
    d_p_odd_residual = residual_count(
        reflection * glue * reflection + glue)
    d_matches_interior = all(
        glue[row, column] == raising[row, column]
        for row in range(COVER_SIZE) for column in range(COVER_SIZE)
        if row // SPACE_EXTENT in POSITIVE_TIMES
        and column // SPACE_EXTENT in POSITIVE_TIMES)
    glued_action = completion(image_hodge, glue, MASS)
    glued_transpose_residual = residual_count(
        reflection * glued_action * reflection - glued_action.T)
    glued_inverse = glued_action.inv()
    glued_inverse_covariance_residual = residual_count(
        reflection * glued_inverse * reflection - glued_inverse.T)

    # --- F: the result, and the REALITY the implication actually needs ------
    glued_gram = two_history_gram(glued_action)
    glued_delta = hermiticity_defect(glued_gram)
    glued_minors = leading_minors(glued_gram)
    # THE REALITY CERTIFICATE.  The adversarial check's C8: transpose
    # covariance alone does NOT give Gram Hermiticity.  Every entry of Q_glued
    # and of its inverse is REAL, and that is what closes the chain.
    glued_reality_holds = all(
        sp.im(value) == 0
        for matrix in (glued_action, glued_inverse) for value in matrix)
    # THE ONE-DIMENSIONAL COUNTEREXAMPLE, BUILT AND MEASURED rather than cited:
    # P = [1] and Q = [i] satisfy P Q P = Q^T exactly, and the Gram
    # conj(G(b, theta a)) = conj(1/i) = i is NOT Hermitian.  The reality clause
    # is therefore load-bearing and is not decoration.
    tiny_reflection = sp.Matrix([[1]])
    tiny_action = sp.Matrix([[sp.I]])
    counterexample_covariance_holds = residual_count(
        tiny_reflection * tiny_action * tiny_reflection - tiny_action.T) == 0
    tiny_gram = sp.Matrix([[sp.conjugate(tiny_action.inv()[0, 0])]])
    counterexample_defect = max_norm(tiny_gram - tiny_gram.H)
    counterexample_gram_hermitian = counterexample_defect == 0

    # --- G: the necessity controls, each ONE ingredient away ----------------
    def seam_variant(seams: tuple) -> Variant:
        restricted_variant = restricted_raising(raising, seams)
        variant_glue = sp.expand(
            restricted_variant - reflection * restricted_variant * reflection)
        return build_variant(MASS, image_cells(base_field), variant_glue,
                             reflection)

    no_seam = seam_variant(())
    near_only = seam_variant((NEAR_SEAM,))
    far_only = seam_variant((FAR_SEAM,))
    # THE PARITY ATTACK: the P-EVEN companion of the same restricted set.
    p_even = build_variant(
        MASS, image_cells(base_field),
        sp.expand(restricted + reflection * restricted * reflection),
        reflection)
    # THE GEOMETRY ATTACK: the SAME D against the raw H(-c) negative half.
    raw_image = build_variant(MASS, plain_cells(base_field), glue, reflection)

    # --- G: THE WINDOW, the adversarial check's four fresh points -----------
    second_mass = build_variant(
        SECOND_MASS, image_cells(base_field), glue, reflection)
    third_mass = build_variant(
        THIRD_MASS, image_cells(base_field), glue, reflection)
    second_history_step = step_history(SECOND_HISTORY_SHEAR)
    second_history = build_variant(
        MASS, image_cells(constant_in_x(second_history_step)), glue,
        reflection)
    alternating = build_variant(
        MASS, image_cells(x_alternating(second_history_step)), glue,
        reflection)
    window = (second_mass, third_mass, second_history, alternating)

    citation_pins = {
        "b107_curved_os": B107_CURVED_OS_PIN in landed_text(BLOCK107_NOTE),
        "b107_dressing": B107_DRESSING_PIN in landed_text(BLOCK107_NOTE),
        "b107_not_a_nogo": B107_NOT_A_NOGO_PIN in landed_text(BLOCK107_NOTE),
        "b184_gram": B184_GRAM_PIN in landed_text(BLOCK184_NOTE),
    }
    banners = {
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        # THE DECLARED STATUS FLAGS, so the B mutations bite on a declared
        # object and not on prose.  ALL FIVE ARE MEASURED AND ALL ARE FALSE.
        "objects_registered": bool(REGISTERED_OBJECTS or ADOPTED_OBJECTS),
        "m_generality_claimed": M_GENERALITY_CLAIMED,
        "history_generality_claimed": HISTORY_GENERALITY_CLAIMED,
        "section_frame_port_claimed": SECTION_FRAME_PORT_CLAIMED,
        "constraint_quotient_claimed": CONSTRAINT_QUOTIENT_CLAIMED,
        "dual_frame_reading_claimed": DUAL_FRAME_READING_CLAIMED,
    }
    # EXACTNESS, MEASURED AND NOT ASSERTED: not one measured scalar is a float.
    exact_scalars = (
        (flat_delta, delta_const, delta_step, delta_a02, glued_delta,
         defect_max_magnitude, p_even.covariance_max_norm, p_even.delta,
         raw_image.covariance_max_norm, raw_image.delta)
        + flat_minors + glued_minors + no_seam.minors + near_only.minors
        + far_only.minors
        + tuple(value for variant in window for value in variant.minors))
    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        kernel_split_residual=kernel_split_residual,
        raising_nilpotent_residual=raising_nilpotent_residual,
        flat_covariance_residual=flat_covariance_residual,
        flat_delta=flat_delta,
        flat_minors=flat_minors,
        flat_signs=minor_signs(flat_minors),
        delta_const=delta_const,
        delta_step=delta_step,
        delta_a02=delta_a02,
        delta_ordering_holds=delta_ordering_holds,
        signed_image_residual=signed_image_residual,
        defect_nonzeros=len(defect_positions),
        defect_all_intra_slice=defect_inter_slice_entries == 0,
        defect_max_magnitude=defect_max_magnitude,
        defect_inter_slice_entries=defect_inter_slice_entries,
        image_p_even_residual=image_p_even_residual,
        d_p_odd_residual=d_p_odd_residual,
        d_matches_interior=d_matches_interior,
        raising_nonzeros=nonzero_entries(raising),
        restricted_nonzeros=nonzero_entries(restricted),
        glue_nonzeros=nonzero_entries(glue),
        glue_equals_raising=residual_count(glue - raising) == 0,
        glue_nilpotent_residual=residual_count(glue * glue),
        glued_transpose_residual=glued_transpose_residual,
        glued_inverse_covariance_residual=glued_inverse_covariance_residual,
        glued_reality_holds=bool(glued_reality_holds),
        counterexample_covariance_holds=bool(counterexample_covariance_holds),
        counterexample_gram_hermitian=bool(counterexample_gram_hermitian),
        counterexample_defect=counterexample_defect,
        glued_delta=glued_delta,
        glued_minors=glued_minors,
        glued_signs=minor_signs(glued_minors),
        no_seam_signs=no_seam.signs,
        near_seam_only_signs=near_only.signs,
        far_seam_only_signs=far_only.signs,
        seam_variant_deltas=(no_seam.delta, near_only.delta, far_only.delta),
        seam_variants_all_hermitian=all(
            variant.delta == 0 for variant in (no_seam, near_only, far_only)),
        p_even_covariance_max_norm=p_even.covariance_max_norm,
        p_even_delta=p_even.delta,
        raw_image_covariance_max_norm=raw_image.covariance_max_norm,
        raw_image_delta=raw_image.delta,
        second_mass_signs=second_mass.signs,
        third_mass_signs=third_mass.signs,
        second_history_signs=second_history.signs,
        x_alternating_signs=alternating.signs,
        window_deltas=tuple(variant.delta for variant in window),
        window_points_all_hermitian=all(
            variant.covariance_residual == 0 and variant.delta == 0
            for variant in window),
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
        "registry blobs in the worktree. THE TWO BLOCK 184 ARTIFACTS ARE "
        "CONTENT-BOUND -- its note and its runner, the pair that identifies "
        "the commit this block's branch is cut from -- at PARENT_COMMIT, in "
        "the worktree and against their pinned blobs, and PARENT_COMMIT IS "
        "REAL and PARENT_REF resolves to it, so nothing needs sed at landing. "
        "THE STALE PIN IS THE BLOCK 183 TIP, a REAL ancestor of HEAD that "
        "PREDATES Block 184 and therefore carries NEITHER Block 184 artifact, "
        "which is exactly what makes the stale_parent_authority mutation bite: "
        "under it the gate looks for the artifact blobs at a commit where they "
        "do not exist. AUDIT_INPUT_PATHS IS LITERAL and every one of its EIGHT "
        "entries is required readable in the worktree EXCEPT this block's own "
        "note, which lands later and belongs to gate H -- and the eight "
        "include the CONVENTION AUTHORITY this block is built on and whose "
        "open items it closes at fixture scope, the Block 107 note. AND THE "
        "MACHINERY IMPORT IS GATED: the LANDED Block 128 runner must have "
        "imported, because the two helper objects this runner does not build "
        "itself -- cover_embedding() and the Block 105 shear_hodge() -- are "
        "read from it, and NOTHING from any scratchpad is imported or read",
        bool(
            AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
            and len(AUDIT_INPUT_PATHS) == 8
            and len(set(AUDIT_INPUT_PATHS)) == 8
            and BLOCK184_NOTE in AUDIT_INPUT_PATHS
            and BLOCK184_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK183_NOTE in AUDIT_INPUT_PATHS
            and BLOCK183_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK107_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_RUNNER in AUDIT_INPUT_PATHS
            and CAMPAIGN_NOTE in AUDIT_INPUT_PATHS
            # EVERY AUDIT INPUT BUT THIS BLOCK'S OWN NOTE IS READABLE IN THE
            # WORKTREE; the note itself is gate H's, because it lands later.
            and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
            and authority.inputs_missing == ()
            and PARENT_ARTIFACTS == (BLOCK184_NOTE, BLOCK184_RUNNER)
            and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
            and facts.main_head == claims["main_head"]
            and authority.fixed_authority
            and authority.machinery_import_landed
            and authority.parent_pin_is_commit
            and authority.parent_ref_and_ancestry
            and parent_blobs_ok
            # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER
            # Block 184 artifact.
            and authority.stale_is_real_ancestor
            and authority.stale_carries_neither_artifact))

    # --- B: the imposed-object banner and the NOT-CLAIMED keys -------------
    ban = facts.banners
    checks.check(
        "B-THE-IMPOSED-OBJECT-BANNER-and-the-NOT-CLAIMED-keys",
        f"THE BANNER COMES BEFORE ANY NUMERAL AND IT IS MEASURED RATHER THAN "
        f"ASSERTED. {ban['imposed_objects']} objects are IMPOSED by this block "
        f"-- Block 107's carrier and conventions rebuilt from their displayed "
        f"equations, their fixture together with the three further points the "
        f"adversarial check supplied, their completion convention "
        f"Q = m*H + H*d - d^T*H, their A02-image geometry at the UNSIGNED "
        f"offset permutation, THE GLUED ACTION which is this block's own "
        f"object, and the two LANDED Block 128 helpers that are the only "
        f"imports -- and {ban['registered_objects']} are REGISTERED and "
        f"{ban['adopted_objects']} are ADOPTED. AND THE BANNER'S SECOND HALF "
        f"IS WHAT IS NOT CLAIMED, gated as declared constants: NO "
        f"m-GENERALITY, because positivity is MEASURED TO FAIL at m = 2 and a "
        f"positivity result reads as general unless the banner says it is not; "
        f"NO HISTORY-GENERALITY, because positivity is MEASURED TO FAIL on the "
        f"x-alternating reflection-odd history; NO PORT TO THE BLOCKS 181-184 "
        f"SECTION FRAME, because Block 107's carrier is a DIFFERENT carrier "
        f"from the Block 128 chart family; NO GRAVITY CONSTRAINT QUOTIENT; and "
        f"THE DUAL-FRAME STATEMENT IS A READING -- that the negative half of "
        f"the glued action IS the dual-frame dynamics is a recognition of the "
        f"transported half's shape and is never derived here. Asserting any of "
        f"the five, or asserting that the imposed objects are registered, "
        f"fails HERE and nowhere else",
        bool(
            ban["imposed_objects"] == 6
            and ban["registered_objects"] == 0
            and ban["adopted_objects"] == 0
            and ban["objects_registered"] == claims["objects_registered"]
            and ban["m_generality_claimed"] == claims["m_generality_claimed"]
            and ban["history_generality_claimed"]
            == claims["history_generality_claimed"]
            and ban["section_frame_port_claimed"]
            == claims["section_frame_port_claimed"]
            and ban["constraint_quotient_claimed"]
            == claims["constraint_quotient_claimed"]
            and ban["dual_frame_reading_claimed"]
            == claims["dual_frame_reading_claimed"]))

    # --- C: the citation pins, then Block 107's own numbers -----------------
    pins = facts.citation_pins
    checks.check(
        "C-THE-CONVENTIONS-AND-THE-OPEN-ITEMS-ARE-READ-FROM-THE-PRIMARY-BODIES",
        f"WHAT THIS BLOCK CLOSES IS PINNED IN THE NOTE THAT LEFT IT OPEN, not "
        f"in a recollection of it. Block 107's own not-claimed list -- "
        f"'{B107_CURVED_OS_PIN}' -- is present in its primary body "
        f"({pins['b107_curved_os']}), and that is the item this block closes "
        f"AT FIXTURE SCOPE. So is their dressing obligation, "
        f"'{B107_DRESSING_PIN}' ({pins['b107_dressing']}), which this block "
        f"SUPERSEDES rather than discharges, because it applies no dressing at "
        f"all. So is their scope firewall '{B107_NOT_A_NOGO_PIN}' "
        f"({pins['b107_not_a_nogo']}), which is the sentence that made this "
        f"attempt admissible rather than foreclosed. AND THE HAND-OFF IS "
        f"PINNED THE SAME WAY: Block 184's '{B184_GRAM_PIN}' "
        f"({pins['b184_gram']}) is the successor sentence this block answers. "
        f"EVERY ONE IS SOMEBODY ELSE'S LANDED SENTENCE",
        bool(all(pins.values()) == claims["citation_pins"]))
    checks.check(
        "C-CONTROL-BLOCK-107s-FLAT-CALIBRATION-REPRODUCED-DIGIT-FOR-DIGIT",
        f"THE CONTROLS COME FIRST AND THEY ARE SOMEBODY ELSE'S NUMBERS. The "
        f"kernel splits as K = d_K - d_K^T at {facts.kernel_split_residual} "
        f"nonzero entries and d_K^2 = 0 at "
        f"{facts.raising_nilpotent_residual}, which is Block 107 equation (4). "
        f"P Q_0 P - Q_0^T has {facts.flat_covariance_residual} nonzero "
        f"entries, their equation (6). AND THEIR EQUATION (8) COMES OUT "
        f"DIGIT-FOR-DIGIT: the flat two-history Gram is EXACTLY Hermitian "
        f"(defect {facts.flat_delta}), its {len(facts.flat_minors)} leading "
        f"principal minors have sign vector {facts.flat_signs}, the first is "
        f"{facts.flat_minors[0]} and the eighth is {facts.flat_minors[-1]}. "
        f"NOTHING BELOW IS BELIEVABLE IF THIS IS NOT EXACT: the flat "
        f"calibration is the only place where this runner and Block 107 can be "
        f"checked to be measuring the same carrier at all. Asserting a "
        f"different first minor fails HERE and nowhere else",
        bool(
            facts.kernel_split_residual == claims["kernel_split_residual"]
            and facts.raising_nilpotent_residual
            == claims["raising_nilpotent_residual"]
            and facts.flat_covariance_residual
            == claims["flat_covariance_residual"]
            and facts.flat_delta == claims["flat_delta"]
            and len(facts.flat_minors) == claims["minor_count"]
            and facts.flat_minors[0] == claims["flat_first_minor"]
            and facts.flat_minors[-1] == claims["flat_last_minor"]
            and facts.flat_signs == claims["flat_signs"]))
    checks.check(
        "C-CONTROL-THEIR-CURVED-DEFECTS-eq-23-and-eq-29-REPRODUCED-EXACTLY",
        f"AND THEIR CURVED NUMBERS COME OUT TOO, WHICH IS WHAT MAKES THE "
        f"RESULT BELOW A DIFFERENT OBJECT RATHER THAN A CONTRADICTION. On "
        f"Q_hist = m*H_hist + H_hist*d_K - d_K^T*H_hist, Block 107 equation "
        f"(23) is reproduced exactly: delta_const = {facts.delta_const} and "
        f"delta_step = {facts.delta_step}, both NONZERO, with their equation "
        f"(24) ordering 0 < 3*delta_step < delta_const re-measured here "
        f"({facts.delta_ordering_holds}). Their equation (29) is reproduced "
        f"exactly on the A02-image geometry: delta_a02 = {facts.delta_a02}. "
        f"BLOCK 107'S RAW DELTA STANDS UNTOUCHED AND IS NOT CORRECTED BY "
        f"ANYTHING IN THIS BLOCK. Asserting that delta_step equals delta_const "
        f"fails HERE and nowhere else",
        bool(
            facts.delta_const == claims["delta_const"]
            and facts.delta_step == claims["delta_step"]
            and facts.delta_a02 == claims["delta_a02"]
            and facts.delta_ordering_holds
            and facts.delta_const != 0
            and facts.delta_step != 0
            and facts.delta_a02 != 0))

    # --- D: the defect localization -----------------------------------------
    checks.check(
        "D-THE-DEFECT-IS-64-ENTRIES-and-EVERY-ONE-IS-INTRA-SLICE",
        f"THE MEASUREMENT THAT CRACKED THE BLOCK, AND IT IS A LOCALIZATION "
        f"RATHER THAN A BOUND. The matter reflection defect "
        f"P(-i d_K)P + (-i d_K)^H has EXACTLY {facts.defect_nonzeros} nonzero "
        f"entries with maximum magnitude {facts.defect_max_magnitude} -- which "
        f"is Block 107 equation (28) -- AND EVERY SINGLE ONE OF THEM IS "
        f"INTRA-SLICE ({facts.defect_all_intra_slice}): row time equals column "
        f"time at all {facts.defect_nonzeros} positions and "
        f"{facts.defect_inter_slice_entries} entries connect different times. "
        f"THE TEMPORAL LINKS ARE REFLECTION-EXACT. What is broken is the "
        f"GRADING SPLIT -- theta flips time parity, so P carries a "
        f"grade-raising entry into a MIXTURE of raising and lowering, and the "
        f"whole obstruction lands in the spatial direction. THIS IS THE "
        f"CO-TRANSPORT LESSON A FOURTH TIME, after Block 106's W1, Block 182's "
        f"T2 and Block 183's grading correction: co-transport the GRADING with "
        f"the map, and the defect that looked like a wall turns out to be "
        f"confined to one direction. Asserting a wider defect fails HERE and "
        f"nowhere else",
        bool(
            facts.defect_nonzeros == claims["defect_nonzeros"]
            and facts.defect_all_intra_slice
            == claims["defect_all_intra_slice"]
            and facts.defect_inter_slice_entries == 0
            and facts.defect_max_magnitude == claims["defect_max_magnitude"]))

    # --- E: the structure of the glue ---------------------------------------
    checks.check(
        "E-THE-GLUE-P-EVEN-GEOMETRY-P-ODD-D-UNTOUCHED-INTERIOR-and-COVARIANCE",
        f"THE CONSTRUCTION'S THREE STRUCTURAL PROPERTIES, MEASURED. FIRST, THE "
        f"GEOMETRY IS P-EVEN: P H_image P - H_image has "
        f"{facts.image_p_even_residual} nonzero entries, which is Block 107 "
        f"equation (27) -- AND THE CONVENTION IS LOAD-BEARING, measured "
        f"against its failing neighbour in the same run: with the SIGNED cell "
        f"map in place of equation (15)'s UNSIGNED corner swap the SAME "
        f"residual is {facts.signed_image_residual} nonzero entries, so a "
        f"reader who signs the swap gets a false statement and their equation "
        f"(29) does not come out either. SECOND, D IS P-ODD: P D P + D has "
        f"{facts.d_p_odd_residual} nonzero entries for D = A - P A P, where A "
        f"is the {facts.restricted_nonzeros} raising entries of the "
        f"{facts.raising_nonzeros} in d_K that lie in the positive half or on "
        f"the two seam edge-time pairs, and D itself carries EXACTLY "
        f"{facts.glue_nonzeros}. THIRD, THE PHYSICAL DYNAMICS IS UNTOUCHED: D "
        f"equals d_K entrywise at every entry whose two times both lie in "
        f"{{0,1,2,3}} ({facts.d_matches_interior}), while D is NOT d_K "
        f"globally ({not facts.glue_equals_raising}) -- the negative half is "
        f"the transported co-graded image and not a copy. AND THEREFORE THE "
        f"HYPOTHESIS HOLDS: P Q_glued P - Q_glued^T has "
        f"{facts.glued_transpose_residual} nonzero entries, and the same "
        f"covariance passes to the inverse at "
        f"{facts.glued_inverse_covariance_residual}. THE GLUE IS NOT NILPOTENT "
        f"-- D^2 has {facts.glue_nilpotent_residual} nonzero entries -- AND NO "
        f"NILPOTENCY IS CLAIMED FOR IT ANYWHERE: Q_glued is a PAIRING and not "
        f"a differential complex. Asserting a P-even D, or a nonzero "
        f"transpose-covariance residual, fails HERE and nowhere else",
        bool(
            facts.image_p_even_residual == claims["image_p_even_residual"]
            and facts.d_p_odd_residual == claims["d_p_odd_residual"]
            and facts.d_matches_interior == claims["d_matches_interior"]
            and facts.glue_nonzeros == claims["glue_nonzeros"]
            and facts.glued_transpose_residual
            == claims["glued_transpose_residual"]
            # THE FAILING NEIGHBOURS, asserted unconditionally: the signed cell
            # map must FAIL and the glue must NOT be d_K globally.
            and facts.signed_image_residual != 0
            and not facts.glue_equals_raising))

    # --- F: the result ------------------------------------------------------
    checks.check(
        "F-THE-GLUED-GRAM-IS-HERMITIAN-BY-COVARIANCE-PLUS-REALITY-and-POSITIVE",
        f"THE RESULT, WITH ITS TWO HALVES KEPT APART BECAUSE THEY HAVE "
        f"DIFFERENT STANDING, AND WITH THE STRUCTURAL HALF SCOPED AS THE "
        f"ADVERSARIAL CHECK SCOPED IT. The Hermiticity defect of the glued "
        f"two-history Gram is EXACTLY {facts.glued_delta}. THAT HALF FOLLOWS "
        f"STRUCTURALLY, BUT NOT FROM COVARIANCE ALONE: the chain is P Q P = "
        f"Q^T PLUS THE CONSTRUCTION'S EXACT REALITY -- every entry of Q_glued "
        f"and of its inverse is real ({facts.glued_reality_holds}) -- PLUS "
        f"invertibility. THE REALITY CLAUSE IS LOAD-BEARING AND THE "
        f"COUNTEREXAMPLE IS BUILT AND MEASURED IN THIS RUN, not cited: with "
        f"P = [1] and Q = [i], P Q P = Q^T holds "
        f"({facts.counterexample_covariance_holds}) while the Gram [i] is NOT "
        f"Hermitian ({facts.counterexample_gram_hermitian}) at defect "
        f"{facts.counterexample_defect}. So delta = 0 is a CONSEQUENCE and it "
        f"is reported as one. THE OTHER HALF DOES NOT FOLLOW FROM COVARIANCE, "
        f"REALITY OR INVERTIBILITY: all {len(facts.glued_minors)} leading "
        f"principal minors are STRICTLY POSITIVE, sign vector "
        f"{facts.glued_signs}, as exact rationals, the first being "
        f"{facts.glued_minors[0]} -- WHICH IS CALIBRATION AND NOT THE CLAIM. "
        f"THE STRICT POSITIVITY IS THE GENUINELY NEW NUMERICAL CONTENT OF THIS "
        f"BLOCK, and positivity is what an OS statement needs. Every value is "
        f"an exact rational determinant by the Berkowitz algorithm, with no "
        f"eigenvalue estimate and no tolerance ({facts.exactness_holds}). "
        f"Asserting a nonzero defect, or a different first minor, fails HERE "
        f"and nowhere else",
        bool(
            facts.glued_delta == claims["glued_delta"]
            and len(facts.glued_minors) == claims["minor_count"]
            and facts.glued_signs == claims["glued_signs"]
            and facts.glued_minors[0] == claims["glued_first_minor"]
            and facts.glued_reality_holds == claims["glued_reality_holds"]
            and facts.counterexample_covariance_holds
            == claims["counterexample_covariance_holds"]
            and facts.counterexample_gram_hermitian
            == claims["counterexample_gram_hermitian"]
            and facts.exactness_holds))

    # --- G: the necessity controls and the window ---------------------------
    checks.check(
        "G-THE-SEAMS-ARE-LOAD-BEARING-FOR-POSITIVITY-and-NOT-FOR-HERMITICITY",
        f"THE SEAM EDGES ARE NOT DECORATION, AND THE CONTROLS SAY EXACTLY WHAT "
        f"THEY CARRY. Rebuild D, Q_glued and the Gram BY THE SAME CODE with "
        f"the seam set changed and NOTHING else. NEITHER SEAM: sign vector "
        f"{facts.no_seam_signs} -- all eight minors exactly zero, the halves "
        f"disconnect and the pairing dies. THE NEAR SEAM {{7,0}} ALONE: "
        f"{facts.near_seam_only_signs} -- INDEFINITE. THE FAR SEAM {{3,4}} "
        f"ALONE: {facts.far_seam_only_signs} -- DEGENERATE. AND HERE IS THE "
        f"PRECISION THAT MATTERS AND THAT A CARELESS READING WOULD MISS: ALL "
        f"THREE VARIANTS ARE STILL EXACTLY HERMITIAN "
        f"({facts.seam_variants_all_hermitian}) at defects "
        f"{facts.seam_variant_deltas}. HERMITICITY IS SEAM-INSENSITIVE. BOTH "
        f"SEAMS ARE NECESSARY ONLY FOR STRICT POSITIVITY, which is the only "
        f"thing they were ever load-bearing for. Asserting that the no-seam "
        f"variant stays positive fails HERE and nowhere else",
        bool(
            facts.no_seam_signs == claims["no_seam_signs"]
            and facts.near_seam_only_signs == claims["near_seam_only_signs"]
            and facts.far_seam_only_signs == claims["far_seam_only_signs"]
            and facts.seam_variants_all_hermitian
            == claims["seam_variants_all_hermitian"]))
    checks.check(
        "G-THE-CANONICITY-ATTACKS-parity-at-313-288-and-geometry-at-65-576",
        f"THE OTHER TWO INGREDIENTS ARE ATTACKED THE SAME WAY, ONE AT A TIME. "
        f"THE PARITY: replace D = A - P A P by its P-EVEN companion "
        f"D' = A + P A P and transpose covariance FAILS at maximum norm "
        f"EXACTLY {facts.p_even_covariance_max_norm}, with a Gram defect of "
        f"{facts.p_even_delta} -- nonzero. THE GEOMETRY: keep D and replace "
        f"the A02-image negative half by the RAW H(-c) geometry, and "
        f"covariance FAILS at maximum norm EXACTLY "
        f"{facts.raw_image_covariance_max_norm} -- which is BLOCK 107'S OWN "
        f"EQUATION (17) SHEAR-CHANNEL RESIDUAL REAPPEARING, the same 65/576 "
        f"they measured -- again with a nonzero Gram defect "
        f"({facts.raw_image_delta}). AND THE SCOPE OF ALL FOUR NECESSITY "
        f"RESULTS IS STATED RATHER THAN LEFT TO THE READER: THESE ESTABLISH "
        f"THE INGREDIENTS' NECESSITY WITHIN THE ENUMERATED VARIANTS, NOT THAT "
        f"D = A - P A P IS THE ONLY CONCEIVABLE CONSTRUCTION. IT IS FORCED "
        f"WITHIN THE TESTED FAMILY, AND THE P-ODD EXTENSION IS WHAT THE "
        f"STRUCTURAL PROOF FORCES ONCE THE INDEPENDENT-HALF DATA ARE FIXED",
        bool(
            facts.p_even_covariance_max_norm
            == claims["p_even_covariance_max_norm"]
            and facts.raw_image_covariance_max_norm
            == claims["raw_image_covariance_max_norm"]
            and facts.p_even_delta != 0
            and facts.raw_image_delta != 0))
    checks.check(
        "G-THE-WINDOW-positivity-FAILS-at-m-2-and-on-the-x-ALTERNATING-history",
        f"AND THE POSITIVITY IS WINDOWED IN BOTH DIRECTIONS, WHICH IS THE "
        f"ADVERSARIAL CHECK'S SCOPE NARROWING AND IS GATED HERE RATHER THAN "
        f"CONFESSED IN PROSE. THE MASS DIRECTION: at m = {SECOND_MASS} the "
        f"sign vector is {facts.second_mass_signs} -- STILL POSITIVE -- while "
        f"at m = {THIRD_MASS} it is {facts.third_mass_signs}, so minors six "
        f"and eight go NEGATIVE and POSITIVITY FAILS. THE HISTORY DIRECTION: "
        f"the constant-in-x step at c = {SECOND_HISTORY_SHEAR} gives "
        f"{facts.second_history_signs} -- STILL POSITIVE -- while the "
        f"x-alternating reflection-odd history c(t,x) = c_t (-1)^x at the same "
        f"c gives {facts.x_alternating_signs}, so minors seven and eight go "
        f"NEGATIVE. AND COVARIANCE AND HERMITICITY SURVIVE ALL FOUR POINTS "
        f"({facts.window_points_all_hermitian}) at defects "
        f"{facts.window_deltas}: THE HERMITIAN HALF GENERALIZES AND THE "
        f"POSITIVE HALF DOES NOT. Positivity therefore holds in a "
        f"MASS-AND-HISTORY WINDOW whose CHARACTERIZATION IS OPEN and whose "
        f"mass-direction boundary is only bracketed in {MASS_WINDOW_BRACKET}. "
        f"Asserting positivity at m = 2, or on the x-alternating history, "
        f"fails HERE and nowhere else",
        bool(
            facts.second_mass_signs == claims["second_mass_signs"]
            and facts.third_mass_signs == claims["third_mass_signs"]
            and facts.second_history_signs == claims["second_history_signs"]
            and facts.x_alternating_signs == claims["x_alternating_signs"]
            and facts.window_points_all_hermitian
            == claims["window_points_all_hermitian"]))

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
        f"is sixteen members mapped one-per-family across A through H",
        bool(
            facts.note_at_final_path
            and NOTE_PATH.name == FINAL_NOTE_NAME
            and set(facts.scope) == set(SCOPE_KEYS)
            # THE FULL KEY SET IS REQUIRED, not a subset.
            and required == SCOPE_KEYS
            and all(facts.scope[key] for key in required)
            and facts.scope["n5_verbatim"]
            and len(MUTATIONS) == 16
            and len(set(MUTATIONS)) == 16
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
          f"it {authority.parent_ref_and_ancestry}, and BOTH Block 184 "
          f"artifacts are content-bound there and in the worktree "
          f"{authority.parent_artifact_blobs}. THE AUDIT INPUTS: "
          f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} "
          f"readable in the worktree (this block's own note excluded, since it "
          f"lands later and is gate H's), missing {authority.inputs_missing}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {authority.stale_is_real_ancestor} and carries NEITHER Block "
          f"184 artifact {authority.stale_carries_neither_artifact} -- it is "
          f"the Block 183 tip, which PREDATES both artifacts, and that absence "
          f"is exactly what makes the stale_parent_authority mutation bite")
    print(f"  THE MACHINERY: THIS BLOCK'S MACHINERY IS NEW. Block 107's "
          f"carrier is NOT the Block 128 chart family, so the staggered "
          f"kernel, the grade projectors, d_K, the site reflection, the offset "
          f"permutation, the restricted raising set, the derived glue and the "
          f"glued action are ALL BUILT DIRECTLY HERE from Block 107's "
          f"displayed equations. The LANDED Block 128 runner is imported "
          f"{authority.machinery_import_landed} for EXACTLY TWO objects, "
          f"cover_embedding() and the Block 105 shear_hodge(); the carrier is "
          f"{TIME_EXTENT}x{SPACE_EXTENT} at dimension {COVER_SIZE}, the "
          f"reference fixture is m = {MASS} and c = {SHEAR} at volume 1, and "
          f"the step history is {step_history(SHEAR)}. NOTHING from any "
          f"scratchpad is imported or read")
    print(f"  THE BANNER: {ban['imposed_objects']} imposed objects, "
          f"{ban['registered_objects']} registered and "
          f"{ban['adopted_objects']} adopted; MEASURED m-generality-claimed "
          f"{ban['m_generality_claimed']}, history-generality-claimed "
          f"{ban['history_generality_claimed']}, section-frame-port-claimed "
          f"{ban['section_frame_port_claimed']}, constraint-quotient-claimed "
          f"{ban['constraint_quotient_claimed']} and dual-frame-reading-"
          f"claimed {ban['dual_frame_reading_claimed']}. The imposed objects "
          f"are {IMPOSED_OBJECTS}")
    print(f"  THE CITATION PINS: {facts.citation_pins} -- the open items read "
          f"from Block 107's PRIMARY BODY and the hand-off from Block 184's")
    print(f"  THE FLAT CALIBRATION, BLOCK 107 EQUATION (8): K = d_K - d_K^T at "
          f"{facts.kernel_split_residual}, d_K^2 = 0 at "
          f"{facts.raising_nilpotent_residual}, P Q_0 P = Q_0^T at "
          f"{facts.flat_covariance_residual}; the flat Gram's defect is "
          f"{facts.flat_delta} and its sign vector is {facts.flat_signs}. THE "
          f"MINORS: {tuple(str(value) for value in facts.flat_minors)}")
    print(f"  THEIR CURVED DEFECTS, EQUATIONS (23) AND (29): delta_const = "
          f"{facts.delta_const}; delta_step = {facts.delta_step}; their "
          f"equation (24) ordering 0 < 3*delta_step < delta_const holds "
          f"{facts.delta_ordering_holds}; delta_A02 = {facts.delta_a02}. ALL "
          f"THREE NONZERO AND ALL THREE STANDING -- this block corrects none "
          f"of them")
    print(f"  THE DEFECT LOCALIZATION: {facts.defect_nonzeros} nonzero "
          f"entries, {facts.defect_inter_slice_entries} of them connecting "
          f"different times, all intra-slice "
          f"{facts.defect_all_intra_slice}, maximum magnitude "
          f"{facts.defect_max_magnitude}. THE TEMPORAL LINKS ARE "
          f"REFLECTION-EXACT AND THE OBSTRUCTION IS THE GRADING SPLIT")
    print(f"  THE STRUCTURE: H_image is P-even at "
          f"{facts.image_p_even_residual} while the SIGNED cell map fails the "
          f"same identity at {facts.signed_image_residual}; d_K carries "
          f"{facts.raising_nonzeros} entries, the restricted set A carries "
          f"{facts.restricted_nonzeros} and D = A - P A P carries EXACTLY "
          f"{facts.glue_nonzeros}; D is P-odd at {facts.d_p_odd_residual}, "
          f"agrees with d_K on the interior of the positive half "
          f"{facts.d_matches_interior}, and is NOT d_K globally "
          f"{not facts.glue_equals_raising}. D^2 has "
          f"{facts.glue_nilpotent_residual} nonzero entries, so THE GLUE IS "
          f"NOT NILPOTENT AND NO NILPOTENCY IS CLAIMED FOR IT ANYWHERE: "
          f"Q_glued is a PAIRING, not a differential complex. P Q_glued P = "
          f"Q_glued^T at {facts.glued_transpose_residual}, and the inverse "
          f"inherits it at {facts.glued_inverse_covariance_residual}")
    print(f"  THE RESULT: the glued Gram's Hermiticity defect is "
          f"{facts.glued_delta}, WHICH FOLLOWS STRUCTURALLY from transpose "
          f"covariance PLUS the construction's exact reality "
          f"({facts.glued_reality_holds}) PLUS invertibility -- and NOT from "
          f"covariance alone, as the measured one-dimensional counterexample "
          f"P = [1], Q = [i] shows: covariance holds "
          f"{facts.counterexample_covariance_holds}, Gram Hermitian "
          f"{facts.counterexample_gram_hermitian}, defect "
          f"{facts.counterexample_defect}. The sign vector is "
          f"{facts.glued_signs}, WHICH DOES NOT FOLLOW FROM ANY OF THEM AND IS "
          f"THE NEW CONTENT. THE MINORS: "
          f"{tuple(str(value) for value in facts.glued_minors)}")
    print(f"  THE NECESSITY CONTROLS: seam sign vectors -- neither "
          f"{facts.no_seam_signs}, near {{7,0}} only "
          f"{facts.near_seam_only_signs}, far {{3,4}} only "
          f"{facts.far_seam_only_signs} -- ALL THREE STILL HERMITIAN "
          f"{facts.seam_variants_all_hermitian} at defects "
          f"{facts.seam_variant_deltas}, so the seams carry POSITIVITY and not "
          f"Hermiticity. The P-EVEN variant D' = A + P A P fails covariance at "
          f"max norm {facts.p_even_covariance_max_norm} with Gram defect "
          f"{facts.p_even_delta}; the RAW H(-c) negative half with the same D "
          f"fails at max norm {facts.raw_image_covariance_max_norm} -- BLOCK "
          f"107 EQUATION (17)'s OWN 65/576 -- with Gram defect "
          f"{facts.raw_image_delta}. NECESSITY IS WITHIN THE TESTED FAMILY, "
          f"NOT ACROSS ALL CONCEIVABLE CONSTRUCTIONS")
    print(f"  THE WINDOW: m = {SECOND_MASS} gives {facts.second_mass_signs} "
          f"and m = {THIRD_MASS} gives {facts.third_mass_signs}; the "
          f"constant-in-x step at c = {SECOND_HISTORY_SHEAR} gives "
          f"{facts.second_history_signs} and the x-alternating reflection-odd "
          f"history gives {facts.x_alternating_signs}. All four are covariant "
          f"and Hermitian {facts.window_points_all_hermitian} at defects "
          f"{facts.window_deltas}. POSITIVITY IS MASS-WINDOWED AND "
          f"HISTORY-WINDOWED; the window's characterization is OPEN and its "
          f"mass-direction boundary is bracketed in {MASS_WINDOW_BRACKET}")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False the note has NOT landed at docs/ yet, there is no draft "
          f"fallback anywhere in this runner, gate H is EXPECTED to fail and "
          f"the gate-H mutation is UNTESTABLE until the note lands. Scope keys "
          f"satisfied: {sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  EXACTNESS: every measured scalar above is an exact sympy "
          f"Rational or Integer and NOT ONE IS A FLOAT "
          f"({facts.exactness_holds}); no tolerance enters any check, the "
          f"volume is sp.Integer(1) and every shear passes through nsimplify, "
          f"because `1/volume` at a Python int would decimalize the Hodge "
          f"block and every number in this runner with it. ELAPSED "
          f"{elapsed_ns // 1_000_000} ms")
    print(f"  THE CORPUS RELATION: Blocks 104, 105, 106, 107, 128 and 181-184 "
          f"STAND EXACTLY AS LANDED and no landed note is edited. BLOCK 107'S "
          f"RAW DELTA IS NOT CORRECTED: their nonzero defects are reproduced "
          f"exactly above, and the Hermitian object here is the SEAM-GLUED "
          f"action, a DIFFERENT operator. Their Section 7 dressing machinery "
          f"is SUPERSEDED AT THIS SCOPE and not refuted -- no dressing is "
          f"applied anywhere in this runner. THE ADVERSARIAL CHECK NARROWED "
          f"SCOPE RATHER THAN OVERTURNING A NUMBER: it supplied the four "
          f"window points and the reality scoping, both of which are GATED "
          f"above. THREE IN-SOLVE CATCHES are recorded as PROCESS in N7 of the "
          f"note: the naive interior-edge glue, the one-sided xpar Gram "
          f"dressing, and the SIGNED cell-map guess -- and the third is GATED "
          f"above at its failure")
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
