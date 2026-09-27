# Raw full-f03 extraction review

2026-09-27. Complete static read of RAW03_PROTOCOL.md, raw03_center.py and RAW03_INPUTS.json; inspected all three completed returns and raw axes. Independent reconstruction of every saved trace from stored nonlinear parameters and linear coefficients reproduces the reported costs to6e−14 and RMS values to3e−17 in stored units. No optimizer, target comparison or prediction-dependent selection performed.

All three runtime manifest hashes match. The code is the previously reviewed raw02 nonnegative variable-projection model with the following intended changes:120 bins instead of60; exact July29 173536 raw acquisition;1MHz spacing over119MHz span; initial widths1,3,6MHz; width bounds.25–30MHz; initial half-separation14.875MHz=span/8 and upper half-separation59.5MHz=span/2. Center begins at the raw-grid midpoint and remains within its bounds. No Hamiltonian prediction, processed03 center or calibration parameter is read or changed.

The source x0 axis is frequency in Hz,14.600348279882–14.719348279882GHz. It is the full-f03 drive axis: no division by3 or other multiphoton factor is implemented or appropriate for this archived axis. x1 is gate voltage; y0 is the stored scalar S21 channel labeled W/W with phase separately stored in y1. As in the prior review, that metadata establishes the archived scalar channel, not an independently calibrated complex response or an unambiguous driver amplitude-versus-power convention. Grouping gates and explicitly sorting/asserting the same frequency grid avoids reshape orientation assumptions and retains all31×120=3720 points.

The reduced-QR background projection plus two-variable NNLS and background recovery are algebraically the correct least-squares profile over unconstrained affine backgrounds and nonnegative peak amplitudes. Scaling by one global data standard deviation preserves the optimum but is not a noise model. Center, widths and half-separations are inMHz internally; output center is restored toHz. Lorentzian width is HWHM, not FWHM.

All starts returned success. Centers are14,667,708,320.327–14,667,708,323.506Hz, with HWHM≈3.004164–3.004165MHz. No saved excess amplitude is negative, no nonlinear coordinate is marked active at a bound, and the largest full-design condition number is≈861.78. Reported optimality remains.0347–.0399 despite the nominal gtol1e−8; successful termination therefore does not establish tight stationarity. The approximately3.18Hz center span is agreement among starts under this one fit family, not experimental precision or uncertainty coverage.

The shared center, symmetric branch positions, common linewidth, Lorentzian scalar-response form, per-gate affine backgrounds and equal point weighting are assumptions. This control does not explore asymmetric lines, saturation/power shifts, gate/time drift, channel covariance, varying linewidths or background curvature. Conditional sub-bin localization is mathematically possible;1MHz sampling neither forbids it nor certifies the fit's systematic accuracy. No covariance, likelihood interval or precision agreement claim follows. The runner still lacks per-start exception handling, but all three current returns completed; that inherited limitation does not remove any result here.

No extraction indexing/unit/profiling defect was found. Keep this measured-only retrospective reanalysis distinct from both the processed source fit and microscopic predictions; preserve all outcomes without picking the center closest to either.

## Source-support clarification, 2026-09-27

The earlier phrase “historical bottom-sweet-spot descriptions” understates direct paper support for the intended operating point. Krause2024 local arXiv text lines304–314 explicitly says Figure2(b,c) f01/f02/f03 and their dispersions were measured at the bottom flux sweet spot; the gate-scan examples in Figure2(d–f) are at Bparallel=.15T. This supports the intended bottom-sweet-spot preparation used by the proposed model. It does not independently determine an exact loop phase psi=pi, a calibrated phase error bound, or its stability throughout each specific archived acquisition. Keep the distinction between source-supported intended setting and exact mathematical phase assumption, rather than treating the intended setting as unsupported. Source text SHA-256 `7b4d9318649b159eb37bb7c55b42c18f0309ee8bd9aa98a2da273ac785f2916f`; PDF identity remains `538f4b4dc70a2d7879e33b91b9d420c604dc64fe490f97103d2c1ea5e3c63ad6`. No frozen protocol, model or inputs were changed.

The same clarification was appended to ../koeln-microscopic-transfer/SOURCE_MODEL_REVIEW.md; only review prose changed.

## SHA-256 identities

| File | SHA-256 |
|---|---|
| RAW03_PROTOCOL.md | 272b7a31b00944d8a8c1d20262d7d491720ccc42f446716edc3e3911c9e099a4 |
| raw03_center.py | 4e4eb266337fe1973b7d6eede4e9b8c46e099be93d13763fa376209109b1cf43 |
| RAW03_INPUTS.json | 3eb1c64c9c2460e053e6c1294ec5b7e1694d6da4ace5e2136bce866ac123638f |
| raw03_results.json | 1437878340418c6d03f062acaa58ac6d3ef14b0fc42922a55468dd5cb49d42df |

Raw dataset SHA-256: `e53727072e8689c63332eebd8094888f6ee4d6ea9d66281f5f7efc56db0bf7cf`. Exact acquisition path is in RAW03_INPUTS.json.
