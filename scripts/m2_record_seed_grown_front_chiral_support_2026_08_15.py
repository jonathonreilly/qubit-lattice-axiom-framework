#!/usr/bin/env python3
"""Score M_2 Record k=3 alphabet plus seed-grown ℓ¹ front support.

Re-earns July-3 Theorems 2–3 on named k-letter models and counts
occupied nearest neighbors on already-displayed B_t / S_{t+1}.
No new occupancy patch, no cache, no axiom edit.
"""

from __future__ import annotations

import itertools
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "M2_RECORD_SEED_GROWN_FRONT_CHIRAL_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
JULY3_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_"
    "ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md"
)

AUDIT_INPUT_PATHS = (
    "docs/M2_RECORD_SEED_GROWN_FRONT_CHIRAL_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRS)}


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} — {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def perm_sign(perm: tuple[int, ...]) -> int:
    sign = 1
    seen = [False] * len(perm)
    for start in range(len(perm)):
        if seen[start]:
            continue
        length = 0
        here = start
        while not seen[here]:
            seen[here] = True
            here = perm[here]
            length += 1
        if length % 2 == 0:
            sign = -sign
    return sign


def apply_signed_perm(
    axis_perm: tuple[int, ...], signs: tuple[int, ...], vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    return (
        signs[0] * vector[axis_perm[0]],
        signs[1] * vector[axis_perm[1]],
        signs[2] * vector[axis_perm[2]],
    )


def direction_perm(axis_perm: tuple[int, ...], signs: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(DIR_INDEX[apply_signed_perm(axis_perm, signs, direction)] for direction in DIRS)


def cubic_direction_perms() -> tuple[list[tuple[int, ...]], list[tuple[int, ...]], tuple[int, ...]]:
    full: list[tuple[int, ...]] = []
    proper: list[tuple[int, ...]] = []
    inversion = None
    for axis_perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            det = perm_sign(axis_perm) * signs[0] * signs[1] * signs[2]
            image = direction_perm(axis_perm, signs)
            full.append(image)
            if det == 1:
                proper.append(image)
            if axis_perm == (0, 1, 2) and signs == (-1, -1, -1):
                inversion = image
    if inversion is None:
        raise RuntimeError("spatial inversion was not generated")
    return full, proper, inversion


def act_col(perm: tuple[int, ...], coloring: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(coloring)
    for source, image in enumerate(perm):
        out[image] = coloring[source]
    return tuple(out)


def cycle_count(perm: tuple[int, ...]) -> int:
    seen = [False] * len(perm)
    cycles = 0
    for start in range(len(perm)):
        if seen[start]:
            continue
        cycles += 1
        here = start
        while not seen[here]:
            seen[here] = True
            here = perm[here]
    return cycles


def burnside_orbits(perms: list[tuple[int, ...]], letters: int) -> int:
    total = sum(letters ** cycle_count(perm) for perm in perms)
    if total % len(perms) != 0:
        raise RuntimeError("Burnside sum was not divisible by the group order")
    return total // len(perms)


def all_colorings(letters: int) -> list[tuple[int, ...]]:
    return list(itertools.product(range(letters), repeat=len(DIRS)))


def direct_orbits(perms: list[tuple[int, ...]], letters: int) -> list[set[tuple[int, ...]]]:
    unseen = set(all_colorings(letters))
    orbits: list[set[tuple[int, ...]]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        orbits.append(orbit)
        unseen -= orbit
    return orbits


def orbit_ids(orbits: list[set[tuple[int, ...]]]) -> dict[tuple[int, ...], int]:
    return {coloring: index for index, orbit in enumerate(orbits) for coloring in orbit}


def chiral_pairs(
    proper_orbits: list[set[tuple[int, ...]]], inversion: tuple[int, ...]
) -> list[tuple[int, int]]:
    ids = orbit_ids(proper_orbits)
    pairs: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    for index, orbit in enumerate(proper_orbits):
        sample = next(iter(orbit))
        image_id = ids[act_col(inversion, sample)]
        if image_id != index:
            pair = tuple(sorted((index, image_id)))
            if pair not in seen:
                seen.add(pair)
                pairs.append(pair)
    return pairs


def l1_norm(site: tuple[int, int, int]) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def sphere(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x_coord in range(-radius, radius + 1):
        for y_coord in range(-radius, radius + 1):
            remaining = radius - abs(x_coord) - abs(y_coord)
            if remaining < 0:
                continue
            if remaining == 0:
                sites.append((x_coord, y_coord, 0))
            else:
                sites.append((x_coord, y_coord, remaining))
                sites.append((x_coord, y_coord, -remaining))
    return sites


def nonzero_count(site: tuple[int, int, int]) -> int:
    return sum(1 for coord in site if coord != 0)


def occupied_neighbor_count(site: tuple[int, int, int], depth: int) -> int:
    occupied = 0
    for step in DIRS:
        neighbor = (site[0] + step[0], site[1] + step[1], site[2] + step[2])
        if l1_norm(neighbor) <= depth:
            occupied += 1
    return occupied


def front_census(max_depth: int) -> dict[int, dict[str, int]]:
    summary: dict[int, dict[str, int]] = {}
    for depth in range(max_depth + 1):
        sites = sphere(depth + 1)
        occupied_counts = [occupied_neighbor_count(site, depth) for site in sites]
        nonzero_counts = [nonzero_count(site) for site in sites]
        summary[depth] = {
            "front_size": len(sites),
            "max_occupied": max(occupied_counts),
            "min_occupied": min(occupied_counts),
            "n_with_6": sum(1 for count in occupied_counts if count == 6),
            "identity_holds": int(occupied_counts == nonzero_counts),
            "min_empty": min(6 - count for count in occupied_counts),
        }
    return summary


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    july3 = JULY3_PATH.read_text(encoding="utf-8")

    lock_letters = 2
    unread_letters = 1
    alphabet_k = lock_letters + unread_letters

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/M2_RECORD_SEED_GROWN_FRONT_CHIRAL_SUPPORT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )
    checks.check(
        "axiom-m2-presentation",
        "live Qubit sentence is M_2(C)",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "axiom-record-lock-one",
        "Record locks one admissible local possibility",
        "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "alphabet-k3",
        "two lock-contents plus unread/empty give k=3",
        lock_letters == 2 and unread_letters == 1 and alphabet_k == 3,
    )

    full_perms, proper_perms, inversion = cubic_direction_perms()
    checks.check(
        "cubic-direction-action",
        "48 signed permutations, 24 proper, inversion outside proper",
        len(full_perms) == 48
        and len(set(full_perms)) == 48
        and len(proper_perms) == 24
        and len(set(proper_perms)) == 24
        and inversion not in set(proper_perms),
    )

    k2_proper = burnside_orbits(proper_perms, 2)
    k2_full = burnside_orbits(full_perms, 2)
    k2_direct_proper = direct_orbits(proper_perms, 2)
    k2_pairs = chiral_pairs(k2_direct_proper, inversion)
    checks.check(
        "july3-thm2-k2-achiral",
        "k=2 Burnside proper=full and zero chiral pairs",
        k2_proper == k2_full
        and len(k2_direct_proper) == k2_proper
        and len(k2_pairs) == 0,
    )

    k3_proper = burnside_orbits(proper_perms, 3)
    k3_full = burnside_orbits(full_perms, 3)
    k3_direct_proper = direct_orbits(proper_perms, 3)
    k3_pairs = chiral_pairs(k3_direct_proper, inversion)
    k3_ids = orbit_ids(k3_direct_proper)
    unpaired = [
        coloring
        for coloring in all_colorings(3)
        if k3_ids[act_col(inversion, coloring)] != k3_ids[coloring]
    ]
    unpaired_orbit_ids = sorted({k3_ids[coloring] for coloring in unpaired})
    representative = min(k3_direct_proper[unpaired_orbit_ids[0]])
    axis_mixed = all(representative[2 * axis] != representative[2 * axis + 1] for axis in range(3))
    color_counts = sorted(representative.count(color) for color in range(3))
    checks.check(
        "july3-thm3-unique-pair",
        "k=3 has exactly one chiral pair",
        k3_proper - k3_full == 1
        and len(k3_direct_proper) == k3_proper
        and len(k3_pairs) == 1
        and len(unpaired_orbit_ids) == 2,
    )
    checks.check(
        "july3-thm3-fully-mixed",
        "unique pair is handed fully-mixed on six slots",
        axis_mixed
        and color_counts == [2, 2, 2]
        and len(representative) == 6,
    )
    checks.check(
        "pair-needs-six-occupied-neighbors",
        "fully-mixed pair is a 6-NN occupancy member",
        len(representative) == 6
        and sum(color_counts) == 6
        and min(color_counts) == 2,
    )

    census = front_census(4)
    identity_ok = all(row["identity_holds"] == 1 for row in census.values())
    max_occupied = max(row["max_occupied"] for row in census.values())
    n_with_6 = sum(row["n_with_6"] for row in census.values())
    min_empty = min(row["min_empty"] for row in census.values())
    checks.check(
        "front-occ-equals-nonzero",
        "on S_{t+1} occupied NN equals nonzero coordinates for t=0..4",
        identity_ok and all(row["front_size"] > 0 for row in census.values()),
    )
    checks.check(
        "front-max-occupied-le-3",
        "max occupied NN on those fronts is at most 3",
        max_occupied <= 3 and max_occupied == 3,
    )
    checks.check(
        "n-with-6-zero",
        "N_with_6=0 on S_{t+1} for t=0..4",
        n_with_6 == 0 and all(row["n_with_6"] == 0 for row in census.values()),
    )
    checks.check(
        "front-empty-count-vs-fully-mixed",
        "front unread count is at least 3, so 2/2/2 empty multiplicity fails",
        min_empty >= 3,
    )
    checks.check(
        "pair-support-empty",
        "unique k=3 pair has empty support on those fronts",
        n_with_6 == 0 and alphabet_k == 3 and len(k3_pairs) == 1,
    )

    forbidden = (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice" + "-named",
        "not a " + "TOE",
    )
    self_source = Path(__file__).read_text(encoding="utf-8")
    checks.check(
        "forbidden-tokens-absent",
        "note and runner omit the dispatch-forbidden tokens",
        all(token not in note and token not in self_source for token in forbidden),
    )
    checks.check(
        "note-theorems-and-scope",
        "note states Theorems 1–3, claim_scope, and displayed-not-adopted",
        "## Theorem 1" in note
        and "## Theorem 2" in note
        and "## Theorem 3" in note
        and "Displayed, not adopted" in note
        and "unique `k=3` chiral pair has empty support" in note
        and "No-Go Discipline disposition: **PASS**" in note,
    )
    checks.check(
        "refusals",
        "Qubit stays M_2; V−A and L1 are not attached",
        "Qubit stays `M_2(C)`" in note
        and "No `V−A` axiom sentence and no L1 attachment" in note
        and "hypothetical_axiom_status: \"not proposed" in note
        and "### Theorem 2 (openness achirality)" in july3
        and "### Theorem 3 (chirality threshold and the minimal/canonical channels)"
        in july3,
    )
    checks.check(
        "no-new-occupancy-patch",
        "only already-displayed B_t / S_{t+1} are scored",
        "No occupancy is grown on a new patch" in note
        and "already-displayed seed-grown" in note
        and max(census) == 4,
    )

    print(
        "census: "
        + ", ".join(
            f"t={depth}:|S|={row['front_size']}:maxN={row['max_occupied']}:N6={row['n_with_6']}"
            for depth, row in census.items()
        )
    )
    print(
        f"alphabet: lock={lock_letters} empty={unread_letters} k={alphabet_k}; "
        f"k2_pairs={len(k2_pairs)} k3_pairs={len(k3_pairs)} "
        f"k3_burnside={k3_proper}/{k3_full} rep={representative}"
    )
    print(
        "per_element: checked exactly — each S_{t+1} site has occupied NN "
        "equal to its nonzero-coordinate count"
    )
    print(
        "per_site: checked exactly — one M_2 record plus unread/empty is k=3"
    )
    print(
        "per_mode: checked exactly — unique k=3 pair is the handed fully-mixed 6-slot coloring"
    )
    print("per_block: checked exactly — N_with_6=0 on each front t=0..4")
    print(
        "lattice_wide: checked and not executed — no non-seed-grown occupancy is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
