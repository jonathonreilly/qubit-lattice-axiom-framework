#!/usr/bin/env python3
"""Lex-first |S|<=3 seed where F_cut f1 fills and its wt1=0 sibling does not.

Two-cube {0,1,2}x{0,1}x{0,1}, off-patch occupancy 0. Remaining-bit order
is (wt1, opp2, adj2, vertex3, mixed3). f1=(1,1,1,1,1) and
fwt=(0,1,1,1,1). Seeds are enumerated by increasing size, then
lexicographic site order. f_L1 is the some-axis-unbalanced (n!=0) map,
not Hamming parity. The first split is displayed, not adopted.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "F_CUT_WT1_ZERO_F1_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_WT1_ZERO_F1_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
OrbitType = tuple[int, int, int]

SITES: tuple[Point, ...] = tuple(
    sorted((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
)
TWO_CUBE_SET = frozenset(SITES)
AXIS_SHIFTS: tuple[tuple[Point, Point], ...] = (
    ((1, 0, 0), (-1, 0, 0)),
    ((0, 1, 0), (0, -1, 0)),
    ((0, 0, 1), (0, 0, -1)),
)
REMAINING_ORDER: tuple[OrbitType, ...] = (
    (1, 0, 2),
    (0, 1, 2),
    (2, 0, 1),
    (3, 0, 0),
    (1, 1, 1),
)
F1_BITS: tuple[int, ...] = (1, 1, 1, 1, 1)
FWT_BITS: tuple[int, ...] = (0, 1, 1, 1, 1)
F0_BITS: tuple[int, ...] = (1, 1, 1, 1, 0)
L1_BITS: tuple[int, ...] = (1, 0, 1, 1, 1)
EMPTY_TYPE: OrbitType = (0, 0, 3)
FULL_TYPE: OrbitType = (0, 3, 0)
WT1_TYPE: OrbitType = (1, 0, 2)
WT1_COMPLEMENT: OrbitType = (1, 2, 0)
MAX_SEED = 3
TWO_SITE_COUNT = 66

ORBIT_REPS: dict[str, Config] = {
    "empty": (0, 0, 0, 0, 0, 0),
    "wt1": (1, 0, 0, 0, 0, 0),
    "opp2": (1, 1, 0, 0, 0, 0),
    "adj2": (1, 0, 1, 0, 0, 0),
    "vertex3": (1, 0, 1, 0, 1, 0),
    "mixed3": (1, 0, 1, 1, 0, 0),
    "type120": (1, 0, 1, 1, 1, 1),
    "full": (1, 1, 1, 1, 1, 1),
}


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


def axis_type(config: Config) -> OrbitType:
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


def remaining_value(bits: tuple[int, ...], kind: OrbitType) -> int:
    if kind in (EMPTY_TYPE, FULL_TYPE):
        return 0
    lookup = {
        (1, 0, 2): bits[0],
        (1, 2, 0): bits[0],
        (0, 1, 2): bits[1],
        (0, 2, 1): bits[1],
        (2, 0, 1): bits[2],
        (2, 1, 0): bits[2],
        (3, 0, 0): bits[3],
        (1, 1, 1): bits[4],
    }
    return lookup[kind]


def predicate_from_remaining(bits: tuple[int, ...]):
    def predicate(config: Config) -> int:
        return remaining_value(bits, axis_type(config))

    return predicate


f1 = predicate_from_remaining(F1_BITS)
fwt = predicate_from_remaining(FWT_BITS)
f0 = predicate_from_remaining(F0_BITS)
f_l1 = predicate_from_remaining(L1_BITS)


def f_hamming(config: Config) -> int:
    return sum(config) % 2


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


def fills(seed: frozenset[Point], predicate) -> bool:
    _tick, locks, _history = run_from_seed(seed, predicate)
    return len(locks) == 12


def seed_family():
    for size in range(1, MAX_SEED + 1):
        for combo in combinations(SITES, size):
            yield combo


def first_split():
    for combo in seed_family():
        seed = frozenset(combo)
        if fills(seed, f1) and not fills(seed, fwt):
            t1, locks1, hist1 = run_from_seed(seed, f1)
            tw, locksw, histw = run_from_seed(seed, fwt)
            return {
                "seed": combo,
                "hist_f1": hist1,
                "fill_f1": len(locks1) == 12,
                "locks_f1": locks1,
                "tick_f1": t1,
                "hist_fwt": histw,
                "fill_fwt": len(locksw) == 12,
                "locks_fwt": locksw,
                "tick_fwt": tw,
            }
    return None


def coverage_two_site(predicate) -> int:
    return sum(1 for pair in combinations(SITES, 2) if fills(frozenset(pair), predicate))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
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
    note_flat = normalize(note)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice, Admissibility, and Record "
        "boundaries; no observations or fits"
    )
    print("negative_scope: neither map nor the first seed is adopted")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_WT1_ZERO_F1_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_WT1_ZERO_F1_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in self_source,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_boundary = "does not supply the formation site, probability, or rate"
    record_lock = "When present, a record locks exactly one admissible local possibility."
    unread = "A site with no record cannot be read."
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
        formation_boundary in normalize(axiom) and formation_boundary in note_flat,
    )
    checks.check(
        "source-record-and-non-dynamics",
        "Record lock wording and the non-dynamics Admissibility boundary are pinned",
        record_lock in normalize(axiom)
        and record_lock in note
        and unread in axiom
        and unread in note
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
        and len(list(combinations(SITES, 2))) == TWO_SITE_COUNT
        and len(list(combinations(SITES, 3))) == 220,
    )
    checks.check(
        "off-patch-zero",
        "every off-patch neighbor contributes occupancy 0",
        occupancy((-1, 0, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((0, -1, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((3, 0, 0), frozenset({(2, 0, 0)})) == 0,
    )
    checks.check(
        "remaining-bits-and-maps",
        "f1 and fwt are the declared remaining-bit F_cut maps",
        axis_type(ORBIT_REPS["wt1"]) == (1, 0, 2)
        and axis_type(ORBIT_REPS["opp2"]) == (0, 1, 2)
        and axis_type(ORBIT_REPS["adj2"]) == (2, 0, 1)
        and axis_type(ORBIT_REPS["vertex3"]) == (3, 0, 0)
        and axis_type(ORBIT_REPS["mixed3"]) == (1, 1, 1)
        and axis_type(ORBIT_REPS["type120"]) == (1, 2, 0)
        and remaining_value(F1_BITS, WT1_TYPE) == 1
        and remaining_value(FWT_BITS, WT1_TYPE) == 0
        and remaining_value(FWT_BITS, WT1_COMPLEMENT) == 0
        and remaining_value(F1_BITS, (0, 1, 2)) == 1
        and remaining_value(FWT_BITS, (0, 1, 2)) == 1
        and f1(ORBIT_REPS["empty"]) == 0
        and f1(ORBIT_REPS["full"]) == 0
        and fwt(ORBIT_REPS["empty"]) == 0
        and fwt(ORBIT_REPS["full"]) == 0
        and f1(ORBIT_REPS["wt1"]) == 1
        and fwt(ORBIT_REPS["wt1"]) == 0
        and f_l1(ORBIT_REPS["opp2"]) == 0
        and f1(ORBIT_REPS["opp2"]) == 1,
    )
    checks.check(
        "f1-not-l1-not-hamming",
        "f1 is not f_L1 and neither is Hamming parity",
        F1_BITS != L1_BITS
        and FWT_BITS != L1_BITS
        and f1(ORBIT_REPS["opp2"]) != f_l1(ORBIT_REPS["opp2"])
        and f1(ORBIT_REPS["adj2"]) != f_hamming(ORBIT_REPS["adj2"])
        and f_l1(ORBIT_REPS["wt1"]) == 1
        and f_l1(ORBIT_REPS["opp2"]) == 0
        and "sum(config) % 2"
        not in self_source.split("def remaining_value", 1)[0],
    )

    cov2_f1 = coverage_two_site(f1)
    cov2_fwt = coverage_two_site(fwt)
    cov2_f0 = coverage_two_site(f0)
    print(f"cov2_f1={cov2_f1} cov2_fwt={cov2_fwt} cov2_f0={cov2_f0}")

    checks.check(
        "thm1-f1-fills-every-2-site",
        "f1 fills every 2-site seed",
        cov2_f1 == TWO_SITE_COUNT,
        residual=cov2_f1,
    )
    checks.check(
        "thm1-fwt-not-in-max2",
        "fwt is not in Max(2), because cov2(fwt) is strictly below cov2(f1)",
        cov2_fwt < cov2_f1
        and cov2_f1 == TWO_SITE_COUNT
        and cov2_f0 == TWO_SITE_COUNT
        and FWT_BITS != F0_BITS
        and FWT_BITS != F1_BITS,
        residual=cov2_fwt,
    )

    first = first_split()
    if first is None:
        print("first_split: none")
    else:
        print(
            f"first_split seed={first['seed']} "
            f"hist_f1={first['hist_f1']} fill_f1={first['fill_f1']} "
            f"hist_fwt={first['hist_fwt']} fill_fwt={first['fill_fwt']}"
        )

    checks.check(
        "thm2-lex-first-seed",
        "the lex-first |S|<=3 seed where f1 fills and fwt does not is {(0,0,0)}",
        first is not None
        and first["seed"] == ((0, 0, 0),)
        and "{(0,0,0)}" in note.replace(" ", ""),
        residual=None if first is None else first["seed"],
    )

    seed0 = frozenset({(0, 0, 0)})
    wave_f1 = step(seed0, f1) - seed0
    wave_fwt = step(seed0, fwt) - seed0
    expected_wave = frozenset({(1, 0, 0), (0, 1, 0), (0, 0, 1)})
    checks.check(
        "thm3-histories",
        "from {(0,0,0)} f1 has history (1, 4, 8, 11, 12) and fills; fwt has (1,) and does not",
        first is not None
        and first["hist_f1"] == (1, 4, 8, 11, 12)
        and first["fill_f1"]
        and first["locks_f1"] == TWO_CUBE_SET
        and first["hist_fwt"] == (1,)
        and not first["fill_fwt"]
        and first["locks_fwt"] == seed0
        and "(1, 4, 8, 11, 12)" in note
        and "(1,)" in note,
        residual=None
        if first is None
        else (first["hist_f1"], first["hist_fwt"], first["fill_f1"], first["fill_fwt"]),
    )
    checks.check(
        "split-mechanism",
        "the first wave from {(0,0,0)} is type wt1; f1 locks it and fwt is silent",
        wave_f1 == expected_wave
        and wave_fwt == frozenset()
        and all(
            axis_type(neighbor_config(site, seed0)) == WT1_TYPE
            for site in expected_wave
        )
        and f1(ORBIT_REPS["wt1"]) == 1
        and fwt(ORBIT_REPS["wt1"]) == 0,
        residual=(sorted(wave_f1), sorted(wave_fwt)),
    )
    checks.check(
        "theorem-3-display-not-adopt",
        "the note displays the seed and refuses adoption of wt1",
        first is not None
        and "Displayed, not adopted" in note
        and "Do not adopt" in note
        and "not written into Admissibility" in note_flat
        and "wt1" in note,
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
        "No-Go Discipline disposition: **PASS**",
        "(1, 4, 8, 11, 12)",
        "lex-first seed",
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
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "not Hamming" in note
        and "n≠0" in note,
    )
    checks.check(
        "not-leftover-opp2-zero",
        "the pair is new, not leftover of the opp2=0 wt1=0 split",
        "Not leftover" in note
        and "opp2=0" in note
        and "(0,1,1,1,1)" in note.replace(" ", ""),
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        'hypothetical_axiom_status: "no edit"' in note
        and "no axiom or approved primitive is added" in note,
    )

    print("per_element: remaining-bit representatives and off-patch occupancy 0 are enumerated")
    print("per_site: each two-cube vertex is tested against both displayed lock predicates")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: every 2-site seed and the lex |S|<=3 search are executed to a fixed point")
    print("lattice_wide: checked and not executed — neither map nor the seed is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
