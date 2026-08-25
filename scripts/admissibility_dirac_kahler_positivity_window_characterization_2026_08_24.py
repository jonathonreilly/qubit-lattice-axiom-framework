#!/usr/bin/env python3
"""BLOCK 187 -- THE POSITIVITY WINDOW CHARACTERIZED.

THE RESULT, AND ITS EXACT SCOPE.  On BLOCK 185's OWN object -- the seam-glued
action on Block 107's d=2 one-fine-mode staggered carrier at dimension 32, with
the restricted raising set A (the positive half {0,1,2,3} plus the two seam
edge-time pairs {3,4} and {7,0}), the derived P-odd glue D = A - P A P at 72
nonzero entries, the P-even A02-image geometry and the two-history span
Lambda_+ = {0,1} x Z4 -- NOW PARAMETERIZED IN (m, c, v): THE POSITIVITY THAT
BLOCK 185 MEASURED AT A SINGLE FIXTURE IS AN OPEN REGION, ITS TWO SAMPLED EDGES
ARE BRACKETED TO WIDTH 1/2048 AND 1/2560 BY EXACT BISECTION, ITS MASS EDGE ON
THE c = 5/13 RAY IS THE UNIQUE SIMPLE ROOT OF AN EXPLICIT QUARTIC, AND THE
POSITIVITY SURVIVES ONE EXACT STEP OF THE VOLUME DIAL IN EACH DIRECTION.

  0. THE CONTROL COMES FIRST AND IT IS BLOCK 185'S OWN NUMBER (C).  At
     (m, c, v) = (9/20, 5/13, 1) this runner's construction reproduces Block
     185's landed first leading minor
     4465961414671029642827787914210419072833144728317065801107200 over
     8932040001245962023277146780748464953706237777456506835365883
     DIGIT-FOR-DIGIT, with D at exactly 72 nonzero entries and P-odd at zero
     residual.  NOTHING BELOW IS BELIEVABLE IF THIS IS NOT EXACT, BECAUSE
     NOTHING BELOW WOULD THEN BE BLOCK 185'S OBJECT.

  1. THE MASS AXIS (C).  At c = 5/13 all eight leading principal minors are
     strictly positive at EVERY sampled mass from m = 1/10 to m = 5/4 -- seven
     consecutive points spanning more than a decade -- and positivity FAILS at
     m = 3/2 with sign vector (+,+,+,+,+,+,-,-) and at m = 2 with
     (+,+,+,+,+,-,+,-).  FIVE of the nine are gated here and four are cited to
     the adversarial check's findings, which reproduced all nine exactly.

  2. THE MASS BOUNDARY, AND IT IS BRACKETED BY A REPRODUCED BISECTION (D).  An
     exact bisection from (5/4, 3/2), run HERE by the same code, walks the
     checker's recorded midpoint path 11/8, 23/16, 45/32, 91/64, 181/128,
     363/256, 727/512, 1455/1024, 2911/2048 and terminates on
     m* in (2911/2048, 91/64), WIDTH 1/2048, with all eight minors positive at
     the lower endpoint and the sole failure Delta_8 < 0 at the upper.  A tenth
     step refines the lower endpoint to 5823/4096.

  3. THE BOUNDARY THEOREM, WHICH IS THE BLOCK'S NEW MATHEMATICS (D).  Jacobi's
     complementary-minor identity gives Delta_8(m, 5/13) EXACTLY as
     KAPPA * A(m)^2 * B_-(m) * B_+(m) / (F(m)^2 G(m)^2) with
     KAPPA = 3101843146481947279097856 a POSITIVE INTEGER, and A^2 B_- B_+ is
     the REDUCED numerator because gcd(A^2 B_- B_+, F^2 G^2) = 1.  On the
     bracket the exact Sturm
     counts are 0, 0 and 1 for A, B_- and B_+; gcd(B_+, B_+') = 1 and B_+' has
     no root there; A and B_- are strictly negative at both endpoints and have
     no root between them, so A^2 > 0 and B_- < 0 throughout and
     sign(Delta_8) = -sign(B_+).  THEREFORE THE Delta_8 EDGE IS EXACTLY THE
     UNIQUE SIMPLE ROOT OF B_+ IN THE BRACKET.  The window's mass edge is an
     ALGEBRAIC OBJECT, not a bisection artifact.

  4. THE SHEAR AXIS AND THE CORNERS (E).  At m = 9/20 positivity holds through
     c = 3/5 and fails at c = 4/5 (minor 6) and c = 12/13 (minors 6 and 8); an
     exact bisection from (3/5, 4/5) reproduces c* in (1713/2560, 857/1280),
     WIDTH 1/2560, MINOR 7 carrying the shear edge.  AND THE REGION IS NOT A
     PRODUCT: m = 1 is certified positive on the mass ray and c = 3/5 is
     certified positive on the shear ray, YET (1, 3/5) FAILS.  Three further
     corners fail too, and THE FAILING MINOR VARIES -- 8 at the mass edge, 7 at
     the shear edge, 6 at the corner -- so the boundary is a union of
     minor-zero loci and it is CURVED.

  5. THE OPENNESS THEOREM, IN THE CHECK'S CORRECTED FORM AND WITH ITS SCOPE (F).
     The domain is U = {(m,c): c != +/-1 AND det Q(m,c) != 0}.  THE CHART
     CONDITION IS NOT DECORATION: the shear Hodge block carries the factor
     1 - c^2 in the denominators of its (dx,dt) channel, measured here on a
     SYMBOLIC c, and the check's C5 correction is exactly that omitting it
     leaves the domain statement incomplete.  On the mass ray the determinant
     has the compact certificate det Q(m, 5/13) = F(m)^2 G(m)^2 / CONST with
     EVERY coefficient of F and G a POSITIVE INTEGER and both even, so
     det Q > 0 for EVERY REAL m.  With the entries rational on c != +/-1 and
     det Q nonvanishing, every Delta_k is continuous and eight strict
     inequalities at a certified point persist on a neighbourhood: THE POSITIVE
     SET IS OPEN AROUND EACH CERTIFIED POINT.  AND THE SCOPE IS THE CHECK'S OWN:
     A UNION OF LOCAL NEIGHBOURHOODS AND NOTHING MORE -- no connectivity, no
     boundary topology, no interpolation between sampled rays.  Hermiticity is
     STRUCTURAL, not a sample accident: P H P = H and P D P = -D give
     Q^T = P Q P, hence (Q^-1 P)^T = Q^-1 P and the reflected restricted Gram is
     REAL SYMMETRIC wherever it is defined.

  6. THE VOLUME DIAL (G).  At the fixture (m, c) = (9/20, 5/13) the Gram stays
     exactly Hermitian and all eight minors stay strictly positive at v = 4/5
     and at v = 5/4, with both exact determinants reproduced.  THE WINDOW HAS A
     THIRD DIMENSION.  THIS IS TWO-POINT ROBUSTNESS AND NOT A CERTIFIED
     INTERVAL, and it is scoped that way in the banner, in the gate and in the
     note.

WHAT IS NOT CLAIMED, STATED ONCE: NO CONNECTIVITY -- the positive set is a union
of certified local neighbourhoods and nothing here says it is connected or
simply connected; NO GLOBAL BOUNDARY TOPOLOGY -- no boundary component is shown
unique, no two-dimensional boundary curve is produced, and no monotonicity away
from the tested slice is established; NO INTERPOLATION BETWEEN SAMPLED RAYS; NO
VOLUME INTERVAL -- two exact points, not a range; NO CERTIFICATE FOR THE SEVEN
LOWER MINORS STRICTLY INSIDE THE MASS BRACKET -- they are certified positive at
the two endpoints, and the boundary theorem is about Delta_8 alone; and NO
GRAVITY CONSTRAINT QUOTIENT.  ONE CONSTRUCTION, Block 185's, on ONE CARRIER,
Block 107's, on a TWO-SLICE span.  BLOCK 185 IS NOT CORRECTED: every number of
theirs that reappears here reappears unchanged, and this block UPGRADES their
windowed-positivity claim rather than amending it.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 186 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the eight audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: five imposed objects,
     ZERO registered and ZERO adopted, with connectivity, global boundary
     topology, ray interpolation, the volume interval and the lower-minor
     interval all declared NOT CLAIMED as measured constants.
  C  THE MASS AXIS: Block 185's own first minor reproduced digit-for-digit as
     the construction control, then five gated mass points with their exact
     sign vectors and four exact negative witnesses.
  D  THE MASS BOUNDARY AND THE BOUNDARY THEOREM: the ten-step bisection path
     reproduced verdict by verdict, both bracket endpoints with their exact
     Delta_8 values, then the Jacobi factorization, the coprimality that makes
     it the REDUCED numerator, the Sturm counts and the simple-root theorem.
  E  THE SHEAR AXIS AND THE CORNERS: the nine-step shear bisection reproduced,
     both bracket endpoints, two gated corners with their exact witnesses, the
     NON-PRODUCT theorem at (1, 3/5), and the varying failing-minor index.
  F  THE OPENNESS THEOREM: the 1 - c^2 chart factor measured symbolically, the
     det certificate verified at 33 nodes with every F and G coefficient a
     positive integer, det Q measured nonzero at every certified sample, and
     the structural Hermiticity chain measured at zero residual.
  G  THE VOLUME DIAL: Hermiticity, the all-positive sign vector and the exact
     determinant at v = 4/5 and v = 5/4, with the v = 1 no-op control.
  H  the note at its final path and the N5 fence, byte-identical.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: fourteen declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_connectivity, claim_volume_interval
    C  break_mass_vector
    D  break_bracket_endpoint, break_jacobi_factorization, break_sturm_counts
    E  break_shear_vector, break_corner
    F  break_det_certificate
    G  break_volume_dial
    H  drop_n5_fence
  TWO OF THE FOURTEEN GUARD THE CHECK'S OWN CORRECTIONS: claim_connectivity
  asserts the positive set connected, which the strictly-local openness theorem
  does not supply, and claim_volume_interval asserts a certified volume range,
  which two points do not supply.  BOTH MUST FAIL.
  BEFORE LANDING GATE H ALREADY FAILS AT BASELINE, on note-at-final-path alone,
  so drop_n5_fence cannot flip it and THE SWEEP IS RUN AT LANDING, once the note
  sits at docs/ and the baseline is 8 of 8 by family.

RUNNING
  python3 scripts/admissibility_dirac_kahler_positivity_window_characterization_2026_08_24.py
  python3 ... --list-mutations
  python3 ... --mutation break_jacobi_factorization

NOTES FOR THE LANDING AGENT
  1. NOTHING from any scratchpad is imported OR READ.  THE CONSTRUCTION IS
     BLOCK 185'S, REBUILT HERE from its displayed equations and parameterized in
     (m, c, v): the staggered kernel with its antiperiodic edge sign, the grade
     projectors, the raising part d_K, the site reflection, the offset
     permutation P_4, the restricted raising set A, the derived D and the glued
     action are ALL BUILT DIRECTLY HERE.  The LANDED Block 128 runner is
     imported for EXACTLY TWO objects -- cover_embedding() and the Block 105
     module's shear_hodge() -- and for nothing else.  Gate C's first check is
     the proof that the rebuild IS Block 185's object.
  2. EVERY CHECK IS EXACT.  sympy Rational and Integer arithmetic only; no float
     enters any measured object and no tolerance is used anywhere.  Positivity
     is decided by exact leading principal minors and the boundary theorem by
     exact Sturm sequences, never by an eigenvalue estimate or a root isolation
     in floating point.
  3. THE b186 nsimplify HAZARD CARRIES OVER AND THIS RUNNER NSIMPLIFIES
     NOTHING.  nsimplify carries a rational TOLERANCE and maps a small nonzero
     rational to EXACTLY ZERO -- nsimplify(Rational(1, 10**200)) is 0 -- so a
     coefficient passed through it can silently lose its sign.  Block 186 hit
     exactly that in draft, where an nsimplified coefficient vector reported a
     false inertia at m = 10.  BLOCK 185 DID call it on its shears; here every
     mass, shear and volume is ALREADY an exact sympy Rational, so nothing needs
     converting and NOTHING IS CONVERTED.  The absence is MEASURED, not
     promised: gate F counts the occurrences of the call in this file's own
     source and requires zero.
  4. The N5 fence appears byte-identically in the note; gate H checks it as a
     raw substring.
  5. PARENT_COMMIT is the Block 186 tip and PARENT_REF resolves to it; nothing
     needs sed, and CURRENT_MAIN was carried forward from the Block 185 runner
     and re-resolved at draft time.
  6. The stale pin is the Block 185 tip, a real ancestor of HEAD that predates
     Block 186 and carries NEITHER Block 186 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  7. THE ADVERSARIAL CHECK PRECEDED THIS DRAFT AND IS FOLDED FROM THE FIRST
     LINE.  Its verdict was CONFIRMED-WITH-CORRECTION.  It confirmed C1-C4 and
     C6 exactly with its own independent bisections; its C5 correction -- the
     chart domain c != +/-1, and the strictly LOCAL scope of the openness
     conclusion -- is gated in family F and declared in family B; and its C7 was
     UPGRADED from the requested finite diagnostic to the exact simple-root
     theorem that family D now measures.  NO PLACEHOLDER SLOT REMAINS.
  8. ONE PROCESS NOTE, AND IT IS NOT A LANDED CORRECTION: the solve's spec
     for the boundary-order diagnostic named 1456/1024 as a point beyond the
     upper endpoint, and 1456/1024 IS 91/64.  The checker caught the
     spec arithmetic, evaluated the point as asked and added 2913/2048 as a
     genuinely further one.  Nothing wrong left the solve; it is recorded as
     process in N7 of the note.
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
# Block 185 imported and no others: cover_embedding(), whose corner order IS the
# form basis (1, dx, dt, dx^dt), and the Block 105 module it re-exports, from
# which shear_hodge() is read.  Everything else is built directly here.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 186 is the commit this block's branch
# is cut from, and its note and its runner are the pair that distinguishes the
# parent pin from the stale pin: both exist at PARENT_COMMIT and NEITHER exists
# at STALE_PARENT_COMMIT.
BLOCK186_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SECTION_FRAME_INERTIA_WALL_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK186_RUNNER = (
    "scripts/admissibility_dirac_kahler_section_frame_inertia_wall_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK186_NOTE, BLOCK186_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "b32143ff6ff633ddf105c62d5b2aa546792fc7ff",   # Block 186 note
    "11bf84d97161eafaf73b3370b6f143c11b5fa043",   # Block 186 runner
)
# THE CONSTRUCTION AUTHORITY.  This block's object IS Block 185's object, and
# the window it characterizes is Block 185's window; their note is the primary
# body every convention and the open item are read from, and their runner is the
# code this one parameterizes.  They are ALSO the stale pin's tell.
BLOCK185_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_OS_SEAM_GLUED_GRAM_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK185_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py"
)
# THE CARRIER AUTHORITY, two blocks up: Block 107's own note.
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVITY_WINDOW_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SECTION_FRAME_INERTIA_WALL_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_section_frame_inertia_wall_2026_08_24.py",
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
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 185 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 186 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block186-"
              "section-frame-inertia-wall-20260824")
PARENT_COMMIT = "f5bcab65286f03001c8d3b88ad0904afa92588a8"
# The Block 185 tip: a real ancestor of HEAD that predates Block 186 and
# therefore carries NEITHER Block 186 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "4d411820f1c19b4130db8ab064a79ba8e86f0fc8"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_connectivity",
    "claim_volume_interval",
    "break_mass_vector",
    "break_bracket_endpoint",
    "break_jacobi_factorization",
    "break_sturm_counts",
    "break_shear_vector",
    "break_corner",
    "break_det_certificate",
    "break_volume_dial",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_connectivity": "B",
    "claim_volume_interval": "B",
    "break_mass_vector": "C",
    "break_bracket_endpoint": "D",
    "break_jacobi_factorization": "D",
    "break_sturm_counts": "D",
    "break_shear_vector": "E",
    "break_corner": "E",
    "break_det_certificate": "F",
    "break_volume_dial": "G",
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
        # THE STALE LEG.  At the Block 185 tip NEITHER Block 186 artifact
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
    "BLOCK 185's SEAM-GLUED OBJECT, REBUILT HERE from its displayed equations and imported from nothing: Block 107's d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32 with eta_t = 1 and eta_x = (-1)^t, the antiperiodic kernel carrying the far-seam edge sign omega_-(3) = -1, the grade-raising part d_K, the link-centered site reflection theta(t) = -1-t, the restricted raising set A (both endpoint times in the positive half {0,1,2,3} PLUS every entry on the two seam edge-time pairs {3,4} and {7,0}), the derived glue D = A - P A P at 72 nonzero entries, the P-even A02-image geometry at the UNSIGNED offset permutation P_4 and the anchor reflection theta_A(t) = -2-t, the completion convention Q = m*H + H*D - D^T*H, the two-history span Lambda_+ = {0,1} x Z4 and the dressing K_ab = conj(G(b, theta a))",
    "THE PARAMETER CHART, WHICH IS THIS BLOCK'S OWN OBJECT: the same construction as a function of THREE exact rationals -- the mass m, the shear c of the constant-in-x reflection-odd step history (c,c,c,0,-c,-c,-c,0), and the Hodge volume v -- with the TWO ZERO-SHEAR SEAM ANCHORS HELD EXACTLY FLAT as identity blocks, which is the adversarial check's own volume-dial construction and which is a MEASURED NO-OP at v = 1 because the landed shear Hodge at zero shear and unit volume IS the identity",
    "THE SAMPLED SET, taken exactly as the solve and the adversarial check displayed it: nine mass-axis points at c = 5/13 from m = 1/10 to m = 2, seven shear-axis points at m = 9/20 from c = 1/5 to c = 12/13, the two certified bracket endpoint pairs (2911/2048, 91/64) and (1713/2560, 857/1280) with the tenth-step refinement 5823/4096, four corner points, and two volume points v = 4/5 and v = 5/4 at the fixture",
    "THE BOUNDARY AND DETERMINANT POLYNOMIALS the adversarial check supplied and this runner RE-DERIVES rather than accepts: A, B_- and B_+ of the Jacobi factorization of Delta_8(m, 5/13), and F, G with the positive integer constant of the determinant certificate det Q(m, 5/13) = F^2 G^2 / CONST",
    "Block 128's LANDED cover_embedding(), whose corner order IS the form basis (1, dx, dt, dx^dt), and the LANDED Block 105 shear_hodge() block it re-exports: THE ONLY TWO OBJECTS IMPORTED BY THIS RUNNER",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS rather than prose, so
# the B mutations bite on an object.  ALL SIX ARE FALSE AND STAY FALSE.  THE
# OPENNESS IS LOCAL: what is established is a union of open neighbourhoods
# around ten certified points, and the region's topology is OPEN in the other
# sense of the word.
CONNECTIVITY_CLAIMED = False
GLOBAL_BOUNDARY_CLAIMED = False
RAY_INTERPOLATION_CLAIMED = False
VOLUME_INTERVAL_CLAIMED = False
LOWER_MINOR_INTERVAL_CLAIMED = False
CONSTRAINT_QUOTIENT_CLAIMED = False

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
TIME_EXTENT = 8
SPACE_EXTENT = 4
COVER_SIZE = TIME_EXTENT * SPACE_EXTENT
MINOR_COUNT = 8
GLUE_NONZEROS = 72
POSITIVE_SIGNS = (1,) * MINOR_COUNT

# THE FIXTURE, which is Block 185's, and THE CONSTRUCTION CONTROL, which is
# their landed first leading minor.  If this number moves, the rebuild is not
# their object and nothing else in this runner means anything.
FIXTURE_MASS = sp.Rational(9, 20)
FIXTURE_SHEAR = sp.Rational(5, 13)
UNIT_VOLUME = sp.Integer(1)
B185_FIRST_MINOR = sp.Rational(
    4465961414671029642827787914210419072833144728317065801107200,
    8932040001245962023277146780748464953706237777456506835365883)

# --- C: THE MASS AXIS, all nine points at c = 5/13 -------------------------
# FIVE are gated by direct measurement; FOUR are cited to the adversarial
# check's findings, which reproduced all nine exactly.  The declared table is
# whole, and the gate says which half it measured.
MASS_AXIS_TABLE = (
    (sp.Rational(1, 10), POSITIVE_SIGNS),
    (sp.Rational(1, 4), POSITIVE_SIGNS),
    (sp.Rational(1, 2), POSITIVE_SIGNS),
    (sp.Rational(3, 5), POSITIVE_SIGNS),
    (sp.Rational(3, 4), POSITIVE_SIGNS),
    (sp.Integer(1), POSITIVE_SIGNS),
    (sp.Rational(5, 4), POSITIVE_SIGNS),
    (sp.Rational(3, 2), (1, 1, 1, 1, 1, 1, -1, -1)),
    (sp.Integer(2), (1, 1, 1, 1, 1, -1, 1, -1)),
)
GATED_MASSES = (sp.Rational(1, 10), sp.Rational(3, 4), sp.Rational(5, 4),
                sp.Rational(3, 2), sp.Integer(2))
CITED_MASSES = (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 5),
                sp.Integer(1))
# THE EXACT NEGATIVE WITNESSES at the two failing gated masses.
DELTA7_AT_THREE_HALVES = sp.Rational(
    -85090229607948729741077107375715753305308272511435659763853597380350349476000039722071097344,
    572960703002653892616167087132755201440169903286762517538700877485657326861128751234870798641374881953125)
DELTA8_AT_THREE_HALVES = sp.Rational(
    -55772685855493751416316702326098115089246386029464592895668226720213343145035865283100672,
    409257645001895637582976490809110858171549930919116083956214912489755233472234822310621999029553487109375)
DELTA6_AT_TWO = sp.Rational(
    -7890231431818882674506063844880003094539586885471536889006112939561800730299477520607415894016,
    74808265874164739714380358730715033870378392220195408647397035293098882634606911082408149805703352125625)
DELTA8_AT_TWO = sp.Rational(
    -17019757780754929852868756247925151195438833387164842763181606680344607789806367277056,
    1526699303554382443150619565932959874905681473881538951987694597818344543563406348620574485830680655625)

# --- D: THE MASS BOUNDARY --------------------------------------------------
MASS_BRACKET_LOW = sp.Rational(2911, 2048)
MASS_BRACKET_HIGH = sp.Rational(91, 64)
MASS_BRACKET_WIDTH = sp.Rational(1, 2048)
MASS_REFINEMENT = sp.Rational(5823, 4096)
MASS_REFINED_WIDTH = sp.Rational(1, 4096)
MASS_BRACKET_HIGH_SIGNS = (1, 1, 1, 1, 1, 1, 1, -1)
DELTA8_AT_BRACKET_LOW = sp.Rational(
    230206563854760436250197653699817592100084132897488822107268894580294758247343047226593939845567274569110442267330144379860729848130383064702436218183609600844961064121532416,
    84470375364379888995202153499838462070278151522745679063471845246921889331880757846172893203515459824707205603166476717922183719525452599555585553650911039370150092009488934961683571931475625)
DELTA8_AT_BRACKET_HIGH = sp.Rational(
    -5272182110724018653744537162235884463195365879031413689821274893357388084196927319941971203859717239968536932744192831013257216,
    2852223386432627766189972804014619353218871437883392803720351552108660577540036605807029903777051262643970139899408284331218980830571655192305625)
# THE ADVERSARIAL CHECK'S OWN BISECTION PATH, from (5/4, 3/2), reproduced HERE
# verdict by verdict rather than cited.  True means all eight minors positive.
MASS_BISECTION_START = (sp.Rational(5, 4), sp.Rational(3, 2))
MASS_BISECTION_PATH = (
    (sp.Rational(11, 8), True),
    (sp.Rational(23, 16), False),
    (sp.Rational(45, 32), True),
    (sp.Rational(91, 64), False),
    (sp.Rational(181, 128), True),
    (sp.Rational(363, 256), True),
    (sp.Rational(727, 512), True),
    (sp.Rational(1455, 1024), True),
    (sp.Rational(2911, 2048), True),
    (sp.Rational(5823, 4096), True),
)
# THE BOUNDARY THEOREM'S POLYNOMIALS, verbatim from the adversarial check.
MASS_SYMBOL = sp.Symbol("m")
JACOBI_A = (2338702173616900 * MASS_SYMBOL**4
            + 5559167172136500 * MASS_SYMBOL**2
            - 34342504390877071)
JACOBI_B_MINUS = (584675543404225 * MASS_SYMBOL**4
                  - 119232179199250 * MASS_SYMBOL**3
                  - 808327810625400 * MASS_SYMBOL**2
                  - 7890304777814160 * MASS_SYMBOL
                  - 12314765055708144)
JACOBI_B_PLUS = (584675543404225 * MASS_SYMBOL**4
                 + 119232179199250 * MASS_SYMBOL**3
                 - 808327810625400 * MASS_SYMBOL**2
                 + 7890304777814160 * MASS_SYMBOL
                 - 12314765055708144)
# THE TWO CONSTANTS OF THE FACTORIZATION, AND THEY ARE DIFFERENT THINGS.
# JACOBI_QUOTIENT is the POSITIVE RATIONAL relating the raw complementary
# determinant to A^2 B_- B_+; JACOBI_KAPPA is that quotient TIMES the
# determinant certificate's constant, and it is the POSITIVE INTEGER in the
# reduced statement Delta_8(m, 5/13) = KAPPA * A^2 B_- B_+ / (F^2 G^2).
JACOBI_QUOTIENT = sp.Rational(
    1, 7286174197556964924654123391513289072415645283434426863405063938768896)
JACOBI_KAPPA = sp.Integer(3101843146481947279097856)
STURM_COUNTS = (0, 0, 1)
B_PLUS_PRIME_AT_LOW = sp.Rational(27984065518306879605205855, 2147483648)
B_PLUS_PRIME_AT_HIGH = sp.Rational(854440470872410964035, 65536)
# (A, B_-, B_+) at (low, high), in that order.  A and B_- are STRICTLY NEGATIVE
# at both endpoints and have NO root between them, so A^2 > 0 and B_- < 0
# throughout the bracket -- which is what turns the sign of Delta_8 into
# -sign(B_+) and makes the crossing B_+'s and nobody else's.
BRACKET_ENDPOINT_SIGNS = (-1, -1, -1, -1, -1, 1)

# --- E: THE SHEAR AXIS AND THE CORNERS -------------------------------------
SHEAR_AXIS_TABLE = (
    (sp.Rational(1, 5), POSITIVE_SIGNS),
    (sp.Rational(5, 13), POSITIVE_SIGNS),
    (sp.Rational(3, 5), POSITIVE_SIGNS),
    (sp.Rational(4, 5), (1, 1, 1, 1, 1, -1, 1, 1)),
    (sp.Rational(12, 13), (1, 1, 1, 1, 1, -1, 1, -1)),
    (sp.Rational(1713, 2560), POSITIVE_SIGNS),
    (sp.Rational(857, 1280), (1, 1, 1, 1, 1, 1, -1, 1)),
)
SHEAR_BRACKET_LOW = sp.Rational(1713, 2560)
SHEAR_BRACKET_HIGH = sp.Rational(857, 1280)
SHEAR_BRACKET_WIDTH = sp.Rational(1, 2560)
SHEAR_BISECTION_START = (sp.Rational(3, 5), sp.Rational(4, 5))
SHEAR_BISECTION_PATH = (
    (sp.Rational(7, 10), False),
    (sp.Rational(13, 20), True),
    (sp.Rational(27, 40), False),
    (sp.Rational(53, 80), True),
    (sp.Rational(107, 160), True),
    (sp.Rational(43, 64), False),
    (sp.Rational(429, 640), False),
    (sp.Rational(857, 1280), False),
    (sp.Rational(1713, 2560), True),
)
DELTA7_AT_SHEAR_BRACKET_HIGH = sp.Rational(
    -1598335222229188848331260139735713538793899586253898956125746360485779772825747609028331825177344729361412327257340956309228330917907048340418019474895782167589382115192894752389697512350270857779922509240329882828800000000000000000000,
    938014989242101233823150045262719995750420024879135748599481531431561317455090902457356073907424738459952665704930454884410309281827235552082034266431218759293162023117376658900999782141305020863400544754905318555013844105305274634098782326361)
CORNER_TABLE = (
    ((sp.Integer(1), sp.Rational(3, 5)), (1, 1, 1, 1, 1, -1, 1, -1)),
    ((sp.Rational(5, 4), sp.Rational(1, 2)), (1, 1, 1, 1, 1, -1, 1, -1)),
    ((sp.Rational(3, 4), sp.Rational(7, 10)), (1, 1, 1, 1, 1, -1, 1, -1)),
    ((sp.Rational(1, 10), sp.Rational(4, 5)), (1, 1, 1, 1, 1, 1, -1, 1)),
)
GATED_CORNERS = ((sp.Integer(1), sp.Rational(3, 5)),
                 (sp.Rational(1, 10), sp.Rational(4, 5)))
DELTA6_AT_FIRST_CORNER = sp.Rational(
    -52523939070044168716349889558763976641355807318191909636161929216,
    212374950530520124008053860398992737861223502117607259903904181168570081)
DELTA7_AT_SECOND_CORNER = sp.Rational(
    -196702296481530945521867791523795742855834960937500000,
    13689881409230243144704927919478627765962998376429743510081)
# THE FAILING-MINOR INDEX, MEASURED, AND IT MOVES ALONG THE BOUNDARY.
FAILING_MINOR_AT_MASS_EDGE = 8
FAILING_MINOR_AT_SHEAR_EDGE = 7
FAILING_MINOR_AT_FIRST_CORNER = 6

# --- F: THE OPENNESS THEOREM ------------------------------------------------
DET_F = (299684727885699454242816 * MASS_SYMBOL**8
         + 1057546650417160380713856 * MASS_SYMBOL**6
         + 1122356975550987673041509 * MASS_SYMBOL**4
         + 334202761189083845162330 * MASS_SYMBOL**2
         + 29915998462435025408400)
DET_G = (1198738911542797816971264 * MASS_SYMBOL**8
         + 8357584267546985416158720 * MASS_SYMBOL**6
         + 20746825460109491061517732 * MASS_SYMBOL**4
         + 21542427261169485079330180 * MASS_SYMBOL**2
         + 7964480716014734889397129)
DET_CONST = sp.Integer(
    22600569498765673425646382617815399421526202244979382923541986986760398250842873973826153086976)
DET_DEGREE = 32
DET_NODE_COUNT = DET_DEGREE + 1
JACOBI_DEGREE_BOUND = 24
# THE THREE EXACT SHEAR-RAY DETERMINANTS the adversarial check displayed, which
# put the three positive shear samples in U by direct computation rather than by
# the mass-ray certificate.
SHEAR_DETERMINANTS = (
    (sp.Rational(1, 5), sp.Rational(
        13994953333167282846091214369164655514347086607283313719491888103245641918756214364756250082102023321,
        219116140165888394222918920571924360929171991805137640992957634969600000000000000000000000000000000)),
    (sp.Rational(5, 13), sp.Rational(
        434365065623226699761613827521957114917610720141816981156959893930988465451681393063174107141165203868793090542441059790529,
        2392141431138299698729697223684503486672742367036209644060651639608672273328387649857126400000000000000000000000000000000)),
    (sp.Rational(3, 5), sp.Rational(
        167938844184906124102413290784793690729579402712204844409919318025080177141229818816121520485796681,
        41137613933030151053874229563933762624568396640839496583715225600000000000000000000000000000000)),
)
# THE CHART FACTOR.  The shear Hodge block's (dx,dt) channel carries 1 - c^2 in
# its denominators, which is the adversarial check's C5 domain correction.
CHART_DENOMINATOR_COUNT = 4
SHEAR_SYMBOL = sp.Symbol("c")

# --- G: THE VOLUME DIAL -----------------------------------------------------
VOLUME_POINTS = (sp.Rational(4, 5), sp.Rational(5, 4))
VOLUME_DETERMINANTS = (
    (sp.Rational(4, 5), sp.Rational(
        14285683622601745390541541674222107411696366222829746178449192238334978522465535938425917614099281941616564421865203844009,
        737135490150174131639534407302747872319099360863783485440000000000000000000000000000000000000000000000000000000000000000)),
    (sp.Rational(5, 4), sp.Rational(
        11077683380864810137902501827970746581828643680934720491721644679599099108149160314066197906131262502661377365732525669243126486878365712105363339819840586280769,
        2630187318821282114327219793844976408897894482189862110474316654737414566893413894283944181897782886400000000000000000000000000000000000000000000000000000000)),
)

# THE CITATION PINS, read from the PRIMARY BODIES so the open item this block
# closes, the bracket it sharpens, the firewall that made the whole line
# admissible and the hazard it inherits all have a measured referent.
B185_WINDOW_PIN = "THE WINDOW'S CHARACTERIZATION IS OPEN"
B185_BRACKET_PIN = "(9/20, 2]"
B107_NOT_A_NOGO_PIN = "This is not a curved OS no-go."
B186_NSIMPLIFY_PIN = "nsimplify IS NOT APPLIED TO ANY MEASURED SCALAR"

# THE H-FAMILY SCOPE KEYS.  The set is required WHOLE by gate H, which is what
# gives drop_n5_fence its teeth.
SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# nsimplify carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO -- nsimplify(Rational(1, 10**200)) is 0 -- so a coefficient or a
# minor passed through it can silently lose its sign, which is precisely how a
# positivity verdict would be manufactured.  Block 185 called it on its shears
# as a float guard; here every mass, shear and volume is ALREADY an exact sympy
# Rational, so nothing needs converting and nothing is converted.  Gate F counts
# the occurrences of the call in this file's own source and requires ZERO.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls nsimplify."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


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


def first_failing_minor(signs: tuple) -> int:
    """THE INDEX OF THE FIRST NON-POSITIVE LEADING MINOR, 1-based, or 0 when all
    eight are positive.  IT IS THE BOUNDARY'S LOCAL IDENTITY: which minor
    vanishes says which sheet of the boundary a point is next to, and it MOVES
    -- 8 at the mass edge, 7 at the shear edge, 6 at the corner."""
    for index, value in enumerate(signs, start=1):
        if value <= 0:
            return index
    return 0


def is_exact_real(value: object) -> bool:
    expression = sp.sympify(value)
    return bool(expression.is_rational and not expression.is_Float)


# ---------------------------------------------------------------------------
# BLOCK 185's OBJECT, BUILT DIRECTLY AND PARAMETERIZED IN (m, c, v)
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
LAMBDA_PLUS = tuple((t, x) for t in (0, 1) for x in range(SPACE_EXTENT))


def site_index(time_coordinate: int, space_coordinate: int) -> int:
    """idx(t,x) = (t mod 8)*4 + (x mod 4): time first, exactly Block 107's
    ordering, and identical to the LANDED Block 128 cover_index."""
    return ((time_coordinate % TIME_EXTENT) * SPACE_EXTENT
            + space_coordinate % SPACE_EXTENT)


def staggered_kernel(antiperiodic: bool = True) -> sp.Matrix:
    """BLOCK 107 EQUATION (3), BUILT DIRECTLY.  eta_t = 1 and eta_x = (-1)^t;
    the temporal edge sign is -1 at t = 3 -- the FAR reflection seam -- and +1
    everywhere else."""
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


def site_reflection() -> sp.Matrix:
    """P e_(t,x) = e_(theta(t),x) with theta(t) = -1-t mod 8."""
    matrix = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        for space in range(SPACE_EXTENT):
            matrix[site_index((-1 - time) % TIME_EXTENT, space),
                   site_index(time, space)] = 1
    return matrix


def shear_block(shear: object, volume: object) -> sp.Matrix:
    """The LANDED Block 105 shear Hodge, read through Block 128, at an EXACT
    rational shear and an EXACT rational volume.  NO nsimplify: both arguments
    are already sympy Rationals or Integers, which is what Block 185's
    nsimplify guard existed to guarantee and what this runner guarantees by
    construction instead."""
    return b128.block105.shear_hodge(shear, volume)


def step_history(shear: object) -> tuple:
    """BLOCK 107 EQUATION (19): the reflection-odd step, with the two straddling
    anchors t = 3 and t = 7 FLAT by antisymmetry rather than by prescription."""
    return (shear, shear, shear, sp.Integer(0),
            -shear, -shear, -shear, sp.Integer(0))


def anchor_block(local_shear: object, volume: object) -> sp.Matrix:
    """THE PARAMETERIZED CELL BLOCK, AND ITS ONE DECLARED CONVENTION.  At a
    ZERO-SHEAR anchor the block is the EXACT IDENTITY, which is the adversarial
    check's own volume-dial construction: the two straddling seam anchors are
    flat by antisymmetry, and the volume dial turns at the SHEARED anchors only.
    AT v = 1 THE CONVENTION IS A MEASURED NO-OP, because the landed shear Hodge
    at zero shear and unit volume IS the identity -- gate G measures both that
    and the fact that at v != 1 it is NOT, so the choice is disclosed and never
    silent."""
    if local_shear == 0:
        return sp.eye(SPACE_EXTENT)
    return shear_block(local_shear, volume)


def image_hodge(shear: object, volume: object) -> sp.Matrix:
    """BLOCK 107 EQUATION (20) with their equation (27) A02-image half: the
    POSITIVE times carry their own anchor blocks and the NEGATIVE times carry
    P_4 B(theta_A(t), x) P_4^T at the anchor reflection theta_A(t) = -2-t."""
    history = step_history(shear)
    result = sp.zeros(COVER_SIZE, COVER_SIZE)
    for time in range(TIME_EXTENT):
        if time in POSITIVE_TIMES:
            block = anchor_block(history[time], volume)
        else:
            reflected = (-2 - time) % TIME_EXTENT
            block = sp.expand(
                OFFSET_PERMUTATION * anchor_block(history[reflected], volume)
                * OFFSET_PERMUTATION.T)
        for space in range(SPACE_EXTENT):
            embedding = b128.cover_embedding(time, space)
            result += embedding * block * embedding.T / 4
    return sp.expand(result)


def restricted_raising(raising: sp.Matrix, seams: tuple) -> sp.Matrix:
    """A: the d_K entries with BOTH endpoint times in the positive half, PLUS
    every d_K entry on each supplied seam edge-time pair."""
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


def completion(hodge: sp.Matrix, glue: sp.Matrix, mass: object) -> sp.Matrix:
    """BLOCK 107 EQUATION (21): Q = m*H + H*D - D^T*H, used unchanged at every
    (m, c, v) below, so no comparison here is between different conventions."""
    return sp.expand(mass * hodge + hodge * glue - glue.T * hodge)


REFLECTION_OF = {anchor: site_index((-1 - anchor[0]) % TIME_EXTENT, anchor[1])
                 for anchor in LAMBDA_PLUS}
SPAN_INDICES = tuple(site_index(*anchor) for anchor in LAMBDA_PLUS)
REFLECTED_INDICES = tuple(REFLECTION_OF[anchor] for anchor in LAMBDA_PLUS)


def two_history_gram(action: sp.Matrix) -> sp.Matrix:
    """BLOCK 107 EQUATION (7)/(22): K_ab = conj(G(b, theta a)) on Lambda_+."""
    inverse = action.inv()
    gram = sp.zeros(len(LAMBDA_PLUS), len(LAMBDA_PLUS))
    for row, anchor in enumerate(LAMBDA_PLUS):
        for column, partner in enumerate(LAMBDA_PLUS):
            gram[row, column] = sp.conjugate(
                inverse[site_index(*partner), REFLECTION_OF[anchor]])
    return sp.expand(gram)


def hermiticity_defect(gram: sp.Matrix) -> object:
    """BLOCK 107 EQUATION (22): delta = ||K - K^dagger||_max, exactly."""
    return max_norm(gram - gram.H)


@dataclass(frozen=True)
class Sample:
    """ONE POINT OF THE CHART, rebuilt by the SAME code: its exact determinant,
    its Hermiticity defect, its eight leading minors, its sign vector and the
    index of the first minor that fails."""
    mass: object
    shear: object
    volume: object
    determinant: object
    delta: object
    real_symmetric: bool
    minors: tuple
    signs: tuple
    first_failure: int

    @property
    def positive(self) -> bool:
        return self.signs == POSITIVE_SIGNS


def build_sample(mass: object, shear: object, glue: sp.Matrix,
                 volume: object = UNIT_VOLUME) -> Sample:
    hodge = image_hodge(shear, volume)
    action = completion(hodge, glue, mass)
    determinant = action.det(method="berkowitz")
    gram = two_history_gram(action)
    minors = leading_minors(gram)
    signs = minor_signs(minors)
    real_symmetric = bool(
        residual_count(gram - gram.T) == 0
        and all(sp.im(value) == 0 for value in gram))
    return Sample(mass, shear, volume, determinant, hermiticity_defect(gram),
                  real_symmetric, minors, signs, first_failing_minor(signs))


def bisect(low: object, high: object, steps: int, positive_at) -> tuple:
    """EXACT BISECTION ON THE RATIONALS, no float and no tolerance: `low` is a
    certified-positive endpoint and `high` a certified-failing one, and each
    step halves the interval at the exact rational midpoint.  Returns the walked
    path as ((midpoint, positive?), ...) together with the bracket standing
    AFTER EACH STEP, so the certified bracket and its refinement are both read
    off the same walk rather than asserted."""
    path = []
    brackets = []
    for _ in range(steps):
        midpoint = (low + high) / 2
        verdict = positive_at(midpoint)
        path.append((midpoint, verdict))
        if verdict:
            low = midpoint
        else:
            high = midpoint
        brackets.append((low, high))
    return tuple(path), tuple(brackets)


# ---------------------------------------------------------------------------
# THE POLYNOMIAL MACHINERY, EXACT AND WITH ITS DEGREE ARGUMENT STATED
# ---------------------------------------------------------------------------
def interpolate_exact(nodes: tuple, values: tuple, symbol: sp.Symbol) -> sp.Poly:
    """EXACT LAGRANGE INTERPOLATION over the rationals.  With d+1 distinct nodes
    it recovers ANY polynomial of degree at most d uniquely, which is why the
    node count below is the degree bound plus one and why extra nodes are then
    checked: agreement at more than d+1 points is a proof, not a spot check."""
    return sp.Poly(sp.interpolate(list(zip(nodes, values)), symbol), symbol)


def submatrix_determinant(hodge: sp.Matrix, glue: sp.Matrix, mass: object,
                          rows: tuple = None, cols: tuple = None) -> object:
    action = completion(hodge, glue, mass)
    if rows is not None:
        action = action[list(rows), list(cols)]
    return action.det(method="berkowitz")


def sturm_count(polynomial, low: object, high: object) -> int:
    """THE EXACT NUMBER OF REAL ROOTS IN [low, high] by Sturm's theorem over the
    rationals.  No root isolation in floating point occurs anywhere."""
    return sp.count_roots(polynomial, low, high)


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
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 185's SEAM-GLUED OBJECT rebuilt here from its displayed equations (Block 107's d=2 one-fine-mode staggered carrier on Z8_t x Z4_x at dimension 32, the antiperiodic kernel carrying omega_-(3) = -1 on the FAR seam, the grade-raising d_K, the link-centered reflection theta(t) = -1-t, the restricted raising set A of the positive half {0,1,2,3} plus the seam edge-time pairs {3,4} and {7,0}, the derived glue D = A - P A P at 72 nonzero entries, the P-even A02-image geometry at the UNSIGNED P_4, the completion Q = m*H + H*D - D^T*H and the span Lambda_+ = {0,1} x Z4), THE PARAMETER CHART (m, c, v) WHICH IS THIS BLOCK'S OWN OBJECT with the two zero-shear seam anchors held EXACTLY FLAT as identity blocks -- the adversarial check's own volume-dial construction, a MEASURED NO-OP at v = 1 -- THE SAMPLED SET of nine mass points at c = 5/13, seven shear points at m = 9/20, the two certified bracket endpoint pairs, four corners and two volume points, THE BOUNDARY AND DETERMINANT POLYNOMIALS A, B_-, B_+, F and G which are RE-DERIVED here and not accepted, and the LANDED Block 128 cover_embedding() and Block 105 shear_hodge() -- THE ONLY TWO OBJECTS IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO CONNECTIVITY OF THE POSITIVE SET IS CLAIMED; NO GLOBAL BOUNDARY TOPOLOGY IS CLAIMED, no boundary component being shown unique and no two-dimensional boundary curve being produced; NO INTERPOLATION BETWEEN SAMPLED RAYS IS CLAIMED; NO VOLUME INTERVAL IS CLAIMED, two exact points not being a range; NO CERTIFICATE IS CLAIMED FOR THE SEVEN LOWER MINORS STRICTLY INSIDE THE MASS BRACKET, the boundary theorem being about Delta_8 alone; AND NO GRAVITY CONSTRAINT QUOTIENT IS FORMED. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE CONTROL COMES FIRST AND IT IS BLOCK 185'S OWN NUMBER. At (m, c, v) = (9/20, 5/13, 1) this runner's construction reproduces THEIR LANDED FIRST LEADING MINOR 4465961414671029642827787914210419072833144728317065801107200/8932040001245962023277146780748464953706237777456506835365883 DIGIT-FOR-DIGIT, with the glue D at EXACTLY 72 nonzero entries and P-odd at zero residual and the two-history Gram exactly Hermitian and positive 8 of 8. THAT IDENTITY IS THE WHOLE LICENCE FOR CALLING WHAT FOLLOWS A CHARACTERIZATION OF THEIR WINDOW: if it moved by a digit, this would be a different object and every statement below would be about a different region. AND THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: nsimplify carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so a minor passed through it can silently lose its sign; this runner calls it ZERO TIMES, counted in its own source by gate F, because every mass, shear and volume here is already an exact sympy Rational.\nper_mode: THE MASS AXIS, AND THE WINDOW IS NOT A KNIFE EDGE. At c = 5/13 all EIGHT leading principal minors are STRICTLY POSITIVE at every sampled mass from m = 1/10 to m = 5/4 -- SEVEN CONSECUTIVE POINTS SPANNING MORE THAN A DECADE -- and positivity FAILS at m = 3/2 with sign vector (+,+,+,+,+,+,-,-) and at m = 2 with (+,+,+,+,+,-,+,-). FIVE of the nine are gated by direct measurement here and FOUR are cited to the adversarial check, which reproduced all nine exactly. THE SHEAR AXIS IS THE SAME SHAPE: at m = 9/20 positivity holds through c = 3/5 and fails at c = 4/5 on minor 6 and at c = 12/13 on minors 6 and 8. THE FIXTURE BLOCK 185 MEASURED SITS WELL INTERIOR TO THIS REGION IN BOTH DIRECTIONS.\nper_block: THE TWO EDGES ARE BRACKETED BY EXACT BISECTIONS REPRODUCED VERDICT BY VERDICT. In the mass direction, bisection from (5/4, 3/2) walks 11/8, 23/16, 45/32, 91/64, 181/128, 363/256, 727/512, 1455/1024, 2911/2048 and terminates on m* in (2911/2048, 91/64) at WIDTH 1/2048, all eight minors positive at the lower endpoint and the SOLE failure Delta_8 < 0 at the upper; a tenth step refines the lower endpoint to 5823/4096 at width 1/4096. In the shear direction, bisection from (3/5, 4/5) walks 7/10, 13/20, 27/40, 53/80, 107/160, 43/64, 429/640, 857/1280 and terminates on c* in (1713/2560, 857/1280) at WIDTH 1/2560, with MINOR 7 carrying the shear edge. THE SUPERVISOR'S BISECTION AND THE ADVERSARIAL CHECK'S WERE RUN ON INDEPENDENT RECONSTRUCTIONS AND LAND ON THE SAME TWO BRACKETS, and this runner walks the recorded paths again as a third pass.\nlattice_wide: THE BOUNDARY THEOREM, WHICH IS THIS BLOCK'S NEW MATHEMATICS AND WHICH THE ADVERSARIAL CHECK SUPPLIED BY UPGRADING ITS OWN ASSIGNMENT. Jacobi's complementary-minor identity gives Delta_8(m, 5/13) EXACTLY as KAPPA * A(m)^2 * B_-(m) * B_+(m) / (F(m)^2 * G(m)^2) with KAPPA = 3101843146481947279097856 a POSITIVE INTEGER, where A(m) = 2338702173616900 m^4 + 5559167172136500 m^2 - 34342504390877071, B_-(m) = 584675543404225 m^4 - 119232179199250 m^3 - 808327810625400 m^2 - 7890304777814160 m - 12314765055708144 and B_+(m) = 584675543404225 m^4 + 119232179199250 m^3 - 808327810625400 m^2 + 7890304777814160 m - 12314765055708144; A^2 B_- B_+ is the REDUCED numerator because gcd(A^2 B_- B_+, F^2 G^2) = 1. On the bracket the exact STURM COUNTS are 0, 0 and 1 for A, B_- and B_+; gcd(B_+, B_+') = 1 and B_+' has NO root there and is positive at both endpoints; A and B_- are strictly negative at both endpoints and have no root between them, so A^2 > 0 and B_- < 0 throughout and sign(Delta_8) = -sign(B_+). THEREFORE THE Delta_8 EDGE IS EXACTLY THE UNIQUE SIMPLE ROOT OF B_+ IN THE BRACKET. THE WINDOW'S MASS EDGE IS AN ALGEBRAIC OBJECT AND NOT A BISECTION ARTIFACT.\nper_scope: THE REGION'S SHAPE, ITS OPENNESS AND THE EXACT LIMITS OF BOTH. THE POSITIVE SET IS NOT A PRODUCT: m = 1 is certified positive on the mass ray and c = 3/5 is certified positive on the shear ray, YET (1, 3/5) FAILS at sign vector (+,+,+,+,+,-,+,-); three further corners (5/4, 1/2), (3/4, 7/10) and (1/10, 4/5) fail too. AND THE FAILING MINOR MOVES ALONG THE BOUNDARY -- 8 at the mass edge, 7 at the shear edge, 6 at the corner -- so the boundary is a UNION OF MINOR-ZERO LOCI and it is CURVED, trading mass against shear. THE OPENNESS THEOREM, IN THE ADVERSARIAL CHECK'S CORRECTED FORM: on U = {(m,c): c != +/-1 AND det Q(m,c) != 0} every entry of H and Q is rational, hence continuous, so on U the inverse is continuous and each Delta_k is continuous, and eight strict inequalities at a certified point persist on a neighbourhood. THE CHART CONDITION c != +/-1 IS THE CHECK'S OWN C5 CORRECTION AND IT IS NOT DECORATION: the shear Hodge block carries 1 - c^2 in the denominators of its (dx,dt) channel, measured here on a SYMBOLIC c. On the mass ray det Q(m, 5/13) = F(m)^2 G(m)^2 / CONST with EVERY coefficient of F and G a POSITIVE INTEGER and both even, so det Q > 0 FOR EVERY REAL m. HERMITICITY IS STRUCTURAL AND NOT A SAMPLE ACCIDENT: P H P = H and P D P = -D give Q^T = P Q P, hence (Q^-1 P)^T = Q^-1 P and the reflected restricted Gram is REAL SYMMETRIC WHEREVER DEFINED. AND THE SCOPE IS THE CHECK'S OWN, VERBATIM IN SUBSTANCE: WHAT IS ESTABLISHED is a UNION OF OPEN POSITIVE NEIGHBOURHOODS around the certified points, the exact one-dimensional sign samples and brackets, and the non-product witnesses; WHAT IS NOT ESTABLISHED is connectivity or simple connectivity of the positive set, uniqueness of a boundary component, monotonicity away from the tested slice, an exact two-dimensional boundary curve, or interpolation between sampled rays. THE VOLUME DIAL ADDS A THIRD DIMENSION AND NOT AN INTERVAL: at (9/20, 5/13) the Gram is exactly Hermitian and positive 8 of 8 at v = 4/5 and at v = 5/4, which is TWO-POINT ROBUSTNESS and is scoped that way everywhere.\nRESULT: THE POSITIVITY WINDOW IS AN OPEN REGION WITH CERTIFIED BRACKETS, AN EXACT-ALGEBRAIC MASS EDGE AND A SURVIVING VOLUME DIRECTION. Block 185's landed first minor is reproduced digit-for-digit as the construction control; the mass axis is positive 8 of 8 at seven consecutive points from 1/10 to 5/4 and fails at 3/2 and 2; the mass edge is bracketed in (2911/2048, 91/64) at width 1/2048 and refined to (5823/4096, 91/64); the shear edge is bracketed in (1713/2560, 857/1280) at width 1/2560; Delta_8(m, 5/13) factors as a positive integer times A^2 B_- B_+ over F^2 G^2 with the numerator REDUCED, the Sturm counts on the bracket are (0, 0, 1) and gcd(B_+, B_+') = 1, so THE MASS EDGE IS THE UNIQUE SIMPLE ROOT OF B_+; det Q(m, 5/13) = F^2 G^2 / CONST with every coefficient of F and G a positive integer, so det Q never vanishes on the real mass ray and the positive set is OPEN AROUND EVERY CERTIFIED POINT; four corners fail, the failing minor moving 8 to 7 to 6, so the region is NOT A PRODUCT and its boundary is CURVED; and positivity survives one exact volume step in each direction. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-186 STAND EXACTLY AS LANDED; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. BLOCK 185 IS UPGRADED AND NOT CORRECTED: their windowed-positivity claim stands, and what this block adds is that the window is ROOMY, that its sampled edges are BRACKETED, that its mass edge on the c = 5/13 ray is EXACT-ALGEBRAIC and that its volume direction is ROBUST at two points. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: THE OPENNESS IS STRICTLY LOCAL and no connectivity, no boundary topology and no interpolation between rays follows from it; TWO SAMPLED RAYS and four corners are not a two-dimensional boundary curve; THE BOUNDARY THEOREM IS ONE EDGE OF ONE RAY and says nothing about the shear edge or about the seven lower minors strictly inside the mass bracket, which are certified at the two endpoints only; THE VOLUME EVIDENCE IS TWO POINTS AND NOT AN INTERVAL; it is ONE CONSTRUCTION on ONE CARRIER on a TWO-SLICE span, and no port to the Blocks 181-186 section frame and no gravity constraint quotient is claimed. NO CORRECTION IS LANDED BY THIS BLOCK. ONE PROCESS NOTE IS RECORDED AND IT IS NOT A CORRECTION: the solve's spec for the boundary-order diagnostic named 1456/1024 as a point BEYOND the upper endpoint, and 1456/1024 IS 91/64; the adversarial check caught the spec arithmetic, evaluated the point as asked and added 2913/2048 as a genuinely further one, and nothing wrong ever left the solve. THE ADVERSARIAL CHECK PRECEDED THIS DRAFT AND ITS VERDICTS ARE FOLDED FROM THE FIRST LINE RATHER THAN APPENDED: CONFIRMED-WITH-CORRECTION, with C1-C4 and C6 confirmed exactly on independent bisections, C5 corrected to carry the chart domain c != +/-1 and scoped strictly local, and C7 UPGRADED from the requested finite diagnostic to the exact simple-root theorem. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE POSITIVITY WINDOW CHARACTERIZED anchor, as corrected and upgraded by the b187 adversarial check.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
        "connectivity_claimed": CONNECTIVITY_CLAIMED,
        "global_boundary_claimed": GLOBAL_BOUNDARY_CLAIMED,
        "ray_interpolation_claimed": RAY_INTERPOLATION_CLAIMED,
        "volume_interval_claimed": VOLUME_INTERVAL_CLAIMED,
        "lower_minor_interval_claimed": LOWER_MINOR_INTERVAL_CLAIMED,
        "constraint_quotient_claimed": CONSTRAINT_QUOTIENT_CLAIMED,
        # C -- the construction control and the mass axis.
        "citation_pins": True,
        "glue_nonzeros": GLUE_NONZEROS,
        "glue_p_odd_residual": ZERO_RESIDUAL,
        "b185_first_minor": B185_FIRST_MINOR,
        "fixture_signs": POSITIVE_SIGNS,
        "mass_axis_signs": tuple(
            signs for mass, signs in MASS_AXIS_TABLE if mass in GATED_MASSES),
        "delta7_at_three_halves": DELTA7_AT_THREE_HALVES,
        "delta8_at_three_halves": DELTA8_AT_THREE_HALVES,
        "delta6_at_two": DELTA6_AT_TWO,
        "delta8_at_two": DELTA8_AT_TWO,
        # D -- the mass boundary and the boundary theorem.
        "mass_bisection_path": MASS_BISECTION_PATH,
        "mass_bracket": (MASS_BRACKET_LOW, MASS_BRACKET_HIGH),
        "mass_refined_bracket": (MASS_REFINEMENT, MASS_BRACKET_HIGH),
        "mass_bracket_low_signs": POSITIVE_SIGNS,
        "mass_bracket_high_signs": MASS_BRACKET_HIGH_SIGNS,
        "delta8_at_bracket_low": DELTA8_AT_BRACKET_LOW,
        "delta8_at_bracket_high": DELTA8_AT_BRACKET_HIGH,
        "jacobi_quotient": JACOBI_QUOTIENT,
        "jacobi_kappa": JACOBI_KAPPA,
        # THE FACTORIZATION ITSELF, carried as a POLYNOMIAL claim so the
        # mutation rewrites the mathematics and not a label.
        "jacobi_target": sp.expand(
            JACOBI_A**2 * JACOBI_B_MINUS * JACOBI_B_PLUS),
        "jacobi_numerator_reduced": True,
        "sturm_counts": STURM_COUNTS,
        "b_plus_squarefree": True,
        "b_plus_prime_at_low": B_PLUS_PRIME_AT_LOW,
        "b_plus_prime_at_high": B_PLUS_PRIME_AT_HIGH,
        "bracket_endpoint_signs": BRACKET_ENDPOINT_SIGNS,
        # E -- the shear axis and the corners.
        "shear_bisection_path": SHEAR_BISECTION_PATH,
        "shear_bracket": (SHEAR_BRACKET_LOW, SHEAR_BRACKET_HIGH),
        "shear_bracket_low_signs": POSITIVE_SIGNS,
        "shear_bracket_high_signs": (1, 1, 1, 1, 1, 1, -1, 1),
        "delta7_at_shear_bracket_high": DELTA7_AT_SHEAR_BRACKET_HIGH,
        "corner_signs": tuple(
            signs for corner, signs in CORNER_TABLE if corner in GATED_CORNERS),
        "delta6_at_first_corner": DELTA6_AT_FIRST_CORNER,
        "delta7_at_second_corner": DELTA7_AT_SECOND_CORNER,
        "not_a_product": True,
        "failing_minor_walk": (FAILING_MINOR_AT_MASS_EDGE,
                               FAILING_MINOR_AT_SHEAR_EDGE,
                               FAILING_MINOR_AT_FIRST_CORNER),
        # F -- the openness theorem.
        "chart_denominator_count": CHART_DENOMINATOR_COUNT,
        "chart_factor_is_one_minus_c_squared": True,
        # THE CERTIFICATE ITSELF, carried as its two polynomials and its
        # constant, so the mutation rewrites the certificate and not a label.
        "det_target": (DET_F, DET_G, DET_CONST),
        "det_coefficients_all_positive": True,
        "det_polynomials_even": True,
        "det_has_no_real_root": True,
        "shear_determinants": tuple(value for _, value in SHEAR_DETERMINANTS),
        "hodge_p_even_residual": ZERO_RESIDUAL,
        "glue_p_odd_residual_f": ZERO_RESIDUAL,
        "transpose_covariance_residual": ZERO_RESIDUAL,
        "inverse_p_symmetric_residual": ZERO_RESIDUAL,
        "all_grams_real_symmetric": True,
        "nsimplify_calls": 0,
        # G -- the volume dial.
        "volume_signs": (POSITIVE_SIGNS, POSITIVE_SIGNS),
        "volume_determinants": tuple(value for _, value in VOLUME_DETERMINANTS),
        "volume_deltas": (sp.Integer(0), sp.Integer(0)),
        "unit_volume_convention_is_noop": True,
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
    elif mutation == "claim_connectivity":
        # THE OPENNESS OVERSOLD, AND THIS IS THE BLOCK'S SINGLE BIGGEST
        # OVERREACH RISK.  "An open region" reads as ONE region unless the
        # banner says otherwise.  What is established is a UNION OF LOCAL
        # NEIGHBOURHOODS around ten certified points; that they are connected --
        # let alone simply connected -- is exactly what the adversarial check's
        # C5 said is NOT established, and asserting it fails here.
        claims["connectivity_claimed"] = True
    elif mutation == "claim_volume_interval":
        # THE THIRD DIMENSION OVERSOLD: a certified volume INTERVAL asserted,
        # which two exact points do not supply.  Positivity at v = 4/5 and
        # v = 5/4 says nothing whatever about v between or beyond them.
        claims["volume_interval_claimed"] = True
    elif mutation == "break_mass_vector":
        # THE MASS AXIS DENIED AT ITS FIRST FAILURE: positivity asserted at
        # m = 3/2, which the measured (+,+,+,+,+,+,-,-) forbids.  Without this
        # the seven positive points read as a ray rather than as a window.
        claims["mass_axis_signs"] = tuple(
            POSITIVE_SIGNS if mass == sp.Rational(3, 2) else signs
            for mass, signs in MASS_AXIS_TABLE if mass in GATED_MASSES)
    elif mutation == "break_bracket_endpoint":
        # THE BRACKET DISSOLVED: the upper endpoint asserted positive, which the
        # measured Delta_8 < 0 forbids.  A bracket with two positive endpoints
        # certifies nothing at all.
        claims["mass_bracket_high_signs"] = POSITIVE_SIGNS
    elif mutation == "break_jacobi_factorization":
        # THE THEOREM'S FACTORIZATION DENIED: the numerator asserted to be
        # A^2 B_- ALONE, dropping B_+ -- which is the factor that carries the
        # edge.  The measured quotient is then not a constant at all, so the
        # "up to a positive rational" clause has nothing to stand on.
        claims["jacobi_target"] = sp.expand(JACOBI_A**2 * JACOBI_B_MINUS)
    elif mutation == "break_sturm_counts":
        # THE ROOT COUNT DENIED: TWO roots of B_+ asserted in the bracket, which
        # the exact Sturm sequence forbids.  With two roots the edge is not a
        # single simple crossing and the theorem says nothing.
        claims["sturm_counts"] = (0, 0, 2)
    elif mutation == "break_shear_vector":
        # THE SHEAR EDGE DENIED: the upper shear endpoint asserted positive,
        # which the measured negative seventh minor forbids.
        claims["shear_bracket_high_signs"] = POSITIVE_SIGNS
    elif mutation == "break_corner":
        # THE NON-PRODUCT WITNESS DENIED: (1, 3/5) asserted positive, which the
        # measured (+,+,+,+,+,-,+,-) forbids.  Without this corner the two
        # certified rays read as a rectangle, and they are not one.
        claims["corner_signs"] = tuple(
            POSITIVE_SIGNS if corner == (sp.Integer(1), sp.Rational(3, 5))
            else signs
            for corner, signs in CORNER_TABLE if corner in GATED_CORNERS)
    elif mutation == "break_det_certificate":
        # THE OPENNESS CERTIFICATE MOVED: a different F coefficient asserted,
        # which the exact polynomial identity at 33 nodes forbids.  If F moves,
        # det Q is a different polynomial and the nonvanishing that promotes a
        # sample to a neighbourhood is no longer certified.
        claims["det_target"] = (DET_F + 1, DET_G, DET_CONST)
    elif mutation == "break_volume_dial":
        # THE THIRD DIMENSION DENIED: positivity asserted to FAIL at v = 5/4,
        # which the measured all-positive sign vector forbids.  It is the
        # mutation that stops the volume evidence from being quietly dropped.
        claims["volume_signs"] = (POSITIVE_SIGNS, (1, 1, 1, 1, 1, -1, 1, -1))
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
    # C -- the construction control and the mass axis
    raising_nonzeros: int
    restricted_nonzeros: int
    glue_nonzeros: int
    glue_p_odd_residual: int
    fixture: Sample
    mass_axis_signs: tuple
    mass_axis_deltas: tuple
    delta7_at_three_halves: object
    delta8_at_three_halves: object
    delta6_at_two: object
    delta8_at_two: object
    # D -- the mass boundary and the boundary theorem
    mass_bisection_path: tuple
    mass_bracket: tuple
    mass_refined_bracket: tuple
    mass_bracket_low_signs: tuple
    mass_bracket_high_signs: tuple
    delta8_at_bracket_low: object
    delta8_at_bracket_high: object
    jacobi_numerator: object
    jacobi_degree: int
    jacobi_extra_nodes_agree: bool
    jacobi_identity_points: tuple
    jacobi_numerator_reduced: bool
    sturm_counts: tuple
    b_plus_squarefree: bool
    b_plus_prime_roots_in_bracket: int
    b_plus_prime_at_low: object
    b_plus_prime_at_high: object
    bracket_endpoint_signs: tuple
    # E -- the shear axis and the corners
    shear_bisection_path: tuple
    shear_bracket: tuple
    shear_bracket_low_signs: tuple
    shear_bracket_high_signs: tuple
    delta7_at_shear_bracket_high: object
    corner_signs: tuple
    corner_deltas: tuple
    delta6_at_first_corner: object
    delta7_at_second_corner: object
    not_a_product: bool
    failing_minor_walk: tuple
    # F -- the openness theorem
    chart_denominator_count: int
    chart_factor_is_one_minus_c_squared: bool
    det_nodes: tuple
    det_values: tuple
    det_polynomials_even: bool
    det_coefficients_all_positive: bool
    det_real_root_counts: tuple
    shear_determinants: tuple
    hodge_p_even_residual: int
    transpose_covariance_residual: int
    inverse_p_symmetric_residual: int
    all_grams_real_symmetric: bool
    all_grams_hermitian: bool
    nsimplify_calls: int
    # G -- the volume dial
    volume_signs: tuple
    volume_determinants: tuple
    volume_deltas: tuple
    zero_shear_unit_volume_is_identity: bool
    zero_shear_dialled_is_identity: bool
    exactness_holds: bool


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    # --- BLOCK 185's OBJECT, rebuilt -----------------------------------------
    kernel = staggered_kernel()
    raising = raising_part(kernel)
    reflection = site_reflection()
    restricted = restricted_raising(raising, BOTH_SEAMS)
    glue = sp.expand(restricted - reflection * restricted * reflection)
    glue_p_odd_residual = residual_count(reflection * glue * reflection + glue)

    cache: dict = {}

    def sample(mass, shear, volume=UNIT_VOLUME) -> Sample:
        key = (mass, shear, volume)
        if key not in cache:
            cache[key] = build_sample(mass, shear, glue, volume)
        return cache[key]

    # --- C: the construction control and the mass axis ----------------------
    fixture = sample(FIXTURE_MASS, FIXTURE_SHEAR)
    mass_samples = tuple(sample(mass, FIXTURE_SHEAR) for mass in GATED_MASSES)
    three_halves = sample(sp.Rational(3, 2), FIXTURE_SHEAR)
    two = sample(sp.Integer(2), FIXTURE_SHEAR)

    # --- D: the mass boundary ------------------------------------------------
    def mass_positive(value) -> bool:
        return sample(value, FIXTURE_SHEAR).positive

    mass_path, mass_brackets = bisect(
        MASS_BISECTION_START[0], MASS_BISECTION_START[1],
        len(MASS_BISECTION_PATH), mass_positive)
    # The NINTH step's bracket is the certified one and the TENTH refines it;
    # both are read off the same walk rather than asserted.
    mass_bracket = mass_brackets[8]
    mass_refined = mass_brackets[9]
    bracket_low = sample(MASS_BRACKET_LOW, FIXTURE_SHEAR)
    bracket_high = sample(MASS_BRACKET_HIGH, FIXTURE_SHEAR)

    # --- D: THE BOUNDARY THEOREM --------------------------------------------
    # Jacobi's complementary-minor identity: det of the 8x8 block of Q^-1 on
    # (span, reflected span) equals, up to sign, the determinant of the
    # COMPLEMENTARY 24x24 block of Q divided by det Q.  The complementary
    # determinant is a polynomial in m of degree at most 24, so it is recovered
    # EXACTLY by interpolation at 25 nodes -- and then checked at four more,
    # which is a proof rather than a spot check.  The identity itself is then
    # verified against the DIRECT Gram route at seven exact masses.
    ray_hodge = image_hodge(FIXTURE_SHEAR, UNIT_VOLUME)
    complement_rows = tuple(
        i for i in range(COVER_SIZE) if i not in REFLECTED_INDICES)
    complement_cols = tuple(
        i for i in range(COVER_SIZE) if i not in SPAN_INDICES)
    jacobi_nodes = tuple(
        sp.Integer(k) for k in range(-(JACOBI_DEGREE_BOUND // 2),
                                     JACOBI_DEGREE_BOUND // 2 + 1))
    jacobi_values = tuple(
        submatrix_determinant(ray_hodge, glue, node,
                              complement_rows, complement_cols)
        for node in jacobi_nodes)
    jacobi_numerator = interpolate_exact(jacobi_nodes, jacobi_values,
                                         MASS_SYMBOL)
    extra_nodes = (sp.Rational(7, 3), sp.Rational(-11, 5), sp.Integer(101),
                   sp.Rational(-3, 7))
    jacobi_extra_nodes_agree = all(
        jacobi_numerator.eval(node)
        == submatrix_determinant(ray_hodge, glue, node,
                                 complement_rows, complement_cols)
        for node in extra_nodes)
    identity_masses = GATED_MASSES + (MASS_BRACKET_LOW, MASS_BRACKET_HIGH)
    jacobi_identity_points = tuple(
        sample(mass, FIXTURE_SHEAR).minors[-1]
        * sample(mass, FIXTURE_SHEAR).determinant
        == jacobi_numerator.eval(mass)
        for mass in identity_masses)
    numerator_target = sp.expand(JACOBI_A**2 * JACOBI_B_MINUS * JACOBI_B_PLUS)
    denominator_target = sp.expand(DET_F**2 * DET_G**2)
    jacobi_numerator_reduced = sp.gcd(numerator_target, denominator_target) == 1
    sturm_counts = tuple(
        sturm_count(polynomial, MASS_BRACKET_LOW, MASS_BRACKET_HIGH)
        for polynomial in (JACOBI_A, JACOBI_B_MINUS, JACOBI_B_PLUS))
    b_plus_prime = sp.diff(JACOBI_B_PLUS, MASS_SYMBOL)
    b_plus_squarefree = sp.gcd(JACOBI_B_PLUS, b_plus_prime) == 1
    bracket_endpoint_signs = tuple(
        int(sp.sign(polynomial.subs(MASS_SYMBOL, endpoint)))
        for polynomial in (JACOBI_A, JACOBI_B_MINUS, JACOBI_B_PLUS)
        for endpoint in (MASS_BRACKET_LOW, MASS_BRACKET_HIGH))

    # --- E: the shear axis and the corners ----------------------------------
    def shear_positive(value) -> bool:
        return sample(FIXTURE_MASS, value).positive

    shear_path, shear_brackets = bisect(
        SHEAR_BISECTION_START[0], SHEAR_BISECTION_START[1],
        len(SHEAR_BISECTION_PATH), shear_positive)
    shear_bracket = shear_brackets[-1]
    shear_low = sample(FIXTURE_MASS, SHEAR_BRACKET_LOW)
    shear_high = sample(FIXTURE_MASS, SHEAR_BRACKET_HIGH)
    corners = tuple(sample(mass, shear) for mass, shear in GATED_CORNERS)
    # THE NON-PRODUCT WITNESS.  m = 1 is certified positive on the mass ray at
    # c = 5/13 and c = 3/5 is certified positive on the shear ray at m = 9/20,
    # and BOTH are measured here rather than recalled -- yet the pair (1, 3/5)
    # FAILS.  The positive set is therefore NOT the Cartesian product of the two
    # certified ray intervals.  Nothing about the intervening boundary follows.
    mass_leg = sample(sp.Integer(1), FIXTURE_SHEAR)
    shear_leg = sample(FIXTURE_MASS, sp.Rational(3, 5))
    first_corner = sample(*GATED_CORNERS[0])
    not_a_product = bool(
        mass_leg.positive and shear_leg.positive and not first_corner.positive)
    failing_minor_walk = (bracket_high.first_failure, shear_high.first_failure,
                          first_corner.first_failure)

    # --- F: the openness theorem --------------------------------------------
    # THE CHART FACTOR, measured on a SYMBOLIC shear: the (dx,dt) channel of the
    # landed shear Hodge carries 1 - c^2 in its denominators, which is exactly
    # the adversarial check's C5 domain correction.
    symbolic_block = shear_block(SHEAR_SYMBOL, UNIT_VOLUME)
    chart_denominators = []
    for row in range(SPACE_EXTENT):
        for column in range(SPACE_EXTENT):
            _, denominator = sp.fraction(sp.cancel(symbolic_block[row, column]))
            if denominator != 1:
                chart_denominators.append(sp.expand(denominator))
    chart_factor_ok = bool(chart_denominators) and all(
        sp.cancel(denominator / (SHEAR_SYMBOL**2 - 1)).is_Rational
        and sp.cancel(denominator / (SHEAR_SYMBOL**2 - 1)) != 0
        for denominator in chart_denominators)
    # THE DETERMINANT CERTIFICATE.  det(m*H + C) has degree at most 32, and so
    # does F^2 G^2 / CONST; agreement at 33 DISTINCT nodes is therefore a
    # POLYNOMIAL IDENTITY and not a sample.
    det_nodes = tuple(sp.Integer(k) for k in range(-(DET_DEGREE // 2),
                                                   DET_DEGREE // 2 + 1))
    det_values = tuple(submatrix_determinant(ray_hodge, glue, node)
                       for node in det_nodes)
    f_poly = sp.Poly(DET_F, MASS_SYMBOL)
    g_poly = sp.Poly(DET_G, MASS_SYMBOL)
    det_coefficients_all_positive = all(
        coefficient > 0 and coefficient.is_Integer
        for polynomial in (f_poly, g_poly)
        for coefficient in polynomial.all_coeffs() if coefficient != 0)
    det_polynomials_even = all(
        sp.expand(polynomial.subs(MASS_SYMBOL, -MASS_SYMBOL) - polynomial) == 0
        for polynomial in (DET_F, DET_G))
    det_real_root_counts = (sp.count_roots(DET_F), sp.count_roots(DET_G))
    shear_determinants = tuple(
        sample(FIXTURE_MASS, shear).determinant
        for shear, _ in SHEAR_DETERMINANTS)
    # THE STRUCTURAL HERMITICITY CHAIN, measured at the fixture.
    fixture_action = completion(ray_hodge, glue, FIXTURE_MASS)
    fixture_inverse = fixture_action.inv()
    hodge_p_even_residual = residual_count(
        reflection * ray_hodge * reflection - ray_hodge)
    transpose_covariance_residual = residual_count(
        reflection * fixture_action * reflection - fixture_action.T)
    inverse_p_symmetric = sp.expand(fixture_inverse * reflection)
    inverse_p_symmetric_residual = residual_count(
        inverse_p_symmetric.T - inverse_p_symmetric)

    # --- G: the volume dial --------------------------------------------------
    volume_samples = tuple(
        sample(FIXTURE_MASS, FIXTURE_SHEAR, volume) for volume in VOLUME_POINTS)
    zero_shear_unit = shear_block(sp.Integer(0), UNIT_VOLUME) == sp.eye(
        SPACE_EXTENT)
    zero_shear_dialled = shear_block(
        sp.Integer(0), VOLUME_POINTS[0]) == sp.eye(SPACE_EXTENT)

    every_sample = tuple(cache.values())
    citation_pins = {
        "b185_window_open": B185_WINDOW_PIN in landed_text(BLOCK185_NOTE),
        "b185_mass_bracket": B185_BRACKET_PIN in landed_text(BLOCK185_NOTE),
        "b107_not_a_nogo": B107_NOT_A_NOGO_PIN in landed_text(BLOCK107_NOTE),
        "b186_nsimplify": B186_NSIMPLIFY_PIN in landed_text(BLOCK186_RUNNER),
    }
    banners = {
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "objects_registered": bool(REGISTERED_OBJECTS or ADOPTED_OBJECTS),
        "connectivity_claimed": CONNECTIVITY_CLAIMED,
        "global_boundary_claimed": GLOBAL_BOUNDARY_CLAIMED,
        "ray_interpolation_claimed": RAY_INTERPOLATION_CLAIMED,
        "volume_interval_claimed": VOLUME_INTERVAL_CLAIMED,
        "lower_minor_interval_claimed": LOWER_MINOR_INTERVAL_CLAIMED,
        "constraint_quotient_claimed": CONSTRAINT_QUOTIENT_CLAIMED,
    }
    exact_scalars = (
        tuple(value for item in every_sample for value in item.minors)
        + tuple(item.determinant for item in every_sample)
        + tuple(item.delta for item in every_sample)
        + det_values + jacobi_values)
    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        raising_nonzeros=nonzero_entries(raising),
        restricted_nonzeros=nonzero_entries(restricted),
        glue_nonzeros=nonzero_entries(glue),
        glue_p_odd_residual=glue_p_odd_residual,
        fixture=fixture,
        mass_axis_signs=tuple(item.signs for item in mass_samples),
        mass_axis_deltas=tuple(item.delta for item in mass_samples),
        delta7_at_three_halves=three_halves.minors[6],
        delta8_at_three_halves=three_halves.minors[7],
        delta6_at_two=two.minors[5],
        delta8_at_two=two.minors[7],
        mass_bisection_path=mass_path,
        mass_bracket=mass_bracket,
        mass_refined_bracket=mass_refined,
        mass_bracket_low_signs=bracket_low.signs,
        mass_bracket_high_signs=bracket_high.signs,
        delta8_at_bracket_low=bracket_low.minors[7],
        delta8_at_bracket_high=bracket_high.minors[7],
        jacobi_numerator=jacobi_numerator,
        jacobi_degree=jacobi_numerator.degree(),
        jacobi_extra_nodes_agree=bool(jacobi_extra_nodes_agree),
        jacobi_identity_points=jacobi_identity_points,
        jacobi_numerator_reduced=bool(jacobi_numerator_reduced),
        sturm_counts=sturm_counts,
        b_plus_squarefree=bool(b_plus_squarefree),
        b_plus_prime_roots_in_bracket=sturm_count(
            b_plus_prime, MASS_BRACKET_LOW, MASS_BRACKET_HIGH),
        b_plus_prime_at_low=b_plus_prime.subs(MASS_SYMBOL, MASS_BRACKET_LOW),
        b_plus_prime_at_high=b_plus_prime.subs(MASS_SYMBOL, MASS_BRACKET_HIGH),
        bracket_endpoint_signs=bracket_endpoint_signs,
        shear_bisection_path=shear_path,
        shear_bracket=shear_bracket,
        shear_bracket_low_signs=shear_low.signs,
        shear_bracket_high_signs=shear_high.signs,
        delta7_at_shear_bracket_high=shear_high.minors[6],
        corner_signs=tuple(item.signs for item in corners),
        corner_deltas=tuple(item.delta for item in corners),
        delta6_at_first_corner=corners[0].minors[5],
        delta7_at_second_corner=corners[1].minors[6],
        not_a_product=not_a_product,
        failing_minor_walk=failing_minor_walk,
        chart_denominator_count=len(chart_denominators),
        chart_factor_is_one_minus_c_squared=chart_factor_ok,
        det_nodes=det_nodes,
        det_values=det_values,
        det_polynomials_even=bool(det_polynomials_even),
        det_coefficients_all_positive=bool(det_coefficients_all_positive),
        det_real_root_counts=det_real_root_counts,
        shear_determinants=shear_determinants,
        hodge_p_even_residual=hodge_p_even_residual,
        transpose_covariance_residual=transpose_covariance_residual,
        inverse_p_symmetric_residual=inverse_p_symmetric_residual,
        all_grams_real_symmetric=all(
            item.real_symmetric for item in every_sample),
        all_grams_hermitian=all(item.delta == 0 for item in every_sample),
        nsimplify_calls=nsimplify_occurrences(),
        volume_signs=tuple(item.signs for item in volume_samples),
        volume_determinants=tuple(
            item.determinant for item in volume_samples),
        volume_deltas=tuple(item.delta for item in volume_samples),
        zero_shear_unit_volume_is_identity=bool(zero_shear_unit),
        zero_shear_dialled_is_identity=bool(zero_shear_dialled),
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
        "registry blobs in the worktree. THE TWO BLOCK 186 ARTIFACTS ARE "
        "CONTENT-BOUND -- its note and its runner, the pair that identifies "
        "the commit this block's branch is cut from -- at PARENT_COMMIT, in "
        "the worktree and against their pinned blobs, and PARENT_COMMIT IS "
        "REAL and PARENT_REF resolves to it, so nothing needs sed at landing. "
        "THE STALE PIN IS THE BLOCK 185 TIP, a REAL ancestor of HEAD that "
        "PREDATES Block 186 and therefore carries NEITHER Block 186 artifact, "
        "which is exactly what makes the stale_parent_authority mutation bite: "
        "under it the gate looks for the artifact blobs at a commit where they "
        "do not exist. AUDIT_INPUT_PATHS IS LITERAL and every one of its EIGHT "
        "entries is required readable in the worktree EXCEPT this block's own "
        "note, which lands later and belongs to gate H -- and the eight "
        "include BOTH BLOCK 185 ARTIFACTS, which are the construction this "
        "block parameterizes and the window it characterizes, and the Block "
        "107 note the carrier itself comes from. AND THE MACHINERY IMPORT IS "
        "GATED: the LANDED Block 128 runner must have imported, because the "
        "two helper objects this runner does not build itself -- "
        "cover_embedding() and the Block 105 shear_hodge() -- are read from "
        "it, and NOTHING from any scratchpad is imported or read",
        bool(
            AUDIT_INPUT_PATHS[0] == SELF_NOTE_INPUT
            and len(AUDIT_INPUT_PATHS) == 8
            and len(set(AUDIT_INPUT_PATHS)) == 8
            and BLOCK186_NOTE in AUDIT_INPUT_PATHS
            and BLOCK186_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK185_NOTE in AUDIT_INPUT_PATHS
            and BLOCK185_RUNNER in AUDIT_INPUT_PATHS
            and BLOCK107_NOTE in AUDIT_INPUT_PATHS
            and BLOCK128_RUNNER in AUDIT_INPUT_PATHS
            and CAMPAIGN_NOTE in AUDIT_INPUT_PATHS
            and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
            and authority.inputs_missing == ()
            and PARENT_ARTIFACTS == (BLOCK186_NOTE, BLOCK186_RUNNER)
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
        f"-- Block 185's seam-glued object rebuilt from its displayed "
        f"equations, THE PARAMETER CHART (m, c, v) which is this block's own "
        f"object, the sampled set, the boundary and determinant polynomials "
        f"which are RE-DERIVED here rather than accepted, and the two LANDED "
        f"Block 128 helpers that are the only imports -- and "
        f"{ban['registered_objects']} are REGISTERED and "
        f"{ban['adopted_objects']} are ADOPTED. AND THE BANNER'S SECOND HALF "
        f"IS WHAT IS NOT CLAIMED, gated as declared constants, because THIS "
        f"BLOCK'S HEADLINE IS THE WORD 'OPEN' AND THAT WORD HAS TWO SENSES. "
        f"NO CONNECTIVITY: what is established is a UNION of open "
        f"neighbourhoods around certified points, and 'an open region' must "
        f"not be read as 'one region'. NO GLOBAL BOUNDARY TOPOLOGY: no "
        f"boundary component is shown unique, no two-dimensional boundary "
        f"curve is produced, no monotonicity away from the tested slice is "
        f"established. NO INTERPOLATION BETWEEN SAMPLED RAYS. NO VOLUME "
        f"INTERVAL: two exact points are not a range. NO CERTIFICATE FOR THE "
        f"SEVEN LOWER MINORS STRICTLY INSIDE THE MASS BRACKET: they are "
        f"certified at the two endpoints and the boundary theorem is about "
        f"Delta_8 alone. NO GRAVITY CONSTRAINT QUOTIENT. Asserting any of the "
        f"six, or asserting that the imposed objects are registered, fails "
        f"HERE and nowhere else",
        bool(
            ban["imposed_objects"] == 5
            and ban["registered_objects"] == 0
            and ban["adopted_objects"] == 0
            and ban["objects_registered"] == claims["objects_registered"]
            and ban["connectivity_claimed"] == claims["connectivity_claimed"]
            and ban["global_boundary_claimed"]
            == claims["global_boundary_claimed"]
            and ban["ray_interpolation_claimed"]
            == claims["ray_interpolation_claimed"]
            and ban["volume_interval_claimed"]
            == claims["volume_interval_claimed"]
            and ban["lower_minor_interval_claimed"]
            == claims["lower_minor_interval_claimed"]
            and ban["constraint_quotient_claimed"]
            == claims["constraint_quotient_claimed"]))

    # --- C: the construction control, then the mass axis --------------------
    pins = facts.citation_pins
    checks.check(
        "C-THE-CONSTRUCTION-IS-BLOCK-185s-OBJECT-and-THE-PINS-ARE-PRIMARY",
        f"THE CONTROL COMES FIRST AND IT IS SOMEBODY ELSE'S NUMBER. This "
        f"runner rebuilds Block 185's seam-glued object from its displayed "
        f"equations: of d_K's {facts.raising_nonzeros} entries the restricted "
        f"set A keeps {facts.restricted_nonzeros}, the derived glue "
        f"D = A - P A P carries EXACTLY {facts.glue_nonzeros} nonzero entries "
        f"and is P-odd at {facts.glue_p_odd_residual}, and at "
        f"(m, c, v) = ({FIXTURE_MASS}, {FIXTURE_SHEAR}, 1) the first leading "
        f"minor of the two-history Gram is {facts.fixture.minors[0]} with sign "
        f"vector {facts.fixture.signs} -- WHICH IS BLOCK 185'S LANDED FIRST "
        f"MINOR, DIGIT-FOR-DIGIT. THAT IDENTITY IS THE WHOLE LICENCE FOR "
        f"CALLING WHAT FOLLOWS A CHARACTERIZATION OF THEIR WINDOW: if it moved "
        f"by a digit this would be a different object and every statement "
        f"below would be about a different region. AND WHAT THIS BLOCK CLOSES "
        f"IS PINNED IN THE NOTE THAT LEFT IT OPEN: Block 185's own "
        f"'{B185_WINDOW_PIN}' ({pins['b185_window_open']}) and their "
        f"mass-direction bracket '{B185_BRACKET_PIN}' "
        f"({pins['b185_mass_bracket']}), which this block narrows by a factor "
        f"of more than a thousand; Block 107's scope firewall "
        f"'{B107_NOT_A_NOGO_PIN}' ({pins['b107_not_a_nogo']}), which is what "
        f"made the whole line admissible rather than foreclosed; and Block "
        f"186's hazard sentence '{B186_NSIMPLIFY_PIN}' "
        f"({pins['b186_nsimplify']}), which this runner inherits and honours "
        f"by absence. EVERY ONE IS SOMEBODY ELSE'S LANDED SENTENCE",
        bool(
            facts.glue_nonzeros == claims["glue_nonzeros"]
            and facts.glue_p_odd_residual == claims["glue_p_odd_residual"]
            and facts.fixture.minors[0] == claims["b185_first_minor"]
            and facts.fixture.signs == claims["fixture_signs"]
            and facts.fixture.delta == 0
            and all(pins.values()) == claims["citation_pins"]))
    checks.check(
        "C-THE-MASS-AXIS-POSITIVE-OVER-MORE-THAN-A-DECADE-then-FAILING",
        f"THE WINDOW IS NOT A KNIFE EDGE, AND THAT IS THE BIGGEST RISK THIS "
        f"BLOCK RETIRES. At c = {FIXTURE_SHEAR} the sign vectors at the five "
        f"gated masses {tuple(str(v) for v in GATED_MASSES)} are "
        f"{facts.mass_axis_signs}: STRICTLY POSITIVE 8 OF 8 at 1/10, 3/4 and "
        f"5/4, and FAILING at 3/2 on minors seven and eight and at 2 on minors "
        f"six and eight. The four masses {tuple(str(v) for v in CITED_MASSES)} "
        f"are CITED to the adversarial check, which reproduced all nine of the "
        f"declared table exactly; the five gated here are measured. SEVEN "
        f"CONSECUTIVE SAMPLED MASSES FROM 1/10 TO 5/4 ARE POSITIVE -- MORE "
        f"THAN A DECADE -- AND BLOCK 185'S FIXTURE m = 9/20 SITS WELL INSIDE "
        f"THEM. The exact negative witnesses are pinned: Delta_7 and Delta_8 "
        f"at m = 3/2 and Delta_6 and Delta_8 at m = 2, all four exact "
        f"rationals. EVERY GATED POINT IS EXACTLY HERMITIAN at defects "
        f"{facts.mass_axis_deltas}. Asserting positivity at m = 3/2 fails HERE "
        f"and nowhere else",
        bool(
            facts.mass_axis_signs == claims["mass_axis_signs"]
            and facts.delta7_at_three_halves
            == claims["delta7_at_three_halves"]
            and facts.delta8_at_three_halves
            == claims["delta8_at_three_halves"]
            and facts.delta6_at_two == claims["delta6_at_two"]
            and facts.delta8_at_two == claims["delta8_at_two"]
            and all(value == 0 for value in facts.mass_axis_deltas)
            and len(MASS_AXIS_TABLE) == 9
            and set(GATED_MASSES) | set(CITED_MASSES)
            == {mass for mass, _ in MASS_AXIS_TABLE}))

    # --- D: the mass boundary, then THE BOUNDARY THEOREM --------------------
    checks.check(
        "D-THE-MASS-EDGE-BRACKETED-to-1-over-2048-by-a-REPRODUCED-BISECTION",
        f"THE EDGE IS NOT ASSERTED, IT IS WALKED. An exact bisection on the "
        f"RATIONALS from ({MASS_BISECTION_START[0]}, "
        f"{MASS_BISECTION_START[1]}) -- no float, no tolerance, each step the "
        f"exact rational midpoint -- reproduces the adversarial check's "
        f"recorded path VERDICT BY VERDICT: "
        f"{tuple((str(point), verdict) for point, verdict in facts.mass_bisection_path)}. "
        f"After NINE steps the bracket is {facts.mass_bracket} at width "
        f"{facts.mass_bracket[1] - facts.mass_bracket[0]}, and a TENTH step "
        f"refines it to {facts.mass_refined_bracket} at width "
        f"{facts.mass_refined_bracket[1] - facts.mass_refined_bracket[0]}. THE "
        f"ENDPOINTS CARRY EXACT SIGN CERTIFICATES: all eight minors positive "
        f"at the lower endpoint with Delta_8 = {facts.delta8_at_bracket_low}, "
        f"and at the upper endpoint the sign vector is "
        f"{facts.mass_bracket_high_signs} -- THE SOLE FAILURE IS Delta_8, "
        f"which is what makes the eighth minor the carrier of the mass edge. "
        f"Block 185 could say only that their mass boundary lay in (9/20, 2]; "
        f"THIS BRACKET IS NARROWER BY A FACTOR OF MORE THAN THREE THOUSAND. "
        f"Asserting the upper endpoint positive fails HERE and nowhere else",
        bool(
            facts.mass_bisection_path == claims["mass_bisection_path"]
            and facts.mass_bracket == claims["mass_bracket"]
            and facts.mass_refined_bracket == claims["mass_refined_bracket"]
            and facts.mass_bracket[1] - facts.mass_bracket[0]
            == MASS_BRACKET_WIDTH
            and facts.mass_refined_bracket[1] - facts.mass_refined_bracket[0]
            == MASS_REFINED_WIDTH
            and facts.mass_bracket_low_signs == claims["mass_bracket_low_signs"]
            and facts.mass_bracket_high_signs
            == claims["mass_bracket_high_signs"]
            and facts.delta8_at_bracket_low == claims["delta8_at_bracket_low"]
            and facts.delta8_at_bracket_high
            == claims["delta8_at_bracket_high"]))
    quotient = sp.cancel(
        facts.jacobi_numerator.as_expr() / claims["jacobi_target"])
    quotient_is_positive_rational = bool(
        sp.sympify(quotient).is_Rational and sp.sympify(quotient).is_positive)
    # THE REDUCED CONSTANT: the raw quotient times the determinant
    # certificate's constant is the POSITIVE INTEGER of the reduced statement
    # Delta_8 = KAPPA * A^2 B_- B_+ / (F^2 G^2), since det Q = F^2 G^2 / CONST.
    reduced_kappa = sp.cancel(quotient * claims["det_target"][2])
    checks.check(
        "D-THE-BOUNDARY-THEOREM-the-mass-edge-is-B-plus-UNIQUE-SIMPLE-ROOT",
        f"AND THE EDGE IS NOT ONLY BRACKETED, IT IS AN ALGEBRAIC OBJECT. "
        f"Jacobi's complementary-minor identity turns Delta_8(m, "
        f"{FIXTURE_SHEAR}) into a ratio of two determinants of the SAME "
        f"pencil: the numerator is the complementary 24x24 block, recovered "
        f"EXACTLY by interpolation at {JACOBI_DEGREE_BOUND + 1} nodes for a "
        f"polynomial of degree {facts.jacobi_degree} and confirmed at four "
        f"further nodes ({facts.jacobi_extra_nodes_agree}), and the identity "
        f"Delta_8 * det Q = numerator is verified against the DIRECT Gram "
        f"route at seven exact masses ({facts.jacobi_identity_points}). THAT "
        f"NUMERATOR IS EXACTLY {quotient} TIMES A(m)^2 B_-(m) B_+(m) -- A "
        f"POSITIVE RATIONAL MULTIPLE ({quotient_is_positive_rational}) -- so "
        f"with det Q = F^2 G^2 / CONST the reduced statement is "
        f"Delta_8(m, {FIXTURE_SHEAR}) = {reduced_kappa} * A^2 B_- B_+ / "
        f"(F^2 G^2) with a POSITIVE INTEGER constant, and A^2 B_- B_+ IS the "
        f"reduced numerator because gcd(A^2 B_- B_+, F^2 G^2) = 1 "
        f"({facts.jacobi_numerator_reduced}). ON THE BRACKET THE EXACT STURM "
        f"COUNTS ARE {facts.sturm_counts} for A, B_- and B_+; A and B_- are "
        f"strictly negative at both endpoints with no root between them "
        f"(endpoint signs {facts.bracket_endpoint_signs}), so A^2 > 0 and "
        f"B_- < 0 THROUGHOUT and sign(Delta_8) = -sign(B_+); and B_+ is "
        f"squarefree ({facts.b_plus_squarefree}) with B_+' carrying "
        f"{facts.b_plus_prime_roots_in_bracket} roots in the bracket and the "
        f"positive endpoint values {facts.b_plus_prime_at_low} and "
        f"{facts.b_plus_prime_at_high}. THEREFORE THE Delta_8 EDGE IS EXACTLY "
        f"THE UNIQUE SIMPLE ROOT OF B_+ IN THE BRACKET. This is an EXACT "
        f"THEOREM about one edge of one ray and it is not a bisection "
        f"artifact; what it does NOT say is anything about the seven lower "
        f"minors strictly inside the bracket, which are certified at the two "
        f"endpoints only. Asserting a factorization without B_+, or two roots "
        f"where the Sturm sequence finds one, fails HERE and nowhere else",
        bool(
            quotient == claims["jacobi_quotient"]
            and quotient_is_positive_rational
            and reduced_kappa == claims["jacobi_kappa"]
            and sp.sympify(reduced_kappa).is_Integer
            and sp.sympify(reduced_kappa).is_positive
            and facts.jacobi_extra_nodes_agree
            and all(facts.jacobi_identity_points)
            and len(facts.jacobi_identity_points) == 7
            and facts.jacobi_numerator_reduced
            == claims["jacobi_numerator_reduced"]
            and facts.sturm_counts == claims["sturm_counts"]
            and facts.b_plus_squarefree == claims["b_plus_squarefree"]
            and facts.b_plus_prime_roots_in_bracket == 0
            and facts.b_plus_prime_at_low == claims["b_plus_prime_at_low"]
            and facts.b_plus_prime_at_high == claims["b_plus_prime_at_high"]
            and facts.bracket_endpoint_signs
            == claims["bracket_endpoint_signs"]))

    # --- E: the shear axis and the corners ----------------------------------
    checks.check(
        "E-THE-SHEAR-EDGE-BRACKETED-to-1-over-2560-and-CARRIED-BY-MINOR-7",
        f"THE SECOND AXIS IS WALKED THE SAME WAY. Exact bisection from "
        f"({SHEAR_BISECTION_START[0]}, {SHEAR_BISECTION_START[1]}) at "
        f"m = {FIXTURE_MASS} reproduces the recorded path verdict by verdict: "
        f"{tuple((str(point), verdict) for point, verdict in facts.shear_bisection_path)}, "
        f"terminating on {facts.shear_bracket} at width "
        f"{facts.shear_bracket[1] - facts.shear_bracket[0]}. The lower "
        f"endpoint is positive 8 of 8 and the upper endpoint is "
        f"{facts.shear_bracket_high_signs} -- THE SOLE FAILURE IS Delta_7, so "
        f"MINOR SEVEN CARRIES THE SHEAR EDGE while minor EIGHT carried the "
        f"mass edge, and the exact witness Delta_7 is pinned. THE TWO EDGES "
        f"ARE DIFFERENT SHEETS OF THE BOUNDARY. Asserting the upper shear "
        f"endpoint positive fails HERE and nowhere else",
        bool(
            facts.shear_bisection_path == claims["shear_bisection_path"]
            and facts.shear_bracket == claims["shear_bracket"]
            and facts.shear_bracket[1] - facts.shear_bracket[0]
            == SHEAR_BRACKET_WIDTH
            and facts.shear_bracket_low_signs
            == claims["shear_bracket_low_signs"]
            and facts.shear_bracket_high_signs
            == claims["shear_bracket_high_signs"]
            and facts.delta7_at_shear_bracket_high
            == claims["delta7_at_shear_bracket_high"]))
    checks.check(
        "E-NOT-A-PRODUCT-the-boundary-is-CURVED-and-the-FAILING-MINOR-MOVES",
        f"AND THE REGION IS NOT A RECTANGLE, WHICH IS THE ONE THING TWO "
        f"COORDINATE RAYS COULD NEVER SHOW BY THEMSELVES. m = 1 is certified "
        f"positive on the mass ray at c = {FIXTURE_SHEAR} and c = 3/5 is "
        f"certified positive on the shear ray at m = {FIXTURE_MASS} -- both "
        f"measured HERE, not recalled -- YET THE PAIR (1, 3/5) FAILS at sign "
        f"vector {facts.corner_signs[0]} ({facts.not_a_product}). THE POSITIVE "
        f"SET IS THEREFORE NOT THE CARTESIAN PRODUCT of the two certified ray "
        f"intervals, and larger shear tolerates only smaller mass. The second "
        f"gated corner (1/10, 4/5) fails at {facts.corner_signs[1]}, and the "
        f"two further corners (5/4, 1/2) and (3/4, 7/10) are CITED to the "
        f"adversarial check, which measured all four. AND THE FAILING MINOR "
        f"MOVES ALONG THE BOUNDARY: the index of the first non-positive minor "
        f"is {facts.failing_minor_walk} at the mass edge, the shear edge and "
        f"the corner respectively -- EIGHT, then SEVEN, then SIX. THE BOUNDARY "
        f"IS A UNION OF MINOR-ZERO LOCI AND IT IS CURVED. What this does NOT "
        f"determine is the intervening curve, and no interpolation between the "
        f"sampled rays is claimed anywhere. Both gated corners are exactly "
        f"Hermitian at defects {facts.corner_deltas}. Asserting (1, 3/5) "
        f"positive fails HERE and nowhere else",
        bool(
            facts.corner_signs == claims["corner_signs"]
            and facts.delta6_at_first_corner
            == claims["delta6_at_first_corner"]
            and facts.delta7_at_second_corner
            == claims["delta7_at_second_corner"]
            and facts.not_a_product == claims["not_a_product"]
            and facts.failing_minor_walk == claims["failing_minor_walk"]
            and all(value == 0 for value in facts.corner_deltas)
            and len(CORNER_TABLE) == 4))

    # --- F: the openness theorem --------------------------------------------
    claimed_f, claimed_g, claimed_const = claims["det_target"]
    det_certificate_holds = all(
        value * claimed_const
        == (claimed_f.subs(MASS_SYMBOL, node) ** 2
            * claimed_g.subs(MASS_SYMBOL, node) ** 2)
        for node, value in zip(facts.det_nodes, facts.det_values))
    checks.check(
        "F-THE-OPENNESS-THEOREM-chart-domain-c-not-plus-minus-1-and-det-Q-positive",
        f"THE PROMOTION FROM SAMPLES TO NEIGHBOURHOODS, IN THE ADVERSARIAL "
        f"CHECK'S CORRECTED FORM. THE DOMAIN IS "
        f"U = {{(m,c): c != +/-1 AND det Q(m,c) != 0}}, AND THE CHART HALF IS "
        f"NOT DECORATION: measured on a SYMBOLIC shear, the landed shear Hodge "
        f"block has {facts.chart_denominator_count} entries with a nontrivial "
        f"denominator and every one of them is 1 - c^2 up to sign "
        f"({facts.chart_factor_is_one_minus_c_squared}) -- the (dx,dt) channel "
        f"-- so a domain statement that says only 'det Q != 0' is INCOMPLETE, "
        f"which is exactly the check's C5 correction. THE DETERMINANT HALF HAS "
        f"A COMPACT CERTIFICATE: det Q(m, {FIXTURE_SHEAR}) * CONST = "
        f"F(m)^2 G(m)^2 as a POLYNOMIAL IDENTITY ({det_certificate_holds}), "
        f"established by agreement at {len(facts.det_nodes)} DISTINCT rational "
        f"nodes for two polynomials of degree at most {DET_DEGREE} -- 33 "
        f"points determine a degree-32 polynomial, so this is a PROOF and not "
        f"a sample. EVERY coefficient of F and of G is a POSITIVE INTEGER "
        f"({facts.det_coefficients_all_positive}) and both are EVEN "
        f"({facts.det_polynomials_even}), with "
        f"{facts.det_real_root_counts} real roots respectively, SO "
        f"det Q > 0 FOR EVERY REAL m ON THIS RAY. The three positive shear "
        f"samples carry their own exact determinants, so all ten certified "
        f"points are in U. THEREFORE each Delta_k is a continuous function on "
        f"U and eight strict inequalities at a certified point persist on a "
        f"neighbourhood: THE POSITIVE SET IS OPEN AROUND EVERY CERTIFIED "
        f"POINT. AND THE CONCLUSION IS STRICTLY LOCAL, AS THE CHECK SCOPED IT: "
        f"a UNION of open neighbourhoods, and NOT connectivity, NOT a unique "
        f"boundary component, NOT a two-dimensional boundary curve and NOT "
        f"interpolation between rays. Asserting a different F fails HERE and "
        f"nowhere else",
        bool(
            det_certificate_holds
            and facts.chart_denominator_count
            == claims["chart_denominator_count"]
            and facts.chart_factor_is_one_minus_c_squared
            == claims["chart_factor_is_one_minus_c_squared"]
            and facts.det_coefficients_all_positive
            == claims["det_coefficients_all_positive"]
            and facts.det_polynomials_even == claims["det_polynomials_even"]
            and facts.det_real_root_counts == (0, 0)
            and facts.shear_determinants == claims["shear_determinants"]
            and all(value != 0 for value in facts.shear_determinants)))
    checks.check(
        "F-HERMITICITY-IS-STRUCTURAL-and-NOTHING-HERE-IS-nsimplified",
        f"AND THE HERMITICITY IS NOT A SAMPLE ACCIDENT, WHICH MATTERS BECAUSE "
        f"IT IS WHAT LETS A SIGN VECTOR MEAN ANYTHING AT ALL. The A02-image "
        f"geometry is P-EVEN at {facts.hodge_p_even_residual} nonzero entries "
        f"and the glue is P-ODD at {facts.glue_p_odd_residual}, so "
        f"P Q P - Q^T has {facts.transpose_covariance_residual} nonzero "
        f"entries; the action and its inverse are REAL, so Q^-1 P is symmetric "
        f"at {facts.inverse_p_symmetric_residual} and THE REFLECTED RESTRICTED "
        f"GRAM IS REAL SYMMETRIC WHEREVER IT IS DEFINED. Every one of the "
        f"chart points measured in this run is real symmetric "
        f"({facts.all_grams_real_symmetric}) at Hermiticity defect exactly "
        f"zero ({facts.all_grams_hermitian}), so leading principal minors are "
        f"the right positivity test at every one of them. EVERY MEASURED "
        f"SCALAR IS AN EXACT sympy Rational or Integer and NOT ONE IS A FLOAT "
        f"({facts.exactness_holds}). AND THE BLOCK 186 HAZARD IS HONOURED BY "
        f"ABSENCE AND MEASURED RATHER THAN PROMISED: nsimplify carries a "
        f"rational TOLERANCE and maps a small nonzero rational to EXACTLY "
        f"ZERO, so a minor passed through it can silently lose its sign and "
        f"manufacture a positivity verdict. THIS RUNNER CALLS IT "
        f"{facts.nsimplify_calls} TIMES, counted in its own source, because "
        f"every mass, shear and volume here is already an exact Rational",
        bool(
            facts.hodge_p_even_residual == claims["hodge_p_even_residual"]
            and facts.glue_p_odd_residual == claims["glue_p_odd_residual_f"]
            and facts.transpose_covariance_residual
            == claims["transpose_covariance_residual"]
            and facts.inverse_p_symmetric_residual
            == claims["inverse_p_symmetric_residual"]
            and facts.all_grams_real_symmetric
            == claims["all_grams_real_symmetric"]
            and facts.all_grams_hermitian
            and facts.nsimplify_calls == claims["nsimplify_calls"]
            and facts.exactness_holds))

    # --- G: the volume dial -------------------------------------------------
    checks.check(
        "G-THE-VOLUME-DIAL-survives-BOTH-directions-and-it-is-TWO-POINTS",
        f"THE WINDOW HAS A THIRD DIMENSION, AND EXACTLY TWO POINTS OF IT ARE "
        f"CERTIFIED. At the fixture (m, c) = ({FIXTURE_MASS}, "
        f"{FIXTURE_SHEAR}) the two-history Gram stays EXACTLY Hermitian at "
        f"defects {facts.volume_deltas} and STRICTLY POSITIVE 8 of 8 at both "
        f"v = {VOLUME_POINTS[0]} and v = {VOLUME_POINTS[1]}, sign vectors "
        f"{facts.volume_signs}, with both exact determinants reproduced. THE "
        f"VOLUME CONVENTION IS DISCLOSED AND NOT SILENT: the two zero-shear "
        f"seam anchors are held EXACTLY FLAT, which is the adversarial check's "
        f"own volume-dial construction, and it is a MEASURED NO-OP at v = 1 "
        f"because the landed shear Hodge at zero shear and unit volume IS the "
        f"identity ({facts.zero_shear_unit_volume_is_identity}) while at "
        f"v = {VOLUME_POINTS[0]} it is NOT "
        f"({facts.zero_shear_dialled_is_identity}) -- so the choice is a real "
        f"choice off v = 1 and it is stated. THIS IS TWO-POINT ROBUSTNESS AND "
        f"NOT A CERTIFIED INTERVAL: nothing here says anything about v between "
        f"or beyond {VOLUME_POINTS[0]} and {VOLUME_POINTS[1]}, and "
        f"claim_volume_interval fails in family B for asserting otherwise. "
        f"Asserting that positivity fails at v = {VOLUME_POINTS[1]} fails HERE "
        f"and nowhere else",
        bool(
            facts.volume_signs == claims["volume_signs"]
            and facts.volume_determinants == claims["volume_determinants"]
            and facts.volume_deltas == claims["volume_deltas"]
            and facts.zero_shear_unit_volume_is_identity
            == claims["unit_volume_convention_is_noop"]
            and not facts.zero_shear_dialled_is_identity
            and len(VOLUME_POINTS) == 2))

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
        f"is fourteen members mapped one-per-family across A through H",
        bool(
            facts.note_at_final_path
            and NOTE_PATH.name == FINAL_NOTE_NAME
            and set(facts.scope) == set(SCOPE_KEYS)
            and required == SCOPE_KEYS
            and all(facts.scope[key] for key in required)
            and facts.scope["n5_verbatim"]
            and len(MUTATIONS) == 14
            and len(set(MUTATIONS)) == 14
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
          f"it {authority.parent_ref_and_ancestry}, and BOTH Block 186 "
          f"artifacts are content-bound there and in the worktree "
          f"{authority.parent_artifact_blobs}. THE AUDIT INPUTS: "
          f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} "
          f"readable in the worktree (this block's own note excluded, since it "
          f"lands later and is gate H's), missing {authority.inputs_missing}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {authority.stale_is_real_ancestor} and carries NEITHER Block "
          f"186 artifact {authority.stale_carries_neither_artifact} -- it is "
          f"the Block 185 tip, which PREDATES both artifacts, and that absence "
          f"is exactly what makes the stale_parent_authority mutation bite")
    print(f"  THE MACHINERY: THE CONSTRUCTION IS BLOCK 185'S, rebuilt here from "
          f"its displayed equations and PARAMETERIZED in (m, c, v). The "
          f"staggered kernel, the grade projectors, d_K, the site reflection, "
          f"the offset permutation, the restricted raising set, the derived "
          f"glue and the glued action are ALL BUILT DIRECTLY HERE. The LANDED "
          f"Block 128 runner is imported {authority.machinery_import_landed} "
          f"for EXACTLY TWO objects, cover_embedding() and the Block 105 "
          f"shear_hodge(); the carrier is {TIME_EXTENT}x{SPACE_EXTENT} at "
          f"dimension {COVER_SIZE} and the reference fixture is "
          f"m = {FIXTURE_MASS}, c = {FIXTURE_SHEAR}, v = 1. NOTHING from any "
          f"scratchpad is imported or read")
    print(f"  THE BANNER: {ban['imposed_objects']} imposed objects, "
          f"{ban['registered_objects']} registered and "
          f"{ban['adopted_objects']} adopted; MEASURED connectivity-claimed "
          f"{ban['connectivity_claimed']}, global-boundary-claimed "
          f"{ban['global_boundary_claimed']}, ray-interpolation-claimed "
          f"{ban['ray_interpolation_claimed']}, volume-interval-claimed "
          f"{ban['volume_interval_claimed']}, lower-minor-interval-claimed "
          f"{ban['lower_minor_interval_claimed']} and "
          f"constraint-quotient-claimed {ban['constraint_quotient_claimed']}. "
          f"The imposed objects are {IMPOSED_OBJECTS}")
    print(f"  THE CITATION PINS: {facts.citation_pins} -- the open item and the "
          f"superseded bracket read from Block 185's PRIMARY BODY, the scope "
          f"firewall from Block 107's, and the nsimplify hazard from Block "
          f"186's own runner")
    print(f"  THE CONSTRUCTION CONTROL: d_K carries {facts.raising_nonzeros} "
          f"entries, the restricted set A carries {facts.restricted_nonzeros} "
          f"and D = A - P A P carries EXACTLY {facts.glue_nonzeros}, P-odd at "
          f"{facts.glue_p_odd_residual}. At the fixture the first leading "
          f"minor is {facts.fixture.minors[0]} with sign vector "
          f"{facts.fixture.signs} and defect {facts.fixture.delta} -- BLOCK "
          f"185'S LANDED NUMBER, DIGIT-FOR-DIGIT")
    print(f"  THE MASS AXIS at c = {FIXTURE_SHEAR}: gated masses "
          f"{tuple(str(v) for v in GATED_MASSES)} give sign vectors "
          f"{facts.mass_axis_signs} at defects {facts.mass_axis_deltas}; the "
          f"cited masses {tuple(str(v) for v in CITED_MASSES)} are the "
          f"adversarial check's. SEVEN CONSECUTIVE SAMPLED MASSES FROM 1/10 TO "
          f"5/4 ARE POSITIVE. Witnesses: Delta_7(3/2) = "
          f"{facts.delta7_at_three_halves}; Delta_8(3/2) = "
          f"{facts.delta8_at_three_halves}; Delta_6(2) = {facts.delta6_at_two}; "
          f"Delta_8(2) = {facts.delta8_at_two}")
    print(f"  THE MASS BISECTION: "
          f"{tuple((str(point), verdict) for point, verdict in facts.mass_bisection_path)} "
          f"-> bracket {facts.mass_bracket} at width "
          f"{facts.mass_bracket[1] - facts.mass_bracket[0]}, refined to "
          f"{facts.mass_refined_bracket} at width "
          f"{facts.mass_refined_bracket[1] - facts.mass_refined_bracket[0]}. "
          f"Endpoint sign vectors {facts.mass_bracket_low_signs} and "
          f"{facts.mass_bracket_high_signs}; "
          f"Delta_8 = {facts.delta8_at_bracket_low} and "
          f"{facts.delta8_at_bracket_high}")
    print(f"  THE BOUNDARY THEOREM: the Jacobi numerator has degree "
          f"{facts.jacobi_degree}, agrees at four extra nodes "
          f"{facts.jacobi_extra_nodes_agree}, and the identity against the "
          f"DIRECT Gram route holds at {facts.jacobi_identity_points}. It is "
          f"{JACOBI_QUOTIENT} times A^2 B_- B_+, so with det Q = F^2 G^2 / "
          f"CONST the reduced statement carries the POSITIVE INTEGER "
          f"{JACOBI_KAPPA}; the numerator is REDUCED "
          f"{facts.jacobi_numerator_reduced}. Sturm counts on the bracket "
          f"{facts.sturm_counts}; endpoint signs of (A, B_-, B_+) "
          f"{facts.bracket_endpoint_signs}; B_+ squarefree "
          f"{facts.b_plus_squarefree}; B_+' has "
          f"{facts.b_plus_prime_roots_in_bracket} roots there and endpoint "
          f"values {facts.b_plus_prime_at_low} and "
          f"{facts.b_plus_prime_at_high}. THE MASS EDGE IS THE UNIQUE SIMPLE "
          f"ROOT OF B_+")
    print(f"  THE SHEAR BISECTION: "
          f"{tuple((str(point), verdict) for point, verdict in facts.shear_bisection_path)} "
          f"-> bracket {facts.shear_bracket} at width "
          f"{facts.shear_bracket[1] - facts.shear_bracket[0]}; endpoint sign "
          f"vectors {facts.shear_bracket_low_signs} and "
          f"{facts.shear_bracket_high_signs}; "
          f"Delta_7 = {facts.delta7_at_shear_bracket_high}")
    print(f"  THE CORNERS: gated sign vectors {facts.corner_signs} at defects "
          f"{facts.corner_deltas}; NOT A PRODUCT {facts.not_a_product}; the "
          f"first failing minor at (mass edge, shear edge, corner) is "
          f"{facts.failing_minor_walk}. THE BOUNDARY IS CURVED AND ITS FAILING "
          f"MINOR MOVES")
    print(f"  THE OPENNESS CERTIFICATES: the symbolic shear Hodge has "
          f"{facts.chart_denominator_count} entries with a nontrivial "
          f"denominator, all of them 1 - c^2 up to sign "
          f"{facts.chart_factor_is_one_minus_c_squared}, so the chart is "
          f"undefined at c = +/-1. det Q(m, {FIXTURE_SHEAR}) is certified "
          f"against F^2 G^2 / CONST at {len(facts.det_nodes)} distinct nodes "
          f"for a degree-{DET_DEGREE} identity; F and G have all-positive "
          f"integer coefficients {facts.det_coefficients_all_positive}, are "
          f"even {facts.det_polynomials_even} and have "
          f"{facts.det_real_root_counts} real roots, SO det Q > 0 FOR EVERY "
          f"REAL m. The three shear-ray determinants are "
          f"{tuple(str(value) for value in facts.shear_determinants)}")
    print(f"  THE STRUCTURE: H_image P-even at {facts.hodge_p_even_residual}, "
          f"D P-odd at {facts.glue_p_odd_residual}, P Q P = Q^T at "
          f"{facts.transpose_covariance_residual}, Q^-1 P symmetric at "
          f"{facts.inverse_p_symmetric_residual}; every measured Gram real "
          f"symmetric {facts.all_grams_real_symmetric} and Hermitian at "
          f"defect zero {facts.all_grams_hermitian}")
    print(f"  THE VOLUME DIAL: sign vectors {facts.volume_signs} at defects "
          f"{facts.volume_deltas} for v in "
          f"{tuple(str(v) for v in VOLUME_POINTS)}; determinants "
          f"{tuple(str(value) for value in facts.volume_determinants)}. The "
          f"zero-shear anchor block IS the identity at v = 1 "
          f"{facts.zero_shear_unit_volume_is_identity} and is NOT at "
          f"v = {VOLUME_POINTS[0]} {facts.zero_shear_dialled_is_identity}, so "
          f"the flat-anchor convention is a REAL choice off v = 1 and it is "
          f"disclosed. TWO POINTS, NOT AN INTERVAL")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False the note has NOT landed at docs/ yet, there is no draft "
          f"fallback anywhere in this runner, gate H is EXPECTED to fail and "
          f"the gate-H mutation is UNTESTABLE until the note lands. Scope keys "
          f"satisfied: {sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  EXACTNESS: every measured scalar above is an exact sympy "
          f"Rational or Integer and NOT ONE IS A FLOAT "
          f"({facts.exactness_holds}); no tolerance enters any check; "
          f"positivity is decided by exact leading principal minors and the "
          f"boundary theorem by exact Sturm sequences, never by an eigenvalue "
          f"estimate or a floating-point root isolation; and sp.nsimplify is "
          f"called {facts.nsimplify_calls} times in this file, counted in its "
          f"own source -- THE BLOCK 186 HAZARD, HONOURED BY ABSENCE. ELAPSED "
          f"{elapsed_ns // 1_000_000} ms")
    print(f"  THE CORPUS RELATION: Blocks 104, 105, 106, 107, 128 and 181-186 "
          f"STAND EXACTLY AS LANDED and no landed note is edited. BLOCK 185 IS "
          f"UPGRADED AND NOT CORRECTED: their windowed-positivity claim "
          f"stands, their fixture number is reproduced above digit-for-digit, "
          f"and what this block adds is that the window is ROOMY, that its two "
          f"sampled edges are BRACKETED, that its mass edge on the c = 5/13 "
          f"ray is EXACT-ALGEBRAIC and that its volume direction survives at "
          f"two points. THE ADVERSARIAL CHECK PRECEDED THIS DRAFT and its "
          f"verdicts are folded from the first line: C1-C4 and C6 confirmed "
          f"exactly on independent bisections, C5 CORRECTED to carry the chart "
          f"domain c != +/-1 and scoped strictly local, and C7 UPGRADED to the "
          f"exact simple-root theorem gated above. ONE PROCESS NOTE, NOT A "
          f"CORRECTION: the solve's spec named 1456/1024 as a point beyond the "
          f"upper endpoint and 1456/1024 IS 91/64; the checker caught the "
          f"arithmetic and added 2913/2048 as a genuinely further point")
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
