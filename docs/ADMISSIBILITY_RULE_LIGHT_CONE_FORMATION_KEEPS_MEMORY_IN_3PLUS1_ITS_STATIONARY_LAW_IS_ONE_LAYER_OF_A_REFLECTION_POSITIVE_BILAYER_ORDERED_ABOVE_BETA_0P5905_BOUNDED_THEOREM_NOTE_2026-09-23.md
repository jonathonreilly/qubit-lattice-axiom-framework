---
claim_id: admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_its_stationary_law_is_one_layer_of_a_reflection_positive_bilayer_ordered_above_beta_0p5905_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the formation reading of the Record axiom with a supplied light-cone clause (the record at level t + 1 and site x forms from the seven records of level t at x + {0, +-e_j}, with block 19's exponential zonal rule on the sphere, weight e^{beta s'.h}); the level-to-level chain on the 3D torus; detailed balance exact on rings with symbolic t = e^beta, and its failure for the level-ordered past by an exact three-step cycle; the doubled graph's relabelling exact on the 4^3 and 6^3 tori and the bilayer's eigenvectors exact on 4^3; the reflection family's structure exact on 4^3 and Gaussian domination by block 19's G2 argument (open PR #8153); the sum rule exact with exact finite-size thresholds on tori of side 4 and 6; the infinite-volume constant, the onset and the finite-size plateaus executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_stationary_law_one_layer_of_a_reflection_positive_bilayer_2026_09_23.py
---

# Light-cone formation keeps memory in 3+1: its stationary law is one layer of a reflection-positive bilayer, ordered above β = 0.5905

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact reversibility, relabelling, reflection structure and sum rule; long-range order for β above an executed constant 0.5905; the route is the probes' derivations re-derived; nothing adopted or registered; unaudited)

This note works within the formation reading of the Record axiom with a supplied light-cone clause (a record forms from the seven records of the previous level around it, by block 19's rule on the sphere); it reports that the formation chain is reversible and that its stationary law keeps memory in 3+1 above a proved coupling; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

**Corrigendum (2026-09-23): status and prior art.** Status: the clause behind this note (a record at every site of `Z³` at every tick, each drawn from the previous tick's records) is the clause that block 36 (open PR #8507, 2026-09-20) found EXCLUDED by the axioms memo as written: "A site never carries more than one record; records are permanent." Every result here is conditional on that clause and would need an axiom change; it is not a reading the memo permits. Under the memo as written every site is recorded once (Z³ read as spacetime, blocks 05–35), where blocks 13, 26 and 35 found that a continuous menu loses its memory and that no three-dimensional inverse-Laplacian kernel appears; the owner's reading of 2026-09-20 (records move; one record per site at a time) is a third reading, not this one. Prior art: block 36 (open PR #8507) already proved, under the same clause, the light-cone chain's reversibility and the doubled graph as a bilayer (its T2), the sum-rule bound `⟨|m₀|²⟩ ≥ 1 − (3/(2β))(G_L + H_L)` with long-range order for `β > (3/2)(I₀ + I₂)` and the rigorous bound `β₀ < 0.5914` from block 22's bracket for `I₀` (its T3), and the linear response `7/E(k)` (its T4). This note re-derived them without citing block 36. New here: the cycle criterion for the level-ordered past, the spectrum checked eigenvector by eigenvector, the layer-halves minor, the exact finite thresholds and an independent simulator.

## Result up front

The owner's reading of the Record axiom is that records form (2026-09-18: "records form" means records form; the static law is only the equilibrium comparator). Blocks 26 and 28 (open PRs #8170, #8172) found that the sphere formation law in level time forgets on two-dimensional planes. The probes' scans (2026-09-18 to 22) found the opposite on three-dimensional planes: a plateau of the mean record direction that does not decay with the plane's size. This note proves it for the light-cone clause, where each new record forms from the record below it and that record's six neighbours.

1. **Light-cone formation is reversible (T1).** With a symmetric past, the chain from one level to the next satisfies detailed balance with `π(s) = Π_x Z(h_x(s))`, `h_x` the sum of the seven records below `x`. The joint law of two successive levels is the sphere ferromagnet `Π e^{β s·s'}` on the doubled graph that joins each record to its seven predecessors. So the formation law's own long-time law is one layer of that ferromagnet. Exact on rings for two-valued and six-axis contents with symbolic `e^β`. With the level-ordered past the chain is reversible with respect to no law: around a three-step cycle of configurations the forward and backward probabilities differ by the factor `e^{8β}`.
2. **A parity relabelling makes it a bilayer (T2).** `(x, a) ↦ (x, a ⊕ parity(x))` carries the doubled graph edge by edge onto the bilayer torus: two copies of the cubic lattice with nearest-neighbour bonds, joined by one rung per site. Its spectrum is `E(k)` and `E(k) + 2`, the doubled graph's `{E, 14 − E}`, checked eigenvector by eigenvector on the `4³` bilayer.
3. **Reflection positive with slab halves, not layer halves (T3).** The bilayer's bond planes and the plane between its slabs have no fixed vertex, and every bond crossing one joins a site to its own mirror image. Every bond crosses some reflection. So block 19's argument gives Gaussian domination and the infrared bounds `1/(βE(k))` and `1/(β(E(k) + 2))`. With the two levels as halves, a minor of the reflection kernel is negative for every `β` (`⟨d, Md⟩ = −64` on a cube, `−20N` on the torus): the relabelling is not a convenience, it is where the positivity lives.
4. **Memory (T4).** The sum rule over both branches gives `⟨|m|²⟩ ≥ 1 − (3/(2β))(G_L + H_L)` for the stationary law's mean record direction. Exact finite-size values: `β_4 = 18239/35840 ≈ 0.5089`, `β_6 = 27735979/51891840 ≈ 0.5345`. In infinite volume, **long-range order for `β > (3/2)(I₀ + I₂) = 0.5905`**, where `I₀ = W/6 = 0.25273` is the cubic lattice's return integral in closed form and `I₂ = 0.14093` is executed.
5. **Executed.** The probes' scans put the onset between `β = 0.55` (the plateau halves from plane 32 to 48) and `0.60` (it holds: `0.418`, `0.411`). My own simulator, independent of theirs, puts it between `0.55` (`0.126 → 0.088` from 24 to 32) and `0.58` (`0.351 → 0.339`). Above it the plateau approaches a positive limit like `m∞ + b/L` (`m∞ ≈ 0.633, 0.759, 0.853` at `β = 0.75, 1, 1.5`, planes 16 to 96). The proved bound lies between 2 and 8 per cent above the executed onset. The level-ordered clause keeps a plateau too (onset between `1.1` and `1.3`, `m∞ ≈ 0.73` at `β = 2`), but it is not reversible and is not proved here.

So under the light-cone clause, forming records in three spatial dimensions keep a common direction whose strength does not fade with the size of space, once the rule's preference exceeds `0.5905`. On two-dimensional planes the level-ordered law loses it (blocks 26, 28); whether the light-cone law does is not settled here (its stationary law is then a layer of a two-dimensional bilayer). In plain terms: if each new record is formed by looking at the record underneath it and that record's six neighbours, then in a world with three dimensions of space the records settle into a shared direction that does not fade however large the world is, provided the rule's preference for agreement is above a definite strength.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "memory 'Formation in 3+1 lead' (2026-09-18) and the probes' derivations lightcone-formation and lightcone-long-range-order (round 1 and 2; issues #8463, #8631): the light-cone law's long-range order, proved by one model family, unrefereed"
source_of_blocker_text: 2026-09-23 harvest
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "long-range order of light-cone formation in 3+1 for beta > 0.5905 (executed constant), onset executed in (0.55, 0.58); next: the level-ordered clause (not reversible; derivation queued), the onset against the proved bound (scan queued), the kernel of the ordered law against the inverse lattice Laplacian (the gravity node, blocks 29 and 35), and the owner's choice of formation clause"
conditional_surface_status: "T1 for every ring and every contents menu with weights e^{beta s.s'} by the symmetry of the stencil, checked on rings, and its failure for every stencil with N != -N by the three-step cycle, checked on the ring and on 4^3; T2 for every even L by parity, checked on 4 and 6; T3's structure for every even L, checked on 4, with Gaussian domination by block 19's G2 argument; T4 for every even L with the infinite-volume constant executed"
hypothetical_axiom_status: "the light-cone formation clause; the sphere menu and block 19's rule; the coupling beta; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Record axiom ("Records form"; permanence), the Admissibility axiom (one covariant nearest-neighbour rule), the Lattice axiom and its silence on which records are the "nearest-neighbor conditions" of a record that forms. Block 19 (open PR #8153) supplies the rule on the sphere and the Gaussian-domination argument (G1–G3); blocks 26 and 28 (#8170, #8172) the two-dimensional formation results. Nothing is adopted here.

- **The light-cone clause (supplied).** Levels `t = 0, 1, 2, …`, each a configuration of unit vectors `s_t(x)`, `x ∈ (Z/L)³`. The record at `(t + 1, x)` forms with density proportional to `e^{β s'·h}`, `h = Σ_{d ∈ N7} s_t(x + d)`, `N7 = {0, ±e_j}`, independently over `x` given level `t`. `Z(h) = ∫ e^{β s'·h} ds'`.
- **The level-ordered clause (comparator).** The same rule with the past `{0, −e_1, −e_2, −e_3}` (four predecessors: the event lattice in level order). Its memory is scanned, not proved.
- **The doubled graph `Γ_L`.** Vertices `(x, a)`, `a ∈ {0, 1}`; edges `(x, 0)–(x + d, 1)`, `d ∈ N7`. `μ_L ∝ Π_{edges} e^{β s·s'}`.
- **The bilayer torus.** Two copies of `(Z/L)³` with nearest-neighbour bonds and one rung `(x, 0)–(x, 1)` per site.
- **Reflections.** Bond planes perpendicular to each axis acting on both slabs; the swap of the slabs. Halves as stated in T3.
- **Sums.** `E(k) = 6 − 2Σcos k_j`; `G_L = N⁻¹Σ_{k≠0} 1/E(k)`; `H_L = N⁻¹Σ_k 1/(E(k) + 2)`; `I₀`, `I₂` their integrals.
- **Mean record direction.** `m₀ = N⁻¹Σ_x s_{(x,0)}`.

That a reversible level-to-level chain has as stationary law a marginal of a pair law symmetric in its two levels is the usual construction of reversible probabilistic cellular automata (Künsch; Dai Pra, Louis and Rœlly); the Gaussian-domination and infrared-bound method is that of Fröhlich, Simon and Spencer, with reflection positivity after Osterwalder and Schrader; the integral `W` is Watson's for the simple cubic lattice. The route of T1–T4 is the probes' (derivation units `lightcone-formation` and `lightcone-long-range-order`: issues #8463 and #8631 and the attempt of worker `w-macbookpro90c72-j451b`), all by one model family and not yet refereed by another. None is used as authority; every step is re-derived or checked here.

## Prior art and what is new

Blocks 26–28 showed that the sphere formation law forgets on two-dimensional level planes and mapped memory for other menus. The probes derived light-cone reversibility (round 1) and the slab route to long-range order (round 2), and found that the layer halves fail. The probes' scans located the onsets. New here, inside the framework's vocabulary: the whole chain written as one theorem with exact checks at every finite step (detailed balance for two menus and its failure for a one-sided past; the relabelling on two tori; the reflection family's structure; the no-go for layer halves; exact finite-size thresholds), an independent simulator for the onset, and the comparison of the proved constant with it. No gravitational claim is made.

## Exact target and obligation graph

Target: memory of the light-cone formation law in 3+1. Obligations: (O1) its stationary law; (O2) a positive structure; (O3) domination and the infrared bound; (O4) the sum rule. T1–T4 discharge O1–O4.

## Theorem T1 — light-cone formation is reversible

*Statement.* For any contents menu and weights `e^{β s·s'}` and a stencil with `N = −N`, the level-to-level chain satisfies `π(s)P(s'|s) = π(s')P(s|s')` with `π(s) = Π_x Z(h_x(s))`; the pair law of two successive levels is `μ ∝ Π_{x, d ∈ N} e^{β s'_x·s_{x+d}}`, and `π` is its one-level marginal. With a stencil for which `N ≠ −N`, in particular the level-ordered past `{0, −e_1, −e_2, −e_3}`, the chain is reversible with respect to no law, for every menu that contains a pair of opposite contents: if `a` and `b` are a uniform configuration with one record reversed, at `x` and at `x − d₀` for some `d₀ ∈ N` with `−d₀ ∉ N`, the cycle `a → b → −a → a` has forward and backward transition products in the ratio `t⁸`.

*Proof.* `π(s)P(s'|s) = Π_x e^{β s'_x·h_x(s)} = exp(β A(s', s))`, `A(s', s) = Σ_{x,d} s'_x·s_{x+d}`, which is symmetric in `(s, s')` iff `N = −N`. Around any cycle the partition functions `Z(h_x)` cancel, so the forward-to-backward ratio of `a → b → c → a` is `t` to the power `B(b, a) + B(c, b) + B(a, c)`, `B(u, v) = A(u, v) − A(v, u)`. With `c = −a` this is `2B(b, a)`. The uniform part drops out on the torus, and `B(b, a) = 4([d₀ ∈ N] − [−d₀ ∈ N]) = 4`. For positive transition probabilities a cycle with unequal products excludes reversibility with respect to any law. Family B checks detailed balance for every pair of configurations on a ring of four (two-valued) and a ring of three (four six-axis contents), with symbolic `t = e^β`; it computes the cycle's ratio `t⁸` from the transition probabilities on the ring of four with the past `{0, −1}`, and the exponent `8` (level-ordered) against `0` (light-cone) on the `4³` torus. For the sphere menu the transition density is continuous, and the violated identity holds on a neighbourhood of the cycle. ∎

## Theorem T2 — the doubled graph is a bilayer

*Statement.* `f(x, a) = (x, a ⊕ parity(x))` maps `Γ_L` onto the bilayer torus edge by edge for every even `L`. The bilayer's Laplacian has the branches `E(k)` and `E(k) + 2`, and `E(k + (π,π,π)) = 12 − E(k)`.

*Proof.* The self-edge joins equal parities and becomes a rung; a shifted edge joins opposite parities and lands in one slab. Checked edge by edge on `4³` (448 edges) and `6³` (1512). On the `4³` bilayer every vector `i^{n·x}(1, ±1)` satisfies the eigenvalue equation exactly at every vertex, with eigenvalue `E(k)` or `E(k) + 2`; the 128 characters are orthogonal, so this is the whole spectrum. Family C. ∎

## Theorem T3 — reflection positivity with slab halves, not layer halves

*Statement.* (a) For each reflection of the bilayer's family, no vertex is fixed, every edge crossing it joins a vertex to its mirror image, and every edge crosses some reflection. So the ferromagnet on the bilayer is reflection positive for every reflection of the family, and block 19's G2 argument gives Gaussian domination and `⟨|Ŝ^e_±(k)|²⟩ ≤ 1/(βλ_±(k))`, `λ_+ = E`, `λ_− = E + 2`. (b) With the two levels of `Γ_L` as halves every edge crosses the swap, the crossing matrix is `M = I + A_nn`, and `⟨d, Md⟩ = −64` for the staggered `d` on the open `2×2×2` cube (`−20N` on the torus of side 4): the `2×2` minor of the kernel `e^{β s·Ms'}` at the two staggered configurations is negative for every `β > 0`.

*Proof.* (a) The crossing factor `Π e^{β s_u·s_{θu}}` expands with nonnegative coefficients in products `g(s_u) ḡ(s_{θu})`, which gives `E[F θF] ≥ 0`; the rest is block 19 G1–G2 with this family. The structure is checked on all 13 reflections of `4³` (family D). (b) The minor is `e^{β(σMσ + τMτ)} − e^{2βσMτ}`, negative iff `(σ − τ)·M(σ − τ) < 0`; with `σ − τ = d` this is `32 − 96` on the cube and `−20N` on the torus (family D). ∎

## Theorem T4 — memory

*Statement.* `⟨|m₀|²⟩_π ≥ 1 − (3/(2β))(G_L + H_L)` for every even `L` and `β > 0`. Exactly, `β_4 = 18239/35840` and `β_6 = 27735979/51891840`. As `L → ∞`, `G_L → I₀` and `H_L → I₂`: the stationary law has long-range order for `β > (3/2)(I₀ + I₂)`.

*Proof.* The sum rule over both branches and three components gives `⟨|M|²⟩/(2N) ≥ 2N − (3N/β)(G_L + H_L)`, `M` the sum over both levels. The swap of the levels is an automorphism of `Γ_L` because `N7 = −N7`, so `⟨|m₀|²⟩ = ⟨|m₁|²⟩`, and `|(m₀ + m₁)/2|² ≤ (|m₀|² + |m₁|²)/2`. On the `4³` bilayer the sum of `1/λ` over the 127 nonzero eigenvalues checked in T2 is exactly `N(G_4 + H_4)`. The finite sums are exact rationals on the tori of side 4 and 6, where the cosines are rational. Family E. ∎

*Executed.* `I₀ = 0.2527310099 = W/6` (closed form, twelve digits), `I₂ = 0.1409314881` (quadrature): `β₀ = 0.5904937`. `β_L` rises through `0.5089, 0.5345, 0.5483, 0.5623, 0.5693, 0.5764, 0.5799, 0.5834, 0.5852` for `L = 4, 6, 8, 12, 16, 24, 32, 48, 64`.

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block90_light_cone_memory.py`, output in `.out.txt`; disjoint machinery: quadrature, lattice sums, and an independent simulator that samples the rule on the sphere exactly by inverting the cosine's distribution).

*W1–W2.* The constants and the finite thresholds above.

*W3 — the onset, independently.* Aligned start, plateau `|m|` over the second half of `1600` levels:

| `β` | `0.55` | `0.58` | `0.60` | `0.62` | `0.65` |
|---|---|---|---|---|---|
| plane `24³` | `0.126` | `0.351` | `0.415` | `0.472` | `0.529` |
| plane `32³` | `0.088` | `0.339` | `0.416` | `0.468` | `0.523` |

The probes' scans (`X:lightcone-threshold-fine`, `X:lightcone-finite-size`; `formation_levelplane.py`, planes 16–96, three seeds): `0.060 → 0.030` at `β = 0.55` (32 → 48), `0.418 → 0.411` at `0.60`; plateaus `0.645 … 0.635` (`β = 0.75`), `0.767 … 0.760` (`1.0`), `0.857 … 0.854` (`1.5`) from 16 to 96, fitted by `m∞ + b/L` with `m∞ ≈ 0.633, 0.759, 0.853`. The level-ordered clause (`X:formation-3plus1-*`): onset in `(1.1, 1.3)`; `0.742 … 0.734` at `β = 2` from 16 to 96, `m∞ ≈ 0.732`.

## No-Go Discipline Gate

The note's negative sentences: the level-ordered chain is not reversible; the layer halves are not reflection positive.

### N1 — Routes by which the sentences could fail or mislead
1. *The clause.* Which records are the conditions of a forming record is supplied; the light-cone past is one choice, the level-ordered past another. Only the first is proved.
2. *The constant.* `β₀` uses `I₂`, executed by quadrature; `I₀` has a closed form. The finite-size thresholds are exact.
3. *Gaussian domination.* Taken from block 19's G2 argument with the reflection family checked here. The argument is independent of the graph once the family has the checked structure; it is not re-run symbolically for the bilayer.
4. *Provenance.* The route is the probes' (one model family, unrefereed by another), and this block is by the same family. The exact checks here are independent code.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The sphere menu for T3–T4; even tori; the aligned start in the simulators.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | "Records form"; one covariant nearest-neighbour rule | yes (premise) |
| block 19 (open PR #8153) | the sphere rule; reflection positivity through bond planes; Gaussian domination; the sum rule | yes (the machinery) |
| blocks 26, 28 (open PRs #8170, #8172) | two-dimensional formation forgets; the map of memory | yes (placed) |
| probes issues #8463, #8631 and the attempt of w-macbookpro90c72-j451b | the route | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "light-cone formation is reversible; its stationary law is one layer of a reflection-positive bilayer; memory for beta > 0.5905" | executed: detailed balance for every pair on two rings; the level-ordered cycle; the relabelling edge by edge on two tori | executed: the 13 reflections vertex by vertex; the cube's and the torus's form | executed: the bilayer's eigenvectors at every vertex; finite sums exactly; control quadrature and simulator | executed: the sum rule's threshold; the finite thresholds | T1–T4 for every even L; the constant executed

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "This is Gaussian domination on a bilayer; nothing about formation." Reply: the content is that the formation chain's own long-time law is a layer of that bilayer (T1, exact), which is what makes the equilibrium method apply to records that form; the level-ordered clause, not reversible, shows that this is not automatic. Second objection: "The constant is not sharp." Reply: agreed; it lies between 2 and 8 per cent above the executed onset.

### N8 — Cross-cycle echo
Block 19: the static sphere law orders on the cubic lattice above `3√3π/8`. Blocks 26–28: formation in level time forgets on planes. Here: formation with a light-cone past remembers on three-dimensional planes above `0.5905`.

## Falsifiers

- A pair of configurations on a ring for which the symmetric-stencil chain violates detailed balance.
- An edge of `Γ_L` whose image under the relabelling is not a bilayer edge, or a bilayer edge not hit.
- A reflection of the family with a fixed vertex or a crossing edge that is not a mirror pair.
- A finite torus whose sum-rule threshold differs from `(3/2)(G_L + H_L)`.
- For the level-ordered past, a torus of side at least 3 on which the cycle `a → b → −a → a` of T1 has equal forward and backward products.

## Boundaries and non-claims

The light-cone clause, the sphere menu and block 19's rule are supplied; the level-ordered clause is not proved; the constant `β₀` is executed; Gaussian domination is block 19's argument applied with the checked family. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Record, Admissibility and Lattice axioms. Blocks 19, 26, 28 (open PRs); the probes' derivations (issues #8463, #8631): restated or re-derived.
- Named standard imports at definition level: detailed balance for a reversible chain and the cycle criterion (Kolmogorov's) for its failure; reflection positivity and Gaussian domination (block 19's G1–G3); lattice sums; the closed form of `W` with Gamma functions; quadrature of the Bessel integral for `I₂`; an exact sampler of the rule on the sphere for the control.

## Review record
Corrigendum (2026-09-23, supervisor): block 36 (#8507) is prior art and its excluded clause governs this note's status; missed in the lens pass, found when the owner asked to probe the readings against known physics. Text-only; no theorem, check or number changed.

Supervisor-run block, the thirty-eighth of the source-link and records campaign; the second run on Claude Opus 5.5; built from the 2026-09-23 harvest of the probes, whose derivation units proposed this route (all by one model family, unrefereed by another; this block is by the same family). Lens pass, in writing, by the supervisor: a foundations lens — the clause is supplied and named; the level-ordered clause is kept apart and shown not reversible; a rigour lens — every finite step (detailed balance for two menus, the relabelling on two tori, the reflection structure, the layer-halves minor, the finite thresholds) is checked exactly by independent code, the no-go minor was first computed on the side-2 torus (doubled edges, `−160`) and then on the open cube to match the attempt's statement (`−64`; both negative), and the onset is re-measured with an independent simulator. Rigour lens, second pass: the first draft showed only that the light-cone law fails detailed balance for the level-ordered past, which does not exclude another law; the check was replaced by the cycle criterion, and the bilayer's spectrum, first asserted, is now checked eigenvector by eigenvector. Mutation census: nine mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_stationary_law_one_layer_of_a_reflection_positive_bilayer_2026_09_23.py
```

Expected: `TOTAL: PASS=15 FAIL=0`.
