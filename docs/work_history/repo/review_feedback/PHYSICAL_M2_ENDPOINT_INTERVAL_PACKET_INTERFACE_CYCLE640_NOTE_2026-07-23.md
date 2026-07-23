# Physical-M2 endpoint / interval packet interface — Cycle 640

Classification: **positive bounded physical candidate-packet interface; full same-species A2 stream/tick composition and actuality remain conditional/open**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough bar met: **false**

## Result up front

Cycle 640 constructs the physical-M2-side interface requested verbatim by the
immutable Cycle610-612 acceptance contract from PR #5557.

First, a two-path contact echo uses one local contact-eigenflag M2 and one
pointer M2.  `H`, controlled contact phase, `H` induces pointer-one effect
`diag(0,sin^2(g/2))`.  At `g=0.37` its contact-flag-one weight is
`0.033836327196983`.  Deleting contact
sets the complete pointer-one effect to zero with residual
`5.005e-34`.  The induced effect
matches the Cycle634 positive-root binary instrument at residual
`2.082e-17`.  This pointer is
a coherent candidate sector, not an occurrence.  Contact deletion kills only
this candidate pointer; it does not establish an actual endpoint.

Second, a reversible endpoint transducer computes

```text
contact_pointer AND crossing AND channel_certified
AND convention_certified AND NOT claimed.
```

It exhausts all `256` basis inputs with zero failures,
returns all `4` work M2 blank, latches
the crossing as claimed, and refuses a second certificate from the same
crossing cell.  Every certificate carries three explicit ports: crossing
orientation, channel sign (`plus/minus`), and convention (`T1/T2`).  The logic
is line-agnostic: no spectral root is hardwired, so a future lawful two-line
domain changes the port values/certificates rather than this hardware.

Third, a local reversible packet consumes one one-use endpoint token only when
the adjacent source cell carries the head and all four controls are one:
`binder`, `actuality`, `admissibility`, and `law_domain`.  It copies the packet
identity, copies predecessor identity from the local head cell, increments the
four-bit rotor once, writes carry exactly on `K15 -> K0`, copies the three
endpoint ports, consumes the token, and moves the head to the new cell.  All
runtime gates have support at most three M2.  The target blank-cell code is a
set of `23` local support-one
constraints; blank genesis is supplied.

| size | role | admitted cells | Delta(A,B) | Delta(B,C) | Delta(A,C) | carries/first24 | gaps undefined |
|---|---|---:|---:|---:|---:|---:|---:|
| L3 | construction | 27 | 9 | 12 | 21 | 2 | yes |
| L6 | train | 30 | 9 | 12 | 21 | 2 | yes |
| L7 | held-out-no-refit | 31 | 9 | 12 | 21 | 2 | yes |

This exactly reproduces Cycle610's `9 + 12 = 21` and two-carry acceptance row
at construction L3, train L6, and held-out L7 without refit.  Reverse endpoint
order returns `-9`.  Missing predecessor, deleted binder, wrong rotor, or
deleted carry returns **undefined**, never zero.  The decoder reads retained
cell state only; no update ordinal enters it.

## Deletion, inverse, malformed, and exactly-once controls

The interval unit exhausts `4096` declared basis
cases with `0` failures, including every rotor and
every combination of the four admission ports.  Applying the reverse gate list
restores the source, packet, ports, head, and blank target exactly.  After a
successful append the packet token is zero, so presenting it to another fresh
target appends nothing.

| deleted gate | output Hamming signal | signal after full inverse |
|---|---:|---:|
| `u_predecessor_copy_0` | 1 | 1 |
| `u_rotor_increment_bit0` | 1 | 1 |
| `u_carry_set` | 1 | 1 |
| `u_binder_copy` | 1 | 1 |
| `u_orientation_copy` | 1 | 1 |
| `u_valid_set` | 4 | 1 |
| `u_admit_and_uncompute_0` | 1 | 13 |
| `u_token_consume` | 1 | 13 |
| `u_head_move` | 2 | 14 |

Deleting binder, actuality, admissibility, or law-domain blocks admission.
Every single dirty target-cell M2 is refused by the declared local blank code.
The endpoint runner separately deletes contact, endpoint conjunction,
certificate, metadata, token, uncompute, and claimed-latch gates; every
deletion is output- and inverse-visible.

## Proper-cubic and resource controls

All `24` proper-cubic frames and
`576` ordered products pass at L3/L6/L7.
The spatial apparatus ray is transported.  Crossing orientation, channel sign,
and T1/T2 convention are spatial scalars.  There is no runtime frame selector.
The reference ray and local bank direction are supplied.

The endpoint neighborhood uses `18`
M2 including the contact eigenflag, echo/certificate ports, and work.  One
retained interval cell uses `23` M2; the complete
two-cell update neighborhood including packet, four explicit ports, and work
uses `72` M2.
These are constants on the declared six-bit-identity domain.  The schedule is
a supplied compiler serialization, not a physical time law or autonomous bank
genesis.

## Exact shore and composition boundary

Cycle632 supplies an exact fixed-sector physical E/G grammar but explicitly
does not compile same-species multiparticle A2.  Cycle634 supplies the bounded
candidate-pointer instrument but explicitly supplies no occurrence or Record.
Cycle639's committed local `64 x 15` wedge2/A2 host is not
consumed as a premise here; its seam-complete stream remains open.  The
unlanded finite-L9 positive A2 line near `+0.30` is not used.

Therefore Cycle640 composes exactly with the Cycle610 **packet semantics** but
does not claim the full Cycle610 detector word has been run over a committed
physical same-species A2 stream.

## Unchanged Cycle610-612 harness rerun

The four PR #5557 source runners were executed unchanged in an isolated
detached worktree at `a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318`.  They reproduced their
preregistered dispositions exactly: Cycle610 `33`
PASS / `3` FAIL (exit 1), Cycle611
`9` / `2`
(exit 1), Cycle612 main `6` /
`1` (exit 1), and the Cycle612 minus
addendum `5` /
`0` (exit 0).  Those expected
FAIL rows remain FAIL; none is repaired or reclassified.  This is a contract
reproduction, not an end-to-end composition with the Cycle640 packet.

## Supplied / derived / open

Supplied: immutable shores; local contact eigenflag and phase; crossing,
orientation, channel/sign/certification, T1/T2/certification; six-bit identity;
claimed latch; one-use token; root `K14` head; blank bank; local bank direction
and serialized schedule; binder, actuality, admissibility, and law-domain.

Derived: exact two-M2 contact echo and contact-off kill; reversible bounded
endpoint predicate; reversible exactly-once predecessor/K16/carry packet;
local head movement; explicit-port refusal; inverse/deletion/malformed and
undefined-gap controls; exact Cycle610 interval-row equality; all24/all576.

Open: committed seam-complete physical same-species A2 stream; physical CT-1
crossing/channel/convention certificates; laws supplying actuality,
admissibility, and law-domain; autonomous identity/bank/head/schedule/reset and
renewal; permanence, empirical duration unit, unbounded causal order,
continuum/Lorentz/proper-time interpretation.

## N1-N8 no-go discipline

N1 normalizes six attempted families and lists the target-equivalent
seam-complete A2 detector composition separately as open and not counted as a
failure.  N2 retains four directional walls and all 12 directed pairs.  N3
lists every flag, seed, selector, schedule, bank, port, and scope boundary.  N4
has seven exact same-scope rows and one dropped Cycle632 scope mismatch.  N5
has six complete five-resolution rows.  N6 has six structured partial-closure
paths.  N7 gives the actionable Cycle639-stream plus physical crossing-comparator
steelman.  N8 has six row-wise echoes.  Status: **PASS** for scoped discipline.

Broad no-go: **withheld**.  Shared route-independent obstruction: **not
established**.  Minimum content: **not claimed**.  Axiom pressure: **none**.

## Six-wall ledger

| wall | Cycle640 movement | residual |
|---|---|---|
| `C_ref` | one-use endpoint identity, predecessor, and local head provenance are retained | identity/root/bank/reference-ray genesis and renewal supplied |
| `C_num` | exact K16 carry, `9+12=21`, inverse/deletion/malformed/held rows | packet counts are not time; they have no empirical unit |
| `C_wrap` | rotor/carry and lineage gaps are locally explicit | cells are reversible candidates, not Records or histories; permanence absent |
| `C_int` | contact echo makes candidate pointer matter-caused and deletion kills exactly | committed seam-complete A2 stream and physical CT-1 crossing detector open |
| `C_local` | bounded support <=3, constant packet neighborhood, all24/all576 | schedule/bank/head genesis and infinite deployment open |
| `C_source` | pointer/work/bank/port resources are fully counted | actuality/admissibility/law-domain and resource renewal supplied; no gravity/source meaning |

## Disposition

**PASS** for the bounded coherent contact candidate, duplicate-safe endpoint,
reversible exactly-once predecessor/interval packet, explicit admission ports,
and exact Cycle610 packet-semantic adapter.

**DO NOT CLAIM** a realized event, Record, history, time/rate/proper-time law,
full physical Cycle610 clock, seam-complete same-species A2 E/G, autonomous
bank/schedule/renewal, shared obstruction, minimum content, or axiom pressure.

Strongest honest terminal: a literal bounded physical-M2 candidate-packet
interface satisfying the Cycle612 endpoint/interval clauses, ready to accept a
future certified CT-1 crossing bit without hardware redesign.
