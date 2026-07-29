# The enforced dual-rail lock — write-once derived as a refusal law — Cycle 745

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py`](../scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py)
- [`frontier_cycle745_lock_independent_check_2026_07_28.py`](../scripts/frontier_cycle745_lock_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The W5 junction probe named the wall: the archive→Record hand-off needs
a **derived** write-once mechanism, and permanence may never be
premised. The campaign's route portfolio ranked the native idiom first
— a lock built from enforcement, so that permanence at the mechanism
level *is* a refusal law. This cycle builds it at the smallest honest
scope, one binary M2 Record cell with seven semantic rails:

- **the write is the lock**: the 8-gate reversible WRITE word writes
  the payload bit and sets the lock rail *in the same word* — first-
  write locking is not a separate step that could be omitted;
- **overwrites are refused, not forbidden by fiat**: the write word is
  gated on the lock rail (the enforcement-cascade lift pattern), so a
  write applied to a locked cell completes as a clean REFUSED
  transition — registers return, the locked content is untouched, a
  refusal latch records the event;
- **exhaustive at the one-cell scope**: all 128 seven-rail states are
  reversible with distinct outputs; first-write 2/2 accepted;
  second-write 4/4 and third-write 8/8 refused with locked bytes
  exactly invariant; all 8 single-gate deletions of the lock cascade
  are detected;
- **the inductive closure**: base — the post-first-write state
  satisfies the lock invariant; step — every word of the declared
  alphabet (`IDLE, READ, WRITE[0], WRITE[1]`) preserves it; hence
  **every finite word over the alphabet preserves locked content** —
  machine-checked, both parts.

## The honest ceiling (stated plainly)

What is derived is **mechanism-level write-once under the declared
alphabet**. `record_permanence_claimed` remains **false** at the axiom
level: out-of-alphabet operations are out of scope, and no statement
about the Record axiom's own permanence semantics is made or needed
here. The next construction is multi-cell archive integration —
composing this lock with the Cycle-741 archive and the Cycle-742
readout feed, so the proto-Record the last campaign built becomes a
locked one.

## Supplied / derived / open

### Supplied

- the rail encoding, initial clean sector, macro domain (the declared
  alphabet), the C_source firewall, and readout conventions — the
  route portfolio's supplied list, verbatim.

### Derived

- first-write locking (same-word); the clean-refusal law; exhaustive
  control coverage; locked-content invariance; the inductive closure
  over the alphabet.

### Open

- multi-cell integration with the 741/742 machinery (the named next
  cycle); out-of-alphabet scope; the W5 junction's full closure;
  everything inherited at original scopes.

## Negative-claim discipline

No negative claim ships. The alphabet bound is a scope statement, not
an impossibility claim about richer operation sets.

## Verdict

Write-once is now a theorem about a physical word, not a property
assumed of a substrate: the lock is set by writing, the refusal is
enforced by the same machinery that enforces charge and count, and the
induction closes the alphabet. If this composes across the archive,
the W5 junction's mechanism exists — and if the composition fails, the
failure will name what the Record axiom must grant. Either way the
axiom conversation advances. Independent audit still required.
