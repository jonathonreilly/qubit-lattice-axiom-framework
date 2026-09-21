---
claim_id: admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN supplied objects and a supplied clause, not adopted: a two-component amplitude psi_x on the sites of Z^3 (the site's qubit as the content of one moving record), a nearest-neighbour generator H, a positive tick-rate field w_x (any; block 53's clause, open PR #8568, supplies one), and the clause that the amplitude at a site advances in that site's own time: i d(psi_x)/d(tau_x) = (H psi)_x with d(tau_x) = w_x dt. The axioms memo contains no amplitude dynamics and no time metric; the objects and the clause are candidate fillings of those open gates and are not derived. (T1) A translation-invariant hermitian nearest-neighbour generator that is covariant under the 24 proper rotations, the content turning as a direction, has the symbol a_0 + 2a sum_j cos k_j + beta sum_j sigma_j sin k_j: three real numbers. beta couples the content to the motion: the velocity operator of the beta term is sigma_j (T_j + T_j^dagger)/2, the content itself at long wavelength. If lattice inversion, which is not among the symmetries the Admissibility axiom names, is added as a symmetry of the evolution, then with the content reversed by it (necessarily an antilinear map) a_0 = a = 0 and the generator is the walk with the qubit as coin, H = sum_j sigma_j D_j; with the content untouched, beta = 0. The walk squares to the scalar sum_j D_j^2, and no 2x2 matrix anticommutes with all three content matrices, so one walker has no rest energy. (T2) The clause gives the generator w H; it is self-adjoint for the inner product sum_x conj(phi_x) psi_x / w_x and not for the plain one, so the conserved quantity is sum_x |psi_x|^2 / w_x; it is similar to the hermitian H_w = sqrt(w) H sqrt(w), as is the sending-site timing H w; multiplying every rate by t multiplies H_w by t, a change of the unit of time. (T3) Where log w has a uniform gradient, w(x + a) = lambda_a w(x), one has H_w^n T_a = lambda_a^n T_a H_w^n on finitely supported amplitudes for every n, for any translation-invariant H and any bond timing of degree one; hence, in a slab of uniform gradient and for as long as the amplitude stays inside it, U_w(t) T_a = T_a U_w(lambda_a t) and T_a(t) = T_a exp(i (lambda_a - 1) H_w t): in a state of energy E the wave vector along a falls at the constant rate (lambda_a - 1) E, that is force = -(energy) x (gradient of log w) for small gradients, in every state and with no ray approximation. It fails for rate fields that are not exponential. (T4) For rays of an energy function E = w(x) eps(k): dv_j/dt = -w^2 sum_l d_j d_l (eps^2/2) d_l u + 2 (v . grad u) v_j, u = log w. The law contains the ray's velocity and nothing else about it exactly when the matrix of second derivatives of eps^2/2 is the unit matrix, eps^2 = |k - k_0|^2 + const; then a ray at rest or moving across the gradient falls at -w^2 grad u, one moving along it at the limiting speed is pushed the other way at +w^2 grad u, and the sign changes at v = w/sqrt 2. For the walk the matrix is diag(cos 2 k_j) whatever the rest energy: the velocity-only law at long wavelength, with relative corrections -2 k_j^2. A constant e_0 added to the walk's energy multiplies a transverse ray's fall by 1 + e_0/|k|; for beta = 0, eps = e_0 + k^2/(2M), a ray at rest falls at e_0/M times -grad u: weight and inertia are separate numbers there, and the walk ties them. EXECUTED, NOT CLAIMED: the passage from the walk to its rays (mean position of packets against a cloud of rays with the packet's own spreads: agreement to 5 parts in 10^4 on a line for rest energies 0.05 to 0.8, at rest and moving up and down the gradient; to 2 parts in 10^3 in three dimensions for five orientations at wave vector 0.5, and to 1 part in 10^2 at wave vector 0.25 with a packet under two wavelengths wide), the content following the direction of travel through the turn, and the time-scaling identity to rounding. CORRESPONDENCE (of form, no gravitational claim): the weak-field packet's third supplied piece, the test response S_test = L_test (1 - phi) with force +m grad phi, is the first order of T2-T3 with phi = -u and m the packet's energy. NOT claimed: the objects and the clause; any statement about where records form (the parked statistical postulate is not used; mean positions describe the amplitude); the ray limit as a theorem; a rest energy for one walker; the rate field's own law and its sources; lengths (the clause times phases and says nothing about distances); any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_2026_09_21.py
---

# A phase timed by the local clock: every packet falls towards slow clocks, force = energy × gradient exactly, and the walk with the qubit as coin ties weight to inertia

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within supplied objects and a supplied clause; the passage from the walk to its rays is executed, not proved; nothing adopted or registered; unaudited)

This note works within a supplied clause for an amplitude whose phase is timed by local tick rates; it reports how such an amplitude moves in a given rate field; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 53 (open PR #8568) asked what law a local tick rate `w_x` can obey when there is no master clock, and found the lattice averaging equation with records as additive sources. It ended on a gap: a record whose *waiting time* is timed by the local clock drifts towards slow clocks, but a drift is not a fall. It has no inertia. The block named the next step: a record whose *phase* is timed by the local clock. This note does that step. The rate field is taken as given; any positive field will do.

**The objects (supplied).** One moving record is carried as an amplitude `ψ_x` with two components per site: the site's qubit is the record's content. A generator `H` moves it between nearest neighbours. **The clause (supplied).** The amplitude at a site advances in that site's own time.

1. **What the generator can be.** Translation invariance, hermiticity and the 24 rotations — the content turning as a direction, as in the campaign's soldered reading — leave three real numbers: a constant, a plain hopping term, and a term `β Σ_j σ_j sin k_j` that couples the content to the motion. For that term the velocity operator *is* the content: block 44's "content = direction of travel" is its expectation value. If inversion of the lattice is added as a symmetry (the Admissibility axiom names only proper rotations, so this is an extra assumption) the choice is forced: a content that reverses under inversion, as a direction does, leaves the coupled term alone — a walk with the qubit as its coin; a content that inversion does not touch removes it (T1).
2. **Timing the phase.** The clause turns `H` into `wH`. The conserved quantity is `Σ_x |ψ_x|²/w_x`, the same weight `1/w` that block 53's drifting record had, and the generator is, up to a change of variable, the hermitian `H_w = √w H √w`. Multiplying every rate by one number only changes the unit of time (T2).
3. **Force = energy × gradient, exactly.** Where `log w` has a uniform gradient, translating a packet by `a` multiplies its generator by the ratio `λ_a` of the clocks at the two places. Two exact consequences: the same packet, moved up the gradient, evolves faster by exactly that ratio; and in a state of energy `E` the wave vector along `a` falls at the constant rate `(λ_a − 1)E`. For a small gradient that is `dk/dt = −E ∇ log w`: a force towards slow clocks, proportional to the packet's energy, in every state, with no approximation (T3).
4. **Everything falls alike, because of the qubit.** A force proportional to energy gives the same fall to every packet only if inertia is proportional to energy too. For rays of `E = w(x) ε(k)` the fall is `−w² M ∇u + 2(v·∇u)v`, with `M` the matrix of second derivatives of `ε²/2`. The three content matrices anticommute, so the walk squares to a plain lattice operator, `ε² = Σ_j sin² k_j` (plus the square of any rest energy), and `M = diag(cos 2k_j)`: the unit matrix at long wavelength, whatever the energy and the rest energy. A packet at rest, or moving across the gradient, falls at `−∇u`; one moving along the gradient faster than `1/√2` of the limiting speed is pushed the other way. With the content decoupled from the motion (`β = 0`) the weight `e_0` and the inertia `M` are two separate numbers and a body falls at `e_0/M` times `−∇u` (T4).
5. **Executed.** Packets of the clocked walk were followed against clouds of rays carrying the packets' own spreads. On a line: rest energies from 0.05 to 0.8, at rest and moving both ways, agree with their clouds to 5 parts in 10⁴. In three dimensions, five orientations of motion and gradient against the lattice: 2 parts in 10³ at wave vector 0.5. The fall does depend on orientation — by the factor `cos 2k_j`, 16 per cent at wave vector 0.5 and 4 per cent at 0.25, vanishing at long wavelength. Block 51's wind differed by 30 per cent between directions at every distance. The content follows the direction of travel through the turn.

**With block 53's field** (open PR; conditional on both clauses): far from `N` records `u ≈ (3 log κ/2π) N/r`, so with `κ < 1` every long-wavelength packet falls towards the records at `(3|log κ|/2π) N/r²` in lattice units, whatever its energy and its direction of travel. One number, `κ`, is still supplied.

What one walker cannot have is a rest energy: nothing in `M₂(ℂ)` anticommutes with all three content matrices. In the executed runs the rest energy is motion across the gradient. The note records the fact and needs no larger site algebra; parked entry 4 is not touched.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 53 (PR #8568), next_trace_action: 'a record whose phase is timed by the local clock (a walk with the qubit as coin) and whether it accelerates in the field'; weak-field packet on main: the test response S_test = L_test (1 - phi) is supplied"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the amplitude as a source: whether action and reaction (a conserved energy for the pair of rate field and amplitude) forces the amplitude's energy density, not its probability density, to source the rate field; the ray limit of the clocked walk as a theorem at scope; the value of kappa; composite bodies and rest energy; a clause for lengths"
conditional_surface_status: "T1 exact for the stated class of generators (the inversion part under an added symmetry); T2 exact for every positive rate field; T3 exact as an algebraic identity on finitely supported amplitudes and, for the evolution, in a slab of uniform gradient while the amplitude stays inside; T4 exact for rays; the passage from the walk to its rays is executed only"
hypothetical_axiom_status: "the amplitude, its nearest-neighbour generator, the soldered action of the rotations on the content, the site-timed clause, and for the second half of T1 inversion as a symmetry; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom's site algebra `M₂(ℂ)`, the covariance sentence of Admissibility ("covariant under lattice translations and proper cubic rotations") and its statement that Admissibility does not "define a time metric". The memo contains no amplitude dynamics: update laws and rates are open gates. Nothing here fills a gate by derivation.

- **Amplitude.** `ψ: Z³ → ℂ²`; the two components are the content of one moving record (the owner's reading of 2026-09-20: records move, one per site at a time). `σ_1, σ_2, σ_3` are the three content matrices (the matrices of Pauli); a content direction `s` is the unit vector with `s·σ` of eigenvalue one.
- **Generator.** `H = Σ_e A_e T_e`, `e` over `0` and the six neighbour directions, `A_e ∈ M₂(ℂ)`, `(T_e ψ)(x) = ψ(x − e)`, so that `T_e` has the symbol `exp(−ik·e)`. `D_j = (i/2)(T_j − T_j†)` has the symbol `sin k_j`. A rotation `R` acts by `ψ(x) → U_R ψ(R⁻¹x)` with `U_R σ_j U_R† = Σ_k R_kj σ_k`: the content turns as a direction (the campaign's soldered reading, block 18).
- **Rate field.** A positive `w_x`, `u = log w`. Block 53's clause supplies one; nothing of block 53 is used except that such a field is there and that only ratios of rates mean anything.
- **The clause.** `i dψ_x/dτ_x = (Hψ)_x`, `dτ_x = w_x dt`.
- **Rays.** For an energy function `E(x, k)`: `dx_l/dt = ∂E/∂k_l`, `dk_l/dt = −∂E/∂x_l` (the equations of Hamilton); `v = dx/dt`.
- **Mean position.** `Σ_x x |χ_x|²` with `χ = ψ/√w`; a descriptor of the amplitude. No reading rule for where records form is used.

The generator `β Σ_j σ_j sin k_j` is the lattice form of the equation of Weyl, and with a rest energy of that of Dirac; its eight zero-energy points are the doubling of Nielsen and Ninomiya; walks with an internal coin are those of Aharonov, Davidovich and Zagury and of Meyer. That a map reversing every direction of a two-level system is antilinear is Wigner's analysis of the reversal of motion. An energy function `w(x) ε(k)` is the optical-mechanical analogy of Hamilton and the variable-speed-of-light picture of Einstein (1911); the law `−w²∇u + 2(v·∇u)v` is the equation of free motion for a line element `−w² dt² + dx²`. None is used as authority.

## Prior art and what is new

Every ingredient is classical: a wave in a medium whose local rate varies refracts towards the slow side, and the refraction of a wave is the fall of its packets. In Einstein's theory of 1915 the bending of light receives equal parts from the rates of clocks and from the measures of length; a field of clock rates alone, as here, gives the first part only, and the fall of slow bodies in full. What is new is the argument inside the framework's vocabulary: (i) that nearest-neighbour determination and rotation covariance, with the content soldered to the lattice, leave a three-parameter family in which the coupling of content to motion is a single term, forced or excluded by how inversion treats the content; (ii) that block 53's premise fixes how a rate field enters — through the timing of the phase — and that in a uniform gradient the resulting force law is an exact lattice identity, not a ray approximation; (iii) that the equality of weight and inertia for every packet is a property of the site algebra: the three content matrices anticommute, so the generator squares to a scalar. It is a conditional derivation of the weak-field packet's supplied response, not a gravitational claim.

## Exact target and obligation graph

Target: how an amplitude whose phase is timed by local clocks moves in a given rate field. Obligations: (O1) the admissible generators; (O2) what the clause does to a generator, and what is conserved; (O3) an exact statement of the force; (O4) the law of fall, and when it is the same for all packets; (O5) executed controls for the passage from the walk to its rays. T1–T4 discharge O1–O4; O5 is executed and not claimed.

## Theorem T1 — the generator

*Statement.* (a) A generator of the declared form that is hermitian and covariant under the 24 rotations has `A_0 = a_0`, `A_{±e_j} = a ± (iβ/2)σ_j` with `a_0, a, β` real; its symbol is `a_0 + 2a Σ_j cos k_j + β Σ_j σ_j sin k_j`. (b) No linear map `X → VXV⁻¹` reverses all three content matrices; the antilinear map `X → σ_2 X̄ σ_2` does. (c) Let inversion `x → −x`, acting on the content by `V`, be a symmetry of the evolution, `P U(t) P⁻¹ = U(t)`. If `V` reverses the content, `a_0 = a = 0`. If `V` leaves the content untouched, `β = 0`. (d) For the walk `H = Σ_j σ_j D_j` (`β = 1`): `H² = Σ_j D_j²`, with energies `±(Σ_j sin² k_j)^{1/2}`; `i[H, X_j] = σ_j (T_j + T_j†)/2`; and the only `X ∈ M₂(ℂ)` with `Xσ_j + σ_jX = 0` for `j = 1, 2, 3` is `X = 0`.

*Proof.* (a) Covariance reads `U_R A_e U_R† = A_{Re}`. The rotations that fix `e_3` are the four turns about it; the matrices commuting with the quarter turn `exp(−iπσ_3/4)` are `a + bσ_3`. The half turn about `e_1` sends `e_3` to `−e_3` and `σ_3` to `−σ_3`, so `A_{−e_3} = a − bσ_3`; the rotations are transitive on the six directions, so the same `a, b` serve all of them. `A_0` commutes with every `U_R`, and these generate `M₂(ℂ)`, so `A_0 = a_0`. Hermiticity is `A_{−e} = A_e†`: `a, a_0` real and `b = iβ/2` imaginary. Summing `A_e exp(−ik·e)` gives the symbol. (b) A multiplicative linear map sends `σ_1σ_2 = iσ_3` to `(−σ_1)(−σ_2) = iσ_3` and also to `i(−σ_3)`: a contradiction. For the antilinear map, `σ_2 σ̄_j σ_2 = −σ_j` for each `j`. (c) A linear `P` commutes with the evolution iff `PHP⁻¹ = H`; an antilinear one iff `PHP⁻¹ = −H`, since it turns `−iH` into `+iPHP⁻¹`. Inversion sends `T_e` to `T_{−e}`. Content reversed: `V A_{−e} V⁻¹ = −A_e` reads `ā + b̄σ_j = −a − bσ_j` and `ā_0 = −a_0`; with `a, a_0` real they vanish, and `b` imaginary is what hermiticity already requires. Content untouched: `A_{−e} = A_e` gives `b = 0`. (d) The `D_j` commute and `σ_jσ_l + σ_lσ_j = 2δ_jl`, so the cross terms of `H²` cancel. `[T_l, X_j] = −δ_lj T_l` gives the velocity operator. The eight real equations of `Xσ_j + σ_jX = 0` have rank eight. ∎

Under the symmetries the axiom names — proper rotations only — the three-parameter family stands. What the rest of the note needs at long wavelength is `β ≠ 0` and `a_0 + 6a = 0` (no energy at zero wave vector; see T4); inversion with a reversing content gives both exactly. If the content did not turn with the lattice at all (an unsoldered content) covariance would force `A_e` to be the same matrix for every direction, and the content would never couple to the motion.

One walker has no rest energy: a term that opens a gap at zero wave vector must anticommute with the walk, and nothing in the site algebra does.

## Theorem T2 — the clocked generator

*Statement.* Under the clause, `i dψ/dt = WHψ` with `W = diag(w_x)`. `WH` is self-adjoint for `⟨φ, ψ⟩_w = Σ_x φ̄_x ψ_x / w_x`, so `Σ_x |ψ_x|²/w_x` is conserved; for a non-uniform `w` it is not self-adjoint for the plain inner product. With `χ = W^{−1/2}ψ`, `i dχ/dt = H_w χ`, `H_w = W^{1/2} H W^{1/2}`, hermitian, every bond carrying the amplitude `√(w_x w_y)`. Timing by the sending site, `HW`, is similar to the same `H_w`. Replacing `w` by `tw` replaces `H_w` by `tH_w`.

*Proof.* `dτ_x = w_x dt` gives the generator. `(WH)†W⁻¹ = H†WW⁻¹ = H = W⁻¹(WH)` is self-adjointness for the weighted inner product. `W^{−1/2}(WH)W^{1/2} = W^{1/2}HW^{1/2} = W^{1/2}(HW)W^{−1/2}`. The last sentence is degree one of `√(w_x w_y)`. ∎

The weight `1/w` is the one block 53's site-timed test record had in its stationary law: an amplitude, like a walker, counts for more where its clock runs slow. The three timings (receiving site, sending site, bond) differ in which variable is called the amplitude, by a factor of `√w` that shifts a packet's mean position by a fixed amount of order `g` times its squared width; they do not differ in the motion. A change of the unit of rate is a change of the unit of `t` and nothing else, as block 53's premise demands.

## Theorem T3 — a uniform gradient: force = energy × gradient, exactly

*Statement.* Let `H` be any translation-invariant generator, and let `w(x + a) = λ_a w(x)` for every site `x` of a region and a lattice vector `a` (in a uniform gradient `u = g·x`, `λ_a = exp(g·a)`). On finitely supported amplitudes whose `n`-step neighbourhoods, with those of their translates, lie in the region,
`H_w^n T_a = λ_a^n T_a H_w^n` for every `n`.
The same holds for any bond timing homogeneous of degree one, such as `(w_x + w_y)/2`. Consequently, in a slab of uniform gradient and for as long as the amplitude stays inside it, `U_w(t) T_a = T_a U_w(λ_a t)` and
`T_a(t) := U_w(t)† T_a U_w(t) = T_a exp(i(λ_a − 1) H_w t)`.
For a rate field that is not exponential there is no such identity.

*Proof.* `(W T_a ψ)(x) = w(x) ψ(x − a) = λ_a w(x − a) ψ(x − a) = λ_a (T_a W ψ)(x)`, so `W^{1/2} T_a = λ_a^{1/2} T_a W^{1/2}`, and `H` commutes with `T_a`: `H_w T_a = λ_a T_a H_w`; iterate. A bond timing of degree one scales by `λ_a` under the translation in the same way. Then `f(H_w) T_a = T_a f(λ_a H_w)` for polynomials `f`, which is the statement about the evolution wherever the evolution is approximated by polynomials in `H_w` applied inside the region. `U_w(t)†T_aU_w(t) = T_a U_w(λ_a t)† U_w(t)`. For `√w = 1 + x_3²` the two sides of the first identity differ by factors that depend on the site (5 and 25/4 at neighbouring sites). ∎

Reading: in a state of wave vector `k` and energy `E`, `⟨T_a⟩ = exp(−ik·a)`, and the identity says its phase advances at the rate `(λ_a − 1)E`: `d(k·a)/dt = −(λ_a − 1)E`, that is `dk/dt = −E∇u` for a small gradient. The force points towards slow clocks and is proportional to the energy of the state, for every generator and every state. And a packet moved up the gradient by `a` does everything `λ_a` times faster, which is what it means for `w` to be the local rate of clocks.

The statement is made for a slab, not for the whole lattice. With a uniform gradient everywhere the rates are unbounded, a ray of the walk moving up the gradient obeys `dz/dt = exp(gz)` and reaches infinity at the finite time `1/g`, and the evolution is not defined without further data at infinity. In a slab the leakage out of it is what limits the identity; in the executed runs it holds to rounding.

## Theorem T4 — the law of fall, and what ties weight to inertia

*Statement.* For rays of `E = w(x) ε(k)`, with `v_j = w ∂ε/∂k_j` and `u = log w`,
`dv_j/dt = −w² Σ_l M_jl ∂_l u + 2 (v·∇u) v_j`, `M_jl = ∂²(ε²/2)/∂k_j∂k_l`.
(a) The law has the form `−w²∇u + 2(v·∇u)v`, containing nothing of the ray but its velocity, for every gradient iff `M` is the unit matrix, that is `ε² = |k − k_0|² + const` on a connected region. Then, the constant being non-negative, `|v| ≤ w`; a ray at rest or moving across the gradient falls at `−w²∇u`; a ray moving along the gradient at speed `v` is accelerated by `−w²(1 − 2v²/w²)∂u`, which changes sign at `v = w/√2` and is `+w²∂u` at the limiting speed. (b) For the walk, with or without a rest energy `m`, `ε² = m² + Σ_j sin² k_j` and `M = diag(cos 2k_j)`: the velocity-only law at long wavelength, with relative corrections `−2k_j²`, and exactly `−w²g` for a ray with no wave vector along an axis gradient, whatever its transverse wave vector. (c) With a constant `e_0` added to the walk's energy a transverse ray falls `1 + e_0/|k|` times faster. (d) For `β = 0`, `ε = e_0 + k²/(2M)`, a ray at rest falls at `(e_0/M)` times `−∇u`.

*Proof.* `dv_j/dt = Σ_l (∂v_j/∂x_l)(dx_l/dt) + (∂v_j/∂k_l)(dk_l/dt) = Σ_l (w ∂_l u ∂_jε)(w ∂_lε) − (w ∂_j∂_lε)(ε w ∂_l u) = (v·∇u)v_j − w² Σ_l ε ∂_j∂_lε ∂_l u`, and `ε ∂_j∂_lε = ∂_j∂_l(ε²/2) − ∂_jε ∂_lε`, whose second part gives `(v·∇u)v_j` again. (a) The coefficients of the three components of `∇u` are independent, so the form holds for every gradient iff `M = 1`; integrate twice. `v = w(k − k_0)/ε` has `|v| ≤ w` when the constant is non-negative. (b)–(d) Differentiate. ∎

The force of T3 is proportional to the energy. Every packet falls alike only if the inertia is proportional to the energy too, and `M = 1` is that statement. The walk has it because it squares to a plain lattice operator, and it squares to one because the three content matrices anticommute: the tie between weight and inertia is a property of the qubit. A walker whose content is decoupled from its motion has a weight `e_0` and an inertia `M` with nothing to relate them.

The walk's energy vanishes at the eight points `k_j ∈ {0, π}`; `M` is the unit matrix at each, so packets near any of them fall alike. They are not pursued here.

## Executed (supervisor controls; floating point; evidence, not proof)

`specs/supervisor_control_block54_clocked_line.py` — the rate field depends on `z` only, so the transverse wave vector is conserved and the walk reduces to a two-component walk on a line in which transverse motion acts as a rest energy `m`. Each packet is compared with a cloud of 160000 rays drawn with the packet's own spreads of position and wave vector.

| packet (`g = 0.002`, `T = 100`, width 40; `−gT²/2 = −10`) | fall of the walk | cloud of rays |
|---|---|---|
| at rest, `m = 0.05` | −8.9626 | −8.9673 |
| at rest, `m = 0.1` | −9.6675 | −9.6692 |
| at rest, `m = 0.2` | −9.8578 | −9.8589 |
| at rest, `m = 0.4`, transverse direction (1,0) / (1,1) / (3,4) | −9.8886 / −9.8694 / −9.8657 | −9.8896 / −9.8703 / −9.8666 |
| at rest, `m = 0.8` | −9.8343 | −9.8353 |

The falls differ because a packet of width 40 has a spread of 0.0125 in wave vector, which at `m = 0.05` is a spread of a quarter of the limiting speed, and by T4 the moving parts of a packet fall less; the clouds reproduce each number to 5 parts in 10⁴. Moving packets (`m = 0.05`, `g = 0.001`, `T = 200`, width 100), excess of the displacement over uniform motion, starting up / down the gradient: at 0.3 of the limiting speed `−18.8 / −14.0`; at 0.5 `−13.3 / −7.5`; at 0.707 `−2.1 / +1.3`; at 0.85 `+9.5 / +8.6` — the change of sign of T4(a), blurred because the rate changes by up to 20 per cent along these paths; walk over cloud between 0.9999 and 1.0000 in all eight. With no transverse motion the packet moves at the local limiting speed: `+247.41` up and `−159.23` down in `T = 200` against `+247.43` and `−159.24`. The time-scaling identity of T3 for shifts of 1, 10 and 100 sites: `4×10⁻¹⁵`, `4×10⁻¹⁵`, `6×10⁻¹⁵` (against `0.035`, `0.35`, `1.9` with the time not rescaled).

`specs/supervisor_control_block54_orientation.py` — three dimensions, open boxes of side 68 and 80, a positive-energy packet, `g = 0.004`, `T = 30`; the fall is half the difference between runs with `+g` and `−g`.

| motion / gradient | wave vector 0.5: walk, cloud, central ray's law | wave vector 0.25: walk, cloud, central ray's law |
|---|---|---|
| (1,0,0) / (0,0,1) | −1.6164, −1.6137, −1.8000 | −1.5241, −1.5118, −1.8000 |
| (1,1,0) / (0,0,1) | −1.6199, −1.6178, −1.8000 | −1.5263, −1.5151, −1.8000 |
| (1,−1,0) / (1,1,1) | −1.3726, −1.3714, −1.5123 | −1.4649, −1.4549, −1.7258 |
| (1,1,−2) / (1,1,1) | −1.3717, −1.3714, −1.5069 | −1.4661, −1.4573, −1.7254 |
| (2,1,0) / (1,−2,3) | −1.5342, −1.5310, −1.6994 | −1.5056, −1.4911, −1.7744 |

Walk over cloud: 1.0002 to 1.0021 at wave vector 0.5; 1.006 to 1.010 at 0.25, where the packet is under two wavelengths wide. The dependence on orientation is T4(b)'s factor: axis gradient over body-diagonal gradient 1.18 at wave vector 0.5 (central rays 1.19) and 1.04 at 0.25 (1.04). Through the fall the velocity turns by 6.0 to 7.4 degrees and the content by 6.6 to 6.9; the angle between them at the end is 0.3 to 2.3 degrees (at wave vector 0.5 the group velocity and the content already differ by up to 1.9 degrees at the start, a lattice effect).

## Correspondence with the weak-field packet (of form; no gravitational claim)

| supplied in the packet on `main` | within this note's objects and clause |
|---|---|
| operator `−Δ_lat`, zero mode projected out | block 53 (open PR #8568), not this note |
| source `ρ = |ψ|²` | not addressed: block 53 has records as sources; whether the amplitude is a source is the next question |
| test response `S_test = L_test(1 − φ)`, `U = −mφ`, `F = +m∇φ` | the phase accumulated over a stretch is timed by `w = exp(u) = 1 + u + …` (T2); the force is `−E∇u` exactly in a uniform gradient (T3): `φ = −u`, and `m` is the packet's energy |
| (not in the packet) the inertia that turns a force into a fall | tied to the energy by the walk (T4): `−∇u` for every packet at long wavelength |

## No-Go Discipline Gate

The note's negative sentences: one walker has no rest energy; a content that inversion leaves untouched does not couple to the motion; the identity of T3 fails for rate fields that are not exponential; with an energy offset, or with the content decoupled, the fall is not the same for all packets.

### N1 — Routes by which the sentences could fail
1. *A larger site algebra* — with more anticommuting matrices a rest energy exists. That is the enlargement parked as entry 4 of `docs/repo/DEFERRED_DECISIONS.md`; it is not used, not proposed and not woken: nothing in this note needs it.
2. *Generators that reach further than nearest neighbours* — more parameters; the long-wavelength conclusions need only a spectrum that passes linearly through zero energy at zero wave vector. Not worked.
3. *A step in place of a generator* — for a walk in discrete steps the clause has no direct analogue, since a step is itself a unit of time. Not worked.
4. *The passage from the walk to its rays* — executed to the accuracies quoted, not proved; a rate field varying on the scale of a wavelength is outside both T3 and T4.
5. *Composite bodies* — a bound state of several walkers has an internal energy that acts as a rest energy; if its energy function is `w(X)` times a function of its total wave vector, T4 applies to it. Not worked.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The note is conditional on supplied objects: an amplitude over sites is not an object of the axioms, and neither is a generator or a rate field. Hermiticity is assumed for the plain inner product at uniform rate. The content is soldered to the lattice. Inversion is not among the symmetries the Admissibility axiom names; T1(c) is conditional on adding it. The mean position describes the amplitude; no rule for where a record forms is used, and none is needed for T3.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice, its rotations, the site algebra `M₂(ℂ)`; the covariance sentence; the absence of amplitude dynamics and of a time metric | yes (premise; the absences motivate the objects and the clause and do not prove them) |
| block 53 (open PR #8568) | the premise that only ratios of rates mean anything; the rate field of records, for the closing corollary | restated; the corollary is conditional on it |
| blocks 18, 44 (open PRs #8152, #8550) | the soldered reading of the content; content = direction of travel | placement |
| blocks 51, 52 (open PRs #8563, #8564) | the record layer's direction-dependent wind, for comparison | placement |
| weak-field packet (`main`) | the supplied test response the correspondence is drawn with | target, not premise |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "three-parameter family, the walk under a reversing inversion, no rest energy; `wH` conserves `Σ|ψ|²/w`; `H_w^n T_a = λ_a^n T_a H_w^n`; the ray law and its matrix `M`" | executed: products of the content matrices; the 24 rotations on the 56 real coefficients with four behaviours under inversion; rank eight for an anticommuting matrix | executed: the walk, its square and its velocity operator on single-site amplitudes; the translation identity at three sites, four shifts, two contents, with its third power | executed: ray equations at rational points with exact second-order jets: six points of the walk's energy surface, the long-wavelength law at 3/5 and 4/5 of the limiting speed, an offset, three uncoupled walkers | executed: the clocked generator on the `3×3×3` torus with a rational rate field | T1 for every generator of the class; T2 for every positive rate field; T3 for every uniform gradient and state, in a slab; T4 for rays of any `w(x)ε(k)`; the ray limit executed only; the objects, the clause, the rate field and record formation not derived |

### N6 — Partial-closure paths and primitive scan
The registered primitives do not supply the objects or the clause. `kinetic_isotropy_primitive` grants the equality `c_t = c_s` of a kinetic form; the equal limiting speed of the walk along the three axes is a consequence of rotation covariance here and the primitive is not used. `scale_reference_primitive` converts units; `realized_state_primitive` grants evaluation at a supplied state. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "An energy `w(x)ε(k)` is the textbook analogy between optics and mechanics; you have put the answer in." Reply: the ray law is classical and is named as such. What is argued here is where the form comes from inside the framework — block 53's premise leaves the timing of the phase as the way a rate field can act — and two things that are not in the analogy: an exact lattice identity for the force, valid for every state, and the role of the site algebra in tying inertia to energy, with the decoupled walker as the control in which the tie is absent. Second objection: "Only records are readable; a mean position is not." Reply: agreed; the mean position is a descriptor of the amplitude, T3 needs no reading rule at all, and what the amplitude implies for where records form is the parked statistical postulate, which is not used. Third objection: "Inversion is not in the axiom." Reply: agreed and flagged; without it the three-parameter family stands and the long-wavelength conclusions need `β ≠ 0` and `a_0 + 6a = 0`.

### N8 — Cross-cycle echo
Block 44 made the content a direction of travel by fiat; here it is the velocity operator of the one covariant term that couples content to motion. Blocks 51 and 52 found the record layer's wind direction-dependent at every distance unless most hops ignore the content; here the dependence on direction is `cos 2k_j`, of second order in the wave vector. Block 53's test record drifted with the stationary weight `1/w`; the same weight is the conserved density here, and the drift has become a fall. Block 50 set a record's clock by a ratio; T3 is the statement that a translate's clock is set by the ratio `λ_a`.

## Falsifiers

- A hermitian, translation-invariant, rotation-covariant nearest-neighbour generator on two-component amplitudes outside the three-parameter family; one that commutes with a content-reversing inversion and is not the walk.
- A `2×2` matrix anticommuting with all three content matrices.
- A positive rate field and an amplitude for which `Σ_x |ψ_x|²/w_x` changes under the clause.
- A uniform gradient and a finitely supported amplitude with `H_w^n T_a ≠ λ_a^n T_a H_w^n`.
- An energy function with `M ≠ 1` whose rays obey the velocity-only law for every gradient.
- A long-wavelength packet in a slowly varying rate field whose mean position departs from its cloud of rays by more than the quoted accuracies.

## Boundaries and non-claims

The amplitude, the generator, the soldered content and the clause are supplied; the axioms contain none of them. Inversion is an added symmetry. One walker has no rest energy; in the executed runs rest energy is transverse motion, and composite bodies are not worked. The passage from the walk to its rays is executed, not proved. T3 is exact in a slab of uniform gradient and says nothing about rate fields that vary faster. Where records form is not addressed; the parked statistical postulate is not used. The rate field is given: its law and its sources are block 53's (open), and whether the amplitude is itself a source is not addressed. The clause times phases and says nothing about lengths: a ray at the limiting speed moving across the gradient is bent at `−w²∇u`, the same as a body at rest. The correspondence with the weak-field packet is one of form. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the site algebra of the Qubit axiom, the covariance sentence of Admissibility, and the memo's silence on amplitude dynamics and the time metric. Block 53 (PR #8568, open): restated. Blocks 18, 44, 51, 52 (PRs #8152, #8550, #8563, #8564, open): placement. The weak-field packet on `main`: the target of the correspondence.
- Named standard imports at definition level: the products of the three content matrices; the ray equations of an energy function; similarity of matrices; the exponential of a bounded generator.
- Reference only: Pauli; Weyl and Dirac; Nielsen and Ninomiya; Aharonov, Davidovich and Zagury; Meyer; Wigner; Hamilton; Einstein (1911, 1915).

## Review record
Supervisor-run block, the second of the source-link direction, on the owner's instruction "ok lets work the source link into the amplitude layer". Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the Admissibility axiom names proper rotations only, so the inversion argument is an added assumption — T1 was split, and the long-wavelength conditions are stated without it; an amplitude is not an axiom object and a mean position is not a reading. A rigour lens: with a uniform gradient everywhere the rates are unbounded and a ray escapes at the time `1/g`, so T3's statement about the evolution is made for a slab; an "iff" was taken out of the title and T4(a) states what the equivalence is. A lattice lens: the eight zero-energy points; the orientation factor `cos 2k_j`. A comparator lens: a field of clock rates alone gives the fall of slow bodies in full and half of the comparator's bending of light; recorded under Prior art and Boundaries. A strategy lens: the packet's supplied response follows from the clause, and the open piece of the source link is whether the amplitude's energy is a source. Refuting pass (`specs/supervisor_control_block54_refuter.py`, machinery disjoint from the runner's): W1 the general generator with explicit `2×2` unitaries and symbolic matrices (three parameters; one with a reversing inversion, the walk surviving; two with the content untouched, the walk excluded); W2 the ray law for a general energy function, symbolically, and `M = diag(cos 2k_j)` free of the rest energy; W3 a random rate field on the `3×3×3` torus (`Σ|ψ|²/w` kept to `8×10⁻¹⁶`, `Σ|ψ|²` changed by 0.19; the spectrum of `wH` real and equal to that of `H_w`); W4 the identities of T3 in a slab (`3×10⁻¹⁵`, `6×10⁻¹⁶`); W5 the reduced walk against clouds of rays. All pass. Findings folded from the controls: the first control measured displacements from the nominal centre of the packet, while the spinor's dependence on the wave vector shifts the mean by several sites, which read as falls differing by a quarter between rest energies and by 5 per cent between transverse directions that are unitarily equivalent; the comparison with a single ray left a 1 per cent excess and deficits up to 10 per cent, both effects of the packet's size (the mean of `w²` over the packet; the spread of velocities, which fall less by T4), removed by comparing with a cloud of rays; a body-diagonal run showed a displacement of `−0.35` where `−1.6` was expected, because at wave vector 0.5 the group velocity is not parallel to the wave vector and the packet drifts up the gradient — the fall is now the part odd in `g`; the first boxes had 1 to 2 per cent of the weight near the walls and were enlarged. Mutation census: 12 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_2026_09_21.py
```

Expected: `TOTAL: PASS=24 FAIL=0`.
