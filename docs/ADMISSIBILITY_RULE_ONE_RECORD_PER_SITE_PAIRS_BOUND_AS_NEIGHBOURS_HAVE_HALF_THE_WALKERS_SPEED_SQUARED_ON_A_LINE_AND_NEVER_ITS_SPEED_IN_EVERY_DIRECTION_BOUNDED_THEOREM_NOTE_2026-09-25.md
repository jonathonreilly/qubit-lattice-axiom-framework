---
claim_id: admissibility_rule_one_record_per_site_pairs_bound_as_neighbours_have_half_the_walkers_speed_squared_on_a_line_and_never_its_speed_in_every_direction_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk and block 78's compression to one record per site, as landed on main, with a supplied neighbour possibility shift V = g M (a hermitian term on the two coins of adjacent records) and block 115 (open) placed; two records, either exchange sign. Exact: (T1) on the line (walkers sigma_z D) a pair of equal coins bound as neighbours by V has E = V + sin^2(K/2)/V for every V, so c^2 = d^2(E^2/2)/dK^2 at rest is 1/2, half the walker's; opposite coins give E = V + cos^2(K/2)/V, inverted. (T2) on Z^3 at strong binding the pair's second-order generator for keeping its bond e_a is 5/2 - (1/2) cos K_a sigma_a sigma_a - sum_{b != a} cos K_b sigma_b sigma_b: exclusion halves the along-bond term. (T3) for every rotation-covariant possibility shift, on every rest level of the strongly bound pairs, the sum over the three axes of the weight matrix (the K^2 form of E^2/2) is at most 3/2, against 3 for a free record, so no strongly bound pair has weight one along all three axes; fermion pairs on a zero-spin ray never roll and have weight -1/2 along their bond. (T4) controls. Moderate binding in three dimensions, the staggered mass, pushes and more records are not treated. The supervisor's own derivation (Claude Opus 5.5), checked by its runner; not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_one_record_per_site_pairs_bound_as_neighbours_have_half_the_walkers_speed_squared_on_a_line_and_never_its_speed_in_every_direction_2026_09_25.py
---

# One record per site: pairs bound as neighbours have half the walker's speed squared on a line, and never its speed in every direction

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact on the line, and at leading order in the binding in three dimensions, within the landed walk and exclusion with a supplied neighbour possibility shift and block 115 placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with a supplied neighbour possibility shift and block 115 placed; it reports how pairs bound by that shift move, on a line and in space; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 115 (open) found that two walkers stuck on one site have a rest energy, but that one record per site forbids the sticking. Under one record per site the only binding left is between neighbours. The owner's reading of records supplies such a binding: the possibility at a site shifts as the neighbourhood changes. This note asks how a pair bound that way moves.

The measure used is the pair's speed squared, `c² = d²(E²/2)/dK²` at rest. It ties the pair's inertia to its rest energy. A free record has `c² = cos 2k = 1` at rest along every axis (block 106 as landed), so the three axes sum to 3. On a level that is degenerate at rest, the same second derivative is a matrix on the level, the weight matrix.

- **T1: on a line, exactly half, for every binding.** Two records with equal coins, bound as neighbours by any `V`, have exactly `E = V + sin²(K/2)/V`. So `c² = 1/2` for every `V`. Opposite coins have `E = V + cos²(K/2)/V`, which is inverted at rest. Without exclusion, the pairs that can reach coincidence have `c² = 3/2` instead.
- **T2: exclusion halves the step along the bond.** At strong binding the pair moves by two single steps. The part of its generator that keeps the bond `e_a` is exactly `5/2 − ½ cos K_a σ_a⊗σ_a − Σ_{b≠a} cos K_b σ_b⊗σ_b`. Along the bond the pair can advance only with the front record stepping first, because the rear record's first step would land on the front record's site. So along its bond a pair has `c² = ½⟨σ_a⊗σ_a⟩`; across it, `⟨σ_b⊗σ_b⟩`.
- **T3: no possibility shift gives a bound pair the walker's speed in every direction.** Consider every possibility shift covariant under the bond's rotations and the records' exchange (five real numbers). On every rest level of the strongly bound pairs, the weight matrices along the three axes sum to at most `3/2`, against 3 for a free record. So no strongly bound pair has weight one along all three axes. Fermion pairs whose coins lie on a zero-spin ray `cos θ S + e^{iφ} sin θ t_a` never roll. Along their bond they have weight `−1/2` for every `θ` and `φ`; across it, `1 − 2 cos²θ`.
- **T4: the controls.**
  - A free record has 3.
  - Without exclusion the along-bond term is not halved.
  - Contact pairs (block 115), possible only when two records may share a site, sum to at most 1.
  - A neighbour term timed like the hops scales like them.

In plain terms: records that can't share a site can still stick together as neighbours if their possibilities shift when they meet. But a stuck pair doesn't move like a single record. On a line its speed squared is exactly half a record's, however strong the sticking, because the back record can never step first. In space the way it moves depends on which way its bond points and on its coins, and no neighbour shift of possibilities gives it a single record's speed in every direction. If, as block 54's conditional ray model would have it, a body's fall follows these numbers, then tightly bound groups under one record per site don't fall like single records.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, one record per site, the neighbour possibility shift and any timing of it are supplied clauses. Nothing is adopted.
- **Two records** (blocks 54 and 78 as landed).
  - `H = Σ_a σ_a S_a` on `ℤ³`, with `S_a = (T_a − T_a⁻¹)/(2i)`. On the line, the walker is block 115's `σ_z D`: block 54's walk on one axis, up to a turn of the coin.
  - The pair states are antisymmetric or symmetric. One record per site removes coincidence.
  - In the relative coordinate `r = x₁ − x₂` at total wave vector `K`, `⟨r|H₂|r + e_a⟩ = (σ_a⊗1 e^{iK_a/2} − 1⊗σ_a e^{−iK_a/2})/(2i)` and `⟨r|H₂|r − e_a⟩ = (−σ_a⊗1 e^{−iK_a/2} + 1⊗σ_a e^{iK_a/2})/(2i)`, record 1's coin first.
- **The neighbour possibility shift.** `V = g Σ_{r = ±e_a} |r⟩⟨r| ⊗ M(r)`, with `M(r)` a hermitian form on the two coins.
  - Exchange: `M(−r) = SWAP M(r) SWAP`.
  - Covariance: `M(Rr) = U_R M(r) U_R†` under the 24 proper rotations, with the coins turned as spinors.
  - Strong binding: `|g|` large. `g μ₀` is an isolated value of `g M` on the bond, and the bound coins span its eigenspace.
- **The speed squared and the weight matrix.** For a bound level `E(K)`, `c²` along a direction is the second derivative of `E²/2` there at rest. On a level degenerate at rest, the weight matrix `W(n)` is the `K²` form of `E²/2` on the level, from second-order perturbation within it.
- **The fall, conditionally.** Block 115 (open) records that, under block 54's conditional ray model, a pair at rest whose binding term is timed by the rates would accelerate as `−g w² Hess(E²/2) ĝ`. This note makes no fall claim of its own.
- **Comparators, named only:** the strong-coupling expansion of bound pairs on a lattice.

## Theorem T1 — the line, exact

*Statement.* On `ℤ` with walkers `σ_z D`, one record per site, and either exchange sign, let `V ≠ 0` act when the records are adjacent (the coin-blind term, or any term keeping each record's `σ_z`).
- **Equal coins.** For `|sin(K/2)| < |V|` the pair has the bound level `E = V + sin²(K/2)/V` exactly, with wave `(sin(K/2)/V)^{r−1}` at separation `r ≥ 1`. So `E² = V² + 2 sin²(K/2) + sin⁴(K/2)/V²`, and `c² = 1/2` for every `V`.
- **Opposite coins.** For `|cos(K/2)| < |V|`, `E = V + cos²(K/2)/V` exactly, and `c² = −1/2 − 1/(2V²)`: inverted.
- **Without exclusion** (control), equal-coin pairs whose wave is even in `r` reach coincidence. Their level is `E = V + 3 sin²(K/2)/V + O(sin⁴(K/2))`, so `c² = 3/2`, the value probes composite-bodies a3 found. The odd ones are unchanged.

*Proof.*
1. At total wave number `K`, equal coins give the relative generator `sin(K/2)(φ(r+1) + φ(r−1))`. Opposite coins give `−i cos(K/2) φ(r+1) + i cos(K/2) φ(r−1)`, and `φ(r) = i^r χ(r)` turns this into `cos(K/2)(χ(r+1) + χ(r−1))`.
2. Under one record per site `φ(0) = 0`. For either exchange sign the pair lives on the half-line `r ≥ 1`; the other half is its exchange image. `V` acts at `r = 1`.
3. With `φ(r) = z^{r−1}`:
   - at `r ≥ 2`, `E = b(z + 1/z)`;
   - at `r = 1`, `E = bz + V`.

   So `z = b/V` and `E = V + b²/V`. The wave is normalizable while `|z| < 1`.
4. `c²` follows from the series in `K`.
5. Without exclusion the even channel has `φ(0) = x` with `Ex = 2b`. This adds `2b²/V` at order `b²`.

∎

*Checked (B1).* The two relative generators; the gauge; the half-line equations; both `c²` exactly; the series of the even channel without exclusion.

## Theorem T2 — the same-bond law

*Statement.* On `ℤ³` at strong binding, the bound pairs' generator is `E = g μ₀ + Λ/(g μ₀) + O(g⁻³)`. Here `Λ = P H₂ Q H₂ P`, where:
- `P` projects onto the bound coins at the six bond positions;
- `Q` projects onto the positions that are neither bond positions nor, under one record per site, coincidence.

For any coins, the part of `Λ` that keeps the bond `e_a` is

`Λ_aa = 5/2 − ½ cos K_a σ_a⊗σ_a − Σ_{b≠a} cos K_b σ_b⊗σ_b`,

and no two-step path joins `e_a` to `−e_a`. On the line the same construction gives `½ − ½ cos K σ_z⊗σ_z`, which is T1's energy exactly.

So a pair that keeps its bond has `c² = ½⟨σ_a⊗σ_a⟩` along the bond and `⟨σ_b⊗σ_b⟩` across it. Exclusion halves the along-bond term. The pair can advance along its bond only with the front record stepping first, because the rear record's first step would land on the front record's site.

*Proof.*
1. Second-order perturbation within the bound set.
2. Every bond position has an odd coordinate sum, and each step changes the sum by one. So no path of odd length returns, and the next correction is `O(g⁻³)`.
3. From `e_a` one step reaches `e_a ± e_b` (`b ≠ a`), `2e_a`, and coincidence, which is excluded.
4. Each reachable position collects the two records' steps into `A = (σ_b⊗1 e^{±iK_b/2} − 1⊗σ_b e^{∓iK_b/2})/(2i)`, and `A†A = (1 − cos K_b σ_b⊗σ_b)/2`.
5. Four positions across the bond and one along it give the law.

∎

*Checked (C1).* The law as a symbolic identity in `K` for each axis; the absent link between the bond's ends; the line; the parity of the bond positions.

## Theorem T3 — every covariant possibility shift

*Statement.*
- **(a) The shifts.** Take a possibility shift covariant under the bond's rotations: quarter-turns about the bond, and half-turns across it combined with the records' exchange. It is `μ_± Π_±` plus any hermitian form on the zero-spin plane `{S, t_a}`: five real numbers. Here:
  - `Π_±` projects onto the coin pairs with spin `±1` along the bond;
  - `S` is the singlet;
  - `t_a` is the triplet with zero spin along the bond.

  At strong binding the bound coins lie on a ray `ψ = cos θ S + e^{iφ} sin θ t_a`, on the spin `±1` plane, or on an accidental union of these.
- **(b) A ray.** The three bonds share the rest level `4 cos²θ + 1`, for every `θ`, `φ` and either exchange sign.
  - Fermion pairs never roll: `Λ = diag_a[5/2 + ½ cos K_a + (2 cos²θ − 1) Σ_{b≠a} cos K_b]`. Along its bond such a pair has weight `−1/2`; across it, `1 − 2 cos²θ`.
  - Boson pairs roll only at order `K²`.
- **(c) The axis sums.** On every rest level of every case, the first-order terms vanish. The sum over the three axes of the weight matrix is a single number, except on one merged level where it takes two:

  | ground space | exchange sign | sums on the rest levels |
  |---|---|---|
  | a ray | either | `(3 − 8 cos²θ)/2` |
  | the spin `±1` plane | fermions | `3/2`, `−1/2` |
  | the spin `±1` plane | bosons | `1/2` |
  | the zero-spin plane | either | `3/2`, `−5/2` |
  | coin-blind | fermions | `7/10`, `3/2`, `−1/2`, `−17/10` |
  | coin-blind | bosons | `3/2`, `1/2`, `−5/2` |
  | a ray with the spin `±1` plane | fermions | `(4 cos²θ + 3)/(2(4 cos²θ + 1))`, `−1/2`, `(3 + 12 cos²θ − 32 cos⁴θ)/(2(4 cos²θ + 1))` |
  | a ray with the spin `±1` plane | bosons | `1/2`, `(3 − 8 cos²θ)/2` |

  At the fermions' coincidence `cos²θ = 3/4` the merged level has `−3/4` and `−1/2`. At the bosons' coincidence `cos²θ = 1/4` it has `1/2`. None exceeds `3/2`, and the maximum is reached by pairs whose coins have zero spin along the bond.
- **(d) The conclusion.** No strongly bound pair has weight one along all three axes, which would need the sum 3 of a free record.

*Proof.*
- (a) Exact linear algebra on the sixteen real coefficients of a hermitian `4 × 4` form.
- (b)–(c) Exact symbolic computation of `Λ` restricted to each ground space, with `cos θ` and `e^{iφ}` as symbols, followed by second-order perturbation within each rest level.
- (d) Suppose a unit vector `v` in a rest level had `v†W(e_d)v = 1` for `d = 1, 2, 3`. Adding the three would give 3, but every level's sum is at most `3/2`.

∎

*Checked (D1).* The commutant and its five generators; each ground space; the fermions' diagonal form on a ray; every axis sum, with the bound `3/2` shown as a quotient of polynomials in `cos θ` with nonnegative coefficients.

## Theorem T4 — the controls

*Statement.*
- **A free record.** `d²(ε²/2)/dk_d² = cos 2k_d`: one along each axis at rest, sum 3 (block 106's fall weight).
- **Without exclusion.** The same-bond law is `3 − Σ_b cos K_b σ_b⊗σ_b`, with the along-bond term not halved, and the bond's two ends are joined through coincidence.
- **Contact pairs** (block 115; possible only when two records may share a site). The same law holds at coincidence, so their axis weights are the coin correlations:
  - `−1, −1, −1` for the singlet;
  - `−1` along `a` and `+1` across for `t_a`, with sum at most 1.

  These are block 115 T3's strong-binding values.
- **The timed term.** A neighbour term timed like the hops, by `√(w(x₁) w(x₂))`, picks up the hops' factor under a joint translation: block 115 T5's identity, for a bond.

*Proof.* Direct computation, as in T2. ∎

*Checked (E1).* All four items.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 115 (open) and probes composite-bodies a4: neighbour binding under one record per site, in three dimensions - the channel split and the limiting speeds"
source_of_blocker_text: block 115 (open); probes composite-bodies-rest-energy-without-a-larger-site-algebra a4
reachability_to_target: advances
artifact_role: no_go
next_trace_action: "moderate binding in three dimensions (the lattice integrals of the pair's resolvent); pushes that move a pair as a unit; massive pairs with the staggered rest energy"
conditional_surface_status: "exact on the line; leading order in 1/g in three dimensions; covariant shifts"
hypothetical_axiom_status: "nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.** Block 54: the walk. Block 78: one record per site is an interaction. Block 106: the fall weight `cos 2k`.
- **Opened, not landed.**
  - Block 115 (PR #9157): contact binding; one record per site removes it; the pair is anisotropic in three dimensions; the conditional fall.
  - Block 111 (PR #9151): block 95's pairs are unbound on `ℤ³`, and a binding clause is needed.
  - Block 141 (PR #9205): the same neighbour term does not restore the books.
- **Probes.**
  - Composite-bodies a3 (#8700, Grok-refereed) found the line's neighbour pairs without exclusion (`c² = 3/2` and `1/2`).
  - Composite-bodies a4 (#8733) listed neighbour binding under one record per site in three dimensions as open.
- **In the literature.** The strong-coupling expansion of bound pairs on a lattice, in which a pair moves by second-order steps; reference only.
- **New here:** T1, the exact law of the line under exclusion; T2, the same-bond law and its halving; T3, the covariant classification and the `3/2` bound; T4.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: how pairs bound by a neighbour possibility shift move under one record per site. The obligations are:
- (O1) the line (T1);
- (O2) the same-bond law (T2);
- (O3) every covariant shift and the bound (T3);
- (O4) the controls (T4).

T1–T4 discharge them. Open: moderate binding in three dimensions, the staggered mass, pushes, and more records.

## No-Go Discipline Gate

The note's negative sentence: in three dimensions, at strong binding, no rotation-covariant neighbour possibility shift gives a pair of records under one record per site weight one along all three axes; the axis sum is at most `3/2`.

### N1 — Routes by which the sentence could fail or mislead
1. *Moderate binding.* The bound is proved at leading order in `1/g`. The corrections are `O(g⁻²)` and are not computed.
2. *Pushes.* A correlated hop that moves the pair as a unit along its bond would add a first-order step, which could restore the missing one. It is not a possibility shift and is not treated.
3. *Massive pairs.* The staggered rest energy is not treated.
4. *Non-covariant shifts and larger groups* are not treated.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, exclusion and term.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 78 (landed) | the walk; exclusion | yes (restated) |
| block 106 (landed) | the free record's fall weight | control only |
| block 115 (open) | contact pairs; the conditional fall | comparison only |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no covariant neighbour shift gives a strongly bound pair weight one along all three axes" | executed: the line exactly; the same-bond law symbolically | executed: every bond and intermediate position; the parity | executed: the commutant and every ground space, symbolic in the mixing and phase | executed: every rest level's weight matrices and their axis sums; the controls | two records; leading order in `1/g` |

### N6 — Partial-closure paths and primitive scan
No approved primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A weakly bound pair is large and slow and may move like one body at the walker's speed."
  - *Reply:* That regime is not treated. At strong binding the pair's internal motion is at the lattice's own scale, and T3 says what it does. On the line T1 holds for every binding.

### N8 — Cross-cycle echo
- Block 115: contact pairs are anisotropic, and one record per site forbids them.
- Block 141: the same neighbour term keeps no books.
- This note: the same term binds, but its pairs do not move like records.

## Falsifiers

- A covariant possibility shift whose strongly bound pairs have a rest level with an axis sum above `3/2`.
- On the line, under one record per site, an equal-coin bound pair with `E ≠ V + sin²(K/2)/V`.

## Boundaries and non-claims

- Two records. Exact on the line; at leading order in the binding in three dimensions; covariant shifts only.
- The fall is not claimed. It enters only through block 115's conditional statement.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 78 and 106, restated. Block 115, restated.
- Named standard imports, at definition level:
  - exact symbolic arithmetic;
  - second-order perturbation theory within a degenerate level;
  - the spinor turns of the coin matrices.

## Review record

- **Who and when.** Supervisor-run block, the ninetieth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check found block 115, probes composite-bodies a3 and a4 (a4 names this question as open), and block 141.
- **Checks during the work.**
  - A numerical exploration, outside the runner, diagonalized the relative generator at `g = 40` on an `11³` box. Finite differences of the lowest six levels reproduced T3's weights for `t_a` pairs: `−0.498, 0.995, 0.997` along an axis for fermions and `−0.498, 1.000, 1.000` for bosons.
  - The union of a ray with the spin `±1` plane first seemed to reduce to the two pure cases. Its ray and spin `±1` states couple at first order in `K`, and the runner includes that coupling.
  - At moderate binding the multiplets split at higher order. That is why T3 is stated through the axis sum, which does not depend on a basis within a level.
- **Independence.** Mutation census: five mutations in families B–E (two in D), each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_record_per_site_pairs_bound_as_neighbours_have_half_the_walkers_speed_squared_on_a_line_and_never_its_speed_in_every_direction_2026_09_25.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
