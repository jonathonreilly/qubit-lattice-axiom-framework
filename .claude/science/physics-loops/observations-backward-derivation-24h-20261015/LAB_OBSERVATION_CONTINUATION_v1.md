# Laboratory observation intake: published processed records

The frozen `LAB_OBSERVATION_ACCESS_PLAN_v1.json` preceded access to John G. Lee's
2020 thesis, *A Fourier-Bessel Test of the Gravitational Inverse-Square Law*.
The [University of Washington record](https://digital.lib.washington.edu/researchworks/items/971237d1-100a-41ae-9027-d1bbce8cf315/full)
identifies an open-access, CC-BY source. The exact public PDF, retrieval failures
and ordinary unauthenticated recovery are pinned in `LAB_THESIS_RETRIEVAL_v1.json`.
No subscription, login, private file share, or experimenter's raw files were used.

## What is now available

`LEE2020_APPENDIX_A1_v1.csv` contains all 95 printed science rows and three torque
channels per row, with printed uncertainties and page provenance. Values are in
micrometres and femtonewton-metres. The table is Appendix A.1, printed pages
146–150 / PDF pages 158–162 of the
[thesis](https://digital.lib.washington.edu/researchworks/bitstreams/6013936a-da00-42b7-ba0a-4dff0cb05bf8/download).
The original table precision is preserved numerically; conversion to CSV does not
create more measurement precision. No rows were removed or fitted here.

Root inspected rendered images of all five table pages. Independent PDF engines
with different row segmentation agree exactly on all 760 numerical cells, run
identifiers and page identifiers. The reproducible extractor regenerates the
original CSV byte-for-byte. Receipts separately record visual inspection and
computational transcription verification. These checks establish transcription
correspondence, not experimental validity.

Appendix A.1 says the listed torques have already been phase rotated, calibrated,
and corrected for systematic contributions. Its `kun` labels flag interpolation
of missing records in the original reduction; preserve the labels. Previously
excluded touching runs are not in this printed list. Chapter 11 determines the
common phase using the full run collection. Accordingly, these records are
**exposed processed development data**, neither primitive angle records nor an
independent empirical test. The published fit summaries were also read; a later
reproduction cannot be described as an unseen prediction.

## Measurement assumptions that the table does not remove

Chapters 8 and 11 (printed 84–95 and 123–137) describe the forward model and
calibration. Angle-to-torque conversion uses measured resonance and damping,
a modeled moment of inertia, and an angular scale. External spheres calibrate
their combined scale through a Newtonian torque calculation using a supplied G.
The calibration harmonic matches the frequency of the 120-fold science signal.
Thus a calibrated torque column alone is not an independent determination of
the scalar tensor coupling `GT=1/(8 pi F0)`. Frequency-transfer corrections,
calibration scalar leakage and environmental applicability still need bounds.

The science model includes Fourier-Bessel geometry, density contrast, radial
misalignment and tilt corrections. It has 17 measured model parameters; the
reported simplified fit varies five. The overcut parameter represents a chosen
surface-roughness model. The cost also propagates separation error through the
model derivative and includes auxiliary measurement terms. Copying best-fit
Newtonian nuisance values into a scalar fit would be an additional assumption.
Appendix A.1 alone does not provide per-run lateral positions, the original
Fourier-Bessel interpolation tables, the full complex records or their covariance.
Their absence from the inspected table is not a claim that they do not exist.

Two source correspondence issues remain explicit. Appendix A.1 includes printed
separations down to 46.2 micrometres, while Chapter 11 describes a minimum of 52.
Chapter 11 defines total separation using a shared coating/screen offset; the
mapping of that definition to the appendix has not yet been resolved. Do not
silently shift or discard rows. Also, the rendered calibration table on printed
page 95 literally shows G with exponent **+11**. It has not been replaced in a
numeric input. Recompute the published calibration expression and check the
necessary value against its reported torque before attributing this apparent
typographical issue. Neither issue is evidence of non-Newtonian physics.

## Next useful work

First reconstruct the published calibration expression and its units from
independent geometry, preserving which quantities were measured and which were
computed. Then determine whether enough public geometry and per-run corrections
exist for a faithful Newtonian reference reproduction. Freeze that computation
before testing a scalar modification. If necessary inputs remain unavailable,
derive an explicit uncertainty envelope or change to a dataset with the required
primitive channels; do not replace missing inputs by a chosen profile or zero
correction. Any physical exclusion must retain material stress, boundary response,
screening, calibration and environmental registration conditions. No fit,
likelihood reproduction, scalar exclusion or theory validation is claimed here.
