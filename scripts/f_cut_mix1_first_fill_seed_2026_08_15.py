#!/usr/bin/env python3
"""Lex-first two-cube seed that F_cut (1,0,0,0,1) fills.

Enumerate seeds of the twelve-vertex two-cube by increasing cardinality,
then lexicographic site order.  Dynamics are occupancy-to-lock with
off-patch occupancy 0.  f_mix1 is the F_cut remaining-bit map (1,0,0,0,1):
fire on wt1, its complement wt5, and mixed3.  f_L1 is the
some-axis-unbalanced (n!=0) map, not Hamming parity.  The first fill seed is
displayed, not adopted.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_MIX1_FIRST_FILL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_MIX1_FIRST_FILL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Config = tuple[int, int, int, int, int, int]
Bits = tuple[int, int, int, int, int]

SITES: tuple[Point, ...] = tuple(
    sorted((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
)
TWO_CUBE_SET = frozenset(SITES)
AXIS_SHIFTS: tuple[tuple[Point, Point], ...] = (
    ((1, 0, 0), (-1, 0, 0)),
    ((0, 1, 0), (0, -1, 0)),
    ((0, 0, 1), (0, 0, -1)),
)
MIX1_TUPLE: Bits = (1, 0, 0, 0, 1)
L1_TUPLE: Bits = (1, 0, 1, 1, 1)
FIRST_SEED: tuple[Point, ...] = ((0, 0, 0), (0, 0, 1))
FIRST_HISTORY = (2, 6, 8, 10, 12)
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
    "opp2c": (1, 1, 1, 1, 0, 0),
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


def f_mix1(config: Config) -> int:
    """F_cut remaining bits (1,0,0,0,1): wt1, mixed3, and the wt1 complement."""
    kind = axis_type(config)
    return 1 if kind in ((1, 0, 2), (1, 2, 0), (1, 1, 1)) else 0


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def remaining_tuple(predicate) -> Bits:
    return tuple(int(predicate(ORBIT_REPS[name]) == 1) for name in BIT_NAMES)  # type: ignore[return-value]


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


def fills(seed: tuple[Point, ...] | frozenset[Point], predicate=f_mix1) -> bool:
    _tick, locks, _history = run_from_seed(frozenset(seed), predicate)
    return len(locks) == 12


def coverage(size: int, predicate=f_mix1) -> tuple[int, int, tuple[Point, ...] | None]:
    n_total = 0
    n_fill = 0
    first: tuple[Point, ...] | None = None
    for combo in combinations(SITES, size):
        n_total += 1
        if fills(combo, predicate):
            n_fill += 1
            if first is None:
                first = combo
    return n_total, n_fill, first


def first_fill_seed(min_size: int = 1, max_size: int = 3):
    per_size = {}
    found = None
    for size in range(min_size, max_size + 1):
        n_total, n_fill, first = coverage(size)
        per_size[size] = {"n_total": n_total, "n_fill": n_fill, "first": first}
        if found is None and first is not None:
            found = first
    return found, per_size


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
    print("construction: displayed F_cut occupancy-to-lock map; lex first-fill seed on the twelve-vertex two-cube")
    print("negative_scope: neither the map nor the first-fill seed is adopted or written into Admissibility")
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
            "docs/F_CUT_MIX1_FIRST_FILL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_MIX1_FIRST_FILL_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "seed counts are C(12,k) for k=1..3",
        all(len(list(combinations(SITES, size))) == count for size, count in CENSUS_COUNTS.items()),
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
        and axis_type(ORBIT_REPS["opp2c"]) == (0, 2, 1)
        and axis_type(ORBIT_REPS["full"]) == (0, 3, 0),
    )

    mix1_bits = remaining_tuple(f_mix1)
    l1_bits = remaining_tuple(f_L1)
    checks.check(
        "f-mix1-remaining-bits",
        "f_mix1 is the F_cut remaining-bit tuple (1,0,0,0,1)",
        mix1_bits == MIX1_TUPLE
        and l1_bits == L1_TUPLE
        and f_mix1(ORBIT_REPS["wt1"]) == 1
        and f_mix1(ORBIT_REPS["wt5"]) == 1
        and f_mix1(ORBIT_REPS["mixed3"]) == 1
        and f_mix1(ORBIT_REPS["opp2"]) == 0
        and f_mix1(ORBIT_REPS["adj2"]) == 0
        and f_mix1(ORBIT_REPS["vertex3"]) == 0
        and f_mix1(ORBIT_REPS["type210"]) == 0
        and f_mix1(ORBIT_REPS["empty"]) == 0
        and f_mix1(ORBIT_REPS["full"]) == 0
        and f_mix1(ORBIT_REPS["opp2c"]) == 0,
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
        not in self_source.split("def f_L1", 1)[1].split("def f_mix1", 1)[0],
    )

    found, per_size = first_fill_seed()
    n_one, cov1, first_one = per_size[1]["n_total"], per_size[1]["n_fill"], per_size[1]["first"]
    n_two, cov2, first_two = per_size[2]["n_total"], per_size[2]["n_fill"], per_size[2]["first"]
    n_three, cov3, first_three = per_size[3]["n_total"], per_size[3]["n_fill"], per_size[3]["first"]
    print(f"cov1={cov1} n_one={n_one}")
    print(f"cov2={cov2} n_two={n_two}")
    print(f"cov3={cov3} n_three={n_three}")
    print(f"lex_first_fill={found}")

    checks.check(
        "theorem-1-coverages",
        "cov2=8, cov1=0, cov3=0 among the 12+66+220 seeds",
        n_one == 12
        and cov1 == 0
        and first_one is None
        and n_two == 66
        and cov2 == 8
        and n_three == 220
        and cov3 == 0
        and first_three is None
        and "cov2(f_mix1)=8" in note.replace(" ", "")
        and "cov1=0" in note
        and "cov3=0" in note,
        residual=(cov1, cov2, cov3),
    )
    checks.check(
        "theorem-2-lex-first-seed",
        "the lex-first fill is the size-2 edge {(0,0,0),(0,0,1)}",
        found == FIRST_SEED
        and len(found) == 2
        and first_two == FIRST_SEED
        and "{(0,0,0),(0,0,1)}" in note.replace(" ", "")
        and "|S|=2" in note.replace(" ", ""),
        residual=found,
    )

    tick, locks, history = run_from_seed(frozenset(FIRST_SEED), f_mix1)
    seed0 = frozenset(FIRST_SEED)
    after1 = step(seed0, f_mix1)
    wave1 = after1 - seed0
    after2 = step(after1, f_mix1)
    wave2 = after2 - after1
    after3 = step(after2, f_mix1)
    wave3 = after3 - after2
    after4 = step(after3, f_mix1)
    wave4 = after4 - after3
    expected_wave1 = frozenset({(0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)})
    expected_wave2 = frozenset({(2, 0, 0), (2, 0, 1)})
    expected_wave3 = frozenset({(2, 1, 0), (2, 1, 1)})
    expected_wave4 = frozenset({(1, 1, 0), (1, 1, 1)})
    print(f"history={history} T={tick} fill={locks == TWO_CUBE_SET}")

    checks.check(
        "theorem-3-history",
        "from that S the lock history is (2, 6, 8, 10, 12) and the run fills",
        tick == 4
        and history == FIRST_HISTORY
        and locks == TWO_CUBE_SET
        and fills(FIRST_SEED)
        and "(2, 6, 8, 10, 12)" in note,
        residual=(tick, history, len(locks)),
    )
    checks.check(
        "fill-mechanism-waves",
        "wt1 waves fill ten sites, then mixed3 locks the leftover middle pair",
        wave1 == expected_wave1
        and wave2 == expected_wave2
        and wave3 == expected_wave3
        and wave4 == expected_wave4
        and after4 == TWO_CUBE_SET
        and all(axis_type(neighbor_config(site, seed0)) == (1, 0, 2) for site in wave1)
        and all(axis_type(neighbor_config(site, after1)) == (1, 0, 2) for site in wave2)
        and all(axis_type(neighbor_config(site, after2)) == (1, 0, 2) for site in wave3)
        and all(axis_type(neighbor_config(site, after3)) == (1, 1, 1) for site in wave4)
        and all(f_mix1(neighbor_config(site, seed0)) == 1 for site in wave1)
        and all(f_mix1(neighbor_config(site, after3)) == 1 for site in wave4),
        residual=(sorted(wave1), sorted(wave2), sorted(wave3), sorted(wave4)),
    )
    checks.check(
        "theorem-3-display-not-adopt",
        "the note displays the seed and refuses adoption of a bit",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in normalize(note)
        and "Do not adopt a bit" in note
        and "Do not adopt" in note
        and "Do not write" in note,
    )

    claim_scope = (
        "On the two-cube with off-patch o=0, the lex-first seed that F_cut "
        "(1,0,0,0,1) fills is reported. Displayed, not adopted."
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
        "(2, 6, 8, 10, 12)",
        "(1, 0, 0, 0, 1)",
        "lex-first seed",
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
        "claim_scope reports the lex-first f_mix1 fill seed and does not adopt it",
        claim_scope in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note.lower(),
    )
    checks.check(
        "note-contract",
        "machine fields, first-fill statement, and forbidden-phrase hygiene hold",
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
        "not-leftover-6510",
        "the residual is the first-fill seed, not leftover coverage scores of #6510/#6502",
        "Not leftover-character of #6510" in note
        and "that scored `cov2=8`" in note
        and "Not leftover-character of #6502" in note
        and "New first fill of a newly named map" in note,
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
        and "f_mix1" not in axiom,
    )

    print("per_element: axis-type representatives and off-patch occupancy 0 are enumerated")
    print("per_site: each two-cube vertex is tested against the displayed lock predicate")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: all seeds of size 1 through 3 are executed to a fixed point")
    print("lattice_wide: checked and not executed — neither the map nor the seed is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
