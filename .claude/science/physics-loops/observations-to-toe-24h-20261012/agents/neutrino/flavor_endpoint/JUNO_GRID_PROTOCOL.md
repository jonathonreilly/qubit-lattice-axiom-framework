# Released JUNO grid: diagnostic processing, frozen before processing

V1 analytical predictions were frozen separately at 18:00:01Z. The Nature
source-data ZIP has now been obtained from the publisher; its Fig.4 header and
domain were inspected, not its best fit or profile/covariance outputs. The
grid is explicitly normal ordering and covers theta12 variable sin²theta12
in [0.26,0.36] and delta21 in [6.9,8.1] in units of 10^-5 eV². It has 10000
rows. Root numerical results still have not been read.

Use this grid only to reproduce the published standard-model profile summary
and estimate a local parameter correlation as a diagnostic. It is not the
raw-data likelihood; detector/flux nuisances and the Daya Bay constraints have
already been processed. It cannot be evaluated at the V1 theta12 prediction
outside its domain, and it cannot impose the candidate's other parameters
jointly. Do not extrapolate or manufacture a delta-chi-square for V1.

Processing fixed now: reshape after verifying the rectangular coordinates;
minimize over the other coordinate at each sampled point; subtract the sampled
global minimum; report linearly interpolated crossings of delta-chi-square
1, 3.841458820694124 and 9, checking that crossings are interior and that
sublevel sets are connected. Local quadratic fits around the sampled minimum
use symmetric index windows of half-width 3,5,8, with constant, linear and all
quadratic terms. Invert the quadratic coefficient matrix (not its doubled
Hessian) to obtain local Gaussian covariance estimates. Report the variation
with window as a numerical/nonquadratic diagnostic, and never label those
estimates an experiment-published covariance matrix.

For the gap-ratio comparison, report both r21/31 and r21/32. The basic rectangle
uses JUNO delta21=7.50±0.12 times 10^-5 eV² and the separate NO accelerator
delta32 interval 2.43(+.04,-.03) times10^-3 eV² from the joint 2025 analysis.
Take endpoint extrema only; this is not a joint CI, and solar/reactor priors
overlap. Newer individual accelerator summaries are checks, not independent
measurements to combine with their older joint-analysis constituents.
