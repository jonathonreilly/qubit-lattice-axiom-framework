# Receiver reference and RSR sign: focused primary-source check v1

The supplied metadata support the **conditional pre-NSP Block-5 X-band reconstruction**

\[
\overline f_{R,X}=\frac{880}{221}F_r-D_{\rm ODF}.
\]

Here `F_r` is the stored **level-1 S-exciter reference**, not the X-band transmitted frequency; `D_ODF` is the finite-count Doppler observable in Hz. There is no further factor of 96 or 11/3 in this branch. This conclusion uses the parent's supplied record classifications; I did not reread the binary records or compare a spectrum.

A newly located primary JPL paper explicitly documents positive `I+iQ` pseudo-residual phase for RSR processing. It corroborates a convention, rather than certifying the 2002 receiver/software configuration. The earlier source-bounded sign gap is therefore narrowed by new evidence; its immutable report is not overwritten.

## 1. Signed RSR frequency and its limits

Border and Paik, **Station Delay Calibration for Ranging Measurements**, IPN 42-177 (2009), §V, p. 10, write the baseband signal as

\[
I_n+iQ_n=V(t_n)e^{i\theta_{\rm pr}(t_n)}+\mathrm{noise},\qquad
\theta_{\rm pr}=\theta_{\rm actual}-\theta_{\rm predict}.
\]

They recover phase by multiplying by `exp(−i theta_local)` and adding predicted/local/remainder phases. They explicitly warn that SFDU phase-polynomial coefficients have the opposite signs from DSN phase predicts. Their §IV–V concerns Cassini ranging experiments in 2007–2008 at DSS-14, using RSR channels at 2 kHz, including carrier and ranging tones. These are instrument-method statements; no data from those experiments were analyzed here. The relevant equations on pp. 9–10 were visually checked.

For the declared transform convention

\[
Z(f)=\sum_n(I_n+iQ_n)e^{-2\pi i f t_n},
\]

a positive rotating tone peaks at positive `f`. Thus this published RSR convention identifies that signed frequency with actual minus predicted frequency. Combining it with original 0159-Science §2.6 and the two registered day-169 labels, columns 45–46, gives

\[
f_{\rm sky}(t)=10^6(L_{\rm RFIF}+L_{\rm DDC})-F_{\rm NCO}(t)+f_{\rm pr}(t)\quad\mathrm{Hz}.
\]

The LO fields are MHz; `F_NCO` and `f_pr` are Hz. Phase polynomials in the labels are cycles: convert to radians by `2*pi` before complex rotation. Positive frequency cannot be assigned from packed-word order alone. The two day-169 X and Ka labels have identical field descriptions and differ only in product/table identifiers. Applying the later published sign convention to the 2002 products remains an explicit instrument premise, not a sign selected by a fit or a certificate for software 2632.

## 2. NCO evaluation and sample times

Original 0159-Science (2001-02-28), §§2.4–2.5, printed pp. 2-7–2-8 / PDF pp. 17–18, specifies:

- phase polynomial `P(u)=P1+P2*u+P3*u^2+P4*u^3`, integrated from the frequency polynomial and continuous across seconds;
- **phase loaded at `u=m/1000`**, but **frequency evaluated at `u=(m+0.5)/1000`**, `m=0,...,999`, and loaded each millisecond;
- first-sample time from the SFDU year/day/seconds fields, with subsequent times incremented by the sample period; pipeline delays are designed to be compensated.

Within an ideal millisecond, exact phase loading plus held frequency would imply `P(m*Delta)+F((m+1/2)*Delta)*(t−m*Delta)`, plus accumulated turns, with `Delta=0.001 s`. That register-model interpolation is a stated inference, not an empirically verified oscillator implementation. The day-169 label columns 65–68 instead print the midpoint argument for **phase as well as frequency**. The 2009 paper does not settle this discrepancy or quantify register effects. Do not replace the original distinction silently with a generic continuous cubic, or regard a midpoint FFT frequency as automatically the same finite-count average.

The original specification's nominal 100 ns timing statement does not independently certify this track's error. ODF mid-count station-time tags and RSR ADC sample tags still need a declared common time/end-point mapping; no timing adjustment was estimated here.

## 3. Why the selected receiver-reference formula has this scale

Moyer (2000), §§13.2.1–13.2.4, printed pp. 13-10–13-17 / PDF pp. 427–434, distinguishes oscillator level 0, transmitter/exciter sky level 1, and direct Doppler-reference level 2. Equation (13-9) is

\[
f_{\rm REF}(t_3)=M_{2R}f_{T,R}(t_3).
\]

`M_2R` uses the receiving station's exciter/uplink band and the downlink band. Table 13-1 gives `880/221` for S exciter and X downlink. The factor 96 converts an S reference oscillator to sky level; it is inapplicable to level 1.

For pre-NSP Block 5, Eq. (13-35), printed p. 13-28 / PDF p. 445, has the constant fictitious reference

\[
N(t)=f_{\rm REF}(t-t_0)-\phi_R(t)+C_4(t-t_0),\qquad
\phi_R(t)=\int^t f_R(s)\,ds.
\]

Combining this with Eqs. (13-26) and (13-32) gives

\[
D=\Delta N/T-C_4=f_{\rm REF}-\Delta\phi_R/T.
\]

This algebra establishes the opening inversion for the selected branch. For the supplied positive bias `1000 kHz`, `C4=10^6 Hz`; the corresponding ATDF-count reconstruction is `mean f_R=f_REF+10^6−DeltaN/T`, conditional on those counts being the pre-NSP MDA quantity. No additional S-to-X factor multiplies `D` or `DeltaN/T` in these equations.

**Source correspondence:** TRK-2-18 Table 3-3b, printed pp. 3-5–3-6 / PDF pp. 17–18, separately identifies downlink band, transmitting uplink band, receiving exciter band, independent receiver/exciter flag, and reference frequency. The reference field is a 46-bit integer in mHz, split 22/24 bits: `F_r=(H*2^24+L)*10^-3 Hz`. For ramped non-one-way data its footnote identifies receiver frequency, rather than transmitted frequency. The day-169 ATDF label items 22 and 43–44 identify sky level and its frequency units; its split decimal reconstruction is instead `F_r=H*10^3+L*10^-6 Hz`. These two encodings must not be conflated.

The ATDF receiver type 5 denotes Block V (TRK-2-25 Table 3-3, printed p. 3-6 / PDF p. 14). Its simulation-synthesizer item 23 is not itself a proof of an actual physical oscillator. I did not infer the branch merely from the supplied numeric synth flag 1; the cited Block-5 pre-NSP formulation provides the conditional constant-reference premise. Post-NSP, the Moyer reference and bias are zero and the inversion changes; the relevant archive network/processing classification must remain checked.

## 4. Receiver epoch, transmit epoch and the archive bias formula

The receiver reference is evaluated at reception, using the **receiving station's** reference or ramp. The transmitted signal uses the **transmitting station's** ramp at the retarded transmission epoch. Moyer Eq. (13-50) separates the two integrals:

\[
D=\frac{M_{2R}}T\int_{t_{3s}}^{t_{3e}} f_{T,R}(t_3)dt_3
 -\frac{M_2}T\int_{t_{1s}}^{t_{1e}} f_{T,T}(t_1)dt_1.
\]

Sections 13.2.6 and 13.3.2.2.2 specify piecewise linear ramps and exact segment integration. Reception and transmission intervals differ through the light-time solutions. Neither a DSS-54 ramp at reception nor that ramp at retarded time automatically replaces a constant DSS-25 receiver reference. This is also why the actual X/X spacecraft ratio `880/749` is not the selected S-exciter receiver multiplier `880/221`.

TRK-2-18 Appendix A, printed A-1–A-2 / PDF pp. 23–24, separately documents the general archive construction

\[
D=\operatorname{sgn}(B)\{\Delta N/T-|KF_b+B|\},\quad
F_b=\frac{X_1}{X_2}(X_3F_r+X_4)-\frac{T_1}{T_2}(T_3F_t+T_4).
\]

It assigns `F_r` to reception time and `F_t` to reception minus RTLT, with `K=11/3` for X downlink. Its coefficients use an S-equivalent construction: `K*(240/221)=880/221` for S exciter, or `K*(240/749)=880/749` for X exciter. At sky level it sets `X3=T3=1`, `X4=T4=0`. This supports the scale, not an extra normalization. It must not be pasted over the explicitly selected Block-5 bias-removal branch. If processing provenance or count/ODF correspondence contradicts the selected branch, preserve that failure rather than adjust a scale or reference to force agreement.

Morabito and Asmar (1995), §III.C, printed p. 130 / PDF p. 10, independently documents closed-loop sky reconstruction from a synthesizer or ramp reference and bias-sign-corrected Doppler count rate. Its legacy receiver formulas should not be substituted wholesale for Block 5. Its open-loop POCA/MMR equations describe different receiver chains from the RSR.

## 5. Comparison boundary and exposure

The parent supplied: 600 ODF type-13 observations for UTC day 169 of 2002, `[48900,49500)`, receiving DSS-25/transmitting DSS-54, S exciter/X uplink/X downlink, 1 s compression, independent receiver flag 1, reference split fields `H=126186,L=14221824`; corresponding ATDF metadata receiver type 5, level 1, synth flag 1 and bias 1000 kHz. These are **parent-provided exposed metadata**, not independently decoded observations in this review.

ODF Doppler tags are count midpoints (Appendix A; Moyer Eqs. 13-24–25), so compare identical start/end intervals. Frequency estimates from RSR samples and finite phase/count differences are different estimators unless their equivalence or discrepancy is established. The inspected sources support instrument conventions and conditional reconstruction, not an error envelope, a noise-free correspondence, a gravity residual, or an independent empirical validation.

Only primary documentation and earlier frozen source-check artifacts were read. No spectra, sign/timing optimization, new raw observation samples, author implementation, repository state, or science sources were changed. This report and its manifest are a focused source check; no formal audit verdict is applied.

## Source identities

The adjacent `RECEIVER_SOURCE_EVIDENCE_v1.json` pins every source/derivative and exact read scope. Principal originals:

| Source | SHA-256 |
|---|---|
| Moyer 2000, full monograph | `23b302fd2b47b6adfadac4c2b01301396ebc54bcefb269cf7126270a3d5d87ce` |
| TRK-2-18, 2000-06-15 | `59c45204b231d5c08e8918038a4c605348d9722487664cf73325050843c77c46` |
| TRK-2-25, 1996-07-31 | `3d47f1372c76a73d1bed60f13403a402f7ded54984cf9bad53855bbfe4946dce` |
| Border–Paik 177C, 2009 | `81143ad7210e55ac6bd0b44352e0f90728cf72e36c5d1b05461f20ee65bf7f34` |
| 0159-Science, 2001-02-28 | `1161d5d7f50134cf3994c52674af4a2d8984990b7a7c64551b6c17d5964fe32d` |
| Morabito–Asmar 1995 | `73d5f703f31903206df81906c9f953f6933d93f6bb5ec54bc1a14d0c5f738ddc` |

Primary links: [Moyer](https://descanso.jpl.nasa.gov/monograph/series2/Descanso2_all.pdf), [ODF specification](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-18/dsn_trk-2-18.2000-06-15.pdf), [ATDF specification](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-25/dsn_trk-2-25.1996-07-31.pdf), [RSR sign paper](https://ipnpr.jpl.nasa.gov/progress_report/42-177/177C.pdf), [original RSR specification](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_0159-SCIENCE/dsn_0159-science.2001-02-28.pdf), [Morabito–Asmar](https://tda.jpl.nasa.gov/progress_report/42-120/120B.pdf).
