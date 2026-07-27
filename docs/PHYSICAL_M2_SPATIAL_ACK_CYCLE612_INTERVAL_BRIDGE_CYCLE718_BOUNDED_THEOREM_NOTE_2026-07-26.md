# Cycle 718: physical-M2 spatial ACK and Cycle-612 interval bridge

Date: 2026-07-26

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runners:

- [`scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py`](../scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py)
- [`scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py`](../scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py)

Load-bearing inherited surfaces:

- [Cycle 715 recurrent directional packet bank](RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 714 fixed full34 physical-M2 packet](PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 713 endpoint instrument](PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 712 joint two-cell update](JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 704 local-Gauss endpoint bridge](work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md);
- [Cycle 610 relational-duration interface](work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md);
- [Cycle 612 causal-order interface](work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md); and
- [Cycle 11 bilateral reversible export prior art](work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md).

## Question

Can the landed Cycle-713 two-cell physical endpoint instrument commit one
admitted packet into a bounded, spatial ACK/export law on physical M2 sites,
and can the resulting packet be mapped reversibly into the landed Cycle-612
causal-order and interval interface without calling a circuit ordinal time or
a reversible packet a permanent Record?

## Construction

The first runner expands a structured NEW/ACK transposition into one- and
two-M2 primitives.  Six endpoint-labelled 39-M2 bundles then move through
disjoint two-layer nearest-neighbour A/B loops.  The update includes a
persistent pending latch and two local HOLD shields so that a blocked matter
event is retained while the matter cell itself sees an identity.  The source,
controller, rails, and transient route workspace are placed explicitly on the
M2 lattice; each routed macro returns its route workspace.

The second runner starts at the exact post-shift station-one bundle of that
layout.  It first tests and rejects a direct identification with the Cycle-610
chain: the raw identity repeats `0,1,0,1` and the raw predecessor word repeats
`3,2,3,2`, so all four tested rows differ from the required chain identity and
predecessor data.  A separate reversible bit-level adapter then writes the
34-bit Cycle-704 payload, six-bit identity, predecessor/head data, K16
rotor/carry, K64 next address, and freshness into a clean output packet.  Its
output is checked against the unchanged Cycle-612 `JointOrder` and Cycle-704
packet-interface controls.

The adapter is a local field update, but repeated collection still supplies a
host-selected fresh blank output cell.  The test follows this selector through
24 finite cells and exposes exhaustion on the 25th attempt.  The selector is
not hidden in a clock, schedule, duplicate-membership table, or global parity
service.

## Exact evidence

Spatial ACK/export:

- all 256 lawful orientation/head/rotor/identity/pending rows satisfy the
  structured commit contract, and all named dirty, refusal, inverse, and
  deletion controls are active;
- all 4,096 pending-matter rows have maximum shield residual
  `2.2263907214770273e-16`; deleting either shield is detected;
- held loop lengths 13 and 17 pass one, two, and four applications on all 79
  Cycle-713 `N<=2` sources;
- the largest intertwiner residual is `6.074003643852178e-16`, largest norm
  residual is `4.218847493575595e-15`, and number leakage and bad-packet weight
  are zero;
- length 13 uses 6,199 assigned M2, 25,181 physical primitives, 190,279 routed
  nearest-neighbour gates, and 13,755 touched M2;
- length 17 uses 8,071 assigned M2, 30,797 physical primitives, 195,895 routed
  nearest-neighbour gates, and 15,627 touched M2;
- assigned and touched support grow by 468 M2 per added rail station, and the
  physical word grows by 1,404 primitives per station;
- all 24 proper-cubic frames, 576 ordered products, and the declared held
  translations have zero failures.

Cycle-612 interval adapter:

- all 64 address classifications and inverses pass, including the explicit
  25th-attempt exhausted state;
- all 41 single dirty-target rows and 256 multi-dirty rows refuse, arbitrary
  inverse has zero failures on 64 rows, and every named deletion is detected;
- the finite chain yields intervals `9`, `12`, and `21`, with exact additivity
  and reversal;
- the unchanged Cycle-612 control gives two consistent admissions, refuses an
  inverted edge, detects a forced cycle, and returns `no_opportunity` when no
  endpoint is present;
- the physical adapter uses 158 assigned M2, 4,661 primitives, and 39,317
  forward plus 39,317 inverse nearest-neighbour routed gates, with maximum
  route distance 48 and 596 touched M2;
- route workspace returns exactly, all active deletions fire, there are zero
  placement or transient crossings with the other live spatial rails, and all
  24 frames and 576 ordered products pass.

## Supplied, derived, and open

Supplied:

- the landed Cycle-713 two-cell decoder and full free/seam/contact update;
- `BINDER=ACTUAL=ADMISS=LAW=1`, clean head/rotor/identity/work, one pending M2,
  and twelve HOLD M2 at genesis;
- six finite A/B packet loops as one proper-cubic orbit, a blank no-return
  pre-wrap sector, and fixed commit-before-shift layer order;
- one acknowledged packet at post-shift station one;
- one host-selected blank adapter cell per append, empty-head sentinel 63,
  initial address 0, initial K16 rotor 14, finite capacity 24, the offline gate
  word, and blank routing workspace.

Derived on the declared domain:

- the structured local NEW/ACK circuit, endpoint cleanup, retry echo, and
  pending-event shield;
- two-layer nearest-neighbour packet transport, exact inverse, bounded support
  scaling, and active proper-cubic/translation covariance;
- a literal reversible Cycle-704 packet projection with predecessor, address,
  rotor/carry, freshness, exhaustion, refusal, and deletion controls;
- unchanged Cycle-612 causal-order outcomes and numeric interval
  additivity/reversal.

Open:

- local genesis or enforcement of the blank/no-return, pending, HOLD, and clean
  work sectors;
- positive-density multi-source rail arbitration, collision handling, and
  renewal after loop wrap or finite adapter exhaustion;
- removal of the host-selected fresh blank adapter cell and physical
  enforcement of unique membership across the 24-cell chain;
- objective occurrence/admission, empirical duration calibration, and an
  inaccessible inverse;
- Record permanence, Born realization, physical time, source/gravity response,
  and a prediction-surface bridge.

## Boundary

This is a positive literal physical-M2 construction for one isolated source in
a supplied finite pre-wrap resource sector.  It is not a translation-invariant
positive-density recurrent law, a genesis/enforcement theorem, a Record or
Born law, a physical-time law, a source/gravity law, a minimum, a no-go, or an
axiom-pressure result.  The integer interval is a decoded reversible field,
not physical time.  The circuit-layer ordinal is not used as time.  Applying
the one-cell adapter again to its retained output is an active hostile control,
not a lawful recurrent update; the moving blank-cell selector remains the
sharp autonomy wall.
