#!/usr/bin/env python3
"""Cycle 96: post-Cycles-93/94 operational-completeness audit.

This is a lightweight classification and dependency runner.  It consumes the
stable Cycle-91/93/94 evidence at its declared scope, checks the approved
primitive boundary, and verifies a falsifiable interface ledger.  It does not
rebuild a compiler, select Nature's law, amend an axiom, issue an audit
verdict, or modify foundation, registry, queue, policy, or git state.
"""

from __future__ import annotations

import ast
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
NOTE = REVIEW / "POST_CYCLE94_OPERATIONAL_COMPLETENESS_AUDIT_CYCLE96_NOTE_2026-07-15.md"

SOURCES = {
    "axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "scale": ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle80": REVIEW / "THREE_PHASE_RECURRENT_APPEND_TUBE_CYCLE80_NOTE_2026-07-14.md",
    "cycle84": REVIEW / "SEPARATED_RECURRENT_TUBE_COLLISION_CONTROL_CYCLE84_NOTE_2026-07-14.md",
    "cycle85": REVIEW / "CYCLE80_RECURRENCE_AUDIT_ENDPOINT_TUBE_NUCLEATION_CYCLE85_NOTE_2026-07-14.md",
    "cycle91": REVIEW / "LIVE_SELECTED_COMPILER_CLOSURE_REVISION_CYCLE91_NOTE_2026-07-15.md",
    "cycle93": REVIEW / "TOTAL_STATUS_SERIAL_REJECT_SELECTOR_CYCLE93_NOTE_2026-07-15.md",
    "cycle94": REVIEW / "LIVE_SEED_ROW_READABLE_MACROSTEP_CYCLE94_NOTE_2026-07-15.md",
    "contract": REVIEW / "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md",
    "cycle35": REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md",
    "cycle41": REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md",
    "cycle42": REVIEW / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md",
    "cycle44": REVIEW / "PROTECTED_MATTER_TRANSPORT_CYCLE44_NOTE_2026-07-14.md",
    "cycle83": REVIEW / "CONSTRUCTIVE_CONSTITUTIONAL_DELTA_AUDIT_CYCLE83_NOTE_2026-07-14.md",
    "actuality": REVIEW / "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md",
    "actuality_lit": REVIEW / "BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md",
    "probability": REVIEW / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "frequency": REVIEW / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md",
    "clock": REVIEW / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md",
    "gravity9": REVIEW / "LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md",
    "gravity10": REVIEW / "REVERSIBLE_DILATION_CLOSED_CYCLE_GRAVITY_CYCLE10_NOTE_2026-07-14.md",
    "matter": REVIEW / "MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md",
    "boundary": REVIEW / "HOMOGENEOUS_BOUNDARY_SEED_SELECTION_NOTE_2026-07-14.md",
    "toe": REVIEW / "TOE_INTERFACE_CONSTRUCTIVE_GATE_NOTE_2026-07-13.md",
    "uniqueness": REVIEW / "EXACT_LAW_UNIQUENESS_SELECTION_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md",
}

SOURCE_RUNNERS = {
    "cycle91_runner": ROOT / "scripts/live_selected_compiler_closure_revision_cycle91_2026_07_15.py",
    "cycle93_runner": ROOT / "scripts/total_status_serial_reject_selector_cycle93_2026_07_15.py",
    "cycle94_runner": ROOT / "scripts/live_seed_row_readable_macrostep_cycle94_2026_07_15.py",
}

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


THEOREM_TARGET = "THEOREM_TARGET"
EXACT_LAW_FIELD = "EXACT_LAW_FIELD"
REFERENCE_PRIMITIVE = "REFERENCE_PRIMITIVE"
EMPIRICAL_INPUT = "EMPIRICAL_INPUT"
GENUINE_CONSTITUTIONAL_ATOM = "GENUINE_CONSTITUTIONAL_ATOM"

CLASSIFICATIONS = {
    THEOREM_TARGET,
    EXACT_LAW_FIELD,
    REFERENCE_PRIMITIVE,
    EMPIRICAL_INPUT,
    GENUINE_CONSTITUTIONAL_ATOM,
}

SUPPLIED = "SUPPLIED_REFERENCE"
OPEN = "OPEN"
PARTIAL = "PARTIAL"
CONDITIONAL = "CONDITIONAL_OPEN"
DORMANT = "DORMANT_UNLESS_NONDERIVED_SELECTION"
STATUSES = {SUPPLIED, OPEN, PARTIAL, CONDITIONAL, DORMANT}


@dataclass(frozen=True)
class Interface:
    ident: str
    group: str
    classification: str
    status: str
    dependencies: tuple[str, ...]
    probe: str
    evidence: tuple[str, ...]


def item(
    ident: str,
    group: str,
    classification: str,
    status: str,
    dependencies: tuple[str, ...],
    pass_condition: str,
    fail_condition: str,
    evidence: tuple[str, ...],
) -> Interface:
    return Interface(
        ident,
        group,
        classification,
        status,
        dependencies,
        f"PASS iff {pass_condition}; FAIL if {fail_condition}.",
        evidence,
    )


INTERFACES = (
    # Approved references: dependencies may consume these without treating
    # them as walls or enlarging their source-note scope.
    item("REF_SCALE", "REFERENCE", REFERENCE_PRIMITIVE, SUPPLIED, (),
         "the registry points to the units-only a^-1=M_Pl source and no dimensionless claim is charged to it",
         "a coupling, rate, mass ratio, or gravity strength is imported from the unit choice",
         ("registry", "scale")),
    item("REF_KINETIC", "REFERENCE", REFERENCE_PRIMITIVE, SUPPLIED, (),
         "the registry grants only c_t=c_s kinetic-form isotropy",
         "dynamics, a Lorentz theorem, a clock rate, or a coupling is credited to it",
         ("registry", "kinetic")),
    item("REF_REALIZED_STATE", "REFERENCE", REFERENCE_PRIMITIVE, SUPPLIED, (),
         "the registry grants only pointwise evaluation at a supplied law-admissible realized state",
         "a state value, complete history, measure, selector, typicality, or past hypothesis is credited to it",
         ("registry", "realized")),

    # Exact-law base fields are upstream of every construction theorem.
    item("LAW_DOMAIN_STATE_CONTEXT", "EXACT_LAW", EXACT_LAW_FIELD, OPEN, (),
         "one exact carrier, predictive-state input, legal context/protocol category, and boundary-slot type is total on every claimed case",
         "any record-distinguishable state or legal intervention has no typed law input",
         ("contract", "cycle35")),
    item("LAW_ATOMIC_EVENT_KERNEL", "EXACT_LAW", EXACT_LAW_FIELD, OPEN,
         ("LAW_DOMAIN_STATE_CONTEXT",),
         "one exact parameter-fixed branch/update/history kernel gives normalized or deterministic answers on the entire declared domain",
         "the artifact is a family name, support-only slogan, partial table, or contains an unfixed record-distinguishing parameter",
         ("contract", "actuality_lit", "cycle41")),
    item("LAW_CONTINUATION_CONCURRENCY", "EXACT_LAW", THEOREM_TARGET, OPEN,
         ("LAW_ATOMIC_EVENT_KERNEL",),
         "finite composition, source-state evaluation, disjoint-order gauge, and every reachable overlap yield one projectively consistent record law",
         "one legal ordering or overlap changes the final record transcript outside the declared physical quotient",
         ("contract", "cycle35", "cycle41")),
    item("LAW_AVAILABILITY_PROJECTION", "EXACT_LAW", THEOREM_TARGET, OPEN,
         ("LAW_ATOMIC_EVENT_KERNEL",),
         "the live nearest-neighbor availability answer equals the exact positive-support or allowed-successor projection of the kernel on every context",
         "an available possibility has no supported continuation or a supported write is absent from Admissibility",
         ("contract", "cycle83")),
    item("LAW_RECORD_CONTRACT", "EXACT_LAW", THEOREM_TARGET, OPEN,
         ("LAW_ATOMIC_EVENT_KERNEL", "LAW_CONTINUATION_CONCURRENCY"),
         "the official decoder identifies formation and every later legal continuation preserves record identity and locked content",
         "an official record changes, disappears, is overwritten, or only survives by an untyped migratory equivalence",
         ("contract", "cycle35", "actuality_lit")),
    item("LAW_STATE_SUFFICIENCY", "EXACT_LAW", THEOREM_TARGET, OPEN,
         ("LAW_DOMAIN_STATE_CONTEXT", "LAW_RECORD_CONTRACT"),
         "equal complete record configurations have equal future transcript laws for every legal adaptive protocol after context, boundary, phase, and gauge are included",
         "two states in one record fibre have different future readable statistics",
         ("cycle35", "probability", "cycle44")),
    item("LAW_PHYSICAL_EQUIVALENCE", "EXACT_LAW", EXACT_LAW_FIELD, OPEN,
         ("LAW_DOMAIN_STATE_CONTEXT",),
         "the declared quotient preserves every finite legal adaptive record protocol, including phase, schedule, context, boundary, and recoding transformations",
         "two representatives called equivalent are separated by one legal record protocol",
         ("contract", "cycle35", "uniqueness")),

    # Seed-to-first physical compiler harness: the seven explicit Cycle-91
    # bootstrap clauses are kept separate so no supplied source is hidden.
    item("BOOT_MACROBLOCK_BIND", "SEED_TO_FIRST_HARNESS", THEOREM_TARGET, OPEN,
         ("LAW_ATOMIC_EVENT_KERNEL",),
         "the exact generated Cycle-85 endpoint, with zero supplied binary source records, grows its first validated eight-bit macroblock with the correct role decoder",
         "a flattened word, START, rail, or macroblock record is prewritten",
         ("cycle85", "cycle91", "cycle94")),
    item("BOOT_RELATIONAL_FRAME", "SEED_TO_FIRST_HARNESS", THEOREM_TARGET, OPEN,
         ("BOOT_MACROBLOCK_BIND",),
         "the grown seed records define all six ordered directions and all 24 proper-cubic images produce the transported slot order",
         "a coordinate axis, host orientation, or unrecorded epoch selects a port",
         ("cycle91", "boundary")),
    item("BOOT_OCCUPIED_ROUTES", "SEED_TO_FIRST_HARNESS", THEOREM_TARGET, OPEN,
         ("BOOT_MACROBLOCK_BIND", "BOOT_RELATIONAL_FRAME"),
         "actual validated occupied-neighbor words grow noncolliding routes into the first six-slot footprint",
         "any ordered input slot is filled from a supplied candidate stream or a neighboring route cross-fires",
         ("cycle91", "cycle94")),
    item("BOOT_CAGES", "SEED_TO_FIRST_HARNESS", THEOREM_TARGET, OPEN,
         ("BOOT_RELATIONAL_FRAME", "BOOT_OCCUPIED_ROUTES"),
         "the endpoint grows the OPEN, comparator, selector, and writer cages and the initial mixed frontier is exactly the intended one",
         "any cage record belongs to a supplied compiler-cell census or causes a parasite frontier",
         ("cycle91", "cycle94")),
    item("BOOT_PROGRAM_BANK", "SEED_TO_FIRST_HARNESS", THEOREM_TARGET, OPEN,
         ("BOOT_CAGES",),
         "all current 236 law programs and associated output words are physical grown records with one injective codebook and no host lookup",
         "the correct reference/output word is selected by Python, a symbolic oracle, or supplied bank records",
         ("cycle91", "cycle93", "cycle94")),
    item("BOOT_FRESH_RESERVATION", "SEED_TO_FIRST_HARNESS", THEOREM_TARGET, OPEN,
         ("BOOT_OCCUPIED_ROUTES", "BOOT_CAGES"),
         "the first completed harness reserves a disjoint successor footprint and every old guide/certificate/debris record is inert there",
         "one reachable old record fires a future cell or the reservation overlaps permanent source records",
         ("cycle91", "cycle94")),
    item("BOOT_STEADY_HANDOFF", "SEED_TO_FIRST_HARNESS", THEOREM_TARGET, OPEN,
         ("BOOT_CAGES", "BOOT_PROGRAM_BANK", "BOOT_FRESH_RESERVATION"),
         "one grown completion record uniquely starts the same physical cell type used by the steady macrostep",
         "the steady cell requires a supplied START, phase flag, candidate rail, or different host-only interface",
         ("cycle91", "cycle94")),

    # One physical strict-NN macrostep.  Cycle 94 retires only the one-row,
    # supplied-cell value-faithful output handoff instance.
    item("STEP_NEIGHBOUR_STREAM", "ONE_AUTONOMOUS_MACROSTEP", THEOREM_TARGET, OPEN,
         ("BOOT_STEADY_HANDOFF",),
         "each actual validated occupied-neighbor macroblock reaches its correct seed-relative slot without a supplied flattened 48-bit stream",
         "one slot is host-packed, permuted, duplicated, or populated from an unvalidated word",
         ("cycle91", "cycle94")),
    item("STEP_OPEN_PACK", "ONE_AUTONOMOUS_MACROSTEP", THEOREM_TARGET, OPEN,
         ("BOOT_STEADY_HANDOFF",),
         "every genuinely open direction grows reserved 11111111 and all occupied/open slots coexist without predecessor sharing or late-record ambiguity",
         "an EMPTY bit is prewritten or a later neighbor can leave a stale candidate accepted",
         ("cycle91", "cycle94")),
    item("STEP_SELECTOR_BANK", "ONE_AUTONOMOUS_MACROSTEP", THEOREM_TARGET, OPEN,
         ("BOOT_PROGRAM_BANK", "STEP_NEIGHBOUR_STREAM", "STEP_OPEN_PACK"),
         "one physical 236-reference bank exposes exactly one associated output port for every current candidate",
         "the correct reference is supplied alone or two bank ports can write",
         ("cycle91", "cycle93", "cycle94")),
    item("STEP_SELECTOR_TRANSPORT", "ONE_AUTONOMOUS_MACROSTEP", THEOREM_TARGET, OPEN,
         ("STEP_SELECTOR_BANK",),
         "a two-reference mismatch-then-match control carries the unchanged candidate across the first AUX trail and starts only the second writer, then the finite-bank induction closes",
         "candidate bit order changes, rejected-prefix debris fires, or the first mismatch exposes a writer",
         ("cycle91", "cycle93")),
    item("STEP_SELECTED_OUTPUT_BIND", "ONE_AUTONOMOUS_MACROSTEP", THEOREM_TARGET, PARTIAL,
         ("STEP_SELECTOR_TRANSPORT",),
         "every selected program port is physically bound to its own output word and a one-bit-swapped association control fails closed",
         "selection and writing can cross-associate or require a host output lookup",
         ("cycle91", "cycle94")),
    item("STEP_OUTPUT_NEXT_FRONT", "ONE_AUTONOMOUS_MACROSTEP", THEOREM_TARGET, PARTIAL,
         ("STEP_SELECTED_OUTPUT_BIND",),
         "for every reachable program the written value is re-read after VALID and becomes the literal occupied word consumed by the next physical comparator with no host decode",
         "completion alone starts the next row or any wrong word propagates",
         ("cycle91", "cycle94")),
    item("STEP_NEXT_CELL_ALLOCATE", "ONE_AUTONOMOUS_MACROSTEP", THEOREM_TARGET, OPEN,
         ("STEP_OUTPUT_NEXT_FRONT", "BOOT_FRESH_RESERVATION"),
         "the completed port grows the next candidate routes, reference source, readable writer, and following footprint with zero supplied compiler-cell records",
         "a successor rail/cage/program/START is supplied or allocated on occupied debris",
         ("cycle91", "cycle94")),
    item("STEP_FULL_MIXED_DOMAIN", "ONE_AUTONOMOUS_MACROSTEP", THEOREM_TARGET, OPEN,
         ("STEP_NEIGHBOUR_STREAM", "STEP_OPEN_PACK", "STEP_SELECTOR_TRANSPORT", "STEP_SELECTED_OUTPUT_BIND", "STEP_OUTPUT_NEXT_FRONT", "STEP_NEXT_CELL_ALLOCATE"),
         "all reachable rows, arities, asynchronous schedules, proper-cubic images, and full mixed-table signatures have one intended frontier and quiet record-faithful terminals",
         "one reachable schedule, rotation, old guide, rejected prefix, or writer debris produces a conflict, parasite, or wrong output",
         ("cycle91", "cycle93", "cycle94")),

    # Recurrent next-front and unbounded iteration.
    item("NEXT_PHASE_RETURN", "RECURRENT_NEXT_FRONT", THEOREM_TARGET, OPEN,
         ("STEP_OUTPUT_NEXT_FRONT", "STEP_FULL_MIXED_DOMAIN"),
         "one complete physical A/B/C period returns a value-decoded front of the same interface type and advances the logical recurrent law exactly once",
         "the exposed next comparator cannot complete the next output/phase or needs a reset token",
         ("cycle80", "cycle91", "cycle94")),
    item("NEXT_SELF_HOSTING", "RECURRENT_NEXT_FRONT", THEOREM_TARGET, OPEN,
         ("STEP_NEXT_CELL_ALLOCATE", "NEXT_PHASE_RETURN"),
         "the second and third cells are wholly grown by their predecessors and repeat the same local source census with zero supplied apparatus",
         "only the first cell works or later cells consume preplaced cages/banks",
         ("cycle91", "cycle94")),
    item("NEXT_INTERFACE_INVARIANT", "RECURRENT_NEXT_FRONT", THEOREM_TARGET, OPEN,
         ("NEXT_SELF_HOSTING", "LAW_RECORD_CONTRACT"),
         "a translation/proper-cubic transport maps each completed cell to the next while preserving decoder roles, fresh support, and every old record",
         "the inductive interface depends on absolute coordinates, hidden phase, or mutable old content",
         ("cycle80", "cycle91", "cycle94")),
    item("ITERATION_INDUCTION", "UNBOUNDED_ITERATION", THEOREM_TARGET, OPEN,
         ("NEXT_INTERFACE_INVARIANT", "STEP_FULL_MIXED_DOMAIN", "ITERATION_RENEWAL_EXPORT"),
         "a base case plus a preserved local invariant proves completion for arbitrary n, not only finite simulated horizons",
         "the proof uses a horizon bound, exhaustible prepared corridor, or n-dependent rule/cage",
         ("cycle80", "cycle91", "cycle94")),
    item("ITERATION_OCCURRENCE_SEMANTICS", "UNBOUNDED_ITERATION", EXACT_LAW_FIELD, OPEN,
         ("LAW_ATOMIC_EVENT_KERNEL", "LAW_CONTINUATION_CONCURRENCY"),
         "the exact law states deterministic, sampled, or fair occurrence semantics under which each enabled macrostep completes with the claimed probability",
         "the construction proves only possible appends while an admissible infinite schedule can starve the front",
         ("contract", "actuality_lit", "cycle41")),
    item("ITERATION_RENEWAL_EXPORT", "UNBOUNDED_ITERATION", EXACT_LAW_FIELD, OPEN,
         ("LAW_ATOMIC_EVENT_KERNEL", "LAW_RECORD_CONTRACT"),
         "fresh capacity, archive, garbage, and reusable working resource obey an exact balance that permits arbitrary n without record erasure or finite saturation",
         "a positive formation current fills a finite archive or exported information returns to corrupt a front",
         ("cycle35", "gravity10", "cycle44")),
    item("ITERATION_GLOBAL_EXTENSION", "UNBOUNDED_ITERATION", THEOREM_TARGET, OPEN,
         ("ITERATION_INDUCTION", "ITERATION_OCCURRENCE_SEMANTICS", "LAW_CONTINUATION_CONCURRENCY", "BOUNDARY_ALLOWED_CLASS"),
         "compatible finite restrictions extend to one full-lattice/history law unique up to the physical record quotient",
         "finite cylinders fail normalization/projectivity or two record-distinguishable global extensions survive the same inputs",
         ("contract", "cycle35", "cycle41")),

    # Reachable multi-apparatus domain.
    item("MULTI_REACHABLE_NUCLEATION", "MULTI_APPARATUS", THEOREM_TARGET, OPEN,
         ("BOOT_STEADY_HANDOFF", "BOUNDARY_ALLOWED_CLASS"),
         "one allowed boundary/history grows two physical compiler apparatuses with no supplied tube or cage records",
         "the factorization test begins from two externally placed symbolic tubes",
         ("cycle84", "cycle91")),
    item("MULTI_SEPARATION_INVARIANT", "MULTI_APPARATUS", THEOREM_TARGET, PARTIAL,
         ("MULTI_REACHABLE_NUCLEATION", "STEP_FULL_MIXED_DOMAIN", "ITERATION_INDUCTION"),
         "the complete expanded compiler supports, buses, writers, and debris preserve distance at least two and the joint graph factors for arbitrary horizon",
         "only the smaller Cycle-80 tube factors or any reachable compiler record enters the other support's nearest-neighbor shell",
         ("cycle84", "cycle91")),
    item("MULTI_CONTACT_RESOURCE_RULE", "MULTI_APPARATUS", EXACT_LAW_FIELD, CONDITIONAL,
         ("MULTI_REACHABLE_NUCLEATION",),
         "either a proved exclusion invariant makes contact unreachable or every reachable contact/resource-sharing signature has one exact physical branch law",
         "contact is reachable but absent from the table/process domain or resource ownership is host-decided",
         ("cycle84", "cycle91", "cycle44")),
    item("MULTI_CONFLUENCE_RECORD", "MULTI_APPARATUS", THEOREM_TARGET, OPEN,
         ("MULTI_SEPARATION_INVARIANT", "MULTI_CONTACT_RESOURCE_RULE", "LAW_RECORD_CONTRACT"),
         "all legal contact/order schedules reach record-equivalent terminals with no partial-prefix corruption and every old official record preserved",
         "two schedules yield different readable records outside the declared quotient or strand a permanent half-write",
         ("cycle84", "cycle91", "cycle44")),

    # Actuality.
    item("ACT_HISTORY_SEMANTICS", "ACTUALITY", EXACT_LAW_FIELD, OPEN,
         ("LAW_DOMAIN_STATE_CONTEXT", "LAW_ATOMIC_EVENT_KERNEL", "BOUNDARY_ALLOWED_CLASS"),
         "the candidate declares complete histories and one route—unique, law-realized, record-reconstructed, or explicit data-interface—to an actual member",
         "a support set or normalized measure is called one actual history without a route",
         ("actuality", "actuality_lit", "cycle41")),
    item("ACT_REALIZED_HISTORY_DATA", "ACTUALITY", EMPIRICAL_INPUT, OPEN,
         ("ACT_HISTORY_SEMANTICS", "BOUNDARY_ACTUAL_INSTANCE", "REF_REALIZED_STATE"),
         "one supplied actual history is law-admissible at every finite cut and all quoted contingent values are pointwise evaluations",
         "the primitive is used to choose the history or an observed value is labeled derived despite varying across allowed histories",
         ("actuality", "cycle42", "realized")),
    item("ACT_COUNTERFACTUAL_COVERAGE", "ACTUALITY", THEOREM_TARGET, OPEN,
         ("LAW_DOMAIN_STATE_CONTEXT", "LAW_PHYSICAL_EQUIVALENCE"),
         "the legal protocol corpus separates every record-distinguishable off-path/intervention law in the candidate class or proves full abstraction",
         "two laws agree on the realized path/corpus yet differ on one legal intervention",
         ("cycle42", "uniqueness")),
    item("ACT_TYPICALITY_GATE", "ACTUALITY", THEOREM_TARGET, CONDITIONAL,
         ("ACT_REALIZED_HISTORY_DATA", "PROB_NORMALIZED_OPERATIONAL_LAW", "PROB_FREQUENCY_THEOREM"),
         "every unconditional actual-world almost-sure claim proves h_* lies in the named set, derives support restriction, or remains explicitly conditional",
         "probability one is promoted to a pointwise fact about h_* without membership proof",
         ("actuality", "frequency", "cycle35")),

    # Probability and operational quantum closure.
    item("PROB_NORMALIZED_OPERATIONAL_LAW", "PROBABILITY", EXACT_LAW_FIELD, OPEN,
         ("LAW_DOMAIN_STATE_CONTEXT", "LAW_ATOMIC_EVENT_KERNEL"),
         "every record-defined preparation and finite adaptive legal protocol has one normalized conditional transcript measure on a faithful full qubit-effect repertoire",
         "only support, a nonselective channel, binary normalization, or a partial effect family is supplied",
         ("probability", "actuality_lit")),
    item("PROB_OPERATIONAL_COMPOSITION", "PROBABILITY", THEOREM_TARGET, OPEN,
         ("PROB_NORMALIZED_OPERATIONAL_LAW", "LAW_CONTINUATION_CONCURRENCY", "LAW_PHYSICAL_EQUIVALENCE"),
         "recorded mixing, exclusive coarse-graining, spectators, sequential composition, and ancillas preserve the declared quotient and transcript laws",
         "a transpose/hidden-memory/context control separates a claimed equivalent procedure",
         ("probability", "toe")),
    item("PROB_BORN_REPRESENTATION", "PROBABILITY", THEOREM_TARGET, OPEN,
         ("PROB_NORMALIZED_OPERATIONAL_LAW", "PROB_OPERATIONAL_COMPOSITION"),
         "the effect functional satisfies the Busch/CFMR premises and tomography returns one unique density representative with p=Tr(sigma E)",
         "the proof imports frame weights, omits full POVM compatibility, or identifies sigma with a separate rho without a bridge",
         ("probability",)),
    item("PROB_TRIAL_RESET_PROCESS", "PROBABILITY", EXACT_LAW_FIELD, OPEN,
         ("PROB_NORMALIZED_OPERATIONAL_LAW", "ITERATION_RENEWAL_EXPORT"),
         "record-visible preparation/close certificates define trials independently of pairing and the next predictive preparation class has the declared conditional process law",
         "old hidden memory can change later outcomes while one-shot marginals remain fixed",
         ("probability", "frequency")),
    item("PROB_FREQUENCY_THEOREM", "PROBABILITY", THEOREM_TARGET, OPEN,
         ("PROB_TRIAL_RESET_PROCESS",),
         "the exact joint process proves the claimed finite concentration and asymptotic IID, martingale, mixing, ergodic, or pointwise frequency statement",
         "the frozen-memory comparator has the same marginals but violates the claimed concentration",
         ("probability", "frequency")),
    item("PROB_PREPARATION_CORPUS_DATA", "PROBABILITY", EMPIRICAL_INPUT, OPEN,
         ("PROB_TRIAL_RESET_PROCESS", "REF_REALIZED_STATE"),
         "actual preparation, setting, close, and outcome records are supplied independently of the statistic used to test the law",
         "trial pairing, prepared-state labels, or exclusions are chosen after seeing the target frequencies",
         ("probability", "frequency")),

    # Local time and rate.
    item("TIME_COMMIT_EVENT", "LOCAL_TIME_RATE", EXACT_LAW_FIELD, OPEN,
         ("LAW_ATOMIC_EVENT_KERNEL", "LAW_RECORD_CONTRACT"),
         "the exact law identifies a record-visible local close/commit event before it is called a tick",
         "clock or read language substitutes for the occurrence condition",
         ("clock", "actuality_lit", "cycle94")),
    item("TIME_COMMIT_COUNT", "LOCAL_TIME_RATE", THEOREM_TARGET, PARTIAL,
         ("TIME_COMMIT_EVENT",),
         "the named clock-chain count is monotone, additive, schedule-invariant, and readable from records on every legal history",
         "total records, host steps, or one arbitrary refinement is silently counted instead",
         ("clock",)),
    item("TIME_COARSE_GRAIN_SYNCHRONIZATION", "LOCAL_TIME_RATE", THEOREM_TARGET, OPEN,
         ("TIME_COMMIT_COUNT", "LAW_PHYSICAL_EQUIVALENCE", "MULTI_CONFLUENCE_RECORD"),
         "record-free refinements quotient as gauge, record-visible refinements remain physical, and separated clocks have path/order-consistent comparison rules",
         "two legal comparison paths give different dimensionless clock ratios outside the quotient",
         ("clock", "toe")),
    item("TIME_RELATIVE_RATE_LAPSE", "LOCAL_TIME_RATE", EXACT_LAW_FIELD, OPEN,
         ("TIME_COMMIT_EVENT", "TIME_COARSE_GRAIN_SYNCHRONIZATION"),
         "one exact dimensionless relative-rate and load-dependent lapse map predicts every declared clock comparison",
         "the same event order admits distinct observable ratios or species-dependent lapse coefficients",
         ("clock", "gravity9", "gravity10")),
    item("TIME_METRIC_CONTINUUM", "LOCAL_TIME_RATE", THEOREM_TARGET, OPEN,
         ("TIME_RELATIVE_RATE_LAPSE", "REF_KINETIC", "BOUNDARY_ALLOWED_CLASS"),
         "clock/causal records converge with controlled errors to a Lorentzian proper-time/causal metric compatible with interactions and CPT diagnostics",
         "only a causal order, scalar tick, free dispersion, or c_t=c_s premise is shown",
         ("clock", "toe", "cycle41")),
    item("TIME_CALIBRATION_DATA", "LOCAL_TIME_RATE", EMPIRICAL_INPUT, OPEN,
         ("TIME_METRIC_CONTINUUM", "REF_SCALE"),
         "independent clock-comparison observations and the units reference calibrate only law-owned dimensionless predictions and one overall unit conversion",
         "the scale primitive is used to fit a dimensionless lapse/rate law",
         ("clock", "scale")),

    # Matter/species.
    item("MATTER_STABLE_READABLE_EXCITATION", "MATTER_SPECIES", THEOREM_TARGET, PARTIAL,
         ("LAW_ATOMIC_EVENT_KERNEL", "ITERATION_INDUCTION", "LAW_RECORD_CONTRACT"),
         "a localized or topological excitation persists/transports indefinitely, has a distinguishing legal record protocol, and carries a derived dispersion/conserved label",
         "the carrier is destroyed, operationally dark, or depends on a supplied clean corridor without a renewal theorem",
         ("cycle41", "cycle44", "toe")),
    item("MATTER_RECORD_STATE_DECODER", "MATTER_SPECIES", THEOREM_TARGET, OPEN,
         ("MATTER_STABLE_READABLE_EXCITATION", "LAW_STATE_SUFFICIENCY"),
         "preparation/lineage/syndrome records determine every future readable statistic of the carrier",
         "two identical record configurations with different carrier states are separated by a legal read",
         ("cycle44", "cycle35")),
    item("MATTER_COLLISION_INTERACTION", "MATTER_SPECIES", EXACT_LAW_FIELD, OPEN,
         ("MATTER_STABLE_READABLE_EXCITATION", "MULTI_CONTACT_RESOURCE_RULE", "MULTI_CONFLUENCE_RECORD"),
         "the exact two-or-more excitation collision/instrument has adequate output dimension, fixed phases/couplings, conserved labels, and record-faithful confluence",
         "two arbitrary inputs are merged into too small an output or scattering is omitted from the reachable domain",
         ("cycle44", "toe")),
    item("MATTER_EVENT_QUOTIENT_STATISTICS_CHIRALITY", "MATTER_SPECIES", EXACT_LAW_FIELD, OPEN,
         ("LAW_PHYSICAL_EQUIVALENCE", "PROB_NORMALIZED_OPERATIONAL_LAW", "MATTER_STABLE_READABLE_EXCITATION"),
         "legal record protocols fix the elementary event/effect quotient, exchange algebra, mirror/conjugate equivalence, and law-owned chirality or chiral-domain slot",
         "tied and untied or mirror-paired laws remain record-distinguishable while one branch is called a presentation ruling",
         ("matter", "toe")),
    item("MATTER_SPECIES_GAUGE_MASS", "MATTER_SPECIES", EXACT_LAW_FIELD, OPEN,
         ("MATTER_RECORD_STATE_DECODER", "MATTER_COLLISION_INTERACTION", "MATTER_EVENT_QUOTIENT_STATISTICS_CHIRALITY"),
         "one exact sector fixes species/generations, gauge carriers/dynamics, charges, masses, mixings, and every dimensionless coupling or derives them from the kernel",
         "a representation class, anomaly constraint, Koide arithmetic, or measured fit leaves a record-distinguishing coefficient/map free",
         ("matter", "uniqueness", "toe")),
    item("MATTER_INTERACTING_CONTINUUM", "MATTER_SPECIES", THEOREM_TARGET, OPEN,
         ("MATTER_SPECIES_GAUGE_MASS", "TIME_METRIC_CONTINUUM", "REF_KINETIC"),
         "the many-body record law has a controlled interacting Lorentz/CPT, locality, anomaly, and regulator-independence limit",
         "only a free Weyl walk, one-particle hopping mode, or finite lattice dispersion is controlled",
         ("uniqueness", "toe", "cycle41")),
    item("MATTER_EMPIRICAL_IDENTIFICATION", "MATTER_SPECIES", EMPIRICAL_INPUT, OPEN,
         ("MATTER_SPECIES_GAUGE_MASS", "MATTER_INTERACTING_CONTINUUM", "BOUNDARY_ACTUAL_INSTANCE", "REF_REALIZED_STATE"),
         "independent particle, mass, coupling, handedness, and scattering data identify the realized sector and test out-of-sample predictions",
         "measured masses or the observed hand are inserted upstream as derived law content",
         ("matter", "cycle44")),

    # Resource, thermodynamics, and tensor gravity.
    item("GR_RESOURCE_SOURCE_COEFFICIENTS", "TENSOR_GRAVITY", EXACT_LAW_FIELD, OPEN,
         ("ITERATION_RENEWAL_EXPORT", "TIME_COMMIT_EVENT"),
         "one conserved/monotone physical current distinguishes active source from archive count and fixes commit, export, diffusion, and response coefficients",
         "record count alone is called mass/source or a coefficient is chosen by the desired 1/r amplitude",
         ("gravity9", "gravity10", "toe")),
    item("GR_RENEWAL_THERMODYNAMIC_LIMIT", "TENSOR_GRAVITY", THEOREM_TARGET, OPEN,
         ("GR_RESOURCE_SOURCE_COEFFICIENTS", "ITERATION_INDUCTION", "BOUNDARY_ALLOWED_CLASS"),
         "the resource law avoids finite archive saturation and derives entropy, temperature, and arrow claims from the exact process plus named boundary/component",
         "a monotone record count is equated with thermodynamic entropy or irreversible current without a maintained bias/export route",
         ("gravity9", "gravity10", "toe")),
    item("GR_UNIVERSAL_COUPLING_WEP", "TENSOR_GRAVITY", THEOREM_TARGET, OPEN,
         ("GR_RESOURCE_SOURCE_COEFFICIENTS", "TIME_RELATIVE_RATE_LAPSE", "MATTER_SPECIES_GAUGE_MASS"),
         "all stable species and composites acquire the same local fractional clock and free-fall response, including transport terms, with composition-dependent controls null",
         "only onsite gaps share q while edge motion or one species carries an independent gamma_s or p_s",
         ("gravity9", "gravity10")),
    item("GR_TENSOR_NONLINEAR_RESPONSE", "TENSOR_GRAVITY", EXACT_LAW_FIELD, OPEN,
         ("GR_RESOURCE_SOURCE_COEFFICIENTS", "TIME_METRIC_CONTINUUM"),
         "one exact tensor or operationally equivalent source-response law fixes spatial curvature, lensing, nonlinear self-source, constraints, and conservation identity",
         "a scalar lapse/Poisson field leaves gamma_PPN, light bending, or self-coupling free",
         ("gravity9", "gravity10", "toe")),
    item("GR_CONTINUUM_EINSTEIN_LIMIT", "TENSOR_GRAVITY", THEOREM_TARGET, OPEN,
         ("GR_UNIVERSAL_COUPLING_WEP", "GR_TENSOR_NONLINEAR_RESPONSE", "MATTER_INTERACTING_CONTINUUM", "TIME_METRIC_CONTINUUM", "REF_KINETIC"),
         "the joint matter-gravity law converges with controlled corrections to the targeted Einstein/WEP/redshift/lensing regime",
         "only a finite 1/r fit, attractive sign, or common scalar scheduler is shown",
         ("gravity9", "gravity10", "toe")),
    item("GR_EMPIRICAL_MATCH_DATA", "TENSOR_GRAVITY", EMPIRICAL_INPUT, OPEN,
         ("GR_CONTINUUM_EINSTEIN_LIMIT", "TIME_CALIBRATION_DATA", "REF_SCALE"),
         "independent redshift, free-fall, lensing, orbital, wave, and cosmological data calibrate allowed parameters and falsify held-out predictions",
         "the units reference or a fitted Newton coefficient is reported as a foundation derivation",
         ("gravity9", "gravity10")),

    # Boundary and initial state.
    item("BOUNDARY_ALLOWED_CLASS", "BOUNDARY_INITIAL_STATE", EXACT_LAW_FIELD, OPEN,
         ("LAW_DOMAIN_STATE_CONTEXT",),
         "one exact covariant boundary/history class types every construction, intervention, limit, and conditional prediction",
         "a finite seed, clean ray, origin, orientation, or infinite program is silently supplied outside the class",
         ("contract", "boundary", "cycle41")),
    item("BOUNDARY_ACTUAL_INSTANCE", "BOUNDARY_INITIAL_STATE", EMPIRICAL_INPUT, OPEN,
         ("BOUNDARY_ALLOWED_CLASS", "REF_REALIZED_STATE"),
         "the actual seed/preparation/cosmological boundary is supplied as contingent world data and satisfies the allowed class",
         "the local law or realized-state primitive is said to choose its value",
         ("boundary", "cycle35", "realized")),
    item("BOUNDARY_SELECTION_LAW", "BOUNDARY_INITIAL_STATE", EXACT_LAW_FIELD, CONDITIONAL,
         ("BOUNDARY_ALLOWED_CLASS",),
         "every unconditional cosmological claim has a normalized measure, unique-selection theorem, or global constraint over allowed instances",
         "one law admits different boundary instances but unconditional records are predicted without a distribution/selector",
         ("boundary", "actuality")),
    item("BOUNDARY_LOW_ENTROPY_DATA", "BOUNDARY_INITIAL_STATE", EMPIRICAL_INPUT, OPEN,
         ("BOUNDARY_ACTUAL_INSTANCE",),
         "the observed low-record/low-entropy past and realized chiral/component data are named and their conditional consequences are tested",
         "the past hypothesis is hidden inside REF_REALIZED_STATE or inferred from append monotonicity alone",
         ("boundary", "cycle35", "realized")),
    item("BOUNDARY_HOMOGENEOUS_NUCLEATION", "BOUNDARY_INITIAL_STATE", THEOREM_TARGET, CONDITIONAL,
         ("BOUNDARY_ALLOWED_CLASS", "LAW_ATOMIC_EVENT_KERNEL"),
         "a translation-covariant positive-density, relational, global, or spacetime-nucleation route produces physical seeds without a privileged finite origin",
         "an exactly-one uniformly located seed on infinite Z^3 is assumed",
         ("boundary",)),
    item("BOUNDARY_WELLPOSED_CONTINUUM", "BOUNDARY_INITIAL_STATE", THEOREM_TARGET, OPEN,
         ("ITERATION_GLOBAL_EXTENSION", "MATTER_INTERACTING_CONTINUUM", "GR_CONTINUUM_EINSTEIN_LIMIT"),
         "the allowed class gives existence, uniqueness/equivalence, intervention compatibility, stability, and the same controlled matter/gravity continuum",
         "two record-distinguishable global solutions or boundary-sensitive continuum limits survive identical declared inputs",
         ("contract", "cycle35", "toe")),

    # Complete referent, scientific selection, and the only universal
    # constitutional candidate.  Empirical state values remain separate.
    item("LAW_COMPLETE_REFERENT", "EXACT_LAW", EXACT_LAW_FIELD, OPEN,
         ("LAW_AVAILABILITY_PROJECTION", "LAW_RECORD_CONTRACT", "LAW_STATE_SUFFICIENCY", "LAW_PHYSICAL_EQUIVALENCE", "ITERATION_GLOBAL_EXTENSION", "MULTI_CONFLUENCE_RECORD", "ACT_HISTORY_SEMANTICS", "ACT_COUNTERFACTUAL_COVERAGE", "PROB_BORN_REPRESENTATION", "PROB_FREQUENCY_THEOREM", "TIME_METRIC_CONTINUUM", "MATTER_INTERACTING_CONTINUUM", "GR_RENEWAL_THERMODYNAMIC_LIMIT", "GR_CONTINUUM_EINSTEIN_LIMIT", "BOUNDARY_WELLPOSED_CONTINUUM"),
         "one stable source/claim ID names a parameter-fixed object or transcript-equivalence class with every field, theorem, provenance, and machine gate present",
         "the referent contains a placeholder, unresolved parameter, omitted interface, source mismatch, or incompatible lane toy model",
         ("contract", "cycle35", "cycle83")),
    item("LAW_UNIQUENESS_OR_EQUIVALENCE", "EXACT_LAW", THEOREM_TARGET, OPEN,
         ("LAW_COMPLETE_REFERENT", "LAW_PHYSICAL_EQUIVALENCE"),
         "the current foundation plus explicitly approved references determines one complete record-predictive class on every legal protocol",
         "two complete foundation-compatible classes disagree on one legal record probability",
         ("uniqueness", "cycle35")),
    item("LAW_SELECTION_DATA", "EXACT_LAW", EMPIRICAL_INPUT, OPEN,
         ("LAW_COMPLETE_REFERENT", "LAW_PHYSICAL_EQUIVALENCE"),
         "prespecified separating protocols and independent data select/falsify complete candidate classes and fix every empirical law-owned parameter with held-out checks",
         "selection uses only the realized path where off-path laws agree or tunes an omitted parameter to the target",
         ("cycle42", "uniqueness")),
    item("LAW_IDENTITY_IF_NONDERIVED", "EXACT_LAW", GENUINE_CONSTITUTIONAL_ATOM, DORMANT,
         ("LAW_COMPLETE_REFERENT", "LAW_UNIQUENESS_OR_EQUIVALENCE", "LAW_SELECTION_DATA"),
         "a complete stable law is scientifically selected, no retained complete uniqueness theorem closes the zero-edit route after the declared audit, and one exact identity excludes record-distinguishable models once",
         "the referent is incomplete, selection is provisional, uniqueness remains live without an audit, or mechanism prose is substituted for extensional identity",
         ("cycle35", "cycle83", "uniqueness")),
)


def source_contract() -> None:
    section("A - Source, authority, and approved-primitive contract")
    for name, path in {"cycle96_note": NOTE, **SOURCES, **SOURCE_RUNNERS}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    for name, path in SOURCE_RUNNERS.items():
        try:
            ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            check(f"A {name} parses", False, str(exc))
        else:
            check(f"A {name} parses", True)

    registry = json.loads(SOURCES["registry"].read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    check("A registry contains exactly foundation plus three approved primitives",
          set(nodes) == {"minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"},
          str(sorted(nodes)))
    check("A registry paths match the three consumed source notes", all(
        ROOT / nodes[node]["current_path"] == SOURCES[key]
        for node, key in (
            ("scale_reference_primitive", "scale"),
            ("kinetic_isotropy_primitive", "kinetic"),
            ("realized_state_primitive", "realized"),
        )
    ))

    texts = {name: normalized(path) for name, path in SOURCES.items()}
    check("A Admissibility remains an availability slot, not hidden dynamics", all(
        needle in texts["axioms"] for needle in (
            "there is one fixed nearest-neighbor admissibility rule",
            "admissibility is not a dynamics axiom",
            "does not choose a hamiltonian or transfer operator",
            "formation rules (which",
        )
    ))
    check("A scale reference remains units-only", all(
        needle in texts["scale"] for needle in ("units conversion, not a physics axiom", "zero dimensionless content")
    ))
    check("A kinetic reference remains form-only", all(
        needle in texts["kinetic"] for needle in ("c_t = c_s", "not a new dynamics", "full lorentz restoration remain separate theorem/support claims")
    ))
    check("A realized-state reference remains pointwise-only", all(
        needle in texts["realized"] for needle in ("one realized-state reference", "no state, averaging over alternatives, measure", "past hypothesis")
    ))


def post_cycle94_evidence_contract() -> None:
    section("B - Stable Cycle-91/93/94 evidence and exact residual boundary")
    c91 = normalized(SOURCES["cycle91"])
    c93 = normalized(SOURCES["cycle93"])
    c94 = normalized(SOURCES["cycle94"])
    check("B Cycle91 pins the live 236/5240/153 inventory",
          "236 canonical / 5,240 raw / 153 roles" in c91)
    check("B Cycle91 preserves W_BOOT/W_STEP/W_MULTI", all(
        needle in c91 for needle in ("w_boot", "w_step", "w_multi", "pairwise independence")
    ))
    check("B Cycle93 closes the supplied-stream decision primitive", all(
        needle in c93 for needle in (
            "every one of the 236 live programs",
            "all 11,328 one-bit perturbations write aux and then stop",
            "55,460 ordered unequal pairs",
            "post-reject state is quiet",
        )
    ))
    check("B Cycle93 leaves exact AUX transport residual", all(
        needle in c93 for needle in ("aux_gated_candidate_transport", "candidate/reference streams", "reference bank")
    ))
    check("B Cycle93 corrected first-difference scope is exact", all(
        needle in c93 for needle in ("first differences at 26 of the 48 positions", "exercises all 48 mismatch positions")
    ))
    check("B Cycle94 pins 472 supplied and 132 grown", all(
        needle in c94 for needle in ("472 supplied compiler-cell records", "132 dynamic appends", "133", "941,784")
    ))
    check("B Cycle94 closes only one value-faithful output-to-front instance", all(
        needle in c94 for needle in ("validated_output_word_to_logical_front", "r_b11", "r_b10", "does not close general w_step")
    ))
    check("B Cycle94 retains every named construction residual", all(
        needle in c94 for needle in (
            "neighbour_macroblocks_to_ordered_stream",
            "empty_slot_to_six_slot_candidate_geometry",
            "serial_program_selection",
            "seed_to_rule_port_output_harness",
            "repeated_cell_allocation",
            "general_w_step_and_w_multi",
        )
    ))
    check("B Cycle84 is only a supplied separated-tube factorization", all(
        needle in normalized(SOURCES["cycle84"]) for needle in (
            "minimum manhattan distance", "does not resolve adjacent collisions", "nucleate either tube"
        )
    ))


def ledger_contract() -> None:
    section("C - Interface classification and coverage")
    identities = [entry.ident for entry in INTERFACES]
    check("C every interface ID is unique", len(identities) == len(set(identities)))
    check("C every interface has one allowed classification", all(entry.classification in CLASSIFICATIONS for entry in INTERFACES))
    check("C every interface has one allowed status", all(entry.status in STATUSES for entry in INTERFACES))
    check("C every probe is explicitly falsifiable", all(entry.probe.startswith("PASS iff ") and "; FAIL if " in entry.probe for entry in INTERFACES))
    check("C every evidence key names a source", all(key in SOURCES for entry in INTERFACES for key in entry.evidence))

    required_groups = {
        "REFERENCE",
        "SEED_TO_FIRST_HARNESS",
        "ONE_AUTONOMOUS_MACROSTEP",
        "RECURRENT_NEXT_FRONT",
        "UNBOUNDED_ITERATION",
        "MULTI_APPARATUS",
        "EXACT_LAW",
        "ACTUALITY",
        "PROBABILITY",
        "LOCAL_TIME_RATE",
        "TENSOR_GRAVITY",
        "MATTER_SPECIES",
        "BOUNDARY_INITIAL_STATE",
    }
    groups = {entry.group for entry in INTERFACES}
    check("C every requested construction and TOE group is present", groups == required_groups, str(sorted(groups)))

    counts = Counter(entry.classification for entry in INTERFACES)
    check("C there are exactly three supplied reference primitives", counts[REFERENCE_PRIMITIVE] == 3 and all(
        entry.status == SUPPLIED for entry in INTERFACES if entry.classification == REFERENCE_PRIMITIVE
    ))
    constitutional = [entry for entry in INTERFACES if entry.classification == GENUINE_CONSTITUTIONAL_ATOM]
    check("C only conditional exact-law identity is constitutional", len(constitutional) == 1 and constitutional[0].ident == "LAW_IDENTITY_IF_NONDERIVED" and constitutional[0].status == DORMANT)
    check("C no construction or TOE-lane item is mislabeled constitutional", all(
        entry.group == "EXACT_LAW" for entry in constitutional
    ))
    check("C empirical values remain separate from primitives", all(
        entry.classification != REFERENCE_PRIMITIVE for entry in INTERFACES if entry.ident in {
            "ACT_REALIZED_HISTORY_DATA", "BOUNDARY_ACTUAL_INSTANCE", "BOUNDARY_LOW_ENTROPY_DATA",
            "PROB_PREPARATION_CORPUS_DATA", "TIME_CALIBRATION_DATA", "MATTER_EMPIRICAL_IDENTIFICATION",
            "GR_EMPIRICAL_MATCH_DATA", "LAW_SELECTION_DATA",
        }
    ))
    check("C Cycle94 partial credit is restricted to two handoff rows", {
        entry.ident for entry in INTERFACES if entry.group == "ONE_AUTONOMOUS_MACROSTEP" and entry.status == PARTIAL
    } == {"STEP_SELECTED_OUTPUT_BIND", "STEP_OUTPUT_NEXT_FRONT"})


def dependency_contract() -> None:
    section("D - Dependency graph")
    by_id = {entry.ident: entry for entry in INTERFACES}
    missing = sorted({dep for entry in INTERFACES for dep in entry.dependencies if dep not in by_id})
    check("D every dependency resolves", not missing, str(missing))

    indegree = {ident: 0 for ident in by_id}
    outgoing: dict[str, list[str]] = defaultdict(list)
    for entry in INTERFACES:
        for dep in entry.dependencies:
            indegree[entry.ident] += 1
            outgoing[dep].append(entry.ident)
    queue = deque(sorted(ident for ident, degree in indegree.items() if degree == 0))
    order: list[str] = []
    while queue:
        ident = queue.popleft()
        order.append(ident)
        for successor in sorted(outgoing[ident]):
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)
    cyclic = sorted(ident for ident, degree in indegree.items() if degree)
    check("D dependency graph is acyclic", len(order) == len(INTERFACES), str(cyclic))

    def ancestors(ident: str) -> set[str]:
        seen: set[str] = set()
        todo = list(by_id[ident].dependencies)
        while todo:
            current = todo.pop()
            if current in seen:
                continue
            seen.add(current)
            todo.extend(by_id[current].dependencies)
        return seen

    complete_ancestors = ancestors("LAW_COMPLETE_REFERENT")
    required_ancestors = {
        "BOOT_STEADY_HANDOFF",
        "STEP_FULL_MIXED_DOMAIN",
        "ITERATION_GLOBAL_EXTENSION",
        "MULTI_CONFLUENCE_RECORD",
        "ACT_HISTORY_SEMANTICS",
        "PROB_BORN_REPRESENTATION",
        "PROB_FREQUENCY_THEOREM",
        "TIME_METRIC_CONTINUUM",
        "MATTER_INTERACTING_CONTINUUM",
        "GR_CONTINUUM_EINSTEIN_LIMIT",
        "BOUNDARY_WELLPOSED_CONTINUUM",
    }
    check("D complete referent depends on every requested high-level interface", required_ancestors <= complete_ancestors, str(sorted(required_ancestors - complete_ancestors)))
    check("D constitutional identity is downstream of completeness, uniqueness audit, and selection data", {
        "LAW_COMPLETE_REFERENT", "LAW_UNIQUENESS_OR_EQUIVALENCE", "LAW_SELECTION_DATA"
    } <= ancestors("LAW_IDENTITY_IF_NONDERIVED"))
    check("D actual boundary and history values do not become ancestors of universal law identity", not {
        "BOUNDARY_ACTUAL_INSTANCE", "ACT_REALIZED_HISTORY_DATA", "BOUNDARY_LOW_ENTROPY_DATA"
    } & ancestors("LAW_IDENTITY_IF_NONDERIVED"))


def note_and_no_go_contract() -> None:
    section("E - Cycle96 note, N1-N8, and scope contract")
    raw_lines = NOTE.read_text(encoding="utf-8").splitlines()
    note = normalized(NOTE)
    check("E note declares authority none", "authority: none" in note)
    check("E note denies foundation, queue, commit, push, and PR authority", all(
        needle in note for needle in ("no foundation", "no queue", "no commit", "no push", "no pr")
    ))
    check("E every interface ID appears in the note", all(entry.ident.lower() in note for entry in INTERFACES))
    missing_rows = []
    for entry in INTERFACES:
        own_rows = [
            line for line in raw_lines
            if f"`{entry.ident}`" in line
            and entry.classification in line
            and entry.status in line
            and "fail" in line.lower()
        ]
        if not own_rows:
            missing_rows.append(entry.ident)
    check("E every interface has a classified falsifiable table row", not missing_rows, str(missing_rows))
    check("E note includes all five classifications", all(classification.lower() in note for classification in CLASSIFICATIONS))
    check("E note contains N1 through N8", all(f"n{index}" in note for index in range(1, 9)))
    check("E N1 preserves at least five live routes", all(
        route in note for route in (
            "selected binary compiler",
            "monolithic self-growing macrocell",
            "z-only spatial code",
            "reversible qca workspace",
            "global-history law",
            "unique-class intersection",
        )
    ))
    check("E N2 collapses constitutional count to one conditional atom", all(
        needle in note for needle in ("collapsed constitutional set", "{l_id}", "record and qualification are conditional compatibility gates")
    ))
    check("E N3 required phrase scan is written", all(
        phrase in note for phrase in (
            "we assume", "by construction", "as is standard", "the framework provides",
            "bridge context", "background", "naturally", "obviously", "standard qft",
            "registered / canonical",
        )
    ))
    check("E N4 exact Cycle91/93/94 residuals are matched", all(
        needle in note for needle in ("aux_gated_candidate_transport", "validated_output_word_to_logical_front", "w_boot / w_step / w_multi")
    ))
    check("E N5 preserves finite-to-TOE resolution boundary", all(
        needle in note for needle in ("one supplied cell", "all 236 rows", "unbounded full lattice", "interacting continuum", "complete toe")
    ))
    check("E N6 reports approved primitive scopes without enlarging them", all(
        needle in note for needle in ("units only", "c_t=c_s form only", "pointwise realized-state reference only")
    ))
    check("E N7 keeps zero-edit intersection theorem live", "strongest hostile steelman" in note and "zero-edit" in note)
    check("E N8 records the constructive retirement mechanism", all(
        needle in note for needle in ("broad cl4", "formation existence versus rate", "record reclassification", "constructive compilation")
    ))
    check("E scoped status rejects universal no-go", all(
        needle in note for needle in ("partial operational census", "not a universal no-go", "no live axiom edit")
    ))

    body = note.split("## no-go discipline gate", 1)[0]
    hidden = [phrase for phrase in (
        "we assume", "as is standard", "the framework provides", "naturally follows", "obviously", "standard qft"
    ) if phrase in body]
    check("E scientific body contains no premise-hiding phrase", not hidden, str(hidden))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_contract()
    post_cycle94_evidence_contract()
    ledger_contract()
    dependency_contract()
    note_and_no_go_contract()
    classifications = Counter(entry.classification for entry in INTERFACES)
    groups = Counter(entry.group for entry in INTERFACES)
    print(f"\nINTERFACES={len(INTERFACES)} CLASSIFICATIONS={dict(sorted(classifications.items()))}")
    print(f"GROUPS={dict(sorted(groups.items()))}")
    print("CYCLE94_BASELINE=43/0 SUPPLIED_CELL=472 DYNAMIC_APPENDS=132")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
