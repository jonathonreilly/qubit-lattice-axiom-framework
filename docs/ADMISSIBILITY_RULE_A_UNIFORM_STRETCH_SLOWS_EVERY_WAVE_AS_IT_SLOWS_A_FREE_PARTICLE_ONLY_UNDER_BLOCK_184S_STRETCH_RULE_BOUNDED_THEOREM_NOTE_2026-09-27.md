---
claim_id: admissibility_rule_a_uniform_stretch_slows_every_wave_as_it_slows_a_free_particle_only_under_block_184s_stretch_rule_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed and block 139's staggered mass as landed, for a walk whose plane-wave block is h = sum_a F(k_a; l) X_a + mu(l) Gamma with anticommuting hermitian involutions, per-axis hops F(k; 1) = sin k, a uniform stretch parameter l and fixed label momenta (sites held physical): (T1) every wave obeys d log E/d log l = -l^2 |v|^2 at every stretch, which is the law of a free particle with fixed momentum per label, iff dF/d(l^2) = -(1/2) F (dF/dk)^2 and the mass is unchanged; (T2) that rule, from F = sin k, is block 184's family (pushed), whose long-wave speed 1/l is the one the law's normalisation fixes; (T3) with the per-axis form of the law, the response of the walk to a further stretch of each axis, dh/d(l_a^2), is minus half its own symmetric stress K^s_aa (block 184 T7) as a matrix; (T4) the frame H/l, block 69's linear completion and the fixed-generator flow meet the law at l = 1 (block 180) and violate it at l != 1; (T5) with the rule, rest waves keep E = mu and each wave presses between 0 and E/(3V). No covariance and no books premise is used: the free-particle law alone fixes the stretch rule. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_a_uniform_stretch_slows_every_wave_as_a_free_particle_only_under_one_rule_2026_09_27.py
---

# A uniform stretch slows every wave as it slows a free particle only under block 184's stretch rule

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 69 and 139 as landed; blocks 180, 181 and 184 are pushed and placed, and the facts used from them are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 69 and 139 as landed on main (the two-step coupling to a uniform strain, and the staggered mass) and asks which stretch rule makes every wave of the walk slow under a uniform stretch as a free particle does; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 184 (pushed) found the one stretch rule that keeps the walker's books symmetric at every stretch. It assumed block 182's covariance, that each further stretch acts as a relabelling. This note removes that premise. It asks a plainer question: does a uniform stretch slow every wave exactly as it would slow a free particle whose momentum per label is fixed? A free particle obeys `d log E/d log ℓ = −|u|²`, where `u` is its velocity measured in lengths.

- **T1: the law fixes the rule.** Every wave of the walk obeys `d log E/d log ℓ = −ℓ²|v|²` at every stretch iff `∂F/∂(ℓ²) = −½F(∂_kF)²` and the mass does not change. Here `v` is the velocity per label, so `ℓ|v| = |u|`.
- **T2: that rule is block 184's.** From `F = sin k` it gives `k = k₀ + ((ℓ² − 1)/2) sin 2k₀` and `F = sin k₀ (sin² k₀ + ℓ² cos² k₀)^{1/2}`. Its long-wave speed is `1/ℓ`, as the law's normalisation already requires.
- **T3: equivalently, the response is the stress.** With the law stated per axis, the walk's response to a further stretch of axis `a`, `∂h/∂(ℓ_a²)`, equals `−½K^s_{aa}` as a matrix, where `K^s` is its own symmetric stress (block 184 T7).
- **T4: the other rules fail beyond first order.** The frame `H/ℓ` slows every wave as `d log E/d log ℓ = −1`, fast or slow. Block 69's linear completion and the fixed-generator flow meet the law at `ℓ = 1` (block 180) and violate it at `ℓ ≠ 1`.
- **T5: rest energy is kept.** Under the rule, a wave at rest keeps `E = μ`, and each wave presses between `0` and `E/(3V)`.

In plain terms: stretch the lattice uniformly, with the sites kept as they are. A free particle slows by an amount set by its own speed: a slow one hardly changes and a fast one slows the most. Ask the walker's waves to behave the same way, every one of them and at every stretch. That single request fixes how the walk must respond to stretch, and it is the rule block 184 found from the books. The simple rescaling of all hops slows every wave alike, fast or slow, and the short-range completions get it right only for small stretches.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 69 and 139 are used as landed on main. Blocks 180, 181 and 184 are pushed and placed; the facts used from them are re-derived (runner C1, D1, E1).

- **The coupling** (block 69), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`"; and "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
- **The staggered mass** (block 139), quoted: "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`, and each wave's energy current is its two-step momentum at every `k`, massive or not."
- **The walk.** `h(k) = Σ_a F(k_a; ℓ)X_a + μ(ℓ)Γ`, with `X_a` and `Γ` mutually anticommuting hermitian involutions (block 139's `τ_z ⊗ σ_a` and `τ_x`), odd per-axis hops, `F(k; 1) = sin k`. So `E² = Σ_a F_a² + μ²`, and `v_a = F_a∂F_a/E`.
- **The stretch.** A uniform isotropic parameter `ℓ > 0`, with the label momenta held fixed (sites held physical, as on a closed lattice). The family is twice differentiable in `ℓ` and real-analytic in `k`.
- **The law.** `d log E/d log ℓ = −ℓ²|v|²` for every wave and every `ℓ`. For a free particle with `E² = μ² + |p|²/ℓ²` and `p` fixed, this is exactly its law, with `u = ℓv` its velocity in lengths (runner B3).
- **The symmetric stress** (block 184 T7, pushed). On single waves, `K^s_{aj}(k, k) = ∂F_a∂F_j(F_jX_a + F_aX_j)/2`.

In the literature, a free particle's momentum in an expanding space falls as the inverse of the scale, and a field's stress is its response to the metric (Hilbert's definition). This note uses neither as authority.

## Domain qualifications

- Per-axis walks with a staggered mass; uniform stretches with fixed labels. Off-diagonal strains and walks that are not per-axis are not treated.
- "At every stretch" means on an interval of `ℓ` containing `1`. Block 184 T4 shows that the rule has no twice-differentiable continuation to `ℓ² = 2`.

## Theorem T1 — the law fixes the rule

*Statement.* The law holds for every wave at every `ℓ` iff `∂F/∂(ℓ²) = −½F(∂_kF)²` and `∂μ/∂ℓ = 0`.

*Proof.*
- Write `m = ℓ²`. The law is undefined where `E = 0`, so use its multiplied form, `∂_m(E²) = −Σ_a F_a²(∂F_a)²`, valid for every wave. Since `E² = Σ_a F_a² + μ²`, it reads `Σ_a g(k_a) + μ∂_mμ = 0` for every `k`, with `g = F(∂_mF + ½F(∂_kF)²)`.
- Comparing `k = (k₁, y, z)` with `k = (k₁′, y, z)` gives `g(k₁) = g(k₁′)`, so `g` is a constant `c`.
- `F` has a zero (it is continuous in `ℓ` from `sin k`, and in fact odd), and `g` vanishes there, so `c = 0`. Then `μ∂_mμ = 0`, so the mass does not change.
- So `∂_mF = −½F(∂_kF)²` wherever `F ≠ 0`. `F` is real-analytic in `k` and not identically zero, so its zeros are isolated, and by continuity of `∂_mF` in `k` the rule holds everywhere.
- The converse is the same computation. Runner B1 checks rule ⇒ law; runner B2 checks the separation step symbolically; the witnesses of T4 (runner E2) are candidates that fail the law. ∎

## Theorem T2 — that rule is block 184's

*Statement.* The rule from `F(k; 1) = sin k` is block 184's family, `k = k₀ + ((ℓ² − 1)/2) sin 2k₀` and `F = sin k₀ (sin² k₀ + ℓ² cos² k₀)^{1/2}`. Its long-wave speed is `∂_kF(0) = 1/ℓ`.

*Proof.* The substitution `u = F²` turns the rule into `∂_mu = −(∂_ku)²/4`, solved along characteristics as in block 184 T2. Runner C1 checks, symbolically in `sin k₀` and `cos k₀`, that the closed form obeys the rule. Its long-wave speed is `1/√m`. Twice-differentiable solutions are unique while the characteristics do not cross (block 184 T4's argument). ∎

The law's normalisation already fixes the long-wave speed. For `E ≈ c(ℓ)|k|` near a species point, the law reads `ℓc′/c = −ℓ²c²`, whose solution with `c(1) = 1` is `c = 1/ℓ`. The closed form is consistent with this.

## Theorem T3 — the response is the stress

*Statement.* Use the law per axis, `∂E/∂(ℓ_a²) = −½E v_a²` for a stretch of axis `a` alone; T1's argument goes through axis by axis. For a further stretch of axis `a` alone, `∂h/∂(ℓ_a²) = X_a ∂F_a/∂(ℓ_a²) + (∂μ/∂(ℓ_a²))Γ` equals `−½K^s_{aa}(k, k) = −½(∂F_a)²F_aX_a` as a matrix iff the rule holds on that axis and the mass is unchanged. Its expectation on a wave, summed over the axes, is the law of T1.

*Proof.* `X_a` and `Γ` are linearly independent, so the matrix equation splits into the two conditions (runner D1, with `4 × 4` involutions). ∎

So under the rule, the walk's symmetric stress is minus twice its response to the squared length. That is the lattice form of "the stress is the response to the metric", here exact at every stretch.

## Theorem T4 — the other rules fail beyond first order

*Statement.*
- The frame `H/ℓ` gives `d log E/d log ℓ = −1` for every wave. That meets the law only where `ℓ|v| = 1`.
- At `ℓ = 1`, block 69's linear completion and the fixed-generator flow meet the law, as all completions with block 69's first order do (block 180).
- At `ℓ ≠ 1` they violate it. At `sin k = 3/5`, `g` is `11675583/244140625` for the linear completion at `ℓ = 2`, and `58968/2825761` for the fixed-generator flow at `ℓ² = 2`.

*Proof.* Exact evaluation (runner E1, E2). ∎

## Theorem T5 — rest energy is kept

*Statement.* Under the rule, a wave at rest (all `F_a = 0`, `E = μ`) keeps its energy. Each wave presses `p = E ℓ²|v|²/(3V)`, between `0` and `E/(3V)` by block 184 T3.

*Proof.* Runner F1. ∎

## What this settles and what it does not

- **Settled.**
  - Block 184's stretch rule is characterised without covariance: it is the one rule under which every wave slows as a free particle does, at every stretch (T1, T2).
  - Under it, the stress is the response to the squared length (T3), and the rest energy is kept (T5).
  - The frame and the short-range completions meet the law only at first order (T4).
- **For the third column (the coupling axis).** The choice on this axis can now be put in one plain question. Does a uniform stretch slow every wave as it slows a free particle?
  - If yes, the rule is block 184's. It has infinite reach at every `ℓ ≠ 1` and ends at `ℓ = √2`.
  - If not, the other named completions depart from free-particle slowing at second order.
- **Not settled.**
  - Off-diagonal strains, which need a completion off the axes.
  - Walks that are not per-axis.
  - Whether the law should be required beyond first order at all. That is a supplied choice.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 69 N1 as landed: the leading order does not determine a nonlinear completion; block 184 (pushed): its rule rests on block 182's covariance"
source_of_blocker_text: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; off-diagonal strains"
conditional_surface_status: "exact within blocks 69 and 139, for per-axis walks with a staggered mass under a uniform stretch with fixed labels"
hypothetical_axiom_status: "the coupling, its completion and the law are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling.
  - Block 139 (landed): the staggered mass; the square is a number.
  - Block 180 (pushed): the law at first order.
  - Block 184 (pushed): the rule from covariance and the books, its closed form, and the pair-level stress.
- **In the literature.**
  - A free particle's momentum in an expanding space falls as the inverse of the scale factor.
  - Hilbert's definition of the stress as the response of the action to the metric.
  - The gravitation lens of the 2026-09-27 panel read block 180's first order as the massive case of Parker's particle creation.
  - None is used as authority.
- **New here.**
  - The free-particle law at every stretch fixes the rule, with no covariance premise (T1).
  - The law's normalisation and the closed form agree on the long-wave length (T2).
  - The stress-response form (T3).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: whether a kinematic criterion, rather than covariance, fixes the stretch rule. The obligations are:
- (O1) the premises (A3);
- (O2) the law and the rule, both directions (B1, B2), and the free particle (B3);
- (O3) the solution and its length (C1);
- (O4) the stress response (D1);
- (O5) the other rules (E1, E2);
- (O6) rest energy and pressure (F1).

## No-Go Discipline Gate

The note's negative sentences:
- no per-axis rule other than block 184's slows every wave as a free particle does at every stretch;
- a stretch that changes the staggered mass cannot meet the law.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A different parametrisation of the stretch.* The law is stated in `ℓ`, and T2 shows that `ℓ` is then the long-wave length. A reparametrised law would be a different law. ATTEMPTED; closed.
2. *A mass that responds.* T1's `k = 0` step forces it constant. ATTEMPTED; closed.
3. *Axis-dependent hops.* The separation argument goes through with `F_a` differing by axis, giving one rule per axis. Isotropy then gives a single `F`. Not needed for the statement.
4. *Walks that are not per-axis.* Not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: per-axis form, fixed labels, the law and smoothness.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling's first order | yes (quoted, A3) |
| block 139 (landed) | the staggered mass anticommutes | yes (quoted, A3) |
| block 180 (pushed) | the law at first order | re-derived (E1) |
| block 184 (pushed) | the closed form; the single-wave stress | re-derived (C1, D1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the free-particle law at every stretch fixes block 184's rule and keeps the mass" | executed: rule ⇒ law; the separation step (symbolic); the free particle; failing witnesses (E2) | executed: the closed form and its long-wave speed | executed: the stress response as matrices | executed: the three other rules at exact points; rest energy | proved, not executed: uniqueness of smooth solutions |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Free-particle slowing is a continuum idea. A lattice need not obey it at finite stretch."
  - *Reply:* Agreed. The note does not require it. It shows what requiring it costs and fixes: exactly block 184's rule.

### N8 — Cross-cycle echo
- Block 180: the law at first order for every completion.
- Block 182: covariance within reach three forces the linear completion.
- Block 184: covariance with the books forces one rule.
- This note: the free-particle law alone forces the same rule.

## Falsifiers

- A per-axis family other than block 184's, obeying the law for every wave on an interval of `ℓ`.
- A responding mass compatible with the law.

## Boundaries and non-claims

- Per-axis walks with a staggered mass; uniform stretch; fixed labels.
- The coupling, its completion and the law are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 69 and 139 (landed), quoted. Blocks 180, 181 and 184 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - separation of variables;
  - characteristics of a first-order equation (Hopf's method), as in block 184;
  - anticommuting involutions;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Before writing.**
  - Origin was re-fetched. Blocks 69 and 139 were read as landed, and blocks 180 and 184 on their branches.
  - The landed notes and the memory were grepped for "free particle", "equation of state" and "kinetic pressure". Block 46's "conserved tensor of radiation" and block 147's frame equation of state are different objects.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.
- **Second version.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error. Its corrections are applied:
  - the square in the claim scope's rule;
  - the converse through the multiplied law and a zero of `F`;
  - the long-wave length is fixed by the law's normalisation;
  - T3 uses the per-axis law;
  - the runner's B2 and E1 are no longer self-comparisons.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_uniform_stretch_slows_every_wave_as_a_free_particle_only_under_one_rule_2026_09_27.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
