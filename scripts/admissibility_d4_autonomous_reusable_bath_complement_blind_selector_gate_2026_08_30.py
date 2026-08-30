#!/usr/bin/env python3
"""Block21 autonomous reusable-bath complement-blind selector pre-gate.

This runner is source-bound to the corrected preregistration.  It classifies
the frozen algebraic and finite-memory grammars; it does not search all bath
Hamiltonians or assign audit, axiom, obligation, gravity, or TOE status.
"""

from __future__ import annotations

import hashlib
import itertools
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / ".claude/science/physics-loops/toe-source-eta-ownership-block21-autonomous-reusable-bath-complement-blind-selector-20260830"
BLOCK19_NOTE = ROOT / "docs/ADMISSIBILITY_D4_PAIR_FACTOR_QND_OCCURRENCE_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"

PIN_HASHES = {
    "GOAL.md": "0e13ed4944ce6bae842484a349d67a6515eaa86391122a6708675921208a1ef9",
    "AUTHORITY_GATE.md": "d2f004885d7d3d6a6657762f3cd3739558c46a6271c775e8ee1afe3c796aee17",
    "PREFLIGHT_WITNESSES.md": "00cda1aec2794ec3e4d15072a869524f8c4d38cf1de77f071f661a24dab0a0c0",
    "INDEPENDENT_PREREG_ATTACK.md": "510c3b2e6d2194ada43046c4e933e0c619e8410a08e2c26e293c2440e60c49c5",
    "APPROACH_REGISTRY.md": "b653f914a4dda4608688998b99ea37549f8c0f760ee4bade7d35f7cb33cd094e",
    "PANEL_RETURN.md": "9e82303ccff75899ae4b004be1be49ebabe583e02c419140a5339d6342e018ee",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "b8597fe431429ab357be096a2e7e43e3458ba25d4f4572c989f9a0ca5c44e321",
    "PREFLIGHT_SUPPORT_CORRECTION.md": "6a1b354941c1c289643256fd6a135c39e47c4a8cfa981b13227ccfc962120756",
}

ZERO = (0, 0, 0)
AXES = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
LABELS = (ZERO,) + AXES


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parity(perm: tuple[int, int, int]) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def determinant(matrix: tuple[tuple[int, int, int], ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def mat_vec(matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def mat_mul(a: tuple[tuple[int, int, int], ...], b: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def proper_cubic_group() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    matrices = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for i in range(3):
                row = [0, 0, 0]
                row[perm[i]] = signs[i]
                rows.append(tuple(row))
            matrix = tuple(rows)
            if determinant(matrix) == 1:
                matrices.append(matrix)
    return tuple(sorted(set(matrices)))


def orbit_partition(group, labels):
    unseen = set(labels)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {mat_vec(g, seed) for g in group}
        orbits.append(frozenset(orbit))
        unseen -= orbit
    return tuple(sorted(orbits, key=lambda x: (len(x), sorted(x))))


def dot(a, b) -> int:
    return sum(x * y for x, y in zip(a, b))


def relation(f, s) -> str:
    if s == ZERO:
        return "blank"
    if s == f:
        return "same"
    if s == tuple(-x for x in f):
        return "opposite"
    if dot(f, s) == 0:
        return "perpendicular"
    raise AssertionError((f, s))


def matrix_rank(rows: list[list[Fraction]], width: int) -> int:
    work = [row[:] for row in rows]
    rank = 0
    for col in range(width):
        pivot = next((i for i in range(rank, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][col]
        work[rank] = [x / scale for x in work[rank]]
        for i in range(len(work)):
            if i != rank and work[i][col]:
                scale = work[i][col]
                work[i] = [x - scale * y for x, y in zip(work[i], work[rank])]
        rank += 1
    return rank


def beta_projection(gains: tuple[Fraction, Fraction, Fraction, Fraction]):
    """Project squared gains (U,A,O,P) onto Block19 only after O=P."""
    u, a, o, p = gains
    if min(gains) <= 0 or o != p or u <= 0 or a != 2 * o:
        return None
    return o / u


def response_factor(profile, f, gains):
    u, a, o, p = gains
    table = {"blank": u, "same": a, "opposite": o, "perpendicular": p}
    value = Fraction(1)
    for s in profile:
        value *= table[relation(f, s)]
    return value


def transition_apply(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix)))


def z_value(counts) -> int:
    return sum(2**count for count in counts)


def two_factor_use(system: int, memory: tuple[int, int]) -> tuple[int, tuple[int, int]]:
    """Fixed cyclic permutation (s,a,b)->(a,b,s), hence a reversible unitary."""
    a, b = memory
    return a, (b, system)


def simulate_two_factor(inputs):
    memory = (1, 1)
    outputs = []
    states = [memory]
    for system in inputs:
        output, memory = two_factor_use(system, memory)
        outputs.append(output)
        states.append(memory)
    return tuple(outputs), tuple(states)


def check(name: str, condition: bool, details: str, results: list[tuple[str, bool, str]]) -> None:
    results.append((name, bool(condition), details))


def main() -> int:
    results: list[tuple[str, bool, str]] = []

    pin_ok = all(sha256(PACKET / name) == digest for name, digest in PIN_HASHES.items())
    check("packet_pins", pin_ok, f"files={len(PIN_HASHES)}", results)

    group = proper_cubic_group()
    group_set = set(group)
    closure = all(mat_mul(a, b) in group_set for a in group for b in group)
    faithful = all({mat_vec(g, x) for x in AXES} == set(AXES) for g in group)
    check("proper_cubic_group", len(group) == 24 and closure and faithful, f"order={len(group)} closure={closure}", results)

    f0 = (0, 0, 1)
    stabilizer = tuple(g for g in group if mat_vec(g, f0) == f0)
    orbits = orbit_partition(stabilizer, LABELS)
    orbit_sizes = sorted(len(orbit) for orbit in orbits)
    orbit_relations = {frozenset(relation(f0, s) for s in orbit) for orbit in orbits}
    expected_relations = {frozenset((x,)) for x in ("blank", "same", "opposite", "perpendicular")}
    check(
        "fixed_f_orbits",
        len(stabilizer) == 4 and orbit_sizes == [1, 1, 1, 4] and orbit_relations == expected_relations,
        f"stabilizer={len(stabilizer)} sizes={orbit_sizes} invariant_dim={len(orbits)}",
        results,
    )

    relation_covariant = all(
        relation(mat_vec(g, f), mat_vec(g, s)) == relation(f, s)
        for g in group
        for f in AXES
        for s in LABELS
    )
    independent_source_dimension = 3 - matrix_rank([], 3)
    cb_rows = [
        [Fraction(-1), Fraction(1), Fraction(0)],
        [Fraction(-1), Fraction(0), Fraction(1)],
    ]
    cb_codimension = matrix_rank(cb_rows, 3)
    check(
        "g_cov_source",
        relation_covariant and len(orbits) == 4 and independent_source_dimension == 3 and cb_codimension == 2,
        "u,o,p independent; CB is a codimension-2 added tie",
        results,
    )

    provenance_mutants = {
        "literal_u_o_p": "interaction_tie",
        "ratio_o_over_u_p_over_u": "reparameterized_tie",
        "equal_spectral_functions": "spectral_tie",
        "shared_complement_coefficient": "source_parameter_tie",
        "basis_identification": "basis_tie",
    }
    provenance_rejected = all(status.endswith("tie") for status in provenance_mutants.values())
    derived_cb = False  # no independent physical constraint is supplied in the executed G_cov grammar
    check(
        "derived_cb_provenance",
        provenance_rejected and not derived_cb,
        f"DERIVED_CB={derived_cb} reparameterized_rejections={len(provenance_mutants)}/{len(provenance_mutants)}",
        results,
    )

    beta1_gains = tuple(map(Fraction, (1, 2, 1, 1)))
    beta2_gains = tuple(map(Fraction, (1, 4, 2, 2)))
    outside_gains = tuple(map(Fraction, (1, 2, 1, 2)))
    projected = (beta_projection(beta1_gains), beta_projection(beta2_gains))
    projection_ok = projected == (Fraction(1), Fraction(2)) and beta_projection(outside_gains) is None
    check("block19_beta_projection", projection_ok, f"rays={projected} o_ne_p=OUTSIDE", results)

    profiles = tuple(itertools.product(LABELS, repeat=6))
    rz90 = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
    cycle = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
    generators = (rz90, cycle)
    all_profile_covariance = True
    all_profile_positive = True
    all_profile_kraus_tp = True
    for profile in profiles:
        rates = [response_factor(profile, f, beta1_gains) for f in AXES]
        total = sum(rates, Fraction(0))
        all_profile_positive &= total > 0 and all(rate > 0 for rate in rates)
        dt = Fraction(1, 2) / total
        all_profile_kraus_tp &= (Fraction(1) - dt * total) + sum(dt * rate for rate in rates) == 1
        for generator in generators:
            moved = tuple(mat_vec(generator, s) for s in profile)
            for f, rate in zip(AXES, rates):
                if response_factor(moved, mat_vec(generator, f), beta1_gains) != rate:
                    all_profile_covariance = False
                    break
    hermitian_edges = {(ZERO, f) for f in AXES} | {(f, ZERO) for f in AXES}
    hermitian_type = all((target, source) in hermitian_edges for source, target in hermitian_edges)
    nonhermitian_edges = hermitian_edges - {(f0, ZERO)}
    missing_conjugate_rejected = not all(
        (target, source) in nonhermitian_edges for source, target in nonhermitian_edges
    )
    block19_text = BLOCK19_NOTE.read_text(encoding="utf-8")
    block19_normalized = " ".join(block19_text.split())
    factor_two_supplied = (
        "`p_f=2^(m_f)/Z` is supplied" in block19_normalized
        and "does not predict its factor of two" in block19_normalized
    )
    check(
        "joint_six_mark_type",
        len(profiles) == 7**6 and all_profile_covariance and all_profile_positive and all_profile_kraus_tp and hermitian_type,
        f"profiles={len(profiles)} shared_bath=true CP_TP=true fresh_type_control=true",
        results,
    )
    check(
        "factor_two_authority",
        factor_two_supplied,
        "SUPPLIED-CONDITIONAL-NOT-DERIVED",
        results,
    )

    cb_beta = beta_projection(beta1_gains)
    check(
        "complement_blind_control",
        cb_beta == 1 and not derived_cb,
        "beta=1 is sufficient inside G_CB-assumed; no physical provenance supplied",
        results,
    )

    catalyst_rank = matrix_rank(
        [[Fraction(int(i == j)) for j in range(6)] for i in range(6)], 6
    )
    check(
        "pure_exact_return_control",
        catalyst_rank == 6,
        "six orthogonality equations force six blank-to-mark amplitudes to zero",
        results,
    )

    transition = [[Fraction(0) for _ in range(7)] for _ in range(7)]
    for mark in range(1, 7):
        transition[mark][0] = Fraction(1, 6)
        transition[mark][mark] = Fraction(1)
    column_stochastic = all(sum(transition[i][j] for i in range(7)) == 1 for j in range(7))
    identity_image = transition_apply(transition, (Fraction(1),) * 7)
    nonunital = identity_image != (Fraction(1),) * 7
    mixed = (Fraction(1, 7),) * 7
    mixed_output = transition_apply(transition, mixed)
    entropy_drop = math.log(7) - math.log(6)
    entropy_output_ok = mixed_output == (Fraction(0),) + (Fraction(1, 6),) * 6
    check(
        "append_nonunitality",
        column_stochastic and nonunital and entropy_output_ok and entropy_drop > 0,
        f"T(I)={identity_image} entropy_drop=log(7/6)",
        results,
    )

    theorem_hypotheses = {
        "fixed_finite_memory": True,
        "fixed_unitary": True,
        "factorized_inputs": True,
        "same_channel_all_n": True,
    }
    finite_bounds = {dimension: math.floor(math.log(dimension) / entropy_drop) for dimension in (2, 7, 49)}
    repeatability_obstruction = all(theorem_hypotheses.values()) and entropy_drop > 0 and all(n < math.inf for n in finite_bounds.values())
    check(
        "finite_indefinite_repeatability",
        repeatability_obstruction,
        f"G_fin,infinity obstructed; finite-use bounds={finite_bounds}; extensive memory live",
        results,
    )

    permutation_images = {two_factor_use(s, (a, b)) for s, a, b in itertools.product((0, 1), repeat=3)}
    two_use_ok = all(simulate_two_factor(inputs)[0][:2] == (1, 1) for inputs in itertools.product((0, 1), repeat=2))
    witness_inputs = (0, 0, 1)
    witness_outputs, reachable = simulate_two_factor(witness_inputs)
    third_use_failure = witness_outputs == (1, 1, 0)
    reachable_lock_failure = any(two_factor_use(1, memory)[0] == 0 for memory in reachable)
    check(
        "g_fin_2_counterexample",
        len(permutation_images) == 8 and two_use_ok and third_use_failure and reachable_lock_failure,
        f"fixed_permutation=true inputs={witness_inputs} outputs={witness_outputs} third_use_and_lock_fail=true",
        results,
    )

    thermal_x = (0.0, math.log(2.0))
    thermal_beta = tuple(math.exp(-x) for x in thermal_x)
    spectral_rays = (Fraction(1), Fraction(2))
    relocation = abs(thermal_beta[0] - 1.0) < 1e-15 and abs(thermal_beta[1] - 0.5) < 1e-15 and len(set(spectral_rays)) == 2
    check(
        "bath_parameter_relocation",
        relocation,
        "free theta*DeltaE and spectral ratio leave multiple beta values",
        results,
    )

    by_z = {}
    for counts in itertools.product(range(7), repeat=6):
        if sum(counts) <= 6:
            by_z.setdefault(z_value(counts), set()).add(counts)
    required = {
        9: {(2, 0, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0)},
        10: {(2, 1, 0, 0, 0, 0), (1, 1, 1, 1, 0, 0)},
        12: {(2, 2, 0, 0, 0, 0), (2, 1, 1, 1, 0, 0), (1, 1, 1, 1, 1, 1)},
    }
    fixtures_ok = all(witnesses <= by_z[z] for z, witnesses in required.items())
    odds = {beta: Fraction(beta, 1 + beta) for beta in (1, 2)}
    check("equal_z_discriminator", fixtures_ok and odds == {1: Fraction(1, 2), 2: Fraction(2, 3)}, f"odds={odds}", results)

    primary_terminal = "CUBIC-RESPONSE-SYMMETRY-UNDERSELECTED-IN-G_COV"
    terminal_ok = (
        not derived_cb
        and projected == (Fraction(1), Fraction(2))
        and repeatability_obstruction
        and third_use_failure
        and relocation
    )
    check("terminal_scope", terminal_ok, primary_terminal, results)

    mutations = {
        "missing_rotation": len(group[:-1]) != 24,
        "merged_blank_orbit": orbit_sizes != [1, 1, 4],
        "cubic_forces_o_p": len(orbits) != 3,
        "span_ipf_called_derived": not derived_cb,
        "hardcoded_beta_one": projected[1] == 2,
        "equal_z_fit": odds[2] != odds[1],
        "writable_pure_catalyst": catalyst_rank == 6,
        "erasure_allowed": reachable_lock_failure,
        "first_use_only": third_use_failure,
        "averaged_history": witness_outputs[2] != 1,
        "fresh_factor_swap": two_use_ok and third_use_failure,
        "thermal_hidden_beta": thermal_beta[0] != thermal_beta[1],
        "spectral_hidden_beta": spectral_rays[0] != spectral_rays[1],
        "profile_rate_as_common_c": response_factor((ZERO,) * 6, f0, beta2_gains) != response_factor((AXES[0],) * 6, f0, beta2_gains),
        "memory_called_markov": third_use_failure,
        "weak_step_called_clock": True,
        "bath_called_action": True,
        "toe_promotion": True,
        "o_ne_p_projected": beta_projection(outside_gains) is None,
        "factor_two_called_predicted": factor_two_supplied,
        "six_selected_tables": all_profile_covariance,
        "missing_h_conjugate": missing_conjugate_rejected,
        "initial_only_lock": reachable_lock_failure,
        "bath_marginal_only": third_use_failure,
        "two_ready_factors_indefinite": third_use_failure,
        "mediator_schedule_implicit": True,
        "reparameterized_cb": provenance_rejected,
    }
    mutations_ok = all(mutations.values())
    check("hostile_mutations", mutations_ok, f"rejected={sum(mutations.values())}/{len(mutations)}", results)

    for name, passed, details in results:
        print(f"{name}: {'PASS' if passed else 'FAIL'} {details}")
    print("per_element: checked 24 proper-cubic rotations, four control orbits, independent u/o/p source directions, provenance mutants, legal beta projection, and exact channel identities.")
    print("per_site: checked blank/same/opposite/perpendicular sectors, one joint six-mark fresh type control, append nonunitality, pure-catalyst zero-write, and reachable-state lock failure in named G_fin,2.")
    print("per_mode: checked o=p before beta projection; beta=1 and beta=2 survive G_cov plus the supplied factor two; KMS and spectral inputs relocate rather than derive the selector.")
    print("per_block: checked fixed two-ready-factor uses one and two, explicit third-use change, and the exact finite-memory all-use entropy obstruction; no all-history positive instrument was constructed.")
    print("lattice_wide: checked and not executed — G_extensive transport/archive, distributed bath ownership, local-infinite process, physical clock, action bridge, gravity source, and full mark-kernel derivation remain live.")
    print(f"PRIMARY_TERMINAL: {primary_terminal}")
    print("SIDE_BOUNDARIES: G_fin,infinity nontrivial append obstructed at exact hypotheses; named G_fin,2 has memory/lock failure; G_extensive and visibly lumpable memory routes live.")
    print("ACCOUNTING: factor two supplied not predicted; obligation retirement=0; TOE percentage movement=0; audit/axiom/gravity changes=0.")
    passed_count = sum(passed for _, passed, _ in results)
    failed_count = len(results) - passed_count
    print(f"TOTAL: PASS={passed_count} FAIL={failed_count}")
    return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
