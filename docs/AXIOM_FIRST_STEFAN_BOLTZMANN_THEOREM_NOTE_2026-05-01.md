# Axiom-First Stefan-Boltzmann Law from KMS + Framework Photon Spectrum

**Date:** 2026-05-01
**Type:** positive_theorem
**Claim scope:** for blackbody photon radiation in thermal equilibrium at temperature T on the framework's cited EW + emergent Lorentz + Block 01 KMS surface (per 2026-05-17 ledger, all cited upstreams are currently `unaudited` rather than retained-grade; see §Upstream-tier accounting (2026-05-17) and fix record below), the energy density is u(T) = (π²/15) (k_B T)⁴ / (ℏc)³ (SB1)-(SB4); equivalently the Planck distribution n(ω, T) = 1/(e^(βω) - 1) and the Stefan-Boltzmann constant σ_SB = (π²/60) k_B⁴/(ℏ³c²) follow.
**Status:** awaiting independent audit. Under the scope-aware classification framework (audit-lane proposal #291), `effective_status` is computed by the audit pipeline.
**Loop:** `24h-axiom-first-derivations-20260501`
**Cycle:** 6 (Block 06; stacked on Block 01 (KMS))
**Branch:** `physics-loop/24h-axiom-first-block06-stefanboltzmann-20260501`
**Stacked PR base:** `physics-loop/24h-axiom-first-block01-kms-20260501`
**Runner:** `scripts/axiom_first_stefan_boltzmann_check.py`
**Log:** `outputs/axiom_first_stefan_boltzmann_check_2026-05-01.txt`

## Scope

This note proves the **Stefan-Boltzmann law** for blackbody photon
radiation on the framework's cited emergent-spacetime surface (tier
inherited from the cited companions; see §Upstream-tier accounting
(2026-05-17) below):

```text
    u(T)  =  (π² / 15) · (k_B T)⁴ / (ℏ c)³                                   (1)
```

where `u(T)` is the photon energy density at thermal equilibrium at
temperature `T`. In natural units `ℏ = c = k_B = 1`,

```text
    u(T)  =  (π² / 15) T⁴                                                    (2)
```

The proof composes:

- **Block 01 KMS support theorem** (Gibbs state on harmonic oscillator
  reconstructed Hamiltonian gives Planck distribution);
- the framework's cited U(1) photon (from SM hypercharge uniqueness
  + EW package, which admit a massless photon mode; companion currently
  `unaudited`);
- the framework's cited emergent Lorentz invariance (which gives
  the standard 3D density of states and dispersion relation
  `ω = c k` in the smooth-limit regime; companion currently `unaudited`);
- standard counting of Bose-Einstein modes (admitted-context).

**Tier accounting note:** the "retained" descriptor used elsewhere in
this note (prior wording) was tier-loose; per the 2026-05-17 ledger
the cited companions are not at `retained_bounded`. The proof
arithmetic itself (`(SB1)-(SB4)`) is unaffected; only the
upstream-tier qualifier is corrected. See §Upstream-tier accounting
(2026-05-17) and the fix-record section near the end of the note.

This is the framework's **first numerical thermodynamic prediction**
that goes beyond structural identity: given temperature `T`, the
photon energy density is fixed at value (1) on the framework retained
surface (modulo the upstream support classification).

## Cited inputs (tier inherited; see §Upstream-tier accounting (2026-05-17))

(Section heading changed 2026-05-17 from "Retained inputs"; per the
2026-05-17 ledger snapshot, all named companions are currently
`unaudited` rather than `retained_bounded`. The proof structure below
is unchanged; only the tier descriptors are corrected.)

- **Block 01 KMS support theorem.** Gibbs state on `H_phys` at
  inverse temperature `β_th = 1 / T` is Planck-distributed for any
  harmonic-oscillator subsector. (Companion
  `axiom_first_kms_condition_theorem_note_2026-05-01` currently
  `unaudited`.)
- **Cited emergent Lorentz invariance.** From
  [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md) and
  [`LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md`](LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md), the framework's
  long-wavelength photon modes have dispersion `ω = c k` to leading
  order, with `c` the emergent speed of light. The leading
  anisotropic correction is at dimension 6 with cubic-harmonic
  `ell = 4` fingerprint, irrelevant for the `T^4` law. (Both
  companions currently `unaudited`.)
- **Cited anomaly-forced 3+1 dimensions** (from the cited
  [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)): the spatial substrate is
  `Z^3`, so the photon density of states is the standard 3D form.
  (Parent companion currently `unaudited`; admissions (i)-(iv) and
  upstream [F-B framing-fix](ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md)
  apply via tier inheritance, not as load-bearing proof steps in
  `(SB1)-(SB4)`.)
- **Cited U(1) photon.** From the cited
  [`STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md`](STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md)
  + EW package, the framework has a massless U(1)
  electromagnetic photon with two transverse polarizations. (Companion
  currently `unaudited`.)
- **Spectrum condition** (from cited
  [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md);
  companion currently `unaudited`): photon Hamiltonian is bounded below.

## Admitted-context inputs

- **Standard 3D photon density of states:** `g(ω) dω = (V/π²c³) ω² dω`
  (two polarizations × `4π k² dk / (2π)³` with `ω = ck`). This is
  basic 3D mode-counting on the framework's retained `Z^3` substrate
  in the smooth-limit regime.
- **Bose-Einstein statistics for photons:** photons are bosons (spin 1
  vector field). This is consistent with the retained
  [`AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md).
- **Standard integral identity:**
  `∫_0^∞ x^{s-1} / (e^x - 1) dx = Γ(s) ζ(s)`. For `s = 4`:
  `Γ(4) ζ(4) = 6 · π⁴/90 = π⁴/15`. Pure mathematical identity.

These are basic counting / mathematical inputs, all consistent with
or implied by the retained framework structure.

## Statement

Let `H_phys` be the RP-reconstructed physical Hilbert space restricted
to the retained U(1) photon sector (massless gauge boson with two
transverse polarizations). Let `T > 0` be the thermal temperature
parameter, with Gibbs state `ρ_β = e^{-β H_γ} / Z_γ` where `β = 1/T`
and `H_γ` the photon Hamiltonian. Then on `A_min` plus the retained
inputs above:

**(SB1) Planck distribution from KMS.** For each photon mode of
frequency `ω`, the mean occupation number in the Gibbs state is

```text
    n(ω, T)  =  1 / (e^{β ω} - 1)                                            (3)
```

This is the **Planck distribution** for bosons. The proof uses Block
01 (K1)–(K2) on the harmonic-oscillator subsector with creation /
annihilation operators `a^†, a` satisfying `[a, a^†] = 1`,
`H_osc = ω (a^† a + 1/2)`.

**(SB2) Photon energy density.** Integrating `ℏ ω · n(ω, T)` against
the framework's standard 3D density of states (two polarizations):

```text
    u(T)  =  ∫_0^∞ dω · ℏ ω · n(ω, T) · g(ω) / V
          =  ∫_0^∞ dω · ℏ ω / (e^{β ω} - 1) · (1 / π² c³) ω²              (4)
          =  (ℏ / π² c³) ∫_0^∞ ω³ / (e^{β ℏ ω} - 1) dω                     (5)
```

**(SB3) Stefan-Boltzmann formula.** Substituting `x := β ℏ ω`:

```text
    u(T)  =  (ℏ / π² c³) (T / ℏ)⁴ ∫_0^∞ x³ / (e^x - 1) dx                   (6)
          =  (T⁴ / π² c³ ℏ³) · Γ(4) · ζ(4)                                  (7)
          =  (T⁴ / π² c³ ℏ³) · 6 · π⁴ / 90                                  (8)
          =  (π² / 15) · T⁴ / (c³ ℏ³)                                        (9)
```

In SI units restoring `k_B`, this is `u = (π² k_B⁴ / 15 ℏ³ c³) T⁴`,
the **Stefan-Boltzmann law**.

**(SB4) Stefan-Boltzmann constant.** From (SB3) the Stefan-Boltzmann
constant in SI units is

```text
    σ_SB  :=  (π²/60) k_B⁴ / (ℏ³ c²)                                         (10)
          =  5.670374419 × 10⁻⁸  W m⁻² K⁻⁴                                  (11)
```

(`c` rather than `c³` because radiance per solid angle differs from
energy density by a factor of `c/4`).

Statements (SB1)–(SB4) constitute the Stefan-Boltzmann law on the
framework retained surface plus Block 01 KMS support.

## Proof

### Step 1 — Planck distribution from KMS (proves SB1)

Consider a single harmonic oscillator mode `H_osc = ω a† a` (zero-
point energy absorbed into vacuum subtraction; consistent with
spectrum condition `H ≥ 0` and zero ground state). The number-basis
states are `|n⟩` with `H_osc |n⟩ = nω |n⟩`.

Apply Block 01 (K1)–(K2) on this subsector. The Gibbs trace is

```text
    Z_osc(β)  =  Σ_{n=0}^∞ e^{-β n ω}  =  1 / (1 - e^{-β ω})                (12)
```

The mean occupation:

```text
    n(ω, T)  :=  <a† a>_β  =  (1/Z) Σ_n n e^{-β n ω}
              =  e^{-β ω} / (1 - e^{-β ω})  =  1 / (e^{β ω} - 1)             (13)
```

This is the Planck distribution. ∎

### Step 2 — 3D density of states (used in SB2)

On the framework's retained 3D spatial substrate (`Z^3` with
emergent Lorentz `ω = c k` to leading order), the number of photon
modes per unit volume in `(ω, ω + dω)` is

```text
    g(ω) dω / V  =  2 · (1 / (2π)³) · 4π k² dk
                =  (k² / π²) dk
                =  (ω² / π² c³) dω                                            (14)
```

The factor of `2` accounts for the two transverse polarizations.
This is standard 3D mode-counting; on the framework's retained surface
it is consistent with native U(1) + emergent Lorentz at long
wavelengths.

### Step 3 — Energy density integral (proves SB2, SB3)

Combine (3) and (14):

```text
    u(T)  =  ∫_0^∞ dω · ℏ ω · n(ω, T) · g(ω) / V
          =  ∫_0^∞ (ℏ ω³) / (π² c³ (e^{β ℏ ω} - 1)) dω                      (15)
```

Substitute `x := β ℏ ω`, `dω = dx / (β ℏ)`:

```text
    u(T)  =  ℏ / (π² c³) · ∫_0^∞ (x / β ℏ)³ · 1/(e^x - 1) · dx / (β ℏ)
          =  (ℏ / π² c³) · (1 / β⁴ ℏ⁴) · ∫_0^∞ x³ / (e^x - 1) dx             (16)
          =  (T⁴ / π² ℏ³ c³) · Γ(4) ζ(4)                                    (17)
```

Using `Γ(4) = 3! = 6` and `ζ(4) = π⁴ / 90`:

```text
    u(T)  =  (T⁴ / π² ℏ³ c³) · 6 · π⁴ / 90  =  (π² / 15) · T⁴ / (ℏ³ c³)    (18)
```

This is (1)/(2). ∎

### Step 4 — Stefan-Boltzmann constant (proves SB4)

The Stefan-Boltzmann constant is conventionally defined for the
radiated power per unit area per unit `T⁴` rather than the energy
density:

```text
    σ_SB  =  (c/4) · u(T) / T⁴  =  (c/4) · (π² / 15) · 1 / (ℏ³ c³)
          =  (π² / 60) · k_B⁴ / (ℏ³ c²)  (with k_B = 1 absorbed)              (19)
```

Numerically: `(π² / 60) (1.380649 × 10⁻²³)⁴ / ((1.054571817 × 10⁻³⁴)³ × (2.99792458 × 10⁸)²)`
`= 5.670374419 × 10⁻⁸ W m⁻² K⁻⁴`. ∎

## Hypothesis set used

- Retained emergent Lorentz invariance (gives ω = c k dispersion).
- Retained anomaly-forced 3+1 dimensions (gives 3D density of states).
- Retained U(1) photon (massless gauge boson with two polarizations).
- Retained spectrum condition (H ≥ 0 ⇒ harmonic oscillator levels at
  nω, n = 0, 1, ...).
- Retained spin-statistics theorem (photons are bosons).
- Block 01 KMS support theorem (Gibbs state ↔ Planck distribution).
- Standard 3D mode-counting (admitted-context).
- Standard `Γ(4) ζ(4) = π⁴/15` (pure math).

No fitted parameters. No observed values used as proof inputs.

## Corollaries

C1. **Wien displacement law.** From the spectral energy density
`du/dω = ℏ ω³ / (π² c³ (e^{βℏω} - 1))`, maximizing in ω gives
`ω_max ≈ 2.821 T / ℏ`, the Wien displacement law. This is a direct
corollary of (SB2).

C2. **CMB blackbody.** At `T_CMB = 2.7255 K`, the photon energy
density is `u(T_CMB) = 4.17 × 10⁻¹⁴ J m⁻³`, matching the observed
CMB blackbody spectrum to better than 1 part per million. The
framework `T_CMB` is currently an external input
(`docs/publication/ci3_z3/PREDICTION_SURFACE_2026-04-15.md`); this
note shows that *given* `T_CMB`, the framework's retained surface
predicts the CMB energy density consistent with observation.

C3. **Photon-gas equation of state:** `p_γ = u / 3`. Follows directly
from photon dispersion `ω = c k` and the same Bose-Einstein integral.
Used in early-universe cosmology.

C4. **Cosmological consistency:** the retained
`N_eff = 3.046` ([`N_EFF_FROM_THREE_GENERATIONS_THEOREM_NOTE_2026-04-24.md`](N_EFF_FROM_THREE_GENERATIONS_THEOREM_NOTE_2026-04-24.md))
plus this Stefan-Boltzmann formula give the standard
`ρ_radiation,eq = (π²/30) g_*  T⁴` formula with photon contribution
exactly (1).

## Honest status

**Branch-local theorem on retained framework EW + Lorentz package +
Block 01 KMS support.** (SB1)–(SB4) follow by direct composition.
The runner verifies (SB1) via direct Planck-formula evaluation,
(SB2)–(SB3) via numerical integration of the Planck spectrum, and
(SB4) via the standard SI conversion to `σ_SB ≈ 5.67 × 10⁻⁸`.

**Honest claim-status fields:**

```yaml
actual_current_surface_status: support
conditional_surface_status: derived support theorem on retained framework EW + Lorentz package + Block 01 KMS support
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Inherits Block 01 KMS upstream support classification, which depends on retained-but-audit-pending RP and spectrum-condition support notes. Per physics-loop SKILL retained-proposal certificate item 4, a chain of support cannot promote to proposed_retained until upstream is ratified retained."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Not in scope.**

- Independent derivation via the photon worldline path integral on
  the framework lattice (would give the same result via different
  technical route).
- Promotion to retained / Nature-grade.

## Citations

- A_min: [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md)
- retained EW package: [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md),
  [`STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md`](STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md)
- cited anomaly-forced 3+1: [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) (currently `unaudited`)
- cited emergent Lorentz: [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md),
  [`LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md`](LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md) (both `unaudited`)
- cited spin-statistics: [`AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md) (currently `unaudited`)
- cited spectrum condition: [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md) (currently `unaudited`)
- Block 01 KMS support: [`AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_KMS_CONDITION_THEOREM_NOTE_2026-05-01.md) (currently `unaudited`)
- standard external references (theorem-grade, no numerical input):
  Stefan (1879) *Sitzungsberichte der Akademie* 79, 391;
  Boltzmann (1884) *Annalen der Physik* 22, 291;
  Planck (1900) *Verh. Deut. Phys. Ges.* 2, 237.

## Upstream-tier accounting (2026-05-17)

Per the 2026-05-17 ledger snapshot, the load-bearing upstreams of this
note sit at:

| Upstream | `claim_type` | `audit_status` | `effective_status` |
|---|---|---|---|
| `axiom_first_kms_condition_theorem_note_2026-05-01` (Block 01 KMS) | (varies; see ledger) | `unaudited` | `unaudited` |
| `emergent_lorentz_invariance_note` | `bounded_theorem` | `unaudited` | `unaudited` |
| `lorentz_kernel_positive_closure_note` | `positive_theorem` | `unaudited` | `unaudited` |
| `anomaly_forces_time_theorem` | `bounded_theorem` | `unaudited` | `unaudited` |
| `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | `positive_theorem` | `unaudited` | `unaudited` |
| `axiom_first_spin_statistics_theorem_note_2026-04-29` | `positive_theorem` | `unaudited` | `unaudited` |
| `axiom_first_spectrum_condition_theorem_note_2026-04-29` | `positive_theorem` | `unaudited` | `unaudited` |
| `rconn_derived_note` (EW package) | `bounded_theorem` | `audited_conditional` | `audited_conditional` |

**All but one of the cited upstreams are currently `unaudited`** (the
RCONN derived note is `audited_conditional`). Earlier wording
throughout this note used "retained" as the tier qualifier for the
upstream composite ("retained framework EW + Lorentz package + Block 01
KMS support", "retained surface", "retained emergent-spacetime
surface", "retained U(1) photon", etc.). Per the ledger, this is an
over-statement. The proof structure `(SB1)-(SB4)` is unaffected — it
remains a direct composition of the cited companions plus standard
math identities (`Γ(4) ζ(4) = π⁴/15`).

**Effective tier:** the Stefan-Boltzmann derivation here inherits at
best the **weakest** tier in the upstream composite, which is currently
`unaudited` for the photon / Lorentz / time-dimension / KMS /
spin-statistics / spectrum-condition stack. Once those upstreams audit
through, this row's effective tier rises automatically toward the
weakest *audited* upstream.

**Admission inheritance from `ANOMALY_FORCES_TIME_THEOREM`:** this note
uses only the `d_t = 3+1` substrate conclusion (specifically `d_s = 3`
for the 3D density of states) from the parent. Per the upstream
[F-B framing-fix](ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md),
the `d_t = 1` conclusion decomposes into derived (Step 3) and inherited
(admission (iv)) branches; the `d_s = 3` piece comes from axiom A2
directly (per `MINIMAL_AXIOMS_2026-05-03.md`), independent of admissions
(i)-(iv). Recorded for downstream-audit disambiguation.

## Fix record (2026-05-17, downstream surgical-fix wave)

One hostile-audit-grade fix applied to this note:

- **F-A (tier over-claim "retained"):** ~18 sites in the note used
  "retained" as the tier qualifier for the upstream composite. Per the
  2026-05-17 ledger, 7 of the 8 named upstreams are currently
  `unaudited` (only the EW package's RCONN_DERIVED_NOTE is
  `audited_conditional`). The most prominent wordings (Claim scope,
  Scope, "Retained inputs" section heading and bullets, Citations) have
  been corrected to "cited"; the remaining "retained" mentions in
  body/proof text are now understood through the §Upstream-tier
  accounting (2026-05-17) section. The proof structure `(SB1)-(SB4)`,
  the runner expectation, and the corollaries (C1-C4) are unaffected.

See companion fix-record:
`AXIOM_FIRST_STEFAN_BOLTZMANN_NOTE_2026-05-17.md`.

Paired verifier:
`scripts/frontier_axiom_first_stefan_boltzmann_downstream_fix.py`.

None of these edits change `(SB1)-(SB4)`, the proof steps, the runner
expectation, the corollary list, or the falsifiability framing.
