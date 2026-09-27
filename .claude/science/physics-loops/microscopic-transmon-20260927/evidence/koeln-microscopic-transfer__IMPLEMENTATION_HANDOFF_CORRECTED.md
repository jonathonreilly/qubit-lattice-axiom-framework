# Corrected portable implementation handoff

The current portable comparator now uses source-corrected265-delay raw calibration inputs and their24 downstream circuit snapshots. Original archive/processed source8 and targets are byte-unchanged. No optimizer, raw extraction, PR/pipeline, commit or publication action was performed. Parent owns note and final source/data review and integration decisions.

## Independent work first

New external koeln-microscopic-corrected/NUMERICAL_REVIEW.md and independent_ablation_check.py/snapshot/results/log plus independent_key_controls.json check all24 exact keys and calibration vectors from corrected raw265 inputs. The raw_period_0.3/.01 spatial/ablation pair was independently reconstructed by direct real-space spatial/phase quadrature and full charge-photon diagonalization at N22/K12 and N28/K16. Maximum primary difference0.000402Hz, cutoff change0.000544Hz. Fine f03 spatial14.669197761379290GHz, ablation14.669393228527792GHz; full endpoint dispersions.03861090195725403 and.03858933833220313GHz. This is selected numerical consistency, not global parameter or physical preparation identification.

## Portable data and code changes

- Replaced current raw_transfer_fits.json / harmonic_ablation_fits.json with all24 corrected circuit fits. No row dropped or selected by target.
- Kept original source fits.json8 and targets.json unchanged.
- Replaced current independent_anchors.json with the new independent pair, which the primary actually recomputes.
- Updated calibration.json with corrected centers/splittings/costs/statuses, membership16430coordinates/265delays and excluded reference times. Its .15-period-start raw calibration success=false is explicit; downstream circuit success=true is separately emitted. The .15 family is labelled nonconverged raw-calibration diagnostic in every corresponding result.
- Preserved old raw24, prior calibration ledger/anchors/protocol byte-for-byte under data/.../historical with SCOPE.json warning: mixed-observation267-sample arrays included2 reference points and are not current/preferred-fit evidence. Historical records are read only for integrity, never current predictions.
- Added REFERENCE_CORRECTED_PROTOCOL.md and provenance entries for corrected upstream circuit/raw fits and independent evidence, with complete included-file pins and AUDIT_INPUT_PATHS closure. Updated emitted scope/read inventory. Independent helper is unchanged.

All32 current predictions/comparisons still execute (source8 plus corrected raw24). No raw03 dispersion statistic is introduced. No target proximity determines a pass. Constants, geometry, numerical Hamiltonian, target arrays and conditional assumptions are unchanged; only the corrected supplied raw calibration snapshots feed the raw24 families. Old upstream fit/review bytes are untouched. Previous portable external logs in the transfer directory were refreshed by the existing harness; complete corrected-run logs and receipts are now copied to koeln-microscopic-corrected, which is the authoritative execution evidence for this handoff.

## Execution evidence

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/microscopic_transmon_2026_09_27.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/microscopic_transmon_2026_09_27.py --mutation FAMILY
```

Runner exits0: TOTAL: PASS=163 FAIL=0. All six mutations data/split/normalization/field/coupling/independent exit1 at their affected real checks. PYTHONHASHSEED1/913 stdout is byte-identical. These logs are not canonical runner-cache envelopes; parent should regenerate the envelope after final closure. No full integration pipeline run.

- `portable_runner.log` (corrected external directory): exit0, SHA256 `2d68ec862f68e384a708b801b0fd60d740b4bb14fb422a9859abe2949d2a6f13`.
- `portable_mutation_data.log` (corrected external directory): exit1, SHA256 `53f9d43a50fe489a25c9fa24b55020c672bcb0f29fc8321ca2417dbfb67cfa58`.
- `portable_mutation_split.log` (corrected external directory): exit1, SHA256 `fa3c776212c4fd3ba1424161e3dfd4c819c60cffbc91b0dd30f10581e4c6654c`.
- `portable_mutation_normalization.log` (corrected external directory): exit1, SHA256 `fa3c776212c4fd3ba1424161e3dfd4c819c60cffbc91b0dd30f10581e4c6654c`.
- `portable_mutation_field.log` (corrected external directory): exit1, SHA256 `041162b27935fc318f8d71cfb900af5e0b184048f152075f798e8cdf08383ee7`.
- `portable_mutation_coupling.log` (corrected external directory): exit1, SHA256 `fa3c776212c4fd3ba1424161e3dfd4c819c60cffbc91b0dd30f10581e4c6654c`.
- `portable_mutation_independent.log` (corrected external directory): exit1, SHA256 `fb374b98fdb6c599e041289ddae10d8617d9db57a68e1a57cddf191f6c8fcd93`.
- Deterministic stdout SHA256 `2d68ec862f68e384a708b801b0fd60d740b4bb14fb422a9859abe2949d2a6f13`; evidence portable_determinism_results.json and portable_hashseed_1/913.log.

## Current file identities

- `scripts/microscopic_transmon_2026_09_27.py`: `665bad885d7b5681fa692a980b1876ee9d6c50d3d30ed74458be49d83465de0c`
- `scripts/microscopic_transmon_independent_2026_09_27.py`: `2fddf6f97495fdfcda12a6b51814a5a9f1cb24600e94e8fcd9cfb4ade9599066`
- `data/microscopic_transmon_2026_09_27/HARMONIC_ABLATION_PROTOCOL.md`: `25e6fd73b2debf7af248f525b95b91ae53bec138767b1e8668836b15a410c89a`
- `data/microscopic_transmon_2026_09_27/PROTOCOL.md`: `d5d6ffc5674ccd62e5468c29e9980a55dbcc74927120548d391ad3c82afce061`
- `data/microscopic_transmon_2026_09_27/REFERENCE_CORRECTED_PROTOCOL.md`: `7925802e312340caa7674328571ebd949c480bcf7481c1b676adf33ad5ecf8ca`
- `data/microscopic_transmon_2026_09_27/calibration.json`: `a73ffeca68ca754e81d2fee5bad7a9acd795af30e486eb050b73ffb5326e9cff`
- `data/microscopic_transmon_2026_09_27/cosine_control.json`: `19311d798ff3c017bc269d790b37217dc4cac00dc41761a84a16775da13e3f88`
- `data/microscopic_transmon_2026_09_27/fits.json`: `1db744ff5ff43d6165f1ae7dfec5a49911be64e413ecfd7addb7d09fc9615786`
- `data/microscopic_transmon_2026_09_27/harmonic_ablation_fits.json`: `71a135379713aa516bd8b75450b3887727d153e728148421d69fe302bef32f65`
- `data/microscopic_transmon_2026_09_27/historical/HARMONIC_ABLATION_PROTOCOL.md`: `25e6fd73b2debf7af248f525b95b91ae53bec138767b1e8668836b15a410c89a`
- `data/microscopic_transmon_2026_09_27/historical/SCOPE.json`: `e8b1fde0415c7a6d0d6f6a466d27ea21b64f67d497b54c199047489c177839b7`
- `data/microscopic_transmon_2026_09_27/historical/calibration.json`: `2e80a3646f6a2527a62c208ce31ccbc3258eb796ac5452dbd009be698d5b5f1b`
- `data/microscopic_transmon_2026_09_27/historical/harmonic_ablation_fits.json`: `fca3770298f91ed7cc158c811fba8fe44c567bd2b946111187f44a72fe60ee9d`
- `data/microscopic_transmon_2026_09_27/historical/independent_anchors.json`: `3e9df2e7e2067c8800cb3267f3689fcb081d4474f1c32d6e19461094e8f007ea`
- `data/microscopic_transmon_2026_09_27/historical/raw_transfer_fits.json`: `5b25bc09c09331c1683e6cb4b2aa62fdecd45f52bc9e7864a04dbedf8a672491`
- `data/microscopic_transmon_2026_09_27/independent_anchors.json`: `8b6e1ad18d6aa4127fae86f68e5b63125e57d31a707ccb00a6f5468f51877502`
- `data/microscopic_transmon_2026_09_27/provenance.json`: `95cf618298ba1ac448fc5c57dab49def02427805fb4e11fe92fc69466e439445`
- `data/microscopic_transmon_2026_09_27/raw_transfer_fits.json`: `0a8b8b6786c913374895951a0b9908d274130bb0c16d5824ebf1ef12c4182d3e`
- `data/microscopic_transmon_2026_09_27/targets.json`: `66401169f1b76bc4813019f0e3247227f6fc793033404146ea440c306d00e084`
