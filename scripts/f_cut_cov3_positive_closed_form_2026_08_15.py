#!/usr/bin/env python3
"""Exact F_cut census: whether cov3>0 is equivalent to P.

P(f) := (wt1=1) and (adj2, vertex3, mixed3) != (0, 0, 0).
New k=3 selector question, not a Max(3) rename. f_L1 is n!=0, not Hamming.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_COV3_POSITIVE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_COV3_POSITIVE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
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
THREE_SITE_SEEDS: tuple[tuple[Point, Point, Point], ...] = tuple(combinations(VERTICES, 3))


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


def selector_p(bits: Bits) -> bool:
    wt1, _opp2, adj2, vertex3, mixed3 = bits
    return wt1 == 1 and (adj2, vertex3, mixed3) != (0, 0, 0)


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


def coverage_of(predicate, seeds) -> int:
    return sum(1 for seed in seeds if fills(predicate, seed))


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

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("external_scientific_inputs: current Lattice, Admissibility, and Record wording; no observations or fits")
    print("construction: 32 F_cut maps on the two-cube, off-patch occupancy 0, 3-site seeds")
    print("negative_scope: displayed selector only; P is not written into Admissibility")

    checks.check(
        "audit-inputs",
        "declared source-bound pair exists",
        len(AUDIT_INPUT_PATHS) == 2
        and AUDIT_TIMEOUT_SEC == 120
        and AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_COV3_POSITIVE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and (
            "AUDIT_INPUT_PATHS = (\n"
            '    "docs/F_CUT_COV3_POSITIVE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
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
        "six-tuples partition into ten orbits with derived sizes",
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
        "three-site-seeds",
        "C(12,3)=220 unordered three-site seeds",
        len(THREE_SITE_SEEDS) == 220
        and len(set(frozenset(seed) for seed in THREE_SITE_SEEDS)) == 220
        and all(len(set(seed)) == 3 for seed in THREE_SITE_SEEDS),
    )
    checks.check(
        "two-site-seeds-control",
        "C(12,2)=66 two-site seeds for the #6494 control",
        len(TWO_SITE_SEEDS) == 66
        and len(set(frozenset(seed) for seed in TWO_SITE_SEEDS)) == 66,
    )

    l1_bits = remaining_bits(f_l1)
    ham_bits = remaining_bits(hamming_parity)
    checks.check(
        "l1-bits",
        "n≠0 evaluates to remaining-bit tuple (1,0,1,1,1) and lies in F_cut",
        l1_bits == (1, 0, 1, 1, 1)
        and f_l1((0, 0, 0, 0, 0, 0)) == 0
        and f_l1((1, 1, 1, 1, 1, 1)) == 0
        and all(f_l1(cell) == f_l1(complement(cell)) for cell in cells)
        and "sum(cell) % 2"
        not in self_source.split("def f_l1", 1)[1].split("def hamming_parity", 1)[0],
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
        cov3 = coverage_of(predicate, THREE_SITE_SEEDS)
        cov2 = coverage_of(predicate, TWO_SITE_SEEDS)
        rows.append((bits, cov2, cov3, selector_p(bits)))

    n_p = sum(1 for _bits, _c2, _c3, flag in rows if flag)
    n_pos = sum(1 for _bits, _c2, cov3, _flag in rows if cov3 > 0)
    n_both = sum(1 for _bits, _c2, cov3, flag in rows if flag and cov3 > 0)
    equivalent = all((cov3 > 0) == flag for _bits, _c2, cov3, flag in rows)
    counterexamples = [(bits, cov3, flag) for bits, _c2, cov3, flag in rows if (cov3 > 0) != flag]
    lex_cex = min(counterexamples) if counterexamples else None
    cov2_matches_p = all((cov2 > 0) == flag for _bits, cov2, _c3, flag in rows)
    n_pos2 = sum(1 for _bits, cov2, _c3, _flag in rows if cov2 > 0)
    n_both2 = sum(1 for _bits, cov2, _c3, flag in rows if flag and cov2 > 0)
    l1_row = next(row for row in rows if row[0] == l1_bits)

    print(f"N_P={n_p}")
    print(f"N_pos={n_pos}")
    print(f"N_both={n_both}")
    print(f"equivalent={equivalent}")
    print(
        "lex_counterexample_tuple: "
        f"{None if lex_cex is None else lex_cex[0]} "
        f"cov3={None if lex_cex is None else lex_cex[1]} "
        f"P={None if lex_cex is None else int(lex_cex[2])}"
    )
    print(f"n_counterexamples={len(counterexamples)}")
    print(f"cov2_iff_P={cov2_matches_p} N_pos2={n_pos2} N_both2={n_both2}")
    print(f"f_L1 remaining={l1_bits} cov2={l1_row[1]} cov3={l1_row[2]} P={int(l1_row[3])}")

    checks.check(
        "p-cardinality",
        "P holds on exactly 14 maps: wt1=1 and (adj2,vertex3,mixed3)!=(0,0,0)",
        n_p == 14
        and n_p == sum(1 for bits in f_cut_maps if selector_p(bits))
        and all(selector_p(bits) == (bits[0] == 1 and bits[2:] != (0, 0, 0)) for bits in f_cut_maps),
        residual=n_p,
    )
    checks.check(
        "control-6494",
        "on the same 32 maps, cov2>0 iff P (investment #6494)",
        cov2_matches_p and n_p == 14 and n_pos2 == 14 and n_both2 == 14,
        residual=(n_pos2, n_both2),
    )
    checks.check(
        "theorem1-not-equivalent",
        "cov3>0 is not equivalent to P among the 32",
        equivalent is False and len(counterexamples) >= 1,
        residual=len(counterexamples),
    )
    checks.check(
        "theorem1-counterexample",
        "lex-first counterexample is (0, 0, 1, 1, 0) with cov3=24 and P=0",
        lex_cex == ((0, 0, 1, 1, 0), 24, False),
        residual=lex_cex,
    )
    checks.check(
        "theorem2-counts",
        "N_P=14, N_pos=20, N_both=13",
        n_p == 14 and n_pos == 20 and n_both == 13,
        residual=(n_p, n_pos, n_both),
    )
    checks.check(
        "l1-positive-control",
        "f_L1 has P=1 and fills every 3-site seed",
        l1_bits[0] == 1
        and selector_p(l1_bits)
        and l1_row[2] == 220
        and l1_row[1] == 62,
    )

    forbidden = ("G_" + "N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "note-scope",
        "note reports the failed equivalence, displays a counterexample, and does not adopt P",
        "is not equivalent" in note
        and "(0, 0, 1, 1, 0)" in note
        and "N_P = 14" in note
        and "N_pos = 20" in note
        and "N_both = 13" in note
        and "Displayed, not adopted" in note
        and "Do not adopt `P`" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and all(token not in note for token in forbidden),
    )
    checks.check(
        "claim-scope",
        "claim_scope states the failed cov3>0 versus P equivalence",
        "Among the 32 F_cut maps on the two-cube" in note
        and "off-patch o=0" in note
        and "positive 3-site coverage is not equivalent to P" in note
        and "Displayed, not adopted" in note,
    )
    checks.check(
        "not-leftover",
        "new k, new selector, not leftover of #6494 and not a Max(3) rename",
        "Not leftover-character of #6494" in note
        and "Not a Max(3)" in note
        and "New `k`" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change and does not adopt P",
        "Do not write P into Admissibility" in note
        and "no axiom or approved primitive is added" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in normalize(note)
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy `0`" in note and "blank-block is a different rule" in note,
    )
    checks.check(
        "claim-type-and-gate",
        "N1-N8 and a passing no-go disposition are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6,
    )
    checks.check(
        "forbidden-phrases-absent",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    print("per_element: checked exactly — each of the 32 remaining-bit tuples is scored")
    print("per_site: checked exactly — each of the twelve two-cube vertices uses the same six-direction stencil")
    print("per_mode: checked exactly — cov3>0 is compared with P on every F_cut map")
    print("per_block: checked exactly — N_P, N_pos, N_both are the F_cut selector-census triple on this patch")
    print("lattice_wide: checked and not executed — no Z^3-wide formation law or physical Admissibility selector is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
