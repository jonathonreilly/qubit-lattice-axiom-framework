---
claim_id: two_axis_opposite_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "O at t+1 versus t+2 on the four y-probes of the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Two-Axis Opposite Y-Probe Own Outgoing Set Freeze t+1 Versus t+2

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** O at t+1 versus t+2 on the four y-probes of the two-axis
opposite seed, reverse/face at each cut, and composition, are reported.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_own_outgoing_set_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

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
`τ1(q) = t(q) + 1` and `τ2(q) = t(q) + 2`. There is no global T. Do not score τ=t. `M(r, τ)` is the set of earliest incoming nearest-neighbor
steps at `r` using only records with tick `<= τ`. Unformed at `τ` is
UNDEFINED. The own outgoing set `O(q, τ)` is the dual of `M`: the set of
`e` in `{±e_1, ±e_2, ±e_3}` such that `q+e` is formed and `e` is in
`M(q+e, τ)`. Unformed `q` at `τ` is UNDEFINED. Empty `O` is empty, not
UNDEFINED. Mixed lock vectors stay a set: uniqueness is not required, and
this is not leftover of unique-L.

Reverse at a cut HOLDs iff some `a` in `O(A, τ)` and some `b` in `O(B, τ)`
have `a+b=(0,0,0)`. Face likewise on `C, D`. Empty or UNDEFINED on either
side is UNDEFINED; nonempty with no opposite pair fails. Composition of `O`
holds iff `O(τ1)=O(τ2)` at `A, B, C,` and `D`. Displayed, not adopted. Do
not write into Admissibility. Do not attach L1.

The four y-probes are `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`.
Probe A is the seed site `(0,1,0)`.

**Theorem 1.** Formation ticks and own outgoing sets at `τ1` and `τ2`:

- t(A)=0
- t(B)=1
- t(C)=1
- t(D)=2
- O(A, τ1) = {+e_2, −e_3}
- O(B, τ1) = {+e_2, +e_3, −e_3}
- O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}
- O(D, τ1) = {+e_1, −e_1}
- O(A, τ2) = {+e_2, −e_3}
- O(B, τ2) = {+e_2, +e_3, −e_3}
- O(C, τ2) = {+e_1, −e_1, +e_3, −e_3}
- O(D, τ2) = {+e_1, −e_1}

O freezes from `τ1` to `τ2` at every probe. New six-neighbor records of
each probe:

- new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)
- new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
- new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
- new 6-NN of D at t(D)+1: (2, 1, 0)
- new 6-NN of A at t(A)+2: (1, 1, 0), (-1, 1, 0)
- new 6-NN of B at t(B)+2: none
- new 6-NN of C at t(C)+2: none
- new 6-NN of D at t(D)+2: none

The t(A)+2 neighbors `(1, 1, 0)` and `(-1, 1, 0)` form with earliest
incoming `−e_3`, so `+e_1` and `−e_1` do not enter `O(A, τ2)`. O is not M:
at A, `M = {−e_1}` while `O = {+e_2, −e_3}`. Scoring `τ=t` is leftover of
nmot2opp: `O(A, t)` is empty, so reverse at formation is UNDEFINED, while
`O(D, t) = {−e_1}` is already nonempty and is not the freeze letter.

**Theorem 2.** Reverse and face at each cut.

- Reverse at τ1: hold
- Reverse at τ2: hold
- Face at τ1: hold
- Face at τ2: hold

Reverse holds at τ1 and at τ2. The witnessing opposite pair is `−e_3` in
`O(A)` against `+e_3` in `O(B)`. Face holds at τ1 and at τ2. The witnessing
opposite pair is `+e_1` in `O(C)` against `−e_1` in `O(D)`. Empty-or-UNDEFINED
remains UNDEFINED; the reverse and face sides are nonempty, so the report
is hold rather than UNDEFINED.

**Theorem 3.** Composition hold if `O(τ1)=O(τ2)` at A, B, C, D.

- Composition of O: hold

Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
The report is not leftover of nmot2opp (O at t versus t+1; Do not score
τ=t), not leftover of nmt2opp (M two-tick exist-opposite), not leftover of
nmoutopp (eventual O with no t+1 versus t+2 cut), not leftover of
axis-cover, not leftover of M exist-opposite, and not leftover of z-probe
O exist-opposite. It is not named-sign lettering: a named sign would have
lost the axis. It is not a unique lock-vector leftover and does not sum;
it is not a sum leftover. It does not use a six-neighbor star. It does not
attach a formation member from already-recorded six-neighbor locks. It is
not the two-tick lock-count clock composition.

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

The present letter is a finite listing of own outgoing sets on four named
sites of one seed. It does not enlarge Admissibility and does not attach
L1.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact listing of O at t+1 versus t+2 on four y-probes, reverse/face at each cut, and O-set composition; displayed, not adopted."
trace_class: bounded_theorem
target_claim_id: two_axis_opposite_yprobe_own_outgoing_set_tplus1_tplus2
target_blocker_text: "display O freeze t+1 versus t+2 reverse/face composition on the two-axis opposite y-probes"
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

`M(r, τ)` earliest incoming from records with tick `<= τ`. `O(q, τ)` is
the own outgoing set defined above. Unformed at `τ` ⇒ UNDEFINED.

## No-Go Discipline Gate

The listing is a displayed finite report. It is not an axiom edit, not a
formation-member attachment, and not a lattice-wide lettering rule.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| own outgoing set freeze | score O at τ1 versus τ2 | executed; freeze holds; composition of O holds |
| score at τ=t | use O at formation tick | leftover of nmot2opp; O empty at A so reverse UNDEFINED; not this letter |
| M exist-opposite | reverse/face on M not O | leftover of nmt2opp; reverse holds and face fails; O is not M |
| eventual O | drop the t+1 versus t+2 cut | leftover of nmoutopp; not this freeze letter |
| axis-cover | unsigned axes of M and O | leftover of axis-cover; cover reverse holds while cover face fails |
| unique lock vector | require a singleton letter | leftover of unique-L; mixed O is UNDEFINED as a unique letter |
| sum of lock vectors | replace exist-opposite by a vector sum | not a sum leftover; mixed A sums to `+e_2−e_3` and does not cancel |
| z-probes or x-probes | move the four sites | z-probe reverse holds and face fails; x-probe both fail; not these y-probes |
| one-axis seed | drop the second opposite pair | leftover child process; `O(A)` keeps `+e_3` |
| named-sign | replace the lock vector by `+`/`-` | not named-sign lettering; a named sign would have lost the axis |

### N2 — wall independence

The seed, the host ball, the perp-step rule, the own-outgoing dual of M,
the two local cuts, and the exist-opposite reverse/face predicate are
distinct inputs. This note claims no complete wall collection.

### N3 — hidden-condition scan

The Euclidean ball, four-site opposite seed, perp-step incoming lock, local
`τ1`/`τ2` cuts, and exist-opposite on O are declared. Occupancy counts,
unique letters, vector sums, axis-cover, z-probes, one-axis leftover
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
| per element | each lock vector in the probe's own outgoing set O(q, tau) | no unique-letter classification |
| per site | scored only at y-probes A,B,C,D on Euclidean B_3(0); no other sites | no lattice-wide lettering |
| per mode | no spectral or mode calculation is executed on this finite host | no mode exhaustion |
| per block | four outgoing sets at t+1 and t+2 plus reverse/face/composition | no Admissibility rewrite |
| lattice wide | checked and not executed — no lattice-wide lettering rule is claimed | no global letter |

### N6 — live partial-closure paths

Live routes include other seeds, other probe families, other cuts, and any
later decision to adopt a letter into Admissibility. Those routes are
outside this displayed listing.

### N7 — hostile steelman

**Steelman:** Because O freezes from τ1 to τ2, reverse and face should be
scored as composition, or composition should be scored on the reverse/face
bits.

**Answer:** Freeze of O is composition of the four sets. Reverse holds and
face holds at both cuts. Bit-stability of reverse/face is a leftover
predicate; this letter scores equality of the O sets themselves.
Composition of O: hold. Axis-cover face still fails at D, and M face still
fails, so hold/hold of signed O is not those leftovers.

### N8 — cross-cycle echo

This is not leftover of nmot2opp O at t versus t+1, not leftover of nmt2opp
M two-tick, not leftover of nmoutopp eventual-O, not leftover of
axis-cover, and not leftover of z-probe O exist-opposite. The second pair
is a new seed, not a formed child. Do not attach L1.

**Gate disposition:** PASS for the finite listing of O at τ1 and τ2,
reverse/face at each cut, and displayed composition. FAIL / DO NOT SHIP
for writing the composition into Admissibility, attaching L1, or treating
the listing as a lattice-wide letter.

## Primary Runner

The primary runner recomputes formation on `B_3(0)`, the four y-probe
outgoing sets at `τ1` and `τ2`, reverse, face, and composition, plus
leftover mutations. It authors no audit verdict. No runner cache is
written.
