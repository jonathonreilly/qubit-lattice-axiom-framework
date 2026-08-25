---
claim_id: two_axis_opposite_yprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the cyclic lex-largest orientation at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic Lex-Largest Orientation At t+1 Reverse And Face On Four Y-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** Neighbor-read of the cyclic lex-largest orientation at t+1 on the four
y-probes of the two-axis opposite seed, and reverse/face from that, are
reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face_2026_08_15.py)

No runner cache is written.

## Result Up Front

On the finite Euclidean host `B_3(0)={n:n·n<=9}`, form records by the
two-axis opposite seed, perp-step, incoming-lock process. Same process and
y-probes as nm2ax. For each formed site `q` write `t(q)` for the formation
tick and `τ(q)=t(q)+1`. There is no global T. `M`, `O`, and split are as
nm2ax12. Orient as nm2oricyclz: cyclic next/prev lex-largest outgoing
determinant orientation of the 1-in 2-out frame. Unformed sites are
`UNDEFINED`.

Neighbor-read HOLDs at a formed `q` iff `Orient(q)` is `±1` and some formed
six-neighbor `r=q+e` has `Orient(r)=Orient(q)` at the same `τ`. If Orient
fails at `q`, neighbor-read fails, not `UNDEFINED`. Uniqueness is not
required. Reverse HOLDs iff neighbor-read HOLDs at probes `A` and `B`. Face
HOLDs iff neighbor-read HOLDs at probes `C` and `D`. Cover and split do not
score handedness.

On this seed and these y-probes the finite listing is:

- t(A)=0, M(A, τ) = {−e_1}, O(A, τ) = {+e_2, −e_3}, split(A) = hold, i(A) = 1, o_next(A) = +e_2, o_prev(A) = −e_3, det(A) = +1, Orient(A) = +1, neighbor-read(A) = hold
- t(B)=1, M(B, τ) = {+e_1}, O(B, τ) = {+e_2, +e_3, −e_3}, split(B) = hold, i(B) = 1, o_next(B) = +e_2, o_prev(B) = −e_3, det(B) = −1, Orient(B) = −1, neighbor-read(B) = fail
- t(C)=1, M(C, τ) = {+e_2}, O(C, τ) = {+e_1, −e_1, +e_3, −e_3}, split(C) = hold, i(C) = 2, o_next(C) = −e_3, o_prev(C) = −e_1, det(C) = +1, Orient(C) = +1, neighbor-read(C) = hold
- t(D)=2, M(D, τ) = {−e_3}, O(D, τ) = {+e_1, −e_1}, split(D) = fail, i(D) = 3, o_next(D) = −e_1, o_prev(D) = fail, det(D) = fail, Orient(D) = fail, neighbor-read(D) = fail
- Reverse neighbor-read at τ: fail
- Face neighbor-read at τ: fail

The face bit is displayed, not adopted. Do not write into Admissibility.
Do not attach L1. This is not leftover of nm2oricycy equal `±1` Orient
signs, not leftover of nm2oricyclz z-probe Orient HOLDING reverse and face,
not leftover of nm2sready neighbor-read of the 1-in 2-out split, not
leftover of nm2ready neighbor-read of M, not leftover of nm2oready
neighbor-read of O, not leftover of nm2ax axis-cover, not leftover of
nm2ax12 1-in 2-out split, not leftover of lexicographic `o1,o2`, not leftover
of cyclic lex-smallest, not leftover of nm2orioney lex-one, not leftover of
leftover-of-`M` alone, not leftover of leftover-of-`O` alone, not
leftover-empty fail, not leftover of mixed #7188 fail/fail, and not the
two-tick lock-count clock composition. The second pair is a new seed, not a
formed child. O is not M. No larger host is used.

## Current Premise Boundary

Quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

Admissibility determines a local distribution from nearest-neighbor
conditions and does not supply the formation site, probability, or rate.

The process below is an explicit finite display on `B_3(0)`. It is not a
rewrite of Admissibility and is not a lattice-wide lettering rule.

## Exact Objects

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`. The six nearest-neighbor
steps are `±e_1,±e_2,±e_3`. The host is the Euclidean ball
`B_3(0)={n:n·n<=9}`. No larger host is used.

The two-axis opposite seed at tick 0 is two disjoint opposite pairs:

- origin locks `+e_1`
- `(0,1,0)` locks `−e_1`
- `(0,0,1)` locks `+e_2`
- `(0,1,1)` locks `−e_2`

The second pair is a new seed, not a formed child of the first pair. A
parent with lock axis `e_i` may take a nearest-neighbor step `s` only when
`s·e_i=0`. A newly formed child locks the incoming step. Seeds keep their
seed letters as a singleton. If several parents first reach a child at the
same tick, `M` is the set of those incoming steps.

The four y-probes are `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`.
These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`,
`C=(2,0,0)`, `D=(1,1,0)`. Probe `A` is a seed. Formation, `M`, and `O` are
computed only from records on this host.

For a site `q` and a tick bound `τ`, if `q` is unformed at `τ` then `M`,
`O`, Orient, and neighbor-read at `q` are `UNDEFINED`. Otherwise `M(q,τ)` is
the earliest nonempty incoming set assembled from parents with formation
tick at most `τ`, and

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

Empty `O` is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs iff `Axis(M)` intersect
`Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`.
Split HOLDs iff cover HOLDs and `|Axis(M)|=1` (hence `|Axis(O)|=2`). Split
HOLD required. When split HOLDs, `m` is the unique vector in `M`. Let `i`
in `{1,2,3}` be the axis index of `m`. `e_next = e_{i+1}` with `3+1→1`.
`e_prev = e_{i-1}` with `1−1→3`. `O_next = O ∩ {±e_next}`. `O_prev =
O ∩ {±e_prev}`. If either slot is empty, Orient fails, not `UNDEFINED`.
Order `+e < −e`. `o_next` is the lex-largest vector in `O_next` (hence `−e`
if both signs). `o_prev` likewise. `Orient(q)` is the sign of the integer
determinant of columns `m`, `o_next`, `o_prev`. If split fails, Orient
fails, not `UNDEFINED`.

Neighbor-read HOLDs at formed `q` iff `Orient(q)` is `±1` and there exists a
formed six-neighbor `r` with `Orient(r)=Orient(q)` at the same `τ`. If
Orient fails at `q`, neighbor-read fails, not `UNDEFINED`. Mixed remains a
set. Uniqueness is not required. Pair-read of two probe bits is
`UNDEFINED` if either bit is `UNDEFINED`, HOLD if both HOLD, and fail
otherwise. Reverse is pair-read of `A` and `B`. Face is pair-read of `C`
and `D`. Occupancy of sites is not used.

## Theorem 1 — Formation Ticks, M, O, Orient, And Neighbor-Read Bits

**Claim.** On this host and seed, the four y-probes have the ticks, lock
sets, cyclic lex-largest Orient signs, and neighbor-read bits listed below.

**Proof.** Direct breadth-first formation with the perp-step rule yields
four tick-0 seeds. Parallel steps from the origin along `±e_1` are blocked
because those steps fail `s·e_i=0`. Probe ticks are t(A)=0, t(B)=1,
t(C)=1, and t(D)=2.

At each probe, `M` at `τ=t+1` equals `M` at formation. `O` is assembled from
neighbors that are formed by that same cut. Orient is the cyclic next/prev
lex-largest determinant sign of nm2oricyclz at that same cut.

- A is the seed `(0,1,0)`, so M(A, τ) = {−e_1}, O(A, τ) = {+e_2, −e_3}, split(A) = hold, i(A) = 1, o_next(A) = +e_2, o_prev(A) = −e_3, det(A) = +1, Orient(A) = +1, neighbor-read(A) = hold.
- B is first reached from `(0,1,1)` by `+e_1`, so M(B, τ) = {+e_1}, O(B, τ) = {+e_2, +e_3, −e_3}, split(B) = hold, i(B) = 1, o_next(B) = +e_2, o_prev(B) = −e_3, det(B) = −1, Orient(B) = −1, neighbor-read(B) = fail.
- C is first reached from `A` by `+e_2`, so M(C, τ) = {+e_2}, O(C, τ) = {+e_1, −e_1, +e_3, −e_3}, split(C) = hold, i(C) = 2, o_next(C) = −e_3, o_prev(C) = −e_1, det(C) = +1, Orient(C) = +1, neighbor-read(C) = hold.
- D is first reached from `B` by `−e_3` at tick 2, so M(D, τ) = {−e_3}, O(D, τ) = {+e_1, −e_1}, split(D) = fail, i(D) = 3, o_next(D) = −e_1, o_prev(D) = fail, det(D) = fail, Orient(D) = fail, neighbor-read(D) = fail.

new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)

new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)

new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)

new 6-NN of D at t(D)+1: (2, 1, 0)

formed 6-NN of A at τ: (1, 1, 0) M=UNDEFINED O=UNDEFINED Orient=UNDEFINED neighbor-read=UNDEFINED, (-1, 1, 0) M=UNDEFINED O=UNDEFINED Orient=UNDEFINED neighbor-read=UNDEFINED, (0, 2, 0) M={+e_2} O={} Orient=fail neighbor-read=fail, (0, 0, 0) M={+e_1} O={−e_2, −e_3} Orient=+1 neighbor-read=hold, (0, 1, 1) M={−e_2} O={+e_1, −e_1, +e_3} Orient=+1 neighbor-read=hold, (0, 1, -1) M={−e_3} O={} Orient=fail neighbor-read=fail

formed 6-NN of B at τ: (2, 1, 1) M=UNDEFINED O=UNDEFINED Orient=UNDEFINED neighbor-read=UNDEFINED, (0, 1, 1) M={−e_2} O={+e_1, −e_1, +e_3} Orient=+1 neighbor-read=hold, (1, 2, 1) M={+e_2} O={} Orient=fail neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} Orient=+1 neighbor-read=fail, (1, 1, 2) M={+e_1, +e_3} O={} Orient=fail neighbor-read=fail, (1, 1, 0) M={−e_3} O={−e_1} Orient=fail neighbor-read=fail

formed 6-NN of C at τ: (1, 2, 0) M={+e_1} O={} Orient=fail neighbor-read=fail, (-1, 2, 0) M={−e_1} O={} Orient=fail neighbor-read=fail, (0, 1, 0) M={−e_1} O={+e_2, −e_3} Orient=+1 neighbor-read=hold, (0, 2, 1) M={+e_3} O={−e_2} Orient=fail neighbor-read=fail, (0, 2, -1) M={+e_2, −e_3} O={} Orient=fail neighbor-read=fail

formed 6-NN of D at τ: (2, 1, 0) M={+e_1} O={} Orient=fail neighbor-read=fail, (0, 1, 0) M={−e_1} O={+e_2, −e_3} Orient=+1 neighbor-read=hold, (1, 2, 0) M={+e_1} O={−e_3} Orient=fail neighbor-read=fail, (1, 0, 0) M={−e_3} O={+e_1} Orient=fail neighbor-read=fail, (1, 1, 1) M={+e_1} O={+e_2, +e_3, −e_3} Orient=−1 neighbor-read=fail, (1, 1, -1) M={+e_1} O={+e_2, −e_3} Orient=−1 neighbor-read=fail

matching 6-NN of A: (0, 0, 0), (0, 1, 1)

matching 6-NN of B: none

matching 6-NN of C: (0, 1, 0)

matching 6-NN of D: none

The matching neighbors of `A` are the origin and the second-pair seed
`(0,1,1)`. Both carry Orient `+1` at `A`'s `τ`, equal to `Orient(A)=+1`,
so neighbor-read(A) = hold. Sites `(1,1,0)` and `(-1,1,0)` do form later
and are `UNDEFINED` at `A`'s `τ`. Site `C=(0,2,0)` is formed at `A`'s `τ`
with empty `O`, so Orient fails there.

`B` has Orient `−1` because lex-largest on the mixed `e_3` slot of
`O(B,τ)={+e_2,+e_3,−e_3}` selects `−e_3`, and `det(+e_1,+e_2,−e_3)=−1`.
No formed six-neighbor at `B`'s `τ` recovers Orient `−1`. Neighbor
`(1,0,1)` has the same unsigned 1-in 2-out axes, so split neighbor-read
HOLDs there, but its Orient is `+1`. Therefore neighbor-read(B) = fail
even though split(B) = hold and Orient(B) is `±1`. This is the first
display of neighbor-read of cyclic lex-largest Orient on these y-probes,
and it is not leftover of nm2sready neighbor-read of the 1-in 2-out split
and not leftover of nm2oricycy equal-sign reverse of Orient.

`C` has Orient `+1`. The matching neighbor is seed `A=(0,1,0)`, so
neighbor-read(C) = hold. Split HOLDs at `C` with no matching unsigned-axis
neighbor, so split neighbor-read fails at `C` while this neighbor-read
HOLDs.

Split fails at `D` from cover fail with leftover `{e_2}` (1-in 1-out).
Empty `O_prev` on `e_2` makes Orient fail, not `UNDEFINED`. Neighbor-read(D)
is therefore fail, not `UNDEFINED`. Mixed remains a set at `C`'s outgoing
`{+e_1,−e_1,+e_3,−e_3}` and at `B`'s mixed `e_3` slot.
`QED`

## Theorem 2 — Reverse Neighbor-Read

**Claim.** Reverse neighbor-read at `τ` is fail, not hold and not
`UNDEFINED`.

**Proof.** Reverse HOLDs iff neighbor-read HOLDs at `A` and at `B`. Both
probes are formed, so the pair is not `UNDEFINED`. Theorem 1 gives
neighbor-read(A) = hold and neighbor-read(B) = fail, hence
Reverse neighbor-read at τ: fail. Equal-sign reverse of Orient also fails,
because `Orient(A)=+1` and `Orient(B)=−1`, but that is a different
predicate: neighbor-read reverse fails because `B` has no matching
neighbor, while neighbor-read at `A` HOLDs. Neighbor-read of split reverse
HOLDs. Cover reverse HOLDs. Cover and split do not score handedness.
`QED`

## Theorem 3 — Face Neighbor-Read, Displayed Not Adopted

**Claim.** Face neighbor-read at `τ` is fail, not hold and not
`UNDEFINED`. The bit is displayed, not adopted.

**Proof.** Face HOLDs iff neighbor-read HOLDs at `C` and at `D`. Theorem 1
gives neighbor-read(C) = hold and neighbor-read(D) = fail, hence
Face neighbor-read at τ: fail. The report is a finite listing on this
seed and these four y-probes. It is displayed, not adopted as an
Admissibility clause, as a lettering law, or as a uniqueness rule. Do not
write into Admissibility. Do not attach L1.
`QED`

## Discriminators

Neighbor-read of `M` as signed sets fails at `A` and at `C`, and HOLDs at
`B` and at `D`. Neighbor-read of `O` as signed sets fails at every
y-probe. Neighbor-read of the 1-in 2-out split HOLDs at `A` and at `B` and
fails at `C` and at `D`, so that reverse HOLDs. The present letter HOLDs at
`A` and at `C` and fails at `B` and at `D`, so reverse fails. It is
therefore not leftover of nm2ready neighbor-read of M, not leftover of
nm2oready neighbor-read of O, and not leftover of nm2sready neighbor-read
of the 1-in 2-out split.

nm2oricycy reverse fail face fail scores equal `±1` Orient signs, not
neighbor-read. Here neighbor-read HOLDs at `A` while Orient(A) disagrees
with Orient(B), and neighbor-read HOLDs at `C` while Orient(D) fails.
nm2oricyclz HOLDING reverse and face is the four z-probes of this seed
under Orient equality; neighbor-read of that same Orient fails at every
z-probe. Cyclic lex-smallest reverse HOLDs with Orient `+1` at `A` and at
`B`; this Orient at `B` is `−1`, and matching 6-NN of A under lex-smallest
is only the origin, not also `(0,1,1)`. Lex-one reverse HOLDs. Leftover of
`M` alone reverse HOLDs. Leftover of `O` alone reverse HOLDs.

The same y-probes on a two-site `±e_1` seed form `B` at tick 2 and `D` at
tick 3 and treat `(0,0,1)` as a formed child, not a seed. A perpendicular
two-site seed and a z-symmetric three-site seed do not reproduce this
listing.

## Exact Target And Proof Obligations

**Exact target:** report neighbor-read of the cyclic lex-largest orientation
at `t+1` on the four y-probes of the two-axis opposite seed, and the
reverse/face pair-read of those bits, on Euclidean `B_3(0)`.

| Obligation | Disposition |
|---|---|
| name the seed, perp-step rule, host, and y-probes | displayed process, closed on `B_3(0)` |
| list `t`, `M`, `O`, Orient, formed six-neighbor bits, and neighbor-read | Theorem 1, finite listing |
| reverse pair-read of `A` and `B` | Theorem 2, fail |
| face pair-read of `C` and `D` | Theorem 3, fail, displayed not adopted |
| adopt reverse or face as Admissibility | not claimed |
| attach a uniqueness cut | not claimed |
| lattice-wide lettering | not claimed; no global T |

The proof-obligation graph is acyclic. The leaves are finite listings on
a 123-site ball. No observational value is used.

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of cyclic next/prev lex-largest Orient at `t+1` on the four y-probes of the two-axis opposite seed, and reverse/face from that. |
| V2 | Current main has no landed neighbor-read of cyclic lex-largest Orient reverse/face on these four y-probes. |
| V3 | Four neighbor-read reports and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because neighbor-read HOLDs at `A` and at `C` while failing at `B`, split neighbor-read reverse HOLDs, and equal-sign Orient reverse fails for a different reason. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-Go Discipline Gate

This note is a displayed finite report, not a negative law. Broad negative
inference from the reverse fail, from the face fail, or from leftover
signed-set misses is **FAIL / DO NOT SHIP**.

### N1 — materially distinct routes

Neighbor-read of cyclic lex-largest Orient, neighbor-read of `M`,
neighbor-read of `O`, neighbor-read of split, equal-sign reverse of Orient,
axis-cover without neighbor-read, unique-letter cuts, cyclic lex-smallest,
and a rewritten Admissibility rule are distinct objects. Only the first is
executed here, and only on four y-probes. The others are named leftovers or
out of scope. No universal negative is claimed, so a no-go is not shipped.

### N2 — wall independence

There is no shipped wall. Reverse fail and face fail are pair-reads of
the four neighbor-read bits. Removing either pair changes the report
without creating a law-level obstruction.

### N3 — hidden-condition scan

Load-bearing and explicit: two-axis opposite seed, perp-step
`s·e_i=0`, incoming lock, Euclidean `B_3(0)`, `τ(q)=t(q)+1`, cyclic
lex-largest Orient of `M` and `O` as nm2oricyclz, neighbor-read of that
sign against formed six-neighbors at the same `τ`, and the four named
y-probes. No phrase such as "by construction" or "naturally" adds a
further premise. Occupancy of sites is not used.

### N4 — residual matching

No prior negative is cited as evidence. The only linked premise document
is the current axiom memo, used to quote Lattice, Qubit, Record, and the
Admissibility non-supply of formation site. The listing is proved here.

### N5 — resolution audit

| Resolution | Executed? | Exact scope |
|---|---:|---|
| per element | yes | cyclic lex-largest Orient of `M` and `O` at a probe and at formed six-neighbors, compared as `±1` signs at that probe's `t+1` |
| per site | yes | y-probes `A,B,C,D` on Euclidean `B_3(0)` only |
| per mode | no | no spectral or mode calculation is executed on this finite host |
| per block | yes | four neighbor-read reports, reverse/face from those bits |
| lattice-wide | checked and not executed | no lattice-wide lettering rule is claimed; no global T |

### N6 — partial-closure paths

Live extensions already named: other seeds, other probe axes, a uniqueness
cut, signed-set leftover, a larger host, or an Admissibility rewrite. None
is closed by this listing, and none is dismissed as requiring a new axiom.

### N7 — steelman

The strongest objection to reading reverse fail and face fail as a law is
decisive: both bits are pair-reads of probe reports on one displayed seed.
Neighbor-read of `M` fails at `A`, neighbor-read of `O` fails at `A` and at
`B`, and neighbor-read of split HOLDs reverse. Equal-sign Orient reverse
fails because `A` is `+1` and `B` is `−1`, while this reverse fails because
`B` has no matching neighbor. That is why Theorem 3 is displayed, not
adopted.

### N8 — cross-cycle echo

Investment names `nm2ax`, `nm2ax12`, `nm2oricyclz`, `nm2oricycy`,
`nm2sready`, `nm2ready`, and `nm2oready` mark nearby displayed processes.
This note reuses the same two-axis opposite seed and y-probes only to
report neighbor-read of cyclic lex-largest Orient at `t+1`. It does not
inherit an Orient-equality reverse, a split neighbor-read, or a signed-set
neighbor-read as a theorem.

**No-Go Discipline status:** FAIL / DO NOT SHIP for any negative
Admissibility, lettering, or uniqueness claim. The positive finite listing
in Theorems 1–3 remains a displayed bounded report.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite neighbor-read of cyclic lex-largest Orient at t+1 on four y-probes, with reverse/face pair-read, on Euclidean B_3(0); displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face
target_blocker_text: "report neighbor-read of cyclic lex-largest Orient at t+1 on the two-axis opposite y-probes and the reverse/face pair of those bits"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep reverse/face displayed. Do not write into Admissibility. Do not attach L1."
conditional_surface_status: "exact finite listing on B_3(0) for the declared seed and y-probes; law-level adoption remains open and is not claimed"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice / Qubit / Record sentences | framework premise | linked current axiom memo |
| Admissibility non-supply of formation site | framework boundary | quoted; process is displayed |
| two-axis opposite seed, perp-step, incoming lock | declared process | explicit condition |
| Euclidean `B_3(0)` | declared host | `{n:n·n<=9}`; no larger host |
| neighbor-read of cyclic lex-largest Orient, reverse, face | reported bits | Theorems 1–3 |
| Admissibility rewrite, L1, uniqueness cut | residual | open and not claimed |

Independent audit remains required before any effective status may change.
