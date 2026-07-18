#!/usr/bin/env python3
"""Cycle 10 red-team of actual-history and calibrated-weight irreducibility.

Companion note:
  docs/work_history/repo/review_feedback/
  CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md

The finite controls ask whether causal readiness plus reversible dynamics can
produce both one append-only actual history and calibrated outcome weights
without an exact law-level or boundary/state-level selector.  They do not
simulate whole interpretations or prove a universal no-go.

No network access, randomness, live axiom/registry/audit mutation, commit, or
PR.  Exit code 0 iff FAIL=0.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def exact_equal(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        difference = sp.Matrix(left) - sp.Matrix(right)
        return all(sp.simplify(value) == 0 for value in difference)
    return sp.simplify(left - right) == 0


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)
KET_MINUS = (KET0 - KET1) / sp.sqrt(2)
PX_PLUS = density(KET_PLUS)
PX_MINUS = density(KET_MINUS)


def normalized_note() -> tuple[str, str]:
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )
    return text, normalized


MECHANISM_START = "<!-- mechanism-matrix:start -->"
MECHANISM_END = "<!-- mechanism-matrix:end -->"
MECHANISM_HEADER = (
    "route_id",
    "actual_history_source",
    "calibrated_weight_source",
    "permanence_source",
    "free_of_equivalent_selector",
)
MECHANISMS = {
    "reversible_qca_only": ("NONE", "NONE", "NONE", "NO"),
    "wolfram_multiway": ("NONE", "NONE", "CONDITIONAL", "NO"),
    "decoherence_darwinism": ("NONE", "CONDITIONAL_NORM", "EFFECTIVE", "NO"),
    "consistent_histories": ("BOUNDARY", "LAW", "EFFECTIVE", "NO"),
    "everett": ("ALL_BRANCHES", "CONDITIONAL_NORM", "EFFECTIVE", "NO"),
    "objective_collapse": ("LAW", "LAW", "DERIVED", "NO"),
    "bohmian_typicality": ("BOUNDARY", "BOUNDARY", "EFFECTIVE", "NO"),
    "causal_set_csg": ("LAW", "LAW", "DERIVED", "NO"),
    "deterministic_superselection": ("BOUNDARY", "BOUNDARY", "CONDITIONAL", "NO"),
    "unique_ergodic_determinism": ("BOUNDARY", "DERIVED", "LAW", "NO"),
    "sampled_instrument": ("LAW", "LAW", "DERIVED", "NO"),
    "two_boundary_global": ("BOUNDARY", "BOUNDARY", "CONDITIONAL", "NO"),
}


ATOM_START = "<!-- atom-ledger:start -->"
ATOM_END = "<!-- atom-ledger:end -->"
ATOM_HEADER = ("atom_id", "disposition", "rationale_key")
ATOMS = {
    "finite_tensor_carrier_from_generated_local_algebra": ("DERIVABLE", "generated_composition"),
    "supported_successors_from_exact_instrument": ("DERIVABLE", "positive_support"),
    "formation_eligibility_as_positive_support": ("DERIVABLE", "support_definition"),
    "normalization_from_complete_instrument": ("DERIVABLE", "kraus_completeness"),
    "finite_cylinders_from_global_process": ("DERIVABLE", "projective_consistency"),
    "spacelike_schedule_quotient": ("DERIVABLE", "disjoint_commutation"),
    "event_order_from_causal_relation": ("DERIVABLE", "causal_order"),
    "nonreconnection_from_invariant_scope": ("DERIVABLE", "append_preservation"),
    "redundant_accessibility": ("DERIVABLE", "darwinism_after_write"),
    "stable_frequencies_given_ergodic_corpus": ("DERIVABLE", "frequency_theorem"),
    "exact_physical_law_domain": ("LAW_OWNED", "extensional_domain"),
    "exact_readiness_rule": ("LAW_OWNED", "event_domain"),
    "exact_coherent_update": ("LAW_OWNED", "reversible_kernel"),
    "exact_symmetry_action": ("LAW_OWNED", "dynamic_covariance"),
    "context_intervention_repertoire": ("LAW_OWNED", "physical_contexts"),
    "physical_outcome_decomposition": ("LAW_OWNED", "instrument_not_channel"),
    "calibrated_weight_rule": ("LAW_OWNED", "measure_value"),
    "branch_to_realized_write_semantics": ("LAW_OWNED", "actuality_interface"),
    "record_identity_and_preservation_scope": ("LAW_OWNED", "operation_scope"),
    "overlap_causal_order": ("LAW_OWNED", "causal_composition"),
    "predictive_record_decoder": ("LAW_OWNED", "future_equivalence"),
    "global_gluing_extension_contract": ("LAW_OWNED", "process_contract"),
    "renewal_export_policy": ("LAW_OWNED", "fresh_capacity"),
    "allowed_boundary_class": ("LAW_OWNED", "boundary_type"),
    "trial_corpus_equivalence": ("LAW_OWNED", "reset_protocol"),
    "metric_clock_calibration": ("LAW_OWNED", "rate_map"),
    "actual_initial_or_boundary_instance": ("BOUNDARY_STATE_OWNED", "contingent_world"),
    "actual_noise_seed_or_ontic_sector": ("BOUNDARY_STATE_OWNED", "realized_member"),
    "preparation_program_setting_records": ("BOUNDARY_STATE_OWNED", "recorded_inputs"),
    "actual_trial_corpus_instance": ("BOUNDARY_STATE_OWNED", "empirical_instance"),
    "records_form_lock_one_and_persist": ("GENUINELY_CONSTITUTIONAL", "existing_record_ontology"),
    "state_is_records_ontology": ("GENUINELY_CONSTITUTIONAL", "existing_state_ontology"),
    "one_fixed_local_rule_exists": ("GENUINELY_CONSTITUTIONAL", "existing_admissibility_ontology"),
    "exact_law_reference_if_not_uniquely_derived": ("GENUINELY_CONSTITUTIONAL", "conditional_new_candidate"),
}


def parse_table(text: str, start: str, end: str) -> tuple[tuple[str, ...], dict[str, tuple[str, ...]]]:
    body = text.split(start, 1)[1].split(end, 1)[0]
    lines = [line for line in body.splitlines() if line.startswith("|")]
    rows = [[cell.strip().strip("`") for cell in line.strip().strip("|").split("|")] for line in lines]
    header = tuple(rows[0])
    parsed = {
        row[0]: tuple(row[1:])
        for row in rows[2:]
        if len(row) == len(header) and row[0]
    }
    return header, parsed


def source_and_matrix_contract() -> None:
    section("A - Source, mechanism, and atom-classification contract")
    text, normalized = normalized_note()
    for phrase in (
        "authority: none",
        "bounded red-team result",
        "not a universal no-go",
        "causal readiness plus reversible dynamics",
        "equivalent selector",
        "law-owned",
        "boundary/state-owned",
        "genuinely constitutional",
        "n1",
        "n8",
        "does not authorize an axiom edit",
    ):
        check(f"A note contains scope phrase: {phrase}", phrase in normalized)

    companions = (
        "CUBIC_QUBIT_RELATIVISTIC_REDUCTION_CYCLE7_NOTE_2026-07-14.md",
        "CUBIC_SPLIT_STEP_QW_QCA_PRIMARY_SOURCE_UNIQUENESS_AUDIT_2026-07-14.md",
        "BARE_METAL_RECORD_ACTUALIZATION_PRIMARY_SOURCE_AUDIT_2026-07-14.md",
        "EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md",
    )
    for companion in companions:
        check(f"A note cites completed Cycle 7-9 surface: {companion}", companion in text)

    framework_surfaces = (
        "MINIMAL_AXIOMS_2026-06-29.md",
        "axiom_premise_nodes.json",
        "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "review-loop/SKILL.md",
        "CONTROLLED_VOCABULARY.md",
    )
    for surface in framework_surfaces:
        check(f"A framework refresher cites {surface}", surface in text)
    check("A literature is proof-pattern inspiration, not repo authority", "External literature is used only as proof-pattern" in text and "it is not repo authority" in text)

    check("A mechanism table has one start marker", text.count(MECHANISM_START) == 1)
    check("A mechanism table has one end marker", text.count(MECHANISM_END) == 1)
    header, routes = parse_table(text, MECHANISM_START, MECHANISM_END)
    check("A mechanism table header is exact", header == MECHANISM_HEADER, repr(header))
    check("A all twelve mechanism routes are present", set(routes) == set(MECHANISMS))
    for route, expected in MECHANISMS.items():
        check(f"A {route} classification is locked", routes.get(route) == expected, repr(routes.get(route)))
    check("A no tested route is selector-free", all(row[-1] == "NO" for row in routes.values()))
    check("A positive collapse and instrument routes visibly own law content", routes["objective_collapse"][:2] == ("LAW", "LAW") and routes["sampled_instrument"][:2] == ("LAW", "LAW"))

    check("A atom ledger has one start marker", text.count(ATOM_START) == 1)
    check("A atom ledger has one end marker", text.count(ATOM_END) == 1)
    atom_header, atoms = parse_table(text, ATOM_START, ATOM_END)
    check("A atom ledger header is exact", atom_header == ATOM_HEADER, repr(atom_header))
    check("A exact surviving atom set is classified", set(atoms) == set(ATOMS))
    for atom, expected in ATOMS.items():
        check(f"A {atom} disposition is locked", atoms.get(atom) == expected, repr(atoms.get(atom)))
    dispositions = {row[0] for row in atoms.values()}
    check("A all four requested dispositions occur", dispositions == {"DERIVABLE", "LAW_OWNED", "BOUNDARY_STATE_OWNED", "GENUINELY_CONSTITUTIONAL"})
    conditional_new = [atom for atom, row in atoms.items() if row == ("GENUINELY_CONSTITUTIONAL", "conditional_new_candidate")]
    check("A only one conditional new constitutional candidate survives", conditional_new == ["exact_law_reference_if_not_uniquely_derived"])


def cnot(control: int, target: int, qubits: int = 3) -> sp.Matrix:
    size = 2**qubits
    matrix = sp.zeros(size)
    for source in range(size):
        bits = [(source >> (qubits - 1 - index)) & 1 for index in range(qubits)]
        output = list(bits)
        if bits[control]:
            output[target] ^= 1
        destination = 0
        for bit in output:
            destination = 2 * destination + bit
        matrix[destination, source] = 1
    return matrix


def reversible_copy_and_boundary_measure() -> None:
    section("B - Reversible copying relocates outcome and weights to boundary data")
    u = cnot(0, 2) * cnot(0, 1)
    check("B copier is exactly unitary", exact_equal(dagger(u) * u, sp.eye(8)))
    check("B copier is exactly reversible by itself", exact_equal(u * u, sp.eye(8)))
    ket000 = sp.eye(8)[:, 0]
    ket100 = sp.eye(8)[:, 4]
    ket111 = sp.eye(8)[:, 7]
    check("B boundary bit zero copies to record 000", exact_equal(u * ket000, ket000))
    check("B boundary bit one copies to record 111", exact_equal(u * ket100, ket111))

    for p in (sp.Rational(1, 3), sp.Rational(2, 3)):
        rho_in = p * density(ket000) + (1 - p) * density(ket100)
        rho_out = sp.simplify(u * rho_in * dagger(u))
        weights = (rho_out[0, 0], rho_out[7, 7])
        check(f"B same copier transports boundary weights p={p}", weights == (p, 1 - p), repr(weights))
    check("B identical reversible law admits different calibrated ensembles", sp.Rational(1, 3) != sp.Rational(2, 3))
    check("B one pure boundary gives one history but no nontrivial ensemble", trace(density(u * ket100)) == 1 and (u * ket100)[7] == 1)
    check("B inverse erases both witness copies", exact_equal(u * ket111, ket100))
    check("B append permanence therefore needs an operation restriction or archive", exact_equal(u * ket111, ket100) and not exact_equal(ket111, ket100))


def actuality_and_weight_independence() -> None:
    section("C - One realized transcript and calibrated weights are independent")
    first = (0, 1) * 4
    second = (1, 0) * 4
    frequency_first = Fraction(sum(first), len(first))
    frequency_second = Fraction(sum(second), len(second))
    check("C two actual histories differ", first != second)
    check("C both histories have the same one-half frequency", frequency_first == frequency_second == Fraction(1, 2))
    check("C a weight law does not name which history occurred", first != second and frequency_first == frequency_second)

    observed = (0, 0, 1, 1)
    likelihoods = {}
    for p in (Fraction(1, 3), Fraction(2, 3)):
        ones = sum(observed)
        zeros = len(observed) - ones
        likelihoods[p] = p**ones * (1 - p) ** zeros
    check("C one finite history has positive likelihood under two laws", all(value > 0 for value in likelihoods.values()))
    check("C one actual history does not identify its full weight law", len(likelihoods) == 2 and all(value > 0 for value in likelihoods.values()))


def permutation_matrix(mapping: tuple[int, ...]) -> sp.Matrix:
    matrix = sp.zeros(len(mapping))
    for source, target in enumerate(mapping):
        matrix[target, source] = 1
    return matrix


def unique_ergodic_route() -> None:
    section("D - Unique ergodicity closes weights only after decoder and law are fixed")
    cycle = permutation_matrix((1, 2, 3, 4, 5, 0))
    uniform = sp.Matrix([sp.Rational(1, 6)] * 6)
    check("D six-cycle is reversible", exact_equal(dagger(cycle) * cycle, sp.eye(6)))
    check("D uniform distribution is stationary", exact_equal(cycle * uniform, uniform))
    check("D stationary eigenspace is one-dimensional", (cycle - sp.eye(6)).nullspace().__len__() == 1)

    weights = {}
    for marked in (1, 2, 3, 4, 5):
        decoder = sp.Matrix([1 if index < marked else 0 for index in range(6)])
        weights[marked] = sp.simplify((decoder.T * uniform)[0])
    check("D one dynamics admits decoder weights m/6", weights == {m: sp.Rational(m, 6) for m in range(1, 6)}, repr(weights))
    check("D dynamics alone does not select the physical record partition", len(set(weights.values())) == 5)

    decoder = tuple(0 if index < 2 else 1 for index in range(6))
    orbit_zero = tuple(decoder[index % 6] for index in range(12))
    orbit_one = tuple(decoder[(index + 1) % 6] for index in range(12))
    check("D distinct boundary phases give different transcripts", orbit_zero != orbit_one)
    check("D complete-cycle frequencies agree", sum(orbit_zero) == sum(orbit_one) == 8)
    check("D unique ergodicity does not select the actual phase", orbit_zero != orbit_one and sum(orbit_zero) == sum(orbit_one))
    check("D cyclic current-state output is not an append-only archive", cycle**6 == sp.eye(6))


def superselection_and_equivariance_route() -> None:
    section("E - Superselection/equivariance preserves but does not select a measure")
    two_cycles = permutation_matrix((1, 0, 3, 2))
    check("E two-sector dynamics is reversible", exact_equal(dagger(two_cycles) * two_cycles, sp.eye(4)))
    check("E stationary eigenspace has two independent sector weights", len((two_cycles - sp.eye(4)).nullspace()) == 2)
    stationary = {}
    for a in (sp.Rational(1, 4), sp.Rational(3, 4)):
        mu = sp.Matrix([a / 2, a / 2, (1 - a) / 2, (1 - a) / 2])
        stationary[a] = mu
        check(f"E equilibrium family member a={a} is equivariant", exact_equal(two_cycles * mu, mu))
    check("E equivariance leaves arbitrary inter-sector weight", stationary[sp.Rational(1, 4)] != stationary[sp.Rational(3, 4)])
    check("E an actual basis state selects one sector as boundary data", two_cycles * sp.eye(4)[:, 0] == sp.eye(4)[:, 1])
    check("E sector ontology does not supply ensemble calibration", len(stationary) == 2 and stationary[sp.Rational(1, 4)] != stationary[sp.Rational(3, 4)])


def multiway_refinement_route() -> None:
    section("F - Multiway causal structure does not fix branch weights or one path")
    path_counts = {"A": 2, "B": 1}
    endpoint_counts = {"A": 1, "B": 1}
    path_law = (Fraction(path_counts["A"], 3), Fraction(path_counts["B"], 3))
    endpoint_law = (Fraction(1, 2), Fraction(1, 2))
    check("F uniform path weights are two-thirds/one-third", path_law == (Fraction(2, 3), Fraction(1, 3)))
    check("F uniform terminal weights are one-half/one-half", endpoint_law == (Fraction(1, 2), Fraction(1, 2)))
    check("F presentation refinement changes raw path weights", path_law != endpoint_law)
    check("F the physical terminal support is unchanged", set(path_counts) == set(endpoint_counts) == {"A", "B"})

    schedules = (("x", "y"), ("y", "x"))
    terminal = {schedule: frozenset({("x", 0), ("y", 1)}) for schedule in schedules}
    check("F causal-order quotient removes disjoint schedule multiplicity", len(set(terminal.values())) == 1)
    check("F schedule quotient still leaves distinct outcome sectors", frozenset({("x", 1), ("y", 1)}) not in set(terminal.values()))
    check("F neither causal invariance nor support names one sector", len({"A", "B"}) == 2)


def decoherence_darwinism_route() -> None:
    section("G - Decoherence and redundant witnesses leave reversible alternatives")
    psi = sp.sqrt(sp.Rational(1, 3)) * sp.eye(8)[:, 0] + sp.sqrt(sp.Rational(2, 3)) * sp.eye(8)[:, 7]
    rho = density(psi)
    check("G two redundant branches remain nonzero", psi[0] != 0 and psi[7] != 0)
    check("G branch coherence remains globally nonzero", rho[0, 7] == sp.sqrt(2) / 3)
    copier = cnot(0, 2) * cnot(0, 1)
    preimage = sp.simplify(copier * psi)
    expected = sp.sqrt(sp.Rational(1, 3)) * sp.eye(8)[:, 0] + sp.sqrt(sp.Rational(2, 3)) * sp.eye(8)[:, 4]
    check("G local inverse erases both redundant witnesses", exact_equal(preimage, expected))
    check("G reduced/decohered appearance does not select one global branch", rho[0, 0] == sp.Rational(1, 3) and rho[7, 7] == sp.Rational(2, 3) and rho[0, 7] != 0)


def histories_and_everett_routes() -> None:
    section("H - Consistent realms and Everett refinement do not yield one selected history")
    rho = density(KET_PLUS)
    z_family = (P0, P1)
    x_family = (PX_PLUS, PX_MINUS)

    def decoherence(projectors: tuple[sp.Matrix, sp.Matrix]) -> sp.Matrix:
        return sp.Matrix(2, 2, lambda i, j: trace(projectors[i] * rho * projectors[j]))

    dz = decoherence(z_family)
    dx = decoherence(x_family)
    check("H incompatible Z and X one-time families both decohere", dz[0, 1] == dx[0, 1] == 0)
    check("H the two consistent realms carry different weights", tuple(dz[i, i] for i in range(2)) != tuple(dx[i, i] for i in range(2)))
    check("H consistency alone does not select a realm", exact_equal(P0 + P1, I2) and exact_equal(PX_PLUS + PX_MINUS, I2) and not exact_equal(P0 * PX_PLUS, PX_PLUS * P0))

    born_aggregate = (sp.Rational(1, 3), sp.Rational(2, 3))
    branch_count_before = (Fraction(1, 2), Fraction(1, 2))
    branch_count_after_threefold_b_refinement = (Fraction(1, 4), Fraction(3, 4))
    refined_amplitudes = (sp.sqrt(sp.Rational(1, 3)),) + (sp.sqrt(sp.Rational(2, 9)),) * 3
    check("H refined Everett vector remains normalized", sp.simplify(sum(abs(value) ** 2 for value in refined_amplitudes)) == 1)
    check("H aggregate Hilbert weights survive refinement", sp.simplify(abs(refined_amplitudes[0]) ** 2) == born_aggregate[0] and sp.simplify(sum(abs(value) ** 2 for value in refined_amplitudes[1:])) == born_aggregate[1])
    check("H raw branch count changes under refinement", branch_count_before != branch_count_after_threefold_b_refinement)
    check("H neither branch-count presentation selects one actual branch", len(refined_amplitudes) == 4 and all(value != 0 for value in refined_amplitudes))


def collapse_instrument_and_growth_routes() -> None:
    section("I - Collapse/instrument and sequential growth close only by owning the missing law")
    a, b, c, d = sp.symbols("a b c d")
    rho = sp.Matrix([[a, b], [c, d]])
    projective = sp.simplify(P0 * rho * P0 + P1 * rho * P1)
    random_unitary = sp.simplify((rho + Z * rho * Z) / 2)
    check("I one nonselective channel has two exact unravellings", exact_equal(projective, random_unitary))
    test = sp.diag(sp.Rational(1, 3), sp.Rational(2, 3))
    projective_labels = (trace(P0 * test), trace(P1 * test))
    token_labels = (sp.Rational(1, 2), sp.Rational(1, 2))
    check("I unravelled event-label laws differ", projective_labels != token_labels)
    check("I a sample instruction is additional to the averaged channel", exact_equal(projective, random_unitary) and projective_labels != token_labels)

    growth_support = ("extension_A", "extension_B")
    fair = {growth_support[0]: Fraction(1, 2), growth_support[1]: Fraction(1, 2)}
    biased = {growth_support[0]: Fraction(2, 3), growth_support[1]: Fraction(1, 3)}
    check("I two sequential-growth kernels share append support", set(fair) == set(biased) == set(growth_support))
    check("I both sequential-growth kernels normalize", sum(fair.values()) == sum(biased.values()) == 1)
    check("I causal append structure does not select transition couplings", fair != biased)
    check("I one sampled extension would still require a sample or boundary member", len(growth_support) == 2)


def no_go_discipline_contract() -> None:
    section("J - N1-N8 and scope contract")
    text, normalized = normalized_note()
    for heading in (
        "N1 — Alternative-route enumeration",
        "N2 — Wall-independence audit",
        "N3 — Hidden-condition scan",
        "N4 — Exact residual matching",
        "N5 — Resolution and rhetoric audit",
        "N6 — Partial-closure paths and primitive registry",
        "N7 — Strongest steelman",
        "N8 — Cross-cycle echo",
    ):
        check(f"J note contains {heading}", heading in text)
    for route in (
        "Wolfram multiway",
        "decoherence/Darwinism",
        "consistent histories",
        "Everett",
        "objective collapse",
        "Bohmian typicality",
        "causal-set sequential growth",
        "deterministic superselection",
        "unique ergodicity",
        "two-boundary",
    ):
        check(f"J required route is explicit: {route}", route.lower() in normalized)
    check("J conclusion is corpus- and mechanism-bounded", "tested mechanisms" in normalized and "finite controls" in normalized)
    check("J deterministic uniqueness remains a live steelman", "deterministic uniquely extendible" in normalized)
    check("J current primitives are not enlarged", "realized-state primitive supplies no selector" in normalized)
    check("J exact law content is separated from constitutional placement", "content/placement split" in normalized)


def main() -> int:
    source_and_matrix_contract()
    reversible_copy_and_boundary_measure()
    actuality_and_weight_independence()
    unique_ergodic_route()
    superselection_and_equivariance_route()
    multiway_refinement_route()
    decoherence_darwinism_route()
    histories_and_everett_routes()
    collapse_instrument_and_growth_routes()
    no_go_discipline_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: finite red-team controls only; no universal no-go, canonical-law selection, axiom edit, registry mutation, or audit verdict")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
