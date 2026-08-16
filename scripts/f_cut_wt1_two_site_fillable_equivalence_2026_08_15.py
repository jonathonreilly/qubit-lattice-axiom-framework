#!/usr/bin/env python3
"""Exact F_cut census: whether cov2>0 is equivalent to f(wt1)=1."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_WT1_TWO_SITE_FILLABLE_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_WT1_TWO_SITE_FILLABLE_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
TWO_SITE_SEEDS: tuple[tuple[Point, Point], ...] = tuple(combinations(VERTICES, 2))


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


def f_l1(cell: Cell) -> int:
    """Formation on a 6-tuple iff some axis is unbalanced (n≠0)."""
    return int(axis_unbalanced(cell))


def hamming_parity(cell: Cell) -> int:
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
    for _ in range(len(VERTICES)):
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


def fills(predicate, seed: tuple[Point, ...]) -> bool:
    halt, _history = run_locks(predicate, seed)
    return halt == len(VERTICES)


def cov2_of(predicate) -> int:
    return sum(1 for seed in TWO_SITE_SEEDS if fills(predicate, seed))


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

    print("external_scientific_inputs: current Lattice, Admissibility, and Record wording; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo")
    print("construction: 32 cube-covariant complement-even predicates on the two-cube, off-patch occupancy 0")
    print("negative_scope: displayed selector only; wt1 is not written into Admissibility")

    checks.check(
        "audit-inputs",
        "declared source-bound pair exists",
        len(AUDIT_INPUT_PATHS) == 2
        and AUDIT_TIMEOUT_SEC == 120
        and AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_WT1_TWO_SITE_FILLABLE_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and (
            "AUDIT_INPUT_PATHS = (\n"
            '    "docs/F_CUT_WT1_TWO_SITE_FILLABLE_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
            '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
            ")"
        )
        in self_source,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"

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
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalize(axiom) for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalize(axiom) and formation_boundary in normalize(note),
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
    checks.check("vertex-count", "two-cube has twelve vertices", len(VERTICES) == 12 == len(set(VERTICES)))
    checks.check(
        "orbit-partition",
        "proper-cube action on six-tuples has ten orbits with derived sizes",
        orbit_counts == expected_counts,
        residual=dict(orbit_counts),
    )
    complement_pairs = {(orbit_name(cell), orbit_name(complement(cell))) for cell in cells}
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
    checks.check("f-cut-cardinality", "five free remaining bits give 32 F_cut maps", len(f_cut_maps) == 32)
    checks.check(
        "two-site-seeds",
        "C(12,2)=66 unordered two-site seeds",
        len(TWO_SITE_SEEDS) == 66
        and len(set(frozenset(seed) for seed in TWO_SITE_SEEDS)) == 66
        and all(len(set(seed)) == 2 for seed in TWO_SITE_SEEDS),
    )

    l1_bits = remaining_bits(f_l1)
    ham_bits = remaining_bits(hamming_parity)
    checks.check(
        "l1-bits",
        "n≠0 evaluates to remaining-bit tuple (1,0,1,1,1) and lies in F_cut",
        l1_bits == (1, 0, 1, 1, 1)
        and f_l1((0, 0, 0, 0, 0, 0)) == 0
        and f_l1((1, 1, 1, 1, 1, 1)) == 0
        and all(f_l1(cell) == f_l1(complement(cell)) for cell in cells),
        residual=l1_bits,
    )
    checks.check(
        "l1-not-hamming",
        "Hamming parity is a different F_cut tuple",
        ham_bits == (1, 0, 0, 1, 1) and ham_bits != l1_bits,
        residual=ham_bits,
    )

    rows = []
    for bits in f_cut_maps:
        predicate = f_cut_from_bits(bits)
        cov = cov2_of(predicate)
        rows.append((bits, cov, bits[0]))

    n_wt1 = sum(1 for _bits, _cov, wt1 in rows if wt1 == 1)
    n_pos = sum(1 for _bits, cov, _wt1 in rows if cov > 0)
    n_both = sum(1 for _bits, cov, wt1 in rows if wt1 == 1 and cov > 0)
    n_wt0 = sum(1 for _bits, _cov, wt1 in rows if wt1 == 0)
    wt0_all_zero = all(cov == 0 for _bits, cov, wt1 in rows if wt1 == 0)
    equivalent = n_wt1 == n_pos == n_both and wt0_all_zero
    counterexamples = [(bits, cov) for bits, cov, wt1 in rows if (wt1 == 1) != (cov > 0)]
    lex_cex = min(counterexamples) if counterexamples else None
    cov_spectrum_wt1 = Counter(cov for _bits, cov, wt1 in rows if wt1 == 1)

    print(f"N_wt1={n_wt1}")
    print(f"N_pos={n_pos}")
    print(f"N_both={n_both}")
    print(f"equivalent={equivalent}")
    print(f"lex_counterexample_tuple: {None if lex_cex is None else lex_cex[0]} cov2={None if lex_cex is None else lex_cex[1]}")
    print(f"wt1_cov2_spectrum: {dict(sorted(cov_spectrum_wt1.items()))}")
    print(f"counterexamples: {counterexamples}")

    checks.check(
        "theorem1-wt1-zero",
        "every wt1=0 map has cov2=0",
        n_wt0 == 16 and wt0_all_zero and all(cov == 0 for _bits, cov, wt1 in rows if wt1 == 0),
    )
    checks.check(
        "theorem2-counts",
        "N_wt1=16, N_pos=14, N_both=14",
        n_wt1 == 16 and n_pos == 14 and n_both == 14,
        residual=(n_wt1, n_pos, n_both),
    )
    checks.check(
        "theorem2-not-equivalent",
        "positive 2-site coverage is not equivalent to f(wt1)=1",
        equivalent is False and len(counterexamples) == 2,
        residual=counterexamples,
    )
    checks.check(
        "theorem2-counterexample",
        "lex-first counterexample is (1, 0, 0, 0, 0) with cov2=0 and f(wt1)=1",
        lex_cex == ((1, 0, 0, 0, 0), 0)
        and counterexamples == [((1, 0, 0, 0, 0), 0), ((1, 1, 0, 0, 0), 0)],
        residual=lex_cex,
    )
    checks.check(
        "l1-positive-control",
        "f_L1 has wt1=1 and cov2=62",
        l1_bits[0] == 1 and cov2_of(f_l1) == 62,
    )
    lex_max_halt = max(run_locks(f_cut_from_bits((1, 0, 0, 0, 0)), seed)[0] for seed in TWO_SITE_SEEDS)
    checks.check(
        "cex-stalls",
        "lex-first counterexample never reaches halt lock-count 12; max halt is 10",
        lex_max_halt == 10,
        residual=lex_max_halt,
    )

    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "note-scope",
        "note reports the failed equivalence, displays a counterexample, and does not adopt wt1",
        "is not equivalent" in note
        and "(1, 0, 0, 0, 0)" in note
        and "N_wt1 = 16" in note
        and "N_pos = 14" in note
        and "N_both = 14" in note
        and "Displayed, not adopted" in note
        and "hypothetical_axiom_status: \"no edit\"" in note
        and all(token not in note for token in forbidden),
    )
    checks.check(
        "claim-scope",
        "claim_scope states the failed cov2>0 versus wt1 equivalence",
        "Among the 32 F_cut maps on the two-cube" in note
        and "off-patch o=0" in note
        and "positive 2-site coverage is not equivalent to f(wt1)=1" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "not-leftover",
        "new selector, not leftover of #6482 or #6429",
        "Not leftover-character of #6482" in note
        and "that only scored the 16" in note
        and "Not leftover-character of #6429" in note
        and "that ranked Max(2)" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt wt1",
        "Do not write the ranking into Admissibility" in note
        or "Do not write wt1 into Admissibility" in note,
    )
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
