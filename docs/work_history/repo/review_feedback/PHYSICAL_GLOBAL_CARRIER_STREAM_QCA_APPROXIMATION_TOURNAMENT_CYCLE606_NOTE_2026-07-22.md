# Cycle 606 — logical global carrier stream/QCA approximation tournament

Date: 2026-07-22
Authority: none
Audit: unset
Author artifact status accepted: false
Broad-negative gate: FAIL / DO NOT SHIP
Constitutional effect: none

## Verdict

Cycle 606 constructs an exact constant-overhead **logical/register only**
carrier stream. Its strongest route is a compact reversible double buffer for
the Cycle-600 three-species four-role-bit words. On the declared
one-carrier-per-species code it obeys the register-algebra identity

```text
E_register G_coarse = G_register E_register
```

for the stream component, with exact inverse, deletion sensitivity, collision
controls, L3 train, L6 held, and L7 held-out-size tests. It uses no runtime
global parity string, parity/color/origin/size query, or preferred traversal.

This is not a physical M2 compiler. No route executes all of the required
literal M2 placement, primitive product, physical encoder, physical
intertwiner, physical-code leakage, and one-fine-site translation-covariant
law. Those fields are respectively `false` or `null`. The logical role line
used for gate routing is not promoted to physical M2.

The broad locality, collision, precision, minimum-content, shared-obstruction,
and axiom-pressure negatives all fail the no-go gate because a concrete
physical-supercell/collision-reservoir steelman remains open. The narrowed
positive register artifact passes. There is no shared obstruction and no
axiom pressure.

## Byte-pinned shore

The runner byte-pins the final independently reviewed Cycle-603 quartet:

| Artifact | SHA-256 |
|---|---|
| Cycle-603 runner | `e64032e369e08e03ad2a742a2bde6914d8adc6ed1fd64f15f4e301c1c8dea739` |
| Cycle-603 note | `ddc06d6d4abf945794b1c0b7566c9183fa744839d1ba5630c1d9ad8b4559c417` |
| Cycle-603 receipt | `751487fa50a738d5473f7ddcb77474785c84463dda1264a34de2643f19102871` |
| Cycle-603 cold | `35385a09b5d075e553de1de9302e0317dd415acbe1f5ccf9425905eedae94174` |

It also verifies the final Cycle-600 quartet and the complete inherited
Cycle-603 transitive science closure. Git status, ancestry, and author status
are not scientific evidence.

## Route A — compact reversible double buffer

For active word register `A` and blank buffer `B`, one macro is

```text
scatter: B_(x+v(w)) XOR= w  controlled by A_x=w
clear:   A_x XOR= w          controlled by B_(x+v(w))=w
swap:    SWAP(A_x,B_x)
```

Every equality-XOR and SWAP is a full-register-space involution. Reversing the
three sublayers gives the exact inverse. On blank-buffer configurations with
no same-species incoming collision, the output is the Cycle-600 word stream.
The declared code has exactly one carrier per species globally, so it lies in
that domain. Blank buffer, word validity, and clean work are locally checkable
register predicates but are not dynamically generated or locally enforced.

The register gate template contains 14,040 one-/two-role-bit gate instances per
coarse cell at serialized declared-role-line depth 11,656, with 24 persistent
active-plus-buffer role bits and at most 33 live role bits per cell when three
species use clean flags/work in parallel. These are role/register counts, not
physical M2 counts and not source or energy.

The exact rows are:

| L | split | lawful rows | invalid rows | inverse trials/failures | register EG / inverse EG | collision pairs leaving code / inverse failures |
|---:|---|---:|---:|---:|---:|---:|
| 3 | train | 729 | 486 | 10 / 0 | 0 / 0 | 15 / 0 |
| 6 | held | 5,832 | 3,888 | 10 / 0 | 0 / 0 | 15 / 0 |
| 7 | held-out-size | 9,261 | 6,174 | 10 / 0 | 0 / 0 | 15 / 0 |

Deleting scatter, clear, or swap changes respectively 2, 1, and 2 register
words at every size. A dirty-buffer full-space input is rejected by the
declared-domain predicate but still recovered by the inverse. Every one of 15
remote two-source collision probes leaves the exactly-one code and is exactly
recoverable. Thus malformed/off-code behavior is visible and reversible; it is not
repaired and is not claimed lawful.

### Route-A covariance scope

- Translation commutators are executed on one frozen lawful register seed for
  all 27, 216, and 343 coarse-cell displacements at L3/L6/L7; failures are zero.
- Register-update commutators are executed on one frozen lawful seed under all
  24 proper-cubic frames at each size; failures are zero.
- All 576 ordered frame products are executed on every site and every one of
  the 16 word labels. This tests the site/word action group law only. It is not
  an all 576 register-update covariance test and not physical covariance.
- All 105 unordered label pairs commute within each scatter and clear
  sublayer; reverse and all24-rotated label enumerations reproduce the same
  sublayer. The fixed scatter-then-clear-then-swap macro remains an explicit
  supplied product, and a schedule is not time.

Route A therefore closes a parity-free logical global stream. It does not
compile simultaneous physical nearest-neighbor placement, a physical encoder,
primitive product, physical intertwiner, physical-code leakage, or a one-site
translation-covariant physical law.

## Route B — direction-expanded partitioned register QCA

Route B allocates outgoing and incoming lanes for all six directions. Local
compact/lane exchange, a role-partition intercell SWAP matching, and a second
local exchange give the exact register stream without parity coloring.

The L3/L6/L7 lawful row counts are 729, 5,832, and 9,261; stream and inverse
failures are zero. A malformed two-source fixture retains two nonzero lanes and
is exactly inverted. All 24 register-update/lane commutators are executed on
one frozen lawful seed per size with zero failures. No all 576 Route-B update
covariance test is executed.

The local exchange is only specified as six disjoint basis transpositions in
a 28-role-bit register block. Its elementary lowering and physical placement
are not executed. The 156 persistent role bits per coarse cell are not M2.

## Route C — state-carried buffer phase

Route C uses two compact buffers and a local phase bit. The phase chooses which
buffer is active, every site toggles its phase, and the decoder alternates
buffers. On the supplied uniform-phase sector,

```text
G_register E_p = E_(1-p) G_coarse,  p in {0,1}.
```

Both phase-zero and phase-one rows pass: 1,458 at L3, 11,664 at L6, and 18,522
at L7. Inverse and two-consecutive-shift failures are zero. A single phase
defect has six disagreeing nearest-neighbor edges. The equality syndrome is
preserved even for a nonuniform phase input, and the malformed full-space
state is inverted.

The uniform phase is supplied, not generated or repaired. Route C executes no
all 24 or all 576 update covariance test, no elementary count, and no physical
M2 compilation. The state-carried phase is a scheduling register; it is not
physical time.

## Finite-precision route

An exhaustive global-phase-quotiented H/T/Tdg search tests 88,572 words through
depth ten for 41 inherited parameterized one-role-bit targets. At depth ten:

```text
worst one-gate ray operator residual = 0.15818455508731935
one-species compiled-coin ray Frobenius residual = 3.940416210503757
logical scratch leakage = 3.831620355454435e-15
weighted per-cell telescoping bound = 44.91804193608823
capped bound = 2
```

The search gives explicit approximants and error bounds. It does not provide
exact Clifford+T closure, asymptotic optimality, a useful global-volume bound,
or physical-code leakage. Wrapped phase is not physical energy.

## Supplied structure and residual ledger

| Item | Status |
|---|---|
| Cycle-600 four-role-bit carrier words and exactly-one/species sector | supplied, byte-pinned |
| Cycle-603 coin/contact/seam fixtures and logical role-event circuits | supplied, byte-pinned |
| Periodic L3/L6/L7 coarse-cell tori | supplied test fixtures |
| Blank secondary buffer and clean logical work | supplied; locally checkable, not generated |
| Route-A register stream, inverse, deletion, collision exit, register EG | directly executed |
| Route-A all24 update commutator | directly executed on one frozen lawful seed per size |
| Route-A all576 site/word group action | directly executed; update covariance not executed |
| Route-B all24 update/lane commutator | directly executed on one frozen lawful seed per size |
| Route-C uniform phase | supplied; not physical time |
| Literal physical M2 placement and primitive product | open |
| Physical encoder/intertwiner/leakage | open; `false`/`null` |
| One-fine-site translation-covariant physical law | open |
| Local enforcement or reversible repair of malformed collisions | open |
| Exact/scalable finite-alphabet synthesis | open |

## No-Go Discipline Gate — N1 through N8

### N1 — five normalized alternative families

Each counted family has a distinct object/mechanism/terminal obligation.

1. `ATTEMPTED`: compact active/buffer registers; equality-controlled
   scatter-clear-swap; exact register stream closes, while physical M2
   composition remains unevaluated.
2. `ATTEMPTED`: direction-expanded Out/In lanes; partition matching; register
   stream closes, while the 28-role-bit exchange is not physically lowered.
3. `ATTEMPTED`: state-carried buffer phase; phase-controlled stream; recurrent
   uniform-sector register shifts close, while phase genesis remains supplied.
4. `ATTEMPTED`: finite H/T/Tdg words; depth-bounded synthesis; explicit nonzero
   residuals remain at depth ten.
5. `RULED OUT BY PRIOR`: independent crossed-link endpoint tables alone;
   Cycle-603 note lines 153-172 explicitly say the six tables are not one
   simultaneous torus update.

An autonomous reversible collision-syndrome/debris reservoir is `OPEN / NOT
COUNTED AS ATTEMPTED OR RULED OUT`. It is the principal counterroute.

### N2 — wall independence

The collapsed walls are: clean register genesis, literal physical M2
placement/product, malformed collision repair/enforcement, elementary
lowering of Route B's exchange, uniform phase genesis, and scalable precision.
All 15 unordered pairs are recorded directionally in the receipt. No closure
implication or shared witness was found, so none is collapsed. This is an
inventory of separate current imports, not a route-independent obstruction.

### N3 — hidden-wall scan

The required phrases `we assume`, `by construction`, `as is standard`, `the
framework provides`, `bridge context`, `background`, `naturally`, `obviously`,
`standard QFT`, and `registered` are absent from the runner proof prose.
`canonical` occurs only as a code-variable name for labels 1 through 15; it is
non-load-bearing because reverse, all24-rotated, and all 105 pair orders are
tested. Blank buffers, clean work, exactly-one sector, uniform phase, frozen
covariance seed, periodic tori, and depth ten are explicit conditions.

### N4 — residual matching

Cycle-603 note lines 167-180 has two residuals: no composed global stream and
no physical M2 intertwiner. Cycle 606 retires only the first at register level;
it does not match or retire the physical residual. Cycle-603 note lines 120-130
matches the parameterized-angle residual; the depth-ten residual remains
nonzero. Cycle-603 note lines 174-190 matches the malformed/physical-leakage
boundary; Cycle 606's collision pairs leave code and physical leakage remains
unevaluated. Nonmatching evidence is not used to support a broad negative.

### N5 — rhetoric at multiple resolutions

The receipt audits per-role, per-event, per-role-line, per-cell, lattice-wide
register, and physical-lattice resolutions. The narrow outcomes are:

- the executed global stream is logical/register only;
- nearest-neighbor means the declared logical role line only;
- register EG is not promoted to a physical intertwiner;
- logical scratch leakage is not physical-code leakage;
- all24 uses one frozen lawful seed and all576 is only the site/word action;
- schedule is not time;
- register counts are not source or energy;
- depth-ten nonzero error is not an impossibility or optimality theorem.

Untested resolutions remain open; no broader negative inherits from them.

### N6 — partial-closure paths

The receipt gives file/status/what-closes rows for Cycles 580, 590, 603, and
606. Cycle 580 shows one literal bounded M2 primitive layout can be constructed
for a different fixture. Cycle 590 gives conditional logical torus placement
but explicitly leaves physical primitive composition open. Cycle 603 gives
bounded local role-event circuits. The next partial-closure path is to
materialize Cycle 606's repeated M2 supercell, physical encoder/product,
one-site covariance, intertwiner/leakage, and lawful-domain gadget. This is a
constructive import-retirement program, not a request for a new axiom.

### N7 — hostile steelman

A hostile reviewer can take the exact compact active/buffer register target,
place its roles in a repeated proper-cubic M2 supercell with directed edge
ports, schedule bounded routed equality-XOR sublayers, retain malformed
collision history in reversible syndrome/debris roles, and replace the depth
ten search with certified epsilon-target synthesis. Cycle 606 finds no
contradiction preventing this route. Its terminal obligation is literal
placement, primitive composition, physical EG/leakage/deletion, held sizes,
and one-site translation covariance. Status is `OPEN / no retained authority`.
This live steelman forces the broad-negative gate to FAIL / DO NOT SHIP.

### N8 — cross-cycle echo

Cycle 560 retired bounded local encoder tables; Cycle 563 retired a runtime
selected-factor ordering service; Cycle 580 retired one bounded gate-layout
import with a literal primitive circuit; Cycle 590 closed a conditional logical
torus macro while preserving the physical-composition boundary; Cycle 603
retired local role-event lowering; Cycle 606 retires the logical global-stream
product. The repeated mechanism is constructive materialization and explicit
import retirement, so constitutional escalation is not justified.

## Final disposition

The strongest result is Route A's exact logical/register global stream. Route B
is an exact register comparator with an unlowered local exchange. Route C is an
exact uniform-phase register comparator with supplied genesis. Precision is
bounded and nonexact. No physical M2 compiler, no broad negative, no minimum
content theorem, no shared obstruction, no breakthrough, and no axiom pressure
is claimed.

The optimal next campaign is a literal repeated M2 supercell with directly
executed one-fine-site translation covariance, physical encoder and primitive
product, physical intertwiner/leakage/deletion, and a local lawful-domain or
reversible collision-syndrome gadget. Only after that should the stream be
composed with Cycle-603 coin/contact and certified epsilon synthesis.
