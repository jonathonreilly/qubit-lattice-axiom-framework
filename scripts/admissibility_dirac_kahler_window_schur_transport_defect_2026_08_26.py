#!/usr/bin/env python3
"""BLOCK 196 -- THE WINDOW-SCHUR THEOREM: THE TRANSPORT-DEFECT FUNCTIONALS OF A
CORE ARE THE UNIQUE SOLUTIONS OF A TWELVE-ROW WINDOW-RESTRICTED SYSTEM, AND THAT
CONSTRUCTION PROVES THE COMPATIBILITY DIRECTION OF BLOCK 193's WINDOW LAW.

THE RESULT, AND ITS EXACT SCOPE.  Block 193 measured a locality law -- a
reflected one-cell source breaks the intertwining identity at core t0 if and
only if it meets the window W(t0) = [2 floor(t0/2)+1, 2 floor(t0/2)+3] -- and
recorded LAW_PROVED_FROM_RECURRENCE_CLAIMED = False: the law was verified
exhaustively and reduced to two measured support facts, NOT derived.  This block
converts ONE of those two facts, and with it ONE of the law's two directions,
from a measurement into a CONSTRUCTION.

  (i) THE SYSTEM.  For a core t0 with cells b <-> (t_b, x_b), t_b in
      {t0, t0+1}, the s-step transport-defect functional is the explicit vector

        d_b^(s)  =  e_(t_b+s, x_b)  -  sum_b' W_s[b', b] e_(t_b', x_b'),
        W_s      =  K_c^-1 L_s,     L_s[a,b] = G[idx(t_b+s, x_b), theta_a],

      for s = 1 and s = 2, with K_c = L_0 and G = Q^-1.  Let J(t0) be the TWELVE
      rows of the three window slices and A = Q^T[:, J(t0)], a (4T) x 12 exact
      rational matrix.

 (ii) IT HAS A UNIQUE WINDOW-SUPPORTED SOLUTION, AND THAT SOLUTION IS BLOCK
      193's MECHANISM OBJECT.  rank(A) = 12 at every core of both widths, so a
      window-supported solution is unique when it exists; it EXISTS for all
      eight columns at both steps; and padding it by zeros reproduces
      u_b = G^T d_b ENTRYWISE.  Block 193's u_b is therefore not merely
      supported in the window -- it IS the window-Schur solution.

(iii) TWELVE ROWS ARE MINIMAL, WITH ONE EXACT QUALIFICATION.  No proper subset
      of J(t0) carries the two-step family, and none carries the joint one-and
      two-step family, at any core of either width -- decided EXHAUSTIVELY, not
      inferred, by the twelve single-row deletions that dominate every proper
      subset.  The ONE-STEP family alone is different and the adversarial check
      found it: at EVEN cores it collapses to the FOUR rows of the window's
      FIRST slice.  That qualification is carried here as content.

 (iv) AND THE LAW'S COMPATIBILITY DIRECTION FOLLOWS AS A PROOF.  Not from
      supp(u_b) subset J alone -- that is not sufficient, and the check's C5
      refinement is the reason.  The bilinear identity is

        u_b^T dQ  =  u_b^T dH (m I + D_s)  -  (D_s u_b)^T dH,

      so TWO containments are needed: supp(u_b) subset J AND
      supp(D_s u_b) subset J.  Both are exact here, at every core of both
      widths and at BOTH rational points, and together they make the vanishing
      a THEOREM for every source whose (symmetric) support misses the window,
      not a sampled cancellation.

THE BREAKING DIRECTION IS NOT PROVEN HERE.  It remains Block 193's exhaustive
censuses -- 40 cells at T = 16 and 70 at T = 20 -- and this block cites them
rather than reproving them.  ONE HALF OF THE LAW IS NOW A THEOREM AND THE OTHER
HALF IS STILL A CENSUS, AND THIS BLOCK SAYS SO FIRST.

ALL OF IT IS FINITE EXACT LINEAR ALGEBRA OVER QQ ON ONE CONSTRUCTED MATRIX
FAMILY AT TWO WIDTHS AND TWO RATIONAL POINTS.  NONE OF IT SUPPLIES GRAVITY.
NONE OF IT IS A WIDTH INDUCTION: 'RECURRENCE PROOF' NAMES THE CONSTRUCTIVE SCHUR
FORM AT EACH FIXED CORE OF EACH FIXED WIDTH AND NOTHING ELSE, AND NO STEP HERE
DERIVES ANYTHING FROM THE STAGGERED RECURRENCE OR PROPAGATES ANYTHING FROM T TO
T + 2.  'WINDOW', 'TRANSPORT', 'SOURCE' AND 'PROOF' NAME PROPERTIES OF EXACT
RATIONAL MATRICES AND OF NOTHING ELSE, AND THEY ARE FENCED BEFORE THE FIRST
NUMERAL.

  0. THE CONSTRUCTION (C).  rank(A) = 12 at all twelve cores of both widths and
     both points; existence 8/8 per (core, step) through an INDEPENDENT
     restricted solve -- an exact rref pivot selection, a 12 x 12 minor inverse
     and a residual checked against all 4T equations -- with the same pivot rows
     serving both right-hand sides; and the rebuilt carrier reproduces Block
     190's and Block 193's landed fingerprints digit for digit.

  1. THE IDENTIFICATION (D).  padded v_b - G^T d_b = 0 for all eight columns at
     both steps and every core, and Q^T u_b - d_b = 0 in the same places.  The
     four t0-row one-step defects are IDENTICALLY ZERO by construction, so the
     one-step content lives in b = 4..7.

  2. EXACTNESS AND THE FINE STRUCTURE (E).  The two-step support union is the
     FULL twelve-row window at every core; the one-step union is all three
     slices at ODD cores and EXACTLY the first slice at EVEN cores; twelve rows
     are minimal for the two-step and the joint families and FOUR are minimal
     for the one-step family at even cores, decided by exhaustive single-row
     deletion; and the three two-slice subsets behave exactly as the check
     reported.

  3. THE CONSEQUENCE (F).  Both containments, the bilinear identity at zero
     residual, the exhaustive disjoint-source census -- 16 cells per T = 16 core
     and 24 per T = 20 core, 248 source/core cells, zero failures -- one gated
     instance per parity, and a NON-VACUITY witness: a source that MEETS the
     window has nonzero u^T dQ, so the theorem is not the empty statement.

  4. GENERALITY (G).  Every structural statement above persists at the second
     rational point (1/2, 1/3) on the same twelve cores, on a carrier that is
     measurably different -- structure of the class, coefficients of the point.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GRAVITY.  NO WIDTH
INDUCTION.  NO DERIVATION FROM THE STAGGERED RECURRENCE.  NO PROOF OF THE
BREAKING DIRECTION.  NO GENERIC (m, c) THEOREM.  NO CONTINUUM.  THE READINGS ARE
READINGS.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 195 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: six imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, a width induction, a recurrence derivation, a
     proof of the breaking direction, a generic-point theorem, the continuum
     limit and licensed readings ALL declared NOT CLAIMED as measured constants,
     and nine gravity structures enumerated as NOT SUPPLIED.
  C  THE CONSTRUCTION: the window rank, the two solve routes at zero residual on
     the full core domain of both widths, the nine-nonzero defect columns, and
     the two landed fingerprints.
  D  THE IDENTIFICATION: the padded solution against G^T d, the dual identity,
     and the four identically zero one-step columns.
  E  EXACTNESS AND FINE STRUCTURE: the two-step union, the parity rule for the
     one-step union, the PER-COLUMN slice rule that names WHICH slices each
     column meets, exhaustive minimality for three families, and the two-slice
     subset table.
  F  THE CONSEQUENCE: the two containments, the D_s u localization, the bilinear
     identity, the disjoint-source census, the two parity instances, and the
     non-vacuity witness.
  G  GENERALITY at (1/2, 1/3): the core signature, the minimality counts, both
     containments, and a carrier that actually differs.
  H  the note at its final path, the N5 fence byte-identical, and the
     nsimplify count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through H PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: thirty-five declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.  The per-family census is
  A 2, B 8, C 5, D 3, E 5, F 7, G 3, H 2.
  SIX OF THE THIRTY-FIVE GUARD CORRECTIONS RATHER THAN RESULTS:
  claim_width_induction asserts the per-width construction is an induction on T;
  claim_recurrence_derivation asserts the law was derived FROM the staggered
  recurrence; claim_breaking_direction_proven asserts this block proves the
  converse; break_core_domain asserts the T = 20 domain is the solve's two
  spot-check cores rather than the checker's seven; break_even_collapse and
  break_subset_table assert the naive reading in which twelve rows are minimal
  for EVERY family at EVERY core; and break_du_containment asserts the single
  containment that would NOT suffice.

RUNNING
  python3 scripts/admissibility_dirac_kahler_window_schur_transport_defect_2026_08_26.py
  python3 ... --list-mutations
  python3 ... --mutation claim_width_induction
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

# THE MACHINERY IMPORT, LANDED, AND IT IS EXACTLY ONE OBJECT: the Block 105
# shear_hodge() re-exported by the Block 128 module, read here at UNIT VOLUME
# and at the two rational shears this block probes.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_WINDOW_SCHUR_TRANSPORT_DEFECT_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 195 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 194 tip.
BLOCK195_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SECTORED_INTERIOR_OS_RECONSTRUCTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
BLOCK195_RUNNER = (
    "scripts/admissibility_dirac_kahler_sectored_interior_os_reconstruction_"
    "2026_08_25.py"
)
PARENT_ARTIFACTS = (BLOCK195_NOTE, BLOCK195_RUNNER)
# Refreshed by anchored sed at landing, exactly as the five pins are.
PARENT_ARTIFACT_BLOBS = (
    "2d2b68338c38a7d930649ed1d82da4bf0a7b45dd",   # Block 195 note
    "8fa8bf49994aa080f442d02f0954e5a2dbcf9bd5",   # Block 195 runner
)
# THE CONSTRUCTION AUTHORITY, AND IT IS TWO NOTES: Block 190's width family,
# whose carrier, reflected pairings and monodromy are carried unchanged, and
# Block 193's parity window law, whose transport-defect functional, one-cell
# reflected tangent and bilinear residual are the objects this block solves for.
# Block 191 supplies the cell-average assembly, Block 105 the imported Hodge and
# Block 188 the site route of which the width family is a disclosed variant.
BLOCK193_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PARITY_WINDOW_INTERTWINING_LAW_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK193_RUNNER = (
    "scripts/admissibility_dirac_kahler_parity_window_intertwining_law_"
    "2026_08_25.py"
)
BLOCK190_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK191_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK105_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_"
    "HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WINDOW_SCHUR_TRANSPORT_DEFECT_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SECTORED_INTERIOR_OS_RECONSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_sectored_interior_os_reconstruction_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PARITY_WINDOW_INTERTWINING_LAW_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_parity_window_intertwining_law_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  RE-RESOLVED LIVE AT DRAFT TIME against the REMOTE origin/main
# of the real repository -- never against a local main ref, which sits behind it.
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block195-"
              "sectored-interior-os-reconstruction-20260825")
PARENT_COMMIT = "7877b4afac1363b80ac37a28c90182c811f01da1"
# The Block 194 tip: a real ancestor of HEAD that predates Block 195 and
# therefore carries NEITHER Block 195 artifact.
STALE_PARENT_COMMIT = "4cbd56203b020475bc9b24cf04a2d24bfe6da43f"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_width_induction",
    "claim_recurrence_derivation",
    "claim_breaking_direction_proven",
    "claim_generic_point_theorem",
    "claim_continuum_limit",
    "claim_readings_licensed",
    "break_window_rank",
    "break_existence",
    "break_solve_route",
    "break_core_domain",
    "break_landed_fingerprints",
    "break_identification",
    "break_dual_identity",
    "break_mechanism_object",
    "break_two_step_union",
    "break_even_collapse",
    "break_minimality",
    "break_joint_minimality",
    "break_subset_table",
    "break_u_containment",
    "break_du_containment",
    "break_du_localization",
    "break_bilinear_identity",
    "break_disjoint_census",
    "break_parity_instances",
    "break_nonvacuity",
    "break_second_point_structure",
    "break_second_point_minimality",
    "break_second_point_containment",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_width_induction": "B",
    "claim_recurrence_derivation": "B",
    "claim_breaking_direction_proven": "B",
    "claim_generic_point_theorem": "B",
    "claim_continuum_limit": "B",
    "claim_readings_licensed": "B",
    "break_window_rank": "C",
    "break_existence": "C",
    "break_solve_route": "C",
    "break_core_domain": "C",
    "break_landed_fingerprints": "C",
    "break_identification": "D",
    "break_dual_identity": "D",
    "break_mechanism_object": "D",
    "break_two_step_union": "E",
    "break_even_collapse": "E",
    "break_minimality": "E",
    "break_joint_minimality": "E",
    "break_subset_table": "E",
    "break_u_containment": "F",
    "break_du_containment": "F",
    "break_du_localization": "F",
    "break_bilinear_identity": "F",
    "break_disjoint_census": "F",
    "break_parity_instances": "F",
    "break_nonvacuity": "F",
    "break_second_point_structure": "G",
    "break_second_point_minimality": "G",
    "break_second_point_containment": "G",
    "drop_n5_fence": "H",
    "break_nsimplify_absence": "H",
}
MUTATED_FAMILIES = "ABCDEFGH"


class Checks:
    def __init__(self) -> None:
        self.results: list = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def families(self) -> dict:
        summary: dict = {}
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
    return is_hash(value) and value.startswith("0" * 30)


def audit_inputs_readable() -> tuple:
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
    "BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20, CARRIED UNCHANGED AND STILL A DISCLOSED VARIANT OF BLOCK 188's SITE CONSTRUCTION: the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H",
    "BLOCK 193's CORE FRAME AND ITS TRANSPORT-DEFECT FUNCTIONALS, READ AT BOTH STEPS RATHER THAN ONLY THE SECOND: the eight cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_s[a,b] = G[idx(t_b + s, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, the step operators W_s = K_c^-1 L_s for s = 1 and s = 2, and the defect columns d_b^(s) = e_(t_b+s, x_b) - sum_b' W_s[b', b] e_(t_b', x_b') -- the ONE-STEP family is this block's addition and Block 193 read only the two-step one",
    "THE THREE-SLICE WINDOW AND ITS TWELVE ROWS AS A ROW SET OF Q^T, WHICH IS THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT: J(t0) = [2 floor(t0/2)+1, 2 floor(t0/2)+3] x Z_4 read as the twelve-column restriction A = Q^T[:, J(t0)] of the transposed action, IMPOSED FROM BLOCK 193's MEASURED WINDOW AND DERIVED FROM NOTHING",
    "THE VALID CORE DOMAIN, BLOCK 193's OWN t0 + 3 <= T/2 RULE: t0 = 1..5 at T = 16 and t0 = 1..7 at T = 20 -- the second is the ADVERSARIAL CHECK's extension of the solve's two spot-check cores and is carried here in full",
    "BLOCK 193's REFLECTED ONE-CELL HODGE TANGENT dH(s, x) = E(s,x) dB E(s,x)^T / 4 + E(thA_s s, x) P_4 dB P_4^T E(thA_s s, x)^T / 4 with thA_s(t) = -1-t and dB the exact volume derivative of the import, together with its action tangent dQ = m dH + dH D_s - D_s^T dH -- carried unchanged as the SOURCE family whose disjointness this block exploits",
    "THE LANDED BLOCK 105 shear_hodge(c, v) READ THROUGH THE BLOCK 128 MODULE AT UNIT VOLUME AND AT THE TWO RATIONAL SHEARS 5/13 AND 1/3 -- THE ONLY OBJECT IMPORTED -- assembled into H by Block 191's quarter-weighted four-corner cell average at Block 190's seam convention",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SIX ARE FALSE
# AND STAY FALSE.  THE SECOND AND THIRD ARE THE TWO THIS BLOCK'S TITLE MOST
# INVITES A READER TO ASSUME, AND THE FOURTH IS THE HALF OF THE LAW THAT IS
# STILL A CENSUS.
GRAVITY_SUPPLIED_CLAIMED = False
WIDTH_INDUCTION_CLAIMED = False
RECURRENCE_DERIVATION_CLAIMED = False
BREAKING_DIRECTION_PROVEN_CLAIMED = False
GENERIC_POINT_THEOREM_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function",
    "shift vector",
    "ADM phase space",
    "Hamiltonian constraint",
    "momentum/diffeomorphism constraint",
    "first-class constraint algebra",
    "Dirac closure",
    "Dirac observable",
    "gauge orbit and its quotient",
)
READINGS = (
    "R1: that Block 193's window law is now PROVEN.  Measured: the COMPATIBILITY direction is proven constructively at twelve cores of two widths and two rational points; the BREAKING direction is Block 193's censuses, cited and not reproved.  Reading.",
    "R2: that this is a RECURRENCE proof.  Measured: a Schur-complement solve at each fixed core of each fixed width, with no step from T to T + 2 and no use of the staggered recurrence.  Reading, and the block's own banner says so.",
    "R3: that the even-core single-slice collapse EXPLAINS the parity switch.  Measured: at even cores the one-step family lives on the window's first slice and four rows are minimal there.  Why the staggering forces that is NOT derived.  Reading.",
    "R4: that u_b is canonical.  Measured: given the twelve window rows it is the UNIQUE supported solution, because rank(A) = 12.  Whether some OTHER twelve-row set also carries the family is NOT decided here.  Reading.",
    "R5: that the structure is a property of the width family rather than of the fixture.  Measured: two rational points on twelve cores.  Two points are not a parameter space.  Reading.",
)
CHECK_VERDICT = "WINDOW-SCHUR-NOT-REFUTED-ALL-CORES-BOTH-WIDTHS-MINIMALITY-QUALIFIED"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
WIDTHS = (16, 20)
SPACE_EXTENT = 4
CORE_CELLS = 8
WINDOW_SLICES = 3
WINDOW_ROWS = 12
UNIT_VOLUME = sp.Integer(1)

FIXTURE = ("9/20", "5/13")
SECOND_POINT = ("1/2", "1/3")
POINTS = (FIXTURE, SECOND_POINT)

# THE VALID CORE DOMAIN: Block 193's t0 + 3 <= T/2.  The T = 20 row is the
# ADVERSARIAL CHECK's all-core extension of the solve's spot check at {3, 4}.
CORE_DOMAIN = {16: (1, 2, 3, 4, 5), 20: (1, 2, 3, 4, 5, 6, 7)}
SOLVE_SPOT_CHECK_CORES_20 = (3, 4)
CORE_COUNT = 12
STEPS = (1, 2)

# --- C: THE CONSTRUCTION -----------------------------------------------------
WINDOW_RANK = 12
CARRIER_RANKS = {16: 64, 20: 80}
EXISTENCE_PER_CORE = 8
EXACT_SOLVES = 384            # 12 cores x 2 points x 2 steps x 8 columns
# d_b^(s) carries ONE entry at (t_b + s, x_b) and at most EIGHT on the read pair
# {t0, t0+1}, so no column of either defect matrix can exceed nine nonzeros.
DEFECT_MAX_NONZEROS = 9
# The two landed fingerprints the rebuilt carrier must reproduce EXACTLY.
BLOCK190_FINGERPRINT_CORE = (20, 3)
BLOCK190_FINGERPRINT = sp.Rational(
    53601896033238042551256, 229758595220483765728625)
BLOCK193_FINGERPRINT_CELL = (16, 2, 5, 0)
BLOCK193_FINGERPRINT = sp.Rational(
    303717414128393981002946552450301011272963193469691599136505997554493148222247708710000000,
    77707725095998816829080256798567544217876202163787270905242891606801827087957579200283634261)
FINGERPRINT_RESIDUALS = (0, 0)

# --- D: THE IDENTIFICATION ---------------------------------------------------
IDENTIFICATION_RESIDUALS = (0, 0)
DUAL_RESIDUALS = (0, 0)
# The four t0-row one-step defects are IDENTICALLY ZERO: W_1's column b for
# b = 0..3 is exactly e_(b+4), so d_b^(1) cancels entrywise.
ONE_STEP_ZERO_COLUMNS = 4
MECHANISM_IS_SOLUTION = True

# --- E: EXACTNESS AND THE FINE STRUCTURE ------------------------------------
TWO_STEP_UNION_IS_FULL_WINDOW = True
ONE_STEP_UNION_SLICES_ODD = 3
ONE_STEP_UNION_SLICES_EVEN = 1
MINIMAL_ROWS_TWO_STEP = 12
MINIMAL_ROWS_JOINT = 12
MINIMAL_ROWS_ONE_STEP_ODD = 12
MINIMAL_ROWS_ONE_STEP_EVEN = 4
# The three two-slice subsets, in the order first+middle, first+last,
# middle+last.  True means the whole eight-column family solves inside it.
SUBSET_TABLE = {
    ("one", "odd"): (False, False, False),
    ("one", "even"): (True, True, False),
    ("two", "odd"): (False, False, False),
    ("two", "even"): (False, False, False),
}
DELETION_TESTS = 864          # 12 cores x 2 points x 3 families x 12 rows
# THE PER-COLUMN SLICE RULE, AS COUNTS OF WINDOW SLICES MET BY COLUMN b = 0..7.
# A count of 0 means an identically zero column, a count of 1 means the window's
# FIRST slice alone and a count of 3 means the whole window; the check enforces
# WHICH slice in each case and not merely how many.
PER_COLUMN_SLICE_RULE = {
    ("one", "odd"): (0, 0, 0, 0, 3, 3, 3, 3),
    ("one", "even"): (0, 0, 0, 0, 1, 1, 1, 1),
    ("two", "odd"): (3, 3, 3, 3, 3, 3, 3, 3),
    ("two", "even"): (1, 1, 1, 1, 3, 3, 3, 3),
}
# At even cores every nonzero ONE-STEP column has exactly four coordinates, one
# per spatial site of the window's first slice.
EVEN_ONE_STEP_COLUMN_WEIGHT = 4

# --- F: THE CONSEQUENCE ------------------------------------------------------
U_CONTAINMENT = True
DU_CONTAINMENT = True
U_SUPPORT_ROWS = 12
DU_SUPPORT_ROWS = 10
# The two rows of J(t0) that D_s u NEVER reaches are the EVEN spatial sites of
# the window's MIDDLE slice, at every core of both widths and both points.
DU_MISSING_SPATIAL = (0, 2)
BILINEAR_IDENTITY_RESIDUAL = 0
DISJOINT_CELLS_PER_CORE = {16: 16, 20: 24}
DISJOINT_CELLS_TOTAL = 248
DISJOINT_FAILURES = 0
# One gated instance per parity at T = 16: (core, source cell, dH slice support).
PARITY_INSTANCES = (
    (1, (4, 0), (4, 5, 11, 12)),
    (2, (0, 0), (0, 1, 15)),
)
PARITY_INSTANCE_SHAPE = (8, 64)
# NON-VACUITY: three sources that DO meet the window, with their exact
# nnz(u^T dQ).  Without these the compatibility theorem would be empty.
NONVACUITY_WITNESSES = (
    (1, (2, 0), 60),
    (2, (2, 0), 64),
    (2, (4, 0), 28),
)
NONVACUITY_WITNESS_SLICES = (
    (2, 3, 13, 14),
    (2, 3, 13, 14),
    (4, 5, 11, 12),
)

# --- G: THE SECOND POINT -----------------------------------------------------
# The exact v = 1 continuation of the imported Block 105 shear Hodge at c = 1/3,
# declared so the second point is bound to the import rather than to a rerun.
SECOND_POINT_HODGE_BLOCK = (
    (1, 0, 0, 0),
    (0, sp.Rational(9, 8), sp.Rational(-3, 8), 0),
    (0, sp.Rational(-3, 8), sp.Rational(9, 8), 0),
    (0, 0, 0, 1),
)
SECOND_POINT_STRUCTURE_MATCHES = True
SECOND_POINT_MINIMAL_MATCHES = True
SECOND_POINT_CONTAINMENT = True
SECOND_POINT_CARRIER_DIFFERS = True

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  This block's entire content is a SUPPORT statement -- which
# entries of an exact rational vector are zero and which are not -- and the
# entries in question are ratios of integers with more than eighty digits in the
# denominator.  A single such call would move rows into and out of every support
# reported here, turning a twelve-row minimal window into a smaller one and a
# nonvacuous witness into a vanishing one.  Every mass, shear and volume here is
# ALREADY an exact sympy Rational.  Gate H counts the occurrences in this file's
# own source and requires ZERO.
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
    QQ^(m x n) exactly; DomainMatrix carries out the inverse, the rank and the
    determinant by exact fraction-free arithmetic over that field.  No float is
    created at any point and no tolerance exists to be tuned."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ)


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return rational_matrix(matrix).inv().to_Matrix()


def exact_rank(matrix: sp.MatrixBase) -> int:
    return rational_matrix(matrix).rank()


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is
    involved."""
    return nonzero_entries(sp.Matrix(matrix).applyfunc(sp.expand))


def rat(text: str) -> sp.Rational:
    """A rational from a plain string literal.  NOT nsimplify: sp.Rational on a
    decimal-free ratio of integers is exact by construction."""
    return sp.Rational(text)


# ---------------------------------------------------------------------------
# THE WIDTH FAMILY AT AN ARBITRARY WIDTH AND (m, c).  Everything except the
# shear block is rebuilt here; the shear block is the ONE import.
# ---------------------------------------------------------------------------
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])


def site_index(width: int, time: int, space: int) -> int:
    return (time % width) * SPACE_EXTENT + space % SPACE_EXTENT


def site_theta(width: int, time: int) -> int:
    """theta_s(t) = -t, fixing the slices {0, T/2}."""
    return (-time) % width


def anchor_theta(width: int, time: int) -> int:
    """thA_s(t) = -1-t: Block 193's ANCHOR reflection, which carries a cell
    across the seam."""
    return (-1 - time) % width


def staggered_kernel(width: int) -> sp.Matrix:
    kernel = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            temporal_sign = -1 if time == width - 1 else 1
            here = site_index(width, time, space)
            ahead = site_index(width, time + 1, space)
            kernel[here, ahead] += sp.Rational(temporal_sign, 2)
            kernel[ahead, here] -= sp.Rational(temporal_sign, 2)
            spatial_sign = (-1) ** time
            right = site_index(width, time, space + 1)
            kernel[here, right] += sp.Rational(spatial_sign, 2)
            kernel[right, here] -= sp.Rational(spatial_sign, 2)
    return kernel


def grade_projector(width: int, grade: int) -> sp.Matrix:
    return sp.diag(*[1 if (time % 2 + space % 2) == grade else 0
                     for time in range(width) for space in range(SPACE_EXTENT)])


def raising_part(width: int, kernel: sp.Matrix) -> sp.Matrix:
    p0, p1, p2 = (grade_projector(width, g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def reflection_permutation(width: int) -> sp.Matrix:
    matrix = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            matrix[site_index(width, site_theta(width, time), space),
                   site_index(width, time, space)] = 1
    return matrix


def site_restricted_raising(width: int, raising: sp.Matrix) -> sp.Matrix:
    half = width // 2
    closed, fixed = set(range(half + 1)), {0, half}
    matrix = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for row in range(width * SPACE_EXTENT):
        for column in range(width * SPACE_EXTENT):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            if row_time not in closed or column_time not in closed:
                continue
            if row_time == column_time and row_time in fixed:
                continue
            matrix[row, column] = raising[row, column]
    return matrix


def cell_embedding(width: int, time: int, space: int) -> sp.Matrix:
    matrix = sp.zeros(width * SPACE_EXTENT, 4)
    for column, (delta_t, delta_x) in enumerate(
            ((0, 0), (0, 1), (1, 0), (1, 1))):
        matrix[site_index(width, time + delta_t, space + delta_x), column] = 1
    return matrix


_GEOMETRY_CACHE: dict = {}


def geometry(width: int) -> dict:
    """The (m, c)-independent half of the carrier, built once per width."""
    if width in _GEOMETRY_CACHE:
        return _GEOMETRY_CACHE[width]
    kernel = staggered_kernel(width)
    reflection = reflection_permutation(width)
    raising = site_restricted_raising(width, raising_part(width, kernel))
    glue = sp.expand(raising - reflection * raising * reflection)
    embeddings = {(time, space): cell_embedding(width, time, space)
                  for time in range(width) for space in range(SPACE_EXTENT)}
    record = {"reflection": reflection, "glue": glue, "embeddings": embeddings}
    _GEOMETRY_CACHE[width] = record
    return record


def imported_shear_block(shear: sp.Rational, volume: object) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT: the LANDED Block 105 shear Hodge
    diag(v, v g(c)^-1, 1/v) with g(c) = [[1, c], [c, 1]].  NO nsimplify: the
    shear is an exact sympy Rational and the volume is a Rational or a Symbol."""
    return sp.Matrix(b128.block105.shear_hodge(shear, volume))


def volume_derivative(shear: sp.Rational) -> sp.Matrix:
    """dB = d/d(delta) shear_hodge(c, 1 - delta) at delta = 0, Block 193's
    displayed tangent, taken here as the SYMBOLIC derivative of the import so
    that no literal stands between the landed object and the source."""
    delta = sp.Symbol("delta")
    block = imported_shear_block(shear, UNIT_VOLUME - delta)
    return sp.expand(block.diff(delta).subs(delta, 0))


def site_hodge(width: int, shear: sp.Rational) -> sp.Matrix:
    """THE QUARTER-WEIGHTED FOUR-CORNER CELL AVERAGE, Block 191's assembly rule
    at Block 190's seam convention and at unit volume."""
    half = width // 2
    block = imported_shear_block(shear, UNIT_VOLUME)
    reflected = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    embeddings = geometry(width)["embeddings"]
    result = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for time in range(width):
        chosen = block if time < half else reflected
        for space in range(SPACE_EXTENT):
            embedding = embeddings[time, space]
            result += embedding * chosen * embedding.T / 4
    return sp.expand(result)


def completion(mass: sp.Rational, hodge: sp.Matrix,
               glue: sp.Matrix) -> sp.Matrix:
    """Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    return sp.expand(mass * hodge + hodge * glue - glue.T * hodge)


def action_tangent(mass: sp.Rational, tangent: sp.Matrix,
                   glue: sp.Matrix) -> sp.Matrix:
    """dQ = m dH + dH D_s - D_s^T dH, exact because D_s does not depend on the
    volume profile at all."""
    return sp.expand(mass * tangent + tangent * glue - glue.T * tangent)


def one_cell_tangent(width: int, anchor: int, space: int,
                     block: sp.Matrix) -> sp.Matrix:
    """BLOCK 193's REFLECTED ONE-CELL HODGE TANGENT: the single cell at
    (anchor, space) carrying dB, plus its thA_s image cell carrying
    P_4 dB P_4^T."""
    positive = cell_embedding(width, anchor, space)
    image = cell_embedding(width, anchor_theta(width, anchor), space)
    mirrored = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    return sp.expand(positive * block * positive.T / 4
                     + image * mirrored * image.T / 4)


# ---------------------------------------------------------------------------
# THE HEAVY WORK, DONE ONCE PER (width, m, c) AND SHARED.  The exact 64 x 64 and
# 80 x 80 inverses are the only expensive steps in this runner and nothing
# recomputes one: four inverses serve every gate below.
# ---------------------------------------------------------------------------
_CARRIER_CACHE: dict = {}


def carrier(width: int, point: tuple) -> dict:
    key = (width, point)
    if key in _CARRIER_CACHE:
        return _CARRIER_CACHE[key]
    mass, shear = rat(point[0]), rat(point[1])
    parts = geometry(width)
    action = completion(mass, site_hodge(width, shear), parts["glue"])
    domain = rational_matrix(action)
    rank = domain.rank()
    record = {"width": width, "mass": mass, "shear": shear, "action": action,
              "rank": rank, "glue": parts["glue"], "inverse": None,
              "transpose": action.T, "tangent_block": volume_derivative(shear)}
    if rank == width * SPACE_EXTENT:
        record["inverse"] = domain.inv().to_Matrix()
        record["inverse_residuals"] = (
            residual_count(action * record["inverse"]
                           - sp.eye(width * SPACE_EXTENT)),
            residual_count(record["inverse"] * action
                           - sp.eye(width * SPACE_EXTENT)))
    else:                                              # pragma: no cover
        record["inverse_residuals"] = (-1, -1)
    _CARRIER_CACHE[key] = record
    return record


# ---------------------------------------------------------------------------
# THE WINDOW-SCHUR OBJECTS, ALL OF THEM FORMULAS
# ---------------------------------------------------------------------------
def core_cells(core: int) -> tuple:
    return tuple((time, space) for time in (core, core + 1)
                 for space in range(SPACE_EXTENT))


def shifted_pairing(width: int, inverse: sp.Matrix, core: int,
                    step: int) -> sp.Matrix:
    """L_s[a,b] = G[idx(t_b + s, x_b), idx(theta_s t_a, x_a)]; s = 0 is K_c."""
    cells = core_cells(core)
    matrix = sp.zeros(CORE_CELLS, CORE_CELLS)
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(width, site_theta(width, row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(width, column_time + step, column_space), partner]
    return matrix


def defect_columns(width: int, core: int, step_operator: sp.Matrix,
                   step: int) -> sp.Matrix:
    """d_b^(s) = e_(t_b+s, x_b) - sum_b' W_s[b', b] e_(t_b', x_b'), as the eight
    columns of one (4T) x 8 exact rational matrix."""
    cells = core_cells(core)
    matrix = sp.zeros(width * SPACE_EXTENT, CORE_CELLS)
    for column, (time, space) in enumerate(cells):
        matrix[site_index(width, time + step, space), column] += 1
        for row, (other_time, other_space) in enumerate(cells):
            matrix[site_index(width, other_time, other_space), column] -= \
                step_operator[row, column]
    return matrix


def window_slices(core: int) -> tuple:
    """W(t0) = [2 floor(t0/2) + 1, 2 floor(t0/2) + 3], Block 193's window."""
    base = 2 * (core // 2)
    return (base + 1, base + 2, base + 3)


def window_rows(core: int) -> tuple:
    return tuple(slice_index * SPACE_EXTENT + space
                 for slice_index in window_slices(core)
                 for space in range(SPACE_EXTENT))


def support_rows(matrix: sp.MatrixBase) -> tuple:
    return tuple(row for row in range(matrix.rows)
                 if any(matrix[row, column] != 0
                        for column in range(matrix.cols)))


def column_supports(matrix: sp.MatrixBase) -> tuple:
    return tuple(tuple(row for row in range(matrix.rows)
                       if matrix[row, column] != 0)
                 for column in range(matrix.cols))


def slice_set(rows: tuple) -> tuple:
    return tuple(sorted({row // SPACE_EXTENT for row in rows}))


def restricted_solve(matrix: sp.Matrix, right: sp.Matrix) -> tuple:
    """THE INDEPENDENT SOLVE ROUTE, AND IT NEVER TOUCHES G.  An exact rref of
    A^T selects rank many independent rows of the tall full-column-rank A; the
    square minor on those rows is inverted over QQ; and the resulting x is
    checked against ALL 4T equations before it is padded.  A solve that agrees
    with G^T d is then two routes agreeing, not one route restated."""
    pivots = tuple(matrix.T.rref(simplify=False)[1])
    if len(pivots) != matrix.cols:                     # pragma: no cover
        raise AssertionError((len(pivots), matrix.cols))
    minor = matrix.extract(pivots, range(matrix.cols))
    solution = exact_inverse(minor) * right.extract(pivots, range(right.cols))
    return solution, pivots, residual_count(matrix * solution - right)


def family_solvable_on(matrix: sp.Matrix, right: sp.Matrix,
                       kept: tuple) -> bool:
    """IMAGE MEMBERSHIP, NOT A RANK COUNT: does the WHOLE eight-column family
    admit a solution supported on the kept column subset?"""
    sub = matrix[:, list(kept)]
    pivots = tuple(sub.T.rref(simplify=False)[1])
    if len(pivots) != sub.cols:                        # pragma: no cover
        return False
    minor = sub.extract(pivots, range(sub.cols))
    solution = exact_inverse(minor) * right.extract(pivots, range(right.cols))
    return residual_count(sub * solution - right) == 0


@dataclass(frozen=True)
class CoreFacts:
    width: int
    point: tuple
    core: int
    parity: str
    window: tuple
    rows: tuple
    window_rank: int
    pivot_rows: tuple
    pivot_route_stable: bool
    defect_weights: tuple
    existence: tuple
    identification: tuple
    dual: tuple
    zero_one_step_columns: int
    union_rows: tuple
    union_slices: tuple
    per_column_slices: tuple
    per_column_counts: tuple
    joint_union_rows: tuple
    droppable: tuple
    minimal_rows: tuple
    subsets: tuple
    u_rows: tuple
    du_rows: tuple
    du_missing: tuple
    containment: tuple


def measure_core(width: int, point: tuple, core: int) -> CoreFacts:
    record = carrier(width, point)
    inverse, transpose = record["inverse"], record["transpose"]
    glue = record["glue"]
    core_gram = shifted_pairing(width, inverse, core, 0)
    gram_inverse = exact_inverse(core_gram)
    steps = {step: gram_inverse * shifted_pairing(width, inverse, core, step)
             for step in STEPS}
    defects = {step: defect_columns(width, core, steps[step], step)
               for step in STEPS}

    rows = window_rows(core)
    restriction = transpose[:, list(rows)]
    rank = exact_rank(restriction)

    solutions, pivots, residuals = {}, {}, {}
    for step in STEPS:
        solutions[step], pivots[step], residuals[step] = restricted_solve(
            restriction, defects[step])

    padded, duals, unions, per_slices, per_counts = {}, {}, {}, {}, {}
    identification = {}
    for step in STEPS:
        block = sp.zeros(width * SPACE_EXTENT, CORE_CELLS)
        for local, global_row in enumerate(rows):
            block[global_row, :] = solutions[step][local, :]
        padded[step] = block
        functional = sp.expand(inverse.T * defects[step])
        identification[step] = residual_count(block - functional)
        duals[step] = residual_count(transpose * functional - defects[step])
        supports = column_supports(solutions[step])
        per_counts[step] = tuple(len(item) for item in supports)
        per_slices[step] = tuple(
            slice_set(tuple(rows[i] for i in item)) for item in supports)
        unions[step] = tuple(
            rows[i] for i in sorted(set().union(*map(set, supports))))

    joint = sp.Matrix.hstack(defects[1], defects[2])
    joint_union = tuple(sorted(set(unions[1]) | set(unions[2])))

    families = {"one": defects[1], "two": defects[2], "joint": joint}
    droppable, minimal = {}, {}
    for name, right in families.items():
        dropped = tuple(
            k for k in range(WINDOW_ROWS)
            if family_solvable_on(
                restriction, right,
                tuple(i for i in range(WINDOW_ROWS) if i != k)))
        droppable[name] = dropped
        minimal[name] = WINDOW_ROWS - len(dropped)

    slices = window_slices(core)
    subsets = {}
    for name in ("one", "two"):
        outcome = []
        for dropped_slice in (slices[2], slices[1], slices[0]):
            kept = tuple(i for i, row in enumerate(rows)
                         if row // SPACE_EXTENT != dropped_slice)
            outcome.append(family_solvable_on(restriction, families[name], kept))
        subsets[name] = tuple(outcome)

    functional_two = sp.expand(inverse.T * defects[2])
    glued = sp.expand(glue * functional_two)
    u_rows = support_rows(functional_two)
    du_rows = support_rows(glued)
    middle = slices[1]
    return CoreFacts(
        width=width,
        point=point,
        core=core,
        parity="even" if core % 2 == 0 else "odd",
        window=slices,
        rows=rows,
        window_rank=rank,
        pivot_rows=pivots[1],
        pivot_route_stable=pivots[1] == pivots[2],
        defect_weights=tuple(
            max(len(item) for item in column_supports(defects[step]))
            for step in STEPS),
        existence=(residuals[1], residuals[2]),
        identification=(identification[1], identification[2]),
        dual=(duals[1], duals[2]),
        zero_one_step_columns=sum(
            1 for count in per_counts[1] if count == 0),
        union_rows=(unions[1], unions[2]),
        union_slices=(slice_set(unions[1]), slice_set(unions[2])),
        per_column_slices=(per_slices[1], per_slices[2]),
        per_column_counts=(per_counts[1], per_counts[2]),
        joint_union_rows=joint_union,
        droppable=(droppable["one"], droppable["two"], droppable["joint"]),
        minimal_rows=(minimal["one"], minimal["two"], minimal["joint"]),
        subsets=(subsets["one"], subsets["two"]),
        u_rows=u_rows,
        du_rows=du_rows,
        du_missing=tuple(sorted(set(rows) - set(du_rows))),
        containment=(set(u_rows).issubset(rows),
                     set(du_rows).issubset(rows),
                     tuple(sorted(set(rows) - set(du_rows)))
                     == (middle * SPACE_EXTENT + DU_MISSING_SPATIAL[0],
                         middle * SPACE_EXTENT + DU_MISSING_SPATIAL[1])))


@dataclass(frozen=True)
class ConsequenceFacts:
    width: int
    core: int
    window: tuple
    cells_checked: int
    failures: tuple
    identity_residual: int
    first_instance: tuple


def measure_consequence(width: int, core: int) -> ConsequenceFacts:
    """THE DISJOINT-SOURCE CENSUS, EXHAUSTIVE OVER THE POSITIVE ANCHORS.  Every
    reflected one-cell source whose symmetric support misses the window is
    built, its dQ is formed, and BOTH u^T dQ and the two-term identity are
    measured.  Nothing is sampled."""
    record = carrier(width, FIXTURE)
    inverse, glue, mass = record["inverse"], record["glue"], record["mass"]
    block = record["tangent_block"]
    gram_inverse = exact_inverse(shifted_pairing(width, inverse, core, 0))
    step_two = gram_inverse * shifted_pairing(width, inverse, core, 2)
    functional = sp.expand(inverse.T * defect_columns(
        width, core, step_two, 2))
    glued = sp.expand(glue * functional)
    rows = set(window_rows(core))
    identity = sp.eye(width * SPACE_EXTENT)

    checked, failures, worst, first = 0, [], 0, ()
    for anchor in range(width // 2):
        for space in range(SPACE_EXTENT):
            tangent = one_cell_tangent(width, anchor, space, block)
            support = set(support_rows(tangent))
            columns = {column for column in range(tangent.cols)
                       if any(tangent[row, column] != 0
                              for row in range(tangent.rows))}
            if support != columns:                     # pragma: no cover
                raise AssertionError("dH support is not symmetric")
            if not support.isdisjoint(rows):
                continue
            daction = action_tangent(mass, tangent, glue)
            product = residual_count(functional.T * daction)
            two_term = residual_count(
                functional.T * daction
                - (functional.T * tangent * (mass * identity + glue)
                   - glued.T * tangent))
            worst = max(worst, two_term)
            checked += 1
            if not first:
                first = (anchor, space, slice_set(tuple(sorted(support))),
                         product)
            if product or two_term:                    # pragma: no cover
                failures.append((anchor, space, product, two_term))
    return ConsequenceFacts(width, core, window_slices(core), checked,
                            tuple(failures), worst, first)


def measure_fingerprints() -> dict:
    """TWO LANDED NUMBERS, REBUILT.  Neither Block 190's runner nor Block 193's
    is imported: both values are recomputed from this file's own carrier and
    compared against the landed literals."""
    width, core = BLOCK190_FINGERPRINT_CORE
    record = carrier(width, FIXTURE)
    inverse = record["inverse"]
    gram_inverse = exact_inverse(shifted_pairing(width, inverse, core, 0))
    one_step = gram_inverse * shifted_pairing(width, inverse, core, 1)
    two_step = gram_inverse * shifted_pairing(width, inverse, core, 2)
    monodromy_entry = sp.expand((two_step - one_step * one_step)[0, 4])

    width, core, anchor, space = BLOCK193_FINGERPRINT_CELL
    record = carrier(width, FIXTURE)
    inverse, glue, mass = record["inverse"], record["glue"], record["mass"]
    gram_inverse = exact_inverse(shifted_pairing(width, inverse, core, 0))
    step_two = gram_inverse * shifted_pairing(width, inverse, core, 2)
    functional = sp.expand(inverse.T * defect_columns(width, core, step_two, 2))
    tangent = one_cell_tangent(width, anchor, space, record["tangent_block"])
    daction = action_tangent(mass, tangent, glue)
    columns = sp.zeros(width * SPACE_EXTENT, CORE_CELLS)
    for index, (time, place) in enumerate(core_cells(core)):
        columns[:, index] = inverse[
            :, site_index(width, site_theta(width, time), place)]
    product = sp.expand(functional.T * daction * columns)
    residual_entry = sp.expand(-product[4, 0])
    return {
        "b190_value": monodromy_entry,
        "b190_residual": sp.simplify(monodromy_entry - BLOCK190_FINGERPRINT),
        "b193_value": residual_entry,
        "b193_residual": sp.simplify(residual_entry - BLOCK193_FINGERPRINT),
        "b193_nnz": nonzero_entries(product),
    }


def measure_witnesses() -> tuple:
    """NON-VACUITY: sources that DO meet the window, with their exact
    nnz(u^T dQ).  A compatibility theorem whose hypothesis is never violated
    would be worth nothing, and this is the gate that says it is not."""
    record = carrier(16, FIXTURE)
    inverse, glue, mass = record["inverse"], record["glue"], record["mass"]
    block = record["tangent_block"]
    out = []
    for core, (anchor, space), _ in NONVACUITY_WITNESSES:
        gram_inverse = exact_inverse(shifted_pairing(16, inverse, core, 0))
        step_two = gram_inverse * shifted_pairing(16, inverse, core, 2)
        functional = sp.expand(inverse.T * defect_columns(16, core, step_two, 2))
        tangent = one_cell_tangent(16, anchor, space, block)
        daction = action_tangent(mass, tangent, glue)
        support = set(support_rows(tangent))
        out.append((core, (anchor, space),
                    not support.isdisjoint(set(window_rows(core))),
                    nonzero_entries(sp.expand(functional.T * daction)),
                    slice_set(tuple(sorted(support)))))
    return tuple(out)


def measure_parity_instances() -> tuple:
    record = carrier(16, FIXTURE)
    inverse, glue, mass = record["inverse"], record["glue"], record["mass"]
    block = record["tangent_block"]
    out = []
    for core, (anchor, space), _ in PARITY_INSTANCES:
        gram_inverse = exact_inverse(shifted_pairing(16, inverse, core, 0))
        step_two = gram_inverse * shifted_pairing(16, inverse, core, 2)
        functional = sp.expand(inverse.T * defect_columns(16, core, step_two, 2))
        tangent = one_cell_tangent(16, anchor, space, block)
        daction = action_tangent(mass, tangent, glue)
        product = sp.expand(functional.T * daction)
        out.append((core, (anchor, space),
                    slice_set(support_rows(tangent)),
                    (product.rows, product.cols),
                    nonzero_entries(product)))
    return tuple(out)


@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    scope: dict
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    readings: int
    cores: dict
    consequences: dict
    fingerprints: dict
    witnesses: tuple
    parity_instances: tuple
    carrier_ranks: dict
    inverse_residuals: dict
    carrier_difference: int
    second_hodge_block: tuple
    inverse_count: int
    nsimplify_calls: int


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    authority = authority_certificate(main_head)
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""

    cores = {(width, point, core): measure_core(width, point, core)
             for point in POINTS for width in WIDTHS
             for core in CORE_DOMAIN[width]}
    consequences = {(width, core): measure_consequence(width, core)
                    for width in WIDTHS for core in CORE_DOMAIN[width]}
    carrier_ranks = {width: carrier(width, FIXTURE)["rank"] for width in WIDTHS}
    inverse_residuals = {(width, point): carrier(width, point)["inverse_residuals"]
                         for point in POINTS for width in WIDTHS}
    difference = residual_count(
        carrier(16, FIXTURE)["action"] - carrier(16, SECOND_POINT)["action"])
    second_block = imported_shear_block(rat(SECOND_POINT[1]), UNIT_VOLUME)
    second_block = tuple(
        tuple(sp.expand(second_block[row, column]) for column in range(4))
        for row in range(4))

    return Facts(
        main_head=main_head,
        authority=authority,
        scope=scope_certificate(note_text),
        imposed=len(IMPOSED_OBJECTS),
        registered=len(REGISTERED_OBJECTS),
        adopted=len(ADOPTED_OBJECTS),
        unsupplied=len(UNSUPPLIED_GRAVITY_STRUCTURES),
        readings=len(READINGS),
        cores=cores,
        consequences=consequences,
        fingerprints=measure_fingerprints(),
        witnesses=measure_witnesses(),
        parity_instances=measure_parity_instances(),
        carrier_ranks=carrier_ranks,
        inverse_residuals=inverse_residuals,
        carrier_difference=difference,
        second_hodge_block=second_block,
        inverse_count=len(_CARRIER_CACHE),
        nsimplify_calls=nsimplify_occurrences())


# ---------------------------------------------------------------------------
# THE CLAIMS, and the thirty-five mutations that each rewrite exactly one
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims = {
        # A -- authority.
        "main_head": CURRENT_MAIN,
        "parent_commit": PARENT_COMMIT,
        "stale_parent": STALE_PARENT_COMMIT,
        # B -- the banner.
        "imposed": len(IMPOSED_OBJECTS),
        "registered": 0,
        "adopted": 0,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
        "readings": len(READINGS),
        "gravity_supplied": GRAVITY_SUPPLIED_CLAIMED,
        "width_induction": WIDTH_INDUCTION_CLAIMED,
        "recurrence_derivation": RECURRENCE_DERIVATION_CLAIMED,
        "breaking_direction_proven": BREAKING_DIRECTION_PROVEN_CLAIMED,
        "generic_point_theorem": GENERIC_POINT_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C -- the construction.
        "window_rank": WINDOW_RANK,
        "carrier_ranks": dict(CARRIER_RANKS),
        "existence_residuals": (ZERO_RESIDUAL, ZERO_RESIDUAL),
        "existence_per_core": EXISTENCE_PER_CORE,
        "exact_solves": EXACT_SOLVES,
        "defect_max_nonzeros": DEFECT_MAX_NONZEROS,
        "route_stable": True,
        "core_domain": {width: tuple(CORE_DOMAIN[width]) for width in WIDTHS},
        "fingerprint_values": (BLOCK190_FINGERPRINT, BLOCK193_FINGERPRINT),
        "fingerprint_residuals": FINGERPRINT_RESIDUALS,
        # D -- the identification.
        "identification_residuals": IDENTIFICATION_RESIDUALS,
        "dual_residuals": DUAL_RESIDUALS,
        "zero_one_step_columns": ONE_STEP_ZERO_COLUMNS,
        "mechanism_is_solution": MECHANISM_IS_SOLUTION,
        # E -- exactness and the fine structure.
        "two_step_union_full": TWO_STEP_UNION_IS_FULL_WINDOW,
        "one_step_union_slices": (ONE_STEP_UNION_SLICES_ODD,
                                  ONE_STEP_UNION_SLICES_EVEN),
        "minimal_two": MINIMAL_ROWS_TWO_STEP,
        "minimal_joint": MINIMAL_ROWS_JOINT,
        "minimal_one": (MINIMAL_ROWS_ONE_STEP_ODD, MINIMAL_ROWS_ONE_STEP_EVEN),
        "deletion_tests": DELETION_TESTS,
        "subset_table": dict(SUBSET_TABLE),
        "per_column_rule": dict(PER_COLUMN_SLICE_RULE),
        "even_one_step_weight": EVEN_ONE_STEP_COLUMN_WEIGHT,
        # F -- the consequence.
        "u_containment": U_CONTAINMENT,
        "du_containment": DU_CONTAINMENT,
        "u_support_rows": U_SUPPORT_ROWS,
        "du_support_rows": DU_SUPPORT_ROWS,
        "du_missing_spatial": DU_MISSING_SPATIAL,
        "bilinear_residual": BILINEAR_IDENTITY_RESIDUAL,
        "disjoint_per_core": dict(DISJOINT_CELLS_PER_CORE),
        "disjoint_total": DISJOINT_CELLS_TOTAL,
        "disjoint_failures": DISJOINT_FAILURES,
        "parity_instances": PARITY_INSTANCES,
        "parity_shape": PARITY_INSTANCE_SHAPE,
        "witness_breaks": tuple(item[2] for item in NONVACUITY_WITNESSES),
        "witness_slices": NONVACUITY_WITNESS_SLICES,
        # G -- the second point.
        "second_hodge_block": SECOND_POINT_HODGE_BLOCK,
        "second_structure": SECOND_POINT_STRUCTURE_MATCHES,
        "second_minimal": SECOND_POINT_MINIMAL_MATCHES,
        "second_containment": SECOND_POINT_CONTAINMENT,
        "second_differs": SECOND_POINT_CARRIER_DIFFERS,
        # H -- the note, the fence and the nsimplify absence.
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
    }

    # --- A ----------------------------------------------------------------
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_commit"] = STALE_PARENT_COMMIT
    # --- B ----------------------------------------------------------------
    elif mutation == "claim_objects_registered":
        claims["registered"] = 1
        claims["adopted"] = 1
    elif mutation == "claim_gravity_supplied":
        claims["gravity_supplied"] = True
        claims["unsupplied"] = 0
    elif mutation == "claim_width_induction":
        # THE SCOPE DENIED: the per-width construction is asserted to be an
        # induction on T, i.e. to hold at every even width.  It is not -- two
        # widths are measured and nothing propagates between them.
        claims["width_induction"] = True
    elif mutation == "claim_recurrence_derivation":
        # THE NAME TAKEN LITERALLY: the law is asserted to be DERIVED from the
        # staggered recurrence.  It is not; it is solved for at each core.
        claims["recurrence_derivation"] = True
    elif mutation == "claim_breaking_direction_proven":
        # THE OTHER HALF OF THE LAW ASSERTED: the converse is asserted proven
        # here.  It is Block 193's census and stays that.
        claims["breaking_direction_proven"] = True
    elif mutation == "claim_generic_point_theorem":
        claims["generic_point_theorem"] = True
    elif mutation == "claim_continuum_limit":
        claims["continuum_limit"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_window_rank":
        claims["window_rank"] = 11
    elif mutation == "break_existence":
        claims["existence_residuals"] = (1, 0)
    elif mutation == "break_solve_route":
        claims["route_stable"] = False
    elif mutation == "break_core_domain":
        # THE CHECKER'S EXTENSION DENIED: the T = 20 domain is asserted to be
        # the solve's two spot-check cores rather than all seven valid ones.
        claims["core_domain"] = {16: CORE_DOMAIN[16],
                                 20: SOLVE_SPOT_CHECK_CORES_20}
    elif mutation == "break_landed_fingerprints":
        claims["fingerprint_residuals"] = (1, 0)
    # --- D ----------------------------------------------------------------
    elif mutation == "break_identification":
        claims["identification_residuals"] = (0, 1)
    elif mutation == "break_dual_identity":
        claims["dual_residuals"] = (1, 1)
    elif mutation == "break_mechanism_object":
        # THE IDENTIFICATION DENIED: Block 193's u_b is asserted to be merely
        # window-supported rather than the constructive solution itself.
        claims["mechanism_is_solution"] = False
    # --- E ----------------------------------------------------------------
    elif mutation == "break_two_step_union":
        claims["two_step_union_full"] = False
    elif mutation == "break_even_collapse":
        # THE FINE STRUCTURE FLATTENED: the one-step union is asserted to be all
        # three slices at BOTH parities, which is the pre-check reading.
        claims["one_step_union_slices"] = (3, 3)
    elif mutation == "break_minimality":
        claims["minimal_two"] = 8
    elif mutation == "break_joint_minimality":
        claims["minimal_joint"] = 4
    elif mutation == "break_subset_table":
        # THE CHECK'S QUALIFICATION DROPPED: every two-slice subset is asserted
        # to fail for every family, i.e. twelve rows minimal everywhere.
        claims["subset_table"] = {key: (False, False, False)
                                  for key in SUBSET_TABLE}
    # --- F ----------------------------------------------------------------
    elif mutation == "break_u_containment":
        claims["u_containment"] = False
    elif mutation == "break_du_containment":
        # THE SECOND CONDITION DROPPED: only supp(u_b) subset J is asserted,
        # which is exactly the containment that does NOT suffice.
        claims["du_containment"] = False
    elif mutation == "break_du_localization":
        claims["du_missing_spatial"] = (1, 3)
    elif mutation == "break_bilinear_identity":
        claims["bilinear_residual"] = 1
    elif mutation == "break_disjoint_census":
        claims["disjoint_total"] = 240
    elif mutation == "break_parity_instances":
        broken = list(PARITY_INSTANCES)
        broken[1] = (2, (0, 0), (0, 1, 14))
        claims["parity_instances"] = tuple(broken)
    elif mutation == "break_nonvacuity":
        # THE HYPOTHESIS ASSERTED VACUOUS: a source that MEETS the window is
        # asserted to give zero as well, which would empty the theorem.
        claims["witness_breaks"] = (0, 0, 0)
    # --- G ----------------------------------------------------------------
    elif mutation == "break_second_point_structure":
        claims["second_structure"] = False
    elif mutation == "break_second_point_minimality":
        claims["second_minimal"] = False
    elif mutation == "break_second_point_containment":
        claims["second_containment"] = False
    # --- H ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    control = tuple(facts.cores[(width, FIXTURE, core)]
                    for width in WIDTHS for core in CORE_DOMAIN[width])
    second = tuple(facts.cores[(width, SECOND_POINT, core)]
                   for width in WIDTHS for core in CORE_DOMAIN[width])
    every = control + second
    consequences = tuple(facts.consequences.values())

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 195 artifacts are "
        f"content-identical at it and in the worktree, the stale pin "
        f"{STALE_PARENT_COMMIT[:12]} is a real ancestor carrying NEITHER, the "
        f"machinery import is landed, and {authority.inputs_readable} of "
        f"{len(AUDIT_INPUT_PATHS) - 1} audit inputs are readable",
        authority.parent_pin_is_commit
        and claims["parent_commit"] == PARENT_COMMIT
        and claims["stale_parent"] == STALE_PARENT_COMMIT
        and authority.parent_ref_and_ancestry
        and authority.parent_artifact_blobs
        and not authority.stale_parent_artifact_blobs
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact
        and authority.machinery_import_landed
        and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
        and not authority.inputs_missing)

    # --- B: THE BANNER AND THE FENCE ---------------------------------------
    checks.check(
        "B-1", f"{facts.imposed} imposed objects, {claims['registered']} "
        f"registered, {claims['adopted']} adopted",
        facts.imposed == claims["imposed"]
        and facts.registered == claims["registered"]
        and facts.adopted == claims["adopted"])
    checks.check(
        "B-2", f"NO GRAVITY IS SUPPLIED: gravity_supplied = "
        f"{claims['gravity_supplied']} and {claims['unsupplied']} gravity "
        f"structures are enumerated as NOT SUPPLIED",
        claims["gravity_supplied"] is False
        and facts.unsupplied == claims["unsupplied"])
    checks.check(
        "B-3", "NO WIDTH INDUCTION: the construction is solved SEPARATELY at "
        "each of the twelve cores of T = 16 and T = 20, nothing propagates "
        "from one width to the other, and no statement is made about any "
        "other even width",
        claims["width_induction"] is False)
    checks.check(
        "B-4", "NO DERIVATION FROM THE STAGGERED RECURRENCE: 'recurrence "
        "proof' names the CONSTRUCTIVE SCHUR FORM at a fixed core -- an exact "
        "linear solve against Q^T's window rows -- and nothing here reasons "
        "from the recurrence itself",
        claims["recurrence_derivation"] is False)
    checks.check(
        "B-5", "THE BREAKING DIRECTION IS NOT PROVEN HERE: only the "
        "COMPATIBILITY direction of Block 193's law is constructive; the "
        "converse remains Block 193's exhaustive censuses of 40 cells at "
        "T = 16 and 70 at T = 20, cited and not reproved",
        claims["breaking_direction_proven"] is False)
    checks.check(
        "B-6", "NO GENERIC (m, c) THEOREM AND NO CONTINUUM: two rational "
        "points and two widths are measured, and neither a parameter space "
        "nor a limit is claimed",
        claims["generic_point_theorem"] is False
        and claims["continuum_limit"] is False)
    checks.check(
        "B-7", f"THE READINGS ARE READINGS: {claims['readings']} of them are "
        f"enumerated as readings and readings_licensed = "
        f"{claims['readings_licensed']}",
        facts.readings == claims["readings"]
        and claims["readings_licensed"] is False)
    checks.check(
        "B-8", "EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND "
        "NEVER METAPHYSICAL NECESSITY, and every positive is candidacy within "
        "this formalism and never a claim about nature -- the cycle-913 "
        "caution, carried verbatim, with nothing registered and nothing "
        "adopted",
        not REGISTERED_OBJECTS and not ADOPTED_OBJECTS
        and claims["registered"] == 0 and claims["adopted"] == 0)

    # --- C: THE CONSTRUCTION ------------------------------------------------
    checks.check(
        "C-1", f"THE VALID CORE DOMAIN IS {claims['core_domain'][16]} at "
        f"T = 16 and {claims['core_domain'][20]} at T = 20 -- Block 193's "
        f"t0 + 3 <= T/2 rule, with the T = 20 row the adversarial check's "
        f"all-core extension of the solve's spot check "
        f"{SOLVE_SPOT_CHECK_CORES_20}; {len(control)} control cores measured",
        claims["core_domain"] == {width: tuple(CORE_DOMAIN[width])
                                  for width in WIDTHS}
        and len(control) == CORE_COUNT
        and all(item.core in CORE_DOMAIN[item.width] for item in every)
        and all(item.core + 3 <= item.width // 2 for item in every))
    checks.check(
        "C-2", f"rank(Q^T[:, J(t0)]) = {claims['window_rank']} at every core "
        f"of both widths and both points, so a window-supported solution is "
        f"UNIQUE; and independently rank(Q) = {claims['carrier_ranks']} with "
        f"two-sided inverse residuals zero, from which every twelve-column "
        f"subset of the invertible Q^T is independent",
        all(item.window_rank == claims["window_rank"] for item in every)
        and facts.carrier_ranks == claims["carrier_ranks"]
        and all(value == (ZERO_RESIDUAL, ZERO_RESIDUAL)
                for value in facts.inverse_residuals.values()))
    checks.check(
        "C-3", f"EXISTENCE {claims['existence_per_core']}/"
        f"{claims['existence_per_core']} per (core, step) at BOTH steps by an "
        f"INDEPENDENT restricted solve -- rref pivot selection, a 12 x 12 "
        f"minor inverse and a residual checked against all 4T equations -- "
        f"with residuals {claims['existence_residuals']} everywhere; "
        f"{claims['exact_solves']} exact vector solves in total, on defect "
        f"columns of at most {claims['defect_max_nonzeros']} nonzeros each",
        all(item.existence == claims["existence_residuals"] for item in every)
        and len(every) * len(STEPS) * CORE_CELLS == claims["exact_solves"]
        and all(max(item.defect_weights) <= claims["defect_max_nonzeros"]
                for item in every))
    checks.check(
        "C-4", f"THE PIVOT ROUTE IS STABLE: the same twelve independent rows "
        f"serve both right-hand sides at every core "
        f"({claims['route_stable']}), so the two step families are solved "
        f"through one and the same minor",
        claims["route_stable"] is True
        and all(item.pivot_route_stable for item in every)
        and all(len(item.pivot_rows) == WINDOW_ROWS for item in every))
    checks.check(
        "C-5", f"THE REBUILT CARRIER REPRODUCES TWO LANDED NUMBERS EXACTLY: "
        f"Block 190's (W - V^2)[0,4] at T = 20, t0 = 3 and Block 193's R[0,4] "
        f"at T = 16, (t0, s, x) = (2, 5, 0), at residuals "
        f"{claims['fingerprint_residuals']}",
        (facts.fingerprints["b190_residual"],
         facts.fingerprints["b193_residual"]) == (0, 0)
        and claims["fingerprint_residuals"] == (0, 0)
        and facts.fingerprints["b190_value"] == claims["fingerprint_values"][0]
        and facts.fingerprints["b193_value"] == claims["fingerprint_values"][1])

    # --- D: THE IDENTIFICATION ---------------------------------------------
    checks.check(
        "D-1", f"PADDING THE RESTRICTED SOLUTION BY ZEROS OUTSIDE J(t0) GIVES "
        f"G^T d_b EXACTLY: residuals {claims['identification_residuals']} for "
        f"all eight columns at both steps and every core of both widths and "
        f"both points",
        all(item.identification == claims["identification_residuals"]
            for item in every))
    checks.check(
        "D-2", f"AND THE FUNCTIONAL SOLVES THE ORIGINAL SYSTEM: "
        f"nnz(Q^T u_b^(s) - d_b^(s)) = {claims['dual_residuals']} in the same "
        f"places, so the padded solution is the preimage and not merely a "
        f"window-supported vector",
        all(item.dual == claims["dual_residuals"] for item in every))
    checks.check(
        "D-3", f"BLOCK 193's MECHANISM OBJECT IS THE CONSTRUCTIVE SOLUTION "
        f"({claims['mechanism_is_solution']}): u_b = G^T d_b is not merely "
        f"SUPPORTED in the window, it IS the unique window-supported solution "
        f"of A v = d_b, by C-2 uniqueness plus D-1 agreement",
        claims["mechanism_is_solution"] is True
        and all(item.identification == (ZERO_RESIDUAL, ZERO_RESIDUAL)
                and item.window_rank == WINDOW_ROWS for item in every))
    checks.check(
        "D-4", f"THE ONE-STEP CONTENT IS EXACTLY HALF THE COLUMNS: "
        f"{claims['zero_one_step_columns']} of the eight one-step defects are "
        f"IDENTICALLY ZERO at every core -- W_1's column b for b = 0..3 is "
        f"e_(b+4) exactly, so d_b^(1) cancels entrywise -- and the content "
        f"lives in b = 4..7",
        all(item.zero_one_step_columns == claims["zero_one_step_columns"]
            for item in every)
        and all(item.per_column_counts[0][:4] == (0, 0, 0, 0)
                and all(count > 0 for count in item.per_column_counts[0][4:])
                for item in every))

    # --- E: EXACTNESS AND THE FINE STRUCTURE -------------------------------
    def per_column_matches(item: CoreFacts, name: str) -> bool:
        """THE PER-COLUMN RULE, AND IT NAMES WHICH SLICES AND NOT ONLY HOW
        MANY: a declared count of 0 demands an identically zero column, 1
        demands the window's FIRST slice exactly, and 3 demands the whole
        window."""
        expected = claims["per_column_rule"][(name, item.parity)]
        measured = item.per_column_slices[0 if name == "one" else 1]
        for count, slices in zip(expected, measured):
            if count == 0 and slices != ():
                return False
            if count == 1 and slices != (item.window[0],):
                return False
            if count == 3 and slices != item.window:
                return False
            if len(slices) != count:
                return False
        return True

    checks.check(
        "E-1", f"THE TWO-STEP SUPPORT UNION IS THE FULL TWELVE-ROW WINDOW "
        f"({claims['two_step_union_full']}) at every core of both widths and "
        f"both points -- all three slices, all four spatial sites, no "
        f"negative-half support -- with the per-column rule "
        f"{claims['per_column_rule'][('two', 'odd')]} at odd cores and "
        f"{claims['per_column_rule'][('two', 'even')]} at even cores, counted "
        f"in window slices met",
        claims["two_step_union_full"] is True
        and all(item.union_rows[1] == item.rows for item in every)
        and all(len(item.union_slices[1]) == WINDOW_SLICES for item in every)
        and all(per_column_matches(item, "two") for item in every))
    checks.check(
        "E-2", f"THE ONE-STEP UNION IS PARITY-SPLIT: "
        f"{claims['one_step_union_slices'][0]} slices at ODD cores and "
        f"{claims['one_step_union_slices'][1]} -- the window's FIRST slice "
        f"alone -- at EVEN cores, at every core of both widths and both "
        f"points; per column the rule is "
        f"{claims['per_column_rule'][('one', 'odd')]} and "
        f"{claims['per_column_rule'][('one', 'even')]}, and each nonzero "
        f"even-core column carries exactly "
        f"{claims['even_one_step_weight']} coordinates",
        all(len(item.union_slices[0])
            == claims["one_step_union_slices"][0 if item.parity == "odd" else 1]
            for item in every)
        and all(item.union_slices[0] == (item.window[0],)
                for item in every if item.parity == "even")
        and all(item.union_slices[0] == item.window
                for item in every if item.parity == "odd")
        and all(per_column_matches(item, "one") for item in every)
        and all(item.per_column_counts[0][4:]
                == (claims["even_one_step_weight"],) * 4
                for item in every if item.parity == "even"))
    checks.check(
        "E-3", f"TWELVE ROWS ARE MINIMAL FOR THE TWO-STEP FAMILY "
        f"({claims['minimal_two']}) AND FOR THE JOINT ONE-AND-TWO-STEP FAMILY "
        f"({claims['minimal_joint']}), decided EXHAUSTIVELY: every single-row "
        f"deletion fails, and every proper subset of J(t0) is contained in "
        f"one of those twelve, so no proper subset carries either family; "
        f"{claims['deletion_tests']} deletion tests in total",
        all(item.minimal_rows[1] == claims["minimal_two"] for item in every)
        and all(item.minimal_rows[2] == claims["minimal_joint"]
                for item in every)
        and all(item.droppable[1] == () and item.droppable[2] == ()
                for item in every)
        and len(every) * 3 * WINDOW_ROWS == claims["deletion_tests"])
    checks.check(
        "E-4", f"AND THE ONE-STEP FAMILY ALONE IS THE EXCEPTION, WHICH IS THE "
        f"CHECK'S QUALIFICATION CARRIED AS CONTENT: minimal rows "
        f"{claims['minimal_one'][0]} at ODD cores and "
        f"{claims['minimal_one'][1]} -- the first slice -- at EVEN cores, so "
        f"the twelve-row window is NOT minimal for one-step transport at even "
        f"cores",
        all(item.minimal_rows[0]
            == claims["minimal_one"][0 if item.parity == "odd" else 1]
            for item in every)
        and all(sorted(item.droppable[0])
                == list(range(SPACE_EXTENT, WINDOW_ROWS))
                for item in every if item.parity == "even"))
    checks.check(
        "E-5", f"THE THREE TWO-SLICE SUBSETS BEHAVE EXACTLY AS TABULATED "
        f"{claims['subset_table']} in the order first+middle, first+last, "
        f"middle+last: for the one-step family at EVEN cores the first two "
        f"solve and middle+last fails; every other row is all-False",
        all(item.subsets[0] == claims["subset_table"][("one", item.parity)]
            and item.subsets[1] == claims["subset_table"][("two", item.parity)]
            for item in every))

    # --- F: THE CONSEQUENCE -------------------------------------------------
    checks.check(
        "F-1", f"supp(u_b) subset J(t0) ({claims['u_containment']}) at every "
        f"core of both widths and both points, on all "
        f"{claims['u_support_rows']} window rows",
        claims["u_containment"] is True
        and all(item.containment[0] for item in every)
        and all(len(item.u_rows) == claims["u_support_rows"]
                for item in every))
    checks.check(
        "F-2", f"AND supp(D_s u_b) subset J(t0) ({claims['du_containment']}) "
        f"in the same places -- THE SECOND CONDITION, WITHOUT WHICH THE "
        f"CONSEQUENCE DOES NOT FOLLOW: the bilinear identity carries a "
        f"(D_s u_b)^T dH term that the first containment says nothing about",
        claims["du_containment"] is True
        and all(item.containment[1] for item in every))
    checks.check(
        "F-3", f"AND D_s u IS LOCALIZED MORE SHARPLY THAN u: exactly "
        f"{claims['du_support_rows']} of the twelve window rows, the two it "
        f"never reaches being the spatial sites "
        f"{claims['du_missing_spatial']} of the window's MIDDLE slice, at "
        f"every core of both widths and both points",
        all(len(item.du_rows) == claims["du_support_rows"] for item in every)
        and all(item.du_missing
                == (item.window[1] * SPACE_EXTENT
                    + claims["du_missing_spatial"][0],
                    item.window[1] * SPACE_EXTENT
                    + claims["du_missing_spatial"][1])
                for item in every))
    checks.check(
        "F-4", f"THE BILINEAR IDENTITY u_b^T dQ = u_b^T dH (m I + D_s) - "
        f"(D_s u_b)^T dH holds at residual {claims['bilinear_residual']} on "
        f"every census cell, so the two containments act on the two terms "
        f"they are containments for",
        all(item.identity_residual == claims["bilinear_residual"]
            for item in consequences))
    checks.check(
        "F-5", f"THE DISJOINT-SOURCE CENSUS IS EXHAUSTIVE AND CLEAN: "
        f"{claims['disjoint_per_core'][16]} cells per T = 16 core and "
        f"{claims['disjoint_per_core'][20]} per T = 20 core, "
        f"{claims['disjoint_total']} source/core cells in total, "
        f"{claims['disjoint_failures']} failures, all eight u_b at once",
        all(item.cells_checked == claims["disjoint_per_core"][item.width]
            for item in consequences)
        and sum(item.cells_checked for item in consequences)
        == claims["disjoint_total"]
        and sum(len(item.failures) for item in consequences)
        == claims["disjoint_failures"])
    checks.check(
        "F-6", f"ONE GATED INSTANCE PER PARITY AT T = 16: "
        f"{claims['parity_instances']} -- core, source cell and dH slice "
        f"support -- each giving u^T dQ = 0 as a full "
        f"{claims['parity_shape']} zero block",
        tuple((item[0], item[1], item[2]) for item in facts.parity_instances)
        == claims["parity_instances"]
        and all(item[3] == claims["parity_shape"] and item[4] == ZERO_RESIDUAL
                for item in facts.parity_instances))
    checks.check(
        "F-7", f"AND THE HYPOTHESIS IS NOT VACUOUS: three sources whose dH "
        f"slice supports {claims['witness_slices']} DO meet the window give "
        f"nnz(u^T dQ) = {claims['witness_breaks']}, all nonzero, so the "
        f"compatibility theorem separates two nonempty cases and the breaking "
        f"direction it does NOT prove is a real question",
        tuple(item[3] for item in facts.witnesses) == claims["witness_breaks"]
        and tuple(item[4] for item in facts.witnesses)
        == claims["witness_slices"]
        and all(value > 0 for value in claims["witness_breaks"])
        and all(item[2] for item in facts.witnesses))

    # --- G: THE SECOND POINT ------------------------------------------------
    signature = tuple(
        (item.core, item.window, item.window_rank, item.existence,
         item.identification, item.dual, item.union_slices,
         item.per_column_slices, item.zero_one_step_columns)
        for item in control)
    second_signature = tuple(
        (item.core, item.window, item.window_rank, item.existence,
         item.identification, item.dual, item.union_slices,
         item.per_column_slices, item.zero_one_step_columns)
        for item in second)
    checks.check(
        "G-1", f"THE STRUCTURE PERSISTS AT (m, c) = ({SECOND_POINT[0]}, "
        f"{SECOND_POINT[1]}) ({claims['second_structure']}): the whole "
        f"per-core signature -- window, rank, existence, identification, dual "
        f"residuals, both support unions, both per-column slice patterns and "
        f"the zero-column count -- is IDENTICAL on all {len(control)} cores, "
        f"on a carrier that differs from the fixture's in "
        f"{facts.carrier_difference} entries and is built from the imported "
        f"unit-volume block {claims['second_hodge_block']}",
        claims["second_structure"] is True
        and signature == second_signature
        and (facts.carrier_difference > 0) == claims["second_differs"]
        and facts.second_hodge_block == claims["second_hodge_block"])
    checks.check(
        "G-2", f"THE MINIMALITY COUNTS PERSIST TOO ({claims['second_minimal']}"
        f"): twelve rows minimal for the two-step and joint families and the "
        f"same parity-split one-step counts, with the same droppable sets, at "
        f"all {len(second)} second-point cores",
        claims["second_minimal"] is True
        and tuple(item.minimal_rows for item in control)
        == tuple(item.minimal_rows for item in second)
        and tuple(item.droppable for item in control)
        == tuple(item.droppable for item in second)
        and tuple(item.subsets for item in control)
        == tuple(item.subsets for item in second))
    checks.check(
        "G-3", f"AND BOTH CONTAINMENTS HOLD AT THE SECOND POINT "
        f"({claims['second_containment']}) -- an extension beyond the "
        f"adversarial check, which ran its C5 at the control fixture only: "
        f"supp(u_b) subset J, supp(D_s u_b) subset J and the same ten-row "
        f"middle-slice localization on all {len(second)} cores",
        claims["second_containment"] is True
        and all(item.containment == (True, True, True) for item in second))

    # --- H: THE NOTE, THE FENCE AND THE nsimplify ABSENCE -------------------
    checks.check(
        "H-1", f"the note is present at {NOTE_PATH.relative_to(ROOT)} and the "
        f"single-line N5 fence appears in it BYTE-IDENTICALLY to this "
        f"runner's own constant",
        NOTE_PATH.is_file() == claims["note_present"]
        and all(facts.scope.get(key) == claims["scope"][key]
                for key in SCOPE_KEYS))
    checks.check(
        "H-2", f"sp.nsimplify occurs {claims['nsimplify_calls']} times in this "
        f"runner's own source, MEASURED and not promised",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED")
    print(f"  elapsed: {elapsed_ns / 1000000000:.1f}s")
    print(f"  origin/main {facts.main_head}")
    print(f"  authority {facts.authority}")
    print(f"  imposed {facts.imposed}, registered {facts.registered}, "
          f"adopted {facts.adopted}, gravity structures NOT SUPPLIED "
          f"{facts.unsupplied}, readings {facts.readings}")
    print(f"  check verdict carried: {CHECK_VERDICT}")
    print(f"  exact carrier inverses built and shared: {facts.inverse_count}")
    print(f"  carrier ranks {facts.carrier_ranks}, inverse residuals "
          f"{facts.inverse_residuals}")
    print(f"  nnz(Q(9/20,5/13) - Q(1/2,1/3)) at T = 16: "
          f"{facts.carrier_difference}")
    print(f"  imported unit-volume block at c = {SECOND_POINT[1]}: "
          f"{facts.second_hodge_block}")
    print("  THE LANDED FINGERPRINTS, REBUILT")
    print(f"    b190 (W - V^2)[0,4] at T = 20, t0 = 3 = "
          f"{facts.fingerprints['b190_value']}, residual "
          f"{facts.fingerprints['b190_residual']}")
    print(f"    b193 R[0,4] at T = 16, (t0,s,x) = (2,5,0) = "
          f"{facts.fingerprints['b193_value']}, residual "
          f"{facts.fingerprints['b193_residual']}, nnz(R) = "
          f"{facts.fingerprints['b193_nnz']}")
    for point in POINTS:
        for width in WIDTHS:
            print(f"  (m, c) = ({point[0]}, {point[1]}), T = {width}")
            for core in CORE_DOMAIN[width]:
                item = facts.cores[(width, point, core)]
                print(f"    t0 = {core} ({item.parity}), W(t0) = "
                      f"{item.window}, J rows {item.rows}")
                print(f"      rank(A) {item.window_rank}, pivots "
                      f"{item.pivot_rows}, one route for both RHS "
                      f"{item.pivot_route_stable}")
                print(f"      existence residuals {item.existence}, padded vs "
                      f"G^T d {item.identification}, Q^T u - d {item.dual}, "
                      f"zero one-step columns {item.zero_one_step_columns}, "
                      f"heaviest defect columns {item.defect_weights}")
                print(f"      one-step union {item.union_slices[0]} "
                      f"({len(item.union_rows[0])} rows), two-step union "
                      f"{item.union_slices[1]} ({len(item.union_rows[1])} "
                      f"rows), joint {len(item.joint_union_rows)} rows")
                print(f"      per-column slices one {item.per_column_slices[0]}")
                print(f"      per-column slices two {item.per_column_slices[1]}")
                print(f"      per-column counts one {item.per_column_counts[0]}"
                      f", two {item.per_column_counts[1]}")
                print(f"      minimal rows (one, two, joint) "
                      f"{item.minimal_rows}, droppable {item.droppable}")
                print(f"      two-slice subsets one {item.subsets[0]}, two "
                      f"{item.subsets[1]}")
                print(f"      supp(u) {len(item.u_rows)} rows, supp(D_s u) "
                      f"{len(item.du_rows)} rows missing {item.du_missing}, "
                      f"containments {item.containment}")
    print("  THE DISJOINT-SOURCE CENSUS, EXHAUSTIVE")
    for (width, core), item in sorted(facts.consequences.items()):
        print(f"    T = {width}, t0 = {core}, W = {item.window}: "
              f"{item.cells_checked} disjoint source cells, failures "
              f"{item.failures}, bilinear identity residual "
              f"{item.identity_residual}, first instance {item.first_instance}")
    print(f"    total {sum(i.cells_checked for i in facts.consequences.values())}"
          f" source/core cells, "
          f"{sum(len(i.failures) for i in facts.consequences.values())} "
          f"failures")
    print("  THE TWO PARITY INSTANCES")
    for item in facts.parity_instances:
        print(f"    t0 = {item[0]}, source {item[1]}, dH slices {item[2]}, "
              f"u^T dQ shape {item[3]}, nnz {item[4]}")
    print("  NON-VACUITY WITNESSES (sources that DO meet the window)")
    for item in facts.witnesses:
        print(f"    t0 = {item[0]}, source {item[1]}, dH slices {item[4]}, "
              f"meets window {item[2]}, nnz(u^T dQ) {item[3]}")
    print("  READINGS, AND EACH IS A READING")
    for reading in READINGS:
        print(f"    {reading}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}")
    print("  NOT CLAIMED: NO GRAVITY. NO WIDTH INDUCTION -- TWO WIDTHS ARE NOT "
          "AN INDUCTION. NO DERIVATION FROM THE STAGGERED RECURRENCE. NO PROOF "
          "OF THE BREAKING DIRECTION -- THAT HALF OF THE LAW REMAINS BLOCK "
          "193's CENSUSES. NO GENERIC (m, c) THEOREM. NO CONTINUUM. THE "
          "READINGS ARE READINGS.")
    print()


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE PROOF LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20 (the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), BLOCK 193's CORE FRAME AND ITS TRANSPORT-DEFECT FUNCTIONALS READ AT BOTH STEPS (the eight cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_s[a,b] = G[idx(t_b + s, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, the step operators W_s = K_c^-1 L_s for s = 1 and s = 2, and the defect columns d_b^(s) = e_(t_b+s, x_b) - sum_b' W_s[b', b] e_(t_b', x_b') -- THE ONE-STEP FAMILY IS THIS BLOCK'S ADDITION), THE TWELVE WINDOW ROWS READ AS A COLUMN SET OF Q^T (J(t0) = [2 floor(t0/2)+1, 2 floor(t0/2)+3] x Z_4 and A = Q^T[:, J(t0)], IMPOSED FROM BLOCK 193's MEASURED WINDOW AND DERIVED FROM NOTHING), THE VALID CORE DOMAIN t0 + 3 <= T/2 (t0 = 1..5 at T = 16 and t0 = 1..7 at T = 20, the second being THE ADVERSARIAL CHECK's EXTENSION of the solve's two spot-check cores), BLOCK 193's REFLECTED ONE-CELL HODGE TANGENT dH(s,x) = E(s,x) dB E(s,x)^T / 4 + E(thA_s s, x) P_4 dB P_4^T E(thA_s s, x)^T / 4 with thA_s(t) = -1-t together with dQ = m dH + dH D_s - D_s^T dH, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module at UNIT VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORDS RECURRENCE PROOF AND IS SAID IN THOSE WORDS: 'RECURRENCE PROOF' NAMES THE CONSTRUCTIVE SCHUR FORM AT EACH FIXED CORE OF EACH FIXED WIDTH -- an exact linear solve of A v = d against Q^T's twelve window rows -- AND NAMES NOTHING ELSE. NO STEP HERE DERIVES ANYTHING FROM THE STAGGERED RECURRENCE AND NO STEP PROPAGATES ANYTHING FROM T TO T + 2: TWO WIDTHS ARE NOT AN INDUCTION. ONLY THE COMPATIBILITY DIRECTION OF BLOCK 193's WINDOW LAW IS PROVEN HERE; THE BREAKING DIRECTION REMAINS BLOCK 193's EXHAUSTIVE CENSUSES OF 40 CELLS AT T = 16 AND 70 AT T = 20, CITED AND NOT REPROVED, AND THIS BLOCK SAYS SO FIRST. 'WINDOW' NAMES A SET OF TWELVE ROW INDICES OF AN EXACT RATIONAL MATRIX, 'TRANSPORT DEFECT' NAMES AN EXPLICIT RATIONAL VECTOR WITH AT MOST NINE NONZERO ENTRIES, 'SOURCE' NAMES A ONE-CELL VOLUME TANGENT OF THE IMPORTED HODGE, 'UNIQUE' NAMES rank(A) = 12 AND NOTHING STRONGER, AND 'PROOF' NAMES A FINITE EXACT ARGUMENT OVER QQ ON ONE CONSTRUCTED MATRIX FAMILY. NO GENERIC (m, c) THEOREM IS SUPPLIED AND NO CONTINUUM LIMIT IS SUPPLIED: TWO WIDTHS AND TWO RATIONAL POINTS ARE NOT A LIMIT. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE SYSTEM EXISTS AND ITS SOLUTION IS UNIQUE, AND BOTH ARE EXACT. At every one of the twelve valid cores -- t0 = 1..5 at T = 16 and t0 = 1..7 at T = 20 -- and at BOTH rational points (m, c) = (9/20, 5/13) and (1/2, 1/3), the twelve-column restriction A = Q^T[:, J(t0)] has EXACT RANK 12, so a solution of A v = d supported on the window is UNIQUE whenever it exists. That uniqueness has a one-line independent proof as well: rank(Q) = 64 at T = 16 and 80 at T = 20 with two-sided inverse residuals nnz(QG - I) = nnz(GQ - I) = 0, so Q^T is invertible and EVERY twelve-column subset of it is linearly independent. AND THE SOLUTION EXISTS FOR ALL EIGHT COLUMNS AT BOTH STEPS: 8/8 per (core, step), reached by an INDEPENDENT restricted route that never touches G -- an exact rref of A^T selects twelve independent rows, the 12 x 12 minor on those rows is inverted over QQ, and the resulting x is checked against ALL 4T equations before it is padded -- at residual ZERO in every case, 384 exact vector solves in total. THE SAME TWELVE PIVOT ROWS SERVE BOTH RIGHT-HAND SIDES at every core, so the one-step and two-step families are solved through one and the same minor. THE REBUILT CARRIER IS THE LANDED ONE: it reproduces Block 190's (W - V^2)[0,4] = 53601896033238042551256/229758595220483765728625 at T = 20, t0 = 3 and Block 193's R[0,4] = 303717414128393981002946552450301011272963193469691599136505997554493148222247708710000000/77707725095998816829080256798567544217876202163787270905242891606801827087957579200283634261 at T = 16, (t0, s, x) = (2, 5, 0) with nnz(R) = 32, each at residual ZERO, and neither landed runner is imported.\\nper_mode: THE IDENTIFICATION, AND IT IS WHAT TURNS A MEASUREMENT INTO A CONSTRUCTION. Padding the restricted solution by zeros outside J(t0) gives G^T d_b ENTRYWISE: nnz(pad(v_b) - G^T d_b) = 0 for all eight columns, at both steps, at every core of both widths and both points. Together with rank(A) = 12 that says something stronger than Block 193's support fact: u_b = G^T d_b is not merely SUPPORTED in the window, it IS the unique window-supported solution of A v = d_b, so BLOCK 193's MECHANISM OBJECT IS THE CONSTRUCTIVE SOLUTION AND NOT A SEPARATE OBJECT THAT HAPPENS TO AGREE WITH ONE. The dual identity is measured in the same places: nnz(Q^T u_b^(s) - d_b^(s)) = 0, so the padded vector is a genuine preimage. AND THE ONE-STEP CONTENT IS EXACTLY HALF THE COLUMNS: FOUR of the eight one-step defects are IDENTICALLY ZERO at every core, because W_1's column b for b = 0..3 is exactly e_(b+4) -- the cell (t0+1, x_b) is already in the core, so d_b^(1) cancels entrywise -- and the whole one-step content lives in b = 4..7.\\nper_block: EXACTNESS, THE PARITY FINE STRUCTURE, AND MINIMALITY DECIDED EXHAUSTIVELY. THE TWO-STEP SUPPORT UNION IS THE FULL TWELVE-ROW WINDOW at every core of both widths and both points -- all three slices, all four spatial sites, and no negative-half support anywhere. THE ONE-STEP UNION IS PARITY-SPLIT: all three window slices at ODD cores, and at EVEN cores EXACTLY THE FOUR ROWS OF THE WINDOW'S FIRST SLICE -- slice 3 at t0 = 2, slice 5 at t0 = 4 and, in the T = 20 extension, slice 7 at t0 = 6. That single-slice collapse is the microscopic shape of the parity switch and of the shared window of the cores 2j and 2j+1. TWELVE ROWS ARE MINIMAL, AND MINIMALITY IS DECIDED AND NOT INFERRED: for the two-step family and for the JOINT one-and-two-step family, EVERY single-row deletion from J(t0) fails as an image-membership question at every core of both widths and both points, and since every proper subset of J(t0) is contained in one of those twelve deleted sets, NO PROPER SUBSET CARRIES EITHER FAMILY -- 864 deletion tests, zero droppable rows. THE ONE-STEP FAMILY ALONE IS THE EXCEPTION AND THE ADVERSARIAL CHECK FOUND IT: at even cores exactly the eight non-first-slice rows are droppable, so FOUR rows are minimal and THE TWELVE-ROW WINDOW IS NOT MINIMAL FOR ONE-STEP TRANSPORT AT EVEN CORES. The three two-slice subsets agree entry for entry: in the order first+middle, first+last, middle+last the one-step family at even cores gives (True, True, False) and every other row is (False, False, False). THAT QUALIFICATION IS CARRIED HERE AS CONTENT AND NOT AS AN ERRATUM.\\nlattice_wide: THE CONSEQUENCE, AND IT NEEDS TWO CONTAINMENTS RATHER THAN ONE -- WHICH IS THE CHECK's C5 REFINEMENT, FOLDED AS CONTENT. Block 193's bilinear reduction is R[a,b] = -u_b^T dQ G[:, theta_a], and expanding dQ = m dH + dH D_s - D_s^T dH once gives the identity u_b^T dQ = u_b^T dH (m I + D_s) - (D_s u_b)^T dH, measured here at residual ZERO on every census cell. THAT SECOND TERM IS WHY supp(u_b) subset J(t0) ALONE PROVES NOTHING: it reads D_s u_b, about which the first containment says nothing at all. BOTH CONTAINMENTS ARE EXACT: supp(u_b) subset J(t0) on all twelve window rows, and supp(D_s u_b) subset J(t0) on exactly TEN of them, the two rows it never reaches being the spatial sites 0 and 2 of the window's MIDDLE slice -- at every core of both widths and BOTH points. Since a reflected one-cell source has IDENTICAL row and column support S, a source with S disjoint from J(t0) kills both terms identically, so u_b^T dQ = 0 and R = 0 FOR THE WHOLE SOURCE-CELL FAMILY. That is a proof and not a sampled cancellation, and the sampling is done anyway as a guard: 16 disjoint source cells per T = 16 core and 24 per T = 20 core, 248 source/core cells, ZERO failures for the eight u_b simultaneously. Two instances are gated, one per parity, both at T = 16: odd t0 = 1 with window {1,2,3} and source (s,x) = (4,0) whose dH meets slices {4,5,11,12}, and even t0 = 2 with window {3,4,5} and source (s,x) = (0,0) whose dH meets slices {0,1,15}, each giving u^T dQ = 0 as a full 8 x 64 zero block. AND THE HYPOTHESIS IS NOT VACUOUS: three sources that DO meet the window give nnz(u^T dQ) = 60, 64 and 28, so the theorem separates two nonempty cases and the direction it does NOT prove is a real question.\\nper_scope: THE STRUCTURE IS OF THE CLASS AND NOT OF THE FIXTURE, AND WHAT REMAINS OPEN IS NAMED. At the second rational point (m, c) = (1/2, 1/3) the ENTIRE per-core signature is identical on all twelve cores -- window, rank, existence residuals, identification residuals, dual residuals, both support unions, both per-column slice patterns, the four zero one-step columns, all three minimality counts, the droppable sets and the two-slice table -- on a carrier that is measurably different, nnz(Q(9/20,5/13) - Q(1/2,1/3)) = 512 of 512 nonzero entries at T = 16. BOTH CONTAINMENTS HOLD AT THE SECOND POINT TOO, WHICH EXTENDS THE ADVERSARIAL CHECK: its C5 was run at the control fixture only, and the ten-row middle-slice localization of D_s u is reproduced here at (1/2, 1/3) as well. WHAT REMAINS OPEN IS NAMED AND NOT PAPERED OVER: the BREAKING direction of the law is not proven and stays Block 193's censuses; nothing here is a width induction and no argument propagates from T to T + 2, so the law for arbitrary even T is untouched; the window J(t0) is IMPOSED from Block 193's measurement and no derivation of the formula 2 floor(t0/2) + 1 from the staggering is offered; whether some OTHER twelve-row set also carries the families is NOT decided, because minimality was tested inside J(t0) and not against every row set of Q^T; the even-core single-slice collapse is MEASURED and its mechanism is NOT explained; and two rational points are not a parameter space.\\nRESULT: ON THE SITE-GLUED WIDTH FAMILY AT T = 16 AND T = 20 AND AT BOTH RATIONAL POINTS, THE TRANSPORT-DEFECT FUNCTIONALS OF EVERY VALID CORE ARE THE UNIQUE SOLUTIONS OF THE TWELVE-ROW WINDOW-RESTRICTED SYSTEM A v = d WITH A = Q^T[:, J(t0)] AND rank(A) = 12, THE PADDED SOLUTION EQUALS G^T d ENTRYWISE SO BLOCK 193's MECHANISM OBJECT IS THAT SOLUTION, THE TWELVE ROWS ARE EXHAUSTIVELY MINIMAL FOR THE TWO-STEP AND JOINT FAMILIES WHILE THE ONE-STEP FAMILY COLLAPSES TO FOUR AT EVEN CORES, AND THE TWO EXACT CONTAINMENTS supp(u_b) subset J AND supp(D_s u_b) subset J TURN THE COMPATIBILITY DIRECTION OF BLOCK 193's WINDOW LAW INTO A THEOREM FOR THE WHOLE REFLECTED ONE-CELL SOURCE FAMILY. Block 193's LAW_PROVED_FROM_RECURRENCE_CLAIMED = False is thereby narrowed and not removed: ONE DIRECTION IS NOW CONSTRUCTIVE AT TWELVE CORES OF TWO WIDTHS AND TWO POINTS, THE OTHER IS STILL A CENSUS, AND NEITHER IS A WIDTH INDUCTION. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-195 STAND EXACTLY AS LANDED. BLOCK 193 IS NOT CORRECTED: its window law, its censuses, its bilinear reduction and its two measured support facts are reproduced here, and its own named open leg is what this block half-closes. BLOCK 190 IS NOT CORRECTED: its unit-cell monodromy is used as the two-step operator and its fingerprint is reproduced digit for digit. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: TWO widths, TWO rational points, ONE profile at unit volume, ONE window formula and ONE source family -- not a scan, not a limit and not an induction; the window is IMPOSED from Block 193's measurement rather than derived; minimality is decided INSIDE J(t0) and says nothing about other row sets; the breaking direction is NOT proven; and the even-core collapse is measured without a mechanism. FOUR ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the T = 20 ALL-CORE EXTENSION from the solve's two spot-check cores to all seven valid ones; the EXHAUSTIVE MINIMALITY result for the two-step and joint families; its EVEN-CORE FOUR-ROW QUALIFICATION, which weakens the attribution if C2 is narrated step-by-step and is stated here rather than buried; and the C5 TWO-CONDITION REFINEMENT, which is the reason the consequence is proven with supp(D_s u_b) subset J and not with supp(u_b) subset J alone. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE RECURRENCE PROOF SOLVE (block 196 candidate), REC PHASE 1+2 MEASURED and B196 CHECK VERDICT anchors.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
