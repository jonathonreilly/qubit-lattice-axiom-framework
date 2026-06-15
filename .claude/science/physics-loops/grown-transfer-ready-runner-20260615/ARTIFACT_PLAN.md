# Artifact Plan

- Add a top-of-note `Runner` label pointing at `scripts/grown_transfer_basin_live_packet.py`.
- Add the matching runner cache label.
- Refresh the live packet cache because the verifier reads the note text.
- Run parser extraction, runner, cache refresh, and audit pipeline checks.
- Restore generated audit/publication outputs before commit.
