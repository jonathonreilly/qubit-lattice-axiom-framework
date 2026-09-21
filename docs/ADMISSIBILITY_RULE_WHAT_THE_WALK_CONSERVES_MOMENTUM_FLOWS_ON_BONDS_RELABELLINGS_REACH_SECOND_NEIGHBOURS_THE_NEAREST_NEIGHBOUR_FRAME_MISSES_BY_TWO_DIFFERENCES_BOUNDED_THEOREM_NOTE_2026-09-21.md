---
claim_id: admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clause of block 54 (open PR #8570; not adopted): amplitudes on Z^3 with the site's qubit as coin and the generator H = sum_a sigma_a S_a, S_a = (T_a - T_a^dagger)/(2i); and with reference to block 62 (open PR #8592), whose curvature member has a static response only for a divergence-free stress and whose site-placed frame response Theta_a^j(x) = Re psi^dagger(x) sigma_a (S_j psi)(x) was executed there NOT to be divergence-free. All statements are exact identities of the walk in the identity frame. (T1) The momentum density pi_j(x) = Re psi^dagger(x)(S_j psi)(x) obeys d(pi_j)/dt(x) + sum_a [J_a^j(x -> x + e_a) - J_a^j(x - e_a -> x)] = 0 for EVERY state, with the bond current J_a^j(x -> x + e_a) = (1/2) Re[psi^dagger(x + e_a) sigma_a (S_j psi)(x) + (S_j psi)^dagger(x + e_a) sigma_a psi(x)], which depends on amplitudes at second neighbours of x. (T2) For G_xi = (1/2) sum_j {xi_j(x), S_j}, the generator of a relabelling of the sites by xi, i[H, G_xi] = sum_a sum_j sigma_a (1/2){(d_a xi_j) C_a, S_j}, where (d_a xi_j) = xi_j(x + e_a) - xi_j(x) sits on the bond along a and C_a is the symmetric hop on that bond; its expectation is sum over bonds of (d_a xi_j) J_a^j for every state, and it vanishes on stationary states: there J is divergence-free exactly. (T3) J_a^j(x -> x + e_a) = (1/2)[Theta_a^j(x) + Theta_a^j(x + e_a)] - (1/2) Re (d_a psi)^dagger sigma_a (d_a S_j psi) for every state. For two plane waves (k, chi), (k', chi') the components at q = k - k' are Theta_a^j = (1/2)(sin k_j + sin k'_j) M_a, M_a = chi'^dagger sigma_a chi, and J_a^j = exp(i q_a/2) cos(kbar_a) Theta_a^j, kbar = (k + k')/2: block 62's defect is the factor cos(kbar_a). The conserved law is sum_a (sin k_a - sin k'_a) M_a = (energy difference) chi'^dagger chi, and sin k_a - sin k'_a = 2 sin(q_a/2) cos(kbar_a). (T4) H moves an amplitude to nearest neighbours only; i[H, G_xi] moves it to second neighbours of both kinds, x +- e_a +- e_j and x +- 2e_a: no relabelling carries a nearest-neighbour generator to a nearest-neighbour one, and no deformation of H confined to nearest-neighbour hops and on-site terms has J as its response. (T5) d(psi^dagger sigma_c psi)/dt = 2 sum_ad eps_cad Theta_d^a - [b_c(x) - b_c(x - e_c)], b_c(x) = Re psi^dagger(x) psi(x + e_c), for every state: the antisymmetric part of the site response is the torque on the coin, and on stationary states it is a lattice divergence. EXECUTED, NOT CLAIMED: for the nearest-neighbour vertex the law's symbol is unique up to scale for a given pair and equals sin k - sin k'; two equal-energy pairs with the same q = (0.5, -0.3, 0.9) and different mean wave vectors have symbols 14.6 degrees apart, so no symbol depending on q alone serves both; block 62's defect equals sum_a p_a (1 - cos kbar_a) M_a to rounding. NOT claimed: that a frame's coupling should reach second neighbours; any member built on the bond current; any law for the rotation of the coin axes; anything about rates or frames that vary; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_2026_09_21.py
---

# What the walk conserves: momentum flows on bonds, a relabelling reaches second neighbours, and the nearest-neighbour frame misses the conserved current by two differences

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact identities of block 54's supplied walk; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin; it reports exact identities of the walk - what it conserves, what a relabelling of the sites generates, and how block 62's site-placed response differs from the conserved current; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 62 (open PR #8592) ended with a bill. With the coin's frame supplying angles, block 60's member has exactly two travelling disturbances at one direction-free speed — but it answers a static source only if the content's stress is divergence-free, and the walk's site-placed frame response, tested there in floating point, was not: it missed by a term of second order. That test also depended, at the same order, on where on the lattice one chooses to place things. This note replaces it by exact statements about the walk itself.

1. **Momentum is conserved locally, and it flows on bonds.** The momentum density has an exact continuity equation for every state. Its current lives on the bonds and is a *three-site* object: the current on the bond from `x` along `a` involves amplitudes at second neighbours of `x` (T1).
2. **That current is what a relabelling generates.** Relabel the sites by a small displacement `ξ(x)`. The generator changes by a deformation placed on the bonds — the difference of `ξ_j` across the bond along `a` — that *hops along `a` and differences along `j`*: second-neighbour reach. The bond current is exactly the response to it, and for stationary states it is divergence-free, exactly (T2).
3. **The nearest-neighbour frame misses it by two differences.** Block 62's site response, averaged over a bond's two ends, differs from the conserved current by a term with two more differences along the bond. For a pair of plane waves that is a factor `cos k̄_a`, the cosine of the *mean* wave number, component by component. The conserved law's symbol is `sin k_a − sin k'_a = 2 sin(q_a/2) cos k̄_a`, which no function of `q` alone supplies (T3).
4. **Nearest-neighbour and relabelling-covariant do not fit together.** The walk's generator reaches nearest neighbours; what a relabelling makes of it reaches second neighbours. No coupling confined to nearest-neighbour hops has the conserved current as its response (T4).
5. **The antisymmetric part is the torque on the coin.** The part of the site response that block 62's metric does not see is, exactly, the rate of change of the coin's density plus a lattice divergence; for stationary states, a pure divergence (T5).

In plain terms: the walker does keep exact books on momentum, but the entries are written on the bonds and each entry looks two steps along the lattice. A frame that talks only to nearest neighbours reads those books slightly wrong — by the cosine of the wave number — and that is the first item on block 62's bill. It can be paid in one of two ways, and the framework's vocabulary does not choose: let the frame's coupling look two steps, or keep it to one step and find what absorbs the remainder. The second item is the part of the response that a metric does not see: it is the torque on the coin — a pure divergence when nothing changes in time — and nothing here gives a law for it, so whether the *symmetric* stress balances even with the bond current is left open.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 62 (PR #8592), next_trace_action: 'whether the walk in a frame field has a stress that is divergence-free in the sense the member needs (a bond-placed response ...)'; ai/probes task 'a-bond-placed-stress-for-the-walk'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a member placed to match the bond current (displacements on sites, the strain of a bond on the bond) and its travelling disturbances; whether the second-neighbour coupling keeps block 62 T1 (H^2 as a metric) and what it does to the walker's top speed; what absorbs the remainder if the coupling is kept to nearest neighbours; the owner's decision between the two"
conditional_surface_status: "T1, T2, T3 (real-space identity), T4, T5 exact operator identities for every state on every torus and on the infinite lattice; their consequences exact for every stationary state; T3's plane-wave form exact for every pair of wave vectors"
hypothetical_axiom_status: "block 54's clause (amplitudes with the qubit as coin, the walk); hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (sites, nearest-neighbour adjacency, translations), the Qubit axiom's one-site algebra, the nearest-neighbour form of the Admissibility rule as the model for "nearest-neighbour", and the memo's silence on amplitude dynamics. Block 54 (open PR) supplies the walk.

- **Shifts and differences.** `(T_aψ)(x) = ψ(x + e_a)`; `S_a = (T_a − T_a†)/(2i)`; `(d_a f)(x) = f(x + e_a) − f(x)`, a quantity on the bond from `x` along `a`, stored at `x`.
- **Walk.** `H = Σ_a σ_a S_a`, `i dψ/dt = Hψ` (identity frame, uniform rates).
- **Momentum density** `π_j(x) = Re ψ†(x)(S_jψ)(x)`. **Bond current** `J_a^j(x → x + e_a)` as in the claim scope. **Site response** `Θ_a^j(x) = Re ψ†(x) σ_a (S_jψ)(x)` (block 62).
- **Relabelling.** `G_ξ = ½ Σ_j {ξ_j(x), S_j}` for a real displacement field `ξ` on the sites. **Symmetric hop on a bond** with weight `v` on the bonds along `a`: `(C_a[v]ψ)(x) = ½[v(x) ψ(x + e_a) + v(x − e_a) ψ(x − e_a)]`.
- **Plane-wave pair.** `ψ = χ e^{ik·x} + χ' e^{ik'·x}`; `q = k − k'`, `k̄ = (k + k')/2`, `M_a = χ'†σ_aχ`.

That a continuous symmetry gives a local conservation law, with the current as the response to the symmetry made local, is Noether's theorem; the difference between the current so obtained and the symmetric one that a metric sees, by the divergence of a quantity built from the spin, is the construction of Belinfante and Rosenfeld. That a lattice derivative `sin k` brings factors of `cos k` into its conservation laws, and that symmetric and one-sided differences place currents differently, is standard in lattice field theory since Wilson. Displacements on sites with strains on bonds are the variables of lattice elasticity after Born and von Kármán. None is used as authority.

## Prior art and what is new

Every identity is of a classical kind. What is new is their exact form for the framework's supplied walk and what they say about block 62: that the defect executed there is not a numerical accident or a matter of placement but the difference between a nearest-neighbour coupling and what a relabelling generates; that this difference is, identically, a term with two more differences (a factor `cos k̄_a` for plane waves); that the symbol of the exact law depends on the mean wave number and so cannot be reproduced by any field-side symbol depending on `q` alone; and that the part of the response a metric does not see is exactly the torque on the coin. No gravitational claim is made.

## Exact target and obligation graph

Target: what the walk conserves, and how it differs from what block 62's member asks for. Obligations: (O1) the local conservation law; (O2) what generates its current; (O3) the relation to the site response; (O4) reach; (O5) the antisymmetric part. T1–T5 discharge them.

## Theorem T1 — momentum flows on bonds

*Statement.* For every `ψ`, with `ψ̇ = −iHψ`: `dπ_j/dt(x) + Σ_a [J_a^j(x → x + e_a) − J_a^j(x − e_a → x)] = 0`. `J_a^j(x → x + e_a)` depends on `ψ(x + e_a ± e_j)`.

*Proof.* Put `φ = S_jψ`. Since `S_j` commutes with `H`, `dπ_j/dt(x) = Im[ψ†(x)(Hφ)(x) − (Hψ)†(x)φ(x)]`. With `(Hφ)(x) = Σ_a σ_a (φ(x + e_a) − φ(x − e_a))/(2i)` and `Im(z/(2i)) = −½ Re z`, the first term is `−½ Σ_a Re[ψ†(x)σ_aφ(x + e_a) − ψ†(x)σ_aφ(x − e_a)]` and the second, by the same step, `+½ Σ_a Re[φ†(x)σ_aψ(x + e_a) − φ†(x)σ_aψ(x − e_a)]` with the opposite overall sign. The terms that reach forward add up to `−J_a^j(x → x + e_a)` and those that reach back to `+J_a^j(x − e_a → x)`, `σ_a` being hermitian. `φ(x + e_a) = (S_jψ)(x + e_a)` contains `ψ(x + e_a ± e_j)`. The runner checks the identity site by site for a state in motion (B1) and the dependence on a second neighbour (B2). ∎

## Theorem T2 — what a relabelling generates

*Statement.* (a) `i[H, G_ξ] = Σ_a Σ_j σ_a ½{C_a[d_aξ_j], S_j}`. (b) `⟨ψ| i[H, G_ξ] |ψ⟩ = Σ_a Σ_j Σ_x (d_aξ_j)(x) J_a^j(x → x + e_a)` for every state. (c) If `Hψ = Eψ` — or `ψ` is any superposition of eigenstates of one energy — the left side of (b) vanishes for every `ξ`, so `Σ_a [J_a^j(x → x + e_a) − J_a^j(x − e_a → x)] = 0` at every site.

*Proof.* (a) `[S_a, S_j] = 0`, and `i[S_a, ξ_j] = C_a[d_aξ_j]` by the shift rule; then `i[σ_aS_a, ½{ξ_j, S_j}] = σ_a ½{i[S_a, ξ_j], S_j}`. (b) Expand the expectation of (a) and compare with the definition of `J`. (c) `⟨ψ|[H, G]|ψ⟩ = (E − E)⟨ψ|G|ψ⟩ = 0`; summation by parts, `ξ` being arbitrary. ∎

So the deformation a relabelling generates is placed on the *bonds along `a`*, is measured by the difference of the displacement across the bond — its stretch for `j = a`, its tilt for `j ≠ a` — and acts by a hop along `a` combined with a difference along `j`. For uniform `d_aξ_j = B_a^j` it adds `Σ B_a^j σ_a cos k_a sin k_j` to `H(k)`, against block 62's `Σ ε_a^j σ_a sin k_j`: the same at long wavelength.

## Theorem T3 — the nearest-neighbour frame misses it by two differences

*Statement.* (a) For every state, `J_a^j(x → x + e_a) = ½[Θ_a^j(x) + Θ_a^j(x + e_a)] − ½ Re (d_aψ)†(x) σ_a (d_a S_jψ)(x)`. (b) For a plane-wave pair the components at wave vector `q` are `Θ_a^j = ½(sin k_j + sin k'_j) M_a` and `J_a^j = e^{iq_a/2} cos(k̄_a) Θ_a^j`. (c) For coins that are eigenvectors, `Σ_a (sin k_a − sin k'_a) M_a = (ε − ε') χ'†χ`, zero for equal energies; and `sin k_a − sin k'_a = 2 sin(q_a/2) cos k̄_a`.

*Proof.* (a) Write `ψ(x + e_a) = ψ(x) + d_aψ(x)` in both terms of `J` and collect. (b) The cross term of `Θ` is `χ'†σ_aχ sin k_j e^{iq·x}` plus the conjugate of its partner; on the bond the average gives `e^{iq_a/2} cos(q_a/2)` and the two-difference term gives `e^{iq_a/2}[cos(q_a/2) − cos k̄_a]`. (c) `Σ_a sin k_a σ_a χ = εχ` and its adjoint for `χ'`. ∎

The lattice divergence of `J` has the symbol `1 − e^{−iq_a}`, a function of `q` alone, and by (b) and (c) `Σ_a (1 − e^{−iq_a}) J_a^j = i(sin k_j + sin k'_j) Σ_a sin(q_a/2) cos(k̄_a) M_a = (i/2)(sin k_j + sin k'_j)(ε − ε') χ'†χ`, zero for equal energies. The site response would need the symbol `2 sin(q_a/2) cos k̄_a` to obey the same law. With block 62's symbol `p_a = 2 sin(q_a/2)` it leaves `Σ_a p_a M_a = Σ_a p_a (1 − cos k̄_a) M_a`: of second order in the wave numbers themselves, not only in their difference.

## Theorem T4 — nearest-neighbour and relabelling-covariant do not fit together

*Statement.* (a) `H` applied to an amplitude on one site is supported on its six nearest neighbours. (b) `i[H, G_ξ]` applied to it is supported, for generic `ξ`, on second neighbours of both kinds, `x ± e_a ± e_j` (`a ≠ j`) and `x ± 2e_a`. (c) The response to any deformation of `H` confined to on-site terms and nearest-neighbour hops is a sum of bilinears in the amplitudes at a site and one nearest neighbour; `J` is not of that form.

*Proof.* (a), (b) from T2(a): `C_a` moves one step along `a` and `S_j` one step along `j`. (c) By T1, `J_a^j(x → x + e_a)` contains `ψ†(x + e_a) σ_a ψ(x ± e_j)`, and `x + e_a`, `x ± e_j` are not nearest neighbours. ∎

## Theorem T5 — the antisymmetric part is the torque on the coin

*Statement.* For every state, `d(ψ†σ_cψ)/dt(x) = 2 Σ_{a,d} ε_{cad} Θ_d^a(x) − [b_c(x) − b_c(x − e_c)]`, `b_c(x) = Re ψ†(x)ψ(x + e_c)`. On stationary states `2 Σ ε_{cad} Θ_d^a = b_c(x) − b_c(x − e_c)`.

*Proof.* `d(ψ†σ_cψ)/dt = 2 Im ψ†σ_c Hψ = 2 Im Σ_a ψ†(δ_{ca} + i ε_{cad} σ_d) S_aψ`; the first term is `2 Im ψ†S_cψ = −[b_c(x) − b_c(x − e_c)]`, the second `2 Σ ε_{cad} Re ψ†σ_d S_aψ`. ∎

So the three numbers of a frame that block 62's walker does not see (rotations of the coin axes) are paired, on the content's side, with the coin's density: a law for the one is a law about the other.

## Executed (supervisor control and refuting pass; floating point; evidence, not proof)

`specs/supervisor_control_block63_refuter.py`. W1: the four identities for a random *complex* state on a `6 × 5 × 4` torus (unequal sides): residuals `2×10⁻¹⁵`, `1×10⁻¹⁵`, `9×10⁻¹⁶`, `4×10⁻¹⁵`. W2: a plane-wave pair on a `24³` torus, mode numbers `(1, 2, 3)` and `(3, 1, 2)`: `J_a^j(q)/Θ_a^j(q) − e^{iq_a/2} cos k̄_a` is below `3×10⁻¹⁶` for all nine `(a, j)` (`cos k̄ = 0.866, 0.924, 0.793`). **W3:** for the nearest-neighbour vertex and a given equal-energy pair, the real symbol `f` with `Σ_a f_a M_a = 0` is unique up to scale (it is `Re M × Im M`) and equals `sin k − sin k'` to five digits; two pairs with the same `q = (0.5, −0.3, 0.9)` and mean wave vectors `(0.3, 0.9, 0.011)` and `(1.1, −0.4, −0.436)` have symbols `14.6°` apart, and `6.1°` and `13.2°` from `p(q)`: no symbol depending on `q` alone serves both. W4: block 62's defect `|Σ_a p_a M_a|` equals `|Σ_a p_a (1 − cos k̄_a) M_a|` to the digits printed (`0.0945, 0.0112, 0.00138` for `L = 12, 24, 48`), with `|Σ_a p_a cos k̄_a M_a| < 10⁻¹⁶`.

## No-Go Discipline Gate

The note's negative sentences: no nearest-neighbour deformation has the conserved current as its response; a relabelling does not carry a nearest-neighbour generator to a nearest-neighbour one; (executed) no symbol depending on `q` alone gives the site response an exact law.

### N1 — Routes by which the sentences could fail
1. *A different walk.* The identities are for `H = Σ σ_a S_a` with the symmetric difference `S_a`. A generator with one-sided hops has a different current; block 54's covariance and hermiticity led to `S_a`.
2. *A different momentum.* `S_j` is the generator's own difference; with another lattice momentum the density, the current and the relabelling change together, and T2's structure (one step of the hop, one step of the momentum) stays.
3. *Frames that vary, and rates.* Not treated; T2(a) is an identity about the identity frame. In a frame field the statement that survives is T2(c)'s mechanism: whatever a relabelling generates has a response that is divergence-free on stationary states.
4. *The field side.* A member that is not exactly relabelling-invariant could absorb a second-order remainder. Not examined.
5. *W3 is a witness, not a theorem.* An exact version needs two equal-energy pairs with rational data and a common `q`; not constructed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Identity frame; uniform rates; the label's time. "Nearest-neighbour" means on-site terms and hops between sites joined by a bond. Stationary means a superposition of eigenstates of one energy. The `4 × 4 × 4` torus of the runner has wave numbers that are multiples of `π/2`, where `e^{ik}` is a Gaussian integer; the identities do not depend on it.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice, its bonds and translations; the Qubit axiom's one-site algebra; nearest-neighbour as the Admissibility rule's form | yes (premise) |
| block 54 (open PR #8570) | the walk with the qubit as coin | yes (restated) |
| block 62 (open PR #8592) | the site response, the member's condition, the executed defect | yes (restated; this note replaces its executed statement by exact ones) |
| blocks 59–61 (open PRs #8581, #8590, #8591) | lengths, the member | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "local conservation with a three-site bond current; the relabelling's deformation and its response; the site response misses by two differences (`cos k̄_a`); second-neighbour reach; the torque on the coin" | executed: the continuity equation at all 125 sites of a `5³` torus for a state in motion; dependence on a second neighbour | executed: `i[H, G_ξ]` at all 125 sites; current against bond-averaged response on all 375 bonds, nine index pairs; the torque identity at all 125 sites | executed: two plane waves of equal energy with rational sines and coins: the law with the symbol `sin k_a − sin k'_a`; the trigonometric identity at rational points | executed: an exactly stationary superposition on a `4³` torus: `Hψ = ψ`, divergence-free currents that vary from bond to bond, antisymmetric response a pure divergence and not zero | operator identities for every state on every torus and the infinite lattice; consequences for every stationary state; the plane-wave form for every pair; rates, varying frames, a member on the bond current and a law for coin rotations not treated |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used or bears on these identities. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Lattice artefacts of order `k²`; take the continuum limit and forget them." Reply: the framework has no continuum limit to take — the lattice is the first axiom — and block 62's member has *no* static solution when its condition fails, however small the failure. The note says exactly what the failure is and what would remove it. Second objection: "Then use the second-neighbour coupling and be done." Reply: it may be the right exit, but it is the owner's: every supplied clause so far has been nearest-neighbour, after the Admissibility rule's form, and T4 says relabelling covariance is bought at the price of that property. Third objection: "T5 is a textbook identity." Reply: yes; it is here because it says what the unseen three numbers of block 62's frame are tied to on the content's side, exactly and on the lattice.

### N8 — Cross-cycle echo
Block 54: inversion was an added symmetry; the walk's direction dependence is of second order in the wave vector. Block 57: nearest-neighbour kinetic terms do not propagate; a reference beyond nearest neighbours does. Block 61: nearest lengths are not enough. Block 62: the coin's frame supplies angles; the price is a conserved stress. Here: the price is exactly the gap between nearest-neighbour and second-neighbour reach, again of second order.

## Falsifiers

- A state with `dπ_j/dt + div J ≠ 0` at some site; a stationary state whose bond current has a non-zero divergence.
- A displacement field for which `i[H, G_ξ]` is not the stated bond-placed deformation, or is supported on nearest neighbours only.
- A state for which the bond current is the bond average of the site response.
- A state violating the torque identity.

## Boundaries and non-claims

Identity frame, uniform rates. No member is built on the bond current, and nothing is said about what such a member's disturbances would be. The bond current is the canonical one; whether its symmetric part is divergence-free on stationary states is not examined (T5 identifies the antisymmetric part and stops there). Whether the frame's coupling should reach second neighbours is not decided and is not proposed. W3's statement about symbols is executed, not proved. No law for the rotation of the coin axes is given. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, the nearest-neighbour form of the Admissibility rule, and the memo's silence on amplitude dynamics. Blocks 54, 59–62 (PRs #8570, #8581, #8590, #8591, #8592, open): restated or placed.
- Named standard imports at definition level: commutators with shifts and projectors; summation by parts on a torus; the product rule `σ_cσ_a = δ_{ca} + iε_{cad}σ_d`; the sum-to-product rule for sines.
- Reference only: Noether; Belinfante; Rosenfeld; Wilson; Born and von Kármán.

## Review record
Supervisor-run block, the eleventh of the source-link direction and the seventh of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: only block 54's clause is needed; the note must not slide from "this is what the walk conserves" to "therefore the coupling should be second-neighbour" — that is a fork for the owner, stated as one. A rigour lens: block 62's executed defect mixed a real effect with a choice of placement of the same order; the supervisor said so in the contract and replaced the statement by identities that hold for every state, checked with Gaussian rationals; an accidental zero (the imaginary part of one amplitude) made the first version of the second-neighbour check fail for the wrong reason and the bump was made generic; the statement about symbols depending on `q` alone stays executed because an exact witness needs rational data the supervisor did not construct. A comparator lens: current from a symmetry made local, the symmetric against the canonical stress, cosines from lattice derivatives — named under the Premises. A strategy lens: block 62's bill is now itemised, and the two ways of paying it are the owner's. Control and refuting pass (`specs/supervisor_control_block63_refuter.py`, floating point, random complex states, unequal torus sides, Fourier transforms — machinery disjoint from the runner's): W1–W4 as reported under Executed; all pass. Mutation census: 9 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_2026_09_21.py
```

Expected: `TOTAL: PASS=17 FAIL=0`.
