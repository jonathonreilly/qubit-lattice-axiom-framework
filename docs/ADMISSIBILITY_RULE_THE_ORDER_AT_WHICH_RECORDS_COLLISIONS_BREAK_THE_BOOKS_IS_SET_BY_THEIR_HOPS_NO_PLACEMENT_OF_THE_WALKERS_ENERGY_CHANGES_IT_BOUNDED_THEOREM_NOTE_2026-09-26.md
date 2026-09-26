---
claim_id: admissibility_rule_the_order_at_which_records_collisions_break_the_books_is_set_by_their_hops_no_placement_of_the_walkers_energy_changes_it_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk (h(k) = sum_a sigma_a sin k_a, energies +-eps(k)), blocks 135, 136 and 143 as landed (the energy placement, the momentum that keeps the books, and the band-diagonal of a placement change), with blocks 150 and 152 as landed (2026-09-26, with the owner's scoping): (T1) exact: for every finite-range placement of the walker's energy and every finite-range momentum placement with which the walker's bracket matches block 112's shift whenever one lapse is uniform, the momentum's total has, in each band b, the diagonal part E_b v_b (the band's energy times its velocity); for block 54's walk it is sin k_j cos k_j in both bands, the two-step momentum. (T2) so under one record per site, below pair energy sqrt(2)/2, the collision law of block 152 (third order in the offsets from the corners) holds for every such placement; no placement changes the order. (T3) exact, for walks of the form h = sum_a sigma_a f(k_a) with f an odd real trigonometric polynomial of degree R and one light cone (f vanishes only at 0 and pi, |f'(0)| = |f'(pi)| = 1): the band-diagonal momentum is f(k_j) f'(k_j), and near every corner it equals the offset through order N - 1 with N <= R + 2; for R = 1 or 2, f = +-sin k and N = 3; for odd R the bound is reached by one f up to sign (R = 3: f = sin k (1 + sin^2 k / 6), f f' = delta - (9/20) delta^5 + ...; R = 5: N = 7). (T4) so if records hop only between neighbouring sites, the hard core's collisions change the member's momentum only at third order in the offsets, whatever the placement (T1); for added finite-range interactions the same holds only under block 152 T4's conditions (same-corner channels, a uniformly regular finite-support T-matrix with a nonzero leading amplitude); only hops of range three or more could raise the order. The supervisor's own derivation (Claude Opus 5.5); not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_order_at_which_records_collisions_break_the_books_is_set_by_their_hops_no_placement_of_the_walkers_energy_changes_it_2026_09_26.py
---

# The order at which records' collisions break the books is set by their hops; no placement of the walker's energy changes it

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact symbol identities and exact kinematics, within the landed walk, energy placement and momentum; blocks 150 and 152 as landed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 135, 136 and 143 as landed on main (the walk, the energy placement, the momentum that keeps the books, and the band-diagonal of a placement change), with blocks 150 and 152 as landed; it reports what sets the order at which records' collisions break the books; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 152 (landed) found that under one record per site a collision changes the records' two-step momentum at third order in their offsets from the corners of the zone. That momentum is what the member's shift sees (block 136). A panel asked whether finite-range choices can raise the order. This note answers for the choices that remain: where the walker's energy is placed, and how far records hop.

- **T1: the placement does not matter at zero transfer.** Take any local placement of the walker's energy, and any local momentum with which the walker's bracket matches the member's whenever one lapse is uniform. The momentum's total is then fixed in each band: it is the band's energy times its velocity. For block 54's walk that is `sin k_j cos k_j`, the two-step momentum, in both bands.
- **T2: so no placement changes the order.** Block 152's collision law holds for every such placement: third order in the offsets.
- **T3: the hops set the order.** For walks `h = Σ_a σ_a f(k_a)` with one light cone and hops of range `R`, the momentum the member sees equals the offset through order `N − 1` near every corner, with `N ≤ R + 2`. Neighbour hops (`R = 1`, and also `R = 2`) force `f = ± sin` and `N = 3`. Range three reaches `N = 5` with one walk, `f = sin k (1 + sin²k/6)`; range five reaches `N = 7`.
- **T4: under neighbour hops the order is three.** If records move only between neighbouring sites, the hard core's collisions change the member's momentum only at third order, for every placement (T1). For added finite-range interactions the same holds under block 152 T4's conditions. Only longer hops could raise the order.

In plain terms: the order at which the books fail is not a matter of bookkeeping choices. It is fixed by how records move. A record moving one site at a time has a speed that bends away from the light speed at third order in its momentum. Collisions conserve momentum on the lattice, but that bend makes the member's momentum drift at the same order. Records that could jump three sites at once could straighten the bend to fifth order.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its placements and one record per site are supplied clauses. Nothing is adopted.
- **The walk** (block 54 as landed). `H` has symbol `h(k) = Σ_a σ_a sin k_a`, with energies `±ε(k)`, `ε² = Σ_a sin²k_a`. For a family `A_x = T_x A_0 T_x^†`, the symbol `A(k + q, k)` is its matrix element between plane waves with transfer `q`. Its total `Σ_x A_x` has symbol `A(k, k)`.
- **Placements.** A placement of the energy is a finite-range family `e_x` with `Σ_x e_x = H`, so `e(k, k) = h(k)`. Block 135's placement `e′ = C₁C₂C₃e` is one. Its current `J` is defined by `i[H, e_x] = −Σ_j (J_{x,j} − J_{x−e_j,j})`. A momentum placement `P_{x,j}` lives on the bond `x → x + e_j`. Block 136's `P^B` is the one that keeps the books with `e′`.
- **The match with a uniform lapse** (block 150 T5(a), landed). With lapses `N`, `M` and block 112's shift `ξ_j = (K/4α)(N_{x+e_j}M_x − N_xM_{x+e_j})`, the walker's bracket matches the member's walker part when `N` is uniform, iff `K/4α = 1`. Here that match is required of the placement pair.
- **Velocity.** The velocity of band `b` is the band-diagonal of the number current's total, the current of the placement `Π_x`. In the symbol convention used here it is `−∂_jE_b` (runner B1).
- **Corners and offsets.** Block 152's: corners `A ∈ {0, π}^d`, offsets `δ = k − A`.
- **Standard imports, named at definition level.**
  - The first-order change of a simple eigenvalue is the diagonal element of the derivative (Hellmann and Feynman).
  - The matrix of powers of distinct numbers is invertible (Vandermonde).
  - Exact rational and symbolic arithmetic.

## Theorem T1 — the placement does not matter at zero transfer

*Statement.* Let `e_x` be any finite-range placement of the walker's energy, with current `J`. Let `P` be any finite-range momentum placement with which the walker's bracket matches block 112's shift whenever one lapse is uniform. Then:
- (a) `P(k, k) = J(k, k)`: the totals agree;
- (b) `J_j(k, k) = −(∂_jh · h + [h, ∂_{q_j}e(k + q, k)|_{q=0}])`, in the sign convention where the velocity's band-diagonal is `−∂_jE_b`;
- (c) so in each band `b` the diagonal part of `Σ_x P_{x,j}` is `E_b` times the band's velocity, `−E_b∂_jE_b` in this convention. For block 54's walk it is `−sin k_j cos k_j` in both bands, whatever the placement: the two-step momentum, oriented as the velocity.

*Proof.*
- (a) With `N` uniform, `i[H, E(M)] = Σ_x M_x i[H, e_x] = Σ_{x,j}(M_{x+e_j} − M_x)J_{x,j}` by the continuity equation and summation by parts. The member's side at `K/4α = 1` is `Σ_{x,j}(M_{x+e_j} − M_x)P_{x,j}`. Matching for every `M` makes `J − P` a family with zero divergence: `Σ_j(1 − e^{−iq_j})(J_j − P_j)(k + q, k) = 0` for every `q`. Its first order in `q` gives `(J_j − P_j)(k, k) = 0` for each `j`.
- (b) The continuity equation in symbols is `i(h(k + q)e(k + q, k) − e(k + q, k)h(k)) = −Σ_j(1 − e^{−iq_j})J_j(k + q, k)`. Its first order in `q_j`, with `e(k, k) = h(k)`, is (b).
- (c) In a band eigenvector `u_b(k)`, `⟨u_b|∂_jh · h|u_b⟩ = E_b⟨u_b|∂_jh|u_b⟩ = E_b∂_jE_b`, by the first-order eigenvalue rule. The commutator has zero diagonal, as in block 143 T2. The same computation for the number density gives the velocity's band-diagonal as `−∂_jE_b`. For block 54's walk `E_b² = ε²`, so `E_b∂_jE_b = ½∂_jε² = sin k_j cos k_j`.
- Runner B1–B3 check (b) and (c) symbolically for the symmetric placement `½(Π_xH + HΠ_x)`, for a placement that adds the divergence of a hermitian family to it, and for the number density. ∎

## Theorem T2 — so no placement changes the order

*Statement.* Under one record per site, take two records in the upper band with pair energy below `√2/2`. For every placement pair of T1, a collision changes the pair's total momentum, the sum of the two records' band-diagonals, exactly as block 152 finds for `P^B`: at third order in the offsets, `−(2/3)Δ(Σδ³) + O(δ⁵)`.

*Proof.* Below pair energy `√2/2` only the band pair `(+, +)` is open (block 152 T1(d)). On states within one band pair, a one-body operator's band-off-diagonal parts have zero expectation, and its band-diagonal is fixed by T1. So the asymptotic momentum of a pair is `g = Σ sin k cos k` for every such placement, and block 152 T1–T3 apply unchanged. ∎

## Theorem T3 — the hops set the order

*Statement.* Take `h = Σ_a σ_a f(k_a)` with `f` an odd real trigonometric polynomial of degree `R ≥ 1` and one light cone: `f` vanishes only at `0` and `π`, and `|f′(0)| = |f′(π)| = 1`. Then:
- (a) `h² = ε²·1` with `ε² = Σ_a f(k_a)²`, and T1's band-diagonal momentum is `f(k_j)f′(k_j)` in both bands. Near a corner it is odd in the offset, with linear coefficient `1`.
- (b) Let `N` be the smallest order at which `f f′(A + δ) − δ` has a nonzero coefficient at some corner `A ∈ {0, π}`. Then `N ≤ R + 2`.
- (c) For `R = 1` and `R = 2`, `f = ± sin k` and `N = 3`.
- (d) For odd `R`, `N = R + 2` is reached, by one `f` up to sign. `R = 3`: `f = (9/8) sin k − (1/24) sin 3k = sin k(1 + sin²k/6)`, with `f f′ = δ − (9/20)δ⁵ + O(δ⁷)` at both corners and `|f′| ≤ 1`. `R = 5`: `f = (75/64) sin k − (25/384) sin 3k + (3/640) sin 5k`, with `N = 7`. For `R = 4` the best is `N = 5`.
- (e) With the corners' offset sums conserved (block 152 T1(b)), collisions whose records stay within `π/4` of corners change the momentum at order `N`. For the `R = 3` walk the fifth-order sum is not constant on the leading-order shell: along block 152's family it is `p⁵/16 + (5/2)p³x² + 5px⁴`.

*Proof.*
- (a) The `σ_a` anticommute, so `h² = Σ_a f(k_a)²`. T1(c) with `E_b = ±ε` gives `E_b∂_jE_b = ½∂_jε² = f(k_j)f′(k_j)`. Since `f` is odd and `2π`-periodic, `f(A + δ)` is odd in `δ` for `A ∈ {0, π}`, with slope `f′(A) = ±1`.
- (b) Split `f = o + e` into odd and even harmonics, so `f(π + δ) = −o(δ) + e(δ)`. The condition at both corners is `(o ± e)² = δ² + O(δ^{N+1})`. So `4oe = O(δ^{N+1})` and `o² + e² = δ² + O(δ^{N+1})`. One light cone gives `|o′(0) + e′(0)| = |−o′(0) + e′(0)| = 1`, so one of `o′(0)`, `e′(0)` vanishes.
  - If `o′(0) ≠ 0`, then `e = O(δ^N)` and `o = ±δ + O(δ^N)`. Write `o = Σ_{j<m} a_j sin((2j + 1)δ)`, with `2m − 1` its degree. The coefficient of `δ^{2l+1}` is `(−1)^l/(2l + 1)!` times `Σ_j b_jx_j^l`, with `b_j = a_j(2j + 1)` and `x_j = (2j + 1)²`. So `Σ_j b_j = ±1`, and `Σ_j b_jx_j^l = 0` for `1 ≤ l ≤ (N − 3)/2`. If `(N − 3)/2 ≥ m`, the equations for `l = 1, …, m` read `Σ_j (b_jx_j)x_j^{l−1} = 0`, with an invertible matrix of powers. So `b = 0`, a contradiction. Hence `N ≤ 2m + 1 ≤ R + 2`.
  - If `o′(0) = 0`, then `e′(0) = ±1` and `o = O(δ^N)`. If `o ≡ 0`, `f = e` vanishes at `π/2`, against one light cone. Otherwise `o`'s lowest power-series order is at most its degree, by the same invertibility. So `N ≤ R`.
- (c) `R = 1`: `f = a sin k` with `|a| = 1`. `R = 2`: `f = a sin k + b sin 2k`. One light cone forces `b = 0` when `a ≠ 0`; when `a = 0`, `f` vanishes at `π/2`. In both cases `f f′ = sin δ cos δ = δ − (2/3)δ³ + …`.
- (d) Runner D1 solves the power-series conditions exactly for `R = 1, …, 5`. The largest `N` is `3, 3, 5, 5, 7`. The solutions are the odd stencils above and, for even `R`, even-harmonic ones vanishing at `π/2`. For `R = 3`, `1 − f′² = (1 − c²)²(4 − c²)/4 ≥ 0` with `c = cos k` (runner E1).
- (e) Block 152 T1(b) uses only crystal momentum and the offsets' bound, not the form of `f`, and `f f′(A + δ) = δ + c_Aδ^N + …`. So the linear terms cancel, and the change is `Σ c_A Δ(δ^N)`. The family and two exact points are runner E2. ∎

## Theorem T4 — under neighbour hops the order is three

*Statement.* If records hop only between neighbouring sites, within walks of T3's form, then:
- the hard core's collisions change the member's momentum only at third order in the offsets, for every placement pair of T1 (T2);
- for added finite-range interactions the same holds under block 152 T4's conditions: same-corner channels, a uniformly regular finite-support T-matrix and a nonzero leading amplitude. Block 152 establishes no universal leading loss for arbitrary interactions, which may have threshold poles or scatter into other corners.

Raising the order needs hops of range three or more (T3(b), (d)). Block 112's shift lives on nearest-neighbour bonds, so the member would then have to pair with a momentum on longer bonds. That is not examined.

*Proof.* T3(c) gives `f = ± sin` for neighbour hops; T1, T2 and block 152 T4, with its conditions, do the rest. ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision-record addendum 43: can finite-range choices raise the order at which the records' books fail?"
source_of_blocker_text: the panel of 2026-09-26; block 152 (landed)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "walks outside T3's form (coin-mixing hops); a member that pairs on longer bonds; the walker's clock defect under placements (probes refill w); an other-family referee"
conditional_surface_status: "block 54's walk for T1-T2; walks of T3's form for T3-T4; blocks 150 and 152 as landed; added interactions under block 152 T4's conditions"
hypothetical_axiom_status: "the walk, its placements and one record per site are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54 (the walk).
  - Block 135 (the energy placement `e′`).
  - Block 136 (`P^B` keeps the books with `e′`).
  - Block 143 T2: a one-body placement change `i[h, f]` has zero band-diagonal. T1 uses it.
- **Blocks, as landed 2026-09-26 with the owner's scoping.** Block 150 T5(a) (the match with a uniform lapse); block 152 (the collision law, its channel closure T1(d), and T4, a conditional same-corner statement for interactions).
- **Probes.** Refill w asks how far a local placement pushes the walker's clock defect. That concerns the dependence on the lapses' wave numbers. T1 shows it cannot move the records' order, which is set at zero transfer.
- **In the literature.** The energy current of a band state is its energy times its group velocity; finite-difference stencils and their error orders. Reference only.
- **New here:** the reduction of every placement pair to the band's energy times velocity (T1(a)–(b)); the bound `N ≤ R + 2` for walks of T3's form and its attainment; the consequence for neighbour hops.
- **Provenance.** The supervisor's own derivation. No other model family has refereed it.

## Exact target and obligation graph

Target: whether finite-range choices can raise the order at which the records' books fail. The obligations are:
- (O1) placements at zero transfer (T1: proved here; runner B1–B3);
- (O2) the collision law for every placement (T2: from block 152, landed);
- (O3) the order against the hop range (T3: proved here; runner D1, D2, E1, E2);
- (O4) the neighbour-hop consequence (T4: from T1–T3 and block 152 T4).

The strongest cited input: block 152 T4, landed as a conditional statement.

## No-Go Discipline Gate

The note's negative sentences: no placement of the walker's energy changes the order; under neighbour hops the order is three.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A cleverer energy placement changes the momentum.* Its total's band-diagonal is the band's energy times velocity, for every placement (T1; runner B2). ATTEMPTED.
2. *The member pairs with a momentum other than the energy current.* The match with a uniform lapse makes the totals equal (T1(a)). ATTEMPTED.
3. *Band-off-diagonal parts of the placement matter in collisions.* Below pair energy `√2/2` only `(+, +)` is open, where they have zero expectation (T2). ATTEMPTED.
4. *Even harmonics at range two help.* One light cone forces `f = ± sin` (T3(c); runner D1). ATTEMPTED.
5. *Some walk of range `R` beats `R + 2`.* The matrix of powers forbids it (T3(b); runner D2). ATTEMPTED.
6. *The `R = 3` walk's fifth-order change cancels on the shell.* Its sum varies along an explicit family (T3(e); runner E2). ATTEMPTED.

Scope left open: walks outside T3's form; the member's pairing on longer bonds; interactions beyond leading order near one corner; the channel closure for walks other than block 54's.

### N2 — Wall-independence audit
No no-go wall of the repository is used. Block 143 T2 is an identity, used as landed.

### N3 — Hidden-wall scan
The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical". The match with a uniform lapse is stated as the requirement on placement pairs. No hidden condition was found.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 54 (landed) | the walk | yes (restated) |
| blocks 135, 136 (landed) | the placement and the momentum that keeps the books | context (T1 covers every placement) |
| block 143 T2 (landed) | zero band-diagonal of `i[h, f]` | yes (re-checked: runner B3) |
| block 150 T5(a) (landed) | the match with a uniform lapse | yes (restated as the requirement) |
| block 152 (landed) | the collision law, T1(d), T4 (conditional) | yes (T2, T4) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no placement changes the order; under neighbour hops it is three" | executed: the continuity symbol at first order | executed: the symmetric placement and one with an added divergence | executed: band-diagonals in both bands; the number current | executed: exact power-series solves for `R ≤ 5`; the power-matrix lemma for `m ≤ 6` | every placement by proof; walks of T3's form |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A placement is a free choice; choose one that repairs the records' books."
  - *Reply:* The books concern the total momentum at zero transfer. There every placement agrees with the band's energy times velocity (T1). A placement changes only terms that vanish with the transfer, or that mix the bands.

### N8 — Cross-cycle echo
- Block 143: nothing local keeps the books under one record per site.
- Block 152: third order.
- This note: third order is set by the hops, not by the placement.

## Falsifiers

- A finite-range placement pair meeting T1's requirement whose total momentum has a different band-diagonal.
- A walk of T3's form and range `R` with `N > R + 2`.
- A neighbour-hop walk of T3's form other than `f = ± sin`.

## Boundaries and non-claims

- Block 54's walk for T1–T2; walks of T3's form for T3–T4; blocks 150 and 152 as landed; added interactions only under block 152 T4's conditions.
- Coin-mixing hops, members pairing on longer bonds, and the channel closure for walks other than block 54's are not covered.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 135, 136 and 143 (landed), restated. Blocks 150 and 152 (landed), cited.
- Named standard imports, at definition level: the first-order eigenvalue rule (Hellmann and Feynman); the invertible matrix of powers (Vandermonde); exact rational and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, 2026-09-26, during the owner's 12-hour campaign of that day, after the panel of the same day.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5). Not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found block 143 T2 (used) and block 120 (a different question: which current can source the member). It found no attempt at the hop-range question.
- **Independence.** Mutation census: at least one mutation per science family (B, D, E), each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_order_at_which_records_collisions_break_the_books_is_set_by_their_hops_no_placement_of_the_walkers_energy_changes_it_2026_09_26.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
