---
claim_id: f_cut_k4_two_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the four F_cut maps with (wt1, opp2, adj2)=(1,1,1) on the two-cube with off-patch o=0, 2-site coverage is 66 iff vertex3=1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k4_two_site_coverage_2026_08_15.py
---

# Two-Site Coverage Of The Four k=4 F_cut Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock coverage of the four F_cut maps with
remaining-bit prefix `(wt1, opp2, adj2)=(1, 1, 1)` on the twelve-vertex
two-cube with off-patch occupancy `0`. No physical Admissibility selector
is asserted. The four-map ranking and the `vertex3` bit are displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k4_two_site_coverage_2026_08_15.py`](../scripts/f_cut_k4_two_site_coverage_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

On the two-cube `x ∈ {0,1,2}`, `y,z ∈ {0,1}` with off-patch occupancy `0`,
the cube-covariant class `F_cut` consists of the maps
`f:{0,1}^6 → {0,1}` with `f(empty)=f(full)=0` and `f(c)=f(1-c)`. After
those constraints, five remaining bits
`(wt1, opp2, adj2, vertex3, mixed3)` label the 32 maps.

The newly named 4 is the `k=4` class: the four remaining-bit tuples

```text
(1, 1, 1, 0, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

These are exactly the maps with `(wt1, opp2, adj2)=(1, 1, 1)` and
`vertex3 × mixed3` free. Each fills all four long-axis two-site seeds
(reconfirming `k = 4`). The two maps with `vertex3=1` fill every one of
the 66 two-site seeds:

```text
cov((1, 1, 1, 1, 0)) = 66
cov((1, 1, 1, 1, 1)) = 66
```

The two maps with `vertex3=0` do not:

```text
cov((1, 1, 1, 0, 0)) = 36
cov((1, 1, 1, 0, 1)) = 36
```

Inside this four, `cov = 66 iff vertex3 = 1`. Mixed3 is free on both
sides of the cut. Full two-site coverage on top of the `k=4` bits
therefore requires `vertex3=1` on this patch. Displayed, not adopted.
Do not adopt vertex3. Do not write them into Admissibility.

This is not leftover-character of #6443: that only reported k. The
present ranking is the two-site coverage of the newly named 4.

`f_L1(c)=1` if and only if some axis is unbalanced, equivalently if
`n_μ = c_{+μ} − c_{-μ}` is nonzero on at least one axis. This is **not** Hamming parity
`|c|_1 mod 2`. The L1 remaining-bit tuple is
`(1, 0, 1, 1, 1)` and is not a member of the newly named 4.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact two-site fill counts on the twelve-vertex two-cube rank the four k=4 F_cut maps and display cov=66 iff vertex3=1 inside that four."
trace_class: frontier_discovery
target_claim_id: f_cut_k4_two_site_coverage
target_blocker_text: "whether the four k=4 F_cut maps all attain cov=66, or whether vertex3 is required on top of those bits"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch occupancy 0; no physical Admissibility selector is asserted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded four-map coverage ranking"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences below supply the cubic nearest-neighbor geometry, covariance,
  and unreadability of an empty site. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the two-cube, the off-patch
  occupancy-`0` default, the `F_cut` class, the remaining-bit labels, the
  four long-axis seeds, and occupancy-to-lock dynamics are supplied
  mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of one remaining-bit tuple, including
  `vertex3`, by Record or Admissibility remains a separate obligation.

## Current Premise Boundary

The Lattice, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.

The axioms do not name `F_cut`, the remaining-bit tuple, `k`, or `cov`.
Those objects are theorem data.

## Exact Objects

A neighbor 6-tuple `c = (c_{+x}, c_{-x}, c_{+y}, c_{-y}, c_{+z}, c_{-z})`
records occupancy of the six coordinate neighbors. Axis type is
`(n_unbalanced, n_both, n_empty)`. Complement swaps both with empty.
Proper cube rotations act on 6-tuples; they partition `{0,1}^6` into ten
orbits.

`F_cut` is the cube-covariant class with `f(empty)=f(full)=0` and
`f(c)=f(1-c)`. Empty and full are fixed at 0, leaving five free bits in
the order `(wt1, opp2, adj2, vertex3, mixed3)`:

```text
wt1     ↔ (1, 0, 2)  and its complement (1, 2, 0)
opp2    ↔ (0, 1, 2)  and its complement (0, 2, 1)
adj2    ↔ (2, 0, 1)  and its complement (2, 1, 0)
vertex3 ↔ (3, 0, 0)
mixed3  ↔ (1, 1, 1)
```

The two-cube is the twelve sites `(x,y,z)` with `x ∈ {0,1,2}` and
`y,z ∈ {0,1}`. Off-patch occupancy `0` means a neighbor not among those
twelve is unoccupied. A blank-block is a different rule and is not used.

A tick locks every unlocked two-cube site whose current neighbor 6-tuple
has `f=1`. A seed fills when the lock set reaches all twelve sites.

The four long-axis two-site seeds are the opposite-end pairs of the four
length-2 edges:

```text
{(0,0,0),(2,0,0)}, {(0,0,1),(2,0,1)}, {(0,1,0),(2,1,0)}, {(0,1,1),(2,1,1)}.
```

`k(f)` is the number of those four seeds that fill. `cov(f)` is the
number of the `C(12,2)=66` unordered two-site seeds that fill.

## Exact Target And Proof Obligations

1. Reconfirm that each of the four maps has `k = 4`, and that
   `(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)` have `cov = 66`.
2. Compute `cov` of `(1, 1, 1, 0, 0)` and `(1, 1, 1, 0, 1)`.
3. State whether, inside this four, `cov = 66 iff vertex3 = 1`.

All three obligations are closed by exact enumeration of the 66 seeds
under occupancy-to-lock. No float is used.

## Theorem 1

The 32 `F_cut` remaining-bit tuples include exactly four with prefix
`(wt1, opp2, adj2)=(1, 1, 1)`. Those four are the newly named 4 listed
above. Direct evolution from each of the four long-axis seeds shows
`k = 4` for every member. Among all 32 maps, these are exactly the maps
with `k = 4`.

The same evolution on all 66 two-site seeds reconfirms

```text
cov((1, 1, 1, 1, 0)) = 66
cov((1, 1, 1, 1, 1)) = 66
```

Those two are the `vertex3=1` members of the four.

## Theorem 2

The `vertex3=0` members of the four do not fill every two-site seed:

```text
cov((1, 1, 1, 0, 0)) = 36
cov((1, 1, 1, 0, 1)) = 36
```

Both values are strictly less than 66. Mixed3 does not change `cov`
inside either `vertex3` slice.

## Theorem 3

Inside the newly named 4 the ranking is therefore

| remaining-bit tuple | vertex3 | mixed3 | k | cov |
|---|---|---|---|---|
| `(1, 1, 1, 0, 0)` | 0 | 0 | 4 | 36 |
| `(1, 1, 1, 0, 1)` | 0 | 1 | 4 | 36 |
| `(1, 1, 1, 1, 0)` | 1 | 0 | 4 | 66 |
| `(1, 1, 1, 1, 1)` | 1 | 1 | 4 | 66 |

So `cov = 66 iff vertex3 = 1`. On this patch, `vertex3` is required for
full two-site coverage on top of the `k=4` bits. Displayed, not adopted.
Do not adopt vertex3.

Not leftover-character of #6443: that only reported k. The present
object is the two-site coverage ranking of the newly named 4.

## No-Go Discipline

The result is a four-map ranking on one finite patch. It is not a
universal no-go against other `F_cut` maps, other seeds, or a later
derived selector.

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| treat leftover `k=4` as already ranking two-site coverage | **ATTEMPTED** | #6443 only reported `k`; `cov` of the `vertex3=0` maps is a new count |
| replace `f_L1` by Hamming parity | **ATTEMPTED** | Hamming `|c|_1 mod 2` is a different predicate and is not `f_L1` |
| adopt `vertex3` into Admissibility because `cov=66` requires it here | **ATTEMPTED** | the iff is displayed on four maps; it is not an axiom selector |
| use a blank-block in place of off-patch occupancy `0` | **ATTEMPTED** | blank-block is a different rule |
| score one seed or only the long-axis four | **ATTEMPTED** | `k` is already 4 for every member; the residual is the 66-seed `cov` |
| import a Hamiltonian, continuum kernel, or physical Record law | **ATTEMPTED** | those objects are outside the finite occupancy-to-lock ranking |

### N2 — wall independence

One displayed cut is claimed: inside the four, `cov=66` holds exactly
when `vertex3=1`. That is not a second impossibility wall and is not an
axiom-necessity claim.

### N3 — hidden-wall scan

The two-cube, the off-patch default, the `F_cut` bits, the long-axis
four, and the 66 two-site seeds are all declared. No full-lattice
embedding, formation rate, or realized-state selector is imported.

### N4 — residual matching

The residual after #6443 was the two-site coverage of the maps that
already have `k=4`. This note fills that residual and does not enlarge
it to a physical selector.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — each of the four k=4 maps is scored on the long-axis four and on all 66 two-site seeds
per-block: executed — the four-map ranking is the newly named k=4 class
lattice-wide: not executed — no Z^3-wide formation law is claimed
```

### N6 — partial-closure paths

A later derived selector could still distinguish the two `vertex3=1`
maps, or could fail on a larger patch. Those routes remain live and need
not alter the axioms.

### N7 — steelman

The strongest objection is that `k=4` already selected the physically
relevant maps, so a `cov<66` count is leftover bookkeeping. Correct that
#6443 named the four. Incorrect that `k` ranks them: the two
`vertex3=0` maps miss 30 of the 66 two-site seeds.

### N8 — cross-cycle echo

Earlier `F_cut` coverage work displayed two maximizers with `cov=66`,
both with `vertex3=1`. This note agrees with that pair and adds the
`cov` of the other two `k=4` maps.

No-Go Discipline disposition: **PASS**

## Boundaries and explicit non-claims

- The theorem is conditional on the supplied two-cube and off-patch
  occupancy `0`.
- `vertex3` is displayed data, not an approved primitive.
- The ranking does not select between `(1, 1, 1, 1, 0)` and
  `(1, 1, 1, 1, 1)`.
- No axiom or approved primitive is added.
- Do not write them into Admissibility.
