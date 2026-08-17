---
claim_id: two_end_occupancy_cost3_minkowski_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_3(0), whether G+-equivariant two-end occupancy hop costs in {1,2,3} can reverse the diamond axis/diagonal order is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_end_occupancy_cost3_minkowski_2026_08_15.py
---

# Two-End Occupancy Costs In `{1,2,3}` Reverse The Diamond Order On `B_3(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact orbit census and exact integer path-cost comparison on the
radius-3 nearest-neighbor ball of one seed. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_end_occupancy_cost3_minkowski_2026_08_15.py`](../scripts/two_end_occupancy_cost3_minkowski_2026_08_15.py)
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
`c(σ_v, σ_w) ∈ {1,2,3}` on a directed nearest-neighbor edge `v → w` is
`G+`-equivariant when it is constant on `G+` orbits of endpoint pairs.
Arrival time `t(n)` is the minimum path cost from `0` to `n` through
`B_3(0)`.

The eight `G+` orbits of inward occupancy pairs on this ball are the same
orbits used by the binary `{1,2}` probe. Enlarging the value set to `{1,2,3}`
is not a leftover of that binary census: a cost-`3` axis-extension orbit is
absent from `{1,2}`, and the binary seed-exit bound no longer decides the
comparison.

On `B_3(0)`, some of the `3^8 = 6561` fillings reverse

```text
t(3,0,0)^2 / 9  <=  t(1,1,1)^2 / 3.
```

Exactly 405 fillings reverse the order. The lex-first reversing filling, in
the orbit order of Theorem 1, is

```text
c = (1, 1, 3, 1, 1, 1, 1, 1)
```

and realizes `t(3,0,0) = 7`, `t(1,1,1) = 3`, hence `3·49 = 147 > 9·9 = 81`.
The comparison is reported on `B_3(0)` only. Displayed, not adopted.

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
orbit `(1,1)`. The unique three-step body-diagonal path
`0 → (1,0,0) → (1,1,0) → (1,1,1)` uses the orbit sequence
`(0,1)`, `(1,2)`, `(2,3)`. The site `(3,0,0)` has a unique neighbor in the
ball, namely `(2,0,0)`.

### Theorem 2

There are `3^8 = 6561` `G+`-equivariant maps from those orbits to `{1,2,3}`.
Of these, 405 reverse

```text
t(3,0,0)^2 / 9  <=  t(1,1,1)^2 / 3.
```

Equivalently, those 405 assignments violate the integer comparison
`3 t(3,0,0)^2 <= 9 t(1,1,1)^2`. The lex-first reversing filling is
`c = (1, 1, 3, 1, 1, 1, 1, 1)` in the Theorem 1 orbit order: seed-exit cost
`1`, inbound `(1,0)` cost `1`, axis-extension cost `3`, and every remaining
orbit cost `1`. It realizes `t(3,0,0) = 7` and `t(1,1,1) = 3`.

The binary seed-exit bound does not block this alphabet. Every path still
leaves the seed along orbit `(0,1)` of common cost `c0 ∈ {1,2,3}`, but the
three-step axis path now costs `c0 + 2 c_aa` with `c_aa` allowed to be `3`,
so `t(3,0,0)` can reach `7` at `c0 = 1`. Then `3·49 = 147` exceeds
`9·9 = 81`. The identity that blocked every `{1,2}` filling therefore fails
as soon as an axis-extension cost `3` is admitted.

The lex-first witness is forced, not accidental. The unique in-ball neighbor
of `(3,0,0)` is `(2,0,0)`, so every path pays a final `(1,1)` hop. Under the
lex-first filling that hop costs `3`. Every path to `(2,0,0)` has even length
at least `2`. The two-step path costs `1+3 = 4`, and any four-step path to
`(2,0,0)` costs at least `4`, so `t(3,0,0) = 7`. The three-step body-diagonal
path uses only cost-`1` hops, so `t(1,1,1) = 3`.

Unit costs and constant-`3` costs stay diamond: both give
`t(3,0,0) = t(1,1,1)` and `3 t^2 <= 9 t^2`. Reversal is a genuine
two-end effect of making the `(1,1)` orbit expensive while the
`(1,2)` and `(2,3)` turns stay cheap.

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
| exhaust `{1,2,3}` fillings | closed by Theorem 2; 6561 maps, 405 reversals |
| exhibit a reversing filling | closed: lex-first `c = (1, 1, 3, 1, 1, 1, 1, 1)` |
| reuse the binary seed-exit block | refused; that identity fails at `c_aa = 3` |
| write a cost into Admissibility | refused; Theorem 3 |
| attach a path-length law | refused; Theorem 3 |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a cost or of a path-length law is not a proof leaf.

## Representative Values

| filling | `t(3,0,0)` | `t(1,1,1)` | `3 t_axis^2` | `9 t_diag^2` | diamond? |
|---|---:|---:|---:|---:|---|
| every orbit cost `1` | `3` | `3` | `27` | `81` | yes |
| every orbit cost `3` | `9` | `9` | `243` | `729` | yes |
| lex-first reversing `(1,1,3,1,1,1,1,1)` | `7` | `3` | `147` | `81` | no |
| seed-exit `1`, axis-extension `2` (binary leftover) | `≤ 5` | `≥ 3` | `≤ 75` | `≥ 81` | yes |

The table is an exact illustration of Theorem 2, not an adopted dynamics.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply a
numerical hop cost on occupancy pairs. This note therefore treats
`c(σ_v, σ_w) ∈ {1,2,3}` as a displayed probe, not as an axiom clause.

Record is not used. No formation site, formation rate, or readout value is
assigned to an unoccupied site. The seed is a theorem hypothesis for the
one-seed front, not a privileged physical site.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `Z^3` nearest-neighbor adjacency and proper cubic rotations | ambient lattice | live axiom memo |
| one-seed front from `0` | theorem hypothesis | declared; no site is privileged in the axiom |
| `σ_n` as 6-bit inward occupation | occupancy used by the probe | defined from the one-seed front |
| `c(σ_v, σ_w) ∈ {1,2,3}` | displayed `G+`-equivariant hop cost | mathematical input; not an axiom |
| comparison points `(3,0,0)` and `(1,1,1)` | diamond axis/diagonal order on `B_3(0)` | declared test pair |
| binary `{1,2}` two-end census | context, not a load-bearing parent | ternary value `3` is absent there |
| arrival-only one-endpoint quotient | context, not a load-bearing parent | two-end orbits are counted first |

There are no measured, fitted, literature, or observational inputs. A
continuum metric, a path-length axiom, and any cost written into
Admissibility remain outside the result.

## Mutations

1. Collapse pairs to arrival occupancy only: distinct two-end orbits that
   share `|σ_w|` are identified, so the census is no longer two-end.
2. Replace the eight-orbit count by seven or nine: the enumerated
   representatives are exactly the eight inward-weight pairs above.
3. Assert that every triple filling stays diamond: 405 of the 6561 maps
   reverse `3 t(3,0,0)^2 <= 9 t(1,1,1)^2`.
4. Reuse the binary seed-exit identity as a block: that bound assumes
   `c_aa ∈ {1,2}` and fails at `c_aa = 3`.
5. Treat the result as a leftover of the `{1,2}` census: cost `3` is not a
   `{1,2}` value, and the binary maps all stay diamond.
6. Write `c` into Admissibility: the live axiom memo still states one
   fixed covariant nearest-neighbor rule and contains no two-end occupancy
   hop cost.

## What This Does Not Claim

- No cost is written into Admissibility.
- No path-length law is attached.
- The comparison is not scored outside `B_3(0)`.
- The ternary census is not a leftover of the binary `{1,2}` filling.
- Arrival-only one-endpoint costs are not reused as the two-end proof.
- No continuum Minkowski metric is derived.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: on `B_3(0)`, the report that some
`G+`-equivariant two-end occupancy hop cost with values in `{1,2,3}`
reverses the diamond axis/diagonal order is not a leftover of the binary
census, is not an Admissibility clause, and does not attach a path-length
law. It is not a claim that every conceivable edge law reverses, nor that
any hop cost belongs in the axiom.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| reuse the binary seed-exit block | Argue `t(3,0,0) ≤ c0+4` as in `{1,2}`. | Theorem 2: `c_aa = 3` gives `t(3,0,0) = 7` at `c0 = 1`, and `147 > 81`. | **ATTEMPTED** |
| cheap diagonal, expensive axis | Put cost `3` on `(1,1)` and cost `1` on `(1,2)` and `(2,3)`. | Theorem 2: this is the lex-first reversing filling; `t(3,0,0) = 7`, `t(1,1,1) = 3`. | **ATTEMPTED** |
| face-site detour to the axis | Route `(3,0,0)` through a weight-2 site to avoid two `(1,1)` hops. | Every path still ends on the unique in-ball neighbor, so the final hop is `(1,1)`; the 6561-map census still finds 405 reversals. | **ATTEMPTED** |
| reverse-direction and backtracking | Allow inbound orbits `(1,0)`, `(2,1)`, `(3,2)` to cheapen the axis. | Those orbits are included; the lex-first filling sets them all to `1` and still has `t(3,0,0) = 7`. | **ATTEMPTED** |
| arrival-only leftover | Collapse each pair to `σ_w` and reuse a one-endpoint argument. | Theorem 1 counts two-end pairs before any collapse; orbits `(1,1)` and `(1,2)` share no arrival class. | **ATTEMPTED** |
| binary leftover | Read the ternary question as already settled by the 256 `{1,2}` maps. | Cost `3` is absent from that alphabet; 405 ternary maps reverse and no binary map does. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one comparison and one adoption refusal, not a stack of independent
walls. The 6561-map census and the lex-first witness are two certificates of
the same reversal statement.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| 6561-map census / lex-first witness | yes, as an exhaustive count that includes the witness | yes, as an explicit reversing filling | collapse into Theorem 2 |
| reversal statement / adoption refusal | no: a probe can reverse and still be refused as an axiom | no: refusing adoption does not decide the comparison | independent conclusions |

Path-length attachment is not counted as a third wall: Theorem 3 simply
does not attach one.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “one-seed growth from `0`” | explicit theorem hypothesis; the Lattice axiom privileges no site |
| “inward occupation of the one-seed front” | defined from nearer neighbors; not an extra occupancy axiom |
| “`c ∈ {1,2,3}`” | displayed finite probe, not a derived scale |
| “`G+`-equivariant” | covariance under the axiom's proper cubic rotations |
| “reverse the diamond order” | the displayed axis/diagonal inequality on `B_3(0)` only |
| “not a leftover” of the `{1,2}` census | Theorem 2; cost `3` is a new value |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | Admissibility covariance | one fixed covariant nearest-neighbor rule; no hop cost supplied | yes; cost stays displayed |
| `scripts/two_end_occupancy_cost3_minkowski_2026_08_15.py:281` | number of pair orbits | exactly eight `G+` orbits | yes |
| `scripts/two_end_occupancy_cost3_minkowski_2026_08_15.py:309` | size of the ternary family | `3^8 = 6561` maps | yes |
| `scripts/two_end_occupancy_cost3_minkowski_2026_08_15.py:312` | existence of a reversing filling | exactly 405 reversals | yes |
| `scripts/two_end_occupancy_cost3_minkowski_2026_08_15.py:317` | lex-first reversing filling | `(1, 1, 3, 1, 1, 1, 1, 1)` with times `(7, 3)` | yes |
| `scripts/two_end_occupancy_cost3_minkowski_2026_08_15.py:361` | adoption of a cost | note and axiom keep the cost out of Admissibility | yes |

No evidence citation is used to claim a path-length axiom, a continuum
metric, or an Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each directed `B_3(0)` edge | one inward occupancy pair; no other edge family is classified |
| per site | yes: occupancy is the 6-bit inward front at that site | no other occupancy dictionary is used |
| per mode | yes: eight pair-orbits and all 6561 fillings | other value sets and larger balls are untested and unclaimed |
| per block | yes: the two comparison points on `B_3(0)` | the diamond order is the stated inequality only |
| lattice wide | no | no Admissibility cost and no path-length law are adopted |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a two-end occupancy hop cost, and none is
reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed. The
binary `{1,2}` census of the same eight orbits is a strictly smaller
alphabet: it stays diamond and does not decide the ternary question. The
arrival-only (one-endpoint) quotient of the same pairs is a coarser probe
and is not used to close Theorem 2. The remaining physical choice—whether
any hop cost belongs in Admissibility—stays explicit and does not require
an axiom edit.

### N7 — hostile steelman

The strongest objection is that the binary seed-exit identity should still
block every triple, because every path shares the first hop and the
diagonal still needs three steps. The objection correctly identifies the
shared first hop. It fails because the leftover budget is no longer
`{1,2}`: the axis-extension orbit may cost `3`, the three-step axis path
then costs `7` at seed-exit cost `1`, and `147 > 81`. The 6561-map census
is the hostile check of that larger budget, and the lex-first filling is
the explicit witness.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby covariance
language is context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance of the displayed cost; the rule itself is not replaced |
| binary two-end occupancy costs in `{1,2}` | same eight orbits, smaller alphabet | counted as a strictly smaller probe; Theorem 2 is not a leftover of that census |
| arrival-only occupancy costs | one-endpoint quotient of the same front | counted as a strictly coarser probe; Theorem 1 does not collapse pairs |

No earlier mechanism retires the ternary census or the adoption refusal.

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
pairs; exhausts the 6561 `{1,2,3}` fillings; exhibits the lex-first reversing
filling; rejects the mutation families, including the binary leftover; and
verifies that the live axiom memo does not host the displayed cost. Declared
audit inputs are this note and the axiom memo.
