#!/usr/bin/env python3
"""Cycle 197A: exact compatibility audit of the Cycle-190 and Cycle-193 laws.

The probe merges the two frozen raw local-law tables, separates inherited
branch disagreements from rows added in Cycles 190 and 193, resolves every
disagreement into its proper-cubic orbit, and runs the frozen hard apparatuses
under the multivalued union and both deterministic branch-priority readings.

This runner has no authority.  It edits no foundation, axiom, primitive,
registry, policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

import hashlib
from collections import Counter
from itertools import product
from pathlib import Path

import bare_metal_literal_egress_bind_cycle190_2026_07_16 as c190
import designed_payload_interaction_window_cycle196_2026_07_16 as c196
import physical_context_program_dispatcher_cycle193_2026_07_16 as c193


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CYCLE190_CYCLE193_LAW_UNION_COMPATIBILITY_AUDIT_CYCLE197A_NOTE_2026-07-16.md"
)

FROZEN = {
    ROOT / "scripts/bare_metal_literal_egress_bind_cycle190_2026_07_16.py":
        "77bafcc6e51759e8a9ad561d2a193e58fdf0699e15c74a8d792f33f999a6d76c",
    ROOT / "scripts/physical_context_program_dispatcher_cycle193_2026_07_16.py":
        "86b67139c77ce5cb059bef69db2c09b91a5439d9448c53e2dbee591ed392a679",
    ROOT / "scripts/designed_payload_interaction_window_cycle196_2026_07_16.py":
        "bbc6325a6d44ffa73672690d96c31253fdd16dbe3ecde15318adefde82659d38",
    ROOT / "docs/work_history/repo/review_feedback/BARE_METAL_LITERAL_EGRESS_BIND_CYCLE190_NOTE_2026-07-16.md":
        "37efc07d3fe8ef7d12826d78e752c7368d0164d332f6cc30ee2320eb297d6c85",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CONTEXT_PROGRAM_DISPATCHER_CYCLE193_NOTE_2026-07-16.md":
        "0ec663d753c44b6559cee564c38190b3927aa4d14219d23cbdb69c65a635e972",
    ROOT / "docs/work_history/repo/review_feedback/DESIGNED_PAYLOAD_INTERACTION_WINDOW_CYCLE196_NOTE_2026-07-16.md":
        "48e4fc6c19f5a11ab26f931eaf2b3789075ec1abc9ddf96eba2f557b5b15e18b",
}

cell = c190.cell
c53 = c190.c53

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def raw_union(*laws):
    return cell.merge_raw(*laws)


MULTIVALUED_UNION = raw_union(c190.FULL_RAW, c193.MERGED_RAW)
SHARED = set(c190.FULL_RAW) & set(c193.MERGED_RAW)
DISAGREEMENTS = frozenset(
    signature
    for signature in SHARED
    if c190.FULL_RAW[signature] != c193.MERGED_RAW[signature]
)
AGREEMENTS = SHARED - DISAGREEMENTS


def priority_union(preferred, other):
    merged = dict(other)
    merged.update(preferred)
    return merged


C190_PRIORITY = priority_union(c190.FULL_RAW, c193.MERGED_RAW)
C193_PRIORITY = priority_union(c193.MERGED_RAW, c190.FULL_RAW)
AGREEMENT_ONLY = {
    signature: outputs
    for signature, outputs in MULTIVALUED_UNION.items()
    if signature not in DISAGREEMENTS
}


class TrackingLaw(dict):
    """A literal law table that records queried disagreement signatures."""

    def __init__(self, source):
        super().__init__(source)
        self.touched: set[object] = set()
        self.hits = 0

    def _touch(self, key) -> None:
        if key in DISAGREEMENTS:
            self.touched.add(key)
            self.hits += 1

    def get(self, key, default=None):
        self._touch(key)
        return super().get(key, default)

    def __getitem__(self, key):
        self._touch(key)
        return super().__getitem__(key)

    def __contains__(self, key):
        self._touch(key)
        return super().__contains__(key)


def causal_hard_run(initial, expected, exits):
    """Run dependency discovery and both extreme schedules under patched law."""

    discovery = c190.c171.discover_causal_dependencies(
        initial, expected, exits, order="min"
    )
    if not discovery["ok"]:
        return False, {
            "stage": "discovery",
            "error": discovery.get("error"),
        }
    dependencies = discovery["dependencies"]
    minimum = c190.c171.causal_replay(
        initial, expected, exits, dependencies, order="min"
    )
    maximum = c190.c171.causal_replay(
        initial, expected, exits, dependencies, order="max"
    )
    ok = minimum["ok"] and maximum["ok"]
    return ok, {
        "stage": "complete" if ok else "replay",
        "minimum": minimum.get("error"),
        "maximum": maximum.get("error"),
    }


def run_cycle190(law):
    tracker = TrackingLaw(law)
    old = c190.c171.FULL_RAW
    c190.c171.FULL_RAW = tracker
    results = {}
    try:
        for word in c190.WORDS:
            apparatus = c190.apparatus(word)
            results[word] = causal_hard_run(
                apparatus[0], apparatus[1], apparatus[2]
            )
    finally:
        c190.c171.FULL_RAW = old
    return {
        "passed": sum(result[0] for result in results.values()),
        "total": len(results),
        "failures": tuple(
            (word, detail)
            for word, (ok, detail) in results.items()
            if not ok
        ),
        "touched": frozenset(tracker.touched),
        "hits": tracker.hits,
    }


def run_cycle196(law):
    tracker = TrackingLaw(law)
    old = c190.c171.FULL_RAW
    c190.c171.FULL_RAW = tracker
    results = {}
    try:
        for pair in product((0, 1), repeat=2):
            apparatus = c196.interaction_apparatus(*pair)
            results[pair] = causal_hard_run(
                apparatus[0], apparatus[1], apparatus[2]
            )
    finally:
        c190.c171.FULL_RAW = old
    return {
        "passed": sum(result[0] for result in results.values()),
        "total": len(results),
        "failures": tuple(
            (pair, detail)
            for pair, (ok, detail) in results.items()
            if not ok
        ),
        "touched": frozenset(tracker.touched),
        "hits": tracker.hits,
    }


def run_cycle193(law):
    tracker = TrackingLaw(law)
    old = c193.MERGED_RAW
    c193.MERGED_RAW = tracker
    results = {}
    try:
        for code in c193.c191.CODE_TO_LABEL:
            apparatus = c193.instance(code)
            for order in ("min", "max"):
                results[(code, order)] = c193.physical_run(apparatus, order)
        hard = c193.instance(c193.c191.CONTEXT_CODES["R2"])
        for rotation_index, rotation in enumerate(c193.c53.ROTATIONS):
            results[("R2-rotation", rotation_index)] = c193.physical_run(
                hard, "min", rotation=rotation
            )
    finally:
        c193.MERGED_RAW = old
    return {
        "passed": sum(result[0] for result in results.values()),
        "total": len(results),
        "failures": tuple(
            (case, detail)
            for case, (ok, detail) in results.items()
            if not ok
        ),
        "touched": frozenset(tracker.touched),
        "hits": tracker.hits,
    }


def compact(result):
    return {
        "passed": result["passed"],
        "total": result["total"],
        "conflict_signatures_touched": len(result["touched"]),
        "conflict_query_hits": result["hits"],
        "first_failure": result["failures"][:1],
    }


def origin_membership(signature):
    left = tuple(
        label
        for label, law in (
            ("Cycle178 predecessor", c190.c178.FULL_RAW),
            ("Cycle190 addition", c190.NEW_RAW),
        )
        if signature in law
    )
    right = tuple(
        label
        for label, law in (
            ("Cycle179 predecessor", c193.c179.MERGED_RAW),
            ("Cycle193 router addition", c193.ROUTER_RAW),
            ("Cycle193 scan addition", c193.SCAN_RAW),
        )
        if signature in law
    )
    return left, right


def canonical_orbit_census():
    canonical = Counter(
        c53.canonical_signature(signature)
        for signature in DISAGREEMENTS
    )
    failures = []
    for representative, observed_size in canonical.items():
        left = c190.FULL_RAW[representative]
        right = c193.MERGED_RAW[representative]
        left_orbit = cell.raw_orbit(representative, next(iter(left)))
        right_orbit = cell.raw_orbit(representative, next(iter(right)))
        expected = set(left_orbit) | set(right_orbit)
        if (
            observed_size != 24
            or set(left_orbit) != set(right_orbit)
            or set(left_orbit) - DISAGREEMENTS
            or expected - DISAGREEMENTS
        ):
            failures.append((representative, observed_size, len(expected)))
    return canonical, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN INPUTS")
    observed = {path: sha256(path) for path in FROZEN}
    check(
        "Cycles 190, 193, and 196 inputs match the frozen audit corpus",
        observed == FROZEN,
        {path.name: digest for path, digest in observed.items()},
    )

    print("\nLITERAL RAW-UNION CENSUS")
    check(
        "the direct union reproduces the exact key and disagreement census",
        len(c190.FULL_RAW) == 102_338
        and len(c193.MERGED_RAW) == 101_768
        and len(SHARED) == 93_614
        and len(AGREEMENTS) == 92_582
        and len(DISAGREEMENTS) == 1_032
        and len(MULTIVALUED_UNION) == 110_492
        and sum(len(outputs) > 1 for outputs in MULTIVALUED_UNION.values())
        == 1_032,
        {
            "cycle190": len(c190.FULL_RAW),
            "cycle193": len(c193.MERGED_RAW),
            "shared": len(SHARED),
            "agreements": len(AGREEMENTS),
            "disagreements": len(DISAGREEMENTS),
            "union": len(MULTIVALUED_UNION),
        },
    )
    origin_counts = Counter(origin_membership(row) for row in DISAGREEMENTS)
    check(
        "all disagreements are inherited branch divergence, not a Cycle190 or Cycle193 new-row conflict",
        origin_counts
        == Counter({
            (("Cycle178 predecessor",), ("Cycle179 predecessor",)): 1_032
        }),
        origin_counts,
    )

    print("\nOUTPUT, ROLE, SIGNATURE, AND ORBIT FAMILIES")
    output_pairs = Counter(
        (
            next(iter(c190.FULL_RAW[signature])),
            next(iter(c193.MERGED_RAW[signature])),
        )
        for signature in DISAGREEMENTS
    )
    role_families = Counter(
        tuple(sorted(role for _direction, role in signature))
        for signature in DISAGREEMENTS
    )
    canonical, orbit_failures = canonical_orbit_census()
    check(
        "the 1,032 disagreements are exactly 43 complete proper-cubic 24-row orbits",
        len(canonical) == 43
        and Counter(canonical.values()) == Counter({24: 43})
        and not orbit_failures,
        (len(canonical), Counter(canonical.values()), orbit_failures[:1]),
    )
    check(
        "output-pair multiplicities are frozen",
        output_pairs
        == Counter({
            ("R_A00", "DONE"): 192,
            ("Z_C", "BTQ"): 168,
            ("RING", "B_0_2"): 168,
            ("R_A02", "COMP6"): 144,
            ("Z_A", "BTG"): 144,
            ("PAIR", "A_0_1"): 120,
            ("Z0", "A_0_2"): 96,
        }),
        output_pairs,
    )
    check(
        "each exact neighbor-role multiset is one complete orbit family",
        len(role_families) == 43
        and set(role_families.values()) == {24},
        (len(role_families), Counter(role_families.values())),
    )
    named_example = next((
        signature
        for signature in sorted(DISAGREEMENTS)
        if Counter(role for _direction, role in signature)
        == Counter(("I2", "MARK", "MARK", "COMPLETE", "MARK"))
        and c190.FULL_RAW[signature] == frozenset(("Z_C",))
        and c193.MERGED_RAW[signature] == frozenset(("BTQ",))
    ), None)
    check(
        "the named I2/MARK/MARK/COMPLETE/MARK collision is reproduced literally",
        named_example is not None,
        named_example,
    )

    print("\nSOURCE-LAW HARD CORPORA AND REACHABILITY")
    source190 = run_cycle190(c190.FULL_RAW)
    source196 = run_cycle196(c190.FULL_RAW)
    source193 = run_cycle193(c193.MERGED_RAW)
    check(
        "all frozen source-law hard apparatuses retain their baselines",
        source190["passed"] == source190["total"] == 32
        and source196["passed"] == source196["total"] == 4
        and source193["passed"] == source193["total"] == 40,
        {
            "cycle190": compact(source190),
            "cycle196": compact(source196),
            "cycle193": compact(source193),
        },
    )
    matter_touched = source190["touched"] | source196["touched"]
    dispatcher_touched = source193["touched"]
    shared_touched = matter_touched & dispatcher_touched
    check(
        "none of the 1,032 inherited disagreement rows is reached in any tested hard schedule",
        not matter_touched and not dispatcher_touched,
        {
            "cycle190": len(source190["touched"]),
            "cycle196": len(source196["touched"]),
            "cycle190_or_196": len(matter_touched),
            "cycle193": len(dispatcher_touched),
            "reached_by_both": len(shared_touched),
        },
    )

    print("\nUNION AND PRIORITY INTERPRETATIONS")
    laws = {
        "multivalued-union": MULTIVALUED_UNION,
        "cycle190-priority": C190_PRIORITY,
        "cycle193-priority": C193_PRIORITY,
        "agreement-only": AGREEMENT_ONLY,
    }
    matrix = {}
    for label, law in laws.items():
        matrix[label] = {
            "cycle190": run_cycle190(law),
            "cycle196": run_cycle196(law),
            "cycle193": run_cycle193(law),
        }
        print(label, {
            corpus: compact(result)
            for corpus, result in matrix[label].items()
        })
    check(
        "all hard corpora close under the multivalued union, both priorities, and conflict deletion",
        all(
            result["passed"] == result["total"]
            for corpora in matrix.values()
            for result in corpora.values()
        )
        and {
            label: {
                corpus: (result["passed"], result["total"])
                for corpus, result in corpora.items()
            }
            for label, corpora in matrix.items()
        }
        == {
            label: {
                "cycle190": (32, 32),
                "cycle196": (4, 4),
                "cycle193": (40, 40),
            }
            for label in laws
        },
        {
            label: {
                corpus: (result["passed"], result["total"])
                for corpus, result in corpora.items()
            }
            for label, corpora in matrix.items()
        },
    )

    print("\nACCOUNTING")
    print("ORIGIN_COUNTS", origin_counts)
    print("OUTPUT_PAIRS", output_pairs)
    print("ROLE_FAMILIES", len(role_families))
    print("CANONICAL_ORBITS", len(canonical), Counter(canonical.values()))
    print("SOURCE_REACHABILITY", {
        "cycle190": len(source190["touched"]),
        "cycle196": len(source196["touched"]),
        "cycle193": len(source193["touched"]),
        "matter_dispatcher_intersection": len(shared_touched),
    })
    print("INTERPRETATION_MATRIX", {
        law: {
            corpus: (result["passed"], result["total"])
            for corpus, result in corpora.items()
        }
        for law, corpora in matrix.items()
    })
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "HARD_SECTOR_COMPATIBLE_GLOBAL_LITERAL_UNION_NONDETERMINISTIC"
        if FAIL == 0
        else "CYCLE197A_NEEDS_REPAIR",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
