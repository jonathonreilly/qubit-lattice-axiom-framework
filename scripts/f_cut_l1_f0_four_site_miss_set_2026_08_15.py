#!/usr/bin/env python3
"""Compare the four-site miss sets of f_L1 and F_cut (1,1,1,1,0).

Recomputes every unordered 4-subset of the twelve two-cube sites with
off-patch occupancy 0. M_L1 (resp. M_f0) is the set of those seeds from
which f_L1 (resp. f0) does not fill. The claimed object is |M_f0|,
|M_L1 ∩ M_f0|, and the equality bit of the two sets. Seeds are not
listed. No map is adopted. f_L1 is the some-axis-unbalanced (n != 0)
map, not Hamming weight.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "F_CUT_L1_F0_FOUR_SITE_MISS_SET_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/F_CUT_L1_F0_FOUR_SITE_MISS_SET_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Point = tuple[int, int, int]
AXES: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Point, ...] = tuple(
    (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
)
SITE_SET = frozenset(SITES)
N_FOUR_SEEDS = 495
N_MISS_L1 = 6
N_MISS_F0 = 36
N_INTER = 4
EQUALITY_BIT = 0
F0_BITS: tuple[int, ...] = (1, 1, 1, 1, 0)
F1_BITS: tuple[int, ...] = (1, 1, 1, 1, 1)
L1_BITS: tuple[int, ...] = (1, 0, 1, 1, 1)
REMAINING_INDEX: dict[tuple[int, int, int], int] = {
    (1, 0, 2): 0,
    (1, 2, 0): 0,
    (0, 1, 2): 1,
    (0, 2, 1): 1,
    (2, 0, 1): 2,
    (2, 1, 0): 2,
    (3, 0, 0): 3,
    (1, 1, 1): 4,
}


def normalize(text: str) -> str:
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def occupancy(site: Point, locked: frozenset[Point]) -> int:
    """On-patch occupancy is the lock bit; off-patch occupancy is 0."""
    if site not in SITE_SET:
        return 0
    return 1 if site in locked else 0


def axis_type(site: Point, locked: frozenset[Point]) -> tuple[int, int, int]:
    """Return (n_unbalanced, n_both, n_empty) for the three cubic axes."""
    n_unbalanced = n_both = n_empty = 0
    for axis in AXES:
        plus = occupancy(add(site, axis), locked)
        minus = occupancy(add(site, (-axis[0], -axis[1], -axis[2])), locked)
        if plus == minus == 0:
            n_empty += 1
        elif plus == minus == 1:
            n_both += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def fire_l1(counts: tuple[int, int, int]) -> bool:
    """f_L1: some axis is unbalanced (n != 0). Not Hamming weight."""
    n_unbalanced, _n_both, _n_empty = counts
    return n_unbalanced != 0


def fire_bits(counts: tuple[int, int, int], bits: tuple[int, ...]) -> bool:
    """F_cut remaining-bit evaluation. Empty and full never fire."""
    if counts in ((0, 0, 3), (0, 3, 0)):
        return False
    index = REMAINING_INDEX.get(counts)
    if index is None:
        raise RuntimeError(f"axis type {counts} is outside F_cut remaining types")
    return bits[index] == 1


def fire_hamming(site: Point, locked: frozenset[Point]) -> bool:
    weight = 0
    for axis in AXES:
        weight += occupancy(add(site, axis), locked)
        weight += occupancy(add(site, (-axis[0], -axis[1], -axis[2])), locked)
    return weight % 2 == 1


def run_map(
    seed: frozenset[Point], predicate
) -> tuple[tuple[int, ...], bool]:
    locked = frozenset(seed)
    history = [len(locked)]
    for _tick in range(len(SITES)):
        ready = [
            site
            for site in SITES
            if site not in locked and predicate(axis_type(site, locked))
        ]
        if not ready:
            break
        locked = locked.union(ready)
        history.append(len(locked))
    return (tuple(history), len(locked) == len(SITES))


def miss_set(predicate) -> tuple[int, frozenset[frozenset[Point]]]:
    seeds = tuple(frozenset(combo) for combo in combinations(SITES, 4))
    misses = [
        seed for seed in seeds if not run_map(seed, predicate)[1]
    ]
    return (len(seeds) - len(misses), frozenset(misses))


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
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: exhaustive four-site lock-step census under f_L1 and f0; set cardinals only")
    print("negative_scope: |M_f0|, |M_L1 ∩ M_f0|, and the equality bit are displayed; no seed is listed and no map is adopted")
    print("cache_write: false")

    checks.check(
        "audit-inputs",
        "the two declared source-bound inputs exist as static literals",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_L1_F0_FOUR_SITE_MISS_SET_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_L1_F0_FOUR_SITE_MISS_SET_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ')' in self_source,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    formation_boundary = "does not supply the formation site, probability, or rate"

    checks.check("source-lattice", "current cubic nearest-neighbor wording is pinned", lattice_sentence in normalized_axiom and lattice_sentence in note)
    checks.check("source-admissibility", "current local-distribution wording is pinned", admissibility_sentence in normalized_axiom and admissibility_sentence in note)
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )

    checks.check(
        "two-cube-cardinality",
        "the two-cube is exactly the twelve sites {0,1,2} x {0,1} x {0,1}",
        len(SITES) == 12 and len(SITE_SET) == 12 and SITES[0] == (0, 0, 0) and SITES[-1] == (2, 1, 1),
    )
    checks.check(
        "four-seed-count",
        "there are C(12,4)=495 unordered four-site seeds",
        len(tuple(combinations(SITES, 4))) == N_FOUR_SEEDS,
    )

    cov_l1, misses_l1 = miss_set(fire_l1)
    cov_f0, misses_f0 = miss_set(lambda counts: fire_bits(counts, F0_BITS))
    cov_f1, misses_f1 = miss_set(lambda counts: fire_bits(counts, F1_BITS))
    intersection = misses_l1 & misses_f0
    equality_bit = int(misses_l1 == misses_f0)

    print(
        f"census: |M_L1|={len(misses_l1)} |M_f0|={len(misses_f0)} "
        f"|intersection|={len(intersection)} equality_bit={equality_bit} "
        f"cov4(L1)={cov_l1} cov4(f0)={cov_f0} cov4(f1)={cov_f1}"
    )

    checks.check(
        "theorem-1-reconfirm-m-l1",
        "|M_L1|=6 and cov4(L1)=489 among the 495 four-site seeds",
        cov_l1 + len(misses_l1) == N_FOUR_SEEDS
        and len(misses_l1) == N_MISS_L1
        and cov_l1 == N_FOUR_SEEDS - N_MISS_L1
        and "|M_L1| = 6" in note,
        residual=(cov_l1, len(misses_l1)),
    )
    checks.check(
        "theorem-1-abs-m-f0",
        "|M_f0|=36 and cov4(f0)=459 among the 495 four-site seeds",
        cov_f0 + len(misses_f0) == N_FOUR_SEEDS
        and len(misses_f0) == N_MISS_F0
        and cov_f0 == N_FOUR_SEEDS - N_MISS_F0
        and "|M_f0| = 36" in note
        and "cov4(f0) = 459" in note,
        residual=(cov_f0, len(misses_f0)),
    )
    checks.check(
        "theorem-1-f1-fills-all",
        "f1 fills every four-site seed, so the f0 misses are exactly mixed3-required seeds",
        cov_f1 == N_FOUR_SEEDS
        and len(misses_f1) == 0
        and "cov4(f1) = 495" in note,
        residual=(cov_f1, len(misses_f1)),
    )

    checks.check(
        "theorem-2-intersection",
        "|M_L1 ∩ M_f0|=4",
        len(intersection) == N_INTER
        and len(misses_l1 - misses_f0) == N_MISS_L1 - N_INTER
        and len(misses_f0 - misses_l1) == N_MISS_F0 - N_INTER
        and "|M_L1 ∩ M_f0| = 4" in note,
        residual=len(intersection),
    )
    checks.check(
        "theorem-2-sets-unequal",
        "M_L1 is not equal to M_f0",
        misses_l1 != misses_f0
        and equality_bit == EQUALITY_BIT
        and "M_L1 ≠ M_f0" in note
        and "not a theorem of `mixed3 = 0`" in normalized_note,
    )

    locked_opp = frozenset(((0, 0, 0), (2, 0, 0)))
    opp2 = axis_type((1, 0, 0), locked_opp)
    hamming_opp = sum(
        occupancy(add((1, 0, 0), shift), locked_opp)
        for shift in AXES + tuple((-a, -b, -c) for a, b, c in AXES)
    )
    locked_mixed = frozenset(((0, 0, 0), (2, 0, 0), (1, 1, 0)))
    mixed3 = axis_type((1, 0, 0), locked_mixed)
    hamming_mixed = sum(
        occupancy(add((1, 0, 0), shift), locked_mixed)
        for shift in AXES + tuple((-a, -b, -c) for a, b, c in AXES)
    )
    checks.check(
        "identity-l1-not-hamming",
        "opp2 has Hamming weight 2 but n_unbalanced=0, so f_L1 does not fire",
        opp2 == (0, 1, 2)
        and hamming_opp == 2
        and not fire_l1(opp2)
        and fire_bits(opp2, F0_BITS)
        and fire_hamming((1, 0, 0), locked_opp) is False
        and "sum(config) % 2" not in self_source.split("def fire_l1", 1)[1].split("def fire_bits", 1)[0],
    )
    checks.check(
        "identity-f0-not-hamming",
        "mixed3 has Hamming weight 3, so Hamming fires it and f0 refuses it",
        mixed3 == (1, 1, 1)
        and hamming_mixed == 3
        and fire_l1(mixed3)
        and not fire_bits(mixed3, F0_BITS)
        and fire_hamming((1, 0, 0), locked_mixed)
        and fire_bits(mixed3, F1_BITS),
    )
    remaining_l1 = tuple(
        int(fire_l1(kind))
        for kind in ((1, 0, 2), (0, 1, 2), (2, 0, 1), (3, 0, 0), (1, 1, 1))
    )
    checks.check(
        "l1-remaining-tuple",
        "n!=0 is exactly the remaining tuple (1,0,1,1,1)",
        remaining_l1 == L1_BITS
        and F0_BITS == (1, 1, 1, 1, 0)
        and "n_unbalanced ≠ 0" in note
        and "(1,0,1,1,1)" in note.replace(" ", ""),
    )

    checks.check(
        "theorem-3-equality-bit",
        "the note displays equality bit 0 and does not adopt a map",
        equality_bit == 0
        and "equality bit is `0`" in normalized_note
        and "displayed, not adopted" in normalized_note.lower()
        and "Do not adopt a map" in note
        and "not written into Admissibility" in normalized_note,
    )
    checks.check(
        "theorem-3-no-seed-list",
        "the note and this runner do not list four-site seeds",
        "{(" not in note
        and "R_adj" not in note
        and "Do not list the seeds" in note
        and "does not print the seeds" in normalized_note
        and "lex representative" not in normalized_note,
    )
    checks.check(
        "not-n-orb-not-leftover",
        "the claimed object is the miss-set comparison, not N_orb and not a leftover table",
        "It is not `N_orb`" in note
        and "not a 6-row leftover table" in normalized_note
        and "Not leftover-character of `#6460`" in normalized_note
        and "unique-max" in normalized_note,
    )

    forbidden = (
        "G_" + "N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice-" + "named",
        "not a " + "TOE",
    )
    checks.check(
        "forbidden-phrases",
        "the note and runner avoid the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "claim-scope",
        "the YAML claim_scope states the miss-set inequality",
        "On the two-cube with off-patch o=0, the 4-site miss set of f_L1 is not equal to the 4-site miss set of F_cut (1,1,1,1,0). Displayed, not adopted."
        in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        "off-patch occupancy is the explicit default `0`" in note
        and "blank-block is a different rule" in note,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "n_unbalanced ≠ 0" in note
        and "not Hamming" in normalized_note
        and "some cubic axis" in normalized_note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
