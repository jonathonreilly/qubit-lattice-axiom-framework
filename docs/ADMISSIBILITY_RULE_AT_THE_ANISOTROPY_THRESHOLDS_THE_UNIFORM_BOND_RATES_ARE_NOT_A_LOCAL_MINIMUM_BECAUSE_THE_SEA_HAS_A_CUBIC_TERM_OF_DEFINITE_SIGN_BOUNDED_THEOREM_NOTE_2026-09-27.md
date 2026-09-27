---
claim_id: admissibility_rule_at_the_anisotropy_thresholds_the_uniform_bond_rates_are_not_a_local_minimum_because_the_sea_has_a_cubic_term_of_definite_sign_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN blocks 88 and 89 as landed (the uniform bond rates; the supplied quadratic law's cost 36 beta eps^2 for the traceless anisotropy u = eps(2, -1, -1); the walker sea's energy -<sqrt(Q)> as a continuum zone average; block 88's linear rates at fixed arithmetic mean, Q = (1 + 2e)^2 s_x^2 + (1 - e)^2 (s_y^2 + s_z^2), with threshold beta = chi_a/72; block 89's rates at fixed mean log, Q = e^(4e) s_x^2 + e^(-2e)(s_y^2 + s_z^2), with threshold beta = (chi_a + 2J)/72; both notes leave the equality case open): (T1) in linear rates the sea energy's cubic coefficient along the path is (3/2)<sum_i u_i (u_j - u_k)^2/|s|^5> > 0, u_j = sin^2 k_j; (T2) in log rates it is -<(s1^3 + 9 s1 s2/2 + 81 s3/2)/(3|s|^5)> < 0, s1, s2, s3 the elementary symmetric functions of the u_j; (T3) the law's cost has no cubic part, and every e-derivative of sqrt(Q) is bounded by a constant times |s| near e = 0, so at each threshold the path energy is e3 e^3 + O(e^4) with e3 != 0: the uniform rates are not a local minimum along the path, descending towards a weaker special axis (e < 0) in linear rates and a stronger one (e > 0) in log rates. A harvest of probe #9222 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9337, Grok). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_two_instabilities_of_the_uniform_bond_rates_alternation_breaks_translation_below_alpha_plus_2beta_anisotropy_breaks_rotation_below_beta_alone_bounded_theorem_note_2026-09-22
  - admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_an_exact_mass_a_convexity_term_and_no_global_minimum_under_a_quadratic_law_bounded_theorem_note_2026-09-23
runner: scripts/admissibility_rule_at_the_anisotropy_thresholds_the_uniform_bond_rates_are_not_a_local_minimum_2026_09_27.py
---

# At the anisotropy thresholds the uniform bond rates are not a local minimum, because the sea has a cubic term of definite sign

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 88 and 89 as landed; a harvest of probe #9222, confirmed by an other-family referee in #9337; nothing adopted or registered; unaudited)

This note works within blocks 88 and 89 as landed on main (the uniform bond rates, the supplied quadratic law's cost and the walker sea's energy along the traceless anisotropy) and settles the equality case both left open; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 88 and 89 (landed) found where the uniform bond rates stop being stable against a traceless anisotropy, one special axis against the other two. That happens where the quadratic coefficient of the path energy changes sign: `β = χ_a/72` in linear rates and `β = (χ_a + 2J)/72` in log rates. Both notes leave the equality case open: "higher orders can matter". This note, a harvest of a probe result another model family has confirmed, settles it.

- **T1: in linear rates the sea's cubic term is positive.** It is `(3/2)⟨Σ_i u_i(u_j − u_k)²/|s|⁵⟩`, where `u_j = sin² k_j`.
- **T2: in log rates it is negative.** It is `−⟨(s₁³ + 9s₁s₂/2 + 81s₃/2)/(3|s|⁵)⟩`.
- **T3: at each threshold, not a minimum.**
  - The law's cost has no cubic part. So at the threshold the path energy starts at third order, with a nonzero coefficient, and the uniform rates are not a local minimum along the path.
  - In linear rates the energy falls when the special axis weakens. In log rates it falls when the special axis strengthens.

In plain terms: at the stiffness where the uniform rates are just barely stable to second order, the third-order term decides, and it is never zero. So the uniform state tips over there, towards a weaker special axis in one description of the rates and a stronger one in the other.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-27.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The rates, the law's cost and the sea are supplied clauses. Nothing is adopted.
- **Block 88 (landed on main).** Quoted by the runner (A3).
  - `u = ε(2, −1, −1)` has quadratic cost `36βε²` per site.
  - The sea integrand along the path is `−√((1 + 2ε)²s_x² + (1 − ε)²(s_y² + s_z²))`.
  - The sign change is at `β = χ_a/72`, with `χ_a = 9⟨s_x²(s_y² + s_z²)/|s|³⟩`.
  - "A zero anisotropy coefficient alone does not settle a minimum; higher orders can matter."
- **Block 89 (landed on main).**
  - The rates `(e^{2ε}, e^{−ε}, e^{−ε})`, so `Q = e^{4ε}s_x² + e^{−2ε}(s_y² + s_z²)`.
  - The same law in its variable.
  - The zero at `β = (χ_a + 2J)/72`, with `J = ⟨|s|⟩`.
  - "At equality higher-order analysis is needed."
- **Averages.** `⟨·⟩` is the continuum average over the zone. It is invariant under permuting the axes, so an integrand may be averaged over the six permutations.

## Domain qualifications

- The traceless path only. Directions at intermediate wave numbers, and finite grids with zero modes, are not treated.
- These are local statements along the path, not global stability or dynamics.
- These are conditional statements within supplied clauses, not a physical identification.

## Theorem T1 — in linear rates the sea's cubic term is positive

*Statement.*
- With `Q = (1 + 2ε)²a + (1 − ε)²b`, `a = s_x²` and `b = s_y² + s_z²`, `d²√Q/dε² = 9ab/Q^{3/2}` at every `ε`.
- The coefficient of `ε³` in the sea energy `−⟨√Q⟩`, averaged over the axes, is `e₃ = (3/2)⟨Σ_i u_i(u_j − u_k)²/|s|⁵⟩ > 0`.

*Proof.*
- Direct differentiation. The second derivative at `ε = 0` is block 88's `9ab/|s|³` (B1).
- The average over the six permutations of the axes is the stated nonnegative expression (B1).
- It is strictly positive at `u = (1, 1/2, 0)` and continuous, so its average is positive (D1). ∎

## Theorem T2 — in log rates it is negative

*Statement.*
- With `Q = e^{4ε}a + e^{−2ε}b`, the second derivative at `ε = 0` exceeds the linear model's by `(4a + b)/√(a + b)`, as block 89 states.
- The coefficient of `ε³` in the sea energy, averaged over the axes, is `e₃ = −⟨(s₁³ + 9s₁s₂/2 + 81s₃/2)/(3|s|⁵)⟩ < 0`. Here `s₁, s₂, s₃` are the elementary symmetric functions of the `u_j`, and `|s|² = s₁`.

*Proof.* Direct differentiation and averaging over the permutations (C1). All terms of the numerator are nonnegative and `s₁ > 0` away from the zeros of `s`, so the average is negative. ∎

## Theorem T3 — at each threshold, not a minimum

*Statement.*
- Along either path, the path energy is `E(ε) = 36βε² − [F(ε) − F(0)]`, with `F = ⟨√Q⟩`.
- At the threshold (`β = χ_a/72` in linear rates, `(χ_a + 2J)/72` in log rates), `E(ε) = e₃ε³ + O(ε⁴)` with `e₃ ≠ 0`.
- So the uniform rates are not a local minimum along the path:
  - in linear rates `E < 0` for small `ε < 0`, so the special axis weakens;
  - in log rates `E < 0` for small `ε > 0`, so the special axis strengthens.
- The anisotropy's local stability along the path is therefore exactly a positive quadratic coefficient.

*Proof.*
- The law's cost is exactly quadratic.
- For `|ε|` small, `Q > 0` away from `s = 0`. Every `ε`-derivative of `√Q` is homogeneous of degree one in `s` (D1). So it is bounded by a constant times `|s|`, and the averages may be differentiated up to fourth order.
- At the threshold the quadratic coefficient vanishes (blocks 88 and 89), which leaves `e₃ε³ + O(ε⁴)`. ∎

## What this settles and what it does not

- **Settled.** The equality cases left open by block 88 T3 and block 89 T2–T3. At each threshold the uniform rates tip along the path.
- **For landed blocks 88 and 89.** Their statements stand. This note answers their open equality case; no correction is owed.
- **Not settled.**
  - How far above threshold the linear path keeps a point below the uniform energy. The probe gives a rigorous window of width `1.2·10⁻⁵` from exact lower sums, and floating-point evidence to `β ≈ 0.0271`; neither is ported here.
  - Directions at intermediate wave numbers.
  - Finite grids with zero modes.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 88 T3: 'a zero anisotropy coefficient alone does not settle a minimum; higher orders can matter'; block 89: 'at equality higher-order analysis is needed' (deferred finding U9-R2)"
source_of_blocker_text: probes task J:derive:deferred-20260924-stability
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the window above threshold; intermediate-q directions"
conditional_surface_status: "exact along the traceless path in the continuum zone average"
hypothetical_axiom_status: "the rates, the law's cost and the sea are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 88: the two instabilities and the anisotropy threshold.
  - Block 89: log rates and their thresholds.
- **Probes.**
  - #9222, worker `w-macbookpro9927a-jbeaa`, Claude Opus 5.5, the supervisor's own model family, found T1–T3 as the owner-requested recovery of deferred finding U9-R2. An earlier refereed probe on the anisotropic state (`the-anisotropic-state` a1) had the log path's cubic in floating point.
  - #9337, worker `w-macbookpro90c72-j360c`, `grok-4.6`, another model family, refereed #9222 with its own checker: "HIT: confirmed - at either threshold the uniform rates are not a local minimum along the traceless path."
- **In the literature.** A symmetric state's loss of stability through a cubic term at the threshold is the familiar mechanism of a cubic invariant (Landau). It is named for reference only.
- **New here.**
  - The harvest.
  - A new exact runner.
  - The homogeneity argument for differentiating the averages to fourth order.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: the equality case of blocks 88 and 89. The obligations are:
- (O1) the premises (A3);
- (O2) the linear cubic (B1);
- (O3) the log cubic (C1);
- (O4) differentiability and sign (D1).

## No-Go Discipline Gate

The note's negative sentence: at either threshold the uniform rates are not a local minimum along the traceless path.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The cubic term averages to zero.* Each integrand is one-signed and nonzero on a set of positive measure (B1, C1, D1). ATTEMPTED.
2. *The averages cannot be differentiated at the zeros of `s`.* Homogeneity bounds every derivative by a constant times `|s|` (D1). ATTEMPTED.

Scope left open: the window above threshold; other directions.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The path and the continuum average are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 88, 89 (landed) | the paths, costs and thresholds; the open equality cases | yes (quoted, A3) |
| probe #9222 and referee #9337 | the result and its confirmation | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "at each threshold the uniform rates are not a local minimum along the path" | executed: the derivatives of `√Q` on both paths | executed: the averaged cubic integrands | executed: homogeneity to fourth order; the sign | executed: agreement with blocks 88 and 89 | not executed: the window above threshold; intermediate directions |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A cubic term only says the minimum moved."
  - *Reply:* At the threshold the quadratic term is zero, so a nonzero cubic term means the energy falls on one side.
  - The uniform rates are then not a local minimum along the path, which is what blocks 88 and 89 left open.

### N8 — Cross-cycle echo
- Blocks 88 and 89: the quadratic signs.
- This note: the equality case.

## Falsifiers

- A point of the zone where `Σ_i u_i(u_j − u_k)²` is negative.
- A zero average of either cubic integrand.

## Boundaries and non-claims

- The traceless path; the continuum zone average.
- The rates, the law's cost and the sea are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 88 and 89 (landed), restated and quoted.
- Named standard imports, at definition level:
  - differentiation under an integral with a dominating function;
  - symmetric functions;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.**
  - Probe #9222 (Claude Opus 5.5) was refereed by #9337 (`grok-4.6`, another family).
  - The supervisor wrote a new exact runner and did not port the probe's lower sums or floating-point scans.
- **Before writing.** Origin was re-fetched. Blocks 88 and 89 were read as landed. The own prior-art check covered memory (blocks 88 and 89), the held branches, open PRs and main.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_at_the_anisotropy_thresholds_the_uniform_bond_rates_are_not_a_local_minimum_2026_09_27.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
