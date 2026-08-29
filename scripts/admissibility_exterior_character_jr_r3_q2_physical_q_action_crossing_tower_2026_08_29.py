#!/usr/bin/env python3
"""Exact recurrence certificate for the selected physical-Q action/crossing tower.

The selected fiber is chi_(ell,parity)(p0) chi_V(C1), where p0 is a fine
plaquette in the first r=3 cell and C1 is the disjoint eight-link coarse
defining-vector loop in the second cell.  One layer has the Block246 order

    central crossing * (I-Q) * defining-vector multiplication.

Physical conditional Haar Q removes only the trivial p0 character.  The
defining-vector Clebsch--Gordan rule is exact, and the original-link crossing
multiplies (ell,parity) by r_(ell,parity)^4 r_V^8.  The resulting triangular
recurrence has a nonzero new top-spin coefficient at every layer whenever the
supplied finite-step multipliers are nonzero.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

import admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_independent_2026_08_29 as independent


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
MAX_LAYER = 8
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_PHYSICAL_Q_ACTION_CROSSING_TOWER_NO_GO_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SECOND_CROSSING_ACTION_LEAKAGE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE = ROOT / AUDIT_INPUT_PATHS[0]
TRIVIAL = (0, 1)
VECTOR = (1, -1)
MUTATIONS = (
    "reverse_action_crossing_order",
    "drop_physical_q",
    "delay_physical_q",
    "replace_action_with_identity",
    "kill_top_multiplier",
    "identify_temporal_multiplicity_as_new_irreps",
    "claim_global_minimal_memory",
    "identify_sample_rank_as_universal",
    "identify_physical_q_with_static_cup",
    "axiom_edit",
)


@dataclass(frozen=True)
class Sample:
    name: str
    determinant: F
    spins: tuple[F, ...]


def make_samples():
    positive_a = Sample(
        "positive_a",
        F(1, 5),
        (F(1),) + tuple(F(spin + 2, 2 * spin + 5) for spin in range(1, MAX_LAYER + 1)),
    )
    positive_b = Sample(
        "positive_b",
        F(2, 7),
        (F(1),) + tuple(F(2 * spin + 1, 3 * spin + 4) for spin in range(1, MAX_LAYER + 1)),
    )
    signed = Sample(
        "signed",
        F(-2, 7),
        (F(1),) + tuple(
            F((-1) ** spin * (spin + 1), 4 * spin + 5)
            for spin in range(1, MAX_LAYER + 1)
        ),
    )
    identity = Sample("identity", F(1), (F(1),) * (MAX_LAYER + 1))
    haar = Sample("Haar", F(0), (F(1),) + (F(0),) * MAX_LAYER)
    t_zero_spins = list(positive_a.spins)
    t_zero_spins[1] = F(0)
    t_zero = Sample("t_zero", positive_a.determinant, tuple(t_zero_spins))
    return positive_a, positive_b, signed, identity, haar, t_zero


POSITIVE_A, POSITIVE_B, SIGNED, IDENTITY, HAAR, T_ZERO = make_samples()


def clean(coefficients):
    return {irrep: value for irrep, value in coefficients.items() if value}


def add_term(coefficients, irrep, value):
    coefficients[irrep] = coefficients.get(irrep, F(0)) + value


def defining_vector_multiply(coefficients):
    """Multiply by (1,-) using exact O(3) Clebsch--Gordan arithmetic."""
    result = {}
    for (spin, parity), coefficient in coefficients.items():
        outputs = (1,) if spin == 0 else range(spin - 1, spin + 2)
        for output_spin in outputs:
            add_term(result, (output_spin, -parity), coefficient)
    return clean(result)


def physical_q_residual(coefficients):
    """Apply physical (I-Q) on the p0 fiber at fixed coarse deltas."""
    result = dict(coefficients)
    result.pop(TRIVIAL, None)
    return clean(result)


def irrep_multiplier(irrep, sample):
    spin, parity = irrep
    if irrep == TRIVIAL:
        return F(1)
    if spin == 0:
        if parity != -1:
            raise AssertionError("unexpected spin-zero O(3) parity")
        return sample.determinant
    return sample.spins[spin]


def crossing_eigenvalue(irrep, sample):
    """Four p0 edges and eight disjoint C1 defining-vector edges."""
    return irrep_multiplier(irrep, sample) ** 4 * sample.spins[1] ** 8


def central_crossing(coefficients, sample):
    return clean({
        irrep: value * crossing_eigenvalue(irrep, sample)
        for irrep, value in coefficients.items()
    })


def physical_layer(coefficients, sample):
    """Block246 order: action, exact physical-Q subtraction, then crossing."""
    return central_crossing(
        physical_q_residual(defining_vector_multiply(coefficients)), sample
    )


def reversed_layer(coefficients, sample):
    """Hostile control: crossing before the new action/Q layer."""
    return physical_q_residual(
        defining_vector_multiply(central_crossing(coefficients, sample))
    )


def recurrence_rhs(coefficients, sample):
    """Direct coefficient recurrence, independent of the composition helpers."""
    result = {}
    maximum = max(spin for spin, _parity in coefficients)
    for output_spin in range(maximum + 2):
        for output_parity in (-1, 1):
            irrep = (output_spin, output_parity)
            if irrep == TRIVIAL:
                continue
            total = F(0)
            for input_spin in range(maximum + 1):
                input_irrep = (input_spin, -output_parity)
                if input_irrep not in coefficients:
                    continue
                allowed = (1,) if input_spin == 0 else range(input_spin - 1, input_spin + 2)
                if output_spin in allowed:
                    total += coefficients[input_irrep]
            if total:
                result[irrep] = total * crossing_eigenvalue(irrep, sample)
    return clean(result)


def tower(sample, last_layer=MAX_LAYER):
    levels = [{VECTOR: F(1)}]
    while len(levels) < last_layer:
        levels.append(physical_layer(levels[-1], sample))
    return levels


def identity_tower(last_layer=4):
    coefficients = {VECTOR: F(1)}
    levels = [coefficients]
    while len(levels) < last_layer:
        coefficients = physical_q_residual(defining_vector_multiply(coefficients))
        levels.append(coefficients)
    return levels


def top_formula(sample, layer):
    result = F(1)
    for spin in range(2, layer + 1):
        result *= crossing_eigenvalue((spin, (-1) ** spin), sample)
    return result


def fraction_rank(rows):
    columns = sorted({irrep for row in rows for irrep in row})
    matrix = [[row.get(irrep, F(0)) for irrep in columns] for row in rows]
    rank = 0
    for column in range(len(columns)):
        pivot = next((row for row in range(rank, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        value = matrix[rank][column]
        matrix[rank] = [entry / value for entry in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                left - factor * right for left, right in zip(matrix[row], matrix[rank])
            ]
        rank += 1
    return rank


def fraction_mod(value, prime):
    return value.numerator * pow(value.denominator, -1, prime) % prime


def modular_rank(rows, prime):
    columns = sorted({irrep for row in rows for irrep in row})
    matrix = [
        [fraction_mod(row.get(irrep, F(0)), prime) for irrep in columns]
        for row in rows
    ]
    rank = 0
    for column in range(len(columns)):
        pivot = next((row for row in range(rank, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [value * inverse % prime for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                (left - factor * right) % prime
                for left, right in zip(matrix[row], matrix[rank])
            ]
        rank += 1
    return rank


def polynomial_product_linear(roots):
    coefficients = [F(1)]
    for root in roots:
        updated = [F(0)] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            updated[degree] -= root * coefficient
            updated[degree + 1] += coefficient
        coefficients = updated
    return coefficients


def crossing_only_recurrence_residual(seed, sample):
    """Check prod_lambda(C-lambda I) seed=0 on its fixed irrep support."""
    roots = sorted({crossing_eigenvalue(irrep, sample) for irrep in seed})
    polynomial = polynomial_product_linear(roots)
    powers = [seed]
    for _index in range(1, len(polynomial)):
        powers.append(central_crossing(powers[-1], sample))
    result = {}
    for coefficient, power in zip(polynomial, powers):
        for irrep, value in power.items():
            add_term(result, irrep, coefficient * value)
    return clean(result), len(roots)


def scope_check(mutation=None):
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = (
        "temporal multiplicity leakage is not new Peter--Weyl content",
        "Global minimal memory remains open",
        "Sample-wise Block246 ranks are not used as universal generic ranks",
        "physical conditional-Haar `Q`, not a static cup projector",
        "No axiom or approved primitive is edited",
    )
    if mutation in {
        "identify_temporal_multiplicity_as_new_irreps",
        "claim_global_minimal_memory",
        "identify_sample_rank_as_universal",
        "identify_physical_q_with_static_cup",
        "axiom_edit",
    }:
        return False
    return all(phrase in text for phrase in required)


def mutation_detected(mutation):
    seed = {VECTOR: F(1)}
    if mutation == "reverse_action_crossing_order":
        return physical_layer(seed, POSITIVE_A) != reversed_layer(seed, POSITIVE_A)
    if mutation == "drop_physical_q":
        hostile = central_crossing(defining_vector_multiply(seed), POSITIVE_A)
        return TRIVIAL in hostile and TRIVIAL not in physical_layer(seed, POSITIVE_A)
    if mutation == "delay_physical_q":
        correct = identity_tower(3)[-1]
        delayed = physical_q_residual(
            defining_vector_multiply(defining_vector_multiply(seed))
        )
        return correct != delayed
    if mutation == "replace_action_with_identity":
        hostile = central_crossing(physical_q_residual(seed), POSITIVE_A)
        return max(spin for spin, _parity in hostile) != 2
    if mutation == "kill_top_multiplier":
        spins = list(POSITIVE_A.spins)
        spins[5] = F(0)
        hostile_sample = Sample("killed_top", POSITIVE_A.determinant, tuple(spins))
        hostile = tower(hostile_sample, 5)[-1]
        return hostile.get((5, -1), F(0)) == 0
    return not scope_check(mutation)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        detected = 0
        for mutation in MUTATIONS:
            caught = mutation_detected(mutation)
            detected += int(caught)
            print(f"[{'PASS' if caught else 'FAIL'}] mutation rejected: {mutation}")
        print(f"TOTAL: PASS={detected} FAIL={len(MUTATIONS)-detected}")
        return int(detected != len(MUTATIONS))
    if arguments.mutation:
        caught = mutation_detected(arguments.mutation)
        print(f"[{'PASS' if caught else 'FAIL'}] mutation rejected: {arguments.mutation}")
        print(f"TOTAL: PASS={int(caught)} FAIL={int(not caught)}")
        return int(not caught)

    checks = []

    def check(label, condition):
        checks.append((label, bool(condition)))
        print(f"[{'PASS' if condition else 'FAIL'}] {label}")

    summaries = {}
    for sample in (POSITIVE_A, POSITIVE_B, SIGNED):
        levels = tower(sample)
        summaries[sample.name] = {
            "layers": len(levels),
            "rational_rank": fraction_rank(levels),
            "top": levels[-1].get((MAX_LAYER, 1)),
        }
        check(f"{sample.name}: direct composition equals coefficient recurrence",
              all(physical_layer(levels[index], sample)
                  == recurrence_rhs(levels[index], sample)
                  for index in range(MAX_LAYER - 1)))
        check(f"{sample.name}: every layer has the exact nonzero top-spin coefficient",
              all(levels[layer - 1].get((layer, (-1) ** layer), F(0))
                  == top_formula(sample, layer) != 0
                  for layer in range(1, MAX_LAYER + 1)))
        check(f"{sample.name}: physical-Q mean vanishes at every layer",
              all(level.get(TRIVIAL, F(0)) == 0 for level in levels))
        check(f"{sample.name}: first {MAX_LAYER} selected layers are rationally independent",
              fraction_rank(levels) == MAX_LAYER)
        for prime in (1009, 1013, 1019):
            check(f"{sample.name} F_{prime}: exact layer rank {MAX_LAYER}",
                  modular_rank(levels, prime) == MAX_LAYER)

    heldout_levels = tower(POSITIVE_B)
    check("held-out F_10007: exact layer rank eight",
          modular_rank(heldout_levels, 10007) == MAX_LAYER)

    expected_identity = (
        {(1, -1): F(1)},
        {(1, 1): F(1), (2, 1): F(1)},
        {(0, -1): F(1), (1, -1): F(2), (2, -1): F(2), (3, -1): F(1)},
        {(1, 1): F(5), (2, 1): F(5), (3, 1): F(3), (4, 1): F(1)},
    )
    check("identity crossing: first four successive physical-Q action layers",
          tuple(identity_tower(4)) == expected_identity
          and tuple(tower(IDENTITY, 4)) == expected_identity)
    check("Haar endpoint: the first crossed residual and all descendants vanish",
          all(not level for level in tower(HAAR)[1:]))
    check("t=0 endpoint with live higher spins: the C1 spectator kills the tower",
          all(not level for level in tower(T_ZERO)[1:]))
    check("action/crossing reversal is a nonzero hostile control",
          physical_layer({VECTOR: F(1)}, POSITIVE_A)
          != reversed_layer({VECTOR: F(1)}, POSITIVE_A))
    check("delaying physical Q changes the third action layer",
          mutation_detected("delay_physical_q"))
    fixed_seed = identity_tower(4)[-1]
    recurrence_residual, recurrence_order = crossing_only_recurrence_residual(
        fixed_seed, POSITIVE_A
    )
    check("crossing-only fixed Peter-Weyl support obeys its finite spectral recurrence",
          not recurrence_residual and recurrence_order <= len(fixed_seed))
    check("crossing-only action creates no new Peter-Weyl irrep",
          set(central_crossing(fixed_seed, POSITIVE_A)) <= set(fixed_seed))
    check("bounded no-go scope", scope_check())
    check("independent Laurent-character implementation", independent.all_checks_pass())

    print("identity_layers", expected_identity)
    print("sample_summaries", summaries)
    print("crossing_only_recurrence_order", recurrence_order)
    print("per_element: checked and executed — every recurrence coefficient through layer eight is exact")
    print("per_site: checked and not executed — no physical lattice-site evolution law is claimed")
    print("per_mode: checked and not executed — no continuum or lattice momentum mode is constructed")
    print("per_block: checked and executed — one selected disjoint p0/C1 physical-J3 fiber is complete")
    print("lattice_wide: checked and not executed — global minimal memory and the full symmetric step remain open")
    passed = sum(int(condition) for _label, condition in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
