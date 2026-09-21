---
claim_id: admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 60, 62 and 63 (open PRs #8570, #8590, #8592, #8593; not adopted): block 54's walk H = sum_a sigma_a S_a with the qubit as coin; block 60's ledger linear in the rates, F = sum_x w_x D_x; block 63's bond current J_a^j and the deformation a relabelling generates. WIDENED by one supplied object: a STRAIN on every bond, B_a^j(x) on the bond from x along a (stretch for j = a, tilt for j != a), coupled as a relabelling's deformation is, H[B] = H + sum_aj sigma_a (1/2){C_a[B_a^j], S_j}; a relabelling xi of the sites shifts B_a^j by d_a xi_j. (T1; the lattice, exactly) the CURL F_ab^j = d_a B_b^j - d_b B_a^j on a plaquette is unchanged by every relabelling; H[B] is hermitian and d<H[B]>/dB_a^j(x) = J_a^j(x -> x + e_a) for every state; for ANY field energy that is a function of the curls the divergence over a of dF/dB_a^j vanishes identically; hence, at first order in the strain and for uniform rates, the static equations dF/dB = -J are consistent for every stationary state of the walk: the first item of block 62's bill is met exactly, at the price block 63 named (a coupling with second-neighbour reach). (T2; continuum, exact symbolic algebra) among densities with at most two derivatives built from a frame e = 1 + strain, D = c0 det e + c5 det e (eps.T) + det e [c1 T^j_ab T_j^ab + c2 T^j_ab T^ba_j + c3 V_b V^b] + c4 d_b(det e V^b), T = curl e, V_b = T^a_ab, those unchanged POINT BY POINT, to first order in the rotation and in a general strain, by a rotation of the coin axes that varies from place to place are exactly c5 = 0, (c1, c2, c3, c4) proportional to (1, 2, -4, -8), c0 free. Point by point is what a ledger linear in the rates requires, since every rate multiplies its own site's density and the rates are arbitrary. (T3) D* = det e [T1/4 + T2/2 - T3] - 2 d_b(det e V^b) equals MINUS (volume density) x (scalar curvature) of g = e^T e, point by point, through second order in a general strain; the second-order part of D* has no variational derivative with respect to the antisymmetric strain. With c4 = -2K, c0 = 0, the blind density is block 60's member. (T4) On the frame l x identity, l = exp(lam), the family has first order -2 c4 Lap lam and second order (4c1 + 2c2 + 4c3)|grad lam|^2: in block 60's form a = -2 c4, ap - b = -(4c1 + 2c2 + 4c3), so block 59's exponent is beta = c4/(4c1 + 2c2 + 4c3): a free number for a member that sees the coin axes (c4/(4c1) for c1 alone, whose antisymmetric strain is a field), and ONE for the blind member: the bending of a ray is twice the fall of a slow body WITHOUT declaring the member. (T5; the lattice, exactly; what blindness costs) a blind field energy gives a rotation of a site's three forward bonds, dB_a^j(x) = om_aj(x), no field equation; stationarity then asks the content for J_a^j(x) - J_j^a(x) = 0 at every site, and an exactly stationary superposition of block 54's walk violates it at all 64 sites of a 4x4x4 torus for each rotation axis: a field energy that does not see the coin's axes has static solutions only for a content that does not see them either, which the walk is not. EXECUTED, NOT CLAIMED: with exact frames and polynomial strain and rotation fields (all orders in the strain) the null space of the blindness conditions at eight rational points is spanned by the volume and (c1, c2, c3, c4) = (-1/8, -1/4, 1/2, 1), and D* + sqrt(g) R vanishes exactly at rational points for a finite strain; a relabelling moves the spectrum of H[B] at second order only (shift/s^2 = 1.333 for s = 0.04, 0.02, 0.01), a generic strain at first order. NOT claimed: that bonds carry strains; the second-neighbour coupling; that the field energy is linear in the rates; the blindness itself (a rotation of the coin axes that varies from site to site is NOT a symmetry of the walk: block 62, and T5 here); a walk that is blind; K; c0 = 0; kinetic terms; a unique lattice form of the contractions that mix the coin index with the bond index (T2 to T4 are statements at leading order in the wave vector); any statistical statement; any gravitational statement; any adoption."
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

Block 60 (open PR #8590) found that a field energy counted per tick of each local clock gives the full bending of rays — for one *declared* member, "rate × volume × curvature", with the power `p = 1` and the numbers `a = 4`, `b = 2` put in by hand. Block 62 (open PR #8592) found angles in the tilt of the coin's frame and a bill: the member needs the content's stress to balance. Block 63 (open PR #8593) itemised the bill: the walk conserves a current that lives on the *bonds*, generated by relabellings, with second-neighbour reach. This note puts the field where the walk keeps its books, and then asks what is left to declare.

**The variables.** Give every bond a *strain*: a small vector `B_a^j(x)` saying how the bond from `x` along `a` is stretched (`j = a`) or tilted (`j ≠ a`), coupled to the walk exactly as a relabelling's deformation is (block 63 T2). A relabelling of the sites by `ξ` shifts the strain by the difference of `ξ` across the bond. The mismatch of the strains around a plaquette — their *curl* — is what a relabelling cannot change.

1. **The lattice, exactly.** Curls are blind to relabellings. The strain is sourced by block 63's conserved bond current. And the field equations of *any* function of the curls are divergence-free identically. So at first order the static equations are consistent for every stationary state of the walk: the first item of block 62's bill is met exactly, with no tuning (T1).
2. **What is left to declare: almost nothing.** Take every density with at most two derivatives that can be built from the strains' curls: six numbers. Demand that it not see the orientation of the coin's axes — *point by point*, because in a ledger linear in the rates every clock multiplies its own site's density and the clocks are arbitrary. Four of the six are fixed: what survives is the volume and **one** combination of the curls, each with its own coefficient (T2).
3. **That combination is the curvature.** It equals minus volume × scalar curvature of the metric the walker sees, point by point; the part of the strain that rotates the coin's axes drops out. With the volume term absent (so that the unstretched lattice is a solution) it is block 60's member, with `K` its one number (T3).
4. **So `β = 1` is forced.** On the whole family block 59's exponent is `β = c_4/(4c_1 + 2c_2 + 4c_3)`, anything one likes; on the blind member it is 1. A member that *does* see the coin's axes — one field of curls per coin axis is the plainest — has a free `β` and three more fields that no walker sees (T4).

5. **What blindness costs.** A field energy that does not see the coin's axes gives the rotation of a site's bonds no equation of its own. The walk *does* see that rotation: its response is a torque, `J_a^j(x) − J_j^a(x)`, and for an exactly stationary state it is non-zero at every site. So the blind member has no static solution for the walk as it stands: **a blind field energy needs a blind content.** This is the second item of block 62's bill, now exact (T5).

In plain terms: put a little arrow on every bond saying where the bond really points, and measure how the arrows fail to close around each square of the lattice. That failure is the only thing a relabelling cannot hide, and it is sourced by exactly what the walker conserves. Now count the field's energy per tick of each local clock, and insist that it not care which way the coin's three axes happen to be set at each site — the walker in a uniform frame does not care either. Then the energy *is* the curvature of the stretched lattice, and light bends twice as much as slow bodies fall. Block 60's member no longer has to be declared; what has to be supplied is the blindness — and it has to be supplied twice. The walker as it stands *can* feel its coin's axes being turned from site to site: it pushes back with a torque. A field that ignores that turning then has no answer to the push. Either the walker is changed so that it cannot feel it either, or the field's energy must see it, and then the bending is a free number again.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 63 (PR #8593), next_trace_action: 'a member placed to match the bond current (displacements on sites, the strain of a bond on the bond) and its travelling disturbances'; block 60 (PR #8590), Boundaries: 'the members are declared; K, p, s and the sign of c_k are not derived'; ai/probes task 'what-fixes-the-powers-and-the-kinetic-sign'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a walk that does not see a varying rotation of its coin axes (what must be added to block 54's generator, and whether the framework's vocabulary has it), since T5 makes the blind member inconsistent with the walk as it stands; the same blindness applied to the kinetic term (does it fix the second kinetic number and the sign, as it fixes the potential?); a lattice form of the mixed contractions and how far the blindness holds beyond leading order in the wave vector; whether blindness to a varying rotation of the coin axes can be had on the content's side (block 62 N1.2, block 63 T5); the owner's decision whether the field's energy sees the coin's axes"
conditional_surface_status: "T1 exact for every strain, relabelling, state and function of the curls, the consistency statement at first order in the strain and for uniform rates; T2 exact to first order in the rotation and in a general strain; T3 exact through second order in a general strain; T4 exact on the isotropic frame through second order; T5 exact for the stated stationary state, the mechanism for every field energy that does not depend on the rotation of a site's forward bonds"
hypothetical_axiom_status: "blocks 54, 60, 62, 63's clauses; a strain on every bond with the relabelling's coupling; a field energy linear in the rates built from the curls with at most two differences; blindness, point by point, to the orientation of the coin's axes; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (sites, bonds, translations, proper rotations), the Qubit axiom's one-site algebra with no possibility privileged, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 60, 62, 63 (open PRs) supply the walk, the ledger linear in the rates, the frame and what the walk conserves.

- **Strain.** `B_a^j(x)`, real, on the bond from `x` along `a`. **Coupling** `H[B] = H + Σ_{a,j} σ_a ½{C_a[B_a^j], S_j}`, `C_a[v]` the symmetric hop along `a` weighted by the bond function `v` (block 63). **Relabelling** `B_a^j → B_a^j + (d_aξ_j)`, `ξ` on the sites.
- **Curl** `F_ab^j(x) = (d_aB_b^j)(x) − (d_bB_a^j)(x)` on the plaquette at `x` spanned by `a < b`.
- **Frame and its curl (continuum).** `e^j_a = δ^j_a +` strain; `T^j_ab = ∂_a e^j_b − ∂_b e^j_a`; bond indices are turned into coin indices with the inverse frame; `V_b = T^a_ab`; `T_1 = T^j_{kl}T^j_{kl}`, `T_2 = T^j_{kl}T^l_{kj}`, `T_3 = V_lV_l`; `ε·T = ε^{jkl}T^j_{kl}` (odd under inversion, which the Lattice axiom does not include). To first order the frame's strain is minus the walk's `B` (the walk's coupling is to the inverse frame, block 62).
- **The family.** `D = c_0 det e + c_5 det e (ε·T) + det e [c_1T_1 + c_2T_2 + c_3T_3] + c_4 ∂_b(det e V^b)`: every scalar density that is covariant under relabellings, built from the frame and its curl, with at most two derivatives in each term. **Ledger** `F = Σ_x w_x D_x` (block 60).
- **Rotation of the coin axes.** `e → R(x)e`, `R(x)` a rotation acting on the coin index.

A frame with the curl as its field strength and no connection is the teleparallel description of Weitzenböck and of Einstein's papers of 1928 to 1930; the three quadratic invariants and the one-parameter family of theories they give are those of Hayashi and Shirafuji; that one combination differs from the scalar curvature by a divergence, and is the only one blind to local rotations of the frame, is the basis of the teleparallel equivalent of the comparator theory (Møller; Cho). That a Lagrangian is blind to local rotations only up to a divergence, while a Lagrangian multiplied by a position-dependent factor needs blindness point by point, is the known reason the lapse spoils the local symmetry of the torsion scalar alone. That the scalar curvature is the only density with two derivatives built from a metric is the theorem of Cartan, Weyl and Vermeil, extended by Lovelock. Lattice fields on bonds with invariants on plaquettes are Wegner's and Wilson's. None is used as authority; the comparator is quoted as a comparator.

## Prior art and what is new

Every piece is classical. What is new is the statement inside the framework's vocabulary: that the walk's exactly conserved current (block 63) picks the variables — strains on bonds, displacements on sites — for which the lattice keeps a relabelling symmetry exactly and the static equations are consistent identically; and that block 60's premise, a field energy counted per local tick, *strengthens* the usual blindness-up-to-a-divergence into blindness point by point, which then fixes the member: the curvature member of blocks 60 to 62 follows from two supplied properties instead of being declared, and with it `β = 1`. The note also says what the blindness is not — a symmetry of the walk — and makes that exact: the walk's stationary states exert a torque on a rotation of a site's bonds, so a blind field energy has no static solution with this content (T5). No gravitational claim is made.

## Exact target and obligation graph

Target: a field placed where the walk keeps its books, and what remains to declare about its energy. Obligations: (O1) the lattice structure and the consistency of the static equations; (O2) which densities are blind to the coin's axes; (O3) what the blind density is; (O4) what blindness buys; (O5) what it costs. T1–T5 discharge them.

## Theorem T1 — the lattice, exactly

*Statement.* (a) `F_ab^j[B + dξ] = F_ab^j[B]` for every `B` and `ξ`. (b) `H[B]` is hermitian, and `∂⟨H[B]⟩/∂B_a^j(x) = J_a^j(x → x + e_a)` for every state. (c) For every function `𝓕` of the curls, `Σ_a [∂𝓕/∂B_a^j(x) − ∂𝓕/∂B_a^j(x − e_a)] = 0` at every site, for each `j`. (d) Hence at first order in the strain, with uniform rates, the static equations `∂𝓕/∂B_a^j = −J_a^j` have a consistent divergence for every stationary state of the walk.

*Proof.* (a) `d_a d_b ξ = d_b d_a ξ`. (b) `C_a[v]` and `S_j` are hermitian and the anticommutator of hermitian operators is hermitian; `⟨H[B]⟩` is linear in `B` and block 63 T2(b) identifies the coefficient. (c) `𝓕[B + dξ] = 𝓕[B]` for all `ξ`; differentiate in `ξ_j(x)` and sum by parts. (d) Block 63 T2(c): `J` is divergence-free on stationary states. ∎

On a closed lattice the uniform part of the current is not balanced by any curl; that is block 60 T2(c)'s statement that a closed lattice with content is not static.

## Theorem T2 — blindness to the coin's axes fixes the density

*Statement.* Let `e = (1 + ηΩ(x))(1 + εB(x))` with `Ω` antisymmetric. The part of `D` of first order in `η` vanishes identically at orders `ε⁰` and `ε¹`, for all `Ω` and `B`, iff `c_5 = 0`, `c_1 = −c_4/8`, `c_2 = −c_4/4`, `c_3 = c_4/2`. `c_0` is unconstrained.

*Proof.* At order `ε⁰` the change of `D` is `c_5` times `4 div ω` (`ω` the axial vector of `Ω`) — the divergence term contributes `∂_a∂_bΩ_{ab} = 0`. At order `ε¹` the change is a polynomial in the derivatives of `B` and `Ω` whose coefficients are, up to sign, `2c_1 − c_2`, `2c_1 + c_2 + c_3`, `2c_3 − c_4`, `4c_2 + c_4` and `4c_5` (runner C1). `det e` is unchanged by a rotation. ∎

*Why point by point.* `F = Σ_x w_x D_x`. If `D` changed by a divergence, `F` would change by minus the sum of that divergence's argument against the differences of the rates, which are arbitrary (block 60 T2: every rate is a multiplier). The weaker demand — unchanged up to a total divergence, tested by the vanishing of all variational derivatives of the first-order change — fixes `c_5 = 0` and `c_1 : c_2 : c_3 = 1 : 2 : −4` and leaves `c_4` free (runner C2).

## Theorem T3 — the blind density is the curvature

*Statement.* (a) `D* = det e [¼T_1 + ½T_2 − T_3] − 2∂_b(det e V^b) = −√g R[g]`, `g = eᵀe`, point by point, through second order in a general strain. (b) Writing the strain as symmetric plus antisymmetric, the second-order part of `D*` has zero variational derivative with respect to the antisymmetric part. (c) With `c_4 = −2K` and `c_0 = 0`, `F = Σ_x w_x K D*_x` is block 60's member; on `e = ℓ·1` it is `−K ℓ(4Δλ + 2|∇λ|²)`, and on `diag(ℓ_j)` block 61's.

*Proof.* (a) Direct expansion of both sides (runner D1; nine strain functions). (b) By (a) the density depends on the strain through `g` alone, and `g` contains the antisymmetric part only at second order, where it enters the first-order curvature — a double divergence (runner D2). (c) From (a) and blocks 60, 61. ∎

`c_0 = 0` is the requirement that the unstretched lattice with uniform rates and no content be a solution (as `f(0) = 0` was in block 55 T4).

## Theorem T4 — what blindness buys

*Statement.* On `e = ℓ·1`, `ℓ = e^λ`: `D = −2c_4 Δλ·ε + (4c_1 + 2c_2 + 4c_3)|∇λ|²·ε² + …` up to a second-order total derivative. In block 60 T3's notation `a = −2c_4`, `ap − b = −(4c_1 + 2c_2 + 4c_3)`, and block 59's exponent is `β = c_4/(4c_1 + 2c_2 + 4c_3)`. For `c_2 = c_3 = 0`: `β = c_4/(4c_1)`, and the second-order part of `det e·T_1` has a non-zero variational derivative with respect to the antisymmetric strain. For the blind member `β = 1`.

*Proof.* Expansion (runner E1, E2) and block 60 T3(b). ∎

So the family without blindness is block 59's situation again — a free exponent — with three additional fields that no walker in a uniform frame sees. With blindness the count of declared objects in the potential part of the field energy falls from `(a, b, p)` to `K`.

## Theorem T5 — what blindness costs

*Statement.* Let `ω_{aj}(x)` be antisymmetric and consider the strain `δB_a^j(x) = ω_{aj}(x)`: a rotation of the three bonds that leave `x`. (a) `∂⟨H[B]⟩/∂ω_{aj}(x) = J_a^j(x → x + e_a) − J_j^a(x → x + e_j)` for every state. (b) If the field energy does not depend on `ω`, stationarity of the ledger in `ω_{aj}(x)` is `J_a^j(x → x + e_a) = J_j^a(x → x + e_j)` at every site. (c) The exactly stationary superposition of block 63 on the `4 × 4 × 4` torus (`Hψ = ψ`) violates (b) at all 64 sites, for each of the three pairs `(a, j)`; the violations sum to zero over the torus.

*Proof.* (a) T1(b). (b) By definition. (c) Computation with Gaussian rationals (runner E3). ∎

A uniform rotation costs nothing (the sum vanishes; block 62 T1): what the walk resists is a rotation that *varies*. Block 63 T5 identified the site-placed version of this quantity as the torque on the coin, a pure divergence on stationary states; a pure divergence is not zero. The blindness that fixes the member (T2) is therefore inconsistent with block 54's walk as the content: either the content is made blind — a generator for which a varying rotation of the coin axes is a symmetry, which needs an object this note does not have — or the field energy sees the rotation, and then T4's exponent is free. At second order the continuum member sees the antisymmetric strain only through a divergence (T3(b)); the torque is first order.

## Executed (supervisor control and refuting pass; evidence, not proof)

`specs/supervisor_control_block64_refuter.py`. W1: `H[B]` as a dense matrix on a `4 × 3 × 3` torus with a random strain of size 0.1: hermitian to rounding; the derivative of `⟨H[B]⟩` in one bond's strain is `−0.00807812` against the bond current `−0.00807812`. W2: for `B = dξ` the largest shift of an eigenvalue is `1.333 s²` for `s = 0.04, 0.02, 0.01` — second order — while a strain of size 0.01 that is not a relabelling shifts it by `5.6×10⁻³`, first order. **W3 (uniqueness by another route):** exact frames — no truncated expansions — with polynomial strain and rotation fields; the six basis densities' first-order change under the rotation evaluated exactly at eight rational points; the system has rank 4 and its null space is spanned by `(1, 0, 0, 0, 0, 0)` and `(0, −1/8, −1/4, 1/2, 1, 0)`: the volume and the blind combination, at all orders in the strain. W4: `D* + √g R` is exactly zero at four rational points for that finite strain.

## No-Go Discipline Gate

The note's negative sentences: no other density of the family is blind; a member that sees the coin axes has a free exponent and three more fields; the blindness is not a symmetry of the walk; with the walk as content the blind member has no static solution.

### N1 — Routes by which the sentences could fail
1. *A wider family.* Densities with more differences, or that are not functions of the curls (they would see relabellings), are outside T2.
2. *Blindness up to a divergence.* That is the weaker demand appropriate to a field energy that is NOT multiplied by the rates; it leaves `c_4` free and fixes only `c_5 = 0` and `c_1 : c_2 : c_3` (runner C2); then the rates do not couple to the lengths at first order with a fixed strength and `β` is free again. The strengthening is block 60's premise, not an extra.
3. *The lattice.* The contractions in `T_2`, `T_3` and `div V` mix the coin index with the bond index and have no unique placement on the lattice; every placement is exactly relabelling-blind (T1), none is known to be exactly rotation-blind. T2–T4 are leading-order statements in the wave vector.
4. *The content's side.* A rotation of the coin axes that varies from site to site is not a symmetry of the walk (block 62 N1.2); block 63 T5 ties the unseen part of the response to the torque on the coin, and T5 here shows the torque is not zero on a stationary state. Blindness of the field energy is supplied, not inherited, and it is inconsistent with this content. The exit is a content that is blind: in the comparator a connection built from the frame does it; whether the framework's vocabulary has such an object is the named next step.
5. *Inversion.* The Lattice axiom has proper rotations only, so the odd term `ε·T` is allowed by covariance; it is blindness that removes it.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T1(d) is at first order in the strain and for uniform rates; with a rate field both sides acquire the fall as a source (block 54) and the statement has not been redone. T2 is at first order in the rotation and the strain (the refuting pass finds the same null space at all orders in the strain). T3 through second order. The relation between the walk's `B` and the frame's strain is used at first order.

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

### N7 — Steelman
Hostile reviewer: "This is the teleparallel equivalent with a lapse; the uniqueness is textbook." Reply: yes, under the Premises. What it does for the owner is change the list in the decision record: block 60's member stops being a declaration and becomes a consequence of two supplied properties, one of which (the field energy per local tick) was already on the list. Second objection: "You have replaced one declaration by another — blindness." Reply: a fair summary, and the note says blindness is supplied and is not a symmetry of the walk; but it is one sentence with a plain meaning — the field's energy does not see what no walker in a uniform frame sees — against three numbers with none. Third objection: "The lattice statement is only T1." Reply: correct, and T1 is where the lattice could have failed: it is exact. N1.3 says what is not known on the lattice.

### N8 — Cross-cycle echo
Block 53: one covariant rule and scale covariance force the clock law's form. Block 55: action and reaction fix the source. Block 59: `β` free. Block 60: `β = 1` for a declared member. Block 62: a uniform rotation of the coin axes is unseen by the walker. Block 63: the walk keeps its books on bonds. Here: a field on the bonds whose energy is counted per tick and does not see the coin's axes has `β = 1`.

## Falsifiers

- A strain and relabelling that change a curl; a state for which `∂⟨H[B]⟩/∂B` is not the bond current; a function of the curls whose field equations have a divergence.
- A density of the family, other than the volume and `D*`, unchanged point by point by a varying rotation of the coin axes at first order.
- A strain for which `D* + √g R ≠ 0` at second order.
- A member with `4c_1 + 2c_2 + 4c_3 ≠ c_4` whose exponent is one.
- A stationary state of block 54's walk, other than a single plane wave or a mirror pair, with `J_a^j(x) = J_j^a(x)` at every site.

## Boundaries and non-claims

That bonds carry strains with the relabelling's second-neighbour coupling is supplied (block 63 named the fork). The blindness is supplied and is not a symmetry of the walk. `K`, `c_0 = 0` and every kinetic term are outside this note; so is the consistency of the static equations with a rate field and beyond first order in the strain. T2 to T4 are continuum identities; on the lattice they hold at leading order in the wave vector, and no exactly rotation-blind lattice member is exhibited. By T5 the blind member has no static solution with block 54's walk as the content; no blind walk is constructed here. The comparator is quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom (proper rotations, no inversion), the Qubit axiom's one-site algebra, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 59–63 (PRs #8570, #8581, #8590, #8591, #8592, #8593, open): restated or placed.
- Named standard imports at definition level: commuting differences on a lattice; summation by parts; the expansion of an inverse matrix and of a determinant; the scalar curvature of a metric from its connection; variational derivatives; the solution of linear conditions on coefficients.
- Reference only: Weitzenböck; Einstein (1928–1930); Møller; Hayashi and Shirafuji; Cho; Cartan; Weyl; Vermeil; Lovelock; Wegner; Wilson.

## Review record
Supervisor-run block, the twelfth of the source-link direction and the eighth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: two things are supplied here and must be named — the strain with its second-neighbour coupling (block 63's fork, taken on one side for the purpose of the note) and the blindness; the second is NOT a symmetry of the walk (block 62), and the note must not borrow authority for it from block 62 T1, which is about uniform rotations only; the Lattice axiom has no inversion, so the odd term belongs in the family. A rigour lens: a first symbolic attempt with exact inverse frames did not finish in ten minutes and was replaced by truncated expansions in the runner; the refuting pass then did the exact-frame computation at rational points with polynomial fields, which finishes, and finds the same two-dimensional null space at all orders in the strain. The isotropic frame was first taken as `1 − λ` (the inverse frame), which flips the sign of the first-order term and gave `β = −1`; the co-frame `ℓ·1` is the right object and the note says which frame the curl is taken of. The supervisor first wrote, without having computed it, that blindness *up to a divergence* does not fix `c_4`; the computation was then added to the runner (C2) and confirms it: the weaker demand fixes `c_5 = 0` and `c_1 : c_2 : c_3` and leaves `c_4`, hence `β`, free. The strengthening to point by point is exactly where block 60's premise enters, and the note says so under N1. While the first run of the gates was under way the supervisor, scoping the next block, saw that a blind field energy gives the rotation of a site's bonds no field equation while the walk's response to it is the torque of block 63 T5; the gates were stopped, the torque was computed exactly on the stationary state of the `4³` torus (non-zero at all 64 sites), and T5 was added with its runner check and mutation: the note's headline result now comes with its cost. A comparator lens: every piece is named under the Premises. A strategy lens: the decision record's list of declared objects shrinks, and a new item appears on it — a content that does not see its coin's axes; the owner should see both. Control and refuting pass (`specs/supervisor_control_block64_refuter.py`): W1–W4 as reported under Executed; all pass. Mutation census: 11 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_2026_09_21.py
```

Expected: `TOTAL: PASS=17 FAIL=0`.
