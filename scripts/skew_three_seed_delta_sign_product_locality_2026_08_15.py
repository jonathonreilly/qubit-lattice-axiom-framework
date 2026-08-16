#!/usr/bin/env python3
"""Exact checks for claim-delta sign-product NN-determination.

The paired note is
docs/SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md.

Stars are scored at unread v=(-1,1,1) only. The product is displayed, not
adopted. No cache or axiom surface is written.
"""

from __future__ import annotations

import ast
from itertools import combinations_with_replacement, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SKEW_THREE_SEED_DELTA_SIGN_PRODUCT_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

Point = tuple[int, int, int]
V: Point = (-1, 1, 1)
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
NEIGHBORS: tuple[Point, ...] = tuple(
    (V[0] + shift[0], V[1] + shift[1], V[2] + shift[2]) for shift in SHIFTS
)
U0_CENTERS: tuple[Point, ...] = ((0, 0, 0), (2, 0, 0), (1, 2, 1))
U1_CENTERS: tuple[Point, ...] = ((0, 0, 0), (1, 2, 1), (1, 2, 2))
BOX: tuple[Point, ...] = tuple(product(range(-2, 3), repeat=3))


def normalize(text: str) -> str:
    return " ".join(text.split())


def taxicab(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def ball(center: Point, radius: int = 2) -> frozenset[Point]:
    sites: set[Point] = set()
    for dx, dy, dz in product(range(-radius, radius + 1), repeat=3):
        if abs(dx) + abs(dy) + abs(dz) <= radius:
            sites.add((center[0] + dx, center[1] + dy, center[2] + dz))
    return frozenset(sites)


def union_of(centers: tuple[Point, ...]) -> frozenset[Point]:
    occupied: set[Point] = set()
    for center in centers:
        occupied |= ball(center)
    return frozenset(occupied)


def occupancy(sites: frozenset[Point]) -> tuple[int, ...]:
    return tuple(1 if neighbor in sites else 0 for neighbor in NEIGHBORS)


def sign_product(delta: Point) -> int:
    value = 1
    for coord in delta:
        if coord > 0:
            value *= 1
        elif coord < 0:
            value *= -1
    return value


def nearest_site(query: Point, sites: frozenset[Point]) -> Point:
    best: Point | None = None
    best_distance: int | None = None
    for site in sites:
        distance = taxicab(query, site)
        if (
            best is None
            or best_distance is None
            or distance < best_distance
            or (distance == best_distance and site < best)
        ):
            best = site
            best_distance = distance
    if best is None:
        raise ValueError("nearest site is undefined on the empty set")
    return best


def claim_delta_tuple(sites: frozenset[Point]) -> tuple[int, ...]:
    values: list[int] = []
    for neighbor in NEIGHBORS:
        seed = nearest_site(neighbor, sites)
        delta = (neighbor[0] - seed[0], neighbor[1] - seed[1], neighbor[2] - seed[2])
        values.append(sign_product(delta))
    return tuple(values)


def nearest_in_ball(query: Point, center: Point) -> tuple[int, tuple[Point, ...]]:
    best_distance: int | None = None
    found: list[Point] = []
    for site in ball(center):
        distance = taxicab(query, site)
        if best_distance is None or distance < best_distance:
            best_distance = distance
            found = [site]
        elif distance == best_distance:
            found.append(site)
    if best_distance is None:
        raise ValueError("empty ball")
    return best_distance, tuple(found)


def merged_sign_product(centers: tuple[Point, ...], neighbor_index: int) -> int:
    neighbor = NEIGHBORS[neighbor_index]
    best_distance: int | None = None
    found: list[Point] = []
    for center in centers:
        distance, sites = nearest_in_ball(neighbor, center)
        if best_distance is None or distance < best_distance:
            best_distance = distance
            found = list(sites)
        elif distance == best_distance:
            found.extend(sites)
    seed = min(found)
    delta = (neighbor[0] - seed[0], neighbor[1] - seed[1], neighbor[2] - seed[2])
    return sign_product(delta)


def audit_input_paths_literal(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS" for target in node.targets):
            continue
        if not isinstance(node.value, ast.Tuple):
            return None
        values: list[str] = []
        for element in node.value.elts:
            if not isinstance(element, ast.Constant) or not isinstance(element.value, str):
                return None
            values.append(element.value)
        return tuple(values)
    return None


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = (ROOT / NOTE_REL).read_text(encoding="utf-8")
    axiom = (ROOT / AXIOM_REL).read_text(encoding="utf-8")
    runner_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("Skew three-seed claim-delta sign-product locality")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scope: stars at unread v=(-1,1,1) only; displayed, not adopted")

    literal_paths = audit_input_paths_literal(runner_source)
    checks.check(
        "audit-input-paths-static-literals",
        literal_paths == AUDIT_INPUT_PATHS == DECLARED_INPUT_PATHS,
    )
    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    distribution_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-distribution-sentence-current",
        distribution_sentence in normalized_axiom,
    )
    checks.check(
        "source-unread-site-sentence-current",
        "A site with no record cannot be read." in normalized_axiom,
    )
    checks.check(
        "note-quotes-admissibility-nn-law",
        distribution_sentence in normalized_note,
    )

    u0 = union_of(U0_CENTERS)
    u1 = union_of(U1_CENTERS)
    sigma0 = occupancy(u0)
    sigma1 = occupancy(u1)
    c0 = claim_delta_tuple(u0)
    c1 = claim_delta_tuple(u1)
    star0 = nearest_site(NEIGHBORS[1], u0)
    star1 = nearest_site(NEIGHBORS[4], u1)

    checks.check("theorem1-v-unread-on-u0", V not in u0)
    checks.check(
        "theorem1-sigma-u0",
        sigma0 == (1, 0, 1, 1, 0, 1),
        str(sigma0),
    )
    checks.check(
        "theorem1-c-u0",
        c0 == (1, 1, 1, 1, 1, 1),
        str(c0),
    )
    checks.check(
        "theorem1-sstar-not-always-neighbor",
        star0 == (-2, 0, 0) and star0 not in set(NEIGHBORS),
        str(star0),
    )
    checks.check("theorem1-u0-has-three-centers", len(U0_CENTERS) == 3)
    checks.check("theorem1-empty-product-is-plus-one", sign_product((0, 0, 0)) == 1)

    checks.check("theorem2-u1-distinct", u1 != u0)
    checks.check("theorem2-v-unread-on-u1", V not in u1)
    checks.check("theorem2-same-sigma", sigma1 == sigma0)
    checks.check("theorem2-c-disagrees", c1 != c0 and c1 == (1, 1, 1, 1, -1, 1), str(c1))
    checks.check(
        "theorem2-centers-in-box",
        all(center in BOX for center in U1_CENTERS) and len(U1_CENTERS) == 3,
    )
    checks.check(
        "theorem2-disagreement-from-distant-seed",
        star1 == (-1, 2, 2) and star1 not in set(NEIGHBORS),
        str(star1),
    )

    occupancy_by_center = {center: occupancy(ball(center)) for center in BOX}
    disagreement_count = 0
    same_sigma_count = 0
    for centers in combinations_with_replacement(BOX, 3):
        bits = [0] * 6
        for center in centers:
            for index, occupied in enumerate(occupancy_by_center[center]):
                if occupied:
                    bits[index] = 1
        if tuple(bits) != sigma0:
            continue
        same_sigma_count += 1
        candidate = tuple(merged_sign_product(centers, index) for index in range(6))
        if candidate != c0 and union_of(centers) != u0:
            disagreement_count += 1
            if disagreement_count >= 1 and same_sigma_count >= 8:
                # Existence is the theorem; keep the census short.
                pass
    checks.check(
        "theorem2-box-census-finds-disagreement",
        disagreement_count >= 1,
        f"same_sigma>={same_sigma_count} disagreements>={disagreement_count}",
    )
    checks.check(
        "product-not-nn-determined",
        sigma0 == sigma1 and c0 != c1,
    )

    claim_scope = (
        "On stars at unread v=(-1,1,1), whether the claim-delta sign-product "
        "6-tuple is a function of the 6-NN occupancy alone is reported. "
        "Displayed, not adopted."
    )
    checks.check("note-claim-scope", claim_scope in note)
    checks.check(
        "theorem3-displayed-not-adopted",
        "Displayed, not adopted" in note and "displayed, not adopted" in note.lower(),
    )
    checks.check(
        "theorem3-not-written-into-admissibility",
        "Do not write the product into Admissibility" in note
        and "The product is not inserted into Admissibility" in note,
    )
    checks.check(
        "theorem3-l1-not-attached",
        "Do not attach L1" in note and "L1 is not attached" in note,
    )
    checks.check(
        "no-fourth-ball",
        "No fourth ball" in note
        and "fourth ball" in normalized_note
        and len(U0_CENTERS) == 3
        and len(U1_CENTERS) == 3,
    )
    checks.check(
        "stars-scored-at-v-only",
        "Stars are scored at `v` only" in note
        and "On stars at unread v=(-1,1,1)" in note,
    )
    checks.check(
        "not-leftover-char-or-skeweq",
        "not a leftover-character membership claim for the product" in normalized_note
        and "not an equivariance claim for a different map" in normalized_note,
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-phrases-absent",
        all(phrase not in note for phrase in forbidden),
        ",".join(phrase for phrase in forbidden if phrase in note),
    )
    checks.check(
        "hypothetical-axiom-no-edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "note-reports-computed-tuples",
        "σ(U0) = (1, 0, 1, 1, 0, 1)" in note
        and "c(U0) = (1, 1, 1, 1, 1, 1)" in note
        and "c(U1) = (1, 1, 1, 1, -1, 1)" in note,
    )
    checks.check(
        "axiom-file-unedited-marker",
        "### Admissibility / Local Constraint" in axiom
        and "claim-delta" not in axiom
        and "U0" not in axiom,
    )

    print("per_element: six neighbors of unread v and their lex-first nearest sites")
    print("per_site: stars scored at v only")
    print("per_mode: checked and not executed")
    print("per_block: three-seed unions U0 and U1; no fourth ball")
    print("lattice_wide: checked and not executed — product displayed, not adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
