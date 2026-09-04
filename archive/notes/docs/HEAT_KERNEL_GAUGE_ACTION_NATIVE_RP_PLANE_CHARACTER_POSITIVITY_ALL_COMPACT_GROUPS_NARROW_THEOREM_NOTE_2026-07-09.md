# Heat-Kernel Gauge Action: Manifest Reflection-Plane Character Positivity for a Specified Central Heat Semigroup

**Date:** 2026-07-09
**Claim type:** bounded_theorem
**Status:** source-side bounded proposal; independent audit required.
**Primary runner:**
[`scripts/audit_companion_heat_kernel_native_rp_plane_character_positivity_2026_07_09.py`](../scripts/audit_companion_heat_kernel_native_rp_plane_character_positivity_2026_07_09.py)
**Cached output:**
[`logs/runner-cache/audit_companion_heat_kernel_native_rp_plane_character_positivity_2026_07_09.txt`](../logs/runner-cache/audit_companion_heat_kernel_native_rp_plane_character_positivity_2026_07_09.txt)

## Comparison boundary

The Wilson temporal-gauge RP bridge
([`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md),
whose current standing is recorded in the live audit ledger) runs a three-step mechanism on the
Wilson plane weight: (W1) reflection split of the action across the temporal
reflection plane, (W2) **nonnegativity of the character coefficients of the
plane (straddling) factor**, (W3) the integrated reflected Gram matrix is PSD
because the plane factor is a norm-square kernel. Step (W2) is load-bearing.

This note does **not** claim that the Wilson weight lacks a general positivity
route. For a finite-dimensional unitary representation `R`,
`exp[(β/2N)(χ_R+χ_R̄)]` expands as a positive power series in tensor-product
characters, and every tensor product decomposes into irreducible characters
with nonnegative integer multiplicities. That representation-ring route gives
nonnegative Wilson character coefficients for compact `G`. The earlier
group-dependent obstruction framing is therefore not an authority used here
and requires separate source repair. This note instead proves the parallel
heat-semigroup construction, whose coefficients and semigroup law are
manifest from the spectral definition.

## Claim (narrow theorem, bounded)

Let `G` be a compact Lie group equipped with a specified positive
bi-invariant Laplacian, and let `λ` label its irreducible representations with
dimension `d_λ` and nonnegative Laplacian eigenvalue `C₂(λ)`. For the `SU(N)`
cases, `C₂` uses the specified trace-form normalization
`Tr(T_a T_b) = δ_ab/2`. The finite and abelian runner testbeds use the explicitly
specified nonnegative central generators stated below. Define the heat-kernel
(HK) single-plaquette weight

```
K_t = Σ_λ c_λ(t) χ_λ ,   c_λ(t) = d_λ · exp(−t · C₂(λ)/2) ,   t > 0 ,
```

the same candidate object and convention as the HK candidate notes
(`HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08`;
the SU(3) fundamental coefficient there, `exp(−2/3)` at `t = 1`,
is `exp(−t·C₂/2)` with `C₂(fund) = 4/3` — the runner cross-checks this
convention alignment). Then:

- **H1 (spectral positivity — manifest for the specified heat semigroup).**
  `c_λ(t) = d_λ e^{−t C₂(λ)/2} > 0` for **every** irrep of every compact Lie
  group carrying the specified positive bi-invariant Laplacian and every
  `t > 0`. The (W2)-analog on the HK weight follows directly from the spectral
  definition. In particular it holds for `SU(3)` and all `SU(N)` with the
  displayed Casimir convention.

- **H2 (plane factor is a norm-square kernel).** `K_t` is real (the spectrum
  is closed under conjugation with `d_λ̄ = d_λ`, `C₂(λ̄) = C₂(λ)`), and by the
  cut factorization `χ_λ(AB†) = Σ_{ij} π_λ(A)_{ij} · conj(π_λ(B)_{ij})` the
  per-link plane factor is

  ```
  K_t(U(0) U(1)†) = Σ_λ c_λ(t) Σ_{ij} π_λ(U(0))_{ij} · conj(π_λ(U(1))_{ij}) ,
  ```

  a positive combination (`c_λ > 0`) of manifest Gram products — a norm-square
  kernel in matrix-element features on this heat-semigroup surface.

- **H3 (integrated two-slice RP Gram PSD, natively).** On the bridge note's
  two-slice temporal-gauge carrier (temporal gauge `U_0 = 1`, periodic spatial
  direction, `L_s` spatial links per slice, antilinear reflection
  `Θ(F)(U) = conj(F(θU))`), replace the Wilson weight by the HK weight
  `exp(−S_HK) = Π_p K_t(U_p)` (one spatial-loop factor per slice, one
  straddling factor per spatial link). The half-slice weights are **real**
  (H2 realness — the property the reflected-Gram argument actually consumes),
  the plane factor is a norm-square kernel (H2), so the reflected Gram
  `G_IJ = ⟨Θ(F_I) F_J⟩` over positive-half observables is PSD:
  `G = W diag(κ) W†` with `κ ≥ 0`. This instantiates the gauge-half
  Cauchy–Schwarz hypotheses
  ([`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md);
  consult the live audit ledger for current standing) on the HK weight for compact Lie `G`
  with the specified heat semigroup. The runner exercises the integrated Gram
  numerically for `SU(2)` and `SU(3)` and exactly for the listed finite
  testbeds; those checks support the factorization but are not its proof.

- **H4 (pointwise-positivity boundary — Boltzmann sensibility).** For `Z_N`
  at the enumerated values and for `U(1)`, the runner establishes `K_t > 0`
  pointwise: `Z_N` by exact evaluation and `U(1)` via
  the Poisson-summation (Jacobi theta) identity
  `Σ_n e^{−tn²/2} e^{inθ} = √(2π/t) Σ_m e^{−(θ−2πm)²/(2t)}` — a sum of
  manifestly positive Gaussian terms. For `SU(2)` and `SU(3)`, the finite
  character truncations are positive on the sampled grids at the printed
  `t` values, but this is numerical evidence only: no analytic infinite-tail
  bound is proved here. H4 is **not** needed for H3 (the
  Gram argument uses realness and spectral positivity, not pointwise
  positivity). Strict pointwise positivity for the full `SU(2)`/`SU(3)` heat
  kernels remains a standard-theorem/import or analytic-tail gate outside the
  runner's certified claim.

**Bounded scope.** The theorem is about the HK **candidate** weight for a
specified central heat semigroup on the narrow two-slice carrier. It makes
the RP coefficient step manifest on that candidate; it does not select the
candidate or establish full-kernel pointwise positivity for `SU(2)`/`SU(3)`
(see boundary below).

## Why the heat-semigroup form is useful

The HK weight defines the plane factor spectrally, so coefficient positivity
is the definition's first line and the semigroup law is explicit. This is a
clean construction in its own right. It is not evidence for a Wilson-side
obstruction, and the theorem's value does not depend on such an obstruction.

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
| `SU(2)` | manifest + enumerated | exact to 1e−12 (symmetric-power reps) | seeded MC, tolerance-gated | finite-truncation grid evidence |
| `SU(3)` | manifest + enumerated | exact to 1e−11 (fund + adjoint) | seeded MC, tolerance-gated | finite-truncation grid evidence |

The `SU(2)`/`SU(3)` integrated Grams are Monte-Carlo estimates (fixed seeds,
printed tolerances). The deterministic H1/H2 coefficient algebra and
semigroup/normalization identities are exact on their stated surface. H4 is
proved for `Z_N`/`U(1)` as stated and is support-only for the sampled
`SU(2)`/`SU(3)` truncations.

## What this note does NOT claim

- **No claim that the HK weight is the framework's realized/selected action.**
  HK is the Casimir-native *candidate*; the uniqueness-among-candidates note
  (`HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08`)
  is a context pointer, as are the semigroup-selection boundary
  (`SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02`)
  and the registration-induced step-kernel route
  (`GAUGE_LINK_CENTRAL_REGISTRATION_INDUCED_BI_INVARIANT_STEP_KERNEL_THEOREM_NOTE_2026-07-02`)
  and the dynamical premise boundary
  (`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`). Nothing here leans on
  any of them; consult the live audit ledger for current standing. They are
  context pointers only.
- **No Wilson obstruction claim.** This note adds a parallel result on a
  different weight. It neither endorses nor depends on the Wilson bridge's
  `SU(N≥3)` comparator framing; the representation-ring route above shows
  that framing requires separate source repair.
- **No fermion factor, no full OS reconstruction.** Two-slice gauge-sector
  Gram positivity on a narrow carrier — not multi-slice transfer-matrix
  positivity (`AXIOM_FIRST_RP_TWO_STEP...` lineage), not a Hamiltonian, not a
  continuum limit, and no coupling value is fixed (`t` is a free positive
  parameter throughout; results are exercised at several `t`).
- **No new axiom.** The HK candidate, the carrier, the reflection,
  the observable algebra, and the trace-form normalization are existing
  framework content; character theory and Poisson summation are standard
  mathematical methods re-verified numerically by the runner. The
  Osterwalder–Seiler and textbook references below are **comparators only**
  (already the bridge note's comparators — no new comparator is introduced).
  The broad H1/H2 statement follows from the specified spectral definition;
  the paired runner verifies its listed finite, abelian, and `SU(2)`/`SU(3)`
  instances rather than exhaustively testing every compact Lie group.
- **No audit-status statement.** Grades are set exclusively by the independent
  audit lane; this note predicts nothing.

## Dependencies

**Load-bearing dependencies** (current standing is audit-lane-owned; consult
the live audit ledger):

- [`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the abstract norm-square/Cauchy–Schwarz mechanism whose
  hypotheses H2–H3 instantiate on the HK weight.
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — supplies the carrier, the antilinear reflection, the
  observable bases, the (W1)–(W3) decomposition, and the negative control
  design; this note swaps its plane weight and re-proves everything on the
  swap.

**Context pointers (NOT load-bearing; consult the live audit ledger for current
standing):** `HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08`,
`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08`,
`SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02`,
`GAUGE_LINK_CENTRAL_REGISTRATION_INDUCED_BI_INVARIANT_STEP_KERNEL_THEOREM_NOTE_2026-07-02`,
`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`,
`RP_WILSON_TEMPORAL_GAUGE_BRIDGE_SIGN_AND_POSITIVITY_REPAIR_NOTE_2026-06-06`,
`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29` (the root RP row;
this note neither uses it as load-bearing authority nor repairs it).

## Runner test plan (Parts A–E ↔ claims)

- **Part A — H1.** Enumerated strict positivity of `c_λ(t)` for `Z_N`
  (`N ∈ {2,…,6}`), `U(1)` (`|n| ≤ 30`), `SU(2)` (`j ≤ 15`), `SU(3)`
  (`p+q ≤ 10`), at several `t`; `SU(3)` dimension/Casimir spot checks
  (`d(1,0)=3, C₂=4/3`; `d(1,1)=8, C₂=3`; `d(2,1)=15`; `d(2,2)=27`).
  Coefficient positivity itself is analytic from H1; these finite checks are
  implementation sanity checks.
- **Part B — H2 algebra + conventions.** Exact coefficient-level semigroup
  `c_λ(s)c_λ(t)/d_λ = c_λ(s+t)` (all four groups); `Z_N` kernel-level
  convolution `K_s ∗ K_t = K_{s+t}` exact; trivial-coefficient normalization
  `= 1`; realness of `K_t` (exact / grid / sampled); character orthonormality
  on trig-exact quadrature grids (`SU(2)` Weyl `sin²` measure; `SU(3)` Weyl
  2-torus measure `|Δ|²/6` — validates the Schur-polynomial character
  machinery the `SU(3)` checks use); `U(1)` Poisson/Jacobi-theta identity to
  1e−10.
- **Part C — H4.** `Z_N` exact pointwise minima; `U(1)` term-positive Gaussian
  representation + grid minimum; `SU(2)`/`SU(3)` finite-truncation grid
  minima as numerical evidence only. No sampled finite-ratio estimate is used
  as an infinite-tail bound.
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
  `SU(2)` seeded MC Gram; **`SU(3)` seeded MC Gram**.

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

On the spectral heat-semigroup parametrization, coefficient positivity is
manifest, the gauge-half Cauchy–Schwarz mechanism runs natively, and
the antilinear-reflection control still separates the mechanism from vacuous
positivity. The runner checks the integrated `SU(3)` Gram as a numerical
instance. It proves pointwise positivity for the stated `Z_N`/`U(1)` surfaces
and reports only finite-truncation evidence for `SU(2)`/`SU(3)`. The remaining
open paths are the full-kernel positivity authority and action selection; this note
does not choose the heat-kernel candidate or rule out the Wilson route.
