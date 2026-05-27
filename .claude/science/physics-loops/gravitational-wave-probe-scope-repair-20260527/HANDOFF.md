# Handoff

## Summary

This block narrows `gravitational_wave_probe_note` to bounded finite-runner
sensitivity scope. It preserves:

- the honest negative for Poisson-field gravitational waves;
- distinguishability of imposed retarded sampling from instantaneous sampling;
- layer-dependent perturbation sensitivity; and
- distinguishability of an imposed `f^2` action term.

It removes physical PN/GR readout claims.

## Changed Files

- `docs/GRAVITATIONAL_WAVE_PROBE_NOTE.md`
- `scripts/frontier_grav_wave_post_newtonian.py`
- `.claude/science/physics-loops/gravitational-wave-probe-scope-repair-20260527/`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_grav_wave_post_newtonian.py
python3 scripts/vocab_lint.py --report-only docs/GRAVITATIONAL_WAVE_PROBE_NOTE.md scripts/frontier_grav_wave_post_newtonian.py .claude/science/physics-loops/gravitational-wave-probe-scope-repair-20260527/*.md
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

## Reviewer Focus

- Confirm runner output no longer claims physical PN/GR derivation.
- Confirm the note preserves the negative Poisson-wave result.
- Confirm no audit verdict was applied manually.
