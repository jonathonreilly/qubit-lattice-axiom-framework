#!/usr/bin/env python3
"""BLOCK 184 -- THE TEMPORAL-LINK EXTRACTION.

THE RESULT, AND ITS EXACT SCOPE.  On the certified Block 105 curved carrier as
landed by Block 128 and re-used by Blocks 181, 182 and 183 -- the 8x4 cover of
dimension 32, the parameterized cover Hodge H[g] over the LANDED Block 105
overlap field, the chart differential d_00 and the completion convention
Q(H,d) = m*H + i*(H d + d^H H) at SYMBOLIC POSITIVE MASS -- and AT THE MINIMAL
REFLECTION-CLOSED FRAME H_min = (H + U_x^T H U_x)/2, THE dt=+-1 TEMPORAL LINK IS
EXTRACTED, IT IS INVERTIBLE AT EVERY BOND, IT SATISFIES AN EXACT PARITY THEOREM
AGAINST THE DUAL FRAME, ITS SYMBOLIC FORM SPLITS EVEN AND ODD BONDS, AND THE
SLICE DETERMINANTS ARE STRICTLY POSITIVE FOR EVERY REAL MASS:

  0. THE FRAME IS ONE ADMITTED MEMBER AND MINIMALITY IS THE ONLY CRITERION.
     Block 183 measured the complete equal-weight reflection-closed family:
     SIXTEEN sets, FIFTEEN of them proper, ALL positive definite, with {I, U_x}
     the MINIMAL member -- and it REFUTED uniqueness rather than leaving it
     unclaimed.  This block works at that minimal member BECAUSE IT IS MINIMAL,
     and it re-measures the two facts that make it usable: the frame closes
     under the derived reflection at ZERO residual, and it is POSITIVE DEFINITE
     by 32 exact leading principal minors.  NO UNIQUENESS IS CLAIMED HERE
     EITHER, and the banner key is gated as a declared constant.

  1. THE BAND STRUCTURE, AND THE LINK IS A PAIR (C).  The band census of
     Q_min = Q(H_min, d_00) by time separation dt = (row//4 - col//4) mod 8 is
     EXACTLY {0: 80, +1: 72, +2: 16, -2: 16, -1: 72} -- 256 nonzero entries in
     five bands and nothing outside them, identical to the equal-weight point's
     census.  THE LINK IS THE dt=+-1 PAIR.  And the pair is IRREDUCIBLY A PAIR:
     B_-1 is NOT the adjoint of B_+1 (40 entries), NOT minus its adjoint (32),
     and NOT its transpose (40).  THREE EXPLICIT NON-IDENTITIES; the backward
     link is not recoverable from the forward link by any of them.

  2. THE TRANSPORTER IS INVERTIBLE AT EVERY BOND (D).  Slicing the link into
     its eight 4x4 per-bond blocks L_t = Q_min[slice t+1, slice t]: ALL EIGHT
     HAVE RANK EXACTLY 4 and EMPTY KERNELS, with nonzero counts alternating
     10 (even t) and 8 (odd t).  THE BLOCK 128 KERNEL IS NOT IN THE LINK: the
     transporter is invertible bond by bond, and whatever degeneracy the
     carrier has lives in the slice Schur complement instead.

  3. THE PARITY THEOREM, EXACT, AND ITS CONVENTION IS LOAD-BEARING (E).
     R B_+1 R^-1 = the dt=-1 band of Q_dual EXACTLY, where Q_dual is the
     DUAL-FRAME completion m*H_min_dual[theta g] + i(H_min_dual d_ref +
     d_ref^H H_min_dual) built with the SEAM IDENTITY'S OWN differential
     d_ref = R d_00 R^-1.  THE FORWARD LINK MAPS EXACTLY ONTO THE DUAL
     BACKWARD LINK.  AND THE CONVENTION IS MEASURED, NOT ASSERTED: against the
     WRONG dual, the one built with d_00 in place of d_ref, the same residual
     is EXACTLY 16 nonzero entries.  Two further controls fail in the same run:
     against the dt=+1 band of the dual (144) and against the dt=-1 band of the
     ORIGINAL frame (96).

  4. THE SYMBOLIC ADM SPLIT, AS THE ADVERSARIAL CHECK CORRECTED IT (F).  At a
     per-slice symbolic field (q_t, v_t) constant in x, and with the checker's
     shear variable a_t = q_t v_t / (q_t^2 - 1), THE ODD BONDS CARRY PURE
     SHEAR: L_1 has EXACTLY 8 nonzero entries and the whole table is exhibited
     -- -3 a_1/20 at (0,0) and (2,2), +3 a_1/20 at (0,2) and (2,0), and
     m a_1/4 at (0,1), (1,2), (2,3) and (3,0) -- so L_1 VANISHES IDENTICALLY
     AT q_1 = 0.  THE EVEN BONDS CARRY THE SAME 8-ENTRY SHEAR PATTERN PLUS
     FOUR MORE: L_0 has 10 nonzeros splitting EXACTLY 8 odd and 4 even under
     q -> -q, THE MASS APPEARS ONLY IN THE ODD PART, and THE EVEN PART IS FOUR
     DIAGONAL ENTRIES WITH SIGNS (-,+,-,+) AND COMMON MAGNITUDE
     E = (1/v_0 + v_1 - v_0/(q_0^2 - 1) - v_1/(q_1^2 - 1))/5.  THE EVEN PART
     IS GENUINELY SHEAR-DEPENDENT: dE/dq_0 = 2 q_0 v_0/(5(q_0^2 - 1)^2) and
     dE/dq_1 = 2 q_1 v_1/(5(q_1^2 - 1)^2) are NONZERO and ODD, which is
     exactly why E is EVEN and the parity split stands.  Under the Pythagorean
     witness constraint q_t^2 + v_t^2 = 1 the magnitude reduces EXACTLY to
     E = (v_1 + 1/v_1 + 2/v_0)/5.  THE ADM READING -- even bonds = lapse plus
     shear, odd bonds = pure shift/shear transport -- IS A READING, MARKED AS
     ONE, AND GATED AS NOT CLAIMED.

  5. THE POLE LOCUS, THE QUOTIENT, AND THE TWIST CERTIFICATE (G).  The eight
     intra-slice blocks D_t = Q_min[slice t, slice t] have determinants that
     are EVEN QUARTICS IN m with ALL THREE COEFFICIENTS STRICTLY POSITIVE;
     slices t and t+4 agree exactly, so there are FOUR distinct determinants;
     and therefore det D_t > 0 FOR EVERY REAL m INCLUDING m = 0 -- gated at the
     coefficient level and again at m = 0.  THE SLICE SCHUR FACTORIZATION IS
     GLOBALLY REGULAR ON THE PHYSICAL MASS AXIS at this frame's decomposition;
     the poles sit at m^2 < 0, off the physical line.  AND THE BLOCK DESCENDS:
     on the 16-dimensional antiperiodic quotient the band census is EXACTLY
     {0: 40, +1: 36, +2: 16, -1: 36} and all four quotient bonds have rank 4
     with the same 10/8 alternation.  THE TWIST CERTIFICATE IS A CERTIFICATE
     AND NO LONGER AN EXPECTATION: the quotient seam bond is MINUS the cover
     bond 3 -> 4 at the SAME field pair, exactly -- the sum is the zero matrix,
     the difference is not, and the entrywise ratio is -1 at all EIGHT common
     nonzero positions.  It was measured by the adversarial checker and it is
     gated here.

WHAT IS NOT CLAIMED, STATED ONCE: NO OS OR REFLECTION-POSITIVITY THEOREM -- the
link is extracted and no pairing is shown positive anywhere; NO TWO-HISTORY GRAM
-- it is the next leg and its inputs (an invertible link and a regular Schur
complement) are what this block supplies; NO GRAVITY RESULT; NO ADM
IDENTIFICATION AS A THEOREM -- the lapse/shift split is a READING of the
measured even/odd structure and the key is gated as a declared constant; and NO
UNIQUENESS FOR THE FRAME -- {I, U_x} is ONE ADMITTED MEMBER of Block 183's
sixteen-member closed family, chosen for MINIMALITY.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 183 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the nine audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: six imposed objects,
     ZERO registered and ZERO adopted, with the OS/reflection-positivity
     theorem, the two-history Gram, any gravity result, the ADM identification
     and any frame uniqueness all declared NOT CLAIMED as measured constants.
  C  THE BAND STRUCTURE: the four citation pins read from the two primary
     bodies, the frame controls next (the landed-field control, the
     reflection's orthogonality, the frame's exact closure and its 32 positive
     leading minors), then the exact five-band census -- for this frame, for
     the dual frame and for the re-measured Block 181 equal-weight point 96
     entries away -- and the three non-identities that make the link a pair.
  D  THE INVERTIBLE TRANSPORTER: eight per-bond blocks, all rank 4, all with
     empty kernels, nonzero counts 10/8 alternating.
  E  THE PARITY THEOREM: exact at zero residual against the dual frame built
     with d_ref, with the WRONG-DUAL contrast at 16 and two further controls at
     144 and 96.
  F  THE SYMBOLIC ADM SPLIT: the odd bond's whole 8-entry table against its
     exhibited closed forms and its vanishing at zero shear, the even bond's
     8/4 split with the mass confined to the odd part, the even part's four
     diagonal positions and (-,+,-,+) signs against the exact magnitude E, its
     two nonzero shear derivatives, and the Pythagorean reduction.
  G  THE POLE LOCUS, THE QUOTIENT AND THE TWIST: four distinct even-quartic
     determinants with every coefficient strictly positive and every m = 0
     value positive, the quotient band census, the four full-rank quotient
     bonds, and the checker-measured seam negation at eight positions.
  H  the note at its final path and the N5 fence, byte-identical.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: sixteen declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_os_positivity, claim_adm_reading,
       claim_frame_unique
    C  break_band_table
    D  break_link_rank
    E  break_parity_theorem, break_wrong_dual_contrast
    F  break_shear_vanishing, break_even_part
    G  break_det_positivity, break_quotient_bands, break_twist_negation
    H  drop_n5_fence
  TWO OF THE SIXTEEN GUARD WHAT THE ADVERSARIAL CHECK SUPPLIED: break_even_part
  restores the solve's refuted "no q dependence" clause for the even part, and
  break_twist_negation denies the seam negation the checker measured.  Both
  must fail.
  BEFORE LANDING GATE H ALREADY FAILS AT BASELINE, on note-at-final-path alone,
  so drop_n5_fence cannot flip it and THE SWEEP IS RUN AT LANDING, once the note
  sits at docs/ and the baseline is 8 of 8 by family.

RUNNING
  python3 scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation break_parity_theorem

NOTES FOR THE LANDING AGENT
  1. NOTHING from any scratchpad is imported OR READ.  Every object below is
     rebuilt from the LANDED Block 128 runner
     scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py
     and from the Block 105 module it re-exports as `block105`, and the note is
     read at its FINAL PATH ONLY -- there is no draft fallback anywhere in this
     runner, so gate H FAILS until the note lands at docs/.
  2. EVERY CHECK IS EXACT.  sympy Rational, Integer and Symbol arithmetic only;
     no float enters any measured object and no tolerance is used anywhere.
  3. The N5 fence appears byte-identically in the note; gate H checks it as a
     raw substring.
  4. PARENT_COMMIT is the Block 183 tip and PARENT_REF resolves to it; nothing
     needs sed, and CURRENT_MAIN was carried forward from the Block 183 runner
     and re-resolved at draft time.
  5. The stale pin is the Block 182 tip, a real ancestor of HEAD that predates
     Block 183 and carries NEITHER Block 183 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  6. THE TWIST CERTIFICATE WAS QUEUED AND IS NOW FOLDED.  The solve left the
     quotient-seam-versus-cover-bond comparison as a queued certificate; the
     adversarial checker measured it -- exact negation, entrywise ratio -1 at
     all eight common nonzero positions -- and this runner GATES the checker's
     measurement rather than a placeholder.  The gate asserts BOTH halves: the
     sum is the zero matrix AND the difference is not.
  7. ONE SOLVE-SIDE CLAUSE WAS REFUTED BY THE ADVERSARIAL CHECK BEFORE LANDING
     AND THE CHECKER'S VERSION IS WHAT THIS RUNNER GATES.  The solve recorded
     the even bond's even part as having "no q dependence"; the even part is
     four diagonal entries of common magnitude E which is EVEN in the shears
     but GENUINELY q^2-dependent, with both shear derivatives nonzero.  The
     parity split -- 8 odd, 4 even, mass only in the odd part -- STANDS
     UNCHANGED; only the compressed clause was wrong.
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

# THE MACHINERY IMPORT, LANDED.  Block 128 is the CARRIER parent: it carries the
# certified Block 105 curved carrier, the 8x4 cover, the cover embedding whose
# corner order IS the form basis, the chart differentials, the completion
# convention and the antiperiodic quotient, and it re-exports Block 105 as
# `block105`, from which the shear Hodge block and the overlap field are read.
# NOTHING from any scratchpad is imported or read anywhere in this runner.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 183 is the commit this block's branch
# is cut from, and its note and its runner are the pair that distinguishes the
# parent pin from the stale pin: both exist at PARENT_COMMIT and NEITHER exists
# at STALE_PARENT_COMMIT.
BLOCK183_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK183_RUNNER = (
    "scripts/admissibility_dirac_kahler_derived_reflection_seam_dual_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK183_NOTE, BLOCK183_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "47b5e58d2e8389be529dac1bdf2c9ff79a9d12e1",   # Block 183 note
    "1e584004cf77092f0fdbdc3f51e3458e842eb11c",   # Block 183 runner
)
# THE SECTION-FRAME GRANDPARENT, whose two artifacts are the STALE pin's tell.
BLOCK182_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK182_RUNNER = (
    "scripts/admissibility_dirac_kahler_dual_patch_pullback_section_frame_2026_08_24.py"
)
# THE CARRIER PARENT, read and imported rather than pinned.
BLOCK128_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_"
    "NOTE_2026-08-17.md"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
# THE PRIMARY BODY THIS BLOCK'S CHARTER IS READ FROM.  Block 106 section 12
# step 1 is the instruction this block executes -- DERIVE the reflection-odd ADM
# temporal link rather than prescribe it -- and its step 2, the two-history
# Gram, is the successor this block hands off to.
BLOCK106_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_"
    "NOTE_2026-08-15.md"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time -- this block's own note excepted,
# since it lands later and gate H is the gate that owns it.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TEMPORAL_LINK_EXTRACTION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DERIVED_REFLECTION_SEAM_DUAL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_derived_reflection_seam_dual_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_PATCH_PULLBACK_SECTION_FRAME_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_dual_patch_pullback_section_frame_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
# THE BLOCK'S OWN NOTE is the one audit input gate A does NOT require readable,
# because it does not exist until landing and gate H is the gate that owns it.
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 183 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 183 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block183-"
              "derived-reflection-seam-dual-20260824")
PARENT_COMMIT = "b1648d61971b7cc10bdf61749211bad8b97f9935"
# The Block 182 tip: a real ancestor of HEAD that predates Block 183 and
# therefore carries NEITHER Block 183 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "9900b2f21e57a732637c8af7ab03667f919e956d"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_os_positivity",
    "claim_adm_reading",
    "claim_frame_unique",
    "break_band_table",
    "break_link_rank",
    "break_parity_theorem",
    "break_wrong_dual_contrast",
    "break_shear_vanishing",
    "break_even_part",
    "break_det_positivity",
    "break_quotient_bands",
    "break_twist_negation",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_os_positivity": "B",
    "claim_adm_reading": "B",
    "claim_frame_unique": "B",
    "break_band_table": "C",
    "break_link_rank": "D",
    "break_parity_theorem": "E",
    "break_wrong_dual_contrast": "E",
    "break_shear_vanishing": "F",
    "break_even_part": "F",
    "break_det_positivity": "G",
    "break_quotient_bands": "G",
    "break_twist_negation": "G",
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
        # THE STALE LEG.  At the Block 182 tip NEITHER Block 183 artifact
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
    "the certified Block 105 curved carrier exactly as landed by Block 128 and re-used by Blocks 181, 182 and 183 -- the 8x4 cover of dimension 32, the parameterized cover Hodge over the LANDED Block 105 overlap field, the chart differential d_00 and the completion convention Q(H,d) = m*H + i*(H d + d^H H) at SYMBOLIC POSITIVE MASS",
    "the MINIMAL reflection-closed frame H_min = (H + U_x^T H U_x)/2, ONE ADMITTED MEMBER of the sixteen-member equal-weight closed family Block 183 enumerated, taken here BECAUSE IT IS THE MINIMAL ONE and with NO uniqueness claimed for it",
    "Block 183's derived bond reflection R = P_edge * tpar with its conjugate differential d_ref = R d_00 R^-1, its cell map M = [[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]], the dual block M H(q,v) M^T and the cell field reflection theta(t,x) = ((2-t)%4, x), all rebuilt here rather than imported from any scratchpad",
    "the BAND DECOMPOSITION by time separation dt = (row//4 - col//4) mod 8, the per-bond link blocks L_t = Q_min[slice t+1, slice t] and the intra-slice blocks D_t = Q_min[slice t, slice t]",
    "the PER-SLICE SYMBOLIC FIELD (q_t, v_t) constant in x, with the odd/even split of a link block under q -> -q",
    "Block 128's LANDED antiperiodic quotient psi(t+4) = -psi(t) applied to Q_min, with its four quotient bonds",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS rather than prose, so
# the B mutations bite on an object.  ALL FIVE ARE FALSE AND STAY FALSE.  The
# link is EXTRACTED and no pairing is shown positive; no Gram is built; no
# gravity result exists here; THE ADM LAPSE/SHIFT IDENTIFICATION IS A READING of
# the measured even/odd structure and is never a theorem; and the frame is one
# admitted member of Block 183's family, not a selected point.
OS_POSITIVITY_CLAIMED = False
TWO_HISTORY_GRAM_CLAIMED = False
GRAVITY_CLAIMED = False
ADM_READING_CLAIMED = False
FRAME_UNIQUENESS_CLAIMED = False

# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
ZERO_RESIDUAL = 0
COVER_DIM = 32
QUOTIENT_DIM = 16
LEADING_MINOR_COUNT = 32
BAND_TABLE = {0: 80, 1: 72, 2: 16, 6: 16, 7: 72}
BAND_TOTAL = 256
# THE BLOCK 181 EQUAL-WEIGHT POINT, re-measured HERE so the "same census" claim
# is a measurement of this runner's and not a recollection: it carries the SAME
# five-band census while differing from the minimal frame at 96 entries.
EQUAL_WEIGHT_ORIGINS = ((0, 0), (0, 1), (1, 0), (1, 1))
EQUAL_WEIGHT_SEPARATION = 96
LINK_BAND_ENTRIES = 72
LINK_RANK = 4
LINK_NNZ = (10, 8, 10, 8, 10, 8, 10, 8)
LINK_NON_IDENTITIES = {"dagger": 40, "minus_dagger": 32, "transpose": 40}
WRONG_DUAL_RESIDUAL = 16
WRONG_BAND_RESIDUAL = 144
NO_DUAL_RESIDUAL = 96
ODD_BOND_NNZ = 8
EVEN_BOND_NNZ = 10
EVEN_BOND_ODD_PART_NNZ = 8
EVEN_BOND_EVEN_PART_NNZ = 4
# THE EVEN PART, AS THE ADVERSARIAL CHECK CORRECTED IT: four DIAGONAL entries
# with these signs and ONE common magnitude E, built in measure().
EVEN_PART_POSITIONS = ((0, 0), (1, 1), (2, 2), (3, 3))
EVEN_PART_SIGNS = (-1, 1, -1, 1)
# THE TWIST CERTIFICATE, AS THE CHECKER MEASURED IT: the quotient seam bond is
# MINUS the cover bond 3 -> 4 at the SAME field pair, with the entrywise ratio
# -1 at all EIGHT common nonzero positions.
TWIST_POSITIONS = ((0, 0), (0, 1), (0, 2), (1, 2),
                   (2, 0), (2, 2), (2, 3), (3, 0))
TWIST_RATIO = -1
SLICE_COUNT = 8
DISTINCT_DET_COUNT = 4
DET_DEGREE = 4
DET_COEFFICIENT_COUNT = 3
QUOTIENT_BAND_TABLE = {0: 40, 1: 36, 2: 16, 3: 36}
QUOTIENT_BOND_NNZ = (10, 8, 10, 8)

# THE CHARTER'S CITATION PINS, read from the PRIMARY BODIES so the block's
# instruction and its hand-off have a measured referent and are never a
# recollection.  Block 106 section 12 step 1 is what this block executes and its
# step 2 is the successor; Block 183's own note supplies the frame lattice this
# block picks its minimal member out of, and its own NOT-CLAIMED key for the
# extraction is the sentence this block answers.
B106_STEP1_PIN = "derive the reflection-odd ADM temporal link and seam overlap from"
B106_STEP2_PIN = "test the unnormalized two-history Gram on both spatial eigenlines"
B183_MINIMAL_PIN = "THE MINIMAL MEMBER IS `{I, U_x}`"
B183_NOT_EXTRACTED_PIN = "NO TEMPORAL-LINK EXTRACTION IS PERFORMED"

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


def positive_definite(matrix: sp.Matrix) -> bool:
    """SYMMETRY PLUS 32 EXACTLY POSITIVE LEADING PRINCIPAL MINORS.  Exact
    rational determinants by the Berkowitz algorithm: no eigenvalue estimate,
    no numerical factorization and no tolerance enters the decision."""
    if residual_count(matrix - matrix.T) != 0:
        return False
    return all(matrix[:size, :size].det(method="berkowitz") > 0
               for size in range(1, matrix.rows + 1))


# ---------------------------------------------------------------------------
# the cover: the shift cocycle, the chart differential, the reflection
# ---------------------------------------------------------------------------
T_COVER, X_EXTENT = b128.COVER_TIME_EXTENT, b128.SPACE_EXTENT
PHYSICAL_T = b128.PHYSICAL_TIME_EXTENT
N_COVER = T_COVER * X_EXTENT
MASS = b128.MASS
IU = sp.I
SYMBOLIC_MASS = sp.Symbol("m", positive=True)
SHEAR_SYMBOL, VOLUME_SYMBOL = sp.symbols("q v")
SLICE_SHEARS = sp.symbols("q0 q1 q2 q3")
SLICE_VOLUMES = sp.symbols("v0 v1 v2 v3")

# BLOCK 183'S CELL MAP, rebuilt here.  A signed corner swap: it exchanges the
# scalar slot with the dt slot and the dx slot with the dx^dt slot, with the
# sign that makes M^2 = -I.
CELL_MAP = sp.Matrix([[0, 0, -1, 0],
                      [0, 0, 0, -1],
                      [1, 0, 0, 0],
                      [0, 1, 0, 0]])


def cover_shift(dt: int, dx: int) -> sp.Matrix:
    """The PLAIN translation on the cover: no staggered sign is needed."""
    shift = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            shift[b128.cover_index(t + dt, x + dx), b128.cover_index(t, x)] = 1
    return shift


def edge_reflection() -> sp.Matrix:
    """P_edge: the SITE permutation t -> 7-t on the 8x4 cover, exactly as Block
    183 derived it from Block 104's bond convention theta(t) = -1-t."""
    matrix = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            matrix[b128.cover_index(T_COVER - 1 - t, x),
                   b128.cover_index(t, x)] = 1
    return matrix


def time_parity() -> sp.Matrix:
    """tpar = diag((-1)^(t%2)): Block 105's P_t = diag(1,1,-1,-1) pullback
    written on this carrier, as Block 183 read it."""
    return sp.diag(*[sp.Integer(-1) ** (t % 2)
                     for t in range(T_COVER) for _ in range(X_EXTENT)])


def completion(hodge: sp.Matrix, differential: sp.Matrix,
               mass: object = SYMBOLIC_MASS) -> sp.Matrix:
    """The LANDED b128 completion convention, applied to a supplied pairing, at
    SYMBOLIC POSITIVE MASS by default so every identity below is an operator
    identity in m and not a coincidence at MASS = 2/7."""
    return sp.expand(mass * hodge
                     + IU * (hodge * differential + differential.H * hodge))


def shear_block(shear: object, volume: object) -> sp.Matrix:
    """The LANDED Block 105 shear Hodge, read through Block 128."""
    return b128.block105.shear_hodge(shear, volume)


def dual_block(shear: object, volume: object) -> sp.Matrix:
    """BLOCK 183'S DUAL BLOCK, M H(q,v) M^T, rebuilt."""
    return sp.expand(CELL_MAP * shear_block(shear, volume) * CELL_MAP.T)


def hodge_cover(field: dict, block=shear_block) -> sp.Matrix:
    """THE PARAMETERIZED COVER HODGE H[g], with the CELL BLOCK left free.  With
    `block = shear_block` this is the LANDED b128 curved_hodge_cover
    construction with the field free -- gate C controls it against the landed
    object -- and with `block = dual_block` it is the DUAL-FRAME Hodge."""
    result = sp.zeros(N_COVER, N_COVER)
    for t in range(T_COVER):
        for x in range(X_EXTENT):
            shear, volume = field[(t % PHYSICAL_T, x)]
            embedding = b128.cover_embedding(t, x)
            result += embedding * block(shear, volume) * embedding.T / 4
    return sp.expand(result)


def reflected_field(field: dict) -> dict:
    """theta on the CELL field: (t,x) -> ((2-t)%4, x), Block 183's map."""
    return {(t, x): field[((2 - t) % PHYSICAL_T, x)]
            for t in range(PHYSICAL_T) for x in range(X_EXTENT)}


def minimal_frame(matrix: sp.Matrix, spatial_shift: sp.Matrix) -> sp.Matrix:
    """THE MINIMAL REFLECTION-CLOSED FRAME, (A + U_x^T A U_x)/2.  It is the
    two-shift member {I, U_x} of Block 183's sixteen-member equal-weight closed
    family -- THE MINIMAL ONE, and one member among sixteen."""
    return sp.expand((matrix + spatial_shift.T * matrix * spatial_shift) / 2)


def slice_block(matrix: sp.Matrix, row_slice: int, column_slice: int
                ) -> sp.Matrix:
    """The 4x4 block at (time slice, time slice).  A slice is the four sites of
    one time coordinate, rows/cols 4t .. 4t+3."""
    return sp.expand(matrix[X_EXTENT * row_slice:X_EXTENT * row_slice + X_EXTENT,
                            X_EXTENT * column_slice:X_EXTENT * column_slice
                            + X_EXTENT])


def band(matrix: sp.Matrix, separation: int, period: int = T_COVER
         ) -> sp.Matrix:
    """THE BAND AT TIME SEPARATION dt: the entries with
    (row//4 - col//4) mod period == dt, everything else zeroed."""
    result = sp.zeros(matrix.rows, matrix.cols)
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if (row // X_EXTENT - column // X_EXTENT) % period \
                    == separation % period:
                result[row, column] = matrix[row, column]
    return result


def band_census(matrix: sp.Matrix, period: int = T_COVER) -> dict:
    """THE BAND CENSUS: nonzero entries per time separation, bands with no
    entries omitted.  It is the whole support of the operator, counted."""
    census: dict = {}
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if matrix[row, column] != 0:
                separation = (row // X_EXTENT - column // X_EXTENT) % period
                census[separation] = census.get(separation, 0) + 1
    return dict(sorted(census.items()))


def odd_even_split(matrix: sp.Matrix) -> tuple:
    """THE SPLIT UNDER q -> -q, taken on ALL FOUR slice shears at once:
    (odd, even) with matrix = odd + even.  Exact substitution, no expansion of
    the field into a series and no tolerance."""
    flipped = sp.expand(matrix.subs(
        {shear: -shear for shear in SLICE_SHEARS}, simultaneous=True))
    return (sp.expand((matrix - flipped) / 2),
            sp.expand((matrix + flipped) / 2))


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
    reads the Block 106 and Block 183 notes through this and through nothing
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
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- the certified Block 105 curved carrier as landed by Block 128 and re-used by Blocks 181, 182 and 183 (the 8x4 cover of dimension 32, the parameterized cover Hodge over the LANDED Block 105 overlap field, the chart differential d_00, and the completion Q(H,d) = m*H + i*(H d + d^H H) at SYMBOLIC POSITIVE MASS), THE MINIMAL REFLECTION-CLOSED FRAME H_min = (H + U_x^T H U_x)/2 taken as ONE ADMITTED MEMBER of the sixteen-member family Block 183 enumerated and chosen for MINIMALITY ALONE, Block 183's derived reflection R = P_edge * tpar with d_ref = R d_00 R^-1, the cell map M and the dual block M H(q,v) M^T and the cell field reflection theta(t,x) = ((2-t)%4, x), the BAND DECOMPOSITION by dt = (row//4 - col//4) mod 8 with the per-bond link blocks L_t and the intra-slice blocks D_t, the PER-SLICE SYMBOLIC FIELD (q_t, v_t) constant in x with its odd/even split under q -> -q, and Block 128's LANDED antiperiodic quotient are IMPOSED MEASURED OBJECTS OF THIS BLOCK, rebuilt from the LANDED Block 128 runner and the Block 105 module it re-exports and from NOTHING in any scratchpad. NO OS OR REFLECTION-POSITIVITY THEOREM IS CLAIMED and no pairing is shown positive anywhere; NO TWO-HISTORY GRAM IS BUILT, it being the next leg; NO GRAVITY RESULT IS CLAIMED; THE ADM LAPSE/SHIFT IDENTIFICATION IS A READING OF THE MEASURED EVEN/ODD STRUCTURE AND IS NOT A THEOREM; AND NO UNIQUENESS IS CLAIMED FOR THE FRAME, which is one admitted member of a sixteen-member family whose uniqueness Block 183 REFUTED. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE BAND STRUCTURE, AND THE LINK IS A PAIR. The band census of Q_min = Q(H_min, d_00) by time separation is EXACTLY {dt=0: 80, dt=+1: 72, dt=+2: 16, dt=-2: 16, dt=-1: 72} -- 256 nonzero entries in five bands and NOTHING outside them. THE SAME CENSUS IS CARRIED BY THE DUAL-FRAME ACTION AND BY THE BLOCK 181 EQUAL-WEIGHT POINT, both MEASURED HERE by the same code from the same landed field, the equal-weight point differing from this frame at 96 entries so that the agreement is a fact about the band structure and not about the two points being the same object. THE LINK IS THE dt=+-1 PAIR AND IT IS IRREDUCIBLY A PAIR: B_-1 is NOT the adjoint of B_+1 (40 nonzero entries), NOT minus its adjoint (32) and NOT its transpose (40). THE BACKWARD LINK IS NOT RECOVERABLE FROM THE FORWARD LINK BY ANY OF THE THREE, so the transporter data is the pair and not one block. THE CONTROLS COME FIRST: the parameterized Hodge at the landed field IS the LANDED curved_hodge_cover() at zero residual, R is real orthogonal at zero residual, the frame closes under the reflection at ZERO residual, and the frame is POSITIVE DEFINITE by 32 exact leading principal minors.\nper_mode: THE TRANSPORTER IS INVERTIBLE AT EVERY BOND. The eight per-bond blocks L_t = Q_min[slice t+1, slice t] ALL HAVE RANK EXACTLY 4 and ALL HAVE EMPTY KERNELS, with nonzero counts alternating 10 at even t and 8 at odd t. THE BLOCK 128 KERNEL IS NOT IN THE LINK: the temporal transporter is invertible bond by bond on this frame, and whatever degeneracy the carrier carries lives in the slice Schur complement rather than in the link. THIS IS THE INPUT THE TWO-HISTORY GRAM NEEDS AND IT IS SUPPLIED HERE AS A MEASUREMENT, NOT AS AN ASSUMPTION.\nper_block: THE PARITY THEOREM, EXACT, AND ITS DIFFERENTIAL CONVENTION IS LOAD-BEARING. R B_+1 R^-1 = the dt=-1 band of Q_dual EXACTLY, at ZERO residual, where Q_dual = m*H_min_dual[theta g] + i(H_min_dual d_ref + d_ref^H H_min_dual) is the DUAL-FRAME completion built with the SEAM IDENTITY'S OWN differential d_ref = R d_00 R^-1. THE FORWARD LINK MAPS EXACTLY ONTO THE DUAL BACKWARD LINK. AND THE CONVENTION IS MEASURED RATHER THAN ASSERTED: against the WRONG dual, the one built with d_00 in place of d_ref, the residual is EXACTLY 16 NONZERO ENTRIES; against the dt=+1 band of the dual it is 144; and against the dt=-1 band of the ORIGINAL frame it is 96. THREE FAILING NEIGHBOURS MEASURED IN THE SAME RUN, AND THE 16 IS THE SHARPEST OF THEM: the theorem is specific to the dual frame AND to its own differential, and a reader who substitutes d_00 gets a false statement.\nlattice_wide: THE SYMBOLIC ADM SPLIT, AS THE ADVERSARIAL CHECK CORRECTED IT, AND THE READING THAT GOES WITH IT IS MARKED. At a per-slice symbolic field (q_t, v_t) constant in x, and with the shear variable a_t = q_t v_t / (q_t^2 - 1), THE ODD BONDS CARRY PURE SHEAR: L_1 has EXACTLY 8 nonzero entries and the whole table is exhibited -- -3 a_1/20 at (0,0) and (2,2), +3 a_1/20 at (0,2) and (2,0), and m a_1/4 at (0,1), (1,2), (2,3) and (3,0) -- so L_1 VANISHES IDENTICALLY AT q_1 = 0. THE EVEN BONDS CARRY THE SAME 8-ENTRY SHEAR PATTERN PLUS FOUR MORE: L_0 has 10 nonzero entries splitting EXACTLY 8 ODD and 4 EVEN under q -> -q, THE MASS APPEARS ONLY IN THE ODD PART, and at q_0 = 0 exactly the 4 even entries survive. THE EVEN PART IS FOUR DIAGONAL ENTRIES WITH SIGNS (-,+,-,+) AND COMMON MAGNITUDE E = (1/v_0 + v_1 - v_0/(q_0^2 - 1) - v_1/(q_1^2 - 1))/5, AND IT IS GENUINELY SHEAR-DEPENDENT: dE/dq_0 = 2 q_0 v_0/(5(q_0^2 - 1)^2) and dE/dq_1 = 2 q_1 v_1/(5(q_1^2 - 1)^2) are both NONZERO and both ODD, which is exactly why E is EVEN and why the 8/4 parity split stands. THE SOLVE'S 'no q dependence' CLAUSE IS REFUTED BY MEASUREMENT AND THE CHECKER'S VERSION IS WHAT SHIPS. UNDER THE PYTHAGOREAN WITNESS CONSTRAINT q_t^2 + v_t^2 = 1, WHICH THE LANDED FIELD SATISFIES AT EVERY CELL, E REDUCES EXACTLY TO (v_1 + 1/v_1 + 2/v_0)/5. THE READING, MARKED AS A READING: the even/odd bond alternation realizes the ADM lapse/shift split, even bonds carrying lapse-and-volume data of ADJACENT slices plus the shear and odd bonds carrying pure shear transport with the mass coupled to it, and the shear-SQUARED corrections in the lapse-transport weights are what an ADM decomposition would predict, the inverse metric's time components carrying shift-squared terms. NO ADM QUANTITY IS DERIVED, THE IDENTIFICATION IS NOT A THEOREM, THE PHYSICAL REMARK IS UNTESTED HERE, AND THE BANNER KEY IS GATED AS A DECLARED CONSTANT.\nper_scope: THE POLE LOCUS, THE QUOTIENT, AND THE SEAM SIGN. The eight intra-slice blocks D_t have determinants that are EVEN QUARTICS IN m WITH ALL THREE COEFFICIENTS STRICTLY POSITIVE; slices t and t+4 agree exactly so there are FOUR distinct determinants; and therefore det D_t > 0 FOR EVERY REAL m INCLUDING m = 0, gated at the coefficient level and again at m = 0. THE SLICE SCHUR FACTORIZATION IS GLOBALLY REGULAR ON THE PHYSICAL MASS AXIS AT THIS FRAME'S DECOMPOSITION, with the poles at m^2 < 0 off the physical line. THE SCOPE IS EXACT AND IT IS NARROW: the #7338 no-pole-free-section warning is DISCHARGED FOR REAL MASS AT THIS DECOMPOSITION ONLY -- their metric-coupled vertical Schur poles are a DIFFERENT decomposition on DIFFERENT fixtures, and nothing here touches those. AND THE BLOCK DESCENDS: on Block 128's LANDED 16-dimensional antiperiodic quotient the band census is EXACTLY {0: 40, +1: 36, +2: 16, -1: 36} and all four quotient bonds have rank 4 with the same 10/8 alternation. AND THE TWIST CERTIFICATE IS A CERTIFICATE RATHER THAN AN EXPECTATION: the quotient seam bond equals MINUS the cover bond 3 -> 4 at the SAME field pair, EXACTLY -- the sum is the zero matrix, the difference is not, and the entrywise ratio is -1 at all EIGHT common nonzero positions (0,0), (0,1), (0,2), (1,2), (2,0), (2,2), (2,3) and (3,0). IT WAS QUEUED BY THE SOLVE, MEASURED BY THE ADVERSARIAL CHECKER, AND THE CHECKER'S MEASUREMENT IS WHAT IS GATED: the antiperiodic seam sign is a measured fact of the descent.\nRESULT: THE TEMPORAL LINK IS EXTRACTED, IT IS INVERTIBLE AT EVERY BOND, IT OBEYS AN EXACT PARITY THEOREM AGAINST THE DUAL FRAME, ITS SYMBOLIC FORM SPLITS EVEN AND ODD BONDS, AND THE SLICE DETERMINANTS ARE STRICTLY POSITIVE FOR EVERY REAL MASS. The band census is {0: 80, +-1: 72, +-2: 16}; the eight per-bond blocks all have rank 4 and empty kernels at 10/8 nonzeros; R B_+1 R^-1 is the dual frame's dt=-1 band at ZERO residual against failing neighbours at 16, 144 and 96; the odd bonds are pure shear vanishing at zero shear while the even bonds carry four more diagonal entries, free of the mass and of common magnitude E, which is even in the shears but NOT free of them; the four distinct slice determinants are even quartics with every coefficient strictly positive; the quotient census is {0: 40, +-1: 36, +2: 16} with four full-rank bonds; and the quotient seam bond is MINUS the cover bond 3 -> 4 exactly. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 128, 181, 182 and 183 STAND EXACTLY AS LANDED; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: it is a SINGLE FIXTURE FAMILY, the b128 8x4 cover over the certified Block 105 curved carrier, at ONE landed field for the numeric legs and ONE per-slice symbolic family for the split, with NO width ladder and NO second carrier rule; it works at ONE MEMBER of Block 183's sixteen-member closed frame family, chosen for MINIMALITY, with NO UNIQUENESS CLAIMED; THE ADM LAPSE/SHIFT IDENTIFICATION IS A READING AND NOT A THEOREM; THE POLE STATEMENT IS SCOPED TO REAL MASS AND TO THIS FRAME'S SLICE DECOMPOSITION and says nothing about the #7338 charts' own vertical Schur; NO OS OR REFLECTION-POSITIVITY THEOREM IS CLAIMED and no pairing is shown positive; NO TWO-HISTORY GRAM IS BUILT; and the whole block is KINEMATIC FRAME DATA. AND ONE SOLVE-SIDE CLAUSE WAS REFUTED BY THE ADVERSARIAL CHECK BEFORE LANDING AND THE CHECKER'S VERSION IS WHAT SHIPS: the even part of the even bond is NOT free of the shear -- it is four diagonal entries of common magnitude E, EVEN in the shears but genuinely q^2-dependent, both derivatives nonzero -- against the solve's compressed 'no q dependence' clause. THE ERROR WAS A SPEC COMPRESSION: the anchor's own displayed formula already carried the q^2 dependence and the summary clause outran it, and the rule reaffirmed is STATE FORMULAS, NOT SUMMARIES, IN CLAIM REGISTERS. THE d_ref CONVENTION CATCH IS A DIFFERENT THING AND IS RECORDED AS PROCESS AND NOT AS A CORRECTION: the first comparison in the solve used d_00 for the dual differential and failed at 16 entries, the seam identity's own differential d_ref was substituted and the residual went to ZERO, and the whole exchange happened INSIDE the solve and never left it. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE TEMPORAL-LINK EXTRACTION COMPLETE anchor, as corrected by the b184 adversarial check.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
        "os_positivity_claimed": OS_POSITIVITY_CLAIMED,
        "two_history_gram_claimed": TWO_HISTORY_GRAM_CLAIMED,
        "gravity_claimed": GRAVITY_CLAIMED,
        "adm_reading_claimed": ADM_READING_CLAIMED,
        "frame_uniqueness_claimed": FRAME_UNIQUENESS_CLAIMED,
        # C -- the controls and the band structure.
        "citation_pins": True,
        "hodge_control_residual": ZERO_RESIDUAL,
        "reflection_is_orthogonal_residual": ZERO_RESIDUAL,
        "frame_closure_residual": ZERO_RESIDUAL,
        "frame_positive_definite": True,
        "frame_leading_minors": LEADING_MINOR_COUNT,
        "band_census": BAND_TABLE,
        "band_total": BAND_TOTAL,
        "equal_weight_versus_minimal_entries": EQUAL_WEIGHT_SEPARATION,
        "link_band_entries": LINK_BAND_ENTRIES,
        "link_non_identities": LINK_NON_IDENTITIES,
        # D -- the invertible transporter.
        "link_rank": LINK_RANK,
        "link_nnz": LINK_NNZ,
        "link_kernel_dimensions": 0,
        "link_block_count": SLICE_COUNT,
        # E -- the parity theorem and its convention.
        "parity_theorem_residual": ZERO_RESIDUAL,
        "wrong_dual_residual": WRONG_DUAL_RESIDUAL,
        "wrong_dual_contrast": True,
        "wrong_band_residual": WRONG_BAND_RESIDUAL,
        "no_dual_residual": NO_DUAL_RESIDUAL,
        # F -- the symbolic ADM split.
        "odd_bond_nnz": ODD_BOND_NNZ,
        "odd_bond_at_zero_shear_nnz": 0,
        "odd_bond_table_residual": ZERO_RESIDUAL,
        "even_bond_nnz": EVEN_BOND_NNZ,
        "even_bond_odd_part_nnz": EVEN_BOND_ODD_PART_NNZ,
        "even_bond_even_part_nnz": EVEN_BOND_EVEN_PART_NNZ,
        "mass_in_odd_part": True,
        "mass_in_even_part": False,
        "even_bond_at_zero_shear_nnz": EVEN_BOND_EVEN_PART_NNZ,
        "even_bond_zero_shear_is_even_part": ZERO_RESIDUAL,
        "even_part_positions": EVEN_PART_POSITIONS,
        "even_part_signs": EVEN_PART_SIGNS,
        "even_part_magnitude_residual": ZERO_RESIDUAL,
        "even_part_shear_dependent": True,
        "even_part_derivative_residual": ZERO_RESIDUAL,
        "pythagorean_reduction_residual": ZERO_RESIDUAL,
        # G -- the pole locus, the quotient and the queued certificate.
        "slice_det_count": SLICE_COUNT,
        "slice_det_period_residual": ZERO_RESIDUAL,
        "distinct_det_count": DISTINCT_DET_COUNT,
        "det_degrees": (DET_DEGREE,) * DISTINCT_DET_COUNT,
        "det_odd_coefficients_zero": True,
        "det_coefficient_counts": (DET_COEFFICIENT_COUNT,) * DISTINCT_DET_COUNT,
        "det_all_coefficients_positive": True,
        "det_zero_mass_all_positive": True,
        "quotient_dimension": QUOTIENT_DIM,
        "quotient_band_census": QUOTIENT_BAND_TABLE,
        "quotient_bond_rank": LINK_RANK,
        "quotient_bond_nnz": QUOTIENT_BOND_NNZ,
        "twist_negation_residual": ZERO_RESIDUAL,
        "twist_is_not_the_identity": True,
        "twist_positions": TWIST_POSITIONS,
        "twist_ratios_all_minus_one": True,
        "mass_is_symbolic": True,
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
    elif mutation == "claim_os_positivity":
        # THE SCOPE OVERSOLD: an extracted link asserted to supply an OS or
        # reflection-positivity theorem, which extraction alone never supplies
        # -- no pairing is shown positive anywhere in this block.
        claims["os_positivity_claimed"] = True
    elif mutation == "claim_adm_reading":
        # THE READING PROMOTED: the lapse/shift identification asserted as a
        # derived ADM decomposition, which the measured even/odd structure does
        # not supply.  This is the mutation that guards the block's single
        # biggest overreach risk.
        claims["adm_reading_claimed"] = True
    elif mutation == "claim_frame_unique":
        # THE FRAME OVERSOLD: the minimal frame asserted to be the unique
        # admissible one, which Block 183's fifteen smaller closed sets refute
        # outright.  Minimality is a choice criterion and never a selection.
        claims["frame_uniqueness_claimed"] = True
    elif mutation == "break_band_table":
        # THE SUPPORT MOVED: a dt=+3 band asserted present, which the exact
        # five-band census forbids -- and if the support were wider the "link"
        # would not be the dt=+-1 pair at all.
        claims["band_census"] = {**BAND_TABLE, 3: 8}
    elif mutation == "break_link_rank":
        # THE TRANSPORTER DEGRADED: a rank-3 bond block asserted allowed, which
        # eight exact rank-4 measurements forbid.  A rank-deficient link is the
        # one thing that would stop the two-history Gram before it started.
        claims["link_rank"] = 3
    elif mutation == "break_parity_theorem":
        # THE THEOREM DELETED: a nonzero R B_+1 R^-1 - B_-1[dual] residual
        # asserted allowed, which the exact identity forbids.
        claims["parity_theorem_residual"] = 4
    elif mutation == "break_wrong_dual_contrast":
        # THE CONVENTION ERASED: the WRONG dual asserted to satisfy the theorem
        # too, which the measured 16-entry residual forbids.  This is the
        # mutation that guards the block's own inline self-catch.
        claims["wrong_dual_contrast"] = False
        claims["wrong_dual_residual"] = ZERO_RESIDUAL
    elif mutation == "break_shear_vanishing":
        # THE PURE-SHEAR ODD BOND DENIED: the odd bond asserted to survive at
        # zero shear, which the exact identical vanishing forbids -- and with it
        # the whole even/odd split that the ADM reading reads.
        claims["odd_bond_at_zero_shear_nnz"] = ODD_BOND_NNZ
    elif mutation == "break_even_part":
        # THE REFUTED CLAUSE RESTORED: the even part asserted free of the
        # shear, which the two exactly nonzero derivatives
        # dE/dq_0 = 2 q_0 v_0/(5(q_0^2 - 1)^2) and dE/dq_1 forbid.  This is the
        # mutation that guards the correction the adversarial check forced.
        claims["even_part_shear_dependent"] = False
    elif mutation == "break_det_positivity":
        # THE POLE LOCUS MOVED ONTO THE PHYSICAL AXIS: a non-positive
        # determinant coefficient asserted allowed, which twelve exactly
        # positive coefficients forbid.  Without it the regularity statement is
        # gone.
        claims["det_all_coefficients_positive"] = False
    elif mutation == "break_quotient_bands":
        # THE DESCENT BROKEN: a different quotient census asserted, which the
        # exact four-band count forbids.
        claims["quotient_band_census"] = {**QUOTIENT_BAND_TABLE, 1: 40}
    elif mutation == "break_twist_negation":
        # THE SEAM SIGN DENIED: the quotient seam bond asserted NOT to be minus
        # the cover bond, which the exact zero sum and the eight entrywise
        # ratios of -1 forbid.  This is the mutation that guards the
        # certificate the adversarial check supplied.
        claims["twist_negation_residual"] = 8
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
    hodge_control_residual: int
    reflection_is_orthogonal_residual: int
    frame_closure_residual: int
    frame_positive_definite: bool
    frame_leading_minors: int
    band_census: dict
    band_total: int
    dual_band_census: dict
    equal_weight_band_census: dict
    equal_weight_versus_minimal_entries: int
    link_band_entries: tuple
    link_non_identities: dict
    link_rank: tuple
    link_nnz: tuple
    link_kernel_dimensions: tuple
    parity_theorem_residual: int
    wrong_dual_residual: int
    wrong_band_residual: int
    no_dual_residual: int
    undressed_residual: int
    odd_bond_nnz: int
    odd_bond_at_zero_shear_nnz: int
    odd_bond_table_residual: int
    odd_bond_entry_ratios: dict
    odd_bond_symbols: tuple
    even_bond_nnz: int
    even_bond_odd_part_nnz: int
    even_bond_even_part_nnz: int
    even_bond_odd_symbols: tuple
    even_bond_even_symbols: tuple
    mass_in_odd_part: bool
    mass_in_even_part: bool
    even_bond_at_zero_shear_nnz: int
    even_bond_zero_shear_is_even_part: int
    even_part_positions: tuple
    even_part_signs: tuple
    even_part_magnitude_residual: int
    even_part_magnitude: str
    even_part_shear_derivatives: tuple
    even_part_derivative_residual: int
    even_part_shear_dependent: bool
    pythagorean_reduction_residual: int
    pythagorean_reduction: str
    slice_det_period_residual: int
    slice_det_count: int
    distinct_det_count: int
    det_degrees: tuple
    det_odd_coefficients_zero: bool
    det_coefficient_counts: tuple
    det_all_coefficients_positive: bool
    det_zero_mass_values: tuple
    det_zero_mass_all_positive: bool
    det_expressions: tuple
    quotient_dimension: int
    quotient_band_census: dict
    quotient_bond_rank: tuple
    quotient_bond_nnz: tuple
    twist_negation_residual: int
    twist_identity_residual: int
    twist_positions: tuple
    twist_ratios: tuple
    twist_ratios_all_minus_one: bool
    mass_is_symbolic: bool


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    # --- the carrier, rebuilt from the LANDED Block 128 runner --------------
    Ux = cover_shift(0, 1)
    d00 = sp.Matrix(b128.chart_differential_cover((0, 0)))
    field = b128.block105.overlap_field()
    theta_g = reflected_field(field)
    P_edge = edge_reflection()
    R = sp.expand(P_edge * time_parity())
    # R IS REAL ORTHOGONAL, so its inverse is its transpose.  No operator
    # inverse is ever formed anywhere in this runner.
    R_inv = R.T
    d_ref = sp.expand(R * d00 * R_inv)

    # --- the controls, before any band is cut -------------------------------
    H_field = hodge_cover(field)
    hodge_control_residual = residual_count(
        H_field - sp.Matrix(b128.curved_hodge_cover()))
    reflection_is_orthogonal_residual = residual_count(
        R * R.T - sp.eye(N_COVER))
    H_min = minimal_frame(H_field, Ux)
    H_dual_theta = hodge_cover(theta_g, dual_block)
    H_min_dual = minimal_frame(H_dual_theta, Ux)
    frame_closure_residual = residual_count(R * H_min * R_inv - H_min_dual)
    frame_positive_definite = positive_definite(H_min)

    # --- C: the band structure ---------------------------------------------
    Q_min = completion(H_min, d00)
    Q_dual = completion(H_min_dual, d_ref)
    Q_wrong_dual = completion(H_min_dual, d00)
    band_census_min = band_census(Q_min)
    band_census_dual = band_census(Q_dual)
    # THE BLOCK 181 EQUAL-WEIGHT POINT, built by the SAME code from the SAME
    # landed field and banded the SAME way: the census claim is measured here.
    Ut = cover_shift(1, 0)
    equal_weight_shifts = tuple(
        sp.expand(Ut ** origin[0] * Ux ** origin[1])
        for origin in EQUAL_WEIGHT_ORIGINS)
    H_equal_weight = sp.expand(
        sum([shift.T * H_field * shift for shift in equal_weight_shifts],
            sp.zeros(N_COVER, N_COVER)) / len(equal_weight_shifts))
    equal_weight_band = band_census(completion(H_equal_weight, d00))
    equal_weight_versus_minimal_entries = residual_count(
        H_equal_weight - H_min)
    forward_link = band(Q_min, 1)
    backward_link = band(Q_min, -1)
    link_non_identities = {
        "dagger": residual_count(backward_link - forward_link.H),
        "minus_dagger": residual_count(backward_link + forward_link.H),
        "transpose": residual_count(backward_link - forward_link.T),
    }

    # --- D: the eight per-bond blocks --------------------------------------
    link_blocks = tuple(
        slice_block(Q_min, (t + 1) % T_COVER, t) for t in range(T_COVER))
    link_rank = tuple(block.rank() for block in link_blocks)
    link_nnz = tuple(nonzero_entries(block) for block in link_blocks)
    link_kernel_dimensions = tuple(
        len(block.nullspace()) for block in link_blocks)

    # --- E: the parity theorem and its three failing neighbours ------------
    reflected_forward = sp.expand(R * forward_link * R_inv)
    parity_theorem_residual = residual_count(
        reflected_forward - band(Q_dual, -1))
    # THE CONVENTION CONTRAST.  The SAME statement against the dual frame built
    # with d_00 instead of the seam identity's own d_ref.
    wrong_dual_residual = residual_count(
        reflected_forward - band(Q_wrong_dual, -1))
    wrong_band_residual = residual_count(reflected_forward - band(Q_dual, 1))
    no_dual_residual = residual_count(reflected_forward - band(Q_min, -1))
    undressed_residual = residual_count(
        P_edge * forward_link * P_edge.T - band(Q_dual, -1))

    # --- F: the symbolic ADM split -----------------------------------------
    symbolic_field = {
        (t, x): (SLICE_SHEARS[t], SLICE_VOLUMES[t])
        for t in range(PHYSICAL_T) for x in range(X_EXTENT)}
    H_symbolic = minimal_frame(hodge_cover(symbolic_field), Ux)
    Q_symbolic = completion(H_symbolic, d00)
    odd_bond = slice_block(Q_symbolic, 2, 1)          # L_1, an ODD bond
    even_bond = slice_block(Q_symbolic, 1, 0)         # L_0, an EVEN bond
    odd_bond_nnz = nonzero_entries(odd_bond)
    odd_bond_at_zero_shear_nnz = residual_count(
        odd_bond.subs({SLICE_SHEARS[1]: 0}))
    # THE WHOLE 8-ENTRY TABLE, EXHIBITED AND COMPARED ENTRYWISE, in the
    # checker's shear variable a_t = q_t v_t / (q_t^2 - 1).
    shear_variable = (SLICE_SHEARS[1] * SLICE_VOLUMES[1]
                      / (SLICE_SHEARS[1] ** 2 - 1))
    odd_bond_table = sp.zeros(X_EXTENT, X_EXTENT)
    for position, coefficient in (((0, 0), sp.Rational(-3, 20)),
                                  ((2, 2), sp.Rational(-3, 20)),
                                  ((0, 2), sp.Rational(3, 20)),
                                  ((2, 0), sp.Rational(3, 20)),
                                  ((0, 1), SYMBOLIC_MASS / 4),
                                  ((1, 2), SYMBOLIC_MASS / 4),
                                  ((2, 3), SYMBOLIC_MASS / 4),
                                  ((3, 0), SYMBOLIC_MASS / 4)):
        odd_bond_table[position] = coefficient * shear_variable
    odd_bond_table_residual = sum(
        1 for row in range(X_EXTENT) for column in range(X_EXTENT)
        if sp.simplify(odd_bond[row, column] - odd_bond_table[row, column]) != 0)
    odd_bond_entry_ratios = {
        (row, column): str(sp.simplify(odd_bond[row, column] / shear_variable))
        for row in range(X_EXTENT) for column in range(X_EXTENT)
        if odd_bond[row, column] != 0}
    odd_bond_symbols = tuple(sorted(str(s) for s in odd_bond.free_symbols))
    odd_part, even_part = odd_even_split(even_bond)
    even_bond_nnz = nonzero_entries(even_bond)
    even_bond_odd_part_nnz = nonzero_entries(odd_part)
    even_bond_even_part_nnz = nonzero_entries(even_part)
    even_bond_odd_symbols = tuple(sorted(str(s) for s in odd_part.free_symbols))
    even_bond_even_symbols = tuple(
        sorted(str(s) for s in even_part.free_symbols))
    mass_in_odd_part = SYMBOLIC_MASS in odd_part.free_symbols
    mass_in_even_part = SYMBOLIC_MASS in even_part.free_symbols
    even_bond_zero_shear = sp.expand(even_bond.subs({SLICE_SHEARS[0]: 0}))
    even_bond_at_zero_shear_nnz = nonzero_entries(even_bond_zero_shear)
    even_bond_zero_shear_is_even_part = residual_count(
        even_bond_zero_shear - even_part.subs({SLICE_SHEARS[0]: 0}))
    # THE EVEN PART IN CLOSED FORM, AS THE ADVERSARIAL CHECK SUPPLIED IT: four
    # DIAGONAL entries, signs (-,+,-,+), ONE common magnitude E.
    even_magnitude = (1 / SLICE_VOLUMES[0] + SLICE_VOLUMES[1]
                      - SLICE_VOLUMES[0] / (SLICE_SHEARS[0] ** 2 - 1)
                      - SLICE_VOLUMES[1] / (SLICE_SHEARS[1] ** 2 - 1)) / 5
    even_part_positions = tuple(
        (row, column) for row in range(X_EXTENT) for column in range(X_EXTENT)
        if even_part[row, column] != 0)
    even_part_signs = tuple(
        sp.simplify(even_part[position] / even_magnitude)
        for position in even_part_positions)
    even_part_magnitude_residual = sum(
        1 for position, sign in zip(even_part_positions, EVEN_PART_SIGNS)
        if sp.simplify(even_part[position] - sign * even_magnitude) != 0)
    # THE SHEAR DEPENDENCE, MEASURED AS DERIVATIVES.  Both are ODD, which is
    # exactly why E is EVEN and the parity split survives the correction.
    shear_derivatives = tuple(
        sp.simplify(sp.diff(even_magnitude, SLICE_SHEARS[index]))
        for index in (0, 1))
    derivative_targets = tuple(
        2 * SLICE_SHEARS[index] * SLICE_VOLUMES[index]
        / (5 * (SLICE_SHEARS[index] ** 2 - 1) ** 2) for index in (0, 1))
    even_part_derivative_residual = sum(
        1 for measured, target in zip(shear_derivatives, derivative_targets)
        if sp.simplify(measured - target) != 0)
    even_part_shear_dependent = all(
        derivative != 0 for derivative in shear_derivatives)
    # THE PYTHAGOREAN WITNESS CONSTRAINT q_t^2 + v_t^2 = 1, which the LANDED
    # field satisfies at every cell: the magnitude collapses to a pure volume
    # expression.
    pythagorean = {SLICE_SHEARS[index]:
                   sp.sqrt(1 - SLICE_VOLUMES[index] ** 2) for index in (0, 1)}
    pythagorean_target = (SLICE_VOLUMES[1] + 1 / SLICE_VOLUMES[1]
                          + 2 / SLICE_VOLUMES[0]) / 5
    pythagorean_reduced = sp.simplify(even_magnitude.subs(pythagorean))
    pythagorean_reduction_residual = int(
        sp.simplify(pythagorean_reduced - pythagorean_target) != 0)

    # --- G: the pole locus --------------------------------------------------
    slice_dets = tuple(
        sp.expand(sp.cancel(slice_block(Q_min, t, t).det(method="berkowitz")))
        for t in range(T_COVER))
    slice_det_period_residual = sum(
        1 for t in range(PHYSICAL_T)
        if sp.simplify(slice_dets[t] - slice_dets[t + PHYSICAL_T]) != 0)
    distinct_dets = slice_dets[:PHYSICAL_T]
    polynomials = tuple(sp.Poly(det, SYMBOLIC_MASS) for det in distinct_dets)
    det_degrees = tuple(int(poly.degree()) for poly in polynomials)
    coefficient_tables = tuple(
        {int(monomial[0]): coefficient
         for monomial, coefficient in poly.terms()}
        for poly in polynomials)
    det_odd_coefficients_zero = all(
        power % 2 == 0
        for table in coefficient_tables for power in table)
    det_coefficient_counts = tuple(len(table) for table in coefficient_tables)
    det_all_coefficients_positive = all(
        coefficient > 0
        for table in coefficient_tables for coefficient in table.values())
    det_zero_mass_values = tuple(
        det.subs({SYMBOLIC_MASS: 0}) for det in distinct_dets)
    det_zero_mass_all_positive = all(
        value > 0 for value in det_zero_mass_values)
    det_expressions = tuple(str(sp.factor(det)) for det in distinct_dets)

    # --- G: the antiperiodic quotient, LANDED -------------------------------
    Q_quotient = sp.expand(sp.Matrix(b128.antiperiodic_quotient(Q_min)))
    quotient_band = band_census(Q_quotient, PHYSICAL_T)
    quotient_bonds = tuple(
        Q_quotient[X_EXTENT * ((t + 1) % PHYSICAL_T):
                   X_EXTENT * ((t + 1) % PHYSICAL_T) + X_EXTENT,
                   X_EXTENT * t:X_EXTENT * t + X_EXTENT]
        for t in range(PHYSICAL_T))
    quotient_bond_rank = tuple(
        sp.expand(bond).rank() for bond in quotient_bonds)
    quotient_bond_nnz = tuple(
        nonzero_entries(sp.expand(bond)) for bond in quotient_bonds)

    # --- G: THE TWIST CERTIFICATE, MEASURED BY THE CHECKER AND GATED HERE ---
    # THE SAME FIELD PAIR ON BOTH SIDES: the quotient's seam bond, rows of
    # slice 0 against columns of slice 3, against the COVER's bond 3 -> 4.  The
    # gate asserts BOTH halves -- the sum is the zero matrix AND the difference
    # is not -- so a sign-blind implementation cannot satisfy it.
    quotient_seam_bond = sp.expand(Q_quotient[0:X_EXTENT, -X_EXTENT:])
    cover_seam_bond = slice_block(Q_min, PHYSICAL_T, PHYSICAL_T - 1)
    twist_negation_residual = residual_count(
        quotient_seam_bond + cover_seam_bond)
    twist_identity_residual = residual_count(
        quotient_seam_bond - cover_seam_bond)
    twist_positions = tuple(
        (row, column) for row in range(X_EXTENT) for column in range(X_EXTENT)
        if quotient_seam_bond[row, column] != 0
        or cover_seam_bond[row, column] != 0)
    twist_ratios = tuple(
        sp.simplify(quotient_seam_bond[position] / cover_seam_bond[position])
        for position in twist_positions)
    twist_ratios_all_minus_one = all(
        ratio == TWIST_RATIO for ratio in twist_ratios)

    citation_pins = {
        "b106_step1": B106_STEP1_PIN in landed_text(BLOCK106_NOTE),
        "b106_step2": B106_STEP2_PIN in landed_text(BLOCK106_NOTE),
        "b183_minimal": B183_MINIMAL_PIN in landed_text(BLOCK183_NOTE),
        "b183_not_extracted": (
            B183_NOT_EXTRACTED_PIN in landed_text(BLOCK183_NOTE)),
    }
    banners = {
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        # THE DECLARED STATUS FLAGS, so the B mutations bite on a declared
        # object and not on prose.  ALL FIVE ARE MEASURED AND ALL ARE FALSE.
        "objects_registered": bool(REGISTERED_OBJECTS or ADOPTED_OBJECTS),
        "os_positivity_claimed": OS_POSITIVITY_CLAIMED,
        "two_history_gram_claimed": TWO_HISTORY_GRAM_CLAIMED,
        "gravity_claimed": GRAVITY_CLAIMED,
        "adm_reading_claimed": ADM_READING_CLAIMED,
        "frame_uniqueness_claimed": FRAME_UNIQUENESS_CLAIMED,
    }
    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        hodge_control_residual=hodge_control_residual,
        reflection_is_orthogonal_residual=reflection_is_orthogonal_residual,
        frame_closure_residual=frame_closure_residual,
        frame_positive_definite=frame_positive_definite,
        frame_leading_minors=N_COVER,
        band_census=band_census_min,
        band_total=sum(band_census_min.values()),
        dual_band_census=band_census_dual,
        equal_weight_band_census=equal_weight_band,
        equal_weight_versus_minimal_entries=equal_weight_versus_minimal_entries,
        link_band_entries=(nonzero_entries(forward_link),
                           nonzero_entries(backward_link)),
        link_non_identities=link_non_identities,
        link_rank=link_rank,
        link_nnz=link_nnz,
        link_kernel_dimensions=link_kernel_dimensions,
        parity_theorem_residual=parity_theorem_residual,
        wrong_dual_residual=wrong_dual_residual,
        wrong_band_residual=wrong_band_residual,
        no_dual_residual=no_dual_residual,
        undressed_residual=undressed_residual,
        odd_bond_nnz=odd_bond_nnz,
        odd_bond_at_zero_shear_nnz=odd_bond_at_zero_shear_nnz,
        odd_bond_table_residual=odd_bond_table_residual,
        odd_bond_entry_ratios=odd_bond_entry_ratios,
        odd_bond_symbols=odd_bond_symbols,
        even_bond_nnz=even_bond_nnz,
        even_bond_odd_part_nnz=even_bond_odd_part_nnz,
        even_bond_even_part_nnz=even_bond_even_part_nnz,
        even_bond_odd_symbols=even_bond_odd_symbols,
        even_bond_even_symbols=even_bond_even_symbols,
        mass_in_odd_part=mass_in_odd_part,
        mass_in_even_part=mass_in_even_part,
        even_bond_at_zero_shear_nnz=even_bond_at_zero_shear_nnz,
        even_bond_zero_shear_is_even_part=even_bond_zero_shear_is_even_part,
        even_part_positions=even_part_positions,
        even_part_signs=tuple(int(sign) for sign in even_part_signs),
        even_part_magnitude_residual=even_part_magnitude_residual,
        even_part_magnitude=str(sp.simplify(even_magnitude)),
        even_part_shear_derivatives=tuple(
            str(derivative) for derivative in shear_derivatives),
        even_part_derivative_residual=even_part_derivative_residual,
        even_part_shear_dependent=even_part_shear_dependent,
        pythagorean_reduction_residual=pythagorean_reduction_residual,
        pythagorean_reduction=str(pythagorean_reduced),
        slice_det_period_residual=slice_det_period_residual,
        slice_det_count=len(slice_dets),
        distinct_det_count=len({sp.srepr(sp.expand(det))
                                for det in slice_dets}),
        det_degrees=det_degrees,
        det_odd_coefficients_zero=det_odd_coefficients_zero,
        det_coefficient_counts=det_coefficient_counts,
        det_all_coefficients_positive=det_all_coefficients_positive,
        det_zero_mass_values=det_zero_mass_values,
        det_zero_mass_all_positive=det_zero_mass_all_positive,
        det_expressions=det_expressions,
        quotient_dimension=Q_quotient.rows,
        quotient_band_census=quotient_band,
        quotient_bond_rank=quotient_bond_rank,
        quotient_bond_nnz=quotient_bond_nnz,
        twist_negation_residual=twist_negation_residual,
        twist_identity_residual=twist_identity_residual,
        twist_positions=twist_positions,
        twist_ratios=tuple(int(ratio) for ratio in twist_ratios),
        twist_ratios_all_minus_one=twist_ratios_all_minus_one,
        mass_is_symbolic=bool(SYMBOLIC_MASS.is_Symbol
                              and SYMBOLIC_MASS.is_positive
                              and SYMBOLIC_MASS in Q_min.free_symbols
                              and SYMBOLIC_MASS in Q_dual.free_symbols),
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
        "registry blobs in the worktree. THE TWO BLOCK 183 ARTIFACTS ARE "
        "CONTENT-BOUND -- its note and its runner, the pair that identifies "
        "the commit this block's branch is cut from -- at PARENT_COMMIT, in "
        "the worktree and against their pinned blobs, and PARENT_COMMIT IS "
        "REAL and PARENT_REF resolves to it, so nothing needs sed at landing. "
        "THE STALE PIN IS THE BLOCK 182 TIP, a REAL ancestor of HEAD that "
        "PREDATES Block 183 and therefore carries NEITHER Block 183 artifact, "
        "which is exactly what makes the stale_parent_authority mutation bite: "
        "under it the gate looks for the artifact blobs at a commit where they "
        "do not exist. AUDIT_INPUT_PATHS IS LITERAL and every one of its NINE "
        "entries is required readable in the worktree EXCEPT this block's own "
        "note, which lands later and belongs to gate H -- and the nine include "
        "the PRIMARY BODY this block's charter is read from, the Block 106 "
        "note whose section 12 step 1 is the instruction being executed. AND "
        "THE MACHINERY IMPORT IS GATED: the LANDED Block 128 runner must have "
        "imported, because every object this runner measures is rebuilt from "
        "it and from the Block 105 module it re-exports -- NOTHING from any "
        "scratchpad is imported or read anywhere",
        bool(
            AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
            and len(AUDIT_INPUT_PATHS) == 9
            and len(set(AUDIT_INPUT_PATHS)) == 9
            and BLOCK183_NOTE in AUDIT_INPUT_PATHS
            and BLOCK183_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK182_NOTE in AUDIT_INPUT_PATHS
            and BLOCK182_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK128_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK106_NOTE in AUDIT_INPUT_PATHS
            and CAMPAIGN_NOTE in AUDIT_INPUT_PATHS
            # EVERY AUDIT INPUT BUT THIS BLOCK'S OWN NOTE IS READABLE IN THE
            # WORKTREE; the note itself is gate H's, because it lands later.
            and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
            and authority.inputs_missing == ()
            and PARENT_ARTIFACTS == (BLOCK183_NOTE, BLOCK183_RUNNER)
            and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
            and facts.main_head == claims["main_head"]
            and authority.fixed_authority
            and authority.machinery_import_landed
            and authority.parent_pin_is_commit
            and authority.parent_ref_and_ancestry
            and parent_blobs_ok
            # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER
            # Block 183 artifact.
            and authority.stale_is_real_ancestor
            and authority.stale_carries_neither_artifact))

    # --- B: the imposed-object banner and the NOT-CLAIMED keys -------------
    ban = facts.banners
    checks.check(
        "B-THE-IMPOSED-OBJECT-BANNER-and-the-NOT-CLAIMED-keys",
        f"THE BANNER COMES BEFORE ANY NUMERAL AND IT IS MEASURED RATHER THAN "
        f"ASSERTED. {ban['imposed_objects']} objects are IMPOSED by this block "
        f"-- the certified Block 105 curved carrier as landed by Block 128, "
        f"THE MINIMAL REFLECTION-CLOSED FRAME H_min = (H + U_x^T H U_x)/2 "
        f"taken as ONE ADMITTED MEMBER of the sixteen-member family Block 183 "
        f"enumerated and chosen for MINIMALITY ALONE, Block 183's derived "
        f"reflection with its conjugate differential and dual block, the band "
        f"decomposition with its per-bond and intra-slice blocks, the "
        f"per-slice symbolic field with its odd/even split, and Block 128's "
        f"LANDED antiperiodic quotient -- and {ban['registered_objects']} are "
        f"REGISTERED and {ban['adopted_objects']} are ADOPTED. AND THE "
        f"BANNER'S SECOND HALF IS WHAT IS NOT CLAIMED, gated as declared "
        f"constants: NO OS OR REFLECTION-POSITIVITY THEOREM, because "
        f"extracting a link is not showing a pairing positive and no pairing "
        f"is shown positive here; NO TWO-HISTORY GRAM, which is the next leg "
        f"and not this one; NO GRAVITY RESULT; NO ADM IDENTIFICATION AS A "
        f"THEOREM -- the lapse/shift split is a READING of the measured "
        f"even/odd structure and the note marks it as one at every occurrence; "
        f"and NO UNIQUENESS FOR THE FRAME, which is one admitted member of a "
        f"family whose uniqueness Block 183 REFUTED with fifteen smaller "
        f"closed sets. Asserting any of the five, or asserting that the "
        f"imposed objects are registered, fails HERE and nowhere else",
        bool(
            ban["imposed_objects"] == 6
            and ban["registered_objects"] == 0
            and ban["adopted_objects"] == 0
            and ban["objects_registered"] == claims["objects_registered"]
            and ban["os_positivity_claimed"] == claims["os_positivity_claimed"]
            and ban["two_history_gram_claimed"]
            == claims["two_history_gram_claimed"]
            and ban["gravity_claimed"] == claims["gravity_claimed"]
            and ban["adm_reading_claimed"] == claims["adm_reading_claimed"]
            and ban["frame_uniqueness_claimed"]
            == claims["frame_uniqueness_claimed"]))

    # --- C: the controls, then the band structure ---------------------------
    pins = facts.citation_pins
    checks.check(
        "C-THE-CHARTER-AND-THE-FRAME-ARE-READ-FROM-THE-PRIMARY-BODIES",
        f"THE INSTRUCTION THIS BLOCK EXECUTES IS PINNED IN THE NOTE IT COMES "
        f"FROM, not in a recollection of it. Block 106 section 12 step 1 -- "
        f"'{B106_STEP1_PIN}' -- is present in its primary body "
        f"({pins['b106_step1']}), and so is its step 2, "
        f"'{B106_STEP2_PIN}' ({pins['b106_step2']}), which is the successor "
        f"this block hands off to and NOT what this block does. AND THE FRAME "
        f"IS PINNED THE SAME WAY: Block 183's own '{B183_MINIMAL_PIN}' is "
        f"present in its primary body ({pins['b183_minimal']}) -- the frame "
        f"used here is THAT member of THAT enumerated family -- together with "
        f"its '{B183_NOT_EXTRACTED_PIN}' sentence ({pins['b183_not_extracted']}"
        f"), which is the gap this block closes. THE CHARTER AND THE FRAME ARE "
        f"BOTH SOMEBODY ELSE'S LANDED FACT",
        bool(all(pins.values()) == claims["citation_pins"]))
    checks.check(
        "C-CONTROL-the-landed-Hodge-the-orthogonal-R-and-the-CLOSED-PD-FRAME",
        f"THE CONTROLS COME FIRST, ALL FOUR OF THEM. H[landed field] equals "
        f"the LANDED b128 curved_hodge_cover() at {facts.hodge_control_residual}"
        f" nonzero entries, so the parameterized Hodge this block bands is the "
        f"landed object and not a redefinition of it. R R^T - I has "
        f"{facts.reflection_is_orthogonal_residual} nonzero entries, so R is "
        f"REAL ORTHOGONAL, R^-1 = R^T, and NO OPERATOR INVERSE IS EVER FORMED. "
        f"THE FRAME CLOSES: R H_min R^-1 - H_min_dual[theta g] has "
        f"{facts.frame_closure_residual} nonzero entries, so the frame this "
        f"block works at is genuinely one of Block 183's reflection-closed "
        f"points and the parity theorem below is being asked at a point where "
        f"the reflection has somewhere to send it. AND THE FRAME IS POSITIVE "
        f"DEFINITE ({facts.frame_positive_definite}) by "
        f"{facts.frame_leading_minors} exact leading principal minors -- exact "
        f"rational determinants, no eigenvalue estimate and no tolerance. IT "
        f"IS ONE ADMITTED MEMBER CHOSEN FOR MINIMALITY AND NOT A SELECTED "
        f"POINT",
        bool(
            facts.hodge_control_residual == claims["hodge_control_residual"]
            and facts.reflection_is_orthogonal_residual
            == claims["reflection_is_orthogonal_residual"]
            and facts.frame_closure_residual == claims["frame_closure_residual"]
            and facts.frame_positive_definite
            == claims["frame_positive_definite"]
            and facts.frame_leading_minors == claims["frame_leading_minors"]))
    checks.check(
        "C-THE-BAND-CENSUS-and-THE-LINK-IS-A-PAIR-at-40-32-40",
        f"THE SUPPORT OF Q_min IS EXACTLY FIVE BANDS: {facts.band_census} by "
        f"time separation dt = (row//4 - col//4) mod 8, "
        f"{facts.band_total} nonzero entries in total and NOTHING outside "
        f"them. The dual-frame action carries the same census "
        f"({facts.dual_band_census}), AND SO DOES THE BLOCK 181 EQUAL-WEIGHT "
        f"POINT ({facts.equal_weight_band_census}), which is built by the same "
        f"code from the same landed field and MEASURED HERE rather than "
        f"recalled -- and which is a genuinely different frame, differing from "
        f"H_min at {facts.equal_weight_versus_minimal_entries} entries, so the "
        f"agreement is a fact about the band structure and not about the two "
        f"points being the same object. THE LINK IS THE dt=+-1 PAIR, "
        f"{facts.link_band_entries[0]} entries forward and "
        f"{facts.link_band_entries[1]} back. AND IT IS IRREDUCIBLY A PAIR: "
        f"B_-1 is NOT the adjoint of B_+1, NOT minus its adjoint and NOT its "
        f"transpose, at {tuple(facts.link_non_identities.values())} nonzero "
        f"entries respectively -- THREE EXPLICIT NON-IDENTITIES, so the "
        f"backward link is not recoverable from the forward link by any of "
        f"them and the transporter data is the pair. Asserting a sixth band "
        f"fails HERE and nowhere else",
        bool(
            facts.band_census == claims["band_census"]
            and facts.band_total == claims["band_total"]
            and facts.dual_band_census == claims["band_census"]
            and facts.equal_weight_band_census == claims["band_census"]
            and facts.equal_weight_versus_minimal_entries
            == claims["equal_weight_versus_minimal_entries"]
            and facts.link_band_entries
            == (claims["link_band_entries"], claims["link_band_entries"])
            and facts.link_non_identities == claims["link_non_identities"]
            and all(value != 0
                    for value in facts.link_non_identities.values())
            and len(facts.link_non_identities) == 3))

    # --- D: the invertible transporter --------------------------------------
    checks.check(
        "D-THE-TRANSPORTER-IS-INVERTIBLE-AT-EVERY-BOND-rank-4-kernel-empty",
        f"ALL {facts.slice_det_count} PER-BOND LINK BLOCKS "
        f"L_t = Q_min[slice t+1, slice t] HAVE RANK EXACTLY 4 "
        f"({facts.link_rank}) AND EMPTY KERNELS "
        f"({facts.link_kernel_dimensions}), with nonzero counts "
        f"{facts.link_nnz} -- 10 at even t and 8 at odd t. THE TEMPORAL "
        f"TRANSPORTER IS INVERTIBLE BOND BY BOND ON THIS FRAME, at symbolic "
        f"positive mass, which is the input the two-history Gram needs and it "
        f"is measured here rather than assumed. AND IT LOCATES THE CARRIER'S "
        f"DEGENERACY ELSEWHERE: whatever kernel the Block 128 analysis found "
        f"is NOT in the link, so it lives in the slice Schur complement -- "
        f"which is exactly the object gate G measures. Asserting a "
        f"rank-deficient bond fails HERE and nowhere else",
        bool(
            len(facts.link_rank) == claims["link_block_count"]
            and all(rank == claims["link_rank"] for rank in facts.link_rank)
            and all(dimension == claims["link_kernel_dimensions"]
                    for dimension in facts.link_kernel_dimensions)
            and facts.link_nnz == claims["link_nnz"]))

    # --- E: the parity theorem and its convention ---------------------------
    checks.check(
        "E-THE-PARITY-THEOREM-EXACT-and-the-WRONG-DUAL-CONTRAST-at-16",
        f"R B_+1 R^-1 = the dt=-1 band of the DUAL-FRAME action EXACTLY, at "
        f"{facts.parity_theorem_residual} nonzero entries, with Q_dual = "
        f"m*H_min_dual[theta g] + i(H_min_dual d_ref + d_ref^H H_min_dual) "
        f"built with d_ref = R d_00 R^-1. THE FORWARD LINK MAPS EXACTLY ONTO "
        f"THE DUAL BACKWARD LINK. AND THE CONVENTION IS LOAD-BEARING, MEASURED "
        f"AGAINST THREE FAILING NEIGHBOURS IN THE SAME RUN: against the WRONG "
        f"dual -- the one built with d_00 in place of the seam identity's own "
        f"d_ref -- the residual is EXACTLY {facts.wrong_dual_residual} "
        f"nonzero entries; against the dt=+1 band of the dual it is "
        f"{facts.wrong_band_residual}; against the dt=-1 band of the ORIGINAL "
        f"frame it is {facts.no_dual_residual}; and the undressed site "
        f"reflection fails at {facts.undressed_residual}. THE 16 IS THE "
        f"SHARPEST OF THEM AND IT IS THIS BLOCK'S OWN INLINE SELF-CATCH: the "
        f"first comparison in the solve used d_00, failed at exactly that "
        f"count, and the seam identity's own differential took the residual to "
        f"zero. Asserting a nonzero theorem residual, or asserting that the "
        f"wrong dual works too, fails HERE and nowhere else",
        bool(
            facts.parity_theorem_residual == claims["parity_theorem_residual"]
            and facts.wrong_dual_residual == claims["wrong_dual_residual"]
            and (facts.wrong_dual_residual != 0) == claims["wrong_dual_contrast"]
            and facts.wrong_band_residual == claims["wrong_band_residual"]
            and facts.no_dual_residual == claims["no_dual_residual"]
            and facts.undressed_residual != 0))

    # --- F: the symbolic ADM split ------------------------------------------
    checks.check(
        "F-THE-ODD-BOND-IS-PURE-SHEAR-and-VANISHES-AT-ZERO-SHEAR",
        f"AT A PER-SLICE SYMBOLIC FIELD (q_t, v_t) CONSTANT IN x, and with the "
        f"shear variable a_t = q_t v_t / (q_t^2 - 1), the odd bond L_1 has "
        f"EXACTLY {facts.odd_bond_nnz} nonzero entries in the symbols "
        f"{facts.odd_bond_symbols}, AND THE WHOLE TABLE IS EXHIBITED AND "
        f"COMPARED ENTRYWISE at {facts.odd_bond_table_residual} disagreements: "
        f"{facts.odd_bond_entry_ratios} as multiples of a_1 -- -3/20 at (0,0) "
        f"and (2,2), +3/20 at (0,2) and (2,0), and m/4 at the four "
        f"mass-coupled positions (0,1), (1,2), (2,3) and (3,0). AND L_1 "
        f"VANISHES IDENTICALLY AT q_1 = 0, at "
        f"{facts.odd_bond_at_zero_shear_nnz} surviving entries. THE ODD BOND "
        f"IS PURE SHEAR TRANSPORT AND THE MASS RIDES ON THE SHEAR: at zero "
        f"shear there is no odd bond at all. This is an identity in the field "
        f"symbols and not a coincidence at the landed field. Asserting that "
        f"the odd bond survives at zero shear fails HERE and nowhere else",
        bool(
            facts.odd_bond_nnz == claims["odd_bond_nnz"]
            and facts.odd_bond_at_zero_shear_nnz
            == claims["odd_bond_at_zero_shear_nnz"]
            and facts.odd_bond_table_residual
            == claims["odd_bond_table_residual"]
            and len(facts.odd_bond_entry_ratios) == claims["odd_bond_nnz"]))
    checks.check(
        "F-THE-EVEN-BOND-SPLITS-8-ODD-4-EVEN-and-THE-MASS-IS-ONLY-IN-THE-ODD",
        f"THE EVEN BOND CARRIES THE SAME SHEAR PATTERN PLUS FOUR MORE ENTRIES. "
        f"L_0 has {facts.even_bond_nnz} nonzero entries, splitting under "
        f"q -> -q into EXACTLY {facts.even_bond_odd_part_nnz} ODD and "
        f"{facts.even_bond_even_part_nnz} EVEN. THE MASS APPEARS ONLY IN THE "
        f"ODD PART: m is in the odd part ({facts.mass_in_odd_part}) and is "
        f"NOT in the even part ({facts.mass_in_even_part}), whose symbols are "
        f"{facts.even_bond_even_symbols} against the odd part's "
        f"{facts.even_bond_odd_symbols}. AND THE SPLIT IS EXHIBITED RATHER "
        f"THAN DESCRIBED: at q_0 = 0 exactly {facts.even_bond_at_zero_shear_nnz}"
        f" entries survive and they ARE the even part, at "
        f"{facts.even_bond_zero_shear_is_even_part} residual. THE ADM "
        f"LAPSE/SHIFT READING OF THIS ALTERNATION IS A READING AND GATE B "
        f"GATES IT AS NOT CLAIMED",
        bool(
            facts.even_bond_nnz == claims["even_bond_nnz"]
            and facts.even_bond_odd_part_nnz
            == claims["even_bond_odd_part_nnz"]
            and facts.even_bond_even_part_nnz
            == claims["even_bond_even_part_nnz"]
            and facts.mass_in_odd_part == claims["mass_in_odd_part"]
            and facts.mass_in_even_part == claims["mass_in_even_part"]
            and facts.even_bond_at_zero_shear_nnz
            == claims["even_bond_at_zero_shear_nnz"]
            and facts.even_bond_zero_shear_is_even_part
            == claims["even_bond_zero_shear_is_even_part"]))
    checks.check(
        "F-THE-EVEN-PART-IN-CLOSED-FORM-and-IT-IS-GENUINELY-SHEAR-DEPENDENT",
        f"THE EVEN PART IS FOUR DIAGONAL ENTRIES AND ONE MAGNITUDE, AND THE "
        f"SOLVE'S 'no q dependence' CLAUSE IS REFUTED BY MEASUREMENT. The "
        f"positions are {facts.even_part_positions} -- THE DIAGONAL, and "
        f"nothing off it -- with signs {facts.even_part_signs}, and every one "
        f"of them equals its sign times the common magnitude "
        f"E = (1/v_0 + v_1 - v_0/(q_0^2 - 1) - v_1/(q_1^2 - 1))/5 at "
        f"{facts.even_part_magnitude_residual} disagreements; measured, "
        f"E = {facts.even_part_magnitude}. E IS EVEN IN THE SHEARS AND IT IS "
        f"NOT FREE OF THEM: its two shear derivatives are "
        f"{facts.even_part_shear_derivatives}, matching "
        f"2 q_t v_t / (5(q_t^2 - 1)^2) at "
        f"{facts.even_part_derivative_residual} disagreements and both "
        f"NONZERO ({facts.even_part_shear_dependent}) -- and they are ODD, "
        f"which is exactly WHY E is even and why the 8/4 parity split above "
        f"survives the correction. AND THE WITNESS CONSTRAINT COLLAPSES IT: "
        f"under q_t^2 + v_t^2 = 1, which the landed field satisfies at every "
        f"cell, E reduces EXACTLY to (v_1 + 1/v_1 + 2/v_0)/5 -- measured "
        f"{facts.pythagorean_reduction} at "
        f"{facts.pythagorean_reduction_residual} disagreements -- so the shear "
        f"dependence is real but is carried by the volumes on the witness "
        f"locus. Asserting that E is shear-independent fails HERE and nowhere "
        f"else",
        bool(
            facts.even_part_positions == claims["even_part_positions"]
            and facts.even_part_signs == claims["even_part_signs"]
            and facts.even_part_magnitude_residual
            == claims["even_part_magnitude_residual"]
            and facts.even_part_shear_dependent
            == claims["even_part_shear_dependent"]
            and facts.even_part_derivative_residual
            == claims["even_part_derivative_residual"]
            and facts.pythagorean_reduction_residual
            == claims["pythagorean_reduction_residual"]))

    # --- G: the pole locus, the quotient, and the twist certificate ---------
    checks.check(
        "G-THE-POLE-LOCUS-four-EVEN-QUARTICS-with-EVERY-COEFFICIENT-POSITIVE",
        f"THE EIGHT INTRA-SLICE DETERMINANTS ARE MEASURED EXACTLY AND THE "
        f"POSITIVITY IS DECIDED AT THE COEFFICIENT LEVEL. Slices t and t+4 "
        f"agree exactly ({facts.slice_det_period_residual} disagreements), so "
        f"the {facts.slice_det_count} determinants are "
        f"{facts.distinct_det_count} distinct ones; each is a polynomial in m "
        f"of degree {facts.det_degrees} with ONLY EVEN POWERS "
        f"({facts.det_odd_coefficients_zero}), carrying "
        f"{facts.det_coefficient_counts} nonzero coefficients, and EVERY ONE "
        f"OF THOSE COEFFICIENTS IS STRICTLY POSITIVE "
        f"({facts.det_all_coefficients_positive}). AN EVEN POLYNOMIAL WITH "
        f"POSITIVE COEFFICIENTS IS STRICTLY POSITIVE AT EVERY REAL m, AND THE "
        f"m = 0 END IS GATED SEPARATELY ({facts.det_zero_mass_all_positive}) "
        f"SO THE MASSLESS POINT IS NOT TAKEN ON FAITH. THEREFORE THE SLICE "
        f"SCHUR FACTORIZATION IS GLOBALLY REGULAR ON THE PHYSICAL MASS AXIS AT "
        f"THIS FRAME'S DECOMPOSITION and the poles sit at m^2 < 0, off the "
        f"physical line. THE SCOPE IS NARROW AND STATED: this discharges the "
        f"#7338 no-pole-free-section warning FOR REAL MASS AT THIS "
        f"DECOMPOSITION ONLY, and says nothing about their metric-coupled "
        f"vertical Schur, which is a different decomposition on different "
        f"fixtures. Asserting a non-positive coefficient fails HERE and "
        f"nowhere else",
        bool(
            facts.slice_det_period_residual
            == claims["slice_det_period_residual"]
            and facts.slice_det_count == claims["slice_det_count"]
            and facts.distinct_det_count == claims["distinct_det_count"]
            and facts.det_degrees == claims["det_degrees"]
            and facts.det_odd_coefficients_zero
            == claims["det_odd_coefficients_zero"]
            and facts.det_coefficient_counts
            == claims["det_coefficient_counts"]
            and facts.det_all_coefficients_positive
            == claims["det_all_coefficients_positive"]
            and facts.det_zero_mass_all_positive
            == claims["det_zero_mass_all_positive"]
            and facts.mass_is_symbolic == claims["mass_is_symbolic"]))
    checks.check(
        "G-THE-QUOTIENT-DESCENT-census-40-36-16-36-and-four-FULL-RANK-bonds",
        f"AND THE BLOCK DESCENDS TO THE PHYSICAL CARRIER. Block 128's LANDED "
        f"antiperiodic quotient psi(t+4) = -psi(t) sends Q_min to a "
        f"{facts.quotient_dimension}-dimensional operator whose band census is "
        f"EXACTLY {facts.quotient_band_census} by time separation mod 4, and "
        f"all four quotient bonds have rank {facts.quotient_bond_rank} with "
        f"nonzero counts {facts.quotient_bond_nnz} -- THE SAME 10/8 "
        f"ALTERNATION AND THE SAME FULL RANK AS THE COVER. The link survives "
        f"the descent, which is what makes the quotient a place the successor "
        f"can be posed. Asserting a different quotient census fails HERE and "
        f"nowhere else",
        bool(
            facts.quotient_dimension == claims["quotient_dimension"]
            and facts.quotient_band_census == claims["quotient_band_census"]
            and all(rank == claims["quotient_bond_rank"]
                    for rank in facts.quotient_bond_rank)
            and len(facts.quotient_bond_rank) == 4
            and facts.quotient_bond_nnz == claims["quotient_bond_nnz"]))
    checks.check(
        "G-THE-TWIST-CERTIFICATE-the-seam-bond-is-MINUS-the-cover-bond-3-to-4",
        f"THE ANTIPERIODIC SEAM SIGN IS A CERTIFICATE AND NO LONGER AN "
        f"EXPECTATION. At the SAME field pair on both sides -- the quotient's "
        f"seam bond, rows of slice 0 against columns of slice 3, against the "
        f"COVER's bond 3 -> 4 -- the SUM is the zero matrix "
        f"({facts.twist_negation_residual} nonzero entries) while the "
        f"DIFFERENCE is not ({facts.twist_identity_residual}), and the "
        f"entrywise ratio is EXACTLY -1 "
        f"({facts.twist_ratios_all_minus_one}) at all "
        f"{len(facts.twist_positions)} common nonzero positions "
        f"{facts.twist_positions}, measured as {facts.twist_ratios}. BOTH "
        f"HALVES ARE ASSERTED so a sign-blind implementation cannot satisfy "
        f"this gate. THE COMPARISON WAS THE SOLVE'S QUEUED CERTIFICATE, IT WAS "
        f"MEASURED BY THE ADVERSARIAL CHECKER, AND WHAT IS GATED HERE IS THE "
        f"CHECKER'S MEASUREMENT. Asserting that the seam bond is not the "
        f"negation fails HERE and nowhere else",
        bool(
            facts.twist_negation_residual == claims["twist_negation_residual"]
            and (facts.twist_identity_residual != 0)
            == claims["twist_is_not_the_identity"]
            and facts.twist_positions == claims["twist_positions"]
            and facts.twist_ratios_all_minus_one
            == claims["twist_ratios_all_minus_one"]))

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
          f"it {authority.parent_ref_and_ancestry}, and BOTH Block 183 "
          f"artifacts are content-bound there and in the worktree "
          f"{authority.parent_artifact_blobs}. THE AUDIT INPUTS: "
          f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} "
          f"readable in the worktree (this block's own note excluded, since it "
          f"lands later and is gate H's), missing {authority.inputs_missing}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {authority.stale_is_real_ancestor} and carries NEITHER Block "
          f"183 artifact {authority.stale_carries_neither_artifact} -- it is "
          f"the Block 182 tip, which PREDATES both artifacts, and that absence "
          f"is exactly what makes the stale_parent_authority mutation bite")
    print(f"  THE MACHINERY: the LANDED Block 128 runner is imported "
          f"{authority.machinery_import_landed} and every object below is "
          f"rebuilt from it and from the Block 105 module it re-exports -- the "
          f"cover is {T_COVER}x{X_EXTENT} at dimension {N_COVER}, the field has "
          f"period {PHYSICAL_T} in t, the landed MASS is {MASS} and every "
          f"completion here is run at SYMBOLIC POSITIVE MASS instead. NOTHING "
          f"from any scratchpad is imported or read")
    print(f"  THE BANNER: {ban['imposed_objects']} imposed objects, "
          f"{ban['registered_objects']} registered and "
          f"{ban['adopted_objects']} adopted; MEASURED os-positivity-claimed "
          f"{ban['os_positivity_claimed']}, two-history-Gram-claimed "
          f"{ban['two_history_gram_claimed']}, gravity-claimed "
          f"{ban['gravity_claimed']}, ADM-reading-claimed "
          f"{ban['adm_reading_claimed']} and frame-uniqueness-claimed "
          f"{ban['frame_uniqueness_claimed']}. The imposed objects are "
          f"{IMPOSED_OBJECTS}")
    print(f"  THE CITATION PINS: {facts.citation_pins} -- the charter read "
          f"from Block 106's PRIMARY BODY and the frame from Block 183's")
    print(f"  THE CONTROLS: the landed-field Hodge control residual is "
          f"{facts.hodge_control_residual}; R R^T - I has "
          f"{facts.reflection_is_orthogonal_residual} entries; the frame "
          f"closes at {facts.frame_closure_residual} and is positive definite "
          f"{facts.frame_positive_definite} by {facts.frame_leading_minors} "
          f"exact leading minors. THE FRAME IS ONE ADMITTED MEMBER OF BLOCK "
          f"183'S SIXTEEN, CHOSEN FOR MINIMALITY, AND NO UNIQUENESS IS CLAIMED")
    print(f"  THE BAND STRUCTURE: Q_min's census is {facts.band_census} at "
          f"{facts.band_total} entries, the dual frame's is "
          f"{facts.dual_band_census} and the Block 181 equal-weight point's is "
          f"{facts.equal_weight_band_census} at "
          f"{facts.equal_weight_versus_minimal_entries} entries away from "
          f"H_min; the link pair carries "
          f"{facts.link_band_entries} entries and the three non-identities are "
          f"{facts.link_non_identities}")
    print(f"  THE TRANSPORTER: the eight per-bond blocks have ranks "
          f"{facts.link_rank}, kernel dimensions "
          f"{facts.link_kernel_dimensions} and nonzero counts "
          f"{facts.link_nnz}. INVERTIBLE AT EVERY BOND")
    print(f"  THE PARITY THEOREM: {facts.parity_theorem_residual} against the "
          f"dual frame's dt=-1 band, with the WRONG-DUAL contrast at "
          f"{facts.wrong_dual_residual}, the wrong band at "
          f"{facts.wrong_band_residual}, the undualized frame at "
          f"{facts.no_dual_residual} and the undressed reflection at "
          f"{facts.undressed_residual}")
    print(f"  THE SYMBOLIC SPLIT: the odd bond has {facts.odd_bond_nnz} "
          f"entries in {facts.odd_bond_symbols}, matching its exhibited "
          f"entrywise table at {facts.odd_bond_table_residual} disagreements "
          f"({facts.odd_bond_entry_ratios} as multiples of "
          f"a_1 = q_1 v_1/(q_1^2 - 1)), and vanishes at zero shear "
          f"({facts.odd_bond_at_zero_shear_nnz}). The even bond has "
          f"{facts.even_bond_nnz} entries splitting "
          f"{facts.even_bond_odd_part_nnz} odd / "
          f"{facts.even_bond_even_part_nnz} even, with m in the odd part "
          f"{facts.mass_in_odd_part} and in the even part "
          f"{facts.mass_in_even_part}; the even part's symbols are "
          f"{facts.even_bond_even_symbols} and at zero shear "
          f"{facts.even_bond_at_zero_shear_nnz} entries survive, identical to "
          f"the even part at {facts.even_bond_zero_shear_is_even_part}")
    print(f"  THE EVEN PART, IN CLOSED FORM AND CORRECTED: positions "
          f"{facts.even_part_positions} with signs {facts.even_part_signs} "
          f"times E = {facts.even_part_magnitude}, at "
          f"{facts.even_part_magnitude_residual} disagreements. IT IS "
          f"GENUINELY SHEAR-DEPENDENT ({facts.even_part_shear_dependent}): the "
          f"derivatives are {facts.even_part_shear_derivatives} at "
          f"{facts.even_part_derivative_residual} disagreements against "
          f"2 q_t v_t/(5(q_t^2 - 1)^2), and both are ODD, which is why E is "
          f"EVEN. Under q_t^2 + v_t^2 = 1 it reduces to "
          f"{facts.pythagorean_reduction} at "
          f"{facts.pythagorean_reduction_residual} disagreements. THE SOLVE'S "
          f"'no q dependence' CLAUSE IS REFUTED AND THE CHECKER'S VERSION IS "
          f"WHAT IS GATED")
    print(f"  THE POLE LOCUS: {facts.slice_det_count} slice determinants with "
          f"{facts.slice_det_period_residual} period-4 disagreements and "
          f"{facts.distinct_det_count} distinct values, degrees "
          f"{facts.det_degrees}, only even powers "
          f"{facts.det_odd_coefficients_zero}, coefficient counts "
          f"{facts.det_coefficient_counts}, ALL COEFFICIENTS POSITIVE "
          f"{facts.det_all_coefficients_positive}, and at m = 0 the values "
          f"{facts.det_zero_mass_values} are all positive "
          f"{facts.det_zero_mass_all_positive}. The four determinants are "
          f"{facts.det_expressions}")
    print(f"  THE QUOTIENT: dimension {facts.quotient_dimension}, census "
          f"{facts.quotient_band_census}, bond ranks "
          f"{facts.quotient_bond_rank} and bond nonzero counts "
          f"{facts.quotient_bond_nnz}")
    print(f"  THE TWIST CERTIFICATE: the quotient seam bond against the cover "
          f"bond 3 -> 4 at the SAME field pair has "
          f"{facts.twist_negation_residual} nonzero entries under ADDITION and "
          f"{facts.twist_identity_residual} under SUBTRACTION, with entrywise "
          f"ratios {facts.twist_ratios} at positions "
          f"{facts.twist_positions} -- all exactly -1 "
          f"({facts.twist_ratios_all_minus_one}). THE SEAM BOND IS MINUS THE "
          f"COVER BOND, EXACTLY. This was the solve's QUEUED certificate; the "
          f"adversarial checker measured it and the checker's measurement is "
          f"what is gated")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False the note has NOT landed at docs/ yet, there is no draft "
          f"fallback anywhere in this runner, gate H is EXPECTED to fail and "
          f"the gate-H mutation is UNTESTABLE until the note lands. Scope keys "
          f"satisfied: {sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  EXACTNESS: every measured object above is exact sympy Rational, "
          f"Integer or Symbol arithmetic; NO FLOAT and NO TOLERANCE enters any "
          f"check, and the mass is a SYMBOL throughout "
          f"({facts.mass_is_symbolic}). ELAPSED {elapsed_ns // 1_000_000} ms")
    print(f"  THE CORPUS RELATION: Blocks 104, 105, 106, 128, 181, 182 and 183 "
          f"STAND EXACTLY AS LANDED and no landed note is edited. What this "
          f"block corrects is ONE OF ITS OWN SOLVE-SIDE CLAUSES, refuted by "
          f"the adversarial check before landing: the even part of the even "
          f"bond is NOT free of the shear. The d_ref convention catch is a "
          f"different thing and is NOT a correction: it happened INSIDE the "
          f"solve, is recorded as PROCESS in N7 of the note, and is gated here "
          f"as the WRONG-DUAL contrast at 16 entries")
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
