# Growing-process experiment plan, fixed before cubic results

Primary author, 2026-09-20. Supplied model and rates from PR #8545; no physical
identification, new axiom, or adoption of the separate probability-field reading.
The small-state generator and simulator are written before the following cubic
comparison. Source changes require a new identity and affected recalibration.

## Calibration already executed

Direct enumeration of all 7^4 states of the four-cycle uses complete global
weights, a sparse generator and matrix exponentials. The event-driven local
simulator instead uses local weight ratios, independent Poisson edge proposals
and a Fenwick tree for unnormalized birth hazards. At rho0=1/4, epsilon=1/10,
21 observation times tau=6 epsilon t between 0 and 4, compare density, total
orientation variance, lowest-mode structure factor and initial-bias response.

The W=1 control uses 8,192 independent trajectories; neutral raw (3,1,2) and
(12,1,2) each use 16,384. The largest discrepancy across those predeclared
observables/times is respectively 2.26, 2.12 and 1.66 estimated standard errors.
The five-standard-error sanity gate is passed. It is a statistical calibration,
not a rigorous confidence guarantee. W=1 has an exact time-dependent product
law, and the full generator also verifies the first/second moment identities.

## First cubic comparison

Periodic simple cubic graphs, sides 6, 8 and 12. Raw triples (1,1,1), (3,1,2),
(6,1,2), (12,1,2), each normalized to pair-matrix row sum six. Initial independent
occupancy rho0=1/4 and independent uniform contents. Epsilon in {1/10,1/100}.
Observe tau from 0 to 4 at 21 equally spaced values. Start with 128 independent
trajectories for each side-8 model/rate; use sides 6 and 12 for the strongest
contrast in that screen. The selection is exploratory and must be labeled so.
A second initial density rho0=1/20 tests dependence on the seed population.

Seeds are consecutive, starting at 20260920 for calibration and at 20261000
for the first cubic screen. Preserve every trajectory's summaries in NPZ files.
Do not discard trajectories or tune clocks/weights after seeing favorable data.
If a rate/event budget fails, preserve the failure and narrow the attempted
computation instead of treating it as evidence about the model.

## Observables and interpretation

Record density, total-content squared per site, the average of the three
smallest axial Fourier intensities, nearest-neighbor alignment and occupied
pairs, cumulative successful hops, birth hazard, exact total-content-variance
drift, the radius-two multiple-occupancy probability, and the absolute local
error of the dilute vector equation. Fourier intensities divided by expected
record count equal one under the W=1 control.

Compute orientation response to a small uniform initial content bias using the
exact likelihood-score identity, averaged over all three content components:
chi(t)=1+E[(M(t)-M(0)) dot M(0)]/(V rho0). The normalized gain is rho0 chi(t)/rho(t).
This is a ratio-of-expectations observable, not the expectation of M/N. Use a
trajectory bootstrap for joint ratios and contrasts, with the full raw records
preserved. Replicates are independent; different times within one trajectory
are not independent samples.

A larger structure factor on one finite torus is evidence of correlations only.
A phase, infinite-volume ordering, physical force or field identification needs
additional arguments. Filling freezes this closed finite model; frozen patterns
do not demonstrate sustained dynamics. Compare at matched density as well as
matched time when formation rates produce different density trajectories.

## Follow-up decisions

If the neutral (3,1,2) model loses normalized seed orientation but develops
local correlations, quantify their range/size dependence and the role of motion.
If stronger weights amplify alignment, distinguish local clusters from a
volume-dependent low-mode effect, and test whether mobility survives through
that interval. If the dilute residual is large, report the measured failure
of that approximation and use exact generator observables instead. A meaningful
negative or inconclusive comparison is retained; no favorable-result quota.
