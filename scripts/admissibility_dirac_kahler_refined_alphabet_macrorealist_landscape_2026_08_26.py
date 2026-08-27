#!/usr/bin/env python3
"""BLOCK 210 -- FINITE REFINED-ALPHABET AND FOUR-FACET NULL DIAGNOSTICS.

On Block 171's declared bench, this runner measures a twelve-column
class-value refinement against six normalized marginal contexts.  The
single-context system is solvable at ranks (4,4), while the unit-sum real
six-context system has ranks (8,9) with an augmented pivot.  Six exact
normalization relations cap the 25-row coefficient rank at 19, so outcome count
alone supplies no threshold; every richer structured alphabet remains open.

For a proposed W9 formation-weight reading, the runner proves the four
deterministic dichotomic upper facets by an eight-assignment truth table and
evaluates all four on four chains and three balanced splits: 48 exact values.
It gates both sum-one and componentwise nonnegativity for every profile used.
The same calibration is applied at seven declared temporal-dial values.  Those
finite samples satisfy the bound, but no continuum-q or no-tuning conclusion is
drawn.

All content is finite exact algebra and proposed_retained only.  It does not
identify a physical joint law, establish macrorealism, exclude a classical
model, select an instrument, or supply dynamics, gravity, or a continuum limit.
Twenty-nine claim-only mutations each fail exactly their mapped family.
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
# profile differenced, stacked or correlated below is the LANDED construction
# and not a rebuild of it.
try:
    import admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21 as b171
    BENCH_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b171 = None
    BENCH_IMPORT_LANDED = False
MACHINERY_IMPORT_LANDED = BENCH_IMPORT_LANDED

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_REFINED_ALPHABET_MACROREALIST_LANDSCAPE_"
    "BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# ---------------------------------------------------------------------------
# REPINNED AT LANDING onto Block 209, which landed first on this stack.  The
# SCIENTIFIC parent remains Block 202 -- the block whose two named next
# instruments this block runs -- and its artifacts stay in AUDIT_INPUT_PATHS;
# the STACK parent is Block 209 and the stale pin is the Block 202 tip.
# Nothing else in this file moves: every measured number below is taken on
# Block 171's bench and is independent of the pin.
# ---------------------------------------------------------------------------
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_"
    "2026_08_26.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "3f18f8db768dbd803c2b040167415adba79dac2c",
    "af2672f13ba633bac9bcaabb393548e2d16a8915",
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_REFINED_ALPHABET_MACROREALIST_LANDSCAPE_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_record_pinning_mixture_diagnostics_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py",
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
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block209-"
              "three-direction-rule-geometry-20260826")
PARENT_COMMIT = "07f0613c8730de54cd50403c809f7102bc1534bf"
# The Block 202 tip: a real ancestor of HEAD that predates Block 209 and
# therefore carries NEITHER parent artifact.
STALE_PARENT_COMMIT = "141b9e8da04319eb2f31c53389de6edd0cf723bf"
# A real but superseded authority head, carried forward from Block 202's record.
STALE_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_alphabet_is_measurement",
    "claim_landscape_is_parameter_space",
    "claim_macrorealist_premises",
    "claim_classical_no_go",
    "claim_readings_licensed",
    "break_refined_alphabet",
    "break_single_context_solvability",
    "break_refined_stack_inconsistency",
    "break_exclusion_extension",
    "break_landscape_design_space",
    "break_pin_normalisation",
    "break_bound_satisfied",
    "break_landscape_maximum",
    "break_committed_dial",
    "break_dial_sweep",
    "break_parked_verdict",
    "claim_reading_identified",
    "claim_alphabet_exhaustive",
    "claim_macrorealism_established",
    "claim_bound_violated",
    "break_instance_scope",
    "claim_violation_impossible",
    "drop_n5_fence",
    "break_nsimplify_absence",
    "break_float_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_alphabet_is_measurement": "B",
    "claim_landscape_is_parameter_space": "B",
    "claim_macrorealist_premises": "B",
    "claim_classical_no_go": "B",
    "claim_readings_licensed": "B",
    "break_refined_alphabet": "C",
    "break_single_context_solvability": "C",
    "break_refined_stack_inconsistency": "C",
    "break_exclusion_extension": "C",
    "break_landscape_design_space": "D",
    "break_pin_normalisation": "D",
    "break_bound_satisfied": "D",
    "break_landscape_maximum": "D",
    "break_committed_dial": "E",
    "break_dial_sweep": "E",
    "break_parked_verdict": "E",
    "claim_reading_identified": "F",
    "claim_alphabet_exhaustive": "F",
    "claim_macrorealism_established": "F",
    "claim_bound_violated": "F",
    "break_instance_scope": "F",
    "claim_violation_impossible": "F",
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
    "THE REFINED CLASS-VALUE ALPHABET, WHICH IS A REFINEMENT OF A SUBSTITUTION ALPHABET AND NOT A MEASUREMENT ALPHABET: the twelve outcomes (x, k) for x = 0..3 and k in {0, 1/5, -1/5} at the mid slot 3, each written into the committed carrier field by Block 171's own record dictionary and read out through Block 171's own Env.profile at the record-free levels",
    "THE TWELVE-OUTCOME REFINED SYSTEM AND ITS SIX-CONTEXT STACK: one column per refined outcome, one row per readout component per (family, level) context over (W9, W2) x (5, 4, 2), plus one affine normalisation row -- read three ways, as the single context W9-L5, as the whole 25 x 12 stack, and against Block 202's 25 x 4 four-outcome stack on the SAME six contexts",
    "THE LEGGETT-GARG-TYPE INSTRUMENT, WHICH IS THIS BLOCK's ONE NEW BOUND AND IS FORMULATED HERE RATHER THAN IMPORTED: a dichotomic variable at three slots with K = C12 + C23 - C13 <= 1, correlations taken under the PROPOSED W9 formation-weight reading p(x_i at slot i, x_j at slot j) = w_i(x_i) * P(x_j at j | pin x_i at i) with w_i = profile('W9', i) record-free and the conditional the pinned profile",
    "THE COMPLETE FOUR-FACET FINITE LANDSCAPE: the four three-slot chains drawn from the free levels (2, 3, 4, 5) with class-0 pins at the first two slots, the three balanced dichotomizations 01|23, 02|13 and 03|12, and all four deterministic upper facets whose sign triples have product -1, together with exact sum-one and componentwise-nonnegativity checks for every profile used",
    "THE PHASE-DIAL K SWEEP: the committed holonomy action Q_holo_t at the COMMITTED spatial dial {g_re: 1/3, g_im: 1/4} and the seven temporal dial values q in {-2, -1, -1/2, 0, 1/2, 1, 2}, evaluated at the landscape's best design point chain (3, 4, 5), split 01|23, variant a",
    "BLOCK 171's COMMITTED 12x4 BENCH READ THROUGH ITS OWN Site AND Env CLASSES AND NOT REBUILT: Site('12x4', 12, 4) with N = 24, T = 6, c = 1, tstar = 5 and lx = 4, the xgraded carrier substitution, the record dictionary, the W1/W2/W9 gram constructions and the committed spatial dial",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL TWELVE ARE
# FALSE AND STAY FALSE.
GRAVITY_SUPPLIED_CLAIMED = False
ALPHABET_IS_MEASUREMENT_CLAIMED = False
LANDSCAPE_IS_PARAMETER_SPACE_CLAIMED = False
MACROREALIST_PREMISES_CLAIMED = False
CLASSICAL_NO_GO_CLAIMED = False
GENERIC_PARAMETER_THEOREM_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
READING_IDENTIFIED_CLAIMED = False
ALPHABET_EXHAUSTIVE_CLAIMED = False
MACROREALISM_ESTABLISHED_CLAIMED = False
BOUND_VIOLATED_CLAIMED = False
SCOPE_GENERALISATION_CLAIMED = False
VIOLATION_IMPOSSIBLE_CLAIMED = False
CONTINUUM_Q_CLASSIFIED = False
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
# THE THREE WORDS THIS BLOCK DOES USE, AND EXACTLY WHAT EACH BUYS.  Block 202
# declared them UNNAMED because no bound was formulated there.  Here a bound IS
# formulated -- and NONE IS VIOLATED, which is the whole of the change.
NAMED_PHYSICS_WORDS = ("QUANTUM", "BELL", "LEGGETT-GARG")
BOUND_FORMULATED = True
BOUNDS_VIOLATED = 0
LG_TYPE_BY_CONSTRUCTION = True
# THE ONE PHRASE THE PACKAGE LICENSES, VERBATIM AND UNCHANGED FROM BLOCK 202.
LICENSED_PHRASE = "contextuality/interference-LIKE diagnostics"
# THE THREE SCOPED HEADLINE WORDS.
SCOPED_HEADLINE_WORDS = ("ALPHABET", "LANDSCAPE", "NULL SAMPLE")
READINGS = (
    "Classical-model exclusion withdrawn: ranks (8,9) exclude one unit-sum real twelve-weight over six declared contexts, not richer alphabets or arbitrary hidden-variable models.",
    "Macrorealism reading withdrawn: the four exact upper facets are satisfied at 48 finite design points and seven q samples under one proposed reading; a satisfied bound establishes neither motivating premise.",
    "Joint-law identification withdrawn: p(x,y)=w_i(x)P_pinned(y) is imposed for the diagnostic, while the conditional and formation-weight identifications remain open.",
    "Continuum-dial reading withdrawn: seven exact q samples cannot exclude a crossing at an unsampled value, even though every sampled value is well below one.",
    "Quantum-signature reading withdrawn: finite movement of K across the seven samples is a measured dependence on q, not a physical interpretation.",
    "Generalisation withdrawn: the measurements cover one bench, carrier, alphabet slot, pin class, spatial dial, four-facet landscape, and seven temporal-dial values.",
)

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0

# --- the committed bench ------------------------------------------------------
BENCH_TAG = "12x4"
BENCH_COVER = 12
BENCH_LX = 4
BENCH_N = 24
BENCH_T = 6
BENCH_CORE = 1
BENCH_TSTAR = 5
FREE_LEVELS = (2, 3, 4, 5)
MID_SLOT = 3
READ_LEVEL = 5
GRAM_PRIMARY = "W9"
GRAM_SECOND = "W2"

# --- C: THE REFINED ALPHABET --------------------------------------------------
REFINED_CLASS_VALUES = (sp.Integer(0), sp.Rational(1, 5), sp.Rational(-1, 5))
REFINED_CELLS = 4
REFINED_OUTCOMES = 12
REFINED_SUPPORT_COMPLETE = True
SINGLE_CONTEXT = ("W9", 5)
SINGLE_CONTEXT_SHAPE = (5, 12)
SINGLE_CONTEXT_RANKS = (4, 4)
SINGLE_CONTEXT_SOLVABLE = True
CONTEXT_FAMILIES = ("W9", "W2")
CONTEXT_LEVELS = (5, 4, 2)
CONTEXT_COUNT = 6
REFINED_STACK_SHAPE = (25, 12)
REFINED_STACK_RANKS = (8, 9)
REFINED_COMMON_EXISTS = False
# THE INCONSISTENCY IS A LITERAL CONTRADICTION ROW AND NOT A RANK COINCIDENCE:
# the augmented column is a PIVOT column of the exact RREF.
REFINED_RREF_PIVOTS = (0, 1, 3, 4, 6, 7, 9, 10, 12)
REFINED_AUGMENTED_PIVOT = True
# BLOCK 202's OWN STACK, RE-MEASURED HERE ON THE SAME SIX CONTEXTS SO THE
# EXTENSION IS ONE COMPARISON AND NOT TWO SEPARATE BLOCKS' NUMBERS.
BASELINE_STACK_SHAPE = (25, 4)
BASELINE_STACK_RANKS = (4, 5)
BASELINE_COMMON_EXISTS = False
EXCLUSION_EXTENDS = True
# THE LINEAR STATEMENT COMES BEFORE THE NONNEGATIVITY ONE, AND THAT IS THE
# SHARP PART: consistency fails before the simplex is ever consulted.
UNIT_SUM_REAL_CONSISTENCY_FAILS_BEFORE_NONNEGATIVITY = True
CONTEXT_NORMALISATION_RELATION_COUNT = 6
COEFFICIENT_RANK_CEILING = 19

# --- D: THE MACROREALIST LANDSCAPE --------------------------------------------
LG_CHAINS = ((2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5))
LG_SPLIT_NAMES = ("01|23", "02|13", "03|12")
LG_VARIANTS = ("a", "b", "c", "d")
LG_FACET_SIGNS = ((1, 1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1))
LG_DETERMINISTIC_ASSIGNMENTS = 8
LG_PIN_SLOTS = (2, 3, 4)
LG_PIN_CLASS_VALUE = 0
LANDSCAPE_POINTS = 48
LANDSCAPE_BOUND = 1
LANDSCAPE_PROFILE_CHECKS = 52
LANDSCAPE_COMPONENT_CHECKS = 208
LANDSCAPE_NORMALISATION_DEFECTS = 0
LANDSCAPE_NONNEGATIVITY_DEFECTS = 0
LANDSCAPE_VIOLATIONS = 0
LANDSCAPE_ALL_SATISFY = True
LANDSCAPE_ALL_STRICT = True
LANDSCAPE_ARGMAX = ((3, 4, 5), "01|23", "a")
LANDSCAPE_ARGMIN = ((3, 4, 5), "03|12", "d")
LANDSCAPE_MAX_IS_UNIQUE = True
LANDSCAPE_MARGIN_IS_NEGATIVE = True
# EIGHTEEN TIMES THE LANDSCAPE MAXIMUM IS STILL BELOW THE BOUND -- an exact
# rational statement, and the honest way to say 'nowhere near' without a float.
LANDSCAPE_MAX_TIMES_EIGHTEEN_BELOW_BOUND = True
LANDSCAPE_MAX_NUMERATOR_DIGITS = 944
LANDSCAPE_MAX_DENOMINATOR_DIGITS = 945
# THE UNIQUE EXACT MAXIMUM OF THE FORTY-EIGHT-FACET LANDSCAPE, CARRIED IN FULL
# RATHER THAN BY A HASH, so the note and the runner can be compared digit for
# digit.  Its display-only value is +5.325e-02.
LANDSCAPE_MAX_K = sp.Rational(
    19038410443768724360969594743451654483963879680307361320802703916679703797770636093585230117562391347254573024514359290748399236347744570974221536021522134707176086886389871788494500364746457693665322170941447256154454624724151730433057839657348681256877873201962884138967199640886822042736269354045550883922460307027906597877862060704991580511243521564012155505805620398717590253237170801761139084238708116267371183466014868854634586173364269831994542062390377850172303703901847515856311447471147451542906514358154636215269097559099287124971966215821803173329353690671007311630998441761184894808474548832817924715843287804316560304082826322216125498573869990021880473463332789495429808952256006488039209859779573889955101022667726573518500405115956222176761985829570733359876070216899674632073225177138142634322379857222805960104025471354194271507334028496453112345615265262797136397557281250424717858954521053619413463704042077737487229474259,
    357532774076892640787807233968934719128434065514762327680842036549521794066680404211473579874886430741211637781376848194467237125916667862653422058538604662903889235230154590541500109097475339217358820085686800735003904812390130726396275999578790489815065480743167908667597298443699565226722835344556242074498013200998485496371819355828323554077957485562127935750015064177062898110024190606681771190543215404021496917094467818465787421283505788522694882232167209552293685368571072529265354849418874899408566367631953577369279942127976565730195326315845321472053572592776867137951514999551752649532747108604711683770935684784114198451478995123329832406854276315654154652438710680738934927149529943006316615903767662357878678090617980940068264281061464489770327930968751037357457248374579520859430115411904992852857952272866947053584090956840041725814912397778648823085462287497544113545250966535642598325187484740300955013928776884619493106072304)

# --- E: THE PHASE-DIAL K SWEEP ------------------------------------------------
SPATIAL_DIAL_REAL = sp.Rational(1, 3)
SPATIAL_DIAL_IMAGINARY = sp.Rational(1, 4)
TEMPORAL_DIAL_VALUES = (
    sp.Rational(-2), sp.Rational(-1), sp.Rational(-1, 2), sp.Rational(0),
    sp.Rational(1, 2), sp.Rational(1), sp.Rational(2),
)
BEST_CHAIN = (3, 4, 5)
BEST_SPLIT = "01|23"
BEST_VARIANT = "a"
# THE CORRECTED INSTRUMENT, INHERITED FROM BLOCK 202 AND MEASURED AGAIN RATHER
# THAN NARRATED.  Block 202's first firing of a holonomy probe left the spatial
# dial SYMBOLIC and asked for the inverse of a 24 x 24 action carrying two free
# symbols; it was killed.  The committed dial is the fix.
UNDIALLED_FREE_SYMBOLS = 2
DIALLED_FREE_SYMBOLS = 0
SWEEP_SIGNS = ("+", "+", "+", "+", "+", "+", "+")
SWEEP_ALL_SATISFY = True
SWEEP_VIOLATIONS = 0
SWEEP_ARGMAX_Q = sp.Rational(-2)
SWEEP_ARGMIN_Q = sp.Rational(1, 2)
# THE MOVEMENT, AS AN EXACT RATIONAL PREDICATE AND NEVER AS A PERCENTAGE OF A
# FLOAT: twice the spread exceeds the minimum, so the dial moves K by more than
# half of its own smallest value.  Real structure, and still nowhere near 1.
SWEEP_MOVEMENT_EXCEEDS_HALF_MIN = True
SWEEP_MAX_TIMES_TEN_BELOW_BOUND = True
# THE SWEEP IS NOT MONOTONE: the successive differences change sign exactly once.
SWEEP_TURNING_POINTS = 1
SWEEP_PROFILE_COMPONENT_CHECKS = 392
SWEEP_NORMALISATION_DEFECTS = 0
SWEEP_NONNEGATIVITY_DEFECTS = 0
SEVEN_POINT_NULL_RESULT = True

# --- F: THE SIX SCOPE FENCES --------------------------------------------------
PROPOSED_READING = ("p(x_i at slot i, x_j at slot j) = w_i(x_i) * "
                    "P(x_j at j | pin x_i at i)")
JOINT_IDENTIFICATION_HALVES = (
    "the pinned profiles read as CONDITIONALS of one common joint law",
    "the native record-free profile('W9', i) read as FORMATION WEIGHTS",
)
WHICH_HALF_FAILS_IS_OPEN = True
ALPHABET_OUTCOMES_TESTED = 12
UNTESTED_ALPHABET_REFINEMENTS = (
    "class values outside the tested triple {0, 1/5, -1/5}",
    "more than one class value per cell, or pins at more than one slot",
    "any readout family outside the tested pair (W9, W2)",
    "any level outside the tested triple (5, 4, 2)",
)
# Six exact row relations follow from context-wise profile normalisation, so
# the 25-row coefficient matrix has rank at most 19.  Outcome count alone does
# not imply spanning, consistency, or simplex membership for any richer
# structured alphabet; every alphabet beyond the twelve declared columns is
# left open.
RICHER_ALPHABET_CLASSIFIED = False
NULL_RESULT_ONLY = True
LICENSED_PHRASE_UNCHANGED_FROM_PARENT = True
INSTANCE_SCOPE = (
    "one bench, the committed Site('12x4', 12, 4)",
    "one carrier, the committed xgraded substitution",
    "one mid slot for the refined alphabet, mid = 3",
    "class-0 pins throughout the landscape and the sweep",
    "one committed spatial dial {g_re: 1/3, g_im: 1/4}",
    "seven temporal dial values at one design point",
)
INSTANCE_SCOPE_COUNT = 6
STRUCTURAL_CHANGES_REQUIRED = (
    "joint-pin correlations -- two records written at once, not one",
    "a stronger coupling between the pinned slot and the readout slot",
)

# THE ONE-FAMILY CONTRACT IS ENFORCED BY DISJOINT CLAIM KEYS AND NOT ONLY BY THE
# ASSERTION IN main().  Every claim key below is read by EXACTLY ONE gate.  The
# F fences therefore carry their own constants -- READING_IDENTIFIED_CLAIMED,
# ALPHABET_EXHAUSTIVE_CLAIMED, MACROREALISM_ESTABLISHED_CLAIMED,
# BOUND_VIOLATED_CLAIMED, SCOPE_GENERALISATION_CLAIMED and
# VIOLATION_IMPOSSIBLE_CLAIMED -- rather than re-reading the B, D and E keys that
# state the same thing from the other side.  Where an F gate depends on a fact
# measured elsewhere, the gate NAMES the family that measures it in its statement
# and does not consume that family's claim, so neither leans on the other and no
# mutation can flip two families at once.

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  This block's content is a set of exact rank statements and a
# set of exact ORDER statements about numbers whose decimal displays sit between
# 1e-4 and 1e-1.  A tolerance-carrying call would collapse the landscape's
# finite exact values, destroy the uniqueness of the maximum, and turn a
# measured sweep movement into numerical noise.  Gate G counts the occurrences
# in this file's own source and requires ZERO, requires ZERO float literals by
# an AST scan of the same source, and requires that decimal conversion happen at
# EXACTLY ONE call site, inside the display helper, so no verdict predicate can
# ever consume a float.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def float_literal_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many float literals this runner's own source
    contains, by an AST walk rather than by a text search."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    """THE SECOND HALF OF THE SAME HYGIENE, AND IT IS THE HALF THIS BLOCK
    ACTUALLY NEEDS.  The note carries decimal DISPLAYS for a landscape whose
    exact maximum runs to 944 digits, so a float conversion must exist
    somewhere; what must NOT exist is a second one.  Gate G-3 requires EXACTLY
    ONE -- the display helper below.  Every verdict predicate in this file
    therefore consumes exact rationals only, by measurement."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


def display(value) -> str:
    """THE ONE AND ONLY DECIMAL CONVERSION IN THIS FILE, AND IT IS DISPLAY-ONLY.
    Nothing this function returns is ever compared, ranked, summed or gated.
    Gate G-3 measures that this is the sole float call site."""
    return f"{float(value):+.9f}"


def exact_rank(matrix: sp.MatrixBase) -> int:
    """The rank over QQ_I, exactly.  Every consistency verdict in family C is one
    of these numbers against another, never a residual norm."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ_I).rank()


def sign_word(value) -> str:
    """The exact sign of an exact rational.  Ternary and never thresholded."""
    return "+" if value > 0 else "-" if value < 0 else "0"


# ---------------------------------------------------------------------------
# THE MEASURED FACTS
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class BenchFacts:
    tag: str
    size: int
    width: int
    core: int
    tstar: int
    extent: int
    free_levels: tuple
    mid_rows: tuple
    read_rows: tuple


@dataclass(frozen=True)
class AlphabetFacts:
    class_values: tuple
    outcomes: int
    support_complete: bool
    single_shape: tuple
    single_ranks: tuple
    single_solvable: bool
    stack_shape: tuple
    stack_ranks: tuple
    common_exists: bool
    rref_pivots: tuple
    augmented_pivot: bool
    baseline_shape: tuple
    baseline_ranks: tuple
    baseline_common_exists: bool
    context_normalisation_relations: bool
    coefficient_rank_ceiling: int


@dataclass(frozen=True)
class LandscapeFacts:
    points: int
    facet_truth_table_exact: bool
    profile_checks: int
    component_checks: int
    normalisation_defects: int
    nonnegativity_defects: int
    violations: int
    all_satisfy: bool
    all_strict: bool
    argmax: tuple
    argmin: tuple
    max_value: object
    min_value: object
    max_is_unique: bool
    margin_is_negative: bool
    max_times_eighteen_below: bool
    max_numerator_digits: int
    max_denominator_digits: int
    table_display: dict


@dataclass(frozen=True)
class SweepFacts:
    undialled_symbols: int
    dialled_symbols: int
    signs: tuple
    violations: int
    all_satisfy: bool
    argmax_q: object
    argmin_q: object
    movement_exceeds_half_min: bool
    max_times_ten_below: bool
    turning_points: int
    component_checks: int
    normalisation_defects: int
    nonnegativity_defects: int
    displays: dict


@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    readings: int
    named_words: int
    scoped_words: int
    bench: BenchFacts
    alphabet: AlphabetFacts
    landscape: LandscapeFacts
    sweep: SweepFacts
    scope: dict
    nsimplify_calls: int
    float_literals: int
    float_calls: int


def outcome_system(base_env, envs, outcomes, contexts, extent):
    """THE OUTCOME SYSTEM, AND ITS SHAPE IS ITS CONTENT.  One column per outcome,
    one row per readout component per context, plus one affine normalisation row
    sum(w) = 1.  `envs` maps an outcome key to the environment that outcome
    pins, so the SAME cache serves the four-outcome baseline and the
    twelve-outcome refinement."""
    rows, rhs, support = [], [], True
    for family, level in contexts:
        base = base_env.profile(family, level)
        pinned = [envs[o].profile(family, level) for o in outcomes]
        if base is None or any(p is None for p in pinned):
            support = False
            continue
        for component in range(extent):
            rows.append([p[component] for p in pinned])
            rhs.append(base[component])
    rows.append([sp.Integer(1)] * len(outcomes))
    rhs.append(sp.Integer(1))
    return sp.Matrix(rows), sp.Matrix(rhs), support


def measure_alphabet(site, base_env, envs) -> AlphabetFacts:
    """THE REFINED ALPHABET, AND THE QUESTION IS A RANK AND NEVER A SEARCH.
    'Does ANY twelve-weight restore the six tested marginals' is rank A against
    rank [A|b], taken exactly over QQ_I.  Block 202's four-outcome stack is
    re-measured here from the SAME environment cache, so the extension is one
    comparison rather than two blocks' numbers set side by side."""
    extent = site.lx
    refined = tuple((x, k) for x in range(extent) for k in REFINED_CLASS_VALUES)
    contexts = tuple((f, l) for f in CONTEXT_FAMILIES for l in CONTEXT_LEVELS)

    single, single_rhs, single_support = outcome_system(
        base_env, envs, refined, (SINGLE_CONTEXT,), extent)
    single_ranks = (exact_rank(single),
                    exact_rank(single.row_join(single_rhs)))

    stack, stack_rhs, stack_support = outcome_system(
        base_env, envs, refined, contexts, extent)
    stack_ranks = (exact_rank(stack), exact_rank(stack.row_join(stack_rhs)))
    pivots = sp.Matrix(stack.row_join(stack_rhs)).rref()[1]

    baseline_outcomes = tuple((x, REFINED_CLASS_VALUES[0]) for x in range(extent))
    baseline, baseline_rhs, _ = outcome_system(
        base_env, envs, baseline_outcomes, contexts, extent)
    baseline_ranks = (exact_rank(baseline),
                      exact_rank(baseline.row_join(baseline_rhs)))
    context_relations = all(
        all(sp.cancel(sum(
            (stack[context * extent + component, column]
             for component in range(extent)), sp.Integer(0))
            - stack[-1, column]) == 0
            for column in range(stack.cols))
        and sp.cancel(sum(
            (stack_rhs[context * extent + component, 0]
             for component in range(extent)), sp.Integer(0))
            - stack_rhs[-1, 0]) == 0
        for context in range(len(contexts)))
    return AlphabetFacts(
        REFINED_CLASS_VALUES, len(refined),
        bool(single_support and stack_support),
        single.shape, single_ranks, single_ranks[0] == single_ranks[1],
        stack.shape, stack_ranks, stack_ranks[0] == stack_ranks[1],
        tuple(pivots), len(refined) in pivots,
        baseline.shape, baseline_ranks,
        baseline_ranks[0] == baseline_ranks[1],
        bool(context_relations), stack.rows - len(contexts))


SPLITS = {
    "01|23": (1, 1, -1, -1),
    "02|13": (1, -1, 1, -1),
    "03|12": (1, -1, -1, 1),
}


def correlation(base_env, pins, i, j, split, extent):
    """THE CORRELATION, UNDER THE PROPOSED READING AND SAID SO IN THE CODE.
    C_ij = sum_x sum_y s(x) s(y) w_i(x) P(y at j | pin x at i), with w_i the
    RECORD-FREE profile at slot i and P(. | pin) the PINNED profile at slot j.
    That product form is the PROPOSED W9 formation-weight reading; it is not
    derived here and Block 202's joint-identification fence still stands over
    it."""
    weights = base_env.profile(GRAM_PRIMARY, i)
    total = sp.Integer(0)
    for x in range(extent):
        conditioned = pins[(i, x)].profile(GRAM_PRIMARY, j)
        for y in range(extent):
            total += split[x] * split[y] * weights[x] * conditioned[y]
    return sp.cancel(total)


def measure_landscape(site, base_env, pins) -> LandscapeFacts:
    """THE FORTY-EIGHT-FACET LANDSCAPE.  Correlations are cached per
    (slot_i, slot_j, split) because the four chains share six distinct slot
    pairs between them; the exact arithmetic is therefore done eighteen times
    and read forty-eight ways."""
    extent = site.lx
    facet_truth_table_exact = all(
        sum(sign * correlation_value for sign, correlation_value in zip(
            signs, (q1 * q2, q2 * q3, q1 * q3))) in (-3, 1)
        for q1 in (-1, 1) for q2 in (-1, 1) for q3 in (-1, 1)
        for signs in LG_FACET_SIGNS)
    profiles = [base_env.profile(GRAM_PRIMARY, level)
                for level in FREE_LEVELS]
    for slot in LG_PIN_SLOTS:
        for level in FREE_LEVELS:
            for x in range(extent):
                profiles.append(
                    pins[(slot, x)].profile(GRAM_PRIMARY, level))
    normalisation_defects = sum(
        sp.cancel(sum(profile, sp.Integer(0)) - sp.Integer(1)) != 0
        for profile in profiles)
    nonnegativity_defects = sum(
        bool(value < 0) for profile in profiles for value in profile)

    cache: dict = {}

    def corr(i, j, name):
        if (i, j, name) not in cache:
            cache[(i, j, name)] = correlation(
                base_env, pins, i, j, SPLITS[name], extent)
        return cache[(i, j, name)]

    table: dict = {}
    for chain in LG_CHAINS:
        t1, t2, t3 = chain
        for name in LG_SPLIT_NAMES:
            c12, c23, c13 = corr(t1, t2, name), corr(t2, t3, name), \
                corr(t1, t3, name)
            for variant, value in (("a", c12 + c23 - c13),
                                   ("b", c12 - c23 + c13),
                                   ("c", -c12 + c23 + c13),
                                   ("d", -c12 - c23 - c13)):
                table[(chain, name, variant)] = sp.cancel(value)

    bound = sp.Integer(LANDSCAPE_BOUND)
    violations = sum(1 for v in table.values() if v > bound)
    argmax = max(table, key=lambda key: table[key])
    argmin = min(table, key=lambda key: table[key])
    peak, trough = table[argmax], table[argmin]
    # EVERY ORDER PREDICATE IS COERCED TO A PYTHON bool AT THE POINT OF
    # MEASUREMENT.  A SymPy comparison between two exact Rationals returns
    # S.true / S.false, which compares EQUAL to True but is not IDENTICAL to it;
    # the gates below use `is` against declared literals precisely so a claim
    # cannot be satisfied by a truthy object, so the coercion belongs here and
    # not in the gate.  The comparison itself is still exact-rational.
    return LandscapeFacts(
        len(table), bool(facet_truth_table_exact), len(profiles),
        sum(len(profile) for profile in profiles),
        normalisation_defects, nonnegativity_defects, violations,
        bool(all(v <= bound for v in table.values())),
        bool(all(v < bound for v in table.values())),
        argmax, argmin, peak, trough,
        sum(1 for v in table.values() if v == peak) == 1,
        bool(sp.cancel(peak - bound) < 0),
        bool(sp.Integer(18) * peak < bound),
        len(str(sp.Integer(peak.p))), len(str(sp.Integer(peak.q))),
        {key: display(value) for key, value in table.items()})


def measure_sweep(site) -> SweepFacts:
    """THE PHASE-DIAL K SWEEP, AT THE LANDSCAPE'S BEST DESIGN POINT.  The
    temporal link is I*sx, so the dial q carries the imaginary link's magnitude
    AND its sign.  Nine environments are built per dial value -- the record-free
    base plus the four pins at each of the chain's first two slots -- and the
    same K as family D is evaluated on each."""
    extent = site.lx
    dial = {b171.GRE: SPATIAL_DIAL_REAL, b171.GIM: SPATIAL_DIAL_IMAGINARY}
    probe = sp.Matrix(site.Q_holo_t.subs(
        site.sub(records={}, sx=TEMPORAL_DIAL_VALUES[0])))
    undialled = len(probe.free_symbols)
    dialled = len(sp.Matrix(probe.subs(dial)).free_symbols)

    def action(records, q):
        return sp.Matrix(
            site.Q_holo_t.subs(site.sub(records=dict(records), sx=q)).subs(dial))

    t1, t2, t3 = BEST_CHAIN
    split = SPLITS[BEST_SPLIT]
    swept: dict = {}
    probability_profiles = []
    for q in TEMPORAL_DIAL_VALUES:
        base = b171.Env(site, action({}, q), f"q{q}")
        pins = {(slot, x): b171.Env(
            site, action({(slot, x): sp.Integer(LG_PIN_CLASS_VALUE)}, q),
            f"q{q}s{slot}x{x}")
            for slot in (t1, t2) for x in range(extent)}
        probability_profiles.extend((
            base.profile(GRAM_PRIMARY, t1),
            base.profile(GRAM_PRIMARY, t2),
        ))
        for x in range(extent):
            probability_profiles.extend((
                pins[(t1, x)].profile(GRAM_PRIMARY, t2),
                pins[(t1, x)].profile(GRAM_PRIMARY, t3),
                pins[(t2, x)].profile(GRAM_PRIMARY, t3),
            ))
        c12 = correlation(base, pins, t1, t2, split, extent)
        c23 = correlation(base, pins, t2, t3, split, extent)
        c13 = correlation(base, pins, t1, t3, split, extent)
        swept[q] = sp.cancel(c12 + c23 - c13)

    bound = sp.Integer(LANDSCAPE_BOUND)
    values = [swept[q] for q in TEMPORAL_DIAL_VALUES]
    peak, trough = max(values), min(values)
    argmax = [q for q in TEMPORAL_DIAL_VALUES if swept[q] == peak][0]
    argmin = [q for q in TEMPORAL_DIAL_VALUES if swept[q] == trough][0]
    steps = [sp.cancel(values[i] - values[i - 1])
             for i in range(1, len(values))]
    turning = sum(1 for i in range(1, len(steps))
                  if sign_word(steps[i]) != sign_word(steps[i - 1]))
    # The same bool() coercion as family D, and for the same reason: the gates
    # test identity against declared literals, so an exact SymPy S.true must be
    # narrowed here rather than loosened there.
    return SweepFacts(
        undialled, dialled,
        tuple(sign_word(swept[q]) for q in TEMPORAL_DIAL_VALUES),
        sum(1 for v in values if v > bound),
        bool(all(v <= bound for v in values)),
        argmax, argmin,
        bool(sp.Integer(2) * sp.cancel(peak - trough) > trough),
        bool(sp.Integer(10) * peak < bound),
        turning,
        sum(len(profile) for profile in probability_profiles),
        sum(sp.cancel(sum(profile, sp.Integer(0)) - sp.Integer(1)) != 0
            for profile in probability_profiles),
        sum(bool(value < 0)
            for profile in probability_profiles for value in profile),
        {q: display(swept[q]) for q in TEMPORAL_DIAL_VALUES})


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() \
        else ""
    site = b171.Site(BENCH_TAG, BENCH_COVER, BENCH_LX)

    def action(records):
        return sp.Matrix(site.bench.Q.subs(site.sub(records=dict(records))))

    # THE ONE MEASUREMENT PASS, AND THE CACHE IS THE COST CONTROL.  Twenty-one
    # committed environments are built here and shared by families C and D: the
    # record-free base, the TWELVE refined outcomes at the mid slot, and the
    # eight remaining class-0 pins at slots 2 and 4.  The four class-0 pins at
    # the mid slot are ONE object serving BOTH families -- Block 202's outcome
    # alphabet is literally the k = 0 column of this block's.  Family E builds
    # its own sixty-three holonomy environments.
    base_env = b171.Env(site, action({}), "b")
    envs = {(x, k): b171.Env(site, action({(MID_SLOT, x): k}), f"m{x}k{k}")
            for x in range(site.lx) for k in REFINED_CLASS_VALUES}
    pins = {(MID_SLOT, x): envs[(x, REFINED_CLASS_VALUES[0])]
            for x in range(site.lx)}
    for slot in LG_PIN_SLOTS:
        if slot == MID_SLOT:
            continue
        for x in range(site.lx):
            pins[(slot, x)] = b171.Env(
                site,
                action({(slot, x): sp.Integer(LG_PIN_CLASS_VALUE)}),
                f"p{slot}x{x}")
    bench = BenchFacts(
        site.tag, site.N, site.T, site.c, site.tstar, site.lx,
        tuple(site.free_levels), tuple(site.rows(MID_SLOT)),
        tuple(site.rows(READ_LEVEL)))
    return Facts(
        main_head,
        authority_certificate(main_head),
        len(IMPOSED_OBJECTS),
        len(REGISTERED_OBJECTS),
        len(ADOPTED_OBJECTS),
        len(UNSUPPLIED_GRAVITY_STRUCTURES),
        len(READINGS),
        len(NAMED_PHYSICS_WORDS),
        len(SCOPED_HEADLINE_WORDS),
        bench,
        measure_alphabet(site, base_env, envs),
        measure_landscape(site, base_env, pins),
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
        "alphabet_is_measurement": ALPHABET_IS_MEASUREMENT_CLAIMED,
        "landscape_is_parameter_space": LANDSCAPE_IS_PARAMETER_SPACE_CLAIMED,
        "macrorealist_premises": MACROREALIST_PREMISES_CLAIMED,
        "lg_type_by_construction": LG_TYPE_BY_CONSTRUCTION,
        "classical_no_go": CLASSICAL_NO_GO_CLAIMED,
        "generic_parameter_theorem": GENERIC_PARAMETER_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "readings": len(READINGS),
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C
        "bench_metadata": (BENCH_TAG, BENCH_N, BENCH_T, BENCH_CORE,
                           BENCH_TSTAR, BENCH_LX),
        "free_levels": FREE_LEVELS,
        "mid_rows": (12, 13, 14, 15),
        "read_rows": (20, 21, 22, 23),
        "class_values": REFINED_CLASS_VALUES,
        "refined_outcomes": REFINED_OUTCOMES,
        "refined_support": REFINED_SUPPORT_COMPLETE,
        "single_shape": SINGLE_CONTEXT_SHAPE,
        "single_ranks": SINGLE_CONTEXT_RANKS,
        "single_solvable": SINGLE_CONTEXT_SOLVABLE,
        "stack_shape": REFINED_STACK_SHAPE,
        "stack_ranks": REFINED_STACK_RANKS,
        "common_exists": REFINED_COMMON_EXISTS,
        "rref_pivots": REFINED_RREF_PIVOTS,
        "augmented_pivot": REFINED_AUGMENTED_PIVOT,
        "baseline_shape": BASELINE_STACK_SHAPE,
        "baseline_ranks": BASELINE_STACK_RANKS,
        "baseline_common_exists": BASELINE_COMMON_EXISTS,
        "exclusion_extends": EXCLUSION_EXTENDS,
        "unit_sum_first":
            UNIT_SUM_REAL_CONSISTENCY_FAILS_BEFORE_NONNEGATIVITY,
        "context_normalisation_relations": True,
        "context_relation_count": CONTEXT_NORMALISATION_RELATION_COUNT,
        "coefficient_rank_ceiling": COEFFICIENT_RANK_CEILING,
        # D
        "landscape_points": LANDSCAPE_POINTS,
        "facet_truth_table_exact": True,
        "profile_checks": LANDSCAPE_PROFILE_CHECKS,
        "component_checks": LANDSCAPE_COMPONENT_CHECKS,
        "normalisation_defects": LANDSCAPE_NORMALISATION_DEFECTS,
        "nonnegativity_defects": LANDSCAPE_NONNEGATIVITY_DEFECTS,
        "landscape_violations": LANDSCAPE_VIOLATIONS,
        "landscape_all_satisfy": LANDSCAPE_ALL_SATISFY,
        "landscape_all_strict": LANDSCAPE_ALL_STRICT,
        "landscape_argmax": LANDSCAPE_ARGMAX,
        "landscape_argmin": LANDSCAPE_ARGMIN,
        "landscape_max": LANDSCAPE_MAX_K,
        "landscape_max_unique": LANDSCAPE_MAX_IS_UNIQUE,
        "landscape_margin_negative": LANDSCAPE_MARGIN_IS_NEGATIVE,
        "landscape_eighteen": LANDSCAPE_MAX_TIMES_EIGHTEEN_BELOW_BOUND,
        "landscape_digits": (LANDSCAPE_MAX_NUMERATOR_DIGITS,
                             LANDSCAPE_MAX_DENOMINATOR_DIGITS),
        # E
        "undialled_symbols": UNDIALLED_FREE_SYMBOLS,
        "dialled_symbols": DIALLED_FREE_SYMBOLS,
        "sweep_signs": SWEEP_SIGNS,
        "sweep_violations": SWEEP_VIOLATIONS,
        "sweep_all_satisfy": SWEEP_ALL_SATISFY,
        "sweep_argmax_q": SWEEP_ARGMAX_Q,
        "sweep_argmin_q": SWEEP_ARGMIN_Q,
        "sweep_movement": SWEEP_MOVEMENT_EXCEEDS_HALF_MIN,
        "sweep_ten": SWEEP_MAX_TIMES_TEN_BELOW_BOUND,
        "sweep_turning": SWEEP_TURNING_POINTS,
        "sweep_component_checks": SWEEP_PROFILE_COMPONENT_CHECKS,
        "sweep_normalisation_defects": SWEEP_NORMALISATION_DEFECTS,
        "sweep_nonnegativity_defects": SWEEP_NONNEGATIVITY_DEFECTS,
        "seven_point_null": SEVEN_POINT_NULL_RESULT,
        # F
        "joint_halves": len(JOINT_IDENTIFICATION_HALVES),
        "which_half_open": WHICH_HALF_FAILS_IS_OPEN,
        "reading_identified": READING_IDENTIFIED_CLAIMED,
        "alphabet_tested": ALPHABET_OUTCOMES_TESTED,
        "alphabet_exhaustive": ALPHABET_EXHAUSTIVE_CLAIMED,
        "untested_refinements": len(UNTESTED_ALPHABET_REFINEMENTS),
        "richer_alphabet_classified": RICHER_ALPHABET_CLASSIFIED,
        "macrorealism_established": MACROREALISM_ESTABLISHED_CLAIMED,
        "null_result_only": NULL_RESULT_ONLY,
        "phrase_unchanged": LICENSED_PHRASE_UNCHANGED_FROM_PARENT,
        "bound_formulated": BOUND_FORMULATED,
        "bounds_violated": BOUNDS_VIOLATED,
        "bound_violated_claimed": BOUND_VIOLATED_CLAIMED,
        "named_words": len(NAMED_PHYSICS_WORDS),
        "instance_scope": INSTANCE_SCOPE_COUNT,
        "scope_generalisation": SCOPE_GENERALISATION_CLAIMED,
        "violation_impossible": VIOLATION_IMPOSSIBLE_CLAIMED,
        "continuum_q_classified": CONTINUUM_Q_CLASSIFIED,
        "structural_changes": len(STRUCTURAL_CHANGES_REQUIRED),
        "scoped_words": len(SCOPED_HEADLINE_WORDS),
        # G
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
    elif mutation == "claim_alphabet_is_measurement":
        # THE FIRST MISREAD: refining the alphabet is asserted to make the
        # instrument a MEASUREMENT.  Three class values written into four cells
        # of a rational matrix are still a substitution.
        claims["alphabet_is_measurement"] = True
    elif mutation == "claim_landscape_is_parameter_space":
        # THE SECOND MISREAD: forty-eight enumerated facet evaluations on ONE
        # bench are asserted to be a parameter space. They are finite points.
        claims["landscape_is_parameter_space"] = True
    elif mutation == "claim_macrorealist_premises":
        # THE WORD MACROREALIST UN-SCOPED: macrorealism and noninvasive
        # measurability are asserted to be established or assumed for this
        # framework.  They are the classical premises that MOTIVATE the bound
        # and neither is proved nor assumed by any line here.
        claims["macrorealist_premises"] = True
        claims["lg_type_by_construction"] = False
    elif mutation == "claim_classical_no_go":
        # THE OVERREACH IN ITS STRONGEST FORM: a general classical no-go is
        # asserted from six tested contexts and forty-eight facet values on one
        # bench.
        claims["classical_no_go"] = True
        claims["generic_parameter_theorem"] = True
        claims["continuum_limit"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_refined_alphabet":
        claims["refined_outcomes"] = 4
        claims["class_values"] = (sp.Integer(0),)
    elif mutation == "break_single_context_solvability":
        # THE OTHER HALF OF THE STATEMENT: if the single refined context were
        # ALSO unsolvable, the six-context inconsistency would carry no
        # information about CONTEXT at all -- it would just be a bad alphabet.
        claims["single_ranks"] = (4, 5)
        claims["single_solvable"] = False
    elif mutation == "break_refined_stack_inconsistency":
        # THE HEADLINE DENIED: the refined stack is asserted CONSISTENT, which
        # is exactly the outcome that would have re-opened Block 202's escape.
        claims["stack_ranks"] = (8, 8)
        claims["common_exists"] = True
        claims["augmented_pivot"] = False
    elif mutation == "break_exclusion_extension":
        # THE COMPARISON BROKEN: Block 202's four-outcome stack is asserted
        # CONSISTENT here, which would make this block's (8, 9) an unrelated
        # fact rather than an extension of a landed one.
        claims["baseline_ranks"] = (4, 4)
        claims["baseline_common_exists"] = True
        claims["exclusion_extends"] = False
    # --- D ----------------------------------------------------------------
    elif mutation == "break_landscape_design_space":
        claims["landscape_points"] = 12
    elif mutation == "break_pin_normalisation":
        # THE INSTRUMENT UNCALIBRATED: sum-one and componentwise nonnegativity
        # are independently required before the profiles are probabilities.
        claims["normalisation_defects"] = 1
        claims["nonnegativity_defects"] = 1
    elif mutation == "break_bound_satisfied":
        # THE RESULT INVERTED: a violation is asserted somewhere in the
        # landscape. There is none among the forty-eight evaluated facets.
        claims["landscape_violations"] = 1
        claims["landscape_all_satisfy"] = False
        claims["landscape_all_strict"] = False
    elif mutation == "break_landscape_maximum":
        claims["landscape_argmax"] = ((2, 3, 4), "01|23", "a")
        claims["landscape_max_unique"] = False
    # --- E ----------------------------------------------------------------
    elif mutation == "break_committed_dial":
        # THE CORRECTED INSTRUMENT UN-CORRECTED: the action is asserted to be
        # symbol-free before the committed dial is applied, which is the exact
        # error that killed Block 202's first holonomy firing.
        claims["undialled_symbols"] = 0
    elif mutation == "break_dial_sweep":
        # THE DIAL ASSERTED INERT: K is claimed not to move across q, which
        # would make the finite null sample a statement about one number rather than
        # about a swept curve.
        claims["sweep_movement"] = False
        claims["sweep_turning"] = 0
    elif mutation == "break_parked_verdict":
        claims["sweep_violations"] = 1
        claims["sweep_all_satisfy"] = False
        claims["sweep_nonnegativity_defects"] = 1
        claims["seven_point_null"] = False
    # --- F ----------------------------------------------------------------
    elif mutation == "claim_reading_identified":
        # BLOCK 202's FENCE DELETED: the W9 formation-weight reading is asserted
        # to be identified rather than proposed, which would turn every K in
        # this block from a conditional number into an established one.
        claims["reading_identified"] = True
        claims["which_half_open"] = False
    elif mutation == "claim_alphabet_exhaustive":
        # THE ESCAPE ASSERTED FULLY CLOSED: twelve outcomes are asserted to
        # exhaust the classical outcome space, so that 'no common w' would become
        # 'no classical model'.  Other class values alone refute it.
        claims["alphabet_exhaustive"] = True
        claims["untested_refinements"] = 0
        claims["richer_alphabet_classified"] = True
    elif mutation == "claim_macrorealism_established":
        # THE NULL RESULT PROMOTED: a satisfied bound is asserted to ESTABLISH
        # macrorealism.  Satisfying an inequality establishes nothing.
        claims["macrorealism_established"] = True
        claims["null_result_only"] = False
    elif mutation == "claim_bound_violated":
        # THE WORD THE PACKAGE DOES NOT EARN: a violated bound is asserted.  A
        # bound is FORMULATED here for the first time in this lane, and NONE is
        # violated anywhere in it.
        claims["bound_violated_claimed"] = True
        claims["bounds_violated"] = 1
    elif mutation == "break_instance_scope":
        claims["instance_scope"] = 0
    elif mutation == "claim_violation_impossible":
        # FINITE NULL SAMPLE READ AS PROVED: absence at these 48+7 evaluations
        # is asserted to make violation impossible. Nothing here bounds an
        # unsampled q or a structurally different instrument.
        claims["violation_impossible"] = True
        claims["continuum_q_classified"] = True
        claims["structural_changes"] = 0
    # --- G ----------------------------------------------------------------
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
    bench = facts.bench
    alphabet = facts.alphabet
    landscape = facts.landscape
    sweep = facts.sweep

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 209 artifacts are "
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
        "B-3", f"THE WORD *ALPHABET* IS SCOPED BEFORE THE FIRST NUMERAL: it "
        f"names a refinement of the SUBSTITUTION alphabet -- the three class "
        f"values {tuple(str(v) for v in REFINED_CLASS_VALUES)} written into the "
        f"committed carrier field by Block 171's own record dictionary -- and "
        f"names NO measurement process, NO collapse, NO state update and NO "
        f"physical intervention",
        claims["alphabet_is_measurement"] is False)
    checks.check(
        "B-4", f"THE WORD *LANDSCAPE* IS SCOPED: it names "
        f"{LANDSCAPE_POINTS} ENUMERATED design points on ONE bench -- "
        f"{len(LG_CHAINS)} chains x {len(LG_SPLIT_NAMES)} splits x "
        f"{len(LG_VARIANTS)} variants -- and names NO parameter space, NO "
        f"continuum and NO generic point",
        claims["landscape_is_parameter_space"] is False)
    checks.check(
        "B-5", f"THE WORD *MACROREALIST* IS SCOPED, AND THIS IS THE ONE THE "
        f"BLOCK MUST GET RIGHT: the bound is LEGGETT-GARG-TYPE BY CONSTRUCTION "
        f"({claims['lg_type_by_construction']}) -- macrorealism and noninvasive "
        f"measurability are the classical premises that MOTIVATE K <= 1 -- and "
        f"this block NEITHER PROVES NOR ASSUMES either premise for this "
        f"framework, so macrorealist_premises = "
        f"{claims['macrorealist_premises']}",
        claims["macrorealist_premises"] is False
        and claims["lg_type_by_construction"] is True)
    checks.check(
        "B-6", "NO GENERAL CLASSICAL NO-GO, NO GENERIC-PARAMETER THEOREM AND "
        "NO CONTINUUM LIMIT: what is established is a set of exact "
        "finite-instance predicates on ONE bench, and six tested contexts with "
        "forty-eight facet evaluations are not a parameter space or a limit",
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

    # --- C: THE REFINED ALPHABET -------------------------------------------
    checks.check(
        "C-1", f"THE REFINED INSTRUMENT IS BLOCK 202's NAMED ESCAPE, BUILT: "
        f"Block 171's bench {claims['bench_metadata']} for "
        f"(tag, N, T, c, tstar, lx) with free levels {claims['free_levels']}, "
        f"pinned rows {claims['mid_rows']} at slot {MID_SLOT} and readout rows "
        f"{claims['read_rows']} at level {READ_LEVEL}; the alphabet is "
        f"{REFINED_CELLS} cells x {len(REFINED_CLASS_VALUES)} class values "
        f"{tuple(str(v) for v in REFINED_CLASS_VALUES)} = "
        f"{claims['refined_outcomes']} outcomes, every one of them with "
        f"support ({claims['refined_support']})",
        (bench.tag, bench.size, bench.width, bench.core, bench.tstar,
         bench.extent) == claims["bench_metadata"]
        and bench.free_levels == claims["free_levels"]
        and bench.mid_rows == claims["mid_rows"]
        and bench.read_rows == claims["read_rows"]
        and alphabet.class_values == claims["class_values"]
        and alphabet.outcomes == claims["refined_outcomes"]
        and claims["refined_outcomes"] == REFINED_CELLS * len(REFINED_CLASS_VALUES)
        and alphabet.support_complete is claims["refined_support"]
        and claims["refined_support"] is True)
    checks.check(
        "C-2", f"AND THE SINGLE REFINED CONTEXT ALONE IS SOLVABLE, WHICH IS "
        f"WHAT MAKES THE STACK A STATEMENT ABOUT CONTEXT: the "
        f"{SINGLE_CONTEXT[0]}-L{SINGLE_CONTEXT[1]} refined system is "
        f"{claims['single_shape']} with ranks {claims['single_ranks']}, so "
        f"single_solvable = {claims['single_solvable']}",
        alphabet.single_shape == claims["single_shape"]
        and alphabet.single_ranks == claims["single_ranks"]
        and claims["single_ranks"][0] == claims["single_ranks"][1]
        and alphabet.single_solvable is claims["single_solvable"]
        and claims["single_solvable"] is True)
    checks.check(
        "C-3", f"THE SIX-CONTEXT REFINED STACK HAS NO UNIT-SUM REAL WEIGHT, "
        f"BEFORE NONNEGATIVITY IS ASKED FOR: the "
        f"stack is {claims['stack_shape']} -- {len(CONTEXT_FAMILIES)} families "
        f"x {len(CONTEXT_LEVELS)} levels x {BENCH_LX} components plus one "
        f"normalisation row -- with rank A = {claims['stack_ranks'][0]} and "
        f"rank [A|b] = {claims['stack_ranks'][1]}, the exact RREF pivots are "
        f"{claims['rref_pivots']} so the AUGMENTED column is itself a pivot "
        f"({claims['augmented_pivot']}) and the contradiction row is literal. "
        f"The six context-normalisation identities are exact "
        f"({claims['context_normalisation_relations']}) and bound the 25-row "
        f"coefficient rank by {claims['coefficient_rank_ceiling']}; outcome "
        f"count alone supplies no richer-alphabet threshold. common_exists = "
        f"{claims['common_exists']}",
        alphabet.stack_shape == claims["stack_shape"]
        and alphabet.stack_ranks == claims["stack_ranks"]
        and claims["stack_ranks"][0] != claims["stack_ranks"][1]
        and alphabet.rref_pivots == claims["rref_pivots"]
        and alphabet.augmented_pivot is claims["augmented_pivot"]
        and claims["augmented_pivot"] is True
        and alphabet.common_exists is claims["common_exists"]
        and claims["common_exists"] is False
        and claims["unit_sum_first"] is True
        and alphabet.context_normalisation_relations
        is claims["context_normalisation_relations"]
        and claims["context_normalisation_relations"] is True
        and claims["context_relation_count"] == len(CONTEXT_FAMILIES) * len(CONTEXT_LEVELS)
        and alphabet.coefficient_rank_ceiling
        == claims["coefficient_rank_ceiling"]
        and claims["coefficient_rank_ceiling"] == 19)
    checks.check(
        "C-4", f"THE EXCLUSION *EXTENDS*, ON THE SAME SIX CONTEXTS AND FROM THE "
        f"SAME ENVIRONMENT CACHE: Block 202's four-outcome stack re-measured "
        f"here is {claims['baseline_shape']} at ranks "
        f"{claims['baseline_ranks']} ({claims['baseline_common_exists']}), and "
        f"this block's twelve-outcome stack is {REFINED_STACK_SHAPE} at ranks "
        f"{REFINED_STACK_RANKS} -- so exclusion_extends = "
        f"{claims['exclusion_extends']} and Block 202's named class-value "
        f"escape closes at its FIRST natural attempt",
        alphabet.baseline_shape == claims["baseline_shape"]
        and alphabet.baseline_ranks == claims["baseline_ranks"]
        and claims["baseline_ranks"][0] != claims["baseline_ranks"][1]
        and alphabet.baseline_common_exists is claims["baseline_common_exists"]
        and claims["baseline_common_exists"] is False
        and claims["exclusion_extends"] is True
        and claims["baseline_shape"][1] < claims["stack_shape"][1])

    # --- D: THE MACROREALIST LANDSCAPE --------------------------------------
    checks.check(
        "D-1", f"THE DESIGN SPACE IS ENUMERATED AND NOT SAMPLED: "
        f"{len(LG_CHAINS)} three-slot chains {LG_CHAINS} drawn from the free "
        f"levels {FREE_LEVELS} with class-{LG_PIN_CLASS_VALUE} pins at the "
        f"first two slots, {len(LG_SPLIT_NAMES)} balanced dichotomizations "
        f"{LG_SPLIT_NAMES} and the {len(LG_VARIANTS)} deterministic upper "
        f"facets with sign products -1, labelled "
        f"{LG_VARIANTS} give exactly {claims['landscape_points']} design "
        f"points. The eight deterministic sign assignments give only -3 or 1 "
        f"for every facet ({claims['facet_truth_table_exact']}), proving the "
        f"upper bound without an imported premise. Every K uses the PROPOSED reading "
        f"{PROPOSED_READING}",
        landscape.points == claims["landscape_points"]
        and claims["landscape_points"]
        == len(LG_CHAINS) * len(LG_SPLIT_NAMES) * len(LG_VARIANTS)
        and landscape.facet_truth_table_exact
        is claims["facet_truth_table_exact"]
        and claims["facet_truth_table_exact"] is True)
    checks.check(
        "D-2", f"THE INSTRUMENT IS CALIBRATED BEFORE IT IS READ: all "
        f"the {claims['profile_checks']}-profile calibration set (four "
        f"record-free free-level profiles plus 48 pinned profiles), which "
        f"contains every landscape profile used, sums to one at "
        f"{claims['normalisation_defects']} "
        f"defects, and all {claims['component_checks']} exact components are "
        f"nonnegative at {claims['nonnegativity_defects']} defects",
        landscape.profile_checks == claims["profile_checks"]
        and landscape.component_checks == claims["component_checks"]
        and landscape.normalisation_defects == claims["normalisation_defects"]
        and landscape.nonnegativity_defects
        == claims["nonnegativity_defects"]
        and claims["normalisation_defects"] == ZERO_RESIDUAL
        and claims["nonnegativity_defects"] == ZERO_RESIDUAL)
    checks.check(
        "D-3", f"THE COMPLETE FOUR-FACET BOUND IS FORMULATED AND SATISFIED "
        f"ON THE ENUMERATED LANDSCAPE: each sign triple with product -1 holds at ALL "
        f"{LANDSCAPE_POINTS} design points with "
        f"{claims['landscape_violations']} violations "
        f"({claims['landscape_all_satisfy']}), and every one of them is "
        f"STRICTLY below the bound ({claims['landscape_all_strict']})",
        landscape.violations == claims["landscape_violations"]
        and claims["landscape_violations"] == 0
        and landscape.all_satisfy is claims["landscape_all_satisfy"]
        and claims["landscape_all_satisfy"] is True
        and landscape.all_strict is claims["landscape_all_strict"]
        and claims["landscape_all_strict"] is True)
    checks.check(
        "D-4", f"AND THE MAXIMUM IS UNIQUE, EXACT AND NOWHERE NEAR THE BOUND: "
        f"the largest K sits at chain {claims['landscape_argmax'][0]} split "
        f"{claims['landscape_argmax'][1]} variant {claims['landscape_argmax'][2]}"
        f" and is unique ({claims['landscape_max_unique']}); it is carried as "
        f"one exact rational with {claims['landscape_digits'][0]}-digit "
        f"numerator and {claims['landscape_digits'][1]}-digit denominator; its "
        f"margin to the bound is exactly negative "
        f"({claims['landscape_margin_negative']}) and EIGHTEEN times it is "
        f"still below the bound ({claims['landscape_eighteen']}); the smallest "
        f"K sits at {claims['landscape_argmin']} -- displays max "
        f"{landscape.table_display[landscape.argmax]}, min "
        f"{landscape.table_display[landscape.argmin]}",
        landscape.argmax == claims["landscape_argmax"]
        and landscape.argmin == claims["landscape_argmin"]
        and landscape.max_is_unique is claims["landscape_max_unique"]
        and claims["landscape_max_unique"] is True
        and sp.cancel(landscape.max_value - claims["landscape_max"]) == 0
        and (landscape.max_numerator_digits,
             landscape.max_denominator_digits) == claims["landscape_digits"]
        and landscape.margin_is_negative is claims["landscape_margin_negative"]
        and claims["landscape_margin_negative"] is True
        and landscape.max_times_eighteen_below is claims["landscape_eighteen"]
        and claims["landscape_eighteen"] is True)

    # --- E: THE PHASE-DIAL K SWEEP ------------------------------------------
    checks.check(
        "E-1", f"THE INSTRUMENT IS PINNED BEFORE IT IS FIRED, AND THE PIN IS "
        f"MEASURED: the holonomy action carries {claims['undialled_symbols']} "
        f"free symbols before the COMMITTED spatial dial "
        f"{{g_re: {SPATIAL_DIAL_REAL}, g_im: {SPATIAL_DIAL_IMAGINARY}}} is "
        f"applied and {claims['dialled_symbols']} after it, so every inverse in "
        f"this family is taken over QQ_I and never symbolically",
        sweep.undialled_symbols == claims["undialled_symbols"]
        and claims["undialled_symbols"] > 0
        and sweep.dialled_symbols == claims["dialled_symbols"]
        and claims["dialled_symbols"] == 0)
    checks.check(
        "E-2", f"THE DIAL MOVES K AND THE MOVEMENT IS REAL: across the "
        f"{len(TEMPORAL_DIAL_VALUES)} temporal dial values at the best design "
        f"point chain {BEST_CHAIN} split {BEST_SPLIT} variant {BEST_VARIANT}, "
        f"every K carries sign {claims['sweep_signs']}, the largest sits at "
        f"q = {claims['sweep_argmax_q']} and the smallest at "
        f"q = {claims['sweep_argmin_q']}, TWICE the spread exceeds the minimum "
        f"({claims['sweep_movement']}), and the successive differences change "
        f"sign exactly {claims['sweep_turning']} time -- displays "
        f"{tuple(sweep.displays[q] for q in TEMPORAL_DIAL_VALUES)}",
        sweep.signs == claims["sweep_signs"]
        and len(claims["sweep_signs"]) == len(TEMPORAL_DIAL_VALUES)
        and sweep.argmax_q == claims["sweep_argmax_q"]
        and sweep.argmin_q == claims["sweep_argmin_q"]
        and sweep.movement_exceeds_half_min is claims["sweep_movement"]
        and claims["sweep_movement"] is True
        and sweep.turning_points == claims["sweep_turning"]
        and claims["sweep_turning"] > 0)
    checks.check(
        "E-3", f"THE SEVEN DECLARED DIAL POINTS FORM AN EXACT NULL SAMPLE: "
        f"{claims['sweep_violations']} of the "
        f"{len(TEMPORAL_DIAL_VALUES)} swept values violate K <= "
        f"{LANDSCAPE_BOUND} ({claims['sweep_all_satisfy']}), TEN times the "
        f"largest swept value is still below the bound ({claims['sweep_ten']}), "
        f"all {claims['sweep_component_checks']} profile components used by "
        f"the sweep are nonnegative at "
        f"{claims['sweep_nonnegativity_defects']} defects, with "
        f"{claims['sweep_normalisation_defects']} profile-normalisation defects. "
        f"seven_point_null = {claims['seven_point_null']}; no value of q outside "
        f"the seven-point set is classified",
        sweep.violations == claims["sweep_violations"]
        and claims["sweep_violations"] == 0
        and sweep.all_satisfy is claims["sweep_all_satisfy"]
        and claims["sweep_all_satisfy"] is True
        and sweep.max_times_ten_below is claims["sweep_ten"]
        and claims["sweep_ten"] is True
        and sweep.component_checks == claims["sweep_component_checks"]
        and sweep.normalisation_defects
        == claims["sweep_normalisation_defects"]
        and sweep.nonnegativity_defects
        == claims["sweep_nonnegativity_defects"]
        and claims["sweep_normalisation_defects"] == 0
        and claims["sweep_nonnegativity_defects"] == 0
        and claims["seven_point_null"] is True)

    # --- F: THE SIX SCOPE FENCES -------------------------------------------
    checks.check(
        "F-1", f"FENCE ONE -- EVERY NUMBER IN FAMILIES D AND E IS TAKEN UNDER A "
        f"*PROPOSED* READING, AND BLOCK 202's JOINT-IDENTIFICATION FENCE STILL "
        f"STANDS: the reading is {PROPOSED_READING}, its "
        f"{claims['joint_halves']} halves are {JOINT_IDENTIFICATION_HALVES}, "
        f"which of them fails is OPEN ({claims['which_half_open']}), and "
        f"reading_identified = {claims['reading_identified']} -- a bound "
        f"SATISFIED under a proposed reading refutes nothing and licenses "
        f"nothing about Nature",
        claims["reading_identified"] is False
        and claims["joint_halves"] == len(JOINT_IDENTIFICATION_HALVES)
        and claims["joint_halves"] == 2
        and claims["which_half_open"] is True)
    checks.check(
        "F-2", f"FENCE TWO -- THE REFINED EXCLUSION IS "
        f"{claims['alphabet_tested']}-OUTCOME AND {CONTEXT_COUNT}-CONTEXT, AND "
        f"NO OUTCOME-COUNT TRIVIALITY THRESHOLD IS CLAIMED: "
        f"alphabet_exhaustive = {claims['alphabet_exhaustive']}, "
        f"{claims['untested_refinements']} richer refinements are named as NOT "
        f"tested. richer_alphabet_classified = "
        f"{claims['richer_alphabet_classified']}; six normalization relations "
        f"make the 25-row coefficient rank at most 19, and neither 19 nor 25 "
        f"outcomes is a spanning or consistency threshold without a proved "
        f"structured-column family",
        claims["alphabet_exhaustive"] is False
        and claims["alphabet_tested"] == REFINED_OUTCOMES
        and claims["untested_refinements"]
        == len(UNTESTED_ALPHABET_REFINEMENTS)
        and claims["untested_refinements"] > 0
        and claims["richer_alphabet_classified"] is False)
    checks.check(
        "F-3", f"FENCE THREE -- K <= {LANDSCAPE_BOUND} SATISFIED DOES *NOT* "
        f"ESTABLISH MACROREALISM: macrorealism_established = "
        f"{claims['macrorealism_established']}, the package is a NULL RESULT "
        f"for this instrument class ({claims['null_result_only']}), and the "
        f"licensed phrase is UNCHANGED from Block 202 "
        f"({claims['phrase_unchanged']}) and remains '{LICENSED_PHRASE}'; the "
        f"premises are scoped separately at B-5, so neither leans on the other",
        claims["macrorealism_established"] is False
        and claims["null_result_only"] is True
        and claims["phrase_unchanged"] is True)
    checks.check(
        "F-4", f"FENCE FOUR -- THE WORDS {NAMED_PHYSICS_WORDS} NAME A BOUND "
        f"*FORMULATED* HERE ({claims['bound_formulated']}) AND *NONE VIOLATED* "
        f"({claims['bounds_violated']} violations, bound_violated_claimed = "
        f"{claims['bound_violated_claimed']}): Block 202 declared these three "
        f"words unnamed because no bound existed there; this block writes one "
        f"down and it holds at every point measured",
        facts.named_words == claims["named_words"]
        and claims["bound_formulated"] is True
        and claims["bounds_violated"] == 0
        and claims["bound_violated_claimed"] is False)
    checks.check(
        "F-5", f"FENCE FIVE -- THE INSTANCE SCOPE, ENUMERATED RATHER THAN "
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
    checks.check(
        "F-6", f"FENCE SIX -- THE FINITE NULL SAMPLE IS NOT AN IMPOSSIBILITY: "
        f"violation_impossible = {claims['violation_impossible']}, "
        f"continuum_q_classified = {claims['continuum_q_classified']}, and "
        f"{claims['structural_changes']} structurally different instruments "
        f"({STRUCTURAL_CHANGES_REQUIRED}) are named as untested; the "
        f"{claims['scoped_words']} scoped headline words "
        f"{SCOPED_HEADLINE_WORDS} each name something narrower than they "
        f"suggest; the measured absence of a violation is gated separately at "
        f"D-3 and E-3, so neither leans on the other",
        claims["violation_impossible"] is False
        and claims["continuum_q_classified"] is False
        and claims["structural_changes"]
        == len(STRUCTURAL_CHANGES_REQUIRED)
        and claims["structural_changes"] > 0
        and facts.scoped_words == claims["scoped_words"])

    # --- G: THE NOTE, THE FENCE AND THE EXACTNESS HYGIENE -------------------
    checks.check(
        "G-1", f"the note is present at {NOTE_PATH.name} and the N5 fence "
        f"appears in it VERBATIM as a single line",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "G-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can collapse the finite exact landscape values, "
        f"destroy the uniqueness of the maximum, or turn a measured dial "
        f"movement into numerical noise",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "G-3", f"and {claims['float_literals']} float literals appear in that "
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
    alphabet, landscape, sweep = facts.alphabet, facts.landscape, facts.sweep
    print(f"MEASURED elapsed={elapsed_ns // 1000000000}s main={facts.main_head}")
    print(f"C refined={alphabet.stack_shape} ranks={alphabet.stack_ranks} "
          f"single={alphabet.single_ranks} baseline={alphabet.baseline_ranks} "
          f"row_ceiling={alphabet.coefficient_rank_ceiling}")
    print(f"D facets={landscape.points} truth_table="
          f"{landscape.facet_truth_table_exact} profile_checks="
          f"{landscape.profile_checks}/{landscape.component_checks} defects="
          f"{landscape.normalisation_defects}/"
          f"{landscape.nonnegativity_defects} violations={landscape.violations} "
          f"argmax={landscape.argmax}")
    print(f"E q_points={len(TEMPORAL_DIAL_VALUES)} "
          f"component_checks={sweep.component_checks} defects="
          f"{sweep.normalisation_defects}/{sweep.nonnegativity_defects} "
          f"violations={sweep.violations} argmax={sweep.argmax_q} "
          f"argmin={sweep.argmin_q}")
    print("SCOPE finite proposed-reading diagnostics only; richer alphabets, "
          "continuum q, physical joint identification, and other instruments remain open")


N5_FENCE = "\n".join((
    "N5: per_element: The twelve declared substitution outcomes, six marginal contexts, four deterministic facet signs, and seven q values are finite imposed algebraic objects. They do not constitute a measurement alphabet, identified joint law, continuum dial, hidden-variable model, or physical selector; nothing is registered or adopted.",
    "per_site: The single declared W9-L5 context is solvable at ranks (4,4), while the six-context unit-sum real system has ranks (8,9) with an augmented pivot. Six normalization relations cap the 25-row coefficient rank at 19; they do not create an outcome-count threshold, and every richer structured alphabet remains open.",
    "per_mode: The complete four deterministic upper facets are evaluated on four chains and three splits, giving 48 exact values. The 52-profile calibration set contains every landscape profile used; all profiles sum to one and all 208 components are nonnegative. Every facet is strictly below one, conditional on the proposed W9 formation-weight reading.",
    "per_block: At the seven declared q values, all 392 used profile components are nonnegative and the profiles are normalized; the sampled K values move nonmonotonically and stay below one. No continuum-q conclusion, no claim that tuning cannot cross, and no structurally different instrument is excluded.",
    "lattice_wide: The results are a finite null sample and a twelve-column incompatibility certificate on one bench. They neither establish macrorealism nor exclude classical models, richer alphabets, joint-pin instruments, other carriers, or other parameter values; all content remains proposed_retained and TOE movement is zero.",
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
