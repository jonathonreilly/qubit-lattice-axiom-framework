# Physical autonomous frame-gauge retirement — Cycle 558 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_autonomous_frame_gauge_retirement_cycle558_2026_07_21.py`.

## Result

Cycle 558 constructs a one-shot physical retirement channel for the three
frame gauge bits left explicit by Cycles 556 and 553.  It does more than change
the protected quotient: after the channel, every old frame M2 is physically
`|0>` and locally pinned by `+Z`.  The complete frame information is exported
to a named environment or persistent spent layer, never silently erased.
The certified terminal predicate is **old frame M2 terminally blank**, while
the full displayed algebra is preserved by the channel stated below.

The strongest route begins from the target-absorbed Cycle-556 representation,
where the full displayed target algebra is independent of the frame gauge.
For each signed direction and coarse cell, place one blank environment M2 at

```text
r[old frame,d,x] = 16x + 3 D_d,
r[environment,d,x] = 16x + 4 D_d.
```

The pairs are disjoint nearest neighbors.  One parallel SWAP layer moves the
entire lawful frame field into the environment.  More strongly, it conjugates
the complete initial check group

```text
old frame (-ZZ/+ZZ checks) + environment (+Z blank pins)
```

exactly to

```text
environment (-ZZ/+ZZ checks) + old frame (+Z blank pins).
```

There are zero phase-aware row-conjugation failures.  Unlike Cycle 553's
`9N -> 21N` transfer, these source and environment codes have the same `21N`
displayed rows and the same rank.  This is an exact local changing-check
schedule induced by the physical SWAP, not an unsupported check relabeling.

Route A retains the environment as persistent spent cells.  The combined map
is unitary and has an exact inverse.  Old frame M2 are terminally blank, but
information and physical content have only moved: 750 L5 or 1,296 held-L6
spent M2 contain three logical qubits.  The route cannot repeat without fresh
spent cells or reset.

Route B traces or resets the explicit environment after the same Stinespring
isometry.  It is a target-preserving CPTP retirement.  The lawful environment
has eight possible global states and therefore carries at most three bits of
entropy.  The old frame code exponent changes `3 -> 0`, the environment
logical exponent changes `0 -> 3`, and the combined Stinespring exponent and
rank are unchanged.  The runner now evaluates both combined phase-aware check
ranks and the eight logical Kraus operators: their Hilbert-Schmidt Gram rank is
eight and the completeness residual is zero.  Tracing the environment removes the inverse; renewing it
requires a supplied entropy sink with capacity up to three bits for a uniform
frame input.  One-shot retirement is closed.  Closed-resource indefinite
renewal is not.

The full displayed target channel is tested, not inferred from the gauge
label.  The Cycle-556 absorption identity passes all 200,000 L5 and 345,600
held-L6 branch cases, including all 19,200/27,648 `chi`-dependent branch cases.
The subsequent frame/environment SWAP and environment trace commute with the
bare target algebra exactly.  Full Cycle-537 `Gamma(P)`, one-particle mass,
onsite mixing, contact, seam, both matter parities, inverse, deletion, leakage,
and lawful domain controls replay.

All bath sites, SWAP pairs, frame branches, and check incidences transform as
one fixed object under all 24 proper-cubic frames and all 576 products.  Every
export primitive is nearest-neighbor support two; target-absorption primitives
have support three and diameter three.  There is no host frame selector,
parity callback, global order, measurement feedback, or postselection.

The straight radial defect/domain wall route is only partially constructive.
It can move the frame code from signed offset three to four.  Attempted
annihilation at the signed midpoint offset eight identifies the positive and
negative sites: `3N` endpoint collisions appear and every opposite-pair
`-ZZ` row becomes a `-I` constraint.  The final `7 -> 8` map is not a unitary
permutation.  This is a falsifier for that normalized radial route, not a
general defect-annihilation no-go.

An abstract affine decoder proves that only three environment qubits are
needed in principle: the `6N-3` frame-constraint coordinates plus three root
bits have full rank `6N`, and all eight lawful branches decode with zero
residual.  A bounded nearest-neighbor all-24 implementation of that decoder is
not constructed.  The physical channel therefore uses `6N` environment M2
while carrying only three logical qubits; this redundancy is explicit.

A fifth, measurement/reset route measures and stores all frame M2 after target
absorption, then locally resets them.  It is all-24 covariant and target exact,
but its 6N classical spent outputs still contain eight lawful strings and need
erasure or unbounded storage for renewal.  Those outputs are not a Record and
not realized history.

Broad negative gate: **FAIL / DO NOT SHIP**.  The exact three-qubit
environment minimum and the open renewal resource create no shared substrate
obstruction and no axiom pressure.

## Exact target and environment contract

Let `H_TG,s` be the target/gauge plus Wilson factor after Cycle 556's exact
target absorption, `H_b` the three-qubit physical frame-code factor, `F` its
`6N` M2 realization, and `E` the installed `6N` environment M2.

| field | Cycle-558 contract |
|---|---|
| target | Retire the physical frame gauge, not merely its protected name, while preserving the full displayed target channel. |
| domain | Every target/gauge vector, every Wilson branch, all eight coherent frame states on the lawful Cycle-553 frame code, product-blank environment, L5 and held L6. |
| physical terminal | Every old frame M2 is `|0>` and has a local `+Z` blank pin; no old `-ZZ` frame check remains. |
| environment terminal | Every environment/spent output is named, counted, and assigned its exact check group and information/entropy content. |
| target channel | For every displayed `O`, `Phi^dag(O)=O` after the Cycle-556 representation change; mass/contact/seam fixtures follow through the full algebra. |
| locality/covariance | Fixed proper-cubic placement, all 24 frames and 576 products, NN export primitives, bounded target-control support, no runtime selector or global order. |
| recurrence | State whether the same installed resources can run again, what reset is needed, and where entropy goes. |
| forbidden weakenings | No environment trace hidden inside “blank,” spent cells called deletion, schedule called physical time, bath output called a Record/history, host-selected frame, parity oracle, postselection, or route-specific defect failure called constitutional. |
| completion witness | Exact Stinespring/Kraus map, target-channel tests, phase-aware check conjugation, old-site blanking, entropy ledger, L5/L6, deletion/leakage/lawful-domain and renewal controls. |

On the accepted Cycle-556 target-absorbed input, the incremental coherent and
reduced maps are

```text
W_558 = SWAP_(F,E),
W_558 O = O W_558,
Phi_558(rho) = Tr_E[ W_558 (rho tensor |0><0|_E) W_558^dag ].
```

From the earlier Cycle-547 relational input, the full pipeline is

```text
W_total = SWAP_(F,E) S_remote C_absorb,
W_total L(O) = O W_total.
```

`C_absorb` and `S_remote` are already physically compiled by Cycles 547/556;
Cycle 558 adds the first SWAP shown above, from the accepted sink F to E.  The
schedule labels `target-absorb`, `source-to-sink`, `parallel-NN-export`, and
`environment-trace-or-reset` are compiler phases, not physical time.

## Exact check and information ledger

One frame family has `6N` M2, `21N` displayed local rows, rank `6N-3`, and
code exponent three.  The blank environment has `6N` independent `+Z` pins.
Their initial combined rank is `12N-3`.  Sitewise SWAP preserves phase and maps
every row one to one:

```text
S_frame(F) -> S_frame(E),
Z_i(E)     -> Z_i(F).
```

The terminal combined rank is also `12N-3`.  Thus the three logical qubits are
in the environment, while old frame M2 have exponent zero.

| check/export control | L5 | held L6 |
|---|---:|---:|
| old frame M2 | 750 | 1,296 |
| environment/spent M2 | 750 | 1,296 |
| frame rows / rank | 2,625 / 747 | 4,536 / 1,293 |
| blank pins | 750 | 1,296 |
| initial/terminal combined rank | 1,497 | 2,589 |
| check-group conjugation failures | 0 | 0 |
| lawful global frame assignments | 8 | 8 |
| environment constraint failures | 0 | 0 |
| old-frame nonblank failures | 0 | 0 |
| exact inverse failures with environment retained | 0 | 0 |
| NN SWAP pairs | 750 | 1,296 |
| layer operand / site / rough-role collisions | 0 | 0 |

Deleting one SWAP is detected on the branch ensemble.  Deleting one old-site
blank pin drops terminal rank by one.  Deleting the seven environment checks
incident on one site drops the environment frame rank by one.  These controls
distinguish successful retirement from accidental deletion or leakage.

For the physical frame code, a channel that sends all old M2 to one fixed
blank while preserving arbitrary coherent inputs has Kraus rank and minimal
Stinespring environment dimension at least eight.  Route B attains this with
eight orthogonal lawful environment outputs:

| entropy/information item | value |
|---|---:|
| input frame logical qubits | 3 |
| terminal old-frame logical qubits | 0 |
| environment logical qubits | 3 |
| lawful environment states | 8 |
| minimum coherent environment dimension | 8 |
| maximum environment entropy for uniform frame mixture | 3 bits |
| physical environment redundancy | `6N-3` M2 |

The entropy value is logical, not `6N`: the lawful physical strings are
perfectly correlated by the local frame code.

## Normalized route registry

| family | object/formulation | mechanism/invariant | terminal obligation | strength | status | concrete evidence / reopen condition |
|---|---|---|---|---|---|---|
| A. persistent spent-cell unitary | doubled frame-code Hilbert space | local SWAP and exact check conjugation | old F blank, spent E retained, exact inverse | target-equivalent for reversible relocation | candidate-complete | all rows/branches/NN pairs pass; consumes 6N fresh spent M2 per use |
| B. explicit Stinespring/CPTP retirement | system-environment channel | target absorption, coherent export, environment trace/reset | old F blank, target channel exact, entropy named | target-equivalent one-shot | candidate-complete | eight environment outputs, Kraus completeness, target and check tests pass; renewal uses reset sink |
| C. radial defect/domain wall | signed offset check complex | translate checks and try opposite-wall annihilation | remove `-ZZ` code without spent output | target-equivalent within radial family | blocked-local | relocation `3 -> 4` works; midpoint has `3N` collisions and `-I`; reopen with a nonradial defect network |
| D. three-bit affine decoder | classical affine frame code | invert constraint coordinates into three data bits plus zeros | only three bath qubits, bounded all-24 NN compiler | stronger resource efficiency | blocked-local | algebraic rank and all branches pass; local covariant circuit is missing |
| E. covariant measurement/reset instrument | local quantum instrument plus classical environment | measure/store every site after target absorption, reset locally | old F blank, target exact, classical spent outputs named | weaker/nonisometric | provisional | all-site rule is covariant; 6N raw outputs encode eight lawful strings and require erasure/storage |

The families differ in object, information mechanism, and terminal proof
obligation.  The successful A/B routes are not counted as physical-content
destruction: their spent/environment outputs are explicit.

## Route A — local unitary export to persistent spent cells

The offset-four bath layer is injective, collision-free with the retained
offsets one, three, five, six, and seven, and disjoint from rough-code M2.  The
Cycle-544 offset-four chain was a route-local candidate and is not
simultaneously installed in the retained Cycle-556 object; reuse is declared.

All `6N` SWAP pairs have physical L1 distance one and no shared operand.  The
layer is scalar in family and treats every signed direction identically.  Its
all-24 coordinate/pair failures and all-576 direction-group failures are zero.

With spent cells retained, the complete map has an exact inverse and preserves
frame coherence.  It physically blanks old F but neither erases information
nor reduces installed content.  A persistent bank supplies only one use unless
new spent cells are installed.  That finite-use resource count is the route's
renewal disposition, not a no-go for resettable baths.

## Route B — CPTP/Stinespring retirement and changing checks

The same unitary is a Stinespring dilation.  Tracing the environment gives an
eight-Kraus replacement channel on the lawful frame factor and leaves every
target observable invariant after `C_absorb`.  The environment is not omitted
from the physical account: it contains 750/1,296 M2 and exactly three logical
qubits before trace or reset.

The changing-check schedule is local and exact because it is induced by the
NN SWAP conjugation.  Initial environment `+Z` pins become terminal old-frame
`+Z` pins; old frame `-ZZ/+ZZ` checks become environment checks.  No check is
turned off by host choice.  The optional environment reset is a separate CPTP
resource step and deliberately has no inverse.

The route is renewable relative to a supplied reset bath.  For a uniform
logical frame mixture, at least three entropy bits per use enter that bath.
Without fresh cells or an entropy sink, a finite persistent environment cannot
return to its initial blank while retaining exact target-channel operation.
This is a resource ledger, not a gravity/source law.

## Route C — defect/domain-wall transport

For signed radial offsets `3,4,5,6,7`, the six directional layers remain
injective and proper-cubic.  Each consecutive translation has NN endpoints.
The first `3 -> 4` step is exactly Route A's code relocation.

At offset eight, positive and negative sites meet at the cell midpoint.  The
`6N` signed labels collapse to `3N` physical sites.  Therefore the `7 -> 8`
endpoint map is not a permutation.  Worse, the opposite constraint becomes

```text
-Z_i Z_i = -I,
```

for all `3N` opposite pairs.  An exact code cannot contain that stabilizer.
The runner checks `3N=375/648` endpoint collisions and the same number of
anti-equality self-relations.

This disposes only of straight signed-radial annihilation in one scale-16
cell.  Branched defects, extra plaquette work, non-Pauli gauge walls, and
dissipative endpoint rules remain open.

## Route D — abstract three-bit reversible decoder

The frame code is an affine repetition code.  Its constraint masks have rank
`6N-3`.  Adding the three positive-root coordinate bits produces rank `6N`.
For every lawful branch, all constraint residuals vanish and the three root
bits take all eight values.  Hence an abstract affine reversible map can send

```text
6N frame M2 -> 3 data qubits + (6N-3) blank syndrome qubits.
```

This proves that Route B's `6N` physical environment is not an information
minimum.  The missing construction is a bounded-NN, all-24 covariant reversible
decoder.  Choosing a Gaussian-elimination tree or positive-axis order is not
silently accepted as that compiler.  The macro origin is supplied; a covariant
independent constraint basis and physical circuit remain open.

## Route E — covariant measurement/reset instrument

After target absorption, measure every old frame M2 in its local Z basis,
write the outcome to a local classical environment, and reset the M2 to zero.
The rule has support one, is identical on all signed sites, and has no feedback
or host branch.  The raw environment contains `6N` bits but only eight lawful
strings and at most three bits of entropy.

This route is target exact and physically blanks F.  It destroys coherent
frame information and has no unitary inverse.  Repetition requires erasing the
classical outputs or storing an unbounded sequence.  A classical bath output
is not a Record and not realized history merely because it persists.

## Full target channel and physical controls

Cycle 558 explicitly evaluates the same relational phase as Cycle 547 and the
Cycle-556 absorption:

```text
f_O(s,b) = sum_a s_a [eta_(a,0)(O) + b_a chi_a(O)].
```

For every displayed matter/gauge row and all 64 branches, the physical chosen
membrane commutator equals `f_O`; applying `C_absorb` cancels it.  Export and
environment trace then act only on frame/environment M2, so the bare target
algebra is fixed by the channel adjoint.

| target-channel control | L5 | held L6 |
|---|---:|---:|
| matter generators | 2,625 | 4,536 |
| gauge generators | 500 | 864 |
| full displayed generators | 3,125 | 5,400 |
| all-branch tests / failures | 200,000/0 | 345,600/0 |
| `chi` branch tests / failures | 19,200/0 | 27,648/0 |
| controlled membrane factors | 150 | 216 |
| maximum target-control support / diameter | 3/3 | 3/3 |
| post-absorption SWAP target failures | 0 | 0 |
| environment-trace target failures | 0 | 0 |

All-24 signed membrane/control failures are zero.  The Cycle-556 branch and
phase-aware frame-`Z` actions and all-576 group laws replay with zero failures.
Full Cycle-537 physics replay passes `Gamma(P)`, mass, contact, seam, both
parities, inverse, deletion, leakage, lawful domain, and held-size controls.

## Recurrence and renewal audit

| route | can repeat on same installed finite cells? | required renewal resource |
|---|---|---|
| A persistent spent | no | a fresh collision-free spent layer or reversible return of `b` |
| B CPTP/Stinespring | yes, conditionally | reset offset-four environment through an entropy sink of up to three bits/cycle |
| C radial defect | no completed annihilation | a nonradial defect endpoint or dissipative removal law |
| D compact decoder | not yet physical | bounded all-24 decoder plus three reset bath qubits |
| E measurement/reset | yes, conditionally | erase/store 6N raw classical outputs carrying three logical entropy bits |

The one-shot channel is autonomous in the limited operational sense that its
local rules and phase order contain no measurement-conditioned host action.
The compiler schedule is not physical time.  A closed-resource recurrent law
that regenerates its own blank environment is not constructed.  The reset bath
is a supplied resource, not a hidden source theory.

## Supplied-structure inventory

Supplied:

- the accepted Cycle-556 target-absorbed frame-gauge representation;
- the lawful Cycle-553 frame code and its complete local check group;
- the Cycle-527 scale-16 microgrid and ordinary NN SWAP law;
- product-blank offset-four environment M2;
- the macro-cell partition and periodic L5/held-L6 geometry;
- a reset bath and entropy sink only for renewable B/E operation;
- the statement that Cycle-544's route-local offset-four chain is not
  simultaneously installed.

Constructed:

- collision-free proper-cubic bath placement and one-layer NN export;
- exact phase-aware initial-to-terminal check-group conjugation;
- old-frame product blanking and local terminal `+Z` pins;
- unitary persistent-spent and CPTP/Stinespring target channels;
- complete physical/logical environment and entropy ledger;
- straight radial defect falsifier, abstract compact decoder, and local
  measurement/reset comparison;
- deletion, leakage, lawful-domain, inverse, L5/L6, and renewal audits.

Not constructed:

- closed-resource environment renewal without an entropy sink;
- a bounded-NN all-24 decoder from `6N` redundant frame M2 to three bath M2;
- a general defect/domain-wall annihilation theorem;
- the full physical recurrent law or rough/source product encoder;
- a causal clock, gravity/source, Born, Record, or realized-history law.

## No-go discipline N1–N8

Status for the narrow information claim “coherent physical blanking of the
full three-qubit frame code requires an environment of dimension at least
eight”: **PASS**.  Status for any broad defect, bath, or substrate no-go:
**FAIL / DO NOT SHIP**.

### N1 — Alternative-route enumeration

1. **Persistent spent-cell unitary — ATTEMPTED.**  It exports the full frame
   state into a congruent 6N-M2 layer and exactly blanks F.  It confirms rather
   than evades the environment minimum; information remains in three spent
   logical qubits.
2. **Explicit Stinespring/CPTP channel — ATTEMPTED.**  It attains the minimum
   logical environment dimension with eight lawful outputs while using a
   redundant local 6N-M2 realization.  Tracing/resetting the environment
   supplies the nonunitarity and entropy export.
3. **Defect/domain-wall annihilation — ATTEMPTED.**  Straight radial transport
   relocates the code but midpoint annihilation is noninjective and phase
   inconsistent.  The failure is route-specific and does not close nonradial
   or dissipative defects.
4. **Abstract three-bit reversible decoder — ATTEMPTED.**  It proves an
   eight-dimensional recipient is sufficient algebraically and could remove
   the 6N physical redundancy.  The bounded covariant NN compiler remains the
   exact missing lemma.
5. **Covariant local measurement/reset — ATTEMPTED.**  It physically blanks F
   and preserves the absorbed target channel, while placing the three logical
   entropy bits in a classical 6N-bit output.  It is nonisometric and needs
   renewal storage/erasure.

The five routes are normalized by different primary objects and terminal
obligations.  Positive altered contracts are retained rather than counted as
failures.

### N2 — Wall-independence audit

After the one-shot construction, one collapsed wall remains for a stronger
closed-resource recurrent claim:

- `W_environment-renewal`: return the finite environment to its blank input
  without hiding the exported entropy or importing fresh spent cells.

There is no second independent wall, so a pairwise table is vacuous.  The
missing compact decoder is a resource-efficiency optimization, not a condition
for one-shot retirement or renewal with the declared reset bath.  Full rough
preparation and recurrent target dynamics remain separate campaigns and are
not premises of the retirement channel.

### N3 — Hidden-wall scan

The product-blank environment, offset-four reuse, target absorption, phase
order, check groups, trace/reset step, entropy sink, macro partition, periodic
sizes, spent-cell count, and renewal condition are explicit.  The route-local
Cycle-544 offset-four role is declared absent rather than overwritten.  No
host frame selector, parity service, global order, postselection, hidden
feedback, or silent environment trace remains.  “Autonomous” is limited to the
fixed local channel macro and is not promoted to a causal recurrent law.

### N4 — Residual matching

| cited witness | witness residual | Cycle-558 residual | match? |
|---|---|---|---|
| `docs/work_history/repo/review_feedback/PHYSICAL_RELATIONAL_FRAME_COMPRESSION_ISOMETRY_CYCLE556_NOTE_2026-07-21.md`, lines 130–162 | three frame qubits require an eight-dimensional isometric recipient | minimum coherent Stinespring environment for physical blanking | yes |
| same Cycle-556 note, lines 232–284 | source blanking with an explicit nonblank recipient | persistent spent/environment export | yes |
| `docs/work_history/repo/review_feedback/PHYSICAL_RELATIONAL_MEMBRANE_FRAME_REFERENCE_PUMP_CYCLE547_NOTE_2026-07-21.md`, lines 42–81 | target dephases if frame side is erased before relational absorption | target absorption before environment trace | yes |
| `docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_PERSISTENT_SUBSYSTEM_SINK_CYCLE553_NOTE_2026-07-21.md`, lines 185–196 | unequal `9N/21N` source/sink checks prevent check-group conjugation | congruent `21N/21N` frame/environment check transfer | no; contrast only |
| `docs/work_history/repo/review_feedback/PHYSICAL_COVARIANT_PARITY_CHAIN_DYNAMIC_PUMP_CYCLE544_NOTE_2026-07-21.md`, lines 46–47 and 241–253 | target dephasing from an unretained membrane side | post-absorption physical gauge retirement | no; dropped as proof witness |

Only the first three match the current information/target residuals.  The
check-conjugation claim is proved anew for congruent frame/environment codes.

### N5 — Rhetoric audit

| phrase | tested resolution | broader untested resolution | disposition |
|---|---|---|---|
| “physical retirement” | every old frame M2, all eight lawful branches, L5/L6 | closed-resource indefinite recurrence | one-shot claim only |
| “target preserved” | every 3,125/5,400 displayed generator on all 64 branches and inherited fixtures | unsynthesized full recurrent update | target channel only |
| “three-qubit minimum” | full coherent frame code under fixed-blank physical output | quotient-only gauge states or restricted/dephased input | environment-specific claim |
| “defect annihilation fails” | straight signed radial offsets 3 through 8 | nonradial, non-Pauli, dissipative defects | route-specific wording only |
| “local” | check support two, target controls three, export SWAP two | compact logical decoder | decoder locality remains open |

No per-route negative is broadened to all blocks, lattices, or mechanisms.

### N6 — Partial-closure path scan

The positive paths are explicit and require no new axiom:

1. keep the offset-four environment as spent physical content;
2. trace/reset it through a declared entropy sink;
3. compile the exact affine decoder to reduce physical bath overhead to three
   qubits;
4. use a nonradial defect network with a named endpoint;
5. store/erase the classical measurement environment.

Paths 1 and 2 close one-shot blanking.  Paths 3 and 4 are constructive next
targets.  Path 5 is weaker but honest.  None is a labeling convention that
silently creates a dynamics or source law, and no “new axiom required” claim
survives.

### N7 — Steelman

A hostile reviewer should reject any suggestion that the `6N`-M2 environment
or supplied reset bath is fundamental.  The affine rank audit already gives a
three-qubit decoder, and the frame constraints are local.  A reversible
cellular decoder with covariant marker work could concentrate the global frame
state into three local bath modes, blank all other frame/environment M2, and
then reset only those modes.  Alternatively a branched defect network could
carry the three logical bits to a compact boundary sink without encountering
the radial midpoint collision.  The concrete terminal obligation is a
bounded-NN all-24 circuit with exact work uncomputation and renewal, not a new
axiom.  These routes do not evade the three-qubit environment minimum; they
could attain it physically and improve Cycle 558's overhead.

### N8 — Cross-cycle echo

Cycle 544's target dephasing was retired in Cycle 547 by retaining the missing
frame relation.  Cycle 550's blank-retirement failure was retired in Cycle 553
by an explicit sink.  Cycle 556 then separated recipient transfer from true
compression.  Cycle 558 follows the same successful mechanism: environment
content is named before it is traced, reset, or stored.  Similar prior walls
were closed by explicit recipients and resource ledgers, so those mechanisms
are constructed here rather than dismissed.  No cross-cycle echo supports a
broader no-go or axiom pressure.

## Six-wall and TOE dependency update

| wall | Cycle-558 effect |
|---|---|
| `C_ref` | Advances: the protected frame gauge can now be physically removed from old M2 by an exact target-preserving channel; its environment image is explicit. |
| `C_num` | Sharpens: three logical environment qubits are necessary/sufficient, while the present local covariant realization uses 6N M2. |
| `C_wrap` | Unchanged; seam/wrapped controls replay and no phase is called energy. |
| `C_int` | Advances one-shot: all displayed matter/gauge operators, mass, contact, and seam survive environment trace.  Full recurrent dynamics remains open. |
| `C_local` | Advances: NN export, exact local check conjugation, old-site pins, all24/576, L5/L6, deletion and lawful-domain controls close.  Compact decoder locality remains open. |
| `C_source` | Sharpens the resource ledger but does not close: renewable operation consumes a named entropy sink of up to three bits/cycle; no source/gravity law supplies it. |

Maturity remains operational quantum/records `3/5`, time `1/5`,
inertia/matter `2/5`, gravity/source `1/5`, Born/probability `1/5`.  Bath and
spent outputs are not Records.

## Disposition and next campaign

Retain Route B as the strongest one-shot physical frame-retirement channel.
Retain Route A as its reversible dilation and exact inverse ledger.  Retain the
radial midpoint result only as a route-specific defect falsifier.  Do not call
environment trace closed-resource autonomy or schedule depth physical time.

The highest-value next campaign is the **bounded all-24 reversible affine
decoder**: turn the exact `6N = (6N-3)+3` coordinate decomposition into an NN
microgrid circuit, uncompute every syndrome/work M2, export only three bath
qubits, and audit reset renewal.  A competing nonradial defect network should
remain live.  Full recurrent target dynamics and rough/source preparation are
independent.

## Cold certificate

The final cold command was:

```text
/usr/bin/time -lp python3 \
  scripts/physical_autonomous_frame_gauge_retirement_cycle558_2026_07_21.py \
  --mode frame-gauge-retirement-certificate
```

It passed `12/12` top-level tests.  Internal elapsed time was
`161.29897933301982 s`; external wall time was `162.67 s`.  The certificate's
maximum checkpoint RSS was `106,954,752` bytes; external maximum RSS was
`118,947,840` bytes, with zero process swaps.  The five normalized L5/L6 route
audits completed at `8.632508915965445 s`; the pinned Cycle-537 target replay
completed at `161.29608416603878 s`.  The hard wall was 1,200 seconds.

Zero cold residuals include bath/old/rough/role collisions, non-NN export
pairs, layer operand collisions, all-24 bath/SWAP/membrane/branch/phase-aware
actions, all-576 direction/branch/phase group laws, phase-aware check-group
conjugation, old-frame blank pins, eight lawful environment assignments,
Stinespring output Gram rank, Kraus completeness, all 200,000/345,600 target
branch cases, all 19,200/27,648 `chi` cases, environment-trace target action,
affine-decoder lawful residuals, matter/gauge cross commutators, and inherited
physics residuals subject to their declared tolerances.

Sensitivity controls remain nonzero where required: deleting one SWAP fails
four of the eight frame assignments; deleting one old blank pin drops rank by
one; actually deleting the seven environment checks incident on one site drops
rank by one with zero phase inconsistency; radial midpoint transport has
375/648 endpoint collisions and `-I` anti-equality rows; persistent renewal
consumes 750/1,296 spent M2; and uniform CPTP renewal exports up to three entropy
bits.
