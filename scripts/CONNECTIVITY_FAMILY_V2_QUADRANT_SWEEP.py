#!/usr/bin/env python3
"""Compatibility helpers for the old quadrant/radial connectivity scripts.

The former ``CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP`` module was superseded by
the parity-tapered elliptical sweep, but several archived fifth-family radial
checks still import its helper API.  Keep those checks reproducible by
re-exporting the shared measurement helpers and the earlier radial-shell
connectivity builder.
"""

from __future__ import annotations

from CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP import (  # noqa: F401
    H,
    MIN_EDGES,
    SHELL_COUNT,
    SOURCE_STRENGTH,
    SOURCE_Z,
    Family,
    RowResult,
    _centroid_z,
    _field_from_sources,
    _layer_centers,
    _mean,
    _measure_family,
    _neighbor_shell,
    _propagate,
    _radial_shell,
)


def _build_radial_shell_connectivity(fam: Family) -> Family:
    """Build the earlier radial-shell connectivity family.

    This is the fifth-family radial slice used by
    ``FIFTH_FAMILY_RADIAL_*``.  It intentionally differs from the current
    elliptical family: shells are ordinary radial shells around each layer's
    y/z center, with one parity-neighbor shell and a nearest-node edge floor.
    """

    pos = fam.positions
    layers = fam.layers
    centers = _layer_centers(pos, layers)
    adj: dict[int, list[int]] = {i: [] for i in range(len(pos))}

    for layer_idx in range(len(layers) - 1):
        src_layer = layers[layer_idx]
        dst_layer = layers[layer_idx + 1]
        cy_src, cz_src = centers[layer_idx]
        cy_dst, cz_dst = centers[layer_idx + 1]

        dst_by_shell: dict[int, list[int]] = {s: [] for s in range(SHELL_COUNT)}
        for dst in dst_layer:
            shell = _radial_shell(pos[dst][1], pos[dst][2], cy_dst, cz_dst)
            dst_by_shell[shell].append(dst)

        for src in src_layer:
            shell = _radial_shell(pos[src][1], pos[src][2], cy_src, cz_src)
            target_shells = [shell, _neighbor_shell(shell, layer_idx)]

            chosen: list[int] = []
            for target in target_shells:
                candidates = dst_by_shell.get(target, [])
                if not candidates:
                    continue
                best = min(
                    candidates,
                    key=lambda dst: (
                        (pos[dst][0] - pos[src][0]) ** 2
                        + (pos[dst][1] - pos[src][1]) ** 2
                        + (pos[dst][2] - pos[src][2]) ** 2
                    ),
                )
                if best not in chosen:
                    chosen.append(best)

            if not chosen:
                best = min(
                    dst_layer,
                    key=lambda dst: (
                        (pos[dst][0] - pos[src][0]) ** 2
                        + (pos[dst][1] - pos[src][1]) ** 2
                        + (pos[dst][2] - pos[src][2]) ** 2
                    ),
                )
                chosen.append(best)

            for dst in sorted(
                dst_layer,
                key=lambda d: (
                    (pos[d][0] - pos[src][0]) ** 2
                    + (pos[d][1] - pos[src][1]) ** 2
                    + (pos[d][2] - pos[src][2]) ** 2
                ),
            ):
                if len(chosen) >= MIN_EDGES:
                    break
                if dst not in chosen:
                    chosen.append(dst)
            adj[src].extend(chosen)

    return Family(pos, layers, adj)
