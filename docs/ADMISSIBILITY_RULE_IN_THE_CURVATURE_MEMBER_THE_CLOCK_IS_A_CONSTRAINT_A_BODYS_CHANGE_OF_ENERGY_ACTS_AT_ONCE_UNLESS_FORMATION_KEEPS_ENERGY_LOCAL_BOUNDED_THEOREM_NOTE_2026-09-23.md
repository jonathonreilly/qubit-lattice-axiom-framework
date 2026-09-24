---
claim_id: admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 60 and 62: the curvature member at second order about the uniform state (R1, R2 of block 62), block 62's kinetic term (alpha h'_ij h'_ij + beta (tr h')^2)/wbar with no rate of change of a rate, and block 55's coupling of the clock to the energy. Exact (a probes worker's derivation, verified here), at every lattice wave vector: the rate's equation is a constraint, 2 K wbar p^2 phi = e; only the two transverse traceless strains travel; the clock is u = -e/(4 K wbar p^2) + alpha(alpha + 3 beta) e''/(K^2 wbar^3 (alpha + beta) p^4), set at each label time by the content; so a change of a body's energy at rest reaches the clocks, and every packet's fall, at once at every distance; at alpha + beta = 0 a body at rest cannot change its energy by a jump. Executed: a walk packet's force changes long before a strain could arrive. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_2026_09_23.py
---

# In the curvature member the clock is a constraint: a body's change of energy acts at once, unless formation keeps energy local

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact at second order within supplied clauses; a probes worker's derivation, verified here; referee of another model family pending; nothing adopted or registered; unaudited)

This note works within the supplied clauses of blocks 60 and 62 (the curvature member and its kinetic term) and reports, from a probes worker's exact derivation verified here, when a change of a body's energy reaches the clocks; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The moving-records column still owes a delay (block 95's pull acts at once). Block 57 (#8578) showed that nearest-neighbour kinetic terms of the rates carry no delay. Block 60 (#8590) T5 showed that the lengths carry none for any kinetic term without a rate of change of a rate. Block 62 (#8592) gave the full strain kinetic term and found two travelling disturbances. A probes worker (task `J:derive:delay-of-the-rate-field-with-the-curvature-member:a1`, worker `w-jonathonsmac4f50-j03c0`, Claude Opus 5.5) put these together and asked what happens when a body's energy changes, as it does at a formation event. This note restates and verifies the result.

- **T1.** Block 62's member is blind to relabellings and sees one scalar. Block 60's isotropic law is its special case.
- **T2: the clock is a constraint.** The rate's equation has no time derivative: `2K w̄ p² φ = e` fixes the scalar length at each label time. Only the two transverse traceless strains travel (block 62 T4), and a body at rest does not source them.
- **T3: the clock law.** `u(k,t) = −e(k,t)/(4K w̄ p²) + α(α + 3β) ë(k,t)/(K² w̄³ (α + β) p⁴)`. The clock is set at each label time by the content and its second derivative. The static limit is block 60's law, and at `α + 3β = 0` it is exactly the instantaneous field.
- **T4: what a formation event does.**
  - A body's energy switched on smoothly moves the clock at label time `0⁺`, at every wave vector.
  - Afterwards the clock has jumped by the whole static field of the change, whatever `α` and `β`.
  - So a packet at any distance starts to fall differently long before a strain wave could arrive.
  - At `α + β = 0` the relabelling equation forbids it: the energy of a body at rest can change only at a constant rate, never by a jump.

So, in the lane's most complete geometry, the clock field's steady part does not travel; only the strains do. A record that forms at rest, gaining energy from nothing nearby, changes the clocks everywhere at once. Two readings avoid that:
- the kinetic ratio `α + β = 0` together with formation that keeps energy local: a record forms by taking its energy from what is already there, as block 58 (#8579) and block 67 (#8598) found the ledger can be kept through a formation event;
- or formation is not at rest and moves energy by currents. This is not worked here.

In plain terms: in this version of the lattice's geometry, the slowing of clocks by matter is not a wave but a bookkeeping rule that holds at every instant everywhere. If a new record could appear with new energy, every clock in the universe would notice at once. The way out is for a record to be made from energy that was already there, so the books never jump.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`): no time metric; update laws open. Nothing is adopted.
- **Block 60's curvature member** (#8590) and **block 62's strains** (#8592).
  - The strain `h_ij` at second order about the uniform state, with `R₁ = −(p_i p_j h_ij − p² tr h)` and block 62's quadratic `R₂`.
  - `p_j = 2 sin(k_j/2)`, `p² = E(k) ≠ 0`.
  - The member `F₂ = −K w̄ (u R₁ + R₂)`.
- **Block 62's kinetic term.** `(α ḣ_ij ḣ_ij + β (tr ḣ)²)/w̄`, with no rate of change of a rate.
- **Block 55's coupling** (#8571). The clock enters through `−e u`, `e` the content's energy density.
- **Bodies at rest.** They have no hop energy, hence no frame response (block 59, #8581).
- **Provenance.** The derivation and the executed control are the probes worker's (Claude Opus 5.5). The supervisor re-ran its check (14 of 14) and ported the exact part into this runner; the control is the worker's section E, re-run. Same model family; a referee of another family has not yet run.

## Theorem T1 — one scalar

*Statement.* `R₁` and `R₂` are unchanged by `h → h + p ξ + ξ p` for every `h`, `p`, `ξ`. On `h = (1 − pp/p²) φ` they are `2p²φ` and `p²φ²/2` in every direction. For `h = 2λδ` the constraint gives `p² λ = e/(4K w̄)`, which is block 60's law.

*Proof.* Symbolic algebra (family B). ∎

## Theorem T2 — the clock is a constraint

*Statement.* At a wave vector rotated to one axis, with `h` decomposed into the scalar `φ`, the transverse traceless `a, b` and the relabellings:
- the rate's equation is `2K w̄ p² φ = e(t)`, with no time derivative;
- `(4α/w̄) ä = −K w̄ p² a`, and the same for `b`, so the strains travel at `speed² = K w̄²/(4α)`, unsourced by a body at rest;
- `d/dt[(α + β) ξ̇_L + β φ̇] = 0`.

*Proof.* The equations of motion of `L = kinetic + K w̄ (u R₁ + R₂) − e u`, symbolically (family C). ∎

## Theorem T3 — the clock law

*Statement.* Starting from rest, eliminating `φ` and `ξ_L` gives `u(k,t) = −e/(4K w̄ p²) + α(α + 3β) ë/(K² w̄³ (α + β) p⁴)`. It equals block 60's static law when `ë = 0`, and at `α + 3β = 0` it is exactly the instantaneous static field.

*Proof.* Symbolic elimination (family D). ∎

## Theorem T4 — what a formation event does

*Statement.*
1. For `e = e₀ + Δe (3s² − 2s³)`, `s = t/τ_r`, the clock moves at `t = 0⁺` by `6α(α + 3β) Δe/(K² w̄³ (α + β) p⁴ τ_r²)` at every wave vector.
2. After the switch-on it has changed by the static field of `Δe`, whatever `α` and `β`.
3. At `α + β = 0` the relabelling equation reads `β φ̇ = constant`, so `ė` is constant and a jump has no solution.

*Proof.* Series at `t = 0` and substitution (family E). ∎

In real space, the static term is the lattice potential of `Δe`, falling as `1/r`. The `ë` term uses the square of the kernel, which grows with distance in three dimensions. That is a push during the switch-on that does not weaken with distance; the worker gives this as a continuum reading, box-dependent on a torus. By block 54, a packet at rest falls at `−E ∇u`, so its fall changes at once. The only freedom of the label time is global (block 57) and does not remove a gradient.

## Executed control

Script `specs/supervisor_control_block101_constraint.py`, output in `.out.txt`; floating point, evidence and not proof; the probes worker's section E, re-run.

The setup is a `48²` plane slice with `K = w̄ = α = 1`, `β = 1/2` (strain speed `1/2`), and a Gaussian body switched on over `τ_r = 2`. A walk packet sits at rest at distances 8 and 16. The force on its momentum was:

| Distance | Before | At label time 0.05 | After the switch-on | Block 54's `−E⟨∇u⟩` |
|---|---|---|---|---|
| 8 | zero (`10⁻²⁷`) | `+3.2·10⁻²` | `−8.46·10⁻⁵` | `−8.76·10⁻⁵` |
| 16 | zero (`10⁻¹⁹`) | `+1.9·10⁻²` | `−2.88·10⁻⁵` | `−2.97·10⁻⁵` |

A strain wave would arrive at label times 16 and 32. The response is linear in `Δe`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the moving-records column's delay (block 95's pull acts at once; blocks 57, 60 T5); formation events (block 58, block 67)"
source_of_blocker_text: block 57 (#8578); block 60 (#8590); probes derivation J:derive:delay-of-the-rate-field-with-the-curvature-member
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the steady part of the clock is a constraint; formation at rest acts at once unless alpha + beta = 0; next: moving bodies' stress as a source (whether alpha + beta = 0 admits exactly the conserved changes), the strong field, and a formation clause that keeps energy local (block 58)"
conditional_surface_status: "T1-T4 exact at second order about the uniform state at every lattice wave vector within blocks 60 and 62's clauses; the control executed"
hypothetical_axiom_status: "blocks 60 and 62's member and kinetic term, block 55's coupling and bodies at rest are hypotheses; nothing adopted"
admitted_observation_status: "none; known physics is not used"
audit_required_before_effective_retained: true
```

## Prior art and what is new

Block 57 (#8578): nearest-neighbour kinetic terms of the rates carry no delay, and a reference clock gives a front. Block 60 T5 (#8590): no delay in isotropic lengths without a rate of change of a rate. Block 62 T4 (#8592): exactly two travelling disturbances, transverse traceless. Blocks 58 and 67 (#8579, #8598): a formation event keeps the ledger if the record's energy matches what it replaces, and nothing is delayed. In the physics comparator the steady part of gravity is also a constraint, and the conservation of the source prevents its sudden change. The kinetic ratio `α + β = 0` corresponds to DeWitt's supermetric; this is named as a comparator only.

New here, from the probes worker and verified by the supervisor:
- the clock law with its `ë` term;
- the push at `0⁺` at every wave vector;
- the statement that `α + β = 0` is exactly the ratio at which a body at rest cannot change its energy by a jump;
- the packet's force changing before any strain could arrive.

## Exact target and obligation graph

Target: when a change of a body's energy reaches the clocks in the curvature member with block 62's kinetic term. The obligations are:
- (O1) the member's content;
- (O2) which modes travel;
- (O3) the clock law;
- (O4) a formation event and the special ratios.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- the steady part of the clock does not travel;
- at `α + β = 0` a body at rest cannot change its energy by a jump.

### N1 — Routes by which the sentences could fail or mislead
1. *Moving bodies.* Their stress sources the strains. Whether `α + β = 0` then admits exactly the changes that move energy by currents is open.
2. *A rate of change of a rate in the kinetic term.* Block 57 found that it needs a reference to distant clocks.
3. *Beyond second order, or the strong field.* Not treated.
4. *Other members.* Block 56's simplest member has no lengths; there block 57's results hold.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The member, the kinetic term, the coupling and bodies at rest are supplied and named.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no time metric | yes |
| blocks 60, 62 (#8590, #8592) | member and kinetic term | yes |
| block 55 (#8571) | coupling | yes |
| block 57 (#8578) | no delay from rate kinetics; label time global | yes (placed) |
| blocks 58, 67 (#8579, #8598) | formation keeping the ledger | no (placement) |
| block 54 (#8570) | a packet's fall | yes (control) |
| probes worker `w-jonathonsmac4f50-j03c0` | the derivation and control | yes (verified here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the clock is a constraint; a change of energy acts at once; alpha + beta = 0 forbids a jump at rest" | executed: relabelling blindness, symbolic | not applicable | executed: reduced equations at a general wave vector; control on a plane slice | executed: the switch-on series | every lattice wave vector at second order |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration. `α` and `β` stay free.

### N7 — Steelman
- Hostile reviewer: "Blocks 60 and 67 already said nothing is delayed." Reply: yes. The content here is the explicit clock law with its `ë` term, the push at `0⁺`, and the exact kinetic ratio that forbids the jump.
- Second objection: "This makes formation impossible." Reply: only at `α + β = 0`, and only for a jump at rest. Formation that keeps energy local, or moves it by currents, remains; block 58 shows the first is possible with the ledger kept.

### N8 — Cross-cycle echo
Blocks 57, 60 and 62 closed the delay route piece by piece. This note ties the result to the owner's "records form": a formation event must keep energy local if clocks are not to act at a distance.

## Falsifiers

- A lattice wave vector at which the rate's equation of this system carries a time derivative.
- `α + β = 0` with a solution of the reduced equations in which a body at rest changes its energy by a jump.

## Boundaries and non-claims

- The note holds at second order about the uniform state, for bodies at rest.
- It is conditional on blocks 60 and 62's clauses and block 55's coupling.
- `α` and `β` are not fixed.
- No gravitational claim is made, and known physics is not used.

## Imports
- `minimal_axioms`. Blocks 54, 55, 57–60, 62, 67 (PRs): restated or placed.
- Named standard imports at definition level:
  - Lagrangian mechanics of a quadratic form (equations of motion, constraints);
  - the DeWitt supermetric's ratio, as a comparator only;
  - floating-point FFT and the walk on a slice for the control.

## Review record
- **Who and when.** Supervisor-run block, the forty-ninth since the source-link direction opened, built from a probes worker's result.
- **Provenance.** Worker `w-jonathonsmac4f50-j03c0` (Claude Opus 5.5), the same family as the supervisor. The supervisor re-ran its check (14 of 14), ported the exact part and re-ran the control. No referee of another family has yet run.
- **Independence.** Mutation census: six mutations, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
