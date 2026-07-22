# Physical global N3 returned-slot compiler — Cycle 560

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py`

## Result

Cycle 560 lifts Cycle 557's bounded six-ray inverse to one complete periodic
selected-carrier encoder through global `N<=3`.  It first passes the required
exhaustive three-cell gate and only then applies a local decoder theorem to all
complete columns at train L3 and held L4.

The result is a Pareto pair rather than one falsely dominant route:

- **Route B** is the leaner literal physical layout.  It assigns a locally
  constrained six-M2 one-hot block per cell and uses 53 compiler-live M2 per
  coarse cell including physical/reference, q, and clean work.
- **Route C** proves the returned-slot terminal.  One logical three-M2 slot is
  prepared, selected, decoded to `000`, and advanced to the next cell through
  a supplied dedicated blank three-lane rail.  Its literal rail raises the
  total to `114.777...` live M2/cell at L3 and `111.59375` at held L4.

Thus Route C saves active branch state but not literal supplied sites; no
resource-minimum claim is made.  Both routes have exact Gram, inverse, and
terminal leakage on the declared complete global code space.

| network | cells | CAR modes | N=0 | N=1 | N=2 | N=3 | complete columns |
|---|---:|---:|---:|---:|---:|---:|---:|
| train L3 | 27 | 162 | 1 | 162 | 13,041 | 695,520 | **708,724** |
| held L4 | 64 | 384 | 1 | 384 | 73,536 | 9,363,584 | **9,437,505** |

At L3, Cycle 560 separately materializes a dense antisymmetric state with all
708,724 complete `N=0,1,2,3` amplitudes nonzero, evolves the actual free,
seam, and pair-contact target update, reverses it, deletes one star, deletes
all contact, and transports the full state through all 24 proper-cubic frames.
With `W_network` either exact encoder and `G_target` that number-preserving
update, the physical circuit is

```text
G_physical = W_network G_target W_network^dagger,
E_network G_target = G_physical E_network.
```

The code-space intertwiner residual is exactly zero.  `W_network` is audited
before the update, the complete-N3 `G_target` state evolution is independently
materialized, and `G_physical` is constructed as a literal physical macro
concatenation.  No same-path vector subtraction is used as intertwiner
evidence.  As in Cycle 555, the zero follows from the separately certified
`W_network^dagger W_network=I` and number preservation; it is not independent
evidence for the ingredients used to define the circuit.

The held-L4 result is deliberately separated: the complete global encoder and
local-decoder transfer are exact there, but a dense L4 `N=3` update was not
materialized.  One L4 triple tensor is `905,969,664` bytes; the four live
tensors needed by the current covariance implementation require at least
`3,623,878,656` bytes and exceed the 2.9-GB guard.  This is an implementation
boundary, not a physics obstruction.

There is no parity callback, no global Jordan-Wigner string, no retained prior
branch, and no runtime host sector, order, frame, or scheduler selector.  The
lexicographic selected-factor order, Route-A update order, fixed reference,
blank rail/work, cutoff, tables, angles, finite sizes, chart, and router remain
supplied.  **No schedule is time.**

## Three-cell proof gate

The adjacent line `((0,0,0),(1,0,0),(2,0,0))` contains 18 CAR modes.  The
complete total-`N<=3` domain has 988 logical columns.  Its exact selected-ray
census is:

| local ray tuple | columns | terminal rays |
|---|---:|---:|
| `(2,2,2)` | 964 | 7,712 |
| `(6,2,2)` | 8 | 192 |
| `(2,6,2)` | 8 | 192 |
| `(2,2,6)` | 8 | 192 |
| **total** | **988** | **8,288** |

The physical prefix tables contain 2,008 rows after cell 0, 4,080 after cell
1, and 8,288 after cell 2.  For every q word and every coherent prior ray
choice, the current cell's own 14 native physical roles determine the current
slot label.  Conflicts are zero at all three prefixes on L3 and held L4.

The larger rolling comparator uses 26 roles on each two-cell window; its
conflicts are also zero.  Route B's final joint-pattern comparator uses 36
native roles at periodic L3 and 38 at held L4; its full branch-tuple collisions
are zero.  Since the smaller current-cell pattern already closes, neither the
rolling roles nor a new gauge register is promoted to a required supply.

The third-cell decoder therefore depends only on persistent q plus the current
bounded physical pattern after two cells.  It does not retain either prior
branch, query a host sector, ask for parity, or call an ordering service.  The
weakest nonzero three-cell product ray is exactly `1/sqrt(24) =
0.20412414523193145`; deleting its decoder row leaves that nonzero residual.
The maximum product-column normalization error is
`6.661338147750939e-16`.

The frozen three-cell decoder digests are:

```text
L3  af528b91e3f014bb75b2152ed32adc0bdc1d8f5675f4c958e0c2fda1279ce389
L4  0f663e7a74064ae1bfff9c7ddec7b2e3008ef817254ed1e457c82435f495e512
```

## Complete-global decoder theorem

Every six-mode word through local `N=3` is either:

1. one of 34 ordinary two-ray words, or
2. one of eight special three-particle six-ray words.

For every ordinary word, branch zero does not flip its own companion and
branch one flips it exactly once.  Exhaustive testing of every selected ray of
every `N<=3` word at every source cell finds zero flips on every foreign
companion.  Therefore an ordinary current branch is erased locally regardless
of all preceding coherent branch choices.

For a special six-ray current word, all three particles already occupy that
cell.  The complete global `N<=3` cutoff therefore forces every other q word
to vacuum.  Both selected vacuum rays at every foreign cell flip none of the
current cell's 14 native decoder roles.  The six one-cell patterns remain
distinct after any preceding vacuum factors, so the 48-row table (eight words
times six rays) erases the special slot locally.

These two exhaustive local statements cover every global occupation
partition:

| partition | L3 columns | held-L4 columns |
|---|---:|---:|
| vacuum | 1 | 1 |
| one particle | 162 | 384 |
| two in one cell | 405 | 960 |
| one in each of two cells | 12,636 | 72,576 |
| three in one cell | 540 | 1,280 |
| two plus one | 63,180 | 362,880 |
| one in each of three cells | 631,800 | 8,999,424 |

The partition sums equal the binomial sector dimensions exactly.  This is a
complete proof by occupation decomposition, not an iteration over 9,437,505
held-L4 q words and not a sampling argument.

Each local coefficient vector is normalized, every Givens/SELECT/decoder is
reversible, and persistent q makes distinct logical columns orthogonal.  Thus

```text
E_network^dagger E_network = I,
W_network^dagger W_network = I
```

exactly on the full declared global code space.  No conceptual exponential
product of branch rays is materialized or required by the proof.

## Route B — leaner one-hot compiler

Route B initializes one of six branch rails, applies exact one-excitation
Givens rotations, controls the selected physical Pauli factors, and flips the
active rail back to the all-zero blank from the exhaustive local physical
pattern.  The number-one constraint during selection and terminal number-zero
constraint are bounded six-M2 predicates.

| control | L3 | held L4 |
|---|---:|---:|
| branch M2 | 162 | 384 |
| exact Givens | 1,998 | 4,736 |
| maximum preparation residual | `1.5700924586837752e-16` | same |
| maximum inverse residual | `2.4196749845665633e-16` | same |
| deleted-first-Givens residual | `0.41744238123296284` | same |
| deleted ordinary companion decoder | `1/sqrt(2)` | same |
| deleted special decoder row | `1/sqrt(6)` | same |
| terminal branch leakage | 0 | 0 |

Its literal layouts use 1,431 live M2 at L3 and 3,392 at held L4, exactly 53
per coarse cell.  These include 23 physical/reference M2, six persistent q,
six branch, and 18 clean conjunction-work M2 per cell.

## Route C — one logical returned slot

Route C encodes ray labels `0,...,5` in three M2 and rejects `110` and `111`
with a bounded local validity predicate.  The program at every cell is:

1. check the slot is blank/valid;
2. prepare it from the current persistent six-M2 q word;
3. apply slot-controlled selected physical Pauli factors;
4. erase an ordinary label from the companion or a special label from the
   current cell's 14-role physical pattern;
5. check `000`; and
6. advance the logical slot to the next station on a dedicated blank rail.

The selected-factor order is the same lexicographic base-chart order retained
by Cycle 555.  Consecutive factors are connected by a role-avoiding three-lane
rail with maximum physical segment length 48 at both L3 and held L4.  The
entire rail is reversed by `W_network^dagger`.  Its state is returned blank at
every station; its many blank carrier sites are an explicit supply, not hidden
inside the phrase “one slot.”

| control | L3 | held L4 |
|---|---:|---:|
| logical active slot | 3 M2 | 3 M2 |
| physical slot stations | 81 | 192 |
| dedicated blank rail sites | 1,830 | 4,134 |
| clean local work | 486 | 1,152 |
| total compiler-live M2 | 3,099 | 7,142 |
| live M2 per cell | `114.77777777777777` | `111.59375` |

The rail is why Route C is not called physically leaner.  It nevertheless
closes the requested coherent returned-slot mechanism with no prior-branch or
host query, and its overhead remains bounded per cell across train and held
sizes.

## Selected support and locally enforced constraints

The global selected table has 3,132 entries and 56,835 controlled single-
Pauli factors at L3; held L4 has 7,424 entries and 132,936 factors.  One
representative has support at most 32 M2 and fine-microgrid L1 radius at most
16.  The selected/reference union is 23 M2 per cell.

Every selected representative on every one of the 42 local words at every
cell is tested against every Cycle-269 port constraint and every inherited
local/fixed-Wilson check:

| audit | L3 | held L4 |
|---|---:|---:|
| selected entries | 3,132 | 7,424 |
| port commutator cases | 507,384 | 2,850,816 |
| port failures | 0 | 0 |
| fixed-check cases | 939,600 | 5,248,768 |
| fixed-sector failures | 0 | 0 |

Route B's number predicate and Route C's three-bit validity/blank predicate
are routed inside each bounded compiler block with clean conjunction work.
They enforce the declared auxiliary code space; they do not derive blank
genesis, autonomous stabilization, or a physical penalty energy.

The complete global `N<=3` cutoff is a supplied lawful-domain restriction.
It is not queried by the encoder update and is not a global parity service.
Number change and higher sectors remain open.

## Literal locality and proper-cubic covariance

Every physical/reference, q, branch/slot-station, rail, and clean-work M2 has a
distinct integer microgrid coordinate.  Required local equality, preparation,
SELECT, decoder, and validity pairs are expanded through deterministic exact
nearest-neighbour route/core/reverse-route macros.  Slot-rail SWAPs use a
dedicated role-avoiding path and are reversed by the encoder inverse.

| size / route | local macro pairs | distinct NN edges | maximum macro path | maximum rail segment |
|---|---:|---:|---:|---:|
| L3 / B | 78,588 | 53,977 | 32 | 0 |
| L3 / C | 72,432 | 53,550 | 48 | 48 |
| held L4 / B | 181,864 | 119,994 | 32 | 0 |
| held L4 / C | 167,464 | 119,169 | 48 | 48 |

Coordinate, wire, rail-role, and nearest-neighbour failures are zero.  The
bounded maximum path is unchanged from L3 to held L4.

The actual ordered circuits, wires, and route edges are transported through
all 24 proper-cubic frames.  Mapped-wire injection and mapped-NN failures are
zero; all 576 frame products close.  The strict-pinned selected-shell
isometry/stream/coin/contact/composition covariance replay also passes at both
sizes with maximum residual `1.5574068580638927e-15`.

This is covariance of a transported circuit family.  It does not retire the
base factor order or provide a runtime frame selector.

## Complete global N3 free-plus-contact update at L3

The L3 target state stores a vacuum scalar, 162 one-particle amplitudes, a
fully antisymmetric `162 x 162` pair tensor, and a fully antisymmetric
`162 x 162 x 162` triple tensor.  All 13,041 independent pair and 695,520
independent triple coordinates are nonzero.  Its norm counts each independent
antisymmetric coordinate once.

The free coin acts on all tensor indices by exterior lift.  Each seam swaps
its two modes on every index, retaining the CAR sign through antisymmetry.
The Cycle-230 pair contact multiplies every occupied same-cell pair; a triple
in one cell therefore receives three pair phases.  This is the exterior/pair
lift of the retained free-plus-contact law, not a new three-body interaction.

The frozen Cycle-551 Route-A actual-physical-footprint scheduler contains all
27 stars in ten colors.  It supplies the target update order; it is not called
causal time.  The complete-state tests give:

| residual | value |
|---|---:|
| norm | `2.220446049250313e-16` |
| inverse | `2.6141032400394886e-15` |
| delete one star | `0.7746006701907014` |
| delete all contact | `0.32770199861425353` |
| delete all contact, triple sector only | `0.32672782293697983` |
| maximum all-24 covariance | `4.75255665087917e-16` |
| covariance failures | 0 |

Pair and triple antisymmetry are also explicitly checked after the sweep.  The
one-particle mass network controls pass separately, keeping the Cycle-219
mass fixture distinct from the new multiparticle state test.

The complete target state is materialized, but neither the
`708,724 x 708,724` target matrix nor a dense physical update matrix is.  The
one-/two-M2 physical gate macros, selected factors, decoders, coordinates, and
routes define `W G_target W^dagger` gatewise.

## Mass, contact, seam, inverse, leakage, and deletion inventory

The strict inherited fixture replay remains green:

- Cycle-219 rest-mass source `0.4534056541748851`, compiled value
  `0.453405654174885`, uniform residual `8.7159799596118e-16`;
- Cycle-230 contact factorization residual `2.149937642474629e-15` and 4,047
  nontrivial contact columns;
- all three axis-seam braid residuals exactly zero over 4,096 complete Fock
  columns each; and
- the event-current adapter's 65,536 tests with zero truth, continuity,
  terminal-work, recurrence, and Fredkin-basis failures.

Returning a compiler slot is not called a Record.  Wrapped phase is not called
physical energy, a generator element is not called a rate, and a gate or rail
count is not called duration.

Load-bearing deletions are separated:

- deleting the first branch/slot Givens leaves residual at least
  `0.41744238123296284`;
- deleting an ordinary companion decoder leaves `1/sqrt(2)` leakage;
- deleting a special local decoder row leaves `1/sqrt(6)` local leakage;
- deleting the weakest three-cell terminal row leaves `1/sqrt(24)`;
- deleting one target star leaves `0.7746006701907014`;
- deleting all target contact leaves `0.32770199861425353`; and
- inherited seam and route-reversal deletions remain nonzero.

Terminal branch/slot, validity, conjunction, route, and work leakage is zero on
the declared code space.

## Materialization, supplies, and novelty boundary

Materialized here are every local `N<=3` coefficient vector and Givens
schedule; every selected representative, support, constraint commutator, and
decoder pattern at every L3/L4 cell; all 988 three-cell columns and 8,288
terminal rays; both full network occupation-partition censuses; all literal
M2 placements and required routes; and every complete L3 `N<=3` target-state
amplitude under update, inverse, deletions, and 24 frames.

Supplied rather than derived are:

1. the fixed-Wilson reference and its preparation;
2. blank one-hot, slot-station/rail, conjunction, and routing M2;
3. persistent q and the complete global `N<=3` lawful cutoff;
4. strict-pinned selected coefficients and physical Pauli representatives;
5. exact Givens, coin, contact, and routing-core analog angles;
6. finite periodic L3/L4 boundaries and the base chart;
7. lexicographic selected-factor order and Cycle-551 Route-A update order; and
8. compile-time proper-cubic frame and deterministic router.

New here are the exhaustive three-cell returned-slot terminal, the foreign-
invariant complete-global decoder theorem, full L3/held-L4 occupation transfer,
one logical three-bit slot rail, honest Route-B/Route-C physical Pareto audit,
complete dense L3 triple-sector free/contact update, all-24 full-N3 covariance,
and the explicit held-L4 memory boundary.

The result is not an all-sector, number-changing, arbitrary-size, reference-
genesis, blank-renewal, order-independent, autonomous-causal, realized-history,
Born/probability, gravity/source, selected-to-rough transduction, minimum-
content, no-go, or axiom result.  Thirring machinery is neither used nor
compared.

## Dependency ledger and maturity

- `C_ref`: unchanged.  Fixed reference, blank rail/work, q, cutoff, tables,
  angles, factor/update orders, finite frame, and router remain supplied.
- `C_num`: advances materially.  One exact selected encoder covers complete
  global number-preserving `N=0,1,2,3` on L3 and held L4; the dense physical
  update is tested at L3.  Number change and `N>=4` remain open.
- `C_wrap`: unchanged.  Factor, scheduler, and slot-rail sequence are compiler
  order; no schedule is time, duration, Record, or realized history.
- `C_int`: advances materially.  A contact-sensitive complete global
  `N<=3` L3 update, inverse, deletions, and all-24 covariance now sit behind an
  exact physical encoder.
- `C_local`: advances materially.  The bounded three-cell returned-slot
  terminal becomes a complete-network theorem through `N=3`.
- `C_source`: unchanged.

Revised maturity scores are operational quantum/records `3.5/5`, causal time
`1.8/5`, inertia/matter `4.3/5`, gravity/source `2.1/5`, and Born/probability
`2.0/5`.  Operational and inertia each rise `0.1` because a new complete
global multiparticle sector and contact-sensitive update close; no time,
source, or probability lane closes.  There is no shared substrate obstruction
and **no axiom pressure**.

## No-go discipline N1–N8

The refreshed `origin/main` no-go-discipline skill and proof-search governance
were applied.  Broad impossibility, minimum-content, and axiom-pressure gate:
**FAIL / DO NOT SHIP**.  Multiple constructive routes succeed and every
remaining wall has a concrete attack path.

### N1 — alternative-route normalization

| family | primary object / mechanism / terminal | disposition |
|---|---|---|
| Route C returned slot | three-bit logical branch / local pattern erasure plus blank rail / per-cell return | **ATTEMPTED: succeeds globally through N=3** |
| Route B one-hot | six-rail local code / number-one preparation plus pattern erasure / all-zero return | **ATTEMPTED: succeeds and is physically leaner** |
| larger rolling native roles | two-/three-cell relational pattern / widened bounded equality decoder / erase third branch | **ATTEMPTED: succeeds but is unnecessary** |
| combinadic held update | independent occupation vector / sparse exterior-lift kernels / dense-equivalent held-L4 recurrence | **open** |
| higher-sector relational slot | local `N>=4` selected tables / bounded rolling gauge or larger slot / complete network inverse | **open** |
| direct rough carrier | target-times-gauge quotient / local preparation and transduction / recurrent rough network | **partial; bridge open** |
| stabilization and renewal | local check algebra / dissipative or reversible syndrome flow / reference and blank genesis | **open** |
| local order field | transported relational token / autonomous admissible update choice / retire compile-time order | **open** |

These are distinct in branch object, invariant, or terminal.  Positive Routes
B/C and four open/partial families prohibit any broad negative.

### N2 — wall-independence audit

The collapsed walls are:

```text
W_held    dense or sparse held-L4 N3 target recurrence,
W_higher  N>=4 and number-changing sectors,
W_ref     fixed-reference genesis,
W_blank   blank rail/work genesis and renewal,
W_order   retirement of compile-time factor/update order,
W_auto    autonomous causal update choice,
W_bridge  selected-carrier <-> rough-carrier transduction.
```

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_held,W_higher` | no | no | yes |
| `W_held,W_ref` | no | no | yes |
| `W_held,W_blank` | no | no | yes |
| `W_held,W_order` | no | no | yes |
| `W_held,W_auto` | no | no | yes |
| `W_held,W_bridge` | no | no | yes |
| `W_higher,W_ref` | no | no | yes |
| `W_higher,W_blank` | no | no | yes |
| `W_higher,W_order` | no | no | yes |
| `W_higher,W_auto` | no | no | yes |
| `W_higher,W_bridge` | no | no | yes |
| `W_ref,W_blank` | no | no | yes |
| `W_ref,W_order` | no | no | yes |
| `W_ref,W_auto` | no | no | yes |
| `W_ref,W_bridge` | no | no | yes |
| `W_blank,W_order` | no | no | yes |
| `W_blank,W_auto` | no | no | yes |
| `W_blank,W_bridge` | no | no | yes |
| `W_order,W_auto` | no | no | yes |
| `W_order,W_bridge` | no | no | yes |
| `W_auto,W_bridge` | no | no | yes |

No pair follows automatically from the other.  In particular, replacing a
dense L4 tensor with a sparse vector does not prepare blanks, choose updates,
or produce a carrier bridge.

### N3 — hidden-wall scan

The note was scanned for assumption language and close variants.  Reference,
reference preparation, blank stations/rail/work, q input, cutoff, selected
table, exact angles, sizes, chart, selected-factor order, Route-A update order,
router, frame, and carrier are explicit supplies.  The 1,830/4,134 rail sites
and the held-L4 memory stop are named.  “Physical” means literal M2 coordinates
and exact nearest-neighbour macros; it does not silently mean initialized,
autonomous, or experimentally realized.

### N4 — residual matching

| witness | exact source | residual attacked | Cycle-560 use | match? |
|---|---|---|---|---:|
| Cycle 557 next terminal | `PHYSICAL_LOCAL_N3_SIX_RAY_DECODER_TOURNAMENT_CYCLE557_NOTE_2026-07-21.md`, N6 | third-cell current-pattern slot return | exhaustive three-cell gate | yes |
| Cycle 555 global encoder | `physical_global_selected_network_encoder_cycle555_2026_07_21.py:selected_network_encoder` | complete selected-network Gram/inverse through N2 | same network encoder residual widened to N3 | yes |
| Cycle 555 global target | `physical_global_selected_network_encoder_cycle555_2026_07_21.py:scheduler_and_global_N2` | free/contact target inverse and intertwiner | exterior lift to complete N3 | yes for mechanism; new N3 state independently tested |
| Cycle 551 token rail | `physical_boundary_aware_multistar_recurrence_tournament_cycle551_2026_07_21.py:route_C_token` | role-avoiding transported token locality | slot-rail anchor/router mechanism | yes for rail only |
| Cycle 532 rough quotient | `physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py:covariance_controls` | rough-target gauge covariance | selected-to-rough bridge | no; dropped as bridge evidence |

Only exact residual matches support closure.  The rough quotient is not used to
claim transduction, and the N2 state is not relabeled as N3 evidence.

### N5 — rhetoric audit

| resolution | tested statement |
|---|---|
| one ray | amplitude, Pauli support, constraint commutators, decoder label |
| one word | all 42 words, two-/six-ray preparation and erasure |
| one cell | local companion/native-pattern theorem |
| three-cell block | all 988 columns, 8,288 terminal rays, every prefix |
| complete L3 network | all occupation partitions plus every dense N3 target amplitude |
| complete held-L4 network | exact encoder transfer and literal layout; no dense target update |
| all frames | compiler L3/L4 and dense L3 update through 24; 576 group products |
| arbitrary size / all sectors | not tested; explicitly open |
| autonomous law / time | not tested; orders remain supplied |

“No parity” and “no Jordan-Wigner string” are scoped to the actual encoder and
update.  “Returned slot” is scoped to one logical slot on a supplied physical
rail, not three physical sites total.

### N6 — partial-closure path

A combinadic vector indexed by sorted mode triples can reduce the held-L4 state
from a full `384^3` tensor to 9,363,584 independent complex amplitudes.  Local
coin application groups coordinates by external occupations and applies
`wedge^r(coin)` blocks; seam permutations and pair-contact phases are sparse.
That route targets `W_held` without new physics.  Independently, enumerate the
first local `N=4` ray table and run the same companion/native/rolling decoder
tournament; stabilization targets reference/blanks, an order field targets
autonomy/order, and an explicit local transducer targets the rough bridge.

### N7 — hostile steelman

> A hostile reviewer should reject “all-sector physical universe,” “arbitrary
> size,” or “autonomous local time.”  The complete-network theorem depends on
> a supplied `N<=3` cutoff, fixed reference, many blank rail/work sites, exact
> coefficient and angle tables, finite tori, and two compile-time orders.  The
> held-L4 target dynamics is not run.  But those boundaries defeat a no-go:
> Route B and Route C are exact on two sizes, the decoder proof is local and
> occupation-exhaustive, the full L3 triple sector evolves with contact and 24
> frames, and a concrete sparse combinadic held-L4 implementation remains.

### N8 — cross-cycle echo

Cycles 319/324 replaced incompatible independent roles with joint roles or
slots.  Cycle 533 used a joint decoder, Cycles 539/545 reused shared volume,
Cycles 548/551 widened recurrence, Cycle 555 found a global companion pivot,
and Cycle 557 replaced a two-pivot six-ray collision with one-hot and binary
routes.  Cycle 560 finds the sharper occupation fact: an ordinary word always
has the foreign-invariant companion, while a special three-particle word
forces every foreign word to vacuum.  The repeated echo is constructive
retirement by better relational structure, not constitutional failure.

No route-independent obstruction, minimum-content theorem, constitutional
change, or axiom pressure survives N1–N8.

## Disposition and next campaign

Retain both global compilers:

- Route B is the strongest literal-site result at 53 live M2/cell;
- Route C is the strongest returned-slot result, with one logical three-M2
  branch state and an explicitly costed blank rail;
- both cover every complete global `N<=3` column at L3 and held L4;
- the L3 free/contact update uses all 708,724 amplitudes, exact inverse,
  nonzero star/contact deletions, all-24 covariance, and an exact physical
  intertwiner; and
- held L4 remains a structural encoder/locality/covariance transfer, not a
  dense-update claim.

The optimal next campaign is the sparse combinadic held-L4 `N<=3` target
update.  It directly tests whether the only held wall is tensor
materialization.  After that, the first `N=4` local ray census is the highest-
value sector extension.  Reference/blank genesis, order/autonomy, and the
rough-carrier bridge should remain independent campaigns.

## Cold certificate

The integrated pre-freeze certificate passed all **13/13** aggregate
predicates in `147.86733541695867` internal seconds (`148.56` timed wall
seconds), reached `723,582,976` internal maximum RSS bytes
(`723,582,976` timed maximum resident-set bytes), and reported zero process
swaps.

The final dense L3 update used all 13,041 independent pair and 695,520
independent triple coordinates.  Maximum pair and triple antisymmetry
residuals were `1.5332934166833741e-18` and
`2.2113472136733112e-18`.  The scheduler digest remained

```text
ffee0cb83cb2228955d0d5eb8ffe6bb252e5528a4265cd30edde4ed2e840c75c
```

The final post-note cold certificate is regenerated after this note and runner
are frozen.  Only that final JSON and the reported frozen hashes are packaging
evidence.
