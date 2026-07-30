# Cycle 821: local parity-exchange carrier for the recurrent Bell prefix

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded constructive theorem

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.py`](../scripts/frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.py)

Independent checker:

- [`frontier_cycle821_local_parity_exchange_carrier_independent_2026_07_30.py`](../scripts/frontier_cycle821_local_parity_exchange_carrier_independent_2026_07_30.py)

Receipt and runner caches:

- [`local_parity_exchange_carrier_recurrent_bell_cycle821_receipt_2026_07_30.json`](../outputs/local_parity_exchange_carrier_recurrent_bell_cycle821_receipt_2026_07_30.json)
- [`frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.txt`](../logs/runner-cache/frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.txt)
- [`frontier_cycle821_local_parity_exchange_carrier_independent_2026_07_30.txt`](../logs/runner-cache/frontier_cycle821_local_parity_exchange_carrier_independent_2026_07_30.txt)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Circuit stages, microsteps, colours, and epochs below are supplied circuit and
verification order. They are not physical time, duration, cadence, rate, or
energy.

The carrier input is initially factorized from the channel input, and the pump
and Bell syndrome controls begin in the declared clean, definite stabilizer
states. On a coherent syndrome/carrier input the same circuit implements a
controlled-`X` joint channel; the scalar conditional carrier law below is not
claimed on that larger process domain.

## Direct scientific dependencies

- the landed [Cycle-720 recurrent companion physical-M2 update and local Choi
  preparation](./RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md);
- the landed [Cycle-789 three-register companion input
  circuit](./THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md);
- the landed [Cycle-794 literal prefix plus recurrent-G modular
  composition](./LITERAL_THREE_BANK_PREFIX_RECURRENT_G_ACTUAL_SHEAR_CYCLE794_BOUNDED_THEOREM_NOTE_2026-07-30.md); and
- the landed [Cycle-820 two-cell parity-superselected even-CAR
  covariance](./FULL128_TWO_CELL_PARITY_SUPERSELECTED_EVEN_CAR_COVARIANCE_CYCLE820_BOUNDED_THEOREM_NOTE_2026-07-30.md).

## Result up front

Cycle 820 exposed twelve physical-matter-parity-odd private-dual corrections
among the 23 rows of the two-cell companion Bell channel. This package closes
that bounded gate defect by adding exactly one typed carrier M2 mode per
coarse cell. For a correction row `D_j` owned by cell `c`, define

```text
D_tilde_j = D_j X_c^epsilon_j,
epsilon_j = 1 exactly when D_j is odd under physical matter parity.
```

The protected grading is the extended parity

```text
P_ext = P_matter product_c Z_c.
```

Every extended correction commutes with `P_ext`. No carrier eigenvalue is
queried or selected. One carrier is shared by all six odd rows owned by a
cell; a six-carrier-per-cell bank is unnecessary on the tested code.

The primary runner executes two consecutive pump/Bell/correction epochs on
the same dirty carrier pair. It closes the complete signed rank-23 channel on
the base `(2,1,1)` fixture and the rank-152 channel on the held `(3,2,2)`
fixture with zero binary or signed-span failures. A second executor starts
from the declared clean O/I resource stabilizers and executes pump, Bell, and
correction in one parity-audited word: 848 elementary gates on `(2,1,1)` and
7,520 on `(3,2,2)`, with zero elementary parity-commutator failures and zero
channel failures after either epoch.

The exact conditional carrier law after an epoch is

```text
rho_c -> X_c^r rho_c X_c^r,
```

where `r` is the xor of the six pump and six Bell odd-row syndromes in that
cell. Thus `X_c` is invariant while `Y_c` and `Z_c` retain `r`. The carrier is
reusable, but it is not reset. The two-epoch carrier channel is the identity
for every carrier input exactly when the two local exchange parities xor to
zero. When the xor is one, state-specific `X_c`-invariant inputs are fixed even
though the channel is not the identity.

The independent checker reconstructs the channel without importing the
primary. Its rank-46 fixture is two disjoint channel copies that share the
same carriers; it is not the primary executor's output-fed second epoch. It
tests the 16-product density-spanning carrier inputs
`{I/2,X+,Y+,Z+}^{tensor 2}`, plus Bell `Phi+` and singlet carrier states. All
outputs have the expected rank 46 across the two shared-carrier copies, with
zero binary, signed, rank, or carrier-update failures. Across all 24
proper-cubic frames and the 16 product carrier states, 384 frame/state contexts
and 552 mapped corrections close with zero private-duality, parity, rank,
support, or channel failures.

## Exact parity-even gate compiler

Cycle 820's correction rows contain controlled pairs of odd Pauli letters.
For each pair `A = A_left A_right`, choose a pivot and define

```text
K = -i A Z_pivot,
U = exp(-i pi K / 4).
```

Then the controlled pair is implemented exactly as

```text
C(A) = U^dagger CZ(control,pivot) U.
```

The primary and independent paths test all `XX`, `XY`, `YX`, and `YY` cases.
The maximum identity and conjugacy residual is
`6.312164422641715e-16`. Every emitted factor and every cumulative prefix has
zero `P_ext` commutator. The independent checker compiles all 552
frame-resolved corrections into 2,448 factors with zero pairing,
reconstruction, factor-parity, or prefix-parity failures.

This is an exact bounded two-target rotation compiler. It is not yet a
nearest-neighbour or radius-one synthesis of `U` in the landed H/CNOT/CZ/SWAP
dictionary. The primary placement has maximum bounded atom diameter 33 and
maximum carrier/correction pair diameter 19. Those constant bounds are
reported as supplied finite-range structure, not hidden as nearest-neighbour
locality.

## Composition with recurrent G

On the declared even-observable code, the constructive equations are

```text
E B_even = B_physical E
```

for two prepared pump/Bell/correction epochs, and by exact postcomposition on
the identical O coordinates,

```text
E (G B_even) = (G_physical B_physical) E.
```

The second equality is a signed-graph/factorwise composition theorem, not a
dense full-width matrix execution. It imports the landed Cycle-794 proof that
the complete signed Choi graph fixes the even-CAR channel and that equality
survives linear postcomposition by the recurrent Cycle-720 update.

This package adds a parity audit of the recurrent factor dictionary. Coin,
reverse-FSWAP, and contact factors commute with matter parity. Each seam
semantic factor is an exact bounded `exp(-i pi P/4)` for a parity-even physical
Pauli `P`. On `(2,1,1)`, held `(3,1,1)`, and held `(3,2,2)`, the direct factors
have zero parity failures, maximum support 17 M2, maximum physical Manhattan
diameter 24, and maximum deterministic-sample phase-aligned state residual
`7.913391346636907e-16` between the semantic factor and the submitted seam
decomposition. The old H/CNOT decomposition is an active hostile control: it
contains respectively 24, 48, and 912 parity-noncommuting elementary seam
instructions.
Replacing it by the exact semantic rotations preserves the update, but a
nearest-neighbour parity-even synthesis of those up-to-17-M2 rotations remains
open.

The one-particle mass residual remains `5.551115123125783e-17`. The imported
Cycle-794 box certificate supplies the landed free/seam/contact recurrent-power
rows through powers `(1,2,3,5,8)` on two cells and `(1,2,3)` on held three
cells. Cycle 821 independently re-gates the recurrent seam-factor parity and
sampled-state residuals plus the mass fixture; it does not re-run Cycle 794's
broader deletion, dirty-state, order, or leakage mutation suite.

## Placement, covariance, and controls

The dedicated carrier has identity-frame chart offset `(3,-7,-4)`, transported
with the supplied coframe under a proper-cubic change of frame. It is not held
at `(3,-7,-4)` in laboratory coordinates under an active rotation. The palette
grows from 64 to 65 M2 per coarse cell. On `(2,1,1)`, `(3,2,2)`, and `(5,3,2)` the
primary reports zero palette, active-G, return-label, same-block,
same-colour-slot, or carrier ownership collisions. The independent literal
schedule repeats this on `(2,1,1)` and held `(6,5,4)` with zero routed-path,
return, target, palette, carrier/G, or block failures.

The carrier's internal X/Z label is a cell scalar, while its physical site is
coframe-transported. The primary checks 192 frame/origin contexts, 384 carrier
comparisons, and all 576 ordered frame products with zero carrier permutation,
origin, physical-offset, physical-palette, distance, or cocycle failures. The
hostile rule that incorrectly keeps the identity-frame offset fixed in
laboratory coordinates is detected in 23 of the 24 frames. The
independent checker transports the complete correction compiler through all 24
frames and 16 carrier states. It does not re-execute the whole 24-by-24 signed
atom word for every frame product, so the landed Cycle-820 and Cycle-794
576-product theorems remain load-bearing for the composed claim.

All 23 second-epoch correction deletions are detected with minimum failure
two. The independent checker separately deletes the matter leg, carrier leg,
or full row for all twelve odd pump rows and twelve odd Bell rows. Carrier-only
deletion is intentionally invisible to the reduced output but parity-detected
in all 24 cases; matter-only and full deletions change the output. This active
control demonstrates why reduced-channel equality alone cannot certify the
physical grading.

## Route tournament disposition

- **Route A, dedicated local carrier:** a positive bounded construction on the
  declared domain, proposed in this package.
- **Route B, borrowing an existing companion gauge register:** no Route-B
  theorem or negative result is submitted in this package. Earlier exploratory
  diagnostics are not used as evidence for the Route-A claim.
- **Route C, staggered/two-rail transport:** no Route-C transport/update theorem
  or negative result is submitted in this package. The route remains untested
  here.

No impossibility, minimum-content, shared-obstruction, or axiom-pressure claim
is made.

## Supplied / derived / open

### Supplied

- one typed carrier M2 per coarse cell and total extended-parity
  superselection as the observable domain;
- an initial carrier state factorized from the channel input and clean,
  definite pump/Bell syndrome stabilizer inputs;
- the landed O/I Choi resource, independent encoded live bank, clean pump and
  Bell syndrome banks, local center/mixed-gauge domain, and permission to
  retain the dirty carrier;
- the finite chart, identity-frame `(3,-7,-4)` carrier offset and its supplied
  coframe transport, local tag/private-dual atlas,
  proper-frame/coframe templates, finite boundary, colour/slot dictionary,
  and fixed stage order;
- the Cycle-230 coin/contact parameters, landed seam convention, and
  Cycle-720 recurrent factor dictionary; and
- bounded two-target and up-to-17-target semantic rotations as exact allowed
  local factors, without a radius-one synthesis theorem.

### Derived

- one carrier per cell is sufficient for all six local parity-odd rows;
- exact two-epoch pump/Bell/correction execution without a carrier value query
  or reset, including the explicit retained-carrier update law;
- an exact parity-even `U^dagger CZ U` compiler for all two-letter Bell and
  correction atoms, with all factors and prefixes parity preserving;
- a collision-free 65-M2/cell bounded palette and the stated proper-cubic
  covariance surfaces;
- exact modular recurrent-G composition on the identical output coordinates,
  including parity-even bounded seam semantic factors; and
- active Cycle-821 deletion, dirty-carrier, missing-parity-leg, held-shape,
  mass, seam-factor parity/sample, and hostile-decomposition controls. The
  broader Cycle-794 mutation suite is parent evidence and is not re-run here.

### Open

- autonomous genesis and local enforcement of the carrier modes, total-parity
  domain, O/I and live resources, clean syndromes, coframe, and occurrence;
- a parity-balanced carrier reset/renewal or a law that admits the dirty
  carrier state across unbounded epochs;
- nearest-neighbour/radius-one synthesis and routing of the bounded Bell and
  recurrent seam rotations;
- one monolithic dense/state executor for preparation, Bell/correction, and
  non-Clifford recurrent `G`, rather than the exact signed-graph/factorwise
  composition theorem;
- translation-invariant lattice-wide gluing, duplicate-view ownership,
  fault rejection, and repair; and
- the causal-time, source/gravity, Record/Born/history, and no-refit prediction
  bridges.

## Verdict

The two-cell physical parity-exchange defect exposed by Cycle 820 has a
bounded constructive solution: one local carrier M2 per cell and an exact
parity-preserving two-target compiler. The prepared even-CAR channel now
composes with recurrent `G` without a global parity string, fixed parity value,
or host-side parity service. Within this submitted construction, the following
interfaces remain open and are not claimed exhaustive or independent:
carrier/resource genesis and renewal, radius-one synthesis of the bounded
semantic rotations, translation-invariant occurrence, and lattice-wide
enforcement. They are not established substrate obstructions.
