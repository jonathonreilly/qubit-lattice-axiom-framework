# Route Portfolio

## Route 1: Source-Runner Routing Sync

Change the source note's primary-runner declaration to
`scripts/grown_transfer_basin_live_packet.py` and keep the slow replay scripts
listed as replay inputs.

Expected movement: direct audit compute unblock for the target row after the
reviewer/audit pipeline rebuilds generated metadata.

## Route 2: New Audit Tooling Override

Rejected for this branch. Tooling overrides would be broader than needed and
could edit generated audit surfaces.

## Route 3: Rerun Slow Replay As Primary

Rejected for this branch. The slow replay is already represented by fresh
caches and remains too slow for the default queue path.
