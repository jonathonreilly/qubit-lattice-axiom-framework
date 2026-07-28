# Companion-bank liveness schedule extension and endpoint/interval packet projection

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional construction

**Type:** bounded_theorem

Primary runner:

- [`frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28.py`](../scripts/frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28.py)

Independent reconstruction:

- [`frontier_companion_bank_endpoint_interval_projection_independent_check_2026_07_28.py`](../scripts/frontier_companion_bank_endpoint_interval_projection_independent_check_2026_07_28.py)

Load-bearing predecessor:

- [`COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md`](./COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. The predecessor has authority `none` and audit `unset`; this dependent
claim is likewise unaudited and does not enter the retained chain.

All identities, schedule slots, rotor values, carries, and decoded intervals
below are finite circuit/software data. None is physical time, duration, rate,
cadence, energy, or a permanent Record.

## Result

Under the supplied packet-projection convention below, the landed
companion-bank liveness schedule admits a collision-free Stage-E extension,
and the resulting declared packet table is compatible with the unchanged
landed `EventChain` implementation on the held finite boxes.

For both the Bell-character and even-exchange input variants on `2x2x2` and
`3x2x2`:

- 24 Stage-E access words read five selected register identifiers under the
  clean/live/retained bookkeeping and write 24 fresh packet-record registers;
- all 120 new producer-consumer handoffs are declared and consumed, with zero
  collisions or liveness violations;
- five separately evaluated static algebraic predicates equal one, and the
  supplied projection convention uses those five values as the
  `certificate`, `binder`, `actuality`, `admissibility`, and `law_domain`
  fields for every opportunity;
- the unchanged `EventChain(bank=24)` admits identities `0..23`, reproduces
  its rotor/carry/predecessor state exactly, and decodes
  `interval(2,11) = 9`, `interval(11,23) = 12`,
  `interval(2,23) = 21`, and `interval(11,2) = -9`; and
- the Stage-E key multiset is invariant over 24 proper cubic frames and eight
  translation parities.

The unchanged `JointOrder` implementation also replays its six frozen control
outcomes and passes its class-module tripwire. That is an independent
byte-pinned regression: this construction does **not** feed the packet table
into `JointOrder`.

## Exact projection convention

The packet table supplies ascending identities `0..23`, orientation `+1`, and
one value for each admission field. The field-to-register association is:

| field | selected parent register | static value calculation |
|---|---|---|
| `certificate` | first Bell ancilla for the Bell-character variant, or first declared port carrier for the exchange variant | first Bell private-dual/row pairing, or absence of a port-parity certificate failure |
| `binder` | second Bell ancilla, or second declared port carrier | second Bell private-dual/row pairing, or absence of a port-parity certificate failure |
| `actuality` | first pump-syndrome register | first pump private-dual/row pairing |
| `admissibility` | second pump-syndrome register | second pump private-dual/row pairing |
| `law_domain` | third pump-syndrome register | third pump private-dual/row pairing |

Each predicate evaluates to one on the held fixtures. The runner separately
traces each selected register to an origin-stage write and a final
`retain_after` owner.

Those two facts must not be conflated. The schedule model records access modes
and ownership, but does not carry or evaluate a quantum/classical register
state. The numeric packet values are static algebraic certificate predicates;
they are not measurements or simulated reads of the selected registers. The
register association and the use of those predicate values as packet fields
are supplied conventions.

## Unchanged harness boundary

The primary runner byte-checks the landed `EventChain` and `JointOrder` source
files against the SHA-256 pins exported by
[`frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py`](../scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py).
It neither modifies nor subclasses either harness.

For the declared all-one packet rows, admission uses the unchanged grammar

```text
opportunity = certificate AND binder
ADMIT = opportunity AND freshness AND actuality AND admissibility AND law_domain
```

and interval decoding uses stored chain state:

```text
16 * carries_after_start_through_end + end_rotor - start_rotor .
```

Controls delete one Stage-E handoff, flip the actuality field for identity 11,
request a 25th admission, reorder identities 11 and 23, and scan the primary
runner for harness replacement or attribute injection. Every fault is
detected.

## Supplied, derived, and not tested

### Supplied

- the predecessor's companion-bank and finite-schedule conventions;
- the ascending identity sequence, orientation, field-to-register
  association, and use of the five static predicates as packet values;
- the finite bank and the unchanged landed harness implementations.

### Derived

- the four collision-free Stage-E liveness extensions and exact handoff
  accounting;
- the five unit-valued static algebraic predicates and selected-register
  liveness traces;
- conditional `EventChain` admission, state agreement, and the four exact
  interval values under the supplied packet rows;
- geometry-key covariance and the named fault controls; and
- unchanged harness hashes plus the separate `JointOrder` regression.

### Not tested by this construction

- register-state readout or a reversible value-carrying packet encoder;
- an end-to-end composite channel or logical intertwiner through the
  predecessor's recurrent tail;
- dynamics-derived occurrence, admission, law-domain, or identity selection;
- a packet-driven `JointOrder` construction; and
- physical time, empirical units, Record permanence, source/response
  dynamics, gravity, or continuum interpretation.

“Not tested” is a scope statement, not a no-go or a claim that any route is
structurally closed.

## Independent reconstruction

The independent runner blocklists the primary runner. From the landed parent
module it rebuilds both variants on both held boxes, independently recomputes
the five static predicates, traces the five selected registers, and reruns the
parent liveness walk. It separately parses the primary packet declarations,
reimplements the finite admission/rotor/carry/interval model, compares every
admission and cell against the landed `EventChain`, verifies the harness hash
pins, and exercises the actuality, exhaustion, and hostile-order controls.

This confirms the bounded conjunction above. It does not promote static
certificate predicates into register-state observations.

## Claim boundary

The theorem is a finite compatibility certificate: the predecessor liveness
schedule can be extended by the declared packet-access surface, and the
separately supplied unit-valued projection produces the stated unchanged
`EventChain` outputs. It is not a dataflow theorem, composite-channel theorem,
occurrence law, physical-time construction, or causal-order packet feed.
