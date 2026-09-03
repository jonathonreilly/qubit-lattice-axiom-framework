---
claim_id: joint_formation_corner_record_set_keeps_sea_zeros_unitary_tick
claim_type: bounded_theorem
claim_scope: "On the 2x2x2 cube graph (8 corners, 12 edge sites, 6 faces) with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, in the staggered (pi-flux) Kawamoto-Smit sector H = -sum_e eta_e T_e at half filling, whose 128-dimensional code space is the even-N space and whose non-degenerate ground state -- the sea -- has E = -4 sqrt 3, gap 2 sqrt 3 and sharp N = 4, with Born support 1984 and 2112 zeros = 1856 charge zeros + 256 cancellation zeros on the 8 closed corner stars: under FIVE STIPULATED UNITS OF RECORD FORMATION, declared here and derived from nothing -- U1 a single edge site, U2 the three edges at one corner (a corner's own record set star(v)), U3 the four edges of a face, U4 the closed corner star of v (the nine edges incident to {v} u N(v), = E \\ star(7-v)), U5 all twelve at once -- in which the not-yet-recorded sites of the next unit in a DECLARED order register JOINTLY with the odds of the current pre-record object, and between formation events one of three DECLARED rules runs: (a) M_R, relaxation to the restricted ground state with the Pi/deg tie-break (PR #7895's tick), (b) A, the unitary exp(-i tau H_R) at tau = 0.5 (PR #7876's Model A), (c) L, nothing. (T1) Rule (c) is order-independent and IS the sea for all 17 declared schedules -- support 1984, TV <= 7.4e-16, max pairwise TV <= 4e-16 -- and U1 reproduces PR #7895 exactly (2240 support, 1856 charge zeros, 0 of 256 cancellation zeros, TV 0.324925160534 under rule (b)); so every deviation below is caused by the between-event rule and not by the joint conditioning. (T2) Under rule (b) joint formation on a corner's record set keeps ALL 256 cancellation zeros at 3 of the 4 declared U2 orders and at 4 of the declared 40-permutation lexicographic sweep, U4 antipodal keeps all 256, and two schedules -- U2 evenfirst (the four disjoint corner record sets) and U4 antipodal -- reproduce the sea EXACTLY, TV 1.11e-15 and 7.02e-16, at every tau in {0.1, 0.5, 1.234567, 2.0}; site-wise formation and every face order keep 0 of the 256. (T3) The mechanism: after a corner's record set forms jointly the Born-conditioned sea lies in the restricted ground space (G = 1) and is an exact eigenvector of H_R at 8/8 outcomes with TV(|psi|^2, Pi/deg) = 0, and after a closed corner star at 448/448 with deg 2, while after a single edge (0/2, G = 0.962606706) and after a FACE (0/16, G = 0.890431430) it is not; along both exact-sea schedules the eigenvector property holds at every node a between-event step follows. (T4) Under rule (a) no unit short of U5 keeps more than 64 of the 256 cancellation zeros in any declared order or in the sweep; the 64 surviving under U4 are exactly the first-formed star's coset and its antipode's; under U2 evenfirst they are cosets 1 and 6, NOT the first-formed corner0's coset 0; P(Q = 0) never reaches 1 below U5 (best 0.841145833 at U3, U4 0.666666667 .. 0.750000000). (T5) Order dependence shrinks with unit size and never vanishes short of U5 (max pairwise TV U1 0.602777777778 (a) / 0.619386368116 (b), U4 0.250000000000 / 0.076616282355) and is not monotone -- the 4-site face is more order-dependent than the 3-site corner record set under both rules; formation events per unit type average 12, 6.00, 4.50, 2.75, 1. OPEN and not claimed: why U2 identity and reverse keep all 256 under rule (b) although the propagated state visits 192 cancellation-coset labels at intermediate nodes. No seeds anywhere: every distribution is the exact product over the whole formation tree and every order is written out in the runner. This note stipulates a unit of record formation and computes with it; nothing is derived from any axiom, no formation clause is supplied, no axiom is amended, no status is set, and no claim is made about what the framework's tick is."
upstream_dependencies: []
runner: scripts/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.py
---

# Joint formation on a corner's record set keeps the sea's zeros under the unitary tick

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.py`](../scripts/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.txt`](../logs/runner-cache/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

`A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_..._2026-09-03.md` (open PR #7895) lets **one edge site at a time** register, and finds that the sea's own
forbidden patterns do not survive. On 2026-09-03 the owner put a different reading of the same clause: **"the whole neighbourhood generally has to move together because it is its own
shared condition"**. Records are permanent, so at the level of formation that sentence is a statement about the **unit** in which records form: a formation event registers a whole
neighbourhood's worth of records **together**, as one event. This note takes that as a stipulation under test. It declares five units of formation on the same cube in the same sector, runs them against the same three between-event rules, and reports what follows. The answer turns on the **shape** of the unit, not its size.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on one named cluster -- the 4096-dimensional record space of the 2x2x2 cube in the staggered sector, whose 128-dimensional code space is the even-N space -- for five stipulated units of record formation and three stipulated between-event rules. The unit and order combinatorics of B1-B2 are exact integer and F2 statements; the sea's zero census is exact F2 combinatorics on a zero set identified from the Born diagonal at 1e-12. The formation trees are enumerated whole and nothing is sampled, but each node's relaxed state or evolution comes from a diagonalisation, so those lines are deterministic double-precision evaluations of exactly specified quantities and are tagged [numerical] with their thresholds. There is no seed anywhere in the runner and no Monte Carlo section."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-sector theorem, and route to the vacuum panel the sharpened question: the unit of record formation is a free choice the axioms do not supply, and on this cluster one shape of unit -- a corner's own record set -- keeps the sea's registration under a unitary between-event rule while relaxation does not, so what a formation rule owes is a unit and a between-event rule together, not either alone."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below plus the open item, exactly the runner's check groups `A`-`G`: the setting and the sea's zeros (`A`); the stipulated units and
orders (`B`); `T1` (`C`) the control; `T2` (`D`) the unitary tick; `T3` (`E1`-`E3`) the mechanism, with the open item recorded at `E4`; `T4` (`F`) relaxation; `T5` (`G`) order
dependence. Groups `A1`, `A2`, `B1` and `B2` are **exact**: symplectic Pauli algebra with phases mod `4`, and integer combinatorics on the cube's own adjacency. `A4` is exact `F2`
combinatorics on a zero set identified from the Born diagonal at `1e-12`. The rest are **deterministic double-precision evaluations** of exactly specified quantities at the stated
thresholds. Nothing is sampled: every distribution is the exact product over the whole formation tree, every order is written out in the runner, and there is **no seed anywhere** and no Monte Carlo section.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggered link signs, Lueders conditioning and the total-variation distance
are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's relations included. No observational value, no fitted number and no
framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight: `A_RELAXATION_TICK_IS_WELL_POSED_..._2026-09-03.md` (open PR #7895 -- the site-wise
result this note extends, and the source of the `M_R` rule, the `Pi/deg` tie-break, and the zero census reproduced at `A4`); `RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_..._2026-09-03.md`
(open PR #7876 -- Model A and `H_R`); `DETERMINANTAL_RECORD_STATISTICS_ON_THE_HALF_FILLED_SEA_..._2026-09-02.md` (PR #7883 -- the sea's Born statistics, the same `eta_ks`);
`EMERGENT_DICTIONARY_SELECTION_RULE_ZEROS_THREE_DIMENSIONS_..._2026-09-02.md` (PR #7842 -- the selection-rule zeros from the dictionary side);
`SUPPORT_CONDITIONS_CONFINE_RECORD_GROUPS_..._2026-09-03.md` (PR #7891 -- the owner's neighbourhood mechanism);
`RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_..._2026-09-02.md` (PR #7858 -- the same cube and encoding); and `MINIMAL_AXIOMS_2026-06-29.md`, from which the axioms in
"Setting" are quoted verbatim. This note cites no grade of any and consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." "No site is privileged." The lattice is physical; the cube below is a finite open subgraph of it, drawn as a graph,
so "edge site" and "corner" have their graph meanings. **Qubit / Site Possibility**: "Each site has a domain of local possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the
probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Two reading notes, interpretive and non-governing, are the hinge of
this note and are quoted with it. (2): "Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site; **it does not
supply the formation site, probability, or rate.**" (3): "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may have zero singleton measure; Record locks a supported realization."

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent."
"Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded clause is used anywhere.
The **record ontology** is used as declared: a record at an edge site **registers** a value there; it does not report one the site already carried. Reading note (2) is what makes this
note's subject a free choice: the axioms supply no formation site and no rate, so **the unit in which records form is not given** -- this note stipulates five of them and reports what each does. Reading note (3) is what makes a lost zero a real cost: "admissible" is the *support* of the odds, so a rule giving a pattern nonzero odds has made that pattern admissible.

**Reading, not theorem.** Records are permanent, so "the whole neighbourhood together" cannot be about anything happening to records already present. Read at the level of formation it
says: the records of one neighbourhood **form together**, in one event, because the neighbourhood is one shared condition. That is the reading tested below, and it is a stipulation.

## The stipulated formation model, declared in full

Seven choices, all made here, none derived. A lane proposing a different unit or a different between-event rule inherits the obligations of `T1`-`T5` and none of these choices.

1. **The object before any record** is the sea: the ground state of `H` in the code space (see "Definitions"). 2. **The unit of formation.** Five **unit types** are declared, each a set of edge sites whose records form together as one event:

   | type | what it is | count | size |
   |---|---|---|---|
   | `U1` | a single edge site | `12` | `1` |
   | `U2` | the three edges at one corner `v` -- **a corner's own record set** `star(v)` | `8` | `3` |
   | `U3` | the four edges of one face | `6` | `4` |
   | `U4` | the **closed corner star** of `v`: every edge incident to `{v} u N(v)`, which on this cube is `E \ star(7 - v)` | `8` | `9` |
   | `U5` | all twelve edge sites | `1` | `12` |

3. **Which unit forms next.** The next unit in a **declared order**, a permutation of that type's unit list. **Sixteen** are declared for `U1`-`U4`, four per type, written out in the
   runner, plus `U5`'s single order; a further declared **lexicographic sweep** of the first `40` permutations of the unit list is run for `U2`, `U3` and `U4`. None is drawn at random.
4. **What forms.** Only the **not-yet-recorded** sites of that unit, and they form **together**: one event registers all `m` of them, with the odds of the current pre-record object on
   the `2^m` joint outcome patterns.
5. **Between formation events**, one of three **declared rules** runs:
   * **(a) `M_R`** -- the object is replaced by the ground state of `H` restricted to the record-consistent subspace, with the normalised projector `Pi/deg` where that ground space is
     degenerate. This is PR #7895's tick, one way of making the vacuum panel's candidate wording -- "Between records, the lattice settles into its lowest-energy arrangement" --
     definite. That wording is a candidate, not axiom text, and is not called wrong here; what is reported is what `M_R` does.
   * **(b) `A`** -- the unitary `exp(-i tau H_R)`, `tau = 0.5`, PR #7876's Model A: the lattice's law simply runs on.
   * **(c) `L`** -- nothing at all, pure sequential Born. This is the control.
6. **Conventions.** A unit with no unrecorded sites is **skipped**: no formation event and no between-event rule. The between-event rule after the **last** event is not applied; it
   cannot change the final odds.
7. **Permanence.** Records never change; the run continues until all `12` sites carry records, so each run ends on one of the `4096` record patterns.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is `P0`-`P5`. `P0` (declared here): the cube, the edge-site
qubits, the encoding, the staggered sector, the parity dictionary, and the seven stipulated choices above, together with the setting and zero census of `A` and the unit/order
combinatorics of `B`. `P1` (`C`): the control. `P2` (`D`): the unitary tick. `P3` (`E`): the mechanism, and the open item. `P4` (`F`): relaxation. `P5` (`G`): order dependence.

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
**parity dictionary** is `n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2`, `N = sum_v n_v` and the **readable charge** is `Q = N - 4`. `H_R` is `H` restricted to the subspace
consistent with the records so far, which by PR #7895's restriction identity is the sum of the hop terms on the **unrecorded** sites. `TV` is total variation, `(1/2) L1`. A
**cancellation coset** is one of the eight `32`-label sets of the sea's non-charge zeros, indexed by the closed corner star carrying it.

## The setting and the sea's zeros, reproduced

`[exact]` The superfast relations `R0`-`R4` hold pair by pair, the face group carries no `-I`, `k = 5`, the code dimension is `128`, the flux is `-1` on all six faces, and every hop
term has Pauli `X`-part exactly one edge qubit, so `P_S H P_S` is the sum of the hops on unrecorded sites. `[numerical, 1e-11]` The code space is `H`-invariant to `2.8e-17`; the sea
has `E = -6.928203230276 = -4 sqrt 3`, is non-degenerate, has gap `3.464101615138 = 2 sqrt 3` and is sharp `N = 4` (mass off `N = 4`: `2.0e-31`). `[exact, 1e-12 zero read]` The
**target** every rule below is checked against is the sea's own registration: support `1984 = 62 x 32`, and `2112` zeros `= 1856` **charge zeros** (`N != 4`) `+ 256` **cancellation
zeros**, whose eight corner-occupation patterns are **exactly** the eight closed corner stars `{v} u N(v)`, `32` labels each; the smallest nonzero sea probability is `2.17e-04`.
`[exact]` The five unit types have counts `12, 8, 6, 8, 1` and sizes `1, 3, 4, 9, 12`, and `cstar(v) = E \ star(7 - v)`: **a closed corner star's complement is the antipode's own
record set.** The sixteen declared orders plus `U5`'s cover all twelve sites, with formation events `U1 [12,12,12,12]`, `U2 [7,7,4,6]`, `U3 [4,4,5,5]`, `U4 [3,3,2,3]`, `U5 [1]` --
means `12`, `6.00`, `4.50`, `2.75`, `1`. `[numerical, 1e-12]` What **one unit's own joint odds** already forbid: `0` charge and `0` cancellation zeros at **every** `U1`, `U2` and `U3`
unit, while every `U4` closed star forbids `448` charge and `64` cancellation zeros, and `U5` forbids all `1856 + 256`.

## Theorem 1 -- the control: with nothing between events, the unit and the order do not matter

**Conclusion.** `[numerical, 1e-15]` Under rule (c) all `17` declared schedules give support `1984` and **are** the sea's registration: `TV` to the sea at most `7.4e-16`. Between the
four declared orders of each proper unit type the maximal pairwise `TV` is `4e-16` (`U1`), `4e-16` (`U2`), `2e-16` (`U3`), `8e-17` (`U4`). `[numerical, 1e-12]` And `U1` reproduces PR
#7895 exactly: under rule (b) at `tau = 0.5` its support is `2240`, all `1856` charge zeros are kept, `0` of the `256` cancellation zeros are, and `TV` to the sea is
`0.324925160534` at the identity order, at all four declared orders alike.

**Proof.** Seventeen whole trees under rule (c) and four more under rule (b), each the exact product over its own leaves with nothing sampled and no branch pruned above `1e-12`
relative. Joint conditioning in the `Z` basis commutes with itself, so the control's order independence is expected and is checked rather than assumed.

**Reading, not theorem.** This is the control the rest of the note needs: with the lattice's law switched off between events, forming records one at a time and forming them a whole
neighbourhood at a time give the same odds, and give the sea's odds. So every difference below is caused by what runs **between** formation events, not by the joint formation itself.

## Theorem 2 -- under the unitary tick, a corner's record set keeps the sea's forbidden patterns

**Conclusion.** `[numerical, 1e-12]` Under rule (b) at `tau = 0.5`, cancellation zeros kept over the four declared orders are `U1 [0,0,0,0]`, `U2 [256,256,256,0]`, `U3 [0,0,0,0]`,
`U4 [128,128,256,128]`, `U5 [256]`: **all `256` at three of the four corner orders, none at any face order**, with all `1856` charge zeros kept everywhere. In the declared
lexicographic sweep of the first `40` permutations, `4` of `40` `U2` orders keep all `256`, `U3` keeps `0` throughout and `U4` `128` throughout. Two schedules reproduce the sea
**exactly**: `U2 evenfirst` -- the four **disjoint** corner record sets `star(0), star(3), star(5), star(6)` -- at `TV = 1.11e-15`, and `U4 antipodal` -- `cstar(0)` then `star(7)` --
at `TV = 7.02e-16`, both on the sea's own support `1984`. Both do it at every `tau` tested, `0.1`, `0.5`, `1.234567`, `2.0`, while `U1 identity` and `U3 identity` keep `0` of the `256`
at every one of them.

**Proof.** Whole formation trees as in `T1`, one per (unit type, order, rule) and four more per schedule for the `tau` sweep; the zero census of each final distribution is read at
`1e-12` against the sea's zero set and split by cancellation coset. The `40`-permutation sweep is `itertools.permutations` on the sorted unit list, a literal enumeration with no seed.

**Reading, not theorem.** Letting the three records at one corner form together, with the lattice's law simply running on in between, keeps every one of the forbidden patterns that
site-wise formation loses -- and for the right sequence of corners the records come out exactly as the sea itself would register them, at any gap length. The four edges of a face are a
**larger** unit and keep none of them.

## Theorem 3 -- the mechanism: a jointly formed corner set leaves the sea at rest under what remains of the law

**Conclusion.** `[numerical, 1e-9]` After a corner's record set forms jointly, the Born-conditioned sea already lies in the restricted ground space (`G = <psi|Pi_0|psi> =
1.000000000`, `deg = 1`) and is an **exact eigenvector of `H_R`** at `8` of `8` outcomes, with `TV(|psi|^2, Pi/deg) = 0`: relaxation is the **identity** there and the unitary is a
global phase. The closed corner star has the same property at `448` of `448` outcomes (`G = 1.000000000`), but its ground space is `2`-fold degenerate, so the `Pi/deg` tie-break gives
a rank-`2` mixture (`F = 0.636894534`, `Fq = 0.500`). A single edge (`G = 0.962606706`, `0/2`) and a **face** (`G = 0.890431430`, `0/16`) are eigenvectors at no outcome at all, though
the face is the larger unit. `[numerical, 1e-9]` Along both exact-sea schedules the conditioned state is an `H_R` eigenvector at **every** node a between-event step follows --
eigen-weight `1.000/1.000/1.000` (`U2 evenfirst`) and `1.000` (`U4 antipodal`) -- against `0.000` at each of the first seven levels for `U1 identity` and `0.000/0.079/0.142` for
`U3 identity`.

**Proof.** For each first-unit outcome the conditioned sea is formed, `H_R psi` is computed directly from the block's real skew form `H = i M` without any diagonalisation, and
`psi` is called an eigenvector when `max |H_R psi - lambda psi| < 1e-9` with `lambda = Re<psi|H_R|psi>`. `G` is `deg` times `<psi|Pi_0/deg|psi>` from the block ground projector, `F` is
the classical fidelity `(sum sqrt(p q))^2` between `|psi|^2` and `diag(Pi_0)/deg`, and every figure is weighted by the outcome's own odds. The stagewise profile repeats the test at
each node of the rule-(b) tree, weighted the same way.

**Reading, not theorem.** This is why the corner works and the face does not. Once a corner's own records are all present, what is left of the law is a Hamiltonian for which the
conditioned sea is already at rest: running it forward changes nothing, and settling it to the lowest arrangement changes nothing either, because it is already there. The face leaves
the conditioned sea off its own ground state, and the lattice's law then carries odds into patterns the sea never registers. Shape, not size.

## Theorem 4 -- under relaxation nothing short of the whole cluster keeps the zeros

**Conclusion.** `[numerical, 1e-12]` Under rule (a) the cancellation zeros kept over the sixteen declared orders are `U1 [0,0,0,0]`, `U2 [0,0,64,0]`, `U3 [0,0,0,0]`, `U4 [64,64,64,64]`,
and over the declared sweep at most `64`; only `U5` -- all twelve sites at once -- keeps all `2112` zeros. The `64` that do survive under `U4` are **exactly the first-formed star's
coset and its antipode's**, at all four declared orders: `cstar(v)`'s nine edges fix the corner parities on `{v} u N(v)`, and in the sharp-`N = 4` sea both all-occupied and all-empty
are forced to zero, so a `U4` unit's own joint odds already vanish there. Later stars' cosets go to the intervening relaxation. The same "formed first, therefore kept" reading does
**not** transfer to the corner unit: under `U2 evenfirst`, whose first unit is `corner0`, the surviving cosets are `1` and `6`, **not** `0` -- consistent with a `3`-site unit's own
joint odds vanishing on none of the sea's zeros. And the readable charge stays smeared: `P(Q = 0)` never reaches `1` below `U5` -- best `0.841145833` at `U3`, the four-site face,
against `U4`'s `0.666666667 .. 0.750000000` -- while `U5` gives exactly `1.000000000`.

**Proof.** Whole trees again, one per (unit type, order) under rule (a) plus the `40`-permutation sweep for `U2`, `U3`, `U4`; the surviving cancellation zeros are broken out per
cancellation coset and compared, coset by coset, with the antipodal pair of the schedule's first unit. The charge law is read off each tree against the parity dictionary.

**Reading, not theorem.** Settling to the lowest-energy arrangement between formation events does something definite, and what it does here is not repaired by forming records
together: at every unit shorter than the whole cube it leaves at least three quarters of the sea's forbidden patterns admissible, and it leaves the readable charge spread out. The
panel's candidate wording and the corner unit are two separate choices, and on this cluster they do not combine.

## Theorem 5 -- order dependence shrinks with the unit but does not vanish, and is not monotone

**Conclusion.** `[numerical, 1e-12]` Max pairwise `TV` over the four declared orders, rules (a)/(b): `U1 0.602777777778 / 0.619386368116`, `U2 0.461024273 / 0.286110110`,
`U3 0.562500000 / 0.506673787`, `U4 0.250000000000 / 0.076616282355`, against exactly `0` for the control. Each is a **lower bound** on the spread over all orders of that unit list.
The dependence shrinks with unit size but never vanishes short of `U5`, and it is **not monotone**: the four-site face `U3` is more order-dependent than the three-site corner record
set `U2` under both rules. Formation events per unit type average `12`, `6.00`, `4.50`, `2.75`, `1`.

**Proof.** Six pairwise `L1` sums per unit type and rule over the trees of `T2` and `T4`; the event counts are the schedule lengths, which are deterministic because which unit
registers which sites does not depend on the outcomes.

**Reading, not theorem.** The finished set is the same twelve records whichever sequence of neighbourhoods formed them, and how likely it was should not depend on that sequence. It
still does, everywhere short of the whole cluster -- and a bigger unit is not automatically a better one.

## Open, not claimed

Under rule (b), `U2 identity` and `U2 reverse` finish with all `256` cancellation zeros although the propagated state **visits** `192` cancellation-coset labels at intermediate nodes
(the union of the state's `Z`-support over every node of the tree is `2176`, against the sea's `1984`). The union never leaves the `N = 4` sector for any schedule, and for the two
exact-sea schedules it never leaves the sea's `1984` labels at all. Why the visited amplitude never reaches a leaf with a matching record prefix is **not** explained here: the
eigenvector mechanism of `T3` covers the two exact-sea schedules and no more. This is recorded as an observation, and anyone landing on it should either derive it or keep it stated.

## Corollary -- what this says about the unit of record formation

Within the setting declared above, on the cube in the staggered sector at half filling, and for the five stipulated units and three stipulated between-event rules alone:

1. **The unit of record formation matters, and the unit that fits is a corner's own record set.** With the unitary tick, joint formation on `star(v)` keeps the sea's forbidden patterns
   that site-wise formation loses (`T2`), and schedules of **disjoint** corner record sets reproduce the sea's registration exactly, at every `tau` tested.
2. **The reason is exact, and it is about shape.** A jointly formed corner set leaves the conditioned sea an eigenvector of what remains of the law, so the evolution between events
   cannot disturb it (`T3`). The face unit is larger and does not have this property; the closed corner star has it, and its complement is another corner's record set.
3. **The panel's candidate and the corner unit do not combine.** Under relaxation nothing short of the whole cluster keeps more than `64` of the `256` cancellation zeros, at any
   declared order or swept order, and the readable charge stays smeared (`T4`).
4. **What remains open.** Order independence short of the whole cluster is not achieved by any unit here (`T5`), and the mechanism for the non-disjoint corner schedules that keep the
   zeros is not derived ("Open, not claimed").
5. **A candidate formation sentence this supports**, offered as a candidate wording and **not** as axiom text, on the same footing as the vacuum panel's own candidate: *"Records form
   together on a corner's record set; between formations the law runs on."*

## Reading, not theorem -- the whole thing in plain words

Let the records at one corner form all at once, as one event, and let the lattice's law run on undisturbed in between. Then the sea's own forbidden patterns, the ones that matched the
known selection rules, all survive, and for the right sequence of corners the records come out exactly as the sea itself would register them. Forming one record at a time loses all of
that, and so does settling to the lowest energy in between. It is the corner, the shape of the shared condition, that does the work, not the number of records formed at once.

## Interfaces named for other lanes, not settled here

- **Larger clusters.** Whether a corner's record set keeps this property on the `3x3x3` cube, on periodic boundaries, or in the thermodynamic limit is outside this note; the sea's
  degeneracy and the corner-star census both depend on the cluster.
- **The fine lattice.** The cube here is an emergent cluster of the physical lattice; nothing is said about the unit of formation on the physical sites themselves.
- **The formation rate.** How often a unit forms, and which one forms next, is stipulated here as an order and is not derived; reading note (2) says the axioms supply neither.
- **The open mechanism.** The non-disjoint corner schedules of `T2` that keep all `256` zeros are not covered by `T3`.
- **The exact-sea schedules on tori.** Whether a minimum vertex cover of the cluster graph plays the role `U2 evenfirst` plays here, on other graphs and on periodic boundaries, is
  named and not computed.

## Remaining live routes

1. Whether some between-event rule other than the three declared here -- a partial relaxation, or a dissipative generator with the sea as its stationary object -- keeps the zeros at a
   unit smaller than the whole cluster. Only the three ends are computed here.
2. Whether the eigenvector property of `T3` characterises the units that work, on this cluster and on others: every unit that keeps all `256` zeros here has it, but the converse is
   not established.

## Executable claim block

The canonical machine-bound restatement of the five theorem conclusions and the open item.

```text
setting: qubits on the 12 EDGE sites of the 2x2x2 cube graph (8 corners, 6 faces); ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading notes (2) and (3)
encoding: A_ij = X(edge ij) * Z's ordered before it at both endpoints; A_ji = -A_ij; B_v the Z's incident to v; S_f the ordered four-A face loop; T_ij = (i/2) A_ij (B_i - B_j)
law: eta = Kawamoto-Smit staggered signs, flux -1 on all six faces; H = -sum_e eta_e T_e, t = 1; code space all six S_f = +1, dim 128 = the even-N space; the sea = its ground state, E = -4 sqrt 3, non-degenerate, gap 2 sqrt 3, sharp N = 4, Born support 1984 and 2112 zeros = 1856 charge + 256 cancellation on the 8 closed corner stars x 32
dictionary: n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2; N = sum_v n_v; readable charge Q = N - 4
formation_model: STIPULATED, seven declared choices -- (i) start from the sea; (ii) five UNITS U1 edge / U2 star(v) / U3 face / U4 closed corner star (9 edges, = E \ star(7-v)) / U5 all twelve; (iii) the next unit in a DECLARED order, 16 declared for U1-U4 plus U5's, plus a declared 40-permutation lexicographic sweep for U2, U3, U4; (iv) only the unrecorded sites of that unit register, and they register JOINTLY with the odds of the current pre-record object on the 2^m patterns; (v) between events one of three DECLARED rules -- (a) M_R relaxation with the Pi/deg tie-break, (b) A = exp(-i tau H_R) at tau = 0.5, (c) L nothing; (vi) a unit with no unrecorded sites is SKIPPED and the rule after the last event is not applied; (vii) records permanent, run to 12. No seed anywhere; every order written out in the runner
setting_and_zeros [exact; 1e-12 zero read]: R0-R4 pair by pair, no -I in the face group, k = 5, code dim 128, flux -1 on all six faces, every hop term has X-part exactly one edge qubit; E_sea = -6.928203230276 = -4 sqrt 3, deg 1, gap 3.464101615138, mass off N = 4 is 2.0e-31; sea support 1984 = 62 x 32, 2112 zeros = 1856 charge + 256 cancellation = the 8 closed corner stars x 32; unit counts 12/8/6/8/1 and sizes 1/3/4/9/12; cstar(v) = E \ star(7-v); events per order U1 [12,12,12,12], U2 [7,7,4,6], U3 [4,4,5,5], U4 [3,3,2,3], U5 [1]; one unit's own joint odds forbid 0 + 0 at every U1, U2, U3 unit, 448 + 64 at every U4 star, 1856 + 256 at U5
T1_control [numerical, 1e-15]: rule (c) gives support 1984 and TV <= 7.4e-16 to the sea at all 17 declared schedules, with max pairwise TV 4e-16 (U1), 4e-16 (U2), 2e-16 (U3), 8e-17 (U4); [numerical, 1e-12] U1 under rule (b) reproduces PR #7895 -- support 2240, 1856 charge zeros kept, 0 of 256 cancellation kept, TV 0.324925160534
T2_unitary [numerical, 1e-12]: cancellation zeros kept, rule (b), four declared orders: U1 [0,0,0,0], U2 [256,256,256,0], U3 [0,0,0,0], U4 [128,128,256,128], U5 [256], all 1856 charge zeros kept everywhere; lexicographic-40 sweep 4/40 for U2, 0 for U3, 128 constant for U4; U2 evenfirst TV 1.11e-15 and U4 antipodal TV 7.02e-16, both on support 1984, at every tau in {0.1, 0.5, 1.234567, 2.0}, while U1 identity and U3 identity keep 0 of 256 at every tau
T3_mechanism [numerical, 1e-9]: after star(0), G = 1.000000000, deg 1, exact H_R eigenvector at 8/8 outcomes, TV(|psi|^2, Pi/deg) = 0; after cstar(0), G = 1.000000000 at 448/448, deg 2, F = 0.636894534, Fq = 0.500; after one edge G = 0.962606706 at 0/2; after one FACE G = 0.890431430 at 0/16; eigen-weight 1.000 at every node a between-event step follows for U2 evenfirst and U4 antipodal, 0.000 at the first seven levels for U1 identity, 0.000/0.079/0.142 for U3 identity
T4_relaxation [numerical, 1e-12]: cancellation zeros kept, rule (a): U1 [0,0,0,0], U2 [0,0,64,0], U3 [0,0,0,0], U4 [64,64,64,64], sweep at most 64, U5 all 2112 zeros; the 64 under U4 are exactly the first-formed star's coset and its antipode's at all four declared orders; under U2 evenfirst the survivors are cosets 1 and 6, NOT the first-formed corner0's coset 0; P(Q = 0) best 0.841145833 (U3), U4 0.666666667 .. 0.750000000, U5 exactly 1
T5_order [numerical, 1e-12]: max pairwise TV over the four declared orders, rules (a)/(b): U1 0.602777777778/0.619386368116, U2 0.461024273/0.286110110, U3 0.562500000/0.506673787, U4 0.250000000000/0.076616282355, control exactly 0; a LOWER BOUND over all orders of each unit list; not monotone -- U3 > U2 under both rules; mean events 12, 6.00, 4.50, 2.75, 1
OPEN_not_claimed [numerical, 1e-11]: under rule (b) the node-support union never leaves N = 4, and is 1984 for both exact-sea schedules, but U2 identity visits 192 cancellation-coset labels at intermediate nodes (union 2176) and still finishes with all 256 zeros; not explained here
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=24 FAIL=0
```

## Proof boundary

Every statement above is proved on **one finite cluster**, the `2x2x2` cube graph, in **one flux sector** (all-minus, the Kawamoto-Smit staggered signs) at **one filling** (the
half-filled sea, `N = 4`). Nothing is claimed for larger clusters, periodic boundaries, infinite lattices, other sectors, other fillings, or any law family other than the one in
"Definitions". The law is **designed**, not derived: the encoding is chosen so that the Majorana relations `R0`-`R4` hold, the face constraints make that consistent, and the parity
dictionary is one readout map among many, with no uniqueness claimed for either.

**The formation model is stipulated in full and derived from nothing.** The five unit types, the sixteen declared orders and `U5`'s, the declared `40`-permutation lexicographic sweep,
the three between-event rules, the `Pi/deg` tie-break, the skip-an-already-recorded-unit convention, `tau in {0.1, 0.5, 1.234567, 2.0}`, and the joint-odds formation step itself are
all declared here, not taken from any axiom. Reading note (2) is explicit that the axioms supply no formation site, probability or rate; they supply no unit of formation either, and
this note supplies none and declares five instead. The owner's statement is quoted as the **question** this note answers on one cluster, read at the level of formation because records
are permanent; it is not treated as axiom text and nothing here settles it. The vacuum panel's candidate wording is likewise a candidate, is not called wrong anywhere above, and
`M_R` is reported as one way of making it definite: what is stated is what each declared rule does.

**Nothing here says what the framework's tick is**, and nothing here forecloses any unit, rule or rate. The order-dependence figures of `T5` and the `4/40` and `0/40` counts of `T2`
and `T4` are maxima and counts over **declared finite sets** -- sixteen orders and forty permutations, all written out in the runner -- and are lower bounds on the spread over all
orders of each unit list, labelled so everywhere they appear. Every line not tagged `[exact]` is a **deterministic double-precision evaluation** of an exactly specified quantity at
the stated threshold: the formation trees are enumerated whole and nothing is sampled, but each node's relaxed object or evolution comes from a diagonalisation, against which no exact
rational value stands. There is **no seed anywhere** in this note or its runner and no Monte Carlo section. No absolute unit appears anywhere, no axiom text is amended, extended,
reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

An honest auditor should come away with a stipulated unit of record formation and its consequences, not a claim about what the framework's tick is; a two-sided result -- the corner
unit keeps the sea's zeros under the unitary rule and the face unit does not, and under relaxation no proper unit does -- on one named finite cluster, sector and filling; the
stipulation declared as stipulated in the front matter, the setting, its own section, the claim block and the proof boundary alike; the owner's statement quoted as the question and
read at the level of formation, with the reading stated; the vacuum panel's candidate sentence quoted as a candidate wording and nowhere called wrong; the order and sweep figures
labelled as lower bounds over declared finite sets; the disagreements with the naive form of the prediction stated plainly in `T3`, `T4` and `T5` -- the larger face unit is worse than
the smaller corner unit, relaxation is the identity at `U2` and worse at `U4`, and the "formed first, therefore kept" reading holds for `U4` only; and the corollary written as an
obligation on a formation rule, not as a foreclosure.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority" pointers are plain
text carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair at `PASS=24 FAIL=0`, runtime under the declared `150` seconds, a current
zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a separate lane.
