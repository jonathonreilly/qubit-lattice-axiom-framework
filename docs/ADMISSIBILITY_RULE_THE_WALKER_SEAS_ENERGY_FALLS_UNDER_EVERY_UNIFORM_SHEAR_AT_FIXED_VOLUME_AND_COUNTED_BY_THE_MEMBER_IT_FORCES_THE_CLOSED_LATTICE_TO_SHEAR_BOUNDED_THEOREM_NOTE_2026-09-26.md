---
claim_id: admissibility_rule_the_walker_seas_energy_falls_under_every_uniform_shear_at_fixed_volume_and_counted_by_the_member_it_forces_the_closed_lattice_to_shear_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 62's framed walk and its uniform frames (H(k)^2 = g^{ij} s_i s_j, s_j = sin k_j), block 139's staggered mass, and blocks 147 and 148 as landed (the zero of energy the member sees; the supplied homogeneous action L = -8 alpha V sum_{i<j} lambdadot_i lambdadot_j / w - w m, V = ell_1 ell_2 ell_3, ell_i = e^{lambda_i}): (T1) exact: under a uniform symmetric frame E the filled lower band has energy per site -<(|E s|^2 + mu^2)^{1/2}>, mu = 0 for block 62's walk and mu > 0 for the staggered mass, and on dilations -I (det g)^{-1/6} at mu = 0; (T2) exact to second order: at fixed volume per site the change is a negative definite quadratic form in the traceless strain, for every mu >= 0, with coefficients bounded by -(B + 5A)/8 and -(A + B)/2 in terms of the positive zone averages A = <s1^2 s2^2/R^3>, B = <s1^4/R^3>, R = (|s|^2 + mu^2)^{1/2}; (T3) exact at every size: for unequal lengths at fixed volume the energy per site is strictly below its value at equal lengths, for every mu >= 0; (T4) exact within block 148's supplied action with the sea's energy as its content m (block 147's first reading, m < 0): the constraint 8 alpha V sum_{i<j} lambdadot_i lambdadot_j = m admits no static state and no motion with equal rates, so the lattice must shear; and the sea's force pushes unequal lengths further apart: d/dt[8 alpha V (lambdadot_i - lambdadot_j)] = dm/dlambda_j - dm/dlambda_i, which has the sign of lambda_i - lambda_j. The landed member's R_1 and R_2 vanish on uniform strains, so it has no uniform-strain energy to oppose this. Measured above the sea (block 147's second reading), none of this arises. A harvest of probe #9198's exact part (Claude Opus 5.5, the supervisor's own model family), with the supervisor's extensions (the massive sea, the exact volume constraint, T3 and T4); not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_walker_seas_energy_falls_under_every_uniform_shear_at_fixed_volume_and_counted_by_the_member_it_forces_the_closed_lattice_to_shear_2026_09_26.py
---

# The walker sea's energy falls under every uniform shear at fixed volume, and, counted by the member, it forces the closed lattice to shear

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact, within block 62's framed walk, block 139's staggered mass and blocks 147 and 148 as landed; a harvest of probe #9198's exact part with the supervisor's extensions; not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 62, 139, 147 and 148 as landed on main (the framed walk, the staggered mass, the zero of energy the member sees, and the closed lattice's homogeneous action); it reports how the walker sea's energy responds to a uniform shear, and what that does to the closed lattice if the member counts it; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 147 (landed) left the owner a reading question: does the member count the walker sea's energy, or only energy above the sea? If it counts the sea, a closed lattice that stretches alike in every direction bounces or cannot move. Probe #9198 computed the sea's energy under a uniform strain. This note harvests that result's exact part and extends it.

- **T1: the sea's energy under a uniform frame.** Per site it is `−⟨(|Es|² + μ²)^{1/2}⟩`, with `μ = 0` for block 62's walk and `μ > 0` for block 139's staggered mass. A dilation gives `−I(det g)^{−1/6}` at `μ = 0`, with `I = ⟨|s|⟩`.
- **T2: every uniform shear lowers it, at second order.** At fixed volume per site the change is a negative definite quadratic form in the traceless strain, for every `μ ≥ 0`.
- **T3: at every size, for unequal lengths.** Stretch the lattice unequally along its axes at fixed volume. The sea's energy per site is then strictly below its value at equal lengths, for every `μ ≥ 0`.
- **T4: counted by the member, the sea forces the closed lattice to shear.** Put the sea's energy into block 148's homogeneous action as the content, which is block 147's first reading. Then:
  - there is no static state and no motion with equal rates;
  - the lattice must stretch unequally;
  - the sea's force pushes unequal lengths further apart.

  The landed member has no energy for uniform strains, so nothing in it opposes this.

In plain terms: the filled sea of walkers is a negative energy that grows in size when the lattice is squeezed along one axis and stretched along another. If the member counts that energy, the lattice cannot stay alike in every direction. It must shear, and the shear feeds itself. If the member counts only energy above the sea, the sea drops out and none of this happens. This is a second cost of the first reading, after block 147's bounce.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, the frame, the mass, the member and its homogeneous action are supplied clauses. Nothing is adopted.
- **The framed walk** (block 62 as landed). For a uniform real frame `E`, `H(k) = Σ_j (E^j·σ) sin k_j`, and `H(k)² = g^{ij}s_is_j`, with `s_j = sin k_j` and `g^{−1} = EᵀE`. The metric is `g = δ + h`. A symmetric frame `E = 1 − h/2` gives `g^{−1} = (1 − h/2)²`; a diagonal one, `E_j^j = 1/ℓ_j`, gives `g_jj = ℓ_j²`.
- **The staggered mass** (block 139 as landed). It adds `μ` to the band energies as `±(|Es|² + μ²)^{1/2}`, with the frame acting on the hops, as in block 150 T4 (landed).
- **The sea.** Every lower-band state is filled. `⟨·⟩` is the zone average, and `R = (|s|² + μ²)^{1/2}`.
- **The member's energy for uniform strains** (block 62). `R₁ = p²tr h − pᵀhp` and `R₂` are quadratic in the symbol `p`, so both vanish on uniform strains.
- **The homogeneous action** (block 148 as landed). `L = −8αVΣ_{i<j}λ̇_iλ̇_j/w − wm`, with `ℓ_i = e^{λ_i}`, `V = ℓ₁ℓ₂ℓ₃`, and `w` varied before `w = 1`. It is supplied, with the owner's review scoping.
- **The zero of energy** (block 147 as landed). Its first reading counts the sea's energy as content. Its second counts only energy above the sea.
- **Standard imports, named at definition level.** Convexity of the logarithm of a sum of exponentials; a positive sum of log-convex functions is log-convex, and so is its square root; the inequality of Cauchy and Schwarz; exact symbolic arithmetic.

## Theorem T1 — the sea's energy under a uniform frame

*Statement.* Under a uniform symmetric frame `E`, the sea's energy per site is `−⟨(|Es|² + μ²)^{1/2}⟩`. At `μ = 0`, a dilation `E = c·1` gives `−cI = −I(det g)^{−1/6}`.

*Proof.* The bands are `±(|Es|² + μ²)^{1/2}` (block 62 T1(a), block 139), and the sea fills the lower one. For `E = c·1`, `det g = c^{−6}`. ∎

Block 147's statement that no constant energy per unit volume arises is the same fact: `−I(det g)^{−1/6}` is no constant plus a multiple of `(det g)^{1/2}` (probe #9198, and runner B4).

## Theorem T2 — every uniform shear lowers it, at second order

*Statement.* Write `h = h_T + (τ/3)·1`, with `h_T` traceless, and hold the volume per site fixed: `det E = 1`. Then the sea's energy per site changes by
`Q(h_T) = (−I_μ/12 + A/4)·tr h_T² + ((B − 3A)/8)·Σ_i (h_T)_ii² + O(h³)`,
with `I_μ = ⟨|s|²/R⟩`, `A = ⟨s₁²s₂²/R³⟩` and `B = ⟨s₁⁴/R³⟩`. `Q` is negative definite for every `μ ≥ 0`. Its diagonal coefficient is at most `−(B + 5A)/8`, and its off-diagonal one at most `−(A + B)/2`.

*Proof.*
- Pointwise, `−(|Es|² + μ²)^{1/2} = −R + s·hs/(2R) − s·h²s/(8R) + (s·hs)²/(8R³) + O(h³)` (runner B1).
- The zone average is invariant under the cube's signed permutations of `s`. So `⟨s_is_j/R⟩ = δ_ijI_μ/3`, and `⟨s_is_js_ks_l/R³⟩ = A(δ_ijδ_kl + δ_ikδ_jl + δ_ilδ_jk) + (B − 3A)δ_ijkl` (runner B2).
- Fixed volume, `det(1 − h/2) = 1`, gives `tr h = −tr h_T²/4 + O(h³)` (runner B3). So the first-order term `(I_μ/6)tr h` adds `−(I_μ/24)tr h_T²`.
- Collecting terms gives `Q`.
- Pointwise `|s|⁴/R³ ≤ |s|²/R`, so `I_μ ≥ 3B + 6A`. With `A, B > 0`, the diagonal coefficient `−I_μ/12 + B/8 − A/8` is at most `−(B + 5A)/8`, and the off-diagonal coefficient `2(−I_μ/12 + A/4)` is at most `−(A + B)/2` (runner B3). ∎

At `μ = 0` and first order in the volume, this is probe #9198's formula: `−(3A/8)Σh_ii² − (B/4)Σ_{i<j}h_ij²` on traceless `h`.

## Theorem T3 — at every size, for unequal lengths

*Statement.* Take a diagonal frame `ℓ_i = e^{λ_i}` with `Σλ_i = 0`, not all zero. Then `−⟨(Σ_i e^{−2λ_i}s_i² + μ²)^{1/2}⟩ < −⟨R⟩` for every `μ ≥ 0`.

*Proof.*
- For fixed `s`, `f(λ) = (Σ_i e^{−2λ_i}s_i² + μ²)^{1/2}` is convex. With `b_i = e^{−2λ_i}s_i²` and `S = Σb + μ²`, its Hessian times `S^{3/2}` is `2S·diag(b) − bbᵀ`. For any `v`, `2SΣb_iv_i² − (Σb_iv_i)² ≥ (2S − Σb)Σb_iv_i² ≥ 0`, since a weighted mean of squares is at least the square of the weighted mean (runner C1).
- It is strictly convex along directions with `Σv_i = 0`, wherever every `s_i ≠ 0`, which is almost everywhere. Equality needs `v_i` constant on the support of `b`.
- The zone average is invariant under permuting the axes, so the averaged `F(λ) = ⟨f(λ)⟩` is strictly convex on `Σλ = 0` and permutation-symmetric.
- Hence `F(λ) > F(λ̄) = F(0)`, where `λ̄` is the average of `λ` over the six permutations, which is `0` on `Σλ = 0`. ∎

## Theorem T4 — counted by the member, the sea forces the closed lattice to shear

*Statement.* In block 148's action take `m = N·ε_sea(λ) < 0`, the sea's energy (block 147's first reading), with `N` sites. Then:
- (a) the constraint `8αVΣ_{i<j}λ̇_iλ̇_j = m` has no static solution, and no solution with equal rates `λ̇_1 = λ̇_2 = λ̇_3`. Every solution has `Σ_{i<j}λ̇_iλ̇_j < 0`, so the lengths stretch unequally;
- (b) the length equations are `d/dt[8αV(S − λ̇_k)] = m + ∂_km`, with `S = Σλ̇_i`. For two axes, `d/dt[8αV(λ̇_i − λ̇_j)] = ∂_jm − ∂_im`. At `λ_i > λ_j` with the third length fixed, `∂_jm − ∂_im` has the sign of `λ_i − λ_j`, so the force pushes the lengths apart;
- (c) the landed member's `R₁` and `R₂` vanish on uniform strains, so its potential adds nothing to (b).

Under block 147's second reading, energy above the sea, `m` loses the sea's part, and (a)–(b) do not arise from it.

*Proof.*
- (a) `α > 0`, `V > 0` and `m < 0` give `Σ_{i<j}λ̇_iλ̇_j < 0`. Equal rates give `3λ̇² ≥ 0`, and a static state gives `0`.
- (b) This is the variation of `L`, using the constraint for `8αVΣ_{i<j}λ̇_iλ̇_j`. In the difference of two length equations the `m` terms cancel, leaving `∂_jm − ∂_im`.
- For the sign, `∂_km = N⟨e^{−2λ_k}s_k²/f⟩`, with `f` as in T3. Take `λ = (a + δ/2, a − δ/2, c)` and `D(δ) = ∂_2m − ∂_1m = N⟨(b₂ − b₁)/f⟩`, with `b₁ = e^{−2a−δ}s₁²` and `b₂ = e^{−2a+δ}s₂²`. Then `D(0) = 0` by the swap of axes 1 and 2. `D` is strictly increasing in `δ`, because `∂_δD = N⟨[(b₁ + b₂)f² − (b₂ − b₁)²/2]/f³⟩ > 0`: in that bracket, `(b₂ − b₁)² ≤ (b₁ + b₂)² ≤ (b₁ + b₂)f²` (runner D1). So `D` has the sign of `δ = λ₁ − λ₂`.
- (c) Block 62's formulas at `p = 0` (runner D2). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 147 (landed): which zero of energy does the member see? Counting the sea, a closed lattice bounces or cannot move"
source_of_blocker_text: block 147's reading question; decision-record addenda 39 and 43
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the q^2 part of the sea's response and its relabelling (non-)invariance, exactly (probe #9198's floating-point part); the sea under one record per site; an other-family referee"
conditional_surface_status: "uniform frames; block 148's supplied homogeneous action for T4; block 147's first reading"
hypothetical_axiom_status: "the walk, the frame, the mass, the member and its homogeneous action are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 62: the framed walk and the member's `R₁`, `R₂`.
  - Block 139: the staggered mass.
  - Block 147: the zero of energy, and the bounce with equal lengths.
  - Block 148: the homogeneous action with unequal lengths.
- **Block 150 T4 (landed 2026-09-26).** The sea's formal adiabatic inertia, positive and without a dilation part. This note concerns its energy, not its inertia.
- **Probes.** #9198 (Claude Opus 5.5 worker `w-macbookpro9927a-j5403`, the supervisor's own model family; not refereed by another family) found T1 at `μ = 0`, the second-order formula on traceless strains at first order in the volume, and the negative definiteness. Its floating-point findings are not used here: the `q²` part is not relabelling-invariant, and the transverse stiffness and `α/K` values.
- **In the literature.** The vacuum energy of a filled lattice band under strain; convexity of log-sum-exp. Reference only.
- **New here:**
  - the massive sea;
  - the exact volume constraint, which adds `−(I_μ/24)tr h_T²`;
  - T3, at every size;
  - T4, the consequence in block 148's action.
- **Provenance.** A same-family harvest plus the supervisor's own extensions. No other model family has refereed it.

## Exact target and obligation graph

Target: what counting the sea's energy does to the closed lattice beyond equal stretches. The obligations are:
- (O1) the energy under uniform frames (T1: runner B1, B4);
- (O2) second order at fixed volume (T2: runner B1–B3);
- (O3) every size for unequal lengths (T3: runner C1);
- (O4) the consequence in block 148's action (T4: runner D1, D2).

The strongest input: block 148's supplied action, as landed and scoped by the owner's review.

## No-Go Discipline Gate

The note's negative sentences: at fixed volume no uniform shear raises the sea's energy; with the sea counted, block 148's closed lattice has no static state and no motion with equal rates.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Some shear direction raises the energy.* The form is negative definite on every traceless strain (T2; runner B3). ATTEMPTED.
2. *The mass stabilizes it.* The bounds hold for every `μ ≥ 0` (T2, T3). ATTEMPTED.
3. *Higher orders reverse it for large strains.* For unequal lengths the statement holds at every size (T3; runner C1). ATTEMPTED.
4. *The member's potential opposes the shear.* `R₁` and `R₂` vanish on uniform strains (T4(c); runner D2). ATTEMPTED.
5. *The constraint allows a static or equal-rate state.* `m < 0` forbids both (T4(a)). ATTEMPTED.

Scope left open: off-diagonal shears at every size (only second order here); long-wavelength shears (`q ≠ 0`); the sea under one record per site; the full lattice beyond the homogeneous action.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical". The first reading of block 147 is stated as the premise of T4. No hidden condition was found.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 62 (landed) | the framed walk; `R₁`, `R₂` | yes (restated) |
| block 139 (landed) | the staggered mass | yes, for `μ > 0` |
| blocks 147, 148 (landed) | the reading; the homogeneous action | yes, for T4 (restated) |
| probe #9198 (unrefereed, same family) | T1–T2 at `μ = 0` | yes (re-derived here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no uniform shear raises the sea's energy at fixed volume; counted, the sea forces shear" | executed: the pointwise expansion | executed: the cube-averaged fourth moments | executed: the volume constraint and the definiteness bounds | executed: the convexity identity; the force's monotonicity | every uniform frame; block 148's action |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A negative energy that falls further is just a deeper vacuum. Why should it drive anything?"
  - *Reply:* Only because block 147's first reading counts it as the member's content. Then block 148's constraint needs `Σ_{i<j}λ̇_iλ̇_j < 0`. Under the second reading the sea's energy is subtracted, and nothing is driven.

### N8 — Cross-cycle echo
- Block 147: the sea's energy thins out as the lattice grows alike; counted, the lattice bounces or cannot move.
- Block 148: unequal stretches.
- This note: counted, the sea forbids alike stretches and drives unequal ones.

## Falsifiers

- A traceless uniform strain that raises the sea's energy at second order at fixed volume.
- Unequal lengths at fixed volume with the sea's energy at or above its value at equal lengths.
- A solution of block 148's constraint with `m < 0` and equal rates.

## Boundaries and non-claims

- Uniform frames; off-diagonal shears only at second order; block 148's supplied homogeneous action for T4; block 147's first reading for T4.
- Long-wavelength shears, the sea under one record per site, and the full lattice are not covered.
- Probe #9198's floating-point findings are not used.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 62, 139, 147 and 148 (landed), restated. Block 150 T4 (landed), cited as context.
- Named standard imports, at definition level: convexity of log-sum-exp and of log-convex functions; the inequality of Cauchy and Schwarz; exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, 2026-09-26, during the owner's 12-hour campaign of that day.
- **Provenance.** T1 at `μ = 0` and T2 at first order in the volume are probe #9198's (Claude Opus 5.5, the supervisor's own model family). The supervisor line-checked them and extended them to the massive sea and the exact volume constraint. T3 and T4 are the supervisor's own. No other model family has refereed it.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found blocks 147, 148 and 150 T4, and no other treatment of the sea's shear energy.
- **Independence.** Mutation census: at least one mutation per science family (B, C, D), each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_walker_seas_energy_falls_under_every_uniform_shear_at_fixed_volume_and_counted_by_the_member_it_forces_the_closed_lattice_to_shear_2026_09_26.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
