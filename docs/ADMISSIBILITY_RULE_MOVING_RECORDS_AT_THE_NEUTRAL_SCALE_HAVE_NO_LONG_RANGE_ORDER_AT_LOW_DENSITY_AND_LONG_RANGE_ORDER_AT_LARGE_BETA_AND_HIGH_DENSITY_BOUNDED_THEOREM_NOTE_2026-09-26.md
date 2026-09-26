---
claim_id: admissibility_rule_moving_records_at_the_neutral_scale_have_no_long_range_order_at_low_density_and_long_range_order_at_large_beta_and_high_density_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 126's static vacancy law as landed (block 39 T5's law with vacancies: each site empty or holding a content s = +-1, empty weight 1 and content weight z, bond kernel 1 with an empty end and c e^(beta s s') between contents, on even periodic cubic tori), at block 40's neutral scale c0 = 1/cosh(beta) for the two-valued menu: (T0) exact: the kernel is 1 + tanh(beta) sigma sigma' with sigma in {-1, 0, 1}; (T1) exact: for every beta and every z < 1/320, sum_x <sigma_0 sigma_x> <= p + 6p^2/(1 - 5p) with p = 64z on every even torus, so there is no long-range order and the structure factor is bounded uniformly; (T2) the law is reflection positive through planes of sites, and given the chessboard estimate for such laws and a torus form of the separation lemma for *-connected sets (both named standard results, stated as premises), if the explicit pattern polynomial P(z^(-1/8), ((1 - t)/(1 + t))^(1/4)) is at most 1/2704 then <sigma_0 sigma_x> >= 1 - 2[2 eps + 2 eps/(1 - 676 eps)^2] - o(1) for every x; z >= 10^40 with 1 - tanh(beta) <= 10^(-8) gives long-range order with <sigma_0 sigma_x> >= 0.998 - o(1). So block 126's open neutral-scale question has two answers for the two-valued menu: no long-range order at low density at any beta, and long-range order at large beta and high density. A harvest of probe #9260 (Claude Opus 5.5, the supervisor's own model family), line-checked by the supervisor, with an independent exact runner. Not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_moving_records_at_the_neutral_scale_have_no_long_range_order_at_low_density_and_long_range_order_at_large_beta_and_high_density_2026_09_26.py
---

# Moving records at the neutral scale have no long-range order at low density, and long-range order at large β and high density

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (T0 and T1 exact; T2 exact given two named standard results; within block 126's static vacancy law, two-valued menu, at block 40's neutral scale; a harvest of probe #9260, line-checked by the supervisor; not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 39, 40 and 126 as landed on main (the law with vacancies, its neutral scale and the static vacancy law's open question); it reports whether that law has long-range order at the neutral scale for the two-valued menu; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 126, as landed, gave an infrared bound for records that move with vacancies above the neutral scale, and left the neutral scale itself open: it claims no disorder there. Probe #9260 answered the question for the two-valued menu. The supervisor checked every step and reran it independently.

- **T0: the neutral kernel.** At `c₀ = 1/cosh β` the bond kernel is `1 + tσσ′`, with `t = tanh β` and `σ = ns ∈ {−1, 0, 1}`. An occupied neighbour, averaged over its two contents, weighs `1`, the same as an empty one.
- **T1: no long-range order at low density, at every β.** For `z < 1/320`, `Σ_x⟨σ₀σ_x⟩ ≤ p + 6p²/(1 − 5p)`, with `p = 64z`, on every even torus. Contents correlate only inside occupied clusters, and the occupied set is dominated by independent site occupation at density `p`.
- **T2: long-range order at large β and high density.**
  - The law is reflection positive through planes of sites.
  - Take the chessboard estimate for such laws and a torus separation lemma for ⋆-connected sets as premises.
  - Then, if the pattern polynomial `P(A, U)` over the 6559 bad `2 × 2 × 2` patterns is at most `1/2704`, `⟨σ₀σ_x⟩ ≥ 1 − 2[2ε + 2ε/(1 − 676ε)²] − o(1)` for every `x`, with `A = z^{−1/8}`, `U = ((1 − t)/(1 + t))^{1/4}` and `ε = P(A, U)`.
  - For example, `z ≥ 10⁴⁰` with `1 − tanh β ≤ 10⁻⁸` gives `⟨σ₀σ_x⟩ ≥ 0.998 − o(1)`.

In plain terms: at the neutral scale an occupied neighbour counts, on average, exactly as much as an empty site. When records are scarce, they sit in small islands and their orientations cannot line up across the lattice. When records are dense and the binding is strong, almost every small cube is filled with records all pointing one way, and a flipped region would cost too much at its boundary. So the records line up across the whole lattice. Both happen at the same neutral scale, at different densities.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The law with vacancies, its weights and the menu are supplied clauses. Nothing is adopted.
- **The law with vacancies** (blocks 39 T5 and 126, as landed). Each site of an even torus `T_L = (ℤ/Lℤ)³` is empty (`∅`) or holds a content `s ∈ {+1, −1}`. The weight is `Π_x w(u_x) Π_bonds B(u_x, u_y)`, with `w(∅) = 1`, `w(s) = z`, `B(∅, ·) = B(·, ∅) = 1` and `B(s, s′) = c e^{βss′}`. The law has one bond per site and direction; on a side of two the pair is joined twice.
- **The neutral scale** (block 40, carried to the two-valued menu by block 126): `c₀(β) = 1/cosh β`.
- **Fields and the diagnostic** (block 126 as landed). `σ_x = n_xs_x`, `σ̂(k) = N^{−1/2}Σ_xe^{ik·x}σ_x`, and `M_N² = N⁻¹⟨|σ̂(0)|²⟩ = N⁻¹Σ_x⟨σ₀σ_x⟩` on a torus of `N` sites. Long-range order of the contents is block 126 T4's torus diagnostic: `liminf M_N² > 0` along even cubic volumes.
- **Standard imports, named at definition level.**
  - Reflection positivity through planes of sites, and its chessboard estimate: for a law reflection positive under every reflection through a plane of sites, `P(∩_j θ_{t_j}E_j) ≤ Π_j 𝔷(E_j)` for events `E_j` in the cube `{0, 1}³`, with `𝔷(E) = P(∩_t θ_tE)^{1/N}` (Fröhlich, Israel, Lieb and Simon; Biskup's lecture notes). Premise A1.
  - A torus form of the separation lemma for ⋆-connected sets (Deuschel and Pisztora; Timár): a set meeting every nearest-neighbour path of cubes between two cubes contains a ⋆-connected subset that either separates them with fewer than `L` cubes or has at least `L` cubes. Premise A2.
  - Domination of a sequentially sampled occupied set by independent site occupation; counting self-avoiding paths (at most `6·5^{n−1}` of length `n`).
  - The Bernstein basis on `[0, 1]`, whose nonnegative coefficients certify a nonnegative polynomial.
  - Exact rational and symbolic arithmetic.

## Theorem T0 — the neutral kernel

*Statement.* At `c = 1/cosh β`, `B(u, u′) = 1 + tσσ′` for all site states, with `t = tanh β`.

*Proof.* `e^{±β}/cosh β = 1 ± tanh β` (runner B1), and a pair with an empty end has `σσ′ = 0`. ∎

## Theorem T1 — no long-range order at low density

*Statement.* For every `β > 0` and `z < 1/320`, on every even torus, `Σ_x⟨σ₀σ_x⟩ ≤ p + 6p²/(1 − 5p)` with `p = 64z`. So `M_N² → 0`, and `⟨|σ̂(k)|²⟩` is bounded uniformly in `k` and `L`.

*Proof.*
- **Clusters decouple.** Given the occupied set `O`, the contents have weight `Π_{bonds in O}(1 + ts_xs_y)`. It is unchanged by flipping every content of one cluster of `O`. So `⟨σ₀σ_x | O⟩ = 0` unless `0` and `x` share a cluster, and `|⟨σ₀σ_x⟩| ≤ P(0 ↔ x in O)`; for `x = 0`, `⟨σ₀²⟩ = P(0 occupied)` (runner D2 checks the decoupling on a small graph).
- **Occupation bound.** Given everything off `x`, `P(x occupied) = zS/(1 + zS) ≤ zS`, with `S = (1 + t)^k(1 − t)^l + (1 − t)^k(1 + t)^l` for `k` neighbours at `+1` and `l` at `−1`. For `k + l ≤ 6`, `S ≤ (1 + t)⁶ + (1 − t)⁶ ≤ 64` on `[0, 1]` (runner D1, by basis certificates). So `P(x occupied | rest) ≤ 64z = p`.
- **Domination and paths.** Sampling the sites in sequence, each is occupied with conditional probability at most `p`, so `O` is dominated by independent occupation at density `p`. The event `0 ↔ x` needs an occupied self-avoiding path, and there are at most `6·5^{n−1}` of `n` steps. So `Σ_xP(0 ↔ x) ≤ p + Σ_n 6·5^{n−1}p^{n+1} = p + 6p²/(1 − 5p)` for `p < 1/5` (runner D2, H2). Runner D3 checks the whole inequality exactly on the `2 × 2 × 2` torus at two parameter points. ∎

## Theorem T2 — long-range order at large β and high density

*Statement.* The law is reflection positive through planes of sites, for every `c`, `β` and `z`. Given premises A1 and A2, let `ε = P(A, U)`, the pattern polynomial below. If `ε ≤ 1/2704`, then for every `x` and every even `L`, `⟨σ₀σ_x⟩ ≥ 1 − 2[2ε + 2ε/(1 − 676ε)²] − δ_L`, with `δ_L → 0`.

*Proof.*
- **Reflection positivity.** Reflect through the plane of sites `{x₁ = j}`, which also fixes `{x₁ = j + L/2}`. The weight splits as `W₊ · θW₊`, where `W₊` collects the half's site and bond weights and the square roots of the weights on the fixed planes. All weights are positive. For `F` depending on one half, `Z·E[F θF]` is a sum of squares. Runner C1 checks this exactly on a `4 × 2` torus: for every configuration of the two fixed planes, the weights over the two mirror columns form a symmetric rank-one matrix, for the neutral kernel and for a general one.
- **Chessboard ratios.** For a pattern `τ` of the cube `{0, 1}³`, disseminate it by reflections: `σ^τ(x) = τ(x mod 2)`. Each of the cube's 12 edges then occurs twice per `2 × 2 × 2` cell. So `W(σ^τ) = w_τ^{N/8}`, with `w_τ/w₊ = z^{−V}((1 − t)/(1 + t))^{2m}(1 + t)^{−2k}`, where `V` counts empty sites, `m` edges with opposite contents, and `k` edges touching an empty site. So `𝔷(τ) ≤ (w_τ/w₊)^{1/8} ≤ A^VU^m` (runner E1 checks the cell weights against the kernel for all `3⁸` patterns, and the dissemination weights on the `4³` torus).
- **The pattern polynomial.** A cube is bad unless all eight sites hold the same content. The 6559 bad patterns give `P(A, U) = Σ A^VU^m = 16A + 16U³ + 48AU² + 56A² + 30U⁴ + …`, with 42 terms, all positive (runner E2).
- **A contour count.** By A1 and its subadditivity, any `n` distinct cubes are all bad with probability at most `εⁿ`. Cubes `t + {0, 1}³` and `t + e_a + {0, 1}³` share four sites, so neighbouring good cubes carry the same content. If `σ₀σ_x ≠ 1`, either the cube at `0` or the cube at `x` is bad (probability at most `2ε`), or both are good with opposite contents, and then every nearest-neighbour path of cubes between them meets a bad cube. By A2 the bad cubes contain a ⋆-connected set of `n` cubes that either separates them with `n < L` cubes, meeting a ray within `n` steps, or has at least `L` cubes. At most `26^{2(n−1)} = 676^{n−1}` ⋆-connected sets of `n` cubes pass through a given cube (a spanning tree's closed walk; runner H2 counts 26 and 711 for `n = 2, 3`). So `P(σ₀σ_x ≠ 1) ≤ 2ε + 2ε/(1 − 676ε)² + δ_L`, where `δ_L ≤ Σ_{n≥L} N·676^{n−1}εⁿ → 0` bounds the sets of at least `L` cubes (runner H1 for the series). Since `σ₀σ_x ∈ {−1, 0, 1}`, `⟨σ₀σ_x⟩ ≥ 1 − 2P(σ₀σ_x ≠ 1)`.
- **The explicit region.** `P` has nonnegative coefficients, so it grows with `A` and `U`. At `A = 10⁻⁵`, `U = 10⁻²` it is below `1/2704`, and the bound exceeds `0.998` (runner E2, H1). ∎

The window `1/320 ≤ z < 10⁴⁰` at large `β` is not covered. Neither is the sphere menu at large `β`: there the contents vary continuously, so a contour count does not apply, and block 126's infrared bound gives nothing at the neutral scale.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 126 (landed): no neutral-scale disorder is claimed; whether the neutral law has long-range order at large beta is open"
source_of_blocker_text: block 126's landed claim scope and its gate item N1.3
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the window 1/320 <= z < 10^40; the sphere menu at the neutral scale (an infrared bound); a proof of the torus separation lemma at this scope; an other-family referee"
conditional_surface_status: "the two-valued menu at the neutral scale; T2 given the chessboard estimate and the torus separation lemma"
hypothetical_axiom_status: "the law with vacancies, its weights and the menu are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.** Block 39 T5 (the law with vacancies), block 40 (the neutral scale), block 126 (the infrared bound above the neutral scale, the finite counterexamples at it, and the open question).
- **Probes.** #9260 (Claude Opus 5.5 worker `w-macbookpro9927a-ja869`, the supervisor's own model family; not refereed by another family) found T0–T2, with its own exact checker (11 checks). The supervisor read every step against block 126's landed text, reran that checker, and wrote this note's runner independently: reflection positivity on a `4 × 2` torus for every configuration of the fixed planes, instead of the probe's ring; the occupation bound by Bernstein certificates, instead of the probe's grid; the cell weights against the kernel for every pattern at two parameter points; and an exact check of T1's inequality on the `2 × 2 × 2` torus.
- **In the literature.** Reflection positivity and the chessboard estimate (Fröhlich, Israel, Lieb and Simon); the Peierls contour argument; domination by independent percolation; the separation lemma for ⋆-connected sets (Deuschel and Pisztora; Timár). Reference only.
- **New here:** the answer to block 126's open neutral-scale question for the two-valued menu, both ways.
- **Provenance.** A harvest of a same-family probe result, line-checked by the supervisor. No other model family has refereed it.

## Exact target and obligation graph

Target: whether the neutral two-valued law with vacancies has long-range order, as a function of `z` and `β`. The obligations are:
- (O1) the neutral kernel (T0: proved here; runner B1);
- (O2) no long-range order at low density (T1: proved here; runner D1, D2, D3, H2);
- (O3) reflection positivity (T2: proved here; runner C1);
- (O4) the chessboard ratios and the pattern polynomial (T2: proved here; runner E1, E2);
- (O5) the contour count (T2: proved given A1 and A2; runner H1, H2).

The strongest step taken as a premise: A2, the torus form of the separation lemma.

## No-Go Discipline Gate

The note's negative sentence: at low density the neutral law has no long-range order at any `β`.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Strong binding orders records even when they are scarce.* Contents correlate only inside occupied clusters, whatever `β` (T1; runner D2). ATTEMPTED.
2. *Occupied neighbours raise the occupation probability without bound.* It is at most `64z` for every `β` (runner D1). ATTEMPTED.
3. *Long paths of occupied sites connect distant records.* Their number is at most `6·5^{n−1}`, and the sum is finite for `p < 1/5` (runner D2, H2). ATTEMPTED.
4. *The structure factor grows at some wave vector.* It is bounded by the same sum at every `k` (T1). ATTEMPTED.
5. *Finite tori hide order that appears only in the limit.* The bound holds on every even torus, uniformly in `L` (T1). ATTEMPTED.

Scope left open: the window `1/320 ≤ z < 10⁴⁰`; the sphere menu at large `β`; the positive sentence T2 rests on premises A1 and A2.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical". The two external results T2 uses are stated as premises A1 and A2; the domination and path counts are proved. No hidden condition was found.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 39, 40 (landed) | the law with vacancies; the neutral scale | yes (restated) |
| block 126 (landed) | the two-valued menu at the neutral scale; the diagnostic; the open question | yes (restated) |
| probes #9260 (unrefereed, same family) | the route | yes (re-derived and line-checked here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no long-range order at low density at any `β`; long-range order at large `β` and high density" | executed: the neutral kernel | executed: the occupation bound for every neighbourhood | executed: cluster decoupling; the path sum | executed: reflection positivity on a `4 × 2` torus; all `3⁸` cube patterns and the dissemination counts | every even torus; T2 given A1 and A2 |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "At the neutral scale an occupied neighbour weighs the same as an empty one on average, so nothing should order."
  - *Reply:* The average is over the neighbour's content. An aligned pair still weighs `1 + t` against `1 − t` for an opposed one. At high density the empty sites that would decouple the lattice are rare, and alignment wins (T2). At low density they are common, and it cannot (T1).

### N8 — Cross-cycle echo
- Block 40: the neutral scale.
- Block 126: order above it, and finite counterexamples at it.
- This note: at it, no order at low density and order at large `β` and high density.

## Falsifiers

- An even torus, `β` and `z < 1/320` with `Σ_x⟨σ₀σ_x⟩ > p + 6p²/(1 − 5p)`.
- A bad cube pattern miscounted in the pattern polynomial, or a dissemination count other than stated.
- A failure of reflection positivity through a plane of sites.

## Boundaries and non-claims

- The two-valued menu, at the neutral scale; T2 given premises A1 and A2.
- The window between the two statements, and the sphere menu at large `β`, are not covered.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 39, 40 and 126 (landed), restated.
- Named standard imports, at definition level: reflection positivity and the chessboard estimate (Fröhlich, Israel, Lieb and Simon; premise A1); the torus separation lemma for ⋆-connected sets (Deuschel and Pisztora; Timár; premise A2); domination by independent site percolation; counting self-avoiding paths; the Bernstein basis certificate; exact rational and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block, 2026-09-26, during the owner's 12-hour campaign of that day.
- **Provenance.** The proof is probe #9260's (Claude Opus 5.5, the supervisor's own model family). The supervisor read every step against block 126's landed text, reran the probe's exact checker (11/11), and wrote this note's runner independently. No other model family has refereed it.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found block 126's open item and no other attempt at it.
- **Independence.** Mutation census: one mutation per science family (B, C, D, E, H), each failing in its own family, and two in family F (7/7).

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_moving_records_at_the_neutral_scale_have_no_long_range_order_at_low_density_and_long_range_order_at_large_beta_and_high_density_2026_09_26.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
