---
claim_id: admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied second-neighbour strain coupling: lattice curls are unchanged by additive displacement gradients, the fixed-state strain derivative is the specified bond current, and curl-only field derivatives have identically zero divergence. This supplies a necessary compatibility condition, not existence of a static solution for every curl energy or stationary state. Within the explicitly chosen six-coefficient continuum density ansatz, infinitesimal local coin-rotation invariance through the stated orders fixes the coefficients to a volume term plus the curvature combination. With nonzero coefficient and the separate weak-field scalar model this gives beta=1; no universal family classification or empirical bending is proved. If a lattice field energy is separately assumed exactly independent of additive antisymmetric bond strains, the displayed stationary state violates its necessary torque condition. Continuum rotation invariance does not itself establish that exact lattice premise."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_2026_09_21.py
---

# Bond strains and plaquette curls: a field energy per local tick that does not see the coin's axes is the curvature member

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact lattice identities within the supplied clauses of blocks 54, 60, 62, 63 widened by a strain on every bond; exact continuum identities to the orders stated; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes with the qubit as their coin and for a ledger linear in the rates, widened by a strain on every bond; it reports what the lattice keeps exactly and which field energies do not see the orientation of the coin's axes; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Curl invariance and the current-response identity are exact on the lattice. Matching their divergences is necessary for static field equations, but does not establish existence: a constant field energy already supplies a counterexample for nonzero conserved current, and periodic zero modes add constraints.

The coefficient selection is within a supplied six-term continuum ansatz. Requiring local rotation invariance for arbitrary rate multipliers makes the density variation vanish point by point, to the perturbative orders tested. This is an additional invariance requirement, not a consequence of rate linearity alone. The surviving nonzero combination equals minus volume times scalar curvature through second order; its isotropic weak-field exponent is one under the companion scalar model's assumptions.

The exact lattice torque obstruction is conditional on a stronger, separately supplied property: independence from additive antisymmetric bond-strain variations at every site. No exactly rotation-invariant lattice discretization is constructed. The continuum transformation of the frame and an additive rotation of the second-neighbour coupling are not interchangeable at finite wave number.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (sites, bonds, translations, proper rotations), the Qubit axiom's one-site algebra with no possibility privileged, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 60, 62, 63 (open PRs) supply the walk, the ledger linear in the rates, the frame and what the walk conserves.

- **Strain.** `B_a^j(x)`, real, on the bond from `x` along `a`. **Coupling** `H[B] = H + Σ_{a,j} σ_a ½{C_a[B_a^j], S_j}`, `C_a[v]` the symmetric hop along `a` weighted by the bond function `v` (block 63). **Relabelling** `B_a^j → B_a^j + (d_aξ_j)`, `ξ` on the sites.
- **Curl** `F_ab^j(x) = (d_aB_b^j)(x) − (d_bB_a^j)(x)` on the plaquette at `x` spanned by `a < b`.
- **Frame and its curl (continuum).** `e^j_a = δ^j_a +` strain; `T^j_ab = ∂_a e^j_b − ∂_b e^j_a`; bond indices are turned into coin indices with the inverse frame; `V_b = T^a_ab`; `T_1 = T^j_{kl}T^j_{kl}`, `T_2 = T^j_{kl}T^l_{kj}`, `T_3 = V_lV_l`; `ε·T = ε^{jkl}T^j_{kl}` (odd under inversion, which the Lattice axiom does not include). To first order the frame's strain is minus the walk's `B` (the walk's coupling is to the inverse frame, block 62).
- **The family.** `D = c_0 det e + c_5 det e (ε·T) + det e [c_1T_1 + c_2T_2 + c_3T_3] + c_4 ∂_b(det e V^b)`: an explicitly supplied six-coefficient continuum ansatz. Completeness among all densities allowed by lattice symmetry, other tensor contractions, nonpolynomial terms or higher derivatives is not asserted. **Ledger** `F = Σ_x w_x D_x` (block 60).
- **Rotation of the coin axes.** `e → R(x)e`, `R(x)` a rotation acting on the coin index.

A frame with the curl as its field strength and no connection is the teleparallel description of Weitzenböck and of Einstein's papers of 1928 to 1930; the three quadratic invariants and the one-parameter family of theories they give are those of Hayashi and Shirafuji; that one combination differs from the scalar curvature by a divergence, and is the only one blind to local rotations of the frame, is the basis of the teleparallel equivalent of the comparator theory (Møller; Cho). That a Lagrangian is blind to local rotations only up to a divergence, while a Lagrangian multiplied by a position-dependent factor needs blindness point by point, is the known reason the lapse spoils the local symmetry of the torsion scalar alone. That the scalar curvature is the only density with two derivatives built from a metric is the theorem of Cartan, Weyl and Vermeil, extended by Lovelock. Lattice fields on bonds with invariants on plaquettes are Wegner's and Wilson's. None is used as authority; the comparator is quoted as a comparator.

## Prior art and what is new

The lattice current identities and the continuum coefficient calculation are distinct results. They do not construct an exactly rotation-invariant discrete field action or a self-consistent coupled stationary solution.

## Theorem T1 — the lattice, exactly

*Statement.* (a) `F_ab^j[B + dξ] = F_ab^j[B]` for every `B` and `ξ`. (b) `H[B]` is hermitian, and `∂⟨H[B]⟩/∂B_a^j(x) = J_a^j(x → x + e_a)` for every state. (c) For every function `𝓕` of the curls, `Σ_a [∂𝓕/∂B_a^j(x) − ∂𝓕/∂B_a^j(x − e_a)] = 0` at every site, for each `j`. (d) Hence at first order in the strain, with uniform rates, the static equations `∂𝓕/∂B_a^j = −J_a^j` satisfy the necessary divergence compatibility condition for stationary states of the unperturbed walk. Solvability requires additional range, zero-mode, boundary and nondegeneracy conditions; no existence theorem for arbitrary functions of curls follows.

*Proof.* (a) `d_a d_b ξ = d_b d_a ξ`. (b) `C_a[v]` and `S_j` are hermitian and the anticommutator of hermitian operators is hermitian; `⟨H[B]⟩` is linear in `B` and block 63 T2(b) identifies the coefficient. (c) `𝓕[B + dξ] = 𝓕[B]` for all `ξ`; differentiate in `ξ_j(x)` and sum by parts. (d) Block 63 T2(c): `J` is divergence-free on stationary states. ∎

On a closed lattice the uniform part of the current is not balanced by any curl; thus a nonzero uniform current supplies a further obstruction. This does not exclude all vacuum or signed-source periodic configurations.

## Theorem T2 — blindness to the coin's axes fixes the density

*Statement.* Let `e = (1 + ηΩ(x))(1 + εB(x))` with `Ω` antisymmetric. The part of `D` of first order in `η` vanishes identically at orders `ε⁰` and `ε¹`, for all `Ω` and `B`, iff `c_5 = 0`, `c_1 = −c_4/8`, `c_2 = −c_4/4`, `c_3 = c_4/2`. `c_0` is unconstrained.

*Proof.* At order `ε⁰` the change of `D` is `c_5` times `4 div ω` (`ω` the axial vector of `Ω`) — the divergence term contributes `∂_a∂_bΩ_{ab} = 0`. At order `ε¹` the change is a polynomial in the derivatives of `B` and `Ω` whose coefficients are, up to sign, `2c_1 − c_2`, `2c_1 + c_2 + c_3`, `2c_3 − c_4`, `4c_2 + c_4` and `4c_5` (runner C1). `det e` is unchanged by a rotation. ∎

*Why point by point.* `F = Σ_x w_x D_x`. If `D` changed by a divergence, `F` would change by minus the sum of that divergence's argument against the differences of the rates, which are arbitrary (the rates are independent supplied coefficients here; the full hopping energy need not be linear in them). The weaker demand — unchanged up to a total divergence, tested by the vanishing of all variational derivatives of the first-order change — fixes `c_5 = 0` and `c_1 : c_2 : c_3 = 1 : 2 : −4` and leaves `c_4` free (runner C2).

## Theorem T3 — the blind density is the curvature

*Statement.* (a) `D* = det e [¼T_1 + ½T_2 − T_3] − 2∂_b(det e V^b) = −√g R[g]`, `g = eᵀe`, point by point, through second order in a general strain. (b) Writing the strain as symmetric plus antisymmetric, the second-order part of `D*` has zero variational derivative with respect to the antisymmetric part. (c) With `c_4 = −2K` and `c_0 = 0`, `F = Σ_x w_x K D*_x` is block 60's member; on `e = ℓ·1` it is `+K ℓ(4Δλ + 2|∇λ|²)`, and on `diag(ℓ_j)` block 61's.

*Proof.* (a) Direct expansion of both sides (runner D1; nine strain functions). (b) By (a) the density depends on the strain through `g` alone, and `g` contains the antisymmetric part only at second order, where it enters the first-order curvature — a double divergence (runner D2). (c) From (a) and blocks 60, 61. ∎

`c_0 = 0` is the requirement that the unstretched lattice with uniform rates and no content be a solution (as `f(0) = 0` was in block 55 T4).

## Theorem T4 — what blindness buys

*Statement.* On `e = ℓ·1`, `ℓ = e^λ`: `D = −2c_4 Δλ·ε + (4c_1 + 2c_2 + 4c_3)|∇λ|²·ε² + …` up to a second-order total derivative. In block 60 T3's notation `a = −2c_4`, `ap − b = −(4c_1 + 2c_2 + 4c_3)`, and block 59's exponent is `β = c_4/(4c_1 + 2c_2 + 4c_3)`. For `c_2 = c_3 = 0`: `β = c_4/(4c_1)`, and the second-order part of `det e·T_1` has a non-zero variational derivative with respect to the antisymmetric strain. For the selected nonzero invariant combination `β = 1`; the denominator and coupling must be nonzero. The zero action also obeys the invariance conditions and has no defined exponent. This is the conditional scalar weak-field exponent, not a general exact deflection measurement.

*Proof.* Expansion (runner E1, E2) and block 60 T3(b). ∎

So the family without blindness is block 59's situation again — a free exponent — with three additional fields that no walker in a uniform frame sees. With blindness the coefficient ratios in this chosen ansatz are fixed up to overall scale. The continuum ansatz, local invariance, vanishing volume term and discrete realization remain supplied choices.

## Theorem T5 — what blindness costs

*Statement.* Let `ω_{aj}(x)` be antisymmetric and consider the strain `δB_a^j(x) = ω_{aj}(x)`: a rotation of the three bonds that leave `x`. (a) `∂⟨H[B]⟩/∂ω_{aj}(x) = J_a^j(x → x + e_a) − J_j^a(x → x + e_j)` for every state. (b) If the field energy does not depend on `ω`, stationarity of the ledger in `ω_{aj}(x)` is `J_a^j(x → x + e_a) = J_j^a(x → x + e_j)` at every site. (c) The exactly stationary superposition of block 63 on the `4 × 4 × 4` torus (`Hψ = ψ`) violates (b) at all 64 sites, for each of the three pairs `(a, j)`; the violations sum to zero over the torus.

*Proof.* (a) T1(b). (b) By definition. (c) Computation with Gaussian rationals (runner E3). ∎

The zero total torque in the runner is a property of that specific axis-wave superposition, not every stationary state or a general uniform-rotation symmetry of H[B]. For a uniform plane wave with sines `(3/5,4/5,0)`, positive energy one and corresponding cosines `(4/5,3/5,1)`, the bond-current antisymmetry per unit probability is `J_1^2-J_2^1=12/125`, nonzero even uniformly. The extra cosine in the second-neighbour coupling prevents identifying additive antisymmetric B with a global coin conjugation of the original walk.

T5 therefore excludes the displayed fixed sources under an explicitly assumed exact additive-antisymmetric null direction. It does not exclude every stationary state, nor does it derive that null direction from the perturbative continuum result. Local rotations of a general coframe obey delta e=Omega e; higher-order terms and nonuniform rate weights cannot be discarded to turn that into an exact discrete additive transformation.

## Historical experiments — deferred

Original finite-strain numerical spectra and rational-point continuum checks remain recoverable on the original PR branch. They are not a proof at all strain orders and are not fresh canonical evidence. The fresh runner covers the explicitly truncated symbolic identities and exact finite lattice controls.

## No-Go Discipline Gate

The note's negative sentences: no other density of the family is blind; a member that sees the coin axes has a free exponent and three more fields; the blindness is not a symmetry of the walk; the stated stationary source violates the necessary equation if exact additive antisymmetric strain independence is supplied.

### N1 — Routes by which the sentences could fail
1. *A wider family.* Densities with more differences, or that are not functions of the curls (they would see relabellings), are outside T2.
2. *Blindness up to a divergence.* That is the weaker demand appropriate to a field energy that is NOT multiplied by the rates; it leaves `c_4` free and fixes only `c_5 = 0` and `c_1 : c_2 : c_3` (runner C2); then the rates do not couple to the lengths at first order with a fixed strength and `β` is free again. The strengthening follows from the additional local invariance demand for arbitrary rates, not from linearity in rates alone.
3. *The lattice.* The contractions in `T_2`, `T_3` and `div V` mix the coin index with the bond index and have no unique placement on the lattice; curl-only lattice functions satisfy T1; inverse-frame contractions and chosen placements need their own invariance proof. No exactly rotation-invariant lattice realization of the continuum combination is established here. T2–T4 are leading-order statements in the wave vector.
4. *The content's side.* A rotation of the coin axes that varies from site to site is not a symmetry of the walk (block 62 N1.2); block 63 T5 ties the unseen part of the response to the torque on the coin, and T5 here shows the torque is not zero on a stationary state. Blindness of the field energy is supplied, not inherited, and its exact additive lattice version conflicts with the specific source in T5. The exit is a content that is blind: in the comparator a connection built from the frame does it; whether the framework's vocabulary has such an object is the named next step.
5. *Inversion.* The Lattice axiom has proper rotations only, so the odd term `ε·T` is allowed by covariance; it is blindness that removes it.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T1(d) is at first order in the strain and for uniform rates; with a rate field the coupled equations require a new derivation; block 54 provides no exact universal packet-force law. T2 is at first order in the rotation and the strain (finite-strain rational-point checks are deferred author evidence, not an all-orders proof). T3 through second order. The relation between the walk's `B` and the frame's strain is used at first order.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice, its bonds and proper rotations (no inversion); the Qubit axiom's one-site algebra, no possibility privileged; the absences that motivate the clauses | yes (premise) |
| block 63 (open PR #8593) | the bond current, the relabelling's deformation, its divergence-free property | yes (restated) |
| block 60 (open PR #8590) | the ledger linear in the rates; the member; `β = a/(2(ap − b))` | yes (restated) |
| block 62 (open PR #8592) | the frame; a uniform rotation of the coin axes is unseen, a varying one is not a symmetry | yes (restated) |
| blocks 54, 59, 61 (open PRs #8570, #8581, #8591) | the walk; the exponent; three lengths | restated or placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "curls blind to relabellings; strain sourced by the bond current; field equations divergence-free; blindness to the coin axes leaves volume and curvature; `β = 1`; a blind field energy needs a blind content" | executed: nine curls of a rational strain on a `5×4×3` torus under a rational relabelling; hermiticity of `H[B]` and the derivative in one bond's strain on a `5³` torus | executed: the divergence of the field equations of a weighted sum of squared curls at every site, each coin axis | executed: the six-number family under a varying rotation, three rotation and nine strain functions: all coefficient conditions and their solution | executed: the blind density against `√g R` through second order, nine functions; variational derivatives in the antisymmetric strain for the blind member and for `c_1` alone; `β` on the isotropic frame; the torque of an exactly stationary state at all 64 sites of a `4³` torus | T1 every strain, relabelling, state and function of the curls; T2–T4 continuum identities to the orders stated, leading order in the wave vector on the lattice; T5 every state and every field energy blind to the rotation of a site's bonds, the violation for the stated state; strains, the coupling, blindness, `K`, `c_0 = 0`, kinetic terms not derived |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. `kinetic_isotropy_primitive` concerns a kinetic form of the repository and is not invoked for the blindness. Nothing is proposed for registration.

### N7 — Strongest objections
Divergence matching is not a static existence proof. A coefficient null space in a chosen continuum ansatz is not a classification of all lattice field energies. The conditional lattice torque obstruction must not be inferred from a continuum total-divergence identity; its stronger exact lattice premise is explicitly supplied. The conformal curvature sign is corrected in T3(c).

### N8 — Cross-cycle echo
Block 53: the first-order rate form follows under normalized differentiability and covariance, with a separately selected nonlinear completion. Block 55: a supplied variational model defines its sources; conservation alone does not force it. Block 59: `β` free. Block 60: `β = 1` for a declared member. Block 62: a uniform rotation of the coin axes is unseen by the walker. Block 63: the walk keeps its books on bonds. Here: the specified nonzero locally invariant continuum ansatz has beta=1 under its nondegeneracy conditions; a matching exact lattice theory is not constructed.

## Falsifiers

- A strain and relabelling that change a curl; a state for which `∂⟨H[B]⟩/∂B` is not the bond current; a function of the curls whose field equations have a divergence.
- A density of the family, other than the volume and `D*`, unchanged point by point by a varying rotation of the coin axes at first order.
- A strain for which `D* + √g R ≠ 0` at second order.
- A member with `4c_1 + 2c_2 + 4c_3 ≠ c_4` whose exponent is one.
- Failure of the explicit stationary-state torque counterexample. Other stationary states can satisfy the condition and are not falsifiers.

## Boundaries and non-claims

That bonds carry strains with the relabelling's second-neighbour coupling is supplied (block 63 named the fork). The blindness is supplied and is not a symmetry of the walk. `K`, `c_0 = 0` and every kinetic term are outside this note; so is the consistency of the static equations with a rate field and beyond first order in the strain. T2 to T4 are continuum identities; on the lattice they hold at leading order in the wave vector, and no exactly rotation-blind lattice member is exhibited. T5 is a conditional obstruction for the specified fixed source; no self-consistent no-solution theorem for every state and no invariant walk is constructed here. The comparator is quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom (proper rotations, no inversion), the Qubit axiom's one-site algebra, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 59–63 (PRs #8570, #8581, #8590, #8591, #8592, #8593, open): restated or placed.
- Named standard imports at definition level: commuting differences on a lattice; summation by parts; the expansion of an inverse matrix and of a determinant; the scalar curvature of a metric from its connection; variational derivatives; the solution of linear conditions on coefficients.
- Reference only: Weitzenböck; Einstein (1928–1930); Møller; Hayashi and Shirafuji; Cho; Cartan; Weyl; Vermeil; Lovelock; Wegner; Wilson.

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8570](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8581](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8590](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8591](ADMISSIBILITY_RULE_THREE_LENGTHS_PER_SITE_A_BODY_AT_REST_STRETCHES_THEM_ALIKE_HOP_ENERGY_DRIVES_WHOLE_COLUMNS_AND_THE_DELAYS_SPEED_DEPENDS_ON_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8592](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8593](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

Original author reports remain at PR #8595 head `e5688665736b60adf84e9eb84276e8c4169c2a17`, branch `physics-loop/admissibility-induced-law-block64-bond-strains-and-plaquette-curls-blindness-to-the-coins-axes-forces-the-curvature-member-20260921`. Landing review narrows existence and uniqueness quantifiers, corrects the conformal sign, separates continuum and exact lattice invariance, and adds a counterexample to universal vanishing of uniform bond torque. Auxiliary content remains deferred; no audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_2026_09_21.py
```

The fresh cache records the executed check count.
