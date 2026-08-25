#!/usr/bin/env python3
"""BLOCK 188 -- THE THICK-SEAM WALL AND THE SITE-ADAPTED OS POSITIVITY.

THE RESULT, AND ITS EXACT SCOPE.  On BLOCK 185's OWN seam-glued action -- Block
107's d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32, at the
single fixture (m, c) = (9/20, 5/13) -- THE FULL-HALF OS FAILURE IS LOCALIZED,
EXPLAINED AND PROVED UNREPAIRABLE BY THREE NAMED FAMILIES, AND THEN THE TERMINAL
IS REACHED ON THE OTHER SIDE: a SITE-ADAPTED RE-DERIVATION whose theta_s-paired
cross operator is IDENTICALLY EMPTY and whose reflected Gram is PSD ON THE WHOLE
POSITIVE HALF.  BOTH TERMINALS LAND IN ONE BLOCK, and neither is the other's
correction.

  0. THE CONTROL COMES FIRST AND IT IS BLOCK 185'S OWN NUMBER (C).  The link
     route rebuilt here reproduces their landed first leading minor
     4465961414671029642827787914210419072833144728317065801107200 over
     8932040001245962023277146780748464953706237777456506835365883
     DIGIT-FOR-DIGIT, with the glue D at exactly 72 nonzero entries, P-odd at
     zero residual, the A02-image geometry P-even at zero and the transpose
     covariance P Q P = Q^T at zero.  NOTHING BELOW IS ABOUT THEIR OBJECT IF
     THIS IS NOT EXACT.

  1. THE REFLECTION SPLIT IS EXACT AND THE SEAM HAS THICKNESS TWO (C).  The
     theta-transported negative-half block equals the positive-half block
     transposed at ZERO residual, so the entire full-half OS question reduces to
     the theta-paired cross operator C[a,b] = Q[a, theta b] -- 16x16, symmetric,
     FULL RANK 16.  Its support is exactly SIX slice blocks: the near-seam
     {(0,0), (0,1), (1,0)} and the far-seam {(2,3), (3,2), (3,3)}.  THE SEAM IS
     TWO SLICES THICK, which the band census of the action already forces: the
     nonzero entries sit in bands {0: 96, +/-1: 56 each, +/-2: 24 each}, and the
     +/-2 bands cross the cut.  The classic single-bond Osterwalder-Seiler
     argument does not apply to a depth-2 coupling.

  2. THE CLOSED FORM, AND THE MECHANISM THEOREM (C).  The action commutes with
     the spatial shift, so C decomposes by x-momentum p with omega_p = i^p.  In
     EVERY sector each seam contributes the 2x2 block
     [[-601/576, (65/1152) omega_p], [conj, 0]] -- the direct seam bond is the
     PURE SCALAR -601/576 with no shear content at all, and the THICKNESS
     coupling 65/1152 sits off-diagonal against a ZERO diagonal.  Therefore
     det(block) = -|65/1152|^2 < 0 WHENEVER THE THICKNESS COUPLING IS NONZERO:
     EACH 2x2 SEAM BLOCK IS FORCED INDEFINITE.  Per sector C has inertia
     (2, 2, 0) and in total (8, 8, 0), by EXACT CONGRUENCE -- exactly matching
     the raw full-half Gram's own (8, 8, 0).  THE FULL-HALF FAILURE IS THE SEAM
     OPERATOR'S SHEAR-CARRYING THICKNESS, localized and explained.

  3. THREE REPAIR FAMILIES, EACH MEASURED TO FAIL (D).  All exact, on the two
     REAL momentum sectors p = 0 and p = 2, which are Block 107's "both spatial
     eigenlines".  (R1) DRESSINGS ARE BARRED BY A THEOREM: the reflected Gram is
     REAL, so every diagonal or local dressing acts as a CONGRUENCE and Sylvester
     forbids it from moving the inertia; the S-sandwich S K S is measured anyway
     and returns the same sector signature (+,+,-,+) at inertia (2, 2, 0).
     (R2) THE GRAM-SIDE SIGN INSERTION theta' = theta compose sign(C) BREAKS
     SYMMETRY: S K has 12 asymmetric entries per real sector, so it is not a
     pairing at all.  (R3) THE ACTION-SIDE SEAM-MODULUS SURGERY C -> |C| = S C
     is built and verified -- |C| is symmetric and POSITIVE DEFINITE, the polar
     action is reflection-covariant at ZERO residual with NONZERO determinant --
     AND THE POLAR GRAM IS STILL INDEFINITE at (+,+,-,+) and inertia (2, 2, 0).
     THE THICK SEAM DEFEATS BLOCK-LEVEL PSD-NESS.

  4. THE SITE-ADAPTED RE-DERIVATION (E).  The site reflection theta_s(t) = -t
     fixes slices {0, 4} and pairs every cell under thA_s(t) = -1-t, so there
     are NO fixed anchors.  The site-adapted glued Hodge takes the physical
     anchors {0..3} at the uniform step c and the image anchors {4..7} as the
     UNFLIPPED P_4-images of their thA_s partners: Ps H Ps = H at ZERO residual
     with the BARE permutation, no xpar dressing and no shear flip.  THE
     CONTRAST WITH THE LINK ROUTE IS ITSELF A FINDING and it is measured, not
     asserted: the FLIPPED variant fails at EXACTLY 64 entries.  The glue is the
     d_K entries in the CLOSED half {0..4} EXCLUDING the fixed-slice spatial
     edges -- a DESIGN-FORCED modification, DISCLOSED with its exact effect: D_s
     differs from d_K at exactly 24 entries on the six time-cells (0,0), (4,4),
     (5,4), (5,5), (6,6) and (7,7), and nowhere on the physical interior.  D_s
     is Ps-ODD at zero and Ps Q_s Ps = Q_s^T at zero.  AND THE ROUTES ARE NOT
     VARIANTS OF EACH OTHER: the site permutation applied to the LINK action
     fails covariance at EXACTLY 240 entries.

  5. THE EMPTY CROSS, AND FULL-SPAN POSITIVITY (F).  The theta_s-paired cross
     operator over the strictly-positive slices {1,2,3} x Z4 is IDENTICALLY
     ZERO, and so is the whole Q_s block between {1,2,3} and {5,6,7} in both
     directions -- AND IT IS SUPPORT EMPTINESS AND NOT CANCELLATION, since each
     of m H, H D_s and -D_s^T H is separately zero on that block.  NO DIRECT
     COUPLING CROSSES THE SITE CUT: the thick-seam obstruction VANISHES BY
     CONSTRUCTION rather than being repaired.  The reflected Gram is then PSD on
     the full positive span: on slices {1,2} ALL EIGHT leading minors are
     STRICTLY POSITIVE; on {1,2,3} eight positive then four zeros; on
     {0,1,2,3} eight positive then eight zeros.  AND THE CERTIFICATE IS THE
     CHECK'S, NOT THE MINOR SEQUENCE: reordered so the positive-definite core
     leads, each larger span's SCHUR COMPLEMENT IS IDENTICALLY ZERO -- 0_4 and
     0_8 -- so each is congruent to the core direct-sum a zero block and the
     TRUE INERTIAS ARE (8,0,0), (8,0,4) and (8,0,8) exactly.

  6. AND THE FOUR LEGS THE CHECK RAN, ONE OF WHICH IS A REFUTATION (G).  THE
     NAIVE RECONSTRUCTION TRANSFER T = K_c^-1 L IS NOT THE OS TRANSFER, on
     three exact counts: L is not symmetric (48 entries, with an exact rational
     witness), T is not K_c-self-adjoint (48 entries), and its exact spectrum
     is 2 roots in (0,1), 2 NEGATIVE real and 4 NONREAL by exact Sturm on a
     rational factorization of degrees (2, 2, 4).  NO TRANSFER-OPERATOR CLAIM
     SURVIVES THIS BLOCK and the physical-Hilbert-space language stays a
     READING.  THE POSITIVITY SURVIVES TWO FURTHER FIXTURES -- (1, 5/13) and
     (9/20, 3/5), same covariance, same empty cross, same three inertias -- AND
     THREE POINTS ARE STILL NOT A WINDOW.  AND THE SITE CORE IS NOT THE LANDED
     LINK CORE IN DISGUISE: the diagonal-congruence invariant
     sign(K_01 K_14 K_40) is -1 for the site core and +1 for the link core, so
     the two positive Grams are neither equal nor diagonally congruent.

WHAT IS NOT CLAIMED, STATED ONCE: NO GENERALITY -- THREE fixtures on ONE
carrier, with no bracket, no ray and no edge, so the SITE route has no window;
NO TRANSFER OPERATOR -- the naive candidate is REFUTED here and the proper
construction is a named open leg, so the physical-Hilbert-space reading stays a
READING; NO GRAVITY CONSTRAINT QUOTIENT -- Block 107's step 3, whose
PREREQUISITE this block supplies and which it does not execute; and the
LINK-ROUTE WALL IS PER-PAIRING AND PER-FRAME, not a curved-OS no-go of any kind.
BLOCK 185 IS NOT CORRECTED: their number is reproduced digit-for-digit, their
windowed positivity stands, and the site core is measured to be a DIFFERENT
object from their link core rather than a rival account of the same one.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 187 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the eight audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: the imposed objects of
     BOTH routes, ZERO registered and ZERO adopted, with the constraint
     quotient, the generality and the transfer operator all declared NOT CLAIMED
     as measured constants.
  C  THE LINK-ROUTE STRUCTURE: Block 185's own number as the control, the band
     census, the exact reflection split, the seam operator's symmetry, rank and
     six-block support, the per-sector closed form entrywise, the forced
     negative determinant, and C's (8, 8, 0) inertia by exact congruence.
  D  THE MECHANISM AND THE THREE REPAIR FAILURES: the congruence lemma with its
     measured S-sandwich and BOTH readings gated separately, since a
     leading-minor sign vector is NOT an inertia; the sign insertion's
     asymmetry and its full-rank commutator; and the seam-modulus surgery in
     ALL THREE ways the action admits it, with its exact closed forms, its PD
     modulus, its covariant nonzero-determinant polar actions and its
     STILL-NOT-PSD polar Grams in every branch.
  E  THE SITE CONSTRUCTION: the bare-permutation Hodge invariance, the flipped
     variant's exact 64-entry failure, the Ps-odd glue, the 24-entry
     fixed-slice effect on its six cells with exact interior and bond
     agreement, the A-convention fork measured to be an EXACT NO-OP, the site
     covariance together with the precision that Q_s is NOT ordinarily
     symmetric, and the LINK action's exact 240-entry failure under the site
     permutation.
  F  THE EMPTY CROSS AND THE POSITIVITY: the cross measured zero in three
     directions AND term by term, so the emptiness is SUPPORT emptiness and not
     cancellation; the three Grams with their exact sign vectors and the first
     two exact core minors; the EXACT SCHUR certification that actually
     certifies the two degenerate spans, with their true inertias; and the zero
     nsimplify count.
  G  THE FOUR CHECKER LEGS: the naive reconstruction transfer REFUTED on three
     exact counts, the two robustness fixtures, and the triangle-sign
     obstruction separating the site core from the landed link core.
  H  the note at its final path and the N5 fence, byte-identical.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: twenty declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_generality, claim_transfer_operator
    C  break_seam_closed_form, break_seam_det
    D  break_modulus_failure, break_modulus_closed_form
    E  break_site_hodge, break_flip_64, break_covariance_240,
       break_a_convention
    F  break_empty_cross, break_core_minors, break_schur_zero
    G  break_transfer_refutation, break_triangle_sign, break_robustness
    H  drop_n5_fence
  THREE OF THE TWENTY GUARD THE CHECK'S OWN CORRECTIONS: break_schur_zero
  asserts a nonzero Schur complement, which would put the PSD claim back on
  leading minors that cannot carry it; break_transfer_refutation asserts the
  naive transfer self-adjoint, which is exactly the REFUTED leg; and
  claim_transfer_operator asserts the operator the block does not have.  ALL
  THREE MUST FAIL.
  BEFORE LANDING GATE H ALREADY FAILS AT BASELINE, on note-at-final-path alone,
  so drop_n5_fence cannot flip it and THE SWEEP IS RUN AT LANDING, once the note
  sits at docs/ and the baseline is 8 of 8 by family.

RUNNING
  python3 scripts/admissibility_dirac_kahler_site_os_positivity_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation break_empty_cross

NOTES FOR THE LANDING AGENT
  1. NOTHING from any scratchpad is imported OR READ.  BOTH CONSTRUCTIONS ARE
     BUILT DIRECTLY HERE: the staggered kernel with its antiperiodic edge sign,
     the grade projectors, the raising part d_K, BOTH reflections, the offset
     permutation P_4, BOTH restricted raising sets, BOTH derived glues and BOTH
     glued actions.  The LANDED Block 128 runner is imported for EXACTLY TWO
     objects -- cover_embedding() and the Block 105 module's shear_hodge() --
     and for nothing else.  Gate C's first check is the proof that the LINK
     rebuild IS Block 185's object.
  2. EVERY CHECK IS EXACT.  sympy Rational, Integer and exact quadratic surds
     only; no float enters any measured object and no tolerance is used
     anywhere.  Signatures are decided by exact leading principal minors and by
     an EXACT CONGRUENCE chain (symmetric Gaussian elimination, so Sylvester's
     law makes the pivot signs the inertia), never by an eigenvalue estimate.
  3. THE b186 nsimplify HAZARD CARRIES OVER AND THIS RUNNER NSIMPLIFIES NOTHING.
     That call carries a rational TOLERANCE and maps a small nonzero rational to
     EXACTLY ZERO, so a coefficient passed through it can silently lose its
     sign.  Every mass, shear and volume here is ALREADY an exact sympy
     Rational, so nothing needs converting and NOTHING IS CONVERTED.  The
     absence is MEASURED, not promised: gate F counts the occurrences of the
     call in this file's own source and requires zero.
  4. The N5 fence appears byte-identically in the note; gate H checks it as a
     raw substring.
  5. PARENT_COMMIT is the Block 187 tip and PARENT_REF resolves to it; nothing
     needs sed, and CURRENT_MAIN was carried forward from the Block 187 runner
     and re-resolved at draft time.
  6. The stale pin is the Block 186 tip, a real ancestor of HEAD that predates
     Block 187 and carries NEITHER Block 187 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  7. THE REPAIR ANALYSIS IS SCOPED TO THE TWO REAL MOMENTUM SECTORS p = 0 and
     p = 2, which are Block 107's own "both eigenlines".  At p = 1 and p = 3 the
     sector operators are Hermitian rather than symmetric and the real-symmetric
     sign-operator identities do not apply unchanged; the runner MEASURES all
     four sectors' seam blocks and their determinants and gates the repairs at
     the two real ones, and report_measured prints the fact rather than hiding
     it.
  8. THE ADVERSARIAL CHECK LANDED BEFORE THIS RUNNER WAS FINISHED, verdict
     CONFIRMED-WITH-CORRECTION, AND ITS VERDICTS ARE FOLDED RATHER THAN
     APPENDED.  NO SENTINEL REMAINS ANYWHERE IN THIS FILE.  It confirmed the
     structural results exactly on an independent reconstruction; it corrected
     three readings that are now gates -- the leading-minor-sign vector is NOT
     an inertia (correction #16, family D), the PSD certification runs through
     an EXACT SCHUR complement and not through leading minors (family F), and
     the empty cross is exact SUPPORT emptiness measured term by term rather
     than a cancellation (family F); and it REFUTED the naive reconstruction
     transfer outright (family G), which is why no transfer-operator claim
     survives this block and the physical-Hilbert-space language stays a
     reading.
  9. Re-run at landing; gate H should then pass, the battery should be 8/8 by
     family, and the fourteen-mutation sweep should be run then.
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

# THE MACHINERY IMPORT, LANDED, AND DELIBERATELY THIN -- the same two objects
# Blocks 185 and 187 imported and no others: cover_embedding(), whose corner
# order IS the form basis (1, dx, dt, dx^dt), and the Block 105 module it
# re-exports, from which shear_hodge() is read.  Everything else is built here.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 187 is the commit this block's branch
# is cut from, and its note and its runner are the pair that distinguishes the
# parent pin from the stale pin: both exist at PARENT_COMMIT and NEITHER exists
# at STALE_PARENT_COMMIT.
BLOCK187_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK187_RUNNER = (
    "scripts/admissibility_dirac_kahler_positivity_window_characterization_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK187_NOTE, BLOCK187_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "085f46b42ef037984f0d50fe5b882c91a5699050",   # Block 187 note
    "de160d954d8bce6fdebc30597e1ff3d5a8b58066",   # Block 187 runner
)
# THE CONSTRUCTION AUTHORITY.  The LINK route of this block IS Block 185's
# object; their note is the primary body every convention is read from and their
# runner is the code this one re-derives rather than imports.
BLOCK185_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK185_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py"
)
# THE CARRIER AUTHORITY AND THE LADDER THIS BLOCK EXECUTES: Block 107's note.
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_positivity_window_characterization_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
# THE BLOCK'S OWN NOTE is the one audit input gate A does NOT require readable,
# because it does not exist until landing and gate H is the gate that owns it.
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 187 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 187 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block187-"
              "positivity-window-characterization-20260824")
PARENT_COMMIT = "22bc4f5406d1aff3b16d120d1e0a1951faf8b2b2"
# The Block 186 tip: a real ancestor of HEAD that predates Block 187 and
# therefore carries NEITHER Block 187 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "f5bcab65286f03001c8d3b88ad0904afa92588a8"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_generality",
    "claim_transfer_operator",
    "break_seam_closed_form",
    "break_seam_det",
    "break_modulus_failure",
    "break_modulus_closed_form",
    "break_site_hodge",
    "break_flip_64",
    "break_covariance_240",
    "break_a_convention",
    "break_empty_cross",
    "break_core_minors",
    "break_schur_zero",
    "break_transfer_refutation",
    "break_triangle_sign",
    "break_robustness",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_generality": "B",
    "claim_transfer_operator": "B",
    "break_seam_closed_form": "C",
    "break_seam_det": "C",
    "break_modulus_failure": "D",
    "break_modulus_closed_form": "D",
    "break_site_hodge": "E",
    "break_flip_64": "E",
    "break_covariance_240": "E",
    "break_a_convention": "E",
    "break_empty_cross": "F",
    "break_core_minors": "F",
    "break_schur_zero": "F",
    "break_transfer_refutation": "G",
    "break_triangle_sign": "G",
    "break_robustness": "G",
    "drop_n5_fence": "H",
}
# EVERY FAMILY CARRIES AT LEAST ONE MUTATION, INCLUDING G.  In the draft that
# preceded the adversarial check, family G held four SUPERVISOR-SUPPLIED
# placeholders and carried NO mutation, because a sentinel has no content to
# break.  THE CHECK LANDED AND FILLED ALL FOUR: family G now measures the
# transfer REFUTATION, the two robustness points and the site-versus-link
# triangle obstruction, and carries three mutations of its own.
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
        # THE STALE LEG.  At the Block 186 tip NEITHER Block 187 artifact
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
    "THE LINK ROUTE, WHICH IS BLOCK 185's SEAM-GLUED OBJECT REBUILT HERE from its displayed equations and imported from nothing: Block 107's d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32 with eta_t = 1 and eta_x = (-1)^t, the antiperiodic kernel carrying the far-seam edge sign omega_-(3) = -1, the grade-raising part d_K, the LINK-centered reflection theta(t) = -1-t, the restricted raising set A (both endpoint times in the positive half {0,1,2,3} PLUS every entry on the two seam edge-time pairs {3,4} and {7,0}), the derived glue D = A - P A P at 72 nonzero entries, the P-even A02-image geometry at the UNSIGNED offset permutation P_4 and the anchor reflection theta_A(t) = -2-t, the completion Q = m*H + H*D - D^T*H and the dressing K_ab = conj(G(b, theta a))",
    "THE THETA-PAIRED SEAM OPERATOR C[a,b] = Q[a, theta b] ON THE POSITIVE HALF {0,1,2,3} x Z4, WHICH IS THIS BLOCK'S OWN OBJECT, together with its x-momentum decomposition at omega_p = i^p, its per-sector 2x2 closed form, its exact sign operator S = sign(C) = (2C - tr(C_block) I)/sqrt(tr^2 - 4 det) built from EXACT QUADRATIC SURDS, and the polar action obtained by the seam-modulus surgery C -> |C| = S C",
    "THE SITE-ADAPTED RE-DERIVATION, WHICH IS THIS BLOCK'S OWN OBJECT AND NOT A VARIANT OF BLOCK 185's: the SITE reflection theta_s(t) = -t with the fixed slices {0,4} and the anchor pairing thA_s(t) = -1-t, the site-adapted glued Hodge with the physical anchors {0..3} at the UNIFORM step c = 5/13 and the image anchors {4..7} the UNFLIPPED P_4-images of their thA_s partners, the site raising set A_s of the d_K entries in the CLOSED half {0..4} EXCLUDING the fixed-slice spatial edges at t = 0 and t = 4, the derived glue D_s = A_s - Ps A_s Ps and the same completion convention",
    "THE THREE FIXTURES (9/20, 5/13), (1, 5/13) and (9/20, 3/5) at unit volume -- the first is BLOCK 185's and BLOCK 107's and the other two are the adversarial check's robustness points -- AND THREE POINTS ARE NOT A WINDOW: no bracket, no ray, no edge and no interior is established for the site route",
    "THE NAIVE RECONSTRUCTION TRANSFER T = K_c^-1 L, with K_c the positive-definite two-slice core and L the same pairing with the column anchors advanced one slice, BUILT HERE ONLY IN ORDER TO BE REFUTED: it is the object the rank-8 reading invites, and measuring it to fail is what keeps that reading a reading",
    "Block 128's LANDED cover_embedding(), whose corner order IS the form basis (1, dx, dt, dx^dt), and the LANDED Block 105 shear_hodge() block it re-exports: THE ONLY TWO OBJECTS IMPORTED BY THIS RUNNER",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS rather than prose, so
# the B mutations bite on an object.  ALL THREE ARE FALSE AND STAY FALSE.
CONSTRAINT_QUOTIENT_CLAIMED = False
GENERALITY_CLAIMED = False
TRANSFER_OPERATOR_CLAIMED = False

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
HALF_SIZE = 16
GLUE_NONZEROS = 72
FIXTURE_MASS = sp.Rational(9, 20)
FIXTURE_SHEAR = sp.Rational(5, 13)
UNIT_VOLUME = sp.Integer(1)
B185_FIRST_MINOR = sp.Rational(
    4465961414671029642827787914210419072833144728317065801107200,
    8932040001245962023277146780748464953706237777456506835365883)

# --- C: THE LINK-ROUTE STRUCTURE -------------------------------------------
# THE BAND CENSUS of the glued action, keyed by SIGNED slice offset.  The +/-2
# bands are what make the seam TWO SLICES THICK.
BAND_CENSUS = {-2: 24, -1: 56, 0: 96, 1: 56, 2: 24}
SEAM_RANK = 16
SEAM_SUPPORT = ((0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3))
SEAM_DIRECT_BOND = sp.Rational(-601, 576)
SEAM_THICKNESS_COUPLING = sp.Rational(65, 1152)
# THE p = 0 SECTOR BLOCKS, entrywise, at omega_0 = 1.  BOTH SEAMS ARE IDENTICAL.
SEAM_BLOCK_AT_ZERO = ((SEAM_DIRECT_BOND, SEAM_THICKNESS_COUPLING),
                      (SEAM_THICKNESS_COUPLING, sp.Integer(0)))
SEAM_BLOCK_DET = -SEAM_THICKNESS_COUPLING ** 2
SEAM_INERTIA = (8, 8, 0)
SECTOR_INERTIA = (2, 2, 0)
REAL_SECTORS = (0, 2)
ALL_SECTORS = (0, 1, 2, 3)

# --- D: THE MECHANISM AND THE THREE REPAIR FAILURES -------------------------
# THE INDEFINITE SIGNATURE, as the leading-minor sign vector of the 4x4 sector
# object.  (+,+,-,+) has TWO sign changes in the sequence 1, D1, D2, D3, D4, so
# it IS the inertia (2, 2) and it is what every repair below fails to move.
INDEFINITE_SIGNS = (1, 1, -1, 1)
POSITIVE_DEFINITE_SIGNS = (1, 1, 1, 1)
MODULUS_INERTIA = (4, 0, 0)
SIGN_INSERTION_ASYMMETRY = 12
# THE SIGN OPERATOR'S EXACT SURD.  For a 2x2 block B, sign(B) = (2B - tr(B) I) /
# sqrt(tr(B)^2 - 4 det(B)); here tr = -601/576 and det = -(65/1152)^2 in EVERY
# sector, so the discriminant is a SINGLE surd and the eigenvalues are
# (-601 +/- sqrt(365426)) / 1152.
SIGN_DISCRIMINANT = sp.sqrt(365426) / 576
SEAM_EIGENVALUES = ((-601 - sp.sqrt(365426)) / 1152,
                    (-601 + sp.sqrt(365426)) / 1152)
# |C|'s four exact leading minors per real sector, surds included.
MODULUS_MINORS = (
    242209 * sp.sqrt(365426) / 140323584,
    sp.Rational(4225, 1327104),
    17850625 * sp.sqrt(365426) / 558671968862208,
    sp.Rational(17850625, 1761205026816),
)

# --- E: THE SITE CONSTRUCTION ----------------------------------------------
FLIPPED_HODGE_FAILURE = 64
SITE_GLUE_NONZEROS = 56
SITE_DIFFERENCE_COUNT = 24
SITE_DIFFERENCE_CELLS = ((0, 0), (4, 4), (5, 4), (5, 5), (6, 6), (7, 7))
LINK_UNDER_SITE_PERMUTATION = 240

# --- F: THE EMPTY CROSS AND THE POSITIVITY ----------------------------------
CORE_SLICES = (1, 2)
THREE_SLICES = (1, 2, 3)
FULL_SLICES = (0, 1, 2, 3)
CORE_SIGNS = (1,) * 8
THREE_SLICE_SIGNS = (1,) * 8 + (0,) * 4
FULL_SLICE_SIGNS = (1,) * 8 + (0,) * 8
CORE_MINOR_1 = sp.Rational(
    250811603701251182926764176363850176714557920003089965221914456500,
    666495028860293624372300921944800123265476111209829299156533225479)
CORE_MINOR_2 = sp.Rational(
    9699265179160355495171233606378759680576921193642386633764164130236400111062250000,
    65542091681979044701359795584266761562795513633598145522262137753727157320281821073)
# THE TRUE INERTIAS, BY EXACT CONGRUENCE AND BY EXACT SCHUR -- the check's B5
# correction, and the distinction that correction #16 is about: a LEADING-MINOR
# SIGN VECTOR IS NOT AN INERTIA, and a sign vector with zeros in it decides
# nothing on its own.
CORE_INERTIA = (8, 0, 0)
THREE_SLICE_INERTIA = (8, 0, 4)
FULL_SLICE_INERTIA = (8, 0, 8)
SCHUR_ORDERS = ((1, 2, 3), (1, 2, 0, 3))
SCHUR_BLOCK_SIZES = (4, 8)
# THE THREE PIECES of Q_s = m H + H D_s - D_s^T H, each measured SEPARATELY on
# the cross-half block: the emptiness is exact SUPPORT emptiness and NOT a
# cancellation between terms.
CROSS_PIECE_COUNT = 3
# --- E: THE A-CONVENTION EQUIVALENCE (the check's B9) -----------------------
A_CONVENTION_EXTRA_ENTRIES = 8
A_CONVENTION_EXTRA_CELLS = ((0, 0), (4, 4))
SITE_BOND_CELLS = ((0, 1), (1, 0), (3, 4), (4, 3))
SITE_ASYMMETRY = 144
# --- G: THE FOUR CHECKER LEGS, ALL MEASURED --------------------------------
# (B6) THE NAIVE RECONSTRUCTION TRANSFER, REFUTED.  T = K_c^-1 L with the
# slice-shifted pairing L is NOT the OS transfer: L is not symmetric, T is not
# K_c-self-adjoint, and the spectrum is nothing like a positive transfer's.
TRANSFER_L_ASYMMETRY = 48
TRANSFER_SELF_ADJOINT_DEFECT = 48
TRANSFER_WITNESS = sp.Rational(
    444512097856708184009271627180561519494827562500,
    6777562511292598590019138125314219038186300704417)
SPECTRAL_SYMBOL = sp.Symbol("lam")
TRANSFER_FACTORS = (
    1553815 * SPECTRAL_SYMBOL ** 2 + 922978 * SPECTRAL_SYMBOL - 1581193,
    7769075 * SPECTRAL_SYMBOL ** 2 + 9188446 * SPECTRAL_SYMBOL - 7905965,
    75372031215225 * SPECTRAL_SYMBOL ** 4
    + 159030179762040 * SPECTRAL_SYMBOL ** 3
    + 205233213680578 * SPECTRAL_SYMBOL ** 2
    - 70021643952600 * SPECTRAL_SYMBOL + 27721850465625,
)
TRANSFER_FACTOR_DEGREES = (2, 2, 4)
# (in (0,1), negative real, nonreal) -- by EXACT STURM, no root isolation.
TRANSFER_CENSUS = (2, 2, 4)
# (B7) THE ROBUSTNESS POINTS.  Two more fixtures, and TWO MORE POINTS ARE NOT A
# WINDOW: generality stays NOT CLAIMED in the banner.
ROBUSTNESS_POINTS = ((sp.Integer(1), sp.Rational(5, 13)),
                     (sp.Rational(9, 20), sp.Rational(3, 5)))
# (B8) THE TRIANGLE-SIGN OBSTRUCTION.  A diagonal congruence multiplies the
# triangle K_01 K_14 K_40 by a POSITIVE SQUARE, so its sign is an INVARIANT of
# the diagonal-congruence class: -1 for the SITE core and +1 for the LINK core
# means the two positive Grams are NOT diagonally congruent and are NOT gauge
# copies of one another.
TRIANGLE_INDICES = ((0, 1), (1, 4), (4, 0))
SITE_TRIANGLE_SIGN = -1
LINK_TRIANGLE_SIGN = 1
LINK_CORE_SLICES = (0, 1)
# --- D: THE POLAR CONVENTIONS AND THEIR EXACT CLOSED FORMS ------------------
SEAM_TRACE = sp.Rational(-601, 576)
MODULUS_DETERMINANT = SEAM_THICKNESS_COUPLING ** 16
FULL_MODULUS_INERTIA = (16, 0, 0)
SIGN_COMMUTATOR_RANK = 4
# The three ways the seam-modulus surgery can be written into the action, and
# NOT ONE OF THEM IS PSD.  C' = Q[theta b, a] is measured to be EXACTLY -C, so
# the sign-preserving branch is the one that respects that antisymmetry -- and
# it flips the Gram to NEGATIVE DEFINITE rather than repairing it, which closes
# the sign-convention branch the solve named as an attack surface.
POLAR_CONVENTIONS = ("one-sided", "symmetric", "sign-preserving")
SYMMETRIC_POLAR_DETERMINANT = sp.Rational(
    4384437304032745240319804044070026581721,
    71911150569763408538286482364825600000000)
SIGN_PRESERVING_POLAR_DETERMINANT = sp.Rational(
    514799026529233365094404498279125051370889,
    647200355127870676844578341283430400000000)
SIGN_PRESERVING_SIGNS = (-1, 1, -1, 1)
SIGN_PRESERVING_INERTIA = (0, 4, 0)

# THE CITATION PINS, read from the PRIMARY BODIES so the ladder this block
# executes, the steelman it realizes, the construction it rebuilds and the scope
# firewall that made the whole line admissible all have a measured referent.
B107_LADDER_PIN = ("Derive the transfer/polar structure of the curved seam "
                   "kernel and its induced (nonlocal) reflection transporter")
B107_ROUTE_PIN = ("| transfer/polar transporter | live, action-derived, and "
                  "axiom-free | compute it and retest both eigenlines |")
B107_STEELMAN_PIN = ("physical shear channel and could change the two-history "
                     "pairing in a way no")
B107_NOT_A_NOGO_PIN = "This is not a curved OS no-go."
B185_SPAN_PIN = "THE FULL POSITIVE-TIME SPAN IS BUILT"
B187_QUOTIENT_PIN = ("AND THE CONSTRAINT QUOTIENT STAYS DOWNSTREAM OF ALL "
                     "FIVE, in flight on its own thread and untouched by "
                     "anything in this note.")

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
# EXACTLY ZERO, so a coefficient or a minor passed through it can silently lose
# its sign, which is precisely how a positivity verdict would be manufactured.
# Here every mass, shear and volume is ALREADY an exact sympy Rational, so
# nothing needs converting and nothing is converted.  Gate F counts the
# occurrences of the call in this file's own source and requires ZERO.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def reduce_exact(expression: object) -> object:
    """EXACT SURD NORMALIZATION, and it is NOT a tolerance.  Every scalar in this
    runner lies in Q(sqrt(365426)); expand plus radsimp puts it in the canonical
    u + v*sqrt(365426) form with u, v exact rationals, so `== 0` is a decision
    and never an approximation.  No float is created at any point."""
    return sp.radsimp(sp.expand(expression))


def reduce_matrix(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(matrix).applyfunc(reduce_exact)


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact reduction.  A
    count of 0 is the exact zero-matrix statement and no tolerance is involved
    at any point."""
    return nonzero_entries(reduce_matrix(matrix))


def leading_minors(matrix: sp.Matrix) -> tuple:
    """THE LEADING PRINCIPAL MINORS, exact determinants by the Berkowitz
    algorithm: no eigenvalue estimate, no numerical factorization and no
    tolerance enters the decision."""
    return tuple(reduce_exact(matrix[:size, :size].det(method="berkowitz"))
                 for size in range(1, matrix.rows + 1))


def minor_signs(minors: tuple) -> tuple:
    """THE SIGN VECTOR, in {+1, 0, -1}."""
    return tuple(int(sp.sign(value)) for value in minors)


def inertia(matrix: sp.MatrixBase) -> tuple:
    """THE EXACT INERTIA (n+, n-, n0) BY CONGRUENCE, and this is the honest
    instrument that leading minors are not.  Symmetric Gaussian elimination is a
    chain of congruences A -> E^T A E, so SYLVESTER'S LAW OF INERTIA makes the
    signs of the pivots the inertia itself.  When every diagonal entry of the
    active block vanishes the hyperbolic step E: col_i -> col_i + col_j is
    applied, which is again a congruence.  A run of leading minors with ZEROS in
    it decides nothing on its own; this does."""
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
            active = reduce_matrix(hyperbolic.T * active * hyperbolic)
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
                reduced[a, b] = reduce_exact(
                    active[i, j] - active[i, pivot] * active[pivot, j] / value)
        active = reduced
    return positive, negative, null


def is_exact_real(value: object) -> bool:
    """EXACT means an algebraic number with NO float anywhere in it: the
    rationals of both routes and the quadratic surds of the polar route."""
    expression = sp.sympify(value)
    return bool(not expression.atoms(sp.Float)
                and expression.is_algebraic
                and expression.is_real)


# ---------------------------------------------------------------------------
# THE CARRIER AND THE TWO CONSTRUCTIONS, BUILT DIRECTLY
# ---------------------------------------------------------------------------
# BLOCK 107 EQUATION (15): the offset permutation, an UNSIGNED corner swap.
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])
FAR_SEAM = frozenset({3, 4})
NEAR_SEAM = frozenset({7, 0})
BOTH_SEAMS = (FAR_SEAM, NEAR_SEAM)
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
    everywhere else, and every bond is antisymmetrized."""
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
    """P e_(t,x) = e_(theta(t),x).  BOTH reflections are built by this one
    routine: theta(t) = -1-t is the LINK-centered one Blocks 107 and 185 use,
    and theta_s(t) = -t is the SITE-centered one this block re-derives on."""
    matrix = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            matrix[site_index(theta(time), space),
                   site_index(time, space)] = 1
    return matrix


def link_theta(time: int) -> int:
    return (-1 - time) % TIME_EXTENT


def site_theta(time: int) -> int:
    return (-time) % TIME_EXTENT


def link_anchor_theta(time: int) -> int:
    """BLOCK 107's anchor reflection theta_A(t) = -2-t, one slice OFF the link
    reflection: it is what carries the image geometry on the link route."""
    return (-2 - time) % TIME_EXTENT


def site_anchor_theta(time: int) -> int:
    """thA_s(t) = -1-t.  Under it EVERY cell pairs and NO anchor is fixed, which
    is the structural difference from the link route's forced-flat anchors."""
    return (-1 - time) % TIME_EXTENT


def shear_block(shear: object, volume: object) -> sp.Matrix:
    """The LANDED Block 105 shear Hodge, read through Block 128, at an EXACT
    rational shear and an EXACT rational volume.  NO nsimplify: both arguments
    are already sympy Rationals or Integers."""
    return b128.block105.shear_hodge(shear, volume)


def anchor_block(local_shear: object) -> sp.Matrix:
    """At a ZERO-SHEAR anchor the block is the EXACT IDENTITY, which is what the
    landed shear Hodge returns at zero shear and unit volume."""
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


def step_history(shear: object) -> tuple:
    """BLOCK 107 EQUATION (19): the reflection-odd step, with the two straddling
    anchors t = 3 and t = 7 FLAT by antisymmetry rather than by prescription."""
    return (shear, shear, shear, sp.Integer(0),
            -shear, -shear, -shear, sp.Integer(0))


def link_image_hodge(shear: object) -> sp.Matrix:
    """BLOCK 185's GLUED HODGE, exactly: the POSITIVE times carry their own
    anchor blocks and the NEGATIVE times carry P_4 B(theta_A(t)) P_4^T at the
    ANCHOR reflection theta_A(t) = -2-t (Block 107 equation (27))."""
    history = step_history(shear)
    blocks = []
    for time in range(TIME_EXTENT):
        if time in POSITIVE_TIMES:
            blocks.append(anchor_block(history[time]))
        else:
            blocks.append(sp.expand(
                OFFSET_PERMUTATION * anchor_block(history[link_anchor_theta(time)])
                * OFFSET_PERMUTATION.T))
    return assemble_hodge(tuple(blocks))


def site_image_hodge(shear: object, flipped: bool = False) -> sp.Matrix:
    """THE SITE-ADAPTED GLUED HODGE, WHICH IS THIS BLOCK'S OWN OBJECT.  The
    physical anchors {0..3} carry the UNIFORM step block B(c); the image anchors
    {4..7} carry the P_4-image of their thA_s partner's block, UNFLIPPED.
    `flipped=True` is the REFUTED VARIANT -- the same image geometry with the
    step history's sign flip on the shear -- and it exists here so that the
    contrast with the link route is MEASURED rather than asserted."""
    physical = anchor_block(shear)
    image_source = anchor_block(-shear) if flipped else physical
    blocks = []
    for time in range(TIME_EXTENT):
        if time in POSITIVE_TIMES:
            blocks.append(physical)
        else:
            # thA_s(t) = -1-t lands every image anchor in {0..3}, where the step
            # is uniform, so the partner lookup is a statement about geometry
            # rather than about which entry of a history is read.
            assert site_anchor_theta(time) in POSITIVE_TIMES
            blocks.append(sp.expand(OFFSET_PERMUTATION * image_source
                                    * OFFSET_PERMUTATION.T))
    return assemble_hodge(tuple(blocks))


def link_restricted_raising(raising: sp.Matrix) -> sp.Matrix:
    """A: the d_K entries with BOTH endpoint times in the positive half, PLUS
    every d_K entry on each of the two seam edge-time pairs."""
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            keep = row_time in POSITIVE_TIMES and column_time in POSITIVE_TIMES
            if frozenset({row_time, column_time}) in BOTH_SEAMS:
                keep = True
            if keep:
                result[row, column] = raising[row, column]
    return result


def site_restricted_raising(raising: sp.Matrix) -> sp.Matrix:
    """A_s: the d_K entries with BOTH endpoint times in the CLOSED half {0..4},
    EXCLUDING the spatial edges that live INSIDE a fixed slice.

    THE EXCLUSION IS DESIGN-FORCED AND IT IS DISCLOSED RATHER THAN BURIED.  A
    spatial edge with both endpoints at t = 0 or both at t = 4 is Ps-INVARIANT,
    so it cancels identically in the odd glue D_s = A_s - Ps A_s Ps and cannot
    contribute; keeping it would only add a Ps-even piece to a construction
    whose whole point is Ps-oddness.  Its exact effect is MEASURED in gate E:
    D_s differs from d_K at 24 entries on six named time-cells and NOWHERE on
    the physical interior."""
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
    """BLOCK 107 EQUATION (21): Q = m*H + H*D - D^T*H, used UNCHANGED on BOTH
    routes, so no comparison here is between different conventions."""
    return sp.expand(mass * hodge + hodge * glue - glue.T * hodge)


def band_census(action: sp.Matrix) -> dict:
    """THE NONZERO ENTRIES BY SIGNED SLICE OFFSET.  The +/-2 bands are the
    measured reason the seam is TWO SLICES THICK."""
    census: dict = {}
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if action[row, column] == 0:
                continue
            offset = (row // SPACE_EXTENT - column // SPACE_EXTENT) % TIME_EXTENT
            if offset > TIME_EXTENT // 2:
                offset -= TIME_EXTENT
            census[offset] = census.get(offset, 0) + 1
    return census


def slice_indices(slices: tuple) -> tuple:
    return tuple(site_index(t, x) for t in slices for x in range(SPACE_EXTENT))


def reflected_indices(slices: tuple, theta) -> tuple:
    return tuple(site_index(theta(t), x)
                 for t in slices for x in range(SPACE_EXTENT))


def paired_gram(inverse: sp.Matrix, slices: tuple, theta) -> sp.Matrix:
    """BLOCK 107 EQUATION (7)/(22): K_ab = conj(G(b, theta a)), on whichever
    span and whichever reflection is handed in."""
    anchors = slice_indices(slices)
    partners = reflected_indices(slices, theta)
    gram = sp.zeros(len(anchors), len(anchors))
    for row in range(len(anchors)):
        for column in range(len(anchors)):
            gram[row, column] = sp.conjugate(inverse[anchors[column],
                                                     partners[row]])
    return sp.expand(gram)


def sector_map(momentum: int) -> sp.Matrix:
    """THE x-MOMENTUM SECTOR EMBEDDING.  The glued LINK action commutes with the
    spatial shift, so it block-diagonalizes at omega_p = i^p; W_p is 32x8 with
    W_p^dagger W_p = I, and Q_p = W_p^dagger Q W_p is the exact 8x8 sector
    action.  Blocks 107 and 185 called p = 0 and p = 2 'both spatial
    eigenlines'; they are the two REAL sectors and they are where the repair
    families are gated."""
    phase = sp.I ** momentum
    embedding = sp.zeros(COVER_SIZE, TIME_EXTENT)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            embedding[site_index(time, space), time] = phase ** space / 2
    return embedding


def sector_reflection(theta) -> sp.Matrix:
    matrix = sp.zeros(TIME_EXTENT, TIME_EXTENT)
    for time in range(TIME_EXTENT):
        matrix[theta(time), time] = 1
    return matrix


SECTOR_ROWS = [0, 1, 2, 3]
SECTOR_COLUMNS = [link_theta(t) for t in range(4)]


def sign_operator(seam: sp.Matrix) -> sp.Matrix:
    """sign(C) IN CLOSED FORM AND IN EXACT SURDS.  Every 2x2 seam block carries
    the SAME trace -601/576 and the SAME determinant -(65/1152)^2, so the 2x2
    identity sign(B) = (2B - tr(B) I)/sqrt(tr(B)^2 - 4 det(B)) lifts verbatim to
    the whole sector operator: sign(C) = (2C + (601/576) I) / sqrt(365426)/576.
    No square root is ever taken numerically."""
    return reduce_matrix((2 * seam - SEAM_DIRECT_BOND * sp.eye(seam.rows))
                         / SIGN_DISCRIMINANT)


def schur_complement(gram: sp.Matrix, core_size: int) -> sp.Matrix:
    """THE EXACT SCHUR COMPLEMENT of the positive-definite core inside a larger
    span.  With the core A invertible, the span is congruent to A (+) (D -
    B^T A^-1 B), so an IDENTICALLY ZERO Schur complement certifies the inertia
    (n+, 0, n0) exactly -- which is what a leading-minor sequence with zeros in
    it cannot do, and what the check's B5 correction insists on."""
    core = gram[:core_size, :core_size]
    corner = gram[:core_size, core_size:]
    tail = gram[core_size:, core_size:]
    return sp.expand(tail - corner.T * core.inv() * corner)


def triangle_sign(gram: sp.Matrix) -> int:
    """THE DIAGONAL-CONGRUENCE INVARIANT.  Under K -> E K E with E diagonal, the
    product K_01 K_14 K_40 is multiplied by (E_0 E_1 E_4)^2 > 0, so its SIGN is
    an invariant of the diagonal-congruence class.  Two positive Grams with
    opposite triangle signs are NOT diagonally congruent."""
    product = sp.Integer(1)
    for row, column in TRIANGLE_INDICES:
        product *= gram[row, column]
    return int(sp.sign(reduce_exact(product)))


def factor_key(polynomial: sp.Expr) -> tuple:
    poly = sp.Poly(polynomial, SPECTRAL_SYMBOL)
    return (poly.degree(),) + tuple(int(c) for c in poly.all_coeffs())


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
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- THE LINK ROUTE, which is BLOCK 185's SEAM-GLUED OBJECT rebuilt here from its displayed equations (Block 107's d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32, the antiperiodic kernel carrying omega_-(3) = -1 on the FAR seam, the grade-raising d_K, the LINK-centered reflection theta(t) = -1-t, the restricted raising set A of the positive half {0,1,2,3} plus the seam edge-time pairs {3,4} and {7,0}, the derived glue D = A - P A P at 72 nonzero entries, the P-even A02-image geometry at the UNSIGNED P_4 and the anchor reflection theta_A(t) = -2-t, and the completion Q = m*H + H*D - D^T*H), THE THETA-PAIRED SEAM OPERATOR C[a,b] = Q[a, theta b] with its x-momentum decomposition, its exact sign operator S = sign(C) in quadratic surds and the polar actions of the seam-modulus surgery C -> |C| = S C in ALL THREE writings the action admits, THE SITE-ADAPTED RE-DERIVATION (the site reflection theta_s(t) = -t with fixed slices {0,4}, the anchor pairing thA_s(t) = -1-t under which NO anchor is fixed, the site-adapted glued Hodge with the physical anchors {0..3} at the uniform step c = 5/13 and the image anchors {4..7} the UNFLIPPED P_4-images of their thA_s partners, the site raising set A_s of the d_K entries in the CLOSED half {0..4} EXCLUDING the fixed-slice spatial edges, and the derived glue D_s = A_s - Ps A_s Ps), THE THREE FIXTURES (9/20, 5/13), (1, 5/13) and (9/20, 3/5), THE NAIVE RECONSTRUCTION TRANSFER T = K_c^-1 L built here only in order to be REFUTED, and the LANDED Block 128 cover_embedding() and Block 105 shear_hodge() -- THE ONLY TWO OBJECTS IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GENERALITY IS CLAIMED: THREE points on ONE carrier, with no bracket, no ray and no edge, so the SITE route has NO WINDOW. NO TRANSFER OPERATOR IS CLAIMED: the naive candidate is MEASURED TO FAIL and the proper OS construction is a NAMED OPEN LEG, so the physical-Hilbert-space language is a READING and not a measurement. NO GRAVITY CONSTRAINT QUOTIENT IS FORMED. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE CONTROL COMES FIRST AND IT IS BLOCK 185'S OWN NUMBER. The link route rebuilt here reproduces THEIR LANDED FIRST LEADING MINOR 4465961414671029642827787914210419072833144728317065801107200/8932040001245962023277146780748464953706237777456506835365883 DIGIT-FOR-DIGIT, with the glue D at EXACTLY 72 nonzero entries, P-odd at zero residual, the A02-image geometry P-even at zero and the transpose covariance P Q P = Q^T at zero. IF THAT NUMBER MOVED BY A DIGIT the wall characterized below would be a wall of some other object. AND THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's many zeros could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate F.\nper_mode: THE REFLECTION SPLIT IS EXACT AND THE SEAM HAS THICKNESS TWO. The theta-transported negative-half block equals the positive-half block TRANSPOSED at zero residual, so the whole full-half OS question REDUCES to the theta-paired cross operator C[a,b] = Q[a, theta b]: 16x16, SYMMETRIC, FULL RANK 16. Its support is exactly SIX slice blocks -- the near-seam {(0,0), (0,1), (1,0)} and the far-seam {(2,3), (3,2), (3,3)} -- and the action's band census {0: 96, +/-1: 56 each, +/-2: 24 each} is the measured reason: the +/-2 overlap bands CROSS THE CUT. THE CLASSIC SINGLE-BOND OSTERWALDER-SEILER ARGUMENT DOES NOT APPLY TO A DEPTH-2 COUPLING.\nper_block: THE SEAM OPERATOR IN CLOSED FORM, AND THE MECHANISM THEOREM IN ONE LINE. The glued action commutes with the spatial shift, so C decomposes by x-momentum at omega_p = i^p and EACH SEAM CONTRIBUTES THE 2x2 BLOCK [[-601/576, (65/1152) omega_p], [conj, 0]]: the direct seam bond is the PURE SCALAR -601/576 with NO shear content -- the forced-flat anchors showing through -- and the THICKNESS coupling 65/1152 sits off-diagonal against a ZERO diagonal, the slice-1 self-coupling vanishing identically. THEREFORE det(block) = -|65/1152|^2 < 0 WHENEVER THE THICKNESS COUPLING IS NONZERO: EACH 2x2 SEAM BLOCK IS FORCED INDEFINITE BY THE SHEAR-CARRYING THICKNESS. Per sector C has inertia (2,2,0) and in total (8,8,0) BY EXACT CONGRUENCE, EXACTLY MATCHING the raw full-half Gram's own (8,8,0): THE FULL-HALF FAILURE IS THE SEAM OPERATOR'S SHEAR THICKNESS, localized and explained. That 65 = 5*13 is the fixture's shear numerator showing through IS A READING and is marked as one.\nlattice_wide: THREE REPAIR FAMILIES, EACH MEASURED TO FAIL, ON BOTH REAL MOMENTUM SECTORS p = 0 AND p = 2 -- BLOCK 107'S OWN BOTH EIGENLINES. (R1) DRESSINGS ARE BARRED BY A THEOREM AND NOT BY A SAMPLE: the reflected Gram is REAL, so every diagonal or local dressing acts as a CONGRUENCE and Sylvester's law forbids it from moving the inertia; the S-sandwich S K S is measured anyway and returns the SAME leading-minor signs (+,+,-,+) at the SAME inertia (2,2,0) -- AND THOSE ARE TWO DIFFERENT OBJECTS, which is the adversarial check's correction #16 and is gated as two claims: a minor sign vector is NOT an inertia. (R2) THE GRAM-SIDE SIGN INSERTION theta' = theta compose sign(C) BREAKS SYMMETRY: S K carries 12 asymmetric entries per real sector and the commutator S K - K S has FULL RANK 4, so it is NOT A PAIRING AT ALL. (R3) THE ACTION-SIDE SEAM-MODULUS SURGERY C -> |C| = S C is exact algebra, not a numerical root: from C^2 = tr*C + b^2*I one gets S = (2C - tr*I)/delta and |C| = (tr*C + 2b^2*I)/delta with delta = sqrt(365426)/576, det|C| = (65/1152)^16 and |C| POSITIVE DEFINITE at inertia (16,0,0). THE SURGERY IS RUN IN ALL THREE WAYS THE ACTION ADMITS -- one-sided, symmetric, and the sign-preserving writing that respects the measured identity Q[theta b, a] = -C -- ALL THREE reflection-covariant at zero residual with NONZERO determinants, AND NOT ONE OF THEM IS PSD: (2,2,0), (2,2,0) and (0,4,0). THE SIGN-CONVENTION BRANCH IS THEREFORE CLOSED TOO: it flips the Gram to NEGATIVE DEFINITE rather than repairing it. THE THICK SEAM DEFEATS BLOCK-LEVEL PSD-NESS, and the classic argument does not extend through depth-2 couplings by seam surgery alone. THE WALL IS PER-PAIRING AND PER-FRAME AND IS NOT A CURVED-OS NO-GO OF ANY KIND.\nper_scope: THE SITE-ADAPTED RE-DERIVATION, AND THE TERMINAL REACHED FROM THE OTHER SIDE. The site reflection theta_s(t) = -t fixes slices {0,4} and pairs EVERY cell under thA_s(t) = -1-t, so there are NO FIXED ANCHORS. The site-adapted glued Hodge satisfies Ps H Ps = H at ZERO residual with the BARE permutation -- NO xpar dressing and NO shear flip -- and THE CONTRAST WITH THE LINK ROUTE IS ITSELF A FINDING AND IS MEASURED: the FLIPPED variant fails at EXACTLY 64 entries. The glue is the d_K entries in the CLOSED half {0..4} EXCLUDING the fixed-slice spatial edges, AND THAT EXCLUSION IS MEASURED TO BE AN EXACT NO-OP: putting those 8 entries back, supported on the cells (0,0) and (4,4), leaves D_s UNCHANGED because they cancel identically in the oddization -- so the apparent convention is not a fork at all. D_s differs from d_K at EXACTLY 24 entries on the six time-cells (0,0), (4,4), (5,4), (5,5), (6,6), (7,7), and equals d_K EXACTLY on the physical interior {1,2,3} AND on the four bond cells (0,1), (1,0), (3,4), (4,3). D_s is Ps-ODD at zero and Ps Q_s Ps = Q_s^T at zero with the BARE site permutation -- AND THE PRECISION MATTERS: Q_s IS NOT AN ORDINARILY SYMMETRIC MATRIX, its plain symmetry defect being 144 nonzero entries; the property is REFLECTED-TRANSPOSE COVARIANCE and nothing weaker should be read from it. THE TWO ROUTES ARE NOT VARIANTS OF EACH OTHER: the site permutation applied to the LINK action fails covariance at EXACTLY 240 entries. AND THEN THE CROSS OPERATOR IS EMPTY, BY SUPPORT AND NOT BY CANCELLATION: the theta_s-paired cross over the strictly-positive slices {1,2,3} x Z4 is IDENTICALLY ZERO, the whole Q_s block between {1,2,3} and {5,6,7} is zero in BOTH directions, and each of the three terms m*H, H*D_s and -D_s^T*H is SEPARATELY zero there. NO DIRECT COUPLING CROSSES THE SITE CUT, and the thick-seam obstruction that defeated the link route VANISHES BY CONSTRUCTION rather than being repaired. THE REFLECTED GRAM IS PSD ON THE FULL POSITIVE SPAN: on slices {1,2} ALL EIGHT leading minors are STRICTLY POSITIVE; on {1,2,3} eight positive then four zeros; on {0,1,2,3} eight positive then eight zeros -- AND THE CERTIFICATE IS THE EXACT SCHUR COMPLEMENT AND NOT THE MINOR SEQUENCE, because leading minors with zeros in them are NECESSARY AND NOT SUFFICIENT: reordered so the positive-definite core leads, the Schur complements are IDENTICALLY ZERO, 0_4 on {1,2,3} and 0_8 on {0,1,2,3}, so the TRUE INERTIAS ARE (8,0,0), (8,0,4) and (8,0,8) EXACTLY.\nRESULT: THE THICK-SEAM WALL IS CHARACTERIZED, THE SITE-ADAPTED ROUTE IS POSITIVE ON THE FULL SPAN, AND THE TRANSFER LEG IS REFUTED -- ALL THREE IN ONE BLOCK. Block 185's landed first minor is reproduced digit-for-digit as the control; the reflection split is exact; the seam operator is symmetric of full rank 16 on six support blocks; each per-sector 2x2 seam block is [[-601/576, (65/1152) omega_p], [conj, 0]] with determinant -(65/1152)^2 < 0, giving C the inertia (8,8,0) that matches the raw Gram's; three repair families -- congruence dressings, Gram-side sign insertion and action-side seam-modulus surgery in all three writings -- are each measured to fail on both real sectors, and NO sign branch is PSD; the site-adapted Hodge is reflection-invariant under the BARE permutation while the flipped variant fails at 64; the fixed-slice exclusion is an EXACT NO-OP on the glue; the site permutation on the LINK action fails at 240; the cross is EMPTY BY SUPPORT in three directions and term by term; the reflected Gram is PSD of rank 8 on {1,2}, {1,2,3} and {0,1,2,3}, certified by IDENTICALLY ZERO SCHUR COMPLEMENTS at true inertias (8,0,0), (8,0,4) and (8,0,8); the positivity survives two further fixtures (1, 5/13) and (9/20, 3/5) unchanged, WHICH IS THREE POINTS AND NOT A WINDOW; THE NAIVE RECONSTRUCTION TRANSFER T = K_c^-1 L IS REFUTED on three exact counts -- L asymmetric at 48 entries with an exact rational witness, T not K_c-self-adjoint at 48, and an exact spectrum of 2 roots in (0,1), 2 NEGATIVE real and 4 NONREAL from a rational factorization of degrees (2,2,4) -- so NO TRANSFER-OPERATOR CLAIM SURVIVES; and the SITE core and Block 185's LANDED LINK core are measured to be DISTINCT OBJECTS, neither equal nor diagonally congruent, by the diagonal-congruence invariant sign(K_01 K_14 K_40) = -1 against +1. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-187 STAND EXACTLY AS LANDED; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. BLOCK 185 IS NEITHER CORRECTED NOR CONTRADICTED: their fixture number is reproduced here digit-for-digit, their windowed two-slice positivity stands exactly as landed, and their link core is measured to be a DIFFERENT GEOMETRIC OBJECT from the site core rather than a rival account of the same one. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: THREE FIXTURES AND NO WINDOW for the site route -- no bracket, no ray, no edge; THE LINK-ROUTE WALL IS PER-PAIRING AND PER-FRAME and speaks only about the three named repair families on that pairing, the (N2) pencil/transfer polar acting on the PROPAGATION having been named in the solve and NOT run; THE TRANSFER LEG IS A REFUTATION AND NOT A CONSTRUCTION, so the rank-8 PHYSICAL-HILBERT-SPACE LANGUAGE REMAINS A READING and the proper OS transfer is a named open leg; and 65 = 5*13 IS A READING. ONE CORRECTION IS LANDED BY THIS BLOCK AND IT IS THE ADVERSARIAL CHECK'S: correction #16, that a LEADING-MINOR SIGN VECTOR IS NOT AN INERTIA -- the solve's (+,+,-,+) descriptions were minor sequences and the true sector inertia is (2,2,0), and both are now gated separately. Two further readings were tightened by the same check and are now gates rather than prose: the PSD certification runs through an EXACT SCHUR COMPLEMENT and not through leading minors, and the empty cross is exact SUPPORT emptiness measured term by term and not a cancellation. Every in-solve fork -- the site-covariance failure at 240, the flipped image at 64, the fixed-slice edge exclusion -- was MEASURED at its fork, so nothing wrong ever left the solve. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE TRANSFER/POLAR SOLVE, POLAR PHASE 2 and THE SITE-ADAPTED RE-DERIVATION anchors, as corrected and extended by the b188 adversarial check.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
        "constraint_quotient_claimed": CONSTRAINT_QUOTIENT_CLAIMED,
        "generality_claimed": GENERALITY_CLAIMED,
        "transfer_operator_claimed": TRANSFER_OPERATOR_CLAIMED,
        # C -- the link-route structure.
        "citation_pins": True,
        "glue_nonzeros": GLUE_NONZEROS,
        "glue_p_odd_residual": ZERO_RESIDUAL,
        "hodge_p_even_residual": ZERO_RESIDUAL,
        "transpose_covariance_residual": ZERO_RESIDUAL,
        "b185_first_minor": B185_FIRST_MINOR,
        "band_census": BAND_CENSUS,
        "reflection_split_residual": ZERO_RESIDUAL,
        "seam_symmetry_residual": ZERO_RESIDUAL,
        "seam_rank": SEAM_RANK,
        "seam_support": SEAM_SUPPORT,
        "seam_block_at_zero": SEAM_BLOCK_AT_ZERO,
        "seam_block_dets": (SEAM_BLOCK_DET,) * (2 * len(ALL_SECTORS)),
        "seam_inertia": SEAM_INERTIA,
        "sector_seam_inertia": (SECTOR_INERTIA,) * len(REAL_SECTORS),
        # D -- the mechanism and the three repair failures.
        "raw_gram_signs": (INDEFINITE_SIGNS,) * len(REAL_SECTORS),
        "sandwich_signs": (INDEFINITE_SIGNS,) * len(REAL_SECTORS),
        "sandwich_inertia": (SECTOR_INERTIA,) * len(REAL_SECTORS),
        "sign_insertion_asymmetry": (SIGN_INSERTION_ASYMMETRY,) * len(REAL_SECTORS),
        "sign_commutator_rank": (SIGN_COMMUTATOR_RANK,) * len(REAL_SECTORS),
        "modulus_inertia": (MODULUS_INERTIA,) * len(REAL_SECTORS),
        "modulus_minors": (MODULUS_MINORS,) * len(REAL_SECTORS),
        "seam_square_identity": True,
        "modulus_closed_form": True,
        "modulus_determinant": MODULUS_DETERMINANT,
        "full_modulus_inertia": FULL_MODULUS_INERTIA,
        "polar_covariance_residual": {
            name: (ZERO_RESIDUAL,) * len(REAL_SECTORS)
            for name in POLAR_CONVENTIONS},
        "polar_gram_signs": {
            "one-sided": (INDEFINITE_SIGNS,) * len(REAL_SECTORS),
            "symmetric": (INDEFINITE_SIGNS,) * len(REAL_SECTORS),
            "sign-preserving": (SIGN_PRESERVING_SIGNS,) * len(REAL_SECTORS)},
        "polar_gram_inertia": {
            "one-sided": (SECTOR_INERTIA,) * len(REAL_SECTORS),
            "symmetric": (SECTOR_INERTIA,) * len(REAL_SECTORS),
            "sign-preserving": (SIGN_PRESERVING_INERTIA,) * len(REAL_SECTORS)},
        "symmetric_polar_determinant":
            (SYMMETRIC_POLAR_DETERMINANT,) * len(REAL_SECTORS),
        "sign_preserving_polar_determinant":
            (SIGN_PRESERVING_POLAR_DETERMINANT,) * len(REAL_SECTORS),
        # E -- the site construction.
        "site_hodge_residual": ZERO_RESIDUAL,
        "flipped_hodge_residual": FLIPPED_HODGE_FAILURE,
        "site_glue_p_odd_residual": ZERO_RESIDUAL,
        "site_glue_nonzeros": SITE_GLUE_NONZEROS,
        "site_difference_count": SITE_DIFFERENCE_COUNT,
        "site_difference_cells": SITE_DIFFERENCE_CELLS,
        "site_covariance_residual": ZERO_RESIDUAL,
        "site_asymmetry": SITE_ASYMMETRY,
        "site_bond_agreement": ZERO_RESIDUAL,
        "site_interior_agreement_count": ZERO_RESIDUAL,
        "a_convention_extra": A_CONVENTION_EXTRA_ENTRIES,
        "a_convention_cells": A_CONVENTION_EXTRA_CELLS,
        "a_convention_glue_unchanged": True,
        "link_under_site_permutation": LINK_UNDER_SITE_PERMUTATION,
        # F -- the empty cross and the positivity.
        "site_cross_nonzeros": ZERO_RESIDUAL,
        "site_cross_piece_nonzeros": (ZERO_RESIDUAL,) * CROSS_PIECE_COUNT,
        "site_cross_half_nonzeros": (ZERO_RESIDUAL, ZERO_RESIDUAL),
        "core_signs": CORE_SIGNS,
        "core_minor_1": CORE_MINOR_1,
        "core_minor_2": CORE_MINOR_2,
        "three_slice_signs": THREE_SLICE_SIGNS,
        "full_slice_signs": FULL_SLICE_SIGNS,
        # THE CERTIFICATION PROPER, which is the check's B5 correction: the
        # exact Schur complement and the exact congruence inertia, NOT the
        # leading-minor sign vectors.
        "congruence_inertia": (CORE_INERTIA, THREE_SLICE_INERTIA,
                               FULL_SLICE_INERTIA),
        "schur_residuals": (ZERO_RESIDUAL, ZERO_RESIDUAL),
        "schur_block_sizes": SCHUR_BLOCK_SIZES,
        "nsimplify_calls": 0,
        # G -- THE FOUR CHECKER LEGS, ALL MEASURED.
        "transfer_l_asymmetry": TRANSFER_L_ASYMMETRY,
        "transfer_witness": TRANSFER_WITNESS,
        "transfer_self_adjoint": False,
        "transfer_factors": TRANSFER_FACTORS,
        "transfer_factor_degrees": TRANSFER_FACTOR_DEGREES,
        "transfer_census": TRANSFER_CENSUS,
        "robustness_inertia": (
            (CORE_INERTIA, THREE_SLICE_INERTIA, FULL_SLICE_INERTIA),) * 2,
        "site_triangle_sign": SITE_TRIANGLE_SIGN,
        "link_triangle_sign": LINK_TRIANGLE_SIGN,
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
    elif mutation == "claim_generality":
        # THE SINGLE FIXTURE OVERSOLD, AND THIS IS THE BLOCK'S BIGGEST OVERREACH
        # RISK.  "Full-span reflection positivity holds" reads as a statement
        # about the construction unless the banner says otherwise.  It is ONE
        # point of the (m, c) plane, and the site route has no window at all --
        # not even the two-ray sampling Block 187 built for the link route.
        claims["generality_claimed"] = True
    elif mutation == "claim_transfer_operator":
        # THE RECONSTRUCTION OVERSOLD: an induced transfer operator asserted,
        # which is exactly the leg NOT built here.  Without it the rank-8 kernel
        # is a linear-algebra fact and the physical-Hilbert-space language is a
        # reading; asserting the operator turns a reading into a claim.
        claims["transfer_operator_claimed"] = True
    elif mutation == "break_seam_closed_form":
        # THE MECHANISM'S CARRIER DELETED: the thickness coupling asserted ZERO,
        # which is the b = 0 degeneration where the seam WOULD be sign-uniform
        # and the raw pairing WOULD work.  It is measured nonzero, and that is
        # the whole obstruction.
        claims["seam_block_at_zero"] = ((SEAM_DIRECT_BOND, sp.Integer(0)),
                                        (sp.Integer(0), sp.Integer(0)))
    elif mutation == "break_seam_det":
        # THE MECHANISM THEOREM DENIED AT ITS ONE INEQUALITY: the 2x2 seam
        # determinant asserted POSITIVE, which would make each block definite
        # and the thick seam harmless.  The measured value is strictly negative.
        claims["seam_block_dets"] = (-SEAM_BLOCK_DET,) * (2 * len(ALL_SECTORS))
    elif mutation == "break_modulus_failure":
        # THE THIRD REPAIR DECLARED A SUCCESS: the polar Gram asserted POSITIVE
        # DEFINITE, which is precisely what the seam-modulus surgery does NOT
        # deliver.  Without this the block would read as a repair rather than as
        # a wall, which is the single most tempting misreading of the result.
        claims["polar_gram_signs"] = dict(
            claims["polar_gram_signs"],
            **{"one-sided": (POSITIVE_DEFINITE_SIGNS,) * len(REAL_SECTORS)})
    elif mutation == "break_modulus_closed_form":
        # THE POLAR CONSTRUCTION'S ALGEBRA DENIED: |C|'s determinant asserted to
        # be something other than (65/1152)^16, which the exact identity
        # C^2 = a C + b^2 I forbids.  If the closed form moves, the polar leg is
        # not the polar leg and the refutation in (R3) is about another object.
        claims["modulus_determinant"] = MODULUS_DETERMINANT * 2
    elif mutation == "break_site_hodge":
        # THE SITE CONSTRUCTION'S FOUNDATION DENIED: the site-adapted Hodge
        # asserted NOT reflection-invariant under the bare permutation, which
        # would put the site route in exactly the position the link route's
        # naive site test was in.  It is measured invariant at zero.
        claims["site_hodge_residual"] = FLIPPED_HODGE_FAILURE
    elif mutation == "break_flip_64":
        # THE CONTRAST ERASED: the FLIPPED image asserted to work equally well,
        # which would make the unflipped choice arbitrary.  It fails at exactly
        # 64 entries, and that failure is what makes the unflipped image a
        # derived feature of the site geometry rather than a convention.
        claims["flipped_hodge_residual"] = ZERO_RESIDUAL
    elif mutation == "break_covariance_240":
        # THE TWO ROUTES CONFLATED: the site permutation asserted covariant on
        # the LINK action, which would make the site route a re-labelling of
        # Block 185's object instead of a re-derivation.  It fails at exactly
        # 240 entries, and that number is why this block builds a new geometry.
        claims["link_under_site_permutation"] = ZERO_RESIDUAL
    elif mutation == "break_a_convention":
        # THE FIXED-SLICE FORK RE-OPENED AS A REAL FORK: the wider raising set
        # asserted to give a DIFFERENT glue, which would make the exclusion a
        # convention that could have changed the answer. The check measured it
        # an EXACT NO-OP -- the extra entries cancel identically in the
        # oddization -- and that is what removes the fork.
        claims["a_convention_glue_unchanged"] = False
    elif mutation == "break_empty_cross":
        # THE HEADLINE MECHANISM DENIED: a nonzero coupling asserted across the
        # site cut.  The empty cross is the entire reason the thick-seam
        # obstruction is absent here rather than repaired; a nonempty cross
        # would put the site route back inside the wall.
        claims["site_cross_nonzeros"] = 8
    elif mutation == "break_core_minors":
        # THE POSITIVE CORE DENIED: the sixth leading minor of the two-slice
        # core asserted NEGATIVE, which the exact Berkowitz determinants forbid.
        # The strictly positive core is what makes the larger spans' zeros a
        # QUOTIENT rather than a defect.
        claims["core_signs"] = (1, 1, 1, 1, 1, -1, 1, 1)
    elif mutation == "break_schur_zero":
        # THE CERTIFICATE DOWNGRADED BACK TO LEADING MINORS: a NONZERO Schur
        # complement asserted, which would leave the two degenerate spans
        # uncertified, since a sign vector of eight positives and eight zeros
        # does not by itself exclude a negative direction. It is exactly zero.
        claims["schur_residuals"] = (1, 1)
    elif mutation == "break_transfer_refutation":
        # THE REFUTED LEG DECLARED A SUCCESS: the naive transfer asserted to be
        # K_c-self-adjoint, which is what an OS transfer would have to be. The
        # measured defect is 48 entries, and this mutation is what stops the
        # rank-8 reading from quietly acquiring an operator it does not have.
        claims["transfer_self_adjoint"] = True
    elif mutation == "break_triangle_sign":
        # THE TWO POSITIVE OBJECTS CONFLATED: the SITE core's triangle sign
        # asserted equal to the LINK core's, which would make them candidates
        # for diagonal congruence -- gauge copies rather than different
        # geometries. The measured signs are opposite.
        claims["site_triangle_sign"] = LINK_TRIANGLE_SIGN
    elif mutation == "break_robustness":
        # THE SECOND AND THIRD POINTS DENIED: the robustness fixtures asserted
        # to lose the full-span rank, which the measured inertias forbid. It is
        # the mutation that stops the two extra points from being quietly
        # dropped -- while the banner still refuses to call three points a
        # window.
        claims["robustness_inertia"] = (
            (CORE_INERTIA, THREE_SLICE_INERTIA, (8, 1, 7)),
            (CORE_INERTIA, THREE_SLICE_INERTIA, FULL_SLICE_INERTIA))
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
    # C -- the link-route structure
    raising_nonzeros: int
    restricted_nonzeros: int
    glue_nonzeros: int
    glue_p_odd_residual: int
    hodge_p_even_residual: int
    transpose_covariance_residual: int
    b185_first_minor: object
    band_census: dict
    reflection_split_residual: int
    seam_symmetry_residual: int
    seam_rank: int
    seam_support: tuple
    seam_block_at_zero: tuple
    seam_sector_blocks: tuple
    seam_block_dets: tuple
    seam_inertia: tuple
    sector_seam_inertia: tuple
    # D -- the mechanism and the three repair failures
    sign_operator_involutive: tuple
    sign_operator_symmetric: tuple
    seam_eigenvalues: tuple
    raw_gram_signs: tuple
    raw_gram_inertia: tuple
    sandwich_signs: tuple
    sandwich_inertia: tuple
    sign_insertion_asymmetry: tuple
    sign_commutator_rank: tuple
    modulus_symmetric: tuple
    modulus_inertia: tuple
    modulus_minors: tuple
    seam_square_identity: bool
    modulus_closed_form: bool
    modulus_determinant: object
    full_modulus_inertia: tuple
    reflected_cross_is_minus_seam: bool
    polar_covariance_residual: dict
    polar_determinants: dict
    polar_gram_symmetry: dict
    polar_gram_signs: dict
    polar_gram_inertia: dict
    # E -- the site construction
    site_hodge_residual: int
    flipped_hodge_residual: int
    site_restricted_nonzeros: int
    site_glue_nonzeros: int
    site_glue_p_odd_residual: int
    site_difference_count: int
    site_difference_cells: tuple
    site_interior_agreement: bool
    site_covariance_residual: int
    site_asymmetry: int
    site_bond_agreement: int
    site_interior_agreement_count: int
    a_convention_extra: int
    a_convention_cells: tuple
    a_convention_glue_unchanged: bool
    link_under_site_permutation: int
    # F -- the empty cross and the positivity
    site_cross_nonzeros: int
    site_cross_piece_nonzeros: tuple
    site_cross_half_nonzeros: tuple
    site_gram_symmetry: tuple
    core_minors: tuple
    core_signs: tuple
    three_slice_signs: tuple
    full_slice_signs: tuple
    congruence_inertia: tuple
    schur_residuals: tuple
    schur_block_sizes: tuple
    schur_core_matches: tuple
    nsimplify_calls: int
    # G -- the four checker legs, ALL MEASURED
    transfer_l_asymmetry: int
    transfer_witness: object
    transfer_self_adjoint_defect: int
    transfer_factors: tuple
    transfer_factor_degrees: tuple
    transfer_census: tuple
    robustness: tuple
    site_triangle_sign: int
    link_triangle_sign: int
    exactness_holds: bool


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    kernel = staggered_kernel()
    raising = raising_part(kernel)
    link_reflection = reflection_permutation(link_theta)
    site_reflection = reflection_permutation(site_theta)

    # --- THE LINK ROUTE, which is Block 185's object ------------------------
    link_restricted = link_restricted_raising(raising)
    link_glue = sp.expand(
        link_restricted - link_reflection * link_restricted * link_reflection)
    link_hodge = link_image_hodge(FIXTURE_SHEAR)
    link_action = completion(link_hodge, link_glue, FIXTURE_MASS)
    link_inverse = link_action.inv()

    positive = slice_indices(POSITIVE_TIMES)
    partners = reflected_indices(POSITIVE_TIMES, link_theta)
    # THE CONTROL: Block 185's first leading minor is K[0,0] on their span.
    b185_first = link_inverse[site_index(0, 0), site_index(link_theta(0), 0)]

    # THE REFLECTION SPLIT, exactly: the theta-transported negative-half block
    # against the transposed positive-half block.
    split_residual = residual_count(
        link_action[list(partners), list(partners)]
        - link_action[list(positive), list(positive)].T)

    seam = sp.expand(link_action[list(positive), list(partners)])
    seam_support = tuple(sorted({
        (row // SPACE_EXTENT, column // SPACE_EXTENT)
        for row in range(HALF_SIZE) for column in range(HALF_SIZE)
        if seam[row, column] != 0}))

    # --- THE x-MOMENTUM SECTORS ---------------------------------------------
    sector_seam_blocks = []
    sector_seam_dets = []
    sector_objects: dict = {}
    sector_p = sector_reflection(link_theta)
    for momentum in ALL_SECTORS:
        embedding = sector_map(momentum)
        action_p = sp.expand(embedding.H * link_action * embedding)
        seam_p = action_p[SECTOR_ROWS, SECTOR_COLUMNS]
        near = sp.Matrix([[seam_p[0, 0], seam_p[0, 1]],
                          [seam_p[1, 0], seam_p[1, 1]]])
        far = sp.Matrix([[seam_p[3, 3], seam_p[3, 2]],
                         [seam_p[2, 3], seam_p[2, 2]]])
        sector_seam_blocks.append((momentum, near, far))
        sector_seam_dets.extend([reduce_exact(near.det()),
                                 reduce_exact(far.det())])
        sector_objects[momentum] = (action_p, seam_p)

    zero_seam = sector_objects[0][1]
    seam_block_at_zero = ((zero_seam[0, 0], zero_seam[0, 1]),
                          (zero_seam[1, 0], zero_seam[1, 1]))

    # --- D: THE MECHANISM AND THE THREE REPAIR FAMILIES ---------------------
    # SCOPED TO THE TWO REAL SECTORS, which are Block 107's both eigenlines.
    # THE FULL 16-DIMENSIONAL CLOSED FORMS, before any sector is taken.
    # C^2 = a C + b^2 I with a = tr(block) and b the thickness coupling, so
    # S = (2C - a I)/delta and |C| = S C = (a C + 2 b^2 I)/delta are POLYNOMIAL
    # in C and no square root is ever taken numerically.
    thickness = SEAM_THICKNESS_COUPLING
    seam_square_identity = residual_count(
        seam * seam - SEAM_TRACE * seam - thickness ** 2 * sp.eye(HALF_SIZE)) == 0
    full_sign = sign_operator(seam)
    full_modulus = reduce_matrix(full_sign * seam)
    modulus_closed_form = residual_count(
        full_modulus
        - (SEAM_TRACE * seam + 2 * thickness ** 2 * sp.eye(HALF_SIZE))
        / SIGN_DISCRIMINANT) == 0
    modulus_determinant = reduce_exact(
        full_modulus.det(method="berkowitz"))
    full_modulus_inertia = inertia(full_modulus)
    # C' = Q[theta b, a], the OTHER cross block, measured against C: it is
    # EXACTLY -C, which is what makes the third polar convention below the one
    # that respects the action's own antisymmetry.
    reflected_cross = sp.expand(link_action[list(partners), list(positive)])
    reflected_cross_is_minus_seam = residual_count(reflected_cross + seam) == 0

    involutive, symmetric_sign, eigen = [], [], []
    raw_signs, raw_inertia = [], []
    sandwich_signs, sandwich_inertia = [], []
    insertion_asymmetry, commutator_rank = [], []
    modulus_symmetric, modulus_inertia, modulus_minors = [], [], []
    polar_covariance: dict = {name: [] for name in POLAR_CONVENTIONS}
    polar_dets: dict = {name: [] for name in POLAR_CONVENTIONS}
    polar_symmetry: dict = {name: [] for name in POLAR_CONVENTIONS}
    polar_signs: dict = {name: [] for name in POLAR_CONVENTIONS}
    polar_inertia: dict = {name: [] for name in POLAR_CONVENTIONS}
    for momentum in REAL_SECTORS:
        action_p, seam_p = sector_objects[momentum]
        sign_p = sign_operator(seam_p)
        involutive.append(
            reduce_matrix(sign_p * sign_p) == sp.eye(len(SECTOR_ROWS)))
        symmetric_sign.append(residual_count(sign_p - sign_p.T) == 0)
        eigen.append(tuple(sorted(
            (reduce_exact((SEAM_DIRECT_BOND - SIGN_DISCRIMINANT) / 2),
             reduce_exact((SEAM_DIRECT_BOND + SIGN_DISCRIMINANT) / 2)),
            key=lambda value: sp.sign(value))))
        raw_gram = reduce_matrix(
            action_p.inv()[SECTOR_ROWS, SECTOR_COLUMNS].T)
        raw_signs.append(minor_signs(leading_minors(raw_gram)))
        raw_inertia.append(inertia(raw_gram))
        # (R1) the S-sandwich: a congruence, so Sylvester already decides it.
        sandwich = reduce_matrix(sign_p * raw_gram * sign_p)
        sandwich_signs.append(minor_signs(leading_minors(sandwich)))
        sandwich_inertia.append(inertia(sandwich))
        # (R2) the sign insertion: not even symmetric.
        # (R2) the sign insertion: not even symmetric.  S K - (S K)^T is S K -
        # K S exactly, since S and K are both symmetric here, so the asymmetry
        # count and the commutator RANK are two readings of one defect.
        inserted = reduce_matrix(sign_p * raw_gram)
        insertion_asymmetry.append(residual_count(inserted - inserted.T))
        commutator_rank.append(
            reduce_matrix(sign_p * raw_gram - raw_gram * sign_p).rank())
        # (R3) the seam-modulus surgery, IN ALL THREE WAYS IT CAN BE WRITTEN
        # INTO THE ACTION, because "the sign-convention branch" was named as an
        # attack surface and one convention is not an answer to it.
        modulus = reduce_matrix(sign_p * seam_p)
        modulus_symmetric.append(residual_count(modulus - modulus.T) == 0)
        modulus_inertia.append(inertia(modulus))
        modulus_minors.append(leading_minors(modulus))
        for name in POLAR_CONVENTIONS:
            polar_action = sp.Matrix(action_p)
            for row, source in enumerate(SECTOR_ROWS):
                for column, target in enumerate(SECTOR_COLUMNS):
                    polar_action[source, target] = modulus[row, column]
                    if name == "symmetric":
                        polar_action[target, source] = modulus[row, column]
                    elif name == "sign-preserving":
                        polar_action[target, source] = -modulus[row, column]
            polar_covariance[name].append(residual_count(
                sector_p * polar_action * sector_p - polar_action.T))
            polar_dets[name].append(
                reduce_exact(polar_action.det(method="berkowitz")))
            polar_gram = reduce_matrix(
                polar_action.inv()[SECTOR_ROWS, SECTOR_COLUMNS].T)
            polar_symmetry[name].append(
                residual_count(polar_gram - polar_gram.T) == 0)
            polar_signs[name].append(minor_signs(leading_minors(polar_gram)))
            polar_inertia[name].append(inertia(polar_gram))

    # --- E: THE SITE-ADAPTED RE-DERIVATION ----------------------------------
    site_hodge = site_image_hodge(FIXTURE_SHEAR)
    flipped_hodge = site_image_hodge(FIXTURE_SHEAR, flipped=True)
    site_hodge_residual = residual_count(
        site_reflection * site_hodge * site_reflection - site_hodge)
    flipped_residual = residual_count(
        site_reflection * flipped_hodge * site_reflection - flipped_hodge)
    site_restricted = site_restricted_raising(raising)
    site_glue = sp.expand(
        site_restricted - site_reflection * site_restricted * site_reflection)
    site_glue_odd = residual_count(
        site_reflection * site_glue * site_reflection + site_glue)
    difference = sp.expand(site_glue - raising)
    difference_cells = tuple(sorted({
        (row // SPACE_EXTENT, column // SPACE_EXTENT)
        for row in range(COVER_SIZE) for column in range(COVER_SIZE)
        if difference[row, column] != 0}))
    # THE INTERIOR AGREEMENT: on the physical interior -- both times strictly
    # inside {1,2,3} -- the derived glue IS d_K, entrywise; AND SO IT IS on the
    # two BOND cell pairs {0,1} and {3,4} that carry the fixed slices into the
    # interior, which is the check's B2 precision.
    interior = slice_indices((1, 2, 3))
    site_interior_agreement_count = residual_count(
        difference[list(interior), list(interior)])
    site_bond_agreement = sum(
        residual_count(difference[list(slice_indices((row,))),
                                  list(slice_indices((column,)))])
        for row, column in SITE_BOND_CELLS)
    site_action = completion(site_hodge, site_glue, FIXTURE_MASS)
    site_covariance = residual_count(
        site_reflection * site_action * site_reflection - site_action.T)
    # AND THE PRECISION THE CHECK INSISTED ON: Q_s is NOT an ordinarily
    # symmetric matrix.  The property is REFLECTED-TRANSPOSE covariance
    # Ps Q_s Ps = Q_s^T, and the plain symmetry defect is large and nonzero.
    site_asymmetry = residual_count(site_action - site_action.T)
    link_under_site = residual_count(
        site_reflection * link_action * site_reflection - link_action.T)
    # THE A-CONVENTION FORK, MEASURED TO BE AN EXACT NO-OP.  Putting the
    # fixed-slice spatial edges BACK into A_s adds entries -- and they cancel
    # identically in the oddization, leaving D_s UNCHANGED.  The exclusion is
    # therefore not a freedom that could have changed the answer.
    wide_restricted = sp.zeros(COVER_SIZE, COVER_SIZE)
    for row in range(COVER_SIZE):
        for column in range(COVER_SIZE):
            if raising[row, column] == 0:
                continue
            if (row // SPACE_EXTENT not in CLOSED_HALF
                    or column // SPACE_EXTENT not in CLOSED_HALF):
                continue
            wide_restricted[row, column] = raising[row, column]
    extra = sp.expand(wide_restricted - site_restricted)
    a_convention_cells = tuple(sorted({
        (row // SPACE_EXTENT, column // SPACE_EXTENT)
        for row in range(COVER_SIZE) for column in range(COVER_SIZE)
        if extra[row, column] != 0}))
    wide_glue = sp.expand(
        wide_restricted - site_reflection * wide_restricted * site_reflection)
    a_convention_glue_unchanged = residual_count(wide_glue - site_glue) == 0

    # --- F: THE EMPTY CROSS AND THE POSITIVITY ------------------------------
    strictly_positive = slice_indices(THREE_SLICES)
    site_partners = reflected_indices(THREE_SLICES, site_theta)
    negative_half = slice_indices((5, 6, 7))
    cross_nonzeros = residual_count(
        site_action[list(strictly_positive), list(site_partners)])
    cross_half = (
        residual_count(site_action[list(strictly_positive), list(negative_half)]),
        residual_count(site_action[list(negative_half), list(strictly_positive)]))
    # THE CHECK'S B4 PRECISION: the emptiness is exact SUPPORT emptiness and NOT
    # a cancellation between the three terms of the completion.  Each of
    # m H, H D_s and -D_s^T H is measured SEPARATELY on the cross-half block.
    cross_pieces = (sp.expand(FIXTURE_MASS * site_hodge),
                    sp.expand(site_hodge * site_glue),
                    sp.expand(-site_glue.T * site_hodge))
    cross_piece_nonzeros = tuple(
        residual_count(piece[list(strictly_positive), list(negative_half)])
        for piece in cross_pieces)
    site_inverse = site_action.inv()
    grams = tuple(paired_gram(site_inverse, slices, site_theta)
                  for slices in (CORE_SLICES, THREE_SLICES, FULL_SLICES))
    gram_symmetry = tuple(residual_count(g - g.T) == 0 for g in grams)
    core_minors = leading_minors(grams[0])
    gram_signs = tuple(minor_signs(leading_minors(g)) for g in grams)
    congruence_inertia = tuple(inertia(g) for g in grams)
    # THE EXACT SCHUR CERTIFICATION, which is what actually certifies the two
    # degenerate spans.  Reordered so the POSITIVE-DEFINITE core {1,2} leads,
    # each larger span's Schur complement is IDENTICALLY ZERO -- 0_4 on
    # {1,2,3} and 0_8 on {0,1,2,3} -- so the span is congruent to the core
    # direct-sum a zero block and the inertia is (8,0,4) and (8,0,8) exactly.
    schur_grams = tuple(paired_gram(site_inverse, order, site_theta)
                        for order in SCHUR_ORDERS)
    schur_core_matches = tuple(
        residual_count(g[:8, :8] - grams[0]) == 0 for g in schur_grams)
    schur_residuals = tuple(
        residual_count(schur_complement(g, 8)) for g in schur_grams)
    schur_block_sizes = tuple(g.rows - 8 for g in schur_grams)

    # --- G: THE FOUR CHECKER LEGS -------------------------------------------
    # (B6) THE NAIVE RECONSTRUCTION TRANSFER, REFUTED.
    core_anchors = slice_indices(CORE_SLICES)
    core_partners = reflected_indices(CORE_SLICES, site_theta)
    shifted = tuple(site_index(t + 1, x)
                    for t in CORE_SLICES for x in range(SPACE_EXTENT))
    core_gram = sp.expand(sp.Matrix(
        8, 8, lambda i, j: site_inverse[core_anchors[j], core_partners[i]]))
    shifted_pairing = sp.expand(sp.Matrix(
        8, 8, lambda i, j: site_inverse[shifted[j], core_partners[i]]))
    transfer = sp.expand(core_gram.inv() * shifted_pairing)
    transfer_l_asymmetry = residual_count(
        shifted_pairing - shifted_pairing.T)
    transfer_witness = reduce_exact(
        shifted_pairing[0, 1] - shifted_pairing[1, 0])
    transfer_self_adjoint_defect = residual_count(
        core_gram * transfer - transfer.T * core_gram)
    factorization = sp.factor_list(
        transfer.charpoly(SPECTRAL_SYMBOL).as_expr())
    measured_factors = tuple(sorted(
        (sp.expand(factor) for factor, multiplicity in factorization[1]
         for _ in range(multiplicity)), key=factor_key))
    transfer_factor_degrees = tuple(
        sp.Poly(factor, SPECTRAL_SYMBOL).degree()
        for factor in measured_factors)
    transfer_census = (
        sum(sp.count_roots(sp.Poly(f, SPECTRAL_SYMBOL), 0, 1)
            for f in measured_factors),
        sum(sp.count_roots(sp.Poly(f, SPECTRAL_SYMBOL), -sp.oo, 0)
            for f in measured_factors),
        8 - sum(sp.count_roots(sp.Poly(f, SPECTRAL_SYMBOL))
                for f in measured_factors))
    # (B7) THE TWO ROBUSTNESS POINTS: same glue, re-dialled Hodge.
    robustness = []
    for mass, shear in ROBUSTNESS_POINTS:
        point_hodge = site_image_hodge(shear)
        point_action = completion(point_hodge, site_glue, mass)
        point_inverse = point_action.inv()
        point_grams = tuple(paired_gram(point_inverse, slices, site_theta)
                            for slices in (CORE_SLICES, THREE_SLICES,
                                           FULL_SLICES))
        robustness.append((
            (mass, shear),
            residual_count(site_reflection * point_action * site_reflection
                           - point_action.T),
            residual_count(
                point_action[list(strictly_positive), list(site_partners)])
            + residual_count(
                point_action[list(strictly_positive), list(negative_half)]),
            tuple(inertia(g) for g in point_grams)))
    # (B8) THE TRIANGLE-SIGN OBSTRUCTION.
    link_core = paired_gram(link_inverse, LINK_CORE_SLICES, link_theta)
    site_triangle = triangle_sign(grams[0])
    link_triangle = triangle_sign(link_core)

    citation_pins = {
        "b107_ladder": B107_LADDER_PIN in landed_text(BLOCK107_NOTE),
        "b107_transfer_route": B107_ROUTE_PIN in landed_text(BLOCK107_NOTE),
        "b107_steelman": B107_STEELMAN_PIN in landed_text(BLOCK107_NOTE),
        "b107_not_a_nogo": B107_NOT_A_NOGO_PIN in landed_text(BLOCK107_NOTE),
        "b185_full_span": B185_SPAN_PIN in landed_text(BLOCK185_NOTE),
        "b187_quotient_downstream":
            B187_QUOTIENT_PIN in landed_text(BLOCK187_NOTE),
    }
    banners = {
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "objects_registered": bool(REGISTERED_OBJECTS or ADOPTED_OBJECTS),
        "constraint_quotient_claimed": CONSTRAINT_QUOTIENT_CLAIMED,
        "generality_claimed": GENERALITY_CLAIMED,
        "transfer_operator_claimed": TRANSFER_OPERATOR_CLAIMED,
    }
    exact_scalars = (
        (b185_first, modulus_determinant, transfer_witness)
        + tuple(sector_seam_dets) + tuple(core_minors)
        + tuple(value for values in polar_dets.values() for value in values)
        + tuple(value for row in modulus_minors for value in row))
    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        raising_nonzeros=nonzero_entries(raising),
        restricted_nonzeros=nonzero_entries(link_restricted),
        glue_nonzeros=nonzero_entries(link_glue),
        glue_p_odd_residual=residual_count(
            link_reflection * link_glue * link_reflection + link_glue),
        hodge_p_even_residual=residual_count(
            link_reflection * link_hodge * link_reflection - link_hodge),
        transpose_covariance_residual=residual_count(
            link_reflection * link_action * link_reflection - link_action.T),
        b185_first_minor=b185_first,
        band_census=band_census(link_action),
        reflection_split_residual=split_residual,
        seam_symmetry_residual=residual_count(seam - seam.T),
        seam_rank=seam.rank(),
        seam_support=seam_support,
        seam_block_at_zero=seam_block_at_zero,
        seam_sector_blocks=tuple(sector_seam_blocks),
        seam_block_dets=tuple(sector_seam_dets),
        seam_inertia=inertia(seam),
        sector_seam_inertia=tuple(
            inertia(sector_objects[p][1]) for p in REAL_SECTORS),
        sign_operator_involutive=tuple(involutive),
        sign_operator_symmetric=tuple(symmetric_sign),
        seam_eigenvalues=tuple(eigen),
        raw_gram_signs=tuple(raw_signs),
        raw_gram_inertia=tuple(raw_inertia),
        sandwich_signs=tuple(sandwich_signs),
        sandwich_inertia=tuple(sandwich_inertia),
        sign_insertion_asymmetry=tuple(insertion_asymmetry),
        sign_commutator_rank=tuple(commutator_rank),
        modulus_symmetric=tuple(modulus_symmetric),
        modulus_inertia=tuple(modulus_inertia),
        modulus_minors=tuple(modulus_minors),
        seam_square_identity=seam_square_identity,
        modulus_closed_form=modulus_closed_form,
        modulus_determinant=modulus_determinant,
        full_modulus_inertia=full_modulus_inertia,
        reflected_cross_is_minus_seam=reflected_cross_is_minus_seam,
        polar_covariance_residual={k: tuple(v)
                                   for k, v in polar_covariance.items()},
        polar_determinants={k: tuple(v) for k, v in polar_dets.items()},
        polar_gram_symmetry={k: tuple(v) for k, v in polar_symmetry.items()},
        polar_gram_signs={k: tuple(v) for k, v in polar_signs.items()},
        polar_gram_inertia={k: tuple(v) for k, v in polar_inertia.items()},
        site_hodge_residual=site_hodge_residual,
        flipped_hodge_residual=flipped_residual,
        site_restricted_nonzeros=nonzero_entries(site_restricted),
        site_glue_nonzeros=nonzero_entries(site_glue),
        site_glue_p_odd_residual=site_glue_odd,
        site_difference_count=nonzero_entries(difference),
        site_difference_cells=difference_cells,
        site_interior_agreement=site_interior_agreement_count == 0,
        site_interior_agreement_count=site_interior_agreement_count,
        site_bond_agreement=site_bond_agreement,
        site_covariance_residual=site_covariance,
        site_asymmetry=site_asymmetry,
        a_convention_extra=nonzero_entries(extra),
        a_convention_cells=a_convention_cells,
        a_convention_glue_unchanged=a_convention_glue_unchanged,
        link_under_site_permutation=link_under_site,
        site_cross_nonzeros=cross_nonzeros,
        site_cross_piece_nonzeros=cross_piece_nonzeros,
        site_cross_half_nonzeros=cross_half,
        site_gram_symmetry=gram_symmetry,
        core_minors=core_minors,
        core_signs=gram_signs[0],
        three_slice_signs=gram_signs[1],
        full_slice_signs=gram_signs[2],
        congruence_inertia=congruence_inertia,
        schur_residuals=schur_residuals,
        schur_block_sizes=schur_block_sizes,
        schur_core_matches=schur_core_matches,
        nsimplify_calls=nsimplify_occurrences(),
        transfer_l_asymmetry=transfer_l_asymmetry,
        transfer_witness=transfer_witness,
        transfer_self_adjoint_defect=transfer_self_adjoint_defect,
        transfer_factors=measured_factors,
        transfer_factor_degrees=transfer_factor_degrees,
        transfer_census=transfer_census,
        robustness=tuple(robustness),
        site_triangle_sign=site_triangle,
        link_triangle_sign=link_triangle,
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
        "registry blobs in the worktree. THE TWO BLOCK 187 ARTIFACTS ARE "
        "CONTENT-BOUND -- its note and its runner, the pair that identifies "
        "the commit this block's branch is cut from -- at PARENT_COMMIT, in "
        "the worktree and against their pinned blobs, and PARENT_COMMIT IS "
        "REAL and PARENT_REF resolves to it, so nothing needs sed at landing. "
        "THE STALE PIN IS THE BLOCK 186 TIP, a REAL ancestor of HEAD that "
        "PREDATES Block 187 and therefore carries NEITHER Block 187 artifact, "
        "which is exactly what makes the stale_parent_authority mutation bite: "
        "under it the gate looks for the artifact blobs at a commit where they "
        "do not exist. AUDIT_INPUT_PATHS IS LITERAL and every one of its EIGHT "
        "entries is required readable in the worktree EXCEPT this block's own "
        "note, which lands later and belongs to gate H -- and the eight "
        "include BOTH BLOCK 185 ARTIFACTS, whose object is this block's LINK "
        "route, and the BLOCK 107 note, whose section-10 ladder this block "
        "executes and whose steelman it realizes. AND THE MACHINERY IMPORT IS "
        "GATED: the LANDED Block 128 runner must have imported, because the "
        "two helper objects this runner does not build itself -- "
        "cover_embedding() and the Block 105 shear_hodge() -- are read from "
        "it, and NOTHING from any scratchpad is imported or read",
        bool(
            AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
            and len(AUDIT_INPUT_PATHS) == 8
            and len(set(AUDIT_INPUT_PATHS)) == 8
            and BLOCK187_NOTE in AUDIT_INPUT_PATHS
            and BLOCK187_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK185_NOTE in AUDIT_INPUT_PATHS
            and BLOCK185_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK107_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_RUNNER in AUDIT_INPUT_PATHS
            and CAMPAIGN_NOTE in AUDIT_INPUT_PATHS
            and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
            and authority.inputs_missing == ()
            and PARENT_ARTIFACTS == (BLOCK187_NOTE, BLOCK187_RUNNER)
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
        "B-THE-IMPOSED-OBJECT-BANNER-and-the-NOT-CLAIMED-keys",
        f"THE BANNER COMES BEFORE ANY NUMERAL AND IT IS MEASURED RATHER THAN "
        f"ASSERTED. {ban['imposed_objects']} objects are IMPOSED by this block "
        f"-- the LINK route which is Block 185's seam-glued object rebuilt "
        f"from its displayed equations, the THETA-PAIRED SEAM OPERATOR with "
        f"its momentum decomposition and its exact surd sign operator and "
        f"polar action, the SITE-ADAPTED RE-DERIVATION which is this block's "
        f"own geometry and not a variant of theirs, the THREE FIXTURES, the "
        f"NAIVE RECONSTRUCTION TRANSFER built only in order to be REFUTED, and "
        f"the two LANDED Block 128 helpers that are the only imports -- and "
        f"{ban['registered_objects']} are REGISTERED and "
        f"{ban['adopted_objects']} are ADOPTED. AND THE BANNER'S SECOND HALF "
        f"IS WHAT IS NOT CLAIMED, gated as declared constants, because THIS "
        f"BLOCK ENDS ON A POSITIVE RESULT AND A POSITIVE RESULT IS THE EASIER "
        f"THING TO OVERREAD. NO GENERALITY: THREE fixtures on ONE carrier -- "
        f"({FIXTURE_MASS}, {FIXTURE_SHEAR}) and the two robustness points -- "
        f"with NO bracket, NO ray, NO edge and NO interior, so the site route "
        f"has no window at all where Block 187 gave the link route one. NO "
        f"TRANSFER OPERATOR: the obvious candidate is BUILT HERE AND REFUTED "
        f"in family G, and the proper OS construction is a NAMED OPEN LEG, so "
        f"the physical-Hilbert-space language is a READING. NO GRAVITY "
        f"CONSTRAINT QUOTIENT: Block 107's step 3, whose PREREQUISITE this "
        f"block supplies and which it does not execute. Asserting any of the "
        f"three, or asserting that the imposed objects are registered, fails "
        f"HERE and nowhere else",
        bool(
            ban["imposed_objects"] == 6
            and ban["registered_objects"] == 0
            and ban["adopted_objects"] == 0
            and ban["objects_registered"] == claims["objects_registered"]
            and ban["constraint_quotient_claimed"]
            == claims["constraint_quotient_claimed"]
            and ban["generality_claimed"] == claims["generality_claimed"]
            and ban["transfer_operator_claimed"]
            == claims["transfer_operator_claimed"]))

    # --- C: the link-route structure ----------------------------------------
    pins = facts.citation_pins
    checks.check(
        "C-THE-CONTROL-THE-REFLECTION-SPLIT-and-THE-SEAM-OF-THICKNESS-TWO",
        f"THE CONTROL COMES FIRST AND IT IS SOMEBODY ELSE'S NUMBER. The LINK "
        f"route rebuilt here from Block 185's displayed equations keeps "
        f"{facts.restricted_nonzeros} of d_K's {facts.raising_nonzeros} "
        f"entries in the restricted set A, derives the glue D = A - P A P at "
        f"EXACTLY {facts.glue_nonzeros} nonzero entries, P-odd at "
        f"{facts.glue_p_odd_residual}, with the A02-image geometry P-even at "
        f"{facts.hodge_p_even_residual} and P Q P = Q^T at "
        f"{facts.transpose_covariance_residual} -- and reproduces their landed "
        f"first leading minor {facts.b185_first_minor} DIGIT-FOR-DIGIT. IF "
        f"THAT NUMBER MOVED, THE WALL BELOW WOULD BE A WALL OF SOME OTHER "
        f"OBJECT. THEN THE SPLIT: the theta-transported negative-half block "
        f"equals the positive-half block TRANSPOSED at "
        f"{facts.reflection_split_residual} residual, so THE WHOLE FULL-HALF "
        f"OS QUESTION REDUCES to the theta-paired cross operator "
        f"C[a,b] = Q[a, theta b], which is symmetric at "
        f"{facts.seam_symmetry_residual} and has FULL RANK {facts.seam_rank}. "
        f"AND THE SEAM IS TWO SLICES THICK: C's support is exactly the six "
        f"slice blocks {facts.seam_support} -- the near-seam trio and the "
        f"far-seam trio -- and the action's band census {facts.band_census} is "
        f"the measured reason, the +/-2 overlap bands CROSSING THE CUT. THE "
        f"CLASSIC SINGLE-BOND OSTERWALDER-SEILER ARGUMENT DOES NOT APPLY. "
        f"EVERY CITATION IS SOMEBODY ELSE'S LANDED SENTENCE, read from the "
        f"PRIMARY BODY: Block 107's ladder, their transfer-route row, their "
        f"steelman and their scope firewall, Block 185's full-span item and "
        f"Block 187's downstream-quotient sentence, at {pins}",
        bool(
            facts.glue_nonzeros == claims["glue_nonzeros"]
            and facts.glue_p_odd_residual == claims["glue_p_odd_residual"]
            and facts.hodge_p_even_residual == claims["hodge_p_even_residual"]
            and facts.transpose_covariance_residual
            == claims["transpose_covariance_residual"]
            and facts.b185_first_minor == claims["b185_first_minor"]
            and facts.band_census == claims["band_census"]
            and facts.reflection_split_residual
            == claims["reflection_split_residual"]
            and facts.seam_symmetry_residual == claims["seam_symmetry_residual"]
            and facts.seam_rank == claims["seam_rank"]
            and facts.seam_support == claims["seam_support"]
            and all(pins.values()) == claims["citation_pins"]))
    checks.check(
        "C-THE-SEAM-OPERATOR-IN-CLOSED-FORM-and-ITS-FORCED-INDEFINITENESS",
        f"THE MECHANISM, IN ONE LINE, AND IT IS THE BLOCK'S CORE MATHEMATICS. "
        f"The glued action commutes with the spatial shift, so C decomposes by "
        f"x-momentum at omega_p = i^p, and in EVERY one of the four sectors "
        f"EACH SEAM CONTRIBUTES A 2x2 BLOCK of the form "
        f"[[{SEAM_DIRECT_BOND}, ({SEAM_THICKNESS_COUPLING}) omega_p], "
        f"[conj, 0]]: at p = 0 the measured entries are "
        f"{facts.seam_block_at_zero}. THE DIRECT SEAM BOND IS A PURE SCALAR "
        f"WITH NO SHEAR CONTENT -- the forced-flat straddling anchors showing "
        f"through -- AND THE THICKNESS COUPLING SITS OFF-DIAGONAL AGAINST A "
        f"ZERO DIAGONAL, the slice-1 self-coupling vanishing identically. "
        f"THEREFORE det = -|{SEAM_THICKNESS_COUPLING}|^2 < 0 whenever the "
        f"thickness coupling is nonzero: all {len(facts.seam_block_dets)} "
        f"measured seam-block determinants are {facts.seam_block_dets[0]} and "
        f"EACH BLOCK IS FORCED INDEFINITE BY THE SHEAR-CARRYING THICKNESS. Per "
        f"real sector C's inertia is {facts.sector_seam_inertia} and in total "
        f"{facts.seam_inertia}, BY EXACT CONGRUENCE and not by a minor "
        f"sequence -- EXACTLY MATCHING the raw full-half Gram's own "
        f"{facts.raw_gram_inertia[0]} per sector. THE FULL-HALF FAILURE IS THE "
        f"SEAM OPERATOR'S SHEAR THICKNESS, localized and explained. At zero "
        f"thickness the seam would be sign-uniform and the raw pairing would "
        f"work, which is why asserting a zero coupling, or a positive "
        f"determinant, fails HERE and nowhere else",
        bool(
            facts.seam_block_at_zero == claims["seam_block_at_zero"]
            and facts.seam_block_dets == claims["seam_block_dets"]
            and all(value < 0 for value in claims["seam_block_dets"])
            and facts.seam_inertia == claims["seam_inertia"]
            and facts.sector_seam_inertia == claims["sector_seam_inertia"]
            and len(facts.seam_sector_blocks) == len(ALL_SECTORS)))

    # --- D: the mechanism's three repair failures ---------------------------
    checks.check(
        "D-THE-CONGRUENCE-LEMMA-NO-DRESSING-CAN-MOVE-THE-INERTIA",
        f"THE FIRST REPAIR FAMILY IS BARRED BY A THEOREM AND NOT BY A SAMPLE, "
        f"AND THAT IS BLOCK 107'S OWN STEELMAN CONFIRMED AT THEOREM LEVEL. The "
        f"reflected Gram is REAL, so EVERY diagonal or local left dressing "
        f"acts on it as a CONGRUENCE K -> S K S, and SYLVESTER'S LAW OF "
        f"INERTIA forbids a congruence from moving the signature. The "
        f"full-span extension therefore REQUIRES THE TRANSPORTER PROPER -- a "
        f"re-pairing -- and never a dressing. The S-sandwich is measured "
        f"anyway on both real sectors {REAL_SECTORS}: the raw sector Gram "
        f"carries signs {facts.raw_gram_signs} at inertia "
        f"{facts.raw_gram_inertia}, and S K S carries {facts.sandwich_signs} "
        f"at {facts.sandwich_inertia} -- THE SAME SIGNATURE, as the lemma "
        f"requires. AND THE TWO NUMBERS IN THAT TABLE ARE DIFFERENT KINDS OF "
        f"OBJECT, WHICH IS THE ADVERSARIAL CHECK'S CORRECTION #16 AND IS GATED "
        f"HERE AS TWO SEPARATE CLAIMS: (+,+,-,+) IS A LEADING-MINOR SIGN "
        f"SEQUENCE AND IS NOT AN INERTIA. A minor sequence with a zero in it "
        f"decides nothing at all, and even without zeros it is a derived "
        f"reading; the INERTIA is what Sylvester's law is about, it is "
        f"{facts.raw_gram_inertia} here by EXACT CONGRUENCE, and both are "
        f"measured rather than one being inferred from the other. The sign "
        f"operator itself is exact: S^2 = I {facts.sign_operator_involutive}, "
        f"symmetric {facts.sign_operator_symmetric}, built from the closed form "
        f"S = (2C - tr(C_block) I)/delta with delta = sqrt(365426)/576, resting "
        f"on the exact matrix identity C^2 = tr*C + b^2*I "
        f"({facts.seam_square_identity}) whose eigenvalue pair is the surd "
        f"{facts.seam_eigenvalues[0]}",
        bool(
            facts.raw_gram_signs == claims["raw_gram_signs"]
            and facts.sandwich_signs == claims["sandwich_signs"]
            and facts.sandwich_inertia == claims["sandwich_inertia"]
            and facts.raw_gram_inertia == claims["sandwich_inertia"]
            and facts.seam_square_identity == claims["seam_square_identity"]
            and all(facts.sign_operator_involutive)
            and all(facts.sign_operator_symmetric)))
    checks.check(
        "D-THE-SIGN-INSERTION-IS-NOT-A-PAIRING",
        f"THE SECOND REPAIR FAMILY DIES ON A DEFINITION. Inserting the sign "
        f"operator on the GRAM side -- theta' = theta compose sign(C), i.e. "
        f"K -> S K -- produces an object that is NOT SYMMETRIC: S K carries "
        f"{facts.sign_insertion_asymmetry} asymmetric entries on the real "
        f"sectors {REAL_SECTORS}, and since S and K are both symmetric there, "
        f"that defect IS the commutator S K - K S, of RANK "
        f"{facts.sign_commutator_rank} -- FULL RANK on a 4-dimensional sector, "
        f"so the failure is not a corner case but the generic situation. A "
        f"two-history pairing that is not symmetric is not a pairing at all, "
        f"so there is nothing here whose positivity could even be asked about. "
        f"AND THE FAILURE IS NOT S'S FAULT: S is symmetric and involutive on "
        f"exactly these sectors ({facts.sign_operator_symmetric}, "
        f"{facts.sign_operator_involutive}), so what fails is the INSERTION, "
        f"not the operator",
        bool(
            facts.sign_insertion_asymmetry
            == claims["sign_insertion_asymmetry"]
            and facts.sign_commutator_rank == claims["sign_commutator_rank"]
            and all(value > 0 for value in facts.sign_insertion_asymmetry)
            and all(facts.sign_operator_symmetric)))
    checks.check(
        "D-THE-SEAM-MODULUS-SURGERY-and-NO-SIGN-BRANCH-IS-PSD",
        f"THE THIRD REPAIR FAMILY IS THE ONE THAT SHOULD HAVE WORKED, AND IT "
        f"IS MEASURED TO FAIL IN EVERY WAY IT CAN BE WRITTEN. The action-side "
        f"seam-modulus surgery replaces the seam operator by its polar modulus "
        f"|C| = S C in the ACTION itself, and the modulus is EXACT ALGEBRA "
        f"rather than a numerical square root: from C^2 = tr*C + b^2*I one gets "
        f"|C| = (tr*C + 2 b^2 I)/delta in closed form "
        f"({facts.modulus_closed_form}), with det|C| = "
        f"{facts.modulus_determinant} = (65/1152)^16 exactly and the full "
        f"16-dimensional inertia {facts.full_modulus_inertia}. EVERY "
        f"PRECONDITION IS VERIFIED AND NOT ASSUMED: |C| symmetric "
        f"{facts.modulus_symmetric}, POSITIVE DEFINITE per sector at "
        f"{facts.modulus_inertia} with exact surd leading minors "
        f"{facts.modulus_minors[0]}. AND THE SURGERY IS RUN IN ALL "
        f"{len(POLAR_CONVENTIONS)} WAYS THE ACTION ADMITS, because 'the "
        f"sign-convention branch' is an attack surface and one convention is "
        f"not an answer to it: the other cross block Q[theta b, a] is measured "
        f"to be EXACTLY -C ({facts.reflected_cross_is_minus_seam}), so the "
        f"one-sided, the symmetric and the antisymmetry-respecting "
        f"sign-preserving writings are all legitimate. ALL THREE ARE "
        f"REFLECTION-COVARIANT at residual {facts.polar_covariance_residual} "
        f"with NONZERO determinants -- the symmetric branch's is the exact "
        f"rational {facts.polar_determinants['symmetric'][0]} and the "
        f"sign-preserving branch's is "
        f"{facts.polar_determinants['sign-preserving'][0]} -- and their polar "
        f"Grams are all symmetric {facts.polar_gram_symmetry}. AND NOT ONE OF "
        f"THEM IS PSD: one-sided {facts.polar_gram_signs['one-sided']} at "
        f"inertia {facts.polar_gram_inertia['one-sided']}, symmetric "
        f"{facts.polar_gram_signs['symmetric']} at "
        f"{facts.polar_gram_inertia['symmetric']}, and the sign-preserving "
        f"branch {facts.polar_gram_signs['sign-preserving']} at "
        f"{facts.polar_gram_inertia['sign-preserving']} -- NEGATIVE DEFINITE, "
        f"which is a global sign flip and not a repair. THE THICK SEAM DEFEATS "
        f"BLOCK-LEVEL PSD-NESS: a positive-definite seam block does NOT buy a "
        f"positive-definite Gram, because the depth-2 coupling is not the whole "
        f"of what the reflection sees. THE CLASSIC OSTERWALDER-SEILER ARGUMENT "
        f"DOES NOT EXTEND THROUGH DEPTH-2 COUPLINGS BY SEAM SURGERY ALONE, and "
        f"THE WALL IS PER-PAIRING AND PER-FRAME AND IS NOT A CURVED-OS NO-GO. "
        f"Asserting that the polar Gram is positive definite, or moving the "
        f"modulus determinant, fails HERE and nowhere else",
        bool(
            facts.modulus_inertia == claims["modulus_inertia"]
            and facts.modulus_minors == claims["modulus_minors"]
            and all(facts.modulus_symmetric)
            and facts.modulus_closed_form == claims["modulus_closed_form"]
            and facts.modulus_determinant == claims["modulus_determinant"]
            and facts.full_modulus_inertia == claims["full_modulus_inertia"]
            and facts.reflected_cross_is_minus_seam
            and facts.polar_covariance_residual
            == claims["polar_covariance_residual"]
            and all(value != 0 for values in facts.polar_determinants.values()
                    for value in values)
            and facts.polar_determinants["symmetric"]
            == claims["symmetric_polar_determinant"]
            and facts.polar_determinants["sign-preserving"]
            == claims["sign_preserving_polar_determinant"]
            and all(all(v) for v in facts.polar_gram_symmetry.values())
            and facts.polar_gram_signs == claims["polar_gram_signs"]
            and facts.polar_gram_inertia == claims["polar_gram_inertia"]
            and not any(
                inertia_value == (4, 0, 0)
                for values in facts.polar_gram_inertia.values()
                for inertia_value in values)))

    # --- E: the site-adapted re-derivation ----------------------------------
    checks.check(
        "E-THE-SITE-HODGE-IS-INVARIANT-UNDER-THE-BARE-PERMUTATION",
        f"THE SITE ROUTE'S FOUNDATION, AND ITS CONTRAST WITH THE LINK ROUTE IS "
        f"MEASURED RATHER THAN ASSERTED. The site reflection theta_s(t) = -t "
        f"fixes slices {FIXED_SLICES} and pairs every cell under "
        f"thA_s(t) = -1-t, so there are NO FIXED ANCHORS and none has to be "
        f"forced flat. With the physical anchors {POSITIVE_TIMES} at the "
        f"UNIFORM step c = {FIXTURE_SHEAR} and the image anchors as the "
        f"UNFLIPPED P_4-images of their thA_s partners, "
        f"Ps H Ps - H has {facts.site_hodge_residual} nonzero entries: "
        f"INVARIANT UNDER THE BARE PERMUTATION, with NO xpar dressing and NO "
        f"shear flip. AND THE FLIPPED VARIANT -- the same geometry carrying "
        f"the step history's sign on the image shear, which is what the LINK "
        f"route's odd history would suggest -- FAILS AT EXACTLY "
        f"{facts.flipped_hodge_residual} ENTRIES. THAT CONTRAST IS ITSELF THE "
        f"FINDING: the unflipped image is a DERIVED FEATURE of the site "
        f"geometry and not a convention, and the two routes want opposite "
        f"things at the same place. Asserting either that the site Hodge fails "
        f"or that the flipped variant works fails HERE and nowhere else",
        bool(
            facts.site_hodge_residual == claims["site_hodge_residual"]
            and facts.flipped_hodge_residual
            == claims["flipped_hodge_residual"]))
    checks.check(
        "E-THE-SITE-GLUE-THE-FIXED-SLICE-EXCLUSION-AS-AN-EXACT-NO-OP-and-THE-240",
        f"THE GLUE, WITH ITS ONE APPARENT FREEDOM MEASURED AWAY. A_s is the "
        f"d_K entries with both times in the CLOSED half {CLOSED_HALF} "
        f"EXCLUDING the spatial edges INSIDE a fixed slice. THE EXCLUSION "
        f"LOOKS LIKE A CONVENTION AND IS MEASURED TO BE AN EXACT NO-OP, which "
        f"is the adversarial check's B9: putting those entries BACK adds "
        f"{facts.a_convention_extra} entries to the raising set, supported on "
        f"exactly the cells {facts.a_convention_cells}, and they CANCEL "
        f"IDENTICALLY in the oddization -- D_s = A_s - Ps A_s Ps is UNCHANGED "
        f"({facts.a_convention_glue_unchanged}). Such an edge is Ps-invariant, "
        f"so it can only contribute a Ps-EVEN piece to a construction whose "
        f"whole point is Ps-oddness, and the arithmetic confirms the design "
        f"argument exactly. THE FORK IS THEREFORE NOT A FORK. A_s keeps "
        f"{facts.site_restricted_nonzeros} entries, D_s carries "
        f"{facts.site_glue_nonzeros} and is Ps-ODD at "
        f"{facts.site_glue_p_odd_residual}; D_s differs from d_K at EXACTLY "
        f"{facts.site_difference_count} entries on the six time-cells "
        f"{facts.site_difference_cells}, and agrees with d_K EXACTLY on the "
        f"physical interior ({facts.site_interior_agreement_count} residual) "
        f"AND on the four bond cells {SITE_BOND_CELLS} that carry the fixed "
        f"slices into the interior ({facts.site_bond_agreement} residual). "
        f"Then Ps Q_s Ps = Q_s^T at {facts.site_covariance_residual} WITH THE "
        f"BARE SITE PERMUTATION -- AND THE CHECK'S PRECISION IS GATED WITH IT: "
        f"Q_s IS NOT AN ORDINARILY SYMMETRIC MATRIX. Its plain symmetry defect "
        f"is {facts.site_asymmetry} nonzero entries. The property that holds "
        f"is REFLECTED-TRANSPOSE COVARIANCE and nothing weaker should be read "
        f"from it. AND THE TWO ROUTES ARE NOT VARIANTS OF EACH OTHER, WHICH IS "
        f"WHY THIS BLOCK BUILDS A NEW GEOMETRY INSTEAD OF RELABELLING THE OLD "
        f"ONE: the SITE permutation applied to the LINK action fails "
        f"covariance at EXACTLY {facts.link_under_site_permutation} entries. "
        f"Asserting that it does not, or re-opening the A-convention fork, "
        f"fails HERE and nowhere else",
        bool(
            facts.site_glue_p_odd_residual
            == claims["site_glue_p_odd_residual"]
            and facts.site_glue_nonzeros == claims["site_glue_nonzeros"]
            and facts.site_difference_count == claims["site_difference_count"]
            and facts.site_difference_cells == claims["site_difference_cells"]
            and facts.site_interior_agreement_count
            == claims["site_interior_agreement_count"]
            and facts.site_bond_agreement == claims["site_bond_agreement"]
            and facts.site_covariance_residual
            == claims["site_covariance_residual"]
            and facts.site_asymmetry == claims["site_asymmetry"]
            and facts.site_asymmetry > 0
            and facts.a_convention_extra == claims["a_convention_extra"]
            and facts.a_convention_cells == claims["a_convention_cells"]
            and facts.a_convention_glue_unchanged
            == claims["a_convention_glue_unchanged"]
            and facts.link_under_site_permutation
            == claims["link_under_site_permutation"]))

    # --- F: the empty cross and the positivity ------------------------------
    checks.check(
        "F-THE-CROSS-OPERATOR-IS-EMPTY-BY-SUPPORT-AND-NOT-BY-CANCELLATION",
        f"AND THEN THE OBSTRUCTION IS SIMPLY NOT THERE. The theta_s-paired "
        f"cross operator over the strictly-positive slices {THREE_SLICES} x Z4 "
        f"-- the exact analogue of the link route's thick 16x16 seam operator "
        f"-- has {facts.site_cross_nonzeros} nonzero entries: IDENTICALLY "
        f"ZERO. And it is not an artefact of the pairing: the whole Q_s block "
        f"between {THREE_SLICES} and (5, 6, 7) is "
        f"{facts.site_cross_half_nonzeros} in BOTH directions. AND THE CHECK'S "
        f"B4 PRECISION IS GATED WITH IT, because 'zero' can mean two very "
        f"different things: THIS IS EXACT SUPPORT EMPTINESS AND NOT A "
        f"CANCELLATION. Each of the three terms of the completion is measured "
        f"SEPARATELY on that block -- m*H, H*D_s and -D_s^T*H at "
        f"{facts.site_cross_piece_nonzeros} nonzero entries respectively -- so "
        f"nothing is cancelling against anything and no fixture-dependent "
        f"coincidence is doing the work. NO DIRECT COUPLING CROSSES THE SITE "
        f"CUT: everything routes through the shared fixed slices, and the "
        f"thick-seam obstruction that defeated three repair families on the "
        f"link route VANISHES BY CONSTRUCTION rather than being repaired. "
        f"Asserting a nonzero coupling across the cut fails HERE and nowhere "
        f"else",
        bool(
            facts.site_cross_nonzeros == claims["site_cross_nonzeros"]
            and facts.site_cross_piece_nonzeros
            == claims["site_cross_piece_nonzeros"]
            and len(facts.site_cross_piece_nonzeros) == CROSS_PIECE_COUNT
            and facts.site_cross_half_nonzeros
            == claims["site_cross_half_nonzeros"]))
    checks.check(
        "F-THE-GRAM-IS-PSD-ON-THE-FULL-SPAN-CERTIFIED-BY-EXACT-SCHUR",
        f"THE REFLECTED GRAM ON THE SITE-ADAPTED ACTION, AT EVERY SPAN, AND "
        f"CERTIFIED BY THE INSTRUMENT THAT ACTUALLY CERTIFIES IT. All three "
        f"spans are symmetric ({facts.site_gram_symmetry}). On the two-slice "
        f"core {CORE_SLICES} the leading minor signs are {facts.core_signs} -- "
        f"ALL EIGHT STRICTLY POSITIVE, a POSITIVE DEFINITE physical core, with "
        f"the first two exact values {facts.core_minors[0]} and "
        f"{facts.core_minors[1]}. On {THREE_SLICES} they are "
        f"{facts.three_slice_signs} and on the FULL positive half "
        f"{FULL_SLICES} they are {facts.full_slice_signs}: eight positive then "
        f"zeros. AND A SIGN VECTOR WITH ZEROS IN IT CERTIFIES NOTHING BY "
        f"ITSELF -- leading principal minors are NECESSARY AND NOT SUFFICIENT "
        f"for PSD-ness, and eight positives followed by eight zeros is "
        f"consistent with a negative direction no LEADING minor ever sees. THE "
        f"ADVERSARIAL CHECK'S B5 SUPPLIES THE CERTIFICATE PROPER AND IT IS "
        f"GATED HERE: reordered so the positive-definite core leads, each "
        f"larger span has block form with an IDENTICALLY ZERO SCHUR COMPLEMENT "
        f"-- 0_{facts.schur_block_sizes[0]} on {SCHUR_ORDERS[0]} and "
        f"0_{facts.schur_block_sizes[1]} on {SCHUR_ORDERS[1]}, at residuals "
        f"{facts.schur_residuals}, with the leading block verified to BE the "
        f"core {facts.schur_core_matches} -- so each span is CONGRUENT to the "
        f"core direct-sum a zero block and the inertia follows exactly. THE "
        f"TRUE INERTIAS ARE {facts.congruence_inertia}, measured independently "
        f"by an EXACT CONGRUENCE chain as well: POSITIVE SEMIDEFINITE OF RANK "
        f"8 ON EVERY SPAN, with no negative direction anywhere. AND THE RANK-8 "
        f"READING IS STILL A READING: that the kernel is the OS "
        f"reconstruction's quotient rather than a defect is an INTERPRETATION, "
        f"and family G measures what happened when the obvious operator was "
        f"built for it. EVERY MEASURED SCALAR IS EXACT -- rationals and exact "
        f"quadratic surds, NOT ONE A FLOAT ({facts.exactness_holds}) -- and "
        f"THE BLOCK 186 HAZARD IS HONOURED BY ABSENCE AND MEASURED RATHER THAN "
        f"PROMISED: the tolerance-carrying nsimplify call, which maps a small "
        f"nonzero rational to EXACTLY ZERO and could manufacture any of the "
        f"zeros above, is called {facts.nsimplify_calls} times in this file, "
        f"counted in its own source",
        bool(
            all(facts.site_gram_symmetry)
            and facts.core_signs == claims["core_signs"]
            and facts.core_minors[0] == claims["core_minor_1"]
            and facts.core_minors[1] == claims["core_minor_2"]
            and facts.three_slice_signs == claims["three_slice_signs"]
            and facts.full_slice_signs == claims["full_slice_signs"]
            and facts.congruence_inertia == claims["congruence_inertia"]
            and facts.schur_residuals == claims["schur_residuals"]
            and facts.schur_block_sizes == claims["schur_block_sizes"]
            and all(facts.schur_core_matches)
            and facts.nsimplify_calls == claims["nsimplify_calls"]
            and facts.exactness_holds))

    # --- G: THE FOUR CHECKER LEGS, ALL MEASURED -----------------------------
    checks.check(
        "G-THE-NAIVE-RECONSTRUCTION-TRANSFER-IS-REFUTED",
        f"THE LEG THAT WOULD HAVE TURNED THE RANK-8 READING INTO A STATEMENT, "
        f"AND IT IS A NEGATIVE RESULT. The obvious candidate for the "
        f"reconstruction transfer is T = K_c^-1 L, with K_c the "
        f"positive-definite two-slice core and L the SAME pairing with the "
        f"column anchors advanced one slice. IT IS NOT THE OS TRANSFER, on "
        f"three counts, each exact. FIRST, L IS NOT SYMMETRIC: "
        f"{facts.transfer_l_asymmetry} asymmetric entries, with the exact "
        f"witness L_01 - L_10 = {facts.transfer_witness}. SECOND, T IS NOT "
        f"K_c-SELF-ADJOINT: K_c T - T^T K_c has "
        f"{facts.transfer_self_adjoint_defect} nonzero entries, and an OS "
        f"transfer must be self-adjoint in the reconstruction inner product or "
        f"it is not a transfer at all. THIRD, THE SPECTRUM IS NOTHING LIKE A "
        f"POSITIVE TRANSFER'S: the exact characteristic polynomial factors "
        f"over the rationals into degrees {facts.transfer_factor_degrees}, and "
        f"the EXACT STURM census of those factors is "
        f"{facts.transfer_census[0]} roots in (0,1), "
        f"{facts.transfer_census[1]} NEGATIVE real and "
        f"{facts.transfer_census[2]} NONREAL. NO TRANSFER-OPERATOR CLAIM "
        f"SURVIVES THIS BLOCK. The proper OS transfer -- through the genuine "
        f"reconstruction quotient with the correct pairing -- is a NAMED OPEN "
        f"LEG, and until it is built the physical-Hilbert-space language stays "
        f"a READING. Asserting that the naive candidate is self-adjoint fails "
        f"HERE and nowhere else",
        bool(
            facts.transfer_l_asymmetry == claims["transfer_l_asymmetry"]
            and facts.transfer_witness == claims["transfer_witness"]
            and (facts.transfer_self_adjoint_defect == 0)
            == claims["transfer_self_adjoint"]
            and facts.transfer_factors == claims["transfer_factors"]
            and facts.transfer_factor_degrees
            == claims["transfer_factor_degrees"]
            and facts.transfer_census == claims["transfer_census"]
            and sum(facts.transfer_census) == 8))
    checks.check(
        "G-TWO-MORE-FIXTURES-and-TWO-MORE-POINTS-ARE-NOT-A-WINDOW",
        f"THE POSITIVITY IS NOT A ONE-POINT ACCIDENT, AND IT IS ALSO NOT A "
        f"REGION. At {tuple((str(m), str(c)) for m, c, in ROBUSTNESS_POINTS)} "
        f"-- one step along the mass axis and one along the shear axis from "
        f"the fixture -- the SAME site glue against a re-dialled Hodge gives: "
        f"{tuple((str(point), covariance, cross, inertias) for point, covariance, cross, inertias in facts.robustness)} "
        f"-- that is, reflected-transpose covariance at zero residual, an "
        f"EMPTY cross at zero, and the SAME three inertias "
        f"{facts.congruence_inertia} at both points. The empty cross is "
        f"structural rather than fixture-tuned, which is what one would expect "
        f"from a SUPPORT statement, and the rank-8 PSD structure survives both "
        f"steps. AND THREE POINTS ARE STILL NOT A WINDOW: no bracket, no ray, "
        f"no edge and no interior is established for the site route, and "
        f"generality stays NOT CLAIMED in family B. Block 187 had to build two "
        f"sampled rays, two exact bisections and an algebraic edge before the "
        f"LINK route's window could be called a region; none of that exists "
        f"here. Asserting that a robustness point loses the full-span rank "
        f"fails HERE and nowhere else",
        bool(
            len(facts.robustness) == len(ROBUSTNESS_POINTS)
            and all(covariance == 0 and cross == 0
                    for _, covariance, cross, _ in facts.robustness)
            and tuple(inertias for _, _, _, inertias in facts.robustness)
            == claims["robustness_inertia"]
            and all(point == declared for (point, _, _, _), declared
                    in zip(facts.robustness, ROBUSTNESS_POINTS))))
    checks.check(
        "G-THE-SITE-AND-LINK-CORES-ARE-DIFFERENT-OBJECTS-NOT-GAUGE-COPIES",
        f"AND THE ONE COMPARISON THAT WOULD HAVE MADE THIS BLOCK A "
        f"RE-DESCRIPTION RATHER THAN A RESULT, ANSWERED BY AN INVARIANT. Both "
        f"the SITE core on slices {CORE_SLICES} and Block 185's LANDED LINK "
        f"core on {LINK_CORE_SLICES} are positive definite on the same carrier "
        f"at the same fixture, so the obvious worry is that they are the same "
        f"object in different clothes. THEY ARE NOT, AND THE OBSTRUCTION IS "
        f"ELEGANT: under a DIAGONAL congruence K -> E K E the triangle product "
        f"K_01 K_14 K_40 is multiplied by (E_0 E_1 E_4)^2, a POSITIVE SQUARE, "
        f"so its SIGN is an INVARIANT of the diagonal-congruence class. The "
        f"measured signs are {facts.site_triangle_sign} for the SITE core and "
        f"{facts.link_triangle_sign} for the LINK core. THEY ARE OPPOSITE, SO "
        f"THE TWO POSITIVE GRAMS ARE NEITHER EQUAL NOR DIAGONALLY CONGRUENT: "
        f"they are DISTINCT GEOMETRIC OBJECTS and not gauge copies. Which "
        f"means the site route's success is not the link route's success "
        f"relabelled -- AND ALSO that nothing here says the two constructions "
        f"describe the same physics; that is a further open leg and it is "
        f"named as one. Asserting the two triangle signs equal fails HERE and "
        f"nowhere else",
        bool(
            facts.site_triangle_sign == claims["site_triangle_sign"]
            and facts.link_triangle_sign == claims["link_triangle_sign"]
            and facts.site_triangle_sign != facts.link_triangle_sign
            and abs(facts.site_triangle_sign) == 1
            and abs(facts.link_triangle_sign) == 1))

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
        f"is twenty members mapped one-per-family across "
        f"{MUTATED_FAMILIES} -- EVERY family carrying at least one, family G "
        f"included, because the adversarial check landed and turned its four "
        f"placeholders into measurements",
        bool(
            facts.note_at_final_path
            and NOTE_PATH.name == FINAL_NOTE_NAME
            and set(facts.scope) == set(SCOPE_KEYS)
            and required == SCOPE_KEYS
            and all(facts.scope[key] for key in required)
            and facts.scope["n5_verbatim"]
            and len(MUTATIONS) == 20
            and len(set(MUTATIONS)) == 20
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


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    authority = facts.authority
    ban = facts.banners
    print("MEASURED, before any gate is read:")
    print(f"  AUTHORITY: origin/main resolves to {facts.main_head}; the "
          f"five-pin block is fixed {authority.fixed_authority}. "
          f"PARENT_COMMIT {PARENT_COMMIT} is REAL and PARENT_REF resolves to "
          f"it {authority.parent_ref_and_ancestry}, and BOTH Block 187 "
          f"artifacts are content-bound there and in the worktree "
          f"{authority.parent_artifact_blobs}. THE AUDIT INPUTS: "
          f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} "
          f"readable in the worktree (this block's own note excluded, since it "
          f"lands later and is gate H's), missing {authority.inputs_missing}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {authority.stale_is_real_ancestor} and carries NEITHER Block "
          f"187 artifact {authority.stale_carries_neither_artifact} -- it is "
          f"the Block 186 tip, which PREDATES both artifacts, and that absence "
          f"is exactly what makes the stale_parent_authority mutation bite")
    print(f"  THE MACHINERY: BOTH CONSTRUCTIONS ARE BUILT DIRECTLY HERE -- the "
          f"staggered kernel, the grade projectors, d_K, BOTH reflections, the "
          f"offset permutation, BOTH restricted raising sets, BOTH derived "
          f"glues and BOTH glued actions. The LANDED Block 128 runner is "
          f"imported {authority.machinery_import_landed} for EXACTLY TWO "
          f"objects, cover_embedding() and the Block 105 shear_hodge(); the "
          f"carrier is {TIME_EXTENT}x{SPACE_EXTENT} at dimension {COVER_SIZE} "
          f"and the ONLY fixture is m = {FIXTURE_MASS}, c = {FIXTURE_SHEAR}, "
          f"v = 1. NOTHING from any scratchpad is imported or read")
    print(f"  THE BANNER: {ban['imposed_objects']} imposed objects, "
          f"{ban['registered_objects']} registered and "
          f"{ban['adopted_objects']} adopted; MEASURED "
          f"constraint-quotient-claimed {ban['constraint_quotient_claimed']}, "
          f"generality-claimed {ban['generality_claimed']} and "
          f"transfer-operator-claimed {ban['transfer_operator_claimed']}. The "
          f"imposed objects are {IMPOSED_OBJECTS}")
    print(f"  THE CITATION PINS: {facts.citation_pins} -- Block 107's "
          f"section-10 ladder and their N6 transfer-route row and N7 steelman "
          f"and their scope firewall, all from THEIR primary body; Block 185's "
          f"full-positive-time-span item; and Block 187's "
          f"constraint-quotient-downstream sentence")
    print(f"  THE LINK CONTROL: d_K carries {facts.raising_nonzeros} entries, "
          f"the restricted set A carries {facts.restricted_nonzeros} and "
          f"D = A - P A P carries EXACTLY {facts.glue_nonzeros}, P-odd at "
          f"{facts.glue_p_odd_residual}, with H P-even at "
          f"{facts.hodge_p_even_residual} and P Q P = Q^T at "
          f"{facts.transpose_covariance_residual}. Block 185's first leading "
          f"minor is {facts.b185_first_minor} -- THEIR LANDED NUMBER, "
          f"DIGIT-FOR-DIGIT")
    print(f"  THE SPLIT AND THE SEAM: the theta-transported negative half "
          f"equals the transposed positive half at "
          f"{facts.reflection_split_residual}; C is symmetric at "
          f"{facts.seam_symmetry_residual} with rank {facts.seam_rank}; its "
          f"support is {facts.seam_support}; the action's band census is "
          f"{facts.band_census} and the +/-2 bands CROSS THE CUT")
    print("  THE SEAM IN CLOSED FORM, PER SECTOR (all four measured, both "
          "seams each):")
    for momentum, near, far in facts.seam_sector_blocks:
        print(f"    p={momentum}: near {near.tolist()}  far {far.tolist()}")
    print(f"    determinants {facts.seam_block_dets}; C's inertia "
          f"{facts.seam_inertia} in total and {facts.sector_seam_inertia} on "
          f"the real sectors {REAL_SECTORS}, BY EXACT CONGRUENCE")
    print(f"  THE REPAIR FAMILIES, ON THE REAL SECTORS {REAL_SECTORS} ONLY -- "
          f"Block 107's both eigenlines. AT p = 1 AND p = 3 the sector "
          f"operators are HERMITIAN rather than symmetric and the "
          f"real-symmetric sign-operator identities do not apply unchanged; "
          f"the seam blocks and determinants above ARE measured at all four, "
          f"and the repairs are gated at the two real ones. AND THE TWO "
          f"READINGS BELOW ARE DIFFERENT OBJECTS -- a LEADING-MINOR SIGN "
          f"SEQUENCE IS NOT AN INERTIA, which is the check's correction #16 -- "
          f"so both are measured. RAW Gram signs {facts.raw_gram_signs} at "
          f"inertia {facts.raw_gram_inertia}; (R1) S K S "
          f"{facts.sandwich_signs} at {facts.sandwich_inertia}; (R2) S K "
          f"asymmetric at {facts.sign_insertion_asymmetry} entries, "
          f"commutator rank {facts.sign_commutator_rank}; (R3) C^2 identity "
          f"{facts.seam_square_identity}, |C| closed form "
          f"{facts.modulus_closed_form}, det|C| = "
          f"{facts.modulus_determinant}, full inertia "
          f"{facts.full_modulus_inertia}, per-sector {facts.modulus_inertia}, "
          f"and Q[theta b, a] == -C {facts.reflected_cross_is_minus_seam}")
    for name in POLAR_CONVENTIONS:
        print(f"    POLAR [{name}]: covariance "
              f"{facts.polar_covariance_residual[name]}, determinants "
              f"{tuple(str(v) for v in facts.polar_determinants[name])}, Gram "
              f"signs {facts.polar_gram_signs[name]} at inertia "
              f"{facts.polar_gram_inertia[name]}")
    print("    NOT ONE POLAR BRANCH IS PSD")
    print(f"  THE SITE CONSTRUCTION: Ps H Ps = H at "
          f"{facts.site_hodge_residual} with the BARE permutation, while the "
          f"FLIPPED variant fails at {facts.flipped_hodge_residual}; A_s keeps "
          f"{facts.site_restricted_nonzeros} entries and D_s carries "
          f"{facts.site_glue_nonzeros}, Ps-odd at "
          f"{facts.site_glue_p_odd_residual}; D_s differs from d_K at "
          f"{facts.site_difference_count} entries on "
          f"{facts.site_difference_cells}, interior agreement "
          f"{facts.site_interior_agreement}; Ps Q_s Ps = Q_s^T at "
          f"{facts.site_covariance_residual}; and the SITE permutation on the "
          f"LINK action fails at {facts.link_under_site_permutation}")
    print(f"  THE EMPTY CROSS: {facts.site_cross_nonzeros} nonzero entries in "
          f"the theta_s-paired cross over {THREE_SLICES}, and "
          f"{facts.site_cross_half_nonzeros} in the full cross-half block in "
          f"both directions -- and the three pieces m*H, H*D_s and -D_s^T*H "
          f"separately at {facts.site_cross_piece_nonzeros}, so it is SUPPORT "
          f"emptiness and NOT cancellation. NOTHING CROSSES THE SITE CUT")
    print(f"  THE GRAMS: {CORE_SLICES} signs {facts.core_signs}; "
          f"{THREE_SLICES} signs {facts.three_slice_signs}; {FULL_SLICES} "
          f"signs {facts.full_slice_signs}; all symmetric "
          f"{facts.site_gram_symmetry}. THE CERTIFICATE PROPER: the Schur "
          f"complements of the core inside {SCHUR_ORDERS[0]} and "
          f"{SCHUR_ORDERS[1]} are IDENTICALLY ZERO at residuals "
          f"{facts.schur_residuals} on blocks of size "
          f"{facts.schur_block_sizes}, leading blocks verified to be the core "
          f"{facts.schur_core_matches}, and the TRUE INERTIAS are "
          f"{facts.congruence_inertia} -- PSD of rank 8 on every span")
    print(f"  THE TRANSFER LEG, REFUTED: L asymmetric at "
          f"{facts.transfer_l_asymmetry} entries with witness "
          f"L_01 - L_10 = {facts.transfer_witness}; T is K_c-self-adjoint "
          f"{facts.transfer_self_adjoint_defect == 0} at defect "
          f"{facts.transfer_self_adjoint_defect}; the charpoly factors over "
          f"the rationals into degrees {facts.transfer_factor_degrees} with "
          f"exact Sturm census (in (0,1), negative, nonreal) = "
          f"{facts.transfer_census}. THE NAIVE CANDIDATE IS NOT THE OS "
          f"TRANSFER, and the proper construction is a NAMED OPEN LEG")
    for factor in facts.transfer_factors:
        print(f"    factor: {factor}")
    print(f"  THE ROBUSTNESS POINTS: "
          f"{tuple((str(point), covariance, cross, inertias) for point, covariance, cross, inertias in facts.robustness)} "
          f"-- covariance and cross at zero and the SAME three inertias at "
          f"both. THREE POINTS ARE NOT A WINDOW and generality stays NOT "
          f"CLAIMED")
    print(f"  THE SITE-VERSUS-LINK OBSTRUCTION: the diagonal-congruence "
          f"invariant sign(K_01 K_14 K_40) is {facts.site_triangle_sign} for "
          f"the SITE core and {facts.link_triangle_sign} for Block 185's "
          f"LANDED LINK core. OPPOSITE, so the two positive Grams are NOT "
          f"diagonally congruent and NOT gauge copies -- they are distinct "
          f"geometric objects")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False the note has NOT landed at docs/ yet, there is no draft "
          f"fallback anywhere in this runner, gate H is EXPECTED to fail and "
          f"the gate-H mutation is UNTESTABLE until the note lands. Scope keys "
          f"satisfied: {sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  EXACTNESS: every measured scalar above is an exact sympy "
          f"Rational, Integer or quadratic surd and NOT ONE IS A FLOAT "
          f"({facts.exactness_holds}); no tolerance enters any check; "
          f"signatures are decided by exact leading principal minors and by an "
          f"EXACT CONGRUENCE chain, never by an eigenvalue estimate; and the "
          f"tolerance-carrying nsimplify call appears {facts.nsimplify_calls} "
          f"times in this file, counted in its own source -- THE BLOCK 186 "
          f"HAZARD, HONOURED BY ABSENCE. ELAPSED "
          f"{elapsed_ns // 1_000_000} ms")
    print(f"  THE CORPUS RELATION: Blocks 104, 105, 106, 107, 128 and 181-187 "
          f"STAND EXACTLY AS LANDED and no landed note is edited. BLOCK 185 IS "
          f"NEITHER CORRECTED NOR CONTRADICTED: their fixture number is "
          f"reproduced above digit-for-digit and their windowed two-slice "
          f"positivity stands; the site route is a DIFFERENT construction "
          f"reaching a DIFFERENT terminal. BLOCK 107'S SECTION-10 LADDER: "
          f"steps 1 and 2 are EXECUTED here -- the transfer/polar structure of "
          f"the seam kernel is derived in closed form and the two-history Gram "
          f"is retested under it on both eigenlines -- and STEP 3, the gravity "
          f"constraint quotient, is NOT executed and now has its prerequisite. "
          f"THE ADVERSARIAL CHECK LANDED AND ITS VERDICTS ARE FOLDED "
          f"THROUGHOUT: {CHECK_VERDICT}. It CONFIRMED the reflection split, "
          f"the seam operator and its congruence inertia, the 240, the 64, the "
          f"Ps-odd glue and its 24-entry census, the covariance, the empty "
          f"cross and the core minors; it CORRECTED the block on three counts "
          f"that are now gates rather than prose -- the minor-signs-versus-"
          f"inertia language (correction #16), the PSD certification which now "
          f"runs through an EXACT SCHUR complement rather than through leading "
          f"minors, and the support-versus-cancellation reading of the empty "
          f"cross; and it REFUTED the naive reconstruction transfer outright, "
          f"which is why NO transfer-operator claim survives this block")
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
