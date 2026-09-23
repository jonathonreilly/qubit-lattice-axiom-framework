---
claim_id: admissibility_rule_the_zero_field_bound_on_the_formation_bilayer_a_held_sources_kernel_without_a_field_in_3plus1_and_no_memory_on_planes_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the formation reading of the Record axiom with block 90's supplied light-cone clause (block 19's rule on the sphere) in dimension 2 and 3; the sphere ferromagnet on block 90's bilayer torus at zero field; a rotation-derivation inequality carried from block 20 to the bilayer, its algebra exact; in 3+1 combined with block 90's long-range-order bound and block 91's response identity; on planes combined with exact lattice sums; the infinite-volume constant beta_0 executed; the plane statement qualitative at accessible sizes"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_zero_field_bound_on_the_formation_bilayer_held_source_kernel_in_3plus1_no_memory_on_planes_2026_09_23.py
---

# The zero-field bound on the formation bilayer: a held source's kernel without a field in 3+1, and no memory on planes

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (an exact inequality at zero field; in 3+1 a two-sided window for a held source's response in every finite volume, with no passage to infinite volume and no named import; on planes, no common direction at any coupling; nothing adopted or registered; unaudited)

This note works within the formation reading of the Record axiom with the supplied light-cone clause of block 90; it reports a zero-field lower bound on the formation bilayer, with what it gives in 3+1 and on planes; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 90 (open PR #8692) showed that under the light-cone clause forming records keep a common direction in 3+1 for `β > 0.5905`. Block 91 (open PR #8696) showed that their answer to a held source lies between `⟨m⟩²/(⟨P_b⟩E(k) + ε⟨m⟩)` and `1/E(k)`. That lower side needs a uniform field `ε`, a passage to infinite volume, and a named step from long-range order to a spontaneous direction. Block 90 also left open whether light-cone formation forgets on planes. Block 20 (PR #8154) had a lower bound that works at zero field, against the long-range-order parameter itself; it was built for the static law. Carried to the formation bilayer, it closes both gaps.

1. **The zero-field inequality (T1).** On the bilayer torus in two or three dimensions, at zero field, for every `k ≠ 0`:

   `u(k) ≥ (M²/3)² / (βE(k) + 2/(3V))`,

   where `u(k) = V⁻¹⟨|Σ_u e^{−ik·x_u} s¹_u|²⟩` is the symmetric branch's structure factor, `M² = ⟨|V⁻¹Σ_u s_u|²⟩` the long-range-order parameter over both levels, and `V = 2N` the number of vertices. The rungs join equal phases and carry no weight, so the bilayer has the single layer's stiffness per vertex and block 20's argument goes through unchanged. A simpler last step gives `2/(3V)` where block 20 had `4/(3N)`.
2. **In 3+1: a held source's window with no field and no limit (T2).** Block 91's response is `R̂(k) = βu(k)`. Block 90's sum rule gives `M² ≥ 1 − β_L/β`. So in every finite volume, at zero field, for `β > β_L`:

   `((1 − β_L/β)/3)² / (E(k) + 2/(3βV))  ≤  R̂(k)  ≤  1/E(k)`,

   and in the limit `((1 − β₀/β)/3)²/E(k) ≤ R̂(k) ≤ 1/E(k)` for every `β > β₀ = 0.5905`. The floor is weaker than block 91's (at most `1/9` of the inverse Laplacian, against block 91's measured `0.94 … 0.98`). It needs no field, no infinite volume and no import. This is the unconditional statement that a held source is answered, at every wave vector, by a positive fraction of the inverse lattice Laplacian, and never more than all of it.
3. **On planes: no memory (T3).** In two dimensions the plane's lattice sum grows like the harmonic numbers, and the sum rule gives `M⁴ ≤ (6π²β + 1/2)/H_{L/2−1}`. A level's own parameter differs from the bilayer's only by the staggered antisymmetric term, at most `3/(20βN)`. So a level's mean record direction tends to zero as the plane grows, at every `β`. Light-cone formation keeps no common direction on planes. The bound is qualitative: it bites only when `H_{L/2−1}` exceeds `6π²β + 1/2`, at sides far beyond any simulation. The executed plateaus fall slowly with the side, as the theorem requires.

So the dimension decides: under the light-cone clause, forming records keep a common direction in three dimensions of space above a proved coupling, and never in two. Where they keep it, a held source is answered by the lattice's inverse Laplacian, a positive fraction of it at every wave vector, and this holds at zero field. In plain terms: records that form by looking at the record beneath them and its neighbours hold a shared direction in a world with three dimensions of space, but not with two. In three, a steady pull at one place spreads through them exactly like the potential of a point source, with a strength that cannot fall below a definite fraction.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 90's open question (does light-cone formation forget on planes?) and block 91's conditions (a uniform field, infinite volume, and a named passage from long-range order to a spontaneous direction for the lower side)"
source_of_blocker_text: blocks 90 and 91
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "zero-field window ((1 - beta_L/beta)/3)^2/(E + 2/(3 beta V)) <= R^(k) <= 1/E(k) in 3+1 in every finite volume; no common direction on planes at any beta; next: the two-source interaction; the small-k limit; the level-ordered law; an other-family referee"
conditional_surface_status: "T1 for every even L in d = 2, 3 and every beta, by block 20's argument with the bilayer's stiffness sum, its algebra checked; T2 for every even L and beta > beta_L with block 90's T4 and block 91's T2 and upper side; T3 for every even L and beta on planes, with exact lattice sums and the plane's reflection structure; beta_0 executed"
hypothetical_axiom_status: "the light-cone formation clause; the sphere menu and block 19's rule; the coupling beta; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Record axiom ("Records form"; permanence), the Admissibility axiom (one covariant nearest-neighbour rule), and the Lattice axiom. Block 90 supplies the light-cone clause, the doubled graph, the bilayer, Gaussian domination and the sum-rule bound on `M²`; block 91 the response identity `R̂ = 2βN⁻¹⟨|Ŝ_+|²⟩` and the upper side; block 20 (PR #8154, closed and archived) the zero-field lower-bound argument and the plane's shell count; block 19 (open PR #8153) the rule on the sphere. Nothing is adopted here.

- **Bilayer torus in dimension `d`.** Two copies of `(Z/L)^d` (`L` even) with nearest-neighbour bonds and one rung per site; `V = 2N` vertices, `N = L^d`; the sphere ferromagnet at coupling `β` and zero field, which is block 90's doubled graph after the parity relabelling.
- **`u(k)`** the symmetric branch's structure factor as above; **`M²`** the long-range-order parameter over both levels; `E(k) = Σ_j (2 − 2cos k_j)`; `H_n` the harmonic numbers.
- **A level's parameter** `⟨|m_0|²⟩`, `m_0` the mean record direction of one level.

The lower-bound argument is the classical Bogoliubov inequality in the zero-field form that block 20 used, after the Mermin–Wagner theorem; its first use on the static law is block 19's (the G-series). None is used as authority; every step is re-derived or checked here.

## Prior art and what is new

Block 19 proved the static law's transverse channel two-sided, with the Bogoliubov inequality at zero field against the long-range-order parameter; block 20 made it dimension-free and showed that the static law never orders on planes or lines. Blocks 90–91 made the light-cone formation law an equilibrium bilayer and wrote a held source's response as its covariance. New here: the zero-field inequality on the formation bilayer (the rungs carry no weight, so nothing changes but the vertex count), with a simpler last step; the unconditional window for a held source in 3+1, in every finite volume; and the answer to block 90's open question, that light-cone formation keeps no common direction on planes.

## Exact target and obligation graph

Target: remove block 91's conditions, and settle planes. Obligations: (O1) the zero-field inequality on the bilayer; (O2) its combination with blocks 90 and 91 in 3+1; (O3) the plane's lattice sum and a level's parameter. T1–T3 discharge O1–O3.

## Theorem T1 — the zero-field inequality on the bilayer

*Statement.* For `d ∈ {2, 3}`, even `L`, `β > 0` and every `k ≠ 0`: `u(k) ≥ (M²/3)²/(βE(k) + 2M²/(3V)) ≥ (M²/3)²/(βE(k) + 2/(3V))`.

*Proof.* Let `D = Σ_u c_u L_u`, with `c_u = e^{ik·x_u}` and `L_u` the rotation of `s_u` about `e₂`; let `A = Σ_u c̄_u s¹_u`, `m³ = V⁻¹Σ_u s³_u` and `F = A m³`. Integration by parts on the spheres and Cauchy–Schwarz give `|⟨DF⟩|² ≤ β⟨|F|²⟩⟨D̄DH⟩` (block 91 T3, block 20 H1). Here `DA = Vm³` and `Dm³ = −V⁻¹Ā`, so `⟨DF⟩ = V⟨(m³)²⟩ − V⁻¹⟨|A|²⟩ = V M²/3 − u(k)`, the first term by rotation invariance at zero field. Next, `⟨|F|²⟩ ≤ ⟨|A|²⟩ = V u(k)` because `|m³| ≤ 1`. And `⟨D̄DH⟩ ≤ Σ_{edges}|c_u − c_v|² = V E(k)`: rungs 0, and the two slabs each give `N E(k)`. With `a = M²/3` and `x = u`: `V(a − x/V)² ≤ βV E x`. The identity `(βE + 2a/V)x − a² = βEx − (a − x/V)² + x²/V²` then gives `x ≥ a²/(βE + 2a/V)`, and `a ≤ 1/3`. Family B checks the derivation identities on a symbolic configuration, the quadratic identity and the weakening, and Parseval on the `4 × 4` bilayer. ∎

## Theorem T2 — in 3+1, a held source's window at zero field

*Statement.* In 3+1, for every even `L` and `β > β_L = (3/2)(G_L + H_L)` (block 90), block 91's response at zero field satisfies

`((1 − β_L/β)/3)² / (E(k) + 2/(3βV))  ≤  R̂(k)  ≤  1/E(k)`  for every `k ≠ 0`,

and every limit point as `L → ∞` lies between `((1 − β₀/β)/3)²/E(k)` and `1/E(k)`, `β₀ = (3/2)(I₀ + I₂)`.

*Proof.* `R̂ = 2βN⁻¹⟨|Ŝ_+|²⟩` (block 91 T2) and `A = 2Ŝ_+`, so `R̂ = βu`. T1 and block 90's sum rule, `M² ≥ 1 − β_L/β` (block 90 T4, first inequality), give the floor. The ceiling is block 91 T3's upper side. `β_L → β₀` as the lattice sums tend to their integrals. Family C checks `R̂ = βu`, recomputes `β_4` and `β_6` exactly, evaluates the floors at `β = 1` on `4³` and `6³`, and checks the limit form. ∎

## Theorem T3 — on planes, no common direction

*Statement.* In 2+1, for every even `L ≥ 4` and every `β > 0`: `M⁴ ≤ (6π²β + 1/2)/H_{L/2−1}` and `⟨|m_0|²⟩ ≤ M² + 3/(20βN)`. Hence `⟨|m_0|²⟩ → 0` as `L → ∞`.

*Proof.* Summing T1 over `k ≠ 0` against the sum rule `Σ_k u(k) ≤ V/3`, with `E(k) ≤ |k|²`, `2/(3V) ≤ |k|²/(12π²)`, and `Σ_{k≠0}|k|⁻² ≥ (N/π²)H_{L/2−1}` (block 20's shell count on the grid `k = 2πn/L`), gives `(M²/3)²(N/π²)H_{L/2−1} ≤ (β + 1/(12π²))·2N/3`, which rearranges to the stated bound. A level's mean is `m_bil + N⁻¹Ŝ_−(π)`, with no cross term by the slab swap. The staggered term is at most `3/(2βN(E(π) + 2)) = 3/(20βN)` by the infrared bound of the antisymmetric branch, which holds on planes by the same reflection structure. Family D checks the plane's relabelling (L = 4, 6), its reflection structure (4 × 4), its stiffness sum, the shell count for every even `L` from 4 to 24, the dyadic growth of `H`, `2 − 2cos t ≤ t²`, the small term, and the final algebra. Family E checks the level-mean identity by enumeration and the staggered bounds in 2+1 and 3+1. ∎

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block92_zero_field_planes.py`, output in `.out.txt`).

*W1 — light-cone formation on planes.* Five predecessors, aligned start, the plateau `|m|` over the second half of 2000 levels:

| `β` | side 16 | 32 | 64 | 128 |
|---|---|---|---|---|
| 1 | 0.393 | 0.289 | 0.107 | 0.073 |
| 2 | 0.809 | 0.777 | 0.751 | 0.729 |
| 4 | 0.910 | 0.897 | 0.887 | 0.878 |

The plateau falls with the side at every `β` tried: fast at `β = 1`, and at `β = 2` and `4` slowly and steadily (about 3 and 1 per cent per doubling), as a slow power of the side would.

*W2 — the 3+1 floor at zero field.* `((1 − β₀/β)/3)² = 0.0186, 0.0552, 0.0717, 0.0903` at `β = 1, 2, 3, 6`, tending to `1/9`; block 91 measures `R̂(k)E(k)` at about `0.94, 0.96, 0.98` at `β = 1, 2, 3`. The unconditional floor is valid and far from tight.

*W3 — where the plane bound bites.* The right side of `M⁴ ≤ (6π²β + 1/2)/H_{L/2−1}` falls below one only when `H_{L/2−1} > 6π²β + 1/2`: at `β = 0.1` for `L/2` of order `350`, at `β = 1` of order `10^{25}`. The theorem is qualitative at every size a simulation reaches; W1 is the evidence at those sizes.

## No-Go Discipline Gate

The note's negative sentence: on planes, light-cone formation keeps no common direction at any coupling.

### N1 — Routes by which the sentence could fail or mislead
1. *The clause.* Only the light-cone past is covered; the level-ordered past is not reversible and not covered (blocks 26, 28 executed its forgetting on planes).
2. *Size.* The bound is qualitative: it is below one only when `H_{L/2−1} > 6π²β + 1/2`, far beyond accessible sides; the executed plateaus fall slowly.
3. *The menu.* The sphere menu; a discrete menu can order on planes (block 17 for the static law).
4. *Provenance.* The route is block 20's (the supervisor's earlier campaign) carried to the bilayer; this block is by Claude Opus 5.5; an other-family referee is owed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The sphere menu; even tori; zero field; the aligned start in the simulator.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | "Records form"; one covariant nearest-neighbour rule | yes (premise) |
| block 90 (open PR #8692) | the clause; the bilayer; Gaussian domination; `M² ≥ 1 − β_L/β` | yes |
| block 91 (open PR #8696) | the response identity; the upper side | yes (T2) |
| block 20 (PR #8154, closed and archived) | the zero-field argument; the shell count | yes (re-derived) |
| block 19 (open PR #8153) | the rule on the sphere; the static law's window | yes (placed) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "zero-field window in 3+1; no common direction on planes" | executed: derivation identities; Parseval; the level-mean identity | executed: the plane relabelling, reflections and stiffness sum | executed: stiffness sums at every wave vector; lattice sums L = 4 to 24; control plateaus | executed: the quadratic step and final algebra; floors on 4³ and 6³ | T1–T3 for every even L with the stated scope

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "This is block 20 again." Reply: the argument is block 20's; what is new is where it lands. On the formation bilayer it answers block 90's open question for records that form, and it turns block 91's conditional floor into an unconditional one. Second objection: "The 3+1 floor is weak." Reply: agreed. At most `1/9` of the inverse Laplacian, where block 91 measures about `0.95`. Its point is that no field, no limit and no import are needed.

### N8 — Cross-cycle echo
Block 20: the static law never orders on planes. Blocks 26 and 28: the level-ordered formation law forgets on planes (executed). Block 90: light-cone formation remembers in 3+1. Here: it forgets on planes, and in 3+1 its answer to a held source is a positive fraction of the inverse Laplacian at zero field.

## Falsifiers

- A symbolic configuration on which `DF ≠ V(m³)² − V⁻¹|A|²`.
- A plane side for which the shell-count inequality fails, or a wave vector at which the plane's stiffness sum is not `2N E₂(k)`.
- A torus of even side in 3+1 with a zero-field response below `((1 − β_L/β)/3)²/(E(k) + 2/(3βV))` for some `β > β_L`.

## Boundaries and non-claims

The light-cone clause, the sphere menu and block 19's rule are supplied; the level-ordered past is not covered; `β₀` is executed; the plane bound is qualitative at accessible sizes; the 3+1 floor is weak; no statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Record, Admissibility and Lattice axioms. Blocks 19, 20, 90, 91 (PRs): restated or used as machinery.
- Named standard imports at definition level: integration by parts on the sphere and Cauchy–Schwarz (the classical Bogoliubov inequality); Parseval's identity; reflection positivity and the infrared bound (block 90); harmonic numbers; floating-point simulation for the control.

## Review record
Supervisor-run block, the fortieth since the source-link direction opened; the formation lane; the fourth run on Claude Opus 5.5. Found while writing block 91: blocks 19 and 20 already held the static law's window and a zero-field lower side, which removes block 91's conditions when carried to the bilayer, and answers block 90's question on planes. Lens pass, in writing, by the supervisor: a foundations lens — the clause is supplied; only the light-cone past is covered; a rigour lens — the derivation identities are checked on a symbolic configuration, the quadratic step is an exact identity, the plane's lattice sums are exact for every even side up to 24, and the qualitative nature of the plane bound is stated with the size at which it bites. Mutation census: seven mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_zero_field_bound_on_the_formation_bilayer_held_source_kernel_in_3plus1_no_memory_on_planes_2026_09_23.py
```

Expected: `TOTAL: PASS=17 FAIL=0`.
