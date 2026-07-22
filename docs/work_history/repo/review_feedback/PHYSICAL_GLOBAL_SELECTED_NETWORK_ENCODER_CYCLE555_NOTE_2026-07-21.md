# Physical global selected-network encoder — Cycle 555

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_global_selected_network_encoder_cycle555_2026_07_21.py`

## Result

Cycle 555 constructs one genuinely **global selected**-carrier encoder on a
complete finite periodic network.  The construction covers the complete
global CAR sectors `N=0,1,2` on the smallest nondegenerate periodic L3 torus
and held L4:

| network | cells | CAR modes | N=0 | N=1 | N=2 | complete columns |
|---|---:|---:|---:|---:|---:|---:|
| train L3 | 27 | 162 | 1 | 162 | 13,041 | **13,204** |
| held L4 | 64 | 384 | 1 | 384 | 73,536 | **73,921** |

Every lawful local word has exactly two strict-pinned selected rays.  A
previously unexploited physical **companion** role provides one unique branch
pivot per cell.  On every declared local word:

```text
branch 0 flips no companion pivot,
branch 1 flips exactly its own cell's companion pivot,
no other cell flips that pivot.
```

Therefore the global decoder is not a `2^(L^3)` table and not a nonlocal GF(2)
parity inverse.  It is exactly one nearest-neighbour **CNOT** per cell:

```text
D_network = product_c CNOT(companion_c -> branch_c).
```

With `A` the local one-bit branch preparation and `SELECT` the actual selected
Pauli circuit in one transported compile-time factor order,

```text
W_network = D_network SELECT A,
E_network |q> = W_network |q>|Omega_fixed>|0_branch,work>.
```

The decoded interval uses the frozen Cycle-551 **Route A** actual-physical-
footprint scheduler rule.  Its target is materialized on complete global
`N<=2` states, including contact-sensitive pair amplitudes.  The physical
update is the explicit circuit

```text
G_physical = W_network G_target W_network^dagger,
E_network G_target = G_physical E_network.
```

The algebraic intertwiner residual is exactly zero on the declared code.  The
construction contains no global Jordan-Wigner string, no parity callback, no
host branch/sector/frame/scheduler query, and one reference allocation.  The
fixed reference, blanks, finite cutoff, factor order, frame, and Route-A
compiler presentation remain supplied.  **No schedule is time.**

That zero is a circuit-composition identity, not independent empirical evidence
for the ingredients used to define it.  Its evidentiary force comes from the
separate encoder isometry/pivot/rank tests, literal M2 placement and routing,
and materialized target-state tests below.  Cycle 555 does not cite
`W G_target W^dagger` alone as proof that `W` or `G_target` is admissible.

This is a complete finite-network compiler theorem through global `N<=2`, not
an all-sector, all-size, prepared-reference, or autonomous-causal theorem.

## Exact global encoder

### One-bit preparation

The complete global `N<=2` cutoff means every individual cell contains zero,
one, or two particles.  Those 22 local occupation words all have two selected
terms, so the generic three-M2 branch register and its six-ray special cases
are unnecessary on this domain.  Each cell uses one branch M2 and 22 exact
q-word-controlled Givens rotations.

| control | L3 | held L4 |
|---|---:|---:|
| one-bit Givens | 594 | 1,408 |
| maximum preparation residual | `1.5700924586837752e-16` | same |
| maximum inverse residual | `2.220446049250313e-16` | same |
| deleted-Givens minimum ray residual | `0.7653668647301795` | same |
| minimum branch-one amplitude | `0.7071067811865475` | same |

Representative phases are folded into the branch amplitudes exactly as in
Cycle 533.  Deleting one preparation Givens changes the intended code ray.

### Companion-pivot theorem and global rank census

The auxiliary X difference between the two terms of a local word defines a
GF(2) column `d_c(q_c)`.  Exhaustive testing gives:

| control | L3 | held L4 |
|---|---:|---:|
| unique companion pivots | 27 | 64 |
| missing own-pivot failures | 0 | 0 |
| foreign-pivot failures | 0 | 0 |
| branch-zero pivot flips | 0 | 0 |
| exhaustive global q columns | 13,204 | 73,921 |
| minimum rank of `D(q)` | 27 | 64 |
| rank failures | 0 | 0 |

The rank digests are

```text
L3  dae5f98652d5884e717095c495b0d8d8b846a38e976b71f8d3e9951fd90dd6e3
L4  89c0ba5674acd9dd8b038a629158f19d2bf8aed8bd214fbf4268a31347806d92
```

The pivot theorem is stronger than bare full rank: the pivot submatrix is the
identity for every lawful q word.  Thus the inverse is local and q-independent.
The companion physical M2 and its branch M2 are adjacent in the integer
microgrid.  Deleting one companion CNOT leaves branch leakage norm at least
`1/sqrt(2)`.

### Gram, inverse, and support

Every local two-ray vector is normalized.  Their tensor branch preparation is
normalized without materializing the conceptual `2^27` or `2^64` branch
products.  `SELECT` and the companion CNOTs are unitary.  Distinct logical
columns remain orthogonal in the persistent q register.  Therefore

```text
E_network^dagger E_network = I,
W_network^dagger W_network = I
```

exactly on all declared columns.  The largest accumulated numerical column-
norm errors are `5.995204332975845e-15` at L3 and
`1.4210854715202004e-14` at held L4; the exact Gram off-diagonal and circuit
inverse residuals are zero.

The compiler uses 44 selected lookup entries per cell.  It has 1,188 entries
and 13,347 controlled single-Pauli factors at L3; held L4 has 2,816 entries
and 31,240 factors.  A single representative has support at most 21 M2 and
fine-microgrid L1 radius at most 16.  The full selected/reference physical
allocation is 23 M2 per coarse cell.  Persistent q adds six and the branch
adds one, so physical storage remains constant per cell.

### Local constraints and global lawful domain

Every selected term on every declared local word is checked against all
Cycle-269 port constraints, local checks, and fixed-Wilson-sector operators.
The runner executes 192,456 port and 356,400 fixed-check commutators at L3,
and 1,081,344 port and 1,990,912 fixed-check commutators at held L4.  Failures
are zero.  All selected role pairs also pass.

Auxiliary legality is locally enforced by those port/check constraints and
the one companion-branch relation per cell.  The global `N<=2` lawful-domain
cutoff is checked by one reversible binary counter over the persistent q M2,
copying the accept bit and reversing the counter.  This counter is a code-
domain test.  It is not consulted by the CAR update and is not a global parity
service.  The encoded global legality projector is

```text
C_network = W_network
            [Pi_(N<=2) tensor |Omega_fixed,0_branch,work><...|]
            W_network^dagger.
```

It is one global legality object, not a product of patch projectors.  The
fixed-reference and blank-input factors are supplies, not consequences of the
number counter.

## Literal locality and proper-cubic transport

All 23 selected/reference physical M2 and six q M2 per cell receive their
inherited distinct microgrid coordinates.  Each branch M2 is placed one
fine-grid `+x` edge from its own companion in the base chart.  The actual edge
is transported under frames.  A small conjunction workspace and the reversible
number counter are reused sequentially.

The train and held layouts test every logical pair required by branch
preparation, SELECT, decoding, and legality.  Every remote one-/two-M2 macro
uses a deterministic periodic Manhattan route, an exact core, and the reverse
route.  No blank bus is assumed.  All actual route edges are nearest neighbour.

The complete ordered compiler family is transported through all 24 proper-
cubic frames: cell addresses, q directions, physical Pauli factors, companion
edges, factor order, Route-A order, and actual NN routes are mapped rather than
re-sorted.  All 576 frame products close.  There is no runtime frame selector.
This is covariance of a transported circuit family, not one raw gate list
invariant in every chart.

The fixed cell-factor order remains explicit supplied compiler presentation
data.  It is not a Jordan-Wigner mode string and does not provide parity signs
to the runtime, but Cycle 555 does not claim to derive or retire that
presentation choice.

## Frozen Route-A network update and contact-sensitive evidence

Cycle 551 is hash-pinned and its Route-A physical-footprint coloring rule is
rerun on L3 and held L4.  Both networks contain every coarse center once.  The
frozen rule uses ten support-disjoint colors at each size.  It provides a
fixed decoded-runtime order; it is not called autonomous time.

Unlike Cycle 551's network-wide one-particle regression, Cycle 555 materializes
a complete global `N<=2` state representation:

```text
(vacuum scalar, all one-particle amplitudes, full antisymmetric pair matrix).
```

Each local coin acts on both indices by exterior lift, each seam swaps its two
modes on both indices and therefore retains the CAR sign, and contact phases
every same-cell pair amplitude.  Thus all 13,204 L3 or 73,921 held-L4
amplitudes participate in the deterministic probe.  The tests include both
repeat and reverse sweeps, deletion of one star, deletion of all contact, and
all 24 frame-transported full `N<=2` sweeps.

The initial construction residuals are:

| residual | L3 | held L4 |
|---|---:|---:|
| maximum complete-N2 norm | `2.220446049250313e-16` | same |
| maximum complete-N2 inverse | `3.369905720946661e-15` | `3.557034954898172e-15` |
| delete one star | `0.6441817724023454` | `0.430327267330417` |
| delete all contact | `0.1778509956372444` | `0.1188079476663609` |
| maximum complete-N2 frame covariance | `3.757813366489876e-16` | `3.849733568341742e-16` |

The final cold run is the packaging authority for exact digests and resources.

Cycle 548's complete six-cell `N=0,1,2` matrices are replayed separately.
They preserve the Cycle-219 mass fixture, nontrivial contact, all five seams
of the adjacent double star, the shared-seam deletion, both update orders,
inverse, and all-24/576 covariance.  This keeps local fixture diagnostics
distinct from the new complete-network multiparticle state test.

### Materialization and macro boundary

The physical conjugation is defined gatewise, not as a dense off-code matrix:

- the 27/64 companion-to-branch CNOT calls, their distinct endpoints, and
  their one-edge routes are literal and materialized;
- every cell's 22 two-component branch vectors and Givens matrices is
  numerically materialized, and every selected representative's actual X/Z
  factors and support are enumerated;
- the equality-controlled Givens, controlled selected X/Z factors, clean
  conjunctions, exact Toffoli reductions, and reversed remote routes are exact
  inherited one-/two-M2 macro expansions; the runner counts and routes every
  required logical pair but does not allocate every repeated primitive row;
- the Cycle-551 local Route-A physical templates and actual footprint coloring
  are rebuilt at L3 and held L4, while their translated per-star repeated gate
  programs remain exact macro placements rather than one enormous emitted
  gate list;
- the full global `N<=2` target state, including every vacuum/single/pair
  amplitude, is materialized and evolved; the full `73,921 x 73,921` target or
  physical unitary matrix is not materialized; and
- `G_physical=W_network G_target W_network^dagger` is therefore a defined
  concatenation of admissible physical macros.  Its zero intertwiner residual
  follows from the separately established `W_network^dagger W_network=I` and
  number preservation.  It is not counted as a second independent validation
  of those facts.

This boundary is also why “literal physical circuit” does not mean “billions
of duplicated output rows.”  Every macro has a finite exact one-/two-M2
decomposition and tested NN endpoints; repeated rows are intentionally not
used as a proxy for additional physics evidence.

## Product-of-patch comparator

A product of per-star encoders is not silently relabeled as `E_network`.
Every oriented star has four cell incidences, so tensorizing all star patches
would use four q copies and four branch copies per physical cell on average.
It would require 27 or 64 nominal reference allocations instead of one.

More decisively, the patch native-role sets overlap.  A disjoint tensor
version duplicates those physical roles and loses one persistent ownership
graph; an overlapped version cannot use independent patch decoders.  Cycle
533's exact comparator already found 22,272 failures in 51,200 one-cell
decoder tests after a joint product.  Cycle 555 uses that witness only against
the independent patch-decoder ansatz, not against the global construction.

The direct encoder instead owns each q, reference role, companion, and branch
once.  Its local companion theorem remains valid after every other cell's
selected factor.  The patch comparator is therefore a controlled failed
alternative, not a no-go and not constitutional evidence.

## Exact ownership, inverse, leakage, and deletions

There is one persistent 6-M2 q word per coarse cell and one global fixed-
Wilson/reference allocation.  The encoder adds one branch M2 per cell.  Clean
conjunction, route, and number-counter work is reused only sequentially.

The reverse schedule daggers each Givens, reverses selected-factor order,
reverses every route, and reapplies the companion CNOT.  Terminal branch,
route, and counter leakage is zero on the lawful domain.  Intermediate gates
may leave the code space; the theorem is terminal.

Load-bearing deletions are separated:

- deleting one branch Givens changes the code ray by at least
  `0.7653668647301795`;
- deleting one companion CNOT leaves branch leakage `1/sqrt(2)`;
- deleting one star gives the complete-network residuals above;
- deleting all contact gives nonzero complete-network pair residuals;
- deleting the shared seam retains Cycle 548's nonzero exact residual;
- deleting a legality count condition accepts a named out-of-domain word; and
- deleting a reverse route leaves displaced physical data.

## Supplied structure and novelty boundary

Supplied rather than derived are:

1. the fixed-Wilson reference and its initial preparation;
2. blank branch, conjunction, route, tag, and number-counter M2;
3. the strict-pinned selected coefficients and physical Pauli representatives;
4. exact branch, coin, contact, and routing-core analog angles;
5. the complete global `N<=2` lawful-domain cutoff;
6. finite periodic L3/L4 boundaries and the base compiler chart;
7. the transported cell-factor order and compile-time proper-cubic frame; and
8. Cycle 551 Route-A orientation, footprint colors, origin, and layer order.

New here are the all-cell one-bit reduction, unique companion-pivot theorem,
exhaustive 13,204/73,921 rank census, one-CNOT-per-cell global decoder, one
global legality object, direct ownership audit, constant-per-cell layout,
complete-network contact-sensitive `N<=2` state evolution, held-size full-N2
covariance, and explicit product-of-patch comparator.

The result is not a reference or blank genesis theorem, an `N>=3` compiler,
an arbitrary-size theorem, an order-independence theorem, autonomous causal
time, realized history, a Record theorem, Born probability, gravity/source
response, a minimum-content theorem, or an axiom.  Thirring machinery is
neither used nor compared.

## Dependency ledger and maturity

- `C_ref`: unchanged.  One fixed reference, blank genesis, exact coefficient
  data, factor order, frame, and Route-A presentation remain supplied.
- `C_num`: advances materially.  The selected compiler now covers complete
  global `N=0,1,2` on 27 and 64 cells.  `N>=3`, number change, and arbitrary
  size remain open.
- `C_wrap`: unchanged.  Factor order, colors, and layers are compiler order;
  no schedule is time, duration, energy, rate, Record, or realized history.
- `C_int`: advances materially.  A contact-sensitive global `N<=2` update,
  seams, inverse, deletion, and covariance now sit behind one exact encoder.
- `C_local`: advances materially.  Cycle 551's supplied-global-encoder terminal
  closes at train L3 and held L4 through complete `N<=2`, with one local CNOT
  decoder per cell and no parity service.
- `C_source`: unchanged.

No five-lane maturity score changes are proposed relative to the current
campaign baseline: operational quantum/records `3.4/5`, causal time `1.8/5`,
inertia/matter `4.2/5`, gravity/source `2.1/5`, and Born/probability `2.0/5`.
This is a compiler import-retirement result, not a new cross-lane closure.
There is no shared obstruction and **no axiom pressure**.

## No-go discipline N1–N8

The refreshed `origin/main` no-go-discipline skill and proof-search governance
were applied.  Broad impossibility, minimum-content, and axiom-pressure gate:
**FAIL / DO NOT SHIP**.  The result is constructive and several independent
extensions remain open.

### N1 — alternative-route normalization

| family | object / mechanism / terminal | disposition |
|---|---|---|
| global companion pivots | complete selected network / one local pivot per cell / exact branch return | **ATTEMPTED: succeeds N<=2** |
| exhaustive GF(2) inverse | branch-difference matrix / full-rank decoder / exact injectivity | **ATTEMPTED: succeeds; collapses to pivots** |
| product of patch encoders | tensor or overlapped patch codes / independent decoders / one network isometry | **ATTEMPTED: fails only as this ansatz** |
| joint network permutation role | symmetric global order register / coherent order sectors / order-neutral encoder | **open** |
| transported encoder slot | locally reused branch/order role / staged SELECT and return / scalable higher sector | **open** |
| direct rough carrier | Cycle-532 target-times-gauge code / physical rough preparation / recurrent network | **partial; target exact, preparation absent** |
| measurement/reset stabilization | local syndromes / prepare reference and renew blanks / convergence | **open** |

The families differ in primary encoded object, invariant, and terminal.  One
strong positive route and four open/partial routes prohibit a broad negative.

### N2 — wall-independence audit

The collapsed residual walls are:

```text
W_ref     fixed-reference genesis,
W_blank   blank-work genesis and renewal,
W_number  global N>=3 sectors and number change,
W_order   retirement of compile-time chart/factor presentation,
W_auto    autonomous local update-choice/causal law,
W_bridge  selected-carrier <-> rough-carrier transduction.
```

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_ref,W_blank` | no | no | yes |
| `W_ref,W_number` | no | no | yes |
| `W_ref,W_order` | no | no | yes |
| `W_ref,W_auto` | no | no | yes |
| `W_ref,W_bridge` | no | no | yes |
| `W_blank,W_number` | no | no | yes |
| `W_blank,W_order` | no | no | yes |
| `W_blank,W_auto` | no | no | yes |
| `W_blank,W_bridge` | no | no | yes |
| `W_number,W_order` | no | no | yes |
| `W_number,W_auto` | no | no | yes |
| `W_number,W_bridge` | no | no | yes |
| `W_order,W_auto` | no | no | yes |
| `W_order,W_bridge` | no | no | yes |
| `W_auto,W_bridge` | no | no | yes |

The global `N<=2` selected encoder, local auxiliary constraints, finite Route-A
recurrence, and literal routing are closed here and are not renamed as walls.

### N3 — hidden-wall scan

The required phrases and close variants were scanned.  Fixed reference,
blanks, persistent q input, selected coefficient table, exact angles, cutoff,
finite sizes, chart, factor order, frame, router, number-counter program,
Route-A orientation/colors/origin/order, and carrier are explicit supplies.
“By construction” is not used to discharge a missing obligation.  “Physical”
means an M2 circuit placement; it does not silently mean initialized or
autonomous.

### N4 — residual matching

| witness | exact source | residual attacked | Cycle-555 use | match? |
|---|---|---|---|---:|
| Cycle 551 global encoder boundary | `scripts/physical_boundary_aware_multistar_recurrence_tournament_cycle551_2026_07_21.py:986` | one global selected encoder/reference allocation | exact `E_network` terminal | yes |
| Cycle 548 fixed six-cell decoder | `scripts/physical_adjacent_star_recurrence_tournament_cycle548_2026_07_21.py:164` | bounded local selected isometry | mechanism comparator only | no for global closure; dropped as proof |
| Cycle 533 one-cell decoder failure | `scripts/physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py:390` | independent local decoder after product | patch-product comparator | yes only for that ansatz |
| Cycle 540 seam identity via Cycle 548 | `scripts/physical_adjacent_star_recurrence_tournament_cycle548_2026_07_21.py:835` | literal CAR FSWAP and tracked phase | local seam fixture | yes |
| Cycle 532 target times gauge | `scripts/physical_adjacent_star_recurrence_tournament_cycle548_2026_07_21.py:1332` | common CAR target | selected-to-rough transducer | no; dropped as bridge evidence |

Only exact residual matches support closure.  Local patch success is not used
as the global encoder proof; the new pivot census is.

### N5 — rhetoric audit

| resolution | tested statement |
|---|---|
| one selected ray | actual Pauli support, amplitude, companion pivot |
| one cell | all 22 legal words, local constraints, branch inverse |
| one patch product | duplicated ownership and decoder-overlap comparator |
| complete L3/L4 network | all global q columns, rank, Gram, full-N2 state sweep |
| all frames | 24 transported circuits and full-N2 sweeps; 576 group products |
| global N>=3 | not tested; explicitly open |
| arbitrary size | not tested; no uniform theorem |
| autonomous law | not tested; compiler order is not time |

“No global parity service” is scoped to the encoder/update mechanism actually
tested.  The reversible number counter checks only lawful-domain membership.

### N6 — partial-closure path

Retain the companion decoder and widen the first new local case: the eight
three-particle words have six selected rays.  Test whether companion plus flag
roles give a bounded multi-pivot code and local erasure before increasing the
global number cutoff.  Independently, a symmetric local order field can attack
`W_order`, a reversible phase/token rule can attack `W_auto`, and stabilization
can attack reference and blank genesis.  These are import-retirement routes,
not evidence for a new axiom.

### N7 — hostile steelman

> A hostile reviewer should reject “global physical universe” or “all-sector
> compiler.”  The theorem starts with a supplied fixed-Wilson ray, blank work,
> finite L3/L4 boundaries, a global `N<=2` cutoff, and a transported factor and
> Route-A order.  At `N=3`, one cell can occupy a six-ray word and the one-bit
> pivot proof no longer applies.  But that same boundary defeats a no-go: the
> six-ray table already supplies concrete companion/flag structure, joint-role
> and transported-slot routes remain open, and the exact one-CNOT theorem shows
> that the former global decoder wall was an implementation wall, not a
> substrate obstruction.

### N8 — cross-cycle echo

Cycles 319/324 replaced incompatible independent roles with joint roles or
slots.  Cycle 533 replaced invariant one-cell decoding with a joint decoder.
Cycles 539/545 decoded a shared patch once.  Cycle 548 widened to adjacent
stars and Cycle 551 closed three finite schedulers while leaving `E_network`
supplied.  Cycle 555 finds that on complete global `N<=2` the apparent global
decoder is actually one local companion CNOT per cell.  The repeated echo is
constructive retirement by a better relational auxiliary, not constitutional
failure.

No route-independent obstruction, minimum-content theorem, constitutional
change, or axiom pressure survives N1–N8.

## Disposition and next campaign

Retain Cycle 555 as the strongest selected-carrier compiler result:

- one complete periodic-network `E_network`, not patch products;
- exhaustive complete global `N<=2` at L3 and held L4;
- one local companion CNOT decoder per cell;
- exact Gram, inverse, legality, and ownership;
- constant physical M2 overhead per cell and explicit NN routes;
- frozen Route-A contact-sensitive full-N2 recurrence;
- all-24/576 transported covariance; and
- exact mass, contact, seam, deletion, and supply boundaries.

The optimal next campaign is a local six-ray `N=3` decoder tournament.  Compare
two companion/flag pivot bits, a bounded qutrit-style branch code, and a
transported slot, first on one cell and then complete global `N<=3` at the
smallest feasible network.  Do not conflate that sector-widening problem with
reference genesis, order retirement, scheduler autonomy, or the rough-carrier
bridge.

## Cold certificate

The integrated pre-freeze run passed all **11/11** aggregate predicates in
`58.24885183398146` internal seconds (`59.69` timed wall seconds), reached
`163,627,008` maximum RSS bytes, and reported zero process swaps.

The L3 layout used 818 compiler-live M2, 3,382 required logical-wire pairs,
12,261 distinct route edges, and maximum route length 57.  Held L4 used 1,929
live M2, 8,442 pairs, 32,326 distinct route edges, and maximum route length 95.
All base and mapped route-edge failures were zero.

The frozen Route-A ordered-list digests were:

```text
L3  ffee0cb83cb2228955d0d5eb8ffe6bb252e5528a4265cd30edde4ed2e840c75c
L4  1cacbccd305bd14ac041432bce3343f74971b702a885e8a31c6befdefad8f799
```

The product-of-patch census found 1,134 overlapping native-role assignments
and 324 overlapping star pairs at L3; held L4 found 2,688 and 1,184.  Both
patch products would use exactly four times the q and branch allocations of
the direct global encoder.

The final post-note cold certificate is regenerated after this note and runner
are frozen.  Only that final JSON and hashes are packaging evidence.
