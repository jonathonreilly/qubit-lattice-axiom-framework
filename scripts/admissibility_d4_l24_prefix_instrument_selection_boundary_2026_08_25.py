#!/usr/bin/env python3
"""Block 195: L24 prefix-instrument selection boundary.

The campaign preregistered the normalized prefix law as a dependency gate.
This runner first verifies the exact Block-194 one-shot Lueders instrument,
then tests two action/cut-native translation constructions and the nearest-
slice covariance predictor.  Finally, conditional on designating its exact
Clifford lift as a CP subchannel, it constructs two inequivalent exact CPTP
completions.  It does not evaluate a
TT source response or open a held-out point.
"""

from __future__ import annotations

import argparse
from functools import cache
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192  # noqa: E402
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_L24_PREFIX_INSTRUMENT_SELECTION_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "6eeae12de0ec1f8263dfef39a0b021581b82a070"
PREREG_COMMIT = "28804ebe9eff1f2a86ea5bf9e7d4b96b40cf149a"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
AUDIT_TIMEOUT_SEC = 240

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_L24_PREFIX_INSTRUMENT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.txt",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.txt",
)

MUTATIONS = (
    "stale_main_authority",
    "break_lueders_completeness",
    "claim_shift_graph_invariant",
    "claim_shift_contractive",
    "claim_projected_shift_selfadjoint",
    "claim_projected_shift_semigroup",
    "claim_predictor_unitary",
    "claim_unique_cp_completion",
    "claim_equal_cylinder_laws",
    "open_tt_response",
    "claim_broad_time_no_go",
    "claim_axiom_update",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "stale_main_authority": "A",
    "break_lueders_completeness": "B",
    "claim_shift_graph_invariant": "C",
    "claim_shift_contractive": "C",
    "claim_projected_shift_selfadjoint": "D",
    "claim_projected_shift_semigroup": "D",
    "claim_predictor_unitary": "E",
    "claim_unique_cp_completion": "F",
    "claim_equal_cylinder_laws": "F",
    "open_tt_response": "G",
    "claim_broad_time_no_go": "G",
    "claim_axiom_update": "G",
    "claim_toe_progress": "G",
}

I = sp.I
R = sp.Rational
L_TIME = 24
HALF_DIMENSION = 24
SIGMA_X = sp.Matrix(((0, 1), (1, 0)))
SIGMA_Z = sp.diag(1, -1)
PHASE = sp.diag(1, -I)
IDENTITY32 = sp.eye(32)
ZERO16 = sp.zeros(16)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def block_diagonal_twice(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix.vstack(
        sp.Matrix.hstack(matrix, sp.zeros(matrix.rows)),
        sp.Matrix.hstack(sp.zeros(matrix.rows), matrix),
    )


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "worktree_axiom": git_output("hash-object", "--", AXIOM_PATH),
        "registry": git_output("rev-parse", f"origin/main:{REGISTRY_PATH}"),
        "worktree_registry": git_output("hash-object", "--", REGISTRY_PATH),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


@cache
def one_shot_instrument_facts() -> dict[str, object]:
    inherited = b194.instrument_pointer_facts()
    effects = inherited["effects"]
    lueders_completeness = sum(
        (effect.H * effect for effect in effects), sp.zeros(32)
    )
    maximally_mixed = IDENTITY32 / 32
    weights = tuple(sp.trace(effect * maximally_mixed) for effect in effects)
    return {
        "effect_count": len(effects),
        "effects": effects,
        "projectors": inherited["projectors"],
        "complete": matrix_equal(lueders_completeness, IDENTITY32),
        "weights": weights,
        "pointer_dilation": (
            inherited["writer_unitary"]
            and inherited["writer_nonidentity"]
            and inherited["faithful_joint_readout"]
        ),
    }


@cache
def reduced_action_fixture() -> dict[str, sp.Matrix]:
    shift, differential, _cosine, _reflection = b192.temporal_matrices()
    original = sp.expand(
        sp.kronecker_product(
            sp.eye(L_TIME), R(2, 7) * sp.eye(2) + I * SIGMA_X
        )
        + sp.kronecker_product(differential, SIGMA_Z)
    )
    full_phase = sp.kronecker_product(sp.eye(L_TIME), PHASE)
    action = sp.expand(full_phase.H * original * full_phase)
    block_c = action[HALF_DIMENSION:, :HALF_DIMENSION]
    block_d = action[HALF_DIMENSION:, HALF_DIMENSION:]
    graph = sp.Matrix.vstack(
        sp.eye(HALF_DIMENSION),
        -block_d.inv(method="DM") * block_c,
    )
    action_inverse = action.inv(method="DM")
    kernel = sp.expand(action_inverse + action_inverse.T)
    gram = sp.expand(graph.T * kernel * graph)
    shift_fiber = sp.kronecker_product(shift, sp.eye(2))
    half_embedding = sp.Matrix.vstack(
        sp.eye(HALF_DIMENSION), sp.zeros(HALF_DIMENSION)
    )
    return {
        "action": action,
        "graph": graph,
        "kernel": kernel,
        "gram": gram,
        "shift": shift_fiber,
        "embedding": half_embedding,
    }


@cache
def coordinate_shift_facts() -> dict[str, object]:
    fixture = reduced_action_fixture()
    graph = fixture["graph"]
    shift = fixture["shift"]
    gram = fixture["gram"]
    embedding = fixture["embedding"]
    orientation_facts = []
    for translated, witness_index in ((shift, 20), (shift.T, 2)):
        candidate = sp.expand(embedding.T * translated * graph)
        graph_residual = sp.expand(translated * graph - graph * candidate)
        symmetry_residual = sp.expand(gram * candidate - candidate.T * gram)
        contraction_defect = sp.expand(
            gram - candidate.T * gram * candidate
        )
        witness = sp.factor(
            contraction_defect[witness_index, witness_index]
        )
        orientation_facts.append({
            "graph_residual_rank": graph_residual.rank(),
            "metric_symmetry_residual_rank": symmetry_residual.rank(),
            "contraction_defect_rank": contraction_defect.rank(),
            "negative_witness": witness,
            "negative_witness_is_negative": (
                sp.ask(sp.Q.negative(witness)) is True
            ),
        })
    return {
        "forward": orientation_facts[0],
        "reverse": orientation_facts[1],
    }


@cache
def projected_shift_facts() -> dict[str, object]:
    fixture = reduced_action_fixture()
    graph = fixture["graph"]
    shift = fixture["shift"]
    kernel = fixture["kernel"]
    gram = fixture["gram"]
    gram_inverse = gram.inv(method="DM")

    def compressed(power: int) -> sp.Matrix:
        return sp.expand(
            gram_inverse * graph.T * kernel * shift**power * graph
        )

    first = compressed(1)
    second = compressed(2)
    third = compressed(3)
    symmetry_residual = sp.expand(gram * first - first.T * gram)
    order_two_residual = sp.expand(first**2 - second)
    order_three_residual = sp.expand(first**3 - third)
    first_nonzero = next(
        sp.factor(value) for value in order_three_residual if value != 0
    )
    return {
        "metric_symmetry_residual_rank": symmetry_residual.rank(),
        "order_two_residual_rank": order_two_residual.rank(),
        "order_three_residual_rank": order_three_residual.rank(),
        "order_three_witness": first_nonzero,
    }


def reflected_lag_predictor(radius: int, lag: int) -> sp.Matrix:
    _shift, differential, _cosine, _reflection = b192.temporal_matrices()
    action = sp.expand(
        sp.kronecker_product(
            sp.eye(L_TIME), R(2, 7) * sp.eye(2) + I * radius * SIGMA_X
        )
        + sp.kronecker_product(differential, SIGMA_Z)
    )
    covariance = action.inv(method="DM")
    reflected = sp.expand(covariance + covariance.H)
    return sp.simplify(
        reflected[2 * lag:2 * lag + 2, :2]
        * reflected[:2, :2].inv(method="DM")
    )


@cache
def adjacent_predictor_facts() -> dict[str, object]:
    _shift, differential, _cosine, _reflection = b192.temporal_matrices()
    action = sp.expand(
        sp.kronecker_product(sp.eye(L_TIME), R(2, 7) * sp.eye(2))
        + sp.kronecker_product(differential, SIGMA_Z)
    )
    covariance = action.inv(method="DM")
    predictor = sp.simplify(
        covariance[2:4, :2] * covariance[:2, :2].inv(method="DM")
    )
    q = sp.factor(predictor[1, 1])
    coefficient = sp.factor(q**2)
    complement = sp.factor(1 - coefficient)
    scalar_predictors = []
    for sign in (1, -1):
        scalar_covariance = (
            R(2, 7) * sp.eye(L_TIME) + sign * differential
        ).inv(method="DM")
        scalar_predictors.append(sp.factor(
            scalar_covariance[1, 0] / scalar_covariance[0, 0]
        ))
    projector_plus = (sp.eye(16) + b194.GTIME) / 2
    projector_minus = (sp.eye(16) - b194.GTIME) / 2
    lifted_internal = sp.expand(
        scalar_predictors[0] * projector_plus
        + scalar_predictors[1] * projector_minus
    )
    lifted_sector = block_diagonal_twice(lifted_internal)
    sector_reflection = block_diagonal_twice(b194.GTIME)
    lag_facts = {
        (radius, lag): reflected_lag_predictor(radius, lag)
        for radius in (0, 1) for lag in (1, 2)
    }
    return {
        "predictor": predictor,
        "raw_covariance_nonhermitian_rank": sp.expand(
            covariance - covariance.H
        ).rank(),
        "q": q,
        "coefficient": coefficient,
        "complement": complement,
        "lifted_sector": lifted_sector,
        "exact_full_clifford_lift": (
            scalar_predictors == [-q, q]
            and matrix_equal(lifted_internal, -q * b194.GTIME)
            and matrix_equal(lifted_sector, -q * sector_reflection)
        ),
        "clifford_form": matrix_equal(predictor, -q * SIGMA_Z),
        "strict": (
            sp.ask(sp.Q.positive(q)) is True
            and sp.ask(sp.Q.positive(1 - q)) is True
        ),
        "lag_one_zero": all(
            matrix_equal(lag_facts[(radius, 1)], sp.zeros(2))
            for radius in (0, 1)
        ),
        "lag_two_nonzero_scalar": all(
            lag_facts[(radius, 2)][0, 0] != 0
            and matrix_equal(
                lag_facts[(radius, 2)],
                lag_facts[(radius, 2)][0, 0] * sp.eye(2),
            )
            for radius in (0, 1)
        ),
    }


@cache
def completion_facts() -> dict[str, object]:
    predictor = adjacent_predictor_facts()
    coefficient = predictor["coefficient"]
    complement = predictor["complement"]
    q = predictor["q"]
    reflection = block_diagonal_twice(b194.GTIME)
    lifted_predictor = predictor["lifted_sector"]
    effects = one_shot_instrument_facts()["effects"]
    rotations = []
    for spatial in b194.proper_cubic_rotations():
        full = sp.eye(4)
        full[:3, :3] = spatial
        rotations.append(block_diagonal_twice(
            b194.b190.wedge_representation(full)
        ))

    # Conditional on physically designating the exact algebraic lift, the
    # resulting invariant common CP subchannel is
    # Psi(rho)=c J rho J, whose sole Kraus operator is the exact lifted raw
    # predictor -q J (its global sign is immaterial).  Completion A adds the
    # CP residual d Id; completion B adds d Ad_J and therefore equals Ad_J.
    completeness_a = sp.expand(
        coefficient * reflection.H * reflection
        + complement * IDENTITY32
    )
    completeness_b = sp.expand(
        (coefficient + complement) * reflection.H * reflection
    )
    cubic_fiber_label_covariance = (
        matrix_equal(reflection.H * reflection, IDENTITY32)
        and all(matrix_equal(rotation.H * rotation, IDENTITY32)
                for rotation in rotations)
        and all(matrix_equal(rotation * reflection,
                             reflection * rotation)
                for rotation in rotations)
    )

    first_effect = effects[0]
    reflected_effect = sp.expand(reflection * first_effect * reflection)
    reflected_index = next(
        index for index, effect in enumerate(effects)
        if matrix_equal(reflected_effect, effect)
    )
    initial = IDENTITY32 / 32
    post_first = sp.expand(first_effect * initial * first_effect)

    def channel_a(matrix: sp.MatrixBase) -> sp.Matrix:
        return sp.expand(
            coefficient * reflection * matrix * reflection
            + complement * matrix
        )

    def channel_b(matrix: sp.MatrixBase) -> sp.Matrix:
        return sp.expand(reflection * matrix * reflection)

    history_a = tuple(sp.simplify(sp.trace(
        effect * channel_a(post_first)
    )) for effect in effects)
    history_b = tuple(sp.simplify(sp.trace(
        effect * channel_b(post_first)
    )) for effect in effects)
    return {
        "lifted_predictor_hermitian": matrix_equal(
            lifted_predictor.H, lifted_predictor
        ),
        "lifted_predictor_norm": matrix_equal(
            lifted_predictor.H * lifted_predictor,
            coefficient * IDENTITY32,
        ),
        "common_subchannel_trace_nonincreasing": (
            sp.ask(sp.Q.nonnegative(coefficient)) is True
            and sp.ask(sp.Q.nonnegative(1 - coefficient)) is True
        ),
        "residual_a_cp": sp.ask(sp.Q.positive(complement)) is True,
        "residual_b_cp": (
            sp.ask(sp.Q.positive(complement)) is True
            and matrix_equal(reflection.H * reflection, IDENTITY32)
        ),
        "coefficient_positive": sp.ask(sp.Q.positive(coefficient)) is True,
        "complement_positive": sp.ask(sp.Q.positive(complement)) is True,
        "coefficient_sum": sp.simplify(coefficient + complement) == 1,
        "completion_a_tp": matrix_equal(completeness_a, IDENTITY32),
        "completion_b_tp": matrix_equal(completeness_b, IDENTITY32),
        "cubic_fiber_label_covariant": cubic_fiber_label_covariance,
        "stationary_a": matrix_equal(channel_a(initial), initial),
        "stationary_b": matrix_equal(channel_b(initial), initial),
        "reflected_index": reflected_index,
        "history_a": history_a,
        "history_b": history_b,
        "prefix_a": sp.simplify(sum(history_a)) == R(1, 8),
        "prefix_b": sp.simplify(sum(history_b)) == R(1, 8),
        "distinct": history_a != history_b,
        "a_first_return": history_a[0],
        "a_reflected": history_a[reflected_index],
        "b_first_return": history_b[0],
        "b_reflected": history_b[reflected_index],
    }


N5_LINES = (
    "per_element: checked the eight exact Block-194 Lueders Kraus projectors, one reduced action fiber, one conditional lifted CP subchannel, and two exact CPTP completions.",
    "per_site: checked one adjacent L24 covariance predictor and one fixed first-to-second event prefix; no physical time step was assumed.",
    "per_mode: checked the frozen radius-zero and radius-one reflected lag-one/lag-two kernels; no TT source response or held-out point was evaluated.",
    "per_block: checked one-shot instrument, coordinate shift, metric projection, covariance predictor, and channel completion as separate dependency blocks.",
    "lattice_wide: checked and not executed -- no full OS/CAR reconstruction, global process tensor, autonomous Record persistence, Regge bridge, nonlinear gravity, or retained TOE theory is claimed.",
)


@cache
def note_facts() -> dict[str, bool]:
    if not NOTE_PATH.is_file():
        return {"exists": False, "n5": False, "scope": False}
    text = NOTE_PATH.read_text(encoding="utf-8")
    scope_tokens = (
        "one_shot_lueders_instrument: exact",
        "coordinate_shift_os_contraction: failed",
        "projected_shift_semigroup: failed_at_order_3",
        "adjacent_predictor: strict_contraction",
        "cp_completion_selection: nonunique_under_conditional_subchannel_typing",
        "tt_response: not_executed",
        "heldouts: sealed",
        "broad_time_no_go: not_claimed",
        "no_go_discipline_gate: FAIL",
        "negative_disposition: partial-attempt-with-named-untested-routes",
        "minimal_axiom_update: none",
        "toe_percentage_movement: 0",
    )
    return {
        "exists": True,
        "n5": all(line in text for line in N5_LINES),
        "scope": all(token in text for token in scope_tokens),
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    instrument = one_shot_instrument_facts()
    coordinate = coordinate_shift_facts()
    projected = projected_shift_facts()
    predictor = adjacent_predictor_facts()
    completions = completion_facts()
    note = note_facts()
    claims = {
        "main": CURRENT_MAIN,
        "lueders_complete": True,
        "shift_graph_invariant": False,
        "shift_contractive": False,
        "projected_selfadjoint": False,
        "projected_semigroup": False,
        "predictor_unitary": False,
        "unique_completion": False,
        "equal_cylinders": False,
        "tt_response_open": False,
        "broad_time_no_go": False,
        "axiom_update": False,
        "toe_progress": False,
    }
    if mutation == "stale_main_authority":
        claims["main"] = "stale"
    elif mutation == "break_lueders_completeness":
        claims["lueders_complete"] = False
    elif mutation == "claim_shift_graph_invariant":
        claims["shift_graph_invariant"] = True
    elif mutation == "claim_shift_contractive":
        claims["shift_contractive"] = True
    elif mutation == "claim_projected_shift_selfadjoint":
        claims["projected_selfadjoint"] = True
    elif mutation == "claim_projected_shift_semigroup":
        claims["projected_semigroup"] = True
    elif mutation == "claim_predictor_unitary":
        claims["predictor_unitary"] = True
    elif mutation == "claim_unique_cp_completion":
        claims["unique_completion"] = True
    elif mutation == "claim_equal_cylinder_laws":
        claims["equal_cylinders"] = True
    elif mutation == "open_tt_response":
        claims["tt_response_open"] = True
    elif mutation == "claim_broad_time_no_go":
        claims["broad_time_no_go"] = True
    elif mutation == "claim_axiom_update":
        claims["axiom_update"] = True
    elif mutation == "claim_toe_progress":
        claims["toe_progress"] = True

    shift_graph_invariant = all(
        coordinate[orientation]["graph_residual_rank"] == 0
        for orientation in ("forward", "reverse")
    )
    shift_contractive = all(
        not coordinate[orientation]["negative_witness_is_negative"]
        for orientation in ("forward", "reverse")
    )
    projected_selfadjoint = (
        projected["metric_symmetry_residual_rank"] == 0
    )
    projected_semigroup = (
        projected["order_two_residual_rank"] == 0
        and projected["order_three_residual_rank"] == 0
    )
    predictor_unitary = sp.simplify(predictor["coefficient"] - 1) == 0
    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["parent"] and authority["prereg"]
            and authority["axiom"] == CURRENT_AXIOM_BLOB
            and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
            and authority["inputs"],
            "authority, parent, preregistration, axioms, registry, and literal inputs are pinned",
        ),
        "B": (
            instrument["effect_count"] == 8
            and instrument["projectors"]
            and instrument["complete"] == claims["lueders_complete"]
            and instrument["weights"] == (R(1, 8),) * 8
            and instrument["pointer_dilation"],
            "Block 194 supplies an exact normalized one-shot Lueders instrument and faithful M2 dilation",
        ),
        "C": (
            all(
                coordinate[orientation]["graph_residual_rank"] == 2
                and coordinate[orientation][
                    "metric_symmetry_residual_rank"
                ] == 24
                and coordinate[orientation]["contraction_defect_rank"] == 4
                and coordinate[orientation]["negative_witness_is_negative"]
                for orientation in ("forward", "reverse")
            )
            and shift_graph_invariant == claims["shift_graph_invariant"]
            and shift_contractive == claims["shift_contractive"],
            "the direct positive-time coordinate shift leaves the Schur graph and fails OS contraction",
        ),
        "D": (
            projected["metric_symmetry_residual_rank"] == 24
            and projected["order_two_residual_rank"] == 0
            and projected["order_three_residual_rank"] == 2
            and projected["order_three_witness"] != 0
            and projected_selfadjoint == claims["projected_selfadjoint"]
            and projected_semigroup == claims["projected_semigroup"],
            "the Gram-projected shifts are not OS self-adjoint and stop composing at order three",
        ),
        "E": (
            predictor["clifford_form"] and predictor["strict"]
            and predictor["exact_full_clifford_lift"]
            and predictor["raw_covariance_nonhermitian_rank"] == 44
            and predictor["lag_one_zero"]
            and predictor["lag_two_nonzero_scalar"]
            and predictor_unitary == claims["predictor_unitary"],
            "the raw predictor is strict while the reflected kernel exposes even-lag correlations",
        ),
        "F": (
            completions["lifted_predictor_hermitian"]
            and completions["lifted_predictor_norm"]
            and completions["common_subchannel_trace_nonincreasing"]
            and completions["residual_a_cp"]
            and completions["residual_b_cp"]
            and completions["coefficient_positive"]
            and completions["complement_positive"]
            and completions["coefficient_sum"]
            and completions["completion_a_tp"]
            and completions["completion_b_tp"]
            and completions["cubic_fiber_label_covariant"]
            and completions["stationary_a"]
            and completions["stationary_b"]
            and completions["reflected_index"] == 7
            and completions["prefix_a"] and completions["prefix_b"]
            and completions["distinct"] == (not claims["equal_cylinders"])
            and claims["unique_completion"] is False,
            "one conditional CP subchannel has two cubic/fiber-label-covariant inequivalent completions",
        ),
        "G": (
            note["exists"] and note["n5"] and note["scope"]
            and claims["tt_response_open"] is False
            and claims["broad_time_no_go"] is False
            and claims["axiom_update"] is False
            and claims["toe_progress"] is False,
            "the failed dependency gate seals response and demotes the negative with zero TOE movement",
        ),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 96 else statement[:93] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0
    checks = Checks()
    for key, (condition, statement) in evaluate(args.mutation).items():
        checks.check(key, statement, condition)
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
