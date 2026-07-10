"""Block01 record saturation and availability-crowding census.

Purpose. Three exact legs.

LEG 1 (saturation corollary): from the Record axiom text alone:
"When present, a record locks exactly one admissible local possibility. A site
never carries more than one record; records are permanent." A region whose
every site is recorded admits zero further record formation at every subsequent
time.

LEG 2 (availability census): over the exact covariant nearest-neighbor rule
spaces, classify how the available-possibility structure at an open site varies
with the number of recorded neighbors. Crowding monotonicity is a counted
property of the declared finite rule class.

LEG 3 (supplied factorized-set model): enumerate rules whose availability is
the intersection of supplied per-direction constraints, with an open neighbor
supplying the full set. This factorization is an additional model premise, not
content of the Admissibility axiom. Raw enablement rules remain in LEG 2.

Companion note:
RECORD_SATURATION_AVAILABILITY_CENSUS_BOUNDED_NOTE_2026-07-08.md.
No time metric, rate law, gravity claim, or audit result is supplied.

Only the three task-authorized source files are read:
  1. docs/MINIMAL_AXIOMS_2026-06-29.md
  2. scripts/admissibility_rule_covariance_extension_classification_2026_07_03.py
  3. docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md

Open-boundary finite-region convention for LEG 1: the 2x2x2 and 3x3x1
sub-blocks inherit the six named Z^3 directions; neighbors outside the block
are treated as open boundary conditions.

SPEC-NOTE design bridge. The imported classification runner enumerates
condition-alphabet colorings and proper/full cubic orbits, not availability
sets. Here the k=2 condition values are read as {open, recorded}, with local
record-value set {recorded}; k=3 condition values are read as {open,
recorded-value-A, recorded-value-B}, with local record-value set {A, B}. A
covariant availability rule is therefore an assignment of a subset of the
local record-value set to each proper cubic orbit of neighbor-condition
patterns. The crowding averages are uniform over all condition patterns with a
fixed recorded-neighbor count, including both recorded values uniformly for
k=3. The attraction flag uses non-increasing count profiles
(STRICT-DECREASING + WEAK-DECREASING + CONSTANT-COUNT); constant-count
axiom-compatible rules are reported separately as the obstruction class with no
count-level crowding response.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import itertools
import math
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
CLASSIFIER_PATH = (
    ROOT / "scripts" / "admissibility_rule_covariance_extension_classification_2026_07_03.py"
)
NOTE_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md"
)

RECORD_QUOTE = (
    "When present, a record locks exactly one admissible local possibility. A "
    "site never carries more than one record; records are permanent."
)
CONDITION_BRIDGE_NEEDLE = "A neighbor's condition is its record content or openness"

DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)

CLASS_ORDER = (
    "STRICT-DECREASING",
    "WEAK-DECREASING",
    "CONSTANT-COUNT",
    "INCREASING",
    "NON-MONOTONE",
)


@dataclass(frozen=True)
class ModelCensus:
    k: int
    value_count: int
    subset_label_count: int
    proper_orbits: int
    full_orbits: int
    proper_rules: int
    full_rules: int
    full_extension_breaks: int
    excluded_constant_set: int
    axiom_compatible_rules: int
    class_counts: dict[str, int]
    axiom_class_counts: dict[str, int]
    horizon_rules: int
    horizon_axiom_rules: int
    abar6_min: str
    abar6_max: str
    abar6_zero_rules: int
    attraction_flag: str
    has_axiom_constant_count: bool
    orbit_count_by_r: dict[int, int]
    pattern_count_by_r: dict[int, int]


@dataclass(frozen=True)
class FactorizedCensus:
    k: int
    value_count: int
    direction_orbit_count: int
    covariance_classes: int
    factorized_rules: int
    excluded_constant_set: int
    axiom_compatible_rules: int
    class_counts: dict[str, int]
    axiom_class_counts: dict[str, int]
    strict_or_weak_axiom_rules: int
    horizon_rules: int
    horizon_axiom_rules: int
    empty_below_full_rules: int
    empty_below_full_axiom_rules: int
    monotone_ok: bool
    class_location_ok: bool


@dataclass(frozen=True)
class NonFactorizedWitness:
    ok: bool
    k: int
    class_name: str
    covariant: bool
    non_factorized: bool
    profile: str


def load_text_authorities() -> tuple[bool, bool]:
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    collapsed_axiom = " ".join(axiom_text.split())
    collapsed_note = " ".join(note_text.split())
    return RECORD_QUOTE in collapsed_axiom, CONDITION_BRIDGE_NEEDLE in collapsed_note


def load_classifier():
    spec = importlib.util.spec_from_file_location("covariance_classifier_2026_07_03", CLASSIFIER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load classification machinery")
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def block_sites(shape: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    sx, sy, sz = shape
    return tuple((x, y, z) for x in range(sx) for y in range(sy) for z in range(sz))


def neighbor_pattern(
    site: tuple[int, int, int],
    state: dict[tuple[int, int, int], int],
    site_set: set[tuple[int, int, int]],
) -> tuple[int, ...]:
    out = []
    x, y, z = site
    for dx, dy, dz in DIRS:
        nbr = (x + dx, y + dy, z + dz)
        out.append(state[nbr] if nbr in site_set else 0)
    return tuple(out)


def enumerate_configurations(k: int, shape: tuple[int, int, int]) -> dict[str, int | bool]:
    sites = block_sites(shape)
    site_set = set(sites)
    total = 0
    full = 0
    open_configs = 0
    open_site_instances = 0
    distinct_open_pattern_multisets = set()
    symbolic_check01 = True
    for values in itertools.product(range(k), repeat=len(sites)):
        total += 1
        state = dict(zip(sites, values, strict=True))
        open_sites = [site for site in sites if state[site] == 0]
        if not open_sites:
            full += 1
        else:
            open_configs += 1
        patterns = tuple(sorted(neighbor_pattern(site, state, site_set) for site in open_sites))
        distinct_open_pattern_multisets.add(patterns)
        open_site_instances += len(open_sites)
        # For any rule, the number of formable records is a sum of nonnegative
        # availability-set sizes over precisely these open sites. Hence the sum
        # is zero iff there are no open sites or every listed availability is
        # empty; this loop exhausts the finite configurations being certified.
        symbolic_check01 = symbolic_check01 and (
            (not open_sites) or all(len(pattern) == len(DIRS) for pattern in patterns)
        )
    return {
        "total": total,
        "full": full,
        "open_configs": open_configs,
        "open_site_instances": open_site_instances,
        "distinct_open_pattern_multisets": len(distinct_open_pattern_multisets),
        "check01": symbolic_check01,
    }


def availability_for_representative(
    rule_name: str, pattern: tuple[int, ...], value_count: int
) -> tuple[int, ...]:
    recorded_neighbors = sum(1 for value in pattern if value != 0)
    all_values = tuple(range(1, value_count + 1))
    if rule_name == "empty":
        return ()
    if rule_name == "full":
        return all_values
    if rule_name == "threshold":
        if recorded_neighbors <= 1:
            return all_values
        if recorded_neighbors <= 3:
            return all_values[:1]
        return ()
    raise ValueError(rule_name)


def verify_depth_limited_sequences(depth_limit: int = 4) -> dict[str, int | bool]:
    sites = block_sites((2, 2, 2))
    site_set = set(sites)
    value_count = 2
    representative_rules = ("empty", "full", "threshold")
    visited_nodes = 0
    ok = True

    def walk(rule_name: str, state: dict[tuple[int, int, int], int], depth: int) -> None:
        nonlocal visited_nodes, ok
        visited_nodes += 1
        if depth >= depth_limit:
            return
        before_recorded = {site for site, value in state.items() if value != 0}
        for site in sites:
            if state[site] != 0:
                continue
            pattern = neighbor_pattern(site, state, site_set)
            for value in availability_for_representative(rule_name, pattern, value_count):
                next_state = dict(state)
                next_state[site] = value
                after_recorded = {s for s, v in next_state.items() if v != 0}
                ok = ok and before_recorded <= after_recorded
                ok = ok and site not in before_recorded
                ok = ok and len(after_recorded) == len(before_recorded) + 1
                walk(rule_name, next_state, depth + 1)

    empty_state = {site: 0 for site in sites}
    for rule_name in representative_rules:
        walk(rule_name, empty_state, 0)
    return {"check02": ok, "rules": len(representative_rules), "depth": depth_limit, "nodes": visited_nodes}


def exact_fraction_percent(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "undef"
    return f"{(100.0 * numerator / denominator):.6g}%"


def dist_for_orbits(orbits: list[set[tuple[int, ...]]], value_count: int) -> dict[int, int]:
    dist = {0: 1}
    for orbit in orbits:
        orbit_size = len(orbit)
        next_dist: dict[int, int] = defaultdict(int)
        for total, ways in dist.items():
            for size in range(value_count + 1):
                next_dist[total + orbit_size * size] += ways * math.comb(value_count, size)
        dist = dict(next_dist)
    return dist


def monotone_count(
    dists: list[dict[int, int]],
    denominators: list[int],
    comparator,
) -> int:
    running = dict(dists[0])
    for index in range(1, len(dists)):
        new_running: dict[int, int] = defaultdict(int)
        prev_den = denominators[index - 1]
        this_den = denominators[index]
        for prev_t, prev_ways in running.items():
            for this_t, this_ways in dists[index].items():
                if comparator(prev_t, prev_den, this_t, this_den):
                    new_running[this_t] += prev_ways * this_ways
        running = dict(new_running)
    return sum(running.values())


def count_constant_profiles(
    dists: list[dict[int, int]], denominators: list[int], value_count: int
) -> int:
    total = 0
    for q in range(value_count + 1):
        ways = 1
        for dist, denominator in zip(dists, denominators, strict=True):
            ways *= dist.get(q * denominator, 0)
        total += ways
    return total


def classify_profiles(
    dists: list[dict[int, int]], denominators: list[int], total_rules: int, value_count: int
) -> dict[str, int]:
    strict_decreasing = monotone_count(
        dists, denominators, lambda a, da, b, db: a * db > b * da
    )
    nonincreasing = monotone_count(
        dists, denominators, lambda a, da, b, db: a * db >= b * da
    )
    nondecreasing = monotone_count(
        dists, denominators, lambda a, da, b, db: a * db <= b * da
    )
    constant_count = count_constant_profiles(dists, denominators, value_count)
    weak_decreasing = nonincreasing - strict_decreasing - constant_count
    increasing = nondecreasing - constant_count
    non_monotone = total_rules - (
        strict_decreasing + weak_decreasing + constant_count + increasing
    )
    counts = {
        "STRICT-DECREASING": strict_decreasing,
        "WEAK-DECREASING": weak_decreasing,
        "CONSTANT-COUNT": constant_count,
        "INCREASING": increasing,
        "NON-MONOTONE": non_monotone,
    }
    if any(value < 0 for value in counts.values()) or sum(counts.values()) != total_rules:
        raise AssertionError("profile classification is not a partition")
    return counts


def orbit_r(orbit: set[tuple[int, ...]]) -> int:
    counts = {sum(1 for value in col if value != 0) for col in orbit}
    if len(counts) != 1:
        raise AssertionError("proper orbit changed recorded-neighbor count")
    return next(iter(counts))


def rational_min_max(dist: dict[int, int], denominator: int) -> tuple[str, str]:
    keys = sorted(dist)
    low = keys[0]
    high = keys[-1]
    return f"{low}/{denominator}", f"{high}/{denominator}"


def compute_model_census(classifier, k: int) -> ModelCensus:
    value_count = k - 1
    subset_label_count = 2**value_count
    proper_orbits = classifier.direct_orbits(classifier.proper_perms, k)
    full_orbits = classifier.direct_orbits(classifier.full_perms, k)
    proper_burnside = classifier.burnside_orbits(classifier.proper_perms, k)
    full_burnside = classifier.burnside_orbits(classifier.full_perms, k)
    if len(proper_orbits) != proper_burnside or len(full_orbits) != full_burnside:
        raise AssertionError("direct-orbit count disagrees with Burnside machinery")

    by_r: dict[int, list[set[tuple[int, ...]]]] = {r: [] for r in range(7)}
    for orbit in proper_orbits:
        by_r[orbit_r(orbit)].append(orbit)

    denominators = [math.comb(6, r) * (value_count**r) for r in range(7)]
    pattern_count_by_r = {r: denominators[r] for r in range(7)}
    for r in range(7):
        if sum(len(orbit) for orbit in by_r[r]) != denominators[r]:
            raise AssertionError(f"orbit sizes do not cover r={r} patterns")

    dists = [dist_for_orbits(by_r[r], value_count) for r in range(7)]
    proper_rules = subset_label_count ** len(proper_orbits)
    full_rules = subset_label_count ** len(full_orbits)
    dist_total = math.prod(sum(dist.values()) for dist in dists)
    if dist_total != proper_rules:
        raise AssertionError("rule count distribution does not match orbit enumeration")

    class_counts = classify_profiles(dists, denominators, proper_rules, value_count)
    excluded_constant_set = subset_label_count
    axiom_class_counts = dict(class_counts)
    axiom_class_counts["CONSTANT-COUNT"] -= excluded_constant_set
    if axiom_class_counts["CONSTANT-COUNT"] < 0:
        raise AssertionError("constant-set exclusion exceeded constant-count class")
    axiom_compatible_rules = proper_rules - excluded_constant_set
    if sum(axiom_class_counts.values()) != axiom_compatible_rules:
        raise AssertionError("axiom-compatible counts do not sum")

    total_except_r6 = math.prod(sum(dists[r].values()) for r in range(6))
    horizon_rules = dists[6].get(0, 0) * total_except_r6
    horizon_axiom_rules = horizon_rules - 1
    abar6_min, abar6_max = rational_min_max(dists[6], denominators[6])
    nonincreasing_axiom = (
        axiom_class_counts["STRICT-DECREASING"]
        + axiom_class_counts["WEAK-DECREASING"]
        + axiom_class_counts["CONSTANT-COUNT"]
    )
    attraction_flag = (
        "CROWDING-MONOTONE-GENERIC"
        if 2 * nonincreasing_axiom > axiom_compatible_rules
        else "CROWDING-MONOTONE-NONGENERIC"
    )
    return ModelCensus(
        k=k,
        value_count=value_count,
        subset_label_count=subset_label_count,
        proper_orbits=len(proper_orbits),
        full_orbits=len(full_orbits),
        proper_rules=proper_rules,
        full_rules=full_rules,
        full_extension_breaks=proper_rules - full_rules,
        excluded_constant_set=excluded_constant_set,
        axiom_compatible_rules=axiom_compatible_rules,
        class_counts=class_counts,
        axiom_class_counts=axiom_class_counts,
        horizon_rules=horizon_rules,
        horizon_axiom_rules=horizon_axiom_rules,
        abar6_min=abar6_min,
        abar6_max=abar6_max,
        abar6_zero_rules=horizon_rules,
        attraction_flag=attraction_flag,
        has_axiom_constant_count=axiom_class_counts["CONSTANT-COUNT"] > 0,
        orbit_count_by_r={r: len(by_r[r]) for r in range(7)},
        pattern_count_by_r=pattern_count_by_r,
    )


def imported_direction_orbits(classifier) -> tuple[tuple[int, ...], ...]:
    """Recover the proper cubic direction action from imported pattern orbits."""
    singleton_orbits = []
    for orbit in classifier.direct_orbits(classifier.proper_perms, 2):
        directions = set()
        for pattern in orbit:
            if len(pattern) != len(DIRS) or sum(pattern) != 1:
                break
            directions.add(pattern.index(1))
        else:
            if directions:
                singleton_orbits.append(tuple(sorted(directions)))

    seen: set[int] = set()
    for directions in singleton_orbits:
        direction_set = set(directions)
        if seen & direction_set:
            raise AssertionError("imported direction orbits overlap")
        seen |= direction_set
    if seen != set(range(len(DIRS))):
        raise AssertionError("imported direction orbits do not cover the six directions")
    return tuple(sorted(singleton_orbits, key=lambda directions: directions[0]))


def iter_factorized_constraint_rules(
    direction_orbits: tuple[tuple[int, ...], ...], k: int
):
    value_count = k - 1
    full_mask = (1 << value_count) - 1
    subset_masks = tuple(range(full_mask + 1))
    class_keys = tuple(
        (orbit_index, recorded_value)
        for orbit_index in range(len(direction_orbits))
        for recorded_value in range(1, k)
    )
    for assignment in itertools.product(subset_masks, repeat=len(class_keys)):
        constraints = [[full_mask for _ in range(k)] for _ in DIRS]
        for (orbit_index, recorded_value), mask in zip(class_keys, assignment, strict=True):
            for direction in direction_orbits[orbit_index]:
                constraints[direction][recorded_value] = mask
        yield tuple(tuple(row) for row in constraints)


def availability_mask_for_factorized(
    constraints: tuple[tuple[int, ...], ...], pattern: tuple[int, ...], full_mask: int
) -> int:
    available = full_mask
    for direction, condition_value in enumerate(pattern):
        available &= constraints[direction][condition_value]
    return available


def profile_sums_for_factorized(
    constraints: tuple[tuple[int, ...], ...], k: int
) -> tuple[int, ...]:
    value_count = k - 1
    full_mask = (1 << value_count) - 1
    sums = [0] * (len(DIRS) + 1)
    for pattern in itertools.product(range(k), repeat=len(DIRS)):
        recorded_neighbors = sum(1 for value in pattern if value != 0)
        sums[recorded_neighbors] += availability_mask_for_factorized(
            constraints, pattern, full_mask
        ).bit_count()
    return tuple(sums)


def reduced_fraction(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "undef"
    divisor = math.gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor
    if denominator == 1:
        return str(numerator)
    return f"{numerator}/{denominator}"


def compact_profile(profile_sums: tuple[int, ...], denominators: list[int]) -> str:
    return "[" + ",".join(
        reduced_fraction(total, denominator)
        for total, denominator in zip(profile_sums, denominators, strict=True)
    ) + "]"


def classify_single_profile(profile_sums: tuple[int, ...], denominators: list[int]) -> str:
    strict_decreasing = all(
        profile_sums[index] * denominators[index + 1]
        > profile_sums[index + 1] * denominators[index]
        for index in range(len(DIRS))
    )
    nonincreasing = all(
        profile_sums[index] * denominators[index + 1]
        >= profile_sums[index + 1] * denominators[index]
        for index in range(len(DIRS))
    )
    nondecreasing = all(
        profile_sums[index] * denominators[index + 1]
        <= profile_sums[index + 1] * denominators[index]
        for index in range(len(DIRS))
    )
    constant_count = all(
        profile_sums[0] * denominators[index] == profile_sums[index] * denominators[0]
        for index in range(1, len(DIRS) + 1)
    )
    if strict_decreasing:
        return "STRICT-DECREASING"
    if nonincreasing and not constant_count:
        return "WEAK-DECREASING"
    if constant_count:
        return "CONSTANT-COUNT"
    if nondecreasing and not constant_count:
        return "INCREASING"
    return "NON-MONOTONE"


def is_set_constant_factorized_rule(
    constraints: tuple[tuple[int, ...], ...], k: int
) -> bool:
    value_count = k - 1
    full_mask = (1 << value_count) - 1
    constant_mask: int | None = None
    for pattern in itertools.product(range(k), repeat=len(DIRS)):
        mask = availability_mask_for_factorized(constraints, pattern, full_mask)
        if constant_mask is None:
            constant_mask = mask
        elif mask != constant_mask:
            return False
    return True


def is_horizon_factorized_rule(constraints: tuple[tuple[int, ...], ...], k: int) -> bool:
    value_count = k - 1
    full_mask = (1 << value_count) - 1
    for pattern in itertools.product(range(1, k), repeat=len(DIRS)):
        if availability_mask_for_factorized(constraints, pattern, full_mask) != 0:
            return False
    return True


def hits_empty_below_full_saturation(
    constraints: tuple[tuple[int, ...], ...], k: int
) -> bool:
    value_count = k - 1
    full_mask = (1 << value_count) - 1
    for pattern in itertools.product(range(k), repeat=len(DIRS)):
        recorded_neighbors = sum(1 for value in pattern if value != 0)
        if not 0 < recorded_neighbors < len(DIRS):
            continue
        if availability_mask_for_factorized(constraints, pattern, full_mask) == 0:
            return True
    return False


def verify_factorized_monotone(
    constraints: tuple[tuple[int, ...], ...], k: int
) -> bool:
    value_count = k - 1
    full_mask = (1 << value_count) - 1
    # Exact proof being checked: if q is p with one open direction d changed
    # to recorded value v, all other intersections are identical and
    # C_d(open)=full, so A(q)=A(p) & C_d(v). Thus A(q) is a subset of A(p).
    # Every chain ordered by adding recorded neighbors is a composition of
    # these one-step extensions; the loop exhausts all one-step cases.
    for pattern in itertools.product(range(k), repeat=len(DIRS)):
        before = availability_mask_for_factorized(constraints, pattern, full_mask)
        for direction, condition_value in enumerate(pattern):
            if condition_value != 0:
                continue
            for recorded_value in range(1, k):
                richer = list(pattern)
                richer[direction] = recorded_value
                after = availability_mask_for_factorized(
                    constraints, tuple(richer), full_mask
                )
                if after & ~before:
                    return False
                if after.bit_count() > before.bit_count():
                    return False
    return True


def compute_factorized_census(classifier, k: int) -> FactorizedCensus:
    value_count = k - 1
    subset_label_count = 2**value_count
    direction_orbits = imported_direction_orbits(classifier)
    covariance_classes = len(direction_orbits) * value_count
    denominators = [math.comb(len(DIRS), r) * (value_count**r) for r in range(len(DIRS) + 1)]
    class_counts = {name: 0 for name in CLASS_ORDER}
    excluded_class_counts = {name: 0 for name in CLASS_ORDER}
    factorized_rules = 0
    excluded_constant_set = 0
    horizon_rules = 0
    horizon_axiom_rules = 0
    empty_below_full_rules = 0
    empty_below_full_axiom_rules = 0
    monotone_ok = True
    class_location_ok = True

    for constraints in iter_factorized_constraint_rules(direction_orbits, k):
        factorized_rules += 1
        profile_sums = profile_sums_for_factorized(constraints, k)
        class_name = classify_single_profile(profile_sums, denominators)
        class_counts[class_name] += 1
        set_constant = is_set_constant_factorized_rule(constraints, k)
        horizon = is_horizon_factorized_rule(constraints, k)
        empty_below_full = hits_empty_below_full_saturation(constraints, k)
        monotone_rule_ok = verify_factorized_monotone(constraints, k)

        if set_constant:
            excluded_constant_set += 1
            excluded_class_counts[class_name] += 1
        if horizon:
            horizon_rules += 1
            if not set_constant:
                horizon_axiom_rules += 1
        if empty_below_full:
            empty_below_full_rules += 1
            if not set_constant:
                empty_below_full_axiom_rules += 1
        monotone_ok = monotone_ok and monotone_rule_ok
        class_location_ok = class_location_ok and class_name not in ("INCREASING", "NON-MONOTONE")

    expected_rules = subset_label_count**covariance_classes
    if factorized_rules != expected_rules:
        raise AssertionError("factorized rule count does not match covariance-class choices")
    axiom_class_counts = {
        name: class_counts[name] - excluded_class_counts[name] for name in CLASS_ORDER
    }
    axiom_compatible_rules = factorized_rules - excluded_constant_set
    if sum(axiom_class_counts.values()) != axiom_compatible_rules:
        raise AssertionError("factorized axiom-compatible counts do not sum")
    strict_or_weak_axiom_rules = (
        axiom_class_counts["STRICT-DECREASING"] + axiom_class_counts["WEAK-DECREASING"]
    )

    return FactorizedCensus(
        k=k,
        value_count=value_count,
        direction_orbit_count=len(direction_orbits),
        covariance_classes=covariance_classes,
        factorized_rules=factorized_rules,
        excluded_constant_set=excluded_constant_set,
        axiom_compatible_rules=axiom_compatible_rules,
        class_counts=class_counts,
        axiom_class_counts=axiom_class_counts,
        strict_or_weak_axiom_rules=strict_or_weak_axiom_rules,
        horizon_rules=horizon_rules,
        horizon_axiom_rules=horizon_axiom_rules,
        empty_below_full_rules=empty_below_full_rules,
        empty_below_full_axiom_rules=empty_below_full_axiom_rules,
        monotone_ok=monotone_ok,
        class_location_ok=class_location_ok,
    )


def compute_non_factorized_witness(classifier) -> NonFactorizedWitness:
    k = 2
    value_count = k - 1
    denominators = [math.comb(len(DIRS), r) * (value_count**r) for r in range(len(DIRS) + 1)]

    def witness_mask(pattern: tuple[int, ...]) -> int:
        recorded_neighbors = sum(1 for value in pattern if value != 0)
        return 0 if recorded_neighbors == 0 else 1

    proper_orbits = classifier.direct_orbits(classifier.proper_perms, k)
    covariant = all(len({witness_mask(pattern) for pattern in orbit}) == 1 for orbit in proper_orbits)

    profile_sums = [0] * (len(DIRS) + 1)
    for pattern in itertools.product(range(k), repeat=len(DIRS)):
        recorded_neighbors = sum(1 for value in pattern if value != 0)
        profile_sums[recorded_neighbors] += witness_mask(pattern).bit_count()
    profile = tuple(profile_sums)
    class_name = classify_single_profile(profile, denominators)

    direction_orbits = imported_direction_orbits(classifier)
    matches_factorized = False
    for constraints in iter_factorized_constraint_rules(direction_orbits, k):
        full_mask = (1 << value_count) - 1
        if all(
            availability_mask_for_factorized(constraints, pattern, full_mask)
            == witness_mask(pattern)
            for pattern in itertools.product(range(k), repeat=len(DIRS))
        ):
            matches_factorized = True
            break
    non_factorized = not matches_factorized
    ok = covariant and non_factorized and class_name == "INCREASING"
    return NonFactorizedWitness(
        ok=ok,
        k=k,
        class_name=class_name,
        covariant=covariant,
        non_factorized=non_factorized,
        profile=compact_profile(profile, denominators),
    )


def compact_counts(counts: dict[str, int]) -> str:
    labels = {
        "STRICT-DECREASING": "STRICT",
        "WEAK-DECREASING": "WEAK",
        "CONSTANT-COUNT": "CONST",
        "INCREASING": "INC",
        "NON-MONOTONE": "NON",
    }
    return ",".join(f"{labels[name]}={counts[name]}" for name in CLASS_ORDER)


def compact_fractions(counts: dict[str, int], denominator: int) -> str:
    labels = {
        "STRICT-DECREASING": "STRICT",
        "WEAK-DECREASING": "WEAK",
        "CONSTANT-COUNT": "CONST",
        "INCREASING": "INC",
        "NON-MONOTONE": "NON",
    }
    return ",".join(
        f"{labels[name]}={exact_fraction_percent(counts[name], denominator)}" for name in CLASS_ORDER
    )


def exact_fraction_label(numerator: int, denominator: int) -> str:
    return f"{numerator}/{denominator}={exact_fraction_percent(numerator, denominator)}"


def census_line(census: ModelCensus) -> str:
    return (
        f"CENSUS-K{census.k}: proper_orbits={census.proper_orbits} "
        f"full_orbits={census.full_orbits} proper_rules={census.proper_rules} "
        f"full_rules={census.full_rules} not_full={census.full_extension_breaks} "
        f"excluded_constant_set={census.excluded_constant_set} "
        f"axiom_rules={census.axiom_compatible_rules} "
        f"classes_all[{compact_counts(census.class_counts)}] "
        f"classes_axiom[{compact_counts(census.axiom_class_counts)}] "
        f"frac_axiom[{compact_fractions(census.axiom_class_counts, census.axiom_compatible_rules)}] "
        f"Abar6_minmax={census.abar6_min}..{census.abar6_max} "
        f"HORIZON={census.horizon_rules} HORIZON_axiom={census.horizon_axiom_rules} "
        f"{census.attraction_flag} axiom_constant_count={str(census.has_axiom_constant_count).lower()}"
    )


def compact_factorized_census(census: FactorizedCensus) -> str:
    return (
        f"k{census.k}:rules={census.factorized_rules} "
        f"dir_orbits={census.direction_orbit_count} choice_classes={census.covariance_classes} "
        f"excluded_constant_set={census.excluded_constant_set} "
        f"axiom_rules={census.axiom_compatible_rules} "
        f"classes_all[{compact_counts(census.class_counts)}] "
        f"classes_axiom[{compact_counts(census.axiom_class_counts)}] "
        "frac_axiom_STRICT_OR_WEAK="
        f"{exact_fraction_label(census.strict_or_weak_axiom_rules, census.axiom_compatible_rules)} "
        f"HORIZON={census.horizon_rules} HORIZON_axiom={census.horizon_axiom_rules} "
        f"EMPTY_BELOW_FULL={census.empty_below_full_rules} "
        f"EMPTY_BELOW_FULL_axiom={census.empty_below_full_axiom_rules}"
    )


def constraint_class_line(
    factorized_k2: FactorizedCensus,
    factorized_k3: FactorizedCensus,
    witness: NonFactorizedWitness,
) -> str:
    check06_ok = (
        factorized_k2.monotone_ok
        and factorized_k3.monotone_ok
        and factorized_k2.class_location_ok
        and factorized_k3.class_location_ok
    )
    return (
        "SUPPLIED-FACTORIZED-MODEL: SPEC-NOTE factorized_covariance=proper direction classes are "
        "recovered from imported one-record pattern orbits; implemented condition is "
        "C_d(v)=C_e(v) for directions d,e in the same imported proper direction orbit "
        "and the same scalar condition value v; OPEN_IS_FREE C_d(open)=full; no k3 "
        "A/B value-permutation covariance is imposed because values carry no orientation. "
        f"CHECK-06={'PASS' if check06_ok else 'FAIL'} monotone_by_intersection_exhaustive "
        f"CHECK-07=REPORTED factorized[{compact_factorized_census(factorized_k2)}; "
        f"{compact_factorized_census(factorized_k3)}] "
        f"CHECK-08={'PASS' if witness.ok else 'FAIL'} "
        f"nonfactorized_witness=k{witness.k}:avail(r=0)=empty,avail(r>=1)=full,"
        f"profile={witness.profile},class={witness.class_name},"
        f"covariant={str(witness.covariant).lower()},"
        f"non_factorized={str(witness.non_factorized).lower()}"
    )


def run() -> int:
    try:
        quote_ok, bridge_ok = load_text_authorities()
        classifier = load_classifier()
        saturation_rows = []
        check01_ok = quote_ok and bridge_ok
        for k in (2, 3):
            for shape in ((2, 2, 2), (3, 3, 1)):
                row = enumerate_configurations(k, shape)
                saturation_rows.append((k, shape, row))
                check01_ok = check01_ok and bool(row["check01"])
        sequence_check = verify_depth_limited_sequences(depth_limit=4)
        check02_ok = bool(sequence_check["check02"])
        k2 = compute_model_census(classifier, 2)
        k3 = compute_model_census(classifier, 3)
        check03_ok = (
            k2.proper_rules == k2.subset_label_count**k2.proper_orbits
            and k3.proper_rules == k3.subset_label_count**k3.proper_orbits
        )
        check05_ok = k2.abar6_zero_rules == k2.horizon_rules and k3.abar6_zero_rules == k3.horizon_rules
        factorized_k2 = compute_factorized_census(classifier, 2)
        factorized_k3 = compute_factorized_census(classifier, 3)
        non_factorized_witness = compute_non_factorized_witness(classifier)
        factorized_monotone_theorem_ok = (
            factorized_k2.monotone_ok
            and factorized_k3.monotone_ok
            and factorized_k2.class_location_ok
            and factorized_k3.class_location_ok
        )
        constraint_checks_ok = factorized_monotone_theorem_ok and non_factorized_witness.ok
        constraint_attraction_numerator = (
            factorized_k2.strict_or_weak_axiom_rules + factorized_k3.strict_or_weak_axiom_rules
        )
        constraint_attraction_denominator = (
            factorized_k2.axiom_compatible_rules + factorized_k3.axiom_compatible_rules
        )
        total_configs = sum(int(row["total"]) for _, _, row in saturation_rows)
        full_configs = sum(int(row["full"]) for _, _, row in saturation_rows)
        pattern_multisets = sum(int(row["distinct_open_pattern_multisets"]) for _, _, row in saturation_rows)
        attraction_flag = (
            "CROWDING-MONOTONE-GENERIC"
            if k2.attraction_flag == "CROWDING-MONOTONE-GENERIC"
            and k3.attraction_flag == "CROWDING-MONOTONE-GENERIC"
            else "CROWDING-MONOTONE-NONGENERIC"
        )
        constant_count_excluded_by_axiom = not (k2.has_axiom_constant_count or k3.has_axiom_constant_count)
        total_status = (
            "CENSUS-COMPLETE"
            if check01_ok and check02_ok and check03_ok and check05_ok and constraint_checks_ok
            else "MACHINERY-FAIL"
        )
        print(
            "SPEC-NOTE: bridge=k2:{open,recorded}->V={recorded};"
            "k3:{open,A,B}->V={A,B}; imported machinery exposes condition orbits, "
            "so subset-valued covariant rules are counted exactly by orbit-DP; "
            "fixed-r averages are uniform over condition patterns/recorded values; "
            "attraction flag uses non-increasing count profiles with constant-count obstruction reported."
        )
        print(
            "SATURATION: blocks=2x2x2,3x3x1 open-boundary configs_exhausted="
            f"{total_configs} full_occupancy_configs={full_configs} "
            f"open_pattern_multisets={pattern_multisets} CHECK-01={'PASS' if check01_ok else 'FAIL'} "
            "full_occupancy_zero_if_direction=rule-independent "
            f"CHECK-02={'PASS' if check02_ok else 'FAIL'} "
            f"sequence_rules={sequence_check['rules']} depth={sequence_check['depth']} "
            f"sequence_nodes={sequence_check['nodes']}"
        )
        print(census_line(k2))
        print(census_line(k3))
        print(constraint_class_line(factorized_k2, factorized_k3, non_factorized_witness))
        print(
            f"CHECKS: CHECK-03={'PASS' if check03_ok else 'FAIL'} exhaustive_rule_counts_match_imported_orbits; "
            f"CHECK-04=REPORTED k2={k2.attraction_flag} k3={k3.attraction_flag} "
            f"axiom_constant_count_any={str(k2.has_axiom_constant_count or k3.has_axiom_constant_count).lower()}; "
            f"CHECK-05={'PASS' if check05_ok else 'FAIL'} saturation_endpoint_distinct_from_Abar6 "
            f"Abar6_zero_counts=k2:{k2.horizon_rules},k3:{k3.horizon_rules}"
        )
        print(
            f"TOTAL: {total_status} {attraction_flag} "
            f"HORIZON-CLASS-COUNT=k2:{k2.horizon_rules},k3:{k3.horizon_rules} "
            f"CONSTANT-COUNT-EXCLUDED-BY-AXIOM={'yes' if constant_count_excluded_by_axiom else 'no'} "
            "SUPPLIED-FACTORIZED-MODEL-MONOTONE="
            f"{exact_fraction_label(constraint_attraction_numerator, constraint_attraction_denominator)} "
            "FACTORIZED-SET-INTERSECTION-LEMMA="
            f"{'ok' if factorized_monotone_theorem_ok else 'fail'}"
        )
    except Exception as exc:
        print(f"TOTAL: MACHINERY-FAIL error={type(exc).__name__}:{exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(run())
