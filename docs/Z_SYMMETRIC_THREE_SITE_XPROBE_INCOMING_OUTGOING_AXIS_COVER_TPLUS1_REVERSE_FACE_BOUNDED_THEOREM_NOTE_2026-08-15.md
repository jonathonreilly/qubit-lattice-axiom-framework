---
claim_id: z_symmetric_three_site_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis-cover of M and O at t+1 on the four #7188 x-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py
---

# Axis-Cover Of Own-Incoming And Own-Outgoing At t+1 Reverse And Face On Four #7188 X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** axis-cover of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that cover, on the
four nszopinx #7188 x-probes in `B_3(0)={n:n·n<=9}`. Same process as
nszopinx #7188. Let `t(q)` be the formation tick of probe `q`. Let
`τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton
seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Axis
of a defined lock set `S` is `Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs
at `q` if and only if both `M` and `O` are defined nonempty, `Axis(M)`
intersect `Axis(O)` is empty, and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. `UNDEFINED` if `M` or `O` is `UNDEFINED`. Else fail.
Reverse HOLDs if and only if cover HOLDs at `A` and at `B`. Face HOLDs if
and only if cover HOLDs at `C` and at `D`. This is HOLD iff cover, not
leftover-empty fail. This is not leftover of leftover-of-`M` alone. This
is not leftover of leftover-of-`O` alone. This is not leftover of #7205
M exist-opposite fail/fail, even when reverse/face bits match. Uniqueness
is not required. Mixed remains a set. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Reverse and face are scored on cover HOLD at the paired probes. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock
letter is a different readout and is not used as the object. Existential
opposite of signed locks is a different readout and is not used as the
cover reverse. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of axis-cover of M and O at t+1 on the four #7188 x-probes, complementary cover at each probe, reverse fail and face fail from cover; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face
target_blocker_text: "display axis-cover of M and O at t+1 on the four #7188 x-probes, and reverse/face from that cover, HOLD iff cover, not leftover-empty fail"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep axis-cover of M and O at t+1 displayed; do not write cover into Admissibility, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace cover by existential opposite of signed locks, do not replace cover by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for axis-cover of M and O at t+1 on the four #7188 x-probes and reverse/face from that cover; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose axis-cover
of `M` and `O` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. `A` is not a seed. Same process and x-probes as nszopinx #7188.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,0,1), (0,0,-1)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,0,1)=−e_1`, and `L(0,0,-1)=−e_1`. The
third site is the z-mirror of the two-site opposite-lock partner `(0,0,1)`.
This seed is not the two-site opposite-lock seed `{0,(0,0,1)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
y-symmetric three-site seed `{0,(0,1,0),(0,-1,0)}`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required. Mixed remains a set.

## Named axis-cover of `M` and `O` at `τ=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate steps collapse in the set. The construction does
not require `M` or `O` to be a singleton. It does not sum either set. It
does not replace `O` by `M`. It does not wait for a global later T.
Occupancy of sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover at a probe at the same cut:

```text
cover(q) HOLDs iff M and O are defined nonempty,
Axis(M) intersect Axis(O) is empty,
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

If `q` is unformed at `τ`, then cover is `UNDEFINED`. Empty `M` or empty
`O` fails. Overlapping axes fail. Incomplete union fails. Axis is unsigned:
`+e_i` and `−e_i` occupy the same axis. Leftover of the union is
`{e_1,e_2,e_3}` minus `(Axis(M) union Axis(O))`. Empty leftover is leftover
fail of leftover axis; this display is HOLD iff cover, not leftover-empty
fail. Leftover of `M` alone is `{e_1,e_2,e_3}` minus `Axis(M)`, a different
object. Leftover of `O` alone is a different object.

Reverse axis-cover holds if and only if cover HOLDs at `A` and at `B`. Face
axis-cover holds if and only if cover HOLDs at `C` and at `D`. Either side
`UNDEFINED` is `UNDEFINED`. Else if both sides HOLD, reverse or face HOLDs.
Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
cover reverse is refused: leftover-empty fail scores empty leftover as
fail, while cover HOLDs from complementary occupation of all three axes.

## Theorem 1 — ticks, `M`, `O`, `Axis`, and cover at `τ=t+1`

On this process the four x-probes form. Compare to #7205 M exist-opposite:
that leftover reports `M(A)={+e_2, −e_2}`, `M(B)={+e_1}`, `M(C)={+e_1}`,
`M(D)={+e_1}` at each probe's own formation tick, reverse fail, and face
fail. This display reads complementary axis-cover of timed `M` and `O` at
`τ=t+1`. `M` at `τ` is frozen equal to `M` at `t`:

```text
t(A)=3
t(B)=2
t(C)=4
t(D)=2
M(A, τ) = {+e_2, −e_2}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {+e_1}
O(A, τ) = {+e_1}
O(B, τ) = {+e_2, −e_2, +e_3}
O(C, τ) = {+e_2, −e_2}
O(D, τ) = {+e_2, −e_2}
Axis(M)(A, τ) = {e_2}
Axis(O)(A, τ) = {e_1}
Axis(M)(B, τ) = {e_1}
Axis(O)(B, τ) = {e_2, e_3}
Axis(M)(C, τ) = {e_1}
Axis(O)(C, τ) = {e_2}
Axis(M)(D, τ) = {e_1}
Axis(O)(D, τ) = {e_2}
cover(A) = fail
cover(B) = hold
cover(C) = fail
cover(D) = fail
```

`A` is not a seed. Mixed remains a set: `M(A,τ)` has two earliest incoming
steps and `O(B,τ)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at mixed probes. Here uniqueness is not required.
At `B`, `M` and `O` are defined nonempty, `Axis(M)` and `Axis(O)` are
complementary: their union is `{e_1,e_2,e_3}` and their intersection is
empty, so cover HOLDs. At `A`, `C`, and `D`, the axes are disjoint and
nonempty but the union misses `e_3`, so cover fails. Leftover of the union
is `{e_3}` at `A`, `C`, and `D`, and empty at `B`. Leftover-empty fail of
that leftover is not this object. O is not M.

#7205 M exist-opposite reverse fail and face fail are signed pair reports
across probes. Cover is unsigned complementary occupation of axes of `M`
versus `O` at one probe. Same reverse/face bits do not make the objects
equal. Leftover of `M` alone at `C` and `D` is `{e_2,e_3}`, nonempty and
equal. Leftover of `O` alone at `C` and `D` is `{e_1,e_3}`, nonempty and
equal. Those one-sided leftovers are not this object.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 0, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0)
new 6-NN of D at t(D)+1: (1, 2, 0), (1, 0, 0)
```

At formation tick, `O` is empty at each of the four x-probes. Empty `O`
fails cover. At `τ=t+1`, `O` is nonempty at each probe. Cover still fails
at `A`, `C`, and `D` by incomplete union, not by empty `O`. Cover HOLDs at
`B` only after that one-tick fill.

## Theorem 2 — reverse from axis-cover at `τ`

Reverse axis-cover holds if and only if cover HOLDs at `A` and at `B`.
Cover fails at `A` and HOLDs at `B`. Reverse fails. This is HOLD iff cover,
not leftover-empty fail.

Reverse axis-cover at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Reverse: fail.
Leftover of the union is `{e_3}` at `A` and empty at `B`, so leftover-empty
reverse also fails. Cover reverse fails because cover fails at `A`, not
because leftover at `B` is empty. Leftover-of-`M` reverse fails because
leftover of `M` at `A` is `{e_1, e_3}` and leftover of `M` at `B` is
`{e_2, e_3}`: nonempty and unequal. Leftover-of-`O` reverse fails because
leftover of `O` at `A` is `{e_2, e_3}` and leftover of `O` at `B` is
`{e_1}`. Exist-opposite reverse of signed `M` fails. Those leftovers are
not this display.

Does `Axis(M)∪Axis(O)` cover still HOLD where #7205 M exist-opposite fails?
No. Cover fails at `A`. Reverse fails.

Reverse fails.

## Theorem 3 — face from axis-cover at `τ`

Face axis-cover holds if and only if cover HOLDs at `C` and at `D`. Both
covers fail. Face fails.

Face axis-cover at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Face: fail. Leftover of the union
is `{e_3}` at `C` and at `D`, nonempty and equal, so leftover-empty face
HOLDs. Cover face fails from incomplete union that misses `e_3`. Leftover
of `M` at `C` and at `D` is `{e_2, e_3}`, nonempty equal, so leftover-of-
`M` face HOLDs. Leftover of `O` at `C` and at `D` is `{e_1, e_3}`, nonempty
equal, so leftover-of-`O` face HOLDs. Exist-opposite face of signed `O`
HOLDs from `{+e_2, −e_2}` at both `C` and `D`. Exist-opposite face of
signed `M` fails, matching the cover face bit. Face HOLD of leftover-empty,
of leftover of `M` alone, of leftover of `O` alone, and of signed `O`
exist-opposite, against cover face fail, is the discriminator. Cover does
not still HOLD on this M-fail member.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover fails at `C` and at `D`.

Face fails.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require cover sides to be singletons.
- It does not sum either set.
- It does not replace cover by leftover-empty fail.
- It does not replace cover by leftover of `M` alone.
- It does not replace cover by leftover of `O` alone.
- It does not replace cover by existential opposite of signed locks.
- It does not replace `O` by `M`.
- It does not replace cover by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint #7205 M exist-opposite fail/fail as this cover.
- It does not reprint axis-cover HOLD from other HOLDING-M members as this
  member.
- It does not use occupancy of sites as the letter.
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
z-symmetric three-site process, axis-cover of `M` and `O` at `t+1`, and the
reverse/face bits from cover are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nszopinx #7188 seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; nonempty outgoing dual |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary only at `B` |
| cover at `τ` | Theorem 1; fail, hold, fail, fail |
| reverse from axis-cover at `τ` | Theorem 2; `fail` |
| face from axis-cover at `τ` | Theorem 3; `fail` |
| compare to #7205 M exist-opposite | Theorem 1; same reverse/face bits, different object |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail | not this cover display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of #7205 M exist-opposite | not this cover display |
| global later T | not used |
| axis-cover as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: axis-cover of `M` and `O` at `t+1` on the four #7188 x-probes, and reverse/face from that cover, on the #7205 M-fail member. |
| V2 | Current main has no landed axis-cover reverse/face of timed `M` and `O` on these four #7188 x-probes. |
| V3 | Cover reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned axis-cover of own incoming and own outgoing at the same `t+1` cut and scores HOLD iff cover. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace cover by leftover-empty fail, does not
replace cover by leftover of `M` alone or leftover of `O` alone, does not
replace cover by existential opposite of signed locks, and does not
identify this display with #7205 M exist-opposite fail/fail. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is `{e_3}` at `C` and `D`, leftover face HOLDs, while cover face fails | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `C` and `D` is `{e_2,e_3}`, nonempty equal, face would hold | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `C` and `D` is `{e_1,e_3}`, nonempty equal, face would hold | ATTEMPTED |
| #7205 M exist-opposite | reuse signed reverse fail and face fail of `M` | those bits fail for a signed pair across probes; cover fails from incomplete unsigned axes of `M` versus `O` at one probe | ATTEMPTED |
| signed `O` exist-opposite | score reverse/face inside `O` | `O` exist-opposite face HOLDs from `{+e_2, −e_2}` at `C` and `D`; cover face fails | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(A,τ)` and mixed `O(B,τ)` remain sets; unique-letter cover is `UNDEFINED` at `A` and at `B` | ATTEMPTED |
| letter intersection as cover | score reverse/face inside `M ∩ O` | letter intersection empty is not axis-cover; opposite signs can share an axis | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover is a six-neighbor star; cover is unsigned complementary axes | ATTEMPTED |
| two-site opposite-lock seed | drop the z-mirror `(0,0,−1)` | different process; `M(A)` then includes `+e_3` | ATTEMPTED |
| y-probes | score `A=(0,1,0)` | different probes; this member scores the #7188 x-probes | ATTEMPTED |
| sum of a set | replace cover by a `Z^3` sum | mixed `M(A)` sums to the origin; cover still reads `{e_2}` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by axis-cover | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of cover with leftover of
`M` alone, missing identification of cover with leftover-empty fail, missing
identification of cover with existential opposite of signed locks, and
missing Record identification of cover reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own incoming set and
own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}` by
nonempty `M` and `O`, HOLD iff cover not leftover-empty fail, four x-probes
with non-seed `A`, and mixed remains a set are declared. No uniqueness of
incoming locks, no six-neighbor lock union as the scored object, no global
later T, no formation attachment from already-recorded six-neighbor locks,
and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
cover `fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four cover reports, reverse/face from cover | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for cover reverse/face, a
formation-rate rule, and a physical selector among complementary axes. None
is taken here.

### N7 — hostile steelman

**Steelman:** Cover fail/fail is only #7205 M exist-opposite fail/fail;
leftover-empty already answers three-axis occupation; leftover of `M`
alone already gives `{e_2,e_3}` at `C`; leftover of `O` alone already
gives `{e_1,e_3}`; incomplete union is only empty leftover `{e_3}`; and
mixed `A` should make reverse `UNDEFINED`.

**Answer:** #7205 M exist-opposite scores a signed pair across two probes.
Cover scores unsigned complementary axes of `M` versus `O` at one probe.
Leftover-empty face HOLDs because leftover of the union is `{e_3}` at `C`
and at `D`. Cover face fails because the union misses `e_3` and cover is
HOLD iff complementary occupation of all three axes. Leftover of `M` alone
and leftover of `O` alone are nonempty one-sided leftovers whose face
HOLDs; they are not complementary cover of the pair. Mixed `M(A)` remains
a set; unique-letter cover is `UNDEFINED` at mixed `A` while cover is
`fail`. Reverse axis-cover is HOLD iff cover at `A` and at `B`, not
leftover-empty fail and not #7205 M exist-opposite.

### N8 — cross-cycle echo

nszopinx #7188 reported reverse hold and face hold from same-tick-inclusive
six-neighbor lock union on these x-probes. nszmenu #7205 reported reverse
fail and face fail from own incoming `M`. Axis-cover HOLD on other
HOLDING-M members is a different process. This note is not those displays:
it reports axis-cover of `M` and `O` at `τ=t+1` on the four #7188
x-probes, cover fail at `A`, hold at `B`, fail at `C`, fail at `D`, reverse
fail, and face fail. HOLD iff cover, not leftover-empty fail. Cover does
not still HOLD where #7205 M exist-opposite fails.

**Gate disposition:** PASS for the axis-cover `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover-empty fail,” “the
predicate equals leftover of `M` alone,” “the predicate equals leftover of
`O` alone,” “the predicate equals #7205 M exist-opposite fail/fail,” “bits
are Admissibility,” “cover HOLDs at `A`,” “reverse axis-cover HOLDs,” or
“face axis-cover HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nszopinx #7188
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports unsigned axis of each, reports cover of the pair, lists new records
in `B_3(0)` between `t` and `t+1` that meet a probe's six-neighbors, and
checks Theorems 1--3. It also checks that cover fails at `A`, `C`, and `D`
and HOLDs at `B`, that leftover-empty face HOLDs while cover face fails,
that leftover of `M` alone and leftover of `O` alone are different objects,
that mixed sets remain sets, that unique-letter cover is `UNDEFINED` at
mixed `M` and mixed `O`, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
and that the display is not leftover of #7205 M exist-opposite. No runner
cache is written.
