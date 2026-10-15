# Focused independent check: temporal scalar-force averages

Checker: /root/localized_history_check. This is a focused mathematical
check of the supplied flat free Klein-Gordon operator and fixed-point
observable, not a formal audit or a physical readout calibration.

The exact dual norm, real-data compatibility, massless/H1 treatment,
full-vector bound, triangular scaling and adjacent-average identity agree
with my independent derivation. One small notation clarification is
recommended for the count-error bound: dN_plus and dN_minus must denote
nonnegative absolute error budgets; if they denote signed errors, write
|delta N_plus|+|delta N_minus|. The author code already uses absolute values.
This point was reported to the author; it changes no executable formula.

## Order and independence

I read TEMPORAL_FORCE_HISTORY_WORKING_v1.md and saved TEMPORAL_PRECHECK_v1.md
before opening the author checker or results. I then read the complete
author script and all saved 70-control results. Those author controls were
not rerun or included in the independent count below. Independent exact
oracles were derived and saved in TEMPORAL_CONTROL_ORACLES_v1.md before
executing the new checker, which imports no author code.

## Exact norm and domains

With alpha=(2*pi)^(-3/2), the functional is
alpha*integral i*(e.k)*exp(i*k.x0)*(C*qhat+S*phat/omega) d^3k.
A real-compatible Riesz representative is
qhat_R=-i*alpha*(e.k)*exp(-i*k.x0)*C/omega^2 and
phat_R=-i*alpha*(e.k)*exp(-i*k.x0)*S/omega.
Both obey the required conjugate symmetry under k -> -k. The joint energy
norm of (omega*qhat,phat) gives exactly the claimed squared operator norm,
with angular coefficient 1/(6*pi^2). Smooth symmetric spectral cutoffs
approximate the representative, establishing sharpness on the energy
completion and approach by real Schwartz data.

For mu=0 the energy space is the homogeneous H1 completion times L2;
the Fourier origin is handled by cutoff approximation. A constant zero
mode, if one uses a quotient convention, cannot affect the gradient
observable. H1 of the real time weight gives finite derivative energy,
and L1 supplies the stated ordinary Fourier transform. Real-weight
Parseval contributes pi, rather than 2*pi, on the positive-frequency
half line. Thus C_mu^2 <= ||w'||_2^2/(6*pi), with equality at mu=0.

The three Cartesian Riesz representatives have Gram matrix C_mu^2 I.
Consequently the full vector observable has the same operator norm C_mu,
without an extra sqrt(3). This is compatible with the single-budget
unit-vector projection proof in the note. Shifting the time window
rotates C,S and preserves the norm. The rough-data extension defines a
bounded linear observable; it does not posit a classical pointwise
trace for arbitrary finite-energy solutions.

The triangular weight is the convolution of two normalized half-width
boxes, so its Fourier transform and derivative norm give exactly the
stated T^(-3/2) energy bound. The rectangular force-window norm with a
massless spectral cutoff is the stated elementary integral of sin^2.
Its divergence is a fact about this continuum functional. Finite-band
measurement devices are not excluded.

## Targeted independent controls

The new checker completed 58 controls successfully in about 0.117 seconds.
They include a symbolic partial-fraction identity and the following
checks distinct from the author's symmetric triangular/Gaussian fixtures.

For the asymmetric real weight w(s)=a^2*s*exp(-a*s) on s>=0, both C and S
are nonzero. Direct integration gives W=a^2/(a-i*omega)^2 and
||w'||_2^2=a^3/4. Partial fractions give the exact squared norm
[2*mu^3+(a^2-2*mu^2)*sqrt(a^2+mu^2)]/(24*pi).
Using this independent oracle, three-dimensional Fourier quadrature
verified real-data symmetry, the complete energy and observable Gram
matrices, vector norm attainment and invariance under a time shift for
mu=0,0.6,1.7. The largest Gram-matrix discrepancy was below 2.77e-16.
Radial integration separately agreed with the exact oracle. Smooth real
Schwartz approximants approached the massless norm: the finest fixture
achieved 0.08226004 against the exact 0.08240516.

I also constructed explicit real Schwartz data for a rectangular window,
using a smooth radial high-pass factor times a Gaussian cutoff in the
Riesz representative. Closed Gaussian integrals give its energy and
observable independently. At E=1/2 and T=1, increasing the cutoff scale
from 16 to 64 to 256 gives averages 0.41151332, 0.82297771 and 1.64593094.
The triangular-window bound at that same energy and T is 0.32573501.
Every member has smooth rapidly decreasing spectral data and finite
energy. The explicit formulas show growth proportional to sqrt(Lambda)
for this family. This supplies an actual smooth witness, rather than
relying solely on a discontinuous hard spectral truncation. It does not
alter the note's limited conclusion about rectangular force averages.

Two piecewise-linear, absolutely continuous velocity profiles with an
interior kink verify the adjacent-average identity outside the smooth
polynomial class. Conditional count errors with opposite signs saturate
the absolute error budget up to floating-point error. A deliberately
drifting bias gives the expected uncancelled term, confirming why the
note's constant-b premise is material.

All numerical quadratures are ordinary floating-point controls, not
interval certificates. Exact inequalities and the norm statement rest
on the separately saved derivation. No held-out or raw observational
data were accessed.

## Interpretation and remaining limits

The gain applies to a different observable: a time-smoothed gradient at
one fixed spatial point and direction under a frozen stable flat operator.
It does not bound an instantaneous force merely because the field is old.
It requires a quantitative energy budget in the displayed normalization.
That budget and its physical kinetic/coupling conversion remain supplied.

The adjacent velocity-average identity is exact for absolutely continuous
v. A count-error bound follows only after supplying the displayed fixed
kappa, fixed f0, constant bias and common time coordinate. These identities
do not establish that actual ODF products measure such v or that a real
spacecraft acceleration equals a fixed-point gradient. Moving worldlines,
changing lines of sight, metric and material response, clock/ramp/media
identification, and physical energy calibration remain open. No actual
ODF-to-force bridge or moving-worldline energy norm was established by
this check. Neither compact localization nor an initial state was inferred
from measurements.

## Exact reviewed identities

Hashes are SHA-256. The report itself is bound by
TEMPORAL_REVIEW_IDENTITY_v1.json, avoiding a self-referential digest.

| File | SHA-256 |
| --- | --- |
| TEMPORAL_FORCE_HISTORY_WORKING_v1.md | 57632b37c2c54f7cf12c48ac54429ffc119bbd3362fce39ffaa8d4a556a36625 |
| temporal_force_history_check_v1.py | 8bb6a06ebb73c04b865fcd47ca7ed63b4e6392419b0090706448296f0474eac9 |
| TEMPORAL_FORCE_RESULTS_v1.json | 6f61d6f2d5e1f7c292e8637aecdd2065cd1fec841c6a86c41ee95f5cfa484755 |
| TEMPORAL_PRECHECK_v1.md | 84024de208522dc17dbbe5fc88e88a9713cdc1135d7cfe3c2e6982b0f4fa8953 |
| TEMPORAL_CONTROL_ORACLES_v1.md | 65b3ad93621838ecea0c6300f746ab2677b6a2624b242f5691b15a0290ac8f0f |
| independent_temporal_check_v1.py | 31c4fa5f862b1be33cc22f8ed302410a3199fe59fbcae5fee5a3c718809ee21a |
| INDEPENDENT_TEMPORAL_RESULTS_v1.json | dc99933002abdf9a9717a70f8d03371b4ec07c3a6979eaec9757d8d4394e12e1 |
