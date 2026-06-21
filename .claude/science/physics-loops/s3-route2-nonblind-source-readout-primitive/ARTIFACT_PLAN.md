# Artifact Plan

## Produced

- Runner:
  `scripts/frontier_quark_route2_nonblind_source_readout_primitive_gate_no_go_2026_06_21.py`
- Note:
  `docs/QUARK_ROUTE2_NONBLIND_SOURCE_READOUT_PRIMITIVE_GATE_NO_GO_NOTE_2026-06-21.md`
- Output:
  `outputs/frontier_quark_route2_nonblind_source_readout_primitive_gate_no_go_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-nonblind-source-readout-primitive/`

## Verification Plan

1. Run the new gate verifier.
2. Run parent S3/Route-2 readout checks that this block cites.
3. Run `py_compile`, diff whitespace, ASCII, and overclaim scans.
4. Commit and publish one PR for this science block.
