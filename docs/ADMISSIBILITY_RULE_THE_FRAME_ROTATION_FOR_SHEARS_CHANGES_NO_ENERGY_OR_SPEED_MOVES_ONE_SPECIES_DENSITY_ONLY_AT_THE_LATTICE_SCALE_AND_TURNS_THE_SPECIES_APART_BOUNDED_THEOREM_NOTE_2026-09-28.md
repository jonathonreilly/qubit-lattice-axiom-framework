---
claim_id: admissibility_rule_the_frame_rotation_for_shears_changes_no_energy_or_speed_moves_one_species_density_only_at_the_lattice_scale_and_turns_the_species_apart_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed, for the frame rotation that block 188 (pushed) found the stress response leaves free for uniform shears (a k-dependent rotation of the walk's Clifford vector at fixed energy), at second order in the strain: (T1) for h' = U h U^dag with U(k) = exp(-i theta(k) n.sigma/2), every energy, every group velocity and every single-wave current is unchanged; (T2) for the same state carried by U (a phase convention: U is fixed only up to phases commuting with h'), the density's pair symbol is multiplied by U(k')^dag U(k) = 1 - (i/2) q.grad(theta) n.sigma + O(q^2), q = k - k', so within one species every q = 0 value is unchanged and the first moment moves by the connection (1/2) grad(theta) times the wave's polarisation; at a species point the O(q^2) term (i/4) q.H.q n.sigma remains; (T3) every angle in block 188 T6's table is (1/4) times a product of cosines with one doubled, per unit product of two strain components, so its gradient vanishes at all eight species points (Hessian diag(5/4, 1/4, 0) at k = 0 for (11)/(12)): within one species the density shift vanishes at long wavelength; (T4) but at the species points every angle is +1/4 or -1/4 and takes both values, so the eight species' coins are turned apart by 1/2 per unit product of strain components at any wavelength; relative to site-local coin states and in interference between species, the rotation is visible to long waves. The supervisor's own derivation; second version after a same-family referee's corrections. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_frame_rotation_for_shears_turns_the_species_apart_2026_09_28.py
---

# The frame rotation for shears changes no energy or speed; it moves one species' density only at the lattice scale, and turns the species apart

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 69 as landed; block 188 is pushed and placed, and the facts used from it are re-derived; the supervisor's own derivation, second version after a same-family referee; nothing adopted or registered; unaudited)

This note works within block 69 as landed on main and asks whether the frame rotation that block 188 found free for shears is observable; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 188 (pushed) found that for shears the walk's response to the lattice's lengths is fixed only up to a rotation of its Clifford vector at fixed energy, a frame rotation. A same-family panel (2026-09-27/28) disagreed about whether that rotation is physical. This note answers what it changes.

- **T1: nothing spectral.** A rotation that depends on the wave number leaves every energy, every group velocity and every single-wave current unchanged.
- **T2: where one species' density sits.** For the same state, the density changes only at nonzero wave-number transfer. Its first moment moves by the rotation's connection, `½∇θ` times the wave's polarisation.
- **T3: within one species that shift is lattice-scale.** Every angle in block 188's table is `¼` times a product of cosines, per unit product of two strain components. Its gradient vanishes at all eight species points. So within one species the shift vanishes at long wavelength. A second-order term, of order `q²`, remains at the species points.
- **T4: but the species are turned apart.** At the species points every angle is `+¼` or `−¼`, and each angle takes both values. So the eight species' coins are rotated relative to one another by `½` per unit product of strain components, at any wavelength.
  - For the `(11)/(12)` angle, it is `−¼` at `k = 0` and `(0, 0, π)`, and `+¼` at `(π, 0, 0)` and `(0, π, 0)`.
  - This is block 188 T6's long-wavelength clash of `±¼`, read at each species point.
  - It is visible to long waves in interference between species and relative to the lattice's own coin states.

In plain terms: the leftover choice in how the walker responds to a slanted stretch does not change any energy or speed. Within one kind of wave it moves where the weight sits only at the scale of the lattice, and not at all for long waves. But it turns the internal arrows of the different kinds of wave by different amounts, and that difference does not shrink for long waves. So the choice is partly physical at long wavelength. It can be seen by comparing kinds of wave, or by comparing a wave's arrow with the lattice's own.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-28) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Block 69 is used as landed on main; block 188 is pushed and placed, and the facts used from it are re-derived (runner D1, S1).

- **The coupling** (block 69), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`".
- **The frame rotation** (block 188, pushed). For uniform shears the stress response fixes the walk's energies but not its Clifford vector's direction. At second order the clashes are rotations about coordinate axes through angles `θ(k)`, one per pair of strain components, given in block 188 T6's table. Each angle is bilinear in the strain: it is quoted per unit product of two strain components.
- **Densities.** The site density of a state `ψ` has pair symbol `ψ(k′)†ψ(k)`, with `q = k − k′`. Its value at `q = 0` is the total, and its first order in `q` gives the first moment. Waves at different species points interfere through the pair symbol at a transfer near a species separation.
- **The rotation.** `U(k) = exp(−iθ(k) n·σ/2)`, a unitary on the coin for each `k`. The runner takes `n = e₃`; any fixed axis is the same up to relabelling the coin. `U` is fixed only up to a phase `exp(iφ(k)ĥ′)` that commutes with `h′`. That phase shifts the first moment by `∇φ`. So "the same state carried by `U`" is a convention, and a statement independent of it needs a preparation protocol.

In the literature, the shift of a wave packet's position under a wave-number-dependent change of internal basis is the Berry connection (Zak's phase on a lattice). The invariance of energies under a unitary change of basis is Hellmann–Feynman's setting. This note uses neither as authority.

## Domain qualifications

- Uniform strain, at second order, as block 188 T6 gives it. A non-uniform strain makes the long-wavelength angle vary in space, and so acts as a coin gauge field at every wavelength. That case is not examined.
- A fixed rotation axis. Block 188's angles are each about a fixed coordinate axis.

## Theorem T1 — nothing spectral

*Statement.* For `h′ = U h U†` with `U(k) = exp(−iθ(k) n·σ/2)`, `h′² = h² = |F|²`. So `h′ = (R_θF)·σ` with `|R_θF| = |F|`. Every energy, every group velocity `∂E/∂k`, and every single-wave current, the `q = 0` value of the energy current `E ∂E/∂k`, is unchanged.

*Proof.* `U` is unitary for each `k`, and conjugation rotates the Clifford vector (runner B1). ∎

## Theorem T2 — where one species' density sits

*Statement.* Carry a state by `U`, `ψ̃ = Uψ`. Then `ψ̃(k′)†ψ̃(k) = ψ(k′)† U(k′)†U(k) ψ(k)`, and with `q = k − k′`

`U(k′)†U(k) = 1 − (i/2) q·∇θ(k) n·σ + (i/4) q·H(k)·q n·σ − ⅛(q·∇θ)² + O(q³)`,

where `H` is the Hessian of `θ`. So within one species the density is unchanged at `q = 0`: the total, and every single-wave value. Its first moment moves by the connection `U† i∇U = ½∇θ n·σ`, weighted by the wave's polarisation `⟨n·σ⟩`. At a species point, where `∇θ = 0`, the term `(i/4) q·H·q n·σ` remains, of order `q²`.

*Proof.* Expansion of `exp(−i(θ(k) − θ(k′)) n·σ/2)` in `q` (runner C1 to first order, S2 to second order at `k = 0`). ∎

## Theorem T3 — within one species the shift is lattice-scale

*Statement.* Every angle in block 188 T6's table has the form `±¼ Π cos(·)` per unit product of two strain components, one of the cosines doubled. The `(11)/(12)` entry, `−¼ cos k₁ cos k₂ cos 2k₁`, is re-derived here. Each angle's gradient vanishes at all eight species points `k ∈ {0, π}³`. For `(11)/(12)` the Hessian at `k = 0` is `diag(5/4, 1/4, 0)`. So near a species point the connection is `O(|k − k_n|)`, and the shift of one species' long-wave density vanishes with its wave number.

*Proof.* Derivatives of cosines vanish at `0` and `π`. The `(11)/(12)` entry is from the flows' mixed derivatives at the free walk (runner D1). ∎

## Theorem T4 — the species are turned apart

*Statement.* At each of the eight species points, each of the nine angles of block 188 T6's table is `+¼` or `−¼` per unit product of strain components, and every angle takes both values over the eight points. For `(11)/(12)`:
- `−¼` at `k = 0` and `(0, 0, π)`;
- `+¼` at `(π, 0, 0)` and `(0, π, 0)`.

So species separated by `(π, 0, 0)` or `(0, π, 0)` have coins rotated relative to each other by `½`, while those separated by `(0, 0, π)` do not, for this entry. The difference does not depend on the wavelength.

*Consequences.*
- Waves near different species points interfere through the pair symbol at a transfer near their separation. There the factor `U(k′)†U(k)` is `exp(∓iθ_rel n·σ/2)` with `θ_rel = ½` per unit product of strains, not `1 + O(q)`. So the lattice-period components of the density change by an amount independent of the envelope's wavelength.
- Relative to site-local coin states (the lattice's own coin frame), each species' coin is rotated by `±¼` per unit product of strains at long wavelength.
- This is block 188 T6's statement that the clash tends to `±¼` at long wavelength and is "not a lattice effect", read species by species.

*Proof.* Evaluation of the table at the eight corners (runner S1). The interference and frame statements follow from T2's factor with `θ(k) − θ(k′)` finite. A referee confirmed them numerically: at strain `0.2` the inter-species overlap changed from `0.72811` to `0.71339` for envelope wave numbers `10⁻¹` to `10⁻³`, while the within-species change scaled as the square of the wave number. ∎

## What this settles and what it does not

- **Settled.**
  - Block 188's frame rotation changes no energy, speed or single-wave current (T1).
  - Within one species it moves where the density sits by a connection that vanishes at the species point, so the within-species shift vanishes at long wavelength (T2, T3).
  - Between species, the rotation does not vanish: the species' coins are turned apart by `½` per unit product of strain components at any wavelength (T4).
- **For the third column (the coupling axis).**
  - With a yes to the free-particle question, the frame-rotation choice for shears remains.
  - It is invisible to energies, speeds and one species' long-wave density.
  - It is visible to long waves through interference between species and through each wave's coin orientation against the lattice's own.
  - So it is partly a long-wavelength matter. The first version's "not a long-wavelength owner decision" is withdrawn.
- **Not settled.**
  - Higher orders in the strain.
  - Non-uniform strain, where the long-wavelength angle varies in space and acts as a coin gauge field.
  - The member's coupling to the density at the pair level.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 188 (pushed) and the 2026-09-27/28 panel's Q3: is the frame rotation for shears physical?"
source_of_blocker_text: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; non-uniform strain; higher orders"
conditional_surface_status: "exact within block 69, at second order in uniform strain"
hypothetical_axiom_status: "the frame is supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling.
  - Block 188 (pushed): the frame rotation and its table, including the long-wavelength clash of `±¼`.
- **In the literature.**
  - The Berry connection and Zak's phase: a wave packet's position shifts under a wave-number-dependent change of internal basis.
  - Hellmann–Feynman: energies depend only on the spectrum.
  - None is used as authority.
- **New here.**
  - The frame rotation's within-species effect is a lattice-scale density shift.
  - Its between-species effect is a finite relative rotation at every wavelength.
- **Provenance.** The supervisor's own (Claude Opus 5.5). The question came from a same-family panel (Claude Fable 5.1, not referees). The second version follows a same-family referee (Claude Sonnet 5).

## Exact target and obligation graph

Target: whether the frame rotation is observable. The obligations are:
- (O1) the premises (A3);
- (O2) spectral invariance (B1);
- (O3) the density shift within one species (C1, S2);
- (O4) the angles' gradients at the species points (D1);
- (O5) the angles' values at the species points (S1).

## No-Go Discipline Gate

The note's negative sentence: the frame rotation changes no energy, speed or single-wave current, and no single species' long-wave density.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *Axes that vary with `k`.* Block 188's angles are about fixed axes. General axes are not examined.
2. *Higher orders.* Not examined.
3. *Between species* (the referee's). Conceded: T4. The negative sentence is restricted to one species.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the rotation's form, the phase convention for "the same state", uniform strain, and the order in the strain.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling | yes (quoted, A3) |
| block 188 (pushed) | the rotation's table | re-derived (D1) and evaluated (S1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no energy or speed changes; one species' density moves only at the lattice scale; the species turn apart" | executed: spectral invariance | executed: the density shift, first and second order | executed: one table entry re-derived | executed: gradients and values at all species points, the Hessian | not executed: higher orders; non-uniform strain |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A frame rotation that differs between species is visible to long waves."
  - *Reply:* Agreed. This is T4. The first version missed it.

### N8 — Cross-cycle echo
- Block 188: the rotation is free for shears, and its clash tends to `±¼` at long wavelength.
- This note: that `±¼` is each species' own rotation. Within a species only its gradient moves the density, and between species the difference persists.

## Falsifiers

- An angle in block 188's table with a nonzero gradient at a species point.
- A change of energy under a wave-number-dependent coin rotation.
- An angle of the table that takes one value at all eight species points.

## Boundaries and non-claims

- Second order in uniform strain; fixed axes.
- The frame is supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 69 (landed), quoted. Block 188 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - unitary conjugation;
  - the connection of a wave-number-dependent basis (Berry's);
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-28, during the owner's third 12-hour campaign.
- **Referee (2026-09-28; Claude Sonnet 5, same vendor family as the author, a separate model and session).** Verdict: confirmed with scope corrections.
  - T1–T3 were re-derived, including all 15 mixed-derivative clashes; the runner reran at 11/0.
  - Corrections, applied in this second version:
    - the between-species rotation (now T4) and the coin-frame rotation relative to site-local states;
    - the second-order term at the species points;
    - "per unit product of two strain components", not "per unit strain";
    - the phase convention behind "the same state";
    - reconciliation with block 188 T6's `±¼`;
    - uniform strain only.
  - The headline and title are narrowed accordingly.
- **Provenance.** The supervisor's own derivation.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_frame_rotation_for_shears_turns_the_species_apart_2026_09_28.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
