# Heat-Kernel Gauge Action: The Reflection-Plane Character-Positivity Step Is Manifest for ALL Compact Groups (Native RP Mechanism, No Group-Dependent Certificate)

**Date:** 2026-07-09
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/audit_companion_heat_kernel_native_rp_plane_character_positivity_2026_07_09.py`](../scripts/audit_companion_heat_kernel_native_rp_plane_character_positivity_2026_07_09.py)
**Cached output:**
[`logs/runner-cache/audit_companion_heat_kernel_native_rp_plane_character_positivity_2026_07_09.txt`](../logs/runner-cache/audit_companion_heat_kernel_native_rp_plane_character_positivity_2026_07_09.txt)

## The gap this note addresses

The retained-bounded Wilson temporal-gauge RP bridge
([`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md),
ledger `effective_status = retained_bounded`) runs a three-step mechanism on the
Wilson plane weight: (W1) reflection split of the action across the temporal
reflection plane, (W2) **nonnegativity of the character coefficients of the
plane (straddling) factor**, (W3) the integrated reflected Gram matrix is PSD
because the plane factor is a norm-square kernel. Step (W2) is the load-bearing
positivity input, and on the **Wilson** weight it is **group-dependent**:

- `Z_N`: exact finite DFT — coefficients computed and checked nonneg.
- `U(1)`: modified Bessel `I_n(β) > 0` — positive-series certificate.
- `SU(2)`: numeric/Monte-Carlo evidence only.
- `SU(N≥3)`: **not derivable by that route.** Positivity of a class function
  does not imply nonnegative character coefficients on a nonabelian group, and
  the note's §4 conformance repair (PR #5050) rescoped its `SU(N≥3)` Wilson
  positivity statement to the Osterwalder–Seiler **literature comparator**,
  naming the heat-kernel action as the forward derivation path.

This note takes exactly that named forward path.

## Claim (narrow theorem, bounded)

Let `G` be any compact group, `λ` its irreps with dimension `d_λ` and Casimir
`C₂(λ)` (for the Lie cases, `C₂` in the retained trace-form normalization
`Tr(T_a T_b) = δ_ab/2`; for finite/abelian testbeds, any nonnegative-spectrum
group-Laplacian eigenvalue `λ_q ≥ 0` in place of `C₂`). Define the heat-kernel
(HK) single-plaquette weight

```
K_t = Σ_λ c_λ(t) χ_λ ,   c_λ(t) = d_λ · exp(−t · C₂(λ)/2) ,   t > 0 ,
```

the same candidate object and convention as the HK candidate notes
(`HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08`,
unaudited; the SU(3) fundamental coefficient there, `exp(−2/3)` at `t = 1`,
is `exp(−t·C₂/2)` with `C₂(fund) = 4/3` — the runner cross-checks this
convention alignment). Then:

- **H1 (spectral positivity — manifest, all compact `G`).**
  `c_λ(t) = d_λ e^{−t C₂(λ)/2} > 0` for **every** irrep of **every** compact
  group and every `t > 0`. The (W2)-analog on the HK weight requires **no**
  group-dependent certificate: no DFT, no Bessel positivity, no Monte-Carlo
  estimate. In particular it holds for `SU(3)` and all `SU(N)` — exactly the
  cases where the Wilson-weight route is not derivable.

- **H2 (plane factor is a norm-square kernel).** `K_t` is real (the spectrum
  is closed under conjugation with `d_λ̄ = d_λ`, `C₂(λ̄) = C₂(λ)`), and by the
  cut factorization `χ_λ(AB†) = Σ_{ij} π_λ(A)_{ij} · conj(π_λ(B)_{ij})` the
  per-link plane factor is

  ```
  K_t(U(0) U(1)†) = Σ_λ c_λ(t) Σ_{ij} π_λ(U(0))_{ij} · conj(π_λ(U(1))_{ij}) ,
  ```

  a positive combination (`c_λ > 0`) of manifest Gram products — a norm-square
  kernel in matrix-element features, for every compact `G`.

- **H3 (integrated two-slice RP Gram PSD, natively).** On the bridge note's
  two-slice temporal-gauge carrier (temporal gauge `U_0 = 1`, periodic spatial
  direction, `L_s` spatial links per slice, antilinear reflection
  `Θ(F)(U) = conj(F(θU))`), replace the Wilson weight by the HK weight
  `exp(−S_HK) = Π_p K_t(U_p)` (one spatial-loop factor per slice, one
  straddling factor per spatial link). The half-slice weights are **real**
  (H2 realness — the property the reflected-Gram argument actually consumes),
  the plane factor is a norm-square kernel (H2), so the reflected Gram
  `G_IJ = ⟨Θ(F_I) F_J⟩` over positive-half observables is PSD:
  `G = W diag(κ) W†` with `κ ≥ 0`. This instantiates the retained gauge-half
  Cauchy–Schwarz hypotheses
  ([`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md),
  ledger `effective_status = retained`) on the HK weight for **all** compact
  `G` — including `SU(3)`, where the runner runs the integrated Gram check the
  Wilson bridge could not derive.

- **H4 (pointwise positivity — Boltzmann sensibility).** `K_t > 0` pointwise,
  so `S_HK = −log K_t` is a real action and the HK weight is a genuine
  Boltzmann factor. Certified per group: `Z_N` exact evaluation; `U(1)` via
  the Poisson-summation (Jacobi theta) identity
  `Σ_n e^{−tn²/2} e^{inθ} = √(2π/t) Σ_m e^{−(θ−2πm)²/(2t)}` — a sum of
  manifestly positive Gaussian terms; `SU(2)` and `SU(3)` by a
  grid-plus-Lipschitz-plus-truncation-tail certificate (margin strictly
  exceeds the certified evaluation error), exercised at the runner's printed
  `t` values. H4 is **not** needed for H3 (the
  Gram argument uses realness and spectral positivity, not pointwise
  positivity); it is stated because a candidate *action* must have one.

**Bounded scope.** The theorem is about the HK **candidate** weight on the
narrow two-slice carrier. It upgrades the RP *mechanism* from
group-dependent-certificate to manifest **on that candidate**; it does not
select the candidate (see boundary below).

## Why this is the structurally honest fix

The Wilson-weight (W2) obstruction is real mathematics: `exp(β·Re χ_fund)` has
character coefficients given by group integrals that are not sign-definite
term-by-term for nonabelian `G`, and no general positivity theorem applies.
The HK weight **defines** the plane factor spectrally — positivity is not a
property to be certified after the fact; it is the *definition's first line*.
The group-dependence of (W2) is thereby located precisely: it is a property of
the **Wilson parametrization** of the plane weight, not of the RP mechanism,
the carrier, the reflection, or the gauge group. On the spectral (HK)
parametrization the mechanism is uniform in `G`.

Two structural bonuses, both re-proved in the runner rather than cited:

- **Semigroup/normalization for free:** `c_λ(s)c_λ(t)/d_λ = c_λ(s+t)`
  (character convolution `(f∗g)_λ = f_λ g_λ/d_λ`), and the trivial-rep
  coefficient is `c_triv(t) = 1`, so `∫ K_t dHaar = 1` — the weight is
  automatically Haar-normalized at every `t`.
- **The antilinear reflection stays load-bearing:** dropping the conjugation
  in `Θ` breaks PSD (the runner reproduces the bridge note's negative control
  on the HK weight — the mechanism is not vacuously positive).

## Carrier, observables, and conventions (mirrors the bridge note)

- Two time slices `t ∈ {0, 1}`; one periodic spatial direction with `L_s = 2`
  spatial links per slice; temporal gauge `U_0 = 1` on temporal links.
- Reflection `θ` swaps the slices; `Θ` is **antilinear**:
  `Θ(F)(U) = conj(F(θU))`.
- Positive-half observable algebra `A_+`: functions of the `t = 1` slice
  links. For the exact abelian Grams the runner uses the bridge note's
  character-degree ≤ 2 monomial basis; for `SU(2)`/`SU(3)` Monte-Carlo Grams
  it uses the bridge note's 6-element matrix-element/trace basis (for `SU(3)`,
  `Tr U` is complex; the basis includes a conjugated trace — a legitimate
  `A_+` element, the antifundamental character).
- HK weight on the carrier:
  `w(c₀, c₁) = K_t(loop(c₁)) · K_t(loop(c₀)) · Π_k K_t(U_k(0) U_k(1)†)`,
  where `loop(c)` is the spatial plaquette (ordered product of the `L_s`
  spatial links) of slice `c`. The straddling factor is the plane factor; the
  two loop factors are the half weights. Plane symmetry (W1-analog): the
  straddling factor is invariant under the slice swap because `K_t` is a real
  class function and `K_t(V†) = K_t(V)`.
- Groups exercised: `Z_N` (exact, finite testbed), `U(1)` (quadrature),
  `SU(2)` (deterministic certificates + seeded MC Gram), `SU(3)` (the target:
  deterministic certificates + seeded MC Gram).
- `SU(3)` irrep data: Dynkin `(p, q)`, `d = (p+1)(q+1)(p+q+2)/2`,
  `C₂ = (p² + q² + pq + 3p + 3q)/3`; characters evaluated as Schur polynomials
  of the link eigenvalues via Newton/Jacobi–Trudi (no character table import —
  computed from the matrices).

## What is exact vs. numeric (honest inventory)

| Group | H1 `c_λ > 0` | H2 factorization/realness | H3 Gram PSD | H4 pointwise |
|---|---|---|---|---|
| `Z_N` | manifest + enumerated | exact (1-dim reps) | **exact** double sum, all configs | exact evaluation |
| `U(1)` | manifest | exact coefficient algebra | quadrature (trig-exact grid) | Poisson identity, term-positive |
| `SU(2)` | manifest + tail bound | exact to 1e−12 (symmetric-power reps) | seeded MC, tolerance-gated | grid + Lipschitz + tail certificate |
| `SU(3)` | manifest + tail bound | exact to 1e−11 (fund + adjoint) | seeded MC, tolerance-gated | grid + Lipschitz + tail certificate |

The `SU(2)`/`SU(3)` integrated Grams are Monte-Carlo estimates (fixed seeds,
printed tolerances) — same evidentiary class as the bridge note's Part E
`SU(2)` check, now including the `SU(3)` case that the Wilson route had no
derivable (W2) for. The deterministic content (H1, H2, semigroup,
normalization, H4 certificates) is exact or certified with explicit error
budgets, and is where the theorem's force lives: **the group-dependent step of
the mechanism is gone by construction.**

## What this note does NOT claim

- **No claim that the HK weight is the framework's realized/selected action.**
  HK is the Casimir-native *candidate*; the uniqueness-among-candidates note
  (`HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08`)
  is **unaudited**, the semigroup-selection boundary
  (`SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02`)
  is **unaudited**, the registration-induced step-kernel route
  (`GAUGE_LINK_CENTRAL_REGISTRATION_INDUCED_BI_INVARIANT_STEP_KERNEL_THEOREM_NOTE_2026-07-02`)
  is **unaudited**, and the dynamical premise boundary
  (`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`) is **audit_in_progress**
  on the live ledger. Nothing here leans on any of them; they are context
  pointers only.
- **No modification of the Wilson bridge note.** Its Wilson-side scoping
  (including the `SU(N≥3)` Osterwalder–Seiler comparator framing after
  PR #5050) stands as audited. This note adds a parallel result on a different
  weight; it does not edit, retire, or re-grade anything.
- **No fermion factor, no full OS reconstruction.** Two-slice gauge-sector
  Gram positivity on a narrow carrier — not multi-slice transfer-matrix
  positivity (`AXIOM_FIRST_RP_TWO_STEP...` lineage), not a Hamiltonian, not a
  continuum limit, and no coupling value is fixed (`t` is a free positive
  parameter throughout; results are exercised at several `t`).
- **No new axiom, no import.** The HK candidate, the carrier, the reflection,
  the observable algebra, and the trace-form normalization are existing
  framework content; character theory and Poisson summation are standard
  mathematical methods re-verified numerically by the runner. The
  Osterwalder–Seiler and textbook references below are **comparators only**
  (already the bridge note's comparators — no new comparator is introduced);
  every positivity statement used here is re-proved by the paired runner.
- **No audit-status statement.** Grades are set exclusively by the independent
  audit lane; this note predicts nothing.

## Dependencies

**Load-bearing (valid retained tiers on the live ledger):**

- [`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
  — `retained`. The abstract norm-square/Cauchy–Schwarz mechanism whose
  hypotheses H2–H3 instantiate on the HK weight.
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — `retained_bounded`. Supplies the carrier, the antilinear reflection, the
  observable bases, the (W1)–(W3) decomposition, and the negative control
  design; this note swaps its plane weight and re-proves everything on the
  swap.

**Context pointers (NOT load-bearing; unaudited / in-progress statuses stated
above):** `HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08`,
`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08`,
`SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02`,
`GAUGE_LINK_CENTRAL_REGISTRATION_INDUCED_BI_INVARIANT_STEP_KERNEL_THEOREM_NOTE_2026-07-02`,
`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`,
`RP_WILSON_TEMPORAL_GAUGE_BRIDGE_SIGN_AND_POSITIVITY_REPAIR_NOTE_2026-06-06`,
`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29` (the root RP row,
`audited_conditional` — this note neither cites it as retained nor repairs it).

## Runner test plan (Parts A–E ↔ claims)

- **Part A — H1.** Enumerated strict positivity of `c_λ(t)` for `Z_N`
  (`N ∈ {2,…,6}`), `U(1)` (`|n| ≤ 30`), `SU(2)` (`j ≤ 15`), `SU(3)`
  (`p+q ≤ 10`), at several `t`; `SU(3)` dimension/Casimir spot checks
  (`d(1,0)=3, C₂=4/3`; `d(1,1)=8, C₂=3`; `d(2,1)=15`; `d(2,2)=27`);
  superexponential truncation-tail bounds with geometric-majorant guards.
- **Part B — H2 algebra + conventions.** Exact coefficient-level semigroup
  `c_λ(s)c_λ(t)/d_λ = c_λ(s+t)` (all four groups); `Z_N` kernel-level
  convolution `K_s ∗ K_t = K_{s+t}` exact; trivial-coefficient normalization
  `= 1`; realness of `K_t` (exact / grid / sampled); character orthonormality
  on trig-exact quadrature grids (`SU(2)` Weyl `sin²` measure; `SU(3)` Weyl
  2-torus measure `|Δ|²/6` — validates the Schur-polynomial character
  machinery the `SU(3)` checks use); `U(1)` Poisson/Jacobi-theta identity to
  1e−10.
- **Part C — H4.** `Z_N` exact pointwise minima; `U(1)` term-positive Gaussian
  representation + grid minimum; `SU(2)`/`SU(3)` certificates: grid minimum
  − Lipschitz·(spacing/2) − truncation tail > 0, with the Lipschitz constant
  from explicit character-derivative bounds (`|χ_j′| ≤ 2j(2j+1)`;
  `SU(3)` weight-phase degree ≤ p+q per torus angle → `|∂χ| ≤ d_λ(p+q)`).
- **Part D — H2 cut factorization.** `χ_λ(AB†) = Σ_{ij} π_λ(A)_{ij}
  conj(π_λ(B)_{ij})` exact on seeded random pairs: `Z_N` (all reps), `SU(2)`
  (symmetric-power reps `j ∈ {1/2, 1, 3/2, 2}`), `SU(3)` (fundamental and
  adjoint `π_ad(U)_{ab} = 2 Tr(T_a U T_b U†)`, cross-checked against the
  Schur-polynomial character and `χ_ad = |Tr U|² − 1`).
- **Part E — H3.** Integrated reflected Gram PSD on the two-slice carrier
  with the HK weight: `Z_N` exact over all configurations (`N ∈ {2,3,4,5}`,
  `t ∈ {0.3, 1.0, 2.5}`), plus the manifest factorization `G = W diag(κ) W†`
  with plane-kernel eigenvalues `κ ≥ 0` reproducing the direct Gram; the
  **dropped-conjugation negative control** (non-PSD); `U(1)` quadrature Gram;
  `SU(2)` seeded MC Gram; **`SU(3)` seeded MC Gram** — the check the Wilson
  bridge could not derivably run.

All checks are deterministic (fixed seeds); the runner prints
`TOTAL: PASS=N FAIL=0` on success.

## Standard methods and comparators (not imports)

- Character theory of compact groups, Weyl integration, Schur polynomials /
  Jacobi–Trudi, Poisson summation — standard mathematical methods; every
  instance used is re-verified numerically inside the runner.
- Heat-kernel lattice gauge actions and their character expansion appear in
  the literature the bridge note already lists as comparators (Osterwalder &
  Seiler, *Ann. Phys.* **110** (1978) 440; Montvay & Münster, *Quantum Fields
  on a Lattice*, §3.4 role). **Comparator only**: no positivity statement is
  imported from them; the runner re-proves each one it uses.

## Closing

The bridge note ends its `SU(N≥3)` discussion at a comparator because the
Wilson plane weight's character positivity is not derivable there. On the
spectral heat-kernel parametrization of the same plane weight, that entire
step is manifest for every compact group, the retained gauge-half
Cauchy–Schwarz mechanism runs natively (including the integrated `SU(3)` Gram
exercised here), the weight is automatically Haar-normalized and pointwise
positive, and the antilinear-reflection control still separates the mechanism
from vacuous positivity. The next path this opens: connecting this native-RP
property to the action-*selection* question (the unaudited HK-candidate lanes
above), where RP-for-all-`G` is now a structural property the HK candidate
carries and the Wilson parametrization does not derivably share.
