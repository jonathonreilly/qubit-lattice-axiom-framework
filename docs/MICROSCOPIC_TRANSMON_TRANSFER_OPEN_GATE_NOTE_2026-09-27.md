---
claim_id: microscopic_transmon_transfer_open_gate_note_2026-09-27
claim_type: open_gate
claim_scope: "Conditional rectangular-junction spatial averaging and retrospective third-level transfer from supplied low-level calibration snapshots; no native TOE confirmation or statistical precision claim."
upstream_dependencies: []
runner: scripts/microscopic_transmon_2026_09_27.py
---

**Type:** open_gate
**Status:** conditional-support; supplied-model comparison, unaudited.

# Rectangular-junction harmonics and third-level transmon transfer

A uniform rectangular junction multiplies its mth local Josephson harmonic by
signed sinc(m B/Bnode). Applying that derived spatial average to a supplied
two-junction circuit gives a concrete retrospective comparison with a measured
third-level transition. For the lowest-cost raw Ramsey calibration return,
the full f03 center is 14.669197761379 GHz: 0.432226 MHz above the processed
source center and about 1.489438 MHz above an alternative raw line extraction.
Both measurement versions are retained. The matched replacement of the mth
harmonic envelope by the fundamental envelope changes this prediction by
+0.195467 MHz after the same low-level recalibration.

This is a conditional imported-circuit calculation. It improves a concrete
comparison while exposing the importance of calibration and measurement
extraction. It does not establish precision agreement, independent microscopic
parameter identification, or native TOE confirmation. All evaluation data had
already been exposed when this construction was selected. The calibration
objectives exclude the third-level measurements, but that does not make this
a blind model-selection experiment.

## Preparation, dynamics and observable

Use the ordinary integer charge space and a photon oscillator, with cyclic GHz
units. Let q be the offset charge and n its conjugate integer charge operator:

    H/h = 4 EC (n-q)^2 + V(phi) + Omega a_dagger a
          + G (n-q) (a+a_dagger).

The conditional preparation is the coupled eigenstate assigned to
the isolated device ground state and cavity vacuum by the largest-overlap
rule at each sampled q. Continuous adiabatic tracking is not checked. Evolution is
the canonical unitary exp(-i 2 pi (H/h) t), with t in ns. For an infinitesimal
probe the candidate transition frequencies are eigenvalue gaps identified by
largest overlaps with the isolated device levels and photon vacuum. The
runner checks unique labels; finite cutoffs are numerical approximations.

For each gap f0j, the reported center is [f0j(0)+f0j(1/2)]/2 and full charge
dispersion is |f0j(0)-f0j(1/2)|. Identifying those quantities with measured
Ramsey or CW-fit centers requires a parity/charge-sampling and readout model.
The actual acquisition is not asserted to realize this ideal preparation or
weak-probe limit. The archived173536 drive axis is used as the full-f03 frequency. A hypothetical
three-photon implementation would instead use f03/3; no such division is
applied to this record.

## Spatial derivation and hypotheses

**Target:** A spatially uniform local harmonic on a rectangular junction with
linear imposed phase acquires signed sinc(m B/Bnode), and two such arm
potentials add with relative phase exp(i m psi).

Assume negligible self-field and screening, uniform field and local harmonic
density, and x in [-L/2,L/2] with phase phi+2 pi (B/Bnode) x/L. For integer m,

    (1/L) integral exp[i m (phi+2 pi (B/Bnode) x/L)] dx
      = exp(i m phi) sinc(m B/Bnode),
    sinc(z) = sin(pi z)/(pi z), sinc(0)=1.

Integration proves the first identity. Adding the second arm shifted by psi
proves the second. If c_m are Fourier coefficients of the normalized local
potential, the charge-basis hopping at signed order m is

    c_|m| [Ja sinc(|m| B/Ba) + Jb sinc(|m| B/Bb) exp(i m psi)].

The opposite hopping is its complex conjugate. A diagonal constant is removed.
At psi=pi odd harmonics subtract and even harmonics add algebraically; signed
envelopes do not imply magnitude enhancement. This argument does not require
a nonzero total fundamental. Ratios or a phase rotation defined by that
fundamental would require it to be nonzero. The zero-field and zero-order
limits use the continuous sinc value. Arbitrary nonuniform current density
and finite screening are outside the declared construction, not excluded
physical alternatives.

For the local short-channel model define s=sin²(phi/2),
r_tau(phi)=4s/[1+sqrt(1-tau s)], and normalize its Fourier coefficients by
minus twice its first coefficient. This fixes the local fundamental to
-cos(phi); constants are irrelevant. At tau=0 it reduces continuously to a
cosine. The square-root potential, shared local transparency tau and canonical
charge quantization are imported physics, not consequences of TOE primitives.

The proof obligations are: spatial integration (proved above), arm superposition
(proved above), Fourier/charge representation (canonical imported machinery,
checked by independent direct-phase projection), converged coupled spectra
(selected numerical checks), and identification with the measured preparation
and line center (open). The strongest missing empirical bridge is a calibrated
preparation/drive/readout model with an uncertainty budget. It is not an
assumption used to prove the spatial identity.

## Inputs, provenance and calibration separation

The experiment is the Krause device record in Krause et al., arXiv2403.03351v1,
and its source archive DOI10.5281/zenodo.10728469. Final-journal equivalence is
not assumed. Upstream source identities and packaged snapshots are recorded in
`data/microscopic_transmon_2026_09_27/`; external documents are provenance,
while the runtime computation depends only on included data and scripts.

The geometric assumptions are B=0.15 T, Ba=0.8 T, Bb=0.8*256/178 T, and
Ja/Jb=(256*257)/(178*143), giving alpha=(Ja-Jb)/(Ja+Jb)=0.442079652807.
The widths and areas are AFM notebook values. Converting physical areas into
critical-current ratio assumes equal current density, common active area and
shared transparency. Ba uses a conditional interpretation of high-field cavity
modulation collapse; Bb uses common magnetic thickness and the width ratio.
These are not independent electrical metrology or measured uncertainty bounds.
The paper supports intended bottom-sweet-spot operation for the example field;
exact psi=pi and stability across acquisitions are additional assumptions.

Omega=7.544917319789201 GHz and G=0.07352541358551871 GHz are supplied from a
27-coordinate low-level photon-number calibration under a cosine model.
An earlier 28th table entry was the constructed expression
2*7.0915-7.1095=7.0735 GHz and was removed before that calibration. This
source correction is preserved; the supplied constants remain model- and
cross-acquisition-dependent, not independent device constants.

EC, Jsum=Ja+Jb and tau are calibrated to f01 and f12 centers and full f01
dispersion. The cosine control has tau=0 and uses only the two centers; the
comparison is not an equal-objective likelihood test. No f03 or delta03 value
enters these objectives. Three inputs for three shape parameters do not
provide an overidentifying empirical test. Calibration optimizers are not
reproduced by the publication comparator: it propagates and checks supplied
snapshots. Historical fits and raw extraction checks are review evidence with
that narrower status.

Five calibration versions are all retained. Two use archived versus processed
analysis of the same 074423 Ramsey acquisition. Three use a raw-only reanalysis
with initial gate periods 0.15, 0.22 and 0.30 V, yielding full f01 splittings
61.215, 111.396 and 111.498 kHz and raw objective costs 2.30693, 1.81808 and
1.81794. The two lower-cost returns support the processed splitting near
108.415 kHz over the archived 189.181 kHz within that raw model. All three
returns, including the poorer basin, are propagated. The 0.15 V start hits its evaluation limit and is retained as a failed-fit
diagnostic. The other two terminate by ftol above gradient tolerance. Unknown
noise/stationarity remain relevant; no
confidence or global-optimum claim follows.

The f12 input is the archived center 4.912700039843716 GHz from 161812.
Acquisitions are separated by hours and charge-offset drift is documented.
This is not a simultaneous common-parity preparation. The exact third-level
record is 20220729-173536-429-b495bf. Its processed center is
14.668765535362667 GHz, fit-only standard error 0.250398 MHz; processed full
dispersion is 41.322465074874 MHz, fit-only error 0.659798 MHz. A raw scalar-S21
two-Lorentzian extraction using all 31*120 bins and three declared width starts
gives centers 14.667708320327–14.667708323506 GHz. Few-Hz agreement among those
starts is numerical stability, not measurement precision. No raw full-dispersion
estimate is used. The approximately 1.057 MHz extraction difference is preserved,
not resolved by choosing whichever center agrees with theory.

## Comparisons and matched mechanism control

For shape start 0.01, full f03 center residuals against the processed target are:

| Calibration version | Center residual (MHz) | Full dispersion residual (MHz) |
|---|---:|---:|
| Archived 01 analysis | -9.953473 | +16.249573 |
| Processed 01 analysis | +0.930015 | -3.526868 |
| Raw period start 0.15 V (not converged) | +10.073133 | -16.929541 |
| Raw period start 0.22 V | +0.448572 | -2.738574 |
| Raw period start 0.30 V | +0.432226 | -2.711563 |

The cosine center residual is about +24.45 MHz. Improvement belongs to the
complete conditional model and extra low-level calibration, not solely to the
spatial envelope. Against all three raw03 centers, the raw calibration cases
give approximately +11.130345, +1.505784 and +1.489438 MHz respectively.
All shape starts and cosine controls are carried in the runner, not just the
rows displayed here. Residual proximity is an observation, never a PASS gate.

The earlier raw analysis mistakenly treated the final two readout-reference
samples as Ramsey delays. Exact processed populations identify them as
calibration 0/1 at every gate. The current raw calibration uses 265 genuine
delays per gate, preserving the two reference I/Q values separately. Exclusion
is based on source semantics, not residual pruning. The old 267-sample results,
including their apparently good numerical checks, are retained as historical
mixed-observation calculations and do not support the current physical
calibration claim. Independent reconstruction now verifies all 16,430 genuine
delay residuals for each corrected raw outcome.

A matched control replaces sinc(m B/Bnode) by sinc(B/Bnode) in each local
harmonic, then recalibrates against the identical low-level inputs. All twelve
raw cases are retained. The three cosine controls coincide within the runner's numerical tolerance. For the three raw calibration versions, ablation
minus spatial f03 is +0.082974, +0.195255 and +0.195467 MHz, while full delta03
changes by -0.006435, -0.021529 and -0.021564 MHz. This is a change with
recalibration, not a fixed-parameter derivative. It isolates a much smaller
magnetic-envelope effect than the entire model comparison.

## Error accounting and review record

Independent raw-phase spatial quadrature and full charge-photon diagonalization
check selected archived/processed snapshots and the raw0.30 spatial/ablation
pair. The runner reports the differences and stronger-cutoff changes for the
current corrected pair. These are selected floating-point controls, not
infinite-basis certificates, optimizer reproduction or blanket
independent coverage of all snapshots. Calibration-version variation, line
extraction variation, unmeasured geometry/phase uncertainty, finite-drive
response and cross-acquisition drift are distinct from numerical errors.
There is no justified combined statistical error bar.

A bounded source inspection of exact spectroscopy snapshots finds that the
f03 generator frequency lies outside its raw frequency axis and the VNA is
recorded off. Cached control-pulse durations/amplitudes, instrument-level powers
and readout settings do not supply a synchronized executed drive calibration.
No quantitative AC-Stark correction was computed from those fields. A calibrated
spectroscopy-path response or independently controlled power series would add
new evidence; fitting a drive amplitude to remove the f03 residual would be
calibration to the target.

Author-side source and independent numerical checks support only the declared
construction and calculations. Formal independent audit remains required for
any effective retained classification. No prior framework claim is promoted or
primitive changed. No theorem excludes other microscopic mechanisms, and no
failure of a numerical fit is presented as a no-go result.

## Machine status and trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: open_gate
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: unknown_frontier
artifact_role: frontier_probe
next_trace_action: "Obtain independent electrical geometry and preparation/drive/readout constraints before a precision empirical comparison."
conditional_surface_status: "Supplied circuit, geometry premises, calibration snapshots and endpoint observation model."
hypothetical_axiom_status: "No new axiom proposed."
admitted_observation_status: "Measured low-level calibration and previously exposed third-level evaluation records."
claim_type_reason: "Constructive conditional calculation with an open empirical identification and uncertainty budget."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
