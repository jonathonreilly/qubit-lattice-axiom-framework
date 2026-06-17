# Artifact Plan

## Source Note

- Update the top `Primary runner` declaration to
  `scripts/grown_transfer_basin_live_packet.py`.
- Explain that the live packet imports and verifies the slow replay runners.
- Keep the slow replay scripts and caches listed as current runner packet
  evidence.

## Verification

- Run `python3 scripts/grown_transfer_basin_live_packet.py`.
- Check that the source extractor now resolves the live packet as the primary
  runner and includes the replay scripts as helpers.
- Run `git diff --check`.
