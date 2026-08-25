---
claim_id: two_axis_opposite_yprobe_neighbor_read_one_two_split_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the 1-in 2-out split at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_neighbor_read_one_two_split_tplus1_reverse_face_2026_08_15.py
---

# Two-Axis Opposite Y-Probe Neighbor-Read Of The 1-In 2-Out Split At t+1, Reverse And Face

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** Neighbor-read of the 1-in 2-out split at t+1 on the four y-probes of the
two-axis opposite seed, and reverse/face from that, are reported. Displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_neighbor_read_one_two_split_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_neighbor_read_one_two_split_tplus1_reverse_face_2026_08_15.py)

No runner cache is written.

## Result Up Front

On the finite Euclidean host `B_3(0)={n:n·n<=9}`, form records by the
two-axis opposite seed, perp-step, incoming-lock process. Same process and
y-probes as nm2ax. For each formed site `q` write `t(q)` for the formation
tick and `τ(q)=t(q)+1`. There is no global T. `M`, `O`, and split are as
nm2ax12. Unformed sites are `UNDEFINED`.

Neighbor-read of the split HOLDs at a formed `q` iff split HOLDs at `q` and
some formed six-neighbor `r=q+e` has split HOLD and
`Axis(M(r,τ))=Axis(M(q,τ))` and `Axis(O(r,τ))=Axis(O(q,τ))`. If split fails
at `q`, neighbor-read fails, not `UNDEFINED`. Uniqueness is not required.
Reverse HOLDs iff neighbor-read HOLDs at probes `A` and `B`. Face HOLDs iff
neighbor-read HOLDs at probes `C` and `D`.

On this seed and these y-probes the finite listing is:

- t(A)=0, M(A, τ) = {−e_1}, O(A, τ) = {+e_2, −e_3}, Axis(M)(A, τ) = {e_1}, Axis(O)(A, τ) = {e_2, e_3}, split(A) = hold, neighbor-read(A) = hold
- t(B)=1, M(B, τ) = {+e_1}, O(B, τ) = {+e_2, +e_3, −e_3}, Axis(M)(B, τ) = {e_1}, Axis(O)(B, τ) = {e_2, e_3}, split(B) = hold, neighbor-read(B) = hold
- t(C)=1, M(C, τ) = {+e_2}, O(C, τ) = {+e_1, −e_1, +e_3, −e_3}, Axis(M)(C, τ) = {e_2}, Axis(O)(C, τ) = {e_1, e_3}, split(C) = hold, neighbor-read(C) = fail
- t(D)=2, M(D, τ) = {−e_3}, O(D, τ) = {+e_1, −e_1}, Axis(M)(D, τ) = {e_3}, Axis(O)(D, τ) = {e_1}, split(D) = fail, neighbor-read(D) = fail
- Reverse neighbor-read at τ: hold
- Face neighbor-read at τ: fail

The face bit is displayed, not adopted. Do not write into Admissibility.
Do not attach L1. This is not leftover of nm2ready neighbor-read of M, not
leftover of nm2oready neighbor-read of O, not leftover of signed (M, O) set
equality, not leftover of nm2ax12 1-in 2-out split without neighbor-read,
and not leftover of nm2sreadz z-probe neighbor-read of the 1-in 2-out split.
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

**Claim.** On this host and seed, the four y-probes and their eventually
formed six-neighbors have the ticks, lock sets, split bits, and
neighbor-read bits listed below.

**Proof.** Direct breadth-first formation with the perp-step rule yields
four tick-0 seeds. Parallel steps from the origin along `±e_1` are blocked
because those steps fail `s·e_i=0`. Probe ticks are t(A)=0, t(B)=1,
t(C)=1, and t(D)=2.

At each probe, `M` at `τ=t+1` equals `M` at formation. `O` is assembled from
neighbors that are formed by that same cut.

- A is the seed `(0,1,0)`, so M(A, τ) = {−e_1}, O(A, τ) = {+e_2, −e_3}, Axis(M)(A, τ) = {e_1}, Axis(O)(A, τ) = {e_2, e_3}, split(A) = hold.
- B is first reached from `(0,1,1)` by `+e_1`, so M(B, τ) = {+e_1}, O(B, τ) = {+e_2, +e_3, −e_3}, Axis(M)(B, τ) = {e_1}, Axis(O)(B, τ) = {e_2, e_3}, split(B) = hold.
- C is first reached from `A` by `+e_2`, so M(C, τ) = {+e_2}, O(C, τ) = {+e_1, −e_1, +e_3, −e_3}, Axis(M)(C, τ) = {e_2}, Axis(O)(C, τ) = {e_1, e_3}, split(C) = hold.
- D is first reached from `B` by `−e_3` at tick 2, so M(D, τ) = {−e_3}, O(D, τ) = {+e_1, −e_1}, Axis(M)(D, τ) = {e_3}, Axis(O)(D, τ) = {e_1}, split(D) = fail.

formed 6-NN of A at τ: (1, 1, 0) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (-1, 1, 0) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 2, 0) M={+e_2} O={} split=fail neighbor-read=fail, (0, 0, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold, (0, 1, 1) M={−e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=hold, (0, 1, -1) M={−e_3} O={} split=fail neighbor-read=fail

formed 6-NN of B at τ: (2, 1, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 1, 1) M={−e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=hold, (1, 2, 1) M={+e_2} O={} split=fail neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, 2) M={+e_1, +e_3} O={} split=fail neighbor-read=fail, (1, 1, 0) M={−e_3} O={−e_1} split=fail neighbor-read=fail

formed 6-NN of C at τ: (1, 2, 0) M={+e_1} O={} split=fail neighbor-read=fail, (-1, 2, 0) M={−e_1} O={} split=fail neighbor-read=fail, (0, 1, 0) M={−e_1} O={+e_2, −e_3} split=hold neighbor-read=hold, (0, 2, 1) M={+e_3} O={−e_2} split=fail neighbor-read=fail, (0, 2, -1) M={+e_2, −e_3} O={} split=fail neighbor-read=fail

formed 6-NN of D at τ: (2, 1, 0) M={+e_1} O={} split=fail neighbor-read=fail, (0, 1, 0) M={−e_1} O={+e_2, −e_3} split=hold neighbor-read=hold, (1, 2, 0) M={+e_1} O={−e_3} split=fail neighbor-read=fail, (1, 0, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail, (1, 1, 1) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, -1) M={+e_1} O={+e_2, −e_3} split=hold neighbor-read=hold

matching 6-NN of A: (0, 0, 0)

matching 6-NN of B: (1, 0, 1)

matching 6-NN of C: none

matching 6-NN of D: none

The matching neighbor of `A` is the other seed of the first pair, the
origin. That site carries `M={+e_1}`, which is not equal to
`M(A,τ)={−e_1}` as signed sets, but `Axis(M)={e_1}` and
`Axis(O)={e_2,e_3}` agree, so neighbor-read(A) = hold without any
uniqueness cut. Sites `(1,1,0)` and `(-1,1,0)` do form later and are
`UNDEFINED` at `A`'s `τ`. Site `C=(0,2,0)` is formed at `A`'s `τ` with
empty `O`, so split fails there and neighbor-read is fail, not
`UNDEFINED`.

The matching neighbor of `B` is `(1,0,1)`. `M` agrees as `{+e_1}`, but
`O(B,τ)={+e_2,+e_3,−e_3}` is not equal to `O((1,0,1),τ)={−e_2,+e_3,−e_3}`
as signed sets. The unsigned axes agree: `Axis(M)={e_1}` and
`Axis(O)={e_2,e_3}`, so neighbor-read(B) = hold.

Split HOLDs at `C`, but no formed six-neighbor recovers
`Axis(M)={e_2}` and `Axis(O)={e_1,e_3}`. Neighbor `A` has split HOLD with
`Axis(M)={e_1}`. Site `(0,3,0)` never forms on this host. Therefore
neighbor-read(C) = fail even though split(C) = hold. This is the first
display of neighbor-read of the 1-in 2-out split on these y-probes, and it
is not leftover of nm2ax12 1-in 2-out split without neighbor-read.

Split fails at `D` from cover fail with leftover `{e_2}` (1-in 1-out).
Neighbor-read(D) is therefore fail, not `UNDEFINED`. Mixed remains a set
at `C`'s outgoing `{+e_1,−e_1,+e_3,−e_3}` and at `B`'s mixed `(1,1,2)`.
`QED`

## Theorem 2 — Reverse Neighbor-Read

**Claim.** Reverse neighbor-read at `τ` is hold, not fail and not
`UNDEFINED`.

**Proof.** Reverse HOLDs iff neighbor-read HOLDs at `A` and at `B`. Both
probes are formed, so the pair is not `UNDEFINED`. Theorem 1 gives
neighbor-read(A) = hold and neighbor-read(B) = hold, hence
Reverse neighbor-read at τ: hold.
`QED`

## Theorem 3 — Face Neighbor-Read, Displayed Not Adopted

**Claim.** Face neighbor-read at `τ` is fail, not hold and not
`UNDEFINED`. The bit is displayed, not adopted.

**Proof.** Face HOLDs iff neighbor-read HOLDs at `C` and at `D`. Theorem 1
gives neighbor-read(C) = fail and neighbor-read(D) = fail, hence
Face neighbor-read at τ: fail. The report is a finite listing on this
seed and these four y-probes. It is displayed, not adopted as an
Admissibility clause, as a lettering law, or as a uniqueness rule. Do not
write into Admissibility. Do not attach L1.
`QED`

## Discriminators

Neighbor-read of `M` as signed sets fails at `A` and at `C`, and HOLDs at
`B` and at `D`. Neighbor-read of `O` as signed sets fails at every
y-probe. Signed `(M, O)` set equality fails at every y-probe: no formed
six-neighbor recovers both lock sets as sets. The present letter recovers
the unsigned 1-in 2-out axis assignment at `A` and at `B`, so reverse
HOLDs, while `C` has split HOLD without a matching neighbor, so face
fails. It is therefore not leftover of nm2ready neighbor-read of M and not
leftover of nm2oready neighbor-read of O.

The same y-probes on a two-site `±e_1` seed reverse/face as hold/fail, but
that member forms `B` at tick 2 and `D` at tick 3 and treats `(0,0,1)` as
a formed child, not a seed. A perpendicular two-site seed and a
z-symmetric three-site seed do not reproduce hold/fail. The same two-axis
opposite seed scored on z-probes returns hold/hold, and on x-probes
returns fail/fail. The report is therefore not leftover of nm2ax12 1-in
2-out split without neighbor-read and not leftover of nm2sreadz z-probe
neighbor-read of the 1-in 2-out split.

## Exact Target And Proof Obligations

**Exact target:** report neighbor-read of the 1-in 2-out split at `t+1` on
the four y-probes of the two-axis opposite seed, and the reverse/face
pair-read of those bits, on Euclidean `B_3(0)`.

| Obligation | Disposition |
|---|---|
| name the seed, perp-step rule, host, and y-probes | displayed process, closed on `B_3(0)` |
| list `t`, `M`, `O`, split, formed six-neighbor bits, and neighbor-read | Theorem 1, finite listing |
| reverse pair-read of `A` and `B` | Theorem 2, hold |
| face pair-read of `C` and `D` | Theorem 3, fail, displayed not adopted |
| adopt reverse or face as Admissibility | not claimed |
| attach a uniqueness cut | not claimed |
| lattice-wide lettering | not claimed; no global T |

The proof-obligation graph is acyclic. The leaves are finite listings on
a 123-site ball. No observational value is used.

## No-Go Discipline Gate

This note is a displayed finite report, not a negative law. Broad negative
inference from the reverse hold, from the face fail, or from leftover
signed-set misses is **FAIL / DO NOT SHIP**.

### N1 — materially distinct route scan

Neighbor-read of the unsigned 1-in 2-out assignment, neighbor-read of `M`,
neighbor-read of `O`, signed `(M, O)` set equality, axis-cover without
`|Axis(M)|=1`, unique-letter cuts, and a rewritten Admissibility rule are
distinct objects. Only the first is executed here, and only on four
y-probes. The others are named leftovers or out of scope. No universal
negative is claimed, so a no-go is not shipped.

### N2 — wall independence

There is no shipped wall. Reverse hold and face fail are pair-reads of
the four neighbor-read bits. Removing either pair changes the report
without creating a law-level obstruction.

### N3 — hidden-condition scan

Load-bearing and explicit: two-axis opposite seed, perp-step
`s·e_i=0`, incoming lock, Euclidean `B_3(0)`, `τ(q)=t(q)+1`, split HOLD
together with unsigned axis equality of `M` and of `O`, and the four named
y-probes. No phrase such as "by construction" or "naturally" adds a
further premise. Occupancy of sites is not used.

### N4 — residual matching

No prior negative is cited as evidence. The only linked premise document
is the current axiom memo, used to quote Lattice, Qubit, Record, and the
Admissibility non-supply of formation site. The listing is proved here.

### N5 — resolution audit

| Resolution | Executed? | Exact scope |
|---|---:|---|
| per element | yes | each 1-in 2-out axis assignment of `M` and `O` at a probe and at formed six-neighbors, compared as unsigned axes at that probe's `t+1` |
| per site | yes | y-probes `A,B,C,D` on Euclidean `B_3(0)` only |
| per mode | no | no spectral or mode calculation is executed on this finite host |
| per block | yes | four neighbor-read reports, reverse/face from those bits |
| lattice-wide | checked and not executed | no lattice-wide lettering rule is claimed; no global T |

### N6 — partial-closure paths

Live extensions already named: other seeds, other probe axes, a uniqueness
cut, signed-set leftover, a larger host, or an Admissibility rewrite. None
is closed by this listing, and none is dismissed as requiring a new axiom.

### N7 — steelman

The strongest objection to reading reverse HOLD and face fail as a law is
decisive: both bits are pair-reads of probe reports on one displayed seed.
Neighbor-read of `M` fails at `A`, neighbor-read of `O` fails at `A` and at
`B`, and signed `(M, O)` equality fails at every y-probe. Split HOLDs at
`C` while neighbor-read fails at `C`. That is why Theorem 3 is displayed,
not adopted.

### N8 — cross-cycle echo

Investment names `nm2ax`, `nm2ax12`, `nm2ready`, `nm2oready`, and
`nm2sreadz` mark nearby displayed processes. This note reuses the same
two-axis opposite seed and y-probes only to report neighbor-read of the
1-in 2-out split at `t+1`. It does not inherit an axis-cover claim, a
split-without-read claim, or a signed-set neighbor-read as a theorem.

**No-Go Discipline status:** FAIL / DO NOT SHIP for any negative
Admissibility, lettering, or uniqueness claim. The positive finite listing
in Theorems 1–3 remains a displayed bounded report.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite neighbor-read of the 1-in 2-out split at t+1 on four y-probes, with reverse/face pair-read, on Euclidean B_3(0); displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_neighbor_read_one_two_split_tplus1_reverse_face
target_blocker_text: "report neighbor-read of the 1-in 2-out split at t+1 on the two-axis opposite y-probes and the reverse/face pair of those bits"
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
| neighbor-read of the 1-in 2-out split, reverse, face | reported bits | Theorems 1–3 |
| Admissibility rewrite, L1, uniqueness cut | residual | open and not claimed |

Independent audit remains required before any effective status may change.
