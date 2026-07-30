# Abstract seven-bit packetized lock protocol — Cycle 745

Date: 2026-07-29

Authority: none

Audit: unset

Status: conditional / support

Claim type: bounded_theorem

Runners:

- [`frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py`](../scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py)
- [`frontier_cycle745_lock_independent_check_2026_07_28.py`](../scripts/frontier_cycle745_lock_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

This package proves a finite result about a supplied event protocol on seven
binary rails

```text
(D, V, U, L, Q_in, Q_accept, Q_refuse) in {0,1}^7.
```

The literal eight-gate `WRITE` word is a permutation of all 128 rail states.
On a clean event packet it accepts either offered bit, copies it to `D`, and
changes the persistent lock pair from `UNLOCKED=(1,0)` to `LOCKED=(0,1)` in
that same word. On each later packetized write, the word leaves `D` and the
lock pair unchanged and returns the event tag `REFUSED`.

The finite-sequence statement is about reduced event maps, not literal
composition of the seven-bit permutations. For persistent storage
`x=(D,U,L)`, the supplied injection maps prepare fresh event rails:

```text
E_IDLE(x)     = (D,0,U,L,0,0,0)
E_READ(x)     = (D,0,U,L,0,0,0)
E_WRITE[b](x) = (D,b,U,L,1,0,0).
```

After the selected literal word acts, the supplied projection
`P(D,V,U,L,Q_in,Q_accept,Q_refuse)=(D,U,L)` discards the four event rails.
The macro maps are therefore `P o M o E_M`. The two post-first-write images
establish the base, and all eight combinations of locked payload
`D in {0,1}` and macro
`M in {IDLE,READ,WRITE[0],WRITE[1]}` establish the step. Ordinary induction
then proves that every finite sequence of these reduced maps preserves the
locked payload.

## Supplied operational inputs

The result is conditional on all of the following:

- the binary diagonal convention `b -> diag(b,0)` inside each named
  `M_2(C)` factor;
- the seven rail roles and order, the displayed coordinate labels, the
  one-hot meanings `UNLOCKED=(1,0)` and `LOCKED=(0,1)`, initial `D=0`, and
  the choices of `D` as stored content and `V` as offered data;
- the literal controlled-`X` and controlled-`SWAP` semantics, control
  polarities, targets, and gate order;
- the event injection and projection above, including fresh
  `Q_accept=Q_refuse=0` on every event, event-rail discard between events,
  and an external scheduler selecting the macro;
- the exact four-symbol macro alphabet and the accept/refuse tag
  interpretation; and
- the `READ` convention, whose copied `V` value is event-local before the
  projection discards it.

The coordinate assignment is only a supplied labeling in this package. It is
not evidence that the multi-controlled gates are nearest-neighbor operations.
No `C_source`, scalar-readout, Record-activation, or physical-observable rule
is used by the finite proof.

## Derived finite result

- all 128 inputs of the literal `WRITE` word have distinct outputs, every
  literal gate is an involution, and reversing the gate order restores every
  input;
- the two clean first-write packets are accepted and set the lock in the same
  literal word;
- all four second-write and all eight third-write packet cases are refused
  with the stored bit and lock pair unchanged;
- the two computed base cases and eight exhaustive reduced-map step cases
  close the finite-sequence induction;
- the independent checker finds no alteration in 680 additional compositions
  of positive lengths 1 through 4; and
- each of the eight single-gate deletions is detected by the enumerated clean,
  locked, and dirty packet tests.

The last item is exactly an 8/8 whole-gate deletion result. It is not a claim
of exhaustive control-polarity, target, ordering, duplication, or hidden-gate
coverage.

## Framework and physical boundary

The [minimal framework axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the
`Z^3` setting, one-site `M_2(C)` possibility domain, local Admissibility, and
Record at their stated scopes. They do not select the binary rail roles,
provide the event protocol, compile the multi-controlled gates, or identify
`LOCKED` with formation or persistence of a Record.

For comparison, the current
[Cycle-730 local charge-row construction](CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md)
reports a literal routed nearest-neighbor compilation, while the
[Cycle-731 counter/refusal fixture](TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md)
explicitly leaves physical transport and nearest-neighbor compilation outside
its scope. The current
[Cycle-719 controller boundary](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
also keeps the physical bridge from reversible packets to the axiomatically
named permanent Record open. Those notes are comparison and scope authorities;
their results are not premises of the finite truth-table proof here.

This package does not supply a nearest-neighbor decomposition, routing and
returned work, a translation-uniform or proper-cubic-covariant rule,
admissibility or dynamics, a closed-system ancilla/garbage lifecycle, Record
formation, physical persistence, or a readout bridge. In particular, applying
the literal `WRITE` word directly to an accepted seven-bit output without the
fresh-event injection can change the lock pair; the closed-system composition
claim is not made.

The package asserts no impossibility, no residual-wall independence, no
axiom pressure, and no conclusion about operations or mechanisms outside the
declared event protocol.

## Verdict

The durable result is a conditional finite-state construction: a reversible
eight-gate `WRITE` permutation plus a packetized persistent-state lock
invariant under the supplied injection/projection convention. It is not a
framework-native physical mechanism or Record-production theorem. Independent
audit is still required.
