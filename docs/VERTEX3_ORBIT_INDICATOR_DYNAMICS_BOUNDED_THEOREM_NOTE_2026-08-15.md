---
claim_id: vertex3_orbit_indicator_dynamics_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The vertex3-orbit indicator has empty 1-site first wave on the twelve-vertex two-cube with off-patch o=0 and does not fill. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/vertex3_orbit_indicator_dynamics_2026_08_15.py
---

# Vertex3-Orbit Indicator Dynamics On The Two-Cube

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-lock ticks of the displayed vertex3-orbit indicator
on one twelve-site two-cube carrier, from one 1-site seed, with
off-patch occupancy `o = 0`. First wave, halt, and fill. Displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/vertex3_orbit_indicator_dynamics_2026_08_15.py`](../scripts/vertex3_orbit_indicator_dynamics_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Recompute the 24 proper cube rotations on the 64 occupation cells of the
six-ray star. Those rotations partition the cells into ten orbits. The
**vertex3** orbit is the complement-fixed orbit of weight-three cells
that occupy exactly one ray from each opposite pair: the `+++` /
cube-vertex type, together with every image of `+++` under a proper
rotation. The displayed member is the orbit indicator

```text
f_v3(c) = 1  iff  c lies in the vertex3 orbit.
```

It vanishes off that orbit. In particular a weight-1 6-tuple is not in
vertex3.

The two-cube patch has twelve vertices. Off-patch occupancy is `o = 0`.
The seed is the single site `(0,0,0)`. Each tick locks every unlocked
site whose current 6-neighbor occupation word has `f_v3 = 1`.

**Theorem 1.** The 1-site first wave is empty.

**Theorem 2.** Halt is immediate: `T = 0` (already a fixed point), and
the one-tick image is still the seed. Locks are the seed only, so
`|locks| = 1`.

**Theorem 3.** The twelve-vertex patch does not fill.

This is not leftover-char of the static membership of the vertex3
indicator in the three-cut class. That inventory only records that the
indicator is one complement-even, empty-and-full-vanishing assignment.
The present residual is the executable 1-site dynamics.

Displayed contrast only, not an identity table and not an adoption:

- `f_L1` is the unbalanced-axis predicate (`n ≠ 0`). It is not Hamming
  parity `|c|_1 mod 2`. From the same 1-site seed with `o = 0`, L1 has
  a nonempty first wave and fills the patch at horizon 4
  (`T = 4`, `|locks| = 12`).
- Hamming parity has a nonempty first wave: the three axis neighbors
  of the seed (weight-1 words are odd).

`f_v3` disagrees with both on every weight-1 cell. Displayed, not
adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact first-wave, halt, and fill census of the displayed vertex3-orbit indicator on one twelve-site two-cube carrier from a 1-site seed with off-patch o=0."
trace_class: frontier_discovery
target_claim_id: vertex3_orbit_indicator_dynamics
target_blocker_text: "whether the vertex3-orbit indicator has a nonempty 1-site first wave or fills the twelve-site two-cube"
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independent audit of the bounded halt census"
conditional_surface_status: "exact on the supplied two-cube vertex3 indicator and 1-site seed; other members and complexes remain separate"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Inputs And Import Boundary

- **Framework dependency:** live Lattice and Record sentences, quoted without rewrite.
- **Explicit theorem-domain condition:** recomputed ten-orbit partition,
  vertex3 = complement-fixed one-ray-per-axis weight-3 orbit, displayed
  indicator `f_v3`, two-cube patch, off-patch occupancy zero, 1-site
  seed, simultaneous lock of every unlocked ready site.
- **External empirical or literature inputs:** none.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant
> under lattice translations and proper cubic rotations.

> Records form.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone.

Their dependency role is limited to the cubic site set, proper cubic
rotations, lock permanence, and the unreadability of absence. The
occupation orbits, the indicator, the two-cube patch, the seed, and the
tick index are separately supplied. Current Admissibility, read with
Record, does not supply the formation site, probability, or rate.

## Exact Objects

All runner values are exact integers. No float is used.

Index the six rays as

```text
(+e_x, −e_x, +e_y, −e_y, +e_z, −e_z).
```

A cell is a 6-bit occupation word. A proper cube rotation is a signed
permutation of the three axes with determinant `+1`. There are 24 such
maps. They partition the 64 cells into ten orbits. The vertex3 orbit is
the orbit of `+++` (the three positive rays). It has size 8, occupies
exactly one ray from each opposite pair, and is complement-fixed as a
set. The mixed3 orbit (one opposite pair plus one further ray) is a
different complement-fixed weight-3 orbit of size 12.

```text
f_v3(c) = 1  exactly on vertex3.
```

Cubes `A = {0,1} × {0,1} × {0,1}` and `B = {1,2} × {0,1} × {0,1}`.
Patch `V = A ∪ B`, so `|V| = 12`. Occupancy of a site is `1` if the
site is locked and `0` otherwise, including every off-patch neighbor.

At an unlocked site `v` the 6-tuple is the occupation of the six
lattice neighbors. The site is ready iff `f_v3` of that 6-tuple is 1.
One tick replaces the lock set `L` by

```text
L ∪ { v ∈ V \ L : f_v3(c(v; L)) = 1 }.
```

Locked sites stay locked. Seed locks `{(0,0,0)}`. First wave is the
ready set at that seed.

The displayed L1 predicate is

```text
f_L1(c) = 1  iff  c_{+μ} ≠ c_{−μ} for some axis μ
```

(`n ≠ 0`). Hamming parity is `|c|_1 mod 2`. These are different
functions on the 64 cells.

## Exact Target And Proof Obligations

Check that a weight-1 cell is not in vertex3, that the 1-site first
wave is empty, that halt is immediate with locks equal to the seed,
and that `|locks| ≠ 12`.

## Theorems

### Theorem 1 — the 1-site first wave is empty

A weight-1 6-tuple occupies a single ray. Vertex3 consists only of
weight-3 one-ray-per-axis cells. So `f_v3 = 0` on every weight-1 word.

After the seed `(0,0,0)` is locked, the only unlocked on-patch sites
with a nonempty 6-tuple are the three axis neighbors
`(1,0,0)`, `(0,1,0)`, and `(0,0,1)`. Each sees exactly one occupied
neighbor (the seed) and five blanks, including off-patch blanks at
`o = 0`. Those words are weight 1, hence not vertex3. Every other
on-patch site sees the empty word. The first wave is empty.

### Theorem 2 — halt is immediate

The seed lock set is already a fixed point: the first wave is empty,
so one attempted tick adds nothing. Halt may be read as `T = 0`
(already halted) or as `T = 1` with the same lock set. In either
reading,

```text
locks = {(0,0,0)},   |locks| = 1.
```

The site set is finite, locks are permanent, and a non-halt tick would
have to add a site. None is added.

### Theorem 3 — the patch does not fill

`|locks| = 1 ≠ 12`, so the lock set is not the patch. The
vertex3-orbit indicator does not fill the twelve-vertex two-cube from
this 1-site seed.

Displayed contrast, not a clone table: L1 from the same seed fills at
horizon 4 with 12 locks. Hamming parity from the same seed has a
nonempty first wave (the three axis sites). Those are different
members. Do not call Hamming `f_L1`. Do not adopt `f_v3`.

## What Is Not Claimed

- No unique member of the axiom class, and no adoption of `f_v3`.
- No leftover-char restatement of static `F_cut` membership.
- No identification of `f_v3` with `f_L1` or with Hamming parity.
- `f_L1` remains the unbalanced-axis predicate `n ≠ 0`.
- No clock identity, no source identity, and no formation-count table.
- No 4x4x4, torus, or line complex.
- No axiom edit and no replacement of the live Record sentences.
- Qubit remains `M_2(C)`.
- No inverse-square law and no Newtonian identification.

## Runner Contract

The companion runner recomputes the ten orbits, rebuilds `f_v3` as the
vertex3 indicator, and checks the first-wave, halt, and fill theorems
with exact integer arithmetic. It prints `TOTAL: PASS=... FAIL=...`
and writes no cache. Declared review inputs are this note and the
axiom memo only.
