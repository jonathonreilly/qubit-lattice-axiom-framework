---
claim_id: admissibility_rule_three_lengths_per_site_a_body_at_rest_stretches_them_alike_hop_energy_drives_whole_columns_and_the_delays_speed_depends_on_direction_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53 to 60 (open PRs #8568, #8570, #8571, #8573, #8578, #8579, #8581, #8590; not adopted), WIDENED from block 60's one length per site to one length for each axis at every site, l_j = exp(lam_j), the bond from x along j having length sqrt(l_j(x) l_j(x + e_j)); tau_j(x) is half the hop energy of the two bonds along j at x. DECLARED MEMBER, at second order in the fields: F_2 = K wbar [2 u.sum_j (Lap - D_j) lam_j + 2 (lam_1.D_3 lam_2 + lam_1.D_2 lam_3 + lam_2.D_1 lam_3)], D_i the second difference along axis i; kinetic terms T_2 = (1/wbar)[M_1 sum_j (dlam_j/dt)^2 + M_2 sum_{i<m} (dlam_i/dt)(dlam_m/dt)], the comparator's values being M_1 = 0, M_2 = -2K. (T1) For the metric diag(l_1^2, l_2^2, l_3^2), volume density times scalar curvature is -2 sum_j sum_{i != j} d_i^2 lam_j at first order and, up to a total derivative, 2 (d_3 lam_1 d_3 lam_2 + d_2 lam_1 d_2 lam_3 + d_1 lam_2 d_1 lam_3) at second order: each pair of lengths is coupled through differences along the third axis and no length has a term of its own; with equal lengths it is block 60's member; the kinetic density with no sliding of sites is -2 sum_{i<m} (dlam_i/dt)(dlam_m/dt)/w^2. (T2) With held walls the static equations have exactly one solution, and for content at rest it has lam_1 = lam_2 = lam_3 = -(u - ubar) with 4K wbar Lap lam = -e: the three lengths stretch alike and block 60's law holds. (T3) With hop energy, a_j = lam_j + u - ubar obeys D_3 a_2 + D_2 a_3 = tau_1/(2K wbar) and its two rotations, solved by inverses of ONE-dimensional second differences: for tau_1 alone a_2 = D_3^{-1} tau_1/(4K wbar), a_3 = D_2^{-1} tau_1/(4K wbar), a_1 = -D_1 D_2^{-1} D_3^{-1} tau_1/(4K wbar). A point of hop energy changes lengths along whole lattice columns, as a tent whose height -(n + 1)/(16 K wbar) grows with the distance to the walls; equal hop energies along the three axes do the same; block 60's equal-lengths law with hop energy does not solve the wider equations. The rates still obey Lap u = (e + tau)/(4K wbar) exactly. (T4) On a torus, with a = 4 sin^2(k_1/2) and so on, s = a + b + c, sigma = ab + ac + bc, pi = abc, the squared frequencies X of travelling disturbances solve (2M_1 - M_2)(M_1 s^2 - (M_1 + M_2) sigma) X^2 - 2K wbar^2 (M_1 s^3 - (2M_1 + M_2) s sigma + 3(M_1 + M_2) pi) X + 4 K^2 wbar^4 pi s = 0. For the comparator's kinetic term v = X/(wbar^2 s) obeys v_1 + v_2 = 1 - 3 rho, v_1 v_2 = rho, rho = pi/(s sigma) in [0, 1/9]: real and non-negative; v = 1 and 0 in the coordinate planes, 1/3 twice on the body diagonals: the speed depends on direction at EVERY wavelength. For no (M_1, M_2) other than zero does any disturbance travel at a direction-free speed. EXECUTED, NOT CLAIMED: a real-space evolution of the constrained lattice system on a 12^3 torus keeps the constraint to 1e-11 and shows spectral peaks at the closed form's frequencies; a grid search over kinetic terms finds no relative spread of the fast speed over directions below 0.19. NOT claimed: that a site has three lengths; the member or its numbers; any statement beyond second order; that other variables (angles between bonds, sliding of sites) exist or what they would do; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_three_lengths_per_site_a_body_at_rest_stretches_them_alike_hop_energy_drives_whole_columns_2026_09_21.py
---

# Three lengths per site under the curvature member: a body at rest stretches them alike, hop energy drives whole columns, and the delay's speed depends on direction

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements at second order within the supplied clauses of blocks 53 to 60, widened to a length for each axis, for one declared member; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for lengths of weight zero, with one length for each axis at every site and one declared member of the ledger at second order; it reports what such lengths do at rest and in motion; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 60 (open PR #8590) kept one length per site — the same stretching in every direction — and found that such lengths carry no delay at all, whatever kinetic term they are given. It named the next step: the direction-dependent parts. Block 59 (open PR #8581) had found that a walker loads only the bonds it crosses, so content in motion sources the three directions unequally. This note gives every site three lengths, one for each axis, keeps block 60's member (rate × volume × curvature, now for a box-shaped stretching), and asks three questions at second order.

1. **Where the member comes from.** For three lengths the curvature couples each *pair* of lengths through their differences along the *third* axis, and nothing else: no length has a gradient term of its own. With the three equal it is block 60's member (T1).
2. **A body at rest.** The static equations with held walls have exactly one solution, and for content at rest the three lengths stretch alike and obey block 60's law. Block 60's restriction was harmless there (T2).
3. **Hop energy.** It is not harmless for content that moves. The combinations `a_j = λ_j + u` obey equations whose inverses are *one-dimensional*: a point of hop energy along one axis changes the other two lengths along whole lattice columns through it, as a tent that reaches the walls and whose height grows with the box. Equal hop energies along the three axes do the same. The rates, remarkably, still obey block 60's law `Δu = (e + τ)/(4Kw̄)` exactly; it is the lengths that go wrong (T3).
4. **The delay.** Disturbances of the three lengths do travel — two of them at each wave vector. But for the comparator's kinetic term their speeds are fixed by one angular quantity `ρ`: squared speed 1 (and a static mode) in the coordinate planes, 1/3 twice along the body diagonals, two unequal speeds in between — *at every wavelength*, not as a lattice correction. And no kinetic term of the covariant two-number family gives any disturbance a direction-free speed (T4).

In plain terms: three stretch factors per site are enough for bodies that sit still and not enough for anything that moves. Motion drives the lengths along whole rows of the lattice instead of producing a field that falls off, and ripples in the lengths run √3 slower along a cube's diagonal than along its faces however long the ripple. The comparator avoids both with variables this picture does not have: the angles between the bonds and the sliding of sites. So if the owner's forks 6 (lengths) and 7 (delay) are to be closed along this line, lengths along the bonds alone will not do it.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 60 (PR #8590), next_trace_action: 'the direction-dependent parts of the lengths (block 59's bond rates) under a ledger linear in the rates: whether they carry a delay and at what speed'; block 60, Boundaries: 'whether the other two modes can stay at rest ... is not examined'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "three lengths AND three angles per site (the full symmetric stretching) under the same member: whether the column-long responses go away and the travelling disturbances get one direction-free speed; what sources the angles; whether sliding of sites is needed as well"
conditional_surface_status: "T1 exact (continuum identity); T2 exact for every box with held walls and content at rest; T3 exact for every box and every distribution of hop energy; T4 exact for every wave vector of a torus and every kinetic term of the two-number family; all at second order, for the declared member"
hypothetical_axiom_status: "blocks 53 to 60's clauses; a length for each axis at every site; the declared member at second order; a kinetic term of the stated family; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the covariance sentence of Admissibility, and its silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 60 (open PRs) supply the rates, the clocked amplitudes, the ledger, lengths as pure numbers, hop energy, and the ledger linear in the rates with its curvature member.

- **Three lengths.** `ℓ_j(x) = e^{λ_j(x)}`, `j = 1, 2, 3`; the bond from `x` along `j` has length `√(ℓ_j(x) ℓ_j(x + e_j))`. **Hop energy** `τ_j(x)`: half the hop energy of the two bonds along `j` at `x`, so `∂⟨H⟩/∂λ_j(x) = −τ_j(x)`; `τ = Σ_j τ_j` is block 60's.
- **Operators.** `D_i` the second difference along axis `i`; `Δ = D_1 + D_2 + D_3`. On a box with held walls the fields vanish on the walls (`u` measured from `ū`).
- **The member (second order).** `F_2 = K w̄ [2 u·Σ_j (Δ − D_j) λ_j + 2(λ_1·D_3 λ_2 + λ_1·D_2 λ_3 + λ_2·D_1 λ_3)]`: minus `K w̄` times the first- and second-order parts of volume × curvature (T1) with derivatives replaced by differences. With `λ_j = λ` it is block 60's `K w̄ [4u·Δλ + 2λ·Δλ]`.
- **Kinetic terms.** `T_2 = (1/w̄)[M_1 Σ_j λ̇_j² + M_2 Σ_{i<m} λ̇_i λ̇_m]`: the two quadratic invariants of three rates of change under permutations of the axes. No rate of change of a rate appears (block 60 T5).
- **Static equations.** `2K w̄ [D_3(λ_2 + u) + D_2(λ_3 + u)] = τ_1` and its two rotations; `2K w̄ Σ_j (Δ − D_j) λ_j = −e`.
- **Wave vectors.** `a = 4 sin²(k_1/2)`, `b`, `c` likewise; `s = a + b + c`, `σ = ab + ac + bc`, `π = abc`, `ρ = π/(sσ)`.

A metric that is diagonal in fixed coordinates, with the rate of clocks as a multiplier and no sliding of the coordinates, is a truncation of the formulation of Arnowitt, Deser and Misner in which the three off-diagonal components and the shift are absent; the equations that are lost with them are the off-diagonal field equations and the momentum constraints, and what those enforce on the sources is the conservation of stress. The two transverse disturbances of the full theory and their single speed are Einstein's of 1916 and 1918; the quadratic form of a symmetric tensor field whose restriction appears in T1 is that of Fierz and Pauli. Lengths on the bonds of a lattice are the calculus of Regge, which assigns lengths to diagonals as well. None is used as authority; the comparator is quoted as a comparator.

## Prior art and what is new

Every piece is classical. What is new is the statement inside the framework's vocabulary: that block 60's restriction to one length per site is exact for content at rest and fails for any hop energy; that the failure has a definite form — inverses of one-dimensional second differences, tents along lattice columns whose height grows with the box — while the rates keep block 60's law exactly; that the travelling disturbances of three lengths have speeds given in closed form by one angular quantity, direction-dependent at zeroth order in the wavelength; and that no kinetic term of the covariant family repairs this. The consequence for the owner's forks is a narrowing: lengths along the bonds are not enough. No gravitational claim is made.

## Exact target and obligation graph

Target: what three lengths per site do under block 60's member. Obligations: (O1) the member for three lengths; (O2) content at rest; (O3) hop energy; (O4) travelling disturbances and their speeds. T1–T4 discharge them.

## Theorem T1 — the member for three lengths

*Statement.* For the metric `diag(ℓ_1², ℓ_2², ℓ_3²)`, `ℓ_j = e^{ελ_j}`: (a) volume density × scalar curvature `= −2ε Σ_j Σ_{i≠j} ∂_i² λ_j + O(ε²)`; (b) its part of order `ε²` has the same variational derivatives as `2(∂_3λ_1 ∂_3λ_2 + ∂_2λ_1 ∂_2λ_3 + ∂_1λ_2 ∂_1λ_3)`; (c) with `λ_j = λ` these are `−4∇²λ` and `2|∇λ|²`; (d) with lengths changing in the label and no sliding of sites, the kinetic density is `−2 Σ_{i<m} λ̇_i λ̇_m/w²`, which is `−6λ̇²/w²` for equal lengths.

*Proof.* Direct computation of the curvature from the connection, expanded to second order (runner B1, B2). ∎

So `∂_jλ_j`, the change of a length along its own axis, does not enter, and neither does any `(∂_kλ_i)²`: the form is purely a coupling of pairs.

## Theorem T2 — a body at rest stretches the three lengths alike

*Statement.* On a box with held walls the static equations have exactly one solution for every `e` and `τ_j`. For `τ_j = 0` it is `λ_1 = λ_2 = λ_3 = λ`, `u − ū = −λ`, `4K w̄ Δλ = −e`.

*Proof.* The `D_i` commute, and minus a one-dimensional second difference with zero walls is positive definite (its leading minors are `2, 3, …, n + 1`), so in a common eigenbasis `D_i = −a, −b, −c` with `a, b, c > 0`. The three equations for `a_j = λ_j + u` have the matrix `[[0, c, b], [c, 0, a], [b, a, 0]]` of determinant `2abc ≠ 0`: `a_j` is fixed by the `τ`'s, and is zero when they are. Then `λ_j = −u` and the constraint reads `−2Δu = −e/(2Kw̄)`. ∎

On a closed lattice some of `a, b, c` vanish and the determinant with them: block 60 T2(c) already excludes static configurations there.

## Theorem T3 — hop energy drives whole columns

*Statement.* (a) `a = (a_1, a_2, a_3)` is `1/(2Kw̄)` times the inverse of the matrix above applied to `(τ_1, τ_2, τ_3)`, written with the operators `D_i` in place of `−a, −b, −c`, and that inverse is `(1/(2 D_1 D_2 D_3)) [[−D_1², D_1D_2, D_1D_3], [D_1D_2, −D_2², D_2D_3], [D_1D_3, D_2D_3, −D_3²]]`: for `τ_1` alone, `a_2 = D_3^{-1}τ_1/(4Kw̄)`, `a_3 = D_2^{-1}τ_1/(4Kw̄)`, `a_1 = −D_1 D_2^{-1} D_3^{-1} τ_1/(4Kw̄)`. (b) For a point of hop energy at the centre of a box with `n` interior sites across, `a_2` is zero off the column through the source along axis 3, and on it is the tent `−min(z, z_0)(n + 1 − max(z, z_0))/((n + 1)·4Kw̄)`, of height `−(n + 1)/(16Kw̄)` at the source. (c) Equal hop energies `τ_j = τ/3` leave `a_1 = (τ/(12Kw̄))[D_3^{-1} + D_2^{-1} − D_1 D_2^{-1} D_3^{-1}]δ ≠ 0`; block 60's equal-lengths law `Δ(u + λ) = τ/(4Kw̄)` does not satisfy the wider equations. (d) The rates obey `Δ(u − ū) = (e + τ)/(4Kw̄)` exactly.

*Proof.* (a) Invert the `3 × 3` matrix of commuting operators. (b) The inverse of a one-dimensional second difference with zero walls is the tent. (c) By linearity and rotation; the equal-lengths law would need `(D_2 + D_3)(u + λ) = τ_1/(2Kw̄)`, which fails one site from the source, where `τ_1 = 0` and `(D_2 + D_3)Δ^{-1}δ ≠ 0`. (d) Put `λ_j = a_j − u` in the constraint: `Δu = e/(4Kw̄) + ½Σ_j (Δ − D_j) a_j`, and with (a) the sum is `Σ_j τ_j/(2Kw̄)` — for `τ_1` alone the terms in `D_1/D_2` and `D_1/D_3` cancel in pairs and `½ + ½` remains. ∎

So the clocks respond to moving content as block 60 said, by a field that falls off. The lengths do not: their response is not a field that falls off in every direction, and its size is set by the distance to the walls.

## Theorem T4 — travelling disturbances and their speeds

*Statement.* (a) On a torus the amplitudes `(A_1, A_2, A_3, U)` of a disturbance `∝ cos(ωt) cos(k·x)` satisfy a linear system whose determinant is a non-zero multiple of the quadratic in `X = ω²`, `(2M_1 − M_2)(M_1 s² − (M_1 + M_2)σ)X² − 2Kw̄²(M_1 s³ − (2M_1 + M_2)sσ + 3(M_1 + M_2)π)X + 4K²w̄⁴πs`: two travelling disturbances at a generic wave vector. (b) For `M_1 = 0`, `M_2 = −2K`: `σX² − w̄²(sσ − 3π)X + w̄⁴πs = 0`; with `v = X/(w̄²s)`, `v_1 + v_2 = 1 − 3ρ`, `v_1v_2 = ρ`, discriminant `(1 − ρ)(1 − 9ρ) ≥ 0` since `9abc ≤ (a + b + c)(ab + ac + bc)`. In a coordinate plane (`π = 0`): `v = 1` and `v = 0`. On a body diagonal (`a = b = c`): `v = 1/3` twice. (c) Let `(M_1, M_2) ≠ (0, 0)`. There is no `v_0` such that `X = v_0 w̄² s` is a root for all directions.

*Proof.* (a), (b) By expansion (runner E1, E2); `ρ ≤ 1/9` is the inequality of the arithmetic and geometric means applied to `a + b + c` and to `ab + ac + bc`. (c) With `m = M/K`, `σ̂ = σ/s²`, `π̂ = π/s³`, which vary independently with direction, the quadratic at `X = v_0 s` is `(2m_1 − m_2)(m_1 − (m_1 + m_2)σ̂)v_0² − 2(m_1 − (2m_1 + m_2)σ̂ + 3(m_1 + m_2)π̂)v_0 + 4π̂`. Its coefficient of `π̂` gives `v_0 = 2/(3(m_1 + m_2))`; its constant term gives `m_1 = 0` or `v_0 = 2/(2m_1 − m_2)`. If `m_1 = 0` the coefficient of `σ̂` is `m_2²v_0² + 2m_2v_0 = 4/9 + 4/3 ≠ 0`. Otherwise `2m_1 − m_2 = 3(m_1 + m_2)`, the coefficient of `σ̂` reduces to `2m_1v_0`, so `m_1 = 0`, then `m_2 = 0`. The runner confirms that the three conditions generate the whole polynomial ring (E4). ∎

The statement is exact in `a, b, c`, hence holds at every wavelength: as `k → 0`, `a → k_1²` and `ρ` tends to a function of direction alone. Block 54's walker is direction-dependent at second order in the wave vector; these disturbances are at zeroth order — as block 51 found for the record layer's wind.

Along a lattice axis the determinant vanishes identically: the length along that axis is arbitrary there and is compensated by the rates (a relabelling of the sites of a line); the disturbance `λ_1 = −λ_2` travels with `X = w̄²c`.

## Executed (supervisor controls; floating point; evidence, not proof)

`specs/supervisor_control_block61_three_lengths.py`: the static matrix of a `7³` box has smallest singular value 0.038; a body at rest gives three equal lengths to `10⁻¹⁶` and block 60's value; a unit of hop energy along axis 1 gives tents of height `−0.375, −0.625, −0.875` for boxes `7³, 11³, 15³` (that is `−(n + 1)/16`, `K = 1`), zero one site off the column; mode speeds from the `4 × 4` matrix agree with the closed form in `ρ` to six digits at seven wave vectors; a time integration of one mode gives `ω² = 0.70806` against `0.70799`. `specs/supervisor_control_block61_refuter.py`: see the Review record.

## No-Go Discipline Gate

The note's negative sentences: block 60's equal-lengths law does not survive hop energy; the response of the lengths to hop energy is not a field that falls off; no kinetic term of the family gives a direction-free speed.

### N1 — Routes by which the sentences could fail
1. *Other variables.* Angles between the bonds (three more numbers per site) and sliding of sites. Not examined; the named next step. The comparator has both.
2. *Other members.* The theorems are for the declared member. A member in which each length has a gradient term of its own (three scalars) has direction-free speeds trivially and is not the curvature of anything; what bending it gives is not examined.
3. *Sources whose hop energies balance.* The column-long response is the inverse of a matrix applied to `(τ_1, τ_2, τ_3)`; distributions with `−D_1τ_1 + D_2τ_2 + D_3τ_3` in the range of `D_2D_3` (and rotations) have local responses. Whether the amplitudes' own equations put them there is not examined.
4. *Beyond second order.* Not examined.
5. *Kinetic terms with differences between sites.* They change the speeds at higher order in the wave vector, not at zeroth.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Second order throughout. Lengths live on sites, one for each axis; block 59's bond lengths are the geometric means of neighbouring ones. The member's lattice form replaces derivatives by nearest differences; T3 and T4 depend on it only through the `D_i`. Walls held in T2, T3; a torus in T4. `K > 0`.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its rotations; the covariance sentence; the absences that motivate the clauses | yes (premise) |
| block 60 (open PR #8590) | the ledger linear in the rates, the curvature member, the multiplier structure, T3(e), T5 | yes (restated) |
| block 59 (open PR #8581) | lengths, hop energy by direction | yes (restated) |
| blocks 51, 54 (open PRs #8563, #8570) | direction dependence elsewhere in the campaign | placement |
| decision record (open PR #8572) | forks 6 and 7 | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "pairs coupled along the third axis; alike at rest, uniquely; columns for hop energy, rates unharmed; speeds by `ρ`, no direction-free speed for any kinetic term" | executed: both orders of volume × curvature for three lengths and the kinetic density, by exact symbolic algebra; equal lengths | executed: the 108 static equations of a `5³` box; the three equations at all 125 sites of a `7³` box; the constraint after an exact solve for the rates | executed: the mode determinant in symmetric functions; coordinate planes and body diagonals; two disturbances at `(π/3, π/3, π)` at all 72 sites of a `6×6×2` torus | executed: tent height against box size; equal hop energies; the equal-lengths law's residual; the reduced basis of the isotropy conditions | T1 every diagonal metric; T2 every box and content at rest; T3 every box and hop energy; T4 every wave vector and kinetic term of the family; second order, the declared member; three lengths, the member, `K`, `M_1`, `M_2`, other variables not derived |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository; it says nothing about a speed's dependence on spatial direction and is not used. `scale_reference_primitive` and `realized_state_primitive` are not used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A diagonal metric with no shift is a bad gauge; of course it misbehaves." Reply: in the comparator it is a choice of coordinates that cannot in general be made; here it is not a choice at all — a lattice with a length on each bond *is* this, and the note's content is that the picture of block 59, taken with block 60's member, inherits exactly those defects, in closed form. Second objection: "Then use another member." Reply: N1 route 2; the member is the one that gave block 60 its `β = 1`, and the owner should see what it costs before the vocabulary is widened. Third objection: "The tents are an artefact of a static source that does not conserve its stress." Reply: yes, and the note says which combinations of hop energies have local responses; but nothing in the clauses so far conserves anything of the kind, so the defect is real for them.

### N8 — Cross-cycle echo
Block 51: the record layer's wind is direction-dependent at every distance. Block 54: the walk's fall is direction-dependent at second order only. Block 59: the anisotropic parts of bond rates are slaved at rest. Block 60: the isotropic lengths carry no delay. Here: three lengths are alike at rest (consistent with blocks 59 and 60), carry a delay, and carry it at a direction-dependent speed at zeroth order.

## Falsifiers

- A box with held walls and content at rest whose three lengths differ, or a second static solution.
- A point of hop energy whose `λ_2 + u` is non-zero off its column, or whose tent's height does not grow with the box.
- A wave vector at which the squared frequencies are not the roots of the stated quadratic; a direction off the coordinate planes with `v = 1` for the comparator's kinetic term.
- A kinetic term `(M_1, M_2) ≠ 0` with a disturbance whose speed is the same in all directions.

## Boundaries and non-claims

Three lengths per site are supplied, and the member is declared and used at second order only. Nothing is said about angles between bonds, sliding of sites, other members, or higher orders. The bending of rays in direction-dependent lengths is not computed. Stability of the disturbances is shown only for the comparator's kinetic term (real, non-negative squared frequencies). The comparator is quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the covariance sentence of Admissibility, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 51, 54, 59, 60 and the decision record (PRs #8563, #8570, #8581, #8590, #8572, open): restated or placed.
- Named standard imports at definition level: the scalar curvature of a metric from its connection; variational derivatives; commuting symmetric matrices and their common eigenbasis; the inverse of a one-dimensional second difference; symmetric functions; the inequality of the arithmetic and geometric means; reduced bases of polynomial ideals.
- Reference only: Arnowitt, Deser and Misner; Einstein (1916, 1918); Fierz and Pauli; Regge.

## Review record
Supervisor-run block, the ninth of the source-link direction and the fifth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: three lengths per site are a widening of block 60's one and a re-parametrisation of block 59's bond lengths; the member is declared at second order only and the note must say that every statement is about that member. A rigour lens: the supervisor's first reading of the scratch algebra was that nothing travels off the lattice axes; adding the rates to the mode equations (they are multipliers, not zero) showed two travelling disturbances at every generic wave vector, and the claim became the closed form in `ρ`. The first version of the runner tested the equal-lengths law at the source, where it passes by symmetry; the residual sits one site away and the check was moved there. The identity that the rates keep block 60's law exactly was found while asking what block 60 T3(e) still means, and was added. A comparator lens: what is missing is known — off-diagonal components, the shift, and the conservation they enforce — and is named under the Premises, not claimed. A strategy lens: the owner needs the narrowing in one sentence — lengths along the bonds alone do not close forks 6 and 7 under this member. Refuting pass (`specs/supervisor_control_block61_refuter.py`, machinery disjoint from the runner's): W1 the mode determinant derived afresh by symbolic differentiation of the quadratic form: equal to the runner's formula; W2 a real-space evolution of the constrained system on a `12³` torus from a random start, 6000 steps: the constraint is kept to `10⁻¹¹` and the spectral peaks sit at 0.733, 0.524, (0.524, 1.571), 1.152 against 0.732, 0.518, (0.506, 1.562), 1.126, within the resolution 0.05; W3 a `25 × 25` grid of kinetic terms, 200 random directions: the relative spread of the fast speed is never below 0.19 (0.20 for the comparator's term); W4 equal hop energies on a `9³` interior by a brute-force solve of all 2916 equations: `λ_1 + u` reaches 0.667 on the columns, lives on three planes, and is `2×10⁻¹⁴` elsewhere; W5 a body at rest next to a wall: the three lengths alike to `10⁻¹⁵`. All pass. Mutation census: 12 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_three_lengths_per_site_a_body_at_rest_stretches_them_alike_hop_energy_drives_whole_columns_2026_09_21.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
