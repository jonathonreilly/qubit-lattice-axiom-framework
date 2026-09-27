# Echo source and timing eligibility

**Eligible for the stated conditional, ideal-pulse prediction.** In the exact-TUID archived analysis convention, x0 is the **total** evolution time; the midpoint swap lies between two intervals of x0/2. This conclusion is from source semantics, without Echo signal or fit inspection. It is not verification of the executed hardware schedule. No alternative timing should be chosen by target agreement.

Only raw HDF x0/x1 values, dataset/variable attributes, snapshots, paper text and notebook source code were inspected. Echo y0/y1 values, processed populations, quantities-of-interest contents, notebook outputs and fitted parameters remain unopened. `inspect_source_metadata.py`, `source_metadata_evidence.json` and `notebook_sequence_evidence.txt` preserve bounded evidence; no supplied code was executed.

## Exact sequence and membership evidence

The archive's `Jupyter_notebooks/fig_S5_T1_Echo_vs_Gate.ipynb`, cell17, selects exact Echo `20220920-210206-915-8331be` and calibration `20220920-215202-730-31ad1f`. Cell18 loads the Echo QutritBeatingRamseyGateScanAnalysis. Cell29 supplies `dataset_echo_vs_gate.x0.to_numpy()[:-3]` directly as the model's delay, with no factor of two. Cell7 converts seconds to microseconds once and evolves an equal-1/2 state for `0.5*echo_time`, applies the explicit 1↔2 permutation matrix, and evolves another `0.5*echo_time`, before a final within12 rotation. A nearby comment calling the middle operation a pi/2 is inconsistent with the actual permutation matrix; the matrix is an ideal pi swap. The source implementation, not that comment, fixes this conditional construction.

Krause2024.txt (local arXiv2403.03351v1 text), lines3509–3524, identifies Fig S5(c,d) as an Echo experiment initialized in a 1/2 superposition and describes the wait-dependent phase in the final pi/2. Phase does not affect the total excited population for a unitary confined to 1/2. The notebook is the exact figure/analysis producer, not an acquisition schedule implementation. Its initial state and swap establish the intended model; actual pulse execution/fidelity, finite-pulse losses and initial equal populations remain assumptions. Its fitted relaxation/dephasing constants were not imported. In particular, its sqrt(2/T1) collapse convention is not used to reinterpret our separately calibrated rates.

The raw dataset identifies x0 as tau, long_name “echo wait time”, unit seconds. This label alone is insufficient to settle total versus half wait; the direct cell29→cell7 chain settles the archived modeling convention. There are 249 stored times at 40 ns spacing and 61 gate values. The genuine data mask is indices0…245: 246 times from80 ns through9.88 µs. The last three indices246,247,248 have x0 values9.92,9.96,10.00 µs and are omitted by the exact Echo producer from all delay fits/plots. These labels are reference slots, not long-delay observations.

State order 0,1,2 for the three reference slots follows the shared three-reference analysis convention, explicitly used for calibration in this same notebook. Because Echo processed population arrays are withheld, their exact tail basis populations have **not yet been numerically verified**. After prediction freeze and access release, verify Echo processed tails and raw affine reconstruction before claiming an observed comparison. This condition is recorded in JSON; no hidden target-array inspection was used to close it prematurely.

## Conditions relative to the frozen-rate calibration

Echo occurred **49 min55.815 s before** the selected T1 acquisition (timestamps include milliseconds). This is not a forward-time physical forecast, even when computational predictions precede Echo amplitude inspection. Paper wording about a “preceding” relaxation experiment does not override these exact timestamps.

All 61 gate values exactly match the calibration grid, −.12…+.12 V in .004 V steps. Reviewed snapshot settings agree exactly: field-vector setpoint [−.0002761604359053202,.15,0] T; f01=5.249095464352618 GHz, f12=4.919770481180519 GHz; mw_amp180=.45828129905010423, mw_ef_amp180=.5283829527841791; 01 duration20 ns, 12 cached duration80 ns; initialization79.04 µs; readout7.547298690445051 GHz, amplitude .1664351851851852, duration600 ns. Snapshot equality is not a continuous field trace, execution log or evidence that rates/charge offsets remain fixed. Cached pulse durations do not establish whether x0 excludes every finite-pulse segment; do not introduce a numerical timing correction from them.

With those declared assumptions, the admissible population construction is E(x0/2) S12 E(x0/2) applied to [0,.5,.5], where E(t)=exp(Lt), then sum components1+2. Its declared no-swap comparator is E(x0)[0,.5,.5]. The final within12 unitary preserves this sum irrespective of angle. Neither construction tests coherence: the same diagonal mixture suffices. Propagate every frozen rate return without target-dependent selection/refitting. No need to hold these explicitly conditional predictions for lack of an executed waveform; a claim of verified physical scheduling would need additional evidence.

## Identities

- Echo raw HDF: `345521167421f528acd7cb1922d235965eaca4c277d9cddba0886555871a67de`
- Echo snapshot: `8fa1f005f3c3790b41fbfa4fa52368f032bd49d1c6f89cd1bf761300009022f8`
- Calibration raw HDF: `1bab2b3255ef0b9719216d959e0a630cb7b2a3406c5f544853aa4b24829a80ba`
- Fig S5 notebook: `6ae168fc07de2ab4181538bf4f6a55e9193048dc123dd5029850a0542327e42e`
- Krause2024.txt: `7b4d9318649b159eb37bb7c55b42c18f0309ee8bd9aa98a2da273ac785f2916f`
- Source archive: `a8272b6cbe92ddc083d2a22b94bdb7743b19c50debbe89f4106baf817c69c574`
- Echo protocol: `310284303c2fbec736d2b0713e8115cbaeb550f68211b1e162cc006a54201eb0`

Machine-readable eligibility, masks, timing mapping and limits are in SOURCE_ELIGIBILITY.json. No Echo fit or population result is claimed.
