---
claim_id: opposite_lock_yprobe_incoming_axis_agreement_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Incoming-axis agreement of M at t+1 on the four #7208 y-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_incoming_axis_agreement_tplus1_reverse_face_2026_08_15.py
---

# Incoming Axis Agreement Of M At t+1 Reverse And Face On Four #7208 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** incoming-axis agreement of the earliest incoming set `M` at each
probe's `τ=t+1`, and reverse/face from that unsigned axis set, on the four
nsmopp #7208 y-probes in `B_3(0)={n:n·n<=9}`. Same process as nsopp #7093.
Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)`
is the set of earliest incoming nearest-neighbor steps at `q` using only
records with tick `<= τ`. Seeds are a singleton seed letter. Unformed at
`τ` is `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Empty Axis is empty, not `UNDEFINED`.
Unformed at `τ` is `UNDEFINED`. Reverse holds if and only if
`Axis(M)(A)=Axis(M)(B)` as sets and both are defined and nonempty. Face
holds if and only if `Axis(M)(C)=Axis(M)(D)` as sets and both are defined
and nonempty. Empty Axis fails, and is not `UNDEFINED`. This is not leftover
of exist-opposite of signed `M`. This is not leftover of leftover-of-`M`
alone. This is not leftover of leftover-of-`O` alone. This is not leftover
of leftover axis of `M` and `O` (empty leftover, 3-axis cover). This is not
leftover of forall-perp of `M` versus `O`. This is not leftover of nmsimopp
exist-opposite of `M` and of `O` at `t+1`. This is not leftover of nmunopp
union. This is not leftover of nmt2opp `M` frozen at `t` as this reverse.
This is not leftover of nmot2opp two-tick composition. This is not leftover
of nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188
fail/fail. Uniqueness of incoming axes is not required. Mixed remains a
set. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_incoming_axis_agreement_tplus1_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_incoming_axis_agreement_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Axis is the unsigned lattice direction of a signed lock. Reverse and
face are scored on equality of nonempty `Axis(M)` sets at `τ=t+1`. Named
signs `{+,−}` are a coarser readout and are not used. A singleton unique
lock letter is a different readout and is not used as the object.
Existential opposite of signed locks is a different readout and is not used
as this reverse. Leftover of `Axis(M)` inside `{e_1,e_2,e_3}` is a different
readout and is not used. Leftover of `M` and `O` together is a different
readout and is not used. A `Z^3` sum of those locks is a different readout
and is not used. Occupancy of sites is not used. A six-neighbor star is not
the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of Axis(M) at t+1 on the four #7208 y-probes, reverse hold from equal nonempty Axis(M) at A and B, face fail from unequal nonempty Axis(M) at C and D; uniqueness of incoming axes is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_incoming_axis_agreement_tplus1_reverse_face
target_blocker_text: "display incoming-axis agreement of M at t+1 on the four #7208 y-probes, and reverse/face from that, no unique Axis required"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep incoming-axis agreement of M at t+1 displayed; do not write Axis(M) equality into Admissibility, do not replace Axis(M) by leftover of M alone, do not replace Axis(M) equality by existential opposite of signed locks, do not replace Axis(M) by leftover of M and O, do not identify the display with forall-perp HOLD, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for incoming-axis agreement of M at t+1 on the four #7208 y-probes and reverse/face from that; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose incoming
axis of `M` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nsmopp #7208.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0.

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

## Named incoming axis `Axis(M)` at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Duplicate incoming steps collapse in the set.
The construction does not require `M(q,τ)` to be a singleton. It does not
sum `M(q,τ)`. It does not replace `M` by locks of six-neighbors of `q`.
It does not wait for a global later T. Occupancy of sites is not used.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Incoming axis at the per-probe cut is `Axis(M(q,τ))`. If `q` is unformed at
`τ`, then `Axis(M)` is `UNDEFINED`. Empty Axis is empty, not `UNDEFINED`.
The construction does not require Axis to be a singleton. Axis is unsigned:
`+e_i` and `−e_i` occupy the same axis. Leftover of `M` alone is
`{e_1,e_2,e_3}` minus `Axis(M)`, a different object. Leftover of `M` and
`O` together is a different object. Existential opposite of signed locks in
`M` is a different object.

Reverse incoming-axis holds if and only if `Axis(M)(A)` and `Axis(M)(B)`
are defined, equal as sets, and nonempty. Face incoming-axis holds if and
only if `Axis(M)(C)` and `Axis(M)(D)` are defined, equal as sets, and
nonempty. Empty Axis on either side of a comparison fails; it is not
`UNDEFINED`. Either side `UNDEFINED` is `UNDEFINED`. Nonempty unequal
axis sets fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying existential opposite of
signed locks with incoming-axis reverse is refused: incoming-axis reverse
is equality of nonempty unsigned `Axis(M)` sets.

Investment nmperp: forall-perp of `M` versus `O` at `t+1` HOLDs reverse and
face. Investment leftover-axis: leftover of `Axis(M)` union `Axis(O)` is
empty at each of the four y-probes (3-axis cover), and leftover reverse
fails and leftover face fails. Those investments are not this object. This
display reads `Axis(M)` alone at `τ=t+1` and scores equality of those
nonempty incoming-axis sets.

## Theorem 1 — ticks, `M`, and `Axis(M)` at `τ=t+1`

On this process the four y-probes form. Compare to nsmopp and nmt2opp: those
leftovers report signed `M` with exist-opposite reverse hold and face hold.
This display reads unsigned incoming axis of those same timed sets:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_2, +e_3, −e_3}
Axis(M)(A, τ) = {e_1}
Axis(M)(B, τ) = {e_1}
Axis(M)(C, τ) = {e_2}
Axis(M)(D, τ) = {e_2, e_3}
```

`A` is a seed at tick 0. Mixed remains a set: `M(D,τ)` has three earliest
incoming steps `−e_2`, `+e_3`, and `−e_3`. Unique letters would assign
`UNDEFINED` at mixed `D`. Here uniqueness is not required. `M` at `τ=t+1`
equals `M` at `t` on each of the four y-probes: new records in `B_3(0)`
between `t` and `t+1` that meet a probe's six-neighbors are later arrivals
and do not enter earliest `M`.

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

Leftover of `M` alone at `A` and at `B` is `{e_2, e_3}`, nonempty and
equal. That one-sided leftover is not `Axis(M)`: `Axis(M)` at `A` and at
`B` is `{e_1}`. Leftover of `M` and `O` is empty at each probe. Empty
leftover of the union is not incoming-axis of `M`.

## Theorem 2 — reverse from incoming-axis agreement at `τ`

Reverse incoming-axis holds if and only if `Axis(M)(A)` and `Axis(M)(B)`
are defined, equal as sets, and nonempty. Both axis sets are `{e_1}`.
Reverse holds.

Reverse incoming-axis agreement at τ: hold

Both sides are defined and nonempty, so this is not `fail` and not
`UNDEFINED`. Exist-opposite reverse of signed `M` also holds, from
`−e_1` against `+e_1`. That leftover is signed opposite, not unsigned
axis equality. Leftover-of-`M` reverse would hold because leftover of
`M` at `A` and at `B` is `{e_2, e_3}`. Those leftovers are not this
display. Reverse HOLD uses nonempty equal `Axis(M)` at `A` and at `B`.

Reverse holds.

## Theorem 3 — face from incoming-axis agreement at `τ`

Face incoming-axis holds if and only if `Axis(M)(C)` and `Axis(M)(D)`
are defined, equal as sets, and nonempty. `Axis(M)(C,τ)={e_2}` and
`Axis(M)(D,τ)={e_2, e_3}` are both nonempty and unequal. Face fails.

Face incoming-axis agreement at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `UNDEFINED`. Exist-opposite face of signed `M` holds, from
`+e_2` against `−e_2` inside mixed `M(D,τ)`. That leftover is signed
opposite, not unsigned axis equality. Leftover-of-`M` face would fail
because leftover of `M` at `C` is `{e_1, e_3}` and leftover of `M` at
`D` is `{e_1}`: nonempty and unequal. Leftover of `M` and `O` is empty
at `C` and at `D`, so leftover-axis face fails from empty leftover.
This display scores incoming-axis equality of `Axis(M)`, which is
nonempty and unequal at `C` and at `D`, so face fails.

Empty Axis does not arise at these four y-probes. Empty Axis would fail
reverse or face by declaration, and would not be `UNDEFINED`.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock or a unique incoming axis.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require `Axis(M)` to be a singleton.
- It does not sum the incoming set.
- It does not replace `Axis(M)` by leftover of `M` alone.
- It does not replace `Axis(M)` by leftover of `O` alone.
- It does not replace `Axis(M)` by leftover of `M` and `O`.
- It does not replace incoming-axis equality by existential opposite of
  signed locks.
- It does not replace `M` by outgoing dual `O`.
- It does not replace `Axis(M)` by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this reverse.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint forall-perp of `M` versus `O`.
- It does not reprint leftover axis of `M` and `O` as this letter.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
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

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock two-site process, incoming axis of `M` at `t+1`, and the
reverse/face bits from incoming-axis equality are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `Axis(M)` at `τ` | Theorem 1; `{e_1}`, `{e_1}`, `{e_2}`, `{e_2, e_3}` |
| reverse from incoming-axis agreement at `τ` | Theorem 2; `hold` |
| face from incoming-axis agreement at `τ` | Theorem 3; `fail` |
| unique incoming axis | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of exist-opposite of signed `M` | not this incoming-axis display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of leftover axis of `M` and `O` | not this display |
| leftover of forall-perp of `M` versus `O` | not this display |
| leftover of nmsimopp exist-opposite HOLD | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| incoming-axis equality as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: incoming-axis agreement of `M` at `t+1` on the four #7208 y-probes, and reverse/face from that. |
| V2 | Current main has no landed incoming-axis-agreement reverse/face of timed `M` on these four #7208 y-probes. |
| V3 | Incoming axis sets at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned incoming axis of own incoming at the `t+1` cut and scores equality of nonempty `Axis(M)` sets. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique incoming axis, does not replace `Axis(M)` by leftover of `M` alone
or leftover of `M` and `O`, does not replace incoming-axis equality by
existential opposite of signed locks, does not identify this display with
forall-perp HOLD, and does not identify it with leftover-axis empty. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and `B` is `{e_2,e_3}`; `Axis(M)` at `A` and `B` is `{e_1}`; reverse bits coincide, the scored sets do not | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and `B` is `{e_1}` equal to `Axis(M)` there; face leftover of `O` is `{e_2}` versus `{e_2,e_3}`, a different object from `Axis(M)` | ATTEMPTED |
| leftover axis of `M` and `O` | score empty leftover of the 3-axis cover | leftover reverse fails and leftover face fails because leftover is empty; incoming-axis reverse holds | ATTEMPTED |
| forall-perp of `M` versus `O` | reuse forall-orthogonal HOLD of `M` against `O` | forall-perp HOLDs reverse and face; incoming-axis face fails | ATTEMPTED |
| exist-opposite of signed `M` | score `a+b=(0,0,0)` inside `M(A)` and `M(B)` | exist-opposite reverse holds and face holds; incoming-axis face fails because `{e_2}≠{e_2,e_3}` | ATTEMPTED |
| nmsimopp exist-opposite | reuse signed reverse hold and face hold of `M` and of `O` | those bits HOLD; incoming-axis face fails | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; incoming axis is unsigned occupied axes of `M` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(D,τ)` remains a set; `Axis(M)(D,τ)={e_2,e_3}` | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes `+e_1` at `A` from the origin partner; incoming axis is unsigned occupied directions of own `M` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores `Axis(M)` at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports incoming-axis reverse hold and face fail | ATTEMPTED |
| sum of a set | replace Axis by a `Z^3` sum | the construction does not sum; Axis is a set of unsigned axes | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by incoming-axis equality | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `Axis(M)` with leftover
of `M` alone, missing identification of incoming-axis equality with
existential opposite of signed locks, and missing Record identification of
incoming-axis reverse are distinct open premises. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, own incoming set from records with tick `<= τ`,
per-probe `τ=t+1`, unsigned axis of `M`, empty Axis fail not `UNDEFINED`,
four y-probes with seed `A`, and mixed remains a set are declared. No
uniqueness of incoming axes, no six-neighbor lock union as the scored
object, no lock-count clock, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
incoming-axis `hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned incoming lattice axis among `{e_1,e_2,e_3}` occupied by `M` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming axis sets, reverse/face from incoming-axis equality | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for incoming-axis reverse/face,
a formation-rate rule, and a physical selector among `{e_1,e_2,e_3}`. None is
taken here.

### N7 — hostile steelman

**Steelman:** Incoming-axis reverse hold is only leftover of `M` alone, because
leftover of `M` at `A` and at `B` is `{e_2,e_3}` and that leftover reverse
also holds; face fail is only leftover of `M` alone, which also fails face;
exist-opposite already answered reverse from `−e_1` against `+e_1`; leftover
of `M` and `O` already covered all three axes; and mixed `D` should make
`Axis(M)` `UNDEFINED`.

**Answer:** Leftover of `M` alone is the complement of `Axis(M)` inside
`{e_1,e_2,e_3}`. Complement equality can coincide with `Axis(M)` equality
on a pair while the scored sets differ: leftover of `M` at `A` is
`{e_2,e_3}` and `Axis(M)` at `A` is `{e_1}`. Exist-opposite reverse holds
from signed opposite letters; incoming-axis reverse holds from unsigned
axis equality of `{e_1}` with `{e_1}`. Exist-opposite face holds from
`+e_2` against `−e_2` while `Axis(M)` at `C` and at `D` is nonempty and
unequal, so incoming-axis face fails. Leftover of `M` and `O` is empty
because those sets occupy complementary axes; empty leftover is not
`Axis(M)`. Mixed `M(D,τ)` remains a set and `Axis(M)(D,τ)={e_2,e_3}` is
defined. Uniqueness is not required.

### N8 — cross-cycle echo

nsmopp #7208 reported reverse hold and face hold from own incoming `M`.
nmt2opp reported `M` at `t` equal to `M` at `t+1`, reverse hold, face hold,
and composition HOLD. nmsimopp reported `M` and `O` together at `τ=t+1`,
empty letter intersection, reverse hold and face hold from `M`, and reverse
hold and face hold from `O`. nmperp reported forall-perp HOLD. leftover-axis
reported empty leftover of `M` and `O` at each of the four y-probes, reverse
fail, and face fail. This note is not those displays: it reports incoming
axis of `M` at `τ=t+1`, reverse hold from `{e_1}={e_1}`, and face fail from
`{e_2}≠{e_2,e_3}`.

**Gate disposition:** PASS for the incoming-axis `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover of `M` alone,”
“the predicate equals leftover of `M` and `O`,” “the predicate equals
exist-opposite of signed `M`,” “the predicate equals nmsimopp exist-opposite
HOLD,” “the predicate equals forall-perp HOLD,” “bits are Admissibility,”
“reverse incoming-axis fails,” “face incoming-axis holds,” or “empty Axis
is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each probe's own earliest incoming set from the
record prefix at that probe's `t+1`, reports unsigned `Axis(M)`, lists new
records in `B_3(0)` between `t` and `t+1` that meet a probe's six-neighbors,
and checks Theorems 1--3. It also checks that reverse holds from equal
nonempty `{e_1}` at `A` and at `B`, that face fails from unequal nonempty
`{e_2}` and `{e_2,e_3}` at `C` and at `D`, that empty Axis fails reverse
and face and is not `UNDEFINED`, that leftover of `M` alone is a different
object, that exist-opposite of signed `M` HOLDs face while incoming-axis
face fails, that mixed sets remain sets, that the construction does not
sum, that a formation member from already-recorded six-neighbor locks is
not attached, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
