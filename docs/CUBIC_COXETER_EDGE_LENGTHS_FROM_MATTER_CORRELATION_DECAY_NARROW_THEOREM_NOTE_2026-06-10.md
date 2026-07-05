# Regge Edge-Length Degrees of Freedom and Matter Correlation Decay: Analytic Decay Exponents Calibrate to the Landed Flat Assignment and Respond Through the Geometric Metric Map — a Linearized Ratios-Only Dictionary

**Date:** 2026-06-10
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_cubic_coxeter_edge_lengths_from_matter_correlation_decay_2026_06_10.py`](../scripts/frontier_cubic_coxeter_edge_lengths_from_matter_correlation_decay_2026_06_10.py) (PASS=9 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_cubic_coxeter_edge_lengths_from_matter_correlation_decay_2026_06_10.txt`](../logs/runner-cache/frontier_cubic_coxeter_edge_lengths_from_matter_correlation_decay_2026_06_10.txt)

## The gap (the named guardrail of the landed geometric rows)

The landed Regge rows presuppose dynamical edge lengths on the `Z³ × Z_τ` complex — *"the edge-length
metric degrees of freedom required by Regge calculus"* is an explicit guardrail of the landed
target-operator row
([`R3_GEOMETRIC_REGGE_LINEARIZATION...`](R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md)).
The axioms supply adjacency (Lattice), a per-site qubit (Quantum), and the record readout (Record) —
no length field. This note closes the **linearized identification** with the dictionary

> `ℓ̂(v) := Λ(v)/κ`,  `Λ(v)` = the **analytic decay exponent** of the matter two-point function along
> the edge ray `v` (the contour-shift singularity location — the standard correlation-decay exponent,
> cited as context and **certified directly** in-runner), `κ` = one overall normalization.

**Ratios only:** `κ` (the absolute scale) is exactly the located residual — the
[`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) boundary (the
conformal factor needs a supplied clock unit) and the registered
[`scale_reference_primitive`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (units bridge). The dictionary never
fixes it. 3D+1 framing throughout: space = `Z³`, tick direction = the supplied `Z_τ` extension used
by the cited geometric rows, and `c_t = c_s` per the registered
[`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md); Euclidean = the OS0
surface. Record is not used as a time metric here. **No asymptotic fits anywhere** — all numerics are
exact-object certificates (zeros and torus-positivity of the analytically continued symbol).

## Theorem (runner-verified)

1. **Sign dictionary (E1).** The landed s-form coupling `q̂ᵀ(1+h)q̂` (the TT-kernel row's canonical
   metric entry,
   [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING...`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md))
   occupies the **inverse-metric** slot of the curved-Laplacian symbol, so the metric perturbation is
   `−h` at linear order.
2. **Closed-form calibration (E2).** For an edge class with `k` active coordinates (`|v|=√k`,
   `k=1..4`): `Λ_k = 2k·asinh(m/(2√k))` exactly; the `m→0` ratios are
   **`√k = {1, √2, √3, 2}` — exactly the landed complex's flat edge-length assignment**
   ([`CUBIC_COXETER_REGGE_DEFICIT_VANISHING...`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)),
   with deviation law `1 + (m²/24)(1−1/k) + O(m⁴)`.
3. **The exponent certified, two-sided (E3).** The continued symbol `K(p+iθv)` has an **exact zero**
   at `p=0, θ* = 2asinh(m/(2√k))` (`~1e-16`, all class types including tick-mixed) and **no zero** on
   the sampled torus at `θ = 0.97θ*` (min `|K| ≈ 1.5e-2`): the exponent is `Λ(v) = kθ*`, the closed
   form. Tick and space orientations agree identically. Supporting: the position-space FFT decay
   sequences converge to the certified exponents monotonically from above (no fit used).
4. **The metric-response theorem (E4) — exact at finite `h`.** For the whole landed metric family,

   > `Λ(v; h) = 2k·asinh( m / (2√(k + vᵀhv)) )` **exactly** (the continued symbol at `p=0` is
   > `m² − 4sinh²(θ/2)(k + vᵀhv)` for every `h`),

   so `δlogΛ = c_resp(m,k)·(vᵀh_metric v)/|v|²` with `c_resp → ½` as `m→0`:
   `δℓ̂/ℓ̂ → vᵀh v/(2|v|²)` — **exactly the geometric metric map of the landed Regge rows, including
   the factor ½.**
5. **Finite-`h` certificates for the whole family (E5).** All 15 edge classes × all 10 metric
   components at `h = ±0.05`: the exact zero sits at `θ*(h)` of the law (machine), the torus is
   nonsingular below it, and **off-pattern components (`vᵀhv = 0`) leave `θ*` exactly unchanged**.
6. **Dictionary convergence (E6) and provenance (E7).** The exact response matrix converges to the
   geometric metric map `M₀` with the `O(m²)` law (log-log slope `1.960`); it has **rank 10** with
   column space → `im(M₀)` (principal-angle sine `8.7e-3` at `m=0.5`, `8.2e-4` at `m=0.15`): **the
   matter sector's metric content and the geometry's metric sector coincide through this linearized
   dictionary**;
   the 5 non-metric (breathing) directions are not populated in the limit.
7. **Tick on equal footing (E8).** The exact law depends only on `(k, vᵀhv)` — manifestly symmetric
   under coordinate permutations including tick↔space (machine-zero permutation identity); the
   record-sector realization of the time-edge response (record density slowing the front) is the
   landed
   [`RECORD_DENSITY_SLOWS_LR_FRONT_OPTICAL_METRIC_TOY...`](RECORD_DENSITY_SLOWS_LR_FRONT_OPTICAL_METRIC_TOY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
   row (cited, not re-derived).

## Net (what the identification means)

Through this linearized ratios-only dictionary, the Regge rows' edge fields are represented by the
matter sector's per-edge correlation-decay structure: the response calibrates to the landed flat
geometry, follows the landed metric family through the geometric metric map, lands on the metric
sector, and leaves the absolute scale unfixed. The runner verifies a shared linearized metric-sector
column space for the matter-correlation and Regge descriptions; it does not supply dynamics.

## What is and is not claimed

- **Is:** the dictionary definition; the closed-form calibration with its `O(m²)` deviation law; the
  two-sided certificates for the exponent and for the exact finite-`h` response law over the entire
  landed metric family; the convergence to `M₀` and the rank-10 provenance statement; the tick
  symmetry; the ratios-only discipline.
- **Is not:** does **not** supply the **dynamics** of these degrees of freedom — the matter-**induced**
  action on them is **not** the embedding-independent action (landed
  [`UNIVERSAL_GR_W_HESSIAN_IDENTIFICATION...`](UNIVERSAL_GR_W_HESSIAN_IDENTIFICATION_FULL_FINITE_K_CHANNEL_TABLE_BOUNDED_THEOREM_NOTE_2026-06-09.md):
  *"pure-gauge channels are not suppressed"*), and the EH-class dynamics is what the landed
  action-selection row
  ([`CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION...`](CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md))
  derives for embedding-independent actions — the **embedding-independence provenance of the dynamics
  is the named remaining gap**, with the nonlinear completion; does **not** fix the absolute scale `κ`
  (the located clock-rate/scale residual); does **not** treat interacting matter (free/Gaussian sector
  here; the scalar symbol is the s-form family's canonical carrier, with the Dirac determinant sharing
  the same s-form per the TT-kernel row). Adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- **Linearized dictionary** around the flat/uniform state; position-dependent (curved) extensions are
  the named next step (the landed record-toy is the time-edge instance).
- **The torus-positivity certificates are grid-sampled** (24⁴); the exact zeros are evaluated exactly.
  The identification of the analytic exponent with the position-space asymptotic rate is the standard
  correlation-decay statement (Ornstein–Zernike-type; context only), supported numerically by the
  from-above convergence of the FFT sequences.
- **Free matter, scalar symbol.** The s-form is the landed canonical metric entry for both the scalar
  symbol and the Dirac determinant (TT-kernel row); interacting corrections are open.
- A development lesson is recorded in-runner: position-space **asymptotic-rate fitting is unreliable**
  at accessible windows (slowly-converging, class-dependent prefactors; near-collinear `1/n` bases) —
  the exact-certificate method replaces it entirely.

## Load-bearing inputs

- [`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md) — the landed flat assignment the dictionary calibrates to.
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md) — the canonical s-form metric entry (E1, E4–E5).
- [`R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md`](R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md) — the edge-length-DOF guardrail this note discharges at the linearized level.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the `c_t=c_s` structural grant (tick on equal footing; nothing beyond the declared grant).
- [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) — the clock-rate boundary (the `κ` normalization stays unfixed; ratios only).
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the units bridge for `κ` (units remark only).
- [`RECORD_DENSITY_SLOWS_LR_FRONT_OPTICAL_METRIC_TOY_BOUNDED_THEOREM_NOTE_2026-06-09.md`](RECORD_DENSITY_SLOWS_LR_FRONT_OPTICAL_METRIC_TOY_BOUNDED_THEOREM_NOTE_2026-06-09.md) — the record-sector time-edge realization (cited).
- [`UNIVERSAL_GR_W_HESSIAN_IDENTIFICATION_FULL_FINITE_K_CHANNEL_TABLE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](UNIVERSAL_GR_W_HESSIAN_IDENTIFICATION_FULL_FINITE_K_CHANNEL_TABLE_BOUNDED_THEOREM_NOTE_2026-06-09.md) and [`CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md`](CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md) — the dynamics boundary (E9).

## Forbidden-imports check

No external-data value is consumed. The closed forms, certificates, response matrices, and reference
map `M₀` are derived/computed in-runner from the lattice symbol and the complex's geometry;
Ornstein–Zernike-type decay-exponent theory is cited as context only and enters no check.
The calibration ratios `{1,√2,√3,2}` and the factor `½` are outputs.
