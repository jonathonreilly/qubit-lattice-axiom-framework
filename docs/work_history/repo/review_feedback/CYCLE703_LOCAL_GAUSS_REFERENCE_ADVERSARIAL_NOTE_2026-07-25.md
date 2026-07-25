# Cycle 703 local-Gauss reference route — adversarial note

**Date:** 2026-07-25

**Reviewed object:** one reference mode `r_x` per coarse cell with
`D_x = B(r_x) product_a B(m_{x,a}) = +1` inside fixed-even BKSF

**Authority:** none

**Audit:** unset

**Status:** local constraint capacity and bounded even-operator construction
positive; physical BKSF common-E state encoder and preparation open

## Verdict

The new local constraint removes the odd/even-volume failure of the older
uniform-reference construction.  For `N` connected coarse cells,

```text
product_x D_x = product_(all 7N modes) B = +1
```

is already the fixed-even BKSF identity.  The `N` displayed constraints
therefore have rank `N-1`, on both odd and even volumes.  Starting from the
`7N-1`-qubit even-Fock representation, they leave exactly `6N` logical
qubits.  Every six-mode matter occupation string has the unique local
reference assignment

```text
n(r_x) = sum_a n(m_x,a) mod 2.
```

Both total matter-parity sectors occur at every volume.  No global matter
parity bit is queried to define this basis bijection.

There is also a bounded dressed nearest-neighbor operator.  For an oriented
matter edge `u=(x,a)` to `v=(y,b)`, let `A_uv` be its BKSF edge generator,
`A_rr` the parallel reference edge, and

```text
P_(y,not b) = product_(c != b) B(m_y,c).
```

With each reference placed after its six matter modes in the local Fock
block, the exact number-preserving hop on the local-D code is

```text
H_uv = - P_(y,not b) (1 - B_u B_v) A_uv A_rr / 2.
```

The corresponding fermionic swap is

```text
FSWAP_uv = (B_u + B_v)/2 + H_uv.
```

The independent companion executes all `4,096` columns of the two-cell
extended-Fock common E for all 36 directed port pairs.  Both formulas match
the independently constructed fermionic target exactly.  The FSWAP is also
executed on all `2^14` extended two-cell basis states for every port pair: it
is a Hermitian involution and preserves both endpoint `D` parities off code.
Deleting `A_rr` violates exactly the two endpoint constraints.  Omitting the
five-spectator parity gives active sign failures, and omitting the
number-sector projector admits pair-creation/deletion branches.

This is a substantive positive result, but it is not yet the full physical
compiler.  The executed common E above is the sparse occupation-basis map
from 12 matter modes to 14 extended fermion modes.  It is **not a BKSF
edge-qubit common-E intertwiner**.  BKSF loop stabilization plus local `D`
leaves three Wilson spectators on a periodic three-torus; fixing all three
gives the exact `6N` dimension.  A stabilizer-rank equality proves that a
finite-dimensional state isometry exists in each fixed Wilson character.  It
does not construct a bounded-radius encoding circuit from matter inputs and
blank physical M2s, prepare the fixed Wilson character, or compare one actual
BKSF physical word with that encoding matrix.

Thus the answer depends on what “state isometry exists without a global parity
bus/order service” means:

- As a finite linear isometry after a fixed Wilson character is supplied:
  **yes**, for odd and even `N`, and no runtime parity query is required.
- As a bounded-radius, locality-preserving physical BKSF encoder from product
  ancillas: **open**.  The Wilson/spin-sector state and its genesis remain
  global resources in the present construction.
- As a bounded representation of the parity-even update algebra: **yes** for
  the tested hop/FSWAP, intracell coin edges, and diagonal contacts.
- As a local representation of the full graded CAR including isolated odd
  creation/annihilation fields: **no such claim is made**.  Disjoint bosonic
  supports commute, whereas remote odd fermion fields anticommute.

No route-independent no-go or axiom pressure is supported.

## Exact rank and sector audit

The companion reuses only the Cycle-232 seven-mode graph and its explicit
BKSF `A/B` Pauli definitions.  It replaces the old uniform-reference rows by
the new cell-local `D_x` rows.  It evaluates open `L=2`, periodic odd `L=3,5`,
and periodic even `L=4`.

For every case:

- every `D_x` commutes with every local loop and Wilson row;
- `product_x D_x` is the phase-free identity Pauli;
- the rank increment is `N-1`;
- deleting any one `D_x` leaves the rank unchanged;
- deleting two rows reduces the rank by one;
- local loops plus `D` leave exponent `6N+3` on the torus;
- adding the three Wilson rows leaves exponent `6N`;
- the stabilizer family has no inconsistent phase relation.

The one-row deletion fact is important.  A closed fixed-even system cannot
use “every `D_x` is independently rank-active” as evidence: exactly one is
globally redundant.  Local enforcement can still include all commuting
penalties, but the genesis and enforcement claim must state this product
relation.

## Bounded operator algebra

For every positive-axis bond on periodic `L=3`, bare `A_uv` anticommutes with
exactly the two endpoint `D` rows.  Multiplying the parallel reference edge
`A_rr` cancels both violations.  The two Pauli terms of `H_uv` then commute
with:

- all local `D` constraints;
- every bounded BKSF loop stabilizer;
- all three supplied Wilson operators.

The maximum Pauli weight is measured by the runner and is independent of
volume because graph degree and the six-mode cell are fixed.  Intracell
matter edges already flip two modes inside one `D_x` and need no reference
edge.  Occupation/contact `B` words are diagonal and commute with `D`.

These checks establish operator-algebra closure.  They do not establish a
state encoder.  In particular, a rank count is not an encoding matrix, and a
commutator table is not a physical residual of the form

```text
|| U_BKSF E_BKSF - E_BKSF U_matter ||.
```

The edge-qubit BKSF Pauli word is therefore executed as exact operator
identities and constraint commutators.  The displayed common E is only the
`12 -> 14` extended-Fock occupation map; it is not the physical M2
intertwiner.

## Wilson and preparation attack

Local loop rows do not fix the three noncontractible torus cycles.  The exact
rank deficit is three for both odd and even held sizes.  All dressed update
words commute with those Wilsons, so dynamics preserves whichever character
is supplied; it does not select one.

This distinction survives the new local `D` construction:

- `D_x` removes the old global matter-parity broadcast;
- it does not prepare a Wilson/spin structure;
- it does not prove finite-depth preparation of the BKSF loop code;
- it does not turn a Wilson label into a local Record or a physical clock.

A valid positive compiler may take a fixed `+++` Wilson vacuum as an explicit
resource.  A stronger genesis claim must supply a local preparation mechanism
or a theorem that the required resource is already physically present.

## Odd/even volume attack

The old uniform-reference law imposed `B(r_x)=B(r_y)` on neighboring cells.
On even `N` it represented two copies of only the even matter sector.  That
failure does not transfer to local `D_x`.

Here the reference bits vary cell by cell.  Their product equals total matter
parity, and total seven-mode parity remains even because every local block has
even combined parity.  Periodic `L=4` therefore has the same exact `6N`
post-Wilson exponent as periodic `L=3,5`.  Reusing the Cycle-232 even-volume
negative against this route would be a false cross-cycle echo.

## Proper-cubic covariance attack

The companion transports the `D` family and both Pauli terms of every directed
dressed hop through all 24 proper-cubic frames.  The fixed local incidence
ordering creates raw mismatches, as expected.  The already explicit local
CZ/Z order gauge repairs the words exactly.  All 576 ordered frame products
compose correctly on vertices and edge operands.

This supports covariance of the directed operator family.  It does not rebuild
or compare the BKSF common E under those frames.  The oriented endpoint used
by `P_(y,not b)` is local program data; a translation/cubic compiler must
transport that direction rather than recover it from a global mode order.
The fixed `+++` Wilson character is invariant as a character, but its physical
preparation remains supplied.

## Common-E boundary

The exact executed layers are:

| Layer | Result |
| --- | --- |
| local occupation map, 12 matter to 14 extended modes | all 4,096 columns exact |
| dressed two-cell hop and FSWAP | all 36 directed port pairs exact |
| full 14-mode FSWAP off-code involution | exact |
| BKSF `A/B` commutators and stabilizer ranks | exact at open/periodic odd/even sizes |
| 24/576 directed operator covariance | exact after local order gauge |

The unexecuted layers are:

| Layer | Missing object |
| --- | --- |
| BKSF edge-qubit state isometry | explicit `E_BKSF` columns/phases in one fixed Wilson sector |
| physical intertwiner | actual `U_BKSF E_BKSF - E_BKSF U_matter` residual |
| leakage | projector or orthogonal-complement residual for the physical word |
| preparation/genesis | bounded circuit or admitted fixed-Wilson resource |
| transformed-E covariance | rebuilt `E_BKSF` and word under frames/translations |
| full graded CAR | bounded odd-field representatives, which are outside the even update claim |

## No-Go Discipline

**Gate result: FAIL for a route-independent no-go.  Ship the layered positive
and open boundary only.**

- **N1 — Alternatives.** The local-D BKSF route, the executed extended-Fock
  parity-compute isometry, a fixed-Wilson resource encoder, an open-boundary
  encoder, higher-form/edge-gauge bosonization, and a non-finite-depth
  stabilizer encoder are materially different routes.  The first two already
  close capacity and bounded even-operator questions, so a broad negative is
  impossible.
- **N2 — Wall independence.** Constraint rank, hop dressing, Wilson selection,
  physical state encoding, preparation depth, transformed-E covariance, and
  odd-field locality are independent obligations.  The three Wilson bits are
  one topological wall, not three separate rhetorical failures.
- **N3 — Hidden conditions.** Fixed total parity of the seven-mode BKSF graph,
  connectedness, one redundant `D`, local incidence ordering, a directed edge,
  six fixed matter modes per cell, bounded graph degree, loop stabilization,
  supplied Wilson character, and the distinction between code and off-code
  action are explicit.
- **N4 — Residual matching.** The 4,096-column residual matches only the
  two-cell extended-Fock common E.  The commutator and rank residuals match the
  BKSF operator algebra and capacity.  Neither is credited as a BKSF physical
  common-E intertwiner or preparation theorem.
- **N5 — Resolution.** Every two-cell matter column and every 14-mode off-code
  FSWAP basis state is tested.  Larger BKSF state columns, arbitrary-volume
  preparation depth, transformed physical encodings, and isolated odd fields
  are not tested.
- **N6 — Partial closure.** Build a stabilizer Clifford isometry for one finite
  periodic size and fixed Wilson character, orient its columns against the
  independent matter basis, and execute one dressed stream word on that common
  E.  Then compare held odd/even sizes and transformed encodings.  This is a
  concrete completion path requiring no axiom edit.
- **N7 — Steelman.** The route has a credible path to a full even-update
  compiler: its dimension is exact at all tested parities, the local hop and
  FSWAP are explicit and deletion-active, and the BKSF graph already supplies
  bounded Pauli representatives.  A pre-prepared fixed-Wilson stabilizer
  resource could close the state layer even if product-state preparation is
  not constant depth.
- **N8 — Cross-cycle echo.** The decisive Cycle-232 even-volume failure came
  from uniform reference equality.  Local `D_x` removes that premise.  The
  surviving Wilson/preparation boundary agrees with later fixed-Wilson work,
  but it is not evidence that the new capacity or hop construction fails.

## Reproduction

```bash
PYTHONPATH=scripts python3 \
  scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py
```

The companion should terminate with
`LOCAL_GAUSS_ALGEBRA_AND_FOCK_ISOMETRY_POSITIVE_BKSF_COMMON_E_OPEN`.
