# Cycle 704 local-Gauss to Cycle-612 endpoint bridge

Date: 2026-07-25

Authority: none. Audit: unset. Constitutional effect: none.

Runner:
`scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py`

## Result

A first conditional interface from the Cycle-703 local-Gauss matter code to
the landed Cycle-610/612 predecessor and causal-order code closes exactly.

For an exact dressed matter FSWAP on an oriented two-cell bond, define the
candidate endpoint opportunity

```text
P_B(before,after) = OR_a [B_a(before) != B_a(after)].
```

On the tested seam factor only the two transported matter endpoints can
change.  Since `B_a=(-1)^{n_a}` on the declared occupation basis,
`P_B=n_u xor n_v`.  The runner executes all 4,096 two-cell matter columns for
all 36 directed port pairs:

- 73,728 changing columns have `P_B=1`;
- 73,728 nonchanging columns have `P_B=0`;
- predicate, B-pointer, matter-delta, local-D, and reference-update failures
  are all zero;
- diagonal contact gives zero false endpoints;
- all 24 proper-cubic frames preserve the port family without an exterior
  ordering table.

The predicate is computed by a seven-M2 reversible XOR/Toffoli comparator.
Its complete 128-row truth table has zero inverse failures.  The two physical
endpoint `B` words occupy at most 11 edge M2 across two owner cells; a single
`B` word has weight at most 6.  No update ordinal or schedule position is read
or stored.

This is a candidate opportunity predicate, not an occurrence law.

## Closed interface equations

Let `A_packet` be the reversible packet append, `Pi_610` forget its extra
reversible payload and retain the landed Cycle-610 `EventCell`, and `D` denote
the interval decoder.  On the declared lawful domain with explicit supplied
tokens, the runner executes

```text
Pi_610 A_packet(P_B, supplied_tokens) = A_610 Pi_610
D_packet = D_610 Pi_610
J_612 Pi_610(packet identities) preserves JointOrder admission/refusal.
```

The first equation is checked after every one of 25 append attempts against
the unchanged landed `EventChain.admit`.  Statuses match exactly: 24 admitted,
then bank exhaustion.  Refill, no-opportunity, duplicate-freshness, and
missing-actuality controls also match exactly.

The second equation is checked on forward and reverse intervals:

```text
D(A,B)=9, D(B,C)=12, D(A,C)=21,
D(A,C)=D(A,B)+D(B,C), D(B,A)=-D(A,B).
```

There are zero packet-projection or interval mismatches.

The third equation uses the landed Cycle-612 `JointOrder` class unchanged.
Two matter-qualified sequential co-registrations are admitted and acyclic;
the existing inverted registration is refused; forcing the two inverted
identifications still creates a detected cycle; and a no-B-change control is
not presented to the harness.

## Reversible packet

Each bounded packet cell stores:

- a 6-M2 predecessor address;
- four pre-rotor and four post-rotor M2;
- one carry M2;
- the 12-bit matter delta;
- endpoint, binder, valid, and orientation M2;
- the three supplied actuality/admissibility/law-domain bits.

Total: 34 payload M2 per packet cell, a 6-M2 head, and the declared finite
24-cell bank.  A blank-address selector is supplied.  The resource is large
but constant on this finite interface; no asymptotic or minimality claim is
made.

Append retains the old head and rotor in the new packet, so unappend is exact
on the last-packet domain.  Six successive appends return exactly to the
initial state under six inverses and replay to the identical forward state.
Additionally, 96 cases spanning every K16 rotor value, both orientations,
and three matter-delta words have zero inverse and carry-truth failures.

The accessible inverse is positive evidence for a reversible candidate
packet and explicit evidence that this object is **not** a permanent Record.

## What is and is not physical

Physical and executed:

- `B` is the actual local BKSF product of incident edge-M2 Z operators;
- the predicate comparator is a bounded reversible binary-M2 permutation;
- the underlying dressed seam action is the exact Cycle-703 local-D action;
- the predecessor/rotor/carry payload is a bounded reversible M2 word;
- projection to the actual landed Cycle-610/612 classes is exact.

Conditional or supplied:

- the input is already in the local-D occupation-basis code sector;
- blank predicate/payload M2 and a blank-address selector are supplied;
- actuality, admissibility, law-domain, and co-registration ports are
  supplied;
- the K16 rotor convention and cross-order consistency rule are consumed
  from Cycles 610/612.

Open:

- the BKSF edge-qubit common E and physical state preparation;
- objective occurrence and an autonomous admission law;
- Record permanence;
- an empirical unit or identification of the decoded integer with duration;
- a satisfactory endpoint predicate for diagonal-phase-only contact or
  general superposed coin dynamics.

On a superposed input the reversible B comparator produces an entangled
opportunity pointer.  Nothing in this runner selects or actualizes a branch.
The diagonal contact control is intentionally silent because no occupation
`B` changes.  Thus this result does not claim that every physical interaction
produces an endpoint.

## Discipline and novelty boundary

The new content is the bounded local-B endpoint predicate, reversible packet,
and exact projection equations.  The predecessor arithmetic, K16 carry
convention, admission token types, and causal-order refusal rule are landed
Cycle-610/612 content and are not presented as new.

No count word, packet ordinal, or rotor value is called time.  No packet is
called a Record.  No occurrence, permanence, empirical calibration, Born
meaning, or state preparation is inferred.  No no-go, minimum-content, or
axiom-pressure claim is made; diagonal and superposed endpoints remain live
constructive work.

## Reproduction

```bash
PYTHONPATH=scripts python3 -u \
  scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py
```

Expected terminal:

```text
LOCAL_GAUSS_ENDPOINT_PACKET_INTERTWINER_CLOSED_OCCURRENCE_RECORD_UNIT_PREPARATION_OPEN
```

The retained canonical replay passed 6 checks, failed 0, used 94.390625 MB
peak RSS, and took 1.1022878328803927 seconds.  Certificate SHA-256:
`357091195c097d1c7cf25465b5243a05b456990f7f0f1509eb5469dd9466022b`.
