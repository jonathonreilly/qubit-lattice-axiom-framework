---
claim_id: x_axis_opposite_e2_own_letter_clifford_plaquette_product_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from Cl(3,0) own-letter products on the #7195 y-probe process are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/x_axis_opposite_e2_own_letter_clifford_plaquette_product_reverse_face_2026_08_15.py
---

# Own-Letter Cl(3,0) Plaquette Product Reverse And Face On The X-Axis Opposite ±e_2 Process

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from own-letter `Cl(3,0)` 4-cycle products on the
x-axis opposite ±e_2 y-probe process in `B_3(0)={n:n·n<=9}`. Same process as
the HOLDING x-axis opposite ±e_2 y-probe display. Seed at tick 0: origin lock
`+e_2`, `(1,0,0)` lock `−e_2`. Perp-step, incoming lock. Letter `L(q)` is
`q`'s own unique incoming lock in `{±e_i}` at `t(q)`; seeds use seed letters.
Mixed earliest steps make `L(q)` `UNDEFINED`. Identify `±e_i` with generators
`γ_i` of `Cl(3,0)`: `γ_i²=+1` and `γ_i γ_j=−γ_j γ_i` for `i≠j`; `−e_i` maps
to `−γ_i`. This is a displayed algebra, not a cube-Pauli Lattice action. Face
plaquette `Q={0,(1,0,0),(1,1,0),(0,1,0)}` in cyclic order
`(0, e_1, e_1+e_2, e_2)`. `U_Q = L(0) L(e_1) L(e_1+e_2) L(e_2)` in `Cl(3,0)`,
each letter at that site's own `t`, with no T_Q. Face HOLD iff `U_Q` is the
scalar ±1. Reverse 4-cycle containing `A=(0,1,0)` and `B=(1,1,1)`:
`R={(0,1,0),(1,1,0),(1,1,1),(0,1,1)}` cyclic. `U_R` is the product of the
four own letters at each vertex's own `t`. Reverse HOLD iff `U_R` is the
scalar `±1`. Any `UNDEFINED` letter, or a vertex unrecorded in `B_3(0)`,
makes the product `UNDEFINED`. This display does not use occupancy `n`. Occupancy `n` is not used. This is not leftover
of vector-sum plaquette holonomy. This is not leftover of opposite-vertex
holonomy. This is not leftover of exist-opposite in `S^+`. This is not a
6-NN star. Uniqueness of incoming locks is not required. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/x_axis_opposite_e2_own_letter_clifford_plaquette_product_reverse_face_2026_08_15.py`](../scripts/x_axis_opposite_e2_own_letter_clifford_plaquette_product_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and two named 4-cycles. Incoming lock letters are unit nearest-neighbor
steps, then mapped to `Cl(3,0)` units. Reverse and face are scored on whether
the cyclic product is the scalar `±1`. Named signs `{+,−}` are a coarser
readout and are not used. A `Z^3` sum of those locks is a different readout
and is not used. Existential opposite of 6-NN lock sets is a different
readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of four own incoming letters on face 4-cycle Q and reverse 4-cycle R of the x-axis opposite ±e_2 y-probe process, each at that site's own t with no T_Q, and of the Cl(3,0) products U_Q and U_R or UNDEFINED, with reverse UNDEFINED and face UNDEFINED because mixed earliest steps leave two letters UNDEFINED on each cycle; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: x_axis_opposite_e2_own_letter_clifford_plaquette_product_reverse_face
target_blocker_text: "display reverse and face from own-letter Cl(3,0) 4-cycle products on #7195 Q and R, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the Cl(3,0) product into Admissibility, do not reduce to named sign, do not replace the product by a vector-sum, do not replace the product by opposite-vertex holonomy, do not replace the product by exist-opposite in S^+, do not use a 6-NN star, do not use occupancy n, do not wait for T_Q, and do not pick a representative among mixed incoming steps."
conditional_surface_status: "exact on B_3(0) for own-letter Cl(3,0) 4-cycle products on Q and R of the x-axis opposite ±e_2 y-probe process, each letter at that site's own t, no T_Q; displayed, not adopted"
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

No larger host is used. The scored sites are the vertices of two 4-cycles:

```text
Q = (0, e_1, e_1+e_2, e_2)
R = ((0,1,0), (1,1,0), (1,1,1), (0,1,1))
```

`A=(0,1,0)` and `B=(1,1,1)` lie on `R`. `A` is not a seed. `A` equals `e_2`.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (1,0,0)}` is recorded at formation tick 0 with
locks `L(0)=+e_2` and `L(1,0,0)=−e_2`. This seed is not the x-axis same-lock
seed `{0,(1,0,0)}` with locks `+e_2/+e_2`. This seed is not the nssame
two-site seed `{0,(0,1,0)}` with locks `+e_1/+e_1`. This seed is not the
nnseed `{0,(1,0,0)}` with locks `+e_2/+e_1`, and not the opposite-lock
two-site seed `{0,(0,1,0)}` with locks `+e_1/−e_1`. This seed is not the
z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Uniqueness is not required. A later parent does not re-form
`q`.

## Named Cl(3,0) product of own incoming letters

Let `t(q)` be the formation tick of site `q` when that tick is defined in
`B_3(0)`. Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}` at that
own tick. Seeds use seed letters. If several earliest incoming steps exist,
`L(q)` is `UNDEFINED`. This display does not wait for a first common tick
`T_Q` at which every vertex of a cycle is recorded. Each letter is read at
that site's own `t`. Occupancy `n` is not used.

Map each defined letter to a unit of the real Clifford algebra `Cl(3,0)`:

```text
+e_i  |->  γ_i
-e_i  |->  -γ_i
γ_i² = +1
γ_i γ_j = −γ_j γ_i   (i≠j)
```

This is a displayed algebra, not a cube-Pauli Lattice action. The map is not
an axiom edit and is not a Lattice rewrite.

Face product and reverse product:

```text
U_Q = L(0) L(e_1) L(e_1+e_2) L(e_2)
U_R = L(0,1,0) L(1,1,0) L(1,1,1) L(0,1,1)
```

in `Cl(3,0)`, in the cyclic orders above. Face holds if and only if `U_Q` is
the scalar `±1`. Reverse holds if and only if `U_R` is the scalar `±1`. If
any factor is `UNDEFINED`, or if any vertex is unrecorded in `B_3(0)`, the
product is `UNDEFINED` and the corresponding report is `UNDEFINED`. Else the
report is `hold` or `fail`.

The construction does not sum the four lock vectors in `Z^3`. It does not
score opposite vertices for opposite locks. It does not score existence of
an opposite pair in a 6-NN lock set `S^+`. It is not a 6-NN star. It is not
leftover of vector-sum plaquette holonomy on nnseed or on the opposite-lock
two-site process. It is not leftover of opposite-vertex holonomy. It is not
leftover of exist-opposite in `S^+`. It is not leftover of a common-tick
`T_Q` or of `T_R=min(t(A),t(B))`. It is not leftover of x-axis same-lock
`+e_2/+e_2`.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on the
`Cl(3,0)` product. They are not scored on `{+,−}` names and are not an
occupancy-kernel inner product.

Admissibility is not edited. The `Cl(3,0)` product is not written into
Admissibility.

## Theorem 1 — four letters on Q and on R, and the Cl(3,0) products

Direct enumeration of the displayed x-axis opposite ±e_2 process on
`B_3(0)` records every vertex of `Q` and of `R`. The own-tick letters are:

```text
Q:
  0         t(0)=0;         incoming +e_2;                    L(0) = +e_2
  e_1       t(e_1)=0;       incoming −e_2;                    L(e_1) = −e_2
  e_1+e_2   t(e_1+e_2)=3;   incoming −e_1, +e_3, −e_3;        L(e_1+e_2) = UNDEFINED
  e_2       t(e_2)=3;       incoming +e_1, +e_3, −e_3;        L(e_2) = UNDEFINED

R:
  (0,1,0)   t(0,1,0)=3;     incoming +e_1, +e_3, −e_3;        L(0,1,0) = UNDEFINED
  (1,1,0)   t(1,1,0)=3;     incoming −e_1, +e_3, −e_3;        L(1,1,0) = UNDEFINED
  (1,1,1)   t(1,1,1)=2;     incoming +e_2;                    L(1,1,1) = +e_2
  (0,1,1)   t(0,1,1)=2;     incoming +e_2;                    L(0,1,1) = +e_2
```

`A=(0,1,0)` is not a seed. Mixed earliest steps at `e_2=A` are `+e_1`,
`+e_3`, and `−e_3`; mixed earliest steps at `(1,1,0)` are `−e_1`, `+e_3`,
and `−e_3`. Uniqueness is not required. Those mixed incoming steps leave
`L(e_2)` and `L(e_1+e_2)` `UNDEFINED`, so both cyclic products are
`UNDEFINED`:

```text
U_Q = UNDEFINED
U_R = UNDEFINED
```

The products are not the scalar `+1` and are not the scalar `−1`. They are
not computed by picking one representative among mixed incoming steps. If
one illegally replaced the two mixed face letters by `(−e_1,+e_1)` or by
`(+e_3,+e_3)`, the face product would be the scalar `+1` or `−1` and would
hold, while `(−e_1,+e_3)` would fail. Mixed face letters disagree, so the
honest product stays `UNDEFINED`. If one illegally replaced the two mixed
reverse letters by `(+e_1,−e_1,+e_2,+e_2)`, the reverse product would be
the scalar `−1` and would hold, while `(+e_1,+e_3,+e_2,+e_2)` would fail.
Mixed reverse letters disagree, so the honest product stays `UNDEFINED`.

A vector-sum leftover of the same four letters is also `UNDEFINED`, because
it still needs a unique letter at `A` and at `(1,1,0)`. An opposite-vertex
leftover of `Q` is `UNDEFINED` for the same mixed letters at `e_2` and at
`e_1+e_2`. The two defined seed letters `L(0)=+e_2` and `L(e_1)=−e_2` do
sum to the origin, but they are adjacent vertices of `Q`, not opposite
vertices. An opposite-vertex leftover that waits for `T_R=min(t(A),t(B))=2`
finds `A` and `(1,1,0)` still unrecorded at that common tick, so it is
`UNDEFINED` for a different reason. This display reads each vertex at its
own `t` and does not wait for `T_Q` or for that `T_R`. Exist-opposite in
`S^+` is a 6-NN star leftover and is not this product: that leftover holds
reverse and face on these y-probes, while both products here are
`UNDEFINED`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if `U_R` is the scalar `±1`. Two of the four
letters on `R` are `UNDEFINED` from mixed earliest incoming steps, so
`U_R` is `UNDEFINED`. Reverse is `UNDEFINED`.

Reverse: UNDEFINED

This is not `hold` and not `fail`. This is not leftover of vector-sum
holonomy, not leftover of opposite-vertex holonomy, and not leftover of
exist-opposite in `S^+`. Opposite-vertex leftover at `T_R=min(t(A),t(B))`
is also `UNDEFINED`, but because two vertices are still unrecorded at that
common tick. This display has those vertices recorded at their own later
ticks; the product is `UNDEFINED` because the own letters mix. Exist-opposite
in `S^+` on these same y-probes holds reverse; that is a different readout.

Reverse is `UNDEFINED`.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if `U_Q` is the scalar `±1`. Two of the four letters
on `Q` are `UNDEFINED` from mixed earliest incoming steps at `e_1+e_2` and
at `e_2`, so `U_Q` is `UNDEFINED`. Face is `UNDEFINED`.

Face: UNDEFINED

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `fail`. Illegal representative picks at mixed
`e_1+e_2` and mixed `e_2` disagree between hold and fail as a scalar `±1`
versus a bivector; the mixed letters forbid those picks. A vector-sum
leftover of the same letters is `UNDEFINED` as a sum, not as a `Cl(3,0)`
product. Opposite-vertex leftover of `Q` is `UNDEFINED` from the same mixed
letters. Exist-opposite in `S^+` is not this product: that leftover holds
face on these y-probes. The first common tick of `Q` happens to be `T_Q=3`,
equal to `t(e_2)` and `t(e_1+e_2)`; this display still does not wait for
`T_Q`. Seeds already carry letters at tick 0. Letters do not update after
formation, so a `T_Q` leftover would reprint the same mixed letters; the
algebra remains the own-tick product, not the common tick.

Face is `UNDEFINED`.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not replace the `Cl(3,0)` product by a `Z^3` sum.
- It does not score opposite vertices for opposite locks.
- It does not score exist-opposite in `S^+`.
- It is not a 6-NN star.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not wait for a common tick `T_Q` or for `T_R=min(t(A),t(B))`.
- It does not pick a representative among mixed incoming steps.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint vector-sum plaquette holonomy on nnseed.
- It does not reprint opposite-vertex holonomy on the opposite-lock two-site
  process.
- It does not reprint exist-opposite same-tick union-own leftover on this
  same seed.
- It does not reprint x-axis same-lock `+e_2/+e_2`.
- It does not reprint the z-symmetric three-site own-letter `Cl(3,0)`
  product.
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
rewrite Admissibility. The x-axis opposite ±e_2 process and the own-letter
`Cl(3,0)` 4-cycle products are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; x-axis opposite ±e_2 seed `+e_2/−e_2` on `{0,(1,0,0)}` |
| four own letters on `Q` | Theorem 1; `+e_2`, `−e_2`, `UNDEFINED`, `UNDEFINED` |
| four own letters on `R` | Theorem 1; `UNDEFINED`, `UNDEFINED`, `+e_2`, `+e_2` |
| `U_Q` and `U_R` in `Cl(3,0)` | Theorem 1; both `UNDEFINED` |
| reverse and face | Theorems 2–3; `UNDEFINED` / `UNDEFINED` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| `Z^3` sum of the four locks | not used; not leftover of vector-sum |
| opposite-vertex holonomy | not used; not leftover of opposite-vertex |
| exist-opposite in `S^+` | not used; not leftover of exist-opposite |
| 6-NN star | not used; not a 6-NN star |
| common tick `T_Q` | not used; no `T_Q` |
| cube-Pauli Lattice action | not used; displayed algebra |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| `Cl(3,0)` product as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: own-letter `Cl(3,0)` 4-cycle products on `Q` and `R` of the x-axis opposite ±e_2 y-probe process, each letter at that site's own `t`, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed own-letter `Cl(3,0)` cyclic product reverse/face report on these two 4-cycles of this seed. |
| V3 | Own-tick letters and the `UNDEFINED`/`UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it maps own incoming locks to `Cl(3,0)` units and scores the cyclic product against the scalar `±1`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not replace the
product by a vector-sum, does not replace the product by opposite-vertex
holonomy, does not replace the product by exist-opposite in `S^+`, does not
use a 6-NN star, does not wait for `T_Q`, does not pick a mixed
representative, and does not use occupancy `n`. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| vector-sum of the four own letters | replace `U` by `L(0)+L(e_1)+L(e_1+e_2)+L(e_2)` in `Z^3` | refused; leftover; that sum is `UNDEFINED` from mixed `L(e_1+e_2)` and `L(e_2)` and is not a `Cl(3,0)` product |
| opposite-vertex holonomy | require `L(0)+L(e_1+e_2)=(0,0,0)` and `L(e_1)+L(e_2)=(0,0,0)` | refused; leftover; mixed letters leave that leftover `UNDEFINED`; adjacent seed letters `+e_2+(−e_2)=0` are not opposite vertices |
| exist-opposite in `S^+` | score 6-NN lock sets for a pair that sums to the origin | refused; leftover; not a 6-NN star; that leftover holds reverse and face on these y-probes while both products are `UNDEFINED` |
| common-tick `T_Q` leftover | wait until all four of `Q` are recorded | refused; this display reads each letter at that site's own `t` with no `T_Q` |
| `T_R=min(t(A),t(B))` leftover | require all of `R` recorded by tick 2 | refused; `A` and `(1,1,0)` form at tick 3; this display reads them at their own `t` |
| pick a mixed representative | replace mixed `L(e_1+e_2)` and `L(e_2)` by one pair of steps | refused; `(−e_1,+e_1)` and `(+e_3,+e_3)` would hold face as scalar `±1` while `(−e_1,+e_3)` would fail; mixed earliest steps make the letters `UNDEFINED` |
| nnseed plaquette holonomy reprint | reuse seed `{0,(1,0,0)}` with locks `+e_2/+e_1` | refused; different process; letter lists differ |
| opposite-lock two-site plaquette reprint | reuse seed `{0,(0,1,0)}` with locks `+e_1/−e_1` | refused; different process |
| x-axis same-lock reprint | reuse seed `{0,(1,0,0)}` with locks `+e_2/+e_2` | refused; `L(e_1)` is `+e_2` on that seed and `−e_2` here |
| nssame y-probe reprint | reuse seed `{0,(0,1,0)}` with locks `+e_1/+e_1` | refused; `A` is a seed on that process |
| z-symmetric three-site `Cl(3,0)` reprint | reuse seed `{0,(0,0,1),(0,0,-1)}` | refused; different process; `Q` letters differ |
| unique incoming lock required | demand one incoming step per vertex | uniqueness is not required; all three earliest incoming steps at `A` and at `(1,1,0)` are kept and those letters are `UNDEFINED` |
| named-sign lettering of the same letters | map `±e_i` to `{+,−}` | refused; lost the axis |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n·n` comparisons | different object; not an occupancy-kernel inner product |
| cube-Pauli Lattice action | treat `γ_i` as a Lattice-supplied cube action | refused; displayed algebra, not a cube-Pauli Lattice action |
| attach a formation member from already-recorded six-neighbor locks | form the vertices by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by the `Cl(3,0)` product | refused; displayed, not adopted |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of the `Cl(3,0)`
product are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, x-axis opposite ±e_2 seed locks `+e_2` and `−e_2` at
`{0,(1,0,0)}`, perpendicular step rule, incoming-step lock, own unique
incoming letter or `UNDEFINED` at each site's own `t`, `Cl(3,0)` units
`γ_i` with `γ_i²=+1` and anticommutators, cyclic products on `Q` and `R`,
hold iff the product is the scalar `±1`, and reverse/face as `hold` /
`fail` / `UNDEFINED` are declared. No uniqueness of incoming locks, no
occupancy `n`, no named-sign reduction, no vector-sum leftover, no
opposite-vertex leftover, no exist-opposite leftover, no 6-NN star, no
`T_Q`, no mixed representative, no cube-Pauli Lattice action, no formation
attachment from already-recorded six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED`/`UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each own incoming lock as a `Cl(3,0)` unit `±γ_i` | no continuum alphabet |
| per site | vertices of `Q` and `R` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four letters and one product per cycle | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among mixed incoming steps.
None is taken here.

### N7 — hostile steelman

**Steelman:** Mixed incoming steps should still yield a product after picking
one parent, some of those picks already give scalar `±1` on `Q` and would
answer face HOLD, vector-sum leftover already answered `UNDEFINED` from the
same mixed letters, opposite-vertex leftover already answered `UNDEFINED`,
exist-opposite in `S^+` already answered reverse/face hold on this seed, a
common tick `T_Q` is the honest plaquette time, `T_R=min(t(A),t(B))` is the
honest reverse time, nnseed and opposite-lock two-site and x-axis same-lock
plaquettes already displayed 4-cycle holonomy, named signs should suffice,
occupancy `n` should track the lock, and `Cl(3,0)` here is just the one-site
algebra used as a Lattice action.

**Answer:** The named construction reports own-tick letters `+e_2`, `−e_2`,
`UNDEFINED`, `UNDEFINED` on `Q` and `UNDEFINED`, `UNDEFINED`, `+e_2`,
`+e_2` on `R`. Mixed remains `UNDEFINED`. The construction does not pick a
representative. Occupancy `n` is not used. Named signs lost the axis. Both
products are `UNDEFINED`, so reverse is `UNDEFINED` and face is
`UNDEFINED`. Illegal picks at mixed face letters disagree between hold and
fail. Vector-sum leftover is a `Z^3` sum, not a `Cl(3,0)` product.
Opposite-vertex leftover scores pairs of opposite vertices, and at
`T_R=min(t(A),t(B))` it is `UNDEFINED` because two vertices are unrecorded,
not because own letters mix after they form. Exist-opposite in `S^+` is a
6-NN star leftover that holds reverse and face here; this product does not.
Nnseed, opposite-lock two-site, x-axis same-lock, and z-symmetric
three-site processes are different seeds. The `Cl(3,0)` map is a displayed
algebra, not a cube-Pauli Lattice action. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

Vector-sum / opposite-vertex holonomy on nnseed and on the opposite-lock
two-site process scored 4-cycles by `Z^3` sums and by opposite locks, not
by a `Cl(3,0)` product, and used a common tick `T_Q` or
`T_R=min(t(A),t(B))`. Exist-opposite in `S^+` on this same x-axis opposite
±e_2 seed scored 6-NN lock sets, not own-letter products, and held reverse
and face. Picking a mixed representative on `Q` disagrees between hold and
fail. X-axis same-lock `+e_2/+e_2` reprints a different `L(e_1)`. This note
is not those displays: each letter is read at that site's own `t` with no
`T_Q`, mixed letters stay `UNDEFINED`, `U_Q` and `U_R` are `UNDEFINED`,
reverse is `UNDEFINED`, and face is `UNDEFINED`.

**Gate disposition:** PASS for the own-letter `Cl(3,0)` 4-cycle product
reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the
vector-sum,” “the predicate equals opposite-vertex holonomy,” “the
predicate equals exist-opposite in `S^+`,” “bits are Admissibility,” “the
letter is occupancy `n`,” “the product equals a mixed representative,”
“the cycles equal nnseed leftover,” “the cycles equal opposite-lock
two-site leftover,” “the cycles equal x-axis same-lock leftover,” “the
letter waits for `T_Q`,” “reverse holds,” or “face holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the x-axis opposite ±e_2
perp-step incoming-lock process, reads each vertex's own unique incoming
lock or `UNDEFINED` at that site's own `t`, maps defined letters to `Cl(3,0)`
units, forms the cyclic products `U_Q` and `U_R`, and checks Theorems 1--3.
It also checks that the construction is not named-sign lettering, that mixed
letters stay `UNDEFINED`, that the construction does not sum, that occupancy
`n` is not used, that a formation member from already-recorded six-neighbor
locks is not attached, that the products are not leftover of vector-sum
holonomy, that the products are not leftover of opposite-vertex holonomy,
that the products are not leftover of exist-opposite in `S^+`, that the
products are not leftover of nnseed, opposite-lock two-site, x-axis
same-lock, or z-symmetric three-site plaquettes, and that picking a mixed
representative would change the face report. No runner cache is written.
