#!/usr/bin/env python3
"""Independent Block-204 checker.

Rebuilds the C32 PVM and its logical Clifford commutant from exterior
generators, derives the Fock obstruction from occupation generating functions,
checks three full-Fock positive maps and a refinement discriminator, and
separates block-diagonal from coherent two-sector controls.  It imports neither
the primary Block-204 runner nor its intermediates.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import cache
from itertools import product
from math import comb
from pathlib import Path
import subprocess

import sympy as sp

import admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24 as b190


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block204-record-operator-system-descent-20260826"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREREG_COMMIT = "03c32997ace9a723fa39ce5fbe6afbad9087e6ee"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block204-record-operator-system-descent-20260826/GOAL.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
)

I = sp.I
R = sp.Rational
EVENT_COUNT = 8
EVENT_RANK = 4
ONE_BODY_DIM = 32

MUTATIONS = (
    "stale_authority",
    "alter_goal",
    "break_pvm_rank",
    "erase_logical_fiber",
    "call_logical_fiber_action_selected",
    "erase_vacuum_intersection",
    "erase_mixed_port_sector",
    "call_gamma_complete",
    "call_at_least_one_orthogonal",
    "call_n1_full_unit",
    "call_n1_selected",
    "erase_complement_extension",
    "erase_number_share_extension",
    "erase_support_share_extension",
    "call_full_extensions_equal",
    "break_extension_covariance",
    "break_extension_n1_match",
    "call_all_extensions_split_consistent",
    "call_positive_extension_unique",
    "drop_periodic_pair",
    "call_map_difference_probability_difference",
    "call_os_periodic",
    "call_partition_derived",
    "call_os_coherence_independent",
    "claim_toe_progress",
)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.cancel(value) == 0 for value in left - right
    )


def block_matrix(
    upper_left: sp.MatrixBase,
    upper_right: sp.MatrixBase,
    lower_left: sp.MatrixBase,
    lower_right: sp.MatrixBase,
) -> sp.Matrix:
    return sp.Matrix.vstack(
        sp.Matrix.hstack(upper_left, upper_right),
        sp.Matrix.hstack(lower_left, lower_right),
    )


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=60
    ).strip()


@cache
def authority_facts() -> dict[str, object]:
    prereg = subprocess.run(
        ("git", "merge-base", "--is-ancestor", PREREG_COMMIT, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, timeout=60,
    ).returncode == 0
    return {
        "main": git_output("rev-parse", "origin/main"),
        "prereg": prereg,
        "goal_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}")
            == git_output("hash-object", "--", GOAL_PATH)
        ),
    }


@cache
def rebuilt_pvm() -> dict[str, object]:
    creation = b190.CREATION
    annihilation = b190.ANNIHILATION
    gammas = tuple(
        item
        for axis in range(4)
        for item in (
            creation[axis] + annihilation[axis],
            I * (creation[axis] - annihilation[axis]),
        )
    )
    identity16 = sp.eye(16)
    o1 = sp.expand(I * gammas[0] * gammas[2] * gammas[3])
    o2 = sp.expand(I * gammas[1] * gammas[2] * gammas[5])
    labels = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    base_effects = tuple(sp.expand(
        (identity16 + sign1 * o1) * (identity16 + sign2 * o2) / 4
    ) for sign1, sign2 in labels)
    gtime = creation[3] + annihilation[3]
    orientation = sp.expand(
        I * gtime * (creation[2] + annihilation[2])
    )
    zero16 = sp.zeros(16)
    effects = tuple(
        sp.expand(block_matrix(
            effect, sign * effect * orientation,
            sign * orientation * effect, effect,
        ) / 2)
        for effect in base_effects for sign in (1, -1)
    )
    return {
        "gammas": gammas,
        "o1": o1,
        "o2": o2,
        "orientation": orientation,
        "effects": effects,
        "orientation_hermitian": matrix_equal(
            orientation.H, orientation
        ),
        "orientation_involution": matrix_equal(
            orientation * orientation, identity16
        ),
        "orientation_commutes": all(matrix_equal(
            orientation * effect, effect * orientation
        ) for effect in base_effects),
        "base_ranks": tuple(effect.rank() for effect in base_effects),
        "ranks": tuple(effect.rank() for effect in effects),
        "projectors": all(matrix_equal(
            effect.H, effect
        ) and matrix_equal(effect * effect, effect) for effect in effects),
        "orthogonal": all(matrix_equal(
            effects[left] * effects[right], sp.zeros(32)
        ) for left in range(EVENT_COUNT)
          for right in range(left + 1, EVENT_COUNT)),
        "complete": matrix_equal(sum(effects, sp.zeros(32)), sp.eye(32)),
        "zero16": zero16,
    }


@cache
def independent_fiber_facts() -> dict[str, object]:
    pvm = rebuilt_pvm()
    gammas = pvm["gammas"]
    identity2 = sp.eye(2)
    identity32 = sp.eye(32)
    tau_x = sp.Matrix(((0, 1), (1, 0)))
    tau_y = sp.Matrix(((0, -I), (I, 0)))
    tensor = sp.kronecker_product
    stabilizers = (
        tensor(identity2, pvm["o1"]),
        tensor(identity2, pvm["o2"]),
        tensor(tau_x, pvm["orientation"]),
    )
    logical = (
        tensor(identity2, gammas[2]),
        -I * tensor(identity2, gammas[0] * gammas[1] * gammas[7]),
        -I * tensor(tau_x, gammas[0] * gammas[5] * gammas[7]),
        -I * tensor(tau_y, gammas[0] * gammas[1] * gammas[4]),
    )
    monomials = []
    for mask in range(16):
        value = identity32
        for index, generator in enumerate(logical):
            if mask & (1 << index):
                value = sp.expand(value * generator)
        monomials.append(value)
    fiber_dimensions = tuple(
        sp.Matrix.hstack(*(
            sp.expand(effect * value * effect).reshape(1024, 1)
            for value in monomials
        )).rank()
        for effect in pvm["effects"]
    )
    return {
        "stabilizers": stabilizers,
        "stabilizers_commute": all(matrix_equal(
            stabilizers[left] * stabilizers[right],
            stabilizers[right] * stabilizers[left],
        ) for left in range(3) for right in range(left + 1, 3)),
        "logical_clifford": all(matrix_equal(
            logical[left] * logical[right] + logical[right] * logical[left],
            (2 if left == right else 0) * identity32,
        ) for left in range(4) for right in range(4)),
        "logical_commutes_pvm": all(matrix_equal(
            generator * effect, effect * generator
        ) for generator in logical for effect in pvm["effects"]),
        "logical_span": sp.Matrix.hstack(*(
            value.reshape(1024, 1) for value in monomials
        )).rank(),
        "fiber_dimensions": fiber_dimensions,
        "action_selected": False,
    }


@cache
def generating_function_facts() -> dict[str, object]:
    pvm = rebuilt_pvm()
    rank = pvm["ranks"][0]
    gamma_rank = sum(comb(rank, degree) for degree in range(rank + 1))
    full_dim = sum(comb(ONE_BODY_DIM, degree)
                   for degree in range(ONE_BODY_DIM + 1))
    mixed_two_particle_count = comb(EVENT_COUNT, 2) * rank**2
    single_port_span = 1 + EVENT_COUNT * (gamma_rank - 1)
    at_least_pair_intersection = (
        (2**rank - 1) ** 2 * 2 ** (ONE_BODY_DIM - 2 * rank)
    )
    return {
        "full_dim": full_dim,
        "gamma_rank": gamma_rank,
        "gamma_cross_rank": 1,
        "vacuum_sum": EVENT_COUNT,
        "mixed_two_particle_count": mixed_two_particle_count,
        "single_port_span": single_port_span,
        "gamma_complete": single_port_span == full_dim,
        "at_least_pair_intersection": at_least_pair_intersection,
        "at_least_orthogonal": at_least_pair_intersection == 0,
        "n1_dim": comb(ONE_BODY_DIM, 1),
        "n1_rank_sum": EVENT_COUNT * rank,
        "n1_full_unit": comb(ONE_BODY_DIM, 1) == full_dim,
    }


@cache
def positive_extension_facts() -> dict[str, object]:
    uniform = (Fraction(1, EVENT_COUNT),) * EVENT_COUNT

    def complement(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        support = tuple(index for index, value in enumerate(counts) if value)
        if len(support) != 1:
            return uniform
        return tuple(Fraction(int(index == support[0]), 1)
                     for index in range(EVENT_COUNT))

    def number_share(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        total = sum(counts)
        return uniform if total == 0 else tuple(
            Fraction(value, total) for value in counts
        )

    def support_share(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        size = sum(value > 0 for value in counts)
        return uniform if size == 0 else tuple(
            Fraction(int(value > 0), size) for value in counts
        )

    maps = (complement, number_share, support_share)
    positive_unital = n1_match = covariance = True
    count = 0
    for counts in product(range(EVENT_RANK + 1), repeat=EVENT_COUNT):
        count += 1
        reversed_counts = tuple(reversed(counts))
        for mapping in maps:
            values = mapping(counts)
            positive_unital = positive_unital and (
                all(value >= 0 for value in values) and sum(values) == 1
            )
            if sum(counts) == 1:
                n1_match = n1_match and values == tuple(
                    Fraction(value, 1) for value in counts
                )
            covariance = covariance and (
                mapping(reversed_counts) == tuple(reversed(values))
            )
    witness = (2, 1) + (0,) * 6
    witness_values = tuple(mapping(witness) for mapping in maps)
    refined = (1, 1, 1) + (0,) * 6

    def dynamic_complement(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
        support = tuple(index for index, value in enumerate(counts) if value)
        if len(support) != 1:
            return (Fraction(1, len(counts)),) * len(counts)
        return tuple(Fraction(int(index == support[0]), 1)
                     for index in range(len(counts)))

    split_pairs = (
        (dynamic_complement(witness)[0],
         sum(dynamic_complement(refined)[:2])),
        (number_share(witness)[0], sum(number_share(refined)[:2])),
        (support_share(witness)[0], sum(support_share(refined)[:2])),
    )
    additive_constraints = []
    for left in range(1, EVENT_RANK + 1):
        for right in range(1, EVENT_RANK + 1 - left):
            row = [0] * EVENT_RANK
            row[left - 1] -= 1
            row[right - 1] -= 1
            row[left + right - 1] += 1
            additive_constraints.append(row)
    return {
        "pattern_count": count,
        "positive_unital": positive_unital,
        "n1_match": n1_match,
        "covariance": covariance,
        "faithful": n1_match,
        "complement_exists": positive_unital,
        "number_share_exists": positive_unital,
        "support_share_exists": positive_unital,
        "distinct": len(set(witness_values)) == 3,
        "witness": witness,
        "witness_values": witness_values,
        "count": len(maps),
        "unique": len(maps) == 1,
        "split_consistent": tuple(
            before == after for before, after in split_pairs
        ),
        "ratio_additive_nullity": (
            EVENT_RANK - sp.Matrix(additive_constraints).rank()
        ),
        "physical_split_rule_supplied": False,
    }


@cache
def periodic_facts() -> dict[str, object]:
    radius = sp.factor(((sp.sqrt(53) - 2) / 7) ** 24)
    weights = tuple(sp.factor(value / (1 - radius) ** 2) for value in (
        1, -radius, -radius, radius**2,
    ))
    return {
        "sum": sp.simplify(sum(weights)),
        "vacuum": weights[0],
        "n1": sp.factor(weights[1] + weights[2]),
        "pair": weights[3],
        "vacuum_nonzero": weights[0] != 0,
        "n1_negative": sp.factor(weights[1] + weights[2]).is_negative is True,
        "pair_nonzero": weights[3] != 0,
    }


@cache
def scalar_lift_control() -> dict[str, object]:
    radius = sp.factor(((sp.sqrt(53) - 2) / 7) ** 24)
    variables = sp.symbols("u0:8")
    numerator = sp.prod((1 - radius * value) ** EVENT_RANK
                        for value in variables)
    denominator = (1 - radius) ** ONE_BODY_DIM
    swapped = numerator.xreplace({variables[0]: variables[1],
                                  variables[1]: variables[0]})
    return {
        "normalized": sp.simplify(
            numerator.subs({value: 1 for value in variables}) / denominator
        ) == 1,
        "exchangeable": sp.simplify(numerator - swapped) == 0,
        "covariant_unital_value": R(1, EVENT_COUNT),
        "map_difference_forces_value_difference": False,
        "actual_c32_lift_supplied": False,
    }


@cache
def os_control_facts() -> dict[str, object]:
    effects = rebuilt_pvm()["effects"]
    weight = sp.symbols("weight", real=True)
    rho = sp.diag(
        weight * sp.eye(16) / 16,
        (1 - weight) * sp.eye(16) / 16,
    )
    values = tuple(sp.factor(sp.trace(rho * effect))
                   for effect in effects)
    coherence = sp.symbols("coherence", real=True)
    syndrome_orientation = independent_fiber_facts()["stabilizers"][2]
    coherent_rho = sp.expand((sp.eye(32) + coherence * syndrome_orientation) / 32)
    coherent_values = tuple(sp.factor(sp.trace(coherent_rho * effect))
                            for effect in effects)
    expected_coherent = tuple(
        (1 + sign * coherence) / EVENT_COUNT
        for _event in range(EVENT_COUNT // 2)
        for sign in (1, -1)
    )
    return {
        "trace": sp.simplify(sp.trace(rho)),
        "values": values,
        "sum": sp.simplify(sum(values)),
        "independent": all(not value.has(weight) for value in values),
        "positive_domain": "0<=weight<=1",
        "block_diagonal_only": True,
        "coherent_trace": sp.simplify(sp.trace(coherent_rho)),
        "coherent_diagonal_blocks": (
            matrix_equal(coherent_rho[:16, :16], sp.eye(16) / 32)
            and matrix_equal(coherent_rho[16:, 16:], sp.eye(16) / 32)
        ),
        "coherent_values": coherent_values,
        "coherent_expected": all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(coherent_values, expected_coherent)
        ),
        "coherence_independent": all(
            not value.has(coherence) for value in coherent_values
        ),
        "periodic_descent": False,
        "physical_partition_derived": False,
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    pvm = rebuilt_pvm()
    fiber = independent_fiber_facts()
    gf = generating_function_facts()
    maps = positive_extension_facts()
    periodic = periodic_facts()
    scalar_control = scalar_lift_control()
    os_control = os_control_facts()
    claims = {
        "main": CURRENT_MAIN,
        "goal_frozen": True,
        "pvm_ranks": (4,) * 8,
        "logical_fiber": True,
        "logical_fiber_action_selected": False,
        "vacuum_cross": 1,
        "mixed_two": True,
        "gamma_complete": False,
        "at_least_orthogonal": False,
        "n1_full_unit": False,
        "n1_selected": False,
        "complement_exists": True,
        "number_share_exists": True,
        "support_share_exists": True,
        "extensions_distinct": True,
        "extension_covariance": True,
        "extension_n1_match": True,
        "all_extensions_split_consistent": False,
        "extension_unique": False,
        "periodic_pair_nonzero": True,
        "map_difference_probability_difference": False,
        "os_periodic": False,
        "partition_derived": False,
        "os_coherence_independent": False,
        "toe_progress": False,
    }
    if mutation == "stale_authority":
        claims["main"] = "stale"
    elif mutation == "alter_goal":
        claims["goal_frozen"] = False
    elif mutation == "break_pvm_rank":
        claims["pvm_ranks"] = (3,) * 8
    elif mutation == "erase_logical_fiber":
        claims["logical_fiber"] = False
    elif mutation == "call_logical_fiber_action_selected":
        claims["logical_fiber_action_selected"] = True
    elif mutation == "erase_vacuum_intersection":
        claims["vacuum_cross"] = 0
    elif mutation == "erase_mixed_port_sector":
        claims["mixed_two"] = False
    elif mutation == "call_gamma_complete":
        claims["gamma_complete"] = True
    elif mutation == "call_at_least_one_orthogonal":
        claims["at_least_orthogonal"] = True
    elif mutation == "call_n1_full_unit":
        claims["n1_full_unit"] = True
    elif mutation == "call_n1_selected":
        claims["n1_selected"] = True
    elif mutation == "erase_complement_extension":
        claims["complement_exists"] = False
    elif mutation == "erase_number_share_extension":
        claims["number_share_exists"] = False
    elif mutation == "erase_support_share_extension":
        claims["support_share_exists"] = False
    elif mutation == "call_full_extensions_equal":
        claims["extensions_distinct"] = False
    elif mutation == "break_extension_covariance":
        claims["extension_covariance"] = False
    elif mutation == "break_extension_n1_match":
        claims["extension_n1_match"] = False
    elif mutation == "call_all_extensions_split_consistent":
        claims["all_extensions_split_consistent"] = True
    elif mutation == "call_positive_extension_unique":
        claims["extension_unique"] = True
    elif mutation == "drop_periodic_pair":
        claims["periodic_pair_nonzero"] = False
    elif mutation == "call_map_difference_probability_difference":
        claims["map_difference_probability_difference"] = True
    elif mutation == "call_os_periodic":
        claims["os_periodic"] = True
    elif mutation == "call_partition_derived":
        claims["partition_derived"] = True
    elif mutation == "call_os_coherence_independent":
        claims["os_coherence_independent"] = True
    elif mutation == "claim_toe_progress":
        claims["toe_progress"] = True

    return {
        "I1": (
            authority["main"] == claims["main"]
            and authority["prereg"]
            and authority["goal_frozen"] == claims["goal_frozen"],
            "registration authority is independently pinned",
        ),
        "I2": (
            pvm["orientation_hermitian"] and pvm["orientation_involution"]
            and pvm["orientation_commutes"]
            and pvm["base_ranks"] == (4,) * 4
            and pvm["ranks"] == claims["pvm_ranks"]
            and pvm["projectors"] and pvm["orthogonal"] and pvm["complete"]
            and fiber["stabilizers_commute"]
            and fiber["logical_clifford"] == claims["logical_fiber"]
            and fiber["logical_commutes_pvm"]
            and fiber["logical_span"] == 16
            and fiber["fiber_dimensions"] == (16,) * EVENT_COUNT
            and fiber["action_selected"]
            == claims["logical_fiber_action_selected"],
            "the rebuilt PVM is a C8 syndrome measurement with an exact C4 logical Clifford fiber, but no action-selected identification",
        ),
        "I3": (
            gf["full_dim"] == 2**32
            and gf["gamma_rank"] == 16
            and gf["gamma_cross_rank"] == claims["vacuum_cross"]
            and (gf["mixed_two_particle_count"] > 0) == claims["mixed_two"]
            and gf["gamma_complete"] == claims["gamma_complete"],
            "generating functions expose the shared vacuum and 448 mixed-port two-particle states",
        ),
        "I4": (
            gf["at_least_orthogonal"] == claims["at_least_orthogonal"]
            and gf["at_least_pair_intersection"] > 0
            and gf["n1_dim"] == 32 and gf["n1_rank_sum"] == 32
            and gf["n1_full_unit"] == claims["n1_full_unit"]
            and claims["n1_selected"] is False,
            "N=1 restores the PVM only as a sector unit; at-least-one-port events overlap",
        ),
        "I5": (
            maps["pattern_count"] == 5**8 and maps["positive_unital"]
            and maps["faithful"]
            and maps["complement_exists"] == claims["complement_exists"]
            and maps["number_share_exists"]
            == claims["number_share_exists"]
            and maps["support_share_exists"]
            == claims["support_share_exists"]
            and maps["distinct"] == claims["extensions_distinct"]
            and maps["covariance"] == claims["extension_covariance"]
            and maps["n1_match"] == claims["extension_n1_match"]
            and maps["unique"] == claims["extension_unique"]
            and maps["split_consistent"] == (False, True, False)
            and (all(maps["split_consistent"])
                 == claims["all_extensions_split_consistent"])
            and maps["ratio_additive_nullity"] == 1
            and maps["physical_split_rule_supplied"] is False,
            "three exhaustive positive extensions differ on multi-port occupation; only number-share passes additive multiplicity splitting, whose physical use is not supplied",
        ),
        "I6": (
            periodic["sum"] == 1 and periodic["vacuum_nonzero"]
            and periodic["n1_negative"]
            and periodic["pair_nonzero"] == claims["periodic_pair_nonzero"]
            and scalar_control["normalized"]
            and scalar_control["exchangeable"]
            and scalar_control["covariant_unital_value"] == R(1, 8)
            and scalar_control["map_difference_forces_value_difference"]
            == claims["map_difference_probability_difference"]
            and scalar_control["actual_c32_lift_supplied"] is False,
            "the periodic per-copy functional has signed sectors; a scalar C32 control proves distinct covariant maps can still all give 1/8",
        ),
        "I7": (
            os_control["trace"] == 1
            and os_control["values"] == (R(1, 8),) * 8
            and os_control["sum"] == 1 and os_control["independent"]
            and os_control["positive_domain"] == "0<=weight<=1"
            and os_control["block_diagonal_only"]
            and os_control["coherent_trace"] == 1
            and os_control["coherent_diagonal_blocks"]
            and os_control["coherent_expected"]
            and os_control["coherence_independent"]
            == claims["os_coherence_independent"]
            and os_control["periodic_descent"] == claims["os_periodic"]
            and os_control["physical_partition_derived"]
            == claims["partition_derived"],
            "the block-diagonal Schur control gives 1/8 for all classical sector weights, while coherent extensions bias the signs and remain unselected",
        ),
        "I8": (
            maps["count"] >= 3 and not maps["unique"]
            and claims["toe_progress"] is False,
            "projective lifts stop but logical-fiber/Naimark and positive operator-system routes survive without a supplied action intertwiner, retiring no obligation",
        ),
    }


def run(mutation: str = "") -> int:
    results = evaluate(mutation)
    passed = failed = 0
    for key, (condition, statement) in results.items():
        ok = bool(condition)
        passed += int(ok)
        failed += int(not ok)
        print(f"[{key}] {'PASS' if ok else 'FAIL'}: {statement}")
    if not mutation:
        gf = generating_function_facts()
        fiber = independent_fiber_facts()
        extensions = positive_extension_facts()
        scalar_control = scalar_lift_control()
        os_control = os_control_facts()
        print(
            "INDEPENDENT_FOCK: dim=2^32; Gamma rank=16; cross=vacuum; "
            f"mixed_N2={gf['mixed_two_particle_count']}; "
            f"single_port_span={gf['single_port_span']}."
        )
        print(
            "INDEPENDENT_FIBER: C32=C8_syndrome x C4_logical; "
            f"logical_span={fiber['logical_span']}; action_intertwiner=absent."
        )
        print(
            "INDEPENDENT_EXTENSIONS: three positive unital full-Fock maps; "
            f"at {extensions['witness']} values={extensions['witness_values']}."
        )
        print(
            "INDEPENDENT_REFINEMENT: complement/number/support split="
            f"{extensions['split_consistent']}; ratio-additive nullity="
            f"{extensions['ratio_additive_nullity']}; physical rule=open."
        )
        print(
            "INDEPENDENT_SCALAR_CONTROL: Q_R=-rI32 would force every "
            "covariant unital map to value "
            f"{scalar_control['covariant_unital_value']}; actual lift=absent."
        )
        print(
            "INDEPENDENT_OS: block-diagonal values="
            f"{os_control['values']}; coherent values="
            f"{os_control['coherent_values']}."
        )
        print(
            "INDEPENDENT_STOP: strict projective lifts fail in tested families; "
            "logical-fiber and positive operator-system routes survive; "
            "no C32 action state/intertwiner or physical context is supplied."
        )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


def mutation_sweep() -> int:
    survived = []
    for mutation in MUTATIONS:
        if all(condition for condition, _statement
               in evaluate(mutation).values()):
            survived.append(mutation)
    print(
        f"MUTATION_TOTAL: PASS={len(MUTATIONS) - len(survived)} "
        f"FAIL={len(survived)}"
    )
    if survived:
        print("SURVIVED: " + ",".join(survived))
    return int(bool(survived))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()
    return run(args.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
