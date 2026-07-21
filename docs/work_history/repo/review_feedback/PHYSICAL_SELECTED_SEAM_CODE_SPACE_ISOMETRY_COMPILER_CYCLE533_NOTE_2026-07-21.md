# Physical selected-seam code-space isometry compiler — Cycle 533 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py`.

## Result

Cycle 533 replaces Cycle 530's arbitrary dense normal-form completion **on the
declared E12 code image** by an explicit reversible
**compute/select/uncompute** circuit.  The construction is exact, has bounded
support and constant (though very large) overhead per selected two-cell seam,
uses only local physical controls, has a nearest-neighbour one-/two-M2 macro
decomposition, and has a 24-member compile-time proper-cubic schedule orbit.
It is a code-space isometry compiler, not an arbitrary
`2^95 x 2^95` unitary synthesis.

The strongest identity is

```text
W G_q W^dagger E12 = E12 G_coarse .
```

Here `G_q` is the strict-pinned Cycle-530 primitive selected-seam core.  `W`
is the new circuit below.  `W^dagger` is literally its reverse dagger, not a
second supplied dense map.

This is a meaningful partial closure, not full campaign success.  The
fixed-Wilson reference state and its initial preparation remain supplied, as
do the strict-pinned selected coefficients, the persistent occupation-shadow
inputs, and blank route-work initialization.  Simultaneous recurrent-volume
shared-seam consistency is also open.  Cycle 533 therefore does not call the
reference preparation wall closed and does not call this conditional
code-space compiler an unconditional physical-site compiler.

## Why the direct branch-pair rotation was rejected

The first attempted construction chose one anchor ray in each q block and
tried to isolate every other ray with native bits that are invariant between
the two rays.  There are 25,600 structural rays in 4,096 q blocks, hence
21,504 candidate eliminations.  The exact census was:

| item | count |
|---|---:|
| separated by an invariant native-bit conjunction | 15,360 |
| no such conjunction | 6,144 |
| maximum successful separator width | 9 |

The 6,144 failures falsify that direct construction as a universal compiler.
They do not falsify local gauge/auxiliary compilation: branch registers and a
joint decoder avoid the separator premise entirely.  Cycle 533 does not
silently replace those failures with generic finite-dimensional QR on 95 M2.

## Explicit circuit W

### 1. Compute exact local branch amplitudes

For each cell, the six persistent Cycle-527 q shadows select one of 64 local
occupation words.  Strict-pinned `selected_gauge_terms` supplies two terms for
56 words and six terms for the eight special three-particle words.  A clean
three-M2 branch register therefore suffices.

For each q word, the runner constructs the exact complex length-eight vector
from those terms.  The representative phase `i^phase` is folded into the
branch amplitude.  Successive explicit two-ray Givens rotations between slot
zero and each occupied slot prepare that vector.  Across both cells this is
192 Givens rotations.  Their inverse reconstruction residual and their
forward state-preparation residual are tested directly.

Each two-ray rotation on a three-M2 register is compiled by a Gray path.  The
Gray permutations and the final two-level core are equality-controlled by the
six physical q M2.  The complete two-cell schedule uses 64 controlled Gray
`X` macros and 192 controlled two-M2 rotation cores.  The controls are quantum
M2, not a runtime host branch.

### 2. SELECT the actual bounded physical Pauli representatives

For each of the 160 `(q,slot)` entries per cell, the circuit equality-selects
the corresponding strict-pinned physical Pauli representative.  Since its
explicit scalar phase was folded into the prepared coefficient, the selector
needs only its listed `X` and `Z` factors.  On a site carrying both, it applies
`Z` and then `X`, realizing the declared `XZ` convention.

The right-cell selector is applied before the left-cell selector.  Thus the
physical operator is exactly `P_left @ P_right`, including their local
symplectic crossing phase.  This is a bounded oriented-edge convention, not a
global Jordan-Wigner ordering.  The selected single-cell support is at most
35 M2; the combined selected representative is at most 63 M2; and the union
over the selected two-cell table is 81 native M2.

No global parity service, global parity string, preferred ordering of the
volume, or host-side branch control is used.

### 3. Uncompute the branch registers from a joint local lookup

The two cells expose 28 named native role positions with two overlaps, hence
26 unique role M2.  For each q word, the map

```text
(left branch slot, right branch slot)
    -> (q12, native-role26 pattern)
```

is injective.  The L5 and held L6 exhaustive results are identical:

| q-block ray count | q blocks |
|---:|---:|
| 4 | 3,136 |
| 12 | 896 |
| 36 | 64 |

All 25,600 `(q12,native-role26)` code rows are unique.  A compile-time truth
table therefore XORs the decoded three-bit left and right slots into the
branch registers and returns all six branch M2 to zero.  Every minterm is a
38-control MCX and has the standard clean-ancilla Toffoli-chain
decomposition.  No oracle or runtime classical service is present.

The simpler one-cell Cycle-523 relational decoder cannot be substituted after
the overlapping product: it fails 22,272 of 51,200 cell/ray tests because the
other cell changes shared native roles.  That is why Cycle 533 uses the
explicit bounded two-cell decoder.  This failed substitution is recorded,
not hidden.

## Exactness proof on the declared code space

Let `A(q)` be the product of the two exact branch-state preparations, `SELECT`
apply the phase-adjusted right and left representatives, and `D` be the joint
injective branch decoder.  Starting with the fixed-Wilson reference `Omega`
and blank branch/work M2,

```text
D SELECT A(q) |q>|Omega>|0_branch>|0_work>
  = E12 |q>|0_branch>|0_work> .
```

The selected amplitudes are normalized.  Distinct terms within one q block
have distinct joint native role words, and q makes rows from different blocks
orthogonal.  Direct sparse reconstruction gives exactly 25,600 E12 nonzeros,
25,600 occupied augmented rows, and zero Gram residual at both L5 and held L6.

Every circuit stage is unitary, the decoder is a reversible XOR table, and
all conjunction work is uncomputed.  Therefore reverse dagger gives
`W^dagger W = I` on the q/reference/blank input code and `W W^dagger = I` on
E12.  Combining this with the strict-pinned Cycle-530 `G_q` intertwiner gives
the displayed update identity.  Arbitrary repeat-count selected-seam
recurrence follows by induction, with zero branch, conjunction-work, and code
leakage on the declared lawful code.

This proof specifies the required action and an actual gate circuit.  It does
not choose an arbitrary dense off-code completion.  The circuit of course has
a definite reversible off-code action, but no claim is made that this action
has independent physical meaning.

## Local constraints

The strict-pinned representatives commute with the Cycle-522 port constraints,
local face checks, and fixed-sector operators.  Cycle 533 adds the explicit
bounded diagonal legality projector `C_E` onto the 25,600 listed
`(q12,native-role26)` words.  `C_E` touches 38 M2 in one selected two-cell
neighbourhood.  Its syndrome circuit uses the same equality-minterm MCX chain,
a local flag, and reverse uncomputation.  Deleting one legal minterm causes
exactly one listed ray to be rejected.

Branch and conjunction-work M2 have local blank-state checks and return blank.
These are locally checkable auxiliary constraints.  The fixed-Wilson sector
is preserved but its initial reference preparation is still an explicit
nonlocal/supplied boundary; Cycle 533 does not relabel that import as local
enforcement.

## Primitive and nearest-neighbour realization

An equality-controlled `X` with `k` controls uses `k-2` clean work M2 and
`2k-3` Toffolis.  An equality-controlled arbitrary one-M2 core computes and
uncomputes the conjunction and uses one controlled two-M2 core.  Each
Toffoli is the exact 15-call Cycle-523/Cycle-527 schedule.  Negative equality
controls are opened and closed with one-M2 `X` calls.  At most 36 clean
conjunction-work M2 are live.  The compiler live-wire upper bound is therefore

```text
81 native + 12 q + 6 branch + 36 reused work = 135 M2
```

inside the already supplied `16 x 16 x 16` integer microgrid per coarse cell.
This is constant overhead, not an efficiency or minimality claim.  The runner
reports the exact high-level macro counts and a conservative Toffoli count.

Every resulting two-M2 call is routed along a deterministic periodic
Manhattan path with ordinary tensor-factor SWAP, one core call, and the reverse
SWAP path.  Intermediates may carry data: the reverse path restores them
exactly.  All pairs among the 135 live locations are checked, giving a bounded
maximum path and zero non-nearest-neighbour edges at L5 and L6.  Fermionic
FSWAP remains only the Cycle-530 CAR braid; ordinary routing SWAP is not
misnamed FSWAP.

## Proper-cubic covariance

The selected local shell and its physical branch representation are rechecked
under all 24 proper-cubic frames at both L5 and held L6.  Branch, selector,
normalization, and 576 frame-product failures are zero.  The new circuit has a
24-member compile-time schedule orbit: transform every q role, selected Pauli
selector, branch/work placement, and nearest-neighbour route edge by the
chosen proper frame.  Rotation is injective and every mapped route edge is
still nearest neighbour.  No runtime frame query is used.

This is a mapped schedule orbit.  Cycle 533 does not claim one
frame-independent gate order.  Endpoint ordering is mapped with the oriented
edge and is not extended to a global preferred ordering.

## Deletion, leakage, inverse, and held-size controls

The certificate includes the following discriminators:

- deleting the first nontrivial special-word Givens gives a nonzero state
  residual;
- deleting a selected representative entry leaves a branch/native mismatch;
- deleting a branch-erasure minterm leaves nonzero branch amplitude;
- deleting a legality minterm rejects one otherwise legal ray;
- deleting a return routing SWAP inherits Cycle 527's dirty-intermediate
  witness;
- exact reverse dagger gives zero branch/work leakage and exact code recovery;
- every structural count, normalized lookup pattern, and preparation program
  recurs at held L6.

Cycle 530 already tests preservation of the Cycle-219 one-particle mass
fixture, Cycle-230 contact, exact 13-FSWAP seam block, and Cycle-526 adapter by
`G_q`.  Replacing dense `S` by exact `W` leaves those residuals unchanged.
Cycle 533 does not call a wrapped phase physical energy, a generator element a
rate, a pointer copy a Record, or this selected code-space result a complete
recurrent-volume physical compiler.

## Supplied structure and novelty boundary

| supplied item | use |
|---|---|
| Cycle-522 selected coefficients and Pauli representatives | exact branch amplitudes and SELECT table |
| Cycle-523 occupation-shadow decoder and exact Toffoli | persistent q input and primitive boolean compilation |
| Cycle-527 installed integer microgrid and ordinary router | NN realization and clean route work |
| Cycle-530 E12 and `G_q` factorization | target code and selected-seam physical core |
| fixed-Wilson reference and its initial preparation | reference on which selected Pauli rays are built |
| blank branch/route-work initialization | reversible compute workspace |
| compile-time truth tables and exact rotation angles | large finite local program data |

The new content is the explicit factorization of the E12 code-space isometry
into branch preparation, actual bounded selected-Pauli SELECT, joint physical
decoder erasure, local legality syndrome, inverse, NN routing, deletions, and a
proper-cubic schedule orbit.  The result does not derive the supplied
coefficients or fixed-Wilson reference preparation.  It also does not claim
gate-count optimality.

## Cold certificate

The final cold certificate passed **12/12** declared test families in
`152.55803033302072` seconds, reached `562,806,784` maximum RSS bytes, and
reported zero process swaps.  Selected exact outputs were:

| control | result |
|---|---:|
| local branch Givens, both cells | 192 |
| controlled Gray-path `X` macros | 64 |
| selected Pauli lookup entries | 320 |
| controlled single-Pauli factors | 5,778 |
| joint branch-erasure MCX minterms with nonzero target bit | 35,840 |
| legality-projector minterms | 25,600 |
| forward-`W` conservative Toffoli count | 2,706,510 |
| `W^dagger` plus `W` conservative Toffoli count | 5,413,020 |
| live-wire upper bound | 135 M2 |
| universal live-wire pairs routed per size | 9,045 |
| maximum route length | 48 NN edges |
| all-24 mapped NN edge failures | 0 |
| E12 Gram residual, L5 / held L6 | 0 / 0 |
| branch/work terminal leakage | 0 / 0 |

The L5 and held-L6 state-preparation schedule digest is
`543b6b0a075b6a17b591670e9bd8ad0011d505c777ab0ffcb97cbc1d7605fe76`.
The normalized joint decoder digest at both sizes is
`6051f73d74b899b7df70e75d5757636135ce5cf41222a03f9d10df1562466391`.

The rechecked Cycle-219 coin residual is
`5.0207498326926886e-15`; the compiled rest mass is
`0.453405654174885` against fixture `0.4534056541748851`, with uniform
one-particle residual `8.7159799596118e-16`.  The Cycle-230 contact residual is
`2.149937642474629e-15` with 4,047 nontrivial columns.  Each spatial axis has
13 FSWAP factors, 4,096 exact columns, and zero braid intertwining residual.
The 32-vector two-step recurrence maximum is `1.5416528402018934e-15`, and
the inverse maximum is `1.1429443574931856e-15`.  All 65,536 Cycle-526 blank
output/data/K tests pass without calling retained-bank reuse a fresh Record.

## Route disposition

| route | Cycle-533 disposition |
|---|---|
| direct even-CAR / invariant pair rotations | **FAILED AS TESTED:** 6,144 of 21,504 pairs lack the required separator; generic dense QR is not substituted |
| local gauge/auxiliary compute/select/uncompute | **CONSTRUCTIVE PARTIAL CLOSURE:** exact on E12, bounded, NN, recurrent for one selected seam, all 24 frames, fixed reference still supplied |
| stabilizer/gauge-fixing Clifford plus syndrome rotations | **OPEN:** may compress the 25,600-row truth table or derive reference preparation |
| Gray paths through off-code native rays | **OPEN:** not needed for the positive route and not tested as a reference-preparation engine |
| staggered/time-multiplexed compiler | **OPEN:** still must close autonomous phase/schedule and shared-volume recurrence |

## N1–N8 no-go discipline

N1 — **Alternative-route map.**  Cycle 533 separately tracks invariant
pair rotations, explicit branch-register compute/select/uncompute,
stabilizer/gauge fixing, off-code Gray paths, and staggered/time-multiplexed
routes.  The priority gauge/auxiliary route is constructive; several other
routes remain open.

N2 — **Wall-independence audit.**  Four different walls must not be conflated:
the 6,144 separator collisions, the now-closed dense-S-on-code factorization,
the still-supplied fixed-Wilson reference preparation, and simultaneous
shared-seam volume recurrence.  None implies the others.

N3 — **Hidden-wall scan.**  The construction explicitly inventories the
selected coefficient table, exact analog rotation angles, fixed reference,
persistent q shadows, blank branch/work M2, compile-time frame choice, finite
truth table, microgrid, and router.  The 38-M2 legality constraint is local but
large.  Initial reference preparation is not derived.

N4 — **Residual matching.**  The 6,144 residual belongs only to the invariant
separator ansatz.  The 22,272/51,200 decoder residual belongs only to reuse of
the one-cell decoder after an overlapping product.  The joint decoder has zero
collisions and the E12 Gram residual is zero.  Neither failed residual matches
a route-independent substrate obstruction.

N5 — **Rhetoric audit.**  The retained words are “code-space isometry,”
“selected seam,” “given the fixed reference,” and “partial closure.”  The note
does not say arbitrary-unitary synthesis, full recurrent volume, derived
reference vacuum, constitutional minimum, impossibility, or axiom requirement.

N6 — **Partial-closure and primitive scan.**  The compute/select/uncompute
route removes Cycle 530's dense `S` import on E12 and exposes exact one-/two-M2
macros.  Stabilizer preparation, decoder compression, and staggered schedules
remain possible improvement routes.  This constructive partial closure blocks
a negative conclusion.

N7 — **Steelman.**  A stronger program could derive the fixed-Wilson reference
from locally initialized M2, replace the truth table with a short covariant
stabilizer circuit, and prove simultaneous colored shared-seam recurrence.
Nothing in Cycle 533 excludes that outcome; the present circuit is an explicit
upper bound, not a minimum.

N8 — **Cross-cycle echo.**  Cycles 522, 523, 527, and 530 progressively removed
carrier, decoder, routing, and `G_q` walls.  Their prior route-specific failures
did not survive later constructive changes.  Cycle 533 repeats that lesson:
the separator and one-cell-decoder failures are bypassed by a joint auxiliary
construction.  No route-independent no-go survives the cross-cycle record.

Gate status for a broad impossibility, minimum-content, or axiom-pressure
claim: **FAIL / DO NOT SHIP**.  There is no shared obstruction and no axiom
pressure from Cycle 533.

## Dependency-ledger effect

`C_local` advances materially: the selected-seam dense normal-form import is
replaced on code by an explicit bounded NN circuit, with local terminal
legality checks, inverse, deletions, L5/held-L6 recurrence, and all 24 frames.
It is not closed because fixed-reference preparation and simultaneous
shared-seam volume recurrence remain.  `C_ref`, `C_num`, `C_wrap`, `C_int`,
and `C_source` do not change in this cycle.  In particular, a circuit-resource
count is not physical time or energy, and the event/current adapter is not a
gravity-source derivation.

The highest-value next campaign is a constructive fixed-Wilson reference
preparation and gauge-fixing compiler from locally initialized M2, tested
against the same two-cell E12 target and then against a genuinely simultaneous
three-cell/two-edge recurrence patch.  Truth-table compression is useful, but
reference preparation and shared-seam consistency are the scientific walls.
