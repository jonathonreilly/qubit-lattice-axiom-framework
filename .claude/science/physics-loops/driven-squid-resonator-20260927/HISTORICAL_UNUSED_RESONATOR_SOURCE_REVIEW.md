# Independent source/extraction review: unused resonator columns

The two large-residual columns contain genuine dominant measured dips near their extracted centers. They are not obvious cases where a one-dip optimizer selected a nonexistent feature. Their centers are stable between the two supplied symmetric line shapes, but the dips have small bottom structure and reduced depth, and the nearby maps show local disturbances. The available data do not exclude an unresolved mixture or independently establish that the dip center equals the chosen ground-state cavity energy difference.

The unused-column comparison is therefore a meaningful **conditional response-center diagnostic**, with its large local discrepancies retained. It is not an assignment-free test of microscopic cavity frequencies, and line-shape agreement must not be treated as a calibrated experimental error.

## Source coordinates and units

Independently reopened the author `source-figure3.xlsx` and compared all entries of `fig3_f_data`, `fig3_f_x_mesh`, and `fig3_f_y_mesh` with the saved `resonator_maps.npz`. All three arrays are identical, with shape 55 frequency rows × 401 flux columns. This check read only data/axis sheets, not theoretical curves. Evidence is in `unused_resonator_source_identity_check.json`.

Flux runs from 0.4860255802936997 to 0.5144481288488868 in units Φext/Φ0. The frequency coordinate spans −0.20 to +0.88 MHz in 0.02 MHz = 20 kHz steps. The source figure, independently retrieved and preserved as `published-figure3-source.png`, explicitly labels panels e/f “Frequency (MHz)” with a `+7.6918 GHz` reference above the axes. The published caption also describes measurements around that reference.

Thus `f_y_mesh/1000` is the **offset in GHz**, as used in extraction; it is not the absolute resonator frequency. Absolute frequency would be `7.6918 GHz + offset_GHz`. This reference convention is established directly from the published figure. It still does not establish that 7.6918 GHz is a separately measured bare frequency; the earlier source-review limits on high-power provenance remain applicable.

Source figure URL: https://media.springernature.com/lw1200/springer-static/image/art%3A10.1038%2Fs41567-026-03285-5/MediaObjects/41567_2026_3285_Fig3_HTML.png . Published caption: https://www.nature.com/articles/s41567-026-03285-5/figures/3 . Theoretical overlays in that image were not used to derive observed centers.

## Separation and extraction dependencies

The saved 22 calibration columns and 20 reserved columns are disjoint. `extract_resonator_ridge.py` fits each calibration column separately, using only within-column Gaussian smoothing to initialize a nonlinear fit to the unsmoothed column. It has no flux smoothing or joint center curve through reserved columns. `unused_resonator_extract.py` uses the same measured-only per-column initialization and Lorentzian fit, then a Gaussian alternative. Prediction data are loaded only after all measured fits have been constructed and written, for comparison arithmetic. They do not enter either fit objective.

All five files in `FROZEN_UNUSED_RESONATOR_PREDICTIONS.json` match their recorded hashes. This verifies content identity, not an independently witnessed timeline or blindness. These are interleaved columns of a previously viewed sweep; source axes, acquisition systematics, and calibration-model assumptions are shared. The full-cavity evaluation was added after the perturbative reserved comparison and is expressly a no-refit follow-up, not a second blind test.

The new independent plotting/check script reads existing fit parameters and raw published signal arrays, reconstructs fitted profiles and residuals, and does **not** fit new target parameters or change the author's extraction. Numeric cavity-shift reconstruction is outside this source review.

## Raw profiles and neighboring columns

Inspected raw columns 40/50/60 and 240/250/260, reconstructed their existing Lorentzian curves, and plotted Gaussian alternatives where available. The normalized signal RMS residuals recompute exactly. Plots are preserved as `unused_resonator_raw_slices_review.png`; local unsmoothed maps covering columns 30–70 and 230–270 are in `unused_resonator_local_maps_review.png`.

| Column | Flux | Lorentzian center offset (MHz) | Raw minimum offset (MHz) | Lorentzian HWHM (MHz) |
|---|---:|---:|---:|---:|
| 40 | 0.488867835 | 0.485760 | 0.480 | 0.077457 |
| 50 | 0.489578399 | 0.338933 | 0.340 | 0.087151 |
| 60 | 0.490288963 | 0.425141 | 0.420 | 0.077358 |
| 240 | 0.503079109 | 0.185589 | 0.180 | 0.076228 |
| 250 | 0.503789673 | 0.241155 | 0.240 | 0.085553 |
| 260 | 0.504500237 | 0.207494 | 0.200 | 0.077953 |

Column 50 has a dominant dip at approximately +0.34 MHz, visibly below the resonance positions of both calibration neighbors. Column 250 has a dominant dip near +0.24 MHz, above both listed neighbors. Their raw minima are close to the fitted centers; their local anomalies are present before fitting. Nearby unsmoothed maps show rapidly changing structures near each selected column, so smooth interpolation between calibration columns would hide relevant measured behavior.

Neither inspected slice shows a cleanly resolved pair of well-separated minima. Both have slight structure or shoulders near the dip bottom and shallower minima (normalized signal about 0.164 and 0.176) than the selected neighbors (about 0.027–0.093). A one-dip center is a reasonable descriptive location for the dominant observed trough at this resolution. That does not establish a single physical resonance: unresolved state mixtures, overlapping transitions, or other response structure remain possible. No doublet decomposition or cause identification was attempted.

The existing Gaussian fits give centers only 0.594 kHz and 1.192 kHz above the Lorentzian centers for columns 50 and 250 respectively. Across all 20 reserved columns, the maximum shape-center difference is 2.641537 kHz. At columns 50/250, Gaussian normalized residual RMS is 0.01491/0.02329 versus Lorentzian 0.03472/0.04071, showing meaningful wing/shape mismatch even though fitted centers agree. No bounds are active in either outlier fit.

The 20 kHz sampling does not automatically forbid subpixel center inference across a dip spanning many rows; these HWHM values span roughly four frequency bins. Nevertheless, agreement of two symmetric templates cannot constrain shared asymmetry or unresolved-response bias. Width is not center uncertainty, Gaussian sigma is not Lorentzian HWHM, and neither residual RMS nor the 2.64 kHz template difference is an experimental confidence interval.

## Consequences for the reported discrepancy

The source/extraction evidence gives no basis to erase the approximately 108 kHz discrepancy at column 50 or approximately 115–120 kHz discrepancy at column 250 merely as fit failures. Their measured centers correspond to real local dip positions. The supplied full-cavity residuals and 36–37 kHz aggregate RMS should remain reported conditionally, with the numeric review providing independent model arithmetic.

Conversely, these figures do not by themselves isolate a Hamiltonian error. The published caption's ground-state wording describes the theoretical resonator curve; independent device-population verification during the sweep remains absent from the reviewed source. The 25 mK refrigerator setting does not establish canonical device populations. A measured transmission/digitizer dip center may differ from a selected undamped eigenenergy gap under mixed populations or driven dissipative readout. Those observable-mapping limits are particularly relevant near local spectral disturbances.

Use the two-shape extraction agreement to support robustness of the **descriptive measured trough location**, not to claim statistical significance or a validated single-transition interpretation. Keep both outliers, preparation alternatives, and source-coordinate assumptions explicit. This review introduces no new exclusions, target fitting, or changes to the physics parameters.

## Preserved evidence and hashes

Independent script/results/log and the two local plots are preserved alongside this report. All hashes below were recomputed for this source revision.

```text
9d4893050f1d4d672448e9ce7ed6cb8ab6d483e261b2d79d8ed7156609d749db  UNUSED_RESONATOR_PROTOCOL.md
eb609a75d2b9777625c38c2498ee6dd678f7906244453baf1f3a37154947ea42  FROZEN_UNUSED_RESONATOR_PREDICTIONS.json
807c4558b91673f4b40c443cc2e70fdfac89af15ab941788c9cfbc3ee75bec58  unused_resonator_extract.py
72c17b6bc6bb867c0b4ff0d8fa40d4c7688892a8d38121e172d8ba101f672b9b  unused_resonator_observations.json
4922587f042c098fb4817ef056cb81329877253b5c8ddb2e41e5ce03f9880d42  unused_resonator_full.json
812505ed51d8a4ae705ab8b438e61291c36d9030eb67e3e30e4a8b2929282030  extract_resonator_ridge.py
ba85c89b104d8a7de8fb9091b1a7a14f42999cacbd245b4db102f8a4f4928318  resonator_ridge.json
ee1e9b4cb7322d2fba09427db72c17a6c53e3b1f5fbb8cccdad387e0ca1ffb5f  resonator_maps.npz
68abbfae73aec3b91ccd6e140cc48cc3cd62e951624efd30283796c9bcd8a303  source-figure3.xlsx
3188cecd56cc3eb95763fae4a104c97f346b3c66fcb11921e7afd63e71a4cc36  published-figure3-source.png
52b46e0e66beb99522bee9690a29352964260ba3931f69cf2a9d53f3cdc78b76  published-figure3-page.html
ec60ebb9c6f586c7bc2c9a0be0548d17d6e20e0fdc31ac81e275b91d426237f8  independent_unused_resonator_source_check.py
3a82f5c6418b6347df97f0c425f839bbd7cf960f0457cd45b3a1b51bccbec3cb  independent_unused_resonator_source_results.json
28fe3ec1454a4d7f33928fbb80a80d2c4a7b6fc5bb69eef71f9bad62855f0ab8  independent_unused_resonator_source_check.log
3faaaa8eee3418964b5ea72072dbc2609c1e45f5da33965749f2185bdbffb221  unused_resonator_source_identity_check.json
48cdc6b7065d603e5748c4124d4be7e4a1ba0f422997a0c58981f958e8007579  unused_resonator_raw_slices_review.png
92fb7e6b0c52893c796189386ad96d0b7ec24f9783cbe7cdf5d5a0fc68b7852c  unused_resonator_local_maps_review.png
```
