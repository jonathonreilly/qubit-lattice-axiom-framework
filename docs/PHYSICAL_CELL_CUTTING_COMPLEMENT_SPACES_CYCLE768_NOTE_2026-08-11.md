# Complement kernels, cover partner pairs, and modular pair/triple ranks

Date: 2026-08-11

Authority: none; self-contained finite construction proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [complement-space and finite-census runner](../scripts/physical_cell_cutting_complement_spaces_cycle768_2026_08_11.py)

Direct scientific dependencies: none.

Constitutional effect: none. This note changes zero axioms, primitives,
registries, policy rules, audit verdicts, effective statuses, or framework
claims.

## Trace and status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_complement_spaces_cycle768_note_2026-08-11
target_blocker_text: "classify complement spaces, cover partner pairs, and pair/triple ranks on the rebuilt finite cell object"
source_of_blocker_text: frontier_question
reachability_to_target: "direct finite construction plus exact and finite-field linear algebra"
artifact_role: "bounded finite incidence theorem candidate"
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "the target domain is the declared finite incidence object"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "two finite structure theorems plus exhaustive modular pair/triple rank censuses on one declared object"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

On the finite object reconstructed below:

1. Every proper, nonempty set `S` of the `96` cover-piece orbit tables has,
   over `Q`, the same right kernel, left kernel, image, and rank as its
   complement.
2. For each of the `192` covers, its order-two stabilizer partitions the `192`
   supported pieces into `96` partner pairs, and the `96` cover-piece orbits
   map bijectively to those pairs.
3. Over `F_1000003`, all `4,560` two-orbit sums and all `142,880` three-orbit
   sums have the rank distributions recorded below. The pair vector is also
   recomputed over `F_1000033` with identical entries.

The theorem domain is finite combinatorics. Physical interpretation, a Record
map, continuum or multicell extension, and framework-level consequences are
separate open targets.

## Inputs, imports, and provenance

| item | classification | role and provenance |
| --- | --- | --- |
| labelled corners `{0,1}^4` | declared finite-model data | Defines the unit four-cube used by this packet. |
| five-corner simplices with determinant magnitude one | declared selection rule | Enumerated directly from the `16` labelled corners. |
| minimum adjacency cost | declared selection rule | Cost counts non-edge corner pairs; the minimum and all minimizers are recomputed. |
| shifted `5^4` rational grid | enumeration nuisance | Certifies interiors and drives the exact-cover search; every mask, cutting, and volume condition is checked. |
| cutting and cover definitions | declared finite-model data | A cutting is a disjoint full mask cover; a cover is an eight-piece set meeting every cutting once. |
| signed-coordinate action | declared symmetry data | All `4! * 2^4 = 384` maps are constructed, checked distinct and closed, and applied to pieces, covers, and cells. |
| Maschke decomposition and finite-dimensional rank identities | standard mathematical import | Used over primes with `gcd(p,384)=1`; the concrete isotypic splitting and map factorizations are rebuilt and checked. |
| `p=1000003`, `q=1000033`, seed `3` | computational nuisances | The first prime defines the exhaustive modular claims; the second independently rebuilds the pair vector. The seed selects reproducible controls only. |
| Python integer/Fraction arithmetic and NumPy `int64` arrays | implementation import | Exact rational paths use `Fraction`; modular products are bounded below `192 p^2 < 2e14`, far below signed 64-bit capacity. |
| runner source text | integrity input | The runner reads only its own source for hygiene checks. External scientific data files form the empty set. |
| physical, Record, probability-law, continuum, and multicell bridges | open bridge inventory | These belong outside the declared theorem domain and supply zero premise here. |

Every numeric object count and every theorem input used below is reconstructed
inside the runner. Branch ancestry and campaign numbering supply zero scientific
premise.

## Declared finite object

The runner enumerates `2,672` determinant-one five-corner candidates, finds
adjacency-cost floor `6`, and keeps all `400` minimizers. Its shifted grid avoids
every kept facet plane. The exact-cover search returns `15,800` distinct
cuttings, each containing `24` unit-volume pieces with disjoint interiors and
full-cell union. Exactly `192` pieces occur. The clique construction returns
`192` distinct covers; every cover has eight pieces, every piece lies in eight
covers, and every cover meets each cutting once.

Permuting coordinates and independently flipping them gives `384` distinct
maps. The runner checks all `147,456` products for closure and verifies
transitivity on pieces and covers. The action on the `192 x 192` cover-piece
cells has `96` orbits. Write `O_0,...,O_95` for their binary indicator tables.
Each `O_i` has two ones in every row and column, and

`O_0 + ... + O_95 = J`,

where `J` is the all-ones table. The reconstructed cover table has exact
rational rank `105`, kernel dimension `87`, and equals the sum of four
distinguished incidence-orbit tables.

The object certificates are load-bearing gates: mask visibility, search
uniqueness and coverage, simplex volumes, pairwise interior disjointness, cover
uniqueness, `8 x 8` cover regularity, exact Gram reconstruction, explicit
kernel annihilation, independent kernel ranks, and selected-row certificates.

## Complement-kernel and image theorem over `Q`

**Complement-kernel and image theorem over `Q`.** For every `S` with
`1 <= |S| <= 95`, let `T_S = sum_{i in S} O_i` and let `S^c` be its complement.
Over `Q`, the tables `T_S` and `T_{S^c}` have equal right kernels, equal left
kernels, equal images, and equal ranks.

Each row and column sum of `T_S` is `2|S|`, while
`T_S + T_{S^c} = J`. If `T_S v = 0`, summing the coordinates of that equation
gives

`2|S| sum_j v_j = 0`.

The scalar is nonzero in `Q`, hence `sum_j v_j=0` and `Jv=0`. Therefore
`T_{S^c}v=0`. Applying the same argument to `S^c` proves equality of right
kernels. Transposition proves equality of left kernels. For a finite-dimensional
linear map over a field, its image is the annihilator of its left kernel;
equality of left kernels therefore gives equality of images. Equal ranks follow.

The same proof applies set by set over a field whenever both `2|S|` and
`2(96-|S|)` are nonzero. In particular, it applies simultaneously to every
proper nonempty `S` over both census primes. It also explains the necessary
scalar boundary: over `F_5`, prefix sets of sizes `5` and `91` give complement
rank pairs `143/144` and `144/143`; over `F_7`, sizes `7` and `89` give the
same inequality pattern. Integral image lattices lie outside this theorem.

The runner checks exact all-ones row/column membership on `16` selected sets
and directly compares right and left kernels over `F_1000003`. A spoiled table
is rejected by the same predicate.

## Cover-stabilizer partner-pair theorem

**Cover-stabilizer partner-pair theorem.** Fix a cover `c`. Its stabilizer in
the `384`-element action has order two. The non-identity element is a
fixed-point-free involution on the `192` pieces, hence gives `96` partner pairs.
Mapping a cover-piece orbit to the pair it meets in row `c` is a bijection from
the `96` cell orbits to those `96` partner pairs.

Orbit-stabilizer gives stabilizer order `384/192=2`. Freeness on cover-piece
cells makes the non-identity element fixed-point-free on pieces in row `c`.
Each orbit table has two entries in that row, and group invariance places those
entries in one partner pair. There are `96` orbit labels and `96` partner
pairs, so the map is bijective.

The runner checks the statement on all `192` covers: stabilizer size, unique
non-identity involution, fixed-point count, partner-label equality, `96`
two-element fibres, and distinct labels. Swapping two labels in a scratch row
is rejected. On one cover, its eight member pieces carry exactly the four
incidence labels, twice each; a separate mutation corrupts one label and is
rejected.

## Certified small-block rank bridge

Let `V` be the piece permutation module and `W` the cover permutation module
over `F_p`, for either declared prime. Since `gcd(p,384)=1`, Maschke's theorem
makes both modules semisimple. On an isotypic part of irreducible degree `d_i`,
an equivariant map `V -> W` has the form `I_{d_i} tensor M_i` after multiplicity
bases are chosen. Consequently,

`rank(T) = sum_i d_i rank(M_i)`.

The runner constructs the full commutant, computes its center with exact
rational elimination, and finds dimension `20`. An integral central element
has `20` distinct eigenvalues modulo each declared prime, so its kernels isolate
all `20` isotypic parts. For each part, the runner verifies the dimensions
`d_i`, source multiplicity `m_i`, and cover multiplicity `mc_i`; constructs
left inverses and pure-vector bases; checks every restriction and reconstruction
residual; and obtains the `96` orbit coefficient matrices. The global sums
recover the dimensions of the commutants and modules. At both primes the
coefficient map has width and rank `96`, the active parts agree, and every
five-condition factorization gate passes. These facts establish the displayed
rank formula for every orbit-table sum used by the censuses.

As controls, the formula matches direct `192 x 192` elimination on `62` tables,
including the cover table; on `25` selected pairs; and on `15` selected triples.
All `15` nonempty incidence subsets also receive exact rational ranks.

## Exhaustive modular censuses

Over `F_1000003`, the complete pair vector has `4,560` entries, `13` distinct
ranks, range `48..144`, `960` entries at `144`, and `1,104` entries at or below
`105`. Rebuilding every pair at `F_1000033` gives zero entrywise differences.
The complement theorem transfers this same modular vector to size `94`.

Over `F_1000003`, the complete triple vector has `142,880` entries, `18`
distinct ranks, range `64..144`, `60,960` entries at `144`, and `1,472` entries
at or below `105`. The complement theorem transfers this modular vector to size
`93`.

The exact rational incidence ranks are:

- four singletons: `144,144,144,144`;
- six pairs: `72,93,117,129,144,144`;
- four triples: `114,130,142,142`;
- the incidence quartet: `105`.

Each singleton orbit table is a disjoint union of `48` bipartite cycles of
length four on each side. The elementary cycle-matrix calculation gives exact
rank `3` per block and exact singleton rank `144`.

From the modular pair vector, all `96` vertices have below-ceiling degree `75`.
Among `325` realized stratum-pair fibres, `313` contain more than one
`F_1000003` rank, with maximum fibre diversity `13`. These are positive finite
census statements at the declared prime.

## Mutation and independent-check ledger

Every scratch mutation is in memory and leaves the scientific object unchanged:

| family | mutation | required response |
| --- | --- | --- |
| object constructor | zero one kept-piece mask | full-cover certificate rejects |
| group | duplicate one signed-coordinate map | distinct-map certificate rejects |
| orbit basis | replace one orbit table by zero | row/column/sum certificate rejects |
| small-block bridge | alter one irreducible degree | block/full rank equality rejects |
| second-prime rebuild | alter one part row | two-prime certificate rejects |
| incidence corollary | replace one cover-block label | four-label/twice-each predicate rejects |
| exact all-ones route | supply the zero table | row/column membership predicate rejects |
| singleton cycle route | delete one orbit cell | two-regular cycle predicate rejects |
| pair census | set one rank above the ceiling | pinned pair summary rejects |
| triple census | set one rank above the ceiling | pinned triple summary rejects |
| degree/stratum aggregation | lift one below-ceiling pair to the ceiling | pinned aggregation rejects |

The partner-fibre and complement-kernel families retain their dedicated
swapped-label and spoiled-entry mutations. Independent review additionally
used a determinant-minors rank algorithm on every pair and triple and found
zero elementwise differences; a separate exact-rational library matched all
incidence-subset ranks.

## Proof-obligation graph

The obligation graph is acyclic:

1. `declared corners/rules -> finite object` - proved here by exhaustive
   construction and object certificates.
2. `finite object + signed-coordinate maps -> group action/orbit tables` -
   proved here by closure, bijection, transitivity, equivariance, and orbit
   certificates.
3. `two-regular orbit tables + sum O_i=J -> complement theorem over Q` - proved
   here; scalar conditions are explicit above.
4. `group action + free cover-piece action -> partner-pair theorem` - proved
   here and checked on all covers.
5. `Maschke + reconstructed isotypic factorizations -> small-block rank formula`
   - standard theorem plus concrete hypotheses and factorization certificates
   proved here.
6. `rank formula + exhaustive subset enumeration -> pair/triple modular vectors`
   - proved here at `F_1000003`; pairs independently rebuilt at `F_1000033`.
7. `modular vectors -> rational vectors for every pair/triple` - open. The
   current claim preserves the modular field label.

The strongest open lemma is item 7: equality of every modular census rank with
its rational rank.

## Edge-case and scope ledger

| case | disposition |
| --- | --- |
| `S` empty or all `96` labels | excluded from the complement theorem; the two ranks are `0` and `1` |
| characteristic dividing `2|S|` or `2(96-|S|)` | excluded from the proof; explicit `F_5` and `F_7` rank inequalities record the boundary |
| census primes | both exceed `96` and satisfy `gcd(p,384)=1` |
| integral image lattice equality | outside scope |
| rational interpretation of all pair/triple census entries | open lemma |
| size-four and size-92 exhaustive spectra | outside this packet |
| physical quantity, Record readout, probability law, continuum, multicell lattice | outside the declared finite domain |
| audit status | unset pending independent audit; this note sets zero verdict |

The landed artifact is the note, runner, canonical cache, harness registration,
and required citation manifest only. Generated audit rows and audit verdicts are
outside this review-lane change.
