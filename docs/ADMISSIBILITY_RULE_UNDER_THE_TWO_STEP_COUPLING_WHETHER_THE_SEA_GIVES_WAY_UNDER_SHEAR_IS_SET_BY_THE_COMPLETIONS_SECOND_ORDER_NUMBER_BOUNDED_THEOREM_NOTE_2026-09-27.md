---
claim_id: admissibility_rule_under_the_two_step_coupling_whether_the_sea_gives_way_under_shear_is_set_by_the_completions_second_order_number_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed, with a per-axis finite-stretch completion in block 176's family (l F = sin k (1 - q sin^2 k); pushed), written q = -lam + q2 lam^2 + O(lam^3) with lam = log l, and the filled negative band of the massless walk counted as energy (block 147's first reading), at second order in a volume-preserving diagonal stretch (lam_1 + lam_2 + lam_3 = 0): (T1) per axis F = s - lam s c^2 + lam^2 s(1/2 - (1 + q2) s^2) + O(lam^3), and block 69's linear completion and block 176's smooth completion both have q2 = -1/2; (T2) the sea's second-order energy per site is E2 = -(sum lam^2/3)[A/2 - (1 + q2) B] - I, with A = <|s|>, B = <sum_a s_a^4/|s|>, I = <|s x w|^2/(2|s|^3)>, w_a = s_a c_a^2 lam_a; (T3) so the sea gives way (E2 < 0) iff q2 < q2* = -1 + (A/2 + 3I/sum lam^2)/B, a number independent of the stretch's direction; q2* > -1/2 on the infinite lattice and on the tori of side 6 and 8, and q2* = -1/2 on side 4; every completion with q2 <= -1/2, the two named ones included, gives way; block 176's admissibility does not constrain q2; (T4) the frame's per-axis stretch gives -(sum lam^2/6)A - I_frame < 0 (the sign of blocks 155 and 167). Off-diagonal shears are not treated (no completion is supplied for them). The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_under_the_two_step_coupling_whether_the_sea_gives_way_under_shear_2026_09_27.py
---

# Under the two-step coupling, whether the sea gives way under shear is set by the completion's second-order number

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 69 as landed and block 176's family; blocks 155, 167 and 180 are placed; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within block 69 as landed on main (the two-step coupling of the walk to a uniform strain), with block 176's reach-three completion family, and asks whether the filled sea still gives way under shear when the walk is coupled as the member's source requires; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 155 (open PR #9289) and 167 (pushed) found that the walkers' filled sea, if counted as energy, loses energy under every shear. So member plus sea gives way to long shear waves at every `K`. That is the worked consequence of the third-column item "whether the member sees the sea". Both computed it with block 62's frame, which block 120 excluded as a source for non-uniform modes. A same-family panel therefore marked the consequence conditional. This note re-derives it for volume-preserving diagonal stretches under block 69's two-step coupling.

- **T1: the stretch to second order.** For block 176's family, with `q = −λ + q₂λ²` and `λ = log ℓ`, each axis stretches as `F = s − λ s c² + λ² s(1/2 − (1 + q₂)s²)`. Block 69's linear completion and block 176's smooth completion both have `q₂ = −1/2`.
- **T2: the sea's second-order energy.** Under `λ₁ + λ₂ + λ₃ = 0`, `E₂ = −(Σλ²/3)[A/2 − (1 + q₂)B] − I`, where:
  - `A = ⟨|s|⟩`;
  - `B = ⟨Σ s⁴/|s|⟩`;
  - `I ≥ 0` is the interband term.
- **T3: a threshold.** The sea gives way iff `q₂ < q₂*`. `q₂* > −1/2` on the infinite lattice, so every completion with `q₂ ≤ −1/2` gives way, the two named ones included. Block 176's admissibility band does not constrain `q₂`.
- **T4: the frame for comparison.** The frame's stretch always gives way, as blocks 155 and 167 found.
- **T5: the massive sea too.** With block 139's staggered mass the same threshold structure holds, again above `−1/2`.

In plain terms: under the walk's own coupling, whether a lattice full of walkers gives way under a gentle shear depends on one number in how the coupling continues to larger stretches. For every continuation written down so far, it gives way, as the earlier notes found with the frame. A continuation that bends more strongly at second order would hold it.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Block 69 is used as landed on main.

- **The coupling** (block 69), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`". Also quoted: "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
- **The completion** (block 176, pushed). Per axis `ℓ_a F_a = sin k_a(1 − q(ℓ_a) sin² k_a)`, admissible iff `q ≥ −1/6`. Here `q(ℓ) = −λ + q₂λ² + O(λ³)`, `λ = log ℓ`; the first coefficient is block 69's.
- **The sea** (block 147's first reading). The filled negative band of the massless walk, counted as energy. Its energy per site is `−⟨|F(k)|⟩` over the zone.
- **The stretch.** Diagonal, `ℓ_a = e^{λ_a}`, volume-preserving: `Σλ_a = 0`. Off-diagonal shears need a completion off the axes, which block 176 does not supply. They are not treated.
- **Placed.**
  - Blocks 155 (open PR #9289) and 167 (pushed): the frame's results.
  - Block 180 (pushed): the first-order stretch law under the two-step coupling.
  - Block 182 (pushed): covariance and the completion.
- **Notation.** `s_a = sin k_a`, `c_a = cos k_a`, `|s| = E`, `w_a = s_a c_a² λ_a`. `⟨·⟩` is the zone average over modes with `E > 0`.

Second-order energy of an occupied band under a perturbation splits into a diagonal part and an interband part. That split is the standard Rayleigh–Schrödinger expansion, and occupation blocks intraband transitions (Pauli). None is used as authority.

## Domain qualifications

- The massless walk; volume-preserving diagonal stretches; second order in `λ`.
- The sea counted as energy is block 147's first reading, which is itself a third-column choice.

## Theorem T1 — the stretch to second order

*Statement.* For `q = −λ + q₂λ²`, `F = s(1 − qs²)e^{−λ} = s − λ s c² + λ² s(1/2 − (1 + q₂)s²) + O(λ³)`. Block 69's linear completion `q = 1 − ℓ` and block 176's smooth completion `q = (1 − ℓ)/√(1 + 36(ℓ − 1)²)` both have first coefficient `−1` and `q₂ = −1/2`.

*Proof.* Series (runner B1). ∎

## Theorem T2 — the sea's second-order energy

*Statement.* For a filled mode of energy `−|F|`, the second-order change is `−(ŝ·F₂) − |ŝ × F₁|²/(2|s|)`. Averaged over the zone for `Σλ_a = 0`, this gives `E₂ = −(Σλ²/3)[A/2 − (1 + q₂)B] − I`.

*Proof.*
- Expand `|s + λF₁ + λ²F₂|` to second order.
- The first-order term averages to zero, since `Σλ_a = 0` and the zone has cubic symmetry.
- For the diagonal part use `⟨s_a²/|s|⟩ = A/3` and `⟨s_a⁴/|s|⟩ = B/3` for each `a`.
- Runner C1 checks the formula against the direct sum on the tori of side 6 and 8, for two directions. ∎

## Theorem T3 — a threshold

*Statement.* `E₂ < 0` iff `q₂ < q₂* = −1 + (A/2 + 3I/Σλ²)/B`.
- `I/Σλ²` is the same for every traceless diagonal direction, so `q₂*` is one number per lattice.
- On the infinite lattice, and on the tori of side 6 and 8, `q₂* > −1/2`. On the side-4 torus `q₂* = −1/2`.
- So every completion with `q₂ ≤ −1/2` gives way, strictly on the infinite lattice; block 69's linear and block 176's smooth completion are two.
- Block 176's band `q ≥ −1/6` concerns values of `q` at finite stretch, which do not bound `q₂`.

*Proof.*
- `q₂* + 1/2 = (A/2 − B/2 + 3I/Σλ²)/B`.
- `A − B = ⟨Σ s²c²/|s|⟩ ≥ 0`, which is zero only if every active axis has `s² = 1`. That holds for every mode of the side-4 torus and for a set of measure zero in the zone. Also `I ≥ 0`.
- The traceless diagonal strains carry one irreducible representation of the axis permutations, so any invariant quadratic form on them is a multiple of `Σλ²`.
- Runner D1 checks the side-4 value, `A − B = (4 + √3 + 2√6)/36` on side 6, the positivity of `I` on sides 6 and 8, and the agreement of the two directions.
- Near `ℓ = 1`, `q = −λ + q₂λ²` satisfies `q ≥ −1/6` for every `q₂`. ∎

## Theorem T4 — the frame for comparison

*Statement.* The frame's per-axis stretch `F = s e^{−λ}` gives `E₂ = −(Σλ²/6)A − I_frame < 0` for every volume-preserving diagonal stretch.

*Proof.* The same expansion with `F₁ = −λs`, `F₂ = λ²s/2` (runner E1, on sides 6 and 8). ∎

## Theorem T5 — the massive sea too

*Statement.* Take block 139's staggered mass `μ > 0`. It anticommutes with every walk in block 176's family, since each symbol is odd under `k → k + π`, so the stretched energies are `±R`, `R = √(μ² + |F|²)`. The filled band's second-order energy under a volume-preserving diagonal stretch is `E₂ = −(Σλ²/3)[A_μ/2 − (1 + q₂)B_μ] − I_μ`, where:
- `A_μ = ⟨|s|²/R⟩`;
- `B_μ = ⟨Σs⁴/R⟩`;
- `I_μ = ⟨(μ²|F₁|² + |s × F₁|²)/(2R³)⟩`.

Since `A_μ − B_μ = ⟨Σ s²c²/R⟩ ≥ 0` and `I_μ ≥ 0`, the threshold again exceeds `−1/2` on the infinite lattice. Every completion with `q₂ ≤ −1/2` gives way, as block 167 T4 found for the frame.

*Proof.* The same expansion with `R` in place of `|s|` (runner E2, at `μ = 1/2` on the tori of side 4 and 6). ∎

## What this settles and what it does not

- **Settled.**
  - Under the two-step coupling, the sea's response to volume-preserving diagonal stretches is `E₂(q₂)` above.
  - Every completion with `q₂ ≤ −1/2`, including both named ones, gives way, as the frame does.
  - So the worked consequence "gives way under shear" of the third-column item on the sea survives the change of coupling for these completions. In general it depends on the completion's `q₂`, which is on the coupling axis.
- **Not settled.**
  - Off-diagonal shears.
  - Long shear waves at non-zero wave vector (block 167's setting) under the two-step coupling.
  - Whether any principle fixes `q₂`. Block 182's covariance within reach three gives the linear completion, with `q₂ = −1/2`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the third column's sea item: consequences worked under block 62's frame (blocks 155, 167); conditional under the two-step coupling (panel 2026-09-27)"
source_of_blocker_text: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; off-diagonal shears with a supplied completion; long shear waves under the two-step coupling"
conditional_surface_status: "exact at second order, volume-preserving diagonal stretches, block 176's family"
hypothetical_axiom_status: "the coupling, the completion and the sea are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling.
  - Block 176 (pushed): the family.
  - Blocks 155 (open PR #9289) and 167 (pushed): the frame's sea gives way under shear.
  - Block 180 (pushed): the first-order stretch law.
  - Block 182 (pushed): covariance picks `q = 1 − ℓ`.
  - The panel of 2026-09-27 (same family) marked the sea's consequences conditional on the coupling.
- **In the literature.** The Rayleigh–Schrödinger split of a filled band's second-order energy into diagonal and interband parts, with Pauli blocking of intraband transitions. None is used as authority.
- **New here.**
  - The sea's second-order energy under the two-step coupling.
  - The threshold `q₂*` and its bound `q₂* > −1/2`.
  - That both named completions give way.
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: the sea's shear response under the two-step coupling. The obligations are:
- (O1) the premises (A3);
- (O2) the expansion (B1);
- (O3) the energy formula (C1);
- (O4) the threshold (D1);
- (O5) the frame's comparison (E1).

## No-Go Discipline Gate

The note's negative sentence: no completion in block 176's family with `q₂ ≤ −1/2` keeps the filled sea from giving way under a volume-preserving diagonal stretch.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A completion with `q₂ > q₂*`.* Allowed; the sea then holds. It is outside the two named completions.
2. *Off-diagonal shears.* Not examined; no completion is supplied for them.
3. *The torus.* On side 4 the named completions are marginal (`E₂ = 0`), because every active `s²` is 1.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the family, `λ = log ℓ`, volume preservation, and the sea's reading.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling; no completion fixed | yes (quoted, A3) |
| block 176 (pushed) | the family | yes (restated) |
| blocks 155, 167, 180, 182 | comparison and placement | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the sea gives way iff `q₂ < q₂*`, `q₂* > −1/2`" | executed: the expansion; `q₂` of the named completions | executed: the mode's second-order energy | executed: every mode of three tori, two directions | executed: `q₂*` on three tori; the frame | proved, not executed: the infinite-lattice bound |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This only shifts the question to `q₂`."
  - *Reply:* Yes, and that is the result. The sea's consequence rests on the coupling axis. For every completion named so far the answer is unchanged.

### N8 — Cross-cycle echo
- Blocks 155 and 167: the frame's sea gives way.
- Blocks 180 and 182: the two-step stretch law and its covariant completion.
- This note: the sea under the two-step coupling at second order.

## Falsifiers

- A torus or zone average for which the direct second-order sum differs from the formula of T2.
- A traceless diagonal direction with a different `q₂*`.

## Boundaries and non-claims

- Volume-preserving diagonal stretches; second order; the massless sea counted as energy.
- The coupling, the completion and the sea's reading are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 69 (landed), quoted. Blocks 155, 167, 176, 180 and 182 placed.
- Named standard imports, at definition level:
  - second-order expansion of a norm;
  - zone averages over finite tori;
  - representations of the axis permutations;
  - exact arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.**
  - The supervisor's own derivation, unrefereed.
  - The panel's lattice lens (same family) noted that both named completions have `q₂ = −1/2`. It was checked here.
- **Second version.** T5, the massive sea, was added.
- **Before writing.** Origin was re-fetched. Block 69 was read as landed, and blocks 155, 167 and 176 on their branches.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_the_two_step_coupling_whether_the_sea_gives_way_under_shear_2026_09_27.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
