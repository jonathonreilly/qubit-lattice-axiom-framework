# Fixed-response expansion to six preselected sources

Direct author result, 2026-10-12. The source-only selection at 19:01:36 UTC
specified these six objects before any of their full QUMOND fields. All six
passed the frozen finite numerical checks. No object or parameter was replaced
because of its observational residual. These are exposed development data;
NGC3972 belonged to the earlier algebraic test split, and the other five to its
training split. All six are outside the later three-object response inversion.

The fixed stellar mass-to-light ratio is 0.5605122519882025 and the supplied
response retains a0=7.658058668049826e-11 m/s^2. These were previously fitted
with an algebraic readout, not recalibrated using this full field equation.

| Galaxy | Newtonian RMS log10 V | Algebraic RMS log10 V | Full-field RMS log10 V |
| --- | ---: | ---: | ---: |
| NGC3949 | 0.0735813 | 0.0256613 | 0.0234552 |
| NGC3972 | 0.2055120 | 0.0471223 | 0.0659444 |
| UGC06667 | 0.5052358 | 0.1574123 | 0.2050560 |
| UGC08837 | 0.1635801 | 0.1540912 | 0.1093332 |
| DDO064 | 0.2952577 | 0.0371138 | 0.0581758 |
| DDO168 | 0.2562566 | 0.0727235 | 0.0547423 |
| Equal galaxy aggregate, six | 0.2835829 | 0.0983767 | 0.1043085 |
| Equal galaxy aggregate, all nine | 0.2442107 | 0.1397852 | 0.1279351 |

The full projection improves three extension objects and worsens three relative
to the earlier algebraic formula. Across all nine preselected sources the full
projection improves the aggregate relative to the tested Newtonian and
algebraic readouts. The six-object aggregate is slightly worse than algebraic.
This is useful evidence that disk geometry matters; it does not rank universal
gravity theories or repair the outstanding full-field calibration.

The last angular-mode changes are respectively 0.00138335, 0.00270597,
0.00290651, 0.00325189, 0.00350031 and 0.00219941. UGC06667 and UGC08837 needed
mode512; the other four passed at256. The largest boundary/Hankel/grid change
is 0.00004302. The Newtonian projection control is below0.00007916 for every
extension object. These are finite refinement checks under the working force
budget, not certified error intervals. All failed coarser refinements remain
preserved in the runtime receipts.

RMS means an unweighted mean squared logarithmic velocity residual within each
galaxy, followed by equal galaxy weighting for the aggregate. No likelihood,
confidence level, nuisance propagation or fit-derived significance is assigned.
The isolated boundary, baryonic profiles, stellar height, inclination, distance
and circular-speed observation map remain premises. In particular, retain the
primary-source pressure-support finding in DIRECT_KINEMATIC_READOUT_FINDING.md
when interpreting the original UGC07577 object in the nine-object aggregate.

Executable evidence is direct_expansion_comparison.py. Its runtime output
galaxy_response/qumond_disk/DIRECT_EXPANSION_COMPARISON.json pins every field
receipt, data digest, source and gate receipt, and preserves the complete curves
and residuals. DIRECT_EXPANSION_GATES.json records the gate outcomes. This is
author-checked numerical evidence; no formal audit or retained-grade promotion.
