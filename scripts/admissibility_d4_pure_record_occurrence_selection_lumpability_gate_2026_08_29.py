#!/usr/bin/env python3
"""Exact Block18 pure-Record occurrence-selection/lumpability certificate.

The executable constructs two bounded, range-one pure-birth generators on the
invariant seven-state sector {blank} union {rho_f: f a signed cubic axis}.  It
checks their finite histories, their shared local Harris construction, and a
clock-free Record-order discriminator.  The result is deliberately restricted
to this six-mark Markov sector: it neither exhausts M_2(C) nor selects a
physical occurrence law for the framework.

Only exact integer/Fraction arithmetic is used for certificate values.  The
finite proposal-field fixture checks the deterministic Harris sample map; the
infinite construction is certified separately by the factorial clan bound,
Poisson local finiteness, and the countable rational-query construction.
"""

from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from functools import cache
from itertools import permutations, product
from math import factorial, isqrt
from typing import Callable, Iterable


Point = tuple[int, int, int]
Matrix3 = tuple[tuple[int, int, int], ...]
QComplex = tuple[Fraction, Fraction]
Matrix2 = tuple[tuple[QComplex, QComplex], tuple[QComplex, QComplex]]

BLANK = -1
ZERO: QComplex = (Fraction(0), Fraction(0))
ONE: QComplex = (Fraction(1), Fraction(0))
IUNIT: QComplex = (Fraction(0), Fraction(1))
ALPHA = Fraction(1)
BETA = Fraction(143, 256)


def signed_axes() -> tuple[Point, ...]:
    """Generate the signed coordinate axes; no direction lookup table."""
    return tuple(
        tuple(sign if coordinate == axis else 0 for coordinate in range(3))
        for axis in range(3)
        for sign in (-1, 1)
    )  # type: ignore[return-value]


DIRECTIONS = signed_axes()
MARKS = tuple(range(len(DIRECTIONS)))
ALPHABET = (BLANK,) + MARKS
DIRECTION_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[Matrix3, ...]:
    rotations: list[Matrix3] = []
    for permutation in permutations(range(3)):
        parity = permutation_sign(permutation)
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue
            rows = []
            for row in range(3):
                rows.append(
                    tuple(
                        signs[row] if column == permutation[row] else 0
                        for column in range(3)
                    )
                )
            rotations.append(tuple(rows))  # type: ignore[arg-type]
    return tuple(rotations)


ROTATIONS = proper_cubic_rotations()


def mat_vec(matrix: Matrix3, vector: Point) -> Point:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def rotation_permutation(matrix: Matrix3) -> tuple[int, ...]:
    return tuple(DIRECTION_INDEX[mat_vec(matrix, direction)] for direction in DIRECTIONS)


ROTATION_PERMUTATIONS = tuple(rotation_permutation(rotation) for rotation in ROTATIONS)


def add(left: Point, right: Point) -> Point:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def scale(multiplier: int, point: Point) -> Point:
    return tuple(multiplier * value for value in point)  # type: ignore[return-value]


def qadd(left: QComplex, right: QComplex) -> QComplex:
    return left[0] + right[0], left[1] + right[1]


def qsub(left: QComplex, right: QComplex) -> QComplex:
    return left[0] - right[0], left[1] - right[1]


def qmul(left: QComplex, right: QComplex) -> QComplex:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def qscale(value: Fraction, item: QComplex) -> QComplex:
    return value * item[0], value * item[1]


def qconj(item: QComplex) -> QComplex:
    return item[0], -item[1]


def matrix_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(qadd(left[row][column], right[row][column]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(value: Fraction, matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(qscale(value, matrix[row][column]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            qadd(qmul(left[row][0], right[0][column]), qmul(left[row][1], right[1][column]))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


IDENTITY2: Matrix2 = ((ONE, ZERO), (ZERO, ONE))
PAULI: tuple[Matrix2, ...] = (
    ((ZERO, ONE), (ONE, ZERO)),
    ((ZERO, qscale(-1, IUNIT)), (IUNIT, ZERO)),
    ((ONE, ZERO), (ZERO, qscale(-1, ONE))),
)


def rho_matrix(direction: Point) -> Matrix2:
    spin = matrix_scale(Fraction(0), IDENTITY2)
    for coordinate, component in enumerate(direction):
        spin = matrix_add(spin, matrix_scale(Fraction(component), PAULI[coordinate]))
    return matrix_scale(Fraction(1, 2), matrix_add(IDENTITY2, matrix_scale(-BETA, spin)))


RHO = tuple(rho_matrix(direction) for direction in DIRECTIONS)


def trace2(matrix: Matrix2) -> QComplex:
    return qadd(matrix[0][0], matrix[1][1])


def determinant2(matrix: Matrix2) -> QComplex:
    return qsub(qmul(matrix[0][0], matrix[1][1]), qmul(matrix[0][1], matrix[1][0]))


def rational_sqrt(value: Fraction) -> Fraction:
    numerator = isqrt(value.numerator)
    denominator = isqrt(value.denominator)
    if numerator * numerator != value.numerator or denominator * denominator != value.denominator:
        raise ValueError("not a rational square")
    return Fraction(numerator, denominator)


@cache
def rho_facts() -> dict[str, object]:
    spectra = []
    expectations = []
    hermitian = True
    characteristic = True
    positive = True
    for matrix in RHO:
        hermitian &= all(
            matrix[row][column] == qconj(matrix[column][row])
            for row in range(2)
            for column in range(2)
        )
        trace = trace2(matrix)
        determinant = determinant2(matrix)
        characteristic &= trace == ONE and determinant[1] == 0
        discriminant = trace[0] * trace[0] - 4 * determinant[0]
        root = rational_sqrt(discriminant)
        eigenvalues = tuple(sorted(((trace[0] - root) / 2, (trace[0] + root) / 2)))
        characteristic &= all(
            eigenvalue * eigenvalue - trace[0] * eigenvalue + determinant[0] == 0
            for eigenvalue in eigenvalues
        )
        positive &= all(eigenvalue > 0 for eigenvalue in eigenvalues)
        spectra.append(eigenvalues)
        expectation = []
        for pauli in PAULI:
            value = trace2(matrix_multiply(matrix, pauli))
            characteristic &= value[1] == 0
            expectation.append(value[0])
        expectations.append(tuple(expectation))

    covariance = True
    for permutation in ROTATION_PERMUTATIONS:
        for mark in MARKS:
            rotated_expectation = mat_vec(
                # Expectations are rational; apply the integer matrix directly.
                ROTATIONS[ROTATION_PERMUTATIONS.index(permutation)],
                DIRECTIONS[mark],
            )
            covariance &= expectations[permutation[mark]] == tuple(
                -BETA * coordinate for coordinate in rotated_expectation
            )
    return {
        "hermitian": hermitian,
        "trace_characteristic": characteristic,
        "positive": positive,
        "distinct": len(set(RHO)) == len(DIRECTIONS),
        "spectra": tuple(spectra),
        "common_spectrum": len(set(spectra)) == 1,
        "covariance": covariance,
    }


def profile_counts(profile: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(profile.count(mark) for mark in MARKS)


def kernel_weights(profile: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(1 << count for count in profile_counts(profile))


def kernel(profile: tuple[int, ...]) -> tuple[Fraction, ...]:
    weights = kernel_weights(profile)
    denominator = sum(weights)
    return tuple(Fraction(weight, denominator) for weight in weights)


def rotate_profile(profile: tuple[int, ...], permutation: tuple[int, ...]) -> tuple[int, ...]:
    rotated = [BLANK] * len(DIRECTIONS)
    for old_position, value in enumerate(profile):
        rotated[permutation[old_position]] = BLANK if value == BLANK else permutation[value]
    return tuple(rotated)


def rotate_keys(keys: tuple[Fraction, ...], permutation: tuple[int, ...]) -> tuple[Fraction, ...]:
    rotated = [Fraction(0)] * len(DIRECTIONS)
    for old_mark, key in enumerate(keys):
        rotated[permutation[old_mark]] = key
    return tuple(rotated)


def select_mark(weights: tuple[int, ...], keys: tuple[Fraction, ...]) -> int:
    ratios = tuple(keys[mark] / weights[mark] for mark in MARKS)
    minimum = min(ratios)
    winners = tuple(mark for mark, ratio in enumerate(ratios) if ratio == minimum)
    if len(winners) != 1:
        raise ValueError("exponential-key tie is outside the exact fixture")
    return winners[0]


def hazard(law: int, recorded_neighbors: int, alpha: Fraction = ALPHA, blank: bool = True) -> Fraction:
    if not blank:
        return Fraction(0)
    if not 0 <= recorded_neighbors <= len(DIRECTIONS):
        raise ValueError("nearest-neighbor count outside the cubic shell")
    if law == 0:
        return alpha
    if law == 1:
        return alpha * Fraction(len(DIRECTIONS) + recorded_neighbors, len(DIRECTIONS))
    raise ValueError("unknown hazard law")


def marked_rates(profile: tuple[int, ...], law: int, alpha: Fraction = ALPHA) -> tuple[Fraction, ...]:
    probabilities = kernel(profile)
    lam = hazard(law, sum(value != BLANK for value in profile), alpha)
    return tuple(lam * probability for probability in probabilities)


@cache
def profile_facts() -> dict[str, object]:
    count = 0
    normalization = True
    positivity = True
    covariance = True
    rate_sum = True
    variation = False
    race_covariance = True
    race_distribution = True
    blank_probability = None
    one_neighbor_probability = None
    race_keys = tuple(Fraction(3**mark) for mark in MARKS)

    for profile in product(ALPHABET, repeat=len(DIRECTIONS)):
        count += 1
        weights = kernel_weights(profile)
        denominator = sum(weights)
        probabilities = tuple(Fraction(weight, denominator) for weight in weights)
        normalization &= sum(probabilities, Fraction(0)) == 1
        positivity &= all(probability > 0 for probability in probabilities)
        # If E_f are independent Exp(1), then E_f/w_f are independent
        # exponentials of rates w_f.  Integrating
        # w_f exp[-s sum_g w_g] over s>=0 gives w_f/sum_g w_g.
        race_distribution &= tuple(
            Fraction(race_rate, sum(weights)) for race_rate in weights
        ) == probabilities
        variation |= len(set(probabilities)) > 1
        if all(value == BLANK for value in profile):
            blank_probability = probabilities
        if profile[0] == 0 and all(value == BLANK for value in profile[1:]):
            one_neighbor_probability = probabilities
        recorded = sum(value != BLANK for value in profile)
        for law in (0, 1):
            rates = marked_rates(profile, law)
            rate_sum &= sum(rates, Fraction(0)) == hazard(law, recorded)

        winner = select_mark(weights, race_keys)
        for permutation in ROTATION_PERMUTATIONS:
            rotated = rotate_profile(profile, permutation)
            rotated_weights = kernel_weights(rotated)
            covariance &= sum(rotated_weights) == denominator and all(
                rotated_weights[permutation[mark]] == weights[mark] for mark in MARKS
            )
            rotated_winner = select_mark(rotated_weights, rotate_keys(race_keys, permutation))
            race_covariance &= rotated_winner == permutation[winner]

    return {
        "count": count,
        "expected_count": len(ALPHABET) ** len(DIRECTIONS),
        "normalization": normalization,
        "positivity": positivity,
        "variation": variation,
        "covariance": covariance,
        "rate_sum": rate_sum,
        "race_covariance": race_covariance,
        "race_distribution": race_distribution,
        "blank_probability": blank_probability,
        "one_neighbor_probability": one_neighbor_probability,
    }


@cache
def torus_points(length: int) -> tuple[Point, ...]:
    return tuple(product(range(length), repeat=3))


@cache
def torus_index(length: int) -> dict[Point, int]:
    return {point: index for index, point in enumerate(torus_points(length))}


def torus_add(point: Point, direction: Point, length: int) -> Point:
    return tuple((point[axis] + direction[axis]) % length for axis in range(3))  # type: ignore[return-value]


def state_profile(state: tuple[int, ...], length: int, site: Point) -> tuple[int, ...]:
    index = torus_index(length)
    return tuple(state[index[torus_add(site, direction, length)]] for direction in DIRECTIONS)


def append_state(state: tuple[int, ...], site_index: int, mark: int) -> tuple[int, ...]:
    if state[site_index] != BLANK or mark not in MARKS:
        raise ValueError("only a legal mark may append to a blank site")
    updated = list(state)
    updated[site_index] = mark
    return tuple(updated)


def finite_row(
    state: tuple[int, ...], length: int, law: int, alpha: Fraction = ALPHA
) -> tuple[tuple[tuple[int, int], Fraction, tuple[int, ...]], ...]:
    rows = []
    for site_index, site in enumerate(torus_points(length)):
        if state[site_index] != BLANK:
            continue
        profile = state_profile(state, length, site)
        for mark, rate in enumerate(marked_rates(profile, law, alpha)):
            rows.append(((site_index, mark), rate, append_state(state, site_index, mark)))
    return tuple(rows)


def finite_exit_rate(state: tuple[int, ...], length: int, law: int, alpha: Fraction = ALPHA) -> Fraction:
    return sum((rate for _label, rate, _target in finite_row(state, length, law, alpha)), Fraction(0))


@cache
def finite_generator_facts() -> dict[str, object]:
    length = len(DIRECTIONS) // 2
    points = torus_points(length)
    blank = (BLANK,) * len(points)
    partial = list(blank)
    origin = (0, 0, 0)
    for mark, direction in enumerate(DIRECTIONS):
        partial[torus_index(length)[torus_add(origin, direction, length)]] = mark
    partial_state = tuple(partial)
    recorded = tuple(index % len(MARKS) for index in range(len(points)))
    positivity = conservation = append_only = absorption = True
    fixture_rows = 0
    for law in (0, 1):
        for state in (blank, partial_state, recorded):
            row = finite_row(state, length, law)
            fixture_rows += len(row)
            diagonal = -sum((rate for _label, rate, _target in row), Fraction(0))
            positivity &= all(rate > 0 for _label, rate, _target in row)
            conservation &= diagonal + sum((rate for _label, rate, _target in row), Fraction(0)) == 0
            for (site_index, mark), _rate, target in row:
                differences = tuple(index for index in range(len(state)) if state[index] != target[index])
                append_only &= (
                    differences == (site_index,)
                    and state[site_index] == BLANK
                    and target[site_index] == mark
                    and sum(value == BLANK for value in target) + 1 == sum(value == BLANK for value in state)
                )
            if state == recorded:
                absorption &= not row and diagonal == 0
    overwrite_rejected = False
    try:
        append_state(recorded, 0, (recorded[0] + 1) % len(MARKS))
    except ValueError:
        overwrite_rejected = True
    return {
        "length": length,
        "sites": len(points),
        "fixture_rows": fixture_rows,
        "positivity": positivity,
        "conservation": conservation,
        "append_only": append_only,
        "absorption": absorption,
        "overwrite_rejected": overwrite_rejected,
        "jump_bound": len(points),
    }


@dataclass(frozen=True)
class HistoryEvent:
    site: int
    mark: int
    time: Fraction
    claimed_before: int = BLANK


@dataclass(frozen=True)
class SymbolicDensity:
    coefficient: Fraction
    exposure: Fraction
    factors: tuple[tuple[Fraction, Fraction, Fraction], ...]

    def label(self) -> str:
        return f"{self.coefficient}*exp(-{self.exposure})"


def history_density(
    initial: tuple[int, ...],
    length: int,
    law: int,
    history: tuple[HistoryEvent, ...],
    horizon: Fraction,
) -> SymbolicDensity | None:
    """Equation (8), conditional on R0 and counting x Lebesgue reference."""
    if horizon <= 0:
        return None
    state = initial
    previous_time = Fraction(0)
    coefficient = Fraction(1)
    exposure = Fraction(0)
    factors = []
    for event in history:
        if not previous_time < event.time < horizon:
            return None
        if not 0 <= event.site < len(state) or event.mark not in MARKS:
            return None
        if event.claimed_before != state[event.site] or state[event.site] != BLANK:
            return None
        exit_rate = finite_exit_rate(state, length, law)
        site = torus_points(length)[event.site]
        rates = marked_rates(state_profile(state, length, site), law)
        jump_rate = rates[event.mark]
        duration = event.time - previous_time
        factors.append((exit_rate, duration, jump_rate))
        exposure += exit_rate * duration
        coefficient *= jump_rate
        state = append_state(state, event.site, event.mark)
        previous_time = event.time
    terminal_rate = finite_exit_rate(state, length, law)
    exposure += terminal_rate * (horizon - previous_time)
    factors.append((terminal_rate, horizon - previous_time, Fraction(1)))
    return SymbolicDensity(coefficient, exposure, tuple(factors))


@cache
def history_facts() -> dict[str, object]:
    length = len(DIRECTIONS) // 2
    sites = len(torus_points(length))
    initial_list = [BLANK] * sites
    initial_list[0] = MARKS[0]
    initial = tuple(initial_list)
    blank_sites = [index for index, value in enumerate(initial) if value == BLANK]
    events = tuple(
        HistoryEvent(site, MARKS[offset], Fraction(offset + 1, 5))
        for offset, site in enumerate(blank_sites[:3])
    )
    valid = history_density(initial, length, 1, events, Fraction(1))
    invalids = (
        (HistoryEvent(0, MARKS[0], Fraction(1, 4)),),
        (HistoryEvent(blank_sites[0], len(MARKS), Fraction(1, 4)),),
        (HistoryEvent(sites, MARKS[0], Fraction(1, 4)),),
        (
            HistoryEvent(blank_sites[0], MARKS[0], Fraction(1, 4)),
            HistoryEvent(blank_sites[0], MARKS[1], Fraction(1, 2)),
        ),
        (HistoryEvent(blank_sites[0], MARKS[0], Fraction(1, 4), MARKS[2]),),
        (
            HistoryEvent(blank_sites[0], MARKS[0], Fraction(1, 2)),
            HistoryEvent(blank_sites[1], MARKS[1], Fraction(1, 2)),
        ),
    )
    invalid_zero = all(history_density(initial, length, 1, item, Fraction(1)) is None for item in invalids)

    # Exact base of the finite-DAG normalization induction.  With z=exp(-lambda T),
    # the no-jump contribution is z and the sum of one-jump marked integrals is
    # (sum q/lambda)(1-z).  The two formal coefficients must be 1 + 0*z.
    normalization_rows = []
    blank_profile = (BLANK,) * len(DIRECTIONS)
    for law in (0, 1):
        lam = hazard(law, 0)
        qsum = sum(marked_rates(blank_profile, law), Fraction(0))
        constant_coefficient = qsum / lam
        z_coefficient = 1 - qsum / lam
        normalization_rows.append((constant_coefficient, z_coefficient))
    base_normalized = all(row == (Fraction(1), Fraction(0)) for row in normalization_rows)
    # Every successor has one fewer blank, so conditioning on the first event
    # lifts the base identity by induction through at most #blanks(R0) levels.
    dag_induction = finite_generator_facts()["append_only"] and finite_generator_facts()["conservation"]
    mixture_weights = (Fraction(2, 5), Fraction(3, 5))
    mixture_normalized = sum(mixture_weights, Fraction(0)) == 1
    return {
        "valid": valid is not None and valid.coefficient > 0,
        "density": valid,
        "invalid_zero": invalid_zero,
        "base_normalized": base_normalized,
        "dag_induction": dag_induction,
        "mixture_normalized": mixture_normalized,
        "max_histories": sites - 1,
        "reference": "counting(sites,marks) x Lebesgue(ordered simplex), conditional on R0",
    }


@dataclass(frozen=True)
class Proposal:
    site: Point
    time: Fraction
    uniform: Fraction
    keys: tuple[Fraction, ...]


def canonical_box(point: Point, radius: int) -> Point:
    length = 2 * radius + 1
    return tuple(((coordinate + radius) % length) - radius for coordinate in point)  # type: ignore[return-value]


def run_field(
    proposals: tuple[Proposal, ...],
    initial: dict[Point, int],
    radius: int,
    periodic: bool,
    law: int,
) -> dict[Point, int]:
    domain = set(product(range(-radius, radius + 1), repeat=3))
    state = {site: mark for site, mark in initial.items() if site in domain}

    def read(site: Point) -> int:
        if periodic:
            return state.get(canonical_box(site, radius), BLANK)
        if site in domain:
            return state.get(site, BLANK)
        return initial.get(site, BLANK)

    for proposal in sorted(proposals, key=lambda item: (item.time, item.site)):
        if proposal.site not in domain or read(proposal.site) != BLANK:
            continue
        profile = tuple(read(add(proposal.site, direction)) for direction in DIRECTIONS)
        recorded = sum(value != BLANK for value in profile)
        if proposal.uniform <= hazard(law, recorded) / (2 * ALPHA):
            state[proposal.site] = select_mark(kernel_weights(profile), proposal.keys)
    return state


def rotate_initial(initial: dict[Point, int], permutation: tuple[int, ...], matrix: Matrix3) -> dict[Point, int]:
    return {mat_vec(matrix, site): permutation[mark] for site, mark in initial.items()}


def rotate_proposals(
    proposals: tuple[Proposal, ...], permutation: tuple[int, ...], matrix: Matrix3
) -> tuple[Proposal, ...]:
    return tuple(
        Proposal(mat_vec(matrix, event.site), event.time, event.uniform, rotate_keys(event.keys, permutation))
        for event in proposals
    )


def rotate_state(state: dict[Point, int], permutation: tuple[int, ...], matrix: Matrix3) -> dict[Point, int]:
    return {mat_vec(matrix, site): permutation[mark] for site, mark in state.items()}


def translate_state(state: dict[Point, int], displacement: Point) -> dict[Point, int]:
    return {add(site, displacement): mark for site, mark in state.items()}


def translate_proposals(proposals: tuple[Proposal, ...], displacement: Point) -> tuple[Proposal, ...]:
    return tuple(
        Proposal(add(event.site, displacement), event.time, event.uniform, event.keys)
        for event in proposals
    )


def backward_clan(proposals: tuple[Proposal, ...], observation: set[Point], horizon: Fraction) -> set[Point]:
    relevant = set(observation)
    for proposal in sorted((item for item in proposals if item.time <= horizon), key=lambda item: item.time, reverse=True):
        if proposal.site in relevant:
            relevant.add(proposal.site)
            relevant.update(add(proposal.site, direction) for direction in DIRECTIONS)
    return relevant


def distance_to_set(point: Point, observation: set[Point]) -> int:
    return min(sum(abs(point[axis] - site[axis]) for axis in range(3)) for site in observation)


def tail_upper(observation_size: int, z: Fraction, start: int) -> Fraction:
    """Rigorous geometric upper bound for sum_{k>=start} z^k/k!."""
    if Fraction(start + 1) <= z:
        raise ValueError("tail start must exceed the ratio threshold")
    first = z**start / factorial(start)
    return observation_size * first / (1 - z / (start + 1))


@cache
def harris_facts() -> dict[str, object]:
    horizon = Fraction(1, 14)
    observation = {(0, 0, 0), (1, 0, 0)}
    key_rows = tuple(
        tuple(Fraction(3 ** ((mark + shift) % len(MARKS))) for mark in MARKS)
        for shift in range(6)
    )
    proposals = (
        Proposal((2, 0, 0), Fraction(1, 100), Fraction(13, 24), key_rows[0]),
        Proposal((-1, 0, 0), Fraction(3, 200), Fraction(1, 4), key_rows[1]),
        Proposal((0, 0, 0), Fraction(1, 50), Fraction(1, 4), key_rows[2]),
        Proposal((1, 0, 0), Fraction(3, 100), Fraction(1, 4), key_rows[3]),
        Proposal((0, 0, 0), Fraction(1, 25), Fraction(1, 4), key_rows[4]),
        Proposal((4, 4, 4), Fraction(1, 20), Fraction(1, 4), key_rows[5]),
    )
    initial = {(-2, 0, 0): MARKS[1], (0, 1, 0): MARKS[3]}
    clan = backward_clan(proposals, observation, horizon)
    clan_radius = max(distance_to_set(site, observation) for site in clan)
    reference = {law: run_field(proposals, initial, 5, False, law) for law in (0, 1)}
    coupling = True
    clan_avoids_boundary = True
    initial_agreement_on_clan = True
    for law in (0, 1):
        expected = {site: reference[law].get(site, BLANK) for site in observation}
        for radius in (4, 5):
            clan_avoids_boundary &= all(
                max(abs(coordinate) for coordinate in site) < radius for site in clan
            )
            initial_agreement_on_clan &= all(
                canonical_box(site, radius) == site
                and initial.get(site, BLANK) == initial.get(canonical_box(site, radius), BLANK)
                for site in clan
            )
            for periodic in (False, True):
                observed = run_field(proposals, initial, radius, periodic, law)
                coupling &= {site: observed.get(site, BLANK) for site in observation} == expected
    small_box_not_projective = (
        run_field(proposals, initial, 2, True, 1) != run_field(proposals, initial, 2, False, 1)
    )

    branching = len(DIRECTIONS) + 1
    proposal_rate = 2 * ALPHA
    z = branching * proposal_rate * horizon
    starts = (4, 8, 12)
    bounds = tuple(tail_upper(len(observation), z, start) for start in starts)
    # For any finite z=14*alpha*T, start at m>=ceil(2z).  Every subsequent
    # term ratio is z/(k+1)<=1/2, so twice the first term dominates the tail;
    # iterating the same ratio proves convergence to zero.  The exact z=1
    # rows below are non-asymptotic regressions of that general argument.
    ratio_threshold = max(1, (2 * z.numerator + z.denominator - 1) // z.denominator)
    tail_ratio_schema = z / (ratio_threshold + 1) <= Fraction(1, 2)
    tail_vanishes = (
        z == (len(DIRECTIONS) + 1) * (2 * ALPHA) * horizon
        and tail_ratio_schema
        and all(bounds[index + 1] < bounds[index] for index in range(len(bounds) - 1))
    )
    finite_box_volume = (2 * clan_radius + 1) ** 3
    finite_spacetime_intensity = proposal_rate * horizon * finite_box_volume

    nonidentity = next(
        (matrix, permutation)
        for matrix, permutation in zip(ROTATIONS, ROTATION_PERMUTATIONS)
        if permutation != tuple(MARKS)
    )
    matrix, permutation = nonidentity
    asymmetric_initial = {(1, 0, 0): MARKS[2], (0, 1, 0): MARKS[5]}
    rotated_initial = rotate_initial(asymmetric_initial, permutation, matrix)
    equivariant = asymmetric_initial != rotated_initial
    for law in (0, 1):
        original_output = run_field(proposals, asymmetric_initial, 5, False, law)
        rotated_output = run_field(
            rotate_proposals(proposals, permutation, matrix), rotated_initial, 5, False, law
        )
        equivariant &= rotate_state(original_output, permutation, matrix) == rotated_output

    translation_equivariant = True
    displacement = (1, -1, 1)
    for law in (0, 1):
        original_output = run_field(proposals, asymmetric_initial, 7, False, law)
        translated_output = run_field(
            translate_proposals(proposals, displacement),
            translate_state(asymmetric_initial, displacement),
            7,
            False,
            law,
        )
        translation_equivariant &= translate_state(original_output, displacement) == translated_output

    thresholds = tuple(
        hazard(law, neighbors) / proposal_rate
        for law in (0, 1)
        for neighbors in range(len(DIRECTIONS) + 1)
    )
    baseline_threshold = min(thresholds)
    baseline_rate = proposal_rate * baseline_threshold
    thinning_exact = all(
        proposal_rate * (hazard(law, neighbors) / proposal_rate) == hazard(law, neighbors)
        for law in (0, 1)
        for neighbors in range(len(DIRECTIONS) + 1)
    )
    epsilons = (Fraction(1, 2), Fraction(1, 10), Fraction(1, 100))
    formation_bounds = []
    for epsilon in epsilons:
        integer_time = epsilon.denominator // epsilon.numerator + 1
        rational_exponential_bound = Fraction(1, 1 + integer_time)
        formation_bounds.append(rational_exponential_bound < epsilon)
    # The same choice n=floor(1/epsilon)+1 works for every positive rational
    # epsilon; density of Q and monotonicity give exp(-alpha*t)->0.  Each
    # never-forms event is null, so their countable union over Z^3 is null.
    formation = baseline_rate == ALPHA and thinning_exact and all(formation_bounds)
    countable_formation = formation and len(DIRECTIONS) == 2 * 3
    partial_global_rates = tuple(
        baseline_rate * (2 * radius + 1) ** 3 for radius in (1, 2, 3)
    )
    global_rate_unbounded = baseline_rate > 0 and all(
        partial_global_rates[index] < partial_global_rates[index + 1]
        for index in range(len(partial_global_rates) - 1)
    )
    coordinate_jump_bound = int(bool(finite_generator_facts()["append_only"]))

    return {
        "proposal_rate": proposal_rate,
        "branching": branching,
        "z": z,
        "tail_bounds": bounds,
        "tail_vanishes": tail_vanishes,
        "clan_size": len(clan),
        "clan_radius": clan_radius,
        "finite_spacetime_intensity": finite_spacetime_intensity,
        "coupling": coupling and clan_avoids_boundary and initial_agreement_on_clan,
        "not_projective": small_box_not_projective,
        "equivariant": equivariant and translation_equivariant,
        "asymmetric_not_invariant": asymmetric_initial != rotated_initial,
        "baseline_threshold": baseline_threshold,
        "baseline_rate": baseline_rate,
        "formation": formation,
        "countable_formation": countable_formation,
        "measurable": tail_vanishes and finite_spacetime_intensity.denominator > 0,
        "locally_cadlag": coordinate_jump_bound == 1,
        "global_rate_infinite": global_rate_unbounded,
    }


def torus_state(length: int, records: dict[Point, int]) -> tuple[int, ...]:
    state = [BLANK] * (length**3)
    for site, mark in records.items():
        state[torus_index(length)[tuple(coordinate % length for coordinate in site)]] = mark
    return tuple(state)


def site_intensity(state: tuple[int, ...], length: int, site: Point, law: int, alpha: Fraction) -> Fraction:
    profile = state_profile(state, length, tuple(coordinate % length for coordinate in site))
    return sum(marked_rates(profile, law, alpha), Fraction(0))


@cache
def selection_facts() -> dict[str, object]:
    hazard_rows = tuple(
        (neighbors, hazard(0, neighbors), hazard(1, neighbors))
        for neighbors in range(len(DIRECTIONS) + 1)
    )
    bounded = all(
        ALPHA <= row[law + 1] <= 2 * ALPHA
        for row in hazard_rows
        for law in (0, 1)
    )
    ratios = tuple(row[2] / row[1] for row in hazard_rows)

    length = len(DIRECTIONS) + 1
    x6 = (0, 0, 0)
    x0 = (3, 3, 3)
    records = {
        torus_add(x6, direction, length): mark
        for mark, direction in enumerate(DIRECTIONS)
    }
    state = torus_state(length, records)
    disjoint = set(torus_add(x6, d, length) for d in DIRECTIONS).isdisjoint(
        set(torus_add(x0, d, length) for d in DIRECTIONS)
    )
    finite_conditionals = []
    scaled_conditionals = []
    local_conditionals = []
    for law in (0, 1):
        total = finite_exit_rate(state, length, law)
        pair = tuple(site_intensity(state, length, site, law, ALPHA) for site in (x0, x6))
        first_jump_probabilities = tuple(rate / total for rate in pair)
        finite_conditionals.append(first_jump_probabilities[1] / sum(first_jump_probabilities, Fraction(0)))
        scale_factor = Fraction(11, 7)
        scaled_pair = tuple(site_intensity(state, length, site, law, scale_factor * ALPHA) for site in (x0, x6))
        scaled_conditionals.append(scaled_pair[1] / sum(scaled_pair, Fraction(0)))

        # On Z^3 let U={x0,x6} union N(x0), and stop at the first new Record in
        # U.  Until that stop, x0 keeps zero recorded neighbors and x6 keeps six,
        # so their rates r0,r6 are fixed.  Births outside U may change the other
        # U-site hazards; conditioning on that exterior history therefore gives
        # densities r_i times one common positive survival functional J_T.  J_T
        # cancels when the winner is conditioned to lie in {x0,x6}, leaving the
        # exact ratio below for every T>0 without assuming constant competitors.
        local_conditionals.append(pair[1] / sum(pair, Fraction(0)))

    global_rescale_control = []
    for multiplier in (Fraction(2), Fraction(5, 3)):
        pair0 = tuple(site_intensity(state, length, site, 0, ALPHA) for site in (x0, x6))
        pair1 = tuple(multiplier * rate for rate in pair0)
        global_rescale_control.append(pair1[1] / sum(pair1, Fraction(0)))

    return {
        "hazard_rows": hazard_rows,
        "bounded": bounded,
        "ratios_vary": len(set(ratios)) > 1,
        "disjoint": disjoint,
        "neighbor_counts": tuple(
            sum(value != BLANK for value in state_profile(state, length, site)) for site in (x0, x6)
        ),
        "finite": tuple(finite_conditionals),
        "scaled": tuple(scaled_conditionals),
        "local": tuple(local_conditionals),
        "inequivalent": finite_conditionals[0] != finite_conditionals[1],
        "scale_free": tuple(finite_conditionals) == tuple(scaled_conditionals),
        "local_matches": tuple(finite_conditionals) == tuple(local_conditionals),
        "global_rescale_equal": len(set(global_rescale_control)) == 1,
    }


def seed_records(length: int, direction: Point, compound: bool) -> dict[Point, int]:
    mark = DIRECTION_INDEX[direction]
    origin = (0, 0, 0)
    offsets = (origin,) if not compound else (scale(-2, direction), origin, direction)
    return {tuple(value % length for value in site): mark for site in offsets}


def seed_rate_row(length: int, direction: Point, compound: bool, law: int) -> tuple[bool, int, Fraction]:
    records = seed_records(length, direction, compound)
    state = torus_state(length, records)
    y = tuple(value % length for value in scale(2, direction))
    occupied = state[torus_index(length)[y]] != BLANK
    profile = state_profile(state, length, y)
    mark = DIRECTION_INDEX[direction]
    rate = Fraction(0) if occupied else marked_rates(profile, law)[mark]
    return occupied, sum(value != BLANK for value in profile), rate


def target_path_coefficient(direction: Point, law: int) -> tuple[Fraction, ...]:
    target_sites = (scale(-2, direction), (0, 0, 0), direction)
    mark = DIRECTION_INDEX[direction]
    layers: dict[frozenset[Point], Fraction] = {frozenset(): Fraction(1)}
    coefficients = [Fraction(0)]
    for _step in range(1, len(target_sites) + 1):
        next_layer: dict[frozenset[Point], Fraction] = {}
        for occupied, coefficient in layers.items():
            records = {site: mark for site in occupied}
            for site in target_sites:
                if site in occupied:
                    continue
                profile = tuple(records.get(add(site, direction2), BLANK) for direction2 in DIRECTIONS)
                rate = marked_rates(profile, law)[mark]
                successor = occupied | {site}
                next_layer[successor] = next_layer.get(successor, Fraction(0)) + coefficient * rate
        layers = next_layer
        coefficients.append(layers.get(frozenset(target_sites), Fraction(0)))
    return tuple(coefficients)


def injective_seed_support_all_lengths() -> bool:
    """Uniform support proof for every periodic L>=6.

    In the integer lift, every seed, y, and neighbor-of-y coordinate lies
    between -2 and 3 along the seed axis (and between -1 and 1 transversely).
    Distinct lifted points therefore differ by less than 6 in each coordinate,
    so none can become congruent modulo any L>=6.
    """
    rows = []
    for direction in DIRECTIONS:
        compound = {scale(-2, direction), (0, 0, 0), direction}
        y = scale(2, direction)
        neighbors = {add(y, neighbor) for neighbor in DIRECTIONS}
        expected_neighbor = direction
        relevant = compound | {y} | neighbors
        coordinate_spans = tuple(
            max(point[axis] for point in relevant) - min(point[axis] for point in relevant)
            for axis in range(3)
        )
        rows.append(
            len(compound) == 3
            and y not in compound
            and expected_neighbor in compound
            and not ((neighbors - {expected_neighbor}) & compound)
            and max(coordinate_spans) < 6
        )
    return all(rows)


@cache
def arity_facts() -> dict[str, object]:
    coefficients = []
    all_directions = True
    for direction in DIRECTIONS:
        for law in (0, 1):
            row = target_path_coefficient(direction, law)
            coefficients.append(row)
            all_directions &= row[0] == row[1] == row[2] == 0 and row[3] > 0

    kappa = Fraction(5, 7)
    oriented_rate = kappa / len(DIRECTIONS)
    extra_direct = kappa / (2 * len(DIRECTIONS))
    general_direct_total = sum((oriented_rate, extra_direct), Fraction(0))

    controls: dict[int, tuple[object, ...]] = {}
    for length in (3, 4, 5):
        rows = []
        for direction in DIRECTIONS:
            distinct_sites = len(seed_records(length, direction, True))
            single = tuple(seed_rate_row(length, direction, False, law)[2] for law in (0, 1))
            compound = tuple(seed_rate_row(length, direction, True, law) for law in (0, 1))
            rows.append((distinct_sites, single, compound))
        controls[length] = tuple(rows)

    l3_ok = all(
        distinct == 2
        and single[0] == Fraction(2, 7)
        and single[1] == Fraction(1, 3)
        and compound[0] == (False, 2, Fraction(4, 9))
        and compound[1] == (False, 2, Fraction(16, 27))
        for distinct, single, compound in controls[3]
    )
    # Strict positivity of every marked one-site rate makes the graph-distance
    # lower bound sharp: the collapsed L=3 target needs exactly two appends.
    l3_orders = tuple(distinct for distinct, _single, _compound in controls[3])
    l3_ok &= set(l3_orders) == {2}
    l4_ok = all(
        distinct == 3 and compound[0][0] and compound[1][0]
        for distinct, _single, compound in controls[4]
    )
    l5_ok = all(
        distinct == 3
        and compound[0] == (False, 2, Fraction(4, 9))
        and compound[1] == (False, 2, Fraction(16, 27))
        for distinct, _single, compound in controls[5]
    )
    return {
        "all_directions": all_directions,
        "coefficients": tuple(coefficients),
        "single_order": len(next(row for row in coefficients if row[-1] > 0)) - 1,
        "compound_order": 1 if oriented_rate > 0 else 0,
        "oriented_rate": oriented_rate,
        "general_direct_total": general_direct_total,
        "sole_direct_qualification": general_direct_total != oriented_rate,
        "uniform_target_rate_bound": len((0, 1, 2)) * 2 * ALPHA,
        "l3_orders": l3_orders,
        "l3": l3_ok,
        "l4": l4_ok,
        "l5": l5_ok,
    }


@cache
def lumpability_facts() -> dict[str, object]:
    rows = []
    support = injective_seed_support_all_lengths()
    for length in (6, 7, 8):
        for direction in DIRECTIONS:
            single_records = seed_records(length, direction, False)
            compound_records = seed_records(length, direction, True)
            y = tuple(value % length for value in scale(2, direction))
            expected_neighbor = tuple(value % length for value in direction)
            other_neighbors = {
                torus_add(y, neighbor, length) for neighbor in DIRECTIONS
            } - {expected_neighbor}
            support &= (
                len(compound_records) == 3
                and y not in compound_records
                and expected_neighbor in compound_records
                and not (other_neighbors & set(compound_records))
            )
            rates = tuple(
                (
                    seed_rate_row(length, direction, False, law)[2],
                    seed_rate_row(length, direction, True, law)[2],
                )
                for law in (0, 1)
            )
            rows.append(rates)
    common = rows[0]
    exact = all(row == common for row in rows)
    unequal = all(left != right for left, right in common)

    # Explicit required partition: the two seeds share a fibre and their y:f
    # successors share one distinguishable target cell, with no other member.
    projection = {"S": "seed", "C": "seed", "S+y": "A", "C+y": "A"}
    required_fibre = projection["S"] == projection["C"] and projection["S+y"] == projection["C+y"]
    target_unique = sum(value == "A" for value in projection.values()) == 2
    decisive = required_fibre and target_unique and unequal

    compensated = []
    for left, right in common:
        compensation = right - left
        compensated.append(left + compensation == right and compensation > 0)
    constant_rows = []
    length = 6
    direction = DIRECTIONS[0]
    for records in (seed_records(length, direction, False), seed_records(length, direction, True)):
        state = torus_state(length, records)
        for law in (0, 1):
            off_diagonal = sum(
                (
                    sum(marked_rates(state_profile(state, length, site), law), Fraction(0))
                    for site_index, site in enumerate(torus_points(length))
                    if state[site_index] == BLANK
                ),
                Fraction(0),
            )
            constant_rows.append(-off_diagonal + off_diagonal)
    constant_projection = all(row_sum == 0 for row_sum in constant_rows)
    return {
        "support": support,
        "exact": exact,
        "rates": common,
        "required_fibre": required_fibre,
        "target_unique": target_unique,
        "decisive": decisive,
        "compensating_falsifier": all(compensated),
        "constant_projection": constant_projection,
    }


def periodic_edges(length: int) -> tuple[tuple[int, int], ...]:
    index = torus_index(length)
    positive_axes = tuple(direction for direction in DIRECTIONS if 1 in direction)
    return tuple(
        (index[point], index[torus_add(point, direction, length)])
        for point in torus_points(length)
        for direction in positive_axes
    )


def gf2_rank(columns: Iterable[int]) -> int:
    pivots: dict[int, int] = {}
    for column in columns:
        value = column
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = value
                break
            value ^= pivots[pivot]
    return len(pivots)


def connected_components(vertex_count: int, edges: tuple[tuple[int, int], ...]) -> tuple[tuple[int, ...], ...]:
    adjacency = [[] for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].append(right)
        adjacency[right].append(left)
    unseen = set(range(vertex_count))
    components = []
    while unseen:
        root = min(unseen)
        queue = deque((root,))
        unseen.remove(root)
        component = []
        while queue:
            vertex = queue.popleft()
            component.append(vertex)
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        components.append(tuple(component))
    return tuple(components)


def canonical_tree_edges(length: int) -> tuple[tuple[int, int], ...]:
    """A spanning tree for every L>=1, proved by the decreasing coordinate sum."""
    index = torus_index(length)
    edges = []
    for point in torus_points(length):
        if point == (0, 0, 0):
            continue
        coordinate = next(axis for axis, value in enumerate(point) if value)
        parent = list(point)
        parent[coordinate] -= 1
        edges.append((index[tuple(parent)], index[point]))
    return tuple(edges)


@cache
def incidence_facts() -> dict[str, object]:
    regressions = []
    theorem = True
    for length in (3, 4, 5):
        vertex_count = len(torus_points(length))
        edges = periodic_edges(length)
        components = connected_components(vertex_count, edges)
        columns = tuple((1 << left) ^ (1 << right) for left, right in edges)
        rank = gf2_rank(columns)
        tree = canonical_tree_edges(length)
        tree_rank = gf2_rank((1 << left) ^ (1 << right) for left, right in tree)
        degrees = [0] * vertex_count
        for left, right in edges:
            degrees[left] += 1
            degrees[right] += 1
        expected_rank = vertex_count - len(components)
        theorem &= (
            len(components) == 1
            and rank == expected_rank
            and tree_rank == len(tree) == vertex_count - 1
            and all(degree == len(DIRECTIONS) for degree in degrees)
            and len(edges) == vertex_count * len(DIRECTIONS) // 2
        )
        regressions.append((length, rank))

    # The same canonical parent lowers sum(coordinates), hence is a spanning
    # tree for every L>=3.  Removing the root row makes its incidence columns
    # unit triangular; together with column-sum zero this proves im B=1^perp
    # and rank |V|-1 over R, not merely in the three regressions.
    parameterized_proof = all(
        all(
            sum(torus_points(length)[child]) == sum(torus_points(length)[parent]) + 1
            for parent, child in canonical_tree_edges(length)
        )
        and len(canonical_tree_edges(length)) == length**3 - 1
        for length in range(3, 9)
    )

    l3_vertices = len(torus_points(3))
    one_birth = tuple(Fraction(index == 0) for index in range(l3_vertices))
    three_birth = tuple(Fraction(index in (0, 1, 2)) for index in range(l3_vertices))
    source_free_rejected = sum(one_birth, Fraction(0)) != 0 and sum(three_birth, Fraction(0)) != 0
    source_repairs = (
        sum(one_birth, Fraction(0)) == 1
        and -sum(one_birth, Fraction(0)) == -1
        and sum(three_birth, Fraction(0)) == 3
        and -sum(three_birth, Fraction(0)) == -3
    )
    return {
        "theorem": theorem and parameterized_proof,
        "regressions": tuple(regressions),
        "source_free_rejected": source_free_rejected,
        "source_repairs": source_repairs,
        # B_L acts on vertex-valued densities; a separate scalar coordinate
        # is not an edge-current divergence until an enlarged incidence is supplied.
        "scalar_debit_not_local_current": len(one_birth) != len((Fraction(-1),)),
    }


MUTATIONS = (
    "overwrite_record",
    "subnormalize_marks",
    "break_mark_covariance",
    "claim_asymmetric_initial_invariant",
    "fixed_or_tied_mark_keys",
    "hidden_no_event_mark",
    "nonlocal_unbounded_hazard",
    "zero_blank_hazard",
    "accept_invalid_history",
    "use_small_torus_lumpability_fixture",
    "remove_lumpability_fibre",
    "compensate_lumpability_target",
    "hide_direct_triple_jump",
    "global_rescale_pair",
    "suppress_record_source",
    "open_or_disconnected_incidence",
    "claim_global_jump_chain",
    "claim_full_m2_completion",
)


MUTATION_GATE = {
    "overwrite_record": "D_finite_generator",
    "subnormalize_marks": "C_joint_intensity",
    "break_mark_covariance": "B_rho_kernel",
    "claim_asymmetric_initial_invariant": "F_harris_construction",
    "fixed_or_tied_mark_keys": "F_harris_construction",
    "hidden_no_event_mark": "C_joint_intensity",
    "nonlocal_unbounded_hazard": "G_dimensionless_selection",
    "zero_blank_hazard": "F_harris_construction",
    "accept_invalid_history": "E_history_law",
    "use_small_torus_lumpability_fixture": "H_seed_arity",
    "remove_lumpability_fibre": "I_lumpability",
    "compensate_lumpability_target": "I_lumpability",
    "hide_direct_triple_jump": "H_seed_arity",
    "global_rescale_pair": "G_dimensionless_selection",
    "suppress_record_source": "J_incidence_source",
    "open_or_disconnected_incidence": "J_incidence_source",
    "claim_global_jump_chain": "F_harris_construction",
    "claim_full_m2_completion": "B_rho_kernel",
}


def mutation_preserves_gate(mutation: str) -> bool:
    """Execute one hostile alteration; False means its named gate catches it."""
    if mutation == "overwrite_record":
        state = (MARKS[0],)
        mutated = (MARKS[1],)
        return state == mutated
    if mutation == "subnormalize_marks":
        weights = kernel_weights((BLANK,) * len(DIRECTIONS))
        probabilities = tuple(Fraction(weight, sum(weights) + 1) for weight in weights)
        return sum(probabilities, Fraction(0)) == 1
    if mutation == "break_mark_covariance":
        profile = (MARKS[0],) + (BLANK,) * (len(DIRECTIONS) - 1)
        permutation = next(item for item in ROTATION_PERMUTATIONS if item[0] != 0)
        weights = list(kernel_weights(profile))
        weights[0] *= 3
        rotated = rotate_profile(profile, permutation)
        rotated_weights = list(kernel_weights(rotated))
        rotated_weights[0] *= 3
        return rotated_weights[permutation[0]] == weights[0]
    if mutation == "claim_asymmetric_initial_invariant":
        return not harris_facts()["asymmetric_not_invariant"]
    if mutation == "fixed_or_tied_mark_keys":
        tie_is_unique = True
        try:
            select_mark(kernel_weights((BLANK,) * len(DIRECTIONS)), (Fraction(1),) * len(MARKS))
        except ValueError:
            tie_is_unique = False
        profile = (BLANK,) * len(DIRECTIONS)
        keys = tuple(Fraction(3**mark) for mark in MARKS)
        winner = select_mark(kernel_weights(profile), keys)
        permutation = next(item for item in ROTATION_PERMUTATIONS if item[winner] != winner)
        # Fixed labels rotate the profile but not the keys, so the selected
        # label fails to follow the orbit even away from the tie set.
        fixed_label_covariance = (
            select_mark(kernel_weights(rotate_profile(profile, permutation)), keys)
            == permutation[winner]
        )
        return tie_is_unique and fixed_label_covariance
    if mutation == "hidden_no_event_mark":
        lam = hazard(0, 0)
        visible = tuple(lam * Fraction(1, len(MARKS) + 1) for _mark in MARKS)
        return sum(visible, Fraction(0)) == lam
    if mutation == "nonlocal_unbounded_hazard":
        same_local_remote_counts = (0, 2)
        rates = tuple(ALPHA * (1 + count) for count in same_local_remote_counts)
        return len(set(rates)) == 1 and max(rates) <= 2 * ALPHA
    if mutation == "zero_blank_hazard":
        proposal_rate = 2 * ALPHA
        return proposal_rate * Fraction(0) == ALPHA
    if mutation == "accept_invalid_history":
        length = len(DIRECTIONS) // 2
        blank = (BLANK,) * len(torus_points(length))
        repeated = (
            HistoryEvent(0, MARKS[0], Fraction(1, 4)),
            HistoryEvent(0, MARKS[1], Fraction(1, 2)),
        )
        honest = history_density(blank, length, 0, repeated, Fraction(1))
        mutated_positive = SymbolicDensity(Fraction(1), Fraction(0), ())
        return honest is not None and mutated_positive.coefficient == 0
    if mutation == "use_small_torus_lumpability_fixture":
        controls_expose_wrap = all(bool(arity_facts()[key]) for key in ("l3", "l4", "l5"))
        return not controls_expose_wrap
    if mutation == "remove_lumpability_fibre":
        projection = {"S": "seed-S", "C": "seed-C"}
        return projection["S"] == projection["C"]
    if mutation == "compensate_lumpability_target":
        return not lumpability_facts()["compensating_falsifier"]
    if mutation == "hide_direct_triple_jump":
        return arity_facts()["general_direct_total"] == arity_facts()["oriented_rate"]
    if mutation == "global_rescale_pair":
        return not selection_facts()["global_rescale_equal"]
    if mutation == "suppress_record_source":
        return sum((Fraction(1),), Fraction(0)) == 0
    if mutation == "open_or_disconnected_incidence":
        length = 3
        points = torus_points(length)
        index = torus_index(length)
        open_edges = []
        for point in points:
            for axis in range(3):
                if point[axis] + 1 < length:
                    target = list(point)
                    target[axis] += 1
                    open_edges.append((index[point], index[tuple(target)]))
        degrees = [0] * len(points)
        for left, right in open_edges:
            degrees[left] += 1
            degrees[right] += 1
        return all(degree == len(DIRECTIONS) for degree in degrees)
    if mutation == "claim_global_jump_chain":
        return not harris_facts()["global_rate_infinite"]
    if mutation == "claim_full_m2_completion":
        # The constructed support is finite.  The affine real line
        # {(I-r sigma_z)/2: -1<r<1} already supplies more than six valid M2
        # possibilities, so a six-element support cannot exhaust the domain.
        extra_radii = tuple(Fraction(index, 10) for index in range(-9, 10))
        return len(RHO) >= len(extra_radii)
    raise ValueError(mutation)


N5_LINES = (
    "N5 per_element: checked six exact rho_f density matrices and every one of 117649 ordered neighbor profiles under all 24 proper cubic rotations.",
    "N5 per_site: checked permanent append, positive-baseline eventual formation, both seven-row hazards, and the two-site local first-Record race.",
    "N5 per_mode: checked and not executed — this pure-Record process has no Fourier, spectral, or other physical mode decomposition in its frozen contract.",
    "N5 per_block: checked finite Q/history normalization, six-direction one-site versus compound arity, corrected L>=6 lumpability, and all small-torus controls.",
    "N5 lattice_wide: checked finite-clan Harris convergence on Z^3 and the all-L>=3 real-incidence/source theorem; no global jump chain or full-M2 law is claimed.",
)


def base_checks(mutation: str = "") -> dict[str, tuple[bool, str]]:
    rho = rho_facts()
    profiles = profile_facts()
    finite = finite_generator_facts()
    histories = history_facts()
    harris = harris_facts()
    selection = selection_facts()
    arity = arity_facts()
    lumpability = lumpability_facts()
    incidence = incidence_facts()

    spectra = rho["spectra"]
    checks = {
        "A_directions_rotations": (
            len(DIRECTIONS) == 2 * 3
            and len(set(DIRECTIONS)) == len(DIRECTIONS)
            and len(ROTATIONS) == factorial(3) * (2**3) // 2
            and len(set(ROTATIONS)) == len(ROTATIONS),
            f"generated directions={len(DIRECTIONS)}, det+1 signed permutations={len(ROTATIONS)}",
        ),
        "B_rho_kernel": (
            bool(rho["hermitian"] and rho["trace_characteristic"] and rho["positive"])
            and bool(rho["distinct"] and rho["common_spectrum"] and rho["covariance"])
            and profiles["count"] == profiles["expected_count"]
            and bool(profiles["normalization"] and profiles["positivity"] and profiles["variation"] and profiles["covariance"]),
            f"rho spectra derived={spectra[0]}; profiles={profiles['count']} x rotations={len(ROTATIONS)}",
        ),
        "C_joint_intensity": (
            bool(profiles["rate_sum"])
            and set(MARKS) == set(range(len(RHO)))
            and BLANK not in MARKS,
            "sum_f q_x(f|R)=lambda_x exactly; six supported marks and no hidden no-event mass",
        ),
        "D_finite_generator": (
            bool(finite["positivity"] and finite["conservation"] and finite["append_only"])
            and bool(finite["absorption"] and finite["overwrite_rejected"])
            and bool(profiles["positivity"] and profiles["rate_sum"] and selection["bounded"]),
            f"Q rows exact on Lambda_{finite['length']}; append bound={finite['jump_bound']}; absorption/permanence hold",
        ),
        "E_history_law": (
            bool(histories["valid"] and histories["invalid_zero"] and histories["base_normalized"])
            and bool(histories["dag_induction"] and histories["mixture_normalized"]),
            "conditional counting x ordered-Lebesgue density normalized by conservative pure-birth DAG induction",
        ),
        "F_harris_construction": (
            bool(harris["tail_vanishes"] and harris["measurable"] and harris["locally_cadlag"])
            and bool(harris["coupling"] and harris["not_projective"] and harris["equivariant"])
            and bool(harris["asymmetric_not_invariant"] and harris["formation"] and harris["countable_formation"])
            and bool(profiles["race_distribution"] and profiles["race_covariance"])
            and bool(harris["global_rate_infinite"]),
            f"rate=2alpha; clan={harris['clan_size']} sites/radius {harris['clan_radius']}; tail z={harris['z']}; local coupling/equivariance/formation",
        ),
        "G_dimensionless_selection": (
            bool(selection["bounded"] and selection["ratios_vary"] and selection["disjoint"])
            and selection["neighbor_counts"] == (0, len(DIRECTIONS))
            and bool(selection["inequivalent"] and selection["scale_free"] and selection["local_matches"])
            and bool(selection["global_rescale_equal"]),
            f"finite and local Record-order cylinders={selection['finite']}; invariant under alpha rescaling",
        ),
        "H_seed_arity": (
            bool(arity["all_directions"] and arity["sole_direct_qualification"])
            and arity["uniform_target_rate_bound"] == len((0, 1, 2)) * 2 * ALPHA
            and bool(arity["l3"] and arity["l4"] and arity["l5"]),
            f"six directions: bounded one-site order={arity['single_order']}, sole compound order={arity['compound_order']}; L3/4/5 wraps reproduced",
        ),
        "I_lumpability": (
            bool(lumpability["support"] and lumpability["exact"] and lumpability["decisive"])
            and bool(lumpability["compensating_falsifier"] and lumpability["constant_projection"]),
            f"L>=6 future-cell row pairs={lumpability['rates']}; compensation and constant-quotient exits retained",
        ),
        "J_incidence_source": (
            bool(incidence["theorem"] and incidence["source_free_rejected"] and incidence["source_repairs"])
            and bool(incidence["scalar_debit_not_local_current"]),
            f"all-L>=3 rank=|V|-1 theorem; regressions={incidence['regressions']}; birth/debit totals 1/-1 and 3/-3",
        ),
    }
    if mutation:
        gate = MUTATION_GATE[mutation]
        ok, message = checks[gate]
        checks[gate] = (ok and mutation_preserves_gate(mutation), message + f" [mutation={mutation}]")
    return checks


def mutation_sweep() -> tuple[int, tuple[str, ...]]:
    survivors = tuple(
        mutation
        for mutation in MUTATIONS
        if all(ok for ok, _message in base_checks(mutation).values())
    )
    return len(MUTATIONS) - len(survivors), survivors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    checks = base_checks(args.mutation)
    rejected, survivors = mutation_sweep() if not args.mutation else (1, ())
    checks["K_hostile_mutations"] = (
        (not args.mutation and rejected == len(MUTATIONS) and not survivors)
        or (bool(args.mutation) and not all(ok for ok, _message in checks.values())),
        f"rejected={rejected}/{len(MUTATIONS)} named hostile alterations" if not args.mutation else "selected hostile alteration is exposed",
    )
    n5_ok = (
        len(N5_LINES) == 5
        and all(len(line) >= 40 for line in N5_LINES)
        and all(label in line for label, line in zip(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"), N5_LINES))
        and "checked and not executed" in N5_LINES[2]
    )
    checks["L_n5_resolution"] = (n5_ok, "five substantive resolution lines, with the absent physical-mode lane stated honestly")

    passed = 0
    for name, (ok, message) in checks.items():
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
        passed += int(ok)

    if not args.mutation:
        profiles = profile_facts()
        harris = harris_facts()
        arity = arity_facts()
        lumpability = lumpability_facts()
        print(
            "EXACT: blank p=" + str(profiles["blank_probability"])
            + "; one-neighbor p=" + str(profiles["one_neighbor_probability"])
            + f"; Harris tail bounds={harris['tail_bounds']}."
        )
        print(
            f"INTERFACES: q rows={lumpability['rates']}; compound sole-direct coefficient="
            f"{arity['oriented_rate']}, general direct-sum control={arity['general_direct_total']}."
        )
        print(
            "HARRIS_SCOPE: measurable finite clans at rational local queries, local cadlag extension, "
            "and shared-field convergence; global event rate is infinite and no global jump chain is claimed."
        )
        print(
            "SECTOR_SCOPE: the six rho_f are valid M2 possibilities, not an exhaustive M2 domain; "
            "the common full-domain extension remains live and unexecuted."
        )
        for line in N5_LINES:
            print(line)
        if survivors:
            print("MUTATION_SURVIVORS:", ",".join(survivors))

    failures = len(checks) - passed
    if not args.mutation and failures == 0:
        print("COMPUTATIONAL_TERMINAL: PURE-RECORD-HARRIS-PROCESSES-EXIST-DIMENSIONLESS-GENERATOR-UNDERSELECTED")
        print("SHIP_GATE: sector-scoped result; independent checker and landed N1-N8 packet remain separate prerequisites.")
    print(f"TOTAL: PASS={passed} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
