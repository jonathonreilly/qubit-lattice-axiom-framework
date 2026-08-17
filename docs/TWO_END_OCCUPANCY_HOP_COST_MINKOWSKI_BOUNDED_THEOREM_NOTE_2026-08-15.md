---
claim_id: two_end_occupancy_hop_cost_minkowski_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_3(0), whether G+-equivariant two-end occupancy hop costs can reverse the diamond axis/diagonal order is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_end_occupancy_hop_cost_minkowski_2026_08_15.py
---

# Two-End Occupancy Hop Costs Stay Diamond On `B_3(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact orbit census and exact integer path-cost comparison on the
radius-3 nearest-neighbor ball of one seed. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_end_occupancy_hop_cost_minkowski_2026_08_15.py`](../scripts/two_end_occupancy_hop_cost_minkowski_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Let `B_3(0)` be the set of sites of `Z^3` reachable from the origin by at
most three nearest-neighbor steps. One-seed growth starts at `0`. The
occupancy `σ_n` at a site `n` is the 6-bit string whose direction-`d` bit is
set exactly when the neighbor of `n` in direction `d` is strictly nearer the
seed. This is the inward occupation of the one-seed front.

`G+` is the 24-element group of proper cubic rotations about the seed. It
acts on sites and, simultaneously, on the six direction bits. A hop cost
`c(σ_v, σ_w) ∈ {1,2}` on a directed nearest-neighbor edge `v → w` is
`G+`-equivariant when it is constant on `G+` orbits of endpoint pairs.
Arrival time `t(n)` is the minimum path cost from `0` to `n` through
`B_3(0)`.

On this ball the axis point `(3,0,0)` and the body-diagonal point `(1,1,1)`
obey

```text
t(3,0,0)^2 / 9  <=  t(1,1,1)^2 / 3
```

for every such cost. No `G+`-equivariant two-end occupancy cost in `{1,2}`
reverses the diamond axis/diagonal order. The comparison is reported on
`B_3(0)` only. Displayed, not adopted.

The family is not a leftover of an arrival-only (one-endpoint) quotient:
pairs that share an arrival occupancy can sit in distinct `G+` orbits, and
the two-end census is taken before any arrival-only collapse.

## Exact Theorems

### Theorem 1

The directed nearest-neighbor edges of `B_3(0)` carry exactly eight
`G+` orbits of endpoint occupancy pairs. Representatives, written as
inward-weight pairs `(|σ_v|, |σ_w|)`, are

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2).
```

`B_3(0)` has 63 sites and 228 directed nearest-neighbor edges. The six
seed-exit edges `0 → ±e_i` occupy the single orbit `(0,1)`. Both axis
extensions `(1,0,0) → (2,0,0)` and `(2,0,0) → (3,0,0)` occupy the single
orbit `(1,1)`. The site `(3,0,0)` has a unique neighbor in the ball,
namely `(2,0,0)`.

### Theorem 2

There are `2^8 = 256` `G+`-equivariant maps from those orbits to `{1,2}`.
None of them reverses

```text
t(3,0,0)^2 / 9  <=  t(1,1,1)^2 / 3.
```

Equivalently, every assignment satisfies the integer comparison
`3 t(3,0,0)^2 <= 9 t(1,1,1)^2`. Two-end occupancy costs therefore stay
diamond on `B_3(0)`.

The same conclusion follows from the shared seed-exit orbit without listing
all 256 fillings. Every path leaves the seed along an edge of orbit
`(0,1)`, of common cost `c0 ∈ {1,2}`. The unique three-step path to
`(3,0,0)` then uses two edges of orbit `(1,1)`, of common cost `c_aa`, so

```text
t(3,0,0) = c0 + 2 c_aa ∈ {3,4,5,6}.
```

Every path to `(1,1,1)` has at least three steps, so `t(1,1,1) ≥ c0 + 2`.
If `c0 = 1`, then `t(3,0,0) ≤ 5` and `t(1,1,1) ≥ 3`, and `3·25 = 75` is
strictly less than `9·9 = 81`. If `c0 = 2`, then `t(3,0,0) ≤ 6` and
`t(1,1,1) ≥ 4`, and `3·36 = 108` is strictly less than `9·16 = 144`.
Detours inside `B_3(0)` cannot raise the axis minimum above the three-step
path and cannot lower the diagonal minimum below three steps.

### Theorem 3

The cost family is displayed as a finite probe on `B_3(0)`. It is
not written into Admissibility. No path-length law is attached. The live axiom
memo continues to state that there is one fixed nearest-neighbor
admissibility rule, covariant under translations and proper cubic
rotations; that rule is not replaced by `c(σ_v, σ_w)`. Displayed, not
adopted.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name `B_3(0)` and the six direction bits | closed by the nearest-neighbor graph of `Z^3` |
| define inward occupancy of the one-seed front | closed: a bit is set exactly on a strictly nearer neighbor |
| count `G+` | closed: 24 proper cubic rotations |
| count orbits of realized endpoint pairs | closed by Theorem 1; eight orbits |
| exhaust `{1,2}` fillings | closed by Theorem 2; 256 maps, zero reversals |
| bound the two comparison points without exhaustion | closed by the shared seed-exit orbit |
| write a cost into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| filling | `t(3,0,0)` | `t(1,1,1)` | `3 t_axis^2` | `9 t_diag^2` | diamond? |
|---|---:|---:|---:|---:|---|
| every orbit cost `1` | `3` | `3` | `27` | `81` | yes |
| every orbit cost `2` | `6` | `6` | `108` | `324` | yes |
| seed-exit `1`, axis-extension `2` | `≤ 5` | `≥ 3` | `≤ 75` | `≥ 81` | yes |
| seed-exit `2`, remaining hops `1` | `≤ 6` | `≥ 4` | `≤ 108` | `≥ 144` | yes |

The table is an exact illustration of Theorem 2, not an adopted dynamics.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply a
numerical hop cost on occupancy pairs. This note therefore treats
`c(σ_v, σ_w) ∈ {1,2}` as a displayed probe, not as an axiom clause.

Record is not used. No formation site, formation rate, or readout value is
assigned to an unoccupied site. The seed is a theorem hypothesis for the
one-seed front, not a privileged physical site.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `Z^3` nearest-neighbor adjacency and proper cubic rotations | ambient lattice | live axiom memo |
| one-seed front from `0` | theorem hypothesis | declared; no site is privileged in the axiom |
| `σ_n` as 6-bit inward occupation | occupancy used by the probe | defined from the one-seed front |
| `c(σ_v, σ_w) ∈ {1,2}` | displayed `G+`-equivariant hop cost | mathematical input; not an axiom |
| comparison points `(3,0,0)` and `(1,1,1)` | diamond axis/diagonal order on `B_3(0)` | declared test pair |
| arrival-only one-endpoint quotient | context, not a load-bearing parent | two-end orbits are counted first |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Collapse pairs to arrival occupancy only: distinct two-end orbits that
   share `|σ_w|` are identified, so the census is no longer two-end.
2. Replace the eight-orbit count by seven or nine: the enumerated
   representatives are exactly the eight inward-weight pairs above.
3. Assert a reversing filling: every one of the 256 maps obeys
   `3 t(3,0,0)^2 <= 9 t(1,1,1)^2`.
4. Raise the axis time above the three-step path: the path
   `0 → (1,0,0) → (2,0,0) → (3,0,0)` lies in `B_3(0)` and is always
   available.
5. Write `c` into Admissibility: the live axiom memo still states one
   fixed covariant nearest-neighbor rule and contains no two-end occupancy
   hop cost.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_3(0)`.
- Arrival-only one-endpoint costs are not reused as the two-end proof.
- No continuum Minkowski metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: on `B_3(0)`, no `G+`-equivariant two-end
occupancy hop cost with values in `{1,2}` reverses the diamond
axis/diagonal order, and the displayed family is not an Admissibility
clause. It is not a claim that every conceivable edge law stays diamond.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| axis-extension expensive, turns cheap | Put cost `2` on orbit `(1,1)` and cost `1` on `(1,2)` and `(2,3)`. | Theorem 2: the shared seed-exit still forces `t(3,0,0) ≤ 5` and `t(1,1,1) ≥ 3`, so `75 < 81`. | **ATTEMPTED** |
| expensive seed-exit | Put cost `2` on orbit `(0,1)`. | Theorem 2: `t(1,1,1) ≥ 4` and `t(3,0,0) ≤ 6`, so `108 < 144`. | **ATTEMPTED** |
| face-site detour to the axis | Route `(3,0,0)` through a weight-2 site. | The three-step axis path remains available, so the axis minimum cannot rise; the runner's 256-map census records zero reversals. | **ATTEMPTED** |
| body-site detour to the axis | Route `(3,0,0)` through a weight-3 site. | Same bound: detours cannot raise a minimum. `(3,0,0)` has a unique in-ball neighbor, so every path still ends on a `(1,1)` hop. | **ATTEMPTED** |
| reverse-direction and backtracking | Allow inbound orbits `(1,0)`, `(2,1)`, `(3,2)`. | Those orbits are included in the eight-orbit census; the 256 fillings still keep the diamond order. | **ATTEMPTED** |
| arrival-only leftover | Collapse each pair to `σ_w` and reuse a one-endpoint argument. | Theorem 1 counts two-end pairs before any collapse; orbits `(1,1)` and `(0,1)` share no arrival class with `(1,2)`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The shared-seed-exit bound and the 256-map census are two
certificates of the same diamond-order statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| shared-seed-exit bound / 256-map census | yes, as an analytic upper bound on the same comparison | yes, as an exhaustive check of the same comparison | collapse into Theorem 2 |
| diamond-order statement / adoption refusal | no: a probe can stay diamond and still be refused as an axiom | no: refusing adoption does not decide the comparison | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “`c ∈ {1,2}`” | displayed finite probe, not a derived scale |
| “`G+`-equivariant” | covariance under the axiom's proper cubic rotations |
| “stay diamond” | the displayed axis/diagonal inequality on `B_3(0)` only |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/two_end_occupancy_hop_cost_minkowski_2026_08_15.py:245` | number of pair orbits | exactly eight `G+` orbits | yes |
| `scripts/two_end_occupancy_hop_cost_minkowski_2026_08_15.py:267` | reversing two-end filling | zero of 256 assignments reverse the order | yes |
| `scripts/two_end_occupancy_hop_cost_minkowski_2026_08_15.py:279` | shared seed-exit bound | `c0=1` and `c0=2` both stay diamond | yes |
| `scripts/two_end_occupancy_hop_cost_minkowski_2026_08_15.py:294` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_3(0)` edge | one inward occupancy pair; no other edge family is classified |
| per site | yes: occupancy is the 6-bit inward front at that site | no other occupancy dictionary is used |
| per mode | yes: eight pair-orbits and all 256 fillings | other value sets and larger balls are untested and unclaimed |
| per block | yes: the two comparison points on `B_3(0)` | the diamond order is the stated inequality only |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, and none is
reclassified as an import or wall.

One partial-closure mechanism is recorded rather than suppressed. The
arrival-only (one-endpoint) quotient of the same pairs is a coarser
probe. It is not used to close Theorem 2, and the two-end census is
strictly finer. The remaining physical choice—whether any hop cost belongs
in Admissibility—stays explicit and does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that a two-end cost can make axis extensions
expensive and diagonal turns cheap, and that this should reverse the
normalized axis/diagonal order because the two comparison points then
use different pair orbits after the first hop. The objection correctly
identifies that the two-end family is finer than arrival-only. It fails
because the first hop is shared: every path, axis or diagonal, pays the
same seed-exit cost, and the remaining budget in `{1,2}` cannot push
`t(3,0,0)^2/9` above `t(1,1,1)^2/3`. The 256-map census is the hostile
check of that budget.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| arrival-only occupancy costs in `{1,2}` | one-endpoint quotient of the same front | counted as a strictly coarser probe; Theorem 1 does not collapse pairs |

No earlier mechanism retires the two-end census or the adoption refusal.

No-Go Discipline disposition: **PASS** for the bounded comparison and the
adoption boundary stated at the start of this section.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

## Runner Contract

The companion runner builds the 24 proper cubic rotations, the 63-site ball,
and the 228 directed edges; counts the eight `G+` orbits of inward occupancy
pairs; exhausts the 256 `{1,2}` fillings; checks the shared-seed-exit bound;
rejects the mutation families; and verifies that the live axiom memo does
not host the displayed cost. Declared audit inputs are this note and the
axiom memo.
