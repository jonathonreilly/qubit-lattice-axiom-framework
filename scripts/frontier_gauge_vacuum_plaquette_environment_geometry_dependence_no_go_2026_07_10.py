#!/usr/bin/env python3
"""Exact finite-geometry obstruction for a universal Wilson environment rho.

Local SU(3) Haar invariance forces triality neutrality at every integrated
link. The first strong-coupling contribution to a fundamental boundary
coefficient therefore requires an active plaquette chain filling the marked
boundary. This runner certifies minimum filling weights 3 at L_s=2 PBC and 5
at L_s=3 PBC, without a fitted rho, witness, or observed plaquette value.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
Site = tuple[int, int, int]
Link = tuple[Site, int]
Plaquette = tuple[Site, int, int]


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{status}] {name}")
    if detail:
        print(f"       {detail}")


@dataclass(frozen=True)
class Geometry:
    size: int
    links: tuple[Link, ...]
    plaquettes: tuple[Plaquette, ...]
    incidence: np.ndarray
    marked_index: int


def add_direction(site: Site, direction: int, size: int) -> Site:
    out = list(site)
    out[direction] = (out[direction] + 1) % size
    return tuple(out)  # type: ignore[return-value]


def plaquette_boundary(plaquette: Plaquette, size: int) -> tuple[tuple[Link, int], ...]:
    site, first, second = plaquette
    return (
        ((site, first), +1),
        ((add_direction(site, first, size), second), +1),
        ((add_direction(site, second, size), first), -1),
        ((site, second), -1),
    )


def build_geometry(size: int) -> Geometry:
    sites = tuple(product(range(size), repeat=3))
    links = tuple((site, direction) for site in sites for direction in range(3))
    plaquettes = tuple(
        (site, first, second)
        for site in sites
        for first in range(3)
        for second in range(first + 1, 3)
    )
    link_index = {link: index for index, link in enumerate(links)}
    incidence = np.zeros((len(links), len(plaquettes)), dtype=np.int8)
    for column, plaquette in enumerate(plaquettes):
        for link, orientation in plaquette_boundary(plaquette, size):
            incidence[link_index[link], column] += orientation
    marked: Plaquette = ((0, 0, 0), 0, 1)
    return Geometry(size, links, plaquettes, incidence, plaquettes.index(marked))


def syndrome(vector: np.ndarray) -> bytes:
    return np.mod(vector, 3).astype(np.uint8).tobytes()


def add_syndromes(left: bytes, right: bytes) -> bytes:
    a = np.frombuffer(left, dtype=np.uint8)
    b = np.frombuffer(right, dtype=np.uint8)
    return np.mod(a + b, 3).astype(np.uint8).tobytes()


def subtract_syndromes(left: bytes, right: bytes) -> bytes:
    a = np.frombuffer(left, dtype=np.uint8)
    b = np.frombuffer(right, dtype=np.uint8)
    return np.mod(a - b, 3).astype(np.uint8).tobytes()


def signed_active_columns(geometry: Geometry) -> list[tuple[int, bytes]]:
    out: list[tuple[int, bytes]] = []
    for column in range(len(geometry.plaquettes)):
        if column == geometry.marked_index:
            continue
        out.extend(
            (column, syndrome(sign * geometry.incidence[:, column]))
            for sign in (-1, +1)
        )
    return out


def no_filling_through_weight(geometry: Geometry, max_weight: int) -> bool:
    """Exact signed-support meet-in-the-middle search through weight four."""
    if max_weight > 4:
        raise ValueError("search is implemented only through weight four")
    target = syndrome(-geometry.incidence[:, geometry.marked_index])
    options = signed_active_columns(geometry)
    if max_weight >= 1 and any(column == target for _, column in options):
        return False

    pairs: dict[bytes, list[tuple[int, int]]] = defaultdict(list)
    for left_index, (left_plaq, left) in enumerate(options):
        for right_plaq, right in options[left_index + 1 :]:
            if left_plaq != right_plaq:
                pairs[add_syndromes(left, right)].append((left_plaq, right_plaq))
    if max_weight >= 2 and target in pairs:
        return False
    if max_weight >= 3:
        for plaquette, column in options:
            needed = subtract_syndromes(target, column)
            if any(plaquette not in pair for pair in pairs.get(needed, ())):
                return False
    if max_weight >= 4:
        for pair_sum, left_pairs in pairs.items():
            right_pairs = pairs.get(subtract_syndromes(target, pair_sum), ())
            for left in left_pairs:
                left_set = set(left)
                if any(left_set.isdisjoint(right) for right in right_pairs):
                    return False
    return True


def fillings_at_weight_three(geometry: Geometry) -> list[tuple[tuple[int, int], ...]]:
    """Enumerate all distinct-support signed triality fillings at weight three."""
    target = syndrome(-geometry.incidence[:, geometry.marked_index])
    options = signed_active_columns(geometry)
    out: list[tuple[tuple[int, int], ...]] = []
    for selected in combinations(options, 3):
        if len({column for column, _ in selected}) != 3:
            continue
        total = add_syndromes(add_syndromes(selected[0][1], selected[1][1]), selected[2][1])
        if total != target:
            continue
        signed: list[tuple[int, int]] = []
        for column, value in selected:
            positive = syndrome(geometry.incidence[:, column])
            signed.append((column, +1 if value == positive else -1))
        out.append(tuple(signed))
    return out


def filling_vector(geometry: Geometry, terms: tuple[tuple[Plaquette, int], ...]) -> np.ndarray:
    total = geometry.incidence[:, geometry.marked_index].astype(int)
    index = {plaquette: column for column, plaquette in enumerate(geometry.plaquettes)}
    for plaquette, sign in terms:
        total += sign * geometry.incidence[:, index[plaquette]]
    return total


def used_link_degrees(geometry: Geometry, terms: tuple[tuple[Plaquette, int], ...]) -> list[int]:
    counts = np.abs(geometry.incidence[:, geometry.marked_index]).astype(int)
    index = {plaquette: column for column, plaquette in enumerate(geometry.plaquettes)}
    for plaquette, _ in terms:
        counts += np.abs(geometry.incidence[:, index[plaquette]]).astype(int)
    return [int(value) for value in counts if value]


L2_FILLING: tuple[tuple[Plaquette, int], ...] = (
    (((0, 1, 0), 0, 1), +1),
    (((1, 0, 0), 0, 1), +1),
    (((1, 1, 0), 0, 1), +1),
)
L3_FILLING: tuple[tuple[Plaquette, int], ...] = (
    (((0, 0, 2), 0, 1), -1),
    (((0, 0, 2), 0, 2), +1),
    (((0, 0, 2), 1, 2), -1),
    (((0, 1, 2), 0, 2), -1),
    (((1, 0, 2), 1, 2), +1),
)


def main() -> int:
    print("=" * 78)
    print("WILSON RESIDUAL ENVIRONMENT: EXACT FINITE-GEOMETRY DEPENDENCE")
    print("=" * 78)
    g2, g3 = build_geometry(2), build_geometry(3)
    check(
        "standard periodic L_s=2 and L_s=3 Wilson spatial complexes are enumerated exactly",
        (len(g2.links), len(g2.plaquettes)) == (24, 24)
        and (len(g3.links), len(g3.plaquettes)) == (81, 81),
        "(links, plaquettes): L_s=2 -> (24,24), L_s=3 -> (81,81)",
    )
    check(
        "every plaquette boundary has two positive and two negative incidences",
        all(
            sorted(g.incidence[:, c][g.incidence[:, c] != 0]) == [-1, -1, 1, 1]
            for g in (g2, g3)
            for c in range(len(g.plaquettes))
        ),
    )
    check(
        "no L_s=2 signed active chain of weight <=2 fills the marked boundary modulo triality",
        no_filling_through_weight(g2, 2),
        "exact signed-support enumeration",
    )
    check(
        "no L_s=3 signed active chain of weight <=4 fills the marked boundary modulo triality",
        no_filling_through_weight(g3, 4),
        "exact meet-in-the-middle signed-support enumeration",
    )
    l2_weight_three = fillings_at_weight_three(g2)
    check(
        "the L_s=2 order-three triality filling is unique",
        len(l2_weight_three) == 1,
        "the unique monomial is the oriented complement of the marked plaquette in its periodic 2x2 plane",
    )
    r2, r3 = filling_vector(g2, L2_FILLING), filling_vector(g3, L3_FILLING)
    check(
        "an explicit three-plaquette L_s=2 sheet closes the marked boundary over the integers",
        np.array_equal(r2, np.zeros_like(r2)),
    )
    check(
        "an explicit five-plaquette L_s=3 cube cap closes the marked boundary over the integers",
        np.array_equal(r3, np.zeros_like(r3)),
    )
    check(
        "the L_s=2 attaining surface pairs every used link once in each orientation",
        set(used_link_degrees(g2, L2_FILLING)) == {2},
        "one-link Haar orthogonality gives a nonzero closed fundamental sheet",
    )
    check(
        "the L_s=3 attaining surface pairs every used link once in each orientation",
        set(used_link_degrees(g3, L3_FILLING)) == {2},
        "one-link Haar orthogonality gives a nonzero closed fundamental cube surface",
    )
    source_note = Path(
        "docs/GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_GEOMETRY_DEPENDENCE_NO_GO_NOTE_2026-07-10.md"
    ).read_text()
    parent_note = Path(
        "docs/GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_IDENTIFICATION_THEOREM_NOTE.md"
    ).read_text()
    check(
        "the source note forbids witness injection and observed plaquette input",
        "generic positive witness" in source_note
        and "observed plaquette" in source_note
        and "forbidden" in source_note.lower(),
    )
    check(
        "the parent note carries the geometry-indexed residual boundary",
        "rho_(p,q)^(env,L_s,BC)" in parent_note
        and "geometry-dependence" in parent_note.lower(),
    )
    print()
    print("Exact strong-coupling order certificate")
    print("  L_s=2 PBC fundamental environment coefficient: first allowed order = 3")
    print("  L_s=3 PBC fundamental environment coefficient: first allowed order = 5")
    print("  consequence: one geometry-free rho_(1,0)^env(beta) cannot represent both")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
