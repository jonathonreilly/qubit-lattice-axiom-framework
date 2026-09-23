---
claim_id: admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_below_alpha_plus_2beta_anisotropy_breaks_rotation_below_beta_alone_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN block 59's bond rates and bond law (open PR #8581; not adopted), block 84's balance (#8652) and the sea of block 76 (#8611) taken as a comparator: exact symbolic algebra for the law's costs and the sea's second-order integrands; the two thresholds in closed form; the response curve, the zone averages, the endpoint property of the single-axis balance and the map executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_anisotropy_breaks_rotation_2026_09_22.py
---

# The two instabilities of the uniform bond rates: the alternation breaks translation below α + 2β = χ/12, the anisotropy breaks rotation below β = χ_a/72 alone

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact costs and integrands; thresholds in closed form with executed zone averages; the endpoint property of the single-axis balance executed; nothing adopted or registered; unaudited)

This note works within block 59's bond rates and bond law, block 84's balance and the sea as a comparator; it reports the two ways the uniform bond-rate field can first give way - an alternation or an anisotropy - and their thresholds in the law's numbers; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 84 (PR #8652) found that the uniform bond-rate field gives way to an alternation when block 59's stiffness `α + 2β` falls below `χ/12`; block 87 found that the collinear coupling `α` rewards walls in that alternation. This note asks the linear question underneath both: among all single-axis modulations of the bond rates, and the uniform anisotropies, which does the uniform field give way to first, and at what stiffness?

1. **What the law charges (T1).** Block 59's law charges a single-axis modulation of the bond rates at wave vector `q` along its own axis `α(1 − cos q) + 4β` per bond per unit modulation power: `4β` for a uniform shift of one axis, `2α + 4β` for the alternation. The traceless anisotropy `u = ε(2, −1, −1)` — one axis' rates raised, the other two lowered, the total held — costs exactly `36βε²` per site: `α` and `γ` do not enter.
2. **What the sea gains (T2).** The sea's energy has no first-order response to the anisotropy (its first derivative's three cyclic images cancel by the cubic symmetry) and the second-order coefficient `χ_a = 9⟨s_x²(s_y² + s_z²)/|s|³⟩ = 1.8827` per `ε²`, pointwise positive; to the alternation it is `χ = 1.5382` (block 84). Per unit power the response to a single-axis modulation rises continuously from `χ_a/9 = 0.209` at `q = 0` to `χ/3 = 0.513` at `q = π` (executed; the jump one sees in the raw response at `π` is only the modulation's power, `1` for the alternation against `½` for a cosine).
3. **Two thresholds (T3).** The uniform field is unstable to the alternation iff `α + 2β < χ/12 = 0.128` and to the anisotropy iff `β < χ_a/72 = 0.0262` — the second independent of `α`. The alternation breaks one-step translation; the anisotropy breaks the cubic rotations to the group of one axis. **Corrigendum (2026-09-23, block 89, PR #8678):** these thresholds take the rates linear in the law's variable at fixed arithmetic mean; in block 59's own variable, the log rate, with the mean log rate as the unit of rate, they are `α + 2β < ⟨1/|s|⟩/4 = 0.228` and `β < (χ_a + 2⟨|s|⟩)/72 = 0.059`; the anisotropy's independence of `α` stands.
4. **Nothing in between (T4, executed).** For a single-axis modulation the balance `χ̃(q)/2 − α(1 − cos q) − 4β` has its maximum at `q = 0` or `q = π` for every `α` tried, never at an intermediate wave vector: the first instability is the alternation or the anisotropy, and the alternation wins the single-axis race iff `α < (χ/3 − χ_a/9)/4 = 0.076`.

So block 59's three numbers draw a map. Where `β > 0.026` and `α + 2β > 0.128` the uniform, isotropic bond rates are a local minimum; below `α + 2β = 0.128` the lattice alternates and every species gains one rest energy (block 84); below `β = 0.026` it goes anisotropic — its clocks tick faster along one axis — whatever `α` is; and where both hold, which comes first is decided by `α` against `0.076` (all with the rates linear in the law's variable; in log rates the lines are `α + 2β = 0.228` and `β = 0.059`, which cross at `α = 0.109`, block 89). In plain terms: a lattice whose bonds are stiff enough sideways stays even; make them soft sideways and the lattice picks a favourite direction; make them soft in line and it goes long-short-long-short instead, and then every moving record is heavy.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 87 N1.3 and queue item 2: 'the domain pattern when walls are favoured' - the linear question of which modulation comes first"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "two thresholds in closed form: alternation below alpha + 2 beta = chi/12, anisotropy below beta = chi_a/72; no intermediate modulation (executed); next: the anisotropic state itself (its walk: E^2 = (1 + 2e)^2 s_x^2 + (1 - e)^2 (s_y^2 + s_z^2), light along one axis), the alternation on top of an anisotropy, and whether anything in the lane constrains beta"
conditional_surface_status: "T1 by block 59's law at every wave vector; T2 by the pointwise sign of an exact integrand; T3 at second order with chi and chi_a executed to four places; T4 executed for the alphas tried (endpoint property not proved); the bond law's numbers, the sea reading and the balance as a minimisation are not derived"
hypothetical_axiom_status: "block 59's bond rates and law; the sea; the balance as a minimisation; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (the cubic rotations permuting the axes) and the Qubit axiom. Blocks 59, 76, 84 (open PRs #8581, #8611, #8652) supply the bond rates and their law, the sea reading and the balance. Nothing is adopted here.

- **Block 59's law.** `M(k)` on the three bond fields (block 84's declaration); `M_jj(q, 0, 0) = c₀ + 2α cos q + 4γ`, `c₀ = −2α − 8β − 4γ`; at `k = 0` the eigenvalues `0` on `(1,1,1)` and `−12β` twice.
- **Single-axis modulation.** `t_x(x) = 1 + ε cos(qx_1)` on the bonds along `x`; its power is the mean of `cos²`: `1` at `q = 0, π`, `½` otherwise. **Cost per unit power** `−M_11(q,0,0)/2`.
- **Traceless anisotropy.** `u = ε(2, −1, −1)` on the three axes (the total of the bond rates held, block 55 T4's unit of rate); cost `−½uᵀM(0)u`.
- **The sea's responses.** By separability (blocks 82, 86) the alternation gives `E² = Σ(sin² + δ²cos²)` and the anisotropy `E² = (1 + 2ε)²s_x² + (1 − ε)²(s_y² + s_z²)`; the second-order coefficients `χ` and `χ_a` are the zone averages of minus the second derivatives at `0`. **Response per unit power** `χ̃(q)` for a single-axis modulation: minus the second derivative of the sea's energy per site, divided by the power (executed).
- **Balances.** Per site: `(6(α + 2β) − χ/2)δ²` for the three-axis alternation (block 84); `(36β − χ_a/2)ε²` for the anisotropy; per bond `χ̃(q)/2 − α(1 − cos q) − 4β` for a single-axis modulation.

That a lattice whose energy is lowered by a distortion at a wave vector nesting its zeros dimerises is the mechanism of Peierls; that an isotropic lattice can instead lower its energy by a uniform anisotropic strain is a nematic or Jahn–Teller-type instability; none is used as authority.

## Prior art and what is new

Block 84 gave the alternation's threshold and block 87 the walls' reward. New, inside the framework's vocabulary: the law's cost as a function of wave vector for a single-axis modulation; the anisotropy's exact cost `36βε²` and its exact second-order integrand with the cancellation of the first order; the second threshold `β = χ_a/72`, `α`-free; the continuity of the response per unit power at the alternation; and the executed endpoint property. No gravitational claim is made.

## Exact target and obligation graph

Target: the first instability of the uniform bond rates. Obligations: (O1) the law's costs; (O2) the sea's gains; (O3) the thresholds; (O4) intermediate wave vectors. T1–T3 discharge O1–O3; T4 is executed.

## Theorem T1 — what the law charges

*Statement.* `−M_11(q, 0, 0)/2 = α(1 − cos q) + 4β`; `M(0)` has eigenvalues `0` (once, on `(1,1,1)`) and `−12β` (twice); `−½uᵀM(0)u = 36βε²` for `u = ε(2, −1, −1)`, independent of `α` and `γ`.

*Proof.* Substitution in block 59 T3's matrix (family B, symbolic). ∎

## Theorem T2 — what the sea gains

*Statement.* For the anisotropy, the sea's energy per site `E(ε) = −⟨√((1 + 2ε)²s_x² + (1 − ε)²(s_y² + s_z²))⟩` has `E'(0) = −⟨(2s_x² − s_y² − s_z²)/|s|⟩ = 0` (the three cyclic images of the integrand sum to zero) and `E''(0) = −9⟨s_x²(s_y² + s_z²)/|s|³⟩ =: −χ_a`, the integrand pointwise negative. For the alternation `E''(0) = −χ` (block 84 T1).

*Proof.* Symbolic differentiation (family C); the cubic rotations permute the axes and preserve the zone average. ∎

*Executed.* `χ_a = 1.88273` (grids of side 64, 128, 256, settled); the direct second difference on `32³` gives `1.88283` and the first difference `2·10⁻⁵`; `χ = 1.5382`; `χ̃(q)` per unit power on rings of 48 and 96: `0.209, 0.219, 0.250, 0.303, 0.376, 0.459` at `q = 0, 0.52, 1.05, 1.57, 2.09, 2.62`, and `0.511` at `π − 2π/96` against `0.514` at `π`.

## Theorem T3 — the two thresholds

*Statement.* At second order the uniform field is a local minimum against the three-axis alternation iff `α + 2β ≥ χ/12` and against the traceless anisotropy iff `β ≥ χ_a/72`; the second condition does not involve `α`.

*Proof.* The balances `(6(α + 2β) − χ/2)δ²` and `(36β − χ_a/2)ε²` (family D, symbolic). ∎

*Executed.* `χ/12 = 0.1282`, `χ_a/72 = 0.02615`.

## Theorem T4 — nothing in between (executed)

*Statement.* The law's cost of a single-axis modulation is `0` at `q = 0`, `2α` at `q = π`, with second derivative `α cos q`. Executed: for `301` values of `α` in `[0, 0.3]` the balance `χ̃(q)/2 − α(1 − cos q)` on the ring of 96 has its maximum at an endpoint; `f(π) = f(0)` at `α = (χ/3 − χ_a/9)/4 = 0.0762`.

*Proof.* Family E for the cost; the endpoint property is the control's (W3), not proved. ∎

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block88_two_instabilities.py`, output in `.out.txt`; disjoint machinery: floating-point spectra on rings, zone sums on midpoint grids).

*W1 — the response curve.* `χ̃(q)` as in T2's executed paragraph, on rings of 48 and 96; continuous at `π` per unit power.

*W2 — the coefficients.* `χ = 1.53751, 1.53808, 1.53822` and `χ_a = 1.88273` (three grids); thresholds `0.1281–0.1282` and `0.02615`; the anisotropy's direct second difference `1.88283`, first difference `2·10⁻⁵`.

*W3 — no interior maximum.* `0` of `301` values of `α` give an interior maximiser; boundary `α = 0.0762`.

*W4 — the map.* `(α, β) = (0.05, 0), (0.05, 0.02), (0.10, 0)`: both unstable; `(0.10, 0.02), (0.15, 0.01)`: anisotropy only; `(0.05, 0.04), (0.15, 0.03)`: uniform stable.

## No-Go Discipline Gate

The note's negative sentences: `α` and `γ` do not enter the anisotropy's cost or threshold; the sea has no first-order response to the anisotropy; no intermediate modulation comes first (executed).

### N1 — Routes by which the sentences could fail or mislead
1. *Second order only.* Both thresholds are linear-instability statements; the states beyond them (block 84's `δ*`; the anisotropic state) and their competition when both are unstable are not computed here.
2. *Single-axis and traceless modes only.* Modulations mixing axes, or with wave vectors off the axes, are not examined; the endpoint property is for single-axis modulations along their own axis.
3. *The unit of rate.* The anisotropy holds the total of the bond rates; a scaling of all rates is the unit of rate (block 55 T4), excluded by construction.
4. *The sea* is a comparator (block 78); the crowd's coefficients (block 85) are smaller by filling-dependent factors, moving both thresholds down.
5. *Block 59's numbers* are not fixed by anything in the lane.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Midpoint grids; rings of 48 and 96 for the curve; `ε = 0.01` in the second differences; `α ∈ [0, 0.3]` for the endpoint scan.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice axiom's rotations (the cyclic permutation of the axes) | yes (premise) |
| block 59 (open PR #8581) | the bond rates and the three-number law | yes (restated) |
| blocks 84, 87 (open PRs #8652, #8662) | the alternation's balance; the walls | yes (placed) |
| blocks 76, 78 (open PRs #8611, #8613) | the sea as comparator | yes (comparator) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "costs alpha(1 - cos q) + 4 beta and 36 beta eps^2; gains chi and chi_a with no first order; thresholds chi/12 and chi_a/72; no interior maximum" | executed: the law's matrix symbolically; the integrand and its cyclic images | executed: the anisotropy's cost from the k = 0 eigenvalues | executed: the response curve; the zone averages | executed: the balances symbolically | T1, T2 by proof; T3 at second order; T4 executed

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "The anisotropy is a trivial strain mode." Reply: it is the one that the collinear coupling cannot stiffen — only `β` holds the lattice isotropic — and its threshold is a closed-form number of the walk; that it competes with the alternation on the same footing is the content. Second objection: "Why not modulations off the axes?" Reply: not examined and said so; the single-axis family is the one block 59's law and the walk's separability make exact.

### N8 — Cross-cycle echo
Block 84: the alternation's threshold. Block 87: `α` rewards walls, `β` holds the pattern. Here: `α + 2β` decides the alternation, `β` alone the anisotropy, and nothing in between.

## Falsifiers

- A wave vector at which `−M_11(q,0,0)/2 ≠ α(1 − cos q) + 4β`, or an anisotropy cost differing from `36βε²`.
- A point of the zone at which the anisotropy's second-order integrand is positive, or a nonzero first-order zone average.
- A threshold of either balance differing from `χ/12` or `χ_a/72`.
- An `α` for which the single-axis balance peaks at an intermediate `q`.

## Boundaries and non-claims

Linear order with the rates linear in the law's variable at fixed arithmetic mean (block 89 gives the law's own unit: `0.228` and `0.059`); single-axis and traceless modes; the endpoint property executed; the sea a comparator; the numbers not fixed. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice and Qubit axioms. Blocks 59, 76, 78, 84, 87 (open PRs): restated or placed.
- Named standard imports at definition level: second-order expansions; zone averages on midpoint grids; dense spectra for the control.

## Review record
Supervisor-run block, the thirty-sixth of the source-link direction; the seventh after the rest-energy panel. Lens pass, in writing, by the supervisor: a foundations lens — the anisotropy is defined with the total of the rates held, so that the unit of rate is not mistaken for an instability; a rigour lens — the apparent discontinuity of the raw response at `π` was traced to the modulation's power and removed by normalising per unit power before any conclusion was drawn; the first-order cancellation was made a symbolic identity; a sign error in the law's second derivative in a first draft of the runner was caught by the check itself and corrected; decimal literals in message strings were replaced by fractions for the float scan. Mutation census: six mutations, each failing in its own family only. No independent review has taken place.

Corrigendum (2026-09-23, supervisor): block 59's law is for the log rate (item 3), with the mean log rate as the unit of rate; this note's balances used rates linear in the law's variable, which differs at second order by a convexity term. The thresholds stated here are correct for that parametrisation; block 89 gives the law's own (`0.228`, `0.059`). No theorem, check or number changed.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_anisotropy_breaks_rotation_2026_09_22.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
