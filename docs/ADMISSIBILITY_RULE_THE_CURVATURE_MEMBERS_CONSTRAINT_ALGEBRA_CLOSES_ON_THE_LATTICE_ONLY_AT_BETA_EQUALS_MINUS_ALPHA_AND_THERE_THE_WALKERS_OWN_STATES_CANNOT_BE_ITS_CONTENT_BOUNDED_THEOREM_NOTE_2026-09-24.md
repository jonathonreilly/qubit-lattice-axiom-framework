---
claim_id: admissibility_rule_the_curvature_members_constraint_algebra_closes_on_the_lattice_only_at_beta_equals_minus_alpha_and_there_the_walkers_own_states_cannot_be_its_content_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: For the supplied staggered constraint stencil at flat strain, the term linear in canonical momentum
  closes at beta=-alpha for the three specified symmetric face means; one-corner timing fails. A trace obstruction
  excludes other nonsingular kinetic ratios. For the separately supplied quadratic action at nonzero momentum, a
  source identity and an explicit violating two-wave symbol are derived. Using the site response as staggered stress
  requires the declared transfer; no universal obstruction to coupling walkers or nonlinear constraint closure is
  proved.
upstream_dependencies:
- admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
- admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
- admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23
runner: scripts/admissibility_rule_the_curvature_members_constraint_algebra_closes_only_at_beta_equals_minus_alpha_where_the_walker_cannot_be_its_content_2026_09_24.py
---

# Flat-strain constraint closure and a conditional source-compatibility witness

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within the supplied clauses of blocks 60, 62 and 101 as landed; harvest block from three Grok-refereed probes attempts, re-checked by an independent runner; nothing adopted or registered; unaudited)

This note studies the supplied staggered constraint stencil and quadratic nonzero-mode action, with an explicitly chosen transfer of a walker response to its abstract source; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 101, as landed, found that in the curvature member the clock is a constraint. Two transverse strains have nonzero oscillatory frequencies; zero-frequency sectors and additional constraints need separate treatment. At the kinetic ratio `β = −α` its elimination is singular. Block 62, as landed, flagged the same ratio. This note asks two things. Do the constraints for different clock profiles (lapses) close into an algebra on the lattice? And if they close only at one ratio, can the walker be the member's content there?

- **T1: closure, exactly on the lattice.** At flat strain, for the term linear in canonical momentum, the bracket of two lapse constraints `C[N]`, `C[M]` equals the strains' relabelling generator, with the bond field `ξ_j(x → x + e_j) = (K/(4α))(N_{x+e_j} M_x − N_x M_{x+e_j})`. It does so for every lapse and at every nonzero symbol wave vector, within the four timing prescriptions stated below, if and only if two conditions hold:
  - `β = −α`;
  - the face timing is the mean of its four corners or either pair of opposite corners, among the four prescriptions examined.

  One-corner timing fails. For `β ≠ −α` the bracket's obstruction lies outside the span of all relabellings.
- **T2: the same ratio is a symmetry.** At `β = −α` the gradient relabelling `h → h + p pᵀ ζ`, `u → u − (2α/(K w̄²)) ζ̈` changes the action by a total derivative plus `ζ[(2α/(K w̄²)) ë + p·Θ·p/2]`. For `β ≠ −α` a term proportional to `α + β` remains.
- **T3: what the symmetry demands of the content.** At `α + β = 0` the equations of motion require, at every nonzero lattice-symbol wave vector,

  `ë = −(K w̄²/(4α)) p·Θ·p`.

  This is the second time derivative of continuity with momentum balance, when the content's energy current is `K w̄²/(4α)` times its momentum density. It is not continuity itself: a constant rate of change of energy is left free.
- **T4: the walker fails it.** Take two positive-branch waves of the walk with the same energy, for example `k₁ = (a, b, 0)` and `k₂ = (−b, a, 0)` with `sin a = 3/5` and `sin b = 5/13`. Their superposition is stationary, so `ë = 0` at the difference wave vector. But the walker's frame response there has `p·Θ·p = 128√2146 (1 − i)/65⁴ ≠ 0`. So:
  - at the ratio that closes the algebra, the nonzero-mode equations have no solution with this explicitly transferred source;
  - by block 62's T5 as landed, the static equations have none at any ratio, since `p·Θ ≠ 0`.

In plain terms: the rules for how clocks and lengths respond to content fit together consistently, as an algebra, only at one setting of the length field's kinetic numbers. At that setting a source identity appears. Continuity and momentum balance with the stated current coefficient imply it; the identity does not imply those full conservation laws. The walker's natural stress does not do that: two of its waves can sit perfectly still while their stress pattern would have to push. So the walker and this clock-and-length field do not yet fit together. Something else has to supply a stress the field accepts. The explicit identity-transfer witness fails; this says nothing about every possible walker-to-field source coupling.

## Premises and declared objects

Supply K>0, alpha>0, wbar>0 and real beta. T1 uses the inverse kinetic form and excludes alpha+3beta=0; it does not analyze the additional constraints at that singular ratio. T1 refers only to the bracket of the linear spatial constraint with the quadratic kinetic term at h=0; higher strain orders of a nonlinear constraint are absent. T2–T4 concern nonzero real symbol momentum p. At p=0 the multiplier instead requires e0=0; no finite torus with unbalanced positive mean source is constructed.

The walker frame response is site-centered, whereas the tensor shear variables are face-centered. Current block62 explicitly leaves this transfer open. Here T4 SUPPLIES identity transfer of the complex Fourier-component values in the stated symbol convention to the abstract staggered symmetric source. No locality, uniqueness or physical necessity of this transfer is asserted. Other transfers or conserved bond stresses may avoid the obstruction.

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The clocks, lengths, kinetic term and walk are supplied clauses. Nothing is adopted.
- **Block 62** (#8592, landed).
  - The placement: `h_jj` on sites, `h_ij` (`i < j`) on the faces spanned by `e_i` and `e_j`, relabellings `ξ_j` on the bonds along `j`. Every difference between neighbouring places has the symbol `p_j = 2 sin(k_j/2)`.
  - `R₁ = p² tr h − p·h·p` and `R₂` (block 62 T3).
  - The kinetic family `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]`.
  - The frame response `Θ_a^j(x) = Re ψ†(x) σ_a (S_jψ)(x)`, with `∂⟨H⟩/∂h_ij = −½Θ_(ij)`.
  - T5: static equations with stress sources are solvable iff `Σ_i p_i Θ_(ij) = 0`.
- **Block 101** (#8895, landed): the quadratic action `L = [α tr(ḣ²) + β (tr ḣ)²]/w̄ + K w̄ (u R₁ + R₂) − e u`, to which the stress coupling `½ Σ_ij Θ_ij h_ij` of block 62 is added here.
- **Constraints and brackets.** `C[N]` is the per-tick energy with the clocks replaced by a lapse `N` on sites. Its kinetic part is the Legendre transform `(1/(4α))[Σ_j P_jj² − c(Σ_j P_jj)²] + Σ_{i<j} P_ij²/(8α)`, with `c = β/(α + 3β)`.
  - A face term's lapse is a declared timing: the four-corner mean, an opposite-corner mean, or one corner. The unit's clocks live on sites, so the timing of a face term is a supplied clause.
  - `G[ξ] = Σ P·δ_ξ h`, with `δ_ξ h_ij = ∂_i ξ_j + ∂_j ξ_i`.
- **Names.** Relabelling identities from a symmetry of the action are Noether's second theorem. The closure of lapse constraints onto spatial relabellings is the structure of the comparator's constraint algebra (Dirac; Bergmann; Hojman, Kuchař and Teitelboim). The kinetic ratio `β = −α` is DeWitt's.

## Theorem T1 — closure on the lattice

*Statement.* At flat strain, for the term linear in canonical momentum, `{C[N], C[M]} = G[ξ]` with `ξ_j(x → x + e_j) = (K/(4α))(N_{x+e_j} M_x − N_x M_{x+e_j})`, exactly on the lattice and for every pair of lapses, within the four declared timing prescriptions, if and only if both of these hold:
- `c = 1/2`, that is `β = −α`;
- the face timing is the four-corner mean or one of the two opposite-corner means. No classification of arbitrary nonlocal or field-dependent timings is asserted.

For `β ≠ −α` the bracket is `b(c) = b(1/2) + (1 − 2c) b₁`, and `b₁` lies outside the span of all relabellings.

*Proof.* Write Delta_j N=N_(x+e_j)-2N_x+N_(x-e_j). The diagonal R1 derivative is -sum_i Delta_i N+Delta_j N and its trace is -2sum_i Delta_i N. At c=1/2 the kinetic contraction leaves Delta_j N, so antisymmetrization gives K[M Delta_j N-N Delta_j M]/(2alpha), exactly twice the backward difference of the stated xi_j.

For a face with corner labels 00,10,01,11, put dN=N00-N10-N01+N11. Its bracket coefficient is K[(mean M)dN-(mean N)dM]/(2alpha). Expanding the four-corner means gives the forward i difference of xi_j plus the forward j difference of xi_i. Either opposite-corner mean differs from the four-corner mean by plus or minus dM/4, which cancels in the antisymmetrization. This is a local polynomial identity, independent of torus size (side at least three). One-corner timing fails already for N10=M00=1 and all other face values zero: its coefficient is twice the required one.

For other c the additional diagonal coefficient is affine in (1-2c). Take N a delta at 0 and M a delta at e1 on a torus of side at least three. In b(0)-b(1/2), the yy coefficient is K/(2alpha) at 0, -K/(2alpha) at e1 and zero elsewhere. At either fixed x1 its sum over x2,x3 is nonzero. Any relabelling coefficient G_yy=2 backward_difference_y xi_y has zero such sum by telescoping. Therefore this obstruction lies outside the relabelling image for every c!=1/2. The runner's complete 3³ rank witness corroborates this analytic projection argument; three sampled lapse pairs are not the general proof. The equivalence c=1/2 iff beta=-alpha uses alpha+3beta!=0. ∎

## Theorem T2 — the ratio that closes is a symmetry

*Statement.* Along `p = p ẑ`, write `h = [[φ + a, b, c_x], [b, φ − a, c_y], [c_x, c_y, 2ξ_L]]`, so that `R₁ = 2p²φ`.
- At `β = −α` the gradient relabelling `ξ_L → ξ_L + p²ζ/2`, `u → u − (2α/(K w̄²)) ζ̈` changes the action with sources by `d/dt[−(4αp²/w̄) ζ̇ φ + (2α/(K w̄²))(e ζ̇ − ė ζ)] + ζ[(2α/(K w̄²)) ë + (p²/2) Θ_zz]`.
- For `β ≠ −α` a remainder proportional to `α + β` survives.

*Proof.* The kinetic change at `β = −α` is `−(4αp²/w̄) ζ̇ φ̇`, and the multiplier's change is `−(4αp²/w̄) ζ̈ φ`: together a total derivative. The sources give the rest. The runner checks this symbolically, and checks that the remainder vanishes only at `β = −α` (C1). ∎

## Theorem T3 — the identity the content must obey

*Statement.* At `α + β = 0` the `u`-equation is the constraint `2K w̄ p² φ = e`, and the longitudinal relabelling's equation then reads

`ë = −(K w̄²/(4α)) p·Θ·p`.

If `ė + i p·J = 0` and `Ṗ + i p·Θ = 0` with `J = c P`, then `ë = −c p·Θ·p`. So the identity is these two laws differentiated once more, exactly when `c = K w̄²/(4α)`. A constant `ė` stays free.

*Proof.* The equations of motion of the mode action, eliminated symbolically (D1). This is also T2's source term: a symmetry of the action holding only up to that term forces the term to vanish (the second theorem named under Premises). ∎

## Theorem T4 — the walker is not such content

*Statement.* Use the infinite-lattice/general momentum symbol, not a claim that these momenta are allowed on an arbitrary finite torus. Choose a,b in (0,pi/2), cos a=4/5, cos b=12/13 and unnormalized spinors chi(s)=(s_x-i s_y, epsilon)^T. Their normalization sets the quoted nonzero amplitude; normalizing both rescales it without removing the obstruction.
- The walk's positive-branch waves `k₁ = (a, b, 0)` and `k₂ = (−b, a, 0)`, with `sin a = 3/5` and `sin b = 5/13`, have the same energy squared, `2146/4225`. Their superposition is stationary, and `ë = 0` at `q = k₂ − k₁`.
- The frame response at `q`, `Θ_a^j = ½ χ₁† σ_a χ₂ (sin k₁ + sin k₂)_j`, has `p·Θ·p = 128√2146 (1 − i)/65⁴ ≠ 0`, and `p·Θ ≠ 0` in every component.
- So T3 fails: at `β = −α` the nonzero-mode equations have no solution with this explicitly transferred source. By block 62 T5 as landed, the static equations have no solution at any ratio.

*Proof.* Exact algebraic arithmetic on the two eigenvectors (E1). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 101 as landed: the clock is a constraint, elimination singular at beta = -alpha; block 62 as landed: beta = -alpha to be analysed separately; the fork probe's lens: closure may fail at O(p^2) on the lattice"
source_of_blocker_text: blocks 62 and 101 as landed; decision record (fork probe, gravitation lens)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a stress for the walker that the member accepts (a conserved bond stress, block 63's current), and whether the walker's own bracket closes with speed 1 (the common cone K = 4 alpha)"
conditional_surface_status: "T1 exact on every torus at flat strain, at leading momentum order for block 62's placement; T2-T3 exact at every nonzero lattice-symbol wave vector for block 101's action; T4 exact for block 62's frame response as the stress"
hypothetical_axiom_status: "the member, the kinetic family, the face timing and the stress coupling are hypotheses; nothing adopted"
admitted_observation_status: "the comparator's constraint algebra and ratio are comparators only"
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 101 (landed) gave the constraint, the elimination and its singular case. There, in the zero-stress model, `ë = 0` at `β = −α`.
  - Block 62 (landed) gave the placement, the kinetic family, the frame response and the static compatibility condition. It noted that at `β = −α` the mode determinant vanishes identically.
  - The fork probe's gravitation lens (decision record) expected that closure might fail at `O(p²)` on the lattice. For this placement it does not.
- **The probes attempts.** All three were written by Claude Opus 5.5 and refereed by a Grok model, confirmed:
  - `constraint-algebra-closure-for-block-62s-kinetic-numbers` a2 (`w-jonathonsmac4f50-ja536`, issue #8711; referee #9033) found T1;
  - `the-kinetic-term-under-the-two-blindness-demands` a1 (issue #8734; referee #8981) found the gradient relabelling's symmetry at `β = −α`, T2's field part;
  - `the-dewitt-ratio-and-local-conservation` a2 (`w-macbookpro9927a-j5393`, issue #8921; referee #8990) found T3 and T4.
- **In the literature.**
  - The comparator's constraints close onto spatial diffeomorphisms (Dirac; Bergmann; Hojman, Kuchař and Teitelboim), with the lapses entering as `N∇M − M∇N`.
  - DeWitt's supermetric has the ratio `β = −α`.
  - The Fierz–Pauli form requires a conserved source.
  - Noether's second theorem ties a gauge symmetry to an identity among the sources.
- **New here:**
  - an independent runner with its own lattice bracket;
  - the obstruction's rank on the `3³` torus;
  - the symmetry, the identity and the witness placed against blocks 62 and 101 as landed;
  - the reading for the third column: the walker's frame response is not a stress this field accepts.

## Exact target and obligation graph

Target: whether the curvature member's constraints close on the lattice, and whether the walker can be the content at the ratio where they do. The obligations are:
- (O1) closure;
- (O2) the symmetry;
- (O3) the identity;
- (O4) the walker.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- the algebra does not close at flat strain, at leading momentum order for `β ≠ −α`, nor with one-corner timing;
- at `β = −α` the specified transferred stationary two-wave source is incompatible.

### N1 — Routes by which the sentences could fail or mislead
1. *Order.* T1 is the leading term linear in canonical momenta at flat strain. Higher strain orders are not treated.
2. *The coupling.* T4 uses block 62's frame response as the stress. A different stress coupling, for example block 63's conserved bond current, could behave differently. That is the open route.
3. *Other placements.* T1 is for block 62's staggered placement. Other placements are not treated.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The imports are named under Imports. The comparator's constraint algebra is named as a comparator, not used.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| blocks 60, 62, 101 (landed) | the member, the placement, the kinetic family, the frame response, the action | yes |
| probes (#8711, #8734, #8921; Grok-refereed) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the algebra closes only at `β = −α`, and there this transferred two-wave source is incompatible" | executed: the gradient relabelling's change of the mode action, and the equations of motion at `α + β = 0` (symbolic) | executed: the linear bracket against the relabelling generator at every strain component of a `4³` torus, for three lapse pairs and four face timings | executed: the walk's stationary two-wave state and its frame response at the difference wave vector (exact algebraic numbers) | executed: the obstruction's rank against all relabellings on the `3³` torus; the affine dependence on the ratio | T1 at flat strain, at leading momentum order for block 62's placement on every torus and every lapse; T2–T3 at every nonzero lattice-symbol wave vector; T4 for the frame response as the stress; the member, the kinetic family, the timing and the coupling supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The walker's frame response is just the wrong stress; use the conserved one." *Reply:* That may well be the way through, and it is the open route of N1. Block 62, as landed, says the frame response is not the conserved bond current. This note excludes the declared identity-transferred two-wave source at the closing ratio; other transfers and stresses remain open.
- *Objection:* "Closure at flat strain, at leading momentum order is weak." *Reply:* It is exact at every nonzero symbol wave vector at that order, with no `O(p²)` remainder, which the fork probe's lens had doubted. Quadratic order is not claimed.

### N8 — Cross-cycle echo
- Block 101 found the singular ratio; block 62 found the compatibility condition.
- This note finds that the singular ratio is the closing ratio, and that the walker's frame response fails the closing ratio's identity.

## Falsifiers

- A lapse pair on a torus for which, at `β = −α` with four-corner timing, the linear bracket differs from `G[ξ]`.
- A relabelling field removing the specified trace obstruction at a nonsingular `β ≠ −α`.
- A stationary two-wave state of the walk with `p·Θ·p ≠ 0` at the difference wave vector that nonetheless solves the member at `β = −α`.

## Boundaries and non-claims

- The member, the kinetic family, the face timing and the stress coupling are supplied.
- Higher strain orders of the constraint bracket, singular Legendre coefficients and other source transfers are not treated.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 60, 62 and 101, restated or placed. The decision record's fork probe, placed.
- The probes attempts, refereed by another model family.
- Named standard imports, at definition level:
  - Noether's second theorem;
  - the Poisson bracket of lattice fields;
  - exact rational Gaussian elimination;
  - exact symbolic arithmetic.

## Review record — historical author provenance

- **Who and when.** Supervisor-run block, the sixtieth since the source-link direction opened; 2026-09-24.
- **Provenance.** Three probes attempts by Claude Opus 5.5 derived the results (#8711, #8734, #8921), and a Grok referee confirmed each one. The supervisor re-checked them with its own lattice bracket, symbolic mode action and exact witness.
- **Not used.** The fourth related attempt, `delay-of-the-rate-field-with-the-curvature-member` a2 (#9012), derives packet displacements from block 54's fall law, which block 54 as landed withdraws. Its field-level content is already block 101's.
- **Before writing.** Main was re-fetched, and blocks 62 and 101 were read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_curvature_members_constraint_algebra_closes_only_at_beta_equals_minus_alpha_where_the_walker_cannot_be_its_content_2026_09_24.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.

## Current dependency boundaries

The current parent notes control over historical block summaries. Source placement and zero-mode compatibility remain supplied/open as stated above. Algebraic alignment of p with an axis is a tensor-coordinate calculation, not a cubic spatial symmetry. The static incompatibility concerns the same declared transferred source. No audit verdict is conferred.

- [ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23](ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md)
- [ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)
