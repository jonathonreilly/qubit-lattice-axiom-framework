#!/usr/bin/env python3
"""Exact overlapping-edge instrument order and clock/rate nonselection checks."""

import itertools
from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def bits_of(index: int, sites: int) -> list[int]:
    return [(index >> (sites - 1 - site)) & 1 for site in range(sites)]


def index_of(bits: list[int]) -> int:
    value = 0
    for bit in bits:
        value = 2 * value + bit
    return value


def basis_state(sites: int, bit_string: str) -> sp.Matrix:
    vector = sp.zeros(2**sites, 1)
    vector[int(bit_string, 2), 0] = 1
    return vector


def projector(vector: sp.Matrix) -> sp.Matrix:
    return vector * vector.H


def swap_operator(sites: int, left: int, right: int) -> sp.Matrix:
    result = sp.zeros(2**sites)
    for source in range(2**sites):
        bits = bits_of(source, sites)
        bits[left], bits[right] = bits[right], bits[left]
        result[index_of(bits), source] = 1
    return result


def edge_projector(sites: int, left: int, right: int, outcome: tuple[int, int]) -> sp.Matrix:
    diagonal = []
    for index in range(2**sites):
        bits = bits_of(index, sites)
        diagonal.append(int((bits[left], bits[right]) == outcome))
    return sp.diag(*diagonal)


def edge_instrument(
    sites: int,
    left: int,
    right: int,
    empty_weight: sp.Expr,
    empty_operator: sp.Matrix | None = None,
) -> tuple[sp.Matrix, list[sp.Matrix]]:
    empty_operator = swap_operator(sites, left, right) if empty_operator is None else empty_operator
    empty = sp.sqrt(empty_weight) * empty_operator
    records = [
        sp.sqrt(1 - empty_weight) * edge_projector(sites, left, right, outcome)
        for outcome in ((0, 0), (0, 1), (1, 0), (1, 1))
    ]
    return empty, records


def channel(kraus: list[sp.Matrix], rho: sp.Matrix) -> sp.Matrix:
    return sp.simplify(sum((item * rho * item.H for item in kraus), sp.zeros(rho.rows)))


def channels_equal_on_matrix_units(left: list[sp.Matrix], right: list[sp.Matrix]) -> bool:
    """Check exact equality of two finite channels on a matrix-unit basis."""
    dimension = left[0].rows
    for row in range(dimension):
        for column in range(dimension):
            matrix_unit = sp.zeros(dimension)
            matrix_unit[row, column] = 1
            if channel(left, matrix_unit) != channel(right, matrix_unit):
                return False
    return True


def sequential_kraus(first: list[sp.Matrix], second: list[sp.Matrix]) -> list[sp.Matrix]:
    return [later * earlier for earlier in first for later in second]


def first_nonempty_stopping_kraus(
    first_empty: sp.Matrix,
    first_records: list[sp.Matrix],
    second_empty: sp.Matrix,
    second_records: list[sp.Matrix],
) -> tuple[list[sp.Matrix], list[list[sp.Matrix]]]:
    groups = [first_records, [item * first_empty for item in second_records], [second_empty * first_empty]]
    return [item for group in groups for item in group], groups


def diagonal_tuple(matrix: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(matrix[index, index]) for index in range(matrix.rows))


def cubic_matching(side: int, axis: int, parity: int) -> frozenset[tuple[tuple[int, ...], tuple[int, ...]]]:
    edges = set()
    for vertex in itertools.product(range(side), repeat=3):
        if vertex[axis] % 2 != parity:
            continue
        neighbor = list(vertex)
        neighbor[axis] = (neighbor[axis] + 1) % side
        edge = tuple(sorted((tuple(vertex), tuple(neighbor))))
        edges.add(edge)
    return frozenset(edges)


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(permutation[i] > permutation[j] for i in range(len(permutation)) for j in range(i + 1, len(permutation)))
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> list[tuple[tuple[int, ...], ...]]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = []
            for row in range(3):
                matrix.append(tuple(signs[row] if column == permutation[row] else 0 for column in range(3)))
            rotations.append(tuple(matrix))
    return rotations


def transform_vertex(vertex: tuple[int, ...], rotation: tuple[tuple[int, ...], ...], translation: tuple[int, ...], side: int) -> tuple[int, ...]:
    return tuple((sum(rotation[row][column] * vertex[column] for column in range(3)) + translation[row]) % side for row in range(3))


def transform_matching(matching: frozenset, rotation: tuple[tuple[int, ...], ...], translation: tuple[int, ...], side: int) -> frozenset:
    transformed = set()
    for left, right in matching:
        new_edge = tuple(sorted((transform_vertex(left, rotation, translation, side), transform_vertex(right, rotation, translation, side))))
        transformed.add(new_edge)
    return frozenset(transformed)


def local_and_order_checks() -> None:
    sites = 3
    dimension = 2**sites
    q = sp.Rational(1, 3)
    a_empty, a_records = edge_instrument(sites, 0, 1, q)
    b_empty, b_records = edge_instrument(sites, 1, 2, q)
    identity = sp.eye(dimension)

    for label, empty, records in (("A", a_empty, a_records), ("B", b_empty, b_records)):
        completeness = empty.H * empty + sum((item.H * item for item in records), sp.zeros(dimension))
        check(f"L01{label}", completeness == identity, f"edge {label} is a complete five-outcome CPTP instrument")
        check(f"L02{label}", sp.simplify(empty.H * empty) == q * identity, f"edge {label} no-record effect is q I")

    check("L03", (b_empty * a_empty - a_empty * b_empty).rank() == 4, "overlapping SWAP no-record branches have commutator rank four")

    rho = projector(basis_state(sites, "100"))
    a_full = a_records + [a_empty]
    b_full = b_records + [b_empty]
    layered_ab = sequential_kraus(a_full, b_full)
    layered_ba = sequential_kraus(b_full, a_full)
    check("O01", sum((item.H * item for item in layered_ab), sp.zeros(dimension)) == identity, "A-then-B layered schedule is CPTP")
    check("O02", sum((item.H * item for item in layered_ba), sp.zeros(dimension)) == identity, "B-then-A layered schedule is CPTP")
    out_ab = channel(layered_ab, rho)
    out_ba = channel(layered_ba, rho)
    check("O03", diagonal_tuple(out_ab) == (0, sp.Rational(1, 9), sp.Rational(2, 9), 0, sp.Rational(2, 3), 0, 0, 0), "A-then-B layered output has the exact witness diagonal")
    check("O04", diagonal_tuple(out_ba) == (0, 0, sp.Rational(1, 3), 0, sp.Rational(2, 3), 0, 0, 0), "B-then-A layered output has the exact witness diagonal")
    check("O05", out_ab != out_ba, "overlapping layered schedules define distinct channels")

    stopping_ab, groups_ab = first_nonempty_stopping_kraus(a_empty, a_records, b_empty, b_records)
    stopping_ba, groups_ba = first_nonempty_stopping_kraus(b_empty, b_records, a_empty, a_records)
    check("O06", len(stopping_ab) == 9 and len(stopping_ba) == 9, "each first-nonempty schedule has nine terminal Kraus operators")
    check("O07", sum((item.H * item for item in stopping_ab), sp.zeros(dimension)) == identity, "A-priority first-nonempty stopping instrument is CPTP")
    check("O08", sum((item.H * item for item in stopping_ba), sp.zeros(dimension)) == identity, "B-priority first-nonempty stopping instrument is CPTP")
    stopping_out_ab = channel(stopping_ab, rho)
    stopping_out_ba = channel(stopping_ba, rho)
    check("O09", diagonal_tuple(stopping_out_ab) == (0, sp.Rational(1, 9), sp.Rational(2, 9), 0, sp.Rational(2, 3), 0, 0, 0), "A-priority stopping output has the exact witness diagonal")
    check("O10", diagonal_tuple(stopping_out_ba) == (0, 0, sp.Rational(1, 9), 0, sp.Rational(8, 9), 0, 0, 0), "B-priority stopping output has the exact witness diagonal")
    check("O11", stopping_out_ab != stopping_out_ba, "first-nonempty priority changes the terminal channel")

    group_weights_ab = tuple(sp.simplify(sum(sp.trace(item * rho * item.H) for item in group)) for group in groups_ab)
    group_weights_ba = tuple(sp.simplify(sum(sp.trace(item * rho * item.H) for item in group)) for group in groups_ba)
    check("O12", group_weights_ab == (sp.Rational(2, 3), sp.Rational(2, 9), sp.Rational(1, 9)), "A-priority terminal stage weights normalize exactly")
    check("O13", group_weights_ba == (sp.Rational(2, 3), sp.Rational(2, 9), sp.Rational(1, 9)), "B-priority terminal stage weights normalize exactly")
    check("O14", b_empty * a_empty * basis_state(sites, "100") == sp.Rational(1, 3) * basis_state(sites, "001"), "A-then-B double-empty branch ends at |001>")
    check("O15", a_empty * b_empty * basis_state(sites, "100") == sp.Rational(1, 3) * basis_state(sites, "010"), "B-then-A double-empty branch ends at |010>")


def controls_and_clock_checks() -> None:
    q = sp.Rational(1, 3)
    sites4 = 4
    dimension4 = 2**sites4
    a_empty, a_records = edge_instrument(sites4, 0, 1, q)
    c_empty, c_records = edge_instrument(sites4, 2, 3, q)
    a_full = a_records + [a_empty]
    c_full = c_records + [c_empty]
    rho4 = projector((basis_state(sites4, "1000") + basis_state(sites4, "0110")) / sp.sqrt(2))
    disjoint_ac = sequential_kraus(a_full, c_full)
    disjoint_ca = sequential_kraus(c_full, a_full)
    check("K01", channel(disjoint_ac, rho4) == channel(disjoint_ca, rho4), "disjoint-edge layered schedules commute on an exact coherent control")
    check("K01U", channels_equal_on_matrix_units(disjoint_ac, disjoint_ca), "disjoint-edge layered schedules are equal as channels on the full matrix-unit basis")

    sites3 = 3
    dimension3 = 2**sites3
    identity3 = sp.eye(dimension3)
    ia_empty, ia_records = edge_instrument(sites3, 0, 1, q, sp.sqrt(1) * identity3)
    ib_empty, ib_records = edge_instrument(sites3, 1, 2, q, sp.sqrt(1) * identity3)
    rho3 = projector((basis_state(sites3, "100") + basis_state(sites3, "011")) / sp.sqrt(2))
    identity_ab = sequential_kraus(ia_records + [ia_empty], ib_records + [ib_empty])
    identity_ba = sequential_kraus(ib_records + [ib_empty], ia_records + [ia_empty])
    check("K02", channel(identity_ab, rho3) == channel(identity_ba, rho3), "identity no-record mutation removes the overlapping order ambiguity on the coherent fixture")
    check("K02U", channels_equal_on_matrix_units(identity_ab, identity_ba), "identity no-record overlapping schedules are equal as channels on the full matrix-unit basis")

    identity_stop_ab, _ = first_nonempty_stopping_kraus(ia_empty, ia_records, ib_empty, ib_records)
    identity_stop_ba, _ = first_nonempty_stopping_kraus(ib_empty, ib_records, ia_empty, ia_records)
    coherence_state = projector((basis_state(sites3, "000") + basis_state(sites3, "001")) / sp.sqrt(2))
    identity_stop_out_ab = channel(identity_stop_ab, coherence_state)
    identity_stop_out_ba = channel(identity_stop_ba, coherence_state)
    check("K03", identity_stop_out_ab[0, 1] == sp.Rational(7, 18) and identity_stop_out_ba[0, 1] == sp.Rational(1, 6), "first-event priority remains order-sensitive with identity no-record branches")
    diagonal_control = projector(basis_state(sites3, "100"))
    check("K04", channel(identity_stop_ab, diagonal_control) == channel(identity_stop_ba, diagonal_control), "a diagonal identity-control state can hide the priority difference")

    q_zero = sp.Integer(0)
    za_empty, za_records = edge_instrument(sites3, 0, 1, q_zero)
    zb_empty, zb_records = edge_instrument(sites3, 1, 2, q_zero)
    zero_ab = sequential_kraus(za_records + [za_empty], zb_records + [zb_empty])
    zero_ba = sequential_kraus(zb_records + [zb_empty], za_records + [za_empty])
    check("K05", channel(zero_ab, rho3) == channel(zero_ba, rho3), "pure computational projective edge instruments commute at q=0 on the coherent fixture")
    check("K05U", channels_equal_on_matrix_units(zero_ab, zero_ba), "q=0 computational projective edge schedules are equal as channels on the full matrix-unit basis")

    swap_a_empty, swap_a_records = edge_instrument(sites3, 0, 1, q)
    swap_b_empty, swap_b_records = edge_instrument(sites3, 1, 2, q)
    swap_ab = sequential_kraus(swap_a_records + [swap_a_empty], swap_b_records + [swap_b_empty])
    swap_ba = sequential_kraus(swap_b_records + [swap_b_empty], swap_a_records + [swap_a_empty])
    symmetrized = [item / sp.sqrt(2) for item in swap_ab + swap_ba]
    check("K06", sum((item.H * item for item in symmetrized), sp.zeros(dimension3)) == identity3, "the equal randomized/symmetrized schedule is another CPTP composition rule")
    sym_output = channel(symmetrized, diagonal_control)
    check("K07", sym_output == sp.simplify((channel(swap_ab, diagonal_control) + channel(swap_ba, diagonal_control)) / 2), "symmetrization is the exact channel average")
    check("K08", sym_output != channel(swap_ab, diagonal_control) and sym_output != channel(swap_ba, diagonal_control), "symmetrization resolves the raw order choice by adding new process content")

    corrupted = list(swap_a_records)
    corrupted[0] = sp.sqrt(2) * corrupted[0]
    check("K09", swap_a_empty.H * swap_a_empty + sum((item.H * item for item in corrupted), sp.zeros(dimension3)) != identity3, "a Kraus-weight mutation is rejected by edge-instrument normalization")

    clock_fast = (sp.Integer(0), sp.Integer(1), sp.Integer(2))
    clock_slow = (sp.Integer(0), sp.Integer(2), sp.Integer(4))
    check("T01", tuple(sorted(range(3), key=lambda i: clock_fast[i])) == tuple(sorted(range(3), key=lambda i: clock_slow[i])), "clock rescaling preserves the same event order")
    check("T02", sp.Rational(2, clock_fast[-1] - clock_fast[0]) == 1 and sp.Rational(2, clock_slow[-1] - clock_slow[0]) == sp.Rational(1, 2), "the same two-layer order has different rates under two clocks")
    lambda_fast = sp.log(3)
    lambda_slow = sp.log(3) / 2
    check("T03", sp.exp(-lambda_fast * 1) == q and sp.exp(-lambda_slow * 2) == q, "the same no-record probability fixes lambda times delta-t, not lambda")
    check("T04", lambda_fast != lambda_slow, "one per-attempt kernel admits distinct physical rates")


def cubic_matching_checks() -> None:
    side = 4
    matchings = [cubic_matching(side, axis, parity) for axis in range(3) for parity in range(2)]
    all_edges = set()
    for vertex in itertools.product(range(side), repeat=3):
        for axis in range(3):
            neighbor = list(vertex)
            neighbor[axis] = (neighbor[axis] + 1) % side
            all_edges.add(tuple(sorted((tuple(vertex), tuple(neighbor)))))
    check("C01", all(len(matching) == side**3 // 2 for matching in matchings), "each cubic layer contains the expected half-volume matching")
    check("C02", all(len({endpoint for edge in matching for endpoint in edge}) == 2 * len(matching) for matching in matchings), "every cubic layer is vertex-conflict-free")
    check("C03", set().union(*matchings) == all_edges and sum(len(item) for item in matchings) == len(all_edges), "the six matchings partition all nearest-neighbor edges")

    rotations = proper_cubic_rotations()
    identity_rotation = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    translations = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
    check("C04", len(rotations) == 24, "the exact proper-cubic rotation list has 24 elements")
    family = set(matchings)
    permuted = all(transform_matching(matching, rotation, translation, side) in family for matching in matchings for rotation in rotations for translation in translations)
    check("C05", permuted, "translations and proper cubic rotations permute the six-layer family")
    orbit = {
        transform_matching(matchings[0], rotation, translation, side)
        for rotation in rotations
        for translation in translations
    }
    check("C06", orbit == family, "one matching has the full six-layer symmetry orbit, so no layer is privileged")


def source_checks() -> None:
    path = Path("docs/OVERLAPPING_EDGE_INSTRUMENT_ORDER_AND_TIME_RATE_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md")
    check("S01", path.exists(), "source note exists")
    text = path.read_text() if path.exists() else ""
    markers = (
        "does not identify terminal labels as framework Records",
        "does not select a physical clock or rate",
        "does not classify all overlapping instruments",
        "does not establish that the axioms require amendment",
    )
    for index, marker in enumerate(markers, 2):
        check(f"S{index:02d}", marker in text, f"source contains boundary marker: {marker}")


def main() -> int:
    local_and_order_checks()
    controls_and_clock_checks()
    cubic_matching_checks()
    source_checks()
    print("BOUNDARY: the finite edge Kraus rule, overlapping-support schedules, first-nonempty stopping, and clock maps are explicit conditional inputs.")
    print("BOUNDARY: separate edge normalization and identical edge rules do not select overlap composition or order; event order does not select metric time or rate.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
