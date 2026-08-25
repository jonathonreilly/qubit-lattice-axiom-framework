---
claim_id: two_axis_opposite_xprobe_neighbor_read_incoming_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of M at t+1 on the four x-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xprobe_neighbor_read_incoming_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Incoming M At t+1 Reverse And Face On Four Two-Axis Opposite X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of earliest incoming set `M` at each probe's
`τ=t+1`, and reverse/face from that neighbor-read, on the four x-probes of
the two-axis opposite seed in `B_3(0)={n:n·n<=9}`, no global T. Same process
and x-probes as nm2axpx. Let `t(q)` be the formation tick of probe `q`. Let
`τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton seed
letter. Unformed at `τ` is `UNDEFINED`. For a formed neighbor `r=q+e`,
report `M(r,τ)`. Neighbor-read HOLDs at `q` if and only if some formed
six-neighbor `r` has `M(r,τ)` defined and equal to `M(q,τ)` as sets.
Unformed `q` is `UNDEFINED`. Reverse HOLDs if and only if neighbor-read
HOLDs at `A` and at `B`. Face HOLDs if and only if neighbor-read HOLDs at
`C` and at `D`. This is the first neighbor-read of `M` at `t+1` on the
nm2axpx forall-perp HOLD x-probe direction of the two-axis opposite seed.
This is not leftover of nm2axpx forall-perp. This is not leftover of nm2axx
axis-cover. This is not leftover of two-axis same-lock z-probe
neighbor-read. This is not leftover of two-axis same-lock x-probe
neighbor-read. This is not leftover of R-style recovery of the incoming
step from neighbors. Uniqueness is not required. Mixed remains a set.
Occupancy `n` is not used. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xprobe_neighbor_read_incoming_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xprobe_neighbor_read_incoming_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Neighbor-read compares those incoming sets as sets at a formed
six-neighbor. Reverse and face are scored on neighbor-read HOLD at the
paired probes. Named signs `{+,−}` are a coarser readout and are not used.
A singleton unique lock letter is a different readout and is not used as
the object. R-style recovery of the incoming step as `−e` in `M(q+e,τ)` is
a different readout and is not used. Forall-perp of `M` versus outgoing
dual `O` is a different readout and is not used. Axis-cover of `M` and `O`
is a different readout and is not used. Occupancy of sites is not used.
This display does not use occupancy. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of M at t+1 on the four x-probes of the two-axis opposite seed, HOLD at A from matching D, HOLD at B,C,D, reverse hold and face hold from those bits; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xprobe_neighbor_read_incoming_tplus1_reverse_face
target_blocker_text: "display neighbor-read of M at t+1 on the four x-probes of the two-axis opposite seed, compare to nm2axpx forall-perp and to same-lock neighbor-read, HOLD iff some formed 6-NN recovers M as a set"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of M at t+1 displayed; do not write the bits into Admissibility, do not reduce to R-style recovery, do not reduce to nm2axpx forall-perp, do not reduce to nm2axx cover leftover, do not replace the display by two-axis same-lock neighbor-read, do not require a unique letter, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of M at t+1 on the four x-probes of the two-axis opposite seed and reverse/face from that; displayed, not adopted"
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
neighbor-read of `M` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. Same process and x-probes as nm2axpx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. The first
pair is `{0, (0,1,0)}` with opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`.
The second pair is `{(0,0,1), (0,1,1)}` with opposite locks `L(0,0,1)=+e_2`
and `L(0,1,1)=−e_2`. The second pair is a new seed, not a formed child of
the first pair. On the one-axis opposite two-site process the sites
`(0,0,1)` and `(0,1,1)` form at tick 1 locking `+e_3`; here they are seeds
at tick 0 locking `+e_2` and `−e_2`. This seed is not the two-axis same-lock
seed `+e_1/+e_1` and `+e_2/+e_2`. This seed is not the perp two-site seed
`+e_1/+e_2`. This seed is not the z-symmetric three-site seed
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

## Named neighbor-read of `M` at `τ=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

Neighbor-read at a formed probe at the same cut:

```text
neighbor-read(q) HOLDs iff some formed 6-NN r has M(r,τ)
defined and equal to M(q,τ) as sets.
```

If `q` is unformed at `τ`, then neighbor-read is `UNDEFINED`. Empty match
fails. Mixed remains a set: equality is set equality, not a unique-letter
reduction. Occupancy of sites is not used. The construction does not require
`M` to be a singleton. It does not sum the set. It does not wait for a
global later T.

R-style recovery is a different object: the set of steps `e` such that
`−e` lies in `M(q+e,τ)`. Forall-perp of `M` versus outgoing dual `O` is a
different object. Axis-cover of `M` and `O` is a different object.

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Face neighbor-read holds if and only if neighbor-read HOLDs at `C`
and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD,
reverse or face HOLDs. Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the set. Identifying R-style recovery with
neighbor-read is refused: at `A`, R-style is `{−e_1}` while `M(A,τ)={−e_3}`;
at `C`, R-style is `{+e_3}` while `M(C,τ)={+e_1}`; at `B` and at `D`,
R-style is empty while neighbor-read HOLDs. Identifying nm2axpx forall-perp
with this reverse/face is refused: forall-perp scores every incoming letter
against every outgoing dual letter at one probe; neighbor-read scores
set-equality of own incoming `M` at a formed six-neighbor. Identifying
nm2axx axis-cover with this reverse/face is refused: nm2axx cover fails at
`A` and at `D` and fails reverse and face; this member HOLDs at each
x-probe and HOLDs reverse and face. Identifying two-axis same-lock z-probe
neighbor-read with this reverse is refused: that leftover has seed `A` at
tick 0 with `M={+e_2}`; here `A` is not a seed, `t(A)=2`, and
`M(A,τ)={−e_3}`. Identifying two-axis same-lock x-probe neighbor-read with
this reverse is refused: same-lock x-probes also HOLD reverse and face, but
`M((0,1,1),τ)` there is `{+e_2}` while here it is `{−e_2}`, and
`M((0,1,0),τ)` there is `{+e_1}` while here it is `{−e_1}`.

## Theorem 1 — ticks, `M` at probes and at formed 6-NN, and neighbor-read bit

On this process the four x-probes form. Incoming is frozen at formation:
`M(q,t+1)=M(q,t)` at every scored probe. Compare to nm2axpx forall-perp:
that leftover HOLDs reverse and face by scoring integer dots of `M` versus
`O`. Here `M` is read at the same cut `τ=t+1` and scored by set-equality
at a formed six-neighbor. Neighbor-read HOLDs at `A`, at `B`, at `C`, and
at `D`. Reverse HOLDs. Face HOLDs. The match at `A` is `D=(1,1,0)` with
the same letter `{−e_3}`. The match at `D` is `A=(1,0,0)` with the same
letter `{−e_3}`.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ) = {−e_3}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {−e_3}
neighbor-read(A) = hold
neighbor-read(B) = hold
neighbor-read(C) = hold
neighbor-read(D) = hold
formed 6-NN of A at τ: (2, 0, 0)={+e_1}, (0, 0, 0)={+e_1}, (1, 1, 0)={−e_3}, (1, -1, 0)={+e_1}, (1, 0, 1)={+e_1}, (1, 0, -1)={+e_1}
formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)={−e_2}, (1, 2, 1)={+e_2}, (1, 0, 1)={+e_1}, (1, 1, 2)={+e_1, +e_3}, (1, 1, 0)={−e_3}
formed 6-NN of C at τ: (1, 0, 0)={−e_3}, (2, 1, 0)={+e_1}, (2, -1, 0)={−e_2, −e_3}, (2, 0, 1)={+e_2, +e_3, −e_3}, (2, 0, -1)={−e_3}
formed 6-NN of D at τ: (2, 1, 0)={+e_1}, (0, 1, 0)={−e_1}, (1, 2, 0)={+e_1}, (1, 0, 0)={−e_3}, (1, 1, 1)={+e_1}, (1, 1, -1)={+e_1}
matching 6-NN of A: (1, 1, 0)
matching 6-NN of B: (1, 0, 1)
matching 6-NN of C: (2, 1, 0)
matching 6-NN of D: (1, 0, 0)
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `M((1,1,2),τ)` at `B`'s cut is
`{+e_1, +e_3}`, and `M((2,0,1),τ)` at `C`'s cut is `{+e_2, +e_3, −e_3}`.
Unique letters would assign `UNDEFINED` at those mixed neighbors. Here
uniqueness is not required. `M` is frozen from `t` to `τ=t+1` at each of
the four x-probes. Unformed six-neighbors remain `UNDEFINED` at the cut
and do not match.

On the two-axis same-lock seed with the same x-probes, neighbor-read also
HOLDs reverse and face with the same ticks and the same probe letters, but
the formed neighbor `(0,1,1)` of `B` locks `{+e_2}` and the formed
neighbor `(0,1,0)` of `D` locks `{+e_1}`. Here those neighbors lock
`{−e_2}` and `{−e_1}` because the pairs are opposite. That leftover is
not this display.

On the two-axis same-lock z-probes, `A=(0,0,1)` is a seed at tick 0 with
`M={+e_2}`, and neighbor-read HOLDs reverse and face from the same-lock
partner seed. Here `A` is not a seed.

On the two-axis opposite z-probes, neighbor-read fails at `A` because the
partner seed `(0,1,1)` locks `−e_2`, unequal to `M(A,τ)={+e_2}`. That
leftover fails reverse. This member HOLDs reverse on the x-probes.

On the 1-axis same-lock two-site seed, `t(A)=3` with mixed `M`,
neighbor-read fails at `A` and at `D`, and reverse and face fail. That is
leftover of the first pair. Here the second pair is a new opposite seed,
`t(A)=2`, and reverse and face HOLD.

## Theorem 2 — reverse from neighbor-read at `τ`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read HOLDs at `A` and HOLDs at `B`. Reverse HOLDs.

Reverse neighbor-read at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Two-axis opposite
z-probe neighbor-read reverse fails because neighbor-read fails at seed
`A`. Two-axis opposite y-probe neighbor-read reverse fails. nm2axx
axis-cover reverse fails because cover fails at `A` from a union that
misses e_2. R-style recovery at `A` is `{−e_1}`, not equal to
`M(A,τ)={−e_3}`, and R-style at `B` is empty. Those leftovers are not
this display.

Reverse holds.

## Theorem 3 — face from neighbor-read at `τ`

Face neighbor-read holds if and only if neighbor-read HOLDs at `C` and at
`D`. Both neighbor-reads HOLD. Face HOLDs.

Face neighbor-read at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Face holds.

On the same seed the four y-probes give reverse fail and face fail. The
four z-probes give reverse fail and face hold, with seed `A` at tick 0.
Those probe-direction readouts are not this x-probe display.

nm2axx cover face fails because cover fails at `D`. 1-axis same-lock face
fails. Two-site opposite leftover face fails. Z-symmetric leftover fails
at `A` and HOLDs face. Those leftovers are not this display.

Face holds.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum the incoming set.
- It does not replace neighbor-read by R-style recovery.
- It does not replace neighbor-read by nm2axpx forall-perp.
- It does not replace neighbor-read by nm2axx axis-cover.
- It does not replace neighbor-read by two-axis same-lock z-probe neighbor-read.
- It does not replace neighbor-read by two-axis same-lock x-probe neighbor-read.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint 1-axis same-lock neighbor-read as this member.
- It does not reprint two-axis opposite y-probe neighbor-read.
- It does not reprint two-axis opposite z-probe neighbor-read.
- It does not treat the second opposite pair as a formed child of the first.
- It does not score the y-probes or the z-probes as this letter.
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
two-axis opposite four-site process, neighbor-read of `M` at `t+1`, and the
reverse/face bits from that neighbor-read are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `M` at formed 6-NN | Theorem 1; `D` matches `A` on `{−e_3}` |
| neighbor-read bit at `τ` | Theorem 1; HOLD at `A`,`B`,`C`,`D` |
| reverse from neighbor-read at `τ` | Theorem 2; `hold` |
| face from neighbor-read at `τ` | Theorem 3; `hold` |
| compare to nm2axpx forall-perp | Theorem 1; forall-perp HOLDs reverse/face by `M` versus `O` dots; this member HOLDs by set-equality of `M` at a formed 6-NN |
| compare to nm2axx cover | Theorem 1; cover reverse FAIL face FAIL; neighbor-read reverse HOLD face HOLD |
| compare to two-axis same-lock z-probe neighbor-read | Theorem 1; same-lock z has seed `A` at tick 0 with `M={+e_2}`; here `t(A)=2` and `M={−e_3}` |
| compare to two-axis same-lock x-probe neighbor-read | Theorem 1; same-lock x HOLDs reverse/face but neighbor `M` at `(0,1,1)` and `(0,1,0)` differs by sign |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2axpx forall-perp | not this neighbor-read display |
| leftover of nm2axx axis-cover | not this display |
| leftover of two-axis same-lock z-probe neighbor-read | not this display |
| leftover of two-axis same-lock x-probe neighbor-read | not this display |
| leftover of R-style | not this display |
| leftover of 1-axis same-lock neighbor-read | not this display |
| leftover of y-probe neighbor-read | not this display |
| leftover of z-probe neighbor-read | not this display |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of `M` at `t+1` on the four x-probes of the two-axis opposite seed, compared to nm2axpx forall-perp and to same-lock neighbor-read, and reverse/face from those bits. |
| V2 | Current main has no landed neighbor-read reverse/face of timed `M` on these four two-axis opposite x-probes. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads set-equality of own incoming `M` at a formed six-neighbor at the same `t+1` cut. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read by R-style recovery, does not
replace neighbor-read by nm2axpx forall-perp, does not replace neighbor-read
by nm2axx axis-cover, and does not identify this display with two-axis
same-lock neighbor-read. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2axpx forall-perp | score every `m·o=0` of `M` versus `O` | forall-perp is incoming-versus-outgoing integer dots at one probe; neighbor-read is set-equality of `M` at a formed 6-NN; `O(A,τ)={+e_1}` is not `M(A,τ)={−e_3}` | ATTEMPTED |
| nm2axx axis-cover | reuse cover of `M` and `O` | cover fails at `A` and at `D` and fails reverse and face; neighbor-read HOLDs at each x-probe and HOLDs reverse and face | ATTEMPTED |
| two-axis same-lock z-probe neighbor-read | reuse seed `+e_1/+e_1` and `+e_2/+e_2` on z-probes | that leftover has seed `A` at tick 0 with `M={+e_2}`; here `A` is not a seed, `t(A)=2`, and `M={−e_3}` | ATTEMPTED |
| two-axis same-lock x-probe neighbor-read | reuse same-lock pairs on these x-probes | same-lock x HOLDs reverse/face, but `M((0,1,1),τ)={+e_2}` and `M((0,1,0),τ)={+e_1}` there; here those neighbors lock `{−e_2}` and `{−e_1}` | ATTEMPTED |
| R-style recovery | recover incoming as `−e` in `M(q+e,τ)` | R-style at `A` is `{−e_1}` unequal to `{−e_3}`; at `C` is `{+e_3}` unequal to `{+e_1}`; at `B` and at `D` it is empty while neighbor-read HOLDs | ATTEMPTED |
| 1-axis same-lock neighbor-read | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` | 1-axis fails reverse and face with `t(A)=3`; here `t(A)=2` and reverse and face HOLD | ATTEMPTED |
| two-site opposite leftover | reuse opposite `+e_1/−e_1` without the second pair | that leftover fails reverse and face; this member HOLDs face from four opposite seeds | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed neighbor `M((1,1,2),τ)={+e_1,+e_3}` remains a set; unique-letter is `UNDEFINED` while neighbor-read HOLDs at `B` | ATTEMPTED |
| y-probe neighbor-read | score the four y-probes on this seed | y-probe reverse fails and face fails; this letter is the four x-probes | ATTEMPTED |
| z-probe neighbor-read | score the four z-probes on this seed | z-probe reverse fails because seed `A` has partner letter `−e_2`; this letter has non-seed `A` at tick 2 | ATTEMPTED |
| z-symmetric leftover | reuse seed `{0,(0,0,1),(0,0,-1)}` | that leftover fails at `A`; this member HOLDs at `A` | ATTEMPTED |
| perp two-site leftover | reuse seed `{0,(0,1,0)}` with `+e_1/+e_2` | perp fails at each x-probe; this member HOLDs reverse and face | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the set | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by neighbor-read | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read with
R-style recovery, missing identification of neighbor-read with nm2axpx
forall-perp, missing identification of neighbor-read with nm2axx
axis-cover, missing identification of this member with two-axis same-lock
neighbor-read, and missing Record identification of neighbor-read reverse
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite pairs with locks `+e_1`, `−e_1`,
`+e_2`, and `−e_2`, perpendicular step rule, incoming-step lock, own
incoming set from records with tick `<= τ`, per-probe `τ=t+1`,
neighbor-read as set-equality of `M` at a formed six-neighbor, four
x-probes with non-seed `A`, reverse as neighbor-read at `A` and `B`, face
as neighbor-read at `C` and `D`, and mixed remains a set are declared. No
uniqueness of incoming locks, no R-style recovery as the scored object, no
forall-perp as the scored object, no axis-cover as the scored object, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read reverse hold and face hold reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest incoming lock set `M` at a probe and at formed 6-NN | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports, reverse/face from those bits | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read reverse/face,
a formation-rate rule, and a physical selector among matching six-neighbors.
None is taken here.

### N7 — hostile steelman

**Steelman:** Two-axis opposite neighbor-read on x-probes is leftover of
nm2axpx forall-perp because the same process and probes already HOLD reverse
and face; leftover of two-axis same-lock x-probe neighbor-read because only
a sign of two seed letters changed; leftover of nm2axx cover with the union
demand dropped; leftover of R-style because some neighbor already carries
an opposite step; and uniqueness of `M` already answers the match.

**Answer:** Forall-perp pairs every incoming letter with every outgoing dual
letter at one probe. Neighbor-read asks whether some formed six-neighbor
carries the same incoming set. `O(A,τ)={+e_1}` is not `M(A,τ)={−e_3}`.
Same-lock x-probes HOLD reverse and face with the same probe letters, but
`M((0,1,1),τ)` and `M((0,1,0),τ)` differ by sign because the pairs are
opposite here. nm2axx cover reverse FAIL face FAIL because the union misses
e_2 at `A` and at `D`; neighbor-read reverse HOLD face HOLD. R-style at `A`
is `{−e_1}`, not `{−e_3}`. Mixed neighbor `M((1,1,2),τ)={+e_1,+e_3}` remains
a set; uniqueness is not required. Reverse neighbor-read is HOLD iff
neighbor-read at `A` and at `B`, not leftover of forall-perp and not
leftover of same-lock x-probe neighbor-read.

### N8 — cross-cycle echo

nm2axpx reported forall-orthogonal `M` versus `O` on these four x-probes
with reverse hold and face hold. nm2axx reported axis-cover of `M` versus
`O` on these four x-probes with reverse fail and face fail because the
union misses e_2. nm2readslz reported neighbor-read of `M` on two-axis
same-lock z-probes with reverse hold and face hold from seed `A` at tick 0.
Two-axis opposite z-probe neighbor-read reports fail at `A`, HOLD at
`B`,`C`,`D`, reverse fail, and face hold. Two-axis opposite y-probes report
reverse fail and face fail. This note is not those displays: it reports
neighbor-read of `M` at `τ=t+1` on two disjoint opposite pairs with
x-probes, HOLD at `A`,`B`,`C`,`D`, reverse hold, and face hold. HOLD iff
some formed 6-NN recovers `M` as a set, not leftover of nm2axpx forall-perp,
and not leftover of same-lock neighbor-read.

**Gate disposition:** PASS for the neighbor-read `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
R-style recovery,” “the predicate equals nm2axpx forall-perp,” “the
predicate equals nm2axx axis-cover,” “the predicate equals two-axis
same-lock neighbor-read,” “bits are Admissibility,” “neighbor-read fails at
`A`,” “neighbor-read fails at `D`,” “reverse neighbor-read fails,” or “face
neighbor-read fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each x-probe's own earliest incoming
set from the record prefix at that probe's `t+1`, reports `M` at each formed
six-neighbor, reports neighbor-read as set-equality of those incoming sets,
lists matching six-neighbors, compares to two-axis same-lock neighbor-read
and to opposite z-probe neighbor-read, and checks Theorems 1--3. It also
checks that neighbor-read HOLDs at `A` from matching `D`, that R-style
recovery is a different object, that mixed sets remain sets, that
unique-letter is `UNDEFINED` at mixed neighbors, that the construction does
not sum, that a formation member from already-recorded six-neighbor locks
is not attached, and that the display is not leftover of nm2axpx forall-perp
or of nm2axx axis-cover. No runner cache is written.
