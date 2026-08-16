#!/usr/bin/env python3
"""Lex-first |S|<=3 seed where f_mix0 fills and its wt1=0 sibling does not.

On the two-cube {0,1,2} x {0,1} x {0,1} with off-patch occupancy 0,
f_mix0 is the complement-even cut map with remaining bits
(wt1, opp2, adj2, vertex3, mixed3) = (1,0,1,1,0) and fwt is the
same map with wt1 cleared, (0,0,1,1,0). This runner recomputes
Max(1) among the 32 F_cut maps, searches nonempty seeds of size
at most 3 in lex order, and reports the first seed at which
f_mix0 fills and fwt does not, together with both lock-count
histories. Values are derived, not embedded. f_L1 is n != 0
(some axis unbalanced), never Hamming |c|_1 mod 2.
"""

from __future__ import annotations

import ast
from itertools import combinations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_WT1_ZERO_MIX0_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_WT1_ZERO_MIX0_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

TWO_CUBE = tuple((x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1))
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
MIX0_BITS = (1, 0, 1, 1, 0)
FWT_BITS = (0, 0, 1, 1, 0)
L1_BITS = (1, 0, 1, 1, 1)
F0_BITS = (1, 1, 1, 1, 0)
F1_BITS = (1, 1, 1, 1, 1)
HAMMING_BITS = (1, 0, 0, 1, 1)
ALL_REMAINING = tuple(product((0, 1), repeat=5))


def _add(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def _sub(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def axis_type(
    site: tuple[int, int, int], locked: set[tuple[int, int, int]]
) -> tuple[int, int, int]:
    n_unbalanced = 0
    n_both = 0
    n_empty = 0
    for step in AXES:
        occupied = int(_add(site, step) in locked) + int(_sub(site, step) in locked)
        if occupied == 0:
            n_empty += 1
        elif occupied == 2:
            n_both += 1
        else:
            n_unbalanced += 1
    return (n_unbalanced, n_both, n_empty)


def fires(typ: tuple[int, int, int], bits: tuple[int, int, int, int, int]) -> bool:
    wt1, opp2, adj2, vertex3, mixed3 = bits
    table = {
        (0, 0, 3): 0,
        (0, 3, 0): 0,
        (1, 0, 2): wt1,
        (1, 2, 0): wt1,
        (0, 1, 2): opp2,
        (0, 2, 1): opp2,
        (2, 0, 1): adj2,
        (2, 1, 0): adj2,
        (3, 0, 0): vertex3,
        (1, 1, 1): mixed3,
    }
    return bool(table[typ])


def evolve(
    seed: tuple[tuple[int, int, int], ...], bits: tuple[int, int, int, int, int]
) -> tuple[tuple[int, ...], frozenset[tuple[int, int, int]]]:
    locked = set(seed)
    history = [len(locked)]
    while True:
        ready = [
            site
            for site in TWO_CUBE
            if site not in locked and fires(axis_type(site, locked), bits)
        ]
        if not ready:
            break
        locked.update(ready)
        history.append(len(locked))
        if len(locked) == 12:
            break
    return tuple(history), frozenset(locked)


def filled(seed: tuple[tuple[int, int, int], ...], bits: tuple[int, int, int, int, int]) -> bool:
    return len(evolve(seed, bits)[1]) == 12


def cov1(bits: tuple[int, int, int, int, int]) -> int:
    return sum(1 for site in TWO_CUBE if filled((site,), bits))


def lex_seeds(max_size: int):
    for size in range(1, max_size + 1):
        for seed in combinations(TWO_CUBE, size):
            yield seed


def first_split(
    fill_bits: tuple[int, int, int, int, int],
    miss_bits: tuple[int, int, int, int, int],
    max_size: int = 3,
) -> tuple[tuple[int, int, int], ...] | None:
    for seed in lex_seeds(max_size):
        if filled(seed, fill_bits) and not filled(seed, miss_bits):
            return seed
    return None


def seed_key(seed: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(sorted(seed))


def audit_paths_are_static_literals(source: str) -> bool:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS" for target in node.targets):
            continue
        value = node.value
        if not isinstance(value, ast.Tuple):
            return False
        return all(
            isinstance(element, ast.Constant) and isinstance(element.value, str)
            for element in value.elts
        )
    return False


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

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("external_scientific_inputs: none; two-cube occupancy and cut-map bits only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integer lock counts; no floating-point inputs")
    print("claim_boundary: displayed first-split seed; wt1 is not adopted")

    checks.check("geometry-two-cube", "the two-cube has 12 sites", len(TWO_CUBE) == 12)
    checks.check(
        "geometry-one-site-count",
        "there are exactly 12 one-site seeds",
        len(TWO_CUBE) == 12 and len(set(TWO_CUBE)) == 12,
    )
    n_two = sum(1 for _ in combinations(TWO_CUBE, 2))
    n_three = sum(1 for _ in combinations(TWO_CUBE, 3))
    checks.check(
        "geometry-seed-counts",
        "there are 66 two-site seeds and 220 three-site seeds",
        n_two == 66 and n_three == 220,
    )

    cov1_by_bits = {bits: cov1(bits) for bits in ALL_REMAINING}
    m1 = max(cov1_by_bits.values())
    max1 = tuple(sorted(bits for bits, cov in cov1_by_bits.items() if cov == m1))
    cov1_mix0 = cov1_by_bits[MIX0_BITS]
    cov1_fwt = cov1_by_bits[FWT_BITS]
    print(f"m1={m1}")
    print(f"N_max1={len(max1)}")
    print(f"Max1={max1}")
    print(f"cov1_mix0={cov1_mix0}")
    print(f"cov1_fwt={cov1_fwt}")

    checks.check(
        "thm1-m1-twelve",
        "maximum one-site coverage is m1=12 attained by four maps",
        m1 == 12
        and len(max1) == 4
        and set(max1) == {MIX0_BITS, L1_BITS, F0_BITS, F1_BITS},
    )
    checks.check(
        "thm1-mix0-in-max1",
        "f_mix0=(1,0,1,1,0) is in Max(1)",
        MIX0_BITS in max1 and cov1_mix0 == 12 and all(filled((site,), MIX0_BITS) for site in TWO_CUBE),
    )
    checks.check(
        "thm1-fwt-not-in-max1",
        "fwt=(0,0,1,1,0) is not in Max(1)",
        FWT_BITS not in max1 and cov1_fwt == 0 and cov1_fwt < m1,
    )
    checks.check(
        "thm1-f-L1-is-unbalanced-axis",
        "f_L1 remaining bits fire every type with n_unbalanced>=1",
        L1_BITS == (1, 0, 1, 1, 1) and L1_BITS in max1,
    )
    checks.check(
        "thm1-f-L1-not-hamming",
        "f_L1 is n!=0, not Hamming parity of the six neighbor bits",
        L1_BITS != HAMMING_BITS
        and MIX0_BITS != HAMMING_BITS
        and FWT_BITS != HAMMING_BITS
        and HAMMING_BITS not in max1,
    )

    split = first_split(MIX0_BITS, FWT_BITS, max_size=3)
    if split is None:
        raise RuntimeError("no |S|<=3 seed where mix0 fills and fwt does not")
    hist_mix0, locks_mix0 = evolve(split, MIX0_BITS)
    hist_fwt, locks_fwt = evolve(split, FWT_BITS)
    print(f"S={seed_key(split)}")
    print(f"hist_mix0={hist_mix0}")
    print(f"hist_fwt={hist_fwt}")
    print(f"fill_mix0={len(locks_mix0) == 12}")
    print(f"fill_fwt={len(locks_fwt) == 12}")

    earlier_ok = True
    for seed in lex_seeds(3):
        if seed == split:
            break
        if filled(seed, MIX0_BITS) and not filled(seed, FWT_BITS):
            earlier_ok = False
            break

    checks.check(
        "thm2-first-seed-is-origin",
        "the lex-first |S|<=3 split is the one-site seed {(0,0,0)}",
        split == ((0, 0, 0),) and len(split) == 1,
    )
    checks.check(
        "thm2-direction",
        "f_mix0 fills S and fwt does not",
        len(locks_mix0) == 12 and len(locks_fwt) != 12,
    )
    checks.check(
        "thm2-no-earlier-split",
        "no earlier nonempty |S|<=3 seed splits in that direction",
        earlier_ok,
    )
    checks.check(
        "thm3-histories",
        "lock-count histories are (1,4,8,11,12) and (1)",
        hist_mix0 == (1, 4, 8, 11, 12) and hist_fwt == (1,) and len(locks_fwt) == 1,
    )

    locked0 = set(split)
    first_wave_types = {
        site: axis_type(site, locked0)
        for site in TWO_CUBE
        if site not in locked0 and fires(axis_type(site, locked0), MIX0_BITS)
    }
    checks.check(
        "thm3-first-wave-is-wt1",
        "the first mix0 wave from S is the three wt1 neighbors; fwt is silent",
        first_wave_types
        == {
            (1, 0, 0): (1, 0, 2),
            (0, 1, 0): (1, 0, 2),
            (0, 0, 1): (1, 0, 2),
        }
        and all(not fires(typ, FWT_BITS) for typ in first_wave_types.values()),
    )

    checks.check(
        "mutation-not-l1-or-hamming",
        "f_mix0 is not f_L1 and neither displayed map is Hamming",
        MIX0_BITS != L1_BITS and MIX0_BITS != HAMMING_BITS and FWT_BITS != HAMMING_BITS,
    )
    checks.check(
        "mutation-not-6437-three-site",
        "the first split is not the mix0/L1 three-site splitter",
        seed_key(split) != ((0, 0, 0), (0, 0, 1), (2, 0, 0)),
    )
    checks.check(
        "mutation-pair-differs-only-on-wt1",
        "the displayed pair differs only on the remaining bit wt1",
        MIX0_BITS[0] == 1
        and FWT_BITS[0] == 0
        and MIX0_BITS[1:] == FWT_BITS[1:]
        and MIX0_BITS[1:] == (0, 1, 1, 0),
    )

    forbidden = ("G" + "_N", "1/" + "r", "1/" + "r^2", "Lattice-" + "named", "not a " + "TOE")
    checks.check(
        "forbidden-substrings",
        "the note and runner omit the dispatch-forbidden phrases",
        all(phrase not in note and phrase not in self_source for phrase in forbidden),
    )
    checks.check(
        "display-not-adopt",
        "the note displays S and refuses adoption of wt1",
        "Displayed, not adopted" in note
        and "Do not adopt wt1" in note
        and "S = {(0,0,0)}" in note
        and "(1, 4, 8, 11, 12)" in note
        and "fwt    : (1)" in note,
    )
    checks.check(
        "live-parent-quotes",
        "Lattice, Admissibility, and Record sentences are quoted without rewrite",
        "proper cubic rotations about each site" in axiom
        and "proper cubic rotations about each site" in note
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "one fixed nearest-neighbor admissibility rule" in note
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded-support status and no axiom adoption are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "hypothetical_axiom_status:" in note
        and "no axiom or approved primitive is added" in note
        and "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_WT1_ZERO_MIX0_FIRST_SPLIT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and audit_paths_are_static_literals(self_source)
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "claim-scope-first-split",
        "claim_scope states the lex-first |S|<=3 mix0-fills / fwt-misses seed",
        "lex-first seed of size at most 3" in note
        and "F_cut (1,0,1,1,0) fills and (0,0,1,1,0) does not" in note
        and "Displayed, not adopted" in note
        and "off-patch o=0" in note,
    )
    checks.check(
        "not-leftover-6476-or-6437",
        "the residual is a new pair seed, not leftover-character of #6476 or #6437",
        "not leftover-character of #6476" in note
        and "not leftover-character of #6437" in note,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        ("Off-patch occupancy is `0`" in note or "off-patch occupancy `0`" in note)
        and "blank-block is a different rule" in note,
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "Do not write the ranking into Admissibility" in note
        and "Do not adopt wt1" in note,
    )
    checks.check(
        "scope-not-nogo",
        "the note is a bounded display, not a no-go",
        "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and "These are scope boundaries, not impossibility" in note
        and ("import " + "qcd") not in self_source.lower(),
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`f_L1(c)=1` if and only if some axis is unbalanced" in note
        and "`n_μ = c_{+μ} − c_{-μ}` is nonzero" in note
        and "This is **not** Hamming parity" in note,
    )

    print("per_element: each F_cut remaining-bit tuple is scored by one-site fill")
    print("per_site: occupancy is the two-cube with off-patch o=0; no other patch is used")
    print("per_mode: nonempty seeds of size at most 3 are searched in lex order")
    print("per_block: the first mix0-fills / fwt-misses seed and both histories are the claim")
    print("lattice_wide: checked and not executed — no Z^3-wide selector or adoption")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
