#!/usr/bin/env python3
"""Local synthesis gate for the minimum-axiom-update exercise.

The gate checks the live constitutional boundary, exact finite separations,
the synthesis contract, and its companion runners.  It does not select a law,
edit an axiom, write an audit verdict, or promote any research note.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MINIMUM_AXIOM_UPDATE_EXERCISE_SYNTHESIS_AND_CUT_GATE_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
AXIOM_RUNNER = ROOT / "scripts" / "audit_companion_minimal_axioms_clean_base_exact.py"

EVIDENCE = {
    "contract": REVIEW / "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md",
    "predictive": REVIEW / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md",
    "irreducible": REVIEW / "EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md",
    "sampled_pair": REVIEW / "COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md",
    "actualization": REVIEW / "BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md",
    "deterministic": REVIEW / "CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md",
    "deterministic_sectors": REVIEW / "DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md",
    "wolfram": REVIEW / "CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md",
    "language": REVIEW / "QUALITATIVE_SUBSTRATE_EXACT_LAW_SELECTION_NOTE_2026-07-14.md",
    "bell": REVIEW / "CFSI_Q_BELL_COHERENT_CAUSAL_FRONT_LAW_NOTE_2026-07-14.md",
    "nucleation": REVIEW / "AUTONOMOUS_HOMOGENEOUS_BINARY_NUCLEATION_NOTE_2026-07-14.md",
    "resource": REVIEW / "LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md",
    "reversible": REVIEW / "REVERSIBLE_DILATION_CLOSED_CYCLE_GRAVITY_CYCLE10_NOTE_2026-07-14.md",
    "cubic": REVIEW / "CUBIC_COVARIANCE_EXACT_REPAIR_TOURNAMENT_NOTE_2026-07-14.md",
    "matter": REVIEW / "MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md",
    "infinite_qca": REVIEW / "INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
    "existence": REVIEW / "EXISTENCE_UNIQUENESS_AND_EXACT_LAW_REFERENCE_NOTE_2026-07-14.md",
    "selection": REVIEW / "FIRST_PRINCIPLES_LAW_SELECTION_TOURNAMENT_NOTE_2026-07-14.md",
    "impact_map": REVIEW / "ONE_CUT_FOUNDATION_SURFACE_IMPACT_MAP_NOTE_2026-07-14.md",
    "fundamental_qca": REVIEW / "FUNDAMENTAL_ONE_QUBIT_QCA_COMPILATION_CYCLE12_NOTE_2026-07-14.md",
    "literature_selection": REVIEW / "EXACT_LAW_UNIQUENESS_SELECTION_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md",
    "relational_selector": REVIEW / "RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md",
    "placement": REVIEW / "EXACT_LAW_CONSTITUTIONAL_PLACEMENT_SCHEMA_PROBE_NOTE_2026-07-14.md",
    "append_wire": REVIEW / "APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md",
    "weyl_equivalence": REVIEW / "WEYL_PAIR_PHYSICAL_EQUIVALENCE_AND_COMBINED_INTERSECTION_NOTE_2026-07-14.md",
    "single_action": REVIEW / "SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md",
    "self_writing": REVIEW / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md",
    "licensed_equivalence": REVIEW / "FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md",
    "topological_action": REVIEW / "TOPOLOGICAL_CONSERVATION_RG_ACTION_STEELMAN_NOTE_2026-07-14.md",
    "simulation_equivalence": REVIEW / "INTRINSIC_SIMULATION_OBSERVER_EQUIVALENCE_RECORD_COST_NOTE_2026-07-14.md",
    "qca_ward": REVIEW / "PROPER_CUBIC_QUBIT_QCA_WARD_IDENTITY_STEELMAN_NOTE_2026-07-14.md",
    "instrument_selection": REVIEW / "RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md",
    "abelian_merge": REVIEW / "ABELIAN_COMPATIBLE_SEED_BELL_MERGE_CYCLE15_NOTE_2026-07-14.md",
    "infinite_sector": REVIEW / "INFINITE_REDUNDANCY_QUASILOCAL_RECORD_SECTOR_NOTE_2026-07-14.md",
    "relational_pointer": REVIEW / "RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md",
    "dynamic_boundary_index": REVIEW / "DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md",
    "delayed_lock": REVIEW / "DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md",
    "universal_rule_space": REVIEW / "UNIVERSAL_RULE_SPACE_MULTIWAY_LAW_STEELMAN_NOTE_2026-07-14.md",
    "chiral_triad_context": REVIEW / "CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md",
    "three_d_anomaly": REVIEW / "THREE_DIMENSIONAL_ANOMALOUS_BULK_CATEGORY_INDEX_STEELMAN_NOTE_2026-07-14.md",
    "autonomous_close": REVIEW / "AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md",
    "primitive_protocol_equivalence": REVIEW / "PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md",
    "actual_header_decoder": REVIEW / "ACTUAL_HEADER_ROLE_DECODER_PARITY_SELECTION_CYCLE18_NOTE_2026-07-14.md",
    "adaptive_full_abstraction": REVIEW / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md",
    "invariant_seed_field": REVIEW / "INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md",
    "site_net_equivalence": REVIEW / "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md",
    "named_site_equivalence": REVIEW / "NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md",
    "foundation_sort_equivalence": REVIEW / "FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md",
    "operational_parity": REVIEW / "COMPLETE_FUTURE_OPERATIONAL_PARITY_CERTIFICATE_CYCLE19_NOTE_2026-07-14.md",
    "commit_clock": REVIEW / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md",
    "seed_compilation": REVIEW / "NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md",
    "born_affinity": REVIEW / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "dissipative_seed_escape": REVIEW / "QUANTUM_DISSIPATIVE_SEED_ESCAPE_CYCLE20_NOTE_2026-07-14.md",
    "frequency_corpus": REVIEW / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md",
    "residual_packing": REVIEW / "BLIND_RESIDUAL_ATOM_PACKING_AND_ONE_LAW_CONSTITUTIONAL_SCHEMA_NOTE_2026-07-14.md",
    "record_state_bell_type": REVIEW / "RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md",
    "actuality_semantics": REVIEW / "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md",
    "record_state_fortress": REVIEW / "RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md",
    "global_record_process": REVIEW / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md",
    "admissibility_definability": REVIEW / "ADMISSIBILITY_SYMBOL_DEFINABILITY_AND_EXACT_LAW_REFERENCE_CHALLENGE_NOTE_2026-07-14.md",
    "constitutional_lower_bound": REVIEW / "CONSTITUTIONAL_LOWER_BOUND_CLOSURE_AND_CLAUSE_DELETION_CYCLE31_NOTE_2026-07-14.md",
    "long_run_append": REVIEW / "LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md",
    "local_global_glue": REVIEW / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md",
    "moving_logical_front": REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md",
    "final_missing_census": REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md",
    "cubic_cz_selection": REVIEW / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md",
    "temporal_equivalence": REVIEW / "TEMPORAL_PROTOCOL_EQUIVALENCE_ALTERNATING_FRAME_CYCLE39_NOTE_2026-07-14.md",
    "cubic_clifford": REVIEW / "CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md",
    "candidate_assembly": REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md",
    "history_identifiability": REVIEW / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md",
    "exhaustion_ledger": REVIEW / "MINIMUM_CONSTITUTIONAL_CONTENT_EXHAUSTION_LEDGER_NOTE_2026-07-14.md",
}

COMPANIONS = (
    ROOT / "scripts" / "exact_predictive_specification_tournament_2026_07_14.py",
    ROOT / "scripts" / "exact_law_irreducible_content_independence_tournament_2026_07_14.py",
    ROOT / "scripts" / "qualitative_substrate_exact_law_selection_probe_2026_07_14.py",
    ROOT / "scripts" / "bare_metal_record_actualization_primary_source_audit_2026_07_14.py",
    ROOT / "scripts" / "causal_reversible_actuality_weight_irreducibility_red_team_2026_07_14.py",
    ROOT / "scripts" / "deterministic_unique_extension_record_sector_probe_2026_07_14.py",
    ROOT / "scripts" / "causal_schedule_equivalence_wolfram_inspiration_probe_2026_07_14.py",
    ROOT / "scripts" / "cfsi_q_bell_coherent_causal_front_law_probe_2026_07_14.py",
    ROOT / "scripts" / "autonomous_homogeneous_binary_nucleation_probe_2026_07_14.py",
    ROOT / "scripts" / "local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    ROOT / "scripts" / "reversible_dilation_closed_cycle_gravity_cycle10_2026_07_14.py",
    ROOT / "scripts" / "matter_counting_chirality_exact_law_placement_probe_2026_07_14.py",
    ROOT / "scripts" / "infinite_reversible_record_export_qca_cycle11_2026_07_14.py",
    ROOT / "scripts" / "existence_uniqueness_exact_law_reference_probe_2026_07_14.py",
    ROOT / "scripts" / "first_principles_law_selection_tournament_probe_2026_07_14.py",
    ROOT / "scripts" / "one_cut_foundation_surface_impact_map_2026_07_14.py",
    ROOT / "scripts" / "fundamental_one_qubit_qca_compilation_cycle12_2026_07_14.py",
    ROOT / "scripts" / "exact_law_uniqueness_selection_primary_source_audit_2026_07_14.py",
    ROOT / "scripts" / "relational_qubit_disagreement_canonical_law_escalation_probe_2026_07_14.py",
    ROOT / "scripts" / "exact_law_constitutional_placement_schema_probe_2026_07_14.py",
    ROOT / "scripts" / "wolfram_multiway_record_sector_probe_2026_07_14.py",
    ROOT / "scripts" / "append_only_causal_bell_wire_cycle13_2026_07_14.py",
    ROOT / "scripts" / "weyl_pair_physical_equivalence_combined_intersection_probe_2026_07_14.py",
    ROOT / "scripts" / "single_invariant_action_steelman_attack_probe_2026_07_14.py",
    ROOT / "scripts" / "self_writing_append_only_bell_front_cycle14_2026_07_14.py",
    ROOT / "scripts" / "foundation_licensed_physical_equivalence_weyl_pair_probe_2026_07_14.py",
    ROOT / "scripts" / "topological_conservation_rg_action_steelman_probe_2026_07_14.py",
    ROOT / "scripts" / "intrinsic_simulation_observer_equivalence_record_cost_probe_2026_07_14.py",
    ROOT / "scripts" / "proper_cubic_qubit_qca_ward_identity_steelman_probe_2026_07_14.py",
    ROOT / "scripts" / "record_instrument_selection_luders_primary_source_probe_2026_07_14.py",
    ROOT / "scripts" / "abelian_compatible_seed_bell_merge_cycle15_2026_07_14.py",
    ROOT / "scripts" / "infinite_redundancy_quasilocal_record_sector_probe_2026_07_14.py",
    ROOT / "scripts" / "relational_pointer_context_selection_cycle16_2026_07_14.py",
    ROOT / "scripts" / "dynamic_record_boundary_index_qca_steelman_probe_2026_07_14.py",
    ROOT / "scripts" / "delayed_locking_causal_close_cycle16_2026_07_14.py",
    ROOT / "scripts" / "universal_rule_space_multiway_law_steelman_probe_2026_07_14.py",
    ROOT / "scripts" / "chiral_triad_transverse_context_cycle17_2026_07_14.py",
    ROOT / "scripts" / "three_dimensional_anomalous_bulk_category_index_steelman_probe_2026_07_14.py",
    ROOT / "scripts" / "autonomous_self_closing_diamond_cycle17_2026_07_14.py",
    ROOT / "scripts" / "primitive_qca_record_protocol_full_equivalence_steelman_probe_2026_07_14.py",
    ROOT / "scripts" / "actual_header_role_decoder_parity_selection_cycle18_2026_07_14.py",
    ROOT / "scripts" / "adaptive_record_protocol_qca_full_abstraction_probe_2026_07_14.py",
    ROOT / "scripts" / "invariant_first_seed_hard_core_cycle18_2026_07_14.py",
    ROOT / "scripts" / "foundation_site_net_record_equivalence_classification_cycle21_2026_07_14.py",
    ROOT / "scripts" / "named_site_record_faithful_equivalence_classification_probe_2026_07_14.py",
    ROOT / "scripts" / "foundation_sort_preserving_equivalence_dynamical_gauge_collapse_probe_2026_07_14.py",
    ROOT / "scripts" / "complete_future_operational_parity_certificate_cycle19_2026_07_14.py",
    ROOT / "scripts" / "clock_as_commit_count_and_rate_classification_cycle22_2026_07_14.py",
    ROOT / "scripts" / "nearest_neighbor_seed_compilation_cycle19_2026_07_14.py",
    ROOT / "scripts" / "operational_quotient_born_affinity_cycle20_2026_07_14.py",
    ROOT / "scripts" / "quantum_dissipative_seed_escape_cycle20_2026_07_14.py",
    ROOT / "scripts" / "certified_record_corpus_ergodic_frequency_cycle21_2026_07_14.py",
    ROOT / "scripts" / "blind_residual_atom_packing_one_law_schema_probe_2026_07_14.py",
    ROOT / "scripts" / "record_only_state_bell_law_type_dichotomy_cycle29_2026_07_14.py",
    ROOT / "scripts" / "stochastic_record_history_actuality_semantics_cycle27_2026_07_14.py",
    ROOT / "scripts" / "record_state_one_m2_nn_fortress_cycle26_2026_07_14.py",
    ROOT / "scripts" / "global_record_history_process_law_cycle30_2026_07_14.py",
    ROOT / "scripts" / "admissibility_symbol_definability_exact_law_reference_probe_2026_07_14.py",
    ROOT / "scripts" / "constitutional_lower_bound_clause_deletion_cycle31_2026_07_14.py",
    ROOT / "scripts" / "long_run_record_only_append_architecture_cycle32_2026_07_14.py",
    ROOT / "scripts" / "local_to_global_cubic_process_glue_cycle33_2026_07_14.py",
    ROOT / "scripts" / "moving_logical_apparatus_append_front_cycle34_2026_07_14.py",
    ROOT / "scripts" / "final_missing_content_census_constitutional_edit_gate_cycle35_2026_07_14.py",
    ROOT / "scripts" / "cubic_cz_edge_rule_uniqueness_selection_cycle36_2026_07_14.py",
    ROOT / "scripts" / "temporal_protocol_equivalence_alternating_frame_cycle39_2026_07_14.py",
    ROOT / "scripts" / "cubic_one_qubit_clifford_qca_uniqueness_cycle40_2026_07_14.py",
    ROOT / "scripts" / "complete_candidate_lstar_assembly_cycle41_2026_07_14.py",
    ROOT / "scripts" / "realized_history_exact_law_identifiability_cycle42_2026_07_14.py",
    ROOT / "scripts" / "minimum_constitutional_content_exhaustion_ledger_2026_07_14.py",
)

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


def source_and_authority_contract() -> None:
    section("A - Source, authority, and current-foundation boundary")
    for label, path in {
        "synthesis": NOTE,
        "axioms": AXIOMS,
        "registry": REGISTRY,
        "policy": POLICY,
        "axiom runner": AXIOM_RUNNER,
        **EVIDENCE,
    }.items():
        check(f"A source exists: {label}", path.is_file(), str(path.relative_to(ROOT)))

    note = normalized(NOTE)
    contract = normalized(EVIDENCE["contract"])
    exhaustion = normalized(EVIDENCE["exhaustion_ledger"])
    check("A synthesis is authority-free", "authority: none" in note)
    check("A synthesis disclaims an axiom amendment", "does not amend an axiom" in note)
    check("A synthesis disclaims a law selection", "does not" in note and "identify the universe's law" in note)
    check("A synthesis carries N1-N8", all(f"n{index} —" in note for index in range(1, 9)))
    check("A synthesis marks the referent missing", "the exact referent does not yet exist" in note)
    check("A synthesis forbids a placeholder cut", "forbid a placeholder cut" in note)
    check("A synthesis includes the completed primary-source audit", "completed primary-source uniqueness" in note)
    check("A synthesis retains the two-Weyl positive route", "two weyl walks" in note and "transcript-equivalent" in note)
    check("A synthesis includes the relational quantum selector", "five equivalent disagreement measures" in note and "quarter-exchange" in note)
    check("A synthesis includes the programmed append theorem", "programmed append" in note and "permanent local extension" in note)
    check("A synthesis includes the Weyl equivalence boundary", "staggered lattice character" in note and "1/4" in note and "same-labeled" in note)
    check("A synthesis includes the one-action wrapper boundary", "feynman--kitaev" in note and "update matrix is inside the action" in note)
    check("A synthesis includes autonomous self-writing", "twenty-two fresh record sites" in note and "no hidden cursor" in note)
    check("A synthesis includes the licensed Weyl quotient", "two proper-chiral presentation orbits" in note and "chi^2" in note)
    check("A synthesis includes the topological-action compression", "(-9,-5,-1,7,8)" in note and "all-zero and an all-one" in note)
    check("A synthesis includes the intrinsic-simulation boundary", "intrinsic simulation is weaker than physical equivalence" in note and "full-abstraction theorem" in note)
    check("A synthesis includes the exact QCA Ward boundary", "rank sectors 1+2+3" in note and "128 completions and 64" in note)
    check("A synthesis includes binary-qubit Lüders reduction", "binary qubit repeatability derives lüders form" in note and "form-after-context" in note)
    check("A synthesis includes abelian compatible merging", "grow-only join-semilattice" in note and "no common extension" in note)
    check("A synthesis includes infinite-sector phase retirement", "infinite-sector escape" in note and "every cat phase" in note)
    check("A synthesis includes context-after-dynamics", "context-after-dynamics theorem" in note and "bell capability selects only the equatorial class" in note)
    check("A synthesis includes the generated-boundary index result", "shell wire-flow index 64" in note and "finite-depth local gates lie in its kernel" in note)
    check("A synthesis includes delayed locking after finite causal closure", "far source at distance r+2" in note and "locking after local causal closure" in note)
    check("A synthesis includes the universal-rule-space steelman", "all-rules" in note and "de bruijn" in note and "compiler-relative" in note)
    check("A synthesis includes the chiral-triad context reduction", "two-ray frame theorem" in note and "apparatus role" in note)
    check("A synthesis includes the genuine 3-D anomaly attack", "three-fermion clifford qca" in note and "finite-depth local gates" in note)
    check("A synthesis includes autonomous post-seed closure", "99-site" in note and "no supplied stop" in note)
    check("A synthesis includes primitive full-protocol equivalence", "update-plus-commit protocol" in note and "full-transport identity" in note)
    check("A synthesis includes the actual-header parity selector", "actual header" in note and "parity-certificate selection" in note)
    check("A synthesis includes adaptive full abstraction", "finite adaptive full-abstraction theorem" in note and "history-dependent frame" in note and "record-net closure" in note)
    check("A synthesis includes invariant positive-density nucleation", "local limit is empty" in note and "positive-density hard-core seed field" in note and "exclusion radius nine" in note)
    check("A synthesis includes the maximal site-net classification", "sp(4,2)" in note and "site permutation plus onsite recoding" in note and "selected pointer-record algebra" in note)
    check("A synthesis includes fixed/selected/transported net split", "pu(2)^n" in note and "selected pointer-record algebra" in note and "transported-net groupoid" in note)
    check("A synthesis resolves foundation site identity semantically", "framework equivalence is a sort-preserving isomorphism" in note and "representation expansions" in note and "needs no lattice or qubit axiom addition" in note)
    check("A synthesis includes complete-future parity audit", "role-specific operational definition" in note and "coherent bell branch" in note and "dephased parity mixture" in note and "record-fibre" in note)
    check("A synthesis includes the commit-clock theorem", "a clock does not make a record lock" in note and "commit count" in note and "dimensionless clock ratios" in note)
    check("A synthesis includes the partial NN seed compile", "isolated-bernoulli factor" in note and "causal-depth floor is 27" in note and "record-only clean-output obstruction" in note)
    check("A synthesis includes the operational Born reduction", "effect noncontextuality becomes definitional" in note and "physical randomization forces affinity" in note and "prepared-state identity" in note)
    check("A synthesis includes the guarded dissipative seed reference", "guarded range-nine" in note and "depth at least 14" in note and "depth-27" in note and "record-inequivalent kraus instruments" in note)
    check("A synthesis includes the weakest frequency bridge", "component-mean condition" in note and "e[x_0 | i_t]" in note and "stationarity plus finite causal locality is insufficient" in note)
    check("A synthesis includes moving logical recurrence", "one-seed nearest-neighbor append front" in note and "causal-lineage bisimulation" in note and "every physical record remains fixed" in note)
    check("A synthesis includes the bounded final missing-content census", "no second universal-looking constitutional atom survived the tested routes" in note and "conditional edit only" in note and "typicality remains claim-specific" in note)
    check("A synthesis includes the cubic CZ selection boundary", "u_0=product cz" in note and "u_1=z_all u_0" in note and "physical temporal record/instrument equivalence category" in note)
    check("A synthesis classifies temporal equivalence as law-relative", "alternating frame is exactly law-relative" in note and "cross-time idle" in note and "transcript preserving" in note)
    check("A synthesis includes the broad cubic Clifford census", "onsite rotation action" in note and "three uniformly local symplectic protocol classes" in note and "single nontrivial skeleton class" in note)
    check("A synthesis includes the complete candidate first failure", "l41^r3" in note and "event_readiness_local_causal_domain" in note and "destroys matter-channel distinguishability" in note)
    check("A synthesis preserves the history reconstruction firewall", "actual h does not select off-path" in note and "separating all-protocol reconstruction theorem" in note)
    check("A synthesis packs universal fields once without hiding them", "one complete history law l" in note and "packing does not derive these fields" in note and "one stable exact object" in note)
    check("A synthesis gives conditional complete-history routes", "projections of one explicitly typed realized history h" in note and "law-owned one-outcome dynamics" in note and "reconstructed from records" in note and "unique-history law collapses" in note)
    check("A synthesis exposes the record-state Bell type gate", "convex mixture of 16 deterministic vertices" in note and "global/contextual history weights" in note and "physically real unrecorded quantum carrier" in note)
    check("A exhaustion ledger classifies the bounded thirteen-interface inventory", "corrected thirteen-interface record-law inventory" in exhaustion and "one universal-looking constitutional obligation" in exhaustion)
    check("A exhaustion ledger preserves the no-cut gate", "minimum live edit justified now: none" in exhaustion and "stable exact law referent" in exhaustion)
    check("A referent contract requires a stable identity", "stable canonical claim identifier" in contract and "source/registry mismatch" in contract)
    check("A referent contract has the local/global type gate", "retype admissibility as the complete local law" in contract and "separate law axiom" in contract)

    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A live foundation still has four named axioms", all(f"### {name}" in axioms for name in ("Lattice", "Qubit", "Admissibility", "Record")))
    check("A live Record occurrence remains exact", "Records form." in axioms)
    check("A live Record permanence remains exact", "records are permanent." in axioms)
    check("A live Admissibility remains one fixed rule", "There is one fixed nearest-neighbor admissibility rule" in axioms)
    check("A live memo still separates Admissibility from dynamics", "Admissibility is not a dynamics axiom." in axioms)
    lowered_axioms = axioms.lower()
    check("A no canonical-law placeholder entered live axioms", "canonical-law" not in lowered_axioms and "[canonical" not in lowered_axioms)
    check("A no witness trigger entered live axioms", "two witness" not in lowered_axioms and "read twice" not in lowered_axioms)
    check("A no clock lock entered live axioms", "clock locks" not in lowered_axioms and "clock causes" not in lowered_axioms)

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    check(
        "A registry canonical ids remain exactly approved",
        registry.get("canonical_ids")
        == [
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ],
    )
    check("A no admission class appears in registry", "admission" not in json.dumps(registry).lower())


def q_lambda(lam: int, n_zero: int, n_one: int) -> tuple[Fraction, Fraction]:
    zero = lam**n_zero
    one = lam**n_one
    return Fraction(zero, zero + one), Fraction(one, zero + one)


def exact_law_lower_bound() -> None:
    section("B - Exact-law value lower bound")
    profiles = tuple((n0, n1) for n0 in range(7) for n1 in range(7 - n0))
    for lam in (1, 2):
        check(f"B q_{lam} normalizes", all(sum(q_lambda(lam, *profile)) == 1 for profile in profiles))
        check(f"B q_{lam} is positive", all(all(weight > 0 for weight in q_lambda(lam, *profile)) for profile in profiles))
        check(
            f"B q_{lam} is label covariant",
            all(q_lambda(lam, n0, n1) == tuple(reversed(q_lambda(lam, n1, n0))) for n0, n1 in profiles),
        )
    fair = q_lambda(1, 2, 1)
    biased = q_lambda(2, 2, 1)
    check("B paired laws share full support", all(value > 0 for value in fair + biased))
    check("B paired laws predict one-half versus two-thirds", fair[0] == Fraction(1, 2) and biased[0] == Fraction(2, 3))
    check("B exact transcript test separates representatives", fair != biased)

    # Deterministic laws remove sampling but not law identity.
    identity = lambda bit: bit
    toggle = lambda bit: 1 - bit
    check("B deterministic identity has one successor", identity(0) == 0)
    check("B deterministic toggle has one successor", toggle(0) == 1)
    check("B deterministic uniqueness leaves different exact laws", identity(0) != toggle(0))


def n_qubit_swap(n: int, left: int, right: int) -> np.ndarray:
    size = 2**n
    result = np.zeros((size, size), dtype=complex)
    for bits in product((0, 1), repeat=n):
        source = sum(bit << (n - 1 - index) for index, bit in enumerate(bits))
        target_bits = list(bits)
        target_bits[left], target_bits[right] = target_bits[right], target_bits[left]
        target = sum(bit << (n - 1 - index) for index, bit in enumerate(target_bits))
        result[target, source] = 1.0
    return result


def reversible_dimensionless_control() -> None:
    section("C - Reversible structural freedom is not only clock scale")
    s01 = n_qubit_swap(3, 0, 1)
    s02 = n_qubit_swap(3, 0, 2)
    s12 = n_qubit_swap(3, 1, 2)
    h1 = s01 + s02
    h2 = s01 @ s02 + s02 @ s01
    ratios = []
    for eta in (0.0, 1.0 / 3.0):
        h = h1 + eta * h2
        check(f"C H_eta Hermitian eta={eta}", np.allclose(h, h.conj().T))
        check(f"C H_eta neighbor-exchange covariant eta={eta}", np.allclose(h @ s12, s12 @ h))
        levels: list[float] = []
        for value in np.linalg.eigvalsh(h):
            if not levels or abs(value - levels[-1]) > 1.0e-9:
                levels.append(float(value))
        check(f"C H_eta has three invariant levels eta={eta}", len(levels) == 3)
        gaps = (levels[1] - levels[0], levels[2] - levels[1])
        ratios.append(gaps[0] / gaps[1])
    check("C eta zero gap ratio is two", math.isclose(ratios[0], 2.0, abs_tol=1.0e-9))
    check("C eta one-third gap ratio is one", math.isclose(ratios[1], 1.0, abs_tol=1.0e-9))
    check("C global rescaling cannot identify the spectra", not math.isclose(ratios[0], ratios[1], abs_tol=1.0e-9))


def mechanism_separations() -> None:
    section("D - Mechanism separations")
    # One measure does not choose its actual member.
    fair_measure = {0: Fraction(1, 2), 1: Fraction(1, 2)}
    histories = ({"measure": fair_measure, "actual": 0}, {"measure": fair_measure, "actual": 1})
    check("D one measure admits two actual members", histories[0]["measure"] == histories[1]["measure"] and histories[0]["actual"] != histories[1]["actual"])

    # Append preservation is a theorem of one law, not of every renewal law.
    first = {0: 1}
    append = {**first, 1: 0}
    overwrite = {**append, 0: 0}
    check("D append preserves old record", append[0] == first[0])
    check("D renewal does not logically force preservation", overwrite[0] != first[0] and 1 in overwrite)

    # Causal predecessors remove simulator order for scalar event factors.
    p_a = Fraction(1, 3)
    p_b = Fraction(2, 5)
    check("D independent causal event order is gauge", p_a * p_b == p_b * p_a)
    # A live-read second event can depend on the first and become order-valued.
    left_first = {"00": Fraction(1, 2), "01": Fraction(1, 2)}
    right_first = {"01": Fraction(1, 2), "11": Fraction(1, 2)}
    check("D uncontrolled live-read schedules are distinguishable", left_first != right_first)

    # Same lapse does not fix spatial curvature/lensing.
    pure_lapse = 2 * (1 + 0)  # coefficient of GM/b
    gr = 2 * (1 + 1)
    check("D pure lapse and GR bending differ by factor two", pure_lapse == 2 and gr == 4)

    # Finite permanent archive with positive write current saturates.
    capacity = 100
    current = Fraction(5, 2)
    saturation_time = Fraction(capacity, 1) / current
    check("D finite positive append current saturates", saturation_time == 40)


def synthesis_contract() -> None:
    section("E - Synthesis classification and language gate")
    note = normalized(NOTE)
    for field in (
        "domain",
        "state",
        "context",
        "atomic_law",
        "continuation",
        "availability",
        "concurrency",
        "record",
        "actuality",
        "statistics",
    ):
        check(f"E synthesis classifies {field.upper()}", field in note)

    for lane in (
        "operational quantum",
        "probability",
        "time",
        "matter/continuum",
        "counting/mass",
        "resource",
        "gravity",
        "thermodynamic arrow",
        "cosmology/boundary",
    ):
        check(f"E synthesis covers lane {lane}", lane in note)

    check("E universal minimum is exact-law identity", "one exact law identity" in note)
    check("E no tested architecture forces a universal sampling atom", "microscopic sampler is additional physics" in note and "not a generic constitutional atom" in note and "normalized measure alone selects no member" in note)
    check("E permanent record sectors bound full-space unique ergodicity", "union is not uniquely ergodic" in note)
    check("E deterministic Bell price remains explicit", "chsh <= 2" in note and "context-correlated boundary data" in note)
    check("E tied and untied counting branches remain explicit", "tied {s,d} gives w=1/2" in note and "untied {s,d+,d-} gives w=1/3" in note)
    check("E chirality is law- or boundary-owned", "any chiral sign is law-owned" in note and "boundary/state-owned" in note)
    check("E infinite reversible export remains boundary-relative", "blank-tape/no-return boundary" in note and "both ghz branches" in note)
    check("E finite reversible permanence theorem is recorded", "invertibility makes it reducing" in note and "blank complement cannot enter" in note)
    check("E programmed fundamental carrier is exact", "programmed cycle-13 wire closes" in note and "one m_2(c) per actual" in note)
    check("E autonomous compiler remains open", "autonomous program generation" in note)
    check("E self-writing closes the static program", "seven permanent seed records" in note and "static-program and unknown-open-state walls" in note)
    check("E self-writing collision remains open", "merge, braid, priority" in note and "twenty-two fresh record sites" in note)
    check("E bounded selectors have genuine but incomplete winners", "uniquely selects copy-equal" in note and "closes only four" in note)
    check("E selector inputs remain explicit", "candidate class, quotient, score, and success target" in note)
    check("E quantum selector leaves occurrence explicit", "no-write ties" in note and "missed-trigger cost" in note)
    check("E one-action steelman remains live", "one invariant action" in note and "forces those terms together" in note)
    check("E relational motif removes absolute axis need", "six permanent records can select an anchor" in note and "all 24 proper cubic rotations" in note)
    check("E fundamental schedule trilemma remains explicit", "moving record cursor" in note and "unrecorded mutable cursor" in note and "fresh site per tick" in note)
    check("E append-clock wording remains a theorem target", "remains a theorem/definition target" in note)
    check("E extension wording is a candidate-law theorem", "is a theorem. it is not a theorem of the current four axioms" in note)
    check("E Weyl pair is not silently quotiented", "not yet one same-labeled finite-record class" in note)
    check("E target-free action remains unselected", "no tested target-free action selects it" in note)
    check("E licensed equivalence remains a groupoid condition", "safe starting category" in note and "fixed-protocol relabelings" in note)
    check("E topological linkage does not supply occurrence", "conservation action has both an all-zero and an all-one solution" in note)
    check("E topological intersection retains physical forks", "sixteen physically different choices" in note and "topological qca" in note)
    check("E simulation overhead remains physically testable", "additive record totals" in note and "path-count weights from 1/2 to 2/3" in note)
    check("E causal invariance is not conflated with confluence", "causal-graph invariance is also distinct from church–rosser confluence" in note)
    check("E Ward conservation does not trigger occurrence", "conservation can transport and protect a commit" in note and "does not make the first commit" in note)
    check("E occurrence remains inside the exact referent", "event/actualization map must be exact inside the selected law referent" in note)
    check("E Lüders form is derived but context remains", "exact x and z instruments both satisfy it" in note and "sentence belongs in record" in note)
    check("E compatible scheduler confluence is derived", "one least fair-schedule closure" in note and "protected bell cages" in note)
    check("E incompatible writes move upstream", "establish compatibility before locking" in note and "dynamical-law fork" in note)
    check("E infinite sector retires phase but not actuality", "mixtures with weights 1/2 and 2/3" in note and "cannot supply occurrence, weight, actuality, or rate" in note)
    check("E exact interaction derives pointer context conditionally", "two-dimensional system-side commutant" in note and "unique binary pointer pvm" in note)
    check("E present Bell interaction leaves transverse azimuth", "center x and center y" in note and "remaining azimuth" in note)
    check("E record-generated normal is covariant", "six outward nearest-neighbor normals" in note and "post-record outward geometry" in note)
    check("E boundary index does not select the record law", "same index admits" in note and "coherent dilation or an actual record instrument" in note)
    check("E finite named-port closure can be local", "two finite named ports" in note and "symmetric parity fact" in note)
    check("E finite-radius silence cannot certify global closure", "far source at distance r+2" in note and "unbounded unclosed channel" in note)
    check("E all-rule union is not predictive selection", "every possible eight-bit configuration" in note and "record-faithful quotient" in note)
    check("E bounded observer is not full future equivalence", "first h record bits" in note and "one-bit separator" in note)
    check("E existing Y and Z rays construct X conditionally", "-i y_f z_f" in note and "full relational pauli frame" in note)
    check("E chirality does not select X versus Y", "proper quarter-turn around z" in note and "unordered binary pvm" in note)
    check("E 3-D anomaly class leaves microscopic representative", "same anomalous bulk" in note and "concurrence" in note and "compiled" in note)
    check("E autonomous diamond retires supplied finite interface", "radius-two cubic fence" in note and "first localized record" in note)
    check("E complete protocol transport can retire representative phase", "fixed decoder distinguishes" in note and "transporting every record branch" in note)
    check("E finite adaptive transport is exact but category-relative", "every finite adaptive transcript" in note and "maximal local-record category" in note and "physical category closure" in note)
    check("E exactly-one seed wall does not become a formation no-go", "no invariant law concentrated on one finite nonempty seed set" in note and "infinitely many seeds almost surely" in note)
    check("E foundation site-net quotient excludes entangling frames", "720" in note and "72" in note and "distributed subfactor" in note)
    check("E transported-net steelman remains semantic", "48 signed-coordinate" in note and "24 proper" in note and "fixed versus transported site identity" in note)
    check("E law gauge keeps locality and record invariants", "compositional" in note and "uniformly local" in note and "choi rank" in note and "every finite reversible edge to identity" in note)
    check("E parity role is not generic record content", "probabilities 1 versus 1/2" in note and "physically legal future tester repertoire" in note)
    check("E clock count derives only after event identity", "schedule-independent relational clock" in note and "total record count" in note and "relative rate" in note)
    check("E NN seed compiler leaves carrier/finalization explicit", "closed candidate layer" in note and "transient mutable" in note and "permanence blocks provisional rewrite" in note)
    check("E Born form leaves one normalized law field", "exact normalized effect-complete operational record law" in note and "trial/reset corpus" in note and "pointwise-versus-almost-sure scope" in note)
    check("E NN seed escape remains scoped to law content", "direct positive-rate nn commits fail" in note and "bounded lindbladian" in note and "message garbage remains open" in note and "forces no record clause" in note)
    check("E frequency remains a theorem contract on global W", "certificate ancestry" in note and "recurring projectively consistent blocks" in note and "no iid, reset, stationary, or ergodic record clause" in note)
    check("E one-law packing preserves the three placement outcomes", "blind residual-packing audit" in note and "one retyped admissibility identification" in note and "one separate law identification" in note and "no independent record" in note)
    check("E state revision remains conditional rather than universal", "global record-history law" in note and "separate law slot" in note and "qualification state-type revision" in note and "no state or record edit is universally forced" in note)
    check("E actuality is a conditional history route, not a universal second atom", "actuality correction: conditional history route" in note and "complete history h" in note and "pushforward measure alone does not select" in note)
    check("E record-only NN construction defeats forced state widening", "5,202-site permanent fortress" in note and "strong-lumpability boundary" in note and "writes b0 last" in note and "no qubit, admissibility, record, or state edit" in note)
    check("E global record process preserves the ontology type gate", "normalized strongly positive decoherence functional" in note and "identity insertion" in note and "scalar quantum measure" in note and "separate law identification" in note)
    check("E model theory retires a duplicate existence axiom", "one slot is not one extension" in note and "second existence-only law sentence" in note and "majority and minority availability maps" in note and "weights 1/2 and 2/3" in note)
    check("E clause deletion leaves one universal-looking identity in tested routes", "model-theory correction" in note and "one universal-looking survivor across the tested routes" in note and "no present scientific case" in note)
    check("E long-run capacity is theorem plus conditional architecture gate", "permanence is already the budget" in note and "lambda t <= 1" in note and "spacetime formation density vanishes" in note and "conditional architecture gate" in note)
    check("E local composition can derive the global process", "exact local-to-global witness" in note and "same cz gate" in note and "all-zero and all-plus boundaries" in note and "separate global law would double-count" in note)
    check("E parity certificate conditionally selects center X", "z_a x_b z_c" in note and "center sign" in note and "endpoint xor" in note)
    check("E zero-edit route remains live", "outcome a — zero axiom update" in note)
    check("E retyped-Admissibility route is staged", "outcome b — retype admissibility and identify one local law" in note)
    check("E separate-Law route is staged", "outcome c — retain admissibility and add one law identification" in note)
    check("E Record clarification remains conditional", "outcome d — exact law plus one record clarification" in note)
    check("E current live-edit verdict is none", "minimum live edit justified today: none" in note)
    check("E likely local-law edit is a retyped Admissibility identification", "one retyped and polished admissibility/local-law identification" in note)
    check("E global-history placement remains type-safe", "one separate law identification while admissibility remains a menu rule" in note)
    check("E witness/count/clock prose is rejected", "witness count, read trigger, clock lock" in note)
    check("E exact reference cannot be an architecture name", "not qca, multiway, causal-front" in note)
    check("E synchronized surface map includes registry", "axiom_premise_nodes.json" in note)
    check("E synchronized surface map includes policy", "axiom_minimality_policy.md" in note)
    check("E synchronized surface map includes runner", "audit_companion_minimal_axioms_clean_base_exact.py" in note)
    check("E executable impact map is linked", "one_cut_foundation_surface_impact_map_note_2026-07-14.md" in note)
    check("E audit verdicts remain excluded", "without authoring or applying an audit verdict" in note)


def no_go_discipline_structure() -> None:
    section("F - Fresh N1-N8 no-go-discipline structure")
    raw = NOTE.read_text(encoding="utf-8")
    note = normalized(NOTE)
    n1 = raw.split("### N1", 1)[1].split("### N2", 1)[0]
    attempted_rows = [line for line in n1.splitlines() if "`ATTEMPTED`" in line and line.startswith("|")]
    check("F N1 has at least five marked routes", len(attempted_rows) >= 5, f"rows={len(attempted_rows)}")
    check("F N1 has no unauthorized prior marker", "RULED IN BY PRIOR" not in n1 and "RULED OUT BY PRIOR" not in n1)
    check("F N2 declares one collapsed referent wall", "collapsed wall set" in note and "stable extensional identity" in note)
    check("F N2 has no fake pairwise independence count", "no unordered pairs inside a one-wall set" in note)
    check("F N3 has a hit/classification/action table", "| hit | line/section | classification | action |" in raw)
    check("F N3 resolves hidden conditions", "unresolved hidden-condition count after classification: 0" in note)
    check("F N4 has residual-matching columns", "| witness | exact residual | exact-law non-entailment? |" in raw)
    check("F N4 drops mismatched witnesses", note.count("drop as exact-law evidence") >= 3 and "boundary only" in note)
    for scope in ("finite instance", "candidate class", "full lattice", "all legal protocols", "all law space"):
        check(f"F N5 names resolution: {scope}", scope in note)
    check("F N5 leaves all-law-space open", "all law space | open" in note)
    check("F N6 has path/status/closure columns", "| path | status | what it closes |" in raw)
    check("F N6 keeps approved primitives out of wall count", "approved premise, not a wall" in note)
    check("F N7 has hostile steelman and outcome", "hostile steelman:" in note and "outcome:" in note)
    check("F N7 demotes broad impossibility", "broad impossibility is demoted" in note and "partial-narrowing" in note)
    check("F N8 has retirement/mechanism/applicability columns", "| prior wall | retired? | mechanism | applicable here? |" in raw)
    n8 = raw.split("### N8", 1)[1].split("## Current Cut Verdict", 1)[0]
    n8_rows = [line for line in n8.splitlines() if line.startswith("|") and "---" not in line]
    check("F N8 has at least three substantive rows", len(n8_rows) >= 4, f"rows={len(n8_rows)-1}")


def run_companions() -> None:
    section("G - Companion runner regression")
    for path in COMPANIONS:
        check(f"G companion exists: {path.name}", path.is_file())
        if not path.is_file():
            continue
        try:
            completed = subprocess.run(
                [sys.executable, str(path)],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=240,
                check=False,
            )
        except subprocess.TimeoutExpired:
            check(f"G companion returns: {path.name}", False, "timeout")
            continue
        tail = " | ".join(completed.stdout.splitlines()[-3:])
        check(f"G companion returns: {path.name}", completed.returncode == 0, tail)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-companions", action="store_true", help="skip the slower companion-runner regression")
    args = parser.parse_args()

    source_and_authority_contract()
    exact_law_lower_bound()
    reversible_dimensionless_control()
    mechanism_separations()
    synthesis_contract()
    no_go_discipline_structure()
    if not args.skip_companions:
        run_companions()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("CUT_GATE: no live axiom edit until an exact law referent, uniqueness theorem, or exact physical-equivalence class exists")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
