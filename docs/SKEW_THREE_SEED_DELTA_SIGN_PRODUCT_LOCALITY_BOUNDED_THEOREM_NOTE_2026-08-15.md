---
claim_id: skew_three_seed_delta_sign_product_locality_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On stars at unread v=(-1,1,1), whether the claim-delta sign-product 6-tuple is a function of the 6-NN occupancy alone is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_delta_sign_product_locality_2026_08_15.py
---

# Skew Three-Seed Claim-Delta Sign-Product Is Not NN-Determined

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** stars at the single unread site `v=(-1,1,1)` for finite unions of
radius-2 taxicab balls. The 6-NN occupancy and the claim-delta sign-product
6-tuple are compared on that star only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_delta_sign_product_locality_2026_08_15.py`](../scripts/skew_three_seed_delta_sign_product_locality_2026_08_15.py)

The product is **displayed, not adopted**. It is not written into
Admissibility. L1 is not attached. No fourth ball is used.

## Result Up Front

Admissibility requires a law-level distribution that is determined by
nearest-neighbor conditions. A July pair member names the product of signs of
the nonzero coordinates of the claim-delta `δ=w-s*(w)`, where `s*(w)` is the
nearest occupied site of a finite seed union `U`. That product can be scored
on the six neighbors of an unread site. The residual answered here is only
whether that 6-tuple is a function of the 6-NN occupancy at `v` alone.

It is not. On the declared three-seed union `U0` the occupancy and the
6-tuple are reported, and `s*(w)` is not always a neighbor of `v`. A second
three-seed union `U1` with centers in `[-2,2]^3` keeps the same occupancy at
`v` and changes the 6-tuple. The product therefore names distant seed
placement, which is extra structure beyond the star occupancy.

This is not a leftover-character membership claim for the product, and it is
not an equivariance claim for a different map. Those residuals are untouched.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite taxicab-ball unions, 6-NN occupancy, and lex-first nearest-site sign products are exact listings; the product is displayed and is not adopted as Admissibility content."
trace_class: negative_route_pruning
target_claim_id: admissibility_nn_determined_law
target_blocker_text: "Admissibility requires a law-level distribution that is NN-determined; the claim-delta sign-product 6-tuple is not such a distribution."
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Leave the product displayed. Do not write it into Admissibility. Do not attach L1. Continue the NN-determined-law residual on a different object."
conditional_surface_status: "exact for stars at unread v=(-1,1,1) on finite unions of radius-2 taxicab balls; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Record is quoted only as the unread-site boundary:

A site with no record cannot be read.

No axiom sentence is edited. The product is not inserted into Admissibility.
The axiom already names an NN-determined law-level distribution; a 6-tuple
that fails to be a function of the 6-NN occupancy cannot fill that role.

## Exact Objects

Write `0=(0,0,0)`, `e_1=(1,0,0)`, `e_2=(0,1,0)`, and `e_3=(0,0,1)`. The
closed taxicab ball of radius 2 is

`B_2(c)={x∈Z^3 : ||x-c||_1 ≤ 2}`.

Each such ball has 25 sites. A three-seed union is a union of three such
balls. The declared starting union is

`U0 = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`.

The scored site is the unread point `v=(-1,1,1)`. Its six neighbors, in the
fixed order `+e_1,-e_1,+e_2,-e_2,+e_3,-e_3`, are

```text
N(v) = ((0,1,1), (-2,1,1), (-1,2,1), (-1,0,1), (-1,1,2), (-1,1,0)).
```

Stars are scored at `v` only.

For a finite nonempty `U⊂Z^3` and a query site `w`, the nearest occupied
site `s*(w)` is the lexicographically first site of `U` at minimal taxicab
distance from `w`. The claim-delta is `δ(w)=w-s*(w)`. The sign product
`π(δ)` is the product of the signs of the nonzero coordinates of `δ`. The
empty product, used when `δ=(0,0,0)`, is `+1`.

The 6-NN occupancy and the claim-delta sign-product 6-tuple are

```text
σ(U)_i = 1 if N(v)_i ∈ U else 0,
c(U)_i = π(δ(N(v)_i)).
```

## Theorem 1 — Occupancy And Product On U0

The site `v` is unread on `U0`: `||v-0||_1=3`, `||v-(2,0,0)||_1=5`, and
`||v-(1,2,1)||_1=3`. The union has 62 sites.

Direct listing of the six neighbors against the three balls gives

```text
σ(U0) = (1, 0, 1, 1, 0, 1).
```

The occupied neighbors are `(0,1,1)`, `(-1,2,1)`, `(-1,0,1)`, and
`(-1,1,0)`. For each of those, `s*(w)=w` and `π((0,0,0))=+1`.

The two unoccupied neighbors are not decided by a neighbor of `v` alone:

| `w` | `s*(w)` | `δ` | `π(δ)` | `s*(w)∈N(v)` |
|---|---|---|---|---|
| `(0,1,1)` | `(0,1,1)` | `(0,0,0)` | `+1` | yes |
| `(-2,1,1)` | `(-2,0,0)` | `(0,1,1)` | `+1` | no |
| `(-1,2,1)` | `(-1,2,1)` | `(0,0,0)` | `+1` | yes |
| `(-1,0,1)` | `(-1,0,1)` | `(0,0,0)` | `+1` | yes |
| `(-1,1,2)` | `(-1,0,1)` | `(0,1,1)` | `+1` | yes |
| `(-1,1,0)` | `(-1,1,0)` | `(0,0,0)` | `+1` | yes |

So

```text
c(U0) = (1, 1, 1, 1, 1, 1),
```

and `s*(w)` is not always a neighbor of `v`. The unoccupied neighbor
`w=(-2,1,1)` is nearest to `(-2,0,0)`, which lies in `B_2(0)` and is not
one of the six neighbors of `v`.

## Theorem 2 — Same Occupancy, Different Product

Let

`U1 = B_2(0) ∪ B_2((1,2,1)) ∪ B_2((1,2,2))`.

This is a three-seed union. Its centers lie in `[-2,2]^3`. It is not `U0`.
The site `v` remains unread: `||v-(1,2,2)||_1=4`. No fourth ball is added.

The six-neighbor occupancy is unchanged:

```text
σ(U1) = (1, 0, 1, 1, 0, 1) = σ(U0).
```

The claim-delta 6-tuple changes. The unoccupied neighbor `w=(-1,1,2)` has
no site of `U0` at distance 1, and the lex-first distance-2 site in `U0` is
`(-1,0,1)`, giving `δ=(0,1,1)` and `π=+1`. On `U1` the same `w` has two
distance-1 sites, `(0,1,2)` and `(-1,2,2)`, both in `B_2((1,2,2))`. The
lex-first of those is `(-1,2,2)`, so `δ=(0,-1,0)` and `π=-1`. The other five
coordinates of `c` stay `+1`. Therefore

```text
c(U1) = (1, 1, 1, 1, -1, 1) ≠ c(U0).
```

A function of the 6-NN occupancy alone cannot take two values on one
occupancy. The product is not NN-determined on this family. The changed
coordinate is decided by the third seed `(1,2,2)`, which is not a neighbor
of `v`.

The primary runner exhausts every three-center union whose centers lie in
`[-2,2]^3` and confirms that this disagreement is not an isolated listing
error: many other same-occupancy triples change `c`. Existence of one
witness is the theorem.

## Theorem 3 — Displayed, Not Adopted

Theorem 2 is a geometric diagnostic. It is not a new Admissibility clause
and it is not a law-level distribution. The product is displayed, not
adopted.

Do not write the product into Admissibility. The axiom already requires an
NN-determined law-level `μ`. A 6-tuple that varies at fixed 6-NN occupancy
cannot be that `μ`.

Do not attach L1. The note does not promote the product to leftover
character, does not settle leftover-character membership of the product, and
does not settle equivariance of a different map.

No fourth ball is introduced to restore locality. Adding a further seed
would be a different family, not a repair of the three-seed residual.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| unread site `v=(-1,1,1)` | `v∉U0` and `v∉U1` |
| 6-NN occupancy on `U0` | exact listing `σ=(1,0,1,1,0,1)` |
| claim-delta 6-tuple on `U0` | exact listing `c=(1,1,1,1,1,1)` |
| `s*` not always a neighbor of `v` | `s*((-2,1,1))=(-2,0,0)` |
| same-occupancy disagreement | `U1` with `c=(1,1,1,1,-1,1)` |
| product written into Admissibility | refused |
| L1 attached | refused |
| fourth ball | not used |
| leftover-character membership of the product | not this residual |
| equivariance of a different map | not this residual |
| stars scored away from `v` | not executed |

## Boundary And Imports

The only imported geometry is the cubic lattice with taxicab balls and
nearest-neighbor adjacency. The only imported axiom sentences are the
quoted Lattice, Admissibility, and unread-site Record lines. No kernel
values, formation process, rate, leftover-character membership test, or
equivariance map is imported.

The July pair member is used only as the definition of the displayed
product. Membership of that pair and equivariance of any other map remain
separate residuals.

## No-Go Discipline Gate

The negative content is narrow: on stars at unread `v=(-1,1,1)`, the
claim-delta sign-product 6-tuple is not a function of the 6-NN occupancy
alone, among three-seed radius-2 unions. No compiler impossibility is
claimed. No replacement law is derived.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| keep `U0` | report `σ` and `c` | Theorem 1; `s*` is not always a neighbor of `v` |
| move the third seed inside `[-2,2]^3` | hold `σ` fixed | Theorem 2 witness `U1` |
| write the product into Admissibility | treat `c` as the NN-determined `μ` | refused; `c` is not NN-determined |
| attach L1 | reuse leftover-character membership | refused; different residual |
| add a fourth ball | enlarge the seed family | refused; different family |
| leftover-character membership | ask whether the product is leftover character | not executed |
| equivariance of a different map | ask whether another map is equivariant | not executed |
| score another star | change `v` | not executed |

### N2 — wall independence

Distant-seed naming of `s*` and the missing NN-determined law-level `μ` are
distinct residuals. This note claims no complete wall collection.

### N3 — hidden-condition scan

Radius 2, three seeds, lex-first nearest site, empty-product `+1`, the
fixed neighbor order, and the single unread site `v` are declared. No
fourth seed, no leftover-character test, and no Admissibility edit is
smuggled in.

### N4 — source residual matching

The current Admissibility sentence requires NN-determination of a law-level
distribution. The residual matched here is whether the displayed product
meets that NN-determination demand on the declared stars. It does not.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | named sites of `N(v)` and named `s*` values | no alphabet classification |
| per site | stars at unread `v` only | no other site scored |
| per mode | no mode calculation | no spectral claim |
| per block | three-seed unions `U0` and `U1` | no four-seed family |
| lattice wide | checked and not executed | no lattice-wide law |

### N6 — live partial-closure paths

Live routes are a different NN-determined object for the Admissibility
distribution, and the untouched leftover-character and equivariance
residuals. The displayed product is not one of those routes.

### N7 — hostile steelman

**Steelman:** Once the six neighbors of `v` are known, the nearest occupied
site of a radius-2 three-seed union should be a neighbor of `v` or else
should be fixed by that occupancy, so the sign product should be
NN-determined.

**Answer:** On `U0` the unoccupied neighbor `(-2,1,1)` is nearest to
`(-2,0,0)`, which is not a neighbor of `v`. Holding the occupancy fixed
and moving the third seed to `(1,2,2)` flips the sign product at
`(-1,1,2)`. Occupancy of `N(v)` does not name the distant seed.

### N8 — cross-cycle echo

This note does not close leftover-character membership of the product and
does not close equivariance of a different map. It reports only the
NN-determination failure of the displayed 6-tuple on the declared stars.

**Gate disposition:** PASS for the finite occupancy listings, the `U1`
disagreement, and the refusal to adopt the product. FAIL / DO NOT SHIP for
“the product is NN-determined,” “write the product into Admissibility,”
“attach L1,” or “a fourth ball restores the law.”

## Primary Runner

The companion runner rebuilds `U0` and `U1` from the three centers, scores
only the star at `v`, checks the Theorem 1 listings, exhibits the Theorem 2
disagreement, exhausts three-center unions in `[-2,2]^3` far enough to
confirm a same-occupancy sign change, and checks that the note keeps the
product displayed rather than adopted.
