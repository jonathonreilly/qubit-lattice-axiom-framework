---
claim_id: admissibility_rule_the_record_gas_never_makes_the_chessboard_a_rest_mass_needs_binding_grows_only_around_loops_content_order_gives_the_walk_no_gap_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN the moving-records reading of blocks 39–42 (open PRs #8530, #8546, #8547, #8548; not adopted) and the supplied clauses of blocks 54, 77 and 79 (open PRs #8570, #8612, #8614; not adopted): the static law with vacancies at the scale c = g·c₀ on finite windows and tori, exact rationals; block 54's walk with a record background entering as a coin-scalar potential (block 79's clause) or read by the coin, exact symbolic algebra; the three-dimensional gas on periodic lattices of side 6 and 8 executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_record_gas_never_makes_the_chessboard_a_rest_mass_needs_loops_bind_content_order_no_gap_2026_09_22.py
---

# The record gas never makes the chessboard that a rest mass needs: binding grows only around loops, and content order gives the walk no gap

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (one general identity by proof; exact enumerations on finite windows and tori; symbolic spectra for every wave vector; executed three-dimensional sampling labelled; nothing adopted or registered; unaudited)

This note works within the moving-records reading of blocks 39-42 and the supplied clauses of blocks 54, 77 and 79; it reports which arrangements of records the static law with vacancies favours and what each kind of record order does to the walk's spectrum; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 79 (PR #8614) found that a chessboard of records — records on one sublattice and none on the other — is felt by block 54's walk as a rest mass, and after its corrigendum presents that chessboard as a supplied configuration, naming blocks 39–42 as the place where it would have to arise. This note asks the lane's own record gas whether it arises. It does not, at any scale the reflection-positivity bound of block 39 allows.

1. **Binding grows only around loops (T1).** In the static law with vacancies at the neutral scale, adding a recorded bond between two records multiplies the weight of the arrangement by exactly `1 + 3t₁λ₁ + 2t₂λ₂`, where `(t₁, t₂)` are the correlation eigenvalues of the two contents in the arrangement without that bond and `(λ₁, λ₂)` are the rule's. Between records not yet connected the factor is exactly `1`; along a path of `n` bonds `t = λⁿ`; at the scale `g·c₀` the factor carries an extra `g`. Block 40's cycle factor and block 41's "no action across empty sites" are the two ends of one identity.
2. **The chessboard is the least likely arrangement (T2).** Both chessboards weigh exactly what the same records weigh placed apart, `zⁿ6ⁿ`, at every scale. On every window enumerated (`2×2×2` at seven triples, `2×3` and `3×3` at three, `2×2×3` at one; every arrangement of every record number) no arrangement weighs less than that, the arrangements that weigh exactly that are precisely those without a cycle, and the heaviest is the full window. At `g ≥ 1` the chessboard is therefore a least-weighted arrangement of its record number: on the cube it weighs `1/(g⁴(1 + 3λ₁⁴ + 2λ₂⁴))` of four records on one face.
3. **The equilibrium's staggered occupancy (T3).** On any torus the mean staggered occupancy is exactly zero at every scale, density and triple. At half filling on the `4×4` torus (all `12870` arrangements, by their `153` orbits) the staggered susceptibility is at most random's `4/15` at `g = 1` and `g = 4` (`0.266, 0.095` at `(3,1,2)`; `0.238, 0.064` at `(12,1,2)`) and the most likely arrangement is a band of twelve bonds with zero staggered count; at the excluded `g = 1/4` the susceptibility is `2.43` and the most likely arrangement is the chessboard. The three-dimensional cube says the same (`0.286, 0.111` against `2/7`; `1.094` at `g = 1/4`). The walk's mean background in equilibrium is therefore uniform, `ρc`: an offset, not a mass.
4. **What gaps the walk (T4).** Three backgrounds on a full or half-full record layer: records of one content read by the coin (`cσ_z`) move the walk's two zeros to `sin k_z = −c` and leave the spectrum touching zero; a chessboard of contents read by the coin (`cεσ_z`, the static law's ordered state when `q > p`) has `det(H − E) = (E² − |s|² − c²)² − 4c²(s_x² + s_y²)`, `s = sin k`, so `E = 0` on the whole ring `s_z = 0`, `s_x² + s_y² = c²`; only the chessboard of occupancy with block 79's content-blind coupling obeys `(H − c/2)² = |s|² + c²/4` and opens the gap `c`. Content order of either kind gives no rest mass.
5. **Executed (control; floating point).** Block 39's gas sampled at half filling on periodic lattices of side `6` and `8` (transit with the ratio acceptance and content re-draws): at `g = 1` the staggered structure factor equals random placement's (`0.250` against `0.251` on `6³`; `0.284` against `0.250` on `8³`), at `g = 2, 4` it falls below it while the recorded neighbours per record rise (`4.5` against `3.0` at `g = 4`), and at `(12,1,2)` it is below random's already at `g = 1` (`0.085`; neighbours `4.05`). At the excluded `g = 1/2` it is seven times random's and at `g = 1/4` a near-perfect chessboard (`50` of the maximum `54` on `6³`; `117` of `128` on `8³`). The walk on the `6³` torus with block 79's clause at `c = 3/5`: the chessboard leaves the interval `(0, c)` empty; a sampled equilibrium arrangement at `g = 1` puts `16` of `432` eigenvalues inside it, the nearest `0.008` from its middle — the equilibrium background has no gap.

So the rest mass of block 79 has no source in the record layer's equilibria: a chessboard of occupancy needs neighbouring records to repel, which the rule at `c ≥ c₀` never supplies (it binds, and only around loops), and the content order the static law does produce leaves the walk gapless. Fork 5 of the decision record (rest energy) remains without an in-framework source; where one could still come from is named under Boundaries.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 79 (PR #8614, corrigendum): 'a density pattern of the record layer; whether the lattice gas of records with exclusion, blocks 39–42, orders this way is not established'"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the gas at every allowed scale disfavours the chessboard (least-weighted arrangement; susceptibility at most random's; mode a clump); binding is a loop identity; content order gives no gap: block 79's background is not supplied by the lane's equilibria; next: formation out of equilibrium (block 39's formation rate at a steady excess) as a source of staggered occupancy; the matched pulls under exclusion; the owner's fork on rest energy"
conditional_surface_status: "T1 by proof on every finite graph; T2 exact on the windows enumerated (not proved for every window: reduces by T1 to 3t₁λ₁ + 2t₂λ₂ ≥ 0 for every pair of lattice-adjacent records); T3 exact on the 4×4 torus and the cube; T4 symbolic for every wave vector; the executed three-dimensional numbers are the control's"
hypothetical_axiom_status: "the moving-records reading with the static law with vacancies; the scale g; the record backgrounds and the coupling clauses; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (the proper cubic rotations act on the six-axis contents transitively and preserve the pair weights; `ε` is invariant about any site), the Record axiom (one record per site at a time, in the owner's reading), the Qubit axiom, and the memo's silence on record motion and on how records act on amplitudes. Blocks 39, 40, 41, 42 (open PRs #8530, #8546, #8547, #8548) supply the moving-records reading and its static law; blocks 54, 77, 79 (open PRs #8570, #8612, #8614) the walk, the staggered term and the coin-scalar clause. Nothing is adopted here.

- **Arrangements.** A finite graph of sites (a window of `Z³`, or a torus); an arrangement `η` is a set of recorded sites, each with a content in the six-axis menu `±e₁, ±e₂, ±e₃`; its recorded bonds are the lattice bonds with both ends in `η`.
- **The static law with vacancies (block 39).** `μ(η, s) ∝ z^{|η|} Π_{recorded bonds} c·ω(s_x, s_y)`, `ω = p, q, r` for equal, opposite, orthogonal contents; a bond with an empty end weighs `1`. `c = g·c₀`, `c₀ = 6/(p + q + 4r)` (block 40), and `g ≥ 1` are the scales at which the law is reflection positive (block 39 T5); `g < 1` is called excluded below.
- **The rule's eigenvalues.** `K₁ = c₀ω/6` is doubly stochastic with eigenvalues `1, λ₁ = (p − q)/(p + q + 4r)` (three times), `λ₂ = (p + q − 2r)/(p + q + 4r)` (twice): `M = c₀ω = J + 6λ₁P₁ + 6λ₂P₂` with `J` the all-ones matrix, `P₁` the projector with entries `1/2, −1/2, 0` and `P₂` the projector with entries `1/3, 1/3, −1/6` on equal, opposite, orthogonal pairs.
- **Weight over free.** `Z₀(η) = Σ_{contents} Π_{recorded bonds} M(s_x, s_y)`; the weight of `η` at scale `g` is `z^{|η|} g^{|bonds|} Z₀(η)`; "free" is `6^{|η|}`, the content sum of the same records placed so that none touch. Weight over free is `g^{|bonds|} Z₀(η)/6^{|η|}`.
- **Correlation eigenvalues.** For two recorded sites `x, y`, the joint law `μ(a, b)` of their contents under the contents' law on `η`; when `μ = (1/6)[J/6 + t₁P₁ + t₂P₂]`, `(t₁, t₂)` are its correlation eigenvalues.
- **Chessboard.** The records on one sublattice of the window and none on the other (`n(x) = (1 + ε(x))/2` or its translate, block 79); a staggered count `Σ_x ε(x) n(x)`; the staggered susceptibility `⟨(Σ ε n)²⟩/N` at fixed record number.
- **The walk and the backgrounds (block 54, 79).** `H = Σ_a σ_a S_a`, `S_a` the symmetric one-step difference with symbol `sin k_a`; a background of records enters as `c Σ_x n(x) P_x` (block 79's clause, content-blind) or as `c Σ_x n(x) (s_x·σ) P_x` (read by the coin; named here for comparison, supplied, not adopted). `ε` sends the plane wave `k` to `k + (π, π, π)`, where `h(k) = σ·sin k` becomes `−h(k)`.
- **Control.** Block 39's transit with the ratio acceptance and a content re-draw by the local law, both in detailed balance with the static law with vacancies; the walk's dense spectrum on a `6³` torus.

Exchange dynamics with a conserved particle number is due to Kawasaki and the ratio acceptance to Metropolis and co-authors; the joint law's spectral form is Schur's lemma for the permutation representation; the content-less repulsive lattice gas at half filling is the model of Ising in the antiferromagnetic case and its chessboard ground states are those of the hard-core gas studied by Dobrushin; a ring of zeros in the spectrum compares with the nodal lines of band theory. None is used as authority.

## Prior art and what is new

Block 40 T2–T3 (open PR #8546) proved that at `c₀` records do not bind on a window without a cycle and that a fully recorded cycle carries the factor `1 + 3λ₁ⁿ + 2λ₂ⁿ`; block 41 (open PR #8547) that records separated by empty sites do not interact; block 17's ordered states of the static law are records of one content, and Gibbs measures with vacancies of this kind are the dilute models of Potts and of Blume, Emery and Griffiths. New, inside the framework's vocabulary: the general bond identity (T1) that contains both of block 40's statements; the exact enumeration showing the chessboard to be a least-weighted arrangement at every allowed scale and the staggered susceptibility to be at most random's (T2, T3); and the symbolic spectra showing that content order, uniform or alternating, leaves the walk gapless, so that only the chessboard of occupancy — the one arrangement the gas disfavours — supplies block 79's rest mass (T4). Whether a Griffiths-type inequality gives T2 for every window is left open. No gravitational claim is made.

## Exact target and obligation graph

Target: whether the record gas supplies block 79's background. Obligations: (O1) how binding grows bond by bond; (O2) the weight of the chessboard against every other arrangement; (O3) the equilibrium's staggered occupancy; (O4) which backgrounds gap the walk. T1 discharges O1; T2, T3 discharge O2, O3 on the windows and tori enumerated; T4 discharges O4.

## Theorem T1 — binding grows only around loops

*Statement.* Let `η` be an arrangement and `x, y ∈ η` lattice-adjacent recorded sites not joined by a recorded bond of `η` (that is, the bond was not counted; adding it gives `η⁺`). At the neutral scale `Z₀(η⁺) = Z₀(η)·(1 + 3t₁λ₁ + 2t₂λ₂)`, with `(t₁, t₂)` the correlation eigenvalues of `(s_x, s_y)` under the contents' law on `η`; at the scale `g·c₀` the factor is `g(1 + 3t₁λ₁ + 2t₂λ₂)`. If `x` and `y` lie in different components of `η`, `t₁ = t₂ = 0` and the factor is exactly `1` (or `g`); if `η` joins them by a path of `n` bonds and nothing else, `t_i = λ_iⁿ`.

*Proof.* `Z₀(η⁺) = Σ_{contents} Π_{η} M · M(s_x, s_y) = Z₀(η)·Σ_{a,b} μ(a, b) M(a, b)`. The proper cubic rotations act on the six contents transitively, on ordered pairs of contents with the three orbits equal, opposite, orthogonal (`6 + 6 + 24` pairs; the group of order `24` acts simply transitively on the ordered orthogonal pairs), and preserve every pair weight; so `μ` is invariant under the simultaneous action and lies in the commutant of the permutation representation, which the three orbits span: `μ = αJ + βI + γA` with `A` the antipode, that is `μ = (1/6)[J/6 + t₁P₁ + t₂P₂]`, the coefficient of `J` fixed at `1/36` by the uniform marginals (transitivity). With `M = J + 6λ₁P₁ + 6λ₂P₂`, `tr P₁ = 3`, `tr P₂ = 2`, `P₁P₂ = 0`, `P_iJ = 0`: `Σ μM = 1 + 3t₁λ₁ + 2t₂λ₂`. Different components: the two contents are independent with uniform marginals, `μ = J/36`. A path: `μ = (1/6)K₁ⁿ`. At the scale `g·c₀` every recorded bond carries the extra `g`. ∎

*Executed exactly (family B).* On the `2×3` ladder without its middle rung the joint law of the two middle contents is constant on the three orbits with uniform marginals, and closing the rung multiplies `Z₀` by `1 + 3t₁λ₁ + 2t₂λ₂` at five triples (`15625/15553` at `(3,1,2)`, `t = (144/15553, 1/15553)`; `179161922/107500967` at `(12,1,2)`); along a path of five bonds `t = λ⁵` and closing the six-cycle gives `1 + 3λ₁⁶ + 2λ₂⁶`; joining two paths gives exactly `1`, and `g` at scale `g`.

Remark. On the bipartite lattice two lattice-adjacent records in one component are at odd graph distance, so along a single path `t_iλ_i = λ_i^{n+1} ≥ 0`: a loop that closes through a path never lightens the arrangement. For arrangements with several paths between `x` and `y` the sign of `3t₁λ₁ + 2t₂λ₂` is not proved in general; T2 finds it non-negative on every window enumerated.

## Theorem T2 — the chessboard is the least likely arrangement on every window enumerated

*Statement.* (a) Both chessboards of any window have no recorded bond and weigh exactly `z^{|η|}6^{|η|}` at every scale. (b) On the windows `2×2×2` (triples `(3,1,2), (5,2,4), (12,1,2), (2,2,5), (1,3,2), (1,1,100), (100,1,1)`), `2×3` and `3×3` (`(3,1,2), (5,2,4), (12,1,2)`) and `2×2×3` (`(3,1,2)`), over every arrangement of every record number: `Z₀(η)/6^{|η|} ≥ 1`, with equality exactly for the arrangements without a cycle (`188` of `255` on the cube, `56` of `63`, `415` of `511`, `2466` of `4095`), and the maximum is the full window (`1.015, 1.005, 12.06` on the cube at the first three triples; `1.028` on `2×2×3` at `(3,1,2)`; `4330` at `(100,1,1)`). (c) Hence at every `g ≥ 1`, on these windows, the chessboard is a least-weighted arrangement of its record number; on the cube it weighs `1/(g⁴(1 + 3λ₁⁴ + 2λ₂⁴))` of the four records on one face — `1/(256·433/432)` at `g = 4`, `(3,1,2)`.

*Proof.* (a) No two sites of one sublattice are adjacent; with no recorded bond the content sum is `6^{|η|}`. (b) Exact enumeration by frontier contraction of the content sum (integers), the acyclicity of each arrangement by union–find. (c) The weight over free at scale `g` is `g^{|bonds|}Z₀/6^{|η|} ≥ 1` for `g ≥ 1` by (b); the face carries four bonds and block 40's cycle factor. ∎

## Theorem T3 — the equilibrium's staggered occupancy

*Statement.* (a) On any torus with even sides, at every scale, density and triple, `⟨Σ_x ε(x) n(x)⟩ = 0`. (b) On the `4×4` torus at half filling: the staggered susceptibility `⟨(Σ ε n)²⟩/16` is `481075812/1805289719 ≈ 0.266` at `g = 1` and `≈ 0.095` at `g = 4` for `(3,1,2)` (`0.238`, `0.064` for `(12,1,2)`), at most random's `4/15`; at `g = 1/4` it is `≈ 2.43` (`2.40`), above four times random's; at `g = 1` and `4` the most likely arrangement is a band of twelve bonds with zero staggered count, at `g = 1/4` it is the chessboard (no bonds, staggered count `8`). (c) On the `2×2×2` cube with four records at `(3,1,2)`: mean staggered count exactly zero; susceptibility `≈ 0.286` and `0.111` at `g = 1, 4` (random's `2/7`), the mode a face; `1.094` at `g = 1/4`, the mode the chessboard.

*Proof.* (a) Translation by one lattice step preserves the law (the weights depend only on the graph) and reverses `ε`; the mean equals its own negative. On the cube the reflection `x → 1 − x` does the same. (b), (c) Exact enumeration: on the torus by the `153` orbits of the `12870` half-filled arrangements under its `128` symmetries (the staggered count sums to zero over every orbit, which is (a) again); on the cube all `70` arrangements. ∎

*Consequence for block 79.* The background the walk feels in equilibrium is, on average, `ρc` at every site: block 79 T1's offset with `m = 0`. Configuration by configuration the chessboard component is disfavoured at every allowed scale; a rest mass of block 79's kind would need a staggered mean, which the gas supplies only below the neutral scale, where block 39's bound excludes it.

## Theorem T4 — which record backgrounds gap the walk

*Statement.* With `s = sin k`, `h(k) = σ·s`: (a) records of one content on every site, read by the coin, `H = h + cσ_z`: `det(H − E) = E² − s_x² − s_y² − (s_z + c)²`; the spectrum touches zero at `s = (0, 0, −c)`. (b) A chessboard of contents read by the coin, `H = h + cεσ_z`: in the doubled basis `(k, k + π)`, `det(H − E) = (E² − |s|² − c²)² − 4c²(s_x² + s_y²)`; `E = 0` on the ring `s_z = 0`, `s_x² + s_y² = c²`. (c) The chessboard of occupancy with the content-blind coupling, `H = h + (c/2)(1 + ε)`: `(H − c/2)² = |s|² + c²/4`; the bands are `c/2 ± √(|s|² + c²/4)`, the gap is `c`, and at the species points the energies are exactly `0` and `c` (block 79 T1).

*Proof.* `ε` maps `k` to `k + π` and `h(k + π) = −h(k)`, so on the pair `(k, k + π)` the operators are the block matrices `[[h, cσ_z], [cσ_z, −h]]` and `[[h + c/2, c/2], [c/2, −h + c/2]]`; (a) needs no doubling. The determinants and the square are exact symbolic identities in `s_x, s_y, s_z, c, E` (family E), checked at rational points: `det = 0` at `s = (3/5, 0, 0)`, `c = 3/5` and `49/625` at `s = (4/5, 0, 0)` for (b); `det = 0` at `s = (0, 0, −3/5)` for (a); energies `{0, 3/5}` at the species point for (c). ∎

Remark. (b) is the static law's own ordered state when `q > p`: on the bipartite lattice the map `s → −s` on one sublattice exchanges `p` and `q` and carries the aligned states to alternating ones. Neither content order opens a gap; the content-reading coupling turns the eight zeros into a ring.

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block81_record_gas_chessboard.py`, output in `.out.txt`; disjoint machinery: sampling and dense diagonalisation, floating point).

*W1 — the three-dimensional gas at half filling.* Block 39's transit with the ratio acceptance and a content re-draw by the local law, `600` (`400`) sweeps to settle and `2400` (`1600`) to measure on `6³` (`8³`), one seed each. Entries: staggered structure factor `⟨(Σ ε n)²⟩/N` / recorded neighbours per record; random placement in brackets (`0.251` / `2.99` on `6³`; `0.250` / `2.99` on `8³`); the maximum of the structure factor is `54` on `6³` and `128` on `8³`.

| scale `g` | `6³`, `(3,1,2)` | `6³`, `(12,1,2)` | `8³`, `(3,1,2)` |
|---|---|---|---|
| `4` | `0.052 / 4.50` | `0.021 / 4.82` | `0.047 / 4.61` |
| `2` | `0.112 / 3.55` | `0.033 / 4.86` | — |
| `1` (neutral) | `0.250 / 2.99` | `0.085 / 4.05` | `0.284 / 3.00` |
| `1/2` (excluded) | `1.79 / 2.38` | `0.40 / 3.11` | — |
| `1/4` (excluded) | `50.0 / 0.21` | `49.4 / 0.24` | `117.1 / 0.24` |
| `1/8` (excluded) | `49.7 / 0.25` | `53.0 / 0.06` | — |

At every allowed scale the structure factor is at or below random placement's and the records clump (more neighbours than random); the chessboard appears only below the neutral scale, and is near perfect from `g = 1/4` down. This agrees with T2–T3's exact windows.

*W2 — the walk in three backgrounds (`6³` torus, block 79's clause, `c = 3/5`, dense spectrum of `432` states).* Chessboard: no eigenvalue strictly inside `(0, c)`, the nearest `0.300` from `c/2` (the band edges `0` and `c` themselves): the gap `c` of T4(c). The sampled equilibrium arrangement at `g = 1` from W1: `16` eigenvalues inside `(0, c)`, the nearest `0.008` from `c/2`: no gap. Records on every site: the spectrum is the free one shifted by `c` (`[−0.90, 2.10]`); on this torus `sin k ∈ {0, ±√3/2}` only, so the count inside `(0, c)` is `0` by coarseness, while the bands `c ± |s|` cover `(0, c)` for `|s| < c` on any finer torus — an offset, not a gap.


## No-Go Discipline Gate

The note's negative sentences: the record gas at any allowed scale does not supply the chessboard; content order gives the walk no gap.

### N1 — Routes by which the sentences could fail or mislead
1. *Every window.* T2 is exact on four windows and not proved in general; T1 reduces the general case to a sign, which the bipartite lattice gives for single paths only. The three-dimensional sampling (control) says the same on periodic lattices of side 6 and 8.
2. *The reading.* The static law with vacancies is block 39's; the odds reading of block 42 makes every arrangement of `k` records weigh the same once contents are summed (its item 1), which supplies no chessboard either, and its seven-outcome density channel at the neutral scale is exactly zero (its item 5). Neither reading is adopted.
3. *Out of equilibrium.* Records form (the axioms); a steady excess of formation next to agreeing records (block 41 item 5) is a source, and a staggered pattern could in principle be laid down by formation and frozen by permanence before transit erases it. Not examined; named as the next probe.
4. *Other couplings.* A record could act on the walk through the rates (block 79 T1(c): invisible for a chessboard) or through a bond term; only the site terms are examined.
5. *The excluded scales.* `g < 1` gives the chessboard (T3, control); block 39 T5 excludes it only if reflection positivity is required of the law. That condition is block 39's, restated, not proved here.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Finite windows and tori; half filling for the susceptibility statements; site couplings only; `c = 3/5` at the rational points (the identities are symbolic).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice axiom's rotations (transitivity on contents); the Record axiom | yes (premise) |
| blocks 39, 40, 41, 42 (open PRs #8530, #8546, #8547, #8548) | the static law with vacancies; the neutral scale; the two ends of T1 | yes (restated) |
| blocks 54, 77, 79 (open PRs #8570, #8612, #8614) | the walk; the staggered term; the coin-scalar clause and the background | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "binding grows only around loops; the chessboard is the least likely arrangement; staggered mean zero and susceptibility at most random's at allowed scales; content order gives no gap" | executed: the joint law entry by entry; the loop factor bond by bond | executed: every arrangement on four windows weighed exactly | executed: symbolic spectra at every wave vector; control on `6³`, `8³` | executed: susceptibility, mode and staggered count over all half-filled arrangements of the torus and the cube | T1 by proof; T2 on the windows enumerated; T4 by identity

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Small windows cannot decide order in three dimensions." Reply: the exact statements are about weights of arrangements, which are local (T1 is a bond identity), and the sampling on `6³` and `8³` agrees; nothing about infinite volume is claimed, and the general inequality is flagged open. Second objection: "A chessboard of contents is order too." Reply: it is, and T4(b) is the reason it does not help — the coin-reading coupling makes a ring of zeros, not a gap.

### N8 — Cross-cycle echo
Block 39: records that move clump. Block 40: no binding without a cycle. Block 41: no action across empty sites. Block 79: a chessboard of records is a rest mass. Here: the gas never makes that chessboard, and the order it does make is not a mass.

## Falsifiers

- An arrangement of records on a window of `Z³` with `Z₀(η) < 6^{|η|}` at the neutral scale (a loop that lightens).
- A pair of lattice-adjacent recorded sites in some arrangement whose joint content law is not constant on the three orbits.
- A torus, scale `g ≥ 1` and triple with a staggered susceptibility above random's at half filling, or with the chessboard as the most likely arrangement.
- A wave vector at which the content chessboard's determinant differs from `(E² − |s|² − c²)² − 4c²(s_x² + s_y²)`, or a gap in its spectrum.

## Boundaries and non-claims

T2 is not proved for every window; T3's numbers are for one torus and one cube; the control is sampling. Formation out of equilibrium, bond couplings and the rates' channel are not examined; the excluded scales are excluded by block 39's bound, restated. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom (proper rotations), the Record axiom, the Qubit axiom. Blocks 39–42, 54, 77, 79 (open PRs): restated or placed.
- Named standard imports at definition level: Schur's lemma for the commutant of a permutation representation; union–find for acyclicity; determinants and block matrices in exact symbolic algebra; Kawasaki-type exchange and the ratio acceptance for the control's sampling; dense Hermitian diagonalisation for the control's spectra.

## Review record
Supervisor-run block, the twenty-ninth of the source-link direction; the sixth after the fork probe. Lens pass, in writing, by the supervisor: a foundations lens — the chessboard was first attributed (block 79) to block 17's ordered states, which are records of one content; the corrigendum made it a supplied object and this block asks the gas for it; a rigour lens — the first orbit-reduced torus computation reported a nonzero mean staggered count because it used the representative's count for the whole orbit; the count is reversed by translation, the mean is exactly zero (T3(a)), and the runner now sums the count over every orbit's elements; the first test of the occupancy chessboard looked for a nonzero determinant at the species point and found zero, which is right — the lower band's top sits at `E = 0` and the gap is the interval `(0, c)`, so the check became the exact square identity; the control's first neighbour indexing produced a non-Hermitian walk, caught by its own assertion and fixed. Refuting pass: the general inequality `Z₀ ≥ 6^{|η|}` was attacked at seven triples including `(1,1,100)`, `(100,1,1)`, `(2,2,5)` (negative `λ₂`) and `(1,3,2)` (negative `λ₁`) without a counterexample; it stays open beyond the windows. Mutation census: ten mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_record_gas_never_makes_the_chessboard_a_rest_mass_needs_loops_bind_content_order_no_gap_2026_09_22.py
```

Expected: `TOTAL: PASS=20 FAIL=0`.
