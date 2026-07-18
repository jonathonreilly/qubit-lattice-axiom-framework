#!/usr/bin/env python3
"""Cycle 65: independent mixed-context audit of the Cycle-64 transducer.

Cycle 64 fixes the completed Cycle-60 comb in its base.  This audit instead
fixes only the completed Cycle-57 builder and treats every Cycle-60 and
Cycle-64 addition as an independently present/absent local variable.  Since a
nearest-neighbour target has at most six variable neighbours, all local
contexts are exhausted exactly.  This is a composability audit, not a global
reachability claim.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import monotone_phase_transducer_cycle64_scratch_2026_07_14 as c64
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MIXED_LOCAL_CONTEXT_PHASE_CYCLE65_NOTE_2026-07-14.md"
CYCLE60_RUNNER = ROOT / "scripts" / "phase_port_preserving_comb_cycle60_scratch_2026_07_14.py"
CYCLE64_RUNNER = ROOT / "scripts" / "monotone_phase_transducer_cycle64_scratch_2026_07_14.py"
CYCLE60_HASH = "616d57dfd96e614b232f35516dc39399d8841ff43a7b5e30fe29bca5eee896a0"
CYCLE64_HASH = "3f38e97c0a1612145fd26d4964a431bf56662dcad17dd6280fa372e5189d01d3"

Coord = tuple[int, int, int]
Signature = c53.Signature
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


@dataclass(frozen=True)
class BadContext:
    target: Coord
    output: str
    expected: str | None
    present: tuple[Coord, ...]
    signature: Signature
    origin: str


@dataclass(frozen=True)
class MixedAudit:
    base: dict[Coord, str]
    allowed: dict[Coord, str]
    rules: dict[Signature, str]
    canonical_conflicts: tuple[tuple[Signature, str, str], ...]
    raw_outputs: dict[Signature, frozenset[str]]
    candidates: frozenset[Coord]
    local_subsets: int
    matches: int
    matched_rows: frozenset[Signature]
    outputs_by_target: dict[Coord, frozenset[str]]
    bad: tuple[BadContext, ...]


def build_mixed_audit() -> MixedAudit:
    # The completed Cycle-57 builder is the only fixed state.
    base = dict(c60.CONSTRUCTION.base)
    allowed = dict(c60.CONSTRUCTION.allowed)
    for site, output in c64.ALLOWED.items():
        prior = allowed.get(site)
        if prior is not None and prior != output:
            raise ValueError(f"footprint conflict at {site}: {prior} / {output}")
        allowed[site] = output

    rules = dict(c60.CONSTRUCTION.table)
    canonical_conflicts: list[tuple[Signature, str, str]] = []
    for signature, output in c64.RULES.items():
        prior = rules.get(signature)
        if prior is not None and prior != output:
            canonical_conflicts.append((signature, prior, output))
        rules[signature] = output

    raw: dict[Signature, set[str]] = defaultdict(set)
    for signature, output in rules.items():
        for rotation in c53.ROTATIONS:
            raw[c53.rotate_signature(signature, rotation)].add(output)

    occupied = set(base) | set(allowed)
    candidates = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in base
    }

    local_subsets = matches = 0
    matched_rows: set[Signature] = set()
    outputs_by_target: dict[Coord, set[str]] = defaultdict(set)
    bad: list[BadContext] = []
    for target in sorted(candidates):
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in allowed
        )
        for mask in range(1 << len(neighbours)):
            local_subsets += 1
            present = tuple(
                neighbour
                for index, neighbour in enumerate(neighbours)
                if mask & (1 << index)
            )
            records = dict(base)
            records.update({site: allowed[site] for site in present})
            signature = c53.canonical_signature(c53.local_signature(records, target))
            output = rules.get(signature)
            if output is None:
                continue
            matches += 1
            matched_rows.add(signature)
            outputs_by_target[target].add(output)
            expected = allowed.get(target)
            if expected != output:
                origin = "c60" if signature in c60.CONSTRUCTION.table else "c64"
                bad.append(BadContext(target, output, expected, present, signature, origin))

    return MixedAudit(
        base,
        allowed,
        rules,
        tuple(canonical_conflicts),
        {signature: frozenset(outputs) for signature, outputs in raw.items()},
        frozenset(candidates),
        local_subsets,
        matches,
        frozenset(matched_rows),
        {target: frozenset(outputs) for target, outputs in outputs_by_target.items()},
        tuple(bad),
    )


AUDIT = build_mixed_audit()


def witness(
    target: Coord,
    output: str,
    expected: str | None,
    present: tuple[Coord, ...],
) -> bool:
    return any(
        item.target == target
        and item.output == output
        and item.expected == expected
        and item.present == present
        for item in AUDIT.bad
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 Cycle-60 subject hash is frozen", digest(CYCLE60_RUNNER) == CYCLE60_HASH)
    check("A03 Cycle-64 subject hash is frozen", digest(CYCLE64_RUNNER) == CYCLE64_HASH)
    check("A04 fixed Cycle-57 base has 38 records", len(AUDIT.base) == 38)
    check("A05 Cycle-60 contributes 52 variables", len(c60.CONSTRUCTION.allowed) == 52)
    check("A06 Cycle-64 contributes 152 variables", len(c64.ALLOWED) == 152)
    check("A07 the two variable footprints are disjoint", set(c60.CONSTRUCTION.allowed).isdisjoint(c64.ALLOWED))
    check("A08 mixed footprint has 204 variables", len(AUDIT.allowed) == 204)

    check("B01 mixed table has 163 canonical rows", len(AUDIT.rules) == 163)
    check("B02 canonical union has no input conflict", not AUDIT.canonical_conflicts)
    check("B03 rotated union has 3,370 raw inputs", len(AUDIT.raw_outputs) == 3_370)
    check("B04 rotated inputs remain single-valued", all(len(outputs) == 1 for outputs in AUDIT.raw_outputs.values()))

    check("C01 exact candidate census is 461", len(AUDIT.candidates) == 461)
    check("C02 exact local-subset census is 6,297", AUDIT.local_subsets == 6_297)
    check("C03 exact matching-context census is 2,215", AUDIT.matches == 2_215)
    check("C04 161 canonical rows match somewhere", len(AUDIT.matched_rows) == 161)
    check("C05 mixed scan has 371 bad contexts", len(AUDIT.bad) == 371)
    triples = {(item.target, item.output, item.expected) for item in AUDIT.bad}
    check("C06 mixed scan has 95 bad target/output triples", len(triples) == 95)

    origin_kind = Counter(
        (item.origin, "outside" if item.expected is None else "mistype")
        for item in AUDIT.bad
    )
    check("D01 Cycle-64 rows cause 254 footprint mistypes", origin_kind[("c64", "mistype")] == 254, str(origin_kind))
    check("D02 Cycle-64 rows cause 89 outside writes", origin_kind[("c64", "outside")] == 89, str(origin_kind))
    check("D03 Cycle-60 rows add 28 arbitrary-subset mistypes", origin_kind[("c60", "mistype")] == 28, str(origin_kind))

    check(
        "E01 one P neighbour can mistype an A target",
        witness((-1, -3, -3), "P", "A", ((-2, -3, -3),)),
    )
    check(
        "E02 one A neighbour can write T outside the footprint",
        witness((-1, -3, -2), "T", None, ((-1, -3, -3),)),
    )
    check(
        "E03 one A neighbour can mistype an F target as T",
        witness((0, -3, -3), "T", "F", ((-1, -3, -3),)),
    )
    check(
        "E04 PHASE_E plus OPEN_B can mistype L2 as X_B",
        witness((0, -2, 0), "X_B", "L2", ((1, -2, 0), (0, -2, -1))),
    )

    conditional_outputs: dict[Coord, set[str]] = defaultdict(set)
    for _, _, _, output, target in c64.compile_conditions():
        conditional_outputs[target].add(output)
    conditional_conflicts = {
        target: frozenset(outputs)
        for target, outputs in conditional_outputs.items()
        if len(outputs) > 1
    }
    check("F01 Cycle-64's own completed-comb scan has 16 target conflicts", len(conditional_conflicts) == 16)
    check(
        "F02 all fifteen A targets admit both A and P",
        all(conditional_conflicts.get(site) == frozenset(("A", "P")) for site in c64.ROLE_SITES["A"]),
    )
    check(
        "F03 L2 admits both L2 and X_B",
        conditional_conflicts.get((0, -2, 0)) == frozenset(("L2", "X_B")),
    )

    print(f"\nBAD_ORIGIN_KIND={dict(origin_kind)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
