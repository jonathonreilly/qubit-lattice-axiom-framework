#!/usr/bin/env python3
"""BLOCK 197 -- THE HIDDEN INVOLUTIVE ISOMETRY: BLOCK 190's p = 0 / p = 2
ISOSPECTRALITY IS IMPLEMENTED BY AN EXACT INVOLUTIVE Gram ISOMETRY IN THE FULL
COMMUTANT OF THE UNIT-CELL MONODROMY, AND THAT OPERATOR IS NOT A MONOMIAL.

THE RESULT, AND ITS EXACT SCOPE.  Block 190 swept all 2048 signed monomial
candidates on a deep core, found the W-commutants to be EXACTLY {I, S, U, S^3}
with EXACTLY {I, U} of them Gram isometries, and then recorded the leftover in
its own words: the p = 0 / p = 2 equality is NOT GROUP-FORCED, it is an
ADDITIONAL exact isospectrality.  This block exhibits the operator that forces
it.

  (i) THE SECTOR SPLIT.  On the core t0 = 3 of Block 190's width family, the
      one-site spatial shift S obeys [W, S] = 0 and S^4 = I but is NOT a Gram
      isometry -- S^T K_c S - K_c has 64 nonzero entries.  Its real momentum
      projectors

        P0 = (I + S + S^2 + S^3)/4,    P2 = (I - S + S^2 - S^3)/4,
        Ph = (I - S^2)/2,

      split the U = +1 light sector into TWO two-dimensional pieces whose
      compressed monodromies W_0 and W_2 have EQUAL characteristic polynomials.
      That equality is the isospectrality, and no monomial explains it.

 (ii) AN ISOMETRIC INTERTWINER EXISTS, AND THE SOLUTION SPACE IS DECIDED.  The
      exact Sylvester system X W_0 = W_2 X has nullity 2; imposing
      X^T K_2 X = lam K_0 on that plane leaves EXACTLY TWO nonzero projective
      rays, decided by one primitive quadratic that factors over QQ.  One ray
      normalizes to lam = 1.  In the displayed column-space gauge it is
      TRIANGULAR,

        X* = [[r, 0], [s, 1]],   r = 1369/1135, s = 104/227    (control),
                                 r = 37/31,     s = 12/31      (fresh),

      and THE TRIANGLE IS A GAUGE.  Under B0 -> B0 A0, B2 -> B2 A2 the zero and
      the entries move; what does not move is the INVARIANT statement

        X* W_0 = W_2 X*    AND    X*^T K_2 X* = K_0,

      a simultaneous QQ[z]-module and Gram equivalence of the two sectors, with
      r = det X* > 0 obeying the coordinate-covariant identity
      r^2 = det K_0 / det K_2.

(iii) IT COMPLETES TO AN INVOLUTIVE ISOMETRY OF THE WHOLE CORE.  The naive
      two-block extension Y = B2 X* pi0 + B0 X*^-1 pi2 commutes with W exactly
      but has rank 4 and a 64-entry Gram defect.  The defect is NOT an
      obstruction in the light exchange -- that exchange is already exactly
      isometric on the light Gram -- it is ENTIRELY the zeroed heavy sector.
      Restoring the heavy sector by the identity gives

        Y' = B2 X* pi0 + B0 X*^-1 pi2 + Ph,

      and at both fixtures and both widths, over QQ and entrywise,

        [W, Y'] = 0,    Y'^T K_c Y' = K_c,    Y'^2 = I_8,    rank Y' = 8.

 (iv) SO THE ISOMETRIC COMMUTANT IS BIGGER THAN THE MONOMIAL ONE, AND BLOCK 190
      IS NOT CORRECTED.  Block 190's census is rebuilt here candidate for
      candidate and confirmed: EXACTLY 4 of its 2048 candidates commute with W,
      namely {I, S, U, S^3}, and EXACTLY 2 of those are Gram isometries, namely
      {I, U}.  Y' is NOT a monomial -- its rows carry four and five nonzeros --
      so it was outside that census by construction.  With U = S^2
      the four elements {I, U, Y', UY'} are exact, involutive, mutually distinct
      Gram isometries commuting with W: a Klein four-group in the isometric
      commutant, two of whose elements no monomial sweep could reach.

THE SCOPE IS A MONODROMY-LEVEL ONE AND IT IS SAID FIRST.  X* does NOT intertwine
the STEP sectors: X* V_0 - V_2 X* has 4 nonzero entries at both fixtures.  The
symmetry is a property of the pair (W, K_c) at ONE core of ONE carrier family --
which is precisely why it is invisible at the step/carrier level and why the
monomial census could not see it.

ALL OF IT IS FINITE EXACT LINEAR ALGEBRA OVER QQ AT ONE CORE OF TWO WIDTHS AND
TWO RATIONAL POINTS.  NONE OF IT SUPPLIES GRAVITY.  NONE OF IT IS A THEOREM
ABOUT A GENERIC (m, c), ABOUT ANOTHER CORE, OR ABOUT A LIMIT.

  0. THE SECTOR SPLIT (C).  The carrier reproduces Block 190's landed
     fingerprint digit for digit; K_c is exactly symmetric; [W, S] = 0 with
     S^4 = I and S^2 = U; S^T K_c S - K_c has 64 nonzeros while U is an exact
     isometry; the three sectors have dimensions 2, 2 and 4; and W_0 and W_2
     carry the SAME primitive quadratic.

  1. THE SOLUTION SPACE (D).  Sylvester nullity 2; one primitive quadratic
     whose two rational roots are the only projective branches and no branch at
     infinity; the lam = 1 branch triangular with its two exact entries; the
     other branch's lam displayed with its factorization and its NONSQUARE
     class, which is the basis-free distinction between the rays; and
     r^2 = det K_0 / det K_2 with the shear's gauge formula.

  2. THE SCOPE (E).  X* V_0 != V_2 X* with exact witnesses; Block 190's
     2048-candidate census rebuilt from its own definition, with its refuted
     reflection and its two landed witnesses reproduced; and Y' measured NOT to
     be a monomial and not to equal any censused one.

  3. THE COMPLETION (F).  Y' displayed as an exact rational 8 x 8 at both
     fixtures, its three identities at zero residual, the Klein four-group, the
     naive extension's exact defect, and the diagnosis: light exchange already
     isometric, cross blocks exactly zero, light and heavy primaries coprime,
     alpha^2 = 1 forced.

  4. GENERALITY (G).  Everything persists at T = 20, where W, V, W_p, V_p do NOT
     move and BOTH compressed Grams move in every entry -- so the branches are
     recomputed against changed data and come back the same.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GRAVITY.  NO
STEP-LEVEL OR CARRIER-LEVEL SYMMETRY.  NO BASIS-INDEPENDENT TRIANGULAR FORM.  NO
CORRECTION TO BLOCK 190.  NO GENERIC (m, c) THEOREM.  NO CONTINUUM.  THE
READINGS ARE READINGS.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 196 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: six imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, a step-level symmetry, a basis-independent
     triangle, a correction to Block 190, a generic-point theorem, the continuum
     limit and licensed readings ALL declared NOT CLAIMED as measured constants,
     and nine gravity structures enumerated as NOT SUPPLIED.
  C  THE SECTOR SPLIT: the landed fingerprint, the shift algebra and its exact
     Gram defect, the sector dimensions and eigenvalues, and the equal
     characteristic polynomials.
  D  THE SOLUTION SPACE: the Sylvester nullity, the projective certificate, the
     two branches with their exact (alpha : beta, lam) data, the triangular
     entries, the nonsquare class of the second lam, and the determinant law.
  E  THE SCOPE: the step-sector refutation with witnesses, Block 190's
     2048-candidate census rebuilt with its refuted reflection and its two
     landed witnesses, and Y' measured non-monomial.
  F  THE COMPLETION: Y' entrywise, its three identities, the Klein four-group,
     the naive extension's defect and the exact diagnosis of that defect.
  G  GENERALITY: T = 20 persistence, the exact motion of the two compressed
     Grams, and the second rational point throughout.
  H  the note at its final path, the N5 fence byte-identical, and the
     nsimplify count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through H PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: thirty-seven declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.  The per-family census is
  A 2, B 8, C 4, D 6, E 5, F 7, G 3, H 2.
  SIX OF THE THIRTY-SEVEN GUARD CORRECTIONS RATHER THAN RESULTS:
  claim_basis_independent_triangle asserts the displayed [[r,0],[s,1]] survives
  a change of sector bases; claim_b190_corrected asserts this block overturns
  Block 190's commutant census; claim_step_level_symmetry asserts X* also
  intertwines the step sectors; break_defect_diagnosis asserts the naive
  extension's Gram defect lives in the light exchange rather than in the zeroed
  heavy sector; break_square_class asserts the second branch is rationally
  normalizable to lam = 1; and break_gram_motion asserts the compressed Grams
  are width-invariant, which would make the T = 20 agreement vacuous.

RUNNING
  python3 scripts/admissibility_dirac_kahler_hidden_involutive_isometry_2026_08_26.py
  python3 ... --list-mutations
  python3 ... --mutation claim_basis_independent_triangle
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
    "ADMISSIBILITY_DIRAC_KAHLER_HIDDEN_INVOLUTIVE_ISOMETRY_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 196 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 195 tip.
BLOCK196_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WINDOW_SCHUR_TRANSPORT_DEFECT_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
BLOCK196_RUNNER = (
    "scripts/admissibility_dirac_kahler_window_schur_transport_defect_"
    "2026_08_26.py"
)
PARENT_ARTIFACTS = (BLOCK196_NOTE, BLOCK196_RUNNER)
# Refreshed by anchored sed at landing, exactly as the five pins are.
PARENT_ARTIFACT_BLOBS = (
    "1c51d871718d0029e05fe193474bfbe34ef33124",   # Block 196 note
    "0cd85964dd9bcc506bbcd768f717fb483c45c067",   # Block 196 runner
)
# THE CONSTRUCTION AUTHORITY, AND IT IS ONE NOTE: Block 190's width family,
# whose carrier, core frame, unit-cell monodromy, shift operators and
# 2048-candidate monomial census are all carried unchanged, and whose own
# recorded leftover -- the p = 0 / p = 2 equality declared NOT GROUP-FORCED --
# is the object this block resolves.  Block 191 supplies the cell-average
# assembly and Block 105 the imported Hodge.
BLOCK190_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK190_RUNNER = (
    "scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_"
    "2026_08_25.py"
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HIDDEN_INVOLUTIVE_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WINDOW_SCHUR_TRANSPORT_DEFECT_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_window_schur_transport_defect_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  RE-RESOLVED LIVE AT DRAFT TIME against the REMOTE origin/main
# of the real repository -- never against a local main ref, which sits behind it,
# and never against the verification mirror's own origin.
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block196-"
              "window-schur-transport-defect-20260826")
PARENT_COMMIT = "a3d8d7b0673c57d949d0f1944feaa2fc90877ae1"
# The Block 195 tip: a real ancestor of HEAD that predates Block 196 and
# therefore carries NEITHER Block 196 artifact.
STALE_PARENT_COMMIT = "7877b4afac1363b80ac37a28c90182c811f01da1"
# Block 196's recorded main: a real but superseded authority head.
STALE_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_step_level_symmetry",
    "claim_basis_independent_triangle",
    "claim_b190_corrected",
    "claim_generic_point_theorem",
    "claim_continuum_limit",
    "claim_readings_licensed",
    "break_landed_fingerprint",
    "break_shift_defect",
    "break_sector_dims",
    "break_isospectrality",
    "break_sylvester_dim",
    "break_branch_count",
    "break_triangular_entries",
    "break_lambda_branch",
    "break_square_class",
    "break_determinant_law",
    "break_step_scope",
    "break_monomial_census",
    "break_isometric_monomials",
    "break_reflection_refutation",
    "break_nonmonomial",
    "break_completion_matrix",
    "break_completion_identities",
    "break_klein_group",
    "break_naive_extension",
    "break_defect_diagnosis",
    "break_sector_certificates",
    "break_alpha_forcing",
    "break_width_persistence",
    "break_gram_motion",
    "break_second_point",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_step_level_symmetry": "B",
    "claim_basis_independent_triangle": "B",
    "claim_b190_corrected": "B",
    "claim_generic_point_theorem": "B",
    "claim_continuum_limit": "B",
    "claim_readings_licensed": "B",
    "break_landed_fingerprint": "C",
    "break_shift_defect": "C",
    "break_sector_dims": "C",
    "break_isospectrality": "C",
    "break_sylvester_dim": "D",
    "break_branch_count": "D",
    "break_triangular_entries": "D",
    "break_lambda_branch": "D",
    "break_square_class": "D",
    "break_determinant_law": "D",
    "break_step_scope": "E",
    "break_monomial_census": "E",
    "break_isometric_monomials": "E",
    "break_reflection_refutation": "E",
    "break_nonmonomial": "E",
    "break_completion_matrix": "F",
    "break_completion_identities": "F",
    "break_klein_group": "F",
    "break_naive_extension": "F",
    "break_defect_diagnosis": "F",
    "break_sector_certificates": "F",
    "break_alpha_forcing": "F",
    "break_width_persistence": "G",
    "break_gram_motion": "G",
    "break_second_point": "G",
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
    "BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20, CARRIED UNCHANGED: the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H",
    "BLOCK 190's CORE FRAME AT THE DEEP CORE t0 = 3, CARRIED UNCHANGED: the eight cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, the STEP operator V = K_c^-1 L_1 and the UNIT-CELL MONODROMY W = K_c^-1 L_2",
    "THE S-MOMENTUM REFINEMENT OF BLOCK 190's U-GRADING, WHICH IS THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT: the one-site spatial shift S on the core, its REAL momentum projectors P0 = (I + S + S^2 + S^3)/4 and P2 = (I - S + S^2 - S^3)/4, and the heavy projector Ph = (I - S^2)/2 -- three exact rational idempotents of ranks 2, 2 and 4 whose sum is I_8",
    "THE SECTOR COMPRESSIONS ON COLUMN-SPACE BASES: B_p a column-space basis of P_p and pi_p = (B_p^T B_p)^-1 B_p^T its exact coordinate left inverse, giving W_p = pi_p W B_p, V_p = pi_p V B_p, K_p = B_p^T K_c B_p and the CROSS Gram K_02 = B_0^T K_c B_2 -- and the whole triangular DISPLAY of X* is a property of THIS basis choice and of nothing else",
    "BLOCK 190's 2048-ELEMENT SIGNED-MONOMIAL CANDIDATE SET, REBUILT HERE AS THE CONTRAST CLASS AND NOT CITED: the eight cell permutations of the core frame -- the spatial shift Z_4 times the swap of the two time rows -- each dressed by all 256 sign diagonals",
    "THE LANDED BLOCK 105 shear_hodge(c, v) READ THROUGH THE BLOCK 128 MODULE AT UNIT VOLUME AND AT THE TWO RATIONAL SHEARS 5/13 AND 1/3 -- THE ONLY OBJECT IMPORTED -- assembled into H by Block 191's quarter-weighted four-corner cell average at Block 190's seam convention",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SEVEN ARE FALSE
# AND STAY FALSE.  THE SECOND AND THIRD ARE THE TWO THIS BLOCK'S RESULT MOST
# INVITES A READER TO ASSUME.
GRAVITY_SUPPLIED_CLAIMED = False
STEP_LEVEL_SYMMETRY_CLAIMED = False
BASIS_INDEPENDENT_TRIANGLE_CLAIMED = False
BLOCK190_CORRECTED_CLAIMED = False
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
    "R1: that the p = 0 / p = 2 isospectrality is now EXPLAINED.  Measured: it is IMPLEMENTED by an exact involutive Gram isometry in W's commutant, at one core of two widths and two rational points.  WHY the carrier admits such an isometry is NOT derived.  Reading.",
    "R2: that Y' is a symmetry of a theory.  Measured: an exact rational 8 x 8 matrix commuting with ONE core's monodromy and preserving ONE core's Gram.  It does NOT intertwine the step operators and no reconstruction is performed from it.  Reading.",
    "R3: that r is an invariant of the sector pair.  Measured: in the DISPLAYED gauge r = det X* > 0 and r^2 = det K_0 / det K_2; under independent base changes B0 -> B0 A0, B2 -> B2 A2 the number r is multiplied by det A0 / det A2.  It is coordinate-covariant, not absolute.  Reading.",
    "R4: that the isometric commutant IS the Klein four-group {I, U, Y', UY'}.  Measured: those four are exact, involutive, mutually distinct Gram isometries commuting with W.  Whether the isometric commutant is EXACTLY that group is NOT decided here.  Reading.",
    "R5: that the mechanism is a property of the width family rather than of this core and this fixture.  Measured: ONE core t0 = 3, two widths and two rational points.  Reading.",
)
CHECK_VERDICT = "HIDDEN-ISOMETRY-CONFIRMED-WITH-A-POSITIVE-P1-UPGRADE"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
WIDTHS = (16, 20)
SPACE_EXTENT = 4
CORE_CELLS = 8
DEEP_CORE = 3
UNIT_VOLUME = sp.Integer(1)

FIXTURE = ("9/20", "5/13")
SECOND_POINT = ("1/2", "1/3")
POINTS = (FIXTURE, SECOND_POINT)

# --- C: THE SECTOR SPLIT -----------------------------------------------------
CARRIER_RANKS = {16: 64, 20: 80}
# Block 190's landed witness that the monodromy is primitive, reproduced here to
# bind the rebuilt carrier to the landed one.
BLOCK190_FINGERPRINT_CORE = (20, 3)
BLOCK190_FINGERPRINT = sp.Rational(
    53601896033238042551256, 229758595220483765728625)
BLOCK190_FINGERPRINT_NNZ = 32
GRAM_SYMMETRIC_RESIDUAL = 0
SHIFT_COMMUTATOR_RESIDUAL = 0
SHIFT_ORDER_RESIDUAL = 0
# S is a commutant element and NOT a Gram isometry -- Block 190's own number.
SHIFT_GRAM_DEFECT = 64
HEAVY_INVOLUTION_GRAM_DEFECT = 0
SECTOR_DIMENSIONS = (2, 2, 4)
# S B0 = +B0, S B2 = -B2, U Bh = -Bh: the sector eigenvalue certificates.
SECTOR_EIGEN_RESIDUALS = (0, 0, 0)
ISOSPECTRAL = True
# The common LIGHT quadratic of W_0 and W_2, and the HEAVY quadratic, as
# primitive integer coefficient tuples.  Block 190's charpoly(W) is the product
# of their squares.
LIGHT_POLYNOMIAL = {
    FIXTURE: (39529825, -109432706, 39529825),
    SECOND_POINT: (233, -690, 233),
}
HEAVY_POLYNOMIAL = {
    FIXTURE: (22569375, -233631106, 22569375),
    SECOND_POINT: (739, -7258, 739),
}

# --- D: THE SOLUTION SPACE ---------------------------------------------------
SYLVESTER_DIMENSION = 2
BRANCH_COUNT = 2
INFINITY_BRANCH = False
# The single primitive quadratic that decides the projective branches, in the
# nullspace coordinate t of the measured intertwiner basis, with its exact
# factorization over QQ.  Both constraint polynomials equal it, so the two
# independent Gram-conformality equations share ONE quadratic factor.
BRANCH_QUADRATIC = {
    FIXTURE: (64358813, 329444835, -164444072),
    SECOND_POINT: (1891, 6491, -2796),
}
BRANCH_FACTORS = {
    FIXTURE: (((227, -104), 1), ((283519, 1581193), 1)),
    SECOND_POINT: (((31, -12), 1), ((61, 233), 1)),
}
# The lam = 1 branch, TRIANGULAR IN THE DISPLAYED GAUGE ONLY: X* = [[r,0],[s,1]].
TRIANGULAR_ENTRIES = {
    FIXTURE: (sp.Rational(1369, 1135), sp.Rational(104, 227)),
    SECOND_POINT: (sp.Rational(37, 31), sp.Rational(12, 31)),
}
UNIT_LAMBDA = sp.Integer(1)
# The ray coordinate alpha : beta of each branch, and the second branch's lam.
UNIT_RAY = {FIXTURE: sp.Rational(104, 227), SECOND_POINT: sp.Rational(12, 31)}
SECOND_RAY = {FIXTURE: sp.Rational(-1581193, 283519),
              SECOND_POINT: sp.Rational(-233, 61)}
SECOND_LAMBDA = {
    FIXTURE: sp.Rational(2323487131056, 80383023361),
    SECOND_POINT: sp.Rational(53816, 3721),
}
# lam scales as the SQUARE of a rescaling of X, so the square class of lam is the
# basis-free projective datum.  The unit ray is rationally normalizable; the
# other is NOT, and these are the factorizations that decide it.
SECOND_LAMBDA_NUMERATOR_FACTORS = {
    FIXTURE: {2: 4, 3: 3, 7: 1, 13: 1, 31: 1, 37: 1, 227: 2},
    SECOND_POINT: {2: 3, 7: 1, 31: 2},
}
SECOND_LAMBDA_DENOMINATOR_FACTORS = {
    FIXTURE: {283519: 2},
    SECOND_POINT: {61: 2},
}
SECOND_LAMBDA_IS_SQUARE = False
# THE DETERMINANT LAW, and it is the reason r is a Gram-VOLUME RATIO and not an
# absolute scalar: taking determinants of X*^T K_2 X* = K_0 gives r^2 det K_2 =
# det K_0.  The displayed shear obeys s = (K_0[0,1] - r K_2[0,1]) / K_2[1,1] with
# K_0[1,1] = K_2[1,1] exactly.
DETERMINANT_RATIO = {
    FIXTURE: sp.Rational(1874161, 1288225),
    SECOND_POINT: sp.Rational(1369, 961),
}
SHEAR_GAUGE_FORMULA = True
GRAM_DIAGONAL_AGREES = True
# THE GAUGE PROBE, and it is what makes the fence a measurement.  With
# A0 = [[1,1],[0,1]], A2 = [[1,0],[1,1]] the invariants survive and the ZERO in
# the upper right does NOT; with A0 = diag(2,1), A2 = I the number r itself moves.
GAUGE_A0 = ((1, 1), (0, 1))
GAUGE_A2 = ((1, 0), (1, 1))
GAUGE_SCALE_A0 = ((2, 0), (0, 1))
GAUGE_TRIANGLE_SURVIVES = False
GAUGE_INVARIANTS_SURVIVE = True
GAUGE_R_MOVES = True

# --- E: THE SCOPE ------------------------------------------------------------
# X* does NOT intertwine the step sectors, and this is the reason the mechanism
# is monodromy-level.
STEP_SCOPE_DEFECT_NNZ = 4
STEP_SCOPE_WITNESS = {
    FIXTURE: sp.Rational(-142376, 257645),
    SECOND_POINT: sp.Rational(-444, 961),
}
# Block 190's census, rebuilt candidate for candidate from ITS OWN definition:
# swap x dihedral x relative signs UP TO AN OVERALL SIGN, 2 * 8 * 2^7 = 2048.
MONOMIAL_CANDIDATES = 2048
MONOMIAL_COMMUTING = 4
MONOMIAL_ISOMETRIC = 2
COMMUTING_LABELS = ("I", "S", "S^3", "U")
ISOMETRIC_LABELS = ("I", "U")
# Nothing commuting is unnamed: a fifth element would be counted here.
CENSUS_OTHER = 0
# Block 190's refuted candidate and its two landed witnesses.  The reflection
# commutator is width-invariant because W is; the S-Gram witness is NOT, and the
# declared literal is Block 190's own, at ITS width T = 20 and ITS fixture.
REFLECTION_COMMUTATOR_NNZ = 16
REFLECTION_WITNESS = {
    FIXTURE: sp.Rational(16334218, 7905965),
    SECOND_POINT: sp.Rational(2414, 1165),
}
SHIFT_GRAM_WITNESS_CORE = (20, FIXTURE)
SHIFT_GRAM_WITNESS = sp.Rational(
    2196923328476037505923247454222973532938493206039747366330235451412004291015625,
    2814140416367857864535548440193722522538862625515710221151046656087532099673561724)
# The per-power Gram defects of the shift: I and U are isometries, S and S^3 are
# not, at exactly Block 190's 64 entries.
SHIFT_POWER_GRAM_DEFECTS = (0, 64, 0, 64)
# Y' is NOT a monomial: its rows carry four and five nonzeros.
COMPLETION_ROW_WEIGHTS = (4, 4, 4, 4, 5, 5, 5, 5)
COMPLETION_IS_MONOMIAL = False
COMPLETION_IN_CENSUS = False

# --- F: THE COMPLETION -------------------------------------------------------
# Y' = B2 X* pi0 + B0 X*^-1 pi2 + Ph, entrywise, as an integer matrix over a
# single denominator.  These are the checker's displayed matrices.
COMPLETION_FORMULA = "Y' = B2 X* pi0 + B0 X*^-1 pi2 + Ph"
COMPLETION_DENOMINATOR = {FIXTURE: 1553815, SECOND_POINT: 1147}
COMPLETION_NUMERATOR = {
    FIXTURE: (
        (1567504, 146484, 13689, 146484, 0, 0, 0, 0),
        (-146484, -13689, -146484, -1567504, 0, 0, 0, 0),
        (13689, 146484, 1567504, 146484, 0, 0, 0, 0),
        (-146484, -1567504, -146484, -13689, 0, 0, 0, 0),
        (30420, 325520, 30420, 325520, 1553815, 0, 0, 0),
        (-325520, -30420, -325520, -30420, 0, 0, 0, -1553815),
        (30420, 325520, 30420, 325520, 0, 0, 1553815, 0),
        (-325520, -30420, -325520, -30420, 0, -1553815, 0, 0),
    ),
    SECOND_POINT: (
        (1156, 102, 9, 102, 0, 0, 0, 0),
        (-102, -9, -102, -1156, 0, 0, 0, 0),
        (9, 102, 1156, 102, 0, 0, 0, 0),
        (-102, -1156, -102, -9, 0, 0, 0, 0),
        (18, 204, 18, 204, 1147, 0, 0, 0),
        (-204, -18, -204, -18, 0, 0, 0, -1147),
        (18, 204, 18, 204, 0, 0, 1147, 0),
        (-204, -18, -204, -18, 0, -1147, 0, 0),
    ),
}
COMPLETION_COMMUTATOR_RESIDUAL = 0
COMPLETION_GRAM_RESIDUAL = 0
COMPLETION_INVOLUTION_RESIDUAL = 0
COMPLETION_RESIDUALS = (COMPLETION_COMMUTATOR_RESIDUAL,
                        COMPLETION_GRAM_RESIDUAL,
                        COMPLETION_INVOLUTION_RESIDUAL)
COMPLETION_RANK = 8
# THE KLEIN FOUR-GROUP {I, U, Y', UY'} in the ISOMETRIC commutant.
KLEIN_ELEMENTS = 4
KLEIN_COMMUTE_RESIDUAL = 0
KLEIN_ALL_INVOLUTIVE = True
KLEIN_ALL_ISOMETRIC = True
KLEIN_ALL_COMMUTING = True
KLEIN_ALL_DISTINCT = True
# THE NAIVE TWO-BLOCK EXTENSION, Y = B2 X* pi0 + B0 (K_0^-1 X*^T K_2 / lam) pi2.
NAIVE_FORMULA = "Y = B2 X* pi0 + B0 (K_0^-1 X*^T K_2 / lam) pi2"
NAIVE_COMMUTATOR_RESIDUAL = 0
NAIVE_RANK = 4
NAIVE_GRAM_DEFECT_NNZ = 64
NAIVE_GRAM_WITNESS = {
    FIXTURE: sp.Rational(
        -48976132744478519489329652146311862124282444534250707666015625,
        33997719455893540048957560867825104440683420084306798815764692622),
    SECOND_POINT: sp.Rational(
        -15161098351719976229483059, 10899840437709830045206044732),
}
# THE DIAGNOSIS: the 64-entry defect is ENTIRELY the omitted heavy block.  The
# light exchange is already an exact isometry of the light Gram, and the identity
# on the heavy sector both commutes with W_h and preserves K_h.
LIGHT_EXCHANGE_GRAM_DEFECT = 0
HEAVY_IDENTITY_COMMUTATOR = 0
HEAVY_IDENTITY_GRAM_DEFECT = 0
# THE STRUCTURAL CERTIFICATES that make the sector-by-sector argument legitimate.
CROSS_GRAM_NNZ = 0
LIGHT_HEAVY_GRAM_CROSS_NNZ = 0
LIGHT_HEAVY_MONODROMY_CROSS_NNZ = 0
PRIMARY_GCD = (1,)
REVERSE_IS_INVERSE_RESIDUAL = 0
FRAME_RANK = 8
# alpha^2 = 1 is FORCED: the light swap [[0, X*^-1],[alpha X*, 0]] preserves the
# light Gram only at alpha = +1 and alpha = -1, and the choice alpha = +1 works.
ALPHA_ROOTS = (-1, 1)

# --- G: GENERALITY -----------------------------------------------------------
# What does NOT move between T = 16 and T = 20, and what does.
WIDTH_INVARIANT_RESIDUALS = 0
GRAM_MOTION_SECTOR = 4
GRAM_MOTION_CORE = 64
WIDTH_PERSISTENCE = True
SECOND_POINT_PERSISTENCE = True
# The exact v = 1 continuation of the imported Block 105 shear Hodge at c = 1/3,
# declared so the second point is bound to the import rather than to a rerun.
SECOND_POINT_HODGE_BLOCK = (
    (1, 0, 0, 0),
    (0, sp.Rational(9, 8), sp.Rational(-3, 8), 0),
    (0, sp.Rational(-3, 8), sp.Rational(9, 8), 0),
    (0, 0, 0, 1),
)
CARRIER_DIFFERS = True

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  This block's entire content is a set of EXACT ZERO statements --
# [W, Y'] = 0, Y'^T K_c Y' - K_c = 0, Y'^2 - I_8 = 0, X* V_0 - V_2 X* != 0 -- and
# the entries in question are ratios of integers with more than sixty digits in
# the denominator.  A single such call would turn the naive extension's real
# 64-entry defect into a spurious zero and the step-scope refutation into a
# spurious symmetry.  Every mass, shear and volume here is ALREADY an exact
# sympy Rational.  Gate H counts the occurrences in this file's own source and
# requires ZERO.
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


def first_nonzero(matrix: sp.MatrixBase) -> tuple:
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if matrix[row, column] != 0:
                return row, column, matrix[row, column]
    return -1, -1, sp.Integer(0)


def rat(text: str) -> sp.Rational:
    """A rational from a plain string literal.  NOT nsimplify: sp.Rational on a
    decimal-free ratio of integers is exact by construction."""
    return sp.Rational(text)


def primitive_tuple(polynomial: sp.Expr, variable: sp.Symbol) -> tuple:
    """The integer coefficient tuple of a rational polynomial, cleared of
    denominators, divided by its content and normalized to a positive leading
    coefficient.  Two polynomials agree as PROJECTIVE data iff these agree."""
    poly = sp.Poly(sp.expand(polynomial), variable, domain=QQ)
    coefficients = [sp.Rational(value) for value in poly.all_coeffs()]
    multiplier = 1
    for value in coefficients:
        multiplier = sp.ilcm(multiplier, value.q)
    integers = [sp.Integer(value * multiplier) for value in coefficients]
    content = 0
    for value in integers:
        content = sp.igcd(content, int(value))
    integers = [value // content for value in integers]
    if integers[0] < 0:
        integers = [-value for value in integers]
    return tuple(int(value) for value in integers)


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
    shear is an exact sympy Rational and the volume is a Rational."""
    return sp.Matrix(b128.block105.shear_hodge(shear, volume))


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
              "rank": rank, "inverse": None}
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
# THE CORE FRAME AND THE S-MOMENTUM SECTORS, ALL OF THEM FORMULAS
# ---------------------------------------------------------------------------
def core_cells(core: int) -> tuple:
    return tuple((time, space) for time in (core, core + 1)
                 for space in range(SPACE_EXTENT))


def shifted_pairing(width: int, inverse: sp.Matrix, core: int,
                    step: int) -> sp.Matrix:
    """L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)]; k = 0 is K_c."""
    cells = core_cells(core)
    matrix = sp.zeros(CORE_CELLS, CORE_CELLS)
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(width, site_theta(width, row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(width, column_time + step, column_space), partner]
    return matrix


def spatial_shift(core: int) -> sp.Matrix:
    """S: the ONE-site spatial shift permutation of the eight core cells."""
    cells = core_cells(core)
    position = {cell: index for index, cell in enumerate(cells)}
    matrix = sp.zeros(CORE_CELLS, CORE_CELLS)
    for cell in cells:
        image = (cell[0], (cell[1] + 1) % SPACE_EXTENT)
        matrix[position[image], position[cell]] = 1
    return matrix


def column_basis(projector: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.hstack(*projector.columnspace())


def coordinate_left_inverse(basis: sp.Matrix) -> sp.Matrix:
    """pi = (B^T B)^-1 B^T, exact over QQ."""
    return exact_inverse(basis.T * basis) * basis.T


def compressed(basis: sp.Matrix, operator: sp.Matrix) -> sp.Matrix:
    return sp.expand(coordinate_left_inverse(basis) * operator * basis)


def compressed_gram(left: sp.Matrix, gram: sp.Matrix,
                    right: sp.Matrix | None = None) -> sp.Matrix:
    return sp.expand(left.T * gram * (left if right is None else right))


def intertwiner_basis(left: sp.Matrix, right: sp.Matrix) -> list:
    """AN EXACT LINEAR NULLSPACE, NOT A SEARCH: the four entries of X are the
    unknowns of the linear system X W_0 - W_2 X = 0 and the solution space is
    the nullspace of its 4 x 4 coefficient matrix over QQ."""
    names = sp.symbols("x00 x01 x10 x11")
    unknown = sp.Matrix(2, 2, names)
    equations = list(sp.expand(unknown * left - right * unknown))
    coefficients, right_hand = sp.linear_eq_to_matrix(equations, names)
    assert all(value == 0 for value in right_hand)
    return [sp.Matrix(2, 2, list(vector))
            for vector in coefficients.nullspace()]


@dataclass(frozen=True)
class Branch:
    x: sp.Matrix
    ray: sp.Rational
    lam: sp.Rational


def conformal_branches(basis: list, k0: sp.Matrix, k2: sp.Matrix) -> tuple:
    """EVERY nonzero projective ray of X^T K_2 X = lam K_0 on the intertwiner
    plane, with an explicit chart at infinity so no branch is lost.  Writing
    X = a X_0 + b X_1 and D = X^T K_2 X, the conformality of D to K_0 is the
    vanishing of the two 2 x 2 minors D[0,0] K_0[0,1] - D[0,1] K_0[0,0] and
    D[0,0] K_0[1,1] - D[1,1] K_0[0,0]; their gcd in the affine coordinate
    t = a/b decides the branches."""
    assert len(basis) == 2
    a, b, t = sp.symbols("a b t")
    generic = a * basis[0] + b * basis[1]
    form = sp.expand(generic.T * k2 * generic)
    constraints = [sp.expand(form[0, 0] * k0[0, 1] - form[0, 1] * k0[0, 0]),
                   sp.expand(form[0, 0] * k0[1, 1] - form[1, 1] * k0[0, 0])]
    affine = [sp.Poly(value.subs({a: t, b: 1}), t, domain=QQ)
              for value in constraints]
    common = sp.gcd(affine[0], affine[1])
    roots = sp.solve(common.as_expr(), t)
    at_infinity = all(
        sp.Poly(value, a, b, domain=QQ).eval({a: 1, b: 0}) == 0
        for value in constraints)
    candidates = [(root, root * basis[0] + basis[1]) for root in roots]
    if at_infinity:                                    # pragma: no cover
        candidates.append((sp.oo, basis[0]))
    branches = []
    for ray, candidate in candidates:
        scale = candidate[1, 1]
        normalized = candidate if scale == 0 else sp.expand(candidate / scale)
        form = sp.expand(normalized.T * k2 * normalized)
        lam = sp.cancel(form[0, 0] / k0[0, 0])
        assert form == sp.expand(lam * k0)
        branches.append(Branch(normalized, ray, sp.Rational(lam)))
    certificate = {
        "constraints": tuple(primitive_tuple(p.as_expr(), t) for p in affine),
        "gcd": primitive_tuple(common.as_expr(), t),
        "quotients": tuple(primitive_tuple(sp.div(p, common)[0].as_expr(), t)
                           for p in affine),
        "factors": tuple(sorted(
            (primitive_tuple(factor, t), power)
            for factor, power in sp.factor_list(common.as_expr(), t)[1])),
        "infinity": at_infinity,
    }
    return branches, certificate


def candidate_monomials(core: int) -> tuple:
    """BLOCK 190's EXHAUSTIVE SIGNED-MONOMIAL CANDIDATE SET, REBUILT VERBATIM
    FROM ITS LANDED DEFINITION: an optional swap of the two time layers, times
    every spatial dihedral action (4 rotations x 2 reflections), times every
    relative sign pattern UP TO AN OVERALL SIGN -- 2 * 8 * 2^7 = 2048
    matrices.  The overall-sign quotient is Block 190's convention and is why
    its commutant count is FOUR rather than eight."""
    cells = core_cells(core)
    position = {cell: index for index, cell in enumerate(cells)}
    output = []
    for swap in (False, True):
        for reflect in (False, True):
            for shift in range(SPACE_EXTENT):
                permutation = sp.zeros(CORE_CELLS, CORE_CELLS)
                for (time, space) in cells:
                    image_time = (2 * core + 1 - time) if swap else time
                    image_space = ((-space) % SPACE_EXTENT if reflect
                                   else (space + shift) % SPACE_EXTENT)
                    permutation[position[(image_time, image_space)],
                                position[(time, space)]] = 1
                for bits in range(2 ** (CORE_CELLS - 1)):
                    signs = [1] + [1 if not (bits >> k) & 1 else -1
                                   for k in range(CORE_CELLS - 1)]
                    output.append(sp.diag(*signs) * permutation)
    return tuple(output)


def spatial_reflection(core: int) -> sp.Matrix:
    """R: the unsigned spatial reflection x -> -x on the core, Block 190's
    refuted candidate."""
    cells = core_cells(core)
    position = {cell: index for index, cell in enumerate(cells)}
    matrix = sp.zeros(CORE_CELLS, CORE_CELLS)
    for (time, space) in cells:
        matrix[position[(time, (-space) % SPACE_EXTENT)],
               position[(time, space)]] = 1
    return matrix


def monomial_census(core: int, monodromy: sp.Matrix, gram: sp.Matrix,
                    shift: sp.Matrix, completion: sp.Matrix) -> dict:
    """BLOCK 190's 2048-CANDIDATE SWEEP, REBUILT: each candidate is tested for
    [W, .] = 0, then for . ^T K_c . = K_c, then for equality with the
    completion.  Anything commuting that is none of I, S, U, S^3 is counted as
    OTHER, so the census cannot silently absorb a fifth element."""
    named = {"I": sp.eye(CORE_CELLS), "S": shift,
             "U": sp.expand(shift ** 2), "S^3": sp.expand(shift ** 3)}
    commutant: set = set()
    isometry: set = set()
    other = 0
    in_census = False
    for candidate in candidate_monomials(core):
        if residual_count(completion - candidate) == 0:  # pragma: no cover
            in_census = True
        if residual_count(monodromy * candidate
                          - candidate * monodromy) != 0:
            continue
        label = next((name for name, matrix in named.items()
                      if residual_count(candidate - matrix) == 0), "OTHER")
        if label == "OTHER":                             # pragma: no cover
            other += 1
        commutant.add(label)
        if residual_count(candidate.T * gram * candidate - gram) == 0:
            isometry.add(label)
    return {
        "candidates": len(candidate_monomials(core)),
        "commuting": len(commutant),
        "isometric": len(isometry),
        "commuting_labels": tuple(sorted(commutant)),
        "isometric_labels": tuple(sorted(isometry)),
        "other": other,
        "completion_in_census": in_census,
    }


def is_monomial(matrix: sp.MatrixBase) -> bool:
    return all(sum(1 for column in range(matrix.cols)
                   if matrix[row, column] != 0) == 1
               for row in range(matrix.rows))


def row_weights(matrix: sp.MatrixBase) -> tuple:
    return tuple(sum(1 for column in range(matrix.cols)
                     if matrix[row, column] != 0)
                 for row in range(matrix.rows))


@dataclass(frozen=True)
class PointFacts:
    width: int
    point: tuple
    core: int
    gram_symmetric: int
    shift_commutator: int
    shift_order: int
    shift_square_is_u: int
    shift_gram_defect: int
    heavy_gram_defect: int
    shift_power_defects: tuple
    sector_dimensions: tuple
    sector_eigen: tuple
    light_polynomial: tuple
    heavy_polynomial: tuple
    isospectral: bool
    sylvester_dimension: int
    certificate: dict
    branches: tuple
    triangular: tuple
    unit_ray: sp.Rational
    second_ray: sp.Rational
    second_lambda: sp.Rational
    lambda_scaling: bool
    second_lambda_is_square: bool
    determinant_ratio: sp.Rational
    determinant_law: bool
    shear_gauge: bool
    gram_diagonal: bool
    gauge_triangle: bool
    gauge_invariants: bool
    gauge_r_moves: bool
    step_defect_nnz: int
    step_witness: sp.Expr
    census: dict
    reflection_defect_nnz: int
    reflection_witness: sp.Expr
    shift_gram_witness: sp.Expr
    completion_matrix: sp.Matrix
    completion_denominator: int
    completion_numerator: tuple
    completion_residuals: tuple
    completion_rank: int
    completion_row_weights: tuple
    completion_is_monomial: bool
    completion_in_census: bool
    klein: dict
    naive_commutator: int
    naive_rank: int
    naive_gram_defect: int
    naive_witness: sp.Expr
    light_exchange_defect: int
    heavy_identity: tuple
    cross_gram_nnz: int
    light_heavy_gram: int
    light_heavy_monodromy: int
    primary_gcd: tuple
    reverse_is_inverse: int
    frame_rank: int
    alpha_roots: tuple


def measure_point(width: int, point: tuple, core: int = DEEP_CORE) -> PointFacts:
    record = carrier(width, point)
    inverse = record["inverse"]
    gram = shifted_pairing(width, inverse, core, 0)
    gram_inverse = exact_inverse(gram)
    step = sp.expand(gram_inverse * shifted_pairing(width, inverse, core, 1))
    monodromy = sp.expand(
        gram_inverse * shifted_pairing(width, inverse, core, 2))

    shift = spatial_shift(core)
    identity = sp.eye(CORE_CELLS)
    even = sp.expand(shift ** 2)
    p0 = sp.expand((identity + shift + shift ** 2 + shift ** 3) / 4)
    p2 = sp.expand((identity - shift + shift ** 2 - shift ** 3) / 4)
    ph = sp.expand((identity - shift ** 2) / 2)
    b0, b2, bh = (column_basis(p) for p in (p0, p2, ph))
    pi0, pi2 = coordinate_left_inverse(b0), coordinate_left_inverse(b2)

    w0, w2 = compressed(b0, monodromy), compressed(b2, monodromy)
    v0, v2 = compressed(b0, step), compressed(b2, step)
    k0, k2 = compressed_gram(b0, gram), compressed_gram(b2, gram)
    k02 = compressed_gram(b0, gram, b2)

    variable = sp.Symbol("z")
    poly0 = primitive_tuple(w0.charpoly(variable).as_expr(), variable)
    poly2 = primitive_tuple(w2.charpoly(variable).as_expr(), variable)

    basis = intertwiner_basis(w0, w2)
    branches, certificate = conformal_branches(basis, k0, k2)
    starred = next(item for item in branches if item.lam == 1)
    other = next(item for item in branches if item.lam != 1)
    star = starred.x
    # lam is quadratic in a common rescaling of X: this is the reason the
    # SQUARE CLASS of lam, and not lam itself, is the projective datum.
    beta = sp.Symbol("beta")
    scaled = sp.expand(other.x * beta)
    scaled_form = sp.expand(scaled.T * k2 * scaled)
    lambda_scaling = sp.expand(
        sp.cancel(scaled_form[0, 0] / k0[0, 0]) - other.lam * beta ** 2) == 0
    second_is_square = bool(sp.sqrt(other.lam).is_rational)

    ratio = sp.cancel(sp.det(k0) / sp.det(k2))
    r_entry, s_entry = star[0, 0], star[1, 0]
    determinant_law = sp.cancel(sp.det(star) ** 2 - ratio) == 0
    shear_gauge = sp.cancel(
        s_entry - (k0[0, 1] - sp.det(star) * k2[0, 1]) / k2[1, 1]) == 0

    # THE GAUGE PROBE.  Under B0 -> B0 A0 and B2 -> B2 A2 the sector data
    # transforms as W_p -> A_p^-1 W_p A_p, K_p -> A_p^T K_p A_p and
    # X -> A_2^-1 X A_0.  The invariants survive; the DISPLAY does not.
    a0 = sp.Matrix([list(row) for row in GAUGE_A0])
    a2 = sp.Matrix([list(row) for row in GAUGE_A2])
    gauged = sp.expand(exact_inverse(a2) * star * a0)
    gauged_w0 = sp.expand(exact_inverse(a0) * w0 * a0)
    gauged_w2 = sp.expand(exact_inverse(a2) * w2 * a2)
    gauged_k0 = sp.expand(a0.T * k0 * a0)
    gauged_k2 = sp.expand(a2.T * k2 * a2)
    gauge_invariants = bool(
        residual_count(gauged * gauged_w0 - gauged_w2 * gauged) == 0
        and residual_count(gauged.T * gauged_k2 * gauged - gauged_k0) == 0)
    scale0 = sp.Matrix([list(row) for row in GAUGE_SCALE_A0])
    scaled_x = sp.expand(star * scale0)
    scaled_k0 = sp.expand(scale0.T * k0 * scale0)
    gauge_r_moves = bool(
        sp.cancel(sp.det(scaled_x) - sp.det(star)) != 0
        and sp.cancel(sp.det(scaled_x) ** 2
                      - sp.det(scaled_k0) / sp.det(k2)) == 0)

    scope = sp.expand(star * v0 - v2 * star)

    # THE FRAME AND ITS BLOCK STRUCTURE.
    frame = b0.row_join(b2).row_join(bh)
    frame_coordinates = sp.expand(exact_inverse(frame) * monodromy * frame)
    frame_gram = sp.expand(frame.T * gram * frame)
    light_monodromy = frame_coordinates[:4, :4]
    heavy_monodromy = frame_coordinates[4:, 4:]
    light_gram = frame_gram[:4, :4]
    heavy_gram = frame_gram[4:, 4:]
    light_squarefree = sp.Poly(
        sp.sqf_part(light_monodromy.charpoly(variable).as_expr()), variable,
        domain=QQ)
    heavy_squarefree = sp.Poly(
        sp.sqf_part(heavy_monodromy.charpoly(variable).as_expr()), variable,
        domain=QQ)
    primary_gcd = primitive_tuple(
        sp.gcd(light_squarefree, heavy_squarefree).as_expr(), variable)

    reverse = sp.expand(exact_inverse(k0) * star.T * k2)
    reverse_is_inverse = residual_count(reverse - exact_inverse(star))
    light_exchange = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), exact_inverse(star)),
        sp.Matrix.hstack(star, sp.zeros(2)))
    light_exchange_defect = residual_count(
        light_exchange.T * light_gram * light_exchange - light_gram)
    alpha = sp.Symbol("alpha")
    swap = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), exact_inverse(star)),
        sp.Matrix.hstack(alpha * star, sp.zeros(2)))
    alpha_defect = sp.expand(swap.T * light_gram * swap - light_gram)
    alpha_roots = tuple(sorted(sp.solve(alpha_defect[0, 0], alpha)))

    naive = sp.expand(b2 * star * pi0 + b0 * reverse * pi2)
    naive_gram = sp.expand(naive.T * gram * naive - gram)

    complete = sp.expand(naive + ph)
    complete_residuals = (
        residual_count(monodromy * complete - complete * monodromy),
        residual_count(complete.T * gram * complete - gram),
        residual_count(complete ** 2 - identity))
    denominator = int(sp.ilcm(*[sp.Rational(value).q for value in complete
                                if value != 0]))
    numerator = tuple(
        tuple(int(complete[row, column] * denominator) for column in range(8))
        for row in range(8))

    census = monomial_census(core, monodromy, gram, shift, complete)
    reflection = spatial_reflection(core)
    reflection_defect = sp.expand(monodromy * reflection
                                  - reflection * monodromy)
    shift_defect = sp.expand(shift.T * gram * shift - gram)

    product = sp.expand(even * complete)
    klein_members = (identity, even, complete, product)
    klein = {
        "commute": residual_count(even * complete - complete * even),
        "involutive": all(residual_count(item ** 2 - identity) == 0
                          for item in klein_members),
        "isometric": all(residual_count(item.T * gram * item - gram) == 0
                         for item in klein_members),
        "commuting": all(residual_count(monodromy * item - item * monodromy) == 0
                         for item in klein_members),
        "distinct": len({sp.ImmutableMatrix(item)
                         for item in klein_members}) == len(klein_members),
        "size": len(klein_members),
        "nonmonomial": tuple(not is_monomial(item) for item in klein_members),
    }

    return PointFacts(
        width=width, point=point, core=core,
        gram_symmetric=residual_count(gram - gram.T),
        shift_commutator=residual_count(monodromy * shift
                                        - shift * monodromy),
        shift_order=residual_count(shift ** 4 - identity),
        shift_square_is_u=residual_count(shift ** 2 - even),
        shift_gram_defect=residual_count(shift.T * gram * shift - gram),
        heavy_gram_defect=residual_count(even.T * gram * even - gram),
        shift_power_defects=tuple(
            residual_count((shift ** power).T * gram * (shift ** power) - gram)
            for power in range(4)),
        sector_dimensions=(exact_rank(p0), exact_rank(p2), exact_rank(ph)),
        sector_eigen=(residual_count(shift * b0 - b0),
                      residual_count(shift * b2 + b2),
                      residual_count(even * bh + bh)),
        light_polynomial=poly0,
        heavy_polynomial=primitive_tuple(heavy_squarefree.as_expr(), variable),
        isospectral=poly0 == poly2,
        sylvester_dimension=len(basis),
        certificate=certificate,
        branches=tuple((item.ray, item.lam) for item in branches),
        triangular=(r_entry, star[0, 1], s_entry, star[1, 1]),
        unit_ray=starred.ray,
        second_ray=other.ray,
        second_lambda=other.lam,
        lambda_scaling=lambda_scaling,
        second_lambda_is_square=second_is_square,
        determinant_ratio=ratio,
        determinant_law=determinant_law,
        shear_gauge=shear_gauge,
        gram_diagonal=k0[1, 1] == k2[1, 1],
        gauge_triangle=gauged[0, 1] == 0,
        gauge_invariants=gauge_invariants,
        gauge_r_moves=gauge_r_moves,
        step_defect_nnz=residual_count(scope),
        step_witness=first_nonzero(scope)[2],
        census=census,
        reflection_defect_nnz=nonzero_entries(reflection_defect),
        reflection_witness=reflection_defect[0, 5],
        shift_gram_witness=first_nonzero(shift_defect)[2],
        completion_matrix=complete,
        completion_denominator=denominator,
        completion_numerator=numerator,
        completion_residuals=complete_residuals,
        completion_rank=exact_rank(complete),
        completion_row_weights=row_weights(complete),
        completion_is_monomial=is_monomial(complete),
        completion_in_census=census["completion_in_census"],
        klein=klein,
        naive_commutator=residual_count(monodromy * naive
                                        - naive * monodromy),
        naive_rank=exact_rank(naive),
        naive_gram_defect=residual_count(naive_gram),
        naive_witness=first_nonzero(naive_gram)[2],
        light_exchange_defect=light_exchange_defect,
        heavy_identity=(
            residual_count(heavy_monodromy * sp.eye(4)
                           - sp.eye(4) * heavy_monodromy),
            residual_count(sp.eye(4).T * heavy_gram * sp.eye(4) - heavy_gram)),
        cross_gram_nnz=nonzero_entries(k02),
        light_heavy_gram=(nonzero_entries(frame_gram[:4, 4:])
                          + nonzero_entries(frame_gram[4:, :4])),
        light_heavy_monodromy=(nonzero_entries(frame_coordinates[:4, 4:])
                               + nonzero_entries(frame_coordinates[4:, :4])),
        primary_gcd=primary_gcd,
        reverse_is_inverse=reverse_is_inverse,
        frame_rank=exact_rank(frame),
        alpha_roots=alpha_roots)


@dataclass(frozen=True)
class MotionFacts:
    point: tuple
    monodromy: int
    step: int
    sector_monodromy: tuple
    sector_step: tuple
    sector_gram: tuple
    core_gram: int
    completion: int


def measure_motion(point: tuple) -> MotionFacts:
    """WHAT MOVES BETWEEN T = 16 AND T = 20, AND WHAT DOES NOT.  Without this
    the T = 20 agreement would be an identity rather than a persistence."""
    data = {}
    for width in WIDTHS:
        record = carrier(width, point)
        inverse = record["inverse"]
        gram = shifted_pairing(width, inverse, DEEP_CORE, 0)
        gram_inverse = exact_inverse(gram)
        step = sp.expand(gram_inverse
                         * shifted_pairing(width, inverse, DEEP_CORE, 1))
        monodromy = sp.expand(gram_inverse
                              * shifted_pairing(width, inverse, DEEP_CORE, 2))
        shift = spatial_shift(DEEP_CORE)
        identity = sp.eye(CORE_CELLS)
        p0 = sp.expand((identity + shift + shift ** 2 + shift ** 3) / 4)
        p2 = sp.expand((identity - shift + shift ** 2 - shift ** 3) / 4)
        b0, b2 = column_basis(p0), column_basis(p2)
        data[width] = {
            "K": gram, "V": step, "W": monodromy,
            "W0": compressed(b0, monodromy), "W2": compressed(b2, monodromy),
            "V0": compressed(b0, step), "V2": compressed(b2, step),
            "K0": compressed_gram(b0, gram), "K2": compressed_gram(b2, gram),
        }
    small, large = data[WIDTHS[0]], data[WIDTHS[1]]
    return MotionFacts(
        point=point,
        monodromy=residual_count(large["W"] - small["W"]),
        step=residual_count(large["V"] - small["V"]),
        sector_monodromy=(residual_count(large["W0"] - small["W0"]),
                          residual_count(large["W2"] - small["W2"])),
        sector_step=(residual_count(large["V0"] - small["V0"]),
                     residual_count(large["V2"] - small["V2"])),
        sector_gram=(residual_count(large["K0"] - small["K0"]),
                     residual_count(large["K2"] - small["K2"])),
        core_gram=residual_count(large["K"] - small["K"]),
        completion=0)


def measure_fingerprint() -> dict:
    """BLOCK 190's LANDED WITNESS, REBUILT: (W - V^2)[0,4] at T = 20, t0 = 3,
    with the primitivity count nnz(W - V^2) beside it."""
    width, core = BLOCK190_FINGERPRINT_CORE
    record = carrier(width, FIXTURE)
    inverse = record["inverse"]
    gram_inverse = exact_inverse(shifted_pairing(width, inverse, core, 0))
    step = sp.expand(gram_inverse * shifted_pairing(width, inverse, core, 1))
    monodromy = sp.expand(gram_inverse
                          * shifted_pairing(width, inverse, core, 2))
    difference = sp.expand(monodromy - step * step)
    return {"value": difference[0, 4],
            "residual": residual_count(
                sp.Matrix([[difference[0, 4] - BLOCK190_FINGERPRINT]])),
            "nnz": nonzero_entries(difference)}


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
    points: dict
    motions: dict
    fingerprint: dict
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

    points = {(width, point): measure_point(width, point)
              for point in POINTS for width in WIDTHS}
    motions = {point: measure_motion(point) for point in POINTS}
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
        points=points,
        motions=motions,
        fingerprint=measure_fingerprint(),
        carrier_ranks=carrier_ranks,
        inverse_residuals=inverse_residuals,
        carrier_difference=difference,
        second_hodge_block=second_block,
        inverse_count=len(_CARRIER_CACHE),
        nsimplify_calls=nsimplify_occurrences())


# ---------------------------------------------------------------------------
# THE CLAIMS, and the thirty-seven mutations that each rewrite exactly one
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
        "step_level_symmetry": STEP_LEVEL_SYMMETRY_CLAIMED,
        "basis_independent_triangle": BASIS_INDEPENDENT_TRIANGLE_CLAIMED,
        "b190_corrected": BLOCK190_CORRECTED_CLAIMED,
        "generic_point_theorem": GENERIC_POINT_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C -- the sector split.
        "carrier_ranks": dict(CARRIER_RANKS),
        "fingerprint_value": BLOCK190_FINGERPRINT,
        "fingerprint_nnz": BLOCK190_FINGERPRINT_NNZ,
        "gram_symmetric": GRAM_SYMMETRIC_RESIDUAL,
        "shift_commutator": SHIFT_COMMUTATOR_RESIDUAL,
        "shift_order": SHIFT_ORDER_RESIDUAL,
        "shift_gram_defect": SHIFT_GRAM_DEFECT,
        "heavy_gram_defect": HEAVY_INVOLUTION_GRAM_DEFECT,
        "sector_dimensions": SECTOR_DIMENSIONS,
        "sector_eigen": SECTOR_EIGEN_RESIDUALS,
        "isospectral": ISOSPECTRAL,
        "light_polynomial": dict(LIGHT_POLYNOMIAL),
        "heavy_polynomial": dict(HEAVY_POLYNOMIAL),
        # D -- the solution space.
        "sylvester_dimension": SYLVESTER_DIMENSION,
        "branch_count": BRANCH_COUNT,
        "infinity_branch": INFINITY_BRANCH,
        "branch_quadratic": dict(BRANCH_QUADRATIC),
        "branch_factors": dict(BRANCH_FACTORS),
        "triangular": dict(TRIANGULAR_ENTRIES),
        "unit_lambda": UNIT_LAMBDA,
        "unit_ray": dict(UNIT_RAY),
        "second_ray": dict(SECOND_RAY),
        "second_lambda": dict(SECOND_LAMBDA),
        "lambda_scaling": True,
        "second_lambda_numerator": dict(SECOND_LAMBDA_NUMERATOR_FACTORS),
        "second_lambda_denominator": dict(SECOND_LAMBDA_DENOMINATOR_FACTORS),
        "second_lambda_is_square": SECOND_LAMBDA_IS_SQUARE,
        "determinant_ratio": dict(DETERMINANT_RATIO),
        "determinant_law": True,
        "shear_gauge": SHEAR_GAUGE_FORMULA,
        "gram_diagonal": GRAM_DIAGONAL_AGREES,
        "gauge_triangle": GAUGE_TRIANGLE_SURVIVES,
        "gauge_invariants": GAUGE_INVARIANTS_SURVIVE,
        "gauge_r_moves": GAUGE_R_MOVES,
        # E -- the scope.
        "step_defect_nnz": STEP_SCOPE_DEFECT_NNZ,
        "step_witness": dict(STEP_SCOPE_WITNESS),
        "monomial_candidates": MONOMIAL_CANDIDATES,
        "monomial_commuting": MONOMIAL_COMMUTING,
        "monomial_isometric": MONOMIAL_ISOMETRIC,
        "commuting_labels": COMMUTING_LABELS,
        "isometric_labels": ISOMETRIC_LABELS,
        "census_other": CENSUS_OTHER,
        "reflection_nnz": REFLECTION_COMMUTATOR_NNZ,
        "reflection_witness": dict(REFLECTION_WITNESS),
        "shift_gram_witness": SHIFT_GRAM_WITNESS,
        "shift_power_defects": SHIFT_POWER_GRAM_DEFECTS,
        "completion_row_weights": COMPLETION_ROW_WEIGHTS,
        "completion_is_monomial": COMPLETION_IS_MONOMIAL,
        "completion_in_census": COMPLETION_IN_CENSUS,
        # F -- the completion.
        "completion_denominator": dict(COMPLETION_DENOMINATOR),
        "completion_numerator": dict(COMPLETION_NUMERATOR),
        "completion_residuals": COMPLETION_RESIDUALS,
        "completion_rank": COMPLETION_RANK,
        "klein_size": KLEIN_ELEMENTS,
        "klein_commute": KLEIN_COMMUTE_RESIDUAL,
        "klein_flags": (KLEIN_ALL_INVOLUTIVE, KLEIN_ALL_ISOMETRIC,
                        KLEIN_ALL_COMMUTING, KLEIN_ALL_DISTINCT),
        "naive_commutator": NAIVE_COMMUTATOR_RESIDUAL,
        "naive_rank": NAIVE_RANK,
        "naive_gram_defect": NAIVE_GRAM_DEFECT_NNZ,
        "naive_witness": dict(NAIVE_GRAM_WITNESS),
        "light_exchange_defect": LIGHT_EXCHANGE_GRAM_DEFECT,
        "heavy_identity": (HEAVY_IDENTITY_COMMUTATOR,
                           HEAVY_IDENTITY_GRAM_DEFECT),
        "cross_gram_nnz": CROSS_GRAM_NNZ,
        "light_heavy_gram": LIGHT_HEAVY_GRAM_CROSS_NNZ,
        "light_heavy_monodromy": LIGHT_HEAVY_MONODROMY_CROSS_NNZ,
        "primary_gcd": PRIMARY_GCD,
        "reverse_is_inverse": REVERSE_IS_INVERSE_RESIDUAL,
        "frame_rank": FRAME_RANK,
        "alpha_roots": ALPHA_ROOTS,
        # G -- generality.
        "width_invariant": WIDTH_INVARIANT_RESIDUALS,
        "gram_motion_sector": GRAM_MOTION_SECTOR,
        "gram_motion_core": GRAM_MOTION_CORE,
        "width_persistence": WIDTH_PERSISTENCE,
        "second_point_persistence": SECOND_POINT_PERSISTENCE,
        "second_hodge_block": SECOND_POINT_HODGE_BLOCK,
        "carrier_differs": CARRIER_DIFFERS,
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
    elif mutation == "claim_step_level_symmetry":
        # THE SCOPE DENIED: X* is asserted to intertwine the STEP sectors too,
        # which would make the symmetry carrier-level.  It does not.
        claims["step_level_symmetry"] = True
    elif mutation == "claim_basis_independent_triangle":
        # THE CHECK'S P2 DENIED: the displayed [[r,0],[s,1]] is asserted to be
        # basis-independent.  A change of sector bases destroys it.
        claims["basis_independent_triangle"] = True
    elif mutation == "claim_b190_corrected":
        # THE PREDECESSOR MISREAD: this block is asserted to correct Block 190's
        # commutant census.  It does not -- that census classified MONOMIALS and
        # is rebuilt here unchanged.
        claims["b190_corrected"] = True
    elif mutation == "claim_generic_point_theorem":
        claims["generic_point_theorem"] = True
    elif mutation == "claim_continuum_limit":
        claims["continuum_limit"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_landed_fingerprint":
        claims["fingerprint_nnz"] = 30
    elif mutation == "break_shift_defect":
        # S ASSERTED A GRAM ISOMETRY, which would make the isospectrality
        # group-forced after all and delete the whole question.
        claims["shift_gram_defect"] = 0
    elif mutation == "break_sector_dims":
        claims["sector_dimensions"] = (4, 4, 0)
    elif mutation == "break_isospectrality":
        claims["light_polynomial"] = {
            key: (value[0], value[1] + 1, value[2])
            for key, value in LIGHT_POLYNOMIAL.items()}
    # --- D ----------------------------------------------------------------
    elif mutation == "break_sylvester_dim":
        claims["sylvester_dimension"] = 1
    elif mutation == "break_branch_count":
        claims["branch_count"] = 1
    elif mutation == "break_triangular_entries":
        claims["triangular"] = {
            key: (value[0], value[1] + 1)
            for key, value in TRIANGULAR_ENTRIES.items()}
    elif mutation == "break_lambda_branch":
        claims["second_lambda"] = {key: sp.Integer(1)
                                   for key in SECOND_LAMBDA}
    elif mutation == "break_square_class":
        # THE PROJECTIVE DISTINCTION ERASED: the second branch is asserted
        # rationally normalizable to lam = 1, i.e. the two rays are asserted to
        # be the same isometry up to scale.  Both lam numerators are nonsquare.
        claims["second_lambda_is_square"] = True
    elif mutation == "break_determinant_law":
        claims["determinant_ratio"] = {key: value + 1
                                       for key, value in
                                       DETERMINANT_RATIO.items()}
    # --- E ----------------------------------------------------------------
    elif mutation == "break_step_scope":
        # THE REFUTATION DELETED: X* V_0 - V_2 X* is asserted to vanish.
        claims["step_defect_nnz"] = 0
    elif mutation == "break_monomial_census":
        claims["monomial_commuting"] = 2
        claims["commuting_labels"] = ISOMETRIC_LABELS
    elif mutation == "break_isometric_monomials":
        # THE MONOMIAL ISOMETRIES OVERCOUNTED: all four commuting monomials are
        # asserted to be Gram isometries, i.e. S itself is asserted to be one.
        claims["monomial_isometric"] = 4
        claims["isometric_labels"] = COMMUTING_LABELS
    elif mutation == "break_reflection_refutation":
        # BLOCK 190's REFUTED CANDIDATE ASSERTED TO COMMUTE: the unsigned
        # spatial reflection is asserted to be a commutant element, which would
        # make the isospectrality reflection-forced after all.
        claims["reflection_nnz"] = 0
    elif mutation == "break_nonmonomial":
        # THE NEW ELEMENT ASSERTED OLD: Y' is asserted to be a monomial, which
        # would put it inside Block 190's census and delete the discovery.
        claims["completion_is_monomial"] = True
        claims["completion_row_weights"] = (1,) * 8
    # --- F ----------------------------------------------------------------
    elif mutation == "break_completion_matrix":
        broken = {key: tuple(
            tuple(value + (1 if (row, column) == (0, 0) else 0)
                  for column, value in enumerate(entries))
            for row, entries in enumerate(matrix))
            for key, matrix in COMPLETION_NUMERATOR.items()}
        claims["completion_numerator"] = broken
    elif mutation == "break_completion_identities":
        claims["completion_residuals"] = (0, 1, 0)
    elif mutation == "break_klein_group":
        claims["klein_size"] = 2
    elif mutation == "break_naive_extension":
        claims["naive_rank"] = 8
    elif mutation == "break_defect_diagnosis":
        # THE DIAGNOSIS INVERTED: the naive extension's 64-entry defect is
        # asserted to live in the LIGHT exchange.  It does not -- the light
        # exchange has exactly zero light-Gram defect and the whole defect is
        # the zeroed heavy sector.
        claims["light_exchange_defect"] = 64
    elif mutation == "break_sector_certificates":
        claims["cross_gram_nnz"] = 4
    elif mutation == "break_alpha_forcing":
        claims["alpha_roots"] = (-2, 2)
    # --- G ----------------------------------------------------------------
    elif mutation == "break_width_persistence":
        claims["width_persistence"] = False
    elif mutation == "break_gram_motion":
        # THE PERSISTENCE MADE VACUOUS: the compressed Grams are asserted
        # width-invariant, so the T = 20 branches would be the T = 16 branches
        # by construction rather than by recomputation.  All four entries move.
        claims["gram_motion_sector"] = 0
    elif mutation == "break_second_point":
        claims["second_point_persistence"] = False
    # --- H ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    every = tuple(facts.points.values())
    control = tuple(facts.points[(width, FIXTURE)] for width in WIDTHS)
    second = tuple(facts.points[(width, SECOND_POINT)] for width in WIDTHS)
    primary = tuple(facts.points[(WIDTHS[0], point)] for point in POINTS)
    motions = tuple(facts.motions.values())

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 196 artifacts are "
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
        "B-3", "THE SYMMETRY IS MONODROMY-LEVEL AND NOTHING WIDER: X* "
        "intertwines the two S-momentum compressions of W and does NOT "
        "intertwine those of the step operator V, so nothing here is a "
        "symmetry of the carrier, of the step, or of a theory",
        claims["step_level_symmetry"] is False)
    checks.check(
        "B-4", "THE TRIANGULAR FORM IS A BASIS GAUGE AND THE INVARIANT "
        "STATEMENT IS PRIMARY: [[r,0],[s,1]] is a property of the chosen "
        "column-space bases; what is basis-free is that X* SIMULTANEOUSLY "
        "intertwines (W_0, W_2) and identifies (K_0, K_2)",
        claims["basis_independent_triangle"] is False)
    checks.check(
        "B-5", "BLOCK 190 IS NOT CORRECTED: its census classified the SIGNED "
        "MONOMIALS and is rebuilt here candidate for candidate; Y' EXTENDS the "
        "isometric commutant BEYOND the monomials and contradicts nothing in "
        "it",
        claims["b190_corrected"] is False)
    checks.check(
        "B-6", "NO GENERIC (m, c) THEOREM AND NO CONTINUUM: one core, two "
        "widths and two rational points are measured, and neither a parameter "
        "space nor a limit is claimed",
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

    # --- C: THE SECTOR SPLIT -----------------------------------------------
    checks.check(
        "C-1", f"THE REBUILT CARRIER IS THE LANDED ONE: ranks "
        f"{claims['carrier_ranks']} with two-sided inverse residuals zero, and "
        f"Block 190's (W - V^2)[0,4] at T = 20, t0 = 3 reproduces "
        f"{claims['fingerprint_value']} with nnz(W - V^2) = "
        f"{claims['fingerprint_nnz']}",
        facts.carrier_ranks == claims["carrier_ranks"]
        and all(value == (0, 0) for value in facts.inverse_residuals.values())
        and facts.fingerprint["value"] == claims["fingerprint_value"]
        and facts.fingerprint["residual"] == ZERO_RESIDUAL
        and facts.fingerprint["nnz"] == claims["fingerprint_nnz"])
    checks.check(
        "C-2", f"THE SHIFT COMMUTES AND IS NOT AN ISOMETRY: nnz(K_c - K_c^T) = "
        f"{claims['gram_symmetric']}, nnz([W, S]) = "
        f"{claims['shift_commutator']}, nnz(S^4 - I) = {claims['shift_order']} "
        f"with S^2 = U, and nnz(S^T K_c S - K_c) = "
        f"{claims['shift_gram_defect']} while nnz(U^T K_c U - K_c) = "
        f"{claims['heavy_gram_defect']}",
        all(item.gram_symmetric == claims["gram_symmetric"]
            and item.shift_commutator == claims["shift_commutator"]
            and item.shift_order == claims["shift_order"]
            and item.shift_square_is_u == ZERO_RESIDUAL
            and item.shift_gram_defect == claims["shift_gram_defect"]
            and item.heavy_gram_defect == claims["heavy_gram_defect"]
            for item in every))
    checks.check(
        "C-3", f"THE THREE SECTORS HAVE DIMENSIONS "
        f"{claims['sector_dimensions']} and the eigenvalue certificates "
        f"S B_0 = +B_0, S B_2 = -B_2 and U B_h = -B_h hold at residuals "
        f"{claims['sector_eigen']}",
        all(item.sector_dimensions == claims["sector_dimensions"]
            and item.sector_eigen == claims["sector_eigen"]
            for item in every))
    checks.check(
        "C-4", f"THE ISOSPECTRALITY, EXACTLY: charpoly(W_0) = charpoly(W_2) as "
        f"primitive integer tuples at every width and both points, equal to "
        f"{claims['light_polynomial'][FIXTURE]} and "
        f"{claims['light_polynomial'][SECOND_POINT]}, with the disjoint heavy "
        f"quadratics {claims['heavy_polynomial'][FIXTURE]} and "
        f"{claims['heavy_polynomial'][SECOND_POINT]}",
        all(item.isospectral is claims["isospectral"]
            and item.light_polynomial == claims["light_polynomial"][item.point]
            and item.heavy_polynomial == claims["heavy_polynomial"][item.point]
            for item in every))

    # --- D: THE SOLUTION SPACE ---------------------------------------------
    checks.check(
        "D-1", f"THE SYLVESTER SPACE HAS EXACT DIMENSION "
        f"{claims['sylvester_dimension']} at every width and both points -- "
        f"the nullity of the 4 x 4 coefficient matrix of X W_0 - W_2 X = 0 "
        f"over QQ",
        all(item.sylvester_dimension == claims["sylvester_dimension"]
            for item in every))
    checks.check(
        "D-2", f"THE PROJECTIVE CERTIFICATE: the two Gram-conformality minors "
        f"share ONE primitive quadratic -- "
        f"{claims['branch_quadratic'][FIXTURE]} at the control and "
        f"{claims['branch_quadratic'][SECOND_POINT]} at the fresh point -- "
        f"which factors over QQ as {claims['branch_factors'][FIXTURE]} and "
        f"{claims['branch_factors'][SECOND_POINT]}, both quotients are units, "
        f"and there is NO branch in the chart at infinity",
        all(item.certificate["gcd"] == claims["branch_quadratic"][item.point]
            and item.certificate["factors"]
            == claims["branch_factors"][item.point]
            and all(value == claims["branch_quadratic"][item.point]
                    for value in item.certificate["constraints"])
            and all(value == (1,) for value in item.certificate["quotients"])
            and item.certificate["infinity"] is claims["infinity_branch"]
            and len(item.branches) == claims["branch_count"]
            for item in every))
    checks.check(
        "D-3", f"THE TWO RAYS, WITH THEIR EXACT (alpha : beta, lam) DATA: the "
        f"unit ray is alpha = {claims['unit_ray'][FIXTURE]} beta "
        f"({claims['unit_ray'][SECOND_POINT]} beta at the fresh point) with "
        f"lam = {claims['unit_lambda']}, the other is alpha = "
        f"{claims['second_ray'][FIXTURE]} beta "
        f"({claims['second_ray'][SECOND_POINT]} beta) with lam = "
        f"{claims['second_lambda'][FIXTURE]} "
        f"({claims['second_lambda'][SECOND_POINT]}), and lam scales as beta^2 "
        f"under a common rescaling of X",
        all(item.unit_ray == claims["unit_ray"][item.point]
            and item.second_ray == claims["second_ray"][item.point]
            and item.second_lambda == claims["second_lambda"][item.point]
            and item.lambda_scaling is claims["lambda_scaling"]
            and sorted(lam for _, lam in item.branches)
            == sorted((claims["unit_lambda"],
                       claims["second_lambda"][item.point]))
            for item in every))
    checks.check(
        "D-4", f"THE lam = 1 BRANCH IS TRIANGULAR IN THE DISPLAYED GAUGE AND "
        f"ITS TWO ENTRIES ARE EXACT: (r, s) = {claims['triangular'][FIXTURE]} "
        f"at the control and {claims['triangular'][SECOND_POINT]} at the fresh "
        f"point, with X*[0,1] = 0 and X*[1,1] = 1",
        all(item.triangular == (claims["triangular"][item.point][0],
                                sp.Integer(0),
                                claims["triangular"][item.point][1],
                                sp.Integer(1))
            for item in every))
    checks.check(
        "D-5", f"THE SQUARE CLASS SEPARATES THE RAYS AND IT IS BASIS-FREE: "
        f"rescaling X by a rational multiplies lam by a rational SQUARE, and "
        f"the second lam is NOT a rational square -- numerator "
        f"{claims['second_lambda_numerator'][FIXTURE]} over denominator "
        f"{claims['second_lambda_denominator'][FIXTURE]} at the control, "
        f"{claims['second_lambda_numerator'][SECOND_POINT]} over "
        f"{claims['second_lambda_denominator'][SECOND_POINT]} at the fresh "
        f"point",
        all(item.second_lambda_is_square is claims["second_lambda_is_square"]
            and sp.factorint(item.second_lambda.p)
            == claims["second_lambda_numerator"][item.point]
            and sp.factorint(item.second_lambda.q)
            == claims["second_lambda_denominator"][item.point]
            for item in every))
    checks.check(
        "D-6", f"THE DETERMINANT LAW AND THE GAUGE PROBE: r^2 = det K_0 / "
        f"det K_2 = {claims['determinant_ratio'][FIXTURE]} at the control and "
        f"{claims['determinant_ratio'][SECOND_POINT]} at the fresh point, "
        f"s = (K_0[0,1] - r K_2[0,1]) / K_2[1,1] with K_0[1,1] = K_2[1,1]; and "
        f"under B_0 -> B_0 A_0, B_2 -> B_2 A_2 the two invariants SURVIVE "
        f"while the upper-right zero does NOT and r itself MOVES",
        all(item.determinant_ratio == claims["determinant_ratio"][item.point]
            and item.determinant_law is claims["determinant_law"]
            and item.shear_gauge is claims["shear_gauge"]
            and item.gram_diagonal is claims["gram_diagonal"]
            and item.gauge_triangle is claims["gauge_triangle"]
            and item.gauge_invariants is claims["gauge_invariants"]
            and item.gauge_r_moves is claims["gauge_r_moves"]
            for item in every))

    # --- E: THE SCOPE ------------------------------------------------------
    checks.check(
        "E-1", f"X* DOES NOT INTERTWINE THE STEP SECTORS: "
        f"nnz(X* V_0 - V_2 X*) = {claims['step_defect_nnz']} at every width "
        f"and both points, with exact first witnesses "
        f"{claims['step_witness'][FIXTURE]} and "
        f"{claims['step_witness'][SECOND_POINT]}",
        all(item.step_defect_nnz == claims["step_defect_nnz"]
            and item.step_witness == claims["step_witness"][item.point]
            for item in every))
    checks.check(
        "E-2", f"BLOCK 190's CENSUS, REBUILT CANDIDATE FOR CANDIDATE FROM ITS "
        f"OWN DEFINITION -- swap x dihedral x relative signs up to an overall "
        f"sign, 2 * 8 * 2^7 = {claims['monomial_candidates']}: exactly "
        f"{claims['monomial_commuting']} commute with W, namely "
        f"{claims['commuting_labels']}, with {claims['census_other']} unnamed "
        f"survivors; and only {claims['monomial_isometric']} of them are Gram "
        f"isometries, namely {claims['isometric_labels']}, with per-power Gram "
        f"defects {claims['shift_power_defects']}",
        all(item.census["candidates"] == claims["monomial_candidates"]
            and item.census["commuting"] == claims["monomial_commuting"]
            and item.census["isometric"] == claims["monomial_isometric"]
            and item.census["commuting_labels"]
            == tuple(sorted(claims["commuting_labels"]))
            and item.census["isometric_labels"]
            == tuple(sorted(claims["isometric_labels"]))
            and item.census["other"] == claims["census_other"]
            and item.shift_power_defects == claims["shift_power_defects"]
            for item in every))
    checks.check(
        "E-3", f"Y' IS NOT A MONOMIAL AND IS NOT IN THE CENSUS: its row "
        f"weights are {claims['completion_row_weights']}, "
        f"is_monomial = {claims['completion_is_monomial']}, and it equals no "
        f"signed core permutation",
        all(item.completion_row_weights == claims["completion_row_weights"]
            and item.completion_is_monomial is claims["completion_is_monomial"]
            and item.completion_in_census is claims["completion_in_census"]
            for item in every))
    checks.check(
        "E-4", "SO THE MONOMIAL SWEEP COULD NOT HAVE FOUND IT, AND THAT IS THE "
        "WHOLE OF THE EXPLANATION: the isometric monomial commutant is {I, U} "
        "while Y' and UY' carry four and five nonzeros per row, so no signed "
        "monomial of the core equals either and no enlargement of the sign set "
        "would have reached them",
        all(item.census["isometric"] == MONOMIAL_ISOMETRIC
            and item.klein["nonmonomial"] == (False, False, True, True)
            for item in every))
    checks.check(
        "E-5", f"AND BLOCK 190's REFUTED CANDIDATE STAYS REFUTED, WITH ITS TWO "
        f"LANDED WITNESSES REPRODUCED: the unsigned spatial reflection has "
        f"nnz([W, R]) = {claims['reflection_nnz']} with "
        f"[W, R][0,5] = {claims['reflection_witness'][FIXTURE]} at the control "
        f"and {claims['reflection_witness'][SECOND_POINT]} at the fresh point, "
        f"and the first nonzero of S^T K_c S - K_c at T = 20 and the control "
        f"fixture is Block 190's own declared literal",
        all(item.reflection_defect_nnz == claims["reflection_nnz"]
            and item.reflection_witness
            == claims["reflection_witness"][item.point]
            for item in every)
        and facts.points[SHIFT_GRAM_WITNESS_CORE].shift_gram_witness
        == claims["shift_gram_witness"])

    # --- F: THE COMPLETION -------------------------------------------------
    checks.check(
        "F-1", f"THE COMPLETION, ENTRYWISE: {COMPLETION_FORMULA} equals the "
        f"declared integer matrix over the single denominator "
        f"{claims['completion_denominator'][FIXTURE]} at the control and "
        f"{claims['completion_denominator'][SECOND_POINT]} at the fresh point, "
        f"at every width",
        all(item.completion_denominator
            == claims["completion_denominator"][item.point]
            and item.completion_numerator
            == claims["completion_numerator"][item.point]
            for item in every))
    checks.check(
        "F-2", f"AND IT SATISFIES ALL THREE IDENTITIES EXACTLY: [W, Y'], "
        f"Y'^T K_c Y' - K_c and Y'^2 - I_8 have residuals "
        f"{claims['completion_residuals']} with rank Y' = "
        f"{claims['completion_rank']}, at every width and both points",
        all(item.completion_residuals == claims["completion_residuals"]
            and item.completion_rank == claims["completion_rank"]
            for item in every))
    checks.check(
        "F-3", f"THE ISOMETRIC COMMUTANT CONTAINS A KLEIN FOUR-GROUP: "
        f"{claims['klein_size']} elements {{I, U, Y', UY'}} with "
        f"nnz(UY' - Y'U) = {claims['klein_commute']}, all involutive, all "
        f"K_c-isometries, all commuting with W and all distinct",
        all(item.klein["size"] == claims["klein_size"]
            and item.klein["commute"] == claims["klein_commute"]
            and (item.klein["involutive"], item.klein["isometric"],
                 item.klein["commuting"], item.klein["distinct"])
            == claims["klein_flags"]
            for item in every))
    checks.check(
        "F-4", f"THE NAIVE TWO-BLOCK EXTENSION IS NOT THE COMPLETION: "
        f"{NAIVE_FORMULA} has nnz([W, Y]) = {claims['naive_commutator']} but "
        f"rank {claims['naive_rank']} and a Gram defect of "
        f"{claims['naive_gram_defect']} entries, with exact first witnesses "
        f"declared at T = 16 for both points",
        all(item.naive_commutator == claims["naive_commutator"]
            and item.naive_rank == claims["naive_rank"]
            and item.naive_gram_defect == claims["naive_gram_defect"]
            for item in every)
        and all(item.naive_witness == claims["naive_witness"][item.point]
                for item in primary))
    checks.check(
        "F-5", f"AND THE DEFECT IS ENTIRELY THE ZEROED HEAVY SECTOR: the light "
        f"exchange [[0, X*^-1], [X*, 0]] has light-Gram defect "
        f"{claims['light_exchange_defect']}, and the identity on the heavy "
        f"sector both commutes with W_h and preserves K_h at residuals "
        f"{claims['heavy_identity']} -- so restoring it is the whole repair",
        all(item.light_exchange_defect == claims["light_exchange_defect"]
            and item.heavy_identity == claims["heavy_identity"]
            for item in every))
    checks.check(
        "F-6", f"THE SECTOR-BY-SECTOR ARGUMENT IS LICENSED BY FOUR EXACT "
        f"CERTIFICATES: nnz(K_02) = {claims['cross_gram_nnz']}, the "
        f"light-heavy blocks of K_c and of W vanish at "
        f"{claims['light_heavy_gram']} and "
        f"{claims['light_heavy_monodromy']} entries in the frame "
        f"(B_0, B_2, B_h) of rank {claims['frame_rank']}, the light and heavy "
        f"squarefree primaries are coprime with gcd {claims['primary_gcd']}, "
        f"and K_0^-1 X*^T K_2 = X*^-1 at residual "
        f"{claims['reverse_is_inverse']}",
        all(item.cross_gram_nnz == claims["cross_gram_nnz"]
            and item.light_heavy_gram == claims["light_heavy_gram"]
            and item.light_heavy_monodromy == claims["light_heavy_monodromy"]
            and item.primary_gcd == claims["primary_gcd"]
            and item.reverse_is_inverse == claims["reverse_is_inverse"]
            and item.frame_rank == claims["frame_rank"]
            for item in every))
    checks.check(
        "F-7", f"alpha^2 = 1 IS FORCED AND NOT CHOSEN: the light swap "
        f"[[0, X*^-1], [alpha X*, 0]] preserves K_light exactly at "
        f"alpha in {claims['alpha_roots']} and nowhere else, and alpha = +1 is "
        f"the branch taken",
        all(tuple(int(value) for value in item.alpha_roots)
            == tuple(claims["alpha_roots"]) for item in every))

    # --- G: GENERALITY -----------------------------------------------------
    checks.check(
        "G-1", f"EVERYTHING PERSISTS AT T = 20: the Sylvester dimension, both "
        f"projective branches, the triangular entries, both lam values and the "
        f"completion Y' with all three identities are IDENTICAL at T = 16 and "
        f"T = 20 at both points",
        claims["width_persistence"] is True
        and all(
            facts.points[(WIDTHS[0], point)].sylvester_dimension
            == facts.points[(WIDTHS[1], point)].sylvester_dimension
            and facts.points[(WIDTHS[0], point)].branches
            == facts.points[(WIDTHS[1], point)].branches
            and facts.points[(WIDTHS[0], point)].triangular
            == facts.points[(WIDTHS[1], point)].triangular
            and facts.points[(WIDTHS[0], point)].completion_numerator
            == facts.points[(WIDTHS[1], point)].completion_numerator
            and facts.points[(WIDTHS[1], point)].completion_residuals
            == COMPLETION_RESIDUALS
            for point in POINTS))
    checks.check(
        "G-2", f"AND THE AGREEMENT IS NOT VACUOUS, BECAUSE THE DATA MOVES: W, "
        f"V, W_p and V_p are width-invariant at residual "
        f"{claims['width_invariant']}, while EACH of K_0 and K_2 moves in all "
        f"{claims['gram_motion_sector']} entries and the core Gram K_c moves "
        f"in all {claims['gram_motion_core']} -- so the T = 20 branches are "
        f"recomputed against changed Grams and return the same rays",
        all(item.monodromy == claims["width_invariant"]
            and item.step == claims["width_invariant"]
            and item.sector_monodromy == (claims["width_invariant"],) * 2
            and item.sector_step == (claims["width_invariant"],) * 2
            and item.sector_gram == (claims["gram_motion_sector"],) * 2
            and item.core_gram == claims["gram_motion_core"]
            for item in motions))
    checks.check(
        "G-3", f"AND THE SECOND RATIONAL POINT CARRIES EVERY STRUCTURAL "
        f"STATEMENT ON A CARRIER THAT DIFFERS: the imported unit-volume block "
        f"at c = 1/3 is {claims['second_hodge_block']}, "
        f"nnz(Q(9/20,5/13) - Q(1/2,1/3)) = {facts.carrier_difference} at "
        f"T = 16, and every C, D, E and F structural count above is asserted "
        f"at BOTH points rather than at the control alone",
        claims["second_point_persistence"] is True
        and facts.second_hodge_block == claims["second_hodge_block"]
        and (facts.carrier_difference > 0) is claims["carrier_differs"]
        and all(item.sylvester_dimension == SYLVESTER_DIMENSION
                and item.completion_residuals == COMPLETION_RESIDUALS
                and item.census["isometric"] == MONOMIAL_ISOMETRIC
                and item.step_defect_nnz == STEP_SCOPE_DEFECT_NNZ
                for item in second))

    # --- H: THE NOTE, THE FENCE AND THE nsimplify ABSENCE -------------------
    checks.check(
        "H-1", f"the note is present at {NOTE_PATH.name} and the N5 fence "
        f"appears in it VERBATIM as a single line",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "H-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can turn a nonzero defect into a zero one",
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
    print(f"  BLOCK 190 FINGERPRINT REBUILT: (W - V^2)[0,4] at T = 20, t0 = 3 "
          f"= {facts.fingerprint['value']}, residual "
          f"{facts.fingerprint['residual']}, nnz(W - V^2) = "
          f"{facts.fingerprint['nnz']}")
    for point in POINTS:
        for width in WIDTHS:
            item = facts.points[(width, point)]
            print(f"  (m, c) = ({point[0]}, {point[1]}), T = {width}, "
                  f"t0 = {item.core}")
            print(f"    K_c symmetric {item.gram_symmetric}, [W,S] "
                  f"{item.shift_commutator}, S^4 - I {item.shift_order}, "
                  f"S^2 = U {item.shift_square_is_u}, S^T K_c S - K_c "
                  f"{item.shift_gram_defect}, U^T K_c U - K_c "
                  f"{item.heavy_gram_defect}, shift-power Gram defects "
                  f"{item.shift_power_defects}")
            print(f"    sector dims {item.sector_dimensions}, eigen residuals "
                  f"{item.sector_eigen}, light {item.light_polynomial}, heavy "
                  f"{item.heavy_polynomial}, isospectral {item.isospectral}")
            print(f"    Sylvester dim {item.sylvester_dimension}, constraint "
                  f"polys {item.certificate['constraints']}, gcd "
                  f"{item.certificate['gcd']}, quotients "
                  f"{item.certificate['quotients']}, factors "
                  f"{item.certificate['factors']}, infinity branch "
                  f"{item.certificate['infinity']}")
            print(f"    branches (ray, lam) {item.branches}, lam scales as "
                  f"beta^2 {item.lambda_scaling}, second lam is a square "
                  f"{item.second_lambda_is_square}")
            print(f"    X* entries (r, X*[0,1], s, X*[1,1]) {item.triangular}, "
                  f"det K_0 / det K_2 {item.determinant_ratio}, r^2 law "
                  f"{item.determinant_law}, shear gauge formula "
                  f"{item.shear_gauge}, K_0[1,1] = K_2[1,1] "
                  f"{item.gram_diagonal}")
            print(f"    GAUGE PROBE: triangle survives {item.gauge_triangle}, "
                  f"invariants survive {item.gauge_invariants}, r moves under "
                  f"an unequal-determinant base change {item.gauge_r_moves}")
            print(f"    SCOPE: nnz(X* V_0 - V_2 X*) {item.step_defect_nnz}, "
                  f"first witness {item.step_witness}")
            print(f"    CENSUS: {item.census['candidates']} candidates, "
                  f"{item.census['commuting']} commuting "
                  f"{item.census['commuting_labels']}, "
                  f"{item.census['isometric']} isometric "
                  f"{item.census['isometric_labels']}, unnamed survivors "
                  f"{item.census['other']}; reflection nnz([W,R]) "
                  f"{item.reflection_defect_nnz}, [W,R][0,5] "
                  f"{item.reflection_witness}; first nonzero of "
                  f"S^T K_c S - K_c {item.shift_gram_witness}")
            print(f"    Y' = 1/{item.completion_denominator} * "
                  f"{item.completion_numerator}")
            print(f"    Y' residuals ([W,Y'], Gram, square) "
                  f"{item.completion_residuals}, rank "
                  f"{item.completion_rank}, row weights "
                  f"{item.completion_row_weights}, monomial "
                  f"{item.completion_is_monomial}, in census "
                  f"{item.completion_in_census}")
            print(f"    KLEIN {item.klein}")
            print(f"    NAIVE Y: [W,Y] {item.naive_commutator}, rank "
                  f"{item.naive_rank}, Gram defect "
                  f"{item.naive_gram_defect}, first witness "
                  f"{item.naive_witness}")
            print(f"    DIAGNOSIS: light-exchange Gram defect "
                  f"{item.light_exchange_defect}, heavy identity "
                  f"{item.heavy_identity}, K_02 {item.cross_gram_nnz}, "
                  f"light-heavy K {item.light_heavy_gram}, light-heavy W "
                  f"{item.light_heavy_monodromy}, primary gcd "
                  f"{item.primary_gcd}, K_0^-1 X*^T K_2 - X*^-1 "
                  f"{item.reverse_is_inverse}, frame rank {item.frame_rank}, "
                  f"alpha roots {item.alpha_roots}")
    print("  WHAT MOVES BETWEEN T = 16 AND T = 20")
    for point, item in facts.motions.items():
        print(f"    (m, c) = ({point[0]}, {point[1]}): W {item.monodromy}, V "
              f"{item.step}, (W_0, W_2) {item.sector_monodromy}, (V_0, V_2) "
              f"{item.sector_step}, (K_0, K_2) {item.sector_gram}, K_c "
              f"{item.core_gram}")
    print("  READINGS, AND EACH IS A READING")
    for reading in READINGS:
        print(f"    {reading}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}")
    print("  NOT CLAIMED: NO GRAVITY. NO STEP-LEVEL OR CARRIER-LEVEL SYMMETRY "
          "-- X* V_0 != V_2 X*. NO BASIS-INDEPENDENT TRIANGULAR FORM -- THE "
          "DISPLAY IS A GAUGE AND THE INVARIANT STATEMENT IS PRIMARY. NO "
          "CORRECTION TO BLOCK 190 -- ITS CENSUS CLASSIFIED THE MONOMIALS AND "
          "IS REBUILT HERE UNCHANGED. NO GENERIC (m, c) THEOREM. NO CONTINUUM. "
          "THE READINGS ARE READINGS.")
    print()


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE SCOPE OF THE WORD SYMMETRY IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20 (the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), BLOCK 190's CORE FRAME AT THE DEEP CORE t0 = 3 (the eight cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, the STEP operator V = K_c^-1 L_1 and the UNIT-CELL MONODROMY W = K_c^-1 L_2), THE S-MOMENTUM REFINEMENT OF BLOCK 190's U-GRADING, WHICH IS THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT (the one-site spatial shift S on the core, the real momentum projectors P0 = (I + S + S^2 + S^3)/4 and P2 = (I - S + S^2 - S^3)/4 and the heavy projector Ph = (I - S^2)/2, three exact rational idempotents of ranks 2, 2 and 4 summing to I_8), THE SECTOR COMPRESSIONS ON COLUMN-SPACE BASES (B_p a column-space basis of P_p and pi_p = (B_p^T B_p)^-1 B_p^T its exact coordinate left inverse, giving W_p = pi_p W B_p, V_p = pi_p V B_p, K_p = B_p^T K_c B_p and the cross Gram K_02 = B_0^T K_c B_2), BLOCK 190's 2048-ELEMENT SIGNED-MONOMIAL CANDIDATE SET REBUILT HERE FROM ITS OWN LANDED DEFINITION AS THE CONTRAST CLASS AND NOT CITED (an optional swap of the two time layers, times every spatial dihedral action of the core -- 4 rotations and 2 reflections -- times every relative sign pattern UP TO AN OVERALL SIGN, 2 * 8 * 2^7 = 2048 matrices), and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module at UNIT VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORD SYMMETRY AND IS SAID IN THOSE WORDS: 'SYMMETRY' NAMES AN EXACT RATIONAL 8 x 8 MATRIX THAT COMMUTES WITH ONE CORE's MONODROMY AND PRESERVES ONE CORE's GRAM -- IT IS A MONODROMY-LEVEL STATEMENT ABOUT THE PAIR (W, K_c) AND NAMES NOTHING ELSE. X* DOES NOT INTERTWINE THE STEP SECTORS: nnz(X* V_0 - V_2 X*) = 4 at BOTH FIXTURES AND BOTH WIDTHS, SO NOTHING HERE IS A SYMMETRY OF THE CARRIER, OF THE STEP OPERATOR, OR OF A THEORY. THE TRIANGULAR DISPLAY X* = [[r, 0], [s, 1]] IS A BASIS GAUGE AND NOT AN INVARIANT: under B_0 -> B_0 A_0 and B_2 -> B_2 A_2 the sector data transforms as W_p -> A_p^-1 W_p A_p, K_p -> A_p^T K_p A_p and X -> A_2^-1 X A_0, the upper-right ZERO does NOT survive, and r is multiplied by det A_0 / det A_2 -- BOTH MEASURED HERE ON EXPLICIT RATIONAL BASE CHANGES. THE INVARIANT STATEMENT IS PRIMARY AND IS THE ONE TO QUOTE: X* SIMULTANEOUSLY INTERTWINES (W_0, W_2) AND IDENTIFIES (K_0, K_2), i.e. X* W_0 = W_2 X* AND X*^T K_2 X* = K_0. BLOCK 190 IS NOT CORRECTED: ITS CENSUS CLASSIFIED THE SIGNED MONOMIALS, IT IS REBUILT HERE CANDIDATE FOR CANDIDATE AND CONFIRMED, AND Y' EXTENDS THE ISOMETRIC COMMUTANT BEYOND THE MONOMIALS RATHER THAN CONTRADICTING ANYTHING IN IT. NO GENERIC (m, c) THEOREM IS SUPPLIED AND NO CONTINUUM LIMIT IS SUPPLIED: ONE CORE, TWO WIDTHS AND TWO RATIONAL POINTS ARE NOT A PARAMETER SPACE AND ARE NOT A LIMIT. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE SECTOR SPLIT, AND EVERY STATEMENT IN IT IS AN EXACT ENTRY COUNT. At the deep core t0 = 3 of both widths and at BOTH rational points (m, c) = (9/20, 5/13) and (1/2, 1/3), the rebuilt carrier is the LANDED one: rank(Q) = 64 at T = 16 and 80 at T = 20 with two-sided inverse residuals ZERO, and Block 190's own witness (W - V^2)[0,4] at T = 20, t0 = 3 comes back as 53601896033238042551256/229758595220483765728625 with nnz(W - V^2) = 32, at residual ZERO and without importing that runner. THE CORE GRAM IS EXACTLY SYMMETRIC: nnz(K_c - K_c^T) = 0. THE ONE-SITE SHIFT COMMUTES AND IS NOT AN ISOMETRY, WHICH IS THE WHOLE REASON THERE IS A QUESTION: nnz([W, S]) = 0 and nnz(S^4 - I) = 0 with S^2 = U at ZERO, while nnz(S^T K_c S - K_c) = 64 -- Block 190's own number -- and nnz(U^T K_c U - K_c) = 0. So the shift GRADES the monodromy without preserving the pairing, and the p = 0 / p = 2 equality it produces is NOT forced by S being a symmetry, because S is not one. THE THREE SECTORS HAVE EXACT DIMENSIONS 2, 2 AND 4, with the eigenvalue certificates S B_0 = +B_0, S B_2 = -B_2 and U B_h = -B_h at residual ZERO -- p = 0 and p = 2 are the two REAL momentum sectors and the heavy sector is the U-ODD complement. AND THE ISOSPECTRALITY IS EXACT: charpoly(W_0) and charpoly(W_2) are the SAME primitive integer tuple, (39529825, -109432706, 39529825) at the control and (233, -690, 233) at the fresh point, disjoint from the heavy quadratics (22569375, -233631106, 22569375) and (739, -7258, 739) whose squares complete Block 190's charpoly(W).\\nper_mode: THE SOLUTION SPACE IS DECIDED AND NOT SAMPLED, AND WHAT IS DECIDED IS PROJECTIVE. The exact Sylvester system X W_0 - W_2 X = 0 is four linear equations in four unknowns over QQ and its nullity is EXACTLY 2 at every width and both points. Imposing X^T K_2 X = lam K_0 on that plane gives two 2 x 2 symmetric-form constraints; writing X = a X_0 + b X_1 and D = X^T K_2 X, the conformality is the vanishing of the minors D[0,0] K_0[0,1] - D[0,1] K_0[0,0] and D[0,0] K_0[1,1] - D[1,1] K_0[0,0], and BOTH equal ONE primitive quadratic in t = a/b: 64358813 t^2 + 329444835 t - 164444072 at the control and 1891 t^2 + 6491 t - 2796 at the fresh point, with both quotients UNITS. They factor over QQ as (227 t - 104)(283519 t + 1581193) and (31 t - 12)(61 t + 233), and the chart at infinity carries NO branch, so the count of TWO nonzero projective rays is EXHAUSTIVE and not a search result. THE UNIT RAY IS alpha = (104/227) beta at the control and (12/31) beta at the fresh point, and normalizing X[1,1] = 1 on it gives the lam = 1 isometry with X* = [[1369/1135, 0], [104/227, 1]] and [[37/31, 0], [12/31, 1]] EXACTLY. THE OTHER RAY IS alpha = -(1581193/283519) beta and -(233/61) beta with lam = 2323487131056/80383023361 and 53816/3721. lam SCALES AS beta^2 UNDER A COMMON RESCALING OF X, so lam itself is not projective data and ITS SQUARE CLASS IS: the second lam has numerator 2^4 * 3^3 * 7 * 13 * 31 * 37 * 227^2 over denominator 283519^2 at the control and 2^3 * 7 * 31^2 over 61^2 at the fresh point, both NONSQUARE in QQ, so the second ray is NOT rationally normalizable to lam = 1 and the two rays are genuinely distinct isometry classes. AND r IS A GRAM-VOLUME RATIO AND NOT AN ABSOLUTE SCALAR: taking determinants of X*^T K_2 X* = K_0 gives r^2 = det K_0 / det K_2 = 1874161/1288225 = 1369^2/1135^2 and 1369/961 = 37^2/31^2, the displayed shear obeys s = (K_0[0,1] - r K_2[0,1]) / K_2[1,1] with K_0[1,1] = K_2[1,1] exactly, and an explicit base change with det A_0 = 2, det A_2 = 1 MOVES r from 1369/1135 to 2738/1135 while the identity r^2 = det K_0 / det K_2 still holds in the new gauge.\\nper_block: THE COMPLETION, AND IT IS THE CHECK's DISCOVERY CARRIED AS CONTENT. The naive two-block extension Y = B_2 X* pi_0 + B_0 (K_0^-1 X*^T K_2 / lam) pi_2 commutes with the monodromy EXACTLY -- nnz([W, Y]) = 0 -- but has rank 4 and nnz(Y^T K_c Y - K_c) = 64, and the solve recorded that defect as a per-sector normalization mismatch and the full-core completion as OPEN. THAT DIAGNOSIS WAS WRONG AND THE REPAIR IS ONE TERM: the light exchange [[0, X*^-1], [X*, 0]] has light-Gram defect EXACTLY 0, so the entire 64-entry defect is the ZEROED HEAVY SECTOR. Restoring it by the identity gives Y' = B_2 X* pi_0 + B_0 X*^-1 pi_2 + Ph, and at BOTH fixtures and BOTH widths, over QQ and entrywise, [W, Y'] = 0, Y'^T K_c Y' = K_c, Y'^2 = I_8 and rank(Y') = 8. The exact control completion is 1/1553815 times the integer matrix with rows (1567504, 146484, 13689, 146484, 0, 0, 0, 0), (-146484, -13689, -146484, -1567504, 0, 0, 0, 0), (13689, 146484, 1567504, 146484, 0, 0, 0, 0), (-146484, -1567504, -146484, -13689, 0, 0, 0, 0), (30420, 325520, 30420, 325520, 1553815, 0, 0, 0), (-325520, -30420, -325520, -30420, 0, 0, 0, -1553815), (30420, 325520, 30420, 325520, 0, 0, 1553815, 0), (-325520, -30420, -325520, -30420, 0, -1553815, 0, 0); the fresh completion is 1/1147 times (1156, 102, 9, 102, 0, 0, 0, 0), (-102, -9, -102, -1156, 0, 0, 0, 0), (9, 102, 1156, 102, 0, 0, 0, 0), (-102, -1156, -102, -9, 0, 0, 0, 0), (18, 204, 18, 204, 1147, 0, 0, 0), (-204, -18, -204, -18, 0, 0, 0, -1147), (18, 204, 18, 204, 0, 0, 1147, 0), (-204, -18, -204, -18, 0, -1147, 0, 0). FOUR EXACT CERTIFICATES LICENSE THE SECTOR-BY-SECTOR ARGUMENT: nnz(K_02) = 0, the light-heavy blocks of K_c and of W vanish at 0 and 0 entries in the frame (B_0, B_2, B_h) of rank 8, the light and heavy squarefree primaries are COPRIME, and K_0^-1 X*^T K_2 = X*^-1 at residual 0. alpha^2 = 1 IS FORCED AND NOT CHOSEN: the light swap [[0, X*^-1], [alpha X*, 0]] preserves K_light exactly at alpha = -1 and alpha = +1 and nowhere else. AND THE ISOMETRIC COMMUTANT CONTAINS A KLEIN FOUR-GROUP: with U = S^2 the four elements {I, U, Y', UY'} are mutually distinct, all involutive, all K_c-isometries and all commuting with W, with nnz(UY' - Y'U) = 0.\\nlattice_wide: THE SCOPE IS MONODROMY-LEVEL, AND THAT IS EXACTLY WHY THE MONOMIAL CENSUS COULD NOT SEE IT. X* DOES NOT INTERTWINE THE STEP SECTORS: nnz(X* V_0 - V_2 X*) = 4 at every width and both points, with exact first witnesses -142376/257645 at the control and -444/961 at the fresh point. BLOCK 190's CENSUS IS REBUILT HERE CANDIDATE FOR CANDIDATE RATHER THAN CITED, AND FROM ITS OWN LANDED CANDIDATE DEFINITION: all 2048 candidates are swept, EXACTLY 4 commute with W -- {I, S, U, S^3}, with ZERO unnamed survivors -- and EXACTLY 2 of those are Gram isometries, {I, U}, with per-power Gram defects (0, 64, 0, 64) for S^0, S^1, S^2, S^3. BLOCK 190's REFUTED CANDIDATE STAYS REFUTED WITH ITS LANDED WITNESSES REPRODUCED: the unsigned spatial reflection R has nnz([W, R]) = 16 with [W, R][0,5] = 16334218/7905965 at the control and 2414/1165 at the fresh point, and the first nonzero of S^T K_c S - K_c at T = 20 and the control fixture is Block 190's own declared literal 2196923328476037505923247454222973532938493206039747366330235451412004291015625/2814140416367857864535548440193722522538862625515710221151046656087532099673561724. Y' IS NOT A MONOMIAL: its row weights are (4, 4, 4, 4, 5, 5, 5, 5) and it equals no censused candidate, and neither does UY'. So the isometric monomial commutant is {I, U} and the isometric commutant proper contains at least {I, U, Y', UY'}, two of whose elements lie outside the sweep BY CONSTRUCTION. THIS IS AN EXTENSION OF BLOCK 190 AND NOT A CORRECTION TO IT: every number in that census is reproduced here, and what changes is only that the ADDITIONAL exact isospectrality Block 190 recorded as NOT GROUP-FORCED is now exhibited as forced by a NON-MONOMIAL involutive isometry.\\nper_scope: THE MECHANISM IS OF THE CLASS AND NOT OF THE FIXTURE, THE PERSISTENCE IS NOT VACUOUS, AND WHAT REMAINS OPEN IS NAMED. At T = 20 the Sylvester dimension, BOTH projective branches with both lam values, the triangular entries and the completion Y' with all three identities are IDENTICAL to T = 16 at both points. That agreement is not an identity, because the data it is computed from MOVES: W, V, W_0, W_2, V_0 and V_2 are width-invariant at residual 0, while EACH of K_0 and K_2 changes in ALL FOUR entries and the core Gram K_c changes in ALL 64 -- so the branches are re-derived against changed Grams and return the same rays. At the second rational point (1/2, 1/3), whose imported unit-volume block is diag(1, [[9/8, -3/8], [-3/8, 9/8]], 1), every structural statement above holds on a carrier that is measurably different: nnz(Q(9/20,5/13) - Q(1/2,1/3)) = 512 of 512 nonzero entries at T = 16. WHAT REMAINS OPEN IS NAMED AND NOT PAPERED OVER: WHY the carrier admits such an isometry is NOT derived, and the operator is exhibited rather than explained; whether the isometric commutant is EXACTLY the Klein four-group is NOT decided, because no exhaustive sweep of the non-monomial isometric commutant is performed; ONE core t0 = 3 is probed and nothing is claimed at any other core; two widths are not a width family theorem and two rational points are not a parameter space; and no Osterwalder-Schrader reconstruction, no transfer interpretation and no physical reading of Y' is supplied by any line of this block.\\nRESULT: ON BLOCK 190's WIDTH FAMILY AT T = 16 AND T = 20, AT THE DEEP CORE t0 = 3 AND AT BOTH RATIONAL POINTS, THE p = 0 / p = 2 ISOSPECTRALITY OF THE UNIT-CELL MONODROMY IS IMPLEMENTED BY AN EXACT INVOLUTIVE K_c-ISOMETRY IN THE FULL COMMUTANT OF W: THE SYLVESTER SPACE HAS DIMENSION 2, THE GRAM-CONFORMALITY CONDITION LEAVES EXACTLY TWO PROJECTIVE RAYS DECIDED BY ONE PRIMITIVE QUADRATIC, THE lam = 1 RAY CARRIES AN INTERTWINER X* THAT SIMULTANEOUSLY IDENTIFIES (K_0, K_2), AND Y' = B_2 X* pi_0 + B_0 X*^-1 pi_2 + Ph SATISFIES [W, Y'] = 0, Y'^T K_c Y' = K_c AND Y'^2 = I_8 ENTRYWISE OVER QQ. Block 190's recorded leftover -- that the p = 0 / p = 2 equality is NOT GROUP-FORCED by any signed monomial -- is thereby EXPLAINED AND NOT CONTRADICTED: the forcing operator exists and is non-monomial, so the 2048-candidate sweep was exhaustive over the wrong class. THE SCOPE IS MONODROMY-LEVEL AND THE TRIANGULAR DISPLAY IS A GAUGE, AND BOTH ARE SAID BEFORE THE RESULT IS. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-196 STAND EXACTLY AS LANDED. BLOCK 190 IS NOT CORRECTED: its carrier, its core frame, its unit-cell monodromy, its shift algebra, its 64-entry S-Gram defect with its exact witness, its refuted spatial reflection and its 2048-candidate commutant census are all rebuilt here and reproduced, and its own declared leftover is what this block resolves. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE core, TWO widths, TWO rational points and ONE profile at unit volume -- not a scan, not a limit and not a width family theorem; the operator is EXHIBITED and its existence is NOT derived from the carrier; the isometric commutant is shown to CONTAIN a Klein four-group and is NOT shown to equal one; and the triangular display is a basis gauge whose entries carry no invariant meaning beyond r^2 = det K_0 / det K_2. THREE ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the FULL COMPLETION Y', which the solve had recorded as a named OPEN refinement; the DIAGNOSIS of the naive extension's 64-entry Gram defect as the zeroed heavy sector rather than a per-sector normalization mismatch; and the BASIS-DEPENDENCE of the triangular form together with the invariant statement that replaces it. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE p=0/p=2 ISOSPECTRALITY MECHANISM (block 197 candidate), ISO PHASE 1 MEASURED, ISO PHASE 2 MEASURED, ISO PHASE 3 MEASURED and B197 CHECK VERDICT anchors.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
