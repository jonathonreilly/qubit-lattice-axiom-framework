# M14 canonical forward and potential correspondence, version 1

This is a focused source, saved-value and execution-envelope check by the independent numerical checker. It is not a new author result, a formal audit, an integrated landing review, an empirical validation or an ODE rerun. Root remains the author. No files outside this checker's assigned directory were written.

## Exposure and immutable evidence

The independent equations, implementation, Radau trajectories and potential diagnostic were frozen before root-source exposure. Their original reports remain unchanged: `DYNAMICAL_FORWARD_REVIEW_v1.md` SHA256 `7510a44722f33175b0199cbc963c0b1e5c833717e4033c07f1bba983eebc68f8` and `POTENTIAL_REVIEW_v1.md` SHA256 `27b6c5675aeea6ecc0389e892377dfdc066a0fbebb5abd9666fe580a0114bfe0`.

For this review I read the complete v1 primary, forward and extensions helpers, all three remaining helpers for their interacting premises and read closure, and the complete canonical note. I also read the original root postprocess source/result for potential correspondence. The source freeze was read before copying source bytes; by the copy step root had begun the announced affected update. Any changed v1 file was therefore copied from the independent-equations reviewer's already frozen snapshot and independently verified against the exact SHA256 in root's v1 freeze. Other files were copied from the working tree only after matching that freeze. `CANONICAL_EXPOSURE_v1.json` records each copy's provenance. An initial preparatory copy command used the wrong JSON key (`sources` rather than `files`) and stopped before source copying; that setup failure is recorded there. No scientific calculation or comparison failed in this step.

The v1 snapshot binds primary `cea1f8f345aa64adf0c2a903b25133418e0389c06b48691e50b553a5d7e341b4`, forward `b7ece5a9ea1e48334c1ee9301b4ca3b5e59f7246f6837ec5b9e0c2b47e64f005`, extensions `935f99266dc7b93ea90589c60a5c35e71accec69bac4592dd11a333d19798f14`, and note `326ad86376122e55c9ff2804d91b7ec95e7e5fa7b43e349a0b834257f0fd810f`. The complete input map is in the exposure and result JSON. These identities are historical v1 after root's affected changes. This report does not claim that its 81-control cache binds later bytes.

## Source and read closure

The primary imports five local helpers: forward, geometry, extensions, domains and covariance. Its eight declared local inputs are those five sources, the canonical note, the unchanged fixed forward protocol and the scope checklist. Primary source is separately hashed. The only numerical scientific file read by the run is the fixed protocol; the action and equations are assembled in the helpers. The other reads are source-integrity hashing. No older result, independent result, unmerged helper or observation is imported as a computational premise. Only RESULTS and SUMMARY are written under the selected output directory. The default directory and command are consistent with the note.

The forward helper is the reviewed working implementation with (i) an explicit guard for Q=Hv=1 and modes 0,1,2 plus reserved mode 3, (ii) the already computed physical h_J added to saved output, and (iii) the former standalone wrapper removed. Its background, action derivatives, initial 00 constraint, coupled scalar/dust ODE, physical-frame transformations, dense output, inversion and numerical thresholds are unchanged. The canonical wrapper adds a finite saved-epoch domain gate and records the y-sign transitions. This is a fixed-protocol test implementation, not an assertion that arbitrary protocol edits are supported. The potential calibration/reserved indices are explicitly coded as 0,2 and 3–6 and agree with the frozen protocol.

The scalar equation contains rho(b_chi+b²)X and the matter lapse source. Number and mass contrasts, velocity sign, Einstein/Jordan clock conversion and the canonical field normalization match the independent precheck. The first three modes invert the momentum equation, the fourth tests the same coefficients. Initial X and Xdot are specified freely; only the number contrast is solved from 00. Neither a quasistatic relation r=q nor subsequent constraint projection is imposed. The source's candidate F relation and beta/kappa reconstruction agree with the independent B=1/kappa convention.

The extensions helper's trace, background and potential identities agree with the independently derived equations. The covariance extension uses the real bilinear ensemble correlation and retains the otherwise missing separate time leg in its counterexample. The new equal-time lift correctly removes that leg by combining S'−yV' at one epoch, where y is not differentiated. Its row multiplication, monomial consistency checks, positive R/q and nonzero y requirements agree with the displayed theorem. Five independent covariance rows are a sufficient conditional construction; they do not guarantee measured rank or imply a minimum-data result. The domain helper's Neumann bound certifies the stated coefficients under supplied input envelopes, not all observable denominators. The revised positive-coefficients label preserves that distinction. I did not execute the covariance, rational-corner or geometric suites again; the separate equation and observation checkers own their independent proof controls.

## All saved trajectory values

`canonical_correspondence_v1.py` reads saved products only and imports no scientific helper. Its 16 correspondence/integrity checks pass. Removing only the newly saved h_J, new sampled-domain check and turning metadata makes each canonical case exactly equal as parsed JSON to the original working case. This includes all 56 mode rows, 14 epoch records, initial data, candidate values, solver counts, reserved residuals and the root 301-time constraint maxima.

All 56 rows and 14 epochs were also compared directly with the frozen independent Radau results using the original physical-coordinate dictionary. Independent aE0=1 and normalized aJ=A*aE/A0 correspond to root aE0=1/A0, so root k_com equals independent k_com/A0. The inferred matrix rows differ by a harmless row scaling; condition numbers of those differently scaled matrices must not be equated.

Maximum absolute canonical-versus-independent differences are 7.87e-14 in inferred q, 2.43e-14 in P, 3.71e-13 in P3, 2.85e-13 in r and 6.45e-18 in Xdot. Newly saved h_J differs by at most 5.33e-15. The complete field-by-field maxima and locations are retained. This repeats saved-value correspondence, not integration or raw independent controls.

Root's maximum 00 diagnostic covers 301 times per background; the independent numerical constraint check covers seven saved epochs per background. The complete source/report preserve that difference. Both root and independent saved y values change sign between fractions 0.10 and 0.25. Continuity would force a zero for an exact history retaining those signs, but no rigorous interval/root enclosure was calculated. The pointwise q=x/y inverse is not uniformly established across either turning point. The wrapper's gate is sampled, not an interval gate.

The original protocol key `reserved_scaled_max` bounds absolute dimensionless residuals in root's forward code. Independent original summaries also have term-normalized diagnostics; these are not silently equated. The earlier correspondence explicitly checked the root-style absolute candidate residual at the same unchanged threshold. The canonical prose and `history_scope` state this limitation.

## Potential diagnostic and conditioning

The independently frozen potential equation is

    V_J/(F H0²) = E²[3+3x−(1/q−3)x²/4]−3R aJ^-3.

With recovered beta, the radial chart gives k=[1−2sqrt(1−3beta)]/3, e_u=(beta/q−1)/[(1−3beta)s_m], u=ln(e_u)/(2sqrt(beta)), and C=(1+s_m)e_u/(1+s_m e_u). Then C V_J/(2F H0²)=gamma U0+(gamma nu)U1. Root implements exactly these formulas. It solves the two supplied basis rows at epochs 0 and 2, using inferred R,x,q,beta and physical HJ/H0; the source u and nu fields are appended for diagnostic comparison only. No truth parameter is substituted into the inverse. Later rows 3–6 use that same fitted pair. Epoch 1 is retained but not presented as a reserved test.

Canonical potential values are exactly equal to the original root postprocess result. The independent results are close rather than bit-identical, as expected for this ill-conditioned inversion:

| Case | Root gamma | Independent gamma | Root nu | Independent nu | Root raw basis condition |
|---|---:|---:|---:|---:|---:|
| positive_roll | 0.7886707325757166 | 0.7886707325594247 | 0.6999999722271422 | 0.6999999900775549 | 976255.322486162 |
| negative_roll | 0.7152287893241936 | 0.7152287893155684 | 1.400000003744959 | 1.399999995673176 | 107337.05132072301 |

Root-minus-independent nu is −1.7850e-8 and +8.0718e-9. Relative to the supplied truth, root nu errors are −2.7773e-8 and +3.7450e-9, while independent errors are −9.9224e-9 and −4.3268e-9. Root later absolute residual maxima are 3.0146e-12 and 5.9395e-13; independent maxima are 1.1606e-12 and 5.1914e-13. Root stores target-minus-prediction, the independent file prediction-minus-target; magnitudes are compared with that sign difference explicit. The independent column-normalized conditions are about 393.26 and 34.77, so the raw matrix conditions include basis scaling as well as near dependence.

No new potential threshold was added, no failed comparison was discarded, and no observed precision, rigorous ODE error or action/scale selection follows from these diagnostic residuals. The potential basis, normalization and branch remain supplied. Both reports retain that limitation.

## V1 output/cache binding and disposition

The v1 result SHA256 is `6572a6a54285ecfebd941b2e49ec59606428eb8bf2a441da2a6cf362c9852619`; summary is `a6517c93aea237e734f62db919847726a916c409b6de8b80c7a337f1e7fbff68`; cache is `b16f96d69e88aaa9e12176ce5af14a698d4aeab596aa3e32f5b4fc0e9db38f3c`. Independent recomputation of the ordered length-delimited input fingerprint gives `2006a7210698d2f95a3e50cbaa0f3b99fe12c6419c0adc673b036c0e66584356`, exactly the cache header. The primary SHA and every input SHA agree with v1 frozen bytes. Cache stdout JSON equals SUMMARY; SUMMARY is exactly the declared RESULTS projection. All 81 declared controls are true, the failure list is empty, empirical_tests is zero, and the cache records exit 0, status ok, 2.16 seconds against 180 seconds.

No numerical or physical finding prevents correspondence of this v1 canonical forward/potential unit to the independently checked material. The current source has already received root's announced potential-control extraction and affected covariance wording/controls; those later bytes require their own narrow confirmation and fresh cache. This v1 report and all pre-exposure evidence remain historical, immutable and independently scoped. Full integrated-main validation, formal audit and actual observational inference are outside this check.
