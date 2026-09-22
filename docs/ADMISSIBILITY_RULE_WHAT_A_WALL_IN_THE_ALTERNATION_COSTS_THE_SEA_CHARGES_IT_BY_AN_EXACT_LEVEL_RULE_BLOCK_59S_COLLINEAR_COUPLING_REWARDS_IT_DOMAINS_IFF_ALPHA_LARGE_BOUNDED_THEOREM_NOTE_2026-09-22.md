---
claim_id: admissibility_rule_what_a_wall_in_the_alternation_costs_the_sea_charges_it_by_an_exact_level_rule_block_59s_collinear_coupling_rewards_it_domains_iff_alpha_large_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN block 59's bond rates and bond law (open PR #8581; not adopted), block 84's alternation and balance (#8652), block 86's separability (#8660) and the sea of block 76 (#8611) taken as a comparator: exact symbolic spectra on the rings of 4, 8, 12; an exact concavity argument; block 59's law as an exact real-space quadratic form on the 4³ torus; the wall tension's zone average, its direct check on 8³ and 16³, and the criterion along the balance executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_what_a_wall_in_the_alternation_costs_sea_charges_by_level_rule_collinear_coupling_rewards_domains_iff_alpha_large_2026_09_22.py
---

# What a wall in the alternation costs: the sea charges it by an exact level rule, block 59's collinear coupling rewards it, and domains form iff α is large

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (an exact level rule on three rings, executed length-independent on longer ones and not proved in general; exact positivity by concavity; the law's wall reward exact; the tension and the criterion executed; nothing adopted or registered; unaudited)

This note works within block 59's bond rates and bond law, block 84's alternation and the sea as a comparator; it reports what a wall in the alternation costs the sea and the law, exactly, and when walls are favoured; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 84 (PR #8652) found that block 59's bond rates alternate below a threshold stiffness, and block 86 what the alternation's walls carry. This note asks what a wall costs — under the sea and under block 59's law — and so whether the alternation stays uniform or breaks into domains.

1. **An exact level rule (T1).** On an even ring, two sharp walls (one where two weak bonds meet, one where two strong bonds meet) replace exactly four levels of the one-axis operator, `±δ` and `±1`, by `0, 0, ±√(1 + δ²)`; every other level is unchanged (rings of 4, 8, 12, exact; rings of 16, 64, 256 to six places). So the sea's energy of the wall pair on a ring is `(1 + δ) − √(1 + δ²)`, positive and independent of the ring's length.
2. **The three-dimensional tension (T2).** By the rule and block 86's separability, a wall's sea energy per unit area is the transverse zone average of `√(δ² + e²) + √(1 + e²) − √(e²) − √(1 + δ² + e²)`, `e² = e_y² + e_z²`: positive at every transverse wave vector by the concavity of the square root; exactly `2√3 − √2 − 2` at `δ = 1`. Executed: `σ_sea = 0.00234, 0.01457, 0.02825, 0.03929, 0.04989` at `δ = 0.1, 0.3, 0.5, 0.7, 1`, the direct three-dimensional differences on `16³` agreeing; `σ_sea/δ² → 0.28` as `δ → 0`.
3. **The law rewards a wall (T3).** Block 59's law charges the uniform alternation `2(α + 2β)δ²` per bond (block 84 T2) and changes by exactly `−2αδ²` per unit area per wall: at a phase slip each of the two wall bonds loses one opposing collinear neighbour; the perpendicular and parallel couplings do not see the slip.
4. **When walls form (T4).** A wall's energy per unit area is `σ_sea(δ) − 2αδ²`: walls are favoured iff `α > σ_sea(δ)/(2δ²)` — between `2/100` and `3/100` at `δ = 1` (exact bounds), about `0.14` near the threshold. Along block 84's balance (executed): at `κ = α + 2β = 0.125, 0.12, 0.11, 0.10, 0.09` the alternation settles at `δ* = 0.10, 0.18, 0.33, 0.48, 0.64` and its walls are favoured iff `α > 0.117, 0.100, 0.076, 0.059, 0.044` — that is, iff the perpendicular coupling `β` carries less than about `0.004, 0.010, 0.017, 0.021, 0.023` of the stiffness.

So the uniform alternation is stable against domain formation only if enough of block 59's stiffness sits in the perpendicular coupling; if the stiffness is mostly collinear, the alternation prefers to break into domains — and, by block 86, the walls and their crossings then carry the lighter matter and the zero modes. In plain terms: whether the long-short pattern stays one pattern or shatters into patches depends on which neighbours a bond's clock listens to — the bonds in line with it push it to shatter, the bonds beside it hold it together.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 86 N1.2 / queue item 1: 'whether the balance of block 84 makes walls — their energy per unit area under the sea and block 59's law — is not examined'"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a wall costs the sea sigma_sea(delta) (exact level rule; positive by concavity) and is rewarded by the law 2 alpha delta^2: domains iff alpha > sigma_sea/(2 delta^2); next: a proof of the level rule on every even ring; the domain pattern when walls are favoured (wall density, period); whether anything in the lane constrains the split of block 59's stiffness between alpha and beta"
conditional_surface_status: "T1 exact on the rings of 4, 8, 12 and executed on 16, 64, 256; T2 by concavity given T1 and block 86; T3 exact on the 4^3 torus and by the local count on every torus; T4 as a criterion with the tension executed; the sea, the balance as a minimisation and the bond law's numbers are not derived"
hypothetical_axiom_status: "block 59's bond rates and law; the alternation; walls; the sea; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom and the Qubit axiom. Blocks 59, 76, 84, 86 (open PRs #8581, #8611, #8652, #8660) supply the bond rates and their law, the sea reading, the balance and the separability. Nothing is adopted here.

- **One-axis operator with walls.** `h = (1/2i)(tT − T†t)`, `t_x = 1 + δ s_x(−1)^x`, `s_x = +1` on the first half of the ring and `−1` on the second: two sharp walls, weak-weak and strong-strong.
- **Level rule.** The multiset of `E²` with walls against the one without.
- **Wall tension.** `σ_sea(δ) = ⟨√(δ² + e²) + √(1 + e²) − √(e²) − √(1 + δ² + e²)⟩` over the transverse zone, `e² = sin²k_y + δ²cos²k_y + sin²k_z + δ²cos²k_z`; by the rule and separability it is `[E_sea(two walls) − E_sea(uniform)]/(2L²)`.
- **Block 59's law as a quadratic form.** `F = −½Σ_b u_b(c₀u_b + αΣ_coll u + βΣ_perp u + γΣ_par u)`, `c₀ = −2α − 8β − 4γ`, the three neighbour classes of block 59 T3 (collinear 2, parallel 4, perpendicular 8); evaluated on the alternation with and without walls across `x`.
- **The balance (block 84).** `E(δ) + 6κδ²` per site, `κ = α + 2β`; `δ*(κ)` its minimiser.

That a soliton of a dimerised chain carries a length-independent energy and that a sharp slip of a dimerisation is a transparent defect for all but a few levels are properties of the model of Su, Schrieffer and Heeger; that the energy of a domain wall decides between a uniform order and a modulated one is the usual competition of surface and bulk energies; none is used as authority.

## Prior art and what is new

Block 84 T5 gave the two zero modes of a ring with two walls; block 86 the separability and the wall modes' form. New, inside the framework's vocabulary: the exact level rule (only four levels move); the closed form of the wall tension and its positivity; the law's exact reward `−2αδ²` for a slip, seen by the collinear coupling only; and the domain criterion along the balance. No gravitational claim is made.

## Exact target and obligation graph

Target: the cost of a wall. Obligations: (O1) the sea's cost on a ring; (O2) in three dimensions; (O3) the law's cost; (O4) the criterion. T1–T4 discharge O1–O4.

## Theorem T1 — the level rule

*Statement.* On the rings of 4, 8 and 12 with `δ = 3/10`, the squared spectrum of the one-axis operator with two sharp walls equals the wall-free one with two copies each of `δ²` and `1` removed and two copies each of `0` and `1 + δ²` added. Hence the negative branch's sum changes by `(1 + δ) − √(1 + δ²) > 0`, independent of the ring.

*Proof.* Exact eigenvalue multisets (family B); positivity from `(1 + δ)² − (1 + δ²) = 2δ`. The rule is verified exactly on three rings and to six places on rings of 16, 64 and 256 (control W1); a proof for every even ring is not given. ∎

## Theorem T2 — the wall tension in three dimensions

*Statement.* Given T1 and block 86 T1, a wall's sea energy per unit area is `σ_sea(δ)` as declared; its integrand is positive at every transverse wave vector; `σ_sea(1) = 2√3 − √2 − 2`.

*Proof.* The four arguments `e², e² + δ², e² + 1, e² + 1 + δ²` have `e² + (e² + 1 + δ²) = (e² + δ²) + (e² + 1)` and the inner pair is less spread, so the concavity of the square root gives `√(e² + δ²) + √(e² + 1) > √(e²) + √(e² + 1 + δ²)` (family C; exactly positive at the rational point `δ = 3/10, e² = 9/16`). At `δ = 1`, `e² = 2` at every wave vector. ∎

*Executed.* `σ_sea = 0.000028, 0.000640, 0.002336, 0.014571, 0.028246, 0.039292, 0.049888` at `δ = 0.01, 0.05, 0.1, 0.3, 0.5, 0.7, 1` (transverse grids to `512²`, settled); the direct three-dimensional difference on `16³` gives `0.014575, 0.028246, 0.039292, 0.049888` at `δ = 0.3, 0.5, 0.7, 1` (finite-size excess at small `δ`); `σ_sea/δ²` rises to `0.275` at `δ = 0.01`.

## Theorem T3 — the law rewards a slip

*Statement.* On the `4³` torus block 59's law gives the uniform alternation `3N·2(α + 2β)δ²` and changes by exactly `−2αδ²` per unit area per wall when the alternation has two walls across `x`; `β` and `γ` do not enter the change.

*Proof.* Exact evaluation of the quadratic form (family D) with `(α, β, γ) = (1/7, 1/11, 1/5)` and with each coupling alone. Locally: a bond's collinear term is `αu_b(u_{b+1} + u_{b−1})`, `−2αδ²` in the alternation and `0` at a slip, one such bond per transverse site on each side of the wall; the perpendicular neighbours of a bond along `x` are bonds along `y, z`, whose pattern the slip does not touch, and the parallel neighbours of a wall bond are wall bonds with the same sign. ∎

## Theorem T4 — when walls are favoured

*Statement.* The energy of a wall per unit area is `σ_sea(δ) − 2αδ²`. Walls are favoured iff `α > σ_sea(δ)/(2δ²)`; at `δ = 1` the threshold `(2√3 − √2 − 2)/2` lies between `2/100` and `3/100` exactly.

*Proof.* T2 and T3; the bounds by exact comparison of algebraic numbers (family E). ∎

*Executed (control W4).* Along block 84's balance: `κ = 0.125, 0.12, 0.11, 0.10, 0.095, 0.09` gives `δ* = 0.098, 0.183, 0.332, 0.480, 0.558, 0.642` and `α_c = 0.117, 0.100, 0.076, 0.059, 0.051, 0.044`; with `κ` held, walls are favoured iff `β < 0.004, 0.010, 0.017, 0.021, 0.022, 0.023`.

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block87_wall_cost.py`, output in `.out.txt`; disjoint machinery: floating-point spectra and zone sums).

*W1.* Wall-pair energies on rings of 16, 64, 256: `0.095012, 0.255969, 0.381966, 0.554638` at `δ = 0.1, 0.3, 0.5, 0.9`, equal to `(1 + δ) − √(1 + δ²)` to six places and independent of the ring.

*W2.* `σ_sea(δ)` on transverse grids of side 64, 256, 512 (settled to six places) and directly on `8³`, `16³`: table above; `σ_sea/(2δ²) = 0.138, 0.128, 0.117, 0.081, 0.057, 0.040, 0.025` at `δ = 0.01, 0.05, 0.1, 0.3, 0.5, 0.7, 1`.

*W3.* Block 59's law on `8³` with random couplings: wall energy per unit area `−0.052588, −0.000952, −0.003994` against `−2αδ²` to six places.

*W4.* The criterion along the balance, as in T4.

## No-Go Discipline Gate

The note's negative sentences: the sea never rewards a wall; the perpendicular and parallel couplings do not see a slip.

### N1 — Routes by which the sentences could fail or mislead
1. *The level rule* is exact on three rings and executed on three more; not proved for every even ring. T2 and T4 depend on it.
2. *Sharp walls only*; a smooth wall or a wall of another kind (e.g. a slip on two axes at once) could have a different tension.
3. *The domain pattern* when walls are favoured is not computed (wall density, period); only the sign of a single wall's energy.
4. *The sea* is a comparator (block 78); the crowd's wall tension is not computed (block 85 gives the crowd's bulk gain only).
5. *The split of the stiffness* between `α` and `β` is not fixed by anything in the lane.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Even rings and tori; `δ = 3/10` in the exact checks; `(α, β, γ) = (1/7, 1/11, 1/5)` in the exact law evaluation (the reward is linear in `α`, checked coupling by coupling).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice axiom (product of rings); the coin | yes (premise) |
| block 59 (open PR #8581) | the bond rates and the three-number law | yes (restated) |
| blocks 84, 86 (open PRs #8652, #8660) | the balance; separability and the wall modes | yes (placed) |
| block 76 (open PR #8611), block 78 (#8613) | the sea as comparator | yes (comparator) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "level rule; positive tension; law's reward 2 alpha delta^2; domains iff alpha > sigma/(2 delta^2)" | executed: level multisets on three rings; the quadratic form bond by bond | executed: the reward coupling by coupling | executed: the integrand at a rational point and at delta = 1; control grids | executed: the criterion's exact bounds at delta = 1 | T1 on three rings; T2 by concavity; T3 by the local count; T4 as a criterion

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A criterion on unfixed numbers decides nothing." Reply: it decides the shape of the phase diagram in the lane's own variables — the alternation is uniform for `β`-dominated stiffness and shatters for `α`-dominated — and it turns block 86's zero modes from a curiosity into a consequence of one number. Second objection: "The level rule is a coincidence of small rings." Reply: it holds to six places on rings of 256 as well; the note says a general proof is missing.

### N8 — Cross-cycle echo
Block 84: the alternation and its eight phases. Block 86: what walls carry. Here: what walls cost and when they form.

## Falsifiers

- A ring of 4, 8 or 12 whose two-wall squared spectrum differs from the level rule.
- A transverse wave vector at which the tension's integrand is negative.
- A coupling `β` or `γ` that changes the law's wall energy, or a wall energy differing from `−2αδ²` per unit area.
- A `δ` at which `σ_sea(δ)/(2δ²)` at `δ = 1` lies outside `(2/100, 3/100)`.

## Boundaries and non-claims

Sharp walls; the level rule unproved in general; no domain pattern; the crowd's wall tension not computed; the stiffness split not fixed. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice and Qubit axioms. Blocks 59, 76, 78, 84, 86 (open PRs): restated or placed.
- Named standard imports at definition level: exact eigenvalue multisets; concavity of the square root; quadratic forms; zone sums and dense spectra for the control.

## Review record
Supervisor-run block, the thirty-fifth of the source-link direction; the sixth after the rest-energy panel. Lens pass, in writing, by the supervisor: a foundations lens — the sea is a comparator and the criterion is on supplied numbers, both said; a rigour lens — the level rule was found from the length-independence of executed wall energies and then checked as an exact multiset identity on three rings before being used; the tension's sign was made a concavity argument rather than a numerical observation; the law's reward was checked coupling by coupling and by a local count; a first control formula for the tension had the wrong sign and factor and was corrected against the direct three-dimensional difference. Mutation census: six mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_what_a_wall_in_the_alternation_costs_sea_charges_by_level_rule_collinear_coupling_rewards_domains_iff_alpha_large_2026_09_22.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
