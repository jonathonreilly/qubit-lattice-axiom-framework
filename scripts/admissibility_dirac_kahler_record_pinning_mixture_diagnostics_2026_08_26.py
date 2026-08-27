#!/usr/bin/env python3
"""BLOCK 202 -- FINITE SUBSTITUTION-PROFILE LINEAR-ALGEBRA DIAGNOSTICS.

The runner reads Block 171's committed finite matrices and preserves exact
profile residuals, restoring weights, context-stack ranks, row-block support,
hermitization comparisons, and a seven-point q sweep.  The four cell
substitutions and the use of a mid-slice W9 profile as mixture weights are
declared diagnostic choices, not a framework-derived measurement instrument.

At the committed complex spatial background, q -> -q is not global matrix
conjugation.  The mismatch is measured explicitly.  The q sweep therefore
establishes only a non-even response under this one dial reversal, not a
general conjugation, interference, contextuality, classical-no-go, or quantum
claim.  Nothing is registered or adopted.

Thirty-one claim-only mutations each fail exactly their mapped family.
"""

from __future__ import annotations

import argparse
import ast
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORT, LANDED, AND IT IS EXACTLY ONE OBJECT: Block 171's
# committed bench, read through ITS OWN Site and Env classes so that every
# profile compared against here is the LANDED construction and not a rebuild of
# it.  The independent check deliberately rebuilt the same profiles from raw Q
# data and agreed digit for digit; this runner takes the landed route and the
# note records both.
try:
    import admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21 as b171
    BENCH_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b171 = None
    BENCH_IMPORT_LANDED = False
MACHINERY_IMPORT_LANDED = BENCH_IMPORT_LANDED

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 201 is the commit this block's
# branch is cut from; its note and its runner both exist at PARENT_COMMIT and
# NEITHER exists at STALE_PARENT_COMMIT, which is the Block 200 tip.
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_covariant_rule_identification_"
    "2026_08_26.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "5455d48a8edbb9eab1a76aad1d4e804c3dd18838",
    "ffbb8fd19247f8938261a868783e86d302ec8aea",
)
# THE CONSTRUCTION AUTHORITY.  Block 171 supplies the committed 12x4 bench, the
# Site and Env classes, the record dictionary, the W1/W2/W9 gram constructions,
# the holonomy action Q_holo_t and the committed spatial dial.
BLOCK171_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_"
    "THEOREM_NOTE_2026-08-21.md"
)
BLOCK171_RUNNER = (
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
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
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block201-"
              "covariant-rule-identification-20260826")
PARENT_COMMIT = "d460d14f89c38c4c2a8774fc62cc103d0ae706a1"
# The Block 200 tip: a real ancestor of HEAD that predates Block 201 and
# therefore carries NEITHER parent artifact.
STALE_PARENT_COMMIT = "4a21fefcce3f161dca9e13b64212add7db003349"
# A real but superseded authority head, carried forward from Block 201's record.
STALE_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_pinning_is_measurement",
    "claim_record_formation_law",
    "claim_diagnostic_is_quantum",
    "claim_classical_no_go",
    "claim_readings_licensed",
    "break_bench_instrument",
    "break_mixture_failure",
    "break_restoring_weight",
    "break_candidate_mismatch",
    "break_no_common_weight",
    "break_per_context_solvability",
    "break_clean_pair",
    "break_hermitized_degeneracy",
    "break_across_level_inconsistency",
    "break_committed_dial",
    "claim_q_flip_is_conjugation",
    "break_odd_response",
    "break_sign_changes",
    "break_joint_identification_fence",
    "claim_outcome_space_exhaustive",
    "claim_causal_isolation",
    "claim_non_hermiticity_sufficient",
    "claim_phase_models_excluded",
    "break_instance_scope",
    "drop_n5_fence",
    "break_nsimplify_absence",
    "break_float_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_pinning_is_measurement": "B",
    "claim_record_formation_law": "B",
    "claim_diagnostic_is_quantum": "B",
    "claim_classical_no_go": "B",
    "claim_readings_licensed": "B",
    "break_bench_instrument": "C",
    "break_mixture_failure": "C",
    "break_restoring_weight": "C",
    "break_candidate_mismatch": "C",
    "break_no_common_weight": "D",
    "break_per_context_solvability": "D",
    "break_clean_pair": "D",
    "break_hermitized_degeneracy": "E",
    "break_across_level_inconsistency": "E",
    "break_committed_dial": "F",
    "claim_q_flip_is_conjugation": "F",
    "break_odd_response": "F",
    "break_sign_changes": "F",
    "break_joint_identification_fence": "G",
    "claim_outcome_space_exhaustive": "G",
    "claim_causal_isolation": "G",
    "claim_non_hermiticity_sufficient": "G",
    "claim_phase_models_excluded": "G",
    "break_instance_scope": "G",
    "drop_n5_fence": "H",
    "break_nsimplify_absence": "H",
    "break_float_absence": "H",
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
        for key, _, value in self.results:
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
    "THE FOUR DECLARED SUBSTITUTION PROFILES: the four cells (mid, x) for x = 0..3 at mid = 3 are separately set to class value 0 and read through Block 171's Env.profile; they are not supplied outcomes or a measurement instrument",
    "THE CONDITIONAL MIXTURE TEST AND ITS RESTORING-WEIGHT SYSTEM: if the four profiles are treated as conditionals and profile('W9', mid) is treated as their weight, the residual is P0 - sum_x w_x P_x; these interpretations are declared for the test rather than derived from the Minimal Axioms",
    "THE SIX TESTED READOUT CONTEXTS: the gram families (W9, W2) against the record-free levels (5, 4, 2), stacked as 24 profile equations plus one normalisation row, together with the CLEAN PAIR W9-L5 with W2-L5",
    "THE HERMITIZED COMPARISON BENCH: herm(Q) formed AFTER record substitution at the base and at all four substituted matrices, deleting the anti-Hermitian part while carrying identical substitutions on both sides",
    "THE FIXED-BACKGROUND q SWEEP: the committed holonomy action Q_holo_t at spatial dial {g_re: 1/3, g_im: 1/4}, seven q values, the non-even split, the sign-change census, and the exact failure of q flip to equal global conjugation",
    "BLOCK 171's COMMITTED 12x4 BENCH READ THROUGH ITS OWN Site AND Env CLASSES AND NOT REBUILT: Site('12x4', 12, 4) with N = 24, T = 6, c = 1, tstar = 5 and lx = 4, the xgraded carrier substitution, the record dictionary, the W1/W2/W9 gram constructions and the committed spatial dial",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL TWELVE ARE
# FALSE AND STAY FALSE.  SIX OF THEM ARE THE INDEPENDENT CHECK'S OWN C6
# CORRECTIONS, CARRIED HERE AS CONTENT RATHER THAN AS ERRATA.
GRAVITY_SUPPLIED_CLAIMED = False
PINNING_IS_MEASUREMENT_CLAIMED = False
RECORD_FORMATION_LAW_CLAIMED = False
OUTCOME_SPACE_EXHAUSTIVE_CLAIMED = False
CAUSAL_ISOLATION_CLAIMED = False
NON_HERMITICITY_SUFFICIENT_CLAIMED = False
PHASE_SENSITIVE_MODELS_EXCLUDED_CLAIMED = False
QUANTUM_BOUND_VIOLATION_CLAIMED = False
CLASSICAL_NO_GO_CLAIMED = False
GENERIC_PARAMETER_THEOREM_CLAIMED = False
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
# THE THREE WORDS THAT NAME NOTHING ESTABLISHED HERE, DECLARED SO THE NOTE'S
# ABSENCE OF THEM IS A MEASUREMENT AND NOT A PROMISE.
UNNAMED_PHYSICS_WORDS = ("QUANTUM", "BELL", "LEGGETT-GARG")
# THE ONE PHRASE THE PACKAGE LICENSES, VERBATIM.
LICENSED_PHRASE = "finite substitution-profile incompatibility diagnostics"
READINGS = (
    "The mixture residual is conditional on treating four substitutions as outcomes and the native mid-slice profile as their weights; the framework supplies neither interpretation.",
    "No four-component weight fits the six tested profiles, but richer latent spaces and other response models remain untested.",
    "The unchanged slot-5 row block is an entrywise certificate, not causal or statistical isolation, because the profile uses the inverse of the full matrix.",
    "Hermitization makes W9 and W2 coincide on the selected level; the separate three-level rank inconsistency survives.  This does not identify a physical source.",
    "The q sweep is non-even at the fixed complex spatial dial, but q-to-minus-q is not global conjugation of the action and has no licensed phase or intensity interpretation here.",
    "Every result is restricted to one finite bench, carrier, slot, class value, spatial dial and seven temporal-dial samples.",
)
CHECK_VERDICT = "FINITE-ALGEBRA-PRESERVED-PHYSICAL-INTERPRETATION-NOT-SUPPLIED"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0

# --- C: THE INSTRUMENT AND THE MIXTURE FAILURE -------------------------------
BENCH_TAG = "12x4"
BENCH_COVER = 12
BENCH_LX = 4
BENCH_N = 24
BENCH_T = 6
BENCH_CORE = 1
BENCH_TSTAR = 5
MID_SLOT = 3
READ_LEVEL = 5
RECORD_CLASS_VALUE = 0
PIN_CELLS = ((3, 0), (3, 1), (3, 2), (3, 3))
READ_ROWS = (20, 21, 22, 23)
MID_ROWS = (12, 13, 14, 15)
GRAM_PRIMARY = "W9"
GRAM_SECOND = "W2"
GRAM_THIRD = "W1"
MIXTURE_IDENTITY_HOLDS = False
MIXTURE_RESIDUAL_NONZERO = (True, True, True, True)
MIXTURE_RESIDUAL_SIGNS = ("+", "-", "+", "+")
MIXTURE_RESIDUAL_SUM = 0
RESTORING_RANKS = (4, 4)
RESTORING_SUM_IS_ONE = True
RESTORING_NONNEGATIVE = True
# THE UNIQUE RESTORING FOUR-WEIGHT, AS FOUR EXACT RATIONALS.  Their numerators
# run past two hundred digits and they are carried in full rather than by a
# hash, so the note and the runner can be compared entry for entry.
RESTORING_WEIGHT = (
    sp.Rational(
        33154389136295793458600031564086468791702539980838836730177947625931900442350305089185584468887076664154046037317562017007594780181729922544232522011468546824068750838022057420519934113665945064033332023521600,
        132023313790888122352490927058928238445516432536630648659370029308150637998863598169246362714781195877931150814082350300465021860369515458810438840010525090052361640631688398201077715318463759273691643002011839),
    sp.Rational(
        32665172262588378893166192217188470240389057013868355694493181261255057266054573648086404300761033628234047966460503059714339939298467300533356029192179148418400698112460819974839998807124612328367848072421000,
        132023313790888122352490927058928238445516432536630648659370029308150637998863598169246362714781195877931150814082350300465021860369515458810438840010525090052361640631688398201077715318463759273691643002011839),
    sp.Rational(
        3212500231948403736288418138804744579328951580039206119705885232622019648263551580704624981102258442270313624789355019939572787804323286346292074025440452395019178426061296588347776741953405722273358310700813,
        44007771263629374117496975686309412815172144178876882886456676436050212666287866056415454238260398625977050271360783433488340620123171819603479613336841696684120546877229466067025905106154586424563881000670613),
    sp.Rational(
        18855417232052912930619816287079688558479326933935279291860414907699207115222688229953499667275436752910705311978740054641456259158782792231324688910185345874944885467673877013558150723937661571490129324655600,
        44007771263629374117496975686309412815172144178876882886456676436050212666287866056415454238260398625977050271360783433488340620123171819603479613336841696684120546877229466067025905106154586424563881000670613),
)
CANDIDATE_NAMES = (
    "W9(mid)", "W2(mid)", "W1(mid)",
    "normalised diagonal of herm(Q[mm,mm]^-1)",
)
CANDIDATE_MISMATCHES = (True, True, True, True)

# --- D: THE SIX CONTEXTS AND THE CLEAN PAIR ----------------------------------
CONTEXT_FAMILIES = ("W9", "W2")
CONTEXT_LEVELS = (5, 4, 2)
CONTEXT_COUNT = 6
STACK_SHAPE = (25, 4)
STACK_RANKS = (4, 5)
COMMON_WEIGHT_EXISTS = False
PER_CONTEXT_RANKS = {
    ("W9", 5): (4, 4), ("W9", 4): (4, 4), ("W9", 2): (4, 4),
    ("W2", 5): (4, 4), ("W2", 4): (4, 4), ("W2", 2): (4, 4),
}
PER_CONTEXT_NONNEGATIVE = (True, True, True, True, True, True)
PER_CONTEXT_SUM_IS_ONE = (True, True, True, True, True, True)
READ_ROW_BLOCK_DELTA = (0, 0, 0, 0)
CLEAN_PAIR_INDIVIDUAL_RANKS = ((4, 4), (4, 4))
CLEAN_PAIR_STACK_SHAPE = (9, 4)
CLEAN_PAIR_STACK_RANKS = (4, 5)
CLEAN_PAIR_CONSISTENT = False

# --- E: THE HERMITIZATION DEGENERACY -----------------------------------------
ANTI_HERMITIAN_NNZ = 56
HERMITISED_W9_EQUALS_W2 = (True, True, True, True, True)
NON_HERMITICITY_IS_NECESSARY = True
REAL_THREE_LEVEL_RANKS = (4, 5)
HERMITISED_THREE_LEVEL_RANKS = (4, 5)
ACROSS_LEVEL_SURVIVES_HERMITISATION = True

# --- F: THE PHASE SWEEP ------------------------------------------------------
SPATIAL_DIAL_REAL = sp.Rational(1, 3)
SPATIAL_DIAL_IMAGINARY = sp.Rational(1, 4)
TEMPORAL_DIAL_VALUES = (
    sp.Rational(-2), sp.Rational(-1), sp.Rational(-1, 2), sp.Rational(0),
    sp.Rational(1, 2), sp.Rational(1), sp.Rational(2),
)
# THE CORRECTED INSTRUMENT, MEASURED RATHER THAN NARRATED.  The first firing of
# this probe left the spatial dial SYMBOLIC and asked for the inverse of a
# 24 x 24 action carrying two free symbols; it was killed.  The committed dial
# is the fix, and the fix is a MEASURED fact about the action's symbol content.
UNDIALLED_FREE_SYMBOLS = 2
DIALLED_FREE_SYMBOLS = 0
CONJUGATION_INVARIANT = (True, True, True, True, True)
Q_FLIP_CONJUGATION_RESIDUALS = (96, 92, 92, 92, 92)
Q_FLIP_IS_GLOBAL_CONJUGATION = False
SWEEP_SIGNS = {
    sp.Rational(-2): ("+", "-", "+", "+"),
    sp.Rational(-1): ("+", "-", "+", "+"),
    sp.Rational(-1, 2): ("+", "-", "+", "+"),
    sp.Rational(0): ("+", "-", "+", "+"),
    sp.Rational(1, 2): ("-", "-", "+", "+"),
    sp.Rational(1): ("-", "-", "+", "+"),
    sp.Rational(2): ("+", "-", "+", "+"),
}
SWEEP_SAMPLED_ZEROS = (0, 0, 0, 0)
ODD_MAGNITUDES = (sp.Rational(1, 2), sp.Rational(1), sp.Rational(2))
ODD_NONZERO = ((True, True, True, True),) * 3
ODD_SIGNS = (("-", "+", "-", "+"),) * 3
SIGN_CHANGES = (2, 0, 0, 0)
EVEN_ONLY_EXPLANATION_EXCLUDED = False

# --- G: THE SIX SCOPE FENCES -------------------------------------------------
JOINT_IDENTIFICATION_HALVES = (
    "the four pinned profiles read as CONDITIONALS of one common joint law",
    "the native mid-slice profile('W9', mid) read as their FORMATION WEIGHTS",
)
WHICH_HALF_FAILS_IS_OPEN = True
OUTCOME_SPACE_DIMENSION_TESTED = 4
UNTESTED_OUTCOME_REFINEMENTS = (
    "the record class-value dimension, which this block holds fixed at 0",
    "observable-dependent disturbance models",
    "any readout family outside the tested pair (W9, W2)",
    "any level outside the tested triple (5, 4, 2)",
)
ROW_BLOCK_CERTIFICATE_ONLY = True
READOUT_USES_GLOBAL_INVERSE = True
CLASSICAL_MODELS_NOT_EXCLUDED = (
    "classical phase-sensitive wave models",
    "observable-dependent classical disturbance models",
    "classical models over a richer outcome space",
)
INSTANCE_SCOPE = (
    "one bench, the committed Site('12x4', 12, 4)",
    "one carrier, the committed xgraded substitution",
    "one mid slot, mid = 3",
    "class-0 pins at four cells",
    "one committed spatial dial {g_re: 1/3, g_im: 1/4}",
    "seven temporal dial values",
)
INSTANCE_SCOPE_COUNT = 6
SCOPE_GENERALISATION_CLAIMED = False

# THE ONE-FAMILY CONTRACT IS ENFORCED BY DISJOINT CLAIM KEYS AND NOT ONLY BY THE
# ASSERTION IN main().  Every claim key below is read by EXACTLY ONE gate.  The
# G fences therefore carry their own constants -- ROW_BLOCK_CERTIFICATE_ONLY,
# NON_HERMITICITY_SUFFICIENT_CLAIMED, PHASE_SENSITIVE_MODELS_EXCLUDED_CLAIMED,
# SCOPE_GENERALISATION_CLAIMED and the rest -- rather than re-reading the B and E
# keys that state the same thing from the other side.  Where a G gate depends on
# a fact measured elsewhere, the gate NAMES the family that measures it in its
# statement and does not consume that family's claim, so neither leans on the
# other and no mutation can flip two families at once.

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  This block's ENTIRE content is a set of exact NONZERO
# statements about numbers whose decimal displays sit between 1e-6 and 1e-4:
# a four-component mixture residual, a non-even q response at three magnitudes,
# and four candidate mismatch vectors.  Every one of them would be turned into
# a spurious success -- the mixture identity would appear to HOLD, and the
# finite non-even-response diagnostic would vanish -- by one tolerance-carrying
# call.  Gate H counts the occurrences in this file's own source and requires
# ZERO, requires ZERO float literals by an AST scan of the same source, and
# requires that decimal conversion happen at EXACTLY ONE call site, inside the
# display helper, so no verdict predicate can ever consume a float.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def float_literal_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many float literals this runner's own source
    contains, by an AST walk rather than by a text search.  A float literal is
    one way an inexact number could enter a file whose every comparison is an
    exact rational one."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    """THE SECOND HALF OF THE SAME HYGIENE, AND IT IS THE HALF THIS BLOCK
    ACTUALLY NEEDS.  The note carries decimal DISPLAYS for residuals whose exact
    values run to hundreds of digits, so a float conversion must exist
    somewhere; what must NOT exist is a second one.  This counts the call sites
    of the builtin float in this runner's own source by an AST walk, and gate H
    requires EXACTLY ONE -- the display helper below.  Every verdict predicate
    in this file therefore consumes exact rationals only, by measurement."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


def display(value) -> str:
    """THE ONE AND ONLY DECIMAL CONVERSION IN THIS FILE, AND IT IS DISPLAY-ONLY.
    Nothing this function returns is ever compared, ranked, summed or gated; it
    exists so the note can print +9.178e-05 beside a two-hundred-digit exact
    rational.  Gate H-3 measures that this is the sole float call site."""
    return f"{float(value):+.3e}"


def gaussian_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    """THE EXACT INVERSE OVER QQ_I, AND IT IS NOT A NUMERICAL METHOD.  The
    committed carrier carries an imaginary unit, so the field is QQ_I rather
    than QQ; DomainMatrix carries out the inverse by exact fraction-free
    arithmetic over that field.  No float is created at any point and no
    tolerance exists to be tuned."""
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix)).convert_to(QQ_I).to_field().inv().to_Matrix()


def exact_rank(matrix: sp.MatrixBase) -> int:
    """The rank over QQ_I, exactly.  Every consistency verdict in families C, D
    and E is one of these numbers against another, never a residual norm."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ_I).rank()


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    matrix = sp.Matrix(matrix)
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is
    involved."""
    return nonzero_entries(sp.Matrix(matrix).applyfunc(sp.expand))


def sign_word(value) -> str:
    """The exact sign of an exact rational.  Ternary and never thresholded."""
    return "+" if value > 0 else "-" if value < 0 else "0"


def sign_tuple(vector) -> tuple:
    return tuple(sign_word(value) for value in vector)


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(sp.expand((sp.Matrix(matrix) + sp.Matrix(matrix).H) / 2))


# ---------------------------------------------------------------------------
# THE MEASURED FACTS
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class InstrumentFacts:
    tag: str
    size: int
    width: int
    core: int
    tstar: int
    extent: int
    read_rows: tuple
    mid_rows: tuple
    pin_cells: tuple
    identity_holds: bool
    residual_nonzero: tuple
    residual_signs: tuple
    residual_sum: object
    residual_display: tuple
    restoring_ranks: tuple
    restoring_weight: tuple
    restoring_sum_is_one: bool
    restoring_nonnegative: bool
    restoring_display: tuple
    candidate_mismatches: tuple
    candidate_values: tuple


@dataclass(frozen=True)
class ContextFacts:
    stack_shape: tuple
    stack_ranks: tuple
    common_exists: bool
    per_context_ranks: dict
    per_context_nonnegative: tuple
    per_context_sum_is_one: tuple
    read_row_block_delta: tuple
    clean_pair_individual: tuple
    clean_pair_shape: tuple
    clean_pair_ranks: tuple
    clean_pair_consistent: bool


@dataclass(frozen=True)
class HermitianFacts:
    anti_hermitian_nnz: int
    w9_equals_w2: tuple
    real_three_level: tuple
    hermitised_three_level: tuple


@dataclass(frozen=True)
class SweepFacts:
    undialled_symbols: int
    dialled_symbols: int
    conjugation_invariant: tuple
    q_flip_conjugation_residuals: tuple
    signs: dict
    sampled_zeros: tuple
    displays: dict
    odd_nonzero: tuple
    odd_signs: tuple
    odd_displays: tuple
    even_displays: tuple
    sign_changes: tuple


@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    readings: int
    unnamed_words: int
    instrument: InstrumentFacts
    contexts: ContextFacts
    hermitian: HermitianFacts
    sweep: SweepFacts
    scope: dict
    nsimplify_calls: int
    float_literals: int
    float_calls: int


def profile_system(base_profiles, pinned_profiles, extent, normalise=True):
    """THE OUTCOME SYSTEM, AND ITS SHAPE IS ITS CONTENT.  One row per readout
    component per level: the four pinned profiles are the columns and the
    record-free profile is the right-hand side.  The optional final row is the
    affine normalisation sum(w) = 1."""
    rows, rhs = [], []
    for base, pinned in zip(base_profiles, pinned_profiles):
        for component in range(extent):
            rows.append([pinned[x][component] for x in range(extent)])
            rhs.append(base[component])
    if normalise:
        rows.append([sp.Integer(1)] * extent)
        rhs.append(sp.Integer(1))
    return sp.Matrix(rows), sp.Matrix(rhs)


def solve_exact(matrix: sp.Matrix, rhs: sp.Matrix, extent: int) -> tuple:
    """SOLVE, DO NOT SEARCH, AND VERIFY THE SOLUTION AGAINST EVERY ROW.  A
    full-column-rank consistent system is reduced to an invertible square
    subsystem by exact pivot selection, inverted over QQ_I, and the answer is
    substituted back into ALL the original rows at exact residual zero."""
    pivots = sp.Matrix(matrix.T).rref()[1]
    square = sp.Matrix([[matrix[r, c] for c in range(extent)] for r in pivots])
    target = sp.Matrix([rhs[r] for r in pivots])
    solution = tuple(sp.cancel(v) for v in (gaussian_inverse(square) * target))
    verified = residual_count(
        matrix * sp.Matrix(list(solution)) - rhs) == ZERO_RESIDUAL
    return solution, verified


def measure_instrument(site, base_env, pinned_envs, base_action) -> InstrumentFacts:
    """THE INSTRUMENT AND THE MIXTURE FAILURE.  Block 171's own Env.profile is
    called for every profile here, so the numbers the residual is built from are
    the LANDED ones and not a rebuild of them."""
    extent = site.lx
    p0 = tuple(base_env.profile(GRAM_PRIMARY, READ_LEVEL))
    weights = tuple(base_env.profile(GRAM_PRIMARY, MID_SLOT))
    pinned = [tuple(e.profile(GRAM_PRIMARY, READ_LEVEL)) for e in pinned_envs]
    residual = tuple(
        sp.cancel(p0[a] - sum((weights[x] * pinned[x][a]
                               for x in range(extent)), sp.Integer(0)))
        for a in range(extent))

    matrix, rhs = profile_system([p0], [pinned], extent, normalise=False)
    ranks = (exact_rank(matrix), exact_rank(matrix.row_join(rhs)))
    restoring, verified = solve_exact(matrix, rhs, extent)

    mid_rows = tuple(site.rows(MID_SLOT))
    local = herm(gaussian_inverse(sp.Matrix(
        extent, extent,
        lambda i, j: base_action[mid_rows[i], mid_rows[j]])))
    total = sum((local[i, i] for i in range(extent)), sp.Integer(0))
    candidates = (
        tuple(base_env.profile(GRAM_PRIMARY, MID_SLOT)),
        tuple(base_env.profile(GRAM_SECOND, MID_SLOT)),
        tuple(base_env.profile(GRAM_THIRD, MID_SLOT)),
        tuple(sp.cancel(local[i, i] / total) for i in range(extent)),
    )
    mismatches = tuple(
        any(sp.cancel(a - b) != 0 for a, b in zip(candidate, restoring))
        for candidate in candidates)
    return InstrumentFacts(
        site.tag, site.N, site.T, site.c, site.tstar, extent,
        tuple(site.rows(READ_LEVEL)), mid_rows, PIN_CELLS,
        all(v == 0 for v in residual),
        tuple(v != 0 for v in residual), sign_tuple(residual),
        sp.cancel(sum(residual, sp.Integer(0))),
        tuple(display(v) for v in residual),
        ranks, restoring,
        bool(verified
             and sp.cancel(sum(restoring, sp.Integer(0)) - sp.Integer(1)) == 0),
        all(v >= 0 for v in restoring),
        tuple(display(v) for v in restoring),
        mismatches, candidates)


def measure_contexts(site, base_env, pinned_envs, base_action,
                     pinned_actions) -> ContextFacts:
    """THE SIX TESTED CONTEXTS AND THE CLEAN PAIR.  The stack is built ONCE and
    then read three ways: whole, per context, and as the two-context clean
    pair."""
    extent = site.lx
    rows, rhs = [], []
    per_ranks, per_nonnegative, per_sum_one = {}, [], []
    for family in CONTEXT_FAMILIES:
        for level in CONTEXT_LEVELS:
            base = tuple(base_env.profile(family, level))
            pinned = [tuple(e.profile(family, level)) for e in pinned_envs]
            block, target = profile_system([base], [pinned], extent)
            per_ranks[(family, level)] = (
                exact_rank(block), exact_rank(block.row_join(target)))
            solution, verified = solve_exact(block, target, extent)
            per_nonnegative.append(all(v >= 0 for v in solution))
            per_sum_one.append(bool(
                verified and sp.cancel(
                    sum(solution, sp.Integer(0)) - sp.Integer(1)) == 0))
            for index in range(extent):
                rows.append([block[index, c] for c in range(extent)])
                rhs.append(target[index])
    rows.append([sp.Integer(1)] * extent)
    rhs.append(sp.Integer(1))
    stack, stack_rhs = sp.Matrix(rows), sp.Matrix(rhs)
    stack_ranks = (exact_rank(stack), exact_rank(stack.row_join(stack_rhs)))

    read_rows = tuple(site.rows(READ_LEVEL))
    delta = tuple(
        sum(1 for i in read_rows for j in range(site.N)
            if sp.expand(action[i, j] - base_action[i, j]) != 0)
        for action in pinned_actions)

    pair_rows, pair_rhs = [], []
    individual = []
    for family in CONTEXT_FAMILIES:
        base = tuple(base_env.profile(family, READ_LEVEL))
        pinned = [tuple(e.profile(family, READ_LEVEL)) for e in pinned_envs]
        block, target = profile_system([base], [pinned], extent)
        individual.append(
            (exact_rank(block), exact_rank(block.row_join(target))))
        for index in range(extent):
            pair_rows.append([block[index, c] for c in range(extent)])
            pair_rhs.append(target[index])
    pair_rows.append([sp.Integer(1)] * extent)
    pair_rhs.append(sp.Integer(1))
    pair, pair_target = sp.Matrix(pair_rows), sp.Matrix(pair_rhs)
    pair_ranks = (exact_rank(pair), exact_rank(pair.row_join(pair_target)))
    return ContextFacts(
        stack.shape, stack_ranks, stack_ranks[0] == stack_ranks[1], per_ranks,
        tuple(per_nonnegative), tuple(per_sum_one), delta, tuple(individual),
        pair.shape, pair_ranks, pair_ranks[0] == pair_ranks[1])


def three_level_ranks(site, base_env, pinned_envs) -> tuple:
    extent = site.lx
    rows, rhs = [], []
    for level in CONTEXT_LEVELS:
        base = tuple(base_env.profile(GRAM_PRIMARY, level))
        pinned = [tuple(e.profile(GRAM_PRIMARY, level)) for e in pinned_envs]
        block, target = profile_system([base], [pinned], extent,
                                       normalise=False)
        for index in range(block.rows):
            rows.append([block[index, c] for c in range(extent)])
            rhs.append(target[index])
    rows.append([sp.Integer(1)] * extent)
    rhs.append(sp.Integer(1))
    stack, target = sp.Matrix(rows), sp.Matrix(rhs)
    return (exact_rank(stack), exact_rank(stack.row_join(target)))


def measure_hermitian(site, base_env, pinned_envs, base_action,
                      pinned_actions) -> HermitianFacts:
    """THE HERMITIZATION DEGENERACY, AND THE ABLATION IS SYMMETRIC.  herm() is
    applied AFTER record substitution, so the ablated bench carries exactly the
    same record contamination as the real one and the only difference between
    the two is the anti-Hermitian part."""
    anti = residual_count(sp.Matrix(base_action) - herm(base_action))
    hermitised_base = b171.Env(site, herm(base_action), "hb")
    hermitised_pinned = [
        b171.Env(site, herm(action), f"hp{x}")
        for x, action in enumerate(pinned_actions)]
    equal = tuple(
        tuple(env.profile(GRAM_PRIMARY, READ_LEVEL))
        == tuple(env.profile(GRAM_SECOND, READ_LEVEL))
        for env in [hermitised_base] + hermitised_pinned)
    return HermitianFacts(
        anti, equal,
        three_level_ranks(site, base_env, pinned_envs),
        three_level_ranks(site, hermitised_base, hermitised_pinned))


def measure_sweep(site) -> SweepFacts:
    """THE PHASE SWEEP, ON THE COMMITTED HOLONOMY ACTION AT THE COMMITTED
    SPATIAL DIAL.  The temporal dial changes one selected link contribution,
    while the complex spatial dial is held fixed.  Consequently q -> -q is
    not assumed to conjugate the full action; that mismatch is measured below.
    The residual at each q uses the same declared profile construction as C."""
    extent = site.lx
    dial = {b171.GRE: SPATIAL_DIAL_REAL, b171.GIM: SPATIAL_DIAL_IMAGINARY}
    probe = sp.Matrix(site.Q_holo_t.subs(
        site.sub(records={}, sx=TEMPORAL_DIAL_VALUES[0])))
    undialled = len(probe.free_symbols)
    dialled = len(sp.Matrix(probe.subs(dial)).free_symbols)

    def action(records, q):
        return sp.Matrix(
            site.Q_holo_t.subs(site.sub(records=dict(records), sx=q)).subs(dial))

    sweep, unit_envs = {}, []
    for q in TEMPORAL_DIAL_VALUES:
        base = b171.Env(site, action({}, q), f"q{q}")
        pinned = [b171.Env(site, action({(MID_SLOT, x): sp.Integer(0)}, q),
                           f"q{q}p{x}") for x in range(extent)]
        p0 = tuple(base.profile(GRAM_PRIMARY, READ_LEVEL))
        weights = tuple(base.profile(GRAM_PRIMARY, MID_SLOT))
        conditioned = [tuple(e.profile(GRAM_PRIMARY, READ_LEVEL))
                       for e in pinned]
        sweep[q] = tuple(
            sp.cancel(p0[a] - sum((weights[x] * conditioned[x][a]
                                   for x in range(extent)), sp.Integer(0)))
            for a in range(extent))
        if q == sp.Rational(1):
            unit_envs = [base] + pinned

    # THE STRUCTURAL HALF, AND IT IS WHY AN INTENSITY-ONLY RESPONSE WOULD BE
    # EVEN.  For any invertible Q, conj(Q)^-1 = conj(Q^-1); every W9 weight is
    # the real part of a diagonal entry of Q^-1, so it cannot see a global
    # conjugation.  Checked here as an exact instance at q = 1, on the base and
    # on all four pinned actions, at EVERY level.
    conjugation = []
    for env in unit_envs:
        conjugated = b171.Env(
            site,
            sp.Matrix(env.Q).applyfunc(sp.conjugate).applyfunc(sp.expand),
            "cj")
        conjugation.append(all(
            tuple(env.profile(GRAM_PRIMARY, level))
            == tuple(conjugated.profile(GRAM_PRIMARY, level))
            for level in range(site.T)))

    # Global conjugation is a valid algebraic comparison, but it is not the
    # q -> -q transformation at the fixed complex spatial dial.  Count the
    # exact entrywise mismatch on the base action and all four substitutions.
    q_flip_conjugation_residuals = tuple(
        residual_count(
            action(records, -sp.Integer(1))
            - action(records, sp.Integer(1)).applyfunc(sp.conjugate)
              .applyfunc(sp.expand))
        for records in ({},) + tuple(
            {(MID_SLOT, x): sp.Integer(0)} for x in range(extent)))

    odd_nonzero, odd_signs, odd_display, even_display = [], [], [], []
    for magnitude in ODD_MAGNITUDES:
        odd = tuple(sp.cancel((sweep[magnitude][a] - sweep[-magnitude][a]) / 2)
                    for a in range(extent))
        even = tuple(sp.cancel((sweep[magnitude][a] + sweep[-magnitude][a]) / 2)
                     for a in range(extent))
        odd_nonzero.append(tuple(v != 0 for v in odd))
        odd_signs.append(sign_tuple(odd))
        odd_display.append(tuple(display(v) for v in odd))
        even_display.append(tuple(display(v) for v in even))

    changes, zeros = [], []
    for component in range(extent):
        sequence = [sp.sign(sweep[q][component]) for q in TEMPORAL_DIAL_VALUES
                    if sweep[q][component] != 0]
        changes.append(sum(1 for i in range(1, len(sequence))
                           if sequence[i] != sequence[i - 1]))
        zeros.append(sum(1 for q in TEMPORAL_DIAL_VALUES
                         if sweep[q][component] == 0))
    return SweepFacts(
        undialled, dialled, tuple(conjugation),
        q_flip_conjugation_residuals,
        {q: sign_tuple(sweep[q]) for q in TEMPORAL_DIAL_VALUES}, tuple(zeros),
        {q: tuple(display(v) for v in sweep[q]) for q in TEMPORAL_DIAL_VALUES},
        tuple(odd_nonzero), tuple(odd_signs), tuple(odd_display),
        tuple(even_display), tuple(changes))


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() \
        else ""
    site = b171.Site(BENCH_TAG, BENCH_COVER, BENCH_LX)

    def action(records):
        return sp.Matrix(site.bench.Q.subs(site.sub(records=dict(records))))

    # THE ONE MEASUREMENT PASS.  Five committed actions and five hermitized
    # ones are built here and shared by families C, D and E; family F builds
    # its own thirty-five holonomy actions.  Nothing below is recomputed.
    base_action = action({})
    pinned_actions = [action({(MID_SLOT, x): sp.Integer(0)})
                      for x in range(site.lx)]
    base_env = b171.Env(site, base_action, "b")
    pinned_envs = [b171.Env(site, act, f"p{x}")
                   for x, act in enumerate(pinned_actions)]
    return Facts(
        main_head,
        authority_certificate(main_head),
        len(IMPOSED_OBJECTS),
        len(REGISTERED_OBJECTS),
        len(ADOPTED_OBJECTS),
        len(UNSUPPLIED_GRAVITY_STRUCTURES),
        len(READINGS),
        len(UNNAMED_PHYSICS_WORDS),
        measure_instrument(site, base_env, pinned_envs, base_action),
        measure_contexts(site, base_env, pinned_envs, base_action,
                         pinned_actions),
        measure_hermitian(site, base_env, pinned_envs, base_action,
                          pinned_actions),
        measure_sweep(site),
        scope_certificate(note_text),
        nsimplify_occurrences(),
        float_literal_occurrences(),
        float_call_sites())


# ---------------------------------------------------------------------------
# THE CLAIMS.  Every one of them is a literal, and a mutation rewrites exactly
# one of them.  No measurement is taken here.
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims = {
        # A
        "main_head": CURRENT_MAIN,
        "parent_commit": PARENT_COMMIT,
        "stale_parent": STALE_PARENT_COMMIT,
        # B
        "imposed": len(IMPOSED_OBJECTS),
        "registered": 0,
        "adopted": 0,
        "gravity_supplied": GRAVITY_SUPPLIED_CLAIMED,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
        "pinning_is_measurement": PINNING_IS_MEASUREMENT_CLAIMED,
        "record_formation_law": RECORD_FORMATION_LAW_CLAIMED,
        "quantum_bound_violation": QUANTUM_BOUND_VIOLATION_CLAIMED,
        "classical_no_go": CLASSICAL_NO_GO_CLAIMED,
        "generic_parameter_theorem": GENERIC_PARAMETER_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "unnamed_words": len(UNNAMED_PHYSICS_WORDS),
        "readings": len(READINGS),
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C
        "bench_metadata": (BENCH_TAG, BENCH_N, BENCH_T, BENCH_CORE,
                           BENCH_TSTAR, BENCH_LX),
        "read_rows": READ_ROWS,
        "mid_rows": MID_ROWS,
        "pin_cells": PIN_CELLS,
        "identity_holds": MIXTURE_IDENTITY_HOLDS,
        "residual_nonzero": MIXTURE_RESIDUAL_NONZERO,
        "residual_signs": MIXTURE_RESIDUAL_SIGNS,
        "residual_sum": MIXTURE_RESIDUAL_SUM,
        "restoring_ranks": RESTORING_RANKS,
        "restoring_weight": RESTORING_WEIGHT,
        "restoring_sum_is_one": RESTORING_SUM_IS_ONE,
        "restoring_nonnegative": RESTORING_NONNEGATIVE,
        "candidate_mismatches": CANDIDATE_MISMATCHES,
        # D
        "stack_shape": STACK_SHAPE,
        "stack_ranks": STACK_RANKS,
        "common_exists": COMMON_WEIGHT_EXISTS,
        "per_context_ranks": dict(PER_CONTEXT_RANKS),
        "per_context_nonnegative": PER_CONTEXT_NONNEGATIVE,
        "per_context_sum_is_one": PER_CONTEXT_SUM_IS_ONE,
        "read_row_block_delta": READ_ROW_BLOCK_DELTA,
        "clean_pair_individual": CLEAN_PAIR_INDIVIDUAL_RANKS,
        "clean_pair_shape": CLEAN_PAIR_STACK_SHAPE,
        "clean_pair_ranks": CLEAN_PAIR_STACK_RANKS,
        "clean_pair_consistent": CLEAN_PAIR_CONSISTENT,
        # E
        "anti_hermitian_nnz": ANTI_HERMITIAN_NNZ,
        "w9_equals_w2": HERMITISED_W9_EQUALS_W2,
        "non_hermiticity_necessary": NON_HERMITICITY_IS_NECESSARY,
        "real_three_level": REAL_THREE_LEVEL_RANKS,
        "hermitised_three_level": HERMITISED_THREE_LEVEL_RANKS,
        "survives_hermitisation": ACROSS_LEVEL_SURVIVES_HERMITISATION,
        # F
        "undialled_symbols": UNDIALLED_FREE_SYMBOLS,
        "dialled_symbols": DIALLED_FREE_SYMBOLS,
        "conjugation_invariant": CONJUGATION_INVARIANT,
        "q_flip_conjugation_residuals": Q_FLIP_CONJUGATION_RESIDUALS,
        "q_flip_is_conjugation": Q_FLIP_IS_GLOBAL_CONJUGATION,
        "sweep_signs": dict(SWEEP_SIGNS),
        "sampled_zeros": SWEEP_SAMPLED_ZEROS,
        "odd_nonzero": ODD_NONZERO,
        "odd_signs": ODD_SIGNS,
        "sign_changes": SIGN_CHANGES,
        "even_only_excluded": EVEN_ONLY_EXPLANATION_EXCLUDED,
        # G
        "joint_halves": len(JOINT_IDENTIFICATION_HALVES),
        "which_half_open": WHICH_HALF_FAILS_IS_OPEN,
        "outcome_dimension": OUTCOME_SPACE_DIMENSION_TESTED,
        "outcome_space_exhaustive": OUTCOME_SPACE_EXHAUSTIVE_CLAIMED,
        "untested_refinements": len(UNTESTED_OUTCOME_REFINEMENTS),
        "row_block_certificate_only": ROW_BLOCK_CERTIFICATE_ONLY,
        "causal_isolation": CAUSAL_ISOLATION_CLAIMED,
        "global_inverse": READOUT_USES_GLOBAL_INVERSE,
        "non_hermiticity_sufficient": NON_HERMITICITY_SUFFICIENT_CLAIMED,
        "phase_models_excluded": PHASE_SENSITIVE_MODELS_EXCLUDED_CLAIMED,
        "classical_models_open": len(CLASSICAL_MODELS_NOT_EXCLUDED),
        "instance_scope": INSTANCE_SCOPE_COUNT,
        "scope_generalisation": SCOPE_GENERALISATION_CLAIMED,
        # H
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
        "float_literals": 0,
        "float_calls": 1,
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
    elif mutation == "claim_pinning_is_measurement":
        # THE FIRST MISREAD: writing a class value into four cells of the
        # committed carrier is asserted to BE a measurement process.  It is a
        # substitution in a rational matrix.
        claims["pinning_is_measurement"] = True
    elif mutation == "claim_record_formation_law":
        # THE CHECK'S C6.1 DELETED: the mixture failure is asserted to be a
        # general fact about RECORD FORMATION.  It indicts a JOINT
        # identification and says nothing about which half fails.
        claims["record_formation_law"] = True
    elif mutation == "claim_diagnostic_is_quantum":
        # THE WORD THE PACKAGE DOES NOT EARN: a quantum-bound violation is
        # asserted.  No Bell, Leggett-Garg or noncontextuality bound is even
        # formulated here, let alone violated.
        claims["quantum_bound_violation"] = True
        claims["unnamed_words"] = 0
    elif mutation == "claim_classical_no_go":
        # THE OVERREACH IN ITS STRONGEST FORM: a general classical no-go is
        # asserted from six tested contexts on one bench.
        claims["classical_no_go"] = True
        claims["generic_parameter_theorem"] = True
        claims["continuum_limit"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_bench_instrument":
        claims["bench_metadata"] = (BENCH_TAG, BENCH_N, BENCH_T, BENCH_CORE,
                                    BENCH_TSTAR, 3)
    elif mutation == "break_mixture_failure":
        # THE HEADLINE DENIED: the mixture identity is asserted to HOLD, which
        # is exactly what a tolerance-carrying simplification would produce
        # from four residuals of size 1e-4.
        claims["identity_holds"] = True
        claims["residual_nonzero"] = (False, False, False, False)
        claims["residual_signs"] = ("0", "0", "0", "0")
    elif mutation == "break_restoring_weight":
        claims["restoring_ranks"] = (3, 4)
        claims["restoring_nonnegative"] = False
    elif mutation == "break_candidate_mismatch":
        # THE NATIVE WEIGHT REINSTATED: W9(mid) is asserted to BE the restoring
        # weight, which would make the failure a bookkeeping slip.
        claims["candidate_mismatches"] = (False, True, True, True)
    # --- D ----------------------------------------------------------------
    elif mutation == "break_no_common_weight":
        claims["stack_ranks"] = (4, 4)
        claims["common_exists"] = True
    elif mutation == "break_per_context_solvability":
        # THE OTHER HALF OF THE SAME STATEMENT: if a single context were also
        # unsolvable, the six-context inconsistency would carry no information
        # about CONTEXT at all.
        claims["per_context_ranks"] = dict(PER_CONTEXT_RANKS)
        claims["per_context_ranks"][("W2", 2)] = (4, 5)
    elif mutation == "break_clean_pair":
        claims["read_row_block_delta"] = (1, 1, 1, 1)
        claims["clean_pair_ranks"] = (4, 4)
        claims["clean_pair_consistent"] = True
    # --- E ----------------------------------------------------------------
    elif mutation == "break_hermitized_degeneracy":
        claims["w9_equals_w2"] = (False, False, False, False, False)
        claims["non_hermiticity_necessary"] = False
    elif mutation == "break_across_level_inconsistency":
        # THE ABLATION MISREPORTED: hermitization is asserted to REMOVE the
        # across-level inconsistency, which would make the anti-Hermitian part
        # the source of the whole package.  It does not.
        claims["hermitised_three_level"] = (4, 4)
        claims["survives_hermitisation"] = False
    # --- F ----------------------------------------------------------------
    elif mutation == "break_committed_dial":
        # THE CORRECTED INSTRUMENT UN-CORRECTED: the action is asserted to be
        # symbol-free before the committed dial is applied, which is the exact
        # error that killed this probe's first firing.
        claims["undialled_symbols"] = 0
    elif mutation == "claim_q_flip_is_conjugation":
        claims["q_flip_is_conjugation"] = True
    elif mutation == "break_odd_response":
        # The measured non-even response is denied without adding a mechanism.
        claims["odd_nonzero"] = ((False, False, False, False),) * 3
        claims["even_only_excluded"] = True
    elif mutation == "break_sign_changes":
        claims["sign_changes"] = (0, 0, 0, 0)
    # --- G ----------------------------------------------------------------
    elif mutation == "break_joint_identification_fence":
        claims["which_half_open"] = False
        claims["joint_halves"] = 1
    elif mutation == "claim_outcome_space_exhaustive":
        # THE CHECK'S C6.2 DELETED: the four-component outcome space is
        # asserted to be exhaustive, so that 'no common w' would become 'no
        # classical model'.  The record class-value dimension alone refutes it.
        claims["outcome_space_exhaustive"] = True
        claims["untested_refinements"] = 0
    elif mutation == "claim_causal_isolation":
        # THE CHECK'S C6.3 DELETED: the row-block certificate is promoted to
        # causal isolation, ignoring that the readout inverts the WHOLE matrix.
        claims["causal_isolation"] = True
        claims["row_block_certificate_only"] = False
        claims["global_inverse"] = False
    elif mutation == "claim_non_hermiticity_sufficient":
        # THE CHECK'S C6.4 DELETED: necessity is silently upgraded to
        # sufficiency, against a measured survival at identical ranks.
        claims["non_hermiticity_sufficient"] = True
    elif mutation == "claim_phase_models_excluded":
        # A response-model exclusion is asserted even though q flip is not the
        # global-conjugation comparison required for that interpretation.
        claims["phase_models_excluded"] = True
        claims["classical_models_open"] = 0
    elif mutation == "break_instance_scope":
        claims["instance_scope"] = 0
    # --- H ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    elif mutation == "break_float_absence":
        claims["float_literals"] = 1
        claims["float_calls"] = 2
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    instrument = facts.instrument
    contexts = facts.contexts
    hermitian = facts.hermitian
    sweep = facts.sweep

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 201 artifacts are "
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
        "B-3", "THE WORD *PINNING* IS SCOPED BEFORE THE FIRST NUMERAL: it "
        "names a SUBSTITUTION of the committed modulus map at four cells of "
        "the carrier field, and names NO measurement process, NO collapse, NO "
        "state update and NO physical intervention",
        claims["pinning_is_measurement"] is False)
    checks.check(
        "B-4", "THE WORD *MIXTURE* IS SCOPED: it names ONE "
        "law-of-total-probability identity under ONE JOINT identification -- "
        "the pins read as conditionals of a common joint law AND the native "
        "mid-slice weights read as formation weights -- and its failure says "
        "those cannot BOTH hold, never which one fails and never anything "
        "general about record formation in this framework",
        claims["record_formation_law"] is False)
    checks.check(
        "B-5", f"THE WORD *DIAGNOSTIC* IS SCOPED: the licensed phrase is "
        f"'{LICENSED_PHRASE}', and the {claims['unnamed_words']} words "
        f"{UNNAMED_PHYSICS_WORDS} name NOTHING established here -- no Bell, "
        f"Leggett-Garg or noncontextuality bound is formulated by any line of "
        f"this block, so none is violated",
        claims["quantum_bound_violation"] is False
        and facts.unnamed_words == claims["unnamed_words"])
    checks.check(
        "B-6", "NO GENERAL CLASSICAL NO-GO, NO GENERIC-PARAMETER THEOREM AND "
        "NO CONTINUUM LIMIT: what is established is a set of exact "
        "finite-instance predicates on ONE bench, and six tested contexts are "
        "not a parameter space and not a limit",
        claims["classical_no_go"] is False
        and claims["generic_parameter_theorem"] is False
        and claims["continuum_limit"] is False)
    checks.check(
        "B-7", f"THE READINGS ARE READINGS: {claims['readings']} of them are "
        f"enumerated as readings, readings_licensed = "
        f"{claims['readings_licensed']}, and EVERY NEGATIVE HERE IS NON-SUPPLY "
        f"WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the "
        f"cycle-913 caution, carried verbatim, with nothing registered and "
        f"nothing adopted",
        facts.readings == claims["readings"]
        and claims["readings_licensed"] is False
        and not REGISTERED_OBJECTS and not ADOPTED_OBJECTS
        and claims["registered"] == 0 and claims["adopted"] == 0)

    # --- C: THE INSTRUMENT AND THE MIXTURE FAILURE --------------------------
    checks.check(
        "C-1", f"THE SUBSTITUTION TEST USES BLOCK 171's OWN BENCH, READ THROUGH ITS OWN "
        f"Site AND Env CLASSES: {claims['bench_metadata']} for "
        f"(tag, N, T, c, tstar, lx), readout rows {claims['read_rows']} at "
        f"level {READ_LEVEL}, pinned rows {claims['mid_rows']} at slot "
        f"{MID_SLOT}, and the four class-{RECORD_CLASS_VALUE} pin cells "
        f"{claims['pin_cells']}",
        (instrument.tag, instrument.size, instrument.width, instrument.core,
         instrument.tstar, instrument.extent) == claims["bench_metadata"]
        and instrument.read_rows == claims["read_rows"]
        and instrument.mid_rows == claims["mid_rows"]
        and instrument.pin_cells == claims["pin_cells"])
    checks.check(
        "C-2", f"THE MIXTURE IDENTITY FAILS, EXACTLY AND IN EVERY COMPONENT: "
        f"P0 - sum_x w_x P_x has nonzero components "
        f"{claims['residual_nonzero']} with the exact sign pattern "
        f"{claims['residual_signs']}, it sums to EXACTLY "
        f"{claims['residual_sum']}, and identity_holds = "
        f"{claims['identity_holds']} -- displays {instrument.residual_display}",
        instrument.identity_holds is claims["identity_holds"]
        and claims["identity_holds"] is False
        and instrument.residual_nonzero == claims["residual_nonzero"]
        and all(claims["residual_nonzero"])
        and instrument.residual_signs == claims["residual_signs"]
        and instrument.residual_sum == claims["residual_sum"])
    checks.check(
        "C-3", f"A UNIQUE RESTORING FOUR-WEIGHT EXISTS AND IT IS A PROBABILITY "
        f"VECTOR: the 4 x 4 outcome system has ranks {claims['restoring_ranks']}"
        f" so the solution is unique, sum(w) = 1 exactly "
        f"({claims['restoring_sum_is_one']}) with every component nonnegative "
        f"({claims['restoring_nonnegative']}), and the four exact rationals are "
        f"carried as literals -- displays {instrument.restoring_display}",
        instrument.restoring_ranks == claims["restoring_ranks"]
        and claims["restoring_ranks"] == (BENCH_LX, BENCH_LX)
        and instrument.restoring_sum_is_one is claims["restoring_sum_is_one"]
        and instrument.restoring_nonnegative is claims["restoring_nonnegative"]
        and claims["restoring_sum_is_one"] is True
        and claims["restoring_nonnegative"] is True
        and len(instrument.restoring_weight) == len(claims["restoring_weight"])
        and all(sp.cancel(a - b) == 0 for a, b
                in zip(instrument.restoring_weight,
                       claims["restoring_weight"])))
    checks.check(
        "C-4", f"AND IT IS NONE OF THE PROPOSED NATIVE WEIGHTS: the exact "
        f"difference against each of {CANDIDATE_NAMES} is nonzero, at "
        f"mismatches {claims['candidate_mismatches']}",
        instrument.candidate_mismatches == claims["candidate_mismatches"]
        and all(claims["candidate_mismatches"])
        and len(instrument.candidate_values) == len(CANDIDATE_NAMES))

    # --- D: THE SIX CONTEXTS AND THE CLEAN PAIR -----------------------------
    checks.check(
        "D-1", f"NO COMMON FOUR-WEIGHT SPANS THE SIX TESTED CONTEXTS: the "
        f"stack is {claims['stack_shape']} -- "
        f"{len(CONTEXT_FAMILIES)} families x {len(CONTEXT_LEVELS)} levels x "
        f"{BENCH_LX} components plus one normalisation row -- with rank A = "
        f"{claims['stack_ranks'][0]} and rank [A|b] = "
        f"{claims['stack_ranks'][1]}, so common_exists = "
        f"{claims['common_exists']}",
        contexts.stack_shape == claims["stack_shape"]
        and contexts.stack_ranks == claims["stack_ranks"]
        and claims["stack_ranks"][0] != claims["stack_ranks"][1]
        and contexts.common_exists is claims["common_exists"]
        and claims["common_exists"] is False)
    checks.check(
        "D-2", f"AND EVERY SINGLE CONTEXT ALONE IS SOLVABLE, WHICH IS WHAT "
        f"MAKES THE STACK A STATEMENT ABOUT CONTEXT: all "
        f"{CONTEXT_COUNT} of the (family, level) systems have ranks "
        f"{claims['per_context_ranks'][('W9', 5)]}, each with a nonnegative "
        f"weight {claims['per_context_nonnegative']} summing to one "
        f"{claims['per_context_sum_is_one']}",
        contexts.per_context_ranks == claims["per_context_ranks"]
        and len(claims["per_context_ranks"]) == CONTEXT_COUNT
        and all(value == (BENCH_LX, BENCH_LX)
                for value in claims["per_context_ranks"].values())
        and contexts.per_context_nonnegative
        == claims["per_context_nonnegative"]
        and contexts.per_context_sum_is_one == claims["per_context_sum_is_one"]
        and all(claims["per_context_nonnegative"])
        and all(claims["per_context_sum_is_one"]))
    checks.check(
        "D-3", f"THE CLEAN PAIR: the record at slot {MID_SLOT} changes "
        f"{claims['read_row_block_delta']} entries of the slot-{READ_LEVEL} "
        f"row block of Q at the four substitutions -- a ROW-BLOCK CERTIFICATE and "
        f"NEVER causal isolation -- while W9-L5 and W2-L5 have individual ranks "
        f"{claims['clean_pair_individual']} and their "
        f"{claims['clean_pair_shape']} stack has ranks "
        f"{claims['clean_pair_ranks']}, so clean_pair_consistent = "
        f"{claims['clean_pair_consistent']}",
        contexts.read_row_block_delta == claims["read_row_block_delta"]
        and all(value == ZERO_RESIDUAL
                for value in claims["read_row_block_delta"])
        and contexts.clean_pair_individual == claims["clean_pair_individual"]
        and contexts.clean_pair_shape == claims["clean_pair_shape"]
        and contexts.clean_pair_ranks == claims["clean_pair_ranks"]
        and claims["clean_pair_ranks"][0] != claims["clean_pair_ranks"][1]
        and contexts.clean_pair_consistent is claims["clean_pair_consistent"]
        and claims["clean_pair_consistent"] is False)

    # --- E: THE HERMITIZATION DEGENERACY ------------------------------------
    checks.check(
        "E-1", f"ON THIS DECLARED MATRIX CONSTRUCTION, HERMITIZATION MAKES THE "
        f"TWO GRAMS COINCIDE: the anti-Hermitian part of the committed action "
        f"carries {claims['anti_hermitian_nnz']} nonzero entries, and with herm "
        f"applied AFTER record substitution W9 == W2 at level {READ_LEVEL} "
        f"identically on the base bench and at all four substitutions "
        f"{claims['w9_equals_w2']}.  This is a scoped algebraic implication, "
        f"not a physical source claim",
        hermitian.anti_hermitian_nnz == claims["anti_hermitian_nnz"]
        and claims["anti_hermitian_nnz"] > 0
        and hermitian.w9_equals_w2 == claims["w9_equals_w2"]
        and all(claims["w9_equals_w2"])
        and claims["non_hermiticity_necessary"] is True)
    checks.check(
        "E-2", f"THE SEPARATE W9 THREE-LEVEL RANK MISMATCH SURVIVES THE "
        f"SPECIFIED HERMITIZATION: the stack over levels "
        f"{CONTEXT_LEVELS} has ranks {claims['real_three_level']} on the real "
        f"bench and {claims['hermitised_three_level']} on the hermitized one, "
        f"BOTH inconsistent, so survives_hermitisation = "
        f"{claims['survives_hermitisation']}.  No wider necessity or "
        f"sufficiency statement is inferred",
        hermitian.real_three_level == claims["real_three_level"]
        and hermitian.hermitised_three_level
        == claims["hermitised_three_level"]
        and claims["real_three_level"][0] != claims["real_three_level"][1]
        and claims["hermitised_three_level"][0]
        != claims["hermitised_three_level"][1]
        and claims["survives_hermitisation"] is True)

    # --- F: THE PHASE SWEEP -------------------------------------------------
    checks.check(
        "F-1", f"THE INSTRUMENT IS PINNED BEFORE IT IS FIRED, AND THE PIN IS "
        f"MEASURED: the holonomy action carries {claims['undialled_symbols']} "
        f"free symbols before the COMMITTED spatial dial "
        f"{{g_re: {SPATIAL_DIAL_REAL}, g_im: {SPATIAL_DIAL_IMAGINARY}}} is "
        f"applied and {claims['dialled_symbols']} after it, so every inverse "
        f"below is taken over QQ_I and never symbolically",
        sweep.undialled_symbols == claims["undialled_symbols"]
        and claims["undialled_symbols"] > 0
        and sweep.dialled_symbols == claims["dialled_symbols"]
        and claims["dialled_symbols"] == 0)
    checks.check(
        "F-2", f"GLOBAL CONJUGATION AND q -> -q ARE DISTINCT TRANSFORMATIONS "
        f"ON THIS FIXED COMPLEX BACKGROUND: conjugating ALL links leaves EVERY "
        f"W9 profile exactly invariant at every one of the {BENCH_T} levels, on "
        f"the base action and at all four pins {claims['conjugation_invariant']}"
        f" -- each W9 weight is the real part of a diagonal entry of Q^-1 and "
        f"conj(Q)^-1 = conj(Q^-1).  But the entrywise residual counts between "
        f"Q(-1) and conj(Q(1)) are "
        f"{claims['q_flip_conjugation_residuals']}, so "
        f"q_flip_is_conjugation = {claims['q_flip_is_conjugation']}",
        sweep.conjugation_invariant == claims["conjugation_invariant"]
        and all(claims["conjugation_invariant"])
        and sweep.q_flip_conjugation_residuals
        == claims["q_flip_conjugation_residuals"]
        and all(value > 0 for value in claims["q_flip_conjugation_residuals"])
        and claims["q_flip_is_conjugation"] is False)
    checks.check(
        "F-3", f"THE FIXED-BACKGROUND q RESPONSE IS EXACTLY NON-EVEN AT EVERY "
        f"MAGNITUDE: (R(q) - R(-q))/2 has nonzero components "
        f"{claims['odd_nonzero']} with sign patterns {claims['odd_signs']} at "
        f"|q| in {tuple(str(m) for m in ODD_MAGNITUDES)}.  Because F-2 shows "
        f"that q flip is not global conjugation, even_only_excluded remains "
        f"{claims['even_only_excluded']} and no phase or intensity mechanism "
        f"is inferred -- displays {sweep.odd_displays}",
        sweep.odd_nonzero == claims["odd_nonzero"]
        and all(all(row) for row in claims["odd_nonzero"])
        and len(claims["odd_nonzero"]) == len(ODD_MAGNITUDES)
        and sweep.odd_signs == claims["odd_signs"]
        and claims["even_only_excluded"] is False)
    checks.check(
        "F-4", f"AND THE SWEEP ITSELF IS SIGN-RESOLVED: the seven sampled "
        f"residuals carry the sign patterns {claims['sweep_signs']} with "
        f"{claims['sampled_zeros']} exact zeros among the sampled values, and "
        f"component 0 changes sign exactly {claims['sign_changes'][0]} times "
        f"across the sweep while the others change "
        f"{claims['sign_changes'][1:]}",
        sweep.signs == claims["sweep_signs"]
        and len(claims["sweep_signs"]) == len(TEMPORAL_DIAL_VALUES)
        and sweep.sampled_zeros == claims["sampled_zeros"]
        and all(value == 0 for value in claims["sampled_zeros"])
        and sweep.sign_changes == claims["sign_changes"]
        and claims["sign_changes"][0] > 0)

    # --- G: THE SIX SCOPE FENCES -------------------------------------------
    checks.check(
        "G-1", f"FENCE ONE -- THE FAILURE INDICTS THE JOINT IDENTIFICATION AND "
        f"NOTHING NARROWER: {claims['joint_halves']} halves are named "
        f"({JOINT_IDENTIFICATION_HALVES}), and which of them fails is OPEN "
        f"({claims['which_half_open']}); the companion statement that NO "
        f"general record-formation law is claimed is gated separately at B-4, "
        f"so neither leans on the other",
        claims["joint_halves"] == len(JOINT_IDENTIFICATION_HALVES)
        and claims["joint_halves"] == 2
        and claims["which_half_open"] is True)
    checks.check(
        "G-2", f"FENCE TWO -- 'NO COMMON w' EXCLUDES "
        f"{claims['outcome_dimension']}-COMPONENT WEIGHTS OVER THE "
        f"{CONTEXT_COUNT} TESTED CONTEXTS ONLY: "
        f"outcome_space_exhaustive = {claims['outcome_space_exhaustive']} and "
        f"{claims['untested_refinements']} richer classical outcome spaces are "
        f"named as NOT excluded, the record class-value dimension first among "
        f"them",
        claims["outcome_space_exhaustive"] is False
        and claims["outcome_dimension"] == BENCH_LX
        and claims["untested_refinements"] == len(UNTESTED_OUTCOME_REFINEMENTS)
        and claims["untested_refinements"] > 0)
    checks.check(
        "G-3", f"FENCE THREE -- 'UNTOUCHED READOUT' IS A ROW-BLOCK CERTIFICATE "
        f"AND NEVER ISOLATION: row_block_certificate_only = "
        f"{claims['row_block_certificate_only']}, causal_isolation = "
        f"{claims['causal_isolation']}, and the readout uses the GLOBAL inverse "
        f"of a globally changed Q ({claims['global_inverse']}), so a change "
        f"outside the {READ_LEVEL}-slot rows can and does move it",
        claims["row_block_certificate_only"] is True
        and claims["causal_isolation"] is False
        and claims["global_inverse"] is True)
    checks.check(
        "G-4", f"FENCE FOUR -- HERMITIZATION CLAIMS ARE RESTRICTED TO THE "
        f"SPECIFIED MATRIX REPLACEMENT AND SELECTED PROFILES: "
        f"non_hermiticity_sufficient = "
        f"{claims['non_hermiticity_sufficient']}, so the anti-Hermitian part is "
        f"no physical source and no uniquely quantum meaning is supplied for "
        f"it; the coincident profiles and surviving hermitized ranks are "
        f"gated separately at E-1 and E-2, so neither leans on the other",
        claims["non_hermiticity_sufficient"] is False)
    checks.check(
        "G-5", f"FENCE FIVE -- THE q SWEEP IS A FIXED-BACKGROUND PARAMETER "
        f"COMPARISON, NOT A CONJUGATION OR PHASE CERTIFICATE: "
        f"phase_models_excluded = "
        f"{claims['phase_models_excluded']}, {claims['classical_models_open']} "
        f"classes of response model are named as still open, and the ONLY "
        f"licensed phrase for the package is '{LICENSED_PHRASE}'; the words "
        f"{UNNAMED_PHYSICS_WORDS} name nothing established here and are gated "
        f"separately at B-5 and B-6, so neither leans on the other",
        claims["phase_models_excluded"] is False
        and claims["classical_models_open"]
        == len(CLASSICAL_MODELS_NOT_EXCLUDED)
        and claims["classical_models_open"] > 0)
    checks.check(
        "G-6", f"FENCE SIX -- THE INSTANCE SCOPE, ENUMERATED RATHER THAN "
        f"GESTURED AT: {claims['instance_scope']} restrictions "
        f"({INSTANCE_SCOPE}), and scope_generalisation = "
        f"{claims['scope_generalisation']} -- NOT every extent, NOT every "
        f"carrier, NOT every slot, NOT every class value and NOT every dial; "
        f"the NO GRAVITY SUPPLIED banner and the registered/adopted counts are "
        f"gated separately at B-1 and B-2, so neither leans on the other",
        claims["instance_scope"] == len(INSTANCE_SCOPE)
        and claims["instance_scope"] == INSTANCE_SCOPE_COUNT
        and claims["instance_scope"] > 0
        and claims["scope_generalisation"] is False)

    # --- H: THE NOTE, THE FENCE AND THE EXACTNESS HYGIENE -------------------
    checks.check(
        "H-1", f"the note is present at {NOTE_PATH.name} and all five "
        f"substantive N5 resolution lines appear in it verbatim",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "H-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can turn a 1e-4 mixture residual into a spurious zero and "
        f"reinstate the very identity this block reports as FAILING",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "H-3", f"and {claims['float_literals']} float literals appear in that "
        f"same source with EXACTLY {claims['float_calls']} float call site, "
        f"both MEASURED by an AST walk rather than by a text search -- so every "
        f"decimal in this note is display-only and no verdict predicate "
        f"anywhere in this file consumes anything but an exact rational",
        facts.float_literals == claims["float_literals"]
        and facts.float_calls == claims["float_calls"])
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    instrument = facts.instrument
    contexts = facts.contexts
    hermitian = facts.hermitian
    sweep = facts.sweep
    print(f"MEASURED elapsed={elapsed_ns // 1000000000}s main={facts.main_head}")
    print(f"C residual_nonzero={instrument.residual_nonzero} "
          f"signs={instrument.residual_signs} restoring_ranks="
          f"{instrument.restoring_ranks} nonnegative="
          f"{instrument.restoring_nonnegative}")
    print(f"D stack={contexts.stack_shape}/{contexts.stack_ranks} "
          f"per_context={tuple(contexts.per_context_ranks.values())} "
          f"clean_pair={contexts.clean_pair_shape}/{contexts.clean_pair_ranks} "
          f"row_delta={contexts.read_row_block_delta}")
    print(f"E antiH_nnz={hermitian.anti_hermitian_nnz} "
          f"herm_W9_eq_W2={hermitian.w9_equals_w2} "
          f"three_level={hermitian.real_three_level}/"
          f"{hermitian.hermitised_three_level}")
    print(f"F q_conj_residuals={sweep.q_flip_conjugation_residuals} "
          f"odd_nonzero={sweep.odd_nonzero} odd_signs={sweep.odd_signs} "
          f"sign_changes={sweep.sign_changes}")
    print("SCOPE substitutions and weights are declared probes, not a supplied "
          "record instrument; q flip is not global conjugation; no physical "
          "or continuum interpretation is adopted")


N5_FENCE = "\n".join((
    "N5: per_element: Four class-0 cell substitutions and the native W9(mid) profile are declared finite algebraic probes. The Minimal Axioms do not supply an outcome instrument, conditional law, formation weights, measurement update, gravity variable, or continuum interpretation; nothing is registered or adopted.",
    "per_site: On Site(12x4,12,4), the declared W9-L5 mixture residual has four nonzero exact rational components with signs (+,-,+,+) and zero sum. The associated 4-by-4 system has ranks (4,4), a unique nonnegative unit-sum solution, and that solution differs from all four declared candidate profiles.",
    "per_mode: The six W9/W2 level profiles each admit a nonnegative unit-sum four-weight with ranks (4,4), while their 25-by-4 stack has ranks (4,5). This excludes only one common four-component coefficient vector for these declared profiles, not richer latent spaces or classical models.",
    "per_block: The selected slot-5 row block has exact substitution deltas (0,0,0,0), yet the clean W9-L5/W2-L5 stack has ranks (4,5); this is an entrywise row-block certificate, not causal isolation. After the specified hermitization W9-L5 equals W2-L5, while the separate W9 three-level stack remains rank-inconsistent.",
    "lattice_wide: At fixed spatial dial (1/3,1/4), the residual is non-even under q -> -q, but Q(-1)-conj(Q(1)) has exact nonzero-entry counts (96,92,92,92,92). Therefore q flip is not global conjugation here, no phase or intensity mechanism is selected, every claim remains finite-instance proposed_retained, and TOE movement is zero.",
))


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
