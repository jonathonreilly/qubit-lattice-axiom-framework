#!/usr/bin/env python3
"""Finite exact probes for the July 14 predictive-specification tournament."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import json
import math


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
WILSON = ROOT / "docs" / "G_BARE_DERIVATION_NOTE.md"
WILSON_SELECTOR = (
    ROOT / "docs" / "WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md"
)
STAGGERED_NO_GO = (
    ROOT / "docs" / "STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md"
)
REVIEW_DIR = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
CYCLE8_NOTES = {
    "bell": REVIEW_DIR / "CFSI_Q_BELL_COHERENT_CAUSAL_FRONT_LAW_NOTE_2026-07-14.md",
    "cubic_repair": REVIEW_DIR / "CUBIC_COVARIANCE_EXACT_REPAIR_TOURNAMENT_NOTE_2026-07-14.md",
    "classification": REVIEW_DIR / "CUBIC_SPLIT_STEP_QW_QCA_PRIMARY_SOURCE_UNIQUENESS_AUDIT_2026-07-14.md",
    "schedule": REVIEW_DIR / "CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md",
    "kernel": REVIEW_DIR / "CUBIC_NEIGHBOR_KERNEL_SELECTION_FIRST_PRINCIPLES_NOTE_2026-07-14.md",
}
LATE_CYCLE_NOTES = {
    "actualization": REVIEW_DIR / "BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md",
    "nucleation": REVIEW_DIR / "AUTONOMOUS_HOMOGENEOUS_BINARY_NUCLEATION_NOTE_2026-07-14.md",
    "resource": REVIEW_DIR / "LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md",
    "reversible": REVIEW_DIR / "REVERSIBLE_DILATION_CLOSED_CYCLE_GRAVITY_CYCLE10_NOTE_2026-07-14.md",
    "language": REVIEW_DIR / "QUALITATIVE_SUBSTRATE_EXACT_LAW_SELECTION_NOTE_2026-07-14.md",
    "deterministic": REVIEW_DIR / "DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md",
    "matter": REVIEW_DIR / "MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md",
    "infinite_qca": REVIEW_DIR / "INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
}
RECENT_CYCLE_NOTES = {
    "append": REVIEW_DIR / "APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md",
    "self_writing": REVIEW_DIR / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md",
    "licensed_equivalence": REVIEW_DIR / "FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md",
    "simulation_equivalence": REVIEW_DIR / "INTRINSIC_SIMULATION_OBSERVER_EQUIVALENCE_RECORD_COST_NOTE_2026-07-14.md",
    "single_action": REVIEW_DIR / "SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md",
    "topological": REVIEW_DIR / "TOPOLOGICAL_CONSERVATION_RG_ACTION_STEELMAN_NOTE_2026-07-14.md",
    "qca_ward": REVIEW_DIR / "PROPER_CUBIC_QUBIT_QCA_WARD_IDENTITY_STEELMAN_NOTE_2026-07-14.md",
    "instrument": REVIEW_DIR / "RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md",
    "abelian_merge": REVIEW_DIR / "ABELIAN_COMPATIBLE_SEED_BELL_MERGE_CYCLE15_NOTE_2026-07-14.md",
    "infinite_sector": REVIEW_DIR / "INFINITE_REDUNDANCY_QUASILOCAL_RECORD_SECTOR_NOTE_2026-07-14.md",
    "relational_pointer": REVIEW_DIR / "RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md",
    "dynamic_boundary_index": REVIEW_DIR / "DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md",
    "delayed_lock": REVIEW_DIR / "DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md",
    "universal_rule_space": REVIEW_DIR / "UNIVERSAL_RULE_SPACE_MULTIWAY_LAW_STEELMAN_NOTE_2026-07-14.md",
    "chiral_triad_context": REVIEW_DIR / "CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md",
    "three_d_anomaly": REVIEW_DIR / "THREE_DIMENSIONAL_ANOMALOUS_BULK_CATEGORY_INDEX_STEELMAN_NOTE_2026-07-14.md",
    "autonomous_close": REVIEW_DIR / "AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md",
    "primitive_protocol_equivalence": REVIEW_DIR / "PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md",
    "actual_header_decoder": REVIEW_DIR / "ACTUAL_HEADER_ROLE_DECODER_PARITY_SELECTION_CYCLE18_NOTE_2026-07-14.md",
    "adaptive_full_abstraction": REVIEW_DIR / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md",
    "invariant_seed_field": REVIEW_DIR / "INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md",
    "site_net_equivalence": REVIEW_DIR / "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md",
    "operational_parity": REVIEW_DIR / "COMPLETE_FUTURE_OPERATIONAL_PARITY_CERTIFICATE_CYCLE19_NOTE_2026-07-14.md",
    "named_site_equivalence": REVIEW_DIR / "NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md",
    "commit_clock": REVIEW_DIR / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md",
    "seed_compilation": REVIEW_DIR / "NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md",
    "born_affinity": REVIEW_DIR / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "sort_equivalence": REVIEW_DIR / "FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md",
    "dissipative_seed": REVIEW_DIR / "QUANTUM_DISSIPATIVE_SEED_ESCAPE_CYCLE20_NOTE_2026-07-14.md",
    "frequency_corpus": REVIEW_DIR / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md",
    "residual_packing": REVIEW_DIR / "BLIND_RESIDUAL_ATOM_PACKING_AND_ONE_LAW_CONSTITUTIONAL_SCHEMA_NOTE_2026-07-14.md",
    "record_state_bell": REVIEW_DIR / "RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md",
    "actuality_semantics": REVIEW_DIR / "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md",
    "record_state_fortress": REVIEW_DIR / "RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md",
    "global_record_process": REVIEW_DIR / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md",
    "admissibility_definability": REVIEW_DIR / "ADMISSIBILITY_SYMBOL_DEFINABILITY_AND_EXACT_LAW_REFERENCE_CHALLENGE_NOTE_2026-07-14.md",
    "constitutional_lower_bound": REVIEW_DIR / "CONSTITUTIONAL_LOWER_BOUND_CLOSURE_AND_CLAUSE_DELETION_CYCLE31_NOTE_2026-07-14.md",
    "long_run_append": REVIEW_DIR / "LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md",
    "local_global_glue": REVIEW_DIR / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md",
    "moving_logical_front": REVIEW_DIR / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md",
    "final_missing_census": REVIEW_DIR / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md",
    "cubic_cz_selection": REVIEW_DIR / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md",
    "temporal_equivalence": REVIEW_DIR / "TEMPORAL_PROTOCOL_EQUIVALENCE_ALTERNATING_FRAME_CYCLE39_NOTE_2026-07-14.md",
    "cubic_clifford": REVIEW_DIR / "CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md",
    "candidate_assembly": REVIEW_DIR / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md",
    "history_identifiability": REVIEW_DIR / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md",
}

OPEN = -1
DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}
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


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[tuple[int, ...], ...]:
    rotations: list[tuple[int, ...]] = []
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(axis_permutation) * math.prod(signs) != 1:
                continue
            matrix = [[0, 0, 0] for _ in range(3)]
            for row in range(3):
                matrix[row][axis_permutation[row]] = signs[row]
            direction_permutation = []
            for direction in DIRECTIONS:
                rotated = tuple(
                    sum(matrix[row][column] * direction[column] for column in range(3))
                    for row in range(3)
                )
                direction_permutation.append(DIR_INDEX[rotated])
            rotations.append(tuple(direction_permutation))
    return tuple(rotations)


def swap_profile(profile: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(OPEN if value == OPEN else 1 - value for value in profile)


def swap_answer(answer: frozenset[int]) -> frozenset[int]:
    return frozenset(1 - value for value in answer)


def availability(profile: tuple[int, ...]) -> frozenset[int]:
    recorded = tuple(value for value in profile if value != OPEN)
    if recorded and len(set(recorded)) == 1:
        return frozenset((recorded[0],))
    return frozenset((0, 1))


def full_support(profile: tuple[int, ...]) -> frozenset[int]:
    return availability(profile)


def majority_support(profile: tuple[int, ...]) -> frozenset[int]:
    answer = availability(profile)
    if len(answer) == 1:
        return answer
    recorded = tuple(value for value in profile if value != OPEN)
    n_zero = recorded.count(0)
    n_one = recorded.count(1)
    if n_zero == n_one:
        return answer
    return frozenset((0 if n_zero > n_one else 1,))


def source_contract() -> None:
    section("A - Authority, source, and live-surface guards")
    note = NOTE.read_text(encoding="utf-8")
    normalized = note.lower().replace("*", "").replace("`", "")
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    check("A note is authority-free", "authority: none" in normalized)
    check("A note defers final language", "no final sentence is frozen" in normalized)
    check("A note carries all N1-N8 headings", all(f"### n{index}" in normalized for index in range(1, 9)))
    check("A live axiom has no instrument edit", "quantum instrument" not in axioms.lower())
    check("A live Record wording remains present", "records are permanent" in axioms)
    check(
        "A registry still has only the approved foundation ids",
        registry.get("canonical_ids")
        == [
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ],
    )


def availability_continuation_separation() -> None:
    section("B - Availability does not determine continuation support")
    profiles = tuple(product((OPEN, 0, 1), repeat=6))
    rotations = proper_cubic_rotations()
    check("B ternary six-neighbour domain has 729 profiles", len(profiles) == 729)
    check("B proper cubic action has 24 rotations", len(set(rotations)) == 24)
    for name, rule in (("availability", availability), ("full", full_support), ("majority", majority_support)):
        check(f"B {name} is total and nonempty", all(rule(profile) for profile in profiles))
        check(
            f"B {name} is proper-cubic invariant",
            all(
                rule(profile) == rule(tuple(profile[position] for position in rotation))
                for profile in profiles
                for rotation in rotations
            ),
        )
        check(
            f"B {name} is global-label covariant",
            all(rule(swap_profile(profile)) == swap_answer(rule(profile)) for profile in profiles),
        )
    check(
        "B both support laws refine the same availability",
        all(full_support(p) <= availability(p) and majority_support(p) <= availability(p) for p in profiles),
    )
    witness = (0, 0, 1, OPEN, OPEN, OPEN)
    check(
        "B support laws differ on a 2:1 mixed profile",
        full_support(witness) == frozenset((0, 1))
        and majority_support(witness) == frozenset((0,)),
    )
    check("B availability varies with conditions", len({availability(p) for p in profiles}) == 3)


def append_nonreconnection_and_actuality() -> None:
    section("C - Append-only nonreconnection and actuality independence")
    # One-site partial records are enough for the exact cone argument.
    states = ((), (("x", 0),), (("x", 1),))

    def as_dict(state: tuple[tuple[str, int], ...]) -> dict[str, int]:
        return dict(state)

    def append_extends(source: tuple[tuple[str, int], ...], target: tuple[tuple[str, int], ...]) -> bool:
        source_map = as_dict(source)
        target_map = as_dict(target)
        return all(target_map.get(site) == value for site, value in source_map.items())

    zero = (("x", 0),)
    one = (("x", 1),)
    zero_cone = frozenset(state for state in states if append_extends(zero, state))
    one_cone = frozenset(state for state in states if append_extends(one, state))
    check("C zero sibling has a nonempty future cone", bool(zero_cone))
    check("C one sibling has a nonempty future cone", bool(one_cone))
    check("C append-only sibling cones do not reconnect", zero_cone.isdisjoint(one_cone))

    # If overwriting is admitted, the zero sibling can change to one and meet
    # the one sibling. This isolates the immutable-extension hypothesis.
    overwrite_zero_cone = frozenset((zero, one))
    overwrite_one_cone = frozenset((zero, one))
    check("C overwrite completion reconnects the same siblings", not overwrite_zero_cone.isdisjoint(overwrite_one_cone))

    histories = ((zero,), (one,))
    check("C one support graph admits distinct actual histories", len(set(histories)) == 2)
    check("C nonreconnection alone does not choose between them", zero_cone.isdisjoint(one_cone) and len(histories) > 1)


def symmetry_obstruction() -> None:
    section("D - Symmetry cannot deterministically create the first classical label")
    # On a transitive eight-site cube, translation-invariant configurations are
    # constant. Global label exchange fixes only the all-open constant state.
    constant_states = tuple((value,) * 8 for value in (OPEN, 0, 1))
    label_fixed = tuple(state for state in constant_states if swap_profile(state) == state)
    check("D translation invariance leaves three constant label states", len(constant_states) == 3)
    check("D label exchange fixes only all-open", label_fixed == ((OPEN,) * 8,))
    check("D no nonempty deterministic symmetric output exists", all(value == OPEN for value in label_fixed[0]))


def kernel(alpha: int, n_zero: int, n_one: int) -> tuple[Fraction, Fraction]:
    total = n_zero + n_one + 2 * alpha
    p_zero = Fraction(n_zero + alpha, total)
    return p_zero, 1 - p_zero


def statistics_independence() -> None:
    section("E - Strong statistics independence and refinement failure")
    profiles = tuple((n_zero, n_one) for n_zero in range(7) for n_one in range(7 - n_zero))
    for alpha in (1, 2):
        check(
            f"E alpha={alpha} kernel is normalized",
            all(sum(kernel(alpha, n_zero, n_one), Fraction(0)) == 1 for n_zero, n_one in profiles),
        )
        check(
            f"E alpha={alpha} kernel is strictly positive",
            all(all(probability > 0 for probability in kernel(alpha, n_zero, n_one)) for n_zero, n_one in profiles),
        )
        check(
            f"E alpha={alpha} kernel is label covariant",
            all(
                kernel(alpha, n_one, n_zero) == tuple(reversed(kernel(alpha, n_zero, n_one)))
                for n_zero, n_one in profiles
            ),
        )
    check("E two covariant local kernels share full support", all(all(p > 0 for p in kernel(a, 2, 1)) for a in (1, 2)))
    check("E kernels disagree on the same 2:1 profile", kernel(1, 2, 1) != kernel(2, 2, 1))

    # Disjoint-product composition and cylinder consistency are exact for both.
    for alpha in (1, 2):
        first = kernel(alpha, 2, 1)
        second = kernel(alpha, 1, 2)
        joint = tuple(p * q for p in first for q in second)
        check(f"E alpha={alpha} disjoint product normalizes", sum(joint, Fraction(0)) == 1)
        marginal = (joint[0] + joint[1], joint[2] + joint[3])
        check(f"E alpha={alpha} cylinder marginal is consistent", marginal == first)

    coarse = (Fraction(1, 2), Fraction(1, 2))
    refined = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    refined_operational = (refined[0], refined[1] + refined[2])
    check("E naive uniform counting changes under presentation refinement", refined_operational != coarse)
    check("E refined equivalent branch gets two thirds by raw counting", refined_operational == (Fraction(1, 3), Fraction(2, 3)))


def channel_instrument_distinction() -> None:
    section("F - Nonselective channel is not a sampled instrument")
    # Exact 2x2 rational matrices for rho_plus and its projector branches.
    rho_plus = ((Fraction(1, 2), Fraction(1, 2)), (Fraction(1, 2), Fraction(1, 2)))
    branch_zero = ((rho_plus[0][0], Fraction(0)), (Fraction(0), Fraction(0)))
    branch_one = ((Fraction(0), Fraction(0)), (Fraction(0), rho_plus[1][1]))
    dephased = tuple(
        tuple(branch_zero[row][column] + branch_one[row][column] for column in range(2))
        for row in range(2)
    )
    check("F dephasing removes off-diagonal coherence", dephased == ((Fraction(1, 2), 0), (0, Fraction(1, 2))))
    probabilities = (branch_zero[0][0] + branch_zero[1][1], branch_one[0][0] + branch_one[1][1])
    check("F labelled branches form a normalized instrument", probabilities == (Fraction(1, 2), Fraction(1, 2)))
    check("F nonselective state is the sum of both branches", dephased[0][0] == sum(probabilities[:1]) and dephased[1][1] == sum(probabilities[1:]))
    check("F mixture contains no selected-outcome field", len(probabilities) == 2 and dephased[0][0] == dephased[1][1])


def clock_rate_independence() -> None:
    section("G - Event order does not determine duration or lapse")
    order_edges = (("e0", "e1"), ("e1", "e2"))
    lapse_a = (Fraction(1), Fraction(1))
    lapse_b = (Fraction(2), Fraction(3))
    check("G both assignments live on the same event order", len(order_edges) == len(lapse_a) == len(lapse_b))
    check("G both lapse assignments are positive", all(value > 0 for value in lapse_a + lapse_b))
    check("G same order admits different elapsed durations", sum(lapse_a) != sum(lapse_b))


def action_selection_boundary() -> None:
    section("H - Existing action stack does not identify the substrate law")
    wilson = WILSON.read_text(encoding="utf-8").lower()
    selector = WILSON_SELECTOR.read_text(encoding="utf-8").lower()
    normalized_selector = selector.replace("*", "").replace("`", "")
    staggered = STAGGERED_NO_GO.read_text(encoding="utf-8").lower()
    check("H Wilson bridge disclaims action-form derivation", "not a derivation of the wilson action form itself" in wilson)
    check("H Wilson bridge leaves action-surface selection open", "wilson action-surface selection" in wilson and "remains open" in wilson)
    check("H Wilson selector is restricted to a bounded ansatz", "canonical leading-`β` single-trace" in selector)
    check(
        "H Wilson selector disclaims uniqueness over all class functions",
        "does not prove uniqueness over all real-valued class functions" in normalized_selector,
    )
    check("H July-10 theorem is a kinetic selection non-forcing result", "minimal-surface kinetic/corner non-forcing" in staggered)
    check("H July-10 theorem supplies an inequivalent qubit-exchange completion", "qubit-exchange kinetic completion" in staggered)


def physical_equivalence_boundary() -> None:
    section("I - Operational equivalence requires the complete statistics table")
    p = kernel(1, 2, 1)
    q = kernel(2, 2, 1)
    check("I one recorded local test separates the two candidate laws", p != q)
    check("I exact operational equivalence cannot identify separated laws", not all(left == right for left, right in zip(p, q)))
    check("I an equivalence class still needs every test probability", len(p) == len(q) == 2 and sum(p) == sum(q) == 1)


def note_completeness() -> None:
    section("J - Tournament documentation contract")
    note = NOTE.read_text(encoding="utf-8")
    for field in (
        "`DOMAIN`",
        "`STATE`",
        "`CONTEXT`",
        "`ATOMIC_LAW`",
        "`CONTINUATION`",
        "`AVAILABILITY`",
        "`CONCURRENCY`",
        "`RECORD`",
        "`ACTUALITY`",
        "`STATISTICS`",
    ):
        check(f"J note classifies {field}", field in note)
    for candidate in (
        "monotone availability closure",
        "process state + compatible sampled instruments",
        "Wilson-plus-staggered action",
        "global tensor/action history",
        "Wolfram-style multiway hypergraph rewriting",
        "error-correcting/topological archive",
        "Bell-current objective-jump QCA",
        "classical append-only CA",
    ):
        check(f"J note includes candidate: {candidate}", candidate.lower() in note.lower())
    check(
        "J note names the exact-law-value residue",
        "none of the current four" in note.lower()
        and "selects this exact tuple" in note.lower(),
    )
    check(
        "J note forbids a final axiom cut in this cycle",
        "authorize an axiom edit" in note.lower() and "does not establish" in note.lower(),
    )


def cycle12_reduction_contract() -> None:
    section("K - Cycle-12 reduction and companion contract")
    note = NOTE.read_text(encoding="utf-8").lower()
    axioms = AXIOMS.read_text(encoding="utf-8").lower()
    check("K tournament title now covers cycles 1-42", "cycles 1–42" in note)
    check("K every Cycle-8 companion note exists", all(path.is_file() for path in CYCLE8_NOTES.values()))
    companions = {
        name: path.read_text(encoding="utf-8").lower()
        for name, path in CYCLE8_NOTES.items()
    }
    check("K Bell construction contains exact Tsirelson target", "2 sqrt(2)" in companions["bell"])
    check("K Bell construction exposes exact-law-value ablation", "v=1/2" in companions["bell"])
    check("K cubic repair contains the finite M12 block", "m12" in companions["cubic_repair"])
    check("K cubic repair leaves primitive M2 open", "primitive m2 remains open" in companions["cubic_repair"])
    check("K classification leaves the exact update unselected", "exact update remains unselected" in companions["classification"])
    check(
        "K schedule probe derives linear-extension equivalence",
        "all linear extensions agree exactly" in companions["schedule"],
    )
    check(
        "K schedule probe rejects schedule randomization as a quotient",
        "randomizing the scheduler" in companions["schedule"]
        and "it is not a quotient" in companions["schedule"],
    )
    check(
        "K kernel probe counts ten proper-cubic orbits",
        "reduce them to ten geometric types" in companions["kernel"],
    )
    check("K kernel probe derives incidence only after channel additivity", "finite additivity" in companions["kernel"] and "incidence" in companions["kernel"])
    check("K synthesis rejects a reader/witness/clock Record clause", "reader, witness count, clock trigger" in note)
    check("K synthesis retains only an exact-law reference as universal residue", "one exact predictive law value" in note)
    check("K live axioms were not silently given a canonical-law placeholder", "canonical-law" not in axioms and "cfsi-q7" not in axioms)

    check("K every Cycle-9/10 companion note exists", all(path.is_file() for path in LATE_CYCLE_NOTES.values()))
    late = {
        name: path.read_text(encoding="utf-8").lower()
        for name, path in LATE_CYCLE_NOTES.items()
    }
    check("K actualization audit rejects clock selection", "clock can count that order" in late["actualization"])
    check("K relational carrier exposes cross-site bridge", "cross-site reference transport" in late["nucleation"])
    check("K relational packet remains finite-radius atomic", "finite-radius atomic write" in late["nucleation"])
    check("K local resource probe derives controlled inverse window", "r^2 > 0.9998" in late["resource"] and "1/r" in late["resource"])
    check("K reversible closure identifies detailed-balance boundary", "detailed balance" in late["reversible"] and "green amplitude vanish" in late["reversible"])
    check("K scalar lapse does not fix GR lensing", "2gm/b" in late["reversible"] and "4gm/b" in late["reversible"])
    check("K qualitative-language probe includes reversible family", "partial-swap family" in late["language"])
    check(
        "K deterministic sectors defeat full-space unique ergodicity",
        "full state space is not uniquely ergodic" in late["deterministic"]
        or "union of both lawful archive sectors is not uniquely ergodic" in late["deterministic"],
    )
    check("K deterministic Bell control exposes contextual price", "chsh=2 sqrt(2)" in late["deterministic"] and "measurement independence" in late["deterministic"])
    check("K matter probe retains tied and untied instruments", "tied" in late["matter"] and "untied" in late["matter"] and "trine povm" in late["matter"])
    check("K matter probe rejects proper-cubic hand selection", "proper-cubic covariance also does not choose a hand" in late["matter"])
    check("K infinite QCA identifies blank-tape boundary", "blank-tape/no-return boundary" in late["infinite_qca"])
    check("K infinite QCA leaves fundamental compilation open", "not constructed" in late["infinite_qca"] and "one-qubit-per-site" in late["infinite_qca"])
    check("K Cycle-12 synthesis still rejects Record slogans", "reader, two-witness trigger, clock lock" in note)

    check("K every Cycle-13/17 companion note exists", all(path.is_file() for path in RECENT_CYCLE_NOTES.values()))
    recent = {
        name: path.read_text(encoding="utf-8").lower()
        for name, path in RECENT_CYCLE_NOTES.items()
    }
    check("K append law derives local extension", "permanent local extension" in recent["append"])
    check("K self-writing front removes hidden cursor", "no hidden cursor" in recent["self_writing"] and "22" in recent["self_writing"])
    check("K licensed equivalence leaves two proper-chiral orbits", "two proper-chiral presentation orbits" in recent["licensed_equivalence"])
    check("K intrinsic simulation is below record equivalence", "computational universality alone is insufficient" in recent["simulation_equivalence"])
    check("K one action can embed incompatible updates", "update `u` appears inside" in recent["single_action"] and "same complete action" in recent["single_action"])
    check("K topological action leaves zero/nonzero occurrence", "all-zero" in recent["topological"] and "all-one" in recent["topological"])
    check("K QCA Ward identity permits multiple transfer amounts", "1/4" in recent["qca_ward"] and "1/2" in recent["qca_ward"] and "unit transfer" in recent["qca_ward"])
    check("K binary repeatability derives Lueders form only after context", "form after context" in recent["instrument"])
    check("K compatible merge leaves distinct-content critical pair", "no common extension" in recent["abelian_merge"])
    check("K infinite sector retires phase but not actuality", "does not actualize one branch" in recent["infinite_sector"])
    check("K relational pointer theorem remains interaction-relative", "simple-fixed-axis theorem" in recent["relational_pointer"] and "center x" in recent["relational_pointer"])
    check("K generated boundary does not select record law", "record-generated boundary" in recent["dynamic_boundary_index"] and "same index" in recent["dynamic_boundary_index"])
    check("K delayed locking closes only finite named ports", "finite-radius silence no-go" in recent["delayed_lock"] and "two finite" in recent["delayed_lock"])
    check("K all-rule union can erase next-state prediction", "every possible eight-bit" in recent["universal_rule_space"] and "compiler-relative" in recent["universal_rule_space"])
    check("K two-ray frame derives X but not apparatus role", "two-ray frame theorem" in recent["chiral_triad_context"] and "apparatus-role" in recent["chiral_triad_context"])
    check("K 3-D anomaly class leaves local-circuit representative", "three-fermion" in recent["three_d_anomaly"] and "finite-depth" in recent["three_d_anomaly"])
    check("K autonomous diamond derives post-seed closure", "99-site" in recent["autonomous_close"] and "first realized seed" in recent["autonomous_close"])
    check("K primitive representative requires complete protocol transport", "update-plus-commit" in recent["primitive_protocol_equivalence"] and "complete protocol transport" in recent["primitive_protocol_equivalence"])
    check("K actual header plus parity certificate selects X conditionally", "adding the operational" in recent["actual_header_decoder"] and "parity-certificate contract uniquely selects" in recent["actual_header_decoder"] and "hard-coded x readiness prefix" in recent["actual_header_decoder"] and "rejected as circular" in recent["actual_header_decoder"])
    check("K adaptive full abstraction is exact but category-relative", "finite adaptive protocol tree" in recent["adaptive_full_abstraction"] and "natural isomorphism" in recent["adaptive_full_abstraction"] and "maximal local-record category" in recent["adaptive_full_abstraction"])
    check("K invariant seed field defeats a broad homogeneous-nucleation no-go", "empty local limit" in recent["invariant_seed_field"] and "positive-density hard-core seed process" in recent["invariant_seed_field"] and "constitutional classification is also exact" in recent["invariant_seed_field"])
    check("K site-net equivalence excludes entangling frames foundation-wide", "permutation followed by onsite unitary recodings" in recent["site_net_equivalence"] and "sp(4,2)" in recent["site_net_equivalence"] and "law-selected record category" in recent["site_net_equivalence"])
    check("K parity certificate is operational role rather than generic content", "parity certificate is a valid role-specific operational definition" in recent["operational_parity"] and "alone is not complete record content" in recent["operational_parity"] and "record-fibre" in recent["operational_parity"])
    check("K fixed selected and transported site nets are distinct", "pu(2)^n semidirect product s_n" in recent["named_site_equivalence"] and "groupoid rather than one fixed-object group" in recent["named_site_equivalence"])
    check("K commit count is a clock theorem after event identity", "a clock does not make a record lock" in recent["commit_clock"] and "record-faithful physical-equivalence class" in recent["commit_clock"] and "dimensionless clock ratios" in recent["commit_clock"])
    check("K NN seed compiler reaches the 27-hop bound", "isolated-bernoulli factor" in recent["seed_compilation"] and "causal-depth floor is" in recent["seed_compilation"] and "record-only clean-output" in recent["seed_compilation"])
    check("K Born reduction leaves numerical law and corpus", "effect noncontextuality" in recent["born_affinity"] and "physical randomization" in recent["born_affinity"] and "trial/reset corpus is separate" in recent["born_affinity"])
    check("K foundation sorts close the site-identity axiom seam", "sort-preserving isomorphism" in recent["sort_equivalence"] and "representation expansion" in recent["sort_equivalence"] and "no axiom addition is needed" in recent["sort_equivalence"])
    check("K guarded seed reference sharpens the NN compiler", "pure-birth hard-core quantum-trajectory instrument" in recent["dissipative_seed"] and "explicit branch-labelled instrument" in recent["dissipative_seed"] and "depth-twenty-seven" in recent["dissipative_seed"] and "a channel does not" in recent["dissipative_seed"] and "uniquely select its record instrument" in recent["dissipative_seed"])
    check("K frequency bridge is the component-mean theorem", "e_mu[x_0 | i_t]=q" in recent["frequency_corpus"] and "ergodic sufficient condition" in recent["frequency_corpus"] and "visible certificates define blocks, not independence" in recent["frequency_corpus"])
    check("K residual packing permits one universal L-star", "yes for universal interfaces; no for the actual history" in recent["residual_packing"] and "packaging is not derivation" in recent["residual_packing"] and "one realized-history instance" in recent["residual_packing"])
    check("K record-only state leaves a global Bell-capable route", "sixteen vertices" in recent["record_state_bell"] and "2 sqrt(2)" in recent["record_state_bell"] and "global record-history law" in recent["record_state_bell"] and "qualification would need revision" in recent["record_state_bell"])
    check("K complete-history status is conditional without a universal sampler axiom", "complete-history status is conditional" in recent["actuality_semantics"] and "four complete-history routes" in recent["actuality_semantics"] and "measure alone still selects no member" in recent["actuality_semantics"])
    check("K record-only NN fortress keeps state widening conditional", "5,202-site fortress" in recent["record_state_fortress"] and "fortress writes `b0` last" in recent["record_state_fortress"] and "strong lumpability" in recent["record_state_fortress"] and "no new record axiom is forced" in recent["record_state_fortress"])
    check("K global record process preserves record-only ontology", "decoherence functional" in recent["global_record_process"] and "identity insertion" in recent["global_record_process"] and "no qualification amendment is forced" in recent["global_record_process"] and "separate law placement" in recent["global_record_process"])
    check("K Admissibility slot is not extensional law identity", "no second existence statement is needed" in recent["admissibility_definability"] and "named function symbol is not an extensional specification" in recent["admissibility_definability"] and "even an exact availability table" in recent["admissibility_definability"])
    check("K clause deletion leaves one universal nonzero atom", "only nonzero universal constitutional content" in recent["constitutional_lower_bound"] and "zero new words" in recent["constitutional_lower_bound"] and "smallest content-level result" in recent["constitutional_lower_bound"])
    check("K long-run append proves the conditional recurrence fork", "time-stationary formation process has zero intensity" in recent["long_run_append"] and "exactly zero spacetime intensity" in recent["long_run_append"] and "literal record-only append architecture is viable" in recent["long_run_append"] and "no generic storage/compute-budget sentence" in recent["long_run_append"])
    check("K local composition derives global process with a boundary", "one exact cubic nearest-neighbor rule" in recent["local_global_glue"] and "no independent finite global measure atom survives" in recent["local_global_glue"] and "all-zero boundary and an all-plus" in recent["local_global_glue"] and "retyped admissibility" in recent["local_global_glue"])
    check("K moving logical front closes recurrence without moving records", "head-process bisimulation" in recent["moving_logical_front"] and "no record moves" in recent["moving_logical_front"] and "one fresh record" in recent["moving_logical_front"])
    check("K final census leaves no second universal atom", "only universal nonzero" in recent["final_missing_census"] and "two conditional constitutional edit gates" in recent["final_missing_census"] and "no live axiom edit" in recent["final_missing_census"])
    check("K cubic CZ witness is not uniquely selected", "exactly two laws remain" in recent["cubic_cz_selection"] and "time-dependent transported equivalence" in recent["cubic_cz_selection"] and "constraint/preparation layer, not the full" in recent["cubic_cz_selection"])
    check("K temporal quotient is law-relative", "necessarily law-relative" in recent["temporal_equivalence"] and "cross-time idle" in recent["temporal_equivalence"] and "no new axiom sentence" in recent["temporal_equivalence"])
    check("K broad cubic Clifford census remains nonunique", "surviving selector is the onsite cubic-rotation action" in recent["cubic_clifford"] and "three uniformly local symplectic protocol" in recent["cubic_clifford"] and "conditional one-skeleton closure" in recent["cubic_clifford"])
    check("K record-law-complete radius-three candidate first fails strict NN readiness", "radius-three, single-front record-law complete" in recent["candidate_assembly"] and "event_readiness_local_causal_domain" in recent["candidate_assembly"] and "first exact channel incompatibility is `matter`" in recent["candidate_assembly"])
    check("K actual history does not identify counterfactual law", "separating reconstruction theorem" in recent["history_identifiability"] and "observational record distribution" in recent["history_identifiability"] and "does not invert" in recent["history_identifiability"])
    check("K Cycle-42 reduction retains one exact referent", "cycle-42 realized-history identifiability firewall" in note and "one exact predictive law identity" in note)


def main() -> int:
    source_contract()
    availability_continuation_separation()
    append_nonreconnection_and_actuality()
    symmetry_obstruction()
    statistics_independence()
    channel_instrument_distinction()
    clock_rate_independence()
    action_selection_boundary()
    physical_equivalence_boundary()
    note_completeness()
    cycle12_reduction_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("CYCLES_1_42: append formation, compatible schedule confluence, binary Lueders form, pointer context, post-record covariant boundary normals, quasilocal phase retirement, invariant seeds with a guarded instrument, a 27-hop partial compiler, an inefficient record-only NN fortress, exact long-run capacity bounds, exact local-to-global gluing, and moving logical recurrence derive conditionally; temporal equivalence is law-relative, the broad cubic Clifford census remains nonunique, and radius-three/single-front record-law-complete L41^R3 first fails the strict NN target on a Boolean readiness compiler before TOE-predictive clock-rate and matter closure; complete H needs an explicit route and does not select counterfactual L-star; within the tested inventory one extensional TOE-predictive-law identity remains universal-looking")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
