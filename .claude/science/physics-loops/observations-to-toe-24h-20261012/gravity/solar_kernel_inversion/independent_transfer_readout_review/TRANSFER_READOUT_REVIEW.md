Focused independent completed-transfer readout check, 2026-10-12 UTC.

All 36 source/candidate/method score rows agree with independent arithmetic from the preserved forces and actual processed target arrays. All twelve candidate/source numerical gates pass when recomputed from those force arrays. No material arithmetic, source-identity, mask, aggregation or residual-direction discrepancy was found. Both candidates nevertheless fail the descriptive rectangles on this transfer: the original has 32 of 50 scored bins outside across five galaxies; the interior candidate has 30 of 50 across all six. The outside-bin sets are identical for base, refined and boundary results. This is a readout check of two fixed candidates, not a formal audit, refit, whole-family exclusion or next-route decision.

Exact snapshots of all requested sources, force receipts, results, frozen weights, input NPZs and supporting metadata are under `snapshots/`. The load-bearing identities are:

- Transfer protocol: `0bb46c333a089440082fe38ace469f2a35bea4c0e0c469c3abb022741e804265`.
- Transfer driver: `d29a6e9d6d6e00399eefaf28f4ef925ed1db650c01a63fa34bfd062914a771ab`.
- Freeze: `1dae3e3888f82c2ced9e07253dcf520bcf744e43e5a31c9e9849618703c90b1f`.
- Official result: `53580c9675a01dcf65cce1bdf4d69719b1dbbbc0e262a279c1e6d7ec6f85978f`.
- Parent readout checker: `0c574b645509b8f1efe041c251e7af41116a430bf4d15698a4b8fe7ba0e84198`.
- Parent readout: `4efbd49ef44b8000a393712671c4a4241d3a308672e39e713d76545eb2777aa0`.
- Baryonic forward NPZ: `217bd10ba3fa8f9972d047081342c023ee7524c16b6d8c685d6d9fa49fd2959f`.
- Processed target NPZ: `1e8f96f1198817fe962ecf43ceed6fb23be795f3c12ae246387a65cdc2dddfa6`.

All frozen identity-map entries match the current files and snapshots, including the operator, validator, six previous source receipts, fit receipt, margin receipt, selection and margin protocol. Both weight arrays exactly match their original optimization receipts and transfer freeze; no element is changed or dropped. E remains 1.4915242022774435e-10 m/s² in both fits. The source mass-to-light ratio remains 0.5605122519882025. All eighteen geometry-cache hashes match the stage receipts and metadata. The refined metadata doubles nr, nc and lmax while retaining the other base settings. The boundary metadata identifies the same base cache, and direct radius-array checks confirm exact preservation of interior nodes with doubled outer and halved inner limits. The expensive field projection was not rerun.

The fixed source order is NGC3949, NGC3972, UGC06667, UGC08837, DDO064, DDO168, identical to the earlier source selection and current freeze. The six full processed target arrays contain 58 rows; the unchanged source score masks select 50. The raw/scored counts are 7/6, 10/9, 9/7, 8/7, 14/12 and 10/9 respectively. Excluded raw indices are [0], [0], [0,1], [0], [0,1] and [0]. These are the already frozen masks, not new residual exclusions. All retained radii and velocities are finite and positive; processed errors are finite and nonnegative. Every reported radius, observed velocity and error equals the corresponding masked NPZ element. The complete arrays and zero-based raw/scored index mapping are retained in the independent calculation.

The recorded chronology is consistent with the required separation. The transfer freeze is 20:38:08Z. The original three-source numerical prerequisite receipt is 20:40:47Z and the margin field/rectangle prerequisite is 20:41:42Z, both before the first extension base receipt at 20:45:00Z. The final extension validation receipt is 22:04:36.102121Z, the official score receipt is 22:04:36.877329Z, and the parent readout starts at 22:05:21.042666Z. All base and validation receipts state target_arrays_read=false. Source inspection confirms their field stages do not load target arrays; hashing the target file for identity is distinct from opening its arrays for scoring. The official scorer requires all six validation receipts and carries numerical-pass flags even for diagnostic failures; it is not a universal hard block on every failed gate. In this actual run all gates pass, and the separate parent readout explicitly asserts that before opening targets. My independent script also verifies all twelve gates before opening the target snapshot.

For each source and candidate I recomputed positivity and max|g_refined/g_base-1| and max|g_boundary/g_base-1| directly, using exact binary-rational force ratios. The largest refinement change is 0.0024392553723256, for original D on DDO064, below 0.005. The largest boundary change is 2.2631440954601e-7, for original D on UGC06667, below 0.003. All method forces are finite and strictly positive. Base receipts also preserve Newtonian control discrepancies below 0.003 and prior-response discrepancies below 1e-10; those projection controls were read and source-bound, not rerun. The convergence gates establish the prescribed numerical stability comparisons, not certified continuum error bounds or observational agreement.

The native radial-force units are (km/s)²/kpc, consistent with the field's G=4.30091e-6 and its separate SI conversion ACC=1e6/(1000 parsec). Thus V_pred=sqrt(R g) is in km/s with the supplied kpc radius. Let q=R g/V_obs² and v_low=max(0,V_obs-2e), v_high=V_obs+2e. I independently used

    log10(V_pred/V_obs) = (1/2)log10(q),
    t_i=max[0, q-(v_high/V_obs)², (v_low/V_obs)²-q].

Force ratios and rectangle comparisons were computed exactly from the binary64 input values as rational numbers; logarithms and square roots used 70-digit arithmetic. This is a different arithmetic path from the parent's velocity-unit checker and imports no author helpers. The largest discrepancy from either existing readout was 2.85e-14 km/s in velocity, 9.1e-17 in a log residual, 5.6e-16 in t and 5.6e-17 in per-galaxy RMS. No bin classification changed. Positive t values remain positive; zero compatibility is not produced by rounding a violation down.

The aggregate is correctly sqrt[(1/6) sum_g (1/n_g) sum_i log10(V_pred/V_obs)²], giving each galaxy equal weight. It is not the average of galaxy RMS values and not a pooled-bin RMS. For example, the refined pooled-bin RMS values would be 0.1610949262 and 0.1351292600, different from the intended scores below. Aggregate t is the maximum bin allowance, not an average.

| Candidate | Method | Equal-galaxy RMS log10 velocity | Largest rectangle t | Outside bins |
| --- | --- | ---: | ---: | ---: |
| Original D | Base | 0.1641404246290445 | 0.6511634521929891 | 32/50 |
| Original D | Refined | 0.1641727922386680 | 0.6513721963795736 | 32/50 |
| Original D | Boundary | 0.1641404422886314 | 0.6511634723383567 | 32/50 |
| Interior D | Base | 0.1416354339212446 | 0.6114791521724803 | 30/50 |
| Interior D | Refined | 0.1416344692630286 | 0.6114844560112628 | 30/50 |
| Interior D | Boundary | 0.1416354484356075 | 0.6114791743554244 | 30/50 |

Per-source refined results are:

| Source | Scored bins | Original RMS | Original t | Interior RMS | Interior t |
| --- | ---: | ---: | ---: | ---: | ---: |
| NGC3949 | 6 | 0.04050624 | 0.16164559 | 0.04226246 | 0.20284708 |
| NGC3972 | 9 | 0.09777548 | 0.28020150 | 0.08089681 | 0.19990658 |
| UGC06667 | 7 | 0.33202728 | 0.65137220 | 0.30209212 | 0.61148446 |
| UGC08837 | 7 | 0.03976423 | 0 | 0.06535155 | 0.23968688 |
| DDO064 | 12 | 0.15351605 | 0.15874225 | 0.09337684 | 0.01854413 |
| DDO168 | 9 | 0.12298353 | 0.44017432 | 0.08821462 | 0.27099704 |

The exact outside-bin pattern below uses zero-based indices into each scored array, not raw target indices. It is unchanged across all three methods. U means below the lower rectangle edge; O means above the upper edge.

| Source | Original outside bins | Interior outside bins |
| --- | --- | --- |
| NGC3949 | O: 0,1 | O: 0,1 |
| NGC3972 | U: 0–8 | U: 0–8 |
| UGC06667 | U: 0–6 | U: 0–6 |
| UGC08837 | None | O: 2,3 |
| DDO064 | U: 4–9 | U: 4,5 |
| DDO168 | O: 0; U: 2–8 | O: 0,1; U: 3–8 |

Totals are 29 underpredicted and 3 overpredicted bins for the original; 24 underpredicted and 6 overpredicted for the interior. The original's sole galaxy wholly inside its rectangles is UGC08837. The interior has fewer failing bins overall but introduces two overpredicted bins in that galaxy. Its smaller aggregate RMS therefore does not mean broader whole-object rectangle compatibility.

“Worst residual” needs its criterion stated. For both candidates all three global extrema below lie in UGC06667, but at different radii. Using the refined forces:

- Largest rectangle allowance occurs at R=3.50 kpc, observed 69.3 km/s with e=3.0 and rectangle [63.3,75.3] km/s. Predictions are 29.642563 km/s (original) and 32.714554 km/s (interior), under by 39.657437 and 36.585446 km/s relative to the observation, with t=0.65137220 and 0.61148446.
- Largest absolute log residual occurs at R=2.61 kpc, observed 57.0 km/s. Predictions are 20.400563 and 22.111386 km/s; signed log10 residuals are -0.44623270 and -0.41125888.
- Largest absolute residual in km/s occurs at R=4.37 kpc, observed 77.3 km/s. Predictions are 34.041605 and 36.834115 km/s; signed residuals are -43.258395 and -40.465885 km/s.

The parent's `worst_bin` consistently means the largest rectangle t, and its indices and directions match the independent computation. It does not mean the largest absolute log or km/s residual. When all t values vanish, as for original UGC08837, argmax's first-bin tie is merely an inside-rectangle placeholder. The independent output preserves all three extrema explicitly.

The t statistic measures the extra acceleration allowance as a fraction of V_obs²/R needed to reach the descriptive rectangle. It is not a fractional velocity error, a sigma count or a likelihood ratio. The processed e values were used unchanged; this check neither recalibrates them nor propagates distance, inclination, source reconstruction, mass-to-light ratio or pressure-support uncertainty. The smallest reported nonzero object t, interior DDO064's approximately 0.01854413, remains a failure under the declared strict comparison rather than being called compatible.

Both response-fit receipts use only NGC2976, UGC07577 and KK98-251 operator inputs, disjoint from these six transfer objects, and their weights remain frozen. This supports the narrow “outside these response-weight fits” description. It does not establish blindness or universal independence from development: five transfer objects carry legacy train labels in the earlier source-selection file, NGC3972 carries a legacy test label, the global source parameter U comes from earlier calibration, and these objects were already exposed through previous response calculations. The protocol and readout correctly call this exposed out-of-fit development evidence. Solar and external constraints were inputs to the original fits and receive no new independent success from unchanged predictions here.

The practical conclusion is limited but clear: under the fixed source model, circular-speed readout, masks, response choices and descriptive errors, these two unchanged candidates do not satisfy all six extension rectangles. Numerical convergence success and observational rectangle failure are separate facts. This cannot by itself reject every response in the family, supply a nuisance likelihood, validate pressure corrections, or assess a relativistic completion. I make no next-route or primary scientific interpretation beyond those source-bound statements.

The independent calculation ran in about 1.1 seconds, used one numerical-library thread and peaked at 196.8 MB RSS. Exact evidence is in `independent_transfer_readout_checks_v1.json`, with fitting-role/prerequisite checks in `role_and_prerequisite_checks_v1.json` and all source hashes in the final receipt. Fifty-four source/input/receipt snapshots were saved; the large geometry caches were hash-verified in place. All original and snapshot identities remained unchanged through final checking. Only this review directory was written. No weights, source code, targets, expensive fields, active processes, Git state, PRs or formal audit state were changed.
