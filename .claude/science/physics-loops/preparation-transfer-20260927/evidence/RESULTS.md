# A working conditional population-prediction chain

We calibrated three downward transition rates using a separate experiment prepared in state |2>, froze predictions, then opened the Ramsey population data. No Ramsey population or frequency was fitted. All 11,780 Ramsey delay/gate observations are retained. The resulting population RMS residual is **1.6593 percentage points** and mean prediction-minus-observation is **+0.2748 points**. This is a concrete comparison with measured physics under supplied canonical dynamics, preparation and readout assumptions.

The chain is: raw three-reference I/Q readout → |2>-relaxation population calibration → nonnegative-rate evolution from equal populations in |1> and |2> → total population p1+p2 invariant under the final within12 rotation → separately acquired Ramsey population comparison. The calibration has61gates and197 genuine delays; evaluation has31gates and380 genuine delays. Final three stored samples in each acquisition are readout references, excluded as delay observations. Exact producer notebooks establish membership; actual reference fidelity and readout linearity remain assumptions.

The prediction covers diagonal populations only. An incoherent equal mixture gives the same result as an equal coherent superposition. Thus this tests a conditional three-state rate-equation transfer, also embedded in canonical Lindblad dynamics; it does not test coherence, distinguish quantum dynamics from that classical population model, or confirm native TOE physics. No native-theory decay-rate derivation is supplied.

The preparations are10h42m02s apart. Recorded fields and readout settings agree, but drive frequencies/amplitudes and initialization times changed. We assumed shared stationary rates, nominal ideal initial states, downward-only Markov dynamics and negligible preparation/final-pulse losses. These are explicit conditions, not measured equivalence. Source-provided frequency fits and notebook relaxation constants were not inputs.

Three full-model calibration starts all return ftol with no active bounds; all fail to reach the specified gradient tolerance. Rates are approximately[k10,k21,k20]=[.07126916,.11124121,.00839770]/µs. Full calibration RMS.03151155 is not a rate uncertainty. Local Jacobian condition~4.97 and close starts support local numerical stability, not global identification or confidence intervals. The target prediction arrays and code/input hashes were frozen before first target amplitude access. Matrix-exponential crosschecks are recorded; independent review is separate.

| Model | Calibration start | Target RMS (percentage points) | Mean residual (percentage points) |
|---|---|---:|---:|
| Three downward channels | [0.05, 0.1, 0.05] | 1.65931512 | 0.27478011 |
| Three downward channels | [0.2, 0.2, 0.2] | 1.65931512 | 0.27478014 |
| Three downward channels | [1, 0.1, 1] | 1.65931512 | 0.27478010 |
| Sequential-only control | [0.05, 0.1] | 1.67354035 | 0.35851367 |
| Sequential-only control | [0.2, 0.2] | 1.67354034 | 0.35851360 |
| Sequential-only control | [1, 0.1] | 1.67354033 | 0.35851357 |

The sequential-only model was a post hoc matched-calibration control: k20=0, the remaining two rates fitted only to the same independent calibration. All three predictions were frozen before comparison, with no target-dependent retuning. Its target RMS1.6735points is close to the full model's1.6593points. This test does not establish that direct2→0 decay is necessary. A fixed no-decay population1 has RMS5.1642points; this too is a descriptive post hoc control, not a significance test.

At the first/last Ramsey delay, the full prediction is .996810/.920138; the measured mean across gates is .992118/.916535. Largest individual absolute residual is7.1561percentage points. About4.5756% of reconstructed target population vectors and33.1447% of calibration vectors leave the physical simplex; none was clipped or removed. Calibration frequently approaches a population boundary, so this fraction alone is not a physical failure probability. Reference covariance, correlated delay/gate noise, preparation errors and cross-acquisition drift prevent a calibrated statistical-accuracy claim. Three-start numerical agreement must not be treated as an error bar.

Artifacts: PROTOCOL.md, SOURCE_ELIGIBILITY.md/json, SOURCE_IDENTITIES.json, calibrate_and_freeze.py, CALIBRATION_INPUTS.json, calibration_fits.json/readout.npz, FROZEN_TARGET_PREDICTIONS.json and PREDICTION_FREEZE.json, TARGET_ACCESS_RELEASE.json, evaluate_frozen.py, evaluation.json and target_observations.npz; sequential control files preserve all alternatives. Independent review and delivery disposition remain explicit separate records. Source archive DOI10.5281/zenodo.10728469, exact members and hashes recorded locally. No source data, primitive, audit status or other campaign was modified.

Figure: preparation_transfer.png/pdf (plot_transfer.py; visually inspected after layout correction). Pale curves show individual gate traces, not confidence bands. Only the lowest-calibration-cost full-model curve is visible; all three differ negligibly at this plotting scale, and all results remain in the table above. The figure does not display the nearly coincident sequential-control curve; its quantitative result is preserved here.
