---
claim_id: f_two_minimal_seed_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the twelve-vertex two-cube with off-patch o=0, f_two has no first wave from 1-site seeds, has a first wave from an explicit 2-site face-diagonal seed (22 of 66 pairs), and has a first wave from an explicit 3-site seed. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_two_minimal_seed_2026_08_15.py
---

# Minimal Occupancy Seed For An `f_two` First Wave

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** first-wave occupancy of the displayed two-axis predicate
`f_two` (`u ≥ 2`) on the twelve-vertex two-cube of construction `#6320`
with off-patch occupancy `o = 0`. The member is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_two_minimal_seed_2026_08_15.py`](../scripts/f_two_minimal_seed_2026_08_15.py)

## Result up front

The displayed two-cube has twelve vertices

```text
A = {0,1}^3,
B = {1,2} × {0,1}^2,
P = A ∪ B.
```

A seed `S ⊂ P` locks exactly the sites in `S`. Off-patch occupancy is the
displayed L1 vacuum default `o = 0`, used here only to hold the patch data
fixed and not adopted. At an unlocked site `v ∈ P \ S` write `c_{±μ}` for
the occupancy of the neighbor `v ± e_μ` and

```text
u(v) = |{ μ : c_{+μ} ≠ c_{-μ} }|.
```

The site is ready for `f_two` iff `u(v) ≥ 2`. The first wave of `S` is the
set of unlocked ready sites.

Every one-site seed has empty first wave: each neighbor of a single lock
has `u ≤ 1`. That is the leftover one-seed emptiness of `#6384`, now
checked on all twelve vertices rather than only `(0,0,0)`.

Not every two-site seed is empty. A pair has a nonempty first wave if and
only if the two sites are opposite corners of an on-patch square (a face
diagonal). There are `C(12,2) = 66` pairs and exactly 22 face diagonals
(six faces on cube `A`, six on cube `B`, two diagonals each, minus the two
diagonals of the shared face counted twice). One explicit pair is

```text
S2 = {(0,0,0), (1,1,0)},
first wave = {(1,0,0), (0,1,0)}.
```

The three axis neighbors of the corner `(0,0,0)` also work:

```text
S3 = {(1,0,0), (0,1,0), (0,0,1)},
first wave = {(0,0,0), (1,0,1), (1,1,0), (0,1,1)}.
```

So the minimal occupancy-seed cardinality that makes the first wave of
`f_two` nonempty on this patch is 2. L1's displayed one-site seed already
has a three-site first wave; that is a member difference, not an
L1-identity clone. This note does not adopt `f_two`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The one-site emptiness, the 22-of-66 face-diagonal pair census, and the explicit 2-site and 3-site first waves are finite exact listings on twelve vertices; no physical formation rule is selected."
trace_class: frontier_discovery
target_claim_id: f_two_minimal_occupancy_seed_cardinality
target_blocker_text: "smallest occupancy seed on the displayed two-cube that makes the first wave of f_two nonempty"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "further structure beyond a nonempty first wave is required before any displayed occupancy-to-lock predicate can be adopted"
conditional_surface_status: "exact on the displayed twelve-vertex two-cube with o=0; no physical law, rate, or site selector"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

The current Lattice and Admissibility wording in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Admissibility names one fixed covariant rule and leaves form open: read with
Record, the distribution is conditional on formation at that site; it does not
supply the formation site, probability, or rate.

Record states:

Records form.

When present, a record locks exactly one admissible local possibility.

Those sentences identify the covariance group, the lock operation, and the
open formation slot. They do not name `f_two`, a seed cardinality, or a
two-cube. The alphabet `{0,1}` on occupancy, the patch `P`, and `o = 0`
are displayed construction data from `#6320` and `#6384`, not axiom text.

## Exact objects

Slots are ordered `(+x,-x,+y,-y,+z,-z)`. Occupancy of a locked site is `1`.
Occupancy of an unlocked on-patch site is `0`. Occupancy of an off-patch
site is `o = 0`. The occupancy 6-tuple at `v ∈ P` is the six neighbor
occupancies. Then

```text
f_two(c) = 1  iff  u(c) ≥ 2,
f_L1(c)  = 1  iff  u(c) ≥ 1.
```

`f_L1` is displayed only as a contrast on one-site seeds. Neither predicate
is adopted.

A pair `{p,q} ⊂ P` is a face diagonal when the taxicab distance is 2, the
coordinatewise max-gap is 1, and `p` and `q` have exactly two common
on-patch neighbors. Those two neighbors are the other corners of the unique
on-patch square they span.

## Theorem 1 — every one-site seed has empty first wave

Let `S = {s}` with `s ∈ P`. For an unlocked site `v`, an axis `μ` is
unbalanced only if exactly one of `v ± e_μ` equals `s`. A site has at most
one neighbor equal to `s`, so `u(v) ≤ 1`. Ready for `f_two` requires
`u(v) ≥ 2`. The first wave is empty.

Direct evaluation on all twelve seeds confirms emptiness. In particular the
three axis neighbors of `(0,0,0)` each have `u = 1`, which is the `#6384`
one-seed fact, now the full one-site census rather than leftover character
of that single seed.

## Theorem 2 — two-site first waves are exactly the face diagonals

There are `C(12,2) = 66` two-site seeds.

If `{p,q}` is an on-patch face diagonal, the other two corners `v,w` of
that square are each adjacent to both locks along two distinct axes. At
each of `v` and `w` those two axes are unbalanced and the third is
balanced, so `u = 2`. Both corners are unlocked. The first wave is
`{v,w}`.

If `{p,q}` is not a face diagonal, no unlocked site is adjacent to both
locks along two distinct axes. A site adjacent to only one lock has
`u ≤ 1`. A site adjacent to both locks along the same axis (the midpoint
of an axis segment of length 2) has that axis balanced (`1 = 1`) and the
other axes empty, so `u = 0`. The first wave is empty.

The two-cube has six faces on `A` and six on `B`. Each face contributes two
diagonals. The shared face `x = 1` is counted in both cubes, so the number
of distinct face diagonals is

```text
6·2 + 6·2 − 2 = 22.
```

Direct listing confirms: 22 pairs have nonempty first wave, 44 have empty
first wave, and the nonempty set is exactly the face-diagonal set. One
explicit witness is `S2` above.

The statement “every two-site seed has empty first wave” is therefore
false. It is recorded here as a failed mutation, not as a theorem.

## Theorem 3 — an explicit three-site seed has a nonempty first wave

Let `S3` be the three axis neighbors of the corner `(0,0,0)`,

```text
S3 = {(1,0,0), (0,1,0), (0,0,1)}.
```

The corner itself has the three locks on its three on-patch axes and
off-patch `0` on the opposite slots, so `u((0,0,0)) = 3`. It is unlocked,
hence ready. Direct evaluation gives the full first wave

```text
{(0,0,0), (1,0,1), (1,1,0), (0,1,1)}.
```

The last three sites are the face-diagonal partners of pairs inside `S3`.
The first wave is nonempty. Combined with Theorem 1 and Theorem 2, the
minimal seed cardinality for a nonempty `f_two` first wave on this patch
is 2, not 3.

## Obligation graph

| obligation | exact disposition |
|---|---|
| `\|P\| = 12` | `A ∪ B` listed |
| off-patch default | displayed `o = 0`, not adopted |
| ready | `u ≥ 2` and unlocked |
| one-site first wave | empty on all 12 seeds (Theorem 1) |
| pair count | `C(12,2) = 66` |
| face-diagonal count | `22` |
| two-site first wave | nonempty iff face diagonal (Theorem 2) |
| explicit pair | `S2` with wave `{(1,0,0),(0,1,0)}` |
| explicit triple | `S3` with four-site wave (Theorem 3) |
| minimal cardinality | `2` |
| L1 one-site contrast | first wave of `{(0,0,0)}` has three sites |
| adopt `f_two` | not claimed |

## Imports and non-claims

The only scientific dependency is the current four-axiom authority linked
above, used only to pin the lattice adjacency, the lock operation, and the
open formation slot. The two-cube, the off-patch default, and `f_two` are
displayed construction data. No observational comparator is admitted. No
dynamics, Hamiltonian, or record-production process is constructed.

This note is a seed-cardinality census for one displayed predicate. It is
not leftover-character of the `#6384` one-seed emptiness and not an
L1-identity replay. It does not adopt `f_two`. It does not write axiom
sentences.

## Value and no-go boundary

The positive content is the exact one-site emptiness, the exact 22-of-66
face-diagonal pair census, and the explicit 2-site and 3-site first waves.
The negative content is only that one-site seeds do not start `f_two` on
this patch, and that “every pair is empty” fails. Further structure could
still select or reject the member. No global impossibility of a formation
rule is claimed.
