---
claim_id: opposite_lock_xprobe_own_lock_in_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite in the union of strictly-earlier 6-NN locks with the probe's own incoming lock on the four nsopp x-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_xprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py
---

# Own-Lock-In Existential Opposite Reverse And Face On Four Opposite-Lock X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite in the union of
strictly-earlier six-neighbor locks with the probe's own incoming lock on
the four nsopp x-probes in `B_3(0)`. Let `t(q)` be the formation tick of
probe `q`. Let `L(q)` be `q`'s own unique incoming lock; seeds use seed
letters. If several earliest incoming steps exist, `L(q)` is `UNDEFINED`.
At that tick, `S^+(q)` is the set of locks of six-neighbors of `q` that
formed at tick `< t(q)` (strictly earlier), union `{L(q)}` when `L(q)` is
defined. Reverse holds if and only if some lock in `S^+(A)` is the vector
opposite of some lock in `S^+(B)`. Face holds if and only if some lock in
`S^+(C)` is the vector opposite of some lock in `S^+(D)`. Empty `S^+` on
either side of a comparison is `UNDEFINED`; nonempty with no opposite pair
fails. Occupancy `n` is not used. This is not named-sign lettering. This is
not a unique lock-vector leftover and not a sum leftover. This is not
leftover of formation-tick existential opposite that excludes `q`: that
display reports reverse fail and face fail. This is not leftover of the
unique own-incoming lock-vector letters on these x-probes: that readout
reports reverse `UNDEFINED` with face `UNDEFINED` at mixed `A` and mixed
`D`. This is not leftover of later-tick existential opposite on these
x-probes (both bits hold after a global `T=4`). This is not leftover of
own-lock-in existential opposite on the four nsopp y-probes (both bits
hold, and `A` is a seed). Uniqueness of incoming locks is not required.
Uniqueness of the lock set is not required. Displayed, not adopted. This
note does not write existential opposite into Admissibility and does not
attach a formation member from already-recorded six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_xprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py`](../scripts/opposite_lock_xprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
own-lock-in union sets. Named signs `{+,−}` are a coarser readout and are
not used. A singleton unique lock-vector letter is a different readout and
is not used. A `Z^3` sum of those locks is a different readout and is not
used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ as the union of strictly-earlier six-neighbor locks with L(q) when defined, on the four nsopp x-probes, with reverse fail and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_xprobe_own_lock_in_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from existential opposite in the union of strictly-earlier 6-NN locks with the probe's own incoming lock on the four nsopp x-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with formation-tick leftover that excludes q, do not identify the sets with unique own-incoming leftover, and do not identify the sets with later-tick leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of own-lock-in union sets on the four nsopp x-probes; displayed, not adopted"
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
own-lock-in union sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. `A` is not a seed.

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

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
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
x-probes. It is not leftover of later-tick existential opposite on these
x-probes.

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

## Theorem 1 — formation ticks, own incoming locks, and S^+ at each x-probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four x-probes. The formation ticks are `t(A)=3`, `t(B)=2`, `t(C)=4`,
`t(D)=3`. `A` is not a seed. Those ticks locate the already-recorded
six-neighbor set. They are not occupancy kernels and are not a global later
T.

Own incoming locks and own-lock-in union sets at each probe's own formation
tick are:

```text
A: incoming −e_3, +e_3, +e_2; +e_1 at (0, 0, 0), +e_1 at (1, -1, 0),
   +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);
   t(A)=3;  L(A) = UNDEFINED;  S^+(A) = {+e_1}
B: incoming +e_1; +e_3 at (0, 1, 1);
   t(B)=2;  L(B) = +e_1;  S^+(B) = {+e_1, +e_3}
C: incoming +e_1; −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0);
   t(C)=4;  L(C) = +e_1;  S^+(C) = {+e_1, +e_2, +e_3, −e_3}
D: incoming −e_2, −e_3, +e_3; −e_1 at (0, 1, 0), +e_1 at (1, 2, 0),
   +e_1 at (1, 1, 1), +e_1 at (1, 1, -1);
   t(D)=3;  L(D) = UNDEFINED;  S^+(D) = {+e_1, −e_1}
```

`A` is not a seed. Its already-recorded neighbors are the seed origin and
three copies of `+e_1`. Same-tick `D` and later `C` are excluded. `L(A)` is
`UNDEFINED` from three earliest incoming steps `−e_3`, `+e_3`, and `+e_2`,
so `S^+(A)` equals the strictly-earlier neighbor set `{+e_1}`. `B`'s
already-recorded neighbor locks `+e_3`, and `L(B)=+e_1`, so
`S^+(B)={+e_1, +e_3}`. `C`'s already-recorded neighbor is `A` with mixed
incoming `{−e_3, +e_3, +e_2}`, and `L(C)=+e_1`, so
`S^+(C)={+e_1, +e_2, +e_3, −e_3}`. `D`'s already-recorded neighbors mix
`−e_1` at the seed partner `(0,1,0)` with three copies of `+e_1`. Mixed
remains a set. `L(D)` is `UNDEFINED` from three earliest incoming steps, so
`S^+(D)` is that neighbor set `{+e_1, −e_1}`.

Incoming locks exist and need not be unique (`A` has three earliest incoming
steps `−e_3`, `+e_3`, and `+e_2`; `D` has three earliest incoming steps
`−e_2`, `−e_3`, and `+e_3`). That non-uniqueness leaves `L(A)` and `L(D)`
`UNDEFINED` and does not empty `S^+(A)` or `S^+(D)`. Uniqueness is not
required.

Reverse HOLD does not use L(A). `L(A)` is `UNDEFINED`, so own–neighbor and
own–own channels that would read `L(A)` are unavailable. Neighbor–neighbor
reverse on the strictly-earlier sets also fails: those sets are `{+e_1}` at
`A` and `{+e_3}` at `B`. Reverse therefore fails on the union sets as well.

The unique own-incoming letters on these same x-probes are `UNDEFINED`,
`+e_1`, `+e_1`, `UNDEFINED`. Those are different objects: `S^+(A)` is
`{+e_1}` and is nonempty. Formation-tick existential opposite that excludes
`q` reports `S(B)={+e_3}` and `S(C)={+e_2, +e_3, −e_3}`, not the unions
that include `L(B)` and `L(C)`. Later-tick existential opposite on these
same x-probes reports `{+e_1, −e_2, +e_3, −e_3}` at `A` after waiting for a
global `T=4`. Own-lock-in existential opposite on the four nsopp y-probes
reports `{−e_1}` at seed `A=(0,1,0)`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty: `S^+(A)={+e_1}` and
`S^+(B)={+e_1, +e_3}`. The pairs are `+e_1+(+e_1)=(2,0,0)` and
`+e_1+(+e_3)=(1,0,1)`. No pair is opposite. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Reverse HOLD does not use L(A):
`L(A)` is `UNDEFINED`, so neither own–neighbor nor own–own can fire from
`A`. Neighbor–neighbor reverse also fails. This is not leftover of
formation-tick existential opposite that excludes `q`: that leftover also
fails reverse, but from `S(B)={+e_3}` rather than `{+e_1, +e_3}`, and it
reports face fail. Unique lock-vector lettering of the union sets would
report reverse `UNDEFINED` because `B` mixes. A sum leftover of the same
lists would replace `S^+(A)` by `+e_1` and `S^+(B)` by `(1,0,1)` and would
also fail reverse, for a different reason. Unique own-incoming letters on
these x-probes report reverse `UNDEFINED` from mixed `A`. Later-tick
existential opposite on these same x-probes reports reverse hold on
different lists that wait for a global `T=4`. Own-lock-in on the four nsopp
y-probes reports reverse hold from seed letter `−e_1` at `A` opposite `+e_1`
at `B`. Holding reverse on this x-probe frame needs the later tick.

Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S^+(C)={+e_1, +e_2, +e_3, −e_3}`
and `S^+(D)={+e_1, −e_1}`, so `+e_1+(−e_1)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Face HOLD uses `L(C)` as
own–neighbor: `L(C)=+e_1` is opposite `−e_1` in the strictly-earlier
neighbor set at `D`. Neighbor–neighbor face on the exclude-`q` sets fails,
because those earlier sets are `{+e_2, +e_3, −e_3}` at `C` and
`{+e_1, −e_1}` at `D`. Own–own face is `UNDEFINED` because `L(D)` is
`UNDEFINED`. Unique own-incoming letters on these same x-probes assign
`L(D)=UNDEFINED` from three earliest incoming steps and report face
`UNDEFINED`. Unique lock-vector lettering of the union sets would also
report face `UNDEFINED` because `C` and `D` mix. A sum leftover would
replace `S^+(C)` by `(1,1,0)` and `S^+(D)` by the origin and would fail
face, while existential opposite holds. Named-sign lettering lost the axis
in mixed `{+,−}` at `C` and `D`. Formation-tick existential opposite that
excludes `q` reports face fail. Later-tick existential opposite reports
face hold after a global `T=4` on a different set at `D` that includes
`+e_2`. Face holds from the own-lock-in union at `C`; it does not wait for
a unique own incoming lock at `D`.

Face holds.

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
  x-probes.
- It does not reprint formation-tick existential opposite that excludes `q`.
- It does not wait for a global later T.
- It does not reprint later-tick existential opposite on these x-probes.
- It does not reprint own-lock-in existential opposite on the four nsopp
  y-probes.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock process, the own-lock-in union sets, and the existential-opposite
reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `3` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `UNDEFINED`, `+e_1`, `+e_1`, `UNDEFINED` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1}`, `{+e_1, +e_3}`, `{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1}` |
| reverse HOLD uses `L(A)` (own–neighbor or own–own) or only neighbor–neighbor | Theorem 1; reverse does not hold; does not use L(A); neighbor–neighbor also fails |
| reverse and face | Theorems 2–3; `fail` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these x-probes | not this display |
| leftover of formation-tick existential opposite that excludes `q` | not this display |
| leftover of later-tick existential opposite on these x-probes | not this display |
| leftover of own-lock-in existential opposite on the four nsopp y-probes | not this display |
| leftover of nnseed x-probe formation-time existential opposite | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite in the union of strictly-earlier 6-NN locks with the probe's own incoming lock on the four nsopp x-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed own-lock-in existential-opposite reverse/face report on these four nsopp x-probes. |
| V3 | Own-lock-in union sets and the `fail`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the union of strictly-earlier six-neighbor lock vectors with `L(q)` when defined and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint formation-tick leftover that excludes
`q`, does not reprint later-tick leftover, does not reprint y-probe
own-lock-in leftover, and does not use occupancy `n`. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while the mixed union sets are nonempty, reverse fails, and face holds |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is `+e_1` and sum of `S^+(B)` is `(1,0,1)`; sum of `S^+(C)` is `(1,1,0)` and sum of `S^+(D)` is the origin, which would fail face while `+e_1+(−e_1)=0` |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `C` and `D` would hide `+e_1+(−e_1)=0` |
| unique own-incoming lock-vector leftover on these x-probes | reuse `L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`, `L(D)=UNDEFINED` | refused; different object; that leftover reports reverse `UNDEFINED` and face `UNDEFINED` while own-lock-in reverse fails and face holds |
| leftover of formation-tick existential opposite that excludes `q` | reuse `S(A)={+e_1}`, `S(B)={+e_3}`, `S(C)={+e_2, +e_3, −e_3}` with reverse fail and face fail | refused; different sets; `S^+(B)` and `S^+(C)` include own letters and face holds |
| leftover of later-tick existential opposite | reuse global later T and reverse hold with face hold | refused; different sets; this display does not wait for a global later T |
| leftover of own-lock-in existential opposite on the four nsopp y-probes | reuse seed `A=(0,1,0)` with reverse hold and face hold | refused; different frame; x-probe `A` is not a seed and reverse fails |
| leftover of nnseed x-probe formation-time existential opposite | reuse seed `+e_1/+e_2` and x-probes | refused; different process |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `A` and at `D` are kept and `L(A)`, `L(D)` are `UNDEFINED` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, formation-tick lock set of six-neighbors formed
strictly earlier than each probe's own `t`, union with `L(q)` when defined,
existential opposite, four x-probes with non-seed `A`, and reverse/face as
existence of a pair that sums to zero are declared. No uniqueness of incoming
locks, no occupancy `n`, no named-sign reduction, no singleton leftover, no
sum leftover, no unique own-incoming leftover, no formation-tick exclude-`q`
leftover, no later-tick leftover, no y-probe own-lock-in leftover, no global
later T, no formation attachment from already-recorded six-neighbor locks,
and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own-lock-in union set | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
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
own-incoming letters already answered reverse `UNDEFINED` with face
`UNDEFINED`, formation-tick existential opposite already answered the
exist-opposite question with reverse fail and face fail, later-tick
existential opposite already answered with hold/hold, y-probe own-lock-in
already answered with hold/hold so this is leftover, named signs should
suffice because they keep orientation, occupancy `n` should track that
vector, and reverse HOLD must use `L(A)`.

**Answer:** The named construction reports lock sets `{+e_1}`, `{+e_1, +e_3}`,
`{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1}` at `A,B,C,D` from strictly-earlier
six-neighbor locks union `{L(q)}` when defined. Mixed remains a set. The
construction does not sum. Occupancy `n` is not used. Named signs lost the
axis. No pair from `S^+(A)` and `S^+(B)` is opposite, so reverse fails.
Reverse HOLD does not use L(A): `L(A)` is `UNDEFINED`, and neighbor–neighbor
also fails. Some pair from `S^+(C)` and `S^+(D)` is opposite, so face holds
from `L(C)=+e_1` against `−e_1` at `D`. Formation-tick leftover that excludes
`q` reports face fail. Unique own-incoming leftover reports both bits
`UNDEFINED`. Later-tick leftover waits for a global `T=4` and holds both
bits. Y-probe own-lock-in holds reverse from a seed letter at a different
`A`. The sets are not those leftovers. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
x-probes assigned `L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`,
`L(D)=UNDEFINED` and reported reverse `UNDEFINED` with face `UNDEFINED`. A
formation-tick existential opposite display that excludes `q` assigned
`S(A)={+e_1}`, `S(B)={+e_3}`, `S(C)={+e_2, +e_3, −e_3}`, `S(D)={+e_1, −e_1}`
and reported reverse fail with face fail. Later-tick existential opposite on
these x-probes reported reverse hold and face hold on different later sets
`{+e_1, −e_2, +e_3, −e_3}` and `{+e_1, +e_2, −e_2, +e_3, −e_3}` after a
global `T=4`. Own-lock-in existential opposite on the four nsopp y-probes
reported reverse hold and face hold from seed letter `−e_1` at `A=(0,1,0)`.
Unique lock-vector lettering of the union sets would report reverse
`UNDEFINED` and face `UNDEFINED` because `B`, `C`, and `D` mix. A sum
leftover of the same lists would report reverse fail and face fail because
the sums are `+e_1` with `(1,0,1)` and `(1,1,0)` with the origin. This note
is not those displays: mixed remains a set, the construction does not sum,
`S^+(A)` is nonempty from strictly-earlier `+e_1`, reverse fails, reverse
HOLD does not use L(A), and `+e_1+(−e_1)=(0,0,0)` so face holds.

**Gate disposition:** PASS for the own-lock-in union existential-opposite
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the sum of the lock set,” “bits are Admissibility,” “the
letter is occupancy `n`,” “the sets equal unique own-incoming letters,” “the
sets equal formation-tick leftover that excludes `q`,” “the sets equal
later-tick leftover,” “reverse is `hold`,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, reads each probe's own unique incoming lock
or `UNDEFINED`, collects six-neighbor locks formed strictly earlier than
each probe's own formation tick, unions those locks with `{L(q)}` when
defined, reads the union sets at the four x-probes, and checks Theorems
1--3. It also checks that reverse HOLD does not use L(A), that face HOLD
uses `L(C)` as own–neighbor, that the construction is not named-sign
lettering, that mixed sets remain defined, that the construction does not
sum, that occupancy `n` is not used, that a formation member from
already-recorded six-neighbor locks is not attached, that the sets are not
leftover of unique own-incoming letters, that the sets are not leftover of
formation-tick existential opposite that excludes `q`, that the sets are not
leftover of later-tick existential opposite, and that the sets are not
leftover of y-probe own-lock-in. No runner cache is written.
