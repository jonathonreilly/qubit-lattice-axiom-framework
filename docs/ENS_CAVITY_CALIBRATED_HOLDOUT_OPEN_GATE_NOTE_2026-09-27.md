---
claim_id: ens_cavity_calibrated_holdout_open_gate_note_2026-09-27
claim_type: open_gate
claim_scope: "Retrospective numerical ENS comparison using five calibration observables and an imported single-transparency circuit model; physical-offset Ramsey scale comparison; no native TOE derivation, unique mechanism identification, statistical validation, or general exclusion."
upstream_dependencies: []
runner: scripts/ens_cavity_holdout_2026_09_27.py
---

**Type:** open_gate
**Status:** conditional-support; independently checked numerical comparison, unaudited.

# A separately calibrated junction shape improves unused ENS transitions

A supplied Andreev junction potential, calibrated with two transmon transitions
and three state-dependent cavity lines, improves four unused measured transmon
transitions relative to a four-input cosine baseline. The nominal drive errors
change from +0.796, +2.899, +6.239, +11.008 MHz to −0.218, −0.390, −0.951,
−2.323 MHz. This uses one additional observation and one additional parameter.
It is a retrospective withheld-observable test, not a blind or parameter-free
prediction. The highest transition still has a MHz-scale residual.

The open gate is physical identification: the framework does not derive this
junction potential, its fitted transparency, the circuit parameters, or the
measurement instrument. Improved numerical agreement of this imported family
does not establish a native TOE prediction or uniquely identify a mechanism.
The earlier square-spectrum result and its finite-spin regulator are not inputs
or physical parameters of this comparison.

## Supplied physical model and its domain

Use conventional charge and photon Hilbert spaces, n integer, and GHz energy
frequencies throughout. The full capacitive-coupling model is

    H/h = 4 EC(n-ng)^2 + V_tau(phi) + Omega a* a + G n(a+a*).

The short-junction, ground-state, zero-temperature shape is supplied from the
Andreev model discussed by Willsch et al. Its unnormalized potential is
−sqrt(1−tau sin²(phi/2)). The Fourier coefficient of cos(phi) is normalized to
−EJ1, fixing its amplitude while tau fixes every higher harmonic. Equivalently,
for s=sin²(phi/2), compute the complex Fourier coefficients c_m of

    w_tau(phi) = 4s / (1+sqrt(1-tau*s)),
    V_tau(phi) = EJ1 w_tau(phi)/(-2 c_1).

For tau>0 this differs from the raw square root only by a positive scale and a
scalar; at tau=0, w=1−cos(phi), so the model reduces continuously to the cosine
potential up to a scalar. The scalar does not affect transition frequencies.
The selected family assumes one shared transparency. It does not infer a
channel distribution, junction area, superconducting gap or channel count.
The current–phase relation obtained by differentiating the potential is
proportional to tau sin(phi)/sqrt(1−tau sin²(phi/2)). No higher harmonic is
independently fitted.

Parameters are positive except ng, with 0<=tau<=.99. Counterrotating cavity
terms remain in the Hamiltonian. Its quadratic stability condition is
4 EC>G²/Omega, satisfied at the selected point. Completing the photon square
leaves (4 EC−G²/Omega)n² plus the linear offset term and a bounded potential;
the calculation is not using an unstable quadratic circuit. Numerical cutoff
checks below are not a proof of truncation-error bounds for its infinite domain.

Canonical quantum mechanics, the Andreev law, one-transparency restriction,
charge-to-device mapping, cavity coupling, offset convention, preparation and
readout are all imports. Dissipation, finite-drive line shifts and microscopic
junction disorder are not derived or fitted away by this calculation.

## Measurements, preparation and declared split

The source is the ENS row of `results/Experiment.csv` at upstream commit
`d97280c61c54ca8d54ccf0a8706713130778eb63`, obtained through
[Juelich DATA](https://doi.org/10.26165/JUELICH-DATA/LGRHUH) for
[Willsch et al.](https://doi.org/10.1038/s41567-024-02400-8).
The committed copy has SHA256
`0b6abf45a5b574f2ecc492b19560d44ff1638894a0579504dc850c1cb628a01b`.
No source-author fitted parameter table is used as a numerical input.

The ENS device and its measurement protocol are described by
[Lescanne et al., Physical Review Applied 11, 014030](https://doi.org/10.1103/PhysRevApplied.11.014030).
Level j is prepared by j-photon pulses near f0j/j; Ramsey detuning tests check
the transition index. Cavity spectroscopy after that preparation associates a
resonance with the transmon level. Thus `fres1` means transmon level0, `fres2`
level1, and `fres3` level2. Preparing the fifth calibration observable needs
f02, already in calibration, rather than any higher evaluation transition.
The model's cavity observable is the dressed photon0→1 energy difference at
fixed bare-transmon label; transmon observables are dressed photon0-sector gaps.

| Calibration input | GHz |
|---|---:|
| f01 | 5.354767 |
| f02 | 10.5356 |
| fres1 | 7.76131 |
| fres2 | 7.75608 |
| fres3 | 7.75135 |

The five fitted parameters are EC,EJ1,Omega,G,tau. The baseline fits only the
first four inputs with tau fixed to zero. f03..f06 and fres4..fres7 are withheld
from both objectives, starts, model selection and stopping conditions. Baseline
fres3 is unused information for that model but becomes a fitted input for the
extension; it is not counted as an improved prediction of the extension.

Prior exposure to the full CSV, published harmonic discrepancies and earlier KIT
results is disclosed. The local protocol was recorded before this fit, but this
is not preregistration before seeing the dataset. An arithmetic mean of ng=0
and ng=.5 transition frequencies is an explicitly supplied benchmark convention.
Lescanne's parity switching and drifting background charge do not establish
that exact pair of charge endpoints as the experimental mean.

## Calibration and nominal evaluation

Declared starts use EC=.18,EJ1=20,Omega=7.75,G=.1 and tau=.01,.2,.6.
Bounds are [.03,1],[1,100],[7,8.5],[.001,1],[0,.99], respectively. Least squares
uses residual divisors [1,2,1,1,1], 200 evaluations and 1e−12 stopping tolerances.
An exact-calibration numerical solution requires residuals below1e−7GHz.
The .2 start converges; the .01 and .6 attempts hit their evaluation limits and
are preserved as unsuccessful searches, not alternative exact roots. Selection
uses calibration cost only. Global uniqueness is not proved.

The selected parameters are approximately

    EC=.1841990760792327, EJ1=21.829772186093592,
    Omega=7.738912856323958, G=.18858878602560333,
    tau=.15464897201354028.

At this point the five calibration residuals are below1e−12GHz. Derived potential
ratios are +.0104917249 cos(2phi) and −.00022017684 cos(3phi), in units of EJ1.
They are consequences of the calibrated shape, not independently measured
transparency or direct predictions of the framework.

| Unused drive | Cosine, four inputs: error MHz | Andreev shape, five inputs: error MHz |
|---|---:|---:|
| f03/3 | +.796329 | −.218231 |
| f04/4 | +2.898695 | −.389980 |
| f05/5 | +6.238759 | −.951250 |
| f06/6 | +11.008222 | −2.323107 |

Errors are prediction minus measurement. The four unused cavity errors fres4..7
at the primary cutoff are −.019387,+.033543,−.546382,−.789351MHz. The third
harmonic and later harmonics have not been adjusted to these results.

## Numerical checks and remaining uncertainty

Primary truncations are n=−16..16, 14 bare transmon eigenstates, 9 photon states
and 4096 Fourier samples. Increasing to n=−20..20,18 transmon states,12 photons
and8192 samples changes the extended-model frequencies by at most37.21Hz.
A separately implemented direct charge⊗photon Hamiltonian uses raw-square-root
binomial/cos-power Fourier coefficients rather than the primary FFT construction
and transmon-subspace reduction. It agrees with the fine primary results within
.001Hz. Original independent cutoffs through57 charges×18 photons and sampled
coupling continuation reproduce14 distinct labels, minimum dominant overlap
about.91548. Both implementations use SciPy eigensolvers; this is independent
construction, not an independent experiment or an interval certificate.

The scaled calibration Jacobian condition number is about203000. Perturbing the
fifth input by±1kHz moves f06/6 by approximately±.123MHz. At±10kHz the nominal
f06/6 residual becomes approximately−3.562 or−1.094MHz. No such perturbation
is selected to minimize an evaluation error.

All32 corners of the five printed-decimal half-unit rounding box are tested:
halfwidths [.0000005,.00005,.000005,.000005,.000005]GHz. Corresponding16-corner
controls are run for the cosine baseline's four inputs.

| Unused drive | Cosine corner range, MHz | Extended corner range, MHz |
|---|---:|---:|
| f03/3 | [.743,.850] | [−.444,.007] |
| f04/4 | [2.813,2.984] | [−1.043,.258] |
| f05/5 | [6.116,6.361] | [−2.334,.415] |
| f06/6 | [10.842,11.174] | [−4.874,.182] |

These are rounded summaries of sampled extrema, not outward-certified interval
endpoints. Improvement persists in those finite controls, which do not supply
measurement error bars, covariance, statistical confidence or a continuous box
bound. Actual systematic uncertainties are unavailable in the inspected sources.
The original protocol's1MHz comparison scale is not established as ENS accuracy;
three sub-MHz point residuals do not establish agreement within measurement error.

For legacy coordinate pairs (ng,ng+.5), samples at ng=.125,.25 move the f06/6 center by
less than.0032MHz but the fres7 center by up to.929MHz. Its endpoint halfspread
is1.036MHz, larger than its nominal mean residual. No robust precision claim is
made from that highest cavity mean. These legacy coordinate pairs are not exact
physical parity pairs under G n(a+a*); the displacement below corrects that
interpretation without overwriting the original numbers. Neither sampled center shifts nor endpoint
halfspreads are error bars or proven extrema over all charge configurations.

## Physical charge convention and unused Ramsey observable

The additional target is the parity splitting of the prepared ground-to-sixth
level Ramsey coherence. Its data were not used in any calibration above.
The short-junction parameters and all rounding-corner parameters are fixed
before reading the new digitized figure values. This is a retrospective
comparison, not a blinded prediction.

**Exact convention identity.** For EC>0, Omega>0 and
`delta=G^2/(4 EC Omega)<1`, define the periodic physical-offset model

    H_phys(q)/h = 4 EC(n-q)^2 + V_tau(phi) + Omega a* a + G(n-q)(a+a*).

Its gap spectrum equals the old model's at `ng=(1-delta)q`. To prove this,
substitute `a=b+Gq/Omega`. The oscillator-linear terms combine to `G n(b+b*)`;
the charge terms become `4 EC n^2 - 8 EC q(1-delta)n + 4 EC q^2(1-delta)`.
Completing that square gives the old Hamiltonian at `(1-delta)q`, plus the
scalar `4 EC q^2 delta(1-delta)`. This unitary identity is exact in the full
oscillator space. Finite Fock cutoffs are not exactly displacement invariant;
the direct numerical checks below address selected truncations.

Integer charge translation gives physical period one. The even real potential,
charge reflection and oscillator parity give even gap spectra in q. Thus the
physical parity pair is `(q,q+.5)`, mapped to an old-coordinate step
`(1-delta)/2`, and its splitting vanishes at q=.25. These statements concern
the supplied stable Hamiltonian and continuously assigned energy branches;
they do not specify measured charge occupation or switching dynamics. At G=0
the two conventions coincide. The unstable quadratic domain is not used.
The identity needs only the stated periodic potential and oscillator algebra;
physical identification with the measured circuit remains an imported premise.

The physical-convention mean shifts the five original calibration values by
about .0012 Hz or less in the tested computation, near numerical subtraction
scales and negligible at the reported calibration precision. It shifts the
full f06 endpoint splitting by about337 Hz for the Andreev snapshot and53 Hz
for the cosine snapshot. No parameters are recalibrated using Ramsey data.

**Preparation and observable.** Lescanne's Appendix C prepares the g/e6
superposition using two six-photon pi/2 pulses separated by variable delay,
then measures sigma_z. For a common drive f_d, signed free-evolution detunings
are `d_a=f06(q)-6 f_d` and `d_b=f06(q+.5)-6 f_d`. Their difference is the full
energy-frequency parity splitting; it must not be divided by six. Positive
Fourier peaks give `|d_a|,|d_b|`. Their separation is at most `|d_a-d_b|`, with
equality for same-sign detunings. Opposite-sign detunings instead give the sum
of the positive peak frequencies. Sign and offset trajectories are not given
numerically by the source and are not fitted here.

Author extraction used six predeclared times,20,40,60,80,100,120min, with
neighboring-time controls. The40 and120min slices were subsequently selected
for independent digitization and the committed comparison after those readings
were available; they were not a separately blinded selection. All six times and
controls remain in `ramsey_author_profiles.json`. Independent vector-registered
source-bin averages locate peaks near8.789 and11.111MHz, about2.3MHz apart.
The source bins are about.332MHz wide. Allowing centers within the selected
rows yields a geometric separation range about1.99–2.65MHz. This is a plot-bin
localization illustration, not an experimental confidence interval or complete
measurement-error bound. Pixel oversampling does not improve source precision.
The committed digitized contrasts and coordinates are declared observations;
the runner consumes them and does not claim to redigitize the source PDF.

Willsch2024 identifies ENS as the same device as Lescanne2019. Identical
cooldown, acquisition conditions, calibration epoch and systematic shifts
between the later table and the earlier parity trace are not established.
That cross-acquisition identification is an explicit comparison assumption.

| Fixed model | Numerical parity maximum, MHz | Printed-decimal corner endpoint range, MHz |
|---|---:|---:|
| Cosine, four calibration inputs | .544477 | .540476–.548504 |
| Andreev shape, five calibration inputs | 3.464585 | 2.586015–4.596982 |

The figure's separation scale lies above the cosine numerical range and
inside the Andreev numerical range. Under same-sign detunings and continuous
physical branches, the latter's nonzero endpoint and quarter-offset zero
supply an existence argument for a compatible offset. No particular offset,
time trace, sign or statistical match is predicted. This additional capacity
comparison keeps the differing calibration counts explicit. It identifies
neither the microscopic correction uniquely nor a native framework prediction.

The runner computes65physical offsets over one period and four bounded
searches partitioning[0,.25], explicitly comparing interval endpoints. These
are sampled/refined numerical maxima, not rigorous continuum upper bounds.
The16/32 rounding controls compute endpoints only, not continuous maxima for
every parameter in a box. Four finer charge/device/photon controls change
f06 by less .003Hz. Independent direct charge-photon matrices implement
`G(n-q)X` directly and verify the displacement-based predictions at q=0,.25,.5.
Source extraction, gauge algebra and selected independent full-basis checks
were reviewed separately; those checks do not turn overlap labels into
experimental preparation or figure binning into calibrated uncertainty.

## Review record for the Ramsey extension

The previous numerical spectra and failed calibration starts remain intact.
The interpretation of legacy `(ng,ng+.5)` controls is narrowed: physical
parity uses the displaced step derived above. The new signal comparison adds
an independently inspected published observable and no fitted parameter.
The committed review records under the existing loop pack identify original
exploratory sources; the live primary runner now recomputes calibration and
parity predictions from this PR's own sources. Formal status remains unaudited.
No negative theorem, certified global bound or exclusion of alternative
models is proposed; the result is the displayed fixed-model comparison.

## Reproduction, checks and next obligation

Run `python3 scripts/ens_cavity_holdout_2026_09_27.py`. Complete computed arrays
are written to `outputs/ens_cavity_holdout_2026_09_27.json`; the canonical cache
prints a compact summary and the full output hash. The primary runner refits
all declared starts, preserves failed attempts, constructs predictions from only
the calibration dictionary, checks an independent direct model, evaluates
sensitivity/rounding/offset controls, and only then converts evaluation data to
numbers. It does not read the historical fitted parameter file. The pinned
measurement CSV and declared digitized Ramsey bins are the experimental
numerical inputs. Its PASS categories
are computational checks and a reproduced nominal comparison, not a verdict
that measured physics or a TOE has been confirmed.

The next obligation is physical identification and quantified experimental
uncertainty, not another parameter chosen using the unused residuals. The
separately calibrated shape improves a reproducible measured comparison, while
its mechanism, parameter uniqueness and native framework derivation remain open.

```yaml
target_claim_type: open_gate
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Numerical imported-model comparison with explicit physical-identification and uncertainty gates; no exact spectral theorem or empirical confirmation is claimed.
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: Compare unused measured physics after fixing correction parameters using separate calibration observables.
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: frontier_probe
next_trace_action: Identify the correction mechanism and experimental uncertainty independently; preserve residuals and calibration limits.
```
