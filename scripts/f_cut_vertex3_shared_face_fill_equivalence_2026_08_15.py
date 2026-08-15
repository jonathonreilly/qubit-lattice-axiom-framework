#!/usr/bin/env python3
"""Exact F_cut census: fill-from-(1,0,0) versus f(vertex3).

F_cut is the cube-covariant class with f(empty)=f(full)=0 and f(c)=f(1-c).
Dynamics are occupancy-to-lock on the twelve-vertex two-cube with off-patch
occupancy 0. The scored seed is the shared-face 1-site seed (1,0,0).
f_L1 is the unbalanced-axis predicate (some n_mu != 0), never Hamming
|c|_1 mod 2. The failed equivalence is displayed; vertex3 is not adopted.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "F_CUT_VERTEX3_SHARED_FACE_FILL_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_VERTEX3_SHARED_FACE_FILL_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
SEED: tuple[Point, ...] = ((1, 0, 0),)
L1_REMAINING: Bits = (1, 0, 1, 1, 1)
DISPLAYED_COUNTEREXAMPLE: Bits = (0, 0, 0, 1, 0)
FILLERS: tuple[Bits, ...] = (
    (1, 0, 1, 1, 0),
    (1, 0, 1, 1, 1),
    (1, 1, 1, 1, 0),
    (1, 1, 1, 1, 1),
)


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
        "construction: 32 cube-covariant complement-even predicates on the "
        "two-cube, off-patch occupancy 0, seed (1,0,0)"
    )
    print("negative_scope: displayed selector only; vertex3 is not adopted")

    expected_tuple = (
        "AUDIT_INPUT_PATHS = (\n"
        '    "docs/F_CUT_VERTEX3_SHARED_FACE_FILL_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")"
    )
    checks.check(
        "audit-inputs",
        "declared inputs are the required two static string literals and exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_VERTEX3_SHARED_FACE_FILL_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
        "two-cube has twelve vertices and the seed is the shared-face site (1,0,0)",
        len(VERTICES) == 12 == len(set(VERTICES))
        and SEED == ((1, 0, 0),)
        and SEED[0] in VERTICES
        and SEED[0][0] == 1,
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

    f_cut_maps = tuple(product((0, 1), repeat=5))
    checks.check(
        "f-cut-cardinality",
        "five free remaining bits give 32 F_cut maps",
        len(f_cut_maps) == 32,
    )

    l1_bits = remaining_bits(f_L1)
    ham_bits = remaining_bits(f_hamming)
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 is 1 iff some axis is unbalanced, and evaluates to (1,0,1,1,1)",
        l1_bits == L1_REMAINING
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
        "thm1-vertex3",
        "f_L1 has vertex3=1",
        l1_bits[3] == 1,
    )

    l1_halt, l1_hist = run_locks(f_L1, SEED)
    checks.check(
        "thm1-fill",
        "f_L1 fills from (1,0,0) with history (1, 5, 10, 12)",
        l1_halt == 12
        and l1_hist == (1, 5, 10, 12)
        and fills_from_seed(f_L1, SEED),
        residual=(l1_halt, l1_hist),
    )

    rows = []
    for bits in f_cut_maps:
        predicate = f_cut_from_bits(bits)
        filled = fills_from_seed(predicate, SEED)
        v3 = bits[3]
        rows.append((bits, filled, v3))
    n_fill = sum(1 for _bits, filled, _v3 in rows if filled)
    n_v3 = sum(1 for _bits, _filled, v3 in rows if v3 == 1)
    n_both = sum(1 for _bits, filled, v3 in rows if filled and v3 == 1)
    equivalent = all(filled == (v3 == 1) for _bits, filled, v3 in rows)
    counterexamples = [
        (bits, filled, v3) for bits, filled, v3 in rows if filled != (v3 == 1)
    ]
    fillers = sorted(bits for bits, filled, _v3 in rows if filled)
    silent_hold = all(not filled for _bits, filled, v3 in rows if v3 == 0)
    lex_cex = min(counterexamples) if counterexamples else None
    first_neighborhoods = {
        orbit_name(neighborhood(site, {SEED[0]}))
        for site in VERTICES
        if site != SEED[0]
    }

    print(f"N_fill={n_fill}")
    print(f"N_v3={n_v3}")
    print(f"N_both={n_both}")
    print(f"equivalent={equivalent}")
    print(f"lex_counterexample_tuple={None if lex_cex is None else lex_cex[0]}")
    print(f"fillers={fillers}")
    print(f"first_neighborhoods={sorted(first_neighborhoods)}")
    print(f"f_L1_remaining={l1_bits}")
    print(f"f_L1_history={l1_hist}")

    checks.check(
        "thm2-counts",
        "N_fill=4, N_v3=16, N_both=4",
        n_fill == 4 and n_v3 == 16 and n_both == 4,
        residual=(n_fill, n_v3, n_both),
    )
    checks.check(
        "thm2-not-equivalent",
        "fill-from-(1,0,0) is not equivalent to f(vertex3)=1",
        equivalent is False and n_fill != n_v3,
    )
    checks.check(
        "thm2-counterexample",
        "lex-first counterexample is (0,0,0,1,0) with fill=0 and vertex3=1",
        lex_cex == ((0, 0, 0, 1, 0), False, 1)
        and len(counterexamples) == 12
        and not fills_from_seed(f_cut_from_bits(DISPLAYED_COUNTEREXAMPLE), SEED)
        and DISPLAYED_COUNTEREXAMPLE[3] == 1,
        residual=lex_cex,
    )
    checks.check(
        "thm2-one-way",
        "every silent-vertex3 map still has fill=0; all four fillers have vertex3=1",
        silent_hold
        and n_v3 == 16
        and all(bits[3] == 1 for bits in fillers)
        and fillers == sorted(FILLERS),
        residual=fillers,
    )
    checks.check(
        "thm2-first-neighborhoods",
        "first neighborhoods of (1,0,0) are only wt1 or empty, so vertex3 alone cannot grow",
        first_neighborhoods == {"wt1", "empty"}
        and run_locks(f_cut_from_bits(DISPLAYED_COUNTEREXAMPLE), SEED)[0] == 1,
        residual=first_neighborhoods,
    )
    checks.check(
        "thm2-conjunction",
        "fill detects wt1=adj2=vertex3=1, not the single vertex3 bit",
        all(bits[0] == 1 and bits[2] == 1 and bits[3] == 1 for bits in fillers)
        and all(
            (bits[0] == 1 and bits[2] == 1 and bits[3] == 1) == filled
            for bits, filled, _v3 in rows
        ),
    )
    checks.check(
        "note-reports-counts",
        "the note reports N_fill, N_v3, N_both, and the counterexample tuple",
        "N_fill = 4" in note
        and "N_v3 = 16" in note
        and "N_both = 4" in note
        and "(0, 0, 0, 1, 0)" in note
        and "is not equivalent" in note,
    )

    claim_scope = (
        "Among the 32 F_cut maps on the two-cube with off-patch o=0, filling "
        "from the shared-face 1-site seed (1,0,0) is not equivalent to "
        "f(vertex3)=1. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "claim_scope states the failed equivalence and does not adopt vertex3",
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
        "bounded theorem, displayed-not-adopted uniqueness failure, and machine status",
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
        "not-leftover-6448",
        "the residual is the 32-map selector, not leftover-character of #6448",
        "Not leftover-character of #6448" in note
        and "New selector, not leftover of #6448" in note
        and "that listed 1-site misses" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt vertex3",
        "no axiom or approved primitive is added" in note
        and "Do not adopt `vertex3`" in note
        and "Do not write `vertex3` into Admissibility" in note,
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
        and "vertex3" not in axiom,
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
        "per_mode: checked exactly — every F_cut map is scored on the "
        "shared-face seed (1,0,0)"
    )
    print(
        "per_block: checked exactly — N_fill, N_v3, and N_both are the "
        "32-map census on this patch"
    )
    print(
        "lattice_wide: checked and not executed — no Z^3-wide formation law "
        "or physical Admissibility selector is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
