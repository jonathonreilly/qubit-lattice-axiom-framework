# Cycle 826: companion endpoint into the Cycle-719 history interface

Date: 2026-07-30

Type: bounded_theorem

Authority: none

Audit: unset

Runner:
[`frontier_cycle826_companion_endpoint_cycle719_history_interface_2026_07_30.py`](../scripts/frontier_cycle826_companion_endpoint_cycle719_history_interface_2026_07_30.py)

Receipt:
[`companion_endpoint_cycle719_history_interface_cycle826_receipt_2026_07_30.json`](../outputs/companion_endpoint_cycle719_history_interface_cycle826_receipt_2026_07_30.json)

Direct inputs:
[Cycle 823 companion endpoint instrument](COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_CYCLE823_BOUNDED_THEOREM_NOTE_2026-07-30.md)
and
[Cycle 719 recurrent matter/history controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md).

## Question

Does the complete Cycle-823 companion seam expose exactly the endpoint state
that the landed Cycle-719 recurrent finite history controller consumes, with
no new selection rule or host-written direction label?

## Result

At the declared register interface, yes. Cycle 823 leaves the post-seam
endpoint occupations `(left,right)` and the coherent pointer
`p=left xor right`. The unchanged Cycle-719 controller maps the four rows as

```text
(left,right,p) = (0,0,0) -> no packet
(left,right,p) = (1,0,1) -> orientation -1
(left,right,p) = (0,1,1) -> orientation +1
(left,right,p) = (1,1,0) -> no packet
```

It preserves both endpoint occupations, returns the source pointer and its
two-rail controller token/work sector, and its inverse restores every input.
The runner lifts this four-row table through every physical and target
reachable phase class of the Cycle-823 complete seam: 1,312 cases over 82
edges and four held boxes, with zero interface or composition failures and
maximum residual zero.

This is an exact register-interface composition. It is not yet a same-chart
physical composition: the collision-free physical placement and route that
identifies each Cycle-823 endpoint/pointer triple with a translated Cycle-719
controller instance remain open.

## Controls

Deleting the Cycle-719 success finalizer is detected on both pointer-true
rows and leaves the source pointer pending. Dirty-pointer inputs are detected
on all four truth rows. Zero- and two-controller-token sectors differ from
the lawful output on both pointer-true rows; pointer-false no-ops are not
misreported as token-sector witnesses.

## Supplied / derived / open

Supplied:

- the landed Cycle-823 finite full-seam compiler and clean endpoint registers;
- the landed Cycle-719 unique token, finite program ring, clean bank/work
  sector, fixed program occurrence, and successful admission sector; and
- the register identification between the two endpoint occupations/pointer
  and the controller source inputs.

Derived:

- the exact four-row endpoint-to-history interface;
- its exact coherent lift through all 1,312 reachable Cycle-823 phase classes;
- successful pointer/token/work return and exact inverse on the finite bank;
  and
- active finalizer, dirty-pointer, zero-token, and two-token controls.

Open:

- same-chart collision-free placement and physical routing between the two
  landed compilers;
- autonomous token and clean-bank genesis or local enforcement;
- renewal after finite capacity and multi-source arbitration;
- objective occurrence/admission and an inaccessible inverse; and
- physical time, permanent Record, Born/history, source/gravity, and a
  no-refit prediction bridge.

The packet chain remains reversible. It is not called a Record or realized
history. Controller ordinals and packet integers are not called time. No
impossibility, minimum-content, shared-obstruction, or axiom-pressure claim is
made.

## TOE effect

This narrows the semantic side of `C_local` and the Cycle-612/history bridge:
the new complete companion seam needs no additional direction-selection law
to enter the landed controller. `C_ref` remains open at the physical
co-location/route boundary, `C_wrap` remains open because no duration law is
attached, and `C_num`, `C_int`, and `C_source` do not move.

## Reproduction

```bash
PYTHONPATH=scripts python3 \
  scripts/frontier_cycle826_companion_endpoint_cycle719_history_interface_2026_07_30.py
```

Expected terminal:

```text
CYCLE826_COMPANION_ENDPOINT_CYCLE719_HISTORY_INTERFACE_BOUNDED_PASS
```
