# Cycle 827: parity-safe typed atlas for the Cycle-719 controller

Date: 2026-07-30

Type: bounded_theorem

Authority: none

Audit: unset

Runner:
[`frontier_cycle827_cycle719_parity_safe_typed_controller_atlas_2026_07_30.py`](../scripts/frontier_cycle827_cycle719_parity_safe_typed_controller_atlas_2026_07_30.py)

Receipt:
[`cycle719_parity_safe_typed_controller_atlas_cycle827_receipt_2026_07_30.json`](../outputs/cycle719_parity_safe_typed_controller_atlas_cycle827_receipt_2026_07_30.json)

Direct inputs:
[Cycle 826 endpoint/history interface](COMPANION_ENDPOINT_CYCLE719_HISTORY_INTERFACE_CYCLE826_BOUNDED_THEOREM_NOTE_2026-07-30.md)
and
[Cycle 719 recurrent controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md).

## Question

Can the landed Cycle-719 recurrent controller be recompiled into the fixed
charged/neutral physical-M2 grammar required by the Cycle-823 companion code,
without changing its semantic update or using a nonlocal parity service?

## Result

Yes, for the declared finite 12-bank controller and a supplied fixed atlas.
The legacy expansion contains six Toffoli gates in which the charged matter
control occupies the second control slot. Its standard decomposition therefore
contains 12 neutral-control/charged-target CNOT factors, each violating the
fixed global parity prefix. Toffoli controls are symmetric. Reordering those
six controls preserves every logical gate but changes the decomposition
orientation so charged matter is always a control and never a target.

The normalized one-controller-step word contains 61,562 semantic gates and
740,226 one/two-M2 factors:

- 303,942 CNOT;
- 96,952 H;
- 193,904 T; and
- 145,428 T-dagger.

The original word has 12 elementary parity violations; the normalized word
has zero. All six hostile restorations of the old control order are detected.
The Toffoli matrix residual is `7.346882794269506e-16`. The normalized
controller and its inverse agree exactly with the landed controller on all
four endpoint/pointer rows.

## Fixed typed atlas

The compiler assigns the 12 matter sites and 84 new charged corridor sites to
the charged type. Charged control transport uses FSWAP through supplied blank
charged route work; every other route uses SWAP through neutral sites. The
charged corridors hit no persistent site.

The full word has 41,717 unique two-M2 endpoint pairs and 303,942 two-M2
factor occurrences. Eight unique pairs (24 occurrences) carry a charged
control. All eight charged routes close. Reserving them forces 1,297 neutral
pair routes, representing 7,700 occurrences, away from the charged palette;
all close without fit changes.

The resulting atlas has:

- zero missing paths, repeated-site/nearest-neighbour failures, operand-order
  failures, or route-return failures;
- zero charged/neutral fixed-type overlap;
- maximum route distance 45;
- 13,315,498 routed gates per controller step and 1,731,014,740 for the fixed
  130-step controller orbit, before the separate Cycle-823 port/caps; and
- 41,056 nonlocal unique routes whose first-swap deletion is detected by the
  operand-position certificate.

The legacy Manhattan atlas is an active adverse control: it has 10 charged
corridor hits on neutral persistent sites, 34 charged/neutral corridor
overlaps, and 12 neutral-corridor hits on charged matter sites. These are
route-specific failures repaired by the new atlas, not a no-go result.

All route edges, the charged/neutral partition, and 256 sampled composition
sites transport with zero failures under all 24 proper-cubic frames and all
576 ordered products. This is passive transport of a supplied coframe and
atlas, not intrinsic atlas generation.

## Supplied / derived / open

Supplied:

- the Cycle-719 finite 12-bank program, unique source token, bank genesis,
  successful admission sector, and program occurrence;
- the fixed laboratory coframe and offline route atlas; and
- clean neutral work and blank charged corridor M2 at genesis.

Derived:

- six semantics-preserving control reorderings;
- a 740,226-factor prefix-parity-safe controller word;
- the complete fixed charged/neutral route atlas with active legacy and route
  deletion controls; and
- proper-cubic transported-atlas covariance.

Open:

- a same-chart collision-free physical port from the Cycle-823 endpoint sites
  into this controller placement;
- intrinsic query-free atlas generation and local type/genesis enforcement;
- autonomous unique-token/bank preparation, objective admission, renewal, and
  separated multi-source arbitration; and
- physical time, an inaccessible inverse or permanent Record, Born/history,
  source/gravity, and a no-refit prediction bridge.

## Boundary and TOE effect

This is a positive bounded physical compiler result for one supplied finite
controller. It is not a translation-invariant autonomous law, time law,
Record/Born law, source/gravity law, minimum, no-go, or axiom-pressure result.
`C_local` narrows because the recurrent controller now shares the companion
code's fixed parity grammar. `C_ref` remains open at physical co-location,
coframe/atlas genesis, and the unique-token sector. `C_num`, `C_wrap`,
`C_int`, and `C_source` do not move.

## Reproduction

```bash
PYTHONPATH=scripts python3 \
  scripts/frontier_cycle827_cycle719_parity_safe_typed_controller_atlas_2026_07_30.py
```

Expected terminal:

```text
CYCLE827_CYCLE719_PARITY_SAFE_TYPED_CONTROLLER_ATLAS_BOUNDED_PASS
```
