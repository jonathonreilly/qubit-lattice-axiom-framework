---
claim_id: opposite_lock_zprobe_own_lock_in_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite in the union of strictly-earlier 6-NN locks with the probe's own incoming lock on the four nsopp z-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_zprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py
---

# Own-Lock-In Existential Opposite Reverse And Face On Four Opposite-Lock Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite in the union of
strictly-earlier six-neighbor locks with the probe's own incoming lock on
the four nsopp z-probes in `B_3(0)`. Let `t(q)` be the formation tick of
probe `q`. Let `L(q)` be `q`'s own unique incoming lock; seeds use seed
letters. If several earliest incoming steps exist, `L(q)` is `UNDEFINED`.
At that tick, `S^+(q)` is the set of locks of six-neighbors of `q` that
formed at tick `< t(q)` (strictly earlier), union `{L(q)}` when `L(q)` is
defined. Reverse holds if and only if some lock in `S^+(A)` is the vector
opposite of some lock in `S^+(B)`. Face holds if and only if some lock in
`S^+(C)` is the vector opposite of some lock in `S^+(D)`. Empty `S^+` on
either side of a comparison is `UNDEFINED`; nonempty with no opposite pair
fails. Occupancy `n` is not used. This is not named-sign lettering. This is
not a unique lock-vector leftover and not a sum leftover. This is the cubic
frame of the y-probe own-lock-in readout on the same opposite-lock seed, not
leftover of later-tick seed-transfer. Reverse HOLD does not use `L(A)`:
reverse fails with and without `L(A)` in `S^+(A)`. This is not leftover of
formation-tick existential opposite that excludes `q`: that display uses
different sets `{+e_1}`, `{+e_3}`, `{+e_3}`, `{+e_3}` even though both
reports are reverse fail and face fail. This is not leftover of the unique
own-incoming lock-vector letters on these z-probes: that readout reports
reverse fail with face `UNDEFINED` at mixed `C`. Uniqueness of incoming
locks is not required. Uniqueness of the lock set is not required.
Displayed, not adopted. This note does not write existential opposite into
Admissibility and does not attach a formation member from already-recorded
six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_zprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py`](../scripts/opposite_lock_zprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
own-lock-in union sets. Named signs `{+,−}` are a coarser readout and are
not used. A singleton unique lock-vector letter is a different readout and
is not used. A `Z^3` sum of those locks is a different readout and is not
used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ as the union of strictly-earlier six-neighbor locks with L(q) when defined, on the four nsopp z-probes, with reverse fail and face fail from existential opposite; reverse HOLD does not use L(A); uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_zprobe_own_lock_in_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from existential opposite in the union of strictly-earlier 6-NN locks with the probe's own incoming lock on the four nsopp z-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with formation-tick leftover that excludes q, do not identify the sets with unique own-incoming leftover, do not identify the readout with the y-probe own-lock-in leftover, and do not wait for later-tick seed-transfer."
conditional_surface_status: "exact on B_3(0) for existential opposite of own-lock-in union sets on the four nsopp z-probes; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose
own-lock-in union sets are scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`,
`C=(0,2,0)`, `D=(1,1,0)`. `A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`.

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

## Named existential opposite from own-lock-in union

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}`. Seeds
use seed letters. If several earliest incoming steps exist, `L(q)` is
`UNDEFINED`. At the own formation tick of each probe `q`, let `S^+(q)` be
the set of locks of six-neighbors of `q` that formed at tick `< t(q)`
(strictly earlier), union `{L(q)}` when `L(q)` is defined. Same-tick partners
are not already recorded as neighbors. The probe itself is not a neighbor of
itself. This display does not wait for a global later T. This display does
not use occupancy `n`. Duplicate locks at two neighbors collapse in the set.
The construction does not require `S^+(q)` to be a singleton. It does not
sum `S^+(q)`. It is not a unique lock-vector leftover and not a sum leftover.
It is not leftover of formation-tick existential opposite that excludes `q`.
It is not leftover of unique own-incoming lock-vector letters on these
z-probes. It is not leftover of the y-probe own-lock-in readout. It is not
leftover of later-tick seed-transfer.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S^+(A) and some b in S^+(B) with a+b=(0,0,0)
face     <=>  some c in S^+(C) and some d in S^+(D) with c+d=(0,0,0)
```

If `S^+(A)` or `S^+(B)` is empty, reverse is `UNDEFINED`. Else reverse fails
if no such pair exists. If `S^+(C)` or `S^+(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — formation ticks, own incoming locks, and S^+ at each z-probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four z-probes. The formation ticks are `t(A)=1`, `t(B)=2`, `t(C)=4`,
`t(D)=2`. `A` is not a seed. Those ticks locate the already-recorded
six-neighbor set. They are not occupancy kernels and are not a global later
T.

Own incoming locks and own-lock-in union sets at each probe's own formation
tick are:

```text
A: incoming +e_3; +e_1 at (0, 0, 0);
   t(A)=1;  L(A) = +e_3;  S^+(A) = {+e_1, +e_3}
B: incoming +e_1; +e_3 at (0, 1, 1);
   t(B)=2;  L(B) = +e_1;  S^+(B) = {+e_1, +e_3}
C: incoming −e_1, +e_2, +e_1; +e_3 at (1, 0, 2), +e_3 at (-1, 0, 2),
   +e_3 at (0, -1, 2), +e_3 at (0, 0, 1);
   t(C)=4;  L(C) = UNDEFINED;  S^+(C) = {+e_3}
D: incoming +e_1; +e_3 at (0, 0, 1);
   t(D)=2;  L(D) = +e_1;  S^+(D) = {+e_1, +e_3}
```

`A` forms at tick 1 from the origin by the incoming step `+e_3`. Its
already-recorded neighbor is the origin locking `+e_1`. The same-tick partner
`(0,1,1)` is not already-recorded. `L(A)` is the unique incoming `+e_3`, so
`S^+(A)={+e_1, +e_3}`. `B`'s already-recorded neighbor locks `+e_3`, and
`L(B)=+e_1`, so `S^+(B)={+e_1, +e_3}`. `C`'s already-recorded neighbors all
lock `+e_3`, and `L(C)` is `UNDEFINED` from three earliest incoming steps, so
`S^+(C)={+e_3}`. `D` forms at tick 2; its already-recorded neighbor is `A`
locking `+e_3`, and `L(D)=+e_1`, so `S^+(D)={+e_1, +e_3}`. Same-tick `B` is
not in `S^+(D)`.

Incoming locks exist and need not be unique (`C` has three earliest incoming
steps `−e_1`, `+e_2`, and `+e_1`). That non-uniqueness leaves `L(C)`
`UNDEFINED` and does not empty `S^+(C)`. Uniqueness is not required.

Reverse HOLD does not use L(A). The strictly-earlier neighbor sets are
`S(A)={+e_1}` and `S(B)={+e_3}`; that neighbor-neighbor reverse already
fails. Union with `L(A)=+e_3` yields `S^+(A)={+e_1, +e_3}` against
`S^+(B)={+e_1, +e_3}`. No own-neighbor pair `L(A)` against `S(B)`, no
own-own pair `L(A)` against `L(B)`, and no neighbor-neighbor pair is
opposite. Including `L(A)` does not create reverse HOLD. This does not use
`L(A)` to hold reverse.

The unique own-incoming letters on these z-probes are `+e_3`, `+e_1`,
`UNDEFINED`, `+e_1`. Those are different objects: `S^+(A)` is not `{+e_3}`,
and `S^+(C)` is nonempty. Formation-tick existential opposite that excludes
`q` reports `{+e_1}`, `{+e_3}`, `{+e_3}`, `{+e_3}` at `A,B,C,D`, a different
set at `A`, `B`, and `D`. Later-tick existential opposite on these same
z-probes reports `{+e_1, −e_1, +e_2, −e_2, +e_3}` at `A` after waiting for a
global later T. The y-probe own-lock-in readout on this same seed reports
`{−e_1}`, `{+e_1, +e_3}`, `{−e_1, +e_2}`, `{+e_1, −e_1}` with seed `A`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty: `S^+(A)={+e_1, +e_3}`
and `S^+(B)={+e_1, +e_3}`. Every pair sums to `(2,0,0)`, `(1,0,1)`, or
`(0,0,2)`. No pair is opposite. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Reverse HOLD does not use `L(A)`.
This is not leftover of formation-tick existential opposite that excludes
`q`: that leftover uses a different set `{+e_1}` at `A` and also fails
reverse. Unique lock-vector lettering of the union sets would report reverse
`UNDEFINED` because `A` and `B` mix. A sum leftover of the same lists would
replace `S^+(A)` by `(1,0,1)` and `S^+(B)` by `(1,0,1)` and would also fail
reverse, while mixing remains a set here. Unique own-incoming letters on
these z-probes also report reverse fail from `L(A)=+e_3` and `L(B)=+e_1`;
that leftover is a different object because its face report at mixed `C` is
`UNDEFINED`. The y-probe own-lock-in leftover on this seed reports reverse
hold from seed letter `−e_1` at y-probe `A`. Later-tick leftover on these
z-probes reports reverse hold after a global later T. Reverse fails because
no pair from `{+e_1, +e_3}` and `{+e_1, +e_3}` is opposite.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S^+(C)={+e_3}` and
`S^+(D)={+e_1, +e_3}`. The pairs are `+e_3+(+e_1)=(1,0,1)` and
`+e_3+(+e_3)=(0,0,2)`. No pair is opposite. Face fails.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.

This is not `hold` and not `UNDEFINED`. Unique own-incoming letters on these
same z-probes assign `L(C)=UNDEFINED` from three earliest incoming steps and
report face `UNDEFINED`. Unique lock-vector lettering of the union sets
would report face `UNDEFINED` because `D` mixes. A sum leftover would
replace `S^+(C)` by `+e_3` and `S^+(D)` by `(1,0,1)` and would also fail
face, while mixing remains a set here. Named-sign lettering lost the axis in
all-plus `{+}` at `C` and `D`. Formation-tick leftover that excludes `q`
reports face fail from `{+e_3}` against `{+e_3}`, a different set at `D`.
The y-probe own-lock-in leftover reports face hold. Later-tick leftover
reports face hold. Face fails from `{+e_3}` against `{+e_1, +e_3}`; it does
not wait for a unique own incoming lock at `C`.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own-lock-in union set to be a singleton.
- It does not sum the own-lock-in union set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  z-probes.
- It does not reprint formation-tick existential opposite that excludes `q`.
- It does not wait for a global later T.
- It does not reprint the y-probe own-lock-in leftover.
- It does not reprint formation-time already-recorded lock sets on nnseed
  x-probes.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock process, the own-lock-in union sets, and the existential-opposite
reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `1`, `2`, `4`, `2` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `+e_3`, `+e_1`, `UNDEFINED`, `+e_1` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1, +e_3}`, `{+e_1, +e_3}`, `{+e_3}`, `{+e_1, +e_3}` |
| reverse HOLD uses `L(A)` | Theorem 1; no |
| reverse and face | Theorems 2–3; `fail` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these z-probes | not this display |
| leftover of formation-tick existential opposite that excludes `q` | not this display |
| leftover of later-tick existential opposite on these z-probes | not this display |
| leftover of the y-probe own-lock-in readout | not this display |
| leftover of nnseed x-probe formation-time existential opposite | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite in the union of strictly-earlier 6-NN locks with the probe's own incoming lock on the four nsopp z-probes, reverse/face or `UNDEFINED`, and whether reverse HOLD uses `L(A)`. |
| V2 | Current main has no landed own-lock-in existential-opposite reverse/face report on these four nsopp z-probes. |
| V3 | Own-lock-in union sets and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the union of strictly-earlier six-neighbor lock vectors with `L(q)` when defined and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint formation-tick leftover that excludes
`q`, does not reprint the y-probe own-lock-in leftover, does not wait for
later-tick seed-transfer, and does not use occupancy `n`. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while the mixed union sets are nonempty and both bits fail |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is `(1,0,1)` and sum of `S^+(B)` is `(1,0,1)`, a different object even though reverse also fails |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; all-plus `{+}` at `A` and `B` would hide that reverse fail is an axis statement |
| unique own-incoming lock-vector leftover on these z-probes | reuse `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`, `L(D)=+e_1` | refused; different object; that leftover reports reverse fail and face `UNDEFINED` while own-lock-in reverse fails and face fails |
| leftover of formation-tick existential opposite that excludes `q` | reuse `{+e_1}`, `{+e_3}`, `{+e_3}`, `{+e_3}` with reverse fail and face fail | refused; different set; `S^+(A)={+e_1, +e_3}` includes `L(A)` |
| leftover of later-tick existential opposite | reuse global later T and reverse hold | refused; different set; this display does not wait for a global later T |
| leftover of the y-probe own-lock-in readout | reuse seed `A=(0,1,0)` and reverse hold | refused; different frame; cubic frame here is z-probes, not y-probes |
| leftover of nnseed x-probe formation-time existential opposite | reuse seed `+e_1/+e_2` and x-probes | refused; different process and different frame |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `C` are kept and `L(C)` is `UNDEFINED` |
| claim reverse HOLD uses `L(A)` | treat including `L(A)` as the y-probe HOLD mechanism | refused; reverse HOLD does not use `L(A)`; reverse fails with and without `L(A)` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, formation-tick lock set of six-neighbors formed
strictly earlier than each probe's own `t`, union with `L(q)` when defined,
existential opposite, four z-probes with non-seed `A`, and reverse/face as
existence of a pair that sums to zero are declared. No uniqueness of incoming
locks, no occupancy `n`, no named-sign reduction, no singleton leftover, no
sum leftover, no unique own-incoming leftover, no formation-tick exclude-`q`
leftover, no later-tick leftover, no y-probe leftover, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own-lock-in union set | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** The union is leftover of unique own-incoming letters plus
formation-tick neighbor locks, mixed neighbor locks should make reverse and
face `UNDEFINED`, the sets should be replaced by their sums, unique
own-incoming letters already answered reverse fail with face `UNDEFINED`,
formation-tick existential opposite already answered the exist-opposite
question with the same fail/fail bits, the y-probe own-lock-in leftover
already answered HOLD by including the own lock at `A`, later-tick
seed-transfer already holds reverse, named signs should suffice because they
keep orientation, and occupancy `n` should track that vector.

**Answer:** The named construction reports lock sets `{+e_1, +e_3}`,
`{+e_1, +e_3}`, `{+e_3}`, `{+e_1, +e_3}` at `A,B,C,D` from strictly-earlier
six-neighbor locks union `{L(q)}` when defined. Mixed remains a set. The
construction does not sum. Occupancy `n` is not used. Named signs lost the
axis. No pair from `S^+(A)` and `S^+(B)` is opposite, so reverse fails. No
pair from `S^+(C)` and `S^+(D)` is opposite, so face fails. Reverse HOLD
does not use `L(A)`. Formation-tick leftover that excludes `q` uses a
different set at `A`. Unique own-incoming leftover reports face `UNDEFINED`
at mixed `C`. The y-probe leftover reports reverse hold on a different
frame. Later-tick leftover waits for a global later T. The sets are not
those leftovers. The bits remain displayed. Incoming-lock uniqueness is not
required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
z-probes assigned `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`, `L(D)=+e_1`
and reported reverse fail with face `UNDEFINED`. A formation-tick
existential opposite display that excludes `q` assigned `{+e_1}`, `{+e_3}`,
`{+e_3}`, `{+e_3}` and reported reverse fail with face fail on a different
set. Later-tick existential opposite on these z-probes reported reverse hold
and face hold on different later sets `{+e_1, −e_1, +e_2, −e_2, +e_3}` and
`{+e_1, +e_2, −e_2, +e_3, −e_3}` after a global later T. The y-probe
own-lock-in readout on this seed reported reverse hold and face hold from
seed letter `−e_1` at y-probe `A`. Unique lock-vector lettering of the union
sets would report reverse `UNDEFINED` and face `UNDEFINED` because `A`, `B`,
and `D` mix. A sum leftover of the same lists would report reverse fail and
face fail because the sums are `(1,0,1)` with `(1,0,1)` and `+e_3` with
`(1,0,1)`. This note is not those displays: mixed remains a set, the
construction does not sum, reverse HOLD does not use `L(A)`, reverse fails,
and face fails.

**Gate disposition:** PASS for the own-lock-in union existential-opposite
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the sum of the lock set,” “bits are Admissibility,” “the
letter is occupancy `n`,” “the sets equal unique own-incoming letters,” “the
sets equal formation-tick leftover that excludes `q`,” “the readout equals
the y-probe own-lock-in leftover,” “the readout equals later-tick
seed-transfer,” “reverse HOLD uses `L(A)`,” “reverse is `hold`,” or “face is
`UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, reads each probe's own unique incoming lock
or `UNDEFINED`, collects six-neighbor locks formed strictly earlier than
each probe's own formation tick, unions those locks with `{L(q)}` when
defined, reads the union sets at the four z-probes, reports whether reverse
HOLD uses `L(A)`, and checks Theorems 1--3. It also checks that the
construction is not named-sign lettering, that mixed sets remain defined,
that the construction does not sum, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
that the sets are not leftover of unique own-incoming letters, that the sets
are not leftover of formation-tick existential opposite that excludes `q`,
that the readout is not leftover of the y-probe own-lock-in, and that the
readout is not leftover of later-tick seed-transfer. No runner cache is
written.
