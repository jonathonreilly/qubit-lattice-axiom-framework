---
claim_id: admissibility_rule_at_the_neutral_scale_moving_records_have_no_long_range_order_at_low_density_on_both_menus_and_the_sphere_threshold_falls_as_beta_to_minus_five_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 126's law with vacancies as landed (each site of an even cubic torus empty with weight 1 or holding a content with weight z times the menu's measure; bond kernel 1 with an empty end and c e^(beta s.s') between contents), at the neutral scales c0 = beta/sinh beta (sphere menu, uniform probability measure) and c0 = 1/cosh beta (two-valued menu, counting measure): (T1) given every other site, the contents' weight at a site is at most F_6(beta) = (beta/sinh beta)^6 sinh(6 beta)/(6 beta) on the sphere and at most G(tanh beta) = (1 + t)^6 + (1 - t)^6 on the two-valued menu, both attained by six aligned neighbours; (T2) with w = z F_6(beta) or w = z G(tanh beta), a site is occupied given the rest with probability at most rho = w/(1 + w), and for w < 1/4, on every even torus, sum_x |<sigma_0.sigma_x>| <= rho + 6 rho^2/(1 - 5 rho): no long-range order and a bounded structure factor for z < 1/(4 F_6(beta)) on the sphere and z < 1/(4 G(tanh beta)) on the two-valued menu, a region that contains z < 1/256 at every beta and so block 153's z < 1/320; (T3) the sphere threshold 1/(4 F_6(beta)) tends to 1/4 as beta -> 0 and is asymptotic to 3/(64 beta^5). A harvest of probe #9304 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9329, Grok), whose occupation bound w/(1 + w) enlarges the attempt's regions. The window between low and high density and the sphere at high density are not covered. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_with_vacancies_the_infrared_stiffness_is_set_by_the_binding_scale_long_range_order_above_the_neutral_scale_and_no_full_bound_at_it_bounded_theorem_note_2026-09-24
runner: scripts/admissibility_rule_at_the_neutral_scale_moving_records_have_no_long_range_order_at_low_density_on_both_menus_2026_09_26.py
---

# At the neutral scale, moving records have no long-range order at low density on both menus, and the sphere's threshold falls as β⁻⁵

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 126's law with vacancies at its neutral scales; a harvest of probe #9304, confirmed by an other-family referee in #9329; nothing adopted or registered; unaudited)

This note works within block 126 as landed on main (the law with vacancies, its two menus and its neutral scales) and places block 153 (open PR #9285); it reports densities below which moving records at the neutral scale have no long-range order, on both menus; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 153 (held as an open PR) found no long-range order at low density on the two-valued menu, for `z < 1/320`, at every `β`. It left the sphere menu open. This note is a harvest of a probe result that another model family has confirmed. The referee also enlarged the result's region.

- **T1: the largest weight at a site.** Given every other site, the contents' weight at a site is at most:
  - `F₆(β) = (β/sinh β)⁶ sinh(6β)/(6β)` on the sphere;
  - `G(tanh β) = (1 + t)⁶ + (1 − t)⁶` on the two-valued menu.

  Six aligned occupied neighbours attain both.
- **T2: no long-range order at low density, on both menus.** Let `w = zF₆(β)` on the sphere or `w = zG(tanh β)` on the two-valued menu. A site is then occupied, given the rest, with probability at most `ρ = w/(1 + w)`. If `w < 1/4`, then on every even torus `Σ_x |⟨σ₀·σ_x⟩| ≤ ρ + 6ρ²/(1 − 5ρ)`.
  - So there is no long-range order, and the structure factor is bounded uniformly in `k` and `L`, for:
    - `z < 1/(4F₆(β))` on the sphere;
    - `z < 1/(4G(tanh β))` on the two-valued menu.
  - The two-valued region contains `z < 1/256` at every `β`, and so block 153's `z < 1/320`. It is larger than `1/320` by the factor `80/G`: `40` as `β → 0` and `5/4` as `β → ∞`.
- **T3: the sphere's threshold.** `1/(4F₆(β))` tends to `1/4` as `β → 0`, and is asymptotic to `3/(64β⁵)` as `β → ∞`.

In plain terms: at the neutral scale an occupied neighbour weighs, on average, what an empty site weighs. Even the worst neighbourhood, six neighbours all pointing one way, raises a site's weight only by a fixed factor. So when records are scarce enough they sit in small islands, and islands cannot line up across the lattice. On the sphere, stronger binding makes the worst neighbourhood much heavier, so the density must fall as `β⁻⁵`.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The law with vacancies, its weights and the menus are supplied clauses. Nothing is adopted.
- **Block 126 (landed on main).** Quoted by the runner (A3).
  - The law: each site of an even torus `(ℤ/Lℤ)³` is empty with weight 1, or holds a content with weight `z` times the menu's measure.
  - The kernel is `1` with an empty end and `B(s, s′) = c e^{βs·s′}` between contents.
  - The menus: the sphere `S²` with the uniform measure, taken here as the probability measure (with the area measure, `z` is rescaled by `4π`); and `s = ±1` with counting measure.
  - The scales: `c₀(γ) = γ/sinh γ` (sphere) or `1/cosh γ` (two-valued). The neutral scale is `c₀(β)`.
  - The diagnostic: `σ_x = n_x s_x`, and `M_N² = N⁻¹Σ_x⟨σ₀·σ_x⟩`.
- **Block 153** (open PR #9285, not landed) is placement only. Its architecture is used: clusters decouple, the occupied set is dominated, and paths are counted.
- **Names.** The two-valued weight bound uses Bernstein-basis certificates on `[0, 1]`. The path count is the standard bound for self-avoiding walks. The domination is the sequential coupling with independent site occupation (Harris's comparison).

## Domain qualifications

- `β > 0` and `z ≥ 0`, at the neutral scale exactly. The torus is even and cubic.
- The sphere's measure is the uniform probability measure.
- The statements are the low-density side only. The window between low and high density, and the sphere at high density, are not covered.
- These are conditional statements within supplied clauses, not a physical identification.

## Theorem T1 — the largest weight at a site

*Statement.*
- **Sphere.** Let the occupied neighbours of `x` carry `s₁, …, s_m` (`m ≤ 6`), with `v = Σ s_j`. The contents' weight at `x` is `c₀^m ⟨e^{βs·v}⟩ = c₀^m sinh(β|v|)/(β|v|)`. It is at most `F_m(β) = c₀^m sinh(mβ)/(mβ)`, and `F_m ≤ F₆`.
- **Two-valued.** With `k` neighbours at `+1` and `l` at `−1`, the weight is `(1 + t)^k(1 − t)^l + (1 − t)^k(1 + t)^l`. It is at most `G(t) = (1 + t)⁶ + (1 − t)⁶`. `G` rises from `2` to `64` on `[0, 1]`.
- At the neutral scales an occupied neighbour weighs `1` on average on both menus.

*Proof.*
- The sphere average is `½∫₀^π e^{β|v|cos θ} sin θ dθ = sinh(β|v|)/(β|v|)` (B1).
- `y cosh y − sinh y = Σ_{n≥1} 2n y^{2n+1}/(2n+1)! > 0` (B2). So `sinh(y)/y` increases, and `|v| ≤ m` gives the bound by `F_m`.
- `F₁ = 1` and `F_{m+1}/F_m = (m/(m+1)) β(coth β + coth(mβ))` (B3). This exceeds 1 because `x coth x > 1` for `x > 0` (B2).
- Two-valued: `e^{±β}/cosh β = 1 ± t` (B1). For all 28 pairs with `k + l ≤ 6`, `G − S` has nonnegative basis coefficients on `[0, 1]` (B4). ∎

## Theorem T2 — no long-range order at low density, on both menus

*Statement.*
- With `w = zF₆(β)` (sphere) or `w = zG(tanh β)` (two-valued), `P(x occupied | rest) ≤ ρ = w/(1 + w)`.
- If `w < 1/4`, then on every even torus `Σ_x |⟨σ₀·σ_x⟩| ≤ ρ + 6ρ²/(1 − 5ρ)`. So `M_N² → 0`, and `⟨|σ̂(k)|²⟩` is bounded uniformly in `k` and `L`.
- The regions are `z < 1/(4F₆(β))` (sphere) and `z < 1/(4G(tanh β))` (two-valued). The second contains `z < 1/256` at every `β`.

*Proof.*
1. **Occupation.** Given the rest, `x` is occupied with probability `zS/(1 + zS)`, which increases in `S`. By T1 it is at most `ρ = w/(1 + w)`. And `ρ < 1/5` exactly when `w < 1/4` (C1).
2. **Clusters decouple.**
   - Given the occupied set, a common rotation (sphere) or sign flip (two-valued) of one cluster's contents keeps every bond weight.
   - On the sphere, the cluster's conditional mean content is therefore fixed by the quarter turns about two axes. Their only common fixed vector is `0` (C3).
   - So contents in different clusters are uncorrelated, and `|⟨σ₀·σ_x⟩| ≤ P(0 ↔ x)`.
3. **Domination and paths.**
   - Sampling the sites in sequence, each is occupied with conditional probability at most `ρ`. So the occupied set is dominated by independent occupation at density `ρ`.
   - A path of `n` steps has `n + 1` sites. There are at most `6·5^{n−1}` self-avoiding ones: exactly 6, 30, 150, 726 and 3534 for `n ≤ 5` (C2).
   - The partial sums satisfy `(1 − 5ρ)Σ_{n≤N} 6·5^{n−1}ρ^{n+1} = 6ρ²(1 − (5ρ)^N)` (C2). This gives the bound for `ρ < 1/5`.
4. **The regions.** `G ≤ 64` on `[0, 1]`, so `1/(4G) ≥ 1/256 > 1/320`. The factor `80/G` runs from `40` to `5/4` (C4). ∎

## Theorem T3 — the sphere's threshold

*Statement.* `z₀(β) = 1/(4F₆(β))` tends to `1/4` as `β → 0`, and `β⁵z₀(β) → 3/64` as `β → ∞`.

*Proof.* `F₆ → 1` as `β → 0`, and `F₆/β⁵ → 16/3` as `β → ∞` (D1). The earlier remark's weight `(βe^β/sinh β)⁶` exceeds `F₆` by a factor asymptotic to `12β` (D2). ∎

- The worst case, six aligned neighbours, is attained, so this method cannot give a larger region.
- Improving it needs an exploration that uses the neutral average for unrevealed neighbours, or a better path count than `5ⁿ`.

## What this settles and what it does not

- **Settled.** At the neutral scale, both menus have no long-range order below explicit densities at every `β`. For the sphere this is new. For the two-valued menu the region grows from `1/320` to `1/(4G(tanh β)) ≥ 1/256`.
- **For block 153 (open PR #9285).** Its T1 stands as stated. This note's T2 contains it.
- **Not settled.**
  - The window between low and high density.
  - The sphere at high density, where a contour count does not apply.
  - The torus separation lemma behind block 153 T2.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 153 (open PR #9285): the sphere menu at the neutral scale and the window 1/320 <= z; block 126 as landed: no statement at the neutral scale"
source_of_blocker_text: probes task J:derive:the-neutral-moving-records-law-between-low-and-high-density
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an exploration with conditional neutrality; the sphere at high density; the torus separation lemma"
conditional_surface_status: "exact at the neutral scales of block 126's law, low density"
hypothetical_axiom_status: "the law with vacancies, its weights and the menus are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 126 (landed): the law, the menus and the neutral scales. At the neutral scale it gives no bound.
  - Block 153 (open PR #9285): the two-valued menu at low density (`z < 1/320`), and order at large `β` and high density under two premises.
- **Probes.**
  - #9260, worker `w-macbookpro9927a-ja869`, Claude Opus 5.5: block 153's source. For the sphere it only remarked on a weight bound, `(βe^β/sinh β)⁶`.
  - #9304, worker `w-jonathonsmac4f50-j1c03`, Claude Opus 5.5, the supervisor's own model family, found:
    - T1;
    - the sphere region `z < 1/(5F₆)`;
    - the β-dependent two-valued region `z < 1/(5G)`.

    Both of its regions use `ρ = w`.
  - #9329, worker `w-macbookpro90c72-jc7b4`, `grok-4.6`, another model family, refereed #9304 with its own checker. It kept the occupation probability as `w/(1 + w)`, which gives the larger regions `1/(4F₆)` and `1/(4G)` stated here: "HIT: confirmed - no long-range order for `z < 1/(4 F_6(β))` on the sphere, asymptotic to `3/(64 β^5)`, and for `z < 1/(4 G(tanh β))` on the two-valued menu."
- **In the literature.**
  - Low-density absence of order by domination and path counting is a standard pattern: Harris's comparison, and counts of self-avoiding walks.
  - The known connective constant of `ℤ³`, about 4.68, is not used.
- **New here.**
  - The harvest.
  - The referee's enlargement, made the statement.
  - An exact runner: the path counts to `n = 5`, the basis certificates for all 28 neighbour counts, and the asymptotics.
- **Provenance.** Found by the supervisor's family. Confirmed, and its regions enlarged, by another family.

## Exact target and obligation graph

Target: no long-range order at the neutral scale at low density, on both menus. The obligations are:
- (O1) the premises (A3);
- (O2) the weights (B1–B4);
- (O3) occupation, decoupling, domination and paths (C1–C4);
- (O4) the sphere's threshold (D1–D2).

## No-Go Discipline Gate

The note's negative sentence: no long-range order below the stated densities on either menu.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A neighbourhood heavier than six aligned ones.* None exists: `F_m` and `G` are the maxima, and they are attained (B3, B4). ATTEMPTED.
2. *Correlations across clusters.* They vanish by the cluster symmetry (C3). ATTEMPTED.
3. *More paths than the count allows.* The count `6·5^{n−1}` bounds the exact numbers (C2). ATTEMPTED.

Scope left open:
- the window between low and high density;
- the sphere at high density.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The sphere's probability normalization is declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 126 (landed) | the law, the menus, the scales | yes (quoted, A3) |
| block 153 (open PR #9285) | the two-valued low-density result; the architecture | placement |
| probe #9304 and referee #9329 | the result and its enlargement | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no long-range order below `1/(4F₆)` and `1/(4G)`" | executed: the sphere average and the neutral scales | executed: the conditional weights | executed: the occupation bound and its cutoff | executed: path counts, the path sum, the quarter turns, the regions, the asymptotics | not executed: the window; the sphere at high density |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This only restates block 153."
  - *Reply:* Block 153 covered the two-valued menu below `1/320`.
  - This note covers the sphere, which block 153 left open, and it enlarges the two-valued region at every `β`: by a factor of up to 40 at small `β`.
- *Objection:* "`β⁻⁵` means the sphere has no low-density region at strong binding."
  - *Reply:* The region shrinks but stays positive at every `β`.

### N8 — Cross-cycle echo
- Block 126: order above the neutral scale.
- Block 153: the two-valued menu at the neutral scale.
- This note: both menus at low density.

## Falsifiers

- A neighbourhood with a conditional weight above `F₆(β)` on the sphere, or above `G(tanh β)` on the two-valued menu.
- An even torus and `z` below the stated regions with `Σ_x|⟨σ₀·σ_x⟩| > ρ + 6ρ²/(1 − 5ρ)`.

## Boundaries and non-claims

- The neutral scale and low density only.
- The law, the weights and the menus are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 126 (landed), restated and quoted. Block 153 (open PR) placed.
- Named standard imports, at definition level:
  - Bernstein-basis certificates of nonnegativity on `[0, 1]`;
  - sequential domination by independent site occupation (Harris);
  - the self-avoiding path bound `6·5^{n−1}` on `ℤ³`;
  - the geometric series;
  - exact symbolic and rational arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.**
  - Probe #9304 (Claude Opus 5.5) was refereed by #9329 (`grok-4.6`, another family). The referee enlarged the regions.
  - The supervisor wrote a new exact runner.
- **Before writing.** Origin was re-fetched. Block 126 was read as landed. Block 153 was read on its PR branch. The own prior-art check covered memory, open PRs and main. It found block 153 and no earlier low-density sphere result.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_at_the_neutral_scale_moving_records_have_no_long_range_order_at_low_density_on_both_menus_2026_09_26.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
