---
claim_id: admissibility_rule_one_field_for_records_and_waves_a_wave_passing_a_record_turns_by_twice_the_pair_energy_at_that_distance_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the owner's moving-records reading, block 53's clock field of the records, block 95's pair law (with block 97's timing) and block 54's walk with its ray law. Exact: on every torus the kernel of one record summed along a lattice line is the plane kernel; for the far field 1/(4 pi r), the line integral of the transverse gradient at impact parameter b is exactly twice the potential at b; so, to first order in log(kappa) and for a straight passage, a long wave passing a record turns towards it by 2|U(b)|, U block 95's pair energy, which is 2 log g(b) for block 95's pair excess g. Executed: the lattice ratio of kick to pair energy (2.008 at b = 8, 2.0002 at b = 16); walk packets against clouds of rays in one record's field (1 to 8 per cent). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_one_field_for_records_and_waves_wave_turns_by_twice_the_pair_energy_2026_09_23.py
---

# One field for records and waves: a wave passing a record turns by twice the record's pair energy at that distance

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; first order in the field; nothing adopted or registered; unaudited)

This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) with block 53's clock field, block 95's pair law and block 54's walk; it reports how the one field that makes records clump turns a passing wave; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 94's scorecard left one row of the moving-records column at "supplied": one geometry for matter and fields. Block 95 (#8860) showed that records clump in block 53's clock field. Block 97 (#8872) fixed the sign. Block 54 (#8570) showed that a walk whose phase runs on the local clock falls towards slow clocks. This note ties the two together with one number, in terms of things that can be counted.

- **T1: a straight path feels the plane kernel.** On every torus, the kernel of one record, summed along a lattice line, is exactly the plane kernel at the transverse offset.
- **T2: twice the potential.** For the far field `1/(4πr)`, the transverse gradient integrated along a straight line at impact parameter `b` is exactly `−2 × 1/(4πb)`.
- **T3: a wave turns by twice the pair energy.** At long waves the walk's ray law has unit tensor and unit speed. So, to first order in `log κ`, a wave passing one record turns towards it by `δ(b) = 2|U(b)|`, where `U(b) = 6 log κ/(4πb)` is block 95's pair energy at that distance. Block 95's pair law gives the pair excess `g(b) = e^(−U(b))`, so

`δ(b) = 2 log g(b)`.

A wave passing a record turns by twice the log of how much likelier a second record is to be found at that distance.

*Corrigendum (2026-09-23): lengths double the turn.* The relation above is for block 54's product-form walk (lengths one). Block 59 (#8581) showed that with bond rates and lengths a wave's bending over a slow body's fall is `1 + β`. Block 60 (#8590) showed that its curvature member has `β = 1`, so the turn doubles, `δ(b) = 4|U(b)| = 4 log g(b)` at first order, if the records' pair law is unchanged by the lengths (not worked). The first version of this note said the lengths' contribution was not worked in the lane; it was, in blocks 59 and 60. That was missed by the supervisor's own-prior-art check.

*Executed.* On a 128-torus, the lattice kick divided by the lattice pair energy is `2.10, 2.04, 2.008, 2.003, 2.0002` at `b = 2, 4, 8, 12, 16`. Walk packets passing one record agree with clouds of rays carrying the packets' own spreads to within 1–8 per cent.

In plain terms: the same slow clocks that make records spend time near one another also bend a passing wave towards them. The bend is fixed by the clumping. Measure how much more often records are found at some distance from one another, take the log, double it, and that is the angle through which a wave passing at that distance turns. One field, one number, for matter and for waves.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`): no time metric; update laws open. Nothing is adopted.
- **Block 53's clock field** (#8568). `u = log w = 6 log κ Σ_r G(z − r)`, with `G` the zero-mean inverse of the lattice Laplacian. Far from a record, `G(r) → 1/(4π|r|)`.
- **Block 95's pair law and block 97's timing** (#8860, #8872). With `a = 1`, two records are found at separation `d` in proportion to `e^(−U(d))`, where `U(d) = 6 log κ G(d)`. The pair excess over large separations is `g(d) = e^(−U(d))` in the far field.
- **Block 54's walk and ray law** (#8570). A two-component amplitude whose phase runs on the local clock, `H_w = √W H √W`. Its rays of `E = w(x) ε(k)`, `ε = |sin k|`, obey `dv_j/dt = −w² M_jl ∂_l u + 2(v·∇u) v_j` with `M = Hess(ε²/2)` (block 54's T4, exact for rays; the walk against its rays was executed there and is executed again here).
- **Weak field and straight passage.** Deflections are computed to first order in `log κ` along the unperturbed straight line.

## Theorem T1 — a straight path feels the plane kernel

*Statement.* On the `L³` torus, `Σ_x G₃(x, y, z) = G₂(y, z)` for every `(y, z)`, where `G₂` is the zero-mean inverse of the plane Laplacian on the `L²` torus.

*Proof.* Summing over `x` keeps the modes with no component along the line. There the three-dimensional symbol equals the plane symbol, and the prefactor `L/L³` is `1/L²`. Exact on `4³` and `6³` at every transverse offset, with the plane kernel's defining identity at all 36 sites of `6²` (family B). ∎

## Theorem T2 — twice the potential

*Statement.* `∫_{−∞}^{∞} ∂_y (1/(4π √(x² + y²)))|_{y=b} dx = −1/(2πb) = −2 · 1/(4πb)`.

*Proof.* Exact integration (family C). ∎

## Theorem T3 — a wave turns by twice the pair energy

*Statement.*
1. For the walk, `M = diag(cos 2k_j)`. This is the identity at `k = 0`, and the speed along an axis tends to one.
2. At long waves the ray law is therefore `dv/dt = −∇u + 2(v·∇u)v` to first order. On a straight passage at impact parameter `b` from one record, the velocity turns by `δ(b) = −∫ ∂_⊥ u dl`.
3. With `u = 6 log κ/(4πr)` and `log κ < 0`, T2 gives `δ(b) = −(3/π)|log κ|/b`, towards the record, with size `2|U(b)|`. By block 95's pair law this is `2 log g(b)`.

*Proof.* The Hessian and the axis speed are symbolic (family E). The kick is from T2 (family D). The second term of the ray law is second order in the field on a straight passage. ∎

On the lattice the ratio of the kick to the pair energy is exactly the ratio of the plane kernel's transverse difference (T1) to the three-dimensional kernel. Both tend to their continuum forms, so the ratio tends to 2; W1 shows how fast. At finite wave number the lattice dispersion multiplies the velocity turn by `1/cos² k₀` along an axis (the ray law, with `v_x = cos k₀`).

## Executed control

Script `specs/supervisor_control_block98_one_geometry.py`, output in `.out.txt`; floating point, evidence and not proof.
- **W1.** On the 128-torus, with torus backgrounds removed, the straight-line kick is `0.02006` at `b = 8`, against `1/(2π·8) = 0.01989`. The kernel is `0.00999`, against `1/(4π·8) = 0.00995`. The ratio of kick to kernel is `2.10, 2.04, 2.008, 2.003, 2.0002, 1.992` at `b = 2, 4, 8, 12, 16, 24`; the last value feels the torus.
- **W2.** Walk packets were run past one record (`6 log κ = −3`, box `80³`, width 4). The change of the mean `sin k_y` for the walk and for a cloud of rays with the packet's own spreads, in the same lattice field, was:

  | Case | Walk | Cloud of rays | Walk / cloud |
  |---|---|---|---|
  | `k₀ = 0.8`, `b = 12` | `−0.01706` | `−0.01620` | `1.053` |
  | `k₀ = 0.8`, `b = 18` | `−0.01334` | `−0.01342` | `0.994` |
  | `k₀ = 0.5`, `b = 18` | `−0.00905` | `−0.00836` | `1.083` |

  The walk follows its rays in a record's field, and it turns towards the record. The first design had wide packets passing close to the record, and the packets' own spreads washed out the turn. It was replaced by narrower spreads at larger `b` before the comparison was made.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 94's scorecard row 'one geometry for matter and fields' for reading (iii): 'the walk and the clocks share Z^3 (supplied)'"
source_of_blocker_text: block 94 (#8840); the owner's request of 2026-09-23
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "one field for records and waves shown at first order; next candidates: the delayed clock law (the field follows the records late); formation with the clock (the jam); the size of gamma"
conditional_surface_status: "T1 exact on every torus; T2-T3 exact in the continuum far field at first order along a straight passage; the lattice ratio and the walk-against-rays comparison executed"
hypothetical_axiom_status: "the owner's reading, block 53's clock field, blocks 95 and 97's motion, block 54's walk are hypotheses; nothing adopted"
admitted_observation_status: "the comparator (light turning by twice the clock-only value) is mentioned only in N1 and N7, as a comparator"
audit_required_before_effective_retained: true
```

## Prior art and what is new

Block 54 (#8570) found that a walk timed by local clocks falls towards slow clocks. Its fall in the field of `N` records was `(3|log κ|/2π) N/r²`, and it compared walks with clouds of rays in uniform gradients. Block 95 (#8860) gave the pair law and block 97 (#8872) the timing and sign. The line integral of the gradient of `1/r`, and the resulting deflection at twice the potential, is the classical first-order deflection of a straight path by a central `1/r` potential (for light, Soldner's 1801 value in the physics comparator). The summation of a lattice kernel along a line to the kernel of one dimension fewer is standard.

New here:
- the relation between the two layers in counted terms, `δ(b) = 2|U(b)| = 2 log g(b)`, with the lattice ratio executed;
- the walk against its rays in a point source's field.

## Exact target and obligation graph

Target: the moving-records column's "one geometry" row, in counted terms. The obligations are:
- (O1) what a straight path past a record feels;
- (O2) the size of the turn;
- (O3) its relation to the records' pair law.

T1–T3 discharge them.

## No-Go Discipline Gate

The note makes no negative claim beyond scope. Its limits are:
- first order;
- straight passage;
- the far field;
- the long-wave limit.

### N1 — Routes by which the sentences could fail or mislead
1. *Strong fields* (near a condensed clump, where `u` is of order one). The ray bends appreciably and the first-order formula fails.
2. *Short waves.* The lattice dispersion adds `1/cos² k₀` and anisotropy.
3. *Wide packets passing close.* Their spreads wash out the mean turn (W2's first design).
4. *Lengths.* This note's walk is block 54's product form: bonds are crossed at `√(w_x w_y)` and every length is one. With block 59's bond rates and lengths, bending over fall is `1 + β` (block 59 T4–T5). Block 54's clauses give `β = 0`, which is this note's turn. Block 60's curvature member (#8590) gives `β = 1`, and at first order the turn doubles to `4|U(b)| = 4 log g(b)`, provided the records' pair law is unchanged by the lengths. That proviso is not worked. The probes' worker result #8862 (unrefereed, same model family) extends block 60's ratio exactly to all field strengths, `1 + 2/(1 + w₀/w) ∈ [2, 3)`.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
First order in the field, straight passage and the far field are stated. The ray law is block 54's.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no time metric | yes |
| block 53 (#8568) | the clock field of records | yes |
| blocks 95, 97 (#8860, #8872) | pair law, timing, sign | yes |
| block 54 (#8570) | the walk and its ray law | yes |
| blocks 59, 60 (#8581, #8590) | lengths: bending over fall `1 + β`; the curvature member `β = 1` doubles the turn | no (placement; see the corrigendum) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a long wave passing a record turns by 2\|U(b)\| = 2 log g(b)" | executed: line sums at every transverse offset on 4³, 6³ | executed: the plane kernel's identity on 6² | executed: control ratio and walk-against-rays | executed: continuum integral; ray tensor | T1 on every torus; T2–T3 at first order in the far field |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- Hostile reviewer: "This is block 54's fall plus block 95's pair law." Reply: yes. The content is the counted relation between them (`δ = 2 log g`), the exact line-sum identity behind it, and the walk checked in a point source's field.
- Second objection: "Twice the potential is only half of what light does in nature." Reply: that is outside this note (no gravitational claim). N1 route 4 names where the rest would have to come from.

### N8 — Cross-cycle echo
Block 94 scored "one geometry" as supplied, and block 96 placed the walk among the wave routes. This note gives the row a counted relation.

## Falsifiers

- A torus on which the line sum of the record kernel differs from the plane kernel.
- A walk packet in a record's field whose mean transverse wave vector departs from its cloud of rays by much more than the packets' spreads allow.

## Boundaries and non-claims

- The note holds at first order, for a straight passage, in the far field and at long waves.
- It is conditional on the cited clauses.
- No gravitational claim is made. Known physics appears only as a comparator, in N1 and N7.

## Imports
- `minimal_axioms`. Blocks 53, 54, 59–61, 94, 95, 97 (PRs): restated or placed.
- Named standard imports at definition level:
  - mode sums of lattice kernels;
  - the first-order deflection by a central `1/r` potential (Soldner, as the comparator's first value);
  - Runge–Kutta integration, sparse exponentials and interpolation for the control;
  - the lattice kernel at the origin, `0.2527310098`, as a literature value used only to align torus constants in W1.

## Review record
- **Corrigendum (2026-09-23, supervisor).** N1 route 4 and the per-citation table corrected: blocks 59 and 60 had already worked the lengths' contribution (bending over fall `1 + β`, curvature member `β = 1`). Found in the probe harvest through worker result #8862. Text only; no theorem, check or number changed.
- **Who and when.** Supervisor-run block, the forty-sixth since the source-link direction opened and the ninth run on Claude Opus 5.5.
- **What prompted it.** Block 94's "one geometry" row.
- **The control's first design failed.** Its wide packets (`σ = 5`, `k₀ = 0.25`) passed close to the record (`b = 6`–`14`), and their transverse spreads washed out the turn. The walk and the cloud then disagreed in sign at `b = 6`. The design was replaced before any comparison entered the note.
- **Independence.** No independent review has taken place. Mutation census: six mutations, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_field_for_records_and_waves_wave_turns_by_twice_the_pair_energy_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
