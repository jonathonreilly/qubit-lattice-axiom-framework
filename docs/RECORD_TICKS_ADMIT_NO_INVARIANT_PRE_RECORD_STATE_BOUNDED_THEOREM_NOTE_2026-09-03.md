---
claim_id: record_ticks_no_invariant_pre_record_state
claim_type: bounded_theorem
claim_scope: "On the 2x2x2 cube graph (8 corners, 12 edge sites, 6 faces) with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, inside the N = 2 record sector of dimension 896 = 28 corner pairs x 32, under a STIPULATED tick model whose four choices are declared here and derived from nothing -- (i) a record forms at an unrecorded site with probability p per tick, independently across sites; (ii) a forming record locks its value by Lueders conditioning; (iii) between ticks the pre-record state runs for a time tau under the post-record Hamiltonian H_R = the hop terms on the sites carrying no record, the only terms of H commuting with every registered Z (Model A); (iv) Model B, named for contrast, keeps the full H for the tick and re-conditions afterwards. With no floating point in any statement tagged exact: (T1) the encoding relations R0-R4 hold pair by pair, k = 5, the code dimension is 2^12/2^5 = 128, the N = 2 record sector is 896-dimensional and is carried onto itself by every one of the 12 hop terms with unit Gaussian-integer amplitudes, the 28-coset code sector carries the exact diagonal gauge onto Jordan-Wigner and the spectrum {-4, -2, 0, 2, 4}, and the E = -4 ground state has amplitudes that are Gaussian integers over sqrt(2048) and carries 384 cancellation zeros = the 12 corner pairs sharing an x-face. (T2) If every site's record forms before any evolution, the finished set of records reproduces the Born diagonal of the pre-record state exactly, as Fractions, and the order within the tick leaves no trace: all 66 Z_e pairs commute, all 264 ordered (site, value) comparisons agree entrywise with 0 mismatches, and the chain rule along 20 shuffled full orders closes on the flat Born value every time. (T3) One record already ends that: conditioning the ground state on any single site's record gives var(H_R) = 1/4 on the 8 in-face sites and 3/8 on the 4 cross-face sites and never 0, the same conditioned states carry var(H) = 3/4 against the unconditioned 0, ||Q H_R |g_eb>||^2 = 0 on the in-face sites and 3/8 on the cross-face sites, and the forbidden mass after one record and one gap of length t is m(t) = c t^2 + O(t^4) with the exact rational coefficient c = 1/8. (T4) The joint kernel of {H_R - H_R'} over all 66 pairs of single-site record sets, together with {H_R - H} over the 12 single-site sets, has dimension 0 on the 896-dimensional sector: no nonzero pre-record state is invariant under all the post-record Hamiltonians at once. (T5) At tau = 0.5 five declared schedules that register the SAME finished set of 12 records give forbidden-pair mass 0, 0.535127, 0.333741, 0.147990, 0.260387 and L1 distances 0, 1.1023, 0.7705, 0.6920, 0.5514 to the pre-record Born diagonal, with L1(A,B) = 1.1023 and L1(B,C) = 0.9028 pairwise. (T6) The completion tick T of the finished set is max of 12 i.i.d. Geometric(p), so P(T <= t) = (1 - (1-p)^t)^12 and E[T] = sum_j (-1)^(j+1) C(12,j)/(1 - (1-p)^j), equal to 1, 4.977, 14.407, 60.999, 309.267 at p = 1, 1/2, 1/5, 1/20, 1/100 -- a function of p alone. One labelled seeded Monte Carlo witness accompanies T5 and the Model A/B contrast. This note declares a tick model and computes with it; nothing is derived from any axiom, no formation clause is supplied, no axiom is amended, no status is set, and no claim is made about what the framework's tick IS."
upstream_dependencies: []
runner: scripts/record_ticks_admit_no_invariant_pre_record_state_check_2026_09_03.py
---

# Record ticks admit no invariant pre-record state: on this model, conditioning alone is not an update clause

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/record_ticks_admit_no_invariant_pre_record_state_check_2026_09_03.py`](../scripts/record_ticks_admit_no_invariant_pre_record_state_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/record_ticks_admit_no_invariant_pre_record_state_check_2026_09_03.txt`](../logs/runner-cache/record_ticks_admit_no_invariant_pre_record_state_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

`RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7858) proves that the finished set of records carries the same odds
whatever order the records formed in -- for a **fixed** pre-record state. It then names two interfaces it does not settle: "the formation clause" and "the update clause as a
tick". This note answers the second on the same cube, in the same sector, by writing a tick model down explicitly and computing what it does: the order independence of PR
#7858 does not survive a tick. The moment the state is allowed to run between one record and the next, the finished set's odds depend on **when** the records formed, and the
selection-rule zeros of the ground state are vacated at first order in the gap length. Nothing here says what the framework's tick is, only what this one does.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-sector theorems on one named cluster -- the 896-dimensional N = 2 record sector of the 2x2x2 cube -- established with Gaussian-integer and Fraction arithmetic and F2/union-find combinatorics: the sector and its cancellation zeros, all-at-once formation against the Born diagonal, the exact first-order leak with a rational leading coefficient, the zero joint kernel of the post-record generator differences, and the exact clock law. The schedule table of T5 and two corroborating lines are deterministic double-precision evaluations of exactly specified quantities, tagged [numerical]; one section is a labelled seeded Monte Carlo witness, tagged [witness], and carries no theorem weight."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-sector theorem, and route to its owner the science-level question this note does not decide: what an update clause must supply beyond conditioning, of which T4 and T5 are the obstruction any candidate has to answer."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`: `T1` (`A`) the sector and its zeros; `T2` (`B`) all-at-once formation
reproduces the Born diagonal and the within-tick order leaves no trace; `T3` (`C`) the first-order leak with its exact rational coefficient; `T4` (`D`) the zero joint kernel,
no invariant pre-record state; `T5` (`E`) schedule dependence; `T6` (`F`) the clock. Group `G` is a **labelled witness**, not part of the target. Groups `A`, `B`, `D` and `F`
and the first four lines of `C` are exact: Pauli algebra in the symplectic representation with phases mod `4`, Gaussian-integer amplitudes, `Fraction` arithmetic, and a
union-find over unit ratios in `Z4`. Four lines -- `C5` and the three of `E` -- are **deterministic double-precision evaluations** of exactly specified quantities: the
propagator `exp(-i H_R t)` is transcendental, so no rational value exists to compare against, but there is no sampling and no seed anywhere in them; they are tagged
`[numerical, 1e-9]`. Group `G`'s two lines are tagged `[witness]`, with seeds and trajectory counts printed.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Jordan-Wigner transform, Slater determinants, Lueders conditioning and the
geometric distribution are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's relations included. No observational
value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight:
`RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7858 -- the same cube, encoding and stipulated conditioning rule,
whose Theorem 5 is order independence for a fixed pre-record state and whose Theorem 7 supplies the `E = -4` ground state and its `384` cancellation zeros) and
`EMERGENT_DICTIONARY_SELECTION_RULE_ZEROS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7842 -- the same selection-rule zeros from the dictionary side); and
`MINIMAL_AXIOMS_2026-06-29.md`, from which the four axioms in "Setting" are quoted verbatim. This note cites no grade of any of these and consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." "No site is privileged. Sites are distinguished by the supplied lattice structure alone." **Qubit / Site
Possibility**: "Each site has a domain of local possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`." "No possibility is privileged.
Possibilities are distinguished by the supplied algebraic structure alone."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each
site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Reading note (2), interpretive and
non-governing, is the exact hinge of this note and is quoted with it: "(2) Read with Record, the distribution concerns which possibility a forming record locks, conditional on
formation at that site; **it does not supply the formation site, probability, or rate.**" Reading note (3) adds that the distribution is a probability measure on the local
possibility domain whose support is what "admissible" denotes, and that "Record locks a supported realization."

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are
permanent." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded or signed clause
is used anywhere. The cube below is a finite open subgraph of that lattice, drawn as a graph, so "edge site" and "corner" have their graph meanings. The **record ontology** is
used as declared: a record at an edge site registers a value there; it does not report one the site already had. Everything below concerns the declared tick model applied to a
declared state: reading note (2) says the axioms supply no formation site, probability or rate, and this note **stipulates** one so the consequences can be read off.

## The stipulated tick model, declared in full

Four choices, all made here, none derived. A lane proposing a different tick inherits the obligations of `T4` and `T5` and none of these choices.

1. **Formation.** At each tick, each site that carries no record forms one with probability `p`, independently of the other sites and of the past; a site's formation tick is
   therefore `Geometric(p)`, and the finished set is complete at the tick `T` at which the last of the `12` has formed.
2. **The value a forming record locks: Lueders conditioning.** When a record forms at site `e` and locks the value `b`, the state is restricted to the `Z_e = b` eigenspace and
   renormalized, the value drawn from the state's own odds at that site. Within one tick this is order-blind, because the `Z_e` commute (`T2`).
3. **The gap: the post-record Hamiltonian `H_R`.** Between ticks the pre-record state runs for a time `tau` under `H_R` = the sum of the hop terms on the sites that carry no
   record, exactly the terms of `H` commuting with every registered `Z`, so the only generator of the family leaving every value already registered untouched. Call it **Model
   A**; it is the model of `T3`-`T5`.
4. **Model B**, named here for contrast and reported only in the witness section, keeps the **full** `H` for the tick and re-conditions on the registered values afterwards --
   a different declared choice, not a correction of the first. The two agree at short `tau` and diverge at long `tau`, which is the point of reporting it.

`tau = 0` (records forming faster than the state can run) and `p = 1` (every record forming at the first tick) are the boundary cases; `T2` is exactly that boundary, and the
only place in this note where the pre-record state's Born diagonal survives.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is precisely `P0`-`P6`.

`P0` (declared here): the cube, the edge-site qubits, the encoding, the parity dictionary, and the four stipulated tick choices above. `P1` (`A`): the sector, the gauge and
the ground state's cancellation zeros. `P2` (`B`): the `tau = 0` boundary. `P3` (`C`): the first-order leak. `P4` (`D`): the zero joint kernel. `P5` (`E`): schedule
dependence. `P6` (`F`): the clock.

## Definitions

The **cube** is the `2x2x2` cube graph, corner `s = 4a + 2b + c`, `8` corners, `12` edge sites, `6` faces. One qubit sits on each **edge site**, neighbours ordered by index:

```text
A_ij = X(edge ij) * prod Z(edges at i ordered before j) * prod Z(edges at j ordered before i),   A_ji = -A_ij,
B_v  = prod of the Z's on the edges incident to v,     S_f = the ordered product of the A's around a face f,
H    = sum over edges of the encoded hop T_e = (i/2) A_ij (B_i - B_j),          star(v) = the edges incident to v.
```

A **record** at an edge site registers a `Z`-value there, so a **finished set of records** is a vector `y` in `F2^12`; the **parity dictionary** is `n_v(y) = (1 - B_v)/2 = |y
intersect star(v)| mod 2`, and the **record number** is `N = sum_v n_v`. The **`N = 2` record sector** is the span of the `896` patterns of record number `2`; it is `28`
corner pairs times `32`, and every hop term carries it onto itself, so no object above `896 x 896` is formed anywhere in the runner. The **odds at a site** are the probability
that a record forming there locks the value `1`, given the records already present. The **pre-record state** used throughout is the `E = -4` Slater ground state of the encoded
hopping, with Gaussian-integer amplitudes over `sqrt(2048)`. A **cross-face** site is one of the `4` edge sites joining the two `x`-faces; the other `8` are **in-face**. `Q`
projects onto the `384` sector patterns whose corner pair shares an `x`-face -- the ground state's cancellation zeros. A **schedule** is a list of (gap in ticks, sites
forming) pairs; all schedules below register all `12` sites and differ only in when.

## Theorem 1 -- the sector, the gauge, and the ground state's zeros

**Conclusion.** `[exact]` On the cube: the superfast relations `R0`-`R4` hold pair by pair, the face group contains no `-I`, `k = 5`, and the code dimension is `2^12/2^5 =
128`. The `N = 2` record sector is `896`-dimensional, `28` corner pairs times `32` patterns each, and **every one of the `12` hop terms carries it onto itself** with unit
Gaussian-integer amplitudes; `H` is Hermitian on it. On the `28`-coset code sector, `2^5 H_enc` is Gaussian-integer, an exact diagonal gauge in `{1, i, -1, -i}` carries it
entrywise onto the Jordan-Wigner matrix of the same law, and the spectrum is exactly `{-4, -2, 0, 2, 4}`. The `E = -4` ground state is an exact eigenvector with
Gaussian-integer amplitudes over `sqrt(2048)` and carries `384` cancellation zeros -- `12` corner pairs times `32` -- exactly the corner pairs sharing an `x`-face. The `4`
cross-face edge sites are `(0,4), (1,5), (2,6), (3,7)`.

**Proof.** The relations are an exhaustive symplectic computation with `Z4` phases; the sector is built by evaluating the parity dictionary on all `4096` patterns and keeping
record number `2`; closure is checked by applying every hop term to every one of the `896` and asserting the image index and the unit amplitude; the gauge is fixed by a
spanning-tree walk and verified entrywise with zero residual; the ground state is built from the hypercube characters, rounded to Gaussian integers, and its eigenvector
property and zero census read off. All exact, reproducing PR #7858's Theorem 7 and PR #7842's zero count from the sector side.

**Reading, not theorem.** The state this note starts from shows the sharp pattern: twelve corner pairs the law allows but it never registers, its amplitudes cancelling there.

## Theorem 2 -- if every record forms before any evolution, the pre-record state's odds survive exactly

**Conclusion.** `[exact]` If every site's record forms in the same tick, before any evolution: the finished set of records reproduces the Born diagonal of the pre-record state
**exactly** -- all `28` odds equal as `Fraction`s, `12` of them `0`, summing to `1`. The order inside that tick leaves no trace: all `66` `Z_e` pairs commute in the symplectic
representation; over all `264` ordered (site, value) comparisons the two conditioned states agree entrywise with `0` mismatches; and walking the chain rule along `20` shuffled
full `12`-site orders, on three target record patterns each, closes on the flat Born value of that pattern every one of the `60` times.

**Proof.** Conditioning on a `Z` value is a coordinate masking of the Gaussian-integer amplitude vector, so both orders produce the identical integer vector and the comparison
is entrywise on integers; the chain-rule products are `Fraction`s of integer squared norms, and the commutation is checked in the symplectic representation. All exact.

**Reading, not theorem.** This is PR #7858's order independence, recovered as the boundary case `tau = 0`: when nothing happens between the records, the finished set is the
pre-record state's own diagonal, zeros and all. Everything below is what happens when something does.

## Theorem 3 -- one record already vacates the zero set at first order

**Conclusion.** `[exact]` Conditioning the ground state on any single site's record, at either value (the odds are `1/2` at every site, so each conditioned state carries
weight `1/2`):

1. `var(H_R) = 1/4` on the `8` in-face sites and `3/8` on the `4` cross-face sites, and is **never `0`** -- the conditioned state is an eigenstate of no post-record
   Hamiltonian.
2. The same conditioned states carry `var(H) = 3/4` against the full Hamiltonian, while the pre-record state itself has `var(H) = 0` exactly: it is the record, not the gap,
   that starts the leak. And `||Q H_R |g_eb>||^2 = 0` on the in-face sites and `3/8` on the cross-face sites, so through those four sites the generator carries the conditioned
   state **out of the zero set at first order in the gap length**.
3. Consequently the forbidden mass after one record and one gap of length `t`, with the remaining `11` records forming immediately, is `m(t) = c t^2 + O(t^4)` with the exact
   rational leading coefficient `c = (1/12) sum_e sum_b w_eb ||Q H_R |g_eb>||^2 = (1/12)(4 x 3/8) = 1/8`.
4. `[numerical, 1e-9]` Evaluating the same `m(t)` on the sector matrices with no sampling gives `0.000012, 0.001246, 0.028694, 0.118672` at `t = 0.01, 0.1, 0.5, 2.0`, and
   `m(0.01)/0.01^2 = 0.12500` against `c = 0.125`.

**Proof.** The conditioned states are coordinate maskings of a Gaussian-integer vector, `H_R` has entries in `{0, i, -i}`, and `Q` is a coordinate projector, so every
variance, every overlap and the coefficient `c` are `Fraction`s of integer squared norms; items 1-3 carry no floating point. Item 4 diagonalizes the two conditioned blocks per
site and evaluates the propagator, unsampled.

**Reading, not theorem.** A single record is enough. It leaves the state no longer at rest under the generator that governs the next gap, and the four sites joining the two
faces point it straight at the pairs it was not registering. Wait any positive time and those pairs start to register.

## Theorem 4 -- no pre-record state is invariant under all the post-record Hamiltonians

**Conclusion.** `[exact]` On the `896`-dimensional sector: not one basis pattern is annihilated by all `12` hop terms, so the joint kernel of `{H_R - H}` over the `12`
single-site record sets is already `0`; and the joint kernel of `{H_R - H_R'}` over all `66` pairs of single-site record sets, taken with `{H_R - H}`, has **dimension `0`**.
There is no nonzero pre-record state on which the choice of which record has formed leaves the generator unchanged. `[numerical, 1e-9]` The deleted hop terms do not commute
with `H` either -- `max ||[H, T_e]|| = 1.0000` over the `12` sites -- so `H` and the post-record Hamiltonians share no eigenbasis.

**Proof.** Each hop term is a signed partial permutation on the sector: column `a` carries a single unit entry `+-i` at row `a xor 2^e`. Hence `T_e v = 0` iff `v` vanishes on
that term's support, and each condition `(T_e v)[b] = (T_f v)[b]` couples exactly two coordinates by a **unit ratio**. The whole system of `69888` conditions is therefore
closed exactly by a union-find carrying a phase in `Z4`, an inconsistent cycle or a one-sided condition forcing its component to zero; the surviving component count is the
kernel dimension, and it is `0`. No floating point, no eigenvalue threshold, no rank tolerance.

**Reading, not theorem.** Whatever state one starts from, the records already formed change what it does next, and change it differently depending on which records they are.

## Theorem 5 -- the same finished set of records, different odds

**Conclusion.** `[numerical, 1e-9]` At `tau = 0.5`, from the ground state, five declared schedules that all register the **same** finished set of `12` records and differ only
in when they form -- `A` all `12` at tick `1`; `B` one per tick in site order `0..11`; `C` one per tick in site order `11..0`; `D` one every `5` ticks in order `0..11`; `E`
two per tick over `6` ticks -- carry **forbidden-pair mass** `0`, `0.535127`, `0.333741`, `0.147990`, `0.260387` and **L1 distance to the pre-record Born diagonal** `0`,
`1.1023`, `0.7705`, `0.6920`, `0.5514`. Pairwise, `L1(A,B) = 1.1023` and `L1(B,C) = 0.9028`, the smallest pairwise distance among the five being `0.5514`. `B` and `C` register
the identical finished set in opposite orders and carry different odds.

**Proof.** Each schedule is evaluated by enumerating the **whole** record tree: at every stage the conditioned block is diagonalized once, the state is run for the declared
gap, the branch weights are the exact squared masses of each locked value, and the leaf weights are accumulated onto the `28` corner pairs. No sampling anywhere, no random
number drawn. The propagator is transcendental, so the values are double precision; the reported separations exceed their double-precision noise floor by twelve orders.

**Reading, not theorem.** PR #7858's Theorem 5 says the finished set of records carries the same odds in any order -- for a state held fixed while the records form. Let the
state run between the records and that stops being true: `B` and `C` end with the same twelve records and not the same odds.

## Theorem 6 -- the clock

**Conclusion.** `[exact]` Under the stipulated formation choice the completion tick `T` of the finished set is the maximum of `12` i.i.d. `Geometric(p)`, so `P(T <= t) = (1 -
(1-p)^t)^12` and `E[T] = sum_{j=1..12} (-1)^(j+1) C(12,j) / (1 - (1-p)^j)`, the second cross-checked exactly against the partial sum of the tail plus its exact rational
remainder. `E[T] = 1, 4.977, 14.407, 60.999, 309.267` at `p = 1, 1/2, 1/5, 1/20, 1/100`, and at `p = 1/2`, `P(T <= t) = 1/4096, 0.20142, 0.68319, 0.91018` at `t = 1, 3, 5, 7`.
`E[T]` is a function of `p` alone: it does not depend on `tau`, on the pre-record state, or on any of the odds above.

**Proof.** Independence across sites gives the product form for the completion tick; the expectation is the binomial expansion of `1 - (1 - q^t)^12` summed as `12` geometric
series, and the runner verifies that finite algebraic identity in `Fraction` arithmetic at every `p`, together with monotonicity of the distribution function. All exact.

**Reading, not theorem.** However badly the odds are scrambled, the count of records still ticks; how long a finished set takes is fixed by the formation probability alone.

## Numerical witness -- labelled, seeded, and carrying no theorem weight

`[witness]` Two Monte Carlo lines, reported for corroboration only; neither is part of the target and neither supports any statement above.

1. **The scrambling.** `2000` trajectories, seed `20260903`, `p = 0.2`, `tau = 0.5`, from the ground state under Model A: the finished set carries `0.3770 +- 0.0108` on the
   `12` forbidden pairs, which the pre-record state carried exactly `0` on; it sits `L1 = 0.1119` from uniform-on-`28` against a sampling noise floor of `0.0927` at this
   trajectory count, and `L1 = 0.7540` from the pre-record Born diagonal. Within sampling error the finished set has forgotten the pattern.
2. **Model A against Model B.** `1000` trajectories, seed `20260904`, `tau = 2.0`, `p = 0.05`: forbidden mass `0.402 +- 0.016` under Model A and `0.649 +- 0.015` under Model
   B, `L1(A, B) = 1.1300`. At short `tau` the two agree; at long `tau` they do not -- the `H_R` convention is a **declared choice**, and at long gaps the answer depends on it.

## Corollary -- what this says about the update clause

Within the setting declared above, on the cube's `N = 2` sector, and for the stipulated tick model alone:

1. **Lueders conditioning alone is not an update clause.** With any evolution between records -- `tau > 0` and `p < 1` -- the finished set's odds depend on the schedule
   (`T5`), and the selection-rule zeros of the stipulated ground state are vacated at first order in the gap length with the exact coefficient `1/8` (`T3`). The readable
   shadow that PR #7842's selection-rule zeros and PR #7858's Theorem 7 exhibit is a property of the **stipulated pre-record state**, not of any tick that lets the state run
   between records.
2. **What an update clause must therefore supply beyond conditioning.** Either records forming faster than the state runs -- the limit `tau/p -> 0`, of which `T2` is the exact
   boundary -- or a **pre-record state selection principle**: something re-supplying, at every stage, a state that is an eigenstate of the *current* post-record Hamiltonian.
   `T4` says no fixed state can serve, the joint kernel being `0`, so any such principle is a relaxation mechanism acting between records. It is named here as an interface and
   is **untested**; nothing here supplies it or shows one exists.
3. **The clock is unaffected.** By `T6` the ticks to a finished set are a fixed function of `p` alone: record accumulation supplies a clock whether or not the odds are
   preserved, so the failure in item 1 does not touch the counting.

## Reading, not theorem -- the whole thing in plain words

If the state can still hop between one record and the next, the finished set of records forgets the sharp pattern the resting state would have shown, unless every record forms
at once. Something has to hold the state at rest between records, and the axioms do not yet say what does. What survives regardless is the count: however scrambled the odds,
the number of ticks it takes to finish the set is fixed by how often records form.

## Interfaces named for other lanes, not settled here

- **The formation clause.** The site at which a record forms, the probability that it forms there, and the rate are all outside this note; reading note (2) says the axioms do
  not supply them, and this note stipulates them rather than deriving them. A lane writing that clause should treat `T4` and `T5` as the obstruction its clause has to answer.
- **The relaxation or selection principle.** Corollary item 2 names it and does not supply it. Whether a mechanism exists that re-supplies an eigenstate of the current
  post-record Hamiltonian at every stage, and whether it can be stated without a preferred tick, is untouched here.
- **Model A against Model B.** Which post-record generator a tick should use is a declared choice here; the witness shows it matters at long gaps, and nothing here decides it.
- **Larger clusters.** The `3x3x3` case, periodic boundaries, and record-number sectors other than `N = 2`, where the face relations and the sector dimension change, are
  outside this note.

## Remaining live routes

1. Whether the `t^2` coefficient of `T3` has a structural form on larger clusters -- here `(1/12) x 4 x 3/8`, one factor per cross-face site, but the cube is small enough that
   the pattern could be a coincidence of this cluster.
2. Whether any pre-record state, not necessarily an energy eigenstate, makes `T5`'s schedule dependence vanish. `T4` forbids the exact mechanism but does not exclude a state
   whose schedule-dependent odds happen to coincide, and none is offered.

## Executable claim block

The canonical machine-bound restatement of the six theorem conclusions.

```text
setting: qubits on the 12 EDGE sites of the 2x2x2 cube graph (8 corners, 6 faces); ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading notes (2) and (3)
encoding: A_ij = X(edge ij) * Z's ordered before it at both endpoints; A_ji = -A_ij; B_v the Z's incident to v; S_f the ordered four-A face loop; H = sum_e T_e
dictionary: n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2; record number N = sum_v n_v
tick_model: STIPULATED, four declared choices -- (i) each unrecorded site forms a record with probability p per tick, independently; (ii) a forming record locks its value by Lueders conditioning; (iii) between ticks the pre-record state runs for tau under H_R = the hop terms on unrecorded sites, the only terms of H commuting with every registered Z (Model A); (iv) Model B keeps the full H then re-conditions. None derived; no formation site, probability or rate is taken from any axiom
T1_sector: R0-R4 pair by pair; k = 5; code dim 2^12/2^5 = 128; N = 2 record sector 896 = 28 corner pairs x 32, carried onto itself by every one of the 12 hop terms with unit Gaussian-integer amplitudes; 28-coset code sector: 2^5 H_enc Gaussian-integer, exact diagonal gauge in {1,i,-1,-i} onto Jordan-Wigner, spectrum {-4,-2,0,2,4}; the E = -4 ground state is an exact eigenvector with Gaussian-integer amplitudes over sqrt(2048) and carries 384 cancellation zeros = 12 corner pairs x 32 = exactly the corner pairs sharing an x-face; the 4 cross-face sites are (0,4), (1,5), (2,6), (3,7)
T2_all_at_once: every record forming before any evolution reproduces the Born diagonal of the pre-record state exactly, 28 odds equal as Fractions, 12 zeros, total 1; 66 Z_e pairs commute; 264 ordered (site, value) comparisons agree entrywise, 0 mismatches; 20 shuffled full orders x 3 target patterns = 60 chain-rule products, all equal
T3_leak: var(H_R) = 1/4 on the 8 in-face sites, 3/8 on the 4 cross-face sites, never 0; the same conditioned states carry var(H) = 3/4 against 0 for the pre-record state; ||Q H_R |g_eb>||^2 = 0 in-face and 3/8 cross-face; m(t) = c t^2 + O(t^4) with c = (1/12)(4 x 3/8) = 1/8 exactly; [numerical, 1e-9] m(t) = 0.000012, 0.001246, 0.028694, 0.118672 at t = 0.01, 0.1, 0.5, 2.0, and m(0.01)/0.01^2 = 0.12500
T4_no_invariant_state: 0 of the 896 sector basis patterns are annihilated by all 12 hop terms; the joint kernel of {H_R - H_R'} over all 66 pairs together with {H_R - H} has dimension 0 on the 896-dim sector, closed exactly by union-find over 69888 unit-ratio conditions with a phase in Z4; max ||[H, T_e]|| = 1.0000 [numerical]
T5_schedules [numerical, 1e-9]: tau = 0.5, the SAME finished set of 12 records; forbidden-pair mass 0, 0.535127, 0.333741, 0.147990, 0.260387; L1 to the pre-record Born diagonal 0, 1.1023, 0.7705, 0.6920, 0.5514; pairwise L1(A,B) = 1.1023, L1(B,C) = 0.9028, smallest pair 0.5514; whole record tree enumerated, no sampling
T6_clock: P(T <= t) = (1 - (1-p)^t)^12; E[T] = sum_j (-1)^(j+1) C(12,j)/(1 - (1-p)^j) = 1, 4.977, 14.407, 60.999, 309.267 at p = 1, 1/2, 1/5, 1/20, 1/100; P(T <= t) at p = 1/2 is 1/4096, 0.20142, 0.68319, 0.91018 at t = 1, 3, 5, 7; a function of p alone
witness [seeded, not a theorem]: 2000 trajectories seed 20260903 at p = 0.2, tau = 0.5 give forbidden mass 0.3770 +- 0.0108, L1 to uniform-on-28 = 0.1119 against a 0.0927 noise floor; 1000 trajectories seed 20260904 at tau = 2.0, p = 0.05 give 0.402 +- 0.016 (Model A) against 0.649 +- 0.015 (Model B), L1(A,B) = 1.1300
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=24 FAIL=0
```

## Proof boundary

Every statement above is proved on **one finite cluster**, the `2x2x2` cube graph, and inside **one sector** of it, the `896`-dimensional `N = 2` record sector. Nothing is
claimed for larger clusters, periodic boundaries, infinite lattices, other record-number sectors, or any law family other than the one in "Definitions". The law is
**designed**, not derived: the encoding is chosen so that the Majorana relations `R0`-`R4` hold, the face constraints make that choice consistent, and the parity dictionary is
one readout map among many, with no minimality or uniqueness claimed for either.

**The tick model is stipulated in full and derived from nothing.** All four choices -- geometric formation with probability `p`, Lueders conditioning for the locked value, the
`H_R` convention, and the Model B alternative -- are declared in this note, not taken from any axiom. Reading note (2) is explicit that the axioms supply no formation site,
probability or rate, and this note supplies none either: it declares one and computes with it, so every statement here is about **that** model. **Nothing here says what the
framework's tick is**, and nothing forecloses any tick: a different update clause is not touched by `T5`, and `T4` constrains only the family of post-record generators
declared in choice 3. This is not a no-go; it is a worked instance whose obligations a candidate clause has to answer.

Four lines -- `T3` item 4 and the three of `T5` -- are **deterministic double-precision evaluations** of exactly specified quantities, tagged `[numerical, 1e-9]`: no sampling,
no seed and no random number, but a transcendental propagator against which no exact rational value exists. The witness section is a **seeded Monte Carlo**, tagged
`[witness]`, printed with its seeds and trajectory counts, and it carries no theorem weight: no statement in `T1`-`T6` depends on it. No absolute unit appears anywhere, no
axiom text is amended, extended, reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

An honest auditor should come away with a declared tick model and its consequences, not a claim about what the framework's tick is; five exact theorems and one whose central
table is a deterministic unsampled double-precision evaluation, on one named finite sector; the stipulation declared as stipulated in the front matter, the setting, its own
section, the claim block and the proof boundary alike; a single seeded Monte Carlo fenced into its own section and load-bearing for nothing; and the corollary written as an
obligation on a future update clause, not a foreclosure of one.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority" pointers
are plain text carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair at `PASS=24 FAIL=0`, runtime under the declared `120` seconds, stdout
under `5500` characters, a current zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a separate lane.
