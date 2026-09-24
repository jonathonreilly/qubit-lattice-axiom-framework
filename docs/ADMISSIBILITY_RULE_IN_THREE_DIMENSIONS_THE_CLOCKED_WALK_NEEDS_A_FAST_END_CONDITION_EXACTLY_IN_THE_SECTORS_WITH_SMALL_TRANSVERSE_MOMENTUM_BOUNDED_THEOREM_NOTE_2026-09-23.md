---
claim_id: admissibility_rule_in_three_dimensions_the_clocked_walk_needs_a_fast_end_condition_exactly_in_the_sectors_with_small_transverse_momentum_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clock clause and walk of blocks 53 and 54 as landed on main (c3f8c47a58), extending block 108 to Z^3 with w = lambda^(x1), lambda = e^g > 1. Exact: (T1) across the gradient, a plane wave exp(i(k2 x2 + k3 x3)) reduces the clocked walk to the line operator J_k = (sigma_1 D_1)_w + w(x1)(sin k2 sigma_2 + sin k3 sigma_3). (T2) Divided by lambda^n, the zero-energy recurrence of J_k has constant coefficients; its solutions are exactly psi(n) = (r/sqrt(lambda))^n v with r - 1/r = +-2m, m = |(sin k2, sin k3)|, so |r| = sqrt(1 + m^2) +- m. (T3) At the fast end the two solutions with |r| = sqrt(1 + m^2) - m are always square-summable, and the two with |r| = sqrt(1 + m^2) + m are square-summable exactly when m < m* = (lambda - 1)/(2 sqrt(lambda)) = sinh(g/2); every sector has four once lambda >= 5 + 2 sqrt(6). With the limit-point/limit-circle theory for matrix three-term operators imported at definition level, the sector's minimal operator has deficiency indices (2,2) for m < m* and (0,0) for m > m*: a fast-end boundary condition is needed exactly in the sectors with small transverse momentum. (T4) In the ray picture a ray with m > 0 turns back before w exceeds E/m, so the sectors 0 < m < m* need a condition though no ray with that m reaches the end. Supervisor's derivation. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_in_three_dimensions_the_clocked_walk_needs_a_fast_end_condition_exactly_in_small_transverse_sectors_2026_09_23.py
---

# In three dimensions the clocked walk needs a fast-end boundary condition exactly in the sectors with small transverse momentum: |(sin k₂, sin k₃)| < sinh(g/2), including waves the ray picture turns back

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact sector identities with the limit-point/limit-circle theory for matrix three-term operators imported at definition level; supervisor's derivation extending block 108; nothing adopted or registered; unaudited)

This note works within the supplied clock clause and walk of blocks 53 and 54, as landed on main, and extends block 108 to three dimensions; it reports which transverse sectors of the clocked walk in an exponential clock field need a boundary condition at the fast-clock end; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 108 found that on the line, in a clock field `w = λ^x`, the walk's dynamics needs a boundary condition at the fast-clock end. That answers, on the line, the realization question in block 54 as landed on main. In three dimensions, with the clock growing along `x₁`:

- **T1: sectors.** A plane wave across the gradient, `exp(i(k₂x₂ + k₃x₃))`, reduces the walk to a line operator. The hops across the gradient become an on-site term `w(x₁)(sin k₂σ₂ + sin k₃σ₃)` that grows with the clock.
- **T2: exact zero-energy solutions.** Dividing by `λ^n` makes each sector's zero-energy recurrence constant. Its solutions are exactly geometric: `ψ(n) = (r/√λ)^n v`, with `r − 1/r = ±2m`, where `m = |(sin k₂, sin k₃)|`.
- **T3: the threshold.**
  - At the fast end, two of the four solutions are always square-summable. The other two are square-summable exactly when `m < m* = (λ − 1)/(2√λ) = sinh(g/2)`.
  - So a sector needs a fast-end boundary condition exactly when its transverse momentum is small: deficiency indices `(2,2)` below `m*` and `(0,0)` above.
  - Every sector needs one once `λ ≥ 5 + 2√6`.
- **T4: rays miss it.** A ray with transverse momentum `m > 0` keeps its energy `E = w√(sin²k₁ + m²)`, so it turns back before `w` exceeds `E/m` and never reaches the fast end. Yet the sectors `0 < m < m*` still need a boundary condition: the lattice waves reach the end where the rays do not.

In plain terms: in three dimensions, only the part of the walker's motion aimed nearly along the direction in which clocks speed up can reach the end of the lattice, and only that part needs the extra condition. How "nearly" is set by the steepness of the clock field: within `sinh(g/2)` of straight along. Rays with any sideways motion turn back, but the waves do not all turn back, so the extra condition is a wave effect the ray picture cannot see.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The walk and its clock are supplied clauses. Nothing is adopted.
- **The walk** (block 54, #8570, as landed in c3f8c47a58).
  - `H = Σ_jσ_jD_j`, with `D_j = (i/2)(T_j − T_j†)` and `(T_eψ)(x) = ψ(x − e)`.
  - `H_w = W^{1/2}HW^{1/2}`.
  - T3 as landed leaves the evolution identity conditional on a realization; T4 as landed is a conditional ray model.
- **Block 108** (#8945, open) answers the question on the line: deficiency indices `(2,2)`.
- **The clock.** `w = λ^{x₁}`, `λ = e^g > 1`, the same on each plane of constant `x₁`.
- **Sectors.** For transverse wave numbers `(k₂, k₃)`, the sector operator is `J_k` on the line. Its minimal operator acts on finitely supported sequences, and the full operator is their direct integral.
- **Names.** The limit-point/limit-circle theory for matrix three-term operators is due to Krein and to Berezanskii. The persistence of the solution count under a summable perturbation is Levinson's asymptotic theorem, in its discrete form. The direct-integral decomposition is von Neumann's.

## Theorem T1 — sectors across the gradient

*Statement.* For `w = λ^{x₁}` and `ψ(x) = exp(i(k₂x₂ + k₃x₃))f(x₁)`, the clocked walk acts as `(J_kf)(x₁) = (σ₁D₁)_w f(x₁) + w(x₁)(sin k₂σ₂ + sin k₃σ₃)f(x₁)`.

*Proof.* A hop across the gradient joins sites with the same `w`, so its bond weight is `w(x₁)`, and `D_j` gives `sin k_j` on the plane wave. The runner checks this exactly for all 16 transverse wave numbers of a side-4 torus, with symbolic `λ` (family B). ∎

## Theorem T2 — the zero-energy solutions are exact geometric sequences

*Statement.*
- Divided by `λ^n`, `J_kψ = 0` reads `−(i/2)√λ σ₁ψ(n+1) + (i/2)σ₁ψ(n−1)/√λ + Mψ(n) = 0`, with `M = sin k₂σ₂ + sin k₃σ₃`.
- Its solutions are exactly `ψ(n) = (r/√λ)^n v`, where `r − 1/r = ±2m` and `v` is an eigenvector of `sin k₂σ₃ − sin k₃σ₂` with eigenvalue `(r − 1/r)/2`.
- The moduli are `|r| = √(1 + m²) + m` and its inverse `√(1 + m²) − m`, each twice.

*Proof.* Multiplying by `σ₁` turns the recurrence into an eigenvalue problem for `σ₁M = i(sin k₂σ₃ − sin k₃σ₂)`. The runner checks it exactly at `(sin k₂, sin k₃) = (3/5, 4/5)`, where `m = 1`, at five sites (family C). ∎

## Theorem T3 — the count at the fast end, and the threshold

*Statement.*
- `|ψ(n)|² = (|r|²/λ)^n`. The solutions with `|r| = √(1 + m²) − m ≤ 1 < √λ` are always square-summable at the fast end.
- Those with `|r| = √(1 + m²) + m` are square-summable exactly when `√(1 + m²) + m < √λ`, that is, when `m < m* = (λ − 1)/(2√λ) = sinh(g/2)`.
- So for `m < m*` all four solutions are square-summable there, and for `m > m*` two are.
- With the limit-point/limit-circle theory for matrix three-term operators imported at definition level, the sector's minimal operator has deficiency indices `(2,2)` for `m < m*` and `(0,0)` for `m > m*`.
  - The slow end is limit point: the sum of the inverse bond norms diverges there.
  - For `m < m*`, all solutions are square-summable at one energy, so at every energy.
  - For `m > m*`, the energy enters the scaled recurrence as `zλ^{−n}`, a summable perturbation, which leaves two square-summable solutions.
- Every sector has `m ≤ √2`, and `√(1 + 2) + √2 ≤ √λ` exactly when `λ ≥ 5 + 2√6`. Above that, every sector needs a condition.

*Proof.* Direct, from T2 (family D). The deficiency statements use the imported theory, as named. ∎

## Theorem T4 — the ray picture misses the small sectors

*Statement.*
- Along a ray of the static field, `E = w√(sin²k₁ + m²)` and `m` are kept. So a ray with `m > 0` turns back at `w = E/m` and never reaches the fast end.
- At `m = 0` all four roots have modulus one. This is block 108's line, whose fast end is reached in finite time.
- The sectors `0 < m < m*` need a fast-end condition although no ray with that `m` reaches the end.

*Proof.* The ray equations of block 54 T4 as landed, with the conserved energy. The finite sum is block 108's (family E). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 54 as landed (c3f8c47a58) T3: the evolution identity conditional on a realization; block 108 answered on the line"
source_of_blocker_text: the owner's landing of block 54; block 108
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "in 3D the fast-end condition is needed exactly in the sectors m < sinh(g/2); next: which conditions keep the translation identity sector by sector, and a clause that could supply them"
conditional_surface_status: "T1-T4 exact sector by sector; the deficiency statements through the imported matrix three-term theory"
hypothetical_axiom_status: "the walk, its clock and the exponential field are hypotheses; no fast-end condition follows from any clause; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Block 54** (#8570, landed) posed the realization question.
- **Block 108** answered it on the line.
- In the literature, the matrix-valued limit-point/limit-circle theory is Krein's and Berezanskii's; the discrete Levinson theorem handles summable perturbations; the direct integral is von Neumann's.
- **New here:**
  - the sector reduction;
  - the exact zero-energy solutions;
  - the threshold `m* = sinh(g/2)` and the whole-zone value `λ = 5 + 2√6`;
  - the contrast with the ray picture.

## Exact target and obligation graph

Target: which parts of the 3D clocked walk need a fast-end boundary condition. The obligations are:
- (O1) the sectors;
- (O2) the solutions;
- (O3) the count;
- (O4) the rays.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentence: sectors with `m > sinh(g/2)` need no boundary condition, since their minimal operator has deficiency indices `(0,0)`.

### N1 — Routes by which the sentence could fail or mislead
1. *The imported theory.* The deficiency count for `m > m*` rests on the summable-perturbation argument, which is imported. At zero energy the count is exact.
2. *Other fields.* Only the exponential field is treated.
3. *Coupled sectors.* The sectors are independent for a field that varies only along `x₁`; other fields couple them.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The imported theorems are named at definition level.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| block 54 (#8570, landed) | the walk; the question; the ray model | yes |
| block 108 (#8945) | the line | yes |
| block 53 (#8568, landed) | the clock | yes |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a fast-end condition is needed exactly in the sectors with small transverse momentum" | executed: the characteristic roots, their product and the threshold (symbolic) | executed: the 3D walk on a `5 × 4 × 4` box against the reduced line operator for 16 transverse wave numbers; exact solutions at five sites | executed: the square-summable count by sector; the ray turning point | executed: the whole zone beyond `λ = 5 + 2√6` | T1–T4 on `Z³` with `w = λ^{x₁}`, sector by sector, with the limit-point/limit-circle theory for matrix three-term operators imported at definition level; block 54 as landed supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Waves with transverse momentum should turn back like rays." *Reply:* The zero-energy solutions show they do not all turn back. For `m < sinh(g/2)` all four are square-summable at the fast end, so the evolution there is not fixed. That is a wave effect, and the ray picture misses it.

### N8 — Cross-cycle echo
- Block 54 posed the question.
- Block 108 settled the line.

This note settles three dimensions, sector by sector.

## Falsifiers

- A sector with `m < sinh(g/2)` that has fewer than four square-summable zero-energy solutions at the fast end.
- A transverse hop whose bond weight is not `w(x₁)`.

## Boundaries and non-claims

- The walk, the clock and the exponential field are supplied.
- The translation identity sector by sector is not worked out here.
- No boundary condition follows from the axioms, and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 53, 54 and 108, restated or placed.
- Named standard imports, at definition level:
  - the matrix limit-point/limit-circle theory (Krein, Berezanskii);
  - the discrete Levinson theorem;
  - the direct integral;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the fifty-seventh since the source-link direction opened, extending block 108.
- **Provenance.** The supervisor's own derivation, the same family as blocks 53 and 54. A probes unit on the 3D question is queued for an independent attempt and an other-family referee.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_three_dimensions_the_clocked_walk_needs_a_fast_end_condition_exactly_in_small_transverse_sectors_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
