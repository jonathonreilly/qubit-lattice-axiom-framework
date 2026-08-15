#!/usr/bin/env python3
"""First neighborhood where f_min and f_L1 disagree from S*.

Two independent occupancy-to-lock runs start from the displayed seed
S*={(0,0,0),(2,1,1)} on the twelve-vertex two-cube with off-patch
occupancy 0.  At each tick, both predicates are evaluated on every
unlocked site against that run's locked set.  The first (tick, site,
axis-type, 6-tuple) at which the predicates differ is displayed, not
adopted.  f_L1 is the some-axis-unbalanced (n!=0) map, not Hamming.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "F_MIN_L1_FIRST_DISAGREEING_NEIGHBORHOOD_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_MIN_L1_FIRST_DISAGREEING_NEIGHBORHOOD_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SEED: tuple[Point, ...] = ((0, 0, 0), (2, 1, 1))
SEED_SET = frozenset(SEED)
L1_HISTORY = (2, 8, 12)

ORBIT_REPS: dict[str, Config] = {
    "empty": (0, 0, 0, 0, 0, 0),
    "wt1": (1, 0, 0, 0, 0, 0),
    "opp2": (1, 1, 0, 0, 0, 0),
    "adj2": (1, 0, 1, 0, 0, 0),
    "vertex3": (1, 0, 1, 0, 1, 0),
    "mixed3": (1, 0, 1, 1, 0, 0),
    "type210": (1, 1, 1, 0, 0, 1),
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


def f_hamming(config: Config) -> int:
    return sum(config) % 2


def ready_sites(locks: frozenset[Point], predicate) -> frozenset[Point]:
    return frozenset(
        site
        for site in SITES
        if site not in locks and predicate(neighbor_config(site, locks)) == 1
    )


def disagreements(locks: frozenset[Point]) -> list[dict]:
    rows: list[dict] = []
    for site in SITES:
        if site in locks:
            continue
        config = neighbor_config(site, locks)
        value_min = f_min(config)
        value_l1 = f_l1(config)
        if value_min != value_l1:
            rows.append(
                {
                    "site": site,
                    "config": config,
                    "axis_type": axis_type(config),
                    "f_min": value_min,
                    "f_l1": value_l1,
                }
            )
    return rows


def run_from_seed(predicate, halt_bound: int = 12) -> dict:
    locks = frozenset(SEED_SET)
    history = [len(locks)]
    first = None
    tick = 0
    while tick < halt_bound:
        tick += 1
        split = disagreements(locks)
        if split and first is None:
            first = {"tick": tick, **split[0], "all": tuple(split)}
        nxt = locks | ready_sites(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        history.append(len(locks))
    return {
        "tick": tick if history[-1] != len(SEED_SET) or first is not None else 0,
        "halt_tick": len(history) - 1,
        "locks": frozenset(locks),
        "history": tuple(history),
        "fill": len(locks) == 12,
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
    print("construction: two independent occupancy-to-lock runs from the displayed seed S*")
    print("negative_scope: neither map nor the disagreeing stencil is adopted or written into Admissibility")
    print("cache_write: false")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_MIN_L1_FIRST_DISAGREEING_NEIGHBORHOOD_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_MIN_L1_FIRST_DISAGREEING_NEIGHBORHOOD_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "two-cube-and-seed",
        "the two-cube has twelve lexicographic vertices and the displayed seed S*",
        len(SITES) == 12
        and SITES == tuple(sorted(SITES))
        and SITES[0] == (0, 0, 0)
        and SITES[-1] == (2, 1, 1)
        and SEED == ((0, 0, 0), (2, 1, 1))
        and SEED_SET <= TWO_CUBE_SET,
    )
    checks.check(
        "off-patch-zero",
        "every off-patch neighbor contributes occupancy 0",
        occupancy((-1, 0, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((0, -1, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((3, 1, 1), frozenset({(2, 1, 1)})) == 0
        and occupancy((1, -1, 1), SEED_SET) == 0,
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
        and axis_type(ORBIT_REPS["empty"]) == (0, 0, 3),
    )
    checks.check(
        "f-min-rule",
        "f_min is 1 exactly when n_both=0 and some axis is unbalanced",
        f_min(ORBIT_REPS["wt1"]) == 1
        and f_min(ORBIT_REPS["adj2"]) == 1
        and f_min(ORBIT_REPS["vertex3"]) == 1
        and f_min(ORBIT_REPS["opp2"]) == 0
        and f_min(ORBIT_REPS["mixed3"]) == 0
        and f_min(ORBIT_REPS["type210"]) == 0
        and f_min(ORBIT_REPS["empty"]) == 0
        and f_min(ORBIT_REPS["full"]) == 0,
    )
    checks.check(
        "f-l1-is-n-unbalanced",
        "f_L1 is the n!=0 (some-axis-unbalanced) map, not Hamming parity",
        f_l1(ORBIT_REPS["wt1"]) == 1
        and f_l1(ORBIT_REPS["mixed3"]) == 1
        and f_l1(ORBIT_REPS["type210"]) == 1
        and f_l1(ORBIT_REPS["opp2"]) == 0
        and f_l1(ORBIT_REPS["empty"]) == 0
        and f_l1(ORBIT_REPS["adj2"]) != f_hamming(ORBIT_REPS["adj2"])
        and sum(ORBIT_REPS["opp2"]) % 2 == 0
        and "sum(config) % 2"
        not in self_source.split("def f_l1", 1)[1].split("def f_min", 1)[0],
    )
    checks.check(
        "maps-disagree-where-n-both-and-unbalanced",
        "the maps disagree on mixed3 and on type (2,1,0), and agree on opp2",
        f_min(ORBIT_REPS["mixed3"]) == 0
        and f_l1(ORBIT_REPS["mixed3"]) == 1
        and f_min(ORBIT_REPS["type210"]) == 0
        and f_l1(ORBIT_REPS["type210"]) == 1
        and f_min(ORBIT_REPS["opp2"]) == 0
        and f_l1(ORBIT_REPS["opp2"]) == 0,
    )

    run_l1 = run_from_seed(f_l1)
    run_min = run_from_seed(f_min)
    first_l1 = run_l1["first"]
    first_min = run_min["first"]
    print(
        f"run_L1: history={run_l1['history']} fill={run_l1['fill']} "
        f"halt_tick={run_l1['halt_tick']}"
    )
    print(
        f"run_min: history={run_min['history']} fill={run_min['fill']} "
        f"halt_tick={run_min['halt_tick']}"
    )
    if first_l1 is None:
        print("first_disagreeing_neighborhood_L1_run: none")
    else:
        print(
            f"first_disagreeing_neighborhood_L1_run: t={first_l1['tick']} "
            f"x={first_l1['site']} axis_type={first_l1['axis_type']} "
            f"stencil={first_l1['config']} f_L1={first_l1['f_l1']} "
            f"f_min={first_l1['f_min']}"
        )
    if first_min is None:
        print("first_disagreeing_neighborhood_min_run: none")
    else:
        print(
            f"first_disagreeing_neighborhood_min_run: t={first_min['tick']} "
            f"x={first_min['site']} axis_type={first_min['axis_type']} "
            f"stencil={first_min['config']} f_L1={first_min['f_l1']} "
            f"f_min={first_min['f_min']}"
        )

    checks.check(
        "theorem-1-reconfirm-fill",
        "from S* f_L1 fills with history (2, 8, 12) and f_min does not fill",
        run_l1["history"] == L1_HISTORY
        and run_l1["fill"]
        and run_l1["locks"] == TWO_CUBE_SET
        and not run_min["fill"]
        and len(run_min["locks"]) < 12
        and run_min["history"][0] == 2
        and "(2, 8, 12)" in note,
        residual=(run_l1["history"], run_min["history"], run_min["fill"]),
    )

    expected_site = (1, 0, 1)
    expected_type = (2, 1, 0)
    expected_stencil = (1, 1, 1, 0, 0, 1)
    checks.check(
        "theorem-2-first-disagreeing-neighborhood",
        "the first disagreeing neighborhood is t=2, x=(1,0,1), type (2,1,0)",
        first_l1 is not None
        and first_min is not None
        and first_l1["tick"] == 2
        and first_l1["site"] == expected_site
        and first_l1["axis_type"] == expected_type
        and first_l1["f_l1"] == 1
        and first_l1["f_min"] == 0
        and first_min["tick"] == 2
        and first_min["site"] == expected_site
        and first_min["axis_type"] == expected_type
        and first_min["f_l1"] == 1
        and first_min["f_min"] == 0
        and "(1, 0, 1)" in note
        and "(2, 1, 0)" in note,
        residual=None if first_l1 is None else (first_l1["tick"], first_l1["site"], first_l1["axis_type"]),
    )

    same_tick_sites = ()
    if first_l1 is not None:
        same_tick_sites = tuple(row["site"] for row in first_l1["all"])
    checks.check(
        "both-runs-same-first-split",
        "the two independent runs share the locked set through the first split",
        first_l1 is not None
        and first_min is not None
        and first_l1["tick"] == first_min["tick"]
        and first_l1["site"] == first_min["site"]
        and first_l1["config"] == first_min["config"]
        and same_tick_sites == ((1, 0, 1), (1, 1, 0))
        and run_l1["history"][:2] == run_min["history"][:2] == (2, 8),
        residual=same_tick_sites,
    )

    after1 = SEED_SET | ready_sites(SEED_SET, f_l1)
    stencil = neighbor_config(expected_site, after1)
    checks.check(
        "theorem-3-display-stencil",
        "the first disagreeing stencil is the displayed 6-tuple (1,1,1,0,0,1)",
        first_l1 is not None
        and first_l1["config"] == expected_stencil
        and stencil == expected_stencil
        and axis_type(stencil) == expected_type
        and "(1, 1, 1, 0, 0, 1)" in note
        and "Displayed, not adopted" in note
        and "not written into Admissibility" in normalize(note)
        and "Do not adopt" in note
        and "Do not write" in note,
        residual=None if first_l1 is None else first_l1["config"],
    )

    wave0 = disagreements(SEED_SET)
    checks.check(
        "no-split-before-tick-2",
        "no unlocked site disagrees at tick 1; the first wave is shared wt1",
        wave0 == []
        and ready_sites(SEED_SET, f_l1) == ready_sites(SEED_SET, f_min)
        and len(ready_sites(SEED_SET, f_l1)) == 6
        and all(
            axis_type(neighbor_config(site, SEED_SET)) == (1, 0, 2)
            for site in ready_sites(SEED_SET, f_l1)
        ),
        residual=wave0,
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
        "(2, 8, 12)",
        "(1, 0, 1)",
        "(2, 1, 0)",
        "(1, 1, 1, 0, 0, 1)",
    )
    source_body = self_source
    for declared in AUDIT_INPUT_PATHS:
        source_body = source_body.replace(declared, "")
        source_body = source_body.replace(Path(declared).name, "")
    checks.check(
        "note-contract",
        "machine fields, first-neighborhood statement, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required)
        and all(f"### N{index}" in note for index in range(1, 9))
        and all(phrase not in note and phrase not in source_body for phrase in forbidden)
        and "promoted" not in note.lower()
        and "new axiom" not in note
        and "Block 12" not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "not-leftover-or-clone",
        "the claim is a new neighborhood object, not leftover seed-naming of #6417",
        "Not leftover-character of #6417" in note
        and "that only named" in normalize(note)
        and "disagreeing stencil" in note
        and "Do not adopt a selector" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in normalize(note)
        and "not Hamming" in note
        and "`f_min(c)=1` if and only if `n_both(c)=0` and some axis is unbalanced"
        in normalize(note),
    )

    print("per_element: axis-type representatives and off-patch occupancy 0 are enumerated")
    print("per_site: each unlocked two-cube vertex is tested against both displayed lock predicates")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: both independent runs from S* are executed tick by tick to a fixed point")
    print("lattice_wide: checked and not executed — neither map nor the stencil is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
