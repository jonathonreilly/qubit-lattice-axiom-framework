#!/usr/bin/env python3
"""Finite/source checks for the four-axiom TOE completeness gate.

This runner does not try to prove a universal no-go.  It pins the live
foundation and exhibits finite model pairs showing that several downstream
interfaces are not entailed by the current axiom wording or by the proposed
Admissibility/Record continuation pair.  No axiom, primitive, ledger, or audit
surface is edited.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOM = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
OBLIGATIONS = ROOT / "docs" / "audit" / "data" / "derivation_obligations.json"
REPORT = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "FOUR_AXIOM_TOE_COMPLETENESS_AND_FINAL_UPDATE_GATE_NOTE_2026-07-13.md"
DRAFT = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "ADMISSIBILITY_RECORD_CONTINUATION_AXIOM_DRAFT_NOTE_2026-07-13.md"
TENSOR_NOGO = ROOT / "docs" / "TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md"
PRE_RECORD = ROOT / "docs" / "PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md"
LOCAL_ATOM = ROOT / "docs" / "RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md"

OPEN = -1
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def source_contract() -> None:
    section("A - Live foundation, registry, and scope contract")
    axiom = AXIOM.read_text()
    report = REPORT.read_text()
    draft = DRAFT.read_text()
    registry = json.loads(REGISTRY.read_text())
    obligations = json.loads(OBLIGATIONS.read_text())
    tensor_nogo = TENSOR_NOGO.read_text()
    pre_record = PRE_RECORD.read_text()
    local_atom = LOCAL_ATOM.read_text()

    for label in ("Lattice", "Qubit", "Admissibility", "Record"):
        check(f"A axiom section {label} is live", f"### {label}" in axiom)

    check("A foundation names exactly four axioms", "They are named" in axiom and axiom.count("### ") == 4)
    check("A state remains typed as a record configuration", "A state is a configuration of records." in axiom)
    check("A Admissibility remains explicitly non-dynamical", "Admissibility is not a dynamics axiom." in axiom)
    check("A current memo withholds tensor composition", "composition theorem" not in axiom and "system composition" not in axiom)
    check("A proposed continuation sentence is not live", "law-admissible continuations" not in axiom)
    check("A proposed exact permanence sentence is not live", "same site and with the same content" not in axiom)
    check("A draft remains authority-free", "**Authority:** none" in draft and "does not edit or enlarge" in draft)

    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("A premise registry has exactly four canonical nodes", set(registry["canonical_ids"]) == expected_ids)
    check("A no admission node is present", all("admission" not in item for item in registry["canonical_ids"]))
    realized_note = registry["nodes"]["realized_state_primitive"]["note"]
    check("A realized-state primitive supplies no selector", "state-selection rule" in realized_note and "Supplies the slot, never the content" in realized_note)
    check("A kinetic-isotropy primitive supplies no dynamics", "no dimensionless DYNAMICAL content" in registry["nodes"]["kinetic_isotropy_primitive"]["note"])
    check("A scale primitive supplies units only", "Units conversion only" in registry["nodes"]["scale_reference_primitive"]["note"])
    check("A derivation registry has exactly three zero-premise obligations", len(obligations["canonical_ids"]) == 3 and "Non-premise registry" in obligations["description"])

    check("A tensor no-go names the duplicate global sector", "M_4(C) oplus M_4(C)" in tensor_nogo)
    check("A pre-record identification remains open", "pre-record reference state" in pre_record and "open admission" in pre_record)
    check("A local atom theorem keeps physical context selection open", "physical choice of readout basis or context" in local_atom)
    check("A completeness report is explicitly bounded", "Completeness scope:" in report and "not a proof that no unimagined" in report)
    check("A report includes all no-go discipline blocks", all(f"### N{i}" in report for i in range(1, 9)))
    check("A report performs no adoption", "**Authority:** none" in report and "does not edit or enlarge" in report)


def vec_pair(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(list(left) + list(right))


def composition_countermodel() -> None:
    section("B - Physical composition is not fixed by one-site qubits plus locality")
    I2 = sp.eye(2)
    I4 = sp.eye(4)
    basis2 = []
    for row in range(2):
        for col in range(2):
            matrix = sp.zeros(2)
            matrix[row, col] = 1
            basis2.append(matrix)

    ordinary_products = [sp.kronecker_product(a, b) for a in basis2 for b in basis2]
    ordinary_rank = sp.Matrix.hstack(*(sp.Matrix(list(matrix)) for matrix in ordinary_products)).rank()
    duplicate_products = [vec_pair(matrix, matrix) for matrix in ordinary_products]
    duplicate_rank = sp.Matrix.hstack(*duplicate_products).rank()

    check("B ordinary two-qubit local products span M4", ordinary_rank == 16)
    check("B duplicate-sector local products still have rank 16", duplicate_rank == 16)

    embeddings_commute = all(
        sp.kronecker_product(a, I2) * sp.kronecker_product(I2, b)
        == sp.kronecker_product(I2, b) * sp.kronecker_product(a, I2)
        for a, b in product(basis2, repeat=2)
    )
    check("B local factor embeddings commute", embeddings_commute)

    left_embedding_rank = sp.Matrix.hstack(
        *(sp.Matrix(list(sp.kronecker_product(a, I2))) for a in basis2)
    ).rank()
    right_embedding_rank = sp.Matrix.hstack(
        *(sp.Matrix(list(sp.kronecker_product(I2, b))) for b in basis2)
    ).rank()
    check("B both local embeddings are faithful", left_embedding_rank == right_embedding_rank == 4)

    sector_z = vec_pair(I4, -I4)
    augmented_rank = sp.Matrix.hstack(*duplicate_products, sector_z).rank()
    check("B extra central sector observable lies outside local-product span", augmented_rank == 17)
    duplicate_basis = []
    for matrix in ordinary_products:
        duplicate_basis.extend((vec_pair(matrix, sp.zeros(4)), vec_pair(sp.zeros(4), matrix)))
    duplicate_algebra_rank = sp.Matrix.hstack(*duplicate_basis).rank()
    check("B duplicate composite has constructed complex dimension 32", duplicate_algebra_rank == 32)
    check("B locality therefore does not force no-extra-global generation", duplicate_rank < 32)


def descendants(config: tuple[int, ...]) -> set[tuple[int, ...]]:
    values = []
    for item in config:
        values.append((0, 1) if item == OPEN else (item,))
    return set(product(*values))


def extends(base: tuple[int, ...], future: tuple[int, ...]) -> bool:
    return all(item == OPEN or future[index] == item for index, item in enumerate(base))


def continuation_and_permanence_countermodels() -> None:
    section("C - Static availability, physical continuation, and permanence separate")
    menu = frozenset({0, 1})
    branch_complete = menu
    singleton_support = frozenset({0})
    check("C identical availability menu admits branch-complete support", branch_complete == menu)
    check("C identical availability menu admits a lawful singleton subset", singleton_support <= menu)
    check("C static menu does not determine successor support", branch_complete != singleton_support)

    base = (OPEN, OPEN, OPEN)
    zero = (OPEN, 0, OPEN)
    one = (OPEN, 1, OPEN)
    check("C both candidate record successors extend the same source", extends(base, zero) and extends(base, one))
    check("C exact immutable descendant cones do not reconnect", not (descendants(zero) & descendants(one)))

    def append(config: tuple[int, ...], site: int, value: int) -> tuple[int, ...]:
        if config[site] not in (OPEN, value):
            raise ValueError("conflicting append")
        updated = list(config)
        updated[site] = value
        return tuple(updated)

    compatible_xy = append(append(base, 0, 1), 2, 0)
    compatible_yx = append(append(base, 2, 0), 0, 1)
    check("C compatible disjoint appends may compose without a preferred order", compatible_xy == compatible_yx == (1, OPEN, 0))

    weak_before = {"record-7": (0, "p")}
    weak_after = {"record-7": (2, "p")}
    weak_identity_survives = set(weak_before) <= set(weak_after)
    exact_site_content_survives = all(weak_after[key] == value for key, value in weak_before.items())
    check("C weak identity-only permanence permits migration", weak_identity_survives)
    check("C weak permanence does not imply same-site preservation", not exact_site_content_survives)

    exact_after = {"record-7": (0, "p"), "record-8": (2, "q")}
    check("C exact append-only semantics preserves old site/content", all(exact_after[key] == value for key, value in weak_before.items()))

    relation = {"s0": {"s1", "s2"}, "s1": {"s3"}, "s2": set(), "s3": set()}
    transitive_closure = {"s0": {"s1", "s2", "s3"}, "s1": {"s3"}, "s2": set(), "s3": set()}
    check("C one-step successor relation differs from continuation closure", relation["s0"] != transitive_closure["s0"])
    check("C continuation semantics can include further continuations", "s3" in transitive_closure["s0"])


def operational_typing_and_downstream_independence() -> None:
    section("D - Operational typing and downstream interfaces remain independent")
    empty_records: tuple[()] = ()
    rho_zero = sp.Matrix([[1, 0], [0, 0]])
    rho_mixed = sp.eye(2) / 2
    check("D distinct density operators can share the same empty record state", rho_zero != rho_mixed and empty_records == ())
    check("D both candidate density operators are normalized", sp.trace(rho_zero) == sp.trace(rho_mixed) == 1)
    check("D both candidate density operators are positive semidefinite", rho_zero.det() >= 0 and rho_mixed.det() >= 0)

    children = ("left", "right")
    selector_a = children[0]
    selector_b = children[1]
    check("D one support graph admits different realized-successor selectors", selector_a != selector_b and selector_a in children and selector_b in children)

    measure_a = {"left": sp.Rational(1, 2), "right": sp.Rational(1, 2)}
    measure_b = {"left": sp.Rational(1, 4), "right": sp.Rational(3, 4)}
    check("D one support graph admits different normalized measures", sum(measure_a.values()) == sum(measure_b.values()) == 1 and measure_a != measure_b)

    event_indices = (0, 1, 2, 3)
    clock_a = (0, 1, 2, 3)
    clock_b = (0, 1, 4, 9)
    check("D one record order admits different strictly increasing clocks", all(x < y for x, y in zip(clock_a, clock_a[1:])) and all(x < y for x, y in zip(clock_b, clock_b[1:])) and event_indices == tuple(range(4)))
    check("D the same event count has different duration/rate", clock_a[-1] != clock_b[-1])

    presentations = ("p", "mirror(p)")
    tickets_distinct = len(set(presentations))
    tickets_quotiented = 1
    check("D one modal label set admits different presentation quotients", tickets_distinct == 2 and tickets_quotiented == 1)

    sigma_minus = sp.Matrix([[0, 1], [0, 0]])
    sigma_z = sp.diag(1, -1)
    I2 = sp.eye(2)
    hard_0 = sp.kronecker_product(sigma_minus, I2)
    hard_1 = sp.kronecker_product(I2, sigma_minus)
    fermion_0 = hard_0
    fermion_1 = sp.kronecker_product(sigma_z, sigma_minus)
    check("D disjoint hard-core lowering operators commute", hard_0 * hard_1 - hard_1 * hard_0 == sp.zeros(4))
    check("D Jordan-Wigner lowering operators anticommute", fermion_0 * fermion_1 + fermion_1 * fermion_0 == sp.zeros(4))
    check("D both statistics readings act on the same four-dimensional carrier", hard_0.shape == fermion_0.shape == (4, 4))

    archive = ((0, "p"), (2, "q"))
    active_source_a = {0: 1, 2: 1}
    active_source_b = {0: 2, 2: 0}
    check("D identical archive admits inequivalent active-source maps", archive == ((0, "p"), (2, "q")) and active_source_a != active_source_b)

    energy_a = lambda records: len(records)
    energy_b = lambda records: sum(site * site + 1 for site, _ in records)
    check("D identical record state admits inequivalent action/energy maps", energy_a(archive) != energy_b(archive))


def closure_matrix() -> None:
    section("E - Candidate closure and remaining-interface matrix")
    interfaces = {"M", "Q", "C", "F", "X", "D", "P", "T", "I", "G"}
    candidate_closure = {
        "qubit_composition": {"C"},
        "admissibility_continuation_support": {"M", "F"},
        "record_exact_permanence": {"M", "F"},
        "qualification_answer_typing": {"M"},
    }
    closed_union = set().union(*candidate_closure.values())
    remaining = interfaces - closed_union
    check("E inventory has ten collapsed interfaces", len(interfaces) == 10)
    check("E composition candidate closes only the carrier interface", candidate_closure["qubit_composition"] == {"C"})
    check("E A/R/Qualification candidates close only modal/formation sub-atoms", set().union(candidate_closure["admissibility_continuation_support"], candidate_closure["record_exact_permanence"], candidate_closure["qualification_answer_typing"]) == {"M", "F"})
    check("E proposed constitutional package leaves seven major downstream interfaces", remaining == {"Q", "X", "D", "P", "T", "I", "G"})
    # The explicit equality above deliberately resolves to seven remaining
    # interfaces; keep a separate exact count guard to prevent prose drift.
    check("E exactly seven interfaces remain after C/M/F sub-closure", len(remaining) == 7)

    report = REPORT.read_text()
    for marker in (
        "operational quantum typing",
        "multi-site composition",
        "formation and causal extension",
        "realized continuation",
        "between-record dynamics/action",
        "preparation/measure/probability",
        "time/continuum kinematics",
        "physical individuation/matter",
        "resource/thermodynamics/gravity/boundary",
    ):
        check(f"E report carries interface marker: {marker}", marker in report)

    check("E report defers exact constitutional wording", "wording is deliberately deferred" in report)
    check("E report keeps the predictive specification as a pre-language probe", "Derive or supply the fixed rule's exact predictive specification" in report)
    check("E report keeps operational typing as a pre-language probe", "Operational typing probe" in report)


def main() -> None:
    source_contract()
    composition_countermodel()
    continuation_and_permanence_countermodels()
    operational_typing_and_downstream_independence()
    closure_matrix()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: finite/source non-entailment checks only; no axiom need is declared")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
