---
claim_id: two_cube_l1_second_wave_k_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied twelve-vertex two-cube patch, after tick 1 of displayed member L1 locks {(0,0,0),(1,0,0),(0,1,0),(0,0,1)}, the four unread sites (1,1,0), (1,0,1), (0,1,1), (2,0,0) form, their integer 3n and k=|3n|^2 are the displayed table with k in {1,2}, and every other unread patch site has n=0. L1 is displayed, not adopted. No spectral traces are claimed at k=2."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_second_wave_k_2026_08_14.py
---

# Two-Cube `L1` Second-Wave Spectral `k`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integer `3n` and `k = |3n|^2` at tick 2 of one displayed
member `L1` on a supplied twelve-vertex two-cube patch. `L1` is displayed
executable data, not adopted law. Qubit remains `M_2(C)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_second_wave_k_2026_08_14.py`](../scripts/two_cube_l1_second_wave_k_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the finite vertex set of two unit cubes that share a face:

```text
A = [0,1]^3,     B = [1,2] × [0,1] × [0,1].
```

The twelve vertices are the union of the eight vertices of `A` and the eight
vertices of `B`. Occupancy off this patch is `0`.

`L1` is one occupancy-step map. An unread site carries the integer bond
imbalance

```text
(3n)_μ = o_{+μ} − o_{-μ} ∈ Z,
```

equivalently `n_μ = (o_{+μ} − o_{-μ}) / 3`. Locked sites stay locked. An
unread patch site forms if and only if `n ≠ 0`. For a forming site the
spectral integer is

```text
k = |3n|^2 ∈ Z.
```

This note stays in `Z`: it records `3n` and `k`, and it does not evaluate
one-site traces at `k=2`.

After tick 1 the locked set is

```text
{(0,0,0), (1,0,0), (0,1,0), (0,0,1)}.
```

The second-wave table on the four forming unread sites is

| site | `3n` | `k` |
|---|---|---|
| `(1,1,0)` | `(-1,-1,0)` | `2` |
| `(1,0,1)` | `(-1,0,-1)` | `2` |
| `(0,1,1)` | `(0,-1,-1)` | `2` |
| `(2,0,0)` | `(-1,0,0)` | `1` |

Those four form. Every other unread patch site has `n = 0` and does not
form. The second-wave values of `k` are exactly `{1,2}`. This is the tick-2
table. It is not the first-wave identity that every seed-neighbor lock has
`k=1`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Z identities for 3n and k=|3n|^2 on the four tick-2 forming sites of one displayed occupancy member, plus vanishing n on the remaining unread patch sites."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_second_wave_k
target_blocker_text: "spectral k at tick 2 of L1 on the two-cube patch"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied twelve-vertex patch after the displayed tick-1 lock set; L1 is displayed, not adopted; no k=2 traces"
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
  off-patch occupancy `0`, the occupancy kernel, the tick-1 lock set, and the
  integer rule `k = |3n|^2` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting this member as a physical law, lifting
  it off the supplied patch, or identifying `k` with a continuum wavenumber
  remain separate, open obligations.

## Exact Objects

All runner coefficients are exact integers. No float is used. The runner
never leaves `Z` for `3n` or `k`.

Occupancy `o(v)` is `1` on a lock in the patch and `0` otherwise, including
every off-patch neighbor. The vector `3n` is a triple in `Z^3`. Locked sites
are not re-tested for formation.

The four first-wave locks are used only as the tick-1 configuration from
which tick-2 `n` is read. Their own first-wave `k=1` identity is not the
claim of this note.

## Exact Target And Proof Obligations

The exact target is to evaluate `3n` and `k` at every unread patch site after
tick 1, and to check the second-wave table by exact integer arithmetic.

The obligation graph is:

1. the patch has twelve vertices;
2. the same occupancy kernel that forms the three on-patch axis neighbors
   from the seed produces the tick-1 lock set
   `{(0,0,0),(1,0,0),(0,1,0),(0,0,1)}`;
3. at that configuration the four sites `(1,1,0)`, `(1,0,1)`, `(0,1,1)`,
   `(2,0,0)` have the displayed `3n` and `k`;
4. those four are unread and have `n ≠ 0`, so they form;
5. every other unread patch site has `n = 0`, so it does not form.

All five obligations are closed below and in the runner. There is no missing
lemma for this bounded display.

## Theorem 1 — tick-1 lock set on the twelve-vertex patch

`A` has eight vertices with coordinates in `{0,1}^3`. `B` has eight vertices
with `x ∈ {1,2}` and `y,z ∈ {0,1}`. The union has twelve sites, all in
`Z^3`. Off-patch occupancy is the supplied value `0`.

Start with locks `{(0,0,0)}`. The three on-patch axis neighbors have
`3n ≠ 0` and form. Every other unread patch site has vanishing neighbor
occupancy on the seed, hence `n = 0`. After that step the locked set is

```text
{(0,0,0), (1,0,0), (0,1,0), (0,0,1)}.
```

The remainder of the note takes this lock set as the tick-1 configuration.

## Theorem 2 — second-wave `3n` and `k`

Occupancy is `1` on the four tick-1 locks and `0` elsewhere. Nearest-neighbor
occupancies at the four unread sites of the table are:

```text
(1,1,0):  o_{-x}=1, o_{-y}=1, else 0  ⇒  3n = (-1,-1,0),  k = 1+1+0 = 2
(1,0,1):  o_{-x}=1, o_{-z}=1, else 0  ⇒  3n = (-1, 0,-1),  k = 1+0+1 = 2
(0,1,1):  o_{-y}=1, o_{-z}=1, else 0  ⇒  3n = ( 0,-1,-1),  k = 0+1+1 = 2
(2,0,0):  o_{-x}=1,           else 0  ⇒  3n = (-1, 0, 0),  k = 1+0+0 = 1
```

Each of these four sites lies in the twelve-vertex set, is unread, and has
`n ≠ 0`, so each forms. The four values of `k` are exactly `{1,2}`.

## Theorem 3 — no other unread patch site has `n ≠ 0`

The unread patch sites after tick 1 that are not in the table are

```text
(1,1,1), (2,1,0), (2,0,1), (2,1,1).
```

At each of these four sites every on-patch neighbor is still unread and
every off-patch neighbor has occupancy `0`, so `3n = (0,0,0)` and `n = 0`.
They do not form.

The four tick-1 locks stay locked and are not new formations. Therefore the
tick-2 formation set is exactly the four-site table, and `k` on that set is
exactly the displayed integers.

## Physical-Interpretation Boundary

The proved output is the tick-2 `k` table of the displayed member on the
supplied patch. This note does not adopt `L1` as axiom content and does not
rewrite Qubit. The one-site algebra remains `M_2(C)`. The integer `k` is
`|3n|^2` at a forming site. It is not a one-site trace and it is not a
continuum wavenumber.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. second-wave `k` is not uniformly `1`: three of the four forming sites have
   `k=2`;
2. `(2,0,0)` has `k=1`, distinct from the three face-diagonal values `k=2`;
3. `k` is the integer `|3n|^2`, not a one-site trace.

## What This Does Not Claim

- `L1` is displayed, not adopted.
- No inverse-square rule is claimed.
- Qubit remains `M_2(C)`.
- The occupancy kernel is not a Lattice map.
- This is the tick-2 table, not the first-wave `k=1` identity.
- No one-site traces are evaluated at `k=2`.
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
the patch, the occupancy kernel, the tick-1 lock set, and the integer rule
`k = |3n|^2`.

## Runner Contract

The companion runner identity-gates every helper and recomputes `3n` and `k`
from occupancy at every unread patch site after tick 1. It checks the four
forming sites against the displayed table, checks that every other unread
patch site has `n = 0`, quotes the four live axiom sentences, and records the
import boundary. Declared review inputs are this note and the axiom memo
only.
