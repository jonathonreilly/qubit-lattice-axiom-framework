# Physical L41 autonomous recurrence/resource tournament — Cycle 582

Date: 2026-07-22

Authority: none

Audit: unset

Authority remains none. Audit remains unset. This cycle changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, audit status,
or PR surface.

Runner:

`scripts/physical_l41_autonomous_recurrence_resource_tournament_cycle582_2026_07_22.py`

## Result up front

Cycle 582 takes the exact Cycle-580 18-M2 H/CNOT/CZ/SWAP instrument circuit
and removes host-side *layer selection* at finite supplied horizon. Route A
adds an in-state eleven-rail program coordinate and an in-state finite-resource
cursor. Repeating one homogeneous controlled update applies the eleven
Cycle-580 layers in order, advances to the next fresh 12-M2 packet, and leaves
earlier spent packets untouched. The host does not choose which layer runs;
it still repeats the same candidate update law.

The construction is exact at controller code-coordinate resolution for train
horizon `H=2` and held horizon `H=3`. The unary `H11` program and `H_H` cursor
are explicitly embedded into physical M2 one-excitation codes. What is not
constructed is a literal proper-cubic nearest-neighbor decomposition of every
phase-and-cursor-controlled gate, the controller/conveyor placement, or local
enforcement of the unary domains. The strongest honest result is therefore a
positive finite-horizon partial construction, not a completed autonomous
physical-volume recurrence.

Route B turns the supplied resource stock into a debit and history-owner
ledger. Each invocation consumes one fresh 12-M2 packet: six encoded-plus
reset M2, three zero pointer M2, and three zero dephasing-copy M2. The spent
packet retains the old input environment and both conditional output words.
Train `H=2` and held `H=3` pass with no refit; the first modulo-cursor overrun
reuses and changes spent slot zero. Finite stock is not renewable.

Route C tests three reversible reset attempts. The exact Cycle-580 inverse
restores the initial system and fresh carriers but erases the pointer,
dephasing, and old-input-environment output episode. Copying pointer/dephasing
words before the inverse preserves those archive bits but prevents exact reset
of the active 18 M2. Copying the old-input computational label before inverse
dephases a coherent input fixture. These are route-specific exact falsifiers;
they are not a universal archive-preserving-reset no-go.

Copied pointer is not a framework Record. Candidate traces are not derived Born
probabilities. Program phase is not time. Carrier count is not energy or
source. The finite invocation count is not duration, and the spent-packet
ledger is not entropy-renewal, temperature, work, stress, or gravity.

No shared obstruction or axiom pressure is claimed. Exact contract phrase:
no axiom pressure.

## Exact target and state spaces

Cycle 580 supplies one exact elementary isometry

```text
V_B : C^8 -> system(6 M2) tensor spent/pointer/dephase(12 M2)
```

with an eleven-layer nearest-neighbor circuit. Cycle 582 supplies `H` resource
packets and reuses the same six-M2 active system:

```text
quantum M2(H) = 6 + 12 H.
```

The controller code coordinates are

```text
phase p in {0,...,10},
resource cursor c in {0,...,H-1}.
```

They have explicit one-excitation embeddings

```text
H11 : C^11 -> (C^2)^tensor11,
H_H : C^H -> (C^2)^tensorH.
```

Thus the declared physical-M2 count at supplied horizon is

```text
6 + 12 H + 11 + H = 17 + 13 H,
```

or 43 M2 at train `H=2` and 56 M2 at held `H=3`. These counts include the
finite stock and controller rails; they do not imply a stationary reservoir.

The Cycle-580 runner, note, and parent receipt are exact-pinned. Its transcript
hash is checked transitively through that receipt, so Cycle 582 does not depend
on an untracked raw transcript.

## Route A — in-state program/cursor recurrence

Let `U_p,c` be Cycle-580 elementary layer `p+1`, with every resource qubit
remapped into packet `c`. Define one homogeneous code-coordinate update

```text
F_H |psi,p,c>
  = U_p,c |psi> tensor |p+1,c>                 for p < 10,
  = U_10,c |psi> tensor |0,c+1 mod H>          for p = 10.
```

Every `U_p,c` is unitary, and the phase/cursor transition is a permutation.
Therefore `F_H` is unitary on the declared quantum/controller code space. The
runner constructs its exact inverse by recovering the predecessor phase and
cursor and applying the corresponding layer adjoints in reverse order.

Starting from `|p=0,c=0>`, eleven repetitions of the same `F_H` reproduce one
Cycle-580 invocation and advance the cursor. Eleven more repetitions reproduce
the second invocation. The runner separately applies the direct Cycle-580
layers to the appropriate packet and compares at every invocation boundary.
At `H=1`, the sparse physical output is compared directly to the materialized
`2^18 x 8` Cycle-580 columns.

This removes host-side selection among the eleven layers. It does not remove
all external structure: invocation of the same framework update remains the
candidate recurrence law; initial phase, cursor, finite packets, and the
controlled-update table are supplied.

### Collision and archive control

Packet zero is used only during invocation zero; packet one is used only
during invocation one. Later gates act on the active system and the selected
fresh packet, so the reduced state of earlier archive packets is invariant.
The runner checks packet-zero reduced-density invariance through the second
invocation and checks that packet one remains exactly fresh before it is used.

Deleting one head advance or the first cursor advance changes the repeated
isometry. At the final legal boundary, all active-system and spent-environment
parity pairs return to their code sectors.

### Physical locality boundary

The base Cycle-580 gates remain nearest-neighbor and support at most two. A
phase-controlled system gate has the two base M2 plus a phase rail; a
resource-touching gate also needs a cursor rail, for bounded logical support
at most four. Cycle 582 does not give the missing literal two-M2
nearest-neighbor routing/decomposition of those controls, nor a spatial
program-token conveyor. It therefore does not promote the code-coordinate
controller to a completed physical-site compiler.

If a physical conveyor first places the selected packet at the active station,
the cursor control drops out of each layer gate and the maximum phase-controlled
support is three M2: one program bit plus the Cycle-580 gate's at-most-two M2.
A replicated local phase ring would then need an explicit synchronization and
genesis ledger; Cycle 582 does not derive that ledger.

The same limitation applies to local enforcement: `H11` and `H_H` exactly-one
membership is a supplied lawful-domain condition. Zero- or two-excitation
heads, out-of-range phase/cursor values, and dirty controller fixtures are
refused, but no penalty, repair, or noise threshold is derived.

Coherent perturbations of the opening H gate are tested at two amplitudes.
Their output residual grows with perturbation size. This is a sensitivity
control, not a fault-tolerance theorem.

## Route B — finite conveyor and resource debit

The held `H=3` resource ledger is

| completed invocations | fresh slots | spent archive slots | fresh M2 |
|---:|---:|---:|---:|
| 0 | 3 | 0 | 36 |
| 1 | 2 | 1 | 24 |
| 2 | 1 | 2 | 12 |
| 3 | 0 | 3 | 0 |

Each spent packet owns:

- six M2 holding the complete old active-system input;
- three pointer M2 holding the coherent conditional history word; and
- three dephasing-copy M2 holding the copied conditional word.

These outputs remain quantum/global history carriers. They are not framework
Records or actual selected histories.

An abstract 12-lane packet rotation can move the next packet to the active
station. At held `H=3`, a left rotation costs 24 adjacent two-M2 SWAPs in two
serial lane steps, with the twelve lanes parallel. Its inverse and a deleted
SWAP are checked as packet permutations. This is an exact debit/routing ledger,
but Cycle 582 does not place the complete conveyor and active station together
in one literal proper-cubic chart; that physical layout remains open.

After three legal invocations the modulo cursor returns to zero, but packet
zero is spent. Applying another cycle visibly changes the packet-zero archive.
That overrun is rejected by the finite-stock domain. It is not called renewal,
and no stationary fresh/spent balance is inferred.

At the active station, a phase bit plus each at-most-two-M2 Cycle-580 gate has
support at most three. The open problem is not support count but the literal
placement, synchronization, and genesis of the required local phase carriers.

## Route C — reversible uncompute/reset attempts

### C1: full inverse without archive

Applying every Cycle-580 gate adjoint in reverse order returns the exact
initial state. The active system recovers its arbitrary encoded input and the
twelve auxiliaries return to encoded-plus/zero. The same inverse removes the
pointer, dephasing, and spent old-input-environment outputs. Carrier reuse is
obtained only by erasing the episode.

### C2: pointer/dephasing copy, then inverse

Six blank archive M2 receive CNOT copies of the three pointer and three
dephasing bits. Their reduced archive state is invariant under the subsequent
inverse. Because which-history information remains outside the 18-M2 block,
the active block does not return to the pure initial state. The runner reports
the exact active-reset infidelity.

This copied conditional word is still not an actual branch or framework
Record; copying a label does not supply occurrence or permanent admission.

### C3: old-input label copy, then inverse

Three blank archive M2 receive the representative computational rails of the
six-M2 old-input environment. For basis inputs this is a reversible classical
copy operation. For the held coherent `(|000>+|111>)/sqrt(2)` fixture it leaves
which-input information outside the inverse block, and the restored active
system loses coherence. The runner reports its trace distance from the target
pure state.

Only these maps and fixtures are falsified. Teleport/swap archives, streaming
garbage rays, catalytic workspaces, and error-corrected constructions remain
concrete untested routes.

### Contract-scoped retained dimension

For the exact branch-conditioned reset contract, the old logical input ranges
over an eight-dimensional code and the supported pointer label has four
orthogonal values. The runner constructs all 32 old-input/label columns,
including the normalized active branch states, and obtains rank 32. The four
supported active branch states are themselves orthogonal; their geometry does
not reduce the rank, and the pointer sectors would make the labels orthogonal
even without that fact. Under the declared contract, any map that resets all
active carriers to one fixed blank while preserving the old-input and
four-valued label distinctions as simultaneously and independently readable
outputs therefore needs a retained archive of dimension at least 32, hence at
least five M2.

This is a dimension bound only for that explicit simultaneous-independent-
readability reset/compression contract. It is not a minimum physical content
theorem and does not apply to arbitrary archive/reset maps, all recurrence
mechanisms, streaming reservoirs, or contracts that do not preserve both
distinctions independently.

## Matter distinction and proper-cubic presentation

The reduced active output is input-independent because Cycle 41 resets it, so
the active system does not retain the original matter distinction. Global
unitarity keeps distinct inputs orthogonal, and the first spent environment
retains trace distance one between logical input zero and seven even after the
held horizon. This is global nonerasure, not active matter-compatible
dynamics.

The exact Cycle-580 18-site station retains all 24 proper-cubic frame tests and
all 576 ordered frame products for all eleven projector roles. Cycle 582
rotates the base coordinates and rechecks uniqueness. The phase/cursor and
conveyor have no completed literal cubic placement, so covariance is claimed
only for the inherited base station and scalar controller code factors, not a
full recurrent physical volume.

## Route dispositions

| route | disposition | exact residual |
|---|---|---|
| A: in-state program/cursor | strongest positive finite-horizon code-coordinate recurrence | controlled-gate NN decomposition, controller placement/enforcement, unbounded horizon open |
| B: finite conveyor/debit | exact held-H3 capacity, history-owner, inverse/deletion, and overrun controls | finite stock exhausted; literal conveyor geometry and stationary balance open |
| C: reversible uncompute/reset | three exact route-specific falsifiers | full inverse erases episode; tested copies prevent exact reset/coherence; alternatives untested |

No route-specific failure is constitutional evidence.

## Supplied / derived / open

### Supplied

1. the exact Cycle-580 circuit, Cycle-577 `V_B`, candidate instrument, and base
   proper-cubic chart;
2. train `H=2` and held `H=3` finite stocks of pure encoded-plus/zero packets;
3. initial unary phase/cursor codes, their exactly-one membership, modulo cursor
   convention, and the controlled layer table;
4. noiseless bounded controlled gates at code-coordinate level and the same
   update-invocation rule;
5. the conditional pointer interpretation and candidate trace functional.

### Derived

1. exact `H=1` equality to Cycle 580 and exact `H=2/H=3` repeated
   code-coordinate recurrence;
2. exact autonomous-step inverse, archive invariance, unused-fresh invariance,
   deletions, boundary code return, malformed-controller refusal, and coherent
   noise response;
3. an exact finite debit/history-owner ledger, held horizon, packet-permutation
   inverse/deletion, and first-overrun signature;
4. exact full-inverse output erasure and exact residuals for pointer/dephasing
   copy and old-input-copy uncompute attempts;
5. global matter-distinction retention in the first spent environment and
   inherited all24/all576 base-station covariance.

### Open

1. a literal proper-cubic nearest-neighbor decomposition and placement of the
   phase/cursor-controlled update and packet conveyor;
2. local unary/controller enforcement, repair, a noise threshold, arbitrary
   volume, and collision-safe unbounded recurrence;
3. stationary fresh/spent balance, carrier genesis and renewal, entropy sink,
   temperature, and reentry law;
4. archive-preserving exact quantum carrier reset beyond the tested copy
   schemes;
5. active matter-compatible evolution rather than only global input export;
6. an actual branch, occurrence, framework Record, realized history, Born or
   frequency calibration;
7. metric time, rate, lapse, energy, work, stress, source, backreaction,
   gravity, continuum, Lorentz, or CPT closure.

## TOE dependency ledger and evidence coordinates

| wall | Cycle-582 movement | residual |
|---|---|---|
| `C_ref` | one homogeneous in-state-controlled update replaces host layer choice at finite horizon | controller table, initial phase/cursor, finite packets and modulo convention supplied |
| `C_num` | exact H1/H2/H3 recurrence, archive, inverse, deletion, overrun, noise and uncompute residuals | sparse finite horizons; no arbitrary-volume/noise theorem |
| `C_wrap` | spent packet explicitly owns pointer/dephasing words and old input | no actual branch, framework Record, permanence, or realized history |
| `C_int` | original input distinction remains in the first spent environment across held H3 | active system reset loses it; full interacting-matter composition open |
| `C_local` | host layer selection removed at controller-code resolution; base all24 geometry retained | controlled-gate/conveyor NN layout, enforcement, collision-safe volume and unbounded recurrence open |
| `C_source` | finite fresh/spent M2 debit is exact | no renewal, entropy/temperature, energy/stress/source, backreaction, or gravity law |

Global evidence coordinates remain unchanged; this partial compiler does not
regrade lane closure:

| lane | repo-wide evidence | strict-M2 evidence | Cycle-582 delta |
|---|---:|---:|---|
| operational quantum / Records | `96/100 (4.80/5)` | `93/100 (4.65/5)` | finite repeated conditional compiler; actuality/Record unchanged |
| causal time | `79/100 (3.95/5)` | `76/100 (3.80/5)` | in-state program phase added; no physical time |
| inertia / matter | `94/100 (4.70/5)` | `97/100 (4.85/5)` | distinction retained globally in spent archive, not active matter dynamics |
| gravity / source | `82/100 (4.10/5)` | `77/100 (3.85/5)` | exact resource debit only; no source response |
| Born / probability | `84/100 (4.20/5)` | `73/100 (3.65/5)` | repeated candidate traces remain conditional diagnostics |

These are evidence-planning coordinates, not probabilities, audit grades, or
constitutional status.

## No-Go Discipline gate

The latest `origin/main` no-go-discipline skill and proof-search governance
were read completely. A broad recurrence, renewal, or archive-preserving-reset
negative does not pass.

### N1 — normalized families

| family | object / mechanism | terminal obligation | status |
|---|---|---|---|
| in-state phase plus cursor | unary controller, homogeneous controlled update, disjoint archives | literal local controlled-gate/conveyor compiler and enforcement | **ATTEMPTED** |
| finite conveyor/debit | supplied packets, permutation, archive ledger | stationary fresh/spent balance | **ATTEMPTED** |
| reversible uncompute/reset | inverse and two copy/archive schemes | faithful archive plus exact carrier return | **ATTEMPTED** |
| bi-infinite streaming QCA | reservoir/garbage rays and local scattering | stationary inflow and arbitrary-volume collision theorem | **UNTESTED / NOT COUNTED** |
| error-corrected catalytic workspace | encoded catalyst and syndrome export | exact catalyst return with faithful history owner | **UNTESTED / NOT COUNTED** |

Only three families qualify. N1 status: **FAIL**. No prior family is
misreported as ruled out.

### N2 — wall independence

Four residuals are audited without using them as a no-go theorem:

`W_L` literal controller/conveyor locality, `W_R` stationary fresh/spent
balance, `W_U` archive-preserving reset, and `W_E` enforcement/noise tolerance.

| pair | first closes second? | second closes first? | disposition |
|---|---|---|---|
| `W_L,W_R` | no—local scheduling can exhaust stock | no—balance supplies no program routing | retain both |
| `W_L,W_U` | no—local gates do not preserve archive under inverse | no—reset gives no layout | retain both |
| `W_L,W_E` | no—compiled control can be unprotected | no—repair gives no recurrence geometry | retain both |
| `W_R,W_U` | no—renewal may export rather than reset | no—one reset proves no stationary balance | retain both |
| `W_R,W_E` | no—flow may carry faults | no—repair generates no fresh inflow | retain both |
| `W_U,W_E` | no—reset may be noise-fragile | no—enforcement does not preserve quantum archives | retain both |

### N3–N8

- **N3:** the runner scans all refreshed hidden-premise phrases. Standardness
  appears only in non-load-bearing prior-art attribution.
- **N4:** Cycle 580's host-order residual matches the finite in-state controller
  claimed here; Cycle 483's finite-bath residual matches the finite debit; the
  Cycle-577 inverse boundary matches Route C. Cycle-580 base NN geometry is
  explicitly dropped as evidence for controller-layout closure.
- **N5:** every negative observation is limited to train/held horizons and the
  three named Route-C maps. No lattice-wide or universal reset claim ships.
- **N6:** program-token QCA, streaming reservoir/garbage rays, catalytic
  correction, and teleport/swap plus independent preparation remain explicit
  partial-closure paths.
- **N7:** the hostile steelman is a translation-invariant reversible QCA with
  a spatial program token, bi-infinite encoded-plus/zero inflow, outward spent
  carriers, and a faithful output algebra. Its terminal obligation is a local
  arbitrary-volume collision theorem and stationary balance. It is concrete
  and untested, so broad negatives are premature.
- **N8:** Cycle 574 and Cycle 577 gaps were later retired constructively;
  Cycle 483's discard was retired at finite export but not renewal; Cycle 580's
  host-order gap is only partially narrowed here. Constructive reopening is
  therefore mandatory.

Artifact status: **POSITIVE FINITE-HORIZON PARTIAL CONSTRUCTION WITH
ROUTE-SPECIFIC FALSIFIERS**.

Broad no-go: **FAIL / DO NOT SHIP**.

Minimum-content theorem: **FAIL / DO NOT SHIP**.

Shared-obstruction claim: **DO NOT SHIP**.

Axiom-pressure claim: **DO NOT SHIP**.

## Prior-art and novelty boundary

Feynman clocks, unary program registers, reversible circuit iteration, finite
reservoir/conveyor ledgers, Stinespring uncompute, coherent copying of
orthogonal labels, and garbage/history export are standard methods. No general
novelty or priority claim is made.

The repo-local result is the exact-pinned joining of the Cycle-580 L41 circuit
to a finite in-state controller, cursor, resource/archive ledger, held horizon,
and three explicit uncompute/reset probes while keeping physical locality,
renewal, matter, occurrence/Record, Born, time, and source boundaries explicit.

## Cold verification

Frozen command:

```bash
/usr/bin/time -l python3 -u scripts/physical_l41_autonomous_recurrence_resource_tournament_cycle582_2026_07_22.py
```

Frozen receipt:

- runner SHA-256:
  `47c5138720add60ed6fa8b6506dcb8a9cbee9af5a1ab3defbc7aea4c3cfa290a`;
- transcript SHA-256:
  `58045c2dd7af2671e522d7e471e7caa89d92dfec9dc72710072c3fa5b81ebf35`;
- `RESULT pass=7 fail=0`;
- Cycle-580 runner, note, and parent receipt match their exact pins; the
  receipt transitively validates Cycle 580's agent transcript and parent
  `10/10`, single-invocation closure, open recurrence obligation, authority
  `none`, and audit `unset`;
- Route A: H1 Cycle-580 residual `1.760210900903115e-18`, H2 direct residuals
  `[0,0]`, autonomous inverse maximum `6.280369834735101e-16`, final Gram
  residual `1.2560739669470201e-15`, slot-zero archive and unused-slot
  residuals at most `3.3306690738754696e-16`, both deletion residuals `4`,
  final code leakage `0`, all six malformed controller fixtures refused, and
  coherent-H noise residuals `0.0014142135476417034` and
  `0.014142120892344281` at perturbations `0.001` and `0.01`;
- Route B: held-H3 Gram residual `6.280369834735101e-16`, exact fresh-M2
  debit `36 -> 24 -> 12 -> 0`, slot-zero archive invariance
  `5.551115123125783e-17`, first overrun archive change
  `0.5077524002897471`, and exact abstract conveyor inverse/deletion controls;
  this is finite archive conservation and debit, not renewal or resource
  thermodynamics;
- Route C: full inverse residual `8.906865629316332e-16`, output-erasure trace
  distances `0.7499999999999991`, `0.7499999999999992`, and
  `0.9354143466934843`, pointer/dephasing-copy active reset fidelity
  `0.2499999999999996`, and old-input-copy coherent restoration trace distance
  `0.4999999999999999`; the rank-32 / at-least-five-M2 bound is conditional on
  the declared simultaneous-independent-readability contract and is not a
  general archive/reset minimum;
- global input-zero/input-seven overlap `0`, global trace distance `1`, active
  trace distance `0`, and first spent-environment trace distance
  `0.9999999999999998`; inherited base-layout all24 collision failures `0`,
  while a literal controller/conveyor cubic layout remains unconstructed;
- N1 has only three qualifying attempts against five required, so N1 is
  `FAIL`; broad no-go, minimum-content, shared-obstruction, and axiom-pressure
  claims are all `DO_NOT_SHIP`;
- external elapsed `2.67 s`, maximum resident set size `291,192,832` bytes,
  peak memory footprint `278,610,544` bytes;
- internal scientific-section elapsed `2.546142000006512 s`, reported RSS
  `291,192,832` bytes;
- authority `none`; audit `unset`.

The run is below 360 seconds and 3 GiB. The transcript is frozen evidence;
this receipt-only note edit does not alter the runner or transcript.

Parent verification independently reran the frozen runner after checking all
three artifact hashes and the contract-scoped wording of the rank bound.  The
parent run again returned `pass=7 fail=0` in `3.40 s`, with maximum resident
set size `282,902,528` bytes, peak memory footprint `277,873,264` bytes, and
zero swaps.  Its transcript SHA-256 is
`517498b146faf091b53941068e8cd36c6e895d1d8b9b27168fa432830d04048b`.
