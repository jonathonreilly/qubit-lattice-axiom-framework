#!/usr/bin/env python3
"""Exact F_cut census: filling the four long-axis 2-site seeds vs f(opp2)."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_OPP2_LONG_AXIS_FILL_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_OPP2_LONG_AXIS_FILL_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
PATCH = frozenset(VERTICES)
LONG_AXIS_SEEDS: tuple[tuple[Point, Point], ...] = (
    ((0, 0, 0), (2, 0, 0)),
    ((0, 0, 1), (2, 0, 1)),
    ((0, 1, 0), (2, 1, 0)),
    ((0, 1, 1), (2, 1, 1)),
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


def k_of(predicate) -> int:
    return sum(1 for seed in LONG_AXIS_SEEDS if fills(predicate, seed))


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
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("external_scientific_inputs: current Lattice, Admissibility, and Record wording; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo")
    print("construction: 32 cube-covariant complement-even predicates on the two-cube, off-patch occupancy 0")
    print("negative_scope: displayed selector only; opp2 is not written into Admissibility")

    checks.check(
        "audit-inputs",
        "declared source-bound pair exists",
        len(AUDIT_INPUT_PATHS) == 2
        and AUDIT_TIMEOUT_SEC == 120
        and AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_OPP2_LONG_AXIS_FILL_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
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

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalize(axiom) and lattice_sentence in note)
    checks.check("source-admissibility", "current local-distribution wording is pinned", admissibility_sentence in normalize(axiom) and admissibility_sentence in note)
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
    complement_pairs = {
        (orbit_name(cell), orbit_name(complement(cell)))
        for cell in cells
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
    checks.check("f-cut-cardinality", "five free remaining bits give 32 F_cut maps", len(f_cut_maps) == 32)

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
    checks.check("theorem1-opp2", "f_L1(opp2)=0", l1_bits[1] == 0)

    l1_k = k_of(f_l1)
    l1_histories = tuple(run_locks(f_l1, seed) for seed in LONG_AXIS_SEEDS)
    checks.check(
        "theorem1-k",
        "f_L1 has k=0 and halt lock-count 8 on each long-axis seed",
        l1_k == 0 and all(halt == 8 and history == (2, 6, 8) for halt, history in l1_histories),
        residual=(l1_k, l1_histories),
    )
    onesite_halt, onesite_hist = run_locks(f_l1, ((0, 0, 0),))
    checks.check(
        "l1-onesite-control",
        "same predicate fills from a 1-site seed",
        onesite_halt == 12 and onesite_hist == (1, 4, 8, 11, 12),
        residual=(onesite_halt, onesite_hist),
    )

    rows = []
    for bits in f_cut_maps:
        predicate = f_cut_from_bits(bits)
        kk = k_of(predicate)
        rows.append((bits, kk, bits[1]))
    k_eq_4_iff_opp = all((kk == 4) == (opp == 1) for _bits, kk, opp in rows)
    k_eq_0_iff_silent = all((kk == 0) == (opp == 0) for _bits, kk, opp in rows)
    counterexamples = [(bits, kk) for bits, kk, opp in rows if (kk == 4) != (opp == 1)]
    silent_hold = all(kk == 0 for _bits, kk, opp in rows if opp == 0)
    k_values = Counter(kk for _bits, kk, _opp in rows)
    k4_maps = [bits for bits, kk, _opp in rows if kk == 4]
    lex_cex = min(counterexamples)

    print(f"k_eq_4_iff_f_opp2: {k_eq_4_iff_opp}")
    print(f"k_eq_0_iff_f_opp2_silent: {k_eq_0_iff_silent}")
    print(f"lex_counterexample_tuple: {lex_cex[0]} k={lex_cex[1]}")
    print(f"k_spectrum: {dict(sorted(k_values.items()))}")
    print(f"k4_maps: {k4_maps}")

    checks.check("theorem2-iff-k4", "k(f)=4 is not equivalent to f(opp2)=1", k_eq_4_iff_opp is False)
    checks.check("theorem2-iff-k0", "k(f)=0 is not equivalent to f(opp2)=0", k_eq_0_iff_silent is False)
    checks.check(
        "theorem2-counterexample",
        "lex-first counterexample is (0,1,0,0,0) with k=0 and f(opp2)=1",
        lex_cex == ((0, 1, 0, 0, 0), 0) and len(counterexamples) == 12,
        residual=lex_cex,
    )
    checks.check(
        "silent-one-way",
        "every silent-opp2 map still has k=0 (one direction holds)",
        silent_hold and sum(1 for _bits, _kk, opp in rows if opp == 0) == 16,
    )
    checks.check(
        "k4-characterization",
        "k=4 exactly on the four maps with (wt1,opp2,adj2)=(1,1,1)",
        k4_maps == [(1, 1, 1, 0, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1)]
        and set(k_values) == {0, 4},
        residual=k4_maps,
    )
    checks.check(
        "mutation-zero-and-fullbits",
        "zero map has k=0; remaining-bit (1,1,1,1,1) has k=4",
        k_of(f_cut_from_bits((0, 0, 0, 0, 0))) == 0
        and k_of(f_cut_from_bits((1, 1, 1, 1, 1))) == 4,
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "note-scope",
        "note reports the failed equivalence, displays a counterexample, and does not adopt opp2",
        "is not equivalent" in note
        and "(0, 1, 0, 0, 0)" in note
        and "Displayed, not adopted" in note
        and "hypothetical_axiom_status: \"no edit\"" in note
        and all(token not in note for token in forbidden),
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
