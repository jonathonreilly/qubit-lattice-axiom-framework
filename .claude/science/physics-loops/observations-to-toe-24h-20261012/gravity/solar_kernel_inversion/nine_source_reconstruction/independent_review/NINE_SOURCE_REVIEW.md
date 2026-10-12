# Independent check of the nine-source reconstruction

2026-10-12. Focused source, arithmetic, numerical-receipt and proof check;
not a formal audit or an empirical/theory acceptance. Parent authored the
protocol, implementation, certificates, sensitivity calculation and interpretation.
I did not fit weights, run field projections, change author files, launch agents,
or alter the campaign. All review outputs are in this directory.

## Result and corrections

No material score, numerical-gate, LP-row, exact-certificate or pressure-sensitivity
arithmetic discrepancy was found. All 162 source/candidate/grid score rows agree
with independent recomputation. All 54 source/candidate gate decisions agree:
51 pass and three fail, leaving four of six complete candidates numerically
qualified. The four qualified candidates still fail the stipulated descriptive
rectangles. The two unqualified candidates' scores remain diagnostics.

The exact rational certificates prove the stated positive lower bounds for the
six frozen finite matrices. They do not certify continuum projection accuracy or
the rotation-to-circular-speed identification. All 90 scored observations are
exposed fitting data. No independent empirical test is created by this block.

Three points were sent to the parent and are correctly disposed in the final note:

1. The original helper stored first-stage status and asserted second-stage
   success, but omitted the second status/message despite the protocol. The
   separately labelled replay supplies new execution evidence and does not
   pretend to recover the missing original log. No weight selection changed.
2. The joint solar primals exceed the scaled upper bound by approximately
   2.03e-9 (M) and 3.02e-10 (D). These remain numerical calibration outputs
   within the declared tolerance, not exact feasible solar witnesses.
3. The perturbation corollary needs the nonnegativity domain and weight cap
   to remain fixed. The final note explicitly retains both independently of
   perturbations to the displayed cap row. That correction is sufficient.

Final `DIRECT_NINE_SOURCE_OUTCOME.md` SHA-256:
`29d77d492d756c3f5b6d0eda84f5353b400389dda1ec074cd1edbc2d7b710cdc`.
I read its complete argument and confirmed the corrected paragraph. The first
filesystem snapshot already contained the correction; the pre-correction wording
was read in tool output. The two saved full-note copies therefore have identical
final hashes, and the empty snapshot-comparison diff is not a claimed historical
before/after diff.

## Source disposition and exact identities

Read in full: `PROTOCOL.md`, `direct_nine_source.py`, inherited
`direct_galaxy_response_operator.py`, `direct_shared_response_fit.py`,
`direct_validate_inverse_fields.py`, `direct_response_basis.py`, and
`FROZEN_DIRECT_INVERSE_PROTOCOL.md`; then `FINITE_LP_CERTIFICATE_PROTOCOL.md`,
`direct_finite_lp_certificate.py`, `verify_finite_lp_certificate.py`,
`direct_solver_status_replay.py`, `direct_pressure_sensitivity.py`, and the
complete outcome note. The unchanged underlying field solver retains the earlier
independent source coverage at SHA `701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00`;
this review did not repeat a field solve or reopen that unchanged mathematics.

| Input | SHA-256 |
|---|---|
| Nine-source protocol | `d8a0bf8f0880e8c180bdf2f59e7df5c9d99b61e9a92ad6135209dab7a937ffe9` |
| Nine-source driver | `6a2ff77b86580f3e4ed9a934a66c5c5e3789a559e60d0c46296aa97482932e6b` |
| Freeze | `00531ffbeeb01f2d7ef5fd4c535dba72bef7904265a061922a64a61d2d2d3ce0` |
| Candidates | `6a51ac43d38def7f745f6e34367ab9474311ff9fb28103bacdbe0e72d01c3263` |
| Results | `a19385766f5fbc11dd403410b6b3008e0fa0b88987943e70373dd34931ee68a4` |
| Baryonic NPZ | `217bd10ba3fa8f9972d047081342c023ee7524c16b6d8c685d6d9fa49fd2959f` |
| Target NPZ | `1e8f96f1198817fe962ecf43ceed6fb23be795f3c12ae246387a65cdc2dddfa6` |
| Certificate protocol | `bdfcaffd703c9e06fda8a42f375f22cca99df1f06637f9c2fb5f63b4185be1a2` |
| Certificate producer | `bfe4f95b993350935d6ca724835ead15a05d3a4465cb158993db5226e9108a43` |
| Status replay | `5e0411d3267e388f752aee0814b8bd535ad0099eba3596a755c3b630aba64992` |
| Pressure checker | `7dc6f7b00e5426a4033eda1f1cd212b3b4ae61802211dce89a96265ca70cc089` |

The manifests give every other exact identity, including all nine operators,
source receipts, 27 geometry caches and their metadata, the original failed
transfer, inherited components, controls, all field receipts, and six exact
matrices/certificates. Source and target NPZs and ordinary input/source receipts
were copied byte-for-byte. Large geometry caches were stream-hashed in place;
they were not copied or recalculated. Every frozen expected hash matches.

The freeze precedes new columns and candidates; all candidate fields follow
the candidate receipt. All six extra operators retain `observed_velocities_read=false`;
inspection confirms that column construction reads source arrays, not observed
velocity/error arrays. Fitting then opens every declared target. The original
three column receipts are reused unchanged. E is exactly
1.4915242022774435e-10 m/s² where imposed, and absent in galaxy-only cases.
The global stellar factor is exactly 0.5605122519882025 throughout.

| Source | Raw/scored bins | Excluded zero-based raw indices |
|---|---:|---|
| NGC2976 | 27/21 | 0,1,2,3,4,5 |
| UGC07577 | 9/7 | 0,1 |
| KK98-251 | 15/12 | 0,1,2 |
| NGC3949 | 7/6 | 0 |
| NGC3972 | 10/9 | 0 |
| UGC06667 | 9/7 | 0,1 |
| UGC08837 | 8/7 | 0 |
| DDO064 | 14/12 | 0,1 |
| DDO168 | 10/9 | 0 |

These are the frozen masks, not residual-driven exclusions. All 109 raw bins
remain in the copied inputs; all 90 masked bins are used in every case.

## Independent scores and numerical decisions

The independent code imports no author module. For each recorded force it treats
the parsed binary64 values as exact fractions, calculates
`q=R*g/Vobs²`, and classifies the rectangle by squared-speed inequalities.
It computes square roots and logarithms at 70 decimal digits. Thus
`log10(Vpred/Vobs)=log10(q)/2`, with Vpred in km/s since g is in
(km/s)²/kpc. The additional allowance is

`max(0, [R*g-(V+2e)²]/V², [max(0,V-2e)²-R*g]/V²)`.

Equal-galaxy RMS is `sqrt((1/9) sum_g (1/n_g) sum_i log_i²)`.
It is neither the mean of galaxy RMS values nor a pooled-bin RMS.
Largest absolute discrepancies are 2.84e-14 km/s in velocity, 2.78e-17
in per-source RMS, 4.44e-16 in t, 1.11e-16 in force-change gates,
and 1.39e-17 in aggregate RMS. Every bin count agrees.

| Case | Whole-candidate numerical gates | Refined equal-galaxy RMS | Refined largest t | Outside bins / 90 | Galaxies outside |
|---|---|---:|---:|---:|---:|
| M galaxies | fail | .13306845604574224 | .5556886185586407 | 55 | 8 |
| M external | fail | .1243961805516149 | .5556886185586407 | 37 | 7 |
| M external+solar | pass | .12652053669332688 | .5556886185586412 | 41 | 8 |
| D galaxies | pass | .1233296611101493 | .5570476147595022 | 39 | 7 |
| D external | pass | .12475312682379691 | .5570476147595024 | 40 | 7 |
| D external+solar | pass | .12281277120465021 | .5570476147595024 | 38 | 7 |

All stored forces are positive and finite. The failed refinement ratios are
.01046757146365656 for M galaxies/NGC2976,
.005802543759447101 for M galaxies/NGC3972, and
.005785125105676412 for M external/NGC2976, against .005.
No boundary ratio fails .003; the largest is 1.838010425839312e-5.
The largest refinement ratio among passing individual gates is .003244986225420282.

All 27 geometry hashes match their metadata. Refined nr, nc and lmax double;
radial endpoints and Hankel order remain fixed. Each boundary cache doubles
the outer radius and halves the inner radius, preserves every original radial
node and both original field components bit-for-bit, retains the angular grid,
and uses the declared 8192 edge Hankel order. This verifies receipt/cache
consistency, not the continuum error of an unrun field calculation.

The directly projected base force differs slightly from `g_N+K*w`; the largest
relative difference is .000116786584170392. Independently calculated absolute
offsets agree across all six weight vectors to 5.29e-12 in native force units,
as expected for the weight-independent Newtonian projection discrepancy.
It is retained in actual field scores. The final t is not overwritten with
the LP optimum, and the grid optimum is not represented as exact final-field
feasibility.

For the passing M joint candidate the largest t is at UGC06667, R=3.50 kpc:
Vpred=36.581429 km/s versus 69.3±3.0, with descriptive rectangle [63.3,75.3].
For all D candidates the largest t is UGC06667, R=2.61 kpc:
Vpred=24.714213 versus 57.0±3.9, rectangle [49.2,64.8].
The maximum absolute velocity residual is a different diagnostic: for D
external it is +47.743058 km/s at NGC3949, R=3.50; for D galaxies and
D joint it is −36.110165 km/s at UGC06667, R=4.37.
Every bin, direction, radius and worst-bin definition is preserved in
`independent_scores_and_gates_v1.json`.

## LP semantics, positivity and exact lower bounds

Independent reconstruction recovers all 180 galaxy rows in each matrix exactly,
including the rounded binary64 normalizers. Upper rows are `(K/A,-1)` with
bound `H/A-g_N/A`; lower rows are `(-K/A,-1)` with bound `g_N/A-L/A`.
The cap, all twenty D rows, external rows, signs, ordering and row labels also
match exactly. D rows are `w_j/log(A_(j+1)/A_j)-sum_(k>j)w_k<=1`.
This is the upper one-sided infimum on each decreasing log ramp; it does
not provide a strictly positive margin.

The solar row was checked independently by 70-digit integration in log(s),
split at s=1. All coefficients agree within 7.28e-16 relative. E-dependent
normalization `E^(3/2)/sqrt(GM)` and `E*N(E)` agree, with correct s^-2 and
m/s² units respectively. This checks computation of the inherited kernel,
not an independent solar field validation or measurement calibration.
All nonzero certificate support lies in exactly reconstructed non-solar rows.

Primary t minimizes the common acceleration allowance. The secondary LP
minimizes total weight with t at most primary+1e-8. The stored second-stage
primals satisfy the published numerical tolerance; exact rational residuals
reproduce their reported magnitudes to rounding. Total weight and positive
matrix forces agree. The code does not silently use equal-galaxy RMS as the
LP objective; that metric is a subsequent readout.

For the literal saved D weights and binary64 knots, high-precision evaluation
of the derivative infima gives approximately −2.09e-15, −1.53e-15 and
−8.23e-16 for the three D cases. These are tolerance-level boundary contacts,
not exact strictly positive D. The M infima are about −109.3662. Neither set
inherits the earlier strict-positivity constrained-energy theorem. No weight
repair was made or requested.

Let z=A^T y, with y<=0 and z_t<=1. For a feasible x=(w,t)>=0,

`y.b <= y.A.x = z_w.w + z_t*t <= delta*sum(w)+t <= 100*delta+t`,

where `delta=max(0,max_j z_w,j)`. Therefore
`t>=y.b-100*delta`. The argument does not assume exact dual weight-column
feasibility. Clipping positive y proposals and reducing their common scale
as prescribed establishes the sign and t conditions exactly.

I recomputed every rational multiplier, rescaling factor, column sum,
deficit, lower bound, support label and downward decimal from the preserved
files. All six are valid. The weight-residual penalties range from
1.22e-17 to 5.05e-15. The reported safe bounds are

`M: t>=0.555684948124`, `D: t>=0.557044667733`.

The certificates use the stated UGC07577 upper bounds and UGC06667 lower
bounds; D additionally uses UGC08837's upper bound and seven D inequalities.
No nonzero multiplier uses an external or solar row. Adding those constraints
cannot remove the galaxy-only finite-matrix lower bound. Changing a galaxy
operator, source, mask, normalizer, readout, basis or cap is another problem.
Exact rational matrix bounds do not turn approximate primal weights into an
exact feasible witness or make finite projections continuum-certified.

For the final perturbation corollary, with the same nonnegative domain and
cap, unchanged t column, |Delta A_ij|<=epsilon and |Delta b_i|<=eta,
the new dot product loses at most `eta*||y||_1` and the weight deficit rises
by at most `epsilon*||y||_1`. The loss is thus at most
`(100*epsilon+eta)*||y||_1`. Without the unchanged cap it need not hold.
An exact rational toy counterexample is preserved: the original constraints
`-w-t<=-300, w<=100`, y=(-1,-1), give L=200. Perturbing both weight
coefficients by .1 while also relaxing the cap admits (w,t)=(1000/9,1600/9),
violating a claimed bound of 180. Retaining cap100 instead gives t>=190,
consistent with the corollary. The final note now excludes this failure.

## Pressure sensitivity and physical scope

If p shifts both squared-speed endpoints while the original R, A and matrix
remain fixed, upper b shifts by +p/(R*A), lower b by −p/(R*A).
The same y and delta therefore give exactly

`t>=L+sum_i (y_upper,i-y_lower,i)*p_i/(R_i*A_i)`.

The independent checker reconstructs every coefficient from the processed
arrays and exact rational y, using the frozen binary64 A rather than silently
replacing R*A by exact V². It checks an arbitrary signed rational perturbation
directly in b and obtains the same affine bound. The coefficient units are
(km/s)^-2; the t shift is dimensionless.

If only UGC07577 changes, the negative coefficients require a necessary
maximum p of 794.2477322233368 (km/s)² for M and
p(.94)>=1113.2873278904708 (km/s)² for D. The exact rational thresholds,
not only their rounded decimals, agree. Setting every relevant UGC07577 p
to the threshold makes this certificate zero; it does not exhibit a feasible
response. Positive support at the active UGC06667 lower-bound bin increases
the obstruction, as the coefficient sign says.

The illustrative D slope is 17.395114498288606 at sigma=8 km/s, and the
illustrative speed is 35.039653649693385 km/s from the central tabulated
10.7 km/s. These are correct conditional arithmetic, not measurements.
For steady isotropic gas with constant sigma and height, radial force balance
gives p=−sigma² d ln Sigma/d ln R. That model does not make the fitted ring
density a verified pressure tracer.

The narrow primary-source claims were checked directly in
[Swaters et al., sections 3.1.2 and 3.5](https://arxiv.org/html/0901.4222v1).
The 8 km/s dispersion belongs to reduction modelling; asymmetric-drift
corrections were left unapplied; UGC7577 is specifically an exception to
the generally small corrections. These sections do not supply an actual
correction at the frozen .94 kpc bin. No new HI-profile values or another
object's dispersion were imported into this review.

The outcome note correctly leaves pressure support, source uncertainty,
galaxy external fields, other response families and matter models open.
The descriptive rectangles are not a joint confidence region, t is not a
velocity percentage or significance, and equal-galaxy RMS is not a likelihood.
No TOE, retained verdict, dynamics completion or broad gravity exclusion follows.

## Reproduction and limits

Run `check_nine_source_independent.py` and `check_pressure_independent.py`
from this directory against the preserved snapshots. They refuse to overwrite
their result JSONs; preserve or move existing reviewer outputs before a rerun.
The main computation took 2.26 seconds, one numerical-library thread, with
peak RSS 243,531,776 bytes. No LP optimizer or author score/projection helper
was imported. The replay was source/receipt checked, not re-executed.

`independent_check_receipt_v1.json`, `independent_scores_and_gates_v1.json`,
`independent_lp_and_certificates_v1.json`,
`independent_pressure_and_replay_checks_v1.json`, the two snapshot manifests,
and the final review receipt preserve the detailed evidence and identities.
Current deadline/stop guards were respected. No exact bound on the continuum
column error, missing physical readout, or optimizer's historical second-stage
log is supplied by these independent checks.
