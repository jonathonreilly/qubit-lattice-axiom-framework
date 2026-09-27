# Preparation-transfer source eligibility

2026-09-27. Metadata-only target review. Read rawHDF5 axes/attributes, both snapshots and relevant archive notebook source. **No target I/Q/population array or target fitted-parameter/QOI file was read.** Notebook source contains historical fixed relaxation constants; these were not adopted, fitted or used to inspect target agreement. No fit or prediction/evaluation was performed.

## Conditional eligibility

The exact sources support a prospective-within-this-workflow population-transfer diagnostic from T1 preparation to Ramsey preparation, with important stationarity/preparation conditions. They do not establish equal physical rates across the two acquisitions. A declared shared-rate prediction may proceed from calibration only. Exact applied-gate matching also permits a separately declared per-gate calibration alternative, without nearest-row choice or target-dependent selection. Preparation fidelity, charge drift, readout linearity and rate stability remain empirical premises; discrepancy would not be a no-go result.

Calibration is `20220920-215202-730-31ad1f`, named T1 12 vs Gate. Evaluation is `20220921-083404-829-b243a3`, named Ramsey oscillation12 vs Gate. Start-to-start gap is10h42m02s. This is a genuine change of acquisition/preparation, not a held-out portion of one trace; it is also a substantial interval for source-documented charge drift.

## Membership, axes and notebook identity

Calibration has61 applied gates−.12…+.12V in.004V steps and200 stored time samples. x0 runs.1…79.7µs in.4µs steps. The x0 long_name is “echo wait time,” a generic/stale label; exact experiment name and matching notebook identification support T1 interpretation, not a reason to treat it as an echo acquisition.

`fig_S5_T1_Echo_vs_Gate.ipynb` zero-based cell17 explicitly selects this exact215202 TUID. Cell22 defines final reference indices−3,−2,−1 as0/1/2 and independently inverts their affine I/Q centroid matrix. Cell23 defines T1 delays as x0[:-3]. Therefore calibration fitting should use197 genuine delays. Preserve stored reference indices197–199 at78.9,79.3,79.7µs separately; retained delays end78.5µs. This is direct source-producer evidence, not deduction from a uniform grid or residual shape. The source paper SupplementaryIII describes relaxation after preparing|2>; ideal pure|2> remains a conditional preparation rather than measured unit fidelity.

Target has31 gates−.12…+.12V in.008V steps and383 stored time samples80ns…1.990µs in5ns steps. `fig_10_Ramsey_gatescan.ipynb` cell12 selects the exact083404 TUID; cell17 and plotting cells use x0/population arrays[:-3]. Thus predeclare380 target delay samples80ns…1.975µs and exclude/preserve final indices380–382 at1.980,1.985,1.990µs as reference records. The processed population-tail identity must be checked after prediction freezing and authorized target access; it was not inspected here. This notebook is appropriate for this September target, unlike the earlier July29 task where reusing its input constants would have mixed acquisitions.

Raw y0/y1 are I/Q, metadata unitsV. Neither their physical scaling nor statistical noise is established by metadata. Exact numeric gate comparison yields calibration_gates[::2] == target_gates with zero floating-point difference for all31 positions. Use that declared index mapping if per-gate transfer is pursued. Equal applied voltage does not prove equal offset charge across10hours.

## Settings and preparation scope

Both snapshots report aligned field components Bparallel=.14999948193938975T and Bperp=.0004813279471407693T exactly equal as recorded. These are snapshot settings/readbacks, not a continuous field-stability measurement. Both report readout frequency7.547298690445051GHz, amplitude.1664351851851852 andduration600ns. Both have q0 microwave duration20ns andqt0 duration80ns. These shared settings aid comparability but do not certify executed pulses or reference-state purity.

Controls changed between acquisitions: q0.freq_01 from5.249095464352618 to5.2489439428039465GHz; q0.freq_12 from4.919770481180519 to4.918388613051287GHz; mw_amp180 from.45828129905 to.46281985709; mw_ef_amp180 from.52838295278 to.54121548020; init_duration from79.04 to100.56µs. Treat those as evidence of recalibration/different preparation settings, not a measured drift correction. Do not infer that unchanged field alone guarantees unchanged relaxation rates or equal superposition.

The canonical within12 final unitary preserves p1+p2 for **any** rotation angle, since it acts inside that subspace; unlike contrast cancellation, idealpi/2 accuracy is not needed for this sum. However, preparation into equal12 populations is still an input assumption, and relaxation/leakage during a finite final pulse, coupling to|0>, readout errors or upward rates can change the proposed observation relation. Coherence detuning and dephasing do not enter Pexc during ideal free downward-rate evolution, so source Ramsey frequencies need not enter this test at all.

The notebook's fixed relaxation constants and its collapse-operator convention are not independent calibration data. Fit canonical nonnegative rates directly to the allowed T1 population curves; do not import those constants or silently translate their T1 names into1/k without checking prefactors. In the ideal|2> calibration u2=exp(−lambda2*t), u1=k21*(exp(−k10*t)−exp(−lambda2*t))/(lambda2−k10), with the continuous degenerate limitk21*t*exp(−k10*t). The later equal12 prediction follows the separately derived formula, not target fitting.

## Conditions before evaluation

Freeze the source-semantic masks, raw-to-population calibration convention, shared/per-gate alternative definitions, all fit outcomes and predicted target arrays before opening target amplitudes. Preserve unsuccessful or boundary fits; ensure sufficient T1 identification rather than assuming it. After release verify target reference membership/centroid conditioning without clipping, and report all residuals with cross-acquisition/reference covariance and preparation limitations. Target agreement must not determine rates, initial populations, offsets, gate mapping or model choice.

## Identities

| Evidence | SHA-256 |
|---|---|
|PROTOCOL.md|266dd151a66f6ff32e68cc7e27a7945b33243383b208d2f01cf87f10f09e0c2a|
|SOURCE_IDENTITIES.json|891747e3ae3a2184efbdab5e1f309428bb305072dfe863ebe58e9272545ec324|
|source/Krause2024_Quasiparticle/Data/quantify_datasets/20220920/20220920-215202-730-31ad1f-T1 12 vs Gate q0 at 4.9198 GHz/snapshot.json|dda1691c7f2b598ff0ab5b5b8a912590b59b5550c2d554a3d1722fe47a828081|
|source/Krause2024_Quasiparticle/Data/quantify_datasets/20220921/20220921-083404-829-b243a3-Ramsey oscillation 12 vs Gate at 4.9184 GHz/snapshot.json|2bfe78e492edc5966074cc034fa24dbcb7293603d4b4d6151f3e65014396862b|
|source/Krause2024_Quasiparticle/Data/quantify_datasets/20220920/20220920-215202-730-31ad1f-T1 12 vs Gate q0 at 4.9198 GHz/dataset.hdf5|1bab2b3255ef0b9719216d959e0a630cb7b2a3406c5f544853aa4b24829a80ba|
|source/Krause2024_Quasiparticle/Data/quantify_datasets/20220921/20220921-083404-829-b243a3-Ramsey oscillation 12 vs Gate at 4.9184 GHz/dataset.hdf5|302ee56a0070368e88a750a3bd7f2b2e52d73d22426020cfeabbd3c1af8fb198|

Notebook source SHA-256: Fig.S5 `6ae168fc07de2ab4181538bf4f6a55e9193048dc123dd5029850a0542327e42e`; Fig.10 `747024bfdf0c0cac346d26bb3b82e3cc33cb37e96c95c7d5c41a2807b5393b56`. No source code executed.
