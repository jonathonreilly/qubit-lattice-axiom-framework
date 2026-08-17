#!/usr/bin/env python3
"""Census: occupied-NN count k versus lock-tick t on mixed-t stars.

Same box as uneqrad. Score a 2000-star prefix of unread weight-4
stars whose occupied lock-ticks are not all equal. Compare the
occupied 4-tuple k of occupied-NN counts inside U with t.
Displayed, not adopted. No cache is written.
"""

from __future__ import annotations

import ast
from itertools import combinations, product
from pathlib import Path
from typing import Iterator


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/UNEQUAL_RADIUS_K_EQUALS_TICK_CENSUS_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/UNEQUAL_RADIUS_K_EQUALS_TICK_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int, ...]
StarRec = dict[str, object]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    'claim_scope: "On a prefix of mixed-t unequal-radius weight-4 stars, '
    "whether occupied-NN count equals lock-tick is reported. "
    'Displayed, not adopted."'
)
PREFIX_CAP = 2000
CENTER_BOX = 2
SITE_BOX = 4
RADII_MENU = (1, 2, 3)
UNEQSRC_SEEDS: tuple[Point, ...] = ((-2, -2, -2), (-2, -2, -1), (-2, -2, 1))
UNEQSRC_RADII = (2, 1, 3)
UNEQSRC_V: Point = (-3, -3, -1)
EXPECTED_UNEQSRC_T = (1, 1, 3, 2)
EXPECTED_UNEQSRC_K = (3, 3, 3, 2)
EXPECTED_N_PREFIX = 2000
EXPECTED_N_EQ = 27
EXPECTED_FIRST_NE_SEEDS: tuple[Point, ...] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 0),
)
EXPECTED_FIRST_NE_RADII = (2, 1, 2)
EXPECTED_FIRST_NE_V: Point = (-3, -3, -1)
EXPECTED_FIRST_NE_SIGMA: Coloring = (1, 0, 1, 0, 1, 1)
EXPECTED_FIRST_NE_T = (1, 1, 2, 2)
EXPECTED_FIRST_NE_K = (3, 3, 2, 2)
EXPECTED_FIRST_EQ_SEEDS: tuple[Point, ...] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, 1, 1),
)
EXPECTED_FIRST_EQ_RADII = (2, 2, 1)
EXPECTED_FIRST_EQ_V: Point = (-2, 0, 0)
EXPECTED_FIRST_EQ_T = (1, 2, 1, 2)
EXPECTED_FIRST_EQ_K = (1, 2, 1, 2)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def box_points(half: int) -> tuple[Point, ...]:
    span = range(-half, half + 1)
    return tuple(product(span, repeat=3))


def radii_options() -> tuple[tuple[int, ...], ...]:
    return tuple(
        radii
        for radii in product(RADII_MENU, repeat=3)
        if len(set(radii)) > 1
    )


def build_union(seeds: tuple[Point, ...], radii: tuple[int, ...]) -> set[Point]:
    union: set[Point] = set()
    for seed, radius in zip(seeds, radii, strict=True):
        span = range(-radius, radius + 1)
        sx, sy, sz = seed
        for dx in span:
            for dy in span:
                for dz in span:
                    if abs(dx) + abs(dy) + abs(dz) <= radius:
                        union.add((sx + dx, sy + dy, sz + dz))
    return union


def occupied_star(
    site: Point, union: set[Point], seeds: tuple[Point, ...]
) -> tuple[Coloring, Tick, tuple[Point, ...]]:
    sigma: list[int] = []
    ticks: list[int] = []
    occupied: list[Point] = []
    contained = union.__contains__
    for direction in DIRS:
        neighbor = add(site, direction)
        if contained(neighbor):
            sigma.append(1)
            ticks.append(min(l1(neighbor, seed) for seed in seeds))
            occupied.append(neighbor)
        else:
            sigma.append(0)
    return tuple(sigma), tuple(ticks), tuple(occupied)


def occupied_nn_counts(occupied: tuple[Point, ...], union: set[Point]) -> Tick:
    contained = union.__contains__
    return tuple(
        sum(1 for direction in DIRS if contained(add(neighbor, direction)))
        for neighbor in occupied
    )


def mixed_tick_stars(limit: int) -> Iterator[StarRec]:
    centers = box_points(CENTER_BOX)
    sites = box_points(SITE_BOX)
    yielded = 0
    for seeds in combinations(centers, 3):
        for radii in radii_options():
            union = build_union(seeds, radii)
            contained = union.__contains__
            for site in sites:
                if contained(site):
                    continue
                sigma, ticks, occupied = occupied_star(site, union, seeds)
                if len(occupied) != 4:
                    continue
                if ticks[0] == ticks[1] == ticks[2] == ticks[3]:
                    continue
                counts = occupied_nn_counts(occupied, union)
                yielded += 1
                yield {
                    "index": yielded,
                    "seeds": seeds,
                    "radii": radii,
                    "v": site,
                    "sigma": sigma,
                    "t": ticks,
                    "k": counts,
                    "equal": counts == ticks,
                }
                if yielded >= limit:
                    return


def score_prefix(limit: int = PREFIX_CAP) -> dict[str, object]:
    n_eq = 0
    first_ne: StarRec | None = None
    first_eq: StarRec | None = None
    uneqsrc: StarRec | None = None
    last: StarRec | None = None
    for record in mixed_tick_stars(limit):
        last = record
        if record["equal"]:
            n_eq += 1
            if first_eq is None:
                first_eq = record
        elif first_ne is None:
            first_ne = record
        if (
            record["seeds"] == UNEQSRC_SEEDS
            and record["radii"] == UNEQSRC_RADII
            and record["v"] == UNEQSRC_V
        ):
            uneqsrc = record
    n_prefix = 0 if last is None else int(last["index"])
    return {
        "n_prefix": n_prefix,
        "n_eq": n_eq,
        "n_eq_is_zero": n_eq == 0,
        "first_disagreement": first_ne,
        "first_equality": first_eq,
        "uneqsrc": uneqsrc,
    }


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


def fmt_tuple(values: object) -> str:
    if not isinstance(values, tuple):
        return str(values)
    inner = ", ".join(
        fmt_tuple(item) if isinstance(item, tuple) else str(item) for item in values
    )
    return f"({inner})"


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
    scored = score_prefix()
    n_prefix = int(scored["n_prefix"])
    n_eq = int(scored["n_eq"])
    first_ne = scored["first_disagreement"]
    first_eq = scored["first_equality"]
    uneqsrc = scored["uneqsrc"]
    assert isinstance(first_ne, dict)
    assert isinstance(first_eq, dict)
    assert isinstance(uneqsrc, dict)

    print("unequal-radius k-equals-tick census")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"N_prefix={n_prefix}")
    print(f"N_eq={n_eq}")
    print(f"N_eq_is_zero={bool(scored['n_eq_is_zero'])}")
    print(
        "lex_first_disagreement: "
        f"seeds={fmt_tuple(first_ne['seeds'])} "
        f"radii={fmt_tuple(first_ne['radii'])} "
        f"v={fmt_tuple(first_ne['v'])} "
        f"t={fmt_tuple(first_ne['t'])} "
        f"k={fmt_tuple(first_ne['k'])}"
    )
    print(
        "uneqsrc: "
        f"index={uneqsrc['index']} "
        f"t={fmt_tuple(uneqsrc['t'])} "
        f"k={fmt_tuple(uneqsrc['k'])} "
        f"equal={uneqsrc['equal']}"
    )
    print(
        "lex_first_equality: "
        f"index={first_eq['index']} "
        f"t={fmt_tuple(first_eq['t'])} "
        f"k={fmt_tuple(first_eq['k'])}"
    )

    expected_paths = (
        "docs/UNEQUAL_RADIUS_K_EQUALS_TICK_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content"
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
        "source-record-qubit",
        record_lock in axiom
        and record_lock in note
        and record_content in axiom
        and record_content in note
        and unread_sentence in axiom
        and unread_sentence in note
        and qubit_sentence in axiom
        and qubit_sentence in note,
    )
    checks.check(
        "theorem-1-n-prefix",
        n_prefix == EXPECTED_N_PREFIX
        and n_prefix == PREFIX_CAP
        and "`N_prefix = 2000`" in note,
        f"N_prefix={n_prefix}",
    )
    checks.check(
        "theorem-1-n-eq",
        n_eq == EXPECTED_N_EQ and "`N_eq = 27`" in note,
        f"N_eq={n_eq}",
    )
    checks.check(
        "theorem-2-n-eq-not-zero",
        scored["n_eq_is_zero"] is False
        and n_eq > 0
        and "N_eq` is not 0" in note
        and "k` never equals `t`" not in note_flat.replace(" ", ""),
        f"N_eq_is_zero={scored['n_eq_is_zero']}",
    )
    checks.check(
        "theorem-2-lex-first-disagreement",
        first_ne["seeds"] == EXPECTED_FIRST_NE_SEEDS
        and first_ne["radii"] == EXPECTED_FIRST_NE_RADII
        and first_ne["v"] == EXPECTED_FIRST_NE_V
        and first_ne["sigma"] == EXPECTED_FIRST_NE_SIGMA
        and first_ne["t"] == EXPECTED_FIRST_NE_T
        and first_ne["k"] == EXPECTED_FIRST_NE_K
        and first_ne["equal"] is False
        and first_ne["index"] == 1
        and "`t = (1, 1, 2, 2)`" in note
        and "`k = (3, 3, 2, 2)`" in note
        and "radii `(2, 1, 2)`" in note
        and "`v = (−3,−3,−1)`" in note,
        f"first_ne={first_ne['seeds'], first_ne['radii'], first_ne['v']}",
    )
    checks.check(
        "uneqsrc-disagreement-recorded",
        uneqsrc["t"] == EXPECTED_UNEQSRC_T
        and uneqsrc["k"] == EXPECTED_UNEQSRC_K
        and uneqsrc["equal"] is False
        and uneqsrc["index"] == 21
        and "`t = (1, 1, 3, 2)`" in note
        and "`k = (3, 3, 3, 2)`" in note
        and "already uneqsrc" in note_flat,
        f"uneqsrc_index={uneqsrc['index']}",
    )
    checks.check(
        "first-equality-on-prefix",
        first_eq["seeds"] == EXPECTED_FIRST_EQ_SEEDS
        and first_eq["radii"] == EXPECTED_FIRST_EQ_RADII
        and first_eq["v"] == EXPECTED_FIRST_EQ_V
        and first_eq["t"] == EXPECTED_FIRST_EQ_T
        and first_eq["k"] == EXPECTED_FIRST_EQ_K
        and first_eq["equal"] is True
        and first_eq["index"] == 342
        and "`k = t = (1, 2, 1, 2)`" in note,
        f"first_eq_index={first_eq['index']}",
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write `k` as `t` into Admissibility" in note
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
        "not-leftover-uneqsrc",
        "not leftover of uneqsrc" in note_flat
        and "one star" in note
        and "uneqsrc" in note,
    )
    checks.check(
        "admissibility-record-unedited",
        covariance_clause in axiom_flat
        and record_lock in axiom
        and "lock-tick" not in axiom
        and "unequal-radius" not in axiom,
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

    print("per_element: scored occupied-NN count k against occupied lock-tick t")
    print("per_site: scored a 2000-star mixed-t unread weight-4 prefix")
    print("per_mode: no spectral calculation; occupancy geometry only")
    print("per_block: 3-ball unequal-radius host only; no fourth ball")
    print(
        "lattice_wide: checked and not executed — finite prefix in the "
        "uneqrad box, not a lattice-wide rule"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
