---
claim_id: two_cube_integrated_member_l1_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied twelve-vertex two-cube patch, one executable member L1 returns updated locks, a formation-count clock, k=1 spectral-PVM traces in Q, and occupancy source/flux values. L1 is displayed, not adopted. No physical identification is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_integrated_member_l1_2026_08_14.py
---

# Two-Cube Integrated Member `L1`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact occupancy, clock, spectral-trace, and source/flux identities
for one displayed member `L1` on a supplied twelve-vertex two-cube patch.
`L1` is displayed executable data, not adopted law. Qubit remains `M_2(C)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_integrated_member_l1_2026_08_14.py`](../scripts/two_cube_integrated_member_l1_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the finite vertex set of two unit cubes that share a face:

```text
A = [0,1]^3,     B = [1,2] × [0,1] × [0,1].
```

The twelve vertices are the union of the eight vertices of `A` and the eight
vertices of `B`. The shared face is `F*` at `x=1`. The outer face of `B` is
`F_B` at `x=2`. Occupancy off this patch is `0`.

`L1` is one map. An unread site carries the occupancy kernel

```text
n_μ = (o_{+μ} − o_{-μ}) / 3.
```

Locked sites stay locked. An unread patch site forms if and only if `n ≠ 0`.
For a forming site, `k = |3n|^2 ∈ {1,2,3}` and the spectral traces of a
one-site `M_2(C)` PVM are

```text
Tr(ρ P±) = (3 ± √k) / 6.
```

On the seed `{(0,0,0)}` the first-wave sites have `k=1`, so the traces are
`2/3` and `1/3` in `Q`. This note restricts the PVM check to those `k=1`
sites.

The clock `F` is `0` on the empty configuration. One step increments `F` by
the number of new locks. Cube source and face flux are functions of occupancy:

```text
ρ(C) = ∑_{v ∈ C} o(v),
φ(F*) = ρ(A),
φ(F_B) = ρ(A) + ρ(B).
```

One `step_L1` returns `(locks', F', traces, ρ(A), ρ(B), φ(F*), φ(F_B))`.

After one step from the seed `{(0,0,0)}`:

- the new locks are the three on-patch axis neighbors
  `(1,0,0)`, `(0,1,0)`, `(0,0,1)`;
- the tick is the new-lock count `3`, so the clock goes `0 → 3`; the
  seed-inclusive lock count goes `1 → 4`;
- each new lock has `k=1` and traces `2/3`, `1/3`;
- `ρ(A) = 4`, `ρ(B) = 1`, `φ(F*) = 4`, `φ(F_B) = 5`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Z/Q identities for one displayed occupancy-PVM-clock-flux member on a supplied twelve-vertex patch."
trace_class: frontier_discovery
target_claim_id: two_cube_integrated_member_l1
target_blocker_text: "whether occupancy, spectral-PVM traces, a formation-count clock, and rho/phi can be one executable member on the two-cube"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied twelve-vertex patch and the k=1 first wave; L1 is displayed, not adopted"
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
  off-patch occupancy `0`, the occupancy kernel, the `k=1` restriction of the
  PVM traces, the formation-count clock, and the occupancy functions `ρ/φ`
  are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting this member as a physical law, lifting
  it off the supplied patch, or identifying `ρ/φ` with a continuum source
  remain separate, open obligations.

## Exact Objects

All runner coefficients are exact integers or `Fraction` values. No float is
used. The PVM check stays in `Q` by restricting to `k=1`, where `√k = 1`.

Occupancy `o(v)` is `1` on a lock in the patch and `0` otherwise, including
every off-patch neighbor. The kernel `n` is a triple in `Q^3`. Locked sites
are not re-tested for formation.

The one-site traces use the live Qubit presentation `M_2(C)`. They are
displayed spectral weights, not a change of the one-site algebra.

`ρ` and `φ` are functions of occupancy on the supplied cells and faces. They
are not a continuum field and they are not an inverse-square rule.

## Exact Target And Proof Obligations

The exact target is to exhibit one `step_L1` on the seed and to check its
returned tuple by exact arithmetic.

The obligation graph is:

1. the patch has twelve vertices; `A` and `B` meet in the four vertices of
   `F*`;
2. on the seed, the three on-patch axis neighbors have `n ≠ 0` and `k=1`,
   and every other unread patch site has `n = 0`;
3. the `k=1` traces equal `(3 ± 1)/6`, hence `2/3` and `1/3`;
4. the tick is `3`; clock values `0 → 3` and seed-inclusive lock counts
   `1 → 4` are both displayed;
5. after the step, `ρ(A)=4`, `ρ(B)=1`, `φ(F*)=ρ(A)=4`, and
   `φ(F_B)=ρ(A)+ρ(B)=5`.

All five obligations are closed below and in the runner. There is no missing
lemma for this bounded display.

## Theorem 1 — twelve-vertex two-cube patch

`A` has eight vertices with coordinates in `{0,1}^3`. `B` has eight vertices
with `x ∈ {1,2}` and `y,z ∈ {0,1}`. Their intersection is the four vertices
with `x=1`. The union has twelve sites, all in `Z^3`. Off-patch occupancy is
the supplied value `0`.

## Theorem 2 — first-wave formation from the seed

Start with locks `{(0,0,0)}`. At `(1,0,0)` the only nonzero neighbor
occupancy is `o(0,0,0)=1` on the `-x` bond, so

```text
n = (−1/3, 0, 0),     k = 1.
```

At `(0,1,0)` one has `n = (0, −1/3, 0)` and `k=1`. At `(0,0,1)` one has
`n = (0, 0, −1/3)` and `k=1`. Each of these three sites lies in the
twelve-vertex set, is unread, and has `n ≠ 0`, so each forms.

The seed is already locked, so it stays and is not a new lock. Every other
unread patch site has vanishing neighbor occupancy on the seed, hence `n=0`,
and does not form. In particular `(2,0,0)` and `(0,1,1)` stay unread.

On the empty configuration every neighbor occupancy is `0`, so no site forms.
The seed is initial data, not a kernel output.

## Theorem 3 — `k=1` spectral traces in `Q`

For `k=1` one has `√k=1`, so

```text
Tr(ρ P+) = (3+1)/6 = 2/3,     Tr(ρ P−) = (3−1)/6 = 1/3.
```

Both values lie in `Q`. Their sum is `1`. The runner evaluates these traces
only at the three first-wave sites.

## Theorem 4 — formation-count clock

`F=0` on the empty configuration. One step increments `F` by the number of
new locks. From the seed that increment is `3`.

Display both integers:

- new-lock clock on the seeded state: `0 → 3`;
- seed-inclusive lock count: `1 → 4`.

The tick is the new-lock count `3`. It is not the seed-inclusive lock count.

## Theorem 5 — occupancy source and flux

After the step the occupied sites are `(0,0,0)`, `(1,0,0)`, `(0,1,0)`, and
`(0,0,1)`. All four have `x ∈ {0,1}`, so they all lie in `A` and `ρ(A)=4`.
Only `(1,0,0)` has `x ∈ {1,2}`, so `ρ(B)=1`. Then

```text
φ(F*) = ρ(A) = 4,     φ(F_B) = ρ(A) + ρ(B) = 5.
```

These identities are the occupancy functions, not a sum of occupancy over
the face vertices alone. After one step the shared-face occupancy sum is
`1` and the outer-face occupancy sum is `0`; those face sums are not `φ`.

## Theorem 6 — one `step_L1`

On input locks `{(0,0,0)}` and clock `0`, `step_L1` returns

```text
locks' = {(0,0,0), (1,0,0), (0,1,0), (0,0,1)},
F' = 3,
traces = {(1,0,0), (0,1,0), (0,0,1)} ↦ (k=1, 2/3, 1/3),
ρ(A) = 4,     ρ(B) = 1,     φ(F*) = 4,     φ(F_B) = 5.
```

The same occupancy step, the same traces, the same tick, and the same
`ρ/φ` values are one returned tuple. `L1` is that tuple-valued map.

## Physical-Interpretation Boundary

The proved output is the displayed member on the supplied patch. This note
does not adopt `L1` as axiom content and does not rewrite Qubit. The
one-site algebra remains `M_2(C)`. The symbols `ρ` and `φ` remain functions
of occupancy.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. the tick `3` is not the seed-inclusive lock count `4`;
2. `φ(F*)` is not the occupancy sum on `F*`;
3. `φ(F_B)` is not the occupancy sum on `F_B`.

## What This Does Not Claim

- `L1` is displayed, not adopted.
- No inverse-square rule is claimed.
- Qubit remains `M_2(C)`.
- `ρ/φ` are functions of occupancy.
- The occupancy kernel is not a Lattice map.
- The first-wave identities are not a continuum lift and not a physical
  selection of this member.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> Records form.

Their dependency role is limited to the repository's site, one-site algebra,
nearest-neighbor, and formation vocabulary. This theorem separately supplies
the patch, the occupancy kernel, the clock, the `k=1` traces, and the
occupancy functions `ρ/φ`.

## Runner Contract

The companion runner identity-gates every helper and recomputes the first-wave
tuple from the occupancy kernel. It checks the tick `3` against the
seed-inclusive count `4`, checks that `φ` is not a face occupancy sum, quotes
the four live axiom sentences, and records the import boundary. Declared
review inputs are this note and the axiom memo only.
