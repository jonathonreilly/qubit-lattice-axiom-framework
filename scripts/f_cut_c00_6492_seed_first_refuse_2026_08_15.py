#!/usr/bin/env python3
"""First refused neighborhood of F_cut (1,0,0,0,0) on the #6492 seed.

Two-cube, off-patch occupancy 0. Seed S={(0,0,0),(1,1,1),(2,0,0)}.
f00 is the F_cut remaining-bit map (1,0,0,0,0): fire only on wt1 and wt5.
f_L1 is the some-axis-unbalanced (n!=0) map, not Hamming parity.
The first refuse is displayed, not adopted.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_C00_6492_SEED_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_C00_6492_SEED_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]

SITES: tuple[Point, ...] = tuple(
    sorted((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
)
TWO_CUBE_SET = frozenset(SITES)
AXIS_SHIFTS: tuple[tuple[Point, Point], ...] = (
    ((1, 0, 0), (-1, 0, 0)),
    ((0, 1, 0), (0, -1, 0)),
    ((0, 0, 1), (0, 0, -1)),
)
F00_TUPLE: tuple[int, ...] = (1, 0, 0, 0, 0)
L1_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 1)
SEED: tuple[Point, ...] = ((0, 0, 0), (1, 1, 1), (2, 0, 0))
SEED_HISTORY = (3, 11)
LEFTOVER: Point = (1, 0, 0)
OPP2_CELL: Config = (1, 1, 0, 0, 0, 0)
ADJ4_CELL: Config = (1, 1, 1, 0, 1, 0)

ORBIT_REPS: dict[str, Config] = {
    "empty": (0, 0, 0, 0, 0, 0),
    "wt1": (1, 0, 0, 0, 0, 0),
    "opp2": (1, 1, 0, 0, 0, 0),
    "adj2": (1, 0, 1, 0, 0, 0),
    "vertex3": (1, 0, 1, 0, 1, 0),
    "mixed3": (1, 0, 1, 1, 0, 0),
    "type210": (1, 1, 1, 0, 0, 1),
    "wt5": (1, 1, 1, 1, 1, 0),
    "full": (1, 1, 1, 1, 1, 1),
}
BIT_NAMES: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
CLAIM_SCOPE = (
    "On the two-cube with off-patch o=0, the first refused neighborhood of "
    "F_cut (1,0,0,0,0) on the #6492 seed {(0,0,0),(1,1,1),(2,0,0)} is "
    "reported. Displayed, not adopted."
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def occupancy(site: Point, locks: frozenset[Point]) -> int:
    if site not in TWO_CUBE_SET:
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


def orbit_name(config: Config) -> str:
    kind = axis_type(config)
    names = {
        (0, 0, 3): "empty",
        (1, 0, 2): "wt1",
        (0, 1, 2): "opp2",
        (2, 0, 1): "adj2",
        (3, 0, 0): "vertex3",
        (1, 1, 1): "mixed3",
        (2, 1, 0): "adj4",
        (0, 2, 1): "opp4",
        (1, 2, 0): "wt5",
        (0, 3, 0): "full",
    }
    return names[kind]


def remaining_bit(config: Config) -> str | None:
    name = orbit_name(config)
    pairing = {
        "wt1": "wt1",
        "wt5": "wt1",
        "opp2": "opp2",
        "opp4": "opp2",
        "adj2": "adj2",
        "adj4": "adj2",
        "vertex3": "vertex3",
        "mixed3": "mixed3",
    }
    return pairing.get(name)


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    n_unbalanced, _n_both, _n_empty = axis_type(config)
    return 1 if n_unbalanced >= 1 else 0


def f00(config: Config) -> int:
    """F_cut remaining bits (1,0,0,0,0): fire only on wt1 and wt5."""
    kind = axis_type(config)
    return 1 if kind in ((1, 0, 2), (1, 2, 0)) else 0


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def remaining_tuple(predicate) -> tuple[int, ...]:
    return tuple(int(predicate(ORBIT_REPS[name]) == 1) for name in BIT_NAMES)


def step(locks: frozenset[Point], predicate) -> frozenset[Point]:
    newcomers = {
        site
        for site in SITES
        if site not in locks and predicate(neighbor_config(site, locks)) == 1
    }
    return locks | newcomers


def run_from_seed(seed: frozenset[Point], predicate, halt_bound: int = 12):
    locks = frozenset(seed)
    history = [len(locks)]
    layers = [locks]
    tick = 0
    while tick < halt_bound:
        nxt = step(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        tick += 1
        history.append(len(locks))
        layers.append(locks)
    return tick, frozenset(locks), tuple(history), tuple(layers)


def refuse_events(seed: frozenset[Point], predicate, halt_bound: int = 12):
    locks = frozenset(seed)
    events = []
    fires = []
    tick = 0
    while True:
        for site in SITES:
            if site in locks:
                continue
            config = neighbor_config(site, locks)
            bit = remaining_bit(config)
            record = (
                tick,
                site,
                orbit_name(config),
                axis_type(config),
                bit,
                config,
            )
            if predicate(config) == 1:
                fires.append(record)
            else:
                events.append(record)
        if tick >= halt_bound:
            break
        nxt = step(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        tick += 1
    return tuple(events), tuple(fires)


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
    self_source = Path(__file__).read_text(encoding="utf-8")
    compact_note = note.replace(" ", "")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the live axiom memo; no other scientific inputs")
    print("construction: displayed F_cut occupancy-to-lock map; first refuse on the #6492 seed")
    print("negative_scope: neither the map nor the refused remaining bit is adopted or written into Admissibility")
    print("cache_write: false")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_C00_6492_SEED_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_C00_6492_SEED_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
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

    checks.check(
        "two-cube-and-lex-order",
        "the two-cube has twelve lexicographically ordered vertices",
        len(SITES) == 12
        and SITES == tuple(sorted(SITES))
        and SITES[0] == (0, 0, 0)
        and SITES[-1] == (2, 1, 1)
        and TWO_CUBE_SET == frozenset(SITES),
    )
    checks.check(
        "off-patch-zero",
        "every off-patch neighbor contributes occupancy 0",
        occupancy((-1, 0, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((0, -1, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((3, 0, 0), frozenset({(2, 0, 0)})) == 0,
    )
    checks.check(
        "axis-type-reps",
        "declared orbit representatives have the stated axis types",
        axis_type(ORBIT_REPS["wt1"]) == (1, 0, 2)
        and axis_type(ORBIT_REPS["opp2"]) == (0, 1, 2)
        and axis_type(ORBIT_REPS["adj2"]) == (2, 0, 1)
        and axis_type(ORBIT_REPS["vertex3"]) == (3, 0, 0)
        and axis_type(ORBIT_REPS["mixed3"]) == (1, 1, 1)
        and axis_type(ORBIT_REPS["type210"]) == (2, 1, 0)
        and axis_type(ORBIT_REPS["empty"]) == (0, 0, 3)
        and axis_type(ORBIT_REPS["wt5"]) == (1, 2, 0)
        and axis_type(ORBIT_REPS["full"]) == (0, 3, 0)
        and orbit_name(OPP2_CELL) == "opp2"
        and orbit_name(ADJ4_CELL) == "adj4"
        and remaining_bit(OPP2_CELL) == "opp2"
        and remaining_bit(ADJ4_CELL) == "adj2",
    )

    f00_bits = remaining_tuple(f00)
    l1_bits = remaining_tuple(f_L1)
    checks.check(
        "f00-remaining-bits",
        "f00 is the F_cut remaining-bit tuple (1,0,0,0,0)",
        f00_bits == F00_TUPLE
        and l1_bits == L1_TUPLE
        and f00(ORBIT_REPS["wt1"]) == 1
        and f00(ORBIT_REPS["wt5"]) == 1
        and f00(ORBIT_REPS["opp2"]) == 0
        and f00(ORBIT_REPS["adj2"]) == 0
        and f00(ORBIT_REPS["vertex3"]) == 0
        and f00(ORBIT_REPS["mixed3"]) == 0
        and f00(ORBIT_REPS["type210"]) == 0
        and f00(ORBIT_REPS["empty"]) == 0
        and f00(ORBIT_REPS["full"]) == 0,
    )
    checks.check(
        "f-l1-is-n-unbalanced",
        "f_L1 is the n!=0 (some-axis-unbalanced) map, not Hamming parity",
        f_L1(ORBIT_REPS["wt1"]) == 1
        and f_L1(ORBIT_REPS["mixed3"]) == 1
        and f_L1(ORBIT_REPS["type210"]) == 1
        and f_L1(ORBIT_REPS["opp2"]) == 0
        and f_L1(ORBIT_REPS["empty"]) == 0
        and f_L1(ORBIT_REPS["adj2"]) != f_hamming(ORBIT_REPS["adj2"])
        and sum(ORBIT_REPS["opp2"]) % 2 == 0
        and "sum(config) % 2"
        not in self_source.split("def f_L1", 1)[1].split("def f00", 1)[0],
    )

    seed0 = frozenset(SEED)
    tick, locks, history, layers = run_from_seed(seed0, f00)
    refuses, fires = refuse_events(seed0, f00)
    first = refuses[0] if refuses else None
    tick0_fires = tuple(event for event in fires if event[0] == 0)
    tick0_refuses = tuple(event for event in refuses if event[0] == 0)
    later_adj4 = tuple(
        event
        for event in refuses
        if event[0] == 1 and event[1] == LEFTOVER and event[2] == "adj4"
    )
    print(f"history={history} T={tick} fill={locks == TWO_CUBE_SET}")
    print(f"first_refuse={first}")
    print(f"n_refuse={len(refuses)} n_fire={len(fires)} tick0_fires={len(tick0_fires)}")

    checks.check(
        "theorem-1-no-fill",
        "f00 has history (3, 11) from S and does not fill",
        tick == 1
        and history == SEED_HISTORY
        and locks == TWO_CUBE_SET - {LEFTOVER}
        and locks != TWO_CUBE_SET
        and history[-1] < 12
        and "(3, 11)" in note
        and "{(0,0,0),(1,1,1),(2,0,0)}" in compact_note
        and "does not fill" in note,
        residual=(tick, history, len(locks)),
    )
    checks.check(
        "theorem-2-fires-remaining-bit",
        "the run fires the wt1 remaining-bit orbit after the seed",
        len(tick0_fires) == 8
        and all(event[2] == "wt1" and event[4] == "wt1" for event in tick0_fires)
        and all(event[3] == (1, 0, 2) for event in tick0_fires)
        and "does fire a remaining-bit orbit after the seed" in note
        and "never fires a remaining-bit orbit after the seed" in note,
    )
    checks.check(
        "theorem-2-first-refuse",
        "the lex-first refuse is opp2 at tick 0 on (1,0,0)",
        first is not None
        and first[0] == 0
        and first[1] == LEFTOVER
        and first[2] == "opp2"
        and first[3] == (0, 1, 2)
        and first[4] == "opp2"
        and first[5] == OPP2_CELL
        and len(tick0_refuses) == 1
        and tick0_refuses[0] == first
        and neighbor_config(LEFTOVER, seed0) == OPP2_CELL
        and f00(OPP2_CELL) == 0
        and "`opp2`" in note
        and "(1,0,0)" in compact_note
        and "(1,1,0,0,0,0)" in compact_note
        and "(0,1,2)" in compact_note,
        residual=first,
    )
    checks.check(
        "theorem-2-later-adj4",
        "the leftover site later sees adj4 / adj2, which is not first",
        later_adj4 != ()
        and later_adj4[0][5] == ADJ4_CELL
        and later_adj4[0][3] == (2, 1, 0)
        and later_adj4[0][4] == "adj2"
        and neighbor_config(LEFTOVER, layers[1]) == ADJ4_CELL
        and f00(ADJ4_CELL) == 0
        and "adj4" in note
        and "not first" in note,
    )
    checks.check(
        "theorem-3-display-not-adopt",
        "the note displays the refuse and refuses adoption of a bit",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not adopt `opp2`" in note
        and "not written into Admissibility" in normalize(note)
        and "Do not write" in note,
    )

    checks.check(
        "mutation-hamming-is-not-l1",
        "Hamming parity is a different predicate from n!=0 and from f00",
        remaining_tuple(f_hamming) != L1_TUPLE
        and remaining_tuple(f_hamming) != F00_TUPLE
        and f_hamming(ORBIT_REPS["adj2"]) == 0
        and f_L1(ORBIT_REPS["adj2"]) == 1,
    )
    checks.check(
        "mutation-swap-fill-fails",
        "the swapped claim that f00 fills S is false",
        history != (3, 12) and len(locks) != 12,
    )

    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        'hypothetical_axiom_status: "no edit"',
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
        "(3, 11)",
        "(1, 0, 0, 0, 0)",
        "first refused neighborhood",
    )
    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")

    checks.check(
        "claim-scope",
        "claim_scope reports the first refuse on the #6492 seed and does not adopt it",
        CLAIM_SCOPE in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note.lower(),
    )
    checks.check(
        "note-contract",
        "machine fields, first-refuse statement, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(f"### N{index}" in note for index in range(1, 9))
        and all(phrase not in note and phrase not in self_source for phrase in forbidden)
        and "promoted" not in note.lower()
        and "new axiom" not in note
        and "Block 12" not in note
        and "toe-lphys" not in note
        and "citation" not in note.lower()
        and "runner-cache" not in note
        and "retained" not in other_retained,
    )
    checks.check(
        "not-leftover",
        "the residual is the first refuse, not L1-miss-why or a named-pair fill",
        "Not leftover-character of L1-miss-why" in note
        and "Not leftover-character of `#6492`" in note
        and "not a second named-pair fill" in note
        and "New finite object" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in normalize(note)
        and "not Hamming" in note
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "off-patch-declared",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "axiom-unedited",
        "the axiom memo still carries the four named premises and no F_cut map",
        "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Admissibility / Local Constraint" in axiom
        and "### Record / Fixed Reality" in axiom
        and "F_cut" not in axiom
        and "f_L1" not in axiom
        and "f00" not in axiom,
    )

    print("per_element: axis-type representatives and off-patch occupancy 0 are enumerated")
    print("per_site: each two-cube vertex is tested against the displayed lock predicate")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: the displayed seed is executed to a fixed point")
    print("lattice_wide: checked and not executed — neither the map nor a bit is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
