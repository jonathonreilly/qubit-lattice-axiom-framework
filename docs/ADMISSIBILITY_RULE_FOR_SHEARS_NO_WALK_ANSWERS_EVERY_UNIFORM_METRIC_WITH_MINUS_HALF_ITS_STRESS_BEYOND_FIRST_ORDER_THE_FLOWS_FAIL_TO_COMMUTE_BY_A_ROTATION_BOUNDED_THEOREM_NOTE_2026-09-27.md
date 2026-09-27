---
claim_id: admissibility_rule_for_shears_no_walk_answers_every_uniform_metric_with_minus_half_its_stress_beyond_first_order_the_flows_fail_to_commute_by_a_rotation_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed (a uniform strain of any symmetric form) and block 139's staggered mass as landed: (T1) every Clifford walk h = sum_a F_a(k) X_a + mu Gamma (anticommuting hermitian involutions; hops of any form, not only per axis) satisfies block 181's two book identities, with P^s and K^s built from any divided-difference decomposition of h - h' and h^2 - h'^2 (hermitian densities need a decomposition with the pair-exchange symmetry, exhibited for per-axis hops by block 184 T7 but not here for hops depending on several momenta); for decompositions continuous at q = 0, on single waves K^s_ab(k, k) = (1/4)(d_a h d_b W + d_b h d_a W) with W = h^2; (T2) the stress-response principle dh/dg_ab = -(1/2) K^s_ab (the off-diagonal variable counting both entries), started from the free walk, is block 69's coupling with B = -(g - 1)/2 at first order for every component; (T3) its (11) and (12) flows do not commute at second order: the mixed derivatives differ by (1/4) cos k1 cos k2 cos 2k1 (sin k2, -sin k1, 0), orthogonal to the walk's Clifford vector, a rotation at fixed energy, while the (11) and (22) flows commute; (T4) no constant-coefficient placement of the metric's indices removes the defect; (T5) a metric-independent rotation term alpha(k) e3 x F in the shear flow would need d_1 alpha = -cos k2 cos 2k1/(2 sin k1), which has no continuous solution across k1 = 0; a metric-dependent one, -(1/4) G11 cos k1 cos k2 cos 2k1 e3 x F, is local and cancels the (11)/(12) clash at second order, so the no-go concerns the plain principle. So no Clifford walk family started from the free walk answers every uniform metric with minus half its own stress beyond first order; on diagonal metrics it does (block 185), and the spectra (block 187) are unaffected. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_for_shears_no_walk_answers_every_uniform_metric_with_minus_half_its_stress_2026_09_27.py
---

# For shears no walk answers every uniform metric with minus half its stress beyond first order: the flows fail to commute by a rotation

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 69 and 139 as landed; blocks 181, 184, 185 and 187 are pushed and placed, and the facts used from them are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 69 and 139 as landed on main (the two-step coupling to a uniform strain of any form, and the staggered mass) and asks whether the walk itself, not only its energies, can answer every uniform metric with minus half its own stress; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 185 (pushed) showed that on diagonal stretches the walk's response to a further stretch is minus half its own symmetric stress, exactly under block 184's rule. Block 187 (pushed) extended the free-particle law for the energies to every uniform metric, shears included. That left open whether the walk itself, as a matrix, can answer shears the same way.

- **T1: every Clifford walk satisfies the book identities.** Block 181's construction works for every walk whose square is a number, with hops of any form. Any divided-difference decomposition of `h − h′` and `h² − h′²` gives an energy current `P^s` whose own current `K^s` is symmetric, exactly. For hermitian densities the decomposition must also have the pair-exchange symmetry. Block 184 T7's per-axis divided differences have it; for hops that depend on several momenta, one is not exhibited here. For decompositions continuous at `q = 0`, on single waves `K^s_ab = ¼(∂_ah ∂_bW + ∂_bh ∂_aW)`.
- **T2: at first order the principle is block 69's coupling.** The rule "respond to a further metric change with minus half your stress", started from the free walk, reproduces block 69's two-step coupling for every strain component, with `B = −(g − 1)/2`.
- **T3: beyond first order, diagonal and shear responses clash.** The response to `g₁₁` and the response to `g₁₂` do not commute at second order. Their mismatch is `¼ cos k₁ cos k₂ cos 2k₁ (sin k₂, −sin k₁, 0)`. That is orthogonal to the walk's Clifford vector, so it rotates the walk without changing any energy. The two diagonal responses commute.
- **T4: moving the metric's indices does not help.** The mismatch is not a constant-coefficient combination of the first-order responses, which is all an index placement could add at this order.
- **T5: rotation terms.** A rotation about the normal axis that does not depend on the metric, `α(k) e₃ × F` in the shear response, would need `∂₁α = −cos k₂ cos 2k₁/(2 sin k₁)`. That has a logarithm at `k₁ = 0`, so no continuous `α` exists. A metric-dependent rotation, `−¼G₁₁ cos k₁ cos k₂ cos 2k₁ e₃ × F` in the shear response, is local and cancels the `(11)/(12)` clash at second order. So the no-go concerns the plain principle.

In plain terms: the walker can keep exact books whatever its hopping, as long as its energy squared is a plain number. And for plain stretches it can respond to the lattice's lengths by its own stress, as a free particle would. For slanted stretches it can do so to first order, where the answer is the coupling already landed. At second order, stretching then slanting and slanting then stretching disagree, by a twist of the walk that leaves every energy alone. So the energies are fixed for every stretch (block 187), but the walk is not.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 69 and 139 are used as landed on main. Blocks 181, 184, 185 and 187 are pushed and placed; the facts used from them are re-derived (runner B1, B2, C1).

- **The coupling** (block 69), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`"; and "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
- **The staggered mass** (block 139), quoted: "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`".
- **Clifford walks.** `h(k) = Σ_a F_a(k)X_a + μΓ`, with `X_a` and `Γ` mutually anticommuting hermitian involutions and hops `F_a` of any form. `W = h² = |F|² + μ²` is a number.
- **Pair symbols** (block 181, pushed). `q = k − k′` and `w_b = 1 − e^{−iq_b}`. A divided-difference decomposition writes `F_a − F′_a = Σ_b w_bD_ab` and `W − W′ = Σ_b w_bV_b`. It exists for trigonometric polynomials, since both vanish at `q = 0` (Hadamard's lemma in its periodic form), and it is not unique. Set `Â_b = (i/2)Σ_aD_abX_a`, `f_b = iV_b`, `P̂^s_j = ½(½f_j + h′Â_j + Â_jh)` and `K̂^s_{aj} = ½(Â_af_j + Â_jf_a)`.
- **The stress-response principle** (supplied; block 185's on the diagonal). `∂h/∂g_ab = −½K^s_ab(k, k)`, with the off-diagonal variable `g_ab = g_ba` counting both entries. On the Clifford vector: `∂F/∂g_aa = −¼∂_aF ∂_aW` and `∂F/∂g_ab = −¼(∂_aF ∂_bW + ∂_bF ∂_aW)`.

In the literature, a system of flows has a common solution through every initial point only if the flows commute (Frobenius). A symmetric stress built from a conserved current's current by adding divergence-free terms is Belinfante's construction. This note uses neither as authority.

## Domain qualifications

- Uniform metrics; the stress-response principle as stated; expansion to second order at the free walk.
- Principles with an additional rotation term are not examined.

## Theorem T1 — every Clifford walk satisfies the book identities

*Statement.* For every Clifford walk and every decomposition, `Σ_j w_jP̂^s_j = i(êh − h′ê)` with `ê = ½(h + h′)`, and `Σ_a w_aK̂^s_{aj} = i(P̂^s_jh − h′P̂^s_j)`, with `K̂^s` symmetric. The densities are hermitian pair symbols when the decomposition is symmetric under exchanging the two waves; that is exhibited for per-axis hops (block 184 T7), not here in general. For decompositions continuous at `q = 0`, on single waves `Â_b → ½∂_bh` and `f_b → ∂_bW`, so `P^s_j = E∂_jE` and `K^s_ab = ¼(∂_ah ∂_bW + ∂_bh ∂_aW)`.

*Proof.*
- The algebra of block 184 T7 uses only `Σ_bw_bÂ_b = (i/2)(h − h′)`, `Σ_bw_bf_b = i(h² − h′²)` and `h²` a number. Both sums hold by construction.
- Runner B1 checks both identities with `4 × 4` involutions, arbitrary hop values and six free entries in each decomposition.
- For decompositions continuous at `q = 0`, the single-wave limits are the first-order terms of the decompositions, which are unique; runner B2 records the resulting stress formula. ∎

## Theorem T2 — at first order the principle is block 69's coupling

*Statement.* At the free walk, `F = sin k`, the principle's first-order responses are `∂F/∂g_aa = −½ sin k_a cos² k_a e_a` and, for `a ≠ b`, `∂F/∂g_ab = −½ cos k_a cos k_b (sin k_b e_a + sin k_a e_b)`. These are block 69's `∂H/∂B` with `B = −(g − 1)/2`.

*Proof.* Runner C1, all six components. ∎

## Theorem T3 — beyond first order, diagonal and shear responses clash

*Statement.* At the free walk, the mixed second derivatives of the `(11)` and `(12)` flows satisfy

`∂_{g₁₂}∂_{g₁₁}F − ∂_{g₁₁}∂_{g₁₂}F = ¼ cos k₁ cos k₂ cos 2k₁ (sin k₂, −sin k₁, 0)`.

This is not zero, and it is orthogonal to `F`. It equals `−¼ cos k₁ cos k₂ cos 2k₁ (e₃ × F)`: a rotation about the axis normal to the shear plane, by an angle that depends on `k`. The `(11)` and `(22)` flows commute. The `(12)` and `(13)` flows also clash: `∂_{g₁₃}∂_{g₁₂}F − ∂_{g₁₂}∂_{g₁₃}F = ¼ cos 2k₁ cos k₂ cos k₃ (0, sin k₃, −sin k₂)`, again orthogonal to `F`.

*Proof.*
- For flows `∂F/∂t_i = Φ_i[F]` with no explicit `t`, a common twice-differentiable solution needs `δΦ_i[F](Φ_j[F]) = δΦ_j[F](Φ_i[F])` along it, and in particular at `t = 0`.
- Runner D1 computes both sides symbolically at `F = sin k`. ∎

The mismatch leaves `|F|²`, and hence every energy, unchanged. That matches block 187, where the energies alone obey commuting flows.

## Theorem T4 — moving the metric's indices does not help

*Statement.* If the principle carries an explicit dependence on `g`, say through the placement of indices, `∂F/∂g_ab = −½M_ab^{cd}(g)K^s_cd` with `M(1)` the identity, then the mixed derivatives at `g = 1` change only by constant-coefficient combinations of the six first-order responses. No such combination equals the mismatch.

*Proof.* The extra terms are `∂M·K^s` at `g = 1`. Runner E1 sets the mismatch equal to a general combination at 64 exact rational points, and the linear system is inconsistent. ∎

## Theorem T5 — rotation terms

*Statement.* Replace the shear flow by `∂F/∂g₁₂ = −¼(∂₁F ∂₂W + ∂₂F ∂₁W) + α(k) e₃ × F`, a rotation about the axis normal to the shear plane. At the free walk, the second-order mismatch becomes

`¼ cos k₁ cos k₂ cos 2k₁ (sin k₂, −sin k₁, 0) + ½ sin k₁ cos k₁ ∂₁α (sin k₂, −sin k₁, 0)`.

It vanishes iff `∂₁α = −cos k₂ cos 2k₁/(2 sin k₁)` wherever `cos k₁ ≠ 0`. Near `k₁ = 0` this is `−cos k₂/(2k₁) + O(k₁)`, so `α` would contain `−(cos k₂/2) log|k₁|`. No continuous `α` on the zone exists.

*Proof.* Runner F1: the mismatch formula symbolically, for a generic function `α`, and the leading behaviour at `k₁ = 0`. ∎

A metric-dependent rotation does better. The mismatch is `−¼ cos k₁ cos k₂ cos 2k₁ (e₃ × F)`. Adding `ρ(k) G₁₁ e₃ × F` to the `(12)` flow changes the mismatch at `g = 1` by `−ρ e₃ × F`. So `ρ = −¼ cos k₁ cos k₂ cos 2k₁`, a trigonometric polynomial and hence a local rotation generator, cancels it at second order (runner F2). Whether local metric-dependent rotations can repair every pair of flows at every order is not examined.

## Remark — rotation terms always exist; locality is the question

For any Clifford vector `F`, the component of each response along `F` is fixed: `F·Φ_ab = −⅛(2 − δ_ab)W_aW_b = ½∂W/∂g_ab`, which is block 187's spectral law (runner D2). So any smooth family realising block 187's spectrum, for example block 187 T6's, obeys `∂F/∂g_ab = Φ_ab[F] + δ_ab`, with `δ_ab` orthogonal to `F`: a rotation. Its flows commute, since they are the derivatives of one family. So rotation terms that restore compatibility exist. What remains is whether one can be local at every order. T5 shows that a metric-dependent local rotation repairs the `(11)/(12)` clash at second order.

## What this settles and what it does not

- **Settled.**
  - Symmetric books exist for every Clifford walk (T1). So on the coupling axis, "books" constrains nothing by itself. What constrains is how the books meet the coupling to lengths: blocks 184 and 185.
  - The stress-response principle is block 69's coupling at first order for every strain (T2). It extends exactly on diagonal metrics (block 185), but not to shears beyond first order (T3, T4).
- **For the third column (the coupling axis).** For uniform metrics the energies are fixed by the free-particle law (block 187). The walk off the diagonal is not fixed by the stress response. It needs a further supplied rule, for example a rotation term.
- **Not settled.**
  - Principles with rotation terms in every flow, `∂h/∂g_ab = −½K^s_ab + i[Ω_ab, h]`. Such terms exist (Remark), and a local one repairs the `(11)/(12)` clash at second order (T5). Whether local ones work for every pair and order is open.
  - Higher orders, and non-uniform metrics.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 187 (pushed): a local walk realising the spectrum off the diagonal is open"
source_of_blocker_text: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; a principle with a rotation term"
conditional_surface_status: "exact within blocks 69 and 139, at second order at the free walk, for the stated principle"
hypothetical_axiom_status: "the principle is supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling.
  - Block 139 (landed): the staggered mass, whose square is a number.
  - Block 181 (pushed): the pair construction for the free walk.
  - Block 184 (pushed): its extension to per-axis walks.
  - Block 185 (pushed): the principle on the diagonal.
  - Block 187 (pushed): the energies for every metric.
- **In the literature.**
  - Frobenius's integrability condition for commuting flows.
  - Belinfante's symmetric stress.
  - Hadamard's lemma for functions vanishing on a subspace.
  - None is used as authority.
- **New here.**
  - The books for every Clifford walk (T1).
  - The principle's first order is block 69's coupling for every component (T2).
  - The second-order clash, a rotation at fixed energy (T3), robust to index placement (T4) and to the simplest rotation term (T5).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: whether the walk, not only its energies, answers every uniform metric with minus half its stress. The obligations are:
- (O1) the premises (A3);
- (O2) the books for every Clifford walk (B1, B2);
- (O3) the first order (C1);
- (O4) the second-order clash (D1);
- (O5) robustness to index placement (E1);
- (O6) the simplest rotation term (F1).

## No-Go Discipline Gate

The note's negative sentence: no Clifford walk family, started from the free walk, obeys the stress-response principle for both a diagonal and a shear component through second order, even with a constant-coefficient index placement.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *Another decomposition.* The single-wave stress does not depend on it (T1). ATTEMPTED; closed.
2. *Index placement.* T4. ATTEMPTED; closed at this order.
3. *Another starting walk.* Only the free walk is examined. The flows are autonomous, so the mismatch at `g = 1` depends only on the walk there; any family starting from the free walk inherits the clash.
4. *A rotation term.* A metric-independent one fails; a metric-dependent local one repairs the `(11)/(12)` clash at second order (T5). Every pair and higher orders are not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the principle, the counting of the off-diagonal variable, and the second-order expansion.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling for any strain | yes (quoted, A3; C1) |
| block 139 (landed) | the square is a number | yes (quoted, A3) |
| blocks 181, 184, 185, 187 (pushed) | the pair construction, the principle, the spectra | re-derived (B1, B2, C1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "every Clifford walk keeps the books; the principle is block 69 at first order and clashes for shears at second order" | executed: the pair identities, generic | executed: the single-wave stress, the first order | executed: the mixed derivatives | executed: the span test | not executed: a rotation term; higher orders |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The mismatch is only a rotation at fixed energy, so it is unobservable."
  - *Reply:* A rotation of the Clifford vector that depends on `k` changes the walk's eigenvectors, and so its currents and its couplings. It is not a relabelling. The energies are indeed unaffected (block 187).

### N8 — Cross-cycle echo
- Block 69: the first order.
- Block 185: the principle on the diagonal.
- Block 187: the energies for every metric.
- This note: the walk for shears is not fixed by the principle beyond first order.

## Falsifiers

- A Clifford walk family obeying the principle for `g₁₁` and `g₁₂` through second order.
- A decomposition for which T1's identities fail.

## Boundaries and non-claims

- Uniform metrics; the stated principle; second order at the free walk.
- The principle is supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 69 and 139 (landed), quoted. Blocks 181, 184, 185 and 187 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - integrability of commuting flows (Frobenius);
  - Hadamard's lemma, periodic form;
  - anticommuting involutions;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Before writing.** Origin was re-fetched. Blocks 69 and 139 were read as landed, and blocks 181 and 184–187 on their branches. T1's generality was noticed while checking block 184 T7: the algebra never used the per-axis form.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.
- **Second version.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error. It re-derived T3 by an independent formal expansion. Its corrections are applied:
  - `B = −(g − 1)/2`, not `−g/2`;
  - T1's hermiticity and continuity qualifiers;
  - "started from the free walk" in the claim;
  - the `(12)`/`(13)` clash is recorded.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_for_shears_no_walk_answers_every_uniform_metric_with_minus_half_its_stress_2026_09_27.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
