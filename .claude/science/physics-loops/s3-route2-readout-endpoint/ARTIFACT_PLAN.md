# Artifact Plan

## Block20

Create:

- `docs/S3_TIME_FACTOR_RIGIDITY_READOUT_PRIMITIVE_SPLIT_NOTE_2026-06-21.md`
- `scripts/frontier_s3_time_factor_rigidity_readout_primitive_split_2026_06_21.py`
- `outputs/frontier_s3_time_factor_rigidity_readout_primitive_split_2026_06_21.txt`
- narrow tolerance repair in
  `scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py`
- loop pack files under `.claude/science/physics-loops/s3-route2-readout-endpoint/`

Verification:

- new runner;
- existing factor-rigidity runner;
- existing readout-primitive bridge assessment runner;
- exact time coupling runner;
- exact theta-to-slice parent runner;
- exact readout map runner;
- `py_compile`;
- `git diff --check`;
- overclaim wording scan.
