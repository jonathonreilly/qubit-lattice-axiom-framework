---
claim_id: f_two_face_diagonal_seed_fill_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "f_two from the face-diagonal 2-site seed {(0,0,0),(1,1,0)} on the twelve-vertex two-cube with off-patch o=0 reaches a fixed point with reported (T, |locks|)=(1, 4). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_two_face_diagonal_seed_fill_2026_08_15.py
---

# `f_two` From A Face-Diagonal Two-Site Seed Halts Without Filling

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-lock ticks of one displayed predicate `f_two`
on the twelve-vertex two-cube from one displayed face-diagonal two-site
seed. The halt pair and fill boolean are computed, not fitted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_two_face_diagonal_seed_fill_2026_08_15.py`](../scripts/f_two_face_diagonal_seed_fill_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the two-cube whose cubes are `A = {0,1}^3` and
`B = {1,2} × {0,1}^2`. The union has twelve vertices. Off-patch occupancy
is the displayed default `o=0`. A locked site stays locked. An unread
on-patch site evaluates the six nearest-neighbor occupancies

```text
c = (c_{+x}, c_{-x}, c_{+y}, c_{-y}, c_{+z}, c_{-z}).
```

An axis `μ` is unbalanced when `c_{+μ} ≠ c_{-μ}`. Write `u` for the number
of unbalanced axes. The displayed member is

```text
f_two(c) = 1  iff  u ≥ 2.
```

This is not `f_L1`. The unbalanced-axis predicate `f_L1` is `n ≠ 0`,
equivalently `u ≥ 1`, with `n_μ = (c_{+μ} − c_{-μ})/3`. It is never
Hamming parity `|c|_1 mod 2`. f_two is u≥2, not f_L1.

The seed is the displayed face-diagonal pair from the two-site family

```text
S0 = {(0,0,0), (1,1,0)}.
```

One simultaneous tick locks every unlocked ready site. The first wave is
exactly `{(1,0,0), (0,1,0)}`. After that tick the locked set is the
`z=0` face of cube `A`,

```text
locks_1 = {(0,0,0), (1,0,0), (0,1,0), (1,1,0)},
```

and no unread site is ready. The process therefore reaches a fixed point
at halt tick `T=1` with `|locks_T|=4`. The twelve-vertex patch does not
fill.

The displayed three-site contrast (axis triple
`{(1,0,0),(0,1,0),(0,0,1)}`) recomputes as `T=2`, eight locks, no fill.
Those integers are a displayed comparison only. They are not a parent,
not an identity, and not this residual: the halt pair here is `(1, 4)`,
not `(2, 8)`.

Displayed, not adopted. The axioms do not select `f_two`, the seed, or
the off-patch default. Occupancy is a displayed extra bit, not Record
content at an unread site.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite occupancy ticks on a twelve-vertex patch produce a unique halt pair (T, |locks|)=(1, 4) and a false fill boolean. The predicate, seed, and off-patch default are displayed extra structure, not a derived formation law."
trace_class: negative_route_pruning
target_claim_id: f_two_face_diagonal_seed_fill
target_blocker_text: "does the minimal working f_two seed fill the two-cube"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed halt pair; any physical use must separately derive a formation predicate and seed law"
conditional_surface_status: "exact for this seed, this patch, off-patch o=0, and f_two as u>=2; other seeds, other predicates, and Z^3-wide dynamics remain unclaimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Proof Obligations

**Exact target.** On the twelve-vertex two-cube with off-patch `o=0`,
start from `S0={(0,0,0),(1,1,0)}` and lock unread sites with `f_two(c)=1`.
Prove that the first wave is nonempty, that the process reaches a fixed
point in at most twelve ticks, and report the exact pair
`(T, |locks|)=(1, 4)` together with the fill boolean `|locks_T|=12`,
which is false.

| Obligation | Disposition |
|---|---|
| first wave nonempty, and equal to the two face-adjacent sites | proved here in Theorem 1 |
| halt in at most twelve ticks | proved here in Theorem 2 |
| exact halt pair `(T, |locks_T|)` | proved here in Theorem 2: `(1, 4)` |
| fill boolean | proved here in Theorem 3: false |
| contrast with the displayed three-site numbers | recomputed in Theorem 3 as displayed integers only |
| `f_two` is not `f_L1` and not Hamming | checked on the first-wave six-tuple |

Boundary cases stay named. A one-site seed has empty first wave under
`f_two`. Hamming parity on the same first-wave six-tuple is `0` while
`f_two` is `1`. `f_L1` from this seed has a strictly larger first wave.
Other two-site pairs, other off-patch defaults, and any `Z^3`-wide law
are outside the target.

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the cubic lattice, nearest-neighbor adjacency, the existence of one
  covariant nearest-neighbor admissibility rule, and Record permanence
  and unreadability. As the registered `minimal_axioms` premise, it is
  not a bounded-status source.
- The axioms do not supply a formation site, formation probability, or
  formation rate. They do not select occupancy as a locked possibility
  and do not name `f_two`.
- The twelve-vertex two-cube, the default `o=0`, the seed `S0`, and the
  predicate `u ≥ 2` are displayed mathematical hypotheses.
- No measured, fitted, observational, or phenomenological value is used.
- Approved primitives (`scale_reference_primitive`,
  `kinetic_isotropy_primitive`, `realized_state_primitive`) are unused.

## Exact Objects

Vertices:

```text
V = {0,1,2} × {0,1} × {0,1}.
```

Cube `A` is `x ∈ {0,1}`; cube `B` is `x ∈ {1,2}`. They share the face
`x=1`. Occupancy of a neighbor not in `V` is `0`. Locked sites contribute
`1`; unread on-patch sites contribute `0` to their neighbors.

The companion runner evaluates six-tuples in the order above and counts
unbalanced axes by comparing each pair `(c_{+μ}, c_{-μ})`.

## Theorem 1 — first wave nonempty

Treat both seed sites as already locked. The unread site `(1,0,0)` sees

```text
c(1,0,0) = (0,1, 1,0, 0,0):
  −x neighbor (0,0,0) occupied, +x neighbor (2,0,0) empty,
  +y neighbor (1,1,0) occupied, −y neighbor off-patch empty,
  ±z empty.
```

So the `x` and `y` axes are unbalanced and `u=2`. The unread site
`(0,1,0)` sees

```text
c(0,1,0) = (1,0, 0,1, 0,0):
  +x neighbor (1,1,0) occupied, −x neighbor off-patch empty,
  −y neighbor (0,0,0) occupied, +y neighbor off-patch empty,
  ±z empty.
```

Again `u=2`. Every other unread vertex has `u ≤ 1`. Therefore the first
wave is nonempty and equals `{(1,0,0),(0,1,0)}`: each sees two occupied
nearest neighbors on different axes.

## Theorem 2 — halt in at most twelve ticks

There are twelve sites, locks are permanent, and a tick adds a subset of
the remaining unread sites. The chain of lock-sets is strictly increasing
until it stabilizes, so a fixed point occurs in at most twelve ticks.

Direct evaluation after the first tick gives

```text
locks_1 = {(0,0,0), (1,0,0), (0,1,0), (1,1,0)}.
```

Each remaining unread site now has `u ≤ 1`:

- `(0,0,1)`, `(0,1,1)`, `(1,0,1)`, `(1,1,1)` each see only the occupied
  `−z` neighbor on the locked face;
- `(2,0,0)` and `(2,1,0)` each see only the occupied `−x` neighbor on
  the shared face;
- `(2,0,1)` and `(2,1,1)` see the empty six-tuple.

No unread site is ready, so the configuration is already a fixed point.
Hence `T=1` and `|locks_T|=4`. The empty occupancy is separately a fixed
point (`u=0` at every site).

## Theorem 3 — the patch does not fill

Fill means `|locks_T|=12`. Here `|locks_T|=4`, so the boolean is false.

The displayed three-site axis seed `{(1,0,0),(0,1,0),(0,0,1)}` is a
different initial condition. Recomputing the same ticks on that seed
gives first wave `{(0,0,0),(1,1,0),(1,0,1),(0,1,1)}`, then one further
lock `(1,1,1)`, then halt: `T=2`, eight locks, no fill. Those numbers
are displayed only. This note's residual is the face-diagonal halt pair
`(1, 4)`, not leftover character of that three-site census.

## Mutations

1. Replace `f_two` by `f_L1` (`u ≥ 1`): the first wave from `S0` is
   strictly larger than `{(1,0,0),(0,1,0)}`.
2. Replace `f_two` by Hamming `|c|_1 mod 2`: the first-wave six-tuple
   at `(1,0,0)` has weight `2`, so Hamming is `0` while `f_two` is `1`.
3. Replace the fill target `|locks_T|=12` by the computed `4`: the
   equality `4=12` fails.
4. Identify this residual with the displayed three-site pair `(2, 8)`:
   `(1, 4) ≠ (2, 8)`.
5. Drop off-patch `o=0`: the first-wave counts above use those empty
   off-patch slots; the displayed default is part of the hypothesis.

## What This Does Not Claim

- No derived formation-site, formation-rate, or update law.
- No adoption of `f_two`, of `o=0`, or of the two-cube as a physical
  domain.
- No claim that every two-site seed, or every face-diagonal pair, fills
  or fails to fill.
- No `Z^3`-wide dynamics, clock identity, source identity, or PVM.
- No Hamming-as-`f_L1` identification.
- Seed content is an initial condition, not a privileged Lattice site.

## No-Go Discipline Gate

The negative claim is only this: on the displayed twelve-vertex two-cube
with off-patch `o=0`, `f_two` from `S0={(0,0,0),(1,1,0)}` reaches a
fixed point with `|locks_T| ≠ 12`. It is not a claim that `f_two` never
fills any patch, or that occupancy formation is impossible.

### N1 — materially distinct routes

| Route | Exact attack | Result and authority | Marker |
|---|---|---|---|
| direct first-wave evaluation | Compute `u` at every unread vertex from `S0`. | Theorem 1: exactly two sites have `u=2`. | **ATTEMPTED** |
| bounded tick chain | Locks are permanent on a twelve-site set. | Theorem 2: halt in at most twelve ticks; here `T=1`. | **ATTEMPTED** |
| second-wave re-evaluation | Recompute `u` after locking the first wave. | Theorem 2: every unread site has `u≤1`. | **ATTEMPTED** |
| fill-count comparison | Test `|locks_T|=12`. | Theorem 3: `|locks_T|=4`. | **ATTEMPTED** |
| `f_L1` substitution | Run `u≥1` from the same seed. | First wave strictly larger; not this member. | **ATTEMPTED** |
| Hamming substitution | Evaluate `|c|_1 mod 2` on the first-wave cell. | Weight `2` is even, so Hamming disagrees with `f_two`. | **ATTEMPTED** |

### N2 — wall independence and collapse

There is one negative: this seed does not fill this patch. The halt-tick
bound, the second-wave vanishing, and the count `|locks_T|=4` are three
certificates of that one finite-CA fact; they collapse rather than count
as independent walls.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| empty second wave / `|locks|≠12` | yes, once the locked set is known to have size 4 | no: a non-filling halt at a later tick could also have size ≠12 | one residual, two readings |
| halt bound / explicit `T=1` | no: the bound does not name the pair | yes: explicit halt implies the bound | bound is a coarse certificate |
| `f_L1` contrast / Hamming contrast | no | no | member distinctions, not extra walls |

### N3 — hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| twelve-vertex two-cube | explicit finite patch, not all of `Z^3` |
| off-patch `o=0` | displayed default; not a derived vacuum |
| `f_two` as `u≥2` | displayed extra predicate; not Admissibility |
| seed `S0` | initial-condition content; not a privileged site |
| “lock” | displayed occupancy bit; Record still locks a possibility only when a record is present |
| “fill” | `|locks_T|=12` on this patch only |

### N4 — citation-to-residual matching

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and nearest-neighbor adjacency | sites and six-tuples are well-typed | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:41` | no privileged site | seed is initial content, not a Lattice privilege | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | one covariant nearest-neighbor rule exists | existence only; `f_two` is not that rule | yes; selector stays open |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unread sites have no readout | occupancy of an unread neighbor is displayed extra data | yes |
| `scripts/f_two_face_diagonal_seed_fill_2026_08_15.py` | halt pair and fill boolean | computed `(T, |locks|)=(1, 4)`, fill false | yes |

No evidence citation is used to claim that a physical formation law,
vacuum default, or `Z^3`-wide fill theorem has been closed.

### N5 — rhetoric and resolution audit

| Resolution | Executed? | Narrow negative supported? |
|---|---:|---|
| per element | yes: each first-wave six-tuple | `u=2` at those two sites only |
| per site | yes: all twelve vertices | four locks, eight unread |
| per mode | yes: one displayed `f_two` seed | other predicates are contrasts |
| per block | yes: the two-cube union | fill means all twelve vertices |
| lattice wide | no | no `Z^3` formation law is asserted |

### N6 — partial closure and primitive scan

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms`
node. No approved primitive supplies occupancy ticks or is needed for
the finite count. None is reclassified as an import or wall.

A partial closure is explicit: `f_two` does form a nonempty first wave
from this two-site seed, and it does reach a fixed point. Those positive
facts do not repair fill. `f_L1` from a one-site seed is a different
member and is not used as a hidden repair.

### N7 — hostile steelman

The strongest objection is that a different two-site pair, a different
off-patch default, or a later tick convention might still fill, or that
the three-site census already answered the fill question. The first
family is outside the claim: only `S0` and `o=0` are evaluated. The
three-site census is a different seed and a different halt pair
`(2, 8)`. To overturn the narrow negative it would have to exhibit an
unread ready site after tick 1 under this exact `f_two` and `S0`, or
show `|locks_1|=12`. Direct six-tuple evaluation rejects both.

### N8 — cross-cycle echo

Nearby displayed mechanisms are context, not load-bearing parents.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| one-site `f_two` first wave | empty first wave from a single lock | two face-diagonal locks make `u=2` at the two face-adjacent sites |
| displayed three-site fill numbers | `T=2`, eight locks, no fill | recomputed as contrast; halt pair here is `(1, 4)` |
| `f_L1` one-site fill | `f_L1` fills this patch at horizon 4 from one lock | different predicate (`u≥1`), not used as a parent |

No earlier mechanism retires the halt pair `(1, 4)` or the false fill
boolean on this seed.

No-Go Discipline disposition: **PASS** for the instance-level non-fill
stated at the start of this section.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> A site with no record cannot be read.

> A state is a configuration of records.

> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

## Runner Contract

The companion runner rebuilds the twelve-vertex two-cube, evaluates
`f_two` as `u≥2` on exact six-tuples with off-patch `o=0`, checks that
the first wave is `{(1,0,0),(0,1,0)}`, computes the halt pair
`(T, |locks|)=(1, 4)`, rejects fill, recomputes the displayed three-site
contrast, and separates `f_two` from both `f_L1` and Hamming parity.
Declared audit inputs are this note and the axiom memo.

`claim_scope`: f_two from the face-diagonal 2-site seed
`{(0,0,0),(1,1,0)}` on the twelve-vertex two-cube with off-patch `o=0`
reaches a fixed point with reported `(T, |locks|)=(1, 4)`. Displayed,
not adopted.
