---
claim_id: blank_block_one_site_fill_count_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Under blank-block, every cube-covariant f has N_fill=0 from a 1-site seed on the twelve-vertex two-cube. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/blank_block_one_site_fill_count_2026_08_15.py
---

# No Cube-Covariant Occupancy Predicate Fills From One Site Under Blank-Block

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** halt census of every cube-covariant occupancy predicate on one
twelve-vertex two-cube, from one locked site, with blank-block readiness
(off-patch neighbors are not occupancy `0`). Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/blank_block_one_site_fill_count_2026_08_15.py`](../scripts/blank_block_one_site_fill_count_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

No runner cache is written.

## Result Up Front

A cube-covariant occupancy predicate is a `{0,1}`-valued function of the
six nearest-neighbor occupancy letters that is constant on the ten proper
cubic rotation orbits of `{0,1}^6`. There are `2^{10} = 1024` such maps,
including the `512` maps with `f(empty) = 0`.

The displayed two-cube has twelve vertices. The seed lock is `(0,0,0)`.
Blank-block says: if any of the six lattice neighbors of a site `v` is
off-patch, then `v` is never ready. Ready sites, if any, lock in
simultaneous ticks. Halt is the first fixed point.

Every on-patch site has at least one off-patch neighbor. After the seed,
no unlocked on-patch site is ready, for any `f`. The first wave is empty
for every cube-covariant `f`. The lock set stays `{ (0,0,0) }`. Therefore

```text
N_fill = |{ f : |locks_halt| = 12 }| = 0.
```

Vacuum occupancy `o = 0` on off-patch neighbors is required to fill this
patch from a 1-site seed. It is not supplied by Record unreadability.
Displayed L1 is the unbalanced-axis map `n ≠ 0` (some axis has
`o_{+μ} ≠ o_{-μ}`). It is never Hamming `|c|_1 mod 2`. Under blank-block
even that L1 map has empty first wave and seed-only halt.

This is a halt census, not a first-wave emptiness statement alone.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact N_fill=0 halt census of every cube-covariant occupancy predicate on one twelve-vertex two-cube under blank-block from a 1-site seed."
trace_class: negative_route_pruning
target_claim_id: blank_block_one_site_fill_count
target_blocker_text: "whether any cube-covariant f fills the twelve-vertex two-cube from a 1-site seed when off-patch neighbors stay blank"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "independent audit of the blank-block one-site fill count"
conditional_surface_status: "exact on the supplied two-cube, 1-site seed, and cube-covariant class under blank-block; o=0 members and other complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Lattice and Record sentences, quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-vertex two-cube, the
  1-site seed `(0,0,0)`, the 1024 cube-covariant occupancy predicates, and
  blank-block readiness.
- **External empirical or literature inputs:** none.

Approved primitives (scale reference, kinetic isotropy, realized state) are
not used and are not walls.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> Records form.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

Their dependency role is limited to the cubic site set, lock permanence, and
the unreadability of absence. Unreadability does not assign occupancy `0`
to an unread or off-patch neighbor. The occupancy predicates, the two-cube
patch, the seed, blank-block, and the tick index are separately supplied.

## Exact Objects

All runner values are exact integers. No float is used.

Cubes `A = {0,1} × {0,1} × {0,1}` and `B = {1,2} × {0,1} × {0,1}`.
Patch `V = A ∪ B`, so `|V| = 12`. The six directed neighbor slots are

```text
(+e_x, −e_x, +e_y, −e_y, +e_z, −e_z).
```

A site is on-patch when it lies in `V`, otherwise off-patch. Occupancy of
an on-patch site is `1` if the site is locked and `0` if it is unlocked.
Off-patch neighbors carry the letter `blank`, not occupancy `0`.

The proper cubic rotation group has 24 elements and acts by permuting the
six slots. The 64 binary 6-tuples split into exactly 10 orbits, with
sizes `[1, 1, 3, 3, 6, 6, 8, 12, 12, 12]`. A cube-covariant occupancy
predicate `f` assigns `{0,1}` to each orbit. There are 1024 such maps.
The empty orbit is the all-zero 6-tuple. The 512 maps with `f(empty) = 0`
are the rawfill subclass; this census includes all 1024.

Displayed L1 is the orbit-constant map

```text
f_L1(c) = 1  iff  some axis μ has c_{+μ} ≠ c_{-μ}.
```

Equivalently `n ≠ 0`, where `n_μ` is the axis occupancy difference. This
is the unbalanced-axis predicate. It is never Hamming `|c|_1 mod 2`. The
two maps disagree on the adjacent-pair orbit (Hamming even, some axis
unbalanced).

**Blank-block:** the 6-tuple at `v` is defined only when every lattice
neighbor of `v` is on-patch. Otherwise `v` is not ready and `f` is not
evaluated. A tick locks every unlocked ready site at once. Halt is the
first fixed point, reached in at most 12 ticks because locks are
permanent on a 12-site set.

`N_fill` is the number of cube-covariant `f` whose halt lock set equals
`V`.

## Exact Target And Proof Obligations

Enumerate the 24 rotations, the 10 orbits, and the 1024 maps. For each
map, run blank-block ticks from the seed and record the first wave and
the halt lock set. Report `N_fill` and the empty-first-wave count.
Separate L1 from Hamming. Contrast the same L1 map with off-patch `o = 0`
only as a discriminator, not as an adopted law.

## Theorems

### Theorem 1 — first wave empty for every cube-covariant `f`

After the seed, no unlocked on-patch site is ready. Every site of `V`
has `y ∈ {0,1}` and `z ∈ {0,1}`, so every site has an off-patch
`±e_y` or `±e_z` neighbor. The six-tuple at every unlocked site is
undefined. The first wave is empty for every `f`, including every map
with `f(empty) = 0` and including displayed L1.

### Theorem 2 — halt is seed-only; `N_fill = 0`

A tick with empty ready set does not add a lock. The lock set remains
`{ (0,0,0) }` at the first tick and at every later tick. Halt is
seed-only for every cube-covariant `f`. No halt lock set equals `V`, so
`N_fill = 0`. The same count on the 512 maps with `f(empty) = 0` is also
`0`.

The object is the halt census. Empty first wave is the mechanism; seed-only
halt is the fill count.

### Theorem 3 — no cube-covariant fill without the `o = 0` default

Therefore no cube-covariant occupancy predicate fills this patch from a
1-site seed without the off-patch `o = 0` default. The vacuum letter is
required to fill, not only to have a first wave.

The paired runner also reconstructs displayed L1 under off-patch `o = 0`
as a discriminator: that member then has a nonempty first wave and fills
all twelve vertices. Blank-block is what sets `N_fill = 0`. Hamming
`|c|_1 mod 2` is a different cube-covariant map and is not L1.

## No-Go Discipline Gate

The negative result is only `N_fill = 0` under blank-block for
cube-covariant `f` on this two-cube from this 1-site seed. It is not a
universal bar on formation.

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| fill off-patch neighbors as occupancy `0` and rerun the same 1024 maps | **ATTEMPTED** | that is a different encoding; displayed L1 then has a nonempty first wave and fills the patch |
| evaluate `f` on the on-patch letters only, ignoring blank slots | **ATTEMPTED** | that replaces blank-block by a partial 6-tuple; the census does not use it |
| start from a multi-site seed whose locked set already closes a six-star | **ATTEMPTED** | the seed here is one site; a larger seed is a different object |
| move the same maps onto a larger patch whose six-neighbor stars close | **ATTEMPTED** | the two-cube is held fixed; every site of `V` has an off-patch neighbor |
| drop cube covariance and allow site-labeled rules | **ATTEMPTED** | outside the 1024-map class named in the claim |
| treat Record unreadability as occupancy `0` | **ATTEMPTED** | the axiom withholds a readout; it does not write the letter `0` |
| use Hamming `|c|_1 mod 2` as if it were L1 | **ATTEMPTED** | Hamming is a different orbit map; under blank-block it is also never evaluated |

### N2 — wall independence

One type wall is claimed: on this two-cube, blank-block plus a 1-site seed
leaves no ready site, so every cube-covariant halt is seed-only. No second
impossibility wall is asserted.

### N3 — hidden-wall scan

The two-cube, the seed, the 24 rotations, the 10 orbits, the 1024 maps,
blank-block, and the halt rule are declared. No leftover-character
identity, no adopted L1, no vacuum axiom, and no axiom edit is imported.

### N4 — residual matching

The residual after this note is still a physical formation rule—site,
process, and rate—plus any lawful encoding of neighbors that are not on a
declared finite patch. A first-wave emptiness statement for one subclass
is a different object from this halt census. An `o = 0` fill census is a
different encoding. Those residuals are not substituted for `N_fill = 0`.

### N5 — certificate granularity

```text
per-element: executed — each of the 1024 cube-covariant maps is enumerated
per-site: executed — readiness is tested at every unlocked on-patch site
per-mode: executed — L1 is the unbalanced-axis map, never Hamming |c|_1 mod 2
per-block: executed — only the supplied two-cube, seed, and blank-block are checked
lattice-wide: not executed — no full Z^3 history or adopted formation law is claimed
```

### N6 — partial-closure paths

A later kernel could fill off-patch neighbors as `0`, define readiness
from on-patch letters only, start from more than one seed, or work on a
patch whose six-neighbor stars close. Those are named extra encodings or
different complexes. None of them is an axiom edit, and none is supplied
by an approved primitive.

### N7 — steelman

The strongest objection is that after later locks some unlocked site
might acquire a fully defined 6-tuple, so a map with `f(empty) = 1` or
`f(wt1) = 1` could still fire and fill. Correct that blank-block is a
per-tick test, not only a first-wave test. Incorrect on this two-cube:
every site of `V` has a lattice neighbor outside `V` at every tick, so
the 6-tuple never becomes defined. The halt census, not only the first
wave, stays seed-only.

### N8 — cross-cycle echo

A prior first-wave comparison on the same two-cube already separated
blank from occupancy `0` for displayed L1. This note keeps that letter
split and changes the object to the halt fill count over the whole
cube-covariant class. Retiring the L1-only first-wave residual does not
retire `N_fill = 0`.

## What Is Not Claimed

- No unique member of the axiom class, and no adoption of L1 or of any `f`.
- L1 is displayed as the unbalanced-axis map `n ≠ 0`. It is never Hamming
  `|c|_1 mod 2`.
- This is a halt census, not a first-wave statement alone, and not a
  leftover-character identity.
- Independent of any `o = 0` fill census: that encoding is a different
  object. The `o = 0` L1 reconstruction here is a discriminator only.
- No 4x4x4, torus, or line complex.
- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No inverse-square law and no Newtonian identification.
- No axiom, primitive, registry, citation manifest, runner cache, or audit
  verdict is edited.

## Runner Contract

The companion runner reconstructs the 24 rotations, the 10 orbits, the
1024 maps, and blank-block ticks on the displayed patch. It computes
`N_fill` by counting halt lock sets of size 12. It prints
`TOTAL: PASS=... FAIL=...` and writes no cache. Declared review inputs
are this note and the axiom memo only.
