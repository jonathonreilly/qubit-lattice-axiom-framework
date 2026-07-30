# Cycle 820: full128 two-cell parity-superselected even-CAR covariance

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded constructive theorem

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle820_full128_two_cell_parity_superselected_even_car_covariance_2026_07_30.py`](../scripts/frontier_cycle820_full128_two_cell_parity_superselected_even_car_covariance_2026_07_30.py)

Independent checker:

- [`frontier_cycle820_full128_two_cell_parity_superselected_even_car_independent_2026_07_30.py`](../scripts/frontier_cycle820_full128_two_cell_parity_superselected_even_car_independent_2026_07_30.py)

Shared algebra core:

- [`frontier_full128_two_cell_even_car_frame_core_2026_07_30.py`](../scripts/frontier_full128_two_cell_even_car_frame_core_2026_07_30.py)

Receipt and runner caches:

- [`full128_two_cell_parity_superselected_even_car_covariance_cycle820_receipt_2026_07_30.json`](../outputs/full128_two_cell_parity_superselected_even_car_covariance_cycle820_receipt_2026_07_30.json)
- [`frontier_cycle820_full128_two_cell_parity_superselected_even_car_covariance_2026_07_30.txt`](../logs/runner-cache/frontier_cycle820_full128_two_cell_parity_superselected_even_car_covariance_2026_07_30.txt)
- [`frontier_cycle820_full128_two_cell_parity_superselected_even_car_independent_2026_07_30.txt`](../logs/runner-cache/frontier_cycle820_full128_two_cell_parity_superselected_even_car_independent_2026_07_30.txt)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Circuit row numbers, frame loops, and correction order below are supplied
verification and circuit structure. They are not physical time, duration,
cadence, rate, or energy.

## Direct scientific dependencies

- the landed [full128 local M64 seam/contact bare-frame
  intertwiner](./FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md);
- the landed [Cycle-720 recurrent companion physical-M2 update and local
  Choi preparation](./RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md);
- the landed [companion-bank Bell-character dilation and epoch-liveness
  census](./COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md); and
- the landed [Cycle-789 three-register companion input
  circuit](./THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md).

## Result up front

On the supplied two-cell shape `(2,1,1)`, the seven-mode/full128 input
representation embeds as a rank-13 parity-even source subalgebra into the
landed three-register companion construction. The companion fixture has 12
matter modes, whose parity-even observable algebra carries an exact rank-23
signed stabilizer channel. The 23 Bell generators commute with total matter
parity. Their signed actions agree for every one of the 24 proper-cubic frames, all eight supplied
coframe-origin sectors, and all 576 ordered frame products.

The primary comparison evaluates all

```text
23 x 576 = 13,248
```

signed Bell-product rows directly; it does not infer this count from an
aggregate digest. Binary and signed residual counts are both zero. The runner
also reconstructs the Cycle-789 channel on `(2,1,1)`, checks the source-role
embedding, evaluates 4,416 frame/origin and 105,984 product/origin signed graph
rows, and actively deletes each of the 23 correction rows or flips each of the
23 Bell-measurement signs. The independent checker does not import the primary
or its new core. It reconstructs the rank, parity restriction, signed product
law, and channel through a separate tuple/bit-vector path, then repeats all 23
deletions and 23 sign flips in every frame: 552 of each, all detected. Across
the primary frame/product domains, 220,800 parity commutators are also tested
with zero failures.

The load-bearing restriction is total-parity superselection of observables,

```text
A_even = { A : [A, P_total] = 0 }.
```

No parity value is selected. The statement covers either parity sector and
arbitrary block-diagonal mixtures

```text
rho = p rho_+ direct-sum (1-p) rho_-,    0 <= p <= 1.
```

It does not cover coherent cross-parity matrix elements. Opposite choices of
an odd extension restrict to the same 23-row even algebra, so the positive
theorem neither needs nor selects an odd representative.

## Exact boundary

This package closes the moving-frame signed covariance of the two-cell
parity-even input/Bell algebra and the imported companion-register correction
rows. It does not provide a gate-by-gate parity-conserving dilation of those
corrections: 12 of the 23 private-dual correction rows anticommute with matter
parity (indices 0-5 and 11-16), while 11 commute. A local parity-exchange
carrier or another even dilation is therefore still required before those
conditional rows are a closed fermionic physical circuit.

The package also does not execute the full prefix, Bell circuit, and
non-Clifford recurrent update in one common state/tableau executor. Separate
landed packages establish the literal prefix, collision-free Bell schedule,
and recurrent update; exact interface-packet equality among those executors is
useful modular evidence, not a monolithic execution theorem, and is not
promoted here.

The 24 proper-frame templates and eight coframe-origin sectors are supplied to
the verification. The frame loop is a covariance audit, not a physical
runtime orientation selector. The package does not derive or autonomously
prepare the parity-superselected input, local-center sector, coframe, clean
ancillas, finite boundary, chart, or occurrence token.

No result here is a Record, Born rule, realized-history selector,
source/gravity law, or physical time law. No minimum-resource, impossibility,
shared-obstruction, or axiom-pressure claim is made.

## Supplied / derived / open

### Supplied

- the two-cell `(2,1,1)` placement, seven-mode/full128 encoding conventions,
  fixed local-center data, finite boundary, and encoded input;
- total-parity superselection as an observable-algebra restriction, without a
  fixed parity eigenvalue;
- the three-register companion Choi/input/correction palette and clean typed
  ancillas, including algebraic conditional correction rows but no declared
  fermionic parity-exchange carrier;
- the proper-cubic frame templates, coframe-origin sectors, signed-port chart,
  and fixed circuit order; and
- permission to retain or trace the declared typed environments.

### Derived

- the exact rank-23 parity-even Bell-generator family on the two-cell fixture;
- parity commutation for every retained generator in every frame;
- 13,248 direct binary and signed frame-product comparisons with zero
  failures;
- exact signed source-role and graph-transport compatibility;
- an explicit companion-register correction family on the declared palette,
  together with the exact 11-even/12-odd parity census; and
- active all-row mutation/deletion controls plus an independent reconstruction.

### Open

- one common-executor prefix/Bell/recurrent-update channel rather than exact
  modular interface composition;
- a gate-by-gate parity-conserving correction dilation, including local genesis
  and reset/renewal of any parity-exchange carrier;
- autonomous genesis or local enforcement of the supplied parity SSR,
  coframe, local-center sector, encoded input, clean ancillas, and occurrence;
- lattice-wide gluing beyond the tested two-cell placement;
- an unrestricted coherent cross-parity extension;
- renewal, fault rejection or repair, and permanent Record production; and
- unchanged bridges into causal duration, source/gravity, Born/history, and
  no-refit prediction surfaces.

## Active controls

The primary executable detects all 23 correction deletions and all 23
Bell-measurement sign flips. The independent checker detects all 552
frame-resolved correction deletions and all 552 frame-resolved sign flips; its
minimum bidirectional signed-span failure is two. Both runners also expose the
same correction-parity census in every frame: 11 commuting and 12
anticommuting rows. The independent checker verifies that two distinct odd
extensions have identical restriction to the retained even algebra. That is a
boundary diagnostic, not an odd-channel construction.

## No-go discipline

No negative theorem ships. An unrestricted odd extension remains a live
constructive route, as do richer local frame sections and projective or
orientation-register implementations. The positive even-algebra construction
therefore blocks any broad compiler no-go and creates no axiom pressure.

## Verdict

The bounded input/Bell covariance problem no longer requires a choice of
global parity value or a host-side parity query on the tested two-cell even
observable algebra. This is not yet a fully physical fermionic correction
circuit: the exposed 12-row parity-exchange requirement, physical
genesis/enforcement of the supplied sectors, lattice-wide gluing, and a
common-executor composition with the recurrent update and downstream TOE
interfaces remain open.
