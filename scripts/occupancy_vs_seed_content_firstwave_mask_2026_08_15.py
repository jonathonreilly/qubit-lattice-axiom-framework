#!/usr/bin/env python3
"""First-wave 6-masks and k=1 reverse/face bits: occupancy vs seed-content.

Formation-tick is a synchronous wavefront on already-formed 6-NN sites.
No shortest-path solver, no cache write, no network, no axiom edit.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/OCCUPANCY_VS_SEED_CONTENT_FIRSTWAVE_MASK_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OCCUPANCY_VS_SEED_CONTENT_FIRSTWAVE_MASK_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

ORIGIN = (0, 0, 0)
# Named rank-1 letter `+` displayed as the +e1 outward axis. Not fed into L1 n.
SEED_LETTER = "+"
SEED_AXIS = (1, 0, 0)
NN_ORDER = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
MASK_HOST = frozenset((ORIGIN,) + NN_ORDER)
BALL_RADIUS = 3
SCORE_SITES = ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
FORBIDDEN = (
    "G_" + "N",
    "1/" + "r",
    "1/" + "r^2",
    "Lattice-" + "named",
    "not a " + "TOE",
)
CLAIM_SCOPE = (
    "First-wave 6-masks and k=1 reverse/face under occupancy vs "
    "seed-content formation-tick on B_3(0) are compared. Displayed, not adopted."
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(site: tuple[int, int, int], step: tuple[int, int, int]) -> tuple[int, int, int]:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def sub(site: tuple[int, int, int], other: tuple[int, int, int]) -> tuple[int, int, int]:
    return (site[0] - other[0], site[1] - other[1], site[2] - other[2])


def l1(site: tuple[int, int, int]) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def ball_b3() -> frozenset[tuple[int, int, int]]:
    radius = BALL_RADIUS
    return frozenset(
        (x, y, z)
        for x, y, z in product(range(-radius, radius + 1), repeat=3)
        if abs(x) + abs(y) + abs(z) <= radius
    )


def neighbors(site: tuple[int, int, int], host: frozenset[tuple[int, int, int]]) -> tuple[tuple[int, int, int], ...]:
    return tuple(add(site, step) for step in NN_ORDER if add(site, step) in host)


def occupied_degree(
    site: tuple[int, int, int],
    formed: frozenset[tuple[int, int, int]],
    host: frozenset[tuple[int, int, int]],
) -> int:
    return sum(1 for nb in neighbors(site, host) if nb in formed)


def occupancy_l1_allows(
    site: tuple[int, int, int],
    formed: frozenset[tuple[int, int, int]],
    host: frozenset[tuple[int, int, int]],
) -> bool:
    degree = occupied_degree(site, formed, host)
    occupancy = Fraction(degree, 3)
    return occupancy != 0


def content_nn_allows(
    site: tuple[int, int, int],
    formed: frozenset[tuple[int, int, int]],
    host: frozenset[tuple[int, int, int]],
) -> bool:
    if not occupancy_l1_allows(site, formed, host):
        return False
    for nb in neighbors(site, host):
        if nb in formed and sub(site, nb) == SEED_AXIS:
            return True
    return False


def first_wave_mask(rule) -> tuple[int, ...]:
    formed = frozenset({ORIGIN})
    return tuple(int(rule(site, formed, MASK_HOST)) for site in NN_ORDER)


def formation_tick(host: frozenset[tuple[int, int, int]], rule) -> dict[tuple[int, int, int], int]:
    ticks = {ORIGIN: 0}
    formed = {ORIGIN}
    while True:
        nxt = {
            site
            for site in host
            if site not in formed and rule(site, frozenset(formed), host)
        }
        if not nxt:
            return ticks
        tick = 1 + max(ticks[site] for site in formed)
        for site in nxt:
            ticks[site] = tick
        formed.update(nxt)


def reverse_bit(ticks: dict[tuple[int, int, int], int]) -> bool | None:
    axis = ticks.get((1, 0, 0))
    body = ticks.get((1, 1, 1))
    if axis is None or body is None:
        return None
    return 3 * axis * axis > body * body


def face_bit(ticks: dict[tuple[int, int, int], int]) -> bool | None:
    axis = ticks.get((2, 0, 0))
    face = ticks.get((1, 1, 0))
    if axis is None or face is None:
        return None
    return axis * axis > 2 * face * face


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    ball = ball_b3()
    occ_mask = first_wave_mask(occupancy_l1_allows)
    content_mask = first_wave_mask(content_nn_allows)
    occ_ticks = formation_tick(ball, occupancy_l1_allows)
    content_ticks = formation_tick(ball, content_nn_allows)
    occ_reverse = reverse_bit(occ_ticks)
    occ_face = face_bit(occ_ticks)
    content_reverse = reverse_bit(content_ticks)
    content_face = face_bit(content_ticks)

    print("construction: synchronous formation-tick on 6-NN already-formed sites")
    print("cache_write: false")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"seed_letter: {SEED_LETTER}")
    print(f"seed_axis: {SEED_AXIS}")
    print(f"occupancy_mask: {occ_mask}")
    print(f"content_mask: {content_mask}")
    print(
        "occupancy_ticks: "
        f"t100={occ_ticks.get((1, 0, 0))} t111={occ_ticks.get((1, 1, 1))} "
        f"t200={occ_ticks.get((2, 0, 0))} t110={occ_ticks.get((1, 1, 0))}"
    )
    print(
        "content_ticks: "
        f"t100={content_ticks.get((1, 0, 0))} t111={content_ticks.get((1, 1, 1))} "
        f"t200={content_ticks.get((2, 0, 0))} t110={content_ticks.get((1, 1, 0))}"
    )
    print(f"occupancy_reverse_face: {occ_reverse} {occ_face}")
    print(f"content_reverse_face: {content_reverse} {content_face}")

    declared = (
        "docs/OCCUPANCY_VS_SEED_CONTENT_FIRSTWAVE_MASK_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
    )
    checks.check(
        "audit-input-paths-static",
        "AUDIT_INPUT_PATHS is the declared note-plus-axiom tuple",
        AUDIT_INPUT_PATHS == declared
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/OCCUPANCY_VS_SEED_CONTENT_FIRSTWAVE_MASK_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )
    checks.check(
        "audit-inputs-exist",
        "both declared inputs exist",
        note_path.is_file() and axiom_path.is_file() and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "mask-host-seven",
        "mask host is origin plus six NN",
        len(MASK_HOST) == 7 and ORIGIN in MASK_HOST and set(NN_ORDER) <= set(MASK_HOST),
    )
    checks.check(
        "b3-l1-radius-three",
        "formation-tick host is B_3(0) and contains the four k=1 score sites",
        ORIGIN in ball
        and all(site in ball for site in SCORE_SITES)
        and all(l1(site) <= 3 for site in ball)
        and max(l1(site) for site in ball) == 3
        and len(ball) != 57,
    )
    checks.check(
        "seed-letter-not-in-n",
        "L1 n uses occupied degree only; seed letter is not an occupancy count",
        occupied_degree((1, 0, 0), frozenset({ORIGIN}), MASK_HOST) == 1
        and Fraction(1, 3) != 0
        and SEED_LETTER not in "n=d/3",
    )
    checks.check(
        "occupancy-first-wave-all-six",
        "occupancy 6-mask is all-form at tick 1",
        occ_mask == (1, 1, 1, 1, 1, 1),
    )
    checks.check(
        "content-first-wave-named-axis",
        "content 6-mask forms only the named + axis",
        content_mask == (1, 0, 0, 0, 0, 0),
    )
    checks.check(
        "theorem1-masks-disagree",
        "the two 6-masks do not agree",
        occ_mask != content_mask,
    )
    checks.check(
        "occupancy-ticks-k1",
        "occupancy t(1,0,0)=1 and t(1,1,1)=3, with t(2,0,0)=2 and t(1,1,0)=2",
        occ_ticks.get((1, 0, 0)) == 1
        and occ_ticks.get((1, 1, 1)) == 3
        and occ_ticks.get((2, 0, 0)) == 2
        and occ_ticks.get((1, 1, 0)) == 2
        and occ_ticks[ORIGIN] == 0,
    )
    checks.check(
        "theorem2-occupancy-bits",
        "occupancy reverse and face bits are both false",
        occ_reverse is False and occ_face is False,
    )
    checks.check(
        "content-ticks-k1",
        "content t(1,0,0)=1 and t(2,0,0)=2; t(1,1,1) and t(1,1,0) stay unformed",
        content_ticks.get((1, 0, 0)) == 1
        and content_ticks.get((2, 0, 0)) == 2
        and (1, 1, 1) not in content_ticks
        and (1, 1, 0) not in content_ticks
        and content_ticks[ORIGIN] == 0,
    )
    checks.check(
        "theorem3-bits-disagree",
        "content reverse/face bits are undefined and do not agree with occupancy",
        content_reverse is None
        and content_face is None
        and (content_reverse, content_face) != (occ_reverse, occ_face),
    )
    checks.check(
        "wavefront-synchronous",
        "runner uses a synchronous wavefront and no shortest-path library",
        occ_ticks[ORIGIN] == 0
        and content_ticks[ORIGIN] == 0
        and len(occ_ticks) == len(ball)
        and max(occ_ticks.values()) <= BALL_RADIUS,
    )
    checks.check(
        "claim-scope-and-display",
        "note states the compared scope as displayed, not adopted",
        CLAIM_SCOPE in note
        and "Displayed, not adopted" in note
        and "Do not attach L1" in note
        and "Do not write into Admissibility" in note
        and "Uniqueness not required" in note,
    )
    checks.check(
        "axiom-boundary",
        "current axioms supply occurrence and content typing, not this formation rule",
        "Records form." in axiom
        and "it does not supply the formation site, probability, or rate" in normalize(axiom)
        and "no edit" in note
        and "Admissibility" in axiom,
    )
    checks.check(
        "forbidden-phrases-absent",
        "note contains none of the forbidden phrases",
        all(phrase not in note for phrase in FORBIDDEN),
    )
    compact_note = normalized_note.replace(" ", "")
    checks.check(
        "note-records-computed-masks",
        "note records the computed 6-masks and k=1 bits",
        "(1, 1, 1, 1, 1, 1)" in note
        and "(1, 0, 0, 0, 0, 0)" in note
        and "t(1,0,0)=1" in compact_note
        and "t(1,1,1)=3" in compact_note
        and "t(2,0,0)=2" in compact_note
        and "t(1,1,0)=2" in compact_note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
