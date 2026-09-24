---
claim_id: admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied real coin frame and symmetrized finite-lattice generator: uniform dispersion squares to the frame Gram form, global coin rotations preserve its spectrum, and fixed-state frame derivatives give the stated response. An invertible frame is required for a positive metric interpretation. A separately declared staggered quadratic symmetric-tensor member has a three-dimensional static null space at nonzero symbol momentum; sources are solvable exactly when orthogonal to it. For K>0, alpha>0 and alpha+beta nonzero its two oscillatory modes are transverse traceless with the same scalar nearest-neighbour lattice dispersion. Their long-wavelength speed is direction independent, while finite-wave-vector phase/group velocities retain lattice anisotropy. Degenerate coefficients, zero momentum and coupling a site-centered walker response to face fields need separate treatment; a cubic-only kinetic counterexample is a witness, not a classification."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_2026_09_21.py
---

# Coin-frame response and a declared tensor model with two equal lattice-wave dispersions

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 61 widened by a frame for the coin, and at second order for one declared member; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for lengths of weight zero, widened by a frame for the coin at every site and one declared member of the ledger at second order; it reports what the walker sees of such a frame, what sources it and what travels in it; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

A uniform real frame gives a Gram form in the two-component walk's dispersion. For an invertible frame this can be parameterized as an inverse metric. This is a supplied extension of the generator; the one-site qubit algebra does not itself supply a varying frame, field action or source equation.

The symmetrized generator is Hermitian, and its fixed-state derivatives define a frame response. That response is not automatically the exactly conserved bond momentum current. Uniform diagonal frames match the earlier dispersion, but their nonuniform endpoint-averaged coupling is not identical to the earlier geometric-mean bond prescription.

The separately declared quadratic tensor energy has relabelling null directions and a source compatibility condition. With the stated positive kinetic coefficient its two oscillatory tensor modes share the scalar nearest-neighbour lattice dispersion. The continuum speed is direction independent; finite lattice phase and group velocities are not. Static response is unique only after a gauge representative is chosen. No consistent coupled nonlinear theory is established.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the covariance sentence of Admissibility, and its silence on a time metric, amplitude dynamics and a conserved energy. The Qubit axiom gives each site a possibility domain with the algebraic presentation `M_2(C)`, equivalently a `Cl(3,0)`-compatible one, with no possibility privileged; block 54 (open PR) used it as the walker's coin, tying its three generators `σ_a` to the three bond directions by covariance under the lattice's proper rotations. The memo itself contains no amplitude dynamics and no frame.

- **Frame.** `E_a^j(x)`, real; `E^j(x)·σ = Σ_a E_a^j(x) σ_a`. **Generator** `H = ½ Σ_j {E^j(x)·σ, S_j}`, `S_j = (T_j − T_j†)/(2i)`, `(T_jψ)(x) = ψ(x + e_j)`: the bond from `x` along `j` carries the mean of its two ends' coin vectors. With rates, `√w H √w` (block 54).
- **Inverse metric** `g^{ij} = Σ_a E_a^i E_a^j`; **metric** `g_ij = δ_ij + h_ij`. For invertible uniform diagonal frames `E_j^j = 1/ℓ_j`, `g_jj = ℓ_j²`. Nonuniform arithmetic endpoint averaging of E differs from the geometric-mean inverse lengths of the earlier bond model; only the uniform comparison is identified here.
- **Frame response** `Θ_a^j(x) = Re ψ†(x) σ_a (S_jψ)(x)`; `Θ_(ij)` its symmetric part. Since `h = −(ε + εᵀ)`, `∂⟨H⟩/∂h_ij = −½Θ_(ij)` (both orders of an off-diagonal pair counted); `Θ_jj` is block 61's `τ_j`.
- **The member (second order), through its symbols.** `h_jj` on sites, `h_ij` (`i ≠ j`) on the faces spanned by `i` and `j`, relabellings `ξ_j` on the bonds along `j`; every difference between neighbouring places then has the real symbol `p_j = 2 sin(k_j/2)`. `R_1=p^2 tr(h)-p^T h p` and `R_2=-(p^2/4) tr(h^T h)+(1/2)|h p|^2-(1/2)(p^T h p)tr(h)+(p^2/4)tr(h)^2`; `F_2 = −K w̄ (u R_1 + R_2)` summed over wave vectors.
- **Source placement.** T5 accepts an abstract symmetric source on the same staggered degrees of freedom. The site-centered frame response of T2 requires a declared transfer/interpolation to those face components. Its preservation of the divergence condition is not established here.
- **Kinetic terms** `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]` (rotation-invariant), and `(1/w̄)[M_1 Σ ḣ_jj² + M_2 Σ_{i<j} ḣ_ii ḣ_jj + M_3 Σ_{i<j} ḣ_ij²]` (the cube's symmetry only); the first is `M_3 = 2M_1 − M_2`.

A frame field for a two-component walker, with the metric as its square, is the dreibein of Weyl and of Fock and Ivanenko; the rotation of the coin axes is their local rotation, which in the comparator is compensated by a connection that this note does not have. That a frame is sourced by the flux of momentum, and that the symmetric part is what the metric sees, is the relation between the canonical and the symmetric stress of Belinfante and Rosenfeld. The quadratic form `R_2` is that of Fierz and Pauli; its invariance is that of Einstein's linearised equations, whose two transverse disturbances at one speed are his of 1916 and 1918, and whose consistency requires the conservation of stress. The formulation with the rate as a multiplier is that of Arnowitt, Deser and Misner. None is used as authority; the comparator is quoted as a comparator.

## Prior art and what is new

The bounded content is explicit generator algebra and a separately supplied tensor-symbol model. Historical continuum analogies do not grant the model or its coupling from the repository's axioms.

## Theorem T1 — what the walker sees

*Statement.* (a) For a uniform frame, `H(k) = Σ_j (E^j·σ) sin k_j` and `H(k)² = (Σ_ij g^{ij} sin k_i sin k_j)·1`. (b) If `E'_a^j = Σ_b R_ab E_b^j` with `R` a rotation, then `g' = g` and `H'` is `H` conjugated by a fixed unitary on the coin. (c) For every real frame field the symmetrised generator is hermitian; the unsymmetrised sum is generally not: it is Hermitian exactly when the sum of its commutators vanishes, including uniform frames.

*Proof.* (a) `(u·σ)(v·σ) + (v·σ)(u·σ) = 2(u·v)`, so the square of `Σ_j s_j E^j·σ` is `Σ_ij s_i s_j E^i·E^j`. (b) `g` is a sum over the coin index; a rotation of coin vectors is a conjugation of `σ`. (c) `S_j` and `E^j(x)·σ` are hermitian, and the anticommutator of two hermitian operators is hermitian; a single product is Hermitian iff its factors commute. For the sum, commutator cancellation is the exact condition. ∎

The uniform dispersion has the Gram form `g^{ij}`. Extending this to nonuniform ray dynamics requires the separate slowly varying approximation; no exact packet-force law follows. The three numbers a rotation removes are not seen by one walker in a uniform frame; a frame field whose rotation varies from site to site is a further object (N1).

## Theorem T2 — what sources the frame

*Statement.* (a) `⟨H⟩ = Σ_x Σ_{a,j} E_a^j(x) Θ_a^j(x)`, and `∂⟨H⟩/∂E_a^j(x) = Θ_a^j(x)` at fixed amplitude. (b) For a plane wave of the identity frame on the positive branch, per unit probability, `Θ_a^j = s_a s_j/ε`, `ε = |s| > 0`.

*Proof.* (a) `⟨ψ|½{E·σ, S}ψ⟩ = Re⟨ψ|E·σ Sψ⟩` because both factors are hermitian; the expression is linear in `E`. (b) `S_jψ = s_jψ` and the coin's expectation on the positive branch of `s·σ` is `s/|s|`. ∎

`Θ_1^1` alone for motion along axis 1 is block 59 T2. For `s = (1/3, 2/3, 2/3)` the off-diagonal parts are `2/9, 2/9, 4/9`.

## Theorem T3 — the member for the full symmetric stretching

*Statement.* (a) For `E = 1 + tε`, `g_ij = δ_ij − t(ε + εᵀ)_ij + O(t²)`; an antisymmetric `ε` does not enter at first order. (b) `R_1` and `R_2` are unchanged by `h_ij → h_ij + p_i ξ_j + p_j ξ_i` for all real `p` and `ξ`. (c) On `h_jj = 2λ_j`, `h_ij = 0`: `R_1 = 2 Σ_j (p² − p_j²) λ_j` and `R_2 = 2(p_3² λ_1 λ_2 + p_2² λ_1 λ_3 + p_1² λ_2 λ_3)`, block 61's; on `h = 2λδ`: `4p²λ` and `2p²λ²`, block 60's.

*Proof.* Direct expansion (runner D1, D2). With the staggered placement every difference in the real-space forms has the symbol `p_j` up to a common phase, so (b) holds on the lattice as it stands; the refuting pass checks `R_1` in real space with integer relabellings. ∎

## Theorem T4 — what travels

*Statement.* (a) For the rotation-invariant kinetic family the determinant of the mode equations in `(h_11, …, h_23, u)` is, with `K = w̄ = 1`, `−32 X³ α² (α + β)(p²)² (p² − 4αX)²`. For nonzero p, `α > 0`, `α + β ≠ 0`, and positive K: three zero-frequency null directions of the spatial form, and two oscillatory disturbances with `X = p²/(4α)`. (b) Those two have `p_i h_ij = 0`, `h_ii = 0` and `u = 0`. (c) For `(M_1, M_2, M_3) = (1, 0, 1)` the values of `X/p²` at `p = (1, 2, 2)` and at `p = (1, 4, 8)` have nothing in common.

*Proof.* Expansion of a `7 × 7` determinant (runner E1); the null space at `p = (1, 2, 2)` (E2); coprimality of two polynomials (E3). ∎

`X = Kw̄² p²/(4α)` is exact in `p² = Σ_j 4 sin²(k_j/2)`: the dispersion of a nearest-neighbour scalar wave. Since p^2=|k|^2-sum(k_j^4)/12+O(|k|^6), the anisotropic correction to X is fourth order; the relative phase-speed correction is second order. Finite-wave-vector phase and group velocities remain direction dependent, while the long-wavelength speed is common; block 61's was of order one. For `β = −α`, the comparator's choice, the determinant vanishes identically: the determinant alone no longer counts modes, and the additional constrained evolution must be analyzed separately. Likewise alpha<0 gives a negative tensor squared frequency, not travelling oscillations. Zero-frequency directions can admit secular motion unless additional constraints or gauge identifications remove it. With `α = K/4` the disturbances' speed at long wavelength is the walker's top speed, one site per ambient tick; nothing here forces that value.

## Theorem T5 — the static response and its price

*Statement.* Fix a wave vector with `p ≠ 0`. (a) The static matrix (the second derivatives of `−K(uR_1 + R_2)`) has rank 4; its null space is the three relabellings. (b) The static equations with sources `(½Θ_11, ½Θ_22, ½Θ_33, Θ_(12), Θ_(13), Θ_(23); −e)` can be solved iff `Σ_i p_i Θ_(ij) = 0` for `j = 1, 2, 3`. (c) For `Θ = 0` the solution is `h = 2λδ`, `u = −λ`, `λ = e/(4Kw̄p²)`, up to relabellings: block 60's law.

*Proof.* (a), (c) by computation at `p = (1, 2, 2)` (runner E4) and by T3(b) in general: the relabellings are null vectors, and the transverse traceless pair and the two scalars `(u, λ)` are not. (b) The matrix is symmetric, so the equations can be solved iff the source is orthogonal to the null space; the source's product with the relabelling `ξ` is `Σ_ij Θ_(ij) p_i ξ_j`. ∎

After choosing the representative orthogonal to the relabelling null space, the static inverse on compatible sources is bounded by a multiple of `1/p²`. To justify this uniformly, rotate each nonzero p to an axis: the isotropic tensor form then has fixed nonzero eigenvalues after dividing by p^2 on the complement, and rotations preserve the tensor norm. Homogeneity alone would not prove this bound (runner E5 at `p = (1, 2, 1/100)`: largest entry `2/3` for a stress of size 4, where block 61's response to a unit of hop energy is `833`; the refuting pass at 300 directions). The columns of block 61 were the three-length model's way of answering sources that the full model refuses.

## Historical experiments — deferred

The original frame-spectrum, stress-divergence, evolution and random-direction experiments remain on the PR branch. They have not been re-executed for this landing, and their scaling observations do not become a general stress-conservation theorem. The canonical runner checks finite exact identities and representative symbolic matrices.

## No-Go Discipline Gate

The note's negative sentences: the unsymmetrised generator need not be Hermitian; the stated cubic-only kinetic witness has direction-dependent normalized dispersion; a stress that is not divergence-free has no static response; (executed) the walk's frame response is not divergence-free on the lattice.

### N1 — Routes by which the sentences could fail
1. *A bond-placed response.* What the walk conserves exactly is a bond current. A member whose `h` lives where that current lives might be matched exactly. Not examined; the named next step.
2. *A law for the rotation of the coin axes.* The antisymmetric part of `Θ` is not zero for superpositions (up to 0.48 in the scratch runs). In the comparator a connection compensates local rotations and makes the symmetric stress the conserved one. This note has no such object.
3. *Beyond second order.* Not examined.
4. *Other members.* As in block 61.
5. *The cube's kinetic family.* One witness is given, not a classification.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
A torus, wave vector by wave vector, in T4 and T5. The member is declared through its symbols, with a staggered placement; T3(b) is an identity in real `p`. The frame's coupling to the rates is block 54's `√w H √w` and plays no part here. `K > 0`, `α > 0`, `α + β ≠ 0`, nonzero p in T4(a).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its proper rotations; the Qubit axiom's one-site algebra; the covariance sentence; the absences that motivate the clauses | yes (premise) |
| block 54 (open PR #8570) | the walk with the qubit as coin; `σ_j` on bond direction `j` | yes (restated) |
| blocks 59, 61 (open PRs #8581, #8591) | bond rates and three lengths as diagonal frames; hop energy; the defects to repair | yes (restated) |
| block 60 (open PR #8590) | the ledger linear in the rates; the curvature member; its law for a body at rest | yes (restated) |
| decision record (open PR #8572) | forks 6 and 7 | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "`H² = g^{ij}s_is_j`; frame sourced by momentum flux, off-diagonal for motion across the axes; relabelling-invariant member; two equal lattice dispersion branches at nondegenerate nonzero modes; static response iff the supplied staggered stress is divergence-free at nonzero p" | executed: `H²` for a uniform rational frame with six non-zero off-diagonal entries of `g`, under a rational rotation, and for diagonal frames; hermiticity on a `3³` torus | executed: the frame response at 27 sites, nine entries each, summing to the energy; its derivative by an exact difference; two plane waves | executed: invariance of both orders of the member; the mode determinant; the transverse traceless pair at `(1, 2, 2)`; coprimality for a kinetic term of the cube's symmetry | executed: the rank test (three sources); the response near a coordinate plane against block 61's; the first-order relation of frame and metric | T1 every uniform frame and wave vector, hermiticity every frame field; T2 every amplitude and frame field; T3 every real `p`; T4 the rotation-invariant family; T5 each wave vector; second order for T3–T5; a frame, the member, `K`, `α`, `β`, the walk's stress and a law for coin rotations not derived |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository; whether it bears on `α = K/4` is not decided here and it is not used. `scale_reference_primitive` and `realized_state_primitive` are not used. Nothing is proposed for registration.

### N7 — Strongest objections
A qubit algebra alone does not supply a dynamical frame or tensor action. Equal lattice dispersions do not imply direction-free finite-wavelength speed. The site-to-face source transfer is missing, so the static compatibility condition is not a completed coupling to the walk. The cubic kinetic witness is not proof that the rotation-invariant coefficients are necessary throughout the cubic family.

### N8 — Cross-cycle echo
Block 54: the qubit as coin; inversion an added symmetry. Block 59: a walker loads the bonds it crosses. Block 60: rates as multipliers. Block 61: three lengths are alike at rest, carry a direction-dependent delay, and answer hop energy with columns. Here: six symmetric frame components, two equal normalized dispersion branches, a bounded static inverse on the nonzero-mode quotient, and a condition on the abstract staggered stress.

## Falsifiers

- A uniform frame and wave vector with `H² ≠ g^{ij} s_i s_j`; a rotation of the coin axes that changes the spectrum.
- An amplitude and frame field with `⟨H⟩ ≠ Σ E·Θ`.
- A relabelling that changes `R_1` or `R_2`; a nonzero wave vector and nondegenerate coefficients in the stated positive family with a third oscillatory tensor branch or a squared frequency other than `K wbar^2 p²/(4α)`.
- At nonzero p in the declared static symbol problem, an abstract staggered stress with nonzero divergence that has a response, or a divergence-free stress that has none modulo the longitudinal kernel.

## Boundaries and non-claims

That the coin's frame may vary is supplied. The member is declared, through its symbols, at second order only; `K`, `α`, `β` are not derived and `α = K/4` is not forced. Nothing is said about a law for the rotation of the coin axes, about frame fields beyond first order in the metric, or about the bending of rays in a frame. The original stress-defect scaling is a deferred author experiment in the identity frame; no general coupling or conservation conclusion relies on it. The comparator is quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, the covariance sentence of Admissibility, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 59, 60, 61 and the decision record (PRs #8570, #8581, #8590, #8591, #8572, open): restated or placed.
- Named standard imports at definition level: the anticommutation of the coin's three matrices; hermiticity of an anticommutator; linearity of an expectation in a parameter; the inverse of a matrix to first order; determinants and null spaces; the solvability of a symmetric linear system; the greatest common divisor of polynomials.
- Reference only: Weyl; Fock and Ivanenko; Belinfante; Rosenfeld; Fierz and Pauli; Einstein (1916, 1918); Arnowitt, Deser and Misner.

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8570](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8581](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8590](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8591](ADMISSIBILITY_RULE_THREE_LENGTHS_PER_SITE_A_BODY_AT_REST_STRETCHES_THEM_ALIKE_HOP_ENERGY_DRIVES_WHOLE_COLUMNS_AND_THE_DELAYS_SPEED_DEPENDS_ON_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

Original author reports are preserved at PR #8592 head `aada579459b89a9c7179442140a90a809e2d696c`, branch `physics-loop/admissibility-induced-law-block62-angles-are-the-tilt-of-the-coins-frame-two-disturbances-one-direction-free-speed-20260921`. Landing review corrects finite-wavelength speed language, kinetic sign and degeneracy conditions, metric invertibility, source placement and the nonuniform diagonal coupling comparison. Auxiliary experiments remain deferred. Review does not apply an audit verdict.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_2026_09_21.py
```

The fresh cache records the executed count.
