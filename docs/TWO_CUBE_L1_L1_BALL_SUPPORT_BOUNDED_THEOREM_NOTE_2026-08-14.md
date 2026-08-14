---
claim_id: two_cube_l1_l1_ball_support_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied twelve-vertex two-cube patch, two occupancy steps of the displayed member L1 lock exactly the on-patch ell^1 ball of radius t at tick t. Sites at ell^1 distance 3 and 4 remain unread after tick 2. L1 is displayed, not adopted. No physical identification is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_l1_ball_support_2026_08_14.py
---

# Two-Cube `L1` Formation Support Is The ℓ¹ Ball Of Radius `t`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact equality of the locked set after `t` occupancy steps of the
displayed member `L1` with the on-patch ℓ¹ ball of radius `t`, for `t=1`
and `t=2` on the supplied twelve-vertex two-cube patch. `L1` is displayed
executable data, not adopted law. Qubit remains `M_2(C)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_l1_ball_support_2026_08_14.py`](../scripts/two_cube_l1_l1_ball_support_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the finite vertex set of two unit cubes that share a face:

```text
A = [0,1]^3,     B = [1,2] × [0,1] × [0,1].
```

The twelve vertices are the union of the eight vertices of `A` and the eight
vertices of `B`. Occupancy off this patch is `0`. Distance from the seed
`(0,0,0)` is the lattice ℓ¹ function

```text
d(v) = |v_x| + |v_y| + |v_z|.
```

The on-patch sphere of radius `r` is `{v ∈ patch : d(v) = r}`. The on-patch
ball of radius `t` is `{v ∈ patch : d(v) ≤ t}`.

`L1` is one displayed occupancy map. An unread site carries the occupancy
kernel

```text
n_μ = (o_{+μ} − o_{-μ}) / 3.
```

Locked sites stay locked. An unread patch site forms if and only if `n ≠ 0`.
This note uses only that occupancy step. It does not evaluate spectral traces:
tick-2 forming sites have `k = |3n|^2 = 2`, which would leave `Q`.

Starting from the seed `{(0,0,0)}`:

- after tick 1 the locked set equals the on-patch ball of radius `1`;
- after tick 2 the locked set equals the on-patch ball of radius `2`;
- every site with `d ∈ {3,4}` is still unread at tick 2.

The same occupancy kernel on a five-site line is a different displayed
patch. This note is the two-cube patch under `L1`, not a new occupancy
kernel and not a new patch.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Z/Q identities: two occupancy steps of displayed L1 lock the on-patch ell^1 ball of radius t."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_l1_ball_support
target_blocker_text: "whether L1 formation support on the two-cube is the ell^1 ball of radius t"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied twelve-vertex patch for t=1 and t=2; L1 is displayed, not adopted"
hypothetical_axiom_status: not proposed
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the four live axiom sentences quoted below. They
  are quoted without rewrite. No map in this note is a Lattice map. Qubit is
  not rewritten.
- **Explicit theorem-domain condition:** the twelve-vertex two-cube patch,
  off-patch occupancy `0`, the occupancy kernel, the seed `(0,0,0)`, and the
  ℓ¹ distance from that seed are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting this member as a physical law, lifting
  it off the supplied patch, or identifying the ℓ¹ ball with a continuum
  causal cone remain separate, open obligations.

## Exact Objects

All runner coefficients are exact integers or `Fraction` values. No float is
used. Occupancy `o(v)` is `1` on a lock in the patch and `0` otherwise,
including every off-patch neighbor. The kernel `n` is a triple in `Q^3`.
Locked sites are not re-tested for formation.

The on-patch spheres computed from `d` are

```text
d = 0 :  {(0,0,0)}
d = 1 :  {(1,0,0), (0,1,0), (0,0,1)}
d = 2 :  {(1,1,0), (1,0,1), (0,1,1), (2,0,0)}
d = 3 :  {(1,1,1), (2,1,0), (2,0,1)}
d = 4 :  {(2,1,1)}
```

These five sets partition the twelve-vertex patch.

## Exact Target And Proof Obligations

The exact target is to compare the locked set after each occupancy step with
the ball computed from `d`, not with a handwritten site list copied into both
sides of an equality.

The obligation graph is:

1. `d` on the twelve vertices yields the five spheres above, and they
   partition the patch;
2. from the seed, the forming set is exactly the `d=1` sphere, so the locked
   set after tick 1 is the ball of radius `1`;
3. from that locked set, the forming set is exactly the `d=2` sphere, so the
   locked set after tick 2 is the ball of radius `2`;
4. every `d=3` and `d=4` site has `n=0` before tick 2 and remains unread.

All four obligations are closed below and in the runner. There is no missing
lemma for this bounded display.

## Theorem 1 — after tick 1 the locked set is the radius-`1` ball

Start with locks `{(0,0,0)}`. At `(1,0,0)` the only nonzero neighbor
occupancy is `o(0,0,0)=1` on the `-x` bond, so

```text
n = (−1/3, 0, 0) ≠ 0.
```

At `(0,1,0)` one has `n = (0, −1/3, 0)`. At `(0,0,1)` one has
`n = (0, 0, −1/3)`. Each of these three sites lies in the twelve-vertex set,
is unread, and has `n ≠ 0`, so each forms.

Every other unread patch site has vanishing neighbor occupancy on the seed,
hence `n=0`, and does not form. The seed is already locked, so it stays.
Therefore

```text
locks_1 = {(0,0,0)} ∪ {v : d(v)=1} = {v ∈ patch : d(v) ≤ 1}.
```

## Theorem 2 — after tick 2 the locked set is the radius-`2` ball

The tick-1 locks stay. At each `d=2` site the runner recomputes `n` from
those locks:

```text
(1,1,0) :  n = (−1/3, −1/3, 0) ≠ 0
(1,0,1) :  n = (−1/3, 0, −1/3) ≠ 0
(0,1,1) :  n = (0, −1/3, −1/3) ≠ 0
(2,0,0) :  n = (−1/3, 0, 0)     ≠ 0
```

Each of these four sites is unread and on-patch, so each forms. No other
unread patch site has `n ≠ 0`. Therefore

```text
locks_2 = locks_1 ∪ {v : d(v)=2} = {v ∈ patch : d(v) ≤ 2}.
```

The four tick-1 locks remain occupied. The lock count is `8`.

## Theorem 3 — every `d=3` and `d=4` site is unread at tick 2

Before tick 2, each site with `d ∈ {3,4}` has only unread or off-patch
neighbors, so `n=0` and the site does not form. After tick 2 those four
sites remain outside `locks_2`. Equivalently,

```text
patch \ locks_2 = {v ∈ patch : d(v) ≥ 3}.
```

On the empty configuration every neighbor occupancy is `0`, so no site
forms. The seed is initial data, not a kernel output.

## Physical-Interpretation Boundary

The proved output is the displayed occupancy support on the supplied patch.
This note does not adopt `L1` as axiom content and does not rewrite Qubit.
The one-site algebra remains `M_2(C)`. The equality `locks_t = ball(t)` is
an occupancy identity, not a continuum causal cone and not a selection of
this member as physical law.

## Mutation Checks

Two non-equivalences guard the load-bearing conclusions:

1. after tick 1 the locked set is not the Chebyshev ball of radius `1`
   (that ball already contains `(1,1,0)`, which is still unread);
2. after tick 2 the locked set is not the Chebyshev ball of radius `2`
   (that ball is the whole twelve-vertex patch; only eight sites are locked).

## What This Does Not Claim

- `L1` is displayed, not adopted.
- Qubit remains `M_2(C)`.
- The occupancy kernel is not a Lattice map.
- The support identity is not a continuum lift and not a physical selection
  of this member.
- The claim is not a new occupancy kernel and not a new patch.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> Records form.

Their dependency role is limited to the repository's site, one-site algebra,
nearest-neighbor, and formation vocabulary. This theorem separately supplies
the patch, the occupancy kernel, the seed, and the ℓ¹ distance.

## Runner Contract

The companion runner identity-gates every helper and recomputes `n` at every
unread patch site after each tick. It compares each locked set to the ball
computed from `d`, checks that the `d=3` and `d=4` sites stay unread,
rejects the Chebyshev balls of radius `1` and `2` as the locked sets, quotes
the four live axiom sentences, and records the import boundary. Declared
review inputs are this note and the axiom memo only.
