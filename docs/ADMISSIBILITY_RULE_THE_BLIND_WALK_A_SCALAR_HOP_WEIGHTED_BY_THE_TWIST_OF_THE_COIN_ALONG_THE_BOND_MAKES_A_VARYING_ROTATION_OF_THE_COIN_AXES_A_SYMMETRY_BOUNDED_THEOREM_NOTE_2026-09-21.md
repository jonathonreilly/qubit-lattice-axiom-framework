---
claim_id: admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clause of block 54 (open PR #8570; not adopted): amplitudes on Z^3 with the site's qubit as coin and the generator H = sum_a sigma_a S_a, S_a = (T_a - T_a^dagger)/(2i); with reference to block 62 (open PR #8592: a frame for the coin; a UNIFORM rotation of the coin axes is unseen), block 63 (open PR #8593: the torque identity) and block 64 (open PR #8595, T5: a field energy that does not see the coin's axes needs a content that does not see them either). (T1) For every real theta(x) on the sites, -(i/2)[theta.sigma, H] = (1/2) sum_j {(theta x e_j).sigma, S_j} + (1/2) sum_a C_a[d_a theta_a], where C_a[v] is the symmetric hop along a weighted by the bond function v and d_a theta_a = theta_a(x + e_a) - theta_a(x): a rotation of the coin axes that varies from site to site acts on the walk, at first order, as a rotation of the frame at every site (nearest-neighbour) PLUS a coin-independent symmetric hop on every bond weighted by the TWIST of the coin along it, the change along the bond of the rotation about the bond's own axis; the hop vanishes for a uniform rotation and for a rotation without twist. (T2) With a rotation vartheta(x) at every site coupled as H[vartheta] = H + (1/2) sum_j {(vartheta x e_j).sigma, S_j} + (1/2) sum_a C_a[d_a vartheta_a], the first-order change of the walk under psi -> exp(-i theta.sigma/2) psi is exactly that of vartheta -> vartheta + theta; H[vartheta] is hermitian and nearest-neighbour; without the scalar hop this fails at first order. (T3) d<H[vartheta]>/d vartheta_c(x) at vartheta = 0 equals (1/2) d(psi^dagger sigma_c psi)(x)/dt for every state (it is block 63 T5's combination, sum eps_cad Theta_d^a - (1/2)[b_c(x) - b_c(x - e_c)]): zero at every site on stationary states; without the hop the response is sum eps_cad Theta_d^a, non-zero at every sampled site of the exactly stationary state of the 4x4x4 torus. So a field energy that does not depend on vartheta is consistent with this content. (T4) For a frame 1 + strain the inversion-odd scalar eps.T of the co-frame is 2 eps^jkl d_k B_jl at first order: zero for every symmetric strain and -4 div vartheta for the rotation of T1; at long wavelength the scalar hop is (1/2) div vartheta = -(1/8) eps.T: the scalar that blindness removed from the FIELD's energy (block 64 T2, c5 = 0) is the term the CONTENT needs; it is odd under inversion, which the Lattice axiom does not include. EXECUTED, NOT CLAIMED: for finite rotations exp(-i s theta.sigma/2) on a 4x3x3 torus, U H U^dagger - H[s theta] is 1.86 s^2 with the hop and 1.10 s without it; the spectrum of H[vartheta] moves by 2.03 s^2 with the hop and 0.6 s without; on a numerically found stationary state of a 6x4x4 torus the response is 3e-17 with the hop and up to 5.6e-3 without. NOT claimed: that sites carry a rotation field or that the walk has the scalar hop; a walk blind beyond first order or around a frame that is not the identity (that needs a rotation carried along each bond, not constructed); that block 64 T5's torque, which belongs to a rotation of a site's BONDS and not of its coin axes, vanishes; how the six symmetric numbers on the bonds and the three rotations on the sites fit in one set of variables; any statistical statement; any gravitational statement; any adoption."
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

Block 64 (open PR #8595) derived block 60's curvature member — and the full bending of rays — from two supplied properties: a field energy counted per local tick, and *blindness* to the orientation of the coin's axes. It also named the cost: a field that ignores the coin's axes needs a walker that ignores them too, and block 54's walker does not. This note asks what the walker lacks.

1. **What turning the coin does.** Turn the coin's axes by a small angle that varies from site to site. The walk changes in two ways, exactly. First, the frame at every site rotates — the obvious part. Second, every bond acquires a small *coin-independent* hop, weighted by the **twist**: how much the rotation about that bond's own axis changes along the bond. A uniform turn has no twist; neither has a turn about axis 1 that varies only across axis 1 (T1).
2. **The blind walk.** So give every site a rotation `ϑ(x)` and couple it with *both* terms. Then turning the coin is the same, at first order, as shifting `ϑ`: the walk cannot tell. The extra term is hermitian and reaches nearest neighbours only. Without it the walk can tell, at first order (T2).
3. **No torque.** The response of the blind walk to `ϑ` at a site is half the rate of change of the coin's own density there — block 63's torque identity, read as a balance law. It vanishes at every site for anything stationary. The content then asks nothing of `ϑ`, and a field energy that does not see `ϑ` is consistent with it. Without the hop the torque is there at every site (T3).
4. **What the hop is.** At long wavelength it is a potential, `½ div ϑ`, and that is minus one eighth of the inversion-odd scalar of the frame's curl — the very term that blindness *removed* from the field's energy in block 64. The walker may carry it because the lattice's symmetry has proper rotations only (T4).

In plain terms: if you turn the walker's coin a little differently at each site, the walker notices in one small way beyond the obvious one — it feels the *twist* of the coin along each bond, as a tiny extra push to hop that does not care which way the coin points. Put that push into the walker's rule and it no longer notices anything: turning the coin becomes pure bookkeeping, the torque that block 64 found disappears for everything stationary, and a field whose energy ignores the coin's axes is no longer at odds with the walker. The price is one more supplied term, nearest-neighbour, first order.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 64 (PR #8595), next_trace_action: 'a walk that does not see a varying rotation of its coin axes (what must be added to block 54's generator, and whether the framework's vocabulary has it), since T5 makes the blind member inconsistent with the walk as it stands'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "one set of variables carrying both exact structures: the symmetric six on the bonds (block 63/64: relabellings, second-neighbour coupling) and the rotation three on the sites (this note: coin rotations, nearest-neighbour), and whether block 64 T5's bond torque is then absorbed; a walk blind beyond first order (a rotation carried along each bond); the kinetic term under the two blindness demands; the owner's decision whether the walk has the scalar hop"
conditional_surface_status: "T1 exact operator identity for every rotation field and state; T2, T3 exact at first order in the rotation around the identity frame, for every state; their consequence exact for every stationary state; T4 exact continuum identity at first order in the strain"
hypothetical_axiom_status: "block 54's clause (amplitudes with the qubit as coin; the walk); a rotation field on the sites with the coupling of T2; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (sites, bonds, translations, *proper* rotations — no inversion), the Qubit axiom's one-site algebra with no possibility privileged, and the memo's silence on amplitude dynamics. Block 54 (open PR) supplies the walk.

- **Walk.** `H = Σ_a σ_a S_a`, `S_a = (T_a − T_a†)/(2i)`. **Differences** `(d_a f)(x) = f(x + e_a) − f(x)`, on the bond from `x` along `a`. **Symmetric hop** `(C_a[v]ψ)(x) = ½[v(x)ψ(x + e_a) + v(x − e_a)ψ(x − e_a)]` for a bond function `v`.
- **Rotation of the coin axes.** `ψ(x) → U(x)ψ(x)`, `U = exp(−iθ(x)·σ/2)`; to first order `H → H − (i/2)[θ·σ, H]`.
- **Rotation of the frame at a site.** In block 62's coupling `½Σ_j{E^j·σ, S_j}` the coin vector of bond direction `j` changes by `θ × e_j`.
- **The blind walk.** `H[ϑ] = H + ½Σ_j{(ϑ × e_j)·σ, S_j} + ½Σ_a C_a[d_aϑ_a]`. **Twist** along the bond from `x` in direction `a`: `(d_aϑ_a)(x)`.
- **Site response and bond density** (block 63): `Θ_a^j(x) = Re ψ†(x)σ_a(S_jψ)(x)`, `b_c(x) = Re ψ†(x)ψ(x + e_c)`.
- **Inversion-odd scalar** (block 64): `ε·T = ε^{jkl}T^j_{kl}`, `T` the curl of the co-frame.

That a two-component amplitude in a frame needs a connection to be blind to local rotations of the frame, and that in three dimensions with a two-component coin the connection's hermitian contribution reduces to a scalar potential built from the totally antisymmetric part of the frame's curl, is the theory of Weyl and of Fock and Ivanenko; the torque identity as the balance law of the local rotation is the argument of Belinfante and Rosenfeld. That a local symmetry is kept on a lattice by variables carried along the bonds is Wilson's. None is used as authority.

## Prior art and what is new

Classical in kind. New: the exact lattice form of what a varying rotation of the coin axes does to the framework's supplied walk — a site rotation of the frame plus a *scalar hop weighted by the twist* — and that this single nearest-neighbour term makes the walk blind at first order; that block 63's torque identity is precisely the balance law which then makes the response vanish on stationary states; and that the term is the inversion-odd scalar block 64's blindness excluded from the field's energy. Together with block 64 it says what the blindness costs in full: one supplied property of the field's energy and one supplied nearest-neighbour term in the walker's rule. No gravitational claim is made.

## Exact target and obligation graph

Target: what the walk lacks in order not to see a varying rotation of its coin axes. Obligations: (O1) the exact first-order action of such a rotation; (O2) a walk that is blind to it; (O3) the content's response; (O4) what the added term is. T1–T4 discharge them.

## Theorem T1 — what turning the coin does

*Statement.* For every real `θ(x)`: `−(i/2)[θ·σ, H] = ½Σ_j{(θ × e_j)·σ, S_j} + ½Σ_a C_a[d_aθ_a]`. The second term vanishes iff `d_aθ_a = 0` on every bond: for uniform `θ`, and for every `θ` whose component along each axis does not change along that axis.

*Proof.* `(θ·σ)σ_a = θ_a + i(θ × e_a)·σ` and `σ_a(θ·σ) = θ_a − i(θ × e_a)·σ`. So `[θ·σ, σ_aS_a] = θ_a S_a − S_a θ_a + i{(θ × e_a)·σ, S_a}` with `θ` a multiplication operator. The anticommutator term, times `−i/2`, is the rotation of the frame. `[θ_a, S_a]ψ(x) = (1/(2i))[(θ_a(x) − θ_a(x + e_a))ψ(x + e_a) − (θ_a(x) − θ_a(x − e_a))ψ(x − e_a)] = −(1/i) C_a[d_aθ_a]ψ(x)`, and `−(i/2)·(−1/i) = ½`. ∎

The twist is the one thing a varying rotation does that a rotation of the frame does not account for; it is first order in the rotation and first order in its change along the bond.

## Theorem T2 — the blind walk

*Statement.* (a) `H[ϑ + θ] − H[ϑ] = −(i/2)[θ·σ, H]` for all `ϑ`, `θ`: the first-order change of the walk under a rotation of the coin is that of `ϑ → ϑ + θ`. (b) `H[ϑ]` is hermitian and couples nearest neighbours only. (c) With the scalar hop left out, (a) fails whenever some `d_aθ_a ≠ 0`.

*Proof.* `H[ϑ]` is linear in `ϑ`, so (a) is T1. (b) Anticommutators and symmetric hops of hermitian operators with real weights; one shift per term. (c) T1. ∎

This is blindness at first order around the identity frame: `U H[ϑ] U† = H[ϑ + θ]` up to terms of second order in `(θ, ϑ)`. Beyond that a rotation must be carried along each bond (a product of the two ends' rotations does not reduce to a site term and a scalar hop); that is not constructed here.

## Theorem T3 — no torque

*Statement.* For every state, `∂⟨H[ϑ]⟩/∂ϑ_c(x)|_{ϑ=0} = ½ d(ψ†σ_cψ)(x)/dt = Σ_{a,d} ε_{cad}Θ_d^a(x) − ½[b_c(x) − b_c(x − e_c)]`. It vanishes at every site if `ψ` is stationary. Without the scalar hop the response is `Σ ε_{cad}Θ_d^a(x)`, which does not.

*Proof.* By T2(a) the derivative is `⟨−(i/2)[σ_cP_x, H]⟩ = ½ d⟨σ_cP_x⟩/dt`, `P_x` the projector on the site; the explicit form is block 63 T5. For a stationary state every expectation is constant. The second statement: runner D2, on the exactly stationary state of block 63. ∎

Block 63 read its identity as "the antisymmetric part of the site response is a pure divergence on stationary states". Here the divergence is recognised as the response of the scalar hop, and the sum of the two as zero.

## Theorem T4 — what the hop is

*Statement.* For a co-frame `1 + B`, at first order `ε·T = 2ε^{jkl}∂_kB_{jl}`: zero for symmetric `B`; for the co-frame of the rotation of T1 (`B = −(`frame's strain`)ᵀ`, frame's strain `(ϑ × e_j)_d`) it is `−4 div ϑ`. At long wavelength `½Σ_a C_a[d_aϑ_a] → ½ div ϑ = −⅛ ε·T`.

*Proof.* Expansion (runner E1); `C_a[v] → v cos k_a → v`. ∎

Block 64 T2 found `c_5 = 0`: a field energy that is blind cannot contain `ε·T`. The same scalar, with the coefficient `−⅛`, is what the content must contain to be blind. It changes sign under inversion of the lattice; block 54 already noted that inversion is an *added* symmetry, not one of the Lattice axiom's.

## Executed (supervisor control and refuting pass; floating point; evidence, not proof)

`specs/supervisor_control_block65_refuter.py`, dense matrices. W1: *finite* rotations `exp(−isθ·σ/2)` with a random `θ` on a `4 × 3 × 3` torus: `|U H U† − H[sθ]|` is `1.84 s², 1.86 s², 1.87 s²` for `s = 0.2, 0.1, 0.05` with the hop, and `1.08 s, 1.10 s, 1.11 s` without. W2: the largest shift of an eigenvalue of `H[ϑ]` from `H`'s is `2.03 s²` with the hop (a change of coin basis at first order) and `0.66 s, 0.60 s` without. W3: a random vector in the 16-fold eigenspace of energy 1 on a `6 × 4 × 4` torus: the response to a rotation at 42 sampled sites and axes is below `4×10⁻¹⁷` with the hop; without it, up to `5.6×10⁻³`, above `10⁻⁶` in 28 of the 42 (in this eigenspace some sites and axes have no torque by accident). W4: for a plane wave in a slowly varying twist the hop's local energy is `½(∂_aϑ_a) cos k_a` to `1.5×10⁻⁵` where it is of size `5×10⁻³`.

## No-Go Discipline Gate

The note's negative sentences: without the scalar hop the walk sees a varying rotation of its coin axes at first order; without it the torque does not vanish on stationary states.

### N1 — Routes by which the sentences could fail
1. *A different compensating term.* T1 is an identity: whatever makes the walk blind at first order must equal the scalar hop on every state.
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
Block 54: inversion is an added symmetry. Block 62: a uniform rotation of the coin axes is unseen. Block 63: the antisymmetric response is a pure divergence on stationary states. Block 64: a blind field energy cannot contain the inversion-odd scalar, and needs a blind content. Here: the content is blind iff it contains that scalar, as a hop weighted by the twist.

## Falsifiers

- A rotation field and state violating T1.
- A nearest-neighbour hermitian term, other than the scalar hop, that makes the walk blind at first order.
- A stationary state with a non-zero response to `ϑ` in the blind walk.

## Boundaries and non-claims

The rotation field and the scalar hop are supplied. Blindness is shown at first order around the identity frame with uniform rates; a walk blind beyond that is not constructed. Block 64 T5's bond torque is not removed. How the bonds' symmetric strain and the sites' rotation fit in one formulation, and what the field energy of blocks 60 to 64 is in those variables, is not examined. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom (proper rotations, no inversion), the Qubit axiom's one-site algebra, and the memo's silence on amplitude dynamics. Blocks 54, 62, 63, 64 (PRs #8570, #8592, #8593, #8595, open): restated or placed.
- Named standard imports at definition level: the product rule of the coin's three matrices; commutators with shifts; hermiticity of anticommutators; the derivative of an expectation under a unitary change; the antisymmetric symbol.
- Reference only: Weyl; Fock and Ivanenko; Belinfante; Rosenfeld; Wilson.

## Review record
Supervisor-run block, the thirteenth of the source-link direction and the ninth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the rotation field and the hop are supplied; the Lattice axiom's lack of inversion is what permits an inversion-odd term, and block 54 had already flagged inversion as added. A rigour lens: the supervisor's first expectation, from the continuum, was an on-site potential; the lattice computation gives a hop weighted by the twist, which becomes the potential only at long wavelength. The naive generalisation to a varying frame (weight `d_j(θ·E^j)`) was tested in scratch and failed, and the note claims first order around the identity frame only. The supervisor also checked what this does *not* do: block 64 T5's torque belongs to a rotation of the bonds, a different lattice deformation, and is not removed; the note says so in the claim scope, under N1 and under the Boundaries. A comparator lens: the connection of a two-component amplitude and its reduction to a scalar — under the Premises. A strategy lens: with block 64 this completes the account of what blindness costs. Control and refuting pass (`specs/supervisor_control_block65_refuter.py`, dense matrices, finite rotations): W1–W4 as reported under Executed; the first version of W3 reported the *smallest* bare response, which is zero by accident at some sites of that eigenspace, and was changed to the largest and a count. Mutation census: 9 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_2026_09_21.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
