---
claim_id: agebit_hopcost_independent_extras_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The age bit and the two-end hop-cost 8-tuple are independent displayed extras. Neither names the other. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/agebit_hopcost_independent_extras_2026_08_15.py
---

# Age Bit And Hop-Cost 8-Tuple Are Independent Extras (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the uneqrad lex-first breaker together with the eight
`G+` orbits of inward occupancy pairs on `B_3(0)`. The age bit `b` is
the older/newer label on the occupancy-named full axis. The hop cost
`c` is a `G+`-equivariant map from those eight orbits to `{1,2,3}`.
Score whether either extra names the other. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/agebit_hopcost_independent_extras_2026_08_15.py`](../scripts/agebit_hopcost_independent_extras_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment our-physics currently uses two extras: a 1-bit older/newer
on the occupancy-named full axis, and an 8-tuple hop cost on inward
occupancy pairs. Those scores each name one extra. bitsec scores the
age-bit section. minkbest scores one hop-cost 8-tuple among the 405
diamond-reversing fillings. The residual here is not leftover of bitsec
or minkbest (those score one extra). New residual: does either extra
name the other? If the age bit does not select `c`, and `c` does not
select the age bit, a matching member needs both.

On the uneqrad lex-first breaker, the age bit `b` names which end of
the unique full axis is older. The hop cost `c` is a `G+`-equivariant
map from the eight inward-occupancy-pair orbits to `{1,2,3}`.

**Theorem 1.** `b` is not a function of the 6-bit occupancy `σ`: the
same `σ` admits both `b=0` and `b=1` on displayed hosts (reuse uneqext
/ uneqbit). The hop-cost 8-tuple is not a function of `b`: flipping `b`
leaves inward occupancy pairs, hence `c`, unchanged.

**Theorem 2.** `c` is not a function of `σ` alone in the axiom text:
Admissibility does not supply a numerical hop cost. Among the 405
reversals, more than one 8-tuple exists, so occupancy of the one-seed
front does not select the minkbest 8-tuple.

**Theorem 3.** Displayed, not adopted. Do not write `b` or `c` into
Admissibility. Uniqueness of either extra is not claimed. Do not attach L1.
Qubit remains `M_2(C)`. No axiom edit.

## Current Premise Boundary

The Lattice, Admissibility, Record, and Qubit sentences used here are quoted
from [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

it does not supply the formation site, probability,
or rate.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

A site never carries more than one record; records are permanent.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility names neither the age bit `b` nor a numerical hop cost
`c` on inward occupancy pairs as the framework's fixed rule. The
nearest-neighbor clause is the reason a local law `μ` must be
determined by the six-neighbor conditions. Formation site and rate
remain outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact comparison of the uneqrad age bit against the eight-orbit hop-cost 8-tuple: same σ admits both b values, flipping b leaves inward occupancy pairs unchanged, and the 405 reversing fillings contain more than one 8-tuple. Displayed only."
trace_class: frontier_discovery
target_claim_id: agebit_hopcost_independent_extras
target_blocker_text: "whether the age bit and the two-end hop-cost 8-tuple name each other"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the same-σ both-b pair, the b-independent occupancy-pair orbits, and the many reversing 8-tuples; do not write b or c into Admissibility or attach L1"
conditional_surface_status: "exact on the uneqrad breaker, the uneqext same-σ star, and the B_3(0) eight-orbit family; neither extra names the other; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. The uneqrad lex-first
breaker is

`U_uneq = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`,
radii `(2, 1, 3)`,
`v = (−3,−3,−1)`.

Occupancy `σ` is the 6-bit nearest-neighbor indicator of a union at an
unread site, in slot order

`(+x, −x, +y, −y, +z, −z)`.

On an occupied neighbor `w`,

`t(w) = min_i ‖w − s_i‖_1`.

Empty slots have no tick. Direct distances give `v ∉ U_uneq`,

`σ = (1, 0, 1, 0, 1, 1)`,
`t = (1, ·, 1, ·, 3, 2)`.

That mask empties `−x` and `−y` and names unique full axis `z`. The
displayed age bit is

`b = 1` if `t(−z) < t(+z)`, else `0`.

On the breaker, `t(−z) = 2 < 3 = t(+z)`, so `b = 1`.

The uneqext lex-first same-`σ` star (not a breaker) is

`(s1,s2,s3) = ((−2,−2,−2), (−2,−2,−1), (−2,−2,0))`, radii `(2, 1, 2)`,
same unread site `v = (−3,−3,−1)`, with the same occupancy
`σ = (1, 0, 1, 0, 1, 1)` and ticks
`t = (1, ·, 1, ·, 2, 2)`.

There `t(−z) = 2` is not strictly less than `t(+z) = 2`, so `b = 0`.

Let `B_3(0)` be the set of sites of `Z^3` reachable from the origin by
at most three nearest-neighbor steps. One-seed growth starts at `0`.
The occupancy `σ_n` at a site `n` is the 6-bit string whose
direction-`d` bit is set exactly when the neighbor of `n` in direction
`d` is strictly nearer the seed. This is the inward occupation of the
one-seed front.

`G+` is the 24-element group of proper cubic rotations about the seed.
A hop cost `c(σ_v, σ_w) ∈ {1,2,3}` on a directed nearest-neighbor edge
`v → w` is `G+`-equivariant when it is constant on `G+` orbits of
endpoint pairs. The eight `G+` orbits of inward occupancy pairs on
this ball, written as inward-weight pairs `(|σ_v|, |σ_w|)`, are

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2).
```

A filling reverses the diamond axis/diagonal order when
`3 t(3,0,0)^2 > 9 t(1,1,1)^2`. Exactly 405 of the `3^8 = 6561`
fillings reverse that order. The lex-first reversing filling is
`c = (1, 1, 3, 1, 1, 1, 1, 1)`. The minkbest 8-tuple
`c = (3, 1, 3, 1, 1, 3, 1, 1)` is one other reversing filling.

Score the two displayed uneqrad hosts and the eight-orbit family on
`B_3(0)`. Uniqueness of either extra is not required.

## Theorem 1 — `b` is not a function of `σ`; `c` is not a function of `b`

On `U_uneq` at `v`, occupied neighbors and ticks are

- `+x = (−2,−3,−1)` has `t = 1`,
- `+y = (−3,−2,−1)` has `t = 1`,
- `+z = (−3,−3,0)` has `t = 3`,
- `−z = (−3,−3,−2)` has `t = 2`.

Hence mixed `t = (1, ·, 1, ·, 3, 2)` at `σ = (1, 0, 1, 0, 1, 1)` and
`b = 1`. Occupancy names the unique full axis `z`; it does not name
which end of that axis is older.

On the uneqext lex-first same-`σ` star the same unread site has the
same occupancy and

- `+x` has `t = 1`,
- `+y` has `t = 1`,
- `+z` has `t = 2`,
- `−z` has `t = 2`.

So `b = 0` at the same `σ`. The same 6-bit occupancy therefore admits
both `b = 0` and `b = 1` on displayed hosts. `b` is not a function of
`σ`. This reuses the uneqext same-`σ` star and the uneqbit breaker
bit; it is not leftover of those scores of one extra.

The hop-cost 8-tuple is a map on inward occupancy pairs. Those pairs
are occupancy data: a bit is set exactly when a neighbor is strictly
nearer the seed. Flipping `b` changes only the older/newer label on
the named full axis. It leaves every occupancy bit, hence every
inward occupancy pair, unchanged. The eight `G+` orbits, and therefore
any `G+`-equivariant `c` on those orbits, are the same at `b = 0` and
at `b = 1`. The hop-cost 8-tuple is not a function of `b`.

## Theorem 2 — `c` is not a function of occupancy in the axiom text

Admissibility supplies one fixed nearest-neighbor rule, covariant
under lattice translations and proper cubic rotations, and says that
the local distribution varies with nearest-neighbor conditions. It
does not supply a numerical hop cost. The live axiom memo contains
neither `c(σ_v, σ_w)` nor an 8-tuple of values in `{1,2,3}`.

On `B_3(0)` the one-seed front occupancy is one fixed 6-bit field at
each site. That occupancy names the eight pair-orbits. It does not
select a numerical value on those orbits. There are `3^8 = 6561`
`G+`-equivariant maps to `{1,2,3}`. Among them, 405 reverse the
diamond axis/diagonal order. Those 405 already contain more than one
8-tuple: the lex-first reversal `(1, 1, 3, 1, 1, 1, 1, 1)` and the
minkbest tuple `(3, 1, 3, 1, 1, 3, 1, 1)` are two distinct reversing
fillings. Occupancy of the one-seed front therefore does not select
the minkbest 8-tuple.

A matching member that wants both extras needs both: `b` does not
name `c`, and `c` does not name `b`. This is not leftover of bitsec
(one age-bit extra) or minkbest (one hop-cost extra).

## Theorem 3 — displayed, not adopted

The two `b` values at one `σ`, the `b`-independence of inward
occupancy pairs, and the many reversing 8-tuples are displayed member
data. They are not the framework's fixed Admissibility rule. This
note does not write `b` or `c` into Admissibility. Do not write b or
c into Admissibility. Uniqueness of either extra is not claimed. Do not attach L1.
Occupancy-only formation is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first breaker and the
  uneqext same-`σ` star, `σ = (1, 0, 1, 0, 1, 1)` admits `b = 1` and
  `b = 0`. Flipping `b` leaves inward occupancy pairs unchanged, so
  `c` is not a function of `b`. Admissibility does not supply a
  numerical hop cost. Among the 405 reversals, more than one 8-tuple
  exists, so occupancy of the one-seed front does not select the
  minkbest 8-tuple.
- **What is displayed only.** The age bit and the hop-cost 8-tuple
  are two rival extras. They are not adopted. Uniqueness of either
  extra is not claimed.
- **What is not claimed.** No attachment of `b`, `c`, radii, integer
  `t`, or a path-length law to Admissibility; no attachment of
  occupancy-only formation; no axiom edit; no formation rate; no
  leftover of bitsec or minkbest (those score one extra); no
  compiler no-go.
- **Mutation controls.** A rebuilt same-`σ` pair that fails to admit
  both `b` values fails. A rebuilt flip of `b` that changes inward
  occupancy pairs fails. A rebuilt reversing family with only one
  8-tuple fails. A note that writes `b` or `c` into Admissibility,
  attaches L1, claims uniqueness, or authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the uneqrad lex-first host and the
uneqext same-`σ` star, the two age bits at that common `σ`, the
eight `G+` orbits of inward occupancy pairs on `B_3(0)`, the census
that more than one of the 405 reversing 8-tuples exists, the current
premise boundary, and the mutation controls. It writes no cache and
authors no audit verdict.
