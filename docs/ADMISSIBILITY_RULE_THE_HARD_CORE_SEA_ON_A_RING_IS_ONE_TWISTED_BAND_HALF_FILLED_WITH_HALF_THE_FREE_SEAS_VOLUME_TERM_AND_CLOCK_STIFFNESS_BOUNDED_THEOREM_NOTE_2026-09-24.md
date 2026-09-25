---
claim_id: admissibility_rule_the_hard_core_sea_on_a_ring_is_one_twisted_band_half_filled_with_half_the_free_seas_volume_term_and_clock_stiffness_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Supplied nearest-neighbor coin-diagonal hard-core ring walk, L>=3 and positive bond weights, with
  separately chosen symmetric/antisymmetric composition and ground-energy minimization over record number. Exact
  gauge reduction to spinless fixed-number bands with signed cyclic coin twists; both signs have the same twist
  set and ground-energy function, hence equal derivatives only where those exist. Uniform rings with4 dividing L
  have half-filled minimum -csc(pi/L). Take the small-amplitude second variation first at these finite rings, then
  L to infinity at fixed0<|q|<pi, then q to0: the stated nonzero-mode coefficient gives c0=-1/pi and kappa=1/(6pi).
  Uniform q0 has a different cosine normalization; checkerboard qpi is exactly invariant. No higher-dimensional
  sea, physical filling rule, complete readout equivalence or stiffness at arbitrary degenerate fields is derived.'
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22
- admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_the_hard_core_sea_on_a_ring_is_one_twisted_band_half_filled_with_half_the_free_seas_volume_term_and_clock_stiffness_2026_09_24.py
---

# The hard-core sea on a ring is one twisted band: it is half filled, with half the free sea's volume term and clock stiffness

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact on rings, within blocks 54, 76 and 78 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 54, 76 and 78 as landed on main (the clocked walk, the sea's energy as a function of the rates, and the reduced ring walk with its hard-core compression); it reports the exact energy of the hard-core sea on a ring and its response to the rates; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 76, as landed, kept the sea's exact symmetries: a chessboard of clocks is invisible to it. It kept only a declared comparator for the sea's response to the rates, "not the exact sea Hessian", and established no induced stiffness. Block 78, as landed, showed that one record per site is an interaction, so the free sea is only a comparator. This note gives the exact answer on a ring: the energy of this separately supplied hard-core ground-state prescription, and how it responds to the rates.

- **T1: packing.**
  - At one record per site the generator is zero: nothing can move.
  - Below it the generator is traceless and nonzero, so the sea's energy is negative.
  - A chessboard of clocks leaves every bond product at one, so it is invisible.
- **T2: one band.**
  - On a ring the reduced walk never changes a record's coin, and records cannot pass each other.
  - After a gauge, every hop is the same spinless hop. A hop across the wrap bond also rotates the coin sequence, with a sign.
  - So the records are one spinless band whose wrap bond carries a twist.
- **T3: one twist set.** Fermionic and bosonic records carry the same set of twists. So they have the same ground-energy function at every positive rate field; derivatives agree wherever they exist.
- **T4: the sea and its stiffness.**
  - The lowest state over all record numbers is half filled.
  - Its response to a rate wave has the closed form `Π(q) = −cos²(q/2) ln(sec(q/2) + tan(q/2))/(4π sin(q/2))`.
  - So the volume term is `c₀ = −1/π` and the clock stiffness is `κ = 1/(6π)`. Both are exactly half the free sea's, with the same sign.

In plain terms, on a ring the supplied nearest-neighbor hard-core records, unable to pass each other, behave like a single band of particles, and it does not matter whether they are fermion-like or boson-like. Their lowest-energy sea fills half the sites. When the clock rates ripple, the sea's energy changes in a definite way. That is the stiffness a field of clocks would feel from the sea. It comes out exactly half of what the free, double-occupancy comparator gives, and with the same sign. It is the first exact induced stiffness in the lane, and it holds only in one dimension.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." The hard-core compression is supplied; with the nearest-neighbor hopping rule records cannot pass each other. Fixed-number sectors do not themselves model record formation.
  - "Records form." The number of records in a sea is not given by the axioms. Here "the sea" is the lowest state over all record numbers, as in block 76.
  - "Admissibility is not a dynamics axiom." The walk, the rates and the composition are supplied clauses. Nothing is adopted.
- **The clocked walk** (block 54 as landed): `H_w = φHφ` with `φ = e^{u/2}`. A hop across the bond `xy` carries `φ_xφ_y`.
- **The ring walk** (block 78 as landed), with L>=3 and positive bond weights. `H = σ₃S`, with `⟨x|H|x+1⟩ = (−i/2)σ₃`.
  - `N` records, at most one per site, each with a coin. The generator is the free many-record generator compressed to configurations without a doubly occupied site.
  - The fermionic composition carries the order sign over modes `2x + coin`; the bosonic carries none. Block 78 calls both supplied model choices.
- **The rate mode and the coefficients** (block 76's definitions).
  - For `u = ε cos(qx)`, `E₀(ε) − E₀(0) = Π(q)ε²n + O(ε³)`.
  - The volume term is `c₀ = E₀/n`, and `Π(q) = c₀/4 + (κ/4)|q|²_lat + …` defines the clock stiffness `κ`.
- **Comparators, named only:**
  - the Jordan–Wigner map;
  - the spin–charge separation of one-dimensional hard-core particles (Lieb and Mattis; the Tomonaga–Luttinger picture);
  - induced stiffness (Sakharov's induced gravity);
  - the Fermi sea.

## Theorem T1 — packing, and the chessboard

*Statement.*
- (a) At `N = n` records the hard-core generator is zero.
- (b) For0<N<n on a finite connected hopping graph with nonzero off-site coin matrices and no on-site term it is traceless and nonzero, so its lowest eigenvalue is negative.
- (c) It depends on the rates only through the bond products `φ_xφ_y`. A chessboard `φ = c^{±1}` makes every bond product one on an even ring, so the sea is unchanged at every amplitude.

*Proof.*
- (a) Every hop lands on an occupied site.
- (b) Some record has an empty neighbour. There is no diagonal entry. A nonzero traceless hermitian matrix has a negative eigenvalue.
- (c) The hop amplitude of a record across `xy` is `φ_xφ_y⟨x|H|y⟩`, whatever the other records do.

∎

*Checked (B1).* The ring of six with generic rational bond weights: zero at six records; nonzero, traceless and hermitian at three; both signs. The chessboard's bond products on the even and odd rings.

## Theorem T2 — on a ring the records are one twisted spinless band

*Statement.* Write a configuration as positions `x₁ < … < x_N` and the coin sequence `(s₁, …, s_N)` in site order. After the gauge `g = Π_{i: s_i = ↓}(−1)^{x_i}`:
- (a) every hop not across the wrap bond `(L − 1, 0)` is the up-coin spinless hop, with the coin sequence unchanged;
- (b) a hop across the wrap bond is the spinless fermions' wrap hop, and it also applies the signed rotation `R` to the coin sequence. `R` carries the factor `1` for fermions and `(−1)^{N−1}` for bosons, times `−1` for a down coin crossing on an odd ring.

So the generator is `h_open ⊗ 1 + h_wrap ⊗ R + h.c.`: one spinless band whose wrap bond carries `R`, and its spectrum is the union over the eigenvalues of `R`.

*Proof.*
- A down coin's amplitude is the opposite of an up coin's, and the gauge's factor `−1` on the bond cancels it.
- Records cannot pass, so only the wrap hop changes their cyclic order.
- The fermionic order sign is trivial for neighbouring hops. At the wrap it is `(−1)^{N−1}`, the spinless fermions' own.

∎

*Checked (C1).* Every nonzero entry (counts reported in the canonical runner capture) of the generator on the ring of `8` (`4` and `6` records) and the ring of `7` (`3` records), with generic rational bond weights and both signs, against the prediction, including the coin-sequence map.

## Theorem T3 — both exchange signs share one twist set

*Statement.* The eigenvalues of `R` are all `N`-th roots of unity on even rings, and all `2N`-th roots on odd rings, for both exchange signs. So fermionic and bosonic records have the same ground energy and the same second variation wherever it exists, with no differentiability claim at arbitrary degeneracies.

*Proof.* `R` permutes coin sequences with signs. An orbit of period `p` whose signs multiply to `σ` contributes the `p`-th roots of `σ`. For even rings a sequence with exactly one down coin has full period N when N>=2 and supplies all N-th roots; N=1 is immediate. For odd rings and N>=3, one down coin has full period and negative product, while two adjacent down coins have full period and positive product, supplying all2N-th roots together. For N=2, the mixed sequence supplies the roots of-1 and the two constant sequences supply+1,-1; N=1 again is direct. The additional bosonic factor is a common sign which permutes these root sets. No other roots occur because `R^N = 1` on even rings for both signs, and `R^N = (−1)^{n_↓}` on odd rings. The ground energy is the minimum over twists of the band's lowest `N` levels, so it depends only on the twist set. ∎

*Checked (D1).* Orbit counting on the ring of `8` (`N = 4, 6`) and the ring of `7` (`N = 3, 6`), both signs.

## Theorem T4 — the sea, its volume term and its clock stiffness

*Statement.*
- (a) On a uniform ring with4 dividing L, with the twist `e^{iθ}` the band's levels are `sin((2πm + θ)/L)`. A window of `M` consecutive grid points sums to `sin(centre)·sin(πM/L)/sin(π/L) ≥ −1/sin(π/L)`. So for `4 | L` the lowest state over all `N` is half filled, with `E = −1/sin(π/L)`, at the twist `π`. The free sea has `−2cot(π/L)`.
- (b) Take the coefficient at epsilon=0 first on uniform rings with4 dividing L, where the half-filled twist-pi branch has a gap to unoccupied levels. Then let L increase along allowed momenta tending to fixed0<|q|<pi. For `u = ε cos(qx)` the half-filled band's second-order coefficient per site tends on long rings to

  `Π(q) = −cos²(q/2) ln(sec(q/2) + tan(q/2))/(4π sin(q/2)) = −1/(4π) + q²/(24π) + …`.

  It is the sum of the held term `−cos²(q/2)/(4π)` and the relaxation term.
The q->0 expansion is taken after that long-ring limit. At exactly q=0, H becomes exp(epsilon)H, so the epsilon-squared coefficient per site is c0/2, not c0/4: a uniform cosine has mean square1 rather than1/2. At q=pi the adjacent-site cosine sum vanishes, so every bond weight is unchanged and the coefficient is exactly0. The displayed formula has the same limiting value there but its integral proof is only for0<|q|<pi.

- (c) Hence `c₀ = −1/π` and `κ = 1/(6π)`: exactly half the free sea's `−2/π` and `1/(3π)`, which is two such bands, with the same sign.

*Proof.*
- (a) For a fixed N the N lowest sine levels form a consecutive window centered as closely as allowed around the minimum. Its sine-sum magnitude is bounded by sin(pi N/L)/sin(pi/L)<=csc(pi/L). For N=L/2 and twist pi the negative window is centered exactly at3pi/2; N is even so pi belongs to the allowed twist set. This attains the bound. Other fillings have a strictly smaller upper magnitude, so at finite L this is the minimizing record number. Coin-sector degeneracies within the same twist have identical charge energies for every rate field and do not split this branch.
- (b) The bond factor is `1 + εa_b + ε²a_b²/2`, with `a_b = cos(q/2)cos(q(x + ½))`. For plane waves:
  - `⟨k|h₂|k⟩ = sin k cos²(q/2)/4`;
  - `⟨k+q|h₁|k⟩ = ½cos(q/2)sin(k + q/2)`;
  - `e_k − e_{k+q} = −2cos(k + q/2)sin(q/2)`.

  For0<q<pi the two occupied-to-empty transition intervals have length q. Setting t=k+q/2 maps them to intervals with |t|<=q/2 modulo pi, so |cos t|>=cos(q/2)>0 and the integrand is bounded, so the finite sums tend to the integrals whatever the twist. The antiderivative is atan h(sin t)-sin t, equivalently ln(sec t+tan t)-sin t on |t|<pi/2. In detail the relaxation contribution is -cos^2(q/2)[atanh(sin(q/2))-sin(q/2)]/[4pi sin(q/2)]. Adding the held term gives the displayed formula. This perturbation result is not a claim that the finite-volume gap stays uniformly positive as L grows.
- (c) Read off the series.

∎

*Checked (E1).*
- The progression sum, symbolically for `M ≤ 8`.
- The half-filled sea at `L = 4, 8, 12, 16`, exactly.
- The held integral and the primitive.
- The closed form and its series.
- The factor of two against the free sea.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 76 as landed: its quadratic comparator is 'not the exact sea Hessian'; no induced stiffness is established"
source_of_blocker_text: block 76 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the half-filled hard-core sea in two and three dimensions (no spin-charge separation there); the 4x4 torus in momentum sectors; what fixes the sea's record number"
conditional_surface_status: "T1 on the stated finite nonzero hopping graphs; T2-T4 exact on rings (T4 in the long-ring limit); the walk, rates and composition supplied"
hypothetical_axiom_status: "the hard-core many-record walk is supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the clocked walk.
  - Block 76: the chessboard invariance and the definitions. Its comparator is declared, not derived.
  - Block 78: the reduced ring walk, and one record per site as an interaction.
- **Opened, not landed.** Block 128 (the exchange sign is not supplied by records). T3 shows that on rings these two supplied ring constructions have the same ground-energy function; full spectral multiplicities and readouts need not agree.
- **The probes attempt.** `the-hard-core-seas-energy` a1 (Claude Opus 5.5) found T1–T4, and executed the `3×3` torus in floating point. A Grok referee confirmed the exact ring statements (#9010).
  - The floating-point results are not used here: the torus tables, and the free sea's filling, where exclusion leaves `2^d` holes and the volume term vanishes per site.
- **In the literature.**
  - The Jordan–Wigner map.
  - Spin–charge separation for hard-core particles in one dimension (Lieb and Mattis; the Tomonaga–Luttinger picture).
  - Induced stiffness (Sakharov).

  All reference only.
- **New here:**
  - an independent exact runner, entry by entry;
  - the results placed against landed blocks 76 and 78;
  - the reading: the first exact induced clock stiffness in the lane, with the same sign as the comparator's, in one dimension.

## Exact target and obligation graph

Target: the exact energy of the hard-core sea on a ring and its response to the rates. The obligations are:
- (O1) packing (T1);
- (O2) the band (T2);
- (O3) the exchange sign (T3);
- (O4) the stiffness (T4).

T1–T4 discharge them. Open: two and three dimensions.

## No-Go Discipline Gate

The note's negative sentences:
- at one record per site nothing moves;
- on a ring the exchange sign changes neither the sea's energy nor its stiffness.

### N1 — Routes by which the sentence could fail or mislead
1. *Higher dimensions.* In two and three dimensions hops flip coins and records pass each other, so T2's reduction fails. The attempt's floating `3×3` values show the sign mattering there.
2. *Degenerate ground levels.* Where the ground level is degenerate across momenta, a rate mode can split it at first order, and then no second-order coefficient exists. For the specified uniform rings with4 dividing L, the charge branch at twist pi has no zero-energy level; derivatives are taken at fixed L before any infinite-volume limit. Arbitrary rate fields can still have crossings or cusps.
3. *The sea's record number.* "The sea" here is the minimum over `N`. A clause fixing `N` differently would change `c₀`.
4. *Other walks.* The reduction needs a coin-diagonal walk. A scalar hop adds coin-independent hopping; the down-coin gauge no longer makes its amplitude identical to the up-coin amplitude. That extension and staggered potentials are not covered by this reduction.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, rates and composition.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; records form; no dynamics in the axioms | yes |
| blocks 54, 76, 78 (landed) | the clocked walk; the definitions and chessboard; the ring walk and compression | yes (restated) |
| block 128 (open) | the exchange sign | no (placement) |
| probes (Grok-refereed #9010) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "one twisted band; one twist set; half filled; `c₀ = −1/π`, `κ = 1/(6π)`" | executed: all entries reported in the canonical capture against the band | executed: packing; the chessboard | executed: twist sets by orbit counting | executed: the window identity, the sea, the integrals, the series | T1 every connected lattice; T2-T3 on L>=3 rings; T4 under its uniform-ring and ordered-limit hypotheses; higher dimensions not treated |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "One dimension is special; this says nothing about the lattice of the axioms."
  - *Reply:* Agreed for the numbers.
  - The structural points (packing, the chessboard, the factor from exclusion) are exact where stated. The sign of the stiffness matching the comparator's is the first exact datum for block 76's question.

### N8 — Cross-cycle echo
- Block 76 kept a declared comparator.
- Block 78 found that one record per site is an interaction.
- This note gives, on rings, the exact sea under exclusion and its stiffness.

## Falsifiers

- A ring entry of the hard-core generator that differs from the gauged band's.
- A ring on which the fermionic and bosonic twist sets differ.
- A value of `Π(q)` on long rings that differs from the closed form.

## Boundaries and non-claims

- The walk, the rates and the composition are supplied.
- Two and three dimensions are not treated.
- The free sea's filling and the `3×3` numbers of the attempt are not used.
- No gravitational claim is made.

## Imports

- [Supplied source, block 54](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 76](ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 78](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 54, 76 and 78, restated. Block 128, placed.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the Jordan–Wigner sign;
  - second-order perturbation theory for a filled band;
  - Riemann sums of bounded integrands;
  - exact rational and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-eighth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results. A Grok referee confirmed the exact ring statements (#9010).
  - The supervisor re-checked them with its own runner, entry by entry.
- **Before writing.**
  - Main was re-fetched, and blocks 54, 76 and 78 were read as landed.
  - The own-prior-art check found block 80's withdrawn interacting-sea claim. This note gives the exact ring answer: the same sign.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_hard_core_sea_on_a_ring_is_one_twisted_band_half_filled_with_half_the_free_seas_volume_term_and_clock_stiffness_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
