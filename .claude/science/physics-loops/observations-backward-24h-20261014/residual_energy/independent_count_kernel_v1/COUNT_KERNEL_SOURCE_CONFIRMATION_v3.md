# Affected count/clock/vector source confirmation

Reviewer: `/root/force_energy_bridge_check`. This supplements the prior
independent 109-control kernel report and its derivation-v2 check.

Reviewed source identities:

- `DERIVATION_v3.md`: `1eca5b9a13278c819e221955518150cbcc44e4a9d012fbcba85db8df08dc707f`.
- `residual_energy_check_v1.py`: `8ce220112159929fc05bbfa2e532f2263cf3a94293742dc2319836fb3738127d`.
- Existing `AUTHOR_RESULTS_v1.json`: `cb2f36aaab8cb6d81cb8431e594cc469281f9ec7f77b461b04cd2eba4d6b654f`.

The independent kernel derivation/109 controls were finished before any new
author code was opened. The requested independent timing reconstruction was
also completed before opening this implementation. I then read the full
script for context and checked its count, clock and vector-kernel blocks against
the independent derivation. I did not execute its top-level author suite or
rewrite its result. Its 149 recorded controls are author results bound to
DERIVATION_v2.md, SHA `1e31731ea505da305b4a6250a63aa0b2b6c85909eb4f89b56e244ee37e9e02e1`;
this confirmation does not pretend they were originally executed against v3.

## Count and unequal-window blocks

The midpoint-separation H, gap plateau, rising/falling weights and velocity
average difference use the correct durations. Direct acceleration quadrature
has the matching normalization. The unequal-window D matrix uses integrated
velocity counts with entries -1/(H_i T_i), +1/(H_i T_{i+1}). Its Gram equals
the explicitly assembled diagonal/off-diagonal form and the duration-weighted
mean-removal energy. The equal-window inverse uses n contrast rows and the
correct negative neighboring cross terms. These are synthetic observation
models; the code reads no ODF values.

## Clock block

The synthetic map is tau(s)=s+0.03s² with positive derivative on both test
intervals. Its inverse is (sqrt(1+0.12tau)-1)/0.06. The direct tau integral
and physical-coordinate integral include the calibration k(tau(s)), the
Jacobian d tau/ds, and the clock-duration normalization. No factor is
silently replaced by a physical-time duration or pulled out of the integral.
This correctly checks the supplied velocity-with-respect-to-s model. It does
not derive the radio response or resolve a different dx/dtau measurement
without the additional factor explained in the independent report.

## Vector kernel block

The synthetic unit direction n_i and constant per-window calibration kappa_i
give N_i=kappa_i n_i, B_ii=kappa_i²/(6pi T_i), and nuisance design [N,1].
The nullspace rows cancel the complete vector moment and the independent
constant additive baseline. The zero third-direction column is redundant,
not an extra data channel. The implemented F_i=c_i N_i/T_i and cumulative
primitive W=-prefix-F_i(s-left_i) have the correct sign and terminal zero.
Its direct integral against acceleration agrees with the projected means.
The scalar sum-zero counterexample correctly shows why scalar cancellation
alone is insufficient when direction changes.

The nuisance quotient has the correct B inverse weights and coefficient one
half. Together with B_ii=1/(6pi T_i), this yields the independent 3pi result.
This auxiliary B does not assert bounded individual raw velocity operators;
the cancellation is essential for the compact H1 acceleration kernels.

## Version3 clarification check

I read the complete v2-to-v3 diff. It resolves both earlier source clarifications:
T_{i+1} is explicit, B is positive definite where the full inverse-square-root
whitening is used, and the scalar denominator requires q>0 and c^T B c>0.
The added L2 premises make the auxiliary matrix entries finite. Positive Q_J
and G_meas are explicit, q=0 has its separate zero-response compatibility
condition, and a zero-Gram contrast is treated by compatibility rather than
an invalid division. Those changes preserve the checked positive-definite
formulas and clarify domains; no new equation in the count/clock/vector blocks
needs an unchanged-suite rerun.

No new mathematical discrepancy is identified in this affected scope. The
independent report's restrictions remain: exact diagonal equality belongs to
a fixed-point massless gradient model; massive modes have only the enclosure;
actual moving spacecraft/full conformal force, calibrated clock/count response,
physical energy and observational uncertainty still require their own bridge.
No actual Cassini force residual has been produced by these source checks.

This is scoped source correspondence, not a full certification of every other
Fourier, optimizer, singular-range or mutation block in the author script,
and not a publication or formal audit verdict. Those scopes remain with root
and its designated reviewers.
