---
claim_id: admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_an_exact_mass_a_convexity_term_no_global_minimum_under_a_quadratic_law_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN block 59's bond rates and bond law read in the law's own variable, the log rate (open PR #8581; not adopted), the balances of blocks 84 and 88 (#8652, #8665) and the free sea of block 76 (#8611) taken as a comparator: exact symbolic identities for every wave vector, exact rational instances, the thresholds as exact solutions of the second-order balances with the zone averages executed; the balance at all strengths and the crowd's coefficient executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_exact_mass_convexity_term_no_global_minimum_2026_09_23.py
---

# The unit of rate decides the alternation's thresholds: in log rates an exact mass, a convexity term, and no global minimum under a quadratic law

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact identities and inequalities; thresholds exact at second order with executed zone averages; corrects the thresholds of blocks 84 and 88; nothing adopted or registered; unaudited)

This note works within block 59's bond rates and bond law, read in the law's own variable (the log rate), the balances of blocks 84 and 88 and the sea as a comparator; it reports what the unit of rate does to those balances and what the alternation is in log rates; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 84 (PR #8652) balanced the free sea's energy against block 59's bond law and found that the bond rates alternate below `α + 2β = χ/12 = 0.128`; block 88 (PR #8665) found a second threshold, `β = χ_a/72 = 0.026`, for an anisotropy. Both balances wrote the rates as linear in the law's variable, `c = 1 + u`. Block 59 says its law is a law for `log c_b` (item 3), and its shift symmetry `u → u + const` is the unit of rate, which is not a variable (block 55 T4). At second order the difference matters. This note redoes the balances in the law's own variable and corrects both thresholds.

1. **In log rates the alternation is an exact mass (T1).** With bond amplitudes `e^{±δ}` alternating along each axis (geometric mean one), `h² = sin²k + sinh²δ` per axis and `H² = Σ_j sin²k_j + Σ_j sinh²δ_j` on the whole species block: the walk's dispersion is exactly `E² = |s|² + m²` with a momentum-independent `m² = Σ_j sinh²δ_j`, the same for all eight species. Block 84's linear alternation is the same shape scaled: `h_log(δ) = cosh δ · h_lin(tanh δ)`. Exact on a ring of eight with amplitudes `2` and `1/2`: `E² = sin²k + 9/16`.
2. **The unit of rate adds a convexity term (T2).** Holding the mean log rate fixed, the arithmetic mean of the amplitudes is `cosh δ > 1`, and the sea gains from it. Pointwise, the second derivative of the sea's energy is `−3/|s|` in log rates against `−(3 − |s|²)/|s|` in linear ones; the difference is `−|s|`. So the uniform bond-rate field is a local minimum iff **`α + 2β ≥ ⟨1/|s|⟩/4 = 0.2277`** (not block 84's `χ/12 = 0.1282`): exactly `⟨|s|⟩/12` higher, since `3⟨1/|s|⟩ = χ + ⟨|s|⟩`.
3. **The anisotropy's threshold moves too (T3).** In log rates the traceless anisotropy picks up the pointwise term `(4s_x² + s_y² + s_z²)/|s|`, average `2⟨|s|⟩`: the uniform field goes anisotropic iff **`β < (χ_a + 2⟨|s|⟩)/72 = 0.0593`** (not block 88's `0.0262`). Its independence of `α` stands.
4. **Above threshold the uniform field is only a local minimum (T4).** With block 59's law quadratic in log rates, `√(|s|² + 3 sinh²δ) ≥ √3 sinh δ` grows exponentially while the law's cost grows as `δ²`: at `δ_w = 6 + 12√3κ` the balance lies below the uniform value for every `κ`, exactly. Executed: at `κ = 0.25` the uniform field sits behind a barrier of height `0.82` at `δ = 1.87` and the energy falls below its value from `δ = 2.51`; just below the threshold an interior minimum appears (`δ* = 0.084, 0.168, 0.312, 0.480` at `κ = 0.225, 0.22, 0.21, 0.20`), and below `κ ≈ 0.19` the alternation runs away. Block 84's `δ*(κ)` curve and runaway value `0.0897` belong to its linear completion (amplitudes bounded by `2` and `0`); the global structure depends on the law's completion, which the lane does not supply. With the axioms' scalar hop the corner crossing of block 84 T4 becomes `tanh δ = 2a`.
5. **What survives unchanged.** Every sign statement: block 85's "the crowd's energy never rises" holds in log rates too (the crowd's generator also scales by `cosh δ`; executed: its log coefficient is the linear one plus exactly `|E(0)|` per site); block 86's separability and zero modes (its amplitudes are stated explicitly); block 87's law reward `2αδ²` (in log rates) and the positivity of the sea's tension.

So the rest energy that block 84 derived is sharper in the law's own variable — an exact relativistic mass `√(Σ sinh²δ_j)`, momentum-independent — and easier to reach (threshold `0.228` rather than `0.128`), but its size and even its existence as a global minimum now visibly depend on how block 59's law continues beyond second order. In plain terms: measured the way the law itself measures rates, long-short-long-short bonds make every moving record carry exactly the same rest energy at every speed, and a lattice somewhat stiffer than the earlier estimate already prefers them; but with the simplest law nothing stops the alternation from growing without bound once it passes a barrier, so what fixes its size is a question about the law that the lane has not answered.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 84 (PR #8652) and block 88 (PR #8665): thresholds computed with rates linear in block 59's variable u; block 59 item 3 states the law is for log c_b and its shift symmetry is the unit of rate"
source_of_blocker_text: supervisor re-reading of block 59 (2026-09-23)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "thresholds in the law's own variable: alternation alpha + 2 beta < <1/|s|>/4 = 0.228, anisotropy beta < (chi_a + 2<|s|>)/72 = 0.059; the alternation is an exact mass sqrt(sum sinh^2 delta_j); corrigenda on blocks 84 and 88; next: the bond law's completion beyond second order (derivation queued on ai/probes), the crowd's coefficient in 3D, the anisotropic state"
conditional_surface_status: "T1 exact for every wave vector; T2, T3 exact at second order with the zone averages executed; T4 an exact inequality for every kappa (the law quadratic in log rates) plus executed curves; the law's variable and its unit are block 59's and block 55 T4's; the completion, the sea and the balance as a minimisation are not derived"
hypothetical_axiom_status: "block 59's bond rates and law; the sea; the balance as a minimisation; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice and Qubit axioms and its silence on a time metric and on the unit of rate. Blocks 55, 59, 76, 84, 85, 86, 87, 88 (open PRs #8571, #8581, #8611, #8652, #8657, #8660, #8662, #8665) supply the unit of rate, the bond rates and their law, the sea reading, and the balances this note corrects. Nothing is adopted here.

- **The law's variable and its unit.** Block 59 item 3: "covariant nearest laws for `log c_b` have three free numbers"; T3's law has the shift symmetry `u → u + const`, `u_b = log c_b`; the uniform shift is the unit of rate (block 55 T4: the unit is not a variable). A balance holds `Σ_b u_b` fixed.
- **The two parametrisations.** Log: `c_b = e^{u_b}`, the alternation `u = δ_j(−1)^{x_j}` (mean zero). Linear (blocks 84, 88): `c_b = 1 + u_b`, the alternation `c = 1 ± δ` (arithmetic mean one; its mean log rate is `−δ²/2 + O(δ⁴)`).
- **Pair operators.** On the pair `(k, k + π)` of an axis with amplitudes `cosh δ ± sinh δ`: `D = e^{−ik}(cosh δ τ_z + i sinh δ τ_y)`, `h = (1/2i)(D − D†) = −cosh δ sin k τ_z + sinh δ cos k τ_y`.
- **Zone averages.** `⟨1/|s|⟩`, `⟨|s|⟩`, `χ = ⟨Σ cos²k_j/|s|⟩`, `χ_a = 9⟨s_x²(s_y² + s_z²)/|s|³⟩`, `|s|² = Σ sin²k_j`.
- **The balances.** Per site, the sea's energy plus block 59's cost: `6κδ²` for the three-axis alternation (`κ = α + 2β`, block 84 T2), `36βε²` for the anisotropy (block 88 T1).
- **Control.** Zone sums on midpoint grids, dense spectra on `6³`, block 80's compressed generator on `3×3`.

That an energy linear in the amplitudes gains from a zero-mean modulation of their logarithms by the convexity of the exponential is Jensen's inequality; that a dimerised hop gives a Dirac-type mass is the comparator of Su, Schrieffer and Heeger; none is used as authority.

## Prior art and what is new

Block 84 gave the balance and block 88 the anisotropy with rates linear in the law's variable. New, inside the framework's vocabulary: the exact mass identity in log rates; the recognition that the law's variable is the log rate and its unit the mean log rate, so that the second-order balance carries a convexity term (Jensen's inequality); the corrected thresholds with the exact relation `3⟨1/|s|⟩ = χ + ⟨|s|⟩`; the exact statement that a law quadratic in log rates never makes the uniform field the global minimum; and the scalar hop's crossing at `tanh δ = 2a`. No gravitational claim is made.

## Exact target and obligation graph

Target: the balances of blocks 84 and 88 in the law's own variable. Obligations: (O1) the walk in log rates; (O2) the alternation's threshold at fixed unit; (O3) the anisotropy's; (O4) the global structure. T1–T4 discharge O1–O4.

## Theorem T1 — in log rates the alternation is an exact mass

*Statement.* (a) `h² = (sin²k + sinh²δ)·1` and `h = cosh δ · h_lin(tanh δ)`, `h_lin(t) = −sin k τ_z + t cos k τ_y`. (b) With independent `δ_j`, `H² = Σ_j sin²k_j + Σ_j sinh²δ_j` on the 16-dimensional block. (c) On a ring of eight with amplitudes `2, 1/2` alternating: `E² ∈ {9/16, 17/16, 25/16}`.

*Proof.* (a) `(τ_z)² = (τ_y)² = 1`, `τ_zτ_y + τ_yτ_z = 0`, and `cosh²δ sin²k + sinh²δ cos²k = sin²k + sinh²δ`. (b) Block 84 T1's argument with these `h_j`. (c) Exact eigenvalues. Family B. ∎

## Theorem T2 — the unit of rate, the convexity term, and the threshold

*Statement.* (a) Block 59's law annihilates the uniform shift: the unit is the mean log rate. (b) Pointwise, the second derivative at `δ = 0` of `−√(|s|² + 3 sinh²δ)` is `−3/|s|`; of block 84's `−√(|s|² + δ²Σcos²)` it is `−(3 − |s|²)/|s|`; the difference is `−|s|`. (c) The second-order balance per site at fixed unit is `(6κ − (3/2)⟨1/|s|⟩)δ²`: the uniform field is a local minimum iff `κ ≥ ⟨1/|s|⟩/4`, which is block 84's `χ/12` plus `⟨|s|⟩/12`.

*Proof.* (a) Block 59 T3 at `k = 0`. (b) Differentiation. (c) `Σ_j(sin² + cos²)/|s| = 3/|s|` and `Σ_j sin²/|s| = |s|` pointwise, so `3⟨1/|s|⟩ = χ + ⟨|s|⟩`. Family C. ∎

*Executed.* `⟨1/|s|⟩ = 0.91067`, `⟨|s|⟩ = 1.19380`, `χ = 1.53822` (grid `256³`; `3⟨1/|s|⟩ − χ − ⟨|s|⟩ = 0` to `10⁻¹⁵`): thresholds `0.2277` (log) and `0.1282` (linear).

## Theorem T3 — the anisotropy in log rates

*Statement.* For `c = (e^{2ε}, e^{−ε}, e^{−ε})`, pointwise `f''_log − f''_lin = (4a + b)/|s|` (`a = s_x²`, `b = s_y² + s_z²`, `f = √(E²)`), `f''_lin = 9ab/|s|³` (block 88); the zone average of the extra term is `2⟨|s|⟩`, and the threshold is `β < (χ_a + 2⟨|s|⟩)/72`.

*Proof.* Differentiation; the cyclic symmetry of the axes gives `⟨s_x²/|s|⟩ = ⟨|s|⟩/3`. Family D. ∎

*Executed.* `χ_a = 1.88273`: thresholds `0.0593` (log) and `0.0262` (linear).

## Theorem T4 — no global minimum under a quadratic law; the scalar hop's crossing

*Statement.* (a) With block 59's law quadratic in log rates, for every `κ > 0` the three-axis balance at `δ_w = 6 + 12√3κ` is below the uniform value. (b) With the scalar hop through the same bonds, the corner energies are `±√(4a²cosh²δ + 3 sinh²δ)` (four each) and `±4a cosh δ ± √(4a²cosh²δ + 3 sinh²δ)` (two each); they cross zero at `tanh δ = 2a`.

*Proof.* (a) `√(|s|² + 3 sinh²δ) ≥ √3 sinh δ ≥ √3δ³/6` and `⟨|s|⟩ ≤ √3`, so the balance at `δ` is at most `−√3δ³/6 + 6κδ²`, below `−√3 ≤ −⟨|s|⟩` whenever `√3δ³/6 − 6κδ² − √3 > 0`; at `δ_w` this equals `√3(δ_w² − 1) > 0`. (b) Exact rational instance `e^δ = 2` (`cosh = 5/4`, `sinh = 3/4`): the corner matrix's nullity is `4` at `a = 3/10 = tanh(δ)/2` and `0` at `a = 1/4`, and its squared spectrum at `a = 1/4` is `{133/64, 233/64 ± 5√133/16}`. Family E. ∎

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block89_unit_of_rate.py`, output in `.out.txt`; disjoint machinery: floating-point zone sums and dense spectra).

*W1.* The zone averages above on grids of side 64, 128, 256; the thresholds `0.2276–0.2277` (log) against `0.1281–0.1282` (linear), `0.0593` against `0.0262`.

*W2.* On the `6³` torus with amplitudes `e^{±δ}` on every axis the whole spectrum equals `±√(Σ sin²k + 3 sinh²δ)` to `10⁻¹⁴` at `δ = 0.2, 0.5`; `cosh δ · E_lin(tanh δ) = E_log(δ)` in the zone sums (`−1.247075`, `−1.507235`).

*W3.* The balance at all strengths (grid `128³`):

| `κ` | uniform | interior minimum `δ*` (rest energy `√3 sinh δ*`) | barrier (`δ`, height) | below the uniform value from |
|---|---|---|---|---|
| `0.30` | local minimum | none | `2.22`, `2.09` | `3.00` |
| `0.25` | local minimum | none | `1.87`, `0.82` | `2.51` |
| `0.2277` | local minimum | none | `1.65`, `0.40` | `2.20` |
| `0.225` | unstable | `0.084` (`0.146`) | `1.62`, `0.36` | `2.15` |
| `0.21` | unstable | `0.312` (`0.549`) | `1.43`, `0.15` | `1.85` |
| `0.20` | unstable | `0.480` (`0.864`) | `1.25`, `0.05` | `1.53` |
| `0.18` and below | unstable | none | none | at once |

*W4.* The crowd on the `3×3` torus (block 85's machinery), 4 and 6 records: the second-order coefficient in log rates is the linear one plus `0.4541` and `0.4470`, which are exactly `|E(0)|` per site.

## No-Go Discipline Gate

The note's negative sentences: block 84's and block 88's thresholds are not those of the law's own variable; with a law quadratic in log rates the uniform field is never the global minimum.

### N1 — Routes by which the sentences could fail or mislead
1. *The law's variable.* The correction rests on block 59 item 3 (the law is for `log c_b`) and on its shift symmetry being the unit of rate. If the owner's reading makes the law's variable the rate itself with the arithmetic mean as the unit, block 84's and block 88's numbers stand; the note states both.
2. *The completion.* T4(a) is for the law quadratic in log rates; a stiffer completion can make the uniform field the global minimum. Not supplied.
3. *The sea.* A comparator (block 78); the crowd's coefficients differ (block 85, W4).
4. *Block 85's linear terms.* On small tori the crowd has exact zero modes that give linear terms in both parametrisations; W4 compares second differences only.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Equal `δ` on the three axes in the balances; midpoint grids; the `3×3` torus for the crowd.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice and Qubit axioms | yes (premise) |
| block 59 (open PR #8581) | the law's variable (item 3) and its shift symmetry | yes (the correction's premise) |
| block 55 (open PR #8571) | the unit of rate is not a variable (T4) | yes (restated) |
| blocks 84, 85, 86, 87, 88 (open PRs #8652, #8657, #8660, #8662, #8665) | the balances corrected and the statements kept | yes (placed) |
| block 76 (#8611), block 78 (#8613) | the sea as comparator | yes (comparator) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "exact mass in log rates; convexity term; thresholds 0.228 and 0.059; no global minimum under a quadratic law; crossing at tanh delta = 2a" | executed: the pair operator, the 16-block, the ring of eight | executed: the pointwise second derivatives | executed: zone sums; `6³` spectra; balance curves | executed: thresholds as exact solutions; the witness `δ_w`; the corner nullities | T1 for every wave vector; T2, T3 at second order; T4 for every `κ`

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A change of variable cannot change physics." Reply: it does not; what changes is which configurations are compared at the same unit of rate. The lane fixes the unit as the law's zero mode (the mean log rate); at that unit the arithmetic mean of the amplitudes rises as `cosh δ`, and the sea, linear in the amplitudes, gains. Block 84 compared at a fixed arithmetic mean, which is a different unit. Second objection: "Then the global runaway is an artefact of the quadratic law." Reply: yes, and the note says so: the local threshold is fixed at second order by the unit; the global structure is fixed by a completion nobody has supplied.

### N8 — Cross-cycle echo
Block 59: a law for `log c_b` with a shift symmetry. Block 55 T4: the unit of rate is not a variable. Block 84: the alternation's balance (linear). Here: the same balance at the law's own unit.

## Falsifiers

- A wave vector at which `H² ≠ Σ sin²k_j + Σ sinh²δ_j` for log-alternating amplitudes.
- A point of the zone at which the difference of the two second derivatives is not `−|s|`, or a threshold other than `⟨1/|s|⟩/4`.
- An anisotropy threshold other than `(χ_a + 2⟨|s|⟩)/72`.
- A `κ > 0` for which the balance at `δ_w` is not below the uniform value (law quadratic in log rates).

## Boundaries and non-claims

Second order at a fixed unit; the completion not supplied; the sea a comparator; equal alternations on the three axes in the balances. The thresholds of blocks 84 and 88 remain correct for their stated parametrisation (rates linear in the law's variable, arithmetic mean fixed). No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice and Qubit axioms. Blocks 55, 59, 76, 78, 84–88 (open PRs): restated or placed.
- Named standard imports at definition level: Jensen's inequality (convexity of the exponential); exact symbolic algebra; zone sums, dense spectra and sparse diagonalisation for the control.

## Review record
Supervisor-run block, the thirty-seventh of the source-link direction; the first run on Claude Opus 5.5 (the owner switched the session's model before this block; the seats, exact runner, refuting control and census are unchanged). Lens pass, in writing, by the supervisor: a foundations lens — the supervisor re-read block 59 before building on blocks 84 and 88 and found that its law is for the log rate (item 3) with the shift symmetry as the unit of rate, which blocks 84 and 88 had not used; a rigour lens — the Jensen term was derived pointwise before any number was quoted, the identity `3⟨1/|s|⟩ = χ + ⟨|s|⟩` checked both symbolically and numerically, the global statement made an exact inequality with an explicit witness, and two heavy symbolic eigenvalue computations replaced by exact rational instances (`e^δ = 2`). Decimal literals in message strings were replaced by fractions for the float scan. Mutation census: nine mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_exact_mass_convexity_term_no_global_minimum_2026_09_23.py
```

Expected: `TOTAL: PASS=17 FAIL=0`.
