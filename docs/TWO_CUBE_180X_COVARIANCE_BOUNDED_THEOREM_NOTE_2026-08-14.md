---
claim_id: two_cube_180x_covariance_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube complex, R:(x,y,z)↦(x,1−y,1−z) is a bijection of the twelve vertices. The occupancy step (locks stay; unread forms iff n≠0) commutes with R on all 4096 occupancy configurations, and the occupancy counts ρ(A), ρ(B) and the displayed tree-gauge fluxes φ(F*), φ(F_B) are R-invariant. Seed (0,0,0) maps to (0,1,1); the formation pattern rotates with it. Not a gauge-uniqueness claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_180x_covariance_2026_08_14.py
---

# 180° About `x` Commutes With The Two-Cube Update

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact covariance of the displayed occupancy+`ρ`+`φ` step
under one 180° rotation about `x`, checked on all `2^12` occupancy
configurations of the twelve vertices.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_180x_covariance_2026_08_14.py`](../scripts/two_cube_180x_covariance_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Cube `A = [0,1]^3` and cube `B = [1,2]×[0,1]×[0,1]` share the face
`x=1`. The twelve vertices are

```text
A-only:  (0,0,0) (0,0,1) (0,1,0) (0,1,1)
shared:  (1,0,0) (1,0,1) (1,1,0) (1,1,1)
B-only:  (2,0,0) (2,0,1) (2,1,0) (2,1,1)
```

The map `R(x,y,z) = (x, 1-y, 1-z)` is a bijection of those twelve
points. Its linear part about the axis through `(*, 1/2, 1/2)` is
`diag(1,-1,-1)`, which has determinant `1`: a 180° proper rotation
about `x`. `R` preserves the A-only, shared, and B-only blocks
setwise, and it preserves the shared face `F*` (`x=1`) and `B`'s
outer face `F_B` (`x=2`) setwise.

Occupancy `o` is a `{0,1}`-label of the twelve vertices. Off-patch
occupancy is `0`. Locked sites stay. At an unread site

```text
n_μ = (o_{+μ} − o_{-μ}) / 3
```

and the site forms iff `n ≠ 0`. Cube sources are occupancy counts

```text
ρ(A) = ∑_{v ∈ A} o(v),    ρ(B) = ∑_{v ∈ B} o(v).
```

Shared vertices contribute to both. The displayed tree-gauge fluxes
(not adopted, not uniqueness-claimed) are the `ρ`-decoders

```text
φ(F*)  = ρ(A),    φ(F_B) = ρ(A) + ρ(B).
```

On every one of the `2^{12} = 4096` occupancy configurations,

```text
R ∘ occ_step = occ_step ∘ R,    ρ(R(s)) = ρ(s),    φ(R(s)) = φ(s).
```

Seed `{(0,0,0)}` is sent to `{(0,1,1)}`. The three first-wave
formations rotate with the seed. This is covariance of one displayed
integrated update, not a gauge-uniqueness theorem and not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact commutation of R with occ_step on all 4096 occupancy labels, with ρ and displayed φ invariant."
trace_class: frontier_discovery
target_claim_id: two_cube_180x_covariance
target_blocker_text: "integrated occupancy+rho+phi update is not known to commute with a displayed cube rotation"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit; gauge uniqueness and other rotations are not in this note"
conditional_surface_status: "exact for the displayed R and occupancy kernel on the twelve vertices"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

Those sentences name proper cubic rotations and nearest-neighbor
covariance. They do not name the twelve-vertex two-cube, this `R`,
`occ_step`, `ρ`, or `φ`. Display. Do not adopt.

## Theorem 1 — `R` is a bijection of the twelve vertices

`R(x,y,z) = (x, 1-y, 1-z)` sends each listed vertex to another listed
vertex. `R∘R` is the identity, so `R` is an involution and therefore
a bijection. The three blocks (A-only, shared, B-only) are each
preserved. Linear part `diag(1,-1,-1)` has determinant `1`.

## Theorem 2 — occupancy step commutes with `R`

`R` sends `±e_y` to `∓e_y` and `±e_z` to `∓e_z`, and it fixes
`±e_x`. Off-patch occupancy remains `0` because `R` permutes the
patch. Therefore `n ≠ 0` at `v` if and only if `n ≠ 0` at `R(v)`
after the occupancy is transported by `R`. Locked sites stay, so

```text
R(occ_step(s)) = occ_step(R(s))
```

holds for every occupancy `s` of the twelve vertices. The companion
runner checks all `4096` labels.

## Theorem 3 — `ρ` and displayed `φ` are invariant

Because `R` permutes the eight `A` vertices among themselves and the
eight `B` vertices among themselves, occupancy counts are unchanged:

```text
ρ(R(s)) = ρ(s).
```

The displayed fluxes are functions of `ρ` alone, so
`φ(R(s)) = φ(s)`. This is invariance of a displayed decoder, not a
uniqueness theorem for tree gauges.

## Theorem 4 — seed rotates; formation pattern rotates

`R(0,0,0) = (0,1,1)`. The seed is not a fixed point. One occupancy
step from `{(0,0,0)}` occupies

```text
{(0,0,0), (1,0,0), (0,1,0), (0,0,1)}.
```

Applying `R` yields

```text
{(0,1,1), (1,1,1), (0,0,1), (0,1,0)},
```

which is exactly one occupancy step from `{(0,1,1)}`. Empty occupancy
is a fixed point of both `R` and `occ_step`.

## Theorem 5 — display

Qubit remains `M_2(C)`. QCD is unused. The axiom sentences quoted
above do not name this update.

## Mutations

1. Predicate “`R` sends seed `(0,0,0)` to itself” must fail.
2. Predicate “some occupancy of the twelve vertices fails
   `R∘occ_step = occ_step∘R`” must fail.
3. Predicate “`ρ` changes under `R`” must fail.
4. Predicate “note adopts Newton / a unique gauge / axiom text” must fail.

Identity gates: `rot`, `occ_step`, `commutes`, `rho`.

## Honest-auditor / Boundary

All `4096` occupancy labels of the twelve vertices; one displayed
180° rotation about `x`. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No unique tree gauge. No axiom text.
- No inverse-square law. No other generator of the cube group.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
