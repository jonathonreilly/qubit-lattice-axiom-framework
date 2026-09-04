# Measurement/feedforward preparation of the square-pyramid code — Cycle 240

**Date:** 2026-07-17

**Type:** constructive deterministic global-decoder protocol with a bounded
local-feedforward residual

**Status:** bounded local measurement layer succeeds; explicit correction,
fixed-spin selection, and coherent dilation are not bounded-local

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** distinct Cycle-240 note and runner only; no commit, push, PR,
foundation, axiom, Qualification, primitive, registry, policy, queue, or audit
change

Companion runner:

```text
scripts/MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_2026_07_17.py
```

## Result up front

Guaita's measurement sketch works exactly through the projection step on the
Cycle-235 square-pyramid code.  It also works deterministically after an
explicit global Gaussian decoder.  This is a constructive test of **local
measurements plus feedforward**, but the completed protocol does not satisfy
the campaign's bounded local-feedforward or no-host-side-control contract.

Start the `15L^3` face qubits in `|0>` and measure all `11L^3` bounded
modified-Gauss operators.  Each check has Pauli weight at most 28 and each data
qubit participates in at most 11 checks.  The ancilla-data incidence graph is
bipartite with maximum degree 28, so its interactions admit 28 collision-free
subrounds; adding one ancilla-preparation and one readout subround gives **30
bounded quantum subrounds**, independent of `L`.  One local syndrome ancilla
per primal edge is `11` additional temporary `M_2` carriers per coarse cell.

This constructs exactly the step Guaita sketches: local measurements project
the product state into a block-code state whose cycle relations hold up to
measured signs.  Let `H` be the binary matrix whose rows are the cycle `X`
supports and let `s` be the outcome-sign vector.  A face-sign reassignment

```text
A_f -> (-1)^(z_f) A_f
```

or, equivalently, a physical face correction `Z(z)`, closes the signs iff

```text
H z = s  (mod 2).
```

The runner constructs a right inverse of `H` and checks every syndrome basis
vector.  Including three Wilson constraints, the deterministic protocol has:

| `L` | Face qubits | Local checks | Local rank | Full rank | Measurement subrounds | Decoder max `Z` weight | Decoder mean weight | Max coarse dependency radius |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 405 | 297 | 241 | 244 | 30 | 90 | 23.729508 | 3 |
| 4 | 960 | 704 | 574 | 577 | 30 | 152 | 39.462738 | 6 |
| 5 | 1,875 | 1,375 | 1,123 | 1,126 | 30 | 314 | 60.094139 | 6 |

Every decoded branch has zero residual.  Starting from `|0>`, the measured
cycle and Wilson operators commute with every cell flux `B_t`; face `Z`
corrections do too.  Thus the global protocol prepares the encoded even vacuum
deterministically.  Once the syndrome has been decoded, all single-face `Z`
corrections can be applied in one parallel quantum layer.  The nonlocal cost is
classical decoding and outcome distribution, not the final one-qubit gate.

The spin-sector part has an exact topological residual.  Three explicit
`L x L` face membranes commute with every local Gauss check and have pairing
matrix

```text
<membrane_a, Wilson_b> = delta_(ab) mod 2.
```

Their weights are `9,16,25` at `L=3,4,5`.  The Wilson measurement weights are
`(21,17,21)`, `(27,23,27)`, and `(33,29,33)`.  Aggregating one Wilson outcome
with nearest-neighbor classical communication has radius at least
`floor(L/2)`; broadcasting the resulting conditional correction across its
transverse membrane has radius `2 floor(L/2)`.  Analytically, the correction
support is `L^2` and the communication radius grows with `L`.  A correction
supported in a bounded contractible ball has trivial pairing with every
noncontractible Wilson loop, so it cannot replace this membrane.

Therefore the explicit deterministic preparation is:

```text
bounded local projective measurement
  + global syndrome/Wilson outcome actualization
  + global classical decoder
  + conditional noncontractible correction.
```

It succeeds with probability one under the supplied projective instrument,
but it is host-controlled and non-bounded.  It is not the requested local
encoding `E`.

Postselection removes corrections but not the resource problem.  For the
clean `|0>` input, the independent check outcomes are uniform.  Selecting the
all-plus local and Wilson branch has probabilities

```text
L=3: 2^(-244),
L=4: 2^(-577),
L=5: 2^(-1126).
```

After deterministic local-sign decoding, postselecting only the three Wilson
signs still succeeds with probability `1/8`.  Both uses require an actual
outcome and a supplied rule that discards other branches.  These are standard
projective-instrument branch weights, not a derivation of the framework's Born
law or a physical occurrence process.

An autonomous coherent dilation avoids actual outcome selection: extract each
syndrome into quantum ancillas, reversibly compute a decoder, and apply
controlled face corrections.  It inherits the Wilson parity light cone and
the noncontractible correction.  With geometrically local control its depth
grows at least with the Wilson communication radius, and Guaita's independent
unitary-depth theorem becomes asymptotically active on the embedded
overlapping-loop graph.  Retaining syndrome garbage is extra supplied quantum
state; uncomputing it does not improve the light cone.  Thus coherent dilation
can remove host actualization, but not bounded depth.

The local measurement family and all-plus Wilson **label** are covariant under
all 24 proper-cubic frames.  The displayed Gaussian pivot decoder and a
depth-one product scaffold that pre-pins the Wilson signs each mismatch 23 of
24 raw frames.  A different covariant global decoder may exist.  No bounded
covariant decoder is constructed or ruled out generally.

Most importantly, measurement does not change the closed-code identity

```text
product_t B_t = I.
```

The odd sector remains absent at `L=3,4,5`.  The even coin, `A/B` FSWAPs, and
contact still have exact bounded operator images, but the one-particle mass
state and rank-73 seam state still have no physical code image.  Cycle 240
reports neither a mass residual nor a seam residual where no intertwining
state exists.

## Protocol in detail

### 1. Local syndrome measurement

The Cycle-235 cellulation has two local check orbits:

1. eight center-corner spoke triangles per coarse cell; and
2. three coarse-edge octagons per coarse cell.

Their actual framed Pauli supports, not only their cycle masks, define the
syndrome incidence graph.  The finite graph metrics are:

| `L` | Syndrome nodes | Face-data nodes | Incidences | Max check degree | Max data degree | Redundant local outcomes |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 297 | 405 | 2,916 | 28 | 11 | 56 |
| 4 | 704 | 960 | 6,912 | 28 | 11 | 130 |
| 5 | 1,375 | 1,875 | 13,500 | 28 | 11 | 252 |

All check operators commute.  A local ancilla can measure one bounded Pauli
by local controlled-Pauli interactions and readout.  Bipartite edge coloring
gives the 28 interaction subrounds.  Routing inside the existing spacing-16
macrocell changes this only by another size-independent factor; the reported
30 is the abstract face-carrier schedule before that fixed routing expansion.

Measuring all redundant checks preserves proper-cubic covariance because it
does not choose a noncovariant independent subset.  Their outcomes obey the
known `2L^3+2` dependencies.  The decoder may retain all outcomes and reduce
them locally/globally, or take the independent basis used in the runner.

The measurement outcomes are syndrome outcome registers.  **Syndrome outcome
registers are not automatically Records.**  Calling them framework Records
would require the independent permanence/readability/actualization law that
this campaign does not supply.  Adaptive feedforward nevertheless requires
one actual branch outcome to become available to the correction controller.

### 2. Exact global sign decoder

Guaita suggests correcting cycle signs by reassigning encoded edge operators.
The runner implements that proposal exactly.  It greedily selects independent
columns of `H`, forms a binary right inverse `D`, and uses

```text
z = D s,
H D = I.
```

The zero decoder residual on all `244,577,1126` syndrome basis vectors proves
deterministic finite-size success.  Reassigning `A_f` signs and applying
`Z(z)` are algebraically equivalent: either changes the sign of precisely the
cycle operators whose `X` support pairs with `z`.

This decoder is intentionally exposed as a host-side Gaussian elimination,
not hidden behind “feedforward.”  Its maximum correction weights grow
`90,152,314`; the selected pivot face set fails raw covariance in 23 frames.
These numbers characterize this decoder, not a lower bound on all decoders.

### 3. Spin/Wilson handling

Local Gauss measurements leave eight topological sectors.  The target
untwisted `(+,+,+)` Wilson label is invariant under proper-cubic rotations,
but obtaining it requires one of three additional resources:

- measure three noncontractible Wilson operators and conditionally apply the
  `L x L` membrane corrections;
- postselect the desired three outcomes, with conditional mass `1/8`; or
- supply a product scaffold already eigenstate of three Wilson representatives.

The runner finds pairwise-disjoint Wilson representatives at every held size.
Once their globally named supports are supplied, single-qubit eigenstate
preparations pin all three signs in depth one and commute with every local
Gauss measurement.  Their support weights are `59,77,95`.  This scaffold does
not fix the local cell fluxes, and its chosen representatives mismatch 23 of
24 frames.  It is a global noncontractible preparation pattern, not a
proper-cubic homogeneous local law.  It removes the Wilson decoder only by
supplying the spin resource in the initial state.

No one of these alternatives is a bounded, host-free, cubic preparation of a
fixed spin sector from homogeneous product data.

### 4. Deterministic, postselected, and coherent dispositions

| Route | Finite result | Correction/control | Contract disposition |
|---|---|---|---|
| local unitary from product | Guaita bound has held-size `d=0`; becomes `1,2,3,4` at `L=6,10,14,18` | local two-body gates only | asymptotically not bounded under theorem hypotheses |
| local measurement + bounded feedforward | 30-round local projection constructed | no bounded sign/Wilson decoder constructed | still live generally; this attempt incomplete |
| measurement + global decoder | exact deterministic success at `L=3,4,5` | Gaussian decoder, outcome broadcast, membranes | constructive but violates no-host/bounded-radius contract |
| postselection | exact selected branch | discard all other outcomes | exponentially small full-branch mass or `1/8` after local decoding |
| autonomous coherent dilation | exact algebraic replacement in principle | coherent syndrome ancillas and reversible global decoder | no outcome actualization, but growing depth/garbage |

Compiler subrounds, classical propagation steps, and coherent circuit depth
are supplied implementation costs.  They are not physical elapsed time, a
rate, a clock, winding, or realized history.

## Proper-cubic covariance

Cycle 235 already established the local framing repair and exact `24 x 24`
group law on face `X/Z` generators.  Cycle 240 separately rechecks that every
local measurement mask maps into the same modified-Gauss family under all 24
frames.  Hence the measurement **instrument family** is cubic before outcome
selection.

The all-plus Wilson target is also cubic: rotations permute its three zero
syndrome bits.  Concrete Wilson loops, membranes, decoder pivots, correction
roots, and the product scaffold are global presentation choices.  The
displayed choices are not frame invariant.  Covariantizing a global decoder
by an orbit/tie-break protocol would still leave global communication and
would add supplied control structure.

Thus covariance succeeds for the local quantum layer and target sector, but
not for the completed bounded host-free protocol because no such protocol was
constructed.

## Even update, odd sector, mass, and seam

The preparation layer does not alter the exact Cycle-235 even algebra:

- cell flux has weight 5;
- hopping generators have weight at most 9;
- modified-Gauss checks have weight at most 28;
- the six-mode onsite even neighborhood uses at most 18 face carriers;
- the coin and contact commute exactly with parity; and
- every mapped even update commutes with the measured constraints.

For a successfully prepared even vacuum, mapped even gates preserve the code
with zero ideal leakage.  Contact deletion at `g=0` remains identity.

However, the Wilson and Gauss measurements add no logical qubit.  Exact ranks
after spin fixing remain

```text
6L^3-1 = 161,383,749  at L=3,4,5.
```

The missing qubit is the odd total-parity sector.  The one-particle fixture is
odd, and the Cycle-230 principal sea has occupied rank 73, also odd.  Therefore:

```text
even update-operator representation: exact and bounded,
even vacuum preparation with global decoder: exact,
one-particle mass intertwining: unavailable,
rank-73 seam intertwining: unavailable,
full-Fock E G = G_physical E: not established.
```

Measurement does not turn a parity-even operator representation into the full
Cycle-230 state compiler.

## Supplied-structure inventory

The global deterministic protocol supplies:

1. the Cycle-235 square-pyramid cellulation and local framing;
2. 15 face data qubits and 11 temporary syndrome ancillas per coarse cell;
3. a projective Pauli-measurement instrument and branch-weight rule;
4. actualized syndrome outcome registers;
5. the independent-row and pivot-face choices of a Gaussian decoder;
6. global classical collection and broadcast of syndrome bits;
7. three noncontractible Wilson measurements and `L x L` correction membranes;
8. a conditional single-face correction layer or outcome-dependent `A_f`
   sign table;
9. the untwisted spin sector, macro origin, routing, and schedule; and
10. the Cycle-219 coin and Cycle-230 contact, coupling, and gate order.

The product-scaffold variant replaces items 6–7 for the Wilson bits with a
globally marked noncontractible initial pattern.  The coherent variant
replaces items 3–6 with quantum syndrome ancillas, a reversible decoder, and
garbage handling.  None is silently counted as native framework structure.

## Primary-source and novelty boundary

Tommaso Guaita, “On the locality of qubit encodings of local fermionic modes,”
*Quantum* **9**, 1644 (2025),
<https://doi.org/10.22331/q-2025-02-25-1644>,
<https://arxiv.org/abs/2401.10077>, proves the local-unitary depth result under
its exact product-state/two-body-unitary hypotheses.  In its discussion it
explicitly says measurements and adaptive feedforward may change the
conclusion, sketches measuring every cycle product, and proposes correcting
outcome signs by `A_jk -> -A_jk`.  It does not construct the decoder or prove
that its classical communication is bounded.

Chen–Kapustin and Chen supply the exact even-algebra bosonization, modified
Gauss law, and spin-structure dependence used by Cycle 235.  They do not
supply this measurement protocol or a full odd-sector encoder.

The Cycle-240 contribution is the explicit square-pyramid syndrome graph,
30-subround local measurement bound, exact finite Gaussian right inverse,
correction support audit, Wilson membranes and pairings, postselection branch
counts, product scaffold, covariance audit, and coherent/actualized outcome
comparison.  It is not a general LOCC lower bound.  Global priority is not
claimed.  Thirring machinery is neither used nor compared.

## TOE dependency ledger after Cycle 240

| Workstream | Cycle-240 effect | Remaining dependency |
|---|---|---|
| `C_ref` | preparation outcomes and spin/scaffold data exposed | physical phase origin, sea, actualized outcome law, and realized preparation remain supplied |
| `C_num` | unchanged structural boundary | closed face code remains total-even; odd number sector absent |
| `C_wrap` | unchanged | Wilson bits, measurement rounds, decoder steps, and membranes are not time or winding history |
| `C_int` | even-sector preparation gain | contact operator is exact on prepared even code; odd rank-73 fixture, selection, and rate remain open |
| `C_local` | materially narrowed | bounded local measurements succeed; bounded local feedforward, host-free spin selection, odd-sector `E`, and homogeneous marker preparation remain open |
| `C_source` | unchanged | no physical energy, stress, action, or gravitational source is selected |

The maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
Measurement syntax and standard branch weights do not derive a Record,
actuality, or probability law.

## No-go discipline gate

The fresh `origin/main` no-go discipline was applied because this artifact
ships a failed bounded-feedforward attempt.

**N1–N8 result:** **PASS for the narrow statement that the explicit
measurement protocol closes local projection but its displayed sign/spin
decoder is global.  FAIL for a general measurement-assisted preparation
no-go, a general LOCC lower bound, minimality, uniqueness, or axiom pressure.**

### N1 — alternative routes

| Route | Marker | Disposition |
|---|---|---|
| local projective checks plus Gaussian decoder | **ATTEMPTED** | deterministic exact code preparation; decoder weights and communication are global |
| all-plus postselection | **ATTEMPTED** | no correction, but branch mass is `2^-(9L^3+1)` |
| Wilson-pinned product scaffold plus local checks | **ATTEMPTED** | removes Wilson decoding but supplies noncontractible marked supports and breaks raw covariance |
| autonomous coherent syndrome dilation | **ATTEMPTED ALGEBRAICALLY** | removes actualized outcomes but retains growing reversible decoding/light cone |
| translation/cubic-covariant local cellular decoder | **UNTESTED, LIVE** | no bounded decoder was found or disproved for all local syndromes |
| measurement-based topological resource state | **UNTESTED, LIVE** | can move long-range correlations into a supplied cluster/resource state |
| open boundary/puncture with local syndrome sink | **UNTESTED, LIVE; TARGET CHANGED** | may simplify decoding and odd flux, but adds a marked boundary and changes the closed target |

Only four rows have the strict no-go-skill honesty marker `ATTEMPTED`; none is
`RULED OUT BY PRIOR`.  The three live rows therefore fail N1 for a broad
measurement-assisted no-go, which is why that claim is demoted rather than
shipped.  They do not weaken the direct finite statement about the displayed
Gaussian protocol.

### N2 — condition independence

The raw conditions collapse to five:

- `K_syndrome`: correction/reassignment of random local Gauss signs;
- `K_spin`: preparation of one of eight Wilson sectors;
- `K_outcome`: actualized measurement outcome and adaptive control, or a
  coherent replacement;
- `K_odd`: the closed-code total-even identity; and
- `K_marker`: homogeneous preparation of the macro/translation role pattern.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `K_syndrome`, `K_spin` | no | no | yes |
| `K_syndrome`, `K_outcome` | no: coherent decoding remains possible | no | yes |
| `K_syndrome`, `K_odd` | no | no | yes |
| `K_syndrome`, `K_marker` | no | no | yes |
| `K_spin`, `K_outcome` | no: scaffold can pre-pin spin | no | yes |
| `K_spin`, `K_odd` | no | no | yes |
| `K_spin`, `K_marker` | no | no | yes |
| `K_outcome`, `K_odd` | no | no | yes |
| `K_outcome`, `K_marker` | no | no | yes |
| `K_odd`, `K_marker` | no | no | yes |

Postselection is a route through `K_syndrome/K_spin`, not a sixth wall.
Decoder covariance is downstream of the chosen syndrome/spin decoder, not a
separate constitutional condition.

### N3 — hidden-condition scan

| Potential hidden phrase/condition | Classification |
|---|---|
| “measure” | supplied projective instrument, outcome actualization, and branch weights |
| “feedforward” | supplied decoder, readable outcome registers, communication graph, and conditional gates |
| “prepare locally” | restricted to the 30-round quantum projection; does not include decoder |
| “standard stabilizer correction” | avoided; exact right inverse and supports are executable |
| “background spin structure” | explicit `K_spin` and three Wilson bits |
| “Record” | not inferred from copied syndrome pointers |
| “time/depth” | compiler cost only; no physical-time interpretation |

No hidden condition is promoted after the collapsed ledger.

### N4 — residual matching

| Witness | Witness residual | Cycle-240 use | Match? |
|---|---|---|---:|
| Guaita 2025 Theorem 2 | local two-body **unitary** depth from product state | comparison route only; not used against measurement | yes, scoped |
| Guaita discussion | measurements/feedforward may prepare block code; signs require reassignment | exact target of the projection/decoder construction | yes |
| Cycle 235 | bounded square-pyramid even algebra, global preparation and spin open | prepares that exact stabilizer family | yes |
| Cycle 237 | measurement/feedforward explicitly live | resolves local projection and exposes global decoder | yes |
| Cycle 219 mass | one-particle odd sector required | remains absent; no false residual reported | yes |
| Cycle 230 seam | rank-73 odd sea required | remains absent; no false residual reported | yes |

No cited theorem is upgraded to a measurement lower bound.

### N5 — resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| one local check | bounded Pauli measurement gadget | fault tolerance/noise threshold |
| whole local check family | exact syndrome graph, rank, dependencies, 30 subrounds | bounded local correction map |
| selected Gaussian decoder | exact `HD=I`, weights, radii | optimal decoder lower bound |
| Wilson sector | exact measurements, membranes, pairing, scaffold | homogeneous bounded sector preparation |
| postselection | exact branch exponents under standard projective instrument | framework Born/actuality law |
| coherent dilation | parity-lightcone and resource inventory | optimized autonomous QCA construction |
| all 24 frames | local family and target label pass; displayed decoder/scaffold fail | every covariant decoder |
| `L=3,4,5` | deterministic global protocol and odd-rank identity | asymptotic LOCC classification |
| mass/seam | sector membership only | physical residuals, because states are absent |

Every negative is restricted to the displayed protocol or exact closed-code
identity.

### N6 — partial-closure and primitive scan

The current primitive registry and every relevant `current_path` were checked.
The approved scale-reference, kinetic-isotropy, and realized-state primitives
chain-satisfy exactly their declared units-conversion, OS0 kinetic-form, and
pointwise-evaluation slots.  Their source notes grant no measurement
instrument, decoder, outcome-actualization rule, spin state, odd reservoir, or
marker preparation.  They are approved premise nodes, not walls and not
sources of bounded status.  The Record axiom says that Records form and lock
one admissible possibility, but it supplies no measurement or record-formation
rule that makes a syndrome ancilla into a Record.  Live closures are:

| Path | Status | Possible effect |
|---|---|---|
| translation/cubic local cellular decoder | unbuilt | retire host Gaussian elimination if bounded rounds suffice |
| measurement resource/cluster state | primary literature live | replace classical long-range correction by a supplied entangled resource |
| coherent local CA run for `O(L)` layers | constructive in principle | remove host/outcome actualization but not bounded depth |
| symmetry-restored Wilson scaffold orbit | unbuilt | recover covariance at cost of long-range resource state |
| open boundary or physical fermion reservoir | target-changing live route | handle odd flux and give syndrome sink |
| operational parity-superselected contract | explicit alternative | retain even compiler without claiming full-Fock `E` |

These are constructive/import-retirement paths, not proposed axioms.

### N7 — steelman

> Guaita explicitly anticipates that local measurements and feedforward may
> efficiently prepare these block encodings.  Cycle 240 confirms the hard
> quantum part: every local Gauss check is measurable in constant depth, and
> a deterministic correction exists at every held size.  The growing weights
> belong to one Gaussian decoder, not an optimum.  A translation-covariant
> cellular decoder, cluster-state resource, pre-pinned spin scaffold, or
> measurement-only topological preparation might keep quantum depth bounded.
> The all-plus spin label itself is cubic.  Therefore this result is progress
> toward Guaita's proposed escape, not evidence that measurement-assisted
> local preparation is impossible.

That steelman is convincing.  The measurement-assisted route remains live;
only the displayed host-free bounded protocol fails.

### N8 — cross-cycle echo

The repository no-go phrase search and physics-loop `NO_GO_LEDGER.md` walk
were rerun with the current `origin/main` no-go skill.

| Earlier boundary | New mechanism | Effect here |
|---|---|---|
| Cycle 235 global code preparation supplied | bounded local check measurement | projection layer closes; decoder remains |
| Cycle 237 Guaita unitary obstruction | measurement/feedforward exception | explicitly attempted rather than foreclosed |
| Cycle 236 local evolution but global preparation | measurement moves nonlocality to outcome decoder | same dependency distinction, different mechanism |
| prior record campaigns | readable pointers do not automatically form Records | syndrome registers remain operational inputs, not derived ontology |
| prior marker campaigns | periodic role choice can become a covariant code family | may help local scheduling, but not Wilson outcome propagation |

No retired convention supplies bounded syndrome communication or an odd
sector.  No axiom pressure follows.

## Route disposition and next discriminator

**Cycle-240 disposition:** retain the exact 30-subround local measurement
layer and deterministic finite global decoder as a constructive preparation
result for the even vacuum.  Reject it as the requested bounded host-free
compiler because the explicit decoder, Wilson measurements/corrections, and
outcome control are global.  Retain local measurement plus a different
bounded cellular decoder as live.

The next discriminator is an explicit translation- and cubic-covariant local
decoder or measurement-resource protocol.  It must solve every lawful local
syndrome and fix the spin sector with correction/communication radius bounded
independently of `L`, avoid postselection and host outcome control, and state
whether its syndrome information is actualized or coherently retained.  The
closed odd-sector failure is separate and must not be hidden by a preparation
success.

`C_local` is narrowed, not closed.  There is no shared obstruction, no axiom
pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_2026_07_17.py
```
