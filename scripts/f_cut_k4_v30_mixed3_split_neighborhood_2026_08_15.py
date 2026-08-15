#!/usr/bin/env python3
"""First neighborhood where the vertex3=0 k=4 pair disagrees from S.

Two independent occupancy-to-lock runs start from the displayed seed
S={(0,0,0),(0,0,1),(2,0,0)} on the twelve-vertex two-cube with off-patch
occupancy 0.  The scored maps are F_cut remaining bits (1,1,1,0,0) and
(1,1,1,0,1).  At each tick both predicates are evaluated on every
unlocked site against that run's locked set.  The first (tick, site,
axis-type, 6-tuple) at which the predicates differ is displayed, not
adopted.  f_L1 is the some-axis-unbalanced (n!=0) map, not Hamming.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "F_CUT_K4_V30_MIXED3_SPLIT_NEIGHBORHOOD_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_K4_V30_MIXED3_SPLIT_NEIGHBORHOOD_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Cell = tuple[int, int, int, int, int, int]
Bits = tuple[int, int, int, int, int]

SITES: tuple[Point, ...] = tuple(
    sorted((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
)
TWO_CUBE_SET = frozenset(SITES)
SHIFTS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXES: tuple[tuple[int, int], ...] = ((0, 1), (2, 3), (4, 5))
FREE_ORBITS: tuple[str, ...] = ("wt1", "opp2", "adj2", "vertex3", "mixed3")
SEED: tuple[Point, ...] = ((0, 0, 0), (0, 0, 1), (2, 0, 0))
SEED_SET = frozenset(SEED)
F00_BITS: Bits = (1, 1, 1, 0, 0)
F01_BITS: Bits = (1, 1, 1, 0, 1)
L1_REMAINING: Bits = (1, 0, 1, 1, 1)
F00_S_HISTORY: tuple[int, ...] = (3, 9, 11, 12)
F01_S_HISTORY: tuple[int, ...] = (3, 9, 12)
MIXED3_TYPE = (1, 1, 1)
FIRST_TICK = 2
FIRST_SITE: Point = (1, 1, 0)
FIRST_STENCIL: Cell = (1, 1, 0, 1, 0, 0)


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def orbit_name(cell: Cell) -> str:
    weight = sum(cell)
    n_full = sum(1 for i, j in AXES if cell[i] == 1 and cell[j] == 1)
    if weight == 0:
        return "empty"
    if weight == 6:
        return "full"
    if weight == 1:
        return "wt1"
    if weight == 5:
        return "wt5"
    if weight == 2:
        return "opp2" if n_full == 1 else "adj2"
    if weight == 4:
        return "opp4" if n_full == 2 else "adj4"
    if weight == 3:
        return "mixed3" if n_full == 1 else "vertex3"
    raise ValueError(cell)


def all_cells() -> tuple[Cell, ...]:
    return tuple(product((0, 1), repeat=6))  # type: ignore[return-value]


def complement(cell: Cell) -> Cell:
    return tuple(1 - bit for bit in cell)  # type: ignore[return-value]


def axis_type(config: Cell) -> tuple[int, int, int]:
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


def axis_unbalanced(cell: Cell) -> bool:
    return any(cell[i] != cell[j] for i, j in AXES)


def occupancy(site: Point, locks: frozenset[Point]) -> int:
    if site not in TWO_CUBE_SET:
        return 0
    return 1 if site in locks else 0


def neighbor_config(site: Point, locks: frozenset[Point]) -> Cell:
    bits = [occupancy(add(site, shift), locks) for shift in SHIFTS]
    return (bits[0], bits[1], bits[2], bits[3], bits[4], bits[5])


def f_L1(cell: Cell) -> int:
    """Formation on a 6-tuple iff some axis is unbalanced (n != 0)."""
    return int(axis_unbalanced(cell))


def f_hamming(cell: Cell) -> int:
    return sum(cell) % 2


def f_cut_from_bits(bits: Bits):
    wt1, opp2, adj2, vertex3, mixed3 = bits
    table = {
        "empty": 0,
        "full": 0,
        "wt1": wt1,
        "wt5": wt1,
        "opp2": opp2,
        "opp4": opp2,
        "adj2": adj2,
        "adj4": adj2,
        "vertex3": vertex3,
        "mixed3": mixed3,
    }
    return lambda cell: table[orbit_name(cell)]


def remaining_bits(predicate) -> Bits:
    reps: dict[str, Cell] = {}
    for cell in all_cells():
        name = orbit_name(cell)
        if name not in reps:
            reps[name] = cell
    return tuple(int(predicate(reps[name])) for name in FREE_ORBITS)  # type: ignore[return-value]


def ready_sites(locks: frozenset[Point], predicate) -> frozenset[Point]:
    return frozenset(
        site
        for site in SITES
        if site not in locks and predicate(neighbor_config(site, locks)) == 1
    )


def disagreements(locks: frozenset[Point], pred_a, pred_b) -> list[dict]:
    rows: list[dict] = []
    for site in SITES:
        if site in locks:
            continue
        config = neighbor_config(site, locks)
        value_a = pred_a(config)
        value_b = pred_b(config)
        if value_a != value_b:
            rows.append(
                {
                    "site": site,
                    "config": config,
                    "axis_type": axis_type(config),
                    "orbit": orbit_name(config),
                    "f00": value_a,
                    "f01": value_b,
                }
            )
    return rows


def run_from_seed(predicate, pred_a, pred_b, halt_bound: int = 12) -> dict:
    locks = frozenset(SEED_SET)
    history = [len(locks)]
    first = None
    tick = 0
    while tick < halt_bound:
        tick += 1
        split = disagreements(locks, pred_a, pred_b)
        if split and first is None:
            first = {"tick": tick, **split[0], "all": tuple(split)}
        nxt = locks | ready_sites(locks, predicate)
        if nxt == locks:
            break
        locks = nxt
        history.append(len(locks))
    return {
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
    source = Path(__file__).read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: current Lattice, Admissibility, and "
        "Record wording; no observations or fits"
    )
    print("integrity_reads: this runner, its note, and the axiom memo")
    print(
        "construction: independent occupancy-to-lock runs of F_cut maps "
        "(1,1,1,0,0) and (1,1,1,0,1) on the two-cube, off-patch occupancy 0, "
        "from S={(0,0,0),(0,0,1),(2,0,0)}"
    )
    print(
        "negative_scope: displayed first neighborhood only; mixed3 is not adopted"
    )

    expected_tuple = (
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_K4_V30_MIXED3_SPLIT_NEIGHBORHOOD_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")"
    )
    checks.check(
        "audit-inputs",
        "declared inputs are the required two static string literals and exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_K4_V30_MIXED3_SPLIT_NEIGHBORHOOD_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and expected_tuple in source
        and AUDIT_TIMEOUT_SEC == 120
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    lattice_sites = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    admissibility = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    local_distribution = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    formation_residual = "it does not supply the formation site, probability, or rate."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    records_form = "Records form."
    not_dynamics = "Admissibility is not a dynamics axiom."

    checks.check(
        "source-lattice-admissibility",
        "Lattice rotations and Admissibility covariance are pinned",
        lattice_sites in axiom_flat
        and admissibility in axiom_flat
        and lattice_sites in note_flat
        and admissibility in note_flat,
    )
    checks.check(
        "source-local-distribution",
        "current local-distribution wording is pinned",
        local_distribution in axiom_flat and local_distribution in note,
    )
    checks.check(
        "source-record-boundary",
        "Record lock, content-only readout, unreadable absence, and formation residual are pinned",
        all(
            phrase in axiom_flat
            for phrase in (
                records_form,
                record_lock,
                record_content,
                record_absence,
                formation_residual,
            )
        )
        and all(
            phrase in note
            for phrase in (
                records_form,
                record_lock,
                record_content,
                record_absence,
            )
        )
        and formation_residual in note_flat
        and not_dynamics in axiom
        and not_dynamics in note,
    )

    cells = all_cells()
    orbit_counts = Counter(orbit_name(cell) for cell in cells)
    expected_counts = {
        "empty": 1,
        "full": 1,
        "wt1": 6,
        "wt5": 6,
        "opp2": 3,
        "adj2": 12,
        "vertex3": 8,
        "mixed3": 12,
        "opp4": 3,
        "adj4": 12,
    }
    checks.check(
        "two-cube-and-seed",
        "two-cube has twelve lexicographic vertices and S is the displayed three-site seed",
        len(SITES) == 12 == len(set(SITES))
        and SITES == tuple(sorted(SITES))
        and SEED == ((0, 0, 0), (0, 0, 1), (2, 0, 0))
        and SEED_SET <= TWO_CUBE_SET,
    )
    checks.check(
        "orbit-partition",
        "proper-cube action on six-tuples has ten orbits with derived sizes",
        orbit_counts == expected_counts,
        residual=dict(orbit_counts),
    )

    f00 = f_cut_from_bits(F00_BITS)
    f01 = f_cut_from_bits(F01_BITS)
    l1_bits = remaining_bits(f_L1)
    ham_bits = remaining_bits(f_hamming)
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis is unbalanced, and evaluates to (1,0,1,1,1)",
        l1_bits == L1_REMAINING
        and remaining_bits(f00) == F00_BITS
        and remaining_bits(f01) == F01_BITS
        and all(f_L1(cell) == int(axis_unbalanced(cell)) for cell in cells)
        and f_L1((0, 0, 0, 0, 0, 0)) == 0
        and f_L1((1, 1, 1, 1, 1, 1)) == 0
        and all(f_L1(cell) == f_L1(complement(cell)) for cell in cells),
        residual=l1_bits,
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is not Hamming |c|_1 mod 2",
        ham_bits == (1, 0, 0, 1, 1)
        and ham_bits != l1_bits
        and any(f_L1(cell) != f_hamming(cell) for cell in cells)
        and "sum(cell) % 2"
        not in source.split("def f_L1", 1)[1].split("def f_hamming", 1)[0],
        residual=ham_bits,
    )
    checks.check(
        "off-patch-zero",
        "every off-patch neighbor contributes occupancy 0",
        occupancy((-1, 0, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((0, -1, 0), frozenset({(0, 0, 0)})) == 0
        and occupancy((3, 0, 0), frozenset({(2, 0, 0)})) == 0
        and occupancy((1, -1, 0), SEED_SET) == 0
        and "off-patch occupancy" in note
        and "blank-block is a different rule" in note,
    )

    run_f00 = run_from_seed(f00, f00, f01)
    run_f01 = run_from_seed(f01, f00, f01)
    first_00 = run_f00["first"]
    first_01 = run_f01["first"]
    print(f"f00_S_history={run_f00['history']} fill={run_f00['fill']}")
    print(f"f01_S_history={run_f01['history']} fill={run_f01['fill']}")
    if first_00 is None:
        print("first_disagreeing_neighborhood_f00_run: none")
    else:
        print(
            f"first_disagreeing_neighborhood_f00_run: t={first_00['tick']} "
            f"x={first_00['site']} axis_type={first_00['axis_type']} "
            f"orbit={first_00['orbit']} stencil={first_00['config']} "
            f"f00={first_00['f00']} f01={first_00['f01']}"
        )
    if first_01 is None:
        print("first_disagreeing_neighborhood_f01_run: none")
    else:
        print(
            f"first_disagreeing_neighborhood_f01_run: t={first_01['tick']} "
            f"x={first_01['site']} axis_type={first_01['axis_type']} "
            f"orbit={first_01['orbit']} stencil={first_01['config']} "
            f"f00={first_01['f00']} f01={first_01['f01']}"
        )

    checks.check(
        "theorem-1-reconfirm-histories",
        "from S, f00 fills with (3, 9, 11, 12) and f01 fills with (3, 9, 12)",
        run_f00["history"] == F00_S_HISTORY
        and run_f00["fill"]
        and run_f00["locks"] == TWO_CUBE_SET
        and run_f01["history"] == F01_S_HISTORY
        and run_f01["fill"]
        and run_f01["locks"] == TWO_CUBE_SET
        and run_f00["history"] != run_f01["history"]
        and "(3, 9, 11, 12)" in note
        and "(3, 9, 12)" in note,
        residual=(run_f00["history"], run_f01["history"]),
    )

    checks.check(
        "theorem-2-first-disagreeing-neighborhood",
        "the first disagreeing neighborhood is t=2, x=(1,1,0), type (1,1,1)",
        first_00 is not None
        and first_01 is not None
        and first_00["tick"] == FIRST_TICK
        and first_00["site"] == FIRST_SITE
        and first_00["axis_type"] == MIXED3_TYPE
        and first_00["orbit"] == "mixed3"
        and first_00["f00"] == 0
        and first_00["f01"] == 1
        and first_01["tick"] == FIRST_TICK
        and first_01["site"] == FIRST_SITE
        and first_01["axis_type"] == MIXED3_TYPE
        and first_01["f00"] == 0
        and first_01["f01"] == 1
        and "(1, 1, 0)" in note
        and "(1, 1, 1)" in note,
        residual=(
            None
            if first_00 is None
            else (first_00["tick"], first_00["site"], first_00["axis_type"])
        ),
    )

    same_tick_sites = ()
    if first_00 is not None:
        same_tick_sites = tuple(row["site"] for row in first_00["all"])
    checks.check(
        "both-runs-same-first-split",
        "the two independent runs share the locked set through the first split",
        first_00 is not None
        and first_01 is not None
        and first_00["tick"] == first_01["tick"]
        and first_00["site"] == first_01["site"]
        and first_00["config"] == first_01["config"]
        and same_tick_sites == (FIRST_SITE,)
        and run_f00["history"][:2] == run_f01["history"][:2] == (3, 9),
        residual=same_tick_sites,
    )

    after1 = SEED_SET | ready_sites(SEED_SET, f00)
    stencil = neighbor_config(FIRST_SITE, after1)
    checks.check(
        "theorem-3-display-stencil",
        "the first disagreeing stencil is the displayed 6-tuple (1,1,0,1,0,0)",
        first_00 is not None
        and first_00["config"] == FIRST_STENCIL
        and stencil == FIRST_STENCIL
        and axis_type(stencil) == MIXED3_TYPE
        and orbit_name(stencil) == "mixed3"
        and "(1, 1, 0, 1, 0, 0)" in note
        and "Displayed, not adopted" in note
        and "Do not adopt mixed3" in note
        and "Do not write mixed3 into Admissibility" in note,
        residual=None if first_00 is None else first_00["config"],
    )

    wave0 = disagreements(SEED_SET, f00, f01)
    first_wave = ready_sites(SEED_SET, f00)
    checks.check(
        "no-split-before-tick-2",
        "no unlocked site disagrees at tick 1; the first wave is shared",
        wave0 == []
        and first_wave == ready_sites(SEED_SET, f01)
        and len(first_wave) == 6
        and neighbor_config((1, 0, 0), SEED_SET) == (1, 1, 0, 0, 0, 0)
        and axis_type(neighbor_config((1, 0, 0), SEED_SET)) == (0, 1, 2)
        and f00(neighbor_config((1, 0, 0), SEED_SET)) == 1
        and f01(neighbor_config((1, 0, 0), SEED_SET)) == 1,
        residual=wave0,
    )

    claim_scope = (
        "On the two-cube with off-patch o=0 and seed "
        "{(0,0,0),(0,0,1),(2,0,0)}, the first neighborhood at which F_cut "
        "(1,1,1,0,0) and (1,1,1,0,1) disagree is reported by tick, site, "
        "and axis type. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope states the displayed first neighborhood and does not adopt mixed3",
        claim_scope in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note.lower(),
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted uniqueness, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "target_claim_type: bounded_theorem" in note
        and "trace_class: frontier_discovery" in note
        and "reachability_to_target: advances" in note
        and 'hypothetical_axiom_status: "no edit"' in note
        and "authors no audit verdict" in note
        and "FAIL / DO NOT SHIP" in note
        and "Theorem 1" in note
        and "Theorem 2" in note
        and "Theorem 3" in note,
    )
    checks.check(
        "claim-type-and-gate",
        "N1-N8 and a passing no-go disposition are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )
    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in source for phrase in forbidden),
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note_flat
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "not-leftover-6452-6441",
        "the residual is a new neighborhood object, not leftover of #6452 or #6441",
        "Not leftover-character of #6452" in note
        and "histories only" in note
        and "Not leftover-character of #6441" in note
        and "different pair" in note
        and "New object" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt mixed3",
        "no axiom or approved primitive is added" in note
        and "Do not adopt mixed3" in note
        and "Do not write mixed3 into Admissibility" in note,
    )
    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-hygiene",
        "machine retained fields are the only retained lines; no cache or citation surface",
        all(line in note for line in allowed_retained)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "toe-lphys" not in note
        and "runner-cache" not in note
        and "citation" not in note.lower(),
    )
    checks.check(
        "axiom-unedited",
        "the axiom memo still carries the four named premises and no F_cut class",
        "### Lattice / Physical Locality" in axiom
        and "### Qubit / Site Possibility" in axiom
        and "### Admissibility / Local Constraint" in axiom
        and "### Record / Fixed Reality" in axiom
        and "F_cut" not in axiom
        and "f_L1" not in axiom
        and "mixed3" not in axiom,
    )

    print(
        "per_element: checked exactly — each of the 64 neighbor 6-tuples is "
        "assigned its axis-type orbit"
    )
    print(
        "per_site: checked exactly — each unlocked two-cube vertex is tested "
        "against both displayed lock predicates"
    )
    print("per_mode: checked and not executed — no spectral claim occurs")
    print(
        "per_block: checked exactly — both independent runs from S are "
        "executed tick by tick to a fixed point"
    )
    print(
        "lattice_wide: checked and not executed — no Z^3-wide formation law "
        "or physical Admissibility selector is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
