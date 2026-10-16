# Independent M10 spectral, exact-cell and tracking calculation, v1

All computations below were completed and frozen before opening either M10 author source or its output ledgers. Inputs remain exposed development. Root supplied the prospective candidates and the anticipated 600/1200 selection and possible 54 nonzero-slip occurrences; these are disclosed prior information, not blind predictions. No physical sky-phase calibration or independent empirical gravity test is established.

## Independent implementation and scope

I reused my immutable M9 corrected-I/Q arrays and complete header ledgers, originally extracted with a separate struct/integer reader from the two pinned raw products. I did not treat the author's canonical decoder as independent input. I re-extracted ODF and ATDF with the separate M8 binary-character slicing method, importing no author decoder. All current code and 20 input identities were frozen in PRECOMPUTE_FREEZE_v1.json before execution; source SHA256 is c7d6b1cdb11282659a7dd05b9703d33a1189fb58293c3a02d4d63a2f7c30e7d5.

Every one-second block in [48900,49500) is retained: 600 X and 600 Ka blocks, each 1000 corrected complex samples. Header quality, metadata and integer sample identities are preserved through the frozen M9 chain. No new sample products, network access, clipping or fit offsets are used.

The spectral implementation differs from the author's prospective method: a 32768-bin complete FFT grid followed by direct-correlation derivative/Hessian safeguarded Newton refinement, rather than 16000 bins and bounded scalar minimization. With centered sample times t_n=(n-499.5)/1000, C=sum z_n exp(-2pi i f t_n), the unconstrained complex amplitude projection gives residual S-|C|^2/N. The exact differentiation identities implemented are g=2 Re(C' conjugate C) and h=2 Re(C'' conjugate C)+2|C'|^2. Seven separately specified positive, negative, zero and near-Nyquist synthetic tones recover their frequencies within 1e-8 Hz. Every observed block has a bracketed local maximum and negative curvature. Maximum final Newton displacement is 9.93e-12 Hz. This is numerical stationarity, not a certified exact global maximum or physical frequency precision. Frequency comparison tolerance was fixed at 2e-5 Hz and relative correlation-power tolerance at 5e-10 before reading author estimates.

X estimated frequencies span [-0.684358875408293,1.5303082973387632] Hz; Ka spans [-2.4514643055984493,3.7629900153316385] Hz. Both bands retain all 600 zero hardware-error/FROV headers. Numerical values are the local single-tone approximations, not identified physical phase slopes.

## Exact integer amplitude-cell certificates

For corrected integer center z_n with radius r_n, any constant-amplitude waveform A exp(i theta_n) has squared residual at least sum(r_n-A)^2. Minimizing A>=0 yields S-(sum r_n)^2/N. With C=sum ceil(sqrt(x_n^2+y_n^2)), C>=sum r_n, so NS-C^2>2N^2 exactly rules out such a waveform inside independent ideal component half-width-one cells. The 2N allowance is the largest total squared distance of a point in those rectangles. All quantities in this certificate are exact integers using isqrt.

The independent second certificate uses each rectangle's squared-radius interval: [(max(|x|-1,0))^2+(max(|y|-1,0))^2,(|x|+1)^2+(|y|+1)^2]. A common amplitude requires max lower <= min upper. Strict separation excludes it without any spectral optimization.

Both certificates reject all 1200 blocks. The smallest NS-C^2-2N^2 margin is 19199220350064; the smallest max-lower-minus-min-upper margin is 1003364704 in squared corrected-code units. No selected center is an extreme component or an origin-touching cell. These conclusions assume the ideal unsaturated independent rectangular analog preimage. They exclude the quantization-only constant-amplitude candidate, including a pure single tone; they do not exclude a useful approximate coherent carrier estimator, bound physical noise from above, or identify a scalar signal.

## Conditional count/reference reconstruction

The independently decoded selection contains exactly 600 ODF type13 records, rx25 tx54 with X downlink, and 601 ATDF endpoint records. All 600 intervals have unique matching endpoints, duration one second and complete RSR coverage. No record is removed. Stored S-exciter reference is exactly 2117064000 Hz throughout; the supplied band conversion gives 1863016320000/221 Hz. Every used endpoint has Block5 code5, bias1000 kHz, level1 and synthesizer flag1. These are decoded metadata, not proof of physical calibration.

For the supplied pre-NSP model N=Fref(t-t0)-Phi_rx+C4(t-t0), subtraction gives mean received sky=Fref-(DeltaN/T-C4). With the conditional historical normalization Fref=(11/3)(240/221)Fstored, this is (880/221)Fstored-(DeltaN/T-1e6). I retained raw count differences as well as the forward modulo-2^32 representative and its integer-history difference. In this selected window every raw difference is already positive and every history integer is zero; no rollover adjustment was applied. The no-reset/history premise is still not derived from endpoint values. The largest exact difference between DeltaN/T-1e6 and ODF D is 439/1000000000 Hz, a format consistency observation rather than a physical error certificate.

There are 54 nonzero-slip endpoint occurrences across the 600 intervals, arising from 27 distinct raw endpoints and affecting 39 distinct intervals. Item87 values on the 601 unique endpoints are 0 on574 records, 1 on11, 2 on15 and 5 on1. Quality/lock items19 and24 are zero on all601. All slip records and their actual values are retained. The label diagnostic is not assumed to measure a physical phase-error magnitude.

## Four retained RSR candidates

For each matched X block, I form LO and the archived cubic phase increment exactly as rational values before subtracting the GHz-scale reference. For shift delta, the phase increment is P2+P3(1+2delta)+P4(1+3delta+3delta^2). The four candidates use mean RSR sky = LO - increment + sign*f_fit with sign +/-1 and delta=0 or1/2000. The fit slope is only conditionally identified with a true mean phase derivative over [s,s+1]; samples end at s+.999. No sign, offset, time shift or scale is fitted or selected.

Errors to the ODF-derived sky, in Hz:

| NCO shift | Sign | Minimum | Median | Maximum | RMS |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | -1 | -3.127846185254607 | -0.5816937105114366 | 1.4524133078531265 | 0.8204176983166233 |
| 0 | +1 | -0.21701022999238728 | 0.00006967871800716077 | 0.3113512494365276 | 0.06642541961013664 |
| 1/2000 | -1 | -3.1280055361357064 | -0.5818457569613362 | 1.4522583915585516 | 0.8205278079393301 |
| 1/2000 | +1 | -0.21716528027772664 | -0.0000821059487694873 | 0.3111964986058772 | 0.06642635411800965 |

This exposed-data contrast can motivate a calibrated convention but is not independent validation of it. The two positive-sign timing candidates remain close; no physical timing precision follows. Ka has no matched closed-loop downlink here and is not calibrated by the X comparison. Full exact per-row terms, flags and both ATDF/ODF candidates are retained in REFERENCE_ROWS_v1.jsonl.

## Execution and preservation

One independent execution completed with exit0 in 4.417394250165671 wall seconds (4.345164500176907 recorded internal seconds), empty stderr, with no failed attempt or adjusted threshold. Results SHA256 is f7334c6e87f2d487db767e23d41ee59d83bc0dde21aa8796a79f6c31d0c43b62; spectral ledger is 95283ddf38d38f209d9ec2455e00e9e47c0dba507a54d2a39ec592d91d7ae562; reference ledger is 498976ce618f4302bf2e1d558dc61af7820490537ec83017c142d346183ba6df. The separate identity manifest binds all original outputs before post-exposure comparison. This original report will not be replaced with the author's results or later source identities.
