---
claim_id: two_axis_opposite_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+2 versus t+3 on the four y-probes of the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py
---

# Two-Axis Opposite Y-Probe Simultaneous Incoming And Outgoing Freeze t+2 Versus t+3

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** Simultaneous M and O at t+2 versus t+3 on the four y-probes of the
two-axis opposite seed, reverse/face at each cut, and composition, are
reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py)

No runner cache is written.

## Result Up Front

On the Euclidean host `B_3(0) = {n : n · n <= 9}`, the two-axis opposite
seed is four tick-0 sites: origin locks `+e_1`, `(0,1,0)` locks `−e_1`,
`(0,0,1)` locks `+e_2`, and `(0,1,1)` locks `−e_2`. The second pair is a new
seed, not a formed child. Growth is perp-step with incoming lock: a
six-neighbor step `s` from a parent locked along `e_i` is allowed only when
`s · e_i = 0`. Newly formed sites lock the incoming step. Seeds keep their
seed letters as a singleton.

Let `t(q)` be the formation tick of site `q`. Cuts are local:
`τ1(q) = t(q) + 2` and `τ2(q) = t(q) + 3`. There is no global T. Do not score τ=t. `M(q, τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Unformed at `τ` is
UNDEFINED. The own outgoing set `O(q, τ)` is the dual of `M`: the set of
`e` in `{±e_1, ±e_2, ±e_3}` such that `q+e` is formed and `e` is in
`M(q+e, τ)`. Unformed `q` at `τ` is UNDEFINED. Empty `O` is empty, not
UNDEFINED. Mixed lock vectors stay a set: uniqueness is not required.

Simultaneous HOLDs at `q, τ` iff both `M` and `O` are defined nonempty and
`M ∩ O` is empty. UNDEFINED if `M` or `O` is UNDEFINED. Else fail. Reverse
at a cut HOLDs iff simultaneous HOLDs at `A` and at `B`. Face likewise on
`C, D`. This is HOLD iff simultaneous, not leftover-empty fail. Composition
holds iff `M(τ1)=M(τ2)` and `O(τ1)=O(τ2)` at `A, B, C,` and `D`. Displayed,
not adopted. Do not write into Admissibility. Do not attach L1.
Occupancy of sites is not used. Occupancy `n` is not used. The construction
does not use occupancy.

The four y-probes are `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`.
Probe A is the seed site `(0,1,0)`.

**Theorem 1.** Formation ticks, `M`, `O`, and sim at `τ1` and `τ2`:

- t(A)=0
- t(B)=1
- t(C)=1
- t(D)=2
- M(A, τ1) = {−e_1}
- M(B, τ1) = {+e_1}
- M(C, τ1) = {+e_2}
- M(D, τ1) = {−e_3}
- O(A, τ1) = {+e_2, −e_3}
- O(B, τ1) = {+e_2, +e_3, −e_3}
- O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}
- O(D, τ1) = {+e_1, −e_1}
- sim(A, τ1) = hold
- sim(B, τ1) = hold
- sim(C, τ1) = hold
- sim(D, τ1) = hold
- M(A, τ2) = {−e_1}
- M(B, τ2) = {+e_1}
- M(C, τ2) = {+e_2}
- M(D, τ2) = {−e_3}
- O(A, τ2) = {+e_2, −e_3}
- O(B, τ2) = {+e_2, +e_3, −e_3}
- O(C, τ2) = {+e_1, −e_1, +e_3, −e_3}
- O(D, τ2) = {+e_1, −e_1}
- sim(A, τ2) = hold
- sim(B, τ2) = hold
- sim(C, τ2) = hold
- sim(D, τ2) = hold

M and O both freeze from `τ1` to `τ2` at every probe. Intersection is empty
at each probe at each cut. Simultaneous HOLDs at each probe at each cut.
New six-neighbor records of each probe:

- new 6-NN of A at t(A)+2: (1, 1, 0), (-1, 1, 0)
- new 6-NN of B at t(B)+2: none
- new 6-NN of C at t(C)+2: none
- new 6-NN of D at t(D)+2: none
- new 6-NN of A at t(A)+3: none
- new 6-NN of B at t(B)+3: (2, 1, 1)
- new 6-NN of C at t(C)+3: none
- new 6-NN of D at t(D)+3: none

The t(A)+2 neighbors `(1, 1, 0)` and `(-1, 1, 0)` form with earliest
incoming `−e_3`, so `+e_1` and `−e_1` do not enter `O(A, τ1)`. The t(B)+3
neighbor `(2, 1, 1)` forms with earliest incoming `{−e_2, +e_3, −e_3}`, so
`+e_1` does not enter `O(B, τ2)`. O is not M: at A, `M = {−e_1}` while
`O = {+e_2, −e_3}`. Scoring `τ=t` is leftover of nmot2opp: `O(A, t)` is
empty, so simultaneous fails at A, B, and C at formation, while `O(D, t) =
{−e_1}` is already nonempty. Do not score τ=t.

**Theorem 2.** Reverse and face at each cut, from simultaneous HOLD.

- Reverse at τ1: hold
- Reverse at τ2: hold
- Face at τ1: hold
- Face at τ2: hold

Reverse holds at τ1 and at τ2 because simultaneous HOLDs at A and at B at
both cuts. Face holds at τ1 and at τ2 because simultaneous HOLDs at C and
at D at both cuts. Empty-or-UNDEFINED remains UNDEFINED; the reverse and
face sides are nonempty simultaneous HOLDs, so the report is hold rather
than UNDEFINED. This is HOLD iff simultaneous, not leftover-empty fail:
leftover of the unsigned-axis union is empty at A, B, and C, leftover at D
is `{e_2}`, so leftover reverse fails and leftover face fails.

**Theorem 3.** Composition hold if `M(τ1)=M(τ2)` and `O(τ1)=O(τ2)` at A, B,
C, D.

- Composition of M and O: hold

Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
The report is not leftover of nm2simt2y (simultaneous freeze t+1 versus t+2,
no t+3 cut), not leftover of nm2simy (simultaneous at t+1 alone, no t+2
cut), not leftover of nm2ot3y (O freeze only, reverse/face from
exist-opposite of O), not leftover of nmot2opp (O at t versus t+1; Do not
score τ=t), not leftover of nmt2opp (M two-tick exist-opposite), not leftover
of nm2axo timed-O exist-opposite, not leftover of leftover-empty fail, and
not leftover of unsigned axis-cover. It is not named-sign lettering: a named
sign would have lost the axis. It is not a unique lock-vector leftover and
does not sum. It does not use a six-neighbor star. It does not attach a
formation member from already-recorded six-neighbor locks. It is not the
two-tick lock-count clock composition.

No larger host is used.

## Current Premise Boundary

Quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

Reading note (2) of Admissibility: the distribution concerns which
possibility a forming record locks, conditional on formation at that site;
it does not supply the formation site, probability, or rate.

Records form.

The present letter is a finite listing of simultaneous `M` and `O` on four
named sites of one seed at two local cuts. It does not enlarge Admissibility
and does not attach L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact listing of simultaneous M and O at t+2 versus t+3 on four y-probes, reverse/face at each cut, and M-and-O composition; displayed, not adopted."
trace_class: bounded_theorem
target_claim_id: two_axis_opposite_yprobe_simultaneous_incoming_outgoing_tplus2_tplus3
target_blocker_text: "display simultaneous M and O freeze t+2 versus t+3 reverse/face composition on the two-axis opposite y-probes"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the listing displayed; do not write the composition into Admissibility and do not attach L1."
conditional_surface_status: "exact on Euclidean B_3(0) for this seed and these four y-probes"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Host: Euclidean closed ball `B_3(0) = { n : n · n <= 9 }`. No larger host
is used.

Seed at tick 0, two disjoint opposite pairs:

- origin `+e_1`
- `(0,1,0)` `−e_1`
- `(0,0,1)` `+e_2`
- `(0,1,1)` `−e_2`

The second pair is a new seed, not a formed child of the first pair.

Process: perp-step, incoming lock. A 6-NN step is allowed iff it is
perpendicular to the parent lock axis (`s · e_i = 0`). Newly formed sites
lock the incoming step.

Y-probes: `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. Probe A is
the seed site `(0,1,0)`, distinct from the z-probe and x-probe A sites.

`M(q, τ)` earliest incoming from records with tick `<= τ`. `O(q, τ)` is
the own outgoing set defined above. Unformed at `τ` ⇒ UNDEFINED.

## No-Go Discipline Gate

The listing is a displayed finite report. It is not an axiom edit, not a
formation-member attachment, and not a lattice-wide lettering rule.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| simultaneous M and O freeze | score M and O at τ1 versus τ2, reverse/face from sim | executed; freeze holds; composition of M and O holds |
| simultaneous freeze t+1 versus t+2 | drop the t+3 cut | leftover of nm2simt2y; not this freeze letter |
| simultaneous at t+1 only | drop the t+2 and t+3 cuts | leftover of nm2simy; not this freeze letter |
| O freeze only | compose O, ignore M, reverse/face from exist-opposite of O | leftover of nm2ot3y; not joint M-and-O composition |
| score at τ=t | use M and O at formation tick | leftover of nmot2opp; O empty at A so sim fails; not this letter |
| M exist-opposite | reverse/face on M not simultaneous | leftover of nmt2opp; reverse holds and face fails; O is not M |
| timed-O exist-opposite | reverse/face on O as exist-opposite | leftover of nm2axo timed-O exist-opposite; pair test is not sim HOLD |
| leftover-empty fail | unsigned leftover axis empty => fail | leftover reverse fails and leftover face fails; not this letter |
| axis-cover | unsigned axes of M and O | leftover of axis-cover; cover reverse holds while cover face fails |
| unique lock vector | require a singleton letter | leftover of unique-L; mixed O is UNDEFINED as a unique letter |
| one-axis seed | drop the second opposite pair | leftover child process; second pair is a new seed |

### N2 — wall independence

The seed, the host ball, the perp-step rule, the simultaneous predicate, the
two local cuts, and reverse/face from simultaneous HOLD are distinct inputs.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The Euclidean ball, four-site opposite seed, perp-step incoming lock, local
`τ1`/`τ2` cuts, and simultaneous HOLD on M and O are declared. Occupancy
counts, unique letters, vector sums, axis-cover, z-probes, one-axis leftover
children, and a global clock are not silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, the one-site possibility
domain `M_2(C)`, record lock of one admissible possibility, and the
boundary that Admissibility does not supply the formation site,
probability, or rate. The residual is a finite displayed listing, not an
axiom edit.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each signed lock among {±e_1,±e_2,±e_3} in M or in O at a probe's t+2 and t+3 | no unique-letter classification |
| per site | scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites | no lattice-wide lettering |
| per mode | no spectral or mode calculation is executed on this finite host | no mode exhaustion |
| per block | four sim reports at t+2 and t+3, reverse/face at each cut, composition of M and O | no Admissibility rewrite |
| lattice wide | checked and not executed — no lattice-wide lettering rule is claimed | no global letter |

### N6 — live partial-closure paths

Live routes include other seeds, other probe families, other cuts, and any
later decision to adopt a letter into Admissibility. Those routes are
outside this displayed listing.

### N7 — hostile steelman

**Steelman:** Because M and O both freeze from τ1 to τ2, reverse and face
should be scored as composition, or composition should be scored on O
alone as in nm2ot3y.

**Answer:** Composition of this letter is equality of both M and O at the
four probes. Reverse holds and face holds at both cuts from simultaneous
HOLD. Bit-stability of reverse/face is a leftover predicate; O-only freeze
is leftover of nm2ot3y. Composition of M and O: hold. Axis-cover face still
fails at D, leftover-empty face fails, and M exist-opposite face fails, so
hold/hold of simultaneous is not those leftovers. Freeze at t+1 versus t+2
is leftover of nm2simt2y; this letter scores the later local cuts t+2 and
t+3.

### N8 — cross-cycle echo

This is not leftover of nm2simt2y simultaneous freeze t+1 versus t+2, not
leftover of nm2simy simultaneous at t+1 alone, not leftover of nm2ot3y O
freeze, not leftover of nmot2opp O at t versus t+1, not leftover of nmt2opp
M two-tick, not leftover of nm2axo timed-O exist-opposite, and not leftover
of leftover-empty fail. The second pair is a new seed, not a formed child.
Do not attach L1.

**Gate disposition:** PASS for the finite listing of simultaneous M and O
at τ1 and τ2, reverse/face at each cut, and displayed composition. FAIL / DO NOT SHIP
for writing the composition into Admissibility, attaching L1, or treating
the listing as a lattice-wide letter.

## Primary Runner

The primary runner recomputes formation on `B_3(0)`, the four y-probe
incoming and outgoing sets at `τ1` and `τ2`, simultaneous, reverse, face,
and composition, plus leftover mutations. It authors no audit verdict. No
runner cache is written.
