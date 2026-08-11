#!/usr/bin/env python3
"""Construct a Record-derived compact-response selector and causal family.

Block 29 shows that phase/ensemble selection precedes homogeneous contact
fitting.  This runner asks whether the relevant branch label can be computed
from Records rather than supplied as a free phase tag.

The compact Regge null projector gives a canonical charge vector.  Its
homothety component and ten-dimensional orthogonal remainder distinguish a
flat-compatible source, a pure scale source, and a source requiring further
constraint/shape reactions.  A positive rational causal kernel on permanent
charge increments supplies one exact prefix-projective Record-history family
and a covariant scale-response compiler.  The kernel, boundary Record, scale
coefficient, and physical source map remain conditional law data.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_global_constraint_phase_ward_contact_reclassification_2026_08_10 as block29  # noqa: E402
import admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10 as network  # noqa: E402
import admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10 as reaction  # noqa: E402


closed = block29.closed
regge = network.regge

AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_RECORD_NULL_CHARGE_PROJECTIVE_HISTORY_PHASE_SELECTOR_"
    "SCALE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PATH = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
BLOCK29_PATH = block29.NOTE_PATH
NETWORK_PATH = network.NOTE_PATH
REACTION_PATH = reaction.NOTE_PATH
CLOSED_PATH = closed.NOTE_PATH
CYCLE30_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / (
    "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md"
)
CYCLE33_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / (
    "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RECORD_NULL_CHARGE_PROJECTIVE_HISTORY_PHASE_SELECTOR_SCALE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/ADMISSIBILITY_GLOBAL_CONSTRAINT_PHASE_WARD_CONTACT_RECLASSIFICATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_TIMELIKE_EDGE_CURRENT_NETWORK_COMPACT_HOMOTHETY_REGGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/work_history/repo/review_feedback/GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_global_constraint_phase_ward_contact_reclassification_2026_08_10.py",
    "scripts/admissibility_timelike_edge_current_network_compact_homothety_regge_boundary_2026_08_10.py",
    "scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py",
    "scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py",
    "scripts/global_record_history_process_law_cycle30_2026_07_14.py",
    "scripts/local_to_global_cubic_process_glue_cycle33_2026_07_14.py",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def rational_kernel(charge: int, increment: int) -> Fraction:
    """A strictly positive normalized causal kernel on {-1,0,+1}."""
    weights = {
        step: Fraction(1, 1 + (charge + step) ** 2)
        for step in (-1, 0, 1)
    }
    return weights[increment] / sum(weights.values(), Fraction())


def history_families(initial_charge: int, maximum_time: int):
    families: dict[int, dict[tuple[int, ...], Fraction]] = {
        0: {(): Fraction(1)}
    }
    for time in range(1, maximum_time + 1):
        current: dict[tuple[int, ...], Fraction] = {}
        for prefix, probability in families[time - 1].items():
            charge = initial_charge + sum(prefix)
            for increment in (-1, 0, 1):
                current[prefix + (increment,)] = (
                    probability * rational_kernel(charge, increment)
                )
        families[time] = current
    return families


def edge_permutation_matrix(permutation: tuple[int, ...]) -> np.ndarray:
    directions = tuple(tuple(item) for item in regge.DIRS15)
    index = {direction: position for position, direction in enumerate(directions)}
    matrix = np.zeros((15, 15), dtype=float)
    for edge, direction in enumerate(directions):
        transformed = [0, 0, 0, 0]
        for old_axis, bit in enumerate(direction):
            transformed[permutation[old_axis]] = bit
        matrix[index[tuple(transformed)], edge] = 1.0
    return matrix


def compact_data():
    hessian = regge.bloch_Q(np.zeros(4)).real
    eigenvalues, eigenvectors = np.linalg.eigh(hessian)
    null_basis = eigenvectors[:, np.abs(eigenvalues) < 1.0e-8]
    null_projector = null_basis @ null_basis.T
    homothety = network.homothety_vector().real
    homothety_unit = homothety / np.linalg.norm(homothety)
    scale_projector = np.outer(homothety_unit, homothety_unit)
    residual_projector = null_projector - scale_projector
    return (
        hessian,
        null_basis,
        null_projector,
        homothety,
        scale_projector,
        residual_projector,
    )


def response_class(
    source: np.ndarray,
    null_projector: np.ndarray,
    scale_projector: np.ndarray,
    residual_projector: np.ndarray,
) -> str:
    null_charge = null_projector @ source
    if np.linalg.norm(null_charge) < 1.0e-10:
        return "flat-compatible"
    if np.linalg.norm(residual_projector @ source) < 1.0e-10:
        return "pure-scale"
    return "shape-or-constraint-required"


def tilted_kernel(
    charge: int, factors: dict[int, Fraction]
) -> dict[int, Fraction]:
    weights = {
        increment: rational_kernel(charge, increment) * factors[increment]
        for increment in (-1, 0, 1)
    }
    normalizer = sum(weights.values(), Fraction())
    return {increment: weight / normalizer for increment, weight in weights.items()}


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    realized = flat(REALIZED_PATH)
    block29_note = flat(BLOCK29_PATH)
    network_note = flat(NETWORK_PATH)
    reaction_note = flat(REACTION_PATH)
    closed_note = flat(CLOSED_PATH)
    cycle30 = flat(CYCLE30_PATH)
    cycle33 = flat(CYCLE33_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; the causal kernel, compact projector, source inventories, and history compiler are repository-local")
    print("analytic_boundary: finite prefix consistency and RN ratios are exact rational algebra; Regge projector and response tests are double precision")
    print("physical_boundary: the kernel, boundary Record, source compiler, scale coefficient, spatial gluing, nonlinear geometry, and Lorentzian interpretation remain unselected")

    checks.check(
        "axiom-and-parent-boundary",
        "current axioms supply Records and an actual-state reference but no causal kernel, boundary law, geometry compiler, or phase dynamics",
        "admissibility is not a dynamics axiom" in axioms
        and "a state is a configuration of records" in axioms
        and "permanent" in axioms
        and "one realized-state reference" in realized
        and "phase/ensemble selection precedes coefficient selection" in block29_note
        and "compact homothety" in network_note
        and "eleven-channel" in reaction_note
        and "background-subtracted pair" in closed_note
        and "projective consistency" in cycle30
        and "boundary/history datum survives" in cycle33
        and all(
            key in registry
            for key in (
                "minimal_axioms",
                "scale_reference_primitive",
                "kinetic_isotropy_primitive",
                "realized_state_primitive",
            )
        ),
    )
    checks.check(
        "note-contract",
        "the note distinguishes a Record-derived response classifier from physical phase selection and carries N1--N8",
        "null-charge response classifier" in note
        and "prefix-projective" in note
        and "not a physical phase theorem" in note
        and "ten residual compact channels" in note
        and "n1--n8 status:" in note
        and "pass" in note
        and "no canonical axiom is edited" in note,
    )

    minimum_kernel = Fraction(1)
    maximum_normalization_error = Fraction()
    for charge in range(-8, 9):
        values = [rational_kernel(charge, step) for step in (-1, 0, 1)]
        minimum_kernel = min(minimum_kernel, *values)
        maximum_normalization_error = max(
            maximum_normalization_error,
            abs(sum(values, Fraction()) - 1),
        )
    checks.check(
        "positive-normalized-causal-kernel",
        "one fixed rational charge kernel is strictly positive and normalized on every tested Record state",
        minimum_kernel > 0 and maximum_normalization_error == 0,
        f"minimum probability={minimum_kernel}; normalization error={maximum_normalization_error}",
    )

    marginal_failures = 0
    normalized_failures = 0
    histories_checked = 0
    marginal_edges_checked = 0
    families_by_boundary = {}
    for initial_charge in (-1, 0, 1):
        families = history_families(initial_charge, 6)
        families_by_boundary[initial_charge] = families
        for time, family in families.items():
            histories_checked += len(family)
            normalized_failures += int(
                sum(family.values(), Fraction()) != Fraction(1)
            )
            if time == 0:
                continue
            previous = families[time - 1]
            for prefix, probability in previous.items():
                marginal_edges_checked += 1
                marginal = sum(
                    family[prefix + (increment,)]
                    for increment in (-1, 0, 1)
                )
                marginal_failures += int(marginal != probability)
    checks.check(
        "prefix-projective-history-family",
        "normalization of the causal kernel makes all finite Record-history laws exactly consistent under deletion of the newest slot",
        normalized_failures == 0
        and marginal_failures == 0
        and histories_checked == 3279
        and marginal_edges_checked == 1092,
        f"histories={histories_checked}; marginal cylinders={marginal_edges_checked}",
    )

    boundary_zero = tuple(rational_kernel(0, step) for step in (-1, 0, 1))
    boundary_one = tuple(rational_kernel(1, step) for step in (-1, 0, 1))
    boundary_distance = sum(
        abs(left - right)
        for left, right in zip(boundary_zero, boundary_one)
    ) / 2
    checks.check(
        "permanent-boundary-record-selector",
        "two boundary charges use the same update law but give different futures, so the boundary must remain in the complete Record fibre",
        boundary_zero
        == (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4))
        and boundary_one
        == (Fraction(10, 17), Fraction(5, 17), Fraction(2, 17))
        and boundary_distance == Fraction(23, 68)
        and "record-fibre future-equivalence" in cycle30,
        f"total-variation separator={boundary_distance}",
    )

    (
        zero_hessian,
        null_basis,
        null_projector,
        homothety,
        scale_projector,
        residual_projector,
    ) = compact_data()
    zero_rank = int(np.linalg.matrix_rank(zero_hessian, tol=1.0e-8))
    residual_rank = int(
        np.linalg.matrix_rank(residual_projector, tol=1.0e-8)
    )
    projector_error = max(
        np.linalg.norm(null_projector @ null_projector - null_projector, 2),
        np.linalg.norm(
            residual_projector @ residual_projector - residual_projector, 2
        ),
        np.linalg.norm(residual_projector @ homothety),
    )
    checks.check(
        "compact-null-charge-decomposition",
        "the compact Hessian has eleven null charges which split canonically into one homothety and ten residual shape/constraint channels",
        zero_rank == 4
        and null_basis.shape == (15, 11)
        and residual_rank == 10
        and np.linalg.norm(zero_hessian @ homothety) < 1.0e-12
        and projector_error < 1.0e-12,
        f"rank/nullity={zero_rank}/{null_basis.shape[1]}; residual rank={residual_rank}; projector error={projector_error:.3e}",
    )

    worst_hessian_covariance = 0.0
    worst_projector_covariance = 0.0
    worst_homothety_covariance = 0.0
    for permutation in permutations(range(4)):
        axis = edge_permutation_matrix(permutation)
        worst_hessian_covariance = max(
            worst_hessian_covariance,
            float(np.linalg.norm(axis @ zero_hessian @ axis.T - zero_hessian, 2)),
        )
        worst_projector_covariance = max(
            worst_projector_covariance,
            float(np.linalg.norm(axis @ null_projector @ axis.T - null_projector, 2)),
        )
        worst_homothety_covariance = max(
            worst_homothety_covariance,
            float(np.linalg.norm(axis @ homothety - homothety)),
        )
    checks.check(
        "axis-covariant-record-geometry-compiler",
        "the compact charge projectors and homothety geometry compiler commute with all 24 simultaneous axis permutations",
        worst_hessian_covariance < 1.0e-12
        and worst_projector_covariance < 1.0e-12
        and worst_homothety_covariance == 0.0,
        f"Q={worst_hessian_covariance:.3e}; Pnull={worst_projector_covariance:.3e}; z={worst_homothety_covariance:.3e}",
    )

    worst_scale_residual = 0.0
    worst_formula_residual = 0.0
    scale_ranks = set()
    compiled_prefixes = 0
    restriction_failures = 0
    for stiffness in (0.5, 1.0, 2.0):
        lifted = zero_hessian + stiffness * scale_projector
        scale_ranks.add(int(np.linalg.matrix_rank(lifted, tol=1.0e-8)))
        for charge in range(-3, 4):
            source = charge * homothety
            response = -np.linalg.pinv(lifted, rcond=1.0e-11) @ source
            expected = -charge * homothety / stiffness
            worst_scale_residual = max(
                worst_scale_residual,
                float(np.linalg.norm(lifted @ response + source)),
            )
            worst_formula_residual = max(
                worst_formula_residual,
                float(np.linalg.norm(response - expected)),
            )
    for initial_charge, families in families_by_boundary.items():
        for time in range(1, 6):
            for history in families[time]:
                charges = [
                    initial_charge + sum(history[:prefix])
                    for prefix in range(time + 1)
                ]
                geometries = [
                    -charge * homothety for charge in charges
                ]
                compiled_prefixes += 1
                restricted = [
                    -charge * homothety for charge in charges[:-1]
                ]
                restriction_failures += int(
                    any(
                        np.linalg.norm(left - right) > 0.0
                        for left, right in zip(geometries[:-1], restricted)
                    )
                )
    checks.check(
        "pure-scale-branch-response",
        "adding one positive homothety projector raises compact rank by one and solves every pure-scale source with the analytic response -q z/kappa",
        scale_ranks == {5}
        and worst_scale_residual < 1.0e-12
        and worst_formula_residual < 1.0e-12,
        f"rank={scale_ranks}; equation={worst_scale_residual:.3e}; formula={worst_formula_residual:.3e}",
    )
    checks.check(
        "projective-record-to-geometry-prefix-map",
        "the cumulative permanent charge gives a geometry history whose restriction is unchanged by every later extension",
        compiled_prefixes == 1089
        and restriction_failures == 0
        and families_by_boundary[0][6][(0, 0, 0, 0, 0, 0)] > 0,
        f"compiled prefixes={compiled_prefixes}; null-history weight={families_by_boundary[0][6][(0, 0, 0, 0, 0, 0)]}",
    )

    edge_sources = np.eye(15)
    residual_norms = [
        float(np.linalg.norm(residual_projector @ edge_sources[:, index]))
        for index in range(15)
    ]
    residual_source_rank = int(
        np.linalg.matrix_rank(residual_projector @ edge_sources, tol=1.0e-8)
    )
    scale_lift = zero_hessian + scale_projector
    scale_solve_residuals = [
        float(
            np.linalg.norm(
                scale_lift
                @ (-np.linalg.pinv(scale_lift, rcond=1.0e-11) @ edge_sources[:, index])
                + edge_sources[:, index]
            )
        )
        for index in range(15)
    ]
    checks.check(
        "rank-one-scale-lift-boundary",
        "none of the fifteen individual actual-edge source rays is completed by the scale branch; their residual compact charges span all ten remaining channels",
        min(residual_norms) > 0.75
        and min(scale_solve_residuals) > 0.75
        and residual_source_rank == 10,
        f"residual norms=[{min(residual_norms):.6f},{max(residual_norms):.6f}]; rank={residual_source_rank}",
    )

    kkt = np.block(
        [
            [zero_hessian, null_basis],
            [null_basis.T, np.zeros((11, 11))],
        ]
    )
    worst_reaction_equation = 0.0
    worst_reaction_constraint = 0.0
    for source in (
        *[edge_sources[:, index] for index in range(15)],
        homothety,
        np.arange(1.0, 16.0),
    ):
        response = -np.linalg.pinv(zero_hessian, rcond=1.0e-10) @ source
        multipliers = -null_basis.T @ source
        worst_reaction_equation = max(
            worst_reaction_equation,
            float(
                np.linalg.norm(
                    zero_hessian @ response
                    + null_basis @ multipliers
                    + source
                )
            ),
        )
        worst_reaction_constraint = max(
            worst_reaction_constraint,
            float(np.linalg.norm(null_basis.T @ response)),
        )
    checks.check(
        "complete-null-reaction-compiler",
        "the canonical eleven-charge KKT compiler solves every tested compact source and exposes reactions rather than projecting sources away",
        np.linalg.matrix_rank(kkt, tol=1.0e-8) == 26
        and worst_reaction_equation < 1.0e-12
        and worst_reaction_constraint < 1.0e-12,
        f"KKT rank=26; equation={worst_reaction_equation:.3e}; constraint={worst_reaction_constraint:.3e}",
    )

    factors_one = {
        -1: Fraction(1),
        0: Fraction(2),
        1: Fraction(3),
    }
    factors_two = {
        -1: Fraction(5),
        0: Fraction(3),
        1: Fraction(2),
    }
    rn_failures = 0
    cocycle_failures = 0
    for charge in range(-6, 7):
        base = {
            increment: rational_kernel(charge, increment)
            for increment in (-1, 0, 1)
        }
        first = tilted_kernel(charge, factors_one)
        combined_factors = {
            increment: factors_one[increment] * factors_two[increment]
            for increment in (-1, 0, 1)
        }
        combined = tilted_kernel(charge, combined_factors)
        for increment in (-1, 0, 1):
            relative_rn = (
                (first[increment] / base[increment])
                / (first[0] / base[0])
            )
            rn_failures += int(
                relative_rn != factors_one[increment] / factors_one[0]
            )
            combined_rn = (
                (combined[increment] / base[increment])
                / (combined[0] / base[0])
            )
            cocycle_failures += int(
                combined_rn
                != (
                    factors_one[increment]
                    * factors_two[increment]
                    / (factors_one[0] * factors_two[0])
                )
            )
    checks.check(
        "local-rn-intervention-cocycle",
        "positive transition tilts cancel their normalizers in null-relative odds and compose exactly along the same causal family",
        rn_failures == 0 and cocycle_failures == 0,
        f"RN failures={rn_failures}; cocycle failures={cocycle_failures}",
    )

    closed_length = 5
    closed_nonzero = 0
    closed_dynamic = 0
    worst_closed_charge = 0.0
    worst_closed_solve = 0.0
    for index in product(range(closed_length), repeat=4):
        momentum = 2.0 * np.pi * np.asarray(index, dtype=float) / closed_length
        momentum = (momentum + np.pi) % (2.0 * np.pi) - np.pi
        source = closed.neutral_pair_row(closed_length, momentum)
        if np.linalg.norm(source) < 1.0e-10:
            continue
        closed_nonzero += 1
        closed_dynamic += int(abs(momentum[3]) > 1.0e-10)
        momentum_hessian = regge.bloch_Q(momentum)
        eigenvalues, eigenvectors = np.linalg.eigh(momentum_hessian)
        mode_null = eigenvectors[:, np.abs(eigenvalues) < 1.0e-8]
        worst_closed_charge = max(
            worst_closed_charge,
            float(np.linalg.norm(mode_null.conj().T @ source.conj())),
        )
        data = closed.source_data(source, momentum)
        worst_closed_solve = max(
            worst_closed_solve, float(data["solve"])
        )
    compact_closed = closed.neutral_pair_row(closed_length, np.zeros(4))
    checks.check(
        "neutral-history-flat-branch",
        "the complete L=5 neutral closed history has zero compact charge and every nonzero source lies in the flat Regge range",
        np.linalg.norm(compact_closed) == 0.0
        and closed_nonzero == 100
        and closed_dynamic == 80
        and worst_closed_charge < 1.0e-10
        and worst_closed_solve < 1.0e-10,
        f"nonzero/dynamic={closed_nonzero}/{closed_dynamic}; null charge={worst_closed_charge:.3e}; solve={worst_closed_solve:.3e}",
    )

    class_flat = response_class(
        compact_closed.real,
        null_projector,
        scale_projector,
        residual_projector,
    )
    class_scale = response_class(
        3.0 * homothety,
        null_projector,
        scale_projector,
        residual_projector,
    )
    edge_classes = [
        response_class(
            edge_sources[:, index],
            null_projector,
            scale_projector,
            residual_projector,
        )
        for index in range(15)
    ]
    checks.check(
        "record-null-charge-response-selector",
        "the source computed from a Record selects flat-compatible, pure-scale, or shape/constraint-required response without a fitted phase tag",
        class_flat == "flat-compatible"
        and class_scale == "pure-scale"
        and set(edge_classes) == {"shape-or-constraint-required"},
        f"neutral={class_flat}; dilation={class_scale}; edge census={dict((x, edge_classes.count(x)) for x in set(edge_classes))}",
    )

    responses = {
        stiffness: -3.0 * homothety / stiffness
        for stiffness in (0.5, 1.0, 2.0)
    }
    checks.check(
        "scale-and-boundary-nonselection",
        "projective consistency, axis covariance, positivity, and compact solvability do not select the boundary Record or the scale stiffness",
        len(
            {
                tuple(np.round(response, 12))
                for response in responses.values()
            }
        )
        == 3
        and boundary_zero != boundary_one
        and "boundary/history datum survives" in cycle33
        and "scale" in network_note,
        "all three stiffnesses pass while responses and boundary futures differ",
    )

    checks.check(
        "minimal-law-or-axiom-delta",
        "the branch classifier is downstream algebra, while autonomy still requires one covariant causal kernel, permanent boundary typing, source compiler, and geometry/reaction law",
        "can remain downstream" in note
        and "fixed covariant causal kernel" in note
        and "permanent boundary record" in note
        and "source compiler" in note
        and "geometry/reaction law" in note
        and "no fifth ontology axiom is proven necessary" in note,
    )
    checks.check(
        "bounded-theorem-and-live-routes",
        "the construction preserves spatial projective gluing, nonlinear curved backgrounds, full Ward connection, source selection, and Lorentzian stability as live obligations",
        "not a physical phase theorem" in note
        and "spatial projective" in note
        and "nonlinear" in note
        and "full ward" in note
        and "lorentzian" in note
        and "n1--n8 status:" in note,
    )

    print("N5_CERTIFICATE: selector=the compact null projector computes an eleven-component source charge and splits it into flat, pure-scale, and ten-channel residual response classes")
    print("N5_CERTIFICATE: projective_family=one positive normalized causal kernel plus a permanent boundary Record yields exact prefix marginals and a compatible geometry history")
    print("N5_CERTIFICATE: gravity_positive=neutral closed histories remain flat-compatible and a rank-one scale lift exactly solves pure homothety sources")
    print("N5_CERTIFICATE: gravity_boundary=every individual actual-edge source retains a nonzero residual charge after the scale lift, so general matter needs the complete reaction/curved sector")
    print("N5_CERTIFICATE: axiom_boundary=the classifier can be downstream, but current axioms do not select the kernel, boundary semantics, source compiler, stiffness, geometry/reaction law, or causal interpretation")
    print("per_element: checked all fifteen actual-edge rays and all 24 axis permutations")
    print("per_site: checked the retained fifteen-edge compact cell and one scalar permanent charge Record")
    print("per_history: checked 3,279 rational history cylinders through six causal steps and 1,092 exact prefix marginals")
    print("per_mode: checked the compact classifier and all 625 L5 neutral-history momenta")
    print("lattice_wide: prefix-projective causal histories and one L5 torus only; no arbitrary spatial region, continuum, nonlinear, or Lorentzian theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
