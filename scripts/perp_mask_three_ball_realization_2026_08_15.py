#!/usr/bin/env python3
"""Perp weight-4 mask realization on uneqrad 3-ball unions.

Among the 12 perpendicular weight-4 occupancy masks, count how many
appear as 6-NN occupancy of an unread site on a 3-ball union in the
uneqrad box: distinct centers in [-2,2]^3, radii in {1,2,3} not all
equal, unread v with ||v||_inf <= 4. Stop at the first realization
per mask. Also report the 2000-star prefix count. Displayed, not
adopted. No cache is written.
"""

from __future__ import annotations

import ast
import itertools
from array import array
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/PERP_MASK_THREE_BALL_REALIZATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/PERP_MASK_THREE_BALL_REALIZATION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Host = tuple[tuple[Point, Point, Point], tuple[int, int, int], Point]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
PREFIX = 2000
SHIFT = 5
STRIDE = 11
GRID = STRIDE * STRIDE * STRIDE
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "Among the 12 perpendicular weight-4 masks, how many '
    "are realized as unread 6-NN occupancy of a 3-ball union is reported. "
    'Displayed, not adopted."'
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def ball(center: Point, radius: int) -> tuple[Point, ...]:
    sites: list[Point] = []
    span = range(-radius, radius + 1)
    for offset in itertools.product(span, repeat=3):
        if abs(offset[0]) + abs(offset[1]) + abs(offset[2]) <= radius:
            sites.append(add(center, offset))
    return tuple(sites)


def enc(point: Point) -> int:
    return (point[0] + SHIFT) + STRIDE * (
        (point[1] + SHIFT) + STRIDE * (point[2] + SHIFT)
    )


def perp_masks() -> tuple[Coloring, ...]:
    records: list[Coloring] = []
    for mask in itertools.product((0, 1), repeat=len(DIRS)):
        if sum(mask) != 4:
            continue
        empty = [index for index, bit in enumerate(mask) if bit == 0]
        axes = {index // 2 for index in empty}
        if len(axes) == 2:
            records.append(mask)
    return tuple(records)


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f" | {detail}" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def realize() -> dict:
    masks = perp_masks()
    remaining = set(masks)
    hosts: dict[Coloring, Host] = {}
    seed_box = tuple(itertools.product(range(-2, 3), repeat=3))
    v_box = tuple(itertools.product(range(-4, 5), repeat=3))
    radii_opts = tuple(
        radii
        for radii in itertools.product((1, 2, 3), repeat=3)
        if not (radii[0] == radii[1] == radii[2])
    )
    ball_enc = {
        (seed, radius): tuple(enc(site) for site in ball(seed, radius))
        for seed in seed_box
        for radius in (1, 2, 3)
    }
    v_enc = tuple(enc(site) for site in v_box)
    neighbor_enc = tuple(
        tuple(enc(add(site, direction)) for direction in DIRS) for site in v_box
    )
    mark = array("I", [0]) * GRID
    generation = 0
    n_wt4 = 0
    prefix_seen: set[Coloring] = set()
    first_star: tuple | None = None

    for s1, s2, s3 in itertools.combinations(seed_box, 3):
        seeds = (s1, s2, s3)
        for radii in radii_opts:
            generation += 1
            for seed, radius in zip(seeds, radii):
                for index in ball_enc[(seed, radius)]:
                    mark[index] = generation
            for v_index, site in enumerate(v_box):
                if mark[v_enc[v_index]] == generation:
                    continue
                sigma = tuple(
                    1 if mark[w_enc] == generation else 0
                    for w_enc in neighbor_enc[v_index]
                )
                if sum(sigma) != 4:
                    continue
                n_wt4 += 1
                if first_star is None:
                    first_star = (seeds, radii, site, sigma)
                if sigma in remaining:
                    remaining.remove(sigma)
                    hosts[sigma] = (seeds, radii, site)
                if n_wt4 <= PREFIX and sigma in masks:
                    prefix_seen.add(sigma)
            if n_wt4 >= PREFIX and not remaining:
                break
        else:
            continue
        break

    return {
        "masks": masks,
        "hosts": hosts,
        "n_real": len(masks) - len(remaining),
        "n_wt4": n_wt4,
        "n_prefix": min(n_wt4, PREFIX),
        "n_prefix_real": len(prefix_seen),
        "first_star": first_star,
        "seed_count": len(seed_box),
        "v_count": len(v_box),
        "radii_count": len(radii_opts),
        "remaining": remaining,
    }


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")
    literal_paths = parse_audit_input_paths(self_source)
    data = realize()
    masks = data["masks"]
    hosts = data["hosts"]
    n_real = data["n_real"]
    n_prefix = data["n_prefix"]
    n_prefix_real = data["n_prefix_real"]

    print("perp-mask 3-ball realization")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"seed_box_card={data['seed_count']}")
    print(f"v_box_card={data['v_count']}")
    print(f"radii_card={data['radii_count']}")
    print(f"N_perp={len(masks)}")
    print(f"N_prefix={n_prefix}")
    print(f"N_prefix_real={n_prefix_real}")
    print(f"N_real={n_real}")
    print(f"first_star={data['first_star']}")
    print("lex_first_hosts:")
    for sigma in masks:
        print(f"  {sigma} {hosts.get(sigma)}")

    expected_paths = (
        "docs/PERP_MASK_THREE_BALL_REALIZATION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
    )
    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS == expected_paths
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    covariance_clause = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    unread_sentence = "A site with no record cannot be read."
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "source-lattice",
        lattice_sentence in axiom_flat and lattice_sentence in note_flat,
    )
    checks.check(
        "source-admissibility",
        covariance_clause in axiom_flat
        and admissibility_sentence in axiom_flat
        and covariance_clause in note_flat
        and admissibility_sentence in note_flat,
    )
    checks.check(
        "source-unread-qubit",
        unread_sentence in axiom
        and unread_sentence in note
        and qubit_sentence in axiom
        and qubit_sentence in note,
    )
    checks.check(
        "perp-mask-count",
        len(masks) == 12
        and masks[0] == (0, 1, 0, 1, 1, 1)
        and masks[-1] == (1, 1, 1, 0, 1, 0)
        and all(sum(mask) == 4 for mask in masks)
        and "12 perpendicular" in note_flat,
        f"N_perp={len(masks)}",
    )
    checks.check(
        "theorem-1-n-real",
        n_real == 12
        and not data["remaining"]
        and "N_real = 12" in note
        and "all 12" in note_flat,
        f"N_real={n_real}",
    )
    checks.check(
        "prefix-2000",
        n_prefix == PREFIX
        and n_prefix_real == 12
        and "N_prefix = 2000" in note
        and "N_prefix_real = 12" in note,
        f"N_prefix={n_prefix} N_prefix_real={n_prefix_real}",
    )
    for sigma in masks:
        host = hosts.get(sigma)
        checks.check(
            f"exists-mask-{sigma}",
            host is not None and str(host) in note,
            str(host),
        )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write a host into Admissibility" in note
        and "hypothetical_axiom_status:" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "l1-not-attached",
        "Do not attach L1" in note
        and "we attach L1" not in note_flat
        and "we add a 4th ball" not in note_flat,
    )
    checks.check(
        "not-leftover-uneqrad",
        "not leftover of uneqrad (one mask)" in note_flat
        and "uneqrad" in note,
    )
    checks.check(
        "admissibility-unedited",
        covariance_clause in axiom_flat
        and "N_real" not in axiom
        and "N_prefix_real" not in axiom
        and "perp mask" not in axiom
        and "3-ball union" not in axiom,
    )
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in FORBIDDEN)
        and all(
            phrase not in self_source.split("FORBIDDEN = ", 1)[0]
            for phrase in FORBIDDEN
        ),
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "cache_write: false" in self_source
        and AXIOM_REL in AUDIT_INPUT_PATHS
        and "no axiom" in note_flat.lower(),
    )

    print("per_element: N_real, N_prefix, and N_prefix_real are exact integers")
    print("per_site: unread weight-4 uneqrad 3-ball stars in the declared box")
    print("per_mode: no spectral calculation")
    print("per_block: 12 perp masks and 3-ball stars")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
