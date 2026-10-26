---
claim_id: admissibility_rule_the_walker_on_the_members_lengths_keeps_relabellings_at_first_order_and_at_the_next_needs_exactly_one_term_the_comparators_inversion_odd_curl_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 62's framed coupling of the walker, taken at long wavelength on smooth states of the species at k = 0 and on half-densities, with the frame built from the member's lengths alone (the symmetric frame e = g^(1/2) = 1 + eta), and the member's spatial relabellings acting on the lengths as on a tensor field: (T1) the comparator's two-component operator in a frame, on half-densities, equals the framed walk plus (1/8) eps.C times the identity (eps.C the frame's inversion-odd curl), checked through second order for general frames; for the lengths' frame eps.C vanishes at first order and equals 2 eps_abc eta_ad d_b eta_cd at second; (T2) relabelled, with its coin turned so that its frame stays the lengths' frame, the framed walk keeps the relabellings at first order and misses them at order strain x relabelling by the coin scalar t = -(1/8) eps_abc (eta_ad d_b S_cd + S_ad d_b eta_cd), S = d xi + d xi^T, which is nonzero (a stretched rod twisted about its axis: t = -lambda tau/4); adding (1/8) eps.C restores them; (T3) among local potentials with at most one derivative, linear or quadratic in the strain, scalar or coin vector, this term is the only one that restores them, and no local law for the coin substitutes. Exact over the Gaussian rationals, bilinear identities proved on all pairs of basis jets. Relabellings in time, the lattice placement for the eight species and third order are not examined. Supervisor's own work (Claude Opus 5.5); unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_walker_on_the_members_lengths_needs_the_comparators_inversion_odd_curl_at_second_order_2026_09_26.py
---

# The walker on the member's lengths keeps relabellings at first order; at the next order it needs exactly one term, the comparator's inversion-odd curl

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact identities at leading order in the spacing, for smooth states of the zero-corner species, with spatial relabellings only; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 62 and 65 as landed on main (the walker's framed coupling, the member's lengths and relabellings, and what turning the coin does); it reports what the member's relabellings require of the walker's coupling at the order of the member's cubic completion, at leading order in the spacing; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The member supplies lengths and nothing else. So the walker can only see a frame built from the lengths: the symmetric square root of the metric. A relabelling of the sites moves the lengths, and the dragged frame is then no longer symmetric. To stay the lengths' frame it must be turned back, and the walker's coin must turn with it. Block 65 showed that turning the coin from place to place costs the walker a coin-scalar term, the twist.

- **T1: what the comparator adds to the framed walk.** The comparator's two-component operator in a frame, with its connection and on half-densities, is the framed walk plus one coin-scalar term, `(1/8) ε·C`. Here `ε·C` is the frame's inversion-odd curl, the totally antisymmetric part of the frame's curl. For the lengths' own frame `e = 1 + η`, this term is zero at first order in the strain and `B = 2ε_abc η_ad ∂_b η_cd` at second order.
- **T2: the framed walk alone keeps relabellings only at first order.** Relabel by `ξ` and turn the coin so the frame stays the lengths'. At first order the framed walk of the old lengths becomes exactly the framed walk of the new lengths. At the next order, strain times relabelling, it misses by the coin scalar `t = −(1/8) ε_abc (η_ad ∂_b S_cd + S_ad ∂_b η_cd)`, with `S = ∂ξ + ∂ξᵀ`, and `t` is not zero. Example: a rod stretched by `λ` along its axis and twisted about that axis by `τ` per unit length gives `t = −λτ/4`. Adding `B/8` removes `t` exactly.
- **T3: nothing else does it.** Consider every local potential built from the strain with at most one derivative: linear or quadratic, coin scalar or coin vector. Exactly one of them restores the relabellings, `B/8` times the identity. No other local law for turning the coin, and no phase, can substitute for it.

In plain terms: a walker that feels only the lattice's lengths slips out of step with the member when the lattice is both stretched and relabelled with a varying twist. The slip is proportional to stretch times twist gradient. One extra term fixes it. That term measures how the stretch winds around itself, it is built from the lengths alone, so no new field is needed, and it is exactly the comparator's connection term. Block 157 found that the member's own next order is the comparator's. At the same order the walker's coupling is the comparator's too.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The walker's coupling, the member's relabellings and the comparator are supplied clauses. Nothing is adopted.
  - The Lattice axiom has proper rotations only (block 54), so an inversion-odd term is not excluded by symmetry.
- **The walker's framed coupling** (block 62, landed): `H[E] = ½Σ_j{E^j·σ, S_j}` with frame vectors `E^j_a`.
  - At long wavelength, on smooth states of the species at `k = 0`, `S_j → −i∂_j`. Then `H_f[E] = ½{E^j_a σ_a, −i∂_j} = −iσ_a E^j_a ∂_j − (i/2)(∂_j E^j_a) σ_a`.
  - The walker's amplitudes carry the lattice's counting norm `Σ_x |ψ_x|²`, so they are half-densities.
- **The member's lengths** (block 62, landed): `g_ij = δ_ij + h_ij`.
  - The lengths' own frame is the symmetric square root, as a covector frame `e = g^{1/2} = 1 + η` (`η` symmetric, `η = h/2 − h²/8 + …`), with frame vectors `E = e⁻¹`.
  - Block 62's first-order coupling sees only the symmetric part of the frame, `h = −(ε + εᵀ)`. A rotation field would be a new field, which the member does not have.
- **Relabellings in space.** The flow of `uξ` moves the lengths as a tensor field. The covector frame is dragged, `δe^a_i = −u(ξ^k ∂_k e^a_i + e^a_k ∂_i ξ^k)`, and the walker is moved as a half-density, `δψ = −u(ξ^k ∂_k ψ + ½(∂_k ξ^k)ψ)`.
- **Turning the coin.**
  - `U = 1 − (iu/2) θ·σ` turns the coin vectors by `θ ×`.
  - The rotation that keeps the frame symmetric has the matrix `Θ_ac = ε_abc θ_b`, with `Θ = ½(J − Jᵀ) + ¼[η, S] + O(η²)`, `J_ai = ∂_i ξ_a`, `S = J + Jᵀ`.
  - At first order `θ = ½ curl ξ`.
- **The inversion-odd curl of a frame:** `ε·C = ε^{abc} E^i_b E^j_c (∂_i e^a_j − ∂_j e^a_i)`, block 64's inversion-odd scalar of the co-frame's curl.
- **The comparator**, named at definition level. It is the two-component operator of Weyl and of Fock and Ivanenko: `H_c = g^{1/4}[−iσ_a E^j_a(∂_j + Γ_j)]g^{−1/4}`, with `Γ_j = (1/8)ω_jab[σ_a, σ_b]` and `ω_jab = e^a_k(∂_j E^k_b + Γ^k_jl E^l_b)`, where `Γ^k_jl` is the metric's own connection. It is covariant under relabellings and under local turns of the coin.
- **Standard imports, named at definition level.**
  - The product rule of the coin's three matrices.
  - Derivatives along a vector field on half-densities, and their naturality under relabellings (checked, runner A3).
  - Exact linear algebra over the rationals.
  - Polarization: an identity bilinear in two sets of jets holds iff it holds on every pair of basis jets.

## Theorem T1 — what the comparator adds to the framed walk

*Statement.*
- (a) For every frame, through second order in its strain, `H_c − H_f[E] = (1/8)(ε·C)·𝟙`, with no coin-vector part (runner B1 and B2, generic jets, general and symmetric frames). This is the comparator's standard identity at every order; only the checked orders are used below.
- (b) For the lengths' frame `e = 1 + η`: `ε·C = 0` at first order in `η`, and `ε·C = B := 2ε_abc η_ad ∂_b η_cd` at second order. In the member's strain, `B = ½ ε_abc h_ad ∂_b h_cd + O(h³)`.

*Proof.*
- (a) Write `ω_abc = E^j_a ω_jbc`. Then `−iσ_a E^j_a Γ_j = (1/4)ω_abc ε_bcd σ_a σ_d`.
  - Its coin-scalar part is `(1/4)ε_abc ω_abc`, and `ε_abc ω_abc = ½ ε·C`: the totally antisymmetric part of the connection is half that of the frame's curl.
  - Its coin-vector part is `−(i/2)ω_aaf σ_f`. Together with the density weight `−¼ ∂_j log det g` and the framed walk's own term `−(i/2)(∂_j E^j_a)σ_a`, it cancels.
  - The runner checks the whole difference at a point, with generic jets, through second order (B1, B2).
- (b) At first order the frame indices are coordinate indices, and `ε·C = 2ε^{abc} ∂_b η_ac`. This vanishes because `η` is symmetric. The second-order form is runner B2. ∎

## Theorem T2 — the framed walk alone keeps relabellings only at first order

*Statement.* Relabel by `uξ` and turn the coin by the rotation `Θ` that keeps the frame the lengths' own. Compare the moved walker with the framed walk of the new lengths `H_f[E']`.
- (a) At order `u`, they are equal.
- (b) At order `uη`, their principal parts are equal, and they differ by a coin scalar `t·𝟙` with no coin-vector part:

  `t = −(1/8) ε_abc (η_ad ∂_b S_cd + S_ad ∂_b η_cd) = (1/8) × (the change of ε·C)`.

  So `H_f + (1/8)ε·C` keeps the relabellings through this order.
- (c) `t ≠ 0`. For a rod stretched by `λ` along axis 1 (`η_11 = λ`) and twisted about that axis by `τ` per unit length (`ξ = τ x_1(0, −x_3, x_2)`), `t = −λτ/4`.

*Proof.*
- **Dragging alone is exact.** The framed walk is `−iσ_a` times the derivative along the frame vector `E_a` on half-densities. That derivative moves with the relabelling. So a relabelling with the frame dragged along reproduces the framed walk of the dragged frame exactly (runner A3, on every pair of basis jets).
- **Turning the coin adds a scalar.** The dragged frame is not symmetric, so the coin is turned by `Θ`. That produces the rotated frame together with block 65's coin scalar, the twist of the turn.
  - At order `u`, `θ = ½ curl ξ` has no divergence, so the twist is zero (runner C1).
  - At order `uη` the twist is the stated `t`. The identity is bilinear in the jets of `η` and `ξ` at the point, so it holds iff it holds on all 1800 pairs of basis jets (runner C2, C3).
- **Consistency with T1.** The comparator is covariant, and by T1 it is `H_f + (1/8)ε·C`. So `t` must equal the change of `(1/8)ε·C`, and the runner confirms it (C3). Example (c) is runner C4. ∎

## Theorem T3 — nothing else does it

*Statement.*
- (a) Let `V = V⁰ + V^f σ_f`, with
  `V^c = z^c_α η_α + y^c_αβ η_α η_β + L^c_αb ∂_b η_α + T^c_αbβ η_α ∂_b η_β`.
  This is any local potential built from the strain with at most one derivative and no constant term: 612 coefficients over the six strain components. Then `H_f + V` keeps the relabellings at orders `u` and `uη` iff `V = (1/8)B·𝟙`.
- (b) The walker's law is fixed. The relabelling moves the walker as it moves every half-density. The only remaining freedom is a local turn of the coin at each site, a rotation times a phase.
  - A further rotation gives the frame an antisymmetric part, so it is no longer the frame of any lengths.
  - A phase `φ` adds `−E^j_a(∂_j φ)σ_a`, a pure coin-vector term.
  - Neither removes a coin-scalar residual.

*Proof.*
- (a) Covariance at a point is linear in the 612 coefficients and bilinear in the jets. The basis pairs give 7320 exact equations over Q.
  - Their rank is 612, and it is 612 again with the residual appended. So there is exactly one solution, and it is `B/8` (runner D1).
  - Why the solution is unique:
    - The relabelling's strain `S` and its first derivatives are arbitrary at a point, so every coefficient is tested.
    - A potential without derivatives changes by terms with one fewer derivative on `ξ` than `t` has.
- (b) Runner D2, and the product rule of the coin's matrices. ∎

A constant `V⁰` is unchanged by everything; it is an overall energy shift and is excluded. Potentials with two or more derivatives are higher order in the spacing. Some of them are invariant, the lengths' curvature scalar among them; they are not classified here.

## What this settles and what it does not

- **Programme T** (panel of 2026-09-26, afternoon) asked whether the framed walk's coupling is consistent with the member at second order in its fields, or whether consistency forces a connection-like term.
  - It forces one term, of second order in the lengths, built from the lengths alone.
  - Among local potentials with at most one derivative it is unique, and it is the comparator's connection term.
  - A new field, for example a coin-rotation field on the bonds, is not needed at this order.
- **With block 157** (pushed, unrefereed): at leading order in the spacing, the member's cubic completion and the walker's second-order coupling are both the comparator's.
- **The term is inversion-odd.** Block 64 T2 found that a field energy blind to the coin's axes cannot contain `ε·T`. Block 65 T4 found that the walker's twist is `−⅛ ε·T` at first order. Here the walker's coupling must contain `(1/8)ε·C` at second order in the lengths, even though the lengths' frame is symmetric.
- **Not settled:**
  - relabellings in time (the lapse and the shift);
  - the term's placement on the lattice and what it does for the other seven species. Block 161 (pushed later the same day) shows that at long wavelength links on the bonds carrying the lengths' own connection supply exactly this term; a nearest-neighbour lattice rule is still open;
  - third order.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "panel 2026-09-26 (afternoon), programme T: at second order in the member's fields, is the framed walk's coupling (no connection) consistent with the comparator's cubic vertex, or does consistency force a connection-like term (a coin rotation field) or fail at a stated order?"
source_of_blocker_text: panel dossier of 2026-09-26 afternoon (decision-record addendum 46)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "relabellings in time (lapse and shift) at the same order; the lattice placement of the term and its effect on the eight species; an other-family referee"
conditional_surface_status: "leading order in the spacing; smooth states of the zero-corner species; spatial relabellings; potentials with at most one derivative"
hypothetical_axiom_status: "the walker's coupling, the member's relabellings and the comparator are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 62: the framed coupling. It remarks that the walker has no connection, where in the comparator a connection compensates local rotations.
  - Block 64 T2: a blind field energy has `c₅ = 0`.
  - Block 65:
    - T1: turning the coin at first order about the identity frame gives the frame rotation plus a scalar hop weighted by the twist.
    - T4: that hop is `−⅛ ε·T` at long wavelength. Its Premises name the reduction of a two-component spinor's connection to a scalar potential in three dimensions (Weyl; Fock and Ivanenko).
- **Probes (Claude Opus 5.5, the supervisor's own family; unrefereed).**
  - *A law for the rotation of the coin axes*, a2 (#8843): with links on the bonds fixed by the frame and flat, "the walker sees only `√g`". A torsion-free rule for the links was named as missing. An other-family referee (a Grok worker, #9308) has since confirmed it, and block 161 harvests it.
  - *Parity-odd couplings under the proper rotations only*: the odd frame density changes by `−4 div ϑ` under a coin rotation at zero strain. An other-family referee (a Grok worker) found attempt 1's steps sound.
- **Block 157** (pushed, unrefereed): the member's cubic completion is the comparator's at leading order.
- **In the literature.**
  - The two-component operator in a frame with its connection (Weyl 1929; Fock and Ivanenko 1929).
  - That it depends on the frame, besides the symmetrized derivative, only through the totally antisymmetric part of the anholonomy. This is a standard identity of the comparator's spinor calculus; T1(a) reproduces it.
  - Reference only.
- **New here.**
  - T1(b): the second-order form for the lengths' own frame.
  - T2: the relabelling residual of the connection-free framed walk. It is zero at first order and nonzero at order strain times relabelling, with its closed form and the twisted-rod example.
  - T3: uniqueness of the repair among potentials with at most one derivative, and the fixed law for the coin.
  - So the probes' "walker that sees only `√g`" is not consistent with relabellings at second order unless the comparator's term is added.
- **Provenance.** The supervisor's own derivation and runner. No other model family has refereed it.

## Exact target and obligation graph

Target: programme T at leading order in the spacing, spatial part. The obligations are:
- (O1) the premise, naturality of the framed walk under dragging (A3);
- (O2) the comparator's difference from the framed walk (T1: B1, B2);
- (O3) the relabelling residual (T2: C1–C4);
- (O4) uniqueness and the coin's law (T3: D1, D2).

The strongest missing steps are relabellings in time and the lattice placement.

## No-Go Discipline Gate

The note's negative sentences:
- without the term, the walker on the lengths' frame misses the relabellings at order strain times relabelling;
- no other local potential with at most one derivative, and no local law for the coin, repairs it.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The residual is a gauge artefact removable by a different turn of the coin.* A different rotation breaks the frame's symmetry, and a phase gives a coin vector (T3(b); runner D2). ATTEMPTED.
2. *Another potential repairs it.* The 612-coefficient system has one solution (T3(a); D1). ATTEMPTED.
3. *The residual vanishes identically.* It is nonzero on 48 basis pairs; the twisted rod gives `−λτ/4` (C3, C4). ATTEMPTED.
4. *The framed walk itself is not natural under dragging.* It is, exactly (A3). ATTEMPTED.
5. *The comparator identity is misapplied.* Checked at a point for general and for symmetric frames with generic jets (B1, B2). ATTEMPTED.

Scope left open:
- potentials with two or more derivatives;
- non-local repairs;
- relabellings in time;
- the lattice placement;
- third order.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The restriction to the lengths' own frame is a declared premise: the member has no rotation field.
- The half-density rule follows from the lattice's counting norm.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms; proper rotations only | yes |
| block 62 (landed) | the framed coupling; the lengths | yes |
| block 65 (landed) | the twist of a coin turn | yes (reproduced inside runner C) |
| block 64 (landed) | the inversion-odd scalar | context |
| block 157 (pushed, unrefereed) | the member's cubic completion | context only |
| probes (unrefereed, same family) | the walker that sees only `√g`; the odd density | context only |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "first order kept; order strain x relabelling missed by `t`; `B/8` the unique repair" | executed: T1 for every jet through second order | executed: all 1800 basis pairs at orders `u`, `uη` | executed: closed form, twisted rod | executed: 7320 x 612 system; the coin's law | not executed: lattice placement, eight species, time, third order |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This is the comparator's spin connection, known for a century."
  - *Reply:* The comparator's operator is known. Three things were not known here:
    - whether the walker, whose frame is built from the member's lengths and which has no connection, is consistent with the member's relabellings;
    - at which order it fails;
    - whether anything other than the comparator's term repairs it.
  - The answers are: first order kept; failure at strain times relabelling; the repair unique among one-derivative potentials.
- *Objection:* "Lengths-only frames are a choice."
  - *Reply:* The member supplies nothing else. Any other frame needs a rotation field, which would be a new field.

### N8 — Cross-cycle echo
- Block 62: no connection.
- Block 65: the first-order twist hop.
- Block 64: `c₅ = 0` for blind field energies.
- The probes: the walker sees only `√g`.
- This note: that walker keeps relabellings at first order only, and the comparator's inversion-odd term is the unique one-derivative repair.

## Falsifiers

- A basis pair of jets on which the residual differs from the stated `t`.
- A second local potential with at most one derivative that restores the relabellings.
- A local turn of the coin that keeps the lengths' frame and removes the residual.

## Boundaries and non-claims

- Leading order in the spacing.
- Smooth states of the species at `k = 0`.
- Spatial relabellings only.
- Potentials with at most one derivative.
- Not covered: the lattice placement of the term, the other seven species, relabellings in time, third order.
- Not refereed by another model family.
- No gravitational claim is made, and nothing is adopted.

## Imports

- `minimal_axioms`. Blocks 62, 64 and 65 (landed), restated.
- Named standard imports, at definition level:
  - the product rule of the coin's three matrices;
  - derivatives along vector fields on half-densities;
  - exact linear algebra over the rationals;
  - polarization of bilinear identities;
  - the comparator's two-component operator in a frame with its connection (Weyl; Fock and Ivanenko), as a comparator.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign of that day. It answers the afternoon panel's programme T.
- **Before writing.** The own prior-art check covered memory, open PRs, the probes' attempts and main. It found:
  - block 65 (the first-order twist hop and its `−⅛ ε·T` form);
  - block 62's remark;
  - the probes on the rotation of the coin axes (flat links fixed by the frame: the walker sees only `√g`) and on parity-odd couplings.
  - None treats the member's relabellings at second order.
- **Independence.** The runner's families use disjoint machinery:
  - the comparator is built at a point from generic jets (B);
  - the moved walker is built as an operator on all basis pairs (C);
  - uniqueness is a separate exact linear system (D).
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_walker_on_the_members_lengths_needs_the_comparators_inversion_odd_curl_at_second_order_2026_09_26.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
