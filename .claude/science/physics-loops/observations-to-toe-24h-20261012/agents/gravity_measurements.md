# Gravity measurements: observables, kernels, and source recovery

Date: 2026-10-12. Source/main pin: `7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de`.
Status: **conditional-support**; focused source reconstruction and mathematical check, not a formal audit or a Cassini likelihood refit.

```yaml
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
proposal_allowed_reason: empirical inputs and candidate metric/spectral premises remain supplied
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Target: establish which measured quantities constrain a positive spin-2/spin-0
spectral response, identify reusable data, and independently check the declared
G1 geometry benchmark. No physical premise is adopted. No claim or audit state
is changed. Scientific success here is a correct forward observable and an
explicit missing-data boundary, not a favorable gravity result.

Runtime evidence directory (all downloads and scratch code):
`/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity_measurements/`.
The dispatch's deadline/stop markers were checked before downloads and the
independent calculation. No detached worker, commit, push, or PR operation.

## 1. Cassini primary source and the fitted response class

Primary paper: [Bertotti, Iess & Tortora, Nature 425, 374-376 (2003)](https://doi.org/10.1038/nature01997).
Downloaded publication PDF: `cassini_bertotti_iess_tortora_2003.pdf`, SHA256
`469522ec41d183062d681860a212934a1dc1ebea741add8e401ac8bbe0942df7`.
Its original publisher supplementary figures and legends were also recovered;
URLs, content sizes, and hashes are in `download_manifest_archives.json`.

Measurement digest (paper pp. 374-376, Figures 1-3, Method):

| Item | Published input/result |
|---|---|
| Fit | `gamma-1 = (2.1 +/- 2.3) 10^-5` |
| Geometry | 2002-06-21 conjunction; minimum impact `1.6 R_sun`; Cassini geocentric distance `8.43 AU` |
| Data span | 2002-06-06 to 2002-07-07; 18 passes of about 8 h; three pre-conjunction days lost |
| Data reduction | 1 kHz open-loop samples; three reconstructed 1 s frequency series; 1,094 points compressed to 300 s |
| Residual RMS | `1.2 10^-4 Hz` at 8.4 GHz, equivalent one-way range rate `2.2 10^-6 m/s` |
| Nine fitted parameters | initial 6D spacecraft state, radial RTG acceleration, diffuse antenna reflectivity, gamma |
| Other parameters | nonradial RTG accelerations and specular reflectivity supplied from 2002-11-26 to 2003-01-04 opposition fit |
| Uncertainty model | independent samples, separate pass standard deviations; considered uncertainties enter covariance |
| Considered effects | dry troposphere, station coordinates, polar motion, Earth Love numbers, supplied force parameters |
| Stability trials | 12-parameter gamma shift `(1.35 +/- 2.47)10^-5`; 8-parameter shift `(0.21 +/- 2.43)10^-5` |

The uncertainty is a fit-derived standard error, not a model-free confidence
envelope for arbitrary radial response. The paper describes noise/outlier and
before/after-conjunction checks but does not publish a numeric covariance
matrix, design matrix, complete point timestamps/weights, or every prior.

The supplementary legend explains the three-link decomposition: the
nondispersive component plus separate up/down plasma components are solved
from X-X, X-Ka, and Ka-Ka observables. It describes calibrated residuals as
approximately white. This does not supply the calibrated time series itself.

### Printed-equation normalization warning

The publication's first page was visually checked in `cassini_page1.png`.
Its equation (1), described as round-trip delay, is

`DeltaT = 2(1+gamma) GM/c^3 log(4 r1 r2/b^2)`.

Its printed equation (2) writes the derivative with coefficient
`-2(1+gamma) GM/(c^3 b) db/dt`; literal differentiation of (1), holding the
far endpoints fixed, instead gives coefficient `-4`. The received-frequency
sign also requires an explicit phase convention. Do not use this schematic
pair to fix a new model's normalization. This observation does **not** identify
an error in the actual Orbit Determination Program fit, which fitted complete
light-time observables. The derivation below fixes its own convention.

## 2. Forward observable derived from phase and null propagation

Use positive attractive potentials in the explicitly supplied weak, static,
isotropic metric

`ds^2 = -(1-2U/c^2)c^2 dt^2 + (1+2V/c^2) d x^2`.

To first order and along the unperturbed ray, `ds^2=0` gives

`T_leg = R/c + c^-3 integral_leg (U+V) dl`.

For a coherent transponder with turnaround ratio k, received phase is
`phi_rec(tau3) = k phi_up(tau1(tau3)) + constant`; therefore
`nu_rec = k nu_up(tau1) d tau1/d tau3`. For a fixed reference carrier, an
additional round-trip delay contributes the received-frequency convention

`delta y = -d(delta T_roundtrip)/dt3`.

A Doppler count of duration tau uses the finite difference
`delta y_i = -[deltaT(t_i+tau/2)-deltaT(t_i-tau/2)]/tau`.
Actual uplink ramps, proper-coordinate time conversions, and distinct
emission/turnaround/reception epochs must be included in a real refit.

In the parent contract's convention, with nonnegative spectral measures and
exterior source factor F(mu),

`U = Gstar M/r [Z + (4/3) integral F exp(-mu r) dW2 + 2 integral F exp(-mu r) dW0]`,

`V = Gstar M/r [Z + (2/3) integral F exp(-mu r) dW2 - 2 integral F exp(-mu r) dW0]`.

Thus `U+V = 2 Gstar M/r [Z + integral F exp(-mu r) dW2]`.
Scalar response cancels from this direct first-order null-path term. It still
affects dynamical masses, trajectories, and endpoint clocks. This cancellation
assumes universal metric coupling and the stated linear unscreened response;
it is not a general assertion about scalar gravity.

For fixed longitudinal endpoints `-L_E, L_S`, define

`I_mu(b) = integral[-L_E,L_S] exp(-mu sqrt(b^2+z^2))/sqrt(b^2+z^2) dz`.

The equal-leg approximation gives

`DeltaT_roundtrip = (4 Gstar M/c^3) [Z I_0(b) + integral F(mu) I_mu(b) dW2(mu)]`.

The gradient kernel is

`K_mu(b) = -partial_b I_mu = b integral exp(-mu r)(1+mu r)/r^3 dz`.

Consequently the quasi-static equal-leg Doppler term is
`y = (4 Gstar M/c^3) db/dt [Z K_0 + integral F K_mu dW2]`.
Useful checks:

`I_0 = asinh(L_E/b) + asinh(L_S/b)`,

`K_0 = [L_E/sqrt(L_E^2+b^2) + L_S/sqrt(L_S^2+b^2)]/b`,

`I_mu(infinite endpoints) = 2 BesselK_0(mu b)` for `mu>0`,

`K_mu(infinite endpoints) = 2 mu BesselK_1(mu b)` and `K_0 -> 2/b`.

These formulas are an analytic geometry benchmark. Cassini's two-way light
time is about 2.34 h at the quoted distance: the two solar passages do not
have identical impact parameters. Fixed endpoints and identical legs are
inappropriate for a precision fit. The parent benchmark explicitly declares
its fixed-z geometry; its spacecraft z endpoint of 8.43 AU is not a recovered
heliocentric Cassini state.

## 3. Why a constant PPN gamma is not a finite-range likelihood

A nonrelativistic circular-force calibration at radius r0 supplies

`GM_dyn(r0) = Gstar M [Z + (4/3) integral F(1+mu r0)exp(-mu r0)dW2 + 2 integral F(1+mu r0)exp(-mu r0)dW0]`.

Actual ephemerides fit multiple bodies/radii; this one-radius calibration is
only a declared benchmark. A local ratio `V(b)/U(b)` is generally not the
coefficient inferred from a light-path fit normalized by orbital `GM_dyn`.
For example, `b << lambda << r0` permits extra spin-2 light response with
little force-calibration change. Its apparent gamma shift can be positive,
although the local positive-spectrum ratio `V/U` is at most one. Different
mass ranges can therefore cancel in a compressed gamma statistic despite
nonnegative spectral weights. Short-range scalar modes can escape the direct
null-path test altogether when their endpoint/dynamical effects are small.

More formally, linearize calibrated data around a reference solution with
gamma template h, nuisance design X, and precision matrix C^-1. With nuisance
prior precision Lambda, define

`P = C^-1 - C^-1 X (X^T C^-1 X + Lambda)^-1 X^T C^-1`.

This is an illustrative linear-Gaussian profiling formula, not a claim that
the original program's consider-parameter treatment used this exact form.

The mean bias in the fitted gamma induced by an alternative signal s is
`delta gamma_hat = (h^T P s)/(h^T P h)`.
The published one-parameter estimate supplies neither `P` nor `s`'s component
orthogonal to h. A new spectral fit needs both the photon kernel and orbital
response to U, nuisance refitting, and the original calibration/covariance.
Replacing gamma by its value at `b_min`, or dividing one raw residual RMS by
a peak prediction, does not recover that likelihood.

## 4. Independent check of the parent's G1 benchmark

The input contract was read before the author's implementation or results.
Its saved SHA256 is
`4478751aae5cd9683466649fc9031d94f75c0ac1259c9661b104a83d692a252d`.
The independent script uses 35-digit `mpmath 1.3.0`: substitute `z=b sinh(t)`
in the potential integral, then numerically differentiate the entire integral
including moving endpoints. The force is independently differentiated from
`exp(-mu r)/r`. It does not import the parent's code or target constants.

Runtime files: `independent_geometry_check.py`,
`independent_check_input_contract.json`, `independent_geometry_results.json`.

For pure massive spin-2, calibrating the light/force ratio at `b=1.6 R_sun`
to its GR value yields

`mu AU = 0.9615553289785613951`,
`mu = 6.4276003694386901e-12 m^-1`,
`lambda = 1.5557905633876987e11 m`.

| b / R_sun | Gamma-like geometry ratio |
|---:|---:|
| 1.6 | 1.0000000000000000 |
| 2 | 0.9998653270109930 |
| 4 | 0.9988695242933285 |
| 8 | 0.9955498691219673 |
| 16 | 0.9849087474122094 |

Force ratios relative to Newtonian gravity after calibration at 1 AU are
`1.26118796436, 1.12796657053, 0.759394074926` at radii
`0.387, 0.723, 1.524 AU`, respectively. These are future data targets, not
scored planetary observations.

For `omega^2=c^2(k^2+mu^2)`, the group delay over the explicitly supplied
26 Mpc is `D/c [(1-(mu c/omega)^2)^(-1/2)-1]`. At frequencies
`30, 100, 300, 1000 Hz`, independent delays are
`139833.133055, 12584.9819741, 1398.33133044, 125.849819740 s`.
After generating these results, the parent's `gravity/block01_results.json`
was read: the root, shape, force, and delay values agree to floating-point
precision. This is a focused mathematical check, not a full landing review.

`compare_independent_geometry.py` subsequently compared 15 frozen values:
15 agree, zero disagree at relative tolerance `1e-10`. It rejected three
deliberately incorrect result sets: doubled mass scale, constant-gamma shape,
and omission of the angular-frequency conversion. The source-bound receipt
is `independent_comparison_receipt.json`; the frozen author output is
`author_results_at_comparison.json`. These probes establish that the
comparison detects those errors, not completeness of the physics check.

Commands actually run:

```sh
python3 /Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity_measurements/independent_geometry_check.py
python3 /Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/gravity_measurements/compare_independent_geometry.py
```

## 5. Source recovery and next measurement calculation

[NASA PDS's SCE1 record](https://pds.nasa.gov/ds-view/pds/viewProfile.jsp?dsid=CO-SS-RSS-1-SCE1-V1.0)
identifies `CO-SS-RSS-1-SCE1-V1.0`. Its
[actual archive](https://atmos.nmsu.edu/pdsd/archive/data/co-ss-rss-1-sce1-v10/)
has volumes `CORS_0021` through `CORS_0028`. The final volume's cumulative
index was downloaded and parsed: 688 products, including 266 RSR recordings,
51 ODFs, 51 TDFs, 30 PD1 and 30 PD2 products, plus attitude, ephemeris, Earth
orientation, ionospheric, and tropospheric products. RSR coverage spans
`2002-157T06:39:50` through `2002-187T01:20:00`. Repeated ancillary products
are included in those counts; they are not 688 independent measurements.

The archive contains raw closed/open-loop recordings and calibration inputs.
It does not identify the published 1,094 calibrated points or numerical
fit covariance in its cumulative index. No such final time series has been
recovered in this bounded search; this is not proof that none exists elsewhere.
Archive errata specifically says no LOG files are supplied.

The [2018 Cassini Radio Science User's Guide](https://pds.nasa.gov/data/pds4/misc/document_cassini/Cassini_Radio_Science_Users_Guide_30Sep2018.pdf),
pp. 66-67, independently describes Doppler-only analysis, exclusion of range,
and tropospheric/antenna-deformation noise. It gives Cassini's heliocentric
distance as approximately **7.4 AU**. Thus **8.43 AU is geocentric**, and using
8.43 AU for the far heliocentric z endpoint in the parent contract is a
declared idealization, not actual Cassini geometry.

Concrete recoverable input set for a next single-pass reconstruction:

- Volume `cors_0025`, directory `sce1_174/rsr/`, common interval
  `2002-174T15:53:00` to `2002-175T00:00:00` (UTC labels).
- Ka-Ka: `c32easc2002_174_1552k25k25d.3a1`.
- X-Ka: `c32easc2002_174_1553x25k25d.1b1`.
- X-X: `c32easc2002_174_1553x25x25d.1a1`.
- Corresponding `.lbl` files define per-record fields and byte order.
  `sce1_candidate_pass_174.json` preserves the index rows. The archive's
  `document/casrssis.txt`, `dors_002_020501.txt`, `trk_2_21_950831.txt`, and
  `trk_2_23_000531.txt` are identified in the downloaded directory listing.
- `SCE1_ANCILLARY/SPK/C32EASC2002_160_2002_186.SPK` is identified as
  `SM727D_SHORTARC_SCE1.BSP` in the index, with label coverage through
  `2002-187T00:00:00`; it covers this candidate pass. Attitude, EOP, TRO,
  ION and PD1/PD2 inputs are indexed separately.

First compute actual distinct uplink/downlink geometry at the 300 s count
endpoints using the SPK plus the matching planetary, time and station model;
evaluate the finite-leg kernel above. Then reconstruct three sky-frequency
series using the RSR frequency/predict metadata, solve the three-channel
nondispersive/plasma system, apply the supplied path corrections, and compare
the residual shape. Large raw RSR products were **not** downloaded or decoded.
This is a concrete next reconstruction, not a promise that the original
calibration/cuts are fully reproducible. A precision refit still needs the
original solve/consider priors, pass weights/cuts, complete force model, and
numerical covariance or an explicitly rebuilt substitute.

For the channel algebra, each fractional frequency has form
`y_j = y_nd + a_j P_up + b_j P_down`, with inverse-square carrier-frequency
coefficients supplied by the actual uplink/downlink frequencies. Inverting
the three-row matrix `[1,a_j,b_j]` preserves an achromatic metric signal.
It need not preserve an arbitrary frequency-dependent photon modification;
the calibration's response class is part of the measurement.

## 6. GW170817/GRB timing: exact fit input and model assumptions

Primary source: [Abbott et al., ApJL 848 L13, arXiv:1710.05834v2](https://arxiv.org/abs/1710.05834v2),
version dated 2017-11-02. Downloaded PDF SHA256
`bf06bd2ae6a23cf7f7092307677c2b681ce02abab3b5bbe37bbce76a8960140a`;
the saved abstract page records the version history.

The measured `+1.74 +/- 0.05 s` is a fitted pulse-onset lag: the gamma-ray
onset fit is `0.310 +/- 0.048 s` before GBM's trigger, with `+3.176 ms`
geocentric correction. It is not the raw trigger difference or a measured
source emission lag. Gamma-ray uncertainties are 68% intervals (§2.2).
Section 4.1 assumes emission lags from zero to ten seconds and takes
`D=26 Mpc`, the lower endpoint of the GW-only 90% luminosity-distance
interval `40[-14,+8] Mpc`, obtaining the rounded speed bracket
`-3e-15 <= (v_GW-c)/c <= 7e-16`.

Frame precision: §4.1 does not explicitly distinguish source-frame and
observer-frame ten-second lags and inserts no redshift factor. Its operational
calculation uses the low-redshift approximation `delta v/c = c DeltaT/D`
with luminosity distance replacing propagation distance. The rounded bracket
does not establish an exact source-frame prior. Changing the waveform's
amplitude/distance law can also invalidate the borrowed GW distance posterior.

Explicit general bookkeeping, derived here, is

`Delta t_obs = (1+z) tau_emit + T_EM - T_GW`,

and, for nearly constant fractional speed change `epsilon=(v_GW-c)/c`,

`Delta t_obs approximately (1+z) tau_emit + (D/c) epsilon`.

For a declared observer-frame lag `tau_int in [0,10] s`, and the parent's
chosen rectangular interval `Delta t_obs in [1.64,1.84] s` (twice the quoted
68% onset uncertainty), a slower identified GW carrier may have

`0 <= T_GW-T_EM <= 10-1.64 = 8.36 s`.

This is a **model-development compatibility rule**, not a 95% joint posterior
or a general statistical exclusion. If ten seconds is assigned to source
proper time instead, use `(1+z)10` and specify z. Intrinsic delays outside
that window change the bound; the paper itself discusses longer/negative
emission lags. Differential background delays must also be modeled if allowed.

The pole in section 4 has group delays above this rule at all four declared
frequencies. The valid statement is conditional on that pole being the
observed propagating carrier, the dispersion law, the distance convention,
and the chosen emission window. A small massive residue coexisting with an
observed massless carrier is not excluded by that arrival-time comparison.
Broadband dispersive waveform fitting is a stronger and distinct next task;
one cannot freeze a GR-inferred waveform and silently identify all its modes.

### Accessible direct radiative data

[GWOSC GW170817-v3 metadata](https://gwosc.org/eventapi/html/event/GW170817/)
was saved as `gwosc_gw170817_v3.json`. It lists H1, L1 and V1 strain files,
including 4096 s at 4096 Hz (GPS start 1187006835), plus other rates/formats.
Those are calibrated detector strain, not the source metric directly.
The [GWTC-1 documentation](https://gwosc.org/GWTC-1/) states the released
Livingston series includes its glitch; the cleaned alternatives use different
calibration/glitch versions and must not be interchanged without recording it.
[DCC T1700406](https://dcc.ligo.org/LIGO-T1700406/public) currently identifies
`L-L1_CLEANED_HOFT_C02_T1700406_v3-1187008667-4096.gwf`.
Metadata were downloaded; the large strain arrays were not.

[HEASARC's GBM event directory](https://heasarc.gsfc.nasa.gov/FTP/fermi/data/gbm/bursts/2017/bn170817529/current/)
is directly accessible. Two files were downloaded and hashed:
`glg_tcat_all_bn170817529_v03.fit` and
`glg_tte_n2_bn170817529_v00.fit` (2.76 MB). The latter contains time-tagged
events for NaI detector 02; the directory supplies other detectors, response
and catalog products. Header extraction in `fermi_primary_fits_headers.json`
records `TIMESYS=TT`, `TIMEUNIT=s`, `MJDREFI=51910`,
`MJDREFF=7.428703703703703e-4`, and `TRIGTIME=524666471.474598`.
Use event times and the source/spacecraft geometry to reproduce a geocentric
onset fit. The older TTE header has a preliminary sky position; the TCAT v03
position differs, so the old position must not be used silently.

## 7. Prior-repository overlap and remaining limits

The exact relevant scopes were inspected in `docs/SHAPIRO_DELAY_NOTE.md`,
`SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`, `SHAPIRO_EXPERIMENTAL_CARD.md`, and
`GRAVITY_CONFORMAL_SCALE_SPLIT_LENSING_RECORDS_DERIVED_SHAPIRO_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md`.
The first two are finite proxy/cone replay artifacts that exclude a physical
Shapiro law. The experimental card contains older stronger proxy language;
none reconstructs Cassini's calibrated data or supplies its likelihood.

The conformal-scale note identifies a propagation-path integral
`integral sqrt(-g_tt) dt` with proper Shapiro delay. That is not the Cassini
clock observable. For fixed endpoint worldlines, null travel time follows
`dt = sqrt(g_ij dx^i dx^j/(-g_tt))/c`, which is unchanged by `g -> Omega^2 g`.
Proper time is accumulated on the receiver's clock worldline, not along a
null ray. If Omega is one on the emitting/receiving ground-clock worldline,
altering Omega only along the ray leaves this travel-time measurement
unchanged. This narrow measurement counterexample does not resolve source
dynamics or any records-to-metric claim and applies no audit verdict.

No new empirical limit on a general spectral measure has been obtained.
What is now supplied is the observable kernel, its checked normalization,
the actual published fit/lag assumptions, an exact raw-data route, and the
specific nuisance/source/detector information still required for inference.

Extraction record: Python's default urllib certificate chain failed; system
`curl -f -L` succeeded with normal certificate verification. Download manifests
preserve URLs, status, sizes and SHA256 hashes. PDF text extraction emitted
warnings about broken object offsets in the user guide; relevant pages were
also extracted with PyMuPDF, and the load-bearing Cassini equation was
visually inspected using Poppler rendering. These are extraction limitations,
not measured physical uncertainties.
