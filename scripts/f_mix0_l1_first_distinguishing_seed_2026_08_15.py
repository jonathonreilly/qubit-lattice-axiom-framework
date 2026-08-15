#!/usr/bin/env python3
"""First |S|<=3 two-cube seed where f_mix0 and f_L1 disagree.

Enumerate nonempty seeds of the twelve-vertex two-cube by increasing
cardinality, then lexicographic site order, through |S|=3.  A run is the
lock-history tuple until halt together with the fill bit |locks_halt|=12.
Off-patch occupancy is 0.  f_L1 is the some-axis-unbalanced (n!=0) map,
not Hamming parity.  f_mix0 is the F_cut remaining-bit map (1,0,1,1,0):
L1 with mixed3=0.  The distinguishing seed is displayed, not adopted.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_MIX0_L1_FIRST_DISTINGUISHING_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_MIX0_L1_FIRST_DISTINGUISHING_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
ONE_SITE: tuple[Point, ...] = ((0, 0, 0),)
FACE_DIAG: tuple[Point, ...] = ((0, 0, 0), (1, 1, 0))
OPP_CORNER: tuple[Point, ...] = ((0, 0, 0), (2, 1, 1))
FIRST_SEED: tuple[Point, ...] = ((0, 0, 0), (0, 0, 1), (2, 0, 0))
ONE_SITE_HISTORY = (1, 4, 8, 11, 12)
FACE_DIAG_HISTORY = (2, 7, 11, 12)
OPP_CORNER_HISTORY = (2, 8, 12)
L1_FIRST_HISTORY = (3, 8, 11, 12)
MIX0_FIRST_HISTORY = (3, 8, 10)
MIX0_TUPLE = (1, 0, 1, 1, 0)
L1_TUPLE = (1, 0, 1, 1, 1)
MAX_SEED = 3
CENSUS_COUNTS = {1: 12, 2: 66, 3: 220}

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


def f_L1(config: Config) -> int:
    """1 iff some axis is unbalanced: n_mu != 0.  Not Hamming parity."""
    n_unbalanced, _n_both, _n_empty = axis_type(config)
    return 1 if n_unbalanced >= 1 else 0


def f_mix0(config: Config) -> int:
    """F_cut remaining bits (1,0,1,1,0): L1 with mixed3 silenced."""
    n_unbalanced, n_both, n_empty = axis_type(config)
    if n_unbalanced == 1 and n_both == 1 and n_empty == 1:
        return 0
    return 1 if n_unbalanced >= 1 else 0


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
    tick = 0
    while tick < halt_bound:
        nxt = step(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        tick += 1
        history.append(len(locks))
    return tick, frozenset(locks), tuple(history)


def seed_family():
    for size in range(1, MAX_SEED + 1):
        for combo in combinations(SITES, size):
            yield combo


def first_disagreement():
    n_total = 0
    n_agree = 0
    specials = {}
    first = None
    for combo in seed_family():
        n_total += 1
        seed = frozenset(combo)
        _t_l1, locks_l1, hist_l1 = run_from_seed(seed, f_L1)
        _t_mix, locks_mix, hist_mix = run_from_seed(seed, f_mix0)
        fill_l1 = len(locks_l1) == 12
        fill_mix = len(locks_mix) == 12
        same = hist_l1 == hist_mix and fill_l1 == fill_mix
        record = {
            "seed": combo,
            "hist_l1": hist_l1,
            "fill_l1": fill_l1,
            "hist_mix": hist_mix,
            "fill_mix": fill_mix,
            "locks_l1": locks_l1,
            "locks_mix": locks_mix,
        }
        if combo in (ONE_SITE, FACE_DIAG, OPP_CORNER, FIRST_SEED):
            specials[combo] = record
        if same:
            n_agree += 1
        elif first is None:
            first = record
    return {
        "n_total": n_total,
        "n_agree": n_agree,
        "n_disagree": n_total - n_agree,
        "specials": specials,
        "first": first,
    }


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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the live axiom memo; no other scientific inputs")
    print("construction: displayed cube-covariant occupancy-to-lock maps; seed census on the twelve-vertex two-cube")
    print("negative_scope: neither map nor the distinguishing seed is adopted or written into Admissibility")
    print("cache_write: false")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIX0_L1_FIRST_DISTINGUISHING_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_MIX0_L1_FIRST_DISTINGUISHING_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "census-cardinality",
        "nonempty seeds of size at most 3 number 12+66+220=298",
        all(len(list(combinations(SITES, size))) == count for size, count in CENSUS_COUNTS.items())
        and sum(CENSUS_COUNTS.values()) == 298,
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
        and axis_type(ORBIT_REPS["wt5"]) == (1, 2, 0),
    )
    mix0_bits = remaining_tuple(f_mix0)
    l1_bits = remaining_tuple(f_L1)
    checks.check(
        "f-mix0-remaining-bits",
        "f_mix0 is the F_cut remaining-bit tuple (1,0,1,1,0)",
        mix0_bits == MIX0_TUPLE
        and l1_bits == L1_TUPLE
        and MIX0_TUPLE[4] == 0
        and L1_TUPLE[4] == 1
        and f_mix0(ORBIT_REPS["wt1"]) == 1
        and f_mix0(ORBIT_REPS["opp2"]) == 0
        and f_mix0(ORBIT_REPS["adj2"]) == 1
        and f_mix0(ORBIT_REPS["vertex3"]) == 1
        and f_mix0(ORBIT_REPS["mixed3"]) == 0
        and f_mix0(ORBIT_REPS["type210"]) == 1
        and f_mix0(ORBIT_REPS["empty"]) == 0
        and f_mix0(ORBIT_REPS["full"]) == 0
        and f_mix0(ORBIT_REPS["wt5"]) == 1,
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
        not in self_source.split("def f_L1", 1)[1].split("def f_mix0", 1)[0],
    )
    checks.check(
        "maps-distinct-on-mixed3",
        "f_mix0 and f_L1 disagree on mixed3, so they are distinct maps",
        f_mix0(ORBIT_REPS["mixed3"]) == 0 and f_L1(ORBIT_REPS["mixed3"]) == 1,
    )

    census = first_disagreement()
    first = census["first"]
    specials = census["specials"]
    print(
        f"census: n_total={census['n_total']} n_agree={census['n_agree']} "
        f"n_disagree={census['n_disagree']}"
    )
    if first is None:
        print("first_distinguishing_seed: none")
    else:
        print(
            f"first_distinguishing_seed={first['seed']} "
            f"hist_L1={first['hist_l1']} fill_L1={first['fill_l1']} "
            f"hist_mix0={first['hist_mix']} fill_mix0={first['fill_mix']}"
        )

    one = specials.get(ONE_SITE)
    face = specials.get(FACE_DIAG)
    opp = specials.get(OPP_CORNER)
    checks.check(
        "theorem-1-named-seeds-agree",
        "the maps agree on {(0,0,0)}, the face-diagonal, and opposite-corner S*",
        one is not None
        and face is not None
        and opp is not None
        and one["hist_l1"] == one["hist_mix"] == ONE_SITE_HISTORY
        and one["fill_l1"]
        and one["fill_mix"]
        and face["hist_l1"] == face["hist_mix"] == FACE_DIAG_HISTORY
        and face["fill_l1"]
        and face["fill_mix"]
        and opp["hist_l1"] == opp["hist_mix"] == OPP_CORNER_HISTORY
        and opp["fill_l1"]
        and opp["fill_mix"],
        residual=None
        if one is None or face is None or opp is None
        else (one["hist_l1"], face["hist_l1"], opp["hist_l1"]),
    )
    checks.check(
        "theorem-1-first-seed",
        "the first disagreement is the lex 3-site seed {(0,0,0),(0,0,1),(2,0,0)}",
        first is not None
        and first["seed"] == FIRST_SEED
        and census["n_total"] == 298
        and census["n_disagree"] >= 1
        and "{(0,0,0),(0,0,1),(2,0,0)}" in note.replace(" ", ""),
        residual=None if first is None else first["seed"],
    )
    checks.check(
        "size-at-most-two-agree",
        "every nonempty seed of size at most 2 has identical history and fill",
        census["n_total"] == 298
        and first is not None
        and len(first["seed"]) == 3
        and census["n_agree"] == 266
        and census["n_disagree"] == 32,
    )
    checks.check(
        "theorem-2-histories-and-fill",
        "on that seed f_L1 history (3, 8, 11, 12) fills and f_mix0 history (3, 8, 10) does not",
        first is not None
        and first["hist_l1"] == L1_FIRST_HISTORY
        and first["fill_l1"]
        and first["locks_l1"] == TWO_CUBE_SET
        and first["hist_mix"] == MIX0_FIRST_HISTORY
        and not first["fill_mix"]
        and len(first["locks_mix"]) == 10
        and "(3, 8, 11, 12)" in note
        and "(3, 8, 10)" in note,
        residual=None
        if first is None
        else (first["hist_l1"], first["hist_mix"], first["fill_l1"], first["fill_mix"]),
    )

    seed0 = frozenset(FIRST_SEED)
    wave1 = step(seed0, f_mix0) - seed0
    expected_wave1 = frozenset(
        {(0, 1, 0), (0, 1, 1), (1, 0, 1), (2, 0, 1), (2, 1, 0)}
    )
    after1 = seed0 | expected_wave1
    mix_ready = {
        site
        for site in SITES
        if site not in after1 and f_mix0(neighbor_config(site, after1)) == 1
    }
    l1_ready = {
        site
        for site in SITES
        if site not in after1 and f_L1(neighbor_config(site, after1)) == 1
    }
    split_site = (1, 0, 0)
    checks.check(
        "split-mechanism",
        "the maps share the first wave and split on mixed3 at (1,0,0)",
        wave1 == expected_wave1
        and axis_type(neighbor_config(split_site, after1)) == (1, 1, 1)
        and axis_type(neighbor_config((1, 1, 1), after1)) == (2, 0, 1)
        and axis_type(neighbor_config((2, 1, 1), after1)) == (2, 0, 1)
        and axis_type(neighbor_config((1, 1, 0), after1)) == (0, 1, 2)
        and mix_ready == frozenset({(1, 1, 1), (2, 1, 1)})
        and l1_ready == mix_ready | {split_site}
        and f_mix0(ORBIT_REPS["mixed3"]) == 0
        and f_L1(ORBIT_REPS["mixed3"]) == 1,
        residual=(sorted(wave1), sorted(mix_ready), sorted(l1_ready)),
    )
    checks.check(
        "theorem-3-display-not-adopt",
        "the note displays the seed and refuses adoption of either map",
        first is not None
        and "Displayed, not adopted" in note
        and "not written into Admissibility" in normalize(note)
        and "Do not adopt" in note
        and "Do not write" in note,
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
        "(3, 8, 11, 12)",
        "(3, 8, 10)",
        "first nonempty seed",
        "(1,0,1,1,0)",
    )
    checks.check(
        "note-contract",
        "machine fields, first-seed statement, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(f"### N{index}" in note for index in range(1, 9))
        and all(phrase not in note and phrase not in self_source for phrase in forbidden)
        and "promoted" not in note.lower()
        and "new axiom" not in note
        and "Block 12" not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "not-leftover-or-clone",
        "the claim is a new seed census, not leftover f_min or cov=66 character",
        "Not leftover-character of #6417" in note
        and "Not leftover-character of #6431" in note
        and "f_min" in note
        and "cov=66" in note
        and "first 10" in note,
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

    print("per_element: axis-type representatives and off-patch occupancy 0 are enumerated")
    print("per_site: each two-cube vertex is tested against both displayed lock predicates")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: all 298 seeds of size at most 3 are executed to a fixed point")
    print("lattice_wide: checked and not executed — neither map nor the seed is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
