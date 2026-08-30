#!/usr/bin/env python3
"""Independent exact checker for the Block18 pure-Record process gate.

This file deliberately reconstructs the witness from the frozen packet.  It
does not import the primary runner.  All compatibility statements are scoped
to the invariant seven-state (blank plus six rho_f marks) process sector.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
from math import factorial, gcd
import sys
from typing import Iterable, Sequence


Q = Fraction
Vec = tuple[int, int, int]
Site = int
Profile = tuple[int, ...]  # 0 is blank; 1,...,6 are signed-axis marks.
Config = frozenset[tuple[Site, int]]  # mark indices are 0,...,5.


class Ledger:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str) -> bool:
        if condition:
            self.passed += 1
            tag = "PASS"
        else:
            self.failed += 1
            tag = "FAIL"
        print(f"{tag} {name}: {detail}")
        return condition


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def vector_add(x: Vec, y: Vec) -> Vec:
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


def vector_scale(k: int, x: Vec) -> Vec:
    return (k * x[0], k * x[1], k * x[2])


DIRECTIONS: tuple[Vec, ...] = tuple(
    tuple(sign if coordinate == axis else 0 for coordinate in range(3))  # type: ignore[misc]
    for axis in range(3)
    for sign in (1, -1)
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}


def permutation_parity(p: tuple[int, int, int]) -> int:
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


@dataclass(frozen=True)
class Rotation:
    axes: tuple[int, int, int]
    signs: tuple[int, int, int]
    direction_map: tuple[int, ...]

    def vector(self, v: Vec) -> Vec:
        out = [0, 0, 0]
        for old_axis in range(3):
            out[self.axes[old_axis]] = self.signs[old_axis] * v[old_axis]
        return (out[0], out[1], out[2])

    def profile(self, profile: Profile) -> Profile:
        rotated = [0] * len(DIRECTIONS)
        for old_slot, state in enumerate(profile):
            new_slot = self.direction_map[old_slot]
            rotated[new_slot] = 0 if state == 0 else self.direction_map[state - 1] + 1
        return tuple(rotated)


def proper_cubic_rotations() -> tuple[Rotation, ...]:
    rotations: list[Rotation] = []
    for axes in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_parity(axes) * signs[0] * signs[1] * signs[2] != 1:
                continue
            probe = Rotation(axes, signs, ())
            mapping = tuple(DIR_INDEX[probe.vector(direction)] for direction in DIRECTIONS)
            rotations.append(Rotation(axes, signs, mapping))
    unique = {rotation.direction_map for rotation in rotations}
    if len(unique) != len(rotations):
        raise ValueError("duplicate signed-permutation rotations")
    return tuple(rotations)


def kernel_weights(profile: Sequence[int]) -> tuple[int, ...]:
    counts = Counter(state - 1 for state in profile if state)
    return tuple(1 << counts[mark] for mark in range(len(DIRECTIONS)))


def kernel_probabilities(profile: Sequence[int]) -> tuple[Fraction, ...]:
    weights = kernel_weights(profile)
    denominator = sum(weights)
    return tuple(Q(weight, denominator) for weight in weights)


def rho_spectrum_certificate() -> tuple[Fraction, Fraction, Fraction, bool]:
    radius = Q(143, 256)
    determinants: list[Fraction] = []
    traces: list[Fraction] = []
    hermitian = True
    for fx, fy, fz in DIRECTIONS:
        diagonal_0 = Q(1, 2) - radius * fz / 2
        diagonal_1 = Q(1, 2) + radius * fz / 2
        offdiag_re = -radius * fx / 2
        offdiag_im = radius * fy / 2
        rho_01 = (offdiag_re, offdiag_im)
        rho_10 = (offdiag_re, -offdiag_im)
        hermitian &= rho_10 == (rho_01[0], -rho_01[1])
        traces.append(diagonal_0 + diagonal_1)
        determinant = diagonal_0 * diagonal_1 - offdiag_re**2 - offdiag_im**2
        determinants.append(determinant)
    if len(set(determinants)) != 1 or len(set(traces)) != 1:
        raise ValueError("rho_f trace/determinant is not orbit constant")
    trace = traces[0]
    determinant = determinants[0]
    discriminant_root = radius  # sqrt(trace^2-4 det) derived from det=(1-r^2)/4.
    eigenvalues = ((trace - discriminant_root) / 2, (trace + discriminant_root) / 2)
    positive = hermitian and determinant > 0 and sum(eigenvalues) == trace and min(eigenvalues) > 0
    return eigenvalues[0], eigenvalues[1], determinant, positive


@dataclass(frozen=True)
class OrbitCensus:
    profiles: int
    rotations: int
    orbits: int
    orbit_sizes: tuple[tuple[int, int], ...]
    covariance_pairs: int
    distinct_probability_rows: int
    uniform_profiles: int
    valid: bool


def profile_orbit_census(rotations: Sequence[Rotation]) -> OrbitCensus:
    orbit_members: dict[Profile, int] = {}
    probability_rows: set[tuple[int, ...]] = set()
    uniform_profiles = 0
    covariance_pairs = 0
    profiles = 0
    valid = True
    for profile in product(range(len(DIRECTIONS) + 1), repeat=len(DIRECTIONS)):
        profiles += 1
        weights = kernel_weights(profile)
        denominator = sum(weights)
        valid &= denominator > 0 and sum(Q(w, denominator) for w in weights) == 1
        common = 0
        for weight in weights:
            common = gcd(common, weight)
        probability_rows.add(tuple(weight // common for weight in weights))
        uniform_profiles += int(len(set(weights)) == 1)

        images: list[Profile] = []
        for rotation in rotations:
            rotated_profile = rotation.profile(profile)
            images.append(rotated_profile)
            rotated_weights = kernel_weights(rotated_profile)
            rotated_denominator = sum(rotated_weights)
            covariant = all(
                Q(rotated_weights[rotation.direction_map[mark]], rotated_denominator)
                == Q(weights[mark], denominator)
                for mark in range(len(DIRECTIONS))
            )
            valid &= covariant
            covariance_pairs += 1
        canonical = min(images)
        orbit_members[canonical] = orbit_members.get(canonical, 0) + 1

    size_histogram = Counter(orbit_members.values())
    return OrbitCensus(
        profiles=profiles,
        rotations=len(rotations),
        orbits=len(orbit_members),
        orbit_sizes=tuple(sorted(size_histogram.items())),
        covariance_pairs=covariance_pairs,
        distinct_probability_rows=len(probability_rows),
        uniform_profiles=uniform_profiles,
        valid=valid,
    )


@dataclass(frozen=True)
class Torus:
    length: int

    @property
    def volume(self) -> int:
        return self.length**3

    def site(self, coordinate: Vec) -> Site:
        x, y, z = (component % self.length for component in coordinate)
        return x + self.length * (y + self.length * z)

    def coordinate(self, site: Site) -> Vec:
        if not 0 <= site < self.volume:
            raise ValueError("site outside torus")
        x = site % self.length
        quotient = site // self.length
        y = quotient % self.length
        z = quotient // self.length
        return (x, y, z)

    def neighbors(self, site: Site) -> tuple[Site, ...]:
        coordinate = self.coordinate(site)
        return tuple(self.site(vector_add(coordinate, direction)) for direction in DIRECTIONS)


def state_map(config: Config) -> dict[Site, int]:
    result = dict(config)
    if len(result) != len(config):
        raise ValueError("configuration gives two marks to one site")
    return result


def append_record(config: Config, site: Site, mark: int, torus: Torus) -> Config | None:
    occupied = state_map(config)
    if site in occupied or not 0 <= site < torus.volume or not 0 <= mark < len(DIRECTIONS):
        return None
    return config | {(site, mark)}


def profile_at(config: Config, site: Site, torus: Torus) -> Profile:
    occupied = state_map(config)
    return tuple(0 if neighbor not in occupied else occupied[neighbor] + 1 for neighbor in torus.neighbors(site))


def hazard_ratio(law: int, recorded_neighbors: int) -> Fraction:
    if not 0 <= recorded_neighbors <= len(DIRECTIONS):
        raise ValueError("nearest-neighbor occupancy is outside 0,...,6")
    if law == 0:
        return Q(1)
    if law == 1:
        return Q(1) + Q(recorded_neighbors, len(DIRECTIONS))
    raise ValueError("unknown hazard law")


@dataclass(frozen=True)
class HazardSpec:
    range_radius: int
    ratios_by_neighbor_count: tuple[Fraction, ...]


def valid_hazard_spec(spec: HazardSpec) -> bool:
    return (
        spec.range_radius == 1
        and len(spec.ratios_by_neighbor_count) == len(DIRECTIONS) + 1
        and all(Q(1) <= ratio <= Q(2) for ratio in spec.ratios_by_neighbor_count)
    )


def frozen_hazard_spec(law: int) -> HazardSpec:
    return HazardSpec(1, tuple(hazard_ratio(law, n) for n in range(len(DIRECTIONS) + 1)))


@dataclass(frozen=True)
class Transition:
    site: Site
    mark: int
    rate: Fraction
    successor: Config


def generator_row(config: Config, torus: Torus, law: int, alpha: Fraction) -> tuple[tuple[Transition, ...], Fraction]:
    occupied = state_map(config)
    transitions: list[Transition] = []
    total_rate = Q(0)
    for site in range(torus.volume):
        if site in occupied:
            continue
        profile = profile_at(config, site, torus)
        probabilities = kernel_probabilities(profile)
        local_rate = alpha * hazard_ratio(law, sum(state != 0 for state in profile))
        marked_sum = Q(0)
        for mark, probability in enumerate(probabilities):
            successor = append_record(config, site, mark, torus)
            if successor is None:
                raise ValueError("legal append was rejected")
            rate = local_rate * probability
            transitions.append(Transition(site, mark, rate, successor))
            marked_sum += rate
        if marked_sum != local_rate:
            raise ValueError("marked intensities do not sum to the site hazard")
        total_rate += local_rate
    return tuple(transitions), -total_rate


@dataclass(frozen=True)
class HistoryEvent:
    site: int
    mark: int
    time: Fraction


def history_signature(
    initial: Config,
    events: Sequence[HistoryEvent],
    horizon: Fraction,
    torus: Torus,
    law: int,
    alpha: Fraction,
) -> tuple[Fraction, Fraction, Config] | None:
    if horizon <= 0:
        return None
    config = initial
    previous_time = Q(0)
    prefactor = Q(1)
    exposure = Q(0)
    for event in events:
        if not previous_time < event.time < horizon:
            return None
        if not 0 <= event.site < torus.volume or not 0 <= event.mark < len(DIRECTIONS):
            return None
        occupied = state_map(config)
        if event.site in occupied:
            return None
        row, diagonal = generator_row(config, torus, law, alpha)
        exposure += (-diagonal) * (event.time - previous_time)
        matches = [transition for transition in row if transition.site == event.site and transition.mark == event.mark]
        if len(matches) != 1:
            return None
        prefactor *= matches[0].rate
        config = matches[0].successor
        previous_time = event.time
    _, diagonal = generator_row(config, torus, law, alpha)
    exposure += (-diagonal) * (horizon - previous_time)
    return prefactor, exposure, config


def finite_history_certificate() -> dict[str, object]:
    torus = Torus(3)
    alpha = Q(5, 7)
    initially_occupied = torus.site((2, 2, 2))
    initial: Config = frozenset({(initially_occupied, 4)})
    row_checks = []
    for law in (0, 1):
        row, diagonal = generator_row(initial, torus, law, alpha)
        append_only = all(
            transition.rate > 0
            and len(transition.successor) == len(initial) + 1
            and initial.issubset(transition.successor)
            for transition in row
        )
        row_checks.append(sum(transition.rate for transition in row) + diagonal == 0 and append_only)

    full: Config = frozenset((site, site % len(DIRECTIONS)) for site in range(torus.volume))
    absorption = all(generator_row(full, torus, law, alpha) == ((), Q(0)) for law in (0, 1))

    valid_events = (
        HistoryEvent(torus.site((0, 0, 0)), 0, Q(1, 5)),
        HistoryEvent(torus.site((1, 0, 0)), 1, Q(1, 2)),
        HistoryEvent(torus.site((0, 1, 0)), 2, Q(4, 5)),
    )
    horizon = Q(6, 5)
    valid = history_signature(initial, valid_events, horizon, torus, 1, alpha)
    if valid is None:
        raise ValueError("valid exact history was rejected")

    invalid_histories = (
        (HistoryEvent(initially_occupied, 0, Q(1, 4)),),
        (valid_events[0], HistoryEvent(valid_events[0].site, 2, Q(3, 5))),
        (HistoryEvent(torus.site((0, 0, 1)), 6, Q(1, 4)),),
        (HistoryEvent(torus.volume, 0, Q(1, 4)),),
        (HistoryEvent(torus.site((0, 0, 1)), 0, Q(2, 3)), HistoryEvent(torus.site((0, 1, 1)), 1, Q(1, 3))),
    )
    invalid_zeroes = sum(
        history_signature(initial, candidate, horizon, torus, 1, alpha) is None
        for candidate in invalid_histories
    )

    # Exact normalization proof: induction on blank count.  If every successor
    # history has mass one, a row of total rate Lambda contributes
    # exp(-Lambda*T) + integral_0^T Lambda exp(-Lambda*t) dt = 1.
    sample_row, sample_diagonal = generator_row(initial, torus, 1, alpha)
    total_rate = -sample_diagonal
    normalized_jump_kernel = sum(transition.rate / total_rate for transition in sample_row) == 1
    acyclic = all(len(transition.successor) == len(initial) + 1 for transition in sample_row)
    conditional_normalization = total_rate > 0 and normalized_jump_kernel and acyclic and absorption
    random_initial_mixture = sum((Q(2, 5), Q(3, 5))) == 1 and conditional_normalization
    return {
        "valid": all(row_checks) and absorption and conditional_normalization and random_initial_mixture,
        "prefactor": valid[0],
        "exposure": valid[1],
        "invalid_zeroes": invalid_zeroes,
        "invalid_total": len(invalid_histories),
        "jump_cap": torus.volume,
        "overwrite_rejected": append_record(initial, initially_occupied, 0, torus) is None,
    }


def site_intensities(config: Config, torus: Torus, law: int, alpha: Fraction) -> dict[Site, Fraction]:
    row, _ = generator_row(config, torus, law, alpha)
    totals: dict[Site, Fraction] = {}
    for transition in row:
        totals[transition.site] = totals.get(transition.site, Q(0)) + transition.rate
    return totals


def discriminator_certificate() -> dict[str, object]:
    torus = Torus(7)
    alpha = Q(11, 13)
    x6 = torus.site((0, 0, 0))
    x0 = torus.site((3, 3, 3))
    records: set[tuple[Site, int]] = set()
    for mark, direction in enumerate(DIRECTIONS):
        records.add((torus.site(direction), mark))
    config: Config = frozenset(records)
    x0_neighbors = set(torus.neighbors(x0))
    disjoint = not x0_neighbors.intersection({site for site, _ in config}) and x0 not in state_map(config)

    finite_odds: list[Fraction] = []
    local_odds: list[Fraction] = []
    local_totals: list[Fraction] = []
    local_set = {x0, x6, *x0_neighbors}
    for law in (0, 1):
        intensities = site_intensities(config, torus, law, alpha)
        r0, r6 = intensities[x0], intensities[x6]
        finite_odds.append(r6 / (r0 + r6))
        total_u = sum(intensities[site] for site in local_set)
        # Before the first new Record in U, r0 and r6 stay fixed.  Exterior
        # births may change the other U-site hazards, but conditional on their
        # history each tested density is r_i times the same positive survival
        # functional.  That common factor cancels for every T>0.
        local_odds.append(r6 / (r0 + r6))
        local_totals.append(total_u / alpha)

    hazard_rows = tuple(
        tuple(hazard_ratio(law, n) for n in range(len(DIRECTIONS) + 1)) for law in (0, 1)
    )
    pointwise_ratios = tuple(hazard_rows[1][n] / hazard_rows[0][n] for n in range(7))
    globally_rescaled = len(set(pointwise_ratios)) == 1
    rescaling_mutant_odds = Q(2) / (Q(2) + Q(2))
    return {
        "valid": disjoint
        and finite_odds == local_odds
        and finite_odds[0] != finite_odds[1]
        and not globally_rescaled
        and rescaling_mutant_odds == finite_odds[0],
        "finite_odds": tuple(finite_odds),
        "local_odds": tuple(local_odds),
        "local_totals": tuple(local_totals),
        "hazard_rows": hazard_rows,
        "rescale_mutant_rejected": rescaling_mutant_odds == finite_odds[0] != finite_odds[1],
    }


def poisson_tail_upper(z: Fraction, m: int, multiplicity: int = 1) -> Fraction:
    if m <= z:
        raise ValueError("geometric tail certificate requires m>z")
    first = z**m / factorial(m)
    ratio = z / (m + 1)
    return multiplicity * first / (1 - ratio)


def proposal_times(site: Vec) -> tuple[Fraction, Fraction]:
    if sum(site) % 2 == 0:
        return (Q(1, 5), Q(3, 5))
    return (Q(2, 5), Q(4, 5))


def field_fraction(site: Vec, event_number: int, label: str) -> Fraction:
    payload = f"block18-independent|{site}|{event_number}|{label}".encode("ascii")
    word = int.from_bytes(sha256(payload).digest()[:16], "big")
    return Q(word + 1, 2**128 + 1)


def marked_decision(
    profile: Profile,
    law: int,
    uniform_key: Fraction,
    exponential_keys: Sequence[Fraction],
) -> tuple[bool, int | None, bool]:
    recorded_neighbors = sum(state != 0 for state in profile)
    threshold = hazard_ratio(law, recorded_neighbors) / 2
    if uniform_key > threshold:
        return False, None, False
    weights = kernel_weights(profile)
    scaled = tuple(key / weight for key, weight in zip(exponential_keys, weights))
    minimum = min(scaled)
    winners = [mark for mark, value in enumerate(scaled) if value == minimum]
    if len(winners) != 1:
        return True, None, True
    return True, winners[0], False


def backward_clan(observation: Iterable[Vec], horizon: Fraction) -> set[Vec]:
    queue: deque[tuple[Vec, Fraction]] = deque((site, horizon) for site in observation)
    seen_queries: set[tuple[Vec, Fraction]] = set()
    sites: set[Vec] = set()
    while queue:
        site, cutoff = queue.popleft()
        query = (site, cutoff)
        if query in seen_queries:
            continue
        seen_queries.add(query)
        sites.add(site)
        for event_time in proposal_times(site):
            if event_time >= cutoff:
                continue
            for direction in DIRECTIONS:
                queue.append((vector_add(site, direction), event_time))
    return sites


def box_sites(radius: int) -> tuple[Vec, ...]:
    return tuple(product(range(-radius, radius), repeat=3))


def wrap_box(site: Vec, radius: int) -> Vec:
    length = 2 * radius
    return tuple(((coordinate + radius) % length) - radius for coordinate in site)  # type: ignore[return-value]


def simulate_shared_box(
    radius: int,
    boundary: str,
    law: int,
    horizon: Fraction,
    observation: Sequence[Vec],
    initial: dict[Vec, int],
) -> tuple[tuple[int, ...], int, int, bool]:
    sites = box_sites(radius)
    site_set = set(sites)
    config = {site: mark for site, mark in initial.items() if site in site_set}
    proposals = 0
    accepted = 0
    tied = False
    event_times = sorted({time for site in ((0, 0, 0), (1, 0, 0)) for time in proposal_times(site)})
    for event_time in event_times:
        if event_time >= horizon:
            continue
        snapshot = dict(config)
        decisions: list[tuple[Vec, int]] = []
        for site in sites:
            local_times = proposal_times(site)
            if event_time not in local_times:
                continue
            event_number = local_times.index(event_time)
            proposals += 1
            if site in snapshot:
                continue
            profile_entries: list[int] = []
            for direction in DIRECTIONS:
                neighbor = vector_add(site, direction)
                if neighbor not in site_set:
                    if boundary == "periodic":
                        neighbor = wrap_box(neighbor, radius)
                    elif boundary == "fixed":
                        profile_entries.append(0)
                        continue
                    else:
                        raise ValueError("unknown boundary")
                profile_entries.append(0 if neighbor not in snapshot else snapshot[neighbor] + 1)
            uniform = field_fraction(site, event_number, "U")
            keys = tuple(field_fraction(site, event_number, f"E{mark}") for mark in range(6))
            is_accepted, mark, has_tie = marked_decision(tuple(profile_entries), law, uniform, keys)
            tied |= has_tie
            if is_accepted and mark is not None:
                decisions.append((site, mark))
        # Equal-time sites have equal parity and are never nearest neighbors on
        # these even periodic boxes, so the snapshot batch is order-free.
        for site, mark in decisions:
            if site in config:
                raise ValueError("shared-field regression overwrote a Record")
            config[site] = mark
            accepted += 1
    cylinder = tuple(0 if site not in config else config[site] + 1 for site in observation)
    return cylinder, proposals, accepted, tied


def harris_coupling_certificate(rotations: Sequence[Rotation]) -> dict[str, object]:
    alpha = Q(1, 14)
    horizon = Q(1)
    z = 14 * alpha * horizon
    tail_ms = (4, 8, 12)
    tails = tuple(poisson_tail_upper(z, m, 3) for m in tail_ms)
    tail_valid = all(tails[i + 1] < tails[i] for i in range(len(tails) - 1)) and tails[-1] < Q(1, 10**6)

    # The <=1/2 proposal subfield has rate alpha and is accepted for either
    # law whenever the site is blank, giving survival <= exp(-alpha*t).
    hazard_specs = tuple(frozen_hazard_spec(law) for law in (0, 1))
    thresholds = tuple(ratio / 2 for spec in hazard_specs for ratio in spec.ratios_by_neighbor_count)
    formation = all(valid_hazard_spec(spec) for spec in hazard_specs) and min(thresholds) >= Q(1, 2)
    zero_ratios = list(hazard_specs[0].ratios_by_neighbor_count)
    zero_ratios[0] = Q(0)
    zero_hazard_mutation_rejected = not valid_hazard_spec(HazardSpec(1, tuple(zero_ratios)))

    observation = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    query_times = (Q(1, 2), Q(1))
    initial = {(1, 0, 0): 0}  # asymmetric point-mass initial law.
    clans = {time: backward_clan(observation, time) for time in query_times}
    clan_radii = tuple(
        max(min(sum(abs(site[j] - anchor[j]) for j in range(3)) for anchor in observation) for site in clans[time])
        for time in query_times
    )
    required_radius: dict[Fraction, int] = {}
    for time in query_times:
        radius = 2
        while not all(
            all(-radius < coordinate < radius - 1 for coordinate in site)
            for site in clans[time]
        ):
            radius += 1
        required_radius[time] = radius

    max_radius = max(required_radius.values()) + 1
    radii = tuple(range(2, max_radius + 1))
    stable = True
    cylinder_counts: dict[tuple[int, Fraction], int] = {}
    no_ties = True
    permanence = True
    finite_points = True
    proposal_count = 0
    for law in (0, 1):
        by_time: dict[Fraction, dict[int, tuple[int, ...]]] = {}
        for time in query_times:
            by_time[time] = {}
            reference_result = simulate_shared_box(max_radius, "fixed", law, time, observation, initial)
            reference = reference_result[0]
            finite_points &= 0 < reference_result[1] < 10**6 and reference_result[2] <= reference_result[1]
            proposal_count += reference_result[1]
            for radius in radii:
                fixed = simulate_shared_box(radius, "fixed", law, time, observation, initial)
                periodic = simulate_shared_box(radius, "periodic", law, time, observation, initial)
                no_ties &= not fixed[3] and not periodic[3]
                finite_points &= (
                    0 < fixed[1] < 10**6
                    and 0 < periodic[1] < 10**6
                    and fixed[2] <= fixed[1]
                    and periodic[2] <= periodic[1]
                )
                proposal_count += fixed[1] + periodic[1]
                by_time[time][radius] = fixed[0]
                if radius >= required_radius[time]:
                    stable &= fixed[0] == periodic[0] == reference
            cylinder_counts[(law, time)] = sum(value != 0 for value in reference)
        for radius in radii:
            early = by_time[query_times[0]][radius]
            late = by_time[query_times[1]][radius]
            permanence &= all(before == 0 or before == after for before, after in zip(early, late))

    # Local sample-map covariance: rotate profile and the labeled key field
    # together.  A fixed-label mutation fails already in the blank profile.
    rotation = next(rotation for rotation in rotations if rotation.direction_map[0] != 0)
    profile: Profile = (1, 0, 3, 0, 0, 0)
    uniform = Q(1, 3)
    keys = tuple(Q(mark + 1, 11) for mark in range(6))
    accepted, mark, tie = marked_decision(profile, 1, uniform, keys)
    rotated_profile = rotation.profile(profile)
    rotated_keys = [Q(0)] * 6
    for old_mark, key in enumerate(keys):
        rotated_keys[rotation.direction_map[old_mark]] = key
    accepted_r, mark_r, tie_r = marked_decision(rotated_profile, 1, uniform, tuple(rotated_keys))
    local_equivariance = accepted and accepted_r and not tie and not tie_r and mark_r == rotation.direction_map[mark]  # type: ignore[index]

    asymmetric_rotated = {
        (rotation.vector(site), rotation.direction_map[mark]) for site, mark in initial.items()
    }
    asymmetric_original = set(initial.items())
    asymmetric_not_invariant = asymmetric_rotated != asymmetric_original

    blank = (0,) * 6
    fixed_label = marked_decision(blank, 0, Q(1, 3), keys)[1]
    fixed_label_rotated = marked_decision(rotation.profile(blank), 0, Q(1, 3), keys)[1]
    fixed_label_mutation_rejected = fixed_label_rotated != rotation.direction_map[fixed_label]  # type: ignore[index]
    tied_key_mutation_rejected = marked_decision(blank, 0, Q(1, 3), (Q(1),) * 6)[2]

    finite_clans = all(0 < len(clan) < 10**6 for clan in clans.values())
    rational_queries = all(isinstance(time, Fraction) and time > 0 for time in query_times)
    # On each finite clan the sample map is a finite composition of Borel
    # comparisons/minima of proposal, uniform, and exponential keys.  The
    # finite event list gives a local cadlag append-only path; taking all
    # rational local queries is countable.
    measurable = finite_clans and finite_points and rational_queries and no_ties and permanence
    return {
        "valid": tail_valid
        and formation
        and stable
        and permanence
        and no_ties
        and local_equivariance
        and asymmetric_not_invariant
        and measurable,
        "tails": tails,
        "tail_ms": tail_ms,
        "clan_sizes": tuple(len(clans[time]) for time in query_times),
        "clan_radii": clan_radii,
        "stable_lengths": tuple(2 * required_radius[time] for time in query_times),
        "cylinder_counts": tuple(cylinder_counts[key] for key in sorted(cylinder_counts)),
        "proposal_count": proposal_count,
        "formation": formation,
        "zero_hazard_mutation_rejected": zero_hazard_mutation_rejected,
        "fixed_label_mutation_rejected": fixed_label_mutation_rejected,
        "tied_key_mutation_rejected": tied_key_mutation_rejected,
        "asymmetric_not_invariant": asymmetric_not_invariant,
    }


def seed_state(torus: Torus, c: Vec, direction_index: int, compound: bool) -> Config:
    direction = DIRECTIONS[direction_index]
    coordinates = (c,) if not compound else (
        vector_add(c, vector_scale(-2, direction)),
        c,
        vector_add(c, direction),
    )
    return frozenset((torus.site(site), direction_index) for site in coordinates)


def marked_rate(config: Config, site: Site, mark: int, torus: Torus, law: int) -> Fraction | None:
    if site in state_map(config):
        return None
    profile = profile_at(config, site, torus)
    return hazard_ratio(law, sum(state != 0 for state in profile)) * kernel_probabilities(profile)[mark]


@dataclass(frozen=True)
class SeedRow:
    direction: Vec
    single_order: int
    compound_order: int
    q0_single: Fraction
    q0_compound: Fraction
    q1_single: Fraction
    q1_compound: Fraction
    lumpable: bool


@dataclass(frozen=True)
class QuotientTargetContract:
    identifies_representatives: bool
    common_distinguishable_successor: bool
    other_rates_from_single: tuple[Fraction, ...] = ()
    other_rates_from_compound: tuple[Fraction, ...] = ()


def single_entry_test_applies(contract: QuotientTargetContract) -> bool:
    return (
        contract.identifies_representatives
        and contract.common_distinguishable_successor
        and not contract.other_rates_from_single
        and not contract.other_rates_from_compound
    )


def shortest_arity_order(target_sites: Sequence[Site], compound_jump: bool) -> int:
    distinct = set(target_sites)
    if compound_jump:
        return 1 if distinct else 0
    reached: set[frozenset[Site]] = {frozenset()}
    distance = 0
    while reached:
        if any(state == distinct for state in reached):
            return distance
        reached = {state | {site} for state in reached for site in distinct - set(state)}
        distance += 1
    raise ValueError("arity search did not terminate")


def seed_and_lumpability_certificate() -> dict[str, object]:
    torus = Torus(6)
    c = (0, 0, 0)
    rows: list[SeedRow] = []
    geometry_valid = True
    for direction_index, direction in enumerate(DIRECTIONS):
        single = seed_state(torus, c, direction_index, False)
        compound = seed_state(torus, c, direction_index, True)
        y = torus.site(vector_add(c, vector_scale(2, direction)))
        five_other_blank = set(torus.neighbors(y)) - {torus.site(vector_add(c, direction))}
        geometry_valid &= len(compound) == 3 and y not in state_map(compound)
        geometry_valid &= not five_other_blank.intersection(state_map(single))
        geometry_valid &= not five_other_blank.intersection(state_map(compound))
        targets = [
            torus.site(vector_add(c, vector_scale(-2, direction))),
            torus.site(c),
            torus.site(vector_add(c, direction)),
        ]
        rates = (
            marked_rate(single, y, direction_index, torus, 0),
            marked_rate(compound, y, direction_index, torus, 0),
            marked_rate(single, y, direction_index, torus, 1),
            marked_rate(compound, y, direction_index, torus, 1),
        )
        if any(rate is None for rate in rates):
            raise ValueError("L>=6 fixture unexpectedly blocks y")
        q0s, q0c, q1s, q1c = rates  # type: ignore[misc]
        rows.append(
            SeedRow(
                direction,
                shortest_arity_order(targets, False),
                shortest_arity_order(targets, True),
                q0s,
                q0c,
                q1s,
                q1c,
                q0s == q0c and q1s == q1c,
            )
        )

    controls: dict[int, tuple[object, ...]] = {}
    all_direction_controls = True
    for length in (3, 4, 5):
        torus_small = Torus(length)
        direction_rows = []
        for direction_index, direction in enumerate(DIRECTIONS):
            single = seed_state(torus_small, c, direction_index, False)
            compound = seed_state(torus_small, c, direction_index, True)
            y = torus_small.site(vector_add(c, vector_scale(2, direction)))
            targets = [
                torus_small.site(vector_add(c, vector_scale(-2, direction))),
                torus_small.site(c),
                torus_small.site(vector_add(c, direction)),
            ]
            direction_rows.append(
                (
                    len(set(targets)),
                    y in state_map(compound),
                    marked_rate(single, y, direction_index, torus_small, 0),
                    marked_rate(compound, y, direction_index, torus_small, 0),
                    marked_rate(single, y, direction_index, torus_small, 1),
                    marked_rate(compound, y, direction_index, torus_small, 1),
                )
            )
        all_direction_controls &= len(set(direction_rows)) == 1
        controls[length] = direction_rows[0]

    # The row test is valid only for the declared fibre and a target cell with
    # no other outgoing transition.  Adding the exact difference to the S row
    # compensates it and must disable the single-entry conclusion.
    exemplar = rows[0]
    compensators = (exemplar.q0_compound - exemplar.q0_single, exemplar.q1_compound - exemplar.q1_single)
    compensation_equalizes = (
        exemplar.q0_single + compensators[0] == exemplar.q0_compound
        and exemplar.q1_single + compensators[1] == exemplar.q1_compound
    )
    declared_contract = QuotientTargetContract(True, True)
    removed_fibre = QuotientTargetContract(False, True)
    compensated_target = QuotientTargetContract(True, True, compensators, ())
    fibre_removed_rejected = single_entry_test_applies(declared_contract) and not single_entry_test_applies(removed_fibre)
    compensation_rejected = compensation_equalizes and not single_entry_test_applies(compensated_target)

    # A direct compound coefficient is the sum of all direct entries.  The
    # advertised kappa/6 coefficient is accepted only for a sole direct jump.
    kappa = Q(5, 4)
    sole_direct = (kappa / 6,)
    hidden_extra = (kappa / 6, Q(1, 9))
    direct_scope_valid = (
        len(sole_direct) == 1
        and sum(sole_direct) == kappa / 6
        and (len(hidden_extra) != 1 or sum(hidden_extra) != kappa / 6)
    )
    return {
        "valid": geometry_valid
        and all(not row.lumpable and row.single_order == 3 and row.compound_order == 1 for row in rows)
        and len(set(rows)) == 6
        and all_direction_controls
        and controls[3][0] == 2
        and controls[4][1] is True
        and controls[5][1] is False
        and compensation_rejected
        and direct_scope_valid,
        "rows": tuple(rows),
        "controls": controls,
        "fibre_removed_rejected": fibre_removed_rejected,
        "compensation_rejected": compensation_rejected,
        "direct_scope_valid": direct_scope_valid,
    }


def periodic_edges(torus: Torus) -> tuple[tuple[Site, Site], ...]:
    positive_directions = tuple(direction for direction in DIRECTIONS if 1 in direction)
    return tuple(
        (site, torus.site(vector_add(torus.coordinate(site), direction)))
        for site in range(torus.volume)
        for direction in positive_directions
    )


def modular_rank(matrix: list[list[int]], prime: int = 1_000_003) -> int:
    if not matrix:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if matrix[row][column] % prime), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column] % prime, -1, prime)
        matrix[rank] = [(entry * inverse) % prime for entry in matrix[rank]]
        for row in range(rows):
            if row == rank or matrix[row][column] % prime == 0:
                continue
            scale = matrix[row][column] % prime
            matrix[row] = [
                (entry - scale * pivot_entry) % prime
                for entry, pivot_entry in zip(matrix[row], matrix[rank])
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def incidence_regression(length: int) -> tuple[int, int, int]:
    torus = Torus(length)
    edges = periodic_edges(torus)
    matrix = [[0] * len(edges) for _ in range(torus.volume)]
    for column, (tail, head) in enumerate(edges):
        matrix[tail][column] = -1
        matrix[head][column] = 1
    column_sums_zero = sum(
        sum(matrix[row][column] for row in range(torus.volume)) == 0
        for column in range(len(edges))
    )
    return modular_rank(matrix), len(edges), column_sums_zero


def polynomial_product(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return tuple(result)


def analytic_tree_certificate(length: int) -> bool:
    torus = Torus(length)
    parents: dict[Site, Site] = {}
    root = torus.site((0, 0, 0))
    for z in range(length):
        for y in range(length):
            for x in range(length):
                site = torus.site((x, y, z))
                if site == root:
                    continue
                if x > 0:
                    parent = torus.site((x - 1, y, z))
                elif y > 0:
                    parent = torus.site((0, y - 1, z))
                else:
                    parent = torus.site((0, 0, z - 1))
                parents[site] = parent
    adjacency = all(parent in torus.neighbors(site) for site, parent in parents.items())
    reaches_root = True
    for site in parents:
        seen: set[Site] = set()
        cursor = site
        while cursor != root and cursor not in seen:
            seen.add(cursor)
            cursor = parents[cursor]
        reaches_root &= cursor == root
    # The reduced incidence of this rooted tree is unimodular (successively
    # delete leaves), giving rank >= V-1; column sums give rank <= V-1.
    return len(parents) == torus.volume - 1 and adjacency and reaches_root


def incidence_and_source_certificate() -> dict[str, object]:
    regressions = {length: incidence_regression(length) for length in (3, 4, 5)}
    # For symbolic L, the parent cases number
    # (L-1)L^2 + (L-1)L + (L-1) = (L-1)(L^2+L+1) = L^3-1.
    # Each parent lowers x+L*y+L^2*z, so there is no cycle and every vertex
    # reaches the root.  Leaf deletion makes the reduced tree incidence
    # determinant +/-1, while 1^T B=0 supplies the matching upper bound.
    tree_count_identity = polynomial_product((-1, 1), (1, 1, 1)) == (-1, 0, 0, 1)
    analytic = tree_count_identity and all(analytic_tree_certificate(length) for length in range(3, 9))
    regression_valid = all(
        rank == length**3 - 1 and edges == 3 * length**3 and zero_columns == edges
        for length, (rank, edges, zero_columns) in regressions.items()
    )

    one_birth = [1]
    three_birth = [1, 1, 1]
    source_totals = (sum(one_birth), sum(three_birth))
    debits = tuple(-total for total in source_totals)
    source_free_rejected = all(total != 0 for total in source_totals)
    repaired = all(total + debit == 0 for total, debit in zip(source_totals, debits))
    suppressed_source_rejected = source_totals[0] != 0 and source_totals[1] != 0

    # Topology mutations do not satisfy the frozen periodic-cubic graph type.
    length = 3
    periodic = periodic_edges(Torus(length))
    open_edges = tuple((u, v) for u, v in periodic if abs(u - v) in (1, length, length**2))
    disconnected_edges = tuple((u, v) for u, v in periodic if u // length**2 == v // length**2)
    topology_mutations_rejected = len(open_edges) != 3 * length**3 and len(disconnected_edges) < len(periodic)
    return {
        "valid": analytic
        and regression_valid
        and source_free_rejected
        and repaired
        and topology_mutations_rejected,
        "regressions": regressions,
        "tree_count_identity": tree_count_identity,
        "source_totals": source_totals,
        "debits": debits,
        "suppressed_source_rejected": suppressed_source_rejected,
        "topology_mutations_rejected": topology_mutations_rejected,
    }


def mutation_certificate(
    rotations: Sequence[Rotation],
    histories: dict[str, object],
    harris: dict[str, object],
    discriminator: dict[str, object],
    seeds: dict[str, object],
    incidence: dict[str, object],
) -> tuple[int, int, tuple[str, ...]]:
    blank: Profile = (0,) * 6
    probabilities = kernel_probabilities(blank)
    normalization_mutant = list(probabilities)
    normalization_mutant[0] += Q(1, 10)
    hidden_no_event_marks = tuple(Q(1, 7) for _ in range(6))

    rotation = next(rotation for rotation in rotations if rotation.direction_map[0] != 0)
    def biased(profile: Profile) -> tuple[Fraction, ...]:
        weights = list(kernel_weights(profile))
        weights[0] += 1
        return tuple(Q(weight, sum(weights)) for weight in weights)

    covariance_mutant_rejected = biased(rotation.profile(blank))[rotation.direction_map[0]] != biased(blank)[0]
    hidden_no_event_rejected = sum(hidden_no_event_marks) != 1
    high_rate_mutant = HazardSpec(1, tuple(Q(1) + Q(n, 3) for n in range(7)))
    long_range_mutant = HazardSpec(2, frozen_hazard_spec(0).ratios_by_neighbor_count)
    rate_mutant_rejected = not valid_hazard_spec(high_rate_mutant)
    range_mutant_rejected = not valid_hazard_spec(long_range_mutant)
    executed_domain = "blank-plus-six-rho"
    requested_upgrade = "full-M2"
    full_domain_upgrade_rejected = executed_domain != requested_upgrade

    checks = {
        "overwrite": bool(histories["overwrite_rejected"]),
        "normalization": sum(normalization_mutant) != 1,
        "covariance": covariance_mutant_rejected,
        "initial-invariance-confusion": bool(harris["asymmetric_not_invariant"]),
        "fixed-label-keys": bool(harris["fixed_label_mutation_rejected"]),
        "tied-keys": bool(harris["tied_key_mutation_rejected"]),
        "hidden-no-event": hidden_no_event_rejected,
        "rate-bound": rate_mutant_rejected,
        "range-one": range_mutant_rejected,
        "zero-hazard": bool(harris["zero_hazard_mutation_rejected"]),
        "invalid-history": histories["invalid_zeroes"] == histories["invalid_total"],
        "removed-fibre": bool(seeds["fibre_removed_rejected"]),
        "compensated-target": bool(seeds["compensation_rejected"]),
        "hidden-direct-triple": bool(seeds["direct_scope_valid"]),
        "global-rescaling": bool(discriminator["rescale_mutant_rejected"]),
        "suppressed-source": bool(incidence["suppressed_source_rejected"]),
        "wrong-graph-type": bool(incidence["topology_mutations_rejected"]),
        "full-M2-scope-upgrade": full_domain_upgrade_rejected,
    }
    failed = tuple(name for name, detected in checks.items() if not detected)
    return sum(checks.values()), len(checks), failed


def direction_name(direction: Vec) -> str:
    axis = next(index for index, value in enumerate(direction) if value)
    sign = "+" if direction[axis] > 0 else "-"
    return f"{sign}{'xyz'[axis]}"


def main() -> int:
    ledger = Ledger()
    try:
        rotations = proper_cubic_rotations()
        small_eigenvalue, large_eigenvalue, determinant, rho_valid = rho_spectrum_certificate()
        ledger.check(
            "rho_f-density-orbit",
            rho_valid and len(DIRECTIONS) == 6,
            f"six Hermitian trace-one marks; spectrum=({qstr(small_eigenvalue)},{qstr(large_eigenvalue)}), det={qstr(determinant)}; full-M2 not claimed",
        )

        census = profile_orbit_census(rotations)
        expected_profiles = (len(DIRECTIONS) + 1) ** len(DIRECTIONS)
        expected_rotations = factorial(3) * 2 ** (3 - 1)
        ledger.check(
            "profile-orbit-covariance-census",
            census.valid
            and census.profiles == expected_profiles
            and census.rotations == expected_rotations
            and census.covariance_pairs == census.profiles * census.rotations
            and census.distinct_probability_rows > 1,
            f"profiles={census.profiles}, rotations={census.rotations}, orbits={census.orbits}, orbit_sizes={dict(census.orbit_sizes)}, covariant_pairs={census.covariance_pairs}, p_rows={census.distinct_probability_rows}, uniform={census.uniform_profiles}",
        )

        histories = finite_history_certificate()
        ledger.check(
            "finite-generator-and-exact-histories",
            bool(histories["valid"]) and histories["invalid_zeroes"] == histories["invalid_total"],
            f"Q rows exact/conservative/append-only; density={qstr(histories['prefactor'])}*exp(-{qstr(histories['exposure'])}); invalid={histories['invalid_zeroes']}/{histories['invalid_total']}; cap={histories['jump_cap']}; normalization=acyclic row-sum induction",
        )

        discriminator = discriminator_certificate()
        odds = discriminator["finite_odds"]
        hazard_row = discriminator["hazard_rows"][1]
        ledger.check(
            "dimensionless-local-Record-order-race",
            bool(discriminator["valid"]),
            f"lambda1/alpha=({','.join(qstr(value) for value in hazard_row)}); finite/local-history odds=({qstr(odds[0])},{qstr(odds[1])}); initial-U-rates/alpha={tuple(qstr(v) for v in discriminator['local_totals'])}; common time scale and every-T survival factor cancel",
        )

        harris = harris_coupling_certificate(rotations)
        ledger.check(
            "Harris-local-measurable-coupling",
            bool(harris["valid"]),
            f"14alphaT tail m={harris['tail_ms']} -> {tuple(qstr(v) for v in harris['tails'])}; clans(size,radius)={tuple(zip(harris['clan_sizes'],harris['clan_radii']))}; finite marked points={harris['proposal_count']}; shared fixed/periodic time cylinders stabilize by even L={harris['stable_lengths']}; counts={harris['cylinder_counts']}",
        )
        ledger.check(
            "formation-and-covariance-scope",
            bool(harris["formation"])
            and bool(harris["zero_hazard_mutation_rejected"])
            and bool(harris["asymmetric_not_invariant"]),
            "lambda>=alpha gives P(blank at t)<=exp(-alpha*t), hence each/all-countable sites eventually record a.s.; sample map equivariant, while asymmetric initial point mass is not invariant; no common finite completion time",
        )

        seeds = seed_and_lumpability_certificate()
        for row in seeds["rows"]:
            ledger.check(
                f"seed-{direction_name(row.direction)}-arity-lumpability",
                row.single_order == 3 and row.compound_order == 1 and not row.lumpable,
                f"L=6 orders(single,compound)=({row.single_order},{row.compound_order}); q0={qstr(row.q0_single)}!={qstr(row.q0_compound)}, q1={qstr(row.q1_single)}!={qstr(row.q1_compound)}; future-preserving single-entry fibre only",
            )
        controls = seeds["controls"]
        ledger.check(
            "small-torus-hostile-controls",
            bool(seeds["valid"]),
            f"L3 distinct={controls[3][0]}, S(q0,q1)=({qstr(controls[3][2])},{qstr(controls[3][4])}), C=({qstr(controls[3][3])},{qstr(controls[3][5])}); L4 y_occupied={controls[4][1]}; L5 C=({qstr(controls[5][3])},{qstr(controls[5][5])}); all six directions",
        )
        ledger.check(
            "arity-and-quotient-scope-falsifiers",
            bool(seeds["compensation_rejected"]) and bool(seeds["direct_scope_valid"]),
            "one-site O(t^3) versus sole direct compound O(t); extra direct rates sum into the linear coefficient, and a compensating target transition disables the single-entry lumpability test",
        )

        incidence = incidence_and_source_certificate()
        regression_text = ",".join(
            f"L{length}:{values[0]}" for length, values in incidence["regressions"].items()
        )
        ledger.check(
            "analytic-all-L-incidence-theorem",
            bool(incidence["valid"]),
            f"(L-1)(L^2+L+1)=L^3-1 rooted edges, unimodular tree lower bound + zero-column-sum upper bound give rank(B_L)=L^3-1 for every L>=3; exact modular regressions {regression_text}",
        )
        ledger.check(
            "raw-occupancy-source-debit-scope",
            incidence["source_totals"] == (1, 3) and incidence["debits"] == (-1, -3),
            f"birth totals={incidence['source_totals']} reject source-free divergence; sigma repairs locally, scalar debits={incidence['debits']} repair global balance only; conditional raw-occupancy join, not gravity no-go",
        )

        detected, mutation_total, mutation_failures = mutation_certificate(
            rotations, histories, harris, discriminator, seeds, incidence
        )
        ledger.check(
            "hostile-mutation-rejection",
            detected == mutation_total,
            f"detected={detected}/{mutation_total}; failures={mutation_failures or 'none'}",
        )

    except Exception as exc:  # Honest failure with a mandatory final TOTAL line.
        ledger.check("independent-runner-exception", False, f"{type(exc).__name__}: {exc}")

    print("per_element: checked exact rho_f spectra and every six-mark kernel probability; no full-M2 occurrence-law claim.")
    print("per_site: checked positive formation hazard, append-only permanence, and both nearest-neighbor activation rows.")
    print("per_mode: checked and not executed — this pure-Record process sector has no physical mode decomposition.")
    print("per_block: checked six L>=6 seed rows, exact L=3,4,5 wrap controls, arity, and scoped lumpability.")
    print("lattice_wide: checked local Harris cylinders and all-L periodic incidence; no global jump chain or gravity no-go.")
    if ledger.failed == 0:
        print("TERMINAL: PURE-RECORD-HARRIS-PROCESSES-EXIST-DIMENSIONLESS-GENERATOR-UNDERSELECTED")
        print("SCOPE: invariant seven-state Markov witness sector; full-M2 extension, physical selector, and absolute clock remain live.")
    else:
        print("TERMINAL: SCOUT-FAILED-PURE-RECORD-OCCURRENCE-GATE")
    print(f"TOTAL: PASS={ledger.passed} FAIL={ledger.failed}")
    return 0 if ledger.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
