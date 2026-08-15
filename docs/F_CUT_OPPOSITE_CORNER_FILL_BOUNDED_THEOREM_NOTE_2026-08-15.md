---
claim_id: f_cut_opposite_corner_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 cube-covariant complement-even predicates that vanish on empty and full, N_cutopp fill the two-cube from the opposite-corner 2-site seed with off-patch o=0. f_L1 is not unique in that set. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_opposite_corner_fill_2026_08_15.py
---

# Opposite-Corner `F_cut` Fill Count

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact fill census of the 32 cube-covariant complement-even
empty-and-full-silent occupancy predicates on the twelve-vertex two-cube,
from the opposite-corner seed `S*={(0,0,0),(2,1,1)}` with off-patch occupancy
`o=0`. Displayed, not adopted. No Admissibility rewrite and no unique-filler
claim.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_opposite_corner_fill_2026_08_15.py`](../scripts/f_cut_opposite_corner_fill_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the twelve-vertex two-cube

```text
PATCH = {0,1,2} × {0,1} × {0,1}.
```

Off-patch occupancy is the displayed default `o=0`. A site is locked when the
displayed occupancy predicate returns `1` on its six nearest-neighbor occupancy
cell. Fill means the halt lock set has size `12`. The seed is the opposite-corner
pair

```text
S* = {(0,0,0), (2,1,1)}.
```

The class `F_cut` is the set of cube-covariant maps `f:{0,1}^6 → {0,1}` with
`f(empty)=f(full)=0` and `f(c)=f(1-c)` for every cell. Complement pairing of
the ten directed-axis orbits leaves five free bits

```text
(wt1, opp2, adj2, vertex3, mixed3),
```

so `|F_cut|=32`. The map `f_L1` is the `n≠0` predicate: it returns `1` exactly
when at least one axis is unbalanced. Its remaining-bit tuple is
`(1, 0, 1, 1, 1)`. This is not Hamming parity.

**Theorem 1.** `f_L1 ∈ F_cut` and `f_L1` fills from `S*` with lock history
`(2, 8, 12)`.

**Theorem 2.** `N_cutopp = |{f ∈ F_cut : fills from S*}| = 4`.

**Theorem 3.** `N_cutopp > 1`, so `f_L1` is not unique among those four.
Another filler has remaining-bit tuple `(1, 0, 1, 1, 0)` and the same history
`(2, 8, 12)`. The four displayed tuples are

```text
(1, 0, 1, 1, 0), (1, 0, 1, 1, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

Displayed, not adopted. Do not write the four maps into Admissibility.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite census of the 32 F_cut maps from one displayed opposite-corner seed. The four fillers are displayed occupancy predicates, not an adopted Admissibility rule."
trace_class: negative_route_pruning
target_claim_id: f_cut_opposite_corner_fill
target_blocker_text: "how many of the 32 F_cut maps fill from the opposite-corner 2-site seed, and is f_L1 unique among them"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the seed-by-class count; any physical use must separately derive an Admissibility selector"
conditional_surface_status: "exact for the twelve-site two-cube, o=0, and S*; other seeds and maps outside F_cut remain separately counted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** Count how many of the 32 cube-covariant complement-even
predicates that vanish on empty and full fill the two-cube from `S*` with
`o=0`, and state whether `f_L1` is unique in that set.

| Obligation | Disposition |
|---|---|
| two-cube, `S*`, and `o=0` | fixed as displayed hypotheses; Theorem 1 |
| `|F_cut|=32` from five remaining orbit bits | proved here with the ten-orbit census |
| `f_L1 ∈ F_cut` and history `(2,8,12)` | proved here in Theorem 1 |
| `N_cutopp` | proved here in Theorem 2 as the exact count `4` |
| uniqueness or a displayed rival tuple | proved here in Theorem 3: not unique; `(1,0,1,1,0)` |
| no Admissibility adoption | explicit refusal; no axiom edit |

Boundary cases are not hidden. The same 32 maps give eight 1-site fillers and
four face-diagonal 2-site fillers; those are different seeds. The support-26
`n_both=0` rival fills from a 1-site seed and does not fill from `S*`. Hamming
parity sits in `F_cut` and reaches nine locks from a 1-site seed. No terminal
lemma equivalent to the `S*` count is left open.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  cubic lattice, nearest-neighbor adjacency, proper cubic covariance of the
  one fixed admissibility rule, and the Record lock sentence. As the registered
  `minimal_axioms` premise, it is not a bounded-status source.
- The two-cube, the seed `S*`, the default `o=0`, and the occupancy-lock tick
  are displayed mathematical hypotheses, not framework-derived physical
  selectors.
- `f_L1` is the displayed `n≠0` predicate on a six-slot cell. It is not
  Hamming weight and not Hamming parity.
- No measured, fitted, observational, literature, or scale value is used.

## Exact Objects

A cell is a six-tuple of occupancies of the directed nearest neighbors of a
site. An axis is unbalanced when its two ends differ, both-occupied when both
ends are `1`, and empty when both ends are `0`. The ten orbits are the level
sets of `(n_unbalanced, n_both, n_empty)`:

```text
empty    = (0,0,3)     full     = (0,3,0)
wt1      = (1,0,2)     wt5      = (1,2,0)
opp2     = (0,1,2)     opp2c    = (0,2,1)
adj2     = (2,0,1)     adj2c    = (2,1,0)
vertex3  = (3,0,0)     mixed3   = (1,1,1)
```

Complement-even maps identify `wt1` with `wt5`, `opp2` with `opp2c`, and
`adj2` with `adj2c`. The orbits `vertex3` and `mixed3` are self-complementary.
Setting `f(empty)=f(full)=0` leaves the five free bits above.

Occupancy of a locked on-patch site is `1`. Occupancy of an unlocked on-patch
site, and of every off-patch neighbor, is `0`. Each tick locks every presently
unlocked on-patch site whose cell evaluates to `1`, simultaneously.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

## Theorem 1 — `f_L1` fills from `S*`

The `n≠0` rule assigns `1` on every orbit with `n_unbalanced≥1` and `0`
otherwise. That assignment is constant on the ten orbits, vanishes on empty
and full, and is complement-even, so it is the `F_cut` tuple `(1, 0, 1, 1, 1)`.
It differs from Hamming parity `(1, 0, 0, 1, 1)` on `adj2`.

Start with `S*` locked. The first wave locks the six remaining sites at
`ℓ¹` distance `1` from exactly one seed point, producing eight locks. The
second wave locks the last four sites. Halt is a fixed point with twelve
locks. The lock-count history is therefore `(2, 8, 12)`.

## Theorem 2 — the count `N_cutopp`

There are exactly `2^5=32` remaining-bit tuples. The companion runner evaluates
the occupancy tick from `S*` on each of them. Exactly four reach a halt lock
set of size `12`. Hence `N_cutopp=4`.

The same enumeration recovers the already-displayed contrasts on other seeds:
eight of the 32 fill from the 1-site seed `{(0,0,0)}`, and four fill from the
face-diagonal seed `{(0,0,0),(1,1,0)}`. Those counts are different
seed-by-class objects. They are not this theorem.

## Theorem 3 — `f_L1` is not unique

The four `S*` fillers are the tuples listed in the result. One of them is
`f_L1`. Another is `(1, 0, 1, 1, 0)`, which also has history `(2, 8, 12)`.
Therefore `N_cutopp>1`. The four maps are displayed rivals. None is written
into Admissibility, and none is proposed as an axiom or approved primitive.

## Mutations

1. Replace the count target `N_cutopp=4` by `1`: the exhaustive 32-map run
   still returns `4`.
2. Identify `f_L1` with Hamming parity: the tuples differ on `adj2`, and
   Hamming parity reaches nine locks from a 1-site seed.
3. Claim that every `F_cut` map fills from `S*`: twenty-eight maps halt
   strictly below twelve locks.
4. Adopt the four fillers as the Admissibility rule: the note states the
   opposite refusal; the axiom memo is not edited.

## What This Does Not Claim

- No unique-filler theorem for `F_cut` on this seed.
- No Admissibility rewrite and no approved-primitive registration.
- No identification of occupancy locks with Record locks of `M_2(C)`
  possibilities.
- No `Z^3`-wide law, formation rate, or source identity.
- No Hamming reading of `f_L1`.
- The 1-site count of eight and the face-diagonal count of four are other
  seeds, not this residual.

## No-Go Discipline Gate

The negative claim is only the uniqueness failure: `f_L1` is not the only
`F_cut` map that fills from `S*`. It is not a claim that occupancy predicates
cannot fill, and it is not a claim that Admissibility is empty.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| unique-`f_L1` route | Test whether only `(1,0,1,1,1)` fills from `S*`. | Theorem 3 and runner check `thm3-not-unique` display three other tuples. | **ATTEMPTED** |
| Hamming identification | Replace `n≠0` by Hamming parity on the same cells. | Theorem 1 and check `thm1-fl1-not-hamming` separate the tuples on `adj2`. | **ATTEMPTED** |
| leftover 1-site count | Import the eight 1-site fillers as this census. | Theorem 2 and check `seed-contrast-one-and-face` recompute eight on a different seed. | **ATTEMPTED** |
| leftover face-diagonal count | Import the four face-diagonal fillers as this census. | Same check: that four is a different seed, even though the integer matches. | **ATTEMPTED** |
| support-26 rival | Ask whether the `n_both=0` 1-site filler also fills from `S*`. | Check `fmin-does-not-fill-sstar` halts at ten locks. | **ATTEMPTED** |
| static `F_cut` cut only | Treat the 32-map list as already answering uniqueness. | Theorem 2 requires the occupancy tick; twenty-eight of the 32 do not fill. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one conclusion: the `S*` fill set inside `F_cut` has size four, so
`f_L1` is not unique there. The Hamming contrast and the other-seed counts
are certificates that this object is not a leftover character of those
earlier lists; they collapse into the same seed-by-class residual rather
than counting as independent walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `N_cutopp=4` / not unique | yes, once `f_L1` is among the four | yes | one conclusion |
| Hamming contrast / uniqueness failure | no: a tuple mismatch does not count fillers | no: a four-element set does not identify Hamming | supporting contrast |
| 1-site eight / `S*` four | no: different seed | no | different object |

Other seeds and maps outside `F_cut` are not counted as walls.

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| twelve-vertex two-cube and `o=0` | explicit displayed hypotheses |
| seed `S*={(0,0,0),(2,1,1)}` | explicit displayed hypothesis |
| occupancy equals the lock set | explicit tick rule, not a Record identity |
| cube-covariant complement-even class | the definition of `F_cut` used here |
| `f_L1` is `n≠0` | explicit; Hamming is excluded |
| “Displayed, not adopted” | adoption refusal, not a hidden selector |
| Record lock sentence | cited only as the ambient lock vocabulary; occupancy locks stay displayed |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and nearest-neighbor adjacency | sites are `Z^3` with nearest-neighbor adjacency | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:56` | covariance of the one admissibility rule | proper-cubic covariance is ambient; no rule is selected | yes; selector stays open |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | meaning of a lock | Record locks one admissible possibility when present | yes; occupancy locks stay displayed |
| `scripts/f_cut_opposite_corner_fill_2026_08_15.py:293` | `f_L1 ∈ F_cut` | the tuple is `(1,0,1,1,1)` | yes |
| `scripts/f_cut_opposite_corner_fill_2026_08_15.py:315` | `S*` history of `f_L1` | exact history `(2,8,12)` | yes |
| `scripts/f_cut_opposite_corner_fill_2026_08_15.py:320` | the count `N_cutopp` | exact integer `4` | yes |
| `scripts/f_cut_opposite_corner_fill_2026_08_15.py:325` | uniqueness inside that set | `N_cutopp>1` | yes |

No evidence citation is used to claim that Admissibility has been rewritten,
that a physical selector has been derived, or that a `Z^3`-wide law has been
closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each of the 32 `F_cut` maps | each is run from `S*`; maps outside `F_cut` are unclaimed |
| per site | yes: the twelve two-cube sites | lock counts are on this patch only |
| per mode | yes: one predicate class and one seed | other seeds are contrasts, not this residual |
| per block | yes: the `S*` fill subset of `F_cut` | uniqueness fails because that subset has size four |
| lattice wide | no | no `Z^3`-wide occupancy law is asserted |

The runner cache carries the same five resolution statements verbatim in its
execution certificate.

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
No approved primitive supplies an occupancy predicate, a two-cube fill rule,
or an opposite-corner seed. None is reclassified as an import or wall.

A partial-closure mechanism is on the table and is not suppressed: the same
four remaining-bit tuples also fill from the face-diagonal 2-site seed. That
coincidence of integers does not identify the two seeds, and it does not
select one of the four tuples. The remaining physical choice — whether any of
these maps is the actual Admissibility rule — stays explicit and does not
require an axiom edit to state honestly.

### N7 — hostile steelman

The strongest objection is that the four `S*` fillers are exactly the four
face-diagonal fillers, so the new seed has not produced a new class: one
could have copied the earlier four-tuple list. That objection correctly notes
the set equality of those two filler lists. To overturn the present theorem
it would still have to show that the `S*` dynamics were not run, or that
`N_cutopp` is not a seed-indexed count. The runner evaluates `S*` directly
and reports history `(2,8,12)` rather than the face-diagonal history. The
object is the seed-by-class pair `(S*, F_cut)`, not the unnamed four-element
set of tuples.

### N8 — cross-cycle echo

No landed two-cube `F_cut` note sits on `origin/main` as a load-bearing
parent. Nearby ambient structure is the axiom memo's nearest-neighbor cubic
covariance, which licenses treating cube-covariant maps as the displayed
class and does not select a member. Earlier investment numbers that counted
1-site or face-diagonal fillers are context, not files cited as dependencies.
Their algebra is recomputed here on those seeds only as a contrast.

No earlier mechanism retires the uniqueness failure on `S*`.

No-Go Discipline disposition: **PASS** for the uniqueness-failure boundary
stated at the start of this section.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

## Runner Contract

The companion runner rebuilds the ten directed-axis orbits, confirms twenty-four
proper cube rotations preserve orbit names, enumerates the 32 `F_cut` maps,
runs the occupancy tick from `S*`, records `N_cutopp=4` and the four remaining-
bit tuples, checks that `f_L1` is the `n≠0` member with history `(2, 8, 12)`,
displays `(1, 0, 1, 1, 0)` as a second filler, rejects the unique-filler
mutation, and verifies the displayed-not-adopted axiom boundary. Declared
audit inputs are this note and the axiom memo.
