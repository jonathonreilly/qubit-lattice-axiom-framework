# Handoff

This branch repairs the audited-failed `causal_impact_parameter_note` source
packet without editing audit results.

The old failure was that alpha/R^2 was fit against nominal `target_z` labels
while the source layer saturated near the generated boundary. This branch
enlarges the transverse source support to `HALF = 20`, emits source-anchor
diagnostics, fits against measured source-to-zero-field-detector-centroid
transverse separation, and adds runner checks that fail if the anchors are not
realized or the realized-b fit is not stable.

Scientific outcome:
- exact zero controls still pass;
- requested anchors are realized with max realized-b error `7.594e-02`;
- all tested variants are toward `5/5`;
- realized-b exponents are about `-1.9` to `-2.3` with minimum `R^2 = 0.944`;
- the repaired result is a steep inverse-power replay, not a `1/b` law;
- the old `c=0.5` finite-cone-boundary reading is removed.

Verification run:
- `python3 scripts/causal_impact_parameter_probe.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/causal_impact_parameter_probe.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/causal_impact_parameter_probe.py`
- `python3 -m py_compile scripts/causal_impact_parameter_probe.py`
- `git diff --check`

Do not land this branch directly. Reviewer extraction and independent audit
decide whether the row moves.
