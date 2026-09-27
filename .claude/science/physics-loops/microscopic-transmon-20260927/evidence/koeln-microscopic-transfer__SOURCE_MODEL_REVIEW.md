# Conditional microscopic transfer: source/model review

2026-09-27. Complete static review of PROTOCOL.md, model.py, calibrate.py and INPUTS.json, using the existing source/AFM and energy-addition reviews and FIELD_HARMONIC_DERIVATION.md. All six frozen hashes match. No optimizer, model evaluation or03 target comparison was executed. This is a conditional construction/code check, not an audit verdict or empirical result.

## Implementation

The FFT normalization is consistent with Josephson first-harmonic energy units. If c_m is the real Fourier coefficient, the cosine amplitude is2c_m; dividing by−2c_1 makes the charge-basis first-neighbor hopping−1/2, hence potential−J cos(phi) for tau0. The normalized cosine harmonic ratio in the derivation is−2 times this code coefficient; the distinction is correct rather than a missing factor2. The constant Fourier term is replaced by the charging diagonal. That discards a parameter-dependent but charge-independent scalar potential offset, which cancels from transition frequencies and does not change eigenvectors.

The potential matrix uses real signed numpy.sinc(mB/Bphi)=sin(pi*mB/Bphi)/(pi*mB/Bphi), including negative lobes. No absolute-value envelope is introduced. Opposite charge displacements give conjugate exp(i*d*psi), preserving Hermiticity. At psi=pi the factor is(−1)^m: odd arm harmonics subtract and even ones add algebraically with their signed envelopes. This matches the spatial integration derivation within its uniform-junction premises. No division by the effective first harmonic is performed, so cancellation does not create a normalization singularity in the potential.

Charge n−q, complex eigenvectors and v†(n−q)v are consistent; the full cavity interaction G(a+a†)⊗charge retains counterrotating terms in photon-major ordering. Prediction uses the mean of charge endpoints0 and.5, and reports full absolute endpoint difference. Full f12 in the objective is mean f02 minus mean f01, with no factor2. Calibration frequencies/dispersion convert Hz→GHz; center residuals are MHz and the shape dispersion residual is log(predicted/observed), a chosen numerical weighting rather than chi-square.

## Geometry and source ledger

Rectangular AFM areas are65,792nm² (256×257) and25,454nm² (178×143). Their ratio is2.584741101595, giving alpha=(Ja−Jb)/(Ja+Jb)=.442079652807 under equal critical-current density and common local transparency. The code uses this alpha in Ja=Jsum(1+alpha)/2, Jb=Jsum(1−alpha)/2 correctly. AFM area is not direct tunneling-current metrology; uniform barrier/current density, common local transparency and equivalent electrical active area remain strong assumptions.

Prior source notebook evidence identifies the field-threaded widths as256nm and178nm, rather than257/143nm. Thus Bb=.8×256/178=1.150561797753T is the stated common-magnetic-thickness geometry transfer. Ba≈.8T comes from a conditionally assigned high-field cavity-modulation collapse, not an exact zero-error node measurement. This construction avoids the source's fitted smaller-arm node and joint-fit arm-energy ratio, but inherits uncertainty in effective thickness, focusing and interpretation of the collapse. Shared gap suppression at fixed field is absorbed in fitted Jsum; this is not a prediction of gap suppression.

NominalB=.15T is close to the July29 magnet components≈.14999887T. **Exact psi=pi is not established by the reviewed acquisition snapshots.** They give perpendicular field≈602.52–602.58µT, not an independently calibrated loop phase proving exact bottom sweet spot at those times. Historical bottom-sweet-spot descriptions do not supply that precise calibration. Keep psi=pi as an explicit hypothesis. Higher harmonics can also alter which point is the spectral minimum; calling it “bottom” is conditional on the usual regime, not a theorem for every allowed tau.

## Calibration separation and qualifications

Two source versions are retained: exact-TUID processed CSV01 and archived01 QOI, with the archived12 center shared. Shape fits use01 center,12 center andfull01 splitting; cosine fits only the two centers. Three free shape parameters for three observables and two cosine parameters for two observables leave no overidentifying calibration residual degrees of freedom. A small calibration residual is not validation or a confidence interval. The two versions are alternatives for the same acquisition, not independent replication. Their center/period/splitting disagreement and cross-acquisition charge drift remain material even if every numerical fit returns successfully.

Omega andG come only from the single cosine return in the source-corrected27-coordinate PNS calibration. This avoids importing its shape parameters, but carries an additional assumption: that these cosine-calibrated cavity parameters are suitable fixed values in this two-arm model at the July29 preparation/field. PNS acquisition-field correspondence and nuisance covariance are not independently closed by this transfer. Do not label them exact independent device constants or ignore their model dependence.

The code reads no03 observation or source fitted harmonic/arm coefficient. It predicts03 as an output only. It does enforce unique eigenstate assignment including03 during every calibration call, so an unused03 label failure can affect whether a start completes; this is not frequency-target fitting. Source-version choice, phase, geometry and nuisance values must not subsequently be selected by03 agreement. The protocol correctly states retrospective scope.

All eight normal returns or exceptions are appended independently; exceptions inside fitting/final forward evaluation are caught and preserved. Initialization uses only the supplied01 center plus assumedEC=.3, divided byalpha; it omits finite-field sinc correction, which is an initialization approximation rather than objective error. Parameter bounds and declared starts are implemented. Bound-clipped absolute Jacobian differences are valid secants but do not certify convergence. The output retains assignment weight and failures; it does not store Jacobian singular values, so identifiability requires a separate check.

At tau0, only the first harmonic survives. At fixed psi andfield, translating its phase gives a single cosine with effective magnitude|Ja*sinc(B/Ba)+Jb*sinc(B/Bb)*exp(i*psi)|. Charge coupling is unchanged by that translation. This is the correct theoretical implementation control, conditional on matching all other numerical settings. No actual numeric cosine-control comparison was performed here.

No sign/unit/normalization defect was found. Source support remains conditional for exact loop phase, equal current density/shared local transparency, node/geometry transfer, PNS nuisance transfer and endpoint-mean preparation. These premises must remain attached to any later result.

## SHA-256 identities

| File | SHA-256 |
|---|---|
| INPUTS.json | b80627a0662c143d033780ebb50c722f0badf801a10a5c103bc20f9371f7ddb3 |
| PROTOCOL.md | d5d6ffc5674ccd62e5468c29e9980a55dbcc74927120548d391ad3c82afce061 |
| calibrate.py | 4a995d96ef058109f142b20df18716c317ef17bf3d2693917c86eada1b53fd30 |
| model.py | d9db69aa06122958dc81120c1518ef2e3148a01dfd46a2f1820e0d593eac8cf3 |
| ../koeln-energy-addition/energy_prediction.json | aaaa330725b0a14dc41562444a4f0176d7463359c12427592b0d08d1d764fa5a |
| ../koeln-dispersion/pns_source_corrected_calibration.json | 8b3d274a05ece665523d8750e1e7644a7ae3d014e12ee537f0749440525aec9e |
| ../koeln-two-junction/source-data/df_ramsey_vs_gate_01_incl_disp_shift.csv | 0a6adbe7046485334e4c840e19d5b5b5225592b9bf663be957476d2353048c3f |
| ../koeln-two-junction/FIELD_HARMONIC_DERIVATION.md | f06a2a3ad9b6aa150ae8ee8a9ea9533561306e0129095ba2023d5816fa554e3c |
| ../koeln-two-junction/TWO_JUNCTION_SOURCE_REVIEW.md | d0f5c149f5c22a79a0020a877bad98415b89c300745f3fc411025a84b01e99c3 |
| ../koeln-energy-addition/SOURCE_REVIEW.md | fe51c052bb9cbeaf39f463e50c957584bba4950afbdd9e1f866b022e6b0ff50b |

## Source-support clarification, 2026-09-27

The earlier phrase “historical bottom-sweet-spot descriptions” understates direct paper support for the intended operating point. Krause2024 local arXiv text lines304–314 explicitly says Figure2(b,c) f01/f02/f03 and their dispersions were measured at the bottom flux sweet spot; the gate-scan examples in Figure2(d–f) are at Bparallel=.15T. This supports the intended bottom-sweet-spot preparation used by the proposed model. It does not independently determine an exact loop phase psi=pi, a calibrated phase error bound, or its stability throughout each specific archived acquisition. Keep the distinction between source-supported intended setting and exact mathematical phase assumption, rather than treating the intended setting as unsupported. Source text SHA-256 `7b4d9318649b159eb37bb7c55b42c18f0309ee8bd9aa98a2da273ac785f2916f`; PDF identity remains `538f4b4dc70a2d7879e33b91b9d420c604dc64fe490f97103d2c1ea5e3c63ad6`. No frozen protocol, model or inputs were changed.
