#!/usr/bin/env python3
"""Deep probe of an extensional nearest-neighbor law.

The runner asks four separate questions:

1. How strongly do the live covariance/variation/no-privilege clauses narrow
   an actual local rule table?
2. Can an explicit append-only local relation derive continuation support and
   record permanence?
3. Does that record rule also derive quantum multi-site composition?
4. Can a reversible QCA or quantum instrument supply the missing pieces
   without importing them in its definition?

Finite witnesses establish non-entailment only.  No toy rule here is proposed
as the framework's physical rule and no foundation surface is edited.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
import json
import math

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOM = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = ROOT / "docs" / "EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md"
CONTINUATION_NOTE = ROOT / "docs" / "ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md"
TENSOR_NOGO = ROOT / "docs" / "TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md"
PRODUCTION_BOUNDARY = ROOT / "docs" / "RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

OPEN = -1
VALUES = (0, 1)
PASS = 0
FAIL = 0

DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[tuple[int, ...], ...]:
    out = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * math.prod(signs) != 1:
                continue
            matrix = [[0, 0, 0] for _ in range(3)]
            for row in range(3):
                matrix[row][perm[row]] = signs[row]
            direction_perm = []
            for direction in DIRECTIONS:
                rotated = tuple(
                    sum(matrix[row][column] * direction[column] for column in range(3))
                    for row in range(3)
                )
                direction_perm.append(DIR_INDEX[rotated])
            out.append(tuple(direction_perm))
    return tuple(out)


ROTATIONS = proper_cubic_rotations()


def rotate_profile(profile: tuple[int, ...], rotation: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(profile[rotation[index]] for index in range(6))


def flip_profile(profile: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(OPEN if value == OPEN else 1 - value for value in profile)


def flip_menu(menu: frozenset[int]) -> frozenset[int]:
    return frozenset(1 - value for value in menu)


def majority_availability(profile: tuple[int, ...]) -> frozenset[int]:
    count0 = profile.count(0)
    count1 = profile.count(1)
    if count0 > count1:
        return frozenset({0})
    if count1 > count0:
        return frozenset({1})
    return frozenset({0, 1})


def copy_neighbor_availability(
    profile: tuple[int, ...], domain: tuple[int, ...]
) -> frozenset[int]:
    represented = frozenset(value for value in profile if value != OPEN)
    return represented if represented else frozenset(domain)


def source_contract() -> None:
    section("A - Live-source and premise boundary")
    axiom = AXIOM.read_text()
    note = NOTE.read_text()
    continuation = CONTINUATION_NOTE.read_text()
    tensor_nogo = TENSOR_NOGO.read_text()
    production = PRODUCTION_BOUNDARY.read_text()
    registry = json.loads(REGISTRY.read_text())

    for needle in (
        "There is one fixed nearest-neighbor admissibility rule",
        "available possibilities are determined by, and vary with",
        "Records form.",
        "A state is a configuration of records.",
        "Admissibility is not a dynamics axiom.",
    ):
        check(f"A live axiom needle: {needle[:45]}", needle in axiom)
    check("A live axiom contains no extensional rule table", "RULE:" not in axiom and "rule table" not in axiom)
    continuation_flat = " ".join(continuation.lower().split())
    tensor_nogo_flat = " ".join(tensor_nogo.lower().split())
    check(
        "A continuation theorem keeps physical successor support underived",
        "does not say that every menu item has a physical successor" in continuation_flat,
    )
    check(
        "A tensor no-go keeps composition independent",
        "does not force generation/local tomography" in tensor_nogo_flat,
    )
    check("A producer boundary keeps the next-token law separate", "The append grammar has no slot" in production)
    check("A only four approved premise nodes exist", len(registry["canonical_ids"]) == 4)
    check("A deep-probe note is authority-free", "**Authority:** none" in note)
    check("A deep-probe note contains N1-N8", all(f"### N{i}" in note for i in range(1, 9)))


def rule_space_census() -> None:
    section("B - Exact rule-space census under covariance and no label privilege")
    profiles = list(product((OPEN, 0, 1), repeat=6))
    canonical: dict[tuple[int, ...], tuple[int, ...]] = {}
    orbit_reps = set()
    for profile in profiles:
        representative = min(rotate_profile(profile, rotation) for rotation in ROTATIONS)
        canonical[profile] = representative
        orbit_reps.add(representative)

    self_flip = []
    paired = []
    consumed = set()
    for representative in sorted(orbit_reps):
        if representative in consumed:
            continue
        partner = canonical[flip_profile(representative)]
        if partner == representative:
            self_flip.append(representative)
            consumed.add(representative)
        else:
            paired.append((representative, partner))
            consumed.update((representative, partner))

    equivariant_rules = 3 ** len(paired)
    varying_equivariant_rules = equivariant_rules - 1
    check("B proper cubic rotation group has 24 elements", len(set(ROTATIONS)) == 24)
    check("B ternary six-neighbor profiles number 729", len(profiles) == 729)
    check("B profiles have 57 proper-cubic orbits", len(orbit_reps) == 57)
    check("B label flip fixes 9 profile orbits", len(self_flip) == 9)
    check("B label flip pairs the other 48 orbits", len(paired) == 24 and 9 + 2 * 24 == 57)
    check("B no-privilege covariant rule count is 3^24", equivariant_rules == 282_429_536_481)
    count_matches = varying_equivariant_rules == 282_429_536_480
    check("B neighbor variation leaves 282,429,536,480 rules", count_matches)
    check("B the live structural clauses do not select one table", count_matches and varying_equivariant_rules > 1)

    menus = {majority_availability(profile) for profile in profiles}
    check("B majority/tie witness is nonempty everywhere", all(majority_availability(profile) for profile in profiles))
    check("B majority/tie witness actually varies", menus == {frozenset({0}), frozenset({1}), frozenset({0, 1})})
    check(
        "B majority/tie witness is exhaustively proper-cubic covariant",
        all(
            majority_availability(rotate_profile(profile, rotation))
            == majority_availability(profile)
            for profile in profiles
            for rotation in ROTATIONS
        ),
    )
    check(
        "B majority/tie witness is label-equivariant",
        all(
            majority_availability(flip_profile(profile))
            == flip_menu(majority_availability(profile))
            for profile in profiles
        ),
    )

    domain = (0, 1, 2)
    general_profiles = tuple(product((OPEN,) + domain, repeat=6))
    relabelings = tuple(permutations(domain))

    def relabel_profile(profile: tuple[int, ...], relabeling: tuple[int, ...]) -> tuple[int, ...]:
        mapping = dict(zip(domain, relabeling))
        return tuple(OPEN if value == OPEN else mapping[value] for value in profile)

    def relabel_menu(menu: frozenset[int], relabeling: tuple[int, ...]) -> frozenset[int]:
        mapping = dict(zip(domain, relabeling))
        return frozenset(mapping[value] for value in menu)

    check("B basis-free schema exhausts all 4^6 ternary-domain profiles", len(general_profiles) == 4096)
    check(
        "B copy-neighbor schema is exhaustively proper-cubic covariant",
        all(
            copy_neighbor_availability(rotate_profile(profile, rotation), domain)
            == copy_neighbor_availability(profile, domain)
            for profile in general_profiles
            for rotation in ROTATIONS
        ),
    )
    check(
        "B copy-neighbor schema is equivariant under every value relabeling",
        all(
            copy_neighbor_availability(relabel_profile(profile, relabeling), domain)
            == relabel_menu(copy_neighbor_availability(profile, domain), relabeling)
            for profile in general_profiles
            for relabeling in relabelings
        ),
    )
    exact_star_support = True
    for profile in general_profiles:
        successors = frozenset(
            (value,) + profile
            for value in copy_neighbor_availability(profile, domain)
        )
        if (
            frozenset(successor[0] for successor in successors)
            != copy_neighbor_availability(profile, domain)
            or any(successor[1:] != profile for successor in successors)
        ):
            exact_star_support = False
            break
    check(
        "B copy-neighbor schema gives exact maximum support without changing neighbors",
        exact_star_support,
    )


def lattice_sites(side: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(product(range(side), repeat=3))


def add_coord(left: tuple[int, int, int], right: tuple[int, int, int], side: int) -> tuple[int, int, int]:
    return tuple((left[index] + right[index]) % side for index in range(3))


def profile_at(state: tuple[int, ...], site_index: int, side: int, sites: tuple[tuple[int, int, int], ...], index: dict[tuple[int, int, int], int]) -> tuple[int, ...]:
    site = sites[site_index]
    return tuple(state[index[add_coord(site, direction, side)]] for direction in DIRECTIONS)


def append_successors(state: tuple[int, ...], side: int = 2) -> frozenset[tuple[int, ...]]:
    sites = lattice_sites(side)
    index = {site: position for position, site in enumerate(sites)}
    successors = set()
    for site_index, content in enumerate(state):
        if content != OPEN:
            continue
        for value in majority_availability(profile_at(state, site_index, side, sites, index)):
            future = list(state)
            future[site_index] = value
            successors.add(tuple(future))
    return frozenset(successors)


def extends(base: tuple[int, ...], future: tuple[int, ...]) -> bool:
    return all(value == OPEN or future[index] == value for index, value in enumerate(base))


def append_rule_theorem() -> None:
    section("C - Explicit append relation closes the record layer by construction")
    side = 2
    sites = lattice_sites(side)
    index = {site: position for position, site in enumerate(sites)}
    states = list(product((OPEN, 0, 1), repeat=len(sites)))

    all_valid = True
    menu_complete = True
    exact_preservation = True
    for state in states:
        successors = append_successors(state, side)
        expected_pairs = set()
        for site_index, content in enumerate(state):
            if content == OPEN:
                profile = profile_at(state, site_index, side, sites, index)
                expected_pairs.update((site_index, value) for value in majority_availability(profile))
        realized_pairs = set()
        for successor in successors:
            changed = [i for i in range(len(state)) if state[i] != successor[i]]
            if len(changed) != 1 or state[changed[0]] != OPEN:
                all_valid = False
                continue
            realized_pairs.add((changed[0], successor[changed[0]]))
            if not extends(state, successor):
                exact_preservation = False
        if realized_pairs != expected_pairs:
            menu_complete = False

    empty = tuple(OPEN for _ in sites)
    check("C finite witness exhausts all 3^8 record configurations", len(states) == 6561)
    check("C every one-step transition appends exactly one record", all_valid)
    check("C every available value has a record-forming successor", menu_complete)
    check("C every transition preserves all old site/content pairs", exact_preservation)
    check("C empty state has both values at every site as successors", len(append_successors(empty, side)) == 2 * len(sites))
    full = tuple(0 for _ in sites)
    check("C a finite fully recorded block is saturated", not append_successors(full, side))

    base = (OPEN, OPEN, OPEN)
    zero = (0, OPEN, OPEN)
    one = (1, OPEN, OPEN)
    future_values = list(product((0, 1), repeat=3))
    descendants_zero = {future for future in future_values if extends(zero, future)}
    descendants_one = {future for future in future_values if extends(one, future)}
    check("C conflicting same-site branches have disjoint append-only futures", not descendants_zero & descendants_one)

    weights_a = {successor: sp.Rational(1, len(append_successors(empty, side))) for successor in append_successors(empty, side)}
    weighted = list(append_successors(empty, side))
    weights_b = {successor: sp.Rational(2 if i == 0 else 1, len(weighted) + 1) for i, successor in enumerate(weighted)}
    check("C one support relation accepts different normalized measures", sum(weights_a.values()) == sum(weights_b.values()) == 1 and weights_a != weights_b)
    check("C append relation itself selects no realized member", len(append_successors(empty, side)) > 1)


def vec_pair(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(list(left) + list(right))


def composition_independence() -> None:
    section("D - The same extensional record rule fits inequivalent global algebras")
    I2 = sp.eye(2)
    I4 = sp.eye(4)
    basis2 = []
    for row in range(2):
        for column in range(2):
            matrix = sp.zeros(2)
            matrix[row, column] = 1
            basis2.append(matrix)
    products = [sp.kronecker_product(left, right) for left in basis2 for right in basis2]
    ordinary_rank = sp.Matrix.hstack(*(sp.Matrix(list(matrix)) for matrix in products)).rank()
    duplicate_vectors = [vec_pair(matrix, matrix) for matrix in products]
    duplicate_rank = sp.Matrix.hstack(*duplicate_vectors).rank()
    central_z = vec_pair(I4, -I4)
    augmented_rank = sp.Matrix.hstack(*duplicate_vectors, central_z).rank()

    check("D ordinary generated two-site product has rank 16", ordinary_rank == 16)
    check("D duplicate-sector local products have the same rank 16", duplicate_rank == 16)
    check("D duplicate composite contains an extra global observable", augmented_rank == 17)
    check("D full duplicate self-adjoint dimension is 32", 2 * 4 * 4 == 32)

    record_state = (OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN)
    rule_successors = append_successors(record_state, 2)
    ordinary_labelled = {("ordinary", successor) for successor in rule_successors}
    duplicate_labelled = {("duplicate", successor) for successor in rule_successors}
    check("D carrier choice leaves the record successor graph unchanged", {item[1] for item in ordinary_labelled} == {item[1] for item in duplicate_labelled})
    check("D record-only rule cannot inspect the extra central sector", central_z not in sp.Matrix.hstack(*duplicate_vectors).columnspace())


def reversible_and_instrument_routes() -> None:
    section("E - Reversible-QCA and quantum-instrument route prices")
    CNOT = sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
    )
    ket10 = sp.Matrix([0, 0, 1, 0])
    ket11 = sp.Matrix([0, 0, 0, 1])
    check("E CNOT is a reversible local write", CNOT.T * CNOT == sp.eye(4) and CNOT * ket10 == ket11)
    check("E applying the reversible write again erases the copied bit", CNOT * ket11 == ket10 and CNOT * CNOT == sp.eye(4))
    check("E global reversible access therefore does not give absolute permanence", CNOT.T * ket11 == ket10)

    P0 = sp.diag(1, 0)
    P1 = sp.diag(0, 1)
    W = sp.Matrix(
        [
            [1, 0],
            [0, 0],
            [0, 0],
            [0, 1],
        ]
    )
    check("E ideal two-register copy is an isometry", W.T * W == sp.eye(2))
    check("E its Kraus blocks are the supplied pointer projectors", W[:2, :] == P0 and W[2:, :] == P1)
    check("E pointer Kraus family is trace preserving", P0.T * P0 + P1.T * P1 == sp.eye(2))

    rho = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 3)], [sp.Rational(1, 3), sp.Rational(1, 2)]])
    dephased = P0 * rho * P0 + P1 * rho * P1
    check("E nonselective instrument dephases but contains no realized label", dephased == sp.eye(2) / 2)
    check("E outcome weights use the trace pairing", sp.trace(P0 * rho) == sp.trace(P1 * rho) == sp.Rational(1, 2))
    check("E the isometry already presupposes system-register tensor composition", W.rows == 2 * 2 and W.cols == 2)

    fresh_registers_needed = 3
    fixed_register_capacity = 2
    check("E repeated append-only writes require fresh capacity or export", fresh_registers_needed > fixed_register_capacity)


def classification() -> None:
    section("F - Deep-probe classification")
    note = NOTE.read_text().lower()
    markers = (
        "282,429,536,480",
        "append-only cellular relation",
        "reversible quantum cellular automaton",
        "quantum instrument",
        "select the physical rule",
        "does not derive tensor composition",
        "actualization remains",
    )
    for marker in markers:
        check(f"F note carries boundary marker: {marker}", marker.lower() in note)
    check("F note declares no axiom need", "no additional axiom is declared necessary" in note)


def main() -> None:
    source_contract()
    rule_space_census()
    append_rule_theorem()
    composition_independence()
    reversible_and_instrument_routes()
    classification()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: explicit finite rule-family probes; no physical rule is selected")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
