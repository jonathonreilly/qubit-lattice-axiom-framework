---
claim_id: admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 60's homogeneous kinetic model and block 101's static clock law, with block 139's staggered mass and the books' zero of energy, all as landed on main, and block 146's zero-mode constraint 24 alpha l^3 lamdot^2 = m (open) placed; uniform content on a closed lattice; unit rate. (T1) exact: the walk's spectrum is symmetric about the books' zero, so the half-filled sea has negative energy; on a uniformly stretched lattice it is -I/l per site for the massless walk (I = (3 + sqrt 3 + 3 sqrt 2)/8 on the 4^3 torus) and -<sqrt(mu^2 + s^2/l^2)> per site with the staggered mass mu; per unit volume neither stays constant as the lattice stretches, and with block 146's pressure the massless sea has p = rho/3 and the massive sea 0 < p/rho < 1/3, while an energy constant per unit volume has p = -rho; under one record per site the many-walker hopping anticommutes with the product of sublattice signs, so the hard-core sea's energy is negative too (checked exactly on the 4^3 torus with two walkers). (T2) exact: if the member sees the sea's energy, a closed lattice holding only the sea has no uniform motion (and, by block 146, no static state); with rest content m0 and the massless sea it turns at l = I/m0, where it bounces, with an exact history; with the massive sea it reaches large lengths only if m0 > mu, and has no uniform motion at all if m0 <= mu. (T3) if the member sees energy measured above the sea, the sea drops out of the zero mode and block 146 holds unchanged; the subtraction is a constant per site and keeps the books. Which zero the member sees is not fixed by the landed clauses. The supervisor's own derivation (Claude Opus 5.5); not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_2026_09_25.py
---

# The member's zero mode tests the zero of energy: if the member sees the half-filled sea, a closed lattice bounces or cannot move

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 60's homogeneous kinetic model with block 146's zero-mode constraint, for uniform content on a closed lattice; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 60, 101 and 139 as landed on main (the homogeneous kinetic model, the static clock law and the staggered mass with the books' zero of energy), with block 146 placed; it reports what the member's zero mode says about the zero of energy the member sees; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 146 (open) found that a closed lattice with content must stretch or shrink as a whole, with `24αℓ³λ̇² = m` for content of energy `m` per site. The walker's sea, all negative-energy states filled, is content too. The books fix the zero of energy at the middle of the walk's spectrum (block 139). Relative to that zero the half-filled sea has negative energy. So which zero the member sees has consequences.

- **T1: the sea's energy.** The spectrum is symmetric about the books' zero, so the half-filled sea's energy is negative.
  - On a uniformly stretched lattice the massless sea has `−I/ℓ` per site, with `I` the zone average of `|sin k|` (`(3 + √3 + 3√2)/8` on the `4³` torus).
  - With the staggered mass `μ`, the sea has `−⟨√(μ² + s²/ℓ²)⟩` per site.
  - Per unit volume neither stays constant as the lattice stretches: the massless sea dilutes like negative top-speed content, and the massive sea tends to negative content at rest.
  - With block 146's pressure the massless sea has `p = ρ/3`, the pressure of top-speed content, and the massive sea `0 < p/ρ < 1/3`. An energy that is constant per unit volume would need `p = −ρ`.
  - Under one record per site the hard-core sea's energy is negative too.
- **T2: if the member sees the sea.**
  - A closed lattice holding only the sea has no uniform motion, and (block 146) no static state: no solution at all.
  - With content at rest, `m₀` per site, and the massless sea, the lattice turns at `ℓ = I/m₀` and bounces there, with an exact history.
  - With the massive sea it can reach large lengths only if `m₀ > μ`: more than one walker's rest energy of content per site. If `m₀ ≤ μ` it has no uniform motion at all.
- **T3: if the member sees energy above the sea.** The sea drops out of the zero mode and block 146 holds unchanged. The subtraction is a constant per site, so it keeps the books.

In plain terms: the lattice's vacuum, the filled sea of walkers, has negative energy, because the walk's energies come in plus-and-minus pairs and the sea fills the minus half. If the member counts that energy, a closed lattice with nothing else in it cannot exist, and one with a little matter cannot shrink below a certain size; it bounces. If the member counts only energy above the sea, none of this happens. Unlike a constant energy of empty space, the sea's energy on this lattice thins out as the lattice stretches, because the number of sites is fixed. The landed clauses do not say which zero the member sees; that is a reading question.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The member, its kinetic term, the walk, its sea and the zero of energy the member sees are supplied clauses. Nothing is adopted.
- **The walk and its zero of energy** (block 139 as landed). The walk `H = Σσ_aS_a`, with or without the staggered mass `μ`. The books admit one site rest energy, the staggered mass, and fix the zero of energy at the middle of the spectrum.
- **The sea.** The half-filled state: every negative-energy one-walker state filled, as in blocks 76 and 130. A filled sea presupposes that walkers exclude one another; the exchange sign is itself supplied (block 128). Its energy per site is the zone average of the negative eigenvalues.
- **Crossing bonds** (block 60's premise). On a uniform stretch, hopping is divided by `ℓ`; the staggered mass is not.
- **The zero-mode constraint** (block 146, open). `24αℓ³λ̇² = m(λ)` at the closing ratio, `s = 3`, unit rate. The length's equation keeps it for any `m(λ)` (block 60 T5(b)).
- **Standard imports, named at definition level.** Exact symbolic arithmetic, including the exact sum of square roots on a finite torus.

## Theorem T1 — the sea's energy

*Statement.*
- (a) The walk's plane-wave block is traceless, with eigenvalues in `±` pairs. So the half-filled sea's energy per site is minus the zone average of the positive eigenvalues.
- (b) On a uniformly stretched lattice:
  - the massless sea has `−I/ℓ` per site, with `I = ⟨|s|⟩` and `s = (sin k_a)`; on the `4³` torus `I = (3 + √3 + 3√2)/8`; the average runs over the whole zone, including the eight corners where `s` vanishes, so all eight of the walk's light species (block 135) contribute;
  - with the staggered mass, the block on `(k, k + (π, π, π))` squares to `(μ² + s²/ℓ²)`, so the sea has `−⟨√(μ² + s²/ℓ²)⟩` per site.
- (c) Per unit volume the sea's energy is `−I/ℓ⁴` or `−⟨√(μ² + s²/ℓ²)⟩/ℓ³`. Both change with `ℓ` at every length, so the sea never acts as a constant energy per unit volume.
- (d) Under one record per site (block 78's compression), on `ℤ³` or an even torus, the many-walker hopping anticommutes with the product of the sublattice signs `(−1)^{x₁+x₂+x₃}` over occupied sites. So in every sector its spectrum is symmetric about zero, and the hard-core sea's energy is negative whenever the hopping acts at all.
- (e) With block 146's pressure, `dm/dλ = −3pℓ³`, the massless sea has `p = ρ/3` exactly. With the staggered mass each mode has `p/ρ = y/(3(μ² + y))`, `y = s²/ℓ²`, so `0 ≤ p/ρ < 1/3`, and the massive sea has `0 < p/ρ < 1/3`. An energy that is constant per unit volume has `p = −ρ`. So neither sea acts as one.

*Proof.* (a) and (b): runner B1. (c): runner E1. (e): runner E2; every mode's energy has the same sign, so the sea's ratio lies between its modes' ratios. (d): each hop moves one walker by one step and flips exactly one sign, so every matrix element joins states of opposite total sign; the compression keeps this. Runner B2 checks it exactly for two walkers on the `4³` torus (8064 states). ∎

## Theorem T2 — if the member sees the sea

*Statement.* Take block 146's constraint with `m` including the sea's energy.
- (a) With the sea alone, `m < 0` and the constraint has no solution: there is no uniform motion. With block 146 T1 (no static state), a closed lattice holding only the sea has no solution at all.
- (b) With rest content `m₀` per site and the massless sea, `m = m₀ − I/ℓ`.
  - The lattice turns at `ℓ = I/m₀`, where `λ̈ = m₀⁴/(48αI³) > 0`: it bounces.
  - Its history is `t(ℓ) = ±(√(24α)/m₀²)[(2/3)(m₀ℓ − I)^{3/2} + 2I(m₀ℓ − I)^{1/2}]`.
- (c) With the massive sea, `m = m₀ − ⟨√(μ² + s²/ℓ²)⟩`. This rises with `ℓ` toward `m₀ − μ`.
  - If `m₀ > μ`, the lattice turns once where `m` vanishes and then reaches arbitrarily large lengths.
  - If `m₀ ≤ μ`, there is no uniform motion at all.

*Proof.*
- (a) and (b): runner C1 and C2. The turn uses the length's equation, `2c_kℓ³λ̈ + 3c_kℓ³λ̇² + dm/dλ = 0` at `λ̇ = 0` with `c_k = −24α`.
- (c): each mode's `√(μ² + s²/ℓ²)` falls with `ℓ`, from `|s|/ℓ` at small `ℓ` to `μ` at large `ℓ` (runner D1). ∎

## Theorem T3 — if the member sees energy above the sea

*Statement.* If the member's source is energy measured from the sea, the sea contributes nothing to the zero mode, and block 146 holds unchanged.

*Proof.* In a translation-invariant sea the subtraction is a constant per site. Its current vanishes, so the books `ė + ∇·P = 0` are kept. ∎

The landed clauses fix the zero of one-walker energies (block 139), not the zero the member sees in a many-walker state. T2 and T3 are the two readings. For the massive walk the difference is at least one walker's rest energy per site.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 146 (open): the zero mode is an expansion for content of positive energy; the walker's sea has negative energy relative to block 139's zero"
source_of_blocker_text: block 146 (open); block 139 (landed)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "which zero the member sees (a reading question for the owner); the hard-core sea under one record per site; an other-family referee"
conditional_surface_status: "uniform content on a closed lattice; block 146's zero-mode constraint on block 60's homogeneous model; the free walk's sea"
hypothetical_axiom_status: "the member, the walk, its sea and the zero the member sees are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 60: the homogeneous model.
  - Block 101: the static clock law.
  - Block 139: the staggered mass and the books' zero of energy.
  - Block 130: the hard-core sea on a ring.
- **Opened, not landed.** Block 146 (the zero-mode constraint).
- **Probes.** Probe #9198 (unrefereed) computes the free sea's energy per site, `I = ⟨|s|⟩`, as its constant for the strained sea. No attempt poses the zero-mode question.
- **In the literature.** The energy of a filled sea and its subtraction (normal ordering), and the question whether a gravitating field sees the vacuum's energy. Reference only.
- **New here:**
  - T1(c): on this lattice the sea's energy per unit volume changes as the lattice stretches, never constant.
  - T2: the consequences if the member sees the sea: no closed lattice with the sea alone, a bounce at `ℓ = I/m₀`, and the threshold `m₀ > μ`.
  - T3: the alternative keeps the books.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: what the zero mode says about the zero of energy the member sees. The obligations are:
- (O1) the sea's energy on a stretched lattice (T1);
- (O2) the zero mode with the sea (T2);
- (O3) the alternative (T3).

T1–T3 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- if the member sees the half-filled sea, a closed lattice holding only the sea has no solution;
- with the massive sea and rest content of at most one walker's rest energy per site, it has no uniform motion.

### N1 — Routes by which the sentences could fail or mislead
1. *The reading.* Both sentences hold only if the member sees the sea's energy. T3 gives the other reading.
2. *The sea.* T2 is stated for the free walk's half-filled sea. Under one record per site the hard-core sea's energy is also negative (T1(d)), so T2(a) holds for it too; its value, and so the bounce length, is not computed here.
3. *The homogeneous model.* Uniform content; block 60's model with `s = 3`.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied member, walk, sea and zero of energy.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 60 (landed) | the homogeneous model; crossing bonds | yes (restated) |
| block 139 (landed) | the staggered mass; the books' zero | yes (restated) |
| block 146 (open) | the zero-mode constraint | yes (restated) |
| probes #9198 (unrefereed) | the constant `I` | no (context) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "if the member sees the half-filled sea, a closed lattice holding only the sea cannot move, one with rest content bounces at `ℓ = I/m₀` (massless sea) or needs `m₀ > μ` (massive sea)" | executed: the spectrum's symmetry; the massless sea on `4³` | executed: the stretched spectra | executed: each massive mode as the lattice stretches | executed: the constraint with the sea; the bounce and its history; the threshold | uniform content; the homogeneous model |

### N6 — Partial-closure paths and primitive scan
`scale_reference_primitive` is not used; nothing here needs a scale. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Of course one subtracts the vacuum. The sea's energy is not physical."
  - *Reply:* That is reading T3, and the note states it keeps the books. But the landed clauses fix the zero of one-walker energies at the middle of the spectrum, and the sea's energy relative to that zero is a definite negative number. Whether the member sees it is not fixed by any landed clause. T2 shows that the choice is not idle: it decides whether a closed lattice with little content can exist.

### N8 — Cross-cycle echo
- Block 139: the books fix the zero of one-walker energies.
- Block 146: the zero mode is an expansion.
- This note: the zero the member sees in a many-walker state is a separate choice, with consequences.

## Falsifiers

- A traceless walk block whose half-filled sea has non-negative energy.
- A uniform motion of a closed lattice holding only the sea, with the sea seen by the member.
- An error in the runner's torus sum, spectra or series.

## Boundaries and non-claims

- Uniform content on a closed lattice; block 146's constraint on block 60's model; the free walk's sea.
- Which zero the member sees is not decided. Both readings are stated.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 60, 76, 78, 101, 128, 130 and 139 (landed), restated. Block 146 (open), restated.
- Named standard imports: exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the ninety-fifth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found the sea's constant in #9198 and the books' zero in block 139, and no treatment of the sea in the zero mode.
- **After opening (a panel's report).** A three-lens panel (programme strategy, lattice field theory, gravitation theory; all three Claude Opus 5.5 subagents, the same model family as the supervisor, so not an independent check) made three points, now in the note.
  - The sea's equation of state was left unstated. With a cutoff that stretches with the lattice, the sea's energy dilutes like negative top-speed content, not like a constant energy of empty space. T1(e) now states it (runner E2).
  - Every sea quantity counts all eight light species. T1(b) now says so.
  - T2 and T3 restate the question whether a gravitating field sees the vacuum's energy, in the lane's terms. It is a reading question, not a derivation target: which zero the member sees stays with the owner.
- **Independence.** Mutation census: seven mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_2026_09_25.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
