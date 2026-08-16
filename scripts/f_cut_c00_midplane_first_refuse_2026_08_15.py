#!/usr/bin/env python3
"""First refused neighborhood of F_cut (1,0,0,0,0) on the #6504 midplane.

Independent occupancy-to-lock run from the size-1 midplane four-site
S = {(1,0,0),(1,0,1),(1,1,0),(1,1,1)} on the twelve-vertex two-cube
with off-patch occupancy 0.  f00 is the F_cut remaining-bit map
(1,0,0,0,0): fire only on wt1 and its complement wt5.  The first
remaining-bit neighborhood that f00 refuses on that filling run is
reported, or N_refuse=0 if every remaining-bit orbit that appears is
accepted.  Displayed, not adopted.  f_L1 is the unbalanced-axis
predicate (some n_mu != 0), never Hamming |c|_1 mod 2.  New seed
census: not leftover of #6504 (that named N_orb=3 and the midplane)
and not the #6493 face refuse census.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_C00_MIDPLANE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_C00_MIDPLANE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
F00_TUPLE: tuple[int, ...] = (1, 0, 0, 0, 0)
L1_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 1)
SEED: tuple[Point, ...] = ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))
SEED_DISPLAY = "{(1,0,0),(1,0,1),(1,1,0),(1,1,1)}"
FACE_SEED: tuple[Point, ...] = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1))
FIRST_HISTORY = (4, 12)
REMAINING_TYPES: frozenset[OrbitType] = frozenset(
    (
        (1, 0, 2),
        (1, 2, 0),
        (0, 1, 2),
        (0, 2, 1),
        (2, 0, 1),
        (2, 1, 0),
        (3, 0, 0),
        (1, 1, 1),
    )
)
AXIS_TYPE_NAME: dict[OrbitType, str] = {
    (0, 0, 3): "empty",
    (0, 3, 0): "full",
    (1, 0, 2): "wt1",
    (1, 2, 0): "wt5",
    (0, 1, 2): "opp2",
    (0, 2, 1): "opp2_comp",
    (2, 0, 1): "adj2",
    (2, 1, 0): "adj2_comp",
    (3, 0, 0): "vertex3",
    (1, 1, 1): "mixed3",
}
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
    snapshots = [locks]
    tick = 0
    while tick < halt_bound:
        nxt = step(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        tick += 1
        history.append(len(locks))
        snapshots.append(locks)
    return tick, frozenset(locks), tuple(history), tuple(snapshots)


def refusal_census(seed: frozenset[Point], predicate=f00, halt_bound: int = 12) -> dict:
    """Remaining-bit refuses on the independent run; empty/full are cuts, not remaining bits."""
    locks = frozenset(seed)
    remaining_refuses: list[dict] = []
    empty_refuses: list[dict] = []
    appeared_remaining: list[OrbitType] = []
    for tick in range(halt_bound + 1):
        for site in SITES:
            if site in locks:
                continue
            config = neighbor_config(site, locks)
            kind = axis_type(config)
            value = predicate(config)
            if kind in REMAINING_TYPES:
                appeared_remaining.append(kind)
                if value == 0:
                    remaining_refuses.append(
                        {
                            "tick": tick,
                            "site": site,
                            "config": config,
                            "axis_type": kind,
                            "axis_name": AXIS_TYPE_NAME[kind],
                        }
                    )
            elif value == 0:
                empty_refuses.append(
                    {
                        "tick": tick,
                        "site": site,
                        "config": config,
                        "axis_type": kind,
                        "axis_name": AXIS_TYPE_NAME[kind],
                    }
                )
        nxt = step(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
    first = remaining_refuses[0] if remaining_refuses else None
    return {
        "n_refuse": len(remaining_refuses),
        "first": first,
        "remaining_refuses": tuple(remaining_refuses),
        "empty_refuses": tuple(empty_refuses),
        "appeared_remaining": tuple(appeared_remaining),
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
    print("construction: displayed F_cut occupancy-to-lock map; first remaining-bit refuse on the #6504 midplane")
    print("negative_scope: neither the map nor any remaining bit is adopted or written into Admissibility")
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
            "docs/F_CUT_C00_MIDPLANE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_C00_MIDPLANE_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and axis_type(ORBIT_REPS["full"]) == (0, 3, 0),
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

    tick, locks, history, snapshots = run_from_seed(frozenset(SEED), f00)
    census = refusal_census(frozenset(SEED), f00)
    seed0 = frozenset(SEED)
    after1 = step(seed0, f00)
    wave1 = after1 - seed0
    after2 = step(after1, f00)
    wave2 = after2 - after1
    expected_wave1 = frozenset(
        {
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (2, 0, 0),
            (2, 0, 1),
            (2, 1, 0),
            (2, 1, 1),
        }
    )
    x0_wave = frozenset({(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1)})
    x2_wave = frozenset({(2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1)})
    empty_sites = tuple(row["site"] for row in census["empty_refuses"])
    appeared_names = tuple(AXIS_TYPE_NAME[kind] for kind in census["appeared_remaining"])

    print(f"seed={SEED_DISPLAY}")
    print(f"history={history} T={tick} fill={locks == TWO_CUBE_SET}")
    print(f"wave1={sorted(wave1)}")
    print(f"wave2={sorted(wave2)}")
    print(f"appeared_remaining={appeared_names}")
    print(f"N_refuse={census['n_refuse']}")
    print(f"first_remaining_refuse={census['first']}")
    print(f"empty_refuses_n={len(census['empty_refuses'])} sites={empty_sites}")

    checks.check(
        "theorem-1-f00-fills-midplane",
        "f00 fills the #6504 midplane S with history (4, 12)",
        tick == 1
        and history == FIRST_HISTORY
        and locks == TWO_CUBE_SET
        and len(SEED) == 4
        and SEED != FACE_SEED
        and SEED_DISPLAY.replace(" ", "") in note.replace(" ", "")
        and "(4, 12)" in note
        and "#6504" in note,
        residual=(tick, history, len(locks)),
    )
    checks.check(
        "fill-mechanism-waves",
        "the midplane locks both end faces in one tick, each site as wt1",
        wave1 == expected_wave1
        and wave2 == frozenset()
        and after1 == TWO_CUBE_SET
        and after2 == TWO_CUBE_SET
        and all(axis_type(neighbor_config(site, seed0)) == (1, 0, 2) for site in wave1)
        and all(neighbor_config(site, seed0) == (1, 0, 0, 0, 0, 0) for site in x0_wave)
        and all(neighbor_config(site, seed0) == (0, 1, 0, 0, 0, 0) for site in x2_wave)
        and all(f00(neighbor_config(site, seed0)) == 1 for site in wave1),
        residual=(sorted(wave1), sorted(wave2)),
    )
    checks.check(
        "theorem-2-n-refuse-zero",
        "every remaining-bit orbit that appears is accepted; N_refuse=0",
        census["n_refuse"] == 0
        and census["first"] is None
        and set(census["appeared_remaining"]) == {(1, 0, 2)}
        and f00(ORBIT_REPS["wt1"]) == 1
        and "N_refuse=0" in note,
        residual=(census["n_refuse"], census["first"], appeared_names),
    )
    checks.check(
        "theorem-2-note-reports-n-refuse",
        "the note reports N_refuse=0 and that only wt1 appears as a remaining bit",
        "N_refuse=0" in note
        and "`wt1`" in note
        and "remaining-bit" in note
        and "refuses none" in note.lower(),
    )
    checks.check(
        "empty-cut-does-not-appear",
        "no unlocked site sees empty; empty remains an F_cut cut, not a remaining bit",
        len(census["empty_refuses"]) == 0
        and empty_sites == ()
        and (0, 0, 3) not in REMAINING_TYPES
        and "empty" in note
        and snapshots[0] == seed0
        and snapshots[-1] == TWO_CUBE_SET,
        residual=empty_sites,
    )
    checks.check(
        "theorem-3-display-not-adopt",
        "the note displays the refuse census and refuses adoption of a bit",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in normalize(note)
        and "Do not adopt" in note
        and "Do not write" in note,
    )

    claim_scope = (
        "On the two-cube with off-patch o=0, the first refused neighborhood "
        "of F_cut (1,0,0,0,0) on the #6504 size-1 midplane four-site fill is "
        "reported, or the run refuses none. Displayed, not adopted."
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
        "(4, 12)",
        "(1, 0, 0, 0, 0)",
        "N_refuse=0",
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
        "claim_scope reports the first refused neighborhood or that the run refuses none",
        claim_scope in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note.lower(),
    )
    checks.check(
        "note-contract",
        "machine fields, refuse census, and forbidden-phrase hygiene hold",
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
        "not-leftover-6504-or-6493-face",
        "the residual is the refuse census on the midplane, not leftover of #6504 or the #6493 face",
        "Not leftover-character of #6504" in note
        and "that named `N_orb=3` and the size-1" in note
        and "Not leftover-character of #6493" in note
        and "not the `#6493` face" in note
        and "New finite object" in normalize(note).replace("new finite object", "New finite object"),
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
    print("per_block: the #6504 midplane run is executed to a fixed point and remaining-bit refuses are counted")
    print("lattice_wide: checked and not executed — neither the map nor a remaining bit is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
