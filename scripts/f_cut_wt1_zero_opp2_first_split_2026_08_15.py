#!/usr/bin/env python3
"""Lex-first |S|<=3 fill split of the wt1=0 F_cut pair that differs on opp2.

On the twelve-vertex two-cube with off-patch occupancy 0, the maps with
remaining-bit tuples (0,0,1,1,1) and (0,1,1,1,1) are recomputed members of
Max(11) minus Max(1). The runner enumerates every seed of size at most 3
in increasing cardinality and then lexicographic site order, and reports
the first seed at which those two maps disagree on fill. The opp2 bit is
displayed, not adopted.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "F_CUT_WT1_ZERO_OPP2_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_WT1_ZERO_OPP2_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

SITES = tuple((x, y, z) for x in range(3) for y in range(2) for z in range(2))
SITE_INDEX = {site: index for index, site in enumerate(SITES)}
SITE_SET = frozenset(SITES)
AXES = ((0, 1), (2, 3), (4, 5))
DIRECTIONS = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)

F00 = (0, 0, 1, 1, 1)
F10 = (0, 1, 1, 1, 1)
L1_BITS = (1, 0, 1, 1, 1)
BIT_POS = {"wt1": 0, "opp2": 1, "adj2": 2, "tripod": 3, "ax1": 4}
DISPLAYED_SEED = ((0, 0, 0), (0, 1, 1), (2, 0, 0))


def translate(site: tuple[int, int, int], step: tuple[int, int, int]) -> tuple[int, int, int]:
    return (site[0] + step[0], site[1] + step[1], site[2] + step[2])


def occupancy_cell(site: tuple[int, int, int], locks: set[tuple[int, int, int]]) -> tuple[int, ...]:
    bits = []
    for step in DIRECTIONS:
        neighbor = translate(site, step)
        bits.append(1 if neighbor in SITE_SET and neighbor in locks else 0)
    return tuple(bits)


def cell_weight(cell: tuple[int, ...]) -> int:
    return int(sum(cell))


def has_full_axis(cell: tuple[int, ...]) -> bool:
    return any(cell[left] == 1 and cell[right] == 1 for left, right in AXES)


def orbit_name(cell: tuple[int, ...]) -> str:
    weight = cell_weight(cell)
    if weight == 0:
        return "empty"
    if weight == 6:
        return "full"
    if weight in (1, 5):
        return "wt1"
    if weight in (2, 4):
        probe = cell if weight == 2 else tuple(1 - bit for bit in cell)
        return "opp2" if has_full_axis(probe) else "adj2"
    return "ax1" if has_full_axis(cell) else "tripod"


def some_axis_unbalanced(cell: tuple[int, ...]) -> bool:
    return any(cell[left] != cell[right] for left, right in AXES)


def hamming_parity(cell: tuple[int, ...]) -> int:
    return cell_weight(cell) % 2


def remaining_bits_from_rule(rule) -> tuple[int, int, int, int, int]:
    witnesses = {
        "wt1": (1, 0, 0, 0, 0, 0),
        "opp2": (1, 1, 0, 0, 0, 0),
        "adj2": (1, 0, 1, 0, 0, 0),
        "tripod": (1, 0, 1, 0, 1, 0),
        "ax1": (1, 1, 1, 0, 0, 0),
    }
    return tuple(int(rule(witnesses[name])) for name in ("wt1", "opp2", "adj2", "tripod", "ax1"))


def evaluate(bits: tuple[int, ...], cell: tuple[int, ...]) -> int:
    name = orbit_name(cell)
    if name in ("empty", "full"):
        return 0
    return int(bits[BIT_POS[name]])


def run_map(
    bits: tuple[int, ...], seed: tuple[tuple[int, int, int], ...]
) -> tuple[tuple[int, ...], bool]:
    locks = set(seed)
    history = [len(locks)]
    while True:
        wave = [
            site
            for site in SITES
            if site not in locks and evaluate(bits, occupancy_cell(site, locks)) == 1
        ]
        if not wave:
            break
        locks.update(wave)
        history.append(len(locks))
        if len(history) > len(SITES) + 1:
            raise RuntimeError("formation tick bound exceeded")
    return tuple(history), len(locks) == len(SITES)


def all_fc_maps() -> tuple[tuple[int, int, int, int, int], ...]:
    return tuple(tuple((index >> place) & 1 for place in range(5)) for index in range(32))


def k_site_seeds(k: int) -> tuple[tuple[tuple[int, int, int], ...], ...]:
    return tuple(combinations(SITES, k))


def seeds_upto(k: int) -> tuple[tuple[tuple[int, int, int], ...], ...]:
    return tuple(seed for size in range(k + 1) for seed in k_site_seeds(size))


def coverage(bits: tuple[int, ...], k: int) -> int:
    return sum(1 for seed in k_site_seeds(k) if run_map(bits, seed)[1])


def maximizers(k: int) -> tuple[int, tuple[tuple[int, ...], ...]]:
    scored = tuple((bits, coverage(bits, k)) for bits in all_fc_maps())
    best = max(score for _bits, score in scored)
    return best, tuple(bits for bits, score in scored if score == best)


def first_fill_split(
    left: tuple[int, ...], right: tuple[int, ...], k: int
) -> tuple[tuple[int, int, int], ...] | None:
    for seed in seeds_upto(k):
        if run_map(left, seed)[1] != run_map(right, seed)[1]:
            return seed
    return None


def orbit_census() -> dict[str, int]:
    counts = {
        "empty": 0,
        "full": 0,
        "wt1": 0,
        "opp2": 0,
        "adj2": 0,
        "tripod": 0,
        "ax1": 0,
    }
    for cell in product((0, 1), repeat=6):
        counts[orbit_name(cell)] += 1
    return counts


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; two-cube occupancy ticks only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integer occupancy, lock counts, and coverage")
    print("claim_boundary: displayed first fill split; opp2 is not adopted")

    census = orbit_census()
    l1_from_n = remaining_bits_from_rule(some_axis_unbalanced)
    ham_bits = remaining_bits_from_rule(hamming_parity)
    max1_value, max1_maps = maximizers(1)
    max11_value, max11_maps = maximizers(11)
    extras = tuple(bits for bits in max11_maps if bits not in max1_maps)
    split = first_fill_split(F00, F10, 3)
    hist00, fill00 = run_map(F00, DISPLAYED_SEED)
    hist10, fill10 = run_map(F10, DISPLAYED_SEED)
    small_agree = all(
        run_map(F00, seed)[1] == run_map(F10, seed)[1] for seed in seeds_upto(2)
    )
    earlier_three = tuple(
        seed
        for seed in k_site_seeds(3)
        if seed < DISPLAYED_SEED and run_map(F00, seed)[1] != run_map(F10, seed)[1]
    )
    same_map_split = first_fill_split(F00, F00, 3)

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_WT1_ZERO_OPP2_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "two-cube-order",
        "the two-cube is the lex-ordered 12-site patch {0,1,2}x{0,1}x{0,1}",
        len(SITES) == 12
        and SITES[0] == (0, 0, 0)
        and SITES[3] == (0, 1, 1)
        and SITES[-1] == (2, 1, 1)
        and SITES == tuple(sorted(SITES)),
    )
    checks.check(
        "orbit-partition",
        "the ten cube-rotation orbit types partition the 64 cells",
        census
        == {
            "empty": 1,
            "full": 1,
            "wt1": 12,
            "opp2": 6,
            "adj2": 24,
            "tripod": 8,
            "ax1": 12,
        }
        and sum(census.values()) == 64
        and len(all_fc_maps()) == 32
        and len(set(all_fc_maps())) == 32,
    )
    checks.check(
        "l1-is-n-neq-0",
        "f_L1 is the n=/=0 predicate and is not Hamming parity",
        l1_from_n == L1_BITS
        and ham_bits != L1_BITS
        and ham_bits == (1, 0, 0, 1, 1)
        and evaluate(L1_BITS, (1, 0, 0, 0, 0, 0)) == 1
        and evaluate(L1_BITS, (1, 1, 0, 0, 0, 0)) == 0,
    )
    checks.check(
        "pair-in-fcut",
        "both remaining-bit tuples are F_cut maps and differ only on opp2",
        F00 in all_fc_maps()
        and F10 in all_fc_maps()
        and F00[0] == 0
        and F10[0] == 0
        and F00[1] == 0
        and F10[1] == 1
        and F00[2:] == (1, 1, 1)
        and F10[2:] == (1, 1, 1),
    )
    checks.check(
        "thm1-max11",
        "both maps attain the Max(11) coverage 12",
        max11_value == 12
        and F00 in max11_maps
        and F10 in max11_maps
        and coverage(F00, 11) == 12
        and coverage(F10, 11) == 12,
    )
    checks.check(
        "thm1-not-max1",
        "neither map is in Max(1)",
        max1_value == 12
        and F00 not in max1_maps
        and F10 not in max1_maps
        and coverage(F00, 1) == 0
        and coverage(F10, 1) == 0
        and L1_BITS in max1_maps,
    )
    checks.check(
        "thm1-extras",
        "the pair sits in the four-element Max(11) minus Max(1) set",
        len(extras) == 4
        and F00 in extras
        and F10 in extras
        and set(extras)
        == {
            (0, 0, 1, 1, 0),
            (0, 0, 1, 1, 1),
            (0, 1, 1, 1, 0),
            (0, 1, 1, 1, 1),
        },
    )
    checks.check(
        "thm2-small-seeds-agree",
        "every seed of size at most 2 has the same fill bit on both maps",
        small_agree and len(seeds_upto(2)) == 1 + 12 + 66,
    )
    checks.check(
        "thm2-lex-first-split",
        "the lex-first |S|<=3 fill disagreement is the displayed 3-site seed",
        split == DISPLAYED_SEED
        and earlier_three == ()
        and DISPLAYED_SEED in k_site_seeds(3),
    )
    checks.check(
        "thm3-who-fills",
        "f10 fills the displayed seed and f00 does not",
        fill10 is True
        and fill00 is False
        and hist00 == (3, 5)
        and hist10 == (3, 6, 8, 11, 12),
    )
    checks.check(
        "mutation-same-map-has-no-split",
        "a map does not disagree with itself on any |S|<=3 seed",
        same_map_split is None,
    )
    checks.check(
        "mutation-hamming-is-not-l1",
        "Hamming parity is a different remaining-bit tuple from n=/=0",
        ham_bits != L1_BITS
        and ham_bits != F00
        and ham_bits != F10
        and run_map(ham_bits, ((0, 0, 0),))[1] is False
        and run_map(L1_BITS, ((0, 0, 0),))[1] is True,
    )
    checks.check(
        "mutation-swap-who-fills-fails",
        "the swapped fill-bit claim is rejected by the recomputed histories",
        not (fill00 and not fill10),
    )
    checks.check(
        "scope-boundary",
        "the note displays the split and does not adopt opp2",
        "Displayed, not adopted" in note
        and "do not adopt opp2" in note.lower()
        and "no additional\naxiom is proposed" in note
        and "These are scope boundaries, not impossibility" in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded status, frontier trace, and next action are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: frontier_discovery" in note
        and 'next_trace_action: "independent audit of the bounded algebraic claim"'
        in note,
    )
    checks.check(
        "import-boundary-contract",
        "the supplied patch and absent physical bridge are disclosed",
        "## Inputs And Import Boundary" in note
        and "Explicit theorem-domain condition" in note
        and "External empirical or literature inputs:** none" in note
        and "Open physical bridge" in note,
    )
    checks.check(
        "live-record-unread",
        "the live Record unread sentence is quoted without rewrite",
        "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note,
    )
    checks.check(
        "claim-type-and-forbidden",
        "the bounded type is declared and forbidden phrases are absent",
        "**Type:** bounded_theorem" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and ("G_" + "N") not in note
        and ("1/" + "r") not in note
        and ("1/" + "r^2") not in note
        and ("Lattice-" + "named") not in note
        and ("not a " + "TOE") not in note
        and ("import " + "qcd") not in self_source.lower()
        and ("from " + "qcd") not in self_source.lower(),
    )
    checks.check(
        "claim-scope-literal",
        "the note claim_scope reports the lex-first fill disagreement",
        "lex-first seed of size at most 3 at which F_cut" in note
        and "(0,0,1,1,1) and (0,1,1,1,1) disagree on fill" in note,
    )

    print(f"displayed_seed: {DISPLAYED_SEED}")
    print(f"f00_history: {hist00} fill={fill00}")
    print(f"f10_history: {hist10} fill={fill10}")
    print(f"max1_value: {max1_value} max1_count: {len(max1_maps)}")
    print(f"max11_value: {max11_value} max11_count: {len(max11_maps)}")
    print(f"max11_minus_max1: {extras}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
