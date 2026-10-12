# Frozen GW170817 extraction: failed arrival-identification control

The fixed extraction did **not** establish a usable set of three
band-arrival windows. It therefore supplies no measured propagation
bound. The algebra below is a conditional compatibility calculation,
not an empirical exclusion obtained from these peaks.

`EXTRACTION_CONTRACT.md` was frozen at `2026-10-12T17:42:58.198264Z`,
before either target strain file was downloaded or read. Its SHA256 is
`1bb220086059126add589bb4a3f2f04c0c35044cfecd361c620157e59ddfa937`.
No extraction amendment was made after viewing the output.

## Observed result of the fixed rule

The one-second Hann transform, five-bin bands, background normalization,
thresholds, and two-second cross-detector tolerance are specified in the
contract. The table gives the strongest target-band power peak; a failed
threshold is retained rather than promoted to an arrival measurement.

| Detector | Band centre | Strongest peak time, s | Score | Frozen threshold | Result |
|---|---:|---:|---:|---:|---|
| L1 | 50 Hz | -8.46125 | 6.112 | 3.568 | Three competing components |
| L1 | 70 Hz | -5.58625 | 9.716 | 4.334 | Two competing components |
| L1 | 90 Hz | -2.96125 | 3.333 | 4.566 | No qualifying component |
| H1 | 50 Hz | -4.05500 | 4.409 | 3.000 | Five competing components |
| H1 | 70 Hz | -8.39875 | 5.531 | 3.712 | Two competing components |
| H1 | 90 Hz | -2.86750 | 4.399 | 4.123 | Two competing components |

Times are relative to GPS `1187008882.43`. The strongest L1/H1 peaks
differ by `4.40625 s` at 50 Hz and `2.81250 s` at 70 Hz. Both fail the
fixed control tolerance. L1 has no accepted 90-Hz component.

For example, naively interpreting the three strongest H1 components as
source arrivals would give a **negative** contrast interval,
`[-6.567,-3.859] s`, incompatible even with a nonnegative dispersive
coefficient under the exact stipulated source family. This is a useful
failure signal for peak assignment, not evidence against the family or
against massless propagation. All competing components are preserved
in `CHECK_RECEIPT.json` and the full runtime receipt.

Visual inspection of the already-computed diagnostic plot shows a rising
feature in L1 across the wider displayed frequency range. That does not
retroactively change the frozen peak-assignment rule or rescue its
failed controls. The extraction needs a better specified association
method before narrower time windows can carry empirical weight.

## Conditional contrast calculation

For

\[
 t(f)=t_c-Bf^{-8/3}+Af^{-2},
\]

take `f=(50,70,90) Hz`,

\[
 \lambda=\frac{f_2^{-8/3}-f_3^{-8/3}}
 {f_1^{-8/3}-f_3^{-8/3}}=0.2515797408531089,
\]

\[
 C=t_2-\lambda t_1-(1-\lambda)t_3=A\kappa,
 \quad \kappa=1.1052173454176778\times10^{-5}\ {\rm Hz}^{-2}.
\]

The constant offset and the free chirp coefficient cancel exactly.
The selected pole `mu=6.42760036943869e-12 m^-1` at the conservative
linear distance `D=26 Mpc` has

\[
 A=\frac{Dc\mu^2}{8\pi^2}=1.2584981973964733\times10^8\ {\rm s\,Hz^2}.
\]

Its leading extra group delays are `50339.928`, `25683.637`, and
`15537.015 s`, and its contrast is `1390.91404 s`. The exact expression

\[
 \frac Dc\left[\frac1{\sqrt{1-(c\mu/(2\pi f))^2}}-1\right]
\]

differs from the leading expansion by less than `2.83e-11` relative in
these bands. The implementation uses `log1p`/`expm1` to avoid losing this
small delay factor by subtraction.

**If** three source arrivals at these nominal frequencies were
established anywhere in the fixed common timing hull
`[-15.30,-1.70] s`, its width alone would imply the necessary condition
`A <= 1.23053e6 s Hz^2`. This is not a fit of `t_c` and does not require
an imported chirp mass.

The frozen, broader frequency-localization box was
`[45,55] x [65,75] x [85,95] Hz`. Concavity of `q=x^(3/4)` for
`x=f^(-8/3)` gives the rigorous interpolation-curvature lower bound
`kappa >= 7.0828524658152e-7 Hz^-2` throughout that box. Conditional on
those frequency and timing assignments, the conservative bound becomes

`A <= 1.92013035e7 s Hz^2`.

The selected pole exceeds that conditional bound by a factor `6.55`.
If independently bounded source-time residuals satisfy
`|delta t_i| <= epsilon`, replace the numerator `13.60` by
`13.60+2 epsilon`. At least `epsilon=37.77 s` is necessary to remove
this particular broad-box contradiction using that residual allowance.
This states the source-model dependence explicitly; it does not prove
that an arbitrary source must obey the leading chirp power law.

The antecedent—reliable identification of all three arrivals—failed
in the frozen extraction. None of these conditional numbers is reported
as a measured exclusion or a confidence limit.

## Data, calibration, noise, and glitch bookkeeping

The primary [GWTC-1 documentation](https://gwosc.org/GWTC-1/) identifies
the O2 C02-cleaned source channels and the 4-kHz downsampling. Its
GW170817-v3 release retains the loud L1 glitch. The separate
[T1700406-v3 product](https://dcc.ligo.org/LIGO-T1700406/public) subtracts
a BayesWave median glitch reconstruction; that product was not used.
The [event data-release page](https://gwosc.org/events/GW170817/) gives
the glitch time and the published search gate. This calculation uses
neither a glitch model nor a global time filter.

Both downloaded 32-s files have native sample spacing `1/4096 s`, GPS
start `1187008867`, and 131072 finite strain samples. The actual target
transform support is `[-15.2425001,-1.7737501] s`; its end precedes the
published glitch time by about `0.733 s`. The transform uses 400 target
centres and 288 post-event background centres. These centres overlap
strongly, so their empirical percentile is not a collection of
independent trials or a calibrated significance.

L1's quality mask is `31` during GPS seconds `1187008880..1187008883`,
and `127` elsewhere in the file. Thus the DATA/CBC flags pass while
BURST_CAT2 and BURST_CAT3 fail in that interval. Some of the latest
allowed transform supports overlap the flagged interval, even though
they precede the glitch itself. H1's mask is `127` throughout. Both
injection masks are `23`: the no-CBC, no-Burst, no-Detchar, and
no-stochastic tests pass, while the no-continuous-wave test does not.
The calculation does not silently equate those files with an injection-
free or artifact-free time series.

The event-specific calibration envelopes were downloaded from
[P1900040-v1](https://dcc.ligo.org/LIGO-P1900040/public), DOI
`10.7935/KSX7-QQ51`, and linearly interpolated as its README instructs.
At 50, 70, and 90 Hz, median amplitudes differ from one by less than
`0.55%`; the reported marginal one-sigma amplitude endpoints range
approximately `0.9848..1.0214`, and phase endpoints lie within about
`0.0148 rad` of zero. These are amplitude/phase envelopes, not a joint
frequency covariance or an arrival-time confidence interval. The
contract's extra `0.05 s` timing allowance remains an explicit margin,
not a confidence statement derived from those envelopes.

The post-event background may differ from the on-source noise. The
finite Hann window also has spectral leakage. The wider frequency
ranges and source association are explicit assumptions; a spectrogram
does not by itself produce hard source-frequency bounds.

## Reproduction and the next calculation

Run `extract_three_bands.py` after restoring the raw files listed in
`CHECK_RECEIPT.json`. The code checks the immutable contract hash and
campaign stop/deadline controls. The receipt includes file URLs and
SHA256 hashes, source calibration envelopes, library versions, all
quality/injection bits, all qualifying components, and failed controls.

Runtime directory:

`/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity_measurements/waveform/`

Key artifacts are `download_manifest.json`, `contract_freeze.json`,
`frozen_extraction_results.json`, `L1_spectrogram.npz`,
`H1_spectrogram.npz`, and `frozen_three_band_diagnostics.png`.

A next extraction should be a named new contract, retain this failure,
and replace isolated band maxima with a specified multi-frequency,
multi-detector association rule plus a longer, independently chosen
noise control. It should test its timing windows on injected chirps and
time-shifted controls before claiming calibrated arrival coverage.
Until then, the robust product is the primary-data receipt and the
explicit conditional contrast, not a new measured dispersive limit.
