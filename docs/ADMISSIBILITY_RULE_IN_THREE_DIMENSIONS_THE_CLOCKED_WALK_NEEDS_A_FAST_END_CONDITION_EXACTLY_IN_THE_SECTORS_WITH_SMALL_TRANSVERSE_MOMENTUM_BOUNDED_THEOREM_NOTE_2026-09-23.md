---
claim_id: admissibility_rule_in_three_dimensions_the_clocked_walk_needs_a_fast_end_condition_exactly_in_the_sectors_with_small_transverse_momentum_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Supplied exponential 3D walk: exact sector recurrence and threshold m*=sinh(g/2). Scalar-chain endpoint theory gives deficiency (2,2) below the threshold and (0,0) at or above it; the whole zone is limit circle only for lambda>5+2sqrt(6). No physical selection or arrival theorem."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_bounded_theorem_note_2026-09-23
runner: scripts/admissibility_rule_in_three_dimensions_the_clocked_walk_needs_a_fast_end_condition_exactly_in_small_transverse_sectors_2026_09_23.py
---

# In three dimensions the clocked walk needs a fast-end boundary condition exactly in the sectors with small transverse momentum: |(sin k₂, sin k₃)| < sinh(g/2), including waves the ray picture turns back

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact sector identities with the limit-point/limit-circle theory for matrix three-term operators imported at definition level; supervisor's derivation extending block 108; nothing adopted or registered; unaudited)

This note works within the supplied clock clause and walk of blocks 53 and 54, as landed on main, and extends block 108 to three dimensions; it reports which transverse sectors of the clocked walk in an exponential clock field need a boundary condition at the fast-clock end; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical endpoint, spectral and calculus results are explicit imports within their stated hypotheses; they supply no physical premise or audit verdict.

## Result up front

Block 108 found that on the line, in a clock field `w = λ^x`, the walk's dynamics needs a boundary condition at the fast-clock end. That answers, on the line, the realization question in block 54 as landed on main. In three dimensions, with the clock growing along `x₁`:

- **T1: sectors.** A plane wave across the gradient, `exp(i(k₂x₂ + k₃x₃))`, reduces the walk to a line operator. The hops across the gradient become an on-site term `w(x₁)(sin k₂σ₂ + sin k₃σ₃)` that grows with the clock.
- **T2: exact zero-energy solutions.** Dividing by `λ^n` makes each sector's zero-energy recurrence constant. A basis of solutions is geometric: `ψ(n) = (r/√λ)^n v`, with `r − 1/r = ±2m`, where `m = |(sin k₂, sin k₃)|`.
- **T3: the threshold.**
  - At the fast end, two of the four solutions are always square-summable. The other two are square-summable exactly when `m < m* = (λ − 1)/(2√λ) = sinh(g/2)`.
  - So a sector needs a fast-end boundary condition exactly when its transverse momentum is small: deficiency indices `(2,2)` below `m*` and `(0,0)` above.
  - Every sector needs one once `λ > 5 + 2√6`.
- **T4: rays miss it.** A ray with transverse momentum `m > 0` keeps its energy `E = w√(sin²k₁ + m²)`, so it turns back before `w` exceeds `E/m` and never reaches the fast end. Yet the sectors `0 < m < m*` still need a boundary condition: there the wave equation's solutions are square-summable at the fast end, where no ray goes.

The relevant sector variable is the transverse sine momentum, not the angle of a continuum velocity. It is also small near transverse zone-edge zeros. The endpoint-domain conclusions and the ray obstruction concern different mathematical questions. Equality at the threshold is limit point, as proved below.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The walk and its clock are supplied clauses. Nothing is adopted.
- **The walk** (block 54, #8570, as landed in c3f8c47a58).
  - `H = Σ_jσ_jD_j`, with `D_j = (i/2)(T_j − T_j†)` and `(T_eψ)(x) = ψ(x − e)`.
  - `H_w = W^{1/2}HW^{1/2}`.
  - T3 as landed leaves the evolution identity conditional on a realization; T4 as landed is a conditional ray model.
- **Block 108** (#8945, landed in 8cc5f114f0) answers the question on the line: deficiency indices `(2,2)`, with the endpoint theory as a stated import. As landed, its inverse-clock sum is a scalar series, not an arrival-time theorem.
- **The clock.** `w = λ^{x₁}`, `λ = e^g > 1`, the same on each plane of constant `x₁`.
- **Sectors.** For transverse wave numbers `(k₂, k₃)`, the sector operator is `J_k` on the line. Its minimal operator acts on finitely supported sequences, and the full operator is their direct integral.
- **Names.** The limit-point/limit-circle theory for matrix three-term operators is due to Krein and to Berezanskii. A constant spin rotation and a parity-spin decomposition reduce each sector to two scalar three-term operators; the endpoint theorem used below is stated under Imports. The direct-integral decomposition is von Neumann's.

## Theorem T1 — sectors across the gradient

*Statement.* For `w = λ^{x₁}` and `ψ(x) = exp(i(k₂x₂ + k₃x₃))f(x₁)`, the clocked walk acts as `(J_kf)(x₁) = (σ₁D₁)_w f(x₁) + w(x₁)(sin k₂σ₂ + sin k₃σ₃)f(x₁)`.

*Proof.* A hop across the gradient joins sites with the same `w`, so its bond weight is `w(x₁)`, and `D_j` gives `sin k_j` on the plane wave. The runner checks this exactly for all 16 transverse wave numbers of a side-4 torus, with symbolic `λ` (family B). ∎

## Theorem T2 — the zero-energy solutions are exact geometric sequences

*Statement.*
- Divided by `λ^n`, `J_kψ = 0` reads `−(i/2)√λ σ₁ψ(n+1) + (i/2)σ₁ψ(n−1)/√λ + Mψ(n) = 0`, with `M = sin k₂σ₂ + sin k₃σ₃`.
- A basis of solutions is given by `ψ(n) = (r/√λ)^n v`, where `r − 1/r = ±2m` and `v` is an eigenvector of `sin k₂σ₃ − sin k₃σ₂` with eigenvalue `(r − 1/r)/2`.
- The moduli are `|r| = √(1 + m²) + m` and its inverse `√(1 + m²) − m`, each twice.

*Proof.* Multiplying by `σ₁` turns the recurrence into an eigenvalue problem for `σ₁M = i(sin k₂σ₃ − sin k₃σ₂)`. The runner checks it exactly at `(sin k₂, sin k₃) = (3/5, 4/5)`, where `m = 1`, at five sites (family C). ∎

## Theorem T3 — the count at the fast end, and the threshold

*Statement.*
- `|ψ(n)|² = (|r|²/λ)^n`. The solutions with `|r| = √(1 + m²) − m ≤ 1 < √λ` are always square-summable at the fast end.
- Those with `|r| = √(1 + m²) + m` are square-summable exactly when `√(1 + m²) + m < √λ`, that is, when `m < m* = (λ − 1)/(2√λ) = sinh(g/2)`.
- So for `m < m*` all four solutions are square-summable there, and for `m ≥ m*` two are.
- With the limit-point/limit-circle theory for matrix three-term operators imported at definition level, the sector's minimal operator has deficiency indices `(2,2)` for `m < m*` and `(0,0)` for `m ≥ m*`.
  - The slow end is limit point: the sum of the inverse bond norms diverges there.
  - For `m < m*`, all solutions are square-summable at one energy, so at every energy.
  - For `m > m*`, the energy enters the scaled recurrence as `zλ^{−n}`, a summable perturbation, which leaves two square-summable solutions.
- Every sector has `m ≤ √2`, and `√(1 + 2) + √2 < √λ` exactly when `λ > 5 + 2√6`. Above that, every sector needs a condition.

*Proof.* Direct, from T2 (family D). The deficiency statements follow from the explicit scalar-chain reduction and endpoint import below. ∎

## Theorem T4 — the ray picture misses the small sectors

*Statement.*
- Along a ray of the static field, `E = w√(sin²k₁ + m²)` and `m` are kept. So a ray with `m > 0` turns back at `w = E/m` and never reaches the fast end.
- At `m = 0` all four roots have modulus one. This is block 108's line, whose inverse-clock sum toward the fast end is finite. The scalar series alone establishes no arrival-time statement for rays or wave packets.
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
- In the literature, the matrix-valued limit-point/limit-circle theory is Krein's and Berezanskii's; the scalar endpoint alternative handles both sides of the threshold; the direct integral is von Neumann's.
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
1. *The imported theory.* The deficiency count for `m ≥ m*` rests on the explicit two-chain reduction and scalar endpoint theory. At zero energy the count is exact, including equality.
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
| block 108 (#8945, landed) | the line | yes |
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

The scalar-chain reduction also resolves equality as limit point.

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
  - the scalar endpoint alternative specified below;
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

Expected: `TOTAL: PASS=12 FAIL=0`.

## Corrigendum 2026-09-24 (after the owner's landing 8cc5f114f0)

Block 108 was landed with its domain conclusions resting on the stated endpoint theory, and with its inverse-clock sum read as a scalar series, not an arrival-time theorem. This note's T4 and its plain terms now say that the small sectors need a condition because their solutions are square-summable at the fast end, not that waves arrive there. The runner's message for E1 says the same. T1–T4, and every check, are unchanged.

## Endpoint proof including equality

For m>0 a constant rotation about the sigma_1 axis takes M to m sigma_3 and leaves sigma_1 fixed. For m=0 use the identity rotation. The two invariant chains consist respectively of spin-up at even sites/spin-down at odd sites and the reversed pattern. Multiplication by i^n on each chain turns the off-diagonal bonds into positive b_n=lambda^(n+1/2)/2. Their real diagonal entries are respectively +(-1)^n m lambda^n and -(-1)^n m lambda^n.

At zero energy, one-step transfer matrices alternate between

    A_plus = [[-2m/sqrt(lambda), -1/lambda], [1,0]],
    A_minus = [[2m/sqrt(lambda), -1/lambda], [1,0]].

For either order the two-step eigenvalues are -rho^2/lambda and -rho^(-2)/lambda, rho=sqrt(1+m^2)+m. For m>0 they are distinct, so on each scalar chain both independent zero solutions are square-summable at the fast end exactly when rho^2<lambda. At equality the first eigenvalue is -1, giving a nondecaying solution; above it that solution grows. For m=0 the two-step matrix is -I/lambda, so both solutions decay. The slow end is limit point because the reciprocal-bond sum diverges there.

The scalar endpoint alternative and energy independence of the all-solutions square-summability condition now suffice: at the fast end each chain is limit circle below the threshold and limit point at or above it. Each chain contributes deficiency (1,1) in the first case and (0,0) in the second, since the slow end is limit point. Their direct sum gives (2,2) and (0,0), respectively. No matrix-valued asymptotic theorem or unproved persistence at a unit-modulus root is needed.

## Imports — scalar endpoint source

[Gerald Teschl, Jacobi Operators and Completely Integrable Nonlinear Lattices, section 2.6](https://www.mat.univie.ac.at/~gerald/ftp/book-jac/jacop.pdf), Lemma 2.15 and the limit-point/limit-circle and deficiency discussion, supply the energy-independent endpoint alternative; the reciprocal-bond criterion supplies the slow-end conclusion. Positive real bonds and real diagonal coefficients are established explicitly above. These are mathematical imports, not numerical conclusions or physical premises.

## Canonical source dependencies

- [admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied parent within its landed scope.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied parent within its landed scope.
- [admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_IN_AN_EXPONENTIAL_CLOCK_FIELD_THE_WALKS_DYNAMICS_NEEDS_A_BOUNDARY_CONDITION_AT_THE_FAST_CLOCK_END_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied parent within its landed scope.
