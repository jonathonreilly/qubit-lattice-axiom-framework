# Handoff

This PR repairs one audited-conditional science row:

`gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification_narrow_theorem_note_2026-05-17`

The previous source text still allowed the load-bearing proof to read as though `rho_(0,0)^env=1`, which reintroduced the missing `kappa_(0,0)=1` premise. The repaired note now uses an independent positive scale `lambda_env` and states that the actual trivial coefficient is `lambda_env*kappa_(0,0)`.

The companion runner now:

- proves `(1/lambda_env) C_Z = R_beta^env`;
- proves normalizing by the actual trivial coefficient gives `R_beta^env/kappa_(0,0)`;
- uses a concrete sample with `kappa_(0,0)=7/5` to catch accidental normalization.

Audit boundary: the row is queued for re-audit by generated audit metadata. This branch does not apply or imply an audit verdict.
