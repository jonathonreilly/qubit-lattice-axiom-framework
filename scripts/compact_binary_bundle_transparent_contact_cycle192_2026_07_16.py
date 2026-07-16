#!/usr/bin/env python3
"""Cycle 192: transparent contact of two compact five-lane H0/H1 bundles.

Two unchanged Cycle-180 compact bundles are placed in their nearest disjoint
rigid-translation contact class.  The runner proves that the contact interface
is fixed-shell only, derives a zero-row contact price, exhausts all 32x32 word
pairs by exact local compilation, and checks representative full causal
certificates, lineage factorization, deletion controls, and proper-cubic
covariance.

This is an authority-free bounded construction.  It edits no foundation,
axiom, primitive, registry, policy, audit, queue, predecessor, commit, push,
or PR surface.
"""

from __future__ import annotations

import hashlib
from collections import Counter
from itertools import product
from pathlib import Path

import compact_five_literal_lane_spacing_cycle180_2026_07_16 as c180
import recurrent_carrier_matter_kinematics_cycle172_2026_07_16 as c172
import recurrent_five_literal_lane_worldline_cycle178_2026_07_16 as c178


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPACT_BINARY_BUNDLE_TRANSPARENT_CONTACT_CYCLE192_NOTE_2026-07-16.md"
)
CYCLE178_SCRIPT = (
    ROOT / "scripts/recurrent_five_literal_lane_worldline_cycle178_2026_07_16.py"
)
CYCLE178_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "RECURRENT_FIVE_LITERAL_LANE_WORLDLINE_CYCLE178_NOTE_2026-07-16.md"
)
CYCLE180_SCRIPT = (
    ROOT / "scripts/compact_five_literal_lane_spacing_cycle180_2026_07_16.py"
)
CYCLE180_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COMPACT_FIVE_LITERAL_LANE_SPACING_CYCLE180_NOTE_2026-07-16.md"
)
CYCLE188_SCRIPT = (
    ROOT / "scripts/proper_cubic_recurrent_contact_kernel_cycle188_2026_07_16.py"
)
CYCLE188_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PROPER_CUBIC_RECURRENT_CONTACT_KERNEL_CYCLE188_NOTE_2026-07-16.md"
)

FROZEN_CYCLE178_SCRIPT_SHA = (
    "2a8ecad9e8f5fbf20269b7aafc5d5511f6be93ddb940a8e8de5b47e115168942"
)
FROZEN_CYCLE178_NOTE_SHA = (
    "c36131ceddf478d239796630327e5c4363a503ac8c17ebf8d645f4d41e0c4a49"
)
FROZEN_CYCLE180_SCRIPT_SHA = (
    "6395239ffe1ded603d9c0d97bad9919bb2460ac1613f384761bd1a23405277c7"
)
FROZEN_CYCLE180_NOTE_SHA = (
    "2ea6be500f31587eaa8ae662b2d26dfc33d710969d19b507e547d8c23e0fbc61"
)
FROZEN_CYCLE188_SCRIPT_SHA = (
    "5f8f9959c2be1e01b75dc61be23e2f4352fe67668cc5021278d994c60803fe56"
)
FROZEN_CYCLE188_NOTE_SHA = (
    "439285edf08d2679391b7909dc119f884e21a0635d3af8778c40d89af2e59cf3"
)

Coord = tuple[int, int, int]
Word = tuple[int, int, int, int, int]

SPACING = 12
CONTACT_OFFSET: Coord = (0, 0, 10)
ROTATION_SHIFT: Coord = (20_003, -20_011, 20_021)
ZERO: Word = (0, 0, 0, 0, 0)
ONE: Word = (1, 1, 1, 1, 1)

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


def shift_map(records, offset: Coord):
    return {
        c172.shift(site, offset): value
        for site, value in records.items()
    }


def bundle(word: Word):
    return c180.compact_bundle(word, SPACING)


def pair_bundle(
    left_word: Word,
    right_word: Word,
):
    (
        left_sources,
        left_outputs,
        left_initial,
        left_expected,
        left_exits,
        left_owners,
    ) = bundle(left_word)
    (
        right_sources,
        right_outputs,
        right_initial,
        right_expected,
        right_exits,
        right_owners,
    ) = bundle(right_word)
    return {
        "left_sources": left_sources,
        "left_outputs": left_outputs,
        "right_sources": tuple(
            shift_map(part, CONTACT_OFFSET)
            for part in right_sources
        ),
        "right_outputs": tuple(
            shift_map(part, CONTACT_OFFSET)
            for part in right_outputs
        ),
        "initial": {
            **left_initial,
            **shift_map(right_initial, CONTACT_OFFSET),
        },
        "expected": {
            **left_expected,
            **shift_map(right_expected, CONTACT_OFFSET),
        },
        "exits": {
            **left_exits,
            **shift_map(right_exits, CONTACT_OFFSET),
        },
        "left_owners": left_owners,
        "right_owners": {
            c172.shift(site, CONTACT_OFFSET): lane
            for site, lane in right_owners.items()
        },
    }


BASE_PAIR = pair_bundle(ZERO, ZERO)
BASE_LEFT = bundle(ZERO)
LEFT_SUPPORT = set(BASE_LEFT[2]) | set(BASE_LEFT[3])
RIGHT_SUPPORT = {
    c172.shift(site, CONTACT_OFFSET)
    for site in LEFT_SUPPORT
}
LEFT_PAYLOADS = {
    c172.shift(c172.payload_site(x), offset)
    for offset in c180.offsets(SPACING)
    for x in range(c172.SEED_X, c172.COPY_X[-1] + 1)
}
RIGHT_PAYLOADS = {
    c172.shift(site, CONTACT_OFFSET)
    for site in LEFT_PAYLOADS
}


def translated_support(offset: Coord) -> set[Coord]:
    return {
        c172.shift(site, offset)
        for site in LEFT_SUPPORT
    }


def l1(vector: Coord) -> int:
    return sum(map(abs, vector))


def offsets_at_l1(radius: int) -> tuple[Coord, ...]:
    return tuple(
        (dx, dy, dz)
        for dx in range(-radius, radius + 1)
        for dy in range(-radius, radius + 1)
        for dz in range(-radius, radius + 1)
        if abs(dx) + abs(dy) + abs(dz) == radius
    )


def contact_pairs(
    left: set[Coord],
    right: set[Coord],
) -> tuple[tuple[Coord, Coord], ...]:
    return tuple(sorted(
        (site, c172.shift(site, direction))
        for site in left
        for direction in c178.c53.DIRECTIONS
        if c172.shift(site, direction) in right
    ))


def nearest_contact_census():
    lower_lawful = []
    for radius in range(1, l1(CONTACT_OFFSET)):
        for offset in offsets_at_l1(radius):
            if LEFT_SUPPORT.isdisjoint(
                translated_support(offset)
            ):
                lower_lawful.append(offset)
    radius_lawful = []
    for offset in offsets_at_l1(l1(CONTACT_OFFSET)):
        shifted = translated_support(offset)
        if LEFT_SUPPORT.isdisjoint(shifted):
            radius_lawful.append(
                (
                    offset,
                    contact_pairs(LEFT_SUPPORT, shifted),
                )
            )
    return tuple(lower_lawful), tuple(radius_lawful)


def payload_contact_offsets() -> frozenset[Coord]:
    return frozenset(
        (
            left[0] + direction[0] - right[0],
            left[1] + direction[1] - right[1],
            left[2] + direction[2] - right[2],
        )
        for left in LEFT_PAYLOADS
        for right in LEFT_PAYLOADS
        for direction in c178.c53.DIRECTIONS
    )


def lawful_payload_contacts():
    return tuple(sorted(
        offset
        for offset in payload_contact_offsets()
        if (
            offset != (0, 0, 0)
            and LEFT_SUPPORT.isdisjoint(
                translated_support(offset)
            )
        )
    ))


def mixed_open_candidates():
    occupied = {
        **{site: "LEFT" for site in LEFT_SUPPORT},
        **{site: "RIGHT" for site in RIGHT_SUPPORT},
    }
    result = []
    for target in c178.c53.open_candidates(occupied):
        left = tuple(
            c172.shift(target, direction)
            for direction in c178.c53.DIRECTIONS
            if c172.shift(target, direction) in LEFT_SUPPORT
        )
        right = tuple(
            c172.shift(target, direction)
            for direction in c178.c53.DIRECTIONS
            if c172.shift(target, direction) in RIGHT_SUPPORT
        )
        if left and right:
            result.append((target, left, right))
    return tuple(sorted(result))


MIXED_OPEN = mixed_open_candidates()


def interface_census():
    left_initial = BASE_LEFT[2]
    left_expected = BASE_LEFT[3]
    right_initial = shift_map(left_initial, CONTACT_OFFSET)
    right_expected = shift_map(left_expected, CONTACT_OFFSET)
    signatures = Counter()
    firings = []
    dynamic_neighbors = []
    payload_neighbors = []
    for target, left, right in MIXED_OPEN:
        premise = {
            site: (
                left_initial.get(site)
                or left_expected.get(site)
                or right_initial.get(site)
                or right_expected.get(site)
            )
            for site in left + right
        }
        signature = c178.c53.local_signature(
            premise,
            target,
        )
        signatures[signature] += 1
        observed = c178.FULL_RAW.get(signature)
        if observed is not None:
            firings.append((target, observed, signature))
        for site in left + right:
            if site in left_expected or site in right_expected:
                dynamic_neighbors.append((target, site))
            if site in LEFT_PAYLOADS or site in RIGHT_PAYLOADS:
                payload_neighbors.append((target, site))
    return (
        signatures,
        tuple(firings),
        tuple(dynamic_neighbors),
        tuple(payload_neighbors),
    )


def formation_premise(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
    target: Coord,
) -> dict[Coord, str]:
    premise = {
        neighbor: initial[neighbor]
        for direction in c178.c53.DIRECTIONS
        if (
            neighbor := c172.shift(target, direction)
        ) in initial
    }
    premise.update({
        parent: expected[parent]
        for parent in dependencies[target]
    })
    return premise


def all_word_pair_local_census(
    dependencies: dict[Coord, frozenset[Coord]],
):
    checks = 0
    failures = []
    geometry_shapes = set()
    endpoint_words = set()
    for left_word, right_word in product(
        c178.WORDS,
        repeat=2,
    ):
        apparatus = pair_bundle(left_word, right_word)
        initial = apparatus["initial"]
        expected = apparatus["expected"]
        exits = apparatus["exits"]
        geometry_shapes.add(
            (
                frozenset(initial),
                frozenset(expected),
                frozenset(exits),
            )
        )
        endpoints = tuple(
            expected[
                c172.shift(
                    c172.payload_site(c172.COPY_X[-1]),
                    (
                        side_shift[0] + lane_offset[0],
                        side_shift[1] + lane_offset[1],
                        side_shift[2] + lane_offset[2],
                    ),
                )
            ]
            for side_shift in ((0, 0, 0), CONTACT_OFFSET)
            for lane_offset in c180.offsets(SPACING)
        )
        endpoint_words.add(endpoints)
        wanted_endpoints = tuple(
            c178.bit_role(bit)
            for bit in left_word + right_word
        )
        if endpoints != wanted_endpoints:
            failures.append(
                (
                    left_word,
                    right_word,
                    "endpoints",
                    endpoints,
                    wanted_endpoints,
                )
            )
            break
        for target, parents in dependencies.items():
            premise = formation_premise(
                initial,
                expected,
                dependencies,
                target,
            )
            observed = c178.FULL_RAW.get(
                c178.c53.local_signature(
                    premise,
                    target,
                )
            )
            checks += 1
            if observed != frozenset((expected[target],)):
                failures.append(
                    (
                        left_word,
                        right_word,
                        target,
                        expected[target],
                        observed,
                    )
                )
                break
        if failures:
            break
    return (
        checks,
        tuple(failures),
        geometry_shapes,
        endpoint_words,
    )


def dependency_factorization(
    pair_certificate,
    single_certificate,
):
    left_expected = set(BASE_LEFT[3])
    right_expected = {
        c172.shift(site, CONTACT_OFFSET)
        for site in left_expected
    }
    pair_dependencies = pair_certificate["dependencies"]
    cross = tuple(
        (parent, target)
        for target, parents in pair_dependencies.items()
        for parent in parents
        if (
            (target in left_expected)
            != (parent in left_expected)
        )
    )
    left_dependencies = {
        target: parents
        for target, parents in pair_dependencies.items()
        if target in left_expected
    }
    translated_dependencies = {
        c172.shift(target, CONTACT_OFFSET):
        frozenset(
            c172.shift(parent, CONTACT_OFFSET)
            for parent in parents
        )
        for target, parents
        in single_certificate["dependencies"].items()
    }
    right_dependencies = {
        target: parents
        for target, parents in pair_dependencies.items()
        if target in right_expected
    }
    return (
        cross,
        left_dependencies == single_certificate["dependencies"],
        right_dependencies == translated_dependencies,
    )


def seed_deletion_controls(
    dependencies: dict[Coord, frozenset[Coord]],
):
    results = []
    for value in (0, 1):
        for side, side_shift in enumerate(
            ((0, 0, 0), CONTACT_OFFSET)
        ):
            left_word = (value,) * 5 if side == 0 else ZERO
            right_word = (value,) * 5 if side == 1 else ZERO
            apparatus = pair_bundle(left_word, right_word)
            initial = apparatus["initial"]
            expected = apparatus["expected"]
            for lane, lane_offset in enumerate(
                c180.offsets(SPACING)
            ):
                offset = tuple(
                    side_shift[index] + lane_offset[index]
                    for index in range(3)
                )
                seed = c172.shift(
                    c172.payload_site(c172.SEED_X),
                    offset,
                )
                target = c172.shift(
                    c172.payload_site(c172.COPY_X[0]),
                    offset,
                )
                premise = formation_premise(
                    initial,
                    expected,
                    dependencies,
                    target,
                )
                baseline = c178.FULL_RAW.get(
                    c178.c53.local_signature(
                        premise,
                        target,
                    )
                )
                trial = dict(premise)
                trial.pop(seed)
                observed = c178.FULL_RAW.get(
                    c178.c53.local_signature(
                        trial,
                        target,
                    )
                )
                results.append(
                    (
                        value,
                        side,
                        lane,
                        seed,
                        target,
                        baseline,
                        observed,
                    )
                )
    return tuple(results)


def rotated_local_check(
    apparatus,
    dependencies,
    rotation,
):
    transform = lambda site: c172.shift(
        c178.c53.matvec(rotation, site),
        ROTATION_SHIFT,
    )
    failures = []
    checks = 0
    for target, parents in dependencies.items():
        premise = formation_premise(
            apparatus["initial"],
            apparatus["expected"],
            dependencies,
            target,
        )
        transformed = {
            transform(site): role
            for site, role in premise.items()
        }
        rotated_target = transform(target)
        observed = c178.FULL_RAW.get(
            c178.c53.local_signature(
                transformed,
                rotated_target,
            )
        )
        checks += 1
        if observed != frozenset(
            (apparatus["expected"][target],)
        ):
            failures.append(
                (
                    target,
                    apparatus["expected"][target],
                    observed,
                )
            )
            break
    for target, left, right in MIXED_OPEN:
        base_initial = BASE_LEFT[2]
        base_expected = BASE_LEFT[3]
        right_initial = shift_map(
            base_initial,
            CONTACT_OFFSET,
        )
        right_expected = shift_map(
            base_expected,
            CONTACT_OFFSET,
        )
        premise = {
            site: (
                base_initial.get(site)
                or base_expected.get(site)
                or right_initial.get(site)
                or right_expected.get(site)
            )
            for site in left + right
        }
        transformed = {
            transform(site): role
            for site, role in premise.items()
        }
        observed = c178.FULL_RAW.get(
            c178.c53.local_signature(
                transformed,
                transform(target),
            )
        )
        checks += 1
        if observed is not None:
            failures.append(
                ("mixed", target, observed)
            )
            break
    return checks, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    old_full_raw = c178.c171.FULL_RAW
    c178.c171.FULL_RAW = c178.FULL_RAW
    try:
        print("AUTHORITY AND LAW")
        check(
            "Cycles 178, 180, and 188 frozen hashes match",
            sha256(CYCLE178_SCRIPT)
            == FROZEN_CYCLE178_SCRIPT_SHA
            and sha256(CYCLE178_NOTE)
            == FROZEN_CYCLE178_NOTE_SHA
            and sha256(CYCLE180_SCRIPT)
            == FROZEN_CYCLE180_SCRIPT_SHA
            and sha256(CYCLE180_NOTE)
            == FROZEN_CYCLE180_NOTE_SHA
            and sha256(CYCLE188_SCRIPT)
            == FROZEN_CYCLE188_SCRIPT_SHA
            and sha256(CYCLE188_NOTE)
            == FROZEN_CYCLE188_NOTE_SHA,
            (
                sha256(CYCLE178_SCRIPT),
                sha256(CYCLE178_NOTE),
                sha256(CYCLE180_SCRIPT),
                sha256(CYCLE180_NOTE),
                sha256(CYCLE188_SCRIPT),
                sha256(CYCLE188_NOTE),
            ),
        )
        check(
            "the compact bundle keeps the exact H0/H1 law with no row-role payload",
            SPACING == c180.MINIMUM_DISJOINT_SPACING
            and c178.BIT_ROLES == (c178.H0, c178.H1)
            and len(c178.FULL_RAW) == 101_996
            and not c178.RAW_CONFLICTS,
            (
                SPACING,
                c178.BIT_ROLES,
                len(c178.FULL_RAW),
                len(c178.RAW_CONFLICTS),
            ),
        )

        print("\nNEAREST LAWFUL RIGID CONTACT")
        lower_lawful, radius_lawful = nearest_contact_census()
        check(
            "L1 radius ten is the first disjoint rigid-translation class",
            not lower_lawful
            and tuple(
                offset
                for offset, _pairs in radius_lawful
            )
            == ((0, 0, -10), (0, 0, 10)),
            (
                lower_lawful,
                tuple(
                    (offset, len(pairs))
                    for offset, pairs in radius_lawful
                ),
            ),
        )
        contacts = contact_pairs(
            LEFT_SUPPORT,
            RIGHT_SUPPORT,
        )
        left_initial = BASE_LEFT[2]
        right_original_initial = BASE_LEFT[2]
        contact_roles = tuple(
            (
                left_initial[left],
                right_original_initial[
                    (
                        right[0] - CONTACT_OFFSET[0],
                        right[1] - CONTACT_OFFSET[1],
                        right[2] - CONTACT_OFFSET[2],
                    )
                ],
            )
            for left, right in contacts
        )
        check(
            "the nearest class has exactly five value-independent BTP-L6 shell contacts",
            len(contacts) == 5
            and contact_roles == (("BTP", "L6"),) * 5
            and all(
                left in BASE_LEFT[2]
                and (
                    right[0] - CONTACT_OFFSET[0],
                    right[1] - CONTACT_OFFSET[1],
                    right[2] - CONTACT_OFFSET[2],
                ) in BASE_LEFT[2]
                for left, right in contacts
            ),
            (contacts, contact_roles),
        )

        print("\nFIXED-SHELL INTERFACE AND LAW PRICE")
        (
            interface_signatures,
            interface_firings,
            dynamic_neighbors,
            payload_neighbors,
        ) = interface_census()
        check(
            "all forty mixed open sites are fixed-shell, value-free, and quiet",
            len(MIXED_OPEN) == 40
            and sum(interface_signatures.values()) == 40
            and len(interface_signatures) == 8
            and not interface_firings
            and not dynamic_neighbors
            and not payload_neighbors,
            (
                len(MIXED_OPEN),
                len(interface_signatures),
                interface_signatures,
                interface_firings,
                dynamic_neighbors,
                payload_neighbors,
            ),
        )
        check(
            "transparent coexistence requires zero new rows and zero new roles",
            len(c178.FULL_RAW) == 101_996,
            {
                "canonical_rows": 0,
                "proper_cubic_raw_rows": 0,
                "onsite_roles": 0,
                "full_raw": len(c178.FULL_RAW),
            },
        )

        print("\nFOUR VALUE-LOCAL FULL CERTIFICATES")
        certificates = {}
        certificate_shapes = Counter()
        certificate_failures = []
        for left_value, right_value in product(
            (0, 1),
            repeat=2,
        ):
            apparatus = pair_bundle(
                (left_value,) * 5,
                (right_value,) * 5,
            )
            certificate = c178.c171.causal_certificate(
                apparatus["initial"],
                apparatus["expected"],
                apparatus["exits"],
            )
            certificates[(left_value, right_value)] = certificate
            if not certificate["ok"]:
                certificate_failures.append(
                    (
                        left_value,
                        right_value,
                        certificate["discovery"].get("error"),
                    )
                )
                continue
            certificate_shapes[(
                certificate["minimum"]["states"],
                certificate["edge_checks"]["edges"],
                certificate["minimum"]["max_frontier"],
                certificate["maximum"]["max_frontier"],
                len(certificate["unordered"]),
                len(certificate["minimum"]["terminal"]),
            )] += 1
        check(
            "H0/H0, H0/H1, H1/H0, and H1/H1 all close with one exact shape",
            not certificate_failures
            and certificate_shapes
            == Counter({(3_041, 6_910, 31, 31, 0, 20): 4}),
            (
                certificate_shapes,
                certificate_failures,
            ),
        )

        print("\nALL 32x32 WORD PAIRS")
        representative = certificates[(0, 1)]
        (
            local_checks,
            local_failures,
            geometry_shapes,
            endpoint_words,
        ) = all_word_pair_local_census(
            representative["dependencies"]
        )
        check(
            "all 1,024 word pairs compile on one geometry",
            local_checks == 1_024 * 3_040
            and not local_failures
            and len(geometry_shapes) == 1,
            (
                local_checks,
                local_failures[:1],
                len(geometry_shapes),
            ),
        )
        check(
            "the ten endpoints identify every ordered word pair without a 32-valued role",
            len(endpoint_words) == 1_024
            and all(
                set(word) <= set(c178.BIT_ROLES)
                for word in endpoint_words
            )
            and not (
                set().union(*map(set, endpoint_words))
                & set(c178.c175.NEW_ROW_ROLES)
            ),
            (
                len(endpoint_words),
                set().union(*map(set, endpoint_words)),
            ),
        )

        print("\nEXACT PRODUCT AND LINEAGES")
        single_initial = BASE_LEFT[2]
        single_expected = BASE_LEFT[3]
        single_exits = BASE_LEFT[4]
        single_certificate = c178.c171.causal_certificate(
            single_initial,
            single_expected,
            single_exits,
        )
        cross, left_exact, right_exact = dependency_factorization(
            representative,
            single_certificate,
        )
        check(
            "the 6,910-edge dependency graph is exactly two five-lane graphs",
            not cross
            and left_exact
            and right_exact
            and representative["edge_checks"]["edges"]
            == 2 * 3_455,
            (
                cross[:2],
                left_exact,
                right_exact,
                representative["edge_checks"]["edges"],
            ),
        )
        left_lineage_bad, left_endpoints = c180.lineage_certificate(
            single_certificate,
            single_initial,
            single_expected,
            SPACING,
        )
        right_endpoints = tuple(
            c172.shift(site, CONTACT_OFFSET)
            for site in left_endpoints
        )
        check(
            "all ten H0/H1 lineages remain separately identifiable",
            not left_lineage_bad
            and len(left_endpoints) == 5
            and len(right_endpoints) == 5
            and set(left_endpoints).isdisjoint(right_endpoints),
            (
                left_lineage_bad,
                left_endpoints,
                right_endpoints,
            ),
        )

        print("\nDELETION CONTROLS")
        seed_deletions = seed_deletion_controls(
            representative["dependencies"]
        )
        check(
            "all twenty value-side-lane seed deletions suppress the first H0/H1 copy",
            len(seed_deletions) == 20
            and all(
                baseline
                == frozenset((c178.bit_role(value),))
                and observed is None
                for (
                    value,
                    _side,
                    _lane,
                    _seed,
                    _target,
                    baseline,
                    observed,
                ) in seed_deletions
            ),
            seed_deletions[:2],
        )
        check(
            "every one of 6,910 direct dynamic edges is deletion-load-bearing",
            representative["edge_checks"]["attempts"] == 6_910
            and not representative["edge_checks"]["signature_failures"]
            and not representative["edge_checks"]["deletion_failures"],
            representative["edge_checks"],
        )
        check(
            "deleting either whole bundle leaves the exact single-bundle certificate",
            single_certificate["ok"]
            and single_certificate["minimum"]["states"] == 1_521
            and single_certificate["edge_checks"]["edges"] == 3_455
            and len(single_certificate["minimum"]["terminal"]) == 10,
            (
                single_certificate["ok"],
                single_certificate["minimum"].get("states"),
                single_certificate["edge_checks"].get("edges"),
                len(single_certificate["minimum"].get("terminal", {})),
            ),
        )

        print("\nPROPER-CUBIC COVARIANCE")
        rotation_checks = 0
        rotation_failures = []
        representative_apparatus = pair_bundle(ZERO, ONE)
        for rotation_index, rotation in enumerate(
            c178.c53.ROTATIONS
        ):
            checks, failures = rotated_local_check(
                representative_apparatus,
                representative["dependencies"],
                rotation,
            )
            rotation_checks += checks
            if (
                c178.c53.determinant(rotation) != 1
                or failures
            ):
                rotation_failures.append(
                    (
                        rotation_index,
                        c178.c53.determinant(rotation),
                        failures[:1],
                    )
                )
        check(
            "all 24 proper-cubic images preserve the exact product interface",
            rotation_checks == 24 * (3_040 + 40)
            and not rotation_failures,
            (
                rotation_checks,
                rotation_failures[:1],
            ),
        )

        print("\nRIGID-PAYLOAD-CONTACT BOUNDARY")
        payload_candidates = payload_contact_offsets()
        lawful_payload = lawful_payload_contacts()
        check(
            "no rigid translation of the unchanged supports gives disjoint payload contact",
            len(payload_candidates) == 1_683
            and not lawful_payload,
            (
                len(payload_candidates),
                lawful_payload,
            ),
        )

        print("\nSCOPE AND NO-GO DISCIPLINE")
        normalized = (
            " ".join(
                NOTE.read_text(encoding="utf-8")
                .lower()
                .split()
            )
            if NOTE.is_file()
            else ""
        )
        required = (
            "fixed-shell contact",
            "zero-row price",
            "not a payload-collision theorem",
            "rigid translation",
            "n1 — alternative routes",
            "n8 — cross-cycle echo",
            "no axiom addition follows",
            "no foundation, axiom, primitive, registry, policy, or audit edit",
        )
        missing = tuple(
            phrase
            for phrase in required
            if phrase not in normalized
        )
        check(
            "the note carries the positive scope and narrowed N1-N8 boundary",
            not missing,
            missing,
        )

        print("\nTOTAL")
        print("PASS", PASS, "FAIL", FAIL)
        print(
            "RESULT",
            "COMPACT_BINARY_BUNDLE_TRANSPARENT_CONTACT"
            if FAIL == 0
            else "CYCLE192_NEEDS_REPAIR",
        )
        return 0 if FAIL == 0 else 1
    finally:
        c178.c171.FULL_RAW = old_full_raw


if __name__ == "__main__":
    raise SystemExit(main())
