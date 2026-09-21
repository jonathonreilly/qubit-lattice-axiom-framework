---
claim_id: admissibility_rule_three_responses_eight_species_the_frames_site_stress_has_the_wrong_sign_in_shear_for_six_species_only_the_two_step_current_serves_all_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 62, 63, 66, 69, 70 and 72 (open PRs #8570, #8592, #8593, #8597, #8601, #8602, #8605; not adopted): the walk's three responses to a deformation of lengths - the SITE STRESS of block 62's nearest-neighbour frame, Theta_a^j = Re psi^dagger sigma_a S_j psi (= d<H[E]>/dE); the BOND CURRENT J_a^j of the relabelling of reach two (block 63); the bond current K_a^j of the relabelling of reach three (block 69); block 70's exchange maps V_n; block 66's requirement on the content of a per-tick relabelling-blind ledger (minus the divergence of the response equals the energy density times the gradient of u, at lowest order); block 72: div K[phi psi] = -fP exactly on stationary states, and fP = e du at leading order for every species. (T1) Exactly, for every state, all eight species and all nine components, at every site: Theta_a^j[V_n psi] = s_n D_a D_j Theta_a^j[psi]; J_a^j[V_n psi] = s_n D_j J_a^j[psi]; K_a^j[V_n psi] = s_n K_a^j[psi]. The energy density picks up s_n (block 70). (T2) For a smooth amplitude the three responses agree at leading order in the lattice spacing, in all nine components. Hence for an amplitude of species n with a smooth envelope: Theta = D_a D_j K and J = D_j K at leading order. (T3) The species' own stress - the one whose divergence balances its weight for every species - is K. The site stress agrees with it in all nine components for two species, (000) and (111); the reach-two current for one, (000); K for all eight. For species n the frame's divergence falls short of the own stress's by twice the sum of d_a K_a^j over the axes a with D_a != D_j: under the frame, block 66's requirement is met at leading order iff the shear stress between a reflected and an unreflected axis has no gradient; under reach two iff nothing acts along a reflected axis (block 72); under reach three always. EXECUTED, NOT CLAIMED: oblique packets of species (0,0) and (1,0) on a 256x256 slice: pairings with a smooth displacement, relative to K: site stress +1.300, +1.194, +1.194, +1.097 for the first species and +1.300, -1.194, -1.194, +1.097 for the reflected one (stretch, two shears, stretch); reach-two current +1.140, +1.047, +1.140, +1.048 and -1.140, +1.047, -1.140, +1.048; the magnitudes are the lattice factors 1/(cos q_a cos q_j) and 1/cos q_j. NOT claimed: which coupling is supplied; which species are present; an exact lattice law for the site stress (block 62: there is a defect at second order for every species); anything beyond leading order in T2, T3; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_three_responses_eight_species_site_stress_bond_current_two_step_current_2026_09_21.py
---

# Three responses, eight species: the frame's site stress has the wrong sign in shear for six species; only the two-step current serves all

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about block 54's supplied walk and the three supplied couplings of lengths; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin and for three supplied couplings of lengths to them; it reports how the three responses of the walk behave under the maps that exchange its species, and what follows for the requirement a ledger places on its content; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The campaign has three ways of coupling lengths to the walker, and each makes the walker answer with a different quantity: the nearest-neighbour frame with a **stress on the sites** (block 62); the relabelling of reach two with a **current on the bonds** built with the one-step momentum (block 63); the relabelling of reach three with a bond current built with the two-step momentum (block 69). Block 72 (open PR #8605) compared the last two through their force densities and found the reach-two ledger unable to hold reflected species. This note compares all three responses directly, component by component, and brings the frame into the same table.

1. **The table** (T1, exact, every state). Under the map that carries species `n` to the first: the site stress picks up `D_aD_j`, the reach-two current `D_j`, the reach-three current nothing — each times the species' sense, which the energy density picks up too.
2. **For the first species they agree** (T2, leading order, all nine components). So for species `n` the site stress is `D_aD_j` times, and the reach-two current `D_j` times, the species' own stress.
3. **Who is served** (T3). The frame's response is right in every component for two species, `(000)` and `(111)`. For the other six it has the **wrong sign in the shear** between a reflected and an unreflected axis; the pressures are right. The reach-two current is right for one species. The reach-three current is right for all eight.

Executed for an oblique packet of a reflected species: the pairings of a smooth displacement with the site stress, relative to the two-step current, are `+1.30` (stretch), `−1.19, −1.19` (the two shears), `+1.10` (stretch) — and `+1.30, +1.19, +1.19, +1.10` for the first species.

In plain terms: lengths can be tied to the walker in three ways, and each way reads the walker's push on space differently. For the first kind of walker the three readings agree. For the other kinds, the nearest-neighbour reading gets the sideways (shearing) push backwards for six kinds out of eight; the two-step reading gets the push along a reflected direction backwards for seven; the three-step reading gets every push right for all eight.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 72 (PR #8605), next_trace_action: 'the same comparison for the frame (reach one)'; block 68 T2: the frame shows the species the same lengths and mirrored angles."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the ladder of reach by species: frame two of eight, reach two one of eight, reach three eight of eight; next: the owner's forks on reach and on the species; couplings of other kinds (block 73 N1.1)"
conditional_surface_status: "T1 exact for every state on tori with even sides (at least six for the two-step momentum) and on the infinite lattice; T2, T3 at leading order for smooth envelopes, with block 72 T1, T3 and block 66 T1, T2 restated"
hypothetical_axiom_status: "block 54's walk; the three couplings of blocks 62, 63, 69; block 66's ledger; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom's one-site algebra, and the memo's silence on amplitude dynamics. Blocks 54, 62, 63, 66, 69, 70, 72 (open PRs) supply the objects.

- **Site stress.** `Θ_a^j(x) = Re ψ†(x)σ_a(S_jψ)(x) = ∂⟨H[E]⟩/∂E_a^j(x)` at the identity frame (block 62).
- **Bond currents.** `J_a^j(x → x + e_a) = ½Re[ψ†(x + e_a)σ_a(S_jψ)(x) + (S_jψ)†(x + e_a)σ_aψ(x)]` (block 63); `K_a^j` the same with `P_j = S_jC_j` (block 69).
- **Maps.** `V_n`, `s_n = det D_n`, `D_n` of block 70; `𝔢[V_nψ] = s_n𝔢[ψ]`.
- **Requirement** (block 66 T1, T2, restated in block 72): with the response `𝒥` of the content to the field that carries the lengths, `−div(response) = 𝔢 du` at lowest order.
- **Own stress.** By block 72 T1(d) and T3(b), `−div K[φψ] = f^P = 𝔢 du` (leading order) for every species: `K` is the response whose divergence balances the weight whatever the species. It is called the species' own stress here.

Nothing classical is used beyond expansion in the lattice spacing.

## Prior art and what is new

New, inside the framework's vocabulary: the exact table of the three supplied responses under the species-exchange maps; and, from it, which species each supplied coupling serves — in particular that the nearest-neighbour frame, which block 68 credited with showing all species the same lengths, sources six of them with the wrong sign in shear. No gravitational claim is made.

## Exact target and obligation graph

Target: the three responses by species. Obligations: (O1) the exact table; (O2) their agreement for the first species; (O3) what follows for the ledger's requirement. T1–T3 discharge them.

## Theorem T1 — the table

*Statement.* For every state, every species `n`, all `a, j`, at every site (bond): `Θ_a^j[V_nψ] = s_nD_aD_jΘ_a^j[ψ]`; `J_a^j[V_nψ] = s_nD_jJ_a^j[ψ]`; `K_a^j[V_nψ] = s_nK_a^j[ψ]`.

*Proof.* `V_n` is a unitary acting site by site with `V_n†σ_aV_n = (ρ_n)_aσ_a`, `S_jV_n = D_jV_nS_j`, `P_jV_n = V_nP_j` (block 70 T1(a)); moving from `x` to `x + e_a` brings the site sign `D_a`. So `Θ` picks up `ρ_aD_j = s_nD_aD_j`; `J` picks up `ρ_aD_aD_j = s_nD_j`; `K` picks up `ρ_aD_a = s_n`. ∎

## Theorem T2 — for the first species the three agree

*Statement.* For a smooth two-component amplitude, with lattice spacing `h`: `Θ_a^j`, `J_a^j` and `K_a^j` all equal `h Re ψ†σ_a(−i∂_jψ) + O(h²)`, in all nine components. Hence, for an amplitude `V_n ×` (smooth): `Θ_a^j = D_aD_jK_a^j` and `J_a^j = D_jK_a^j` at leading order.

*Proof.* `S_jψ` and `P_jψ` are both `−ih∂_jψ + O(h³)`; evaluating one factor at `x + e_a` changes the product at the next order. Then T1. ∎

For a plane wave the exact ratios are `Θ/K = 1/(cos k_a cos k_j)` and `J/K = 1/cos k_j`, and `cos k_a = D_a cos q_a`: the signs of T1 are the lattice's cosines at the species' zero.

## Theorem T3 — who is served

*Statement.* (a) `D_aD_j = 1` for all `a, j` iff `n ∈ {(000), (111)}`; `D_j = 1` for all `j` iff `n = (000)`. (b) For species `n` and each `j`, at leading order: `Σ_ad_aK_a^j − Σ_ad_aΘ_a^j = 2Σ_{a: D_a ≠ D_j}d_aK_a^j`, and `Σ_ad_aK_a^j − Σ_ad_aJ_a^j = (1 − D_j)Σ_ad_aK_a^j`. (c) Hence block 66's requirement is met at leading order: under reach three by every species; under reach two iff `(1 − D_j)𝔢 d_ju = 0` for each `j` (block 72); under the frame iff for each `j` the shear stress between the axes with `D_a ≠ D_j` and axis `j` has no divergence, `Σ_{a: D_a ≠ D_j}d_aK_a^j = 0` — always for `(000)` and `(111)`, and for the other six only in such flows.

*Proof.* (a) Enumeration. (b) T2. (c) Block 72 T1(d), T3(b) give `−Σ_ad_aK_a^j = 𝔢 d_ju` for every species; substitute (b) into the requirement with `Θ` or `J` as the response. ∎

For fields that vary along one axis only, with the content uniform across it, the shear divergences vanish and the frame's requirement is met by every species; an oblique flow in fields varying along two axes has them. Block 62's defect of the frame at second order is a separate matter and concerns every species.

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block74_three_responses.py` (a `256 × 256` slice, `H = σ_1S_x + σ_2S_y`; packets of positive energy, width 24, own wave number `q = (0.5, 0.3)`). **W1**, site by site where `|K|` exceeds a fifth of its maximum: for species `(0,0)` the ratios `Θ/K` lie in `[1.25, 1.35]`, `[1.15, 1.24]`, `[1.15, 1.24]`, `[1.06, 1.14]` for `(a, j) = (x,x), (x,y), (y,x), (y,y)` and `J/K` within `0.001` of `1.140, 1.047, 1.140, 1.047`; for species `(1,0)` the same magnitudes with the signs `+, −, −, +` and `−, +, −, +`. The plane-wave values are `D_aD_j/(cos q_a cos q_j) = 1.298, 1.193, 1.193, 1.096` and `D_j/cos q_j = 1.139, 1.047`. **W2**, pairings of one sinusoidal mode of displacement with each response, relative to the pairing with `K`: site stress `+1.3002, +1.1937, +1.1937, +1.0972` (first species) and `+1.3002, −1.1937, −1.1937, +1.0972` (reflected); reach-two current `+1.1403, +1.0474, +1.1402, +1.0476` and `−1.1403, +1.0474, −1.1402, +1.0476`.

## No-Go Discipline Gate

The note's negative sentence: the frame's response is not the own stress of six of the eight species.

### N1 — Routes by which the sentence could fail or mislead
1. *Only species (000) and (111) present, or only (000).* Then the frame, respectively reach two, serves all that is there.
2. *Flows without the named shear gradients.* T3(c) says when the frame's requirement is met nevertheless.
3. *A different identification of the frame's source.* The response is fixed by the coupling, `∂⟨H[E]⟩/∂E`; symmetrising it in `(a, j)` does not change the sign `D_aD_j`.
4. *Block 68 T2.* "The frame shows all species the same lengths" stands; mirrored angles there and the wrong sign in shear here are the same fact seen from the two sides of the coupling.
5. *Beyond leading order.* All three responses differ by lattice factors (`1/(cos q_a cos q_j)`, `1/cos q_j`); the signs are of order one.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The identity frame and uniform rates in T1, T2 (the rates enter T3 through block 72's restated law); smooth envelopes; tori with even sides.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the Qubit axiom's one-site algebra | yes (premise) |
| blocks 62, 63, 69 (open PRs #8592, #8593, #8601) | the three couplings and their responses | yes (restated) |
| block 70 (open PR #8602) | the exchange maps | yes (restated; used in B1, B2) |
| blocks 66, 72 (open PRs #8597, #8605) | the requirement; `K` as the own stress of every species | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the table; agreement for the first species; two, one, eight species served" | executed: each of the nine components of the three responses for `V_nψ` against `ψ`, all eight species | executed: as equalities at all 216 sites of a `6×6×6` torus | executed: leading order of the three responses for a smooth two-component amplitude in three dimensions, all nine components | executed: the species served by each response; the shortfall of each divergence, all species and `j` | T1 an identity for every state; T2, T3 leading order with blocks 66, 72 restated; which coupling and which species not decided |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "T1 is three lines." Reply: it is, and until it was written the campaign's own record credited the frame with treating the species alike; the three lines change the ladder's bottom rung. Second objection: "Shear gradients are a special circumstance." Reply: they are the generic circumstance for content moving obliquely through fields that vary in more than one direction; T3(c) states the exception exactly.

### N8 — Cross-cycle echo
Block 68: the frame shows all species the same lengths, reach two does not. Block 72: reach two's ledger cannot hold reflected species. Here the frame joins it for six species, in shear. The count of species served falls `2, 1` and then rises to `8` with reach.

## Falsifiers

- A state, species and component violating the table at some site.
- A smooth-envelope amplitude of species `(100)` whose site stress `Θ_2^1` has the same sign as its `K_2^1` at leading order.
- A species other than `(000)`, `(111)` with `D_aD_j = 1` for all `a, j`.

## Boundaries and non-claims

The coupling is not chosen and no species is declared present or absent. The frame's second-order defect (block 62) is not revisited. Varying frames, the blind walk, kinetic terms and records are outside. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, the memo's silence on amplitude dynamics. Blocks 54, 62, 63, 66, 69, 70, 72 (PRs #8570, #8592, #8593, #8597, #8601, #8602, #8605, open): restated or placed.
- Named standard imports at definition level: conjugation by site signs and by a half turn of the coin; expansion in the lattice spacing.

## Review record
Supervisor-run block, the twenty-second of the source-link direction and the eighteenth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: nothing new is supplied; the note ranks nothing — it counts which species each supplied coupling serves. A rigour lens: the table is proved for every state and executed at every site before any leading-order statement is combined with it; the "own stress" is defined by what block 72 proved of `K` (its divergence balances the weight for every species), not by preference; block 68's statement about the frame was re-read and N1.4 says how the two statements fit; the control's first header carried a garbled prediction, which was replaced by the plane-wave formula and its numbers before the output was committed. A strategy lens: with this block the decision record's ladder can be given by species — two, one, eight. Control: as reported under Executed. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_three_responses_eight_species_site_stress_bond_current_two_step_current_2026_09_21.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
