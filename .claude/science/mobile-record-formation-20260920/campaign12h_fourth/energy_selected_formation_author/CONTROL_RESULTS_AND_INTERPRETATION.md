# Energy-filter controls and interpretation

Root controls completed on 2026-09-23. The analytic draft remains unchanged
at SHA256 ecf6f39f0632d0f5fd7d4526ec66d39437019985655566cc9ad724837c7495c8.
The controls use the previously frozen physical finite-spin builder and
compact-projector implementation; their hashes are checked in the runner.
This source reuse is not an independent reconstruction.

Exact rational path algebra checks every one of the 16 resolved first marks
and 8 coherent first marks. The projected Grams are I/2 per resolved mark
and I per coherent edge. Every opposite-sign projected cross Gram vanishes
as a Laurent operator identity on the initial field space, not just at one
flux. The limiting first loss is therefore 8 kappa I in either convention.

Complete physical spin sectors at S=4,8,16,32 were used without an added
field cutoff. K=0.4 and delta=0.7. The expanding window width was fixed
before execution at R_S=2 sqrt(eta). For the resolved edge-zero positive mark:

| S | selected weight | norm error to F B psi | smooth-filter norm error |
|---|---:|---:|---:|
| 4 | 0.167052 | 0.809242 | 0.525678 |
| 8 | 0.437229 | 0.376481 | 0.237519 |
| 16 | 0.525817 | 0.159959 | 0.116124 |
| 32 | 0.510425 | 0.101940 | 0.055853 |

The smooth filter is 16²/(x²+16²), whose limit is g(h_F) F B psi. Its accepted
weight is not asserted to equal one half. The small-S sharp window excludes
much of the positive ordinary flat energy; it is not a good preparation at
every finite S. These data check approach to the stated asymptotic result,
not an accuracy guarantee for arbitrary size or a quantitative convergence
rate. Both positive and negative time purely Hamiltonian prepared motion were
also checked at t=0.4 in magnitude. Norm errors decrease from 0.107988 to
0.012906 over the same sizes, and finite norms stay one to floating precision.

The infinite flat reference uses circulation cutoff24. Its resolvent
truncation error is bounded analytically by the rational geometric tail
2(7/40)^24/(1-7/40). Its time-propagation truncation has a separate rational
Dyson-tail bound. Numerical solve residuals are reported separately; the
floating-point arithmetic is not interval certified.

The first successful execution reported an omitted-boundary residual as a
reference error bound without separating interior solve error and roundoff.
Root review found that qualification inadequate. Its original source, result,
streams and receipt remain in `first_control_run`, with an explicit diagnosis.
The current run replaces that label with the analytic truncation bound and
separate numerical residuals. No theorem or model was changed.

The equality of resolved/coherent first rates in the draft is a limiting
identity involving F. At finite S an energy projection can mix the two
opposite-sign output ranges, so the filtered finite-spin loss operators need
not coincide. Each finite model must use the loss belonging to its own
projected jumps. Full densities or histories of the two instruments are
never identified. The displayed count probabilities in the draft concern
their common limiting rates.

No cube propagation, full finite-spin filtered count simulation, reservoir
derivation or microscopic filter theorem was executed or inferred here.
The cube conclusion uses the independently checked no-point-spectrum
certificate and the analytic shrinking-window argument. The full ring
target density uses the analytic Duhamel and prepared-propagator argument.
