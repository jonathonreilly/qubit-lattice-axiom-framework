#!/usr/bin/env python3
"""Exact lock histories of the vertex3=0 k=4 pair from the mix0/L1 seed.

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. The scored maps are remaining bits (1,1,1,0,0) and (1,1,1,0,1).
The scored seed is S={(0,0,0),(0,0,1),(2,0,0)}. f_L1 is the unbalanced-axis
predicate (some n_mu != 0), never Hamming |c|_1 mod 2. The equality bit of
the two lock histories is displayed; mixed3 is not adopted.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "F_CUT_K4_V30_MIXED3_SPLIT_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_K4_V30_MIXED3_SPLIT_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
Cell = tuple[int, int, int, int, int, int]
Bits = tuple[int, int, int, int, int]

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
VERTICES: tuple[Point, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
ONE_SITE: tuple[Point, ...] = ((0, 0, 0),)
SEED_S: tuple[Point, ...] = ((0, 0, 0), (0, 0, 1), (2, 0, 0))
F00_BITS: Bits = (1, 1, 1, 0, 0)
F01_BITS: Bits = (1, 1, 1, 0, 1)
MIX0_BITS: Bits = (1, 0, 1, 1, 0)
L1_REMAINING: Bits = (1, 0, 1, 1, 1)
ONE_SITE_HISTORY: tuple[int, ...] = (1, 4, 8, 10, 11, 12)
F00_S_HISTORY: tuple[int, ...] = (3, 9, 11, 12)
F01_S_HISTORY: tuple[int, ...] = (3, 9, 12)
L1_S_HISTORY: tuple[int, ...] = (3, 8, 11, 12)
MIX0_S_HISTORY: tuple[int, ...] = (3, 8, 10)
EQUALITY_BIT = 0


def normalize(text: str) -> str:
    return " ".join(text.split())


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


def axis_unbalanced(cell: Cell) -> bool:
    return any(cell[i] != cell[j] for i, j in AXES)


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


def neighborhood(site: Point, locked: set[Point]) -> Cell:
    bits = []
    for shift in SHIFTS:
        neighbor = (site[0] + shift[0], site[1] + shift[1], site[2] + shift[2])
        bits.append(1 if neighbor in locked else 0)
    return tuple(bits)  # type: ignore[return-value]


def run_locks(predicate, seed: tuple[Point, ...]) -> tuple[int, tuple[int, ...]]:
    locked: set[Point] = set(seed)
    history = [len(locked)]
    for _tick in range(13):
        fresh = {
            site
            for site in VERTICES
            if site not in locked and predicate(neighborhood(site, locked))
        }
        if not fresh:
            break
        locked |= fresh
        history.append(len(locked))
    return len(locked), tuple(history)


def fills_from_seed(predicate, seed: tuple[Point, ...]) -> bool:
    halt, _history = run_locks(predicate, seed)
    return halt == len(VERTICES)


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
        "from (0,0,0) and from S={(0,0,0),(0,0,1),(2,0,0)}"
    )
    print("negative_scope: displayed equality bit only; mixed3 is not adopted")

    expected_tuple = (
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_K4_V30_MIXED3_SPLIT_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")"
    )
    checks.check(
        "audit-inputs",
        "declared inputs are the required two static string literals and exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_K4_V30_MIXED3_SPLIT_SEED_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        and formation_residual in note_flat,
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
        "vertex-count",
        "two-cube has twelve vertices and S is the displayed three-site seed",
        len(VERTICES) == 12 == len(set(VERTICES))
        and SEED_S == ((0, 0, 0), (0, 0, 1), (2, 0, 0))
        and set(SEED_S).issubset(set(VERTICES))
        and ONE_SITE == ((0, 0, 0),),
    )
    checks.check(
        "orbit-partition",
        "proper-cube action on six-tuples has ten orbits with derived sizes",
        orbit_counts == expected_counts,
        residual=dict(orbit_counts),
    )
    complement_pairs = {
        (orbit_name(cell), orbit_name(complement(cell))) for cell in cells
    }
    checks.check(
        "complement-action",
        "complement pairs empty/full, wt1/wt5, opp2/opp4, adj2/adj4 and fixes vertex3, mixed3",
        complement_pairs
        == {
            ("empty", "full"),
            ("full", "empty"),
            ("wt1", "wt5"),
            ("wt5", "wt1"),
            ("opp2", "opp4"),
            ("opp4", "opp2"),
            ("adj2", "adj4"),
            ("adj4", "adj2"),
            ("vertex3", "vertex3"),
            ("mixed3", "mixed3"),
        },
        residual=complement_pairs,
    )

    f00 = f_cut_from_bits(F00_BITS)
    f01 = f_cut_from_bits(F01_BITS)
    mix0 = f_cut_from_bits(MIX0_BITS)
    l1_bits = remaining_bits(f_L1)
    ham_bits = remaining_bits(f_hamming)
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis is unbalanced, and evaluates to (1,0,1,1,1)",
        l1_bits == L1_REMAINING
        and remaining_bits(mix0) == MIX0_BITS
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

    f00_one_halt, f00_one_hist = run_locks(f00, ONE_SITE)
    f01_one_halt, f01_one_hist = run_locks(f01, ONE_SITE)
    checks.check(
        "thm1-one-site-agree",
        "both vertex3=0 k=4 maps fill from (0,0,0) with history (1, 4, 8, 10, 11, 12)",
        f00_one_halt == 12
        and f01_one_halt == 12
        and f00_one_hist == ONE_SITE_HISTORY
        and f01_one_hist == ONE_SITE_HISTORY
        and f00_one_hist == f01_one_hist
        and fills_from_seed(f00, ONE_SITE)
        and fills_from_seed(f01, ONE_SITE),
        residual=(f00_one_hist, f01_one_hist),
    )

    mix0_s_halt, mix0_s_hist = run_locks(mix0, SEED_S)
    l1_s_halt, l1_s_hist = run_locks(f_L1, SEED_S)
    checks.check(
        "thm1-S-splits-mix0-L1",
        "S splits mix0/L1: L1 fills with (3, 8, 11, 12) and mix0 halts unfilled at (3, 8, 10)",
        l1_s_halt == 12
        and mix0_s_halt == 10
        and l1_s_hist == L1_S_HISTORY
        and mix0_s_hist == MIX0_S_HISTORY
        and fills_from_seed(f_L1, SEED_S)
        and not fills_from_seed(mix0, SEED_S)
        and mix0_s_hist != l1_s_hist,
        residual=(mix0_s_hist, l1_s_hist),
    )

    f00_s_halt, f00_s_hist = run_locks(f00, SEED_S)
    f01_s_halt, f01_s_hist = run_locks(f01, SEED_S)
    equality_bit = int(f00_s_hist == f01_s_hist)
    print(f"f00_one_site_history={f00_one_hist}")
    print(f"f01_one_site_history={f01_one_hist}")
    print(f"mix0_S_history={mix0_s_hist} fill={mix0_s_halt == 12}")
    print(f"L1_S_history={l1_s_hist} fill={l1_s_halt == 12}")
    print(f"f00_S_history={f00_s_hist} fill={f00_s_halt == 12}")
    print(f"f01_S_history={f01_s_hist} fill={f01_s_halt == 12}")
    print(f"equality_bit={equality_bit}")

    checks.check(
        "thm2-f00-from-S",
        "f00=(1,1,1,0,0) fills from S with history (3, 9, 11, 12)",
        f00_s_halt == 12
        and f00_s_hist == F00_S_HISTORY
        and fills_from_seed(f00, SEED_S),
        residual=(f00_s_halt, f00_s_hist),
    )
    checks.check(
        "thm2-f01-from-S",
        "f01=(1,1,1,0,1) fills from S with history (3, 9, 12)",
        f01_s_halt == 12
        and f01_s_hist == F01_S_HISTORY
        and fills_from_seed(f01, SEED_S),
        residual=(f01_s_halt, f01_s_hist),
    )
    checks.check(
        "thm3-histories-differ",
        "the two S-histories differ; equality bit is 0, not a seed census",
        f00_s_hist != f01_s_hist
        and equality_bit == EQUALITY_BIT == 0
        and f00_s_halt == 12
        and f01_s_halt == 12,
        residual=(f00_s_hist, f01_s_hist, equality_bit),
    )
    checks.check(
        "note-reports-histories",
        "the note reports both S-histories, both fill bits, and equality bit 0",
        "(3, 9, 11, 12)" in note
        and "(3, 9, 12)" in note
        and "(1, 4, 8, 10, 11, 12)" in note
        and "equality bit is `0`" in note
        and "do not have the same lock history" in note,
    )

    claim_scope = (
        "On the two-cube with off-patch o=0 and seed "
        "{(0,0,0),(0,0,1),(2,0,0)}, the F_cut maps (1,1,1,0,0) and "
        "(1,1,1,0,1) do not have the same lock history. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope states the failed history equality and does not adopt mixed3",
        claim_scope in note
        and "Displayed, not adopted" in note
        and "do not adopt" in note.lower(),
    )
    checks.check(
        "lattice-and-admissibility-parents",
        "the live axiom memo supplies Z^3, proper cubic rotations, and a covariant nearest-neighbor rule",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site." in axiom
        and "one fixed nearest-neighbor admissibility rule, covariant under lattice"
        in axiom
        and "A site with no record cannot be read." in axiom,
    )
    checks.check(
        "note-contract",
        "bounded theorem, displayed-not-adopted uniqueness, and machine status",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "target_claim_type: bounded_theorem" in note
        and "trace_class: frontier_discovery" in note
        and "reachability_to_target: advances" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
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
    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
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
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6449-6437",
        "the residual is a new uniqueness on this pair and seed, not leftover of #6449 or #6437",
        "Not leftover-character of #6449" in note
        and "Not leftover-character of #6437" in note
        and "New uniqueness" in note
        and "not a `|S|` census" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt mixed3",
        "no axiom or approved primitive is added" in note
        and "Do not adopt `mixed3`" in note
        and "Do not write `mixed3` into Admissibility" in note,
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
        "per_site: checked exactly — each of the twelve two-cube vertices "
        "uses the same six-direction stencil"
    )
    print(
        "per_mode: checked exactly — independent runs of the two maps from "
        "(0,0,0) and from S"
    )
    print(
        "per_block: checked exactly — the displayed equality bit compares the "
        "two lock histories on this seed"
    )
    print(
        "lattice_wide: checked and not executed — no Z^3-wide formation law "
        "or physical Admissibility selector is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
