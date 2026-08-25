---
claim_id: two_axis_opposite_yprobe_neighbor_read_outgoing_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of O at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_neighbor_read_outgoing_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Own-Outgoing At t+1 Reverse And Face On Four Two-Axis Opposite Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of the outgoing dual `O` at each probe's `τ=t+1`,
and reverse/face from that neighbor-read, on the four y-probes of the
two-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same process and y-probes
as nm2axo. Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`.
There is no global T. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set
of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Neighbor-read HOLDs at formed `q` if and only if some formed
6-NN `r` has `O(r,τ)` defined and equal to `O(q,τ)` as sets. Unformed `q`
is `UNDEFINED`. Uniqueness is not required. Mixed remains a set. Reverse
HOLDs if and only if neighbor-read HOLDs at `A` and at `B`. Face HOLDs if
and only if neighbor-read HOLDs at `C` and at `D`. This is not leftover of
nm2axo timed-O exist-opposite. This is not leftover of nm2simy simultaneous
`M` and `O`. This is not leftover of nm2ready neighbor-read of M. This is
not leftover of nm2oreadz z-probe neighbor-read of `O`. This is not leftover
of R-style recovery of the outgoing step from neighbors. Occupancy of sites
is not used. Named-sign lettering is not used. Displayed, not adopted. Do
not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_neighbor_read_outgoing_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_neighbor_read_outgoing_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Neighbor-read asks whether a formed six-neighbor recovers that
outgoing set as a set, without being `O` itself. Reverse and face are
scored on neighbor-read HOLD at the paired probes. Named signs `{+,−}` are
a coarser readout and are not used. A singleton unique lock letter is a
different readout and is not used as the object. Existential opposite of
signed locks in `O` is a different readout and is not used. Simultaneous
nonempty disjoint `M` and `O` is a different readout and is not used.
Neighbor-read of `M` is a different readout and is not used. R-style
recovery of signed steps from a neighbor's `O` is a different readout and
is not used. A `Z^3` sum of those locks is a different readout and is not
used. Occupancy of sites is not used. A six-neighbor star is not the letter.
O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of O at t+1 on the four y-probes of the two-axis opposite seed, neighbor-read bits at each probe, reverse fail and face fail from those bits; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_neighbor_read_outgoing_tplus1_reverse_face
target_blocker_text: "display neighbor-read of O at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, HOLD iff some formed 6-NN recovers O as a set"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of O at t+1 displayed; do not write neighbor-read into Admissibility, do not reduce to neighbor-read of M, do not reduce to R-style recovery, do not reduce to timed-O exist-opposite or simultaneous M and O, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of O at t+1 on the four y-probes of the two-axis opposite seed and reverse/face from that; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose
neighbor-read of `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the first opposite pair.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. First pair:
`L(0)=+e_1` and `L(0,1,0)=−e_1`. Second pair: `L(0,0,1)=+e_2` and
`L(0,1,1)=−e_2`. The second pair is a new seed, not a formed child of the
first pair. This seed is not the one-axis opposite two-site seed alone.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.

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

## Named neighbor-read of `O` at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
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
not require `O` to be a singleton. It does not sum the set. It does not
replace `O` by `M`. It does not wait for a global later T. Occupancy of
sites is not used. O is not M.

Neighbor-read at a formed probe at the same cut:

```text
neighbor-read(q) HOLDs iff some formed 6-NN r has O(r,τ)
defined and equal to O(q,τ) as sets.
```

If `q` is unformed at `τ`, then neighbor-read is `UNDEFINED`. Else if no
formed six-neighbor recovers `O(q,τ)` as a set, neighbor-read fails. The
probe is not counted as its own neighbor. Empty matching is fail, not
`UNDEFINED`. Mixed remains a set: a mixed `O(q,τ)` may still match a mixed
`O(r,τ)`.

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Face neighbor-read holds if and only if neighbor-read HOLDs at `C`
and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD,
reverse or face HOLDs. Else fail.

Identifying neighbor-read of `O` with neighbor-read of `M` is refused: the
two bits disagree at `B` and at `D`. Identifying neighbor-read with R-style
recovery of signed steps from a neighbor's `O` is refused: R-style recovers
a different set. Identifying neighbor-read with nm2axo timed-O
exist-opposite is refused: that leftover HOLDs reverse and HOLDs face.
Identifying neighbor-read with nm2simy simultaneous `M` and `O` is refused:
that leftover also HOLDs reverse and HOLDs face.

## Theorem 1 — ticks, `O` at probes and formed 6-NN, neighbor-read bit

On this process the four y-probes form. Compare to neighbor-read of `M`:
that leftover reports fail at `A` and at `C` and hold at `B` and at `D`.
This display reads whether a formed six-neighbor recovers the outgoing dual
as a set:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
O(A, τ) = {+e_2, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
neighbor-read(A) = fail
neighbor-read(B) = fail
neighbor-read(C) = fail
neighbor-read(D) = fail
formed 6-NN of A at τ: (1, 1, 0)=UNDEFINED, (-1, 1, 0)=UNDEFINED, (0, 2, 0)={}, (0, 0, 0)={−e_2, −e_3}, (0, 1, 1)={+e_1, −e_1, +e_3}, (0, 1, -1)={}
formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)={+e_1, −e_1, +e_3}, (1, 2, 1)={}, (1, 0, 1)={−e_2, +e_3, −e_3}, (1, 1, 2)={}, (1, 1, 0)={−e_1}
formed 6-NN of C at τ: (1, 2, 0)={}, (-1, 2, 0)={}, (0, 1, 0)={+e_2, −e_3}, (0, 2, 1)={−e_2}, (0, 2, -1)={}
formed 6-NN of D at τ: (2, 1, 0)={}, (0, 1, 0)={+e_2, −e_3}, (1, 2, 0)={−e_3}, (1, 0, 0)={+e_1}, (1, 1, 1)={+e_2, +e_3, −e_3}, (1, 1, -1)={+e_2, −e_3}
matching 6-NN of A: none
matching 6-NN of B: none
matching 6-NN of C: none
matching 6-NN of D: none
```

`A` is a seed at tick 0 with seed letter `−e_1`. The partner of that pair,
the origin, is also a seed at tick 0 with seed letter `+e_1`. At `τ=1`
those two seeds do not share an outgoing set: `O(A,τ)={+e_2, −e_3}` while
`O(0,τ)={−e_2, −e_3}`. The second-pair seed `(0,1,1)` carries
`{+e_1, −e_1, +e_3}`, also unequal. Empty `O` at a formed neighbor is
defined empty, not `UNDEFINED`, and is not equal to nonempty probe `O`.
Sites `(1,1,0)` and `(-1,1,0)` form later, at tick 2, and are `UNDEFINED`
at `A`'s `τ`. Mixed remains a set: `O(A,τ)` has two outgoing steps, and
unique letters would assign `UNDEFINED`; uniqueness is not required, and
neighbor-read still fails because no formed six-neighbor equals that mixed
set. At `t`, `O` is empty at `A`, `B`, and `C`, and is `{−e_1}` at `D`. At
`τ=t+1`, `O` is nonempty and differs from the value at `t`. `M` is frozen
from `t` to `t+1`; `O` is not. O is not M.

On the one-axis opposite two-site seed, `t(B)=2` and `t(D)=3`, and
`(0,0,1)` and `(0,1,1)` are formed children locking `+e_3`. Here both of
those sites are seeds of a second opposite pair on a second axis, and the
y-probe ticks are `t(B)=1` and `t(D)=2`. Neighbor-read of `O` on that
leftover seed still fails at each y-probe, but the ticks and the second
pair's lock letters differ.

Empty matching is fail, not `UNDEFINED`. All four y-probes are formed, so
neighbor-read is defined at each.

## Theorem 2 — reverse from neighbor-read of `O` at `τ`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read fails at `A` and fails at `B`. Reverse fails. This is
HOLD iff neighbor-read at both reverse probes, not leftover of neighbor-read
of `M`, not leftover of nm2axo timed-O, and not leftover of nm2simy
simultaneous.

Reverse neighbor-read at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Neighbor-read of `M`
also has reverse fail, but from a different pair of bits: fail at `A` and
hold at `B`. Timed-O exist-opposite reverse HOLDs. Simultaneous reverse
HOLDs. R-style recovery of `O` is unequal to `O` at each reverse probe.
Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from neighbor-read of `O` at `τ`

Face neighbor-read holds if and only if neighbor-read HOLDs at `C` and at
`D`. Neighbor-read fails at `C` and at `D`. Face fails.

Face neighbor-read at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Neighbor-read of `M` has face fail from fail at `C` and hold at `D`.
Timed-O exist-opposite face HOLDs. Simultaneous face HOLDs. This display
scores neighbor-read of `O`, which fails at `C` and at `D`, so face fails.

On the same seed the four z-probes give neighbor-read hold at `A` and fail
at `B`, `C`, and `D`, so reverse fail and face fail, but from hold at
z-probe `A`, not fail at y-probe `A`. The four x-probes fail at each probe
and have a different outgoing set at x-probe `A`. Those probe-direction
readouts are not this y-probe display.

Face fails.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum either set.
- It does not replace neighbor-read of `O` by neighbor-read of `M`.
- It does not replace neighbor-read by R-style recovery of signed steps.
- It does not replace neighbor-read by nm2axo timed-O exist-opposite.
- It does not replace neighbor-read by nm2simy simultaneous `M` and `O`.
- It does not replace `O` by `M`.
- It does not replace neighbor-read by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2axo timed-O reverse hold and face hold.
- It does not reprint nm2simy simultaneous reverse hold and face hold.
- It does not reprint nm2ready neighbor-read of `M`.
- It does not reprint nm2oreadz z-probe neighbor-read of `O`.
- It does not treat the second opposite pair as a formed child of the first.
- It does not score the z-probes or the x-probes as this letter.
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
two-axis opposite process, neighbor-read of `O` at `t+1`, and the reverse/face
bits from that neighbor-read are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint opposite pairs `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| `O` at formed 6-NN | Theorem 1; reported at each eventually-formed neighbor |
| neighbor-read bit at `τ` | Theorem 1; fail, fail, fail, fail |
| reverse from neighbor-read at `τ` | Theorem 2; `fail` |
| face from neighbor-read at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2axo timed-O exist-opposite | not this neighbor-read display |
| leftover of nm2simy simultaneous | not this neighbor-read display |
| leftover of nm2ready neighbor-read of `M` | not this display |
| leftover of nm2oreadz z-probe neighbor-read | not this display |
| leftover of R-style recovery | not this display |
| one-axis opposite leftover of the second pair | not this seed |
| z-probe or x-probe neighbor-read on this seed | not this letter |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of `O` at `t+1` on the four y-probes of the two-axis opposite seed, and reverse/face from that. |
| V2 | Current main has no landed neighbor-read reverse/face of timed `O` on these four y-probes of this two-axis opposite seed. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads whether a formed six-neighbor recovers own outgoing as a set at the same `t+1` cut. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read of `O` by neighbor-read of `M`,
does not replace neighbor-read by R-style recovery, and does not identify
this display with timed-O exist-opposite or simultaneous `M` and `O`. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| neighbor-read of `M` | score reverse/face from equal incoming sets | neighbor-read of `M` is fail/hold/fail/hold; neighbor-read of `O` is fail/fail/fail/fail | ATTEMPTED |
| R-style recovery | recover `e` by `(-e)` in `O(q+e)` | R-style of `O` is empty at `A`, `{−e_1}` at `B`, `{−e_2}` at `C`, `{+e_3}` at `D`; none equals `O` | ATTEMPTED |
| nm2axo timed-O | reuse exist-opposite reverse hold and face hold | timed-O HOLDs reverse and HOLDs face; neighbor-read of `O` fails both | ATTEMPTED |
| nm2simy simultaneous | reuse simultaneous reverse hold and face hold | simultaneous HOLDs at each y-probe; neighbor-read of `O` fails at each | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O` remains a set; neighbor-read still fails at each y-probe | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the outgoing set | ATTEMPTED |
| z-probe neighbor-read | score the four z-probes on this seed | z-probe neighbor-read HOLDs at `A`; this letter fails at y-probe `A` | ATTEMPTED |
| x-probe neighbor-read | score the four x-probes on this seed | x-probe `A` has `O={+e_1}` and `t=2`; y-probe `A` has `O={+e_2, −e_3}` and `t=0` | ATTEMPTED |
| one-axis leftover | treat `(0,0,1)` and `(0,1,1)` as formed children of `+e_1/−e_1` | those children lock `+e_3` at tick 1; here they are seeds locking `+e_2/−e_2` at tick 0 | ATTEMPTED |
| sum of a set | replace neighbor-read by a `Z^3` sum | the construction does not sum; equality is set equality of `O` | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by neighbor-read of `O` | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read of `O`
with neighbor-read of `M`, missing identification with R-style recovery,
missing identification with timed-O exist-opposite, and missing Record
identification of neighbor-read reverse are distinct open premises. This
note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite-pair seed locks `+e_1`, `−e_1`,
`+e_2`, and `−e_2`, perpendicular step rule, incoming-step lock, own
outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
neighbor-read as set equality of `O` at some formed six-neighbor, four
y-probes with seed `A`, and mixed remains a set are declared. No uniqueness
of outgoing locks, no six-neighbor lock union as the scored object, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read `hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest outgoing lock set `O` at a probe and at formed 6-NN, compared as sets at the probe's `t+1` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports, reverse/face from those bits | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read reverse/face,
a formation-rate rule, and a physical selector among matching neighbors.
None is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read FAIL of `O` is only the partner seed not sharing
a lock; neighbor-read of `M` already asked whether a neighbor recovers a
lock set and already has reverse fail and face fail; R-style already
recovers outgoing steps from neighbors; timed-O already uses `O`;
simultaneous already uses `O`; empty `O` at a neighbor should be
`UNDEFINED`; and reverse fail is only leftover of nm2ready reverse fail.

**Answer:** The partner seed at the origin has `O={−e_2, −e_3}`, unequal to
`O(A,τ)={+e_2, −e_3}`. Neighbor-read of `M` fails at `A` and `C` and HOLDs
at `B` and `D`. Neighbor-read of `O` fails at each y-probe. R-style recovers
`{ }` at `A`, `{−e_1}` at `B`, `{−e_2}` at `C`, and `{+e_3}` at `D`, none
equal to `O`. Timed-O exist-opposite HOLDs reverse and HOLDs face from
opposite pairs inside the probe's own `O`. Simultaneous HOLDs at each
y-probe from nonempty disjoint `M` and `O`. Empty `O` at a formed neighbor
is empty, not `UNDEFINED`, and does not match nonempty `O` at `τ`. Reverse
fail of neighbor-read of `M` is fail at `A` with hold at `B`. Reverse fail
here is fail at `A` with fail at `B`.

### N8 — cross-cycle echo

Investment names `nm2simy` and `nm2axo` mark nearby displayed processes.
nm2axo reported timed-O exist-opposite HOLD at reverse and HOLD at face on
these same y-probes. nm2simy reported simultaneous HOLD at each of those
probes, reverse hold, and face hold. nm2ready reported neighbor-read of `M`
fail at `A` and `C` and hold at `B` and `D`, reverse fail, and face fail.
nm2oreadz reported neighbor-read of `O` hold only at z-probe `A`. This note
is not those displays: it reports neighbor-read of `O` at `τ=t+1` on the
four y-probes of the two-axis opposite seed, fail at each probe, reverse
fail, and face fail.

**Gate disposition:** PASS for the neighbor-read of `O` `t+1` reverse/face
reports above. FAIL / DO NOT SHIP for “the predicate equals the named sign,”
“the predicate equals the unique singleton lock vector,” “the predicate
equals six-neighbor lock union,” “the predicate equals neighbor-read of
`M`,” “the predicate equals R-style recovery,” “the predicate equals
nm2axo timed-O,” “the predicate equals nm2simy simultaneous,” “bits are
Admissibility,” “neighbor-read of `O` HOLDs at a y-probe,” “reverse
neighbor-read HOLDs,” or “face neighbor-read HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each y-probe's own outgoing dual
from the record prefix at that probe's `t+1`, reads `O` at each eventually-
formed six-neighbor at the same cut, reports neighbor-read as set equality
at some formed six-neighbor, and checks Theorems 1--3. It also checks that
neighbor-read fails at each y-probe, that neighbor-read of `M` is a
different pattern, that R-style recovery is a different set, that timed-O
exist-opposite HOLDs reverse and face, that simultaneous HOLDs reverse and
face, that mixed sets remain sets, that unique-letter neighbor-read is not
required at mixed `O`, that the construction does not sum, that a formation
member from already-recorded six-neighbor locks is not attached, that the
second pair is a seed and not a formed child, and that the display is not
the z-probe or x-probe neighbor-read. No runner cache is written.
