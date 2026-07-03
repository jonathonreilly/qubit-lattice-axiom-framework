# Record Density Slows the Local Front: an Exact 1D Toy Builds the Named-Not-Built Step to the Optical Metric

**Date:** 2026-06-09
**Claim type:** bounded_theorem (an exactly-solved toy model + closed-form bridge identities; no axiom-level derivation)
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:**
[`scripts/record_density_slows_lr_front_optical_metric_toy_2026_06_09.py`](../scripts/record_density_slows_lr_front_optical_metric_toy_2026_06_09.py)
(TOTAL: PASS=26 FAIL=0; cached:
[`logs/runner-cache/record_density_slows_lr_front_optical_metric_toy_2026_06_09.txt`](../logs/runner-cache/record_density_slows_lr_front_optical_metric_toy_2026_06_09.txt))

---

## The step this builds

The emergent-metric conformal-class note
([`EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS...`](EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md),
unaudited) states: *"A position-dependent record-density (varying `v_LR`) would curve the conformal
class — the seed of an emergent curved geometry / gravity. That extension is beyond this note"* and
lists it in its boundary as *"named, not built."* The weak-field map proposal
([PR #3385](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3385), closed, not
on main) called the same step its **M1 posit**: record-density `n(x)` → varying local front speed
`v_LR(x)` → curved effective metric, `g_00 = -(1+2Φ)`, `v_LR² = 1+2Φ`.

This note **builds that single step as an honest toy**: a minimal, exactly-diagonalized
one-dimensional model in which sites carrying records measurably slow the local information front,
so a record-density profile `n(x)` defines a front-speed field `v_eff(x)` and hence an
optical-metric potential `Φ(x)`. It is a toy: it shows the step is *constructible and internally
consistent in a concrete quantum model*, not that the framework's axioms force it.

## The toy model (all quantities in lattice units, `t = 1`)

- A single particle hops on an open chain (one axis of the Lattice axiom's `Z³`):
  `H_chain = -t Σ_x (|x+1⟩⟨x| + h.c.)`.
- A **record site** `x` carries a **frozen environment qubit** (no self-Hamiltonian in the ancilla
  sector), coupled by the excitation-conserving registration coupling
  `g (σ⁺_a c_x + c_x† σ⁻_a)`: the site's occupation amplitude is registered into the frozen qubit.
  This is the toy's reading of the Record axiom's noun — *a record is the durable registration of
  the realized outcome* — as a minimal interaction; the registration **dynamics** itself is a
  supplied model input (see Boundaries).
- In the one-excitation sector the qubit ancilla is **exactly** a quadratic dangling mode: the full
  `2^7` spin model's one-excitation sector reproduces the quadratic model's spectrum to `6.7e-16`
  (runner S1.1). Everything is exact diagonalization / transfer matrices / sympy — **no Monte
  Carlo** (the S3.5 channel sum is an exact `2^8` enumeration).
- **Record density** `n`: the fraction of sites carrying record couplings (periodic dilution
  `n = 1/m`), or for smooth profiles the coupling weight `g(x)² = g₀² n(x)`; the two
  implementations give the same velocity shift at weak coupling (S2.5).

## Results

### (a) The front slows, monotonically in record density

Exact bridge identities, derived symbolically (S1): eliminating the frozen mode gives the
energy-dependent on-site weight `ε_eff(E) = g²/E`; the single-record transmission
`τ(E) = 1/(1 + i g²/(2tE sin k))` (unitary, `|τ|²+|r|²=1`); the per-record Wigner delay is
**positive exactly on the inner band** `|E| < √2·t` with sign structure
`sign(τ_W) = sign(d(E sin k)/dE)` (positive at the carrier and every fast mode; the honest
band-edge advance for `|E| > √2·t` is verified, not hidden — the front statement below is
carrier-independent). The `n=1` medium has the exact inverse dispersion `ε(E) = E - g²/E`, a
spectral gap `2(√(t²+g²)-t)` at the pointer energy, and closed-form group velocity
`v_med(E) = v_k(ε(E))/(1+g²/E²)`.

At the carrier `E₀ = -2t cos(2π/5) ≈ -0.618` and `g = 0.4` (runner S2, exact Bloch +
Hellmann-Feynman and independent transfer-matrix slope, agreeing to 0.16%):

| record density n | 0 | 1/8 | 1/4 | 1/2 | 1 |
|---|---|---|---|---|---|
| carrier `v_g(E₀; n)` | 1.9021 | 1.7948 | 1.7128 | 1.4817 | 1.3868 |
| front speed `v_F(n) = max_k dE/dk` | 2.0000 | 1.7986 | 1.7379 | 1.6396 | 1.5649 |

Both **strictly decrease** with `n`. The time domain agrees independently: exact wave-packet
arrival through record slabs matches the frequency-domain prediction to 2.4% (W=120) and the
boundary-cancelling two-width subtraction to 1.4% (S3.1-S3.2); the exact one-particle propagator
light cone (the in-model information front) has its slope reduced by the Bloch ratio to 0.5%
(S3.3). Small-`g` laws are controlled: `τ_W ∝ g²` per record, and the full-comb front obeys
`v_F = 2t - √2·g + O(g²)` (Richardson-verified, S2.7).

### (b) The optical-metric map

For a smooth record-density bump `n(x) = exp(-(x-x_c)²/2σ²)` (σ = 60 sites, `g₀ = 0.45`), the
closed form gives the front-speed field `v_eff(x)` and the explicit optical-metric potential

```
Φ(x) = (v_eff(x)² - v_bare²) / (2 v_bare²)   ≤ 0,
ds² = -(1 + 2Φ(x)) (v_bare dt)² + dx²,   null cone dx/dt = v_eff(x)
```

| x | 400 | 550 | 640 | 700 (peak) | 760 | 850 | 1000 |
|---|---|---|---|---|---|---|---|
| n(x) | 0 | 0.044 | 0.607 | 1.000 | 0.607 | 0.044 | 0 |
| v_eff(x) | 1.902 | 1.863 | 1.480 | 1.293 | 1.480 | 1.863 | 1.902 |
| Φ(x) | 0 | -0.020 | -0.197 | -0.269 | -0.197 | -0.020 | 0 |

More record density ⇔ lower `Φ` (pointwise, S4.1), and the **exact packet arrival matches the
optical metric's null-geodesic (eikonal) time** `Σ_x (1/v_eff - 1/v_bare)` to 1.2% (measured 37.70
vs 37.24, S4.2): propagation follows `ds² = 0` of the exhibited metric. Within this toy, a
record-density bump is a `Φ < 0` well of the optical metric — the concrete content of "varying
record density curves the conformal class."

### (c) Controls: the effect is physical, controlled, and bounded honestly

- **Gauge invariance:** arbitrary local `U(1)` phase redefinitions on every site and every record
  mode leave all densities and arrivals unchanged to `1.1e-15` (S3.4).
- **Limits:** `n→0` or `g→0` restores the bare cone (S2.4); at the pointer energy (`E=0`
  antiresonance / the `n=1` gap) full records are perfectly opaque — transmitted weight `1e-9` vs
  bare `1.0` — the cone closes (S1.5, S1.6, S3.6).
- **Mechanism, quantified:** the measured time-integrated record-mode occupation equals the
  closed-form registration dwell `W·(g²/E²)/v_k'` to 1.3%, and delay = dwell + (small negative)
  refraction term to 1.9% (S3.7). The front is slow because amplitude **dwells in the record modes
  while being registered**.
- **Windowed imprint:** after the packet exits, a nonzero record-mode occupation remains and
  persists over the window (`1.50e-3 → 1.44e-3`; the slow residual leak of a unitary toy is
  reported, not hidden) (S3.8).
- **Class dependence (honest finding):** a projective pointer-copy record coupling
  (`g·n_x ⊗ σˣ_a`, exactly decomposed into `±g` potential channels) **attenuates** the front
  (plateau 0.72) with almost no delay (+0.21), while the amplitude-registration record **delays**
  (+1.71, 8×) with almost no attenuation (plateau 0.99) (S3.5). "Records slow the front" is a
  property of the registration class built here, **not** of every conceivable record coupling.

### The clock-rate boundary (respected and demonstrated)

Rescaling the supplied clock unit (`H → λH`) rescales every absolute speed by `λ` but leaves
`Φ(x)` — the dimensionless cone-slope field, i.e. the conformal-class datum — invariant to machine
precision (S4.3). The toy therefore fixes **only the conformal class**; the absolute scale (the
conformal factor = clock rate) remains the supplied time unit of the toy Hamiltonian, exactly the
boundary of the clock-rate no-go
([`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
[`RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06`](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md)).
Nothing here derives the scale.

## What is and is not claimed

- **Is claimed:** in this exactly-solved toy, record density (registration-coupling density of the
  amplitude-registration class) monotonically **reduces** the local front speed; the reduction is
  gauge-invariant, controlled in `g` and `n`, has the exact limits (bare cone at `n→0`; closed cone
  at the pointer energy); a smooth `n(x)` defines an explicit optical-metric potential `Φ(x) ≤ 0`
  whose eikonal time the exact dynamics follows. The load-bearing bridge `n → v_eff` is verified by
  two independent methods (frequency-domain Bloch/transfer-matrix vs time-domain packet/propagator
  cone), cross-checked numerically throughout.
- **Is NOT claimed:** no derivation of the emergent metric from the axioms (the toy's hopping and
  registration couplings are supplied model dynamics); no fixing of the conformal factor / clock
  rate (the no-go stands, and is demonstrated); no Einstein/weak-field dynamics, no Poisson closure,
  no statement about the framework's gravity **sign** (within the toy, records make `Φ < 0` wells,
  but whether the framework's matter → record-density → `Φ` chain carries that sign is the separate
  source-positivity question of the weak-field reduction — untouched here); no TT/spin-2 content;
  no claim that *every* record coupling slows the front (S3.5 shows the contrary); no claim about
  `d > 1` or beyond the one-excitation sector. Adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- **A toy, not the framework's dynamics.** The Lattice/Quantum/Record axioms supply no dynamics
  ([`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md): record-production dynamics is
  explicitly outside axiom content). The hopping chain and the registration coupling are model
  inputs chosen for exact solvability. What the toy establishes is the **internal consistency and
  constructibility** of the posited link `n(x) → v_eff(x) → Φ(x)` in a concrete quantum-lattice
  model, with controls — not its derivation from the axioms.
- **One dimension, one particle.** The chain is a single axis of `Z³`; everything is in the
  one-excitation sector. Many-body, higher-dimensional, and interacting versions are not addressed.
- **Dispersive medium.** `v_eff` depends on the carrier energy (the medium is dispersive); the
  monotone-decrease statement is proven at the inner-band carrier and, carrier-independently, for
  the front speed `v_F(n) = max_k |dE/dk|`. Near band edges (`|E| > √2·t`) the *per-carrier* group
  delay changes sign (verified exactly) while no speed ever exceeds the bare front.
- **Durability is not produced here.** A single frozen mode is a unitary environment: the imprint
  persists over the observation window with a slow re-emission leak (measured). Axiom-level
  durability is a constraint on what counts as a record; this toy does not supply a mechanism that
  makes the imprint permanently fixed.
- **Class dependence.** The slowing is a property of the amplitude-registration coupling class; the
  projective pointer-copy class attenuates instead (S3.5). Which class the framework's actual
  record formation realizes is not decided here.
- **The cited posit source is unaudited.** The conformal-class note itself is an unaudited,
  conditional assembly; this toy builds its named extension as a model, which neither audits nor
  promotes that note.

## Load-bearing inputs

- [`EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md`](EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md)
  — the posit source (unaudited): names the varying-record-density → varying `v_LR` → curved
  conformal class step ("named, not built") and locates the conformal-factor/clock-rate no-go this
  toy respects. The weak-field map proposal
  ([PR #3385](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3385), closed,
  not on main) frames the same step as its M1 posit; cited here as context only.
- [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md)
  and
  [`RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md`](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md)
  — the clock-rate boundary (the scale needs a supplied clock unit); demonstrated in S4.3, not
  violated.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the Lattice/Quantum/Record
  axiom statements and their explicit non-content (no dynamics), which set this note's honest
  scope. The Record axiom's noun (durable registration of the realized outcome) motivates the
  frozen-qubit registration model.
- No approved primitive is consumed: `scale_reference_primitive` is not used (all quantities in
  lattice units `t = 1`; no physical unit conversion), and `kinetic_isotropy_primitive` is not used
  (a 1D single-axis toy has no `c_t = c_s` cross-axis content).

## Forbidden-imports check

No PDG, fitted, or empirical value is consumed; every number is computed from the toy Hamiltonian
in lattice units `t = 1`. "Lieb-Robinson" is cited as the standard literature term for the front
concept **as context only**: the front statement actually used (max group velocity = the
free-model information front) is reproven in-model by the exact propagator light cone (S3.3) and
the exact band maximum (S2.3). The Fano-antiresonance / slow-light analogies are descriptive
context, not derivation inputs. All bridge identities (`ε_eff = g²/E`, `τ(E)`, the sign structure,
`ε(E) = E - g²/E`, the gap, `v_med`, the dwell accounting) are derived in the runner from the model
by sympy/exact linear algebra, not asserted. No Monte Carlo; the only ensemble (S3.5) is an exact
`2^8`-channel enumeration. No audit-lane file is touched.

## Runner check breakdown

S1 (the model + exact bridge, 8 checks): qubit↔mode equivalence; `ε_eff(E)`; derived `τ(E)` +
unitarity; Wigner-delay sign structure; antiresonance; `n=1` dispersion + gap; closed-form `v_med`.
S2 (monotone slowing, frequency domain, 7 checks): Bloch `v_g(E₀;n)` strict decrease; closed-form
match; front `v_F(n)` strict decrease; bare limit; density well-definedness; independent
transfer-matrix slope; `g²` and `√2·g` scaling laws.
S3 (time domain + controls, 8 checks): slab arrival vs prediction; two-width subtraction;
propagator cone; gauge invariance; pointer-vs-registration class contrast; pointer-energy opacity;
dwell mechanism accounting; windowed imprint.
S4 (optical metric, 3 checks): the `Φ(x)` map exhibited + ordering; eikonal arrival match;
supplied-clock rescaling invariance of `Φ` (the no-go boundary).
`TOTAL: PASS=26 FAIL=0`.

## Runner

```bash
python3 scripts/record_density_slows_lr_front_optical_metric_toy_2026_06_09.py
```
