#!/usr/bin/env python3
"""Cycle 197B: one-law Cycle-190/Cycle-193 integration repair.

The 1,032 conflicts in the literal full-law union are exactly the old-versus-
replacement signed-row codebook rows already priced by Cycle 175.  This probe
chooses the replacement Cycle-169 base once, then adds only the complete
Cycle-179/Cycle-193 deltas: six binary-ingress rows, forty-eight router rows,
and six net scan rows.

The result is a full 102,398-row deterministic law, not a reachable-signature
union.  No host branch tag, apparatus dispatcher, role namespace, or new onsite
role is introduced.  This runner has no authority and performs no foundation,
axiom, primitive, registry, policy, audit, commit, push, or PR edit.
"""

from __future__ import annotations

import dataclasses
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
    "COMMON_REPLACEMENT_BASE_INTEGRATION_CYCLE197B_NOTE_2026-07-16.md"
)
CYCLE190_SCRIPT = ROOT / "scripts/bare_metal_literal_egress_bind_cycle190_2026_07_16.py"
CYCLE190_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "BARE_METAL_LITERAL_EGRESS_BIND_CYCLE190_NOTE_2026-07-16.md"
)
CYCLE193_SCRIPT = ROOT / "scripts/physical_context_program_dispatcher_cycle193_2026_07_16.py"
CYCLE193_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONTEXT_PROGRAM_DISPATCHER_CYCLE193_NOTE_2026-07-16.md"
)
CYCLE196_SCRIPT = ROOT / "scripts/designed_payload_interaction_window_cycle196_2026_07_16.py"
CYCLE196_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "DESIGNED_PAYLOAD_INTERACTION_WINDOW_CYCLE196_NOTE_2026-07-16.md"
)

FROZEN = {
    CYCLE190_SCRIPT: "77bafcc6e51759e8a9ad561d2a193e58fdf0699e15c74a8d792f33f999a6d76c",
    CYCLE190_NOTE: "37efc07d3fe8ef7d12826d78e752c7368d0164d332f6cc30ee2320eb297d6c85",
    CYCLE193_SCRIPT: "86b67139c77ce5cb059bef69db2c09b91a5439d9448c53e2dbee591ed392a679",
    CYCLE193_NOTE: "0ec663d753c44b6559cee564c38190b3927aa4d14219d23cbdb69c65a635e972",
    CYCLE196_SCRIPT: "bbc6325a6d44ffa73672690d96c31253fdd16dbe3ecde15318adefde82659d38",
    CYCLE196_NOTE: "48e4fc6c19f5a11ab26f931eaf2b3789075ec1abc9ddf96eba2f557b5b15e18b",
}

cell = c190.cell
c53 = c190.c53
c179 = c193.c179
c175 = c190.c178.c175

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


# ---------------------------------------------------------------------------
# Conflict provenance and the one-law construction
# ---------------------------------------------------------------------------

DIRECT_UNION = cell.merge_raw(c190.FULL_RAW, c193.MERGED_RAW)
DIRECT_CONFLICTS = {
    signature: outputs
    for signature, outputs in DIRECT_UNION.items()
    if len(outputs) != 1
}

BASE_CONFLICTS = {
    signature: (
        c175.CANDIDATE169_RAW[signature],
        c179.c169.UNIFIED_RAW[signature],
    )
    for signature in (
        set(c175.CANDIDATE169_RAW) & set(c179.c169.UNIFIED_RAW)
    )
    if c175.CANDIDATE169_RAW[signature]
    != c179.c169.UNIFIED_RAW[signature]
}

FULL_RAW = cell.merge_raw(
    c190.FULL_RAW,
    c179.BINARY_INGRESS_RAW,
    c193.ROUTER_RAW,
    c193.SCAN_RAW,
)
FULL_CONFLICTS = {
    signature: outputs
    for signature, outputs in FULL_RAW.items()
    if len(outputs) != 1
}

INGRESS_OVERLAP = set(c179.BINARY_INGRESS_RAW) & set(c190.FULL_RAW)
ROUTER_OVERLAP = set(c193.ROUTER_RAW) & set(c190.FULL_RAW)
SCAN_OVERLAP = set(c193.SCAN_RAW) & set(
    cell.merge_raw(c190.FULL_RAW, c179.BINARY_INGRESS_RAW, c193.ROUTER_RAW)
)


def law_roles(law) -> frozenset[str]:
    return frozenset(
        role
        for signature, outputs in law.items()
        for role in (
            *(value for _offset, value in signature),
            *outputs,
        )
    )


def fired_signatures(initial, expected, dependencies) -> frozenset[object]:
    """Exact local premise for every declared write in a causal certificate."""

    result = set()
    for target, parents in dependencies.items():
        premise = {
            neighbour: initial[neighbour]
            for direction in c53.DIRECTIONS
            if (
                neighbour := tuple(
                    value + delta
                    for value, delta in zip(target, direction)
                )
            ) in initial
        }
        premise.update({parent: expected[parent] for parent in parents})
        result.add(c53.local_signature(premise, target))
    return frozenset(result)


def conflict_reachability_census():
    conflicts = set(DIRECT_CONFLICTS)
    cycle190 = set()
    for word in c190.WORDS:
        apparatus = c190.apparatus(word)
        cycle190.update(
            fired_signatures(
                apparatus[0],
                apparatus[1],
                c190.BASE_CERTIFICATES[word]["dependencies"]
                | {
                    site: parents
                    for site, parents in c190.EXTENSION_PARENTS.items()
                },
            )
        )

    cycle193 = set()
    for code in c193.c191.CODE_TO_LABEL:
        apparatus = c193.instance(code)
        cycle193.update(
            fired_signatures(
                apparatus.initial,
                apparatus.expected,
                apparatus.dependencies,
            )
        )
    return {
        "cycle190_unique": len(cycle190),
        "cycle193_unique": len(cycle193),
        "cycle190_conflicts": len(cycle190 & conflicts),
        "cycle193_conflicts": len(cycle193 & conflicts),
    }


# ---------------------------------------------------------------------------
# Replacement-codebook replay of the Cycle-179 predecessor
# ---------------------------------------------------------------------------

def mapped_cycle179_instance():
    original = c179.instance(c179.ZI)
    role_map = c175.ROLE_MAP
    return dataclasses.replace(
        original,
        initial={site: role_map.get(role, role) for site, role in original.initial.items()},
        expected={site: role_map.get(role, role) for site, role in original.expected.items()},
        expected_output=role_map.get(original.expected_output, original.expected_output),
    )


def cycle179_mapping_control():
    c179.instance.cache_clear()
    original = c179.instance(c179.ZI)
    mapped = mapped_cycle179_instance()
    old_labels = set(c175.ALIAS_REPLACEMENT)
    initial_occurrences = Counter(
        role for role in original.initial.values() if role in old_labels
    )
    expected_occurrences = Counter(
        role for role in original.expected.values() if role in old_labels
    )

    old_law = c179.MERGED_RAW
    try:
        c179.MERGED_RAW = FULL_RAW
        with c175.replacement_codebook():
            c179.instance.cache_clear()
            regenerated = c179.instance(c179.ZI)
    finally:
        c179.MERGED_RAW = old_law
        c179.instance.cache_clear()

    return {
        "mapped_equals_regenerated": mapped == regenerated,
        "initial_occurrences": initial_occurrences,
        "expected_occurrences": expected_occurrences,
    }


def mapped_cycle179_replay():
    apparatus = mapped_cycle179_instance()
    old_law = c179.MERGED_RAW
    old_initial_enabled = c179.initial_enabled
    try:
        c179.MERGED_RAW = FULL_RAW
        local = c179.local_compiled_check(apparatus)
        c179.initial_enabled = lambda _measured: c179.enabled(apparatus.initial)
        minimum = c179.physical_run(apparatus, order="min")
        maximum = c179.physical_run(apparatus, order="max")
    finally:
        c179.MERGED_RAW = old_law
        c179.initial_enabled = old_initial_enabled
    return local, minimum, maximum


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN PREDECESSORS")
    observed = {path: sha256(path) for path in FROZEN}
    check(
        "Cycles 190, 193, and 196 remain byte-frozen",
        observed == FROZEN,
        {path.name: digest for path, digest in observed.items()},
    )

    print("\nCONFLICT PROVENANCE")
    replacement_pairs = Counter(
        (
            next(iter(old)),
            next(iter(new)),
        )
        for new, old in BASE_CONFLICTS.values()
    )
    wanted_pairs = Counter(
        {
            (old, new): count
            for (old, new), count in (
                (("A_0_1", "PAIR"), 120),
                (("A_0_2", "Z0"), 96),
                (("BTG", "Z_A"), 144),
                (("BTQ", "Z_C"), 168),
                (("B_0_2", "RING"), 168),
                (("COMP6", "R_A02"), 144),
                (("DONE", "R_A00"), 192),
            )
        }
    )
    check(
        "all 1,032 direct-union conflicts are exactly Cycle-175 codebook replacements",
        len(DIRECT_CONFLICTS) == 1_032
        and set(DIRECT_CONFLICTS) == set(BASE_CONFLICTS)
        and replacement_pairs == wanted_pairs,
        replacement_pairs,
    )
    check(
        "no Cycle-190 egress or Cycle-193 router/scan delta touches a conflict row",
        not (
            set(DIRECT_CONFLICTS)
            & (
                set(c190.NEW_RAW)
                | set(c193.ROUTER_RAW)
                | set(c193.SCAN_RAW)
            )
        ),
        len(
            set(DIRECT_CONFLICTS)
            & (
                set(c190.NEW_RAW)
                | set(c193.ROUTER_RAW)
                | set(c193.SCAN_RAW)
            )
        ),
    )
    reachability = conflict_reachability_census()
    check(
        "the conflicting compiler rows are absent from all Cycle-190 and dispatcher target histories",
        reachability["cycle190_conflicts"] == 0
        and reachability["cycle193_conflicts"] == 0,
        reachability,
    )

    print("\nONE FULL LAW AND EXACT PRICE")
    check(
        "the complete common-base law is deterministic on all raw signatures",
        len(FULL_RAW) == 102_398
        and not FULL_CONFLICTS
        and all(len(outputs) == 1 for outputs in FULL_RAW.values()),
        (len(FULL_RAW), len(FULL_CONFLICTS)),
    )
    check(
        "the exact price is +6 ingress, +48 router, and +6 net scan rows",
        len(c179.BINARY_INGRESS_RAW) == 6
        and not INGRESS_OVERLAP
        and len(c193.ROUTER_RAW) == 48
        and not ROUTER_OVERLAP
        and len(c193.SCAN_RAW) == 30
        and len(SCAN_OVERLAP) == 24
        and len(FULL_RAW) - len(c190.FULL_RAW) == 60,
        {
            "ingress": len(c179.BINARY_INGRESS_RAW),
            "router": len(c193.ROUTER_RAW),
            "scan_raw": len(c193.SCAN_RAW),
            "scan_overlap": len(SCAN_OVERLAP),
            "net": len(FULL_RAW) - len(c190.FULL_RAW),
        },
    )
    check(
        "the integration adds zero onsite roles and no branch-identity role",
        law_roles(FULL_RAW) == law_roles(c190.FULL_RAW),
        law_roles(FULL_RAW) - law_roles(c190.FULL_RAW),
    )

    print("\nCYCLE-190 AND CYCLE-196 HARD REPLAY")
    old_190 = c190.FULL_RAW
    old_171 = c190.c171.FULL_RAW
    c190.FULL_RAW = FULL_RAW
    c190.c171.FULL_RAW = FULL_RAW
    try:
        predecessor = c190.apparatus((1, 0, 1, 0, 1))
        predecessor_certificate = c190.c171.causal_certificate(
            predecessor[0], predecessor[1], predecessor[2]
        )
        check(
            "the Cycle-190 hard consumer remains exact with no parasitic firing",
            predecessor_certificate["ok"]
            and predecessor_certificate["minimum"]["states"] == 2_289
            and predecessor_certificate["edge_checks"]["edges"] == 4_232
            and not predecessor_certificate["unordered"]
            and len(predecessor_certificate["minimum"]["terminal"]) == 10,
            {
                "ok": predecessor_certificate["ok"],
                "states": predecessor_certificate["minimum"]["states"],
                "edges": predecessor_certificate["edge_checks"]["edges"],
            },
        )

        certificates = {}
        shapes = Counter()
        for pair in product((0, 1), repeat=2):
            apparatus = c196.interaction_apparatus(*pair)
            certificate = c190.c171.causal_certificate(
                apparatus[0], apparatus[1], apparatus[2]
            )
            certificates[pair] = certificate
            if certificate["ok"]:
                shapes[(
                    certificate["minimum"]["states"],
                    certificate["edge_checks"]["edges"],
                    certificate["minimum"]["max_frontier"],
                    certificate["maximum"]["max_frontier"],
                    len(certificate["unordered"]),
                    len(certificate["minimum"]["terminal"]),
                )] += 1
        check(
            "all four Cycle-196 interaction histories remain exact",
            len(certificates) == 4
            and all(certificate["ok"] for certificate in certificates.values())
            and shapes == Counter({(3_256, 7_126, 31, 31, 0, 20): 4}),
            shapes,
        )
        deletions, deletion_failures = c196.deletion_controls(certificates)
        flips, flip_failures = c196.flip_controls()
        check(
            "all Cycle-196 deletion and flip controls remain exact",
            len(deletions) == 32
            and not deletion_failures
            and flips == 4
            and not flip_failures,
            (len(deletions), deletion_failures[:1], flips, flip_failures[:1]),
        )
        rotation_checks, rotation_failures, terminal_failures = (
            c196.covariance_census()
        )
        check(
            "Cycle-196 remains exact in every proper-cubic image",
            rotation_checks == 20_640
            and not rotation_failures
            and not terminal_failures,
            (rotation_checks, rotation_failures[:1], terminal_failures[:1]),
        )
    finally:
        c190.FULL_RAW = old_190
        c190.c171.FULL_RAW = old_171

    print("\nCYCLE-193 DISPATCHER REPLAY")
    old_193 = c193.MERGED_RAW
    c193.MERGED_RAW = FULL_RAW
    try:
        dispatcher_runs = {
            (code, order): c193.physical_run(c193.instance(code), order)
            for code in c193.c191.CODE_TO_LABEL
            for order in ("min", "max")
        }
        check(
            "all eight dispatcher contexts close under both schedules",
            len(dispatcher_runs) == 16
            and all(result[0] for result in dispatcher_runs.values()),
            {
                key: result
                for key, result in dispatcher_runs.items()
                if not result[0]
            },
        )
        context_deletions = {
            (code, bit_index): c193.context_deletion_run(
                c193.instance(code), bit_index, "min"
            )
            for code in c193.c191.CODE_TO_LABEL
            for bit_index in range(3)
        }
        program = c193.program_controls()
        check(
            "all dispatcher context and program controls remain exact",
            len(context_deletions) == 24
            and all(result[0] for result in context_deletions.values())
            and not program["failures"]
            and program["selected_bit_deletions"] == 84
            and program["selected_bit_flips"] == 84
            and program["token_pair_deletions"] == 28
            and program["token_pair_flips"] == 28
            and program["unselected_bit_mutations"] == 168,
            program,
        )
        hard = c193.instance(c193.c191.CONTEXT_CODES["R2"])
        rotated = tuple(
            c193.physical_run(hard, "min", rotation=rotation)
            for rotation in c193.c53.ROTATIONS
        )
        check(
            "the dispatcher remains exact in all twenty-four proper-cubic images",
            len(rotated) == 24
            and all(result[0] for result in rotated)
            and not c193.orbit_failures(),
            tuple(result for result in rotated if not result[0])[:1],
        )
    finally:
        c193.MERGED_RAW = old_193

    print("\nMAPPED CYCLE-179 PREDECESSOR")
    mapping_control = cycle179_mapping_control()
    check(
        "the ZI fixture map is exactly regeneration under the replacement codebook",
        mapping_control["mapped_equals_regenerated"]
        and mapping_control["initial_occurrences"] == Counter()
        and mapping_control["expected_occurrences"] == Counter({"A_0_2": 141}),
        mapping_control,
    )
    local, minimum, maximum = mapped_cycle179_replay()
    check(
        "all 341,029 mapped Cycle-179 writes use the replacement codebook exactly",
        local == (341_029, ()),
        (local[0], local[1][:1]),
    )
    check(
        "the mapped Cycle-179 hard apparatus closes under both schedules",
        minimum[0]
        and maximum[0]
        and minimum[1]["dynamic"] == 341_029
        and maximum[1]["dynamic"] == 341_029
        and minimum[1]["output"] == c179.H1
        and maximum[1]["output"] == c179.H1
        and not minimum[1]["residual"]
        and not maximum[1]["residual"],
        (minimum, maximum),
    )

    print("\nSCOPE AND NO-GO DISCIPLINE")
    normalized_note = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    required = (
        "full 102,398-row law",
        "not a reachable-signature union",
        "global deterministic codebook choice",
        "unchanged old-codebook cycle-179 artifact is not replayed",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
        "no axiom conclusion follows",
        "no commit or push",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized_note)
    check(
        "the note states the full-law boundary and passes the narrow N1-N8 gate",
        NOTE.is_file() and not missing,
        missing,
    )

    print("\nACCOUNTING")
    print("DIRECT_CONFLICTS", len(DIRECT_CONFLICTS))
    print("FULL_RAW_ROWS", len(FULL_RAW))
    print("NET_NEW_ROWS", len(FULL_RAW) - len(c190.FULL_RAW))
    print("NEW_ROLES", tuple(sorted(law_roles(FULL_RAW) - law_roles(c190.FULL_RAW))))
    print("REACHABILITY", reachability)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "COMMON_REPLACEMENT_BASE_INTEGRATION"
        if FAIL == 0
        else "CYCLE197B_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
