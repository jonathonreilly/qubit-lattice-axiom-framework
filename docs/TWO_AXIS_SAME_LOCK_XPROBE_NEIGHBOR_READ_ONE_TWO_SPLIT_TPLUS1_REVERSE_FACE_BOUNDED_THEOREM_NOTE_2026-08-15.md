---
claim_id: two_axis_same_lock_xprobe_neighbor_read_one_two_split_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the 1-in 2-out split at t+1 on the four x-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_neighbor_read_one_two_split_tplus1_reverse_face_2026_08_15.py
---

# Two-Axis Same-Lock X-Probe Neighbor-Read Of The 1-In 2-Out Split At t+1, Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** Neighbor-read of the 1-in 2-out split at t+1 on the four x-probes of the
two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_neighbor_read_one_two_split_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_neighbor_read_one_two_split_tplus1_reverse_face_2026_08_15.py)

No runner cache is written.

## Result Up Front

On the finite Euclidean host `B_3(0)={n:n·n<=9}`, form records by the
two-axis same-lock seed, perp-step, incoming-lock process. Same process and
x-probes as nm2slx. For each formed site `q` write `t(q)` for the formation
tick and `τ(q)=t(q)+1`. There is no global T. `M`, `O`, and split are as
nm2sl12. Unformed sites are `UNDEFINED`.

Neighbor-read of the split HOLDs at a formed `q` iff split HOLDs at `q` and
some formed six-neighbor `r=q+e` has split HOLD and
`Axis(M(r,τ))=Axis(M(q,τ))` and `Axis(O(r,τ))=Axis(O(q,τ))`. If split fails
at `q`, neighbor-read fails, not `UNDEFINED`. Uniqueness is not required.
Reverse HOLDs iff neighbor-read HOLDs at probes `A` and `B`. Face HOLDs iff
neighbor-read HOLDs at probes `C` and `D`.

On this seed and these x-probes the finite listing is:

- t(A)=2, M(A, τ) = {−e_3}, O(A, τ) = {+e_1}, Axis(M)(A, τ) = {e_3}, Axis(O)(A, τ) = {e_1}, split(A) = fail, neighbor-read(A) = fail
- t(B)=1, M(B, τ) = {+e_1}, O(B, τ) = {+e_2, +e_3, −e_3}, Axis(M)(B, τ) = {e_1}, Axis(O)(B, τ) = {e_2, e_3}, split(B) = hold, neighbor-read(B) = hold
- t(C)=3, M(C, τ) = {+e_1}, O(C, τ) = {−e_2, +e_3, −e_3}, Axis(M)(C, τ) = {e_1}, Axis(O)(C, τ) = {e_2, e_3}, split(C) = hold, neighbor-read(C) = hold
- t(D)=2, M(D, τ) = {−e_3}, O(D, τ) = {+e_1}, Axis(M)(D, τ) = {e_3}, Axis(O)(D, τ) = {e_1}, split(D) = fail, neighbor-read(D) = fail
- Reverse neighbor-read at τ: fail
- Face neighbor-read at τ: fail

The face bit is displayed, not adopted. Do not write into Admissibility.
Do not attach L1. This is not leftover of nm2readslx neighbor-read of M, not
leftover of nm2oreadslx neighbor-read of O, not leftover of signed (M, O) set
equality, not leftover of nm2sl12 1-in 2-out split without neighbor-read,
not leftover of nm2sreadz, and not leftover of nm2sreadslz.
No larger host is used.

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

The two-axis same-lock seed at tick 0 is two disjoint same-lock pairs:

- origin locks `+e_1`
- `(0,1,0)` locks `+e_1`
- `(0,0,1)` locks `+e_2`
- `(0,1,1)` locks `+e_2`

The second pair is a new seed, not a formed child of the first pair. A
parent with lock axis `e_i` may take a nearest-neighbor step `s` only when
`s · e_i = 0`. A newly formed child locks the incoming step. Seeds keep their
seed letters as a singleton. If several parents first reach a child at the
same tick, `M` is the set of those incoming steps.

The four x-probes are `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`.
These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. Probe `A` is not a seed: the origin locks `+e_1`,
so the parallel step from the origin to `A` is blocked. Formation, `M`, and
`O` are computed only from records on this host.

For a site `q` and a tick bound `τ`, if `q` is unformed at `τ` then `M`,
`O`, split, and neighbor-read at `q` are `UNDEFINED`. Otherwise `M(q,τ)` is
the earliest nonempty incoming set assembled from parents with formation
tick at most `τ`, and

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

Empty `O` is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs iff `Axis(M)` intersect
`Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`.
Split HOLDs iff cover HOLDs and `|Axis(M)|=1` (hence `|Axis(O)|=2`). 2-in
1-out is fail of this object, not UNDEFINED.

Neighbor-read HOLDs at formed `q` iff split HOLDs at `q` and there exists a
formed six-neighbor `r` with split HOLD and the same unsigned axis
assignment: `Axis(M(r,τ))=Axis(M(q,τ))` and `Axis(O(r,τ))=Axis(O(q,τ))`.
If split fails at `q`, neighbor-read fails, not `UNDEFINED`. Mixed remains
a set. Uniqueness is not required. Pair-read of two probe bits is
`UNDEFINED` if either bit is `UNDEFINED`, HOLD if both HOLD, and fail
otherwise. Reverse is pair-read of `A` and `B`. Face is pair-read of `C`
and `D`. Occupancy of sites is not used.

## Theorem 1 — Formation Ticks, M, O, Split, And Neighbor-Read Bits

**Claim.** On this host and seed, the four x-probes have the ticks, lock
sets, split bits, and neighbor-read bits listed below.

**Proof.** Direct breadth-first formation with the perp-step rule yields
four tick-0 seeds. Parallel steps from the origin along `±e_1` are blocked
because those steps fail `s · e_i = 0`. Probe ticks are t(A)=2, t(B)=1,
t(C)=3, and t(D)=2.

At each probe, `M` at `τ=t+1` equals `M` at formation. `O` is assembled from
neighbors that are formed by that same cut.

- A is first reached from `(1,0,1)` by `−e_3`, so M(A, τ) = {−e_3}, O(A, τ) = {+e_1}, Axis(M)(A, τ) = {e_3}, Axis(O)(A, τ) = {e_1}, split(A) = fail.
- B is first reached from `(0,1,1)` by `+e_1`, so M(B, τ) = {+e_1}, O(B, τ) = {+e_2, +e_3, −e_3}, Axis(M)(B, τ) = {e_1}, Axis(O)(B, τ) = {e_2, e_3}, split(B) = hold.
- C is first reached from `A` by `+e_1`, so M(C, τ) = {+e_1}, O(C, τ) = {−e_2, +e_3, −e_3}, Axis(M)(C, τ) = {e_1}, Axis(O)(C, τ) = {e_2, e_3}, split(C) = hold.
- D is first reached from `B` by `−e_3`, so M(D, τ) = {−e_3}, O(D, τ) = {+e_1}, Axis(M)(D, τ) = {e_3}, Axis(O)(D, τ) = {e_1}, split(D) = fail.

formed 6-NN of A at τ: (2, 0, 0) M={+e_1} O={} split=fail neighbor-read=fail, (0, 0, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold, (1, 1, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail, (1, -1, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 0, -1) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold

formed 6-NN of B at τ: (2, 1, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 1, 1) M={+e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=fail, (1, 2, 1) M={+e_2} O={} split=fail neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, 2) M={+e_1, +e_3} O={} split=fail neighbor-read=fail, (1, 1, 0) M={−e_3} O={} split=fail neighbor-read=fail

formed 6-NN of C at τ: (1, 0, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail, (2, 1, 0) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (2, -1, 0) M={−e_2, −e_3} O={} split=fail neighbor-read=fail, (2, 0, 1) M={+e_2, +e_3, −e_3} O={} split=fail neighbor-read=fail, (2, 0, -1) M={−e_3} O={} split=fail neighbor-read=fail

formed 6-NN of D at τ: (2, 1, 0) M={+e_1} O={} split=fail neighbor-read=fail, (0, 1, 0) M={+e_1} O={+e_2, −e_3} split=hold neighbor-read=hold, (1, 2, 0) M={+e_1} O={−e_3} split=fail neighbor-read=fail, (1, 0, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail, (1, 1, 1) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, -1) M={+e_1} O={+e_2, −e_3} split=hold neighbor-read=hold

matching 6-NN of A: none

matching 6-NN of B: (1, 0, 1)

matching 6-NN of C: (2, 1, 0)

matching 6-NN of D: none

Split fails at `A` because cover fails from missing `e_2`. Neighbor-read
therefore fails at `A`, not `UNDEFINED`. Site `(1,-1,0)` is a formed
six-neighbor of `A` with split HOLD and `Axis(M)={e_1}`, `Axis(O)={e_2,e_3}`,
which is not the `{e_3}`/`{e_1}` assignment at `A`. The origin is a formed
six-neighbor with split HOLD, but again `Axis(M)={e_1}`. No formed
six-neighbor recovers `A`'s axes, so matching 6-NN of A: none.

The matching neighbor of `B` is `(1,0,1)`. `M` agrees as `{+e_1}`, but
`O(B,τ)={+e_2,+e_3,−e_3}` is not equal to `O((1,0,1),τ)={−e_2,+e_3,−e_3}`
as signed sets. The unsigned axes agree: `Axis(M)={e_1}` and
`Axis(O)={e_2,e_3}`, so neighbor-read(B) = hold without any uniqueness cut.
Site `(0,1,1)` is a formed six-neighbor of `B` with split HOLD, yet
`Axis(M)={e_2}` is not `{e_1}`, so neighbor-read fails there. Site
`(1,1,2)` is mixed `{+e_1,+e_3}` at `B`'s `τ` and does not recover a 1-in
2-out assignment.

The matching neighbor of `C` is `(2,1,0)`. `M` agrees as `{+e_1}`, but
`O(C,τ)={−e_2,+e_3,−e_3}` is not equal to `O((2,1,0),τ)={+e_2,+e_3,−e_3}`
as signed sets. The unsigned axes agree: `Axis(M)={e_1}` and
`Axis(O)={e_2,e_3}`, so neighbor-read(C) = hold. Site `(3,0,0)` lies in
`B_3(0)` (`n·n=9`) and is never formed: the only in-ball parent would be
`C` itself, whose lock `+e_1` forbids the parallel step. Probe `A` is a
six-neighbor of `C` with split fail. Mixed remains a set: `O(C,τ)` has
three outgoing steps.

Split fails at `D` because cover fails from missing `e_2`. Neighbor-read
therefore fails at `D`, not `UNDEFINED`. This is the same lock-set pattern
as `A`, at a different site and tick.
`QED`

## Theorem 2 — Reverse Neighbor-Read

**Claim.** Reverse neighbor-read at `τ` is fail, not hold and not
`UNDEFINED`.

**Proof.** Reverse HOLDs iff neighbor-read HOLDs at `A` and at `B`. Both
probes are formed, so the pair is not `UNDEFINED`. Theorem 1 gives
neighbor-read(A) = fail and neighbor-read(B) = hold, hence
Reverse neighbor-read at τ: fail.
`QED`

## Theorem 3 — Face Neighbor-Read, Displayed Not Adopted

**Claim.** Face neighbor-read at `τ` is fail. The bit is displayed, not
adopted.

**Proof.** Face HOLDs iff neighbor-read HOLDs at `C` and at `D`. Theorem 1
gives neighbor-read(C) = hold and neighbor-read(D) = fail, hence
Face neighbor-read at τ: fail. The report is a finite listing on this seed
and these four x-probes. It is displayed, not adopted as an Admissibility
clause, as a lettering law, or as a uniqueness rule. Do not write into
Admissibility. Do not attach L1.
`QED`

## Discriminators

Neighbor-read of `M` as signed sets HOLDs at every x-probe, so that leftover
reverse HOLDs and leftover face HOLDs. Neighbor-read of `O` as signed sets
HOLDs at `A` and `D` and fails at `B` and `C`: reverse still fails, but
neighbor-read of the split HOLDs at `B` and at `C` while neighbor-read of
`O` fails there. Signed `(M, O)` set equality fails at every x-probe: no
formed six-neighbor recovers both lock sets as sets. The present letter
fails reverse because split fails at `A`, and fails face because split
fails at `D`, while recovering the unsigned 1-in 2-out assignment at `B`
and at `C`. It is therefore not leftover of nm2readslx neighbor-read of M
and not leftover of nm2oreadslx neighbor-read of O.

nm2sl12 split without neighbor-read on this same seed and these same
x-probes also returns reverse fail and face fail. Those pair-read bits
agree with the present reverse/face, but the objects differ: at `(1,-1,0)`
and at seed `(0,1,1)`, split HOLDs and neighbor-read fails. The report is
therefore not leftover of nm2sl12 1-in 2-out split without neighbor-read.

nm2sreadz neighbor-read of the split on opposite z is HOLDING reverse and
face. nm2sreadslz on the same two-axis same-lock seed with z-probes is
reverse fail and face HOLD. The same two-axis same-lock seed scored on
y-probes returns reverse HOLD and face fail. A perpendicular two-site seed
on these x-probes fails neighbor-read at every probe. The two-axis opposite
seed keeps `M(A,τ)={−e_3}` but has `O(D,τ)={+e_1, −e_1}`. One-axis same-lock
has `t(A)=3`, `t(B)=2`, `t(C)=4`, and `t(D)=3`. Those leftovers are not this
display. The report is therefore not leftover of nm2sreadz and not leftover
of nm2sreadslz.

## Exact Target And Proof Obligations

**Exact target:** report neighbor-read of the 1-in 2-out split at `t+1` on
the four x-probes of the two-axis same-lock seed, and the reverse/face
pair-read of those bits, on Euclidean `B_3(0)`.

| Obligation | Disposition |
|---|---|
| name the seed, perp-step rule, host, and x-probes | displayed process, closed on `B_3(0)` |
| list `t`, `M`, `O`, split, and neighbor-read | Theorem 1, finite listing |
| reverse pair-read of `A` and `B` | Theorem 2, fail |
| face pair-read of `C` and `D` | Theorem 3, fail, displayed not adopted |
| adopt reverse or face as Admissibility | not claimed |
| attach a uniqueness cut | not claimed |
| lattice-wide lettering | not claimed; no global T |

The proof-obligation graph is acyclic. The leaves are finite listings on
a 123-site ball. No observational value is used.

## No-Go Discipline Gate

This note is a displayed finite report, not a negative law. Broad negative
inference from the reverse fail, from the face fail, or from leftover
signed-set misses is **FAIL / DO NOT SHIP**.

### N1 — materially distinct route scan

Neighbor-read of the unsigned 1-in 2-out assignment, neighbor-read of `M`,
neighbor-read of `O`, signed `(M, O)` set equality, axis-cover without
`|Axis(M)|=1`, unique-letter cuts, and a rewritten Admissibility rule are
distinct objects. Only the first is executed here, and only on four
x-probes. The others are named leftovers or out of scope. No universal
negative is claimed, so a no-go is not shipped.

### N2 — wall independence

There is no shipped wall. Reverse fail and face fail are pair-reads of
the four neighbor-read bits. Removing either pair changes the report
without creating a law-level obstruction.

### N3 — hidden-condition scan

Load-bearing and explicit: two-axis same-lock seed, perp-step
`s · e_i = 0`, incoming lock, Euclidean `B_3(0)`, `τ(q)=t(q)+1`, split HOLD
together with unsigned axis equality of `M` and of `O`, and the four named
x-probes. No phrase such as "by construction" or "naturally" adds a
further premise. Occupancy of sites is not used.

### N4 — residual matching

No prior negative is cited as evidence. The only linked premise document
is the current axiom memo, used to quote Lattice, Qubit, Record, and the
Admissibility non-supply of formation site. The listing is proved here.

### N5 — resolution audit

| Resolution | Executed? | Exact scope |
|---|---:|---|
| per element | yes | each 1-in 2-out axis assignment of `M` and `O` at a probe and at formed six-neighbors, compared as unsigned axes at that probe's `t+1` |
| per site | yes | x-probes `A,B,C,D` on Euclidean `B_3(0)` only |
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
Neighbor-read of `M` HOLDs reverse and face, neighbor-read of `O` fails at
`B` and at `C` where the present letter HOLDs, signed `(M, O)` equality
fails at every x-probe, and split HOLDs at `(1,-1,0)` and at `(0,1,1)` while
neighbor-read fails there. That is why Theorem 3 is displayed, not adopted.

### N8 — cross-cycle echo

Investment names `nm2sreadz`, `nm2sreadslz`, `nm2slx`, `nm2sl12`,
`nm2readslx`, and `nm2oreadslx` mark nearby displayed processes. This note
reuses the same two-axis same-lock seed and x-probes only to report
neighbor-read of the 1-in 2-out split at `t+1`. It does not inherit an
axis-cover claim, a split-without-read claim, a signed-set neighbor-read,
the opposite-z HOLDING reverse/face, or the same-lock z reverse-fail
face-HOLD as a theorem.

**No-Go Discipline status:** FAIL / DO NOT SHIP for any negative
Admissibility, lettering, or uniqueness claim. The positive finite listing
in Theorems 1–3 remains a displayed bounded report.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite neighbor-read of the 1-in 2-out split at t+1 on four x-probes, with reverse fail and face fail, on Euclidean B_3(0); displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_neighbor_read_one_two_split_tplus1_reverse_face
target_blocker_text: "report neighbor-read of the 1-in 2-out split at t+1 on the two-axis same-lock x-probes and the reverse/face pair of those bits"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep reverse/face displayed. Do not write into Admissibility. Do not attach L1."
conditional_surface_status: "exact finite listing on B_3(0) for the declared seed and x-probes; law-level adoption remains open and is not claimed"
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
| two-axis same-lock seed, perp-step, incoming lock | declared process | explicit condition |
| Euclidean `B_3(0)` | declared host | `{n:n·n<=9}`; no larger host |
| neighbor-read of the 1-in 2-out split, reverse, face | reported bits | Theorems 1–3 |
| Admissibility rewrite, L1, uniqueness cut | residual | open and not claimed |

Independent audit remains required before any effective status may change.
