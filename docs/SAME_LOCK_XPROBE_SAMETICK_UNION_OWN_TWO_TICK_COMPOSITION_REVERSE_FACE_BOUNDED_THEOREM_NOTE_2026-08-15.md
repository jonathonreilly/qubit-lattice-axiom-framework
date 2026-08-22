---
claim_id: same_lock_xprobe_sametick_union_own_two_tick_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse/face from S⁺ at t versus t+1 on the four #7181 x-probes, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/same_lock_xprobe_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py
---

# Two-Tick Composition Of Same-Tick Union Own Reverse And Face On Four Nssame X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from `S^+` at each probe's formation tick `t`
versus `t+1`, on the four nssame x-probes in `B_3(0)={n:n·n<=9}`, no
global T. Let `t(q)` be the formation tick of probe `q`. Let `L(q)` be
`q`'s own unique incoming lock; seeds use seed letters. If several
earliest incoming steps exist, `L(q)` is `UNDEFINED`. Let `τ0(q)=t(q)`
and `τ1(q)=t(q)+1`. At cut `τ`, `S^+(q,τ)` is the set of locks of
six-neighbors of `q` that formed at tick `<= τ` and are not `q`, union
`{L(q)}` when `L(q)` is defined and `t(q)<=τ`. Reverse at a cut holds if
and only if some lock in `S^+(A,·)` is the vector opposite of some lock
in `S^+(B,·)`. Face likewise on `C,D`. Empty `S^+` on either side is
`UNDEFINED`; nonempty with no opposite pair fails. Composition HOLD if
and only if the `t+1` reverse/face bits equal the `t` bits (neither side
`UNDEFINED`, or both `UNDEFINED`). Occupancy `n` is not used; the
construction does not use occupancy. This is
not leftover of same-tick union own at each probe's own `t` alone. This
is not leftover of later-tick union own. This is not leftover of own
incoming set `M`. This is not leftover of unique own-incoming letters.
This is not the two-tick lock-count clock. Uniqueness of incoming locks is not required. Uniqueness of the lock set is not required. Displayed,
not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/same_lock_xprobe_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py`](../scripts/same_lock_xprobe_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in
`S^+` at each probe's `t` and at `t+1`. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock-vector letter is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ at t and at t+1 on the four nssame x-probes, with reverse hold, face hold, and composition HOLD because t+1 bits equal t bits; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: same_lock_xprobe_sametick_union_own_two_tick_composition_reverse_face
target_blocker_text: "display reverse and face from S^+ at t versus t+1 on the four nssame x-probes, no global T, and whether those bits compose"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse, face, and composition displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the cuts with own-t leftover, do not identify the cuts with later-tick global T leftover, and do not attach a formation member from already-recorded six-neighbor locks."
conditional_surface_status: "exact on B_3(0) for two-tick composition of S^+ reverse/face on the four nssame x-probes, no global T; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Displayed process

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, and `e_3=(0,0,1)`. The six nearest-neighbor
steps are

```text
NN = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
```

The finite host is the closed Euclidean ball of radius 3 centered at the
origin,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

No larger host is used. The four x-probes are the only sites whose
two-cut union sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

`A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
same-letter locks `L(0)=+e_1` and `L(0,1,0)=+e_1`. This is the same process
as nssame #7060 and nssamxinc #7181 on these x-probes.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Uniqueness is not required. A later parent does not re-form
`q`.

## Named `S^+` at `t` and at `t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There is no global T.

Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}`. Seeds use seed
letters. If several earliest incoming steps exist, `L(q)` is `UNDEFINED`.
At cut `τ`, `S^+(q,τ)` is the set of locks of six-neighbors of `q` that
formed at tick `<= τ` and are not `q`, union `{L(q)}` when `L(q)` is
defined and `t(q)<=τ`. Duplicate locks collapse in the set. The
construction does not require `S^+(q,τ)` to be a singleton. It does not
sum `S^+(q,τ)`. It does not wait for a global later T. It does not use
occupancy `n`.

Reverse at a cut holds if and only if some `a` in `S^+(A,·)` and some `b`
in `S^+(B,·)` have `a+b=(0,0,0)`. Face at a cut holds if and only if some
`c` in `S^+(C,·)` and some `d` in `S^+(D,·)` have `c+d=(0,0,0)`. Empty on
either side of a comparison is `UNDEFINED`; nonempty with no opposite pair
fails.

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`, with neither side `UNDEFINED` or both
sides `UNDEFINED`. Else composition fails. Displayed, not adopted.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero inside `S^+`. They are not an
occupancy-kernel inner product.

This is not leftover of same-tick union own at each probe's own t alone:
that leftover reports `S^+` only at `t` and does not report the `t+1` cut
or composition. This is not leftover of later-tick union own: that leftover
waits for a global later T equal to the max of the four formation ticks.
This is not leftover of own incoming set `M`: that leftover scores earliest
incoming steps, not six-neighbor lock union. This is not leftover of unique
own-incoming letters. This is not the two-tick lock-count clock.

## Theorem 1 — ticks, `S^+` at `τ0` and at `τ1`, and new six-neighbor records

Direct enumeration of the displayed nssame process on `B_3(0)` forms all four
x-probes. The formation ticks and two-cut union sets are:

```text
t(A)=3
t(B)=2
t(C)=4
t(D)=3
S^+(A, τ0) = {+e_1, −e_2, +e_3, −e_3}
S^+(B, τ0) = {+e_1, +e_3}
S^+(C, τ0) = {+e_1, +e_2, +e_3, −e_3}
S^+(D, τ0) = {+e_1, +e_2, +e_3, −e_3}
S^+(A, τ1) = {+e_1, −e_2, +e_3, −e_3}
S^+(B, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}
S^+(C, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}
S^+(D, τ1) = {+e_1, +e_2, +e_3, −e_3}
```

`A` is not a seed. `L(A)` is `UNDEFINED` from three earliest incoming steps
`−e_3`, `+e_3`, and `+e_2`. `L(B)=+e_1`. `L(C)=+e_1`. `L(D)` is
`UNDEFINED` from three earliest incoming steps `−e_2`, `−e_3`, and `+e_3`.
At `τ0` the sets match the #7181 own-`t` display. At `τ1`, `S^+(B)` and
`S^+(C)` enlarge: `S^+(B)` gains `+e_2` and `−e_2`, and `S^+(C)` gains
`−e_2`. `S^+(A)` and `S^+(D)` are unchanged as sets. Mixed remains a set.
Uniqueness is not required.

New records in `B_3(0)` between `τ0` and `τ1` that meet a probe's
six-neighbors are:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

The new neighbor `(2, 0, 0)` of `A` is probe `C`, formed at tick 4 with
incoming `+e_1`, already in `S^+(A,τ0)`. The new neighbors of `B` at tick
3 contribute `+e_2`, `−e_2`, and `−e_3`. The new neighbors of `C` at tick
5 contribute `−e_2`. The new neighbor `(2, 1, 0)` of `D` carries `+e_1`,
already in `S^+(D,τ0)`.

This is not leftover of later-tick union own: that leftover uses global
`T=4`. Here `τ1(C)=5`, and `S^+(C,τ1)` includes `−e_2` while `S^+(C)` at
global `T=4` does not. This is not leftover of same-tick union own at each
probe's own t alone: that leftover does not report `S^+(B,τ1)` or
`S^+(C,τ1)`.

## Theorem 2 — reverse and face at `τ0` and at `τ1`

Reverse holds if and only if some `a` in `S^+(A,·)` and some `b` in
`S^+(B,·)` have `a+b=(0,0,0)`. At `τ0` the sets are
`{+e_1, −e_2, +e_3, −e_3}` and `{+e_1, +e_3}`. The pair
`−e_3+(+e_3)=(0,0,0)` holds. Reverse holds. At `τ1` the enlarged `S^+(B)`
still contains `+e_3`, and `S^+(A)` still contains `−e_3`, so reverse
holds again. Both sides are nonempty and defined, so this is not
`UNDEFINED`.

Reverse at τ0: hold
Reverse at τ1: hold

Face holds if and only if some `c` in `S^+(C,·)` and some `d` in
`S^+(D,·)` have `c+d=(0,0,0)`. At `τ0` the sets are
`{+e_1, +e_2, +e_3, −e_3}` and `{+e_1, +e_2, +e_3, −e_3}`, so
`+e_3+(−e_3)=(0,0,0)`. Face holds. At `τ1` the enlarged `S^+(C)` still
contains `+e_3` and `−e_3`, and `S^+(D)` is unchanged, so face holds
again.

Face at τ0: hold
Face at τ1: hold

Unique own-incoming letters on these x-probes report reverse `UNDEFINED`
and face `UNDEFINED` from mixed `A` and mixed `D`. Own incoming set `M`
reports reverse fail and face fail. Same-tick union own at each probe's
own t alone reports the same `τ0` bits and does not report `τ1`. Later-tick
union own reports hold/hold after a global later T, from a different
`S^+(C)` that lacks `−e_2`. Those are different objects.

## Theorem 3 — composition

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`. Both reverse reports are `hold` and both
face reports are `hold`, so the bits match and neither side is `UNDEFINED`.

Composition: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. The `t+1` reverse/face
bits equal the `t` bits on this process even though `S^+(B)` and `S^+(C)`
enlarge: the holding opposite pairs survive the enlargement. Composition
HOLD is a displayed equality of bits, not an Admissibility rewrite.

This is not leftover of unique own-incoming letters (reverse `UNDEFINED`,
face `UNDEFINED`). This is not leftover of own incoming set `M` (reverse
fail, face fail). This is not leftover of same-tick union own at each
probe's own t alone (no `t+1` cut). This is not leftover of later-tick
union own (global `T=4`). This is not the two-tick lock-count clock.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the union set to be a singleton.
- It does not sum the union set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint same-tick union own at each probe's own t alone.
- It does not reprint later-tick union own.
- It does not reprint own incoming set `M`.
- It does not reprint unique own-incoming lock-vector letters on these
  x-probes.
- It does not reprint the two-tick lock-count clock.
- It does not wait for a global later T.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

Records form.

When present, a record locks exactly one admissible local possibility.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
nssame process, the two-cut union sets, and the reverse/face/composition
predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `3` |
| `S^+` at `τ0` and at `τ1` | Theorem 1 |
| reverse and face at `τ0` and at `τ1` | Theorem 2; `hold` / `hold` |
| composition | Theorem 3; `HOLD` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| leftover of same-tick union own at each probe's own t alone | not this display |
| leftover of later-tick union own | not this display |
| leftover of own incoming set `M` | not this display |
| leftover of unique own-incoming letters | not this display |
| two-tick lock-count clock | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: `S^+` reverse/face at `t` versus `t+1` on the four #7181 x-probes, and whether those bits compose. |
| V2 | Current main has no landed two-tick composition of `S^+` reverse/face on these four nssame x-probes. |
| V3 | The two-cut union sets and the `hold`/`hold`/`HOLD` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads `S^+` at two per-probe cuts and scores equality of reverse/face bits. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint own-`t`
leftover, does not reprint later-tick leftover, does not reprint own
incoming set `M`, does not reprint unique own-incoming letters, does not
reprint the two-tick lock-count clock, and does not use occupancy `n`. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique own-incoming letters | replace mixed `S^+` by `L(q)` | refused; leftover; reverse and face would be `UNDEFINED` while both bits hold |
| own incoming set `M` | score earliest incoming steps | refused; leftover; `M` reverse fail and face fail while `S^+` reverse hold and face hold |
| same-tick union own at each probe's own t alone | report `S^+` only at `t` | refused; leftover; that leftover does not report `S^+(B,τ1)` or composition |
| later-tick union own | wait for global `T=4` | refused; leftover; `S^+(C,τ1)` includes `−e_2` while `S^+(C)` at `T=4` does not |
| two-tick lock-count clock | score a lock-count clock across two ticks | refused; different member; this display scores `S^+`, not a lock-count clock |
| sum of `S^+` | replace each set by its `Z^3` sum | refused; leftover; sum of `S^+(A,τ0)` is `(1,−1,0)` and sum of `S^+(B,τ0)` is `(1,0,1)`; those sums fail reverse while existential opposite holds |
| named-sign lettering | map `±e_i` to `{+,−}` | refused; lost the axis |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required |

### N2 — wall independence

Missing physical adoption, missing Record identification of existential
opposite, and missing formation attachment from already-recorded
six-neighbor locks are distinct open premises. This note claims no complete
wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_1`, perpendicular step
rule, incoming-step lock, `S^+` as same-tick-inclusive six-neighbor locks
union `L(q)` when defined at per-probe `τ0=t` and `τ1=t+1`, existential
opposite, four x-probes with non-seed `A`, and composition as equality of
the two-cut bits are declared. No uniqueness of incoming locks, no occupancy
`n`, no named-sign reduction, no singleton leftover, no sum leftover, no
own-`t`-only leftover, no later-tick leftover, no own-incoming-set leftover,
no unique-letter leftover, no lock-count clock, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold`/`HOLD` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in `S^+` at a probe's `t` and at `t+1` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `S^+` lock sets at two cuts and reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** New six-neighbor records between `t` and `t+1` should flip
reverse or face, so composition should fail; this is leftover of #7181
own-`t` `S^+` because the bits already hold there; this is leftover of
later-tick union own because reverse and face both hold after a later cut;
mixed `A` should make reverse `UNDEFINED`; own incoming set `M` already
answered the two-tick question; unique own-incoming letters already
answered reverse `UNDEFINED`; the two-tick lock-count clock already
answered two-tick composition; named signs should suffice; occupancy `n`
should track the vector; and composition HOLD is tautological.

**Answer:** `S^+(B)` and `S^+(C)` do enlarge at `t+1`, so this is not
own-`t` leftover. The holding opposite pairs survive, so the bits stay
`hold`/`hold` and composition HOLD. Later-tick leftover uses global `T=4`;
`S^+(C,τ1)` at `t(C)+1=5` includes `−e_2` while `S^+(C)` at `T=4` does
not. Mixed remains a set. Own incoming set `M` fails both bits. Unique
own-incoming letters report `UNDEFINED`. The two-tick lock-count clock is
a different member. Named signs lost the axis. Occupancy `n` is not used.
Composition HOLD is the displayed fact that the `t+1` bits equal the `t`
bits on this process; it is not an Admissibility rewrite.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same nssame x-probes
assigned `L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`, `L(D)=UNDEFINED` and
reported reverse `UNDEFINED` with face `UNDEFINED`. Same-tick union own at
each probe's own t reported reverse hold and face hold without a `t+1` cut.
Later-tick union own reported reverse hold and face hold on a larger
`S^+(B)` after global `T=4`, with `S^+(C)` still missing `−e_2`. Own
incoming set `M` on a z-symmetric three-site process reported reverse fail,
face fail, and composition HOLD from frozen `M`. A two-tick lock-count
clock composition scored a different clock. This note is not those
displays: `S^+` is read at `t` and at `t+1`, reverse holds, face holds, and
composition HOLD because those bits are unchanged even though `S^+(B)` and
`S^+(C)` enlarge.

**Gate disposition:** PASS for the two-tick `S^+` reverse/face composition
reports above. FAIL / DO NOT SHIP for “the predicate equals the named
sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the sum of the lock set,” “bits are Admissibility,” “the
letter is occupancy `n`,” “the cuts equal own-`t` leftover,” “the cuts
equal later-tick union own,” “the sets equal own incoming set `M`,”
“reverse is `fail`,” “composition fails,” or “`S^+` is frozen at every
probe from `t` to `t+1`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nssame two-site
perp-step incoming-lock process, reads `S^+` at each probe's `t` and at
`t+1`, lists new records in `B_3(0)` between those cuts that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that `S^+(B)` and
`S^+(C)` enlarge at `t+1`, that later-tick leftover at global `T=4` does
not match `S^+(C,τ1)`, that own incoming set `M` fails both bits, that
unique-letter reverse is `UNDEFINED`, that mixed remains a set, that the
construction does not sum, that occupancy `n` is not used, that a formation
member from already-recorded six-neighbor locks is not attached, and that
the display is not the two-tick lock-count clock. No runner cache is
written.
