---
claim_id: two_cube_l1_two_tick_composition_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied twelve-vertex two-cube patch, two successive ticks of the displayed member L1 compose: tick-1 locks remain locked, the formation-count clock adds, the empty configuration is a fixed point, and the occupancy tree gauge still holds. Tick-1 traces stay in Q; tick-2 k=2 sites are k-checked only. L1 is displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_two_tick_composition_2026_08_14.py
---

# Two-Cube `L1` Two-Tick Composition

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact two-tick composition of one displayed member `L1` on a
supplied twelve-vertex two-cube patch. The same kernel is reused; the new
object is the composed time, not a new patch. `L1` is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_two_tick_composition_2026_08_14.py`](../scripts/two_cube_l1_two_tick_composition_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work on the finite vertex set of two unit cubes that share a face:

```text
A = [0,1]^3,     B = [1,2] x [0,1] x [0,1].
```

The twelve vertices are the union of the eight vertices of `A` and the eight
vertices of `B`. Occupancy off this patch is `0`.

`L1` is reconstructed locally as one map. An unread site carries the occupancy
kernel

```text
n_μ = (o_{+μ} − o_{-μ}) / 3.
```

Locked sites stay locked. An unread patch site forms if and only if `n ≠ 0`.
For a forming site, `k = |3n|^2` is an integer in `{1,2,3}`. Tick 1 has `k=1`,
so the one-site traces in `Q` are `2/3` and `1/3`. Tick 2 has `k=2` sites;
those traces are not forced into `Q`. The runner checks `k` at tick 2 and
records a `Q` trace only at the remaining `k=1` site.

The clock `F` starts at `0` and adds the number of new locks. Cube source and
face flux are functions of occupancy:

```text
ρ(C) = ∑_{v ∈ C} o(v),
φ(F*) = ρ(A),
φ(F_B) = ρ(A) + ρ(B).
```

Seed `{(0,0,0)}`.

**Tick 1.** New locks: `(1,0,0)`, `(0,1,0)`, `(0,0,1)`. `F: 0 → 3`.
`ρ(A)=4`, `ρ(B)=1`, `φ(F*)=4`, `φ(F_B)=5`. Each new lock has `k=1` and traces
`2/3`, `1/3`.

**Tick 2.** New locks: `(1,1,0)`, `(1,0,1)`, `(0,1,1)`, `(2,0,0)`. The three
tick-1 locks stay locked. `F: 3 → 7`. `ρ(A)=7`, `ρ(B)=4`, `φ(F*)=7`,
`φ(F_B)=11`. The first three new sites have `k=2`; `(2,0,0)` has `k=1`.

Two successive `step_L1` calls are the composition. The composed object is
the same kernel at a later clock, not a new occupancy patch.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Z/Q identities for two composed ticks of one displayed occupancy-clock-flux member on a supplied twelve-vertex patch."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_two_tick_composition
target_blocker_text: "whether two ticks of L1 compose with permanence, clock additivity, empty fixed point, and tree gauge"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied twelve-vertex patch; tick-2 k=2 traces are not claimed in Q; L1 is displayed, not adopted"
hypothetical_axiom_status: no edit
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live axiom memo named above. No map in this
  note is named as a Lattice map. Qubit is not rewritten.
- **Explicit theorem-domain condition:** the twelve-vertex two-cube patch,
  off-patch occupancy `0`, the occupancy kernel, the formation-count clock,
  the occupancy functions `ρ/φ`, and the two-tick seed history are supplied
  mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting this member as a physical law, lifting
  it off the supplied patch, or identifying `ρ/φ` with a continuum source
  remain separate, open obligations.

## Exact Objects

All runner coefficients are exact integers or `Fraction` values. No float is
used. Tick-1 traces stay in `Q` because those sites have `k=1`. Tick-2 `k=2`
sites are excluded from the `Q` trace check.

Occupancy `o(v)` is `1` on a lock in the patch and `0` otherwise, including
every off-patch neighbor. The kernel `n` is a triple in `Q^3`. Locked sites
are not re-tested for formation.

`ρ` and `φ` are functions of occupancy on the supplied cells. They are not a
continuum field.

## Exact Target And Proof Obligations

The exact target is to apply `step_L1` twice from the seed and to check the
composed tuple by exact arithmetic.

The obligation graph is:

1. tick-1 output matches the first-wave locks, clock `3`, and tree-gauge
   values `4,1,4,5`;
2. every tick-1 lock remains locked after tick 2;
3. `F_2 = F_1 + |new_2|`, hence `7 = 3 + 4`;
4. the empty configuration is a fixed point of `step_L1`, checked on a
   separate snapshot;
5. after both ticks, `φ(F*)=ρ(A)=7` and `φ(F_B)=ρ(A)+ρ(B)=11`.

All five obligations are closed below and in the runner. There is no missing
lemma for this bounded display.

## Theorem 1 — permanence of tick-1 locks

After tick 1 the locks are

```text
{(0,0,0), (1,0,0), (0,1,0), (0,0,1)}.
```

Locked sites stay. Tick 2 therefore cannot drop any of those four sites. After
tick 2 the locks are

```text
{(0,0,0), (1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1), (2,0,0)}.
```

The tick-1 set is a subset. Permanence is this inclusion, not a new lock rule.

## Theorem 2 — clock additivity

`F` starts at `0`. Tick 1 adds the three first-wave locks, so `F_1 = 3`.
Tick 2 adds four new locks, so

```text
F_2 = F_1 + |new_2| = 3 + 4 = 7.
```

The composed clock is the sum of the two ticks. It is not a reset and it is
not the seed-inclusive lock count at tick 1.

## Theorem 3 — empty is a fixed point

On a separate snapshot with no locks and clock `0`, every neighbor occupancy
is `0`, so `n = 0` at every patch site. No site forms. `step_L1` returns the
empty lock set, clock `0`, vanishing `ρ/φ`, and an empty `k` map. A second
tick on that output is again empty. The seed is initial data, not this
snapshot.

## Theorem 4 — tree gauge after both ticks

The identities `φ(F*)=ρ(A)` and `φ(F_B)=ρ(A)+ρ(B)` are the same occupancy
functions after each tick.

After tick 1 the four occupied sites all lie in `A` and only `(1,0,0)` lies
in `B`, so `ρ(A)=4`, `ρ(B)=1`, `φ(F*)=4`, `φ(F_B)=5`.

After tick 2 seven occupied sites lie in `A` and four lie in `B`, so
`ρ(A)=7`, `ρ(B)=4`, `φ(F*)=7`, `φ(F_B)=11`.

These values are not occupancy sums on the face vertices alone. After two
ticks the shared-face occupancy sum is `3` and the outer-face occupancy sum
is `1`; those face sums are not `φ`.

## Tick-1 traces and tick-2 `k`

At each first-wave site after the seed, `k=1`. The traces in `Q` are

```text
Tr(ρ P+) = 2/3,     Tr(ρ P−) = 1/3.
```

Their sum is `1`.

At tick 2, the unread sites `(1,1,0)`, `(1,0,1)`, and `(0,1,1)` each have two
nonzero axis components of `n`, hence `k=2`. The site `(2,0,0)` has `k=1`.
The runner checks those four integers. It does not place the `k=2` traces in
`Q`.

No other unread patch site has `n ≠ 0` after tick 1.

## Physical-Interpretation Boundary

The proved output is two composed ticks of the displayed member on the
supplied patch. This note does not adopt `L1` as axiom content and does not
rewrite Qubit. The one-site algebra remains `M_2(C)`. The symbols `ρ` and `φ`
remain functions of occupancy.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. the composed clock `7` is the sum of ticks, not a lock-count reset;
2. `φ(F*)` after two ticks is not the occupancy sum on `F*`;
3. `φ(F_B)` after two ticks is not the occupancy sum on `F_B`.

## What This Does Not Claim

- `L1` is displayed, not adopted.
- Two ticks are a composed history of the same kernel, not a new patch.
- Tick-2 `k=2` traces are not claimed in `Q`.
- Qubit remains `M_2(C)`.
- `ρ/φ` are functions of occupancy.
- The occupancy kernel is not a Lattice map.
- The two-tick identities are not a continuum lift and not a physical
  selection of this member.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Runner Contract

The companion runner reconstructs `L1` locally and identity-gates the helpers.
It applies two ticks from the seed, checks permanence, clock additivity, the
empty fixed point on a separate snapshot, and the tree gauge after both ticks.
Tick-1 traces are checked in `Q`. Tick-2 `k=2` sites are `k`-checked only.
Declared review inputs are this note and the axiom memo only.
