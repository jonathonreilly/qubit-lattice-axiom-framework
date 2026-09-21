---
claim_id: admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53 to 61 (open PRs #8568, #8570, #8571, #8573, #8578, #8579, #8581, #8590, #8591; not adopted), WIDENED by one supplied object: a FRAME for the coin at every site, E_a^j(x) (coin axis a, bond direction j), with the generator H = (1/2) sum_j {E^j(x).sigma, S_j}, S_j = (T_j - T_j^dagger)/(2i). Block 54's walk is E = 1; block 59's bond rates and block 61's three lengths are the diagonal frames. (T1) For a uniform frame H^2 = sum_ij g^ij sin k_i sin k_j with g^ij = sum_a E_a^i E_a^j: the walker sees a full symmetric inverse metric, three lengths and three angles; a rotation of the coin axes changes neither g nor the spectrum; the symmetrised generator is hermitian for every frame field, the unsymmetrised one is not. (T2) <H> = sum_x sum_aj E_a^j(x) Theta_a^j(x) with Theta_a^j(x) = Re psi^dagger(x) sigma_a (S_j psi)(x) = d<H>/dE_a^j(x): the frame is sourced by the flux of momentum j carried along coin axis a. A plane wave of the identity frame has Theta_a^j = s_a s_j/energy per unit probability (s_j = sin k_j): symmetric, with off-diagonal parts unless the walker moves along an axis (block 59 T2). (T3) For E = 1 + eps the metric is delta + h with h = -(eps + eps^T) at first order; the antisymmetric part of eps drops out. DECLARED MEMBER at second order, through its symbols p_j = 2 sin(k_j/2) (h_jj on sites, h_ij on faces, relabellings on bonds): R_1 = -(p_i p_j h_ij - p^2 h), R_2 = -(1/4) p^2 h_ij h_ij + (1/2)(p_i h_ij)^2 - (1/2)(p_i h_ij p_j) h + (1/4) p^2 h^2, F_2 = -K wbar (u R_1 + R_2). Both are unchanged by the relabelling h_ij -> h_ij + p_i xi_j + p_j xi_i; on diagonal h they are block 61's forms and on h = 2 lam delta block 60's. (T4) With the kinetic term (1/wbar)[alpha hdot_ij hdot_ij + beta hdot^2] the mode determinant is a non-zero multiple of X^3 alpha^2 (alpha + beta)(p^2)^2 (K wbar^2 p^2 - 4 alpha X)^2: exactly TWO travelling disturbances, transverse and traceless and invisible to the rates, with X = K wbar^2 p^2/(4 alpha) in every direction and at every wavelength, and three static relabelling modes. A kinetic term invariant under the cube's symmetries only does not have one speed (witness (M_1, M_2, M_3) = (1, 0, 1)). (T5) Wave vector by wave vector, the static equations can be solved iff the stress is divergence-free, sum_i p_i Theta_(ij) = 0; a body at rest gives block 60's law; the responses hold no one-dimensional inverses. EXECUTED, NOT CLAIMED: the real-space spectrum of the walk in a tilted frame on a 6^3 torus agrees with +-sqrt(g^ij s_i s_j) to 2e-14 and the group velocity with its formula; for stationary superpositions of the identity-frame walk the symmetric frame response is NOT divergence-free on the lattice: relative defect 0.178 (12/L)^3 at fixed mode numbers, second order in the wave vector, while a bond current of the momentum density is conserved to 1e-14; static responses to divergence-free stresses at 300 random directions stay below 1.14 |stress|/p^2. NOT claimed: that the coin has a frame; the member or its numbers; a law for the rotation of the coin axes; that the walk's stress satisfies the member's condition; any statement beyond second order; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_2026_09_21.py
---

# Angles are the tilt of the coin's frame: with them two disturbances travel at one direction-free speed, and the price is a conserved stress

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 61 widened by a frame for the coin, and at second order for one declared member; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for lengths of weight zero, widened by a frame for the coin at every site and one declared member of the ledger at second order; it reports what the walker sees of such a frame, what sources it and what travels in it; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 61 (open PR #8591) found that three lengths per site are enough for bodies at rest and not for anything that moves: hop energy drives the lengths along whole lattice columns, and ripples in the lengths travel at a speed that depends on direction at every wavelength. It named what the comparator has and this picture lacked: the *angles* between the bonds. This note asks where angles could come from in the framework's own vocabulary, and what they repair.

**The observation.** Block 54's walker is a qubit whose coin axis `σ_j` is tied to bond direction `j`. That tie is a *frame*: a rule saying which coin axis goes with which bond. Let it vary: `E_a^j(x)` is the component along coin axis `a` of the vector attached to bond direction `j` at `x`. Block 54 is the identity frame. Block 59's bond rates are the diagonal frames. A frame that is not diagonal tilts the coin's axes against the bonds.

1. **What the walker sees.** For a uniform frame, `H² = Σ g^{ij} sin k_i sin k_j` with `g^{ij} = Σ_a E_a^i E_a^j`. That is the energy of a walker in a space whose bonds have three lengths *and three angles between them*. Rotating all the coin axes together changes nothing. Of a frame's nine numbers the walker sees six (T1).
2. **What sources the frame.** Each entry of the frame is sourced by the flux of momentum `j` carried along coin axis `a`. For a walker moving along an axis that is block 59's hop energy. For one moving across the axes it has off-diagonal parts: **motion across the axes sources angles** (T2).
3. **The member.** The curvature member of blocks 60 and 61, written for the full symmetric stretching `h_ij` at second order, is unchanged by relabellings of the sites along the bonds — exactly, on the lattice, with `h_jj` on sites, `h_ij` on faces and relabellings on bonds. On diagonal `h` it is block 61's form (T3).
4. **What travels.** With a rotation-invariant kinetic term, exactly **two** disturbances travel, both transverse and traceless, both invisible to the clock rates, at **one speed in every direction and at every wavelength** — `X = K w̄² p²/(4α)`, the dispersion of the plainest lattice wave. Block 61's direction-dependent speed is gone. A kinetic term with only the cube's symmetry brings it back (T4).
5. **The price.** Block 61's three-length model accepted any hop energy and answered with columns. The full model has no static answer at all unless the stress is divergence-free, `Σ_i p_i Θ_(ij) = 0`; when it is, the answer falls off, with no one-dimensional inverses. Whether the walk's own stress meets that condition is *executed, not claimed*: for stationary superpositions it does not, exactly — it fails by a term of second order in the wave vector, while a neighbouring quantity, a bond current, is conserved exactly (T5).

In plain terms: the walker already carries angles — they are how its coin is set against the bonds. Let that setting vary from site to site and the walker moves as if space were sheared. Feed those six numbers to block 60's "curvature per tick" and the ripples become the comparator's: two, sideways, one speed. What the framework then owes is a reason for the content's stress to balance on the lattice, which the comparator gets from equations this picture does not have.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 61 (PR #8591), next_trace_action: 'three lengths AND three angles per site (the full symmetric stretching) under the same member: whether the column-long responses go away and the travelling disturbances get one direction-free speed; what sources the angles'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "whether the walk in a frame field has a stress that is divergence-free in the sense the member needs (a bond-placed response; a law for the rotation of the coin axes, which the symmetric part of the stress leaves open); the bending of rays in a frame; whether alpha = K/4 (the disturbances' speed equal to the walker's top speed) follows from anything; the owner's decision whether the coin has a frame"
conditional_surface_status: "T1 exact for every uniform frame and wave vector, hermiticity for every frame field; T2 exact for every amplitude and frame field; T3 exact for every real p; T4 exact for the rotation-invariant kinetic family at every wave vector; T5 exact wave vector by wave vector; T3 to T5 at second order, for the declared member"
hypothetical_axiom_status: "blocks 53 to 61's clauses; a frame for the coin at every site; the declared member at second order; a kinetic term of the stated family; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the covariance sentence of Admissibility, and its silence on a time metric, amplitude dynamics and a conserved energy. The Qubit axiom gives each site a possibility domain with the algebraic presentation `M_2(C)`, equivalently a `Cl(3,0)`-compatible one, with no possibility privileged; block 54 (open PR) used it as the walker's coin, tying its three generators `σ_a` to the three bond directions by covariance under the lattice's proper rotations. The memo itself contains no amplitude dynamics and no frame.

- **Frame.** `E_a^j(x)`, real; `E^j(x)·σ = Σ_a E_a^j(x) σ_a`. **Generator** `H = ½ Σ_j {E^j(x)·σ, S_j}`, `S_j = (T_j − T_j†)/(2i)`, `(T_jψ)(x) = ψ(x + e_j)`: the bond from `x` along `j` carries the mean of its two ends' coin vectors. With rates, `√w H √w` (block 54).
- **Inverse metric** `g^{ij} = Σ_a E_a^i E_a^j`; **metric** `g_ij = δ_ij + h_ij`. Diagonal frames `E_j^j = 1/ℓ_j` give `g_jj = ℓ_j²`: blocks 59 and 61.
- **Frame response** `Θ_a^j(x) = Re ψ†(x) σ_a (S_jψ)(x)`; `Θ_(ij)` its symmetric part. Since `h = −(ε + εᵀ)`, `∂⟨H⟩/∂h_ij = −½Θ_(ij)` (both orders of an off-diagonal pair counted); `Θ_jj` is block 61's `τ_j`.
- **The member (second order), through its symbols.** `h_jj` on sites, `h_ij` (`i ≠ j`) on the faces spanned by `i` and `j`, relabellings `ξ_j` on the bonds along `j`; every difference between neighbouring places then has the real symbol `p_j = 2 sin(k_j/2)`. `R_1`, `R_2` as in the claim scope; `F_2 = −K w̄ (u R_1 + R_2)` summed over wave vectors.
- **Kinetic terms** `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]` (rotation-invariant), and `(1/w̄)[M_1 Σ ḣ_jj² + M_2 Σ_{i<j} ḣ_ii ḣ_jj + M_3 Σ_{i<j} ḣ_ij²]` (the cube's symmetry only); the first is `M_3 = 2M_1 − M_2`.

A frame field for a two-component walker, with the metric as its square, is the dreibein of Weyl and of Fock and Ivanenko; the rotation of the coin axes is their local rotation, which in the comparator is compensated by a connection that this note does not have. That a frame is sourced by the flux of momentum, and that the symmetric part is what the metric sees, is the relation between the canonical and the symmetric stress of Belinfante and Rosenfeld. The quadratic form `R_2` is that of Fierz and Pauli; its invariance is that of Einstein's linearised equations, whose two transverse disturbances at one speed are his of 1916 and 1918, and whose consistency requires the conservation of stress. The formulation with the rate as a multiplier is that of Arnowitt, Deser and Misner. None is used as authority; the comparator is quoted as a comparator.

## Prior art and what is new

Every piece is classical. What is new is the statement inside the framework's vocabulary: that the angles block 61 found missing are already present as the setting of the walker's coin against the bonds, so that no new kind of object is needed — the supplied widening is that this setting may vary; that the walker then sees exactly a symmetric inverse metric, with the frame sourced by a momentum flux whose off-diagonal parts come from motion across the axes; that block 60's member for the full symmetric stretching is relabelling-invariant exactly on the lattice and repairs both defects of block 61; and that the repair has a price the walk does not pay exactly — its frame response is divergence-free only to second order in the wave vector (executed). No gravitational claim is made.

## Exact target and obligation graph

Target: where angles come from and what they repair. Obligations: (O1) what the walker sees of a frame; (O2) what sources it; (O3) the member for the full symmetric stretching; (O4) what travels; (O5) the static response and its condition. T1–T5 discharge them.

## Theorem T1 — what the walker sees

*Statement.* (a) For a uniform frame, `H(k) = Σ_j (E^j·σ) sin k_j` and `H(k)² = (Σ_ij g^{ij} sin k_i sin k_j)·1`. (b) If `E'_a^j = Σ_b R_ab E_b^j` with `R` a rotation, then `g' = g` and `H'` is `H` conjugated by a fixed unitary on the coin. (c) For every real frame field the symmetrised generator is hermitian; the unsymmetrised `Σ_j E^j(x)·σ S_j` is not.

*Proof.* (a) `(u·σ)(v·σ) + (v·σ)(u·σ) = 2(u·v)`, so the square of `Σ_j s_j E^j·σ` is `Σ_ij s_i s_j E^i·E^j`. (b) `g` is a sum over the coin index; a rotation of coin vectors is a conjugation of `σ`. (c) `S_j` and `E^j(x)·σ` are hermitian, and the anticommutator of two hermitian operators is hermitian; their product is not unless they commute. ∎

So rays see `g^{ij}`: block 59 T4's fall and bending become statements about a full metric. The three numbers a rotation removes are not seen by one walker in a uniform frame; a frame field whose rotation varies from site to site is a further object (N1).

## Theorem T2 — what sources the frame

*Statement.* (a) `⟨H⟩ = Σ_x Σ_{a,j} E_a^j(x) Θ_a^j(x)`, and `∂⟨H⟩/∂E_a^j(x) = Θ_a^j(x)` at fixed amplitude. (b) For a plane wave of the identity frame on the positive branch, per unit probability, `Θ_a^j = s_a s_j/ε`, `ε = |s|`.

*Proof.* (a) `⟨ψ|½{E·σ, S}ψ⟩ = Re⟨ψ|E·σ Sψ⟩` because both factors are hermitian; the expression is linear in `E`. (b) `S_jψ = s_jψ` and the coin's expectation on the positive branch of `s·σ` is `s/|s|`. ∎

`Θ_1^1` alone for motion along axis 1 is block 59 T2. For `s = (1/3, 2/3, 2/3)` the off-diagonal parts are `2/9, 2/9, 4/9`.

## Theorem T3 — the member for the full symmetric stretching

*Statement.* (a) For `E = 1 + tε`, `g_ij = δ_ij − t(ε + εᵀ)_ij + O(t²)`; an antisymmetric `ε` does not enter at first order. (b) `R_1` and `R_2` are unchanged by `h_ij → h_ij + p_i ξ_j + p_j ξ_i` for all real `p` and `ξ`. (c) On `h_jj = 2λ_j`, `h_ij = 0`: `R_1 = 2 Σ_j (p² − p_j²) λ_j` and `R_2 = 2(p_3² λ_1 λ_2 + p_2² λ_1 λ_3 + p_1² λ_2 λ_3)`, block 61's; on `h = 2λδ`: `4p²λ` and `2p²λ²`, block 60's.

*Proof.* Direct expansion (runner D1, D2). With the staggered placement every difference in the real-space forms has the symbol `p_j` up to a common phase, so (b) holds on the lattice as it stands; the refuting pass checks `R_1` in real space with integer relabellings. ∎

## Theorem T4 — what travels

*Statement.* (a) For the rotation-invariant kinetic family the determinant of the mode equations in `(h_11, …, h_23, u)` is, with `K = w̄ = 1`, `−32 X³ α² (α + β)(p²)² (p² − 4αX)²`. For `α ≠ 0`, `α + β ≠ 0`: three static modes, the relabellings, and two travelling disturbances with `X = p²/(4α)`. (b) Those two have `p_i h_ij = 0`, `h_ii = 0` and `u = 0`. (c) For `(M_1, M_2, M_3) = (1, 0, 1)` the values of `X/p²` at `p = (1, 2, 2)` and at `p = (1, 4, 8)` have nothing in common.

*Proof.* Expansion of a `7 × 7` determinant (runner E1); the null space at `p = (1, 2, 2)` (E2); coprimality of two polynomials (E3). ∎

`X = Kw̄² p²/(4α)` is exact in `p² = Σ_j 4 sin²(k_j/2)`: the dispersion of a nearest-neighbour scalar wave. Its dependence on direction is that of the lattice itself and vanishes as the fourth power of the wave vector; block 61's was of order one. For `β = −α`, the comparator's choice, the determinant vanishes identically: the relabelling along `p` becomes free in the label as well. With `α = K/4` the disturbances' speed at long wavelength is the walker's top speed, one site per ambient tick; nothing here forces that value.

## Theorem T5 — the static response and its price

*Statement.* Fix a wave vector with `p ≠ 0`. (a) The static matrix (the second derivatives of `−K(uR_1 + R_2)`) has rank 4; its null space is the three relabellings. (b) The static equations with sources `(½Θ_11, ½Θ_22, ½Θ_33, Θ_(12), Θ_(13), Θ_(23); −e)` can be solved iff `Σ_i p_i Θ_(ij) = 0` for `j = 1, 2, 3`. (c) For `Θ = 0` the solution is `h = 2λδ`, `u = −λ`, `λ = e/(4Kw̄p²)`, up to relabellings: block 60's law.

*Proof.* (a), (c) by computation at `p = (1, 2, 2)` (runner E4) and by T3(b) in general: the relabellings are null vectors, and the transverse traceless pair and the two scalars `(u, λ)` are not. (b) The matrix is symmetric, so the equations can be solved iff the source is orthogonal to the null space; the source's product with the relabelling `ξ` is `Σ_ij Θ_(ij) p_i ξ_j`. ∎

Every entry of the static matrix is of second degree in `p` and, on the sources it admits, its inverse is bounded by a multiple of `1/p²` in every direction (runner E5 at `p = (1, 2, 1/100)`: largest entry `2/3` for a stress of size 4, where block 61's response to a unit of hop energy is `833`; the refuting pass at 300 directions). The columns of block 61 were the three-length model's way of answering sources that the full model refuses.

## Executed (supervisor control and refuting pass; floating point; evidence, not proof)

`specs/supervisor_control_block62_refuter.py`. W1: the walk in a uniform tilted frame (off-diagonal `g` of `−0.09, −0.26, −0.22`) as a `432 × 432` real-space matrix: hermitian to rounding, spectrum equal to `±√(g^{ij} s_i s_j)` to `2×10⁻¹⁴`. W2: the group velocity is `cos k_i Σ_j g^{ij} s_j/ε`, `(0.2201, 0.9417, −0.6074)` at `k = (0.4, 0.7, −0.3)` against `(0.4435, 0.6093, −0.3491)` in the identity frame: the tilt turns the walker. **W3 (the price):** for a stationary superposition of two plane waves of equal energy, mode numbers `(1, 2, 3)` and `(3, 1, 2)`, the divergence of the symmetric frame response relative to its oscillating part is `0.178, 0.022, 0.0028` for `L = 12, 24, 48`: `0.178 (12/L)³` to three digits — second order in the wave vector relative to the leading term. The bond current of the momentum density `Re ψ†S_jψ` is conserved to `10⁻¹⁴` in all three. W4: a numerical constrained eigenproblem at four random directions: `X/p²` is `1, 1` and zeros. W5: static responses to divergence-free stresses at 300 random directions, 100 of them within `10⁻³` of a coordinate plane: largest entry below `1.14 |stress|/p²`. W6: `R_1` of a pure relabelling with random integer `ξ` on a `5 × 4 × 3` torus, staggered placement, in real space: exactly zero.

## No-Go Discipline Gate

The note's negative sentences: the unsymmetrised generator is not hermitian; a kinetic term with only the cube's symmetry does not have one speed; a stress that is not divergence-free has no static response; (executed) the walk's frame response is not divergence-free on the lattice.

### N1 — Routes by which the sentences could fail
1. *A bond-placed response.* What the walk conserves exactly is a bond current. A member whose `h` lives where that current lives might be matched exactly. Not examined; the named next step.
2. *A law for the rotation of the coin axes.* The antisymmetric part of `Θ` is not zero for superpositions (up to 0.48 in the scratch runs). In the comparator a connection compensates local rotations and makes the symmetric stress the conserved one. This note has no such object.
3. *Beyond second order.* Not examined.
4. *Other members.* As in block 61.
5. *The cube's kinetic family.* One witness is given, not a classification.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
A torus, wave vector by wave vector, in T4 and T5. The member is declared through its symbols, with a staggered placement; T3(b) is an identity in real `p`. The frame's coupling to the rates is block 54's `√w H √w` and plays no part here. `K > 0`, `α ≠ 0`, `α + β ≠ 0` in T4(a).

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
| "`H² = g^{ij}s_is_j`; frame sourced by momentum flux, off-diagonal for motion across the axes; relabelling-invariant member; two disturbances at one speed; static response iff divergence-free stress" | executed: `H²` for a uniform rational frame with six non-zero off-diagonal entries of `g`, under a rational rotation, and for diagonal frames; hermiticity on a `3³` torus | executed: the frame response at 27 sites, nine entries each, summing to the energy; its derivative by an exact difference; two plane waves | executed: invariance of both orders of the member; the mode determinant; the transverse traceless pair at `(1, 2, 2)`; coprimality for a kinetic term of the cube's symmetry | executed: the rank test (three sources); the response near a coordinate plane against block 61's; the first-order relation of frame and metric | T1 every uniform frame and wave vector, hermiticity every frame field; T2 every amplitude and frame field; T3 every real `p`; T4 the rotation-invariant family; T5 each wave vector; second order for T3–T5; a frame, the member, `K`, `α`, `β`, the walk's stress and a law for coin rotations not derived |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository; whether it bears on `α = K/4` is not decided here and it is not used. `scale_reference_primitive` and `realized_state_primitive` are not used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You have rediscovered the dreibein." Reply: yes, and the note says so under the Premises. The point for the owner is where it sits: the Qubit axiom already gives every site the algebra whose three generators are the coin's axes, and block 54 already ties them to the bonds; angles cost no new kind of object, only the permission for that tie to vary. Second objection: "The member is put in by hand; of course it has the comparator's waves." Reply: it is block 60's member, written for the variables the walker turns out to see; what is reported is that blocks 61's two defects are properties of the truncation, not of the member, and that the repair exposes a condition the content must meet. Third objection: "The price is a lattice artefact of second order; ignore it." Reply: an equation with no solution is not improved by the smallness of what obstructs it; either the placement of `h` is changed to match what the walk conserves, or something must absorb the remainder. That is the next block's question, not a footnote.

### N8 — Cross-cycle echo
Block 54: the qubit as coin; inversion an added symmetry. Block 59: a walker loads the bonds it crosses. Block 60: rates as multipliers. Block 61: three lengths are alike at rest, carry a direction-dependent delay, and answer hop energy with columns. Here: six numbers of a frame, a direction-free delay, no columns, and a condition on the stress.

## Falsifiers

- A uniform frame and wave vector with `H² ≠ g^{ij} s_i s_j`; a rotation of the coin axes that changes the spectrum.
- An amplitude and frame field with `⟨H⟩ ≠ Σ E·Θ`.
- A relabelling that changes `R_1` or `R_2`; a wave vector at which the rotation-invariant family has a third travelling disturbance or a speed other than `p²/(4α)`.
- A stress with `Σ_i p_i Θ_(ij) ≠ 0` that has a static response; a divergence-free one that has none.

## Boundaries and non-claims

That the coin's frame may vary is supplied. The member is declared, through its symbols, at second order only; `K`, `α`, `β` are not derived and `α = K/4` is not forced. Nothing is said about a law for the rotation of the coin axes, about frame fields beyond first order in the metric, or about the bending of rays in a frame. That the walk's stress fails the member's condition at second order in the wave vector is executed, not proved, and for the identity frame only. The comparator is quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, the covariance sentence of Admissibility, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 59, 60, 61 and the decision record (PRs #8570, #8581, #8590, #8591, #8572, open): restated or placed.
- Named standard imports at definition level: the anticommutation of the coin's three matrices; hermiticity of an anticommutator; linearity of an expectation in a parameter; the inverse of a matrix to first order; determinants and null spaces; the solvability of a symmetric linear system; the greatest common divisor of polynomials.
- Reference only: Weyl; Fock and Ivanenko; Belinfante; Rosenfeld; Fierz and Pauli; Einstein (1916, 1918); Arnowitt, Deser and Misner.

## Review record
Supervisor-run block, the tenth of the source-link direction and the sixth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the frame is a widening of block 54's tie between coin axes and bonds, which block 54 took from covariance under the lattice's rotations; a varying frame is supplied and must be named as such; the Qubit axiom's one-site algebra is what makes it cost no new object, and the memo has no frame and no amplitude dynamics, which the note must say. A rigour lens: the supervisor's first test of conservation took the divergence over the wrong index and then over the right one; in both the symmetric frame response fails to be divergence-free for generic stationary superpositions, by exactly `(12/L)³` scaling, while a bond current is conserved to rounding; the note therefore reports the condition as a price and the failure as executed, and does not claim that the walk satisfies the member. The comparison of responses near a coordinate plane is between what each model does with the sources it admits, and is worded so. A comparator lens: every piece is named under the Premises; the missing connection for coin rotations is stated as missing. A strategy lens: the owner's forks 6 and 7 get one candidate home — the coin's frame — with its cost stated: one supplied permission, a declared member, and an open condition on the content. Control and refuting pass (`specs/supervisor_control_block62_refuter.py`, machinery disjoint from the runner's): W1 real-space spectrum in a tilted frame; W2 group velocity; W3 the divergence of the symmetric frame response against the box size and the conserved bond current; W4 a numerical constrained eigenproblem; W5 static responses at 300 directions; W6 `R_1` in real space with integer relabellings. All as reported under Executed. Mutation census: 11 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_2026_09_21.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
