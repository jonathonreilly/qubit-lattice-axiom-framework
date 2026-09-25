---
claim_id: admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk H = sum_a sigma_a S_a at a uniform clock rate wbar, block 69's two-step momentum P_j = S_j C_j and its reach-three current K_a^j (blocks 73 and 74), block 62's member with its stress coupling (1/2) sum Theta_ij h_ij and block 101's quadratic action, all as landed on main and supplied, with block 120's phi-realisation B_i^j = -(1/2) phi_j h_ij, phi_j = (1/2)(1 + T_j^-1) prod_{l != j} C_l (open) as the placement; first order in the member's fields. Exact: (T1) with Theta_ij = phi_j^T K_i^j and e' = C_1 C_2 C_3 e, the energy density averaged over the eight body-diagonal neighbours, every state of the walk obeys the operator identity d^2 e'(x)/dt^2 = wbar^2 sum_ij dbar_i dbar_j Theta_ij(x) on Z^3 (all eight species, both branches, every wave vector), that is e'' = -wbar^2 p.Theta.p in block 62's placement. (T2) the site energy e misses by the one factor prod_l cos q_l, the same for every species, branch and mean wave number. (T3) block 62's site stress meets neither placement, and without its transverse average block 120's realisation leaves a factor that depends on the mean wave number, which no placement of the energy repairs. (T4) at the closing ratio beta = -alpha the member demands e_u'' = -(K wbar^2/(4 alpha)) p.Theta.p of the energy e_u sourcing its clock; with e_u = e' and this source its constraint equations admit the walker's content, for every state, iff alpha = K/4. The supervisor's own derivation (Claude Opus 5.5), checked by its runner; not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_2026_09_25.py
---

# One light cone exactly on the lattice: the two-step content meets the member's identity for every state iff α = K/4

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact within the landed walk, currents and member, with block 120's placement; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 62, 69, 73, 74 and 101 as landed on main (the walk, the frame's stress coupling, the two-step momentum and its current, and the member's quadratic action), with blocks 112, 120 and 134 placed; it reports whether the walker's two-step content, placed as block 120 places it, meets the member's identity exactly; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 134 (open) found that at the closing ratio `β = −α` the member demands `ë = −(Kw̄²/(4α)) p·Θ·p` of its content. The walker's smooth states meet that demand at leading order iff `α = K/4`. Two things were left over:
- lattice corrections that depend on the waves' directions;
- six species that fail already at leading order.

Block 120 (open) found that only the two-step current can be placed on the member so that the member's static equation stays solvable, through its φ-realisation. This note asks whether that same placement also meets the member's dynamic demand.

- **T1: it does, exactly.**
  - Read block 69's reach-three current through block 120's realisation.
  - Average the energy density over each site's eight body-diagonal neighbours.
  - Then every state of the walk obeys `ë′ = −w̄² p·Θ·p` exactly. This is an operator identity on `ℤ³`, for all eight species, both branches and every wave vector.
- **T2: why.** The site energy misses by one factor, `Π_l cos q_l`. That factor is the same for every species, branch and mean wave number, and the body-diagonal average supplies it.
- **T3: what fails.**
  - Block 62's site stress meets neither placement of the energy.
  - Without its transverse average, block 120's realisation leaves a factor that depends on the mean wave number. No placement of the energy can repair that.
- **T4: one light cone, exactly.** The member's constraint equations admit this content, for every state, iff `α = K/4`. Block 134's lattice corrections and species split disappear.

In plain terms, the field's equations only work if what feeds them keeps its books in the field's own way: energy must flow exactly as fast as momentum. The walker's ordinary momentum does this only for smooth, slow waves. Its two-step momentum does it for every state, provided the energy is counted as a local average. Then the field's travelling disturbances must have exactly the walker's top speed.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its currents and their placements, the member, its kinetic term and the source link are supplied clauses. Nothing is adopted.
- **The walk** (block 54 as landed).
  - `(T_aψ)(x) = ψ(x + e_a)`, `S_a = (T_a − T_a⁻¹)/(2i)`, `C_a = (T_a + T_a⁻¹)/2`.
  - `H = Σ_aσ_aS_a`, at a uniform clock rate `w̄` (take `w̄ = 1`; a rate multiplies both sides of T1 by `w̄²`).
- **Energy densities.**
  - The site energy is `e(x) = Re ψ†(x)(Hψ)(x)` (blocks 55–56).
  - The averaged energy is `e′ = C₁C₂C₃e`, the mean of `e` over the eight sites `x + (±1, ±1, ±1)`.
- **The two-step current** (blocks 69, 73 and 74 as landed).
  - `P_j = S_jC_j`, with symbol `½ sin 2k_j`.
  - On the bond `x → x + e_a`: `K_a^j = ½Re[ψ†(x+e_a)σ_a(P_jψ)(x) + (P_jψ)†(x+e_a)σ_aψ(x)]`.
- **The placement** (block 120, open).
  - `B_i^j = −½φ_jh_ij`, with `φ_j = ½(1 + T_j⁻¹)Π_{l≠j}C_l`.
  - Read as a source, it couples to `h` as `½ΣΘ_ijh_ij` with `Θ_ij = φ_jᵀK_i^j` and `φ_jᵀ = ½(1 + T_j)Π_{l≠j}C_l`. This is block 120's site convention, whose `h_ij(x)` sits at `x + (e_i + e_j)/2` in block 62's placement.
- **The member** (blocks 62 and 101 as landed).
  - `L = [α tr(ḣ²) + β(tr ḣ)²]/w̄ + Kw̄(uR₁ + R₂) − e_uu + ½ΣΘ_ijh_ij`, with `R₁ = p² tr h − p·h·p` and block 62's `R₂`. The energy that sources the clock is written `e_u`.
  - Everything is at first order in the member's fields.
- **Double divergence.** `∇̄_if(x) = f(x) − f(x − e_i)`. In block 62's placement, `−p·Θ·p` reads `Σ_ij∇̄_i∇̄_jΘ_ij` in the site convention.
- **Comparators, named only:** the conservation identities of a symmetric action (Noether's second theorem); the consistency of a stress source with a relabelling-invariant member, which is the comparator's contracted identity.

## Theorem T1 — the two-step content meets the identity exactly

*Statement.* For every state of the walk on `ℤ³`,

`d²e′(x)/dt² = Σ_ij ∇̄_i∇̄_jΘ_ij(x)`, with `Θ_ij = φ_jᵀK_i^j`.

In operator form, `−[H, [H, e′(x)]] = Σ_ij∇̄_i∇̄_jΘ_ij(x)`. In block 62's placement it reads `ë′ = −p·Θ·p` at every wave vector. It holds for all eight species and for both branches.

*Proof.* T2 below gives the matrix element between any two eigen-waves, so the operator identity holds on `ℤ³`. ∎

*Checked (B1).*
- As exact matrices over `ℚ(i)`, on the `5³`, `6³` and `9³` tori; both sides are nonzero.
- Folding `ℤ³` onto a torus preserves these operators, because each product has a translation-invariant factor.
- Both sides are supported within distance 4 of `x`, and the `9³` torus separates such points. So the torus identity carries over to `ℤ³` independently of T2.

## Theorem T2 — the mechanism: one common factor

*Statement.* Take the beat of two eigen-waves `(k, l, u)` and `(k′, l′, u′)`, with `σ·s u = lu` and `s = sin k`, at `q = k − k′`, and let `k̄ = (k + k′)/2`. Then:
- `e_q = ½(l + l′)u′†u`, and `ë_q = −(l − l′)²e_q`;
- in block 62's placement, `Θ_ij(q) = cos(q_j/2) Π_{l≠j}cos q_l · cos k̄_i · ½(P_j(k) + P_j(k′)) · u′†σ_iu`;
- `p·Θ·p = Π_l cos q_l · (l − l′)²e_q`.

So the site energy misses by the one factor `Π_l cos q_l`, which is the symbol of `C₁C₂C₃`, and `ë′ = −p·Θ·p` exactly.

*Proof.*
- The bond current carries `e^{iq_i/2}cos k̄_i` at `q`. With `p_i = 2 sin(q_i/2)`, `p_i cos k̄_i = sin k_i − sin k′_i`. Also `Σ_i(sin k_i − sin k′_i)u′†σ_iu = (l − l′)u′†u`, since both are eigenvectors.
- Along `j`: `p_j cos(q_j/2) = sin q_j`, and `sin q_j(P_j(k) + P_j(k′)) = cos q_j(sin²k_j − sin²k′_j)`.
- With the transverse factor, every `j` carries the same `Π_l cos q_l`. Summing `sin²k_j − sin²k′_j` over `j` gives `l² − l′²`.
- The placement phases cancel.

∎

*Checked (C1).* Symbolically:
- the trigonometric identity;
- the eigen-identity, modulo `l² = |s|²` and `l′² = |s′|²`;
- the assembly into the common factor.

## Theorem T3 — what fails

*Statement.*
- (a) Block 62's site stress `Θ_i^j = Re ψ†σ_i(S_jψ)` meets neither `e` nor `e′`.
- (b) Block 120's realisation without its transverse average, `φ_j = ½(1 + T_j⁻¹)`, meets neither `e` nor `e′`.
- (c) For (b), the beat's double divergence is `½(l − l′)u′†u Σ_j cos q_j(sin²k_j − sin²k′_j)`. At a fixed `q`, its ratio to `l² − l′²` changes with `k̄`. So no placement of the energy, which can depend only on `q`, repairs it.

*Proof.* (a), (b): exact operator comparisons. (c): T2's computation without the transverse factor. ∎

*Checked (D1).*
- (a) and (b): the operators differ on the `5³` torus.
- (c): at `cos q = (4/5, 12/13, 1)`, two mean wave numbers give the ratios `7645551/9075248` and `197797929/232852880`.

## Theorem T4 — one light cone, exactly

*Statement.*
- (a) At `β = −α` the member demands `ë_u = −(Kw̄²/(4α)) p·Θ·p` of the energy `e_u` that sources its clock. This is block 134 T1, re-derived with `R₂` and the full stress.
- (b) With `e_u = e′` and the two-step source, T1 gives `ë′ = −w̄² p·Θ·p` for every state. So the member's constraint equations admit the walker's content for every state, all eight species, both branches and every wave vector, iff `α = K/4`. At that value the member's travelling disturbances move at the walker's top speed at long wavelength.
- (c) The averaged energy has the same total as the site energy: `Σ_xe′(x) = Σ_xe(x)`. Its symbol `Π_l cos q_l` is:
  - `1` at `q = 0`;
  - `1 − |q|²/2 + O(|q|⁴)` near it;
  - `−1` at the stagger `π(1,1,1)`, where it moves a chessboard source (block 133) to the other sublattice.
- (d) By action and reaction (block 55), a clock that is sourced by `e′` is felt by the walker through the same average, as the strain is felt through `φ`.

*Proof.* (a) as in block 134. (b) combine (a) with T1. (c) `C_l` preserves sums; the symbol is a product of cosines. (d) the coupling `−⟨u, C₁C₂C₃e⟩` equals `−⟨C₁C₂C₃u, e⟩`. ∎

*Checked (E1).*
- The member's demand, symbolically.
- The solve.
- `Σ_xe′(x) = Σ_xe(x) = H` as operators on `5³`.
- The symbol at `0` and at `π(1,1,1)`, and its series along `(1, 2, 3)`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 134 (open): the walker is the member's content only at leading order, with direction-dependent lattice corrections, and six species fail; block 129 (open): alpha/K supplied"
source_of_blocker_text: blocks 129 and 134 (open)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the transverse sector (block 120's open strict normalisation); nonuniform rates; an other-family referee (probes problem the-two-step-content-and-the-members-identity)"
conditional_surface_status: "exact at first order in the member's fields, at the closing ratio, with block 120's placement and the averaged energy; the walk, currents, placements, member and link supplied"
hypothetical_axiom_status: "the source link (the walker's two-step content as the member's source, placed as block 120 places it) is supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 62: the member, its stress coupling and placement.
  - Blocks 69 and 73: the two-step momentum and its reach-three current.
  - Block 74: the two-step current is every species' own stress.
  - Block 101: the quadratic action.
- **Opened, not landed.**
  - Block 112 (PR #9152): the identity, and the walker's exact failure with the site stress.
  - Block 120 (PR #9173): only the two-step current can be placed statically, through the φ-realisation. Its proof uses the same trigonometric identity for stationary states.
  - Block 134 (PR #9193): the leading-order result, its lattice corrections, and its species split.
- **Probes attempts.**
  - `the-dewitt-ratio-and-local-conservation` a2 (harvested as block 112) shows that content whose energy current is `c` times its momentum meets the identity iff `c = Kw̄²/(4α)`. Its "what would finish it" asks whether a bond-placed current satisfies the identity at every wave number.
  - `deferred-20260924-ledger` a1 (harvested as block 120) lists "beyond statics" as open.
- **In the literature.**
  - Noether's second theorem.
  - The contracted identity that makes a relabelling-invariant member demand a conserved source.
  - The comparator's single light cone.

  All reference only.
- **New here:**
  - T1: the dynamic identity, exact on `ℤ³` for every state;
  - T2: the common factor, and the averaged energy that supplies it;
  - T3: the no-go for the realisation without its transverse average;
  - T4: `α = K/4` from the source link, exactly, for every species.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: whether the source link, placed as block 120 places it, fixes `α/K` exactly. The obligations are:
- (O1) the content's identity (T1, T2);
- (O2) what fails (T3);
- (O3) the member and the conclusion (T4).

T1–T4 discharge them. Open: the transverse sector, nonuniform rates, and a referee.

## No-Go Discipline Gate

The note's negative sentence: without its transverse average, no placement of the energy makes block 120's realisation meet the member's identity; and block 62's site stress meets neither placement.

### N1 — Routes by which the sentence could fail or mislead
1. *Nonlocal placements.* A placement whose symbol depends on `k̄` is not a placement of a density. T3(c) covers only placements of the energy as a local density.
2. *Other currents.* Block 73 shows that the two-step momentum is the only covariant conserved one of reach two. Higher reach is not treated.
3. *Nonuniform rates.* The identity is at a uniform rate, which is first order in the member's fields.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, currents, placements, member and link.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics or time metric in the axioms | yes |
| blocks 54, 62, 69, 73, 74, 101 (landed) | the walk; the member; the two-step current | yes (restated) |
| block 120 (open) | the placement | yes (restated and executed here) |
| blocks 112, 134 (open) | the demand; the leading-order result | no (re-derived; placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the two-step content with the averaged energy meets the member's identity for every state iff `α = K/4`; the site stress and the untransverse realisation do not" | executed: exact operators over `ℚ(i)` on `5³`, `6³` and `9³` | executed: two sites of `5³`, the origin of `6³` and `9³`; totals on `5³` | executed: the beat's mechanism symbolically | executed: the member's demand; the failures; two `k̄` at one `q` | exact on `ℤ³` by support radius 4; first order in the fields |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository. It is not used: T4 reaches `α = K/4` from the source link. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The averaged energy is a new clause, so the result is bought with a choice."
  - *Reply:* The average has the same total and agrees with the site energy at long wavelength. By action and reaction, it is the clock seen through the same local average by which block 120 lets the walker see the strain.
  - With the site energy, T2 still gives one species-blind factor `1 − |q|²/2 + …`. So `α = K/4` holds for every species at leading order, without the average.

### N8 — Cross-cycle echo
- Block 62 left `α = K/4` unforced.
- Block 112 found the demand, and the site stress's exact failure.
- Block 120 placed the two-step current statically.
- Block 134 fixed `α = K/4` at leading order for the smooth species.
- This note fixes it exactly, for every state, with block 120's placement.

## Falsifiers

- A state of the walk for which the operator identity of T1 fails on `ℤ³`.
- A placement of the energy, as a local density, that repairs the untransverse realisation.
- A derivation of the member's demand at `β = −α` with a coefficient other than `Kw̄²/(4α)`.

## Boundaries and non-claims

- The walk, its currents and their placements, the member, its kinetic term and the source link are supplied.
- The result is at first order in the member's fields and at a uniform rate.
- Only the constraint and longitudinal equations are treated. The transverse equations impose no condition, and block 120's strict normalisation at `q ≠ 0` stays open.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 62, 69, 73, 74 and 101, restated. Block 120's placement, restated and executed. Blocks 112 and 134, placed.
- Named standard imports, at definition level:
  - Fourier analysis on the lattice;
  - trigonometric identities;
  - exact arithmetic over `ℚ(i)`.

## Review record

- **Who and when.** Supervisor-run block, the eighty-third since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own runner. It is not refereed by another model family. The probes problem `the-two-step-content-and-the-members-identity` poses the same question independently.
- **Before writing.**
  - Main was re-fetched, and blocks 54, 62, 69, 73, 74 and 101 were read as landed.
  - Block 120 was read on its branch.
  - The own prior-art check (memory, open PRs, probes attempts) found the static version (block 120 T4) and the open question "beyond statics", both credited above, but no dynamic identity.
- **Independence.** T1 is checked as an operator identity on tori, separately from T2's Fourier argument. Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_2026_09_25.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
