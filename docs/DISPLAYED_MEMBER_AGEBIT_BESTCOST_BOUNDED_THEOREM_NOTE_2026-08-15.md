---
claim_id: displayed_member_agebit_bestcost_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "One displayed member pairing the leftover-frame pair section with the B_3 variance-minimizing hop cost is scored on both our-physics hosts. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/displayed_member_agebit_bestcost_2026_08_15.py
---

# Displayed Member: Age-Bit Pair Section Plus Best Hop Cost (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one displayed member `M = (f, c)` scored on two finite hosts
only: the uneqrad lex-first breaker (same host as bitfire) and the
radius-3 ball `B_3(0)`. Displayed, not adopted. Uniqueness of `M` is
not claimed. Finite hosts only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/displayed_member_agebit_bestcost_2026_08_15.py`](../scripts/displayed_member_agebit_bestcost_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Owner close condition is a member that yields our universe, not a
unique leftover. Live extras: (i) occupancy plus one older/newer bit on
the full axis plus leftover-frame-positive section fires a July-3 pair
(bitsec / bitfire / bitall); (ii) hop cost `10→c=(3,1,3,1,1,3,1,1)`
reverses diamond and beats ell^1 on `B_3` (minkbest). New residual:
treat those two as one displayed member and check both our-physics
probes on their hosts. Not leftover of either probe alone. Do not
attach L1. Uniqueness not required.

Member `M = (f, c)` pairs the leftover-frame-positive pair section `f`
with the hop cost `c`. Here `f` is the bitsec section: the unique
July-3 pair completion of each age-bit encoding whose ordered triple of
directions (leftover `+`, leftover `−`, full-axis `+`) has determinant
`+1`. The cost is

```text
c = (3, 1, 3, 1, 1, 3, 1, 1)
```

on the eight inward-occupancy-pair orbits of `B_3(0)`, in the order

```text
(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2).
```

**Theorem 1.** On the uneqrad lex-first breaker, `f` still fires
`N_new = 1` (one unread site becomes occupied). Same host as bitfire.

**Theorem 2.** On `B_3(0)`, `c` still realizes `t(3,0,0) = 9`,
`t(1,1,1) = 5`, so diamond reverses, and
`var(|v|_2/t) = 0.00017588571746` `<` ell^1 `0.02073945514155`.

**Theorem 3.** Displayed, not adopted. Neither extra is written into
Admissibility. Uniqueness of `M` is not claimed. Do not attach L1.

`claim_scope`: One displayed member pairing the leftover-frame pair
section with the B_3 variance-minimizing hop cost is scored on both
our-physics hosts. Displayed, not adopted.

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

Admissibility names neither the leftover-frame-positive section nor any
two-end occupancy hop cost as the framework's fixed rule. Neither extra
is written into Admissibility. Record permanence is used only to keep
the locks on `U`. Formation site and rate remain outside the axiom
memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite pairing of leftover-frame-positive f on the uneqrad star with the B_3 hop cost c; both our-physics probes are scored on their hosts. Displayed report only."
trace_class: frontier_discovery
target_claim_id: displayed_member_agebit_bestcost
target_blocker_text: "treat the July-3 leftover-frame pair section and the B_3 variance-minimizing hop cost as one displayed member"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of M=(f,c) on both hosts; do not write either extra into Admissibility or attach L1"
conditional_surface_status: "exact on two finite hosts; f fires N_new=1 on the uneqrad breaker; c realizes t(3,0,0)=9, t(1,1,1)=5 and var=0.00017588571746 < ell^1; displayed, not adopted; uniqueness of M is not claimed"
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

### Hop-cost host (`B_3(0)`)

Let `B_3(0)` be the set of sites of `Z^3` reachable from the origin by
at most three nearest-neighbor steps. One-seed growth starts at `0`.
The occupancy `σ_n` at a site `n` is the 6-bit string whose
direction-`d` bit is set exactly when the neighbor of `n` in direction
`d` is strictly nearer the seed. `G+` is the 24-element group of
proper cubic rotations about the seed. A hop cost
`c(σ_v, σ_w) ∈ {1,2,3}` on a directed nearest-neighbor edge `v → w` is
`G+`-equivariant when it is constant on `G+` orbits of endpoint pairs.
Arrival time `t(n)` is the minimum path cost from `0` to `n` through
`B_3(0)`. The eight `G+` orbits of inward occupancy pairs, in the
order used by `c`, are the inward-weight pairs
`(0,1), (1,0), (1,1), (1,2), (2,1), (2,2), (2,3), (3,2)`.

A filling reverses the diamond axis/diagonal order when
`3 t(3,0,0)^2 > 9 t(1,1,1)^2`. On the 62 sites of `B_3(0) \ {0}`,
write `r(v) = |v|_2 / t(v)` and let `var` be the population variance

```text
var(r) = (1/62) sum_v (r(v) - mean(r))^2.
```

The ell^1 filling `t(v) = |v|_1` has `var = 0.02073945514155`.

## Theorem 1 — `f` still fires on the uneqrad host

The unique full axis of `σ` is `z`. The bit `b = 1` writes `+` on `+z`
and `−` on `−z`. The two completions are

`(+, 0, −, 0, +, −)` and `(−, 0, +, 0, +, −)`.

The first has leftover `+` on `+x`, leftover `−` on `+y`, and
full-axis `+` on `+z`. That ordered triple of directions has
determinant `+1`. Therefore

`f(σ,b) = (+, 0, −, 0, +, −)`.

This 6-tuple lies in the 48-member July-3 pair. The center `v` is
unread. The displayed pair step therefore forms exactly `v`
(`N_new = 1`) and does not remove any lock of `U`. So `U` persists.
One unread site becomes occupied. Same host as bitfire.

## Theorem 2 — `c` still reverses diamond and beats ell^1

On `B_3(0)` the displayed filling

```text
c = (3, 1, 3, 1, 1, 3, 1, 1)
```

realizes `t(3,0,0) = 9` and `t(1,1,1) = 5`. Then
`3·81 = 243 > 9·25 = 225`, so diamond reverses. Its population
variance of `|v|_2/t` on the 62 nonzero sites is
`0.00017588571746`, strictly below the ell^1 baseline
`0.02073945514155`.

The axis path `0 → (1,0,0) → (2,0,0) → (3,0,0)` costs `3+3+3 = 9`.
The body-diagonal path `0 → (1,0,0) → (1,1,0) → (1,1,1)` costs
`3+1+1 = 5`. The six `G+` site-types arrive at

```text
t(1,0,0) = 3,  t(2,0,0) = 6,  t(1,1,0) = 4,
t(3,0,0) = 9,  t(2,1,0) = 7,  t(1,1,1) = 5.
```

This is the same `B_3` host as minkbest. The pairing does not re-open
the 405-map census; it asks whether this already-named `c` still
realizes those two times and that variance comparison.

## Theorem 3 — Displayed, not adopted

The pair `M = (f, c)` is displayed member data. Neither extra is
written into Admissibility. Do not write f into Admissibility. Do not
write that `c` into Admissibility. Uniqueness of `M` is not claimed.
Uniqueness not required. Do not attach L1. No path-length law is
attached. Occupancy-only formation is not attached. Qubit remains
`M_2(C)`. No approved primitive is added. No axiom edit.

This residual is not leftover of either probe alone: bitfire reports
fire of `f` on one host, and minkbest reports the variance-minimizing
`c` on `B_3(0)`. The present claim is the pairing of those two extras
as one displayed member scored on both our-physics hosts.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first breaker, leftover-frame-
  positive `f(σ,b) = (+, 0, −, 0, +, −)` fires with `N_new = 1` and
  `U` persists. On `B_3(0)`, `c = (3, 1, 3, 1, 1, 3, 1, 1)` realizes
  `t(3,0,0) = 9`, `t(1,1,1) = 5`, diamond reverses, and
  `var(|v|_2/t) = 0.00017588571746 < 0.02073945514155`.
- **What is displayed only.** The member `M = (f, c)` is one rival
  table. It is not adopted.
- **What is not claimed.** Uniqueness of `M` is not claimed. Neither
  extra is written into Admissibility. L1 is not attached. No path-
  length law. No leftover of either probe alone. No axiom edit. No
  formation rate. No compiler no-go.
- **Mutation controls.** A rebuilt `f` other than `(+, 0, −, 0, +, −)`
  fails. A rebuilt `N_new ≠ 1` fails. A rebuilt
  `(t(3,0,0), t(1,1,1))` other than `(9, 5)` fails. A variance that
  does not beat ell^1 fails. A note that writes either extra into
  Admissibility, attaches L1, claims uniqueness of `M`, or authors an
  audit verdict fails.

This note authors no audit verdict.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name the uneqrad lex-first breaker and rebuild `f` | closed by Theorem 1; same host as bitfire |
| report `N_new` on that star | closed by Theorem 1; `N_new = 1` |
| name the eight inward-occupancy-pair orbits on `B_3(0)` | closed by the `G+` action on directed edges |
| evaluate `c = (3, 1, 3, 1, 1, 3, 1, 1)` | closed by Theorem 2; `t(3,0,0) = 9`, `t(1,1,1) = 5` |
| compare `var(|v|_2/t)` to ell^1 | closed by Theorem 2 |
| treat fire of `f` alone as the member | refused; not leftover of either probe alone |
| treat the hop-cost census alone as the member | refused; not leftover of either probe alone |
| write either extra into Admissibility | refused; Theorem 3 |
| attach L1 or a path-length law | refused; Theorem 3 |
| claim uniqueness of `M` | refused; uniqueness not required |

The obligation graph is acyclic. Every leaf of the bounded pairing is
closed. Adoption of `f` or of `c` is not a proof leaf.

## Representative Values

| host | displayed extra | report |
|---|---|---|
| uneqrad breaker, `v = (−3,−3,−1)` | leftover-frame-positive `f` | `f = (+, 0, −, 0, +, −)`, `N_new = 1`, `U` persists |
| `B_3(0)` | hop cost `c = (3, 1, 3, 1, 1, 3, 1, 1)` | `t(3,0,0) = 9`, `t(1,1,1) = 5`, `var = 0.00017588571746` `<` ell^1 `0.02073945514155` |

The table is an exact illustration of Theorems 1 and 2, not an adopted
dynamics.

## Framework Boundary

Admissibility supplies one fixed nearest-neighbor rule, covariant under
lattice translations and proper cubic rotations, and says that the local
distribution varies with nearest-neighbor conditions. It does not supply
a leftover-frame section and it does not supply a numerical hop cost on
occupancy pairs. This note therefore treats `M = (f, c)` as a displayed
probe, not as an axiom clause.

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
| one-seed front from `0` on `B_3(0)` | hop-cost host | same host as minkbest; rebuilt here |
| `c = (3, 1, 3, 1, 1, 3, 1, 1)` | second coordinate of `M` | displayed `G+`-equivariant hop cost |
| pairing `M = (f, c)` | displayed member | not leftover of either probe alone |
| uniqueness of `M` | not claimed | uniqueness not required |

There are no measured, fitted, literature, or observational inputs. A
path-length axiom and any extra written into Admissibility remain
outside the result.

## Mutations

1. Score only the fire of `f`: that is bitfire, not the pairing.
2. Score only the hop-cost census: that is minkbest, not the pairing.
3. Attach L1 as a path-length law because ell^1 is the baseline:
   Theorem 3 does not attach L1.
4. Write `f` or `c` into Admissibility: the live axiom memo still
   states one fixed covariant nearest-neighbor rule.
5. Claim that `M` is the unique leftover that yields our universe:
   uniqueness of `M` is not claimed.

## What This Does Not Claim

- Neither extra is written into Admissibility.
- Do not attach L1.
- Uniqueness of `M` is not claimed.
- The pairing is not leftover of either probe alone.
- The comparison is not scored outside the two finite hosts.
- No path-length law is attached.
- No privileged physical seed is added to the Lattice axiom.
- No Record readout is assigned to a site without a record.

## No-Go Discipline Gate

The negative claim is only this: pairing the leftover-frame-positive
section with the `B_3` variance-minimizing hop cost as one displayed
member, scored on both our-physics hosts, is not leftover of either
probe alone, is not an Admissibility clause, does not attach L1, and
does not claim uniqueness of `M`. It is not a claim that `M` belongs
in the axiom.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| fire leftover | Argue that bitfire already names the member. | Theorem 3: fire of `f` is one coordinate; the pairing is not leftover of either probe alone. | **ATTEMPTED** |
| cost leftover | Argue that minkbest already names the member. | Theorem 3: `c` is one coordinate; the pairing is not leftover of either probe alone. | **ATTEMPTED** |
| attach L1 | Read the ell^1 baseline as a path-length law. | Theorem 3: Do not attach L1. | **ATTEMPTED** |
| uniqueness | Treat `M` as the unique leftover. | Theorem 3: Uniqueness of `M` is not claimed. | **ATTEMPTED** |
| adopt `f` | Write the section into Admissibility. | Theorem 3 and the live axiom memo. | **ATTEMPTED** |
| adopt `c` | Write the hop cost into Admissibility. | Theorem 3 and the live axiom memo. | **ATTEMPTED** |

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
| “one-seed growth from `0`” | explicit theorem hypothesis |
| “`c = (3, 1, 3, 1, 1, 3, 1, 1)`” | displayed finite probe |
| “`G+`-equivariant” | covariance under the axiom's proper cubic rotations |
| “diamond reverses” | the displayed axis/diagonal inequality on `B_3(0)` |
| “population variance on 62 sites” | the finite list `B_3(0) \ {0}` |
| “not leftover of either probe alone” | Theorems 1–3 |
| “Displayed, not adopted” | Theorem 3; no Admissibility edit |
| “Uniqueness of `M` is not claimed” | Theorem 3 |

### N4 — citation-to-residual matching

| Evidence path | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | ambient lattice and proper cubic rotations | `Z^3` nearest-neighbor graph and `G+` | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | Admissibility covariance | one fixed covariant nearest-neighbor rule; neither extra supplied | yes |
| runner Theorem 1 | fire of `f` on the uneqrad host | `N_new = 1`, `U` persists | yes |
| runner Theorem 2 | hop cost on `B_3(0)` | `t(3,0,0) = 9`, `t(1,1,1) = 5`, variance digits | yes |
| runner Theorem 3 | adoption, L1, uniqueness | displayed, not adopted | yes |

No evidence citation is used to claim a path-length axiom or an
Admissibility rewrite.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: the star at `v` and each directed `B_3(0)` edge | no other star or edge family is classified |
| per site | yes: unread center `v` and the 62 nonzero ball sites | no other occupancy dictionary is used |
| per mode | yes: one section value and one hop-cost 8-tuple | other sections and other fillings are unclaimed |
| per block | yes: fire report plus population variance | closeness is the stated variance only |
| lattice wide | no | neither extra is written into Admissibility |

The runner prints the same five resolution statements.

### N6 — partial closure and primitive scan

The only dependency used is the registered `minimal_axioms` node. No
approved primitive supplies a leftover-frame section or a two-end
occupancy hop cost, and none is reclassified as an import or wall.

Two partial-closure mechanisms are recorded rather than suppressed.
Fire of `f` on one host is a strictly weaker statement: it does not
pair a hop cost. The hop-cost census on `B_3(0)` is a strictly weaker
statement: it does not pair the age-bit section. The remaining
physical choice—whether any such member belongs in Admissibility—
stays explicit and does not require an axiom edit.

### N7 — hostile steelman

The strongest objection is that the owner close condition already
names a unique leftover, so pairing `f` with `c` is either redundant
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
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | proper cubic covariance of the nearest-neighbor rule | used as `G+` equivariance; the rule itself is not replaced |
| leftover-frame-positive fire | same `f` on the uneqrad star | rebuilt as the first coordinate of `M` |
| `B_3` variance-minimizing hop cost | same `c` on `B_3(0)` | rebuilt as the second coordinate of `M` |

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
leftover-frame-positive section `f(σ,b)`, and the fire report
(`N_new = 1`, `U` persists). It rebuilds the eight inward-occupancy-
pair orbits on `B_3(0)`, evaluates `c = (3, 1, 3, 1, 1, 3, 1, 1)`,
and reports `t(3,0,0) = 9`, `t(1,1,1) = 5`, diamond reversal, and
`var(|v|_2/t)` against ell^1. It rejects leftover-of-either-probe,
uniqueness, L1 attachment, and Admissibility rewrite. Declared audit
inputs are this note and the axiom memo. Finite hosts only. No cache
is written. No axiom edit.
