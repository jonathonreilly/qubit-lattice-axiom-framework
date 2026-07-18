#!/usr/bin/env python3
"""Cycle 108: repair the Cycle-101/Cycle-104 phase collision exactly.

Cycle 104 is role-closed against Cycle 100, but two of its phase aliases are
unary inputs introduced by Cycle 101.  This runner replaces only those two
aliases with live unary-inert roles, then exhausts the complete 22-record
reader against eight renewed rail slices and the inherited certificate-to-type
append.  Every rule is simultaneously live.

Authority: none.  This runner writes nothing and changes no foundation,
registry, queue, policy, selected-law, or git state.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path

import onsite_alphabet_closed_frame_rail_cycle104_2026_07_15 as c104
import zero_binary_source_endpoint_macroblock_bind_cycle100_2026_07_15 as c100
import zero_source_relational_first_harness_cycle101_2026_07_15 as c101


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "FRAGMENT_SAFE_ROLE_REMAP_TYPE_INTEGRATION_CYCLE108_NOTE_2026-07-15.md"

Coord = c104.Coord
Signature = c104.Signature
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


# Keep every Cycle-104 choice except the two roles which become unary-active
# when Cycle 101's reader rows are present.
ROLE_MAP = dict(c104.ROLE_MAP)
ROLE_MAP["D_1_1"] = "J1"
ROLE_MAP["C_3_1"] = "J2"

REMAPPED_RAW = c104.relabel_raw(ROLE_MAP)
INTEGRATED_RAW = c104.merge_raw(
    c100.COMBINED_RAW,
    c101.FRAGMENT_RAW,
    REMAPPED_RAW,
)
NINE_SLICES = c104.rail_sequence(9, ROLE_MAP)
HORIZON = 96

TYPE_SITE: Coord = (4, 5, 1)
TYPE_CONTENT = "R_B21"
TYPE_FRONT = {TYPE_SITE: frozenset((TYPE_CONTENT,))}


def enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: INTEGRATED_RAW[local]
        for target in c100.c53.open_candidates(records)
        if (local := c100.c53.local_signature(records, target)) in INTEGRATED_RAW
    }


def unary_outputs(
    role: str,
    *tables: dict[Signature, frozenset[str]],
) -> frozenset[str]:
    return frozenset(
        output
        for table in tables
        for local, values in table.items()
        if len(local) == 1 and local[0][1] == role
        for output in values
    )


@dataclass(frozen=True)
class GraphStats:
    states: int
    edges: int
    terminals: int
    terminal_frontiers: tuple[tuple[tuple[Coord, frozenset[str]], ...], ...]
    max_front: int
    bad: tuple[object, ...]


def integrated_graph() -> GraphStats:
    """All reader schedules x 96 ordered rail appends x optional TYPE append."""

    start = (frozenset(), 0, False)
    queue = deque((start,))
    seen = {start}
    edges = 0
    terminals: list[tuple[tuple[Coord, frozenset[str]], ...]] = []
    max_front = 0
    bad: list[object] = []

    while queue:
        fragment_state, rail_prefix, typed = queue.popleft()
        records = dict(c101.TERMINAL)
        records.update({
            site: c101.FRAGMENT_OUTPUTS[site]
            for site in fragment_state
        })
        records.update(dict(NINE_SLICES[:rail_prefix]))
        if typed:
            records[TYPE_SITE] = TYPE_CONTENT

        actual = enabled(records)
        allowed = {
            site: frozenset((c101.FRAGMENT_OUTPUTS[site],))
            for site in c101.FRAGMENT_SITES - fragment_state
        }
        rail_site, rail_content = NINE_SLICES[rail_prefix]
        allowed[rail_site] = frozenset((rail_content,))
        if c101.CERTIFICATE in fragment_state and not typed:
            allowed.update(TYPE_FRONT)

        wrong = {
            site: values
            for site, values in actual.items()
            if allowed.get(site) != values
        }
        if wrong:
            bad.append((fragment_state, rail_prefix, typed, wrong))
            break

        max_front = max(max_front, len(actual))
        if (
            len(fragment_state) == len(c101.FRAGMENT_SITES)
            and rail_prefix == HORIZON
            and typed
        ):
            terminals.append(tuple(sorted(actual.items())))
            continue

        futures: list[tuple[frozenset[Coord], int, bool]] = []
        for site in actual:
            if site in c101.FRAGMENT_SITES:
                futures.append((fragment_state | {site}, rail_prefix, typed))
            elif site == TYPE_SITE:
                futures.append((fragment_state, rail_prefix, True))
            elif rail_prefix < HORIZON and site == rail_site:
                futures.append((fragment_state, rail_prefix + 1, typed))

        if not futures:
            bad.append((fragment_state, rail_prefix, typed, "dead", actual))
            break
        for future in futures:
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)

    return GraphStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminals),
        terminal_frontiers=tuple(sorted(set(terminals))),
        max_front=max_front,
        bad=tuple(bad),
    )


def mapping_and_table_contract() -> None:
    section("A - Exact two-role repair and integrated table")
    check("A01 Cycle 108 note exists", NOTE.is_file())
    changes = {
        role: (c104.ROLE_MAP[role], ROLE_MAP[role])
        for role in ROLE_MAP
        if ROLE_MAP[role] != c104.ROLE_MAP[role]
    }
    check(
        "A02 repair changes exactly R_B12 and R_B31 phase aliases",
        changes == {
            "D_1_1": ("R_B12", "J1"),
            "C_3_1": ("R_B31", "J2"),
        },
        str(changes),
    )
    check(
        "A03 repaired map remains 36-role injective and onsite closed",
        set(ROLE_MAP) == c104.PHASE_DOMAIN
        and len(set(ROLE_MAP.values())) == 36
        and set(ROLE_MAP.values()) <= c104.c89.FULL_ROLES,
    )
    check(
        "A04 removed aliases are exactly Cycle-101's unary inputs",
        unary_outputs("R_B12", c101.FRAGMENT_RAW) == {"R_B13"}
        and unary_outputs("R_B31", c101.FRAGMENT_RAW) == {"R_B32"},
    )
    check(
        "A05 J1/J2 are unary-inert in the complete pre-rail union",
        not unary_outputs("J1", c100.COMBINED_RAW, c101.FRAGMENT_RAW)
        and not unary_outputs("J2", c100.COMBINED_RAW, c101.FRAGMENT_RAW),
    )
    source_counts = Counter(c100.SOURCE.values())
    check(
        "A06 J1/J2 reuse is explicit at one pre-existing source site each",
        source_counts["J1"] == source_counts["J2"] == 1,
        str((source_counts["J1"], source_counts["J2"])),
    )
    check(
        "A07 relabelled rail keeps 1,080 single-valued inputs",
        len(REMAPPED_RAW) == 1_080
        and all(len(values) == 1 for values in REMAPPED_RAW.values()),
    )
    overlap_base = set(REMAPPED_RAW) & set(c100.COMBINED_RAW)
    overlap_fragment = set(REMAPPED_RAW) & set(c101.FRAGMENT_RAW)
    check(
        "A08 rail inputs are disjoint from Cycle 100 and Cycle 101",
        not overlap_base and not overlap_fragment,
        str((tuple(overlap_base)[:1], tuple(overlap_fragment)[:1])),
    )
    check(
        "A09 integrated union has 6,896 single-valued inputs",
        len(INTEGRATED_RAW) == 6_896
        and all(len(values) == 1 for values in INTEGRATED_RAW.values()),
    )
    contents = {
        content
        for local, values in INTEGRATED_RAW.items()
        for _direction, content in local
    } | {
        output
        for values in INTEGRATED_RAW.values()
        for output in values
    }
    check(
        "A10 every integrated input/output remains in FULL_ROLES",
        contents <= c104.c89.FULL_ROLES,
    )


def sequential_and_type_contract() -> None:
    section("B - Eight-slice sequential contacts and inherited TYPE")
    start_site, start_content = c101.FRAGMENT_GROUPS[0][0]
    empty_failures = []
    full_failures = []
    typed_failures = []
    debris_uses = []
    debris_sites = {
        site
        for site, content in c100.SOURCE.items()
        if content in {"J1", "J2"}
    }
    for prefix in range(HORIZON + 1):
        rail_site, rail_content = NINE_SLICES[prefix]
        rail_front = {rail_site: frozenset((rail_content,))}

        empty = dict(c101.TERMINAL)
        empty.update(dict(NINE_SLICES[:prefix]))
        expected_empty = dict(rail_front)
        expected_empty[start_site] = frozenset((start_content,))
        if enabled(empty) != expected_empty:
            empty_failures.append((prefix, expected_empty, enabled(empty)))

        complete = dict(empty)
        complete.update(c101.FRAGMENT_OUTPUTS)
        expected_full = dict(rail_front)
        expected_full.update(TYPE_FRONT)
        if enabled(complete) != expected_full:
            full_failures.append((prefix, expected_full, enabled(complete)))

        complete[TYPE_SITE] = TYPE_CONTENT
        if enabled(complete) != rail_front:
            typed_failures.append((prefix, rail_front, enabled(complete)))

        local = c100.c53.local_signature(empty, rail_site)
        used = {
            c104.add(rail_site, direction)
            for direction, _content in local
        } & debris_sites
        if used:
            debris_uses.append((prefix, rail_site, tuple(sorted(used))))

    check(
        "B01 all 97 empty-reader prefixes expose exactly reader plus rail fronts",
        not empty_failures,
        str(empty_failures[:1]),
    )
    check(
        "B02 all 97 complete-reader prefixes expose exactly TYPE plus rail fronts",
        not full_failures,
        str(full_failures[:1]),
    )
    check(
        "B03 all 97 typed prefixes expose only the next rail front",
        not typed_failures,
        str(typed_failures[:1]),
    )
    check(
        "B04 neither pre-existing J1/J2 debris site supplies an intended rail row",
        not debris_uses,
        str(debris_uses[:1]),
    )

    complete_fragment = dict(c101.TERMINAL)
    complete_fragment.update(c101.FRAGMENT_OUTPUTS)
    type_signature = c100.c53.local_signature(complete_fragment, TYPE_SITE)
    check(
        "B05 CERT alone is the exact inherited TYPE signature",
        type_signature == (((-1, 0, 0), "R_B40"),),
        str(type_signature),
    )
    check(
        "B06 TYPE is supplied only by the remapped rail family",
        REMAPPED_RAW.get(type_signature) == frozenset((TYPE_CONTENT,))
        and c100.COMBINED_RAW.get(type_signature) is None
        and c101.FRAGMENT_RAW.get(type_signature) is None,
    )


def asynchronous_and_covariance_contract() -> None:
    section("C - Complete asynchronous product and proper-cubic covariance")
    stats = integrated_graph()
    expected_terminal = (((NINE_SLICES[HORIZON][0], frozenset((NINE_SLICES[HORIZON][1],))),),)
    check(
        "C01 full reader x eight-slice rail x TYPE graph has 22,310 states",
        stats.states == 22_310,
        str(stats),
    )
    check(
        "C02 all 91,338 legal asynchronous edges are parasite-free",
        stats.edges == 91_338 and not stats.bad,
        str(stats),
    )
    check(
        "C03 graph has one complete terminal exposing only slice-nine start",
        stats.terminals == 1
        and stats.terminal_frontiers == expected_terminal,
        str(stats.terminal_frontiers),
    )
    check("C04 maximum simultaneous lawful frontier is seven", stats.max_front == 7)

    covariance_failures = []
    covariance_controls = 0
    for signature, values in INTEGRATED_RAW.items():
        for rotation in c100.c53.ROTATIONS:
            covariance_controls += 1
            actual = INTEGRATED_RAW.get(c100.c53.rotate_signature(signature, rotation))
            if actual != values:
                covariance_failures.append((signature, rotation, values, actual))
                break
        if covariance_failures:
            break
    check(
        "C05 all 165,504 proper-cubic raw images preserve output",
        covariance_controls == 6_896 * 24 and not covariance_failures,
        str(covariance_failures[:1]),
    )


def scope_contract() -> None:
    section("D - Scope, no-go discipline, and constitutional disposition")
    note = NOTE.read_text(encoding="utf-8").lower()
    check(
        "D01 note names the repaired integration edge",
        "fragment_safe_role_remap" in note,
    )
    check(
        "D02 note preserves CERT_TO_TYPE as positive contact",
        "cert_to_type" in note and "positive" in note,
    )
    check(
        "D03 note withholds unbounded and complete-compiler claims",
        "does not prove unbounded" in note and "does not complete the compiler" in note,
    )
    check(
        "D04 note contains the full N1-N8 gate",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "D05 note checks the approved primitive registry without adding one",
        all(name in note for name in ("ref_scale", "ref_kinetic", "ref_realized_state"))
        and "no new primitive" in note,
    )
    check(
        "D06 note makes no foundation or axiom edit",
        "no foundation edit" in note and "no axiom addition" in note,
    )
    check(
        "D07 Cycle 108 writes only its runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    mapping_and_table_contract()
    sequential_and_type_contract()
    asynchronous_and_covariance_contract()
    scope_contract()
    print(
        f"\nMAP_ROLES={len(ROLE_MAP)} RAIL_RAW={len(REMAPPED_RAW)} "
        f"UNION_RAW={len(INTEGRATED_RAW)} ASYNC_STATES=22310 ASYNC_EDGES=91338"
    )
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
