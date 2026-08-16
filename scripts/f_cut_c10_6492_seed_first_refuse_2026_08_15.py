#!/usr/bin/env python3
"""First refused neighborhood of F_cut (1,1,0,0,0) on the #6492 seed.

Two-cube, off-patch occupancy 0. Seed S = {(0,0,0),(1,1,1),(2,0,0)}.
f10 is the F_cut remaining-bit map (1,1,0,0,0). The filling run is
recomputed; remaining-bit neighborhoods of unlocked sites are listed in
tick then lex-site order; the first refused event is reported, or
N_refuse=0 if every appearing remaining-bit orbit is accepted. Displayed,
not adopted. f_L1 is n!=0, not Hamming. No axiom edit, no cache write,
no network, no citation manifest.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/F_CUT_C10_6492_SEED_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/F_CUT_C10_6492_SEED_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Site = tuple[int, int, int]
Bits = tuple[int, int, int, int, int]
Config = tuple[int, ...]

AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SITES: tuple[Site, ...] = tuple(
    (x, y, z) for x in range(3) for y in range(2) for z in range(2)
)
SITE_SET = frozenset(SITES)
SEED: tuple[Site, ...] = ((0, 0, 0), (1, 1, 1), (2, 0, 0))

# Remaining F_cut bits in the order (wt1, opp2, adj2, vertex3, mixed3).
F10: Bits = (1, 1, 0, 0, 0)
F00: Bits = (1, 0, 0, 0, 0)
F_L1: Bits = (1, 0, 1, 1, 1)
HAMMING: Bits = (1, 0, 0, 1, 1)

FORBIDDEN = (
    "G_" + "N",
    "1/" + "r",
    "1/" + "r^2",
    "Lattice-" + "named",
    "not a " + "TOE",
)

CLAIM_SCOPE = (
    "On the two-cube with off-patch o=0, the first refused neighborhood of "
    "F_cut (1,1,0,0,0) on the #6492 seed {(0,0,0),(1,1,1),(2,0,0)} is "
    "reported, or the run refuses none. Displayed, not adopted."
)


def add(left: Site, right: Site) -> Site:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def occupancy_tuple(site: Site, locked: frozenset[Site]) -> Config:
    bits: list[int] = []
    for axis in AXES:
        plus = add(site, axis)
        minus = add(site, (-axis[0], -axis[1], -axis[2]))
        bits.append(int(plus in locked))
        bits.append(int(minus in locked))
    return tuple(bits)


def axis_pairs(cell: Config) -> tuple[tuple[int, int], ...]:
    return ((cell[0], cell[1]), (cell[2], cell[3]), (cell[4], cell[5]))


def orbit_name(cell: Config) -> str:
    pairs = axis_pairs(cell)
    weight = sum(cell)
    both = sum(1 for a, b in pairs if a == 1 and b == 1)
    unbalanced = sum(1 for a, b in pairs if a != b)
    if weight == 0:
        return "empty"
    if weight == 6:
        return "full"
    if weight == 1:
        return "wt1"
    if weight == 5:
        return "wt1_comp"
    if weight == 2 and both == 1:
        return "opp2"
    if weight == 2 and unbalanced == 2:
        return "adj2"
    if weight == 4 and both == 2:
        return "opp2_comp"
    if weight == 4:
        return "adj2_comp"
    if weight == 3 and both == 1:
        return "mixed3"
    if weight == 3 and unbalanced == 3:
        return "vertex3"
    raise ValueError(f"unclassified cell {cell}")


def remaining_family(name: str) -> str | None:
    if name in ("empty", "full"):
        return None
    if name in ("wt1", "wt1_comp"):
        return "wt1"
    if name in ("opp2", "opp2_comp"):
        return "opp2"
    if name in ("adj2", "adj2_comp"):
        return "adj2"
    if name == "vertex3":
        return "vertex3"
    if name == "mixed3":
        return "mixed3"
    raise ValueError(name)


def n_neq_0(cell: Config) -> int:
    return int(any(a != b for a, b in axis_pairs(cell)))


def hamming_parity(cell: Config) -> int:
    return sum(cell) % 2


def eval_bits(bits: Bits, cell: Config) -> int:
    family = remaining_family(orbit_name(cell))
    if family is None:
        return 0
    index = ("wt1", "opp2", "adj2", "vertex3", "mixed3").index(family)
    return bits[index]


def all_cells() -> tuple[Config, ...]:
    return tuple(tuple((n >> k) & 1 for k in range(6)) for n in range(64))


def proper_cube_rotations() -> tuple[tuple[int, ...], ...]:
    images: list[tuple[int, ...]] = []
    for perm in permutations(range(3)):
        parity = 0
        seen = list(perm)
        for i in range(3):
            while seen[i] != i:
                j = seen[i]
                seen[i], seen[j] = seen[j], seen[i]
                parity += 1
        for signs in product((-1, 1), repeat=3):
            if (parity + sum(1 for s in signs if s < 0)) % 2 != 0:
                continue
            image = [0] * 6
            for axis in range(3):
                for sign_bit, sign in ((0, 1), (1, -1)):
                    src = 2 * axis + sign_bit
                    new_axis = perm[axis]
                    new_sign = sign * signs[axis]
                    image[src] = 2 * new_axis + (0 if new_sign == 1 else 1)
            images.append(tuple(image))
    return tuple(images)


def apply_perm(cell: Config, perm: tuple[int, ...]) -> Config:
    out = [0] * 6
    for src, dst in enumerate(perm):
        out[dst] = cell[src]
    return tuple(out)


def rotation_orbits() -> dict[Config, frozenset[Config]]:
    rots = proper_cube_rotations()
    seen: set[Config] = set()
    orbits: dict[Config, frozenset[Config]] = {}
    for cell in all_cells():
        if cell in seen:
            continue
        orbit = frozenset(apply_perm(cell, rot) for rot in rots)
        seen.update(orbit)
        orbits[min(orbit)] = orbit
    return orbits


def normalize(text: str) -> str:
    return " ".join(text.split())


def remaining_bits_from_rule(rule) -> Bits:
    assignment: dict[str, int] = {}
    for cell in all_cells():
        family = remaining_family(orbit_name(cell))
        value = int(rule(cell))
        key = "empty" if family is None and sum(cell) == 0 else (
            "full" if family is None else family
        )
        if key in assignment and assignment[key] != value:
            raise RuntimeError("rule is not cube-covariant")
        assignment[key] = value
    if assignment["empty"] != 0 or assignment["full"] != 0:
        raise RuntimeError("rule is not in F_cut")
    bits = (
        assignment["wt1"],
        assignment["opp2"],
        assignment["adj2"],
        assignment["vertex3"],
        assignment["mixed3"],
    )
    return bits


def run_map(bits: Bits, seed: tuple[Site, ...]) -> tuple[tuple[int, ...], tuple[frozenset[Site], ...]]:
    locked = frozenset(seed)
    counts = [len(locked)]
    layers = [locked]
    for _ in range(12):
        nxt = set(locked)
        for site in SITES:
            if site in locked:
                continue
            if eval_bits(bits, occupancy_tuple(site, locked)) == 1:
                nxt.add(site)
        nxt_f = frozenset(nxt)
        if nxt_f == locked:
            return tuple(counts), tuple(layers)
        locked = nxt_f
        counts.append(len(locked))
        layers.append(locked)
    return tuple(counts), tuple(layers)


def refuse_events(bits: Bits, seed: tuple[Site, ...]) -> list[dict]:
    locked = frozenset(seed)
    events: list[dict] = []
    for tick in range(13):
        for site in SITES:
            if site in locked:
                continue
            cell = occupancy_tuple(site, locked)
            name = orbit_name(cell)
            family = remaining_family(name)
            if family is None:
                continue
            value = eval_bits(bits, cell)
            row = {
                "tick": tick,
                "site": site,
                "cell": cell,
                "orbit": name,
                "family": family,
                "value": value,
            }
            if value == 0:
                events.append(row)
        nxt = set(locked)
        for site in SITES:
            if site in locked:
                continue
            if eval_bits(bits, occupancy_tuple(site, locked)) == 1:
                nxt.add(site)
        nxt_f = frozenset(nxt)
        if nxt_f == locked:
            break
        locked = nxt_f
    return events


def appearing_families(bits: Bits, seed: tuple[Site, ...]) -> tuple[str, ...]:
    locked = frozenset(seed)
    seen: list[str] = []
    for _tick in range(13):
        for site in SITES:
            if site in locked:
                continue
            family = remaining_family(orbit_name(occupancy_tuple(site, locked)))
            if family is not None and family not in seen:
                seen.append(family)
        nxt = set(locked)
        for site in SITES:
            if site in locked:
                continue
            if eval_bits(bits, occupancy_tuple(site, locked)) == 1:
                nxt.add(site)
        nxt_f = frozenset(nxt)
        if nxt_f == locked:
            break
        locked = nxt_f
    return tuple(seen)


def unlocked_rows(bits: Bits, seed: tuple[Site, ...]) -> list[dict]:
    locked = frozenset(seed)
    rows: list[dict] = []
    for site in SITES:
        if site in locked:
            continue
        cell = occupancy_tuple(site, locked)
        name = orbit_name(cell)
        rows.append(
            {
                "site": site,
                "cell": cell,
                "orbit": name,
                "family": remaining_family(name),
                "value": eval_bits(bits, cell),
            }
        )
    return rows


def audit_paths_literal(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in node.targets):
            continue
        value = ast.literal_eval(node.value)
        if isinstance(value, tuple) and all(isinstance(item, str) for item in value):
            return value
    return None


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    compact_note = note.replace(" ", "")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("external_scientific_inputs: none; two-cube occupancy ticks only")
    print("explicit_bounded_inputs: the twelve-vertex two-cube, off-patch occupancy 0")
    print(
        "framework_context: Lattice supplies Z^3 nearest-neighbor adjacency; "
        "Record supplies permanence of a formed lock; no map is written into "
        "Admissibility"
    )
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact integer occupancy, lock counts, and refuse events")
    print("claim_boundary: displayed first refuse or N_refuse=0; no bit is adopted")
    print("negative_scope: neither the map nor any remaining bit is adopted")

    literal = audit_paths_literal(source)
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        literal == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "docs/F_CUT_C10_6492_SEED_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and AUDIT_TIMEOUT_SEC == 120
        and 'AUDIT_INPUT_PATHS = (\n'
        '    "docs/F_CUT_C10_6492_SEED_FIRST_REFUSE_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n'
        '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
        ")" in source,
    )

    checks.check(
        "source-lattice",
        "the axiom memo names Z^3 sites with nearest-neighbor adjacency",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom,
    )
    checks.check(
        "source-record",
        "the axiom memo states that a formed record locks one admissible possibility",
        "When present, a record locks exactly one admissible local possibility."
        in axiom,
    )

    rots = proper_cube_rotations()
    orbits = rotation_orbits()
    named = {orbit_name(cell) for cell in all_cells()}
    checks.check(
        "ten-orbits",
        "the 24 proper cube rotations partition the 64 cells into 10 orbits",
        len(rots) == 24
        and len(orbits) == 10
        and len(named) == 10
        and len(SITES) == 12
        and SITES[0] == (0, 0, 0)
        and SITES[-1] == (2, 1, 1)
        and SITES == tuple(sorted(SITES))
        and SEED[0] in SITE_SET
        and set(SEED) <= SITE_SET,
    )

    l1_from_n = remaining_bits_from_rule(n_neq_0)
    ham_bits = remaining_bits_from_rule(hamming_parity)
    checks.check(
        "l1-is-n-neq-0",
        "f_L1 equals some-axis-unbalanced and is not Hamming parity",
        l1_from_n == F_L1
        and ham_bits != F_L1
        and ham_bits == HAMMING
        and eval_bits(F_L1, (1, 0, 0, 0, 0, 0)) == 1
        and eval_bits(F_L1, (1, 1, 0, 0, 0, 0)) == 0
        and "sum(cell) % 2"
        not in source.split("def n_neq_0", 1)[1].split("def hamming_parity", 1)[0],
    )
    checks.check(
        "f10-remaining-bits",
        "f10 is the F_cut remaining-bit tuple (1,1,0,0,0)",
        F10 == (1, 1, 0, 0, 0)
        and eval_bits(F10, (1, 0, 0, 0, 0, 0)) == 1
        and eval_bits(F10, (1, 1, 0, 0, 0, 0)) == 1
        and eval_bits(F10, (1, 0, 1, 0, 0, 0)) == 0
        and eval_bits(F10, (1, 0, 1, 0, 1, 0)) == 0
        and eval_bits(F10, (1, 0, 1, 1, 0, 0)) == 0
        and eval_bits(F10, (0, 0, 0, 0, 0, 0)) == 0
        and eval_bits(F10, (1, 1, 1, 1, 1, 1)) == 0,
    )

    hist10, layers10 = run_map(F10, SEED)
    fill10 = hist10[-1] == 12
    rows0 = unlocked_rows(F10, SEED)
    appears = appearing_families(F10, SEED)
    refuses10 = refuse_events(F10, SEED)
    n_refuse = len(refuses10)
    checks.check(
        "thm1-f10-fills",
        "f10 fills the #6492 seed with history (3, 12) and locks_halt=12",
        fill10 is True
        and hist10 == (3, 12)
        and layers10[-1] == SITE_SET
        and len(SEED) == 3
        and "(3, 12)" in note
        and "locks_halt=12" in note.replace(" ", "")
        and "{(0,0,0),(1,1,1),(2,0,0)}" in compact_note,
    )

    expected_tick0 = {
        (0, 0, 1): ((0, 0, 0, 0, 0, 1), "wt1"),
        (0, 1, 0): ((0, 0, 0, 1, 0, 0), "wt1"),
        (0, 1, 1): ((1, 0, 0, 0, 0, 0), "wt1"),
        (1, 0, 0): ((1, 1, 0, 0, 0, 0), "opp2"),
        (1, 0, 1): ((0, 0, 1, 0, 0, 0), "wt1"),
        (1, 1, 0): ((0, 0, 0, 0, 1, 0), "wt1"),
        (2, 0, 1): ((0, 0, 0, 0, 0, 1), "wt1"),
        (2, 1, 0): ((0, 0, 0, 1, 0, 0), "wt1"),
        (2, 1, 1): ((0, 1, 0, 0, 0, 0), "wt1"),
    }
    tick0_ok = (
        len(rows0) == 9
        and all(row["value"] == 1 for row in rows0)
        and all(
            row["site"] in expected_tick0
            and row["cell"] == expected_tick0[row["site"]][0]
            and row["orbit"] == expected_tick0[row["site"]][1]
            for row in rows0
        )
    )
    checks.check(
        "thm2-n-refuse-zero",
        "no remaining-bit neighborhood is refused, so N_refuse=0",
        n_refuse == 0
        and refuses10 == []
        and tick0_ok
        and "N_refuse = 0" in note
        and "N_refuse=0" in note.replace(" ", ""),
    )
    checks.check(
        "thm2-appearing-accepted",
        "every remaining-bit orbit that appears is accepted",
        appears == ("wt1", "opp2")
        and all(eval_bits(F10, row["cell"]) == 1 for row in rows0)
        and "Every remaining-bit orbit that appears is accepted" in note
        and "`wt1` and `opp2`" in note,
    )

    hist00, _layers00 = run_map(F00, SEED)
    refuses00 = refuse_events(F00, SEED)
    checks.check(
        "thm3-display-not-adopt",
        "the note displays the empty refuse list and refuses adoption",
        "Displayed, not adopted" in note
        and "Do not adopt a bit" in note
        and "Do not write `wt1` or `opp2` into Admissibility" in note_flat
        and "no Admissibility sentence is rewritten" in note,
    )

    checks.check(
        "mutation-hamming-is-not-l1",
        "Hamming parity is a different remaining-bit tuple from n!=0 and from f10",
        ham_bits != F_L1
        and ham_bits != F10
        and ham_bits == HAMMING,
    )
    checks.check(
        "mutation-f00-does-refuse",
        "the opp2-silent sibling from the same seed has a nonempty refuse list",
        hist00 == (3, 11)
        and hist00[-1] != 12
        and len(refuses00) >= 1
        and refuses00[0]["site"] == (1, 0, 0)
        and refuses00[0]["family"] == "opp2"
        and refuses00[0]["tick"] == 0,
    )
    checks.check(
        "mutation-opp2-not-refused-by-f10",
        "the claim that f10 refuses opp2 on this run is false",
        eval_bits(F10, (1, 1, 0, 0, 0, 0)) == 1
        and all(not (row["family"] == "opp2" and row["value"] == 0) for row in rows0),
    )

    checks.check(
        "claim-scope",
        "the note reports the first refuse or that the run refuses none",
        CLAIM_SCOPE in note
        and "Displayed, not adopted." in note
        and "the run refuses none" in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded status, frontier trace, and next action are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: frontier_discovery" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
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
        "live-parent-quotes",
        "the live Lattice and Record unread sentences are quoted without rewrite",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in note
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note
        and "When present, a record locks exactly one admissible local possibility."
        in note
        and "does not supply the formation site, probability, or rate" in axiom_flat
        and "does not supply the formation site, probability, or rate" in note_flat,
    )
    checks.check(
        "l1-definition-in-note",
        "the note defines f_L1 as unbalanced-axis / n != 0 and rejects Hamming",
        "`n_μ = c_{+μ} − c_{-μ}`" in note
        and "This is **not** Hamming parity" in note
        and "`f_L1(c)=1` if and only if some axis is unbalanced" in note,
    )
    checks.check(
        "claim-type-and-forbidden",
        "the bounded type is declared and forbidden phrases are absent",
        "**Type:** bounded_theorem" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and all(token not in note and token not in source for token in FORBIDDEN)
        and ("import " + "qcd") not in source.lower()
        and ("from " + "qcd") not in source.lower(),
    )
    checks.check(
        "no-axiom-edit",
        "the theorem proposes no axiom change",
        "no axiom or approved primitive is added" in note
        and "hypothetical_axiom_status" in note
        and "Do not adopt a bit" in note
        and "F_cut" not in axiom
        and "f_L1" not in axiom
        and "f10" not in axiom,
    )
    checks.check(
        "off-patch-zero",
        "off-patch occupancy is the explicit 0 default, not a blank-block",
        ("off-patch occupancy 0" in note or "off-patch occupancy `0`" in note)
        and "blank-block is a different rule" in note,
    )
    checks.check(
        "not-leftover-6492",
        "the residual is the first refuse, not leftover fill-bit of #6492",
        "Not leftover-character of #6492" in note
        and "not a second copy of the fill bit" in note
        and "New finite object" in note,
    )

    print(f"n_rotations={len(rots)}")
    print(f"n_orbits={len(orbits)}")
    print(f"f10_remaining={F10}")
    print(f"seed={SEED}")
    print(f"f10_history={hist10} fill={fill10}")
    print(f"appearing_families={appears}")
    print(f"N_refuse={n_refuse}")
    print(f"tick0_unlocked={[(row['site'], row['orbit'], row['value']) for row in rows0]}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
