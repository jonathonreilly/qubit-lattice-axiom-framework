#!/usr/bin/env python3
"""Exact checks for formation-order covariance and isotropic binary order-blindness.

A sequential single-site formation order on Z^3 cannot be invariant under a
non-identity proper cubic rotation. On the isotropic binary alphabet, the only
interior nearest-neighbor rules whose formation law is independent of order are
the independent (constant) rules, which do not vary with neighbour conditions.
A declared Ising-type varying rule is a witness: distinct orders give distinct
exact joints. No physical order or rule is selected.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/FORMATION_ORDER_COVARIANCE_AND_ISOTROPIC_BINARY_ORDER_BLIND_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
REALIZED_PATH = ROOT / AUDIT_INPUT_PATHS[2]

Vector = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Vector) -> Vector:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return tuple(result)  # type: ignore[return-value]


def identity_rotation() -> Rotation:
    return ((0, 1, 2), (1, 1, 1))


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def ising_plus(m: int, k: int) -> Fraction:
    """P(+ | m recorded neighbours, k of them +) for e^J = 2."""
    weight_plus = 2 ** (2 * k)
    weight_minus = 2 ** (2 * (m - k))
    return Fraction(weight_plus, weight_plus + weight_minus)


def constant_plus(_m: int, _k: int, value: Fraction = Fraction(1, 2)) -> Fraction:
    return value


def site_factor(
    plus_prob,
    value: int,
    recorded_values: list[int],
) -> Fraction:
    recorded = len(recorded_values)
    pluses = sum(recorded_values)
    p_plus = plus_prob(recorded, pluses)
    return p_plus if value == 1 else (1 - p_plus)


def undirected_edges(pairs: tuple[tuple[int, int], ...]) -> set[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for left, right in pairs:
        edges.add((left, right))
        edges.add((right, left))
    return edges


def formation_probability(
    order: tuple[int, ...],
    config: tuple[int, ...],
    edges: set[tuple[int, int]],
    plus_prob,
) -> Fraction:
    probability = Fraction(1)
    formed: list[int] = []
    for site in order:
        recorded = [config[neighbour] for neighbour in formed if (site, neighbour) in edges]
        probability *= site_factor(plus_prob, config[site], recorded)
        formed.append(site)
    return probability


def joint_vector(order: tuple[int, ...], n_sites: int, edges: set[tuple[int, int]], plus_prob):
    return tuple(
        formation_probability(order, config, edges, plus_prob)
        for config in product((0, 1), repeat=n_sites)
    )


def total_variation(left, right) -> Fraction:
    return sum(abs(a - b) for a, b in zip(left, right, strict=True)) / 2


def differing_cells(left, right) -> int:
    return sum(a != b for a, b in zip(left, right, strict=True))


def exchange_holds(plus_prob, max_recorded: int = 2) -> list[tuple]:
    failures = []
    for m_x in range(max_recorded):
        for m_y in range(max_recorded):
            for k_x in range(m_x + 1):
                for k_y in range(m_y + 1):
                    for a in (0, 1):
                        for b in (0, 1):
                            def chance(value: int, recorded: int, pluses: int) -> Fraction:
                                p_plus = plus_prob(recorded, pluses)
                                return p_plus if value == 1 else (1 - p_plus)

                            left = chance(a, m_x, k_x) * chance(b, m_y + 1, k_y + a)
                            right = chance(b, m_y, k_y) * chance(a, m_x + 1, k_x + b)
                            if left != right:
                                failures.append((m_x, k_x, m_y, k_y, a, b, left, right))
    return failures


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    realized = REALIZED_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    realized_flat = normalize(realized)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: current minimal_axioms Lattice/Admissibility/Record clauses and realized_state_primitive")
    print("declared_math: proper cubic rotations, finite sequential formation products, isotropic binary kernels")

    checks.check(
        "audit-input-paths",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
        "the note, axiom memo, and realized-state primitive are the declared source packet",
    )
    checks.check(
        "lattice-sites-clause",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site."
        in axiom_flat,
        "Lattice supplies Z^3, nearest-neighbor adjacency, and proper cubic rotations",
    )
    checks.check(
        "admissibility-covariance-clause",
        "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat,
        "Admissibility requires one covariant nearest-neighbor rule",
    )
    checks.check(
        "admissibility-distribution-clause",
        "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
        in axiom_flat,
        "Admissibility supplies a local distribution that varies with neighbour conditions",
    )
    record_section = axiom.split("### Record / Fixed Reality", 1)[1].split(
        "## Qualification", 1
    )[0]
    checks.check(
        "record-form-and-unreadability",
        "Records form." in record_section
        and "Only records are readable." in record_section
        and "A site with no record cannot be read." in normalize(record_section),
        "Record supplies formation, readability of records only, and unreadable absence",
    )
    checks.check(
        "admissibility-no-order-or-rate",
        "It does not" in axiom
        and "provide a record-production process" in axiom_flat,
        "Admissibility supplies no record-production process, order, or rate",
    )
    checks.check(
        "realized-state-no-average",
        "no averaging over alternatives" in realized_flat
        and "A value that would change under a different law-admissible realized state is registered data, not derivation output."
        in realized_flat,
        "the realized-state primitive supplies no measure over alternative orders",
    )
    checks.check(
        "note-contract",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "no proper-cubic-invariant total order" in note_flat
        and "only independent rules" in note_flat
        and "positive pair-of-orders witness" in note_flat,
        "the note states the bounded classification and witness target",
    )
    checks.check(
        "note-dependency",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)" in note
        and "physical formation order is not selected" in note_flat,
        "scientific authorities are the axiom memo and the realized-state primitive; no order is selected",
    )

    checks.check(
        "proper-cubic-group",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
        "the determinant-positive signed-permutation group has 24 elements",
    )
    checks.check(
        "identity-in-group",
        identity_rotation() in ROTATIONS,
        "the identity is a proper cubic rotation",
    )

    moved_by_every_nonidentity = True
    orbit_cycle_lengths: list[int] = []
    for rotation in ROTATIONS:
        if rotation == identity_rotation():
            continue
        moved = None
        for seed in (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0),
            (1, 1, 1),
        ):
            if rotate_vector(rotation, seed) != seed:
                moved = seed
                break
        if moved is None:
            moved_by_every_nonidentity = False
            break
        orbit = [moved]
        image = rotate_vector(rotation, moved)
        while image != moved:
            orbit.append(image)
            image = rotate_vector(rotation, image)
            if len(orbit) > 8:
                break
        orbit_cycle_lengths.append(len(orbit))
        if len(orbit) < 2:
            moved_by_every_nonidentity = False
    checks.check(
        "lemma-C-no-invariant-total-order",
        moved_by_every_nonidentity
        and all(length >= 2 for length in orbit_cycle_lengths)
        and len(orbit_cycle_lengths) == 23,
        "every non-identity proper cubic rotation moves a lattice point, so an invariant total order would require x < Rx < ... < x",
    )

    ninety = None
    for rotation in ROTATIONS:
        image = rotate_vector(rotation, (1, 0, 0))
        if image == (0, 1, 0) and rotate_vector(rotation, (0, 1, 0)) == (-1, 0, 0):
            ninety = rotation
            break
    checks.check(
        "ninety-degree-about-z",
        ninety is not None and rotate_vector(ninety, (0, 0, 1)) == (0, 0, 1),
        "a order-4 rotation about the z axis exists in the proper cubic group",
    )

    # Path3 graph 0-1-2.
    path_edges = undirected_edges(((0, 1), (1, 2)))
    chain_order = (0, 1, 2)
    ends_first = (0, 2, 1)
    chain_ising = joint_vector(chain_order, 3, path_edges, ising_plus)
    ends_ising = joint_vector(ends_first, 3, path_edges, ising_plus)
    chain_const = joint_vector(chain_order, 3, path_edges, constant_plus)
    ends_const = joint_vector(ends_first, 3, path_edges, constant_plus)
    checks.check(
        "path3-masses",
        sum(chain_ising) == 1 and sum(ends_ising) == 1 and sum(chain_const) == 1,
        "every executed formation law is a probability law",
    )
    path_laws: dict[tuple[Fraction, ...], list[tuple[int, ...]]] = {}
    for order in permutations((0, 1, 2)):
        path_laws.setdefault(joint_vector(order, 3, path_edges, ising_plus), []).append(order)
    checks.check(
        "path3-ising-two-laws",
        len(path_laws) == 2,
        "the six orders on the three-site path collapse to two Ising formation laws",
    )
    path_tv = total_variation(chain_ising, ends_ising)
    path_diffs = differing_cells(chain_ising, ends_ising)
    checks.check(
        "path3-ising-witness",
        path_diffs == 8 and path_tv == Fraction(9, 50)
        and chain_ising[0] == Fraction(8, 25)
        and ends_ising[0] == Fraction(4, 17),
        "chain versus ends-first differs on all eight configurations, TV 9/50, all-minus 8/25 versus 4/17",
    )
    checks.check(
        "path3-constant-order-blind",
        chain_const == ends_const and len({joint_vector(order, 3, path_edges, constant_plus) for order in permutations((0, 1, 2))}) == 1,
        "the constant rule gives one formation law on every path3 order",
    )

    # Algebraic constancy: (pminus - pplus)^2 identity.
    plus_one = ising_plus(1, 1)
    minus_one = ising_plus(1, 0)
    p0_from_plus_side = plus_one ** 2 + (1 - plus_one) * minus_one
    left_minus_side = (1 - minus_one) ** 2 + minus_one * (1 - plus_one)
    one_minus_p0 = 1 - p0_from_plus_side
    checks.check(
        "constancy-polynomial-on-ising",
        left_minus_side - one_minus_p0 == (minus_one - plus_one) ** 2
        and (minus_one - plus_one) != 0
        and p0_from_plus_side != ising_plus(0, 0),
        "the path3 matching identity's residual is (pminus-pplus)^2 and is nonzero for the Ising kernel",
    )

    def residual_of_free(pplus: Fraction, pminus: Fraction) -> Fraction:
        p0 = pplus ** 2 + (1 - pplus) * pminus
        left = (1 - pminus) ** 2 + pminus * (1 - pplus)
        return left - (1 - p0)

    samples = (
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(4, 5), Fraction(1, 5)),
        (Fraction(2, 3), Fraction(1, 4)),
        (Fraction(1, 7), Fraction(5, 8)),
        (Fraction(3, 10), Fraction(3, 10)),
    )
    polynomial_ok = all(
        residual_of_free(pplus, pminus) == (pminus - pplus) ** 2
        for pplus, pminus in samples
    )
    checks.check(
        "constancy-polynomial-identity",
        polynomial_ok,
        "for every sampled one-neighbour kernel, the path3 residual equals (pminus-pplus)^2 exactly",
    )
    checks.check(
        "interior-constancy",
        residual_of_free(Fraction(1, 2), Fraction(1, 2)) == 0
        and all(
            residual_of_free(pplus, pminus) == 0
            for pplus, pminus in samples
            if pplus == pminus
        )
        and all(
            residual_of_free(pplus, pminus) != 0
            for pplus, pminus in samples
            if pplus != pminus
        ),
        "the residual vanishes if and only if the one-neighbour kernel is independent of the neighbour value",
    )

    # L-shaped path (perpendicular two-edge window) repeats the same graph identity.
    ell_edges = undirected_edges(((0, 1), (1, 2)))
    checks.check(
        "ell-shape-same-graph",
        joint_vector((0, 1, 2), 3, ell_edges, ising_plus) == chain_ising
        and joint_vector((0, 2, 1), 3, ell_edges, ising_plus) == ends_ising,
        "the perpendicular L-window is the same path graph and carries the same two Ising laws",
    )

    const_exchange = exchange_holds(constant_plus, max_recorded=5)
    ising_exchange = exchange_holds(ising_plus, max_recorded=2)
    checks.check(
        "exchange-constant",
        const_exchange == [],
        "the constant kernel satisfies the adjacent-pair exchange identity through five recorded neighbours",
    )
    checks.check(
        "exchange-ising-fails",
        len(ising_exchange) == 24,
        "the Ising kernel fails twenty-four exchange identities already at recorded-neighbour cardinalities 0 and 1",
    )

    # Adjacent transposition on path3: swapping 0 and 1 in (0,1,2) gives (1,0,2),
    # which is not a neighbour-pair in the formation sequence? 0 and 1 ARE neighbours.
    # (0,1,2) vs (1,0,2) should match iff exchange on that pair with empty background.
    # Those two orders are both forest orders and share the chain law.
    swap_01 = joint_vector((1, 0, 2), 3, path_edges, ising_plus)
    checks.check(
        "non-two-neighbour-swap-ising",
        swap_01 == chain_ising,
        "swapping the first two sites of the chain keeps every recorded set of size at most one, so the Ising law is unchanged",
    )
    # Non-neighbour consecutive pair: in (0,2,1), sites 0 and 2 are consecutive in the
    # order and are not adjacent on the path. Swapping them yields (2,0,1), same class.
    swap_nonadj = joint_vector((2, 0, 1), 3, path_edges, ising_plus)
    checks.check(
        "non-adjacent-consecutive-swap",
        swap_nonadj == ends_ising,
        "swapping two consecutive non-neighbours leaves the formation product unchanged",
    )

    # Cycle4 plaquette.
    cycle_edges = undirected_edges(((0, 1), (1, 2), (2, 3), (3, 0)))
    snake = (0, 1, 2, 3)
    opposite = (0, 2, 1, 3)
    rotated_snake = (1, 2, 3, 0)
    snake_ising = joint_vector(snake, 4, cycle_edges, ising_plus)
    opposite_ising = joint_vector(opposite, 4, cycle_edges, ising_plus)
    rotated_ising = joint_vector(rotated_snake, 4, cycle_edges, ising_plus)
    cycle_laws: dict[tuple[Fraction, ...], list[tuple[int, ...]]] = {}
    for order in permutations((0, 1, 2, 3)):
        cycle_laws.setdefault(joint_vector(order, 4, cycle_edges, ising_plus), []).append(order)
    checks.check(
        "cycle4-ising-four-laws",
        len(cycle_laws) == 4 and sorted(len(group) for group in cycle_laws.values()) == [4, 4, 8, 8],
        "the twenty-four plaquette orders collapse to four Ising formation laws of sizes 4, 4, 8, 8",
    )
    checks.check(
        "cycle4-snake-versus-opposite",
        differing_cells(snake_ising, opposite_ising) == 16
        and total_variation(snake_ising, opposite_ising) == Fraction(9, 50)
        and sum(snake_ising) == 1,
        "cyclic order versus opposite-corners differs on all sixteen configurations, TV 9/50",
    )
    checks.check(
        "cycle4-constant-one-law",
        len({joint_vector(order, 4, cycle_edges, constant_plus) for order in permutations((0, 1, 2, 3))}) == 1,
        "the constant rule is order-blind on the plaquette",
    )

    # C2: rotating the configuration is the same as rotating the order.
    def rotate_cycle_config(config: tuple[int, ...]) -> tuple[int, ...]:
        return (config[3], config[0], config[1], config[2])

    c2_mismatches = 0
    for config in product((0, 1), repeat=4):
        direct = formation_probability(snake, config, cycle_edges, ising_plus)
        pushed = formation_probability(rotated_snake, rotate_cycle_config(config), cycle_edges, ising_plus)
        if direct != pushed:
            c2_mismatches += 1
    checks.check(
        "lemma-C2-pushforward",
        c2_mismatches == 0 and snake_ising != rotated_ising,
        "the Ising formation law of a rotated order is the pushforward of the original law, and a 90-degree cyclic shift of the snake order is a different law",
    )

    # 2x3 rectangle.
    grid = [(row, column) for row in range(2) for column in range(3)]
    index = {site: n for n, site in enumerate(grid)}
    grid_edges: set[tuple[int, int]] = set()
    for site in grid:
        for step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbour = (site[0] + step[0], site[1] + step[1])
            if neighbour in index:
                grid_edges.add((index[site], index[neighbour]))
    row_major = (0, 1, 2, 3, 4, 5)
    reverse = (5, 4, 3, 2, 1, 0)
    corners = (
        index[(0, 0)],
        index[(0, 2)],
        index[(1, 0)],
        index[(1, 2)],
        index[(0, 1)],
        index[(1, 1)],
    )
    row_ising = joint_vector(row_major, 6, grid_edges, ising_plus)
    reverse_ising = joint_vector(reverse, 6, grid_edges, ising_plus)
    corner_ising = joint_vector(corners, 6, grid_edges, ising_plus)
    grid_laws: dict[tuple[Fraction, ...], int] = {}
    for order in permutations(range(6)):
        vec = joint_vector(order, 6, grid_edges, ising_plus)
        grid_laws[vec] = grid_laws.get(vec, 0) + 1
    checks.check(
        "rectangle-2x3-ising-twenty-eight-laws",
        len(grid_laws) == 28 and sum(grid_laws.values()) == 720,
        "the 720 orders on the 2x3 window give twenty-eight distinct Ising formation laws",
    )
    checks.check(
        "rectangle-opposite-corners-coincide",
        row_ising == reverse_ising,
        "row-major and its reverse, a pair of opposite-corner monotone classes, give the same Ising law",
    )
    checks.check(
        "rectangle-corners-versus-row",
        differing_cells(row_ising, corner_ising) == 44
        and total_variation(row_ising, corner_ising) == Fraction(135, 578)
        and sum(row_ising) == 1,
        "corners-first versus row-major differs on 44 of 64 configurations, TV 135/578",
    )
    checks.check(
        "rectangle-constant-one-law",
        len({joint_vector(order, 6, grid_edges, constant_plus) for order in permutations(range(6))}) == 1,
        "the constant rule is order-blind on the 2x3 window",
    )

    checks.check(
        "ising-varies-with-neighbours",
        ising_plus(0, 0) == Fraction(1, 2)
        and ising_plus(1, 1) == Fraction(4, 5)
        and ising_plus(1, 0) == Fraction(1, 5)
        and ising_plus(1, 1) != ising_plus(1, 0),
        "the declared Ising kernel varies with the recorded-neighbour values",
    )
    checks.check(
        "constant-does-not-vary",
        constant_plus(0, 0) == constant_plus(1, 1) == constant_plus(2, 1) == Fraction(1, 2),
        "the independent kernel is insensitive to nearest-neighbour conditions",
    )
    checks.check(
        "note-quotes-witness-numbers",
        "8/25" in note
        and "4/17" in note
        and "9/50" in note
        and "135/578" in note
        and "twenty-eight" in note_flat
        and "44 of 64" in note_flat,
        "the note quotes the exact path3, plaquette, and 2x3 witness numbers",
    )
    checks.check(
        "note-no-order-selected",
        "selects neither order" in note_flat
        and "selects neither rule" in note_flat,
        "the note selects neither a physical order nor a physical rule",
    )
    checks.check(
        "note-separating-clauses-not-adopted",
        "not adopted" in note_flat
        and "owner decision" in note_flat,
        "separating clauses are recorded as owner decisions and not adopted",
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
