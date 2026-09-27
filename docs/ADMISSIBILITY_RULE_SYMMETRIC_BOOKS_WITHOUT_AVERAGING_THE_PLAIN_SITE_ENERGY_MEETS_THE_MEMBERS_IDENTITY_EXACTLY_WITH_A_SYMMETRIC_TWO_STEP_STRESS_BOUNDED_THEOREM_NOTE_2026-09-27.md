---
claim_id: admissibility_rule_symmetric_books_without_averaging_the_plain_site_energy_meets_the_members_identity_exactly_with_a_symmetric_two_step_stress_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk H = sum_a sigma_a S_a at a uniform rate and block 69's two-step momentum as landed, with block 179's unaveraged density P^s and symmetric stress K^s (pushed; re-derived here), exact operator identities for every state on Z^3, stated as matrix-symbol identities: (T1) the plain site energy e = Re psi^dag H psi obeys de/dt + sum_j dbar_j P^s_j = 0, so the energy current is the momentum density; (T2) dP^s_j/dt + sum_a dbar_a K^s_aj = 0 with K^s symmetric and P^s summing to S_j C_j; (T3) hence d^2 e/dt^2 = sum_aj dbar_a dbar_j K^s_aj for every state, all eight species and both branches; (T4) with e_u = e and Theta = K^s, block 135 T4's member demand holds for every state iff alpha = K/4, without block 135's body-diagonal average or block 120's transverse average; (T5) with P = P^s on the bond shift, block 136 T4(b)'s conditions for keeping every nonzero-mode lapse and shift constraint hold for every state iff alpha = K/4, without averages; blocks 135 and 136's averaged identities are these, averaged. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
  - admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_symmetric_books_without_averaging_2026_09_27.py
---

# Symmetric books without averaging: the plain site energy meets the member's identity exactly with a symmetric two-step stress

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact operator identities within blocks 69, 135 and 136 as landed, with block 179's density and stress re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 69, 135 and 136 as landed on main (the two-step momentum, the member's identity, and the symmetric books of the two-step content) and asks whether the books need their averages; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 135 (landed) made the walker's two-step content meet the member's identity exactly, for every state, iff `α = K/4`. It needed two averages:
- the energy averaged over the eight body-diagonal neighbours, `e′ = C₁C₂C₃e`;
- block 120's transverse average in the stress.

It also found that the site energy misses by the one factor `Π_l cos q_l`, and that no convolution of the site energy repairs block 120's unaveraged realisation. Block 136 (landed) kept symmetric books with averaged densities. It found the site energy, the unaveraged and one-step momenta, and block 62's site stress failing its laws.

This note finds that the averages are not needed once the stress is placed as block 179's `K^s`.

- **T1: the energy current is the momentum.** The plain site energy `e = Re ψ†Hψ` obeys `ė + ∇̄·P^s = 0` exactly, where `P^s` is block 179's unaveraged two-step momentum density.
- **T2: the momentum current is symmetric.** `Ṗ^s + ∇̄·K^s = 0` exactly, and `K^s_aj = K^s_ja`.
- **T3: one identity.** Hence `ë = Σ_aj ∇̄_a∇̄_jK^s_aj` for every state, all eight species and both branches.
- **T4: the member.** With the plain site energy sourcing the clock and `K^s` as the stress, block 135's member demand holds for every state iff `α = K/4`. The same condition as block 135, with no averages.
- **T5: every constraint.** With `P^s` coupled to block 136's bond shift, block 136's conditions for keeping every nonzero-mode lapse and shift constraint hold for every state iff `α = K/4`, with no averages.

Blocks 135 and 136's identities are these, averaged: averaging multiplies both sides by `Π_l cos q_l`.

In plain terms: the walker's energy, momentum and stress can be written site by site so that energy flows exactly as momentum, momentum flows exactly as a symmetric stress, and nothing needs to be smeared over neighbours. The member's clock can then be sourced by the plain energy at each site, and it matches the walker exactly when `α = K/4`.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 69, 135 and 136 are used as landed on main. Block 179 is pushed without a PR; its `P^s` and `K^s` are re-derived here (runner C1).

- **The walk and its momentum** (block 69). `H = Σ_aσ_aS_a`, at unit rate. Quoted: "Set P_j=S_j C_j=(T_j^2-T_j^-2)/(4i)".
- **Block 135.**
  - The site energy, quoted: "  - The site energy is `e(x) = Re ψ†(x)(Hψ)(x)` (blocks 55–56)."
  - Its finding, quoted: "So the site energy misses by the one factor `Π_l cos q_l`, which is the symbol of `C₁C₂C₃`, and `ë′ = −p·Θ·p` exactly."
  - Its T3(b), quoted: "- (b) Block 120's realisation without its transverse average, `φ_j = ½(1 + T_j⁻¹)`, meets neither `e` nor `e′`."
  - Its member, quoted: "- (a) At `β = −α` the member demands `ë_u = −(Kw̄²/(4α)) p·Θ·p` of the energy `e_u` that sources its clock. This is block 134 T1, re-derived with `R₂` and the full stress."
- **Block 136**, quoted: "The site energy, the unaveraged and one-step momenta, and block 62's site stress also fail."
- **Symbols.**
  - Pair symbols as in block 179: `F(x)` has `⟨ψ'|F(x)|ψ⟩ = e^{iq·x} F̂(k', k)`, a 2×2 matrix, `q = k − k'`.
  - `h(k) = Σ_a s_aσ_a`. `Â_a = ¼(e^{ik_a} + e^{−ik'_a})σ_a` and `f_a = ½(1 + e^{iq_a}) sin(k_a + k'_a)`.
  - `K^s_aj = ½(Â_a f_j + Â_j f_a)`, `P^s_j = ½(½f_j + h(k')Â_j + Â_jh(k))`, and `ê = ½(h(k) + h(k'))`, the symbol of `e`.
  - `∇̄_j F(x) = F(x) − F(x − e_j)`, with symbol `1 − e^{−iq_j}`.

## Domain qualifications

- Uniform rate and identity frame. The identities are between local operators, on square-summable states, finite periodic states and formal finite wave sums.
- T4 concerns the member's longitudinal identity, as block 135 T4 does. The full field equations and zero modes are not treated.

## Theorem T1 — the energy current is the momentum

*Statement.* `Σ_j (1 − e^{−iq_j}) P̂^s_j = i(ê h(k) − h(k') ê)` as matrices, for all `k, k'`. So `de(x)/dt + Σ_j ∇̄_jP^s_j(x) = 0` for every state.

*Proof.*
- `Σ_j (1 − e^{−iq_j}) f_j = i(h(k)² − h(k')²)` and `Σ_j (1 − e^{−iq_j}) Â_j = (i/2)(h(k) − h(k'))` (block 179 T2).
- So `Σ_j (1 − e^{−iq_j}) P̂^s_j = (i/2)(h² − h'²)`.
- And `i(êh − h'ê) = (i/2)(h² − h'²)` for `ê = ½(h + h')`.
- Runner B1 checks it. ∎

## Theorem T2 — the momentum current is symmetric

*Statement.* `Σ_a (1 − e^{−iq_a}) K̂^s_aj = i(P̂^s_j h(k) − h(k') P̂^s_j)`, `K^s_aj = K^s_ja`, and `Σ_x P^s_j(x) = S_jC_j`.

*Proof.* Block 179 T2, re-checked (runner C1). ∎

## Theorem T3 — one identity

*Statement.* `Σ_aj (1 − e^{−iq_a})(1 − e^{−iq_j}) K̂^s_aj = −(h'²ê − 2h'êh + êh²)`, the symbol of `d²e/dt² = −[H, [H, e]]`. So `ë(x) = Σ_aj ∇̄_a∇̄_jK^s_aj(x)` for every state. On eigen-coins it reads `∇̄∇̄:K^s = −(E − E')² e_q`.

*Proof.* Apply T2, then T1 (runner D1). The eigen-coin form is checked at an exact pair with energies `1` and `3/5`: both sides equal `−96/625` (D2). ∎

## Theorem T4 — the member without averages

*Statement.* Take block 135 T4(a)'s member at `β = −α`, with the plain site energy `e` sourcing its clock and `K^s` as its stress. Its demand `ë = −(K/(4α)) p·K^s·p = (K/(4α)) ∇̄∇̄:K^s` holds for every state iff `α = K/4`.

*Proof.* By T3, `ë = ∇̄∇̄:K^s` for every state. The double divergence is non-zero on the pair of T3, so the ratio `K/(4α)` must be one (runner E1). ∎

Averaging both sides of T3 over the eight body-diagonal neighbours multiplies them by `Π_l cos q_l`. That gives an identity of block 135's form for `e′ = C₁C₂C₃e`, with the correspondingly averaged stress. Block 135 T3(b) and block 136 T3 exclude stated unaveraged placements. The placement `f` used here is a different one.

## Theorem T5 — every constraint kept, without averages

*Statement.* Take block 136 T4's member at `β = −α`, with a bond shift coupled to `P^s`, the plain site energy `e` sourcing the clock, and `K^s` as the stress. Block 136 T4(b)'s conditions are, quoted: "  - `Ṗ_z = −pΘ_zz` and `Ṗ_x = −pΘ_xz`, with the symmetric stress;" and "  - `ė_u = (Kw̄²/(4α)) pP_z`." They hold for every state iff `α = K/4`. So, with block 136's qualifiers, the initially satisfied nonzero-mode lapse and shift constraints are kept for every free-walk source, without averages. The qualifiers are: initially satisfied constraints, non-zero `q`, and the member's algebra as block 136 executed it along one wave-vector axis.

*Proof.*
- The first condition is T2, since `K^s` is symmetric.
- By T1, `ė = −∇̄·P^s` for every state. The second condition asks `ė = (K/(4α))(−∇̄·P^s)`.
- `∇̄·P^s` is non-zero on the pair of T3, so `K/(4α) = 1` (runner E2).
- The member's side, (a) and (b), is block 136 T4 as landed. The placements agree: `e` sits on sites, `P^s_j` on the bond `x → x + e_j` (its symbol carries `e^{iq_j/2}`), and `K^s_aj` at `x + (e_a + e_j)/2`, where block 136 places the clock, the shift and the lengths. ∎

## What this settles and what it does not

- **Settled.**
  - The symmetric books of the two-step content hold exactly without averaging: energy flows as `P^s`, `P^s` flows as the symmetric `K^s`, and `ë = ∇̄∇̄:K^s`.
  - Block 135's member identity, and block 136's conditions for keeping every nonzero-mode constraint, then hold with the plain site energy iff `α = K/4`. The clock can be sourced, and by action and reaction felt, site by site rather than through `C₁C₂C₃`.
- **Not settled.**
  - Uniqueness of the placement.
  - Zero modes, and the member's field equations beyond block 136's constraints.
  - Rates, varying frames and one record per site (block 137's losses remain).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 135 and 136 as landed: exact books and the member's identity with body-diagonal and transverse averages; unaveraged placements fail"
source_of_blocker_text: admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; the member's full equations with K^s; rates"
conditional_surface_status: "exact operator identities at uniform rate; the member's longitudinal identity"
hypothetical_axiom_status: "the walk, its densities, the placement and the member are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.** Landed, the supervisor's own:
  - block 135: the member's identity with averages;
  - block 136: averaged symmetric books;
  - block 138: the symmetric momentum as the two-step momentum plus half the curl of the spin.
- **Block 179** (pushed): `P^s` and `K^s`.
- **In the literature.** A symmetric energy-momentum tensor conserved on a field's equations is Belinfante's and Rosenfeld's construction. Here it holds exactly on the lattice, site by site. None is used as authority.
- **New here.**
  - The exact energy continuity with current `P^s` (T1). With block 179's T2 this gives the whole tensor without averages.
  - The member's identity with the plain site energy (T3, T4).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: the member's identity without averages. The obligations are:
- (O1) the premises (A3);
- (O2) energy continuity (B1);
- (O3) momentum continuity and symmetry (C1);
- (O4) the double divergence (D1, D2);
- (O5) the member's ratio (E1);
- (O6) every constraint (E2).

## No-Go Discipline Gate

The note's negative sentence: no ratio other than `α = K/4` lets block 135's member admit the content with the plain site energy and `K^s`.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A different ratio.* The double divergence is non-zero on an exact pair, so the ratio is forced. ATTEMPTED; closed.
2. *A different placement.* Block 135 T3(b) and block 136 T3 exclude stated unaveraged placements; this one works. Other placements are not examined.
3. *Zero modes.* Not examined, as in blocks 135 and 136.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the uniform rate, the placement, and the member's longitudinal identity.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the two-step momentum | yes (quoted, A3) |
| block 135 (landed) | the member's demand; the averaged identity; the failing unaveraged realisation | yes (quoted, A3) |
| block 136 (landed) | the averaged books; the failing unaveraged momenta; T4(b)'s conditions | yes (quoted, A3) |
| block 179 (pushed) | `P^s`, `K^s` | re-derived (C1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "energy flows as `P^s`, `P^s` as the symmetric `K^s`; `ë = ∇̄∇̄:K^s`; the member's identity and every constraint iff `α = K/4`" | executed: continuity as matrix symbols | executed: the double divergence | executed: an exact pair of unequal energies | executed: the member's ratio, twice | every state, as operator identities; zero modes not examined |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 135 said no convolution of the site energy repairs the unaveraged realisation."
  - *Reply:* That is about block 120's realisation. The repair here is in the current, not the energy. `K^s` is a different placement of the two-step stress, and with it the site energy needs no convolution.

### N8 — Cross-cycle echo
- Block 135: the identity with averages.
- Block 136: averaged symmetric books.
- Block 179: `P^s` and `K^s`.
- This note: the books and the identity without averages.

## Falsifiers

- A pair `(k, k')` at which any of the symbol identities of T1–T3 fails.
- A state for which `ë ≠ ∇̄∇̄:K^s`.

## Boundaries and non-claims

- Uniform rate; identity frame; the member's longitudinal identity only.
- The densities, the placement and the member are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 69, 135 and 136 (landed), quoted. Block 179 (pushed), re-derived.
- Named standard imports, at definition level:
  - symbols of translation-covariant local forms;
  - summation by parts;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Third version (after a same-family adversarial review).**
  - Block 136 T3 is described as it is.
  - T5 carries block 136's qualifiers.
  - The reviewer also reports that block 136's objects are exactly the body-diagonal averages of these: `Θ^sym = C₁C₂C₃K^s`, `P^B = C₁C₂C₃P^s` and `e′ = C₁C₂C₃e`. So the identities here are block 136's with the average removed. `C₁C₂C₃` annihilates modes with some `q_l = ±π/2`, so they say strictly more. This is not re-verified here.
- **Before writing.** Origin was re-fetched. Blocks 69, 135, 136 and 138 were read as landed. The landed notes and the probes' attempts were grepped for "unaveraged", "without averaging" and "site energy"; none has an exact unaveraged version.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_symmetric_books_without_averaging_2026_09_27.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
