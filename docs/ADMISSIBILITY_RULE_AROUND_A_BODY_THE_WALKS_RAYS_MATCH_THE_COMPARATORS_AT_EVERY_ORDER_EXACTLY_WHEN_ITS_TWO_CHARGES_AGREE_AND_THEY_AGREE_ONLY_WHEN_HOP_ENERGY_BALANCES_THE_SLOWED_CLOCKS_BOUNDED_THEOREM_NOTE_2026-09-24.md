---
claim_id: admissibility_rule_around_a_body_the_walks_rays_match_the_comparators_at_every_order_exactly_when_its_two_charges_agree_and_they_agree_only_when_hop_energy_balances_the_slowed_clocks_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN block 60's curvature member (p = 1, c = 8K; landed on main) for lengths l = chi^2 and rates w = N/chi, the rates of crossing of block 59 (landed), and the long-wave ray model of massless walkers, E = (w/l)|k|; all supplied. Exact: (T1) outside a spherical body chi = 1 + a/r and N = 1 - p/r, and the rays see the index n = chi^3/N = (r + a)^3/(r^2 (r - p)); at equal charges p = a = M/2 this is the comparator's index identically. (T2) On any box with walls held at w = l = 1 and any content with fixed-state derivatives e (rates) and tau (half the hop energies at a site), a static configuration has (Lap chi) = -e/(8K w chi) and (Lap N) = (e + 2 tau)/(8K chi) at every site, so the two charges seen by the walls are Q = sum e/(8K w chi) and P = sum (e + 2 tau)/(8K chi), and P - Q = (1/8K) sum [2 tau - e(1 - w)/w]/chi. A body at rest has P < Q. Equal charges need the hop energy to balance the rest energy's clock deficit, 2 sum tau/chi = sum e(1 - w)/(w chi); with 0 <= tau <= e this is impossible when every content clock runs slower than 1/3. At weak field P/Q = 1 + 2 sum tau/sum e, between 1 and 3. (T3) Capture: rays with b below min_r r n(r) = f(r*), r* = a + p + sqrt(a^2 + ap + p^2), reach a body inside r*; at a fixed first-order turn 4M/b the threshold b_c/M rises with the charge ratio rho = P/Q from 9/2 through 3 sqrt(3) at rho = 1 towards 8. (T4) The turn is 2 nu1/b + pi(nu2 + nu1^2/2)/b^2 + (4/3)(nu1^3 + 6 nu1 nu2 + 3 nu3)/b^3 + ... for n = 1 + nu1/r + nu2/r^2 + ...; at a fixed first-order turn the second-order term is 6 pi (5 + 4 rho + rho^2)/(3 + rho)^2 (M/b)^2, the comparator's 15 pi/4 exactly at rho = 1. (T5) The log-linear completion, index e^(kA/r), has capture threshold e k A and the tree-function series (refereed probes result); with lengths (k = 2) it gives 4 pi (M/b)^2 at second order. Supervisor's derivation with one refereed probes result. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_around_a_body_the_walks_rays_and_the_two_charges_of_the_curvature_member_2026_09_24.py
---

# Around a body, the walk's rays match the comparator's at every order exactly when the body's two charges agree; the charges agree only when hop energy balances the slowed clocks

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses: block 60's curvature member, block 59's rates of crossing and the long-wave ray model; one refereed probes result for the log-linear completion; nothing adopted or registered; unaudited)

This note works within supplied clauses, block 60's curvature member for lengths and rates and the long-wave ray model of the walk; it reports how the walk's rays bend around a body at every order and what makes the body's two charges agree; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 98 (#8878, landed in 8cc5f114f0) computed the first-order transverse kick of a supplied ray model, with no nonlinear bending and no changed lengths. Blocks 59 and 60 (landed) give the local ray ratio with lengths, `1 + β`, which is 2 for the curvature member at weak field. This note works to every order, and asks what a body must be for its field to bend waves as the comparator's does, known physics used as a comparator only.

- **T1: the index.** Outside a spherical body the curvature member's two fields are `χ = 1 + a/r` and `N = wχ = 1 − p/r`. Long-wave rays of the walk see the index `n = χ³/N = (r + a)³/(r²(r − p))`. When the body's two charges agree, `p = a = M/2`, this is the comparator's index, identically. So then every order of the turn and the capture threshold are the comparator's: `4M/b + (15π/4)(M/b)² + (128/3)(M/b)³ + (3465π/64)(M/b)⁴ + …`, capture below `b = 3√3 M`.
- **T2: the two charges, exactly.** For any content, on any box with held walls, the charge the lengths see is `Q = Σ e/(8Kwχ)` and the charge the clocks' `N` sees is `P = Σ(e + 2τ)/(8Kχ)`. Here `e` is the content's derivative in the rates and `τ` is half its hop energies at a site. So

  `P − Q = (1/8K) Σ [2τ − e(1 − w)/w]/χ`.

  - A body at rest (`τ = 0`) has `P < Q`, since its own clock is slowed.
  - Equal charges need the hop energy to pay exactly for the rest energy's slowed clocks: `2Σ τ/χ = Σ e(1 − w)/(wχ)`. An exact lattice example with positive rest energy and clocks near 0.6 has `P = Q`.
  - If no content site has negative rest or hop energy, equal charges are impossible when every content clock runs slower than `1/3`.
  - At weak field `P/Q = 1 + 2Στ/Σe`, between `1` (content at rest) and `3` (content with no rest energy).
- **T3: capture.** Rays with impact parameter below the smallest value of `r n(r)` reach a body lying inside the circular ray. At a fixed first-order turn `4M/b`, the threshold rises with the charge ratio `ρ = P/Q`: `9/2 M` as `ρ → 0`, `3√3 M` at `ρ = 1`, `(70 + 26√13)/27 M ≈ 6.06 M` at `ρ = 3`, tending to `8M`.
- **T4: the turn at every order.** An index `n = 1 + ν₁/r + ν₂/r² + …` turns a ray by `2ν₁/b + π(ν₂ + ν₁²/2)/b² + …`. At a fixed first-order turn the second-order term is `6π(5 + 4ρ + ρ²)/(3 + ρ)² (M/b)²`. That is `10π/3` for a body at rest with very slow clocks, the comparator's `15π/4` exactly at `ρ = 1`, and `13π/3` for content with no rest energy at weak field.
- **T5: another completion.** If the logarithms of the rates and lengths are the fields that obey the linear law, the index is `e^{kA/r}`, `k = 1 + β`. Then the capture threshold is `ekA` and the turn is a tree-function series; this is the refereed probes result, re-derived here by another route. With block 59's lengths (`k = 2`) it gives `4π(M/b)²` at second order, not `15π/4`.

**Executed.** Rays integrated directly in three dimensions agree with the exact quadrature of the turn to `10⁻⁸`. Rays at `b = b_c(1 − 10⁻³)` are captured and rays at `b_c(1 + 10⁻³)` escape, for `ρ = 1/2, 1, 3` and for the log-linear completion.

In plain terms: around a lump, the walker's waves bend the way light bends around a star in known physics, to every order, exactly when the lump does the same thing to lengths as it does to clocks. Records alone do not make that happen. A lump that just sits still slows its own clocks, and that lowers its clock charge below its length charge, so it bends waves too little at second order. A lump of pure motion does the opposite. The two agree only when the lump's internal motion exactly pays for how much it slows its own clocks. That is what a star in balance does, and nothing in the clauses yet makes the lattice's content settle into it.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The clocks, the lengths, the walk and the member are supplied clauses. Nothing is adopted.
- **Rates and lengths** (block 59, #8581, and block 60, #8590, both landed on main). Rates `w_x = e^{u_x}`, lengths `ℓ_x = χ_x²`, and a bond from `x` to `y` is crossed at `√(w_x w_y)/(χ_x χ_y)`. `N = wχ`.
- **The curvature member** (block 60 T4, landed): the field energy `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)` over bonds with an interior end, with walls held at `w = ℓ = 1`.
- **Content.** Only its fixed-state derivatives enter, as in block 60. These are `e_x = ∂⟨H⟩/∂u_x = r_x + τ_x` and `∂⟨H⟩/∂λ_x = −τ_x`, where `r_x` is the on-site (rest) part and `τ_x` is half the hop energies of the bonds at `x` (block 59 T2). A body at rest has `e = mw`, `τ = 0`.
- **Charges.** `Q = −Σ(Δχ)`, `P = Σ(ΔN)` over the interior. Far from the content `χ − 1 ≈ Qg` and `1 − N ≈ Pg`, `g` the potential of a unit source. In the continuum `g = 1/(4πr)`, so `a = Q/4π` and `p = P/4π`.
- **The ray model.** Long-wave massless rays of `E = (w/ℓ)|k|`, in the continuum exterior of a spherical body. This is the smooth identification `c = w/ℓ` of block 59 T5(c) and the ray model of block 54 T4 as landed (conditional). As landed, block 59 T4 and block 60 T4(d) are local ray statements, not integrated turns. The integrated turn here is computed within this declared model.
- **The comparator.** Known physics, used as a comparator only. Its static isotropic line element has `ψ = 1 + M/2r` and `αψ = 1 − M/2r` (Schwarzschild's solution in isotropic form). Its values `15π/4`, `128/3`, `3465π/64` and `3√3 M` are computed here from that index, not imported. For static bodies in equilibrium its two masses agree (Tolman, Komar; Beig's theorem).
- **The log-linear completion** (T5): the log-rate `u` and the log-length obey the linear law (block 53's clock clause, block 59 T5's exponentiated ansatz), so `n = ℓ/w = e^{−(1+β)u}` with `u = −A/r`.
- **Names.** The invariant `r n sin φ` is Bouguer's. The tree function is Lambert's `W` up to sign. The moments are Beta integrals.

## Theorem T1 — the exterior and the index its rays see

*Statement.*
- Outside a spherical body, the curvature member's fields are `χ = 1 + a/r` and `N = 1 − p/r`.
- For `H = c(|x|)|k|`, a ray moves along `k` and keeps `E` and `x × k`. With `c = w/ℓ = N/χ³`, the rays are those of the index `n = χ³/N = (r + a)³/(r²(r − p))`, and `r n sin φ = b` along each ray.
- `n = 1 + (3a + p)/r + (3a² + 3ap + p²)/r² + (a + p)³/r³ + …`. At `p = a = M/2` it equals `ψ²/α` with `ψ = 1 + M/2r` and `α = (1 − M/2r)/(1 + M/2r)`, identically.

*Proof.*
- Off the content both `χ` and `N` are harmonic (block 60 T4(a), (b): `Δχ = 0`, and `(−Δ + Q_x/χ_x)N = 0` with `Q_x = 0`). A spherically symmetric harmonic function tending to 1 is `1 + const/r`.
- For the rays: `d(x × k)/dt = ẋ × k + x × k̇ = 0`, because `ẋ ∥ k` and `k̇ ∥ x`. The runner checks this and `dE/dt = 0` symbolically for arbitrary `c` (family B). ∎

## Theorem T2 — the two charges

*Statement.*
- (a) **Site equations.** In a static configuration of the curvature member with content, at every interior site
  - `(Δχ)_z = −e_z/(8K w_z χ_z)`, and
  - `(ΔN)_z = (e_z + 2τ_z)/(8Kχ_z)`.
- (b) **The charges.** So `Q = Σ e/(8Kwχ)` and `P = Σ(e + 2τ)/(8Kχ)` are the fluxes of `χ − 1` and `1 − N` into the walls. Hence

  `P − Q = (1/8K) Σ_z [2τ_z − e_z(1 − w_z)/w_z]/χ_z`.

- (c) **Rest bodies and massless content.** Content at rest has `P = Σ Q_z w_z < Q`, the `Q`-weighted mean of its clocks times `Q`; one body has `P = w₀Q` (block 60 T4). At weak field `P/Q = Σ(r + 3τ)/Σ(r + τ) = 1 + 2Στ/Σe`: `1` for content at rest, `3` for content with no rest energy.
- (d) **Balance.** `P = Q` exactly when `2Σ τ/χ = Σ e(1 − w)/(wχ)`.
  - If `0 ≤ τ_z ≤ e_z` at every site (no negative rest part), balance forces `Σ (e_z/χ_z)(1 − 3w_z)/w_z ≤ 0`, so not every content clock can run slower than `1/3`.
  - One content site balances exactly when `w = e/(e + 2τ)`, which is `1/3` for content with no rest energy.

*Proof.*
- (a) By differentiation. `w_z ∂(⟨H⟩ + F)/∂w_z = e_z + 8Kw_zχ_z(Δχ)_z`, and `∂(⟨H⟩ + F)/∂χ_z = 8K(w_z(Δχ)_z + (ΔN)_z) − 2τ_z/χ_z`. The second holds because each bond at `z` is crossed at a rate proportional to `1/χ_z`. The runner checks both symbolically on a side-4 box, for arbitrary rates, lengths, rest parts and hop amplitudes (C1). Setting both to zero gives (a).
- (b) Summing `Δχ` or `ΔN` over the interior leaves only the bonds into the walls. Then subtract.
- (c) `τ = 0`, `e = mw`, or `w = χ = 1`.
- (d) With `τ ≤ e`, `Σ e(1 − w)/(wχ) = Σ 2τ/χ ≤ Σ 2e/χ`.
- Executed exactly on a `7 × 7 × 7` box (C2–C5):
  - one body at rest, `Q = 5/2`: `P = 1.166`;
  - content on one bond: `P − Q = −0.210` equals the sum;
  - a balanced content: charges `(1, 3/4)`, positive rest parts, clocks `0.577` and `0.614`, and `P = Q = 7/4` exactly;
  - the same construction with charges `(2, 2)`: clocks `0.264` and `0.267`, below `1/3`, where balance needs a negative rest part. ∎

## Theorem T3 — capture

*Statement.*
- Let `f(r) = r n(r) = (r + a)³/(r(r − p))` on `r > p`, where `N > 0`. Then `f′` vanishes at exactly one point, `r* = a + p + √(a² + ap + p²)`, a minimum. Let `b_c = f(r*)`.
- If the body lies inside `r*`:
  - a ray with `b < b_c` never turns and reaches it;
  - `b = b_c` winds onto the circular ray `r = r*`;
  - `b > b_c` escapes.
- At `p = a = M/2`: `r* = (2 + √3)M/2` and `b_c = 3√3 M`.
- At a fixed first-order turn `4M/b` (`3a + p = 2M`) and charge ratio `ρ = p/a = P/Q`,

  `b_c/M = 2(ρ + s + 2)³/((ρ + 3)(s + 1)(ρ + s + 1))`, `s = √(ρ² + ρ + 1)`.

  It is `9/2` at `ρ = 0`, `4√7 − 40/7 ≈ 4.869` at `ρ = 1/2`, `3√3` at `ρ = 1` and `(70 + 26√13)/27 ≈ 6.065` at `ρ = 3`, and it tends to `8`. It rises strictly with `ρ`.

*Proof.*
- `f′/f = 3/(r + a) − 1/r − 1/(r − p)` vanishes exactly at the roots of `r² − 2(a + p)r + ap`. The larger root exceeds `p` by `a + √(a² + ap + p²)`. The smaller lies below `p`, because `a² < a² + ap + p²`. And `f → ∞` at both ends of `(p, ∞)`.
- By the invariant of T1, `v_r² = c²(1 − b²/f²)`.
- The rise: at the minimum, `db_c/dρ = ∂f/∂a · a′(ρ) + ∂f/∂p · p′(ρ) = (6Mf/(3 + ρ)²)(1/(r* − p) − 1/(r* + a)) > 0`.
- The runner checks every step symbolically (family D). ∎

## Theorem T4 — the turn at every order

*Statement.*
- With `F = r n(r)` and `y = b/F` along the outer branch, the turn is `χ(b) = 2∫₀¹ (D(b/y) − 1) dy/√(1 − y²)`, where `D = d log r/d log F`.
- Expanding `D` in `1/F` and integrating term by term gives, for `n = 1 + ν₁/r + ν₂/r² + ν₃/r³ + …`,

  `χ = 2ν₁/b + π(ν₂ + ν₁²/2)/b² + (4/3)(ν₁³ + 6ν₁ν₂ + 3ν₃)/b³ + …`.

- For the curvature member:

  `χ = 2(3a + p)/b + (3π/2)(5a² + 4ap + p²)/b² + (8/3)(42a³ + 54a²p + 27ap² + 5p³)/b³ + (15π/8)(99a⁴ + 176a³p + 132a²p² + 48ap³ + 7p⁴)/b⁴ + …`.

  At `a = p = M/2` this is `4M/b + (15π/4)(M/b)² + (128/3)(M/b)³ + (3465π/64)(M/b)⁴ + …`.
- At a fixed first-order turn the second-order term is `6π(5 + 4ρ + ρ²)/(3 + ρ)² (M/b)²`. It increases with `ρ`, with slope `12(1 + ρ)/(3 + ρ)³` in units of `π(M/b)²`. It runs from `10π/3` (`ρ → 0`) through `15π/4` (`ρ = 1`) and `13π/3` (`ρ = 3`) towards `6π`.

*Proof.*
- The change of variables is exact on the outer branch, where `F` increases.
- For large `b`, `1/F = y/b ≤ 1/b` along the ray, and `D` is analytic in `1/F` near 0 on the physical branch. So the remainder after `K` terms is `O(b^{−K−1})`, uniformly in `y`. The moments `∫₀¹ yⁿ/√(1 − y²) dy = (√π/2)Γ((n+1)/2)/Γ(n/2 + 1)` are checked for `n ≤ 6`.
- The coefficients follow by series inversion of `F`, exactly (family E). ∎

## Theorem T5 — the log-linear completion

*Statement.*
- For the index `e^{kA/r}` (`k = 1 + β`):
  - `r e^{kA/r}` has its one minimum at `r = kA`, so the capture threshold is `ekA`;
  - the turn is `Σ_{n≥1} cₙ (kA/b)ⁿ`, with `cₙ = √π nⁿ Γ((n+1)/2)/(n! Γ(n/2 + 1)) = 2, π, 6, 4π, 250/9, 81π/4, …`.
- Without lengths (`k = 1`) this is the probes attempt's result.
- With block 59's lengths (`k = 2`), at the same first-order turn `4M/b`, the second- and third-order terms are `4π(M/b)²` and `48(M/b)³`, against the comparator's `15π/4` and `128/3`.

*Proof.* T4's expansion applied to `F = r e^{kA/r}` reproduces the probes attempt's tree-function coefficients, obtained there by inversion of `T = z e^T` (family E; D4 for the threshold). The probes attempt also shows that the series in `A/b` has radius exactly `1/(ek)`, the capture threshold. ∎

## Executed control

The control is `specs/supervisor_control_block110_rays.py`, with its output in `.out.txt`. It uses floating point.

**Ray integration.** Rays of `H = c(x)|k|` were integrated directly in three Cartesian dimensions, with DOP853 at `rtol 10⁻¹¹`, starting at `2 × 10⁵`.
- They agree with the exact quadrature of the half-turn to `10⁻⁸`. At `b = 40, 12, 8` (`M = 1`) the turns are:
  - `ρ = 1/2`: `0.10763, 0.44310, 0.81929`;
  - `ρ = 1`: `0.10810, 0.45260, 0.85871`;
  - `ρ = 3`: `0.10952, 0.48335, 1.00881`.
- The four-term series approaches them as `b` grows.

**Capture.** Rays at `b_c(1 − 10⁻³)` are captured and rays at `b_c(1 + 10⁻³)` escape. This holds at `b_c = 4.8687, 5.1962, 6.0646` and for the log-linear completion at `2e`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 98 as landed (8cc5f114f0): the first-order kick only, no nonlinear bending or changed-length result; block 60 as landed: T4(d) a local ray comparison, not an integrated turn; block 67 as landed: no general equality of the two fluxes after adding stresses"
source_of_blocker_text: blocks 98, 60 and 67; the probes result strong-field-turning-by-a-clump a2 (refereed)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "whether bound states of walkers in their own field balance their charges (a lattice virial identity), and a clause that could make them"
conditional_surface_status: "T1, T3-T5 exact in the continuum exterior and the long-wave ray model; T2 exact on any box for any content with fixed-state derivatives"
hypothetical_axiom_status: "the member, its number K, the rates of crossing, the ray model and the content are hypotheses; nothing adopted"
admitted_observation_status: "known physics (its static isotropic index; the turn's series; the capture threshold) is a comparator only"
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 60 (#8590, landed) gave the member's exact strong field for bodies at rest, with `P = Qw` and the local ray ratio `1 + 2Q/(P + Q)`. It named the comparator's masses of Arnowitt, Deser and Misner and of Tolman and Komar.
  - Block 67 (landed) kept the two fluxes distinct and made no claim of equality after stresses are added.
  - Block 98 (#8878, landed in 8cc5f114f0) gave the first-order kick of the supplied ray model, and stated no nonlinear bending or changed-length result.
  - Block 59 (landed) gave the rates of crossing and the local ray acceleration.
- **The probes attempt** `strong-field-turning-by-a-clump` a2 (worker `w-macbookpro9927a-j72ca`, Claude Opus 5.5) found the capture threshold `eA` and the Lambert series for the index `e^{A/r}`. A Grok model refereed it (`referee_w-macbookpro90c72-jd58b`, confirmed).
- **In the literature.**
  - The comparator's constraint and lapse equations for a conformally flat static metric are `∇²ψ = −2πρψ⁵` (Lichnerowicz, York) and `∇²(αψ) = 2παψ⁵(ρ + 2S)`, `S` the trace of the stress. The site equations of T2(a) have this form with `e ↔ αρψ⁶`, `τ ↔ αSψ⁶` and `8K ↔ 1/(2π)`. A massless walker, `e = τ`, then has `S = ρ`, the stress of radiation.
  - That the two masses agree for a static body in equilibrium is Beig's theorem. Its local form is the virial identity (Tolman). Buchdahl's bound puts the surface clock of a static fluid ball, with density not increasing outward, above `1/3`.
  - The comparator's series `4, 15π/4, 128/3, 3465π/64` is Keeton and Petters's. Its second-order term is the post-post-Newtonian light deflection, and its capture threshold `3√3 M` follows from its circular light orbit.
  - The invariant is Bouguer's, the tree function Lambert's.
- **New here:**
  - the exterior index `χ³/N` and its identity with the comparator's at equal charges;
  - the exact charge identity for any content on a box, with the balance condition and the bound at clocks `1/3`;
  - the capture threshold and the second-order turn as exact functions of the charge ratio;
  - the log-linear completion's threshold `ekA` and series, re-derived by series inversion, and its departure at second order.

## Exact target and obligation graph

Target: what the curvature member's field does to the walk's rays beyond first order, and what makes it the comparator's. The obligations are:
- (O1) the index;
- (O2) the charges;
- (O3) capture;
- (O4) every order;
- (O5) the other completion.

T1–T5 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- a body at rest never has equal charges;
- with no negative rest part, equal charges are impossible when every content clock runs slower than `1/3`;
- the log-linear completion departs from the comparator at second order.

### N1 — Routes by which the sentences could fail or mislead
1. *The continuum exterior.* T1, T3 and T4 use `g = 1/(4πr)`. On the lattice, `g` has cubic corrections at relative order `1/r²`, which enter the turn at second order for bodies near the ray. T2 is exact on any box.
2. *The ray model.* Long waves only. At finite wave number block 59 T4's local statement is what holds, and the lattice's direction dependence enters.
3. *Content.* T2 needs only `e` and `τ`. Whether a stationary walker state has the balance is not worked.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The comparator's values are computed from its index here. Its masses are named, not used.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| block 60 (#8590, landed) | the member; its exact strong field; `P = Qw` for bodies at rest | yes |
| block 59 (#8581, landed) | the rates of crossing; `e = r + τ`; the local ray statement | yes |
| block 54 (#8570, landed) | the conditional ray model | yes |
| block 98 (#8878, landed) | the first-order kick | placement |
| block 67 (landed) | the two fluxes kept distinct | placement |
| probes `strong-field-turning-by-a-clump` a2 (refereed) | T5 without lengths | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the rays are the comparator's at every order exactly when the charges agree; equal charges need hop energy to balance the slowed clocks" | executed: the exterior fields, the index and the ray invariants; the site equations from the bond form and a walker's energy on a side-4 box (symbolic) | executed: every site equation at all 125 interior sites of a `7 × 7 × 7` box for a body at rest and for content on one bond, generic and balanced; the charges as wall fluxes | executed: the turn's coefficients to fourth order for the member and to sixth for the log-linear completion; the comparator's series at equal charges | executed: the capture threshold against the charge ratio, its derivative, values and limit; the second-order term against the charge ratio | T2 on any box with held walls for any content with fixed-state derivatives; T1, T3–T5 in the continuum exterior of a spherical body in the long-wave ray model; the member, `K`, the ray model and the content supplied; whether bound walkers balance is not derived |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 60 already showed the member is the comparator's static theory, so the rays must be the comparator's." *Reply:* Only when the two charges agree. For a body at rest the member gives `P = Qw < Q`. The rays then depart at second order, by an amount T4 gives exactly. The member supplies the comparator's equations; it does not supply the comparator's balance.
- *Objection:* "Equality is automatic for any body that holds together." *Reply:* In the comparator it follows from the body's equilibrium. Here it needs `2Στ/χ = Σe(1 − w)/(wχ)`, a condition on the content that no clause imposes. The exact example with charges `(2, 2)` shows content that cannot meet it with nonnegative rest energy.

### N8 — Cross-cycle echo
- Block 98 gave first order; block 60 gave the member and bodies at rest; block 67 kept the fluxes apart.
- This note gives every order, the exact charge identity and the balance.

## Falsifiers

- A static configuration of the member whose wall fluxes differ from `Σ e/(8Kwχ)` and `Σ(e + 2τ)/(8Kχ)`.
- A ray of `E = (w/ℓ)|k|` in the exterior field whose turn differs from T4's series at large `b`.
- Content with `0 ≤ τ ≤ e`, every content clock below `1/3`, and `P = Q`.

## Boundaries and non-claims

- The member, `K`, the rates of crossing, the ray model and the content are supplied.
- The comparator's values are a comparator. Nothing here says that the lattice's content balances, nor that its rays are the comparator's.
- Finite wave numbers, lattice corrections to the exterior, and bound states of walkers in their own field are not worked.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 59, 60, 67 and 98, restated or placed.
- The probes result for the log-linear completion, refereed by another model family.
- Named standard imports, at definition level:
  - Bouguer's invariant;
  - the Beta integrals;
  - series inversion;
  - the tree function (Lambert's `W`);
  - DOP853 and adaptive quadrature in the control;
  - exact symbolic arithmetic.
- The comparator's constraint and lapse equations, masses (Arnowitt, Deser and Misner; Tolman; Komar; Beig) and bounds (Buchdahl) are named as comparators only.

## Review record

- **Who and when.** Supervisor-run block, the fifty-eighth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - T1–T4 are the supervisor's derivation, the same family as blocks 53–60.
  - T5 is the probes attempt `strong-field-turning-by-a-clump` a2 (Claude Opus 5.5), refereed by a Grok model (confirmed), and re-derived here by series inversion.
  - T1–T4 have no other-family check yet. T4's values at equal charges agree with the published series.
- **Before writing.** Main was re-fetched (8cc5f114f0), and blocks 59, 60, 67 and 98 were read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_around_a_body_the_walks_rays_and_the_two_charges_of_the_curvature_member_2026_09_24.py
```

Expected: `TOTAL: PASS=23 FAIL=0`.
