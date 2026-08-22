---
claim_id: z_symmetric_three_site_sametick_union_own_clifford_exist_choice_plaquette_product_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from exist-choice Cl(3,0) 4-cycle products of S⁺ on #7188 Q and R are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_sametick_union_own_clifford_exist_choice_plaquette_product_reverse_face_2026_08_15.py
---

# Exist-Choice Cl(3,0) Plaquette Product Reverse And Face From Same-Tick Union Own S^+ On The Z-Symmetric Three-Site Process

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from exist-choice `Cl(3,0)` 4-cycle products of
`S^+` on the z-symmetric three-site process in `B_3(0)={n:n·n<=9}`. Same
process and x-probes as the HOLDING z-symmetric three-site same-tick
union-own display. Seed at tick 0: origin lock `+e_1`, `(0,0,1)` lock `−e_1`,
`(0,0,−1)` lock `−e_1`. Perp-step, incoming lock. Let `t(q)` be the formation
tick. Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}` at `t(q)`;
seeds use seed letters. Mixed earliest steps make `L(q)` `UNDEFINED`. At
`q`'s own `t`, `S^+(q)` is the set of locks of six-neighbors of `q` that
formed at tick `<= t(q)` and are not `q`, union `{L(q)}` when `L(q)` is
defined. Unformed sites make `S^+` `UNDEFINED`. No global T. Identify `±e_i`
with generators `γ_i` of `Cl(3,0)`: `γ_i²=+1` and `γ_i γ_j=−γ_j γ_i` for
`i≠j`; `−e_i` maps to `−γ_i`. This is a displayed algebra, not a cube-Pauli
Lattice action. Face plaquette `Q={0,(1,0,0),(1,1,0),(0,1,0)}` in cyclic
order `(0, e_1, e_1+e_2, e_2)`. Reverse 4-cycle containing `A=(1,0,0)` and
`B=(1,1,1)`: `R={(1,0,0),(1,1,0),(1,1,1),(1,0,1)}` cyclic. At a 4-cycle
`V=(v0,v1,v2,v3)`, a pick is one letter from each `S^+(vi)` at that site's
own `t` (no T_Q). `U` is the `Cl(3,0)` product of the four picked units.
Exist-choice HOLD iff some pick has `U` equal to the scalar ±1. If any
vertex is unformed or `S^+` is `UNDEFINED` or empty, the report is
`UNDEFINED`. Else fail. Unique-L product is comparison only (mixed vertex
⇒ `UNDEFINED`). It is not the theorem. This display does not use occupancy
`n`. Occupancy `n` is not used. This is not leftover of unique-L `Cl(3,0)`
products. This is not leftover of exist-opposite on the four x-probes.
This is not another `S^+` seed reprint. Uniqueness of incoming locks is not
required. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_sametick_union_own_clifford_exist_choice_plaquette_product_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_sametick_union_own_clifford_exist_choice_plaquette_product_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and two named 4-cycles. Incoming lock letters are unit nearest-neighbor
steps, collected into `S^+` at each vertex's own `t`, then mapped to
`Cl(3,0)` units. Reverse and face are scored on whether some pick from those
four sets has cyclic product equal to the scalar `±1`. Named signs `{+,−}`
are a coarser readout and are not used. A unique incoming letter at a mixed
vertex is a different readout and is not used. Existential opposite of two
probe `S^+` sets is a different readout and is not used. A `Z^3` sum of
those locks is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ at the four Q vertices and the four R vertices of the z-symmetric three-site process, each at that site's own t with no T_Q and no global T, of N_picks and N_hold, and of exist-choice reverse hold and face hold because some Cl(3,0) pick has U equal to the scalar ±1; unique-L products stay UNDEFINED from mixed vertices and are comparison only; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_sametick_union_own_clifford_exist_choice_plaquette_product_reverse_face
target_blocker_text: "display whether some pick from HOLDING S^+ on #7188 Q and R makes the Cl(3,0) 4-cycle product U=±1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the exist-choice Cl(3,0) product into Admissibility, do not reduce to unique-L, do not replace the 4-cycle product by exist-opposite of two probes, do not reprint S^+ seeds, do not wait for T_Q, do not use occupancy n, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for exist-choice Cl(3,0) 4-cycle products of S^+ on Q and R of the z-symmetric three-site process, each set at that site's own t, no T_Q, no global T; displayed, not adopted"
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
R = ((1,0,0), (1,1,0), (1,1,1), (1,0,1))
```

The four x-probes of the same process are `A=(1,0,0)`, `B=(1,1,1)`,
`C=(2,0,0)`, and `D=(1,1,0)`. `A` and `B` lie on `R`. `A` is also `e_1` on
`Q`. `A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,0,1), (0,0,-1)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,0,1)=−e_1`, and `L(0,0,-1)=−e_1`. The
third site is the z-mirror of the two-site opposite-lock partner `(0,0,1)`.
This seed is not the two-site opposite-lock seed `{0,(0,0,1)}`, not the
nnseed `{0,(0,1,0)}` with locks `+e_1/+e_2`, and not the opposite-lock
two-site seed `{0,(0,1,0)}` with locks `+e_1/−e_1`.

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

## Named exist-choice Cl(3,0) product of S^+

Let `t(q)` be the formation tick of site `q` when that tick is defined in
`B_3(0)`. There is no global T. Let `L(q)` be `q`'s own unique incoming lock
in `{±e_i}` at that own tick. Seeds use seed letters. If several earliest
incoming steps exist, `L(q)` is `UNDEFINED`.

At `q`'s own `t`, `S^+(q)` is the set of locks of six-neighbors of `q` that
formed at tick `<= t(q)` and are not `q`, union `{L(q)}` when `L(q)` is
defined. Same-tick partners are kept when they are neighbors. The site
itself is excluded from the neighbor set and re-enters only through `{L(q)}`
when that letter is defined. Duplicate locks collapse in the set. Unformed
sites make `S^+` `UNDEFINED`. The construction does not require `S^+` to be
a singleton. It does not sum `S^+`. It does not wait for a first common
tick `T_Q`. Occupancy `n` is not used. This display does not use occupancy.

Map each defined letter to a unit of the real Clifford algebra `Cl(3,0)`:

```text
+e_i  |->  γ_i
-e_i  |->  -γ_i
γ_i² = +1
γ_i γ_j = −γ_j γ_i   (i≠j)
```

This is a displayed algebra, not a cube-Pauli Lattice action. The map is not
an axiom edit and is not a Lattice rewrite.

At a 4-cycle `V=(v0,v1,v2,v3)`, a pick is one letter from each `S^+(vi)` at
that site's own `t`. `U` is the `Cl(3,0)` product of the four picked units,
in cyclic order. Exist-choice HOLD if and only if some pick has `U` equal to
the scalar `±1`. If any vertex is unformed, or any `S^+` is `UNDEFINED` or
empty, the report is `UNDEFINED`. Else, with every `S^+` nonempty and
defined and with no holding pick, the report fails.

Unique-L product of the four own incoming letters is comparison only. Mixed
vertices make that leftover `UNDEFINED`. Unique-L is not the theorem.

The construction does not score opposite vertices for opposite locks. It
does not score existence of an opposite pair in two probe `S^+` sets. It
does not reprint the four x-probe `S^+` sets as a seed display. Named-sign
lettering lost the axis. Reverse and face are scored on exist-choice of a
`Cl(3,0)` 4-cycle product.

Admissibility is not edited. The exist-choice `Cl(3,0)` product is not
written into Admissibility.

## Theorem 1 — S^+ on Q and on R, N_picks, N_hold, unique-L letters

Direct enumeration of the displayed z-symmetric three-site process on
`B_3(0)` records every vertex of `Q` and of `R`. Own unique incoming letters
and same-tick-inclusive union-own sets, each at that site's own `t`, are:

```text
Q:
  0         t(0)=0;         incoming +e_1;              L(0) = +e_1
            S^+(0) = {+e_1, −e_1}
  e_1       t(e_1)=3;       incoming +e_2, −e_2;        L(e_1) = UNDEFINED
            S^+(e_1) = {+e_1, +e_2, −e_2, +e_3, −e_3}
  e_1+e_2   t(e_1+e_2)=2;   incoming +e_1;              L(e_1+e_2) = +e_1
            S^+(e_1+e_2) = {+e_1, +e_2}
  e_2       t(e_2)=1;       incoming +e_2;              L(e_2) = +e_2
            S^+(e_2) = {+e_1, +e_2}

R:
  (1,0,0)   t(1,0,0)=3;     incoming +e_2, −e_2;        L(1,0,0) = UNDEFINED
            S^+((1,0,0)) = {+e_1, +e_2, −e_2, +e_3, −e_3}
  (1,1,0)   t(1,1,0)=2;     incoming +e_1;              L(1,1,0) = +e_1
            S^+((1,1,0)) = {+e_1, +e_2}
  (1,1,1)   t(1,1,1)=2;     incoming +e_1;              L(1,1,1) = +e_1
            S^+((1,1,1)) = {+e_1, +e_2}
  (1,0,1)   t(1,0,1)=3;     incoming +e_2, −e_2, −e_3;  L(1,0,1) = UNDEFINED
            S^+((1,0,1)) = {+e_1, −e_1, +e_2, −e_2}
```

`A=(1,0,0)` is not a seed. Mixed earliest steps at `e_1=A` are `+e_2` and
`−e_2`; mixed earliest steps at `(1,0,1)` are `+e_2`, `−e_2`, and `−e_3`.
Uniqueness is not required. Those mixed incoming steps leave `L(e_1)` and
`L(1,0,1)` `UNDEFINED`, so unique-L cyclic products are comparison-only
`UNDEFINED`:

```text
unique-L U_Q = UNDEFINED
unique-L U_R = UNDEFINED
```

`S^+` at those mixed vertices is nonempty. Cartesian picks and holding
counts are

```text
N_picks(Q) = 40
N_hold(Q) = 12
N_picks(R) = 80
N_hold(R) = 24
```

One holding face pick is `(+e_1, +e_2, +e_2, +e_1)`, with `U=+1`. One
holding reverse pick is `(+e_2, +e_2, +e_2, +e_2)`, with `U=+1`. Not every
pick holds: `N_hold` is strictly smaller than `N_picks` on both cycles.
Unique-L forbids the mixed letters that those holding picks use.

This is not leftover of unique-L products: unique-L stays `UNDEFINED` from
the mixed vertices, while exist-choice reads the nonempty `S^+` sets. This
is not leftover of exist-opposite on the four x-probes: that leftover
scores a pair of probe sets for a vector sum to the origin, not a four-unit
`Cl(3,0)` product on `Q` and `R`. This is not another `S^+` seed reprint:
nnseed, opposite-lock two-site, and two-site opposite-lock seeds produce
different `S^+` on `Q`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if some pick from the four `S^+` sets on `R` has
`Cl(3,0)` product equal to the scalar `±1`. All four vertices of `R` are
formed in `B_3(0)`. All four `S^+` sets are nonempty and defined.
`N_picks(R) = 80` and `N_hold(R) = 24`, so some pick holds. Reverse is
`hold`. Unique-L reverse is `UNDEFINED` from mixed `L(1,0,0)` and
`L(1,0,1)` and is not this report.

Reverse: hold

This is not leftover of unique-L. This is not leftover of exist-opposite.
This is not another `S^+` seed reprint. Reverse does not wait for
`T_R=min(t(A),t(B))`. Each `S^+` is read at that vertex's own `t`.

Reverse is `hold`.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if some pick from the four `S^+` sets on `Q` has
`Cl(3,0)` product equal to the scalar `±1`. All four vertices of `Q` are
formed in `B_3(0)`. All four `S^+` sets are nonempty and defined.
`N_picks(Q) = 40` and `N_hold(Q) = 12`, so some pick holds. Face is `hold`.
Unique-L face is `UNDEFINED` from mixed `L(e_1)` and is not this report.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not leftover of unique-L. Illegal unique-L representative picks at
mixed `e_1` are not the theorem: exist-choice enumerates `S^+`, including
neighbor locks that are not the site's own incoming letter. A unique-L
leftover of the same four letters is `UNDEFINED` as a product of mixed
letters, not as an exist-choice count. Exist-opposite leftover of `S^+` on
the four x-probes already holds reverse and face by a pair summing to the
origin; that is not a 4-cycle `Cl(3,0)` product. The first common tick of
`Q` happens to be `T_Q=3`, equal to `t(e_1)`; this display still does not
wait for `T_Q`.

Face is `hold`.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not replace exist-choice by the unique-L product.
- It does not score opposite vertices for opposite locks.
- It does not score exist-opposite of two probe `S^+` sets as the theorem.
- It does not reprint the four x-probe `S^+` sets as a seed display.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not wait for a common tick `T_Q` or for `T_R=min(t(A),t(B))`.
- It does not wait for a global T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
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
exist-choice product of `S^+` units is theorem-domain data, not an axiom
rewrite. It uses Record only as a boundary: a present lock is content. It does
not rewrite Admissibility. The z-symmetric three-site process and the
exist-choice `Cl(3,0)` 4-cycle products of `S^+` are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; z-symmetric three-site seed `+e_1/−e_1/−e_1` on `{0,(0,0,1),(0,0,-1)}` |
| `S^+` on `Q` | Theorem 1; `{+e_1,−e_1}`, `{+e_1,+e_2,−e_2,+e_3,−e_3}`, `{+e_1,+e_2}`, `{+e_1,+e_2}` |
| `S^+` on `R` | Theorem 1; `{+e_1,+e_2,−e_2,+e_3,−e_3}`, `{+e_1,+e_2}`, `{+e_1,+e_2}`, `{+e_1,−e_1,+e_2,−e_2}` |
| `N_picks` and `N_hold` | Theorem 1; `40/12` on `Q` and `80/24` on `R` |
| unique-L letters | comparison only; mixed `UNDEFINED` on `e_1` and on `(1,0,1)` |
| reverse and face | Theorems 2–3; `hold` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| unique-L `Cl(3,0)` product | comparison only; not the theorem |
| exist-opposite of two probe `S^+` sets | not the theorem |
| `S^+` seed reprint | not this display |
| common tick `T_Q` | not used; no `T_Q` |
| global T | not used; no global T |
| cube-Pauli Lattice action | not used; displayed algebra |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| exist-choice `Cl(3,0)` product as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: exist-choice `Cl(3,0)` 4-cycle products of `S^+` on `Q` and `R` of the z-symmetric three-site process, each set at that site's own `t`, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed exist-choice `Cl(3,0)` cyclic product reverse/face report from `S^+` on these two 4-cycles of this seed. |
| V3 | Own-tick `S^+` sets, pick counts, and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it maps `S^+` letters to `Cl(3,0)` units and scores exist-choice of the cyclic product against the scalar `±1`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not replace
exist-choice by unique-L, does not replace the 4-cycle product by
exist-opposite of two probes, does not reprint `S^+` seeds, does not wait
for `T_Q`, and does not use occupancy `n`. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L `Cl(3,0)` product | replace each `S^+` by the unique own incoming letter | refused; leftover; mixed `L(e_1)` and `L(1,0,1)` leave unique-L `UNDEFINED` while exist-choice holds |
| exist-opposite of two probe `S^+` sets | score `S^+(A)` against `S^+(B)` and `S^+(C)` against `S^+(D)` for a pair summing to the origin | refused; leftover; that pairwise opposite is not a four-unit `Cl(3,0)` product on `Q` and `R` |
| `S^+` seed reprint | reuse the four x-probe `S^+` sets as the theorem | refused; this display scores 4-cycle exist-choice products, not a seed reprint of those four sets |
| common-tick `T_Q` leftover | wait until all four of `Q` are recorded | refused; this display reads each `S^+` at that site's own `t` with no `T_Q` |
| `T_R=min(t(A),t(B))` leftover | require all of `R` recorded by tick 2 | refused; `A` and `(1,0,1)` form at tick 3; this display reads them at their own `t` |
| pick only the unique letter | drop neighbor locks from mixed `S^+` | refused; mixed remains a set; unique-L is comparison only |
| nnseed `S^+` reprint | reuse seed `{0,(0,1,0)}` with locks `+e_1/+e_2` | refused; different process; `S^+` on `Q` differs |
| opposite-lock two-site reprint | reuse seed `{0,(0,1,0)}` with locks `+e_1/−e_1` | refused; different process |
| unique incoming lock required | demand one incoming step per vertex | uniqueness is not required; both earliest incoming steps at `A` are kept in `S^+` |
| named-sign lettering of the same letters | map `±e_i` to `{+,−}` | refused; lost the axis |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n·n` comparisons | different object; not an occupancy-kernel inner product |
| cube-Pauli Lattice action | treat `γ_i` as a Lattice-supplied cube action | refused; displayed algebra, not a cube-Pauli Lattice action |
| attach a formation member from already-recorded six-neighbor locks | form the vertices by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by the exist-choice `Cl(3,0)` product | refused; displayed, not adopted |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of the exist-choice
`Cl(3,0)` product are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1` at `{0,(0,0,1),(0,0,-1)}`, perpendicular step rule, incoming-step
lock, `S^+` as same-tick-inclusive six-neighbor locks union own unique
incoming lock when defined, each at that site's own `t`, `Cl(3,0)` units
`γ_i` with `γ_i²=+1` and anticommutators, exist-choice cyclic products on
`Q` and `R`, hold iff some pick has `U` equal to the scalar `±1`, and
reverse/face as `hold` / `fail` / `UNDEFINED` are declared. No uniqueness
of incoming locks, no occupancy `n`, no named-sign reduction, no unique-L
theorem, no exist-opposite theorem, no `S^+` seed reprint, no `T_Q`, no
global T, no cube-Pauli Lattice action, no formation attachment from
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
| per element | each lock vector in `S^+` as a `Cl(3,0)` unit `±γ_i` | no continuum alphabet |
| per site | vertices of `Q` and `R` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `S^+` sets, pick counts, and exist-choice hold iff some `U=±1` | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among mixed incoming steps.
None is taken here.

### N7 — hostile steelman

**Steelman:** Mixed incoming steps should still leave the product
`UNDEFINED`, unique-L already answered `UNDEFINED`/`UNDEFINED` on these
cycles, exist-opposite in `S^+` already answered reverse/face HOLD on the
four x-probes of this seed, a common tick `T_Q` is the honest plaquette
time, `S^+` at the four probes is already the theorem, named signs should
suffice, occupancy `n` should track the lock, and `Cl(3,0)` here is just
the one-site algebra used as a Lattice action.

**Answer:** Unique-L products stay `UNDEFINED` from mixed `L(e_1)` and
`L(1,0,1)` and are comparison only. Exist-choice enumerates nonempty `S^+`
sets at those same vertices; `N_hold(Q)=12` of `40` picks and
`N_hold(R)=24` of `80` picks have `U=±1`, so reverse holds and face holds.
Exist-opposite of two probe sets is a pairwise vector-sum leftover, not a
four-unit product on `Q` and `R`. The four x-probe `S^+` sets are not this
4-cycle display. Occupancy `n` is not used. Named signs lost the axis.
The `Cl(3,0)` map is a displayed algebra, not a cube-Pauli Lattice action.
The bits remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

Unique-L `Cl(3,0)` 4-cycle products on this same seed scored own incoming
letters and reported reverse `UNDEFINED` and face `UNDEFINED` from mixed
vertices. Exist-opposite of `S^+` on the four x-probes of this same seed
scored a pair of sets for a vector sum to the origin, not a 4-cycle
product. This note is not those displays: `S^+` is read at each vertex of
`Q` and of `R` at that site's own `t` with no `T_Q` and no global T,
unique-L stays `UNDEFINED`, exist-choice reverse is `hold`, and exist-choice
face is `hold`.

**Gate disposition:** PASS for the exist-choice `Cl(3,0)` 4-cycle product
reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals unique-L,”
“the predicate equals exist-opposite of two probe sets,” “the predicate
equals an `S^+` seed reprint,” “bits are Admissibility,” “the letter is
occupancy `n`,” “the product waits for `T_Q`,” “reverse is `UNDEFINED`,”
or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the z-symmetric three-site
perp-step incoming-lock process, reads `S^+` at each vertex of `Q` and of
`R` at that site's own `t`, enumerates exist-choice `Cl(3,0)` products,
records `N_picks` and `N_hold`, and checks Theorems 1--3. It also checks
that unique-L products stay `UNDEFINED`, that the construction is not
named-sign lettering, that occupancy `n` is not used, that a formation
member from already-recorded six-neighbor locks is not attached, that the
products are not leftover of unique-L, that the products are not leftover
of exist-opposite on the four x-probes, and that the products are not
another `S^+` seed reprint. No runner cache is written.
