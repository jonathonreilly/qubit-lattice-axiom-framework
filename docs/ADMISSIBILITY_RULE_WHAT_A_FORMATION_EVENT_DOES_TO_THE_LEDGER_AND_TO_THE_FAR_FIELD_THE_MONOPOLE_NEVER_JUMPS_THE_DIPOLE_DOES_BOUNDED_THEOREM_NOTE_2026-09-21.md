---
claim_id: admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_the_monopole_never_jumps_the_dipole_does_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied finite positive quadratic rate-field model with positive coupling, fixed unit walls and nonnegative diagonal rest sources: a single-site replacement preserves a positive ledger E exactly when E is below that target site capacity, with the stated unique bare mass. Harmonic moments of boundary flux equal six times source-charge moments. A ledger-preserving replacement keeps the total flux and changes the dipole by Q times the displacement from the charge centroid, possibly zero. Feasible formation probabilities preserve the mean dipole exactly when their centroid equals the charge centroid; charge-proportional probabilities suffice only if all their supported targets are feasible. No formation rule, stationary quantum body, global conservation law, or strict propagation front is derived."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_2026_09_21.py
---

# Conditional ledger preservation and harmonic boundary moments of a single-site replacement

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 56, in block 56's setting; no rule of formation is assumed; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a kept ledger, with the simplest bond energy of weight one; it reports what the replacement of a spread amplitude at rest by one record does to the ledger and to what the walls see; no rule of formation is assumed; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The results concern a supplied diagonal static source model, not the existence of a stationary amplitude under the full walk. With positive coupling and nonzero total bare mass, a record at target y can match the original ledger E iff E is below that site's capacity. The matching bare mass need not exceed the original total mass at an arbitrary target. That inequality holds when the target's inverse-operator diagonal is maximal on the original support.

Conditional on matching E, total wall flux is unchanged. The dipole changes by Q(y-Xbar), which is zero at a centroid target. Higher harmonic moments are readable at the wall but need not change either. Formation probabilities must be supported on feasible targets; zero expected dipole change imposes only a centroid condition, not a unique probability rule. A records-only source model with no other source or compensating field has a positive change in static boundary flux. No conservation of the full event dynamics follows from either static comparison.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, through the Record axiom's statement that a record is permanent, and through the memo's silence on a time metric, amplitude dynamics and a conserved energy. How and where records form is an open gate of the memo and the subject of the parked statistical postulate (registry entry 1); this note assumes nothing about it and makes no statement of it.

- **Setting.** Block 56's finite connected interior with grounded boundaries and `γ > 0`: `w = φ²`; `F = (2/γ) Σ_bonds (φ_x − φ_y)²`; walls held at `φ = 1`; `A` the average over the six neighbours; `G` the inverse of `1 − A` inside the box with zero walls, `g_y = G(y, y)`.
- **The amplitude at rest.** Weights `|χ_x|² ≥ 0` summing to one, positive bare rest energy `m`; by block 55 T2(c) its energy density is `m w_x |χ_x|²`, so in block 56's law it is the diagonal `M = diag(m_x)`, `m_x = m|χ_x|²`. Ledger `E = Σ m_x φ_x`; charges `q_x = (γ/12) m_x φ_x`; `Q = Σ q_x = (γ/12)E`; dipole `P = Σ q_x x`; `X̄ = P/Q`.
- **The record.** One body at rest at `y` with bare energy `m'`; ledger `m'φ'_y`.
- **Discrete-harmonic** `h`: `h_x` equals the average of `h` over the six neighbours at every interior site (constants, coordinates, `x² − y²`, `xyz`, …).
- **Odds.** Any non-negative `p_y` summing to one over sites where T1's condition holds. They are a free input; nothing is said about what they are.
- **Three densities** are compared: `|χ_x|²` (the conserved density of block 54), `|χ_x|² φ_x` (the charge density of block 56) and `|χ_x|² φ_x²` (the energy density of block 55).

The identity behind T2 is the second identity of Green on a lattice. That a sudden localization does not in general keep energy and the centre of energy is the known difficulty of the collapse models of Ghirardi, Rimini and Weber and of Pearle, and the question of what a spread amplitude sources is that of the semiclassical coupling discussed by Diósi and by Penrose. None is used as authority, and no statement of the rule of Born is made or used.

## Prior art and what is new

This is a finite quadratic model comparison. Standard boundary summation identities and concavity of a minimized quadratic ledger supply the useful mathematical content; no priority or universal physical claim is made.

## Theorem T1 — the ledger through the event

*Statement.* `E' = m'/(1 + (γ/12) g_y m')`. `E' = E` iff `m' = E/(1 − (γ/12) g_y E)`, and such an `m' > 0` exists iff `0 < E < 12/(γ g_y)`. With `m' = m` instead, and `y` a site of the largest `g` on the support, `E' ≤ E`.

*Proof.* Block 56 T3(a) gives `E'`; solve for `m'`. `E'` is increasing in `m'` with supremum `12/(γ g_y)`. The ledger equals the minimum over interior phi with fixed unit walls of `(2/γ) Σ_bonds (phi_x-phi_y)^2 + Σ_x m_x phi_x^2`. The objective is affine in the nonnegative mass vector at each phi, so its infimum is concave in that vector. Thus so on the simplex of bare energies with a given total it is smallest at a vertex, and the vertex with the largest `g` is the smallest of those. ∎

A region can show more than any one of its sites can (block 56 T3b). An amplitude spread over such a region, with a ledger above `12/(γ g_y)` for every `y`, cannot become one record with the books balanced. The bound here is target-specific on the finite box. Infinite-lattice constants in the original author experiments are deferred, not inputs to this finite result.

## Theorem T2 — what the walls see

*Statement.* For a static solution with charges `q` and any discrete-harmonic `h`, `Σ_{x inside, y wall, x∼y} (1 − φ_x) h_y = 6 Σ_x q_x h_x`.

*Proof.* `ψ = 1 − φ` vanishes on the walls and `(1 − A)ψ = q` inside. Then `Σ_x h_x q_x = Σ_x [h_x((1 − A)ψ)_x − ψ_x((1 − A)h)_x]`, the second term being zero. The terms with both sites inside cancel by symmetry; the terms with a wall neighbour leave `(1/6) Σ ψ_x h_y`. ∎

With `h = 1` this is block 56's statement that the flux is `(γ/2)E`: keep the ledger and the monopole does not move. With `h` a coordinate the walls read off the dipole; with `x² − y²` or `xyz`, the higher moments. Nothing about the arrangement of charges that a harmonic weight can see is hidden from the walls.

## Theorem T3 — the dipole change and feasible odds

*Statement.* With the ledger kept, `P' − P = Q(y − X̄)`, whatever `m'` is chosen to be otherwise it would also change `Q`. For odds `p`, the mean of `P' − P` is `Q(Σ_y p_y y − X̄)`. It is zero if `p_y = q_y/Q` AND every site with positive q is a feasible target, namely `E < 12/(γ g_y)`. Otherwise that distribution is not an admissible ledger-preserving formation rule. More generally such odds exist iff Xbar belongs to the convex hull of feasible targets, since the condition is precisely that their weighted mean equals Xbar. For `p_y = |χ_y|²` it is `Q(X̄_prob − X̄)`, and `X̄_prob = X̄` iff `Σ_x |χ_x|² φ_x (x − X̄_prob) = 0`; for an amplitude on two sites of equal potential `g` with unequal weights this fails, because `φ` is lower at the heavier site.

*Proof.* `P' = q'_y y` with `q'_y = (γ/12) m'φ'_y = Q`. The mean is linear in `p`. For two sites `a, b` with `g_a = g_b = g`, mutual potential `c < g` and `d_a > d_b` (`d = (γ/12)m|χ|²`), block 56 T4 gives `φ_a = (1 + d_b(g − c))/det` and `φ_b = (1 + d_a(g − c))/det`, so `φ_a < φ_b`: the charge weights `d_aφ_a : d_bφ_b` are less unequal than the probability weights `d_a : d_b`, and the charge-weighted centre lies nearer `b`. ∎

At exactly uniform phi the normalized densities coincide. In a regular weak-coupling expansion their differences are of order gamma. Nonuniform phi does not by itself require different centroids: symmetric distributions can share the same centroid. The asymmetric two-site argument above is a specific sufficient example, not a converse for arbitrary supports. The statement is a constraint any rule would face, not a rule. It concerns the first moment only.

## Theorem T4 — if only records source

*Statement.* If the amplitude sources nothing and there are no other sources or compensating fields, `φ = 1` before the event and the flux through the walls is zero; after it the flux is `(γ/2) m'φ'_y > 0`.

*Proof.* Block 56's law with `M = 0`, and T2 with `h = 1`. ∎

This is a comparison of two supplied static source conventions. It is not energy creation from nothing, a model of formation dynamics, or a claim that boundary information propagates instantaneously in a physical process. The continuous-time lattice-wave model of the companion delay note has small tails; its numerical support cone is a property of a chosen integrator.

## Historical experiments — deferred

Original large-box numerical formation, transient and higher-moment reports are preserved on the original PR branch. They have not been re-executed for this landing. Canonical evidence below checks finite exact systems only; the boundary identity itself supplies the proof for arbitrary discrete-harmonic h.

## No-Go Discipline Gate

The note's negative sentences: above `12/(γ g_y)` no single record keeps the ledger; the dipole change is fixed once the positive ledger and target are fixed, but can be zero; probability or energy weights need not hold the centroid, although some configurations do.

### N1 — Routes by which the sentences could fail
1. *A record spread over several sites.* The Record axiom has one record to a site; several records could share the ledger and then the bound is that of block 56's capacity. Not worked.
2. *A ledger that is not kept through a formation event.* Possible; then the outside sees the monopole change by the amount of T1's second sentence. The note states both.
3. *An amplitude in motion.* Then `K` is not diagonal (block 56, Remark to T1), the charges are `φ_x(Kφ)_x` with bond parts, and a record "at rest" does not carry the momentum. Not worked.
4. *Another bond energy.* T2 holds for every bond energy of weight one in the form "the ledger is a surface term"; the harmonic-moment identity uses the linear law of the simplest one. T1's bound changes (the alternative member has only the necessary positive-solution bound `m < 18/γ`).
5. *Records that move* (the owner's reading of 2026-09-20). Then the record is an amplitude again after it forms, and the event is a change of shape, not a freezing. Not worked.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Everything is in block 56's setting: the simplest bond energy, bodies at rest with a rest energy (supplied), walls at the ambient rate. The source replacement compares two static solutions; it supplies no trajectory or propagation time. Historical transient controls establish no strict physical front. The statement about odds requires the ledger to be kept at every site that has positive odds. It is a statement about first moments; it does not single out one rule.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; a record is permanent and sits one to a site; the absences that motivate the clauses | yes (premise) |
| block 56 (open PR #8573) | the exact static law, the ledger `Σ m φ`, the surface term, saturation, monotonicity | yes (restated) |
| block 55 (open PR #8571) | the energy density of an amplitude at rest; the two readings of the source | yes (restated) |
| block 57 (open PR #8578) | the wall-referred law used in the control | executed comparison |
| decision record (open PR #8572) | fork 4 | placement |
| registry entry 1 (`docs/repo/DEFERRED_DECISIONS.md`) | the parked statistical postulate | not used; named so that it is clear nothing of it is assumed |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "ledger kept iff `m' = E/(1 − (γ/12)g_yE)`, only below `12/(γg_y)`; wall flux moments = harmonic moments of the charges; monopole fixed, dipole jumps by `Q(y − X̄)`; mean over any odds; records-only static source convention: a positive flux change without other sources" | executed: exact rates of a five-site amplitude and of its record in a `7³` box | executed: the record's bare energy; the ledger's fall with the bare energy kept; a seven-site amplitude whose ledger cannot fit at the tested central site | executed: the total wall flux and its three first moments before and after, against the ledger and six times the dipole | executed: the dipole's jump; mean jumps for two kinds of odds; records-only flux | any amplitude at rest, any site, any box with walls at the ambient rate, simplest bond energy; T2 for every discrete-harmonic weight; the odds are arbitrary; the fork itself not decided |

### N6 — Partial-closure paths and primitive scan
`realized_state_primitive` grants evaluation at a supplied state and supplies no rule of formation, no odds and no density; it is not used. `scale_reference_primitive` and `kinetic_isotropy_primitive` do not bear on the event. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "This is the parked postulate by the back door." Reply: no odds are assumed, derived or proposed. T3 is a linear identity valid for every choice of odds, stated so that whoever takes up the parked question knows one exact constraint the clauses of blocks 53 to 56 would put on it; the note names the registry entry to make plain that nothing of it is used. Second objection: "A spread amplitude at rest with a rest energy is two supplied things at once." Reply: yes (blocks 54 to 56 say so); the note is exact within that setting and lists motion as not worked. Third objection: "Bare energy is not observable, so T1 says nothing." Reply: what is observable from outside is the ledger, and T1's content is the bound: above `12/(γg_y)` no bare energy works.

### N8 — Cross-cycle echo
Block 41 made a source a record; block 53 let a record enter as `log κ`; block 55 made the source the amplitude's energy density and left the two unreconciled; block 56 made both exactly solvable. Here the two readings are set side by side for one event, and they differ in the first thing the outside sees. Block 24 (unrecorded sites) asked a related question of the record layer: when is a window with unrecorded sites the same as the integrated exterior; there too the answer turned on what the unrecorded part is allowed to do.

## Falsifiers

- An amplitude at rest and a site `y` with `E < 12/(γg_y)` for which `m' = E/(1 − (γ/12)g_yE)` does not keep the ledger, or with `E ≥ 12/(γg_y)` for which some `m'` does.
- A static solution and a discrete-harmonic `h` for which the wall sum differs from `6Σ q_x h_x`.
- A formation event with the ledger kept whose dipole does not jump by `Q(y − X̄)`.
- Feasible odds proportional to `|χ_x|²φ_x` with a non-zero mean jump; two distinct equal-self-potential sites with unequal positive weights and mutual potential strictly less than the self-potential whose probability centre equals `X̄`.

## Boundaries and non-claims

The note does not decide whether an amplitude that has formed no record sources anything, nor whether a formation event keeps the ledger; it computes both cases. It assumes and proposes no rule of formation and makes no statement of the parked statistical postulate; T3 is an identity in arbitrary odds and concerns first moments only. Everything is in block 56's setting: the simplest bond energy, supplied bodies at rest with a rest energy, walls at the ambient rate, a static law. Motion, several records and records that move are not worked. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom; the Record axiom (a record is permanent; one to a site); the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 55, 56, 57 and the decision record (PRs #8571, #8573, #8578, #8572, open): restated or placed.
- Named standard imports at definition level: the second identity for the lattice operator `1 − A`; discrete-harmonic functions; concavity of a parallel sum.
- Reference only: Green; Ghirardi, Rimini and Weber; Pearle; Diósi; Penrose; Born (not used).

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8571](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8573](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8578](ADMISSIBILITY_RULE_A_DELAY_FOR_THE_RATE_FIELD_NEIGHBOUR_REFERRED_MOTION_DOES_NOT_PROPAGATE_A_REFERENCE_TO_DISTANT_CLOCKS_DOES_AT_A_SPEED_SET_BY_THE_LOCAL_RATE_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

The original author checks, simulations and review history are preserved at PR #8579 head `e526d22c1841c4d53170ad945fdb46b968832bff`, branch `physics-loop/admissibility-induced-law-block58-what-a-formation-event-does-to-the-ledger-and-to-the-far-field-20260921`. They are historical evidence, not a fresh independent audit. Landing review narrows the target-capacity quantifier, the conditional moment statements and the feasibility of formation odds. It replaces the concavity citation with the explicit minimization proof. Auxiliary experiments remain deferred and recoverable on that branch.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_2026_09_21.py
```

The fresh cache records the executed check count; review is not an audit verdict.
