---
claim_id: two_cube_l1_draw_does_not_feed_n_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied twelve-vertex two-cube patch, after one L1 tick from the seed, assigning first-wave lock labels + or − leaves occupancy 1 at every first-wave site. The occupancy kernel n at every unread site before tick 2 is therefore the same for the all-+ assignment and the mixed assignment with (1,0,0)=+ and the other first-wave sites −. The tick-2 formation set is independent of that realized PVM content. L1 is displayed, not adopted. No physical identification is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_draw_does_not_feed_n_2026_08_14.py
---

# Two-Cube `L1` Realized Draw Does Not Feed `n`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact occupancy and occupancy-kernel identities after one displayed
`L1` tick on a supplied twelve-vertex two-cube patch. First-wave lock labels
are realized `P+`/`P−` content. Occupancy stays `1` in both displayed
assignments. Qubit remains `M_2(C)`. `L1` is displayed executable data, not
adopted law.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_draw_does_not_feed_n_2026_08_14.py`](../scripts/two_cube_l1_draw_does_not_feed_n_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the finite vertex set of two unit cubes that share a face:

```text
A = [0,1]^3,     B = [1,2] × [0,1] × [0,1].
```

The twelve vertices are the union of the eight vertices of `A` and the eight
vertices of `B`. Occupancy off this patch is `0`. The displayed member `L1`
uses the occupancy kernel

```text
n_μ = (o_{+μ} − o_{-μ}) / 3.
```

Locked sites stay locked. An unread patch site forms if and only if `n ≠ 0`.
On the seed `{(0,0,0)}` the first-wave sites are `(1,0,0)`, `(0,1,0)`, and
`(0,0,1)`. Each has `k = |3n|^2 = 1`. The one-site spectral traces in `Q` are

```text
Tr(ρ P+) = (3+1)/6 = 2/3,     Tr(ρ P−) = (3−1)/6 = 1/3.
```

`L1` records those traces. This note then assigns each first-wave site a lock
label `+` or `−`: the realized projector content at that site. Two assignments
are displayed:

- all `+`;
- mixed: `(1,0,0) = +` and the other first-wave sites `−`.

Occupancy is `1` at every first-wave site in both assignments. The lock label
is record content, not a change of occupancy.

**Theorem.** After the first tick, `n` at every unread patch site is the same
for both assignments. The tick-2 formation set is therefore independent of
the realized PVM content. That set is

```text
{(1,1,0), (1,0,1), (0,1,1), (2,0,0)}
```

in both branches.

This is not a new family of `k` projectors and not a three-site line draw.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Z/Q identities: first-wave PVM labels do not change occupancy, so n before tick 2 and the tick-2 formation set are assignment-independent on the supplied twelve-vertex patch."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_draw_does_not_feed_n
target_blocker_text: "whether realized first-wave PVM content feeds the occupancy kernel before tick 2"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied twelve-vertex patch and the two displayed first-wave assignments; L1 is displayed, not adopted"
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
  off-patch occupancy `0`, the `L1` occupancy kernel, first-wave `k=1` traces
  in `Q`, and the two displayed lock-label assignments are supplied
  mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting `L1` as a physical law, lifting it off
  the supplied patch, or adopting a Born reading of the traces remain
  separate, open obligations.

## Exact Objects

All runner coefficients are exact integers or `Fraction` values. No float is
used. First-wave traces stay in `Q` because `k=1`.

Occupancy `o(v)` is `1` on a lock in the patch and `0` otherwise, including
every off-patch neighbor. A first-wave lock label `+` or `−` does not change
`o(v)`. The kernel `n` is a triple in `Q^3` computed from occupancy alone.

The one-site traces use the live Qubit presentation `M_2(C)`. They are
displayed spectral weights, not a change of the one-site algebra and not a
new projector family.

## Exact Target And Proof Obligations

The exact target is to compare the two displayed first-wave assignments after
one `L1` tick from the seed.

The obligation graph is:

1. the patch has twelve vertices;
2. on the seed, each first-wave site has `k=1` and traces `2/3`, `1/3`;
3. occupancy at every first-wave site is `1` under both assignments;
4. `n` at every unread patch site before tick 2 is the same in both
   assignments;
5. the forming set after tick 1 is
   `{(1,1,0), (1,0,1), (0,1,1), (2,0,0)}` in both branches.

All five obligations are closed below and in the runner. There is no missing
lemma for this bounded display.

## Theorem 1 — first-wave sites after the seed tick

Start with locks `{(0,0,0)}`. At `(1,0,0)` the only nonzero neighbor occupancy
is `o(0,0,0)=1` on the `-x` bond, so

```text
n = (−1/3, 0, 0),     k = 1.
```

At `(0,1,0)` one has `n = (0, −1/3, 0)` and `k=1`. At `(0,0,1)` one has
`n = (0, 0, −1/3)` and `k=1`. Each of these three sites lies in the
twelve-vertex set, is unread, and has `n ≠ 0`, so each forms. After the tick
the locked set is

```text
{(0,0,0), (1,0,0), (0,1,0), (0,0,1)}.
```

The `k=1` traces are `(3±1)/6`, hence `2/3` and `1/3`. Their sum is `1`.

## Theorem 2 — occupancy is `1` for both displayed assignments

Assign each first-wave site a lock label `+` or `−`. The two displayed
assignments are

```text
all-+ :  (1,0,0) ↦ +,  (0,1,0) ↦ +,  (0,0,1) ↦ +
mixed :  (1,0,0) ↦ +,  (0,1,0) ↦ −,  (0,0,1) ↦ −
```

In both assignments every first-wave site is locked, so `o=1` there. The
seed remains occupied. Occupancy off the patch remains `0`. The label is
realized PVM content at an already-formed site. It is not a signed occupancy
and it is not a new `k` projector.

## Theorem 3 — `n` before tick 2 is assignment-independent

The kernel `n` at an unread site is a function of neighbor occupancies. Those
occupancies after tick 1 are the same function of the locked set in both
assignments. Therefore `n` at every unread patch site is the same pair of
triples.

Explicit values, identical in both branches:

```text
(1,1,0) : n = (−1/3, −1/3, 0)
(1,0,1) : n = (−1/3, 0, −1/3)
(0,1,1) : n = (0, −1/3, −1/3)
(2,0,0) : n = (−1/3, 0, 0)
(1,1,1) : n = (0, 0, 0)
(2,1,0) : n = (0, 0, 0)
(2,0,1) : n = (0, 0, 0)
(2,1,1) : n = (0, 0, 0)
```

If a minus label were misread as vacant occupancy, `n` at `(1,1,0)` and at
`(0,1,1)` would change. That mutation is not the `L1` occupancy rule.

## Theorem 4 — tick-2 formation set is the same in both branches

An unread site forms if and only if `n ≠ 0`. From the table of Theorem 3 the
forming set after tick 1 is

```text
{(1,1,0), (1,0,1), (0,1,1), (2,0,0)}
```

in both assignments. The four remaining unread patch sites stay unread. The
tick-2 formation set is therefore independent of the realized first-wave PVM
content.

## Physical-Interpretation Boundary

The proved output is the displayed comparison on the supplied patch. This
note does not adopt `L1` as axiom content and does not rewrite Qubit. The
one-site algebra remains `M_2(C)`. The lock labels are displayed projector
content. They are not a physical selection rule and not a new projector
family.

## Mutation Checks

Two non-equivalences guard the load-bearing conclusions:

1. a minus lock label is not vacant occupancy: treating `(0,1,0)` as
   unoccupied changes `n` at `(1,1,0)` and at `(0,1,1)`;
2. the tick-2 formation set is not the first-wave set
   `{(1,0,0), (0,1,0), (0,0,1)}`.

## What This Does Not Claim

- `L1` is displayed, not adopted.
- No inverse-square rule is claimed.
- Qubit remains `M_2(C)`.
- The occupancy kernel is not a Lattice map.
- Realized first-wave labels are not a new family of `k` projectors.
- The comparison is not a three-site line draw.
- Occupancy remains a `{0,1}` function of the locked set; it is not signed
  by the lock label.
- The identities are not a continuum lift and not a physical selection of
  this member.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> Records form.

Their dependency role is limited to the repository's site, one-site algebra,
nearest-neighbor, and formation vocabulary. This theorem separately supplies
the patch, the occupancy kernel, the first-wave traces, and the two displayed
lock-label assignments.

## Runner Contract

The companion runner identity-gates every helper and recomputes `n` from
occupancy at every unread patch site in both assignments. It checks that
occupancy is `1` under both labelings, that the two `n` tables agree, that
the forming set after tick 1 is the four-site set above in both branches,
quotes the four live axiom sentences, and records the import boundary.
Declared review inputs are this note and the axiom memo only.
