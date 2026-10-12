# GW170817 three-band timing extraction: frozen development contract

This contract is fixed before downloading or inspecting the target strain
or any target ridge output. Published event identity, GPS time, source
descriptions, and the existence/location of the L1 glitch are known.
This is a model-development comparison, not a blinded discovery test,
full likelihood, significance calculation, or universal gravity bound.

## Data and version

Use the GWTC-1-confident event `GW170817-v3`, DOI
`10.7935/82H3-HH23`, 4096-Hz, 32-second HDF5 strain files for L1 and H1,
starting at GPS `1187008867`. L1 is primary; H1 is an independent
instrumental control. Reference GPS `1187008882.43` defines only a time
origin. A constant detector/geocentre offset cancels in a within-detector
contrast. The event API rounds its event GPS to `1187008882.4`; this is
not a timing uncertainty or a fitted Fourier-mode arrival time.

Source metadata already read, without strain inspection:

* https://gwosc.org/eventapi/json/GWTC-1-confident/GW170817/v3/
* https://gwosc.org/GWTC-1/
* https://gwosc.org/events/GW170817/

GWTC-1 v3 contains the L1 glitch. For O2 it packages the
`H1:DCH-CLEAN_STRAIN_C02` and `L1:DCH-CLEAN_STRAIN_C02` source channels,
with the public 4-kHz series downsampled from 16 kHz. This ordinary noise
cleaning is distinct from removing the GW170817 glitch. The older v2
release and DCC T1700406 glitch-subtracted data have different calibration
and/or glitch-model histories and are not silently substituted.

Published glitch GPS is `1187008881.389`, about `-1.041 s` relative to
the chosen origin. The release describes a search gate zeroed within
`0.1 s` of that time, with an additional `0.5 s` roll-off on each side.
This extraction does not apply that gate or any glitch model. Every
target transform has compact support ending before relative time
`-1.75 s`. Data-quality and injection masks must be retained in the
receipt, including any differing CBC/Burst flags.

## Fixed transform and background

* Read native 4096-Hz strain, with no additional downsampling, notch,
  global Fourier whitening, or causal/noncausal bandpass filter.
* Use a one-second periodic Hann window, remove the constant mean in
  each window, and compute one-sided PSD spectrograms with 1-Hz bins.
  Window-centre hop is `1/32 s`; do not pad beyond data boundaries.
* Target bands, inclusive of frequency-bin endpoints, are `48..52`,
  `68..72`, and `88..92 Hz`, nominal centres `50,70,90 Hz`.
* Search all window centres in `[-14.75,-2.25] s`; do not select a
  different time interval after viewing the ridge.
* Background uses centres in `[4.5,13.5] s`, so all background supports
  lie in `[4,14] s`. This assumes those low-frequency post-event data
  represent a usable local noise control; it does not establish
  stationarity.
* Divide each frequency-bin power by its median background power, then
  average the five normalized powers in a target band. This normalizes
  displayed power without filtering time samples or spreading the glitch
  into earlier windows.

## Operational windows and failure reporting

For each detector and band, report the maximum score, all connected
components exceeding `max(3, empirical 99th percentile of background
band scores)`, and their peak times. These thresholds are diagnostics
fixed in advance; their percentiles are not false-alarm probabilities.
Pad each reported component by half the transform duration (`0.5 s`)
and a further `0.05 s` timing allowance. The latter is an explicit
development margin, not a derived calibration confidence interval.

Report the strongest component and its cross-detector match, using a
fixed two-second tolerance for peak-time agreement. Retain competing
components. Do not force three identified chirp arrivals if the data
are ambiguous, a peak fails the threshold, or H1 fails the control.
A strong control failure limits any use of narrow windows; the broad
support calculation below remains conditional on actual band assignment.

For a conservative frequency-localization calculation, use fixed ranges
`[45,55]`, `[65,75]`, `[85,95] Hz`. The broader ranges account for a
finite-window chirp and leakage only as an explicit identification
assumption. A Hann spectrogram does not mathematically guarantee that
all contributing source power has frequencies in these ranges.

The fixed common timing support, including the margin, is
`[-15.30,-1.70] s`, of width `13.60 s`. It is an intentionally broad
conditional alternative to the selected narrow components. Neither
type of interval is a statistical confidence interval.

## Frozen propagation and source model

Use the previously selected pole `mu=6.42760036943869e-12 m^-1`,
distance `D=26 Mpc`, `c=299792458 m/s`, and
`1 Mpc=3.0856775814913673e22 m`. Neglect cosmological redshift in this
linear-distance benchmark. The leading extra group delay is

`Delta t(f)=A/f^2`, `A=D c mu^2/(8 pi^2)`.

This is valid here because `c mu/(2 pi f)` is very small. Compare with
the exact massive-pole expression to retain its truncation error.

The conditional emitted time-frequency family is

`t_emit(f)=t_c-B f^(-8/3)`, with `B>0` free.

Do not insert a measured chirp mass or identify fitted `t_c` with a
single Fourier-mode arrival. The exponent, the source association,
linear propagation, and the single selected pole are explicit premises.
Also report sensitivity to independent source-time residuals
`|delta t_i| <= epsilon`, rather than treating the leading chirp law as
exact physics for every source.

For three frequencies define `x_i=f_i^(-8/3)`, `q_i=f_i^-2`,
`lambda=(x_2-x_3)/(x_1-x_3)`, and

`C=t_2-lambda t_1-(1-lambda)t_3`,
`kappa=q_2-lambda q_1-(1-lambda)q_3`.

Then `C=A kappa` eliminates both `t_c` and `B`. Since
`q=x^(3/4)` is strictly concave, `kappa>0` for ordered distinct
frequencies. From timing intervals `[L_i,U_i]`, the necessary bound is

`A <= [U_2-lambda L_1-(1-lambda)L_3+2 epsilon]/kappa`.

For the entire frequency-range box a rigorous lower bound is

`kappa_min = (3/32) f1_lo^(10/3)`
`             * (f1_hi^(-8/3)-f2_lo^(-8/3))`
`             * (f2_hi^(-8/3)-f3_lo^(-8/3))`.

It follows from the interpolation remainder and a lower bound on
`-d^2[x^(3/4)]/dx^2` over the full interval. The broad timing hull
therefore implies, conditionally, `A <= (13.60+2 epsilon)/kappa_min`.
No target output changes this predeclared inequality or the data choices.

## Artifacts and amendments

Keep raw downloads and all signal arrays/plots only in the campaign
runtime `gravity_measurements/waveform/`. Keep code, this contract, and
compact reports only in `agents/gravity_waveform/`. Record URLs,
retrieval times, hashes, library versions, HDF5 metadata, transform
parameters, DQ/injection masks, and all failed/ambiguous components.
Any later change is a named amendment with its reason and cannot be
represented as the original frozen extraction.
