---
claim_id: admissibility_rule_only_the_two_step_current_can_source_block_62s_symmetric_member_no_local_placement_of_the_frame_response_or_of_the_one_step_current_keeps_its_divergence_condition_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied identity-frame uniform-rate walk and declared quadratic tensor member. Reflection-state responses
  span the stated spaces, excluding real finite-range translation-invariant linear placements of the fixed site
  response or one-step current with their prescribed uniform normalization that work for all stationary plane-wave
  states. The two-step current has a transposed identity for finite equal-energy wave sums and finite periodic eigenspaces;
  an explicit local averaging makes its source compatible. Modewise static solvability follows for nonzero q and
  nonzero tensor coefficient under an explicit phase reindexing of the parent member. No uniqueness among all improved
  currents, zero-mode solution, self-consistent nonlinear coupling, or physical field is established.
upstream_dependencies:
- admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
- admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
- admissibility_rule_the_two_step_momentum_is_the_only_one_among_conserved_covariant_momenta_of_reach_two_that_is_every_species_own_wave_number_bounded_theorem_note_2026-09-21
- admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_only_the_two_step_current_can_source_block_62s_symmetric_member_2026_09_24.py
---

# Local placements of three specified walk responses: two obstructions and a compatible two-step construction

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 62, 63, 64 and 73 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 62, 63, 64 and 73 as landed on main, with the walk in the identity frame at uniform rates; it reports which placements of the walk's currents can source block 62's symmetric member without breaking its divergence condition; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 62, as landed, gives a symmetric member for the lengths. Its static equations can be solved exactly when the source is divergence-free, meaning orthogonal to the relabelling directions. Block 62 leaves one question open: "The site-centered frame response of T2 requires a declared transfer/interpolation to those face components. Its preservation of the divergence condition is not established here." Two review items deferred when blocks 62–65 landed ask the same thing of the currents. This note answers all three.

- **T1: reflection states.** Two plane waves mirrored about `k₁ = π/2` form a stationary state with simple closed-form responses. As the other two wave numbers vary, their responses at one wave vector fill everything a local rule would have to respect.
- **T2: the frame response cannot be placed.** No local transfer of the site-centred frame response onto the member keeps the divergence condition on every stationary state.
  - An exact witness: the simplest transfer, paired with one relabelling on one reflection state, gives `−1152/625`, not zero.
  - Block 62's question has a negative answer within this specified placement class.
- **T3: nor can the walk's one-step momentum current.** It is conserved, but no local realisation keeps the member's condition. The exact witness gives `−1728/3125`.
- **T4: the specified two-step current can, for the stated monochromatic states.**
  - The current of block 73's two-step momentum obeys a second, transposed conservation law.
  - One explicit local averaging onto the bonds (`φ_j`) then makes it exactly compatible with the member on every stationary state.
  - With block 62 T5, the member's static equation with this source can be solved at every nonzero wave vector.

In plain terms, block 62 has a candidate field for the lattice's lengths, and asks what the walker can feed into it. The obvious quantities, the walker's local "frame stress" and the flow of its ordinary momentum, fail. For any real, translation-invariant, finite-range linear map with the stated uniform normalization, some steady walker state produces a source the field equations cannot absorb. The two-step momentum works; block 73 found it is the same for all eight species. Its flow satisfies a second conservation law, and a simple local averaging turns it into a source the field can always absorb away from zero wave vector. Records alone do not choose it: the two-step momentum is a supplied choice.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "Each site has a domain of local possibilities." The coin and its amplitude walk are separately supplied.
  - "Admissibility is not a dynamics axiom." It does not "define a time metric". The walk, its currents and the lengths member are supplied clauses. Nothing is adopted.
- **The walk.**
  - `(T_aψ)(x) = ψ(x + e_a)`, `S_a = (T_a − T_a⁻¹)/(2i)` and `C_a = (T_a + T_a⁻¹)/2`.
  - `H = Σ_a σ_a S_a` in the identity frame, at uniform rates (block 54 as landed).
  - `P_j = S_jC_j` is block 73's two-step momentum, with symbol `½ sin 2k_j`.
- **Responses.**
  - The frame's site response is `Θ_a^j(x) = Re ψ†(x)σ_a(S_jψ)(x)` (block 62 T2).
  - Bond currents live on `x → x + e_a`:
    - `J_a^j = ½Re[ψ†(x+e_a)σ_a(S_jψ)(x) + (S_jψ)†(x+e_a)σ_aψ(x)]` (block 63);
    - `K_a^j` is the same with `P_j`.
  - These are the responses of block 64's bond coupling and of block 73's.
- **The member** (block 62 as landed), in site convention.
  - A function `F(h)` of a symmetric field `h_ij(x)`, invariant under the relabellings `(Gξ)_ij = −(d_iξ_j + d_jξ_i)`, with `d_a f(x) = f(x + e_a) − f(x)`.
  - The parent member is explicitly pulled back by unit-modulus component phases. At wave vector q define h_st,ij=exp[-i(q_i+q_j)/2] h_site,ij and xi_st,j=exp[-iq_j/2] xi_site,j. Then the forward-difference G becomes -i(p_i xi_st,j+p_j xi_st,i), p_i=2 sin(q_i/2). These phases reindex staggered components; they do not assert a fractional-site interpolation of arbitrary site data. Define F_site(h)=F_parent(h_st) with its scalar variable unchanged, and transform sources by the adjoint phase map. Rank and source orthogonality are preserved. Assume the parent's tensor coefficient K is nonzero (K>0 suffices).
  - Its static equations with source `Σ` can be solved at nonzero wave vector exactly when `⟨Σ, Gξ⟩ = 0` for all `ξ` (block 62 T5).
- **Placements.**
  - A *local transfer* is a real, translation-invariant, finite-range linear map `ε = Ph` from the member's field to the frame's strain. A *local realisation* is such a map `B = Rh` to a bond strain.
  - Each is normalised so that the walker sees the member's uniform field: `sym P(0) = −½`, and `ΛR(0) = 1` with `Λ(B)_ij = −(B_i^j + B_j^i)`.
  - *Compatibility* on a stationary state means `⟨Θ, PGξ⟩ = 0`, `⟨J, RGξ⟩ = 0` or `⟨K, RGξ⟩ = 0` for every finitely supported `ξ`. It is necessary for the member's static equation at first order in the strain.

## Theorem T1 — reflection states and their spans

*Statement.* Take `cos θ ≠ 0 ≠ sin θ` and any `k₂, k₃`. Put `s = (cos θ, sin k₂, sin k₃)` and `E = ±|s|`, with `(s·σ)χ = Eχ`. Let `k = (π/2 + θ, k₂, k₃)` and `k' = (π/2 − θ, k₂, k₃)`.
- (a) `ψ = χ(e^{ik·x} + e^{ik'·x})` has `Hψ = Eψ`. With `ρ = |ψ|²`:
  - `Θ_a^j = s_as_jρ/E`;
  - `J₁^j = 0`;
  - `J_a^j = s_as_j cos k_a ρ/E` for `a = 2, 3`.
- (b) At `q = (2θ, 0, 0)`, as `(k₂, k₃)` vary, the `q`-parts span:
  - `Sym(3)` for `Θ`;
  - `{v₁ = 0} ⊗ ℂ³` for `J`, which is the whole space where conserved currents at `q` live.

*Proof.*
- (a) `sin(π/2 ± θ) = cos θ`, so `s(k) = s(k')` and `S_jψ = s_jψ`. For `a = 1` the bond factor is purely imaginary.
- (b) The `e^{iq·x}` part of `ρ` is `|χ|²`. The spans are six determinants, polynomial in `cos θ`. ∎

*Checked (B1, B2).*
- (a) holds exactly at all 125 sites of `[−2, 2]³`, for three states with rational data.
- (b) Over six rational samples the determinants are nonzero multiples of `cos²θ` and `cos⁴θ`, so they are nonzero for every `cos θ ≠ 0`.

## Theorem T2 — the frame response cannot be placed

*Statement.*
- No local transfer `P` with `sym P(0) = −½` keeps the member compatible on every stationary state of `ℤ³`.
- For any one fixed finite-range transfer P, compatibility on all stationary states of the L^3 tori with 4 dividing L can hold for at most finitely many L. This does not exclude rules changed with L or a special finite-size rule.

*Proof.*
- On a two-wave state, compatibility reads `⟨Θ̂(q), P(q)G(q)w⟩ = 0` for all `w ∈ ℂ³`. By T1(b) this gives `sym(P(q)G(q)w) = 0` at every axis `q`.
- `G(te_c)w/t → −i(e_c ⊗ w + w ⊗ e_c)` as `t → 0`, and `P` is continuous. So `sym P(0)` annihilates `Sym(3)`, which contradicts `sym P(0) = −½`.
- On an unbounded sequence of such tori, take theta=2pi/L and q_L=(4pi/L)e_c; the reflection momenta pi/2 +/-theta belong to their grids. For each of the six transverse samples, choose nearest allowed k2,k3. As L grows their span matrices approach the nonzero sample determinants at cos(theta)=1, so are invertible eventually by continuity. Divide G(q_L) by |q_L| and pass to P(0) as above. The fixed transfer's normalization is then contradicted. ∎

*Checked (C1).* The simplest transfer `ε = −h/2`, on the reflection state with `s = (4/5, 3/5, 0)` and the relabelling `ξ = e₁δ₀`, pairs to `−1152/625`.

## Theorem T3 — the one-step current cannot be realised

*Statement.* `J` is conserved. Still, no local realisation `R` with `ΛR(0) = 1` keeps the member compatible with block 64's coupling on every stationary state.

*Proof.* By T1(b), compatibility at `q = te_c` forces `R(q)G(q)w ∈ e_c ⊗ ℂ³`. As `t → 0`, `R(0)(e_c ⊗ e_d + e_d ⊗ e_c)` must lie in `e_c ⊗ ℂ³ ∩ e_d ⊗ ℂ³ = {0}` for `c ≠ d`. But `Λ` of it must be `e_c ⊗ e_d + e_d ⊗ e_c`. ∎

*Checked (D1).*
- `Σ_x J·dη = 0` for a finitely supported `η` (conservation).
- The plain realisation `B = −h/2`, on the same state against `ξ = e₂δ₀`, pairs to `−1728/3125`.

## Theorem T4 — the two-step current can

*Statement.*
- (a) **A transposed law.** On every finite superposition of plane waves of one real energy, and hence every eigenstate of a finite periodic walk, for every site `x` and every `a`:
  `Σ_j Π_{l≠j} C_l [K_a^j(x + e_j) − K_a^j(x − e_j)] = 0`.
- (b) **A compatible realisation.** `B_i^j = −½ φ_j h_ij`, with `φ_j = ½(1 + T_j⁻¹)Π_{l≠j} C_l`.
  - `φ_j = 1` on uniform fields, so the normalisation holds at `q = 0`.
  - This realisation keeps the member exactly compatible with block 73's coupling on those states.
- (c) **Solvability.** With block 62 T5 (the static null space at nonzero wave vector is exactly the relabellings), the member's static equation with this source can be solved at every nonzero wave vector.

*Proof.*
- (a) For a finite sum `ψ = Σ_k χ_k e^{ik·x}` of one real energy `E`, each pair `(k, k')` of `K` carries `½(P_j(k) + P_j(k'))`. Also `sin q_j (P_j(k) + P_j(k')) = cos q_j (sin²k_j − sin²k'_j)`. The combination then multiplies each pair by `Π_l cos q_l (|s(k)|² − |s(k')|²) = 0`.
- (b) `φ_j d_j = ½(T_j − T_j⁻¹)Π_{l≠j}C_l`, and its transpose is its negative.
  - The part of `⟨K, B⟩` with `d_iξ_j` vanishes by conservation.
  - The part with `d_jξ_i` vanishes by (a).
- (c) The source is orthogonal to G. After the unitary component reindexing above it is orthogonal to the parent's three null directions. At any nonzero q in the Brillouin zone p is nonzero, and the parent's nondegenerate static matrix has precisely those null directions, so its finite mode equation has a solution modulo them. This is a fixed-source linear equation only: no q=0 compatibility, summability of an infinite-space inverse, or coupled nonlinear solution follows. ∎

*Checked (E1, E2).*
- (a) holds at all 27 sites of `[−1, 1]³` for each `a`, on an exact energy-1 superposition of five plane waves with rational sines. The same combination of `J` is nonzero at 81 of 81.
- (b) The `φ`-realisation pairs to exactly 0 against three random relabellings. The plain `B = −h/2` does not.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 62 as landed: 'The site-centered frame response of T2 requires a declared transfer/interpolation to those face components. Its preservation of the divergence condition is not established here.'; the deferred review items U7-R4 (site-to-face transfer) and U7-R5 (q-only numerical no-go) of blocks 62-65"
source_of_blocker_text: block 62 as landed; the deferred PR #8590-#8597 review items
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a realisation of the two-step current with Lambda R(q) = 1 at every q; the q = 0 (global) condition; versions of T2-T3 demanded only near one species point"
conditional_surface_status: "T1-T4 exact for the supplied walk and member; T4(c) rests on block 62 T5 as landed"
hypothetical_axiom_status: "the walk, its currents and the member are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 62: the member, its relabellings and T5, and the open placement question.
  - Block 63: the one-step current.
  - Block 64: the bond coupling.
  - Block 73: the two-step momentum and its current.
  - Block 74: the two-step current serves all eight species.
- **The probes attempt.** `deferred-20260924-ledger` a1 (Claude Opus 5.5, issue #9060) found T1–T4. A Grok referee confirmed them (#9110). It built on the site convention and realisation formalism of `a-bond-placed-stress-for-the-walk` a3 (issue #8636; its referee report is #9136).
- **In the literature.**
  - That a canonical momentum current need not be a consistent source for a symmetric tensor field, and that an improved current can be, is the situation of the canonical and symmetric stress tensors (Belinfante; Rosenfeld). Reference only.
- **New here:**
  - an independent exact runner, reproducing both witnesses (`−1152/625`, `−1728/3125`) and the compatible realisation;
  - the answer placed against block 62's open question.

## Exact target and obligation graph

Target: block 62's placement question and the deferred items U7-R4 and U7-R5. The obligations are:
- (O1) states that probe every local rule;
- (O2) the site response;
- (O3) the one-step current;
- (O4) the two-step current.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- no local transfer of the frame response;
- no local realisation of the one-step current.

### N1 — Routes by which the sentences could fail or mislead
1. *Near one species point.* At an axis wave vector the species-0 component gives only currents in the `{2,3}²` block. There the plain transfer and realisation pass. T2 and T3 rest on states in the middle of the zone.
2. *Non-local placements.* Excluded by definition. A non-local rotation part could restore strict normalisation for the two-step current (open).
3. *Other frames or rates.* The theorems are at the identity frame and uniform rates, at first order in the strain.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- T4(c) uses block 62 T5 as landed.
- The q=0 part is a separate global condition. The proof of T4 uses finite equal-energy wave expansions; arbitrary unbounded generalized eigenfunctions are outside the claimed domain.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| blocks 62, 63, 64, 73 (landed) | the member, the currents and the couplings | yes (restated) |
| block 74 (landed) | the two-step current serves all species | placement |
| probes (deferred-20260924-ledger a1, #9060; Grok-refereed #9110) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "only the two-step current can source block 62's member through a local placement" | executed: the closed forms of `Θ` and `J` on reflection states | executed: 125 sites for the states; 27 for the transposed law | executed: the spans as determinants in `cos θ` | executed: both witnesses; conservation; the `φ`-realisation against three relabellings | no-go witnessed by stationary plane waves on Z^3; T4 for finite equal-energy sums and finite periodic eigenspaces; torus no-go concerns one fixed placement across unbounded sizes; T4(c) through block 62 T5; the clauses supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "One transfer failing on one state proves nothing about all transfers." *Reply:* The witness only illustrates. The proof is the spanning argument of T2, which constrains `P(0)` from the reflection states at every axis wave vector.
- *Objection:* "The two-step current's realisation is not normalised at `q ≠ 0`." *Reply:* Agreed, and listed as open. The normalisation holds at `q = 0`, which is what the walker's uniform field needs.

### N8 — Cross-cycle echo
- Block 62 found the member and asked how the frame response is placed.
- Blocks 63 and 73 found the one-step and two-step currents, and block 74 found that the two-step current serves all species.
- This note finds that within these three fixed responses and placement definitions, the two-step construction is compatible; other improved currents are unclassified.

## Falsifiers

- A local transfer with `sym P(0) = −½` compatible on every reflection state.
- A stationary state on which the transposed law for `K` fails.
- A relabelling against which the `φ`-realisation pairs to a nonzero value.

## Boundaries and non-claims

- The walk, its currents and the member are supplied.
- The `q = 0` condition and strict normalisation of the realisation at `q ≠ 0` are not treated.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 62, 63, 64, 73 and 74, restated or placed.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - Fourier analysis of two-wave states;
  - continuity of trigonometric-polynomial symbols;
  - exact rational and symbolic arithmetic.
- Reference only: Belinfante; Rosenfeld.

## Review record

- **Who and when.** Supervisor-run block, the sixty-eighth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (`deferred-20260924-ledger` a1, #9060). A Grok referee confirmed them (#9110).
  - The supervisor re-checked them with its own runner.
- **Before writing.** Main was re-fetched, and blocks 62 and 63 were read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_only_the_two_step_current_can_source_block_62s_symmetric_member_2026_09_24.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.

## Current source dependencies

- [Current conditional input](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current conditional input](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current conditional input](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current conditional input](ADMISSIBILITY_RULE_THE_TWO_STEP_MOMENTUM_IS_THE_ONLY_ONE_AMONG_CONSERVED_COVARIANT_MOMENTA_OF_REACH_TWO_THAT_IS_EVERY_SPECIES_OWN_WAVE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
