# Finite-volume confirmation and population dependence

Declared 2026-09-21 before follow-up execution. Selection follows the side-eight
exploratory screen: compare raw (3,1,2) and (12,1,2), each normalized to row sum
six. The simulator source remains the calibrated version. Run every combination
of side length 6, 12, 16; epsilon 0.1 and 0.01; initial independent density 0.25
and 0.05. Use 512 trajectories per case, seeds 20272000 through 20272511. These
seeds do not overlap the cubic screen. They overlap part of a different-geometry
calibration only; no uncertainty calculation treats those datasets as independent
evidence. All follow-up cases are preserved, without favorable-result stopping.
Maximum two local simulation processes at a time; hard campaign deadline applies.

Use the existing 21 observations at tau=6 epsilon t from zero to four. Primary
comparisons are at tau=2 and at ensemble mean density 0.9, with 0.75 and 0.95
as secondary density windows. Matched density here means a deterministic time
chosen by the **ensemble density curve**, not a trajectory's random birth-count
stopping time. Linearly interpolate the two surrounding ensemble means. For
uncertainty, resample whole independent trajectories and repeat both density
inversion and observable interpolation for each resample. If the target is not
bracketed by a resample or full sample, mark it unavailable; do not extrapolate.
The time-grid interpolation error is separate from bootstrap uncertainty and
must be checked if it affects a scientific conclusion.

Report pointwise 95% percentile intervals from 4,000 resamples with a recorded
fixed seed. Cases sharing initial RNG seeds are correlated; a direct difference
must resample the same trajectory indices in both cases, or explicitly avoid a
cross-case significance claim. No multiple-comparison-adjusted claim or phase
inference is planned. Finite-volume trends and effect sizes matter more than
whether a particular interval crosses one.

The population-normalized bias response is a property of the specified initial
perturbation, not a universal susceptibility or a physical force. In particular,
its dependence on the initially supplied population needs to be exposed. A
subsequent separate experiment will start from a completely vacant graph and
measure correlation spectra and motion without this undefined normalization.
That is the direct formation-from-empty model. Its new measurement code must
receive focused checks before its results are interpreted.
