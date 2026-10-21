# Stefan–Boltzmann law on a supplied continuum photon model

**Date:** 2026-05-01; scope corrected 2026-10-21
**Type:** positive_theorem
**Claim scope:** the standard Planck and Stefan–Boltzmann formulas follow for a supplied continuum gas of independent bosonic harmonic-oscillator modes, with two polarizations, dispersion omega=c|k|, zero chemical potential and a Gibbs state. This does not derive that photon model from the framework axioms.
**Status authority:** independent audit lane only; no retention is asserted here.
**Runner:** `scripts/axiom_first_stefan_boltzmann_check.py`
**Historical log:** `outputs/axiom_first_stefan_boltzmann_check_2026-05-01.txt`

## Premises and scope

The calculation recovers a standard continuum result. It is not a new numerical thermodynamic prediction of the lattice axioms. The named physical bridges remain supplied:

- Independent bosonic oscillator modes with levels `n hbar omega`, `n=0,1,...`, after vacuum subtraction. Positivity of H alone does not supply these levels or Bose statistics. The cited spin-statistics note now retains only a finite-dimensional CCR obstruction, not a physical statistics selector.
- A Gibbs state with `beta=1/(k_B T)`, `T>0`, and zero chemical potential. KMS/Gibbs reasoning gives the geometric occupation sum only after the oscillator spectrum is specified.
- A continuum three-dimensional momentum measure, two transverse polarizations and `omega=c|k|` at all frequencies in the continuum model.
- For emitted power, an isotropic photon distribution with propagation speed c.

The current [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the spatial Z³ substrate, not these dynamics or physical photon identification. The cited [Lorentz note](EMERGENT_LORENTZ_INVARIANCE_NOTE.md) establishes a leading long-wavelength dispersion on its supplied free model, with lattice corrections. That leading term cannot justify extending an exact linear dispersion to infinite frequency on a finite-spacing lattice.

For a lattice realization, the continuum expression can serve as a leading low-temperature approximation only with matching low-energy mode content and control of the remaining bands and dispersion corrections. No error bound, finite-temperature correction or all-temperature lattice law is derived here. Exactness below belongs to the ideal continuum model.

## Conditional theorem and proof

**SB1 — Occupation.** For one supplied oscillator put `q=exp(-beta hbar omega)`, with `omega>0`. Then

```text
Z = sum_{n>=0} q^n = 1/(1-q),
<n> = (sum_{n>=0} n q^n)/Z = q/(1-q)
    = 1/(exp(beta hbar omega)-1).
```

The zero-point term cancels in the occupation average; the thermal energy below excludes the vacuum energy.

**SB2 — Density of states.** The supplied continuum measure gives

```text
g(omega)/V = 2 * 4 pi k²/(2 pi)³ * dk/domega
           = omega²/(pi² c³).
```

This is a continuum counting identity, not an exact Brillouin-zone density of states.

**SB3 — Energy density.** Combining the two identities and writing `x=beta hbar omega` gives

```text
u(T) = hbar/(pi² c³) integral_0^infty omega³/(exp(beta hbar omega)-1) d omega
     = (k_B T)^4/(pi² hbar³ c³) integral_0^infty x³/(exp(x)-1) dx
     = (pi²/15) (k_B T)^4/(hbar c)³.
```

The last equality is the standard integral `Gamma(4) zeta(4)=pi^4/15`. In natural units, `u=(pi²/15)T^4`.

**SB4 — Emitted flux.** Integrating an isotropic energy density over the outward hemisphere gives flux `F=c u/4`. Hence

```text
sigma_SB = F/T^4 = (pi²/60) k_B^4/(hbar³ c²)
         ≈ 5.670374419e-8 W m^-2 K^-4.
```

The denominator is c² rather than c³ because the flux gains a factor c. Flux per unit area is not radiance per solid angle. The SI number uses the supplied unit constants; it is not an independent fit or framework prediction.

## Conditional consequences and limits

The continuum spectral maximum obeys `x=3(1-exp(-x))`, with the positive root `x≈2.821439372` and `omega_max=x k_B T/hbar`. The isotropic continuum photon pressure is `u/3`.

At the externally supplied temperature `T=2.7255 K`, the same formula evaluates to approximately `4.17e-14 J/m³`. This numerical substitution is not a new measurement or a part-per-million comparison with an observed spectrum. Other radiation species and their effective degree counts require separate inputs.

The runner checks Gibbs sums, continuum quadrature, scaling, the integral, Wien's root and SI conversion. Its checks do not supply the photon sector, prove a lattice continuum limit or establish an empirical accuracy. It also checks two counterexamples to the withdrawn inferences: a positive two-level Hamiltonian does not have oscillator occupation, and truncating the continuum spectrum changes u/T^4 at finite temperature.

```yaml
actual_current_surface_status: support
conditional_surface_status: standard continuum photon calculation with supplied bosonic oscillator spectrum, Gibbs state, dispersion and mode measure
hypothetical_axiom_status: null
admitted_observation_status: external temperature used only in an illustrative substitution
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Historical accounting

The dated records below preserve the earlier review and tier discussion. Their references to the earlier proof wording do not override the corrected supplied-model scope above.

## Citations

- Historical axiom reference: [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md)
- Supplied photon-sector context: [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md),
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
