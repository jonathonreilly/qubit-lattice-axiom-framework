---
claim_id: admissibility_rule_the_only_reach_three_completion_that_keeps_each_further_stretch_a_relabelling_is_block_69s_linear_one_and_it_fails_beyond_seven_sixths_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed, for a uniform isotropic stretch and a finite-stretch completion per axis F(k, b) with F(k, 0) = sin k and first-order term sin k cos^2 k (block 69 T4), inside block 176's reach-three family l F = sin k (1 - q sin^2 k) (pushed; one geometry for all species), and for the supplied covariance principle that each further stretch acts on the stretched walk as a relabelling, dF/db = p dF/dk with p a formal series of local odd generators: (T1) covariance to every order forces F = sin k (1 + beta(b) cos^2 k), so q(l) = 1 - l, block 69's linear completion; (T2) that completion is covariant, with generator beta' sin k cos k/(1 + beta - 3 beta sin^2 k); (T3) counted in lattice labels, it keeps the long-wave speed the fastest only for l <= 7/6 (blocks 173, 176); (T4) covariant completions outside reach three exist, the fixed-generator flow and the self-consistent flow, and already have reach-five terms at second order; the first outruns w/l somewhere iff l^2 > 3/2; (T5) for l > 2/3 the linear completion is F = g_l(sin k) with g_l monotone on [-1, 1], the free walk relabelled, with a bounded generator; (T6) that generator is not parallel to the stretched walk's velocity, so its current twists at every l != 1, while the momentum F F_k that keeps symmetric books generates the self-consistent flow: of reach three, covariance and symmetric books at finite stretch, at most two hold. So the completion is a supplied choice among these. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_only_covariant_reach_three_completion_2026_09_27.py
---

# The only reach-three completion that keeps each further stretch a relabelling is block 69's linear one, and it fails beyond seven sixths

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 69 as landed and a supplied covariance principle; blocks 173 and 176 are pushed and placed, and the facts used from them are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within block 69 as landed on main (the two-step coupling of the walk to a uniform strain) and asks whether a natural principle fixes its completion to finite stretch; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 69 (landed) fixes the two-step coupling at first order in the strain, and says its leading order does not determine a nonlinear completion. Block 176 (pushed) wrote every reach-three completion at uniform stretch as one number `q(ℓ)`, with `ℓ F = sin k (1 − q sin² k)`. It found that one speed limit holds iff `q ≥ −1/6`. The completion is item 5 of the third column.

This note tests one principle that could fix it. The principle is covariance: at every stretch, a further infinitesimal stretch acts on the stretched walk as a relabelling. That is, `∂_b F = p ∂_k F`, with `p` a local generator at each order.

- **T1: within reach three, covariance forces the linear completion.** Every covariant completion in block 176's family is `F = sin k (1 + β(b) cos² k)`, so `q(ℓ) = 1 − ℓ`. This is block 69's own linear completion.
- **T2: and that completion is covariant**, with generator `β′ sin k cos k/(1 + β − 3β sin² k)`.
- **T3: it fails beyond `ℓ = 7/6`.** With `q = 1 − ℓ`, short waves near the axes outrun `w/ℓ` exactly when `ℓ > 7/6` (blocks 173, 176).
- **T4: covariance outside reach three.** Two natural covariant completions leave reach three already at second order:
  - the flow of block 69's fixed two-step momentum;
  - the flow of the stretched walk's own momentum.
  The first outruns `w/ℓ` somewhere once `ℓ² > 3/2`.
- **T5: the covariant completion is a relabelling.** For `ℓ > 2/3`, `F = g_ℓ(sin k)` with `g_ℓ(S) = S(1 + (ℓ − 1)S²)/ℓ` monotone on `[−1, 1]`. So the linear completion is the free walk relabelled, with a bounded generator.
- **T6: a trilemma.** Take reach three, covariance, and symmetric books at finite stretch (block 179). At most two can hold.
  - The linear completion's generator is not parallel to the stretched walk's velocity, so its current twists at every `ℓ ≠ 1`.
  - The momentum `F ∂_kF` that keeps the books generates the self-consistent flow, which leaves reach three.

Block 176's label-unit speed limit is the right test when the sites are held physical, as for a hopping law. On a closed lattice a uniform stretch cannot be a relabelling, since a linear displacement is not periodic. For the linear completion read as a relabelling (T5), the free walk's single speed limit holds by unitary equivalence. So the completion is a supplied choice among three pairs from the trilemma, and each pair has a worked cost.

In plain terms: one might hope that stretching an already stretched lattice a little more is just a relabelling, as it is for the unstretched lattice. If the coupling is to stay short-ranged, that hope pins down how the walk stretches: it is the free walk with its labels moved. But then the walk twists the bonds once stretched. And if the stretch is a real change of hopping, as it must be on a closed lattice, the same completion lets some short waves outrun long ones past seven sixths. Short range, relabelling and untwisted books cannot all hold at once.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Block 69 is used as landed on main. Blocks 173 and 176 are pushed and placed; the facts used from them are re-derived (runner D1).

- **The coupling** (block 69).
  - Uniform form, quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`".
  - Its boundary, quoted: "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
  - Its momentum, quoted: "Set P_j=S_j C_j=(T_j^2-T_j^-2)/(4i)".
  - At isotropic `B = b·1` each axis has `F = sin k + b sin k cos² k + O(b²)`.
- **Block 176's family** (pushed). `ℓ F = sin k (1 − q sin² k)`: odd, reach at most three per axis, and one geometry for all species, hence symmetric under `k → π − k`. `ℓ` is fixed by the long-wave speed, `∂_k F(0) = 1/ℓ`.
- **Covariance** (supplied, and the principle tested). `F(k, b)` obeys `∂_b F = p(k, b) ∂_k F`, where `p = Σ_n bⁿ p_n` and each `p_n` is an odd trigonometric polynomial. At `b = 0`, `p_0 = sin k cos k`, the symbol of block 69's two-step momentum.
- **Notation.** `s = sin k`, `c = cos k`, `x = s²`.

In the literature, a symmetry kept order by order constrains higher-order couplings through its identities (the Ward–Takahashi identities). This note uses none of it as authority.

## Domain qualifications

- Uniform isotropic stretch, per axis. Anisotropic stretches are not treated.
- Covariance is formal: order by order in `b`.
- "Admissible" means block 176's single speed limit: no wave faster than `w/ℓ`.

## Theorem T1 — within reach three, covariance forces the linear completion

*Statement.* If `F` stays in block 176's family at every order and obeys covariance, then `F = s(1 + β(b)c²)` for a formal series `β` with `β(0) = 0` and `β′(0) = 1`. With `1/ℓ = 1 + β`, this is `ℓF = s(1 − (1 − ℓ)s²)`, that is `q(ℓ) = 1 − ℓ`.

*Proof.*
- *The generator's form.* `F` is odd and symmetric under `k → π − k`, so `∂_bF` is too, while `∂_kF` is antisymmetric. So each `p_n` is odd and antisymmetric under `k → π − k`. That leaves `p_n = Σ_m a_m sin 2mk = s c g_n(x)` with `g_n` a polynomial (runner B1).
- *Induction.* Suppose `F ≡ s(1 + β^{(n−1)}c²)` modulo `bⁿ`. Covariance at order `b^{n−1}` fixes `p_0, …, p_{n−2}` uniquely from `F`, since each enters as `p_m c` with `c ≢ 0`. They are those of the linear family with the same `β^{(n−1)}` (T2).
- At order `b^{n−1}` the new term is `n F_n = n F̃_n + (p_{n−1} − p̃_{n−1})c`, where `F̃_n = β̃_n s c²` is the linear family's term. So `F_n = s c²(β̃_n + δg(x)/n)` with `δg = (p_{n−1} − p̃_{n−1})/(sc)`.
- Reach three requires `F_n/s = (1 − x)(β̃_n + δg(x)/n)` to have degree at most one in `x`. So `δg` is constant, and `F_n = β_n s c²`. This completes the induction.
- *The length.* `∂_kF(0) = 1 + β`, so `1/ℓ = 1 + β`. Then `ℓF = s(1 − (1 − ℓ)s²)` (runner C1).
- Runner B2 checks the solution order by order to order five, with every generator coefficient kept free. Each term stays proportional to `s c²`, and the four free constants only reparametrise `b`. ∎

## Theorem T2 — the linear completion is covariant

*Statement.* `F = s(1 + βc²)` obeys `∂_bF = p ∂_kF` with `p = β′ s c/(1 + β − 3β s²)`. Its series in `b` has coefficients `s c` times polynomials in `s²`, so it is local order by order.

*Proof.* `∂_bF = β′ s c²` and `∂_kF = c(1 + β − 3βs²)` (runner C1). ∎

## Theorem T3 — it fails beyond seven sixths

*Statement.* For `ℓF = s(1 − q s²)`, the axis group speed squared, in units of `w/ℓ`, is `(1 − x)(1 − 3qx)²`. Near `k = 0` its root is `1 − (1/2 + 3q)k² + O(k⁴)`, so it exceeds the long-wave value iff `q < −1/6`. For `q = 1 − ℓ` that is `ℓ > 7/6`.

*Proof.* Differentiation and series (runner D1). This re-derives block 176's T2 and block 173's threshold. ∎

## Theorem T4 — covariance outside reach three

*Statement.*
- (a) With the fixed generator `p = sin k cos k`, the covariant completion is the flow `F = e^b s/√(c² + e^{2b}s²)`. Its second-order term is `s(1 − 4s² + 3s⁴)/2`, which has reach five. In the length, `F = s/√(ℓ²c² + s²)`, and its axis speed exceeds `1/ℓ` somewhere iff `ℓ² > 3/2`.
- (b) With the stretched walk's own two-step momentum, `p = F ∂_kF`, the covariant completion obeys `∂_bF = F(∂_kF)²`, so `u = F²` obeys `∂_bu = (∂_ku)²/2`. Its second-order term is `s(3 − 10s² + 7s⁴)/2`, which also has reach five.

*Proof.*
- (a) Integrate `dk/db` along `p`: `tan k ↦ e^b tan k`.
- The speed `ℓ²c/(1 + (ℓ² − 1)c²)^{3/2}` has an interior maximum iff `ℓ² > 3/2`. The squared ratio to `1/ℓ` there is `4y³/(27(y − 1))` with `y = ℓ²`: it equals 1 at `y = 3/2` and increases beyond.
- (b) The substitution `u = F²`.
- Runner E1 checks all of these. ∎

## Theorem T5 — the covariant completion is a relabelling

*Statement.* In `ℓ`, the linear completion is `F = g_ℓ(sin k)`, with `g_ℓ(S) = S(1 + (ℓ − 1)S²)/ℓ` and `g_ℓ′ = (1 + 3(ℓ − 1)S²)/ℓ ≥ (3ℓ − 2)/ℓ`. For `ℓ > 2/3`, `g_ℓ` is a monotone bijection of `[−1, 1]`, so each axis's dispersion is the free one composed with a diffeomorphism of the zone. Its generator in `ℓ` is `s c/(ℓ(1 + 3(ℓ − 1)s²))`, which is bounded there.

*Proof.* Differentiation (runner C2). ∎

So for the walker the linear completion is the free walk relabelled. Block 176's label-unit speed limit then does not describe a physical outrunning. It describes one when the sites are held physical, for a hopping law. That is the case on a closed lattice, where a uniform stretch cannot be a relabelling, since a linear displacement is not periodic.

## Theorem T6 — a trilemma at finite stretch

*Statement.* The linear completion's generator divided by the stretched walk's `F ∂_kF` is `ℓ/((1 + (ℓ − 1)s²)(1 + 3(ℓ − 1)s²)²)`. This depends on the axis: at `ℓ = 2` it is `15625/45968` for `sin k = 3/5` and `31250/218489` for `sin k = 4/5`. By block 179 T1, a current is symmetric on single waves only if its momentum is parallel to the velocity, so the linear completion's current twists at every `ℓ ≠ 1`. The momentum `F ∂_kF`, which keeps symmetric books, generates the self-consistent flow (T4(b)), and that flow leaves reach three. Hence at most two of the following hold:
- reach three;
- covariance;
- symmetric books at finite stretch.

*Proof.* Runner E2, with T1 and T4. ∎

## What this settles and what it does not

- **Settled.**
  - Within reach three, the covariance principle fixes the completion as block 69's linear one, which is the free walk relabelled (T5).
  - Its current twists at every finite stretch (T6).
  - Read as a hopping law with sites held physical, it outruns `w/ℓ` beyond `ℓ = 7/6`.
- **For the third column** (item 5). The completion remains a supplied choice. Its sharpest form is a pair from the trilemma of T6:
  - reach three with covariance: the linear completion, the free walk relabelled, which twists;
  - covariance with symmetric books: the self-consistent flow, which leaves reach three;
  - reach three with symmetric books: a hopping law without covariance, such as block 176's smooth completion.
  - On a closed lattice, where the zero mode of blocks 146–148 and 180 lives, a uniform stretch is a hopping law, and block 176's speed limit applies.
- **Not settled.**
  - Anisotropic stretches.
  - Whether any covariant completion outside reach three is admissible at every stretch.
  - Principles other than covariance.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 69 N1 as landed: the leading order does not determine a nonlinear completion; blocks 173 and 176 (pushed): admissibility iff q >= -1/6"
source_of_blocker_text: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; anisotropic stretches; admissible covariant completions outside reach three"
conditional_surface_status: "exact within block 69 and block 176's family, under the supplied covariance principle"
hypothetical_axiom_status: "the coupling, its completion and the covariance principle are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling, and that the leading order does not fix a completion.
  - Block 173 (pushed): the linear completion outruns `w/ℓ` beyond `ℓ = 7/6`.
  - Block 176 (pushed): the family and its admissibility.
- **In the literature.**
  - A symmetry kept order by order fixes higher couplings through its identities (Ward; Takahashi).
  - The substitution `u = F²` turns the self-consistent flow into a first-order equation of the Hamilton–Jacobi type, whose derivative obeys the inviscid equation named after Burgers and solved by Hopf's method of characteristics.
  - None is used as authority.
- **New here.**
  - Covariance within reach three forces the linear completion (T1).
  - The trade-off with admissibility (T3 with T1).
  - The two covariant completions outside reach three, and the first one's threshold (T4).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed. T5, T6 and the label-unit caveat came from a lattice lens of the supervisor's panel (Claude Fable 5.1, the same vendor family, not a referee), and were checked here exactly.

## Exact target and obligation graph

Target: whether covariance fixes a reach-three completion. The obligations are:
- (O1) the premises (A3);
- (O2) the generator's form and the order-by-order solution (B1, B2);
- (O3) the linear family's covariance and its `q` (C1);
- (O4) the speed limit (D1);
- (O5) the covariant completions outside reach three (E1);
- (O6) the relabelling at finite stretch (C2), and the trilemma (E2).

## No-Go Discipline Gate

The note's negative sentences:
- no completion in block 176's reach-three family is both covariant and admissible, as a hopping law, beyond `ℓ = 7/6`;
- reach three, covariance and symmetric books at finite stretch do not all hold.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A generator of larger reach.* Allowed: `p_n` is any odd trigonometric polynomial. T1's reach condition is on `F`, not on `p`. ATTEMPTED; closed.
2. *A different parametrisation of the stretch.* `ℓ` is fixed by the long-wave speed, and reparametrising `b` changes only `β(b)`. ATTEMPTED; closed.
3. *Covariance only to finite order.* T1's induction holds at each order. Covariance to order two already forces `q₂ = 0`, meaning `q = 1 − ℓ + O((ℓ − 1)³)`. ATTEMPTED; closed.
4. *Anisotropic stretches.* Not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the family, the covariance principle, isotropy and formality.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling's first order and momentum; no completion fixed | yes (quoted, A3) |
| blocks 173, 176 (pushed) | the family and its speed limit | re-derived (D1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "covariance within reach three forces `q = 1 − ℓ`, which fails beyond `7/6`" | executed: the generator's form; the linear family's generator | executed: the speed polynomial | executed: covariance to order five, free coefficients symbolic | executed: the two completions outside reach three | proved, not executed: every order (induction) |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Covariance is too strong; nobody requires it."
  - *Reply:* Then it cannot be the principle that fixes the completion. That is the point of the note: the completion stays supplied, and this principle, the natural one, would fix it only at the cost of admissibility or locality.

### N8 — Cross-cycle echo
- Block 69: no completion fixed.
- Block 173: the linear completion fails beyond `7/6`.
- Block 176: admissible iff `q ≥ −1/6`, with a smooth completion.
- This note: covariance picks the linear completion within reach three.

## Falsifiers

- A covariant completion in block 176's family other than `q = 1 − ℓ`.
- An order at which the linear family is not covariant with a local generator term.

## Boundaries and non-claims

- Uniform isotropic stretch; block 176's family; formal covariance.
- The coupling, its completion and covariance are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 69 (landed), quoted. Blocks 173 and 176 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - formal power series;
  - trigonometric polynomials;
  - integration along a vector field;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Before writing.**
  - Origin was re-fetched. Block 69 was read as landed, and blocks 173 and 176 on their branches.
  - The landed notes were grepped for "completion", "finite strain" and "dilation". The probes' queued task on what fixes the completion (refill ae) is unworked.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_only_covariant_reach_three_completion_2026_09_27.py
```

Expected: `TOTAL: PASS=15 FAIL=0`.
