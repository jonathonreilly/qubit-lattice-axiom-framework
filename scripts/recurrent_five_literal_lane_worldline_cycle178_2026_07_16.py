#!/usr/bin/env python3
"""Cycle 178: recurrent five-lane H0/H1 worldline bundle.

Five translated copies of the four-period recurrent carrier each transport one
literal H0/H1 record.  Together the lanes encode all 32 signed-Pauli row words
without using a 32-valued payload role.  The probe certifies per-lane lineage,
bundle factorization, causal-layer speed, and an explicit decoder-facing port
contract.

This runner has no authority.  It edits no foundation, axiom, primitive,
registry, policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import autonomous_signed_row_recurrent_sidecar_cycle171_2026_07_16 as c171
import clean_row_alphabet_component_replacement_cycle175_2026_07_16 as c175
import recurrent_carrier_matter_kinematics_cycle172_2026_07_16 as c172


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RECURRENT_FIVE_LITERAL_LANE_WORLDLINE_CYCLE178_NOTE_2026-07-16.md"
)

cell = c171.cell
c53 = c171.c53
Coord = tuple[int, int, int]

H0 = c175.ported.d.H0
H1 = c175.ported.d.H1
BIT_ROLES = (H0, H1)
WORDS = tuple(product((0, 1), repeat=5))
LANE_SPACING = 200
LANE_OFFSETS = tuple(
    (0, LANE_SPACING * lane, 0)
    for lane in range(5)
)
SEED_SITES = tuple(
    c172.shift(c172.payload_site(c172.SEED_X), offset)
    for offset in LANE_OFFSETS
)
G4_SITES = tuple(
    c172.shift(c172.payload_site(c172.GENERATION_X[-1]), offset)
    for offset in LANE_OFFSETS
)
ENDPOINT_SITES = tuple(
    c172.shift(c172.payload_site(c172.COPY_X[-1]), offset)
    for offset in LANE_OFFSETS
)
PROPAGATION_DIRECTION = (-1, 0, 0)

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


def bit_role(value: int) -> str:
    return H1 if value else H0


BIT_CARRIER_TABLE = c171.canonical_sidecar_table(BIT_ROLES)
BIT_CARRIER_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in BIT_CARRIER_TABLE.items()
))
FULL_RAW = cell.merge_raw(c175.CANDIDATE169_RAW, BIT_CARRIER_RAW)
RAW_CONFLICTS = {
    signature: values
    for signature, values in FULL_RAW.items()
    if len(values) != 1
}


def translated(records: dict[Coord, str], offset: Coord) -> dict[Coord, str]:
    return {
        c172.shift(site, offset): role
        for site, role in records.items()
    }


def translated_values(
    values: dict[Coord, frozenset[str]],
    offset: Coord,
) -> dict[Coord, frozenset[str]]:
    return {
        c172.shift(site, offset): roles
        for site, roles in values.items()
    }


def bundle_source(word: tuple[int, ...]) -> dict[Coord, str]:
    source = {}
    for value, offset in zip(word, LANE_OFFSETS, strict=True):
        lane = translated(c172.source(bit_role(value)), offset)
        overlap = set(source) & set(lane)
        if overlap:
            raise ValueError(("source-overlap", offset, tuple(sorted(overlap))[:3]))
        source.update(lane)
    return source


def bundle_outputs(word: tuple[int, ...]) -> dict[Coord, str]:
    expected = {}
    for value, offset in zip(word, LANE_OFFSETS, strict=True):
        lane = translated(c172.outputs(bit_role(value)), offset)
        overlap = set(expected) & set(lane)
        if overlap:
            raise ValueError(("output-overlap", offset, tuple(sorted(overlap))[:3]))
        expected.update(lane)
    return expected


def bundle_exits() -> dict[Coord, frozenset[str]]:
    exits = {}
    for offset in LANE_OFFSETS:
        lane = translated_values(c172.EXITS, offset)
        overlap = set(exits) & set(lane)
        if overlap:
            raise ValueError(("exit-overlap", offset, tuple(sorted(overlap))[:3]))
        exits.update(lane)
    return exits


BUNDLE_EXITS = bundle_exits()


def lane_index(site: Coord) -> int:
    distances = tuple(
        abs(site[1] - offset[1])
        for offset in LANE_OFFSETS
    )
    return min(range(5), key=distances.__getitem__)


def cross_lane_edges(dependencies):
    return tuple(
        (parent, target)
        for target, parents in dependencies.items()
        for parent in parents
        if lane_index(parent) != lane_index(target)
    )


def lane_payload_sites(lane: int) -> tuple[Coord, ...]:
    offset = LANE_OFFSETS[lane]
    return tuple(
        c172.shift(c172.payload_site(x), offset)
        for x in range(c172.SEED_X, c172.COPY_X[-1] + 1)
    )


def bundle_lineage(certificate, initial, expected):
    direct = c172.direct_parents(
        initial,
        expected,
        certificate["dependencies"],
    )
    failures = []
    endpoints = []
    for lane in range(5):
        payloads = lane_payload_sites(lane)
        payload_set = set(payloads)
        children = {site: [] for site in payloads}
        for index, target in enumerate(payloads[1:], 1):
            parents = tuple(sorted(direct[target] & payload_set))
            if parents != (payloads[index - 1],):
                failures.append(("parents", lane, target, parents))
            for parent in parents:
                children[parent].append(target)
        lane_endpoints = tuple(
            site for site, descendants in children.items()
            if not descendants
        )
        if lane_endpoints != (payloads[-1],):
            failures.append(("endpoints", lane, lane_endpoints))
        endpoints.extend(lane_endpoints)
    return tuple(failures), tuple(endpoints)


def representative_words():
    return (
        (0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1),
        (1, 0, 1, 0, 1),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    old_full_raw = c171.FULL_RAW
    c171.FULL_RAW = FULL_RAW
    try:
        print("AUTHORITY, ENCODING, AND LAW")
        check("Cycle-178 review note exists", NOTE.is_file())
        check(
            "the five lanes use exactly the retained orthogonal literal roles",
            BIT_ROLES == (c175.fanout.bit(0), c175.fanout.bit(1))
            and len(WORDS) == 32
            and all(
                tuple(bit_role(bit) for bit in row)
                == tuple(
                    c175.fanout.bit(bit)
                    for bit in row
                )
                for row in WORDS
            ),
            BIT_ROLES,
        )
        check(
            "the two-value recurrent delta is compact and deterministic",
            len(BIT_CARRIER_TABLE) == 12
            and len(BIT_CARRIER_RAW) == 288
            and len(FULL_RAW) == 101_996
            and not RAW_CONFLICTS,
            (
                len(BIT_CARRIER_TABLE),
                len(BIT_CARRIER_RAW),
                len(FULL_RAW),
                len(RAW_CONFLICTS),
            ),
        )

        print("\nSINGLE-LANE CERTIFICATES")
        single = {}
        for role in BIT_ROLES:
            single[role] = c171.causal_certificate(
                c172.source(role),
                c172.outputs(role),
                c172.EXITS,
            )
        check(
            "both H0 and H1 close through G4 with one exact lineage",
            all(certificate["ok"] for certificate in single.values())
            and {
                (
                    certificate["minimum"]["states"],
                    certificate["edge_checks"]["edges"],
                    len(certificate["unordered"]),
                )
                for certificate in single.values()
            } == {(305, 691, 0)},
            {
                role: certificate.get("discovery", {}).get("error")
                for role, certificate in single.items()
            },
        )
        single_lineages = {
            role: c172.lineage_certificate(
                certificate,
                c172.source(role),
                c172.outputs(role),
            )
            for role, certificate in single.items()
        }
        check(
            "both literal values retain the Cycle-172 steady causal ratio",
            all(
                not lineage["degree_failures"]
                and lineage["generation_depths"] == (0, 19, 71, 123, 175)
                and lineage["steady_ratios"]
                == (c172.Fraction(1, 13),) * 3
                for lineage in single_lineages.values()
            ),
            single_lineages,
        )

        print("\nFIVE-LANE ALL-32 BUNDLE")
        certificates = {}
        shapes = Counter()
        failures = {}
        for word in WORDS:
            initial = bundle_source(word)
            expected = bundle_outputs(word)
            certificate = c171.causal_certificate(
                initial,
                expected,
                BUNDLE_EXITS,
            )
            certificates[word] = certificate
            if not certificate["ok"]:
                failures[word] = certificate
                continue
            shapes[(
                certificate["minimum"]["states"],
                certificate["edge_checks"]["edges"],
                certificate["minimum"]["max_frontier"],
                certificate["maximum"]["max_frontier"],
                len(certificate["unordered"]),
                len(certificate["minimum"]["terminal"]),
            )] += 1
        check(
            "all 32 five-bit words close on five independent recurrent lanes",
            not failures
            and shapes == {(1_521, 3_455, 18, 16, 0, 10): 32},
            (shapes, tuple(failures)[:2]),
        )

        mixed = (1, 0, 1, 0, 1)
        mixed_initial = bundle_source(mixed)
        mixed_expected = bundle_outputs(mixed)
        mixed_certificate = certificates[mixed]
        lineage_failures, endpoints = bundle_lineage(
            mixed_certificate,
            mixed_initial,
            mixed_expected,
        )
        check(
            "the encoded word has five disjoint payload lineages and five endpoints",
            not lineage_failures
            and endpoints == ENDPOINT_SITES
            and not cross_lane_edges(mixed_certificate["dependencies"]),
            (
                lineage_failures,
                endpoints,
                cross_lane_edges(mixed_certificate["dependencies"])[:3],
            ),
        )
        check(
            "the literal word is conserved without any 32-valued payload record",
            all(
                mixed_expected[site] == bit_role(mixed[lane])
                for lane in range(5)
                for site in lane_payload_sites(lane)[1:]
            )
            and not (
                {
                    mixed_expected[site]
                    for lane in range(5)
                    for site in lane_payload_sites(lane)[1:]
                }
                & set(c175.NEW_ROW_ROLES)
            ),
            {
                mixed_expected[site]
                for lane in range(5)
                for site in lane_payload_sites(lane)[1:]
            }
            & set(c175.NEW_ROW_ROLES),
        )

        print("\nDECODER-FACING PORT CONTRACT")
        check(
            "the five seed and endpoint sites are disjoint and ordered",
            len(set(SEED_SITES)) == 5
            and len(set(G4_SITES)) == 5
            and len(set(ENDPOINT_SITES)) == 5
            and all(
                (
                    endpoint[0] - seed[0],
                    endpoint[1] - seed[1],
                    endpoint[2] - seed[2],
                ) == (-18, 0, 0)
                for seed, endpoint in zip(
                    SEED_SITES,
                    ENDPOINT_SITES,
                    strict=True,
                )
            ),
            (SEED_SITES, G4_SITES, ENDPOINT_SITES),
        )

        print("\nSCOPE")
        note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
        normalized_note = " ".join(note.split())
        check(
            "review note states the five-rail cost and physical scope",
            "five translated recurrent rails" in normalized_note
            and "No 32-valued payload role" in normalized_note
            and "not a transported qubit-state theorem" in normalized_note
            and "distributed five-bit bundle" in normalized_note
            and "generated finite composition" in normalized_note
            and "silent global sectors" in normalized_note
            and "decoder-facing port contract" in normalized_note
            and "No axiom addition follows" in normalized_note
            and "6bd03383ea" in normalized_note
            and "caf3687c93b4" in normalized_note,
        )

        print("\nACCOUNTING")
        print("BIT_ROLES", BIT_ROLES)
        print("LANE_SPACING", LANE_SPACING)
        print("SEED_SITES", SEED_SITES)
        print("G4_SITES", G4_SITES)
        print("ENDPOINT_SITES", ENDPOINT_SITES)
        print("PROPAGATION_DIRECTION", PROPAGATION_DIRECTION)
        print("BIT_CARRIER", len(BIT_CARRIER_TABLE), len(BIT_CARRIER_RAW), len(FULL_RAW))
        print("BUNDLE_SHAPES", shapes)
        print("PASS", PASS, "FAIL", FAIL)
        print(
            "RESULT",
            "RECURRENT_FIVE_LITERAL_LANE_WORLDLINE"
            if FAIL == 0
            else "CYCLE178_OPEN",
        )
        return int(FAIL != 0)
    finally:
        c171.FULL_RAW = old_full_raw


if __name__ == "__main__":
    raise SystemExit(main())
