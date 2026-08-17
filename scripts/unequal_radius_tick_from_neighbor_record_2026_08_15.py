#!/usr/bin/env python3
"""Neighbor-Record clocks versus M_2 on the uneqrad lex-first star.

U, v are the uneqrad lex-first breaker. Occupied neighbors display the
ℓ¹-to-nearest-seed clock t(w). The 6-tuple of (occupied?, clock-or-none)
is compared with (σ, t). The same M_2 lock on every occupied neighbor
shows that Record-as-M_2 does not supply t. Displayed, not adopted.
No cache is written.
"""

from __future__ import annotations

import ast
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/UNEQUAL_RADIUS_TICK_FROM_NEIGHBOR_RECORD_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/UNEQUAL_RADIUS_TICK_FROM_NEIGHBOR_RECORD_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Coloring = tuple[int, ...]
Tick = tuple[int | None, ...]
RecordSlot = tuple[int, int | None]

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
    'claim_scope: "On the lex-first unequal-radius breaker, '
    "whether neighbor Records valued in M_2 supply the lock-tick field "
    'is reported. Displayed, not adopted."'
)
SEEDS: tuple[Point, Point, Point] = (
    (-2, -2, -2),
    (-2, -2, -1),
    (-2, -2, 1),
)
RADII = (2, 1, 3)
V: Point = (-3, -3, -1)
EXPECTED_SIGMA: Coloring = (1, 0, 1, 0, 1, 1)
EXPECTED_TICKS: Tick = (1, None, 1, None, 3, 2)
EXPECTED_RECORD: tuple[RecordSlot, ...] = (
    (1, 1),
    (0, None),
    (1, 1),
    (0, None),
    (1, 3),
    (1, 2),
)
COMMON_PROJECTOR = ((1, 0), (0, 0))
COMMON_BLOCH = (0, 0, 1)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def l1(left: Point, right: Point) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1]) + abs(left[2] - right[2])


def in_union(point: Point, seeds: tuple[Point, ...], radii: tuple[int, ...]) -> bool:
    return any(l1(point, seed) <= radius for seed, radius in zip(seeds, radii))


def occupancy_ticks(
    seeds: tuple[Point, ...], radii: tuple[int, ...], site: Point
) -> tuple[Coloring, Tick]:
    sigma: list[int] = []
    ticks: list[int | None] = []
    for direction in DIRS:
        neighbor = add(site, direction)
        if in_union(neighbor, seeds, radii):
            sigma.append(1)
            ticks.append(min(l1(neighbor, seed) for seed in seeds))
        else:
            sigma.append(0)
            ticks.append(None)
    return tuple(sigma), tuple(ticks)


def record_tuple(sigma: Coloring, ticks: Tick) -> tuple[RecordSlot, ...]:
    return tuple((occupied, clock) for occupied, clock in zip(sigma, ticks))


def bloch_of_projector(projector: tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int, int]:
    a, b = projector[0]
    c, d = projector[1]
    # P = (I + r·σ)/2  ⇒  r = (2 Re P_01, 2 Im P_01, P_00 − P_11)
    return (b + c, 0, a - d)


def l1_bloch_occupancy(sigma: Coloring) -> Coloring:
    # L1 Bloch is an occupancy function: present Record ↦ 1, unread ↦ 0.
    return tuple(int(bit == 1) for bit in sigma)


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

    sigma, ticks = occupancy_ticks(SEEDS, RADII, V)
    displayed = record_tuple(sigma, ticks)
    unread = not in_union(V, SEEDS, RADII)
    occupied_clocks = tuple(clock for bit, clock in zip(sigma, ticks) if bit == 1)
    bloch = bloch_of_projector(COMMON_PROJECTOR)
    bloch_occ = l1_bloch_occupancy(sigma)
    same_m2_on_occupied = len(set(occupied_clocks)) > 1 and bloch == COMMON_BLOCH
    clocks_not_m2_function = same_m2_on_occupied and bloch_occ == sigma
    record_as_m2_supplies_t = False if clocks_not_m2_function else None
    occupancy_alone = displayed == tuple((bit, 1 if bit else None) for bit in sigma)

    print("unequal-radius tick from neighbor Record")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(f"seeds={SEEDS}")
    print(f"radii={RADII}")
    print(f"v={V}")
    print(f"unread={unread}")
    print(f"sigma={sigma}")
    print(f"ticks={ticks}")
    print(f"record_6tuple={displayed}")
    print(f"equals_sigma_t={displayed == record_tuple(sigma, ticks)}")
    print(f"occupancy_alone={occupancy_alone}")
    print(f"occupied_clocks={occupied_clocks}")
    print(f"common_projector={COMMON_PROJECTOR}")
    print(f"common_bloch={bloch}")
    print(f"l1_bloch_occupancy={bloch_occ}")
    print(f"clocks_not_function_of_M2={clocks_not_m2_function}")
    print(f"Record_as_M2_supplies_t={record_as_m2_supplies_t}")

    expected_paths = (
        "docs/UNEQUAL_RADIUS_TICK_FROM_NEIGHBOR_RECORD_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "host-lex-first-breaker",
        unread
        and sigma == EXPECTED_SIGMA
        and ticks == EXPECTED_TICKS
        and len(set(RADII)) > 1
        and "`v = (−3,−3,−1)`" in note
        and "radii `(2, 1, 3)`" in note
        and "`σ = (1, 0, 1, 0, 1, 1)`" in note
        and "`t = (1, ·, 1, ·, 3, 2)`" in note,
        f"sigma={sigma} ticks={ticks}",
    )
    checks.check(
        "theorem-1-six-tuple-equals-sigma-t",
        displayed == EXPECTED_RECORD
        and displayed == record_tuple(EXPECTED_SIGMA, EXPECTED_TICKS)
        and "That 6-tuple equals `(σ,t)` on this star" in note
        and "`ρ = ((1, 1), (0, ·), (1, 1), (0, ·), (1, 3), (1, 2))`" in note,
        f"rho={displayed}",
    )
    checks.check(
        "theorem-1-not-occupancy-alone",
        not occupancy_alone
        and set(occupied_clocks) == {1, 2, 3}
        and "It is not occupancy alone" in note
        and "not occupancy alone" in note_flat,
        f"occupied_clocks={occupied_clocks}",
    )
    checks.check(
        "theorem-2-clocks-not-m2-function",
        clocks_not_m2_function
        and bloch == COMMON_BLOCH
        and bloch_occ == sigma
        and occupied_clocks == (1, 1, 3, 2)
        and "Those clocks are not a function of the qubit state on `M_2` at `w`"
        in note
        and "L1 Bloch is an occupancy function" in note,
        f"bloch={bloch} bloch_occ={bloch_occ}",
    )
    checks.check(
        "theorem-2-record-as-m2-does-not-supply-t",
        record_as_m2_supplies_t is False
        and "So Record-as-`M_2` does not supply" in note
        and "Naming seed-distance as Record content is the same extra" in note,
    )
    checks.check("claim-scope", CLAIM_SCOPE in note)
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not write a clock into Record or Admissibility" in note
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
        "not-leftover-delloc-uneqext",
        "not leftover of delloc" in note_flat
        and "product rule" in note
        and "uneqext" in note
        and "extra vs occupancy" in note,
    )
    checks.check(
        "admissibility-record-unedited",
        covariance_clause in axiom_flat
        and record_lock in axiom
        and "lock-tick" not in axiom
        and "seed-distance" not in axiom
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

    print(
        "per_element: scored the displayed (occupied?, clock-or-none) "
        "6-tuple against (σ,t) and against one common M_2 lock"
    )
    print("per_site: scored only the uneqrad lex-first star at v")
    print("per_mode: no spectral calculation; occupancy, ticks, and M_2 lock only")
    print("per_block: 3-ball unequal-radius host only; no fourth ball")
    print(
        "lattice_wide: checked and not executed — one finite 6-star, "
        "not a lattice-wide rule"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
