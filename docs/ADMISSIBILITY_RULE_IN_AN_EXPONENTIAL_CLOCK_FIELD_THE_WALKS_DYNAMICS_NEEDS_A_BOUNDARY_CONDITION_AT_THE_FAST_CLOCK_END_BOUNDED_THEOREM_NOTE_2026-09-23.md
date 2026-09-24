---
claim_id: admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clock clause and walk of blocks 53 and 54 as landed on main (c3f8c47a58), on the infinite line with w = lambda^x, lambda > 1. Exact: (T1) the clocked line walk H_w = W^(1/2) sigma_x D W^(1/2) is hermitian on finitely supported vectors, splits into two independent chains, and satisfies H_w T_a = lambda^a T_a H_w there. (T2) At zero energy each chain has two solutions, one component on one parity with value lambda^(-m), both square-summable on the fast side and growing on the slow side; each chain is, after a phase gauge, the real three-term chain matrix with zero diagonal and bonds b_n = lambda^(n+1/2)/2, whose Carleman sum diverges on the slow side and is finite on the fast side. With the limit-point/limit-circle theory imported at definition level, each chain is limit point at the slow end and limit circle at the fast end, so the minimal operator has deficiency indices (2,2): the lattice clause does not fix the dynamics, and a boundary condition at the fast-clock end must be supplied. (T3) The summation-by-parts identity places the boundary form at the ends; the self-adjoint realizations that keep the chains separate are the conditions lim W_n(psi, v) = 0 at the fast end with v a real zero-energy solution of each chain. (T4) The shift by two multiplies every zero-energy solution by lambda, so every such realization keeps the evolution identity U(t) T_2 = T_2 U(lambda^2 t); the shift by one carries chain A's solutions onto chain B's, so exactly the realizations whose chain-B condition is the image of the chain-A condition keep U(t) T_a = T_a U(lambda^a t) for every a; and the fast end is reached in finite label time (sum over x >= x0 of 1/w_x = lambda^(-x0)/(1 - 1/lambda)). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_2026_09_23.py
---

# In an exponential clock field the walk's dynamics needs a boundary condition at the fast-clock end: deficiency indices (2,2) on the line; every condition keeps the even-translation identity, and a circle of them keeps it for every translation

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact identities on the infinite line with the limit-point/limit-circle theory imported at definition level; supervisor's own derivation, same model family as blocks 53–54; nothing adopted or registered; unaudited)

This note works within the supplied clock clause and walk of blocks 53 and 54, as landed on main; it reports what the walk's generator needs in an exponential clock field on the infinite line before its evolution is defined, and which realizations keep the translation identity; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 54 (#8570) was landed on main (c3f8c47a58) with a precise caveat in its T3. The translation identity `H_w^n T_a = λ_a^n T_a H_w^n` holds on finitely supported amplitudes. But "on an infinite exponential field the generator is unbounded and needs a compatible self-adjoint realization", and the evolution identity `U(t)T_a = T_aU(λ_a t)` is left conditional on one. This note answers that question on the line.

- **T1: two chains and the scaling.** For `w = λ^x`, the clocked line walk splits into two independent chains, and `H_wT_a = λ^aT_aH_w` on finitely supported vectors.
- **T2: the fast end needs a boundary condition.**
  - At zero energy each chain has two solutions. Both are square-summable towards fast clocks, and both grow towards slow clocks.
  - Each chain is, after a phase gauge, a real three-term chain matrix with bonds `λ^{n+1/2}/2`.
  - Each chain is therefore limit point at the slow end and limit circle at the fast end. The walk's generator has deficiency indices `(2,2)`: the lattice clause does not fix the dynamics.
- **T3: the realizations are boundary conditions at the fast end.** For each chain, the chain-separate self-adjoint realizations are the conditions `lim W_n(ψ, v) = 0` at the fast end, with `v` a real zero-energy solution: one angle per chain.
- **T4: which conditions keep the translation identity.**
  - A shift by two multiplies every zero-energy solution by the same number `λ`. So every such condition keeps `U(t)T_2 = T_2U(λ²t)`.
  - A shift by one carries one chain's solutions onto the other's. So exactly the conditions whose second chain's angle is the image of the first's keep `U(t)T_a = T_aU(λ^a t)` for every `a`. They form a circle.
  - The fast end is reached in finite label time: `Σ_{x≥x₀} 1/w_x = λ^{−x₀}/(1 − 1/λ)`.

In plain terms: when clocks speed up without limit in one direction, a walker heading that way gets to "the end of the lattice" in a finite time. The rule says nothing about what happens there, so a boundary condition has to be supplied. The evolution then exists, and for a circle's worth of choices the promised identity holds exactly: a walker moved towards faster clocks does everything proportionally faster. Nothing else makes that choice; it is one more thing the records do not supply.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The walk and its clock are supplied clauses. Nothing is adopted.
- **The walk** (block 54, #8570, as landed in c3f8c47a58, "Clocked nearest-neighbour amplitudes: finite operator identities and conditional ray motion").
  - `(Tψ)(x) = ψ(x − 1)` and `D = (i/2)(T − T†)`, with symbol `sin k`.
  - The line walk is `σ_x D`, and `H_w = W^{1/2}σ_xDW^{1/2}`.
  - T3 as landed gives the finite-power identity and leaves the evolution identity conditional on a realization.
- **The clock** (block 53, #8568, landed): positive local rates. Here the rates form an exponential field `w_x = λ^x`, `λ > 1`, as in block 54's identity.
- **Chains.** Chain A is `{(up, even x), (down, odd x)}` and chain B is `{(up, odd x), (down, even x)}`, each ordered along the line.
- **Realizations.** The minimal operator is `H_w` on finitely supported vectors. Its self-adjoint extensions are the realizations, and the deficiency indices count their freedom.
- **Names.** The limit-point/limit-circle alternative for Jacobi matrices is Weyl's. The divergence test is Carleman's. The extension theory is von Neumann's. The discrete Green identity is the Christoffel–Darboux form of the Wronskian.

## Theorem T1 — two chains and the scaling identity

*Statement.* For `w = λ^x`, `H_w` is hermitian on finitely supported vectors. No entry joins chain A to chain B. For `a = 1, 2`, `H_wT_a = λ^aT_aH_w` on finitely supported vectors.

*Proof.* `σ_x` exchanges the components, and `D` moves one site, so each entry joins (up, x) to (down, x ± 1). The scaling follows from `√(w_{x+a}w_{y+a}) = λ^a√(w_xw_y)`. The runner checks both exactly on windows with symbolic `λ` (family B). ∎

## Theorem T2 — each chain is limit circle at the fast end; deficiency indices (2,2)

*Statement.*
- (a) The four sequences with one component on one parity, with value `λ^{−m}` at `x = 2m` or `x = 2m + 1`, solve `H_wψ = 0`. Each chain contains two of them.
- (b) Each has squared norm `λ²/(λ² − 1)` on the fast side, and grows on the slow side.
- (c) In the gauge `ψ_n → i^nψ_n`, each chain is the real three-term chain matrix with zero diagonal and bonds `b_n = λ^{n+1/2}/2`. The sum of `1/b_n` diverges on the slow side and is finite on the fast side.
- (d) Hence each chain is limit point at the slow end and limit circle at the fast end. Its minimal operator has deficiency indices `(1,1)`, and the walk's are `(2,2)`.

*Proof.* (a)–(c) are exact computations (family C).
- (d) On the slow side, the diverging sum of `1/b_n` makes that end limit point (Carleman's test, imported).
- On the fast side, both zero-energy solutions are square-summable, so all solutions are, for every energy, and that end is limit circle (the limit-point/limit-circle alternative, imported).
- A chain with one limit-point end and one limit-circle end has deficiency indices `(1,1)`, and the two chains add. ∎

## Theorem T3 — the realizations are boundary conditions at the fast end

*Statement.* For a real chain `J`, `Σ_{k=1}^{N}[(Ju)_kv_k − u_k(Jv)_k] = W_0(u, v) − W_N(u, v)`, with `W_k(u, v) = b_k(u_kv_{k+1} − u_{k+1}v_k)`. Hence the boundary form of the maximal operator sits at the ends. Only the fast end contributes, because the slow end is limit point. The self-adjoint realizations that keep the chains separate are the conditions `lim_{n→∞} W_n(ψ, v_θ) = 0` at the fast end, one for each chain, where `v_θ = cos θ χ + sin θ φ` and `χ`, `φ` are the chain's two real zero-energy solutions.

*Proof.* The identity is exact (family D). The description of the realizations is the standard one for a limit-circle end (imported at definition level). ∎

Realizations that mix the two chains at the fast end also exist, since the deficiency indices are `(2,2)`. They are not needed below.

## Theorem T4 — translations and the realizations

*Statement.*
- (a) The shift by two multiplies each of the four zero-energy solutions by the same number `λ`. It therefore maps every real line of solutions to itself. Every chain-separate realization satisfies `T_2^{−1}H_θT_2 = λ²H_θ`, and hence `U(t)T_2 = T_2U(λ²t)`.
- (b) The shift by one carries chain A's solutions (up on even, down on odd) onto chain B's (up on odd, down on even). A pair of conditions `(θ_A, θ_B)` is kept by it exactly when `θ_B` is the image of `θ_A`. For that circle of realizations, `U(t)T_a = T_aU(λ^a t)` holds for every integer `a`.
- (c) The fast end is reached in finite label time: `Σ_{x≥x₀} 1/w_x = λ^{−x₀}/(1 − 1/λ)`.

*Proof.*
- (a) and (b) are exact on windows (family E).
- The Wronskian of shifted sequences is the shifted Wronskian times a constant ratio of bonds, so a shift maps the condition set by `v` to the condition set by the shifted `v`.
- (c) is a geometric sum (family E). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 54 as landed (c3f8c47a58) T3: the evolution identity is conditional on a self-adjoint realization in an exponential field, not established there"
source_of_blocker_text: the owner's landing of block 54 (review caveat)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "on the line the realizations are boundary conditions at the fast end, and a circle of them keeps the identity for every translation; next: the three-dimensional walk (transverse momentum adds site terms growing with the clock), and what boundary condition, if any, a clause could supply"
conditional_surface_status: "T1-T4 exact on the infinite line with the limit-point/limit-circle theory imported at definition level; chain-mixing realizations not classified"
hypothetical_axiom_status: "the walk, its clock and the exponential field are hypotheses; the boundary condition at the fast end is not supplied by any clause; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Block 54** (#8570, landed in c3f8c47a58) gave the finite-power identity. It left the realization open, and withdrew its exact packet force.
- **Block 105** (#8934) showed that discrete ticks keep a local clock exactly only for walks that do not move; this note is the continuous-time side.
- **Block 53** (#8568, landed) gave the clock.
- In the literature, the limit-point/limit-circle alternative is Weyl's, the divergence test Carleman's, and the extension theory von Neumann's; the Jacobi-matrix setting is standard.
- **New here:** the deficiency indices of the clocked walk in an exponential field, the realizations as fast-end boundary conditions, and exactly which of them keep the evolution identity.

## Exact target and obligation graph

Target: whether the walk's evolution in an exponential clock field is defined, and whether the identity `U(t)T_a = T_aU(λ^a t)` holds. The obligations are:
- (O1) structure;
- (O2) the ends' types;
- (O3) the realizations;
- (O4) the translations.

T1–T4 discharge them on the line.

## No-Go Discipline Gate

The note's negative sentence: the lattice clause alone does not fix the walk's dynamics in an exponential clock field on the infinite line.

### N1 — Routes by which the sentence could fail or mislead
1. *A finite lattice.* On a finite window every realization question disappears. The statement is about the infinite line, where block 54 posed it.
2. *A clause at infinity.* A supplied boundary condition fixes the dynamics. The note says which conditions keep the identity; it does not say that the axioms supply one.
3. *Three dimensions.* Transverse momentum adds site terms that grow with the clock. The deficiency indices in 3D are not computed here.
4. *Non-exponential fields.* For fields whose rates grow slowly enough that the sum of `1/w` diverges, the fast end is limit point and no condition is needed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The imported theorems are named at definition level. The walk and the clock are supplied.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| block 54 (#8570, landed) | the walk and the finite-power identity; the open realization question | yes |
| block 53 (#8568, landed) | the clock | yes |
| block 105 (#8934) | placement | no |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the dynamics needs a boundary condition at the fast end; every condition keeps the even-translation identity, a circle keeps it for all" | executed: the bond entries, the chain split and the gauge to a real chain (symbolic λ) | executed: the four zero-energy solutions at every interior site of a window; the scaling identity at every site of a window for `a = 1, 2` | executed: the square sums and Carleman sums on both sides; the summation-by-parts identity | executed: the action of the shifts by one and two on the zero-energy solution spaces of both chains | T1–T4 on the infinite line for `w = λ^x`, `λ > 1`, with the limit-point/limit-circle theory imported at definition level; block 54 as landed supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "An exponential field on the whole line is unphysical." *Reply:* It is the field in which block 54 stated its identity. The note answers the question as posed. For fields whose `1/w` sums diverge, no condition is needed (N1.4).
- *Objection:* "The boundary condition is arbitrary." *Reply:* Yes, and that is the content. The records and the rule do not choose it. A circle of choices keeps the translation identity.

### N8 — Cross-cycle echo
- Block 54 posed the realization question.
- Block 105 settled discrete ticks.

This note settles continuous time on the line.

## Falsifiers

- A zero-energy solution of a chain that is not square-summable on the fast side.
- A chain-separate realization not kept by the shift by two.
- A finite sum of `1/b_n` on the slow side.

## Boundaries and non-claims

- The walk, the clock and the exponential field are supplied, not adopted.
- The work is on the line; three dimensions are open.
- Realizations that mix the chains are not classified.
- No boundary condition is claimed to follow from the axioms, and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 53, 54 and 105 (PRs), restated or placed.
- Named standard imports, at definition level:
  - the limit-point/limit-circle alternative for Jacobi matrices (Weyl);
  - Carleman's test;
  - von Neumann's extension theory;
  - the discrete Green identity;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the fifty-sixth since the source-link direction opened, written to answer the realization question in the owner's landed block 54.
- **Provenance.** The supervisor's own derivation, the same family as blocks 53 and 54. A probes unit with the same question (and the 3D case) is queued for an independent attempt and an other-family referee.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
