---
claim_id: opposite_lock_yprobe_sametick_union_own_two_tick_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse/face from S⁺ at t versus t+1 on the four #7167 y-probes, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py
---

# Two-Tick Composition Of Same-Tick-Inclusive Union Own Reverse And Face On Four Opposite-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from `S^+` at each probe's formation tick `t`
versus `t+1` on the four #7167 y-probes in `B_3(0)={n:n·n<=9}`, no global
T. Let `t(q)` be the formation tick of probe `q`. Let `τ0(q)=t(q)` and
`τ1(q)=t(q)+1`. `L(q)` is `q`'s own unique incoming lock; seeds use seed
letters. If several earliest incoming steps exist, `L(q)` is `UNDEFINED`.
At cut `τ`, `S^+(q,τ)` is the set of locks of six-neighbors of `q` that
formed at tick `<= τ` and are not `q`, union `{L(q)}` when `L(q)` is
defined and `t(q)<=τ`. Reverse at a cut holds if and only if some `a` in
`S^+(A,·)` and some `b` in `S^+(B,·)` have `a+b=(0,0,0)`. Face likewise
on `C,D`. Empty `S^+` on either side is `UNDEFINED`; nonempty with no
opposite pair fails. Composition HOLD if and only if the `t+1`
reverse/face bits equal the `t` bits. Occupancy `n` is not used. This is
not leftover of own incoming sets M: that leftover freezes earliest
incoming steps, while S^+ grows at A, B, and C from t to t+1.
This is not leftover of unique own-incoming letters. This is not leftover
of same-tick-inclusive existential opposite that excludes `q`. This is
not leftover of later-tick union own. Uniqueness of incoming locks is not
required. Mixed remains a set. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_sametick_union_own_two_tick_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in
`S^+` at each probe's `t` and at `t+1`. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock letter is a different
readout and is not used. A `Z^3` sum of those locks is a different readout
and is not used. Own incoming sets `M` are a different readout and are not
used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ at t and at t+1 on the four #7167 y-probes, with reverse hold, face hold, and composition HOLD because t+1 bits equal t bits even though S^+ grows at A, B, and C; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_sametick_union_own_two_tick_composition_reverse_face
target_blocker_text: "display reverse and face from S^+ at t versus t+1 on the four #7167 y-probes, no global T, and whether those bits compose"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse, face, and composition displayed; do not write existential opposite into Admissibility, do not reduce to a unique incoming letter, do not replace S^+ by own incoming M, do not wait for a global later T, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for two-tick composition of S^+ reverse/face on the four #7167 y-probes, no global T; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose `S^+`
sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This is the same process as
the #7167 same-tick union-own display on these y-probes.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required.

## Named `S^+` at `t` and at `t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There is no global T.

`L(q)` is `q`'s own unique incoming lock in `{±e_i}`. Seeds use seed
letters. If several earliest incoming steps exist, `L(q)` is `UNDEFINED`.

At cut `τ`, `S^+(q,τ)` is the set of locks of six-neighbors of `q` that
formed at tick `<= τ` and are not `q`, union `{L(q)}` when `L(q)` is defined
and `t(q)<=τ`. Same-tick partners are kept when they are neighbors. The
probe itself is excluded from the neighbor set and re-enters only through
`{L(q)}` when that letter is defined and the probe has already formed.
This display does not wait for a global later T. Duplicate locks collapse
in the set. The construction does not require `S^+(q,τ)` to be a singleton.
It does not sum `S^+(q,τ)`. It does not replace `S^+` by own incoming `M`.
It does not use occupancy `n`.

Reverse at a cut holds if and only if some `a` in `S^+(A,·)` and some `b`
in `S^+(B,·)` have `a+b=(0,0,0)`. Face at a cut holds if and only if some
`c` in `S^+(C,·)` and some `d` in `S^+(D,·)` have `c+d=(0,0,0)`. Empty
`S^+` on either side is `UNDEFINED`; nonempty with no opposite pair fails.

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`. Else composition fails. Displayed, not
adopted.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero inside `S^+`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not attach L1.

## Theorem 1 — ticks, `S^+` at `τ0` and at `τ1`, and new six-neighbor records

On this process the four y-probes form. Own incoming locks and `S^+` at
each probe's `t` and at `t+1` are:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
L(A) = −e_1
L(B) = +e_1
L(C) = +e_2
L(D) = UNDEFINED
S^+(A, τ0) = {+e_1, −e_1}
S^+(B, τ0) = {+e_1, +e_3}
S^+(C, τ0) = {−e_1, +e_2}
S^+(D, τ0) = {+e_1, −e_1, +e_2, +e_3, −e_3}
S^+(A, τ1) = {+e_1, −e_1, +e_2, +e_3, −e_3}
S^+(B, τ1) = {+e_1, +e_2, −e_2, +e_3, −e_3}
S^+(C, τ1) = {+e_1, −e_1, +e_2, +e_3, −e_3}
S^+(D, τ1) = {+e_1, −e_1, +e_2, +e_3, −e_3}
```

`A` is a seed. `S^+` at `τ0` is the #7167 same-tick union-own set.
S^+ grows at A, B, and C from τ0 to τ1. `S^+` at `D` is unchanged:
the new neighbor at `t(D)+1` locks `+e_1`, already in the `τ0` set. Mixed
`D` remains a set; `L(D)` stays `UNDEFINED` from three earliest incoming
steps `−e_2`, `−e_3`, and `+e_3`. Uniqueness is not required.

New records in `B_3(0)` between `τ0` and `τ1` that meet a probe's
six-neighbors:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

Those later neighbors enter `S^+` at `τ1` for `A`, `B`, and `C`. They do
not enter own incoming `M`: `M` is earliest incoming at the probe itself
and is frozen at formation. This is not leftover of own incoming sets `M`.

## Theorem 2 — reverse and face at `τ0` and at `τ1`

Reverse holds if and only if some `a` in `S^+(A,·)` and some `b` in
`S^+(B,·)` have `a+b=(0,0,0)`. At `τ0` the sets are `{+e_1, −e_1}` and
`{+e_1, +e_3}`, so `−e_1+(+e_1)=(0,0,0)`. Reverse holds. At `τ1` the sets
grow but still contain that opposite pair, so reverse holds again. Both
sides are nonempty and defined, so this is not `UNDEFINED`.

Reverse at τ0: hold
Reverse at τ1: hold

Face holds if and only if some `c` in `S^+(C,·)` and some `d` in
`S^+(D,·)` have `c+d=(0,0,0)`. At `τ0` the sets are `{−e_1, +e_2}` and
`{+e_1, −e_1, +e_2, +e_3, −e_3}`, so `−e_1+(+e_1)=(0,0,0)`. Face holds.
At `τ1` the sets still contain that pair, so face holds again.

Face at τ0: hold
Face at τ1: hold

Same-tick leftover that excludes `q` leaves `S(A)={+e_1}` and reports
reverse fail. Unique own-incoming letters report face `UNDEFINED` at mixed
`D`. Own incoming `M` freezes at formation and does not grow. Reverse and
face here are exist-opposite in `S^+` at two per-probe cuts.

## Theorem 3 — composition

Composition HOLD if and only if reverse at `τ1` equals reverse at `τ0` and
face at `τ1` equals face at `τ0`. Both reverse reports are `hold` and both
face reports are `hold`, so the bits match and neither side is `UNDEFINED`.

Composition: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. `S^+` grows at `A`,
`B`, and `C` between the cuts; the reverse/face bits nevertheless freeze.
Composition HOLD is that bit equality, not equality of the lock sets.

This is not leftover of own incoming sets `M` (those sets freeze and do
not grow). This is not leftover of unique own-incoming letters (face
`UNDEFINED` at mixed `D`). This is not leftover of same-tick-inclusive
existential opposite that excludes `q` (reverse fail). This is not leftover
of later-tick union own (global later T).

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the union set to be a singleton.
- It does not sum the union set.
- It does not replace `S^+` by own incoming `M`.
- It does not wait for a global later T.
- It does not use occupancy `n`.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint unique own-incoming lock-vector letters on these
  y-probes.
- It does not reprint same-tick-inclusive existential opposite that excludes
  `q`.
- It does not reprint later-tick union own.
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
a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock process, the two-cut `S^+` sets, and the reverse/face/composition
predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `−e_1`, `+e_1`, `+e_2`, `UNDEFINED` |
| `S^+` at `τ0` | Theorem 1; `{+e_1, −e_1}`, `{+e_1, +e_3}`, `{−e_1, +e_2}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` |
| `S^+` at `τ1` | Theorem 1; `{+e_1, −e_1, +e_2, +e_3, −e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` |
| reverse at `τ0` and at `τ1` | Theorem 2; `hold` / `hold` |
| face at `τ0` and at `τ1` | Theorem 2; `hold` / `hold` |
| composition | Theorem 3; HOLD |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| own incoming sets `M` | not this display |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: reverse/face from `S^+` at `t` versus `t+1` on the four #7167 y-probes, and whether those bits compose. |
| V2 | Current main has no landed two-tick `S^+` composition reverse/face report on these four #7167 y-probes. |
| V3 | Two-cut `S^+` sets and the `hold`/`hold`/`HOLD` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors union `L(q)` at two per-probe cuts and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not replace `S^+` by own incoming `M`, does
not wait for a global later T, and does not use occupancy `n`. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| own incoming sets `M` | replace `S^+` by earliest incoming steps at the probe | refused; leftover; `M` freezes at formation while `S^+` grows at `A`, `B`, and `C` |
| unique own-incoming lock-vector leftover | reuse `L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` | refused; different object; that leftover reports face `UNDEFINED` while face holds |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse `S(A)={+e_1}` with reverse fail | refused; different set; reverse holds at both cuts |
| leftover of later-tick union own | reuse global later T | refused; `τ0(q)=t(q)` and `τ1(q)=t(q)+1` are per-probe; no global T |
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; mixed remains a set |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sums fail reverse while exist-opposite holds |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; `L(D)` is `UNDEFINED` and face still holds |

### N2 — wall independence

Missing physical adoption, missing identification of `S^+` with own
incoming `M`, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, `S^+` as six-neighbor locks formed at tick `<= τ`
with the probe excluded, union with `L(q)` when defined and `t(q)<=τ`,
per-probe `τ0=t` and `τ1=t+1`, existential opposite, four y-probes with
seed `A`, and composition as equality of the two-cut bits are declared. No
uniqueness of incoming locks, no occupancy `n`, no named-sign reduction,
no `M` leftover, no same-tick exclude-`q` leftover, no later-tick leftover,
no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold`/`HOLD` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in `S^+` at `t` and at `t+1` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets at two cuts and reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** New six-neighbor records between `t` and `t+1` should flip
reverse or face; `S^+` growth means composition should fail; own incoming
`M` already answered two-tick composition because incoming is frozen;
unique own-incoming letters already answered reverse hold with face
`UNDEFINED`; same-tick-inclusive existential opposite already answered
reverse fail; later-tick union own already answered hold after a global T;
mixed sets should make reverse and face `UNDEFINED`; and composition HOLD
is only tautological.

**Answer:** `S^+` grows at `A`, `B`, and `C`. The opposite pair
`−e_1+(+e_1)=(0,0,0)` remains in both reverse sides and both face sides, so
the bits freeze at hold/hold. Composition HOLD is that bit equality, not
set equality. Own incoming `M` is a different object and freezes at
formation. Unique own-incoming leftover reports face `UNDEFINED` at mixed
`D`. Same-tick leftover that excludes `q` reports reverse fail. Later-tick
union own waits for a global later T. Mixed remains a set. The bits remain
displayed.

### N8 — cross-cycle echo

A same-tick union-own display on these y-probes (#7167) assigned
`S^+={+e_1, −e_1}`, `{+e_1, +e_3}`, `{−e_1, +e_2}`,
`{+e_1, −e_1, +e_2, +e_3, −e_3}` at each probe's own `t` and reported
reverse hold with face hold. A two-tick own-incoming-set composition on a
different process used `M` not `S^+` and reported frozen incoming sets.
Unique own-incoming letters on these y-probes report reverse hold with face
`UNDEFINED`. Same-tick leftover that excludes `q` reports reverse fail.
This note is not those displays: it reads `S^+` at `t` and at `t+1` on the
four #7167 y-probes, `S^+` grows at `A`, `B`, and `C`, reverse holds at
both cuts, face holds at both cuts, and composition HOLD because those bits
match.

**Gate disposition:** PASS for the two-tick `S^+` reverse/face composition
reports above. FAIL / DO NOT SHIP for “the predicate equals the named
sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals own incoming `M`,” “bits are Admissibility,” “reverse
fails,” “face is `UNDEFINED`,” “composition fails,” or “`S^+` is frozen at
`t+1`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, reads `S^+` at each y-probe's `t` and at
`t+1`, lists new records in `B_3(0)` between those cuts that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that `S^+` grows
while the bits freeze, that own incoming `M` is a different frozen object,
that unique-letter face is `UNDEFINED`, that same-tick leftover that
excludes `q` fails reverse, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
and that there is no global later T. No runner cache is written.
