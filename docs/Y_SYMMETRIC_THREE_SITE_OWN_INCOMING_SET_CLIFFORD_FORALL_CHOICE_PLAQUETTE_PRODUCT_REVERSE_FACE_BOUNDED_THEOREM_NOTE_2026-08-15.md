---
claim_id: y_symmetric_three_site_own_incoming_set_clifford_forall_choice_plaquette_product_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from forall-choice Cl(3,0) 4-cycle products of own incoming sets on #7175 Q and R are reported. No S⁺. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_symmetric_three_site_own_incoming_set_clifford_forall_choice_plaquette_product_reverse_face_2026_08_15.py
---

# Own Incoming Set Forall-Choice Cl(3,0) Plaquette Product Reverse And Face On #7175 Q And R

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from forall-choice `Cl(3,0)` 4-cycle products of
own incoming sets `M(q)` on nsyopinc #7175 face plaquette `Q` and reverse
4-cycle `R` in `B_3(0)={n:n·n<=9}`. Same process as nsyopp #7132 / nsyopinc
#7175. Let `t(q)` be the formation tick of site `q`. `M(q)` is the set of
earliest incoming nearest-neighbor steps at `q`. Seeds use their seed letter
as a singleton. Mixed stays a set. Unformed is `UNDEFINED`. Identify `±e_i`
with generators `γ_i` of `Cl(3,0)`: `γ_i²=+1`, `γ_i γ_j=−γ_j γ_i` (`i≠j`);
`−e_i` maps to `−γ_i`. Displayed algebra, not a cube-Pauli Lattice action.
At a 4-cycle `V=(v0,v1,v2,v3)`, a pick is one letter from each `M(vi)` at
that site's own `t` (no `T_Q`). `U` is the `Cl(3,0)` product of the four
picked units. Exist-choice HOLD iff some pick has `U` equal to the scalar
`±1` (comparison). Forall-choice HOLD iff every pick has `U` equal to the
scalar `±1` (`N_hold=N_picks` and `N_picks≥1`). If any vertex is unformed or
`M` is `UNDEFINED` or empty, the report is `UNDEFINED`. Else fail.
Unique-L product is comparison only. It is not the theorem. Unique `L` is
`UNDEFINED` when mixed. The six-neighbor star `S^+` is not the letter.
Occupancy `n` is not used. This is not named-sign lettering. This is not a
unique lock-vector leftover. This is not leftover of unique-L. This is not
leftover of exist-choice: nmclsy `N_hold(Q)=4` is some-picks extra, not a
determined `Cl` member. This is not leftover of #7175 `S^+`. This is
independent of nmclall #7167. No S⁺. Uniqueness of incoming locks is not
required. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1. This note does not write forall-choice into Admissibility and
does not attach a formation member from already-recorded six-neighbor
locks. This display does not use occupancy. Mixed stays a set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_symmetric_three_site_own_incoming_set_clifford_forall_choice_plaquette_product_reverse_face_2026_08_15.py`](../scripts/y_symmetric_three_site_own_incoming_set_clifford_forall_choice_plaquette_product_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the named 4-cycles `Q` and `R`. Incoming lock letters are unit
nearest-neighbor steps. Reverse and face are scored on whether every pick
from the own incoming sets has `Cl(3,0)` product the scalar `±1`. Named
signs `{+,−}` are a coarser readout and are not used. A singleton unique
lock-vector letter is a different readout and is not used as the object:
report `M` and forall-choice over picks. Unique-L product is comparison
only. Exist-choice is comparison only. A `Z^3` sum of those locks is a
different readout and is not used. The construction does not sum. No S⁺.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of M at the four Q vertices and the four R vertices on the #7175 process, mixed stays a set, with N_picks and N_hold, unique-L letters if defined, reverse forall-choice fail from some-picks extra, and face forall-choice fail; exist-choice reverse and face hold as comparison; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_symmetric_three_site_own_incoming_set_clifford_forall_choice_plaquette_product_reverse_face
target_blocker_text: "display reverse and face from forall-choice Cl(3,0) 4-cycle products of own incoming sets on #7175 Q and R, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write forall-choice into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the report with unique-L leftover, do not identify the report with exist-choice leftover, do not identify the letter with #7175 S^+ leftover, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for forall-choice Cl(3,0) products of own incoming sets on #7175 Q and R; displayed, not adopted"
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

No larger host is used. The scored 4-cycles are

```text
Q = (0, e_1, e_1+e_2, e_2) cyclic
  = {(0,0,0),(1,0,0),(1,1,0),(0,1,0)}
R = {(0,1,0),(1,1,0),(1,1,1),(0,1,1)} cyclic
```

`R` is the reverse 4-cycle containing y-probes `A=(0,1,0)` and `B=(1,1,1)`.
`Q` is the face plaquette. These are not x-probes. Same process and y-probes
as nsyopinc #7175. Same process as nsyopp #7132.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,1,0), (0,-1,0)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,1,0)=−e_1`, and `L(0,-1,0)=−e_1`. The
third site is the y-mirror of the two-site opposite-lock partner `(0,1,0)`.
This seed is not the two-site opposite-lock seed `{0,(0,1,0)}` of nmclall
#7167. This seed is not the three-site opposite-lock seed whose third site
is `(1,0,0)` with lock `+e_2`. This seed is not the perp two-site seed
`+e_1/+e_2`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Mixed stays a set. Uniqueness is not required. A later parent
does not re-form `q`.

## Named forall-choice Cl(3,0) product from own incoming sets

Let `t(q)` be the formation tick of site `q` when that tick is defined in
`B_3(0)`. Let `M(q)` be the set of earliest incoming nearest-neighbor steps
at `q`. Seeds use their seed letter as a singleton. Mixed stays a set.
Unformed is `UNDEFINED`. Unique `L(q)` is not used as the letter. Unique-L
product is comparison only. Exist-choice is comparison only. This display
does not use a six-neighbor star. Occupancy `n` is not used. Duplicate
incoming steps collapse in the set. The construction does not require
`M(q)` to be a singleton. It does not sum `M(q)`. It is not a unique
lock-vector leftover. It is not leftover of unique-L. It is not leftover of
exist-choice. It is not leftover of #7175 same-tick union own `S^+`.

Identify `±e_i` with generators `γ_i` of displayed `Cl(3,0)`:

```text
γ_i² = +1
γ_i γ_j = −γ_j γ_i   (i ≠ j)
−e_i  |->  −γ_i
+e_i  |->  +γ_i
```

This is a displayed algebra, not a cube-Pauli Lattice action.

At a 4-cycle `V=(v0,v1,v2,v3)`, a pick is one letter from each `M(vi)` at
that site's own `t` (no `T_Q`). `U` is the `Cl(3,0)` product of the four
picked units in cyclic order. Exist-choice HOLD iff some pick has `U` equal
to the scalar `±1` (comparison). Forall-choice HOLD iff every pick has `U`
equal to the scalar `±1` (`N_hold=N_picks` and `N_picks≥1`). If any vertex
is unformed or `M` is `UNDEFINED` or empty, the report is `UNDEFINED`. Else
the report fails if some pick is not scalar `±1`. The report is one of
`hold`, `fail`, or `UNDEFINED`. Determined readout versus some-picks extra
is the distinction: exist-choice HOLD does not pin a `Cl` member.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on whether
every four-letter pick has `Cl(3,0)` product scalar `±1`. They are not
scored on `{+,−}` names and are not an occupancy-kernel inner product.

Admissibility is not edited. Forall-choice is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — own incoming sets, N_picks, N_hold

Direct enumeration of the displayed nsyopp #7132 process on `B_3(0)` forms
all four `Q` vertices and all four `R` vertices.

Own incoming sets at each vertex's own formation tick are:

```text
Q:
  0         t=0;  M(0) = {+e_1};                 L(0) = +e_1
  e_1       t=3;  M(e_1) = {+e_3, −e_3};         L(e_1) = UNDEFINED
  e_1+e_2   t=3;  M(e_1+e_2) = {−e_2, +e_3, −e_3}; L(e_1+e_2) = UNDEFINED
  e_2       t=0;  M(e_2) = {−e_1};               L(e_2) = −e_1
R:
  (0,1,0)   t=0;  M(A) = {−e_1};                 L(A) = −e_1
  (1,1,0)   t=3;  M(D) = {−e_2, +e_3, −e_3};     L(D) = UNDEFINED
  (1,1,1)   t=2;  M(B) = {+e_1};                 L(B) = +e_1
  (0,1,1)   t=1;  M((0,1,1)) = {+e_3};           L((0,1,1)) = +e_3
```

Mixed stays a set: `M(e_1)` has two earliest incoming steps and
`M(e_1+e_2)=M(D)` has three. Unique-L leftover assigns `UNDEFINED` at those
mixed vertices. Unique-L letters if defined are the singletons above.
Unique-L product on `Q` is `UNDEFINED`. Unique-L product on `R` is
`UNDEFINED`. Unique-L product is comparison only. It is not the theorem.

Forall-choice counts:

```text
N_picks(Q) = 6
N_hold(Q) = 4
N_picks(R) = 3
N_hold(R) = 2
```

`N_picks(Q)=1·2·3·1=6`. Four of those picks have `U=±1`; the two misses pick
`−e_2` at `e_1+e_2`. `N_picks(R)=1·3·1·1=3`. Two of those picks have
`U=±1`; the miss picks `−e_2` at `D`. Holding picks on `Q`:

```text
(+e_1, +e_3, +e_3, −e_1) -> U = −1
(+e_1, +e_3, −e_3, −e_1) -> U = +1
(+e_1, −e_3, +e_3, −e_1) -> U = +1
(+e_1, −e_3, −e_3, −e_1) -> U = −1
```

Holding picks on `R`:

```text
(−e_1, +e_3, +e_1, +e_3) -> U = +1
(−e_1, −e_3, +e_1, +e_3) -> U = −1
```

The extra picks are not scalar `±1`:

```text
(+e_1, +e_3, −e_2, −e_1) not scalar
(+e_1, −e_3, −e_2, −e_1) not scalar
(−e_1, −e_2, +e_1, +e_3) not scalar
```

Incoming locks exist and need not be unique. Uniqueness is not required.
`N_hold(Q)=4` is not `N_picks(Q)=6`. Exist-choice HOLD is some-picks extra;
it does not pin a `Cl` member. The two-site opposite-lock leftover (nmclall
#7167) uses seed `{0,(0,1,0)}` and reports `M(e_1)={+e_2, +e_3, −e_3}` with
`N_picks(Q)=9`, not the two-element `M(e_1)` of this display. This report is
independent of nmclall #7167.

## Theorem 2 — reverse forall-choice hold / fail / UNDEFINED

Reverse forall-choice holds if and only if every pick from `M` at the four
`R` vertices has `Cl(3,0)` product `U` equal to the scalar `±1`, with
`N_picks≥1`. All four vertices are formed with nonempty `M`.
`N_hold(R)=2≠3=N_picks(R)`, so reverse fails.

Reverse: fail

exist-choice reverse: hold

Exist-choice reverse is comparison only. Some pick has `U=±1`, so
exist-choice reverse holds. Unique-L leftover reports unique-L product
`UNDEFINED` from mixed `D`. Unique-L product is comparison only. Forall-
choice still sees one extra pick that is not scalar `±1`. #7175 `S^+`
leftover is not the letter. Reverse fails because not every pick from the
own incoming sets on `R` multiplies to scalar `±1`.

Reverse fails.

## Theorem 3 — face forall-choice hold / fail / UNDEFINED

Face forall-choice holds if and only if every pick from `M` at the four `Q`
vertices has `Cl(3,0)` product `U` equal to the scalar `±1`, with
`N_picks≥1`. All four vertices are formed with nonempty `M`.
`N_hold(Q)=4≠6=N_picks(Q)`, so face fails.

Face: fail

exist-choice face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Exist-choice face is comparison only. This is not `UNDEFINED`. Face fails.
Unique-L leftover reports unique-L product `UNDEFINED` from mixed `e_1` and
mixed `e_1+e_2`. Exist-choice leftover reports HOLD from nmclsy
`N_hold(Q)=4` some-picks extra. That exist-choice HOLD does not pin a `Cl`
member: two picks on `Q` are not scalar `±1`. Face already fails at each
vertex's own formation tick from forall-choice over the own incoming sets.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own incoming set to be a singleton.
- It does not sum the own incoming set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique-L letters on `Q` and `R` as the object.
- It does not reprint exist-choice HOLD as a determined `Cl` member.
- It does not reprint #7175 `S^+` as the letter.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later `T_Q`.
- It does not enlarge the host beyond `B_3(0)`.
- It does not call the displayed `Cl(3,0)` map a cube-Pauli Lattice action.
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

This display uses Lattice to name `B_3(0)` and the 4-cycles `Q` and `R`. It
uses Qubit only as the algebra of the local possibility domain. The
displayed `Cl(3,0)` product is theorem-domain data, not a cube-Pauli Lattice
action. It uses Record only as a boundary: a present lock is content. It
does not rewrite Admissibility. The y-symmetric three-site process, the own
incoming sets, and the forall-choice reverse/face predicates are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsyopp #7132 seed `+e_1/−e_1/−e_1` |
| `M` at four `Q` vertices and four `R` vertices | Theorem 1 |
| `N_picks` and `N_hold` on `Q` and on `R` | Theorem 1; `6`/`4` and `3`/`2` |
| unique-L letters if defined | Theorem 1; mixed vertices `UNDEFINED`; unique-L product `UNDEFINED` |
| reverse and face forall-choice | Theorems 2–3; `fail` / `fail` |
| exist-choice reverse and face | comparison; `hold` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed stays a set |
| unique-L product as the theorem | not the theorem; comparison only |
| exist-choice as the theorem | not the theorem; comparison only |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique-L | not this display |
| leftover of exist-choice | not this display |
| leftover of #7175 `S^+` | not this display |
| leftover of nmclall #7167 | not this display; independent |
| six-neighbor star as the letter | not used |
| forall-choice as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: forall-choice `Cl(3,0)` products of own incoming sets on #7175 `Q` and `R`, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed forall-choice `Cl(3,0)` reverse/face report on these #7175 `Q` and `R` own incoming sets. |
| V3 | Own incoming sets, `N_picks`/`N_hold`, and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads own incoming sets and scores whether every pick has scalar `Cl(3,0)` product `±1`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L
as the theorem, does not reprint exist-choice as a determined `Cl` member,
does not reprint #7175 `S^+` as the letter, does not use a six-neighbor
star, does not depend on nmclall #7167, and does not use occupancy `n`. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED`, then one `Cl(3,0)` product | refused; leftover; unique-L product is `UNDEFINED` on mixed `Q` while forall-choice has `N_hold(Q)=4≠6` and face fails |
| exist-choice leftover | take some-picks `U=±1` as a determined `Cl` member | refused; leftover; nmclsy `N_hold(Q)=4` is some-picks extra; exist-choice reverse/face hold while forall-choice fails |
| #7175 `S^+` exist-opposite | reuse same-tick six-neighbor locks union `L(q)` | refused; leftover; that readout is a six-neighbor star, not a `Cl(3,0)` product of own incoming picks |
| nmclall #7167 forall-choice | reuse two-site opposite-lock seed `{0,(0,1,0)}` | refused; independent; that seed reports `M(e_1)={+e_2,+e_3,−e_3}` and `N_picks(Q)=9` |
| sum of the same incoming sets | replace `M` by the `Z^3` sum | refused; leftover; the construction does not sum |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score vertices by formation order | different object; ticks locate `M` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the vertices by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by forall-choice | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per vertex | uniqueness is not required; mixed stays a set |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of forall-choice
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, y-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own incoming set of
earliest nearest-neighbor steps, mixed stays a set, displayed `Cl(3,0)`
units, forall-choice over 4-cycle picks, 4-cycles `Q` and `R`, and
reverse/face as every pick having scalar `U=±1` are declared. No uniqueness
of incoming locks, no occupancy `n`, no named-sign reduction, no singleton
leftover as the object, no sum leftover, no unique-L leftover as the
theorem, no exist-choice leftover as the theorem, no #7175 `S^+` leftover,
no nmclall #7167 dependence, no six-neighbor star as the letter, no global
later `T_Q`, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own incoming set, each 4-cycle pick | no continuum alphabet |
| per site | `Q` and `R` vertices on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | eight incoming sets, `N_picks`/`N_hold`, and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Forall-choice is leftover of exist-choice because exist-choice
HOLD already pins a `Cl` member from `N_hold(Q)=4` picks with `U=±1`,
unique-L is `UNDEFINED` on mixed `Q`, nmclall #7167 already asked
forall-choice on the same `Q` and `R`, #7175 `S^+` already answered a
HOLDING letter, named signs should suffice because they keep orientation,
and occupancy `n` should track that vector.

**Answer:** The named construction reports own incoming sets at the eight
vertices, mixed stays a set, and counts `N_picks(Q)=6`, `N_hold(Q)=4`,
`N_picks(R)=3`, `N_hold(R)=2`. Unique-L product is `UNDEFINED` on mixed
`Q` and mixed `R`. Unique-L product is comparison only. It is not the
theorem. Exist-choice reverse holds and exist-choice face holds; those are
comparison only. They are not leftover of exist-choice as a determined
`Cl` member: two picks on `Q` and one pick on `R` are not scalar `±1`, so
forall-choice reverse fails and face fails. Occupancy `n` is not used.
Named signs lost the axis. nmclall #7167 uses a different seed and a
different `M(e_1)`. #7175 `S^+` is not the letter. The bits remain
displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique-L `Cl(3,0)` product on these same #7175 `Q` and `R` vertices would
assign `UNDEFINED` at mixed `e_1` and mixed `D` and leave both products
`UNDEFINED`. An exist-choice `Cl(3,0)` product on the same vertices would
HOLD from some-picks extra (`N_hold(Q)=4`, `N_hold(R)=2`) and would not
require every pick. A #7175 same-tick union own display reports a
six-neighbor star, not a 4-cycle `Cl(3,0)` product of own incoming picks.
nmclall #7167 uses two-site seed `{0,(0,1,0)}` and a larger `M(e_1)`. Unique
lock-vector lettering of the incoming sets would refuse the mixed vertices.
A sum leftover of the same lists would replace mixed `M(D)` by a cancelled
vector. This note is not those displays: mixed stays a set, the
construction does not sum, the letter is the own incoming set,
forall-choice asks whether every pick has `U=±1`, reverse fails, and face
fails.

**Gate disposition:** PASS for the own-incoming-set forall-choice `Cl(3,0)`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the unique-L product,” “the predicate equals exist-choice,”
“the predicate equals the sum of the lock set,” “bits are Admissibility,”
“the letter is occupancy `n`,” “the sets equal unique-L leftover,” “the
sets equal exist-choice leftover,” “the sets equal #7175 `S^+` leftover,”
“the report is leftover of nmclall #7167,” “reverse holds,” or “face is
`UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsyopp #7132 perp-step
incoming-lock process, reads own incoming sets at the four `Q` vertices and
the four `R` vertices, identifies `±e_i` with displayed `Cl(3,0)` units,
enumerates picks, counts `N_picks` and `N_hold`, reports unique-L letters
if defined, reports exist-choice as comparison, and checks Theorems 1--3.
It also checks that the construction is not named-sign lettering, that mixed
stays a set, that the construction does not sum, that occupancy `n` is not
used, that a formation member from already-recorded six-neighbor locks is
not attached, that unique-L product is comparison only, that exist-choice
is comparison only, that the report is not leftover of unique-L, that the
report is not leftover of exist-choice, that the letter is not leftover of
#7175 `S^+`, and that the report is independent of nmclall #7167. No runner
cache is written.
