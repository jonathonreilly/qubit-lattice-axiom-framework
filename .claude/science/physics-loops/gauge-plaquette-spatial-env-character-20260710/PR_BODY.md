## Status

Bounded support.  This PR does not propose retained-grade closure of the
spatial-environment character-measure row.

## Auditor blocker reached

The prior audit found that the runner supplied a `rho_env` sequence instead of
computing it from the unmarked spatial Wilson environment or independently
checking the residual spectrum.

This block computes the static periodic `L_s=3`, `beta=6` 80-plaquette
environment coefficients without witness injection.  It also records why that
valid coefficient packet does not by itself prove the ordering-sensitive
post-compression source-residual identity.

## New science

- Exact marked-factor deletion identity:
  `rho_lambda = <conj(chi_lambda)/w>_full /
  (d_lambda <1/w>_full)`.
- Independent direct 80-plaquette estimator:
  `rho_lambda = <conj(chi_lambda)>_env/d_lambda`.
- Four hot/cold chains in each estimator family, block-jackknife errors, Haar
  controls, action-delta checks, conjugation checks, and fixed minimum
  production protocol.
- A doubled-slice literal-factor-deletion character-matrix discriminator that
  keeps the distinction between deletion before compression and algebraic
  stripping after compression explicit.

The full-Wilson estimator gives
`rho_(1,0)(6)=0.040787 +/- 0.003432`; the independent direct environment
estimator gives `0.047235 +/- 0.01165`.  The estimator spectra agree within
`0.76` combined standard errors and reject the old single-link packet in the
fundamental and adjoint channels by more than 100 reported jackknife errors.

## Claim boundary

The remaining blocker is

`R_stripped=(D_beta^loc)^(-1) M^(-1)
             (P_cls T_beta P_cls^*) M^(-1)`.

The class-sector compression must be formed before the operator factors are
stripped.  The companion doubled-slice runner performs literal factor deletion
before compression and is only a route discriminator; even a diagonal result
does not prove the desired residual equality.

## Artifacts

- [Target note](https://github.com/jonathonreilly/cl3-lattice-framework/blob/claude/science-fix/gauge_vacuum_plaquette_spatial_environment_character_measure-7824208b/docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md)
- Primary runner/cache:
  `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3.py`
  and its SHA-pinned runner cache.
- Companion runner/cache:
  `scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py`
  and its SHA-pinned runner cache.
- [Loop handoff](https://github.com/jonathonreilly/cl3-lattice-framework/blob/claude/science-fix/gauge_vacuum_plaquette_spatial_environment_character_measure-7824208b/.claude/science/physics-loops/gauge-plaquette-spatial-env-character-20260710/HANDOFF.md)
- [Trace gate](https://github.com/jonathonreilly/cl3-lattice-framework/blob/claude/science-fix/gauge_vacuum_plaquette_spatial_environment_character_measure-7824208b/.claude/science/physics-loops/gauge-plaquette-spatial-env-character-20260710/TRACE_GATE.md)
- [Claim certificate](https://github.com/jonathonreilly/cl3-lattice-framework/blob/claude/science-fix/gauge_vacuum_plaquette_spatial_environment_character_measure-7824208b/.claude/science/physics-loops/gauge-plaquette-spatial-env-character-20260710/CLAIM_STATUS_CERTIFICATE.md)

## Verification

```bash
python3 scripts/cached_runner_output.py scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3.py --check-only
python3 scripts/cached_runner_output.py scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py --check-only
python3 -m py_compile scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3.py scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py
python3 scripts/vocab_lint.py --fix docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3.py scripts/frontier_gauge_vacuum_plaquette_residual_environment_spectrum_actual_l3.py .claude/science/physics-loops/gauge-plaquette-spatial-env-character-20260710
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Review-loop disposition: pass with bounded claims.  Independent audit remains
required; this PR does not carry an audit verdict or effective-status change.
