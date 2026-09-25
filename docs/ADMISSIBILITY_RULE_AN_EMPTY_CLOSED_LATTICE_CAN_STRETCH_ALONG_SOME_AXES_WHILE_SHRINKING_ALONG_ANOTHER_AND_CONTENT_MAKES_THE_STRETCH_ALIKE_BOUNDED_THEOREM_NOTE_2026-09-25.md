---
claim_id: admissibility_rule_an_empty_closed_lattice_can_stretch_along_some_axes_while_shrinking_along_another_and_content_makes_the_stretch_alike_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 61's three-length kinetic family and block 60's homogeneous model, with the member's kinetic term (blocks 124 and 134-136), all as landed on main, and block 146 (open) placed; uniform stretches of a closed lattice, with the site volume l1 l2 l3 supplied as the homogeneous model's volume factor; unit rate. (T1) exact: on a uniform diagonal stretch the member's kinetic term is block 61's M1 sum lamdot^2 + M2 sum_{i<m} lamdot_i lamdot_m with M1 = 4(alpha + beta) and M2 = 8 beta, so at the closing ratio only -8 alpha sum_{i<m} lamdot_i lamdot_m survives; on the isotropic stretch this is block 146's c_k = -24 alpha. (T2) exact: an empty closed lattice has uniform motions l_i = t^(p_i) with sum p = sum p^2 = 1 (an exact rational family), in which some length shrinks or stays (under reversing time the growing and shrinking lengths swap, so the lengths never all grow, or all shrink, together); it has no isotropic motion. (T3) exact: with rest content m0 per site, the family 8 alpha V (S - lamdot_k) = m0 t + D_k, V = (3 m0 t^2/2 + D t)/(16 alpha), keeps the equations and the constraint on the cone D0^2 + D1^2 + D2^2 = 2(D0 D1 + D0 D2 + D1 D2), and every lamdot_k t tends to 2/3 as t -> +oo and as t -> -oo: with content the stretch is alike wherever the lattice is large, block 146's |t|^(2/3); the family is closed under reversing time (t -> -t with D_k -> -D_k), so the equations fix no direction. The supervisor's own derivation (Claude Opus 5.5); not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_an_empty_closed_lattice_can_stretch_along_some_axes_while_shrinking_along_another_and_content_makes_the_stretch_alike_2026_09_25.py
---

# An empty closed lattice can stretch along some axes while shrinking along another; with content the stretch is alike wherever the lattice is large

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 60's homogeneous model with three lengths and the landed kinetic term, for uniform stretches of a closed lattice, with the volume factor supplied; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 60 and 61 as landed on main (the homogeneous kinetic model and the three-length kinetic family), with the member's kinetic term of blocks 124 and 134 to 136 as landed and block 146 placed; it reports how an empty or filled closed lattice can stretch unequally along its axes; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 146 (open) treated the lattice stretching alike along its three axes. Its uniform motions with three different lengths, the rest of the zero modes, were left open. Block 61 (landed) gave the kinetic terms for three lengths per site.

- **T1: only the cross term.** On a uniform stretch with three lengths, the member's kinetic term is block 61's `M₁Σλ̇_j² + M₂Σ_{i<m}λ̇_iλ̇_m` with `M₁ = 4(α + β)` and `M₂ = 8β`. At the closing ratio `M₁ = 0`: only the cross term `−8αΣ_{i<m}λ̇_iλ̇_m` survives. On the alike stretch it is block 146's `c_k = −24α`.
- **T2: an empty lattice can move.** With no content, the lattice has uniform motions `ℓ_i = t^{p_i}` with `Σp_i = Σp_i² = 1`. In every such motion some length shrinks or stays fixed while the others grow; run backwards in time, the growing and shrinking lengths swap. So the lengths never all grow, or all shrink, together. An empty lattice cannot stretch alike.
- **T3: with content the stretch is alike where the lattice is large.** With content at rest there is an exact family of motions. Toward either end of its time range, where the lattice is large, every length goes as `|t|^{2/3}`: block 146's alike stretch. The family is closed under reversing time, so the equations do not say which end is later.

In plain terms: an empty lattice does not have to sit still. It can stretch along two directions while shrinking along the third, in a fixed pattern of rates, because the member's kinetic energy for such motions is zero. What it cannot do, when empty, is stretch equally in all directions. Put content in, and the unevenness fades as the lattice grows: wherever the lattice is large it stretches alike in every direction. The equations do not fix a direction of time, so this compares large and small lattices, not early and late.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The member, its kinetic term, the volume factor and the content are supplied clauses. Nothing is adopted.
- **Three lengths** (block 61 as landed): `ℓ_j = e^{λ_j}`, one per axis. The kinetic family `T₂ = M₁Σλ̇_j² + M₂Σ_{i<m}λ̇_iλ̇_m`.
- **The member's kinetic term** (blocks 124 and 134–136 as landed): `α tr(Ḣ²) + β(tr Ḣ)²` at the closing ratio `β = −α`.
- **The homogeneous model with three lengths.** This is block 60 T5(b) with three lengths: `−8α V Σ_{i<m}λ̇_iλ̇_m/w − w m`, with `V = ℓ₁ℓ₂ℓ₃`, the site's volume.
  - The volume factor `V` is supplied. On the alike stretch it is block 129's `ℓ³`.
  - Stationarity in `w` is the constraint `8αVΣ_{i<m}λ̇_iλ̇_m = m`. Time is labelled so that `w = 1`.
- **Standard imports.** Exact symbolic arithmetic.

## Theorem T1 — only the cross term

*Statement.* On `h_ii = 2λ_i` (a uniform diagonal stretch), `α tr(Ḣ²) + β(tr Ḣ)² = 4(α + β)Σλ̇_j² + 8βΣ_{i<m}λ̇_iλ̇_m`. At `β = −α` this is `−8αΣ_{i<m}λ̇_iλ̇_m`, and on `λ_j = λ` it is `−24αλ̇²`.

*Proof.* Direct (runner B1, E1). ∎

## Theorem T2 — an empty lattice can move

*Statement.*
- (a) With `m = 0`, `ℓ_i = t^{p_i}` solves the constraint and the three equations whenever `Σp_i = 1` and `Σ_{i<m}p_ip_m = 0`, that is `Σp_i² = 1`. The family `p = (−u, 1 + u, u(1 + u))/(1 + u + u²)`, `u > 0`, is an exact rational one.
- (b) If all `p_i > 0`, then `Σ_{i<m}p_ip_m > 0`. So in every such motion some length shrinks or stays fixed. Since `Σp_i = 1`, not all `p_i` are negative. Under reversing time, `ℓ_i = (−t)^{p_i}`, the roles swap.
- (c) An alike stretch needs `3λ̇² = 0`. An empty lattice has no alike motion.

*Proof.* (a) Substitution (runner C1). (b) `(Σp)² − Σp² = 2Σ_{i<m}p_ip_m` (runner C2). (c) Runner C1. ∎

## Theorem T3 — with content, the stretch is alike where the lattice is large

*Statement.* With rest content `m₀` per site, take `V = (3m₀t²/2 + Dt)/(16α)` with `D = D₀ + D₁ + D₂`, `S = V̇/V`, and `λ̇_k = S − (m₀t + D_k)/(8αV)`.
- Then `Σλ̇_k = S`, each equation `d/dt[8αV(S − λ̇_k)] = m₀` holds, and the constraint holds exactly on the cone `D₀² + D₁² + D₂² = 2(D₀D₁ + D₀D₂ + D₁D₂)`.
- As `t → +∞` and as `t → −∞`, every `λ̇_k t → 2/3`: where the lattice is large the stretch is alike, block 146's `|t|^{2/3}`.
- The family is closed under reversing time: `t → −t` with `D_k → −D_k` turns each `λ̇_k` into `−λ̇_k`. So the equations fix no direction.

*Proof.* The equation for `λ_k`, with the constraint, is `d/dt[8αV(S − λ̇_k)] = m₀`. Summing gives `16αV̇ = 3m₀t + D`. The rest is substitution, limits and the substitution `t → −t`, `D_k → −D_k` (runner D1). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 146 (open): the zero modes with three different lengths (uniform shear) were left open"
source_of_blocker_text: block 146 (open); the landing review's zero-mode residual
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the volume factor for three lengths from the member's nonlinear order; top-speed content with three lengths; an other-family referee"
conditional_surface_status: "uniform stretches of a closed lattice; the volume factor supplied; unit rate"
hypothetical_axiom_status: "the member, its kinetic term, the volume factor and the content are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 60: the homogeneous model.
  - Block 61: three lengths per site and their kinetic family.
  - Blocks 124 and 129: the kinetic family `c_k = 12α + 36β`, and the volume power.
  - Blocks 134–136: `α = K/4` and the closing ratio.
- **Opened, not landed.** Block 146 (the alike stretch).
- **Probes.** Refill u asks for anisotropic uniform stretches. No attempt yet.
- **In the literature.** Kasner's exponents for empty uniform space with three unequal scale factors, and the smoothing of such motions by matter (Heckmann and Schücking). Reference only.
- **New here:**
  - T1: at the closing ratio only the cross term survives, in block 61's family.
  - T2: an empty closed lattice can move, but never alike.
  - T3: with rest content the stretch is alike wherever the lattice is large, in either direction of time.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: the uniform motions of a closed lattice with three lengths. The obligations are:
- (O1) the kinetic term (T1);
- (O2) the empty lattice (T2);
- (O3) rest content (T3).

T1–T3 discharge them.

## No-Go Discipline Gate

The note's negative sentence: an empty closed lattice has no alike motion, and in its uniform motions the lengths never all grow, or all shrink, together.

### N1 — Routes by which the sentence could fail or mislead
1. *The volume factor* `ℓ₁ℓ₂ℓ₃` is supplied. It is block 129's `ℓ³` on the alike stretch.
2. *Uniform stretches only.* Diagonal stretches of a closed lattice; no shear between axes.
3. *Content.* Rest content only in T3.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied member, kinetic term, volume factor and content.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 60, 61 (landed) | the homogeneous model; three lengths | yes (restated) |
| blocks 124, 129, 134–136 (landed) | the kinetic term and ratio | yes (restated) |
| block 146 (open) | the alike stretch | no (comparison) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "an empty closed lattice moves as `t^{p_i}` with `Σp = Σp² = 1` and never alike; with content the stretch is alike wherever the lattice is large" | executed: the kinetic term on the stretch | executed: the three-length model's equations | executed: the exponent family; the sign argument | executed: the content family, its cone and its limit | uniform stretches; the volume factor supplied |

### N6 — Partial-closure paths and primitive scan
No approved primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "These are the comparator's uniform motions, rewritten."
  - *Reply:* They are, and the note says so. What the lane adds is that the member's own numbers (`M₁ = 0` at the closing ratio) are what allow an empty lattice to move at all, and that its landed three-length family gives them.

### N8 — Cross-cycle echo
- Block 60: uniform motion with content.
- Block 146: the alike stretch at the pull's coupling.
- This note: the uneven stretches, empty and with content.

## Falsifiers

- A uniform diagonal stretch on which the member's kinetic term differs from `4(α + β)Σλ̇² + 8βΣλ̇_iλ̇_m`.
- An empty uniform motion with every length growing, or every length shrinking.
- An error in the runner's substitutions or limits.

## Boundaries and non-claims

- Uniform diagonal stretches of a closed lattice; the volume factor supplied; unit rate.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 60, 61, 124, 129 and 134–136 (landed), restated. Block 146 (open), for comparison.
- Named standard imports: exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the ninety-sixth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found block 61's kinetic family and no treatment of uniform uneven stretches.
- **After opening (a panel's report).** A three-lens panel (programme strategy, lattice field theory, gravitation theory; all three Claude Opus 5.5 subagents, the same model family as the supervisor, so not an independent check) noted that "content makes the stretch alike" assumed a direction of time the equations do not supply. The equations are even under reversing time, and the content family is closed under it (runner D1 now checks this and both limits). What is shown is that the stretch is alike wherever the lattice is large. The title in the body is corrected; the file name keeps the original wording.
- **Independence.** Mutation census: five mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_an_empty_closed_lattice_can_stretch_along_some_axes_while_shrinking_along_another_and_content_makes_the_stretch_alike_2026_09_25.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
