---
claim_id: admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on a supplied motion clause that is not in the axioms memo (the memo lists update laws and persistence dynamics among its open gates): a site is empty or carries one record; a record carries its content; two neighbouring records weigh W(a, b) = c omega(a, b) (omega the rule's pair weights, c > 0 a scale) and a bond with an empty end weighs 1. On finite windows: (T1) a record choosing between its position and an empty neighbouring position in proportion to the pair weights it would have there (or with any acceptance whose ratio is w_y/w_x) is in detailed balance with the static law on the occupied set with the contents fixed; motion conserves the number of records and their contents; on the 2x3 window with two vacancies the moves connect all 180 arrangements of four six-axis records. (T2) The scale c cancels from the axioms' normalized distribution K and enters the motion exactly through the change in the number of record-record bonds: P(x -> y) = 1/(1 + c^(k_x - k_y) Omega_x/Omega_y); a record with k agreeing neighbours moves to an isolated position with probability 1/(1 + (c p)^k). (T3) If a move is instead accepted with the rule's normalized probability of the content at the destination, the chain is blind to c and is reversible for no law (a cycle of four moves with products of rates 1/2592 and 1/2376). (T4) Formation at an empty site x at rate z Z_x with content drawn from K is the creation half of a reversible birth-death pair for the static law with fugacity z, and z Z_x is the only rate law with that property; at the neutral scale c_0 = 6/(p + q + 4r) the mean pair weight is 1, and at (3,1,2) the formation rate next to two agreeing, orthogonal, opposite records is multiplied by 13/12, 1, 11/12. (T5) With the empty state included, the bond kernel (1 if an end is empty, c omega between records) is positive semidefinite, hence the static law with vacancies is reflection positive through bond planes for every fugacity, exactly when p >= q, p + q >= 2r and c >= c_0; for c < c_0 reflection positivity fails on the four-site ring: the neutral scale is the least binding scale compatible with reflection positivity. EXECUTED, not claimed (cubic lattice, density 3/10, line (p,1,2)): records stay uniformly spread below an onset and clump into aligned clusters above it: between p = 8 and 12 at the neutral scale (near 10 on a 24^3 lattice), between 5 and 6 at scale 1, between 8 and 12 at scale 1/2; the fraction of accepted moves falls from 0.48 to 0.18 (neutral) and to 0.03 (scale 1) with seven tenths of the sites empty; for content-less records the onset lies between c = 2.43 and 2.7. Neither the motion clause nor any value of the scale is adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_records_that_move_pair_weight_transit_static_equilibrium_binding_scale_2026_09_20.py
---

# Records that move: pair-weight transit has the static law as its equilibrium, the binding scale is a constant the rule cannot see, and where records clump and jam

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact on finite windows under a supplied motion clause; the clumping and jamming map executed, not claimed; nothing adopted; unaudited)

## Result up front

The owner's reading of the Record axiom (2026-09-20): records move. A site holds at most one record at a time; an empty site can form a record according to the rule; a record can transit to a neighbouring empty site when the neighbourhood allows; a site may therefore generate more than one record over time. The memo's sentence "A site never carries more than one record; records are permanent." forbids two records on a site at once and the destruction of a record; it does not forbid a record leaving. Motion itself is not in the memo, which lists update laws and persistence dynamics among its open gates. This note works out what that reading gives.

This note is conditional on a supplied motion clause (records move, carrying their content, by pair-weight transit) and on a supplied binding scale, neither of which is in the axioms memo; the memo lists update laws and persistence dynamics among its open gates, and nothing here is adopted.

1. **The comparator is the equilibrium of moving records (T1).** If a record chooses between where it is and an empty neighbouring position in proportion to the pair weights it would have in each, every move is in detailed balance with the static law on the occupied set. Motion conserves the number of records and their contents.
2. **A constant the rule cannot see (T2).** Multiply every pair weight by a scale `c`. The axioms' normalized distribution does not change. The motion does, exactly when a move changes the number of record–record bonds. The scale is how much a bond between two records outweighs a bond with an empty end: a binding constant. A record with `k` agreeing neighbours escapes to an isolated position with probability `1/(1 + (cp)^k)`.
3. **The other reading is not an equilibrium (T3).** If a move is accepted with the rule's normalized probability of that content at the destination, the scale cancels and the chain is reversible for no law: moving carries an arrow of its own, with no formation at all.
4. **The formation rate that fits (T4).** Formation at an empty site at a rate proportional to the rule's normalizer there, with the content drawn from the rule, is the creation half of a reversible pair for the same static law, and it is the only such rate. At the neutral scale, where an empty neighbour weighs what a record of random content weighs on average, one neighbouring record leaves the formation rate unchanged, two agreeing ones raise it and two opposite ones lower it.
5. **Reflection positivity bounds the scale from below (T5).** Count the empty state as a seventh state of a site. The static law with vacancies is reflection positive through bond planes exactly when the binding scale is at least the neutral scale (and the rule's own weights are positive semidefinite, `p ≥ q` and `p + q ≥ 2r`). Below the neutral scale it is not. So a principle the framework already relies on gives a lower bound on the constant, and the neutral scale is its boundary value.
6. **Executed, not claimed.** On the cubic lattice at density `0.3` records stay spread out below an onset and gather into aligned clusters above it, and the onset moves with the scale: near `p = 10` on the line `(p,1,2)` at the neutral scale, between `5` and `6` at scale `1`. Mobility falls to a few percent at strong preference while seven tenths of the sites are empty.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'records move - they can transit between nodes assuming the neighborhood allows'; 'this weight is a primitive like planck - if we derive or find it, we can state it'; block 36 (PR #8507): the comparator is an equilibrium only if something re-forms or moves"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the moving-records reading made exact on finite windows: equilibrium, the binding scale, the irreversibility of the normalized reading, the fitting formation rate; the clumping and jamming map executed on one line at three scales. the law with vacancies reflection positive exactly from the neutral scale up. Next: the onset of clumping as a function of the weight ratios and of the density (probe grids); rigorous bounds on it; the transverse kernel's stiffness in a clumped aligned cluster; the owner's decisions on the motion clause and on the scale (a primitive, or fixed by the neutral principle)"
conditional_surface_status: "T1-T4 proved on finite windows under the supplied motion clause and scale; the executed map (one or two seeds, lattices of side 16 and 24, 2000 sweeps) is in the controls and not claimed; nothing is adopted and no primitive is registered"
hypothetical_axiom_status: "a motion clause ('a record may transit to an empty neighbouring site, choosing between its two positions in proportion to the pair weights') and a binding scale; stated as hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", "A site never carries more than one record; records are permanent.", and its list of open gates, which names "update laws" and "record-production dynamics, physical persistence dynamics" as outside the axiom content. Block 01 (on `main`, proposed and unaudited) supplies the rule as a product of pair weights and the static law of a product rule.

- **Configurations.** A finite graph of sites; each site is empty or carries one record with content in the six-axis menu. `η` is the occupied set.
- **Pair weights and the scale.** `W(a, b) = c·ω(a, b)`, `ω = p, q, r` for equal, opposite, orthogonal axes, `c > 0`. A bond with an empty end weighs `1`.
- **The rule.** `K(a | records around x) ∝ Π_{y∼x, y∈η} W(a, s_y)`, with normalizer `Z_x`.
- **The static law on the occupied set.** `μ(ζ) ∝ Π_{bonds with both ends occupied} W`, with the contents fixed (motion) or with a factor `z` per record (formation).
- **Pair-weight transit.** A bond with exactly one occupied end is visited (bonds at any symmetric rates); the record, of content `a` at `x`, with `y` the empty end, has local weights `w_x = Π_{v∼x, v≠y, v∈η} W(a, s_v)` and `w_y` likewise at `y`; it moves with probability `w_y/(w_x + w_y)`, or with any acceptance `A` such that `A(w_x, w_y)/A(w_y, w_x) = w_y/w_x`. `k_x, k_y` count the recorded neighbours entering `w_x, w_y`; `Ω_x, Ω_y` are the products of the `ω`'s.
- **Normalized transit** (the other reading): the move is accepted with `K(a | records around y, x excluded)`.
- **Neutral scale.** `c₀ = 6/(p + q + 4r)`, so that `(1/6) Σ_b W(a, b) = 1` for every `a`.

Exchange dynamics with conserved particle number is due to Kawasaki; heat-bath and ratio acceptances to Glauber and to Metropolis and co-authors; the cycle criterion for reversibility to Kolmogorov; laws of the static kind to Gibbs, with weights of the kind of Boltzmann. The complement used in T5 is the one of Schur; reflection positivity is the lattice form of the positivity condition of Osterwalder and Schrader. The lattice gas without content is the model of Ising in other variables; with content it belongs with the dilute models of Potts and of Blume, Emery and Griffiths. None is used as authority.

## Prior art and what is new

Blocks 01–16 separated the formation law from the static law and traced the difference to the rule's normalizers; block 24 (PR #8158) asked how an unrecorded site should be weighed; block 36 (PR #8507) showed that re-recording with the axioms' rule has the static law as its stationary law but needed a record at every tick, which the memo excludes. What is new: (i) the owner's reading that records move, which contradicts no sentence of the memo; (ii) under it, the same normalizer split decides between an equilibrium (pair weights) and an irreversible chain (normalized probabilities); (iii) the overall scale of the pair weights, invisible to everything the campaign computed so far, becomes a binding constant once records move or sites can be empty; (iv) the formation rate that belongs to the same equilibrium, and the neutral scale; (v) reflection positivity of the law with vacancies holds exactly from the neutral scale up, which is a lower bound on the constant from a principle already in use (blocks 17, 19 and the gravity lane's closure); (vi) an executed map of where records clump and jam. The lattice gas and its onset of condensation are classical; for content-less records the literature value of the onset on the cubic lattice is `e^{4K}` with `K = 0.2216544`, that is `2.427`, against which the simulator is calibrated and which is not used as a result.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | detailed balance of pair-weight transit with the static law; connectedness on the window | the ratio `μ(ζ')/μ(ζ) = w_y/w_x` | B |
| T2 | the scale cancels from `K` and enters the motion through `k_x − k_y` | direct | C |
| T3 | normalized transit: blind to the scale; no reversible law | a four-move cycle | D |
| T4 | the rate `zZ_x`; the neutral scale | one line of detailed balance | E |
| T5 | reflection positivity through bond planes iff `c ≥ c₀` (and `ω` positive semidefinite) | the complement of the empty state in the bond kernel; an explicit function on the four-site ring | E |

## Theorem T1 — pair-weight transit is in detailed balance with the static law

Let `ζ'` be `ζ` after the record at `x` has moved to the empty neighbour `y`. The bond `xy` has an empty end before and after and weighs `1`. The record loses its bonds at `x`, of total weight `w_x`, and gains those at `y`, of weight `w_y`; every other bond is unchanged. So `μ(ζ')/μ(ζ) = w_y/w_x`. In `ζ'` the reverse move has local weights `w_y` and `w_x` interchanged, and the same bond is visited at the same rate. Hence `μ(ζ) A(w_x, w_y) = μ(ζ') A(w_y, w_x)` for every acceptance with the stated ratio, in particular `w_y/(w_x + w_y)` and `min(1, w_y/w_x)`. On each set of arrangements connected by moves `μ` is the only stationary law; on the `2×3` window with two vacancies the moves connect all `180` arrangements of the contents `(+z, +z, −z, +x)`. Motion changes neither the number of records nor their contents. ∎

## Theorem T2 — the binding scale

A neighbourhood of `k` records multiplies every unnormalized weight of the rule by `c^k`, which cancels on normalization: `K` does not depend on `c`. For a move, `w_x/w_y = c^{k_x − k_y} Ω_x/Ω_y`, so `P(x → y) = 1/(1 + c^{k_x − k_y} Ω_x/Ω_y)`: the scale enters exactly when the move changes the number of record–record bonds. With `k` agreeing neighbours at `x` and none at `y`, `P = 1/(1 + (cp)^k)`. On the window of T1, at `(3,1,2)`, the motion probabilities at scales `1` and `1/2` agree on the `288` moves with `k_x = k_y` and differ on the `384` others. ∎

## Theorem T3 — normalized transit is blind to the scale and reversible for no law

Because `K` does not depend on `c`, neither does the chain. Take the arrangement `(+z, +z, −z, +x, ∅, ∅)` on the window and the two moves `3 → 4` and `2 → 5`. Going around the cycle "first record hops, second hops, first hops back, second hops back" the product of the acceptance probabilities is `1/2592`; around the same cycle in the other direction it is `1/2376` (the bond-visiting rates are equal and cancel). A chain reversible for some law has equal products around every cycle, so no law is reversible for this chain: its stationary law carries probability currents, with no formation in the dynamics. The pair-weight transit passes the same test. ∎

## Theorem T4 — the formation rate that belongs to the same equilibrium; the neutral scale

Let formation at an empty site `x` happen at rate `λ(ζ)` with content drawn from `K(· | records around x)`, and let a record be removed at rate `1`. Detailed balance with `μ_z(ζ) ∝ z^{|η|} Π W` reads `μ_z(ζ) λ K(a | ·) = μ_z(ζ^{x,a})`, that is `λ · Π W(a, s_y)/Z_x = z Π W(a, s_y)`, so `λ = zZ_x` and no other rate. With permanence there is no removal and only the creation half acts: the process grows, the content given formation is the axioms' distribution, and the rate depends on the neighbourhood through `Z_x = c^k Σ_a Π ω(a, s_y)`. At the neutral scale `Z_x/6 = 1` next to one record, whatever its content; at `(3,1,2)`, `c₀ = 1/2` and next to two agreeing, two orthogonal, two opposite records `Z_x/6 = 13/12, 1, 11/12`. ∎

**Remark (rare formation).** On a finite window the motion chain on a connected set of arrangements is irreducible and, because moves can be refused, aperiodic, so its law approaches `μ` for the records present. If formation events are separated by times long against that relaxation, the arrangement just before each formation is as close as desired to the static law on the occupied set: the lattice is in equilibrium for the records it has, and only formation, which is irreversible, carries an arrow.

## Theorem T5 — reflection positivity bounds the binding scale from below

Treat the empty state as a seventh state `∅` of a site, with the a priori weight `1` for `∅` and `z` for each content. The static law with vacancies is then a nearest-neighbour pair law with the bond kernel `B(∅, ·) = B(·, ∅) = 1`, `B(a, b) = cω(a, b)`. For a reflection through a bond plane the crossing bonds join a site to its image, and if `B = Σ_k λ_k f_k ⊗ f_k` with `λ_k ≥ 0` the product of the crossing factors is a sum with non-negative coefficients of terms `g(ζ_+) g(θζ_−)`, so `E[F · θF] ≥ 0`: a positive semidefinite bond kernel gives reflection positivity, for every `z`. `B` has the entry `1` at `(∅, ∅)`, so it is positive semidefinite exactly when the complement of the empty state, `cω − J` (`J` the all-ones matrix), is. On the constant vector `ω` has the eigenvalue `p + q + 4r` and `J` the eigenvalue `6`; on the vectors orthogonal to it `J` vanishes and `ω` has the eigenvalues `p − q` (three times) and `p + q − 2r` (twice). So `B` is positive semidefinite exactly when `p ≥ q`, `p + q ≥ 2r` and `c ≥ 6/(p + q + 4r) = c₀`. Conversely, on the four-site ring with the reflection exchanging its two bonds-halves the reflection form is `Gᵀ(B ⊗ B)G` with `G` arbitrary, and with `v = (−6, 1, …, 1)`, `w = (1, 0, …, 0)`, `G = v ⊗ w` it equals `(vᵀBv)(wᵀBw) = 6(c(p + q + 4r) − 6)`, negative for `c < c₀`: at `(3,1,2)` it is `−18` at `c = 1/4`, `0` at `c₀ = 1/2`, `36` at `c = 1`. For the sphere menu the same computation gives `c₀ = β/sinh β`. ∎

So the neutral scale has two characterizations: an empty neighbour weighs what a record of uniformly random content weighs on average (T4), and it is the least scale at which the law with vacancies is reflection positive. If reflection positivity is required of the law, the binding constant is at least `c₀`.

## Executed: where records clump and jam (not proved)

Controls in the pack (`specs/supervisor_control_block39_*`). The simulator visits every bond once per sweep in 48 sublattice passes whose bonds do not interact; it agrees with a site-by-site reference on a lattice of side `8`. Observables, averaged over the last quarter of the run: the mean number of recorded neighbours per record over its value for random placement (`6ρ`); the fraction of record–record bonds with equal contents (`1/6` at random); the fraction of proposed moves accepted.

*Calibration, content-less records (`p = q = r = 1`), density `1/2`, side `16`.* The density structure factor at the smallest wavevector is `0.5, 2.0, 1.7, 5.3` at `c = 1.5, 2.0, 2.2, 2.43` and `39, 57, 114` at `c = 2.7, 3, 4`: the onset lies between `2.43` and `2.7`.

*Line `(p,1,2)`, density `0.3`, side `16`, 2000 sweeps.*

| `p` | neutral scale: neighbours / aligned / accepted | scale `1`: neighbours / aligned / accepted | scale `1/2`: neighbours / aligned / accepted |
|---|---|---|---|
| `3` | `1.01 / 0.25 / 0.47` | `1.41 / 0.25 / 0.38` | `1.01 / 0.25 / 0.47` |
| `4` | `1.01 / 0.31 / 0.45` | `1.49 / 0.32 / 0.34` | `1.05 / 0.31 / 0.45` |
| `6` | `1.02 / 0.41 / 0.41` | `2.24 / 0.71 / 0.27` | `1.13 / 0.42 / 0.39` |
| `8` | `1.04 / 0.51 / 0.37` | `2.43 / 0.83 / 0.18` | `1.33 / 0.62 / 0.34` |
| `12` | `1.39 / 0.83 / 0.30` | `2.56 / 0.86 / 0.10` | `2.21 / 0.95 / 0.22` |
| `16` | `1.71 / 0.94 / 0.27` | `2.45 / 0.86 / 0.07` | `2.33 / 0.96 / 0.15` |
| `24` | `1.84 / 0.97 / 0.23` | `2.38 / 0.86 / 0.05` | `2.34 / 0.95 / 0.09` |
| `48` | `2.02 / 0.99 / 0.18` | `2.31 / 0.83 / 0.03` | `2.20 / 0.94 / 0.04` |

On a lattice of side `24` (second seed): neutral scale `1.04 / 0.51` at `p = 8`, `1.14 / 0.66` at `10`, `1.43 / 0.84` at `12`, `1.70 / 0.93` at `16`; scale `1`: `1.49 / 0.32` at `p = 4`, `1.64 / 0.42` at `5`, `2.18 / 0.70` at `6`, and at `p = 24` an acceptance of `0.049`. The refuting control solves the stationary laws exactly on the `2×3` window: pair-weight transit has the static law (total variation `0`, detailed balance) with one and with two vacancies; normalized transit differs from it by `0.20` (one vacancy, where it happens to be reversible) and `0.146` (two vacancies, not reversible), gives the four records a `2×2` clump with probability `0.1195` against `0.1333` at random and the same at twice the scale, while pair-weight transit gives `0.22` and, at twice the scale, `0.40`.

## No-Go Discipline Gate

T3 is a negative sentence (no law is reversible for normalized transit); the gate applies.

### N1 — Routes by which the sentences could fail
1. *The clause* — motion is supplied, not axiom content; the note is conditional on it.
2. *Other acceptances* — T1 covers every acceptance with the ratio `w_y/w_x`; acceptances built from `K` are T3's.
3. *Connectedness* — it depends on the window and the number of vacancies (a single vacancy on a cycle keeps the cyclic order of the records); T1 asserts uniqueness only on connected sets of arrangements.
4. *One vacancy* — on the `2×3` window with one vacancy the normalized chain happens to be reversible (for a law `0.20` away from the static one); T3's witness needs two moving records.
5. *The executed map* — one or two seeds, sides `16` and `24`, `2000` sweeps; at strong preference the dynamics arrests in many small clusters, so the large-scale structure factor understates the clumping there; the onset values are brackets, not estimates of a limit.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the declared clause and scale.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the distribution sentence; "Records form."; the one-record sentence; the open gates | yes (premise and boundary) |
| block 01 (`main`) | the rule as a product of pair weights; the static law | yes (premise, proposed) |
| block 24 (open PR #8158) | how an unrecorded site is weighed | placement |
| block 36 (open PR #8507) | the comparator as an equilibrium under a clause the memo excludes | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "pair-weight transit equilibrates to the static law; the scale is invisible to the rule and visible to motion; normalized transit is reversible for no law; the rate `zZ_x`" | executed: detailed balance of every move; the scale cancelling from `K`; the escape probability | executed: all 180 arrangements at three weight and scale choices; all 2401 configurations of the four-cycle | not applicable | executed: connectedness; the four-move cycle | proved on every finite window under the clause; the clumping and jamming map executed and not claimed; nothing adopted |

### N6 — Partial-closure paths and primitive scan
The registered primitives (scale reference, kinetic isotropy, realized state) supply neither motion nor a binding scale. The scale is a candidate primitive; registering it is the owner's act and is not done here.

### N7 — Steelman
Hostile reviewer: "This is the lattice gas with exchange dynamics, in every textbook." Reply: the mathematics is, and the note says so. What the campaign did not know is which parts of it the axioms fix. They fix the content of a forming record and nothing about motion; any motion that respects the pair weights makes the campaign's comparator an equilibrium without contradicting a sentence of the memo; and it exposes one number that the axioms' distribution cannot carry. That is the form in which the owner can decide it.

### N8 — Cross-cycle echo
The normalizer split of blocks 01–16 returns as the split between the two transit readings; block 24's question about unrecorded sites returns as the binding scale; block 36's conclusion is obtained again without its excluded clause.

## Falsifiers
- A move of the pair-weight transit violating detailed balance with the static law, or an arrangement not reached (B1–B2).
- A neighbourhood where the scale changes `K`; a move with `k_x = k_y` whose probability depends on the scale, or one with `k_x ≠ k_y` whose probability does not; an escape probability other than `1/(1 + (cp)^k)` (C1–C3).
- Normalized transit depending on the scale, or every four-move cycle balanced (D1–D2).
- A configuration of the four-cycle where the birth-death pair with rate `zZ_x` is not balanced; a mean pair weight other than `1` at the neutral scale (E1–E2).
- A spectrum of the complement of the empty state other than the stated one; a non-negative reflection form for `v ⊗ w` below the neutral scale (E3).
- For the executed part: clumping at the neutral scale below `p = 8` on the line `(p,1,2)` at density `0.3`, or none at `p = 16`.

## Boundaries and non-claims
This note is conditional on a supplied motion clause (records move, carrying their content, by pair-weight transit) and on a supplied binding scale, neither of which is in the axioms memo; the memo lists update laws and persistence dynamics among its open gates, and nothing here is adopted. It proves T1–T4 on finite windows; it makes no infinite-volume statement, proves no onset of clumping, registers no primitive, fixes no value of the scale, and identifies the clusters it finds with nothing in nature. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises. Block 01 (on `main`): the rule and the static law; proposed, unaudited. Blocks 24 and 36 as evidence addresses.
- Named standard imports at definition level: detailed balance; the cycle criterion for reversibility (Kolmogorov); irreducible aperiodic finite chains approach their stationary law (Markov).
- Reference only: Kawasaki (1966) for conserved exchange dynamics; the literature value `K = 0.2216544` of the cubic lattice, used to calibrate the simulator and not as a result.

## Review record
Supervisor-run block (owner 2026-09-20: "records move — they can transit between nodes assuming the neighborhood allows"; "a single site can generate more than one record, but only one record allowed per site"; "this weight is a primitive like planck — if we derive or find it, we can state it"; "go for it"). Lens: the supervisor read the complete axioms memo before anything else; the one-record sentence does not exclude a record leaving, and motion is an open gate. The two readings of "the neighbourhood allows" were separated by exact stationary laws on a six-site window before any argument was written. Refuting pass: exact linear solves of the stationary laws (disjoint from the runner's detailed-balance checks); the simulator against a site-by-site reference and against the literature onset for content-less records. Fold: T5 was found after the first gate run, while asking what could fix the scale, and added before the pull request; the first draft expected the formation rate next to two orthogonal records to change at the neutral scale; it is exactly unchanged at `(3,1,2)`, and the runner's own value replaced the expectation. Mutation census: nine mutations, each failing in its own family.

## Verification

```bash
python3 scripts/admissibility_rule_records_that_move_pair_weight_transit_static_equilibrium_binding_scale_2026_09_20.py
python3 scripts/admissibility_rule_records_that_move_pair_weight_transit_static_equilibrium_binding_scale_2026_09_20.py --list-mutations
python3 scripts/admissibility_rule_records_that_move_pair_weight_transit_static_equilibrium_binding_scale_2026_09_20.py --mutation normalized_reading_reversible_injected
```
