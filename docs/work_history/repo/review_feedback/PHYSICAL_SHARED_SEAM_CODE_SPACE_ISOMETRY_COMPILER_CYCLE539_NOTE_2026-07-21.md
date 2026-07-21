# Physical shared-seam code-space isometry compiler — Cycle 539

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_shared_seam_code_space_isometry_compiler_cycle539_2026_07_21.py`

## Result

Cycle 539 replaces Cycle 525's rebuilt dense physical code-space completion on
three declared shared-cell patch families with an explicit bounded
**compute/select/uncompute** isometry:

- a three-cell, two-seam straight path through total particle number `n<=3`;
- a three-cell, two-seam right-angle corner through total `n<=3`; and
- a four-cell, degree-three star through total `n<=2`.

The construction combines per-cell branch preparation with one joint S3 or S4
order register, actual selected physical Pauli representatives, and one
injective joint physical-role decoder.  It is exact on the enumerated Cycle-525
code spaces, has constant overhead for each addressed patch, has a literal
one-/two-M2 macro decomposition and nearest-neighbour router, and has a mapped
schedule orbit under all 24 proper-cubic frames at train L5 and held L6.

The strongest identities are

```text
W_path   Gq_path   W_path^dagger   E_path   = E_path   Gcoarse_path,
W_corner Gq_corner W_corner^dagger E_corner = E_corner Gcoarse_corner,
W_star   Gq_star   W_star^dagger   E_star   = E_star   Gcoarse_star.
```

This is a meaningful partial closure, not recurrent volume.  The fixed-Wilson
reference state and its preparation remain supplied.  The path/corner cutoff
does not cover sectors `n=4..18`; the star cutoff does not cover `n=3..24`.
The certificate does not yet compose differently addressed overlapping patches
through an unbounded or periodic volume.

## Why this advances Cycle 525 and Cycle 533

Cycle 525 proved the exact shared-cell target algebra, S3/S4 role constraint,
two-/three-seam update, mass fixture, contact, covariance, inverse, and deletion
controls.  Its physical update was nevertheless rebuilt as

```text
E U E^dagger + I - E E^dagger
```

inside each order block.  That formula supplied an arbitrary dense off-code
completion and was not a primitive physical compiler.

Cycle 533 removed the analogous dense import for one selected two-cell seam by
constructing branch Givens, selected-Pauli SELECT, and a joint decoder.  It did
not show that those ingredients survive a genuinely shared cell or the S3/S4
factor-order algebra.

Cycle 539 supplies exactly that missing patch bridge.  It retains a single set
of three branch M2 per physical cell, including the shared middle/center cell;
it does not clone that cell separately for each seam.  The joint order register
handles the nontrivial factor order coherently, and one decoder sees the whole
bounded patch.

## Explicit circuit

### Per-cell branch preparation

Each physical cell has six persistent occupation-shadow M2 and one clean
three-M2 branch register.  The strict-pinned selected term table has two terms
for 56 occupation words and six terms for the eight three-particle words.
Cycle 533's explicit two-ray construction therefore supplies 96 controlled
Givens and 32 controlled Gray-path `X` macros per cell.

The path and corner use 288 branch Givens; the star uses 384.  Representative
scalar phases are folded into the branch amplitudes.  Direct forward and
reverse state-vector tests establish the preparation and inverse, and deleting
the first special-word Givens produces a nonzero residual.

### Joint S3/S4 order preparation

Cycle 525 showed that independent seam-order registers are incompatible at a
shared cell.  Cycle 539 therefore prepares one joint register:

```text
path/corner:  3 M2, uniform support on the six S3 orders,
star:         5 M2, uniform support on the twenty-four S4 orders.
```

The uniform states are synthesized by five and twenty-three explicit two-ray
Givens, respectively.  The retained order register is a local joint role for
the addressed patch.  It is not a global preferred ordering of the lattice.

### Order-controlled selected-Pauli SELECT

For each order label, Cycle 539 applies the actual strict-pinned cell
representatives in that declared order.  Equality controls include the cell's
six occupation M2, its three branch M2, and the joint order bits.  Applying the
physical representatives sequentially, rather than multiplying only their
supports, retains every local scalar and symplectic crossing phase.

The selected representatives use bounded unions within the addressed patch.
Maximum combined support is 42 M2 for the path/corner and 27 M2 for the star.
No global Jordan-Wigner string, global parity service, host-side branch query,
or runtime order selector is used.

### Joint physical decoder and legality constraint

After SELECT, the physical auxiliary-role pattern and persistent occupation
words determine every cell's branch slot, conditional on the retained joint
order.  Exhaustive exact censuses give:

| patch | logical columns | order-resolved physical rows | native role bits | collisions |
|---|---:|---:|---:|---:|
| path | 988 | 49,728 | 38 | 0 |
| corner | 988 | 49,728 | 38 | 0 |
| degree-three star | 301 | 115,584 | 50 | 0 |

The path/corner branch-product histogram is 964 columns with eight products
and 24 columns with 24 products.  Every star column has 16 products.  The same
normalized decoder tables recur at held L6.

A compile-time equality table XORs the decoded branch slots back to zero.  It
uses 59 equality controls on a path/corner and 79 on a star, with a clean
Toffoli conjunction chain.  The diagonal patch-legality projector contains the
same 49,728 or 115,584 rows and is bounded because the coordination patch is
fixed.  This is a very large constant upper bound, not an efficiency or
minimality claim.

## Exactness on the declared patch code

For a logical patch word `q`, let `A(q)` be the product of the per-cell branch
preparations, `R` prepare the uniform joint order, `SELECT` apply the actual
physical representatives in the order selected by `R`, and `D` erase every
branch register through the injective joint decoder.  Then

```text
W = D SELECT R A.
```

Each stage is an explicit unitary circuit.  The local amplitude vectors and
joint order vector are normalized.  Within every `(q,order)` block, distinct
branch tuples have distinct physical role patterns.  Different q or order
blocks remain orthogonal in retained physical registers.  Therefore `W` is an
isometry on the declared input code, its reverse dagger is an exact inverse,
and all branch/conjunction work ends blank.

Cycle 525's strict-pinned target updates act on the q code.  Conjugating those
explicit q updates by `W` yields the three displayed intertwiners without an
arbitrary dense off-code completion.  Exact repeat-count recurrence follows by
induction for the same addressed patch.  This does not prove that differently
addressed overlapping patches can be alternated across a volume without a new
shared schedule/constraint analysis.

## Preserved physics

The runner re-executes the Cycle-525 path, corner, and star logical update
controls and the Cycle-533 selected-seam fixture controls.  On their declared
low-sector domains these retain:

- the Cycle-219 one-particle mass fixture and uniform rest mode;
- the Cycle-230 contact factor;
- two ordered FSWAP seams on path/corner and three on the star;
- the joint S3/S4 role constraint and update commutator;
- exact inverse and code-space terminal leakage;
- proper-cubic schedule covariance and frame group law; and
- the selected event/current adapter inherited through Cycle 533.

No gate count is called physical time, no phase is called energy, no copied
pointer is called a Record, and no patch isometry is called a full physical
site compiler without its reference and volume obligations.

## One-/two-M2 macros and nearest-neighbour layout

Every equality-controlled `X`, `Z`, or arbitrary one-M2 core uses a clean
conjunction and the strict-pinned exact 15-call Toffoli decomposition.  Negative
controls are opened and closed by one-M2 `X`.  The circuit reports conservative
Toffoli upper counts separately for path, corner, and star.

All native selected roles, q M2, branch M2, joint order M2, and reused clean
work receive explicit distinct integer-microgrid locations.  Every pair of
live locations is routed by ordinary adjacent SWAP, the intended core, and the
reverse route.  For an exactly antipodal periodic coordinate pair, the base
chart uses the positive-direction tie; the all-frame compiler then rotates the
actual chosen edge path rather than recomputing that tie in each frame.  Train
L5 and held L6 test all universal pairs.  The base patch and every route edge
are rotated to a 24-member compile-time schedule orbit.
All mapped wires remain injective, all mapped edges remain nearest neighbour,
and all 576 frame products act consistently.  No runtime frame query occurs.

## Deletion and lawful-domain controls

The certificate distinguishes several load-bearing ingredients:

- deleting a special branch Givens produces a nonzero state residual;
- deleting a joint-order Givens fails the uniform S3/S4 role state;
- deleting one S3 or S4 order block gives exact Gram residual `1/6` or `1/24`;
- deleting the shared middle-cell role inherits Cycle 525's exact residual `1/2`;
- deleting a decoder minterm leaves nonzero branch amplitude;
- deleting a legality minterm rejects one legal ray; and
- deleting a return routing SWAP inherits Cycle 527's dirty-intermediate witness.

Inputs outside the stated L5/L6 nonaliased domains, local occupation words,
path/corner total `n<=3`, star total `n<=2`, clean branch/order/work state, and
fixed reference are not silently coerced into the code.

## Supplied structure and novelty boundary

Supplied rather than derived are the Cycle-525 low-sector target tables and
joint-order algebra, Cycle-533 selected coefficients/Paulis/Toffoli/router, the
fixed-Wilson reference and its preparation, blank q/branch/order/work M2,
compile-time truth tables and analog angles, finite patch addresses, low-sector
cutoffs, and compile-time frame.

New here are the actual cell-shared branch allocation, order-controlled
selected-Pauli circuit, exhaustive joint decoder, patch legality constraint,
inverse/leakage proof, NN layout, and all-frame schedule orbit for the three
Cycle-525 patch families.

This is not a new general bosonization theorem, a gate-count optimum, a
fixed-reference preparation theorem, a full-Fock patch compiler, or a periodic
volume compiler.  Thirring machinery is neither used nor compared.

## Dependency-ledger effect

- `C_ref`: unchanged.  The fixed-Wilson reference and its preparation remain
  supplied.
- `C_num`: advances only on the declared low-sector patch domains; arbitrary
  Fock sectors and volume horizons remain open.
- `C_wrap`: unchanged.  Patch schedules and order registers are not time,
  history, energy, or Records.
- `C_int`: advances.  Mass, contact, two-/three-seam updates, and inverse now
  sit behind explicit patch isometries instead of dense completions.
- `C_local`: advances materially.  The dense shared-cell completion is removed
  on path, corner, and star patches with bounded constraints, NN macros, and
  all-frame schedules.  Reference genesis and differently overlapping volume
  recurrence remain.
- `C_source`: unchanged.

There is no shared obstruction and no axiom pressure.

## Cold certificate

The independent certificate passed **10/10** test families in
`41.54437829100061` internal seconds (`43.09` timed wall seconds), reached
`432,160,768` maximum RSS bytes, and reported zero process swaps.

Selected exact resource upper bounds are:

| patch | live M2 | SELECT Pauli factors | decoder controls | `W^dagger+W` Toffoli upper bound |
|---|---:|---:|---:|---:|
| path | 205 | 52,374 | 59 | 19,896,368 |
| corner | 205 | 52,734 | 59 | 19,911,488 |
| degree-three star | 273 | 287,616 | 79 | 86,057,236 |

These are deliberately conservative constant upper bounds.  Every one of the
20,910 path/corner and 37,128 star live-wire pairs was routed at L5 and held
L6.  Maximum route length was 64 nearest-neighbour edges; mapped-edge,
wire-injection, and 576-product failures were zero.

Branch preparation residual was at most `1.5700924586837752e-16` and inverse
residual at most `2.4196749845665633e-16`.  The S3 order preparation residual
was `3.764949453935611e-16`; the S4 residual was
`5.661048867003676e-16`.  All normalized joint-decoder digests matched between
L5 and L6.

The re-executed path/corner rest mass is exactly
`0.4534056541748851`, matching the Cycle-219 fixture, with uniform one-particle
residual `3.534751832054436e-16`.  The star value is
`0.45340565417488515` with residual `2.4097051235218626e-16`.  All patch update
frame residuals are zero.  The selected-seam coin/contact residuals remain
`5.0207498326926886e-15` and `2.149937642474629e-15`; recurrence and inverse
remain `1.5416528402018934e-15` and `1.1429443574931856e-15`.

## No-go discipline N1–N8

The broad no-go gate is **FAIL / DO NOT SHIP**.  Cycle 539 is constructive on
its declared patches and leaves several extension routes open.

### N1 — alternative-route normalization

The joint S3/S4 auxiliary route is positive.  A cell-shared colored-volume
schedule, full-sector algebraic compiler, rough-gauge reference initializer,
and staggered/time-multiplexed volume law remain distinct open routes.  The
bounded patch result cannot decide any of them negatively.

### N2 — wall-independence audit

Low-sector completeness, full-Fock completeness, fixed-reference genesis,
same-patch repeat recurrence, differently overlapping patch recurrence, and
periodic-volume tiling are separate obligations.  The explicit patch `W`
closes only the dense-isometry obligation on the enumerated patch code.

### N3 — hidden-wall scan

The fixed reference, blank registers, selected coefficient table, truth table,
rotation angles, q input, joint-order initialization, patch address, low-sector
cutoff, finite periodic domain, frame choice, integer microgrid, and router are
listed as supplied.  No host callback or global ordering is hidden in `W`.

### N4 — residual matching

Zero decoder collisions diagnose injectivity of this branch-erasure circuit.
Zero inverse/leakage diagnoses the declared code-space isometry.  Cycle 525's
dense-completion residual is retired only on these patches.  None of these
residuals diagnoses fixed-reference genesis or arbitrary-volume recurrence.

### N5 — rhetoric audit

The retained terms are “bounded patch,” “declared low sectors,” “code-space
isometry,” and “partial closure.”  The result does not say full Fock, recurrent
volume, derived time/energy/Record/Born/gravity, minimum content, impossibility,
or constitutional requirement.

### N6 — partial-closure path

Retain the explicit path/corner/star `W`, its patch legality constraints, and
the exact q update.  Next construct a cell-shared edge-color schedule for
differently overlapping patches, then widen the sector census.  Separately
attack the fixed-Wilson reference initializer.

### N7 — hostile steelman

A stronger compiler can reuse one per-cell branch register across a covariant
edge coloring, retain bounded order roles only during the active local layer,
and prove alternating-layer recurrence on a periodic volume.  The present
injective decoders make that route more plausible; they do not prove it.  A
rough-gauge initializer could also close the reference wall independently.

### N8 — cross-cycle echo

Cycle 525 had exact shared-cell physics but a dense physical completion.
Cycle 533 had an explicit physical isometry but only one selected seam.  Cycle
539 composes those complementary strengths on three bounded patch families.
Earlier route-specific failures were repeatedly bypassed by joint auxiliaries,
so no remaining patch or reference wall supports axiom pressure.

## Disposition and next campaign

Retain Cycle 539 if its independent certificate passes.  The highest-value
next compiler experiment is a six-color or other proper-cubic cell-shared
volume schedule that alternates these explicit patch isometries without
duplicating shared q/branch/reference M2.  Test a periodic multi-star domain,
arbitrary repeat count, full constraint preservation, inverse/leakage,
deletions, held size, and all 24 frames.  In parallel, continue the independent
fixed-Wilson reference-preparation tournament.
