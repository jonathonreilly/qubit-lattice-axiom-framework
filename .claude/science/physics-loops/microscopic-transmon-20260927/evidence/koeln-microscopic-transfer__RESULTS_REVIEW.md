# Microscopic-transfer results review

2026-09-27. Bounded static review of RESULTS.md, RAW_TRANSFER_PROTOCOL.md, calibrate_raw_transfer.py, both evaluators, manifests and saved outputs. Reused verified model/source identities and the separate selective forward-spectrum/raw-residual reviews. Independently recomputed evaluation arithmetic using standard-library CSV/JSON operations. No optimizer, new diagonalization, target-dependent fit, or audit verdict.

## Verified coverage

Original INPUTS.json and RAW_TRANSFER_INPUTS.json match every entry. Model identity is unchanged. The raw transfer contains exactly12 unique records: each of raw period starts.15,.22,.30 crossed with cosine and shape starts.01,.1,.4. All are returned/success=True; none was removed. Each calibration_GHz triplet exactly equals the corresponding raw fit's center and full splitting plus the inherited archived12 center, converted Hz→GHz. Omega/G and geometry remain the inherited values. The code never reads03 observations into calibration and uses no target residual in source-version selection, initialization or optimization. All raw inputs are already exposed, so this is retrospective objective separation, not blind validation.

Both evaluators select exactly the source row with timestamp20220729-173536-429-b495bf, not a nearby frequency. It is saved dataframe index31. Its center is14,668,765,535.362667Hz, full dispersion41,322,465.074874Hz, center fit error250,397.781560Hz and dispersion fit error659,798.171271Hz. No estimated dispersive-shift column is applied. Full-dispersion values have no half-amplitude or multiphoton division.

Independently checked all8 original and12 raw-transfer status identities, target dictionaries and recorded input/output hashes, every center/dispersion error, and all36 raw03-center differences (12 predictions×3 extraction centers). All agree with the saved evaluations. Raw03 centers are exactly those in the reviewed three-return extraction file. Reported rounded numerical values in RESULTS.md are consistent with the saved evidence.

| Raw period start | Shape error versus source03 center (MHz) | Shape full-dispersion error (MHz) | Shape error versus raw03 centers, approximately (MHz) |
|---|---:|---:|---:|
|.15|+10.936011|−18.037397|+11.993223|
|.22|+.671195|−3.104338|+1.728408|
|.30|+.647953|−3.066134|+1.705166|

Each row represents three closely agreeing shape starts; all are preserved. Cosine source-center errors are approximately+24.4483,+24.4494,+24.4493MHz. Original archive/processed shape center errors−9.953473/+.930015MHz and full-dispersion errors+16.249573/−3.526868MHz also reproduce. The source-versus-raw03 extraction shift≈1.057212MHz exceeds the source's quoted center fit standard error; the results appropriately do not reinterpret either error as full systematic coverage.

## Claim boundaries and required wording qualifications

The qualitative ordering against the retained cosine controls is supported by the inspected outputs, and no measurement analysis was chosen by03 agreement. However, “a fixed geometric correction improves” must mean the **complete conditional two-arm shared-transparency construction with low-level recalibration**. These files do not isolate the effect of sinc(mB/Bnode) from area-fixed two-arm interference, local-potential shape and refitted EC/Jsum/tau. A causal claim that spatial averaging alone supplies the observed improvement needs a matched declared control with that factor changed; otherwise explicitly keep the composite-model attribution. The cosine controls also omit01 dispersion from their objectives, so their comparison is a declared different-model/different-calibration-constraint comparison, not an equal-objective likelihood contest.

“Processed/raw-supported” is defensible only as shorthand for the two lower-cost raw-Ramsey returned solutions under the specified raw residual model. It is not proof that the processed source version is correct. The full retained.15 raw basin gives materially different predictions; the results explicitly preserve it. Three raw returns are versions of one acquisition, not independent replication. Three nuisance parameters fitting three low-level observables are not validation, parameter identification or microscopic metrology.

The independent<.001Hz spatial/cutoff statement refers to selected **original** cases: archive shape.01, processed shape.01 and processed cosine, as specified in NUMERICAL_REVIEW.md. It must not be read as fresh independent forward/cutoff coverage of all12 raw-transfer parameter sets. RESULTS already says selective forward verification; name those selected cases or explicitly exclude blanket raw-transfer coverage when packaging. This review verifies all12 arithmetic and transfer identities, not their forward spectra by a new implementation.

All prior premises remain: equal current density/shared local transparency, AFM active-area interpretation, conditional Fraunhofer node/common thickness, intended bottom-sweet-spot versus exactpsi=pi, PNS cavity-nuisance transfer, endpoint means as fitted centers, state/charge preparation, time drift and scalar line-shape extraction. The raw03 start agreement is not experimental confidence. Numerical agreement cannot close these observation/source premises or establish native-theory confirmation.

## Code and evidence limits

Calibration saves normal returns and per-start exceptions correctly. Evaluators preserve status but do not propagate optimizer success/optimality into their compact result rows; those diagnostics remain in fit files. Current all20 fits are successful normal returns, so none is silently omitted. Future code should not equate status='returned' with adequate optimization.

Evaluator length/uniqueness assertions check8/12 records, but not the full expected named key sets. I independently checked the expected12-key set here; current output is correct. Raw03 evaluator asserts three entries but not their status, identities or raw-source hash internally; these are checked by this review and the earlier extraction review. Both evaluation outputs record target and fit hashes (raw evaluation also raw03 hash), but evaluator source and target files are not part of the pre-calibration runtime manifests. That is appropriate for target exclusion but is not a complete immutable evaluation freeze. These current identities are recorded below. File content alone does not establish the asserted chronology of a pre-comparison fit-output freeze; this review verifies the saved linkage, not launch timing.

No consequential numerical transcription, target-selection or objective-leakage defect was found. Preserve the composite-model and selective-check scope clarifications above in any publication surface. This remains provisional research with unresolved physical/source uncertainty, not a retained audit outcome.

## SHA-256 identities

| File | SHA-256 |
|---|---|
| RESULTS.md | 6b86ec7d8265d2f8df517bceb05e9c074e0eff204103561bed02fceb26b6a682 |
| RAW_TRANSFER_PROTOCOL.md | 17a88f7f9682eeaa917b68803ad2859b9d785c5c20f9f09c148fb86d5e6514f3 |
| calibrate_raw_transfer.py | 1d6b3e9221966b71d6fab7eacdf8ccb0a15a65d0d946a6793565f89ac0f2707c |
| RAW_TRANSFER_INPUTS.json | f563a01bf59caaf266aa6216002cc2496a18d1d1a2c4db3139a070ad5fa65dc1 |
| model.py | d9db69aa06122958dc81120c1518ef2e3148a01dfd46a2f1820e0d593eac8cf3 |
| raw_transfer_fits.json | 5b25bc09c09331c1683e6cb4b2aa62fdecd45f52bc9e7864a04dbedf8a672491 |
| evaluate.py | d031e4d68c3dffc6bc9a21f308280e412fc8b21e6f982d36590fc13ff98d8b92 |
| evaluate_raw_transfer.py | 22147d0b87aa499607620319d5623075ed7bc86444d7befa7c43895aee37dfbb |
| evaluation.json | 9bb38fd2da52999476173a698d6f11fef82469d8e02116b82ebdfe3f8f7f0f1a |
| raw_transfer_evaluation.json | c5cbb2c2f4db3481bbb1ddb6646c6f38dc849b49ab33584fc06637dff91fc2a4 |
| fits.json | 1db744ff5ff43d6165f1ae7dfec5a49911be64e413ecfd7addb7d09fc9615786 |
| NUMERICAL_REVIEW.md | 74a8ec5d355b44547d40df03efd2b24e2f751148e7bd47bede897cc7455ae5f6 |
| ../koeln-ramsey-reanalysis/fits.json | 4bab159078275824642eec59d4ce02415438419fedeed62f82795eeb64c1b5eb |
| ../koeln-energy-addition/raw03_results.json | 1437878340418c6d03f062acaa58ac6d3ef14b0fc42922a55468dd5cb49d42df |
| ../koeln-two-junction/source-data/df_spec_vs_gate_03_incl_disp_shift.csv | d2d0a7ab2aa15651eabbf1a9c4af7611fd3f6a2e5f51ec91cf4e23313402a7ee |
