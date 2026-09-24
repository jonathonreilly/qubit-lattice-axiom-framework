---
claim_id: admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the supplied identity-frame walk and time-independent real local coin rotations, the infinitesimal unitary commutator equals the stated site-frame rotation plus a coin-independent nearest-neighbour symmetric hop weighted by the axial rotation difference along each bond. Including both terms gives covariance to joint first order about the identity frame, not finite-rotation covariance of the truncated generator. At zero rotation-field background its fixed-state rotation derivative equals half the coin-density time derivative under the unperturbed walk and vanishes for its stationary states. This meets a necessary rotation equation only; it neither proves full static solvability nor removes the separate second-neighbour bond-strain torque. The long-wavelength leading scalar term is minus one eighth of the linearized coframe curl pseudoscalar under the stated conventions."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_2026_09_21.py
---

# The blind walk: a scalar hop weighted by the twist of the coin along the bond makes a varying rotation of the coin axes a symmetry

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact identities of block 54's supplied walk at first order in a rotation of the coin axes; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin; it reports what a rotation of the coin axes that varies from site to site does to the walk, exactly at first order, and the nearest-neighbour term that makes the walk blind to it; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

A local coin conjugation has an exact infinitesimal operator identity: a site-frame rotation plus a scalar symmetric hop proportional to the rotation difference along each bond. Adding both terms reproduces that conjugation to joint first order in the rotation fields about the identity frame.

At zero rotation background, the energy derivative is half the unperturbed coin-density time derivative. It vanishes for stationary states of the unperturbed H; this supplies a necessary equation when the field energy has no rotation dependence. It does not prove existence of a complete static solution, finite-rotation covariance, or vanishing response for stationary states at arbitrary nonzero background rotation.

The author's 2026-09-23 corrigendum is incorporated: this coin response is distinct from the second-neighbour bond-strain torque in the preceding note. That obstruction is not removed here. The continuum pseudoscalar comparison is a leading long-wavelength identity, not an exact on-site replacement for the lattice hop.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (sites, bonds, translations, *proper* rotations — no inversion), the Qubit axiom's one-site algebra with no possibility privileged, and the memo's silence on amplitude dynamics. Block 54 (open PR) supplies the walk.

- **Walk.** `H = Σ_a σ_a S_a`, `S_a = (T_a − T_a†)/(2i)`. **Differences** `(d_a f)(x) = f(x + e_a) − f(x)`, on the bond from `x` along `a`. **Symmetric hop** `(C_a[v]ψ)(x) = ½[v(x)ψ(x + e_a) + v(x − e_a)ψ(x − e_a)]` for a bond function `v`.
- **Domain.** Finite periodic lattices, or local infinite-lattice identities on finitely supported data; summed operator statements require suitable domains. Rotations are time independent. A time-dependent basis change adds its temporal connection term and is outside this note.
- **Rotation of the coin axes.** `ψ(x) → U(x)ψ(x)`, `U = exp(−iθ(x)·σ/2)`; to first order `H → H − (i/2)[θ·σ, H]`.
- **Rotation of the frame at a site.** In block 62's coupling `½Σ_j{E^j·σ, S_j}` the coin vector of bond direction `j` changes by `θ × e_j`.
- **The blind walk.** `H[ϑ] = H + ½Σ_j{(ϑ × e_j)·σ, S_j} + ½Σ_a C_a[d_aϑ_a]`. **Twist** along the bond from `x` in direction `a`: `(d_aϑ_a)(x)`.
- **Site response and bond density** (block 63): `Θ_a^j(x) = Re ψ†(x)σ_a(S_jψ)(x)`, `b_c(x) = Re ψ†(x)ψ(x + e_c)`.
- **Inversion-odd scalar** (block 64): `ε·T = ε^{jkl}T^j_{kl}`, `T` the curl of the co-frame.

That a two-component amplitude in a frame needs a connection to be blind to local rotations of the frame, and that in three dimensions with a two-component coin the connection's hermitian contribution reduces to a scalar potential built from the totally antisymmetric part of the frame's curl, is the theory of Weyl and of Fock and Ivanenko; the torque identity as the balance law of the local rotation is the argument of Belinfante and Rosenfeld. That a local symmetry is kept on a lattice by variables carried along the bonds is Wilson's. None is used as authority.

## Prior art and what is new

The bounded content is the exact first-order lattice commutator and its fixed-background response identity. It does not finish the separate strain-current coupling or derive these additional fields from the qubit axiom.

## Theorem T1 — what turning the coin does

*Statement.* For every real `θ(x)`: `−(i/2)[θ·σ, H] = ½Σ_j{(θ × e_j)·σ, S_j} + ½Σ_a C_a[d_aθ_a]`. On the infinite lattice or tori with at least three sites per axis, the second term vanishes as an operator iff `d_aθ_a = 0` on every bond; very small periodic lattices can alias the hops. In particular it vanishes for uniform `θ`, and for every `θ` whose component along each axis does not change along that axis.

*Proof.* `(θ·σ)σ_a = θ_a + i(θ × e_a)·σ` and `σ_a(θ·σ) = θ_a − i(θ × e_a)·σ`. So `[θ·σ, σ_aS_a] = θ_a S_a − S_a θ_a + i{(θ × e_a)·σ, S_a}` with `θ` a multiplication operator. The anticommutator term, times `−i/2`, is the rotation of the frame. `[θ_a, S_a]ψ(x) = (1/(2i))[(θ_a(x) − θ_a(x + e_a))ψ(x + e_a) − (θ_a(x) − θ_a(x − e_a))ψ(x − e_a)] = −(1/i) C_a[d_aθ_a]ψ(x)`, and `−(i/2)·(−1/i) = ½`. ∎

The twist is the one thing a varying rotation does that a rotation of the frame does not account for; it is first order in the rotation and first order in its change along the bond.

## Theorem T2 — the blind walk

*Statement.* (a) `H[ϑ + θ] − H[ϑ] = −(i/2)[θ·σ, H]` for all `ϑ`, `θ`: the first-order change of the walk under a rotation of the coin is that of `ϑ → ϑ + θ`. (b) `H[ϑ]` is hermitian and couples nearest neighbours only. (c) With the scalar hop left out, (a) fails whenever some `d_aθ_a ≠ 0`.

*Proof.* `H[ϑ]` is linear in `ϑ`, so (a) is T1. (b) Anticommutators and symmetric hops of hermitian operators with real weights; one shift per term. (c) T1. ∎

This is blindness at first order around the identity frame: `U H[ϑ] U† = H[ϑ + θ]` up to terms of second order in `(θ, ϑ)`. Beyond that a rotation must be carried along each bond (a product of the two ends' rotations does not reduce to a site term and a scalar hop); that is not constructed here.

## Theorem T3 — no torque

*Statement.* For every state, `∂⟨H[ϑ]⟩/∂ϑ_c(x)|_{ϑ=0} = ½ d(ψ†σ_cψ)(x)/dt = Σ_{a,d} ε_{cad}Θ_d^a(x) − ½[b_c(x) − b_c(x − e_c)]`. It vanishes at every site if psi is stationary under the unperturbed H. Without the scalar hop the response is `Σ ε_{cad}Θ_d^a(x)`, which need not vanish; special states can have zero response too.

*Proof.* By T2(a) the derivative is `⟨−(i/2)[σ_cP_x, H]⟩ = ½ d⟨σ_cP_x⟩/dt`, `P_x` the projector on the site; the explicit form is block 63 T5. For a stationary state every expectation is constant. The second statement: runner D2, on the exactly stationary state of block 63. ∎

Block 63 read its identity as "the antisymmetric part of the site response is a pure divergence on stationary states". Here the divergence is recognised as the response of the scalar hop, and the sum of the two as zero.

## Theorem T4 — what the hop is

*Statement.* For a co-frame `1 + B`, at first order `ε·T = 2ε^{jkl}∂_kB_{jl}`: zero for symmetric `B`; for the co-frame of the rotation of T1 (`B = −(`frame's strain`)ᵀ`, frame's strain `(ϑ × e_j)_d`) it is `−4 div ϑ`. At long wavelength `½Σ_a C_a[d_aϑ_a] → ½ div ϑ = −⅛ ε·T`.

*Proof.* Expansion (runner E1); `C_a[v] → v cos k_a → v`. ∎

Block 64 T2 found `c_5 = 0`: a field energy that is blind cannot contain `ε·T`. The same scalar, with the coefficient `−⅛`, is what the content must contain to be blind. It changes sign under inversion of the lattice; block 54 already noted that inversion is an *added* symmetry, not one of the Lattice axiom's.

## Historical experiments — deferred

Original finite-rotation dense-matrix, spectral and numerical stationary-state checks remain on the original branch. Their measured error scalings are not fresh canonical evidence. The exact runner checks the infinitesimal identities and specific stationary examples.

## No-Go Discipline Gate

The note's negative sentences: without the scalar hop the walk sees a varying rotation of its coin axes at first order; without it there are stationary states of the unperturbed walk with nonzero local rotation response; other states can have zero response.

### N1 — Routes by which the sentences could fail
1. *A different compensating term.* T1 is an identity: with the stated coin transformation and fixed site-frame rotation term, equality as an operator fixes the missing first-order contribution to the scalar hop. Other transformations, additional fields or higher-order terms are outside this uniqueness statement.
2. *A rotation of the bonds is not a rotation of the coin.* Block 64 T5 turned a site's three forward *bonds* (a strain, with second-neighbour coupling); its response `J_a^j(x) − J_j^a(x)` is not the response to turning the *coin* and is not removed by the hop. The two deformations agree at long wavelength only. Which lattice variables carry the symmetric six numbers (bonds, by blocks 63 and 64) and which the rotation three (sites, by this note), in one formulation, is the named next step.
3. *Beyond first order; frames away from the identity.* For a varying frame the first-order action of a coin rotation contains, besides a scalar hop weighted by `d_j(θ·E^j)`, a coin-dependent term of second order in the differences (the supervisor's scratch check of the naive generalisation failed, residual 2.1 on a field of size 5.8). Not constructed.
4. *Rates.* With `√w H √w` the identity is conjugated by `√w`, which commutes with `θ·σ`; T1–T3 go through with the hop's weight multiplied by `√(w_x w_y)`. Stated, not run.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
First order in the rotation; identity frame; uniform rates; the label's time. "Stationary" means a superposition of eigenstates of one energy.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its proper rotations (no inversion); the Qubit axiom's one-site algebra; the memo's silence on amplitude dynamics | yes (premise) |
| block 54 (open PR #8570) | the walk; inversion as an added symmetry | yes (restated) |
| block 63 (open PR #8593) | the torque identity; the exactly stationary state | yes (restated) |
| block 64 (open PR #8595) | the blindness of the field energy, its cost (T5), `c_5 = 0` | yes (restated) |
| block 62 (open PR #8592) | the frame; a uniform rotation is unseen | restated |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a varying coin rotation = frame rotation + scalar hop by the twist; the blind walk; no torque on stationary states; the hop is `−⅛ ε·T`" | executed: the operator identity at all 60 sites of a `5×4×3` torus; the hop's vanishing for a uniform rotation and for one without twist | executed: the change of `H[ϑ]` under a coin rotation against the shift of `ϑ`; hermiticity; reach; the derivative in one site's rotation against the coin density's rate of change | executed: `ε·T` at first order for a general strain, a symmetric strain and the rotation | executed: the exactly stationary state of the `4³` torus: response with and without the hop at 39 sampled sites and axes | T1 every rotation field and state; T2, T3 first order around the identity frame, every state, every stationary state; T4 continuum, first order; a walk blind beyond that, the rotation field and the hop themselves not derived |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "This is the spin connection of a two-component spinor, which everyone knows reduces to a scalar in three dimensions." Reply: yes, under the Premises. On the lattice it is not a potential but a *hop*, weighted by the twist, and T1 is its exact form for the supplied walk; and the point for the owner is the pairing with block 64 — the scalar the field may not contain is the scalar the content must. Second objection: "First order only." Reply: the ledger of blocks 60 to 64 is of second order, which is first order in the coupling; the note says what is missing beyond. Third objection: "You have not removed block 64's torque." Reply: correct, and N1.2 says why: that torque belongs to a rotation of the bonds, which on the lattice is a different deformation; what is shown is that the rotation of the *coin*, the transformation block 64's blindness is about, costs the content nothing once the hop is there.

### N8 — Cross-cycle echo
Block 54: inversion is an added symmetry. Block 62: a uniform rotation of the coin axes is unseen. Block 63: the antisymmetric response is a pure divergence on stationary states. Block 64: a blind field energy cannot contain the inversion-odd scalar, and needs a blind content. Here: the fixed first-order operator completion includes the twist-weighted scalar hop. Other couplings and higher-order completions are not classified.

## Falsifiers

- A rotation field and state violating T1.
- A different first-order Hermitian operator contribution satisfying the same infinitesimal commutator identity with the site-frame term and transformation held fixed.
- A stationary state of the unperturbed H with a nonzero rotation response at vartheta=0 in the stated linearized model.

## Boundaries and non-claims

The rotation field and the scalar hop are supplied. Blindness is shown at first order around the identity frame with uniform rates; a walk blind beyond that is not constructed. Block 64 T5's bond torque is not removed. How the bonds' symmetric strain and the sites' rotation fit in one formulation, and what the field energy of blocks 60 to 64 is in those variables, is not examined. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom (proper rotations, no inversion), the Qubit axiom's one-site algebra, and the memo's silence on amplitude dynamics. Blocks 54, 62, 63, 64 (PRs #8570, #8592, #8593, #8595, open): restated or placed.
- Named standard imports at definition level: the product rule of the coin's three matrices; commutators with shifts; hermiticity of anticommutators; the derivative of an expectation under a unitary change; the antisymmetric symbol.
- Reference only: Weyl; Fock and Ivanenko; Belinfante; Rosenfeld; Wilson.

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8570](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8592](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8593](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8595](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

Original author material, including the 2026-09-23 coin-versus-bond torque corrigendum, remains at PR #8596 head `fb37a985ba166358495f7878d06a41776f60744d`, branch `physics-loop/admissibility-induced-law-block65-the-blind-walk-a-scalar-hop-weighted-by-the-twist-of-the-coin-20260921`. Landing review retains that distinction, fixes the background and perturbative scope, and separates a necessary rotation equation from complete static existence. Auxiliary experiments are deferred; no audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_2026_09_21.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
