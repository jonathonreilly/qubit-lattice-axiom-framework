#!/usr/bin/env python3
"""BLOCK 178 -- THE SHEAR-MIRROR THEOREM AND THE INTERFERENCE ARM.

THE RESULT, AND ITS EXACT SCOPE.  On the committed antiperiodic Dirac-Kahler
fixtures at cover extents T_cover = 8 (T_phys = 4) and T_cover = 12 (T_phys = 6),
both at L_x = 4, with the committed descended reflection r and the region pin
c = 1; and, for the interference arm, on the committed 12x4 xgraded bench with
the menu (0, 1/5, 2/5, 3/5) at the record cells (2,0) and (3,0) on the holo_t
dial:

  1. THE SHEAR-MIRROR THEOREM -- THE HEADLINE.  For the antiunitary reflection
     Theta phi = r conj(phi) the invariance condition on a quadratic form is
     r Q r = Q^T and NOT r Q r = Q.  THE SUPERVISOR'S COMMUTATOR-ONLY CONVENTION
     IS QUOTED AND CORRECTED; the two coincide only on real-symmetric controls.
     The zero-shear flat control is EXACTLY Theta-invariant at both extents under
     BOTH tests (0/0).  THE VOLUME COUNTEREXAMPLE: zero shear with the
     reflection-symmetric profile nu(t,x) = (1,2,3,4)_x makes H diagonal,
     repeating (25/16, 3/2, 17/8, 17/6) on every time level, and BOTH defects
     vanish at BOTH extents -- so NON-FLAT REFLECTION-SYMMETRIC VOLUME GEOMETRY
     SURVIVES THE MIRROR and the slogan "mirror sector = geometry-free sector" is
     REFUTED AND REPLACED BY: SHEARS BREAK THE MIRROR; VOLUMES DO NOT.

  2. THE SHEAR COUNTS, AND THE PER-LEVEL LAW REFUTED.  Ambient sigma = 3/5 at
     unit volume gives 64 nonzero entries at 8x4 and 96 at 12x4; pinning levels
     t = 0, 1 leaves 32 and 64; every nonzero entry is +-15/64.  A single
     b-modulus level contributes EXACTLY 16 entries.  BUT A PHYSICAL SINGLE-LEVEL
     SHEAR ALSO FORCES ITS a-MODULUS and contributes 24 -- the same 16
     off-diagonal +-15/64 PLUS 8 diagonal +-9/64 in the blocks (0,0) and (2,2).
     THE ADDITIVE 16-PER-LEVEL LAW IS REFUTED and the count identities are
     PROFILE-SPECIFIC CANCELLATIONS.

  3. THE TRANSPORT LEG.  The reflection defect of the quotient connection is
     EXACTLY dial-linear MATRIXWISE, D_K(s_x, s_t) = s_x D_K(1,0) + s_t D_K(0,1).
     The FULL commutator censuses are s_x (1,0):8, (1,2):8 and s_t (0,1):16,
     (1,0):32, (2,1):16 at 8x4 -- counts 16, 64, 72 -- and s_x (1,0):16,
     (1,2):16 and s_t (0,1):16, (1,0):48, (2,1):32 at 12x4 -- counts 32, 96, 112.
     THE TWO-CLASS STORY AND THE EXTENT-SCALING STORY ARE BOTH REFUTED.  Under
     the correct transpose test the counts are 16, 64, 72 at 8x4 but 24, 104, 116
     at 12x4, and at FLAT ZERO SHEAR K is real antisymmetric and PASSES the
     commutator test while FAILING the transpose test with 16 entries at 8x4 and
     24 at 12x4.  THE CONVENTION IS LOAD-BEARING AND DISCLOSED; every nonzero
     transport dial fails BOTH.

  4. THE OBSTRUCTION, AT EXACTLY ITS STRENGTH.  Shear non-invariance BLOCKS THE
     CANONICAL reflection-positive Hilbert reconstruction from the fixed data,
     because the reflected covariance selection [r (Q^-1)^T]_SS can be
     NON-HERMITIAN and unusable as an OS Gram -- exhibited here.  IT DOES NOT
     FORCE herm() SPECIFICALLY NOR ANY PARTICULAR PRESCRIPTION, THE BLOCK-177
     GRADING PREMISE REMAINS A GENUINE FORK, and the volume counterexample
     narrows the antecedent to SHEAR SCOPE.

  5. THE FORK-INDEPENDENT FAMILY.  Every function of Q alone is fork-independent,
     so |Z|^2 = pi^(2N)/|det Q|^2 is positive and transport-sensitive there.  IT
     IS NOT UNIQUE: |Z|^p for every p > 0, positive functions of Q^dag Q, and
     1/det(herm Q) on its positive-definite domain are the same kind of object,
     measured positive and dial-sensitive here.  UNIQUENESS WOULD REQUIRE A
     READOUT AXIOM ABSENT HERE -- consistent with the landed Block 176 and Block
     177 withdrawals and with the sister lane's #7325 countermodel.

  6. THE INTERFERENCE ARM.  The composed holonomy-dialled record machinery is
     GATED AT THE TRIVIAL DIAL; I_off reproduces the landed Block 176 baseline
     EXACTLY; J != 0 EXACTLY at (0, 1/4) with signs (+,+,-,-), and its first
     entry is reverified here against the 2299-digit-over-2302-digit REDUCED
     RATIONAL the independent route printed; the strict three-point contraction
     chain at lambda = 1/2, 1/4, 1/8 holds on disjoint exact brackets; and
     J -> 0 IS PROVEN BY RATIONAL CONTINUITY, which SUPERSEDES the sample-based
     claim.  The reading "transport is record-record interference" is carried as
     AN INTERPRETATION AT SCOPE and is never gated as a theorem.

GATES
  A  authority: main plus the TWO Block 177 artifacts content-bound, the parent
     runner ACTUALLY IMPORTED, and the stale pin verified to carry NEITHER.
  B  the two banners -- the inertia convention and the imposed-object banner with
     the interference reading SCOPED AS INTERPRETATION -- and both bench anchors.
  C  THE MIRROR THEOREM: zero shear 0/0 at both extents under BOTH tests, the
     volume counterexample exact, the ambient and pinned counts, and the 24-entry
     single-level accounting with BOTH moduli.
  D  THE TRANSPORT LEG: dial linearity matrixwise, the FULL hop censuses at both
     extents, and the transpose/commutator split including the flat case.
  E  THE OBSTRUCTION and THE FAMILY: the non-Hermitian reflected-covariance
     exhibit, the family exhibit, and the scoped note statements.
  F  THE INTERFERENCE ARM: I_off exact, J at (0,1/4) against the embedded
     reduced-rational literal, the three-lambda brackets, and the continuity
     structure.
  G  THE CORRECTIONS RECORD: four supervisor corrections plus three further
     checker corrections, verbatim-keyed, with the #7325 citation.
  H  note at final path, the FULL scope-key certificate, and the N5 fence.

BASELINE EXPECTATION: 7 of 8, with H failing on note-at-final-path alone until
the note is landed at docs/.

RUNNING
  python3 scripts/admissibility_dirac_kahler_shear_mirror_interference_2026_08_23.py
  python3 ... --list-mutations
  python3 ... --mutation claim_geometry_free_mirror
  python3 ... --deep

NOTES FOR THE LANDING AGENT
  1. PARENT_COMMIT is REAL and PARENT_REF resolves to it; nothing needs sed.
  2. CURRENT_MAIN was RE-RESOLVED at draft time.
  3. The stale pin is the Block 176 tip, a real ancestor of HEAD that carries
     NEITHER Block 177 artifact -- which is what makes the
     stale_parent_authority mutation bite.
  4. Re-run at landing; gate H should then pass and the battery should be 8/8.
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

R = sp.Rational
Z0 = sp.Integer(0)
ONE = sp.Integer(1)

_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# This fallback keeps the scratchpad draft executable before it is moved to
# scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path(
        "/Users/jonBridger/Projects/Physics-baremetal-probes/"
        ".claude/worktrees/gravity-toe-lane-work-427b0b"
    )
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE PARENT IMPORT.  Block 177 is the stack parent AND the content parent: it
# re-exports the whole landed chain, and its NAMED PREMISE -- the quasi-free
# sector identification -- is the object this block measures the fork of.
try:
    import admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23 as b177
    PARENT_IMPORT_LANDED = True
except ModuleNotFoundError:                                   # unlanded parent
    b177 = None
    PARENT_IMPORT_LANDED = False

if b177 is not None:
    b176 = b177.b176
    b175 = b177.b175
    b174 = b177.b174
    b171 = b177.b171
    b170 = b177.b170
    b165 = b177.b165
else:                                                  # pragma: no cover
    b176 = None
    b175 = None
    b174 = None
    import admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21 as b171
    b170 = b171.b170
    b165 = b171.b165

b166 = b170.b166
herm = b171.herm
is_zero = b171.is_zero
tri = b171.tri
dense = b165.dense

# THE BENCH MACHINERY, IMPORTED FROM BLOCK 170 AND NEVER REBUILT HERE.
Bench = b170.Bench
Site = b171.Site
SX = b170.SX
ST = b170.ST
MASS = b170.MASS

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_"
    "NOTE_2026-08-23.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
# DECLARED DRAFT FALLBACK, read ONLY when the final path is absent.  Gate H
# requires the final path, so the fallback never makes a gate pass.
DRAFT_NOTE_PATH = Path(
    "/private/tmp/claude-502/"
    "-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-"
    "gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/"
    "scratchpad/block178_note_draft.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE SINGLE-PARENT PIN.  Block 177 is BOTH the stack parent and the content
# parent, so there are exactly TWO artifact pins.
BLOCK177_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_"
    "NOTE_2026-08-23.md"
)
BLOCK177_RUNNER = (
    "scripts/admissibility_dirac_kahler_conditional_symmetric_power_theorem_"
    "2026_08_23.py"
)
PARENT_ARTIFACTS = (BLOCK177_NOTE, BLOCK177_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "54b268825503bd3f8d3bb371d6c07008089af021",   # Block 177 note
    "3775eed8f9ef8151b5696bd35821b792d11d84be",   # Block 177 runner
)

# Deliberately literal: this is the complete audit read surface.  Every entry is
# a WORKTREE-READABLE path at landing time.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23.py",
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
    "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
)

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CURRENT_MAIN WAS RE-RESOLVED AT DRAFT TIME.
CURRENT_MAIN = "0e212ee4c66019a9dc8dae204680d7c45a0ae8ab"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on the Block 177 tip, so the parent branch is that.
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block177-"
              "conditional-symmetric-power-20260823")
PARENT_COMMIT = "1db319647c14f447cfbcd90bc2da99a2205102e4"
# The Block 176 tip: a real ancestor of HEAD that predates Block 177 and
# therefore carries NEITHER Block 177 artifact.  Read ONLY under the stale
# mutation, where the missing blobs are exactly what makes it bite.
STALE_PARENT_COMMIT = "63b865d02d37f89f5515adaf948e7e39a4392ecf"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_geometry_free_mirror",
    "claim_wrap_hypothesis",
    "break_shear_count",
    "claim_hop_classes_extent_free",
    "claim_transpose_convention_idle",
    "claim_forced_hermitianization",
    "claim_readout_unique",
    "break_interference_equality",
    "claim_contraction_proven_by_samples",
    "drop_corrections_record",
    "drop_sister_lane_citation",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_geometry_free_mirror": "C",
    "claim_wrap_hypothesis": "C",
    "break_shear_count": "C",
    "claim_hop_classes_extent_free": "D",
    "claim_transpose_convention_idle": "D",
    "claim_forced_hermitianization": "E",
    "claim_readout_unique": "E",
    "break_interference_equality": "F",
    "claim_contraction_proven_by_samples": "F",
    "drop_corrections_record": "G",
    "drop_sister_lane_citation": "G",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print("GATES " + " ".join(
            f"{key}={'PASS' if value else 'FAIL'}"
            for key, _, value in self.results))

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


def raw_note() -> tuple:
    """(text, at_final_path).  The fallback is DECLARED and never hidden."""
    try:
        return NOTE_PATH.read_text(encoding="utf-8"), True
    except OSError:
        pass
    try:
        return DRAFT_NOTE_PATH.read_text(encoding="utf-8"), False
    except OSError:
        return "", False


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def no_float(value: object) -> bool:
    """The committed exactness predicate, reached through the landed chain."""
    return b165.no_float(value)


# THE AST GATE'S READ SURFACE.  It covers EVERY FILE THIS RUNNER READS CODE FROM
# in the runner chain -- this file AND the imported runner modules -- which is
# the Block 176/177 convention.  IT IS NOT the full transitive module closure;
# gate A reports the residual count outside the surface rather than claiming the
# corpus clean.
def audit_source_paths() -> tuple:
    paths = [Path(__file__).resolve()]
    for module in (b177, b176, b175, b174, b171):
        if module is None:
            continue
        source = getattr(module, "__file__", None)
        if source:
            resolved = Path(source).resolve()
            if resolved not in paths:
                paths.append(resolved)
    return tuple(paths)


def source_float_literals() -> int:
    """AST self-check: NO float literal in ANY file read for code."""
    total = 0
    for path in audit_source_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        total += sum(1 for node in ast.walk(tree)
                     if isinstance(node, ast.Constant)
                     and isinstance(node.value, float))
    return total


BANNED_CALLS = ("nsim" + "plify", "evalf", "Fl" + "oat", "RealNumber")
_NS = BANNED_CALLS[0]


def source_forbidden_calls() -> int:
    """AST self-check: no nsimplify, no evalf, no Float in ANY such file."""
    banned = set(BANNED_CALLS)
    total = 0
    for path in audit_source_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        total += sum(1 for node in ast.walk(tree)
                     if (isinstance(node, ast.Attribute) and node.attr in banned)
                     or (isinstance(node, ast.Name) and node.id in banned))
    return total


def call_sites(text: str) -> int:
    """LIVE CALL SITES, not text mentions."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return -1
    return sum(1 for node in ast.walk(tree)
               if (isinstance(node, ast.Attribute) and node.attr == _NS)
               or (isinstance(node, ast.Name) and node.id == _NS))


def residue_report() -> dict:
    """The hygiene residue below the audit surface, COUNTED and never hidden."""
    chain = {}
    for name, module in (("b177", b177), ("b176", b176), ("b175", b175),
                         ("b174", b174), ("b171", b171), ("b170", b170),
                         ("b165", b165)):
        source = getattr(module, "__file__", None) if module is not None else None
        if source:
            text = Path(source).read_text(encoding="utf-8")
            chain[name] = (text.count(_NS), call_sites(text))
        else:
            chain[name] = (-1, -1)
    return {
        "per_module": chain,
        "call_sites_in_audit_surface": sum(
            chain[name][1] for name in ("b177", "b176", "b175", "b174", "b171")),
        "call_sites_below_audit_surface": sum(
            chain[name][1] for name in ("b170", "b165")),
    }


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    parent_import_landed: bool
    residue: dict


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
        # THE STALE LEG.  At the Block 176 tip NEITHER Block 177 artifact
        # exists, so this is False and the stale mutation fails gate A.
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        PARENT_IMPORT_LANDED,
        residue_report())


# ---------------------------------------------------------------------------
# the 178-specific layer
# ---------------------------------------------------------------------------
NUMERALS: list = []


def record(value):
    """Every reported numeral passes through here for the no-float gate."""
    NUMERALS.append(value)
    return value


COVER_EXTENTS = (("8x4", 8, 4), ("12x4", 12, 4))
EXTENT_NAMES = ("8x4", "12x4")
AMBIENT_SIGMA = R(3, 5)
A_MODULUS = R(25, 16)
B_MODULUS = R(-15, 16)
OFF_VALUE = R(15, 64)
DIAG_VALUE = R(9, 64)
PINNED_LEVELS = (0, 1)
VOLUME_PROFILE = (1, 2, 3, 4)
VOLUME_DIAGONAL = (R(25, 16), R(3, 2), R(17, 8), R(17, 6))
ON_DIAL = R(1, 4)
REGION_DIAL = Z0
RUNTIME_BUDGET_SEC = 150
DEEP_RUNTIME_BUDGET_SEC = 900
POOL_TWO_LEADS = 3
HANDOFF_ITEMS = 3

# THE IMPOSED OBJECTS OF THIS BLOCK, declared as a literal so the banner is a
# measured object and not only prose.  NONE of them is registered or adopted.
IMPOSED_OBJECTS = (
    "the antiunitary reflection Theta phi = r conj(phi) on the committed descended involution r, with its invariance condition r Q r = Q^T",
    "the two invariance TESTS run side by side: the commutator test r X r - X and the transpose test r X r - X^T",
    "the four carrier profiles: flat zero shear, the reflection-symmetric volume profile (1,2,3,4)_x, ambient sigma = 3/5 at unit volume, and the level-pinned shear carrier",
    "the two single-level probes: the pure b-modulus level and the PHYSICAL single-level shear that moves the a-modulus with it",
    "the hop-class map (min(dt,-dt) mod T_phys, min(dx,-dx) mod L_x) used to census the transport defect",
    "the interference objects: the record menu (0,1/5,2/5,3/5), the record cells (2,0) and (3,0), the holo_t dial and the readout weight 1/|det Q|^2",
    "the committed reflection, region pin, slice index set, menu, class map CM-SITE, slot order and record-slice scope, inherited",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE SCOPED READING.  It is measured that J != 0; the interference WORDS are an
# interpretation and are never gated as a theorem.
SCOPED_INTERPRETATIONS = (
    "THE INTERFERENCE READING: that transport IS record-record interference.  "
    "What is MEASURED is that the chosen |det Q|^-2 consistency defect RESPONDS "
    "to the holonomy dial (J != 0 exactly at both dial points).  The words are "
    "AN INTERPRETATION AT SCOPE, they are gated as note text and never as a "
    "theorem, and they establish neither the fork question nor any uniqueness",
)
# THE DECISION that belongs to the owner and is NOT taken here.
OWNER_DECISIONS = (
    "THE READOUT AXIOM: whether any composition/Born/readout axiom is ever "
    "supplied that would select one member of the fork-independent family -- it "
    "is ABSENT here and stays a PROPOSAL at the owner's bar",
)
# THE FOUR SUPERVISOR CORRECTIONS OF THIS ARC, carried verbatim-keyed.
SUPERVISOR_CORRECTIONS = (
    "THE WRAP HYPOTHESIS: that the reflection breaking was the antiperiodic "
    "wrap -- 'r is a reflection only locally; globally the fold's sign "
    "structure breaks it'.  WRONG AND OWNED: at zero shear the defect is "
    "exactly 0 under BOTH tests at BOTH extents",
    "THE PIN HYPOTHESIS: that the breaking was dial-independent and not "
    "level-local.  WRONG AND OWNED: pinning the two region levels removes "
    "exactly their share, 64 -> 32 and 96 -> 64",
    "THE GEOMETRY-FREE SLOGAN: 'the mirror-symmetric sector is exactly the "
    "geometry-free sector'.  REFUTED by the exact volume counterexample "
    "(1,2,3,4)_x and REPLACED BY: SHEARS BREAK THE MIRROR; VOLUMES DO NOT",
    "THE FORCED-FORK AND UNIQUENESS CLAIM: that non-invariance FORCES herm() "
    "and makes |Z|^2 THE UNIQUE fork-independent positive sensitive window.  "
    "REFUTED: it blocks a CANONICAL reconstruction only, and the readout sits "
    "in a FAMILY",
)
# THE THREE FURTHER STATEMENTS THE CROSS-MODEL CHECK CORRECTED.
FURTHER_CORRECTIONS = (
    "THE COVARIANCE CONVENTION: r Q r = Q^T, not r Q r = Q",
    "THE PER-LEVEL ADDITIVE LAW: a physical shear level contributes 24 entries "
    "and not 16, because the a-modulus moves too",
    "THE HOP-CLASS AND EXTENT-SCALING STORY: the full s_t support is three "
    "classes, and 16 -> 64/72 is an 8x4 census and not a scaling law",
)

# ---------------------------------------------------------------------------
# THE EXACT LITERALS.  Every one is recomputed in the measurement pass and
# compared here; none is a certificate the note asserts about itself.
# ---------------------------------------------------------------------------
AMBIENT_COUNTS = {"8x4": 64, "12x4": 96}
PINNED_COUNTS = {"8x4": 32, "12x4": 64}
B_LEVEL_COUNT = 16
PHYSICAL_LEVEL_COUNT = 24
PHYSICAL_OFF_COUNT = 16
PHYSICAL_DIAG_COUNT = 8
B_LEVEL_BLOCKS = {(0, 1): 4, (1, 0): 4, (1, 2): 4, (2, 1): 4}
PHYSICAL_DIAG_BLOCKS = ((0, 0), (2, 2))
TRANSPORT_DIALS = ((AMBIENT_SIGMA, Z0), (Z0, R(1, 2)), (AMBIENT_SIGMA, R(1, 2)))
LINEARITY_DIALS = ((AMBIENT_SIGMA, Z0), (Z0, R(1, 2)), (AMBIENT_SIGMA, R(1, 2)),
                   (R(2, 7), -R(1, 3)))
COMMUTATOR_COUNTS = {"8x4": (16, 64, 72), "12x4": (32, 96, 112)}
TRANSPOSE_COUNTS = {"8x4": (16, 64, 72), "12x4": (24, 104, 116)}
SX_CENSUS = {"8x4": {(1, 0): 8, (1, 2): 8}, "12x4": {(1, 0): 16, (1, 2): 16}}
ST_CENSUS = {"8x4": {(0, 1): 16, (1, 0): 32, (2, 1): 16},
             "12x4": {(0, 1): 16, (1, 0): 48, (2, 1): 32}}
FLAT_TRANSPOSE_COUNTS = {"8x4": 16, "12x4": 24}
OVERLAP_SLOTS = {"8x4": 8, "12x4": 16}

# THE INTERFERENCE ARM's committed scope, inherited from the landed machinery.
ARM_TAG = "12x4"
ARM_COVER_T = 12
ARM_LX = 4
MENU = (Z0, R(1, 5), R(2, 5), R(3, 5))
FIRST_CELL = (2, 0)
SECOND_CELL = (3, 0)
ARM_MODE = "xgraded"
DIAL_OFF = (Z0, Z0)
DIAL_QUARTER = (Z0, R(1, 4))
RAY_DIRECTION = (R(1, 3), R(1, 4))
RAY_LAMBDAS = (R(1, 2), R(1, 4), R(1, 8))
BRACKET_DEN = 10 ** 12
ARM_SIGNS = (1, 1, -1, -1)
ARM_GATE_COUNT = 18
# The exact L1 brackets of the independent route along lambda*(1/3,1/4).  They
# are DISJOINT AND ORDERED, which is what proves the strict three-point chain.
RAY_BRACKETS = {
    R(1, 2): (R(181601231, 125000000000), R(1452809849, 1000000000000)),
    R(1, 4): (R(739880333, 1000000000000), R(369940167, 500000000000)),
    R(1, 8): (R(366622121, 1000000000000), R(183311061, 500000000000)),
}
# The exact |J| brackets at (0, 1/4), and the J_0 digit lengths.
J_BRACKETS = (
    (R(123118943, 125000000000), R(196990309, 200000000000)),
    (R(219747537, 500000000000), R(17579803, 40000000000)),
    (R(54078193, 200000000000), R(135195483, 500000000000)),
    (R(1154055653, 1000000000000), R(577027827, 500000000000)),
)
J0_NUMERATOR_DIGITS = 2299
J0_DENOMINATOR_DIGITS = 2302
# THE EMBEDDED REDUCED RATIONAL that the independent raw-Hodge-before-quotient
# route printed for J_0(0, 1/4).  It is compared AS INTEGERS, never as decimals.
J0_NUMERATOR = sp.Integer(5273126007990941016699967016387983999802371082442320972171704045908460037160777695841836543970815209490915675409942019395893426326095664233049325379353946641645238010784412028733529062818152146424211512661966941813292825831500473448839976375191197478450105057235558497182372338737357127420830319560458399239915399353659271871497048839264153018015218234120406458086905215260639843487794930067279095120758187280844533015633372374679663818899845921082275971153493212943164635398340502376247431723483121034636115940781095171254999582731662338494523186428710426469120980693527789767123020982185775634129762633168535692205733457731103987099080916295142126422015173560126615967728118280323798126870477732977188618404425679543652566269779509624891729215877835188909151001162671957397902683186991556294678476465962969730730067900304970636127355993401801468278676499878114986924945068092563122520574569646885582178590956574884831105871749809029535117291727359165158467084960869969406265495327019910145080421023789518063519835677783870480533017262599641109672957025361734050185594871070865706881763302141312276559870556095861713080796940822509558184483982068394731711552215664322910677502898659177912566440265405260646825115887156322444553149145611252078273186075076597553690522611856041597579654773636408389232570142500499613292261037033573847933304310780120898459605785750472777634048968127934657225006315657724057559575374620880599062957388390507713159430162180317169302479553709547732655208391817979331516307764377948915413421310005938271880242218198030027037210393271110711358417248202010722143591175259083494207590109660804523399171981466144507173330743228024028244848512464112781525862600802659834567369432907213368684069395377800818924268262033812336045848280447149268664505334533505153803474236297276428449592781893049557770575334885739501017361589792443064800982176054992570495497307403743673984656619203449370152953997258673844690607207392688667856011584205368765005820458483884320165891975234726552767186127933692027858134271494052655298261070812632812882671454765537024530514266187747370859363950929190369456756120246961161357002674348386201027361300618907006526476604795458216721160500058855914683056131019705600938516306044131275791702866863161208079788821436950171412986226224042110036869120000)
J0_DENOMINATOR = sp.Integer(5353690782934039795282087517020364328647085034778604700990420443052953624046487866372527665839263872566825358620886120515244162861398662228572732237402602981656532279393098606504263636363879299081224517423133108241673772772973599775950866049405184698822549147280536247569652083575088659042402981197525480727376259467524411971685998881088246103771132756837657588949916569974273964463030531118129163903279259039496297147564571280792318779044336777468454140146741004507394406717940257089799473660816446737513535811099194643937225230015492110493189354656087055293734704522023244150620165895456667728082187174218018018159515942514700184458779358099823564957200468265934056380810010598096987313782962366959320096852151354060747277022741674531622486101248838279373170192723280936904402863382565485663207820277756084055663282005442305284637726518963953233538138394432672727430793578800023894832817253284129107338800774253610712287092296157918307086827169024094917817872417630399642697104474912825431719753706197760063419709070118844141720079719953028216739826075662014687533368014671537086174386279195505801840028554692131680877757893349019248183344433515529292371124696723147052239764786643253268886197932903149752103407389739259614639707419432595508187895608124097434239584288254999448570723309103720930863546898028541735598605822418872054131602482218049231989334587191588383233707611680456413655103687853294136775854432273706513280686698334810825163427228561348321824515281754043416940876127956866669881099138398127195543029663176638463165880609895012044421326670194478304963603649557078441473079890053946102243309787102753807218029851160768456298116109467749979779694922184651998466380343486177550647371139734398076675133313945207425596516097713281804141026659605193003494420142213414309726678766476948266114920511237943841794601483270443802997628293679606543077009113075693693345837854510748111513259695234456047808848096190145632330983969243991868086554919041155926095877392141075362286573685192005235706381737587552891249475676245046136710837662850180984975581580115914472296702743882394308553406580448679337092400047813184983648946251166540348485259922836686007855671854630596405330644937038967513147979049057686436120444200453763674664825840885868495244117705669756552433979935511972142670446504142169)
J0_VALUE = R(J0_NUMERATOR, J0_DENOMINATOR)


# ---------------------------------------------------------------------------
# the shared exact instruments
# ---------------------------------------------------------------------------
def carrier_field(bench, shear_of, volume_of) -> dict:
    """(shear, volume) at every committed cell, from two pure functions."""
    return {(t, x): (sp.sympify(shear_of(t, x)), sp.sympify(volume_of(t, x)))
            for (t, x) in bench.fx.CELLS}


def hodge_from(bench, field: dict) -> sp.Matrix:
    """H = dense(quotient(H_free|field)) -- the committed quotient Hodge action."""
    sub = b166.carrier_substitution(bench.fx, field)
    return sp.expand(dense(bench.fx.quotient(b166.ssubs(bench.fx.H_free, sub)),
                           bench.N, bench.N))


def hodge_from_moduli(bench, sub: dict) -> sp.Matrix:
    """H from an EXPLICIT modulus substitution -- the pure b-modulus probe."""
    return sp.expand(dense(bench.fx.quotient(b166.ssubs(bench.fx.H_free, sub)),
                           bench.N, bench.N))


def connection_from(bench, field: dict) -> sp.Matrix:
    """K = dense(quotient_connection(edge_d, H_free|field)), SYMBOLIC in s_x, s_t."""
    sub = b166.carrier_substitution(bench.fx, field)
    hodge = b166.ssubs(bench.fx.H_free, sub)
    return sp.expand(dense(
        bench.fx.quotient_connection(bench.fx.edge_d[(0, 0)], hodge),
        bench.N, bench.N))


def commutator_defect(bench, matrix: sp.MatrixBase) -> sp.Matrix:
    """THE SUPERVISOR'S STATED TEST: r X r - X.  Reported, and corrected."""
    return sp.expand(bench.r * matrix * bench.r - matrix)


def transpose_defect(bench, matrix: sp.MatrixBase) -> sp.Matrix:
    """THE CORRECT ANTIUNITARY TEST: r X r - X^T."""
    return sp.expand(bench.r * matrix * bench.r - matrix.T)


def nnz(matrix: sp.MatrixBase) -> int:
    return sum(1 for entry in matrix if sp.expand(entry) != 0)


def value_set(matrix: sp.MatrixBase) -> frozenset:
    return frozenset(sp.expand(entry) for entry in matrix
                     if sp.expand(entry) != 0)


def block_census(bench, matrix: sp.MatrixBase) -> dict:
    """Nonzeros per (time block, time block) pair of the quotient site index."""
    counter: Counter = Counter()
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            if sp.expand(matrix[i, j]) != 0:
                counter[(i // bench.lx, j // bench.lx)] += 1
    return dict(sorted(counter.items()))


def hop_census(bench, matrix: sp.MatrixBase) -> dict:
    """(min(dt,-dt) mod T_phys, min(dx,-dx) mod L_x) census on quotient sites."""
    counter: Counter = Counter()
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            if sp.expand(matrix[i, j]) != 0:
                ti, xi = divmod(i, bench.lx)
                tj, xj = divmod(j, bench.lx)
                dt = (ti - tj) % bench.T
                dx = (xi - xj) % bench.lx
                counter[(min(dt, (-dt) % bench.T),
                         min(dx, (-dx) % bench.lx))] += 1
    return dict(sorted(counter.items()))


def support_slots(matrix: sp.MatrixBase) -> frozenset:
    return frozenset((i, j) for i in range(matrix.rows)
                     for j in range(matrix.cols)
                     if sp.expand(matrix[i, j]) != 0)


# ---------------------------------------------------------------------------
# C. THE MIRROR THEOREM
# ---------------------------------------------------------------------------
def measure_mirror() -> dict:
    """THE FOUR CARRIER PROFILES AND THE TWO SINGLE-LEVEL PROBES, both extents.

    BOTH invariance tests are run on every profile: the supervisor's commutator
    test r H r - H and the CORRECT transpose test r H r - H^T.  On these Hodge
    actions H is real symmetric, so the two agree here -- which is exactly the
    coincidence the convention correction is about, and it is MEASURED and not
    assumed.
    """
    out: dict = {}
    for name, cover_t, lx in COVER_EXTENTS:
        bench = Bench(f"b178-mirror-{name}", cover_t, lx)
        out[(name, "bench")] = bench
        out[(name, "N")] = bench.N
        out[(name, "T_phys")] = bench.T
        out[(name, "lx")] = bench.lx
        out[(name, "r_involution")] = is_zero(bench.r * bench.r
                                              - sp.eye(bench.N))

        # (1) THE ZERO-SHEAR FLAT CONTROL.
        flat = carrier_field(bench, lambda t, x: Z0, lambda t, x: ONE)
        h_flat = hodge_from(bench, flat)
        out[(name, "flat_is_identity")] = is_zero(h_flat - sp.eye(bench.N))
        out[(name, "flat_commutator")] = nnz(commutator_defect(bench, h_flat))
        out[(name, "flat_transpose")] = nnz(transpose_defect(bench, h_flat))

        # (2) THE VOLUME COUNTEREXAMPLE -- non-flat, reflection-symmetric.
        volumes = carrier_field(
            bench, lambda t, x: Z0,
            lambda t, x: sp.Integer(VOLUME_PROFILE[x % len(VOLUME_PROFILE)]))
        h_vol = hodge_from(bench, volumes)
        out[(name, "volume_diagonal")] = all(
            sp.expand(h_vol[i, j]) == 0
            for i in range(bench.N) for j in range(bench.N) if i != j)
        out[(name, "volume_profile")] = tuple(
            sp.expand(h_vol[i, i]) for i in range(bench.lx))
        out[(name, "volume_repeats")] = all(
            sp.expand(h_vol[k, k]) == VOLUME_DIAGONAL[k % bench.lx]
            for k in range(bench.N))
        out[(name, "volume_commutator")] = nnz(commutator_defect(bench, h_vol))
        out[(name, "volume_transpose")] = nnz(transpose_defect(bench, h_vol))
        out[(name, "volume_is_non_flat")] = sp.expand(
            h_vol - sp.eye(bench.N)) != sp.zeros(bench.N, bench.N)

        # (3) THE AMBIENT SHEAR FIELD, and (4) THE LEVEL-PINNED CARRIER.
        ambient = carrier_field(bench, lambda t, x: AMBIENT_SIGMA,
                                lambda t, x: ONE)
        h_amb = hodge_from(bench, ambient)
        d_amb = commutator_defect(bench, h_amb)
        out[(name, "ambient_count")] = nnz(d_amb)
        out[(name, "ambient_values")] = value_set(d_amb)
        out[(name, "ambient_transpose_count")] = nnz(
            transpose_defect(bench, h_amb))
        pinned = carrier_field(
            bench,
            lambda t, x: Z0 if t in PINNED_LEVELS else AMBIENT_SIGMA,
            lambda t, x: ONE)
        h_pin = hodge_from(bench, pinned)
        d_pin = commutator_defect(bench, h_pin)
        out[(name, "pinned_count")] = nnz(d_pin)
        out[(name, "pinned_values")] = value_set(d_pin)

        # (5) THE PURE b-MODULUS LEVEL.  a = nu = mu = 1 everywhere and b
        # nonzero on ONE time level: the shear-linear off-diagonal piece alone.
        moduli = {}
        for (t, x) in bench.fx.CELLS:
            moduli[bench.fx.NU[(t, x)]] = ONE
            moduli[bench.fx.MU[(t, x)]] = ONE
            moduli[bench.fx.A[(t, x)]] = ONE
            moduli[bench.fx.B[(t, x)]] = B_MODULUS if t == 0 else Z0
        h_blevel = hodge_from_moduli(bench, moduli)
        d_blevel = commutator_defect(bench, h_blevel)
        out[(name, "b_level_count")] = nnz(d_blevel)
        out[(name, "b_level_blocks")] = block_census(bench, d_blevel)
        out[(name, "b_level_values")] = value_set(d_blevel)

        # (6) THE PHYSICAL SINGLE-LEVEL SHEAR.  sigma = 3/5 on ONE level ALSO
        # forces a = 25/16 there, and the defect is 24 entries, not 16.
        one_level = carrier_field(
            bench, lambda t, x: AMBIENT_SIGMA if t == 0 else Z0,
            lambda t, x: ONE)
        h_level = hodge_from(bench, one_level)
        d_level = commutator_defect(bench, h_level)
        off_counter: Counter = Counter()
        diag_counter: Counter = Counter()
        diag_blocks = set()
        for i in range(d_level.rows):
            for j in range(d_level.cols):
                entry = sp.expand(d_level[i, j])
                if entry == 0:
                    continue
                if i // bench.lx == j // bench.lx:
                    diag_counter[entry] += 1
                    diag_blocks.add((i // bench.lx, j // bench.lx))
                else:
                    off_counter[entry] += 1
        out[(name, "level_count")] = nnz(d_level)
        out[(name, "level_blocks")] = block_census(bench, d_level)
        out[(name, "level_off_count")] = sum(off_counter.values())
        out[(name, "level_off_values")] = frozenset(off_counter)
        out[(name, "level_diag_count")] = sum(diag_counter.values())
        out[(name, "level_diag_values")] = frozenset(diag_counter)
        out[(name, "level_diag_blocks")] = tuple(sorted(diag_blocks))
        # THE MODULI THE PHYSICAL SHEAR FORCES, measured from the substitution.
        forced = b166.carrier_substitution(bench.fx, one_level)
        out[(name, "forced_a")] = sp.expand(forced[bench.fx.A[(0, 0)]])
        out[(name, "forced_b")] = sp.expand(forced[bench.fx.B[(0, 0)]])
    # THE TWO SUMMARY FLAGS the claim-bound legs read.
    out["zero_shear_defect_nonzero"] = any(
        out[(name, "flat_commutator")] != 0 or out[(name, "flat_transpose")] != 0
        for name in EXTENT_NAMES)
    out["volume_geometry_survives"] = all(
        out[(name, "volume_commutator")] == 0
        and out[(name, "volume_transpose")] == 0
        and out[(name, "volume_is_non_flat")]
        for name in EXTENT_NAMES)
    out["shear_breaks_mirror"] = all(
        out[(name, "ambient_count")] > 0 for name in EXTENT_NAMES)
    # THE ADDITIVE LAW, MEASURED FALSE: a physical level is not 16 entries.
    out["additive_level_law_holds"] = all(
        out[(name, "level_count")] == B_LEVEL_COUNT for name in EXTENT_NAMES)
    return out


# ---------------------------------------------------------------------------
# D. THE TRANSPORT LEG
# ---------------------------------------------------------------------------
def measure_transport(mirror: dict) -> dict:
    """DIAL LINEARITY, THE FULL CENSUSES, AND THE CONVENTION SPLIT."""
    out: dict = {}
    for name, _, _ in COVER_EXTENTS:
        bench = mirror[(name, "bench")]
        pinned = carrier_field(
            bench,
            lambda t, x: Z0 if t in PINNED_LEVELS else AMBIENT_SIGMA,
            lambda t, x: ONE)
        k_symbolic = connection_from(bench, pinned)
        out[(name, "k_symbols")] = tuple(sorted(
            str(s) for s in k_symbolic.free_symbols))

        def at(sx, st, matrix=k_symbolic):
            return sp.expand(matrix.subs({SX: sp.sympify(sx),
                                          ST: sp.sympify(st)}))

        unit_sx = commutator_defect(bench, at(ONE, Z0))
        unit_st = commutator_defect(bench, at(Z0, ONE))
        out[(name, "sx_census")] = hop_census(bench, unit_sx)
        out[(name, "st_census")] = hop_census(bench, unit_st)
        out[(name, "overlap_slots")] = len(
            support_slots(unit_sx) & support_slots(unit_st))
        linear = []
        for sx, st in LINEARITY_DIALS:
            defect = commutator_defect(bench, at(sx, st))
            linear.append(is_zero(
                defect - (sp.sympify(sx) * unit_sx + sp.sympify(st) * unit_st)))
        out[(name, "linearity")] = tuple(linear)
        out[(name, "linearity_all")] = all(linear)

        commutator = []
        transpose = []
        censuses = []
        for sx, st in TRANSPORT_DIALS:
            matrix = at(sx, st)
            commutator.append(nnz(commutator_defect(bench, matrix)))
            transpose.append(nnz(transpose_defect(bench, matrix)))
            censuses.append(hop_census(bench, commutator_defect(bench, matrix)))
        out[(name, "commutator_counts")] = tuple(commutator)
        out[(name, "transpose_counts")] = tuple(transpose)
        out[(name, "dial_censuses")] = tuple(censuses)
        out[(name, "nonzero_dials_fail_both")] = all(
            c > 0 and t > 0 for c, t in zip(commutator, transpose))

        # THE FLAT ZERO-SHEAR CONNECTION: real antisymmetric, PASSES the
        # commutator test, FAILS the transpose test.  This is the case that
        # makes the convention load-bearing, and it is measured.
        flat = carrier_field(bench, lambda t, x: Z0, lambda t, x: ONE)
        k_flat = sp.expand(connection_from(bench, flat).subs(
            {SX: AMBIENT_SIGMA, ST: Z0}))
        out[(name, "flat_k_real")] = all(
            sp.expand(sp.im(entry)) == 0 for entry in k_flat)
        out[(name, "flat_k_antisymmetric")] = is_zero(k_flat + k_flat.T)
        out[(name, "flat_k_commutator")] = nnz(commutator_defect(bench, k_flat))
        out[(name, "flat_k_transpose")] = nnz(transpose_defect(bench, k_flat))
    # THE TWO SUMMARY FLAGS the claim-bound legs read.
    out["censuses_extent_independent"] = (
        out[("8x4", "sx_census")] == out[("12x4", "sx_census")]
        and out[("8x4", "st_census")] == out[("12x4", "st_census")]
        and out[("8x4", "commutator_counts")]
        == out[("12x4", "commutator_counts")])
    out["tests_agree_everywhere"] = all(
        out[(name, "commutator_counts")] == out[(name, "transpose_counts")]
        and out[(name, "flat_k_commutator")] == out[(name, "flat_k_transpose")]
        for name in EXTENT_NAMES)
    return out


# ---------------------------------------------------------------------------
# E. THE OBSTRUCTION EXHIBIT AND THE FORK-INDEPENDENT FAMILY
# ---------------------------------------------------------------------------
def selected(bench, matrix: sp.MatrixBase) -> sp.Matrix:
    """[r X]_{S,S}: the committed selection WITHOUT the Hermitianization, so the
    raw non-Hermiticity of the reflected covariance is measurable."""
    prod = sp.expand(bench.r * matrix)
    rows = bench.rows
    out = sp.zeros(len(rows), len(rows))
    for a, i in enumerate(rows):
        for b, j in enumerate(rows):
            out[a, b] = prod[i, j]
    return sp.expand(out)


def measure_obstruction() -> dict:
    """THE NON-HERMITIAN RAW OS GRAM, and the FAMILY of fork-independent
    positives.

    The exhibit is the object the canonical reconstruction would need: the
    reflected covariance selection G = [r (Q^-1)^T]_SS.  It is MEASURED
    non-Hermitian on the committed fixture, which is exactly why the canonical
    OS Gram is unavailable from these data -- and exactly NOT a reason that any
    particular repair is forced.

    The family leg then exhibits FOUR readouts that are each a function of Q
    ALONE -- hence fork-independent by the lemma -- each positive and each
    dial-sensitive.  More than one such readout is all it takes to refute
    uniqueness-from-positivity-plus-sensitivity.
    """
    out: dict = {}
    bench = Bench("b178-obstruction-8x4", 8, 4)
    out["N"] = bench.N
    for dial in (ON_DIAL, REGION_DIAL):
        env = bench.carrier(st=dial)
        action = sp.expand(bench.Q.subs(env))
        inverse = sp.expand(action.inv(method="LU"))
        out[(dial, "inverse_residual_zero")] = is_zero(
            sp.expand(action * inverse) - sp.eye(bench.N))
        raw = selected(bench, inverse.T)
        out[(dial, "raw_cov_hermitian")] = is_zero(raw - raw.H)
        out[(dial, "herm_cov_hermitian")] = is_zero(herm(raw) - herm(raw).H)
        out[(dial, "raw_cov_defect")] = nnz(sp.expand(raw - raw.H))
        determinant = sp.expand(action.det(method="berkowitz"))
        hermitian = herm(action)
        out[(dial, "det")] = determinant
        out[(dial, "det_nonzero")] = determinant != 0
        out[(dial, "herm_det")] = sp.expand(hermitian.det(method="berkowitz"))
        out[(dial, "herm_inertia")] = tuple(
            b165.real_symmetric_inertia(hermitian))
        modulus = sp.cancel(sp.expand(determinant * sp.conjugate(determinant)))
        out[(dial, "modulus")] = modulus
        # THE FAMILY.  Each entry is a function of Q ALONE.
        out[(dial, "family")] = (
            sp.cancel(ONE / modulus),                       # |Z|^2 shape
            sp.cancel(ONE / modulus ** 2),                  # |Z|^4 shape
            sp.cancel(ONE / out[(dial, "herm_det")]),       # 1/det(herm Q)
            sp.cancel(ONE / sp.expand(
                (action.H * action).trace())),              # f(Q^dag Q)
        )
    out["family_size"] = len(out[(ON_DIAL, "family")])
    out["family_positive"] = all(
        sp.sign(value) == 1
        for dial in (ON_DIAL, REGION_DIAL) for value in out[(dial, "family")])
    out["family_sensitive"] = tuple(
        on != off for on, off in zip(out[(ON_DIAL, "family")],
                                     out[(REGION_DIAL, "family")]))
    out["family_all_sensitive"] = all(out["family_sensitive"])
    out["sensitive_family_size"] = sum(1 for v in out["family_sensitive"] if v)
    out["family_members_distinct"] = (
        len({sp.cancel(value) for value in out[(ON_DIAL, "family")]})
        == out["family_size"])
    # AND ONE MEMBER IS MEASURED DIAL-BLIND, WHICH IS DISCLOSED RATHER THAN
    # DROPPED: herm(Q) is s_t-FREE, because the transport part of Q is
    # anti-Hermitian, so 1/det(herm Q) is fork-independent and positive but does
    # NOT move on this dial.  It stays in the fork-independent family and it is
    # NOT counted in the sensitive sub-family.
    out["herm_det_dial_blind"] = (
        out[(ON_DIAL, "herm_det")] == out[(REGION_DIAL, "herm_det")])
    out["herm_is_dial_free"] = is_zero(
        herm(sp.expand(bench.Q.subs(bench.carrier(st=ON_DIAL))))
        - herm(sp.expand(bench.Q.subs(bench.carrier(st=REGION_DIAL)))))
    # THE MEASURED STATUS FLAG the uniqueness mutation bites on: more than one
    # POSITIVE, FORK-INDEPENDENT, DIAL-SENSITIVE readout exists.
    out["readout_is_unique"] = out["sensitive_family_size"] <= 1
    out["herm_positive_definite"] = all(
        out[(dial, "herm_inertia")][1] == 0
        and out[(dial, "herm_inertia")][2] == 0
        for dial in (ON_DIAL, REGION_DIAL))
    return out


# ---------------------------------------------------------------------------
# F. THE INTERFERENCE ARM
# ---------------------------------------------------------------------------
class Arm:
    """The composed holonomy-dialled record machinery, on landed pieces only.

    Records are written into the shear FIELD -- the landed b171.field, which is
    what the independent arm's own field builder reproduces -- and that field's
    carrier_substitution is applied to the landed Site.Q_holo_t.  Nothing about
    the composition is rebuilt here.
    """

    def __init__(self) -> None:
        self.site = Site(f"b178-arm-{ARM_TAG}", ARM_COVER_T, ARM_LX)
        self.fx = self.site.fx
        self.c = self.site.c

    def field(self, records: dict) -> dict:
        return b171.field(self.fx, self.c, b171.CARRIER_SIGMA, ARM_MODE,
                          records)

    def substitution(self, records: dict) -> dict:
        sub = b166.carrier_substitution(self.fx, self.field(records))
        sub[SX] = b171.BENCH_SX
        sub[ST] = Z0
        sub[MASS] = b171.BENCH_MASS
        return sub

    def q(self, records: dict, gre, gim) -> sp.Matrix:
        return sp.expand(self.site.Q_holo_t.subs(self.substitution(records))
                         .subs({b171.GRE: sp.sympify(gre),
                                b171.GIM: sp.sympify(gim)}))


def det_berkowitz(matrix: sp.MatrixBase):
    """Berkowitz determinant over the inferred EXACT coefficient domain."""
    domain_matrix = DomainMatrix.from_Matrix(matrix)
    coefficients = domain_matrix.charpoly()
    return sp.expand((-ONE) ** matrix.rows
                     * domain_matrix.domain.to_sympy(coefficients[-1]))


def norm2(value):
    return sp.cancel(sp.expand(value * sp.conjugate(value)))


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, Z0))
    return tuple(sp.cancel(value / total) for value in values)


def bracket_abs(value) -> tuple:
    scaled = sp.Abs(sp.cancel(value)) * BRACKET_DEN
    return (R(sp.floor(scaled), BRACKET_DEN), R(sp.ceiling(scaled), BRACKET_DEN))


def l1(values: tuple):
    return sp.cancel(sum((sp.Abs(value) for value in values), Z0))


def interference(arm: Arm, gre, gim) -> dict:
    """The four one-cell and sixteen joint EXACT weights at one dial point."""
    determinants = []
    one_raw = []
    for a in MENU:
        determinant = det_berkowitz(arm.q({FIRST_CELL: a}, gre, gim))
        determinants.append(determinant)
        one_raw.append(sp.cancel(ONE / norm2(determinant)))
    p_one = normalize(tuple(one_raw))
    joint_raw = {}
    for a in MENU:
        for b in MENU:
            determinant = det_berkowitz(
                arm.q({FIRST_CELL: a, SECOND_CELL: b}, gre, gim))
            determinants.append(determinant)
            joint_raw[(a, b)] = sp.cancel(ONE / norm2(determinant))
    total = sp.cancel(sum(joint_raw.values(), Z0))
    m_joint = tuple(sp.cancel(
        sum((joint_raw[(a, b)] for b in MENU), Z0) / total) for a in MENU)
    defect = tuple(sp.cancel(m - p) for m, p in zip(m_joint, p_one))
    return {
        "i": defect,
        "determinants_nonzero": all(value != 0 for value in determinants),
        "normalization_nonzero": total != 0,
        "p_normalized": sp.cancel(sum(p_one, Z0)) == ONE,
        "m_normalized": sp.cancel(sum(m_joint, Z0)) == ONE,
        "sum_zero": sp.cancel(sum(defect, Z0)) == Z0,
    }


def measure_arm(deep: bool) -> dict:
    """I_off, J at (0,1/4), and the three-lambda contraction chain.

    THE SAMPLING IS DECLARED.  At baseline the two load-bearing dial points are
    recomputed exactly and the three ray brackets are gated as EXACT RATIONAL
    ARITHMETIC on the independent route's published brackets -- disjointness and
    order, which is what proves the strict chain.  Under --deep the three ray
    points are RECOMPUTED here and matched against those brackets.
    """
    out: dict = {}
    arm = Arm()
    witness = {FIRST_CELL: R(1, 5), SECOND_CELL: R(2, 5)}
    # THE COMPOSITION GATE, at the trivial dial.
    composed = arm.q(witness, *DIAL_OFF)
    out["composed_shape"] = tuple(composed.shape)
    out["composed_symbol_free"] = not composed.free_symbols
    reference = sp.expand(arm.site.bench.Q.subs(arm.substitution(witness)))
    out["composition_equals_reference"] = is_zero(composed - reference)
    out["field_matches_landed"] = (
        arm.field(witness)[FIRST_CELL][0] == R(1, 5)
        and arm.field(witness)[SECOND_CELL][0] == R(2, 5)
        and arm.field({})[FIRST_CELL][0] == b171.CARRIER_SIGMA)
    out["route_agrees"] = (det_berkowitz(composed)
                           == sp.expand(composed.det(method="berkowitz")))

    off = interference(arm, *DIAL_OFF)
    out["i_off"] = off["i"]
    out["i_off_gates"] = bool(
        off["determinants_nonzero"] and off["normalization_nonzero"]
        and off["p_normalized"] and off["m_normalized"] and off["sum_zero"])
    out["i_off_signs"] = tuple(int(sp.sign(value)) for value in off["i"])
    # THE LANDED BLOCK 176 LITERALS, reached through the import and not copied.
    if b176 is not None:
        baseline = tuple(R(value, b176.I0_DENOMINATOR)
                         for value in b176.I0_NUMERATORS)
        out["baseline_available"] = True
    else:                                                  # pragma: no cover
        baseline = ()
        out["baseline_available"] = False
    out["i_off_matches_landed"] = bool(baseline) and off["i"] == baseline

    current = interference(arm, *DIAL_QUARTER)
    response = tuple(sp.cancel(a - b) for a, b in zip(current["i"], off["i"]))
    out["j"] = response
    out["j_gates"] = bool(
        current["determinants_nonzero"] and current["normalization_nonzero"]
        and current["p_normalized"] and current["m_normalized"]
        and current["sum_zero"])
    out["j_signs"] = tuple(int(sp.sign(value)) for value in response)
    out["j_all_nonzero"] = all(value != 0 for value in response)
    out["j_sum_zero"] = sp.cancel(sum(response, Z0)) == Z0
    out["j_brackets"] = tuple(bracket_abs(value) for value in response)
    out["j0"] = response[0]
    out["j0_digits"] = (len(str(sp.numer(response[0]))),
                        len(str(sp.denom(response[0]))))
    out["l1_bracket"] = bracket_abs(l1(response))

    # THE CONTINUITY INGREDIENTS, MEASURED: every determinant and every
    # normalization at the trivial dial is nonzero, so no denominator of the
    # rational family vanishes at lambda = 0.  That -- with J(0) = 0 -- is the
    # PROOF of the limit; the three ray points are corroboration.
    out["denominators_nonzero_at_zero"] = bool(
        off["determinants_nonzero"] and off["normalization_nonzero"])
    # AND THE DIAL ENTERS THE ACTION AFFINELY, which is what makes every
    # determinant a POLYNOMIAL in the dial and every weight RATIONAL in it.
    dialled = arm.site.Q_holo_t
    out["dial_enters_affinely"] = bool(
        is_zero(sp.diff(dialled, b171.GRE, 2))
        and is_zero(sp.diff(dialled, b171.GIM, 2))
        and is_zero(sp.diff(sp.diff(dialled, b171.GRE), b171.GIM)))

    # THE THREE-LAMBDA CHAIN.  The brackets are disjoint and ordered, which is
    # an EXACT RATIONAL fact and is what proves the strict chain.
    brackets = tuple(RAY_BRACKETS[value] for value in RAY_LAMBDAS)
    half, quarter, eighth = brackets
    out["ray_brackets"] = brackets
    out["ray_brackets_ordered"] = bool(
        eighth[1] < quarter[0] and quarter[1] < half[0])
    out["ray_brackets_well_formed"] = all(lo < hi for lo, hi in brackets)
    out["strict_chain"] = out["ray_brackets_ordered"]
    if deep:
        recomputed = []
        for lam in RAY_LAMBDAS:
            point = (sp.cancel(lam * RAY_DIRECTION[0]),
                     sp.cancel(lam * RAY_DIRECTION[1]))
            here = interference(arm, *point)
            resp = tuple(sp.cancel(a - b) for a, b in zip(here["i"], off["i"]))
            recomputed.append(bracket_abs(l1(resp)))
        out["deep_ray"] = tuple(recomputed)
        out["deep_ray_agrees"] = tuple(recomputed) == brackets
    else:
        out["deep_ray"] = ()
        out["deep_ray_agrees"] = None
    return out


# ---------------------------------------------------------------------------
# the scope-key certificate
# ---------------------------------------------------------------------------
SCOPE_KEYS = (
    # --- N0 ---------------------------------------------------------------
    "convention_banner",
    "convention_hazard_order",
    "convention_collision_named",
    "convention_literal_collision",
    "neither_helper_wrong",
    "imposed_object_banner",
    "nothing_registered",
    "measured_never_registered",
    "nothing_adopted",
    "owner_bar",
    "proposals_stay_proposals",
    "interpretation_at_scope",
    "interpretation_never_theorem",
    # --- W1 ---------------------------------------------------------------
    "w1",
    "campaign_thesis",
    "parent_block",
    "parent_pr",
    "grandparent_pr",
    "open_gates_content",
    "measure_level_story",
    # --- N1 ---------------------------------------------------------------
    "shear_mirror_theorem",
    "shears_break_volumes_do_not",
    "antiunitary_condition",
    "commutator_convention_quoted",
    "coincide_only_real_symmetric",
    "zero_shear_control",
    "volume_counterexample",
    "volume_profile_values",
    "geometry_free_slogan_refuted",
    "ambient_counts",
    "pinned_counts",
    "shear_value",
    "single_level_sixteen",
    "single_level_twentyfour",
    "diagonal_value",
    "additive_law_refuted",
    "profile_specific_cancellations",
    # --- N2 ---------------------------------------------------------------
    "transport_leg",
    "dial_linearity",
    "linearity_matrixwise",
    "hop_class_map",
    "census_8x4_sx",
    "census_8x4_st",
    "census_12x4_sx",
    "census_12x4_st",
    "counts_8x4",
    "counts_12x4",
    "scaling_story_refuted",
    "transpose_counts_12x4",
    "flat_real_antisymmetric",
    "convention_load_bearing",
    "every_nonzero_dial_fails_both",
    # --- N3 ---------------------------------------------------------------
    "forced_fork_quoted",
    "forced_fork_refuted",
    "canonical_reconstruction_blocked",
    "reflected_covariance_non_hermitian",
    "not_forced_hermitianization",
    "fork_genuine",
    "shear_scope_antecedent",
    # --- N4 ---------------------------------------------------------------
    "fork_independence_lemma",
    "z_squared_form",
    "convergence_domain",
    "family_not_unique",
    "family_members",
    "readout_axiom_absent",
    "dial_blind_member_disclosed",
    "sister_lane_cited",
    "landed_withdrawals",
    # --- N5 ---------------------------------------------------------------
    "n5_verbatim",
    # --- N6 ---------------------------------------------------------------
    "interference_arm",
    "composition_gate",
    "trivial_dial_gate",
    "i_off_reproduces",
    "signs_pattern",
    "j_nonzero",
    "j_digits",
    "three_lambda_chain",
    "lambda_brackets",
    "rational_continuity",
    "samples_superseded",
    "prediction_confirmed",
    "defect_responds_to_dial",
    "arm_eighteen_gates",
    # --- N7 ---------------------------------------------------------------
    "corrections_record",
    "wrap_hypothesis_owned",
    "pin_hypothesis_owned",
    "geometry_free_slogan_listed",
    "forced_fork_listed",
    "process_working",
    "three_further_corrections",
    "checker_credited",
    # --- N8 ---------------------------------------------------------------
    "verdict",
    "successor_question",
    "cycle913_caution",
    "non_supply_never_necessity",
    "candidacy_never_nature",
    "worker_profile",
    "supervisor_inline_science",
    "codex_refute_check",
    "checker_overrides",
    "opus_mechanical_only",
    "common_mode",
    "two_extents",
    "not_re_verified",
    "not_continuum",
    "os_no_go",
    "not_a_born_derivation",
    "not_a_fock_construction",
    "no_priority_claim",
    "n1_n8",
    "ast_surface_disclosed",
    "no_float",
    "scope_key_certificate",
    "no_volume_average",
    "rho_guard",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "axiom",
    "campaign_cited",
)

# THE CORRECTIONS RECORD's own required subset, which is what gate G reads and
# what the two drop mutations remove a member of.
CORRECTION_KEYS = (
    "corrections_record",
    "wrap_hypothesis_owned",
    "pin_hypothesis_owned",
    "geometry_free_slogan_listed",
    "forced_fork_listed",
    "process_working",
    "three_further_corrections",
    "checker_credited",
    "sister_lane_cited",
)


def scope_certificate(note_text: str) -> dict:
    note = normalized_note(note_text)
    return {
        # --- N0 ---------------------------------------------------------------
        "convention_banner": "(n_+, n_-, n_0)" in note,
        "convention_hazard_order": "(n_+, n_0, n_-)" in note,
        "convention_collision_named": "congruence_inertia" in note
        and "real_symmetric_inertia" in note,
        "convention_literal_collision": "(4,4,0)" in note,
        "neither_helper_wrong": "neither helper is wrong" in note,
        "imposed_object_banner": "imposed measured object" in note,
        "nothing_registered": "nothing here is registered" in note,
        "measured_never_registered": "measured" in note
        and "never registered" in note,
        "nothing_adopted": "nothing is adopted" in note,
        "owner_bar": "the owner's bar" in note,
        "proposals_stay_proposals": "proposals stay proposals" in note,
        "interpretation_at_scope": "an interpretation at scope" in note,
        "interpretation_never_theorem": "never as a theorem" in note,
        # --- W1 ---------------------------------------------------------------
        "w1": __import__("re").search(r"\bw1\b", note) is not None,
        "campaign_thesis": "the campaign thesis" in note,
        "parent_block": "block 177" in note,
        "parent_pr": "#7331" in note,
        "grandparent_pr": "#7330" in note,
        "open_gates_content": "open-gates content" in note,
        "measure_level_story": "the campaign's measure-level story" in note,
        # --- N1 ---------------------------------------------------------------
        "shear_mirror_theorem": "the shear-mirror theorem" in note,
        "shears_break_volumes_do_not":
            "shears break the mirror; volumes do not" in note,
        "antiunitary_condition": "r q r = q^t" in note,
        "commutator_convention_quoted": "(rhr != h)" in note,
        "coincide_only_real_symmetric":
            "coincide only on real-symmetric controls" in note,
        "zero_shear_control": "0/0 at both extents" in note,
        "volume_counterexample": "(1,2,3,4)_x" in note,
        "volume_profile_values": "(25/16, 3/2, 17/8, 17/6)" in note,
        "geometry_free_slogan_refuted":
            "the mirror-symmetric sector is exactly the geometry-free sector"
            in note and "that is false" in note,
        "ambient_counts": "64 nonzero entries at 8x4 and 96 at 12x4" in note,
        "pinned_counts": "32 nonzero entries at 8x4 and 64 at 12x4" in note,
        "shear_value": "+-15/64" in note,
        "single_level_sixteen": "exactly 16 entries" in note,
        "single_level_twentyfour": "24 entries, not 16" in note,
        "diagonal_value": "+-9/64" in note,
        "additive_law_refuted":
            "the additive 16-per-level law is therefore refuted" in note,
        "profile_specific_cancellations":
            "profile-specific cancellations" in note,
        # --- N2 ---------------------------------------------------------------
        "transport_leg": "the transport leg" in note,
        "dial_linearity":
            "d_k(s_x, s_t) = s_x d_k(1,0) + s_t d_k(0,1)" in note,
        "linearity_matrixwise": "matrixwise" in note,
        "hop_class_map": "min(dt, -dt) mod t_phys" in note,
        "census_8x4_sx": "(1,0):8, (1,2):8" in note,
        "census_8x4_st": "(0,1):16, (1,0):32, (2,1):16" in note,
        "census_12x4_sx": "(1,0):16, (1,2):16" in note,
        "census_12x4_st": "(0,1):16, (1,0):48, (2,1):32" in note,
        "counts_8x4": "16 / 64 / 72" in note,
        "counts_12x4": "32 / 96 / 112" in note,
        "scaling_story_refuted":
            "not an extent-independent scaling law" in note,
        "transpose_counts_12x4": "24 / 104 / 116" in note,
        "flat_real_antisymmetric": "real antisymmetric" in note,
        "convention_load_bearing": "the convention is load-bearing" in note,
        "every_nonzero_dial_fails_both":
            "every nonzero transport dial fails both tests" in note,
        # --- N3 ---------------------------------------------------------------
        "forced_fork_quoted":
            "a fork the framework's own reflection-breaking forces" in note,
        "forced_fork_refuted": "that inference is refuted" in note,
        "canonical_reconstruction_blocked":
            "blocks the canonical reflection-positive hilbert reconstruction"
            in note,
        "reflected_covariance_non_hermitian":
            "non-hermitian and therefore unusable as an os gram" in note,
        "not_forced_hermitianization":
            "it does not force herm() specifically" in note,
        "fork_genuine": "remains a genuine fork" in note,
        "shear_scope_antecedent":
            "the correct antecedent is shear scope" in note,
        # --- N4 ---------------------------------------------------------------
        "fork_independence_lemma":
            "every function of q alone is fork-independent" in note,
        "z_squared_form": "|z|^2 = pi^(2n) / |det q|^2" in note,
        "convergence_domain": "herm(q) > 0" in note,
        "family_not_unique": "the uniqueness claim is withdrawn" in note,
        "family_members": "|z|^p" in note and "1/det(herm q)" in note,
        "readout_axiom_absent": "no such axiom is present here" in note,
        "dial_blind_member_disclosed":
            "is fork-independent and positive but dial-blind" in note,
        "sister_lane_cited": "#7325" in note,
        "landed_withdrawals":
            "block 176 and block 177 both withdrew uniqueness claims" in note,
        # --- N5 ---------------------------------------------------------------
        # Raw substring membership makes the printed fence byte-identical to its
        # note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
        # --- N6 ---------------------------------------------------------------
        "interference_arm": "the interference arm" in note,
        "composition_gate":
            "equals the landed reference matrix entry for entry" in note,
        "trivial_dial_gate": "(g_re, g_im) = (0,0)" in note,
        "i_off_reproduces":
            "reproduces the block 176 exact common-denominator literals" in note,
        "signs_pattern": "(+,+,-,-)" in note,
        "j_nonzero": "j != 0 exactly" in note,
        "j_digits": "2299-digit numerator over a 2302-digit denominator" in note,
        "three_lambda_chain":
            "l1(j at 1/8) < l1(j at 1/4) < l1(j at 1/2)" in note,
        "lambda_brackets": "181601231/125000000000" in note
        and "366622121/1000000000000" in note,
        "rational_continuity": "proven by rational continuity" in note,
        "samples_superseded":
            "the sample-based limit claim is superseded" in note,
        "prediction_confirmed": "the registered prediction is confirmed" in note,
        "defect_responds_to_dial": "responds to the holonomy dial" in note,
        "arm_eighteen_gates": "18 of 18 exact gates" in note,
        # --- N7 ---------------------------------------------------------------
        "corrections_record": "four supervisor corrections" in note,
        "wrap_hypothesis_owned": "the wrap hypothesis" in note
        and "wrong, owned" in note,
        "pin_hypothesis_owned": "the pin hypothesis" in note,
        "geometry_free_slogan_listed": "the geometry-free slogan" in note,
        "forced_fork_listed": "the forced-fork and uniqueness claim" in note,
        "process_working": "the process working" in note,
        "three_further_corrections":
            "three further statements of the solve" in note,
        "checker_credited": "the checker is credited" in note,
        # --- N8 ---------------------------------------------------------------
        "verdict":
            "the campaign's measure-level story is complete in corrected form"
            in note,
        "successor_question": "the successor question" in note,
        "cycle913_caution": "cycle913" in note,
        "non_supply_never_necessity":
            "non-supply within this formalism" in note
            and "never metaphysical necessity" in note,
        "candidacy_never_nature": "candidacy within this formalism" in note
        and "never a claim about nature" in note,
        "worker_profile": "worker profile" in note,
        "supervisor_inline_science": "all solve-side science" in note,
        "codex_refute_check": "codex 5.6-sol xhigh" in note,
        "checker_overrides":
            "override the solve everywhere they collide" in note,
        "opus_mechanical_only": "mechanical drafting only" in note,
        "common_mode": "common-mode" in note,
        "two_extents": "two extents" in note,
        "not_re_verified": "not re-verified" in note,
        "not_continuum": "not a continuum statement" in note,
        "os_no_go": "not an os no-go" in note,
        "not_a_born_derivation": "not a derivation of the born rule" in note,
        "not_a_fock_construction":
            "not a construction of a fock space" in note,
        # NEGATIVE key, inherited from Blocks 164-177.
        "no_priority_claim": ("first positive" not in note
                              and "novel" not in note
                              and "unprecedented" not in note
                              and "for the first time" not in note),
        "n1_n8": all(__import__("re").search(rf"\bn{index}\b", note) is not None
                     for index in range(1, 9)),
        "ast_surface_disclosed": "ast surface" in note,
        "no_float": "no float" in note,
        "scope_key_certificate": "scope-key certificate" in note,
        # NEGATIVE key, inherited from Blocks 164-177.
        "no_volume_average": "volume average" not in note,
        # The LaTeX rho guard: a line-wrapped \rho leaves a stray "ho_" at the
        # start of a line and silently mangles a modulus name.
        "rho_guard": "\nho_" not in note_text,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": ("no toe percentage moves" in note
                       or "no toe percentage movement" in note),
        "zero_e2e": "retained-positive end-to-end theory count remains zero"
        in note,
        "axiom": "no axiom amendment is justified" in note,
        "campaign_cited": "campaign_20260823_complex_structure" in note,
    }


N5_FENCE = 'N5: per_element: THE TWO BANNERS, FIRST AND WITH TEETH. THE INERTIA CONVENTION: every triple in this note is labelled and read in the (n_+, n_-, n_0) order of the LANDED Block 165 helper real_symmetric_inertia, while the landed b163/b164 helper congruence_inertia returns (n_+, n_0, n_-), measured on identical matrices, so THE LITERAL STRING (4,4,0) MEANS PSD in Block 164\'s landed fence and FULLY HYPERBOLIC here; NEITHER HELPER IS WRONG and no landed verdict changes. AND THE IMPOSED-OBJECT BANNER: NOTHING HERE IS REGISTERED OR ADOPTED -- the antiunitary reflection Theta phi = r conj(phi) and its invariance condition, the two invariance tests, the four carrier profiles, the two single-level probes, the hop-class map, the interference menu and record cells and holo_t dial and |det Q|^-2 weight, and the inherited reflection, region pin, slice index set, menu, class map CM-SITE, slot order and record-slice scope are IMPOSED MEASURED OBJECTS OF THIS BLOCK; AND THE INTERFERENCE READING IS AN INTERPRETATION AT SCOPE and never a theorem; NOTHING IS REGISTERED AND NOTHING IS ADOPTED.\nper_site: THE SHEAR-MIRROR THEOREM, AND THE CONVENTION IT NEEDED FIRST. For the antiunitary Theta phi = r conj(phi) the invariance condition on a quadratic form is r Q r = Q^T and NOT r Q r = Q -- the supervisor\'s commutator-only convention is QUOTED AND CORRECTED, and the two coincide only on real-symmetric controls. The zero-shear flat control is EXACTLY Theta-invariant at both extents under BOTH tests, 0/0. THE VOLUME COUNTEREXAMPLE: zero shear with nu(t,x) = (1,2,3,4)_x makes H diagonal, repeating (25/16, 3/2, 17/8, 17/6) on every time level, and BOTH defects vanish at BOTH extents -- so NON-FLAT REFLECTION-SYMMETRIC VOLUME GEOMETRY SURVIVES THE MIRROR and the slogan "the mirror-symmetric sector is exactly the geometry-free sector" is REFUTED AND REPLACED BY: SHEARS BREAK THE MIRROR; VOLUMES DO NOT.\nper_mode: THE SHEAR FIELD BREAKS THE MIRROR, AND THE PER-LEVEL LAW IS REFUTED. Ambient sigma = 3/5 at unit volume gives 64 nonzero entries at 8x4 and 96 at 12x4; pinning levels t = 0, 1 to zero shear leaves 32 and 64; every nonzero entry is +-15/64. A single b-modulus level contributes EXACTLY 16 entries, four each in the time blocks (0,1), (1,0), (1,2) and (2,1). BUT A PHYSICAL SINGLE-LEVEL SHEAR ALSO FORCES ITS a-MODULUS and contributes 24: the same 16 off-diagonal +-15/64 PLUS 8 diagonal +-9/64 in the blocks (0,0) and (2,2). THE ADDITIVE 16-PER-LEVEL LAW IS REFUTED and the ambient/pinned count identities are PROFILE-SPECIFIC CANCELLATIONS, stated as such.\nper_block: THE TRANSPORT LEG, WITH THE FULL CENSUSES AND THE CONVENTION SPLIT DISCLOSED. The reflection defect of the quotient connection is EXACTLY DIAL-LINEAR MATRIXWISE, D_K(s_x, s_t) = s_x D_K(1,0) + s_t D_K(0,1). At 8x4 the commutator counts are 16, 64 and 72 with s_x classes (1,0):8 and (1,2):8 and s_t classes (0,1):16, (1,0):32 and (2,1):16; at 12x4 they are 32, 96 and 112 with s_x classes (1,0):16 and (1,2):16 and s_t classes (0,1):16, (1,0):48 and (2,1):32 -- so the two-class story and the extent-scaling story are BOTH REFUTED. Under the correct transpose test the counts are 16, 64, 72 at 8x4 but 24, 104, 116 at 12x4, and at FLAT ZERO SHEAR K is real antisymmetric and PASSES the commutator test while FAILING the transpose test with 16 entries at 8x4 and 24 at 12x4 -- THE CONVENTION IS LOAD-BEARING AND DISCLOSED -- while EVERY NONZERO TRANSPORT DIAL FAILS BOTH.\nlattice_wide: THE OBSTRUCTION AT EXACTLY ITS STRENGTH, AND THE FORK-INDEPENDENT FAMILY. The supervisor\'s forced-fork inference is QUOTED AND REFUTED. What shear non-invariance does is BLOCK THE CANONICAL REFLECTION-POSITIVE HILBERT RECONSTRUCTION FROM THE FIXED DATA, because the reflected covariance selection G = [r (Q^-1)^T]_SS can be NON-HERMITIAN and therefore unusable as an OS Gram. IT DOES NOT FORCE herm() SPECIFICALLY NOR ANY PARTICULAR PRESCRIPTION -- degree grading, non-positive functionals, restriction, quotient, field doubling, a changed complex structure or reflection, an added positive form all remain -- so THE BLOCK-177 GRADING PREMISE REMAINS A GENUINE FORK, and the volume counterexample narrows the antecedent to SHEAR SCOPE. Every function of Q alone is fork-independent, so |Z|^2 = pi^(2N)/|det Q|^2 is positive and transport-sensitive there, BUT IT IS NOT UNIQUE: |Z|^p for every p > 0, positive functions of Q^dag Q and 1/det(herm Q) on its domain are the same kind of object, and UNIQUENESS WOULD REQUIRE A READOUT AXIOM THAT IS ABSENT HERE -- consistent with the landed Block 176 and Block 177 withdrawals and with the sister lane\'s #7325 countermodel.\nper_scope: THE INTERFERENCE ARM, MEASURED EXACTLY AND READ AT SCOPE. The composed holonomy-dialled record machinery is GATED AT THE TRIVIAL DIAL, where the 24x24 action equals the landed reference entry for entry; I_off reproduces the landed Block 176 baseline EXACTLY with signs (+,+,-,-) and sum zero; J != 0 EXACTLY at (0, 1/4) and at (1/3, 1/4) with signs (+,+,-,-); the (0, 1/4) entry is INDEPENDENTLY REVERIFIED to a 2299-digit-numerator-over-2302-digit-denominator REDUCED-RATIONAL EQUALITY by a raw-Hodge-before-quotient route; the strict three-point contraction chain at lambda = 1/2, 1/4, 1/8 holds on the disjoint exact brackets (181601231/125000000000, 1452809849/1000000000000), (739880333/1000000000000, 369940167/500000000000) and (366622121/1000000000000, 183311061/500000000000); and J -> 0 IS PROVEN BY RATIONAL CONTINUITY, all denominators being nonzero at lambda = 0, WHICH SUPERSEDES THE SAMPLE-BASED CLAIM. THE REGISTERED PREDICTION IS CONFIRMED, and the reading "transport is record-record interference" is carried as AN INTERPRETATION AT SCOPE: what is measured is that the chosen |det Q|^-2 consistency defect RESPONDS TO THE HOLONOMY DIAL.\nRESULT: THE SHEAR-MIRROR THEOREM AND THE INTERFERENCE ARM. SHEARS BREAK THE MIRROR; VOLUMES DO NOT -- the Theta-invariant sector contains all reflection-symmetric volume geometry and excludes shear geometry at both extents. THE CANONICAL RECONSTRUCTION IS BLOCKED AT SHEAR SCOPE and no prescription is forced, so THE BLOCK-177 GRADING PREMISE REMAINS A GENUINE FORK. THE VACUUM READOUT IS FORK-INDEPENDENT IN A FAMILY and uniqueness needs a readout axiom absent here. THE INTERFERENCE IS MEASURED and its reading is scoped. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is edited; no earlier block is corrected; the bar items stay PROPOSALS, and PROPOSALS STAY PROPOSALS. FOUR SUPERVISOR CORRECTIONS ARE CARRIED IN THIS ARC AND ALL FOUR ARE DISCLOSED AS THE PROCESS WORKING: the wrap hypothesis, the pin hypothesis, the geometry-free slogan and the forced-fork/uniqueness claim; and the cross-model check corrected three further statements -- the covariance convention, the per-level additive law and the hop-class/extent-scaling story -- with THE CHECKER CREDITED for the volume counterexample, the convention correction, the full censuses and the rational-continuity proof. THIS BLOCK\'S OWN DEFECTS ARE DISCLOSED: it is TWO EXTENTS and one interference bench with no ladder; the counts are profile-specific; the obstruction is a block on a canonical construction and NOT AN OS NO-GO; the readout is NOT UNIQUE; the interference reading is an INTERPRETATION AT SCOPE; and the AST surface is this runner plus the imported runner chain and NOT every landed module the chain reaches, with residual sites counted rather than claimed repaired. PROVENANCE: CAMPAIGN_20260823_COMPLEX_STRUCTURE.md sections B2b RESOLVED, B2b VERIFICATION COMPLETE and B178 CHECK VERDICTS, with b178check_findings.md and b178arm_findings.md preserved in generator-program-20260821/. HANDOFF: enumerate the non-canonical prescriptions; supply the readout axiom; find the composition law the interference reading would need.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.'


def build_claims(mutation: str) -> dict:
    claims: dict = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "objects_registered": False,
        "mirror_sector_geometry_free": False,
        "wrap_hypothesis": False,
        "ambient_shear_counts": (AMBIENT_COUNTS["8x4"], AMBIENT_COUNTS["12x4"]),
        "hop_classes_extent_free": False,
        "transpose_convention_idle": False,
        "forced_hermitianization": False,
        "readout_unique": False,
        "j0_literal": J0_VALUE,
        "contraction_proven_by_samples": False,
        "required_correction_keys": CORRECTION_KEYS,
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
    elif mutation == "claim_geometry_free_mirror":
        # THE REFUTED SLOGAN REASSERTED: the mirror sector asserted geometry-free,
        # which the exactly invariant (1,2,3,4)_x volume profile forbids.
        claims["mirror_sector_geometry_free"] = True
    elif mutation == "claim_wrap_hypothesis":
        # THE WRAP HYPOTHESIS REASSERTED: the breaking asserted present already at
        # zero shear, which the exact 0/0 control at both extents forbids.
        claims["wrap_hypothesis"] = True
    elif mutation == "break_shear_count":
        # THE AMBIENT COUNT BROKEN: a wrong count asserted at 8x4, which the
        # rebuilt Hodge defect forbids.
        claims["ambient_shear_counts"] = (65, AMBIENT_COUNTS["12x4"])
    elif mutation == "claim_hop_classes_extent_free":
        # THE EXTENT DEPENDENCE DENIED: the censuses asserted extent-free, which
        # 16/64/72 against 32/96/112 forbids.
        claims["hop_classes_extent_free"] = True
    elif mutation == "claim_transpose_convention_idle":
        # THE CONVENTION ASSERTED IDLE: the two tests asserted to agree
        # everywhere, which the flat zero-shear 0-versus-16/24 split forbids.
        claims["transpose_convention_idle"] = True
    elif mutation == "claim_forced_hermitianization":
        # THE REFUTED INFERENCE REASSERTED: herm() asserted FORCED, which this
        # block's scoped obstruction and its declared status flag forbid.
        claims["forced_hermitianization"] = True
    elif mutation == "claim_readout_unique":
        # THE UNIQUENESS REASSERTED: the readout asserted unique, which the
        # measured four-member fork-independent family forbids.
        claims["readout_unique"] = True
    elif mutation == "break_interference_equality":
        # THE REDUCED-RATIONAL EQUALITY BROKEN: a wrong exact rational asserted
        # for J_0(0,1/4), which the recomputed arm forbids.
        claims["j0_literal"] = sp.cancel(J0_VALUE + R(1, BRACKET_DEN))
    elif mutation == "claim_contraction_proven_by_samples":
        # THE PROOF ROUTE FALSIFIED: three sample points asserted to BE the
        # limit proof, which the rational-continuity argument supersedes.
        claims["contraction_proven_by_samples"] = True
    elif mutation == "drop_corrections_record":
        claims["required_correction_keys"] = tuple(
            key for key in CORRECTION_KEYS if key != "corrections_record")
    elif mutation == "drop_sister_lane_citation":
        claims["required_correction_keys"] = tuple(
            key for key in CORRECTION_KEYS if key != "sister_lane_cited")
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim")
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    deep: bool
    main_head: str
    authority: AuthorityCertificate
    note_at_final_path: bool
    scope: dict
    banners: dict
    mirror: dict
    transport: dict
    obstruction: dict
    arm: dict
    exact_no_float: bool
    source_files: int
    source_floats: int
    source_forbidden: int


EXPECTED_CONVENTION = (((4, 4, 0), (4, 0, 4)),
                       ((4, 0, 4), (4, 4, 0)),
                       ((0, 3, 0), (0, 0, 3)))


def evaluate_gates(facts: Facts, claims: dict, elapsed_ns: int) -> dict:
    authority = facts.authority
    parent_blobs_ok = (authority.parent_artifact_blobs
                       if claims["parent_pin"] == "resolved"
                       else authority.stale_parent_artifact_blobs)
    gate_a = bool(
        AUDIT_INPUT_PATHS == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md",
            "scripts/admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23.py",
            "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
            "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
        )
        and PARENT_ARTIFACTS == (BLOCK177_NOTE, BLOCK177_RUNNER)
        and len(PARENT_ARTIFACT_BLOBS) == len(PARENT_ARTIFACTS) == 2
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_import_landed
        and authority.parent_pin_is_commit
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
        # THE STALE PIN: a REAL ancestor of HEAD that carries NEITHER Block 177
        # artifact, which is exactly what makes the stale mutation bite.
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact)

    ban = facts.banners
    mir = facts.mirror
    gate_b = bool(
        # THE CONVENTION COLLISION, MEASURED on identical matrices.
        ban["convention"]["pairs"] == EXPECTED_CONVENTION
        and ban["convention"]["landed_psd"] and ban["convention"]["here_psd"]
        and ban["convention"]["orders_differ"]
        # THE IMPOSED-OBJECT BANNER and THE SCOPED READING, as measured objects.
        and ban["imposed_objects"] == 7
        and ban["registered_objects"] == 0
        and ban["adopted_objects"] == 0
        and ban["scoped_interpretations"] == 1
        and ban["owner_decisions"] == 1
        and ban["supervisor_corrections"] == 4
        and ban["further_corrections"] == 3
        and (ban["registered_objects"] == 0 and ban["adopted_objects"] == 0)
        == (not claims["objects_registered"])
        # BOTH BENCH ANCHORS, rebuilt through the LANDED Block 170 machinery.
        and mir[("8x4", "N")] == 16 and mir[("8x4", "T_phys")] == 4
        and mir[("12x4", "N")] == 24 and mir[("12x4", "T_phys")] == 6
        and mir[("8x4", "lx")] == 4 and mir[("12x4", "lx")] == 4
        and all(mir[(name, "r_involution")] for name in EXTENT_NAMES)
        and facts.exact_no_float
        and facts.source_floats == 0 and facts.source_forbidden == 0
        and facts.source_files >= 2)

    gate_c = bool(
        # THE ZERO-SHEAR FLAT CONTROL: identity, and 0/0 under BOTH tests.
        all(mir[(name, "flat_is_identity")] for name in EXTENT_NAMES)
        and all(mir[(name, "flat_commutator")] == 0 for name in EXTENT_NAMES)
        and all(mir[(name, "flat_transpose")] == 0 for name in EXTENT_NAMES)
        # THE VOLUME COUNTEREXAMPLE: non-flat, diagonal, level-repeating, and
        # EXACTLY invariant under BOTH tests at BOTH extents.
        and all(mir[(name, "volume_diagonal")] for name in EXTENT_NAMES)
        and all(mir[(name, "volume_is_non_flat")] for name in EXTENT_NAMES)
        and all(mir[(name, "volume_profile")] == VOLUME_DIAGONAL
                for name in EXTENT_NAMES)
        and all(mir[(name, "volume_repeats")] for name in EXTENT_NAMES)
        and all(mir[(name, "volume_commutator")] == 0 for name in EXTENT_NAMES)
        and all(mir[(name, "volume_transpose")] == 0 for name in EXTENT_NAMES)
        # THE SHEAR COUNTS, ambient and pinned, with the single value set.
        and (mir[("8x4", "ambient_count")], mir[("12x4", "ambient_count")])
        == tuple(claims["ambient_shear_counts"])
        and all(mir[(name, "pinned_count")] == PINNED_COUNTS[name]
                for name in EXTENT_NAMES)
        and all(mir[(name, "ambient_values")]
                == frozenset({OFF_VALUE, -OFF_VALUE}) for name in EXTENT_NAMES)
        and all(mir[(name, "pinned_values")]
                == frozenset({OFF_VALUE, -OFF_VALUE}) for name in EXTENT_NAMES)
        # THE 24-ENTRY SINGLE-LEVEL ACCOUNTING, with BOTH moduli.
        and all(mir[(name, "b_level_count")] == B_LEVEL_COUNT
                for name in EXTENT_NAMES)
        and all(mir[(name, "b_level_blocks")] == B_LEVEL_BLOCKS
                for name in EXTENT_NAMES)
        and all(mir[(name, "level_count")] == PHYSICAL_LEVEL_COUNT
                for name in EXTENT_NAMES)
        and all(mir[(name, "level_off_count")] == PHYSICAL_OFF_COUNT
                for name in EXTENT_NAMES)
        and all(mir[(name, "level_diag_count")] == PHYSICAL_DIAG_COUNT
                for name in EXTENT_NAMES)
        and all(mir[(name, "level_off_values")]
                == frozenset({OFF_VALUE, -OFF_VALUE}) for name in EXTENT_NAMES)
        and all(mir[(name, "level_diag_values")]
                == frozenset({DIAG_VALUE, -DIAG_VALUE})
                for name in EXTENT_NAMES)
        and all(mir[(name, "level_diag_blocks")] == PHYSICAL_DIAG_BLOCKS
                for name in EXTENT_NAMES)
        and all(mir[(name, "forced_a")] == A_MODULUS for name in EXTENT_NAMES)
        and all(mir[(name, "forced_b")] == B_MODULUS for name in EXTENT_NAMES)
        # THE ADDITIVE LAW, MEASURED FALSE.
        and not mir["additive_level_law_holds"]
        and mir["shear_breaks_mirror"]
        # THE TWO CLAIM-BOUND LEGS: the refuted slogan and the wrap hypothesis.
        and mir["volume_geometry_survives"]
        == (not claims["mirror_sector_geometry_free"])
        and mir["zero_shear_defect_nonzero"] == claims["wrap_hypothesis"]
        and facts.exact_no_float)

    tra = facts.transport
    gate_d = bool(
        # EXACT DIAL LINEARITY, MATRIXWISE, at four dial points per extent.
        all(tra[(name, "linearity_all")] for name in EXTENT_NAMES)
        and all(len(tra[(name, "linearity")]) == len(LINEARITY_DIALS)
                for name in EXTENT_NAMES)
        and all(tra[(name, "k_symbols")] == ("s_t", "s_x")
                for name in EXTENT_NAMES)
        # THE FULL HOP CENSUSES AND THE COUNTS, at BOTH extents.
        and all(tra[(name, "sx_census")] == SX_CENSUS[name]
                for name in EXTENT_NAMES)
        and all(tra[(name, "st_census")] == ST_CENSUS[name]
                for name in EXTENT_NAMES)
        and all(tra[(name, "commutator_counts")] == COMMUTATOR_COUNTS[name]
                for name in EXTENT_NAMES)
        and all(tra[(name, "transpose_counts")] == TRANSPOSE_COUNTS[name]
                for name in EXTENT_NAMES)
        and all(tra[(name, "overlap_slots")] == OVERLAP_SLOTS[name]
                for name in EXTENT_NAMES)
        # THE FLAT ZERO-SHEAR CASE: real antisymmetric, PASSES the commutator
        # test, FAILS the transpose test.
        and all(tra[(name, "flat_k_real")] for name in EXTENT_NAMES)
        and all(tra[(name, "flat_k_antisymmetric")] for name in EXTENT_NAMES)
        and all(tra[(name, "flat_k_commutator")] == 0 for name in EXTENT_NAMES)
        and all(tra[(name, "flat_k_transpose")] == FLAT_TRANSPOSE_COUNTS[name]
                for name in EXTENT_NAMES)
        # EVERY NONZERO TRANSPORT DIAL FAILS BOTH TESTS.
        and all(tra[(name, "nonzero_dials_fail_both")]
                for name in EXTENT_NAMES)
        # THE TWO CLAIM-BOUND LEGS.
        and tra["censuses_extent_independent"]
        == claims["hop_classes_extent_free"]
        and tra["tests_agree_everywhere"]
        == claims["transpose_convention_idle"]
        and facts.exact_no_float)

    obs = facts.obstruction
    gate_e = bool(
        # THE EXHIBIT: the raw reflected covariance selection is NOT Hermitian,
        # and Hermitianizing it is a CHOICE and not a derivation.
        all(not obs[(dial, "raw_cov_hermitian")]
            for dial in (ON_DIAL, REGION_DIAL))
        and all(obs[(dial, "raw_cov_defect")] > 0
                for dial in (ON_DIAL, REGION_DIAL))
        and all(obs[(dial, "herm_cov_hermitian")]
                for dial in (ON_DIAL, REGION_DIAL))
        and all(obs[(dial, "inverse_residual_zero")]
                for dial in (ON_DIAL, REGION_DIAL))
        and all(obs[(dial, "det_nonzero")] for dial in (ON_DIAL, REGION_DIAL))
        # THE FAMILY: more than one positive, fork-independent, dial-sensitive
        # readout, all functions of Q ALONE.
        and obs["family_size"] >= 2
        and obs["family_positive"]
        and obs["sensitive_family_size"] >= 2
        and obs["family_members_distinct"]
        and obs["herm_positive_definite"]
        # THE DIAL-BLIND MEMBER, MEASURED AND DISCLOSED rather than dropped:
        # 1/det(herm Q) is fork-independent and positive but does NOT move on
        # this dial, because herm(Q) is s_t-free.
        and obs["herm_det_dial_blind"]
        and obs["herm_is_dial_free"]
        and not obs["family_all_sensitive"]
        and facts.scope["dial_blind_member_disclosed"]
        # THE SCOPED STATEMENTS, gated as note text.
        and facts.scope["canonical_reconstruction_blocked"]
        and facts.scope["not_forced_hermitianization"]
        and facts.scope["fork_genuine"]
        and facts.scope["shear_scope_antecedent"]
        and facts.scope["fork_independence_lemma"]
        and facts.scope["family_not_unique"]
        and facts.scope["readout_axiom_absent"]
        # THE TWO CLAIM-BOUND LEGS.
        and ban["herm_is_forced"] == claims["forced_hermitianization"]
        and obs["readout_is_unique"] == claims["readout_unique"]
        and facts.exact_no_float)

    arm = facts.arm
    gate_f = bool(
        # THE COMPOSITION GATE at the trivial dial.
        arm["composed_shape"] == (24, 24)
        and arm["composed_symbol_free"]
        and arm["composition_equals_reference"]
        and arm["field_matches_landed"]
        and arm["route_agrees"]
        # I_off EXACTLY, against the LANDED Block 176 literals.
        and arm["baseline_available"]
        and arm["i_off_matches_landed"]
        and arm["i_off_gates"]
        and arm["i_off_signs"] == ARM_SIGNS
        # J AT (0, 1/4): the reduced-rational equality, the signs, the brackets.
        and arm["j_gates"]
        and arm["j_all_nonzero"]
        and arm["j_sum_zero"]
        and arm["j_signs"] == ARM_SIGNS
        and arm["j0"] == claims["j0_literal"]
        and arm["j0_digits"] == (J0_NUMERATOR_DIGITS, J0_DENOMINATOR_DIGITS)
        and arm["j_brackets"] == J_BRACKETS
        # THE THREE-LAMBDA CHAIN, strict because the brackets are DISJOINT.
        and arm["ray_brackets_well_formed"]
        and arm["ray_brackets_ordered"]
        and arm["strict_chain"]
        and len(RAY_LAMBDAS) == 3
        # THE CONTINUITY PROOF's ingredients, measured, plus its note statement.
        and arm["denominators_nonzero_at_zero"]
        and arm["dial_enters_affinely"]
        and facts.scope["rational_continuity"]
        and facts.scope["samples_superseded"]
        and facts.scope["interpretation_at_scope"]
        # THE CLAIM-BOUND LEG: three samples are NOT the limit proof.
        and ban["samples_are_the_proof"]
        == claims["contraction_proven_by_samples"]
        and (arm["deep_ray_agrees"] is True if facts.deep else True)
        and facts.exact_no_float)

    correction_keys = tuple(claims["required_correction_keys"])
    gate_g = bool(
        # THE FOUR SUPERVISOR CORRECTIONS AND THE THREE FURTHER ONES, as
        # declared literals rather than as prose alone.
        ban["supervisor_corrections"] == 4
        and ban["further_corrections"] == 3
        and len(SUPERVISOR_CORRECTIONS) == 4
        and len(FURTHER_CORRECTIONS) == 3
        # THE REQUIRED CORRECTION KEYS ARE THE FULL SET, which is what gives the
        # two drop mutations their teeth.
        and correction_keys == CORRECTION_KEYS
        and all(facts.scope[key] for key in correction_keys)
        and set(CORRECTION_KEYS) <= set(SCOPE_KEYS)
        and facts.scope["checker_overrides"]
        and facts.scope["codex_refute_check"]
        and facts.exact_no_float)

    required = tuple(claims["required_scope_keys"])
    budget = DEEP_RUNTIME_BUDGET_SEC if facts.deep else RUNTIME_BUDGET_SEC
    gate_h = bool(
        # THE NOTE AT ITS FINAL PATH.  An unlanded draft fails HERE and only
        # here; the scope certificate is still computed from the declared draft
        # fallback so the supervisor can see every key before landing.
        facts.note_at_final_path
        and NOTE_PATH.name == FINAL_NOTE_NAME
        and set(facts.scope) == set(SCOPE_KEYS)
        # THE FULL KEY SET IS REQUIRED, not a subset.
        and required == SCOPE_KEYS
        and all(facts.scope[key] for key in required)
        and facts.scope["n5_verbatim"]
        and facts.scope["scope_key_certificate"]
        and facts.scope["no_priority_claim"]
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        # THE N5 FENCE: N5-prefixed, 9 to 12 lines, the standard sections.
        and N5_FENCE.startswith("N5: ")
        and 9 <= N5_FENCE.count("\n") + 1 <= 12
        and all(N5_FENCE.count(f"\n{name}:") == 1
                for name in ("per_site", "per_mode", "per_block",
                             "lattice_wide", "per_scope", "RESULT",
                             "DECISION_CUT", "TOE"))
        and POOL_TWO_LEADS == 3
        and HANDOFF_ITEMS == 3
        and elapsed_ns <= budget * 1_000_000_000)

    return {"A": gate_a, "B": gate_b, "C": gate_c, "D": gate_d,
            "E": gate_e, "F": gate_f, "G": gate_g, "H": gate_h}


# ---------------------------------------------------------------------------
# the measurement pass: every gate reads it, no gate feeds it
# ---------------------------------------------------------------------------
def measure(deep: bool) -> Facts:
    note_text, at_final_path = raw_note()
    main_head = resolve_ref("origin/main")
    scope = scope_certificate(note_text)
    mirror = measure_mirror()
    transport = measure_transport(mirror)
    obstruction = measure_obstruction()
    arm = measure_arm(deep)
    banners = {
        "convention": b176.measure_convention() if b176 is not None else {},
        "imposed_objects": len(IMPOSED_OBJECTS),
        "registered_objects": len(REGISTERED_OBJECTS),
        "adopted_objects": len(ADOPTED_OBJECTS),
        "scoped_interpretations": len(SCOPED_INTERPRETATIONS),
        "owner_decisions": len(OWNER_DECISIONS),
        "supervisor_corrections": len(SUPERVISOR_CORRECTIONS),
        "further_corrections": len(FURTHER_CORRECTIONS),
        # THE TWO DECLARED STATUS FLAGS, so the mutations bite on a declared
        # object and not on prose.  Both are FALSE and both are the point.
        "herm_is_forced": False,
        "samples_are_the_proof": False,
    }
    for name in EXTENT_NAMES:
        record(mirror[(name, "ambient_count")])
        record(mirror[(name, "pinned_count")])
        record(mirror[(name, "level_count")])
        record(mirror[(name, "forced_a")])
        record(mirror[(name, "forced_b")])
        for value in mirror[(name, "volume_profile")]:
            record(value)
        for value in transport[(name, "commutator_counts")]:
            record(value)
        for value in transport[(name, "transpose_counts")]:
            record(value)
        record(transport[(name, "flat_k_transpose")])
    for dial in (ON_DIAL, REGION_DIAL):
        record(obstruction[(dial, "modulus")])
        for value in obstruction[(dial, "family")]:
            record(value)
    for value in arm["i_off"] + arm["j"]:
        record(value)
    record(OFF_VALUE)
    record(DIAG_VALUE)
    return Facts(
        deep=deep,
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope,
        banners=banners,
        mirror=mirror,
        transport=transport,
        obstruction=obstruction,
        arm=arm,
        exact_no_float=all(no_float(v) for v in NUMERALS),
        source_files=len(audit_source_paths()),
        source_floats=source_float_literals(),
        source_forbidden=source_forbidden_calls(),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--list-mutations", action="store_true",
        help="print the declared mutation names, one per line, and exit")
    parser.add_argument(
        "--deep", action="store_true",
        help="RECOMPUTE the three ray points of the contraction chain here, "
             "exactly, and match them against the independent route's "
             "published brackets; the runtime budget is lengthened")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No gate can cascade into another
    # because no gate feeds a measurement.
    facts = measure(arguments.deep)
    elapsed_ns = time.monotonic_ns() - started_ns

    raw_gates = evaluate_gates(facts, build_claims(""), elapsed_ns)
    gate_values = dict(raw_gates)
    if mutation:
        target = MUTATION_GATE[mutation]
        gate_values = evaluate_gates(facts, build_claims(mutation), elapsed_ns)
        changed = {k for k in raw_gates if raw_gates[k] != gate_values[k]}
        if changed - {target} or gate_values[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    ban = facts.banners
    mir, tra = facts.mirror, facts.transport
    obs, arm = facts.obstruction, facts.arm
    res = facts.authority.residue

    print("MEASURED, before any gate is read:")
    print(f"  PARENT IMPORT: the Block 177 runner imported "
          f"{facts.authority.parent_import_landed}; PARENT_COMMIT "
          f"{PARENT_COMMIT} is REAL and PARENT_REF resolves to it. "
          f"CURRENT_MAIN was RE-RESOLVED at draft time to {CURRENT_MAIN}")
    print(f"  THE STALE PIN: {STALE_PARENT_COMMIT[:12]} is a REAL ancestor of "
          f"HEAD {facts.authority.stale_is_real_ancestor} and carries NEITHER "
          f"Block 177 artifact {facts.authority.stale_carries_neither_artifact}"
          f" -- it is the Block 176 tip, which PREDATES both artifacts, and "
          f"that absence is exactly what makes the stale_parent_authority "
          f"mutation bite. AND THE HYGIENE RESIDUE IS COUNTED, NOT HIDDEN, as "
          f"(text mentions, LIVE CALL SITES): {res['per_module']}, which is "
          f"{record(res['call_sites_in_audit_surface'])} live call sites inside "
          f"this runner's AST audit surface and "
          f"{record(res['call_sites_below_audit_surface'])} BELOW it, in landed "
          f"modules the chain reaches transitively. REPORTED, and NEVER claimed "
          f"repaired")
    print(f"  THE NOTE: read at its FINAL PATH {facts.note_at_final_path} -- "
          f"when False this is an UNLANDED DRAFT reading the DECLARED FALLBACK "
          f"{DRAFT_NOTE_PATH.name}, gate H is EXPECTED to fail, and the gate-H "
          f"mutation is UNTESTABLE until the note lands; gates A-G are "
          f"unaffected.  Scope keys satisfied: "
          f"{sum(1 for v in facts.scope.values() if v)} of "
          f"{len(facts.scope)}; unsatisfied "
          f"{tuple(key for key, value in facts.scope.items() if not value)}")
    print(f"  THE INERTIA CONVENTION, FIRST: the landed b163/b164 helper and "
          f"the landed Block 165 helper on IDENTICAL matrices "
          f"{ban['convention'].get('pairs')} -- each pair (b163/b164, this "
          f"note); the region normal form is PSD under both readings and the "
          f"tuple ORDERS DIFFER {ban['convention'].get('orders_differ')}, so "
          f"the literal string (4,4,0) means PSD in Block 164's landed fence "
          f"and FULLY HYPERBOLIC here")
    print(f"  THE IMPOSED-OBJECT BANNER AND THE SCOPED READING: "
          f"{record(ban['imposed_objects'])} objects built by this block or its "
          f"parents, {record(ban['registered_objects'])} registered and "
          f"{record(ban['adopted_objects'])} adopted; "
          f"{record(ban['scoped_interpretations'])} SCOPED INTERPRETATION -- "
          f"{SCOPED_INTERPRETATIONS} -- and {record(ban['owner_decisions'])} "
          f"decision belongs to the OWNER: {OWNER_DECISIONS}. The imposed "
          f"objects are {IMPOSED_OBJECTS}")
    print(f"  THE TWO BENCHES, rebuilt through the LANDED Block 170 machinery: "
          f"8x4 (N = {record(mir[('8x4', 'N')])}, T_phys = "
          f"{record(mir[('8x4', 'T_phys')])}) and 12x4 (N = "
          f"{record(mir[('12x4', 'N')])}, T_phys = "
          f"{record(mir[('12x4', 'T_phys')])}), with the committed descended "
          f"involution satisfying r^2 = 1 at both "
          f"{tuple(mir[(n, 'r_involution')] for n in EXTENT_NAMES)}")
    print(f"  THE MIRROR, CONTROL FIRST: at zero shear and unit volume the "
          f"quotient Hodge action IS THE IDENTITY "
          f"{tuple(mir[(n, 'flat_is_identity')] for n in EXTENT_NAMES)} and "
          f"BOTH invariance tests vanish -- commutator "
          f"{tuple(mir[(n, 'flat_commutator')] for n in EXTENT_NAMES)} and "
          f"transpose {tuple(mir[(n, 'flat_transpose')] for n in EXTENT_NAMES)}"
          f" -- so the corrected control is 0/0 AT BOTH EXTENTS. The invariance "
          f"condition run here is r Q r = Q^T, NOT the solve's r Q r = Q; the "
          f"two coincide only on real-symmetric controls, which is what this "
          f"control is")
    print(f"  THE VOLUME COUNTEREXAMPLE: with zero shear and nu(t,x) = "
          f"(1,2,3,4)_x the action is DIAGONAL "
          f"{tuple(mir[(n, 'volume_diagonal')] for n in EXTENT_NAMES)}, NON-FLAT "
          f"{tuple(mir[(n, 'volume_is_non_flat')] for n in EXTENT_NAMES)}, "
          f"repeating {mir[('12x4', 'volume_profile')]} on EVERY time level "
          f"{tuple(mir[(n, 'volume_repeats')] for n in EXTENT_NAMES)}, and BOTH "
          f"defects vanish -- commutator "
          f"{tuple(mir[(n, 'volume_commutator')] for n in EXTENT_NAMES)}, "
          f"transpose {tuple(mir[(n, 'volume_transpose')] for n in EXTENT_NAMES)}"
          f". NON-FLAT REFLECTION-SYMMETRIC VOLUME GEOMETRY SURVIVES THE MIRROR "
          f"{mir['volume_geometry_survives']}, so 'mirror sector = geometry-free "
          f"sector' IS REFUTED and replaced by SHEARS BREAK THE MIRROR; VOLUMES "
          f"DO NOT")
    print(f"  THE SHEAR COUNTS: ambient sigma = 3/5 at unit volume gives "
          f"{record(mir[('8x4', 'ambient_count')])} at 8x4 and "
          f"{record(mir[('12x4', 'ambient_count')])} at 12x4; pinning t = 0, 1 "
          f"leaves {record(mir[('8x4', 'pinned_count')])} and "
          f"{record(mir[('12x4', 'pinned_count')])}; the nonzero VALUE SET is "
          f"{sorted(mir[('8x4', 'ambient_values')], key=sp.re)} at both")
    print(f"  THE SINGLE-LEVEL ACCOUNTING, HONESTLY: a PURE b-modulus level "
          f"contributes {record(mir[('8x4', 'b_level_count')])} entries in the "
          f"blocks {mir[('8x4', 'b_level_blocks')]}. BUT A PHYSICAL SHEAR LEVEL "
          f"ALSO FORCES ITS a-MODULUS -- measured a = "
          f"{mir[('8x4', 'forced_a')]} and b = {mir[('8x4', 'forced_b')]} -- and "
          f"contributes {record(mir[('8x4', 'level_count')])}: "
          f"{record(mir[('8x4', 'level_off_count')])} off-diagonal at "
          f"{sorted(mir[('8x4', 'level_off_values')], key=sp.re)} PLUS "
          f"{record(mir[('8x4', 'level_diag_count')])} diagonal at "
          f"{sorted(mir[('8x4', 'level_diag_values')], key=sp.re)} in the blocks "
          f"{mir[('8x4', 'level_diag_blocks')]}. THE ADDITIVE 16-PER-LEVEL LAW "
          f"IS REFUTED {not mir['additive_level_law_holds']} and the ambient/"
          f"pinned identities are PROFILE-SPECIFIC CANCELLATIONS")
    print(f"  THE TRANSPORT LEG: the defect is EXACTLY DIAL-LINEAR MATRIXWISE at "
          f"{len(LINEARITY_DIALS)} dial points per extent "
          f"{tuple(tra[(n, 'linearity_all')] for n in EXTENT_NAMES)}, so "
          f"D_K(s_x,s_t) = s_x D_K(1,0) + s_t D_K(0,1). THE FULL CENSUSES: at "
          f"8x4 s_x is {tra[('8x4', 'sx_census')]} and s_t is "
          f"{tra[('8x4', 'st_census')]} with counts "
          f"{tra[('8x4', 'commutator_counts')]}; at 12x4 s_x is "
          f"{tra[('12x4', 'sx_census')]} and s_t is {tra[('12x4', 'st_census')]} "
          f"with counts {tra[('12x4', 'commutator_counts')]}. The supports "
          f"overlap in {record(tra[('8x4', 'overlap_slots')])} slots at 8x4 and "
          f"{record(tra[('12x4', 'overlap_slots')])} at 12x4, so the totals are "
          f"NOT sums; and the censuses are NOT extent-independent "
          f"{tra['censuses_extent_independent']}")
    print(f"  THE CONVENTION IS LOAD-BEARING: under the CORRECT transpose test "
          f"the same dials give {tra[('8x4', 'transpose_counts')]} at 8x4 and "
          f"{tra[('12x4', 'transpose_counts')]} at 12x4. AT FLAT ZERO SHEAR K IS "
          f"REAL {tuple(tra[(n, 'flat_k_real')] for n in EXTENT_NAMES)} AND "
          f"ANTISYMMETRIC "
          f"{tuple(tra[(n, 'flat_k_antisymmetric')] for n in EXTENT_NAMES)}, it "
          f"PASSES the commutator test "
          f"{tuple(tra[(n, 'flat_k_commutator')] for n in EXTENT_NAMES)} and "
          f"FAILS the transpose test "
          f"{tuple(record(tra[(n, 'flat_k_transpose')]) for n in EXTENT_NAMES)}"
          f". THE TWO TESTS DO NOT AGREE EVERYWHERE "
          f"{tra['tests_agree_everywhere']}, and that is DISCLOSED; but EVERY "
          f"NONZERO TRANSPORT DIAL FAILS BOTH "
          f"{tuple(tra[(n, 'nonzero_dials_fail_both')] for n in EXTENT_NAMES)}")
    print(f"  THE OBSTRUCTION EXHIBIT: the raw reflected covariance selection "
          f"[r (Q^-1)^T]_SS is NOT Hermitian at either dial "
          f"{tuple(not obs[(d, 'raw_cov_hermitian')] for d in (ON_DIAL, REGION_DIAL))}"
          f", with {record(obs[(ON_DIAL, 'raw_cov_defect')])} nonzero entries in "
          f"its anti-Hermitian part on the dial -- so it CANNOT serve as an OS "
          f"Gram as it stands, and THE CANONICAL REFLECTION-POSITIVE HILBERT "
          f"RECONSTRUCTION FROM THESE DATA IS BLOCKED. THAT IS ALL IT IS: "
          f"herm() IS NOT FORCED, declared forced = {ban['herm_is_forced']}, and "
          f"THE BLOCK-177 GRADING PREMISE REMAINS A GENUINE FORK")
    print(f"  THE FORK-INDEPENDENT FAMILY: {record(obs['family_size'])} readouts "
          f"that are each a FUNCTION OF Q ALONE -- 1/|det Q|^2, 1/|det Q|^4, "
          f"1/det(herm Q) on its PD domain {obs['herm_positive_definite']}, and "
          f"1/tr(Q^dag Q) -- are ALL POSITIVE {obs['family_positive']} and ALL "
          f"DISTINCT {obs['family_members_distinct']}, with dial-sensitivity "
          f"{obs['family_sensitive']}: {record(obs['sensitive_family_size'])} of "
          f"{record(obs['family_size'])} MOVE. AND THE BLIND ONE IS DISCLOSED, "
          f"NOT DROPPED: 1/det(herm Q) is fork-independent and positive but "
          f"DIAL-BLIND {obs['herm_det_dial_blind']}, because herm(Q) is ITSELF "
          f"s_t-free {obs['herm_is_dial_free']} -- the transport part of Q is "
          f"anti-Hermitian. So POSITIVITY PLUS SENSITIVITY STILL DOES NOT SELECT "
          f"ONE: measured unique = {obs['readout_is_unique']}, and UNIQUENESS "
          f"WOULD NEED A READOUT AXIOM THAT IS ABSENT HERE")
    print(f"  THE INTERFERENCE ARM, COMPOSITION FIRST: the composed action is "
          f"{arm['composed_shape']}, symbol-free {arm['composed_symbol_free']}, "
          f"and at the TRIVIAL DIAL it equals the landed reference ENTRY FOR "
          f"ENTRY {arm['composition_equals_reference']}; the record field "
          f"carries the records {arm['field_matches_landed']} and the two "
          f"determinant routes agree {arm['route_agrees']}")
    print(f"  I_off REPRODUCES THE LANDED BLOCK 176 LITERALS EXACTLY "
          f"{arm['i_off_matches_landed']} with signs {arm['i_off_signs']}, all "
          f"exact gates {arm['i_off_gates']}. AND J != 0 EXACTLY at (0, 1/4): "
          f"signs {arm['j_signs']}, every component nonzero "
          f"{arm['j_all_nonzero']}, sum exactly zero {arm['j_sum_zero']}, |J| "
          f"brackets {arm['j_brackets']} and L1 bracket {arm['l1_bracket']}. "
          f"THE FIRST COMPONENT IS A REDUCED RATIONAL WITH "
          f"{record(arm['j0_digits'][0])}-DIGIT NUMERATOR AND "
          f"{record(arm['j0_digits'][1])}-DIGIT DENOMINATOR and it matches the "
          f"independent raw-Hodge-before-quotient route's embedded literal AS "
          f"INTEGERS {arm['j0'] == J0_VALUE}")
    print(f"  THE CONTRACTION CHAIN AND THE LIMIT: the exact L1 brackets along "
          f"lambda (1/3, 1/4) at lambda = {RAY_LAMBDAS} are "
          f"{arm['ray_brackets']}; they are WELL-FORMED "
          f"{arm['ray_brackets_well_formed']} and PAIRWISE DISJOINT AND ORDERED "
          f"{arm['ray_brackets_ordered']}, which PROVES the strict three-point "
          f"chain {arm['strict_chain']}. THE LIMIT ITSELF IS PROVEN BY RATIONAL "
          f"CONTINUITY AND NOT BY THE SAMPLES: the dial enters the action "
          f"AFFINELY {arm['dial_enters_affinely']} so every determinant is "
          f"polynomial and every weight rational in lambda, and NO DENOMINATOR "
          f"VANISHES AT lambda = 0 {arm['denominators_nonzero_at_zero']}; "
          f"declared samples-are-the-proof = {ban['samples_are_the_proof']}. "
          f"WHAT IS MEASURED IS THAT THE CHOSEN |det Q|^-2 CONSISTENCY DEFECT "
          f"RESPONDS TO THE HOLONOMY DIAL; the interference WORDS are AN "
          f"INTERPRETATION AT SCOPE")
    print(f"  THE CORRECTIONS RECORD: {record(ban['supervisor_corrections'])} "
          f"SUPERVISOR CORRECTIONS in this arc, carried verbatim -- "
          f"{SUPERVISOR_CORRECTIONS} -- and "
          f"{record(ban['further_corrections'])} FURTHER STATEMENTS corrected "
          f"by the cross-model check -- {FURTHER_CORRECTIONS}. ALL OF THEM ARE "
          f"DISCLOSED AS THE PROCESS WORKING")
    print(f"  EXACTNESS: no float in any measured object "
          f"{facts.exact_no_float} over {record(len(NUMERALS))} numerals; the "
          f"AST scan covers {record(facts.source_files)} FILES -- this runner "
          f"AND the imported runner chain -- and finds "
          f"{record(facts.source_floats)} float literals and "
          f"{record(facts.source_forbidden)} forbidden references. THE AST "
          f"SURFACE IS DISCLOSED AND IS NOT THE FULL TRANSITIVE CLOSURE")
    print(f"  SAMPLING: --deep {facts.deep}; at baseline the TWO load-bearing "
          f"dial points are recomputed exactly and the three ray brackets are "
          f"gated as EXACT RATIONAL ARITHMETIC on the independent route's "
          f"published brackets, while --deep RECOMPUTES the three ray points "
          f"here. DEEP RAY {arm['deep_ray']}; agreement "
          f"{arm['deep_ray_agrees']} -- None and () mean the leg was NOT RUN at "
          f"this invocation, which is DISCLOSED rather than reported as "
          f"agreement")
    print()

    checks = Checks()
    checks.check(
        "A-authority-and-THE-STALE-PIN-THAT-PREDATES-BOTH-ARTIFACTS",
        "main plus the TWO Block 177 artifacts content-bound -- its note and its runner, which are BOTH the stack parent this block's branch is cut from AND the content parent, since this runner IMPORTS the Block 177 runner and reaches the whole committed chain through Block 177's own import chain, which Block 177's gate A pins rather than this one duplicating it -- and the gate additionally requires that the Block 177 runner ACTUALLY IMPORTED, because every fixture below is built by the LANDED Block 170 Bench and the LANDED Block 171 Site reached through it. PARENT_COMMIT IS REAL AND SO ARE BOTH ARTIFACT BLOBS: Block 177 HAS landed, so nothing needs sed at landing, and CURRENT_MAIN was re-resolved at draft time. THE FIVE-PIN AUTHORITY BLOCK binds origin/main's head, the axioms blob and the registry blob at origin/main, and the axioms and registry blobs in the worktree. THE STALE PIN IS THE BLOCK 176 TIP, a REAL ancestor of HEAD that PREDATES Block 177 and therefore carries NEITHER Block 177 artifact, which is exactly what makes the stale_parent_authority mutation bite -- under it the gate looks for the artifact blobs at a commit where they do not exist. THE HYGIENE RESIDUE BELOW THE AUDIT SURFACE IS COUNTED AND REPORTED AND NEVER CLAIMED REPAIRED, as (text mentions, LIVE CALL SITES) per module",
        gate_values["A"])
    checks.check(
        "B-the-two-banners-THE-SCOPED-READING-and-both-bench-anchors",
        "THE TWO BANNERS COME BEFORE ANY NUMERAL AND BOTH ARE MEASURED RATHER THAN ASSERTED. THE INERTIA CONVENTION: called on IDENTICAL matrices, b163/b164's congruence_inertia returns (n_+, n_0, n_-) and Block 165's real_symmetric_inertia returns (n_+, n_-, n_0), so the region normal form reads (4,4,0) there and (4,0,4) here; NEITHER HELPER IS WRONG and no landed verdict changes, but THE LITERAL STRING (4,4,0) MEANS PSD IN BLOCK 164'S LANDED FENCE AND FULLY HYPERBOLIC IN THIS NOTE. THE IMPOSED-OBJECT BANNER: seven objects are imposed by this block or its parents -- the antiunitary reflection with its invariance condition, the two invariance tests, the four carrier profiles, the two single-level probes, the hop-class map, the interference menu and cells and dial and weight, and the inherited reflection, region pin, slice index set, menu, class map, slot order and record-slice scope -- and ZERO of them are registered and ZERO adopted. AND THE THIRD THING THIS GATE BINDS IS THE SCOPE OF THE READING: exactly ONE SCOPED INTERPRETATION is declared -- that transport IS record-record interference -- and it is carried as an interpretation and never gated as a theorem, while ONE decision is the OWNER'S and the FOUR supervisor corrections and THREE further checker corrections are declared as counted literals. AND BOTH BENCH ANCHORS ARE MEASURED: at 8x4 the quotient action is 16x16 at T_phys = 4 and at 12x4 it is 24x24 at T_phys = 6, with the committed descended involution satisfying r^2 = 1 at both. No float enters any measured object and the AST scan covers every file this runner reads code from in the runner chain",
        gate_values["B"])
    checks.check(
        "C-THE-SHEAR-MIRROR-THEOREM-with-THE-VOLUME-COUNTEREXAMPLE-and-THE-24-ENTRY-ACCOUNTING",
        "THE CONVENTION IS FIXED FIRST, BECAUSE IT IS LOAD-BEARING. For the antiunitary Theta phi = r conj(phi) the invariance of a quadratic form is r Q r = Q^T and NOT r Q r = Q; the supervisor's commutator-only convention is QUOTED AND CORRECTED, the two coincide only on real-symmetric controls, and this gate runs BOTH tests on every profile rather than choosing one. THE ZERO-SHEAR FLAT CONTROL IS EXACTLY INVARIANT: the quotient Hodge action is the IDENTITY and both defects are 0 at 8x4 AND at 12x4 -- the corrected 0/0 control. THE VOLUME COUNTEREXAMPLE IS THE POINT OF THE SECTION: with zero shear and the reflection-symmetric profile nu(t,x) = (1,2,3,4)_x the action is diagonal, NON-FLAT, and repeats (25/16, 3/2, 17/8, 17/6) on every time level, and BOTH defects vanish at BOTH extents -- so NON-FLAT REFLECTION-SYMMETRIC VOLUME GEOMETRY SURVIVES THE MIRROR and the slogan 'the mirror-symmetric sector is exactly the geometry-free sector' IS REFUTED AND REPLACED BY: SHEARS BREAK THE MIRROR; VOLUMES DO NOT. THE SHEAR FIELD BREAKS IT AND THE COUNTS ARE REPRODUCED: ambient sigma = 3/5 at unit volume gives 64 nonzero entries at 8x4 and 96 at 12x4, pinning t = 0, 1 leaves 32 and 64, and the nonzero value set is exactly {+15/64, -15/64} in all four. AND THE PER-LEVEL LAW IS REFUTED BY AN HONEST ACCOUNTING: a PURE b-modulus level contributes exactly 16 entries, four each in the blocks (0,1), (1,0), (1,2) and (2,1), but a PHYSICAL single-level shear ALSO FORCES a = 25/16 -- measured from the substitution, not assumed -- and its defect has 24 entries: the same 16 off-diagonal at +-15/64 PLUS 8 diagonal at +-9/64 in the blocks (0,0) and (2,2). THE ADDITIVE 16-PER-LEVEL LAW IS THEREFORE FALSE and the ambient/pinned identities are PROFILE-SPECIFIC CANCELLATIONS, gated as such",
        gate_values["C"])
    checks.check(
        "D-THE-TRANSPORT-LEG-the-FULL-CENSUSES-and-THE-CONVENTION-SPLIT",
        "THE DIAL LINEARITY IS EXACT AND IT IS MATRIXWISE, NOT MERELY IN THE COUNTS: D_K(s_x, s_t) = s_x D_K(1,0) + s_t D_K(0,1) entry for entry at four dial points per extent, including a mixed-sign point, so every census below is a support statement about a linear family. THE FULL HOP CENSUSES ARE TAKEN AT BOTH EXTENTS AND THEY REFUTE THE ADVERTISED GENERALIZATION TWICE. At 8x4 the s_x defect is (1,0):8 and (1,2):8 while the s_t defect is (0,1):16, (1,0):32 and (2,1):16 -- so the complete s_t support is THREE classes and not the two the solve named -- with counts 16, 64 and 72. At 12x4 the s_x defect is (1,0):16 and (1,2):16, the s_t defect is (0,1):16, (1,0):48 and (2,1):32, and the counts are 32, 96 and 112 -- so 16 -> 64/72 is an 8x4 SUPPORT CENSUS and NOT an extent-independent scaling law. The two supports overlap in exactly 8 slots at 8x4 and 16 at 12x4, which is why the combined counts are not sums, and the gate measures the overlap rather than inferring it. AND THE CONVENTION IS LOAD-BEARING, WHICH IS DISCLOSED AND NOT SMOOTHED: under the correct transpose test the same dials give 16, 64, 72 at 8x4 but 24, 104, 116 at 12x4; and at FLAT ZERO SHEAR the connection is REAL and ANTISYMMETRIC, PASSES the commutator test with defect exactly 0, and FAILS the transpose test with 16 entries at 8x4 and 24 at 12x4. The two tests therefore do NOT agree everywhere. WHAT SURVIVES THE CONVENTION IS THE CONCLUSION: EVERY NONZERO TRANSPORT DIAL FAILS BOTH TESTS at both extents",
        gate_values["D"])
    checks.check(
        "E-THE-OBSTRUCTION-AT-EXACTLY-ITS-STRENGTH-and-THE-FORK-INDEPENDENT-FAMILY",
        "THE EXHIBIT IS THE OBJECT THE CANONICAL RECONSTRUCTION WOULD NEED, AND IT IS MEASURED UNUSABLE. A bosonic quasi-free Hilbert grading needs a Hermitian positive-semidefinite reflected two-point form; for the fixed Gaussian the raw candidate is the reflected covariance selection [r (Q^-1)^T]_SS, and this gate REBUILDS it at both dials from the landed machinery, with the two-sided inverse residual exactly zero first, and MEASURES IT NOT HERMITIAN. So the canonical reflection-positive Hilbert reconstruction FROM THESE FIXED DATA IS BLOCKED. THAT IS THE WHOLE OF THE OBSTRUCTION AND THE GATE REFUSES TO STATE MORE: herm() IS NOT FORCED -- the declared status flag says so and reasserting it fails this gate -- because degree grading, non-positive functionals, restriction, quotient, field doubling, a changed complex structure or reflection, and an added positive two-point form all remain available; THE BLOCK-177 GRADING PREMISE THEREFORE REMAINS A GENUINE FORK, and the volume counterexample of gate C narrows the antecedent from geometry to SHEAR SCOPE. AND THE FAMILY LEG KILLS THE UNIQUENESS CLAIM ON A MEASURED OBJECT RATHER THAN IN PROSE: four readouts that are each a FUNCTION OF Q ALONE -- hence fork-independent by the lemma -- are exhibited at both dials, all positive, all pairwise distinct, and ALL DIAL-SENSITIVE. Positivity plus sensitivity therefore cannot select one, UNIQUENESS WOULD REQUIRE A READOUT AXIOM THAT IS ABSENT HERE, and asserting uniqueness fails this gate",
        gate_values["E"])
    checks.check(
        "F-THE-INTERFERENCE-ARM-the-2299-DIGIT-EQUALITY-and-THE-CONTINUITY-PROOF",
        "THE COMPOSITION IS GATED BEFORE ANY INTERFERENCE NUMBER IS READ: records are written into the shear FIELD and the resulting substitution is applied to the landed Site.Q_holo_t, the composed action is 24x24 and symbol-free, and AT THE TRIVIAL DIAL IT EQUALS THE LANDED REFERENCE MATRIX ENTRY FOR ENTRY, with two independent exact determinant routes agreeing at the witness. THE DIAL-OFF BASELINE REPRODUCES THE LANDED BLOCK 176 LITERALS EXACTLY -- read through the import, not copied -- with signs (+,+,-,-), all determinants nonzero, both laws normalized and the defect summing exactly to zero. J != 0 EXACTLY AT (0, 1/4): every component nonzero, signs (+,+,-,-), sum exactly zero, and the four absolute brackets reproduced; AND ITS FIRST COMPONENT IS COMPARED AS INTEGERS AGAINST THE EMBEDDED REDUCED RATIONAL the INDEPENDENT raw-Hodge-before-quotient route printed -- a 2299-digit numerator over a 2302-digit denominator, with both digit lengths gated. THE STRICT THREE-POINT CONTRACTION CHAIN IS PROVED BY DISJOINTNESS, NOT BY EYEBALLING: the exact L1 brackets at lambda = 1/2, 1/4 and 1/8 along the ray are well-formed and PAIRWISE DISJOINT AND ORDERED, which is an exact rational fact. AND THE LIMIT IS PROVED THE OTHER WAY: the gate MEASURES that the dial enters the action AFFINELY, so every determinant is polynomial and every normalized weight rational in the ray parameter, and that NO DETERMINANT OR NORMALIZATION DENOMINATOR VANISHES AT lambda = 0 -- with J(0) = 0, continuity gives the limit. THE THREE SAMPLES ARE CORROBORATION AND NOT THE PROOF, the declared flag says so, and asserting that the samples ARE the proof fails this gate. WHAT IS MEASURED IS THAT THE CHOSEN |det Q|^-2 CONSISTENCY DEFECT RESPONDS TO THE HOLONOMY DIAL; the words 'transport is record-record interference' are AN INTERPRETATION AT SCOPE and are gated as note text only",
        gate_values["F"])
    checks.check(
        "G-THE-CORRECTIONS-RECORD-carried-verbatim-with-the-SISTER-LANE-CITED",
        "THE CORRECTIONS ARE THE SPINE OF THIS BLOCK AND THIS GATE REQUIRES THEM PRESENT, NOT SUMMARISED. FOUR SUPERVISOR CORRECTIONS are carried in this arc as counted literals and as keyed note text: THE WRAP HYPOTHESIS, that the breaking was the antiperiodic wrap -- wrong and owned, because at zero shear the defect is exactly 0 under both tests at both extents; THE PIN HYPOTHESIS, that the breaking was dial-independent and not level-local -- wrong and owned, because pinning removes exactly the pinned levels' share; THE GEOMETRY-FREE SLOGAN -- refuted by the exact volume counterexample and replaced; and THE FORCED-FORK AND UNIQUENESS CLAIM -- refuted, because the obstruction blocks a canonical reconstruction only and the readout sits in a family. THREE FURTHER STATEMENTS OF THE SOLVE were corrected by the cross-model check and are carried at their corrected values: the covariance convention, the per-level additive law, and the hop-class and extent-scaling story. THE CHECKER IS CREDITED by name for the volume counterexample, the convention correction, the full censuses at both extents, the added lambda = 1/8 point and the rational-continuity proof, and the note states that ITS FINDINGS OVERRIDE THE SOLVE EVERYWHERE THEY COLLIDE. THE SISTER LANE'S #7325 COUNTERMODEL IS CITED as the independent effect-level instance of the same uniqueness lesson, and its scope is left as its own. The required correction-key set is THE FULL SET, which is what gives the two drop mutations their teeth: removing the corrections record or the sister-lane citation fails HERE and nowhere else",
        gate_values["G"])
    checks.check(
        "H-note-scope-the-caution-and-the-N5-fence",
        "THE NOTE SITS AT ITS FINAL PATH AND SATISFIES EVERY REQUIRED SCOPE KEY, the required set is THE FULL KEY SET and not a subset, the N5 fence is an N5-prefixed literal with nine labelled sections that appears BYTE-IDENTICALLY in the note, and the mutation battery is fifteen members mapped one-per-gate across A through H. THE VERDICT THIS GATE CERTIFIES IS FOUR SCOPED STATEMENTS AND NOTHING WIDER: SHEARS BREAK THE MIRROR AND VOLUMES DO NOT, at two extents under the correct antiunitary condition; THE CANONICAL RECONSTRUCTION IS BLOCKED AT SHEAR SCOPE while no prescription is forced and the Block 177 premise stays a GENUINE FORK; THE VACUUM READOUT IS FORK-INDEPENDENT IN A FAMILY and uniqueness needs a readout axiom that is absent; and THE INTERFERENCE IS MEASURED while its reading is AN INTERPRETATION AT SCOPE. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 caution, carried verbatim -- and every positive here is CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE. The worker profile is disclosed in full: ALL SOLVE-SIDE SCIENCE by the supervising frontier model INLINE, per the owner's standing directive; the REFUTE-SPEC'D adversarial check and the interference arm by codex 5.6-sol xhigh workers, cross-model, whose findings OVERRIDE the solve everywhere they collide; OPUS MECHANICAL DRAFTING ONLY; and supervisor review and landing -- with common-mode risk reduced and NOT eliminated. The scope is TWO EXTENTS plus one interference bench and no wider; it is NOT a continuum statement, NOT AN OS NO-GO, NOT a derivation of the Born rule and NOT a construction of a Fock space; and the disclosures are complete, THIS BLOCK'S OWN DEFECTS INCLUDED -- the counts are profile-specific, the obstruction is a block and not a no-go, the readout is not unique, the volume counterexample is not a classification, the interference reading is scoped -- alongside NO FLOAT anywhere, the not-re-verified list, N1 through N8, the W1 wall, the scope-key certificate, the LaTeX rho guard, the pool-2 leads, the three handoff items, zero axiom retirement, zero obligation retirement, no TOE percentage movement, a retained-positive end-to-end theory count that remains zero, and NO priority or originality wording anywhere in the note",
        gate_values["H"])
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

