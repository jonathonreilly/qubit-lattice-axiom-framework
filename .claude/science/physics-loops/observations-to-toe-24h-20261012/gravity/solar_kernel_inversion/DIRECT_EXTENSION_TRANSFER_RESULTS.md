# Both frozen responses fail the six-source development transfer

Direct parent analysis, 2026-10-12. The fixed numerical driver completed
at 22:04:38Z with exit 0. Both unchanged responses passed every numerical
source gate, then failed the stated observational rectangles. This changes
the campaign's inference: three-source fitted compatibility did not extend
to the declared additional sources under the fixed source/measurement map.

The comparison uses previously exposed observations outside these two fits.
It is a development transfer, not blind validation. Neither response, its
E, any source selection, mass ratio, distance, inclination, vertical profile
or score mask changed. No new fit preceded preserving these results.

## Numerical qualification and independent parent arithmetic

All twelve candidate/source gates passed. The largest sampled radial-force
change on refinement was 0.0024392553723255883; the largest on boundary
extension was 2.2631440954601345e-7. Positivity, source/control identities and
all frozen weights remained intact. These are the declared numerical
checks, not a rigorous total discretization-error bound.

The parent wrote direct_transfer_readout_check.py before the final score
was available. It reads and verifies all six numerical receipts first,
checks processed source/target file hashes, compares every measured array,
and recomputes scores directly in velocity units without importing the
original scoring helper. All 36 candidate/source/method combinations agree.
The official result and the independent parent readout preserve base,
refined and boundary scores.

At 22:05Z a completed-driver log poll exposed the final combined score
tail. The parent then explicitly checked all twelve numerical gates before
running the full processed-target readout. No source selection, inference
or parameter change occurred between that tail and the gate check. This
does not make the already exposed data blind.

## Frozen outcome

The per-source figures below use the refined fields. Let
L=max(0,V-2 err)^2/R, H=(V+2 err)^2/R, A=V^2/R. The reported t is
max over the source's scored bins of max(0,(g-H)/A,(L-g)/A).
It is an acceleration-rectangle relaxation, not a p-value or a velocity
percentage. The processed error rectangles are descriptive, not a joint
statistical confidence region.

| Source | Original RMS log10 V | Original t | Interior RMS log10 V | Interior t |
|---|---:|---:|---:|---:|
| NGC3949 | 0.0405062363 | 0.1616455854 | 0.0422624614 | 0.2028470753 |
| NGC3972 | 0.0977754835 | 0.2802015024 | 0.0808968105 | 0.1999065808 |
| UGC06667 | 0.3320272783 | 0.6513721964 | 0.3020921184 | 0.6114844560 |
| UGC08837 | 0.0397642275 | 0 | 0.0653515540 | 0.2396868789 |
| DDO064 | 0.1535160511 | 0.1587422480 | 0.0933768424 | 0.0185441305 |
| DDO168 | 0.1229835299 | 0.4401743160 | 0.0882146211 | 0.2709970388 |

The original candidate fails at 5/6 sources and 32/50 scored bins; its
equal-galaxy RMS log10 velocity residual is 0.16417279223866804. The interior
candidate fails at 6/6 sources and 30/50 bins, with equal-galaxy RMS
0.1416344692630286. Both fail the all-source comparison. A smaller aggregate
score does not turn the interior candidate into a passing result.

The largest acceleration-rectangle violation for both is UGC06667 at
R=3.5 kpc. The observed processed velocity is 69.3 km/s with error 3.0 km/s,
so the fixed rectangle is [63.3,75.3] km/s. Predictions are
29.64256298988098 and 32.71455356336795 km/s. Conversely, at NGC3949,
R=3.5 kpc, the processed rectangle is [139.6,164.4] km/s while the
predictions are 175.3910476744609 and 178.0840779716831 km/s.
There are both underpredictions and overpredictions.

## Exploratory diagnosis after the frozen failure

A shared multiplication of already predicted circular velocities cannot
put every bin inside its rectangle. Intersecting the fifty allowed scale
intervals gives:
- original: scale must be at least 2.4116981468658962 (UGC06667 at 2.61 kpc)
  and at most 0.9373340440108373 (NGC3949 at 3.5 kpc);
- interior: at least 2.225097916621487 (UGC06667 at 2.61 kpc)
  and at most 0.9121672158862082 (DDO168 at 1.24 kpc).

These intervals are empty. This is only a postprediction normalization
diagnostic, not a self-consistent change to G, mass-to-light ratio,
distances, source profiles or the nonlinear response N(A). It neither
fits nor excludes such a different physical model.

At the largest-t UGC06667 bin, the same refined source geometry gives
Newtonian circular speed 20.38985365530663 km/s. Candidate radial-force
enhancements over that field are 2.1135050281833805 and 2.5742681224322688;
the observed acceleration ratio under that source model is
11.551496524855674. This locates the missing acceleration under the supplied
source model. It does not identify dark matter, modified dynamics, or
source-systematic error. In a disk, a local value of N alone is not a
universal bound on the projected force; no such inequality is assumed.

## Revision and completion limits

Preserve both candidates as failed frozen transfers. Their earlier fitted
solar/external rectangles and three-source results remain separate facts.
Neither the entire twenty-ramp family nor all modified gravity has been
tested by carrying two selected responses. The next observation-driven
question is whether the SAME response family, with a newly declared exposed
nine-source development fit, can accommodate the combined data and the
existing solar/external working constraints. Any fit must have a new name,
protocol and artifacts and must keep this failure intact. No claimed
independent validation can reuse these now-exposed targets.

Source nuisances, pressure support, the imposed baryonic reconstruction and
the empirical-error model still matter. This comparison supplies no complete
likelihood, significance, cosmology, lensing or radiative test. The separately
checked dynamical attempt has its own anisotropic propagation failure;
neither its positive field energy nor this transfer can validate the other.

Evidence: extension_transfer_readout_v1.json,
extension_transfer_shape_diagnostic_v1.json, direct_transfer_readout_check.py,
and the exact original input/results/receipts copied into
extension_transfer_evidence/. A focused independent final-readout check is
complete; the parent read its full report. All36 score rows, all12 numerical
gate decisions and source/target/weight identities agree, with no material
discrepancy. The report and separate arithmetic are preserved in
independent_transfer_readout_review/TRANSFER_READOUT_REVIEW.md.
