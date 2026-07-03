# The Heat-Kernel Is the Unique Diffusion-Kernel Among the Candidate Gauge Actions

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_heat_kernel_unique_diffusion_kernel_2026_06_08.py`](../scripts/frontier_heat_kernel_unique_diffusion_kernel_2026_06_08.py)
**Cached output:**
[`logs/runner-cache/frontier_heat_kernel_unique_diffusion_kernel_2026_06_08.txt`](../logs/runner-cache/frontier_heat_kernel_unique_diffusion_kernel_2026_06_08.txt)

## Claim under test

PR #3338 reopened the gauge action-selection question (the action-form no-go's
continuum-equivalence premise is void on the framework's baseline physical lattice).
The no-go's **own Step 3(b)** gestured at a *"Brownian-motion uniqueness"* selection
criterion — the heat semigroup `exp(tΔ_g)` is uniquely determined by the canonical
metric — but **dismissed it as "suggestive, not tight,"** on the grounds that "the
canonical heat semigroup doesn't translate directly to the canonical lattice gauge
action … Wilson, HK, and Manton are all valid functionals."

**Is that criterion actually distinguishing?** Make it exact: which of the candidate
actions, if any, is the transition kernel of a continuous-time diffusion on the gauge
group?

## Verdict

**Among `{Wilson, heat-kernel (HK), Manton}`, the HK single-plaquette weight is the
UNIQUE continuous-time Markov diffusion transition kernel on the gauge group.** Its
generator is the canonical group Laplacian, fixed by the retained trace form. The
no-go's Step-3b criterion is therefore not "suggestive" — it is exact and genuinely
**selects HK uniquely** *among the candidates*. What remains open (and is named, not
hidden) is whether the framework's emergent-time gauge dynamics realize that diffusion.

## What is proved (exact — runner Parts 1–5)

Write a class-function weight as `w = Σ_λ c_λ χ_λ`; convolution acts as
`(f∗g)_λ = f_λ g_λ / d_λ` (Chapman–Kolmogorov in the character basis).

1. **HK is a convolution semigroup.** `c_λ(t) = d_λ exp(−t C₂(λ)/2)` satisfies
   `c_λ(s) c_λ(t)/d_λ = c_λ(s+t)` for **all** irreps (verified to `10⁻¹⁶`, SU(2) and
   SU(3)), and is **infinitely divisible** — `(P_{t/n})^{∗n} = P_t` — i.e. the
   transition kernel of a *continuous-time* Markov process. `P_s∗P_t=P_{s+t}` is
   exactly the Chapman–Kolmogorov equation.

2. **HK solves the group heat equation.** `d/dt c_λ = −(C₂(λ)/2) c_λ`, i.e.
   `∂_t P_t = ½ Δ P_t` with `Δ` the group Laplacian (eigenvalue `−C₂(λ)`). The
   generator's eigenvalues are the **canonical** Casimirs `C₂` fixed by the retained
   trace form `Tr(T_a T_b)=δ_ab/2` — no convention freedom.

3. **Wilson and Manton are NOT semigroups.** Their character coefficients (Bessel /
   Gaussian-geodesic) fail `c_λ(s)c_λ(t)/d_λ = c_λ(s+t)` (defects `O(1)`–`O(10)`).
   Neither is a diffusion transition kernel.

4. **SU(3) cross-check.** HK is a semigroup on trivial/fundamental/adjoint; the
   fundamental coefficient is `exp(−2/3)` at `t=1` — the no-go's single-plaquette
   `⟨P⟩_HK`. Wilson fails by the same mechanism.

5. **Uniqueness + isolation (teeth).** The reduced coefficient `φ_λ(t)=c_λ(t)/d_λ`
   must satisfy the Cauchy law `φ(s)φ(t)=φ(s+t)`; the only continuous solution is
   `exp(−κ_λ t)`, and the heat equation fixes `κ_λ=C₂(λ)/2`. So the HK form is the
   **unique** semigroup, generator pinned by the metric. A non-exponential coefficient,
   or any `HK + ε·(non-exp)` admixture, **breaks** the semigroup for `ε≠0` — HK is an
   isolated point, not a generic one.

**Net:** the heat-kernel is the unique candidate gauge action that is a diffusion
transition kernel, with a canonical (retained-metric) generator. The Brownian-naturality
criterion the no-go dismissed is in fact exact and decisive *as a selection rule*.

## The honestly-located open residual (NOT closed here)

Selecting HK by this criterion requires the gauge-link evolution under emergent time to
**be** a continuous Markov diffusion with this generator. That is a dynamical input, and
it is **named open**, for a reason grounded in a *retained* result:

> `record_classical_semigroup_boundary_2026-06-06` (**retained**): *"Nontrivial
> continuous Markov semigroups … require supplied transition rates or a supplied
> generator … Record can host the resulting realized tokens and counts; **Record alone
> does not generate the rate law**."*

So the RECORD axiom (time = monotone record accumulation) does **not** by itself supply
the continuous Markov generator that the diffusion criterion needs. The **generator**
`Δ` is retained-canonical (from the Tr-form); what is open is that emergent time drives
**this** `Δ`-diffusion on the gauge link.

This **locates the action-selection residual precisely**: derive the emergent-time
gauge-link diffusion (equivalently, supply/justify the canonical-Laplacian generator as
the realized dynamics). It converts "which of three functionals?" into one sharp
dynamical question with a unique answer *if* resolved — real progress over the no-go's
"suggestive."

## What this does NOT claim (boundary)

- **No claim that HK is the framework's realized action.** The diffusion premise is
  open (above); per the retained boundary, Record alone does not supply it.
- **No new axiom or import.** The candidate set, characters, and Casimirs are existing
  framework content / standard rep theory; the convolution-semigroup / heat-equation
  facts are standard math; the open premise is named, not assumed as background.
- **No continuum-limit claim, no coupling value.** Uniqueness is at the fixed physical
  lattice.
- Does **not** retire or contradict the action-form no-go; it sharpens its own Step-3b.

## Cross-references

- Reopened the question (companion): action-form no-go *scoped* — PR #3338 (`ACTION_FORM_NO_GO_EQUIVALENCE_PREMISE_CONTINUUM_REMOVAL_SCOPED_RELOCATION_NOTE_2026-06-08`)
- The no-go whose Step-3b this makes exact: [`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md)
- The open-residual boundary (retained): [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
- HK candidate context, plain references only:
  `BRIDGE_GAP_HK_TIME_DERIVATION_NOTE_2026-05-06`,
  `BRIDGE_GAP_HK_PLAQUETTE_CLOSED_FORM_NOTE_2026-05-06`.
- Baseline reading: [`PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08`](PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md)
- Standard method (not imports): heat kernel / Brownian motion on compact Lie groups; Chapman–Kolmogorov / convolution semigroups (Helgason 1978; Liao, *Lévy Processes in Lie Groups*).
