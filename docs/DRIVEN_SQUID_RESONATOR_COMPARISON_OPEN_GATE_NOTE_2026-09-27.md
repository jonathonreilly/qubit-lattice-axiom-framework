---
claim_id: driven_squid_resonator_comparison_open_gate_note_2026-09-27
claim_type: open_gate
claim_scope: "Exact oscillator displacement for a supplied driven circuit, and a retrospective resonator comparison at supplied calibration snapshots; numerical diagnostics, not native TOE confirmation or statistical model exclusion."
upstream_dependencies: []
runner: scripts/driven_squid_resonator_2026_09_27.py
---

**Type:** open_gate
**Status:** conditional-support; author proposal awaiting independent audit.

# Driven SQUID displacement and reserved resonator centers

A periodic oscillator displacement converts the supplied cavity drive into a
charge drive exactly in the infinite oscillator. At one declared calibration
snapshot, the selected avoided-quasienergy-gap shift is about +6.181683 MHz.
Separately, a ground-state cavity calculation at two supplied driven-calibration
snapshots gives about 36.453 and 37.235 kHz RMS residuals on twenty measured
resonator columns excluded from the earlier center calibration. These are
constructive calculations and numerical observations within an imported model.
The experimental preparation and readout identification remain open.

## Model, preparation and observables

Use ordinary quantum charge and photon spaces and cyclic GHz units. Let n be
integer, f the supplied dimensionless flux, J_left=J(1+a), J_right=J(1-a), and

    H_device/h = 4 EC(n-ng)^2
      - J_left cos(phi) - J_right cos(phi+2 pi f)
      + [J_left^2 cos(2phi)+J_right^2 cos(2phi+4 pi f)]/(4 EL).
    H(t)/h = H_device/h + Omega a_dagger a + G n P + D X cos(2 pi w t),
    P=i(a_dagger-a), X=a+a_dagger.

The second harmonic is the supplied leading series-inductance correction,
with per-arm geometry L=10.2 pH and EL=(hbar/2e)^2/(h L), expressed in GHz.
It is not an independently adjustable harmonic. The rotor potential, canonical
quantum mechanics, geometry-to-circuit identification and all fitted EC,J,a,G
are imports. The publication input snapshots explicitly supply their values.
No framework axiom or primitive is changed or used to derive these quantities.

The undriven observable is the difference of two full coupled eigenvalues,
selected by largest overlaps with bare device ground times photon vacuum and
one photon, minus Omega, plus a supplied fitted offset. It assumes the device
starts in its ground state. Actual thermal preparation and the mapping from
this frequency to the measured finite-width resonator dip are not independently
established here. The two charge offsets ng=0 and ng=0.5 are retained separately.

The driven observable is a local avoided-quasienergy-gap minimum, not a
computed dissipative spectroscopy peak. The drive normalization uses the
source's 50 ns cosine-envelope pulse, pi-amplitude 0.411 and spectroscopy
amplitude 22 dB lower, and this model's own cavity-X transition matrix at
f=0.5035: D=10^(-22/20)/(0.411*50*|X_ge|) in GHz. Pulse-area interpretation,
frequency-independent transfer, population preparation and readout are supplied
assumptions. The source-author fitted drive amplitude is not a numerical input.

## Exact displacement and proof obligations

**Target:** For the supplied oscillator, Omega not equal to positive drive
frequency w, a periodic displacement preserves quasienergy differences and
replaces D X cos(2 pi w t) by F n sin(2 pi w t), where
F=2 G D w/(Omega^2-w^2).

Write theta=2 pi w t and the state as psi=D(alpha) chi. The oscillator identity
D(alpha)^dagger a D(alpha)=a+alpha is the first lemma, used on the usual
oscillator domain. Cancellation of linear oscillator terms gives

    i dot(alpha)/(2 pi) = Omega alpha + D cos(theta),
    alpha = -D/2 [exp(-i theta)/(Omega-w)+exp(i theta)/(Omega+w)].

Substitution verifies the second lemma, the bounded periodic forced solution.
Since P transforms to P+2 Im(alpha), the third lemma is the displayed positive
charge-drive coefficient F. All device operators commute with the photon
displacement. The scalar term has mean -D^2 Omega/[2(Omega^2-w^2)]. Its periodic
part is removed by a periodic scalar phase; its mean shifts all quasienergies
equally. This proves the target about differences, not equality of absolute
quasienergies with an omitted scalar. D=0 is the trivial limit. The resonant
case Omega=w is outside this bounded-periodic construction.

These lemmas are derived here from imported canonical oscillator algebra.
Arbitrary finite ladder truncations do not satisfy that algebra exactly; the
runner's convergence comparisons are numerical diagnostics rather than an
infinite-basis error certificate. The strongest missing bridge for an empirical
drive prediction is a source-justified dissipative preparation/drive/readout
model relating the local gap minimum to the measured line center. The proven
identity does not assume or establish that bridge.

## Measured inputs and calibration separation

The measured source is [Kim et al.](https://www.nature.com/articles/s41567-026-03285-5),
published Fig.3f and its
[source workbook](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41567-026-03285-5/MediaObjects/41567_2026_3285_MOESM12_ESM.xlsx).
The plotted frequency axis is MHz offset from 7.6918 GHz. The source workbook
identity and extraction lineage are pinned in the
[provenance record](../data/driven_squid_resonator_2026_09_27/provenance.json).
The committed [measured columns](../data/driven_squid_resonator_2026_09_27/measurements.json)
contain the full 55-point signal of each reserved column, not source-author fit
curves. The runner refits a Lorentzian dip with linear background and repeats
with a Gaussian dip, without consulting a physics prediction in either fit.

The supplied [snapshots](../data/driven_squid_resonator_2026_09_27/inputs.json)
come from earlier author calibration using 75 qubit-ridge observations at
f<=0.480, one separately reclassified outer-edge qubit observation, and 22
resonator columns 0,20,...,400 plus197. The evaluation columns are
10,30,...,390. There was prior image/source-context exposure: this is
retrospective numerical separation, not blind validation. The primary runner
propagates the snapshots; it does NOT reproduce or validate the preceding
optimizer, infer parameter covariance, or claim independently measured circuit
coefficients. Raw calibration reconstruction is outside this narrow packet.
The calibration protocols and their historical source hashes are preserved in
the review pack as provenance, not prerequisites for executing this comparison.

The nominal snapshots used a self-consistent closed-system drive correction in
the qubit calibration. Six additional supplied snapshots represent all three
starts at each charge offset for a retrospective calibration-only relative
flux-axis coordinate, using the older undriven objective. They are propagated
as explicit alternative assumptions, not selected by evaluation residuals.
The 20 MHz qubit and 20 kHz resonator calibration scales were numerical weights,
not experimental standard deviations. The axis reference does not independently
establish the bare resonator frequency used in the Hamiltonian.

## Numerical observations and errors

At the drive reference snapshot, photon cutoff7, device charge cutoff32 and14
bare device levels, displaced Floquet sizes40/4 and70/6 (dressed levels/sidebands)
reproduce the local shift about6.181683MHz. Earlier independent continuous-time
monodromy, with its own direct charge-photon construction, gave6.1816829728MHz;
that value is an explicit numerical regression anchor, not an experimental
target. The historical original-frame larger-cutoff calculation agreed within
0.414Hz. These selective historical checks used the same physical inputs and
had access to author results. Current publication-code review is recorded in
the packet, separately from those historical checks.

At charge cutoff40,24 device levels and7 photon levels, the nominal resonator
RMS residuals are36.453/37.235kHz for ng=0/0.5. Column50 residuals are
+108.149/+108.519kHz; column250 residuals are+114.807/+120.441kHz. Independent
historical direct charge-photon calculations checked those four values; the
primary runner tests explicit regression anchors with a1Hz tolerance. This
is implementation regression, not a confidence bound. All twenty residuals
and label weights are emitted, with no target-based rejection.

Changing the extraction shape moves centers by at most2.642kHz. This is a
sensitivity diagnostic, not an uncertainty estimate. The six relative-flux
snapshots give column50 about+113.27..+113.62kHz and column250 about+17.18..+28.98kHz.
Their differing responses matter: the nominal discrepancies have different
sensitivity to this particular calibration assumption. The added coordinate
was explored after the evaluation discrepancies were known. No statistical
significance, unique physical cause, all-model exclusion or native TOE
confirmation is inferred from these observations.

## Imports and trace

| Input | Role and provenance | Open physical identification |
|---|---|---|
| Canonical rotor and oscillator dynamics | Conventional supplied Hamiltonian above | Framework-to-device derivation is outside this result |
| Geometry and fitted snapshots | Source inductance plus pinned author-calibration output | Microscopic capacitance/impedance and parameter errors |
| Pulse settings | Published supplementary Rabi settings | Transfer and pulse-area identification |
| Measured dip signals | Source workbook, copied measured columns | Preparation and observable-to-instrument relation |
| Numerical anchors | Selective independent computations in historical review | Finite-domain checks, no statistical interpretation |

The downstream consumer is a future preparation-to-observable measured-physics
chain. This artifact supplies a drive reduction and a concrete empirical
comparison for that chain; it does not confer framework authority on the
imported model. The registered units, kinetic-isotropy and realized-state
primitives are not missing premises of this calculation and are not relabeled
as circuit dynamics or empirical calibration.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: open_gate
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: frontier_probe
next_trace_action: "Specify a justified preparation and readout model or an independent microscopic calibration before another empirical prediction."
conditional_surface_status: "Supplied circuit and calibration snapshots"
hypothetical_axiom_status: null
admitted_observation_status: "Measured resonator columns are comparison data"
claim_type_reason: "Constructive oscillator identity and retrospective comparison with explicit physical identification still open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review record and execution

The [primary runner](../scripts/driven_squid_resonator_2026_09_27.py) imports a
[direct-basis comparison helper](../scripts/driven_squid_independent_2026_09_27.py)
and otherwise requires NumPy/SciPy and its three declared data files. The helper
uses phase quadrature and the full finite charge-photon basis to check column250
for all six alignment snapshots, with a1Hz numerical agreement check. It performs scientific
reads of snapshots and measured signals, plus integrity reads of their hashes
in provenance. Its declared closure also binds the imported helper source. It has no runtime dependency on prior PRs, local recovery paths,
raw source workbooks, gitignored audit data or historical exploratory scripts.
The physics comparison is proposed as open_gate; this author note sets no audit
verdict. No broader negative claim or bounded-with-walls classification is
proposed. Historical perturbative drive and nominal-pair interpretations are
superseded only within the explicit numerical domains described above.

The review packet is `.claude/science/physics-loops/driven-squid-resonator-20260927/`.
Run `python3 scripts/driven_squid_resonator_2026_09_27.py`; create canonical cache
through `scripts/runner_cache.py`. Full current-main integration gates remain
required before landing. No author merge is authorized by this artifact.
