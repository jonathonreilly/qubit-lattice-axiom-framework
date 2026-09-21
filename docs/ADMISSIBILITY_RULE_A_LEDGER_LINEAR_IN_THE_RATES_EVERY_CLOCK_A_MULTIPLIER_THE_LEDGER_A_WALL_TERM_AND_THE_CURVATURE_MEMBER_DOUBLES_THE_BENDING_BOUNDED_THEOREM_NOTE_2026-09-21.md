---
claim_id: admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53 to 59 (open PRs #8568, #8570, #8571, #8573, #8578, #8579, #8581; not adopted): site rates w_x = exp(u_x) of weight one, amplitudes timed by them, a kept ledger <H> + F of weight one, and lengths of weight zero; here one length l_x = exp(lam_x) per site (isotropic stretching only), chi = sqrt(l), N = w chi, bonds crossed at sqrt(w_x w_y)/(chi_x chi_y). (T1) For every ledger of weight one the sum over ALL sites of dE/du_x is E. If every rate is varied the ledger vanishes on solutions, which a non-negative field energy with positive content cannot do (block 55 T4(b), block 56); if the walls' rates are held the ledger equals the walls' own terms. (T2) With a weight-zero field a field energy LINEAR in the rates exists, F = sum_x w_x G_x(lam). Then every rate is a multiplier: stationarity in u_x is e_x = -w_x G_x(lam), F contributes no difference of rates (the rates have no stiffness of their own), and the rates follow from stationarity in the lengths, which is linear in them. For the bilinear members G = c X Lap X, X = l^(p/2), a closed lattice has no static solution with positive content. (T3) The nearest-neighbour members G = K l^p (a Lap lam + b q), q_x = (1/2) sum over neighbours of (lam_y - lam_x)^2, have the second-order form K wbar [a u.Lap lam + (ap - b) lam.Lap lam]: a body at rest stretches lengths as l = (wbar/w)^beta with beta = a/(2(ap - b)); clocks are slow near positive energy iff ap > b. Bilinear members have b = ap/2 and beta = 1/p. For p = 1, c = 8K, the continuum form 8K w chi Lap chi is -K x rate x volume x scalar curvature of the metric l^2 delta in three dimensions (p = 1 is three minus two): beta = 1, a ray's bending is twice a slow body's fall (block 59 T4), and at weak field Lap lam = -e/(4K wbar), Lap u = (e + tau)/(4K wbar), tau the site's hop energy; gamma of block 55 is 1/(4K). (T4) Strong field exactly, for that member, bodies at rest of bare energies m_i, walls held at w = l = 1: chi = 1 + sum Q_i g(., x_i) with Q_i chi(x_i) = m_i/(8K), the unique positive solution, the minimum of a strictly convex function; N solves a LINEAR equation, N = 1 - sum P_i g_i with P_i = Q_i w_i, and 0 < w <= 1 everywhere: no clock stops at any strength; the rates' equation is block 53's form, w_z = kappa_z x (the chi-weighted mean of the six neighbours' rates), kappa_z = 1/(1 + m_z/(4K chi_z sum_y chi_y)); one body: w_0 = 1/(1 + 2 Q g_0). The ledger is the wall term 8K sum Q_i = sum m_i/chi_i: below the bare energies, above block 56's value at the same bare energy with the same first correction, and unbounded (M + M^2 g_0/(8K) = m); a pair shows the walls less than its parts, and less as the mutual potential rises. Far field: the lengths carry 2Q and the rates P + Q, equal only to first order: bending over fall = 1 + (1 + 2Qg_0)/(1 + Qg_0), between 2 and 3. (T5) For every kinetic term that holds no rate of change of a rate, c_k l^s (dlam/dt)^2/w among them, the rates stay multipliers and at second order the lengths and the rates are fixed at each label time by the content at that label time: nothing in the isotropic lengths is delayed. On a closed lattice with content at rest a uniform solution exists iff c_k < 0: m w + c_k l^s (dlam/dt)^2/w = 0, kept by the lengths' own equation, l proportional to (t + t_0)^(2/s) in the label with w = 1. EXECUTED, NOT CLAIMED: the stationary point in all 250 variables of a 7x7x7 box found by a root search with no unit-source potential agrees with the closed form to six digits for bare energies from 0.05 to 500; six members' exponents read off brute-force solutions agree with beta to within 0.7 per cent; on a torus the constraint's residual is never zero and falls only as one site's length shrinks without bound. NOT claimed: that lengths exist; that the field energy is linear in the rates; the member, its number K, the powers p and s, the sign of c_k; that the anisotropic parts of block 59 can stay at rest; that bound bodies with internal motion have P = Q; that what the walls see is constant while content moves; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_2026_09_21.py
---

# A ledger linear in the rates: every clock a multiplier, the ledger a wall term, and the member built on curvature doubles the bending

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 59 and one declared family of field energies; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for lengths of weight zero; it reports what a ledger linear in the rates does, in general and for one declared member; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 59 (open PR #8581) ended with a number left over. A field of clock rates makes slow bodies fall and bends rays by half of the comparator's amount; lengths that stretch as `ℓ = (w̄/w)^β` supply the rest if `β = 1`; a cross term in the field's energy gives any `β` one likes. Block 55 (open PR #8571) had left a second loose end: its ledger could not let the unit of rate be a variable, because a positive field energy plus positive content can never add up to the zero that would require.

Both ends meet in one observation. Once there is a field of weight zero — lengths — a new kind of field energy becomes possible that was not available to blocks 53 to 57: one that is **linear in the clock rates**, `F = Σ_x w_x G_x(lengths)`. This note works out what such a ledger does.

1. **The unit of rate.** For any ledger of weight one, the derivatives with respect to all the log-rates add up to the ledger itself. So if every rate is varied the ledger is zero on solutions; if the walls' rates are held, the ledger *is* the walls' share (T1). Block 56's "the ledger is a surface term" was an instance.
2. **Every clock a multiplier.** With `F` linear in the rates, varying a rate brings in no difference of rates from the field's side. It gives a relation at that one site between the energy per tick and the lengths; for content at rest that relation holds no rate at all. The rates have no stiffness of their own; they are fixed afterwards by the lengths' equation, which is linear in them. On a closed lattice no static solution with positive content exists (T2).
3. **The exponent.** For nearest-neighbour members `K ℓ^p (aΔλ + b q)` a body at rest gives `β = a/(2(ap − b))`. The members that are bilinear in a power of the length have `β = 1/p`. The one with `p = 1` is, in the continuum, `−K ×` rate `×` volume `×` scalar curvature of the stretched lattice, the power one being three (volume) minus two (curvature). It has `β = 1`: **bending is twice the fall.** Its weak-field equations are `Δλ = −e/(4Kw̄)` and `Δu = (e + τ)/(4Kw̄)`: content that moves slows clocks by more than content at rest (T3).
4. **Strong field, exactly.** For that member and bodies at rest the root of the length is one plus a sum of unit-source potentials with charges fixed by a quadratic relation; the rates then solve a *linear* equation. No clock stops at any strength. The rates obey block 53's rule — each rate is a factor `κ < 1` times a mean of its neighbours' — with the lengths as weights. What the walls see is `Σ m_i/χ_i`: less than the bare energies, more than block 56 gave, without bound. Far away the lengths carry `2Q` and the rates `P + Q`, which agree only at first order (T4).
5. **No delay here either.** Give the lengths any kinetic term that holds no rate of change of a clock rate. The rates stay multipliers, and at second order both fields are fixed at each label time by the content at that label time. On a closed lattice with content, a uniform solution exists only if the kinetic term is negative, and then the lengths must move: `ℓ ∝ t^{2/s}` (T5).

In plain terms: if the field's energy is counted per tick of each local clock, then no clock's rate is a thing with its own springiness. Each clock is a bookkeeping multiplier, the books of a closed region are kept entirely on its boundary, and the one natural way to write "how curved is the stretched lattice, per tick" doubles the bending of rays. That is the comparator's structure, found in the framework's objects. But it is *declared*, not forced: the power `p`, the number `K` and the sign of the kinetic term are put in by hand, and the isotropic lengths carry no delay — if a delay lives anywhere, it is in the direction-dependent parts that block 59 found slaved at rest.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 59 (PR #8581), next_trace_action: 'whether anything in the framework fixes beta (the comparator's 1 would need the cross stiffness to equal the lengths' own); a law of motion for lengths and the front it carries'; block 55 (PR #8571) T4(b): 'with positive energies the ledger cannot be stationary in every u_x: the unit of rate is not a variable'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the direction-dependent parts of the lengths (block 59's bond rates) under a ledger linear in the rates: whether they carry a delay and at what speed; whether a bound body's internal hop energy restores P = Q; whether what the walls see stays constant while content moves; whether anything in the framework fixes p = 1 and the sign of the kinetic term; the owner's decision whether the field energy is counted per local tick"
conditional_surface_status: "T1 exact for every ledger of weight one; T2 exact for every field energy linear in the rates, the closed-lattice statement for bilinear members; T3 exact at second order for the members named, the continuum identity by exact symbolic algebra; T4 exact for bodies at rest in any box with held walls, bilinear member p = 1, isotropic stretching; T5 exact at second order for kinetic terms holding no rate of change of a rate, and for uniform configurations"
hypothetical_axiom_status: "blocks 53 to 59's clauses; one length per site; a field energy linear in the rates; for T3 to T5 the declared members; for T5 a kinetic term for the lengths; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the covariance sentence of Admissibility, and its silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 59 (open PRs) supply the rates, the clocked amplitudes, the ledger, the change of parameter under which a rate has weight one and a pure number weight zero, and lengths as pure numbers.

- **Rates and lengths.** `w_x = e^{u_x} > 0` (weight one). One length per site, `ℓ_x = e^{λ_x} > 0` (weight zero): isotropic stretching only; block 59's bond lengths are here `ℓ_b = χ_x χ_y` with `χ = √ℓ`. `N_x = w_x χ_x`.
- **Content.** `⟨H⟩` of weight one in the rates; bonds are crossed at `√(w_x w_y)/(χ_x χ_y)`. `e_x = ∂⟨H⟩/∂u_x` (block 55); `τ_x` half the hop energies of the six bonds at `x` (block 59), so that `∂⟨H⟩/∂λ_x = −τ_x`. A body at rest at `x` with bare energy `m_x` has `e_x = m_x w_x`, `τ = 0`.
- **Ledger.** `𝓔 = ⟨H⟩ + F`, `F` of weight one. **Linear in the rates:** `F = Σ_x w_x G_x(λ)`.
- **Nearest-neighbour members.** `G_x = K ℓ_x^p (a (Δλ)_x + b q_x)`, `(Δf)_x = Σ_{y∼x}(f_y − f_x)`, `q_x = ½ Σ_{y∼x}(λ_y − λ_x)²`. **Bilinear members:** `G_x = c X_x (ΔX)_x`, `X = ℓ^{p/2}`. **The curvature member:** `p = 1`, `c = 8K`, written over bonds as `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`, the sum over every bond with an interior end; the walls' terms are part of it.
- **Walls.** Held at `w = 1`, `ℓ = 1`. `g(·, x_i)` is the potential of a unit source, the inverse of `−Δ` on the interior with zero walls, `g_0` its value at the source.
- **Kinetic terms** (T5). Any function of the lengths and their rates of change, quadratic in the latter, holding no rate of change of a rate and of the weight that makes `L dt` unchanged by a change of label; the local instance `Σ_x c_k ℓ_x^s (dλ_x/dt)²/w_x`.

That the rate of a clock enters the comparator's energy function linearly, as a multiplier whose variation gives a constraint at each point, and that the energy of a bounded system is then a surface term while that of a closed one vanishes, is the formulation of Arnowitt, Deser and Misner. For a metric that is a stretching of the flat one the constraint is the equation of Lichnerowicz and York, `volume × curvature = −8ψ∇²ψ`; its solution for bodies momentarily at rest is that of Brill and Lindquist; keeping only the isotropic stretching is the approximation of Isenberg and of Wilson and Mathews. One body in these coordinates is Schwarzschild's solution, where the two far-field coefficients agree; that they agree for a static body only when its stresses are counted is the content of the masses of Tolman and Komar. The negative kinetic term of the isotropic stretching and the uniform motion it drives are Friedmann's equation. The family with a free exponent has the form of the theories of Brans and Dicke. Block 55's and block 56's law is Einstein's static theory of 1912. None is used as authority; the comparator's values are quoted as a comparator.

## Prior art and what is new

Every piece is classical. What is new is the statement inside the framework's vocabulary: that the obstruction of block 55 T4(b) is lifted exactly by a weight-zero field, which allows a field energy linear in the rates; that for such a ledger every rate is a multiplier, the rates have no stiffness of their own, and the ledger of a region with held walls is the walls' term; that block 59's free exponent is `a/(2(ap − b))` on the nearest-neighbour family and `1/p` on the bilinear members, equal to one for the member that is rate times volume times curvature; that this member's strong field for bodies at rest is solved exactly on the lattice, where a point body is regular, with the rates obeying block 53's rule weighted by the lengths and `κ` given in closed form; that at strong field a body pinned at rest shows different coefficients to clocks and to lengths; and that the isotropic lengths carry no delay for any kinetic term of the stated kind. No gravitational claim is made.

## Exact target and obligation graph

Target: what a ledger linear in the rates does, and what it fixes of block 59's exponent. Obligations: (O1) the unit of rate; (O2) the structure of a multiplier ledger; (O3) the exponent on a family of members; (O4) the strong field of one member; (O5) whether the lengths carry a delay. T1–T5 discharge them.

## Theorem T1 — the unit of rate as a variable

*Statement.* Let `𝓔` be of weight one: `𝓔(s w) = s 𝓔(w)` for `s > 0`, all rates scaled, all else fixed. (a) `Σ_x ∂𝓔/∂u_x = 𝓔`, the sum over all sites. (b) If `𝓔` is stationary in every `u_x`, then `𝓔 = 0`; a ledger that is positive at every configuration has no such stationary point. (c) If the rates of a set `W` of sites are held and `𝓔` is stationary in every other `u_x`, then `𝓔 = Σ_{x∈W} ∂𝓔/∂u_x`.

*Proof.* Differentiate `𝓔(e^s w) = e^s 𝓔(w)` at `s = 0`: (a). Then (b) and (c) are read off. Block 56's field energy is a sum of squares and its content positive, so (b) is block 55 T4(b); with held walls (c) is block 56's statement that the ledger is a surface term. ∎

## Theorem T2 — multiplier ledgers

*Statement.* Let `F = Σ_x w_x G_x(λ)` with `G_x` functions of the lengths alone. (a) `∂F/∂u_x = w_x G_x` and `∂²F/∂u_x∂u_y = 0` for `x ≠ y`: stationarity in `u_x` is `e_x = −w_x G_x(λ)`, and `F` contributes no difference of rates to any equation. (b) Stationarity in `λ_z` is `Σ_x w_x ∂G_x/∂λ_z = τ_z`: linear in the rates. (c) For a bilinear member `G = c X ΔX`, `c > 0`, on a closed lattice there is no static configuration with `e ≥ 0`, `e ≢ 0`.

*Proof.* (a), (b) by differentiation; `∂⟨H⟩/∂λ_z = −τ_z` because the bonds at `z` are crossed at a rate proportional to `1/χ_z`. (c) The constraint is `(ΔX)_x = −e_x/(c w_x X_x) ≤ 0`, negative somewhere, while `Σ_x (ΔX)_x = 0` on a closed lattice. ∎

For content at rest `e_x/w_x = m_x`: the constraint holds no rate at all. It fixes the lengths from the bare energies; the rates come afterwards.

## Theorem T3 — the nearest-neighbour family and the exponent

*Statement.* (a) For `G = K ℓ^p (aΔλ + bq)` the part of `F` of second order in `(u − ū, λ)` is `K w̄ [a u·Δλ + (ap − b) λ·Δλ]`; there is no term in `u` alone. (b) With no hop energy and walls held, stationarity in the lengths gives `λ = −β (u − ū)`, `β = a/(2(ap − b))` (`ap ≠ b`); stationarity in the rates gives `Δλ = −e/(aKw̄)`, so `Δu = 2(ap − b) e/(a²Kw̄)`: for `a, K > 0` lengths stretch near positive energy in every member, and clocks are slow there iff `ap > b` (the member `(4, 8, 1)` has fast clocks near a body). (c) The bilinear member `c X ΔX`, `X = ℓ^{p/2}`, agrees at second order with `(Ka, Kb) = (cp/2, cp²/4)`: `b = ap/2`, `β = 1/p`. (d) In the continuum, for the metric `ℓ² δ` in three dimensions, (volume density) × (scalar curvature) `= −8χ∇²χ = −ℓ(4∇²λ + 2|∇λ|²)`. (e) For the member `(a, b, p) = (4, 2, 1)` with hop energy: `Δλ = −e/(4Kw̄)`, `Δ(u + λ) = τ/(4Kw̄)`, so `Δu = (e + τ)/(4Kw̄)`; block 55's `γ` is `1/(4K)`.

*Proof.* (a) `e^{u} e^{pλ}(aΔλ + bq)` to second order is `aΔλ + (u + pλ)aΔλ + bq`; the first-order sum vanishes because every bond enters `ΣΔλ` twice with opposite signs, and `Σ_x q_x = −λ·Δλ`. (b) The gradient in `λ` is `Kw̄[aΔu + 2(ap − b)Δλ]`, in `u` it is `Kw̄ aΔλ`. (c) `X_x(X_y − X_x) = ℓ_x^p (e^{(p/2)d} − 1)`, `d = λ_y − λ_x`, is `ℓ_x^p((p/2)d + (p²/8)d² + …)`. (d) By direct computation of the curvature (runner C4). (e) From (b) with the source `τ_z` of T2(b); block 56's law is `Δu = γ e/w̄` at weak field. ∎

By block 59 T4 a ray's bending over a slow body's fall is `1 + β`. It is 2 for every member with `a = 2(ap − b)`; among bilinear members, for `p = 1` only. A walker with no rest energy has `e = τ` (block 59 T2): it slows clocks twice as much as a body at rest of the same energy and stretches lengths alike.

## Theorem T4 — the strong field of the curvature member, exactly

*Setting.* The bilinear member with `p = 1`, `c = 8K`, in its bond form; bodies at rest at sites `x_i` with bare energies `m_i > 0`, `μ_i = m_i/(8K)`; walls held at `w = ℓ = 1`; `G_{ij} = g(x_i, x_j)`.

*Statement.* (a) `χ = 1 + Σ_i Q_i g(·, x_i)` with `Q_i χ(x_i) = μ_i`. The positive solution exists and is unique: it is the minimum of the strictly convex function `Φ(Q) = Σ Q_i + ½ Q·GQ − Σ μ_i log Q_i` on `Q > 0`. One body: `Q(1 + Qg_0) = μ`. (b) `N` solves the linear equation `(−Δ + Q_x/χ_x) N = 0`, `N = 1` on the walls: `N = 1 − Σ_i P_i g(·, x_i)` with `P_i = Q_i w_i`, and `0 < N ≤ 1`, so `0 < w ≤ 1`: no clock stops at any strength. One body: `P = Q/(1 + 2Qg_0)`, `w_0 = 1/(1 + 2Qg_0)`. Equivalently, at every interior site `w_z = κ_z × (Σ_y χ_y w_y/Σ_y χ_y)` over the six neighbours, `κ_z = 1/(1 + m_z/(4Kχ_z Σ_y χ_y))`. (c) The ledger of the box is the walls' term, `𝓔 = 8K Σ_i Q_i = Σ_i m_i/χ(x_i) < Σ m_i`. One body: `M = 8KQ` solves `M + M²g_0/(8K) = m`; it exceeds block 56's `m/(1 + m g_0/(8K))` (with `γ = 1/(4K)`), agrees with it through `m − m²g_0/(8K)`, and is unbounded, growing as `√(8Km/g_0)`, where block 56's was bounded by `8K/g_0`. For several bodies each `Q_i` is smaller than the charge the body would carry alone, and for two bodies `∂(Q_1 + Q_2)/∂G_{12} < 0`. (d) Far from one body `χ − 1 = Qg` and `1 − N = Pg`: the lengths carry `2Q`, the rates `P + Q`, and bending over fall is `1 + 2Q/(P + Q) = 1 + (1 + 2Qg_0)/(1 + Qg_0)`, which is 2 at first order in `Q` and below 3 at any strength.

*Proof.* (a) Off the bodies the constraint is `Δχ = 0`; at a body `(Δχ)(x_i) = −μ_i/χ(x_i) =: −Q_i`. `∂Φ/∂Q_i = 1 + (GQ)_i − μ_i/Q_i = χ(x_i) − μ_i/Q_i`; `G` is positive definite and `−log` convex, and `Φ → ∞` at the boundary of the orthant and at infinity. (b) `F = 8K Σ_x N_x (Δχ)_x` over all sites, and `Δ` is symmetric, so `∂F/∂χ_z = 8K[w_z(Δχ)_z + (ΔN)_z]`, with `N = 1` on the walls because the walls' terms are part of the bond form. Setting it to zero with `(Δχ)_z = −Q_z`: `(ΔN)_z = (Q_z/χ_z) N_z`. If `N` had a non-positive minimum at an interior site, `ΔN ≥ 0` and `(Q/χ)N ≤ 0` there force `N` equal at the neighbours, and so on to the walls, where `N = 1`. `P_i = (ΔN)(x_i) = Q_i N_i/χ_i = Q_i w_i`. For one body `P = (Q/χ_0)(1 − Pg_0)`. The weighted-mean form is `w_z(6χ_z − (Δχ)_z) = Σ_y χ_y w_y` rewritten. (c) T1(c): the walls' term is `8K Σ_{x∈W}(Δχ)_x`, and the sum of `Δχ` over all sites of the box vanishes, so it equals `8K Σ Q_i`. `χ_0 = 1 + Mg_0/(8K) < 1 + m g_0/(8K)` gives the comparison. If `Q_i^0` is the charge alone, `Q(1 + G_{ii}Q) − μ_i` is increasing and negative at `Q_i`. Differentiating the two-body equations in `G_{12}` gives `(D + G) dQ = −(Q_2, Q_1)ᵀ dG_{12}` with `D = diag(χ_i/Q_i)`, and `1ᵀ(D + G)^{-1}(Q_2, Q_1)ᵀ > 0` because `G_{ii} > G_{12}`. (d) By (a), (b). ∎

At weak field `log κ = −m/(24K) = −(γ/6) m`: block 55's Corollary. The rule "a rate is a factor times a mean of its neighbours' rates" of block 53 holds at every strength, with the lengths as weights.

## Theorem T5 — motion of the lengths

*Statement.* (a) Let the kinetic term hold no rate of change of a rate. Then the equations of the rates remain constraints, and at first order in the fields `Δλ = −e/(aKw̄)` holds at each label time, with `Δu` fixed at that label time by the content and the second rate of change of the lengths: no equation of the pair is a wave equation. (b) On a closed lattice with content at rest, `m` per site, and the kinetic term `Σ c_k ℓ^s (dλ/dt)²/w`, a uniform solution exists iff `c_k < 0`. In the label with `w = 1`: `m = |c_k| ℓ^s (dλ/dt)²`, `2λ̈ + s λ̇² = 0`, `ℓ = (1 + t/t_0)^{2/s}`, `t_0 = (2/s)√(|c_k|/m)`; the rate of change of the constraint is `−λ̇` times the lengths' equation, so the constraint is kept.

*Proof.* (a) No `du/dt` appears, so stationarity in `u_x` is `e_x + w_x G_x +` (terms quadratic in the lengths' rates of change) `= 0`; the last are of second order. (b) Stationarity in `w` of `c_k ℓ^s λ̇²/w − mw` is `m w² + c_k ℓ^s λ̇² = 0`; the rest by differentiation (runner E2). ∎

The comparator's values are `s = 3` (the volume) and `c_k = −6K`. Block 57 (open PR #8578) covers kinetic terms in differences of rates' rates of change: they do not propagate either.

## Executed (supervisor controls; floating point; evidence, not proof)

`specs/supervisor_control_block60_multiplier_ledger.py`: the stationary point of the bond-form ledger in all 250 interior variables of a `7³` box, by a root search on the analytic gradient (itself checked against finite differences, `9×10⁻⁹`), with no unit-source potential anywhere. For one body of bare energy 0.05, 0.5, 5, 50, 150, 500 (`K = 1/2`) the body's `u`, its `λ` and the ledger agree with T4's closed form to the six digits printed (continuation in the bare energy; a cold start at 500 did not finish and was not used). The far-field coefficients read two sites out agree with `Q` and `P`. `λ/(−u)` two sites out is 1.003 at 0.05 and 1.80 at 500. The member `K w ℓ (4Δλ + 2q)`, not bilinear, agrees at 0.05 and differs by two parts in a thousand at 5.

`specs/supervisor_control_block60_refuter.py`: see the Review record.

## No-Go Discipline Gate

The note's negative sentences: a positive ledger has no stationary point once the unit of rate is varied; a closed lattice has no static configuration with positive content; the rates have no stiffness of their own; the far-field coefficients of a body pinned at rest agree only at first order; nothing in the isotropic lengths is delayed.

### N1 — Routes by which the sentences could fail
1. *The direction-dependent parts.* Block 59's bond rates have two modes beyond the isotropic one. Nothing here says they carry no delay; this note holds them at rest. They are the named next step.
2. *Internal motion.* `Δu = (e + τ)/(4Kw̄)`: hop energy raises `P`. Whether a bound body's internal hop energy brings `P` up to `Q` is not examined.
3. *A closed lattice that moves.* T5(b) is the exit from T2(c), and needs `c_k < 0`.
4. *Field energies not linear in the rates.* Outside T2; blocks 55 and 56 are that case.
5. *Kinetic terms with rates' rates of change.* Differences only are covariant (block 57 T1) and do not propagate (block 57 T2); a mixed term with the lengths' rates is not examined.
6. *A site whose length shrinks to nothing.* The refuting pass found the closed lattice's residual falls towards zero that way; it is not a configuration (`ℓ > 0`).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Isotropic stretching only. `K > 0`, `a > 0`. Walls held at `w = ℓ = 1`: the reference to the ambient rate is the same object as in blocks 56, 57 and 59. Bodies at rest are supplied and pinned; nothing holds them but the statement that they are at rest. T3 and T5(a) are second-order statements. The continuum identity is used to *name* a member, not to derive one.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its rotations; the covariance sentence; the absences that motivate the clauses | yes (premise) |
| block 55 (open PR #8571) | the ledger, weight one, `e_x`, T4(b), `γ`, the Corollary's `κ` | yes (restated) |
| block 59 (open PR #8581) | lengths as pure numbers, hop energy, bending over fall `= 1 + β` | yes (restated) |
| block 56 (open PR #8573) | held walls, the ledger as a surface term, the comparison value | restated |
| blocks 53, 57 (open PRs #8568, #8578) | the rule for a rate; the change of label and kinetic terms in rates | placement |
| decision record (open PR #8572) | forks 6 and 7 | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "weight one and the walls' term; multipliers; `β = a/(2(ap − b))`, `1/p`, the curvature identity; the exact strong field; no delay, uniform motion iff `c_k < 0`" | executed: both ledgers on a `5³` box with a hopping rational amplitude: weight one, the sum of `w ∂𝓔/∂w` by exact differences, additivity in the rates | executed: both stationarity conditions at all 125 interior sites of a `7³` box for one and for three bodies; the rate at each body; `P_i = Q_i w_i`; the weighted-mean rule | executed: exact second-order jets of six members and three bilinear members; `β` by exact differences; the curvature identity by exact symbolic algebra | executed: the ledger against the wall term, the bare energies and block 56; convexity; the far-field coefficients; the closed lattice; the uniform motion and its constraint | T1 every ledger of weight one; T2 every field energy linear in the rates; T3 the members named, second order; T4 bodies at rest, held walls, the curvature member, isotropic stretching; T5 second order and uniform configurations; lengths, linearity in the rates, the member, `K`, `p`, `s`, the sign of `c_k` not derived |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository; it is not used, and whether it bears on the sign or size of `c_k` is not decided here. `scale_reference_primitive` converts units and fixes no `K`. `realized_state_primitive` grants evaluation at a supplied state. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You have written down the comparator and found that it is the comparator." Reply: the note says so, under the Premises. What it adds is where the comparator's structure sits in the framework's objects and what is and is not forced there. Forced, given a ledger of weight one: the walls' term (T1). Forced, given linearity in the rates: multipliers, no stiffness, the closed-lattice statement (T2). Not forced: linearity in the rates itself, `p`, `K`, `c_k`. The owner's decision record should carry those three lists. Second objection: "`P ≠ Q` contradicts the comparator's static solution." Reply: there the two agree because the body's stresses are counted; a body pinned at rest on one site has none, and T3(e) shows which term would supply them. Third objection: "No delay again; then what is the point of lengths?" Reply: the isotropic part is one of three modes of block 59's bond rates. The statement narrows where a delay can live.

### N8 — Cross-cycle echo
Block 53: a rate is a factor times the mean of its neighbours' rates; here the same rule at every strength, weighted by the lengths, with `κ` in closed form. Block 55: the unit of rate is not a variable; here the premise that made it so (`F ≥ 0`) is what a weight-zero field removes. Block 56: the ledger is a surface term, bounded; here a surface term again, unbounded. Block 57: neighbour-referred kinetic terms do not propagate; here the isotropic lengths do not either. Block 59: `β` free; here `β` on two families.

## Falsifiers

- A ledger of weight one whose derivatives in all the log-rates do not sum to it.
- A field energy linear in the rates whose rate equations contain a difference of rates coming from `F`.
- A nearest-neighbour member of the stated form whose body at rest gives `λ ≠ −β(u − ū)` at second order with `β = a/(2(ap − b))`.
- A second positive solution of `Q_i χ(x_i) = μ_i`; a box in which the curvature member's ledger is not `Σ m_i/χ_i`; a clock that stops.
- A kinetic term holding no rate of change of a rate under which a small disturbance of the isotropic lengths travels.

## Boundaries and non-claims

Lengths, and that the field energy is counted per local tick, are supplied. The members are declared; `K`, `p`, `s` and the sign of `c_k` are not derived, and the continuum identity names a member without forcing it. Only the isotropic part of block 59's bond rates is kept; whether the other two modes can stay at rest, and whether they carry a delay, is not examined. Bodies are pinned at rest; a bound body with internal motion is not examined, and neither is the constancy of the walls' term while content moves. The stationary points are saddles, and nothing is said about stability. The comparator's values are quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the covariance sentence of Admissibility, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 59 and the decision record (PRs #8568, #8570, #8571, #8573, #8578, #8579, #8581, #8572, open): restated or placed.
- Named standard imports at definition level: the degree-one identity for homogeneous functions; the symmetry and the maximum principle of the lattice Laplacian with held walls; strict convexity and uniqueness of a minimum; second-order expansions; the scalar curvature of a metric from its connection; stationarity of a Lagrangian.
- Reference only: Arnowitt, Deser and Misner; Lichnerowicz; York; Brill and Lindquist; Isenberg; Wilson and Mathews; Schwarzschild; Tolman; Komar; Friedmann; Brans and Dicke; Einstein (1912).

## Review record
Supervisor-run block, the eighth of the source-link direction and the fourth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: nothing in the axioms memo or in blocks 53 to 59 forces the field energy to be linear in the rates; the note must present it as a supplied possibility that a weight-zero field opens, and keep three lists apart — forced by weight one, forced by linearity, declared. A rigour lens: the first design had the box's ledger "identically zero"; writing the gradient for the control showed that the walls' terms belong to the bond form (they are what puts `N = 1` on the walls), and the ledger of a box is then the walls' term, not zero — T1(c), which also recovers block 56's surface term. The pair comparison was first planned across separations, which mixes the mutual effect with the walls' nearness; it was replaced by two statements that are exact (each charge below its value alone; the slope in the mutual potential). A comparator lens: the structure is the comparator's in every part, named under the Premises; `P ≠ Q` for a pinned body is the known difference that stresses remove, and the note says which term would do it rather than claiming agreement. A strategy lens: the owner needs to know that block 59's missing half has a natural home and what it costs — one more supplied clause (the field energy counted per local tick) and three declared values. Refuting pass (`specs/supervisor_control_block60_refuter.py`, floating point, machinery disjoint from the runner's): W1 six members solved by brute force at weak field, `λ/(−u)` two sites out against `β`: 1.0011, 0.3341, 0.6674, 0.2516, −0.5005, 1.0007; W2 two bodies at three placements, 200 random starts each: one positive solution every time, `P_i = Q_i w_i` to six digits, the walls see least for the adjacent pair; W3 the closed lattice: the constraint's residual is never zero — and here the pass corrected the supervisor, whose random starts sat at `1.4×10⁻²` and suggested a positive floor: a start built to defeat the claim, one far site shrunk to the cap, drives the residual to `10⁻⁶` as the cap loosens, so the infimum is zero and not attained (N1 route 6); W4 block 56's ledger and its derivative along the uniform shift: equal and positive; W5 the uniform motion integrated from the lengths' equation alone for three `(c_k, s)`: constraint kept to `10⁻¹¹`, exponents `2/s` to five digits; W6 the far length responds at the same label time. All pass. Mutation census: 13 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_2026_09_21.py
```

Expected: `TOTAL: PASS=25 FAIL=0`.
