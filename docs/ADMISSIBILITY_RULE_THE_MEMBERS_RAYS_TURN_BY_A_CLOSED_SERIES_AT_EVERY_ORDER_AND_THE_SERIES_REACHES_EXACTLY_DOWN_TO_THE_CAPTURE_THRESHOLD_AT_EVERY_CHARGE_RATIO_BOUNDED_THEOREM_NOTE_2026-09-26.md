---
claim_id: admissibility_rule_the_members_rays_turn_by_a_closed_series_at_every_order_and_the_series_reaches_exactly_down_to_the_capture_threshold_at_every_charge_ratio_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 110's declared model as landed (the curvature member's exterior chi = 1 + a/r, N = 1 - p/r of a spherical body, and the long-wave ray model of the walk, E = (w/l)|k|, in the continuum exterior, so that rays see the index n = chi^3/N and keep r n sin(psi) = b); exact: (T1) for an index n(u), u = 1/r, analytic at 0 with n(0) = 1, let u(w) be the root of u = w n(u) with u(0) = 0 and R the radius of the series of g(w) = log n(u(w)); if w = u/n(u) rises with positive slope from 0 to 1/b at the turning point and 1/b < R, the turn is chi(b) = sum_k m_k [u^k] n(u)^k b^-k with m_k = 2 int_0^1 y^k (1 - y^2)^(-1/2) dy = sqrt(pi) Gamma((k+1)/2)/Gamma(k/2 + 1), and the series in 1/b has radius exactly R; (T2) for the member n = (1 + a u)^3/(1 - p u), [u^k] n^k = sum_j C(3k, k - j) C(k + j - 1, j) a^(k-j) p^j, which gives block 110 T4's coefficients, the comparator's series at equal charges and block 110 T5's series, and at a fixed first-order turn 4M/b the third-order term (64/3)(42 + 54 rho + 27 rho^2 + 5 rho^3)/(3 + rho)^3 (M/b)^3, rising with the charge ratio rho from 896/27 through 128/3 at rho = 1 to 320/3; (T3) block 110's capture threshold is the one positive root of the discriminant of the turning-point cubic (1 + a u)^3 - b u (1 - p u), where the cubic has the double root 1/r*; (T4) for a, p >= 0 not both zero the member's turn series sums to the turn for every b > b_c, diverges for every b < b_c, and diverges at b = b_c, where the turn grows without bound: its radius is exactly the capture threshold at every charge ratio. A harvest of probe #9231 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9326, Grok); T4 is proved here by a second route through the nonnegative coefficients. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_around_a_body_the_walks_rays_match_the_comparators_at_every_order_exactly_when_its_two_charges_agree_and_they_agree_only_when_hop_energy_balances_the_slowed_clocks_bounded_theorem_note_2026-09-24
runner: scripts/admissibility_rule_the_members_rays_turn_by_a_closed_series_at_every_order_2026_09_26.py
---

# The member's rays turn by a closed series at every order, and the series reaches exactly down to the capture threshold at every charge ratio

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 110's declared continuum exterior and long-wave ray model; a harvest of probe #9231, confirmed by an other-family referee in #9326; nothing adopted or registered; unaudited)

This note works within block 110 as landed on main (the curvature member's exterior fields and the long-wave ray model of the walk, in the continuum exterior of a spherical body); it reports the turn of the rays at every order in closed form and the exact reach of its series; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 110 (landed) showed that around a body, the member's rays see the index `n = χ³/N = (r + a)³/(r²(r − p))`. It gave the turn's series to fourth order and the capture threshold `b_c` against the charge ratio `ρ = p/a = P/Q`. This note, a harvest of a probe result that another model family has confirmed, gives the series at every order and says exactly where it represents the turn.

- **T1: the turn at every order.** Write `u = 1/r`, and let `m_k = 2∫₀¹ yᵏ(1 − y²)^{−1/2} dy = 2, π/2, 4/3, 3π/8, 16/15, …`. For any index regular on the ray's outer branch,

  `χ(b) = Σ_{k≥1} m_k [uᵏ] n(u)ᵏ b^{−k}`.

  The series in `1/b` has the same radius as the series of `log n` along the inverse of `w = u/n(u) = 1/(r n)`.
- **T2: the member's coefficients.**
  - `[uᵏ] nᵏ = Σ_j C(3k, k − j) C(k + j − 1, j) a^{k−j} p^j`.
  - This gives block 110 T4's four coefficients, the comparator's series `4, 15π/4, 128/3, 3465π/64, 3584/5, 255255π/256` (times `(M/b)ᵏ`) at equal charges, and block 110 T5's series.
  - New: at a fixed first-order turn `4M/b`, the third-order term is `(64/3)(42 + 54ρ + 27ρ² + 5ρ³)/(3 + ρ)³ (M/b)³`. It rises with `ρ`, from `896/27` through the comparator's `128/3` at `ρ = 1` to `320/3`.
- **T3: capture by the discriminant.** Block 110's threshold is the one positive root of the discriminant of the turning-point cubic `(1 + au)³ − bu(1 − pu)`. At it the cubic has the double root `1/r*`, the circular ray.
- **T4: the reach of the series.** For `a, p ≥ 0`, not both zero, the series of T1 has these properties:
  - it sums to the turn for every `b > b_c`;
  - it diverges for every `b < b_c`;
  - it diverges at `b = b_c`, where the turn itself grows without bound.

  So its radius is exactly the capture threshold, at every charge ratio.

**Executed.** Every step is checked exactly:
- the moments;
- the inversion identity to order 12;
- an independent direct expansion of the orbit integral to order 5;
- the member's coefficients;
- the discriminant;
- the stationary points of `1/(r n)`;
- the ratios of the exact coefficients up to `k = 81` at four charge ratios.

The last of these is evidence only. Every ratio lies in the window `[b_c(1 − 3/(2k)), b_c)` that a square-root singularity at `1/b_c` produces.

In plain terms: the walker's rays bend around a lump by an amount given by one formula at every order. That formula stops working exactly at the impact distance where rays start being captured, and not before. How far out it works depends on the lump only through the capture distance.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The clocks, the lengths, the walk, the member and the ray model are supplied clauses. Nothing is adopted.
- **Block 110 (landed on main).** Quoted by the runner (A3).
  - T1: the exterior fields `χ = 1 + a/r` and `N = 1 − p/r`, and the index `n = χ³/N`.
  - The invariant `r n sin ψ = b` along each ray.
  - T3: the threshold.
  - T4: the turn to fourth order.
  - T5: the index `e^{κu}`.
  - The model is block 110's declared long-wave ray model in the continuum exterior. It is conditional as landed. No lattice statement is made here.
- **Charges.** `a = Q/4π` and `p = P/4π`, with `ρ = p/a`. A fixed first-order turn means `3a + p = 2M`.
- **The comparator.** Known physics, used as a comparator only: at `a = p = M/2` the index is the comparator's static isotropic index (block 110 T1). Its coefficients here are computed from that index.
- **Names.** The invariant `r n sin ψ` is Bouguer's. The coefficient identity of T1 is the Lagrange–Bürmann inversion formula. The moments are Beta integrals. The fact used in T4, that a power series with nonnegative coefficients is singular at the positive point of its circle, is the Vivanti–Pringsheim theorem. The index `e^{κu}`'s series is Lambert's tree function.

## Domain qualifications

- Throughout, `a, p ≥ 0` are not both zero, and the ray comes in from infinity in the continuum exterior `r > p`, where `N > 0`.
- As in block 110 T3, the body lies inside `r*`. Every ray with `b > b_c` turns at `r₀ > r*`, so it stays in the exterior.
- T1 is stated for indices analytic at `u = 0` with `n(0) = 1`, where `w = u/n(u)` has positive slope from 0 up to the ray's turning point and `n` stays positive there.
- The exact ratio window of T4 is evidence at four charge ratios and `10 ≤ k ≤ 80`. It is not part of the proof.
- These are conditional continuum-ray statements, not a physical gravitational identification.

## Theorem T1 — the turn at every order

*Statement.*
- Let `n(u)` be analytic at `u = 0` with `n(0) = 1`.
- Let `u(w)` be the root of `u = w n(u)` with `u(0) = 0`, `g(w) = log n(u(w))`, and `R` the radius of the power series of `g` at `0`.
- Let a ray come in from infinity with impact parameter `b`. Suppose `w(u) = u/n(u)` has `w′ > 0` and `n > 0` on `[0, u₀]`, where `u₀` is the first root of `w = 1/b` (the turning point).
- If `1/b < R`, then

  `χ(b) = Σ_{k≥1} m_k [uᵏ] n(u)ᵏ b^{−k}`, with `m_k = 2∫₀¹ yᵏ(1 − y²)^{−1/2} dy = √π Γ((k+1)/2)/Γ(k/2 + 1)`.

- The series in `1/b` has radius exactly `R`.

*Proof.*
1. **The orbit integral.** By the invariant `r n sin ψ = b`, with `tan ψ = r dφ/dr` and `u = 1/r`, `(du/dφ)² = n²/b² − u²`. So `χ + π = 2∫₀^{u₀} du/√(n²/b² − u²)`, as in block 110 T4.
2. **The substitution.**
   - `w = u/n(u)` rises from `0` to `1/b` on `[0, u₀]`, so its inverse there is the branch `u(w)`, analytic on `[0, 1/b]`.
   - `n²/b² − u² = n²(1/b² − w²)`.
   - From `log u = log w + g(w)`, `du/n = (1 + w g′(w)) dw` (B1).
   - Hence `χ + π = 2∫₀^{1/b} (1 + w g′(w)) dw/√(1/b² − w²) = π + 2∫₀^{1/b} w g′(w) dw/√(1/b² − w²)`.
3. **The coefficients.** `[wᵏ] g = (1/k)[uᵏ] nᵏ`. This is the inversion formula named under the premises, imported at definition level: with `H = log n`, `[wᵏ] H(u(w)) = (1/k)[u^{k−1}] H′(u) n(u)ᵏ`, and `H′nᵏ = (1/k)(nᵏ)′`. It is checked exactly to order 12 on five random rational indices and on the member (B3).
4. **Term by term.**
   - For `1/b < R`, the series `w g′(w) = Σ k λ_k wᵏ`, with `λ_k = (1/k)[uᵏ]nᵏ`, sums uniformly on `[0, 1/b]`. It equals the branch's `w g′` there, since both are analytic near the segment and agree near `0`.
   - Each term gives `2∫₀^{1/b} wᵏ dw/√(1/b² − w²) = m_k b^{−k}`.
   - The moments are integrated exactly for `k ≤ 8` (B2).
5. **The radius.**
   - `2/(k + 1) ≤ m_k ≤ π`, since `1 ≤ (1 − y²)^{−1/2}` and `yᵏ ≤ 1`.
   - So `(k m_k)^{1/k} → 1`, and `Σ m_k k λ_k xᵏ` has the radius of `Σ λ_k xᵏ`, which is `R`.
6. **An independent route (B4).**
   - Expand the orbit integral directly in `1/b` for a generic index `n = 1 + ν₁u + … + ν₅u⁵`, with the turning point `x₀ = n(x₀/b)` as a series.
   - Use the identity `n(εx₀v)² − x₀²v² = (1 − v)x₀²[(1 + v) − T(v)]`. Every term is then an exact rational integral in `tan(θ/2)`.
   - The result gives `m_k [uᵏ]nᵏ` for `k = 1..5`, orders 1–3 are block 110 T4's, and order 4 is `(3π/8)(ν₁⁴ + 12ν₁²ν₂ + 12ν₁ν₃ + 6ν₂² + 4ν₄)`. ∎

## Theorem T2 — the member's coefficients

*Statement.* For `n = (1 + au)³/(1 − pu)`:
- `[uᵏ] nᵏ = Σ_{j=0}^{k} C(3k, k − j) C(k + j − 1, j) a^{k−j} p^j`.
- The first four `m_k [uᵏ]nᵏ` are block 110 T4's `2(3a + p)`, `(3π/2)(5a² + 4ap + p²)`, `(8/3)(42a³ + 54a²p + 27ap² + 5p³)` and `(15π/8)(99a⁴ + 176a³p + 132a²p² + 48ap³ + 7p⁴)`.
- At `a = p = M/2`: `4, 15π/4, 128/3, 3465π/64, 3584/5, 255255π/256` times `(M/b)ᵏ`, for `k = 1..6`.
- For `n = e^{κu}`: block 110 T5's `c_k = √π kᵏ Γ((k+1)/2)/(k! Γ(k/2 + 1)) κᵏ`.
- At a fixed first-order turn (`3a + p = 2M`, `ρ = p/a`):
  - the second-order term is block 110's `6π(5 + 4ρ + ρ²)/(3 + ρ)² (M/b)²`;
  - the third-order term is `(64/3)(42 + 54ρ + 27ρ² + 5ρ³)/(3 + ρ)³ (M/b)³`. Its slope in `ρ` is `384(ρ + 1)(ρ + 2)/(3 + ρ)⁴ (M/b)³ > 0`. It runs from `896/27` (`ρ → 0`) through `128/3` (`ρ = 1`) to `320/3` (`ρ → ∞`).

*Proof.*
- `nᵏ = (1 + au)^{3k}(1 − pu)^{−k}`, and the product of the two binomial series gives the sum (C1, `k ≤ 8`).
- The rest is substitution (C2–C5): `a = 2M/(3 + ρ)`, `p = ρa`, and `[uᵏ] e^{kκu} = (kκ)ᵏ/k!`. ∎

## Theorem T3 — capture by the discriminant

*Statement.*
- The turning points are the roots in `(0, 1/p)` of `E_b(u) = (1 + au)³ − bu(1 − pu)`, since `n(u)/b = u` there.
- `Disc_u E_b = −b²[27a²(a + p)² + (4p³ + 6ap² − 6a²p − 4a³)b − p²b²]`.
  - For `p > 0` the bracket's two roots in `b` have product `−27a²(a + p)²/p² < 0`, so exactly one is positive.
  - For `p = 0` the bracket is linear, with root `27a/4`.
- That positive root is block 110 T3's `b_c/M = 2(ρ + s + 2)³/((ρ + 3)(s + 1)(ρ + s + 1))`, `s² = ρ² + ρ + 1`.
- At `b = b_c` the cubic has the double root `u* = 1/r*`, `r* = a + p + S`, `S = √(a² + ap + p²)`, and `0 < u* < 1/p`.
- Values: `9/2`, `4√7 − 40/7`, `3√3` and `(70 + 26√13)/27` at `ρ = 0, 1/2, 1, 3`, and the limit is `8`.

*Proof.*
- As `b` falls from `∞`, the smallest positive root `u₀(b)` moves continuously until it meets another root. They meet first at a double root, a zero of the discriminant.
- The runner computes the discriminant (D1) and the product of its roots (D2). It reduces the bracket to zero at block 110's closed form using `s² = ρ² + ρ + 1` (D3). It reduces `E_b(u*)` and `E_b′(u*)` to zero using `S² = a² + ap + p²` (D4). The values and limit are D5.
- This route does not re-derive that `b_c` rises with `ρ`. Block 110 T3's derivative argument stands for that. ∎

## Theorem T4 — the series reaches exactly down to capture

*Statement.* For `a, p ≥ 0`, not both zero, the member's turn series `Σ m_k [uᵏ]nᵏ b^{−k}` has these properties:
- (a) it sums to the turn `χ(b)` for every `b > b_c`;
- (b) it diverges for every `b < b_c`;
- (c) it diverges at `b = b_c`, where `χ(b)` grows without bound as `b` falls to `b_c`.

So its radius in `1/b` is exactly `1/b_c`, at every charge ratio.

*Proof (the supervisor's route, through the signs of the coefficients).*
1. **The coefficients are nonnegative.** `λ_k = (1/k)[uᵏ]nᵏ ≥ 0`, because `(1 + au)^{3k}` and `(1 − pu)^{−k}` have nonnegative coefficients (E1). Also `λ₁ = 3a + p > 0`.
2. **The branch is regular below `w*`.**
   - `w = u(1 − pu)/(1 + au)³ = 1/(r n)` has `w′ = q(u)/(1 + au)⁴`, with `q = 1 − 2(a + p)u + apu²`.
   - `q` has roots `u* = 1/(a + p + S)` and `u₋ = 1/(a + p − S)`, where `(a + p)² − S² = ap ≥ 0` (E2). So `q > 0` on `[0, u*)`, and `w` rises there from `0` to `w* = w(u*) = 1/b_c`.
   - On `[0, u*]`, `n` is finite and at least 1, since `u* < 1/p` (D4).
   - So the inverse branch `u(w)` and `g = log n(u(w))` are analytic on a complex neighbourhood of `[0, w*)`. The series `Σ λ_k wᵏ` is `g`'s power series at `0`, since the power series of `u(w)` solves `u = w n(u)` (T1, step 3).
3. **`R ≥ w*`.**
   - By step 1 the series has nonnegative coefficients. So it is singular at `w = R`, the positive point of its circle (the theorem named under the premises).
   - Suppose `R < w*`. Take a thin convex neighbourhood `V` of `[0, R]` on which the branch's `g` is analytic. On the connected set `V ∩ {|w| < R}` the sum agrees with `g`, since the two agree near `0`. So `g` continues the sum analytically across `w = R`, a contradiction.
4. **`R ≤ w*`.**
   - As `w ↑ w*`, `u′(w) = 1/w′(u) → +∞`, since `w′ > 0` on `[0, u*)` and `w′(u*) = 0`.
   - `d log n/du = 3a/(1 + au) + p/(1 − pu) > 0` at `u*` (E3). So `g′(w) → +∞`.
   - If `R > w*`, the sum would be analytic at `w*` with bounded derivative near it, a contradiction. Hence `R = w* = 1/b_c`.
5. **(a) and (b).**
   - For `b > b_c`, `1/b < w*`. The first root `u₀` of `w = 1/b` lies below `u*`, where `w′ > 0`, so T1 applies.
   - For `b < b_c` the power series diverges by the radius.
6. **(c).**
   - At the stationary point `a + p − apu* = S` exactly, so `q′(u*) = −2S` and `w″(u*) = −2S/(1 + au*)⁴ < 0` (E4). Hence `u′(w) ≥ c/√(w* − w)` near `w*` for some `c > 0`, and `g′(w)` has the same kind of bound, with another constant.
   - Near `w*`, `1/b² − w² ≤ 2w*(1/b − w)` and `1/b − w ≤ w* − w`. So the part of T1's integral over `[w* − δ, 1/b]` is at least `c′ log(δ/(w* − 1/b))`, which grows without bound as `1/b ↑ w*`.
   - The terms of the series are nonnegative, and for `b > b_c` it sums to `χ(b)`. Its partial sums at `b_c` bound those at any `b > b_c`, so a finite sum at `b_c` would bound `χ(b)` for all `b > b_c`. Hence the series diverges at `b_c`. ∎

*The probe's route (#9231, refereed in #9326).*
- `u(w)` is a branch of the algebraic curve `w(1 + au)³ = u(1 − pu)`.
- Its finite branch values are `w* = 1/b_c > 0` and `w₋ = w(u₋) < 0`, with `u₋ > 1/p`.
- The principal branch is analytic along the negative axis and simple at `w₋`, so it is single-valued and analytic in the whole disk `|w| < w*`.
- `n` stays finite and nonzero there.
- At `w*` the singularity of `g` is a genuine square root.

The two routes agree.

*Exact evidence (E5, not part of the proof).*
- At `ρ = 0, 1/2, 1, 3` (`M = 1`), every ratio `λ_{k+1}/λ_k` for `10 ≤ k ≤ 80` lies in `[b_c(1 − 3/(2k)), b_c)`.
- The comparison with the surds `9/2`, `4√7 − 40/7`, `3√3` and `(70 + 26√13)/27` is done exactly.
- This window is the one a square-root singularity at `1/b_c` produces: `λ_k ∝ k^{−3/2} b_cᵏ`.

## What this settles and what it does not

- **Settled.** Within block 110's model:
  - the turn at every order, in closed form;
  - the third-order term against the charge ratio;
  - the exact range `b > b_c` in which the series is the turn, at every charge ratio.
- **For landed block 110.** T4's coefficients and T5's series are special cases. T3's threshold is re-derived by another route. No correction is owed.
- **Not settled.**
  - Lattice corrections to the exterior, and finite wave numbers (block 110's N1).
  - Monotonicity of `b_c(ρ)` by the discriminant route. Block 110's derivative argument covers it.
  - Other indices. The same argument applies to any index whose series has nonnegative coefficients. Without that, a complex singularity nearer than capture is not excluded by this route.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 110 as landed: the turn to fourth order and the log-linear completion's radius; the member's series at every order and its reach (probes task the-two-charges-of-the-curvature-member, part b)"
source_of_blocker_text: probes task J:derive:the-two-charges-of-the-curvature-member
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "lattice corrections to the exterior; finite wave numbers"
conditional_surface_status: "exact in the continuum exterior and the long-wave ray model of block 110"
hypothetical_axiom_status: "the member, its number K, the rates of crossing, the ray model and the content are supplied; nothing adopted"
admitted_observation_status: "known physics (its static isotropic index and its turn's series) is a comparator only"
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 110: the index, the turn to fourth order, the capture threshold against `ρ`, and the log-linear completion. The completion's series in `A/b` has radius `1/(ek)`, the capture threshold; that is a refereed probes result.
- **Probes.**
  - #9231, worker `w-jonathonsmac4f50-j1c5e`, Claude Opus 5.5, the supervisor's own model family, found T1–T3 and T4 by the branch-point route. It also re-checked block 110 T2 on new exact `7³` boxes: a balanced content with `P = Q = 5/6`; too-compact content that needs negative rest parts; and one content bond into a held wall, which shifts the two global identities by exactly `−1/20` and `−1/10`. Those box checks are not ported here, since block 110's runner executes the same identities.
  - #9326, worker `w-macbookpro90c72-j4f60`, `grok-4.6`, another model family, refereed it with its own checker: "HIT: confirmed - the curvature member's turn series has radius exactly the capture threshold, and the two charges agree on balanced content away from the walls." It did not rebuild the attempt's floating-point ratio test or its monotonicity grid.
- **In the literature.** The expansion of a ray's turn in an isotropic index in powers of `1/b`, and the comparator's series, are classical. For the comparator (Schwarzschild's index), the closed form of the turn in elliptic integrals and its logarithmic growth near the circular ray are standard. They are named for reference only; nothing is imported from them.
- **New here.**
  - The harvest.
  - T4's second proof, through the nonnegative coefficients (the Vivanti–Pringsheim theorem). It uses only the real stationary point of `1/(r n)`, not the global structure of the branch.
  - The divergence at `b_c` itself.
  - The exact ratio window, in place of the attempt's floating-point extrapolation.
  - The slope of the third-order term.
- **Provenance.** Found by the supervisor's family and confirmed by another family. T4's second route and part (c) are the supervisor's and have no other-family check.

## Exact target and obligation graph

Target: the member's turn at every order, and where its series is the turn. The obligations are:
- (O1) the premises (A3);
- (O2) the closed form (B1–B4);
- (O3) the member's coefficients (C1–C5);
- (O4) capture (D1–D5);
- (O5) the radius (E1–E4, with the evidence E5).

## No-Go Discipline Gate

The note's negative sentences:
- the series diverges for every `b < b_c` and at `b_c`;
- no charge ratio moves the radius off the capture threshold.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A complex singularity nearer than capture.* Excluded by the nonnegative coefficients (step 3). The probe's route excludes it independently. ATTEMPTED.
2. *A removable point at `w*`.* Excluded because `g′` grows without bound (step 4). ATTEMPTED.
3. *Summable at `b_c`.* Excluded by the logarithmic growth of the turn (step 6). ATTEMPTED.

Scope left open:
- lattice corrections;
- finite wave numbers;
- indices whose series have coefficients of both signs.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The continuum exterior and the long-wave ray model are declared, as block 110 declares them.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 110 (landed) | the index, the invariant, T3's threshold, T4's coefficients, T5's series | yes (quoted, A3) |
| probe #9231 and referee #9326 | the result and its confirmation | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the turn at every order; the member's series reaches exactly down to capture" | executed: the substitution for an arbitrary index; the moments | executed: the inversion identity to order 12; the direct expansion to order 5 | executed: the member's coefficients; the discriminant | executed: the stationary points, the signs, `w″(u*)`; exact ratios at four charge ratios | not executed: lattice corrections; finite wave numbers |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This only restates block 110."
  - *Reply:* Block 110 gave four coefficients and a threshold.
  - This note gives every coefficient in closed form, and the third-order term against `ρ`.
  - It also proves that the series is the turn exactly for `b > b_c`, at every charge ratio.
- *Objection:* "The radius is capture for the comparator, so it must be for every ratio."
  - *Reply:* The radius is fixed by the nearest singularity of the inverse branch, and that need not be real.
  - Here it is real because the coefficients are nonnegative, which holds for `a, p ≥ 0`.

### N8 — Cross-cycle echo
- Block 110: fourth order; the threshold.
- This note: every order; the reach.

## Falsifiers

- A coefficient of the turn's series differing from `m_k [uᵏ]nᵏ`.
- A charge ratio `ρ ≥ 0` at which the member's series sums at some `b < b_c`, or fails to sum to the turn at some `b > b_c`.

## Boundaries and non-claims

- Block 110's continuum exterior and long-wave ray model.
- The member, `K`, the rates of crossing and the ray model are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 110 (landed), restated and quoted.
- Named standard imports, at definition level:
  - Bouguer's invariant;
  - the Lagrange–Bürmann inversion formula (formal residues under a change of variable);
  - the Beta integrals;
  - the binomial series and their product;
  - the implicit function theorem and the identity theorem for analytic functions;
  - the Vivanti–Pringsheim theorem on power series with nonnegative coefficients;
  - the discriminant of a cubic;
  - exact symbolic and rational arithmetic.
- The comparator's index (Schwarzschild's, in isotropic form) is named as a comparator only.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.**
  - Probe #9231 (Claude Opus 5.5) was refereed by #9326 (`grok-4.6`, another family).
  - The supervisor wrote a new exact runner. It ports the attempt's direct expansion, with an exact turning point and inverse in place of the attempt's series of a square root. It replaces the attempt's floating-point ratio test and monotonicity grid with the exact ratio window.
- **Before writing.** Origin was re-fetched. Block 110 was read as landed. The own prior-art check covered memory, open PRs and main, and found no earlier treatment of the radius.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_members_rays_turn_by_a_closed_series_at_every_order_2026_09_26.py
```

Expected: `TOTAL: PASS=27 FAIL=0`.
