---
claim_id: admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Supplied rate-length static models: degree-one homogeneity gives a stationary boundary-ledger identity. Field energy linear in site rates has rate-independent field derivatives, but a hopping content energy is generally nonlinear in those rates. The stated weak-field family has exponent a/[2(ap-b)] under nondegenerate fixed-wall assumptions. The selected bilinear member has a unique positive finite-box diagonal-source solution, with charges given by a strictly convex minimum and a subsequent linear equation for N. Its single-source ledger is unbounded with bare mass; a fixed-diagonal pair derivative is negative. At linear order about a static uniform background, the specified quadratic length kinetics leave a grounded instantaneous constraint; this is not a general nonlinear no-propagation theorem. Positive uniform rest content in the chosen homogeneous kinetic model requires negative kinetic coefficient, including an exponential solution when s=0. No empirical deflection or complete dynamical theory is derived."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_2026_09_21.py
---

# Rate-linear field energies: stationary identities, a finite static solution, and restricted kinetic constraints

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 59 and one declared family of field energies; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for lengths of weight zero; it reports what a ledger linear in the rates does, in general and for one declared member; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Homogeneity gives an exact identity for a stationary ledger and its boundary derivatives. Linearity of the field energy alone does not make the entire hopping ledger linear in independent site rates: hopping contains square roots of products of rates. Its energy derivatives and hop sources retain that dependence. The subsequent linear solve is valid in the separately supplied diagonal rest-source sector.

The weak-field exponent is conditional on the specified nondegenerate scalar model. The bilinear member has an exact finite static solution with positive fields at every finite positive mass, and a ledger growing without bound as mass increases. Its far-field coefficient comparison has only the local ray interpretation of the corrected companion note. It is not an empirical or integrated deflection result.

The kinetic obstruction concerns a linearization about a static uniform background, quadratic length velocities, held boundaries and a nonzero mixed potential coefficient. It does not exclude nonlinear propagation, time-dependent backgrounds, other potentials or other fields. The uniform kinetic example has an exponential branch at s=0 as well as the stated power laws for s nonzero.

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

The declared models illustrate homogeneity, boundary summation and static elliptic identities. Their relationship to continuum curvature is a mathematical comparison, not a derivation of a physical field energy.

## Theorem T1 — the unit of rate as a variable

*Statement.* Let `𝓔` be of weight one: `𝓔(s w) = s 𝓔(w)` for `s > 0`, all rates scaled, all else fixed. (a) `Σ_x ∂𝓔/∂u_x = 𝓔`, the sum over all sites. (b) If `𝓔` is stationary in every `u_x`, then `𝓔 = 0`; a ledger that is positive at every configuration has no such stationary point. (c) If the rates of a set `W` of sites are held and `𝓔` is stationary in every other `u_x`, then `𝓔 = Σ_{x∈W} ∂𝓔/∂u_x`.

*Proof.* Differentiate `𝓔(e^s w) = e^s 𝓔(w)` at `s = 0`: (a). Then (b) and (c) are read off. Block 56's field energy is a sum of squares and its content positive, so (b) is block 55 T4(b); with held walls (c) is block 56's statement that the ledger is a surface term. ∎

## Theorem T2 — multiplier ledgers

*Statement.* Let `F = Σ_x w_x G_x(λ)` with `G_x` functions of the lengths alone. (a) `∂F/∂u_x = w_x G_x` and `∂²F/∂u_x∂u_y = 0` for `x ≠ y`: stationarity in `u_x` is `e_x = −w_x G_x(λ)`, and the field contribution to this rate derivative contains no neighbouring rate. The content term e_x can still depend on neighbouring rates. (b) Stationarity in `λ_z` is `Σ_x w_x ∂G_x/∂λ_z = τ_z`: the left side is linear in the rates. The full equation is generally nonlinear because tau_z contains hopping coefficients sqrt(w_x w_y). It is linear in rates for the diagonal rest-source case tau=0, not every amplitude. (c) For a bilinear member `G = c X ΔX`, `c > 0`, on a closed lattice there is no static configuration with `e ≥ 0`, `e ≢ 0`.

*Proof.* (a), (b) by differentiation; `∂⟨H⟩/∂λ_z = −τ_z` because the bonds at `z` are crossed at a rate proportional to `1/χ_z`. (c) The constraint is `(ΔX)_x = −e_x/(c w_x X_x) ≤ 0`, negative somewhere, while `Σ_x (ΔX)_x = 0` on a closed lattice. ∎

For content at rest `e_x/w_x = m_x`: the constraint holds no rate at all. It fixes the lengths from the bare energies; the rates come afterwards.

## Theorem T3 — the nearest-neighbour family and the exponent

*Statement.* (a) For `G = K ℓ^p (aΔλ + bq)` the part of `F` of second order in `(u − ū, λ)` is `K w̄ [a u·Δλ + (ap − b) λ·Δλ]`; there is no term in `u` alone. (b) With no hop energy and walls held, stationarity in the lengths gives `λ = −β (u − ū)`, `β = a/(2(ap − b))` (`a != 0`, `ap ≠ b`, positive K and wbar); stationarity in the rates gives `Δλ = −e/(aKw̄)`, so `Δu = 2(ap − b) e/(a²Kw̄)`: for `a, K > 0` lengths stretch near positive energy in every member, and clocks are slow there iff `ap > b` (the member `(4, 8, 1)` has fast clocks near a body). (c) The bilinear member `c X ΔX`, `X = ℓ^{p/2}`, agrees at second order with `(Ka, Kb) = (cp/2, cp²/4)`: `b = ap/2`, `β = 1/p` for p nonzero. (d) In the continuum, for the metric `ℓ² δ` in three dimensions, (volume density) × (scalar curvature) `= −8χ∇²χ = −ℓ(4∇²λ + 2|∇λ|²)`. (e) For the member `(a, b, p) = (4, 2, 1)` with hop energy: `Δλ = −e/(4Kw̄)`, `Δ(u + λ) = τ/(4Kw̄)`, so `Δu = (e + τ)/(4Kw̄)`; block 55's `γ` is `1/(4K)`.

*Proof.* (a) `e^{u} e^{pλ}(aΔλ + bq)` to second order is `aΔλ + (u + pλ)aΔλ + bq`; the first-order sum vanishes because every bond enters `ΣΔλ` twice with opposite signs, and `Σ_x q_x = −λ·Δλ`. (b) The gradient in `λ` is `Kw̄[aΔu + 2(ap − b)Δλ]`, in `u` it is `Kw̄ aΔλ`. (c) `X_x(X_y − X_x) = ℓ_x^p (e^{(p/2)d} − 1)`, `d = λ_y − λ_x`, is `ℓ_x^p((p/2)d + (p²/8)d² + …)`. (d) By direct computation of the curvature (runner C4). (e) From (b) with the source `τ_z` of T2(b); block 56's law is `Δu = γ e/w̄` at weak field. ∎

Under block 59 T4's same-location, parallel-gradient, massive-rest versus massless-axial transverse comparison only, the local acceleration ratio is `1 + β`. It is 2 for every member with `a = 2(ap − b)`; among bilinear members, for `p = 1` only. A walker with no rest energy has `e = τ` (block 59 T2): for equal nonnegative supplied source distributions in this linear scalar ansatz the clock source is twice the diagonal-rest one. Arbitrary hopping densities can have either sign; no universal moving-body statement follows.

## Theorem T4 — the strong field of the curvature member, exactly

*Setting.* The bilinear member with `p = 1`, `c = 8K`, in its bond form; bodies at rest at sites `x_i` with bare energies `m_i > 0`, `μ_i = m_i/(8K)`; walls held at `w = ℓ = 1`; `G_{ij} = g(x_i, x_j)`.

*Statement.* (a) `χ = 1 + Σ_i Q_i g(·, x_i)` with `Q_i χ(x_i) = μ_i`. The positive solution exists and is unique: it is the minimum of the strictly convex function `Φ(Q) = Σ Q_i + ½ Q·GQ − Σ μ_i log Q_i` on `Q > 0`. One body: `Q(1 + Qg_0) = μ`. (b) `N` solves the linear equation `(−Δ + Q_x/χ_x) N = 0`, `N = 1` on the walls: `N = 1 − Σ_i P_i g(·, x_i)` with `P_i = Q_i w_i`, and `0 < N ≤ 1`, so `0 < w ≤ 1`: no clock stops at any strength. One body: `P = Q/(1 + 2Qg_0)`, `w_0 = 1/(1 + 2Qg_0)`. Equivalently, at every interior site `w_z = κ_z × (Σ_y χ_y w_y/Σ_y χ_y)` over the six neighbours, `κ_z = 1/(1 + m_z/(4Kχ_z Σ_y χ_y))`. (c) The ledger of the box is the walls' term, `𝓔 = 8K Σ_i Q_i = Σ_i m_i/χ(x_i) < Σ m_i`. One body: `M = 8KQ` solves `M + M²g_0/(8K) = m`; it exceeds block 56's `m/(1 + m g_0/(8K))` (with `γ = 1/(4K)`), agrees with it through `m − m²g_0/(8K)`, and is unbounded, growing as `√(8Km/g_0)`, where block 56's was bounded by `8K/g_0`. For several bodies each `Q_i` is smaller than the charge the body would carry alone, and for two bodies `∂(Q_1 + Q_2)/∂G_{12} < 0` holding diagonal entries and bare masses fixed. Motion in a box changes more than this entry, so this is not a general force law. (d) In the formal weak-exterior expansion in g for one body `χ − 1 = Qg` and `1 − N = Pg`: the lengths carry `2Q`, the rates `P + Q`, and the corresponding same-location transverse ray coefficient ratio is `1 + 2Q/(P + Q) = 1 + (1 + 2Qg_0)/(1 + Qg_0)`, whose limit as Q tends to zero is 2 and which lies strictly between 2 and 3 for finite positive Q. This compares leading weak-exterior coefficients, not a globally uniform finite-box ratio or integrated deflection.

*Proof.* (a) Off the bodies the constraint is `Δχ = 0`; at a body `(Δχ)(x_i) = −μ_i/χ(x_i) =: −Q_i`. `∂Φ/∂Q_i = 1 + (GQ)_i − μ_i/Q_i = χ(x_i) − μ_i/Q_i`; `G` is positive definite and `−log` convex, and `Φ → ∞` at the boundary of the orthant and at infinity. (b) `F = 8K Σ_x N_x (Δχ)_x` over all sites, and `Δ` is symmetric, so `∂F/∂χ_z = 8K[w_z(Δχ)_z + (ΔN)_z]`, with `N = 1` on the walls because the walls' terms are part of the bond form. Setting it to zero with `(Δχ)_z = −Q_z`: `(ΔN)_z = (Q_z/χ_z) N_z`. If `N` had a non-positive minimum at an interior site, `ΔN ≥ 0` and `(Q/χ)N ≤ 0` there force `N` equal at the neighbours, and so on to the walls, where `N = 1`. `P_i = (ΔN)(x_i) = Q_i N_i/χ_i = Q_i w_i`. For one body `P = (Q/χ_0)(1 − Pg_0)`. The weighted-mean form is `w_z(6χ_z − (Δχ)_z) = Σ_y χ_y w_y` rewritten. (c) T1(c): the walls' term is `8K Σ_{x∈W}(Δχ)_x`, and the sum of `Δχ` over all sites of the box vanishes, so it equals `8K Σ Q_i`. `χ_0 = 1 + Mg_0/(8K) < 1 + m g_0/(8K)` gives the comparison. If `Q_i^0` is the charge alone, `Q(1 + G_{ii}Q) − μ_i` is increasing and negative at `Q_i`. Differentiating the two-body equations in `G_{12}` gives `(D + G) dQ = −(Q_2, Q_1)ᵀ dG_{12}` with `D = diag(χ_i/Q_i)`, and `1ᵀ(D + G)^{-1}(Q_2, Q_1)ᵀ > 0` because `G_{ii} > G_{12}`. (d) By (a), (b). ∎

At weak field `log κ = −m/(24K) = −(γ/6) m`: block 55's Corollary. The rule "a rate is a factor times a mean of its neighbours' rates" of block 53 holds at every strength, with the lengths as weights.

## Theorem T5 — motion of the lengths

*Statement.* (a) Linearize about a static uniform background with zero length velocities, positive K and wbar, nonzero a, fixed walls, and a smooth kinetic term quadratic in length velocities and containing no rate velocities. Then the equations of the rates remain constraints, and at first order in the fields `Δλ = −e/(aKw̄)` holds at each label time, with `Δu` fixed at that label time by the content and the second rate of change of the lengths: there is no independent free scalar wave in this constrained linearized system. The equation for u can depend on source time derivatives through lambda; this is not a general nonlinear signaling statement. (b) On a closed lattice with content at rest, positive constant `m` per site, and the kinetic term `Σ c_k ℓ^s (dλ/dt)²/w`, a uniform solution exists iff `c_k < 0`. In the label with `w = 1`: `m = |c_k| ℓ^s (dλ/dt)²`, `2λ̈ + s λ̇² = 0`, `ℓ = (1 + t/t_0)^{2/s}`, `t_0 = (2/s)√(|c_k|/m)` for s nonzero, normalized initial length one, on an interval with positive bracket. The opposite sign of t_0 is the other branch. At s=0, `lambda=lambda_0 +/- sqrt(m/|c_k|)t`, so length is exponential. For general initial length and s nonzero, `ell^(s/2)=ell_0^(s/2) +/- (s/2)sqrt(m/|c_k|)t`. In all cases the rate of change of the constraint is `−λ̇` times the lengths' equation, so the constraint is kept.

*Proof.* (a) No `du/dt` appears, so stationarity in `u_x` is `e_x + w_x G_x +` (terms quadratic in the lengths' rates of change) `= 0`; the last are of second order. (b) Stationarity in `w` of `c_k ℓ^s λ̇²/w − mw` is `m w² + c_k ℓ^s λ̇² = 0`; the rest by differentiation (runner E2). ∎

The comparator's values are `s = 3` (the volume) and `c_k = −6K`. The corrected block 57 distinguishes its flat-band reduced model from more general gapped dispersions; lack of an acoustic branch is not a universal no-propagation result.

## Historical experiments — deferred

Original nonlinear root searches, numerical continuation, kinetic simulations and comparator reports remain on the original PR branch. They have not been reproduced as canonical evidence in this landing. The exact runner supplies the bounded finite identities described in its cache.

## No-Go Discipline Gate

The note's negative sentences: a positive ledger has no stationary point once the unit of rate is varied; a closed lattice has no static configuration with positive content; the rates have no stiffness of their own; the far-field coefficients of a body pinned at rest agree only at first order; the specified static-background linear scalar system has an instantaneous grounded constraint.

### N1 — Routes by which the sentences could fail
1. *The direction-dependent parts.* Block 59's bond rates have two modes beyond the isotropic one. Nothing here says they carry no delay; this note holds them at rest. They are the named next step.
2. *Internal motion.* `Δu = (e + τ)/(4Kw̄)`: hop energy raises `P`. Whether a bound body's internal hop energy brings `P` up to `Q` is not examined.
3. *A closed lattice that moves.* T5(b) is the exit from T2(c), and needs `c_k < 0`.
4. *Field energies not linear in the rates.* Outside T2; blocks 55 and 56 are that case.
5. *Kinetic terms with rates' rates of change.* Differences only are covariant (block 57 T1) and only the specified reduced nearest-neighbour model has flat dispersion (corrected block 57 T2); a mixed term with the lengths' rates is not examined.
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
| "weight one and the walls' term; field multipliers; `β = a/(2(ap − b))`, `1/p`, the curvature identity; the exact static field; constrained linear scalar dynamics, uniform motion iff `c_k < 0`" | executed: both ledgers on a `5³` box with a hopping rational amplitude: weight one, the sum of `w ∂𝓔/∂w` by exact differences, additivity of the field term in the rates, not the hopping contribution | executed: both stationarity conditions at all 125 interior sites of a `7³` box for one and for three bodies; the rate at each body; `P_i = Q_i w_i`; the weighted-mean rule | executed: exact second-order jets of six members and three bilinear members; `β` by exact differences; the curvature identity by exact symbolic algebra | executed: the ledger against the wall term, the bare energies and block 56; convexity; the far-field coefficients; the closed lattice; the uniform motion and its constraint | T1 every ledger of weight one; T2 every field energy linear in the rates; T3 the members named, second order; T4 bodies at rest, held walls, the curvature member, isotropic stretching; T5 second order and uniform configurations; lengths, linearity in the rates, the member, `K`, `p`, `s`, the sign of `c_k` not derived |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository; it is not used, and whether it bears on the sign or size of `c_k` is not decided here. `scale_reference_primitive` converts units and fixes no `K`. `realized_state_primitive` grants evaluation at a supplied state. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You have written down the comparator and found that it is the comparator." Reply: the note says so, under the Premises. What it adds is where the comparator's structure sits in the framework's objects and what is and is not forced there. Forced, given a ledger of weight one: the walls' term (T1). Forced, given linearity in the rates: multipliers, no stiffness, the closed-lattice statement (T2). Not forced: linearity in the rates itself, `p`, `K`, `c_k`. The owner's decision record should carry those three lists. Second objection: "`P ≠ Q` contradicts the comparator's static solution." Reply: there the two agree because the body's stresses are counted; a body pinned at rest on one site has none, and T3(e) shows which term would supply them. Third objection: "No delay again; then what is the point of lengths?" Reply: the isotropic part is one of three modes of block 59's bond rates. The statement narrows where a delay can live.

### N8 — Cross-cycle echo
Block 53: a rate is a factor times the mean of its neighbours' rates; here the same rule at every strength, weighted by the lengths, with `κ` in closed form. Block 55: the unit of rate is not a variable; here the premise that made it so (`F ≥ 0`) is what a weight-zero field removes. Block 56: the ledger is a surface term, bounded; here a surface term again, unbounded. Block 57: one reduced nearest-neighbour model has flat dispersion. Here the specified grounded linear scalar system has no independent free wave; neither statement proves a universal absence of propagation. Block 59: `β` free; here `β` on two families.

## Falsifiers

- A ledger of weight one whose derivatives in all the log-rates do not sum to it.
- A field energy linear in the rates whose rate equations contain a difference of rates coming from `F`.
- A nearest-neighbour member of the stated form whose body at rest gives `λ ≠ −β(u − ū)` at second order with `β = a/(2(ap − b))`.
- A second positive solution of `Q_i χ(x_i) = μ_i`; a box in which the curvature member's ledger is not `Σ m_i/χ_i`; a clock that stops.
- An independent free scalar wave in the stated linearized grounded nondegenerate model, with smooth quadratic length kinetics about a static zero-velocity background.

## Boundaries and non-claims

Lengths, and that the field energy is counted per local tick, are supplied. The members are declared; `K`, `p`, `s` and the sign of `c_k` are not derived, and the continuum identity names a member without forcing it. Only the isotropic part of block 59's bond rates is kept; whether the other two modes can stay at rest, and whether they carry a delay, is not examined. Bodies are pinned at rest; a bound body with internal motion is not examined, and neither is the constancy of the walls' term while content moves. The stationary points are saddles, and nothing is said about stability. The comparator's values are quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the covariance sentence of Admissibility, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 59 and the decision record (PRs #8568, #8570, #8571, #8573, #8578, #8579, #8581, #8572, open): restated or placed.
- Named standard imports at definition level: the degree-one identity for homogeneous functions; the symmetry and the maximum principle of the lattice Laplacian with held walls; strict convexity and uniqueness of a minimum; second-order expansions; the scalar curvature of a metric from its connection; stationarity of a Lagrangian.
- Reference only: Arnowitt, Deser and Misner; Lichnerowicz; York; Brill and Lindquist; Isenberg; Wilson and Mathews; Schwarzschild; Tolman; Komar; Friedmann; Brans and Dicke; Einstein (1912).

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8568](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8571](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8573](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8578](ADMISSIBILITY_RULE_A_DELAY_FOR_THE_RATE_FIELD_NEIGHBOUR_REFERRED_MOTION_DOES_NOT_PROPAGATE_A_REFERENCE_TO_DISTANT_CLOCKS_DOES_AT_A_SPEED_SET_BY_THE_LOCAL_RATE_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8581](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

Original author history and auxiliary controls are preserved at PR #8590 head `ec3a6abdf004d9fa5accbbcf4464b23812cc2aac`, branch `physics-loop/admissibility-induced-law-block60-the-geometric-member-rates-as-multipliers-energy-tied-to-curvature-20260921`. Landing review distinguishes field linearity from hopping-energy nonlinearity, restricts kinetic quantifiers and ray comparisons, and adds the missing s=0 uniform solution. Auxiliary results remain deferred; review is not an independent audit verdict.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_2026_09_21.py
```

The fresh cache records the executed check count.
