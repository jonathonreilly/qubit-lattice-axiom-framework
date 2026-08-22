---
claim_id: opposite_lock_yprobe_own_incoming_set_clifford_exist_choice_plaquette_product_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from exist-choice Cl(3,0) 4-cycle products of own incoming sets on #7167 Q and R are reported. No S⁺. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_own_incoming_set_clifford_exist_choice_plaquette_product_reverse_face_2026_08_15.py
---

# Own Incoming Set Exist-Choice Cl(3,0) Plaquette Product Reverse And Face On #7167 Q And R

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from exist-choice `Cl(3,0)` 4-cycle products of
own incoming sets `M(q)` on nsuoyinc #7167 / nsmopp #7208 face plaquette `Q`
and reverse 4-cycle `R` in `B_3(0)={n:n·n<=9}`. Same process as nsopp
#7093. Same y-probes as nsuoyinc #7167 / nsmopp #7208. Let `t(q)` be the
formation tick of site `q`. `M(q)` is the set of earliest incoming
nearest-neighbor steps at `q`. Seeds use their seed letter as a singleton.
Mixed stays a set. Unformed is `UNDEFINED`. Identify `±e_i` with generators
`γ_i` of `Cl(3,0)`: `γ_i²=+1` and `γ_i γ_j=−γ_j γ_i` for `i≠j`; `−e_i`
maps to `−γ_i`. This is a displayed algebra, not a cube-Pauli Lattice
action. At a 4-cycle `V=(v0,v1,v2,v3)`, a pick is one letter from each
`M(vi)` at that site's own `t`, with no T_Q. `U` is the `Cl(3,0)` product
of the four picked units. Exist-choice HOLD iff some pick has `U` equal to
the scalar ±1. If any vertex is unformed or `M` is `UNDEFINED` or empty,
the report is `UNDEFINED`. Else fail. Unique-L product is comparison only:
a mixed vertex makes that leftover `UNDEFINED`. Unique-L is not the
theorem. This retires “Cl has no member because unique-L is UNDEF” on mixed
`Q` vertices by displaying whether some pick from HOLDING `M`-sets of
#7208 makes `U=±1`. Occupancy `n` is not used. This is not named-sign
lettering. This is not a unique lock-vector leftover and not a sum leftover.
This is not leftover of unique-L. This is not leftover of exist-opposite of
nsmopp #7208. This is not leftover of #7208. This is not leftover of #7167
`S^+`. The own incoming set
does not use a six-neighbor star. Uniqueness of incoming locks is not
required. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1. This note does not write exist-choice `Cl(3,0)` products into
Admissibility and does not attach a formation member from already-recorded
six-neighbor locks. This display does not use occupancy. Mixed stays a set.
No S⁺.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_own_incoming_set_clifford_exist_choice_plaquette_product_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_own_incoming_set_clifford_exist_choice_plaquette_product_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and two named 4-cycles. Incoming lock letters are unit nearest-neighbor
steps, then mapped to `Cl(3,0)` units. Reverse and face are scored on
existence of a pick whose cyclic product is the scalar `±1`. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique
lock-vector letter is a different readout and is not used as the object:
report `M` and count picks. A `Z^3` sum of those locks is a different
readout and is not used. The construction does not sum. Existential
opposite of y-probe incoming sets is a different readout and is not used.
No S⁺.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of M(q) as the site's own incoming set of earliest NN steps on #7167 Q and R, mixed stays a set, with N_picks and N_hold and reverse hold plus face hold from exist-choice Cl(3,0) products; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_own_incoming_set_clifford_exist_choice_plaquette_product_reverse_face
target_blocker_text: "display reverse and face from exist-choice Cl(3,0) 4-cycle products of own incoming sets on #7167 Q and R, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write exist-choice Cl(3,0) products into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the products with unique-L leftover, do not identify the products with exist-opposite leftover of #7208, and do not identify the sets with #7167 S^+ leftover."
conditional_surface_status: "exact on B_3(0) for exist-choice Cl(3,0) 4-cycle products of own incoming sets on #7167 Q and R; displayed, not adopted"
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

No larger host is used. The four y-probes of nsuoyinc #7167 / nsmopp #7208
are

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. The scored sites are the vertices of two
4-cycles:

```text
Q = (0, e_1, e_1+e_2, e_2)
R = ((0,1,0), (1,1,0), (1,1,1), (0,1,1))
```

`A` and `B` lie on `R`. `A` and `D` lie on `Q` and on `R`. `C` lies on
neither cycle.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`. This seed is not the z-symmetric three-site seed
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

## Named exist-choice Cl(3,0) product of own incoming sets

Let `t(q)` be the formation tick of site `q` when that tick is defined in
`B_3(0)`. Let `M(q)` be the set of earliest incoming nearest-neighbor steps
at `q`. Seeds use their seed letter as a singleton. Mixed stays a set.
Unformed is `UNDEFINED`. Unique `L(q)` is comparison only and is not the
object. This display does not use a six-neighbor star. Occupancy `n` is not
used. Duplicate incoming steps collapse in the set. The construction does
not require `M(q)` to be a singleton. It does not sum `M(q)`. It is not a
unique lock-vector leftover and not a sum leftover. It is not leftover of
unique-L. It is not leftover of exist-opposite of nsmopp #7208. It is not
leftover of #7167 same-tick union own `S^+`. This display does not wait for
a first common tick `T_Q`. Each pick is read at that site's own `t`, with
no T_Q.

Map each defined letter to a unit of the real Clifford algebra `Cl(3,0)`:

```text
+e_i  |->  γ_i
-e_i  |->  -γ_i
γ_i² = +1
γ_i γ_j = −γ_j γ_i   (i≠j)
```

This is a displayed algebra, not a cube-Pauli Lattice action. The map is not
an axiom edit and is not a Lattice rewrite.

At a 4-cycle `V=(v0,v1,v2,v3)`, a pick is one letter from each `M(vi)`.
`U` is the `Cl(3,0)` product of the four picked units, in cyclic order.
`N_picks` is the product of the four set sizes. `N_hold` is the number of
picks with `U` equal to the scalar `±1`. Exist-choice reverse and face:

```text
reverse  <=>  some pick on R has U = ±1
face     <=>  some pick on Q has U = ±1
```

If any vertex is unformed, or if any `M` is empty or `UNDEFINED`, the
report is `UNDEFINED`. Else the report fails if no pick has `U` equal to
the scalar `±1`. The report is one of `hold`, `fail`, or `UNDEFINED`.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pick whose `Cl(3,0)` product is the scalar `±1`. They are not scored
on `{+,−}` names and are not an occupancy-kernel inner product.

Admissibility is not edited. Exist-choice `Cl(3,0)` products are not written
into Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — own incoming sets, N_picks, N_hold, and unique-L letters

Direct enumeration of the displayed nsopp #7093 process on `B_3(0)` records
every vertex of `Q` and of `R`. The formation ticks locate the earliest
incoming sets. They are not occupancy kernels and are not a global later T.

Own incoming sets at each vertex's own formation tick are:

```text
Q:
  0         t(0)=0;         incoming +e_1;
            M(0) = {+e_1}
  e_1       t(e_1)=3;       incoming +e_2, +e_3, −e_3;
            M(e_1) = {+e_2, +e_3, −e_3}
  e_1+e_2   t(e_1+e_2)=3;   incoming −e_2, −e_3, +e_3;
            M(e_1+e_2) = {−e_2, +e_3, −e_3}
  e_2       t(e_2)=0;       incoming −e_1;
            M(e_2) = {−e_1}

R:
  (0,1,0)   t(0,1,0)=0;     incoming −e_1;
            M(0,1,0) = {−e_1}
  (1,1,0)   t(1,1,0)=3;     incoming −e_2, −e_3, +e_3;
            M(1,1,0) = {−e_2, +e_3, −e_3}
  (1,1,1)   t(1,1,1)=2;     incoming +e_1;
            M(1,1,1) = {+e_1}
  (0,1,1)   t(0,1,1)=1;     incoming +e_3;
            M(0,1,1) = {+e_3}
```

`A=(0,1,0)` is a seed at tick 0 and equals `e_2`. Mixed stays a set:
`e_1` has three earliest incoming steps, and `e_1+e_2=D` has three earliest
incoming steps `−e_2`, `−e_3`, and `+e_3`. Those mixed vertices keep
nonempty `M`. Uniqueness is not required.

Pick counts and hold counts:

```text
N_picks(Q)=9
N_hold(Q)=5
N_picks(R)=3
N_hold(R)=2
```

Unique-L leftover letters, comparison only, are:

```text
Q:
  L(0) = +e_1
  L(e_1) = UNDEFINED
  L(e_1+e_2) = UNDEFINED
  L(e_2) = −e_1

R:
  L(0,1,0) = −e_1
  L(1,1,0) = UNDEFINED
  L(1,1,1) = +e_1
  L(0,1,1) = +e_3
```

Unique-L leftover products are both `UNDEFINED`, because mixed vertices
leave `L(e_1)`, `L(e_1+e_2)`, and `L(1,1,0)` undefined. That leftover is
the claim that `Cl` has no member because unique-L is `UNDEF`. It is not
this theorem. Exist-choice still has nine face picks and three reverse
picks from the HOLDING `M`-sets of #7208.

Incoming locks exist and need not be unique. That non-uniqueness does not
empty `M`. Uniqueness is not required. No S⁺.

## Theorem 2 — reverse exist-choice hold / fail / UNDEFINED

Reverse holds if and only if some pick from `M` at the four vertices of
`R` has `Cl(3,0)` product `U` equal to the scalar `±1`. All four vertices
are formed and all four incoming sets are nonempty. `N_picks(R)=3` and
`N_hold(R)=2`. One holding pick is `(−e_1, +e_3, +e_1, +e_3)` with
`U=+1`. Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Reverse holds. Unique-L leftover
reports reverse `UNDEFINED` from mixed `L(1,1,0)`. nsmopp #7208
exist-opposite leftover reports reverse hold from singleton `M(A)` against
`M(B)` on y-probes, which is a pair-sum predicate, not a 4-cycle product.
#7167 `S^+` leftover reports reverse hold from a two-element star at `A`.
This display multiplies four picked units on `R`. Reverse holds because
some pick on `R` has `U=±1`.

Reverse holds.

## Theorem 3 — face exist-choice hold / fail / UNDEFINED

Face holds if and only if some pick from `M` at the four vertices of `Q`
has `Cl(3,0)` product `U` equal to the scalar `±1`. All four vertices are
formed and all four incoming sets are nonempty. `N_picks(Q)=9` and
`N_hold(Q)=5`. One holding pick is `(+e_1, +e_2, −e_2, −e_1)` with
`U=+1`. Another is `(+e_1, +e_3, +e_3, −e_1)` with `U=−1`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Face holds. Unique-L leftover
reports face `UNDEFINED` from mixed `L(e_1)` and mixed `L(e_1+e_2)`. That
is the leftover this display retires: unique-L has no `Cl` member, while
five of nine exist-choice picks are the scalar `±1`. nsmopp #7208
exist-opposite leftover reports face hold from `M(C)` against mixed
`M(D)` on y-probes; `C` is not a vertex of `Q`. #7167 `S^+` leftover is a
six-neighbor star, not a 4-cycle product. Named-sign lettering lost the
axis in mixed `{+,−}` at `D`. Face already holds at each vertex's own
formation tick from exist-choice on the own incoming sets.

Face holds.

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
- It does not reprint unique-L letters on these cycles as the object.
- It does not reprint #7167 `S^+` as the letter.
- It does not reprint exist-opposite of nsmopp #7208 as the predicate.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T or for a common tick `T_Q`.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.
- It does not treat the `Cl(3,0)` map as a cube-Pauli Lattice action.

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

This display uses Lattice to name `B_3(0)` and the two 4-cycles. It uses Qubit
only as the algebra of the local possibility domain. The displayed `Cl(3,0)`
product of incoming-step units is theorem-domain data, not an axiom rewrite.
It uses Record only as a boundary: a present lock is content. It does not
rewrite Admissibility. The opposite-lock two-site process, the own incoming
sets, and the exist-choice `Cl(3,0)` reverse/face predicates are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| own incoming sets on `Q` | Theorem 1; `{+e_1}`, `{+e_2, +e_3, −e_3}`, `{−e_2, +e_3, −e_3}`, `{−e_1}` |
| own incoming sets on `R` | Theorem 1; `{−e_1}`, `{−e_2, +e_3, −e_3}`, `{+e_1}`, `{+e_3}` |
| `N_picks` and `N_hold` on `Q` and on `R` | Theorem 1; `9/5` and `3/2` |
| unique-L letters if defined | Theorem 1; mixed `e_1`, `e_1+e_2`, and `(1,1,0)` are `UNDEFINED` |
| reverse and face | Theorems 2–3; `hold` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed stays a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique-L | not this display |
| leftover of exist-opposite of #7208 | not this display |
| leftover of #7167 `S^+` exist-opposite | not this display |
| six-neighbor star as the letter | not used |
| common tick `T_Q` | not used; no `T_Q` |
| cube-Pauli Lattice action | not used; displayed algebra |
| exist-choice `Cl(3,0)` product as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: exist-choice `Cl(3,0)` 4-cycle products of own incoming sets on #7167 `Q` and `R`, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed exist-choice `Cl(3,0)` cyclic product reverse/face report on these two 4-cycles from HOLDING `M`-sets of #7208. |
| V3 | Own incoming sets, pick counts, and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads each vertex's own incoming set, maps picks to `Cl(3,0)` units, and scores existence of a scalar `±1` product. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L,
does not reprint exist-opposite of #7208, does not reprint #7167 `S^+` as
the letter, does not use a six-neighbor star, does not wait for `T_Q`, and
does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED`, then multiply | refused; leftover; unique-L products are `UNDEFINED` on mixed `Q` and `R` while exist-choice HOLDs from `N_hold(Q)=5` and `N_hold(R)=2` |
| exist-opposite of nsmopp #7208 | score some `a` in `M(A)` and `b` in `M(B)` with `a+b=0`, and likewise on `C,D` | refused; leftover of exist-opposite; that predicate HOLDs reverse and face on y-probes, and `C` is not a vertex of `Q` or `R` |
| #7167 `S^+` exist-opposite | reuse same-tick six-neighbor locks union `L(q)` | refused; leftover of #7167; that readout HOLDs reverse and face from a two-element star at `A` |
| vector-sum of unique letters | replace `U` by a `Z^3` sum of four unique letters | refused; leftover; that sum is `UNDEFINED` from mixed unique-L and is not a `Cl(3,0)` product |
| opposite-vertex holonomy | require opposite vertices to carry opposite unique letters | refused; leftover; mixed unique-L leaves that leftover `UNDEFINED` |
| common-tick `T_Q` leftover | wait until all four of `Q` are recorded | refused; this display reads each pick at that site's own `t` with no `T_Q` |
| unique incoming lock required | demand one incoming step per vertex | uniqueness is not required; mixed stays a set and exist-choice still HOLDs |
| named-sign lettering of the same letters | map `±e_i` to `{+,−}` | refused; lost the axis |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n·n` comparisons | different object; not an occupancy-kernel inner product |
| cube-Pauli Lattice action | treat `γ_i` as a Lattice-supplied cube action | refused; displayed algebra, not a cube-Pauli Lattice action |
| attach a formation member from already-recorded six-neighbor locks | form the vertices by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by exist-choice `Cl(3,0)` products | refused; displayed, not adopted |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of exist-choice
`Cl(3,0)` products are distinct open premises. This note claims no complete
wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, own incoming set of earliest nearest-neighbor
steps, mixed stays a set, `Cl(3,0)` units `γ_i` with `γ_i²=+1` and
anticommutators, exist-choice over picks on `Q` and `R`, hold iff some
product is the scalar `±1`, and reverse/face as `hold` / `fail` /
`UNDEFINED` are declared. No uniqueness of incoming locks, no occupancy
`n`, no named-sign reduction, no singleton leftover as the object, no sum
leftover, no unique-L leftover, no exist-opposite leftover of #7208, no
#7167 `S^+` leftover, no six-neighbor star as the letter, no global later
T, no `T_Q`, no cube-Pauli Lattice action, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each picked lock vector as a `Cl(3,0)` unit `±γ_i` | no continuum alphabet |
| per site | vertices of `Q` and `R` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets, `N_picks`, `N_hold`, and exist-choice hold iff some `U=±1` | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among mixed incoming steps.
None is taken here.

### N7 — hostile steelman

**Steelman:** Unique-L already answered that `Cl` has no member because
mixed `Q` vertices make unique-L `UNDEF`, so exist-choice is an illegal
pick among mixed parents; nsmopp #7208 already answered exist-opposite
HOLD from these same `M`-sets; #7167 `S^+` already answered HOLD; the
sets should be replaced by their sums; named signs should suffice; occupancy
`n` should track that vector; and `Cl(3,0)` here is just the one-site
algebra used as a Lattice action.

**Answer:** The named construction reports incoming sets `{+e_1}`,
`{+e_2, +e_3, −e_3}`, `{−e_2, +e_3, −e_3}`, `{−e_1}` on `Q` and `{−e_1}`,
`{−e_2, +e_3, −e_3}`, `{+e_1}`, `{+e_3}` on `R` from each vertex's own
earliest incoming steps. Mixed stays a set. The construction does not sum.
Occupancy `n` is not used. Named signs lost the axis. Unique-L leftover
has no product because mixed vertices leave unique letters `UNDEFINED`.
Exist-choice still has `N_picks(Q)=9` with `N_hold(Q)=5` and
`N_picks(R)=3` with `N_hold(R)=2`, so reverse holds and face holds. nsmopp
#7208 exist-opposite leftover HOLDs a pair-sum on y-probes `A,B,C,D`, not
a 4-cycle product; `C` is not on `Q` or `R`. #7167 `S^+` leftover uses a
six-neighbor star. The `Cl(3,0)` map is a displayed algebra, not a
cube-Pauli Lattice action. The sets are not those leftovers. The bits
remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique-L `Cl(3,0)` product on these same #7167 cycles would assign
`L(e_1)=UNDEFINED` and `L(e_1+e_2)=UNDEFINED` and report reverse
`UNDEFINED` with face `UNDEFINED`. A #7167 same-tick union own display
reports `S^+(A) = {+e_1, −e_1}` with reverse hold and face hold from
exist-opposite of stars. nsmopp #7208 reports reverse hold and face hold
from exist-opposite of own incoming sets on y-probes `A,B,C,D`. Unique
lock-vector lettering of the incoming sets would report face `UNDEFINED`
because `D` mixes. A sum leftover of the same lists would replace mixed
`M(D)` by `−e_2` after cancelling `+e_3` and `−e_3`. This note is not
those displays: mixed stays a set, the construction does not sum, the
letter is the own incoming set, exist-choice `Cl(3,0)` products HOLD on
`Q` and on `R`, reverse holds, and face holds.

**Gate disposition:** PASS for the exist-choice `Cl(3,0)` 4-cycle product
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals the sum of the lock set,” “bits are Admissibility,”
“the letter is occupancy `n`,” “the products equal unique-L leftover,”
“the products equal exist-opposite leftover of #7208,” “the sets equal
#7167 `S^+` leftover,” “reverse fails,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each vertex's own incoming set of earliest
nearest-neighbor steps on `Q` and on `R`, maps picks to `Cl(3,0)` units,
counts `N_picks` and `N_hold`, scores reverse and face by exist-choice
hold iff some product is the scalar `±1`, and checks Theorems 1--3. It
also checks that the construction is not named-sign lettering, that mixed
stays a set, that the construction does not sum, that occupancy `n` is
not used, that a formation member from already-recorded six-neighbor locks
is not attached, that the products are not leftover of unique-L, that the
products are not leftover of exist-opposite of #7208, and that the sets
are not leftover of #7167 `S^+`. No runner cache is written.
