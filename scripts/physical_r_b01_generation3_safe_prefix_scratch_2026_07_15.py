#!/usr/bin/env python3
"""Stop the physical R_B01 bridge before its unsafe unary-W3 generation.

The retargeted byte grows allocator, port, OZ, W3, A_0_0, and A_1_2.  Every
row has at least two parents.  This prefix is integrated with the recurrent
rail and becomes the source for a fresh A_1_2-to-root adapter search.
"""

from __future__ import annotations

import r_b01_word_retargeted_cycle121_writer_probe_2026_07_15 as word
import recurrent_post_oz_payload_prototype_2026_07_15 as payload
import recurrent_socket_to_cycle129_downstream_interface_probe_2026_07_15 as old


c112 = payload.c112
c53 = c112.c53
cell = payload.cell
c141 = payload.c141
screen = payload.screen
ALLOCATOR = (4, 4, -3)
PORT = (5, 4, -3)
GENERATIONS = old.GROUPS[:4]
START = GENERATIONS[-1][0][0]


def build():
    records = {**c112.SOURCE, **word.GROWN_OUTPUTS}
    table = {}
    outputs = {}
    observed = []
    for sites, output in (
        ((ALLOCATOR,), "R_A01"),
        ((PORT,), "R_B01"),
        *GENERATIONS,
    ):
        local = c53.local_signature(records, sites[0])
        canonical = cell.canonical(local)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise RuntimeError((sites, prior, output, canonical))
        table[canonical] = output
        orbit = cell.raw_orbit(local, output)
        matches = tuple(sorted(
            target
            for target in c53.open_candidates(records)
            if c53.local_signature(records, target) in orbit
        ))
        observed.append((sites, matches, local))
        for site in sites:
            records[site] = output
            outputs[site] = output
    raw = c141.replacement_probe.merge_raw(*(
        cell.raw_orbit(signature, output)
        for signature, output in table.items()
    ))
    return records, table, raw, outputs, tuple(observed)


RECORDS, TABLE, NEW_RAW, PREFIX_OUTPUTS, OBSERVED = build()
WORD_DELTA = {
    local: values
    for local, values in word.FULL_RAW.items()
    if local not in c112.FULL_RAW
}
FULL_RAW = c141.replacement_probe.merge_raw(
    payload.FULL_RAW, WORD_DELTA, NEW_RAW
)
POST_WORD_OUTPUTS = {
    site: value
    for site, value in word.GROWN_OUTPUTS.items()
    if site not in c112.GROWN_OUTPUTS
}
PHYSICAL_OUTPUTS = {**POST_WORD_OUTPUTS, **PREFIX_OUTPUTS}
COMBINED_OUTPUTS = {
    **c112.GROWN_OUTPUTS,
    **PHYSICAL_OUTPUTS,
    **payload.OUTPUTS,
}
COMPILED = c112.compile_conditions(
    c112.SOURCE, COMBINED_OUTPUTS, FULL_RAW, payload.IGNORED
)
WRONG = screen.wrong_value_details(
    COMPILED, COMBINED_OUTPUTS, payload.IGNORED
)


def main() -> None:
    mismatches = tuple(
        (declared, matches, local)
        for declared, matches, local in OBSERVED
        if tuple(sorted(declared)) != matches
    )
    print("MISMATCHES", mismatches)
    print(
        "TABLE", len(TABLE), "NEW_RAW", len(NEW_RAW),
        "FULL_RAW", len(FULL_RAW),
        "MULTI", sum(len(values) != 1 for values in FULL_RAW.values()),
    )
    print(
        "COMPILED", len(COMBINED_OUTPUTS), len(COMPILED.conditions),
        "UNEXPECTED", len(COMPILED.unexpected_targets),
        tuple(sorted(COMPILED.unexpected_targets)),
        "WRONG", len(WRONG),
    )
    terminal = {**c112.SOURCE, **COMBINED_OUTPUTS}
    print("TERMINAL_ENABLED", c141.enabled(terminal, FULL_RAW))
    print("START", START, RECORDS[START])
    print(
        "RESULT",
        "PHYSICAL_R_B01_GENERATION3_SAFE_PREFIX"
        if not mismatches
        and all(len(values) == 1 for values in FULL_RAW.values())
        and c141.enabled(terminal, FULL_RAW) == payload.IGNORED
        else "PREFIX_REJECTED",
    )


if __name__ == "__main__":
    main()
