---
claim_id: relaxation_tick_well_posed_loses_sea_record_statistics
claim_type: bounded_theorem
claim_scope: "On the 2x2x2 cube graph (8 corners, 12 edge sites, 6 faces) with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, in the staggered (pi-flux) sector H = -sum_e eta_e T_e with the Kawamoto-Smit link signs, whose 128-dimensional code space is the even-N space and whose ground state -- the sea -- has E = -4 sqrt 3, is non-degenerate with gap 2 sqrt 3 and is a sharp N = 4 state: under ONE STIPULATED tick model M_R, declared here and derived from nothing, in which (i) the next unrecorded edge site in a DECLARED order forms a record with the Born odds of the current pre-record state, (ii) the state is then replaced by the ground state of H restricted to the record-consistent subspace, (iii) with the normalised projector Pi/deg where that ground space is degenerate, and (iv) records are permanent, run to 12 records. (T1) Every hop term has Pauli X-part exactly one edge qubit, so P_S H P_S is the sum of the hop terms on the unrecorded sites: 'H restricted to the records' and the parent note's H_R are one operator, and M_R is memoryless -- its state is a function of the record set alone. (T2) The sea's own record odds are flat: every one of the 24 + 264 + 1760 = 2048 record blocks with k <= 3 carries sea weight 2^-k to 4e-15, so a forming record has odds 1/2 and nothing is forced up to three records; and at p = 1, where every site registers at once, the finished set is the sea's Born diagonal with support 1984 = 62 x 32 and 2112 zeros = 1856 charge zeros (N != 4) + 256 = 8 x 32 cancellation zeros whose 8 corner-occupation patterns are exactly the closed corner stars {v} u N(v). (T3) Under M_R the support is all 4096 patterns for every one of the 32 declared orders and none of the 2112 zeros survives; TV(M_R, sea) = 1283/2880 at the identity order, against 0.324925160534 for the parent note's Model A at tau = 0.5. (T4) TV(identity order, reverse order) = 1/3; over the 32 declared orders the maximal pairwise TV is 0.727031250000 and the minimal 0.113194444444, a lower bound on the spread over all 12! orders; pure Lueders conditioning is order-independent to 6e-15. (T5) <Q> = 0 and <N> = 4 at every declared order to 1e-14, but Q is not sharp: the identity-order law is (1/384, 1/8, 143/192, 1/8, 1/384) with var Q = 13/12, P(Q = 0) ranges 0.6146 .. 0.8813 over the declared orders, the 1456 tree nodes whose relaxed state is not N-sharp are exactly the 1456 carrying a degenerate ground space (ticks 5, 6, 8, 9, 11), and the declared variant M_R^N restores P(Q = 0) = 1 while still losing all 256 cancellation zeros, as Model A does. (T6) Relaxation is not conditioning: the relaxed state overlaps the Lueders-conditioned sea by 0.962606705806 at all 24 one-record blocks, by k = 3 the worst of 1760 blocks is at 0.448473881026 with mean 0.773546569701 and 64 blocks at 1; the conditioned column is exactly -(12 - k)/sqrt 3; E_0(R,w) <= <sea_S|H_R|sea_S> at all 2048 blocks with 0 violations, the tree-average drop peaking at k = 9 (0.401011505139) and vanishing at k = 0 and k = 12. (T7) Z_e commutes with all 8 corner parities at all 12 sites while X_e and Y_e each anticommute with exactly the two endpoint parities; Z_e anticommutes with exactly the two faces through its site; no one-site basis commutes with the corner and face dictionaries at once. No seeds anywhere: every distribution is the exact product over the whole 4096-leaf tick tree and every order is written out in the runner. This note declares a tick model and computes with it; nothing is derived from any axiom, no formation clause is supplied, no axiom is amended, no status is set, and no claim is made about what the framework's tick IS."
upstream_dependencies: []
runner: scripts/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.py
---

# A relaxation tick is well posed and loses the sea's record statistics

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.py`](../scripts/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.txt`](../logs/runner-cache/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

`RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7876) writes a tick model down and finds its answer turning on two declared choices it
cannot settle -- the gap length `tau` and the post-record generator `H_R` -- and names the interface it leaves open: something would have to re-supply, between one record and the
next, a state at rest under the current generator. At the campaign's vacuum panel on 2026-09-03 a candidate wording was proposed that would close exactly that interface: **"Between
records, the lattice settles into its lowest-energy arrangement."** That sentence is not axiom text. This note takes it as a **stipulation under test**, turns it into a tick on the
same cube in the staggered sector, and computes what it does against the reference it has to reproduce -- the half-filled sea's own record statistics. The result is two-sided: the
tick is well posed and memoryless, and it does not give back the sea's odds.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on one named cluster -- the 4096-dimensional record space of the 2x2x2 cube in the staggered sector, whose 128-dimensional code space is the even-N space -- for one stipulated tick model. T1 and T7 are exact symplectic-Pauli statements with no floating point, and T2's zero census is exact F2 combinatorics on a zero set identified from the Born diagonal at 1e-12. The tick trees of T3-T6 are enumerated whole, 4096 leaves and nothing sampled, but each node's relaxed state comes from a diagonalisation, so those lines are deterministic double-precision evaluations of exactly specified quantities and are tagged [numerical] with their thresholds. There is no seed anywhere in the runner and no Monte Carlo section."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-sector theorem, and route to the vacuum panel the science-level question it sharpens: a tick has to keep the sea's flat odds and its selection-rule zeros, and the record basis is already fixed by the corner parities, so what remains open is the formation rule -- the rate and the odds -- not the basis."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the seven statements below, exactly the runner's check groups `A`-`G`: `T1` (`A`) the restriction identity and the setting; `T2` (`B`) the sea's own
record odds and its zeros; `T3` (`C`) support; `T4` (`D`) order dependence; `T5` (`E`) charge; `T6` (`F`) relaxation against conditioning; `T7` (`G`) the pointer-basis table. Groups
`A1`-`A3` and `G` are **exact**: symplectic Pauli algebra with phases mod `4` and integer amplitudes. `B2` and `B3` are exact `F2` combinatorics on a zero set identified from the Born
diagonal at `1e-12`, and are tagged so. The rest are **deterministic double-precision evaluations** of exactly specified quantities at the stated thresholds. Nothing is sampled: every
distribution is the exact product over the whole `4096`-leaf tick tree, every order is written out in the runner, and there is **no seed anywhere** and no Monte Carlo section.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggered link signs, Lueders conditioning and the total-variation distance
are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's relations included. No observational value, no fitted number and no
framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight: `RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_..._2026-09-03.md`
(open PR #7876 -- the same cube and encoding, its Models A and B, its `T2` boundary at `p = 1`, and the `tau`/`H_R` interface this note's model closes by fiat);
`DETERMINANTAL_RECORD_STATISTICS_ON_THE_HALF_FILLED_SEA_..._2026-09-02.md` (PR #7883 -- the sea's Born statistics, the same `eta_ks`);
`EMERGENT_DICTIONARY_SELECTION_RULE_ZEROS_THREE_DIMENSIONS_..._2026-09-02.md` (PR #7842 -- the selection-rule zeros from the dictionary side);
`RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_..._2026-09-02.md` (PR #7858 -- forcing on the empty vacuum, whose `T2` this note's `T2` is the half-filled analogue of);
and `MINIMAL_AXIOMS_2026-06-29.md`, from which the four axioms in "Setting" are quoted verbatim. This note cites no grade of any and consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." "No site is privileged. Sites are distinguished by the supplied lattice structure alone." The lattice is physical;
the cube below is a finite open subgraph of it, drawn as a graph, so "edge site" and "corner" have their graph meanings. **Qubit / Site Possibility**: "Each site has a domain of local
possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`." "No possibility is privileged. Possibilities are distinguished by the supplied algebraic
structure alone."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the
probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Two reading notes, interpretive and non-governing, are the hinge
of this note and are quoted with it. (2): "Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site; **it does not
supply the formation site, probability, or rate.**" (3): "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on
finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may have zero singleton measure; Record locks a supported realization."

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent."
"Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded clause is used anywhere.
The **record ontology** is used as declared: a record at an edge site **registers** a value there; it does not report one the site already carried. Reading note (3) is what makes `T3`
a real cost: "admissible" is the *support* of the distribution, so a tick giving every pattern nonzero odds has made every pattern admissible. **The stipulation under test** --
"Between records, the lattice settles into its lowest-energy arrangement" -- is a candidate wording, not axiom text, and is not called wrong anywhere below; `M_R` is one way of making
it definite, and what is reported is what `M_R` does and does not do.

## The stipulated tick model `M_R`, declared in full

Six choices, all made here, none derived. A lane proposing a different tick inherits the obligations of `T3`-`T6` and none of these choices.

1. **The state before any record** is the sea: the ground state of `H` in the code space (see "Definitions").
2. **Which site forms next.** The next unrecorded edge site in a **declared order**, a permutation of the `12` sites. Thirty-two are declared and written out in the runner -- the `12`
   cyclic shifts of the identity order, their `12` reverses, and `8` further orders listed explicitly -- and none is drawn at random.
3. **The value the forming record locks.** The Born odds of the current pre-record state in the `Z_e` record basis.
4. **Relaxation -- the panel's clause.** The pre-record state is then **replaced** by the ground state of `H` restricted to the subspace consistent with all records so far. Unitarity
   is given up at this step and the map is not linear in the state.
5. **The tie-break.** Where that ground space is degenerate the state becomes the **normalised projector** `Pi/deg` onto it, and the next record's odds are its diagonal. Degeneracy is
   not a corner case: it occurs at ticks `5`, `6`, `8`, `9` and `11` (`T5`).
6. **Permanence.** Records never change; the run continues until all `12` sites carry records, so each run ends on one of the `4096` record patterns.

**`M_R^N`**, the charge-superselected variant, is declared alongside: identical except that step 4 relaxes inside the conserved `N = 4` sector of the block. Two reference ticks are
computed against `M_R`: **`L`**, pure Lueders conditioning with no dynamics at all, which is PR #7876's `p = 1` boundary; and **`A`**, PR #7876's Model A, identical to `M_R` except
that step 4 is replaced by the unitary `exp(-i tau H_R)`, run at `tau = 0.5`.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is `P0`-`P7`. `P0` (declared here): the cube, the edge-site
qubits, the encoding, the staggered sector, the parity dictionary, and the six stipulated choices above. `P1` (`A`): the restriction identity and the sea. `P2` (`B`): the sea's own
record odds and its zeros. `P3` (`C`): support. `P4` (`D`): order dependence. `P5` (`E`): charge. `P6` (`F`): relaxation against conditioning. `P7` (`G`): the pointer-basis table.

## Definitions

The **cube** is the `2x2x2` cube graph, corner `s = 4a + 2b + c`, `8` corners, `12` edge sites, `6` faces. One qubit sits on each **edge site**, neighbours ordered by index:

```text
A_ij = X(edge ij) * prod Z(edges at i ordered before j) * prod Z(edges at j ordered before i),   A_ji = -A_ij,
B_v  = prod of the Z's on the edges incident to v,     S_f = the ordered product of the A's around a face f,
T_ij = (i/2) A_ij (B_i - B_j),     H = -t sum_e eta_e T_e,  t = 1,     star(v) = the edges incident to v.
```

`eta` are the **Kawamoto-Smit staggered link signs** `eta_x = 1`, `eta_y = (-1)^x`, `eta_z = (-1)^(x+y)`, the same `eta_ks` as PR #7883; their product round every one of the six faces
is `-1`, the all-minus (**pi-flux**) sector. The **code space** is all six `S_f = +1`, of dimension `2^12/2^5 = 128`; because `prod_v B_v = I` it *is* the even-`N` space, and the
**sea** is the ground state of `H` there. A **record** at an edge site registers a `Z`-value, so a finished set of records is a vector in `F2^12`, one of `4096` **patterns**; the
**parity dictionary** is `n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2`, `N = sum_v n_v` and the **readable charge** is `Q = N - 4`. A **record block** `S(R,w) = {z : z|_R = w}` is
the subspace consistent with the records `w` on `R`; `H_R` is `H` restricted to it. The **odds at a site** are the probability that a record forming there locks `1`, given the records
present. `TV` is total variation, `(1/2) L1`.

## Theorem 1 -- the restriction identity, and why `M_R` is memoryless

**Conclusion.** `[exact]` Every one of the `12` hop terms has Pauli `X`-part exactly one edge qubit. Hence for every record set `R`, `P_S H P_S` is the sum of the hop terms on the
sites carrying **no** record: "`H` restricted to the records" and PR #7876's `H_R` are **the same operator**, not two conventions. So the relaxed state of step 4 depends on `(R, w)`
and nothing else, and `M_R` is **memoryless**. `[numerical, 1e-11]` The setting: `R0`-`R4` hold pair by pair, the face group carries no `-I`, `k = 5`, the code dimension is `128`, the
flux is `-1` on all six faces, the code space is `H`-invariant to `3e-17`, and the sea has `E = -6.928203230276 = -4 sqrt 3`, is non-degenerate, has gap `3.464101615138 = 2 sqrt 3`
and is sharp `N = 4` (Born mass off `N = 4`: `2e-31`).

**Proof.** `T_ij = (i/2) A_ij (B_i - B_j)` and `B_i`, `B_j` are pure `Z`, so both Pauli words `A_ij B_i` and `A_ij B_j` carry the `X`-part of `A_ij`, the single edge qubit `ij`; the
runner asserts this pair by pair. A term whose `X`-part touches a recorded site carries `S(R,w)` off itself and is killed by `P_S ... P_S`; a term whose `X`-part is unrecorded
preserves it. The relations, the group and the code dimension are the complete symplectic computation with `Z4` phases; the sea is one `128 x 128` diagonalisation.

**Reading, not theorem.** This is the one thing the candidate wording buys outright, and it is worth having: with it, nothing at all is left to declare between one record and the
next. The state is fixed by the records.

## Theorem 2 -- the sea's own record odds are flat, and its zeros

**Conclusion.** `[numerical, 1e-12]` On the sea, every one of the `24 + 264 + 1760 = 2048` record blocks with `k <= 3` carries weight exactly `2^-k` (to `4e-15`): the odds at a
forming record are `1/2` and **nothing is forced up to three records** -- the half-filled-sea analogue of PR #7858's `T2`. `[exact, 1e-12 zero read]` At `p = 1`, where every site registers before
anything else happens, the finished set is the sea's Born diagonal: support `1984 = 62 x 32`, and `2112` zeros splitting as `1856` **charge zeros** (every pattern with `N != 4`) plus
`256 = 8 x 32` **cancellation zeros**. The `8` corner-occupation patterns carrying the cancellation zeros are **exactly the `8` closed corner stars** `{v} u N(v)`, one per corner --
for example `{0,1,2,4}` and its complement `{3,5,6,7}`.

**Proof.** The block weights are sums of `|sea|^2` over coordinate subsets. The zero census is read off the Born diagonal at `1e-12` and then handled combinatorially: the `N != 4`
count is `4096 - 2240 = 1856` by the parity dictionary, the remaining zero labels group by corner-occupation pattern into `8` patterns of `32`, and those `8` are compared as sets
against the `8` closed corner stars built from the cube's adjacency -- an equality of two `8`-element sets of `F2^8` vectors, with no tolerance in it.

**Reading, not theorem.** This is the target any tick has to hit: before any record the lattice favours neither value at any site, and it never registers eight of the corner patterns
at all -- the forbidden patterns PR #7842 and PR #7883 exhibit from the dictionary side.

## Theorem 3 -- under `M_R` every pattern becomes admissible

**Conclusion.** `[numerical, 1e-12]` Under `M_R` at the identity order all `4096` patterns carry strictly positive odds (smallest `1.6e-05`), so **not one of the sea's `2112` zeros
survives**; the same holds at all `32` declared orders -- support `4096`, `0` zeros kept -- the charge zeros included, although `N` is conserved by `H` and commutes with every record
projection. `TV(M_R, sea Born) = 0.445486111111 = 1283/2880` at the identity order. PR #7876's Model A at `tau = 0.5` sits **closer**, `TV = 0.324925160534`, on support `2240`,
keeping all `1856` charge zeros and losing the same `256` cancellation zeros.

**Proof.** Each order's distribution is the exact product over the whole `4096`-leaf tree: at every node the block ground space is diagonalised once, the branch odds are the masses of
the relaxed diagonal on the two values, and the leaf weights are accumulated; nothing is sampled and no branch is pruned. The relaxed state uses the real skew form of `H_R`: the block
matrix is purely imaginary, so its square is `-M M^T`, the ground level is `-sqrt(lambda_max)`, and the ground projector's diagonal is half that of the real spectral projector at
`lambda_max`.

**Reading, not theorem.** By reading note (3), "admissible" is the support of the distribution; under this tick the support is everything, so the patterns the sea never registered are
now registered, with odds of one in sixty thousand or better.

## Theorem 4 -- the odds depend on the order in which the sites record

**Conclusion.** `[numerical, 1e-12]` `TV(identity order, reverse order) = 0.333333333333 = 1/3`, for the same twelve sites and tick. Over the `32` declared orders -- the `12` cyclic
shifts, their `12` reverses, and `8` further orders written out in the runner, **no seed anywhere** -- the maximal pairwise `TV` is `0.727031250000` and the minimal `0.113194444444`,
and `TV` to the sea ranges `0.445486111111` .. `0.569444444444`. The maximum is a **lower bound** on the spread over all `12!` orders, not the spread itself. `[numerical, 1e-14]` The
sea's own Born rule, by contrast, is order-independent: pure Lueders conditioning reproduces its Born diagonal to `6e-15`, identity and reverse agreeing to `6e-15`.

**Proof.** Thirty-two whole trees as in `T3`, then `496` pairwise `L1` sums; the Lueders tree is the same enumeration with the relaxation step removed. The declared order set is a
literal in the runner, asserted to be `32` distinct permutations of the `12` sites.

**Reading, not theorem.** The finished set is the same twelve records either way, and which order they formed in should not change how likely it was. Under this tick it does: by a
third between one order and its reverse, and by more than seven tenths between the two furthest orders tried.

## Theorem 5 -- half filling survives on average; the readable charge does not stay sharp

**Conclusion.** `[numerical, 1e-12]` `<Q> = 0` and `<N> = 4` at every one of the `32` declared orders (`max |<Q>| = 2e-16`, `max |<N> - 4| = 1e-14`), so `M_R` keeps half filling on
average. But `Q` is no longer sharp: at the identity order the law over `Q = -4, -2, 0, 2, 4` is `(1/384, 1/8, 143/192, 1/8, 1/384)` and `var Q = 1.083333333333 = 13/12`; over the
declared orders `P(Q = 0)` ranges `0.614583333333` .. `0.881319444444` and `var Q` ranges `0.488888888889` .. `1.666666666667`, so the charge law is itself order-dependent. The spread
sits on the tie-break: of the `8190` nodes of the identity-order tree, the `1456` whose relaxed state is **not** `N`-sharp are **exactly** the `1456` carrying a degenerate ground
space, at ticks `5`, `6`, `8`, `9` and `11`; at every tick the weight-averaged `<N>` is still `4` to `7e-15`. The variant `M_R^N` restores `P(Q = 0) = 1` and all `1856` charge zeros
on support `2240`, but still loses all `256` cancellation zeros, as Model A does.

**Proof.** The charge law is read off the `T3` trees against the parity dictionary and compared with the stated rationals at `1e-12`. The node census records, at every node, the
block's ground-space degeneracy and the `N` values its relaxed diagonal is supported on, and asserts the two coincide node by node. At tick `11` the degenerate blocks are exactly
those where `H_R` vanishes -- the last free hop has zero amplitude, its two corner endpoints carrying equal occupancy -- and the block's two states then differ in `N` by `2`; at ticks
`5`, `6`, `8` and `9` the degenerate ground space has `E_0 < 0` and still spans two `N` sectors.

**Reading, not theorem.** The tie-break is doing real work, and it is a declared choice, not a technicality: where the lattice has more than one lowest-energy arrangement this tick
shares the weight evenly among them, and there the arrangement carries no one definite charge. Superselecting charge fixes that and not the rest.

## Theorem 6 -- relaxation is not the sea held to the records

**Conclusion.** `[numerical, 1e-12]` Relaxation parts from conditioning at the **first** record: the relaxed state and the Lueders-conditioned sea overlap by `0.962606705806` at all
`24` (site, value) blocks, identically (spread `7e-15`), so `P_S|sea>` is not a ground state of `H_R` even after one record. By `k = 3` the overlap has fallen to `0.448473881026` in
the worst of the `1760` blocks, with mean `0.773546569701`, while in `64` of them the conditioned sea **is** the block ground state. The conditioned column has the closed form `<H_R>
= -(12 - k) / sqrt 3` at `k = 0..12` (to `4e-14`): conditioning alone costs `sqrt 3 / 3` per record, whatever the record says. `[numerical, 1e-9]` Relaxation lowers the energy and
never raises it: `E_0(R,w) <= <sea_S|H_R|sea_S>` at all `2048` blocks with `k <= 3`, `0` violations. But the gain is not where a settling picture would put it: the tree-average drop
peaks at `k = 9` (`0.401011505139`), vanishes at `k = 0` and `k = 12` where the block is one-dimensional, and is `0` to `1e-14` at `k = 3`.

**Proof.** Each of the `2048` blocks is diagonalised once; the overlap with the conditioned sea uses the same real skew form as `T3`, the ground projector being `(1/2)(P - (i/mu) M
P)`. The conditioned column needs no diagonalisation -- `<H_R>` is one quadratic form per node -- and its closed form has an exact reason: each hop term is block-diagonal in the
record bits of any `R` not containing its site, so averaging over the Lueders values leaves `<sea|T_e|sea>` unchanged, and the staggered sector's site symmetry gives `<sea|T_e|sea> =
E_sea/12 = -sqrt 3 / 3` at every edge. The `0` violations are the variational principle, checked block by block.

**Reading, not theorem.** "Settling to the lowest arrangement" and "the sea, held to the records so far" are not the same state, and they part company at the first record, by the same
amount at every site and value. The energy bookkeeping is honest -- settling never costs energy -- but that is all it buys.

## Theorem 7 -- which description a record can take is already settled

**Conclusion.** `[exact]` `Z_e` commutes with all `8` corner parities `B_v` at all `12` edge sites, while `X_e` and `Y_e` each anticommute with exactly the two endpoint parities of
their site. So the **corner-parity dictionary singles out the record basis**: `Z_e` is the unique one-site description it cannot disturb. The **face dictionary singles out none**:
`Z_e` anticommutes with exactly the two faces through `e` at all `12` sites, and no one-site basis at any site commutes with the corner dictionary and the face dictionary at once.

**Proof.** Three one-site Pauli words per site against `8 + 6` stabilizer words in the symplectic representation, the face incidences compared against the cube's own face list; all
integer arithmetic. (The `X_e`/`Y_e` counts against the faces are not uniform across sites and are an artefact of the declared `Z`-tail ordering; they are not used, `X_e` and `Y_e`
being already excluded by the corner column.)

**Reading, not theorem.** Whatever the tick turns out to be, it does not have to choose which description a record locks: the corner parities have already chosen, and they choose the
same one at every site.

## Corollary -- what this says about a relaxation tick

Within the setting declared above, on the cube in the staggered sector at half filling, and for the stipulated model `M_R` alone:

1. **The candidate tick is well posed and memoryless.** By `T1` the relaxed state is a function of the records alone, so `M_R` does close PR #7876's `tau`/`H_R` interface -- by fiat,
   since there is nothing left to declare between one record and the next except which site records next. It also has an honest variational content (`T6`): settling never raises the
   energy, at any of the `2048` blocks checked.
2. **It is not the sea's registration.** Every pattern becomes admissible (`T3`), the selection-rule zeros of `T2` are lost -- the `256` cancellation zeros and, through the tie-break,
   even the `1856` charge zeros -- the odds depend on the order the sites record in (`T4`), and the readable charge is no longer sharp (`T5`), though `<Q> = 0` and half filling
   survive on average.
3. **Among the ticks examined so far, only registration of all sites at once reproduces the sea's odds.** That is `p = 1`, the `L` reference of `T2`, and it is a limit rather than a
   tick: nothing happens between records because there is no between. `M_R` sits further from the sea than a plain unitary gap at `tau = 0.5` does (`T3`).
4. **What any tick must satisfy is now sharper.** It has to keep the sea's flat odds (`T2`) and its zeros, and by `T7` the corner-parity dictionary already fixes the basis a record
   forms in. So the open content of a tick is the **formation rule** -- the rate and the odds -- and not the basis.

## Reading, not theorem -- the whole thing in plain words

Suppose that between one record and the next the lattice always drops to its lowest-energy arrangement given the records so far. That rule is at least definite: the state is fixed by
the records alone. But it does not give back the sea's own record statistics. Every pattern becomes possible, the forbidden patterns that matched known selection rules are lost, and
the answer depends on the order in which sites record. Whatever the framework's tick is, it has to keep the sea's odds, and this one does not. Which values a record can take, on the
other hand, is already settled by the corner parities: the record basis is the one they cannot disturb.

## Interfaces named for other lanes, not settled here

- **The formation rate.** How often a record forms, and where, is outside this note; reading note (2) says the axioms supply neither, and `M_R` stipulates an order rather than
  deriving one. Corollary item 4 is the obligation a formation rule has to answer, and none is supplied here.
- **A Lindbladian stationary state.** The panel's referee lens -- a tick written as a dissipative generator whose stationary state is the sea, rather than as a replacement map -- is
  named and not computed; `M_R` is not linear in the state and is not of that form.
- **Partial relaxation.** Ticks relaxing only partly, running a finite time towards the conditioned ground state rather than arriving, interpolate between PR #7876's Model A and
  `M_R`; only the two ends are computed here.
- **Larger regions.** The `3x3x3` cube, periodic boundaries, other fillings and other flux sectors are outside this note; the sea's degeneracy and the corner-star census both depend
  on the cluster.

## Remaining live routes

1. Whether the order spread of `T4` grows or saturates on larger clusters. The `0.727031250000` here is a maximum over `32` declared orders, and the true maximum over all `12!` orders
   is not computed.
2. Whether any tie-break other than `Pi/deg` and the `N`-superselected one makes `T5`'s charge spread vanish without a superselection rule added by hand; `M_R^N` adds one, and nothing
   here says whether something else does it.

## Executable claim block

The canonical machine-bound restatement of the seven theorem conclusions.

```text
setting: qubits on the 12 EDGE sites of the 2x2x2 cube graph (8 corners, 6 faces); ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading notes (2) and (3)
encoding: A_ij = X(edge ij) * Z's ordered before it at both endpoints; A_ji = -A_ij; B_v the Z's incident to v; S_f the ordered four-A face loop; T_ij = (i/2) A_ij (B_i - B_j)
law: eta = Kawamoto-Smit staggered signs (eta_x = 1, eta_y = (-1)^x, eta_z = (-1)^(x+y)), flux -1 on all six faces; H = -sum_e eta_e T_e, t = 1; code space all six S_f = +1, dim 128 = the even-N space; the sea = its ground state, E = -4 sqrt 3, non-degenerate, gap 2 sqrt 3, sharp N = 4
dictionary: n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2; N = sum_v n_v; readable charge Q = N - 4
tick_model: STIPULATED, six declared choices -- (i) start from the sea; (ii) the next unrecorded site in a DECLARED order forms; (iii) it locks its value with the Born odds of the current pre-record state; (iv) the state is then REPLACED by the ground state of H restricted to the record-consistent subspace; (v) Pi/deg where that ground space is degenerate; (vi) records permanent, run to 12. Variant M_R^N relaxes inside N = 4. References: L = pure Lueders (the p = 1 boundary), A = PR #7876 Model A at tau = 0.5. No seed anywhere; every order written out in the runner
T1_restriction [exact]: every hop term has Pauli X-part exactly one edge qubit, so P_S H P_S = sum over unrecorded e of T_e = PR #7876's H_R; hence M_R is memoryless, its state a function of the record set alone. R0-R4 pair by pair, no -I in the face group, k = 5, code dim 2^12/2^5 = 128, flux -1 on all six faces; [numerical, 1e-11] code space H-invariant to 3e-17, E_sea = -6.928203230276 = -4 sqrt 3, non-degenerate, gap 3.464101615138 = 2 sqrt 3, Born mass off N = 4 is 2e-31
T2_sea_odds [numerical, 1e-12]: all 24 + 264 + 1760 = 2048 record blocks with k <= 3 carry sea weight 2^-k to 4e-15 -- odds 1/2, nothing forced up to three records; [exact, 1e-12 zero read] at p = 1 the support is 1984 = 62 x 32 and the 2112 zeros are 1856 charge zeros (N != 4) + 256 = 8 x 32 cancellation zeros whose 8 corner patterns are EXACTLY the 8 closed corner stars {v} u N(v)
T3_support [numerical, 1e-12]: under M_R support 4096 and 0 of the 2112 zeros kept, at the identity order (smallest pattern probability 1.6e-05) and at all 32 declared orders; TV(M_R identity, sea Born) = 0.445486111111 = 1283/2880; Model A at tau = 0.5 is closer, TV = 0.324925160534, on support 2240, keeping 1856 charge zeros and 0 of the 256 cancellation zeros
T4_order [numerical, 1e-12]: TV(identity, reverse) = 0.333333333333 = 1/3; over the 32 declared orders max pairwise TV = 0.727031250000, min 0.113194444444, TV to the sea 0.445486111111 .. 0.569444444444, the maximum a LOWER BOUND on the spread over all 12! orders; [numerical, 1e-14] pure Lueders reproduces the sea's Born diagonal to 6e-15 and is order-independent to 6e-15
T5_charge [numerical, 1e-12]: max |<Q>| = 2e-16 and max |<N> - 4| = 1e-14 over the 32 orders; identity-order law over Q = -4,-2,0,2,4 is (1/384, 1/8, 143/192, 1/8, 1/384), var Q = 1.083333333333 = 13/12; over the orders P(Q = 0) in 0.614583333333 .. 0.881319444444 and var Q in 0.488888888889 .. 1.666666666667; of the 8190 identity-tree nodes the 1456 whose relaxed state is not N-sharp are EXACTLY the 1456 with a degenerate ground space, at ticks 5, 6, 8, 9, 11, and the weight-averaged <N> is 4 at every tick to 7e-15; M_R^N gives P(Q = 0) = 1, support 2240, all 1856 charge zeros, 0 of the 256 cancellation zeros
T6_relaxation_vs_conditioning [numerical, 1e-12]: overlap with the Lueders-conditioned sea is 0.962606705806 at all 24 one-record blocks (spread 7e-15); at k = 3, min 0.448473881026, mean 0.773546569701, 64 of 1760 blocks at 1; <H_R> on the conditioned sea = -(12 - k)/sqrt 3 at k = 0..12 to 4e-14; [numerical, 1e-9] E_0(R,w) <= <sea_S|H_R|sea_S> at all 2048 blocks, 0 violations; tree-average drop peaks at k = 9 (0.401011505139), vanishes at k = 0 and k = 12, and is 0 to 1e-14 at k = 3
T7_pointer [exact]: Z_e commutes with all 8 corner parities at all 12 sites; X_e and Y_e each anticommute with exactly the two endpoint parities; Z_e anticommutes with exactly the two faces through its site at all 12 sites; no one-site basis commutes with the corner and face dictionaries at once
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=26 FAIL=0
```

## Proof boundary

Every statement above is proved on **one finite cluster**, the `2x2x2` cube graph, in **one flux sector** (all-minus, the Kawamoto-Smit staggered signs) at **one filling** (the
half-filled sea, `N = 4`). Nothing is claimed for larger clusters, periodic boundaries, infinite lattices, other sectors, other fillings, or any law family other than the one in
"Definitions". The law is **designed**, not derived: the encoding is chosen so that the Majorana relations `R0`-`R4` hold, the face constraints make that consistent, and the parity
dictionary is one readout map among many, with no uniqueness claimed for either.

**The tick model is stipulated in full and derived from nothing.** All six choices -- the starting state, the declared order, Born odds at formation, replacement by the restricted
ground state, the `Pi/deg` tie-break, and permanence -- are declared here, not taken from any axiom. Reading note (2) is explicit that the axioms supply no formation site, probability
or rate, and they supply no relaxation clause either; this note supplies none and declares one instead. **Nothing here says what the framework's tick is**, and nothing here forecloses
any tick. This is an obstruction for **one stipulated tick model**: a different formation rule, a different tie-break, a partial relaxation, or a dissipative generator with the sea as
its stationary state are all untouched above, and several are named as interfaces. The panel's candidate sentence is a candidate wording and is not called wrong here; what is reported
is what `M_R`, one way of making it definite, does and does not do.

The order-dependence figure of `T4` is a maximum over **`32` declared orders**, written out in the runner, and is a **lower bound** on the spread over all `12!` orders, labelled so
everywhere it appears. The `Pi/deg` tie-break is a further declared choice, and `M_R^N` is reported alongside because it changes the charge conclusion. The `p`-variant of PR
#7876 is touched only at its `p = 1` boundary. Every line not tagged `[exact]` is a **deterministic double-precision evaluation** of an exactly specified quantity at the stated
threshold: the tick trees are enumerated whole, `4096` leaves and nothing sampled, but each node's relaxed state comes from a diagonalisation, against which no exact rational value
stands. There is **no seed anywhere** in this note or its runner and no Monte Carlo section. No absolute unit appears anywhere, no axiom text is amended, extended, reworded or
reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

An honest auditor should come away with a declared tick model and its consequences, not a claim about what the framework's tick is; a two-sided result -- well posed and memoryless,
and not the sea's record statistics -- on one named finite cluster, sector and filling; the stipulation declared as stipulated in the front matter, the setting, its own section, the
claim block and the proof boundary alike; the panel's candidate sentence quoted as a candidate wording and nowhere called wrong; the order-dependence maximum labelled a lower bound
over a declared finite set of orders; and the corollary written as an obligation, not a foreclosure.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority" pointers are plain
text carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair at `PASS=26 FAIL=0`, runtime under the declared `120` seconds, a current
zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a separate lane.
