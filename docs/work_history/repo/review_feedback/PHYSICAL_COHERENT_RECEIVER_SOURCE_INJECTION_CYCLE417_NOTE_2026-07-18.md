# Physical coherent receiver-source injection — Cycle 417

Date: 2026-07-18

Authority: none

Audit: unset

## Result and exact boundary

Cycle 417 compiles one bounded coherent near-side replacement for the Cycle-416 expectation-to-source seam. Two physical M2 receiver-source ports start blank. One is labeled retarded and one static. Two fixed local CNOT gates coherently latch the Cycle-416 mediator M2 into both ports. **No mediator expectation is queried** to perform this update and there is no host branch query.

On the declared source-port code,

```text
E_417 G_417 = G_physical,417 E_417,
```

and reversing the two layers gives the exact inverse. The Cycle-416 scalar expectation remains useful only as a post-update diagnostic occupation weight; it no longer controls source-port preparation.

This is the **source-port seam only**. The Cycle-213/216 real field arrays, cubic point profile, signs, couplings, retarded propagation, and static solve are not encoded in M2 here. Thus the result does not claim a complete physical receiver compiler.

## Five-M2 local code

The common code contains the inherited strict-response, source-excitation, and mediator M2s plus two new blank receiver-source M2s. They occupy one bounded connected neighborhood. The fixed source action is

```text
retarded_source ^= mediator
static_source   ^= mediator.
```

The common represented installation is therefore 4,859 M2, two more than Cycle 416. Both gates have support two. Proper-cubic rotation preserves their adjacency in all 24 frames; the five labels use the explicitly supplied scalar frame representation.

On every coherent branch after the Cycle-416 balance gate:

```text
mediator = 0  ->  retarded_source = static_source = 0
mediator = 1  ->  retarded_source = static_source = 1.
```

The receiver-port occupations are coherently correlated copies of one cause, **not independent confirmations**.
This is computational-basis fanout producing GHZ-type correlation, not
cloning an arbitrary mediator state. The mediator excitation remains present;
the two port occupations are control labels, not a split or transfer of a
conserved excitation, resource, energy, or source quantum.

Exact inverse cleanup applies to this source-port seam before downstream
receiver actions alter the ports, or after those actions are coherently
uncomputed. Reapplying the fanout without such a protocol toggles the occupied
ports; Cycle 417 does not derive recurrent receiver consumption.

## Controls

- Basis transfer: both source-port weights and their joint weight equal `sin^2(theta) = 0.12589921612871371`; inverse residual is zero.
- L5 and blind held L6: for both inherited source routes and both origins, mediator, retarded-port, static-port, and joint weights equal the frozen strict-response weight times the Cycle-416 transfer factor. All inverse residuals are zero.
- Deletion: deleting either CNOT leaves exactly that source port blank while the other port retains the mediator-correlated transfer.
- All 24 proper-cubic frames preserve the two nearest-neighbor gate supports
  under the supplied scalar identity representation, with zero coordinate or
  locality failures; no tensor transformation law is derived.
- Bridge keys, prior Record hashes, Cycle-219 mass, and the Cycle-230 contact
  fixture are structural/inherited spectators under the new port action.
- Binary and one-excitation domains reject malformed states.

## Supplied, derived, and open

Supplied: the Cycle-416 strict-response balance, scalar mediator meaning, and register preparation; two blank receiver-source M2 ports; their retarded/static interpretation; the fixed two-CNOT schedule; and the scalar proper-cubic representation.

Derived: coherent branchwise injection into both source ports without expectation feedback; exact inverse cleanup; held-size transfer; deletion visibility; and all-frame locality.

Open: reversible downstream port consumption and cleanup; the full Cycle-213/
216 field-array encoding and propagation in physical M2; the cubic point-
profile and sign representation; coupling and calibration; autonomous
recurrence; recoil; resource accounting; source selection; actual Record
formation; physical time; metric dynamics; and gravity.

The copied port coordinate is not physical energy, stress, or a selected source. It is not a rate, probability, or Born weight. No actual Record is formed. This note makes no negative, minimum-content, shared-obstruction, or axiom-pressure claim.
