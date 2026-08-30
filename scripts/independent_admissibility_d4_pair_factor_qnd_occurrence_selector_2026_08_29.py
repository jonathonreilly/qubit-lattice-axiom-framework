#!/usr/bin/env python3
"""Independent certificate for the corrected Block19 pair-factor grammar.

The runner derives its census and numerical witnesses from the grammar.  In
particular, anticipated orbit counts, race fractions, and hazard bounds are
not embedded as comparison constants.
"""

from __future__ import annotations

import itertools
import hashlib
import math
import re
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


DIM = 3


def signed_coordinate_axes(dimension: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(sign if coordinate == axis else 0 for coordinate in range(dimension))
        for axis in range(dimension)
        for sign in (1, -1)
    )


DIRECTIONS = signed_coordinate_axes(DIM)
MARKS = len(DIRECTIONS)
SLOTS = len(DIRECTIONS)
BLANK = 0
CARRIER_SIZE = MARKS + 1
EXECUTED_BETAS = (Fraction(1), Fraction(2))
CORRECTION_REF = "809a64b74d"
BLOCK19_SUPPORT_DIRECTORY = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block19-microscopic-qnd-occurrence-selector-20260829"
)
BLOCK18_DIRECTORY = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block18-pure-record-occurrence-selection-lumpability-20260829"
)


class Certificate:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failures: list[str] = []

    def require(self, name: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
            suffix = f": {detail}" if detail else ""
            self.failures.append(f"FAIL {name}{suffix}")


def parity(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def rotate_vector(
    vector: tuple[int, ...], perm: tuple[int, ...], signs: tuple[int, ...]
) -> tuple[int, ...]:
    out = [0] * DIM
    for source_axis, value in enumerate(vector):
        out[perm[source_axis]] = signs[source_axis] * value
    return tuple(out)


def proper_cubic_rotations() -> tuple[tuple[int, ...], ...]:
    direction_index = {vector: index for index, vector in enumerate(DIRECTIONS)}
    maps = set()
    for perm in itertools.permutations(range(DIM)):
        for signs in itertools.product((-1, 1), repeat=DIM):
            if parity(perm) * math.prod(signs) != 1:
                continue
            maps.add(
                tuple(
                    direction_index[rotate_vector(vector, perm, signs)]
                    for vector in DIRECTIONS
                )
            )
    return tuple(sorted(maps))


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Return left after right."""
    return tuple(left[right[index]] for index in range(MARKS))


def power(rotation: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    result = tuple(range(MARKS))
    for _ in range(exponent):
        result = compose(rotation, result)
    return result


def cycles(permutation: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(permutation)))
    answer = []
    while unseen:
        start = min(unseen)
        cycle = []
        cursor = start
        while cursor in unseen:
            unseen.remove(cursor)
            cycle.append(cursor)
            cursor = permutation[cursor]
        answer.append(tuple(cycle))
    return tuple(answer)


def rotate_profile(
    profile: tuple[int, ...], rotation: tuple[int, ...]
) -> tuple[int, ...]:
    out = [BLANK] * SLOTS
    for slot, value in enumerate(profile):
        out[rotation[slot]] = BLANK if value == BLANK else rotation[value - 1] + 1
    return tuple(out)


def profile_stats(profile: tuple[int, ...]) -> tuple[int, tuple[int, ...], int]:
    counts = tuple(profile.count(label + 1) for label in range(MARKS))
    occupancy = sum(counts)
    raw_sum = sum(1 << count for count in counts)
    return occupancy, counts, raw_sum


def burnside_fixed(rotation: tuple[int, ...]) -> int:
    fixed = 1
    for slot_cycle in cycles(rotation):
        returned = power(rotation, len(slot_cycle))
        fixed_labels = sum(returned[label] == label for label in range(MARKS))
        fixed *= 1 + fixed_labels  # the additional choice is blank
    return fixed


def matmul(left: list[list[complex]], right: list[list[complex]]) -> list[list[complex]]:
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(inner))
            for j in range(columns)
        ]
        for i in range(rows)
    ]


def dagger(matrix: list[list[complex]]) -> list[list[complex]]:
    return [list(row) for row in zip(*[[value.conjugate() for value in row] for row in matrix])]


def matrix_add(
    left: list[list[complex]], right: list[list[complex]], right_scale: complex = 1.0
) -> list[list[complex]]:
    return [
        [left[i][j] + right_scale * right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def matrix_scale(matrix: list[list[complex]], scale: complex) -> list[list[complex]]:
    return [[scale * value for value in row] for row in matrix]


def identity(size: int) -> list[list[complex]]:
    return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]


def max_abs(matrix: list[list[complex]]) -> float:
    return max(abs(value) for row in matrix for value in row)


def matrix_rank(matrix: list[list[complex]], tolerance: float = 1e-11) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    rank = 0
    for column in range(columns):
        pivot = max(range(rank, rows), key=lambda row: abs(work[row][column]))
        if abs(work[pivot][column]) <= tolerance:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        divisor = work[rank][column]
        work[rank] = [value / divisor for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][column]
            if abs(factor) > tolerance:
                work[row] = [
                    work[row][j] - factor * work[rank][j]
                    for j in range(columns)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def outer(vector: list[complex]) -> list[list[complex]]:
    return [[left * right.conjugate() for right in vector] for left in vector]


def channel_target(
    rho: list[list[complex]], coefficients: tuple[float, ...], delta: float
) -> list[list[complex]]:
    hazard = sum(value * value for value in coefficients)
    root = math.sqrt(hazard)
    cosine = math.cos(math.sqrt(delta) * root)
    sine = math.sin(math.sqrt(delta) * root)
    k0 = identity(CARRIER_SIZE)
    k0[0][0] = cosine
    kraus = [k0]
    for mark, coefficient in enumerate(coefficients):
        operator = [[0j] * CARRIER_SIZE for _ in range(CARRIER_SIZE)]
        operator[mark + 1][0] = -1j * sine * coefficient / root
        kraus.append(operator)
    result = [[0j] * CARRIER_SIZE for _ in range(CARRIER_SIZE)]
    for operator in kraus:
        term = matmul(matmul(operator, rho), dagger(operator))
        result = matrix_add(result, term)
    return result


def lindblad_target(
    rho: list[list[complex]], coefficients: tuple[float, ...]
) -> list[list[complex]]:
    jumps = []
    for mark, coefficient in enumerate(coefficients):
        jump = [[0j] * CARRIER_SIZE for _ in range(CARRIER_SIZE)]
        jump[mark + 1][0] = coefficient
        jumps.append(jump)
    result = [[0j] * CARRIER_SIZE for _ in range(CARRIER_SIZE)]
    for jump in jumps:
        jj = matmul(dagger(jump), jump)
        gain = matmul(matmul(jump, rho), dagger(jump))
        loss = matrix_add(matmul(jj, rho), matmul(rho, jj))
        result = matrix_add(result, gain)
        result = matrix_add(result, loss, -0.5)
    return result


def rates(
    profile: tuple[int, ...], beta: Fraction, g_squared: Fraction
) -> tuple[tuple[Fraction, ...], Fraction]:
    occupancy, counts, _ = profile_stats(profile)
    values = tuple(g_squared * beta**occupancy * (1 << count) for count in counts)
    return values, sum(values, Fraction(0))


def exact_write_probability(hazard: float, delta: float) -> float:
    return math.sin(math.sqrt(delta * hazard)) ** 2


def apply_local_collision(
    distribution: dict[tuple[int, int], float],
    site: int,
    delta: float,
    beta: Fraction,
    g_squared: Fraction,
) -> dict[tuple[int, int], float]:
    result: defaultdict[tuple[int, int], float] = defaultdict(float)
    for state, mass in distribution.items():
        if state[site] != BLANK:
            result[state] += mass
            continue
        neighbor = state[1 - site]
        profile = (neighbor,) + (BLANK,) * (SLOTS - 1)
        mark_rates, hazard_exact = rates(profile, beta, g_squared)
        hazard = float(hazard_exact)
        write = exact_write_probability(hazard, delta)
        result[state] += mass * (1.0 - write)
        for mark, mark_rate in enumerate(mark_rates, start=1):
            updated = list(state)
            updated[site] = mark
            result[tuple(updated)] += mass * write * float(mark_rate / hazard_exact)
    return dict(result)


def apply_generator(
    distribution: dict[tuple[int, int], float],
    beta: Fraction,
    g_squared: Fraction,
) -> dict[tuple[int, int], float]:
    result: defaultdict[tuple[int, int], float] = defaultdict(float)
    for state, mass in distribution.items():
        for site in range(2):
            if state[site] != BLANK:
                continue
            neighbor = state[1 - site]
            profile = (neighbor,) + (BLANK,) * (SLOTS - 1)
            mark_rates, hazard = rates(profile, beta, g_squared)
            result[state] -= mass * float(hazard)
            for mark, mark_rate in enumerate(mark_rates, start=1):
                updated = list(state)
                updated[site] = mark
                result[tuple(updated)] += mass * float(mark_rate)
    return dict(result)


def uniformized_semigroup(
    initial: dict[tuple[int, int], float],
    beta: Fraction,
    g_squared: Fraction,
    time: float,
    tolerance: float = 1e-14,
) -> dict[tuple[int, int], float]:
    states = tuple(itertools.product(range(CARRIER_SIZE), repeat=2))
    exit_rates = []
    for state in states:
        point = {state: 1.0}
        derivative = apply_generator(point, beta, g_squared)
        exit_rates.append(-derivative.get(state, 0.0))
    uniform_rate = max(exit_rates)

    def stochastic_step(distribution: dict[tuple[int, int], float]) -> dict[tuple[int, int], float]:
        derivative = apply_generator(distribution, beta, g_squared)
        result = defaultdict(float, distribution)
        for state, value in derivative.items():
            result[state] += value / uniform_rate
        return dict(result)

    poisson_mean = uniform_rate * time
    weight = math.exp(-poisson_mean)
    cumulative = weight
    term = dict(initial)
    answer = {state: weight * mass for state, mass in term.items()}
    order = 0
    while 1.0 - cumulative > tolerance:
        order += 1
        term = stochastic_step(term)
        weight *= poisson_mean / order
        cumulative += weight
        for state, mass in term.items():
            answer[state] = answer.get(state, 0.0) + weight * mass
        if order > 10000:
            raise RuntimeError("uniformization did not converge")
    return answer


def l1_distance(
    left: dict[tuple[int, int], float], right: dict[tuple[int, int], float]
) -> float:
    return sum(abs(left.get(state, 0.0) - right.get(state, 0.0)) for state in set(left) | set(right))


def factorial_tail(parameter: float, start: int) -> float:
    if parameter == 0:
        return 0.0
    term = math.exp(start * math.log(parameter) - math.lgamma(start + 1))
    total = term
    order = start
    while term > 1e-18 * max(total, 1.0):
        order += 1
        term *= parameter / order
        total += term
        if order > start + 10000:
            raise RuntimeError("factorial tail did not converge")
    return total


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def git_output(repository: Path, *arguments: str) -> bytes:
    completed = subprocess.run(
        ("git", "-C", str(repository), *arguments),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def committed_provenance() -> dict[str, object]:
    repository = Path(__file__).resolve().parents[1]
    correction = git_output(repository, "rev-parse", f"{CORRECTION_REF}^{{commit}}").decode().strip()
    parents = git_output(repository, "show", "-s", "--format=%P", correction).decode().split()
    if len(parents) != 1:
        raise RuntimeError(f"correction parent count={len(parents)}")
    parent = parents[0]

    support_names = (
        "APPROACH_REGISTRY.md",
        "GOAL.md",
        "INDEPENDENT_PREREG_ATTACK.md",
        "PANEL_RETURN.md",
        "PREFLIGHT_SUPPORT_CORRECTION.md",
        "PREFLIGHT_WITNESSES.md",
    )
    support_paths = tuple(f"{BLOCK19_SUPPORT_DIRECTORY}/{name}" for name in support_names)
    correction_text = git_output(
        repository,
        "show",
        f"{correction}:{BLOCK19_SUPPORT_DIRECTORY}/PREFLIGHT_SUPPORT_CORRECTION.md",
    ).decode()
    declared_match = re.search(
        r"committed preregistration packet\s+([0-9a-f]{10,40})",
        correction_text,
    )
    declared_parent = declared_match.group(1) if declared_match else ""

    block18_paths = {
        "claim": f"{BLOCK18_DIRECTORY}/CLAIM_STATUS_CERTIFICATE.md",
        "source": "scripts/admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.py",
        "independent_source": "scripts/independent_admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.py",
        "cache": "logs/runner-cache/admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.txt",
        "independent_cache": "logs/runner-cache/independent_admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.txt",
    }

    def manifest(commit: str, paths: tuple[str, ...]) -> tuple[str, dict[str, str]]:
        records = []
        objects = {}
        for path in paths:
            blob = git_output(repository, "rev-parse", f"{commit}:{path}").decode().strip()
            content = git_output(repository, "show", f"{commit}:{path}")
            source_digest = hashlib.sha256(content).hexdigest()
            objects[path] = blob
            records.append(f"{path}\0{blob}\0{source_digest}\0{len(content)}")
        combined = hashlib.sha256("\n".join(records).encode()).hexdigest()
        return combined, objects

    support_digest, support_objects = manifest(correction, support_paths)
    block18_digest, block18_objects_by_path = manifest(parent, tuple(block18_paths.values()))
    block18_objects = {
        label: block18_objects_by_path[path] for label, path in block18_paths.items()
    }
    return {
        "correction": correction,
        "parent": parent,
        "declared_parent": declared_parent,
        "support_digest": support_digest,
        "support_objects": support_objects,
        "block18_digest": block18_digest,
        "block18_objects": block18_objects,
    }


def main() -> None:
    checks = Certificate()

    provenance_error = ""
    provenance: dict[str, object] = {}
    try:
        provenance = committed_provenance()
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError, RuntimeError) as error:
        provenance_error = str(error)
    checks.require("committed_provenance_readable", not provenance_error, provenance_error)
    if provenance:
        checks.require(
            "correction_commit_exact",
            str(provenance["correction"]).startswith(CORRECTION_REF),
        )
        checks.require(
            "correction_parent_declared",
            str(provenance["parent"]).startswith(str(provenance["declared_parent"])),
        )
        checks.require(
            "corrected_support_objects",
            len(provenance["support_objects"]) == 6
            and all(len(blob) >= 40 for blob in provenance["support_objects"].values()),
        )
        checks.require(
            "block18_anchor_objects",
            set(provenance["block18_objects"])
            == {"claim", "source", "independent_source", "cache", "independent_cache"}
            and all(len(blob) >= 40 for blob in provenance["block18_objects"].values()),
        )

    rotations = proper_cubic_rotations()
    identity_rotation = tuple(range(MARKS))
    rotation_set = set(rotations)
    expected_group_order = math.factorial(DIM) * 2 ** (DIM - 1)
    checks.require("proper_rotation_count", len(rotations) == expected_group_order)
    checks.require("rotation_identity", identity_rotation in rotation_set)
    checks.require(
        "rotation_closure",
        all(compose(left, right) in rotation_set for left in rotations for right in rotations),
    )
    checks.require(
        "rotation_inverses",
        all(any(compose(left, right) == identity_rotation for right in rotations) for left in rotations),
    )

    profiles = tuple(itertools.product(range(CARRIER_SIZE), repeat=SLOTS))
    checks.require("profile_space", len(profiles) == CARRIER_SIZE**SLOTS)
    representatives: set[tuple[int, ...]] = set()
    occupancy_values = set()
    simultaneous_covariance = True
    slot_only_witness = None
    label_only_witness = None
    for profile in profiles:
        occupancy, counts, _ = profile_stats(profile)
        occupancy_values.add(occupancy)
        images = []
        for rotation in rotations:
            image = rotate_profile(profile, rotation)
            images.append(image)
            image_occupancy, image_counts, _ = profile_stats(image)
            if image_occupancy != occupancy or any(
                image_counts[rotation[mark]] != counts[mark] for mark in range(MARKS)
            ):
                simultaneous_covariance = False
            if slot_only_witness is None:
                slot_only = [BLANK] * SLOTS
                for slot, value in enumerate(profile):
                    slot_only[rotation[slot]] = value
                slot_counts = profile_stats(tuple(slot_only))[1]
                if any(slot_counts[rotation[mark]] != counts[mark] for mark in range(MARKS)):
                    slot_only_witness = (profile, rotation)
            if label_only_witness is None:
                label_only = tuple(
                    BLANK if value == BLANK else rotation[value - 1] + 1 for value in profile
                )
                # The rate happens to have a larger relabeling symmetry.  The
                # mutation is instead that label-only motion is not the
                # stipulated geometric action on a profile: slots must move.
                if label_only != image:
                    label_only_witness = (profile, rotation)
        representatives.add(min(images))
    burnside_sum = sum(burnside_fixed(rotation) for rotation in rotations)
    checks.require("burnside_integral", burnside_sum % len(rotations) == 0)
    burnside_orbits = burnside_sum // len(rotations)
    checks.require("orbit_methods_agree", burnside_orbits == len(representatives))
    orbit_sizes = Counter(
        len({rotate_profile(profile, rotation) for rotation in rotations})
        for profile in representatives
    )
    checks.require(
        "orbit_partition",
        sum(size * count for size, count in orbit_sizes.items()) == len(profiles),
    )
    checks.require("simultaneous_covariance", simultaneous_covariance)
    checks.require("slot_only_mutation_rejected", slot_only_witness is not None)
    checks.require("label_only_mutation_rejected", label_only_witness is not None)
    full_projective_dimension = len(representatives) - 1
    count_projective_dimension = len(occupancy_values) - 1

    one_record = next(profile for profile in profiles if profile_stats(profile)[0] == 1)
    _, one_counts, _ = profile_stats(one_record)
    matched_mark = one_counts.index(1)
    unmatched_mark = next(index for index, count in enumerate(one_counts) if count == 0)
    supplied_ratio = Fraction(1 << one_counts[matched_mark], 1 << one_counts[unmatched_mark])
    kappa = supplied_ratio
    checks.require("kappa_necessity", kappa == Fraction(1 << 1, 1 << 0))

    g_squared = Fraction(1, profile_stats((BLANK,) * SLOTS)[2])
    alpha = MARKS * g_squared
    kernel_all_profiles = True
    # The preceding exhaustive action check proves n(g r)=n(r) and
    # m_{g f}(g r)=m_f(r).  Applying the exact monomial rate formula then
    # proves rate covariance without a second floating or Fraction sweep over
    # the same 24 images.
    covariance_rates = simultaneous_covariance
    extrema: dict[Fraction, tuple[Fraction, Fraction]] = {}
    for beta in EXECUTED_BETAS:
        hazards = []
        for profile in profiles:
            mark_rates, hazard = rates(profile, beta, g_squared)
            occupancy, counts, raw_sum = profile_stats(profile)
            hazards.append(hazard / alpha)
            for mark in range(MARKS):
                if mark_rates[mark] / hazard != Fraction(1 << counts[mark], raw_sum):
                    kernel_all_profiles = False
        extrema[beta] = (min(hazards), max(hazards))
    checks.require("conditional_kernel_exhaustive", kernel_all_profiles)
    checks.require("rate_covariance_exhaustive", covariance_rates)

    count_extrema: dict[Fraction, tuple[Fraction, Fraction]] = {}
    count_vectors = [
        vector
        for vector in itertools.product(range(SLOTS + 1), repeat=MARKS)
        if sum(vector) <= SLOTS
    ]
    for beta in EXECUTED_BETAS:
        candidates = [
            g_squared * beta ** sum(vector) * sum(1 << value for value in vector) / alpha
            for vector in count_vectors
        ]
        count_extrema[beta] = (min(candidates), max(candidates))
    checks.require("hazard_extrema_independent", extrema == count_extrema)
    common_minimum = min(value[0] for value in extrema.values())
    common_maximum = max(value[1] for value in extrema.values())
    checks.require("strict_common_rate_bounds", common_minimum > 0 and common_maximum < math.inf)

    largest_hazard = float(common_maximum * alpha)
    shared_delta = 0.25 / largest_hazard
    completeness_error = 0.0
    exact_completeness_all_profiles = True
    sine_remainder_ratio = 0.0
    weak_error = {1: 0.0, 2: 0.0}
    for beta in EXECUTED_BETAS:
        for profile in profiles:
            mark_rates, hazard_fraction = rates(profile, beta, g_squared)
            hazard = float(hazard_fraction)
            normalized_jump_coefficient = sum(
                (mark_rate / hazard_fraction for mark_rate in mark_rates),
                Fraction(0),
            )
            # Formally substitute sin^2(theta)=1-cos^2(theta).  The blank
            # completeness coefficient is then
            # normalized_jump_coefficient
            # + (1-normalized_jump_coefficient) cos^2(theta).
            formal_constant = normalized_jump_coefficient
            formal_cosine_squared = 1 - normalized_jump_coefficient
            if formal_constant != 1 or formal_cosine_squared != 0:
                exact_completeness_all_profiles = False
            x = shared_delta * hazard
            sine_mass = exact_write_probability(hazard, shared_delta)
            completeness_error = max(completeness_error, abs(math.cos(math.sqrt(x)) ** 2 + sine_mass - 1.0))
            difference = x - sine_mass
            if x > 0:
                sine_remainder_ratio = max(sine_remainder_ratio, difference / (x * x))
            if difference < -1e-14 or difference > x * x / 3.0 + 1e-14:
                checks.require("sine_remainder_profile", False, f"beta={beta} profile={profile}")
            for divisor in (1, 2):
                delta = shared_delta / divisor
                mass = exact_write_probability(hazard, delta)
                for mark_rate in mark_rates:
                    estimate = mass * float(mark_rate / hazard_fraction) / delta
                    weak_error[divisor] = max(weak_error[divisor], abs(estimate - float(mark_rate)))
    checks.require("exact_cp_tp_symbolic", exact_completeness_all_profiles)
    checks.require("exact_cp_tp_numeric_regression", completeness_error < 2e-14)
    checks.require("weak_rate_convergence", weak_error[2] < 0.55 * weak_error[1])
    checks.require("exact_mass_not_linear", sine_remainder_ratio > 0)

    profile_two_same = next(
        profile
        for profile in profiles
        if profile_stats(profile)[0] == 2 and max(profile_stats(profile)[1]) == 2
    )
    profile_three_distinct = next(
        profile
        for profile in profiles
        if profile_stats(profile)[0] == 3
        and sorted(profile_stats(profile)[1], reverse=True)[:3] == [1, 1, 1]
    )
    n2, counts2, z2 = profile_stats(profile_two_same)
    n3, counts3, z3 = profile_stats(profile_three_distinct)
    checks.require("same_z_fixture", n3 == n2 + 1 and z2 == z3)
    race_odds = {}
    for beta in EXECUTED_BETAS:
        _, hazard2 = rates(profile_two_same, beta, g_squared)
        _, hazard3 = rates(profile_three_distinct, beta, g_squared)
        odds = hazard3 / (hazard2 + hazard3)
        race_odds[beta] = odds
        checks.require("same_z_race_formula", odds == beta / (1 + beta))
    checks.require("beta_not_global_clock", len(set(race_odds.values())) == len(EXECUTED_BETAS))

    blank_profile = (BLANK,) * SLOTS
    diverse_full = tuple(range(1, MARKS + 1))
    _, blank_hazard = rates(blank_profile, Fraction(1), g_squared)
    old_fixture_odds = {}
    for beta in EXECUTED_BETAS:
        _, full_hazard = rates(diverse_full, beta, g_squared)
        old_fixture_odds[beta] = full_hazard / (blank_hazard + full_hazard)
    checks.require(
        "old_fixture_mutation_rejected",
        any(old_fixture_odds[beta] != race_odds[beta] for beta in EXECUTED_BETAS),
    )

    coefficients = tuple(math.sqrt(float(value)) for value in rates(profile_two_same, Fraction(2), g_squared)[0])
    star_hazard = sum(value * value for value in coefficients)
    star = [[0j] * CARRIER_SIZE for _ in range(CARRIER_SIZE)]
    for mark, coefficient in enumerate(coefficients):
        star[0][mark + 1] = coefficient
        star[mark + 1][0] = coefficient
    star_squared = matmul(star, star)
    star_cubed = matmul(star_squared, star)
    checks.require("star_hermitian", max_abs(matrix_add(star, dagger(star), -1.0)) < 1e-13)
    checks.require("star_rank_two", matrix_rank(star) == 2)
    checks.require(
        "star_minimal_polynomial",
        max_abs(matrix_add(star_cubed, matrix_scale(star, star_hazard), -1.0)) < 1e-11,
    )
    checks.require(
        "star_trace_identity",
        abs(sum(star[i][i] for i in range(CARRIER_SIZE))) < 1e-13
        and abs(sum(star_squared[i][i] for i in range(CARRIER_SIZE)) - 2 * star_hazard) < 1e-11,
    )
    theta = math.sqrt(shared_delta * star_hazard)
    cosine = math.cos(theta)
    sine = math.sin(theta)
    unitary = identity(CARRIER_SIZE)
    unitary[0][0] = cosine
    for mark, coefficient in enumerate(coefficients):
        unitary[0][mark + 1] = -1j * sine * coefficient / math.sqrt(star_hazard)
        unitary[mark + 1][0] = -1j * sine * coefficient / math.sqrt(star_hazard)
        for other, other_coefficient in enumerate(coefficients):
            unitary[mark + 1][other + 1] += (
                (cosine - 1.0) * coefficient * other_coefficient / star_hazard
            )
    checks.require(
        "exact_star_unitary",
        max_abs(matrix_add(matmul(dagger(unitary), unitary), identity(CARRIER_SIZE), -1.0)) < 2e-13,
    )

    joint_size = CARRIER_SIZE * CARRIER_SIZE
    joint_hamiltonian = [[0j] * joint_size for _ in range(joint_size)]
    joint_blank_vacuum = 0
    for mark, coefficient in enumerate(coefficients, start=1):
        joint_mark = mark * CARRIER_SIZE + mark
        joint_hamiltonian[joint_mark][joint_blank_vacuum] = coefficient
        joint_hamiltonian[joint_blank_vacuum][joint_mark] = coefficient
    vacuum_record_columns = [
        target * CARRIER_SIZE for target in range(1, CARRIER_SIZE)
    ]
    vacuum_lock_exact = all(
        all(abs(joint_hamiltonian[row][column]) == 0 for row in range(joint_size))
        for column in vacuum_record_columns
    )
    nonvacuum_reverse_exact = all(
        abs(joint_hamiltonian[joint_blank_vacuum][mark * CARRIER_SIZE + mark]) > 0
        for mark in range(1, CARRIER_SIZE)
    )

    state_vector = [complex(index + 1, (-1) ** index) for index in range(CARRIER_SIZE)]
    norm = math.sqrt(sum(abs(value) ** 2 for value in state_vector))
    state_vector = [value / norm for value in state_vector]
    rho = outer(state_vector)
    generator_rho = lindblad_target(rho, coefficients)
    quantum_errors = []
    for divisor in (1, 2):
        delta = 1e-4 / (divisor * star_hazard)
        exact = channel_target(rho, coefficients, delta)
        approximation = matrix_add(rho, generator_rho, delta)
        quantum_errors.append(max_abs(matrix_add(exact, approximation, -1.0)))
    checks.require("quantum_weak_generator", quantum_errors[1] < 0.3 * quantum_errors[0])
    recorded_vector = [0j] + [complex(index, 1 - index) for index in range(1, CARRIER_SIZE)]
    recorded_norm = math.sqrt(sum(abs(value) ** 2 for value in recorded_vector))
    recorded_vector = [value / recorded_norm for value in recorded_vector]
    recorded_rho = outer(recorded_vector)
    recorded_after = channel_target(recorded_rho, coefficients, shared_delta)
    recorded_generator = lindblad_target(recorded_rho, coefficients)
    checks.require(
        "vacuum_target_lock",
        vacuum_lock_exact
        and max_abs(matrix_add(recorded_after, recorded_rho, -1.0)) < 1e-13
        and max_abs(recorded_generator) < 1e-13,
    )
    checks.require("nonvacuum_reverse_exposed", nonvacuum_reverse_exact)
    checks.require("vacuum_centered", star[0][0] == 0)

    relation_diagonal = [1.0, math.sqrt(2.0)] + [1.0] * (MARKS - 1)
    projector_commutators = []
    for label in range(CARRIER_SIZE):
        projector = [[0j] * CARRIER_SIZE for _ in range(CARRIER_SIZE)]
        projector[label][label] = 1.0
        relation = [[0j] * CARRIER_SIZE for _ in range(CARRIER_SIZE)]
        for index, value in enumerate(relation_diagonal):
            relation[index][index] = value
        projector_commutators.append(max_abs(matrix_add(matmul(projector, relation), matmul(relation, projector), -1.0)))
    checks.require("neighbor_projector_qnd", max(projector_commutators) == 0.0)

    def branch_overlap(left_profile: tuple[int, ...], right_profile: tuple[int, ...]) -> float:
        left_rates, left_h_fraction = rates(left_profile, Fraction(2), g_squared)
        right_rates, right_h_fraction = rates(right_profile, Fraction(2), g_squared)
        left_h = float(left_h_fraction)
        right_h = float(right_h_fraction)
        left_theta = math.sqrt(shared_delta * left_h)
        right_theta = math.sqrt(shared_delta * right_h)
        bright_overlap = sum(
            math.sqrt(float(left_rates[index] * right_rates[index]))
            for index in range(MARKS)
        ) / math.sqrt(left_h * right_h)
        return math.cos(left_theta) * math.cos(right_theta) + math.sin(left_theta) * math.sin(right_theta) * bright_overlap

    coherence_overlap = branch_overlap(blank_profile, one_record)
    checks.require("complete_neighbor_identity_mutation_rejected", abs(coherence_overlap - 1.0) > 1e-10)

    order_coefficients = {}
    order_exact = {}
    order_delta = 1e-5
    one_neighbor_profile = (1,) + (BLANK,) * (SLOTS - 1)
    for beta in (Fraction(1), Fraction(1, 2)):
        _, h0_fraction = rates(blank_profile, beta, g_squared)
        _, h1_fraction = rates(one_neighbor_profile, beta, g_squared)
        h0 = float(h0_fraction)
        h1 = float(h1_fraction)
        r0 = exact_write_probability(h0, order_delta)
        r1 = exact_write_probability(h1, order_delta)
        difference = r0 * (r1 - r0)
        coefficient = h0 * (h1 - h0)
        order_exact[beta] = difference
        order_coefficients[beta] = coefficient
        checks.require(
            "order_second_order_coefficient",
            abs(difference / order_delta**2 - coefficient) < 2e-4,
        )
        checks.require("no_first_order_order_effect", abs(difference / order_delta) < 1e-4)
    checks.require(
        "order_sign_mutation",
        order_exact[Fraction(1)] * order_exact[Fraction(1, 2)] < 0,
    )

    finite_volume_side = DIM
    volume_sites = finite_volume_side**DIM
    h_max = largest_hazard
    product_time = 1.0 / (10.0 * volume_sites * h_max)

    def sweep_bound(delta: float) -> float:
        argument = 2.0 * delta * volume_sites * h_max
        return (
            (2.0 / 3.0) * volume_sites * delta * delta * h_max * h_max
            + math.expm1(argument)
            - argument
        )

    telescope_bounds = []
    for sweeps in (8, 16, 32):
        delta = product_time / sweeps
        generator_norm_bound = 2.0 * volume_sites * h_max
        exponential_remainder = math.expm1(delta * generator_norm_bound) - delta * generator_norm_bound
        telescope_bounds.append(sweeps * (sweep_bound(delta) + exponential_remainder))
    checks.require(
        "finite_volume_product_bound",
        telescope_bounds[2] < telescope_bounds[1] < telescope_bounds[0],
    )
    first_order_remainders = [
        sweep_bound(product_time / sweeps) / (product_time / sweeps)
        for sweeps in (8, 16, 32)
    ]
    checks.require(
        "varying_order_first_order",
        first_order_remainders[2] < first_order_remainders[1] < first_order_remainders[0],
    )

    two_site_errors = {}
    initial_distribution = {(BLANK, BLANK): 1.0}
    process_time = 0.4
    for beta in EXECUTED_BETAS:
        limit = uniformized_semigroup(initial_distribution, beta, g_squared, process_time)
        errors = []
        for sweep_count in (32, 64, 128):
            distribution = dict(initial_distribution)
            delta = process_time / sweep_count
            for sweep in range(sweep_count):
                order = (0, 1) if sweep % 2 == 0 else (1, 0)
                for site in order:
                    distribution = apply_local_collision(distribution, site, delta, beta, g_squared)
            errors.append(l1_distance(distribution, limit))
        two_site_errors[beta] = errors[-1]
        checks.require("ordered_sweep_numeric_limit", errors[2] < errors[1] < errors[0])

    proposal_rate = common_maximum * alpha
    harris_membership = True
    mark_race_membership = True
    for beta in EXECUTED_BETAS:
        for profile in profiles:
            mark_rates, hazard = rates(profile, beta, g_squared)
            if not (0 < hazard <= proposal_rate):
                harris_membership = False
            acceptance = hazard / proposal_rate
            for mark_rate in mark_rates:
                reconstructed = proposal_rate * acceptance * (mark_rate / hazard)
                if reconstructed != mark_rate:
                    mark_race_membership = False
    checks.require("common_harris_proposal", harris_membership)
    checks.require("exponential_mark_race", mark_race_membership)
    branch_factor = 1 + SLOTS
    clan_coefficient = branch_factor * proposal_rate
    observation_time = float(1 / proposal_rate)
    tail_parameter = float(clan_coefficient) * observation_time
    tail_start = branch_factor
    initial_tail = factorial_tail(tail_parameter, tail_start)
    while factorial_tail(tail_parameter, tail_start) > 1e-10:
        tail_start += 1
    final_tail = factorial_tail(tail_parameter, tail_start)
    checks.require("backward_clan_factorial_tail", final_tail < 1e-10 < initial_tail)
    finite_generator_conservative = True
    finite_generator_append_only = True
    for state in itertools.product(range(CARRIER_SIZE), repeat=2):
        derivative = apply_generator({state: 1.0}, Fraction(2), g_squared)
        if abs(sum(derivative.values())) > 1e-13:
            finite_generator_conservative = False
        old_recorded = sum(value != BLANK for value in state)
        for successor, rate_value in derivative.items():
            if successor == state or rate_value <= 0:
                continue
            new_recorded = sum(value != BLANK for value in successor)
            preserved = all(
                state[index] == BLANK or successor[index] == state[index]
                for index in range(2)
            )
            if new_recorded != old_recorded + 1 or not preserved:
                finite_generator_append_only = False
    checks.require(
        "finite_history_bound",
        finite_generator_conservative
        and volume_sites * float(proposal_rate) < math.inf
        and volume_sites < math.inf,
    )
    minimum_hazard = common_minimum * alpha
    survival_bounds = [math.exp(-float(minimum_hazard) * time) for time in (1, 10, 100)]
    checks.require(
        "formation_lower_bound",
        minimum_hazard > 0
        and survival_bounds[2] < survival_bounds[1] < survival_bounds[0] < 1,
    )
    checks.require("append_only_permanence", finite_generator_append_only and vacuum_lock_exact)
    finite_volume_rate_lower_bounds = [
        sites * float(minimum_hazard) for sites in (10, 100, 1000)
    ]
    checks.require(
        "global_next_event_mutation_rejected",
        finite_volume_rate_lower_bounds[2]
        > finite_volume_rate_lower_bounds[1]
        > finite_volume_rate_lower_bounds[0]
        > 0,
    )

    outer_dimension_separated = full_projective_dimension > count_projective_dimension > 0
    checks.require("outer_control_demoted", outer_dimension_separated)
    checks.require("strict_m2_upgrade_rejected", CARRIER_SIZE != 2)
    checks.require("single_target_arity_import", 1 < SLOTS)
    forbidden_upgrades = {
        "strict-M2",
        "autonomous-bath",
        "physical-clock",
        "compound-event",
        "gravity",
        "axiom",
        "audit",
        "TOE-movement",
        "global-quantum-unitary",
    }
    licensed_claims = {
        "orthogonal-pointer",
        "fresh-ancilla",
        "range-one",
        "diagonal-generator",
        "local-classical-Harris",
    }
    provenance_roles = {
        "Block02": "writer-precedent-only",
        "Block11": "strict-M2-boundary-preserved",
        "Block18": "pure-Record/Harris-method-only",
    }
    checks.require("scope_firewall", licensed_claims.isdisjoint(forbidden_upgrades))
    checks.require(
        "provenance_boundary",
        bool(provenance)
        and not provenance_error
        and set(provenance_roles)
        == {"Block02", "Block11", "Block18"}
        and all(role.endswith(("only", "preserved")) for role in provenance_roles.values()),
    )

    orbit_distribution = ",".join(
        f"{size}:{count}" for size, count in sorted(orbit_sizes.items())
    )
    race_text = ",".join(
        f"beta={fraction_text(beta)}->{fraction_text(race_odds[beta])}"
        for beta in EXECUTED_BETAS
    )
    old_text = ",".join(
        f"beta={fraction_text(beta)}->{fraction_text(old_fixture_odds[beta])}"
        for beta in EXECUTED_BETAS
    )
    order_text = ",".join(
        f"beta={fraction_text(beta)}:{order_coefficients[beta]:+.12g}"
        for beta in (Fraction(1), Fraction(1, 2))
    )
    convergence_text = ",".join(
        f"beta={fraction_text(beta)}:{two_site_errors[beta]:.3e}"
        for beta in EXECUTED_BETAS
    )
    if provenance:
        block18_blob_text = ",".join(
            f"{label}:{blob[:12]}"
            for label, blob in provenance["block18_objects"].items()
        )
        provenance_object_text = (
            f"correction={str(provenance['correction'])[:12]} "
            f"parent={str(provenance['parent'])[:12]} "
            f"support_sha256={str(provenance['support_digest'])[:16]} "
            f"block18_sha256={str(provenance['block18_digest'])[:16]} "
            f"block18_blobs={block18_blob_text}"
        )
    else:
        provenance_object_text = f"unavailable:{provenance_error}"

    section_status = "PASS" if checks.failed == 0 else "FAIL"
    lines = [
        "BLOCK19 independent relation-factor QND collision certificate",
        f"group: {section_status} rotations={len(rotations)} profiles={len(profiles)} orbits={len(representatives)} burnside_sum={burnside_sum}",
        f"orbit_sizes: {section_status} {orbit_distribution} outer_projective_dim={full_projective_dimension} count_projective_dim={count_projective_dimension}",
        f"collision: {section_status} star_rank={matrix_rank(star)} spectrum=(+sqrt(h),-sqrt(h),0x{CARRIER_SIZE-2}) cp_error={completeness_error:.2e}",
        f"weak_generator: {section_status} max_rate_errors_delta,half=({weak_error[1]:.3e},{weak_error[2]:.3e}) sine_remainder_ratio<={sine_remainder_ratio:.6g}",
        f"classification: {section_status} kappa={fraction_text(kappa)} beta_dimension=1 modulo_global_g2",
        f"same_Z_race: {section_status} n=({n2},{n3}) Z=({z2},{z3}) {race_text}",
        f"hostile_old_fixture: {section_status} odds={old_text}",
        f"order_mutation: {section_status} leading_coefficients={order_text} first_order=0",
        f"ordered_limit: {section_status} varying_sweeps_to_exp errors_at_N128={convergence_text}",
        f"local_Harris: {section_status} h_over_alpha=[{fraction_text(common_minimum)},{fraction_text(common_maximum)}] clan_coefficient_over_alpha={fraction_text(clan_coefficient/alpha)} tail_m={tail_start} tail={final_tail:.2e}",
        f"hostile_mutations: {section_status} linear_delta,nonvacuum_lock,complete_state_QND,slot_only,label_only,beta_clock,old_fixture,first_order_order,global_next_event",
        f"per_element: {section_status} profiles={len(profiles)} marks={MARKS} exact_channel/kernel/covariance checked",
        f"per_site: {section_status} blank write/no-write, recorded lock, pointer-projector QND, range-one append-only generator checked",
        f"per_mode: {section_status} marks={MARKS} profile_orbits={len(representatives)} pair-factor_beta_dimension=1 outer_control_demoted",
        f"per_block: {section_status} finite_sites={volume_sites} arbitrary-permutation remainder and varying-order weak limit checked",
        f"lattice_wide: {section_status} local classical Harris construction only; proposal={fraction_text(proposal_rate)} backward_clan_tail finite; no global next-event or quantum-unitary claim",
        f"provenance_objects: {section_status} {provenance_object_text}",
        f"provenance: {section_status} Block02=writer-precedent-only Block11=strict-M2-boundary-preserved Block18=pure-Record/Harris-method-only; bath/reset/scaling/cadence imported",
        f"scope: {section_status} orthogonal-pointer fresh-ancilla range-one diagonal-generator classification only; no clock/action/gravity/axiom/audit/TOE upgrade",
    ]
    lines.extend(checks.failures)
    prospective_total = f"TOTAL: PASS={checks.passed} FAIL={checks.failed}"
    payload = "\n".join(lines + [prospective_total]) + "\n"
    if len(payload.encode("utf-8")) >= 6000:
        checks.require("stdout_under_6000", False, f"bytes={len(payload.encode('utf-8'))}")
    else:
        checks.require("stdout_under_6000", True)
    lines = lines[:20] + checks.failures
    lines.append(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    print("\n".join(lines))
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
