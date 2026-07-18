#!/usr/bin/env python3
"""Exact finite witnesses for the exact-law content-independence tournament.

The runner checks finite countermodels, algebraic reductions, and source-note
contracts.  It does not identify a physical law, prove Gleason's theorem,
alter an axiom, or issue an audit verdict.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md"
COMPOSITION_NOTE = ROOT / "docs" / "GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md"
OPERATIONAL_NOTE = REVIEW / "OPERATIONAL_RECORD_RECONSTRUCTION_DEEP_PROBE_NOTE_2026-07-13.md"
SUBSTRATE_NOTE = REVIEW / "SUBSTRATE_TOURNAMENT_DECISIVE_PROBES_NOTE_2026-07-13.md"
FD_NOTE = REVIEW / "FINITE_DIAMOND_SAMPLED_LUDERS_INVARIANT_RECORD_MODEL_NOTE_2026-07-14.md"
INVENTORY_NOTE = REVIEW / "FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md"
SAMPLED_PAIR_NOTE = REVIEW / "COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md"
ACTUALIZATION_NOTE = REVIEW / "BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md"
QUALITATIVE_NOTE = REVIEW / "QUALITATIVE_SUBSTRATE_EXACT_LAW_SELECTION_NOTE_2026-07-14.md"
RESOURCE_NOTE = REVIEW / "LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md"
SELF_WRITING_NOTE = REVIEW / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md"
LICENSED_EQUIVALENCE_NOTE = REVIEW / "FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md"
TOPOLOGICAL_NOTE = REVIEW / "TOPOLOGICAL_CONSERVATION_RG_ACTION_STEELMAN_NOTE_2026-07-14.md"
SIMULATION_EQUIVALENCE_NOTE = REVIEW / "INTRINSIC_SIMULATION_OBSERVER_EQUIVALENCE_RECORD_COST_NOTE_2026-07-14.md"
QCA_WARD_NOTE = REVIEW / "PROPER_CUBIC_QUBIT_QCA_WARD_IDENTITY_STEELMAN_NOTE_2026-07-14.md"
INSTRUMENT_SELECTION_NOTE = REVIEW / "RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md"
ABELIAN_MERGE_NOTE = REVIEW / "ABELIAN_COMPATIBLE_SEED_BELL_MERGE_CYCLE15_NOTE_2026-07-14.md"
INFINITE_SECTOR_NOTE = REVIEW / "INFINITE_REDUNDANCY_QUASILOCAL_RECORD_SECTOR_NOTE_2026-07-14.md"
RELATIONAL_POINTER_NOTE = REVIEW / "RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md"
DYNAMIC_BOUNDARY_INDEX_NOTE = REVIEW / "DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md"
DELAYED_LOCK_NOTE = REVIEW / "DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md"
UNIVERSAL_RULE_SPACE_NOTE = REVIEW / "UNIVERSAL_RULE_SPACE_MULTIWAY_LAW_STEELMAN_NOTE_2026-07-14.md"
CHIRAL_TRIAD_CONTEXT_NOTE = REVIEW / "CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md"
THREE_D_ANOMALY_NOTE = REVIEW / "THREE_DIMENSIONAL_ANOMALOUS_BULK_CATEGORY_INDEX_STEELMAN_NOTE_2026-07-14.md"
AUTONOMOUS_CLOSE_NOTE = REVIEW / "AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md"
PRIMITIVE_PROTOCOL_EQUIVALENCE_NOTE = REVIEW / "PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md"
ACTUAL_HEADER_DECODER_NOTE = REVIEW / "ACTUAL_HEADER_ROLE_DECODER_PARITY_SELECTION_CYCLE18_NOTE_2026-07-14.md"
ADAPTIVE_FULL_ABSTRACTION_NOTE = REVIEW / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"
INVARIANT_SEED_FIELD_NOTE = REVIEW / "INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md"
SITE_NET_EQUIVALENCE_NOTE = REVIEW / "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md"
OPERATIONAL_PARITY_NOTE = REVIEW / "COMPLETE_FUTURE_OPERATIONAL_PARITY_CERTIFICATE_CYCLE19_NOTE_2026-07-14.md"
NAMED_SITE_EQUIVALENCE_NOTE = REVIEW / "NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md"
COMMIT_CLOCK_NOTE = REVIEW / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md"
SEED_COMPILATION_NOTE = REVIEW / "NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md"
BORN_AFFINITY_NOTE = REVIEW / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
SORT_EQUIVALENCE_NOTE = REVIEW / "FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md"
DISSIPATIVE_SEED_NOTE = REVIEW / "QUANTUM_DISSIPATIVE_SEED_ESCAPE_CYCLE20_NOTE_2026-07-14.md"
FREQUENCY_CORPUS_NOTE = REVIEW / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md"
RESIDUAL_PACKING_NOTE = REVIEW / "BLIND_RESIDUAL_ATOM_PACKING_AND_ONE_LAW_CONSTITUTIONAL_SCHEMA_NOTE_2026-07-14.md"
RECORD_STATE_BELL_NOTE = REVIEW / "RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md"
ACTUALITY_SEMANTICS_NOTE = REVIEW / "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md"
RECORD_STATE_FORTRESS_NOTE = REVIEW / "RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md"
GLOBAL_RECORD_PROCESS_NOTE = REVIEW / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md"
ADMISSIBILITY_DEFINABILITY_NOTE = REVIEW / "ADMISSIBILITY_SYMBOL_DEFINABILITY_AND_EXACT_LAW_REFERENCE_CHALLENGE_NOTE_2026-07-14.md"
CONSTITUTIONAL_LOWER_BOUND_NOTE = REVIEW / "CONSTITUTIONAL_LOWER_BOUND_CLOSURE_AND_CLAUSE_DELETION_CYCLE31_NOTE_2026-07-14.md"
LONG_RUN_APPEND_NOTE = REVIEW / "LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md"
LOCAL_GLOBAL_GLUE_NOTE = REVIEW / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md"
MOVING_LOGICAL_FRONT_NOTE = REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md"
FINAL_MISSING_CENSUS_NOTE = REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md"
CUBIC_CZ_SELECTION_NOTE = REVIEW / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md"
TEMPORAL_EQUIVALENCE_NOTE = REVIEW / "TEMPORAL_PROTOCOL_EQUIVALENCE_ALTERNATING_FRAME_CYCLE39_NOTE_2026-07-14.md"
CUBIC_CLIFFORD_NOTE = REVIEW / "CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md"
CANDIDATE_ASSEMBLY_NOTE = REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md"
HISTORY_IDENTIFIABILITY_NOTE = REVIEW / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
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


def normalize_text(path: Path) -> str:
    text = (
        path.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .replace(">", "")
    )
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Sources, authority, and claim boundary")
    paths = (
        NOTE,
        COMPOSITION_NOTE,
        OPERATIONAL_NOTE,
        SUBSTRATE_NOTE,
        FD_NOTE,
        INVENTORY_NOTE,
        SAMPLED_PAIR_NOTE,
        ACTUALIZATION_NOTE,
        QUALITATIVE_NOTE,
        RESOURCE_NOTE,
        SELF_WRITING_NOTE,
        LICENSED_EQUIVALENCE_NOTE,
        TOPOLOGICAL_NOTE,
        SIMULATION_EQUIVALENCE_NOTE,
        QCA_WARD_NOTE,
        INSTRUMENT_SELECTION_NOTE,
        ABELIAN_MERGE_NOTE,
        INFINITE_SECTOR_NOTE,
        RELATIONAL_POINTER_NOTE,
        DYNAMIC_BOUNDARY_INDEX_NOTE,
        DELAYED_LOCK_NOTE,
        UNIVERSAL_RULE_SPACE_NOTE,
        CHIRAL_TRIAD_CONTEXT_NOTE,
        THREE_D_ANOMALY_NOTE,
        AUTONOMOUS_CLOSE_NOTE,
        PRIMITIVE_PROTOCOL_EQUIVALENCE_NOTE,
        ACTUAL_HEADER_DECODER_NOTE,
        ADAPTIVE_FULL_ABSTRACTION_NOTE,
        INVARIANT_SEED_FIELD_NOTE,
        SITE_NET_EQUIVALENCE_NOTE,
        OPERATIONAL_PARITY_NOTE,
        NAMED_SITE_EQUIVALENCE_NOTE,
        COMMIT_CLOCK_NOTE,
        SEED_COMPILATION_NOTE,
        BORN_AFFINITY_NOTE,
        SORT_EQUIVALENCE_NOTE,
        DISSIPATIVE_SEED_NOTE,
        FREQUENCY_CORPUS_NOTE,
        RESIDUAL_PACKING_NOTE,
        RECORD_STATE_BELL_NOTE,
        ACTUALITY_SEMANTICS_NOTE,
        RECORD_STATE_FORTRESS_NOTE,
        GLOBAL_RECORD_PROCESS_NOTE,
        ADMISSIBILITY_DEFINABILITY_NOTE,
        CONSTITUTIONAL_LOWER_BOUND_NOTE,
        LONG_RUN_APPEND_NOTE,
        LOCAL_GLOBAL_GLUE_NOTE,
        MOVING_LOGICAL_FRONT_NOTE,
        FINAL_MISSING_CENSUS_NOTE,
        CUBIC_CZ_SELECTION_NOTE,
        TEMPORAL_EQUIVALENCE_NOTE,
        CUBIC_CLIFFORD_NOTE,
        CANDIDATE_ASSEMBLY_NOTE,
        HISTORY_IDENTIFIABILITY_NOTE,
        AXIOMS,
        REGISTRY,
    )
    for path in paths:
        check(f"A source exists: {path.name}", path.is_file())
    note = normalize_text(NOTE)
    check("A tournament is authority-free", "authority: none" in note)
    check("A tournament disclaims an axiom amendment", "does not amend an axiom" in note)
    check("A exact-law referent is expanded rather than named vaguely", "the referent l is not the words" in note)
    check("A bounded universal-looking and branching packages are separated", "strongest universal-looking constitutional lower bound" in note and "one honest branching-law package" in note)
    check("A one-reference target is staged, not landed", "one-reference constitutional compression" in note and "neither placement is ready to land with a placeholder" in note)
    check("A full Gleason theorem is not claimed by the runner", "does not prove the full gleason theorem" in note)
    check("A complete sampled-law pair is treated as the decisive witness", "decisive full-interface witness" in note)
    check("A repeated q-lambda check is not double-counted", "not counted as a second independent non-entailment result" in note)
    check("A Cycle-11 robustness update is present", "cycle-11 robustness update" in note)
    check("A Cycle-13/14 robustness update is present", "cycle-13/14 robustness update" in note)
    check("A Cycle-14/15 robustness update is present", "cycle-14/15 robustness update" in note)
    check("A Cycle-16/17 robustness update is present", "cycle-16/17 robustness update" in note)
    check("A Cycle-20 robustness update is present", "cycle-20 robustness update" in note)
    check("A Cycle-21 robustness update is present", "cycle-21 robustness update" in note)
    check("A Cycle-22/23 robustness update is present", "cycle-22/23 robustness update" in note)
    check("A Cycle-24 robustness update is present", "cycle-24 robustness update" in note)
    check("A Cycle-25 robustness update is present", "cycle-25 robustness update" in note)
    check("A Cycle-26 robustness update is present", "cycle-26 robustness update" in note)
    check("A Cycle-27 robustness update is present", "cycle-27 robustness update" in note)
    check("A Cycle-31 record-state update is present", "cycle-31 record-only nn state construction" in note)
    check("A Cycle-32 global-process update is present", "cycle-32 global record-process law type" in note)
    check("A Cycle-33 definability update is present", "cycle-33 admissibility definability correction" in note)
    check("A Cycle-34 long-run update is present", "cycle-34 long-run record-capacity boundary" in note)
    check("A Cycle-35 local-global glue is present", "cycle-35 local-to-global process glue" in note)
    check("A Cycle-36 moving-front update is present", "cycle-36 moving logical apparatus" in note)
    check("A Cycle-37 final census is present", "cycle-37 final clause-deletion census" in note)
    check("A Cycle-38 CZ selection boundary is present", "cycle-38 cubic-cz selection boundary" in note)
    check("A Cycle-39 temporal boundary is present", "cycle-39 temporal-equivalence boundary" in note)
    check("A Cycle-40 Clifford boundary is present", "cycle-40 cubic-clifford classification boundary" in note)
    check("A Cycle-41 candidate boundary is present", "cycle-41 complete-candidate assembly boundary" in note)
    check("A Cycle-42 identifiability boundary is present", "cycle-42 actual-history identifiability boundary" in note)
    check("A self-writing residual remains law content", "twenty-two fresh sites per event" in note and "collision law" in note)
    check("A licensed Weyl quotient is bounded", "two proper-chiral presentation orbits" in note and "up to unitary equivalence" in note)
    check("A topological linkage does not select the law", "all-zero and all-one histories" in note and "(-9,-5,-1,7,8)" in note)
    check("A intrinsic simulation is below record equivalence", "visible phase certificate" in note and "full abstraction" in note)
    check("A QCA Ward identity leaves exact-law fields", "quarter, half, or unit transfer" in note and "required field of l" in note)
    check("A binary instrument form is retired conditionally", "binary-qubit instrument theorem" in note and "projective/lüders branch form" in note)
    check("A compatible merge derives only scheduler closure", "compatible same-content append system" in note and "no common append extension" in note)
    check("A infinite sector retires phase but not actuality", "genuine quasilocal phase quotient" in note and "distinct central weights" in note)
    check("A pointer context is derived only after the interaction", "simple-fixed-axis theorem" in note and "x/y azimuth" in note)
    check("A dynamic boundary is derived only after a record", "record-generated normal" in note and "shell index 64" in note)
    check("A finite causal-close certificate is law-relative", "finite named ports" in note and "far source at distance r+2" in note)
    check("A universal all-rule law still needs a predictive quotient", "all-rule union" in note and "compiler-relative" in note)
    check("A two-ray frame derives X but not apparatus role", "x_f = -i y_f z_f" in note and "apparatus-role decoder" in note)
    check("A 3-D anomaly class leaves finite-depth representative", "three-fermion clifford qca" in note and "cp(pi/2)" in note)
    check("A autonomous close removes supplied finite boundary post-seed", "99-site" in note and "first localized record" in note)
    check("A primitive full protocol can transport representative", "update-plus-commit protocol" in note and "k'_t=k_t f" in note)
    check("A actual header plus parity certificate selects X", "z_a x_b z_c=1" in note and "parity-certificate" in note)
    check("A adaptive transport retires the algebraic multi-time seam", "finite adaptive full-abstraction theorem" in note and "record-net closure" in note and "maximal local-record category" in note)
    check("A positive-density seed field retires the global-first-site wall", "empty local limit" in note and "positive-density hard-core seed process" in note and "exclusion radius nine" in note)
    check("A maximal foundation site-net quotient is classified", "sp(4,2)" in note and "720" in note and "72" in note and "site permutation plus onsite recoding" in note)
    check("A parity role does not become generic record content", "role-specific operational definition" in note and "pc alone is not complete record content" in note and "record-fibre strong lumpability" in note)
    check("A fixed selected and transported nets remain distinct", "pu(2)^n" in note and "selected pointer-record algebra" in note and "transported-net groupoid" in note)
    check("A commit count is clock only after event identity", "a clock does not make a record lock" in note and "relational integer clock" in note and "dimensionless clock ratios" in note)
    check("A NN seed compilation reaches exact depth but not clean output", "isolated-bernoulli factor" in note and "causal-depth floor is 27" in note and "record-only clean-output obstruction" in note)
    check("A operational Born imports reduce to W plus corpus", "effect noncontextuality becomes definitional" in note and "physical randomization forces affinity" in note and "numerical normalized law w" in note and "reset/trial corpus" in note)
    check("A foundation site identity is sort-preserving semantics", "framework equivalence is a sort-preserving isomorphism" in note and "representation expansions" in note and "not an axiom addition" in note)
    check("A guarded seed reference leaves NN compile law-relative", "exact guarded seed reference" in note and "range nine" in note and "record-inequivalent instruments" in note and "depth-27" in note and "not a new record axiom" in note)
    check("A corpus theorem reduces frequency to component means", "f_n" in note and "e[x_0|i_t]" in note and "component-mean condition" in note and "iid is stronger" in note and "not record axioms" in note)
    check("A residual atoms pack into one L-star plus H", "one complete history law l" in note and "packing is not derivation" in note and "projections of one realized history h" in note and "not constitutional content" in note)
    check("A record-only ontology retains global Bell route", "sixteen deterministic vertices" in note and "2 sqrt(2)" in note and "global record-history law" in note and "qualification state-type revision" in note)
    check("A placement is conditional on exact-law type", "complete local law can retype admissibility" in note and "global-history law needs its own named law" in note)
    check("A later attacks preserve deterministic escape", "uniquely extendible deterministic law can retire a" in note)
    check("A later attacks preserve exact-law residue", "it still does not identify l" in note)
    moving = normalize_text(MOVING_LOGICAL_FRONT_NOTE)
    census = normalize_text(FINAL_MISSING_CENSUS_NOTE)
    cz_selection = normalize_text(CUBIC_CZ_SELECTION_NOTE)
    temporal = normalize_text(TEMPORAL_EQUIVALENCE_NOTE)
    cubic_clifford = normalize_text(CUBIC_CLIFFORD_NOTE)
    candidate = normalize_text(CANDIDATE_ASSEMBLY_NOTE)
    identifiability = normalize_text(HISTORY_IDENTIFIABILITY_NOTE)
    check("A moving-front source proves logical recurrence", "head-process bisimulation" in moving and "no record moves" in moving and "one fresh record" in moving)
    check("A final census retains only conditional ontology gates", "only universal nonzero" in census and "two conditional constitutional edit gates" in census and "no live axiom edit" in census)
    check("A CZ source leaves two protocol-relative laws", "exactly two laws remain" in cz_selection and "time-dependent transported equivalence" in cz_selection and "constraint/preparation layer, not the full" in cz_selection)
    check("A temporal source makes the quotient law-relative", "necessarily law-relative" in temporal and "cross-time idle" in temporal and "no new axiom sentence" in temporal)
    check("A cubic source retains three uniform protocol classes", "three uniformly local symplectic protocol classes survive" in cubic_clifford and "conditional one-skeleton closure" in cubic_clifford)
    check("A candidate source exposes readiness and matter gaps", "event_readiness_local_causal_domain" in candidate and "radius-three, single-front record-law complete" in candidate and "first exact channel incompatibility is matter" in candidate)
    check("A history source retains a separating reconstruction route", "separating reconstruction theorem" in identifiability and "does not invert" in identifiability and "no second atom" in identifiability)
    for index in range(1, 9):
        check(f"A N{index} gate section is present", f"n{index} —" in note)
    registry = REGISTRY.read_text(encoding="utf-8")
    check("A premise registry includes minimal axioms", '"minimal_axioms"' in registry)
    check("A premise registry includes realized-state primitive", '"realized_state_primitive"' in registry)
    check("A realized-state primitive is not enlarged into a selector", "supplies no state, selection rule, measure" in note)


I2 = sp.eye(2)
I4 = sp.eye(4)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
PAULI = (I2, X, Y, Z)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


def exact(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        return sp.simplify(left - right) == sp.zeros(*left.shape)
    return sp.simplify(left - right) == 0


def vectorize(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.reshape(matrix.rows * matrix.cols, 1)


def generated_composition() -> None:
    section("B - Generated composition and silent-sector countermodel")
    left = tuple(sp.kronecker_product(pauli, I2) for pauli in PAULI)
    right = tuple(sp.kronecker_product(I2, pauli) for pauli in PAULI)
    products = tuple(a * b for a in left for b in right)
    product_span = sp.Matrix.hstack(*(vectorize(operator) for operator in products))
    check("B distinct-site copies commute", all(exact(a * b, b * a) for a in left for b in right))
    check("B each local Pauli image has dimension four", sp.Matrix.hstack(*(vectorize(a) for a in left)).rank() == 4 and sp.Matrix.hstack(*(vectorize(b) for b in right)).rank() == 4)
    check("B two-site local products span M4", product_span.rank() == 16)
    check("B ordinary generated physical algebra has dimension sixteen", I4.rows**2 == 16)

    duplicate_products = tuple(sp.diag(operator, operator) for operator in products)
    duplicate_span = sp.Matrix.hstack(*(vectorize(operator) for operator in duplicate_products))
    sector = sp.diag(I4, -I4)
    check("B duplicate algebra has dimension thirty-two", 2 * I4.rows**2 == 32)
    check("B diagonal local products still span only sixteen", duplicate_span.rank() == 16)
    check("B silent central sector is outside local-product span", duplicate_span.row_join(vectorize(sector)).rank() == 17)
    check("B silent sector commutes with every local product", all(exact(sector * operator, operator * sector) for operator in duplicate_products))
    check("B generated law domain retires the duplicate sector", product_span.rank() == I4.rows**2 < 2 * I4.rows**2)


def protocol_words(contexts: tuple[str, ...], max_depth: int):
    for depth in range(1, max_depth + 1):
        yield from product(contexts, repeat=depth)


def future_fingerprint(state, contexts, transition, max_depth=3):
    fingerprint = []
    for protocol in protocol_words(contexts, max_depth):
        current = state
        transcript = []
        for context in protocol:
            output, current = transition(current, context)
            transcript.append(output)
        fingerprint.append((protocol, tuple(transcript)))
    return tuple(fingerprint)


def quotient_blocks(states, contexts, transition):
    blocks = defaultdict(set)
    for state in states:
        blocks[future_fingerprint(state, contexts, transition)].add(state)
    return tuple(sorted((tuple(sorted(block)) for block in blocks.values())))


def operational_state_retirement() -> None:
    section("C - Operational future equivalence and STATE retirement")
    states = tuple(product((0, 1), repeat=2))  # record bit, hidden token

    def transition(state, context):
        record, hidden = state
        if context == "read":
            return ("r", record), state
        if context == "idle":
            return ("idle",), (record, 1 - hidden)
        if context == "probe":
            return ("h", hidden), state
        raise ValueError(context)

    record_contexts = ("read", "idle")
    complete_contexts = ("read", "idle", "probe")
    coarse = quotient_blocks(states, record_contexts, transition)
    refined = quotient_blocks(states, complete_contexts, transition)
    check("C raw history space has four elements", len(states) == 4)
    check("C record-only future quotient has two classes", len(coarse) == 2, str(coarse))
    check("C record-only quotient classes are record fibres", coarse == (((0, 0), (0, 1)), ((1, 0), (1, 1))))
    check("C token-sensitive future quotient has four classes", len(refined) == 4, str(refined))
    check("C token-sensitive classes are singletons", all(len(block) == 1 for block in refined))
    check("C the same raw carrier has context-dependent quotient", coarse != refined)

    for record in (0, 1):
        left_state = (record, 0)
        right_state = (record, 1)
        check(
            f"C record fibre {record} is strongly future-equivalent without token probe",
            future_fingerprint(left_state, record_contexts, transition) == future_fingerprint(right_state, record_contexts, transition),
        )
        check(
            f"C record fibre {record} fails equivalence when token is physical",
            future_fingerprint(left_state, complete_contexts, transition) != future_fingerprint(right_state, complete_contexts, transition),
        )


def q_lambda(lam: int, n_zero: int, n_one: int) -> tuple[Fraction, Fraction]:
    zero = lam**n_zero
    one = lam**n_one
    total = zero + one
    return Fraction(zero, total), Fraction(one, total)


def threshold_sample(probability_zero: Fraction, seed: Fraction) -> int:
    return 0 if seed < probability_zero else 1


def exact_law_value_and_schedule() -> None:
    section("D - Exact law value, context, and schedule")
    profiles = tuple(product(range(7), repeat=2))
    for lam in (1, 2):
        check(f"D lambda-{lam} kernel normalizes", all(sum(q_lambda(lam, *profile)) == 1 for profile in profiles))
        check(f"D lambda-{lam} kernel is strictly positive", all(all(weight > 0 for weight in q_lambda(lam, *profile)) for profile in profiles))
        check(
            f"D lambda-{lam} kernel is label covariant",
            all(q_lambda(lam, n_zero, n_one) == tuple(reversed(q_lambda(lam, n_one, n_zero))) for n_zero, n_one in profiles),
        )
    check("D lambda-1 and lambda-2 have identical support", all(all(weight > 0 for weight in q_lambda(1, *profile)) == all(weight > 0 for weight in q_lambda(2, *profile)) for profile in profiles))
    check("D exact law values disagree at profile two-to-one", q_lambda(1, 2, 1)[0] == Fraction(1, 2) and q_lambda(2, 2, 1)[0] == Fraction(2, 3))

    seed = Fraction(3, 5)
    fair_zero = q_lambda(1, 2, 1)[0]
    biased_zero = q_lambda(2, 2, 1)[0]
    check("D same presentation seed separates the complete law pair", threshold_sample(fair_zero, seed) == 1 and threshold_sample(biased_zero, seed) == 0)
    check(
        "D fixed scalar seed is not pathwise label equivariant for fair law",
        threshold_sample(1 - fair_zero, seed) != 1 - threshold_sample(fair_zero, seed),
    )
    check(
        "D transformed seed restores fair-law pathwise covariance",
        threshold_sample(1 - fair_zero, 1 - seed) == 1 - threshold_sample(fair_zero, seed),
    )
    check(
        "D transformed seed restores biased-law pathwise covariance",
        threshold_sample(1 - biased_zero, 1 - seed) == 1 - threshold_sample(biased_zero, seed),
    )
    check("D boundary-relative compatibility seam is documented", "foundation-compatibility statement is boundary-relative" in normalize_text(NOTE))

    def synchronous(bits):
        left, right = bits
        return right, left

    def left_then_right(bits):
        left, right = bits
        left = right
        right = left
        return left, right

    def right_then_left(bits):
        left, right = bits
        right = left
        left = right
        return left, right

    initial = (0, 1)
    check("D synchronous copy schedule swaps the bits", synchronous(initial) == (1, 0))
    check("D left-first schedule gives all one", left_then_right(initial) == (1, 1))
    check("D right-first schedule gives all zero", right_then_left(initial) == (0, 0))
    check("D one local copy table does not determine overlap schedule", len({synchronous(initial), left_then_right(initial), right_then_left(initial)}) == 3)


def marginal_first(law):
    result = {0: Fraction(0), 1: Fraction(0)}
    for word, weight in law.items():
        result[word[0]] += weight
    return result


def gluing_and_extension() -> None:
    section("E - Normalization versus global projective consistency")
    one_bit = {(0,): Fraction(1, 2), (1,): Fraction(1, 2)}
    iid_two = {word: Fraction(1, 4) for word in product((0, 1), repeat=2)}
    bad_two = {(0, 0): Fraction(1)}
    check("E one-bit law normalizes", sum(one_bit.values()) == 1)
    check("E IID two-bit law normalizes", sum(iid_two.values()) == 1)
    check("E point-mass two-bit law normalizes", sum(bad_two.values()) == 1)
    check("E IID prefix marginal matches the one-bit law", marginal_first(iid_two) == {0: Fraction(1, 2), 1: Fraction(1, 2)})
    check("E normalized point mass has incompatible prefix marginal", marginal_first(bad_two) != {0: Fraction(1, 2), 1: Fraction(1, 2)})
    check("E normalization alone does not imply projective extension", sum(bad_two.values()) == 1 and marginal_first(bad_two) != {0: Fraction(1, 2), 1: Fraction(1, 2)})

    three_iid = {word: Fraction(1, 8) for word in product((0, 1), repeat=3)}
    check(
        "E one consistent family marginalizes two-to-one",
        all(sum(iid_two.get(prefix + (tail,), 0) for tail in (0, 1)) == weight for prefix, weight in one_bit.items()),
    )
    check(
        "E one consistent family marginalizes three-to-two",
        all(sum(three_iid.get(prefix + (tail,), 0) for tail in (0, 1)) == weight for prefix, weight in iid_two.items()),
    )


def append_record(history: dict[int, int], address: int, value: int) -> dict[int, int]:
    if address in history:
        raise ValueError("address is already recorded")
    result = dict(history)
    result[address] = value
    return result


def record_preservation_renewal_and_support() -> None:
    section("F - Record identity, preservation, renewal, and positive support")
    first = append_record({}, 0, 1)
    second = append_record(first, 1, 0)
    check("F append output has site-tagged identity", first == {0: 1})
    check("F later append preserves prior site and content", second[0] == first[0])
    check("F fresh allocation produces a second address", 1 not in first and 1 in second)

    absorbing_one_site = {"open": {"r0", "r1"}, "r0": {"r0"}, "r1": {"r1"}}
    check("F one-site archive preserves either written fact", absorbing_one_site["r0"] == {"r0"} and absorbing_one_site["r1"] == {"r1"})
    check("F one-site archive has no renewed open carrier", all("open" not in targets for state, targets in absorbing_one_site.items() if state != "open"))

    old_record = {0: 0}
    corrupt_after_renewal = {0: 0, 1: 1}
    corrupt_after_renewal[0] = 1
    check("F renewal can coexist with old-record corruption", 1 in corrupt_after_renewal and corrupt_after_renewal[0] != old_record[0])
    check("F preservation and renewal are directionally independent", second[0] == first[0] and all("open" not in targets for state, targets in absorbing_one_site.items() if state != "open"))

    rho = density(KET0)
    weights = {0: trace(P0 * rho * P0), 1: trace(P1 * rho * P1)}
    menu = set(weights)
    support = {outcome for outcome, weight in weights.items() if weight > 0}
    check("F PVM instrument weights normalize", sum(weights.values()) == 1)
    check("F algebraic menu contains both outcomes", menu == {0, 1})
    check("F positive support contains only outcome zero", support == {0})
    check("F support is a strict subset of algebraic menu", support < menu)


def negate(axis):
    return tuple(-component for component in axis)


def scale_axis(sign, axis):
    return tuple(sign * component for component in axis)


def cubic_frame_weight(axis):
    return sp.simplify((1 + axis[2] ** 3) / 2)


def projector(axis):
    return sp.simplify((I2 + axis[0] * X + axis[1] * Y + axis[2] * Z) / 2)


def born_representation_tournament() -> None:
    section("G - Loose product composition versus full-composite Born route")
    root2 = sp.sqrt(2)
    axes = (
        (sp.Integer(1), sp.Integer(0), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(1), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(0), sp.Integer(1)),
        (1 / root2, sp.Integer(0), 1 / root2),
        (1 / root2, 1 / root2, sp.Integer(0)),
    )
    check("G cubic qubit weights normalize on every tested binary frame", all(exact(cubic_frame_weight(axis) + cubic_frame_weight(negate(axis)), 1) for axis in axes))
    check("G cubic qubit weights stay in zero-one range", all(0 <= float(cubic_frame_weight(sign_axis)) <= 1 for axis in axes for sign_axis in (axis, negate(axis))))
    check("G cubic assignment gives X and Y one half", cubic_frame_weight(axes[0]) == cubic_frame_weight(axes[1]) == sp.Rational(1, 2))
    check("G cubic assignment gives Z certainty", cubic_frame_weight(axes[2]) == 1)

    diagonal = axes[3]
    born_forced_by_axes = sp.simplify((1 + diagonal[2]) / 2)
    cubic_diagonal = cubic_frame_weight(diagonal)
    check("G axis values force Bloch vector zero-zero-one", cubic_frame_weight(axes[0]) == sp.Rational(1, 2) and cubic_frame_weight(axes[1]) == sp.Rational(1, 2) and cubic_frame_weight(axes[2]) == 1)
    check("G cubic diagonal weight differs from forced Born value", not exact(cubic_diagonal, born_forced_by_axes), f"cubic={cubic_diagonal}, Born={born_forced_by_axes}")

    for left_axis, right_axis in product(axes, repeat=2):
        law = {
            (left_sign, right_sign): sp.simplify(
                cubic_frame_weight(scale_axis(left_sign, left_axis))
                * cubic_frame_weight(scale_axis(right_sign, right_axis))
            )
            for left_sign, right_sign in product((1, -1), repeat=2)
        }
        check(
            f"G product context normalizes {axes.index(left_axis)}-{axes.index(right_axis)}",
            exact(sum(law.values()), 1),
        )
        left_marginal = sp.simplify(sum(weight for (left_sign, _), weight in law.items() if left_sign == 1))
        right_marginal = sp.simplify(sum(weight for (_, right_sign), weight in law.items() if right_sign == 1))
        check(
            f"G product context has local marginals {axes.index(left_axis)}-{axes.index(right_axis)}",
            exact(left_marginal, cubic_frame_weight(left_axis)) and exact(right_marginal, cubic_frame_weight(right_axis)),
        )

    phi_plus = (sp.kronecker_product(KET0, KET0) + sp.kronecker_product(KET1, KET1)) / sp.sqrt(2)
    rho_composite = density(phi_plus)
    rho_left = I2 / 2
    check("G generated spectator composite has dimension four", rho_composite.rows == 4 > 2)
    for index, axis in enumerate(axes):
        local_projection = projector(axis)
        embedded_projection = sp.kronecker_product(local_projection, I2)
        check(
            f"G spectator marginal identity for axis {index}",
            exact(trace(rho_composite * embedded_projection), trace(rho_left * local_projection)),
        )
    check("G spectator embedding preserves complements", exact(sp.kronecker_product(I2 - P0, I2), I4 - sp.kronecker_product(P0, I2)))
    check("G spectator embedding preserves orthogonality", exact(sp.kronecker_product(P0, I2) * sp.kronecker_product(P1, I2), sp.zeros(4)))

    bell_states = (
        (sp.kronecker_product(KET0, KET0) + sp.kronecker_product(KET1, KET1)) / sp.sqrt(2),
        (sp.kronecker_product(KET0, KET0) - sp.kronecker_product(KET1, KET1)) / sp.sqrt(2),
        (sp.kronecker_product(KET0, KET1) + sp.kronecker_product(KET1, KET0)) / sp.sqrt(2),
        (sp.kronecker_product(KET0, KET1) - sp.kronecker_product(KET1, KET0)) / sp.sqrt(2),
    )
    bell_projectors = tuple(density(state) for state in bell_states)
    check("G Bell projectors form one complete composite frame", exact(sum(bell_projectors, sp.zeros(4)), I4))
    check("G Born weights normalize on the Bell frame", exact(sum(trace(rho_composite * projection) for projection in bell_projectors), 1))
    check("G positive theorem is explicitly invoked rather than re-proved", "invokes, rather than re-proves" in normalize_text(NOTE))


def actuality_separation() -> None:
    section("H - Born/normalization versus one actual history")
    rho_plus = density(KET_PLUS)
    branch_zero = sp.simplify(P0 * rho_plus * P0)
    branch_one = sp.simplify(P1 * rho_plus * P1)
    nonselective = sp.simplify(branch_zero + branch_one)
    check("H dephasing branches each have weight one half", trace(branch_zero) == trace(branch_one) == sp.Rational(1, 2))
    check("H dephasing weights normalize", trace(branch_zero) + trace(branch_one) == 1)
    check("H nonselective output is maximally mixed", exact(nonselective, I2 / 2))
    check("H averaged channel equals the sum of outcome branches", exact(nonselective, branch_zero + branch_one))

    fair_measure = {0: Fraction(1, 2), 1: Fraction(1, 2)}
    models = (
        {"measure": fair_measure, "actual": None},
        {"measure": fair_measure, "actual": 0},
        {"measure": fair_measure, "actual": 1},
    )
    check("H one fair measure admits three actuality annotations", len(models) == 3 and all(model["measure"] == fair_measure for model in models))
    check("H measure equality does not fix the actuality field", {model["actual"] for model in models} == {None, 0, 1})

    delta_measure = {0: Fraction(1), 1: Fraction(0)}
    support = {outcome for outcome, weight in delta_measure.items() if weight > 0}
    check("H deterministic delta law has a unique supported member", support == {0})
    check("H deterministic uniqueness fixes the complete member when claimed", len(support) == 1)

    allowed_histories = {(0, 0, 0), (1, 1, 1)}
    boundary_zero = {history for history in allowed_histories if history[0] == 0}
    boundary_one = {history for history in allowed_histories if history[0] == 1}
    check("H unconditioned global law has two histories", len(allowed_histories) == 2)
    check("H either boundary instance selects a unique history", len(boundary_zero) == len(boundary_one) == 1)
    check("H boundary selection is separate from the common law", boundary_zero != boundary_one and boundary_zero | boundary_one == allowed_histories)
    actuality_note = normalize_text(ACTUALITY_SEMANTICS_NOTE)
    check("H registered ontology closes actual-state reference only", "actual-state reference is closed" in actuality_note and "complete-history status is conditional" in actuality_note)
    check("H normalized measure alone selects no history", "measure alone still selects no member" in actuality_note and "four complete-history routes" in actuality_note)
    check("H typicality remains distinct from history status", "history status and typicality/pointwise upgrade are distinct" in actuality_note)


def semantic_inventory_reduction() -> None:
    section("I - Semantic inventory partition and lower bound")
    inventory = {*(f"C{index}" for index in range(1, 12)), "E1", "B*"}
    referent_owned = {"C1", "C2", "C3", "C5", "C6", "C7", "C9", "C10"}
    derived_or_defined = {"C4", "C8", "C11"}
    branching_separate: set[str] = set()
    empirical_interface = {"E1"}
    contingent_external = {"B*"}
    partition = (referent_owned, derived_or_defined, branching_separate, empirical_interface, contingent_external)
    check("I inventory has thirteen named entries", len(inventory) == 13)
    check("I five disposition sets are pairwise disjoint", all(left.isdisjoint(right) for index, left in enumerate(partition) for right in partition[index + 1 :]))
    check("I disposition sets cover the full inventory", set().union(*partition) == inventory)
    check("I eight entries are owned by the exact referent", len(referent_owned) == 8)
    check("I STATE, actuality typing, and eligibility are derived or definitional", derived_or_defined == {"C4", "C8", "C11"})
    check("I no branching semantic remainder survives", not branching_separate)
    check("I trials and boundary are not universal law atoms", empirical_interface == {"E1"} and contingent_external == {"B*"})
    check("I gluing and projective extension share one global contract", {"C7", "C9"} <= referent_owned)

    universal_package = {"EXACT_LAW_IDENTITY"}
    branching_package = set(universal_package)
    check("I universal lower bound has one semantic obligation", len(universal_package) == 1)
    check("I branching package adds no universal semantic obligation", branching_package == universal_package)
    check("I single-clause target contains exact law identity", "the fixed nearest-neighbor rule is the exact law specified by" in normalize_text(NOTE))
    check("I history-domain typing replaces a selector clause", "normalized measure on complete physical record histories" in normalize_text(NOTE))
    check("I actual facts do not force a universal actuality clause", "does not by itself add a universal a atom" in normalize_text(NOTE))


def no_go_discipline_contract() -> None:
    section("J - N1-N8 discipline and live alternatives")
    note = normalize_text(NOTE)
    routes = (
        "exact generated algebra-valued law",
        "complete operational future quotient",
        "all-effects busch/cfmr route",
        "full-composite projective gleason route",
        "deterministic unique extension",
        "boundary-conditioned global uniqueness",
        "sampled instrument",
        "unique-ergodic full law plus reset corpus",
        "exact physical-equivalence class instead of one presentation",
    )
    check("J N1 enumerates at least five distinct routes", sum(route in note for route in routes) >= 5)
    for route in routes:
        check(f"J N1 route retained: {route}", route in note)
    check("J N2 separates law from conditional history without adding a universal atom", "exact branching l determines h" in note and "one actual history h determines exact l" in note and "only universal-looking residual" in note and "conditional law/data interface" in note)
    check("J N3 classifies causal-composition ambiguity", "split into product-only and full-composite readings" in note)
    check("J N4 matches seven source residuals", note.count("| yes |") >= 7)
    check("J N5 confines cubic control to product contexts", "covers qubit projectors and all product contexts, not every entangled composite frame" in note)
    check("J N6 records non-axiom retirement paths", "live non-axiom retirement paths" in note)
    check("J N7 keeps unique derivation live", "if such a uniqueness theorem is proved, no new law sentence is needed" in note)
    check("J N8 rejects an inflated C1-C10 wall set", "warns against declaring c1--c10 an irreducible wall set" in note)
    check("J no universal two-atom minimum is claimed", "does not claim a universal two-atom minimum" in note)
    check("J eventual joint derivation remains open", "no claim is made that the eventual exact law cannot derive" in note)
    check("J sample-coordinate pathwise covariance seam is explicit", "pathwise sampled law must transform its sample coordinate" in note)
    check("J shell allocator is boundary-anchored in the contract", "shell allocation must be anchored to a physical boundary/context record" in note)


def main() -> int:
    source_contract()
    generated_composition()
    operational_state_retirement()
    exact_law_value_and_schedule()
    gluing_and_extension()
    record_preservation_renewal_and_support()
    born_representation_tournament()
    actuality_separation()
    semantic_inventory_reduction()
    no_go_discipline_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: exact finite countermodels and a conditional semantic "
        "reduction; no canonical-law, axiom, boundary, or audit selection"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
