# Three-register companion input circuit and fixed physical schedule — Cycle 789

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded constructive theorem plus a route-specific semantic correction

Claim type: bounded_theorem

Runners:

- [`frontier_cycle789_two_bank_input_collision_discriminator_2026_07_30.py`](../scripts/frontier_cycle789_two_bank_input_collision_discriminator_2026_07_30.py)
- [`frontier_cycle789_three_register_even_car_channel_2026_07_30.py`](../scripts/frontier_cycle789_three_register_even_car_channel_2026_07_30.py)
- [`frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py`](../scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Circuit ordinals, colour blocks, and stage labels below are supplied circuit
structure. They are not physical time, duration, cadence, rate, or energy.

## Direct scientific dependencies

- the landed [Cycle-720 recurrent companion code, local Choi pump, and
  recurrent physical update](./RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md); and
- the landed [companion-bank Bell-character dilation and epoch-liveness
  census](./COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md).

## Result

The predecessor's two-register joint epoch does not inject an independent live
input. Stage A writes all nine registers in the interval it later labels the
live bank: six are the Choi input half and three receive the encoded-bank
supply. An exact dense character discriminator consequently finds an
input-independent output, with maximum pairwise residual
`7.850462293418876e-17` across four independent inputs and identity-channel
residual `0.7071067811865476`. This corrects only the predecessor's joint-epoch
input interpretation. Its standalone Bell-character algebra is not retracted.

Adding a distinct companion-encoded live register `L` repairs the channel.
With `O,I` the prepared Choi pair and `R` a diagnostic reference, the circuit
Bell-couples `I,L`, applies the private corrections only on `O`, and reproduces
the signed `O,R` even-CAR character algebra exactly. The tested character
ranks are 11, 100, 152, and 389. The dense one-mode repair
has identity residual `7.771561172376096e-16`. The full stabilizer/tableau
runner passes on `1x1x1`, `2x2x2`, `3x2x2`, and held `5x3x2`; deleting one
private dual and replacing `I,L` by the old self-comparison are both detected.

The repaired circuit also has a literal fixed physical schedule. A conservative
explicit palette assigns, per coarse cell:

- 9 M2 for each of `O`, `I`, and `L`;
- 3 distinct coframe M2; and
- 17 retained pump-syndrome plus 17 retained Bell-syndrome M2.

The resulting census is 64 M2 per cell. This is an exhibited construction, not
a minimum. On `1x1x1`, `2x2x2`, `3x2x2`, `5x3x2`, and held `6x5x4`, every
controlled-Pauli is compiled as a nearest-neighbour returned
SWAP/controlled-Pauli/SWAP word. All labels return, all semantic targets are
reconstructed, and all same-block collisions vanish under the fixed
mod-3-cell by 17-family schedule. The longest word uses 1,981 microsteps, below
the fixed padded bound 4,096. The external `I,L` Bell routes cross neither a
live palette nor a Cycle-720 `G` site. The landed recurrent word touches only
`O`; it is disjoint from the coframe and every non-`O` palette after the
returned-route barrier.

Coordinate, palette, nearest-neighbour, and colour-block covariance passes for
all 24 proper-cubic frames, eight translation origins, and all 576 ordered
frame products. Actual frame/origin numerical mod-3 re-sorts yield 1, 45, 84,
144, and 192 distinct row orders on the held ladder and reconstruct every
overlapping two-hot correction target with zero failures. The one-cell and
2-cube frame/origin orders need no phase repair. Larger held boxes expose
nonzero anticommuting inversions; the explicitly routed local inversion-CZ
cocycle repairs every tested target with zero failures.

Hostile ordering is an active control, not an alternative law. On the exact
one-cell 49-wire, 150-gate Clifford dilation, reversal changes 64 of 98 signed
generator images, including 11 of 18 output-`O` images. After initialization
and reduction of the 22 syndrome ancillas, however, all `4^9 = 262,144`
output Pauli observables agree. Thirty local inversion-CZ gates restore the
complete retained tableau exactly. Eleven additional permutations use 122 CZ
gates in total and leave zero repaired-tableau failures. The identity used is
the exact controlled-Pauli cocycle: reversing controlled Paulis `P_i,P_j`
adds a syndrome-control CZ precisely when `P_i P_j = -P_j P_i`.

## Exact boundary

This package closes the literal physical-M2 Bell/correction leg and a
collision-free fixed schedule **conditional on an already companion-encoded
live bank**. It does not prepare that live bank from arbitrary bare physical
M2 input. It also does not execute the full pump, literal prefix, and
non-Clifford recurrent `G` as one held-box signed channel in this package.

The 24/576 schedule result actively reconstructs coordinates, palettes,
colours, and tested correction phases. It still assumes the coframe-transported
generator/slot chart. A full held-box signed-channel comparison under actual
frame-induced generator-basis shears remains open and is not inferred from the
geometric census.

The clean parity/center sector, mixed gauge reference, coframe-origin sector,
clean retained syndrome inputs, finite boundary, cell chart, stage order, and
permission to trace typed semantic environments remain supplied. There is no
autonomous occurrence, admission, renewal, physical clock, source/gravity law,
permanent Record, Born weighting, or realized-history selection here.

## Supplied / derived / open

### Supplied

- the landed Cycle-720 `O,I` Choi pump and recurrent `G`;
- one independent companion-encoded live bank `L`;
- fixed parity and local-center sectors, mixed gauge, and three coframe M2 per
  cell;
- clean pump/Bell syndrome registers and their retained-environment typing;
- the private correction atlas, finite cell chart, mod-3 origin, fixed stage
  order, and boundary.

### Derived

- the exact semantic diagnosis of the two-bank joint epoch;
- the exact three-register signed even-CAR channel on four held fixtures;
- private corrections confined to `O` and active deletion/self-comparison
  controls;
- an explicit constant-density 64-M2/cell palette;
- literal nearest-neighbour returned routes with zero held-size schedule
  collisions and a fixed 4,096-microstep word bound;
- the `G` site/palette firewall;
- 24-frame, eight-origin, and 576-product schedule geometry; and
- an exact bounded inversion-CZ phase firewall for the tested hostile orders.

### Open

- autonomous raw-M2 to companion-encoded `L` preparation and local enforcement;
- one executed held-box pump/Bell/correction/`G` signed channel including seam
  and contact terms;
- full frame-induced generator-basis-shear covariance of that channel;
- clean-resource genesis, epoch occurrence, admission, renewal, and fault
  repair; and
- unchanged bridges into causal intervals, source/gravity, Record/Born, and
  prediction surfaces.

## No-go discipline

The negative statement is only that the submitted two-bank joint epoch has no
independent input register. It is not a substrate obstruction.

### N1 — alternatives

The gate for any broader compiler no-go **fails**, which is why no such claim
ships:

| route family | marker | result |
|---|---|---|
| submitted two-bank joint epoch | ATTEMPTED | all nine purported input registers are written by Stage A, and the dense output is input-independent |
| distinct third companion bank | ATTEMPTED | succeeds exactly and defeats a broad input-channel no-go |
| predecessor raw-mode Bell correction | RULED OUT BY PRIOR at its submitted representative only | Cycle 720 finds growing Jordan–Wigner correction support; it does not rule out other representatives |
| direct raw-input Clifford/gauging map | UNTESTED/OPEN | it could avoid teleportation entirely |
| staggered parity-rail or dissipative local preparation | UNTESTED/OPEN | it could carry or pump the missing encoding locally |

Because fewer than five route families are closed, the only admissible negative
is the literal register census of the submitted program.

### N2–N6 — walls, imports, residuals, rhetoric, and partial closure

- N2: the observed wall is exactly the register collision between Stage A and
  the purported input; it is not shared by the repaired route.
- N3: parity, center, gauge, coframe, clean ancillas, boundary, chart, schedule,
  and encoded-`L` genesis are explicit imports.
- N4: the dense two-bank output is a replacer-like channel, while the
  three-bank channel has identity residual below `8e-16`; the residuals do not
  match a shared obstruction.
- N5: the negative is tested at the individual-register and complete one-cell
  bank resolutions only. It is not extended to arbitrary layouts, other
  schedules, other encodings, or a lattice-wide compiler statement.
- N6: the exact standalone Bell algebra and the complete three-register repair
  are retained as partial and constructive closures.

### N7 — steelman

A hostile reviewer should reject any broad obstruction immediately: the
problem is not fermionic algebra but aliasing two semantic roles onto the same
physical bank. Allocate a distinct `L` bank, or rewrite Stage A so that one
bank remains untouched, and the input can remain independent. The explicit
third-bank construction realizes exactly that counterargument and recovers the
full signed character channel. Direct raw gauging and staggered parity-rail
routes remain untested and could reduce the retained resources further.

### N8 — cross-cycle echo

- N8: earlier raw-Jordan-Wigner and overlap failures are route-specific and do
  not strengthen this collision into a no-go. Cycle 720 itself escaped a raw
  correction wall by changing to even-CAR characters; the same
  change-the-representation lesson applies here.

N1 therefore blocks any no-go and forces the present route-specific demotion.
This package creates no axiom pressure.

## Verdict

The physical input-side mystery is materially narrower. The old joint epoch
did not contain an independent input, but one additional local companion bank
repairs the channel and admits an explicit collision-free nearest-neighbour
schedule at constant density. The remaining compiler wall is autonomous
preparation/enforcement of that bank and one full seam/contact signed-channel
composition with recurrent `G`.
