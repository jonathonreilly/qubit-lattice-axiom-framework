# Physical L41 elementary gate/layout compiler — Cycle 580

Date: 2026-07-22

Authority: none

Audit: unset

Authority remains none. Audit remains unset. This cycle changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, audit status,
or PR surface.

Runner:

`scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py`

## Result up front

Cycle 580 retires the exact elementary-gate/layout implementation residual
left open by Cycle 577 Route B. It gives a full-space unitary sequence on all
18 physical M2 whose gates have support at most two, places every two-M2 gate
on a literal proper-cubic nearest-neighbor edge, and reproduces all eight
lawful input columns of the Cycle-577 `V_B` retained-environment isometry.
It closes the bounded gate/layout and full-unitary-extension obligations. The
seven- or eleven-layer gate order remains supplied compile-time schedule data:
no in-state phase/program carrier or autonomous no-host-control recurrence is
constructed.

The compiler uses the actual Cycle-577 code

```text
W|0> = |00>,   W|1> = |11>
```

and performs, without an omitted host-side transformation:

1. six pairwise physical SWAPs from the encoded system into three fresh
   encoded-plus reset blocks;
2. encoded `CZ` on one representative rail of the left-middle and
   middle-right code blocks;
3. coherent logical-X extraction from the middle block and logical-Z
   extraction from the left and right blocks into three pointer M2; and
4. three pointer-to-dephasing-carrier CNOTs.

Two gate realizations are exact. A native two-M2 logical-H block preserves the
even-parity code at every step. The elementary standard-gate realization uses
`CNOT-H-CNOT`; it leaves the code sector temporarily after each decoding CNOT
and returns exactly after the closing CNOT. The temporary code-sector departure
is measured and reported rather than hidden.

The resulting finite circuit neither selects one pointer sector nor creates a
framework occurrence or Record. The four supported `1/4` candidate weights
remain pinned Cycle-41 diagnostics, not derived Born probabilities. A copied
pointer is not a framework Record. Gate layers are not physical time, and M2
or carrier counts are not energy, rate, stress, source, or gravity.

This is a positive construction. There is no negative claim, minimum-content
claim, shared-obstruction claim, or axiom-pressure claim. There is no axiom
pressure from this result. Exact contract phrase: no axiom pressure.

## Exact target contract

The target is the single Cycle-577 Route-B isometry

```text
V_B : C^8 -> (C^2)^tensor18,
axes = encoded system(64) x encoded spent environment(64)
       x pointer(8) x dephasing copy(8).
```

For logical input basis column `|i>`, Cycle 577 defines

```text
V_B |i>
 = sum_h [W P_h CZ |+++>] system
         tensor [W |i>] spent-environment
         tensor |h> pointer tensor |h> dephasing.
```

The Cycle-577 runner, note, and committed parent receipt are exact-pinned.
Cycle 580 validates the agent cold-transcript hash transitively from that
receipt, without requiring the untracked raw transcript in a clean checkout.
It reconstructs the target columns independently from the pinned
projector/instrument objects and compares both compiled variants to the same
`2^18 x 8` target.

“Full-space unitary sequence” means every listed gate is a unitary lift on the
entire `2^18` space, so their finite product is a unitary on all 18 M2. The
dense `2^18 x 2^18` square is not materialized. The runner checks each local
unitarity identity, applies the forward and inverse products to lawful and
off-code fixtures, and proves the native and decomposed products agree because
their only substitution obeys an exact four-dimensional matrix identity.

## Exact parity-preserving logical H

On one two-M2 code block define

```text
U_H = CNOT_(0->1) (H_0 tensor I_1) CNOT_(0->1).
```

Then

```text
W^dagger U_H W = H,
[U_H, W W^dagger] = 0,
[U_H, Z tensor Z] = 0,
U_H^dagger U_H = I_4.
```

Thus an exact parity-preserving logical H is a legitimate two-M2 block gate.
It is not merely specified on the code columns; the displayed product fixes a
unitary extension on the complete four-dimensional block.

The same equation gives the elementary decomposition. Its intermediate
states are different:

```text
alpha|00> + beta|11>
  --CNOT--> alpha|00> + beta|10>
  --H_0-->  generally mixed even/odd parity support
  --CNOT--> W H(alpha|0> + beta|1>).
```

The first and second intermediate states need not satisfy `ZZ=+1`. Cycle 580
records the maximum column leakage after every elementary layer. The native
block-gate schedule has zero leakage at every declared layer boundary; the
standard decomposition has explicit nonzero leakage at layers 4, 5, 8, and 9
and exact return at layers 6, 10, and the final boundary. Within the parallel
six-SWAP reset layer, serializing one rail before its partner can also leave a
code block temporarily; no stronger sub-gate enforcement claim is made. This
distinction matters if a future law demands code membership after every
elementary substep rather than at schedule-layer boundaries.
For the two logical code-basis inputs, the decoding CNOT has worst-case
code-sector leakage norm `1`; on the actual post-reset cluster columns the
reported layer leakage is `1/sqrt(2)`.

## Full elementary sequence

Physical axis order is

```text
0..5   S_L0,S_L1,S_M0,S_M1,S_R0,S_R1
6..11  E_L0,E_L1,E_M0,E_M1,E_R0,E_R1
12..14 P_M,P_L,P_R
15..17 D_M,D_L,D_R.
```

The elementary sequence is:

| layer | mutually disjoint operations | role |
|---:|---|---|
| 1 | six `SWAP(S_cell, E_cell)` gates | reset old-input export |
| 2 | `CZ(S_L0,S_M0)` | encoded left-middle contact |
| 3 | `CZ(S_M0,S_R0)` | encoded middle-right contact |
| 4 | `CNOT(S_M0,S_M1)` | logical-H opening decode |
| 5 | `H(S_M0)` | logical-H opening rotation |
| 6 | `CNOT(S_M0,S_M1)` | logical-H opening re-encode |
| 7 | `CNOT(S_M0,P_M)`, `CNOT(S_L0,P_L)`, `CNOT(S_R0,P_R)` | coherent X/Z/Z pointer extraction |
| 8 | `CNOT(S_M0,S_M1)` | logical-H closing decode |
| 9 | `H(S_M0)` | logical-H closing rotation |
| 10 | `CNOT(S_M0,S_M1)` | logical-H closing re-encode |
| 11 | `CNOT(P_M,D_M)`, `CNOT(P_L,D_L)`, `CNOT(P_R,D_R)` | dephasing copy |

This has 20 gates: two one-M2 H gates and eighteen two-M2 gates. The native
parity-block version has sixteen two-M2 gates in seven layers. Both have
maximum support two.

The order of these layers is part of the supplied compiler description. No
physical carrier inside the 18 M2 advances the layer, arbitrates collisions,
or initiates another invocation. Consequently the finite circuit does not
close the original host-side-control/autonomous-recurrence requirement.
Schedule index and circuit depth are not physical time.

The six layer-1 SWAPs are the physical reset operation: they move the complete
old encoded input into the spent environment while placing encoded `|+++>` on
the active system. They are not anonymous routing swaps. No additional routing
SWAP is needed.

## Literal nearest-neighbor layout

All sites lie in a constant `3 x 4 x 2` proper-cubic bounding box:

| carrier | coordinate | carrier | coordinate |
|---|---|---|---|
| `S_L0` | `(-1,0,0)` | `S_L1` | `(-1,0,1)` |
| `S_M0` | `(0,0,0)` | `S_M1` | `(0,0,1)` |
| `S_R0` | `(1,0,0)` | `S_R1` | `(1,0,1)` |
| `E_L0` | `(-1,1,0)` | `E_L1` | `(-1,1,1)` |
| `E_M0` | `(0,1,0)` | `E_M1` | `(0,1,1)` |
| `E_R0` | `(1,1,0)` | `E_R1` | `(1,1,1)` |
| `P_M` | `(0,-1,0)` | `D_M` | `(0,-2,0)` |
| `P_L` | `(-1,-1,0)` | `D_L` | `(-1,-2,0)` |
| `P_R` | `(1,-1,0)` | `D_R` | `(1,-2,0)` |

Each code pair, each pairwise reset edge, both encoded-CZ edges, all three
pointer-extraction edges, and all three pointer-copy edges have Manhattan
length one. Gates within a listed layer have disjoint supports. This is a
literal bounded nearest-neighbor schedule, not an all-to-all circuit followed
by an uncompiled routing assertion.

The runner rotates all 18 coordinates through all 24 proper-cubic frames and
rechecks every native and elementary two-M2 gate occurrence. Site uniqueness
and unit-edge adjacency survive in every frame.

## Exact channel and inverse controls

The output is reshaped only after compilation as

```text
system(64) x spent environment(64) x pointer(8)
  x dephasing(8) x logical input(8).
```

For every one of the 64 logical input matrix units and every one of the eight
histories, the runner extracts the 64 spent-environment Kraus slices and tests

```text
Phi_h^physical(W rho W^dagger)
  = W Phi_h(rho) W^dagger.
```

It separately sums histories and tests the nonselective channel. Off-diagonal
pointer/dephasing sectors are zero. This exact compilation does not turn the
pointer copy into an actual branch.

Reversing the gate list and taking each local adjoint recovers the complete
initial state. The inverse is also tested on off-code full-space fixtures. As
expected for a reversible measurement dilation, running that inverse erases
the output episode while restoring the fresh carriers; it is not a reusable
reset-entropy theorem.

Every elementary gate is deletion-tested at the state immediately after its
application. Unitary suffix invariance makes that local deletion norm equal to
the final output difference for the corresponding omitted gate. An encoded-CZ
deletion also changes at least one branch channel.

## Lawful-domain and covariance controls

The declared initial domain contains:

- an arbitrary normalized three-logical-M2 state in the six-M2 `ZZ=+1` code;
- three encoded-plus reset blocks;
- three zero pointer M2; and
- three zero dephasing-copy M2.

The runner refuses an odd-parity system state, a reset block other than the
encoded-plus resource, dirty pointer or dephasing words, wrong shape, and
wrong normalization. These are supplied, locally checkable domain conditions;
no parity-enforcement or repair dynamics is constructed.

The final active system and spent environment return to their exact parity
codes. Train L3 and held L6 spectator controls are exact. The site-only frame
presentation is checked on all 24 proper-cubic frames and all 576 ordered
frame products for all eleven Cycle-41 projector roles. The cubic coordinate
chart rotates with a proper-cubic frame; the internal M2 matrices remain local
scalar carrier data under this declared presentation.

## Supplied / derived / open

### Supplied

1. Cycle 577's exact code, projector dictionary, candidate instrument,
   candidate trace targets, and `V_B` target columns;
2. a finite L3 block and held L6 spectator boundary;
3. three encoded-plus reset blocks, three zero pointer M2, and three zero
   dephasing-copy M2 per invocation;
4. lawful code membership, six locally checkable parity constraints, noiseless
   H/CNOT/CZ/SWAP gates, and the explicit 18-site cubic placement;
5. the Cycle-41 site-only proper-cubic frame chart and candidate law order.

### Derived

1. an exact parity-preserving two-M2 logical H and its exact CNOT-H-CNOT
   elementary decomposition;
2. a full-space 18-M2 unitary sequence with maximum gate support two;
3. a conflict-free 11-layer elementary nearest-neighbor schedule with zero
   routing SWAPs beyond the six physical reset SWAPs;
4. exact equality of native and elementary outputs with all eight Cycle-577
   target columns;
5. exact branch and nonselective channels on the complete logical operator
   basis, exact inverse, visible deletions, boundary code return, held
   spectators, and all24/all576 covariance.

### Open

1. genesis, renewal, entropy export, temperature, and reentry law for the
   fresh encoded-plus and zero carriers;
2. local enforcement or repair of parity constraints and robustness under
   noise;
3. autonomous collision-safe recurrence, arbitrary volume/horizon, and a
   physical scheduling law, including an in-state phase/program carrier that
   replaces the supplied compile-time gate order and removes host control;
4. selection of Cycle 41 as nature's law and one actual branch, occurrence,
   framework Record, permanence, or realized history;
5. derivation or empirical calibration of the candidate weights as Born
   probabilities or frequencies;
6. composition with the full interacting matter update without reduced reset
   erasing matter distinction;
7. metric time, rate, lapse, energy, stress, source, backreaction, gravity,
   continuum, Lorentz, or CPT closure.

## Constructive variant dispositions

| variant | disposition | exact residual left |
|---|---|---|
| A: native parity-preserving block gates | exact seven-layer nearest-neighbor compiler | treats the complete two-M2 `U_H` as one allowed gate |
| B: decomposed H/CNOT/CZ/SWAP gates | strongest elementary result; exact eleven-layer compiler | temporary middle-block code departure at four named layers |
| C: routed proper-cubic schedule | exact spatial realization of B with no routing SWAP overhead | compile-time order, fresh-resource genesis, enforcement, and recurrence remain supplied/open |

The variants are constructive refinements, not three normalized no-go route
families. No route-specific implementation condition is constitutional
evidence.

## TOE dependency ledger and evidence coordinates

| wall | Cycle-580 movement | residual |
|---|---|---|
| `C_ref` | exact Cycle-577 code and V_B target now have an elementary full-space gate realization | candidate law, boundary, code membership, carriers, and cubic chart supplied |
| `C_num` | exact columns, complete operator-basis channels, inverse, deletions, held and covariance tests | finite noiseless block only; no noisy-volume or continuum theorem |
| `C_wrap` | pointer and dephasing carriers are produced by explicit CNOTs | no actual branch, Record admission, permanence, or realized history |
| `C_int` | reset old input is exported by six literal SWAPs | reduced active system still resets; full interacting-matter composition open |
| `C_local` | Route-B gate/layout and full-unitary-extension residuals retired with support-two NN gates and constant depth/volume | compile-time order remains supplied; in-state control, enforcement, fresh-resource renewal, noise, recurrence, and arbitrary volume open |
| `C_source` | every carrier and gate is counted | no entropy-renewal, energy/stress/source, temperature, backreaction, or gravity law |

The global evidence coordinates carried through Cycle 576 remain unchanged;
Cycle 580 adds a local compiler but does not regrade global lane closure:

| lane | repo-wide evidence | strict-M2 evidence | Cycle-580 delta |
|---|---:|---:|---|
| operational quantum / Records | `96/100 (4.80/5)` | `93/100 (4.65/5)` | exact elementary finite instrument compiler; actuality/Record unchanged |
| causal time | `79/100 (3.95/5)` | `76/100 (3.80/5)` | circuit layers explicit but not physical time |
| inertia / matter | `94/100 (4.70/5)` | `97/100 (4.85/5)` | global old-input retention explicit; matter-compatible composition open |
| gravity / source | `82/100 (4.10/5)` | `77/100 (3.85/5)` | carrier accounting only; no source response |
| Born / probability | `84/100 (4.20/5)` | `73/100 (3.65/5)` | conditional trace diagnostics unchanged |

These are evidence-planning coordinates, not probabilities, audit grades, or
constitutional status.

## No-Go Discipline applicability audit

The latest `origin/main` no-go-discipline skill and proof-search governance
were read before packaging. Because Cycle 580 ships a positive exact compiler,
the negative-claim gate is not triggered. N1-N8 are nevertheless recorded to
prevent residual language from turning into an implicit no-go.

- **N1:** there is no negative target. Native parity-block gates, elementary
  decomposition, and cubic scheduling are constructive variants, not inflated
  negative route families.
- **N2:** supplied/open obligations are an import ledger. They are not asserted
  to be a pairwise-independent route-independent obstruction set.
- **N3:** the runner scans the refreshed hidden-premise phrase list. Any
  standardness wording is confined to non-load-bearing prior-art attribution.
- **N4:** the witness residual matches exactly: Cycle 577 left an exact
  elementary gate/layout decomposition open, and Cycle 580 supplies that
  decomposition. It does not claim to close carrier genesis, enforcement,
  recurrence, occurrence, Record, or Born residuals.
- **N5:** all negative wording is block-scoped. A finite copied pointer is not
  promoted to a framework Record; a layer number is not assigned time; a
  carrier count is not assigned energy or source.
- **N6:** the gate/layout import is retired by a constructive bounded theorem,
  not by a new axiom or definition change. The other imports remain explicit.
- **N7:** the strongest counterroute to any gate-synthesis obstruction is the
  exact `CNOT-H-CNOT` compiler given here. Therefore no negative gate claim is
  available.
- **N8:** Cycle 574's representation gap and Cycle 577's isometry-only gap were
  retired by explicit encodings and circuits. The same history counsels
  continued constructive attacks on enforcement and recurrence.

Gate status: **NOT TRIGGERED — POSITIVE CONSTRUCTION**.

Negative or minimum claim shipped: **false**.

Shared-obstruction claim shipped: **false**.

Axiom-pressure claim shipped: **false**.

## Prior-art and novelty boundary

Stinespring/Naimark dilation, repetition codes, coherent projective
measurement circuits, CNOT-H-CNOT encode/decode, SWAP reset, and cubic
nearest-neighbor scheduling are standard circuit methods. No general novelty
or priority claim is made.

The repo-local result is the exact-pinned compilation of Cycle 577's specific
eleven-projector `P/E/X/Z` Route-B isometry into a complete 18-M2 elementary
gate list and literal cubic layout, with temporary code departure, reset
export, pointer/dephasing carriers, semantic firewalls, and every residual
named.

## Cold verification

Frozen command:

```bash
/usr/bin/time -l python3 -u scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py
```

Frozen receipt:

- runner SHA-256:
  `c46917d4a932cd3ad9a78e0547625055f5adf9d5cf7393700d7e6715dd515cd3`;
- transcript SHA-256:
  `186fa69e34c55655194d79329fc2fbf1c5521006f4ffc295c5a49c70747e6763`;
- `RESULT pass=10 fail=0`;
- Cycle-577 runner, note, and committed-receipt hashes match their exact pins;
  the receipt transitively validates the agent transcript hash
  `0ba0c1b5d6223df39faa5f3a30275f858201bd0d354de9b0b8b1dd6021ecd21a`,
  parent verification `11/11`, Route-B target shape `(262144,8)`, and the
  previously open gate/layout and full-unitary obligations; the raw transcript
  is not a clean-checkout dependency;
- logical-H code intertwiner, parity-projector commutator, `ZZ` commutator,
  and `CNOT-H-CNOT` decomposition residuals all `0`; local-gate unitarity
  maximum `4.463374267214424e-16`; encoded left-middle/right `CZ`
  intertwiner and code-commutator residuals `0`;
- native and elementary output shapes `(262144,8)`, with 64 nonzero
  amplitudes; each differs from Cycle-577 `V_B` by
  `4.440926982597988e-16`, differs from the other by `0`, and has canonical
  14-digit SHA-256
  `fa431ff11ac8093864200f65acedb9c054e32a34a3dab5a57f6caa966b9bb50f`;
  compiled isometry residual `2.198129442157285e-15`;
- native schedule: sixteen two-M2 gates in seven layers; elementary schedule:
  two one-M2 plus eighteen two-M2 gates in eleven layers; maximum gate support
  two;
- 18 occupied sites in a `3 x 4 x 2` bounding box, zero adjacency or layer
  conflicts, zero routing SWAPs beyond the six physical reset SWAPs, and 816
  all24 rotated-layout edge tests with zero edge or collision failures;
- 512 exhaustive branch operator tests with zero failures and maximum residual
  `8.326672684688674e-17`; 64 nonselective tests with zero failures and maximum
  residual `1.6653345369377348e-16`; mismatched pointer/dephasing sector norm
  `0`;
- lawful inverse residual `8.906865629316332e-16`, off-code full-sequence
  inverse residual `5.25970249964293e-16`, and native/elementary off-code
  fixture residual `0`; all twenty elementary deletion residuals lie between
  `2.828427124746189` and `3.9999999999999987`; deleted encoded-CZ branch shift
  `0.2499999999999998`;
- initial/final system and environment code leakage `0`; native layer-boundary
  leakage `0`; elementary system leakage `0.7071067811865474` at layer 4 and
  `0.7071067811865472` at layers 5, 8, and 9, with exact return after layers 6
  and 10; decoding-CNOT worst logical-basis leakage `1`; six of six malformed
  domains refused;
- held-L6 isometry residual `6.217248937900877e-15`, eight held branch failures
  `0`, 24 proper-frame failures `0`, and 6,336 all576 projector-role failures
  `0`;
- compile-time gate order supplied `true`; in-state phase/program carrier and
  autonomous no-host-control recurrence constructed `false`; actuality,
  framework Record, derived Born probability, time, energy, and source remain
  unclaimed;
- external elapsed `3.10 s`, maximum resident set size `456,212,480` bytes,
  peak memory footprint `445,858,560` bytes;
- internal scientific-section elapsed `3.00450100004673 s`, reported RSS
  `448,741,376` bytes;
- authority `none`; audit `unset`.

The run is below 360 seconds and 3 GiB. The transcript is frozen evidence;
this receipt-only note edit does not alter the runner or transcript.
