---
claim_id: admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk H = sum_a sigma_a S_a and block 78's compression to one record per site, as landed on main and supplied, with block 121's compressed source (open) and blocks 135 and 136 (open) placed; two records; uniform rates. Exact: (T1) under exclusion, for both exchange signs, the total energy current J = i[H2, D2] of two records (D2 the compressed energy dipole) is not kept, [H2, J] != 0, on Z^2 and Z^3 (witnesses: adjacent pairs; and on the 5 x 5 torus from the site densities). (T2) it is kept for free antisymmetric pairs in every dimension, where two records may share a site with opposite coins, and for excluded pairs on the line and on the ring of 7 sites. (T3) the member's identity e_u'' = sum dbar_i dbar_j Theta_ij with any finitely supported stress keeps the total current d/dt sum_x x e_u; the body-diagonal average keeps first moments; so with block 121's compressed source or block 135's average no local stress serves two excluded records in two or three dimensions. (T4) each record's energy current j(k) = (1/2) sin 2k is k - (2/3) k^3 + ..., the same at every species corner; collisions keep the crystal momentum, so for slow records the total current changes by -(2/3) Delta sum kappa^3 + O(kappa^5): the books hold at leading order for every species. The supervisor's own derivation (Claude Opus 5.5), checked by its runner; not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_2026_09_25.py
---

# One record per site keeps the books only at leading order: two excluded records lose their energy current in two and three dimensions

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact for two records within the landed walk and exclusion, with block 121's source placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with blocks 121, 135 and 136 placed; it reports whether two records under exclusion keep the books that the member's identity needs; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 135 and 136 (open) showed that one walker, or free walkers, keep exact books in the member's placement: energy flows as the two-step momentum, and the momentum flows as a symmetric stress. So the member's constraints admit that content iff `α = K/4`. The owner's reading of the records is one record per site (block 78: an interaction). Do records under that reading keep the same books?

- **T1: not exactly, in two or three dimensions.** For two records under exclusion, with either exchange sign, the total energy current is not kept.
- **T2: exactly on a line, and without exclusion.**
  - On a line, and on a ring, excluded pairs keep it.
  - Free antisymmetric pairs keep it in every dimension. Such pairs let two records share a site with opposite coins.
- **T3: why it matters.** With any local stress, the member's identity forces the total energy current to be kept. So with block 121's compressed source, or block 135's average, no local stress serves two excluded records in two or three dimensions.
- **T4: at leading order they do.**
  - Each record carries energy current `½ sin 2k`, which is `k − (2/3)k³ + …` and the same at every species corner.
  - Collisions keep the crystal momentum.
  - So for slow records the total current changes only at third order in their offsets. The books hold at leading order for every species, and fail only at the scale of a collision.

In plain terms, the field wants its source's energy to flow exactly as its momentum. A lone walker does that exactly. So do walkers that ignore one another, even when two share a site. Walkers that must keep out of each other's way do it exactly only in a line. In a plane or in space, each collision spoils the match slightly, by an amount that vanishes quickly for slow walkers. One record per site and the exact books are therefore in tension, and the tension lives at the lattice scale.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its exclusion, the currents and their placements, the member and the source link are supplied clauses. Nothing is adopted.
- **The walk** (block 54 as landed). `H = Σ_{a<d}σ_aS_a` on `ℤ^d`, with `S_a = (T_a − T_a⁻¹)/(2i)`, at a uniform rate.
- **Two records** (block 78 as landed).
  - Pair states are symmetric or antisymmetric in the two records.
  - `P` removes every state with both records on one site. The compressed generator is `H₂ = P(H⊗1 + 1⊗H)P`.
- **Energy and its current.**
  - The compressed energy density `h_x = P(e_x⊗1 + 1⊗e_x)P`, with `e_x = ½(Π_xH + HΠ_x)`, is block 121's source.
  - The energy dipole is `D₂ = Σ_x x h_x = P(D⊗1 + 1⊗D)P`, with `⟨t|D|s⟩ = ½(x_t + x_s)⟨t|H|s⟩`.
  - The total energy current is `J = i[H₂, D₂] = ½Σ_{x,y}(x − y) i[h_y, h_x]`.
- **The member's identity** (block 135): `ë_u = Σ_ij∇̄_i∇̄_jΘ_ij`, with `∇̄_if(x) = f(x) − f(x − e_i)`.
- **Comparators, named only:** a boost-invariant stress (the symmetry of the energy current and the momentum density); the conservation of the energy current in integrable chains.

## Theorem T1 — the current is not kept in two or three dimensions

*Statement.* Under exclusion, for both exchange signs, `[H₂, J] ≠ 0` on `ℤ²` and `ℤ³`.

*Proof.* Exact witnesses: `[H₂, J]` applied to adjacent pairs of records is nonzero. The same holds on the `5 × 5` torus, with `J` built from the site densities by minimal image. ∎

*Checked (B1).* Over `ℚ(i)`: every coin pair on the open lattices, and a sample of pair states on the torus.

## Theorem T2 — where the current is kept

*Statement.* `[H₂, J] = 0` in these cases:
- free antisymmetric pairs, on `ℤ`, `ℤ²` and `ℤ³`, where a site may hold two records with opposite coins;
- excluded pairs of both signs on the line, where block 121 T2 shows the chain pair is free;
- excluded pairs on the ring of 7 sites.

*Proof.*
- Free pairs: `J` is the sum of the two records' currents, and each record's current is its two-step momentum `P_j = S_jC_j`, which commutes with `H` (block 136).
- The line: the excluded chain pair is a free two-record hop (block 121 T2).
- The ring: exact computation. On a ring the excluded pair is one twisted band (blocks 121 and 130).

∎

*Checked (C1).* On adjacent pairs (open lattices), on a sample of pair states of the `5 × 5` torus (free), and on every basis state of the ring.

## Theorem T3 — why no local stress serves excluded records

*Statement.*
- (a) For any finitely supported stress, `Σ_x x_k Σ_ij∇̄_i∇̄_jΘ_ij(x) = 0`. So the member's identity with a local stress keeps `d/dt Σ_x x e_u(x)`, which is the total energy current of the placement `e_u`.
- (b) The body-diagonal average keeps every first moment.
- (c) So with block 121's compressed source, or with block 135's average of it, the total current is T1's `J`, and no local stress serves two excluded records in two or three dimensions.

*Proof.*
- (a) Sum by parts twice; each difference of a first moment is a total sum of a finitely supported field.
- (b) The average is symmetric about each site.
- (c) Combine (a), (b) and T1.

∎

*Checked (D1).*
- (a) On a rational stress supported on `5³`, where the double divergence is nonzero but its first moments vanish.
- (b) On a rational field.

## Theorem T4 — slow records keep the books at leading order

*Statement.*
- Each record's energy current is `j(k) = ½ sin 2k`, per component. It is `k − (2/3)k³ + O(k⁵)`, and `j(π + κ) = j(κ)`.
- A collision keeps the crystal momentum. So for slow records, with offsets `κ` from their species corners, the total current changes by `−(2/3)ΔΣκ³ + O(κ⁵)`, whether or not the records change species: `j` is the same at every corner, and the corners' parts cancel modulo `2π`.
- The books therefore hold at leading order for every species, and fail only at the scale of a collision.

*Proof.* Series. A species change that leaves the offsets small must shift both records by the same corner. ∎

*Checked (E1).* The series, the species blindness, and the third-order change on a sample with kept crystal momentum.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 135-136 (open): exact books for one or free walkers; the owner's reading of records (one per site, block 78) not tested"
source_of_blocker_text: blocks 78 (landed), 135 and 136 (open)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "other local placements (a total time derivative of a local sum); many records; whether a record's exclusion can be relaxed to opposite coins"
conditional_surface_status: "exact for two records at uniform rates; T3 for the placements with block 121's first moment"
hypothetical_axiom_status: "the exclusion, the placements and the member are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 78: one record per site is an interaction.
- **Opened, not landed.**
  - Block 121 (PR #9174): the compressed source.
  - Block 130 (PR #9187): the ring's twisted band.
  - Blocks 135 (PR #9195) and 136 (PR #9196): the exact books for one or free walkers.
- **In the literature.**
  - The symmetry of the energy current and the momentum density under boosts.
  - The conservation of the energy current in integrable chains.

  Both reference only.
- **New here:**
  - T1: the exact failure for excluded records in two and three dimensions;
  - T2: the line, and the free pairs;
  - T3: the consequence for the member;
  - T4: the third-order estimate for slow records.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: whether excluded records keep the member's books. The obligations are:
- (O1) the witness (T1);
- (O2) the controls (T2);
- (O3) the consequence (T3);
- (O4) the leading order (T4).

T1–T4 discharge them for two records. Open: other placements, and many records.

## No-Go Discipline Gate

The note's negative sentence: with block 121's compressed source, or any placement with the same first moment, no local stress meets the member's identity for two excluded records in two or three dimensions.

### N1 — Routes by which the sentence could fail or mislead
1. *Another placement.* A placement with a different first moment changes the total current by the rate of a local sum. Whether one such placement restores conservation is open. For records that are far apart before and after a collision, such a rate averages to zero, which suggests not; that is not proved here.
2. *Relaxed exclusion.* If two records may share a site with opposite coins (T2's free pairs), the books are exact.
3. *Slow records.* T4: the violation is of third order.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, exclusion, placements and member.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics or time metric in the axioms | yes |
| blocks 54, 78 (landed) | the walk; one record per site | yes (restated) |
| block 121 (open) | the compressed source | yes (restated) |
| blocks 130, 135, 136 (open) | the ring; the books; the identity | no (placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "two excluded records lose the total energy current in 2D and 3D, keep it on a line; no local stress serves them with block 121's first moment; slow records keep it to third order" | executed: `[H₂, J]` on adjacent pairs over `ℚ(i)` | executed: the `5 × 5` torus; the ring on every state | executed: first moments of a double divergence | executed: series and species | two records; placements with block 121's first moment |

### N6 — Partial-closure paths and primitive scan
No approved primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The energy current is defined only up to a total time derivative, so the failure is an artefact of the placement."
  - *Reply:* That is N1's route 1, and it is left open. T3 is stated for the placements the lane already uses: block 121's source, and block 135's average.
  - The failure has a mechanism that any placement must face: in two or three dimensions, collisions change the records' total two-step momentum.

### N8 — Cross-cycle echo
- Block 78 found that exclusion is an interaction.
- Block 121 found that the compressed source is what pulls.
- Blocks 135 and 136 found the exact books for free content.
- This note finds that excluded records keep those books exactly only on a line.

## Falsifiers

- A pair state of two excluded records on `ℤ²` or `ℤ³` for which T1's witnesses vanish.
- An excluded pair on a line whose current is not kept.
- A finitely supported stress whose double divergence has a nonzero first moment.

## Boundaries and non-claims

- The walk, the exclusion, the placements and the member are supplied.
- Two records only, at uniform rates. Many records are not treated.
- Other placements are open (N1).
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54 and 78, restated. Block 121's source, restated. Blocks 130, 135 and 136, placed.
- Named standard imports, at definition level:
  - exact arithmetic over `ℚ(i)`;
  - series expansion;
  - summation by parts.

## Review record

- **Who and when.** Supervisor-run block, the eighty-fifth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own runner. It is not refereed by another model family.
- **Before writing.**
  - Main was re-fetched.
  - The own prior-art check (memory, open PRs, probes attempts) found no test of the energy current under exclusion.
- **Corrections during the work.** Two drafts of the dipole were wrong: one included cross terms between the records, and one mislabelled the moving record after reordering the pair. The free-pair control failed for each, which exposed them. The dipole now carries `½(x_t + x_s)` on each hop, and the free pairs keep the current.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_2026_09_25.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
