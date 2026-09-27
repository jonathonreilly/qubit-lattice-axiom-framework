---
claim_id: ens_cavity_calibrated_holdout_open_gate_note_2026-09-27
claim_type: open_gate
claim_scope: "Retrospective numerical ENS comparison using five calibration observables and an imported single-transparency circuit model; no native TOE derivation, unique mechanism identification, statistical validation, or general exclusion."
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

For paired offsets (ng,ng+.5), samples at ng=.125,.25 move the f06/6 center by
less than.0032MHz but the fres7 center by up to.929MHz. Its endpoint halfspread
is1.036MHz, larger than its nominal mean residual. No robust precision claim is
made from that highest cavity mean. Neither sampled center shifts nor endpoint
halfspreads are error bars or proven extrema over all charge configurations.

## Reproduction, checks and next obligation

Run `python3 scripts/ens_cavity_holdout_2026_09_27.py`. The primary runner refits
all declared starts, preserves failed attempts, constructs predictions from only
the calibration dictionary, checks an independent direct model, evaluates
sensitivity/rounding/offset controls, and only then converts evaluation data to
numbers. It does not read the historical fitted parameter file. The pinned
measurement CSV is the sole experimental numerical input. Its PASS categories
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
