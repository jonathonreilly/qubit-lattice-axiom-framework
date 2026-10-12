# Direct full-field comparison at frozen galaxy parameters

The user chat personally reconstructed, implemented and tested the axisymmetric
QUMOND field equation after the direct-author handoff. At the three galaxies
selected by source geometry before any PDE output, replacing the algebraic
radial rule changes the prediction materially. This is a conditional forward
comparison, not a new calibration, blind test or evidence of a complete theory.

The physical response, stellar mass-to-light ratio, acceleration parameter,
64-ring baryonic reconstructions and scored radii are unchanged from
`FROZEN_FORWARD_CONTRACT.md`. No parameters were refitted. The three galaxies
were already part of the exposed training set. Their choice was not based on
observed fit quality.

## Numerical result before opening the processed targets

The initial coarse/fine grids failed the 0.5% force-refinement gate for
NGC2976 and UGC07577. Refinement separated angular quadrature from the true
angular-mode tail. NGC2976 and KK98-251 pass at mode256; UGC07577 requires
mode512. All use1536 logarithmic radial base points plus the scored radii.
Final boundaries are sigma/32 and16 Rmax, with Hankel order4096. The final
boundary checks also change radial spacing and double the Hankel order.

| Galaxy | Last angular force change | Boundary/Hankel/grid change | Full/algebraic force range |
| --- | ---: | ---: | ---: |
| NGC2976 | 0.00313947 | 0.0000293965 | 0.778133–0.989752 |
| UGC07577 | 0.00411260 | 0.000111213 | 0.660164–0.931689 |
| KK98-251 | 0.00165098 | 0.0000343291 | 0.628664–1.033466 |

Changes use the previous force as denominator, as in the archived gate
receipt. The initial run console used the final force as denominator; those
slightly different diagnostics have the same passing disposition.

All Newtonian midplane reconstruction checks are below1.1e-12 relative.
The real-source nu=1 projection checks are below0.000471. Analytic Gaussian,
vertical-convolution, spherical, Kuzmin, gradient and non-gradient controls
pass. The independently derived non-gradient controls detect zeroing,
reversing and rescaling the nonlocal projection. The final source and
derivation have a focused independent source check. The complete subsequent
gate/score check in `independent_direct_review/FOLLOWUP_REVIEW.md` reproduces
the masks, provenance and every reported score independently. The parent
read that complete report and its hashed receipt before the next reuse.

The frozen1% working force budget is based on these finite comparisons, not
an interval proof or propagated mass-model uncertainty. A trial subtraction
of a curl-free sheet trace did not cure the mode tail and was removed; its
source and output remain preserved. Other source changes repaired diagnostic
zero handling and added controls, leaving the positive-field projection
formula unchanged. Original failed outputs are not overwritten.

## Observed velocity comparison

Only after `DIRECT_NUMERICAL_GATES.json` passed were the processed velocities
read by `direct_fixed_comparison.py`. Predicted speeds are sqrt(R*g), in
km/s with R in kpc and g in (km/s)^2/kpc. The following score is the root
mean square of log10(V_prediction/V_observed) within each galaxy.

| Galaxy | Newtonian baryons | Algebraic rule | Local full-norm rule | Full PDE |
| --- | ---: | ---: | ---: | ---: |
| NGC2976 | 0.100885 | 0.032960 | 0.030056 | 0.015566 |
| UGC07577 | 0.070164 | 0.312670 | 0.270207 | 0.267934 |
| KK98-251 | 0.197822 | 0.137631 | 0.093838 | 0.099969 |
| Equal galaxy weight | 0.134455 | 0.198151 | 0.166053 | 0.165353 |

The full equation improves the frozen algebraic score in all three selected
objects, but the outcome is mixed: the Newtonian baseline has the smaller
aggregate score for this particular subset, largely because UGC07577 needs
far less enhancement than the supplied nonlinear response predicts. NGC2976
is described substantially better by the full field than by either of those
baselines; KK98-251 still has excess predicted velocity. This subset cannot
replace the previous full-sample score or determine a universal model rank.

The gas-sheet normal field explains much of the change for the gas-rich
objects; the nonlocal Poisson correction is additionally important in
NGC2976. Both effects were derived and computed, not fitted to these rows.
The released velocity-error bars include fitted and kinematic-asymmetry
terms; geometry and source uncertainties remain unpropagated. No chi-square
significance, ephemeris likelihood or joint
probability is assigned.

The subsequent primary-source check in `DIRECT_KINEMATIC_READOUT_FINDING.md`
identifies an additional limitation: UGC07577's original reduction left gas
pressure support uncorrected and named it as a significant exception. The
current table's use as circular speed is therefore a load-bearing premise.
No correction has been fitted or applied to these fixed results.

This resolves a concrete forward-model gap at three fixed sources. It does
not supply a full-PDE galaxy-calibrated a0 and therefore does not validate
the earlier transfer of an algebraic fit into the solar quadrupole problem.
The required six-object source-ranked extension is running. The next theory
step is to reconstruct a shared response function under both galaxy and
solar constraints, with its family and empirical roles frozen before fitting.

## Reproduction and exact receipts

Final solver SHA256:
`701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00`.
Physical contract SHA256:
`f6225b00b62a82b050586535a933f82d8320783d7934d35ef0ce9e8f31d49b93`.

Runtime `galaxy_response/qumond_disk/` preserves `DIRECT_NUMERICAL_GATES.json`,
`DIRECT_FIXED_COMPARISON.json`, the PNG/PDF comparison, all field coefficient
arrays and solver-version receipts. The gate receipt hashes every field
output; the comparison receipt hashes its numerical gate and target archive.
`independent_direct_review/` records the independent checks and their limits.
The implementation scripts refuse to overwrite scientific execution receipts.
