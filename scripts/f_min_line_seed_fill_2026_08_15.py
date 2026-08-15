#!/usr/bin/env python3
"""Line-seed fill of the named nonempty n_both=0 map on the two-cube.

Displayed occupancy-to-lock dynamics only. The runner does not adopt
f_min and does not write it into Admissibility.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_MIN_LINE_SEED_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_MIN_LINE_SEED_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]

TWO_CUBE: tuple[Point, ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SEED: frozenset[Point] = frozenset(((0, 0, 0), (1, 0, 0), (2, 0, 0)))
AXIS_SHIFTS: tuple[tuple[Point, Point], ...] = (
    ((1, 0, 0), (-1, 0, 0)),
    ((0, 1, 0), (0, -1, 0)),
    ((0, 0, 1), (0, 0, -1)),
)
ONE_SITE_L1_HISTORY = (1, 4, 8, 11, 12)
LINE_L1_HISTORY = (3, 9, 12)

# Axis-type orbit representatives in order (+x, -x, +y, -y, +z, -z).
ORBIT_REPS: dict[str, Config] = {
    "empty": (0, 0, 0, 0, 0, 0),
    "wt1": (1, 0, 0, 0, 0, 0),
    "opp2": (1, 1, 0, 0, 0, 0),
    "adj2": (1, 0, 1, 0, 0, 0),
    "vertex3": (1, 0, 1, 0, 1, 0),
    "mixed3": (1, 0, 1, 1, 0, 0),
    "full": (1, 1, 1, 1, 1, 1),
}


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def on_patch(site: Point) -> bool:
    return site in TWO_CUBE_SET


TWO_CUBE_SET = frozenset(TWO_CUBE)


def occupancy(site: Point, locks: frozenset[Point]) -> int:
    if not on_patch(site):
        return 0
    return 1 if site in locks else 0


def neighbor_config(site: Point, locks: frozenset[Point]) -> Config:
    bits: list[int] = []
    for plus, minus in AXIS_SHIFTS:
        bits.append(occupancy(add(site, plus), locks))
        bits.append(occupancy(add(site, minus), locks))
    return (bits[0], bits[1], bits[2], bits[3], bits[4], bits[5])


def axis_type(config: Config) -> tuple[int, int, int]:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for index in (0, 2, 4):
        plus, minus = config[index], config[index + 1]
        if plus == 1 and minus == 1:
            n_both += 1
        elif plus == 0 and minus == 0:
            n_empty += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def f_l1(config: Config) -> int:
    n_unbalanced, _n_both, _n_empty = axis_type(config)
    return 1 if n_unbalanced >= 1 else 0


def f_min(config: Config) -> int:
    n_unbalanced, n_both, _n_empty = axis_type(config)
    return 1 if n_both == 0 and n_unbalanced >= 1 else 0


def support_size(predicate) -> int:
    count = 0
    for bits in range(64):
        config = (
            (bits >> 0) & 1,
            (bits >> 1) & 1,
            (bits >> 2) & 1,
            (bits >> 3) & 1,
            (bits >> 4) & 1,
            (bits >> 5) & 1,
        )
        count += predicate(config)
    return count


def step(locks: frozenset[Point], predicate) -> frozenset[Point]:
    newcomers = {
        site
        for site in TWO_CUBE
        if site not in locks and predicate(neighbor_config(site, locks)) == 1
    }
    return locks | newcomers


def run_from_seed(seed: frozenset[Point], predicate, halt_bound: int = 12):
    locks = frozenset(seed)
    history = [len(locks)]
    tick = 0
    while tick < halt_bound:
        nxt = step(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        tick += 1
        history.append(len(locks))
    return tick, frozenset(locks), tuple(history)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the live axiom memo; no other scientific inputs")
    print("construction: displayed cube-covariant occupancy-to-lock maps on the twelve-vertex two-cube")
    print("negative_scope: f_min is displayed, not adopted, and is not written into Admissibility")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIN_LINE_SEED_FILL_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_boundary = "does not supply the formation site, probability, or rate"
    record_lock = "When present, a record locks exactly one admissible local possibility."
    not_dynamics = "Admissibility is not a dynamics axiom."

    checks.check(
        "source-lattice",
        "current cubic nearest-neighbor wording is pinned",
        lattice_sentence in normalize(axiom) and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in normalize(axiom) and admissibility_sentence in note,
    )
    checks.check(
        "source-formation-boundary",
        "formation site, probability, and rate remain outside Admissibility",
        formation_boundary in normalize(axiom) and formation_boundary in normalize(note),
    )
    checks.check(
        "source-record-and-non-dynamics",
        "Record lock wording and the non-dynamics Admissibility boundary are pinned",
        record_lock in normalize(axiom)
        and record_lock in note
        and not_dynamics in axiom
        and not_dynamics in note,
    )

    checks.check("two-cube-cardinality", "the two-cube has exactly twelve vertices", len(TWO_CUBE) == 12 and len(TWO_CUBE_SET) == 12)
    checks.check(
        "line-seed",
        "S is the three-site long-axis seed",
        SEED == frozenset(((0, 0, 0), (1, 0, 0), (2, 0, 0))) and SEED.issubset(TWO_CUBE_SET),
    )
    checks.check(
        "off-patch-zero",
        "every off-patch neighbor contributes occupancy 0",
        occupancy((-1, 0, 0), SEED) == 0 and occupancy((0, -1, 0), SEED) == 0 and occupancy((3, 0, 0), SEED) == 0,
    )

    checks.check(
        "axis-type-reps",
        "declared orbit representatives have the stated (n_unbalanced, n_both, n_empty) types",
        axis_type(ORBIT_REPS["wt1"]) == (1, 0, 2)
        and axis_type(ORBIT_REPS["opp2"]) == (0, 1, 2)
        and axis_type(ORBIT_REPS["adj2"]) == (2, 0, 1)
        and axis_type(ORBIT_REPS["vertex3"]) == (3, 0, 0)
        and axis_type(ORBIT_REPS["mixed3"]) == (1, 1, 1)
        and axis_type(ORBIT_REPS["empty"]) == (0, 0, 3),
    )
    checks.check(
        "f-min-rule",
        "f_min is 1 exactly on nonempty n_both=0 configurations",
        f_min(ORBIT_REPS["wt1"]) == 1
        and f_min(ORBIT_REPS["adj2"]) == 1
        and f_min(ORBIT_REPS["vertex3"]) == 1
        and f_min(ORBIT_REPS["opp2"]) == 0
        and f_min(ORBIT_REPS["mixed3"]) == 0
        and f_min(ORBIT_REPS["empty"]) == 0
        and f_min(ORBIT_REPS["full"]) == 0,
    )
    checks.check(
        "f-l1-is-n-unbalanced",
        "f_L1 is the n≠0 (some-axis-unbalanced) map, not Hamming parity",
        f_l1(ORBIT_REPS["wt1"]) == 1
        and f_l1(ORBIT_REPS["mixed3"]) == 1
        and f_l1(ORBIT_REPS["opp2"]) == 0
        and f_l1(ORBIT_REPS["empty"]) == 0
        and f_l1((1, 0, 0, 0, 0, 0)) == 1
        and sum(ORBIT_REPS["opp2"]) % 2 == 0,
    )
    checks.check(
        "maps-distinct",
        "f_min and f_L1 disagree on mixed3, so they are distinct maps",
        f_min(ORBIT_REPS["mixed3"]) == 0 and f_l1(ORBIT_REPS["mixed3"]) == 1,
    )
    checks.check(
        "f-min-support",
        "f_min has support 26 on {0,1}^6",
        support_size(f_min) == 26,
        residual=support_size(f_min),
    )

    t_l1, locks_l1, hist_l1 = run_from_seed(SEED, f_l1)
    checks.check(
        "theorem-1-l1-line-fill",
        "f_L1 fills from S with history (3, 9, 12)",
        t_l1 == 2 and len(locks_l1) == 12 and hist_l1 == LINE_L1_HISTORY and locks_l1 == TWO_CUBE_SET,
        residual=(t_l1, len(locks_l1), hist_l1),
    )

    t_min, locks_min, hist_min = run_from_seed(SEED, f_min)
    fills = len(locks_min) == 12
    print(f"f_min_line_seed: T={t_min} locks_halt={len(locks_min)} history={hist_min} fills={fills}")
    checks.check(
        "theorem-2-halt-locks",
        "f_min from S reaches a fixed point with reported halt locks",
        t_min <= 12 and len(locks_min) == 12 and locks_min == TWO_CUBE_SET,
        residual=(t_min, len(locks_min)),
    )
    checks.check(
        "theorem-2-history",
        "f_min lock history from S is (3, 9, 12) and T=2",
        hist_min == (3, 9, 12) and t_min == 2,
        residual=(t_min, hist_min),
    )
    checks.check(
        "theorem-2-fills",
        "f_min does fill from the 3-site long-axis seed",
        fills and "|locks_halt|=12" in note and "does fill" in note,
    )

    first_wave = step(SEED, f_min) - SEED
    expected_first_wave = frozenset(
        {
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0),
            (1, 0, 1),
            (2, 1, 0),
            (2, 0, 1),
        }
    )
    checks.check(
        "first-wave",
        "the first f_min wave from S is the six long-axis y/z neighbors",
        first_wave == expected_first_wave and len(SEED | first_wave) == 9,
        residual=sorted(first_wave),
    )

    appearing = set()
    locks = SEED
    while True:
        for site in TWO_CUBE:
            if site not in locks:
                appearing.add(axis_type(neighbor_config(site, locks)))
        nxt = step(locks, f_min)
        if nxt == locks:
            break
        locks = nxt
    checks.check(
        "no-mixed3-on-this-seed",
        "mixed3 never appears as an unlocking config from S, so the maps agree on the executed path",
        (1, 1, 1) not in appearing and (0, 1, 2) not in appearing,
        residual=sorted(appearing),
    )

    t_one, _locks_one, hist_one = run_from_seed(frozenset({(0, 0, 0)}), f_l1)
    checks.check(
        "mutation-one-site-seed",
        "the 1-site f_L1 history is (1, 4, 8, 11, 12), so this line-seed map is not that leftover",
        t_one == 4 and hist_one == ONE_SITE_L1_HISTORY and hist_one != hist_min,
    )

    checks.check(
        "theorem-3-comparison",
        "the note displays the f_min versus f_L1 comparison without adopting f_min",
        hist_min == hist_l1
        and "same lock history" in normalize(note)
        and "Displayed, not adopted" in note
        and "not written into Admissibility" in normalize(note)
        and "Do not adopt" in note,
    )

    forbidden = (
        "new axiom",
        "Block 12",
        "toe-lphys",
    )
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        'hypothetical_axiom_status: "no edit"',
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "does fill",
        "(3, 9, 12)",
        "3-site long-axis seed",
    )
    checks.check(
        "note-contract",
        "machine fields, fill statement, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(f"### N{i}" in note for i in range(1, 9))
        and not any(phrase in note for phrase in forbidden)
        and "promoted" not in note.lower()
        and "adopt f_min" in note.lower(),
    )

    print("per_element: axis-type representatives and off-patch occupancy 0 are enumerated")
    print("per_site: each two-cube vertex is tested against the displayed lock predicate")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: the twelve-vertex two-cube is executed from the long-axis seed")
    print("lattice_wide: checked and not executed — f_min is not adopted as an admissibility rule")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
