---
claim_id: admissibility_rule_with_records_as_the_members_sources_no_movable_bond_clause_fixed_once_balances_the_two_charges_of_every_body_at_weak_field_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 60's curvature member and block 110's site equations as landed (walls held at w = l = 1, eps = 1/(8K)), solved self-consistently with records as its sources: one record per interior site, crossing to an empty interior neighbour at block 110's factor kappa = sqrt(w_x w_y)/(chi_x chi_y) (block 171, pushed), and the supplied clause family H = m sum_(x in C) w_x + sum over the movable bonds (interior bonds with exactly one end occupied) of g(kappa), g a smooth function of kappa alone: (T1) e_z = m w_z n_z + sum g'(kappa) kappa/2 and tau_z = sum g'(kappa) kappa/2 over the movable bonds at z; the field's-change clause (mu/2)(kappa - 1) has the activity clause's (e, tau); (T2) at weak field P - Q = 2 g'(1) B eps + eps^2 [-4 m g''(1) S - 2 m^2 n.Gn] + O(eps^3), the bracket for g'(1) = 0, with G the inverse of -Delta with the walls held, B the number of movable bonds and S the sum over them of (Gn)_x + (Gn)_y; G is entrywise positive, so a clause with g'(1) = 0 and g''(1) >= 0, and every jammed body, has P < Q at order eps^2, and a clause with g'(1) != 0 misses at order eps on the side of its sign; (T3) balance at order eps^2 needs a concave clause tuned to g''(1) = -m n.Gn/(2S), which differs between bodies (on the 5^3 box: single records -11/162, -145/1762, -23/222, -353/2546 times m at the centre, a face, an edge and a corner; the uniform law -3739/36462, -103877/1011162, -690875/6664644 times m for N = 1, 2, 3), and one body tuned at eps^2 needs a new tuning at eps^3 (centre: m^2 (472392 g3 - 73777 m)/280908); so no clause fixed once balances every body; (T4) the same clause on every interior bond touching a record has the same form with its own B and S and narrows the body dependence without removing it (a corner 2x2x2 cube: -5941/59232 m against -5941/23586 m). Exact (Fractions; the self-consistent weak-field series on the 5^3 box). Weak field only; the body dependence is chiefly wall proximity and compact against dilute, and the N-dependence on 5^3 is a small-box effect. A harvest of probe HIT #9366 (a Claude Opus 5.5 worker), refereed by Claude Sonnet 5 (same vendor family; the owner ruled on 2026-09-28 that a Sonnet referee counts). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_around_a_body_the_walks_rays_match_the_comparators_at_every_order_exactly_when_its_two_charges_agree_and_they_agree_only_when_hop_energy_balances_the_slowed_clocks_bounded_theorem_note_2026-09-24
runner: scripts/admissibility_rule_with_records_as_the_members_sources_no_movable_bond_clause_balances_every_body_2026_09_28.py
---

# With records as the member's sources, no clause fixed once on the movable bonds balances the two charges of every body at weak field

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact at weak field within blocks 60 and 110 as landed and block 171's crossing rule as placed; a harvest of probe HIT #9366, refereed by Claude Sonnet 5; nothing adopted or registered; unaudited)

This note works within block 60's curvature member and block 110's site equations as landed, with records as the member's sources; it reports whether a clause for a moving record's energy can make the member's two charges agree for every body; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Row 4 of the owner's third column is a moving record's energy.
- Block 110 (landed) showed the member's two charges agree, `P = Q`, only when the content's hop energy balances its slowed clocks. Rays around a body then bend as the comparator's do.
- Block 171 (pushed) found that moving records carry no energy, so their charges need a clause.
  - At prescribed fields, rest energy alone gives `P < Q`.
  - A clause giving each crossing an energy (the activity clause) gives `P > Q` at weak field.

Probe HIT #9366 solved the member self-consistently with the records as its sources. This note harvests it with the referee's scope.

- **T1: what a clause on the movable bonds supplies.** A bond term `g(κ)` gives each end `e = τ = g′(κ)κ/2`. A clause that counts only the field's change of the crossing activity, `(μ/2)(κ − 1)`, has the same `(e, τ)` as the activity clause.
- **T2: the charges at weak field.** With `ε = 1/(8K)`,

  `P − Q = 2g′(1) B ε + ε² [−4m g″(1) S − 2m² n·Gn] + O(ε³)`,

  the bracket being for `g′(1) = 0`. Here `G` is the inverse of `−Δ` with the walls held, `n` marks the occupied sites, `B` counts the movable bonds, and `S` sums `(Gn)_x + (Gn)_y` over them.
  - `G` is positive everywhere. So a clause with `g′(1) = 0` and `g″(1) ≥ 0`, and every jammed body, has `P < Q`.
  - A clause with `g′(1) ≠ 0` misses at order `ε`, on the side of its sign.
- **T3: balance needs tuning to the body.** Balance at order `ε²` needs a concave clause with `g″(1) = −m n·Gn/(2S)`.
  - That value differs between bodies. On the `5³` box it is `−11/162, −145/1762, −23/222, −353/2546` (times `m`) for a single record at the centre, a face, an edge and a corner.
  - Once tuned at `ε²`, one body needs a new tuning at `ε³`.
  - So no clause fixed once balances every body.
- **T4: a clause on every bond touching a record comes closer.** It has the same form with its own `B` and `S`. It narrows the body dependence (a corner `2×2×2` cube needs `−5941/59232 m` rather than `−5941/23586 m`), but does not remove it. The referee's floating-point search on a `33³` box found the spread of the needed tuning falls from a factor 7.8 to 1.23 across single records and cubes.

In plain terms: a lump of records slows its own clocks by an amount that grows with the lump's own pull, which depends on its whole size and shape. Energy put on the records' moves can pay for that only where the records can move: at the lump's edge, for the movable bonds. So the energy a move must carry, for the lump to bend light as the comparator's lump does, depends on the lump. No single rule for records serves every lump. A rule that counts every bond at a record, inside the lump too, comes much closer, but still not exactly.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-28.
  - "Records form."
  - "A site never carries more than one record; records are permanent."
  - "Admissibility is not a dynamics axiom."
  - The member, the crossing rule and the clause are supplied clauses. Nothing is adopted.
- **The member** (block 60, landed). Rates `w = e^u`, lengths `ℓ = χ² = e^λ`, `N = wχ`, and the field energy `F = −8KΣ_bonds(N_y − N_x)(χ_y − χ_x)`, with walls held at `w = ℓ = 1`.
- **The site equations** (block 110, landed), quoted: "`(Δχ)_z = −e_z/(8K w_z χ_z)`", "`(ΔN)_z = (e_z + 2τ_z)/(8Kχ_z)`" and "`P − Q = (1/8K) Σ_z [2τ_z − e_z(1 − w_z)/w_z]/χ_z`". Here `e = ∂H/∂u` and `τ = −∂H/∂λ`.
- **Records** (block 171, pushed, placed). One per interior site, in a configuration `C`, crossing to an empty interior neighbour at `κ = √(w_xw_y)/(χ_xχ_y)`.
- **The clause** (supplied, a family). `H = mΣ_{x∈C} w_x + Σ_{b∈∂C} g(κ_b)`. Here `∂C` is the set of interior bonds with exactly one end occupied (the movable bonds), and `g` is smooth at `κ = 1`.
  - Block 171's rest-only clause is `g = 0`.
  - Its activity clause is `g = μκ/2`.
- **A stationary law of records.** Its charges are averages over the law. "Balance" in a law means `⟨P⟩ = ⟨Q⟩`, not balance configuration by configuration. At zero field the law is block 171's; the uniform law is its `W = 1` case.
- **Imports, named at definition level.**
  - The analytic implicit function theorem: the self-consistent weak-field branch exists and is analytic in `ε`.
  - The entrywise positivity of the inverse of an irreducible nonsingular M-matrix.
  - Analytic perturbation of a finite chain's stationary law: a law that depends on the fields moves at `O(ε)`, so its average of an `O(ε²)` quantity moves at `O(ε³)`.
  - Exact rational arithmetic.

## Prior art and what is new

- **Block 110** (landed): the two charges for any content, and `4K(P − Q) = H_hop − F` for content away from the walls. The landed note on a ledger linear in the rates (2026-09-21) names the comparator's reading: a static body's two far-field coefficients agree only when its stresses are counted (Tolman and Komar).
- **Block 171** (pushed): moving records carry no energy; its clauses at prescribed fields.
- **Probe `internal-hop-energy-and-the-two-masses`** a1 (unrefereed): a confining agent's stress enters `ΔN` and must cancel the hop energy.
- **Probe HIT #9366** (a Claude Opus 5.5 worker, `w-jonathonsmac4f50-jae2d`): the self-consistent case, harvested here.
- **The referee** (Claude Sonnet 5, 2026-09-28).
  - Re-derived the site equations at 160 digits, and the `ε²` bracket by hand and by an exact series on the `4³` and `5³` boxes.
  - Checked every tuned value and the `ε³` formula, and solved the nonlinear equations at 40 digits through `ε⁴`.
  - Found the local variant of T4 and the scope limits below.
- **New here.** The harvest with the referee's scope, the supervisor's own exact series, and T4 checked exactly on the `5³` box.

## Theorem T1 — what a clause on the movable bonds supplies

*Statement.*
- (a) A bond term `g(κ)`, with `κ = exp((u_x + u_y − λ_x − λ_y)/2)`, gives `∂/∂u_x = −∂/∂λ_x = g′(κ)κ/2`.
- (b) So `e_z = m w_z n_z + Σ_{b∋z} g′(κ_b)κ_b/2` and `τ_z = Σ_{b∋z} g′(κ_b)κ_b/2`, the sums over the movable bonds at `z`.
- (c) The clause `(μ/2)(κ − 1)` differs from `μκ/2` by a constant, so it has the same `(e, τ)`. Its hop energy vanishes with the field, but its `τ` does not, so block 171's weak-field result `P > Q` applies to it.

*Proof.* Differentiation (runner B1). ∎

## Theorem T2 — the charges at weak field

*Statement.* The self-consistent member exists for small `ε` and is analytic in `ε`. With `B` the number of movable bonds and `S = Σ_{b∈∂C}[(Gn)_x + (Gn)_y]`:

`P − Q = 2g′(1) B ε + ε² [−4m g″(1) S − 2m² n·Gn] + O(ε³)`,

the bracket for `g′(1) = 0`. For `g′(1) ≠ 0` the `ε²` coefficient differs from the bracket: on the `5³` box, the centre record with `m = 3/2`, `g′(1) = 1/5` and `g″(1) = −2/3` gives `3777/850`. Since every entry of `G` is positive:
- a clause with `g′(1) = 0` and `g″(1) ≥ 0`, and every jammed body (`S = 0`), has `P < Q` at order `ε²`;
- a clause with `g′(1) ≠ 0` and `B > 0` has the sign of `g′(1)` at order `ε`.

*Proof.*
- Existence: the linearisation at `ε = 0` is `−Δ` twice with Dirichlet walls, which is invertible (the named implicit function theorem).
- Order `ε`: at zero field `Στ = g′(1)B`.
- Order `ε²` with `g′(1) = 0`:
  - At first order `χ − 1 = 1 − N = εmGn`, so `u = −2εmGn` and `κ_b − 1 = −2εm[(Gn)_x + (Gn)_y]`.
  - Then `Στ = −2εm g″(1) S`, and the rest part gives `e(1 − w)/w = 2εm² n(Gn)`.
- The runner iterates the fixed point `χ − 1 = εG[e/(wχ)]`, `1 − N = εG[(e + 2τ)/χ]` as exact power series in `ε`, on the `3³` interior of the `5³` box. It matches the formula at orders `ε` and `ε²` for five configurations (runner C1), and checks the positivity of `G` (C2). ∎

## Theorem T3 — balance needs tuning to the body

*Statement.*
- (a) With `g′(1) = 0`, balance at order `ε²` holds iff `g″(1) = −m n·Gn/(2S)`, a concave clause.
- (b) On the `5³` box the value is `−11/162, −145/1762, −23/222, −353/2546` (times `m`) for a single record at the centre, a face, an edge and a corner.
- (c) Under the uniform law it is `−3739/36462, −103877/1011162, −690875/6664644` (times `m`) for 1, 2 and 3 records: the ratio of the law's averages, since the law's field dependence enters only at `ε³`.
- (d) For the centre record tuned at `ε²`, the `ε³` term is `m²(472392 g‴(1) − 73777m)/280908`.
- So no clause fixed once balances two bodies whose tuned values differ, and one body needs a new tuning at each order.

*Proof.* The values are exact (runner D1, D2). For (d) the series is carried to `ε³` for two choices of `(m, g‴)` (D3). ∎

*Scope (the referee's).*
- On the `5³` box every site touches a wall. There the values for 1, 2 and 3 records differ by `0.2%` and `1.1%`. The ordering reverses by side 7, and the spread shrinks slowly with the box.
- Dilute records share the single-record value: `−0.0625` for four far-apart records on `49³` (floating point).
- So the robust body dependence is wall proximity and compact against dilute. The compact evidence, cubes of side 2 to 5 needing `−0.112` to `−0.284` (times `m`) on `17³`, is floating point, and the `17³` box inflates the values by 2 to 7% against `49³`.
- Unbounded growth with the body's size is not established.

## Theorem T4 — a clause on every bond touching a record comes closer

*Statement.* Put the same `g(κ)` on every interior bond with at least one end occupied, the occupied pairs included. Then T2 holds with `B` and `S` taken over those bonds. For a single record nothing changes. For a corner `2×2×2` cube on the `5³` box the tuned value is `−5941/59232 m`, against `−5941/23586 m` for the movable-bond clause and `−353/2546 m` for the lone corner record. So the spread narrows but does not close.

*Proof.* The same derivation; the runner checks the series against the formula for two configurations and the three values (runner F1). The referee's floating-point search on `33³` found the spread of the tuned value across a single record and cubes of side 2 to 9 falls from a factor 7.8 to 1.23. ∎

## What this settles and what it does not

- **Settled** (weak field, within the premises).
  - With records as the member's sources, `P − Q` has the form of T2.
  - Balance needs a concave clause tuned to the body. No clause fixed once on the movable bonds balances every body.
  - A clause on every bond touching a record narrows the body dependence but does not remove it.
- **For the owner's row 4.**
  - A record's clock deficit grows with the body's own pull. Energy on the records' moves pays for it only where the moves are, at the edge for movable bonds.
  - So the two charges agree only for a clause matched to the body, and the owner's choice of a moving record's energy cannot be fixed once for every body within these families.
  - The comparator balances through a static body's own stress. The member reads only the content's length-conjugate stress (block 110), and records' exclusion supplies none. That is why a clause is needed at all.
- **Not settled.**
  - Clauses outside the family: non-local ones, as the probe suggested, or ones depending on more than `κ`.
  - Finite field.
  - The clocked law `W ≠ 1` of block 171 T3, which favours clumps.
  - Larger boxes exactly.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
- Weak field, order `ε²` (and `ε³` for one body).
- The clause family `g(κ)` on the movable bonds (T2, T3), and on every bond touching a record (T4).
- The exact values are on the `5³` box.
- "Every body" means every body among those examined. The no-balance statement needs two bodies with different tuned values, which the box supplies.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The member, the crossing rule, the clause family and the laws are supplied.

### N4 — Dependencies
Blocks 60 and 110 (landed; 110 quoted). Block 171 (pushed), placed; its crossing rule is restated and the clause's derivatives re-derived.

### N5 — Resolution
- per_element: executed - the clause's derivatives; the equality of the activity and field's-change clauses
- per_site: executed - the exact self-consistent series on the 5^3 box for five configurations, through eps^2 (and eps^3 for the centre)
- per_mode: executed - the tuned values for single records at four site classes and under the uniform law for N = 1, 2, 3
- per_block: executed - entrywise positivity of the inverse of -Delta with held walls; the local variant's form and its narrower spread on 5^3
- lattice_wide: checked and not executed - larger boxes (floating point in the probe and the referee); the clocked law W != 1; finite field

### N6 — Primitive boundary
No new primitive, selection or physical interpretation is adopted.

### N7 — Strongest objection
"A local clause might still balance every body." Within the family on all bonds touching a record it does not, though it comes close (T4). The probe's claim that balance "would need a non-local clause" is too strong, and is not made here.

### N8 — Earlier claims
The probe's HIT said "no clause fixed once balances two bodies" without naming the family. The note states the family.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 171: the member solved self-consistently with records as its sources; can a clause balance the two charges?"
source_of_blocker_text: probes task J:derive:the-member-with-record-sources (after block 171)
reachability_to_target: advances
next_trace_action: "clauses beyond the family; finite field; the clocked law"
```

## Review record

- **Author checks (not a review PASS).** The supervisor's own runner, exact, `TOTAL: PASS=15 FAIL=0`. Mutation census 7/7, each failing in its own family only.
- **Provenance.**
  - Derived by probe worker `w-jonathonsmac4f50-jae2d` (Claude Opus 5.5), HIT #9366, `check.py` 20/20.
  - Refereed by Claude Sonnet 5 on 2026-09-28: confirmed with scope corrections, all applied here (the clause family, the body dependence, weak field only, the local variant). Same vendor family; the owner ruled on 2026-09-28 that a Sonnet referee counts for harvest.
  - Harvested by the supervisor (Claude Opus 5.5), with its own runner.
