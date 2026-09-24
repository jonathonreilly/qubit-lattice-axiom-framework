---
claim_id: admissibility_rule_three_lengths_per_site_a_body_at_rest_stretches_them_alike_hop_energy_drives_whole_columns_and_the_delays_speed_depends_on_direction_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the declared quadratic three-length model on rectangular product boxes with fixed zero boundary perturbations: the commuting directional differences give a unique static solution for supplied sources, with equal lengths when hop sources vanish. A unit point source in one hop component produces the stated column tents, while suitably structured nonzero sources can retain equal lengths. On periodic lattices the displayed determinant is exact; generic nondegenerate modes of the specified kinetic coefficients have direction-dependent normalized squared frequency X/(wbar^2 sum 4sin^2(kj/2)). That quantity is a squared phase speed only in the long-wavelength limit. No constant root of the indicated normalized form exists for the whole two-parameter onsite kinetic family. Degenerate wave vectors and kinetic coefficients require separate constraint analysis; no full nonlinear stability or universal impossibility for all length-field models is claimed."
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

This is a declared quadratic model with three directional length perturbations. The fixed-wall product-box static problem is invertible. Vanishing hop sources give equal lengths, while the specified point-source examples produce column-shaped responses growing with box size. This does not imply that every nonzero hop-source distribution breaks equal lengths.

The periodic determinant yields a direction-dependent normalized dispersion. At long wavelength the direction dependence remains in the phase speed; at finite lattice wave vector, X/s is a normalized frequency, not literally squared phase or group velocity. The no-constant-root proof applies to the stated two-parameter onsite kinetic family and a continuum of directions. It does not cover arbitrary gradient kinetics, different field energies or additional fields. Special axes, zero modes and degenerate kinetic coefficients must be treated separately.

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

The useful results are explicit static inverses and mode-polynomial identities for this model. The continuum curvature comparison motivates the declared quadratic energy but does not derive its discretization or establish a unique physical interpretation.

## Theorem T1 — the member for three lengths

*Statement.* For the metric `diag(ℓ_1², ℓ_2², ℓ_3²)`, `ℓ_j = e^{ελ_j}`: (a) volume density × scalar curvature `= −2ε Σ_j Σ_{i≠j} ∂_i² λ_j + O(ε²)`; (b) its part of order `ε²` has the same variational derivatives as `2(∂_3λ_1 ∂_3λ_2 + ∂_2λ_1 ∂_2λ_3 + ∂_1λ_2 ∂_1λ_3)`; (c) with `λ_j = λ` these are `−4∇²λ` and `2|∇λ|²`; (d) with lengths changing in the label and no sliding of sites, the kinetic density is `−2 Σ_{i<m} λ̇_i λ̇_m/w²`, which is `−6λ̇²/w²` for equal lengths.

*Proof.* Direct computation of the curvature from the connection, expanded to second order (runner B1, B2). ∎

So `∂_jλ_j`, the change of a length along its own axis, does not enter, and neither does any `(∂_kλ_i)²`: the form is purely a coupling of pairs.

## Theorem T2 — a body at rest stretches the three lengths alike

*Statement.* On a rectangular product box with held walls the static equations have exactly one solution for every `e` and `τ_j`. For `τ_j = 0` it is `λ_1 = λ_2 = λ_3 = λ`, `u − ū = −λ`, `4K w̄ Δλ = −e`.

*Proof.* The `D_i` commute, and minus a one-dimensional second difference with zero walls is positive definite (its leading minors are `2, 3, …, n + 1`), so in a common eigenbasis `D_i = −a, −b, −c` with `a, b, c > 0`. The three equations for `a_j = λ_j + u` have the matrix `[[0, c, b], [c, 0, a], [b, a, 0]]` of determinant `2abc ≠ 0`: `a_j` is fixed by the `τ`'s, and is zero when they are. Then `λ_j = −u` and the constraint reads `−2Δu = −e/(2Kw̄)`. ∎

On a closed lattice some of `a, b, c` vanish and the determinant with them: a nonnegative nonzero total content source is incompatible with the summed periodic rate constraint. This does not exclude every signed-source or vacuum static configuration.

## Theorem T3 — hop energy drives whole columns

*Statement.* (a) `a = (a_1, a_2, a_3)` is `1/(2Kw̄)` times the inverse of the operator matrix [[0,D_3,D_2],[D_3,0,D_1],[D_2,D_1,0]] applied to `(τ_1, τ_2, τ_3)`, written with the operators `D_i` in place of `−a, −b, −c`, and that inverse is `(1/(2 D_1 D_2 D_3)) [[−D_1², D_1D_2, D_1D_3], [D_1D_2, −D_2², D_2D_3], [D_1D_3, D_2D_3, −D_3²]]`: for `τ_1` alone, `a_2 = D_3^{-1}τ_1/(4Kw̄)`, `a_3 = D_2^{-1}τ_1/(4Kw̄)`, `a_1 = −D_1 D_2^{-1} D_3^{-1} τ_1/(4Kw̄)`. (b) For a point of hop energy at the centre of a cubic box with odd `n` interior sites across, `a_2` is zero off the column through the source along axis 3, and on it is the tent `−min(z, z_0)(n + 1 − max(z, z_0))/((n + 1)·4Kw̄)`, of height `−(n + 1)/(16Kw̄)` at the source. (c) Equal hop energies `τ_j = τ/3` leave `a_1 = (τ/(12Kw̄))[D_3^{-1} + D_2^{-1} − D_1 D_2^{-1} D_3^{-1}]δ ≠ 0`; block 60's equal-lengths law `Δ(u + λ) = τ/(4Kw̄)` does not satisfy the wider equations. (d) The rates obey `Δ(u − ū) = (e + τ)/(4Kw̄)` exactly.

*Proof.* (a) Invert the `3 × 3` matrix of commuting operators. (b) The inverse of a one-dimensional second difference with zero walls is the tent. (c) By linearity and rotation; the equal-lengths law would need `(D_2 + D_3)(u + λ) = τ_1/(2Kw̄)`, which fails one site from the source, where `τ_1 = 0` and `(D_2 + D_3)Δ^{-1}δ ≠ 0`. (d) Put `λ_j = a_j − u` in the constraint: `Δu = e/(4Kw̄) + ½Σ_j (Δ − D_j) a_j`, and with (a) the sum is `Σ_j τ_j/(2Kw̄)` — for `τ_1` alone the terms in `D_1/D_2` and `D_1/D_3` cancel in pairs and `½ + ½` remains. ∎

These point-source examples have column-supported combinations a_j whose magnitude depends on the walls. The rate equation retains the three-dimensional grounded inverse. Arbitrary source distributions can cancel the column response. For example, choosing `tau_j=2K wbar (Delta-D_j)f` gives `a_1=a_2=a_3=f`, hence equal lengths, despite nonzero hop sources. The claim concerns the explicit point-source failures, not every moving state.

## Theorem T4 — travelling disturbances and their speeds

*Statement.* (a) On a torus the amplitudes `(A_1, A_2, A_3, U)` of a disturbance `∝ cos(ωt) cos(k·x)` satisfy a linear system whose determinant is a non-zero multiple of the quadratic in `X = ω²`, `(2M_1 − M_2)(M_1 s² − (M_1 + M_2)σ)X² − 2Kw̄²(M_1 s³ − (2M_1 + M_2)sσ + 3(M_1 + M_2)π)X + 4K²w̄⁴πs`: generically a quadratic mode condition, with two oscillatory branches only where its leading coefficient is nonzero and its roots are real and positive. Degenerate kinetic choices may reduce its degree or remove oscillatory branches. (b) For `M_1 = 0`, `M_2 = −2K`: `σX² − w̄²(sσ − 3π)X + w̄⁴πs = 0`; with `v = X/(w̄²s)`, `v_1 + v_2 = 1 − 3ρ`, `v_1v_2 = ρ`, discriminant `(1 − ρ)(1 − 9ρ) ≥ 0` since `9abc ≤ (a + b + c)(ab + ac + bc)`. In a coordinate plane (`π = 0`): `v = 1` and `v = 0`. On a body diagonal (`a = b = c`): `v = 1/3` twice. (c) Let `(M_1, M_2) ≠ (0, 0)`. There is no `v_0` such that `X = v_0 w̄² s` is a root for all directions.

*Proof.* (a), (b) By expansion (runner E1, E2); `ρ ≤ 1/9` is the inequality of the arithmetic and geometric means applied to `a + b + c` and to `ab + ac + bc`. (c) With `m = M/K`, `σ̂ = σ/s²`, `π̂ = π/s³`, which vary independently with direction, the quadratic at `X = v_0 s` is `(2m_1 − m_2)(m_1 − (m_1 + m_2)σ̂)v_0² − 2(m_1 − (2m_1 + m_2)σ̂ + 3(m_1 + m_2)π̂)v_0 + 4π̂`. Its coefficient of `π̂` gives `v_0 = 2/(3(m_1 + m_2))`; its constant term gives `m_1 = 0` or `v_0 = 2/(2m_1 − m_2)`. If `m_1 = 0` the coefficient of `σ̂` is `m_2²v_0² + 2m_2v_0 = 4/9 + 4/3 ≠ 0`. Otherwise `2m_1 − m_2 = 3(m_1 + m_2)`, the coefficient of `σ̂` reduces to `2m_1v_0`, so `m_1 = 0`, then `m_2 = 0`. The runner confirms that the three conditions generate the whole polynomial ring (E4). ∎

The polynomial statement is exact in `a, b, c`. Here v is a normalized squared frequency, not finite-wave-vector phase speed `X/|k|^2` or group speed. Its long-wavelength interpretation follows because as `k → 0`, `a → k_1²` and `ρ` tends to a function of direction alone. Block 54's walker is direction-dependent at second order in the wave vector; these disturbances are at zeroth order — as block 51 found for the record layer's wind.

For the specified comparator coefficients, along a lattice axis the determinant vanishes identically: the length along that axis is arbitrary there and is compensated by the rates (a null direction of these linear equations; a physical relabelling interpretation requires an additional symmetry argument); on the third axis, the disturbance `λ_1 = −λ_2` has `X = w̄²c`. A vanishing determinant by itself does not count physical modes.

## Historical experiments — deferred

Original finite-volume numerical solves, time evolutions and kinetic grid searches remain on the original PR branch and are not fresh canonical evidence. Exact symbolic and rational controls below cover the stated quadratic model.

## No-Go Discipline Gate

The note's negative sentences: block 60's equal-lengths law fails for the specified point hop sources; the specified point hop source produces column-supported length combinations; no nonzero onsite kinetic term of the stated family has a direction-independent normalized-frequency root.

### N1 — Routes by which the sentences could fail
1. *Other variables.* Angles between the bonds (three more numbers per site) and sliding of sites. Not examined; the named next step. The comparator has both.
2. *Other members.* The theorems are for the declared member. A member in which each length has a gradient term of its own (three scalars) has isotropic leading small-wave dispersion with appropriately matched kinetic coefficients and is not the curvature of anything; what bending it gives is not examined.
3. *Sources whose hop energies balance.* The column-long response is the inverse of a matrix applied to `(τ_1, τ_2, τ_3)`; distributions with `−D_1τ_1 + D_2τ_2 + D_3τ_3` in the range of `D_2D_3` (and rotations) have local responses. Whether the amplitudes' own equations put them there is not examined.
4. *Beyond second order.* Not examined.
5. *Kinetic terms with differences between sites.* Smooth finite-range gradient corrections are higher order only if a nondegenerate onsite kinetic leading term remains. Pure-gradient or degenerate kinetics require separate analysis and are outside this no-constant-root theorem.

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
| "pairs coupled along the third axis; alike at rest, uniquely; columns for hop energy, rates unharmed; speeds by `ρ`, no direction-free speed for any kinetic term" | executed: both orders of volume × curvature for three lengths and the kinetic density, by exact symbolic algebra; equal lengths | executed: the 108 static equations of a `5³` box; the three equations at all 125 sites of a `7³` box; the constraint after an exact solve for the rates | executed: the mode determinant in symmetric functions; coordinate planes and body diagonals; two disturbances at `(π/3, π/3, π)` at all 72 sites of a `6×6×2` torus | executed: tent height against box size; equal hop energies; the equal-lengths law's residual; the reduced basis of the isotropy conditions | T1 every diagonal metric; T2 rectangular product boxes and content at rest; T3 such boxes and arbitrary hop sources, with column and unequal-length assertions restricted to the named point sources; T4 every wave vector and kinetic term of the family; second order, the declared member; three lengths, the member, `K`, `M_1`, `M_2`, other variables not derived |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository; it says nothing about a speed's dependence on spatial direction and is not used. `scale_reference_primitive` and `realized_state_primitive` are not used. Nothing is proposed for registration.

### N7 — Strongest objections
The point-source response does not establish failure for every moving or extended source; the explicit structured-source counterexample above prevents that overclaim. The discretized determinant does not by itself derive a coordinate symmetry or physical signal cone. The no-constant-root theorem is about the declared polynomial and onsite kinetic family, not all possible theories using directional lengths.

### N8 — Cross-cycle echo
Block 51: the record layer's wind is direction-dependent at every distance. Block 54: the walk's fall is direction-dependent at second order only. Block 59: the anisotropic parts of bond rates are slaved at rest. Block 60: the isotropic lengths carry no delay. Here: three lengths are alike at rest (consistent with blocks 59 and 60), carry a delay, and carry it at a direction-dependent speed at zeroth order.

## Falsifiers

- A rectangular product box with held walls and content at rest whose three lengths differ, or a second static solution.
- A point of hop energy whose `λ_2 + u` is non-zero off its column, or whose tent's height does not grow with the box.
- A wave vector at which the squared frequencies are not the roots of the stated quadratic; a direction off the coordinate planes with `v = 1` for the comparator's kinetic term.
- A nonzero kinetic coefficient pair of the stated onsite family with a root X=v_0 wbar^2 s for every positive directional triple.

## Boundaries and non-claims

Three lengths per site are supplied, and the member is declared and used at second order only. Nothing is said about angles between bonds, sliding of sites, other members, or higher orders. The bending of rays in direction-dependent lengths is not computed. Real nonnegative squared frequencies are shown for the specified comparator coefficients at the stated nondegenerate wave vectors. This is a spectral statement, not full dynamical or nonlinear stability; zero and constrained modes need their own treatment. The comparator is quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the covariance sentence of Admissibility, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 51, 54, 59, 60 and the decision record (PRs #8563, #8570, #8581, #8590, #8572, open): restated or placed.
- Named standard imports at definition level: the scalar curvature of a metric from its connection; variational derivatives; commuting symmetric matrices and their common eigenbasis; the inverse of a one-dimensional second difference; symmetric functions; the inequality of the arithmetic and geometric means; reduced bases of polynomial ideals.
- Reference only: Arnowitt, Deser and Misner; Einstein (1916, 1918); Fierz and Pauli; Regge.

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8570](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8581](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8590](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

Original source and author controls remain at PR #8591 head `084fd809f9457d942576714dd8b9f98d91844d9d`, branch `physics-loop/admissibility-induced-law-block61-three-lengths-per-site-the-delay-has-a-direction-dependent-speed-20260921`. Landing review limits source quantifiers, distinguishes normalized dispersion from finite-wavelength speed, states the product-box premise and separates degenerate modes. Auxiliary work remains deferred, with no audit verdict applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_three_lengths_per_site_a_body_at_rest_stretches_them_alike_hop_energy_drives_whole_columns_2026_09_21.py
```

The fresh cache records the executed check count.
