# Source-corrected Ramsey01 numerical review

2026-09-27. Full bounded code/manifest/source-membership and saved-residual reconstruction. No optimizer duplication,03 input, downstream transfer, or publication-branch modification. Earlier review bytes and267-sample results remain unchanged historical evidence. Their arithmetic checks do not validate interpreting the two tail reference points as Ramsey evolution.

## Source-semantic membership

Read RAW12_SOURCE_REVIEW.md and READOUT_REFERENCE_CERTIFICATE.json completely, then independently inspected exact074423 raw and processed HDF5. All manifest hashes match. Processed bias_gate/x0 match the independently sorted raw axes. Its final two pop_exc entries are0 and1 across all31 gates, within2.22e−16. The two omitted indices are265/266 (zero-based), with stored x0 values19.915 and19.990µs. Their exact raw I/Q arrays and times match the separate excluded_reference_IQ/excluded_reference_times_s fields saved by the corrected fitter.

The retained indices0…264 span40ns…19.840µs, with75ns spacing, for all31 gates. There are31×265×2=16,430 real residual coordinates. This exclusion is tied to source-calibration semantics, not residual size. The processed-population test verifies these exact reference identifications; it does not reconstruct the executed pulse schedule or establish that every remaining signal is described adequately by the proposed model. The raw12 qutrit correction remains a separate source-review result; no raw12 fitting was performed here.

The complete diff from the prior fitter changes only sample membership, reference preservation and resulting residual/sparsity dimensions. Normalization is recomputed from the265-delay I/Q array. The reference and artificial detuning, model, bounds, three starts, optimizer options, local decay coordinates and linear projection remain unchanged. The frozen processed source is hash-checked by the author runner even though the mask itself is implemented positionally; this review independently verifies that positional mask against processed populations. A changed acquisition cannot safely reuse it merely because it has267 samples.

## Residual reconstruction and numerical results

An independent script directly regroups raw axes, verifies the source reference populations, removes exactly those reference indices and reconstructs every residual from saved66 nonlinear parameters and310 linear coefficients per fit. Hz/seconds complex exponentials independently implement recorded oscillation=artificial+reference−transition, where transition=reference+c±(fullsplitting/2)cos(2piV/period+phase). This confirms detuning signs,2pi and MHz/µs conversions. An independent reduced-QR projection checks the saved least-squares coefficients.

All three saved outcomes have16,430 reconstructed coordinates. Maximum cost discrepancy is2.38e−12; maximum relative normal-equation defect is1.19e−12; saved-versus-QR signal discrepancy is below1.71e−7 raw units; per-gate RMS discrepancies are below1.25e−9 raw units. Complete normalized residual arrays and separate omitted reference arrays are preserved in the independent evidence. Source ordinates are labelledV but are reported here as stored raw units, without independent physical-voltage calibration.

| Initial period(V) | Center(Hz) | Full splitting(Hz) | Returned period(V) | Reconstructed cost | Raw RMS |
|---|---:|---:|---:|---:|---:|
| 0.15 | 5241116881.437193 | 61214.718132 | 0.135957384 | 2.306926268684 | 208.934905 |
| 0.22 | 5241114336.895615 | 111395.721445 | 0.215905660 | 1.818075658431 | 185.481295 |
| 0.3 | 5241114693.747121 | 111498.145973 | 0.213912404 | 1.817935314204 | 185.474135 |

The.15-start outcome is **not converged**: success=false, maximum150 evaluations exceeded, optimality.0057525. The.22 and.30 starts return by ftol, with optimalities.0012565 and.0018719, above gtol1e−6. Their maximum decay times are24.4134 and39.2138µs; the.15-start maximum is42.0552µs. Maximum returned design condition numbers are138.43,16.71 and11.98. These are saved local outcomes, not a proof of stationarity/global basin coverage or precision. The lower costs of the two longer-period starts support only preference within this corrected dataset and residual family; the.30-start cost is slightly lower than.22, with centers differing about357Hz. Do not compare normalized costs across the old267-point and new265-point datasets as though they were the same objective.

Each gate contributes530 contiguous residuals. All depend on four global coordinates, and exactly two local decay coordinates for that gate; the16,430×66 sparse pattern uses these blocks correctly. Linear profiling does not introduce cross-gate coupling. The free sine/cosine quadratures permit branch swap/phase ambiguity; no parity labeling or unique gate-period identification is established. Across declared bounds, modeled frequencies lie between.573 and2.573MHz, safely inside the positive real-channel Nyquist range0…6.6667MHz. This bounds the allowed parameterization; it does not exclude all physical alias-equivalent signals outside those bounds. Current saved oscillations span about1.517…1.629MHz.

Equal residual weighting divided by one global standard deviation is numerical scaling, not a likelihood/noise covariance. Stationary sinusoidal gate dependence, common center, two exponential decays and constant per-channel backgrounds remain phenomenological assumptions. Source-driven reference removal repairs a consequential membership error but does not establish preparation/readout adequacy, noise coverage, or a microscopic theory result. The publication remains outside this review.

## Evidence identities

Independent script: independent_residual_check.py. Results: independent_residual_results.json, independent_residual_arrays.npz and independent_residual_check.log. All paths below are current frozen evidence; no previous review was rewritten. SHA-256:

- `PROTOCOL.md`: `71fa78849efe65501aa4351a7a81b566b80129b3731ce845a7645c7b1dff12f9`
- `INPUTS.json`: `9d3b4e03ddd9244ac4911d26c0118f3e000fc7c82d89418f2f814a16583fd786`
- `fit_raw.py`: `2450278c9fc2867432d1393ff3e1e69180965571558ef1e98433ec84c6e356ee`
- `fits.json`: `68fea0a2fd98d9e6d783082f32f629a8b9be62b3269f27ab14312c38df6eb823`
- `independent_residual_check.py`: `14c59f10181d4f4f07ee59fe1e59ca12fa8d8807e2264b139313e167d85c4ea2`
- `independent_residual_arrays.npz`: `b998a72e1aed34fe9681df3351b69411d8b227d69d444738a62bcd85624f0fe7`
- `../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-074423-596-6dd5d0-Ramsey oscillation 01 vs Gate at 5.2411 GHz/dataset.hdf5`: `b48d9620e77a4eb0d47550ea405531908ca9514525c022df6d99ebba4c31e6cc`
- `independent_residual_results.json`: `d0f19b56b6989969512c956d1402be92b940f0d91e2e26fcb1dd56ffd9437465`
- `independent_residual_check.log`: `5be54c0160ebe2ef407996cb089a619179eaddb35001bfc1f7e723a93067de98`
- `../koeln-microscopic-transfer/RAW12_SOURCE_REVIEW.md`: `1776fcb8f9724dce27a7fa1eec64fd14865d38a75c8ba929770572d7751609d4`
- `../koeln-microscopic-transfer/READOUT_REFERENCE_CERTIFICATE.json`: `bc93aba8dcea9b61aef1e44b9bc5a95fcfc412e5bd7f17e7f7f202c1d8487356`
- `../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-074423-596-6dd5d0-Ramsey oscillation 01 vs Gate at 5.2411 GHz/analysis_BeatingRamseyGateScanAnalysis/dataset_processed.hdf5`: `1ad5632d8e8e26719da7271c3ced4cc7fbc5567220fa2400e10e2774525f0174`
