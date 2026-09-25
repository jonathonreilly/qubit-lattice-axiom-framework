---
claim_id: admissibility_rule_the_two_wall_level_rule_holds_on_every_ring_whose_length_is_a_multiple_of_four_and_an_antipodal_wall_pair_costs_the_sea_exactly_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Positive unequal bond weights in the supplied one-axis equal-half-reversal pattern on even rings L>=4.
  Exact antipodal squared-level replacement and negative-level sum difference for every4-divisible L, including
  a separate doubled-edge L4 case. General real symmetric cyclic tridiagonal transfer identity with nonzero hops
  at M>=3 and an opposite-diagonal-defect formula at sublattice separation r. Balanced even/odd bond products give
  exactly two zero modes. At L=2 mod4 the upper band edge is absent, excluding the stated replacement; no shared
  level is asserted only for the executed L6/10 parameter pair. No arbitrary wall arrangement, many-record hard-core
  sea or domain-formation law.
upstream_dependencies:
- admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_of_lower_mass_lines_lower_still_three_crossing_walls_bind_exact_zero_modes_bounded_theorem_note_2026-09-22
- admissibility_rule_what_a_wall_in_the_alternation_costs_the_sea_charges_it_by_an_exact_level_rule_block_59s_collinear_coupling_rewards_it_domains_iff_alpha_large_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_the_two_wall_level_rule_holds_on_every_ring_whose_length_is_a_multiple_of_four_and_an_antipodal_wall_pair_costs_the_sea_exactly_2026_09_24.py
---

# The two-wall level rule holds on every ring whose length is a multiple of four, and an antipodal wall pair costs the sea exactly

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 87 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within block 87 as landed on main (the one-axis hop with alternating bond rates and two walls, and the sea's energy as the sum of negative levels); it reports the exact change of the levels on every ring whose length is a multiple of four, and the wall pair's cost to the sea; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 87, as landed, found an exact rule for how two walls in an alternating pattern of bond rates change the walker's levels, but only on rings of `4`, `8` and `12` sites at one alternation strength. It said that this "is not a rule for every even ring", and noted that the ring of `6` breaks it. This note proves the rule on every ring whose length is a multiple of four, for any positive unequal pair of bond weights, and finds exactly where it fails.

- **T1: the walls are two defects.**
  - The squared hop splits into two sublattice blocks with the same levels.
  - On one of them block 87's two walls are a raised and a lowered diagonal entry, half the ring apart, on an otherwise uniform chain.
- **T2: a closed form.**
  - A ring's characteristic polynomial is a trace of transfer matrices.
  - Two opposite defects at any separation give a closed formula in the standard trigonometric polynomials.
- **T3: the rule, everywhere it can hold.**
  - On every ring whose length is a multiple of four, the walls remove the two band-edge levels and add `0` and the bonds' mean square, twice each. Nothing else moves.
  - So an antipodal wall pair costs the sea exactly `max(t_s, t_w) − √((t_s² + t_w²)/2)`, which is positive. That is block 87's `(1 + δ) − √(1 + δ²)`, now on every such ring.
- **T4: zero modes, and where the rule fails.**
  - Exact zero modes exist iff the products of the even and the odd bonds agree, and then there are exactly two.
  - On rings of length `2 mod 4` one band edge is not a level at all, so the rule cannot hold. For the executed L6 and L10 examples no level is shared; this stronger property is not proved for all such rings.

In plain terms, when the bond rates alternate strong–weak and two domains meet at walls, the walls cost the sea of the walker's states a definite amount of energy. On every ring whose length is a multiple of four, the cost of a pair of walls on opposite sides of the ring is exactly the stronger bond minus the root-mean-square of the two. That is the exact version of block 87's number, which it could check only on three rings.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "No possibility is privileged." "No site is privileged." The alternation and its walls are supplied patterns of bond rates, not consequences of the axioms.
  - "Admissibility is not a dynamics axiom." The hop, the bond rates and the sea are supplied. Nothing is adopted.
- **The operator** (block 87 as landed). `h = (1/2i)(tT − Tᵀt)` on an even ring of L>=4 sites, with `T[x, x+1] = 1` and `t = diag(t_x)`: the bond from `x` to `x + 1` carries `t_x`.
- **Alternation with two walls** (block 87's equal-half reversal).
  - `t_x = t_s` where `s_x(−1)^x = +1` and `t_x = t_w` otherwise, with `s_x = +1` for `x < L/2` and `−1` beyond. Here `t_s ≠ t_w` are both positive.
  - `t = 1 ± δ` is block 87's case, and `t = e^{±δ}` is block 89's log parametrisation.
  - A wall is a site where two consecutive bonds are equal: strong–strong or weak–weak.
- **The sea** (block 87 as landed): the sum of the negative levels of `h`.
- **The standard polynomials.** `T_k` and `U_k` are the Chebyshev polynomials: `T_k(cos θ) = cos kθ` and `U_k(cos θ) = sin((k + 1)θ)/sin θ`, with `U_{−1} = 0`.
- **Comparators, named only:** domain walls with bound zero modes in dimerised chains (Su, Schrieffer and Heeger; Jackiw and Rebbi); the Peierls instability.

## Theorem T1 — the walls are two opposite diagonal defects

*Statement.*
- (a) Ordering the sites even first, `h = [[0, A], [A†, 0]]`. So `h² = AA† ⊕ A†A`, and the two blocks have the same characteristic polynomial.
- (b) For `4 | L`, the even block with block 87's walls is the uniform chain with diagonal `D = (t_s² + t_w²)/4` and hop `−C`, `C = t_st_w/4`, plus `+η` at the site0 (strong-strong when t_s>t_w) and `−η` at the siteL/2 (weak-weak when t_s>t_w), with `η = (t_s² − t_w²)/4`. The two defects are half the sublattice ring apart.

*Proof.*
- (a) `h` joins only opposite parities. For square `A`, `det(λ − AA†) = det(λ − A†A)`: this holds for invertible `A` by conjugation, and extends to every `A` as a polynomial identity.
- (b) Read off `h²`. Away from the walls every diagonal pairs one strong and one weak bond, and so does every hop. At the walls the diagonal pairs two equal bonds.

∎

*Checked (B1).*
- The split and the equal characteristic polynomials on rings `L = 4, 8, 12, 16`.
- The defect form, symbolically in `t_s` and `t_w`, on rings `L = 8, …, 24`.

## Theorem T2 — the ring lemma and the closed form

*Statement.*
- (a) For a ring of `M ≥ 3` sites with real diagonal a_i and nonzero real symmetric hops b_i, `det(λ − J) = (Π b_i)(tr(T_{M−1}⋯T_0) − 2)`, with transfer matrices `T_i = [[(λ − a_i)/b_i, −b_{i−1}/b_i], [1, 0]]`.
- (b) With the uniform chain written as `B = [[2z, −1], [1, 0]]`, `z = (D − λ)/2C`, one has `(B^k)₁₁ = U_k` and `tr B^k = 2T_k`.
- (c) Two opposite defects `±η = ±εC`, r sublattice sites apart on a ring of M (equivalently2r original-lattice sites), give the characteristic function `2(T_M − 1) − ε²U_{r−1}U_{M−r−1}`.

*Proof.*
- (a) Expand the determinant over permutations. On a ring only matchings with fixed points, and the two full rotations, contribute. The transfer product counts the matchings, and the rotations add `−2Π b`.
- (b) Induction from `U_{k+1} = 2zU_k − U_{k−1}`.
- (c) By cyclicity the two linear terms cancel, and the quadratic term is `−ε²(B^{r−1})₁₁(B^{M−r−1})₁₁`.

∎

*Checked (C1).*
- (a) exactly on random rational rings of `3` to `7` sites.
- (b) for `k ≤ 12`.
- (c) symbolically, for every `M = 3, …, 12` and every `r`.

## Theorem T3 — the four-level rule on every ring with 4 | L, and the wall pair's cost

*Statement.* For every ring with `4 | L` and every `t_s ≠ t_w`:

`det(λ − J_walls)(λ − (t_s − t_w)²/4)(λ − (t_s + t_w)²/4) = det(λ − J₀) · λ(λ − (t_s² + t_w²)/2)`.

So the walls replace the two band-edge levels `(t_s − t_w)²/4` and `(t_s + t_w)²/4` of the squared spectrum by `0` and `(t_s² + t_w²)/2`, each twice in `h²`, and nothing else moves. Consequently:
- the antipodal wall pair raises the sea's energy by exactly `max(t_s, t_w) − √((t_s² + t_w²)/2) > 0`, which is1+|delta|-sqrt(1+delta^2) at t=1 plus/minus delta, 0<|delta|<1 (the displayed original1+delta form assumes delta>0);
- for `t = e^{±δ}` the rule reads absolute sinh(delta), cosh(delta) ->0,sqrt(cosh(2delta)) for the nonnegative energy magnitudes; the squared levels are their squares.

*Proof.*
- First take L>=8. With `M = L/2` even, `T_{2n} − 1 = 2(z² − 1)U_{n−1}²`. So at the antipodal separation `r = n` the characteristic function of T2(c) is `U_{n−1}²(4(z² − 1) − ε²)`, against `U_{n−1}² · 4(z² − 1)` without walls.
- The ratio is `((D − λ)² − 4C² − η²)/((D − λ)² − 4C²)`.
- `D² − 4C² = η²`, `D − 2C = (t_s − t_w)²/4` and `D + 2C = (t_s + t_w)²/4` give the identity.
- For L=4 the sublattice ring has two sites, so the two directed nearest links add to off-diagonal -2C. Its wall-free determinant is(lambda-D)^2-4C^2 and the wall determinant is(lambda-D)^2-4C^2-eta^2. These give the same identity directly, without applying the M>=3 lemma.
- The degenerate levels sit in the common factor `U_{n−1}²`, so they stay.
- The sea's energy changes by the removed negative levels `−|t_s − t_w|/2` and `−(t_s + t_w)/2`, against the added `0` and `−√((t_s² + t_w²)/2)`.

∎

*Checked (D1).*
- The identity exactly on every ring `L = 4, 8, …, 24` at `(t_s, t_w) = (13/10, 7/10)` and `(7/4, 2/5)`.
- `D² − 4C² = η²` symbolically.
- The log form and the cost.

## Theorem T4 — exact zero modes, and where the rule fails

*Statement.*
- (a) On any even ring, `det A = (Π_{x even} t_x − Π_{x odd} t_x)/(2i)^M`, and `A` has a kernel of dimension at most one. So `h` has exact zero modes iff the two bond products agree, and then exactly two. Block 87's antipodal walls balance the products.
- (b) On rings of length `2 mod 4` the band edge `(t_s + t_w)²/4` is not a level of the wall-free ring, and the general replacement cannot apply. Absence of every common level is checked only at L6,10 and(t_s,t_w)=(13/10,7/10). So the four-level rule cannot hold there.

*Proof.*
- (a) A is cyclic bidiagonal with nonzero bonds; expanding its determinant gives exactly the two parity products. Equivalently, the zero equation t_x psi_(x+1)=t_(x-1) psi_(x-1) determines each parity subsequence from one seed. Closure is exactly equality of the parity products, giving one independent seed on each parity and hence two zero vectors.
- (b) With `M` odd, `k = π` is not a momentum of the sublattice ring.

∎

*Checked (E1).*
- The determinant on random rational rings of `6` to `12` sites.
- The balance and a zero level for block 87's walls on rings of `8`, `12` and `16`.
- The rings of `6` and `10`: no common factor, and the band edge absent.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 87 as landed: the level rule is proved only on rings of 4, 8 and 12 at d = 3/10; 'this is not a rule for every even ring'; no universal wall tension"
source_of_blocker_text: block 87 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the sea's energy of walls at every separation in closed form (the separation dependence is executed only in floating point in the attempt); two and three dimensions; the wall cost against block 87's law cost"
conditional_surface_status: "T1-T3 on every ring with 4 | L; T4 on every even ring; one axis; the alternation, the walls and the sea supplied"
hypothetical_axiom_status: "the alternation and its walls are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 87: the one-axis hop with walls, and the level rule on three rings at `δ = 3/10`.
  - Block 89: the log parametrisation.
  - Block 86: the defects of the alternation.
- **The probes attempt.** `the-two-wall-level-rule-on-every-ring` a2 (Claude Opus 5.5, issue #8763) found T1–T4. A Grok referee confirmed it (#9058).
  - The attempt's floating-point sea energies of wall pairs at other separations are not used.
- **In the literature.**
  - Dimerised chains with domain walls (Su, Schrieffer and Heeger) and bound zero modes (Jackiw and Rebbi).
  - Chebyshev polynomials, Sylvester's `AA†`/`A†A` identity, and the Weinstein–Aronszajn determinant formula.

  All reference only.
- **New here:**
  - an independent exact runner;
  - the results placed against block 87 as landed, which proves its rule on every ring with `4 | L` and explains its `L = 6` exception.

## Exact target and obligation graph

Target: block 87's two-wall level rule on every ring, and the wall pair's cost to the sea. The obligations are:
- (O1) the defect form (T1);
- (O2) a closed characteristic function (T2);
- (O3) the rule and the cost (T3);
- (O4) zero modes and the failure (T4).

T1–T4 discharge them. Open: other separations' costs in closed form, and higher dimensions.

## No-Go Discipline Gate

The note's negative sentence: on rings of length `2 mod 4` the four-level rule cannot hold.

### N1 — Routes by which the sentence could fail or mislead
1. *Other wall placements.* On rings of length `2 mod 4` block 87's two walls are both strong–strong. A different pair can be placed, and its levels follow T2 and T4, not the four-level rule.
2. *Other separations.* T2(c) gives the characteristic function at every separation. Only the antipodal pair has the four-level form.
3. *Domain formation.* The sea's cost of walls is one side of a domain-formation balance. Block 87's law cost is the other, and no criterion is claimed here.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied alternation, walls and sea.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks86 and87 (landed) | hop, wall pattern and finite predecessor result | yes (restated); block89 is parametrization context only |
| probes (#8763; Grok-refereed #9058) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the four-level rule on every ring with `4 | L`; the antipodal wall pair's exact cost; zero modes iff balanced; failure for `2 mod 4`" | executed: the sublattice blocks and defects, symbolically | executed: the ring lemma on random rings; the transfer powers | executed: the closed form for every `M ≤ 12` and every separation | executed: the identity on rings to `24`; the determinant; the `2 mod 4` rings | every ring with `4 | L` by proof; one axis; supplied patterns |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 87 already had the rule."
  - *Reply:* On three rings at one strength. Its landed text says the rule is not established for every even ring.
  - This note proves it for every ring with `4 | L` and every pair of bonds, and shows why the other rings fail.

### N8 — Cross-cycle echo
- Block 86 found the alternation's defects.
- Block 87 found the level rule on three rings.
- This note proves it wherever it can hold, and gives the exact cost.

## Falsifiers

- A ring with `4 | L` and bonds `t_s ≠ t_w` on which the identity of T3 fails.
- An even ring with balanced bond products and no zero mode.
- A ring of length2 mod4 in the stated positive unequal uniform alternation whose upper band edge is present; or failure of the explicitly scoped L6/10 no-common-level controls.

## Boundaries and non-claims

- The alternation, the walls and the sea are supplied.
- One axis only.
- No domain-formation criterion is claimed.
- No gravitational claim is made.

## Imports

- [Supplied source, block 86](ADMISSIBILITY_RULE_DEFECTS_OF_THE_ALTERNATION_ARE_SEPARABLE_WALLS_CARRY_SHEETS_OF_LOWER_MASS_LINES_LOWER_STILL_AND_THREE_CROSSING_WALLS_BIND_EXACT_ZERO_MODES_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 87](ADMISSIBILITY_RULE_WHAT_A_WALL_IN_THE_ALTERNATION_COSTS_THE_SEA_CHARGES_IT_BY_AN_EXACT_LEVEL_RULE_BLOCK_59S_COLLINEAR_COUPLING_REWARDS_IT_DOMAINS_IFF_ALPHA_LARGE_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 86, 87 and 89, restated.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the Chebyshev polynomials and their product identities;
  - Sylvester's determinant identity for `AA†` and `A†A`;
  - the Leibniz expansion of a determinant;
  - exact rational and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the eightieth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (#8763). A Grok referee confirmed them (#9058).
  - The supervisor re-checked them with its own runner, in block 87's own convention for `h`. There the walls sit on the even sublattice; the attempt used the reversed shift.
- **Before writing.** Main was re-fetched, and blocks 86, 87 and 89 were read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_two_wall_level_rule_holds_on_every_ring_whose_length_is_a_multiple_of_four_and_an_antipodal_wall_pair_costs_the_sea_exactly_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
