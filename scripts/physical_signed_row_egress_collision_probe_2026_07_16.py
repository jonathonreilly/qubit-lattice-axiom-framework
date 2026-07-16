#!/usr/bin/env python3
"""Pin the two exact zero-delta failures at the signed-row output seam."""

from __future__ import annotations

from itertools import product

import physical_row_reader_payload_tap_probe_2026_07_16 as tap


ported = tap.ported
terminal = ported.terminal
cell = tap.cell
c53 = tap.c53
five = ported.five
FRAME = tap.FRAME
ROWS = tuple(product((0, 1), repeat=5))
SOURCE = ported.SOURCE
SIGN_TARGET = (0, 0, 1)
SIGN_PORT = (0, 0, 2)


def terminal_sign_records(row):
    records = {
        SOURCE: five.ROW_ROLE[row],
        terminal.INDEX_SITES[4]: terminal.INDEX_ROLES[4],
    }
    for direction in c53.DIRECTIONS:
        site = c53.add(SIGN_TARGET, direction)
        if site not in {SOURCE, terminal.INDEX_SITES[4]}:
            records[site] = FRAME
    return records


def proposed_open_port_local(row):
    records = {
        SOURCE: five.ROW_ROLE[row],
        **{
            site: role
            for site, role in zip(
                ported.INDEX_SITES,
                ported.INDEX_ROLES,
                strict=True,
            )
        },
    }
    return c53.canonical_signature(
        c53.local_signature(records, SIGN_TARGET)
    )


PROPOSED_TABLE = {
    proposed_open_port_local(row): ported.bit(row[4])
    for row in ROWS
}
PROPOSED_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in PROPOSED_TABLE.items()
))
OVERLAP = set(PROPOSED_RAW) & set(tap.MERGED_RAW)
CONFLICTS = {
    signature: (tap.MERGED_RAW[signature], PROPOSED_RAW[signature])
    for signature in OVERLAP
    if tap.MERGED_RAW[signature] != PROPOSED_RAW[signature]
}


def main() -> int:
    terminal_failures = []
    identity_failures = []
    for row in ROWS:
        records = terminal_sign_records(row)
        occupied = {
            c53.add(SIGN_TARGET, direction)
            for direction in c53.DIRECTIONS
            if c53.add(SIGN_TARGET, direction) in records
        }
        if len(occupied) != 6 or SIGN_PORT not in occupied:
            terminal_failures.append((row, occupied))
        if proposed_open_port_local(row) != tap.tap_local(five.ROW_ROLE[row]):
            identity_failures.append(row)

    output_pairs = {
        (
            next(iter(tap.MERGED_RAW[signature])),
            next(iter(PROPOSED_RAW[signature])),
        )
        for signature in CONFLICTS
    }
    print(
        "TERMINAL",
        len(ROWS),
        len(terminal_failures),
        "all-six-neighbors-occupied",
    )
    print(
        "OPEN_PORT_IDENTITY",
        len(ROWS),
        len(identity_failures),
        "equals-whole-row-tap",
    )
    print(
        "LAW",
        len(tap.MERGED_RAW),
        len(PROPOSED_TABLE),
        len(PROPOSED_RAW),
        len(OVERLAP),
        len(CONFLICTS),
        len(set(PROPOSED_RAW) - set(tap.MERGED_RAW)),
    )
    print("OUTPUT_PAIRS", len(output_pairs), sorted(output_pairs)[:8])
    if terminal_failures or identity_failures or len(CONFLICTS) != 768:
        print(
            "FAILURE_SAMPLE",
            (
                terminal_failures[:2],
                identity_failures[:2],
                tuple(CONFLICTS.items())[:2],
            ),
        )

    result = (
        len(PROPOSED_TABLE) == 32
        and len(PROPOSED_RAW) == 768
        and len(OVERLAP) == len(CONFLICTS) == 768
        and not (set(PROPOSED_RAW) - set(tap.MERGED_RAW))
        and not terminal_failures
        and not identity_failures
        and all(
            existing == frozenset((five.ROW_ROLE[row],))
            for row in ROWS
            for signature in (proposed_open_port_local(row),)
            for existing in (tap.MERGED_RAW[signature],)
        )
        and all(
            proposed == frozenset((ported.bit(row[4]),))
            for row in ROWS
            for signature in (proposed_open_port_local(row),)
            for proposed in (PROPOSED_RAW[signature],)
        )
    )
    print(
        "RESULT",
        "PHYSICAL_SIGNED_ROW_EGRESS_COLLISION" if result else "OPEN",
    )
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
