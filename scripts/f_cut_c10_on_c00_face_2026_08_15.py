#!/usr/bin/env python3
"""Whether F_cut (1,1,0,0,0) fills the #6493 four-site face.

Two-cube occupancy-to-lock dynamics with off-patch occupancy 0.  S is the
#6493 face {(0,0,0),(0,0,1),(0,1,0),(0,1,1)}.  Theorem 1 reconfirms that
f00=(1,0,0,0,0) fills S.  Theorem 2 reports whether f10=(1,1,0,0,0) fills
S and locks the history either way.  f_L1 is the some-axis-unbalanced
(n!=0) map, not Hamming parity.  Displayed, not adopted.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_C10_ON_C00_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_C10_ON_C00_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
F10_TUPLE: tuple[int, ...] = (1, 1, 0, 0, 0)
F00_TUPLE: tuple[int, ...] = (1, 0, 0, 0, 0)
L1_TUPLE: tuple[int, ...] = (1, 0, 1, 1, 1)
FACE: tuple[Point, ...] = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1))
SEED_6492: tuple[Point, ...] = ((0, 0, 0), (1, 1, 1), (2, 0, 0))
FACE_HISTORY = (4, 8, 12)

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


def f10(config: Config) -> int:
    """F_cut remaining bits (1,1,0,0,0): fire on wt1, opp2, and complements."""
    kind = axis_type(config)
    return 1 if kind in ((1, 0, 2), (0, 1, 2), (1, 2, 0), (0, 2, 1)) else 0


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
    tick = 0
    while tick < halt_bound:
        nxt = step(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        tick += 1
        history.append(len(locks))
    return tick, frozenset(locks), tuple(history)


def fills(seed: tuple[Point, ...] | frozenset[Point], predicate) -> bool:
    _tick, locks, _history = run_from_seed(frozenset(seed), predicate)
    return len(locks) == 12


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
    print("construction: displayed F_cut occupancy-to-lock maps on the #6493 four-site face")
    print("negative_scope: neither map nor remaining bit is adopted or written into Admissibility")
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
            "docs/F_CUT_C10_ON_C00_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_C10_ON_C00_FACE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        and TWO_CUBE_SET == frozenset(SITES)
        and FACE == SITES[:4],
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

    f10_bits = remaining_tuple(f10)
    f00_bits = remaining_tuple(f00)
    l1_bits = remaining_tuple(f_L1)
    checks.check(
        "f10-remaining-bits",
        "f10 is the F_cut remaining-bit tuple (1,1,0,0,0)",
        f10_bits == F10_TUPLE
        and f00_bits == F00_TUPLE
        and l1_bits == L1_TUPLE
        and f10(ORBIT_REPS["wt1"]) == 1
        and f10(ORBIT_REPS["opp2"]) == 1
        and f10(ORBIT_REPS["wt5"]) == 1
        and f10(ORBIT_REPS["opp2c"]) == 1
        and f10(ORBIT_REPS["adj2"]) == 0
        and f10(ORBIT_REPS["vertex3"]) == 0
        and f10(ORBIT_REPS["mixed3"]) == 0
        and f10(ORBIT_REPS["empty"]) == 0
        and f10(ORBIT_REPS["full"]) == 0
        and f00(ORBIT_REPS["opp2"]) == 0
        and f00(ORBIT_REPS["wt1"]) == 1,
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
        not in self_source.split("def f_L1", 1)[1].split("def f10", 1)[0],
    )

    seed = frozenset(FACE)
    tick00, locks00, history00 = run_from_seed(seed, f00)
    tick10, locks10, history10 = run_from_seed(seed, f10)
    after1_00 = step(seed, f00)
    after1_10 = step(seed, f10)
    middle = frozenset({(1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)})
    far = frozenset({(2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1)})
    print(f"f00_on_face history={history00} T={tick00} fill={locks00 == TWO_CUBE_SET}")
    print(f"f10_on_face history={history10} T={tick10} fill={locks10 == TWO_CUBE_SET}")

    checks.check(
        "theorem-1-f00-fills-face",
        "f00 fills the #6493 four-site face with history (4, 8, 12)",
        tick00 == 2
        and history00 == FACE_HISTORY
        and locks00 == TWO_CUBE_SET
        and fills(FACE, f00)
        and after1_00 == seed | middle
        and all(axis_type(neighbor_config(site, seed)) == (1, 0, 2) for site in middle)
        and all(axis_type(neighbor_config(site, seed)) == (0, 0, 3) for site in far)
        and all(f00(neighbor_config(site, seed)) == 1 for site in middle)
        and all(f00(neighbor_config(site, seed)) == 0 for site in far)
        and "#6493" in note
        and "(4, 8, 12)" in note,
        residual=(tick00, history00, len(locks00)),
    )
    checks.check(
        "theorem-2-f10-fills-face",
        "f10 fills the same #6493 four-site face",
        tick10 == 2
        and history10 == FACE_HISTORY
        and locks10 == TWO_CUBE_SET
        and fills(FACE, f10)
        and after1_10 == after1_00
        and all(f10(neighbor_config(site, seed)) == 1 for site in middle)
        and all(f10(neighbor_config(site, seed)) == 0 for site in far)
        and all(axis_type(neighbor_config(site, after1_10)) == (1, 0, 2) for site in far)
        and all(f10(neighbor_config(site, after1_10)) == 1 for site in far),
        residual=(tick10, history10, len(locks10)),
    )
    checks.check(
        "theorem-2-history-either-way",
        "the lock history on this face is (4, 8, 12) for both maps",
        history00 == FACE_HISTORY
        and history10 == FACE_HISTORY
        and "history `(4, 8, 12)`" in note
        and "`f10` also fills" in note,
        residual=(history00, history10),
    )
    checks.check(
        "opp2-not-seen-on-face",
        "this face executes only wt1; opp2 does not appear",
        all(
            axis_type(neighbor_config(site, seed)) in ((1, 0, 2), (0, 0, 3))
            for site in TWO_CUBE_SET - seed
        )
        and all(
            axis_type(neighbor_config(site, after1_10)) == (1, 0, 2)
            for site in far
        )
        and f10(ORBIT_REPS["opp2"]) != f00(ORBIT_REPS["opp2"])
        and "only `wt1`" in note,
    )

    tick00_s3, locks00_s3, history00_s3 = run_from_seed(frozenset(SEED_6492), f00)
    tick10_s3, locks10_s3, history10_s3 = run_from_seed(frozenset(SEED_6492), f10)
    print(f"f00_on_6492 history={history00_s3} fill={locks00_s3 == TWO_CUBE_SET}")
    print(f"f10_on_6492 history={history10_s3} fill={locks10_s3 == TWO_CUBE_SET}")

    checks.check(
        "not-6492-named-pair",
        "this face is not a second named-pair fill of the #6492 seed",
        FACE != SEED_6492
        and fills(SEED_6492, f10)
        and not fills(SEED_6492, f00)
        and history10_s3 == (3, 12)
        and history00_s3 == (3, 11)
        and "not a second named-pair fill of `#6492`" in normalize(note)
        and "#6496" in note
        and "{(0,0,0),(1,1,1),(2,0,0)}" in note.replace(" ", ""),
        residual=(FACE, SEED_6492, history00_s3, history10_s3),
    )
    checks.check(
        "theorem-3-display-not-adopt",
        "the note displays the face and refuses adoption of a bit",
        "Displayed, not adopted" in note
        and "not written into Admissibility" in normalize(note)
        and "Do not adopt a bit" in note
        and "Do not write" in note,
    )

    claim_scope = (
        "On the two-cube with off-patch o=0, whether F_cut "
        "(1,1,0,0,0) fills the #6493 four-site face of "
        "(1,0,0,0,0) is reported. Displayed, not adopted."
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
        "(4, 8, 12)",
        "(1, 1, 0, 0, 0)",
        "(1, 0, 0, 0, 0)",
        "#6493",
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
        "claim_scope reports whether f10 fills the #6493 face and does not adopt it",
        claim_scope in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note.lower(),
    )
    checks.check(
        "note-contract",
        "machine fields, face-fill statement, and forbidden-phrase hygiene hold",
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
        and "f10" not in axiom,
    )

    print("per_element: axis-type representatives and off-patch occupancy 0 are enumerated")
    print("per_site: each two-cube vertex is tested against both displayed lock predicates")
    print("per_mode: checked and not executed — no spectral claim occurs")
    print("per_block: the displayed four-site face is executed to a fixed point")
    print("lattice_wide: checked and not executed — neither map nor bit is adopted")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
