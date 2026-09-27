---
claim_id: admissibility_rule_under_the_two_step_coupling_the_filled_sea_presses_below_a_third_of_its_energy_and_a_uniform_stretch_can_excite_it_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's massless walk and block 69's two-step coupling as landed (the coupling blocks 120 and 136 use to source the member), for a uniform isotropic stretch at first order (H(k) = sum_a sigma_a s_a (1 + b c_a^2), 1 + b = 1/l, block 69 T4), compared with the rescaled walk H(k)/l supplied in blocks 146 and 147: (T1) a walker's energy changes as d log E/d log l = -(1 - sum_a s_a^4/E^2), which lies in (-1, 0] wherever E > 0 and tends to -1 only at the eight species points; (T2) so with block 146's dilation pressure a walker presses (1 - sum s^4/E^2) rho/3, nothing where every active axis has s^2 = 1, and the filled negative band presses strictly between 0 and rho/3 of its energy density on the infinite lattice: exactly 0, 1/12 and an exact algebraic number on the tori of side 4, 6 and 8, against 1/3 for the rescaled walk; (T3) two stretches do not commute: [H(b1), H(b2)] = 2i(b2 - b1)(s x w).sigma with w_a = s_a c_a^2, so a stretch turns a walker's coin at fixed wave number unless its active axes share one cos^2, and the filled sea is not an eigenstate of a stretched walk (240 of 512 modes on the side-8 torus, none on sides 4 and 6); (T4) long waves agree at every species point. First order in the stretch; the finite-stretch completion is not used. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_only_the_two_step_current_can_source_block_62s_symmetric_member_no_local_placement_of_the_frame_response_or_of_the_one_step_current_keeps_its_divergence_condition_bounded_theorem_note_2026-09-24
  - admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
  - admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_bounded_theorem_note_2026-09-25
  - admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_under_the_two_step_coupling_the_filled_sea_presses_below_a_third_2026_09_27.py
---

# Under the two-step coupling the filled sea presses below a third of its energy, and a uniform stretch can excite it

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 69, 120, 136, 146 and 147 as landed, at first order in a uniform stretch; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 69, 120, 136, 146 and 147 as landed on main (the two-step coupling, the member's source, and the lattice's uniform stretch) and compares two rules for how a uniform stretch acts on the walk; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 146 and 147 (landed) worked a closed lattice's uniform stretch with the rescaled walk `H(k)/ℓ`, a supplied rule. Every walker's energy falls as `1/ℓ`, a massless sea presses `ρ/3`, and stretches at different lengths commute, so a filled sea stays filled.

Block 69's two-step coupling gives a different stretch at first order. This is the coupling blocks 120 and 136 use to source the member. At a uniform isotropic strain it reads `H(k) = Σ_a σ_a s_a(1 + b c_a²)`, with `1 + b = 1/ℓ`.

- **T1: short waves lose energy more slowly.** `d log E/d log ℓ = −(1 − Σ_a s_a⁴/E²)`.
  - Long waves lose energy as `1/ℓ`.
  - Every other wave loses it more slowly.
  - Where every active axis has `s² = 1`, as at `k = (π/2, π/2, 0)`, the energy does not change at first order.
- **T2: the sea presses less than a third.** With block 146's dilation pressure, a walker presses `(1 − Σs⁴/E²) ρ/3`. The filled negative band presses strictly between `0` and `ρ/3` of its energy density on the infinite lattice. On the tori of side 4, 6 and 8 it is exactly `0`, `1/12` and about `0.09`; the rescaled walk gives `1/3`.
- **T3: the filled sea is not invariant under a stretch.** Two stretches do not commute: `[H(b₁), H(b₂)] = 2i(b₂ − b₁)(s × w)·σ`, with `w_a = s_a c_a²`.
  - A stretch turns a walker's coin at fixed wave number unless its active axes share one `cos²`.
  - So the filled sea is not an eigenstate of a stretched walk, and a stretch history can move walkers out of it.
  - For a slow stretch the excitation is second order in the rate, as for block 147's massive walk, and the gap `2E` suppresses it away from the species points.
  - This affects 240 of the 512 modes of the side-8 torus, and none on sides 4 and 6.
- **T4: long waves agree.** Near each of the eight species points both rules give `1/ℓ` and `ρ/3`.
- **A kinetic reading.** `r = |v|²`, the squared group velocity, so a walker presses `ρ|v|²/3` as a kinetic gas does. Each mode carries `m_eff² = E²(1 − |v|²) = Σ_a s_a⁴`, which is zero only at the species points. The band-top modes have `v = 0` and press nothing, like matter at rest.

In plain terms: if the lattice stretches evenly, how much energy does a walker lose? The rule blocks 146 and 147 used says every walker loses it in proportion, like light. The walk's own two-step coupling says only long waves do. Under it each lattice wave behaves like a particle with a mass that grows toward the top of the band, where it stops moving and loses no energy at first order. So a filled sea of walkers pushes outward less than light would. A stretch can also turn a walker's coin, which can lift walkers out of the filled sea; the rescaled rule never does that. The two rules agree only on long waves.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 69, 120, 136, 146 and 147 are used as landed on main.

- **The two-step coupling** (block 69 T4), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]` and `H² = Σ_a[s_a + c_a Σ_j B_a^j s_jc_j]²`. Near `k = πn + q`: `H² = qᵀ(1 + B)ᵀ(1 + B)q + O(q⁴)` for every `n`." So the long-wave speed at isotropic `B = b·1` is `1 + b`, and the length is `ℓ = 1/(1 + b)` at first order.
- **Its role as the member's source.**
  - Block 120, quoted: "The two-step current has a transposed identity for finite equal-energy wave sums and finite periodic eigenspaces;".
  - Block 136, quoted: "Their mean `P^B = (P″ + Q)/2` is conserved with the symmetric stress, and the energy flows as `P^B` too."
  - Block 179 (pushed) shows its symmetric current has the same uniform form.
- **The rescaled walk and the pressure** (blocks 146, 147).
  - Block 146, quoted: "Under the supplied uniform hopping rule the massless symbol is `H(k)/ell(t)`". Also "Define scalar dilation pressure by `m'=-3p ell³`." and "For positive massless-band energy per site `m=epsilon/ell`, scalar dilation pressure is rho/3."
  - Block 147, quoted: "With the supplied dilation pressure `p=-dm/dlambda/(3ell³)`, the massless sea has `p=rho/3`." Also "For the massless symbol H(ell)=H(1)/ell, Hamiltonians commute at all positive lengths; an initially filled negative band keeps its occupations under any uniform length history."
- **Notation.** `s_a = sin k_a`, `c_a = cos k_a`, `E = |s|`. A walker's energy per site is `m`, its density `ρ = m/ℓ³`, and `λ = log ℓ`. The **filled sea** is every negative-energy mode, with `m_sea = −avg_k E`. An axis `a` is **active** if `s_a ≠ 0`.

In the comparator, a stretching background changes a massless field's modes only through its scale, while massive fields can be excited. That is the setting of Parker's work on particle creation in an expanding space. This note uses none of it as authority.

## Domain qualifications

- First order in a uniform isotropic stretch at `ℓ = 1`. The finite-stretch completion (block 176, pushed) is not used.
- The identity frame, uniform rates, and the massless walk.
- T3 gives the non-commutation and the interband element. Excitation for a given stretch history needs the dynamics, which is not solved here.

## Theorem T1 — short waves lose energy more slowly

*Statement.*
- (a) At isotropic strain `B = b·1`, block 69 T4's form is `H(k) = Σ_a σ_a s_a(1 + b c_a²)`.
- (b) `dE/db` at `b = 0` is `Σ_a s_a²c_a²/E = (E² − Σ_a s_a⁴)/E`. Hence `d log E/d log ℓ = −r(k)`, with `r = 1 − Σ_a s_a⁴/E²`. The rescaled walk has `r = 1`.
- (c) `0 ≤ r < 1` wherever `E > 0`. `r = 0` iff every active axis has `s_a² = 1`, and `r → 1` at the eight species points.

*Proof.*
- (a) Set `B_a^j = bδ_aj`: `s_a + c_a b s_a c_a` (runner B1).
- (b) Differentiate `E² = Σ s_a²(1 + bc_a²)²`, and use `c² = 1 − s²` (B2). Since `d log ℓ = −db` at first order, `d log E/d log ℓ = −(Σs²c²)/E²`.
- (c) With `x_a = s_a² ∈ [0, 1]`, `E² − Σ s⁴ = Σ x_a(1 − x_a) ≥ 0`, with equality iff each `x_a ∈ {0, 1}`. And `Σ s⁴ > 0` where `E > 0` (B3). The limit is T4. ∎

## Theorem T2 — the sea presses less than a third

*Statement.*
- (a) A walker of positive energy `E` presses `p = r ρ/3` with block 146's dilation pressure. It presses nothing where `r = 0`; an axis wave with `sin k = 3/5` presses `(16/25) ρ/3`.
- (b) The filled sea presses `p/ρ = avg(E r)/(3 avg E)`. This is strictly between `0` and `1/3` on the infinite lattice.
- (c) On the tori of side 4, 6 and 8 the filled sea's ratio is exactly `0`, `1/12` and `(√10 + 20 + 15√2 + 10√6)/(10(√3 + 3√10 + 15 + 10√6 + 18√2))`, about `0.09`. The rescaled walk gives `1/3` on each.

*Proof.*
- (a) `p/ρ = −(1/3) d log m/d log ℓ` by the definition `m' = −3pℓ³`, with T1 (runner C2).
- (b) For `m_sea = −avg E`: `dm/dλ = avg(E r)` and `p/ρ = avg(E r)/(3 avg E)`. On the infinite lattice `0 ≤ r < 1`, `r > 0` on a set of positive measure near the species points, and `r < 1` wherever `E > 0`. So the ratio lies strictly between `0` and `1/3`.
- (c) Exact sums over the tori (C1). On side 4, `s² ∈ {0, 1}`, so `r = 0` for every mode. On side 6 every active axis has `s² = 3/4`, so `r = 1/4` for every mode. ∎

## Theorem T3 — a stretch can excite the sea

*Statement.*
- (a) At first order `H(b) = σ·(s + b w)` with `w_a = s_a c_a²`. So `[H(b₁), H(b₂)] = 2i(b₂ − b₁)(s × w)·σ`.
- (b) The interband element of `∂H/∂b` between the two eigen-coins of `σ·s` is `|ŝ × w|² = (E² Σ s²c⁴ − (Σ s²c²)²)/E²`. It is zero iff `w ∥ s`, that is, iff the active axes share one `cos²`.
- (c) So where it is non-zero, the filled sea is not an eigenstate of `H(b)` for `b ≠ 0`, and a stretch history can move walkers between the bands. The rescaled walk commutes at all lengths (block 147).
- (d) The element is non-zero for 240 of the 512 modes of the side-8 torus, and zero for every mode of the sides 4 and 6. At `k = (π/4, π/2, 0)` it is `1/12`.

*Proof.*
- (a) `(σ·u)(σ·v) − (σ·v)(σ·u) = 2i(u × v)·σ` (runner D1).
- (b) `|⟨+|σ·w|−⟩|² = |w|² − (ŝ·w)²`, the component of `w` across `ŝ`. The rest is the identity `|s × w|² = |s|²|w|² − (s·w)²` (D1).
- (c) A walker in an eigen-coin of `H(0)` has a non-zero component in the other band of `H(b)` when the element is non-zero.
- (d) Exact over the tori (D2). ∎

## Theorem T4 — long waves agree

*Statement.* Near each of the eight species points, `r = 1 + O(ε²)` at distance `ε`. So long waves of every species lose energy as `1/ℓ` and press `ρ/3` under both rules, and the element of T3(b) vanishes there to leading order.

*Proof.* Series at each species point (runner E1). ∎

## What this settles and what it does not

- **Settled.**
  - Blocks 146 and 147 found that a massless sea presses `ρ/3` and stays filled under any stretch. Both results rest on the rescaled walk.
  - Under block 69's two-step coupling at first order, the sea presses strictly less than `ρ/3`, and a stretch can excite it.
  - The two rules agree only on long waves.
- **For the third column.** The stretch rule is not an independent item. It is the uniform part of the coupling, meaning which momentum generates relabellings and how covariantly the coupling reaches.
  - The rescaled walk is block 62's nearest-neighbour frame at a uniform stretch.
  - The two-step coupling is the one blocks 120 and 136 need for the member's non-uniform modes. If one local coupling acts on every mode, the uniform stretch is the two-step one, and blocks 146 and 147's equation of state and inert sea change as above.
  - The sea's worked consequences in blocks 147, 155 and 167 were computed under the frame. Under the two-step coupling they are conditional until re-derived.
- **Not settled.**
  - The finite-stretch completion (block 176). It decides the full `m_sea(ℓ)` and so block 147's turning point.
  - Excitation rates for a given history.
  - Anisotropic stretches.
  - Massive walkers under the two-step coupling.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 146 and 147 as landed: the zero mode's massless pressure rho/3 and inert sea under the supplied rescaled walk"
source_of_blocker_text: admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; the sea's excitation for a given stretch history; the finite-stretch completion's m_sea(l)"
conditional_surface_status: "exact at first order in a uniform stretch, within blocks 69, 120, 136, 146, 147"
hypothetical_axiom_status: "the walk, the couplings, the stretch rules and the pressure definition are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.** All landed, the supervisor's own:
  - block 69: the two-step coupling's uniform form;
  - blocks 120 and 136: the two-step current as the member's source;
  - block 146: the rescaled walk, the dilation pressure and `ρ/3`;
  - block 147: the sea's energy, `p = ρ/3`, commuting stretches, and a massive block whose stretches do not commute.
- **Block 179** (pushed): the symmetric two-step current, with the same uniform form.
- **In the literature.**
  - Particle creation by an expanding background is Parker's. There a conformally coupled massless field is not excited, and a massive one can be.
  - Here each lattice mode carries `m_eff² = Σ s_a⁴` under the two-step coupling, so this is the massive case. A same-family panel lens pointed out the kinetic reading, and it is checked here (B4).
  - None is used as authority.
- **New here.**
  - The two-step coupling's stretch law for every wave number (T1).
  - The sea's equation of state under it (T2).
  - The non-commutation and interband element for the massless walker (T3). Block 147 found non-commutation only for the massive block.
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: what a uniform stretch does to the walk under the member's own coupling, against the rule blocks 146 and 147 used. The obligations are:
- (O1) the premises (A3, A4);
- (O2) the stretch law (B1–B3);
- (O3) pressures (C1, C2);
- (O4) non-commutation and the interband element (D1, D2);
- (O5) long waves (E1).

## No-Go Discipline Gate

The note's negative sentences:
- under the two-step coupling, no mode away from the species points loses energy as fast as `1/ℓ`;
- the filled sea does not press `ρ/3`;
- the sea is not an eigenstate of a stretched walk wherever the element of T3(b) is non-zero.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A different completion.* T1, T2 and T3(b)–(d) are first-order derivatives at `ℓ = 1`, fixed by block 69 T4's first-order form, and no completion changes them. T3(a)'s commutator at finite `b` is a property of the first-order form. ATTEMPTED; closed for the derivatives.
2. *An anisotropic stretch.* Not examined.
3. *A massive walker.* Not examined under the two-step coupling.
4. *Averaging over a stretch history.* T3 gives the element, not a rate. Excitation for a given history is not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- "Background" appears only in the comparator sentences, under the Premises and Prior art.
- The following are declared: first order, isotropic stretch, the massless walk, the pressure definition of block 146, and the filled sea.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the two-step coupling's uniform form | yes (quoted, A3; re-derived, B1) |
| blocks 120, 136 (landed) | the two-step current as the member's source | placement (quoted, A3) |
| blocks 146, 147 (landed) | the rescaled walk, the pressure, `ρ/3`, commuting stretches | yes (quoted, A4) |
| block 179 (pushed) | the symmetric current's uniform form | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "short waves lose energy more slowly; the sea presses below a third; a stretch can excite it" | executed: the uniform form, its first-order change, the identity | executed: per-mode pressures | executed: the commutator, the element, every mode of three tori | executed: the sea's ratio on three tori; species limits | proved, not executed: the infinite-lattice ratio in `(0, 1/3)`; not examined: histories, completion |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "At long wavelength the two rules agree, so this is a lattice artefact."
  - *Reply:* The filled sea occupies the whole band, not only long waves. Its equation of state and its inertness are whole-band properties, and there the rules differ at first order.
- *Objection:* "Blocks 146 and 147 said their rule is supplied."
  - *Reply:* Yes. This note computes what the other supplied rule gives. That rule is the member's own coupling (blocks 120, 136), and the choice between the two is not made by records.

### N8 — Cross-cycle echo
- Block 69: the two-step coupling.
- Blocks 120 and 136: its role as source.
- Blocks 146 and 147: the zero mode under the rescaled walk.
- Block 176: the completion.
- This note: the zero mode's equation of state and inertness under the two-step coupling.

## Falsifiers

- A mode with `E > 0` away from the species points whose energy changes as `−E` per unit log-length under block 69 T4's form.
- A torus on which the filled sea's ratio under the two-step coupling differs from `avg(E r)/(3 avg E)`.
- A mode whose active axes have different `cos²` but whose coin a stretch leaves unturned.

## Boundaries and non-claims

- First order in a uniform isotropic stretch. The massless walk. Block 146's pressure definition.
- The couplings and stretch rules are supplied; excitation for a given history is not computed.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 69, 120, 136, 146 and 147 (landed), quoted. Block 179 (pushed), placed.
- Named standard imports, at definition level:
  - differentiation;
  - products of Pauli matrices;
  - the vector identity `|u × v|² = |u|²|v|² − (u·v)²`;
  - exact sums over finite tori;
  - series expansion.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Second version (after a same-family adversarial review and panel).**
  - T3's wording is "not invariant", with the rate caveat.
  - The kinetic reading is added (B4).
  - The third-column framing is folded into the coupling axis.
  - The sea's consequences under the frame are marked conditional.
- **Before writing.**
  - Origin was re-fetched. Blocks 69, 120, 136, 146 and 147 were read as landed.
  - The landed notes were grepped for "pressure", "comoving", "two-step" and "stretch". Blocks 146 and 147 use the rescaled walk; none computes the two-step stretch law.
  - The own prior-art check covered memory, the held branches, open PRs and the probes' attempts.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_the_two_step_coupling_the_filled_sea_presses_below_a_third_2026_09_27.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
