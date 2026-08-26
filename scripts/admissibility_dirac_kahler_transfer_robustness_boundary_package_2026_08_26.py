#!/usr/bin/env python3
"""BLOCK 200 -- FINITE EXACT TRANSFER-ROBUSTNESS PROBES: A FOURTH-WIDTH
MEASUREMENT, TWO CLASSIFIED SHEAR ENDPOINTS, A DECLARED [4/4] INTERPOLATION
MODEL, FIRST-ORDER VOLUME RESPONSES, AND SEVEN POSITIVE VOLUME SAMPLES.

THE RESULT, AND ITS EXACT SCOPE.  Block 190 landed a unit-cell monodromy
W = K_c^-1 L_2 on pair cores of a staggered Dirac-Kahler carrier, with a
positive reciprocal spectrum at its deep cores.  This block is FOUR ROBUSTNESS
MEASUREMENTS on that object, and TWO OF THE FOUR CORRECT THE WORDING OF THE
SCOUT RECORD THEY COME FROM.  Nothing here is a new construction.

  (i) THE WIDTH LOCK EXTENDS, AND ITS WIDTH LIST IS CORRECTED WHILE IT DOES.
      At T = 24 -- ONE exact 96 x 96 inverse, the only heavy object in this
      runner -- the deep core t0 = 3 reproduces the LANDED pair squared and the
      near-boundary core t0 = 1 reproduces the LANDED boundary value, both digit
      for digit.  BUT THE DEEP LOCK IS T = 16, 20, 24 AND NOT T = 12, 16, 20,
      24: at T = 12 the slot t0 = 3 IS the seam mirror T/2 - 3, it is NOT a deep
      core, and it is measured here to carry a DIFFERENT quadratic.  The
      BOUNDARY lock does hold at all four widths.

 (ii) TWO CLASSIFIED ENDPOINTS AND AN INTERPOLATION MODEL.  The two exact
      shears 1213333/1703936 and 151669/212992 are separated by 19/1703936.
      The first has positive reciprocal heavy/light pairs and the second has a
      negative reciprocal heavy pair.  Ten additional exact carrier values
      determine a unique declared [4/4] rational interpolation model

        beta_H(c) = -2 N(c) / D(c),
        N = 1362 c^4 + 800 c^3 - 5529 c^2 - 1600 c + 5448,
        D =  400 c^4 + 800 c^3 - 1681 c^2 - 1600 c + 1600,

      with gcd(N, D) = 1.  For THIS MODEL, D has exactly one bracket root, N has
      none, and |beta_H| > 2 on the punctured bracket.  The model therefore has
      a pole rather than a numerator zero and its projective quadratic
      (D,-2N,D) degenerates there.  The model matches fourteen exact carrier
      probes (ten fit points, two withheld points, and two endpoint probes), but
      no degree bound or symbolic identity for the carrier has been proved.
      Consequently none of the model's between-probe statements is promoted to
      a theorem about the physical carrier.

(iii) THE FIRST-ORDER VOLUME RESPONSE, AND THE SCOUT'S "PER-SINGLE-CELL" WORDING
      IS WRONG WHILE ITS SIX NUMBERS ARE RIGHT.  The six quoted tr(dW) values
      are responses of a FULL SLICE CELL -- the sum of all four spatial anchors
      at a temporal anchor s, each with its reflected image partner -- and NOT
      of one (s, x) cell.  The individual (s, x) responses SPLIT BY SPATIAL
      PARITY: at most two values per slice, with two distinct values on the four
      nonzero interior slices and one common zero at each endpoint.  The
      window-law zeros at s = 1 and s = 6 hold AT EVERY SPATIAL ANCHOR
      SEPARATELY and not only after a cancellation in the sum.

 (iv) THE VOLUME SAMPLES, AND THE INTERVAL THAT WAS CLAIMED IS NOT AN INTERVAL.
      Positivity holds at ALL SEVEN of v = 1/100, 1/10, 1/5, 2/5, 3/5, 4/5, 6/5.
      The scout's "(1/10, 1]" EXCLUDES the very endpoint v = 1/10 it also claims,
      and positivity holds at 1/100 and at 6/5, outside both of its ends.  WHAT
      IS RECORDED IS SEVEN SAMPLES.  NO INTERVAL IS CLAIMED, NO EDGE IS LOCATED
      AND NOTHING BETWEEN THE SAMPLES IS ASSERTED EITHER WAY.

ALL OF IT IS FINITE EXACT LINEAR ALGEBRA OVER QQ ON ONE CARRIER FAMILY AT ONE
MASS, AT FOUR WIDTHS, AT FINITELY MANY EXACT RATIONAL SHEARS AND VOLUMES.  NONE
OF IT SUPPLIES GRAVITY, A SEMIGROUP, A GENERATOR, A HAMILTONIAN, AN ENERGY, A
MASS, A BOUNDARY CURVE OR A CONTINUUM LIMIT.

  0. THE WIDTH LOCK (C).  The carrier at four widths with its two-sided inverse
     residuals; the deep census at T = 16, 20, 24 and the corrected T = 12 slot;
     the boundary census at all four widths; and the ONE 96 x 96 inverse.

  1. THE ENDPOINTS AND INTERPOLATION MODEL (D).  The two endpoints with four
     quadratics, discriminants, margins, palindromicity and multiplicities; the
     exact [4/4] fit of beta_H from TEN measured points with TWO WITHHELD points
     at zero residual; the model's Sturm counts and pole; projective agreement
     at seven probes; and the model's band exclusion on the punctured bracket.

  2. THE RESPONSE PROFILE (E).  The six slice-cell values EXACT; the spatial
     parity split; the per-anchor window law; and the s = 4 -> s = 5 sign flip.

  3. THE VOLUME SAMPLES (F).  Seven volumes, each with two distinct palindromic
     squared factors, positive leading coefficients, positive margins and
     positive discriminants -- as SAMPLES and never as a region.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GRAVITY.  NO WINDOW
BOUNDARY CURVE AND NO LOCATED EDGE.  NO MAXIMAL VOLUME INTERVAL.  NO ALL-WIDTH
THEOREM.  NO GENERIC (m, c) THEOREM.  NO CONTINUUM.  NO DYNAMICS.  THE READINGS
ARE READINGS.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 199 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: seven imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, a window boundary curve, a located edge, a
     maximal volume interval, an all-width theorem, a generic-point theorem, the
     continuum limit, a dynamics and licensed readings ALL declared NOT CLAIMED
     as measured constants, and nine gravity structures enumerated as NOT
     SUPPLIED.
  C  THE WIDTH LOCK: the carrier at T = 12, 16, 20, 24 with grade, Hodge
     reflection, covariance and TWO-SIDED inverse residuals all ZERO; the deep
     census locked at T = 16, 20, 24; the T = 12 slot t0 = 3 measured DIFFERENT
     and declared the seam mirror; the boundary census locked at all four; and
     EXACTLY ONE 96 x 96 inverse built.
  D  THE ENDPOINTS AND MODEL: both endpoints' primitive quadratics with their
     leading and linear coefficient SIGNS, discriminants, margins and squared
     multiplicities; the reconstruction with gcd(N, D) = 1 and both withheld
     points at ZERO residual; the model's Sturm counts 1 and 0; endpoint signs
     of D and N; projective agreement at SEVEN probes; and ZERO roots of
     N -+ D in the bracket for the declared model only.
  E  THE RESPONSE PROFILE: the six slice-cell values; at most two
     parity-labelled values per slice, distinct on s = 2,3,4,5 and coincident
     at zero on s = 1,6; the per-anchor window zeros; and the sign flip.
  F  THE VOLUME SAMPLES: seven volumes, each two distinct palindromic squared
     factors with positive leading coefficient, margin and discriminant.
  G  the note at its final path, the N5 fence byte-identical, the nsimplify
     count measured ZERO in this file's own source, and NO sympy Float anywhere
     in any carrier matrix built by this runner.

BASELINE EXPECTATION: A through G PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: thirty-three declared mutations, each of which rewrites
  the ONE CLAIM its name denies -- a few rewrite the two or three constants that
  state that claim jointly -- and each of which must flip EXACTLY ONE FAMILY to
  FAIL.  Every measurement happens once, before any mutation flag is consulted,
  so a mutation can only rewrite a CLAIM and no gate can cascade into another.
  The per-family census is A 2, B 9, C 5, D 6, E 4, F 4, G 3, run against
  thirty-three checks with the same per-family census.  TWO of the thirty-three
  -- break_twelve_deep_core and break_window_law_zeros -- fail TWO checks inside
  their OWN family, because the claim each denies is gated twice; neither
  touches a second family, which is the contract that is enforced.
  SEVEN OF THE THIRTY-THREE GUARD CORRECTIONS RATHER THAN RESULTS:
  break_twelve_deep_core asserts the T = 12 slot t0 = 3 carries the deep value,
  which it does not because that slot is the seam mirror; break_zero_crossing
  gives the interpolation model a numerator zero; break_unimodular_band asserts that
  the fitted-model roots pass through the unit circle away from its pole;
  break_parity_split asserts the scout's "per-single-cell" reading;
  break_endpoint_membership
  asserts the "(1/10, 1]" reading in which v = 1/10 is excluded;
  claim_volume_interval_maximal asserts the sampled set is a maximal interval;
  and claim_window_boundary_curve asserts the edge is a fitted curve, which
  Block 194's own fence forbids.

RUNNING
  python3 scripts/admissibility_dirac_kahler_transfer_robustness_boundary_package_2026_08_26.py
  python3 ... --list-mutations
  python3 ... --mutation break_zero_crossing
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
# shear_hodge() re-exported by the Block 128 module, read here at the ONE shear
# this block probes structurally and at the seven volumes it samples.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_ROBUSTNESS_BOUNDARY_PACKAGE_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 199 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 198 tip.
BLOCK199_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HEAVY_METRIC_OPERATOR_COMPLETION_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
BLOCK199_RUNNER = (
    "scripts/admissibility_dirac_kahler_heavy_metric_operator_completion_"
    "2026_08_26.py"
)
PARENT_ARTIFACTS = (BLOCK199_NOTE, BLOCK199_RUNNER)
# Refreshed by anchored sed at landing, exactly as the five pins are.
PARENT_ARTIFACT_BLOBS = (
    "604010424c9f87d27ecf1cfb92325c154da018ae",   # Block 199 note
    "f9da0a140ab0f024c86396802b3828b2bbe371b5",   # Block 199 runner
)
# THE CONSTRUCTION AUTHORITY.  Block 190 supplies the carrier, the pair cores,
# the monodromy W = K_c^-1 L_2, the core convention and the landed deep pair;
# Block 194 supplies the landed negative-pair failure mode and the fence that
# forbids fitting a boundary curve through a finite census; Block 191 supplies
# the quarter-weighted cell-average assembly; Block 105 supplies the imported
# Hodge; Block 199 is the stack parent.
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_ROBUSTNESS_BOUNDARY_PACKAGE_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HEAVY_METRIC_OPERATOR_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_heavy_metric_operator_completion_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
    ".claude/science/physics-loops/generator-program-20260821/scout_batch1_findings.md",
    ".claude/science/physics-loops/generator-program-20260821/scout_batch2_findings.md",
    ".claude/science/physics-loops/generator-program-20260821/scout_r2_findings.md",
)
# THE TWO INPUTS THIS BLOCK ITSELF LANDS.  Its own note does not exist until it
# lands, and the batch-2 findings file is carried into the repository BY THIS
# COMMIT exactly as Block 199 carried the round-2 findings file.  Both are
# excluded from the readable count and from nothing else.
SELF_SUPPLIED_INPUTS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_ROBUSTNESS_BOUNDARY_PACKAGE_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    ".claude/science/physics-loops/generator-program-20260821/scout_batch2_findings.md",
)

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
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block199-"
              "heavy-metric-operator-completion-20260826")
PARENT_COMMIT = "725269c6057deed9b7ac1f72a315297a9f99f35a"
# The Block 198 tip: a real ancestor of HEAD that predates Block 199 and
# therefore carries NEITHER Block 199 artifact.
STALE_PARENT_COMMIT = "e784ffc1ef94489383b0869f058962ccd2af7f74"
# A real but superseded authority head, carried from Block 199's own record.
STALE_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_window_boundary_curve",
    "claim_edge_located",
    "claim_volume_interval_maximal",
    "claim_all_width_theorem",
    "claim_generic_point_theorem",
    "claim_continuum_limit",
    "claim_readings_licensed",
    "break_carrier_closure",
    "break_deep_width_lock",
    "break_boundary_width_lock",
    "break_twelve_deep_core",
    "break_big_inverse_count",
    "break_edge_endpoint_signs",
    "break_edge_discriminants",
    "break_pole_count",
    "break_zero_crossing",
    "break_normalization_form",
    "break_unimodular_band",
    "break_response_values",
    "break_window_law_zeros",
    "break_sign_flip",
    "break_parity_split",
    "break_volume_positivity",
    "break_volume_margins",
    "break_endpoint_membership",
    "break_outside_samples",
    "drop_n5_fence",
    "break_nsimplify_absence",
    "break_float_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_window_boundary_curve": "B",
    "claim_edge_located": "B",
    "claim_volume_interval_maximal": "B",
    "claim_all_width_theorem": "B",
    "claim_generic_point_theorem": "B",
    "claim_continuum_limit": "B",
    "claim_readings_licensed": "B",
    "break_carrier_closure": "C",
    "break_deep_width_lock": "C",
    "break_boundary_width_lock": "C",
    "break_twelve_deep_core": "C",
    "break_big_inverse_count": "C",
    "break_edge_endpoint_signs": "D",
    "break_edge_discriminants": "D",
    "break_pole_count": "D",
    "break_zero_crossing": "D",
    "break_normalization_form": "D",
    "break_unimodular_band": "D",
    "break_response_values": "E",
    "break_window_law_zeros": "E",
    "break_sign_flip": "E",
    "break_parity_split": "E",
    "break_volume_positivity": "F",
    "break_volume_margins": "F",
    "break_endpoint_membership": "F",
    "break_outside_samples": "F",
    "drop_n5_fence": "G",
    "break_nsimplify_absence": "G",
    "break_float_absence": "G",
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
            # Keep runner stdout within the repository's 6,000-character
            # execution contract.  The full auditable statements remain in
            # build_checks; stdout carries stable keys and verdicts.
            print(f"[{'PASS' if value else 'FAIL'}] {key}")
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
        if path not in SELF_SUPPLIED_INPUTS and not (ROOT / path).is_file())
    expected = len(AUDIT_INPUT_PATHS) - len(SELF_SUPPLIED_INPUTS)
    return expected - len(missing), missing


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
    "BLOCK 190's WRAP-EDGE CONSTRUCTION ON Z_T x Z_4 FOR EVEN T, CARRIED UNCHANGED: the staggered Dirac-Kahler carrier with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H",
    "BLOCK 190's PAIR CORES AND ITS UNIT-CELL MONODROMY, IMPOSED AS THE OBJECT THIS BLOCK MEASURES AND REBUILT HERE RATHER THAN CITED: for a core t0 the eight cells {(t, x) : t in {t0, t0+1}} in t-major order, the shifted pairings L_k[a, b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1, the core Gram K_c = L_0 and the MONODROMY W = K_c^-1 L_2",
    "BLOCK 190's TWO-SITE SPATIAL SHIFT U AS THE SECTOR LABEL, IMPOSED SO THAT HEAVY AND LIGHT ARE DEFINED BY A SYMMETRY AND NOT BY PICKING A FACTOR: U on the eight core cells with U^2 = I, U^T K_c U = K_c and [W, U] = 0, the U = -1 compression carrying the HEAVY quadratic and the U = +1 compression the LIGHT one",
    "THE FIRST-ORDER VOLUME RESPONSE, WHICH IS THIS BLOCK's ONE NEW OBJECT AND IS A DERIVATIVE AND NOT A DIFFERENCE QUOTIENT: for a local anchor (s, x) and its reflected image partner (T-1-s, x) with the image block conjugated by the offset permutation, dH the quarter-weighted assembly of dB = d/d(delta) shear_hodge(c, 1 - delta) at delta = 0, then dQ = m dH + dH D_s - D_s^T dH, dG = -G dQ G, and the response tr(K_c^-1 (dL_2 - dK_c W))",
    "BLOCK 194's LANDED FAILURE-MODE CENSUS AND ITS FENCE, IMPOSED AS THE COMPARISON TARGET AND AS A PROHIBITION: the scale census (1, 0, 1) naming a NEGATIVE real reciprocal pair, the four shear columns c = 3/4, 9/10, 19/20, 99/100 failing in that mode at every one of its twelve searched masses, and its declared fence that a finite set of exact rational points is NOT a boundary curve",
    "BLOCK 190's LANDED DEEP PAIR AND ITS LANDED BOUNDARY VALUE AT (m, c) = (9/20, 5/13), IMPOSED AS THE COMPARISON TARGET AND ALSO REBUILT HERE RATHER THAN ONLY CITED: 22569375 z^2 - 233631106 z + 22569375 with 39529825 z^2 - 109432706 z + 39529825 at the deep cores, and 43033320714375 z^2 - 445467467014578 z + 48554286398375 as the extra near-boundary factor at t0 = 1",
    "THE LANDED BLOCK 105 shear_hodge(c, v) READ THROUGH THE BLOCK 128 MODULE -- THE ONLY OBJECT IMPORTED -- assembled into H by Block 191's quarter-weighted four-corner cell average at Block 190's seam convention, read at the shear 5/13 and at the SEVEN sampled volumes and at the shears of the edge probe",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL NINE ARE FALSE
# AND STAY FALSE.  THE SECOND, THE THIRD AND THE FOURTH ARE THE THREE THIS
# BLOCK'S RESULTS MOST INVITE A READER TO ASSUME.
GRAVITY_SUPPLIED_CLAIMED = False
WINDOW_BOUNDARY_CURVE_CLAIMED = False
EDGE_LOCATED_CLAIMED = False
VOLUME_INTERVAL_MAXIMAL_CLAIMED = False
ALL_WIDTH_THEOREM_CLAIMED = False
GENERIC_POINT_THEOREM_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
DYNAMICS_CLAIMED = False
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
    "R1: that the deep monodromy is width-INDEPENDENT, or that a fourth width proves an all-T theorem.  Measured: FOUR exact widths, at ONE mass and ONE shear, with the deep value agreeing at THREE of them and the T = 12 slot t0 = 3 measured DIFFERENT because it is the seam mirror.  An empirical lock over four widths is not a theorem in T and none is attempted here.  Reading.",
    "R2: that the two classified shear endpoints locate an edge, or that a finite [4/4] fit is the carrier on a continuum.  Measured: TWO exact endpoint classifications and a declared interpolation model matching fourteen exact probes.  The model has one denominator root and no numerator root in the bracket, but no carrier degree bound or symbolic identity is proved.  Between-probe carrier behavior remains open.  Reading.",
    "R3: that the volume samples establish an INTERVAL of positivity.  Measured: SEVEN exact rational volumes at which positivity holds.  Nothing between them is asserted, no edge is located, and the scout's '(1/10, 1]' is corrected here rather than repeated -- it excludes an endpoint it also claims, and positivity holds outside BOTH of its ends.  Reading.",
    "R4: that the first-order response profile is a physical susceptibility, a force or a coupling.  Measured: six exact rational traces of a derivative of a finite rational matrix, with at most two parity-labelled values per slice, distinct on the four nonzero interior slices and equal to zero at the two endpoints.  No energy, no force and no coupling is supplied by any line here.  Reading.",
    "R5: that any of this is a statement about the construction CLASS rather than about this carrier at this mass.  Measured: ONE carrier family, ONE mass 9/20, FOUR widths, ONE structural shear and finitely many exact rational shears and volumes.  Reading.",
)
CHECK_VERDICT = "FINITE-PROBES-CONFIRMED-INTERPOLATION-MODEL-FENCED"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
SPACE_EXTENT = 4
MASS = sp.Rational(9, 20)
STRUCTURAL_SHEAR = sp.Rational(5, 13)
UNIT_VOLUME = sp.Integer(1)
DEEP_CORE = 3
BOUNDARY_CORE = 1

# --- C: THE WIDTH LOCK ------------------------------------------------------
WIDTHS = (12, 16, 20, 24)
CARRIER_SIZES = {12: 48, 16: 64, 20: 80, 24: 96}
GRADE_COMPLEX_RESIDUAL = 0
HODGE_REFLECTION_RESIDUAL = 0
CARRIER_COVARIANCE_RESIDUAL = 0
INVERSE_RESIDUALS = (0, 0)
CORE_GRAM_SYMMETRY_RESIDUAL = 0
# THE NEW WIDTH, AND IT IS THE ONLY HEAVY OBJECT IN THIS RUNNER.
NEW_WIDTH = 24
BIG_INVERSE_SIZE = 96
BIG_INVERSES = 1
LANDED_HEAVY = (22569375, -233631106, 22569375)
LANDED_LIGHT = (39529825, -109432706, 39529825)
LANDED_BOUNDARY_QUADRATIC = (43033320714375, -445467467014578, 48554286398375)
DEEP_CENSUS = ((LANDED_HEAVY, 2), (LANDED_LIGHT, 2))
BOUNDARY_CENSUS = ((LANDED_HEAVY, 1), (LANDED_LIGHT, 2),
                   (LANDED_BOUNDARY_QUADRATIC, 1))
# THE DEEP LOCK IS THREE WIDTHS AND NOT FOUR, AND THAT IS THIS BLOCK'S
# CORRECTION TO THE SCOUT RECORD'S WIDTH LIST.
DEEP_LOCK_WIDTHS = (16, 20, 24)
# AT T = 12 THE SLOT t0 = 3 IS T/2 - 3, THE SEAM MIRROR, AND IT IS DIFFERENT.
MIRROR_WIDTH = 12
MIRROR_QUADRATIC = (48554286398375, -376762652339458, 35686537764375)
MIRROR_CENSUS = ((LANDED_HEAVY, 1), (LANDED_LIGHT, 2), (MIRROR_QUADRATIC, 1))
TWELVE_SLOT_IS_DEEP = False
BOUNDARY_LOCK_WIDTHS = (12, 16, 20, 24)
# The U grading, which is what makes HEAVY and LIGHT definitions and not picks.
U_RESIDUALS = (0, 0, 0)               # U^2 - I, U^T K_c U - K_c, [W, U]
SECTOR_DIM = 4

# --- D: TWO ENDPOINTS AND THE DECLARED INTERPOLATION MODEL -----------------
EDGE_WIDTH_T = 16
EDGE_LOW = sp.Rational(1213333, 1703936)
EDGE_HIGH = sp.Rational(151669, 212992)
EDGE_BRACKET_WIDTH = sp.Rational(19, 1703936)
PASS_HEAVY = (22731666619014252910884,
              -9037516115117032760684071897,
              22731666619014252910884)
PASS_LIGHT = (1965446916440236496410958116,
              -5106576818903321739356333897,
              1965446916440236496410958116)
FAIL_HEAVY = (7068274392254939356,
              2206352658131956553649497,
              7068274392254939356)
FAIL_LIGHT = (479836341843952799153956,
              -1246694110992835465220297,
              479836341843952799153956)
EDGE_MULTIPLICITY = 2
# THE SIGN PATTERN IS THE WHOLE CLASSIFICATION: leading coefficients POSITIVE on
# both sides by primitive normalization, and the LINEAR coefficient flips.
PASS_SIGNS = ((1, -1, 1), (1, -1, 1))     # (heavy, light) leading/linear/constant
FAIL_SIGNS = ((1, 1, 1), (1, -1, 1))
PASS_HEAVY_DISCRIMINANT = 81676697528933149477232145548993051505525203131282532785
PASS_LIGHT_DISCRIMINANT = 10625200481983032893373241731901607723531989031726128785
FAIL_HEAVY_DISCRIMINANT = 4867992051846108338250759415448622431312577574065
FAIL_LIGHT_DISCRIMINANT = 633274546567469442533268055181385192837178968465
PASS_HEAVY_MARGIN = 9037470651783794732178250129
PASS_LIGHT_MARGIN = 1175682986022848746534417665
FAIL_HEAVY_MARGIN = 2206338521583172043770785
FAIL_LIGHT_MARGIN = 287021427304929866912385
# THE DECLARED [4/4] INTERPOLATION MODEL, FIT FROM TEN MEASURED POINTS.
RECONSTRUCTION_POINTS = (sp.Rational(1, 3), sp.Rational(1, 4),
                         sp.Rational(3, 4), sp.Rational(1, 5),
                         sp.Rational(2, 5), sp.Rational(3, 5),
                         sp.Rational(4, 5), sp.Rational(1, 6),
                         sp.Rational(5, 6), sp.Rational(1, 7))
RECONSTRUCTION_NULLITY = 1
NUMERATOR_COEFFS = (1362, 800, -5529, -1600, 5448)      # highest degree first
DENOMINATOR_COEFFS = (400, 800, -1681, -1600, 1600)
NUMERATOR_DENOMINATOR_COPRIME = True
# TWO POINTS HELD OUT OF THE RECONSTRUCTION AND CHECKED AGAINST IT.
WITHHELD_POINTS = (sp.Rational(1, 2), sp.Rational(2, 3))
WITHHELD_VALUES = (sp.Rational(-27607, 2019), sp.Rational(-98418, 2071))
WITHHELD_RESIDUALS = (0, 0)
# EXACT STURM COUNTS FOR THE INTERPOLATION MODEL ON THE TIGHT BRACKET.
DENOMINATOR_ROOTS_IN_BRACKET = 1
NUMERATOR_ROOTS_IN_BRACKET = 0
INTERPOLANT_ZERO_CROSSING = False
DENOMINATOR_AT_LOW = sp.Rational(5682916654753563227721,
                                 526857457489218503704576)
DENOMINATOR_AT_HIGH = sp.Rational(-1767068598063734839,
                                  128627308957328736256)
NUMERATOR_AT_LOW = sp.Rational(9037516115117032760684071897,
                               4214859659913748029636608)
NUMERATOR_AT_HIGH = sp.Rational(2206352658131956553649497,
                                1029018471658629890048)
DENOMINATOR_ENDPOINT_SIGNS = (1, -1)
NUMERATOR_ENDPOINT_SIGNS = (1, 1)
# FINITE PROJECTIVE AGREEMENT: the carrier's heavy quadratic matches the
# interpolation model (D(c), -2 N(c), D(c)) at every listed probe.  This is not
# a symbolic identity and supplies no statement at unprobed shears.
NORMALIZATION_PROBES = (sp.Rational(1, 2), sp.Rational(2, 3),
                        sp.Rational(1, 3), sp.Rational(3, 4),
                        sp.Rational(4, 5), EDGE_LOW, EDGE_HIGH)
NORMALIZATION_MATCHES = 7
INTERPOLANT_LEADING_COEFFICIENT_IS_DENOMINATOR = True
# THE BAND IS EXCLUDED FOR THE INTERPOLATION MODEL on each component of the
# bracket punctured at D = 0.  The model is undefined at its pole.  This does
# not classify the carrier between probes.
BAND_POLYNOMIAL_ROOTS = (0, 0)        # roots of num - 2 den, num + 2 den
BAND_SIGNS_AT_LOW = (-1, -1)
INTERPOLANT_UNIMODULAR_CROSSING = False
# THE LANDED FAILURE MODE, CROSS-MEASURED AT A NEW POINT.  Block 194's twelve
# searched masses do NOT include 9/20, so this is an EXTENSION of its c = 3/4
# column and not a re-measurement of one of its points.
B194_CROSS_SHEAR = sp.Rational(3, 4)
B194_CROSS_HEAVY = (5216, 244017, 5216)
B194_CROSS_IS_NEGATIVE_PAIR = True
B194_NEGATIVE_PAIR_CENSUS = (1, 0, 1)
B194_FAILING_COLUMNS = (sp.Rational(3, 4), sp.Rational(9, 10),
                        sp.Rational(19, 20), sp.Rational(99, 100))
B194_SEARCHED_MASSES = 12
B194_MASSES_INCLUDE_FIXTURE = False

# --- E: THE RESPONSE PROFILE ------------------------------------------------
RESPONSE_WIDTH_T = 16
RESPONSE_WINDOW = (3, 5)
RESPONSE_SLICES = (1, 2, 3, 4, 5, 6)
# THE SIX VALUES THE SCOUT QUOTED, WHICH ARE FULL-SLICE-CELL SUMS AND NOT
# SINGLE-CELL RESPONSES.  That correction is this block's, carried as content.
SLICE_RESPONSES = {
    1: sp.Integer(0),
    2: sp.Rational(-3924317879963744, 17744088856432749),
    3: sp.Rational(-285033126329023712, 147867407136939575),
    4: sp.Rational(-73354817263464195597509202636832,
                   5276875808912607540299962640625),
    5: sp.Rational(38264746670503590368, 3696685178423489375),
    6: sp.Integer(0),
}
# THE PARITY PATTERN: at most two values per slice, one for x in {0, 2} and one
# for x in {1, 3}.  They are distinct on s = 2,3,4,5 and coincide at zero on
# s = 1,6.  A single (s, x) cell does NOT give the quoted slice sum.
PARITY_RESPONSES = {
    1: (sp.Integer(0), sp.Integer(0)),
    2: (sp.Rational(-20900678024945648, 88720444282163745),
        sp.Rational(3696627775012096, 29573481427387915)),
    3: (sp.Rational(149518897051870024, 147867407136939575),
        sp.Rational(-58407092043276376, 29573481427387915)),
    4: (sp.Rational(-8956827997451709214445818024208,
                    5276875808912607540299962640625),
        sp.Rational(-9240193544760129528102927764736,
                    1758958602970869180099987546875)),
    5: (sp.Rational(907245269067878860293432, 222484997463417708034375),
        sp.Rational(244236620114250432855608, 222484997463417708034375)),
    6: (sp.Integer(0), sp.Integer(0)),
}
PARITY_PATTERN_HOLDS = True
INTERIOR_PARITY_VALUES_DISTINCT = True
PER_SINGLE_CELL_WORDING_CORRECT = False
# THE WINDOW LAW, AND IT HOLDS PER ANCHOR AND NOT ONLY AFTER SUMMING.
WINDOW_ZERO_SLICES = (1, 6)
WINDOW_ZEROS_PER_ANCHOR = True
# THE SIGN FLIP, AND IT SURVIVES BEFORE SUMMATION TOO.
SIGN_FLIP_SLICES = (4, 5)
SIGN_FLIP_SIGNS = (-1, 1)
SIGN_FLIP_PER_ANCHOR = True
DERIVATIVE_BLOCK = ((-1, 0, 0, 0),
                    (0, sp.Rational(-169, 144), sp.Rational(65, 144), 0),
                    (0, sp.Rational(65, 144), sp.Rational(-169, 144), 0),
                    (0, 0, 0, 1))

# --- F: THE VOLUME SAMPLES --------------------------------------------------
VOLUME_WIDTH_T = 16
SAMPLED_VOLUMES = (sp.Rational(1, 100), sp.Rational(1, 10), sp.Rational(1, 5),
                   sp.Rational(2, 5), sp.Rational(3, 5), sp.Rational(4, 5),
                   sp.Rational(6, 5))
# Each entry is the pair of PRIMITIVE integer factors, each of multiplicity two.
VOLUME_FACTORS = {
    sp.Rational(1, 100): ((207461386358175, -1412992189424194, 207461386358175),
                          (207498839574625, -583071737558594, 207498839574625)),
    sp.Rational(1, 10): ((21760118175, -150049193794, 21760118175),
                         (22147734625, -62233488194, 22147734625)),
    sp.Rational(1, 5): ((9229575, -65883826, 9229575),
                        (9861625, -27701426, 9861625)),
    sp.Rational(2, 5): ((154718175, -1228109794, 154718175),
                        (191334625, -536004194, 191334625)),
    sp.Rational(3, 5): ((964625, -2690274, 964625),
                        (6057575, -53690866, 6057575)),
    sp.Rational(4, 5): ((31260675, -302948719, 31260675),
                        (50327125, -139773119, 50327125)),
    sp.Rational(6, 5): ((3801625, -10499666, 3801625),
                        (6132725, -66574198, 6132725)),
}
VOLUME_MULTIPLICITY = 2
VOLUME_MARGINS = {
    sp.Rational(1, 100): (998069416707844, 168074058409344),
    sp.Rational(1, 10): (106528957444, 17938018944),
    sp.Rational(1, 5): (47424676, 7978176),
    sp.Rational(2, 5): (918673444, 153334944),
    sp.Rational(3, 5): (761024, 41575716),
    sp.Rational(4, 5): (240427369, 39118869),
    sp.Rational(6, 5): (2896416, 54308748),
}
VOLUME_DISCRIMINANTS = {
    sp.Rational(1, 100): (1824386020055153498463715227136,
                          167749577440334068823807694336),
    sp.Rational(1, 10): (20620749586269506791936, 1910918456715041819136),
    sp.Rational(1, 5): (3999938309675776, 378362411870976),
    sp.Rational(2, 5): (1412502811417399936, 140864741090027136),
    sp.Rational(3, 5): (3515568632576, 2735932232307456),
    sp.Rational(4, 5): (87869007137918461, 9405246751925661),
    sp.Rational(6, 5): (52433575549056, 4281682575640704),
}
VOLUMES_ALL_POSITIVE = True
# THE TWO CORRECTIONS TO THE SCOUT'S INTERVAL NOTATION, AS CONSTANTS.
CLAIMED_INTERVAL_LOW = sp.Rational(1, 10)
ENDPOINT_IN_CONFIRMED_SET = True          # v = 1/10 IS confirmed positive
OUTSIDE_SAMPLES = (sp.Rational(1, 100), sp.Rational(6, 5))
OUTSIDE_SAMPLES_POSITIVE = True
VOLUME_EDGES_LOCATED = False

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  This block's content is a set of EXACT SIGN and EXACT ROOT-COUNT
# statements -- a Sturm count of 1 against a Sturm count of 0, a linear
# coefficient that flips sign, six exact rational traces two of which are ZERO
# and a parity split that is an exact equality between anchors.  A single such
# call could manufacture a false model numerator zero, collapse a window
# zero that is the content, or merge the two parity values into one.  Every
# mass, shear and volume here is ALREADY an exact sympy Rational.  Gate G counts
# the occurrences in this file's own source and requires ZERO.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("

# AND A SECOND HAZARD, FOUND IN THIS BLOCK'S OWN DRAFTING AND GATED HERE RATHER
# THAN ONLY AVOIDED.  The imported Block 105 shear_hodge(c, v) forms 1/v with
# PYTHON division, so a plain int argument -- shear_hodge(c, 1) -- returns a
# sympy FLOAT in its last corner while shear_hodge(c, sp.Integer(1)) returns an
# exact Rational.  The two matrices compare EQUAL and give the same factorization
# at this fixture, so the contamination is silent, but it destroys the exact
# two-sided inverse residual: 0 becomes 3459 nonzero entries at T = 16.  Every
# volume passed by this runner is an exact sympy Rational, and gate G MEASURES
# the absence of any Float in every carrier matrix it builds.
FLOAT_HAZARD_RESIDUAL = 3459
FLOAT_CALLS = 0


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def float_entries(matrix: sp.MatrixBase) -> int:
    """MEASURED, NOT PROMISED: how many entries of a matrix are sympy Floats.
    A single one silently voids every exact residual computed from it."""
    return sum(1 for entry in sp.Matrix(matrix) if entry.is_Float)


def rational_matrix(matrix: sp.MatrixBase) -> DomainMatrix:
    """THE EXACT RATIONAL DOMAIN, AND IT IS NOT A NUMERICAL METHOD.  Every entry
    of every matrix passed here is a sympy Rational, so the matrix lies in
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


def primitive_from_values(values) -> tuple:
    """The same primitive normalization applied to a bare coefficient tuple."""
    rationals = [sp.Rational(value) for value in values]
    multiplier = 1
    for value in rationals:
        multiplier = sp.ilcm(multiplier, value.q)
    integers = [sp.Integer(value * multiplier) for value in rationals]
    content = 0
    for value in integers:
        content = sp.igcd(content, int(value))
    integers = [value // content for value in integers]
    if integers[0] < 0:
        integers = [-value for value in integers]
    return tuple(int(value) for value in integers)


Z = sp.Symbol("z")
C = sp.Symbol("c")


def factor_census(matrix: sp.MatrixBase) -> tuple:
    """The primitive integer factors of charpoly(M) with their multiplicities,
    sorted by degree then by leading coefficient -- PROJECTIVE data, so the
    monic normalization SymPy applies cannot move it."""
    census = []
    for factor, multiplicity in sp.factor_list(
            sp.expand(matrix.charpoly(Z).as_expr()))[1]:
        if not factor.has(Z):                          # pragma: no cover
            continue
        census.append((primitive_tuple(factor, Z), int(multiplicity)))
    return tuple(sorted(census, key=lambda item: (len(item[0]), item[0])))


# ---------------------------------------------------------------------------
# THE CARRIER, REBUILT FROM FORMULAS.  Everything except the shear block is
# built here; the shear block is the ONE import.
# ---------------------------------------------------------------------------
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])
CORNERS = ((0, 0), (0, 1), (1, 0), (1, 1))


def site_index(width: int, time: int, space: int) -> int:
    return (time % width) * SPACE_EXTENT + space % SPACE_EXTENT


def site_theta(width: int, time: int) -> int:
    """theta_s(t) = -t, fixing the slices {0, T/2}."""
    return (-time) % width


def staggered_kernel(width: int) -> sp.Matrix:
    """eta_t = 1, eta_x = (-1)^t, and the temporal sign w = -1 ON THE WRAP EDGE
    t = T-1 -- Block 190's convention."""
    size = width * SPACE_EXTENT
    kernel = sp.zeros(size, size)
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
                     for time in range(width)
                     for space in range(SPACE_EXTENT)])


def raising_part(width: int, kernel: sp.Matrix) -> sp.Matrix:
    """d_K = P1 K P0 + P2 K P1."""
    p0, p1, p2 = (grade_projector(width, g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def reflection_permutation(width: int) -> sp.Matrix:
    size = width * SPACE_EXTENT
    matrix = sp.zeros(size, size)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            matrix[site_index(width, site_theta(width, time), space),
                   site_index(width, time, space)] = 1
    return matrix


def site_restricted_raising(width: int, raising: sp.Matrix) -> sp.Matrix:
    """A_s: the d_K entries inside the CLOSED half {0..T/2}, with the two fixed
    slices' own spatial edges removed."""
    size = width * SPACE_EXTENT
    half = width // 2
    closed, fixed = set(range(half + 1)), {0, half}
    matrix = sp.zeros(size, size)
    for row in range(size):
        for column in range(size):
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
    for column, (delta_t, delta_x) in enumerate(CORNERS):
        matrix[site_index(width, time + delta_t, space + delta_x), column] = 1
    return matrix


def exact_scalar(value):
    """THE FLOAT GUARD, AND IT IS THE WHOLE POINT OF THIS FUNCTION.  A plain
    Python int reaching the import makes 1/v a FLOAT; sp.Rational of it does
    not.  A SYMBOLIC volume -- used only for the exact volume derivative -- is
    passed through unchanged, because it carries no float either.  This is NOT
    nsimplify: no tolerance exists here and nothing inexact is ever accepted."""
    if isinstance(value, sp.Basic):
        return value if value.free_symbols else sp.Rational(value)
    return sp.Rational(value)


def imported_shear_block(shear, volume) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT: the LANDED Block 105 shear_hodge(c, v) =
    diag(v, v g(c)^-1, 1/v) with g(c) = [[1, c], [c, 1]].  BOTH ARGUMENTS ARE
    EXACT AND THAT IS LOAD-BEARING, not stylistic: the import forms 1/v by
    Python division, so a plain int argument returns a FLOAT corner.
    NO nsimplify is used and gate G measures that no Float survives."""
    return sp.expand(sp.Matrix(b128.block105.shear_hodge(
        exact_scalar(shear), exact_scalar(volume))))


def site_hodge(width: int, block: sp.Matrix) -> sp.Matrix:
    """THE QUARTER-WEIGHTED FOUR-CORNER CELL AVERAGE, Block 191's assembly rule
    at Block 190's seam convention: block B on t < T/2 and P_4 B P_4^T beyond.
    The cell contributions are SCATTERED directly, which is entry for entry the
    same arithmetic as summing e B e^T / 4 over the cell embeddings."""
    half = width // 2
    reflected = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    result = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    quarter = sp.Rational(1, 4)
    for time in range(width):
        chosen = block if time < half else reflected
        for space in range(SPACE_EXTENT):
            where = [site_index(width, time + dt, space + dx)
                     for (dt, dx) in CORNERS]
            for i in range(4):
                row = where[i]
                for j in range(4):
                    value = chosen[i, j]
                    if value != 0:
                        result[row, where[j]] += value * quarter
    return sp.expand(result)


def completion(mass: sp.Rational, hodge: sp.Matrix,
               glue: sp.Matrix) -> sp.Matrix:
    """Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    return sp.expand(mass * hodge + hodge * glue - glue.T * hodge)


# ---------------------------------------------------------------------------
# THE HEAVY WORK, DONE ONCE PER (WIDTH, SHEAR, VOLUME) AND SHARED.  The glue is
# shear- and volume-independent and is cached per width; the ONE 96 x 96 inverse
# at T = 24 is the only heavy object here and NOTHING recomputes it.
# ---------------------------------------------------------------------------
_GLUE_CACHE: dict = {}
_CARRIER_CACHE: dict = {}
_BIG_INVERSES: list = []


def glue(width: int) -> dict:
    if width in _GLUE_CACHE:
        return _GLUE_CACHE[width]
    kernel = staggered_kernel(width)
    raising = raising_part(width, kernel)
    reflection = reflection_permutation(width)
    restricted = site_restricted_raising(width, raising)
    record = {
        "glue": sp.expand(restricted - reflection * restricted * reflection),
        "reflection": reflection,
        "grade_complex": residual_count(raising * raising),
    }
    _GLUE_CACHE[width] = record
    return record


def carrier(width: int, shear: sp.Rational, volume: sp.Rational,
            controls: bool = False) -> dict:
    key = (width, shear, volume)
    if key in _CARRIER_CACHE:
        return _CARRIER_CACHE[key]
    frame = glue(width)
    size = width * SPACE_EXTENT
    block = imported_shear_block(shear, volume)
    hodge = site_hodge(width, block)
    action = completion(MASS, hodge, frame["glue"])
    domain = rational_matrix(action)
    rank = domain.rank()
    started_ns = time.monotonic_ns()
    inverse = domain.inv().to_Matrix() if rank == size else None
    seconds = (time.monotonic_ns() - started_ns) / 1000000000
    if size >= BIG_INVERSE_SIZE:
        _BIG_INVERSES.append(key)
    record = {
        "width": width, "shear": shear, "volume": volume, "size": size,
        "glue": frame["glue"], "reflection": frame["reflection"],
        "block": block, "hodge": hodge, "action": action,
        "rank": rank, "inverse": inverse, "inverse_seconds": seconds,
        "grade_complex": frame["grade_complex"],
        "floats": (float_entries(block) + float_entries(hodge)
                   + float_entries(action)
                   + (float_entries(inverse) if inverse is not None else 0)),
    }
    if controls:
        record["hodge_reflection"] = residual_count(
            frame["reflection"] * hodge * frame["reflection"] - hodge)
        record["covariance"] = residual_count(
            frame["reflection"] * action * frame["reflection"] - action.T)
        record["inverse_residuals"] = (
            (residual_count(action * inverse - sp.eye(size)),
             residual_count(inverse * action - sp.eye(size)))
            if inverse is not None else (-1, -1))      # pragma: no cover
    _CARRIER_CACHE[key] = record
    return record


def core_cells(core: int) -> tuple:
    """THE PAIR CORE {(t, x) : t in {t0, t0+1}} in t-major order."""
    return tuple((time, space) for time in (core, core + 1)
                 for space in range(SPACE_EXTENT))


def shifted_pairing(width: int, inverse: sp.Matrix, core: int,
                    step: int) -> sp.Matrix:
    """L_k[a, b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)]; k = 0 is the core
    Gram K_c itself.  THE INDEX ORDER IS t-MAJOR."""
    cells = core_cells(core)
    matrix = sp.zeros(len(cells), len(cells))
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(width, site_theta(width, row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(width, column_time + step, column_space), partner]
    return sp.expand(matrix)


def monodromy(width: int, inverse: sp.Matrix, core: int) -> tuple:
    """W = K_c^-1 L_2, Block 190's unit-cell monodromy, rebuilt."""
    gram = shifted_pairing(width, inverse, core, 0)
    two_step = shifted_pairing(width, inverse, core, 2)
    return sp.expand(exact_inverse(gram) * two_step), gram, two_step


def core_shift(core: int, amount: int) -> sp.Matrix:
    """U at amount 2 is the two-site spatial shift on the eight core cells."""
    cells = core_cells(core)
    position = {cell: index for index, cell in enumerate(cells)}
    matrix = sp.zeros(len(cells), len(cells))
    for index, (time, space) in enumerate(cells):
        matrix[position[time, (space + amount) % SPACE_EXTENT], index] = 1
    return matrix


def sector_compression(operator: sp.Matrix, involution: sp.Matrix,
                       sign: int) -> sp.Matrix:
    """The compression of W to the U = sign eigenspace, which is what DEFINES
    heavy and light here rather than picking a factor out of a list."""
    basis = sp.Matrix.hstack(
        *(involution - sign * sp.eye(involution.rows)).nullspace())
    projector = sp.expand(exact_inverse(basis.T * basis) * basis.T)
    return sp.expand(projector * operator * basis)


# ---------------------------------------------------------------------------
# THE MEASUREMENT PASS.  Every number this runner reports is produced here, once
# and before any mutation flag is read, and the heavy inverses are shared.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class WidthFacts:
    width: int
    size: int
    rank: int
    grade_complex: int
    hodge_reflection: int
    covariance: int
    inverse_residuals: tuple
    inverse_seconds: float
    floats: int
    deep_census: tuple
    boundary_census: tuple
    deep_gram_symmetry: int
    boundary_gram_symmetry: int
    u_residuals: tuple
    heavy_sector: tuple
    light_sector: tuple


def measure_width(width: int) -> WidthFacts:
    record = carrier(width, STRUCTURAL_SHEAR, UNIT_VOLUME, controls=True)
    inverse = record["inverse"]
    deep, deep_gram, _ = monodromy(width, inverse, DEEP_CORE)
    boundary, boundary_gram, _ = monodromy(width, inverse, BOUNDARY_CORE)
    shift = core_shift(DEEP_CORE, 2)
    u_residuals = (
        residual_count(shift * shift - sp.eye(8)),
        residual_count(shift.T * deep_gram * shift - deep_gram),
        residual_count(deep * shift - shift * deep))
    return WidthFacts(
        width=width, size=record["size"], rank=record["rank"],
        grade_complex=record["grade_complex"],
        hodge_reflection=record["hodge_reflection"],
        covariance=record["covariance"],
        inverse_residuals=record["inverse_residuals"],
        inverse_seconds=record["inverse_seconds"],
        floats=record["floats"],
        deep_census=factor_census(deep),
        boundary_census=factor_census(boundary),
        deep_gram_symmetry=residual_count(deep_gram - deep_gram.T),
        boundary_gram_symmetry=residual_count(
            boundary_gram - boundary_gram.T),
        u_residuals=u_residuals,
        heavy_sector=factor_census(sector_compression(deep, shift, -1)),
        light_sector=factor_census(sector_compression(deep, shift, 1)))


def sector_quadratics(width: int, shear: sp.Rational,
                      core: int = DEEP_CORE) -> tuple:
    """The HEAVY and LIGHT primitive quadratics at a shear, each identified by
    the U eigenvalue and not by position in a factor list."""
    record = carrier(width, shear, UNIT_VOLUME)
    operator, _, _ = monodromy(width, record["inverse"], core)
    shift = core_shift(core, 2)
    out = []
    for sign in (-1, 1):
        census = factor_census(sector_compression(operator, shift, sign))
        out.append(census[0])
    return tuple(out)


@dataclass(frozen=True)
class EdgeFacts:
    bracket: tuple
    bracket_width: sp.Expr
    pass_heavy: tuple
    pass_light: tuple
    fail_heavy: tuple
    fail_light: tuple
    multiplicities: tuple
    pass_signs: tuple
    fail_signs: tuple
    pass_discriminants: tuple
    fail_discriminants: tuple
    pass_margins: tuple
    fail_margins: tuple
    palindromic: tuple
    reconstruction_nullity: int
    numerator: tuple
    denominator: tuple
    coprime: bool
    withheld_values: tuple
    withheld_residuals: tuple
    denominator_roots: int
    numerator_roots: int
    denominator_endpoints: tuple
    numerator_endpoints: tuple
    denominator_signs: tuple
    numerator_signs: tuple
    normalization_matches: int
    band_roots: tuple
    band_signs: tuple
    cross_heavy: tuple
    cross_is_negative_pair: bool


def _quad_facts(triple: tuple) -> tuple:
    a, b, c = (sp.Integer(v) for v in triple)
    return (b * b - 4 * a * c, abs(b) - 2 * a, a == c,
            (int(sp.sign(a)), int(sp.sign(b)), int(sp.sign(c))))


def measure_edge() -> EdgeFacts:
    low_heavy, low_light = sector_quadratics(EDGE_WIDTH_T, EDGE_LOW)
    high_heavy, high_light = sector_quadratics(EDGE_WIDTH_T, EDGE_HIGH)
    pass_h, pass_l = _quad_facts(low_heavy[0]), _quad_facts(low_light[0])
    fail_h, fail_l = _quad_facts(high_heavy[0]), _quad_facts(high_light[0])

    # THE DECLARED [4/4] INTERPOLATION MODEL from TEN measured points.  beta_H
    # = b/a is invariant under primitive scaling.  This fit is not treated as a
    # carrier identity without an independently proved degree bound.
    beta = {}
    for shear in RECONSTRUCTION_POINTS + WITHHELD_POINTS:
        heavy, _ = sector_quadratics(EDGE_WIDTH_T, shear)
        beta[shear] = sp.Rational(heavy[0][1], heavy[0][0])
    numerator_symbols = sp.symbols("n0:5")
    denominator_symbols = sp.symbols("d0:5")
    equations = []
    for shear in RECONSTRUCTION_POINTS:
        num = sum(numerator_symbols[i] * shear ** i for i in range(5))
        den = sum(denominator_symbols[i] * shear ** i for i in range(5))
        equations.append(sp.expand(beta[shear] * den - num))
    coefficients, _ = sp.linear_eq_to_matrix(
        equations, list(numerator_symbols) + list(denominator_symbols))
    nullspace = coefficients.nullspace()
    solution = nullspace[0]
    raw_num = sp.expand(sum(solution[i] * C ** i for i in range(5)))
    raw_den = sp.expand(sum(solution[5 + i] * C ** i for i in range(5)))
    # beta_H = raw_num / raw_den; the block DISPLAYS it as -2 N / D with N, D the
    # primitive integer polynomials, so both are normalized here.
    numerator = primitive_tuple(-raw_num / 2, C)
    denominator = primitive_tuple(raw_den, C)
    num_poly = sp.Poly(list(numerator), C)
    den_poly = sp.Poly(list(denominator), C)
    coprime = sp.gcd(num_poly, den_poly).as_expr() == 1
    beta_formula = sp.cancel(-2 * num_poly.as_expr() / den_poly.as_expr())
    withheld = tuple(sp.together(beta_formula.subs(C, p)) for p in WITHHELD_POINTS)
    residuals = tuple(
        0 if sp.simplify(withheld[i] - beta[p]) == 0 else 1
        for i, p in enumerate(WITHHELD_POINTS))

    # THE MODEL'S STURM COUNTS: one denominator root and no numerator root
    # inside the tight bracket.  These counts classify the interpolant only.
    den_roots = int(sp.count_roots(den_poly, EDGE_LOW, EDGE_HIGH))
    num_roots = int(sp.count_roots(num_poly, EDGE_LOW, EDGE_HIGH))
    den_at = (den_poly.eval(EDGE_LOW), den_poly.eval(EDGE_HIGH))
    num_at = (num_poly.eval(EDGE_LOW), num_poly.eval(EDGE_HIGH))

    # FINITE PROJECTIVE AGREEMENT between carrier probes and the model.
    matches = 0
    for shear in NORMALIZATION_PROBES:
        heavy, _ = sector_quadratics(EDGE_WIDTH_T, shear)
        predicted = primitive_from_values(
            (den_poly.eval(shear), -2 * num_poly.eval(shear),
             den_poly.eval(shear)))
        if predicted == heavy[0]:
            matches += 1

    # THE MODEL'S BAND POLYNOMIALS.  Their root counts imply |beta_H| > 2 on
    # each component of the bracket punctured at D = 0, for the model only.
    band_polys = (sp.Poly(sp.expand(-2 * num_poly.as_expr()
                                    - 2 * den_poly.as_expr()), C),
                  sp.Poly(sp.expand(-2 * num_poly.as_expr()
                                    + 2 * den_poly.as_expr()), C))
    band_roots = tuple(int(sp.count_roots(p, EDGE_LOW, EDGE_HIGH))
                       for p in band_polys)
    band_signs = tuple(int(sp.sign(p.eval(EDGE_LOW))) for p in band_polys)

    cross_heavy, _ = sector_quadratics(EDGE_WIDTH_T, B194_CROSS_SHEAR)
    cross = cross_heavy[0]
    return EdgeFacts(
        bracket=(EDGE_LOW, EDGE_HIGH), bracket_width=EDGE_HIGH - EDGE_LOW,
        pass_heavy=low_heavy[0], pass_light=low_light[0],
        fail_heavy=high_heavy[0], fail_light=high_light[0],
        multiplicities=(low_heavy[1], low_light[1],
                        high_heavy[1], high_light[1]),
        pass_signs=(pass_h[3], pass_l[3]), fail_signs=(fail_h[3], fail_l[3]),
        pass_discriminants=(pass_h[0], pass_l[0]),
        fail_discriminants=(fail_h[0], fail_l[0]),
        pass_margins=(pass_h[1], pass_l[1]),
        fail_margins=(fail_h[1], fail_l[1]),
        palindromic=(pass_h[2], pass_l[2], fail_h[2], fail_l[2]),
        reconstruction_nullity=len(nullspace),
        numerator=numerator, denominator=denominator, coprime=coprime,
        withheld_values=withheld, withheld_residuals=residuals,
        denominator_roots=den_roots, numerator_roots=num_roots,
        denominator_endpoints=den_at, numerator_endpoints=num_at,
        denominator_signs=tuple(int(sp.sign(v)) for v in den_at),
        numerator_signs=tuple(int(sp.sign(v)) for v in num_at),
        normalization_matches=matches,
        band_roots=band_roots, band_signs=band_signs,
        cross_heavy=cross,
        cross_is_negative_pair=bool(
            cross[0] > 0 and cross[1] > 0 and cross[2] > 0
            and cross[1] * cross[1] - 4 * cross[0] * cross[2] > 0))


@dataclass(frozen=True)
class ResponseFacts:
    derivative_block: tuple
    anchors: dict
    parity: dict
    slices: dict
    parity_pattern: bool
    interior_parity_distinct: bool
    window_zeros_per_anchor: bool
    sign_flip_signs: tuple
    sign_flip_per_anchor: bool


def measure_response() -> ResponseFacts:
    width = RESPONSE_WIDTH_T
    record = carrier(width, STRUCTURAL_SHEAR, UNIT_VOLUME)
    inverse, glue_matrix = record["inverse"], record["glue"]
    operator, gram, _ = monodromy(width, inverse, DEEP_CORE)
    gram_inverse = exact_inverse(gram)
    delta = sp.Symbol("delta")
    block = sp.Matrix(imported_shear_block(STRUCTURAL_SHEAR, 1 - delta))
    derivative = sp.expand(
        block.applyfunc(lambda entry: sp.diff(entry, delta)).subs(delta, 0))
    reflected = sp.expand(
        OFFSET_PERMUTATION * derivative * OFFSET_PERMUTATION.T)

    # ONLY the entries of dG that the two pairings read are formed: the pairing
    # touches eight partner COLUMNS and eight shifted ROWS per step, so a
    # 16 x 8 slice of -G dQ G suffices and no 64 x 64 product is ever built.
    cells = core_cells(DEEP_CORE)
    columns = [site_index(width, site_theta(width, t), x) for (t, x) in cells]
    rows = {k: [site_index(width, t + k, x) for (t, x) in cells] for k in (0, 2)}
    needed = sorted(set(rows[0]) | set(rows[2]))
    left = inverse[needed, :]
    right = inverse[:, columns]
    where = {row: index for index, row in enumerate(needed)}

    def response(anchor_time: int, anchor_space: int) -> sp.Expr:
        here = cell_embedding(width, anchor_time, anchor_space)
        image = cell_embedding(width, width - 1 - anchor_time, anchor_space)
        d_hodge = sp.expand(
            (here * derivative * here.T + image * reflected * image.T) / 4)
        d_action = sp.expand(MASS * d_hodge + d_hodge * glue_matrix
                             - glue_matrix.T * d_hodge)
        slice_block = sp.expand(-(left * d_action) * right)
        pairings = {}
        for step in (0, 2):
            matrix = sp.zeros(8, 8)
            for a in range(8):
                for b in range(8):
                    matrix[a, b] = slice_block[where[rows[step][b]], a]
            pairings[step] = matrix
        return sp.expand(sp.trace(
            gram_inverse * (pairings[2] - pairings[0] * operator)))

    anchors, parity, slices = {}, {}, {}
    pattern = True
    for s in RESPONSE_SLICES:
        values = tuple(response(s, x) for x in range(SPACE_EXTENT))
        anchors[s] = values
        pattern = pattern and values[0] == values[2] and values[1] == values[3]
        parity[s] = (values[0], values[1])
        slices[s] = sp.together(sum(values))
    zeros = all(all(v == 0 for v in anchors[s]) for s in WINDOW_ZERO_SLICES)
    interior_distinct = all(
        parity[s][0] != parity[s][1]
        and parity[s][0] != slices[s]
        and parity[s][1] != slices[s]
        for s in (2, 3, 4, 5))
    flip = tuple(int(sp.sign(slices[s])) for s in SIGN_FLIP_SLICES)
    per_anchor_flip = (all(v < 0 for v in anchors[SIGN_FLIP_SLICES[0]])
                       and all(v > 0 for v in anchors[SIGN_FLIP_SLICES[1]]))
    return ResponseFacts(
        derivative_block=tuple(tuple(derivative.row(i)) for i in range(4)),
        anchors=anchors, parity=parity, slices=slices,
        parity_pattern=pattern, interior_parity_distinct=interior_distinct,
        window_zeros_per_anchor=zeros,
        sign_flip_signs=flip, sign_flip_per_anchor=per_anchor_flip)


@dataclass(frozen=True)
class VolumeFacts:
    factors: dict
    margins: dict
    discriminants: dict
    multiplicities: dict
    palindromic: dict
    distinct: dict
    positive: bool


def measure_volumes() -> VolumeFacts:
    factors, margins, discriminants = {}, {}, {}
    multiplicities, palindromic, distinct = {}, {}, {}
    positive = True
    for volume in SAMPLED_VOLUMES:
        record = carrier(VOLUME_WIDTH_T, STRUCTURAL_SHEAR, volume)
        operator, _, _ = monodromy(VOLUME_WIDTH_T, record["inverse"], DEEP_CORE)
        census = factor_census(operator)
        triples = tuple(item[0] for item in census)
        factors[volume] = triples
        multiplicities[volume] = tuple(item[1] for item in census)
        facts = tuple(_quad_facts(t) for t in triples)
        discriminants[volume] = tuple(f[0] for f in facts)
        margins[volume] = tuple(f[1] for f in facts)
        palindromic[volume] = tuple(f[2] for f in facts)
        distinct[volume] = len(set(triples)) == len(triples)
        positive = positive and len(triples) == 2 and distinct[volume] and all(
            t[0] > 0 and f[0] > 0 and f[1] > 0 and f[2]
            for t, f in zip(triples, facts))
    return VolumeFacts(
        factors=factors, margins=margins, discriminants=discriminants,
        multiplicities=multiplicities, palindromic=palindromic,
        distinct=distinct, positive=positive)


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
    widths: dict
    edge: EdgeFacts
    response: ResponseFacts
    volumes: VolumeFacts
    big_inverses: int
    big_inverse_size: int
    carrier_floats: int
    nsimplify_calls: int


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    authority = authority_certificate(main_head)
    note_text = NOTE_PATH.read_text(encoding="utf-8") \
        if NOTE_PATH.is_file() else ""
    widths = {width: measure_width(width) for width in WIDTHS}
    edge = measure_edge()
    response = measure_response()
    volumes = measure_volumes()
    return Facts(
        main_head=main_head,
        authority=authority,
        scope=scope_certificate(note_text),
        imposed=len(IMPOSED_OBJECTS),
        registered=len(REGISTERED_OBJECTS),
        adopted=len(ADOPTED_OBJECTS),
        unsupplied=len(UNSUPPLIED_GRAVITY_STRUCTURES),
        readings=len(READINGS),
        widths=widths, edge=edge, response=response, volumes=volumes,
        big_inverses=len(_BIG_INVERSES),
        big_inverse_size=BIG_INVERSE_SIZE,
        carrier_floats=sum(record["floats"]
                           for record in _CARRIER_CACHE.values()),
        nsimplify_calls=nsimplify_occurrences())


# ---------------------------------------------------------------------------
# THE CLAIMS, and the thirty-three mutations that each rewrite exactly one
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
        "window_boundary_curve": WINDOW_BOUNDARY_CURVE_CLAIMED,
        "edge_located": EDGE_LOCATED_CLAIMED,
        "volume_interval_maximal": VOLUME_INTERVAL_MAXIMAL_CLAIMED,
        "all_width_theorem": ALL_WIDTH_THEOREM_CLAIMED,
        "generic_point_theorem": GENERIC_POINT_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "dynamics": DYNAMICS_CLAIMED,
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C -- the width lock.
        "sizes": CARRIER_SIZES,
        "ranks": {w: CARRIER_SIZES[w] for w in WIDTHS},
        "grade_complex": GRADE_COMPLEX_RESIDUAL,
        "hodge_reflection": HODGE_REFLECTION_RESIDUAL,
        "covariance": CARRIER_COVARIANCE_RESIDUAL,
        "inverse_residuals": INVERSE_RESIDUALS,
        "gram_symmetry": CORE_GRAM_SYMMETRY_RESIDUAL,
        "deep_lock_widths": DEEP_LOCK_WIDTHS,
        "deep_census": DEEP_CENSUS,
        "boundary_lock_widths": BOUNDARY_LOCK_WIDTHS,
        "boundary_census": BOUNDARY_CENSUS,
        "mirror_census": MIRROR_CENSUS,
        "twelve_slot_is_deep": TWELVE_SLOT_IS_DEEP,
        "u_residuals": U_RESIDUALS,
        "heavy_sector": ((LANDED_HEAVY, 2),),
        "light_sector": ((LANDED_LIGHT, 2),),
        "big_inverses": BIG_INVERSES,
        # D -- the positivity edge.
        "bracket_width": EDGE_BRACKET_WIDTH,
        "pass_heavy": PASS_HEAVY,
        "pass_light": PASS_LIGHT,
        "fail_heavy": FAIL_HEAVY,
        "fail_light": FAIL_LIGHT,
        "multiplicities": (EDGE_MULTIPLICITY,) * 4,
        "pass_signs": PASS_SIGNS,
        "fail_signs": FAIL_SIGNS,
        "pass_discriminants": (PASS_HEAVY_DISCRIMINANT,
                               PASS_LIGHT_DISCRIMINANT),
        "fail_discriminants": (FAIL_HEAVY_DISCRIMINANT,
                               FAIL_LIGHT_DISCRIMINANT),
        "pass_margins": (PASS_HEAVY_MARGIN, PASS_LIGHT_MARGIN),
        "fail_margins": (FAIL_HEAVY_MARGIN, FAIL_LIGHT_MARGIN),
        "palindromic": (True,) * 4,
        "reconstruction_nullity": RECONSTRUCTION_NULLITY,
        "numerator": NUMERATOR_COEFFS,
        "denominator": DENOMINATOR_COEFFS,
        "coprime": NUMERATOR_DENOMINATOR_COPRIME,
        "withheld_values": WITHHELD_VALUES,
        "withheld_residuals": WITHHELD_RESIDUALS,
        "denominator_roots": DENOMINATOR_ROOTS_IN_BRACKET,
        "numerator_roots": NUMERATOR_ROOTS_IN_BRACKET,
        "zero_crossing": INTERPOLANT_ZERO_CROSSING,
        "denominator_endpoints": (DENOMINATOR_AT_LOW, DENOMINATOR_AT_HIGH),
        "numerator_endpoints": (NUMERATOR_AT_LOW, NUMERATOR_AT_HIGH),
        "denominator_signs": DENOMINATOR_ENDPOINT_SIGNS,
        "numerator_signs": NUMERATOR_ENDPOINT_SIGNS,
        "normalization_matches": NORMALIZATION_MATCHES,
        "band_roots": BAND_POLYNOMIAL_ROOTS,
        "band_signs": BAND_SIGNS_AT_LOW,
        "unimodular_crossing": INTERPOLANT_UNIMODULAR_CROSSING,
        "cross_heavy": B194_CROSS_HEAVY,
        "cross_negative_pair": B194_CROSS_IS_NEGATIVE_PAIR,
        # E -- the response profile.
        "derivative_block": DERIVATIVE_BLOCK,
        "slices": SLICE_RESPONSES,
        "parity": PARITY_RESPONSES,
        "parity_pattern": PARITY_PATTERN_HOLDS,
        "interior_parity_distinct": INTERIOR_PARITY_VALUES_DISTINCT,
        "single_cell_wording": PER_SINGLE_CELL_WORDING_CORRECT,
        "window_zeros": WINDOW_ZEROS_PER_ANCHOR,
        "sign_flip": SIGN_FLIP_SIGNS,
        "sign_flip_per_anchor": SIGN_FLIP_PER_ANCHOR,
        # F -- the volume samples.
        "volume_factors": VOLUME_FACTORS,
        "volume_margins": VOLUME_MARGINS,
        "volume_discriminants": VOLUME_DISCRIMINANTS,
        "volume_multiplicities": {v: (VOLUME_MULTIPLICITY,) * 2
                                  for v in SAMPLED_VOLUMES},
        "volumes_positive": VOLUMES_ALL_POSITIVE,
        "endpoint_member": ENDPOINT_IN_CONFIRMED_SET,
        "outside_positive": OUTSIDE_SAMPLES_POSITIVE,
        # G -- the note, the fence, nsimplify and the float absence.
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
        "carrier_floats": 0,
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
    elif mutation == "claim_window_boundary_curve":
        # BLOCK 194's OWN FENCE BROKEN: a finite set of exact rational points is
        # asserted to be a fitted boundary curve.  It is a census.
        claims["window_boundary_curve"] = True
    elif mutation == "claim_edge_located":
        # THE BRACKET PROMOTED TO A NUMBER: the edge is asserted LOCATED.  What
        # is measured is an open interval and a Sturm count inside it.
        claims["edge_located"] = True
    elif mutation == "claim_volume_interval_maximal":
        # THE SCOUT'S INTERVAL READING, MAXIMALLY: seven samples are asserted to
        # be a maximal interval of positivity.  Nothing between them is measured.
        claims["volume_interval_maximal"] = True
    elif mutation == "claim_all_width_theorem":
        # FOUR WIDTHS PROMOTED TO A THEOREM IN T.  No induction is attempted.
        claims["all_width_theorem"] = True
    elif mutation == "claim_generic_point_theorem":
        claims["generic_point_theorem"] = True
    elif mutation == "claim_continuum_limit":
        claims["continuum_limit"] = True
        claims["dynamics"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_carrier_closure":
        claims["ranks"] = {**claims["ranks"], NEW_WIDTH: 94}
    elif mutation == "break_deep_width_lock":
        claims["deep_census"] = ((LANDED_HEAVY, 2), (LANDED_LIGHT, 1))
    elif mutation == "break_boundary_width_lock":
        claims["boundary_lock_widths"] = (16, 20, 24)
    elif mutation == "break_twelve_deep_core":
        # THE CORRECTED WIDTH LIST DENIED: the T = 12 slot t0 = 3 is asserted to
        # carry the deep value, which would make the deep lock four widths wide.
        # That slot is T/2 - 3, the seam mirror, and it measures DIFFERENT.
        claims["deep_lock_widths"] = (12, 16, 20, 24)
        claims["twelve_slot_is_deep"] = True
        claims["mirror_census"] = DEEP_CENSUS
    elif mutation == "break_big_inverse_count":
        claims["big_inverses"] = 2
    # --- D ----------------------------------------------------------------
    elif mutation == "break_edge_endpoint_signs":
        claims["fail_signs"] = ((1, -1, 1), (1, -1, 1))
    elif mutation == "break_edge_discriminants":
        claims["fail_discriminants"] = (-FAIL_HEAVY_DISCRIMINANT,
                                        FAIL_LIGHT_DISCRIMINANT)
    elif mutation == "break_pole_count":
        claims["denominator_roots"] = 0
    elif mutation == "break_zero_crossing":
        # Alter the declared interpolation model so its numerator has a bracket
        # root.  The measured model has none; this says nothing by itself about
        # the unprobed carrier.
        claims["numerator_roots"] = 1
        claims["zero_crossing"] = True
    elif mutation == "break_normalization_form":
        # Break one of the finite projective carrier/model agreements.
        claims["normalization_matches"] = NORMALIZATION_MATCHES - 1
    elif mutation == "break_unimodular_band":
        # Give the interpolation model a unit-band crossing on the punctured
        # bracket.  No carrier continuum statement is encoded here.
        claims["band_roots"] = (1, 0)
        claims["unimodular_crossing"] = True
    # --- E ----------------------------------------------------------------
    elif mutation == "break_response_values":
        claims["slices"] = {**SLICE_RESPONSES, 3: SLICE_RESPONSES[3] + 1}
    elif mutation == "break_window_law_zeros":
        claims["slices"] = {**SLICE_RESPONSES, 6: sp.Integer(1)}
    elif mutation == "break_sign_flip":
        claims["sign_flip"] = (-1, -1)
    elif mutation == "break_parity_split":
        # THE SCOUT'S "PER-SINGLE-CELL" WORDING ASSERTED: every (s, x) anchor is
        # claimed to give the quoted slice number.  The anchors split by spatial
        # parity into TWO values and neither equals the sum.
        claims["parity"] = {s: (SLICE_RESPONSES[s], SLICE_RESPONSES[s])
                            for s in RESPONSE_SLICES}
        claims["single_cell_wording"] = True
    # --- F ----------------------------------------------------------------
    elif mutation == "break_volume_positivity":
        claims["volumes_positive"] = False
        spoiled = sp.Rational(3, 5)
        claims["volume_margins"] = {
            **VOLUME_MARGINS,
            spoiled: (-VOLUME_MARGINS[spoiled][0], VOLUME_MARGINS[spoiled][1])}
    elif mutation == "break_volume_margins":
        spoiled = sp.Rational(1, 5)
        claims["volume_discriminants"] = {
            **VOLUME_DISCRIMINANTS,
            spoiled: (VOLUME_DISCRIMINANTS[spoiled][0] + 1,
                      VOLUME_DISCRIMINANTS[spoiled][1])}
    elif mutation == "break_endpoint_membership":
        # THE "(1/10, 1]" READING: the very endpoint the scout also claims is
        # asserted to be OUTSIDE the confirmed set.  It is measured positive.
        claims["endpoint_member"] = False
    elif mutation == "break_outside_samples":
        # THE INTERVAL'S TWO ENDS DEFENDED: v = 1/100 and v = 6/5 are asserted
        # to fail.  Both are measured positive, which is why no interval is
        # claimed at all.
        claims["outside_positive"] = False
    # --- G ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    elif mutation == "break_float_absence":
        # THE SECOND HAZARD DENIED: a Float is asserted to be present and
        # harmless.  One Float in the imported block silently turns the exact
        # two-sided inverse residual from 0 into 3459 nonzero entries.
        claims["carrier_floats"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    widths = facts.widths
    edge = facts.edge
    response = facts.response
    volumes = facts.volumes

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 199 artifacts are "
        f"content-identical at it and in the worktree, the stale pin "
        f"{STALE_PARENT_COMMIT[:12]} is a real ancestor carrying NEITHER, the "
        f"machinery import is landed, and {authority.inputs_readable} of "
        f"{len(AUDIT_INPUT_PATHS) - len(SELF_SUPPLIED_INPUTS)} audit inputs "
        f"are readable",
        authority.parent_pin_is_commit
        and claims["parent_commit"] == PARENT_COMMIT
        and claims["stale_parent"] == STALE_PARENT_COMMIT
        and authority.parent_ref_and_ancestry
        and authority.parent_artifact_blobs
        and not authority.stale_parent_artifact_blobs
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact
        and authority.machinery_import_landed
        and authority.inputs_readable == (len(AUDIT_INPUT_PATHS)
                                          - len(SELF_SUPPLIED_INPUTS))
        and not authority.inputs_missing)

    # --- B: THE BANNER AND THE FENCE ---------------------------------------
    checks.check(
        "B-1", f"{claims['imposed']} imposed objects are declared, "
        f"{claims['registered']} are registered and {claims['adopted']} are "
        f"adopted",
        facts.imposed == claims["imposed"] == 7
        and facts.registered == claims["registered"] == 0
        and facts.adopted == claims["adopted"] == 0)
    checks.check(
        "B-2", f"NO GRAVITY IS SUPPLIED and {claims['unsupplied']} gravity "
        f"structures are enumerated as NOT SUPPLIED",
        claims["gravity_supplied"] is False
        and facts.unsupplied == claims["unsupplied"] == 9)
    checks.check(
        "B-3", "NO WINDOW BOUNDARY CURVE is claimed -- Block 194's own fence, "
        "carried here: a finite set of exact rational points is a CENSUS and "
        "is not a fitted curve, and nothing between the points is asserted",
        claims["window_boundary_curve"] is False)
    checks.check(
        "B-4", f"NO LOCATED EDGE is claimed: two endpoints separated by "
        f"{EDGE_BRACKET_WIDTH} are exactly classified; the Sturm count and "
        f"pole belong only to the declared interpolation model, and no carrier "
        f"behavior between probes is asserted",
        claims["edge_located"] is False)
    checks.check(
        "B-5", "NO MAXIMAL VOLUME INTERVAL is claimed: seven exact rational "
        "volumes are measured positive and the edges are NOT located",
        claims["volume_interval_maximal"] is False
        and VOLUME_EDGES_LOCATED is False)
    checks.check(
        "B-6", f"NO ALL-WIDTH THEOREM is claimed: {len(WIDTHS)} exact widths "
        f"are measured and no induction in T is attempted",
        claims["all_width_theorem"] is False)
    checks.check(
        "B-7", "NO GENERIC (m, c) THEOREM is claimed: ONE mass and finitely "
        "many exact rational shears and volumes are not a parameter space",
        claims["generic_point_theorem"] is False)
    checks.check(
        "B-8", "NO CONTINUUM LIMIT and NO DYNAMICS are claimed",
        claims["continuum_limit"] is False and claims["dynamics"] is False)
    checks.check(
        "B-9", f"{claims['readings']} readings are enumerated and each is "
        f"declared a READING rather than a licensed conclusion",
        facts.readings == claims["readings"] == 5
        and claims["readings_licensed"] is False)

    # --- C: THE WIDTH LOCK --------------------------------------------------
    checks.check(
        "C-1", f"the carrier closes at all four widths {WIDTHS}: sizes "
        f"{tuple(claims['sizes'][w] for w in WIDTHS)}, rank(Q) equal to the "
        f"size at each, nnz(d_K^2) {claims['grade_complex']}, "
        f"nnz(Ps H Ps - H) {claims['hodge_reflection']}, nnz(Ps Q Ps - Q^T) "
        f"{claims['covariance']} and TWO-SIDED inverse residuals "
        f"{claims['inverse_residuals']}",
        all(widths[w].size == claims["sizes"][w]
            and widths[w].rank == claims["ranks"][w]
            and widths[w].grade_complex == claims["grade_complex"]
            and widths[w].hodge_reflection == claims["hodge_reflection"]
            and widths[w].covariance == claims["covariance"]
            and widths[w].inverse_residuals == claims["inverse_residuals"]
            for w in WIDTHS))
    checks.check(
        "C-2", f"the DEEP core t0 = {DEEP_CORE} carries the LANDED pair "
        f"squared {claims['deep_census']} at the widths "
        f"{claims['deep_lock_widths']}, with nnz(K_c - K_c^T) "
        f"{claims['gram_symmetry']} at each",
        tuple(claims["deep_lock_widths"]) == DEEP_LOCK_WIDTHS
        and all(widths[w].deep_census == tuple(claims["deep_census"])
                and widths[w].deep_gram_symmetry == claims["gram_symmetry"]
                for w in claims["deep_lock_widths"]))
    checks.check(
        "C-3", f"the T = {MIRROR_WIDTH} slot t0 = {DEEP_CORE} is T/2 - 3, the "
        f"SEAM MIRROR and NOT a deep core, and it carries the DIFFERENT census "
        f"{claims['mirror_census']} -- which is why the deep lock is three "
        f"widths and not four",
        widths[MIRROR_WIDTH].deep_census == tuple(claims["mirror_census"])
        and (widths[MIRROR_WIDTH].deep_census == DEEP_CENSUS)
        is claims["twelve_slot_is_deep"]
        and MIRROR_WIDTH // 2 - 3 == DEEP_CORE)
    checks.check(
        "C-4", f"the near-boundary core t0 = {BOUNDARY_CORE} carries the "
        f"LANDED boundary census {claims['boundary_census']} at ALL FOUR "
        f"widths {claims['boundary_lock_widths']}, and the two-site shift U "
        f"grades the deep spectrum at residuals {claims['u_residuals']} with "
        f"the U = -1 sector carrying {claims['heavy_sector']} and the U = +1 "
        f"sector {claims['light_sector']}",
        tuple(claims["boundary_lock_widths"]) == BOUNDARY_LOCK_WIDTHS
        and all(widths[w].boundary_census == tuple(claims["boundary_census"])
                and widths[w].boundary_gram_symmetry == claims["gram_symmetry"]
                for w in claims["boundary_lock_widths"])
        and all(widths[w].u_residuals == tuple(claims["u_residuals"])
                and widths[w].heavy_sector == tuple(claims["heavy_sector"])
                and widths[w].light_sector == tuple(claims["light_sector"])
                for w in DEEP_LOCK_WIDTHS))
    checks.check(
        "C-5", f"EXACTLY {claims['big_inverses']} exact inverse of size "
        f"{BIG_INVERSE_SIZE} x {BIG_INVERSE_SIZE} or larger is built in this "
        f"runner -- the T = {NEW_WIDTH} carrier, built ONCE in "
        f"{widths[NEW_WIDTH].inverse_seconds:.1f}s -- and every gate above "
        f"reads it rather than recomputing it",
        facts.big_inverses == claims["big_inverses"] == 1
        and facts.big_inverse_size == BIG_INVERSE_SIZE)

    # --- D: TWO ENDPOINTS AND THE INTERPOLATION MODEL ----------------------
    checks.check(
        "D-1", f"the bracket ({EDGE_LOW}, {EDGE_HIGH}) has exact width "
        f"{claims['bracket_width']}, and its four primitive quadratics are "
        f"pass-heavy {claims['pass_heavy']}, pass-light {claims['pass_light']}, "
        f"fail-heavy {claims['fail_heavy']} and fail-light "
        f"{claims['fail_light']}, each of multiplicity "
        f"{claims['multiplicities'][0]} and each PALINDROMIC",
        edge.bracket_width == claims["bracket_width"]
        and edge.pass_heavy == tuple(claims["pass_heavy"])
        and edge.pass_light == tuple(claims["pass_light"])
        and edge.fail_heavy == tuple(claims["fail_heavy"])
        and edge.fail_light == tuple(claims["fail_light"])
        and edge.multiplicities == tuple(claims["multiplicities"])
        and edge.palindromic == tuple(claims["palindromic"]))
    checks.check(
        "D-2", f"the LEADING and LINEAR coefficient signs are "
        f"{claims['pass_signs']} on the pass side and {claims['fail_signs']} "
        f"on the fail side -- the leading coefficients stay POSITIVE and it is "
        f"the HEAVY LINEAR coefficient that flips -- and the fail-side "
        f"discriminants {claims['fail_discriminants']} and margins "
        f"{claims['fail_margins']} are all STRICTLY POSITIVE, so the failure is "
        f"a REAL NEGATIVE reciprocal pair and not a complex one",
        edge.pass_signs == tuple(claims["pass_signs"])
        and edge.fail_signs == tuple(claims["fail_signs"])
        and edge.pass_discriminants == tuple(claims["pass_discriminants"])
        and edge.fail_discriminants == tuple(claims["fail_discriminants"])
        and edge.pass_margins == tuple(claims["pass_margins"])
        and edge.fail_margins == tuple(claims["fail_margins"])
        and all(v > 0 for v in edge.fail_discriminants)
        and all(v > 0 for v in edge.fail_margins))
    checks.check(
        "D-3", f"the declared [4/4] interpolation model beta_fit(c) = "
        f"-2 N(c) / D(c) is fitted EXACTLY from "
        f"{len(RECONSTRUCTION_POINTS)} measured points at nullity "
        f"{claims['reconstruction_nullity']}, with N = {claims['numerator']}, "
        f"D = {claims['denominator']}, gcd(N, D) = 1, and the TWO WITHHELD "
        f"points {WITHHELD_POINTS} reproduced at residuals "
        f"{claims['withheld_residuals']}",
        edge.reconstruction_nullity == claims["reconstruction_nullity"]
        and edge.numerator == tuple(claims["numerator"])
        and edge.denominator == tuple(claims["denominator"])
        and edge.coprime is claims["coprime"]
        and edge.withheld_residuals == tuple(claims["withheld_residuals"])
        and edge.withheld_values == tuple(claims["withheld_values"]))
    checks.check(
        "D-4", f"for the interpolation model, in the bracket D has EXACTLY "
        f"{claims['denominator_roots']} "
        f"root and N has {claims['numerator_roots']}, with D "
        f"{claims['denominator_endpoints'][0]} > 0 at the low end and "
        f"{claims['denominator_endpoints'][1]} < 0 at the high end while N is "
        f"POSITIVE at both -- so the MODEL has a denominator pole rather than "
        f"a numerator zero; this does not classify the carrier between probes",
        edge.denominator_roots == claims["denominator_roots"]
        and edge.numerator_roots == claims["numerator_roots"]
        and edge.denominator_endpoints == tuple(
            claims["denominator_endpoints"])
        and edge.numerator_endpoints == tuple(claims["numerator_endpoints"])
        and edge.denominator_signs == tuple(claims["denominator_signs"])
        and edge.numerator_signs == tuple(claims["numerator_signs"])
        and (edge.numerator_roots > 0) is claims["zero_crossing"])
    checks.check(
        "D-5", f"the carrier heavy quadratic agrees PROJECTIVELY with the "
        f"model (D(c), -2 N(c), D(c)) at all "
        f"{claims['normalization_matches']} listed probes; this is finite "
        f"agreement, not a symbolic carrier identity",
        edge.normalization_matches == claims["normalization_matches"]
        == len(NORMALIZATION_PROBES)
        and INTERPOLANT_LEADING_COEFFICIENT_IS_DENOMINATOR is True)
    checks.check(
        "D-6", f"for the interpolation model N -+ D have "
        f"{claims['band_roots']} roots in the bracket with signs "
        f"{claims['band_signs']} at the low end, so |beta_fit| > 2 on each "
        f"component of the punctured bracket; the model is undefined at its "
        f"pole and no between-probe carrier conclusion follows -- and at the "
        f"new exact carrier point "
        f"(9/20, {B194_CROSS_SHEAR}) the heavy pair {claims['cross_heavy']} is "
        f"NEGATIVE, extending Block 194's census {B194_NEGATIVE_PAIR_CENSUS} "
        f"column to a mass outside its {B194_SEARCHED_MASSES}",
        edge.band_roots == tuple(claims["band_roots"])
        and edge.band_signs == tuple(claims["band_signs"])
        and any(v > 0 for v in edge.band_roots) is claims["unimodular_crossing"]
        and edge.cross_heavy == tuple(claims["cross_heavy"])
        and edge.cross_is_negative_pair is claims["cross_negative_pair"]
        and B194_MASSES_INCLUDE_FIXTURE is False)

    # --- E: THE RESPONSE PROFILE -------------------------------------------
    checks.check(
        "E-1", f"the exact volume derivative dB is {claims['derivative_block']} "
        f"and the SIX slice-cell responses -- each the sum of all FOUR spatial "
        f"anchors at s with their reflected image partners -- are "
        f"{tuple(claims['slices'][s] for s in RESPONSE_SLICES)}",
        response.derivative_block == tuple(
            tuple(sp.Rational(v) for v in row)
            for row in claims["derivative_block"])
        and all(response.slices[s] == claims["slices"][s]
                for s in RESPONSE_SLICES))
    checks.check(
        "E-2", f"the individual (s, x) responses follow spatial parity -- "
        f"x in {{0, 2}} against x in {{1, 3}} -- with two DISTINCT values on "
        f"s = 2,3,4,5 and a common zero on s = 1,6; the scout's "
        f"per-single-cell wording is {claims['single_cell_wording']}",
        response.parity_pattern is claims["parity_pattern"]
        and response.interior_parity_distinct
        is claims["interior_parity_distinct"]
        and all(response.parity[s] == tuple(claims["parity"][s])
                for s in RESPONSE_SLICES)
        and all(response.parity[s][0] == response.slices[s]
                for s in RESPONSE_SLICES) is claims["single_cell_wording"])
    checks.check(
        "E-3", f"the window law holds AT EVERY SPATIAL ANCHOR SEPARATELY and "
        f"not only after the spatial sum: every anchor at s in "
        f"{WINDOW_ZERO_SLICES} responds EXACTLY ZERO, because a cell anchored "
        f"at s occupies slices {{s, s+1}} and that meets the response window "
        f"{RESPONSE_WINDOW} only for s = 2, 3, 4, 5",
        response.window_zeros_per_anchor is claims["window_zeros"]
        and all(claims["slices"][s] == 0 for s in WINDOW_ZERO_SLICES))
    checks.check(
        "E-4", f"the s = {SIGN_FLIP_SLICES[0]} -> s = {SIGN_FLIP_SLICES[1]} "
        f"SIGN FLIP is exact at signs {claims['sign_flip']}, and it survives "
        f"BEFORE summation: both parity values are negative at "
        f"s = {SIGN_FLIP_SLICES[0]} and both are positive at "
        f"s = {SIGN_FLIP_SLICES[1]}",
        response.sign_flip_signs == tuple(claims["sign_flip"])
        and response.sign_flip_per_anchor is claims["sign_flip_per_anchor"])

    # --- F: THE VOLUME SAMPLES ---------------------------------------------
    checks.check(
        "F-1", f"at ALL {len(SAMPLED_VOLUMES)} sampled volumes "
        f"{SAMPLED_VOLUMES} the deep monodromy factors into TWO DISTINCT "
        f"palindromic quadratics, each of multiplicity "
        f"{VOLUME_MULTIPLICITY}, matching the declared factors entry for entry",
        all(volumes.factors[v] == tuple(claims["volume_factors"][v])
            and volumes.multiplicities[v] == tuple(
                claims["volume_multiplicities"][v])
            and volumes.distinct[v] and all(volumes.palindromic[v])
            for v in SAMPLED_VOLUMES))
    checks.check(
        "F-2", f"every one of those factors has a POSITIVE leading "
        f"coefficient, a STRICTLY POSITIVE margin |b| - 2a and a STRICTLY "
        f"POSITIVE discriminant, so each pair is real, positive and reciprocal "
        f"-- positivity {claims['volumes_positive']} at all "
        f"{len(SAMPLED_VOLUMES)} samples",
        volumes.positive is claims["volumes_positive"]
        and all(volumes.margins[v] == tuple(claims["volume_margins"][v])
                and volumes.discriminants[v] == tuple(
                    claims["volume_discriminants"][v])
                and all(m > 0 for m in volumes.margins[v])
                and all(d > 0 for d in volumes.discriminants[v])
                for v in SAMPLED_VOLUMES))
    checks.check(
        "F-3", f"v = {CLAIMED_INTERVAL_LOW} is IN the confirmed positive set, "
        f"which the scout's half-open '({CLAIMED_INTERVAL_LOW}, 1]' notation "
        f"EXCLUDES while also claiming it -- the notation is corrected here "
        f"and the membership is {claims['endpoint_member']}",
        (CLAIMED_INTERVAL_LOW in volumes.factors
         and all(m > 0 for m in volumes.margins[CLAIMED_INTERVAL_LOW])
         and all(d > 0 for d in volumes.discriminants[CLAIMED_INTERVAL_LOW]))
        is claims["endpoint_member"])
    checks.check(
        "F-4", f"positivity ALSO holds at {OUTSIDE_SAMPLES}, which lie outside "
        f"BOTH ends of the claimed interval, so the sampled positive set is "
        f"wider than the claim on both sides -- and it is recorded as SEVEN "
        f"SAMPLES with the edges NOT located, never as a region",
        (all(all(m > 0 for m in volumes.margins[v])
             and all(d > 0 for d in volumes.discriminants[v])
             for v in OUTSIDE_SAMPLES)) is claims["outside_positive"]
        and VOLUME_EDGES_LOCATED is False)

    # --- G: THE NOTE, THE FENCE, nsimplify AND THE FLOAT ABSENCE -----------
    checks.check(
        "G-1", f"the note is present at {NOTE_PATH.name} and all five N5 "
        f"resolution certificates appear in it VERBATIM",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "G-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can manufacture a false model numerator zero, "
        f"collapse a window zero that is the content, or merge the two parity "
        f"values into one",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "G-3", f"NO sympy Float appears in ANY carrier matrix built here -- "
        f"{claims['carrier_floats']} across every block, Hodge, action and "
        f"inverse in the cache -- which is load-bearing and not stylistic: the "
        f"imported shear_hodge forms 1/v by PYTHON division, so a plain int "
        f"volume returns a Float corner that compares EQUAL, leaves this "
        f"fixture's factorization unmoved, and silently turns the exact "
        f"two-sided inverse residual from 0 into {FLOAT_HAZARD_RESIDUAL} "
        f"nonzero entries at T = 16",
        facts.carrier_floats == claims["carrier_floats"] == FLOAT_CALLS)
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    edge = facts.edge
    response = facts.response
    volumes = facts.volumes
    print("MEASURED BLOCK 200")
    print(f"elapsed={elapsed_ns / 1000000000:.1f}s main={facts.main_head}")
    print(f"verdict={CHECK_VERDICT} registered={facts.registered} "
          f"adopted={facts.adopted} floats={facts.carrier_floats}")
    print(f"widths={WIDTHS} deep_agreement={DEEP_LOCK_WIDTHS} "
          f"boundary_agreement={BOUNDARY_LOCK_WIDTHS} big_inverses="
          f"{facts.big_inverses}")
    print(f"endpoints={edge.bracket} pass_signs={edge.pass_signs} "
          f"fail_signs={edge.fail_signs}")
    print(f"fit=[4/4] N={edge.numerator} D={edge.denominator} "
          f"withheld_residuals={edge.withheld_residuals}")
    print(f"fit_only: D_roots={edge.denominator_roots} "
          f"N_roots={edge.numerator_roots} band_roots={edge.band_roots}; "
          "carrier_between_probes=OPEN")
    print(f"response_slices={tuple(response.slices[s] for s in RESPONSE_SLICES)}")
    print(f"parity_pattern={response.parity_pattern} interior_distinct="
          f"{response.interior_parity_distinct} endpoint_zeros="
          f"{response.window_zeros_per_anchor} sign_flip_per_anchor="
          f"{response.sign_flip_per_anchor}")
    print(f"positive_volume_samples={SAMPLED_VOLUMES} all_positive="
          f"{volumes.positive}; no interval claimed")
    print("scope=finite exact probes; no all-T, generic-parameter, continuum, "
          "dynamics, gravity, located edge, or maximal interval claim")


N5_FENCE = (
    "N5: per_element: checked — fourteen exact values of the heavy-sector "
    "coefficient do not determine an unrestricted rational continuation; "
    "the explicit beta_alt construction preserves every probe and inserts "
    "one additional rational zero.\n"
    "N5: per_site: checked and not executed — the interpolation boundary "
    "concerns one compressed scalar coefficient as shear varies, not a "
    "sitewise response; no between-probe site claim is made.\n"
    "N5: per_mode: checked — only the U=-1 heavy compression is fitted; the "
    "U=+1 light compression is classified at the two endpoints and receives "
    "no interpolation or between-probe conclusion.\n"
    "N5: per_block: checked — all interpolation statements are restricted to "
    "T=16, t0=3, m=9/20 and unit volume; other cores, widths, masses, and "
    "carrier families are not classified.\n"
    "N5: lattice_wide: checked and not executed — no all-T, generic-parameter, "
    "continuum, dynamics, gravity, energy, or Nature conclusion is drawn from "
    "the finite exact probes."
)

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
