---
claim_id: admissibility_rule_the_free_particle_law_for_every_uniform_metric_shears_included_fixes_one_spectrum_smooth_while_the_metrics_eigenvalues_lie_between_zero_and_two_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed (a uniform strain of any symmetric form) and block 139's staggered mass as landed, for the energies E(k; g) of a walk under a uniform metric g with label momenta held fixed, starting from W0 = sum sin^2 k + mu^2 at g = 1, and for the supplied law that every wave slows as a free particle does, dE/dg_ab = -(1/2) E v^a v^b with v = dE/dk (block 185 on diagonal metrics, pushed): (T1) the law, written for W = E^2 as dW/dg_ab = -(1/4) W_a W_b, is a system of six compatible flows; (T2) its solution is k = k0 + (1/2)(g - 1) grad W0(k0), W = W0(k0) + (1/4) grad W0 . (g - 1) . grad W0, with grad_k W = grad W0(k0), and it is the only twice-differentiable one; (T3) on diagonal metrics it is block 184's per-axis rule, and waves at rest keep W = mu^2; (T4) every wave's speed in lengths obeys v.g.v <= 1, strictly unless E = 0; (T5) it is a real-analytic relabelling exactly while every eigenvalue of g lies in (0, 2): at an eigenvalue 2 the band top folds and at an eigenvalue 0 a species point folds; a pure shear 1 + eps(e1 e2 + e2 e1) is smooth iff |eps| < 1. Spectral statement: a local walk realising the spectrum off the diagonal, and its pair-level books, are not constructed. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_the_free_particle_law_for_every_uniform_metric_2026_09_27.py
---

# The free-particle law for every uniform metric, shears included, fixes one spectrum, smooth while the metric's eigenvalues lie between zero and two

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 69 and 139 as landed; blocks 184 and 185 are pushed and placed, and the facts used from them are re-derived; a spectral statement; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 69 and 139 as landed on main (the two-step coupling to a uniform strain of any form, and the staggered mass) and extends block 185's free-particle law from diagonal stretches to every uniform metric; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 185 (pushed) showed that a diagonal stretch slows every wave as it slows a free particle only under block 184's rule. Shears, the off-diagonal strains, were left open, since the walk is no longer a sum over axes there. A free particle obeys `∂E/∂g_ab = −½E v^a v^b` for any uniform metric `g`, with `v` its velocity per label. This note asks every wave of the walk to do the same, for every metric. It works with the energies only.

- **T1: the law is consistent.** For `W = E²` the law is `∂W/∂g_ab = −¼W_aW_b`, six equations for one function. They are compatible: the six flows commute.
- **T2: one spectrum.** From the free walk with its staggered mass, `W₀ = Σ sin² k + μ²`, the solution is

  `k = k₀ + ½(g − 1)∇W₀(k₀)`,  `E² = W₀(k₀) + ¼∇W₀·(g − 1)·∇W₀`,

  with `∇_kW = ∇W₀(k₀)`. It is the only twice-differentiable solution.
- **T3: on the diagonal it is block 184's rule.** Waves at rest keep `E = μ` in every metric.
- **T4: no wave outruns the long waves.** In every metric, every wave's speed in lengths is at most one, `v·g·v ≤ 1`, and strictly below it unless `E = 0`.
- **T5: smooth exactly while the metric's eigenvalues lie between 0 and 2.** At an eigenvalue 2 the band top folds, and at an eigenvalue 0 a species point folds. So a pure shear `1 + ε(e₁e₂ + e₂e₁)` is fine iff `|ε| < 1`. Block 184's end at `ℓ = √2` is the diagonal case.

In plain terms: ask that bending the lattice's lengths, in any direction or at any slant, slows every wave just as it would slow a free particle. That request is not self-contradictory, and it fixes exactly how every wave's energy changes. No wave ever becomes faster than the long waves. The answer works as long as no direction of the lattice is stretched by more than √2 or squeezed to nothing.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 69 and 139 are used as landed on main. Blocks 184 and 185 are pushed and placed; the facts used from them are re-derived (runner D1).

- **The coupling** (block 69), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`", for a strain `B` of any symmetric form; and "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
- **The staggered mass** (block 139), quoted: "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`".
- **The metric.** A uniform symmetric `g = 1 + G`, with label momenta held fixed (sites held physical). At `g = 1`, `E² = W₀ = Σ_a sin² k_a + μ²`.
- **The law** (supplied; block 185's on diagonal metrics). For every wave, `∂E/∂g_ab = −½E v^a v^b` with `v = ∇_kE`, where the off-diagonal variable `g_ab = g_ba` counts both entries. A free particle, `E² = μ² + p·g^{−1}·p` with `p` fixed, obeys exactly this law (runner B1).
- **Scope.** Energies only. A local walk `h(k; g)` whose squared energy is `W`, and its pair-level books, are not constructed off the diagonal.

In the literature, systems of first-order equations whose flows commute are integrated along common characteristics (Hamilton–Jacobi theory, with involutive Hamiltonians). This note uses none of it as authority.

## Domain qualifications

- Uniform metrics; fixed labels; energies only.
- "Smooth" means that `k₀ ↦ k` is a real-analytic diffeomorphism of the zone, so that `W` is real-analytic in `k`.

## Theorem T1 — the law is consistent

*Statement.* With `W = E²`, the law is `∂W/∂g_ab = −¼W_aW_b`, with `W_a = ∂W/∂k_a`. Its six flows have Hamiltonians `H_ab = ¼p_ap_b` that depend only on `p = ∇W`, so they commute. The explicit common solution of T2 exhibits the compatibility.

*Proof.* `∇W = 2E∇E = 2Ev`, so `2E ∂E/∂g_ab = −E²v^av^b = −¼W_aW_b`. Brackets of functions of `p` alone vanish. Runner C1 checks the common solution. ∎

## Theorem T2 — one spectrum

*Statement.* For every symmetric `G`, the parametric family

`k = k₀ + ½G∇W₀(k₀)`,  `W = W₀(k₀) + ¼∇W₀(k₀)·G·∇W₀(k₀)`

has `∇_kW = ∇W₀(k₀)` and obeys `∂W/∂G_ab = −¼W_aW_b` (per entry) at fixed `k`, for all six components, with `W = W₀` at `G = 0`. Twice-differentiable solutions are unique.

*Proof.*
- Runner C1, symbolically for a general symmetric `3 × 3` `G`: `Jᵀ∇W₀ = ∇_{k₀}W`, with `J = ∂k/∂k₀`, and the law for each component.
- For a twice-differentiable solution the slope `∇W` is constant along each flow's characteristics, so each flow separately fixes the solution. ∎

## Theorem T3 — on the diagonal it is block 184's rule

*Statement.* For `g = diag(ℓ_a²)`, T2 gives `k_a = k₀_a + ((ℓ_a² − 1)/2) sin 2k₀_a` and `W = Σ_a sin² k₀_a (sin² k₀_a + ℓ_a² cos² k₀_a) + μ²`: block 184's per-axis rule. Where `∇W₀ = 0`, that is at rest, `W = μ²` in every metric.

*Proof.* Runner D1. ∎

## Theorem T4 — no wave outruns the long waves

*Statement.* `4W₀ − |∇W₀|² = 4Σ_a sin⁴ k₀_a + 4μ² ≥ 0`. With `v = ∇W₀(k₀)/(2E)`, the speed in lengths is

`v·g·v = (|p|² + p·G·p)/(4W₀ + p·G·p)`,  `1 − v·g·v = (4W₀ − |p|²)/(4W) ≥ 0`,

where `p = ∇W₀(k₀)` and `4W = 4W₀ + p·G·p > 0` away from `E = 0`. So no wave is faster than one in lengths, and none reaches it unless `E = 0`.

*Proof.* Runner E1. Positivity of `W` for `‖G‖ < 1` follows from `¼p·G·p > −¼|p|² ≥ −W₀ + μ²`. ∎

## Theorem T5 — smooth exactly while the eigenvalues lie between 0 and 2

*Statement.*
- The Jacobian is `J = 1 + GD`, with `D = diag(cos 2k₀_a)`.
- If every eigenvalue of `g` lies in `(0, 2)`, then `‖G‖ < 1` and `‖GD‖ < 1`, so `J` is invertible. `k₀ ↦ k` moves each point by a periodic amount, so it is then a real-analytic diffeomorphism of the zone.
- If `g` has an eigenvalue `2`, then `det(1 − G) = 0`, and `J` is singular at the band top, `D = −1`. If `g` has an eigenvalue `0`, `J` is singular at a species point, `D = 1`.
- A path of metrics from `g = 1` leaves the set of eigenvalues in `(0, 2)` only through such a metric. So the smooth family reaches exactly that set.
- For a pure shear `1 + ε(e₁e₂ + e₂e₁)`, the vertex determinants are `1 ± ε²`: smooth iff `|ε| < 1`.

*Proof.*
- `J = 1 + ½G·Hess W₀` with `Hess W₀ = 2D` (runner F1). `det J` is affine in each `cos 2k₀_a` (runner F1).
- The shear and the two folds are runner F2.
- A local diffeomorphism of the torus homotopic to the identity is a covering of degree one, hence a diffeomorphism. ∎

## What this settles and what it does not

- **Settled.**
  - Block 185's free-particle law extends to every uniform metric, shears included. It is consistent and fixes the spectrum (T1, T2).
  - On the diagonal the spectrum is block 184's rule (T3).
  - No wave outruns the long waves in any metric (T4).
  - The family ends exactly where some direction is stretched by `√2` or squeezed to nothing (T5).
- **For the third column (the coupling axis).** The plain question of block 185, "must a stretch slow every wave as it slows a free particle?", now covers every uniform metric. A yes fixes the energies in all of them.
- **Not settled.**
  - A local walk `h(k; g)` off the diagonal whose squared energy is `W`, and its pair-level books. On the diagonal, block 184 T7 supplies both.
  - Non-uniform metrics.
  - Behaviour at the boundary of the smooth set.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 183-185 (pushed): off-diagonal strains need a completion off the axes"
source_of_blocker_text: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; a local walk realising the spectrum off the diagonal"
conditional_surface_status: "exact within blocks 69 and 139, for the energies under a uniform metric with fixed labels, under the supplied free-particle law"
hypothetical_axiom_status: "the coupling's completion and the law are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling for any uniform strain.
  - Block 139 (landed): the staggered mass.
  - Block 183 (pushed): off-diagonal shears were left open for lack of an off-axis completion.
  - Block 184 (pushed): the per-axis rule, its fold at `√2`, and the speed limit per axis.
  - Block 185 (pushed): the free-particle law fixes the per-axis rule.
- **In the literature.**
  - Commuting Hamilton–Jacobi flows and their common characteristics.
  - A free particle's energy in a metric, `E² = μ² + p·g^{−1}·p`.
  - Coverings of the torus.
  - None is used as authority.
- **New here.**
  - The law for every uniform metric is consistent, with one explicit spectrum (T1, T2).
  - The speed limit in every metric (T4).
  - The exact smooth set, eigenvalues in `(0, 2)` (T5).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: the free-particle law for off-diagonal strains. The obligations are:
- (O1) the premises (A3);
- (O2) the free particle's law (B1);
- (O3) the common solution (C1);
- (O4) the diagonal reduction and the rest energy (D1);
- (O5) the speed identity (E1);
- (O6) the Jacobian and the smooth set (F1, F2).

## No-Go Discipline Gate

The note's negative sentences:
- no twice-differentiable spectrum other than T2's obeys the law;
- no member of the smooth family reaches a metric with an eigenvalue `0` or `2`.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *Path dependence.* The flows commute, so the solution depends only on `g`, not on the path. ATTEMPTED; closed.
2. *A different starting walk.* `W₀` is the free walk with the staggered mass. Other starting spectra are not examined.
3. *A local walk realising `W`.* Not constructed off the diagonal.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: uniform metrics, fixed labels, energies only, the law.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling for any uniform strain | yes (quoted, A3) |
| block 139 (landed) | the staggered mass | yes (quoted, A3) |
| blocks 184, 185 (pushed) | the diagonal rule and the law | re-derived (D1, B1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the law for every uniform metric fixes one spectrum; speed at most one; smooth exactly for eigenvalues in `(0, 2)`" | executed: the free particle's law | executed: the common solution, general `3 × 3` metric | executed: the diagonal reduction, the rest energy, the speed identity | executed: the Jacobian, the shear, the folds | not executed: a local walk off the diagonal |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A spectrum is not a walk. Without a local hopping law off the diagonal, this says nothing about the lattice."
  - *Reply:* Agreed for the walk itself. The spectrum is what the member's zero mode, the sea's energy and the speed limit use. The walk off the diagonal is stated as open.

### N8 — Cross-cycle echo
- Block 183: shears need an off-axis completion.
- Blocks 184 and 185: the per-axis rule, and the law that fixes it.
- This note: the law fixes the energies for every uniform metric.

## Falsifiers

- A symmetric `G` for which T2's family fails the law at some component.
- A wave in the smooth set with `v·g·v > 1`.

## Boundaries and non-claims

- Uniform metrics; fixed labels; energies only.
- The coupling's completion and the law are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 69 and 139 (landed), quoted. Blocks 183, 184 and 185 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - characteristics of first-order equations, and commuting flows;
  - the operator norm of a symmetric matrix;
  - coverings of the torus;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Before writing.**
  - Origin was re-fetched. Blocks 69 and 139 were read as landed, and blocks 183–185 on their branches.
  - The landed notes were grepped for "shear" with "completion". Block 183 names off-diagonal shears as open.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_free_particle_law_for_every_uniform_metric_2026_09_27.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
