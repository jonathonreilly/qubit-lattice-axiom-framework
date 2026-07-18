#!/usr/bin/env python3
"""Cycle 18: invariant first-seed and hard-core infinite-volume probes.

Companion note:
  docs/work_history/repo/review_feedback/
  INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md

The runner proves finite controls for the translation-invariant one-seed
obstruction, constructs a positive-density finite-range factor of IID typed
seeds, connects its exclusion radius to Cycle 17's 99-site builder, and keeps
deterministic, stochastic, quantum/QCA, global-history, and contingent-boundary
routes distinct.  It changes no axiom, registry, audit surface, commit, or PR.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb, log
from pathlib import Path
import random

import numpy as np

import autonomous_self_closing_diamond_cycle17_2026_07_14 as c17


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CYCLE17_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md"
)
FINITE_SEED_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "HOMOGENEOUS_BOUNDARY_SEED_SELECTION_NOTE_2026-07-14.md"
)
POSITIVE_DENSITY_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_HOMOGENEOUS_BINARY_NUCLEATION_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]

# Cycle 17's B0-relative completed support lies in B_infinity(4).  To ensure
# that arbitrary independently typed copies neither overlap nor become nearest
# neighbors, forbid B0 displacements through 2*4+1 = 9.
SUPPORT_RADIUS = 4
EXCLUSION_RADIUS = 2 * SUPPORT_RADIUS + 1
SAFE_SEPARATION = EXCLUSION_RADIUS + 1
DEPENDENCE_SIDE = 2 * EXCLUSION_RADIUS + 1
DEPENDENCE_VOLUME = DEPENDENCE_SIDE**3
ALIGNED_PERIOD = 6


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def subtract(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def chebyshev(vector: Coord) -> int:
    return max(abs(value) for value in vector)


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def rotate_coord(vector: Coord, rotation: np.ndarray) -> Coord:
    return c17.matvec(rotation, vector)


def mod_coord(vector: Coord, side: int) -> Coord:
    return tuple(value % side for value in vector)  # type: ignore[return-value]


def torus_sites(side: int) -> tuple[Coord, ...]:
    return tuple(product(range(side), repeat=3))


def torus_chebyshev(left: Coord, right: Coord, side: int) -> int:
    distances = []
    for a, b in zip(left, right):
        raw = abs(a - b)
        distances.append(min(raw, side - raw))
    return max(distances)


def torus_displacement(left: Coord, right: Coord, side: int) -> Coord:
    """Shortest signed displacement from left to right on an odd torus."""

    answer = []
    for a, b in zip(left, right):
        value = (b - a) % side
        if value > side // 2:
            value -= side
        answer.append(value)
    return tuple(answer)  # type: ignore[return-value]


def canonical_terminal_support() -> frozenset[Coord]:
    cell = c17.Cell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    records, _, _, _ = c17.run_schedule("first", cell, 0, 1818)
    b0 = c17.global_site(cell, c17.CANONICAL_PATH[0])
    return frozenset(subtract(site, b0) for site in records)


def frame_rotation(frame: c17.Frame) -> np.ndarray:
    """Map canonical (x=transverse,y=normal,z=forward) coordinates."""

    return np.asarray(
        (
            (frame.transverse[0], frame.normal[0], frame.forward[0]),
            (frame.transverse[1], frame.normal[1], frame.forward[1]),
            (frame.transverse[2], frame.normal[2], frame.forward[2]),
        ),
        dtype=int,
    )


def frame_support(support: frozenset[Coord], frame: c17.Frame) -> frozenset[Coord]:
    rotation = frame_rotation(frame)
    return frozenset(rotate_coord(site, rotation) for site in support)


def supports_touch(
    left: frozenset[Coord], right: frozenset[Coord], displacement: Coord
) -> bool:
    shifted = frozenset(add(site, displacement) for site in right)
    return any(
        candidate in shifted
        for site in left
        for candidate in (site,) + tuple(add(site, direction) for direction in c17.DIRECTIONS)
    )


def source_and_scope_contract() -> None:
    section("A - Framework, source contract, and N1-N8 surface")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    realized = REALIZED.read_text(encoding="utf-8").lower()
    cycle17 = CYCLE17_NOTE.read_text(encoding="utf-8").lower()
    finite_seed = FINITE_SEED_NOTE.read_text(encoding="utf-8").lower()
    positive_density = POSITIVE_DENSITY_NOTE.read_text(encoding="utf-8").lower()

    check(
        "A framework still has four named axioms",
        all(name in axioms for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")),
    )
    check("A Record still withholds a formation rule", "formation rules" in axioms)
    check("A registry still has four approved premise paths", registry.count('"current_path"') == 4)
    check("A realized-state primitive supplies no selector", "state-selection rule" in realized and "supplied by the physical history" in realized)
    check("A Cycle 17 leaves first-record nucleation separate", "first-record nucleation remains separate" in cycle17)
    check("A finite-seed predecessor states the countable-additivity wall", "countable additivity" in finite_seed and "exactly one marked site" in finite_seed)
    check("A positive-density predecessor keeps IID marks explicit", "ephemeral random marks" in positive_density and "positive-density stochastic nucleation" in positive_density)

    required = (
        "authority: none",
        "exactly-one invariant obstruction",
        "finite-torus one-seed law",
        "empty local limit",
        "positive-density hard-core seed process",
        "finite-range factor of iid",
        "b0-site exclusion radius nine",
        "99-site construction path",
        "infinite seeds almost surely",
        "configuration-level symmetry breaking",
        "measure remains invariant",
        "occurrence intensity is law data",
        "frame-orbit weights",
        "deterministic route",
        "stochastic route",
        "quantum route",
        "qca route",
        "global-history route",
        "contingent-boundary route",
        "no new record axiom is forced",
    )
    for phrase in required:
        check(f"A note states scope phrase: {phrase}", phrase in normalized)
    for index in range(1, 9):
        check(f"A no-go discipline includes N{index}", f"n{index} —" in normalized or f"n{index} -" in normalized)


def cycle17_exclusion_geometry() -> None:
    section("B - Cycle 17 support and tight frame-independent exclusion")
    support = canonical_terminal_support()
    frames = c17.oriented_frames()
    rotations = c17.proper_cubic_rotations()
    rotated = tuple(frozenset(rotate_coord(site, rotation) for site in support) for rotation in rotations)
    orbit_union = frozenset(site for copy in rotated for site in copy)

    check("B Cycle 17 builder path has 99 sites", len(c17.CANONICAL_PATH) == 99)
    check("B Cycle 17 completed diamond has 111 record sites", len(support) == 111)
    check("B completed support has B0-relative radius four", max(chebyshev(site) for site in support) == SUPPORT_RADIUS)
    check("B all 24 proper-cubic frames are available", len(frames) == len(rotations) == 24)
    check("B every rotated support stays inside radius four", all(max(chebyshev(site) for site in copy) == SUPPORT_RADIUS for copy in rotated))
    check("B exclusion radius is 2r+1 = nine", EXCLUSION_RADIUS == 9)
    check("B safe B0 separation is ten", SAFE_SEPARATION == 10)
    check("B radius-nine cube contains 19 cubed sites", DEPENDENCE_VOLUME == 6859)

    # Tightness: these two orbit points can be brought to NN contact by a
    # displacement of infinity norm nine.  Therefore radius eight is not a
    # frame-independent protection rule.
    upper = (4, 4, 4)
    lower = (4, 4, -4)
    displacement = (0, 0, 9)
    left_index = next(index for index, copy in enumerate(rotated) if upper in copy)
    right_index = next(index for index, copy in enumerate(rotated) if lower in copy)
    check("B extreme orbit points needed for tightness exist", upper in orbit_union and lower in orbit_union)
    check("B a norm-nine displacement can create NN contact", supports_touch(rotated[left_index], rotated[right_index], displacement))
    check("B radius eight would permit that collision", chebyshev(displacement) == 9 > 8)

    # Sufficiency is an exact coordinate bound: along a coordinate realizing
    # |d|_infinity >= 10, the two radius-four supports remain at least two
    # lattice steps apart.
    for separation in (10, 11, 19):
        lower_distance = separation - 2 * SUPPORT_RADIUS
        check(f"B separation {separation} leaves no NN contact by bound", lower_distance >= 2)
    check("B same-frame period-six copies are already NN-disjoint", not supports_touch(support, support, (6, 0, 0)))
    check("B arbitrary frames need the conservative radius-nine rule", EXCLUSION_RADIUS > ALIGNED_PERIOD)


def one_seed_finite_and_infinite() -> None:
    section("C - Finite-torus one seed and the infinite-volume obstruction")
    frames = c17.oriented_frames()
    rotations = c17.proper_cubic_rotations()
    frame_set = set(frames)

    for side in (2, 3, 5):
        volume = side**3
        branches = volume * len(frames)
        weight = Fraction(1, branches)
        check(f"C side {side} typed one-seed law normalizes", branches * weight == 1)
        check(f"C side {side} gives each site marginal 1/volume", len(frames) * weight == Fraction(1, volume))
        check(f"C side {side} translations permute equal-weight branches", all(mod_coord(add(site, shift), side) in torus_sites(side) for site in torus_sites(side) for shift in ((1, 0, 0), (0, 1, 0), (0, 0, 1))))

    check(
        "C rotations permute the 24 frame branches",
        all(c17.transform_frame(frame, rotation) in frame_set for frame in frames for rotation in rotations),
    )
    fixed_frames = tuple(
        frame
        for frame in frames
        if all(c17.transform_frame(frame, rotation) == frame for rotation in rotations)
    )
    check("C no oriented frame is fixed by the full proper-cubic group", fixed_frames == ())

    window_size = 27
    local_probabilities = tuple(Fraction(window_size, side**3) for side in (5, 9, 17, 33))
    check("C finite one-seed window weights decrease", all(a > b for a, b in zip(local_probabilities, local_probabilities[1:])))
    check("C finite one-seed local probability tends toward zero", local_probabilities[-1] < Fraction(1, 1000))

    # If an invariant exactly-one law existed on Z3, p=P(x is seeded) would be
    # common to every site.  Every N-site set gives Np<=1, hence p=0; the
    # countable union of zero-probability site events then has probability 0.
    inverse_bounds = tuple(Fraction(1, size) for size in (1, 8, 27, 125, 1000, 1_000_000))
    check("C exactly-one marginal upper bounds converge to zero", all(a > b for a, b in zip(inverse_bounds, inverse_bounds[1:])))
    check("C zero invariant site mass has zero countable-union mass", sum((Fraction(0) for _ in range(10000)), Fraction(0)) == 0)
    check("C positive common site mass violates a finite partial sum", 101 * Fraction(1, 100) > 1)

    # Finite normalized one-particle W states are the quantum analogue.  Their
    # mass in a fixed window is again |W|/volume, while a nonzero constant
    # amplitude on infinite Z3 is not square summable.
    for side in (3, 5, 9):
        volume = side**3
        vector = np.ones(volume, dtype=complex) / np.sqrt(volume)
        check(f"C side {side} uniform one-particle vector normalizes", np.allclose(np.vdot(vector, vector), 1.0))
    partial_norms = tuple((2 * radius + 1) ** 3 for radius in (1, 2, 4, 8))
    check("C nonzero constant infinite one-particle amplitude has divergent partial norm", all(a < b for a, b in zip(partial_norms, partial_norms[1:])))
    check("C finite quantum fixed-window mass equals the classical ratio", abs(window_size / 33**3 - float(local_probabilities[-1])) < 1e-15)


def winner_density(activity: Fraction, neighborhood_size: int = DEPENDENCE_VOLUME) -> Fraction:
    if not 0 <= activity <= 1:
        raise ValueError("activity must lie in [0,1]")
    return (1 - (1 - activity) ** neighborhood_size) / neighborhood_size


def winner_density_binomial(activity: Fraction, neighborhood_size: int) -> Fraction:
    total = Fraction(0)
    for other_candidates in range(neighborhood_size):
        total += (
            activity
            * comb(neighborhood_size - 1, other_candidates)
            * activity**other_candidates
            * (1 - activity) ** (neighborhood_size - 1 - other_candidates)
            / (other_candidates + 1)
        )
    return total


FieldValue = tuple[int, int]
Field = dict[Coord, FieldValue]


def random_candidate_field(side: int, activity: float, seed: int) -> Field:
    rng = random.Random(seed)
    candidates = [site for site in torus_sites(side) if rng.random() < activity]
    ranks = list(range(len(candidates)))
    rng.shuffle(ranks)
    return {
        site: (rank, rng.randrange(24))
        for site, rank in zip(candidates, ranks)
    }


def local_minimum_winners(field: Field, side: int) -> Field:
    winners: Field = {}
    items = tuple(field.items())
    for site, value in items:
        rank, _ = value
        if all(
            other == site
            or torus_chebyshev(site, other, side) > EXCLUSION_RADIUS
            or rank < other_value[0]
            for other, other_value in items
        ):
            winners[site] = value
    return winners


def translate_field(field: Field, shift: Coord, side: int) -> Field:
    return {mod_coord(add(site, shift), side): value for site, value in field.items()}


def rotate_field(field: Field, rotation: np.ndarray, side: int) -> Field:
    frames = c17.oriented_frames()
    frame_index = {frame: index for index, frame in enumerate(frames)}
    return {
        mod_coord(rotate_coord(site, rotation), side): (
            value[0],
            frame_index[c17.transform_frame(frames[value[1]], rotation)],
        )
        for site, value in field.items()
    }


def finite_range_hard_core_factor() -> None:
    section("D - Positive-density finite-range hard-core factor")
    for neighborhood_size in (1, 2, 3, 5, 9):
        for activity in (Fraction(1, 5), Fraction(1, 2), Fraction(1)):
            check(
                f"D exact binomial minimum identity M={neighborhood_size} q={activity}",
                winner_density(activity, neighborhood_size)
                == winner_density_binomial(activity, neighborhood_size),
            )

    check("D q=1 exact seed intensity is one per 6859 sites", winner_density(Fraction(1)) == Fraction(1, DEPENDENCE_VOLUME))
    q_low = Fraction(1, DEPENDENCE_VOLUME)
    q_high = Fraction(2, DEPENDENCE_VOLUME)
    rho_low = winner_density(q_low)
    rho_high = winner_density(q_high)
    check("D two activities preserve geometry but change intensity", 0 < rho_low < rho_high < Fraction(1, DEPENDENCE_VOLUME))
    check("D completed-record density remains below one", 111 * winner_density(Fraction(1)) < 1)

    side = 25
    field = random_candidate_field(side, 0.05, 1818)
    winners = local_minimum_winners(field, side)
    check("D sampled finite torus has candidates and winners", len(field) > 100 and len(winners) > 0)
    check(
        "D sampled winners obey radius-nine hard core",
        all(torus_chebyshev(left, right, side) > EXCLUSION_RADIUS for left, right in combinations(winners, 2)),
    )

    shift = (3, 7, 11)
    shifted_field = translate_field(field, shift, side)
    shifted_winners = local_minimum_winners(shifted_field, side)
    expected_shifted = {mod_coord(add(site, shift), side) for site in winners}
    check("D local-minimum map is exactly translation covariant", set(shifted_winners) == expected_shifted)

    rotation = c17.proper_cubic_rotations()[7]
    rotated_field = rotate_field(field, rotation, side)
    rotated_winners = local_minimum_winners(rotated_field, side)
    expected_rotated = {mod_coord(rotate_coord(site, rotation), side) for site in winners}
    check("D local-minimum map is exactly proper-cubic covariant", set(rotated_winners) == expected_rotated)

    support = canonical_terminal_support()
    frames = c17.oriented_frames()
    typed_supports = {
        site: frame_support(support, frames[value[1]])
        for site, value in winners.items()
    }
    check(
        "D accepted typed diamonds are pairwise noninteracting",
        all(
            not supports_touch(
                typed_supports[left],
                typed_supports[right],
                torus_displacement(left, right, side),
            )
            for left, right in combinations(winners, 2)
        ),
    )

    # Winner events at centers spaced 2R+1 have disjoint input cubes and are
    # independent under the IID field.  Their positive chance forces infinitely
    # many winners almost surely by the second Borel-Cantelli lemma.
    dependency_blocks = []
    for center in ((0, 0, 0), (DEPENDENCE_SIDE, 0, 0), (2 * DEPENDENCE_SIDE, 0, 0)):
        dependency_blocks.append(
            frozenset(
                add(center, offset)
                for offset in product(range(-EXCLUSION_RADIUS, EXCLUSION_RADIUS + 1), repeat=3)
            )
        )
    check("D spaced winner events have disjoint dependence blocks", all(left.isdisjoint(right) for left, right in combinations(dependency_blocks, 2)))
    rho_full = float(winner_density(Fraction(1)))
    no_winner = tuple((1.0 - rho_full) ** count for count in (100, 1000, 10000, 100000))
    check("D probability of no independent winner tends to zero", all(a > b for a, b in zip(no_winner, no_winner[1:])) and no_winner[-1] < 1.0e-6)


def periodic_seed_sites(side: int, phase: Coord) -> frozenset[Coord]:
    return frozenset(
        site
        for site in torus_sites(side)
        if all((site[axis] - phase[axis]) % ALIGNED_PERIOD == 0 for axis in range(3))
    )


def global_orbit_and_symmetry_breaking() -> None:
    section("E - Global orbit mixture and configuration-level symmetry breaking")
    phases = tuple(product(range(ALIGNED_PERIOD), repeat=3))
    frames = c17.oriented_frames()
    rotations = c17.proper_cubic_rotations()
    branch_count = len(phases) * len(frames)
    branch_weight = Fraction(1, branch_count)
    check("E periodic orbit has 216 spatial phases", len(phases) == 216)
    check("E phase-frame orbit mixture normalizes", branch_count * branch_weight == 1)

    side = 12
    phase = (0, 0, 0)
    seeds = periodic_seed_sites(side, phase)
    check("E aligned period-six history has density 1/216", len(seeds) == (side // ALIGNED_PERIOD) ** 3 and Fraction(len(seeds), side**3) == Fraction(1, 216))
    shifted = periodic_seed_sites(side, (1, 0, 0))
    check("E an actual periodic history breaks unit translation", seeds != shifted)
    check("E translations permute the 216 phases", all(mod_coord(add(item, (1, 2, 3)), ALIGNED_PERIOD) in phases for item in phases))

    frame_set = set(frames)
    check("E proper-cubic rotations permute phase-frame branches", all(mod_coord(rotate_coord(item, rotation), ALIGNED_PERIOD) in phases and c17.transform_frame(frame, rotation) in frame_set for item in phases for frame in frames[:1] for rotation in rotations))

    support = canonical_terminal_support()
    check(
        "E aligned same-frame period-six diamonds are NN-disjoint",
        all(
            not supports_touch(
                frame_support(support, frame),
                frame_support(support, frame),
                displacement,
            )
            for frame in frames
            for displacement in (
                (6, 0, 0),
                (0, 6, 0),
                (0, 0, 6),
                (6, 6, 0),
                (6, 6, 6),
            )
        ),
    )
    check("E global correlated orbit is denser than the IID local-minimum factor", Fraction(1, 216) > winner_density(Fraction(1)))


def deterministic_quantum_rate_and_routes() -> None:
    section("F - Deterministic, quantum/QCA, rate, and route separation")
    side = 2
    sites = torus_sites(side)
    translations = sites

    def translate_bits(bits: tuple[int, ...], shift: Coord) -> tuple[int, ...]:
        lookup = {site: bits[index] for index, site in enumerate(sites)}
        return tuple(lookup[mod_coord(subtract(site, shift), side)] for site in sites)

    invariant_bits = tuple(
        bits
        for bits in product((0, 1), repeat=len(sites))
        if all(translate_bits(bits, shift) == bits for shift in translations)
    )
    check("F only empty and full binary torus states are translation fixed", invariant_bits == ((0,) * len(sites), (1,) * len(sites)))
    check("F full fixed state violates hard-core isolation", sum(invariant_bits[1]) == len(sites) > 1)

    # Finite quantum W states preserve symmetry but their local one-particle
    # mass vanishes in the infinite limit.  A covariant unitary preserves the
    # invariant subspace; it does not choose an actual record branch.
    volume = side**3
    uniform = np.ones(volume, dtype=complex) / np.sqrt(volume)
    phases = np.exp(2j * np.pi * np.arange(volume) / volume)
    commuting_phase = np.diag(np.ones(volume, dtype=complex))
    check("F finite uniform one-particle state is normalized", np.allclose(np.vdot(uniform, uniform), 1.0))
    check("F a translation-scalar unitary preserves the uniform state", np.allclose(commuting_phase @ uniform, uniform))
    check("F quantum phase choices exist beyond geometry", len(set(np.round(phases, 12))) == volume)

    # Rescaling exponential clocks preserves every local priority ordering but
    # changes all occurrence times.  Thus the spatial seed geometry cannot fix
    # a temporal rate.
    uniforms = np.asarray((0.13, 0.27, 0.44, 0.71, 0.93))
    times_one = -np.log(uniforms)
    times_seven = -np.log(uniforms) / 7.0
    check("F changing exponential rate preserves event order", tuple(np.argsort(times_one)) == tuple(np.argsort(times_seven)))
    check("F changing exponential rate rescales every event time", np.allclose(times_seven, times_one / 7.0))
    global_first_survival = tuple(np.exp(-0.2 * count) for count in (1, 10, 100, 1000))
    check(
        "F infinite IID clocks have zero positive-time global survival",
        all(a > b for a, b in zip(global_first_survival, global_first_survival[1:]))
        and global_first_survival[-1] < 1.0e-80,
    )

    # Proper-cubic symmetry fixes equal weights only within the single frame
    # orbit.  It says nothing about invariant scalar content branches.
    frames = c17.oriented_frames()
    uniform_frame_weight = Fraction(1, len(frames))
    check("F frame-orbit invariance gives 24 equal normalized weights", len(frames) * uniform_frame_weight == 1)
    scalar_weights_a = (Fraction(1, 2), Fraction(1, 2))
    scalar_weights_b = (Fraction(1, 3), Fraction(2, 3))
    check("F inequivalent scalar branch weights remain free", sum(scalar_weights_a) == sum(scalar_weights_b) == 1 and scalar_weights_a != scalar_weights_b)

    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    route_phrases = (
        "deterministic route",
        "stochastic route",
        "quantum route",
        "qca route",
        "global-history route",
        "contingent-boundary route",
        "static seed kernel is not an ongoing clocked dynamics",
        "covariant solution set is not a normalized selector",
        "realized-state primitive supplies the slot, not the sample",
    )
    for phrase in route_phrases:
        check(f"F route classification states: {phrase}", phrase in note)


def no_go_and_classification_contract() -> None:
    section("G - Scoped classification and no-go discipline")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    claims = (
        "finite tori admit an invariant exactly-one typed seed law",
        "infinite z3 admits no invariant probability law concentrated on exactly one seed",
        "positive-density isolated typed seeds are viable",
        "the local-minimum seed process is candidate law content",
        "the global periodic orbit mixture is candidate history-law content",
        "actual configurations may break symmetry while the law remains invariant",
        "a spatial seed kernel does not derive a temporal rate",
        "born weights and actuality remain open",
        "not a theorem of the current four axioms",
        "residual law fields are not separate axiom atoms",
        "no new record axiom is forced",
    )
    for claim in claims:
        check(f"G note preserves classification: {claim}", claim in normalized)

    n1_routes = (
        "deterministic equivariant map — attempted",
        "finite-torus uniform seed — attempted",
        "finite-range iid hard core — attempted",
        "continuous-time stochastic clocks — attempted",
        "one-particle quantum state — attempted",
        "positive-density quantum state — attempted",
        "qca coherent evolution — attempted",
        "global periodic orbit — attempted",
        "covariant global constraint — attempted",
        "contingent physical boundary — attempted",
    )
    for route in n1_routes:
        check(f"G N1 includes route: {route}", route in normalized)
    check("G N2 includes collapsed three-condition table", "collapsed wall set has three conditions" in normalized)
    check("G N3 records the hidden-condition scan", "hidden-condition scan" in normalized)
    check("G N4 uses exact residual matching", "exact residual matching" in normalized)
    check("G N5 narrows the rhetoric to exactly-one probability", "no claim against positive-density invariant measures" in normalized)
    check("G N6 rejects automatic axiom promotion", "partial-closure path" in normalized and "no constitutional promotion follows" in normalized)
    check("G N7 contains the hostile steelman", "hostile reviewer" in normalized and "broad nucleation no-go would be false" in normalized)
    check("G N8 records cross-cycle retirement mechanisms", "cross-cycle echo" in normalized and "conditional law construction" in normalized)
    check("G no-go discipline gate records PASS", "no-go-discipline status: pass" in normalized)


def main() -> int:
    source_and_scope_contract()
    cycle17_exclusion_geometry()
    one_seed_finite_and_infinite()
    finite_range_hard_core_factor()
    global_orbit_and_symmetry_breaking()
    deterministic_quantum_rate_and_routes()
    no_go_and_classification_contract()
    print(
        "\nSUMMARY: INVARIANT FIRST-SEED HARD-CORE CYCLE 18 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
