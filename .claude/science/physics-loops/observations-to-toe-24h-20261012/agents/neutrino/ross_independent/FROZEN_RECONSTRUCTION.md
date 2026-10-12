# Independent Ross estimator reconstruction protocol

Frozen after complete original second-stage source and first-stage/basis source reads, before this worker loads archived fit values or computes output estimates. Source EotWash/EP-Analysis-Sun commit 1e103b78b5c3f2d948a30da4f1e7301c6b6f83f5. The paper v1 summary (0.66 +/-0.61 fm/s^2) is known. No composition-agent numerical output has been viewed. While locating source paths, grep exposed comments about m alias, percentile convention and final-point decimation alignment in ross_response.py; the derivation below was checked against original source and MathWorks documentation, and does not claim blinding to those possible issues.

## Source-derived mapping

1. Select each first-stage array out using out(4)/thermalAmplitude <3.77. Treat out(2),out(3) as torque cosine/sine coefficients, since the first-stage source multiplies angle by torsion response with units N m. These cannot be independently recalibrated without raw TDMS and original first-stage state.
2. Detrend each retained run against uniform sample index, separately for cosine/sine. Apply the explicit flip sign schedule, tropical-year modulo/time shift, and joint strict 5th/95th percentile cuts.
3. Determine sampling rate from retained entries 4 and5; decimate archived Sun time/complex basis with the default IIR algorithm. Preserve endpoint alignment and expose filter order/roundoff choices. Apply all daylight-saving comparisons against the old time vector.
4. Set z=filtAt*exp(i*filtPhase)*P*(C+iS). In each accepted two-day block y=z-mean(z), x=inSun+i*outSun is a column. MATLAB apostrophe is conjugating, so a=(x^dagger x)^(-1)x^dagger conjugate(y). Its prediction is y=conjugate(a*x).
5. Report unweighted mean real(a), sample standard deviation/sqrt(number of blocks), plus quadrature. Source display divides by r*m. Track m exactly: initialized in kg, then overwritten by each min(abs(time_basis-time_data)) residual in days. Report dimensional incompatibility if reached. A second diagnostic retaining the declared physical mass is a counterfactual normalization, never a corrected publication.

## Fixed synthetic probes

- Exact block-only probe z=r*m_physical*A*conjugate(x), A=1e-15 m/s^2, tests response after only block centering. Analytic gain is x^dagger M x/(x^dagger x).
- Full second-stage amplitude injection: add r*m_physical*A*conjugate(x)/(filtAt*exp(i*filtPhase)*P) to each archived complex amplitude, with x sampled at its midpoint timestamp. Run per-run detrending, cuts, calibration, block centering and fits. Misfit arrays are held fixed: raw time-domain/first-stage injection is not established.
- First compute with selection/rate/basis/blocks fixed to nominal masks to measure the linear transfer. Also rerun the amplitude percentile selection for A= +/-1e-15 and report changes; do not silently call it a linear response. No uncertainty/significance claims from these injections.
- Compare the source-filter port against explicitly labeled order/endpoint/direct-basis alternatives to expose sensitivity. No port is certified MATLAB-identical without the actual executable/version/filter state.

## Decision

A source-computed estimator, a dimensionally valid map, response-corrected physical inference and published result are separate claims. Return exact equations, input/source hashes, port controls, injection gain, numerical reproduction status and the missing first-stage/MATLAB conditions. Do not publish an alternative experimental bound.
