# Teleportation 3D+1 Causal Bell-Record Channel Note

**Date:** 2026-04-26
**Type:** open_gate
**Status:** open / finite 3D+1 local record-propagation artifact
**Runner:** `scripts/frontier_teleportation_3d1_causal_record_channel.py`

## Scope

This artifact replaces the earlier generic directed-DAG record harness with an
explicit 3D spatial lattice plus one discrete causal/time direction. It remains
only a classical Bell-record channel for ordinary quantum state teleportation.

The model does not transport matter, mass, charge, energy, or objects. It does
not claim faster-than-light signaling or controllable pre-message influence.

## Model

Alice emits an already-created two-bit Bell record at a 3D lattice site and
integer tick:

```text
record = (z, x)
source event = (x_A, y_A, z_A, t_A)
target site = (x_B, y_B, z_B)
```

The channel accepts either a 3D Manhattan or 3D Chebyshev metric. The default
run uses Manhattan locality with speed one site per tick:

```text
distance = |dx| + |dy| + |dz|
earliest_delivery_tick = emitted_at_tick + ceil(distance / speed)
```

For the default audit:

```text
lattice shape = (8, 6, 5)
Alice site/tick = (1, 1, 1), t=4
Bob site = (5, 3, 2)
metric/speed = manhattan / 1 site per tick
distance = 7
earliest delivery tick = 11
```

The emitted worldline is local at each tick:

```text
t=4:(1, 1, 1)
 -> t=5:(2, 1, 1)
 -> t=6:(3, 1, 1)
 -> t=7:(4, 1, 1)
 -> t=8:(5, 1, 1)
 -> t=9:(5, 2, 1)
 -> t=10:(5, 3, 1)
 -> t=11:(5, 3, 2)
```

The channel schedules and delivers the record. It does not derive the Bell
bits from the lattice, from a measurement apparatus, or from the Bell resource.

## Gates

The runner checks:

1. The 3D+1 worldline is local under the configured metric and integer speed.
2. The earliest delivery tick equals the distance/velocity rule.
3. A target event outside the future cone fails, and Bob cannot receive before
   the cone reaches the target.
4. A duplicate record id is rejected and a delivered record cannot be received
   twice.
5. Wrong receiver and wrong 3D-site receives fail.
6. The correct delivered two-bit record restores Bob's branch state.
7. Wrong, dropped, and delayed records act as controls.
8. Bob's pre-delivery local state is input-independent and equals `I/2` to
   numerical precision.

The first four probe density matrices span the one-qubit operator space.
Because the reduced-state and unconditioned Bell-branch maps are linear in the
input density matrix, the runner checks this rank explicitly before treating
the finite probe calculation as input-independent. The fifth probe is a
redundant non-axis control.

## First Run

Commands:

```bash
python3 docs/audit/scripts/ledger_io.py --materialize
python3 -m py_compile scripts/frontier_teleportation_3d1_causal_record_channel.py
python3 scripts/frontier_teleportation_3d1_causal_record_channel.py
```

The runner cache pins the shared boundary helper, the terminal conclusion
note, and the eleven canonical ledger shards read by the boundary report. The
materialization command rebuilds the ignored monolithic read cache from those
tracked shards before execution.

Observed output:

```text
cache rematerialized
TELEPORTATION 3D+1 CAUSAL BELL-RECORD CHANNEL
Status: open / finite 3D+1 local record-propagation artifact

3D+1 discrete light cone:
  lattice shape: (8, 6, 5)
  metric / speed: manhattan / 1 site(s)/tick
  Alice event: site=(1, 1, 1) t=4
  Bob target site: (5, 3, 2)
  spatial distance: 7
  expected light-cone latency: 7 tick(s)
  earliest delivery tick: 11
  propagation worldline: t=4:(1, 1, 1) -> t=5:(2, 1, 1) -> t=6:(3, 1, 1) -> t=7:(4, 1, 1) -> t=8:(5, 1, 1) -> t=9:(5, 2, 1) -> t=10:(5, 3, 1) -> t=11:(5, 3, 2)
  worldline local under metric: True
  delivery event inside future cone: True

Explicit Bell record:
  record: Psi- bits(z,x)=(1, 1) id=bell-record-3d1-0001
  channel derives Bell bits: False
  Bell branch probability: 0.2499999999999999

Causal delivery checks:
  earliest tick equals distance/velocity rule: True
  target event at t=10 outside cone rejected: True
  receive before cone arrival blocked: True
  wrong receiver blocked: True
  wrong 3D site blocked: True
  duplicate record id rejected: True
  receive at delivery exactly once: True

Correction and record controls:
  correct delivered-record fidelity: 1.0000000000000000
  wrong-record fidelity: 0.3333333333333334
  dropped/pre-delivery no-correction fidelity: 0.3333333333333333
  dropped record remains undelivered: True
  delayed control blocked at base arrival: True (base t=11, actual t=13)
  delayed control delivered late: True
  delayed delivered-record fidelity after waiting: 1.0000000000000000

Bob pre-message input-independence:
  probe states: 5
  operator-space rank of first four probe densities: 4 / 4
  max Bob trace distance to I/2 before Alice measurement: 2.220e-16
  max Bob trace distance to I/2 after Alice measurement before delivery: 3.331e-16
  max pairwise pre-delivery Bob-state distance across inputs: 1.388e-16
  max Bell probability error from 1/4: 1.110e-16

Acceptance gates:
  3D+1 light-cone locality: PASS
  distance/velocity earliest arrival: PASS
  outside-cone attempts fail: PASS
  no duplicate delivery: PASS
  correct record restores Bob state: PASS
  wrong/dropped/delayed controls: PASS
  Bob pre-delivery input-independence: PASS
  explicit not derived record channel: PASS

Claim boundary:
  This models only a causal classical Bell-record channel.
  It is ordinary quantum state teleportation only.
  It does not transfer matter, mass, charge, energy, or objects.
  It does not enable faster-than-light signaling or pre-message control.
  It does not derive the Bell record, Bell resource, or measurement dynamics.

Downstream boundary checks:
  downstream teleportation boundary: teleportation_causal_channel_note has audited bounded/status support: PASS (effective=retained_bounded, audit=audited_clean)
  downstream teleportation boundary: teleportation_measurement_record_note has audited bounded/status support: FAIL (effective=audited_conditional, audit=audited_conditional)
  downstream teleportation boundary: teleportation_apparatus_dynamics_closure_note has audited bounded/status support: FAIL (effective=audited_failed, audit=audited_failed)
  downstream teleportation boundary: teleportation_dynamical_resource_generation_note has audited bounded/status support: PASS (effective=retained_bounded, audit=audited_clean)
  downstream teleportation boundary: teleportation_resource_fidelity_note has audited bounded/status support: FAIL (effective=audited_conditional, audit=audited_conditional)
  downstream teleportation boundary: teleportation_retained_axis_operator_algebra_closure_note has audited bounded/status support: PASS (effective=retained_bounded, audit=audited_clean)
  downstream teleportation boundary: teleportation_cross_encoding_maps_note has audited bounded/status support: FAIL (effective=audited_conditional, audit=audited_conditional)
  downstream teleportation boundary: teleportation_three_register_cross_encoding_note has audited bounded/status support: FAIL (effective=audited_conditional, audit=audited_conditional)
  downstream teleportation boundary: teleportation_no_signaling_audit has audited bounded/status support: PASS (effective=retained_bounded, audit=audited_clean)
  downstream teleportation boundary: teleportation_3d_operator_consistent_end_to_end_note has audited bounded/status support: PASS (effective=retained_bounded, audit=audited_clean)
  downstream teleportation boundary: teleportation_conclusion_boundary_note has audited bounded/status support: PASS (effective=audited_renaming, audit=audited_renaming)
  downstream teleportation boundary: lane remains state-teleportation only with no-transfer boundary: PASS (checked conclusion boundary note)
  downstream teleportation boundary: finite planning support is not nature-grade closure: PASS (planning closure and nature-grade hold are distinct)

Downstream boundary disposition:
  downstream retained-grade alignment currently complete: False
  downstream status is reported but does not gate this independent upstream finite-channel result.
```

The three commands exit zero. The runner reports `PASS` for:

- 3D+1 light-cone locality;
- distance/velocity earliest arrival;
- outside-cone attempts fail;
- no duplicate delivery;
- correct record restores Bob state;
- wrong/dropped/delayed controls;
- Bob pre-delivery input-independence;
- explicit not-derived record channel.

## Limitations

- The Bell record is supplied to the channel; the channel does not derive it.
- The Bell measurement, durable classical record, and apparatus dynamics remain
  idealized.
- The Bell resource is assumed by this runner.
- The dropped and wrong-record controls are sanity checks, not security proofs.
- The lattice is a discrete planning model, not a relativistic field theory.
- The artifact supports ordinary quantum state teleportation only. It does not
  transfer matter, mass, charge, energy, or objects, and it does not support
  faster-than-light signaling.

## Downstream Boundary Alignment (2026-06-13; corrected 2026-07-27)

The runner prints the current audit-derived status of the downstream
teleportation boundary stack and checks the terminal conclusion note's
state-teleportation-only and no-transfer wording. Those downstream rows do not
serve as premises of this earlier finite channel computation, so their later
audit demotions are reported explicitly but do not flow backward into the
exit status of the eight independent acceptance gates.

The downstream report is status telemetry, not support for the finite channel
claim and not a claim that the broader stack is closed. The source artifact
still treats the Bell record and ordinary teleportation resource as supplied,
and it does not derive a physical record carrier, durable measurement
apparatus, matter transfer, or faster-than-light control.
