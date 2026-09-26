---
claim_id: admissibility_rule_relabellings_in_time_whose_clock_profile_varies_in_space_need_no_new_term_the_walkers_own_generator_moves_it_as_the_members_shift_changes_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 62's framed coupling at long wavelength on smooth zero-corner states, on half-densities, with the frame built from the member's lengths (the symmetric e = g^(1/2) = 1 + eta, static) plus block 158's (1/8) eps.C, the lapse entering as (1/2){n, H_s} and the shift as (1/2){N^j, -i d_j} plus block 163's frame-rotation coupling (1/4) sigma_c eps_cab (e (d_t + L_N) E)_ab, zero background lapse and shift, and a relabelling in time with a clock profile xi0 that varies in space, which moves the walker by its own smeared generator exp(-i u (1/2){xi0, H_s}) (the time shift with the coin's boost; unitary): (T1) at first order the moved walker is exactly the walker with the new shift N' = u grad xi0, nothing left; (T2) at order strain x relabelling the principal part is the shift term with the metric-raised gradient N'^k = u g^{jk} d_j xi0, and the remainder is exactly block 163's coupling of that shift, so no new term is needed (all 600 basis pairs of jets); (T3) without block 163's coupling a residual remains, and block 158's (1/8) eps.C does not enter at this order. Profiles that vary in time add the lapse's own term exactly. Exact over the Gaussian rationals. A background lapse or shift, second order in the strain and the lattice (block 150's defect at higher wave numbers) are not examined. The supervisor's own derivation; unrefereed; nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_relabellings_in_time_whose_clock_profile_varies_in_space_need_no_new_term_2026_09_26.py
---

# Relabellings in time whose clock profile varies in space need no new term: the walker's own generator moves it as the member's shift changes

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact at leading order in the spacing, for smooth states of the zero-corner species, with zero background lapse and shift, through first order in the strain; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 62, 101, 136 and 150 as landed on main (the walker's framed coupling, the rate as a multiplier, the shift and the clock rules); it reports what relabellings in time with clock profiles that vary in space require of the walker's coupling, through first order in the strain, at leading order in the spacing; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Programme T's last open piece was the lapse sector. Relabellings in time whose clock profile varies from place to place are required only under reading E (addendum 44). This note asks whether they need anything more of the walker's coupling than blocks 158 and 163 already give.

They do not.
- **T1: first order.** A relabelling in time with profile `ξ⁰` moves the walker along its own evolution by `ξ⁰`. The time shift and the coin's boost together form the unitary `exp(−iu·½{ξ⁰, H_s})`. The moved walker is then exactly the walker with the member's new shift `u∇ξ⁰`.
- **T2: strain times relabelling.**
  - The new shift carries the lengths' inverse metric, `g^{jk}∂_jξ⁰`, as the member's law says.
  - What remains is exactly block 163's coupling of that shift, the coin's coupling to the frame's rotation rate relative to the flow.
  - So no new term is needed.
- **T3: block 163's coupling is needed here too.** Without it a remainder is left. Block 158's `(1/8)ε·C` does not enter at this order.

In plain terms: when the clocks are reset by different amounts in different places, the walker follows correctly using only the couplings already found for relabellings in space. Two different kinds of relabelling asked for the same coin coupling. That is a check that the pieces fit. Block 150 found the lattice's clock rules match only through second order in the profiles' wave numbers. So this is the continuum statement, and the lattice defect sits at higher order.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The walker's coupling, the member's relabellings and the comparator are supplied clauses. Nothing is adopted.
- **The walker** (blocks 62, 101, 136, 158, 163).
  - The spatial part is `H_s = H_f[E] + (1/8)ε·C`, on the lengths' symmetric frame (static here).
  - With lapse and shift: `H = ½{1 + n, H_s} + ½{N^j, −i∂_j} + V₁₆₃(N)`, where `V₁₆₃ = ¼σ_c ε_cab (e(∂_t + L_N)E)_ab` (block 163, pushed).
- **Block 150** (landed): "the walker's clocks close for a uniform lapse, but not for all pairs." On the lattice they match through second order in the profiles' wave numbers.
- **Relabellings in time.**
  - A profile `ξ⁰` moves the walker along its evolution by `uξ⁰`: the unitary `U = exp(−iu·½{ξ⁰, H})`.
  - At first order, `−iu·½{ξ⁰, H} = −iuξ⁰H − ½u σ·E∇ξ⁰` for flat parts. That is the time shift with the coin's boost, and it keeps the counting norm.
  - The member's fields move by `n′ = n + uξ̇⁰` and `N′ = N + u g⁻¹∇ξ⁰` (the sign of the shift as in block 163), and the static lengths do not move.
- **Standard imports, named at definition level.**
  - Commutators of differential operators with matrix coefficients.
  - The product rule of the coin's matrices.
  - Polarization of bilinear identities.
  - Exact arithmetic.

## Theorem T1 — first order

*Statement.* With zero background lapse and shift and flat lengths, `U H_s U† = H_s + ½{u∇ξ⁰, −i∂} + O(u²)` exactly: the moved walker is the walker with the new shift `u∇ξ⁰`.

*Proof.* `U H U† − H = −iu[½{ξ⁰, H}, H] = −(iu/2)[ξ⁰, H²]`, since `[½{ξ⁰, H}, H] = ½[ξ⁰, H²]`. For the flat walk `H² = −Δ`, and `−(iu/2)[ξ⁰, −Δ] = ½{u∇ξ⁰, −i∂}`. Checked for all basis profiles (runner B1). ∎

## Theorem T2 — strain times relabelling

*Statement.* At order `u·η`, `−(iu/2)[ξ⁰, H_s²] = ½{uN′, −i∂} + V₁₆₃(uN′)` with `N′^k = g^{jk}∂_jξ⁰`. That holds on all 600 basis pairs of strain jets and profile jets. Profiles that vary in time add `u·½{ξ̇⁰, H_s}`, which is the lapse coupling of `n′ = uξ̇⁰` exactly.

*Proof.* `H_s² = A_jk∂_j∂_k + B_k∂_k + C`, with `A_jk = M_jM_k`. Then `[ξ⁰, H_s²]` is a first-order operator:
- its principal part gives `N′^k = −½Σ_j(A_jk + A_kj)∂_jξ⁰ = g^{jk}∂_jξ⁰`;
- its remainder is compared with the target at a point, with generic jets (runner C1).

For profiles varying in time, `i(∂_tU)U† = u·½{ξ̇⁰, H}` at first order. ∎

## Theorem T3 — block 163's coupling is needed here too

*Statement.*
- Without `V₁₆₃`, the remainder at order `u·η` is nonzero on 18 of the 600 basis pairs.
- With or without block 158's `(1/8)ε·C`, the result at this order is the same.

*Proof.* Runner D1 and D2. `(1/8)ε·C` is second order in the strain, so its commutator term is third order. ∎

## What this settles and what it does not

- **Programme T now stands as follows.** Through first order in the strain, at leading order in the spacing, the walker's coupling to the member's lengths, lapse and shift keeps every relabelling of both readings:
  - relabellings in space, fixed or varying in time (blocks 158 and 163);
  - relabellings in time with any clock profile (this note).

  The coupling is the framed walk with `(1/8)ε·C` and with the coin's coupling to the frame's rotation rate. It has the comparator's form.
- **Reading E at leading order.** Its clock profiles that vary in space cost the walker nothing new at this order. The owner's reading question therefore matters for walkers only beyond leading order in the spacing, where block 150 found the lattice clock rules fail at third order in the profiles' wave numbers, and for the records' books (blocks 151–154).
- **Not settled.**
  - A background lapse or shift.
  - Second order in the strain.
  - The lattice.
  - The other seven species.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "programme T, lapse sector: relabellings in time whose clock profile varies in space (reading E)"
source_of_blocker_text: decision-record addendum 49 (the lapse sector left open)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a background lapse and shift; second order in the strain; the lattice; an other-family referee of blocks 158, 163 and this note"
conditional_surface_status: "leading order in the spacing; zero background lapse and shift; through first order in the strain; smooth zero-corner states"
hypothetical_axiom_status: "the walker's coupling, the member's relabellings and the comparator are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 150: the lattice clock rules, exact for uniform profiles and through second order otherwise.
  - Block 101: the rate as a multiplier.
  - Block 136: the shift.
- **Pushed blocks** (the supervisor's; unrefereed): 158 (`(1/8)ε·C`) and 163 (the frame's rotation-rate coupling).
- **In the literature.**
  - The algebra of smeared energy densities that the comparator's constraints satisfy, with the metric-raised gradient in its shift (Dirac; Teitelboim).
  - The spinor's boost under a change of slicing (Weyl).
  - Reference only.
- **New here.**
  - The lapse sector through first order in the strain, which needs no new term.
  - The cross-check: the coupling that relabellings in space demanded in block 163 is exactly what relabellings in time demand.
- **Provenance.** The supervisor's own derivation, using the point-jet machinery of blocks 158 and 163. Unrefereed.

## Exact target and obligation graph

Target: programme T's lapse sector. The obligations are:
- (O1) the premise, block 150 (A3);
- (O2) first order (B1);
- (O3) strain times relabelling (C1);
- (O4) necessity of block 163's coupling (D1, D2).

The strongest missing step is a background lapse and shift.

## No-Go Discipline Gate

The note's negative sentences:
- without block 163's coupling the walker misses relabellings in time at order strain times relabelling;
- no new term is needed at this order.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The time relabelling does not act as the smeared generator.* The unitary form is fixed by keeping the counting norm, which is the boost's role. Declared as a premise and checked through its consequences (B1, C1). ATTEMPTED.
2. *The shift the member moves by differs from the walker's.* Both carry the metric-raised gradient (C1). ATTEMPTED.
3. *Block 163's coupling is superfluous here.* Without it, 18 pairs fail (D1). ATTEMPTED.

Scope left open:
- a background lapse and shift;
- second order in the strain;
- the lattice.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- "Background" refers only to the declared zero lapse and shift.
- The unitary action is a declared premise.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 62, 101, 136, 150 (landed) | the coupling, the lapse, the shift, the clock rules | yes (150 quoted, A3) |
| blocks 158, 163 (pushed, unrefereed) | the walker's terms | yes |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the lapse sector needs no new term; block 163's coupling is needed" | executed: the commutator at a point | executed: 10 basis profiles | executed: 600 basis pairs | executed: with and without 163 and 158 | not executed: background fields; second order; lattice |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Moving the walker along its own evolution is circular."
  - *Reply:* It is the definition of a relabelling in time, and the content is the check.
  - The shift the member moves by, `g⁻¹∇ξ⁰`, and the coupling it then needs are independent inputs.
  - They could have disagreed with the walker's own commutator, and they do not.

### N8 — Cross-cycle echo
- Block 150: the lattice clock rules.
- Block 163: relabellings in space that vary in time need the frame's rotation-rate coupling.
- This note: relabellings in time need the same coupling and nothing new.

## Falsifiers

- A basis pair of jets with a nonzero remainder when block 163's coupling is included.
- A principal part other than the metric-raised gradient.

## Boundaries and non-claims

- Leading order in the spacing.
- Smooth zero-corner states.
- Zero background lapse and shift.
- Through first order in the strain.
- Not refereed.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 62, 101, 136 and 150 (landed), restated and quoted.
- Named standard imports, at definition level:
  - commutators of differential operators;
  - the product rule of the coin's matrices;
  - polarization;
  - exact arithmetic;
  - the algebra of the comparator's constraints (Dirac; Teitelboim), as a comparator.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-26 evening, during the owner's 12-hour campaign. It closes programme T's last open sector at this order.
- **Before writing.** The own prior-art check covered memory, open PRs, main and the probes. It found block 150 (lattice clock rules), blocks 158 and 163, and refill z's open time-sector task, which has no attempt yet.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_relabellings_in_time_whose_clock_profile_varies_in_space_need_no_new_term_2026_09_26.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
