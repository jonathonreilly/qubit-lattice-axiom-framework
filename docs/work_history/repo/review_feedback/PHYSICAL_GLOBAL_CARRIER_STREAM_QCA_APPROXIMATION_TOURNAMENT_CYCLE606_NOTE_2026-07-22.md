# Physical global carrier stream/QCA and approximation tournament — Cycle 606

Date: 2026-07-22
Authority: none
Audit: unset
Branch: `codex/toe-cross-lane-campaign-20260718`

## Question and disposition

Cycle 606 asks whether the Cycle 600 three-species, four-M2 word stream can be
executed simultaneously on the whole cubic torus without a checkerboard,
global parity string, preferred origin, size query, or host tick.  It also asks
whether the remaining Cycle 603 calibrated beta/contact-g rotations can be
replaced by finite Clifford+T words with an explicit q-update error budget.

The strongest constructive result is an **exact compact-register global
stream**, not yet a physical-site compiler.  Route A uses a second four-M2 word
per species and realizes the abstract stream exactly on the inherited Cycle 600
one-carrier-per-species sector.  Its scatter and clear label sublayers commute,
so the printed label order is not a hidden spatial order.  Every individual
event has a counted support-one/two nearest-neighbor lowering.  What is still
missing is one translation-invariant proper-cubic physical-M2 supercell,
including scratch coordinates, in which all simultaneously routed event
instances are vertex-disjoint or obey an explicit bounded conflict schedule.
A per-event eleven-site line is not that global packing proof.

Therefore the decisive physical compiler question remains open, but it is
sharply reduced.  There is no impossibility result and no axiom pressure.

The fixed scatter/clear/swap schedule is not time.  The buffer, phase, and
carrier bookkeeping below are not energy, source, Record, or causal-time
constructions.

## Accepted shore

The runner pins the accepted Cycle 603 runner, note, receipt, and cold transcript
byte-for-byte.  Inherited facts are restricted to these:

- the Cycle 603 support-two parametric event compiler passed;
- exact finite-alphabet angle closure remained false;
- the crossed-link event schedule had not been composed into a global stream;
- the inherited persistent carrier cost was twelve M2 per coarse cell.

No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit-status file is changed here.

## Route A — compact double buffer

For each cell `x` and species `s`, let `A[x,s]` and `B[x,s]` be four-bit words.
Words 1–3 are neutral and words 4–9 carry the six cubic directions.  Invalid
words 10–15 are retained only to define and test a reversible off-code
extension.  The encoding is

`E(a) = (A=a, B=0, clean local work)`.

One fixed compact-register update has three factors:

1. scatter: for every word `w`, XOR `w` into `B[x+v(w),s]` when `A[x,s]=w`;
2. clear: XOR `w` out of `A[x,s]` when `B[x+v(w),s]=w`;
3. swap: exchange the local A and B words.

Each equality-controlled XOR is an involution.  The inverse reverses the three
factors.  Source controls and destination targets have distinct A/B roles.  For
one fixed label, `x -> x+v(w)` is a bijection, so no checkerboard or color is
needed at compact-register resolution.

On the declared code,

`E G_coarse = G_register E`

exactly.  The same relation holds for any initially blank, valid-word
configuration that does not create an incoming collision.  That broader domain
is not claimed invariant under repeated updates.

### Exact tests

| control | L3 | L6 | L7 |
|---|---:|---:|---:|
| lawful site/species/label rows | 729 | 5,832 | 9,261 |
| stream failures | 0 | 0 | 0 |
| complete-macro dirty-buffer failures | 0 | 0 | 0 |
| invalid-word identity rows | 486 | 3,888 | 6,174 |
| invalid-word identity failures | 0 | 0 | 0 |
| arbitrary full-space inverse trials/failures | 10/0 | 10/0 | 10/0 |
| translation commutator failures | 0/27 | 0/216 | 0/343 |
| all 24 frame commutator failures | 0 | 0 | 0 |
| all 576 frame-product site/word failures | 0 | 0 | 0 |
| exterior-CAR EG / inverse residual | 0 / 0 | 0 / 0 | 0 / 0 |

The all-576 group test covers every site and all sixteen words at each size.
The exterior tests used 31 factorized occupation samples per size through
occupation three and observed both reordering signs, `-1` and `+1`.

For each size, every one of the 105 label pairs was applied in both orders in
both the scatter and clear sublayers.  There were zero commutator failures.
The reverse order and the orders induced by all 24 proper-cubic frames also
gave zero failures.  Scatter followed by clear followed by swap remains a
supplied update factorization; commutation within a sublayer does not turn that
factorization into causal time.

The deletion control for scatter, clear, or swap separately changed the lawful result by
two, one, and two word slots, respectively.  Thus no macro factor is inert.

### Malformed, collision, and lawful-domain controls

All fifteen pairs of distinct bound directions that can send two remote
same-species carriers into one target B word were tested at every size.  Every
pair left the declared code; every malformed output was exactly inverted.
The construction retains reversibility but neither rejects nor repairs the
collision.  A random dirty B register also failed the code check and was exactly
recovered by the inverse.

The local auxiliary conditions `B=0`, valid word, and clean work are on-cell
checks.  The condition "exactly one carrier per species" is inherited from
Cycle 600, is global, and is not locally generated or enforced here.  It is the
reason same-species incoming collisions are absent on the tested lawful sector.
This nonlocal sector boundary must remain visible in any claim about Route A.

### Elementary event template and open physical packing

The equality predicate is a C4X compiled through three Toffoli calls and two
clean work bits; the flag controls the four target bits and is uncomputed.  The
accepted Cycle 603 exact Toffoli sequence lowers it to
`X/H/T/Tdg/CNOT/SWAP`.  The event-local audit reports:

- maximum elementary gate support: two M2;
- persistent A+B carrier storage: 24 M2 per coarse cell;
- maximum live storage with species-parallel flag/work: 33 M2 per coarse cell;
- complete macro template: 14,040 base gates per coarse cell;
- event-local serial routed depth: 11,656;
- zero nearest-neighbor or all-24 rotated-line failures;
- no template dependence on volume parity, origin, or size.

These counts are useful upper bounds on a local block.  They do **not** prove
that the routed lines for all translated cell instances can coexist on one M2
lattice.  The current open obligation is a concrete proper-cubic supercell with
coordinates for A, B, flag, work, ports, and paths, followed by collision checks
for all simultaneous instances on L3, L6, L7, every translation, and all 24
frames.  Until that exists, `G_register` must not be renamed `G_physical`.

## Route B — direction-expanded partitioned QCA

Route B uses a compact A word plus six outgoing and six incoming four-bit lanes
per species: 156 persistent M2 per coarse cell.  A local involution exchanges a
bound compact word with its matching direction lane.  The intercell layer swaps
`Out_d(x)` with `In_d(x+v_d)`.  Distinct Out/In roles make these pairs a perfect
matching without parity coloring.

The word-register construction passed all 729/5,832/9,261 lawful rows, inverse
tests, and all 24 code-and-lane covariance checks with zero failures.  A
malformed pair of incoming carriers remained in two lanes and inverted exactly.

This route has a narrower but larger import: one cubic-covariant 28-M2 local
exchange containing six disjoint basis transpositions.  A generic Gray outline
would use 38 C27X calls, each reducible to 51 Toffoli calls with 25 clean work
bits, but that lowering was not executed.  A translation-invariant physical
placement of all lane registers is also not materialized.  Route B is therefore
an exact partitioned register QCA with named block and geometry imports, not a
finished physical-M2 compiler.

## Route C — state-carried phase

Route C retains A and B and adds one local phase bit `p_x`.  The phase bit is
part of the state.  No host layer, tick parity, color, origin, or size is queried.
For a uniform phase sector,

`G_register E_p = E_(1-p) G_coarse`.

The phase advances by a parallel local X on every `p_x`.  That advance is
self-inverse.  The local constraint `p_x=p_y` on every nearest-neighbor edge is
preserved exactly: random nonuniform syndrome counts were 42 to 42, 318 to 318,
and 476 to 476 for L3, L6, and L7.  A single flipped phase bit had syndrome six.

For phase zero and phase one together, Route C passed 1,458/11,664/18,522
lawful rows with zero stream or inverse failures.  Two consecutive global shifts
passed at every size.  Random nonuniform malformed states inverted exactly.

Uniform phase genesis is supplied, not derived or repaired.  The
phase-controlled C6X equality block and its global physical packing are also
not executed.  The phase field is a scheduler state; it is not physical time.

## Precision-bounded Clifford+T attempt

The precision route extracts all 41 distinct parameterized one-M2 matrices from
the Cycle 603 compiled three-species coin and contact circuit.  The inherited
calibrations are beta `-0.3` and contact `g=0.37`.  It exhaustively enumerates
all 88,572 words over H, T, and Tdg through depth ten, quotients global phase,
and retains the best observed word for each matrix.  This is exhaustive only
for that finite word set; it is not a synthesis-optimality statement.

The worst one-gate ray-operator residual decreased at depths 2/4/6/8/10 as

`0.765367, 0.409938, 0.292893, 0.158185, 0.158185`.

Replacing 864 parameterized instances in the one-species compiled coin gave a
ray-Frobenius residual `3.9404162105` and scratch leakage
`3.8316203555e-15`.  The depth-ten weighted telescoping bound was already
`44.9180419361` per cell and therefore capped at the trivial operator bound two.
After multiplication by volume and q-update count, every tested L3/L6/L7,
q-update `1/10/100` bound was also trivial.  This attempt quantifies failure at
the chosen depth; it does not prove exact finite-alphabet synthesis impossible and it
does not supply a useful global precision budget.

## Supplied structure inventory

1. The Cycle 600 three-species, exactly-one-carrier-per-species global sector.
2. Blank B words and clean equality work at encoding.
3. The fixed scatter/clear/swap macro factorization.
4. The event-local eleven-site routing layout inherited from Cycle 603.
5. A physical cubic supercell packing for simultaneous Route A events: absent.
6. Route B's 28-M2 symmetric exchange and physical lane placement: imported.
7. Route C's uniform phase genesis, C6X count, and physical packing: imported.
8. Periodic L3/L6/L7 tori as fixtures; the local register rules do not query L.
9. Calibrated beta and contact g, plus a maximum Clifford+T search depth of ten.
10. The abstract update factorization; no causal duration or energy assignment.

## Six-wall ledger delta

- `C_ref`: unchanged.  No reference-frame or external-order service was added.
- `C_num`: not retired.  A finite beta/g approximation and q-update scaling
  audit now exists, but depth ten gives only trivial global bounds.
- `C_wrap`: unchanged.  No wrapped phase is called physical energy.
- `C_int`: advanced at compact-register resolution.  The simultaneous stream
  now has an exact reversible double-buffer product and exact exterior EG tests.
- `C_local`: advanced but open.  Event-local support-two lowering is counted;
  translation-invariant simultaneous physical-M2 supercell packing is absent.
- `C_source`: unchanged.  Carrier/buffer resources are bookkeeping, not a
  gravity/source or energy derivation.

No wall is retired beyond its stated scope.

## N1–N8 no-go discipline

### N1 — normalized route families

Six families are separated: compact double buffer; direction-expanded
partitioned lanes; state-carried phase; finite Clifford+T approximation;
Cycle 603 independent crossed-link gates; and a live untested reversible
collision-syndrome/debris reservoir.  The first four are attempted here, the
fifth is a scoped prior failure when used alone, and the sixth remains live.

### N2 — wall independence

The runner audits every pair among clean initialization, physical supercell
packing, malformed collision repair, Route B elementary lowering, uniform
phase genesis, and finite-precision scaling.  None is treated as closing
another.  These are current imports, not route-independent obstructions.

### N3 — hidden-wall scan

Blank auxiliary state, the global exactly-one sector, macro factorization,
per-event versus global geometry, Route B's exchange, Route C's uniform phase,
finite search depth, and periodic test boundaries are explicit.  The scan does
not silently identify an abstract register with a physical site compiler.

### N4 — residual matching

The Cycle 603 global-schedule residual is only partly matched.  Route A supplies
an exact role-separated compact-register product, but not a simultaneous
physical routing/packing theorem.  The analog-angle residual is measured rather
than retired.  Malformed duplicate-carrier controls still leave the Route A
code and remain visible in Route B lanes.

### N5 — rhetoric audit

No physical compiler, causal time, energy, source, Record, exact precision
closure, or all-malformed-sector repair is claimed.  Exactness is always tied
to the named encoding and global one-carrier/species sector.

### N6 — partial closure paths

The nearest constructive steps are: build a directed-edge proper-cubic
supercell and collision-check every routed event; add a reversible local
collision syndrome/debris reservoir; lower Route B's local exchange; derive or
avoid the Route C phase genesis; and use certified epsilon-target single-qubit
synthesis with a declared volume/horizon budget.

### N7 — hostile steelman

A hostile reviewer should reject a locality, scheduling, collision, or precision
no-go.  Route A already removes host parity at register resolution, Route B
turns intercell movement into literal role-separated matchings, and Route C
carries phase in state.  Constant-size supercells, reversible syndrome fields,
and certified single-qubit synthesis are concrete live counterroutes.

### N8 — cross-cycle echo

Earlier cycles repeatedly retired apparent services by bounded constructive
objects.  Cycle 606 continues that pattern: it closes the register-level global
permutation while isolating a physical packing obligation.  That is evidence
for another construction campaign, not constitutional escalation.

No negative, minimum-content, or shared-obstruction claim is shipped.  There is
no axiom pressure.

## Optimal next campaign

Materialize a single translation-invariant proper-cubic M2 supercell for Route
A.  Give coordinates for every A/B/scratch/port site, compile each macro layer,
and exhaustively check simultaneous route vertex/edge conflicts on L3, L6, L7,
all translations, all 24 frames, and all 576 frame products.  The schedule may
use a fixed bounded number of local conflict colors only if those colors are
part of the translation-covariant cell structure and do not query origin,
parity, or size.  If this closes, compose the resulting physical stream with the
Cycle 603 onsite coin/contact block and then address collision syndromes and
certified beta/g precision budgeting.

## Parent-agent verification

The parent agent independently imported the frozen runner without invoking its
receipt-writing main path and replayed the pinned shore, Routes A–C, the finite
Clifford+T search, and the full N1–N8 gate.  All six science checks passed and
none failed.  In particular the replay reproduced exact compact-register
stream `EG` and inverse residuals, zero all24/all576 failures on L3/L6/L7, the
positive register-QCA Route B and phase-carried Route C results, the failed
exact/global precision target, and the explicit false value of Route A's
simultaneous physical-supercell-packing contract.

The parent transcript is outside the repository at
`/tmp/cycle606_parent_verify.txt`, SHA-256
`50e918141d34af7b860d7854776cb362ccf8d28dab3888d6cd583b3d9fe26add`.
The frozen receipt and cold transcript pin the runner and pre-appendix note;
this appendix changes only the human-readable note.
