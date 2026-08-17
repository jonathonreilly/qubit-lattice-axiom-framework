---
claim_id: displayed_member_agebit_support_drop_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "One displayed member pairing the leftover-frame pair section with the support-drop hop-cost is scored on both our-physics hosts. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/displayed_member_agebit_support_drop_2026_08_15.py
---

# Displayed Member: Age-Bit Pair Section Plus Support-Drop Hop-Cost (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one displayed member `M = (f, ν)` scored on two finite hosts
only: the uneqrad lex-first breaker (same host as bitfire) and the
radius-6 ball `B_6(0)`. Displayed, not adopted. Uniqueness of `M` is
not claimed. Finite hosts only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/displayed_member_agebit_support_drop_2026_08_15.py`](../scripts/displayed_member_agebit_support_drop_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Owner close is a member that yields our universe. Live extras:
leftover-frame pair section (chirality) and support-drop hop-cost `ν`
(reverse diamond). New residual: treat those two as one displayed
member and check both probes. Not leftover of either alone. Uniqueness
not required. Do not attach L1.

Member `M = (f, ν)` pairs the leftover-frame-positive section `f` with
the support-drop hop-cost `ν`. Here `f` is the bitsec section: the
unique July-3 pair completion of each age-bit encoding whose ordered
triple of directions (leftover `+`, leftover `−`, full-axis `+`) has
determinant `+1`. Write `|σ_x|` for inward occupancy weight at a site
`x` relative to the host seed or seeds. On a directed nearest-neighbor
hop `x → y`,

```text
ν(x→y) = 3 if |σ_x|=0 or (|σ_x|=|σ_y|=1) or |σ_y| < |σ_x|,
else 1.
```

The first clause is seed-exit. The second is both weights `1`. The
third is support drop. Those three clauses are the whole rule.

**Theorem 1.** On the uneqrad lex-first breaker, `f` still fires
`N_new = 1` with `ν` as unused labels.

**Theorem 2.** On `B_6(0)`, `ν` still realizes `t(4,0,0) = 10`,
`t(2,2,2) = 8`, so diamond reverses, and `var < ℓ¹`.

**Theorem 3.** Displayed, not adopted. Uniqueness of `M` is not claimed.
Do not write `f` or `ν` into Admissibility. Do not attach L1.

`claim_scope`: One displayed member pairing the leftover-frame pair
section with the support-drop hop-cost is scored on both our-physics
hosts. Displayed, not adopted.

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

Admissibility names neither the leftover-frame-positive section nor the
support-drop hop-cost as the framework's fixed rule. Do not write `f`
or `ν` into Admissibility. Record permanence is used only to keep the
locks on `U`. Formation site and rate remain outside the axiom memo.
Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite pairing of leftover-frame-positive f on the uneqrad star with the support-drop hop-cost ν; both our-physics probes are scored on their hosts. Displayed report only."
trace_class: frontier_discovery
target_claim_id: displayed_member_agebit_support_drop
target_blocker_text: "treat the leftover-frame pair section and the support-drop hop-cost as one displayed member"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of M=(f,ν) on both hosts; do not write either extra into Admissibility or attach L1"
conditional_surface_status: "exact on two finite hosts; f fires N_new=1 with ν as unused labels on the uneqrad breaker; ν realizes t(4,0,0)=10, t(2,2,2)=8 and var=0.00590563902870 < ell^1; displayed, not adopted; uniqueness of M is not claimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

### Age-bit host (same host as bitfire)

Write `s1 = (−2,−2,−2)`, `s2 = (−2,−2,−1)`, and `s3 = (−2,−2,1)`. The
closed ℓ¹ ball of radius `r` is

`B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`.

The locked set is the already-given unequal-radius union

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`.

The three balls have 25, 7, and 63 sites. Pairwise overlaps are 7, 7,
and 7, and the triple overlap has 7 sites, so `|U| = 81`. The unread
site is

`v = (−3,−3,−1)`.

Then `‖v − s1‖_1 = 3 > 2`, `‖v − s2‖_1 = 2 > 1`, and
`‖v − s3‖_1 = 4 > 3`, so `v ∉ U`. Direction order is
`(+x, −x, +y, −y, +z, −z)`. Occupancy mask at `v`:

`σ = (1, 0, 1, 0, 1, 1)`.

Occupied nearest neighbors receive the lock tick
`t(w) = min_i ‖w − si‖_1`. Empty slots have no tick. Local data is
`(σ, t)` with

`t = (1, ·, 1, ·, 3, 2)`.

The unique full axis is `z`. The age bit is
`b = [t(−z) < t(+z)]`. On this star `t(−z) = 2` and `t(+z) = 3`, so
`b = 1`. Letters are `{0, +, −}`. The July-3 `k = 3` pair is the unique
pair of proper-cube orbits of 3-letter 6-tuples that are not
proper-equivalent to their inversion images. That set has 48 members.
Completions of `(σ,b)` are the two pair members that match occupancy
`σ` and write opposite letters on the full axis according to `b`. The
leftover-frame sign of a completion is the determinant of the ordered
triple of directions (leftover `+`, leftover `−`, full-axis `+`
letter). The section `f` takes the unique completion of sign `+1`. A
displayed pair step at an unread site forms that site if and only if
the encoded 6-tuple lies in the pair; existing locks are not removed.

Inward occupancy at a site `x` uses the same seed-distance already
used for lock-ticks, `d(x) = min_i ‖x − si‖_1`, with a direction bit
set exactly when the neighbor is strictly nearer the nearest seed.
Inward weight is the number of such bits. On this host,
`|σ_v| = 2`. Incoming `ν` labels on the four occupied neighbors, in
direction order `(+x, +y, +z, −z)`, are

`incoming_ν = (1, 1, 3, 1)`.

The cost-3 label is the support-drop hop from `+z` (`|σ| = 4`) into
`v` (`|σ| = 2`). Those integers are unused labels: they are recorded
on the incoming edges and they do not restrict fire. Fire still uses
the full occupancy `σ`, not the cost-1 restriction of `σ`.

### Hop-cost host (`B_6(0)`)

Let `B_6(0)` be the set of sites of `Z^3` with `|v|_1 ≤ 6`. That ball
has 377 sites and 376 nonzero sites. One-seed growth starts at `0`.
Inward occupancy at a site `n` is the 6-bit string whose direction-`d`
bit is set exactly when the neighbor of `n` in direction `d` is
strictly nearer the seed. Inward weight equals the number of nonzero
coordinates. Arrival time `t(n)` is the minimum path cost from `0` to
`n` through `B_6(0)` under `ν`. Unit-cost ℓ¹ arrival is the closed
form `t_ℓ¹(v) = |v|_1`; it is not obtained from a second Dijkstra.

A filling reverses the diamond axis/diagonal order when
`12 t(4,0,0)^2 > 16 t(2,2,2)^2`. On the 376 sites of `B_6(0) \ {0}`,
write `r(v) = |v|_2 / t(v)` and let `var` be the population variance

```text
var(r) = (1/376) sum_v (r(v) - mean(r))^2.
```

The ℓ¹ filling has `var = 0.01350203761919`.

## Theorem 1 — `f` still fires with `ν` as unused labels

The unique full axis of `σ` is `z`. The bit `b = 1` writes `+` on `+z`
and `−` on `−z`. The two completions are

`(+, 0, −, 0, +, −)` and `(−, 0, +, 0, +, −)`.

The first has leftover `+` on `+x`, leftover `−` on `+y`, and
full-axis `+` on `+z`. That ordered triple of directions has
determinant `+1`. Therefore

`f(σ,b) = (+, 0, −, 0, +, −)`.

This 6-tuple lies in the 48-member July-3 pair. The center `v` is
unread. Incoming `ν` labels `(1, 1, 3, 1)` are unused: they do not
drop the cost-3 `+z` slot from occupancy. The displayed pair step
therefore forms exactly `v` (`N_new = 1`) and does not remove any lock
of `U`. So `U` persists. One unread site becomes occupied. Same host as bitfire.

If those labels were instead a cost-1 readiness filter, the restricted
mask would be `(1, 0, 1, 0, 0, 1)`, which has no unique full axis, so
the pair section would not fire. Unused labels are load-bearing for
`N_new = 1`.

## Theorem 2 — `ν` still reverses diamond and beats ℓ¹

On `B_6(0)` one origin Dijkstra under `ν` realizes `t(4,0,0) = 10` and
`t(2,2,2) = 8`. Then `12·100 = 1200 > 16·64 = 1024`, so diamond
reverses. Its population variance of `|v|_2/t` on the 376 nonzero
sites is `0.00590563902870`, strictly below the ℓ¹ baseline
`0.01350203761919`. So `var < ℓ¹`.

The pairing does not re-open the hop-cost census; it asks whether this
already-named `ν` still realizes those two times and that variance
comparison on the same `B_6(0)` host.

## Theorem 3 — Displayed, not adopted

The pair `M = (f, ν)` is displayed member data. Do not write `f` or `ν`
into Admissibility. Uniqueness of `M` is not claimed. Uniqueness not required. Do not attach L1. No path-length law is attached.
Occupancy-only formation is not attached. Qubit remains `M_2(C)`. No
approved primitive is added. No axiom edit.

This residual is not leftover of either probe alone: bitfire reports
fire of `f` on one host, and the support-drop hop-cost reports diamond
reverse plus variance on `B_6(0)`. The present claim is the pairing of
those two extras as one displayed member scored on both our-physics
hosts.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first breaker, leftover-frame-
  positive `f(σ,b) = (+, 0, −, 0, +, −)` fires with `N_new = 1` and
  `U` persists when `ν` is unused labels. On `B_6(0)`, `ν` realizes
  `t(4,0,0) = 10`, `t(2,2,2) = 8`, diamond reverses, and
  `var(|v|_2/t) = 0.00590563902870 < 0.01350203761919`.
- **What is displayed only.** The member `M = (f, ν)` is one rival
  table. It is not adopted.
- **What is not claimed.** Uniqueness of `M` is not claimed. Do not
  write `f` or `ν` into Admissibility. L1 is not attached. No path-
  length law. No leftover of either probe alone. No axiom edit. No
  formation rate. No compiler no-go.
- **Mutation controls.** A rebuilt `f` other than `(+, 0, −, 0, +, −)`
  fails. A rebuilt `N_new ≠ 1` fails. Using `ν` as a cost-1 filter
  instead of unused labels fails. A rebuilt
  `(t(4,0,0), t(2,2,2))` other than `(10, 8)` fails. A variance that
  does not beat ℓ¹ fails. A note that writes either extra into
  Admissibility, attaches L1, claims uniqueness of `M`, or authors an
  audit verdict fails.

This note authors no audit verdict.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name the uneqrad lex-first breaker and rebuild `f` | closed by Theorem 1; same host as bitfire |
| report `N_new` with `ν` as unused labels | closed by Theorem 1; `N_new = 1` |
| name the support-drop clauses of `ν` | closed by the three-clause rule |
| evaluate `ν` on `B_6(0)` | closed by Theorem 2; `t(4,0,0) = 10`, `t(2,2,2) = 8` |
| compare `var(|v|_2/t)` to ℓ¹ | closed by Theorem 2 |
| treat fire of `f` alone as the member | refused; not leftover of either probe alone |
| treat the hop-cost census alone as the member | refused; not leftover of either probe alone |
| write `f` or `ν` into Admissibility | refused; Theorem 3 |
| attach L1 or a path-length law | refused; Theorem 3 |
| claim uniqueness of `M` | refused; uniqueness not required |

The obligation graph is acyclic. Every leaf of the bounded pairing is
closed. Adoption of `f` or of `ν` is not a proof leaf.

## Representative Values

| host | displayed extra | report |
|---|---|---|
| uneqrad breaker, `v = (−3,−3,−1)` | leftover-frame-positive `f` with unused `ν` labels | `f = (+, 0, −, 0, +, −)`, `incoming_ν = (1, 1, 3, 1)`, `N_new = 1`, `U` persists |
| `B_6(0)` | support-drop hop-cost `ν` | `t(4,0,0) = 10`, `t(2,2,2) = 8`, `var = 0.00590563902870` `<` ℓ¹ `0.01350203761919` |

The table is an exact illustration of Theorems 1 and 2, not an adopted
dynamics.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply
a leftover-frame section and it does not supply a numerical hop cost on
inward-occupancy pairs. This note therefore treats `M = (f, ν)` as a
displayed probe, not as an axiom clause.

Record permanence is used only to keep the locks on `U`. No formation
site, formation rate, or readout value is assigned to an unoccupied
site. The seed at the origin is a theorem hypothesis for the one-seed
front, not a privileged physical site.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| `Z^3` nearest-neighbor adjacency and proper cubic rotations | ambient lattice | live axiom memo |
| uneqrad lex-first breaker `(U, v, σ, t)` | age-bit host | same host as bitfire; rebuilt here |
| leftover-frame-positive section `f` | first coordinate of `M` | bitsec section; determinant `+1` |
| one-seed front from `0` on `B_6(0)` | hop-cost host | same host as the support-drop census; rebuilt here |
| support-drop hop-cost `ν` | second coordinate of `M` | displayed three-clause hop cost |
| pairing `M = (f, ν)` | displayed member | not leftover of either probe alone |
| uniqueness of `M` | not claimed | uniqueness not required |

There are no measured, fitted, literature, or observational inputs. A
path-length axiom and any extra written into Admissibility remain
outside the result.

## Mutations

1. Score only the fire of `f`: that is bitfire, not the pairing.
2. Score only the hop-cost census: that is the support-drop `B_6`
   score, not the pairing.
3. Attach L1 as a path-length law because ℓ¹ is the baseline:
   Theorem 3 does not attach L1.
4. Write `f` or `ν` into Admissibility: the live axiom memo still
   states one fixed covariant nearest-neighbor rule.
5. Claim that `M` is the unique leftover that yields our universe:
   uniqueness of `M` is not claimed.
6. Treat incoming `ν` as a cost-1 readiness filter: Theorem 1 uses
   unused labels.

## What This Does Not Claim

- Do not write `f` or `ν` into Admissibility.
- Do not attach L1.
- Uniqueness of `M` is not claimed.
- The pairing is not leftover of either probe alone.
- The comparison is not scored outside the two finite hosts.
- No path-length law is attached.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: pairing the leftover-frame-positive
section with the support-drop hop-cost as one displayed member, scored
on both our-physics hosts, is not leftover of either probe alone, is
not an Admissibility clause, does not attach L1, and does not claim
uniqueness of `M`. It is not a claim that `M` belongs in the axiom.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| fire leftover | Argue that bitfire already names the member. | Theorem 3: fire of `f` is one coordinate; the pairing is not leftover of either probe alone. | **ATTEMPTED** |
| cost leftover | Argue that the support-drop census already names the member. | Theorem 3: `ν` is one coordinate; the pairing is not leftover of either probe alone. | **ATTEMPTED** |
| attach L1 | Read the ℓ¹ baseline as a path-length law. | Theorem 3: Do not attach L1. | **ATTEMPTED** |
| uniqueness | Treat `M` as the unique leftover. | Theorem 3: Uniqueness of `M` is not claimed. | **ATTEMPTED** |
| adopt `f` | Write the section into Admissibility. | Theorem 3 and the live axiom memo. | **ATTEMPTED** |
| adopt `ν` | Write the hop cost into Admissibility. | Theorem 3 and the live axiom memo. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one pairing and one adoption refusal, not a stack of
independent walls. The two host scores are two certificates of the
same displayed member.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| fire report / hop-cost report | no: each host is independent | no | two certificates of `M` |
| pairing statement / adoption refusal | no: a probe can score on both hosts and still be refused as an axiom | no | independent conclusions |

Attaching L1 is not counted as a third wall: Theorem 3 simply does not
attach L1.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “uneqrad lex-first breaker” | explicit finite host; same host as bitfire |
| “leftover-frame-positive section” | bitsec section; determinant `+1` |
| “ν as unused labels” | incoming hop costs recorded, not used as a readiness filter |
| “one-seed growth from `0`” | explicit theorem hypothesis |
| “support-drop hop-cost `ν`” | displayed finite probe |
| “diamond reverses” | the displayed axis/diagonal inequality on `B_6(0)` |
| “population variance on 376 sites” | the finite list `B_6(0) \ {0}` |
| “not leftover of either probe alone” | Theorems 1–3 |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |
| “Uniqueness of `M` is not claimed” | Theorem 3 |

### N4 — citation-to-residual matching

| Evidence path | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | Admissibility covariance | one fixed covariant nearest-neighbor rule; neither extra supplied | yes |
| runner Theorem 1 | fire of `f` with unused `ν` labels | `N_new = 1`, `U` persists | yes |
| runner Theorem 2 | hop cost on `B_6(0)` | `t(4,0,0) = 10`, `t(2,2,2) = 8`, variance digits | yes |
| runner Theorem 3 | adoption, L1, uniqueness | displayed, not adopted | yes |

No evidence citation is used to claim a path-length axiom or an
Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: the star at `v` and each directed `B_6(0)` edge | no other star or edge family is classified |
| per site | yes: unread center `v` and the 376 nonzero ball sites | no other occupancy dictionary is used |
| per mode | yes: one section value and one three-clause hop cost | other sections and other fillings are unclaimed |
| per block | yes: unused-label fire report plus population variance | closeness is the stated variance only |
| lattice wide | no | neither extra is written into Admissibility |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a leftover-frame section or a support-drop
hop cost, and none is reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed.
Fire of `f` on one host is a strictly weaker statement: it does not
pair a hop cost. The hop-cost census on `B_6(0)` is a strictly weaker
statement: it does not pair the age-bit section. The remaining
physical choice—whether any such member belongs in Admissibility—
stays explicit and does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that the owner close condition already
names a unique leftover, so pairing `f` with `ν` is either redundant
or a uniqueness claim. The objection correctly identifies that each
extra was already scored on its own host. It fails because the
residual asked for one displayed member scored on both our-physics
hosts, and Theorem 3 refuses uniqueness. The pairing is not leftover
of either probe alone.

### N8 — cross-cycle echo

The live axiom memo is the only load-bearing parent. Nearby fire and
hop-cost surfaces are context.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as host covariance; the rule itself is not replaced |
| leftover-frame-positive fire | same `f` on the uneqrad star | rebuilt as the first coordinate of `M` |
| support-drop hop-cost on `B_6(0)` | same `ν` on `B_6(0)` | rebuilt as the second coordinate of `M` |

No earlier mechanism retires the pairing or the adoption refusal.

No-Go Discipline disposition: **PASS** for the bounded pairing and the
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

The companion runner rebuilds the uneqrad lex-first breaker, the
leftover-frame-positive section `f(σ,b)`, incoming `ν` as unused
labels, and the fire report (`N_new = 1`, `U` persists). It rebuilds
`B_6(0)`, evaluates the three-clause support-drop hop-cost `ν`, and
reports `t(4,0,0) = 10`, `t(2,2,2) = 8`, diamond reversal, and
`var(|v|_2/t)` against ℓ¹. It rejects leftover-of-either-probe,
uniqueness, L1 attachment, and Admissibility rewrite. Declared audit
inputs are this note and the axiom memo. Finite hosts only. No cache
is written. No axiom edit.
