---
claim_id: admissibility_rule_the_walks_links_built_from_the_frame_carry_the_lengths_curvature_only_at_plaquette_reach_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54 (the walk H = sum sigma_a S_a with the qubit as its coin), 62 (the frame coupling (1/2) sum {E^j.sigma, S_j}), 64 (plaquette curls F_ab^j = d_a B_b^j - d_b B_a^j, unchanged by relabellings) and 65 (the blind walk, joint first order), all as landed on main. Exact: (T1) the generator sum_x (1/2i)[psi_x^+ M_a(x) V_a(x) psi_(x+e_a) - h.c.] with SU(2) bond links V_a is hermitian and exactly covariant under psi -> U psi, M -> U M U^+, V_a -> U_x V_a U_(x+e_a)^+, and is block 54's walk at M = sigma, V = 1. (T2) With M_a = U_x sigma_a U_x^+ and V_a = U_x U_(x+e_a)^+ it is exactly U H U^+, to all orders; its first order is block 65's blind walk (the bond-averaged frame rotation and the scalar hop (i/2)(th_y - th_x)_a, the link's twist about its own bond); its second order is (1/4)(th_x.sigma) sigma_a (th_y.sigma) - (|th_x|^2 + |th_y|^2)/8 sigma_a; with a frame the scalar weight is E(x).(th_y - th_x). (T3) With the frame split into rotation and stretch, a link fixed by the frame alone changes the coin basis by the rotation part; in long-wavelength symbols, at first order in the stretch, no nonzero rule at bond reach (linear in the stretch at the bond's two ends, covariant about the bond, zero on uniform stretch) has a plaquette holonomy blind to relabellings. (T4) At plaquette reach the rule omega_a = -curl(s e_a), equal to block 64's curls of the stretch, is blind, and its holonomy's normal component in the plane (0,1) is the linearized curvature R_0101 of the metric g = 1 + 2s. From a probes worker (Claude Opus 5.5), refereed by another model family (a Grok model). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_walks_links_carry_the_lengths_curvature_only_at_plaquette_reach_2026_09_23.py
---

# The walk's links built from the frame carry the lengths' curvature only at plaquette reach: exact links beyond first order, no curvature at bond reach, and the linearized curvature from block 64's curls

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (T1–T2 exact for every link and rotation field; T3–T4 in long-wavelength symbols at first order in the stretch; a probes worker's result refereed by another model family; nothing adopted or registered; unaudited)

This note works within the supplied clauses of blocks 54, 62, 64 and 65 (the walk with the qubit as its coin, the frame, the relabelling curls and the blind walk); it reports, from a probes worker's result refereed by another model family, how bond links built from the frame alone can carry the curvature of the lengths; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 65 (#8596), as landed on main, made the walk blind to a varying rotation of the coin axes at joint first order. It adds a scalar hop weighted by the twist along each bond. Block 64 (#8595), as landed, found that a field energy blind to the coin's axes is the curvature member, within its stated ansatz. Block 98 (#8878) asked whether records and waves see one geometry.

A probes worker asked how the walk can see the frame's curvature without a new field, and a referee of another model family (a Grok model) confirmed its exact core.

- **T1: links on the bonds make the walk exactly covariant.** Put a 2×2 matrix `M_a(x)` on each bond's first site and an `SU(2)` link `V_a(x)` on the bond. The generator is hermitian and exactly covariant when the links transform by their two ends. With `M = σ`, `V = 1` it is block 54's walk.
- **T2: links built from the sites' rotations are exact to all orders.**
  - With `M_a = U_xσ_aU_x†` and `V_a = U_xU_{x+e_a}†`, the generator is exactly `UHU†`.
  - Its first order is block 65's blind walk: the frame rotation, plus the scalar hop that is the link's twist about its own bond.
  - Its second order is `(1/4)(θ_x·σ)σ_a(θ_y·σ) − (|θ_x|² + |θ_y|²)σ_a/8`, which block 65's truncated walk leaves out.
  - For a varying frame the scalar weight is `E(x)·(θ_y − θ_x)`, not the bond difference of `θ·E`.
- **T3: bond reach carries no curvature.**
  - A link fixed by the frame alone sees the frame's rotation only as a change of coin basis, so the rotation part carries nothing.
  - Among rules that read the stretch at the bond's two ends, linearly, only the zero rule has a plaquette holonomy that ignores relabellings.
- **T4: plaquette reach carries exactly the linearized curvature.**
  - The rule `ω_a = −curl(s e_a)` reads the stretch on the plaquettes next to the bond, and it is block 64's curls of the stretch.
  - Its holonomy ignores relabellings, and in the plane `(0,1)` its normal component is the linearized curvature `R₀₁₀₁` of the metric `g = 1 + 2s`.

In plain terms: the walker's sense of direction can be carried from site to site by links built out of the same frame that sets the lengths, and then going round a small loop turns the walker by exactly the curvature of those lengths. No new field is needed. The links must look at the whole square next to each bond, though, not just the bond's two ends. At that reach, walker and lengths share one geometry, at first order in the stretch.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The walk, the frame and the links are supplied clauses. Nothing is adopted.
- **The walk** (block 54, #8570; landed in c3f8c47a58). `H = Σ_aσ_aS_a`, with `S_a = (T_a − T_a†)/(2i)`, and the qubit as its coin.
- **The frame** (block 62, #8592; landed). The coupling is `½Σ_j{E^j·σ, S_j}`. The frame splits as `E = R_E S`, a rotation times a symmetric stretch `S = 1 + s`.
- **Relabellings and curls** (block 64, #8595; landed). Strains `B_a^j` live on bonds, and relabellings shift them by `d_aξ_j`. The curls `F_ab^j = d_aB_b^j − d_bB_a^j` are unchanged by relabellings. In long-wavelength symbols the stretch shifts by `(i/2)(kξᵀ + ξkᵀ)`.
- **The blind walk** (block 65, #8596; landed). `H[ϑ] = H + ½Σ_j{(ϑ × e_j)·σ, S_j} + ½Σ_aC_a[d_aϑ_a]`, blind at joint first order about the identity frame.
- **Links.** `V_a(x) ∈ SU(2)` on the bond from `x` along `a`. The generator is `Σ_x (1/2i)[ψ_x†M_a(x)V_a(x)ψ_{x+e_a} − h.c.]`. The holonomy is taken around a plaquette.
- **Reach.** "Bond reach" means the link reads the stretch at the bond's two ends; "plaquette reach" means it reads the stretch on the plaquettes adjoining the bond.
- **Provenance.**
  - The result is from `J:derive:the-blind-walk-beyond-first-order:a1`, worker `w-jonathonsmac4f50-jd491` (Claude Opus 5.5, the same family as the supervisor). The worker's sibling unit #8843 overlaps parts (a) and (b).
  - The referee `w-macbookpro90c72-ja9b7`, a Grok model, confirmed the exact conjugation, the second-order term and the curl holonomy. It did not re-enumerate the four-parameter bond-reach family; the runner solves it exactly.
- **Names.** The links are those of Wilson's lattice gauge theory. A two-component coin in a frame needs the connection of Weyl and of Fock and Ivanenko. The linearized curvature is Riemann's tensor. The curls are the teleparallel torsion of Weitzenböck.

## Theorem T1 — links make the walk exactly covariant

*Statement.* The generator with bond matrices `M_a(x)V_a(x)` is hermitian. It is exactly covariant under `ψ → Uψ`, `M → UMU†`, `V_a → U_xV_aU_{x+e_a}†`: the bond matrix goes to `U_x(M V)U_y†`. At `M_a = σ_a` and `V = 1` it is block 54's walk.

*Proof.* `(U_xMU_x†)(U_xVU_y†) = U_x(MV)U_y†`, and hermiticity holds because the conjugate term is included. The runner checks this exactly on a ring of three sites, with random rational unit quaternions (family B). ∎

## Theorem T2 — links from the sites' rotations: exact, with block 65 as first order

*Statement.*
- With `M_a(x) = U_xσ_aU_x†` and `V_a = U_xU_{x+e_a}†`, the generator is exactly `UHU†`, to all orders.
- With `U = exp(−iθ·σ/2)`, `U_xσ_aU_y† = σ_a + [((θ_x + θ_y)/2) × e_a]·σ + (i/2)(θ_y − θ_x)_a + O(θ²)`. This is block 65's blind walk. Its scalar part `½tr(σ_aV_a)` is the link's twist about its own bond.
- The second-order term is exactly `(1/4)(θ_x·σ)σ_a(θ_y·σ) − ((|θ_x|² + |θ_y|²)/8)σ_a`.
- With a frame `E(x)` at the bond's first site, the scalar weight is `(i/2)E(x)·(θ_y − θ_x)`. The naive bond difference of `θ·E` differs from it by `(i/2)θ_y·(E(y) − E(x))`.

*Proof.* `M_aV_a = U_xσ_aU_y†`. Then expand the exponentials through third order (family C, symbolic, and exact on the ring). ∎

## Theorem T3 — bond reach carries no curvature

*Statement.*
- (a) With `E = R_E S`, a link fixed by the frame alone has the form `Û_x f Û_y†`. Then `M_aV_a = Û_x[(S_xe_a)·σ f]Û_y†`: the frame's rotation part is only a change of coin basis.
- (b) In long-wavelength symbols, consider rules `ω_a = ik_a L_a(s)` with `L_a` linear from symmetric matrices to vectors and covariant under the rotations about `e_a`. This is the four-parameter family `e_a × (se_a)`, `se_a`, `(tr s)e_a`, `(e_a·se_a)e_a`. The plaquette holonomy `ik_aω_b − ik_bω_a` vanishes for every relabelling only for the zero rule.

*Proof.* (a) By covariance under local rotations. (b) The runner solves the coefficient equations exactly in all three planes (family D). ∎

## Theorem T4 — plaquette reach carries the linearized curvature

*Statement.*
- The rule `ω_a = −curl(s e_a)` equals `−½ε_{cbd}F^a_{bd}`, with `F^a_{bd} = ∂_b s_{da} − ∂_d s_{ba}`: block 64's curls, with the stretch in place of the strain.
- Its plaquette holonomy vanishes for every relabelling.
- In the plane `(0,1)` its normal component is `k₀²s₁₁ − 2k₀k₁s₀₁ + k₁²s₀₀`. This equals the linearized curvature `R₀₁₀₁` of the metric `g = 1 + 2s`, computed from its definition.

*Proof.* Symbolic, in long-wavelength symbols (family E). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 65 (landed): the blind walk at joint first order; the one-geometry question of whether the walker's connection and the lengths share one curvature (block 98)"
source_of_blocker_text: blocks 62, 64, 65, 98; probes derivation J:derive:the-blind-walk-beyond-first-order (refereed by another family)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "links built from the frame carry the lengths' linearized curvature at plaquette reach; next: an exact lattice holonomy beyond long-wavelength symbols, the second-order completion (a lattice torsion-free condition), and whether a ledger without link energy is consistent with the curvature-carrying links"
conditional_surface_status: "T1-T2 exact for every link and rotation field; T3-T4 in long-wavelength symbols at first order in the stretch"
hypothetical_axiom_status: "the walk, the frame, the relabellings and the links are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Block 65** (#8596, landed in c3f8c47a58) gave the blind walk at joint first order, and named the separate second-neighbour torque as not removed.
- **Block 64** (#8595, landed) gave the curls and relabellings, and the curvature member within its stated ansatz.
- **Block 62** (#8592) gave the frame coupling; **block 98** (#8878) asked the one-geometry question for rays.
- In the literature, links on bonds keeping a local symmetry are Wilson's; the connection a two-component coin needs in a frame is that of Weyl and of Fock and Ivanenko; the curls are Weitzenböck's teleparallel torsion; the linearized curvature is Riemann's tensor. None is used as authority.
- **New here:**
  - the exact link form and its all-orders identity;
  - the exact second-order term of the blind walk;
  - the correct varying-frame weight;
  - the bond-reach no-go;
  - the plaquette-reach rule with the linearized curvature as its holonomy.

## Exact target and obligation graph

Target: whether the walk's links, built from the frame alone, can carry the lengths' curvature, and at what reach. The obligations are:
- (O1) covariance with links;
- (O2) links from rotations, and their expansion;
- (O3) bond reach;
- (O4) plaquette reach.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentence: no nonzero rule at bond reach, linear in the stretch, has a relabelling-blind plaquette holonomy.

### N1 — Routes by which the sentence could fail or mislead
1. *Nonlinear rules.* T3 is at first order in the stretch.
2. *Beyond long-wavelength symbols.* A lattice rule blind at every wave number is blind at leading order, so the no-go holds for lattice rules too. The positive T4 is established only at leading order.
3. *Links that are new fields.* T3 concerns links fixed by the frame. A link field with its own degrees of freedom is not excluded; it is not the "no new field" route.
4. *The second-neighbour torque.* Block 64's obstruction for antisymmetric bond strains is separate and not removed here.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The clauses of blocks 54, 62, 64 and 65 are named and supplied, and the reach classes are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| blocks 54, 62, 64, 65 | the walk, the frame, the curls, the blind walk | yes |
| block 98 | placement | no |
| probes worker `w-jonathonsmac4f50-jd491`; referee `w-macbookpro90c72-ja9b7` | the result; the confirmation | yes (verified here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "links from the frame carry the lengths' curvature only at plaquette reach" | executed: the bond matrix and link identities with random rational unit quaternions; the first- and second-order expansions (symbolic) | executed: the whole generator on a ring of three: hermiticity, covariance, and `UHU†` with links from the sites' rotations | executed: the long-wavelength symbols: the four-parameter bond-reach family, the plaquette-reach rule, and the linearized curvature from its definition | executed: plaquette holonomies in the three coordinate planes | T1–T2 exact for every link and rotation field; T3–T4 in long-wavelength symbols at first order in the stretch; blocks 54, 62, 64, 65 supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This is the textbook torsion-free connection." *Reply:* yes, at first order. The note shows that on the lattice it needs plaquette reach, which bond reach cannot give. It shows that it can be built from block 64's own curls, with no new field.
- *Objection:* "Long-wavelength symbols are not the lattice." *Reply:* true for T4. An exact lattice holonomy is the next step, and N1.2 says so.

### N8 — Cross-cycle echo
- Block 65 made the walk blind at first order.
- Block 64 found the curvature member.
- Block 98 asked about one geometry.

This note connects the walker's turning round a loop to the lengths' curvature.

## Falsifiers

- A nonzero bond-reach rule of the stated family with a relabelling-blind holonomy.
- A different second-order term from an independent expansion.
- A plaquette holonomy of `−curl(s e_a)` that differs from the linearized `R₀₁₀₁`.

## Boundaries and non-claims

- The walk, the frame and the links are supplied, not adopted.
- T3 and T4 are at first order in the stretch, in long-wavelength symbols.
- No second-order completion or exact lattice holonomy is given, and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 62, 64, 65 and 98 (PRs), restated or placed.
- Named standard imports, at definition level:
  - the Pauli matrices;
  - unit quaternions and the Cayley map;
  - Wilson links;
  - the linearized Riemann tensor;
  - exact rational and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the fifty-fifth since the source-link direction opened, built from a probes worker's result with an other-family referee.
- **Provenance.**
  - Worker `w-jonathonsmac4f50-jd491` (Claude Opus 5.5). Referee `w-macbookpro90c72-ja9b7` (a Grok model).
  - The supervisor ported the exact checks, and added the linearized curvature computed from its definition.
  - The mutation census exposed a weak mutation: restricting to one plane still leaves only the zero rule. It was replaced by a false claim that a nonzero rule is blind.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_walks_links_carry_the_lengths_curvature_only_at_plaquette_reach_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
