# Focused independent expansion reconstruction review

Reviewer: direct_field_check. Parent remains the scientific author. This is a
source-bound mathematical, numerical and processed-data check, with no formal
audit, status promotion, new research route or author-source edit.

No material correction to the frozen author block is needed. The field and frame
signs, sharp deceleration bound, dynamical equality solution, distance-order
consequence and conditional Gaussian readout are consistent under their stated
premises. All 6,692 checks in the final independent calculation pass, along with
63 source/receipt checks. These counts describe finite checks, not a mathematical
proof of every implementation behavior or a rigorous integration error bound.

The complete proof is separately rederived in INDEPENDENT_DERIVATION.md. In
particular, the matter/scalar energy exchange fixes the trace-source sign; the
completed square retains unsourced kinetic directions; the equality trajectory
has H_* proportional to R_*^[-(3+a)/2] and the stated physical scale-factor power;
and the distance-order bound applies only when the deceleration bound holds over
the entire relevant redshift interval. The a=0 case retains possible uncoupled
scalar kinetic energy. The domain a<1/3 ensures positive physical expansion.
No attraction theorem, spatial-curvature extension or potential is inferred.

The independent code does not import or execute the author's runner. It uses
dimensional scalar momenta/fluid densities, a Friedmann-reconstructed H and Radau
instead of the author's normalized-variable DOP853 evolution. It reconstructs all
5,775 simplex rows, all six synthetic histories and all 108 stored comparison
states across the two author refinements. Exact rational controls also use a
non-diagonal three-field K. Independent 80-node Gauss-Legendre integration checks
all six distance-control rows and all 1,358 distances for each frozen curve.

Maximum observed author/independent discrepancies are 8.88e-16 on the simplex
rows, 8.13e-14 on normalized evolution states and 8.44e-15 on the physical q_J.
The equality trajectory agrees with its independent closed form to 1.37e-13.
The author's Richardson values differ from independent physical acceleration by
at most 1.54e-9. The two numerical predictive-covariance constructions differ by
at most 3.73e-17. These are observed discrepancies, not certified error bounds.

The literal input table and all 2,893,401 covariance entries were read. Manual
whitespace table parsing preserves the CID strings; the covariance parser is
independent of the author's parser. Exact compressed/decompressed hashes, all
1,358 selected row indices, all selected zHD/zHEL/m_b_corr/CID entries, and every
calibration/transfer/contrast index agree. All relevant observation fields are
finite across the full 1,701 rows, including excluded rows. Raw covariance
asymmetry is 3.0000000000038676e-8 against the prefrozen threshold; arithmetic
symmetrization is explicit and both full and predictive matrices are positive
definite without jitter. The full-matrix Cholesky minimum diagonal is
0.06046040535001047. No observation or covariance row was silently removed.

| Row group | Light-curve rows | Distinct literal CID strings |
| --- | ---: | ---: |
| Full release | 1701 | 1543 |
| Frozen selection | 1358 | 1296 |
| Calibration | 405 | 343 |
| Reserved transfer | 953 | 953 |
| High contrast | 469 | 469 |

The selected sample has 49 repeated literal CIDs; no literal CID is shared across
the calibration and transfer partitions. Neither fact establishes a physical
event identity map. In particular, 1,543 literal IDs must not be substituted for
the publication's 1,550 distinct physical supernovae. All repeated light curves
and all released cross-correlations remain in the calculation.

The official release README and SN-only likelihood were read completely from
their pinned local primary copies. The likelihood's angular-diameter-distance
factor (1+zHD)(1+zHEL) is equivalent to the present comoving integral times
(1+zHEL); the code correctly integrates to zHD. Its explicit selection differs
from the official likelihood's default zHD>.01 selection, as declared. It uses
m_b_corr and does not import Cepheid-calibrated MU_SH0ES as an independent SN-only
observation. Swapping zHD into the heliocentric prefactor changes a selected shape
by up to 0.0051138861 mag and is rejected by the independent convention check.

For prediction I construct the full intercept-annihilating residual operator W
and compute W C W^T, rather than using the author's Schur-complement implementation
as the scientific oracle. LU solves and whitened residual norms reproduce the
complete curve, prediction and residual arrays. A separate, explicitly labelled
provenance calculation reproduces the author's exact predictive-covariance byte
hash 6c97f491998dbed4951d97e37e7f8ba9d145e5f9505fa005b2bd8eeb19eacd92.
Omitting intercept uncertainty changes an entry by 0.0003898089 and fails the
control. The calibration-only intercept standard error is 0.008478273354230141.

| Fixed shape | Calibration-only intercept | Calibration chi-square /404 | Conditional transfer chi-square /953 |
| --- | ---: | ---: | ---: |
| q=1/2 | 23.853290968581423 | 382.0851314468949 | 1468.7770777525302 |
| Weak equality | 23.853309595987895 | 382.0905958912589 | 1469.3812919133034 |
| Supplied flat LCDM, Omega_m=.3 | 23.804973801128547 | 373.7357880260023 | 834.1212232129885 |

Every reported fixed-curve array and scalar agrees within the independent frozen
checking tolerances. The largest scalar discrepancy is 5.51e-11 in a quadratic
form. The independent whitened global-intercept projection confirms the sum
identity only; its fitted intercept is never used in the reserved prediction.
The rank 953 accounts for calibration-intercept uncertainty through the predictive
covariance. It does not count independent physical supernovae or add a new fitted
parameter to the transfer sample.

The independent difference-of-group-means calculation yields

    contrast = +0.3085345352698319 mag,
    full-covariance sigma = 0.02379802403453029 mag,
    standardized contrast = 12.964712314860957,
    log-redshift lever = 0.1499939807313954,
    beta cancelling this one contrast = 2.056979445210845.

All 1,358 contrast weights and all four frozen nuisance rows match. The signs are
correct: adding beta log10(1+z) to the mean absolute magnitude predicts a positive
contrast shift; correcting the data subtracts it. Positive within-group weights
are essential for the mean-order result. An independent negative-weight example
demonstrates why replacing these means with arbitrary GLS means is unjustified.
The free cancelling beta is calibrated on this diagnostic and cannot serve as
an independent test. It is not a prediction of stellar evolution or a guarantee
that all remaining residuals disappear.

The observational boundary is substantive. Constant standardized luminosity is
an added premise, not a consequence of universal metric coupling when physical
G varies. Flat optical geometry, distance duality/transparency, ideal source
closure, released redshift corrections, and a fixed Gaussian summary covariance
are also supplied. The reviewed paper methodology describes model-dependent
redshift-error propagation, a reference flat LCDM response in parts of the
systematic covariance, nuisance standardization and duplicate correlations.
These are reasons to keep the inference conditional, not a second independent
measurement. See the primary [Pantheon+ methodology, sections II.1–II.3](https://arxiv.org/html/2202.04077v2).
I read those sections and the abstract, not the full paper or raw-light-curve
pipeline. No independent cosmological recalibration is claimed.

The positive contrast conflicts with the permitted model-mean ordering under
those supplied assumptions. Its standardized value is not a raw-experiment or
globally blind significance. A noisy Gaussian realization is not logically
forbidden by a nonpositive mean; the outcome note's “cannot reproduce this
distance ordering” must be read as the stated conditional mean discrepancy.
The contrast overlaps the transfer diagnostic and cannot be multiplied into an
independent likelihood. No unique dark-energy mechanism, universal scalar-theory
exclusion, or empirically established luminosity evolution follows. The declared
scope files retain these limits; no author correction is requested.

Coverage includes every one of the 24 original block files: complete protocol,
proof, fixtures, manifest, ledger, scope/status/trace files, runner, original
execution/freeze/stdout/stderr, all full-result classes and five executed-source
snapshots. Both gzip inputs are preserved exactly. Four external primary
artifacts were hash-verified; the small README and likelihood have additional
reviewer-owned exact copies, while numeric originals recover exactly from the
snapshotted gzip inputs. Repository cosmology context notes are not new proof
premises and were not re-reviewed or promoted here. No author runner execution,
Git operation, model/settings change, worker launch or author edit occurred.

The preparse freeze records 02:31:51.986066Z; the execution freeze precedes the
single recorded successful author execution at 02:37:33.597740Z. All bindings
match the current original bytes. Recorded freezes establish source continuity;
they do not independently prove the author's prior knowledge or absence of an
earlier inspection. The protocol itself expressly acknowledges public exposure
and uses a local model-development reservation, so no global blinding claim is
being certified. The initial proof's future-tense execution statements and scope
files' “review pending” text are preserved historical bytes, not claims that this
review rewrote or updated them.

One reviewer failure is preserved. My first independent execution had eight
failed equality-oracle comparisons because I used (3-a)/2 for the Einstein H
exponent instead of (3+a)/2. All other 6,684 checks passed. The source, complete
result, stdout/stderr and execution receipt remain in execution_v1 and
INDEPENDENT_RESULTS_v1.json. REVIEWER_CORRECTION_v2.json records the exact two-line
patch: fix that oracle sign and choose a new output path. The second execution
passes all 6,692 checks; its source and logs are independently preserved. The
author's physical exponent and both author ODE refinements were correct throughout.

ORIGINAL_DISPOSITIONS_v1.json lists all 24 original/final path hashes and exact
recoveries, with all originals unchanged. SOURCE_PINS_v1.json,
EXTERNAL_PRIMARY_PINS_v1.json, LINEAGE_RESULTS_v1.json and the final RECEIPT.json
bind this readable report, derivation, independent code, all results and failures.
