---
claim_id: admissibility_rule_the_frame_rotation_for_shears_is_seen_only_at_the_lattice_scale_it_moves_a_waves_density_by_a_connection_that_vanishes_at_the_species_points_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed, for the frame rotation that block 188 (pushed) found the stress response leaves free for shears (a k-dependent rotation of the walk's Clifford vector at fixed energy): (T1) for h' = U h U^dag with U(k) = exp(-i theta(k) n.sigma/2), every energy, every group velocity and every single-wave current is unchanged; (T2) for the same state carried by U, the density's pair symbol is multiplied by U(k')^dag U(k) = 1 - (i/2) q.grad(theta) n.sigma + O(q^2), so every q = 0 value is unchanged and the density's first moment moves by the rotation's connection (1/2) grad(theta) times the wave's polarisation along n; (T3) every rotation angle in block 188 T6's table is (1/4) times a product of cosines with one doubled, per unit strain, so its gradient vanishes at all eight species points and grows linearly away from them (Hessian diag(5/4, 1/4, 0) at k = 0 for (11)/(12)): the shift is proportional to the strain and to the distance from a species point, and vanishes at long wavelength. So the frame rotation is observable only at the lattice scale. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_frame_rotation_for_shears_is_seen_only_at_the_lattice_scale_2026_09_28.py
---

# The frame rotation for shears is seen only at the lattice scale: it moves a wave's density by a connection that vanishes at the species points

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 69 as landed; block 188 is pushed and placed, and the facts used from it are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within block 69 as landed on main and asks whether the frame rotation that block 188 found free for shears is observable; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 188 (pushed) found that for shears the walk's response to the lattice's lengths is fixed only up to a rotation of its Clifford vector at fixed energy, a frame rotation. A same-family panel (2026-09-27/28) disagreed about whether that rotation is physical. This note answers what it changes.

- **T1: nothing spectral.** A rotation that depends on the wave number leaves every energy, every group velocity and every single-wave current unchanged.
- **T2: where the density sits.** For the same state, the density changes only at nonzero wave-number transfer. Its first moment moves by the rotation's connection, `½∇θ` times the wave's polarisation.
- **T3: that shift is lattice-scale.** Every rotation angle in block 188's table is `¼` times a product of cosines, per unit strain. Its gradient vanishes at all eight species points. So the shift is proportional to the strain and to the distance from a species point, and it vanishes at long wavelength.

In plain terms: the leftover choice in how the walker responds to a slanted stretch does not change any energy or speed. It moves where a wave's weight sits, by less than a lattice spacing per unit strain, and not at all for long waves. So it is real, but only at the scale of the lattice itself. That settles the panel's disagreement in the lattice lens's favour at long wavelength, while granting the gravitation lens that the angle is not purely a label.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-28) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Block 69 is used as landed on main; block 188 is pushed and placed, and the facts used from it are re-derived (runner D1).

- **The coupling** (block 69), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`".
- **The frame rotation** (block 188, pushed). For shears the stress response fixes the walk's energies but not its Clifford vector's direction. At second order the clashes are rotations about coordinate axes through angles `θ(k)`, one per pair of strain components, given in block 188 T6's table.
- **Densities.** The site density of a state `ψ` has pair symbol `ψ(k′)†ψ(k)`, with `q = k − k′`. Its value at `q = 0` is the total, and its first order in `q` gives the first moment.
- **The rotation.** `U(k) = exp(−iθ(k) n·σ/2)`, a unitary on the coin for each `k`. The runner takes `n = e₃`; any fixed axis is the same up to relabelling the coin.

In the literature, the shift of a wave packet's position under a wave-number-dependent change of internal basis is the Berry connection (Zak's phase on a lattice). The invariance of energies under a unitary change of basis is Hellmann–Feynman's setting. This note uses neither as authority.

## Domain qualifications

- The rotation at second order in the strain, as block 188 T6 gives it. Higher orders are not examined.
- A fixed rotation axis. Block 188's angles are each about a fixed coordinate axis.

## Theorem T1 — nothing spectral

*Statement.* For `h′ = U h U†` with `U(k) = exp(−iθ(k) n·σ/2)`, `h′² = h² = |F|²`. So `h′ = (R_θF)·σ` with `|R_θF| = |F|`. Every energy, every group velocity `∂E/∂k`, and every single-wave current, the `q = 0` value of the energy current `E ∂E/∂k`, is unchanged.

*Proof.* `U` is unitary for each `k`, and conjugation rotates the Clifford vector (runner B1). ∎

## Theorem T2 — where the density sits

*Statement.* Carry a state by `U`, `ψ̃ = Uψ`. Then `ψ̃(k′)†ψ̃(k) = ψ(k′)† U(k′)†U(k) ψ(k)`, and

`U(k′)†U(k) = 1 − (i/2) q·∇θ(k) n·σ + O(q²)`.

So the density is unchanged at `q = 0`: the total, and every single-wave value. Its first moment moves by the connection `U† i∇U = ½∇θ n·σ`, weighted by the wave's polarisation `⟨n·σ⟩`.

*Proof.* Expansion of `exp(−i(θ(k) − θ(k′)) n·σ/2)` in `q` (runner C1). ∎

## Theorem T3 — that shift is lattice-scale

*Statement.* Every angle in block 188 T6's table has the form `±¼ Π cos(·)` per unit strain, one of the cosines doubled. The `(11)/(12)` entry, `−¼ cos k₁ cos k₂ cos 2k₁`, is re-derived here. Each angle's gradient vanishes at all eight species points `k ∈ {0, π}³`. For `(11)/(12)` the Hessian at `k = 0` is `diag(5/4, 1/4, 0)`. So near a species point the connection is `O(|k − k_n|)` per unit strain, and the shift of a long wave's density vanishes with its wave number.

*Proof.* Derivatives of cosines vanish at `0` and `π`. The `(11)/(12)` entry is from the flows' mixed derivatives at the free walk (runner D1). ∎

## What this settles and what it does not

- **Settled.**
  - Block 188's frame rotation changes no energy, speed or single-wave current (T1).
  - It moves where a wave's density sits by a connection proportional to the strain (T2).
  - That shift vanishes at every species point and so at long wavelength (T3).
- **For the third column (the coupling axis).** With a yes to the free-particle question, the frame-rotation choice for shears remains. It is a lattice-scale choice, invisible to long waves, so it is not a long-wavelength owner decision.
- **Not settled.**
  - Higher orders in the strain.
  - The member's coupling to the density at the pair level. A lattice-scale shift of the source is a lattice-scale change of where the member is sourced.

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
next_trace_action: "an other-family referee; higher orders"
conditional_surface_status: "exact within block 69, at second order in the strain"
hypothetical_axiom_status: "the frame is supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling.
  - Block 188 (pushed): the frame rotation and its table.
- **In the literature.**
  - The Berry connection and Zak's phase: a wave packet's position shifts under a wave-number-dependent change of internal basis.
  - Hellmann–Feynman: energies depend only on the spectrum.
  - None is used as authority.
- **New here.**
  - The frame rotation's effect is a lattice-scale density shift that vanishes at the species points.
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed. The question came from a same-family panel (Claude Fable 5.1, not referees).

## Exact target and obligation graph

Target: whether the frame rotation is observable. The obligations are:
- (O1) the premises (A3);
- (O2) spectral invariance (B1);
- (O3) the density shift (C1);
- (O4) the angles at the species points (D1).

## No-Go Discipline Gate

The note's negative sentence: the frame rotation changes no energy, speed or single-wave current, and no long-wave density.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *Axes that vary with `k`.* Block 188's angles are about fixed axes. General axes are not examined.
2. *Higher orders.* Not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the rotation's form and the order in the strain.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling | yes (quoted, A3) |
| block 188 (pushed) | the rotation's table | re-derived (D1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the frame rotation is seen only at the lattice scale" | executed: spectral invariance | executed: the density shift | executed: one table entry re-derived | executed: gradients at all species points, the Hessian | not executed: higher orders |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A lattice-scale shift of where content sits is still a physical difference."
  - *Reply:* Agreed. The note says it is real at the lattice scale and absent at long wavelength.

### N8 — Cross-cycle echo
- Block 188: the rotation is free for shears.
- This note: it is observable only at the lattice scale.

## Falsifiers

- An angle in block 188's table with a nonzero gradient at a species point.
- A change of energy under a wave-number-dependent coin rotation.

## Boundaries and non-claims

- Second order in the strain; fixed axes.
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
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_frame_rotation_for_shears_is_seen_only_at_the_lattice_scale_2026_09_28.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
