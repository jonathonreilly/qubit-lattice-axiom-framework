---
claim_id: c2d4_deep_interior_cost2_samek_k13_b39_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=13 under the named c2d4-plus-deep-interior hop-cost on B_39(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_deep_interior_cost2_samek_k13_b39_2026_08_15.py
---

# Same-k Reverse At k=13 Under The Named C2d4-Plus-Deep-Interior Hop-Cost On B_39(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival comparison at k=13 on the finite nearest-neighbor
graph `B_39(0)`, under the named c2d4-plus-deep-interior hop-cost `j2` displayed
for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_deep_interior_cost2_samek_k13_b39_2026_08_15.py`](../scripts/c2d4_deep_interior_cost2_samek_k13_b39_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named c2d4-plus-deep-interior hop-cost `j2` is
the first display of `j2` at `k=13`. The parent clauses `ν`, `μ`, `ρ3`, and
`c2d4` are those of the cost-2 max≥4 out-face scoring:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`;
- `j2(v→w) = 3` if `ρ3` would be `3`, else `2` if `c2d4` would be `2` or
  (`|σ_v|=|σ_w|=3` and `min_i |w_i| ≥ 3`), else `1`.

The extra deep-interior clause prices a fully supported `3→3` hop whose
destination least absolute coordinate is at least `3`. It fires on
`(3,3,3) → (4,3,3)` at cost `2`. It also fires on `(2,3,3) → (3,3,3)` at
cost `2`. It does not fire on `(2,2,2) → (3,2,2)`, whose destination least
absolute coordinate is `2`. It does not fire on the height-`2` ridge
`(4,2,2) → (5,2,2)`. It does not fire on `(4,3,1) → (5,3,1)`, whose
destination least absolute coordinate is `1`. The parent `c2d4` extra
remains: `(4,2,0) → (5,2,0)` stays at cost `2`. The skipped max≥3 out hop
`(3,2,0) → (4,2,0)` stays at cost `1`. The interior comparator `i2` prices
every dest-min-`≥2` interior `3→3` hop at `2`; `j2` is not that clause.
Uniqueness is not claimed.

The finite host is scored independently: one origin Dijkstra is run on this
ball. The ball is not leftover of a larger-ball table.

```text
B_39(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 39 }.
```

It has 82239 sites. Edges are the cubic nearest-neighbor steps that remain
inside `B_39(0)`. One Dijkstra from the origin yields

```text
t(13,0,0) = 29
t(13,13,13) = 54
```

The same-k comparison at k=13 is

```text
t(13,0,0)^2 / 169 = 841/169 = 2523/507
t(13,13,13)^2 / 507 = 2916/507
2523/507 < 2916/507
```

Equivalently `2523 < 2916`. The inequality `t(13,0,0)^2 / 169 > t(13,13,13)^2 / 507`
does not hold. Same-k reverse at k=13 under `j2` is reported no. Displayed,
not adopted.

A witness axis walk of cost `29` is seed-exit `3` onto `(1,0,0)`, unit-cube
leave `1` onto `(1,1,0)`, unit-cube enter `1` onto `(1,1,1)`, ridge-slide
`3` onto `(2,1,1)`, support-preserving `1` onto `(2,2,1)`, eleven
support-preserving cost-`1` hops to `(13,2,1)`, ridge-slide `3` onto
`(13,1,1)`, support-drop `3` onto `(13,1,0)`, and support-drop `3` onto
`(13,0,0)`. That walk is a witness of cost `29`, not a uniqueness claim.

A witness body walk of cost `54` is the same prefix of cost `9` to
`(2,2,1)`, eleven cost-`1` hops to `(13,2,1)`, eleven cost-`1` hops to
`(13,13,1)`, one dest-min-`2` interior `3→3` hop of cost `1` onto
`(13,13,2)`, and eleven deep-interior `3→3` hops of cost `2` to
`(13,13,13)`, summing to `54`. Independently, `t(13,13,1) = 31` and
`t(13,13,2) = 32`. Those last eleven hops have destination least absolute
coordinate at least `3`, so the deep-interior clause is live on the body
walk. That walk is a witness of cost `54`, not a uniqueness claim.

On the max≥4 out hop `(4,2,0) → (5,2,0)` one has `|σ_v|=|σ_w|=2`, dest max
`5` greater than source max `4`, and source max already `4`, so `ρ3 = 1`
while `c2d4 = 2` and `j2 = 2`. Independently, `t(4,2,0) = 10` and
`t(5,2,0) = 12`. On the skipped max≥3 out hop `(3,2,0) → (4,2,0)` the
`c2d4` extra is idle because the source max is `3`; both `c2d4` and `j2`
cost `1`. Independently, `t(3,2,0) = 9`. On the dest-min-`2` interior hop
`(2,2,2) → (3,2,2)` one has `|σ|=3→3` and dest min `2`, so `c2d4 = 1`,
`i2 = 2`, and `j2 = 1`. On the dest-min-`3` interior hop
`(3,3,3) → (4,3,3)` one has `|σ|=3→3` and dest min `3`, so `c2d4 = 1`
while `j2 = 2`. Independently, `t(3,3,3) = 14`, `t(4,3,2) = 13`, and
`t(4,3,3) = 15`. Therefore `c2d4` cannot price the deep-interior clause,
and the body arrival `54` is not leftover of `c2d4`.

The displayed body last hop `(12,13,13) → (13,13,13)` has dest min `13`,
so `j2 = 2`. The displayed dest-min-`2` interior hop is not a leftover of
`i2`: on `(2,2,2) → (3,2,2)` one has `i2 = 2` while `j2 = 1`, and on
`(4,2,2) → (5,2,2)` one has `i2 = 2` while `j2 = 1`. On
`(3,3,3) → (4,3,3)` both `i2` and `j2` cost `2`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_39(0) reports t(13,0,0) and t(13,13,13) under the named c2d4-plus-deep-interior hop-cost and scores the k=13 same-k comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: c2d4_deep_interior_cost2_samek_k13
target_blocker_text: "whether same-k reverse at k=13 still holds after interior 3-to-3 hops with dest min abs coord at least 3 are priced at 2 on top of c2d4"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded arrival comparison"
conditional_surface_status: "exact on B_39(0) under the named hop-cost; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `j2` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_39(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`,
  `c2d4`, and `j2` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `j2` into Admissibility, selecting it as
  a physical cost, or lifting the comparison off `B_39(0)` remain separate
  obligations. This note does not close them.

## Exact Objects

All runner values are integers. No float is used in the comparison.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

`j2` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`j2`, using one Dijkstra on `B_39(0)`.

Representative values:

| hop | class | `j2` |
|---|---|---|
| `(0,0,0)→(1,0,0)` | leave origin | `3` |
| `(1,0,0)→(2,0,0)` | `1→1` | `3` |
| `(1,0,0)→(1,1,0)` | `1→2` | `1` |
| `(1,1,0)→(1,1,1)` | `2→3` unit cube | `1` |
| `(1,1,0)→(2,1,0)` | corridor `2→2` | `3` |
| `(2,2,0)→(3,2,0)` | plane `2→2` with min nonzero `2` | `1` |
| `(3,2,0)→(4,2,0)` | skipped max≥3 out-face | `1` |
| `(4,2,0)→(5,2,0)` | max≥4 out-face | `2` |
| `(4,1,0)→(5,1,0)` | corridor already in `ρ3` | `3` |
| `(2,2,2)→(3,2,2)` | dest-min-`2` interior `3→3` | `1` |
| `(3,3,2)→(4,3,2)` | dest-min-`2` non-ridge `3→3` | `1` |
| `(4,2,2)→(5,2,2)` | height-`2` ridge `3→3` | `1` |
| `(1,2,2)→(2,2,2)` | dest-min-`2` equal-coordinate `3→3` | `1` |
| `(3,3,3)→(4,3,3)` | dest-min-`3` interior `3→3` | `2` |
| `(2,3,3)→(3,3,3)` | dest-min-`3` enter | `2` |
| `(4,3,1)→(5,3,1)` | min-`1` non-ridge `3→3` | `1` |
| `(4,1,1)→(5,1,1)` | unit ridge `3→3` | `3` |
| `(12,13,13)→(13,13,13)` | last hop onto `(13,13,13)` | `2` |

## Theorem 1 — Arrival times at k=13

Under `j2` on `B_39(0)`,

```text
t(13,0,0) = 29
t(13,13,13) = 54
```

Both sites lie in the ball: `13 ≤ 39` and `13+13+13 = 39`. The search
visits `82239` sites, which is the exact census of `B_39(0)`. The runner
computes both values from the single origin Dijkstra and checks them
against the explicit walks above. These values are Dijkstra outputs, not
fitted scalars.

The word "unique" here names the single Dijkstra run required by the
theorem, not uniqueness of a realizing hop sequence.

## Theorem 2 — Same-k comparison at k=13

The displayed comparison is whether

```text
t(13,0,0)^2 / 169 > t(13,13,13)^2 / 507.
```

Substituting the computed times gives the integer statement `841/169 > 2916/507`,
or equivalently `2523 > 2916`. Cross-multiplication is exact:

```text
29^2 · 507 = 426387
54^2 · 169 = 492804
426387 < 492804
```

Therefore `t(13,0,0)^2 / 169 > t(13,13,13)^2 / 507` is false, so
the displayed inequality does not hold. Displayed, not adopted.

## Theorem 3 — No axiom write and no L1 attachment

Do not write j2 into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `j2`, `c2d4`, `ρ3`, `μ`, or `ν`. This
note proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost. The coordinate-sum that names `B_39(0)` is not
attached as an arrival law.

## What This Does Not Claim

- No uniqueness claim is made for this named hop-cost at k=13.
- The live dest-min-`≥3` interior `3→3` clause on `B_39(0)` is not a statement
  about larger hosts.
- No physical identification of `t` as a clock, mass, or force law is made.
- No claim is made that Record locks these arrival times.
- Independent leftovers on larger balls are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site graph and the
refusal to treat a named hop-cost as axiom content.

## Current Premise Boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

When present, a record locks exactly one admissible local possibility.

A site with no record cannot be read.

Lattice supplies the cubic graph used to name nearest-neighbor hops. Qubit
and Record are unused beyond vocabulary and the unread-absence boundary.
Admissibility is quoted and is not edited. `j2` is a declared scoring on that
already-named graph.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `B_39(0)` | finite search domain | declared as sites with coordinate-sum at most `39` |
| six nearest-neighbor shifts | hop graph | Lattice adjacency, restricted to the ball |
| `ν`, `μ`, `ρ3`, `c2d4`, `j2` | named hop-costs | declared integer scoring; not axiom content |
| `t(13,0,0)`, `t(13,13,13)` | arrivals | one Dijkstra from the origin |
| `169`, `507` | displayed denominators | `13^2` and `3·13^2`; comparison only |
| Record unread sentence | absence boundary | live axiom memo, quoted |

There are no measured, fitted, literature, or observational inputs. No second
search is run. No hop-cost is written into Admissibility.

## No-Go Discipline

The negative report is only that the displayed same-k inequality is false
for this named scoring on this named ball. It is not a universal obstruction
against other declared scorings.

No-Go Discipline disposition: **PASS** for the displayed comparison and the
refusal to adopt `j2` or attach a coordinate-sum arrival.

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| attach the coordinate-sum itself as arrival | **ATTEMPTED** | the ball predicate is not the scored arrival; `t(13,0,0)=29 ≠ 13` |
| write `j2` into Admissibility | **ATTEMPTED** | Theorem 3 refuses the edit; the live sentences are unchanged |
| claim a unique cheapest path | **ATTEMPTED** | uniqueness of a realizing sequence is outside the target |
| adopt the same-k reverse as a law | **ATTEMPTED** | Theorem 2 is displayed, not adopted, and the inequality is false |
| run a second search from the body site | **ATTEMPTED** | one origin Dijkstra already returns both arrivals |
| enlarge the ball or add non-neighbor hops | **ATTEMPTED** | the theorem is only `B_39(0)` with the six in-ball shifts |

### N2 — wall independence

One comparison is reported: the displayed `k=13` same-k inequality under
`j2`. Failure of that inequality is not a second impossibility wall and is
not promoted to a no-go against later named scorings.

### N3 — hidden-wall scan

The ball, the six shifts, and the integer costs are declared. No clock,
boost, continuum limit, occupancy growth, or Record readout of `t` is
imported.

### N4 — residual matching

The residual that remains after this report is the same one named in the
claim scope: a same-k reverse at `k=13` under this hop-cost is not obtained.
The residual is not enlarged. Closing it would require a different declared
scoring or a different theorem, not an axiom edit.

### N5 — certificate granularity

```text
per-element: executed — j2 samples and both k=13 targets
per-site: executed — origin, (13,0,0), and (13,13,13)
per-mode: executed — the single named c2d4-plus-deep-interior hop-cost
per-block: executed — the displayed k=13 comparison only
lattice-wide: not executed — no axiom edit and no attached arrival law
```

### N6 — partial-closure paths

A later named scoring on the same graph could be compared in the same
displayed way. Any such scoring remains a declaration until independently
supported. Admissibility need not change.

### N7 — steelman

The strongest objection is that a cheaper path to `(13,13,13)` might exist
outside `B_39(0)` or along a non-neighbor step. Correct: those graphs are
different theorems. Inside the declared ball and six-shift graph, the
origin Dijkstra is exhaustive.

### N8 — cross-cycle echo

Earlier hop-cost scores at other `k` or under `c2d4` or `i2` are not consumed
as premises. This note is the first display of `j2` at `k=13` on `B_39(0)`
and stands on one Dijkstra plus exact rational arithmetic.

## Boundaries and explicit non-claims

- `j2` is displayed hop-cost data. It is not an axiom, primitive, or adopted
  law.
- The same-k comparison is displayed, not adopted.
- Uniqueness of a cheapest path is not claimed.
- The coordinate-sum that names `B_39(0)` is not attached as an arrival law.
- No Record readout of `t`, no clock, and no continuum identification is
  asserted.
- No axiom, primitive, registry, citation manifest, or audit verdict is
  edited.

## Runner Contract

The companion runner builds `B_39(0)`, evaluates the named hop-cost, and
runs one Dijkstra from the origin. It reports `t(13,0,0)` and `t(13,13,13)`,
checks the integer form of Theorem 2, checks that the dest-min-`≥3` interior
`3→3` clause adds a cost-`2` tax that `c2d4` does not, keeps dest-min-`2`
interior hops at cost `1`, keeps the max≥4 out-face tax at `2`, skips
`(3,2,0) → (4,2,0)` as a new tax, checks that the live Admissibility wording
does not name `j2`, and records the import boundary. Declared review inputs
are this note and the axiom memo only.

## Verification

Run:

```bash
python3 scripts/c2d4_deep_interior_cost2_samek_k13_b39_2026_08_15.py
```

The runner evaluates one origin Dijkstra on `B_39(0)`, checks the named
hop-cost samples, the two arrivals, the exact reverse comparison, the live
axiom quotes, and the N1–N8 packet. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
