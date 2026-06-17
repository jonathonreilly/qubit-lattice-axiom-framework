# Assumptions And Imports

## Current Premises

- The target source note remains a bounded-support repair packet.
- The live packet verifier imports `GROWN_TRANSFER_BASIN_SWEEP` and
  `GROWN_TRANSFER_BASIN_TARGETED`, so packet construction can still expose the
  slow replay source chain.
- The slow replay outputs are cache-backed evidence inputs, not newly imported
  mathematical constants.

## Remaining Imports

- `GATE_B_GROWN_JOINT_PACKAGE_NOTE.md` remains the upstream grown-geometry
  helper dependency.
- The finite row grid remains the audited scope proposed by the source note.

## Retired Import Or Blocker

- The branch removes the source-note ambiguity that made the slow targeted
  replay look like the default primary runner despite the note already
  describing `grown_transfer_basin_live_packet.py` as the live verifier.
