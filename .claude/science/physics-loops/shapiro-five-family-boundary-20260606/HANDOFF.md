# Handoff

This branch repairs the source-side Shapiro five-family portability blocker without editing audit results.

Changed artifacts:

- `scripts/shapiro_five_family_portability.py`
- `logs/runner-cache/shapiro_five_family_portability.txt`
- `docs/SHAPIRO_FIVE_FAMILY_PORTABILITY_CORRECTED_BOUNDARY_NOTE_2026-06-06.md`
- `.claude/science/physics-loops/shapiro-five-family-boundary-20260606/`

Verification:

- `PYTHONPATH=scripts python3 scripts/shapiro_five_family_portability.py`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/shapiro_five_family_portability.py`

Audit-facing point:

The old `0.065--0.071 rad` source-off values are now labeled diagnostic, not zero control. The true zero-source finite-c control is below `1e-12`, and the five-family sampled spread remains below `0.003 rad`.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3013
