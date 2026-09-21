---
claim_id: admissibility_rule_the_two_step_momentum_is_the_only_one_among_conserved_covariant_momenta_of_reach_two_that_is_every_species_own_wave_number_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 63 and 69 (open PRs #8570, #8593, #8601; not adopted): block 54's walk H = sum_a sigma_a S_a with its eight zeros; relabellings G = (1/2) sum_j {xi_j, M_j} generated with a conserved momentum M_j, whose deformation of the walk, sum_a (1/2){sigma_a C_a[d_a xi_j], M_j}, has reach 1 + reach(M_j) and an exactly conserved response (the argument of blocks 63 and 69 uses only that M_j commutes with the walk and with translations). Block 69 T1 excluded momenta a sin k + b cos k + c along ONE axis and exhibited S_j C_j; its N1 left open other momenta. (T1) A translation-invariant operator of finite reach commutes with the walk iff its symbol is a(k) + c(k) H(k) with a, c trigonometric polynomials; reach(cH) = reach(c) + 1. (T2) No scalar symbol of reach <= 1 - any combination of 1, cos k_b, sin k_b over the three axes - vanishes at all eight zeros with gradient e_j. A relabelling generated with M_j = sum_b alpha_jb sin k_b shows species n the inverse metric (1 + B alpha D)^T (1 + B alpha D), the same for all species and all strains only if alpha = 0. A constant c_j is not a vector under the proper cubic rotations. Hence no relabelling of this kind with reach <= 2 shows all species one geometry. (T3) Among the 25 real trigonometric monomials of reach <= 2, the symbols vanishing at all eight zeros with gradient e_j are (1/2) sin 2k_j plus the span of the six functions sin k_b sin k_c (b <= c), each of second order at every zero. For M_1 to be unchanged by the quarter turn about axis 1 and to change sign under the half turn about axis 2 all six coefficients must vanish: (1/2) sin 2k_j is the only covariant scalar momentum of reach <= 2 that is every species' own wave number. The part along the walk allowed by covariance at this reach is gamma sin k_j H, of second order at every zero. (T4) For a uniform strain that part contributes to H(k) the scalar gamma sum B_a^j sin k_a sin k_j cos k_a, of second order at every zero: it makes no lengths. Hence, among relabellings generated with a conserved covariant momentum, block 69's coupling is the one of least reach with an exact current and one geometry for all eight species, and it is unique up to the second-order number gamma. NOT claimed: anything about couplings that are not a relabelling's deformation with a conserved momentum of this kind (in particular couplings whose response is conserved through a generator that is not local); that a coupling may reach three; which species are present; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_two_step_momentum_is_the_only_one_2026_09_21.py
---

# The two-step momentum is the only one: among conserved covariant momenta of reach two, only `½ sin 2k` is every species' own wave number

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about symbols of operators commuting with block 54's supplied walk; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin and for relabellings generated with a conserved momentum; it reports which conserved momenta of short reach are every species' own wave number; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 69 (open PR #8601) found *a* momentum that is the same for all eight species of the walk — the difference over two steps — and the relabelling it generates: exact books and one geometry for all, at reach three. Its first theorem excluded only momenta built from the shifts along one axis, and its gate left other momenta open. Blocks 70 and 72 (open PRs #8602, #8605) have since made the reach-two alternative untenable when reflected species are present. So it matters whether block 69's coupling is one of many or the only one.

1. **What can be conserved** (T1). An operator of finite reach that commutes with the walk and with translations is `a(k) + c(k)H(k)`: a scalar function of the shifts, plus a function of the shifts times the walk itself.
2. **Reach one: nothing** (T2). No scalar momentum of reach one — along an axis or mixing the axes in any way — is every species' own wave number, and one that is not shows the species different geometries. A part along the walk of this reach is not a vector.
3. **Reach two: exactly one** (T3). The candidates are `½ sin 2k_j` plus six functions that vanish to second order at every zero; asking that the momentum turn as a vector under the lattice's proper rotations removes all six.
4. **The part along the walk makes no lengths** (T4). What covariance allows of it at this reach, `γ sin k_j H`, is of second order at every zero, and its contribution for a uniform strain is a scalar of second order.

So, among relabellings generated with a conserved momentum that turns as a vector, block 69's coupling is the one of least reach with both properties, and it is unique up to one number that does not touch the geometry.

In plain terms: block 69 found a rule that looks three steps along the lattice, keeps exact momentum books and treats all eight kinds of walker alike. This note checks whether a shorter or a different rule of the same kind could do the same. None can: with two steps there is nothing, and with three the rule is the one already found.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 69 (PR #8601), N1.1 and N1.2: couplings not excluded by its T1 - momenta mixing axes; reach-two couplings with both properties; next_trace_action 'whether reach three is the least reach with both properties'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "within relabellings generated with a conserved covariant momentum the ladder is closed: reach three is least and block 69's coupling is unique up to gamma; still open: couplings that are not of this kind; the owner's fork on how far a supplied rule may reach"
conditional_surface_status: "T1 exact for translation-invariant operators of finite reach with the qubit as coin; T2, T3 exact for all scalar symbols of reach <= 1 and <= 2 on Z^3; T4 exact for every uniform strain"
hypothetical_axiom_status: "block 54's walk; relabellings generated with a conserved momentum; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom and its proper cubic rotations, the Qubit axiom's one-site algebra, the nearest-neighbour form of the Admissibility rule as the measure of reach, and the memo's silence on amplitude dynamics. Blocks 54, 63, 69 (open PRs) supply the walk and the relabellings.

- **Symbol.** A translation-invariant operator acts on plane waves through a `2 × 2` matrix of trigonometric polynomials in `k`; its **reach** is the largest number of steps `|m|₁` among its monomials `e^{im·k}`.
- **Own wave number.** A scalar symbol `a_j(k)` is every species' own wave number if it vanishes at each of the eight zeros `k = πn` with gradient `e_j` there.
- **Relabelling.** `G = ½Σ_j{ξ_j, M_j}` with `[M_j, H] = 0`; then `i[H, G] = Σ_a½{σ_aC_a[d_aξ_j], M_j}` and its expectation is the pairing of `d_aξ_j` with a current of the density of `M_j` (blocks 63, 69).
- **Covariance.** `M_j` turns as a vector under the 24 proper rotations acting on the lattice and on the coin together (block 54's soldered content); the walk is unchanged by them.

Nothing classical is used beyond the algebra of trigonometric polynomials.

## Prior art and what is new

New, inside the framework's vocabulary: the form of every conserved translation-invariant operator of the supplied walk; the exclusion of all scalar momenta of reach one, mixtures of axes included, with the inverse metric each would show the species; the complete list at reach two and its reduction to one by covariance; and that the part along the walk makes no lengths. No gravitational claim is made.

## Exact target and obligation graph

Target: whether block 69's coupling is of least reach and unique among relabellings generated with a conserved covariant momentum. Obligations: (O1) what can be conserved; (O2) reach one; (O3) reach two; (O4) the part along the walk. T1–T4 discharge them.

## Theorem T1 — what can be conserved

*Statement.* For `M(k) = a(k) + b(k)·σ`: `[M, H] = 2i(b × s)·σ`, `s_a = sin k_a`. `M` commutes with the walk iff `b = c s` with `c` a trigonometric polynomial, and then `reach(b) = reach(c) + 1`.

*Proof.* `[σ_a, σ_b] = 2iε_{abc}σ_c`. If `b × s = 0` then `b_1 sin k_2 = b_2 sin k_1`; `sin k_1` and `sin k_2` are polynomials in different variables `e^{±ik_1}`, `e^{±ik_2}` with no common factor, so `sin k_1` divides `b_1`, and `c = b_1/sin k_1 = b_2/sin k_2 = b_3/sin k_3`. The largest `|m|₁` of a product is the sum of the factors' largest. ∎

## Theorem T2 — reach one

*Statement.* (a) No real combination of `1, cos k_b, sin k_b` (`b = 1, 2, 3`) vanishes at all eight zeros with gradient `e_j`. (b) A relabelling generated with `M_j = Σ_bα_{jb} sin k_b` and a uniform strain give `H(k) = Σ_aσ_a[s_a + c_aΣ_jB_a^jM_j]`, and species `n` sees the inverse metric `(1 + BαD)ᵀ(1 + BαD)`. It is the same for every species and every strain only if `α = 0`. (c) A constant `c_j` is unchanged by every rotation and is a vector only if it vanishes.

*Proof.* (a) The gradient of `Σ_bα_b sin k_b` at `πn` is `(α_b(−1)^{n_b})_b`; for `b = j` it would have to equal 1 at `n_j = 0` and at `n_j = 1`. The cosines and the constant must vanish with the value. (b) Near `πn + q`: `s_a = D_aq_a`, `c_a = D_a`, `M_j = (αDq)_j`: the vector is `D(1 + BαD)q`. For `B = ε` times a matrix unit the first order in `ε` is linear in `αD`, which depends on `n` unless `α = 0`. (c) Immediate. ∎

## Theorem T3 — reach two

*Statement.* (a) Among real combinations of the 25 monomials of reach `≤ 2`, those vanishing at all eight zeros with gradient `e_1` are `½ sin 2k_1 + Σ_{b≤c}e_{bc} sin k_b sin k_c`, the `e_{bc}` arbitrary. (b) If `M_1` is unchanged by the quarter turn about axis 1 and changes sign under the half turn about axis 2, all six `e_{bc}` vanish. (c) The part along the walk with `c_j` of reach `≤ 1` and `M_j` a vector is `γ sin k_j H`.

*Proof.* (a) Thirty-two linear conditions on 25 coefficients; the runner solves them: one particular solution and six free directions, whose overlap matrix with the six functions `sin k_b sin k_c` has rank six. Each of these has a zero of second order at every `πn`. (b) The quarter turn sends `(k_2, k_3)` to `(k_3, −k_2)`: it turns `sin k_2 sin k_3` into its negative, so `e_{23} = 0`; it turns `sin k_1 sin k_2` into `sin k_1 sin k_3` and `sin k_1 sin k_3` into `−sin k_1 sin k_2`, so `e_{13} = e_{12}` and `e_{12} = −e_{13}`, and both vanish. The half turn sends `(k_1, k_3)` to `(−k_1, −k_3)` and leaves the three squares unchanged, where `M_1` must change sign: `e_{11} = e_{22} = e_{33} = 0`. (c) The half turn about axis 2 must reverse `c_1`: constants and cosines are excluded, and `sin k_2` is; the quarter turn about axis 1 then excludes `sin k_3`. ∎

## Theorem T4 — the part along the walk makes no lengths

*Statement.* For a uniform strain, `Σ_{a,j}B_a^j½{σ_aC_a, γ S_jH}` has the symbol `γΣ_{a,j}B_a^j s_a s_j c_a` times the identity; at `k = πn + q` it is `γΣB_a^jD_jq_aq_j + O(q⁴)`.

*Proof.* `½{σ_a, σ·s} = s_a`. `s_ac_a = q_a + O(q³)` and `s_j = D_jq_j + O(q³)`. ∎

The walk's energies near a zero are `± |(1 + B)q| + O(q²)`: a scalar of second order changes no length and no angle. It depends on the species through `D_j`; whether `γ` is present is one more number of the supplied coupling, not examined further.

## Executed (supervisor control; floating point; numerical linear algebra; evidence, not proof)

`specs/supervisor_control_block73_only_momentum.py` (no symbolic algebra; singular values of sampled linear systems). **W1**: all translation-invariant operators `Σ_{|m|₁≤R}A_me^{im·k}` with `A_m` complex `2 × 2`, the condition `[M(k), H(k)] = 0` at 200 random wave vectors: null spaces of dimension `8, 32, 88` for `R = 1, 2, 3`, equal to the count of `a + cH` (`7 + 1`, `25 + 7`, `63 + 25`), with a gap of fourteen orders between kept and dropped singular values. **W2**: the 32 conditions as a numerical matrix: reach one — rank 7, least-squares residual `2.83` (not solvable); reach two — rank 19, nullity 6, solvable; `½ sin 2k_1` meets them to `2e-16`; the six functions `sin k_b sin k_c` meet the homogeneous conditions to `5e-16` and have rank six. **W3**: under the eight proper rotations that send `e_1` to `±e_1`, sampled at 40 wave vectors, the six functions have singular values between `8.2` and `22.7` — no combination of them turns as the first component of a vector — while `½ sin 2k_1` violates no condition.

## No-Go Discipline Gate

The note's negative sentences: no scalar momentum of reach one is every species' own wave number; at reach two there is no second covariant one.

### N1 — Routes by which the sentences could fail or mislead
1. *Couplings that are not a relabelling's deformation of this kind.* A coupling whose response is conserved through a generator that is not `½{ξ, M}` with `M` local, conserved and translation-invariant is outside. So are couplings through the curls alone (their response is conserved identically and they make no lengths for uniform strains).
2. *A momentum that is not a vector.* Without covariance the six functions of T3(a) are allowed; they are of second order at every zero and would not change the geometry at leading order either.
3. *A weaker demand.* "Own wave number" is sufficient for one geometry; T2(b) shows that at reach one it is also necessary.
4. *Fewer species.* If only the first species were present, `sin k_j` would serve (block 63).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Three dimensions, the cubic lattice, the qubit as coin, the identity frame, uniform strain in T2(b) and T4.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its proper rotations; nearest-neighbour as the measure of reach | yes (premise) |
| block 54 (open PR #8570) | the walk; the coin turning with the lattice | yes (restated) |
| blocks 63, 69 (open PRs #8593, #8601) | relabellings generated with a conserved momentum; the two-step momentum | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "conserved operators are `a + cH`; nothing at reach one; exactly one at reach two; the part along the walk makes no lengths" | executed: the commutator as `2i(b × s)·σ`; a parallel and a non-parallel example | not applicable: statements about symbols; the operators were checked site by site in blocks 69 and 70 | executed: the 32 conditions on 7 and on 25 monomials; the inverse metric through a general reach-one momentum for all eight species; the part along the walk at each zero | executed: six free directions against six second-order functions (rank six); two rotations against six coefficients | every symbol of the stated reach on `Z³`; couplings of other kinds outside |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "This is an exercise in trigonometric polynomials." Reply: yes; its use is that block 69's price list now has no unlisted cheaper item of the same kind, which the decision record could not say before. Second objection: "Couplings of other kinds are the interesting ones." Reply: N1.1 names them and the note claims nothing about them; the four demands now on the ladder (exact current, one geometry, the energy reversal, the ledger's requirement for every species) make their classification a finite computation, queued.

### N8 — Cross-cycle echo
Block 63: the books need reach two. Block 68: reach two shows the species different geometries. Block 69: reach three has both. Blocks 70, 72: reach two cannot hold reflected species. Here: nothing shorter, and nothing else at that length.

## Falsifiers

- A real combination of `1, cos k_b, sin k_b` vanishing at all eight zeros with gradient `e_j`.
- A scalar symbol of reach `≤ 2`, a vector under the proper cubic rotations, that is every species' own wave number and is not `½ sin 2k_j`.
- An operator of finite reach commuting with the walk and with translations whose symbol is not `a + cH`.

## Boundaries and non-claims

Only relabellings generated with a conserved, translation-invariant, covariant momentum are covered. Whether a supplied coupling may reach three is not decided and is not proposed. Which species are present is not decided. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom and its proper rotations, the Qubit axiom's one-site algebra, the nearest-neighbour form of the Admissibility rule, the memo's silence on amplitude dynamics. Blocks 54, 63, 69 (PRs #8570, #8593, #8601, open): restated or placed.
- Named standard imports at definition level: trigonometric polynomials and their unique factorisation; linear systems over the rationals; the commutation relations of the coin's matrices.

## Review record
Supervisor-run block, the twenty-first of the source-link direction and the seventeenth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: covariance is taken under the proper rotations only, as the Lattice axiom names them, with the coin turning with the lattice as block 54 supplied; nothing is recommended. A rigour lens: the supervisor first considered claiming least reach for *all* couplings with an exactly conserved response and withdrew it — the step from "the response is divergence-free on every stationary state" to "the coupling is a relabelling's deformation with a local generator" was not proved, and the note claims only the class it covers (N1.1); T2(b) was added so that "own wave number" is shown necessary at reach one and not merely sufficient; the runner's E1 mutation was first a flipped constant and was replaced by a computed condition before the gates; the control's first count of the commutant at reach three was wrong (132 against 88) because 60 sampled wave vectors give fewer equations than unknowns — raised to 200, after which all three counts agree. A strategy lens: the block is small and closes a named gap in block 69's gate, so that the decision record's ladder can say "least" and "only" within a stated class. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_two_step_momentum_is_the_only_one_2026_09_21.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
