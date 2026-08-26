#!/usr/bin/env python3
"""BLOCK 198 -- THE SPATIAL EMBEDDING THEOREM AND THE MOMENTUM POSITIVITY
BOUNDARY: ON A SECOND CARRIER Z_16 x Z_8 THE ENTIRE Z_16 x Z_4 MONODROMY
SPECTRUM EMBEDS VERBATIM ON AN EXACT 8-DIMENSIONAL SECTOR, AND THE MONODROMY
POSITIVITY THAT HOLDS THERE FAILS ON THE NEW MOMENTUM SECTORS.

THE RESULT, AND ITS EXACT SCOPE.  Every transfer result of Blocks 190 to 197
lives on ONE spatial extent, X = 4.  This block builds the construction once
more at X = 8 -- the SAME staggered kernel, the SAME wrap-edge sign, the SAME
grade-raising, the SAME site reflection, the SAME quarter-weighted cell Hodge,
the SAME completion Q = m H + H D_s - D_s^T H -- and asks what happens to the
spectrum under spatial refinement.  The answer has two halves and the second
half is a REFUTATION of this lane's own scouting record.

  (i) THE CONSTRUCTION SURVIVES THE REFINEMENT INTACT.  On Z_16 x Z_8 at the
      control fixture (m, c) = (9/20, 5/13) and unit volume: nnz(d_K^2) = 0,
      nnz(Ps H Ps - H) = 0, nnz(Ps Q Ps - Q^T) = 0, rank(Q) = 128 with two-sided
      inverse residuals ZERO, the directed cross block is EMPTY at 0 entries,
      and the 16-cell deep core Gram K_c is exactly symmetric with ALL SIXTEEN
      leading principal minors strictly positive.

 (ii) THE EMBEDDING, AND IT IS A SECTOR STATEMENT AND NOT A COINCIDENCE OF
      COEFFICIENTS.  The half-lattice shift U_4 splits the 16-dimensional core
      into two 8-dimensional pieces by P_e = (I + U_4)/2 and P_o = (I - U_4)/2,
      and BOTH the Gram and the monodromy are block diagonal for that split --
      the cross blocks carry 0 entries.  On the EVEN sector the compressed
      monodromy W_e has

        charpoly(W_e)  =  charpoly(W_4)    EXACTLY, monic residual 0,

      where W_4 is the Z_16 x Z_4 monodromy REBUILT HERE from the same formulas
      at the same core, and W_e is SIMILAR TO W_4 OVER QQ -- same elementary
      divisor census, and an explicit nonsingular rational intertwiner is
      exhibited.  Its primitive factors are Block 190's and Block 194's landed
      pair, digit for digit,

        heavy  =  22569375 z^2 - 233631106 z + 22569375,
        light  =  39529825 z^2 - 109432706 z + 39529825,

      each squared.  On the ODD sector the compressed monodromy carries ONE new
      irreducible palindromic quartic, squared,

        q(z) =  1035991876210625 z^4 - 10651994137075200 z^3
              + 31207521664211586 z^2 - 10651994137075200 z
              + 1035991876210625.

(iii) THE COMMUTANTS.  All EIGHT spatial shifts commute with W exactly, and the
      Gram splits them: the four EVEN shifts are exact K_c-isometries at 0
      defect and the four ODD shifts are not, at 256 entries each.  In
      particular [W, U_2] = [W, U_4] = 0.

 (iv) THE MOMENTUM POSITIVITY BOUNDARY, AND IT REFUTES THE SCOUTING RECORD.
      Write q(z) = A z^4 + B z^3 + C z^2 + B z + A.  Then q(z) = z^2 q_u(u) with
      u = z + 1/z and q_u(u) = A u^2 + B u + (C - 2A), an EXACT polynomial
      identity.  The discriminant of q_u is

        B^2 - 4 A (C - 2 A) = -7271743246281426848714247040000  <  0,

      certified without a radical by the exact sum-of-squares identity
      4 A q_u(u) - (2 A u + B)^2 = 7271743246281426848714247040000.  So q_u has
      NO real root, hence q has NO real root and NO unimodular root, and all
      four new-sector eigenvalues are nonreal and OFF the unit circle.  On the
      embedded sector, by contrast, both quadratics have strictly positive
      discriminant, root product exactly 1, positive root sum and |b| > 2a, so
      all their roots are real, positive and reciprocal.  BOTH DIRECTIONS ARE
      GATED.  The scouting record's sentence -- that this was a strong pass with
      the new quartic positive -- IS FALSE AND IS CARRIED HERE AS CORRECTION 82.

WHICH POSITIVITY FAILS IS SAID EXPLICITLY, BECAUSE TWO DIFFERENT ONES ARE IN
PLAY.  The core Gram stays positive definite -- 16 of 16 minors on the whole
core and 8 of 8 on EACH sector.  What fails on the new sectors is the MONODROMY
SPECTRAL positivity, not the positivity of the reflected pairing.  The new
sectors are therefore a MEASURED BOUNDARY of a transfer property and NOT a
defect of the construction, and that distinction is gated in both directions.

ALL OF IT IS FINITE EXACT LINEAR ALGEBRA OVER QQ AT ONE CORE OF ONE WIDTH AT ONE
RATIONAL POINT ON TWO SPATIAL EXTENTS.  NONE OF IT SUPPLIES GRAVITY.  NONE OF IT
IS A THEOREM ABOUT A GENERIC (m, c), ABOUT ANOTHER CORE, ABOUT ANOTHER WIDTH,
ABOUT A THIRD EXTENT OR ABOUT A LIMIT.

  0. THE CONSTRUCTION AT X = 8 (C).  The grade complex, the reflection
     covariance of H and of Q, the empty cross block, the carrier rank with its
     two-sided inverse residuals, and the 16 x 16 core Gram with all sixteen
     leading principal minors strictly positive.

  1. THE EMBEDDING (D).  The U_4 sector split with its exact projector ranks and
     zero cross blocks; charpoly(W_e) - charpoly(W_4) = 0 against a REBUILT
     X = 4 carrier; the similarity of W_e to W_4 over QQ with an explicit
     nonsingular intertwiner; the two landed quadratics reproduced verbatim; and
     the new quartic displayed, irreducible and palindromic.

  2. THE COMMUTANTS (E).  All eight shifts commute; the even ones are exact
     isometries and the odd ones carry a 256-entry Gram defect.

  3. THE MOMENTUM BOUNDARY (F).  The u-substitution as a polynomial identity,
     the u-quadratic with its exact negative discriminant and its sum-of-squares
     certificate, zero real roots and zero unimodular roots on the new sector,
     the real positive reciprocal pairs on the embedded sector, and the two
     sector Grams both positive definite.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GRAVITY.  NO
UNSCOPED POSITIVITY -- IT IS SCOPED TO THE EMBEDDED SECTOR.  THE NEW-SECTOR
NONREALITY IS NOT A DEFECT.  THE LARGER-UNIT-CELL QUESTION IS NOT DECIDED.  NO
GENERIC (m, c) THEOREM.  NO CONTINUUM.  THE READINGS ARE READINGS.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 197 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: six imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, unscoped positivity, the new sector as a
     defect, a decided larger-unit-cell question, a generic-point theorem, the
     continuum limit and licensed readings ALL declared NOT CLAIMED as measured
     constants, and nine gravity structures enumerated as NOT SUPPLIED.
  C  THE CONSTRUCTION AT X = 8: the grade complex, both reflection covariances,
     the empty cross block, the carrier rank with its inverse residuals, and the
     16 x 16 core Gram's sixteen positive minors.
  D  THE EMBEDDING: the sector split, the zero cross blocks, the exact charpoly
     identity against a rebuilt X = 4 carrier, the QQ-similarity with its
     explicit nonsingular intertwiner, the two verbatim landed quadratics and
     the new quartic.
  E  THE COMMUTANTS: all eight shift commutators at zero, and the even/odd
     split of the Gram defect.
  F  THE MOMENTUM BOUNDARY: the u identity, the u-quadratic and its NEGATIVE
     discriminant with a sum-of-squares certificate, the new sector's zero real
     roots, its zero unimodular roots counted a SECOND time by the Cayley
     transform, the embedded sector's real positive reciprocal pairs, and both
     sector Grams positive definite.
  G  the note at its final path, the N5 fence byte-identical, and the nsimplify
     count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through G PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: thirty-five declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.  The per-family MUTATION census
  is A 2, B 8, C 6, D 7, E 4, F 6, G 2, run against thirty-six CHECKS whose
  per-family census is A 2, B 8, C 6, D 7, E 4, F 7, G 2.
  SIX OF THE THIRTY-FIVE GUARD CORRECTIONS RATHER THAN RESULTS:
  claim_positivity_unscoped asserts the monodromy positivity holds on the whole
  X = 8 core, which is the scouting record's refuted sentence;
  claim_new_sector_defect asserts the nonreal sector is an arithmetic defect of
  the construction rather than a measured boundary of a transfer property;
  claim_larger_cell_decided asserts this block decides whether an X = 8-native
  larger unit cell restores positivity; break_embedded_positivity asserts the
  OTHER direction, that positivity fails on the embedded sector too;
  break_unimodular asserts the new roots are complex UNIMODULAR, which is Block
  194's second failure mode and is NOT this one; and break_sector_similarity
  asserts the embedding is a coincidence of characteristic coefficients with no
  similarity behind it.

RUNNING
  python3 scripts/admissibility_dirac_kahler_spatial_embedding_momentum_boundary_2026_08_26.py
  python3 ... --list-mutations
  python3 ... --mutation claim_positivity_unscoped
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
# and at the one rational shear this block probes.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_EMBEDDING_MOMENTUM_BOUNDARY_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 197 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 196 tip.
BLOCK197_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HIDDEN_INVOLUTIVE_ISOMETRY_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
BLOCK197_RUNNER = (
    "scripts/admissibility_dirac_kahler_hidden_involutive_isometry_"
    "2026_08_26.py"
)
PARENT_ARTIFACTS = (BLOCK197_NOTE, BLOCK197_RUNNER)
# Refreshed by anchored sed at landing, exactly as the five pins are.
PARENT_ARTIFACT_BLOBS = (
    "f357fea912c4909f59daa3b979c54ee3172040d3",   # Block 197 note
    "cb8b5728366874cacc6a46dd38862335376f2736",   # Block 197 runner
)
# THE CONSTRUCTION AUTHORITY.  Block 190 supplies the carrier, the core frame,
# the unit-cell monodromy and the X = 4 heavy/light pair this block's embedding
# is measured against; Block 194 re-declares that same pair at the control and
# supplies the two failure MODES this block's new mode is separated from; Block
# 191 supplies the quarter-weighted cell-average assembly; Block 105 supplies
# the imported Hodge; Block 197 is the stack parent.
BLOCK190_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK190_RUNNER = (
    "scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_"
    "2026_08_25.py"
)
BLOCK194_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_"
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_EMBEDDING_MOMENTUM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HIDDEN_INVOLUTIVE_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_hidden_involutive_isometry_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
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
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block197-"
              "hidden-involutive-isometry-20260826")
PARENT_COMMIT = "de78bc55790ea4509af0cf9c4de1830e8284ac76"
# The Block 196 tip: a real ancestor of HEAD that predates Block 197 and
# therefore carries NEITHER Block 197 artifact.
STALE_PARENT_COMMIT = "a3d8d7b0673c57d949d0f1944feaa2fc90877ae1"
# A real but superseded authority head, carried from Block 196's own record.
STALE_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_positivity_unscoped",
    "claim_new_sector_defect",
    "claim_larger_cell_decided",
    "claim_generic_point_theorem",
    "claim_continuum_limit",
    "claim_readings_licensed",
    "break_grade_complex",
    "break_hodge_reflection",
    "break_carrier_covariance",
    "break_empty_cross",
    "break_carrier_rank",
    "break_core_gram_definiteness",
    "break_sector_split",
    "break_sector_cross_blocks",
    "break_embedded_charpoly",
    "break_sector_similarity",
    "break_heavy_verbatim",
    "break_light_verbatim",
    "break_new_quartic",
    "break_shift_census",
    "break_u2_commutant",
    "break_u4_commutant",
    "break_odd_shift_isometry",
    "break_u_substitution",
    "break_u_quadratic",
    "break_u_discriminant_sign",
    "break_sos_certificate",
    "break_unimodular",
    "break_embedded_positivity",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_positivity_unscoped": "B",
    "claim_new_sector_defect": "B",
    "claim_larger_cell_decided": "B",
    "claim_generic_point_theorem": "B",
    "claim_continuum_limit": "B",
    "claim_readings_licensed": "B",
    "break_grade_complex": "C",
    "break_hodge_reflection": "C",
    "break_carrier_covariance": "C",
    "break_empty_cross": "C",
    "break_carrier_rank": "C",
    "break_core_gram_definiteness": "C",
    "break_sector_split": "D",
    "break_sector_cross_blocks": "D",
    "break_embedded_charpoly": "D",
    "break_sector_similarity": "D",
    "break_heavy_verbatim": "D",
    "break_light_verbatim": "D",
    "break_new_quartic": "D",
    "break_shift_census": "E",
    "break_u2_commutant": "E",
    "break_u4_commutant": "E",
    "break_odd_shift_isometry": "E",
    "break_u_substitution": "F",
    "break_u_quadratic": "F",
    "break_u_discriminant_sign": "F",
    "break_sos_certificate": "F",
    "break_unimodular": "F",
    "break_embedded_positivity": "F",
    "drop_n5_fence": "G",
    "break_nsimplify_absence": "G",
}
MUTATED_FAMILIES = "ABCDEFG"


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
    "BLOCK 190's WRAP-EDGE CONSTRUCTION AT T = 16, CARRIED UNCHANGED EXCEPT THAT THE SPATIAL EXTENT IS A PARAMETER: the staggered Dirac-Kahler carrier on Z_T x Z_X with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H",
    "THE SECOND SPATIAL EXTENT X = 8, WHICH IS THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT AND IS ONE CARRIER AND NOT A FAMILY: Z_16 x Z_8 at the SINGLE control fixture (m, c) = (9/20, 5/13) at unit volume, built beside the landed Z_16 x Z_4 carrier at the SAME width, the SAME fixture, the SAME volume and the SAME deep core t0 = 3",
    "BLOCK 190's CORE FRAME AT THE DEEP CORE t0 = 3, CARRIED UNCHANGED AND WIDENED WITH THE EXTENT: the 2X cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, and the UNIT-CELL MONODROMY W = K_c^-1 L_2",
    "THE HALF-LATTICE MOMENTUM SPLIT, WHICH IS THE OBJECT THE EMBEDDING IS STATED ON: the spatial shifts U_j by j sites on both time layers of the core, and the two real projectors P_e = (I + U_{X/2})/2 and P_o = (I - U_{X/2})/2 -- exact rational idempotents of equal rank X summing to I_{2X} -- together with the column-space bases B_e, B_o and their exact coordinate left inverses pi = (B^T B)^-1 B^T",
    "BLOCK 190's AND BLOCK 194's LANDED HEAVY/LIGHT PAIR AT THE CONTROL, IMPOSED AS THE COMPARISON TARGET AND ALSO REBUILT HERE RATHER THAN ONLY CITED: 22569375 z^2 - 233631106 z + 22569375 and 39529825 z^2 - 109432706 z + 39529825, whose squares are the whole X = 4 deep-core charpoly",
    "THE LANDED BLOCK 105 shear_hodge(c, v) READ THROUGH THE BLOCK 128 MODULE AT UNIT VOLUME AND AT THE ONE RATIONAL SHEAR 5/13 -- THE ONLY OBJECT IMPORTED -- assembled into H by Block 191's quarter-weighted four-corner cell average at Block 190's seam convention",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SEVEN ARE FALSE
# AND STAY FALSE.  THE SECOND AND THIRD ARE THE TWO THIS BLOCK'S RESULT MOST
# INVITES A READER TO ASSUME, AND THE SECOND IS THE SCOUTING RECORD'S OWN
# REFUTED SENTENCE.
GRAVITY_SUPPLIED_CLAIMED = False
POSITIVITY_UNSCOPED_CLAIMED = False
NEW_SECTOR_IS_DEFECT_CLAIMED = False
LARGER_CELL_DECIDED_CLAIMED = False
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
    "R1: that the X = 4 physics SURVIVES spatial refinement.  Measured: at ONE width, ONE fixture and ONE core, the compressed monodromy on the U_4-even sector has charpoly EQUAL to the rebuilt X = 4 monodromy's and is SIMILAR to it over QQ.  Nothing is measured at a third extent and no refinement limit is taken.  Reading.",
    "R2: that the new momentum sectors are UNPHYSICAL, or that their nonreal spectrum is an error.  Measured: their monodromy eigenvalues are nonreal and off the unit circle, AND the core Gram restricted to them is positive definite with 8 of 8 positive minors.  Which of the two facts is the physical one is NOT decided here.  Reading.",
    "R3: that these numbers are a DISPERSION RELATION and that 'heavy' and 'light' are masses.  Measured: roots of exact rational polynomials.  On the embedded sector the trace T = z + 1/z is real and exceeds 2 so acosh(T/2) exists; on the new sectors T is NONREAL and no acosh exists.  No physical energy and no mass is supplied by any line here.  Reading.",
    "R4: that an X = 8-native LARGER UNIT CELL would restore positivity on the new sectors.  Measured: NOTHING.  No larger-cell construction is built, probed or excluded in this block.  It is a NAMED OPEN LEG and it is named rather than answered.  Reading.",
    "R5: that the momentum boundary is a property of the construction CLASS rather than of this fixture.  Measured: ONE width, ONE rational point, ONE core, ONE unit volume and TWO spatial extents.  Reading.",
)
CHECK_VERDICT = "SPATIAL-EMBEDDING-CONFIRMED-NEW-QUARTIC-POSITIVITY-REFUTED"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
WIDTH = 16
EXTENTS = (4, 8)
NEW_EXTENT = 8
LANDED_EXTENT = 4
DEEP_CORE = 3
UNIT_VOLUME = sp.Integer(1)
FIXTURE = ("9/20", "5/13")

# --- C: THE CONSTRUCTION AT X = 8 -------------------------------------------
CARRIER_RANKS = {4: 64, 8: 128}
CORE_DIMENSIONS = {4: 8, 8: 16}
GRADE_COMPLEX_RESIDUAL = 0
HODGE_REFLECTION_RESIDUAL = 0
CARRIER_COVARIANCE_RESIDUAL = 0
# THE DIRECTED CROSS BLOCK, EMPTY: Q has no entry from the strict past half
# {1..T/2-1} to the strict future half {T/2+1..T-1}.
CROSS_BLOCK_NNZ = 0
GRAM_SYMMETRIC_RESIDUAL = 0
# ALL SIXTEEN leading principal minors of the 16 x 16 core Gram are POSITIVE.
CORE_MINOR_SIGNS = {4: (1,) * 8, 8: (1,) * 16}
# The imported unit-volume shear block at c = 5/13, declared so the carrier is
# bound to the import rather than to a rerun.
HODGE_BLOCK = (
    (1, 0, 0, 0),
    (0, sp.Rational(169, 144), sp.Rational(-65, 144), 0),
    (0, sp.Rational(-65, 144), sp.Rational(169, 144), 0),
    (0, 0, 0, 1),
)

# --- D: THE EMBEDDING --------------------------------------------------------
# The half-lattice shift U_4 splits the 16-cell core into two 8-dimensional
# pieces, and BOTH K_c and W are block diagonal for that split.
SECTOR_PROJECTOR_RANKS = (8, 8)
SECTOR_IDEMPOTENT_RESIDUALS = (0, 0)
SECTOR_PARTITION_RESIDUAL = 0
SECTOR_CROSS_GRAM_NNZ = 0
SECTOR_CROSS_MONODROMY_NNZ = (0, 0)
# THE EMBEDDING ITSELF: the compressed even-sector monodromy has EXACTLY the
# characteristic polynomial of the REBUILT X = 4 monodromy, as a monic identity
# over QQ[z] and not as a coefficient coincidence.
EMBEDDED_CHARPOLY_RESIDUAL = 0
# ... and the two are SIMILAR OVER QQ: same charpoly AND same elementary divisor
# census dim ker p(M)^k, with an explicit nonsingular rational intertwiner.
ELEMENTARY_DIVISOR_CENSUS = {
    (22569375, 1): 4, (22569375, 2): 4, (22569375, 3): 4,
    (39529825, 1): 4, (39529825, 2): 4, (39529825, 3): 4,
}
SYLVESTER_DIMENSION = 16
INTERTWINER_RANK = 8
INTERTWINER_RESIDUAL = 0
SECTORS_SIMILAR = True
# Block 190's and Block 194's landed pair at the control, as primitive integer
# coefficient tuples.  These are the numbers the embedding must reproduce
# VERBATIM, and they are also rebuilt here from the X = 4 carrier.
HEAVY_POLYNOMIAL = (22569375, -233631106, 22569375)
LIGHT_POLYNOMIAL = (39529825, -109432706, 39529825)
EMBEDDED_FACTORS = ((HEAVY_POLYNOMIAL, 2), (LIGHT_POLYNOMIAL, 2))
# THE ONE NEW IRREDUCIBLE FACTOR, PALINDROMIC, OF MULTIPLICITY TWO.
NEW_QUARTIC = (1035991876210625, -10651994137075200, 31207521664211586,
               -10651994137075200, 1035991876210625)
NEW_QUARTIC_MULTIPLICITY = 2
NEW_QUARTIC_IRREDUCIBLE = True
NEW_QUARTIC_PALINDROMIC = True
# charpoly(W) at X = 8 is the product of the two sector charpolys, exactly.
FULL_CHARPOLY_FACTORS = ((HEAVY_POLYNOMIAL, 2), (LIGHT_POLYNOMIAL, 2),
                         (NEW_QUARTIC, 2))
FULL_CHARPOLY_CONTENT = sp.Rational(
    1, 854282575605737410298720470187055375971422309970855712890625)
# Block 194's OWN declared monic-normalization scalar at the control, which the
# rebuilt X = 4 carrier must return: the squared product of the two leading
# coefficients, 22569375^2 * 39529825^2.
LANDED_CHARPOLY_CONTENT = sp.Rational(
    1, 795955611005101889386962890625)
SECTOR_PRODUCT_RESIDUAL = 0

# --- E: THE COMMUTANTS -------------------------------------------------------
# ALL EIGHT spatial shifts commute with the monodromy, and the Gram splits them
# by parity: the even ones are exact isometries, the odd ones are not.
SHIFT_COMMUTATORS = (0,) * 8
SHIFT_GRAM_DEFECTS = (0, 256, 0, 256, 0, 256, 0, 256)
EVEN_SHIFTS_ISOMETRIC = True
ODD_SHIFT_GRAM_DEFECT = 256
SHIFT_ORDER_RESIDUAL = 0

# --- F: THE MOMENTUM BOUNDARY ------------------------------------------------
# q(z) = A z^4 + B z^3 + C z^2 + B z + A  =  z^2 (A u^2 + B u + (C - 2A)),
# u = z + 1/z, AS A POLYNOMIAL IDENTITY and not as a substitution rule.
U_SUBSTITUTION_RESIDUAL = 0
RECIPROCAL_IDENTITY_RESIDUAL = 0
U_QUADRATIC = (1035991876210625, -10651994137075200, 29135537911790336)
U_DISCRIMINANT = sp.Integer(-7271743246281426848714247040000)
U_DISCRIMINANT_SIGN = -1
# THE SUM-OF-SQUARES CERTIFICATE, and it is why no radical is ever evaluated:
# 4 A q_u(u) - (2 A u + B)^2 = -disc, a POSITIVE integer, so 4A q_u is a sum of
# a square and a positive constant and q_u is strictly positive on all of RR.
SOS_CONSTANT = sp.Integer(7271743246281426848714247040000)
SOS_RESIDUAL = 0
U_VERTEX = sp.Rational(213039882741504, 41439675048425)
U_MINIMUM = sp.Rational(2908697298512570739485698816, 1657587001937)
U_AT_PLUS_TWO = sp.Integer(11975517142482436)
U_AT_MINUS_TWO = sp.Integer(54583493690783236)
# THE TWO CONSEQUENCES, COUNTED EXACTLY AND NOT INFERRED: a real root z of q
# needs a real root u of q_u, and a UNIMODULAR root z of q needs a real root u
# of q_u in [-2, 2].  There are none of either.
U_REAL_ROOTS = 0
U_REAL_ROOTS_IN_BAND = 0
NEW_SECTOR_REAL_ROOTS = 0
NEW_SECTOR_DISTINCT_NONREAL = 4
# THE UNIMODULAR COUNT AGAIN, BY AN INDEPENDENT ROUTE THAT DOES NOT PASS THROUGH
# u AT ALL.  The Cayley transform z = (1 + i w)/(1 - i w) carries the real
# w-axis ONTO the unit circle minus {-1}, so (1 - i w)^4 q((1 + i w)/(1 - i w))
# is a REAL polynomial in w whose real roots are exactly the unimodular roots of
# q other than z = -1, and z = -1 and z = +1 are excluded separately by its
# constant and leading coefficients, which are exactly q(-1) and q(1).
CAYLEY_TRANSFORM = (54583493690783236, 0, 49983140813895672, 0,
                    11975517142482436)
CAYLEY_IMAGINARY_PART_ZERO = True
CAYLEY_REAL_ROOTS = 0
NEW_SECTOR_UNIMODULAR_ROOTS = 0
Q_AT_PLUS_ONE = sp.Integer(11975517142482436)
Q_AT_MINUS_ONE = sp.Integer(54583493690783236)
# THE OTHER DIRECTION: on the embedded sector every root is real, positive and
# reciprocal, by discriminant, product, sum and the |b| > 2a test.
HEAVY_DISCRIMINANT = sp.Integer(52545986939220736)
LIGHT_DISCRIMINANT = sp.Integer(5725088884359936)
EMBEDDED_DISCRIMINANT_SIGNS = (1, 1)
EMBEDDED_ROOT_PRODUCTS = (1, 1)
EMBEDDED_ROOT_SUMS = (sp.Rational(233631106, 22569375),
                      sp.Rational(109432706, 39529825))
EMBEDDED_DISTINCT_REAL_ROOTS = 4
EMBEDDED_DISTINCT_POSITIVE_ROOTS = 4
EMBEDDED_DISTINCT_NEGATIVE_ROOTS = 0
EMBEDDED_POSITIVITY = True
NEW_SECTOR_POSITIVITY = False
# AND THE POSITIVITY THAT DOES NOT FAIL, WHICH IS WHY THE BOUNDARY IS NOT A
# DEFECT: the core Gram is positive definite on the whole core AND on EACH
# sector separately.
SECTOR_GRAM_MINOR_SIGNS = ((1,) * 8, (1,) * 8)
SECTOR_GRAM_SYMMETRIC_RESIDUALS = (0, 0)

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  This block's content is a set of EXACT ZERO statements --
# nnz(d_K^2) = 0, nnz(Ps Q Ps - Q^T) = 0, the empty cross block, the zero sector
# cross blocks, charpoly(W_e) - charpoly(W_4) = 0 -- together with a set of
# EXACT SIGN statements whose whole content is a discriminant that is NEGATIVE
# by 7271743246281426848714247040000 against coefficients above 10^30.  A single
# such call could turn the odd shifts' real 256-entry Gram defect into a
# spurious zero, or a sign into its opposite.  Every mass, shear and volume here
# is ALREADY an exact sympy Rational.  Gate G counts the occurrences in this
# file's own source and requires ZERO.
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


def exact_determinant(matrix: sp.MatrixBase) -> sp.Expr:
    return rational_matrix(matrix).det()


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


def minor_signs(matrix: sp.MatrixBase) -> tuple:
    """THE SYLVESTER CRITERION, EXACTLY: the signs of the leading principal
    minors of a symmetric rational matrix.  All +1 is positive definiteness and
    no eigenvalue is ever computed."""
    return tuple(int(sp.sign(exact_determinant(matrix[:k, :k])))
                 for k in range(1, matrix.rows + 1))


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


def evaluate_polynomial(coefficients: tuple, matrix: sp.MatrixBase
                        ) -> sp.Matrix:
    """p(M) for an integer coefficient tuple, exactly and by Horner."""
    result = sp.zeros(matrix.rows, matrix.cols)
    for coefficient in coefficients:
        result = sp.expand(result * matrix + sp.Integer(coefficient)
                           * sp.eye(matrix.rows))
    return result


Z = sp.Symbol("z")
U = sp.Symbol("u")
W_SYMBOL = sp.Symbol("w", real=True)


# ---------------------------------------------------------------------------
# THE CARRIER AT AN ARBITRARY SPATIAL EXTENT.  Everything except the shear block
# is rebuilt here; the shear block is the ONE import.
# ---------------------------------------------------------------------------
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])


def site_index(extent: int, time: int, space: int) -> int:
    return (time % WIDTH) * extent + space % extent


def site_theta(time: int) -> int:
    """theta_s(t) = -t, fixing the slices {0, T/2}."""
    return (-time) % WIDTH


def staggered_kernel(extent: int) -> sp.Matrix:
    """eta_t = 1, eta_x = (-1)^t, and the temporal sign w = -1 ON THE WRAP EDGE
    t = T-1 -- Block 190's convention at a general spatial extent."""
    size = WIDTH * extent
    kernel = sp.zeros(size, size)
    for time in range(WIDTH):
        for space in range(extent):
            temporal_sign = -1 if time == WIDTH - 1 else 1
            here = site_index(extent, time, space)
            ahead = site_index(extent, time + 1, space)
            kernel[here, ahead] += sp.Rational(temporal_sign, 2)
            kernel[ahead, here] -= sp.Rational(temporal_sign, 2)
            spatial_sign = (-1) ** time
            right = site_index(extent, time, space + 1)
            kernel[here, right] += sp.Rational(spatial_sign, 2)
            kernel[right, here] -= sp.Rational(spatial_sign, 2)
    return kernel


def grade_projector(extent: int, grade: int) -> sp.Matrix:
    return sp.diag(*[1 if (time % 2 + space % 2) == grade else 0
                     for time in range(WIDTH) for space in range(extent)])


def raising_part(extent: int, kernel: sp.Matrix) -> sp.Matrix:
    """d_K = P1 K P0 + P2 K P1."""
    p0, p1, p2 = (grade_projector(extent, g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def reflection_permutation(extent: int) -> sp.Matrix:
    size = WIDTH * extent
    matrix = sp.zeros(size, size)
    for time in range(WIDTH):
        for space in range(extent):
            matrix[site_index(extent, site_theta(time), space),
                   site_index(extent, time, space)] = 1
    return matrix


def site_restricted_raising(extent: int, raising: sp.Matrix) -> sp.Matrix:
    """A_s: the d_K entries inside the CLOSED half {0..T/2}, with the two fixed
    slices' own spatial edges removed."""
    size = WIDTH * extent
    half = WIDTH // 2
    closed, fixed = set(range(half + 1)), {0, half}
    matrix = sp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            if raising[row, column] == 0:
                continue
            row_time = row // extent
            column_time = column // extent
            if row_time not in closed or column_time not in closed:
                continue
            if row_time == column_time and row_time in fixed:
                continue
            matrix[row, column] = raising[row, column]
    return matrix


def cell_embedding(extent: int, time: int, space: int) -> sp.Matrix:
    matrix = sp.zeros(WIDTH * extent, 4)
    for column, (delta_t, delta_x) in enumerate(
            ((0, 0), (0, 1), (1, 0), (1, 1))):
        matrix[site_index(extent, time + delta_t, space + delta_x), column] = 1
    return matrix


def imported_shear_block(shear: sp.Rational, volume: object) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT: the LANDED Block 105 shear Hodge
    diag(v, v g(c)^-1, 1/v) with g(c) = [[1, c], [c, 1]].  NO nsimplify: the
    shear is an exact sympy Rational and the volume is a Rational."""
    return sp.expand(sp.Matrix(b128.block105.shear_hodge(shear, volume)))


def site_hodge(extent: int, shear: sp.Rational) -> sp.Matrix:
    """THE QUARTER-WEIGHTED FOUR-CORNER CELL AVERAGE, Block 191's assembly rule
    at Block 190's seam convention and at unit volume."""
    half = WIDTH // 2
    block = imported_shear_block(shear, UNIT_VOLUME)
    reflected = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    result = sp.zeros(WIDTH * extent, WIDTH * extent)
    for time in range(WIDTH):
        chosen = block if time < half else reflected
        for space in range(extent):
            embedding = cell_embedding(extent, time, space)
            result += embedding * chosen * embedding.T / 4
    return sp.expand(result)


def completion(mass: sp.Rational, hodge: sp.Matrix,
               glue: sp.Matrix) -> sp.Matrix:
    """Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    return sp.expand(mass * hodge + hodge * glue - glue.T * hodge)


def directed_cross_block(extent: int, action: sp.Matrix) -> int:
    """THE DIRECTED CROSS BLOCK: entries of Q from the STRICT past half
    {1..T/2-1} to the STRICT future half {T/2+1..T-1}.  Zero is the statement
    that the glue never connects the two open halves directly."""
    half = WIDTH // 2
    size = WIDTH * extent
    return sum(1 for row in range(size) for column in range(size)
               if action[row, column] != 0
               and 1 <= row // extent <= half - 1
               and half + 1 <= column // extent <= WIDTH - 1)


# ---------------------------------------------------------------------------
# THE HEAVY WORK, DONE ONCE PER EXTENT AND SHARED.  The exact 128 x 128 inverse
# is the only expensive step in this runner and NOTHING recomputes it: ONE
# 128 x 128 inverse and ONE 64 x 64 inverse serve every gate below.
# ---------------------------------------------------------------------------
_CARRIER_CACHE: dict = {}


def carrier(extent: int) -> dict:
    if extent in _CARRIER_CACHE:
        return _CARRIER_CACHE[extent]
    mass, shear = rat(FIXTURE[0]), rat(FIXTURE[1])
    size = WIDTH * extent
    kernel = staggered_kernel(extent)
    raising = raising_part(extent, kernel)
    reflection = reflection_permutation(extent)
    restricted = site_restricted_raising(extent, raising)
    glue = sp.expand(restricted - reflection * restricted * reflection)
    hodge = site_hodge(extent, shear)
    action = completion(mass, hodge, glue)
    domain = rational_matrix(action)
    rank = domain.rank()
    started_ns = time.monotonic_ns()
    inverse = domain.inv().to_Matrix() if rank == size else None
    record = {
        "extent": extent,
        "size": size,
        "grade_complex": residual_count(raising * raising),
        "hodge_reflection": residual_count(
            reflection * hodge * reflection - hodge),
        "covariance": residual_count(
            reflection * action * reflection - action.T),
        "cross": directed_cross_block(extent, action),
        "rank": rank,
        "action": action,
        "inverse": inverse,
        "inverse_seconds": (time.monotonic_ns() - started_ns) / 1000000000,
    }
    record["inverse_residuals"] = (
        (residual_count(action * inverse - sp.eye(size)),
         residual_count(inverse * action - sp.eye(size)))
        if inverse is not None else (-1, -1))       # pragma: no cover
    _CARRIER_CACHE[extent] = record
    return record


# ---------------------------------------------------------------------------
# THE CORE FRAME AND THE HALF-LATTICE MOMENTUM SPLIT, ALL OF THEM FORMULAS
# ---------------------------------------------------------------------------
def core_cells(extent: int) -> tuple:
    return tuple((time, space) for time in (DEEP_CORE, DEEP_CORE + 1)
                 for space in range(extent))


def shifted_pairing(extent: int, inverse: sp.Matrix, step: int) -> sp.Matrix:
    """L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)]; k = 0 is K_c."""
    cells = core_cells(extent)
    size = len(cells)
    matrix = sp.zeros(size, size)
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(extent, site_theta(row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(extent, column_time + step, column_space), partner]
    return matrix


def spatial_shift(extent: int, step: int) -> sp.Matrix:
    """U_j: the j-site spatial shift permutation of the 2X core cells, acting on
    BOTH time layers."""
    cells = core_cells(extent)
    position = {cell: index for index, cell in enumerate(cells)}
    matrix = sp.zeros(len(cells), len(cells))
    for cell in cells:
        image = (cell[0], (cell[1] + step) % extent)
        matrix[position[image], position[cell]] = 1
    return matrix


def column_basis(projector: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.hstack(*projector.columnspace())


def coordinate_left_inverse(basis: sp.Matrix) -> sp.Matrix:
    """pi = (B^T B)^-1 B^T, exact over QQ."""
    return exact_inverse(basis.T * basis) * basis.T


def compressed(basis: sp.Matrix, operator: sp.Matrix) -> sp.Matrix:
    return sp.expand(coordinate_left_inverse(basis) * operator * basis)


def factor_census(matrix: sp.MatrixBase) -> tuple:
    """The primitive integer factors of charpoly(M) with their multiplicities,
    sorted by degree then by leading coefficient -- PROJECTIVE data, so the
    monic normalization SymPy applies cannot move it."""
    factors = sp.factor_list(sp.expand(matrix.charpoly(Z).as_expr()))[1]
    census = []
    for factor, multiplicity in factors:
        polynomial = sp.Poly(factor, Z)
        if polynomial.degree() == 0:                   # pragma: no cover
            continue
        census.append((primitive_tuple(factor, Z), int(multiplicity)))
    return tuple(sorted(census, key=lambda item: (len(item[0]), item[0])))


def elementary_divisor_census(matrix: sp.MatrixBase,
                              factors: tuple) -> dict:
    """THE CANONICAL SIMILARITY INVARIANT: dim ker p(M)^k for each irreducible
    rational factor p of charpoly(M) and each k.  Two matrices over QQ with the
    same characteristic polynomial are SIMILAR iff these dimensions agree for
    every (p, k) -- this is the Frobenius normal form read off without
    computing it."""
    census = {}
    for coefficients in factors:
        value = evaluate_polynomial(coefficients, matrix)
        power = sp.eye(matrix.rows)
        for exponent in (1, 2, 3):
            power = sp.expand(power * value)
            census[(coefficients[0], exponent)] = (
                matrix.rows - exact_rank(power))
    return census


def intertwiner_space(left: sp.Matrix, right: sp.Matrix) -> list:
    """AN EXACT LINEAR NULLSPACE, NOT A SEARCH: the entries of X are the
    unknowns of X L - R X = 0 and the solution space is the nullspace of its
    coefficient matrix over QQ."""
    size = left.rows
    names = sp.symbols(f"x0:{size * size}")
    unknown = sp.Matrix(size, size, list(names))
    equations = list(sp.expand(unknown * left - right * unknown))
    coefficients, right_hand = sp.linear_eq_to_matrix(equations, names)
    assert all(value == 0 for value in right_hand)
    return [sp.Matrix(size, size, list(vector))
            for vector in coefficients.nullspace()]


def nonsingular_intertwiner(basis: list) -> tuple:
    """A NONSINGULAR MEMBER, FOUND DETERMINISTICALLY AND NOT RANDOMLY: the
    singular members of an intertwiner space are a proper algebraic subset, so
    a fixed deterministic sweep of integer combinations reaches an invertible
    one.  The trial index is REPORTED, so the search is reproducible."""
    size = basis[0].rows
    for trial in range(1, 64):
        combination = sp.zeros(size, size)
        for index, member in enumerate(basis):
            combination += sp.Integer(pow(trial, index, 97) + 1) * member
        if exact_rank(combination) == size:
            return trial, combination
    return -1, sp.zeros(size, size)                    # pragma: no cover


@dataclass(frozen=True)
class SectorFacts:
    projector_ranks: tuple
    idempotent_residuals: tuple
    partition_residual: int
    cross_gram: int
    cross_monodromy: tuple
    embedded_factors: tuple
    new_factors: tuple
    embedded_charpoly_residual: int
    sector_product_residual: int
    census_embedded: dict
    census_landed: dict
    similar: bool
    sylvester_dimension: int
    intertwiner_trial: int
    intertwiner_rank: int
    intertwiner_residual: int
    gram_minor_signs: tuple
    gram_symmetric_residuals: tuple


def measure_sectors(frame8: dict, frame4: dict) -> SectorFacts:
    """THE HALF-LATTICE SPLIT, AND EVERY LINE OF IT IS A FORMULA:
    P_e = (I + U_4)/2, P_o = (I - U_4)/2, B_p a column-space basis of P_p,
    pi_p = (B_p^T B_p)^-1 B_p^T, W_p = pi_p W B_p, K_p = B_p^T K_c B_p."""
    monodromy, gram = frame8["monodromy"], frame8["gram"]
    size = monodromy.rows
    half_shift = spatial_shift(NEW_EXTENT, NEW_EXTENT // 2)
    even = sp.expand((sp.eye(size) + half_shift) / 2)
    odd = sp.expand((sp.eye(size) - half_shift) / 2)
    basis_even, basis_odd = column_basis(even), column_basis(odd)
    embedded = compressed(basis_even, monodromy)
    fresh = compressed(basis_odd, monodromy)
    landed = frame4["monodromy"]
    gram_even = sp.expand(basis_even.T * gram * basis_even)
    gram_odd = sp.expand(basis_odd.T * gram * basis_odd)

    embedded_factors = factor_census(embedded)
    census_embedded = elementary_divisor_census(
        embedded, tuple(item[0] for item in embedded_factors))
    census_landed = elementary_divisor_census(
        landed, tuple(item[0] for item in embedded_factors))
    charpoly_residual = 0 if sp.expand(
        embedded.charpoly(Z).as_expr() - landed.charpoly(Z).as_expr()
    ) == 0 else 1
    basis = intertwiner_space(landed, embedded)
    trial, member = nonsingular_intertwiner(basis)
    return SectorFacts(
        projector_ranks=(exact_rank(even), exact_rank(odd)),
        idempotent_residuals=(residual_count(even * even - even),
                              residual_count(odd * odd - odd)),
        partition_residual=residual_count(even + odd - sp.eye(size)),
        cross_gram=residual_count(basis_even.T * gram * basis_odd),
        cross_monodromy=(
            residual_count(coordinate_left_inverse(basis_even)
                           * monodromy * basis_odd),
            residual_count(coordinate_left_inverse(basis_odd)
                           * monodromy * basis_even)),
        embedded_factors=embedded_factors,
        new_factors=factor_census(fresh),
        embedded_charpoly_residual=charpoly_residual,
        sector_product_residual=0 if sp.expand(
            monodromy.charpoly(Z).as_expr()
            - embedded.charpoly(Z).as_expr() * fresh.charpoly(Z).as_expr()
        ) == 0 else 1,
        census_embedded=census_embedded,
        census_landed=census_landed,
        similar=(census_embedded == census_landed and charpoly_residual == 0),
        sylvester_dimension=len(basis),
        intertwiner_trial=trial,
        intertwiner_rank=exact_rank(member),
        intertwiner_residual=residual_count(member * landed - embedded * member),
        gram_minor_signs=(minor_signs(gram_even), minor_signs(gram_odd)),
        gram_symmetric_residuals=(residual_count(gram_even - gram_even.T),
                                  residual_count(gram_odd - gram_odd.T)))


@dataclass(frozen=True)
class BoundaryFacts:
    quartic: tuple
    palindromic: bool
    irreducible: bool
    reciprocal_residual: int
    substitution_residual: int
    u_quadratic: tuple
    discriminant: sp.Expr
    discriminant_sign: int
    sos_constant: sp.Expr
    sos_residual: int
    vertex: sp.Expr
    minimum: sp.Expr
    at_plus_two: sp.Expr
    at_minus_two: sp.Expr
    u_real_roots: int
    u_real_roots_in_band: int
    new_real_roots: int
    new_distinct_nonreal: int
    cayley_transform: tuple
    cayley_imaginary_zero: bool
    cayley_real_roots: int
    new_unimodular_roots: int
    at_plus_one: sp.Expr
    at_minus_one: sp.Expr
    heavy_discriminant: sp.Expr
    light_discriminant: sp.Expr
    embedded_signs: tuple
    embedded_products: tuple
    embedded_sums: tuple
    embedded_real: int
    embedded_positive: int
    embedded_negative: int
    embedded_positivity: bool
    new_positivity: bool


def measure_boundary(sectors: SectorFacts) -> BoundaryFacts:
    """THE MOMENTUM BOUNDARY, AND THE WHOLE ARGUMENT IS TWO POLYNOMIAL
    IDENTITIES AND FOUR EXACT ROOT COUNTS.  For a real palindromic quartic
    q(z) = A z^4 + B z^3 + C z^2 + B z + A the substitution u = z + 1/z gives
    q(z) = z^2 q_u(u) with q_u(u) = A u^2 + B u + (C - 2A); a REAL root z of q
    forces a REAL root u of q_u, and a UNIMODULAR root z forces a real root u
    in [-2, 2].  Positivity of q_u on all of RR is certified WITHOUT A RADICAL
    by 4 A q_u(u) = (2 A u + B)^2 + (4 A (C - 2A) - B^2)."""
    quartic = sectors.new_factors[0][0]
    a, b, c = (sp.Integer(quartic[0]), sp.Integer(quartic[1]),
               sp.Integer(quartic[2]))
    q_expression = (a * Z ** 4 + b * Z ** 3 + c * Z ** 2 + b * Z + a)
    u_expression = a * U ** 2 + b * U + (c - 2 * a)
    discriminant = b ** 2 - 4 * a * (c - 2 * a)
    u_polynomial = sp.Poly(u_expression, U)
    q_polynomial = sp.Poly(q_expression, Z)

    # THE UNIMODULAR COUNT BY AN INDEPENDENT ROUTE.  The Cayley transform never
    # mentions u; its real roots are the unimodular roots of q other than -1.
    transform = sp.expand(sp.simplify(
        (1 - sp.I * W_SYMBOL) ** 4
        * q_expression.subs(Z, (1 + sp.I * W_SYMBOL) / (1 - sp.I * W_SYMBOL))))
    imaginary = sp.Poly(sp.expand(sp.im(transform)), W_SYMBOL)
    real_transform = sp.Poly(sp.expand(sp.re(transform)), W_SYMBOL)
    cayley_roots = real_transform.count_roots()

    heavy = sp.Poly(sum(sp.Integer(v) * Z ** (2 - i)
                        for i, v in enumerate(HEAVY_POLYNOMIAL)), Z)
    light = sp.Poly(sum(sp.Integer(v) * Z ** (2 - i)
                        for i, v in enumerate(LIGHT_POLYNOMIAL)), Z)
    heavy_discriminant = (sp.Integer(HEAVY_POLYNOMIAL[1]) ** 2
                          - 4 * sp.Integer(HEAVY_POLYNOMIAL[0])
                          * sp.Integer(HEAVY_POLYNOMIAL[2]))
    light_discriminant = (sp.Integer(LIGHT_POLYNOMIAL[1]) ** 2
                          - 4 * sp.Integer(LIGHT_POLYNOMIAL[0])
                          * sp.Integer(LIGHT_POLYNOMIAL[2]))
    embedded = heavy.mul(light)
    products = tuple(sp.Rational(item[2], item[0])
                     for item in (HEAVY_POLYNOMIAL, LIGHT_POLYNOMIAL))
    sums = tuple(sp.Rational(-item[1], item[0])
                 for item in (HEAVY_POLYNOMIAL, LIGHT_POLYNOMIAL))
    signs = (int(sp.sign(heavy_discriminant)), int(sp.sign(light_discriminant)))
    embedded_real = embedded.count_roots()
    embedded_positive = embedded.count_roots(0, sp.oo)
    return BoundaryFacts(
        quartic=quartic,
        palindromic=(quartic[0] == quartic[4] and quartic[1] == quartic[3]),
        irreducible=(len(sp.factor_list(q_expression)[1]) == 1
                     and sp.factor_list(q_expression)[1][0][1] == 1),
        reciprocal_residual=0 if sp.expand(
            sp.together(Z ** 4 * q_expression.subs(Z, 1 / Z))
            - q_expression) == 0 else 1,
        substitution_residual=0 if sp.expand(
            sp.together(q_expression
                        - Z ** 2 * u_expression.subs(U, Z + 1 / Z))) == 0
        else 1,
        u_quadratic=(int(a), int(b), int(c - 2 * a)),
        discriminant=discriminant,
        discriminant_sign=int(sp.sign(discriminant)),
        sos_constant=-discriminant,
        sos_residual=0 if sp.expand(
            4 * a * u_expression - (2 * a * U + b) ** 2 + discriminant) == 0
        else 1,
        vertex=sp.Rational(-b, 2 * a),
        minimum=sp.Rational(-discriminant, 4 * a),
        at_plus_two=u_polynomial.eval(2),
        at_minus_two=u_polynomial.eval(-2),
        u_real_roots=u_polynomial.count_roots(),
        u_real_roots_in_band=u_polynomial.count_roots(-2, 2),
        new_real_roots=q_polynomial.count_roots(),
        new_distinct_nonreal=q_polynomial.degree() - q_polynomial.count_roots(),
        cayley_transform=tuple(int(v) for v in real_transform.all_coeffs()),
        cayley_imaginary_zero=bool(imaginary.is_zero),
        cayley_real_roots=cayley_roots,
        new_unimodular_roots=(
            cayley_roots
            + (1 if q_polynomial.eval(-1) == 0 else 0)),
        at_plus_one=q_polynomial.eval(1),
        at_minus_one=q_polynomial.eval(-1),
        heavy_discriminant=heavy_discriminant,
        light_discriminant=light_discriminant,
        embedded_signs=signs,
        embedded_products=products,
        embedded_sums=sums,
        embedded_real=embedded_real,
        embedded_positive=embedded_positive,
        embedded_negative=embedded.count_roots(-sp.oo, 0),
        embedded_positivity=bool(
            embedded_real == embedded.degree()
            and embedded_positive == embedded.degree()
            and all(sign > 0 for sign in signs)
            and all(value == 1 for value in products)
            and all(value > 0 for value in sums)),
        new_positivity=bool(q_polynomial.count_roots(0, sp.oo) > 0))


@dataclass(frozen=True)
class FrameFacts:
    extent: int
    dimension: int
    gram_symmetric: int
    minor_signs: tuple
    factors: tuple
    charpoly_content: sp.Expr
    shift_commutators: tuple
    shift_gram_defects: tuple
    shift_order: int


def measure_frame(extent: int) -> dict:
    record = carrier(extent)
    gram = shifted_pairing(extent, record["inverse"], 0)
    second = shifted_pairing(extent, record["inverse"], 2)
    monodromy = sp.expand(exact_inverse(gram) * second)
    charpoly = sp.expand(monodromy.charpoly(Z).as_expr())
    factors = factor_census(monodromy)
    leading = sp.Integer(1)
    for coefficients, multiplicity in factors:
        leading *= sp.Integer(coefficients[0]) ** multiplicity
    commutators, defects = [], []
    for step in range(extent):
        shift = spatial_shift(extent, step)
        commutators.append(residual_count(monodromy * shift
                                          - shift * monodromy))
        defects.append(residual_count(shift.T * gram * shift - gram))
    unit = spatial_shift(extent, 1)
    order = residual_count(unit ** extent - sp.eye(2 * extent))
    return {
        "extent": extent, "gram": gram, "monodromy": monodromy,
        "facts": FrameFacts(
            extent=extent,
            dimension=monodromy.rows,
            gram_symmetric=residual_count(gram - gram.T),
            minor_signs=minor_signs(gram),
            factors=factors,
            charpoly_content=sp.Rational(1, 1) / leading,
            shift_commutators=tuple(commutators),
            shift_gram_defects=tuple(defects),
            shift_order=order),
    }


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
    carriers: dict
    frames: dict
    sectors: SectorFacts
    boundary: BoundaryFacts
    hodge_block: tuple
    big_inverses: int
    nsimplify_calls: int


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    authority = authority_certificate(main_head)
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""

    frames = {extent: measure_frame(extent) for extent in EXTENTS}
    carriers = {
        extent: {key: carrier(extent)[key] for key in
                 ("size", "grade_complex", "hodge_reflection", "covariance",
                  "cross", "rank", "inverse_residuals", "inverse_seconds")}
        for extent in EXTENTS}
    sectors = measure_sectors(frames[NEW_EXTENT], frames[LANDED_EXTENT])
    boundary = measure_boundary(sectors)
    block = imported_shear_block(rat(FIXTURE[1]), UNIT_VOLUME)
    block = tuple(tuple(sp.expand(block[row, column]) for column in range(4))
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
        carriers=carriers,
        frames={extent: frames[extent]["facts"] for extent in EXTENTS},
        sectors=sectors,
        boundary=boundary,
        hodge_block=block,
        big_inverses=sum(1 for extent in _CARRIER_CACHE
                         if WIDTH * extent == 128),
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
        "positivity_unscoped": POSITIVITY_UNSCOPED_CLAIMED,
        "new_sector_is_defect": NEW_SECTOR_IS_DEFECT_CLAIMED,
        "larger_cell_decided": LARGER_CELL_DECIDED_CLAIMED,
        "generic_point_theorem": GENERIC_POINT_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C -- the construction at X = 8.
        "carrier_ranks": dict(CARRIER_RANKS),
        "grade_complex": GRADE_COMPLEX_RESIDUAL,
        "hodge_reflection": HODGE_REFLECTION_RESIDUAL,
        "covariance": CARRIER_COVARIANCE_RESIDUAL,
        "cross": CROSS_BLOCK_NNZ,
        "gram_symmetric": GRAM_SYMMETRIC_RESIDUAL,
        "minor_signs": dict(CORE_MINOR_SIGNS),
        "hodge_block": HODGE_BLOCK,
        # D -- the embedding.
        "projector_ranks": SECTOR_PROJECTOR_RANKS,
        "idempotent_residuals": SECTOR_IDEMPOTENT_RESIDUALS,
        "partition_residual": SECTOR_PARTITION_RESIDUAL,
        "cross_gram": SECTOR_CROSS_GRAM_NNZ,
        "cross_monodromy": SECTOR_CROSS_MONODROMY_NNZ,
        "embedded_charpoly_residual": EMBEDDED_CHARPOLY_RESIDUAL,
        "census": dict(ELEMENTARY_DIVISOR_CENSUS),
        "similar": SECTORS_SIMILAR,
        "sylvester_dimension": SYLVESTER_DIMENSION,
        "intertwiner_rank": INTERTWINER_RANK,
        "intertwiner_residual": INTERTWINER_RESIDUAL,
        "heavy": HEAVY_POLYNOMIAL,
        "light": LIGHT_POLYNOMIAL,
        "embedded_factors": EMBEDDED_FACTORS,
        "new_quartic": NEW_QUARTIC,
        "new_multiplicity": NEW_QUARTIC_MULTIPLICITY,
        "new_irreducible": NEW_QUARTIC_IRREDUCIBLE,
        "new_palindromic": NEW_QUARTIC_PALINDROMIC,
        "full_factors": FULL_CHARPOLY_FACTORS,
        "full_content": FULL_CHARPOLY_CONTENT,
        "landed_content": LANDED_CHARPOLY_CONTENT,
        "sector_product_residual": SECTOR_PRODUCT_RESIDUAL,
        # E -- the commutants.
        "shift_commutators": SHIFT_COMMUTATORS,
        "shift_gram_defects": SHIFT_GRAM_DEFECTS,
        "even_isometric": EVEN_SHIFTS_ISOMETRIC,
        "odd_defect": ODD_SHIFT_GRAM_DEFECT,
        "shift_order": SHIFT_ORDER_RESIDUAL,
        # F -- the momentum boundary.
        "substitution_residual": U_SUBSTITUTION_RESIDUAL,
        "reciprocal_residual": RECIPROCAL_IDENTITY_RESIDUAL,
        "u_quadratic": U_QUADRATIC,
        "discriminant": U_DISCRIMINANT,
        "discriminant_sign": U_DISCRIMINANT_SIGN,
        "sos_constant": SOS_CONSTANT,
        "sos_residual": SOS_RESIDUAL,
        "u_vertex": U_VERTEX,
        "u_minimum": U_MINIMUM,
        "u_endpoints": (U_AT_PLUS_TWO, U_AT_MINUS_TWO),
        "u_real_roots": U_REAL_ROOTS,
        "u_real_roots_in_band": U_REAL_ROOTS_IN_BAND,
        "new_real_roots": NEW_SECTOR_REAL_ROOTS,
        "new_unimodular_roots": NEW_SECTOR_UNIMODULAR_ROOTS,
        "new_distinct_nonreal": NEW_SECTOR_DISTINCT_NONREAL,
        "cayley_transform": CAYLEY_TRANSFORM,
        "cayley_imaginary_zero": CAYLEY_IMAGINARY_PART_ZERO,
        "cayley_real_roots": CAYLEY_REAL_ROOTS,
        "q_endpoints": (Q_AT_PLUS_ONE, Q_AT_MINUS_ONE),
        "heavy_discriminant": HEAVY_DISCRIMINANT,
        "light_discriminant": LIGHT_DISCRIMINANT,
        "embedded_signs": EMBEDDED_DISCRIMINANT_SIGNS,
        "embedded_products": EMBEDDED_ROOT_PRODUCTS,
        "embedded_sums": EMBEDDED_ROOT_SUMS,
        "embedded_real": EMBEDDED_DISTINCT_REAL_ROOTS,
        "embedded_positive": EMBEDDED_DISTINCT_POSITIVE_ROOTS,
        "embedded_negative": EMBEDDED_DISTINCT_NEGATIVE_ROOTS,
        "embedded_positivity": EMBEDDED_POSITIVITY,
        "new_positivity": NEW_SECTOR_POSITIVITY,
        "sector_gram_signs": SECTOR_GRAM_MINOR_SIGNS,
        "sector_gram_symmetric": SECTOR_GRAM_SYMMETRIC_RESIDUALS,
        # G -- the note, the fence and the nsimplify absence.
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
    elif mutation == "claim_positivity_unscoped":
        # THE SCOUTING RECORD'S REFUTED SENTENCE: monodromy positivity is
        # asserted for the WHOLE X = 8 core rather than for the embedded sector
        # alone.  The new sector's four roots are nonreal.
        claims["positivity_unscoped"] = True
    elif mutation == "claim_new_sector_defect":
        # THE BOUNDARY MISREAD AS AN ERROR: the nonreal sector is asserted to be
        # a defect of the construction.  The core Gram is positive definite on
        # that sector -- what fails is a transfer property, not the build.
        claims["new_sector_is_defect"] = True
    elif mutation == "claim_larger_cell_decided":
        # THE OPEN LEG CLOSED WITHOUT MEASUREMENT: this block is asserted to
        # decide whether an X = 8-native larger unit cell restores positivity.
        # No such construction is built here.
        claims["larger_cell_decided"] = True
    elif mutation == "claim_generic_point_theorem":
        claims["generic_point_theorem"] = True
    elif mutation == "claim_continuum_limit":
        claims["continuum_limit"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_grade_complex":
        claims["grade_complex"] = 1
    elif mutation == "break_hodge_reflection":
        claims["hodge_reflection"] = 1
    elif mutation == "break_carrier_covariance":
        claims["covariance"] = 1
    elif mutation == "break_empty_cross":
        claims["cross"] = 4
    elif mutation == "break_carrier_rank":
        claims["carrier_ranks"] = {4: 64, 8: 126}
    elif mutation == "break_core_gram_definiteness":
        claims["minor_signs"] = {
            4: CORE_MINOR_SIGNS[4],
            8: CORE_MINOR_SIGNS[8][:15] + (-1,)}
    # --- D ----------------------------------------------------------------
    elif mutation == "break_sector_split":
        claims["projector_ranks"] = (12, 4)
    elif mutation == "break_sector_cross_blocks":
        # THE DIRECT SUM DENIED: the two sectors are asserted to be coupled by
        # the Gram, which would make "the embedded sector" not a sector at all.
        claims["cross_gram"] = 8
    elif mutation == "break_embedded_charpoly":
        claims["embedded_charpoly_residual"] = 1
    elif mutation == "break_sector_similarity":
        # THE EMBEDDING REDUCED TO A COINCIDENCE: equal characteristic
        # polynomials are asserted to carry no similarity behind them.  The
        # elementary divisor censuses agree and a nonsingular rational
        # intertwiner is exhibited.
        claims["similar"] = False
    elif mutation == "break_heavy_verbatim":
        claims["heavy"] = (HEAVY_POLYNOMIAL[0], HEAVY_POLYNOMIAL[1] + 1,
                           HEAVY_POLYNOMIAL[2])
    elif mutation == "break_light_verbatim":
        claims["light"] = (LIGHT_POLYNOMIAL[0], LIGHT_POLYNOMIAL[1] + 1,
                           LIGHT_POLYNOMIAL[2])
    elif mutation == "break_new_quartic":
        claims["new_quartic"] = NEW_QUARTIC[:2] + (NEW_QUARTIC[2] + 1,) \
            + NEW_QUARTIC[3:]
    # --- E ----------------------------------------------------------------
    elif mutation == "break_shift_census":
        claims["shift_commutators"] = (0, 4) + (0,) * 6
    elif mutation == "break_u2_commutant":
        claims["shift_commutators"] = (0, 0, 8) + (0,) * 5
    elif mutation == "break_u4_commutant":
        claims["shift_commutators"] = (0,) * 4 + (8,) + (0,) * 3
    elif mutation == "break_odd_shift_isometry":
        # THE SPLIT MADE TRIVIAL: the odd shifts are asserted to be exact Gram
        # isometries too, which would make the whole shift group isometric and
        # the momentum split forced rather than measured.
        claims["shift_gram_defects"] = (0,) * 8
        claims["odd_defect"] = 0
    # --- F ----------------------------------------------------------------
    elif mutation == "break_u_substitution":
        claims["substitution_residual"] = 1
    elif mutation == "break_u_quadratic":
        claims["u_quadratic"] = (U_QUADRATIC[0], U_QUADRATIC[1],
                                 U_QUADRATIC[2] + 1)
    elif mutation == "break_u_discriminant_sign":
        # THE REFUTATION DELETED: the u-discriminant is asserted POSITIVE, which
        # is exactly the scouting record's positivity claim in its arithmetic
        # form.  It is negative by 7271743246281426848714247040000.
        claims["discriminant_sign"] = 1
    elif mutation == "break_sos_certificate":
        claims["sos_constant"] = SOS_CONSTANT + 1
    elif mutation == "break_unimodular":
        # BLOCK 194's SECOND FAILURE MODE MISAPPLIED: the new roots are asserted
        # to be complex UNIMODULAR, which is the mode Block 194 found beyond the
        # Hodge edge.  Here the INDEPENDENT Cayley count is zero, so no root is
        # unimodular either.
        claims["new_unimodular_roots"] = 4
        claims["cayley_real_roots"] = 4
    elif mutation == "break_embedded_positivity":
        # THE OTHER DIRECTION: positivity is asserted to fail on the EMBEDDED
        # sector too, which would make the boundary vacuous by making the whole
        # core fail.  Both landed quadratics have real positive reciprocal
        # roots.
        claims["embedded_positivity"] = False
        claims["embedded_positive"] = 0
    # --- G ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    new = facts.frames[NEW_EXTENT]
    landed = facts.frames[LANDED_EXTENT]
    sectors = facts.sectors
    boundary = facts.boundary

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 197 artifacts are "
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
        "B-3", "POSITIVITY IS SCOPED TO THE EMBEDDED SECTOR AND IS NOT A "
        "STATEMENT ABOUT THE X = 8 CORE: the monodromy roots are real and "
        "positive on the U_4-EVEN sector and NONREAL on the U_4-ODD sector, so "
        "no unscoped positivity claim is made for this carrier",
        claims["positivity_unscoped"] is False)
    checks.check(
        "B-4", "THE NEW SECTOR IS A MEASURED BOUNDARY AND NOT A DEFECT: the "
        "core Gram is positive definite on the whole core AND on EACH sector, "
        "so what fails on the new sectors is the MONODROMY spectral positivity "
        "and not the reflected pairing, and no construction error is implied",
        claims["new_sector_is_defect"] is False)
    checks.check(
        "B-5", "THE LARGER-UNIT-CELL QUESTION IS A NAMED OPEN LEG AND IS NOT "
        "DECIDED HERE: whether an X = 8-native larger unit cell restores "
        "monodromy positivity on the new sectors is neither built, probed nor "
        "excluded by any line of this block",
        claims["larger_cell_decided"] is False)
    checks.check(
        "B-6", "NO GENERIC (m, c) THEOREM AND NO CONTINUUM: ONE width, ONE "
        "rational point, ONE core, ONE unit volume and TWO spatial extents are "
        "measured, and neither a parameter space nor a refinement limit is "
        "claimed",
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

    # --- C: THE CONSTRUCTION AT X = 8 ---------------------------------------
    checks.check(
        "C-1", f"THE GRADE COMPLEX CLOSES AT BOTH EXTENTS: with grade "
        f"deg(t, x) = t mod 2 + x mod 2 and d_K = P1 K P0 + P2 K P1, "
        f"nnz(d_K^2) = {claims['grade_complex']}",
        all(facts.carriers[extent]["grade_complex"] == claims["grade_complex"]
            for extent in EXTENTS))
    checks.check(
        "C-2", f"THE IMPORTED HODGE ASSEMBLES REFLECTION-COVARIANTLY: the "
        f"unit-volume block at c = {FIXTURE[1]} is {claims['hodge_block']} and "
        f"the quarter-weighted four-corner cell average obeys "
        f"nnz(Ps H Ps - H) = {claims['hodge_reflection']} at both extents",
        facts.hodge_block == claims["hodge_block"]
        and all(facts.carriers[extent]["hodge_reflection"]
                == claims["hodge_reflection"] for extent in EXTENTS))
    checks.check(
        "C-3", f"THE COMPLETION IS Ps-COVARIANT AT BOTH EXTENTS: with "
        f"D_s = A_s - Ps A_s Ps and Q = m H + H D_s - D_s^T H, "
        f"nnz(Ps Q Ps - Q^T) = {claims['covariance']}",
        all(facts.carriers[extent]["covariance"] == claims["covariance"]
            for extent in EXTENTS))
    checks.check(
        "C-4", f"THE DIRECTED CROSS BLOCK IS EMPTY AT BOTH EXTENTS: Q has "
        f"{claims['cross']} nonzero entries from the STRICT past half "
        f"{{1..{WIDTH // 2 - 1}}} to the STRICT future half "
        f"{{{WIDTH // 2 + 1}..{WIDTH - 1}}}",
        all(facts.carriers[extent]["cross"] == claims["cross"]
            for extent in EXTENTS))
    checks.check(
        "C-5", f"THE CARRIER CLOSES: rank(Q) = {claims['carrier_ranks']} with "
        f"two-sided inverse residuals ZERO -- ONE exact 128 x 128 inverse and "
        f"ONE exact 64 x 64 inverse, each built once and shared by every gate "
        f"below ({facts.big_inverses} inverse of size 128 built)",
        {extent: facts.carriers[extent]["rank"] for extent in EXTENTS}
        == claims["carrier_ranks"]
        and all(facts.carriers[extent]["inverse_residuals"] == (0, 0)
                for extent in EXTENTS)
        and facts.big_inverses == 1)
    checks.check(
        "C-6", f"THE DEEP CORE GRAM IS SYMMETRIC AND POSITIVE DEFINITE AT BOTH "
        f"EXTENTS: at t0 = {DEEP_CORE}, nnz(K_c - K_c^T) = "
        f"{claims['gram_symmetric']} and the leading principal minor signs are "
        f"{claims['minor_signs'][NEW_EXTENT]} on the {CORE_DIMENSIONS[8]}-cell "
        f"core and {claims['minor_signs'][LANDED_EXTENT]} on the "
        f"{CORE_DIMENSIONS[4]}-cell one",
        all(facts.frames[extent].gram_symmetric == claims["gram_symmetric"]
            for extent in EXTENTS)
        and {extent: facts.frames[extent].minor_signs for extent in EXTENTS}
        == claims["minor_signs"])

    # --- D: THE EMBEDDING ---------------------------------------------------
    checks.check(
        "D-1", f"THE HALF-LATTICE SPLIT IS AN EXACT PARTITION OF THE 16-CELL "
        f"CORE: P_e = (I + U_4)/2 and P_o = (I - U_4)/2 have ranks "
        f"{claims['projector_ranks']}, idempotent residuals "
        f"{claims['idempotent_residuals']} and P_e + P_o - I at residual "
        f"{claims['partition_residual']}",
        sectors.projector_ranks == claims["projector_ranks"]
        and sectors.idempotent_residuals == claims["idempotent_residuals"]
        and sectors.partition_residual == claims["partition_residual"])
    checks.check(
        "D-2", f"BOTH THE GRAM AND THE MONODROMY ARE BLOCK DIAGONAL FOR THAT "
        f"SPLIT, which is what makes 'the embedded sector' a sector: "
        f"nnz(B_e^T K_c B_o) = {claims['cross_gram']} and the two compressed "
        f"monodromy cross blocks are {claims['cross_monodromy']}, and "
        f"charpoly(W) = charpoly(W_e) charpoly(W_o) at residual "
        f"{claims['sector_product_residual']}",
        sectors.cross_gram == claims["cross_gram"]
        and sectors.cross_monodromy == claims["cross_monodromy"]
        and sectors.sector_product_residual
        == claims["sector_product_residual"])
    checks.check(
        "D-3", f"THE EMBEDDING, AS AN EXACT POLYNOMIAL IDENTITY AGAINST A "
        f"REBUILT X = 4 CARRIER AND NOT AGAINST A CITATION: "
        f"charpoly(W_e) - charpoly(W_4) has residual "
        f"{claims['embedded_charpoly_residual']} as monic polynomials over QQ, "
        f"where W_4 is the Z_16 x Z_4 monodromy rebuilt here at the same "
        f"width, fixture, volume and core",
        sectors.embedded_charpoly_residual
        == claims["embedded_charpoly_residual"]
        and landed.factors == claims["embedded_factors"])
    checks.check(
        "D-4", f"AND IT IS A SIMILARITY AND NOT A COINCIDENCE OF COEFFICIENTS: "
        f"the elementary divisor census dim ker p(M)^k is "
        f"{claims['census']} for BOTH W_e and W_4, the Sylvester space "
        f"{{X : X W_4 = W_e X}} has dimension {claims['sylvester_dimension']}, "
        f"and a deterministic sweep exhibits a member of rank "
        f"{claims['intertwiner_rank']} intertwining at residual "
        f"{claims['intertwiner_residual']} (trial "
        f"{sectors.intertwiner_trial})",
        claims["similar"] is True
        and sectors.similar is True
        and sectors.census_embedded == claims["census"]
        and sectors.census_landed == claims["census"]
        and sectors.sylvester_dimension == claims["sylvester_dimension"]
        and sectors.intertwiner_rank == claims["intertwiner_rank"]
        and sectors.intertwiner_residual == claims["intertwiner_residual"])
    checks.check(
        "D-5", f"THE EMBEDDED SPECTRUM IS BLOCK 190's AND BLOCK 194's LANDED "
        f"PAIR VERBATIM, EACH SQUARED: heavy = {claims['heavy']} and light = "
        f"{claims['light']} as primitive integer tuples, at X = 8 on the even "
        f"sector AND at X = 4 on the rebuilt carrier",
        sectors.embedded_factors == ((claims["heavy"], 2), (claims["light"], 2))
        and landed.factors == ((claims["heavy"], 2), (claims["light"], 2)))
    checks.check(
        "D-6", f"THE ODD SECTOR CARRIES EXACTLY ONE NEW FACTOR AND IT IS "
        f"DISPLAYED: {claims['new_quartic']} of multiplicity "
        f"{claims['new_multiplicity']}, irreducible over QQ = "
        f"{claims['new_irreducible']} and palindromic = "
        f"{claims['new_palindromic']}",
        sectors.new_factors == ((claims["new_quartic"],
                                 claims["new_multiplicity"]),)
        and boundary.quartic == claims["new_quartic"]
        and boundary.irreducible is claims["new_irreducible"]
        and boundary.palindromic is claims["new_palindromic"])
    checks.check(
        "D-7", f"SO THE WHOLE X = 8 DEEP-CORE CHARACTERISTIC POLYNOMIAL IS "
        f"{claims['full_factors']} over the exact content "
        f"{claims['full_content']} -- the entire X = 4 spectrum plus ONE new "
        f"doubly degenerate palindromic quartic and nothing else -- while the "
        f"rebuilt X = 4 carrier returns Block 194's OWN declared monic scalar "
        f"{claims['landed_content']}",
        new.factors == claims["full_factors"]
        and new.charpoly_content == claims["full_content"]
        and landed.charpoly_content == claims["landed_content"])

    # --- E: THE COMMUTANTS --------------------------------------------------
    checks.check(
        "E-1", f"ALL EIGHT SPATIAL SHIFTS COMMUTE WITH THE MONODROMY: "
        f"nnz([W, U_j]) = {claims['shift_commutators']} for j = 0..7, with "
        f"nnz(U_1^8 - I) = {claims['shift_order']}",
        new.shift_commutators == claims["shift_commutators"]
        and new.shift_order == claims["shift_order"])
    checks.check(
        "E-2", f"THE TWO SHIFTS THE SCOUTING DESIGN NAMED ARE AMONG THEM: "
        f"nnz([W, U_2]) = {claims['shift_commutators'][2]} and "
        f"nnz([W, U_4]) = {claims['shift_commutators'][4]}",
        new.shift_commutators[2] == claims["shift_commutators"][2]
        and new.shift_commutators[4] == claims["shift_commutators"][4]
        and claims["shift_commutators"][2] == 0
        and claims["shift_commutators"][4] == 0)
    checks.check(
        "E-3", f"BUT THE GRAM SPLITS THEM BY PARITY, WHICH IS WHY THE MOMENTUM "
        f"SPLIT IS A MEASUREMENT AND NOT A GROUP IDENTITY: "
        f"nnz(U_j^T K_c U_j - K_c) = {claims['shift_gram_defects']}, so the "
        f"FOUR even shifts are exact K_c-isometries and the FOUR odd ones each "
        f"carry a {claims['odd_defect']}-entry defect",
        new.shift_gram_defects == claims["shift_gram_defects"]
        and claims["even_isometric"] is True
        and all(claims["shift_gram_defects"][j] == 0 for j in (0, 2, 4, 6))
        and all(claims["shift_gram_defects"][j] == claims["odd_defect"]
                for j in (1, 3, 5, 7)))
    checks.check(
        "E-4", f"AND THE X = 4 CARRIER SHOWS THE SAME PARITY LAW AT ITS OWN "
        f"EXTENT, so the law is of the construction and not of the extent: "
        f"nnz([W_4, U_j]) = {landed.shift_commutators} and "
        f"nnz(U_j^T K_c U_j - K_c) = {landed.shift_gram_defects} for "
        f"j = 0..3",
        all(value == 0 for value in landed.shift_commutators)
        and landed.shift_gram_defects[0] == 0
        and landed.shift_gram_defects[2] == 0
        and landed.shift_gram_defects[1] > 0
        and landed.shift_gram_defects[3] > 0)

    # --- F: THE MOMENTUM BOUNDARY -------------------------------------------
    checks.check(
        "F-1", f"THE u-SUBSTITUTION IS A POLYNOMIAL IDENTITY AND NOT A "
        f"SUBSTITUTION RULE: q(z) = A z^4 + B z^3 + C z^2 + B z + A satisfies "
        f"z^4 q(1/z) - q(z) at residual {claims['reciprocal_residual']} and "
        f"q(z) - z^2 q_u(z + 1/z) at residual "
        f"{claims['substitution_residual']}, with "
        f"q_u(u) = A u^2 + B u + (C - 2A) = {claims['u_quadratic']}",
        boundary.reciprocal_residual == claims["reciprocal_residual"]
        and boundary.substitution_residual == claims["substitution_residual"]
        and boundary.u_quadratic == claims["u_quadratic"])
    checks.check(
        "F-2", f"AND ITS DISCRIMINANT IS NEGATIVE, EXACTLY: "
        f"B^2 - 4 A (C - 2A) = {claims['discriminant']} of sign "
        f"{claims['discriminant_sign']}, with vertex u* = {claims['u_vertex']} "
        f"and minimum q_u(u*) = {claims['u_minimum']} > 0, and q_u(2), q_u(-2) "
        f"= {claims['u_endpoints']}",
        boundary.discriminant == claims["discriminant"]
        and boundary.discriminant_sign == claims["discriminant_sign"]
        and claims["discriminant_sign"] == -1
        and boundary.vertex == claims["u_vertex"]
        and boundary.minimum == claims["u_minimum"]
        and (boundary.at_plus_two, boundary.at_minus_two)
        == claims["u_endpoints"])
    checks.check(
        "F-3", f"THE SIGN IS CERTIFIED WITHOUT EVALUATING A RADICAL, BY AN "
        f"EXACT SUM OF SQUARES: 4 A q_u(u) - (2 A u + B)^2 = "
        f"{claims['sos_constant']} identically, at residual "
        f"{claims['sos_residual']}, so 4 A q_u is a square plus a strictly "
        f"positive integer and q_u is strictly positive on ALL of RR",
        boundary.sos_constant == claims["sos_constant"]
        and boundary.sos_residual == claims["sos_residual"]
        and claims["sos_constant"] > 0)
    checks.check(
        "F-4", f"SO THE NEW SECTOR CARRIES NO REAL EIGENVALUE: a real root z of "
        f"q needs a real root u of q_u and there are {claims['u_real_roots']}; "
        f"counted directly on q itself, there are {claims['new_real_roots']}, "
        f"leaving {claims['new_distinct_nonreal']} distinct NONREAL roots in a "
        f"reciprocal-conjugate quadruple -- so monodromy positivity FAILS on "
        f"the new momentum sectors, at {claims['new_positivity']}",
        boundary.u_real_roots == claims["u_real_roots"]
        and boundary.u_real_roots_in_band == claims["u_real_roots_in_band"]
        and boundary.new_real_roots == claims["new_real_roots"]
        and boundary.new_distinct_nonreal == claims["new_distinct_nonreal"]
        and boundary.new_positivity is claims["new_positivity"]
        and claims["new_positivity"] is False)
    checks.check(
        "F-5", f"AND NO UNIMODULAR ONE EITHER, COUNTED BY A SECOND ROUTE THAT "
        f"NEVER MENTIONS u: the Cayley transform (1 - i w)^4 q((1 + i w)/"
        f"(1 - i w)) is the REAL polynomial {claims['cayley_transform']} in w "
        f"(imaginary part identically zero = "
        f"{claims['cayley_imaginary_zero']}) whose real roots are exactly the "
        f"unimodular roots of q other than z = -1, and it has "
        f"{claims['cayley_real_roots']}; z = 1 and z = -1 are excluded by "
        f"q(1), q(-1) = {claims['q_endpoints']}, both nonzero; total "
        f"unimodular roots {claims['new_unimodular_roots']} -- so this is "
        f"NEITHER of Block 194's two failure modes",
        boundary.cayley_transform == claims["cayley_transform"]
        and boundary.cayley_imaginary_zero is claims["cayley_imaginary_zero"]
        and boundary.cayley_real_roots == claims["cayley_real_roots"]
        and boundary.new_unimodular_roots == claims["new_unimodular_roots"]
        and (boundary.at_plus_one, boundary.at_minus_one)
        == claims["q_endpoints"]
        and boundary.at_plus_one != 0 and boundary.at_minus_one != 0)
    checks.check(
        "F-6", f"WHILE ON THE EMBEDDED SECTOR EVERY EIGENVALUE IS REAL,"
        f"POSITIVE AND RECIPROCAL -- THE OTHER DIRECTION, GATED: the "
        f"discriminants are {claims['heavy_discriminant']} and "
        f"{claims['light_discriminant']} of signs {claims['embedded_signs']}, "
        f"the root products are {claims['embedded_products']} and the root "
        f"sums {claims['embedded_sums']} are positive, giving "
        f"{claims['embedded_real']} distinct real roots of which "
        f"{claims['embedded_positive']} are positive and "
        f"{claims['embedded_negative']} negative",
        boundary.heavy_discriminant == claims["heavy_discriminant"]
        and boundary.light_discriminant == claims["light_discriminant"]
        and boundary.embedded_signs == claims["embedded_signs"]
        and boundary.embedded_products == claims["embedded_products"]
        and boundary.embedded_sums == claims["embedded_sums"]
        and boundary.embedded_real == claims["embedded_real"]
        and boundary.embedded_positive == claims["embedded_positive"]
        and boundary.embedded_negative == claims["embedded_negative"]
        and boundary.embedded_positivity is claims["embedded_positivity"]
        and claims["embedded_positivity"] is True)
    checks.check(
        "F-7", f"AND THE POSITIVITY THAT DOES NOT FAIL IS NAMED, WHICH IS WHY "
        f"THIS IS A BOUNDARY AND NOT A DEFECT: the compressed Grams "
        f"K_e = B_e^T K_c B_e and K_o = B_o^T K_c B_o are symmetric at "
        f"residuals {claims['sector_gram_symmetric']} with leading principal "
        f"minor signs {claims['sector_gram_signs']} -- BOTH sectors carry a "
        f"positive definite reflected pairing, and only the MONODROMY spectral "
        f"positivity distinguishes them",
        sectors.gram_symmetric_residuals == claims["sector_gram_symmetric"]
        and sectors.gram_minor_signs == claims["sector_gram_signs"]
        and all(all(sign > 0 for sign in signs)
                for signs in claims["sector_gram_signs"]))

    # --- G: THE NOTE, THE FENCE AND THE nsimplify ABSENCE -------------------
    checks.check(
        "G-1", f"the note is present at {NOTE_PATH.name} and the N5 fence "
        f"appears in it VERBATIM as a single line",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "G-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can turn a nonzero defect into a zero one or a negative "
        f"discriminant into a vanishing one",
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
    print(f"  exact 128 x 128 inverses built and shared: {facts.big_inverses}")
    print(f"  imported unit-volume block at c = {FIXTURE[1]}: "
          f"{facts.hodge_block}")
    for extent in EXTENTS:
        record = facts.carriers[extent]
        frame = facts.frames[extent]
        print(f"  Z_{WIDTH} x Z_{extent} at (m, c) = ({FIXTURE[0]}, "
              f"{FIXTURE[1]}), unit volume, t0 = {DEEP_CORE}")
        print(f"    nnz(d_K^2) {record['grade_complex']}, nnz(Ps H Ps - H) "
              f"{record['hodge_reflection']}, nnz(Ps Q Ps - Q^T) "
              f"{record['covariance']}, directed cross block {record['cross']}")
        print(f"    rank(Q) {record['rank']} of {record['size']}, inverse "
              f"residuals {record['inverse_residuals']}, inverse built in "
              f"{record['inverse_seconds']:.1f}s")
        print(f"    core dimension {frame.dimension}, nnz(K_c - K_c^T) "
              f"{frame.gram_symmetric}, leading principal minor signs "
              f"{frame.minor_signs}")
        print(f"    charpoly(W) primitive factors {frame.factors} over content "
              f"{frame.charpoly_content}")
        print(f"    shift commutators {frame.shift_commutators}, shift Gram "
              f"defects {frame.shift_gram_defects}, nnz(U_1^{extent} - I) "
              f"{frame.shift_order}")
    sectors = facts.sectors
    print("  THE HALF-LATTICE SPLIT OF THE X = 8 CORE")
    print(f"    projector ranks {sectors.projector_ranks}, idempotent "
          f"residuals {sectors.idempotent_residuals}, partition residual "
          f"{sectors.partition_residual}")
    print(f"    cross Gram {sectors.cross_gram}, cross monodromy "
          f"{sectors.cross_monodromy}, charpoly product residual "
          f"{sectors.sector_product_residual}")
    print(f"    EMBEDDED sector factors {sectors.embedded_factors}")
    print(f"    NEW sector factors {sectors.new_factors}")
    print(f"    charpoly(W_e) - charpoly(W_4) residual "
          f"{sectors.embedded_charpoly_residual}, elementary divisor census "
          f"W_e {sectors.census_embedded}, W_4 {sectors.census_landed}, "
          f"similar over QQ {sectors.similar}")
    print(f"    Sylvester dimension {sectors.sylvester_dimension}, "
          f"nonsingular intertwiner at deterministic trial "
          f"{sectors.intertwiner_trial} of rank {sectors.intertwiner_rank}, "
          f"intertwining residual {sectors.intertwiner_residual}")
    print(f"    sector Grams: symmetric residuals "
          f"{sectors.gram_symmetric_residuals}, minor signs "
          f"{sectors.gram_minor_signs}")
    boundary = facts.boundary
    print("  THE MOMENTUM BOUNDARY")
    print(f"    q(z) = {boundary.quartic}, palindromic {boundary.palindromic}, "
          f"irreducible over QQ {boundary.irreducible}, z^4 q(1/z) - q(z) "
          f"residual {boundary.reciprocal_residual}")
    print(f"    q(z) - z^2 q_u(z + 1/z) residual "
          f"{boundary.substitution_residual}, q_u = {boundary.u_quadratic}")
    print(f"    DISCRIMINANT {boundary.discriminant} of sign "
          f"{boundary.discriminant_sign}")
    print(f"    SOS certificate 4 A q_u(u) - (2 A u + B)^2 = "
          f"{boundary.sos_constant} at residual {boundary.sos_residual}")
    print(f"    vertex {boundary.vertex}, minimum {boundary.minimum}, q_u(2) "
          f"{boundary.at_plus_two}, q_u(-2) {boundary.at_minus_two}")
    print(f"    real u-roots {boundary.u_real_roots}, real u-roots in [-2, 2] "
          f"{boundary.u_real_roots_in_band}")
    print(f"    CAYLEY transform (1 - i w)^4 q((1 + i w)/(1 - i w)) = "
          f"{boundary.cayley_transform}, imaginary part identically zero "
          f"{boundary.cayley_imaginary_zero}, real roots "
          f"{boundary.cayley_real_roots}; q(1) {boundary.at_plus_one}, q(-1) "
          f"{boundary.at_minus_one}")
    print(f"    NEW sector: real roots {boundary.new_real_roots}, unimodular "
          f"roots {boundary.new_unimodular_roots}, distinct nonreal "
          f"{boundary.new_distinct_nonreal}, positivity "
          f"{boundary.new_positivity}")
    print(f"    EMBEDDED sector: discriminants "
          f"({boundary.heavy_discriminant}, {boundary.light_discriminant}) of "
          f"signs {boundary.embedded_signs}, root products "
          f"{boundary.embedded_products}, root sums {boundary.embedded_sums}, "
          f"distinct real {boundary.embedded_real}, positive "
          f"{boundary.embedded_positive}, negative "
          f"{boundary.embedded_negative}, positivity "
          f"{boundary.embedded_positivity}")
    print("  READINGS, AND EACH IS A READING")
    for reading in READINGS:
        print(f"    {reading}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}")
    print("  NOT CLAIMED: NO GRAVITY. NO UNSCOPED POSITIVITY -- IT IS SCOPED "
          "TO THE EMBEDDED SECTOR AND FAILS ON THE NEW ONE. THE NEW-SECTOR "
          "NONREALITY IS A MEASURED BOUNDARY AND NOT A DEFECT -- BOTH SECTOR "
          "GRAMS ARE POSITIVE DEFINITE. THE LARGER-UNIT-CELL QUESTION IS NOT "
          "DECIDED. NO GENERIC (m, c) THEOREM. NO CONTINUUM. THE READINGS ARE "
          "READINGS.")
    print()


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE WORD POSITIVITY IS SCOPED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE CONSTRUCTION AT T = 16 WITH THE SPATIAL EXTENT PROMOTED FROM A FIXTURE TO A PARAMETER (the staggered Dirac-Kahler carrier on Z_T x Z_X with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), THE SECOND SPATIAL EXTENT X = 8 WHICH IS THIS BLOCK's ONE NEW CONSTRUCTION ELEMENT AND IS ONE CARRIER AND NOT A FAMILY (Z_16 x Z_8 at the SINGLE control fixture (m, c) = (9/20, 5/13) at unit volume, built beside the landed Z_16 x Z_4 carrier at the SAME width, the SAME fixture, the SAME volume and the SAME deep core t0 = 3), BLOCK 190's CORE FRAME AT THE DEEP CORE t0 = 3 WIDENED WITH THE EXTENT (the 2X cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, and the UNIT-CELL MONODROMY W = K_c^-1 L_2), THE HALF-LATTICE MOMENTUM SPLIT (the spatial shifts U_j by j sites on both time layers of the core, the two real projectors P_e = (I + U_{X/2})/2 and P_o = (I - U_{X/2})/2 as exact rational idempotents of equal rank X summing to I_{2X}, the column-space bases B_e, B_o and their exact coordinate left inverses pi = (B^T B)^-1 B^T), BLOCK 190's AND BLOCK 194's LANDED HEAVY/LIGHT PAIR AT THE CONTROL IMPOSED AS THE COMPARISON TARGET AND ALSO REBUILT HERE RATHER THAN ONLY CITED (22569375 z^2 - 233631106 z + 22569375 and 39529825 z^2 - 109432706 z + 39529825), and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module at UNIT VOLUME and at the ONE rational shear 5/13 -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORDS EMBEDDING AND POSITIVITY AND IS SAID IN THOSE WORDS: 'EMBEDDING' NAMES AN EXACT EQUALITY OF CHARACTERISTIC POLYNOMIALS AND A QQ-SIMILARITY BETWEEN ONE 8-DIMENSIONAL COMPRESSED OPERATOR AND ONE REBUILT 8 x 8 MONODROMY, AT ONE CORE OF ONE WIDTH AT ONE RATIONAL POINT, AND NAMES NOTHING ELSE. 'POSITIVITY' NAMES TWO DIFFERENT STATEMENTS AND THE NOTE NEVER LETS THEM MERGE: THE POSITIVE DEFINITENESS OF THE REFLECTED PAIRING K_c, WHICH HOLDS ON THE WHOLE 16-DIMENSIONAL CORE AND ON EACH SECTOR SEPARATELY AT 8 OF 8 POSITIVE LEADING PRINCIPAL MINORS, AND THE REALITY AND POSITIVITY OF THE MONODROMY SPECTRUM, WHICH HOLDS ON THE EMBEDDED SECTOR AND FAILS ON THE NEW ONE. THE SCOUTING RECORD's SENTENCE THAT THE NEW PALINDROMIC QUARTIC IS POSITIVE IS FALSE AND IS CORRECTED HERE AS CONTENT: THE u-SUBSTITUTION DISCRIMINANT IS EXACTLY -7271743246281426848714247040000, ALL FOUR NEW-SECTOR ROOTS ARE NONREAL, AND NO POSITIVITY CLAIM IS MADE FOR THE X = 8 CORE AS A WHOLE. THE NEW-SECTOR NONREALITY IS A MEASURED BOUNDARY OF A TRANSFER PROPERTY AND NOT A DEFECT OF THE CONSTRUCTION: THE CARRIER CLOSES AT rank(Q) = 128 WITH TWO-SIDED INVERSE RESIDUALS ZERO, THE CROSS BLOCK IS EMPTY, AND THE GRAM IS POSITIVE DEFINITE ON EXACTLY THE SECTOR WHOSE SPECTRUM IS NONREAL. WHETHER AN X = 8-NATIVE LARGER UNIT CELL RESTORES MONODROMY POSITIVITY ON THE NEW SECTORS IS A NAMED OPEN LEG AND IS NEITHER BUILT, PROBED NOR EXCLUDED HERE. NO GENERIC (m, c) THEOREM IS SUPPLIED AND NO CONTINUUM LIMIT IS SUPPLIED: ONE WIDTH, ONE RATIONAL POINT, ONE CORE, ONE UNIT VOLUME AND TWO SPATIAL EXTENTS ARE NOT A PARAMETER SPACE AND ARE NOT A REFINEMENT LIMIT. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE CONSTRUCTION SURVIVES THE SPATIAL REFINEMENT INTACT, AND EVERY STATEMENT IN THIS SECTION IS AN EXACT ENTRY COUNT. At T = 16, (m, c) = (9/20, 5/13), unit volume and the deep core t0 = 3, the carrier is rebuilt at BOTH spatial extents from the same formulas, and at BOTH: nnz(d_K^2) = 0 with grade deg(t, x) = t mod 2 + x mod 2; the imported unit-volume Hodge block diag(1, [[169/144, -65/144], [-65/144, 169/144]], 1) assembles by Block 191's quarter-weighted four-corner cell average to nnz(Ps H Ps - H) = 0; the completion obeys nnz(Ps Q Ps - Q^T) = 0; and the DIRECTED CROSS BLOCK IS EMPTY at 0 entries from the strict past half {1..7} to the strict future half {9..15}. THE CARRIER CLOSES AT BOTH EXTENTS: rank(Q) = 128 of 128 at X = 8 and 64 of 64 at X = 4, with two-sided inverse residuals ZERO in both cases. EXACTLY ONE 128 x 128 EXACT INVERSE AND ONE 64 x 64 EXACT INVERSE ARE BUILT IN THIS RUNNER, EACH ONCE, AND EVERY GATE BELOW READS THEM RATHER THAN RECOMPUTING THEM. AND THE DEEP-CORE GRAM IS SYMMETRIC AND POSITIVE DEFINITE AT BOTH EXTENTS: nnz(K_c - K_c^T) = 0, with ALL SIXTEEN leading principal minors strictly positive on the 16-cell X = 8 core and all eight strictly positive on the 8-cell X = 4 core, by the exact Sylvester criterion over QQ and with no eigenvalue computed anywhere.\\nper_mode: THE EMBEDDING, AND IT IS A SECTOR STATEMENT AND A SIMILARITY RATHER THAN A COINCIDENCE OF COEFFICIENTS. The half-lattice shift U_4 gives the real projectors P_e = (I + U_4)/2 and P_o = (I - U_4)/2, exact rational idempotents of ranks 8 and 8 whose sum is I_16 at residual 0. BOTH THE GRAM AND THE MONODROMY ARE BLOCK DIAGONAL FOR THAT SPLIT, WHICH IS WHAT MAKES 'THE EMBEDDED SECTOR' A SECTOR AT ALL: nnz(B_e^T K_c B_o) = 0 and both compressed monodromy cross blocks are 0, and charpoly(W) = charpoly(W_e) charpoly(W_o) at residual 0. ON THE EVEN SECTOR THE COMPRESSED MONODROMY REPRODUCES THE X = 4 MONODROMY EXACTLY: charpoly(W_e) - charpoly(W_4) = 0 as monic polynomials over QQ, where W_4 is the Z_16 x Z_4 monodromy REBUILT HERE at the same width, fixture, volume and core rather than cited from a runner. AND THE AGREEMENT IS A SIMILARITY: the elementary divisor census dim ker p(M)^k is (4, 4, 4) for the heavy factor and (4, 4, 4) for the light one, for BOTH W_e and W_4, so the two have the same Frobenius normal form; the Sylvester space {X : X W_4 = W_e X} has dimension 16; and a deterministic sweep of integer combinations exhibits a member of rank 8 intertwining at residual 0. THE EMBEDDED SPECTRUM IS BLOCK 190's AND BLOCK 194's LANDED PAIR VERBATIM, EACH SQUARED: 22569375 z^2 - 233631106 z + 22569375 and 39529825 z^2 - 109432706 z + 39529825 as primitive integer tuples, at X = 8 on the even sector AND at X = 4 on the rebuilt carrier. THE ODD SECTOR CARRIES EXACTLY ONE NEW FACTOR, OF MULTIPLICITY TWO, IRREDUCIBLE OVER QQ AND PALINDROMIC: 1035991876210625 z^4 - 10651994137075200 z^3 + 31207521664211586 z^2 - 10651994137075200 z + 1035991876210625. SO THE WHOLE X = 8 DEEP-CORE CHARACTERISTIC POLYNOMIAL IS THE ENTIRE X = 4 SPECTRUM PLUS ONE NEW DOUBLY DEGENERATE PALINDROMIC QUARTIC AND NOTHING ELSE, over the exact content 1/854282575605737410298720470187055375971422309970855712890625.\\nper_block: THE MOMENTUM POSITIVITY BOUNDARY, AND IT IS THIS BLOCK's CENTRE AND ALSO A REFUTATION OF ITS OWN SCOUTING RECORD. Write the new factor q(z) = A z^4 + B z^3 + C z^2 + B z + A with A = 1035991876210625, B = -10651994137075200 and C = 31207521664211586. TWO POLYNOMIAL IDENTITIES CARRY THE WHOLE ARGUMENT AND BOTH ARE GATED AT RESIDUAL ZERO: z^4 q(1/z) = q(z), so the root set is closed under z -> 1/z and the root product is exactly 1; and q(z) = z^2 q_u(z + 1/z) with q_u(u) = A u^2 + B u + (C - 2A) = 1035991876210625 u^2 - 10651994137075200 u + 29135537911790336. THE DISCRIMINANT OF q_u IS NEGATIVE, EXACTLY: B^2 - 4 A (C - 2A) = -7271743246281426848714247040000. THE SIGN IS CERTIFIED WITHOUT EVALUATING A SINGLE RADICAL, BY AN EXACT SUM OF SQUARES: 4 A q_u(u) - (2 A u + B)^2 = 7271743246281426848714247040000 identically, so 4 A q_u is a perfect square plus a strictly positive integer and q_u is strictly positive on ALL of RR, with vertex u* = 213039882741504/41439675048425, minimum q_u(u*) = 2908697298512570739485698816/1657587001937, q_u(2) = 11975517142482436 and q_u(-2) = 54583493690783236. TWO CONSEQUENCES FOLLOW AND BOTH ARE COUNTED DIRECTLY RATHER THAN INFERRED: a REAL root z of q forces a REAL root u of q_u and q_u has 0 of them, so q has 0 real roots and 4 distinct NONREAL roots; and a UNIMODULAR root z of q forces a real root u of q_u in [-2, 2] and q_u has 0 of those, a count CONFIRMED BY A SECOND ROUTE THAT NEVER MENTIONS u -- the Cayley transform (1 - i w)^4 q((1 + i w)/(1 - i w)) is the REAL polynomial 54583493690783236 w^4 + 49983140813895672 w^2 + 11975517142482436, whose imaginary part vanishes identically and whose real roots are exactly the unimodular roots of q other than z = -1, and it has 0 of them, while z = 1 and z = -1 are excluded by q(1) = 11975517142482436 and q(-1) = 54583493690783236, both nonzero. SO THE FOUR NEW-SECTOR EIGENVALUES ARE NONREAL AND OFF THE UNIT CIRCLE, IN A RECIPROCAL-CONJUGATE QUADRUPLE. ON THE EMBEDDED SECTOR THE OPPOSITE HOLDS AND IS GATED IN THE SAME DETAIL: the heavy and light discriminants are 52545986939220736 and 5725088884359936, both strictly positive; both root products are exactly 1; both root sums 233631106/22569375 and 109432706/39529825 are positive; so all 4 distinct roots are real, positive and reciprocal, with 0 negative. THE SCOUTING RECORD's POSITIVITY SENTENCE IS THEREFORE FALSE AND IS CARRIED HERE AS CORRECTION 82 RATHER THAN AS AN ERRATUM.\\nlattice_wide: THE COMMUTANTS, AND THE PARITY LAW THAT MAKES THE SPLIT A MEASUREMENT. ALL EIGHT spatial shifts commute with the unit-cell monodromy exactly: nnz([W, U_j]) = 0 for every j = 0..7, with nnz(U_1^8 - I_16) = 0. IN PARTICULAR THE TWO SHIFTS THE SCOUTING DESIGN NAMED COMMUTE: nnz([W, U_2]) = nnz([W, U_4]) = 0. BUT THE GRAM SPLITS THEM BY PARITY, AND THAT IS WHY THE MOMENTUM SPLIT IS A MEASUREMENT AND NOT A GROUP IDENTITY: nnz(U_j^T K_c U_j - K_c) = (0, 256, 0, 256, 0, 256, 0, 256) for j = 0..7, so the FOUR EVEN shifts are exact K_c-isometries and the FOUR ODD ones each carry a 256-entry Gram defect. THE SAME PARITY LAW HOLDS AT THE LANDED EXTENT ON ITS OWN CORE -- all four X = 4 shifts commute and the Gram defects are 0 for j = 0, 2 and strictly positive for j = 1, 3, which is Block 190's own S-versus-U asymmetry read at the new extent's scale. SO THE SHIFT GROUP GRADES THE MONODROMY WITHOUT PRESERVING THE PAIRING, EXACTLY AS IT DID AT X = 4, AND THE HALF-LATTICE PROJECTORS ARE BUILT FROM AN ISOMETRIC ELEMENT U_4 RATHER THAN FROM A NON-ISOMETRIC ONE. THE FAILURE MODE ON THE NEW SECTORS IS ALSO SEPARATED FROM BOTH OF BLOCK 194's: that block classified its positivity failures as a REAL NEGATIVE reciprocal pair below the Hodge edge and as a COMPLEX UNIMODULAR pair beyond it. This one is NEITHER -- the u-quadratic has no real root at all, so the quadruple is nonreal AND non-unimodular, and it occurs at c = 5/13, well inside the Hodge edge, at a fixture where the X = 4 spectrum is fully positive.\\nper_scope: WHICH POSITIVITY FAILS IS SAID EXPLICITLY, BECAUSE TWO DIFFERENT ONES ARE IN PLAY, AND WHAT REMAINS OPEN IS NAMED. THE REFLECTED PAIRING STAYS POSITIVE DEFINITE ON THE NEW SECTOR: the compressed Grams K_e = B_e^T K_c B_e and K_o = B_o^T K_c B_o are exactly symmetric and BOTH carry 8 of 8 strictly positive leading principal minors. What fails on the new sectors is the REALITY AND POSITIVITY OF THE MONODROMY SPECTRUM and nothing else, so the new momentum sectors are a MEASURED BOUNDARY of a transfer property and NOT a defect of the construction -- and both halves of that sentence are gated. WHAT REMAINS OPEN IS NAMED AND NOT PAPERED OVER: whether an X = 8-NATIVE LARGER UNIT CELL -- a two-site-wide cell matched to the refined lattice rather than the four-corner cell carried from X = 4 -- restores monodromy positivity on the new sectors is NOT decided, because no such construction is built here; WHY the old spectrum embeds verbatim is NOT derived, and the embedding is exhibited rather than explained; ONE core t0 = 3, ONE width T = 16, ONE rational point (9/20, 5/13) and ONE unit volume are probed, and two spatial extents are not a refinement family; no third extent is measured, so nothing here is a statement about X = 16 or about a limit; and no Osterwalder-Schrader reconstruction, no transfer interpretation and no physical dispersion reading of any root in this note is supplied by any line of this block.\\nRESULT: ON A SECOND CARRIER Z_16 x Z_8 AT THE CONTROL FIXTURE AND THE DEEP CORE t0 = 3, THE HALF-LATTICE SHIFT U_4 SPLITS THE 16-DIMENSIONAL CORE INTO TWO 8-DIMENSIONAL SECTORS THAT ARE BLOCK DIAGONAL FOR BOTH THE GRAM AND THE MONODROMY; THE EVEN SECTOR REPRODUCES THE Z_16 x Z_4 MONODROMY EXACTLY -- charpoly(W_e) = charpoly(W_4) AS MONIC POLYNOMIALS OVER QQ, WITH EQUAL ELEMENTARY DIVISOR CENSUSES AND AN EXPLICIT NONSINGULAR RATIONAL INTERTWINER, SO BLOCK 190's AND BLOCK 194's LANDED HEAVY/LIGHT PAIR EMBEDS VERBATIM AND STAYS REAL, POSITIVE AND RECIPROCAL; AND THE ODD SECTOR CARRIES ONE NEW IRREDUCIBLE PALINDROMIC QUARTIC OF MULTIPLICITY TWO WHOSE u-SUBSTITUTION DISCRIMINANT IS EXACTLY -7271743246281426848714247040000, SO ALL FOUR OF ITS ROOTS ARE NONREAL AND OFF THE UNIT CIRCLE AND THE MONODROMY POSITIVITY DOES NOT EXTEND TO THE NEW MOMENTUM SECTORS. THAT IS A MOMENTUM POSITIVITY BOUNDARY, IT IS MEASURED IN BOTH DIRECTIONS, AND IT REFUTES THIS LANE's OWN SCOUTING SENTENCE THAT THE NEW QUARTIC IS POSITIVE. THE REFLECTED PAIRING IS POSITIVE DEFINITE ON BOTH SECTORS, SO THE BOUNDARY IS A PROPERTY OF THE TRANSFER SPECTRUM AND NOT A DEFECT OF THE BUILD. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-197 STAND EXACTLY AS LANDED. BLOCK 190 AND BLOCK 194 ARE NOT CORRECTED: their heavy/light pair at the control is rebuilt here from the same formulas at the same width, fixture, volume and core, reproduced digit for digit, and shown to EMBED in the refined carrier rather than to be revised by it; Block 194's two failure modes stand as landed and this block's new mode is separated from both rather than merged with either. THIS BLOCK's OWN DEFECTS ARE DISCLOSED: ONE width, ONE rational point, ONE core, ONE unit volume and TWO spatial extents -- not a refinement family, not a parameter space and not a limit; the embedding is EXHIBITED and not DERIVED; the larger-unit-cell question is NAMED and not answered; and no third extent is measured, so nothing here constrains X = 16. ONE ITEM IS FOLDED FROM THE ADVERSARIAL CHECK AS THE BLOCK's CENTRE AND NOT AS AN ERRATUM: the REFUTATION of the scouting record's positivity sentence for the new quartic, carried as correction 82 with its exact negative discriminant, its sum-of-squares certificate and its two root counts. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its SCOUT MODE, S1 DESIGN, SCOUT S1 RESULT and BATCH-1 CHECK VERDICT anchors.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
